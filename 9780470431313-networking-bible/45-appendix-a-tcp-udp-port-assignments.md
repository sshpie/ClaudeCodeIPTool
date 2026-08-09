# Appendix A. TCP - UDP Port Assignments

**IN THIS APPENDIX**

- Different port assignments are listed

[Table A.1](apa.html#well-known_ports_colon_1_to_1023_registe) lists many common ports in use for both the TCP and UDP protocols, under the Port column as T and U, respectively. The most widely used ports are typically found in the range 1 to 1023 and are referred to as the "well-known ports." A large range of port assignments are registered by vendors for specific applications. Over time, many of these port assignments become just as popular as well-known ports. Registered ports are found in the range 1024 to 49191. Finally, ICANN allows the remaining ports from 49152 to 65535 to be used either dynamically or for private assignments. Ports in the high range are not registered or assigned; they are for use by anyone at any time.

In many instances, TCP and UDP use the same numbers for the same protocol, but not always. Nor is a single protocol such as HTTP necessarily found on only one port assignment. There can be multiple ports assigned, and in the case of HTTP, the two common port assignments are not a contiguous range: both 80 and 8080 (for firewalls) are commonly used.

**Table A.1. Well-Known Ports: 1 to 1023 Registered Ports: 1024 to 49191 Dynamic and Private Ports: 49152 to 65535 (unassigned)**

| Port | Assignment | Notes |
| --- | --- | --- |
| Reference: `www.iana.org/assignments/port-numbers`. The list above is edited and is not as complete as the list of ports on this official site. Also, their list is updated on a regular basis. |  |  |
| 0 - T, U | Reserved |  |
| 0 - T, U | Shirt Pocket netTunes; Shirt Pocket launchTunes |  |
| 1 - T, U | TCP Port Service Multiplexer |  |
| 2 - T, U | Management Utility |  |
| 3 - T, U | Compression Process |  |
| 5 - T, U | Remote Job Entry |  |
| 6 - T, U | Unassigned |  |
| 7 - T, U | Echo |  |
| 8 - T, U | Unassigned |  |
| 9 - T, U | Discard |  |
| 10 - T, U | Unassigned |  |
| 11 - T, U | Active Users |  |
| 12 - T, U | Unassigned |  |
| 13 - T, U | Daytime - (RFC 867) |  |
| 14 - T. P | Unassigned |  |
| 15 - T, U | Unassigned |  |
| 16 - T, U | Unassigned |  |
| 17 - T, U | Quote of the Day |  |
| 18 - T, U | Message Send Protocol |  |
| 19 - T, U | Character Generator |  |
| 20 - T, U | FTP - Default Data |  |
| 21 - T, U | FTP - Control Command |  |
| 22 - T, U | SSH Remote Login Protocol |  |
| 23 - T, U | Telnet |  |
| 24 - T, U | Any private mail system |  |
| 25 - T, U | Simple Mail Transfer Protocol (SMTP) |  |
| 26 - T, U | RSFTP | Unofficial |
| 27 - T, U | New User System FE |  |
| 28 - T, U | Unassigned |  |
| 29 - T, U | MSG ICP |  |
| 30 - T, U | Unassigned |  |
| 31 - T, U | MSG Authentication |  |
| 32 - T, U | Unassigned |  |
| 33 - T, U | Display Support Protocol |  |
| 34 - T, U | Unassigned |  |
| 35 - T, U | Any private printer server protocol |  |
| 35 - T, U | QMS Magicolor 2 printer server protocol | Unofficial |
| 36 - T, U | Unassigned |  |
| 37 - T, U | TIME protocol |  |
| 38 - T, U | Remote Access Protocol |  |
| 39 - T, U | Resource Location Protocol (RLP) |  |
| 40 -T, U | Unassigned |  |
| 41 - T, U | Graphics |  |
| 42 - T, U | ARPA Host Name Server Protocol |  |
| 42 - T, U | WINS | Unofficial |
| 43 - T, U | WHOIS Protocol |  |
| 44 - T, U | MPM FLAGS Protocol |  |
| 45 - T, U | Message Processing Module |  |
| 46 - T, U | MPM (default send) |  |
| 47 - T, U | NI FTP |  |
| 48 - T, U | Digital Audit Daemon |  |
| 49 - T, U | TACACS Login Host Protocol |  |
| 50 - T, U | Remote Mail Checking Protocol |  |
| 51 - T, U | IMP Logical Address Maintenance |  |
| 52 - T, U | Xerox Network Services (XNS) Time Protocol |  |
| 53 - T, U | Domain Name System (DNS) |  |
| 54 - T, U | Xerox Network Services (XNS) Clearinghouse |  |
| 55 - T, U | ISI Graphics Language |  |
| 56 - T, U | Xerox Network Services (XNS) Authentication |  |
| 56 - T, U | Route Access Protocol (RAP) | Unofficial |
| 57 -T | Mail Transfer Protocol (MTP) | Unofficial |
| 57 - T, U | Any private mail system |  |
| 58 - T, U | Xerox Network Services (XNS) Mail |  |
| 59 - T, U | Any private file service |  |
| 60 - T, U | Unassigned |  |
| 61 - T, U | NI Mail |  |
| 62 - T, U | ACA Services |  |
| 63 - T, U | whois++ |  |
| 64 - T, U | Communications Integrator (CI) |  |
| 65 - T, U | TACACS - Database Service |  |
| 66 - T, U | Oracle SQL*NET |  |
| 67 - T, U | Bootstrap Protocol (BOOTP) Server |  |
| 68 - T, U | Bootstrap Protocol (BOOTP) Client |  |
| 69 - T, U | Trivial File Transfer Protocol (TFTP) |  |
| 70 - T, U | Gopher Protocol |  |
| 71 - T, U | Remote Job Service |  |
| 72 - T, U | Remote Job Service |  |
| 73 - T, U | Remote Job Service |  |
| 74 - T, U | Remote JobService |  |
| 75 - T, U | Any private dial out service |  |
| 76 - T, U | Distributed External Object Store |  |
| 77 - T, U | Any private RJE server |  |
| 78 - T, U | Vettcp |  |
| 79 - T, P | Finger Protocol |  |
| 80 - T, P | Hypertext Transfer Protocol (HTTP) |  |
| 81 - T, P | Unassigned |  |
| 82 - T, U | XFER Utility |  |
| 83 - T, U | MIT ML Device |  |
| 84 - T, U | Common Trace Facility |  |
| 85 - T, U | MIT ML Device |  |
| 86 - T, U | Micro Focus Cobol |  |
| 87 - T, U | Any private terminal link |  |
| 88 - T, P | Kerberos |  |
| 90 - T, U | DNSIX Security Attribute Token Map |  |
| 90 - T, U | PointCast | Unofficial |
| 91 - T, U | MIT Dover Spooler |  |
| 92 - T, U | Network Printing Protocol |  |
| 93 - T, U | Device Control Protocol |  |
| 94 - T, U | Tivoli Object Dispatcher |  |
| 95 - T, U | SUPDUP |  |
| 96 - T, U | DIXIE Protocol Specification |  |
| 97 - T, U | Swift Remote Virtual File Protocol |  |
| 98 - T, U | TAC News |  |
| 99 - T, U | Metagram Relay |  |
| 100 - T | Unauthorized use |  |
| 101 - T,U | NIC Host Name Server |  |
| 102 - T,U | ISO Transport Service Access Point (TSAP) Class 0 Protocol |  |
| 103 - T,U | Genesis Point-to-Point Trans Net |  |
| 104 - T, U | ACR-NEMA Digital Imag. & Comm. 300 |  |
| 105 - T, U | Mailbox Name Nameserver |  |
| 106 - T, U | 3COM-TSMUX |  |
| 106 - T, U | Insecure poppassd Protocol | Unauthorized |
| 107 - T,U | Remote Telnet Service Protocol |  |
| 108 - T,U | SNA Gateway Access Server |  |
| 109 - T, U | Post Office Protocol 2 (POP2) |  |
| 110 - T, U | Post Office Protocol 3 (POP3) |  |
| 111 - T, U | Sun Remote Procedure Call |  |
| 112 - T, U | McIDAS Data Transmission Protocol |  |
| 113 - T, U | Authentication Service |  |
| 114 - T, U | Deprecated June 2004 |  |
| 115 - T, U | Simple File Transfer Protocol (SFTP) |  |
| 116 - T, U | ANSA REX Notify |  |
| 117 - T, U | UUCP Path Service |  |
| 118 - T, U | Structured Query Language (SQL) Services |  |
| 119 - T, P | Network News Transfer Protocol (NNTP) |  |
| 120 - T, P | CFDPTKT |  |
| 121 - T, P | Encore Expedited Remote Pro.Call |  |
| 122 - T, P | SMAKYNET |  |
| 123 - T, U | Network Time Protocol (NTP) |  |
| 124 - T, U | ANSA REX Trader |  |
| 125 - T, U | Locus PC-Interface Net Map Ser |  |
| 126 - T, U | NxEdit | Previously assigned to Unisys Unitary Login |
| 127 - T, U | Locus PC-Interface Conn Server |  |
| 128 - T, U | GSS X License Verification |  |
| 129 - T, U | Password Generator Protocol |  |
| 130 - T, U | Cisco FNATIVE |  |
| 131 - T, U | Cisco TNATIVE |  |
| 132 - T, U | Cisco SYSMAINT |  |
| 133 - T, U | Statistics Service |  |
| 134 - T, U | INGRES-NET Service |  |
| 135 - T, U | DCE endpoint resolution |  |
| 135 - T, U | Microsoft End Point Mapper (EPMAP), AKA DCE/RPC Locator service | Unofficial |
| 137 - T, U | NetBIOS Name Service |  |
| 138 - T, U | NetBIOS Datagram Service |  |
| 139 - T, U | NetBIOS Session Service |  |
| 140 - T, U | EMFIS Data Service |  |
| 141 - T, U | EMFIS Control Service |  |
| 142 - T, U | Britton-Lee IDM |  |
| 143 - T, U | Internet Message Access Protocol (IMAP) |  |
| 152 - T, U | Background File Transfer Program (BFTP) |  |
| 153 - T, U | Simple Gateway Monitoring Protocol (SGMP) |  |
| 156 - T, U | SQL Service |  |
| 158 - T, U | Distributed Mail Service Protocol (DMSP) | Unofficial |
| 161 - T, U | Simple Network Management Protocol (SNMP) | Official |
| 162 - T, U | Simple Network Management Protocol Trap (SNMPTRAP) | Official |
| 170 - T | Print-srv, Network PostScript | Official |
| 177 - T, U | X Display Manager Control Protocol (XDMCP) | Official |
| 179T | Border Gateway Protocol (BGP) | Official |
| 194T | Internet Relay Chat (IRC) | Official |
| 201 - T, U | AppleTalk Routing Maintenance | Official |
| 209 - T, U | The Quick Mail Transfer Protocol | Official |
| 213 - T, U | IPX | Official |
| 218 - T, U | Message Posting Protocol (MPP) | Official |
| 220 - T, U | Interactive Mail Access Protocol (IMAP) version 3 | Official |
| 259 - T, U | Efficient Short Remote Operations (ESRO) | Official |
| 264 - T, U | Border Gateway Multicast Protocol (BGMP) | Official |
| 311 - T | Mac OS X Server Admin (officially AppleShare IP Web administration) | Official |
| 318 - T, U | PKIX Time Stamp Protocol (TSP) | Official |
| 323 - T, U | Internet Message Mapping Protocol (IMMP) | Unofficial |
| 366 - T, U | On-Demand Mail Relay (ODMR) | Official |
| 369 - T, U | Rpc2portmap | Official |
| 387 - T, U | AppleTalk Update-based Routing Protocol (AURP) | Official |
| 389 - T, U | Lightweight Directory Access Protocol (LDAP) | Official |
| 401 - T, U | Uninterruptible Power Supply (UPS) | Official |
| 402 - T | Altiris Deployment Client | Unofficial |
| 411 - T | Direct Connect Hub | Unofficial |
| 412 - T | Direct Connect Client-to-Client | Unofficial |
| 427 - T, U | Service Location Protocol (SLP) | Official |
| 443 - T | Hypertext Transfer Protocol over TLS/SSL (HTTPS) | Official |
| 444 - T, U | Simple Network Paging Protocol (SNPP) (RFC 1568) | Official |
| 445T | Microsoft-DS Active Directory, Windows shares | Official |
| 445 -U | Microsoft-DS SMB file sharing | Official |
| 464 - T, U | Kerberos Change/Set password | Official |
| 465T | Cisco protocol | Unofficial |
| 465T | SMTP over SSL | Unofficial |
| 500 - U | Internet Security Association and Key Management Protocol (ISAKMP) | Official |
| 502 - T, U | Modbus Protocol | Unofficial |
| 513T | Login | Official |
| 513 - U | Who | Official |
| 514T | Shell | Official |
| 514 - U | Syslog | Official |
| 515 - T | Line Printer Daemon (print service) | Official |
| 517 - U | Talk | Official |
| 518 - U | Ntalk | Official |
| 520T | Extended filename server (EFS) | Official |
| 520 - U | Routing Internet Protocol (RIP) | Official |
| 524 - T, U | NetWare Core Protocol (NCP) | Official |
| 525 - U | Timed, Timeserver | Official |
| 530 - T, U | RPC | Official |
| 531 - T, U | AOL Instant Messenger, IRC | Unofficial |
| 540T | Unix-to-Unix Copy Protocol (UUCP) | Official |
| 542 - T, U | Commerce (Commerce Applications) | Official |
| 543T | Kerberos login (klogin) | Official |
| 544T | Kerberos Remote shell (kshell) | Official |
| 546 - T, U | DHCPv6 client | Official |
| 547 - T, U | DHCPv6 server | Official |
| 548T | Apple Filing Protocol (AFP) over TCP | Official |
| 550 - U | new-rwho, new-who | Official |
| 554 - T, U | Real Time Streaming Protocol (RTSP) | Official |
| 556T | Remotefs, RFS, rfs_server | Official |
| 560 - U | Remote Monitor (rmonitor) | Official |
| 561 - U | Monitor | Official |
| 563 - T, U | NNTP protocol over TLS/SSL (NNTPS) | Official |
| 587T | Simple Mail Transfer Protocol (message submission) | Official |
| 591T | FileMaker 6.0 (and later) Web Sharing (HTTP Alternate, also see port 80) | Official |
| 593 - T, U | HTTP RPC Ep Map, R | Official |
| 631 - T, U | Internet Printing Protocol (IPP) | Official |
| 636 - T, U | Lightweight Directory Access Protocol over TLS/SSL (LDAPS) | Official |
| 639 - T, U | Multicast Source Discovery Protocol (MSDP) | Official |
| 646 - T, U | Label Distribution Protocol (LDP), a routing protocol used in MPLS networks | Official |
| 647 - T | Dynamic Host Configuration Protocol (DHCP) Failover | Official |
| 648 - T | Registry Registrar Protocol (RRP) | Official |
| 652 - T | Dynamic Tunnel Configuration Protocol (DTCP) | Unofficial |
| 654 - T | Ad-hoc On-demand Distance Vector (AODV) | Official |
| 655 - T | IEEE Media Management System (IEEE MMS) | Official |
| 657 - T, U | IBM Remote Monitoring and Control (RMC) Protocol | Official |
| 660 - T | Mac OS X Server administration | Official |
| 666 - U | Doom | Official |
| 674 - T | Application Configuration Access Protocol (ACAP) | Official |
| 691 - T | MS Exchange Routing | Official |
| 694 - U | Linux-HA High Availability Heartbeat | Unofficial |
| 695 - T | IEEE Media Management System over SSL (IEEE-MMS-SSL) | Official |
| 698 - U | Optimized Link State Routing (OLSR) | Official |
| 700 - T | Extensible Provisioning Protocol (EPP) | Official |
| 701 - T | Link Management Protocol (LMP) | Official |
| 702 - T | Internet Registry Information Service (IRIS) over Blocks Extensible Exchange Protocol (BEEP) | Official |
| 706 - T | Secure Internet Live Conferencing (SILC) | Official |
| 712 - T | Topology Broadcast based on Reverse-Path Forwarding (TBRPF) routing protocol | Official |
| 749 - T, U | Kerberos Administration | Official |
| 750 - T | RFile | Official |
| 750 - U | Loadav | Official |
| 750 - U | Kerberos version IV (Kerberos IV) | Official |
| 751 - T, U | Pump | Official |
| 751 - T, U | Kerberos authentication (kerberos_master) | Unofficial |
| 752 - T | qrh | Official |
| 752 - U | qrh | Official |
| 752 - U | userreg_server, Kerberos Password (kpasswd) server | Unofficial |
| 753 - T | Reverse Routing Header (RRH) | Official |
| 753 - U | Reverse Routing Header (RRH) | Official |
| 753 - U | Kerberos userreg server (passwd_server) | Unofficial |
| 754 - T | tell send | Official |
| 754 - T | Kerberos v5 slave propagation (krb5_prop) | Unofficial |
| 754 - U | tell send | Official |
| 760 - T, U | ns | Official |
| 783 - T | SpamAssassin spamd daemon | Unofficial |
| 829 - T | Certificate Management Protocol (CMP) | Unofficial |
| 860 - T | iSCSI | Official |
| 873 - T | rsync file synchronization protocol | Official |
| 901 - T | Samba Web Administration Tool (SWAT) | Unofficial |
| 901T - U | VMware Virtual Infrastructure Client | Unofficial |
| 902 - T | VMware Server Console | Unofficial |
| 904 - T | VMware Server Alternate | Unofficial |
| 953 - T, U | Domain Name System (DNS) RDNC Service | Official |
| 989 - T, U | FTPS Protocol (data): FTP over TLS/SSL | Official |
| 990 - T, U | FTPS Protocol (control): FTP over TLS/SSL | Official |
| 992 - T, U | TELNET protocol over TLS/SSL | Official |
| 993 - T | Internet Message Access Protocol over SSL (IMAPS) | Official |
| 995 - T | Post Office Protocol 3 over TLS/SSL (POP3S) | Official |
| 1025 - T | NFS-or-IIS | Unofficial |
| 1026 - T | Microsoft DCOM services | Unofficial |
| 1029 - T | Microsoft DCOM services | Unofficial |
| 1058 - T, U | nim, IBM AIX Network Installation Manager (NIM) | Official |
| 1059 - T, U | nimreg, IBM AIX Network Installation Manager (NIM) | Official |
| 1080 - T | SOCKS proxy | Official |
| 1085 - T, U | WebObjects | Official |
| 1098 - T, U | RMI Activation (rmiactivation) | Official |
| 1099 - T, U | RMI Registry (rmiregistry) | Official |
| 1109 - T | Kerberos Post Office Protocol (KPOP) | Unofficial |
| 1140 - T, U | AutoNOC Network Operations protocol | Official |
| 1167 - U | Phone, conference calling | Unofficial |
| 1194 - T, U | OpenVPN | Official |
| 1214 - T | Kazaa | Official |
| 1220 - T | QuickTime Streaming Server administration | Official |
| 1223 - T, U | TrulyGlobal Protocol (TGP) | Official |
| 1234 - U | VLC media player Default port for UDP/RTP stream | Unofficial |
| 1270 - T, U | Microsoft System Center Operations Manager (SCOM; AKAMS MOM) agent | Official |
| 1293 - T, U | Internet Protocol Security (IPSec) | Official |
| 1311 - T | Dell Open Manage HTTPS | Unofficial |
| 1352 - T | IBM Lotus Notes/Domino Remote Procedure Call (RPC) Protocol | Official |
| 1387 - T, U | cadsi-lm, LMS International (formerly Computer Aided Design Software, Inc. [CADSI]) LM | Official |
| 1414 - T | IBM WebSphere MQ (formerly known as MQSeries) | Official |
| 1417 - T, U | Timbuktu Service 1 Port | Official |
| 1418 - T, U | Timbuktu Service 2 Port | Official |
| 1419 - T, U | Timbuktu Service 3 Port | Official |
| 1420 - T, U | Timbuktu Service 4 Port | Official |
| 1433 - T, U | Microsoft SQL Server database management system Server | Official |
| 1434 - T, U | Microsoft SQL Server database management system Monitor | Official |
| 1494 - T | Citrix XenApp Independent Computing Architecture (ICA) thin client protocol | Official |
| 1512 - T, U | Microsoft Windows Internet Name Service (WINS) | Official |
| 1521 - T | Oracle database default listener, in future releases official port 2483 | Unofficial |
| 1524 - T, U | ingreslock, ingres | Official |
| 1526 - T | Oracle database common alternative for listener | Unofficial |
| 1533 - T | IBM Sametime IM — Virtual Places Chat SQL Server | Official |
| 1547 - T, U | Laplink | Official |
| 1581 - U | MIL STD 2045-47001 VMF | Official |
| 1589 - U | Cisco VLAN Query Protocol (VQP) / VMPS | Unofficial |
| 1645 - T, U | radius, RADIUS authentication protocol (default for Cisco and Juniper Networks RADIUS servers) | Unofficial |
| 1646 - T, U | radaccT, RADIUS accounting protocol (default for Cisco and Juniper Networks RADIUS servers) | Unofficial |
| 1677 - T, U | Novell GroupWise clients | Official |
| 1701 - U | Layer 2 Forwarding Protocol (L2F) & Layer 2 Tunneling Protocol (L2TP) | Official |
| 1723 - T, U | Microsoft Point-to-Point Tunneling Protocol (PPTP) | Official |
| 1725 - U | Valve Steam Client | Unofficial |
| 1755 - T, U | Microsoft Media Services (MMS, ms-streaming) | Official |
| 1761 - T, U | cft-0 | Official |
| 1761 - T | Novell ZENworks Remote Control utility | Unofficial |
| 1762–1768 - T, U | cft-1 to cft-7 | Official |
| 1812 - T, U | radius, RADIUS authentication protocol | Official |
| 1813 - T, U | radaccT, RADIUS accounting protocol | Official |
| 1863 - T | Microsoft Notification Protocol (MSNP) | Official |
| 1900 - U | Microsoft SSDP for UPnP devices | Official |
| 1935 - T | Adobe Macromedia Flash Real Time Messaging Protocol (RTMP) | Official |
| 1975–1977 - U | Cisco TCO (Documentation) | Official |
| 1985 - U | Cisco HSRP | Official |
| 1994 - T, U | Cisco Serial Tunneling — Synchronous Data Link Control (STUN-SDLC) Protocol | Official |
| 1998 - T, U | Cisco X.25 over TCP (XOT) service | Official |
| 2000 - T, U | Cisco SCCP (Skinny) | Official |
| 2002 - T | Secure Access Control Server (ACS) for Windows | Unofficial |
| 2030 | Oracle Services for Microsoft Transaction Server | Unofficial |
| 2049 - U | Network File System | Official |
| 2053 - T | knetd Kerberos de-multiplexor | Unofficial |
| 2083 - T | Secure Radius Service (RadSec) | Official |
| 2083 - T | CPanel default SSL | Unofficial |
| 2086 - T | GNUnet | Official |
| 2086 - T | WebHost Manager default | Unofficial |
| 2087 - T | WebHost Manager default SSL | Unofficial |
| 2105 - T, U | IBM MiniPay | Official |
| 2105 - T, U | eklogin Kerberos encrypted remote login (rlogin) | Unofficial |
| 2161 - T | APC Agent | Official |
| 2181 - T, U | EForward - document transport system | Official |
| 2190 - U | TiVoConnect Beacon | Unofficial |
| 2219 - T, U | NetIQ NCAP Protocol | Official |
| 2220 - T, U | NetIQ End2End | Official |
| 2222 - T | DirectAdmin default | Unofficial |
| 2302 - U | Halo | Unofficial |
| 2369 - T | BMC Software CONTROL-M/Server —Configuration Agent | Unofficial |
| 2370 - T | BMC Software CONTROL-M/Server | Unofficial |
| 2404 - T | IEC 60870-5-104 | Official |
| 2427 - U | Cisco MGCP | Official |
| 2447 - T, U | Ovwdb — OpenView Network Node Manager (NNM) daemon | Official |
| 2483 - T, U | Oracle database listening (replaces port 1521) | Official |
| 2484 - T, U | Oracle database listening for SSL client connections to the listener | Official |
| 2598 - T | New ICA — when Session Reliability is enabled, TCP port 2598 replaces port 1494 | Unofficial |
| 2710 - T | XBT BitTorrent Tracker | Unofficial |
| 2710 - U | XBT BitTorrent Tracker experimental UDP tracker extension | Unofficial |
| 2735 - T, U | NetIQ Monitor Console | Official |
| 2809 - T | IBM WebSphere Application Server (WAS) Bootstrap/rmi default | Unofficial |
| 2948 - T, U | WAP-push Multimedia Messaging Service (MMS) | Official |
| 2949 - T, U | WAP-pushsecure Multimedia Messaging Service (MMS) | Official |
| 2967 - T | Symantec AntiVirus Corporate Edition | Unofficial |
| 3025 - T | `netpd.org` | Unofficial |
| 3074 - T, U | Xbox Live | Official |
| 3260 - T, U | iSCSI target | Official |
| 3268 - T, U | msft-gc, Microsoft Global Catalog (LDAP service) | Official |
| 3269 - T, U | msft-gc-ssl, Microsoft Global Catalog over SSL | Official |
| 3283 - T | Apple Remote Desktop reporting (officially Net Assistant) | Official |
| 3306 - T, U | MySQL database system | Official |
| 3389 - T | Microsoft Terminal Server (RDP) officially registered as Windows Based Terminal (WBT) | Unofficial |
| 3396 - T, U | Novell NDPS Printer Agent | Official |
| 3455 - T, U | Reservation Protocol (RSVP) | Official |
| 3689 - T | Digital Audio Access Protocol (DAAP) for Apple iTunes and AirPort Express | Official |
| 3702 - T, U | Web Services Dynamic Discovery (WS-Discovery), used by various components of Windows Vista | Official |
| 3868 - T, Stream Control Transfer Protocol (SCTP) | Diameter base protocol (RFC 3588) | Official |
| 3872 - T | Oracle Management Remote Agent | Unofficial |
| 3899 - T | Remote Administrator | Unofficial |
| 3900 - T | udt_os, IBM UniData UDT OS[30] | Official |
| 4100 | WatchGuard Authentication Applet—default | Unofficial |
| 4125 - T | Microsoft Remote Web Workplace administration | Unofficial |
| 4224 - T | Cisco Discovery Protocol (CDP) | Unofficial |
| 4500 - U | IPsec NAT traversal | Official |
| 4664 - T | Google Desktop Search | Unofficial |
| 4993 - T, U | Home FTP Server Web Interface Default Port |  |
| 4899 - T, U | Radmin remote administration tool (sometimes used as a Trojan) | Official |
| 5000 - T | UPnP—Windows network device interoperability | Unofficial |
| 5001 - T, U | Iperf (Tool for measuring TCP and UDP bandwidth performance ) | Unofficial |
| 5001 - T | Slingbox and SlingPlayer | Unofficial |
| 5003 - T, U | FileMaker | Official |
| 5004 - T, U, Datagram Congestion Control Protocol (DCCP) | Real-time Transport Protocol (RTP) media data | Official |
| 5005 - T, U, DCCP | Real-time Transport Protocol (RTP) control protocol | Official |
| 5050 - T | Yahoo! Messenger | Unofficial |
| 5060 - T, U | Session Initiation Protocol (SIP) | Official |
| 5061 - T | Session Initiation Protocol (SIP) over TLS | Official |
| 5093 - U | Statistical Package for the Social Sciences (SPSS) License Administrator | Unofficial |
| 5104 - T | IBM Tivoli Framework NetCOOL/Impact HTTP Service | Unofficial |
| 5190 - T | ICQ and AOL Instant Messenger | Official |
| 5351 - T, U | NAT Port Mapping Protocol | Official |
| 5353 - U | Multicast DNS (MDNS) | Official |
| 5355 - T, U | Link-Local Multicast Name Resolution (LLMNR) | Official |
| 5432 - T, U | PostgreSQL database system | Official |
| 5445 - U | Cisco Unified Video Advantage | Unofficial |
| 5500 - T | VNC remote desktop protocol | Unofficial |
| 5517 - T | SETIQueue Proxy server client for SETI@Home project | Unofficial |
| 5631 - T | pcANYWHEREdata | Official |
| 5632 - U | pcANYWHERE-sta | Official |
| 5800 - T | VNC remote desktop protocol—for use over HTTP | Unofficial |
| 5814 - T, U | Hewlett-Packard Support Automation (HP OpenView Self-Healing Services) | Official |
| 5900 - T, U | Virtual Network Computing (VNC) remote desktop protocol (used by Apple Remote Desktop and others) | Official |
| 6000 - T | X11 | Official |
| 6001 - U | X11 | Official |
| 6005 - T | BMC Software CONTROL-M/Server | Unofficial |
| 6346 - T, U | gnutella-svc, Gnutella (FrostWire, LimeWire, Shareaza, and so on) | Official |
| 6347 - T, U | gnutella-rtr, Gnutella alternate | Official |
| 6444 - T, U | Sun Grid Engine — Qmaster Service | Official |
| 6445 - T, U | Sun Grid Engine — Execution Service | Official |
| 6571 | Windows Live FolderShare client | Unofficial |
| 6600 - T | Music Playing Daemon (MPD) | Unofficial |
| 6660–6664 - T | Internet Relay Chat | Unofficial |
| 6665–6669 - T | Internet Relay Chat | Official |
| 6679 - T | IRC SSL (Secure Internet Relay Chat) | Unofficial |
| 6697 - T | IRC SSL (Secure Internet Relay Chat) | Unofficial |
| 6771 - U | Polycom server broadcast | Unofficial |
| 6881–6887 - T, U | BitTorrent | Unofficial |
| 6888 - T, U | MUSE | Official |
| 6888 - T, U | BitTorrent | Unofficial |
| 6889–6890 - T, U | BitTorrent | Unofficial |
| 6891–6900 - T, U | BitTorrent | Unofficial |
| 6891–6900 - T, U | Windows Live Messenger (File transfer) | Unofficial |
| 6901 - T, U | Windows Live Messenger (Voice) | Unofficial |
| 6901 - T, U | BitTorrent | Unofficial |
| 6902–6968 - T, U | BitTorrent | Unofficial |
| 6969 - T | BitTorrent tracker | Unofficial |
| 6970–6999 - T, U | BitTorrent | Unofficial |
| 7001 - T | BEA WebLogic Server's HTTP server | Unofficial |
| 7002 - T | BEA WebLogic Server's HTTPS server | Unofficial |
| 7005 - T, U | BMC Software CONTROL-M/Server and CONTROL-M/Agent | Unofficial |
| 7006 - T, U | BMC Software CONTROL-M/Server and CONTROL-M/Agent | Unofficial |
| 7010 - T | Cisco AON AMC (AON Management Console) | Unofficial |
| 7400 - T, U | Real Time Publish Subscribe (RTPS) DDS Discovery | Official |
| 7401 - T, U | Real Time Publish Subscribe (RTPS) DDS User-Traffic | Official |
| 7402 - T, U | RTPS (Real Time Publish Subscribe) DDS Meta-Traffic | Official |
| 7777 - T | iChat server file transfer proxy | Unofficial |
| 7777 - T | Default used by Windows backdoor program tini.exe | Unofficial |
| 8000 - T, U | Intel Remote Desktop Management Interface (iRDMI) | Official |
| 8000–8001 - T | Internet radio streams such as SHOUTcast | Unofficial |
| 8002 - T | Cisco Systems Unified CallManager Intercluster | Unofficial |
| 8008 - T | HTTP Alternate | Official |
| 8008 - T | IBM HTTP Server administration default | Unofficial |
| 8080 - T | HTTP alternate (http_alt) — commonly used for Web proxy and caching server, or for running a Web server as a non-root user | Official |
| 8080 - T | Apache Tomcat | Unofficial |
| 8081 - T | HTTP alternate, such as McAfee ePolicy Orchestrator (ePO) | Unofficial |
| 8086 - T | Kaspersky AntiVirus Control Center | Unofficial |
| 8087 - U | Kaspersky AntiVirus Control Center | Unofficial |
| 8090 - T | HTTP Alternate (http_alt_alt) — used as an alternative to port 8080 | Unofficial |
| 8192 - T | Sophos Remote Management System | Unofficial |
| 8193 - T | Sophos Remote Management System | Unofficial |
| 8194 - T | Sophos Remote Management System | Unofficial |
| 8200 - T | GoToMyPC | Unofficial |
| 8220 - T | Bloomberg | Unofficial |
| 8222 | VMware Server Management User Interface (insecure Web interface) | Unofficial |
| 8243 - T, U | HTTPS listener for Apache Synapse | Official |
| 8280 - T, U | HTTP listener for Apache Synapse | Official |
| 8294 - T | Bloomberg | Unofficial |
| 8333 | VMware Server Management User Interface (secure Web interface) | Unofficial |
| 8400 - T, U | cvp, CommVault Unified Data Management | Official |
| 8500 - T | ColdFusion Macromedia/Adobe ColdFusion default | Unofficial |
| 8880 - U | cddbp-al - T, CD DataBase (CDDB) Protocol (CDDBP) alternate | Official |
| 8880 - T | cddbp-al - T, CD DataBase (CDDB) Protocol (CDDBP) alternate | Official |
| 8880 - T | WebSphere Application Server SOAP connector default | Unofficial |
| 8888 - T | Sun AnswerBook dwhttpd server (deprecated by `docs.sun.com`) | Unofficial |
| 8888 - T | GNUmp3d HTTP music streaming and Web interface | Unofficial |
| 9000 - T | Buffalo LinkSystem Web access | Unofficial |
| 9000 - U | UDPCast | Unofficial |
| 9001 | cisco-xremote router configuration | Unofficial |
| 9001 | Tor network default | Unofficial |
| 9030 - T | Tor often used | Unofficial |
| 9043 - T | WebSphere Application Server Administration Console secure | Unofficial |
| 9050 - T | Tor | Unofficial |
| 9051 - T | Tor | Unofficial |
| 9060 - T | WebSphere Application Server Administration Console | Unofficial |
| 9080 - U | glrpc, Groove Collaboration software GLRPC | Official |
| 9080 - T | glrpc, Groove Collaboration software GLRPC | Official |
| 9080 - T | WebSphere Application Server HTTP Transport (port 1) default | Unofficial |
| 9110 - U | SSMP Message Protocol | Unofficial |
| 9443 - T | WSO2 Web Services Application Server HTTPS transport (officially WSO2 Tungsten HTTPS) | Official |
| 9443 - T | WebSphere Application Server HTTP Transport (port 2) default | Unofficial |
| 9535 - T | mngsuite, LANDesk Management Suite Remote Control | Official |
| 9535 - T | BBOS001, IBM WebSphere Application Server (WAS) High Availability Manager Communications | Unofficial |
| 9535 - U | mngsuite, LANDesk Management Suite Remote Control | Official |
| 9800 - T, U | WebDAV Source | Official |
| 9800 | WebCT e-learning portal | Unofficial |
| 9898 - T | Tripwire — File Integrity Monitoring Software | Unofficial |
| 9999 - T | Lantronix UDS-10/UDS100[43] RS-485 to Ethernet Converter TELNET control | Unofficial |
| 10000 | Webmin — Web-based Linux admin tool | Unofficial |
| 10000 | Backup Exec | Unofficial |
| 10001 - T | Lantronix UDS-10/UDS100[44] RS-485 to Ethernet Converter default | Unofficial |
| 10017 | AIX, NeXT, HPUX — rexd daemon control | Unofficial |
| 10113 - T, U | NetIQ Endpoint | Official |
| 10114 - T, U | NetIQ QCheck | Official |
| 10115 - T, U | NetIQ Endpoint | Official |
| 10116 - T, U | NetIQ VoIP Assessor | Official |
| 11211 | memcached | Unofficial |
| 11371 | OpenPGP HTTP key server | Official |
| 11576 | IPStor Server management communication | Unofficial |
| 12035 - U | Linden Lab viewer to sim | Unofficial |
| 12345 | NetBus — remote administration tool (often a Trojan) | Unofficial |
| 12975 - T | LogMeIn Hamachi (VPN tunnel software) | Unofficial |
| 13000–13050 - U | Linden Lab viewer to sim | Unofficial |
| 13720 - T, U | Symantec NetBackup — bprd | Official |
| 13721 - T, U | Symantec NetBackup — bpdbm | Official |
| 13724 - T, U | Symantec Network Utility — vnetd | Official |
| 13782 - T, U | Symantec NetBackup — bpcd | Official |
| 13783 - T, U | Symantec VOPIED Protocol | Official |
| 13785 - T, U | Symantec NetBackup Database — nbdb | Official |
| 13786 - T, U | Symantec nomdb | Official |
| 14567 - U | Battlefield 1942 and mods | Unofficial |
| 16000 - T | shroudBNC | Unofficial |
| 16080 - T | Mac OS X Server Web (HTTP) service with performance cache | Unofficial |
| 16384 - U | Iron Mountain Digital online backup | Unofficial |
| 18180 - T | DART Reporting server | Unofficial |
| 19226 - T | Panda Software AdminSecure Communication Agent | Unofficial |
| 19638 - T | Ensim Control Panel | Unofficial |
| 19771 - T, U | Softros LAN Messenger | Unofficial |
| 19813 - T | 4D Database Client Server Communication | Unofficial |
| 19880 - T | Softros LAN Messenger | Unofficial |
| 20000 | Distributed Network Protocol (DNP), used in SCADA | Official |
| 20000 | Usermin, Web-based user tool | Unofficial |
| 20014 - T | DART Reporting server | Unofficial |
| 20720 - T | Symantec i3 Web GUI server | Unofficial |
| 22347 - T, U | WibuKey, WIBU-SYSTEMS AG Software protection system | Official |
| 22350 - T, U | CodeMeter, WIBU-SYSTEMS AG Software protection system | Official |
| 24444 | NetBeans integrated development environment | Unofficial |
| 24800 | Synergy: keyboard/mouse sharing software | Unofficial |
| 25999 - T | Xfire | Unofficial |
| 26000 - T, U | id Software Quake server | Official |
| 27000 - U | (Through 27006) id Software QuakeWorld master server | Unofficial |
| 27010 | Half-Life and its mods, such as Counter-Strike | Unofficial |
| 27015 | Half-Life and its mods, such as Counter-Strike | Unofficial |
| 27374 | Sub7 default. Most script kiddies do not change from this. | Unofficial |
| 27500 - U | (Through 27900) id Software QuakeWorld | Unofficial |
| 27900 | (Through 27901) Nintendo Wi-Fi Connection | Unofficial |
| 28910 | Nintendo Wi-Fi Connection | Unofficial |
| 29900 | (Through 29901) Nintendo Wi-Fi Connection | Unofficial |
| 29920 | Nintendo Wi-Fi Connection | Unofficial |
| 30564 - T | Multiplicity: keyboard/mouse/clipboard sharing software | Unofficial |
| 31337 - T | Back Orifice — remote administration tool (often a Trojan) | Unofficial |
| 32976 - T | LogMeIn Hamachi (VPN tunnel software; also port 12975) | Unofficial |
| 33434 - T, U | Traceroute | Official |
| 34443 | Linksys PSUS4 print server | Unofficial |
| 37777 - T | Digital Video Recorder hardware | Unofficial |
| 36963 | Counter-Strike 2D multiplayer (2D clone of popular Counter-Strike computer game) | Unofficial |
| 40000 - T, U | SafetyNET p Real-time Industrial Ethernet Protocol | Official |
| 47808 - T, U | BACnet Building Automation and Control Networks | Official |
