# VPN Considerations for ClaudeCodeIPTool

## TL;DR

**Mullvad VPN BLOCKS IP spoofing** (implements BCP 38/uRPF).

- ✗ Cannot send spoofed packets through Mullvad tunnel
- ✓ Can test spoofing on **direct connection** (bypass VPN)
- ✓ Can use toolkit for **defensive testing** regardless of VPN

---

## How VPNs Affect IP Spoofing

### What Happens

```
Normal Flow (No VPN):
┌─────────┐         Raw Packet          ┌──────────┐
│   You   ├──(src=8.8.8.8, dst=Target)──>│ ISP Edge │ → Internet
└─────────┘       (spoofed)              └──────────┘
                                          ↑
                                          May or may not filter (depends on ISP)

With VPN (e.g., Mullvad):
┌─────────┐    Encrypted Tunnel    ┌─────────┐      BCP 38 Filter      ┌──────────┐
│   You   ├────(all traffic)───────>│ Mullvad ├────────✗ BLOCKED ───────>│ Internet │
└─────────┘                         └─────────┘                         └──────────┘
                                     ↑
                                     Mullvad drops packets with src IP not in their range
```

### Why Mullvad Blocks Spoofing

1. **BCP 38 Compliance** (RFC 2827)
   - Mullvad implements strict ingress filtering
   - Drops packets where `src_ip` doesn't match customer IP allocation
   - Industry best practice for responsible VPN providers

2. **Prevents Abuse**
   - Stops customers from launching DDoS attacks via reflection
   - Prevents attribution evasion abuse
   - Protects Mullvad's reputation/IP space

3. **Security Posture**
   - Good: Mullvad prioritizes network security
   - Demonstrates proper egress filtering
   - Exactly what you'd want in production networks

---

## Testing IP Spoofing with Mullvad

### Option 1: Bypass VPN for Testing (Recommended)

```bash
# Disconnect Mullvad before testing
mullvad disconnect

# Test spoofing capability
sudo python3 ghostport.py test-spoof <target_you_control> --spoof 8.8.8.8

# On target machine, check if packets arrive:
sudo tcpdump -i any icmp and src 8.8.8.8

# Result:
# - Packets arrive → Your ISP allows spoofing (no BCP 38)
# - No packets → Your ISP blocks spoofing (BCP 38 active)

# Reconnect VPN after testing
mullvad connect
```

**Why this works:**
- Mullvad isn't in the path
- Packets go directly through your ISP
- Your home ISP **may** allow spoofing (many do, unfortunately)

### Option 2: VPN That Allows Spoofing (Not Recommended for Production)

Some VPS/dedicated server providers allow spoofing:
- Hetzner (some locations)
- OVH (some products)
- Digital Ocean (historically, now mostly blocked)

**To test:**
```bash
# SSH into VPS
ssh user@your-vps.com

# Clone toolkit
git clone <your-repo> ~/ClaudeCodeIPTool-toolkit

# Test spoofing
sudo python3 ghostport.py test-spoof <target> --spoof 8.8.8.8
```

### Option 3: Controlled Lab Network (Best for VDT)

```
┌──────────────────────────────────────────────────────┐
│  Lab Network (No BCP 38 filtering)                   │
│                                                       │
│  ┌─────────┐       ┌────────┐       ┌────────┐      │
│  │Attacker ├───────>│ Target │       │ Victim │      │
│  └─────────┘       └────────┘       └────────┘      │
│                                                       │
│  All machines controlled, spoofing allowed           │
└──────────────────────────────────────────────────────┘
```

**Setup:**
- 3 VMs (VirtualBox/VMware/KVM)
- Internal network segment (no BCP 38)
- Full control for testing

---

## Your Specific Setup (Mullvad + VDT)

### Current State
- **Mullvad connected**: IP spoofing BLOCKED
- **Direct connection**: Depends on ISP (likely allowed)

### Recommended Workflow

**For Active Spoofing Tests:**
```bash
# 1. Disconnect VPN
mullvad disconnect

# 2. Run test
sudo python3 spoof-scanner.py scan --targets <controlled_target> --spoof 8.8.8.8

# 3. Reconnect VPN
mullvad connect
```

**For Defensive Research (No Active Spoofing):**
```bash
# These work WITH VPN connected:
python3 spoof-scanner.py list-services        # No spoofing needed
python3 spoofer.py demo 127.0.0.1             # Localhost spoofing (loopback)

# TTL analysis (reads packets, doesn't send):
python3 -c "from spoofer import SpoofDetector; d = SpoofDetector(); print(d.check_ttl('8.8.8.8', 13))"
```

---

## VPN Provider Comparison

