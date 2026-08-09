# ClaudeCodeIPTool - Quick Start Guide

## Setup (30 seconds)

```bash
cd ~/VDT/tools/ClaudeCodeIPTool

# Install Scapy (if not already installed)
pip install scapy

# Test installation
python3 -c "from scapy.all import *; print('✓ Scapy installed')"

# Make scripts executable
chmod +x *.py
```

---

## Test 1: Verify Spoofing Works (Your Network)

```bash
# IMPORTANT: Run WITHOUT VPN connected
# Mullvad blocks spoofing (BCP 38 compliance)

# Test if you can send spoofed packets
sudo python3 ghostport.py test-spoof 127.0.0.1 --spoof 8.8.8.8

# If loopback works, test external (requires target you control)
sudo python3 ghostport.py test-spoof <your_controlled_server> --spoof 8.8.8.8

# On controlled server, verify:
# sudo tcpdump -i any icmp and src 8.8.8.8
```

**Expected Result:**
- ✓ Packets arrive → Spoofing works (ISP has no BCP 38)
- ✗ No packets → ISP blocks spoofing (good security, can't test tools)

---

## Test 2: Reflection Scanner (Working Tool)

```bash
# List available service probes
python3 spoof-scanner.py list-services

# Scan controlled target for DNS/NTP reflection
sudo python3 spoof-scanner.py scan \
    --targets <your_controlled_server> \
    --spoof 1.1.1.1 \
    --services dns,ntp

# Full scan of multiple targets
sudo python3 spoof-scanner.py scan \
    --targets ips.txt \
    --spoof 8.8.8.8 \
    --output results.json
```

**What it finds:**
- Open DNS resolvers (amplification: 28x)
- NTP servers with monlist (amplification: 556x)
- Memcached exposed (amplification: 51,000x)
- Other reflection services

---

## Test 3: GhostPort Stealth Scanner (Novel)

```bash
# Scan without your IP touching target
sudo python3 ghostport.py scan 192.168.1.100 \
    --victim 8.8.8.8 \
    --ports 80,443,22,3389 \
    --method timing

# Scan port range
sudo python3 ghostport.py scan 192.168.1.100 \
    --victim 8.8.8.8 \
    --ports 1-1024 \
    --method passive

# Target logs show 8.8.8.8 as scanner, NOT your IP
```

**Attack Surface:**
- Target believes victim IP is scanning
- Your IP never appears in logs
- Attribution evasion demonstration

---

## Test 4: Spoof Detection (Defensive)

```bash
# Detect spoofed packets via TTL analysis
python3 spoofer.py demo 127.0.0.1

# Or use directly:
python3 -c "
from spoofer import SpoofDetector
detector = SpoofDetector(threshold=5)
result = detector.check_ttl('8.8.8.8', 13)  # Suspicious TTL
print(result)
"
```

**H.D. Moore Technique:**
- Compares observed TTL vs expected hop count
- TTL mismatch = likely spoofed
- Used to defend Pentagon (1999)

---

## Controlled Lab Setup (Recommended)

### 3-Host Configuration

```
Network: 192.168.56.0/24 (VirtualBox Host-Only)

┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Attacker   │         │    Target    │         │    Victim    │
│ 192.168.56.10│────────>│192.168.56.100│<────────│192.168.56.20 │
└──────────────┘         └──────────────┘         └──────────────┘
  Runs toolkit            Receives spoofed         Appears in logs
                          packets from Victim
```

**Setup:**
```bash
# On all 3 VMs:
sudo sysctl -w net.ipv4.conf.all.rp_filter=0     # Disable uRPF
sudo sysctl -w net.ipv4.conf.default.rp_filter=0

# On Attacker:
cd ~/VDT/tools/ClaudeCodeIPTool
sudo python3 ghostport.py scan 192.168.56.100 \
    --victim 192.168.56.20 \
    --ports 22,80,443 \
    --method passive

# On Victim (monitor):
sudo tcpdump -i any src 192.168.56.100

# On Target (verify logs show Victim, not Attacker):
sudo tail -f /var/log/syslog | grep 192.168.56.20
```

---

## Common Use Cases

### 1. DDoS Amplification Research

```bash
# Find open DNS resolvers
sudo python3 spoof-scanner.py scan \
    --targets dns-servers.txt \
    --spoof 8.8.8.8 \
    --services dns \
    --output dns-amplifiers.json

# Identify high-risk services (NTP, Memcached)
sudo python3 spoof-scanner.py scan \
    --targets servers.txt \
    --spoof 1.1.1.1 \
    --services ntp,memcached
```

### 2. BCP 38 Compliance Testing

```bash
# Test your network
sudo python3 spoof-scanner.py test-bcp38 \
    <your_server> \
    --victim 8.8.8.8

# Test customer networks (authorized)
for network in customer_nets.txt; do
    sudo python3 spoof-scanner.py test-bcp38 $network --victim 1.1.1.1
done
```

### 3. Incident Response (Detect Spoofing)

```bash
# Captured packet shows src=8.8.8.8 with TTL=13
python3 -c "
from spoofer import SpoofDetector
d = SpoofDetector()
is_spoofed, expected, diff = d.check_ttl('8.8.8.8', 13)
print(f'Spoofed: {is_spoofed}, Expected TTL: {expected}, Diff: {diff}')
"
```

---

## Integration with VDT Workflow

### Pre-Assessment

```bash
# 1. Test BCP 38 status
sudo python3 ghostport.py test-spoof <target> --spoof 8.8.8.8

# 2. If spoofing works, proceed with reflection scan
sudo python3 spoof-scanner.py scan --targets <target> --spoof <victim>
```

### During Assessment

```bash
# Add to arsenal chain (after aimap, before verify)
sudo python3 spoof-scanner.py scan \
    --targets lane-a/ips.txt \
    --spoof 1.1.1.1 \
    --output ~/VDT/assessments/<category>/reflection-scan.json
```

### Post-Assessment

```bash
# Generate findings
cat reflection-scan.json | jq '.results[] | select(.responsive==true)'

# Add to VULNERABILITIES-<ip>.md
# F<n>: Reflection Amplification - <service> (CRITICAL)
```

---

## Troubleshooting

### "Permission denied" / "Operation not permitted"

```bash
# Need root for raw sockets
sudo python3 spoof-scanner.py scan ...

# OR grant CAP_NET_RAW capability
sudo setcap cap_net_raw=eip $(which python3)
```

### "No packets arriving at target"

**Causes:**
1. BCP 38 / uRPF active (ISP blocks spoofing)
2. VPN connected (Mullvad blocks spoofing)
3. Firewall dropping packets

**Fix:**
- Disconnect VPN
- Test on direct connection
- Use lab network

### "Scapy import error"

```bash
pip install scapy

# If system Python:
sudo pip install scapy

# Verify:
python3 -c "from scapy.all import *"
```

---

## Next Steps

1. **Read the Books** (~/VDT/books/)
   - Violent Python Ch4 (TTL detection)
   - Python for Security Ch5 (Scapy)
   - Network Security Hacks (ARP spoofing)

2. **Run Controlled Tests**
   - Set up 3-VM lab
   - Test all 5 spoofing techniques
   - Verify defensive detection works

3. **Add to VDT Arsenal**
   - Integrate into assessment workflow
   - Document findings in VULNERABILITIES-*.md
   - Generate SKILLS-*.md from results

4. **Defensive Hardening**
   - Test your networks for BCP 38 compliance
   - Implement TTL-based spoof detection
   - Deploy service-level mitigations (DNS RRL, etc.)

---

## OPSEC Reminder

**VDT Baseline v2.1:**
- ✓ Controlled environments / owned infrastructure
- ✓ Authorized penetration tests
- ✓ Defensive research / purple team exercises
- ✗ Unauthorized scanning
- ✗ DDoS attacks
- ✗ Attribution evasion for malicious purposes

**These tools demonstrate attack primitives to BUILD BETTER DEFENSES.**
