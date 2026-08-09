#!/usr/bin/env python3
"""
GhostPort - Stealthy Port Scanner via IP Spoofing + Timing Side-Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Novel Technique: Combines IP spoofing with timing analysis to discover open
ports WITHOUT sending packets from your real IP address.

Method:
1. Send spoofed SYN to Target from VictimIP
2. Target sends SYN-ACK to VictimIP (if port open) or RST (if closed)
3. Measure timing difference in VictimIP's responses to infer Target's state
4. Your real IP never touches Target — completely ghost scan

Detection Surface:
- Target sees traffic from VictimIP, not you
- IDS/IPS logs show VictimIP as scanner
- Your IP remains invisible in target logs

Defensive Value:
- Demonstrates why ingress/egress filtering (BCP 38) is critical
- Shows how attackers can frame other IPs
- Teaches timing side-channel detection

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
Requires: 3 hosts (Attacker, Victim, Target) OR 2 hosts + sniffing capability
"""

import sys
import argparse
import time
import random
from collections import defaultdict
from scapy.all import (
    IP, TCP, ICMP, Raw, send, sniff, sr1, RandShort, conf
)

conf.verb = 0


class GhostPortScanner:
    """
    Novel IP spoofing technique: Port scan via timing side-channels.

    Attack Primitive:
    ┌─────────┐         Spoofed SYN          ┌────────┐
    │ Attacker├──────(src=Victim)────────────>│ Target │
    └─────────┘                               └────┬───┘
                                                   │
        ┌─────────┐                               │
        │ Victim  │<──────SYN-ACK (open)───────────┤
        │   or    │       or RST (closed)          │
        │ Sniffer │                                 │
        └─────────┘                                 │

    Attacker infers port state by:
    - Sniffing Victim's responses (if you control Victim)
    - Timing analysis of Victim's ICMP errors
    - Monitoring Victim's network load (covert channel)

    Why This Works:
    - Target believes Victim is scanning
    - Attacker's IP never appears in Target logs
    - Useful for attribution evasion or framing
    """

    def __init__(self, target, victim_ip, attacker_iface=None, verbose=False):
        self.target = target
        self.victim_ip = victim_ip
        self.attacker_iface = attacker_iface
        self.verbose = verbose
        self.results = {}
        self.sniffer_running = False

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["RESULT", "VULN", "GHOST"]:
            timestamp = time.strftime("%H:%M:%S")
            prefix = {
                "GHOST": "[👻]",
                "VULN": "[!]",
                "RESULT": "[+]",
                "INFO": "[*]",
                "DEBUG": "[·]"
            }.get(level, "[ ]")
            print(f"[{timestamp}] {prefix} {msg}")

    def spoof_syn(self, port, custom_ttl=None):
        """
        Send spoofed SYN packet: Victim → Target

        Returns:
            None (fire-and-forget)
        """
        pkt = IP(src=self.victim_ip, dst=self.target) / \
              TCP(sport=RandShort(), dport=port, flags="S", seq=random.randint(1000, 50000))

        if custom_ttl:
            pkt[IP].ttl = custom_ttl

        self.log(f"Spoofing SYN: {self.victim_ip}:{pkt[TCP].sport} → {self.target}:{port}", "DEBUG")
        send(pkt, verbose=0, iface=self.attacker_iface)

    def passive_inference(self, port, observation_time=3):
        """
        Technique 1: Passive Inference via Sniffing Victim's Responses

        If you control Victim or can sniff its traffic:
        - Capture packets from Target → Victim after spoofed SYN
        - SYN-ACK = port open
        - RST = port closed
        - No response = filtered/dropped

        Returns:
            str: 'open', 'closed', 'filtered'
        """
        self.log(f"Passive inference on port {port} (sniffing for {observation_time}s)", "GHOST")

        # Send spoofed SYN
        self.spoof_syn(port)

        # Sniff for responses to Victim
        def packet_filter(pkt):
            return (pkt.haslayer(TCP) and
                    pkt[IP].src == self.target and
                    pkt[IP].dst == self.victim_ip and
                    pkt[TCP].sport == port)

        captured = sniff(
            filter=f"tcp and src host {self.target} and dst host {self.victim_ip}",
            timeout=observation_time,
            lfilter=packet_filter,
            iface=self.attacker_iface
        )

        # Analyze captured packets
        for pkt in captured:
            if pkt[TCP].flags == 0x12:  # SYN-ACK
                self.log(f"Port {port}: OPEN (SYN-ACK observed)", "VULN")
                return 'open'
            elif pkt[TCP].flags & 0x04:  # RST
                self.log(f"Port {port}: CLOSED (RST observed)", "DEBUG")
                return 'closed'

        self.log(f"Port {port}: FILTERED (no response)", "DEBUG")
        return 'filtered'

    def timing_inference(self, port, baseline_rtt=None):
        """
        Technique 2: Timing Side-Channel via ICMP Errors

        Theory:
        - Spoofed SYN reaches Target
        - If port open: Target sends SYN-ACK to Victim
        - If port closed: Target sends RST to Victim
        - Victim may send ICMP Port Unreachable back to Target
        - Timing difference in Victim's behavior leaks port state

        Advanced:
        - Measure Victim's response latency to our probes
        - Open port: Victim's network stack processes SYN-ACK (slight delay)
        - Closed port: Victim's network stack processes RST (faster)

        Returns:
            str: 'open', 'closed', 'unknown'
        """
        self.log(f"Timing inference on port {port}", "GHOST")

        # Establish baseline if not provided
        if baseline_rtt is None:
            baseline_rtt = self._measure_baseline_rtt()

        # Send spoofed SYN
        start = time.time()
        self.spoof_syn(port)

        # Wait for potential side-effects
        time.sleep(0.5)

        # Probe Victim to measure timing delta
        probe_rtt = self._probe_victim_rtt()
        elapsed = time.time() - start

        # Heuristic: RTT increase suggests network stack activity
        if probe_rtt and baseline_rtt:
            delta = probe_rtt - baseline_rtt
            self.log(f"RTT delta: {delta*1000:.2f}ms (baseline: {baseline_rtt*1000:.2f}ms)", "DEBUG")

            if delta > 0.01:  # >10ms increase
                self.log(f"Port {port}: Likely OPEN (RTT spike)", "VULN")
                return 'open'
            else:
                self.log(f"Port {port}: Likely CLOSED (no RTT spike)", "DEBUG")
                return 'closed'

        return 'unknown'

    def ttl_differential_analysis(self, port):
        """
        Technique 3: TTL Differential Analysis (Novel)

        Theory:
        1. Send spoofed SYN with TTL=X
        2. Target processes packet, sends response
        3. If you can sniff ANY routing point between Target → Victim,
           observe TTL of response packet
        4. Open port: SYN-ACK (larger packet, different routing)
        5. Closed port: RST (smaller packet, may route differently)

        Exploit:
        - Some networks have asymmetric routing for different packet sizes
        - TTL traces reveal internal network topology
        - Can map network paths without touching Target from your IP

        Returns:
            dict: {'state': str, 'ttl_observed': int}
        """
        self.log(f"TTL differential analysis on port {port}", "GHOST")

        # Send spoofed SYN with controlled TTL
        custom_ttl = 64
        self.spoof_syn(port, custom_ttl=custom_ttl)

        # This requires sniffing capability at intermediate hop
        # For demonstration, we note the technique
        self.log(f"Sent spoofed SYN with TTL={custom_ttl}", "DEBUG")
        self.log(f"Monitor intermediate routers to observe response TTL", "INFO")

        return {'state': 'requires_sniffing', 'ttl_sent': custom_ttl}

    def covert_channel_inference(self, port):
        """
        Technique 4: Covert Channel via Victim's Network Load (Extreme)

        Theory:
        - Spoofed SYN triggers Target to send response to Victim
        - Victim's network interface processes unexpected packet
        - Attacker with side-channel access to Victim (e.g., shared network,
          cloud co-location) can measure:
          * CPU load spikes (processing SYN-ACK vs RST)
          * Network interface queue depth
          * Cache timing (if Victim is in same CPU cache domain)

        This is a **theoretical** covert channel demonstrating extreme
        side-channel attacks. Not practical for most scenarios.

        Returns:
            str: 'covert_channel_method' (proof-of-concept)
        """
        self.log(f"Covert channel inference on port {port} (theoretical)", "GHOST")

        self.spoof_syn(port)

        self.log("Theoretical: Measure Victim's CPU/network load delta", "DEBUG")
        self.log("Practical implementation requires privileged access to Victim", "INFO")

        return 'covert_channel_method'

    def _measure_baseline_rtt(self):
        """Measure baseline RTT to Victim for timing comparison"""
        self.log(f"Measuring baseline RTT to {self.victim_ip}", "DEBUG")

        try:
            pkt = IP(dst=self.victim_ip) / ICMP()
            start = time.time()
            resp = sr1(pkt, timeout=2, verbose=0)
            rtt = time.time() - start

            if resp:
                self.log(f"Baseline RTT: {rtt*1000:.2f}ms", "DEBUG")
                return rtt
        except Exception as e:
            self.log(f"Baseline RTT measurement failed: {e}", "DEBUG")

        return None

    def _probe_victim_rtt(self):
        """Probe Victim to measure current RTT"""
        try:
            pkt = IP(dst=self.victim_ip) / ICMP()
            start = time.time()
            resp = sr1(pkt, timeout=2, verbose=0)
            rtt = time.time() - start

            if resp:
                return rtt
        except Exception:
            pass

        return None

    def scan_ports(self, ports, method='passive'):
        """
        Scan multiple ports using specified method.

        Args:
            ports: List of ports to scan
            method: 'passive', 'timing', 'ttl', 'covert'
        """
        self.log(f"Starting GhostPort scan: {len(ports)} ports", "RESULT")
        self.log(f"Target: {self.target}", "INFO")
        self.log(f"Spoofed Source: {self.victim_ip}", "INFO")
        self.log(f"Method: {method}", "INFO")
        self.log(f"Attack surface: Target logs show {self.victim_ip}, NOT your IP", "GHOST")

        print("\n" + "═" * 80)

        method_dispatch = {
            'passive': self.passive_inference,
            'timing': self.timing_inference,
            'ttl': self.ttl_differential_analysis,
            'covert': self.covert_channel_inference
        }

        scan_func = method_dispatch.get(method, self.passive_inference)

        for port in ports:
            result = scan_func(port)
            self.results[port] = result
            time.sleep(0.5)  # Rate limiting

        self.print_results()

    def print_results(self):
        """Print scan results summary"""
        print("\n" + "═" * 80)
        print("GHOSTPORT SCAN RESULTS")
        print("═" * 80)
        print(f"Target: {self.target}")
        print(f"Apparent Scanner (in Target logs): {self.victim_ip}")
        print(f"Ports Scanned: {len(self.results)}")
        print("═" * 80 + "\n")

        open_ports = [p for p, s in self.results.items() if s == 'open']
        closed_ports = [p for p, s in self.results.items() if s == 'closed']
        filtered_ports = [p for p, s in self.results.items() if s == 'filtered']

        if open_ports:
            print(f"OPEN PORTS ({len(open_ports)}):")
            print("─" * 80)
            for port in sorted(open_ports):
                print(f"  {port}/tcp - OPEN")
            print()

        if closed_ports:
            print(f"CLOSED PORTS ({len(closed_ports)}):")
            print("─" * 80)
            for port in sorted(closed_ports):
                print(f"  {port}/tcp - CLOSED")
            print()

        if filtered_ports:
            print(f"FILTERED PORTS ({len(filtered_ports)}):")
            print("─" * 80)
            for port in sorted(filtered_ports):
                print(f"  {port}/tcp - FILTERED")
            print()

        self._print_attribution_analysis()

    def _print_attribution_analysis(self):
        """Educational: Show what Target sees"""
        print("═" * 80)
        print("ATTRIBUTION ANALYSIS - What Target Sees")
        print("═" * 80)
        print(f"""
TARGET LOG VIEW:
├─ Source IP in all packets: {self.victim_ip}
├─ Your real IP: NEVER appears
├─ Target believes: {self.victim_ip} is scanning
└─ Forensic investigation would attribute attack to Victim

DEFENDER DETECTION:
├─ Ingress/Egress filtering (BCP 38/uRPF) prevents this attack
├─ TTL analysis (H.D. Moore technique) can detect spoofing
├─ Geolocation mismatch (Victim's location vs scan pattern)
└─ Behavioral analysis (Victim's normal traffic vs scan traffic)

WHY BCP 38 MATTERS:
├─ Prevents packets with spoofed source IPs from leaving network
├─ Drops packets at edge router if src IP not in customer prefix
├─ Makes this entire attack class impossible
└─ RFC 2827 / BCP 38 compliance is critical infrastructure defense
        """)
        print("═" * 80 + "\n")


