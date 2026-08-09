#!/usr/bin/env python3
"""
Defense Detector - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defensive tools to detect spoofing attacks on YOUR network.

Detects:
- ARP spoofing attacks
- DNS spoofing attempts
- Network anomalies
- MITM activity
- Suspicious traffic patterns

Use to DEFEND against attacks demonstrated by other tools.

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import time
from collections import defaultdict
from scapy.all import (
    ARP, DNS, DNSRR, IP, sniff, conf, get_if_hwaddr
)

conf.verb = 0


class ARPSpoofDetector:
    """Detect ARP cache poisoning attacks"""

    def __init__(self, interface=None, verbose=False):
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.arp_table = {}  # IP → MAC mapping
        self.alerts = []

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["ALERT", "ATTACK"]:
            prefix = {
                "ATTACK": "[🚨]",
                "ALERT": "[⚠]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def process_arp(self, pkt):
        """Analyze ARP packet for spoofing"""
        if not pkt.haslayer(ARP):
            return

        arp_src_ip = pkt[ARP].psrc
        arp_src_mac = pkt[ARP].hwsrc

        # Check if we've seen this IP before
        if arp_src_ip in self.arp_table:
            known_mac = self.arp_table[arp_src_ip]

            # MAC address changed for same IP → ARP spoofing!
            if known_mac != arp_src_mac:
                alert = {
                    'type': 'ARP_SPOOF',
                    'ip': arp_src_ip,
                    'old_mac': known_mac,
                    'new_mac': arp_src_mac,
                    'time': time.time()
                }
                self.alerts.append(alert)

                self.log(f"ARP SPOOFING DETECTED!", "ATTACK")
                self.log(f"  IP: {arp_src_ip}", "ATTACK")
                self.log(f"  Known MAC: {known_mac}", "ATTACK")
                self.log(f"  New MAC: {arp_src_mac} (SUSPICIOUS)", "ATTACK")
                self.log(f"  Possible attacker MAC: {arp_src_mac}", "ATTACK")
                print()
        else:
            # Learn new IP → MAC mapping
            self.arp_table[arp_src_ip] = arp_src_mac
            if self.verbose:
                self.log(f"Learned: {arp_src_ip} → {arp_src_mac}", "INFO")

    def start(self):
        """Start ARP spoof detection"""
        self.log(f"ARP spoof detector started on {self.interface}", "INFO")
        self.log(f"Our MAC: {get_if_hwaddr(self.interface)}", "INFO")
        self.log("Monitoring for ARP cache poisoning...", "INFO")
        print()

        try:
            sniff(
                iface=self.interface,
                prn=self.process_arp,
                filter="arp",
                store=0
            )
        except KeyboardInterrupt:
            self.show_summary()

    def show_summary(self):
        """Show detection summary"""
        print("\n" + "=" * 70)
        print("DETECTION SUMMARY")
        print("=" * 70)
        print(f"ARP spoofing attacks detected: {len(self.alerts)}")

        if self.alerts:
            print("\nATTACK DETAILS:")
            for i, alert in enumerate(self.alerts, 1):
                print(f"\n[{i}] ARP Spoof")
                print(f"    Target IP: {alert['ip']}")
                print(f"    Legitimate MAC: {alert['old_mac']}")
                print(f"    Attacker MAC: {alert['new_mac']}")

        print("=" * 70 + "\n")


class DNSSpoofDetector:
    """Detect DNS spoofing/poisoning"""

    def __init__(self, interface=None, verbose=False):
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.dns_responses = defaultdict(list)  # domain → [IPs]
        self.alerts = []

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["ALERT", "ATTACK"]:
            prefix = {
                "ATTACK": "[🚨]",
                "ALERT": "[⚠]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def process_dns(self, pkt):
        """Analyze DNS responses for spoofing"""
        if not pkt.haslayer(DNS) or not pkt.haslayer(DNSRR):
            return

        domain = pkt[DNS].qd.qname.decode('utf-8').rstrip('.')
        response_ip = pkt[DNSRR].rdata

        # Check for inconsistent responses
        if domain in self.dns_responses:
            known_ips = self.dns_responses[domain]

            if response_ip not in known_ips:
                alert = {
                    'type': 'DNS_SPOOF',
                    'domain': domain,
                    'known_ips': known_ips,
                    'new_ip': response_ip,
                    'time': time.time()
                }
                self.alerts.append(alert)

                self.log(f"DNS SPOOFING DETECTED!", "ATTACK")
                self.log(f"  Domain: {domain}", "ATTACK")
                self.log(f"  Known IPs: {known_ips}", "ATTACK")
                self.log(f"  New IP: {response_ip} (SUSPICIOUS)", "ATTACK")
                print()

        self.dns_responses[domain].append(response_ip)

    def start(self):
        """Start DNS spoof detection"""
        self.log(f"DNS spoof detector started on {self.interface}", "INFO")
        self.log("Monitoring for DNS poisoning...", "INFO")
        print()

        try:
            sniff(
                iface=self.interface,
                prn=self.process_dns,
                filter="udp port 53",
                store=0
            )
        except KeyboardInterrupt:
            self.show_summary()

    def show_summary(self):
        """Show detection summary"""
        print("\n" + "=" * 70)
        print("DETECTION SUMMARY")
        print("=" * 70)
        print(f"DNS spoofing attacks detected: {len(self.alerts)}")

        if self.alerts:
            print("\nATTACK DETAILS:")
            for i, alert in enumerate(self.alerts, 1):
                print(f"\n[{i}] DNS Spoof")
                print(f"    Domain: {alert['domain']}")
                print(f"    Legitimate IPs: {alert['known_ips']}")
                print(f"    Spoofed IP: {alert['new_ip']}")

        print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Defense Detector - Detect spoofing attacks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Detect ARP spoofing attacks
  sudo python3 defense-detector.py arp

  # Detect DNS spoofing attacks
  sudo python3 defense-detector.py dns

  # Verbose mode (see all traffic)
  sudo python3 defense-detector.py arp -v

Detection Methods:
  ARP Spoofing:
    - Monitors ARP traffic
    - Learns legitimate IP → MAC mappings
    - Alerts when MAC changes for same IP (spoofing indicator)

  DNS Spoofing:
    - Monitors DNS responses
    - Tracks domain → IP mappings
    - Alerts when domain resolves to different IP (poisoning indicator)

Defensive Use:
  Run on YOUR network to detect if you're under attack.
  Identifies attacker's MAC address for blocking.

CONTROLLED ENVIRONMENT ONLY
        """
    )

    subparsers = parser.add_subparsers(dest='mode', help='Detection mode')

    # ARP detection
    arp_parser = subparsers.add_parser('arp', help='Detect ARP spoofing')
    arp_parser.add_argument('--interface', help='Network interface')
    arp_parser.add_argument('-v', '--verbose', action='store_true')

    # DNS detection
    dns_parser = subparsers.add_parser('dns', help='Detect DNS spoofing')
    dns_parser.add_argument('--interface', help='Network interface')
    dns_parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if args.mode == 'arp':
        detector = ARPSpoofDetector(args.interface, args.verbose)
        detector.start()

    elif args.mode == 'dns':
        detector = DNSSpoofDetector(args.interface, args.verbose)
        detector.start()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
