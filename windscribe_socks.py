#!/usr/bin/env python3
"""
windscribe_socks.py — Route sessions through Windscribe SOCKS5 proxy

Windscribe creates a SOCKS5 proxy at localhost:1080 when connected.
Combines with session_replay.py for full proxy+Chrome-impersonate chain.

Usage:
  python3 windscribe_socks.py status                      # proxy status + exit IP/ASN
  python3 windscribe_socks.py probe https://admin.google.com/
  python3 windscribe_socks.py chain --cookies cookies.txt --url https://admin.google.com/
  python3 windscribe_socks.py find-location --asn AS7843   # find exit matching target ASN
"""

import argparse
import json
import subprocess
import sys
import socket
from urllib.parse import urlparse

try:
    from curl_cffi import requests as cffi_requests
except ImportError:
    print("[ERROR] pip install curl_cffi", file=sys.stderr)
    sys.exit(1)

try:
    import socks
    HAS_SOCKS = True
except ImportError:
    HAS_SOCKS = False


SOCKS5_PROXY = "socks5://127.0.0.1:1080"
HTTP_PROXY = "http://127.0.0.1:8888"   # Windscribe also exposes an HTTP proxy

CHROME_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
}

IP_INFO_URLS = [
    "https://ipinfo.io/json",
    "https://ipapi.co/json",
]


def check_socks5(host="127.0.0.1", port=1080) -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False


def get_exit_ip(proxy: str | None = None, impersonate: str = "chrome120") -> dict:
    """Get exit IP and ASN info."""
    session = cffi_requests.Session(impersonate=impersonate)
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}
    for url in IP_INFO_URLS:
        try:
            resp = session.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            continue
    return {}


def windscribe_status() -> dict:
    """Get Windscribe CLI status."""
    try:
        r = subprocess.run(["windscribe", "status"], capture_output=True, text=True, timeout=5)
        return {"output": r.stdout.strip(), "rc": r.returncode}
    except FileNotFoundError:
        return {"error": "windscribe CLI not found"}


def windscribe_locations() -> list:
    """List available Windscribe locations."""
    try:
        r = subprocess.run(["windscribe", "locations"], capture_output=True, text=True, timeout=10)
        return r.stdout.strip().split("\n")
    except Exception as e:
        return [str(e)]


def windscribe_connect(location: str) -> bool:
    """Connect to a Windscribe location."""
    try:
        r = subprocess.run(["windscribe", "connect", location],
                           capture_output=True, text=True, timeout=30)
        print(r.stdout.strip())
        return r.returncode == 0
    except Exception as e:
        print(f"[!] {e}")
        return False


def load_cookies_for_url(cookie_file: str, url: str) -> dict:
    parsed = urlparse(url)
    host = parsed.hostname or ""
    cookies = {}
    with open(cookie_file) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) < 7:
                continue
            domain, _, _, _, _, name, value = parts
            d = domain.lstrip(".")
            if host == d or host.endswith("." + d):
                cookies[name] = value
    return cookies


def cmd_status(args):
    print("[*] Windscribe CLI status:")
    ws = windscribe_status()
    print(f"  {ws.get('output', ws.get('error', 'unknown'))}")

    print("\n[*] SOCKS5 proxy (localhost:1080):", end=" ")
    socks5_up = check_socks5(port=1080)
    print("UP" if socks5_up else "DOWN")
    print("[*] HTTP proxy (localhost:8888):", end=" ")
    http_up = check_socks5(port=8888)
    print("UP" if http_up else "DOWN")

    proxy = SOCKS5_PROXY if socks5_up else (HTTP_PROXY if http_up else None)

    print(f"\n[*] Direct exit IP:")
    direct = get_exit_ip(proxy=None)
    print(f"  IP:  {direct.get('ip', '?')}")
    print(f"  ASN: {direct.get('org', '?')}")
    print(f"  Loc: {direct.get('city', '?')}, {direct.get('region', '?')}")

    if proxy:
        print(f"\n[*] Exit IP via {proxy}:")
        via_proxy = get_exit_ip(proxy=proxy)
        print(f"  IP:  {via_proxy.get('ip', '?')}")
        print(f"  ASN: {via_proxy.get('org', '?')}")
        print(f"  Loc: {via_proxy.get('city', '?')}, {via_proxy.get('region', '?')}")

        direct_asn = direct.get("org", "")
        proxy_asn = via_proxy.get("org", "")
        if direct_asn != proxy_asn:
            print(f"\n[+] ASN CHANGED: {direct_asn} -> {proxy_asn}")
        else:
            print(f"\n[!] ASN unchanged — proxy exit is same AS as direct")
    else:
        print("\n[!] No proxy available — connect Windscribe first")