class AntiSpoofValidator:
    """Validate if your network can send spoofed packets (BCP 38 test)"""

    @staticmethod
    def test_spoof_capability(target_ip, spoof_src):
        """
        Test if you can send spoofed packets from your network.

        Returns:
            bool: True if spoofing works, False if BCP 38/uRPF blocks it
        """
        print("\n" + "═" * 80)
        print("BCP 38 / uRPF CAPABILITY TEST")
        print("═" * 80)
        print(f"Testing: Can you send packets with src={spoof_src}?")
        print(f"Target: {target_ip}")
        print("═" * 80 + "\n")

        # Send spoofed ICMP echo
        pkt = IP(src=spoof_src, dst=target_ip) / ICMP()

        print(f"[*] Sending spoofed ICMP echo: {spoof_src} → {target_ip}")
        send(pkt, verbose=0)

        print(f"\n[!] MANUAL VERIFICATION REQUIRED:")
        print(f"    Run tcpdump on {target_ip}:")
        print(f"    $ sudo tcpdump -i any icmp and src {spoof_src}")
        print(f"\n    Result interpretation:")
        print(f"    ├─ Packet received → Spoofing WORKS (no BCP 38)")
        print(f"    └─ No packet → BCP 38/uRPF ACTIVE (spoofing blocked)")
        print(f"\n{'═' * 80}\n")


