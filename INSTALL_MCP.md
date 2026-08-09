# Claude Code MCP Integration - ClaudeCodeIPTool

## Installation

### 1. Install MCP Server

```bash
# Server already created at:
~/.claude/mcp-servers/spoof-toolkit/server.py

# Make executable (already done)
chmod +x ~/.claude/mcp-servers/spoof-toolkit/server.py
```

### 2. Register with Claude Code

Add to `~/.claude/mcp-servers/config.json`:

```json
{
  "mcpServers": {
    "spoof-toolkit": {
      "command": "python3",
      "args": ["/home/cowboy/.claude/mcp-servers/spoof-toolkit/server.py"],
      "env": {
        "TOOLKIT_PATH": "/home/cowboy/VDT/tools/ClaudeCodeIPTool"
      }
    }
  }
}
```

### 3. Restart Claude Code

```bash
# If running in terminal, restart the session
# OR use /reset-mcp command if available
```

---

## Available MCP Tools

Once registered, Claude Code can invoke these tools directly:

### 1. `spoof_reflection_scan`

Scan for amplification/reflection vulnerabilities.

**Parameters:**
- `targets`: Target IPs (comma-separated or file path)
- `spoof_src`: Spoofed source IP
- `services` (optional): Specific services (dns,ntp,memcached,etc.)
- `output_file` (optional): Export to JSON

**Example in Claude Code:**
```
Scan 8.8.8.8 and 1.1.1.1 for DNS and NTP reflection vulnerabilities, 
spoofing source as 192.168.1.100
```

### 2. `spoof_ghostport_scan`

Stealth port scan via IP spoofing.

**Parameters:**
- `target`: Target IP to scan
- `victim_ip`: Victim IP (appears in target logs)
- `ports`: Ports (comma-separated or range)
- `method` (optional): passive, timing, ttl, covert

**Example in Claude Code:**
```
Run ghostport scan on 192.168.1.100 ports 80,443,22 
using victim IP 8.8.8.8 with timing method
```

### 3. `spoof_test_bcp38`

Test if network allows IP spoofing.

**Parameters:**
- `target`: Target IP to test
- `spoof_ip`: IP to spoof as source
- `port` (optional): Target port (default 80)

**Example in Claude Code:**
```
Test if I can send spoofed packets with source 8.8.8.8 to 192.168.1.1
```

### 4. `spoof_detect_ttl`

Detect spoofed packets via TTL analysis.

**Parameters:**
- `src_ip`: Source IP from packet to validate
- `observed_ttl`: TTL value from suspicious packet
- `threshold` (optional): Difference threshold (default 5)

**Example in Claude Code:**
```
Check if packet from 8.8.8.8 with TTL 13 is spoofed
```

### 5. `spoof_list_services`

List available service probes.

**Example in Claude Code:**
```
Show me all available reflection service probes
```

---

## Usage from Claude Code

### Natural Language Commands

```
"Scan 8.8.8.8 for DNS amplification vulnerabilities spoofing from 1.1.1.1"

"Run a ghostport scan on 192.168.1.100 ports 1-1024 using timing method"

"Test if my network blocks IP spoofing by sending to 192.168.1.1 as 8.8.8.8"

"Analyze TTL for packet from 8.8.8.8 with observed TTL 13"

"List all reflection services the scanner can probe"
```

Claude Code will:
1. Parse your request
2. Select appropriate MCP tool
3. Fill parameters
4. Execute with sudo (via MCP server)
5. Return formatted results

---

## Permissions

**IMPORTANT**: MCP server runs with sudo for raw socket access.

- Tools require `CAP_NET_RAW` capability (root)
- MCP server runs: `sudo python3 spoof-scanner.py ...`
- Ensure sudoers allows passwordless execution OR configure sudo timeout

### Optional: Passwordless Sudo for Toolkit

```bash
# Add to /etc/sudoers.d/spoof-toolkit
cowboy ALL=(ALL) NOPASSWD: /usr/bin/python3 /home/cowboy/VDT/tools/ClaudeCodeIPTool/*.py
```

---

## Testing MCP Server

```bash
# Test server directly (stdio mode)
python3 ~/.claude/mcp-servers/spoof-toolkit/server.py

# Should output MCP initialization message
```

---

## Troubleshooting

### "Permission denied" errors
- Ensure toolkit scripts are executable: `chmod +x ~/VDT/tools/ClaudeCodeIPTool/*.py`
- Check sudo access: `sudo -v`

### "Scapy not found"
```bash
pip install scapy
# OR
sudo pip install scapy  # If using system Python
```

### "BCP 38 blocks spoofing"
- Your network has anti-spoofing controls (good for defense!)
- Tools will report "spoofing blocked" in test output
- Cannot test reflection/ghostport on networks with BCP 38/uRPF

### MCP server not loading
- Check `~/.claude/mcp-servers/config.json` syntax
- Restart Claude Code session
- Check logs: `~/.claude/logs/mcp-spoof-toolkit.log` (if available)

---

## Security Notice

**VDT Baseline v2.1 Compliance:**
- Use on controlled environments only
- Do NOT scan unauthorized networks
- These tools demonstrate attack primitives for DEFENSIVE research
- Unauthorized use violates computer fraud laws (CFAA, etc.)

---

## Uninstallation

```bash
# Remove MCP server
rm -rf ~/.claude/mcp-servers/spoof-toolkit/

# Remove from config
# Edit ~/.claude/mcp-servers/config.json and remove "spoof-toolkit" entry

# Restart Claude Code
```
