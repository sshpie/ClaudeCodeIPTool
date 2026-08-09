# Chapter 29. Virtual Private Networks

**IN THIS CHAPTER**

- VPN and where it is used
- VPN types and topologies
- VPN devices and software
- VPN encryption, encapsulation, and transport protocols

Virtual Private Networks, or VPNs, are a fundamental building block for creating secure links and for enabling secure internetworking. To create VPNs, you need to create a connection, usually one over a public provider network such as the Public Switched Telephone Network (PSTN) or the Internet.

VPNs use a whole host of Data Link and Session layer protocols — Levels 2 and 3 in the OSI model. Some of these protocols are used to secure the data, usually by a process of encryption using cryptography. Other protocols encapsulate data to provide the necessary mechanism to support the VPN connection. Still other protocols are used to transport data over a VPN.

When the payload portion of a packet is encrypted and encapsulated, that data is sent using VPN transport. When the entire packet, both the payload and header, is encrypted and then encapsulated, the data is sent using VPN tunneling. VPN tunneling is most often either remote access or site to site.

VPNs are a combination of hardware and software. VPNs require a routing function to establish a connection and the software necessary to provide the data translation and packaging mechanisms. The various devices used on VPN systems — routers, gateway/concentrators, network access servers, and others — are described in this chapter.

A variety of VPN software packages, such as OpenVPN, LogMeIn Hamachi, and tinc, are mentioned. The procedure to create a VPN link between Vista and Windows Server 2008 is also described.

Tunneling and encryption protocols are covered in detail, as is the encapsulation process. Encryption on IP networks often uses the IPsec protocol suite. A common protocol for encapsulation is the Generic Routine Encapsulation protocol. The various point-to-point protocols used to enable remote access VPN — PPTP, L2TP, and L2F — are also described.

# VPN Technologies

In a highly connected world, there is a need for people and organizations to communicate securely with one another. Local Area Networks (LANs) are secured by methods such as Challenge Handshake Authentication System (CHAP), but these methods are less secure when a network is shared or when Wide Area Network (WAN) links are used. Remote users of a network provide yet another set of issues. The cost of maintaining leased lines for WAN links is cost prohibitive for organizations, as well as being impractical for the average user.

A solution to this problem is the use of Virtual Private Networks, or VPNs, to create secure links over a connection defined by a virtual circuit. A VPN is a private data network that connects over public networks with tunneling and security protocols.

## VPN types

Historically, VPNs developed first over private leased telephone lines, and then over public networks. The first type of VPNs were called *trusted VPNs* and relied on the privacy of the leased line for its security. Because trusted VPNs can transit a number of devices en route, the VPN clients are depending upon the VPN service provider to maintain security.

Trusted VPNs use the following Data Link Layer 2 or Session Link Layer 3 technologies:

- **ATM Layer 2 virtual circuits**.
- **Frame relay Layer 2 virtual circuits**.
- **Multiprotocol Label Switching (MPLS) Layer 2 frame transport**.
- **The Draft Martini transport uses ATM, Frame Relay, Ethernet, Ethernet VLAN, PPP, High Data Link Control (HDLC), or any other point-to-point transport over MPLS**. Draft Martini is sometimes called Any Transport over MPLS (AToM). Draft Martini is a Layer 2 protocol.
- **MPLS routing controlled by the Layer 3 Border Gateway Protocol (BGP) used on the Internet**.

The Internet made security even more problematic. Trusted VPN technology could not be counted on to protect the data en route from snooping. To make VPN more secure, encryption was applied and removed at the endpoints of the VPN prior to transiting the Internet. The endpoints were often edge routers or other devices. VPNs of this type are called *secure VPNs*.

Secure VPNs use the following encryption protocols:

- **IPsec encryption using either tunnel or transport**.
- **L2TP over IPsec for remote access client/server VPNs**.
- **IEEE.802.1Q tunneling (Q in Q)**. This tunneling protocol can tunnel data in the Ethernet 802.1Q frame format on a shared backbone by adding an additional Q tag to the beginning of the header.
- **MPLS LSP**. A Label Switch Path (LSP) connects Label Switch Routers (LSRs) over an MPLS network.
- **Secure Sockets Layer (SSL) 3.0 or Transport Layer Security Protocol (TLS, or less commonly TLSP) with encryption**.

