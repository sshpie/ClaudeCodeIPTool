# ClaudeCodeIPTool - VDT

Three functional tools demonstrating IP spoofing attack primitives and defenses.

## Tools

### 1. `spoofer.py` - Core IP Spoofing Techniques
Educational demonstrations of 5 spoofing primitives:
- TCP SYN flood with forged source
- UDP amplification (reflection attacks)
- ICMP redirect spoofing
- Decoy scanning (Nmap -D style)
- TTL manipulation detection evasion

**Status**: ✓ Functional (requires root/sudo)

### 2. `spoof-scanner.py` - Reflection/Amplification Reconnaissance
**WORKING TOOL** for identifying DDoS amplification vectors:
- Scans 8 reflection services (DNS, NTP, SNMP, Memcached, etc.)
- Reports amplification factors (1 byte → 51,000 bytes for Memcached)
- Tests BCP 38 / uRPF anti-spoofing controls
- Export to JSON for further analysis

**Status**: ✓ Functional (tested against controlled targets)

### 3. `ghostport.py` - Stealth Port Scanner via Spoofing
**NOVEL TECHNIQUE** - port scanning without your IP touching target:
- 4 inference methods: passive sniffing, timing side-channel, TTL differential, covert channels
- Target logs show victim IP, not attacker
- Demonstrates attribution evasion

**Status**: ✓ Functional (requires 3-host setup or sniffing capability)

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

### Spoof-Scanner (Reflection/Amplification)

```bash
# Scan single IP for all reflection services
sudo python3 spoof-scanner.py scan --targets 8.8.8.8 --spoof 1.1.1.1

# Scan specific services only
sudo python3 spoof-scanner.py scan --targets ips.txt --spoof 1.1.1.1 --services dns,ntp,memcached

# Test BCP 38 anti-spoofing
sudo python3 spoof-scanner.py test-bcp38 192.168.1.1 --victim 8.8.8.8

# Export results
sudo python3 spoof-scanner.py scan --targets ips.txt --spoof 1.1.1.1 --output results.json
```

### GhostPort (Stealth Port Scan)

```bash
# Passive method (requires sniffing)
sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443,22 --method passive

# Timing inference (no sniffing needed)
sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 80,443 --method timing

# Scan port range
sudo python3 ghostport.py scan 192.168.1.100 --victim 8.8.8.8 --ports 1-1024 --method passive

# Test if your network allows spoofing
sudo python3 ghostport.py test-spoof 192.168.1.1 --spoof 8.8.8.8
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

## TODO: Claude Code MCP Integration

Create MCP server for Claude Code integration:

```python
# ~/.claude/mcp-servers/spoof-toolkit/server.py

tools = [
    "spoof_reflection_scan",    # Wrapper for spoof-scanner.py
    "spoof_ghostport_scan",     # Wrapper for ghostport.py
    "spoof_test_bcp38",         # Test spoofing capability
    "spoof_detect_ttl"          # TTL analysis for spoof detection
]
```

**Status**: Pending implementation
