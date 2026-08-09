# Chapter 32. Remote Access

**IN THIS CHAPTER**

- Remote access methods
- How remote desktop applications are used
- Remote connection protocols
- Remote access servers' roles in authentication and access

Remote access describes a system of client/server software that connects a remote client to a remote access server. In this chapter, remote access software that connects clients through the Public Switched Telephone Network is highlighted, but the trend in this area of software is toward remote clients connected using Virtual Private Network (VPN) connections over the Internet. A variety of remote access connection protocols are used, including SLIP, PPP, PPPoE, PPTP, and L2TP. Their relationship to remote access software is described.

Remote desktop software allows a client system to remotely connect to a host system so that the desktop of the host is shown on the client system; this software will be described in this chapter. Among the uses of remote desktop software are remote computing, remote system management, help desk applications, remote learning, and thin client/server applications. Remote desktop protocols are low-bandwidth connections that are optimized to send graphics data from server to client.

The different remote desktop connection protocols, such as ICA, RDP, X11, and others, are described. Among the applications described are Microsoft Remote Desktop Connection, Citrix GoToMyPC, and others.

Remote access servers not only provide a connection to a network but must also allow access to the network based on the user's credentials. One remote access server in common use is the Remote Authentication Dial-In User Service (RADIUS) system. RADIUS is an authentication, authorization, and accounting ("Triple A") server.

The nature of a RADIUS session is described, as is the range of different devices that the RADIUS service may be found on. RADIUS can be used to validate roaming clients. A future version of RADIUS called the Diameter protocol is discussed.

# Remote Access

Remote access technology appears in nearly all network server operating systems, supported by applications offered by the operating system vendor or vigorously supported by the third-party market. It is used to enable remote clients to connect to the local area network securely. Typically the Remote Access Server (RAS) runs on a server, and Remote Access Client (RAC) software runs on the client as a client/server application. The client connects to the server either through a dial-up connection, or over the Internet using a standard Internet connection technology such as ADSL, ISDN, or something else over a Virtual Private Network (VPN).

Remote access server technology used to be the preferred connection technology when clients connected over dial-up connections on the telephone network. Dial-up access had a number of significant advantages: telephone lines were ubiquitous worldwide, modem technology based on digital audio conversion (DAC) technology was inexpensive and could be miniaturized, and the dial-up connection technology used was independent of any network hardware or software that a system was using.