def main():
    parser = argparse.ArgumentParser(
        description="GhostPort - Stealthy Port Scanner via IP Spoofing + Timing Side-Channels",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Passive scan (requires sniffing capability)
  sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443,22 --method passive

  # Timing-based inference
  sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443 --method timing

  # Test if your network allows spoofing
  sudo python3 ghostport.py test-spoof 192.168.1.1 --spoof 8.8.8.8

  # Scan port range
  sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 1-1024 --method passive

Note: Requires root/sudo for raw socket access.
      CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.

Novel Contributions:
  1. Port scanning without your IP touching target
  2. Timing side-channel inference of port state
  3. TTL differential analysis for network topology mapping
  4. Attribution evasion / IP framing demonstration
        """
    )

    subparsers = parser.add_subparsers(dest='mode', help='Operating mode')

    # Scan mode
    scan_parser = subparsers.add_parser('scan', help='Ghost port scan')
    scan_parser.add_argument('target', help='Target IP address')
    scan_parser.add_argument('--victim', required=True, help='Victim IP (spoofed source)')
    scan_parser.add_argument('--ports', required=True, help='Ports (comma-separated or range: 1-1024)')
    scan_parser.add_argument('--method', choices=['passive', 'timing', 'ttl', 'covert'],
                             default='passive', help='Inference method (default: passive)')
    scan_parser.add_argument('--iface', help='Network interface for sniffing')
    scan_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    # Spoof capability test
    test_parser = subparsers.add_parser('test-spoof', help='Test if your network allows spoofing')
    test_parser.add_argument('target', help='Target IP for test')
    test_parser.add_argument('--spoof', required=True, help='Spoofed source IP to test')

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Mode dispatch
    if args.mode == 'scan':
        # Parse ports
        if '-' in args.ports:
            start, end = map(int, args.ports.split('-'))
            ports = list(range(start, end + 1))
        else:
            ports = [int(p) for p in args.ports.split(',')]

        scanner = GhostPortScanner(args.target, args.victim, args.iface, args.verbose)
        scanner.scan_ports(ports, method=args.method)

    elif args.mode == 'test-spoof':
        AntiSpoofValidator.test_spoof_capability(args.target, args.spoof)


if __name__ == "__main__":
    main()