def cmd_probe(args):
    socks5_up = check_socks5(port=1080)
    proxy = args.proxy or (SOCKS5_PROXY if socks5_up else None)
    if not proxy:
        print("[!] No proxy — connect Windscribe or pass --proxy", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Probing {args.url} via {proxy}")
    print(f"[*] TLS impersonation: {args.impersonate}")

    s = cffi_requests.Session(impersonate=args.impersonate)
    s.proxies = {"http": proxy, "https": proxy}
    resp = s.get(args.url, headers=CHROME_HEADERS, allow_redirects=True, timeout=20)
    print(f"[+] Status: {resp.status_code}")
    print(f"[+] Final URL: {resp.url}")
    print(f"[+] Body: {len(resp.content)} bytes")
    if args.output:
        with open(args.output, "w") as f:
            f.write(resp.text)
        print(f"[+] Saved: {args.output}")
    else:
        print(resp.text[:3000])


def cmd_chain(args):
    """Full chain: proxy + Chrome TLS + session cookies."""
    socks5_up = check_socks5(port=1080)
    proxy = args.proxy or (SOCKS5_PROXY if socks5_up else None)

    print(f"[*] Chain: {'proxy=' + proxy if proxy else 'NO PROXY'} + impersonate={args.impersonate}")
    print(f"[*] URL: {args.url}")

    cookies = {}
    if args.cookies:
        cookies = load_cookies_for_url(args.cookies, args.url)
        print(f"[*] Cookies loaded: {len(cookies)}")

    s = cffi_requests.Session(impersonate=args.impersonate)
    if proxy:
        s.proxies = {"http": proxy, "https": proxy}

    resp = s.get(
        args.url,
        cookies=cookies,
        headers=CHROME_HEADERS,
        allow_redirects=True,
        timeout=25,
    )
    print(f"[+] Status: {resp.status_code}")
    print(f"[+] Final URL: {resp.url}")
    print(f"[+] Body: {len(resp.content)} bytes")

    # Auth heuristic
    final = str(resp.url)
    target_host = urlparse(args.url).netloc
    final_host = urlparse(final).netloc
    if target_host == final_host:
        print(f"[+] Auth maintained — stayed on {target_host}")
    else:
        print(f"[ ] Redirected away: {final[:80]}")

    if args.output:
        with open(args.output, "w") as f:
            f.write(resp.text)
        print(f"[+] Saved: {args.output}")
    else:
        print("\n--- RESPONSE (first 3KB) ---")
        print(resp.text[:3000])


def cmd_find_location(args):
    """Try Windscribe locations to find one matching a target ASN."""
    print(f"[*] Looking for exit matching ASN: {args.asn}")
    locations = windscribe_locations()
    print(f"[*] Available locations: {len(locations)}")

    # Filter to relevant locations (US only for residential matching)
    us_locations = [l for l in locations if any(
        x in l.lower() for x in ["us", "oregon", "portland", "seattle", "california"]
    )]
    print(f"[*] US candidates: {len(us_locations)}")
    for loc in us_locations:
        print(f"  {loc.strip()}")


def main():
    parser = argparse.ArgumentParser(description="Windscribe SOCKS5 proxy + Chrome TLS session routing")
    parser.add_argument("--proxy", default=None, help="Override proxy URL")
    parser.add_argument("--impersonate", default="chrome120",
                        help="TLS impersonation (chrome120, chrome110, safari17)")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("status", help="Show proxy and exit IP status")

    p = sub.add_parser("probe", help="Probe URL through proxy")
    p.add_argument("url", help="Target URL")
    p.add_argument("--output", help="Save response body to file")

    c = sub.add_parser("chain", help="Full chain: proxy + TLS impersonation + cookies")
    c.add_argument("--url", required=True, help="Target URL")
    c.add_argument("--cookies", help="Netscape cookie file")
    c.add_argument("--output", help="Save response body to file")

    f = sub.add_parser("find-location", help="Find Windscribe exit matching target ASN")
    f.add_argument("--asn", required=True, help="Target ASN (e.g. AS7843)")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    dispatch = {
        "status": cmd_status,
        "probe": cmd_probe,
        "chain": cmd_chain,
        "find-location": cmd_find_location,
    }
    dispatch[args.cmd](args)


if __name__ == "__main__":
    main()