IPsec, L2TP, and TLS are all IETF standards. SSL is an earlier version of TLS. These are all Level 4 Transport layer protocols used on the Internet to place encrypted payloads into routable packets.

The third category of VPNs combines aspects of the first two and is called a *hybrid VPN*. On a hybrid VPN, the Internet is assumed to be a WAN and a secure VPN segment is created that spans that part of the VPN. The remaining portions on either side may or may not be secured, but at a minimum, they offer the capabilities of a trusted VPN. Vendors offering hybrid solutions provide a management console that can create and modify the VPN, providing a guaranteed Quality of Service that a VPN provider meets. Hybrid VPNs can be created on any type of secure VPN that can be carried over a trusted VPN.

## VPN links

Broadly speaking, there are four different types of VPNs deployed today:

- **Internal LAN link**. This is a link from one computer to another within a LAN.
- **Intranetwork WAN links**. These are links from one LAN to another LAN on the same network.
- **Extranet WAN links**. These are links from one LAN to another LAN on different networks, often from one company to another.
- **Remote Access link**. This is a transient WAN link from a remote user or system. Remote access links are not shared.

VPN links can be created over dialup, broadband, network, and even wireless connections. Generally speaking, a VPN link can be either remote access or site to site. VPN technologies that encrypt the payload portion of their packets but not the header are referred to as *VPN transport*. VPN technologies that encrypt both the header and payload portion of the packets, and then encapsulate as datagrams within another packet, are referred to as *VPN tunnels*.

