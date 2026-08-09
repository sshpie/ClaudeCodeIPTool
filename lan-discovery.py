#!/usr/bin/env python3
"""
LAN Discovery & Auto-Targeting - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatically discover all devices on local network.
Map network topology, identify targets, launch attacks.

Features:
- ARP scan (find all hosts)
- Port scan (identify services)
- OS fingerprinting
- Auto-target selection
- Attack chain orchestration

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import subprocess
import json
from scapy.all import (
    ARP, Ether, IP, TCP, ICMP, srp, sr1, conf, RandShort
)

conf.verb = 0


class LANDiscovery:
    """Automated LAN reconnaissance and targeting"""

    def __init__(self, network="192.168.1.0/24", interface=None, verbose=False):
        self.network = network
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.hosts = []

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["FOUND", "RESULT"]:
            prefix = {
                "FOUND": "[🎯]",
                "RESULT": "[+]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def arp_scan(self):
        """Discover all hosts via ARP scan"""
        self.log(f"ARP scanning {self.network}", "INFO")

        ans, _ = srp(
            Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=self.network),
            timeout=3,
            verbose=0,
            iface=self.interface
        )

        for snd, rcv in ans:
            host = {
                'ip': rcv.psrc,
                'mac': rcv.hwsrc,
                'ports': [],
                'os': None
            }
            self.hosts.append(host)
            self.log(f"Found: {rcv.psrc} ({rcv.hwsrc})", "FOUND")

        self.log(f"Discovered {len(self.hosts)} hosts", "RESULT")
        return self.hosts

    def port_scan(self, target_ip, ports=[22, 80, 443, 445, 3389]):
        """Quick port scan on target"""
        open_ports = []

        for port in ports:
            pkt = IP(dst=target_ip) / TCP(sport=RandShort(), dport=port, flags="S")
            resp = sr1(pkt, timeout=1, verbose=0)

            if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:  # SYN-ACK
                open_ports.append(port)
                # Send RST to close
                rst = IP(dst=target_ip) / TCP(sport=pkt[TCP].sport, dport=port,
                                               flags="R", seq=resp[TCP].ack)
                sr1(rst, timeout=1, verbose=0)

        return open_ports

    def os_fingerprint(self, target_ip):
        """Basic OS fingerprinting via TTL"""
        pkt = IP(dst=target_ip) / ICMP()
        resp = sr1(pkt, timeout=2, verbose=0)

        if not resp:
            return "Unknown (no ICMP response)"

        ttl = resp[IP].ttl

        # TTL-based OS detection
        if ttl <= 64:
            return "Linux/Unix"
        elif ttl <= 128:
            return "Windows"
        elif ttl <= 255:
            return "Network device (router/switch)"
        else:
            return "Unknown"

    def scan_all(self):
        """Full network scan: discovery + port scan + OS fingerprint"""
        self.arp_scan()

        self.log("Performing port scans and OS fingerprinting...", "INFO")

        for host in self.hosts:
            ip = host['ip']

            # Port scan
            host['ports'] = self.port_scan(ip)

            # OS fingerprint
            host['os'] = self.os_fingerprint(ip)

            if host['ports']:
                self.log(f"{ip}: {host['os']} | Ports: {host['ports']}", "FOUND")

        return self.hosts

    def export_json(self, filename):
        """Export results to JSON"""
        with open(filename, 'w') as f:
            json.dump(self.hosts, f, indent=2)
        self.log(f"Exported to {filename}", "RESULT")

    def suggest_targets(self):
        """Suggest best targets for attack"""
        print("\n" + "=" * 70)
        print("SUGGESTED TARGETS")
        print("=" * 70)

        # High-value targets
        print("\nHigh-Value Targets (servers/workstations):")
        for host in self.hosts:
            if host['ports']:
                print(f"  {host['ip']}")
                print(f"    OS: {host['os']}")
                print(f"    Open ports: {host['ports']}")

                # Suggest attacks
                if 80 in host['ports'] or 443 in host['ports']:
                    print(f"    → DNS spoof: Redirect web traffic")
                if 445 in host['ports']:
                    print(f"    → SMB relay attack")
                if 22 in host['ports']:
                    print(f"    → SSH credential capture")
                print()

        # Gateway (usually .1)
        gateways = [h for h in self.hosts if h['ip'].endswith('.1')]
        if gateways:
            print("\nGateway Target (for full network MITM):")
            for gw in gateways:
                print(f"  {gw['ip']} - Spoof this to intercept ALL traffic")
                print(f"    sudo python3 arp-spoof.py spoof <target> --spoof-ip {gw['ip']}")

        print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="LAN Discovery & Auto-Targeting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic network scan
  sudo python3 lan-discovery.py

  # Scan specific network
  sudo python3 lan-discovery.py --network 10.0.0.0/24

  # Full scan with JSON export
  sudo python3 lan-discovery.py --full --output lan-hosts.json

  # Get attack suggestions
  sudo python3 lan-discovery.py --suggest

Attack Chain Integration:
  1. Discover targets:
     sudo python3 lan-discovery.py --suggest

  2. Pick target from suggestions

  3. Launch attack:
     sudo python3 arp-spoof.py spoof <target> --spoof-ip <gateway>
     sudo python3 dns-spoof.py --domain "*" --ip <your_ip>

CONTROLLED ENVIRONMENT ONLY
        """
    )

    parser.add_argument('--network', default='192.168.1.0/24',
                       help='Network to scan (default: 192.168.1.0/24)')
    parser.add_argument('--interface', help='Network interface')
    parser.add_argument('--full', action='store_true',
                       help='Full scan (port scan + OS fingerprint)')
    parser.add_argument('--suggest', action='store_true',
                       help='Suggest attack targets')
    parser.add_argument('--output', help='Export results to JSON')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    scanner = LANDiscovery(args.network, args.interface, args.verbose)

    if args.full:
        scanner.scan_all()
    else:
        scanner.arp_scan()

    if args.suggest:
        scanner.suggest_targets()

    if args.output:
        scanner.export_json(args.output)


if __name__ == "__main__":
    main()