[Figure 32.1](ch32.html#remote_access_is_most_often_applied_to_s) shows some of the common scenarios for remote access technology. The four most common remote access scenarios are users connecting to a LAN through a Remote Access Server (often a RADIUS server), over the Internet from a client on another LAN (say in a branch office), from a computer in a SOHO (Small Office Home Office), or a remote client (usually a laptop) connecting through a wireless access point.

Although the cost of dial-up tended to be high and the security of a dial-up connection was low when dial-up connections were first used, as the technology matured, dial-up got cheaper and security protocols were developed that improved the connection security. The one factor of dial-up technology that can't be improved is the overall transfer speed. The bandwidth of a standard phone line connection (D0) is 56 Kbits/s, and although modems could approach this throughput with advanced compression technology, modems couldn't advance much beyond this limit. The use of multiple phone lines ganged together has served as an interim solution, but for the most part, phone line connections are being replaced by mobile network connection technologies such as Wi-Fi and DSL.

For all of these reasons, remote access server technology isn't nearly as important a topic as it used to be, although RAS is an important part of VPNs. The use of RAS over the Internet has become the most widely used form of remote access because Internet connectivity has become pervasive in most countries and regions. When connecting over the Internet to a RAS server using a VPN connection, you gain the advantage of a much higher bandwidth and much smaller incremental charges than phone lines, as well as the many authentication and encryption options that have been developed for the Internet protocol suite.

![Remote access is most often applied to services provided for remote clients connected over the public telephone network.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3201.png)

**Figure 32.1. Remote access is most often applied to services provided for remote clients connected over the public telephone network.**

### Note

VPNs are covered in [Chapter 29](ch29.html).

The whole point of remote access is to provide an experience for a connected user that is identical to the experience that the user might have with a direct connection to a LAN. To enable this experience, not only must the bandwidth of the connection be sufficiently high, but the user must also be authenticated and authorized on a per-resource basis, and the connection must be sufficiently protected. Modern remote access technology focuses on these three issues, as well as providing for an accounting function that service providers need.

In the sections that follow, you learn about some of the standard protocols used to make remote connections possible, the services that work with these standard protocols, and technologies that allow you to view the desktop of a remote system on your local computer.

## Remote connection protocols

It is through the use of a remote access protocol that the connection between the remote user and the remote access server can be managed. The most commonly used remote access protocols today are:

- Serial Line Internet Protocol (SLIP)
- Point-to-Point Protocol (PPP)
- Point-to-Point Protocol over Ethernet (PPPoE)
- Point-to-Point Tunneling Protocol (PPTP)
- Layer 2 Tunneling Protocol (L2TP)

### Note

All of the aforementioned protocols are described in detail in [Chapter 29](ch29.html), and all are connection protocols.

The SLIP, PPP, and PPPoE protocols are used for dial-up remote access, whereas PPTP and L2TP are used for VPN protocols when connecting remotely from one LAN to another (a WAN connection). Remote access requires more than simply a connection method. In order to authenticate and authorize a remote connection, different protocols needed to be developed. The most important authorization service in use is the Remote Authentication Dial-In Service (RADIUS), which is discussed in detail later in the chapter. The Microsoft version of RADIUS was called the Internet Authentication Service (IAS) prior to Windows Server 2003, and the Network Policy Server (NPS) from Windows 2003 on forward.

The original remote connection protocol by dial-up was SLIP; it was developed as the method for connecting green-screen terminals to mainframes, particularly to large UNIX-based systems. SLIP, which stands for Serial Line Internet Protocol, is a method for connecting to the Internet using serial ports and modem communications. SLIP is now considered to be obsolete, having been replaced by PPP, which has more advanced support for addressing and error control. SLIP continues to see limited use in situations where low-overhead communications are essential, such as in microcontroller applications, and in the BlueCore Serial Protocol used by some Bluetooth controllers.

## Remote access services

A remote access service is a network service that accepts incoming connections from remote users, validates the credentials of the user, creates a secure connection, and serves as a gateway for access to network resources. Remote access servers can be implemented to accept connections in any one of the following types:

- From PPP or SLIP connections using DSL modems over WAN connections, that is, over long-distance links
- Routed traffic over an IP network
- VPN connections over an IPsec tunnel or some other secure connection typeNoteVPN connections over an IPsec tunnel are discussed in [Chapter 29](ch29.html).
- ATM broadband connections, or some other WAN protocol
- An asynchronous terminal connection using Telnet, TN3270, or a similar type of connection

Many remote access servers accept some combination of the aforementioned traffic, and often can translate between the different protocols that are used, when needed.

While most of the original RAS servers supported dial-in connections, today RAS is more commonly used for remote broadband services. When a remote access server is used for routing Internet traffic, it is referred to as a broadband RAS, or alternatively BRAS or BBRAS. BRAS are used to aggregate traffic from Digital Subscriber Line Access Multipliers (DSLAMs) so that the traffic can be managed and Quality of Service (QoS) can be applied. A BRAS is the endpoint of a remote client's PPP connections (either PPP over Ethernet or ATM), and adds the necessary session-level information, such as IP destinations, to packets that enable the communication to find its target. Many BRAS servers are front ends to a variety of AAA servers (Authentication, Authorization, and Accounting), the most common of which are the RADIUS servers that are described in detail later in the chapter.

## Remote desktops

The term *remote desktop* is applied to software and a connection protocol that allows a remote system to display the graphical user interface of the system it is connected to inside a window on the client. While remote desktop technology is a form of remote access, it is different in both implementation and impact from the other types of remote access that this chapter has focused on. While remote access allows a client to gain access to network resources just as if the remote client were a local system, remote desktop software allows the client to control and view the server system as if the user were sitting in front of the system itself. An active remote desktop connection is referred to as a *session*, the same name given to a terminal server connection.

Remote desktop technology is used in the following applications:

- Remote computing applications
- Remote system management applications
- Help desk applications
- Remote learning applications
- Thin client/server applications

Remote desktop clients connect to systems using VPN connection protocols that are optimized for low-bandwidth transmission of keyboard and mouse input from the client, and display output from the server. These connection protocols are typically encrypted; the data that flows over these connections is highly compressed, making it possible for the client to connect to the server over low-speed connections such as phone lines with very good performance on the client. Remote desktop connection protocols are therefore a form of VPN connection protocol with emphasis on optimized graphic capabilities and remote printing and not necessarily focused on overall data throughput.

### Note

For a comparison chart of remote desktop software by product name, operating system, and capabilities, go to `en.wikipedia.org/wiki/Comparison_of_remote_desktop_software`.

The most important remote desktop protocols in use today are:

- **Independent Computing Architecture (ICA)**, the Citrix proprietary protocol that is used with Citrix WinFrame and XenApp (formerly called the Citrix MetaFrame and Presentation Servers).
- **Remote Desktop Protocol (RDP)**, the Microsoft connection protocol used by its remote desktop software to connect to Windows systems. Clients using RDP are available for all modern desktop operating systems, and RDP clients can connect to systems using the Windows TS Gateway available in Windows 2008.
- **X Window System v X11**, used by many operating systems, but particularly UNIX and Linux, to connect clients to server systems.
- **NX Technology (NX)**, a protocol that can be used by X Window Systems as an alternative to the X11 protocol.
- **Virtual Network Computing (VNC)**, which uses the Remote Frame Buffering (RFB) protocol for remote desktop connections, is used by the RealVNC open source software.

ICA, RDP, and X11 work by using kernel-level drivers to redirect the graphic display subsystem output to the remote client. The other remote desktop connection protocols used by software such as PC Anywhere, VNC, and others use application-layer software to create and manage the VPN connection.

The Microsoft native Windows RDP server software is referred to as *Terminal Services* in Windows 2000, and *Remote Desktop Services* in Windows 2003/XP, Windows Server 2008/Vista, and Windows 7. On the Mac OS X desktop, the software is called *Remote Desktop*. Two open source RDP clients are XRDP (`xrdp.sourceforge.net`) and RDESKTOP (`www.rdesktop.org`). [Figure 32.2](ch32.html#the_remote_desktop_connection_client_in) shows the Remote Desktop Connection client connection properties dialog box, which alters the features that you see in the remote desktop client software based on the speed of the connection you are using. You can also turn features on and off if they are of interest or if you want to improve performance.

### Note

Microsoft offers a Web conferencing service called Microsoft Live Meeting (`office.microsoft.com/en-us/livemeeting/default.aspx`), and their enterprise conferencing server system is the Office Communications Server 2007 (`office.microsoft.com/en-us/communicationsserver/default.aspx`). LiveMeeting replaced the older NetMeeting product. Other important products in this area include IBM Lotus Sametime (`www.ibm.com/sametime`), Glance (`www.glance.net`), and WebEx (`www.webex.com`).

![The Remote Desktop Connection client in Windows 7 and Vista allows you to adjust the features available in a remote desktop window.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3202.png)

**Figure 32.2. The Remote Desktop Connection client in Windows 7 and Vista allows you to adjust the features available in a remote desktop window.**

Remote desktop software is widely used in the help desk market. The two best-selling products in this area are Symantec (formerly Norton) pcAnywhere v12.5 (`www.symantec.com/norton/symantec-pcanywhere`) and Citrix Systems' GoToMyPC (`www.gotomypc.com/`). Symantec sells its product as a client/server application, while Citrix has combined the client/server software with a Web-based subscription service that transmits highly encrypted data in a manner that allows GoToMyPC clients to work through very selective firewalls.

[Figure 23.3](ch23.html#a_conceptual_diagram_of_a_service_orient) shows GoToMyPC system architecture. GoToMyPC uses the GoToMyPC Broker to listen for session connection requests, authenticate clients, and then initiate a GoToMyPC session. Once the session is under way, the GoToMyPC Broker uses the Encrypted Polling Protocol (EPP) to ensure that the remote PC and host PC are the validated endpoints in the session that it created. This approach prevents another system from intercepting GoToMyPC traffic. Because all data flows through the GoToMyPC Communications Server where the encrypted packets are relayed, communications between the Broker and Communications Server is the additional check that maintains the validity of the host and remote systems in the remote desktop session.

GoToMyPC has been extended to include the GoToAssist conferencing feature and is sold as the GoToMeeting subscription service by Citrix Systems. This software broadcasts the desktop of a remote computer to a set of GoToMeeting clients over the Internet. The broadcasts are encrypted and password protected, and use a host-based architecture similar to that used by GoToMyPC. GoToMeeting can allow a single application to be shown, or the entire host desktop; it can also allow any of the participants to take over control of the host system, as well as record the session for later playback. A more expanded version of GoToMeeting called GoToWebinar, which allows for larger audiences, is also available.

![The GoToMyPC system architecture uses a Web-based set of servers to authenticate sessions and to manage and relay session data.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3203.png)

**Figure 32.3. The GoToMyPC system architecture uses a Web-based set of servers to authenticate sessions and to manage and relay session data.**

# RADIUS Servers

The Remote Authentication Dial-In User Service (RADIUS) is the name of a networking protocol that allows remote users to be authenticated and connect to a LAN. RADIUS is deployed in the form of RADIUS servers, which can range from small RADIUS servers deployed on a SOHO network for a few users up to large enterprise-class RADIUS servers deployed in large telecommunication companies (TELCOS) or ISPs that service thousands of user connections, and all sizes in between. RADIUS also plays a central role in IEEE 802.11i security and works along with WEP to create a secure tunnel with Extensible Authentication Protocol (EAP) or Protected Extensible Authentication Protocol (PEAP) between remote clients and the Wi-Fi network. RADIUS is also commonly used by VoIP systems, where remote clients such as broadband phones connect to the VoIP server using a secure technology such as the Session Initiation Protocol (SIP) to the SIP registrar server.

### Note

802.11*x* Wi-Fi technologies are described in [Chapter 14](ch14.html). For information about VoIP, return to [Chapter 26](ch26.html).

RADIUS servers are essentially security gateways, and fall into a class of network services that are often referred to as AAA ("Triple A") servers. AAA servers refer to the following functions:

- **Authentication**. The RADIUS server provides a means to identify a remote user, and to enable or disable their connection. During authentication, a RADIUS server can determine whether the user's phone number is the authorized phone number, whether that user has a session in progress, as well as perform other tasks. Thus RADIUS can prevent a user with a stolen password from calling into a system from an unknown phone number.RADIUS servers may maintain a copy of the network user accounts, or it can be part of what is referred to as a *Pluggable Authentication Service* (PAM) architecture where authentication is passed through to a network access server or a domain server. Although storing user account information on a RADIUS server is certainly convenient from a manageability standpoint, doing so provides an attacker with all of the security information necessary to compromise the network should they gain access to the system. For this reason, it is preferred to have RADIUS pass authentication through to other servers on a session-by-session basis.
- **Authorization**. The RADIUS server determines the access rights and privileges that the user can have on the network. Authorization also determines the connection type that the RADIUS client may provide, such as PPP or Telnet.
- **Accounting**. RADIUS servers maintain detailed event logs and can organize event data to provide usage data for billing or accounting purposes. A RADIUS client sends usage information periodically to the RADIUS server during sessions, and the client can send an accounting request message to the server when logons or logoffs occur.

### Note

RADIUS is an open standard as described in IETF RFC 2865 (`tools.ietf.org/html/rfc2865`). The accounting functionality in RADIUS is described in IETF RFC 2866 (`tools.ietf.org/html/rfc2866`). However, because RADIUS is extensible, different vendors implement RADIUS using their own set of attributes.

RADIUS servers are used in a wide variety of applications. You will find RADIUS as one of the services in routers; wireless access points; just behind firewalls or proxy servers in a perimeter network; as part of Web and e-mail servers; as Internet facing devices; and in VPN systems. RADIUS is the default authentication protocol for wireless networks conforming to the new 802.11i Wi-Fi standard.

Cisco uses the remote authentication protocol standard called the Terminal Access Controller Access-Control System (TACACS) in its routers and network servers. The original version of TACACS was designed for use in authenticating UNIX servers. Cisco has gone on to update and extend TACACS into a version called TACACS+ that is both a proprietary Cisco standard and incompatible with the original version of TACACS. Cisco recommends TACACS+ instead of RADIUS, even though both protocols are often available on Cisco routers. Cisco has published the specifications for TACACS+ as an IETF RFC draft (see `http://tools.ietf.org/html/draft-grant-tacacs-02/`). TACACS+ is used for authentication and authorization, but not for accounting, and runs over TCP port 49 by default.

In the two sections that follow, you learn about the elements of RADIUS sessions and the way in which RADIUS allows mobile clients to roam.

## RADIUS sessions

A RADIUS session has the following steps:

1. A remote user connects to a RADIUS client device using PPP or another Data Layer link protocol, and initiates a login.
2. The RADIUS client — a router, gateway, Network Access Server (NAS), or another device — creates a secure encrypted connection to the RADIUS server using a shared secret MD5- generated key encryption mechanism.RADIUS uses UDP port 1812 for authentication and 1813 for accounting. Older implementations of RADIUS used the unofficial ports 1645 and 1646 for these two functions, respectively. Some RADIUS implementations use both sets of ports; Microsoft uses 1812/1813 while Cisco and Juniper Networks RADIUS servers use 1645/1646.
3. A RADIUS Access Request message is then transmitted to the RADIUS server with the login information (user ID and password), system information (network address and login location) included using the Password Authentication Protocol (PAP), Challenge-Handshake Authentication Protocol (CHAP), or Extensible Authentication Protocol (EAP).
4. The RADIUS server verifies the login request either against a local database or with the authentication service running on the network.Authentication services can include LDAP servers (for a domain validation), Active Directory servers (on Windows networks), Kerberos servers (for a certificate validation), or SQL Server (or some other database for a database validation).
5. The validation then results in an Access Accept, Access Reject, or Access Challenged response.*Access Accept* provides the user access to the resource that was requested. An Access Accept condition does not apply to all resources; each additional resource is checked as required, and the RADIUS client also verifies the original access offered on a periodic basis.*Access Reject* locks the user out of the network, denying them access to the resource that was requested.*Access Challenge* occurs when the system requires additional information in order to create a secure channel from the RADIUS server to the remote client that tunnels through the RADIUS client.
6. An Access Accept response results in the NAS (Network Attached Storage) providing the following services to the remote client: supply a static or dynamic IP address; assign a Time-To-Live for the session; download the client's Access Control List (ACL); and set up for L2TP, VLAN, and any QoS session parameters required.
7. Once the session is established at the RADIUS client, accounting begins with an Accounting Start message, which creates the session account record. Subsequent Interim Accounting messages populate the session account record, and an Account Stop message closes the session account record out.Accounting information that is stored includes the following: time of session; number of packets and amount of data transferred; user and machine identification; network address; and point of attachment information. This database can then be used to generate billable information and statistical reporting, or for any other purpose.

RADIUS servers are available as open source freeware and shareware programs such as FreeRADIUS (`www.freeradius.org`), GNU Radius (`www.gnu.org/software/radius`), and OpenRADIUS (`www.xs4all.nl/~evbergen/openradius/`), among others; they are also available as commercial programs such as Juniper Networks' Steel Belted Radius (`www.juniper.net/products_and_services/aaa_and_802_1x/steel_belted_radius/index.html`), and in some network server operating systems such as Windows Server. RADIUS was added to Windows as the IAS Server, starting with Windows Server 2000 in the Option Pack.

In Windows Server 2008, the Microsoft RADIUS server was renamed from the Internet Authentication Service (IAS) to the Network Policy Server (NPS), but the functionality remained about the same. RADIUS is now a relatively mature technology. [Figure 32.4](ch32.html#a_radius_server_deployed_on_a_windows_se) shows how an NPS server is deployed on a Windows network. In this scheme, the NAS operates as the RADIUS client and provides the necessary network access once the authentication request to the RADIUS server is returned successfully.

![A RADIUS server deployed on a Windows Server 2003 or later network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3204.png)

**Figure 32.4. A RADIUS server deployed on a Windows Server 2003 or later network**

A RADIUS server can be configured to be a RADIUS client to other RADIUS servers. That is, a RADIUS server can perform the function of a proxy client, passing through authentication and accounting to other RADIUS servers. This proxy function is important when you deploy RADIUS in a perimeter network and need to ensure authenticated access to other portions of the network.

## RADIUS roaming

Many RADIUS implementations require that the client be mobile and therefore must support a roaming feature. When a RADIUS client roams between networks, the client must have the AAA status moved to a different RADIUS server. Each set of RADIUS servers exists in what is called a *realm*. In order to identify a remote user connected to a RADIUS server, the server information is added using an @ sign and a postfix or by adding a backwards slash "\" and a prefix to the name of the client, or both. An example of the extended name would be domain_1.ext\userid@domain_2.ext, where two realms are indicated. A realm is simply a name given to the RADIUS server group and is not registered or tracked in any way; therefore, realm names are totally arbitrary.

Realms are stored in tables on the RADIUS servers, and any unknown realm must first be contacted or configured before a roaming client is allowed onto a network. RADIUS servers therefore play the role of a proxy server in that they forward AAA requests from roaming remote users that they can't find in their realm table to the domain server of the roaming client. The roaming table is manageable, and additional RADIUS servers can be added, modified, or stripped (removed) from the table. RADIUS doesn't specify how these management functions are implemented.

A remote client connects through a RADIUS client using a secure authenticated connection. When the client roams, security issues arise concerning how to establish a new secure connection. RADIUS solves this problem by establishing a two-layer security scheme, the details of which are dependent on the vendor implementation. With EAP, a secure tunnel is created between the authenticating RADIUS server (the inner identity) and the domain server, and an additional tunnel (the outer identity), which communicates in clear text, is used to allow proxy systems to route the packets appropriately. A roaming system can also create a secure, encrypted tunnel between RADIUS servers, thus hiding the user's security details from further view.

## The Diameter protocol

RADIUS technology is getting a little old. The technology was first described by Merrit Network for NSFnet and developed by Livingston Enterprises in 1991. The replacement technology that is currently being developed is known as the Diameter protocol. Diameter replaces RADIUS's use of UDP transport with the reliable transport protocols TCP and SCTP. The name Diameter is a takeoff on the name RADIUS, as a diameter is twice the length of a radius, so the name has no other significance. As defined currently, the Diameter protocol is not backwards compatible with RADIUS, but RADIUS systems can be upgraded to Diameter.

Diameter is currently defined by the IETF RFC 3588 (`tools.ietf.org/html/rfc3588`) and includes all of the elements for an AAA server that RADIUS has. A Diameter service can be extended with vendor-specific attributes and with additional commands. As with RADIUS, Diameter is a connection protocol and not an application. Diameter offers both Network and Transport layer security and can create secure tunnels over IPsec or TLS, over either stateful or stateless connections. There are a number of either new or improved features in Diameter that weren't in RADIUS, including:

- Dynamic peer discovery with Domain Name Service Records (DNS SRV) or Name Authority Pointer Records (NAPTR)
- Application layer acknowledgment and error messaging
- Session capability negotiation
- A client-server architecture
- Improved roaming capabilities
- A full set of AAA functions

A Diameter session between two peers begins first with the creation of a TCP or SCTP transport connection. One node acts as the initiator and the other acts as the target. The initiator sends a Capabilities-Exchange-Request (CER) to the target, which responds with a Capabilities-Exchange-Answer (CEA), leading to a negotiated TLS connection. Once the connection is established, applications can begin exchanging messages.

A TLS connection is monitored for activity. If a certain period of inactivity is detected, either peer sends a Device-Watchdog-Request (DWR) to the other peer, and that peer must return a Device-Watchdog-Answer (DWA) in exchange. Failure to exchange this information leads either peer to send a Disconnect-Peer-Request (DPR) message. If a Disconnect-Peer-Answer (DPA) isn't forthcoming, then the transport protocol is contacted and the connection is terminated.

### Note

You can use the search page at `www.ietf.org/rfc.html` to find the RFCs mentioned in the following list, or any of IETF's other RFCs. The general form for any RFC URL is `www.ietf.org/rfc/rfc####.txt`, where #### is the RFC number padded with zeros to get to four digits if necessary.

Among the various Diameter-enabled applications so far defined by the IETF, you will find the following:

- Applications that are part of the 3GPP IP Multimedia Subsystem (`www.3gpp.org/`) for wireless connectivity
- Bootstrapping Server Function for mutual authentication of cellular network devices and servers, which is part of the 3GPP Standard (`www.3gpp.org/`)
- Diameter Credit-Control Application (DCCA, RFC 4006; `tools.ietf.org/html/rfc4006`)
- Diameter Extensible Authentication Protocol Application (RFC 4072; `tools.ietf.org/html/rfc4072`)
- Diameter Mobile IPv4 Application (MobileIP, RFC 4004; `tools.ietf.org/html/rfc4004`)
- Diameter Network Access Server Application (NASREQ, RFC 4005; `tools.ietf.org/html/rfc4005`)
- Diameter Session Initiation Protocol Application (RFC 4740)

# Summary

In this chapter, different remote access technologies were described. Remote access used to be concerned primarily with low-bandwidth phone connections of clients to servers. The penetration of broadband technologies and the Internet has made VPN connections the dominant form of remote access. In this chapter, the various forms of remote access technologies were surveyed.

Remote desktop software is a related client/server technology to remote access. However, unlike remote access, where the connection is optimized for maximum data throughput and the remote client appears as a connected node on the network, remote desktop connections are optimized for graphic data transfer and low bandwidth. Different types of remote desktop software were described.

Remote access servers not only function as a point of access to a network, but they must also validate the client and selectively allow the remote client access to network resources. RADIUS servers were described as an example of what is known as a "Triple A" server, which stands for the functions authentication, authorization, and accounting.