[Figure 29.1](ch29.html#different_types_of_vpns) shows VPN connections over different types of WAN links, such as a leased line, standard LAN line, or Wi-Fi link, from a conceptual standpoint. The routers, switches, and other devices necessary to implement a VPN are not shown in this figure, nor are the actual VPN endpoints. VPNs can be provisioned (configured and managed) either by a customer, as shown for the tunnel between Dilbert and his home office, or by a service provider over leased lines or the Internet. When one VPN provider's service is transported over another VPN provider's service, the VPN service is called a *carrier of carriers*. The resulting service offered to the customer is a carrier's carrier VPN service.

![Different types of VPNs](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2901.png)

**Figure 29.1. Different types of VPNs**

Service provider VPNs can be categorized as follows:

- IPsec VPN
- Virtual Private LAN Service (VPLS)
- Virtual Private Wire Service (VPWS)
- IP Private LAN Service (IPLS)
- Virtual Router (VR)
- BGP/MPLS

Customer VPNs are usually either of the following:

- IPsec VPN
- GRE VPN

## Site-to-site topologies

VPN can be implemented in either hardware or software; often VPN solutions are a combination of the two. High-performance VPN hardware can be found in many different network devices. Devices can be categorized by where they are on a VPN and their function. The broadest range of devices is found on a site-to-site topology where two sites connect across a provider network or VPN backbone. [Figure 29.2](ch29.html#a_site-to-site_vpn_topology) shows site-to-site topologies, which use many of the elements described in the following list of VPN device categories:

- **Customer (C) and Provider (P) systems**. Computers, routers, or switches on the source and destination LAN are connected by a VPN link. To those systems, the resource appears to be a local resource and the VPN is invisible. A P system can't connect to customer networks or view a VPN on the customer network.
- **Customer Edge (CE) and Provider Edge (PE) systems**. An edge device connects to another edge device, creating a WAN link. The CE device can view the VPN if that VPN is located on the customer network; the PE device cannot. The PE device can view the VPN if that VPN is on the provider network; the CE device cannot.A customer edge router and switch can be indicated as CE-r and CE-s, respectively, and the provider versions would be indicated as PE-r and PE-s. Some VPN edge devices can be both routing and switching and take an -rs label.
- **Gateway or Concentrator**. This device can be either the endpoint for a VPN connection or the endpoints of many VPN connections, respectively. They are typically used for edge devices in place of CEs or as a remote access entry for the VPN. These kinds of devices are often given several different names, depending upon their placement and the protocol that they use. You may see any of the following: PPTP Network Server (PNS), L2TP Network Server (LNS), or L2F Home or Network Gateway.
- **Network Access Server (NAS)**. These devices provide the network interface between a public network like the telephone system (Public Switched Telephone Network, or PSTN) and an IP backbone and can be a VPN tunnel endpoint.The function of a NAS is to authenticate a user logon request, and if it is authentic, to pass the traffic through. NAS are also used to provide these functions for VoIP services.NoteThe acronym NAS is also used for Network Attached Storage servers. Those devices are described in [Chapter 22](ch22.html).
- **AAA ("Triple A") servers**. These VPN servers perform authentication, authorization, and accounting services.Authentication verifies user, group, and machine accounts. Authorization provides the rules related to resource access. Both of these functions are usually implemented as pass-through security from a domain controller or another authority. If there is no security authority, the AAA server takes over these tasks. The accounting function provides statistical data that is helpful for maintaining security, for troubleshooting, and, of course, for billing.

![A site-to-site VPN topology](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2902.png)

**Figure 29.2. A site-to-site VPN topology**

VPN providers often employ an internally protected and redundant VPN backbone called a *Virtual Private LAN Service* (VPLS). This type of VPN is created by separating the Provider Edge (PE) device into one that faces the user (U-PE) and another that faces the network (N-PE). [Figure 29.3](ch29.html#the_provider_vpls_backbone) shows the internal elements of a VPLS backbone.

VPLS and the similar IP Only LAN Service (IPLS) VPNs are sometimes called Multipoint-to-Multipoint (M2M) VPNs. An example of a Point-to-Point (P2P) circuit VPN is the Virtual Private Wire Service (WPSN) VPN, Draft Martini, and L2TP v.3 emulated circuits. All of these technologies are based on Layer 2 protocols.

![The Provider VPLS backbone](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2903.png)

**Figure 29.3. The Provider VPLS backbone**

## VPN hardware

The Virtual Private Network Consortium (VPNC), which helps to create interoperability standards in this area, maintains a members list at `www.vpnc.org/member-list.html`. You can see a list of features supported by different products that use IPsec by vendor at `www.vpnc.org/vpnc-IPsec-features-chart.html`. That same list compiled for SSL is maintained at `www.vpnc.org/vpnc-ssl-features-chart.html`.

The two companies that are most associated with hardware VPN solutions are Cisco Systems (`www.cisco.com/en/US/products/hw/vpndevc/`) and Juniper Networks (`www.juniper.net/`).

Cisco is one vendor that sells end-to-end VPN solutions for a large range of situations. The Cisco 1700 series routers have built-in VPN. These routers can also be configured as a firewall within the Cisco Internetwork Operating System (Cisco IOS) that runs on the 1700s. A higher-performance VPN device is the Cisco Adaptive Security Appliance (ASA), which replaced their PIX Firewall and VPN 3000 Series Concentrator in 2005. The most current ASA models introduced in 2008 were the 5580 series. The 5580 comes with Cisco's Min OS 8.1 operating system, which can support SSL and IPsec VPN over six interface cards, with up to 10,000 remote users simultaneously connected by VPN.

## VPN software

There are many VPN software solutions. In this section, some of the better-known products are described, with an emphasis on open source/freeware products and capabilities built into operating systems.

One of the best-known VPN packages is the OpenVPN (`http://openvpn.net/index.php/home.html`) SSL client/server software. Versions of OpenVPN are available for Linux, Windows (2.1 supports Vista), and the Macintosh. OpenVPN is configured from either the command line as a daemon or service or by using one of the Graphical User Interface front ends that you can download from `http://openvpn.net/index.php/documentation/graphical-user-interface.html`.

With OpenVPN, you can create SSL/TSL VPN connections of various types, including remote access, site-to-site, Wi-Fi, and backbone links. The enterprise versions of OpenVPN support failover and load balancing between servers, as well as providing resource access controls. VPN connections can be authenticated by this software using certificates, smart cards, and other methods. The detailed How To page at `http://openvpn.net/index.php/documentation/howto.html#install` contains instructions on how to get started with the program.

Another popular VPN product on Windows is LogMeIn Hamachi (`https://secure.logmein.com/products/hamachi/vpn.asp?lang=en`). It is notable for its ease of installation and configuration. Hamachi is a UDP VPN that uses a mediation server to establish a connection between two peer endpoints and then instantiate (bootstrap) the direct connection. Once the connection is established, the server no longer participates in the VPN.

Originally a freeware product, LogMeIn still offers a basic version for free and has a commercial Premium version. The LogMeIn Hamachi product is a VPN service that creates a virtual network of up to 256 systems with 50 connected users over the Internet.

Among the other features offered by LogMeIn Hamachi are:

- Firewall and broadband router NAT traversal
- Remote access control using Windows Remote Desktop
- Network drive access
- Peer-to-peer and group chats
- User accounts with passwords and privileges
- Relays for connections when direct connections can't be made point-to-point
- Built-in Web proxy for users connected to a Hamachi network from a public location such as a cyber café
- It can run on a Windows server as a service.

Another open source VPN program that is available on multiple platforms is tinc (`www.tinc-vpn.org/`). Versions of tinc support Linux, OpenBSD, NetBSD, Windows 2000/XP, Mac OS X, and Sun Solaris on both IP v.4 and IP v.6 networks. tinc makes a best effort to send traffic between tunnel endpoints by the most direct route. The program offers the ability to bridge Ethernet segments.

Microsoft Internet Security and Acceleration (ISA) Server 2006, which runs on Windows Server 2003, can be configured as a VPN endpoint. Originally released in 1997 as Microsoft Proxy Server, it became a platform for security (firewall), routing, and caching functions. ISA Server creates VPNs using either Layer 2 Tunneling Protocol (L2PT) over IPsec, or the Point-to-Point Tunneling Protocol (PPTP). Both are discussed in more detail later in this chapter.

ISA Server 2006 has a feature called Quarantine Control. When a remote client connects to the server, the client is evaluated by a number of criteria that you specify either within the Windows security model or from a RADIUS server. If the client doesn't have anti-virus software or the latest patch from Microsoft Update, for example, then the client is given only limited access until the configuration changes.

A new version of Microsoft ISA Server is to be released for Windows Server 2008 under the name Microsoft Forefront Threat Management Gateway (TMG). It is expected to also be part of the Windows Essential Business Server. The product Web site can be found at `www.microsoft.com/forefront/default.mspx`.

### The Windows Server 2008 VPN Service

To create an incoming VPN connection on a Windows Server 2008, you need to turn the service on using the following procedure:

1. From the Control panel in the Network Connection dialog box, click File and then select the New Incoming Connection command.
2. In the Who may connect to this computer? dialog box (shown in [Figure 29.4](ch29.html#the_who_may_connect_to_this_computer_que)) of the Allow Connections to this Computer Wizard, select the user accounts that can connect by VPN to Windows Server 2008, and click the Next button.
3. In the How will people connect? page, disable the Through the Internet check box if the VPN is used on your LAN, or leave it enabled for a WAN connection; then click the Next button.
4. In the Networking software allows this computer to accept connections from other kinds of computers dialog box (shown in [Figure 29.5](ch29.html#the_networking_software_allows_this_comp)), make sure that the network protocols required for a connection are installed, and that their parameters are correct for the VPN connection you want to establish; then click the Next button.Make sure that the IP v.4 address is the one you will provide on the client side, or install IP v.6 if required.![The Who may connect to this computer? dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2904.png)**Figure 29.4. The Who may connect to this computer? dialog box**![The Networking software allows this computer page to accept connections from other kinds of computers dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2905.png)**Figure 29.5. The Networking software allows this computer page to accept connections from other kinds of computers dialog box**
5. The Wizard creates the incoming connection and posts the final dialog box that you see in [Figure 29.6](ch29.html#the_people_you_chose_can_now_connect_to).

![The people you chose can now connect to the computer dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2906.png)

**Figure 29.6. The people you chose can now connect to the computer dialog box**

### The Vista client

VPN client software is common to most operating systems. As an example, a VPN client for Windows Vista 64 is configured as follows:

1. Click Start, and then select the Network command.
2. Click the Set up a connection or network link, and in the Choose a connection option dialog box (see [Figure 29.7](ch29.html#the_choose_a_connection_option_or_networ)), select Connect to a workplace; then click Next.
3. In the How do you want to connect? dialog box (see [Figure 29.8](ch29.html#the_how_do_you_want_to_connect_question)), click Use my Internet connection (VPN).![The Choose a Connection Option or Network Wizard in Vista](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2907.png)**Figure 29.7. The Choose a Connection Option or Network Wizard in Vista**![The How do you want to connect? dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2908.png)**Figure 29.8. The How do you want to connect? dialog box**
4. The Type the Internet address to connect to dialog box appears (see [Figure 29.9](ch29.html#the_type_the_internet_address_to_connect)). In the Internet address field, type the Internet address as the FQDN (Fully Qualified Domain Name), or the IP address.
5. In the Destination name field, type the name that you want to appear for the virtual network interface in your Network Connections dialog box.
6. Select the Use a smart card option, the Allow other people to use this connection option, or the Don't connect now; just set it up so I can connect later option by enabling the check box or boxes; then click the Next button.You can check one or more of these check boxes, and change these VPN settings later.![The Type the Internet address to connect to dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2909.png)**Figure 29.9. The Type the Internet address to connect to dialog box**
7. In the Type your user name and password dialog box, enter the details and the domain name (optional), and then click the Connect button.The connection is established and the VPN network interface appears in the Network connections dialog box. The server appears in your Network folder when you browse for neighbors.

# Encryption

VPN traffic is encrypted and decrypted at the endpoints of the VPN connection by the software that creates the VPN. Encryption is either by public key or symmetric key encryption. Public key encryption, also known as asymmetric key encryption, works by using a private or public key to encrypt data and using the other key to decrypt the data once it arrives. The well-known Pretty Good Privacy (PGP) software uses a public key encryption system. Symmetric key encryption works by using the same secret key at each endpoint.

### Note

For more information on encryption, see [Chapter 27](ch27.html).

The symmetric key mechanism is essentially a key exchange. A commonly used method is the Diffie-Hellman key exchange. In this mechanism, the sender and receiver create a public/private key pair. The public keys are then exchanged between sender and recipient. Each endpoint then participates in creating a shared secret offline, and that shared secret is used as the key for the symmetric algorithm.

In a VPN route that goes from a PC on LAN A to a PC on LAN B, the following segments can be encrypted:

1. PC A to Server A
2. Server A to Router A
3. Router A to Firewall A
4. Firewall A across the WAN to Firewall B
5. Firewall B to Router B
6. Router B to Server B
7. Server B to PC B

The one link that is always encrypted, regardless of which endpoints you select, is segment 4, where the data travels across a WAN and can be seen by others. Many routers function as their network's edge device in place of firewalls, and servers may or may not be in the chain. Indeed, the destination endpoint can be a server. So there is considerable variance in how one goes about setting up a VPN connection.

# Tunneling

*Tunneling* is the name given to the process of encapsulation, routing, and the removal of encapsulation. Tunnels do not require that the data enclosed be encrypted, although it almost always is. The tunnel is a logical path, but it appears as if it is a point-to-point connection in the network. The devices that are inside the tunnel — routers, gateways, switches, or proxy servers — are invisible to the sending (source) and receiving (destination) systems.

Internet Protocol Security, or IPsec, is another method used to encrypt VPN traffic. When IPsec, GRE, PPTP, or L2TP (the carrier protocols) encrypts the data or payload of an IP packet and sends that packet to the VPN endpoint where the packet's payload is decrypted, this is called *IPsec transport*.

When IPsec or another carrier protocol encrypts the entire packet (both header and payload) and the encrypted packet is sent to the other VPN endpoint, this is referred to as a *VPN tunnel*. Tunneling works by encapsulating the encrypted packet inside another packet. The encrypted packet is referred to as the *passenger packet*. The container packet is unencrypted, and contains the addressing information. The endpoints of the tunnel are called *tunnel interfaces*, with the local side of the tunnel being the source and the remote side being the destination.

A tunnel is considered to be more secure than transport because more information is hidden from view; however, a tunnel requires more network resource overhead to operate.

The fact that a VPN tunnel uses encrypted packets means that the technology makes no demands on what kind of data the VPN carries. You can send any type of data through the tunnel, and even use addresses that are in private IP ranges and therefore non-routable. A tunnel can allow a user to send a packet type that would be disallowed at the port level and even perhaps by network security. If the sender knows that an application server has the private address 192.168.1.10, then the encrypted packets can be sent to that address, even if they come from outside the LAN. This feature makes VPN a very powerful technology.

# Tunneling Protocols

Tunneling uses a variety of different protocols for transport. One set of protocols are used to encapsulate the encrypted packet, another set is used as transport by the network that carries the tunnel (TSL/SSL, for example), and a third protocol is used in the header of the encrypted protocol that contains the addressing required by the packet (a wrapper). The wrapper can use IPsec, GRE, PPTP, and L2TP for packet encapsulation. For example, on the Internet, the carrier protocol would probably be TCP/IP, and for the encrypted header, the network transport protocol or passenger protocol used might be NBT for Windows, IPX for Netware, or perhaps the Internet Protocol on almost any network.

## Generic Routing Encapsulation

The Generic Routing Encapsulation, or GRE, protocol is commonly used as the encapsulation protocol for VPNs that connect one LAN to another. It is a routing protocol. GRE does not encrypt packets, but it can perform both multicasts and broadcasts. The edge router on the sending network uses GRE to package the passenger packet, and the edge router on the receiving network reads the header GRE information, extracts the passenger packet, and sends it on its way. GRE makes it appear as if remote networks connected by a tunnel are local to one another. GRE tunnels are often placed into VPN tunnels to use the encryption features VPN offers.

GRE supports physical IP addresses as well as valid logical or virtual IP addresses. For example, when you create a site-to-site VPN, you can use either the network interface address facing the client or the router's loopback interface address. A loopback interface is not the same as a NIC address. The loopback interface is a logical interface (or a set of them) on the router that is always on.

## IPsec tunnels

IPsec is a suite of protocols that can be used for encapsulation of IP traffic on tunnels for remote access as well as site to site. IPsec must run not only on endpoints of the VPN but also on the firewalls in between or any other device with a routing function, in order for the packets to be routed correctly. IPsec has the additional requirement that the devices running the protocol share a key and be configured to allow this type of traffic to be forwarded.

IPsec can be used in the IPsec tunnel mode, without the use of a carrier protocol. In this mode, IPsec also provides the encapsulation that the carrier protocol would. Typically, IPsec tunnels in a site-to-site topology go from the CE device on one site to the CE device on another through the provider network. The primary reason that you would create an IPsec tunnel is that it works on routers, gateways, and other endpoints that cannot run L2TP over IPsec or PPTP VPN tunnels.

## Secure Sockets Layer/Transport Layer Security

The Secure Sockets Layer (SSL) v.3 protocol creates secure connections for remote access users. The Transport Layer Security (TLS) protocol is the newer IETF standard that is derived by SSL v.3. In many ways, the two protocols are very similar.

TSL is an older protocol that was developed by Netscape. SSL's security isn't as powerful as IPsec, L2TP v.2, L2F, or even PPTP when the VPN doesn't include client software to enforce the security. Although these clientless connections are easy to create and configure, because SSL is included in all modern browsers, clientless or Web-based VPN connections are common. It is possible to strengthen SSL/TLS by adding client software that supports these protocols.

## Point-to-Point tunneling protocols

VPN tunnels over remote access links use the Point-to-Point Protocol (PPP) as their carrier over IP networks.

### Point-to-Point Tunneling Protocol

The Point-to-Point Tunneling Protocol (PPTP) is a Layer 2 Data Link protocol that tunnels remote access PPP data between a remote user and a NAS or gateway/concentrator. The PPTP tunnel can also be set up to include the remote access network segment.

PPTP provides either 40-bit or 128-bit encryption for a remote client connection. PPTP connections can use CHAP or EAP-TLS authentication from Microsoft. PPTP connections provide only the user authentication that PPP enables, and so this protocol should only be used when the source computer does not need to be authenticated.

The PPP packets that PPTP encapsulates are given a GRE and IP header. To encrypt PPTP on Windows, you can use the Microsoft Point-to-Point Encryption (MPPE) protocol. MPPE creates its session keys from passwords using either MS-CHAP (Challenge Handshake Authentication Protocol) or EAP (Extensible Authentication Protocol), which means that encryption is dependent upon the strength of the user's password.

[Figure 29.10](ch29.html#the_pptp_protocol_encapsulation_packet_f) shows a PPTP encapsulation packet. The encapsulation process adds an IP Header field and the protocol Header (shown here as GRE) to the front of the encrypted packet. From the standpoint of a router, the packet appears just like any other IP packet, with the PPP Frame being the packet's payload.

![The PPTP protocol encapsulation packet format](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2910.png)

**Figure 29.10. The PPTP protocol encapsulation packet format**

PPTP is an older format that is supported on Windows but not on many other platforms. Microsoft recommends that users adopt the L2TP protocol instead.

### Layer 2 Forwarding Protocol

Layer 2 Forwarding (L2F) is a Cisco protocol that tunnels PPP or SLIP (Serial Line Interface Protocol) frames. L2F is usually deployed on a NAS and a VPN gateway. The remote connections to the NAS are tunneled through the VPN that spans these two devices and forwarded to a home VPN gateway.

### Layer 2 Tunneling Protocol

The Layer 2 Tunneling Protocol (L2TP) v.3 allows a remote access user to connect a NAS to a gateway/concentrator tunnel and send PPP frames through it. The tunnel can also be extended to include the remote network segments.

Because L2TP doesn't have security, its traffic is usually secured by IPsec. Traffic can flow over ATM, Frame Relay, PPP, VLAN, or PPP over IP networks. L2TP v.3 is the latest of the three protocols and incorporates elements of both PPTP and L2F in it. L2TP encapsulates PPP frames into packets; IPsec encrypts those packets. L2TP over IPsec not only uses PPP user authentication but also requires machine authentication by either a certificate or shared key. L2TP is the PPP remote access protocol that is currently favored.

The L2TP packet is constructed by first adding the L2TP and UDP headers and the IPsec Encapsulating Security Payload trailer to the passenger packet. IPsec encrypts this data and then adds the IPsec Encapsulating Security Payload header and the IPsec Authentication trailer to the carrier packet. An IP address header is added to complete the L2TP encapsulated packet that is transmitted through the VPN tunnel. UDP is used because it is more efficient than TCP and because the use of a tunnel ensures that data will more often arrive in sequence. [Figure 29.11](ch29.html#the_l2tp_protocol_encapsulation_packet_f) shows an L2TP encapsulated packet.

![The L2TP protocol encapsulation packet format](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2911.png)

**Figure 29.11. The L2TP protocol encapsulation packet format**

While L2TP is a strong VPN protocol in wide use, it is not without its problems. As is true with many WAN technologies, L2TP over IPsec often has problems with Network Address Translation (NAT) Traversal on older platforms. The NAT routing system works at the firewall or proxy server by changing the IP address and potentially the port number in the UDP header, leaving the encapsulated IPsec portion of the packet untouched. If this redirection isn't done correctly or can't be recognized, the packet will be dropped when it reaches its destination.

# Summary

In this chapter, you learned about Virtual Private Networks, or VPNs, and how they are used to create secure links on networks, over WANs and on the Internet. Modern networking would not be possible without these important technologies. The first VPNs were created to transfer data over the telephone network. Later systems moved to leased lines, and then to the Internet.

VPN uses a number of Layer 2 and Layer 3 protocols to enable its technology. VPN links are typically either remote access or site to site. VPN data is sent using either VPN transfer or by VPN tunneling. Techniques used to secure VPN data — encryption, encapsulation, and others — were described in detail, as were a number of different types of VPNs that have been created.

The next chapter describes network management. Networks are big, complex structures that change frequently. The software and methods for managing networks and systems efficiently are important for a network of almost any size.