| Provider       | Allows Spoofing? | BCP 38? | Notes                          |
|----------------|------------------|---------|--------------------------------|
| Mullvad        | ✗                | ✓       | Strong BCP 38 enforcement      |
| NordVPN        | ✗                | ✓       | BCP 38 active                  |
| ExpressVPN     | ✗                | ✓       | BCP 38 active                  |
| ProtonVPN      | ✗                | ✓       | BCP 38 active                  |
| AWS/GCP/Azure  | ✗                | ✓       | Cloud providers block spoofing |
| Home ISP (US)  | Varies           | Varies  | Many allow (SHOULD block)      |
| Hetzner (some) | ✓ (some)         | ✗       | Depends on product             |
| OVH (some)     | ✓ (some)         | ✗       | Depends on product             |

---

## Detecting BCP 38 Status

### Method 1: Quick Test (No Target Needed)

```bash
# Attempt to ping with spoofed source
sudo python3 -c "
from scapy.all import *
pkt = IP(src='8.8.8.8', dst='1.1.1.1')/ICMP()
send(pkt)
print('Packet sent. Check if it left your network.')
"
```

### Method 2: Full Test (Requires Controlled Target)

```bash
# On your machine:
sudo python3 ghostport.py test-spoof <target_you_control> --spoof 8.8.8.8

# On target machine:
sudo tcpdump -i any icmp and src 8.8.8.8

# Results:
# Packets arrive → No BCP 38 (spoofing works)
# No packets → BCP 38 active (spoofing blocked)
```

### Method 3: Programmatic Check

```python
#!/usr/bin/env python3
"""Test BCP 38 enforcement"""
from scapy.all import IP, ICMP, send, sr1
import sys

def test_bcp38(target="1.1.1.1", spoof_src="8.8.8.8"):
    """
    Attempt to send spoofed ICMP packet.
    NOTE: This only tests if packet can be SENT, not if it reaches destination.
    """
    print(f"Testing BCP 38: Spoofing {spoof_src} → {target}")
    
    pkt = IP(src=spoof_src, dst=target) / ICMP()
    
    try:
        send(pkt, verbose=0)
        print("[*] Packet sent from local interface")
        print("[!] Manual verification needed on target to confirm arrival")
        print(f"    Run on {target}: sudo tcpdump icmp and src {spoof_src}")
    except Exception as e:
        print(f"[!] Failed to send: {e}")
        print("    Likely permission issue (need root) or interface error")

if __name__ == "__main__":
    test_bcp38()
```

---

## OPSEC Considerations

### With VPN (Mullvad Connected)
- ✓ Your real IP hidden
- ✗ Cannot test IP spoofing tools
- ✓ Safe for passive reconnaissance
- ✓ Use for: port scanning, service enum, web recon

### Without VPN (Direct Connection)
- ✗ Your real IP exposed
- ✓ Can test IP spoofing (if ISP allows)
- ⚠ Higher attribution risk
- ⚠ ISP may log traffic

### Recommended OPSEC

**For VDT Assessments:**
1. **Passive recon**: VPN connected (Mullvad)
2. **Active spoofing tests**: Lab network OR owned infrastructure
3. **Never**: Spoof on live 3rd-party networks (illegal, unethical)

**For Defensive Research:**
- Use localhost (127.0.0.1) targets with VPN on
- Read O'Reilly books on theory (no network needed)
- Practice TTL analysis on captured PCAPs

---

## Summary: Do You Need VPN Off?

| Task                              | VPN Status   | Notes                          |
|-----------------------------------|--------------|--------------------------------|
| Read toolkit documentation        | Either       | No network needed              |
| List service probes               | Either       | No packets sent                |
| TTL analysis (defensive)          | Either       | Analyzes existing packets      |
| **Test spoofing capability**      | **VPN OFF**  | Mullvad blocks spoofing        |
| **Active reflection scan**        | **VPN OFF**  | Requires spoofing              |
| **GhostPort stealth scan**        | **VPN OFF**  | Requires spoofing              |
| Passive port scan (no spoofing)   | VPN ON OK    | Standard scanning works        |

---

## Mullvad-Specific Notes

### Lockdown Mode
- If Mullvad "Lockdown" is ON, ALL traffic routes through VPN
- Cannot bypass even if you want to
- Disable lockdown: `mullvad lockdown-mode set off`

### Split Tunneling (If Supported)
- Some VPN clients support split tunneling
- Mullvad CLI doesn't natively support it
- Alternative: Use network namespaces (Linux):

```bash
# Create namespace for spoofing tests (bypass VPN)
sudo ip netns add spoof-test
sudo ip netns exec spoof-test bash

# Inside namespace (VPN not active here):
sudo python3 ghostport.py test-spoof <target> --spoof 8.8.8.8
```

---

## Final Recommendation

**For your VDT work:**

1. **Keep Mullvad connected** for general research/assessments
2. **Disconnect temporarily** when actively testing spoofing tools
3. **Use lab network** for extensive spoofing research (no production network impact)
4. **Document BCP 38 status** of your ISP as a finding (if they allow spoofing, it's a risk!)

**The toolkit works WITHOUT VPN. VPN (Mullvad) blocks spoofing as intended (good security).**
