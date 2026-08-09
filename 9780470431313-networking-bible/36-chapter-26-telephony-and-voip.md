# Chapter 26. Telephony and VoIP

**IN THIS CHAPTER**

- Telephone service and protocols
- PBX telephone systems
- VoIP
- Computer telephony integration
- Video telephony in action

Telephony is the marriage of computers and telephones, enabled by two different types of networks. Telephony covers a broad range of multimedia applications, including voice, video, business, and pleasure. It is always an area of great innovation and is supported natively in network operating systems by application programming interfaces, or APIs.

You can create a network of telephones using a Private Branch Exchange (PBX) System as a management server. PBXs can network with public switched telephone network (PSTN) telephones over phone lines or with IP-enabled phones over Ethernet. Two PBX server systems are considered in detail: the open source Asterisk system and Cisco Unified Communications Manager.

Voice over Internet Protocol, or VoIP, is a rapidly developing area of technology. VoIP can be implemented in software as a softphone, using IP phones, or by adapting an existing telephone using an Analog Telephone Adapter (ATA) to connect it to an IP network. This chapter discusses the properties of IP phones.

VoIP uses a special set of protocols to send and manage communications that are described in detail in this chapter. Session protocols include Session Initiation Protocol (SIP) and Skinny Call Control Protocol (SCCP), and packets are often in Real-Time Transport Protocol (RTP) format. The problems with firewalls and NAT (Network Address Translation) traversal are described, as well as how Simple Traversal of User Datagram Protocol (STUN) solves them in some instances.

Computer Telephony Integration, or CTI, is a set of application rules that allow VARs (Value Added Resellers) and developers to create custom telephone applications. These applications draw on telephony APIs to help call centers and businesses of all types, and to power intelligent telephone systems. CTI's capabilities are briefly described.

Dick Tracy had one, and so can you. Video telephony is on telephones, wireless phones, and Webcams, and in IM (Instant Messaging) systems. Some of the applications are described at the end of this chapter.

# Telephony

Telephony is a set of services that allow computers to transmit analog sound across a network as digital data. Telephony involves an audio-to-digital conversion on the input end and a digital-to-audio conversion on the output end. In some instances, telephony services transmit discrete communications, usually in the form of audio files over standard packet-switched networks. In other instances, telephony transmits audio as it is being created and streams the result to the recipient: one example, VoIP, is described later in this chapter.

Telephony applications on networked computer systems span the following categories:

- Voice calls over a circuit-switched telephone network
- PBX simulation systems with advanced call-handling features
- Conferencing over IP networks
- Voice response systems
- VoIP calls
- Collaboration systems, shared whiteboards, and remote desktop systems
- Automated calling technologies

The software for creating and managing digital telephony has been included in most operating systems with various levels of sophistication. The field of CTI 45 now enables computers to integrate peripheral devices that send and receive networked voice and data. To support these technologies, many operating systems ship with APIs to support these features. The Windows telephony API is referred to as Microsoft Telephony API (TAPI), Sun Microsystems, Inc., has a Java Telephony API (JTAPI), and the Macintosh and Linux operating systems have similar APIs.

Telephony has had a historical role in the development of computer networks, especially in the areas of switching and routing. Many large networks have been built specifically for telephone systems in an effort to replace the manual telephone exchange with an automated system. The result of this automation was the creation of PSTN. The computer software that enables an automated telephone exchange was referred to as a *Stored Program Control* exchange, but this term is historical and is no longer used.

Prior to the commoditization of computers, telephone services were sent as analog signals over circuit-switched networks, which today is referred to as p*lain old telephone service* (POTS). As data transmission became important and the volume of data traffic increased, telephone networks began upgrading their lines to provide digital services using Integrated Services Digital Network (ISDN) and Digital Subscriber Line (DSL) technologies. As phone lines morphed into digital communication networks, copper wire was replaced by light-conducting glass fiber.

# Private Branch Exchange Systems

A private branch exchange (PBX) system is a telephone network that is generally installed in a medium to large office. The PSTN connects to the PBX, supplying one or more telephone lines for incoming and outgoing calls. Incoming calls for an entire company can come into a PBX and be routed appropriately. Each telephone connected to the network is referred to as an *extension*.

Office telephone systems come in the following varieties:

- **Key system**. When the extensions have a set of buttons that users press to manually choose the outgoing line, they are referred to as key systems.
- **Centrex**. Centrex is a service that is offered by the telephone company where switching and the software to control the system are located at an end office or another central office. It is similar to a PBX. A Centrex system places telephone extensions on individuals' desks, which allows both internal and external calls.
- **PBX**. These systems can be either private or circuit switched, and often connect using POTS.
- **PABX**. Private automatic branch exchanges automatically select an available outgoing line.
- **ISDN PBX**. This type of PBX connects to an ISDN line.
- **IP PBX or IPBX**. With the implementation of digital networks, most PBXs now offer VoIP on this type of PBX.

These systems emulate the function of a telephone exchange: they establish, maintain, and disconnect connections. Most of them also provide usage information. The range of calling features of PBXs can be quite large, and they can add the following unique features to a standard home telephone line: auto attendant, automated directory services, call distribution, conference calls, custom greetings and welcome messages, music or radio on hold, paging, roaming extensions, voice mail, and voice message broadcasting. In the sections that follow, three different PBX systems are described: the open source Asterisk server, Cisco's Unified Communications Manager, and Microsoft's Response Point.

## Asterisk

Digium's Asterisk (`www.asterisk.org`) open source PBX software is one solution to create an IP or hybrid PBX system from a modestly powered computer. It is one of the more popular VoIP server applications and is widely used. Asterisk can run on various versions of UNIX, such as OpenBSD, FreeBSD, and NetBSD, as well as on Mac OS X, Sun Solaris, and Microsoft Windows. (The version that runs on Windows is called AsteriskWin32.) The hardware necessary to connect an Asterisk server to PSTN, T1, E1, and other networks is sold by Digium and a number of other vendors.

After installing Asterisk, the application must be configured to either be a VoIP system or a PBX. Setup involves altering a set of configuration files; a PBX requires a dial plan for each device. [Figure 26.1](ch26.html#the_asterisk_gui_provides_pbx_management) shows the calling rules for an outgoing call. These calling rules ensure that the telephone numbers called conform to a particular numeric pattern, how the call is routed, and what to do if the call fails to go through the primary routing.

![The Asterisk GUI provides PBX management in a Web interface. Shown here is the Edit Calling Rule dialog box for outgoing calls.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2601.png)

**Figure 26.1. The Asterisk GUI provides PBX management in a Web interface. Shown here is the Edit Calling Rule dialog box for outgoing calls.**

Asterisk has a programming language where extensions can be matched to contexts (scenarios) and actions can be assigned based on the logic you provide. The Asterisk Gateway Interface provides an API that can be accessed by Perl, Java, C, or PHP programs.

Applications that come with Asterisk are:

- `app_dial`. This program executes the rules for device-to-device connections.
- `app_meeting`. This program creates and manages conference calls.
- `app_voicemail`. This program stores and plays back voice messages.

There are a number of GUI interfaces that you can install to manage Asterisk. Digium offers asterisk-gui 2.0, and FreePBX is another. A distribution from trixbox called Asterisk@Home combines an installation of Asterisk and FreePBX together.

## Cisco Unified Communications Manager

Cisco Unified Communications Manager (CUCM) is PBX software that manages a variety of telephony products and the components that support them. The product is better known by its older name Cisco CallManager (CCM). Cisco CallManager is installed on a Cisco Media Convergence Server (MCS) or another approved platform. MCS can be clustered with a Publisher server being supported by eight subscriber servers.

CUCM's main function is to determine the nature of a dialed phone number and then communicate with the gateway to coordinate sending or receiving calls from the public phone or private IP network.

CUCM uses the Skinny Call Control Protocol (SCCP) for signal control of telephony hardware, as well as the Media Gateway Control Protocol or Session Initiation Protocol (SIP) to communicate with network gateways, bridges, and other components. With CUCM you can also support VoIP phone calls and H.323 sessions. These protocols are described in more detail later in this chapter.

The latest release of CUCM was version 7.0 released in September 2008. Cisco has a Windows version of CUCM as well as selling an appliance. System 7 unifies the version number of the various components that make up the Communication Manager suite, including consolidating the underlying data store on IBM Informix.

## Microsoft Response Point

Microsoft Response Point (`www.microsoft.com/responsepoint/default.aspx`) is voice-activated PBX software for offices with up to 50 telephones. A system of 10 phones would have optimal performance on a 100Base-T LAN. Service Pack 1 of the Response Point software supports both analog and VoIP telephones. IP calls use Session Initiation Protocol (SIP). Among the features of Response Point are integration with e-mail systems, and easy setup and management through a graphical user interface, as shown in [Figure 26.2](ch26.html#the_administrative_console_in_microsoft). The voice recognition is based on the Speech Server engine, and is powerful, easy to work with, and doesn't require training. Training is where the user gives the system voice samples so that the system can better understand the particular user's commands and speech patterns.

Response Point is built to be an open system that interoperates with hardware from a number of vendors. The software is built to run on a version of Microsoft Embedded XP software, which is supplied in the form of small appliance-sized devices from various hardware partners. When you plug the appliance into the network and turn it on, a setup wizard launches that prompts you to plug in the phones and assign them to users or locations. Configuration takes about 15 minutes to perform, which is unique in this area of hardware and software.

![The Administrative console in Microsoft Response Point](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2602.png)

**Figure 26.2. The Administrative console in Microsoft Response Point**

An early model Syspine, from Quanta, connects to up to eight POTS lines, and is strictly an analog configuration. The OEM (Original Equipment Manufacturer) and their VAR partners supply the PBX server hardware with the management features, and phone handsets that connect to clients complete a working Response Point system. The server must run either XP or Vista, and any client that wants full telephony support also requires that operating system.

Microsoft has kept the requirements for Response Point to a minimum, and does not require that you run a domain server, Exchange, SharePoint, or the Office Communications Server to make this system work. The Response Point server can run the required networking services for clients, such as DHCP. There aren't many hooks (special connections) to Microsoft software in the first edition: no integration into Small Business Server, import of contact databases from Outlook, or use of Active Directory if your network is running a domain server. Response Point is a new product in its first version and will evolve over time.

# Voice over Internet Protocol

Voice over Internet Protocol, or VoIP, is the name given to a protocol for sending voice transmission over packet-switched networks. VoIP uses a data network, typically the Internet, to serve as the transmission medium for voice data transfer.

There is no requirement that both parties use VoIP during a connection, only that the IP-connected party has a direct connection to the data network. When telephone calls are placed from users who are connected to a PSTN to a VoIP phone, the sending party must use Direct Inward Dialing (DID) to connect to the VoIP network through a VoIP gateway using an assigned access number. Calls originating on the VoIP network are sent to the PSTN party through the DID number or numbers that were assigned to the PSTN party. In Europe, this system is called Direct Dial-In (DDI).

VoIP relies on a Digital Audio Conversion (DAC) to convert voice or sound into a digital audio file. As with other sound file formats like MP3, VoIP applies compression techniques to create a small file size, and that file is packetized by TCP and sent over IP networks. VoIP files can be very efficiently compressed, and so depending upon the quality level you select, a call lasting an hour might be no more than 20MB in size — no more than a podcast of that duration.

VoIP services are implemented in one of the following ways:

- As a software-only solution, as is the case with Skype, shown in [Figure 26.3](ch26.html#skype_apostrophy_s_main_window_comma_sho).![Skype's main window, shown here, supports IM chats and telephony, and is often used by 12 million users concurrently.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2603.png)**Figure 26.3. Skype's main window, shown here, supports IM chats and telephony, and is often used by 12 million users concurrently.**
- Connecting a phone to an Internet connection through an analog telephone adapter (ATA), as is the case with Vonage (`www.vonage.com`), AT&T CallVantage (`www.corp.att.com/voip`), and Verizon VoiceWing (`https://www22.verizon.com/ForYourHome/VOIP/VOIPHome.aspx`).
- Connecting through a cable modem, usually as part of a TV/phone/Internet package, as with Comcast (`www.comcast.com`).
- Using a VoIP PBX system connected to a TCP/IP network. A VoIP-connected PBX usually requires a high-speed Internet connection such as a T1 or Fiber-Optic Service (FIOS), a LAN, phones with IP connectors (or both items as separate parts), and the PBX server. Refer to the previous section for more details.

The primary motivation for using a VoIP system has historically been the greatly reduced charges imposed for long-distance connections. The primary drawback has been that VoIP consolidates your telephone and Internet into one line, and so if your Internet connection is broken, you lose both methods of communication. Early implementations of VoIP suffered from voice quality problems, but the current technology delivers voice quality that is as good as, and often better than, telephone lines. [Table 26.1](ch26.html#advantages_and_disadvantages_of_voip) summarizes some of the advantages and disadvantages of VoIP.

**Table 26.1. Advantages and Disadvantages of VoIP**

| Feature | Advantage | Disadvantage |
| --- | --- | --- |
| Area Code Independence | Your phone number can be in any area code, and it is transparent to an outside caller. |  |
| Computer Integration | When you connect a computer to an ATA, additional features such as voice mail and e-mail integration are possible. | Faxes can be hard to incorporate. |
| Cost | Long-distance service is inexpensive for a VoIP-to-VoIP call. | There are additional costs for DID calls. |
| Features | VoIP has an extensive feature set: call waiting, call forwarding, caller ID, and voice mail; three-way and conference calling are also usually included. | Calls to emergency services such as 911 aren't supported. Because VoIP isn't tied to a specific location, you can't be traced. |
| Interoperability |  | Calls through firewalls and NATs can be problematic. Doesn't work with old-style pulse phones. |
| Quality | Usually as good as, or better than, PSTN phone lines. | A poor or low-speed Internet connection results in poor telephone quality. Congestion can lead to jitters. |
| Mobility | An ATA can be used anywhere you can connect to the Internet and have electricity. | Mobile telephones aren't supported, and so you still need a cell phone. |
| Security | Through the use of protocols such as the Secure Real-Time Transport Protocol (SRTP), you can create a secure connection. |  |

Several of Cisco's switches, including the 2950, 2955, and 3550, allow their ports to be configured for VoIP traffic, a feature that they call voice Virtual Local Area Network, or voice VLAN. The traffic employs 802.1P priority tagged frames that support a class of service (CoS) (which is a form of Quality of Service) for voice and data traffic.

## Analog telephone adapters

An analog telephone adapter (ATA) connects an analog telephone to a digital telephone system such as a VoIP network, essentially turning a PSTN phone into an IP phone. These devices are typically quite small and come with an Ethernet RJ45 port and a telephone RJ11 port when used for a single phone. All ATAs require a power source.

### Note

A long list of currently available ATAs can be found on the `VoIP-Info.org` site at `www.voip-info.org/wiki-Analog+Telephone+Adapters`.

Larger ATAs support multiple phone connections and take an RJ14 (two-line), RJ25 (three-line), or RJ45 (four-line) jack for enterprise applications. They use a Foreign eXchange Station (FXS) port to connect the adapter to a LAN. ATAs that perform analog-to-digital conversions, or ADC, allow phones to connect directly to a VoIP server and are sometimes referred to as *VoIP gateways*. ATAs use protocols such as H.323, SIP, Media Gateway Control Protocol (MGCP), and Inter-Asterisk eXchange Protocol (IAX) and contain a codec or set of codecs to encode and decode voice communications. These protocols are described later in the chapter. ATAs are Plug-and-Play devices that don't require any configuration or computer software to connect to a VoIP server. When these devices are connected to a laptop or computer, they are managed by softphone programs.

ATAs usually come in one of two types: those that are simple connections between a phone and an IP network and devices that are keyed to a specific VoIP provider and service and that can't be used with any other system.

The Linksys SPA3102 is an example of an ATA device that can connect phones to an IP network. The SPA3102 allows a user to place a local call from a mobile or landline phone to the SPA-3102 where the caller's credentials are authenticated and the phone is connected to the Internet. If an SPA3102 is located on the receiving end of a call, then VoIP calls can be answered or routed to any PSTN phone or mobile phone.

This $70 device is shown in [Figure 26.4](ch26.html#the_linksys_spa3102_ata). It comes with one RJ11 connector (POTS) FXS port, one PSTN FXO port that connects to either a PBX or Telco device, and two 100Base-T RJ45 Ethernet connections that can be connected to a LAN and a broadband connection or an ISP's router. The software that comes with this ATA can configure the FXS and FXO lines independently. This ATA is installed by an end user and configured by their ISP remotely for their particular VoIP service. It supports IP Centrex systems.

![The Linksys SPA3102 ATA](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2604.png)

**Figure 26.4. The Linksys SPA3102 ATA**

## Internet Protocol phones

VoIP phones can be implemented as either hardware or software (as a softphone). They have features that allow them to connect to an IP network and communicate using protocols that efficiently send voice communication as data. Some VoIP providers use proprietary standards, or come with several standard protocols, such as the Session Initiation Protocol (SIP) or the Skinny Call Control Protocol (SCCP). As mentioned earlier, you can turn a regular phone into an IP phone by adding an analog telephone adapter that provides the missing functionality.

IP phones require the following features:

- Enabling hardware (for a physical phone)
- Software to either emulate (softphone) or manage an IP phone
- A protocol stack, such as SIP, SCCP, H.323, and Skype
- DNS client
- DHCP client (sometimes)
- Real-Time Transport Protocol (RTP) support
- Tunneling protocols such as the Simple Traversal of User Datagram Protocol through Network Address Translators (STUN) to traverse firewalls and gateways

[Figure 26.5](ch26.html#the_d-link_dph-140s_express_ethernet_bus) shows the D-Link DPH-140S Express Ethernet Business IP Phone. This phone comes with an Ethernet connection, speakerphone, transfer, voice mail, and an address book.

![The D-Link DPH-140S Express Ethernet Business IP Phone](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2605.png)

**Figure 26.5. The D-Link DPH-140S Express Ethernet Business IP Phone**

## VoIP protocols

As mentioned in the previous section, IP phones require a special set of protocols to create and manage connections. Usually these protocols are bundled together as a protocol stack so that the IP phone can be used on different networks and connect to different types of devices and management software. In the sections that follow, a number of the more widely used VoIP protocols are described, including:

- Session Initiation Protocol (SIP)
- Skinny Call Control Protocol (SCCP)
- Real-Time Transfer Protocol (RTP)
- Session Traversal Utilities for NAT (STUN)
- H.323
- Inter-Asterisk eXchange Protocol (IAX)
- Media Gateway Control Protocol (MGCP)

The Session Initiation Protocol, or SIP, is commonly used for voice and video communication over the Internet. It is also used for streaming multimedia, and shows up in instant messaging (IM) and even in video games. SIP supports two-party point-to-point or unicast sessions, as well as multistream, multiparty, and multicast sessions. The Transport layer protocol is usually as follows: TCP for point to point; UDP for VoIP, games, and applications; or Stream Control Transmission Protocol (SCTP) for streaming applications. SIP manages port assignments, addressing, and other connection functions for the data stream. Conceptually, SIP is a Session layer protocol in the ISO/OSI model, but would be an Application layer protocol in the TCP/IP model where Layers 5 to 7 are consolidated.

### Skinny Call Control Protocol

The Skinny Call Control Protocol, or SCCP, is the Session layer protocol used by Cisco to connect "skinny" clients through Cisco switches to one another. Skinny Calls include the following: Cisco's line of wired and wireless IP phones (the 7900 series); the Cisco IP Communicator softphone; and the Cisco Unity voicemail server. Cisco's line of IP phones uses various protocols for communication.

All of these devices can be managed by the Cisco Unified Communications Manager (CUCM) call processing software, also called the Cisco CallManager (CCM). (Cisco Systems is very big on acronyms that start with *C*.) CallManager is essentially a messaging server that provides transaction management for a variety of media protocols such as SIP, ISDN, H.323 video, and the Media Gateway Control Protocol (MGCP).

### Real-Time Transport Protocol and Real-Time Transfer Control

The Real-Time Transport Protocol (RTP) is a standard packet format for multimedia content sent over IP networks as either TCP or UDP data. It can be used for either unicast or multicast data. RTCP is used to manage the RTP data, as well as to provide QoS monitoring.

RTP doesn't specify which ports are to be used, but it does require that RTP be assigned an even port, and that the Real-Time Transfer Control (RTCP) protocol be assigned the next highest available odd port. The pair of ports for RTP and RTCP are assigned in the Dynamic Port range of 16384 to 32767. RTP data can be real time and interactive; RTP packets require a Session protocol like SIP or H.323 for VoIP.

### Session Traversal Utilities for NAT

It can be difficult for telephony applications to successfully negotiate with network firewalls and gateways where network address translation, or NAT, operates. NATs manage application access to specific ports, and clients' access to different applications for both inbound and outbound traffic. NAT implementations can be somewhat different on different devices, and they tend to break different IP applications by denying that application access to Internet resources or allowing communications from outside the router to reach the application server. RTP, which was described in the previous section, is particularly vulnerable to NAT traversal problems due to its dynamic port assignments.

The Simple Traversal of User Datagram Protocol through Network Address Translators (STUN) protocol provides a solution to this problem. STUN is used as a service (server) on the public side of a WAN connection (such as the Internet) to obtain the appropriate public IP address and port number required for UDP to transit the device. It works by sending a series of STUN messages through the STUN listening port number 3478 to a STUN client on a LAN. The client obtains the appropriate port information and returns it to the STUN server.

The problem with some STUN clients is that they aren't able to use the transport information (IP address and port) from their location on the network. Also, not all NATs support STUN, although many do. STUN doesn't work with symmetric or bidirectional NATs that are used in enterprise-class networks. An alternative protocol called Traversal Using Relay NAT (TURN) is under development for that class of device.

Another NAT traversal mechanism under development is called Interactive Connectivity Establishment (ICE). It is specifically meant to connect VoIP clients using SIP to clients within a network.

### The H.323 Protocol

The H.323 protocol of the ITU-T (International Telephone Union Telecommunication Sector) is a suite of audio-visual session transport, signaling, control, and bandwidth management standards for both point-to-point sessions as well as conferencing. H.323 is mostly used by voice and videoconferencing applications, particular real-time applications deployed over the Internet. H.323 is also used on the public telephone network, 3G mobile networks, over ISDN, and in many other places. Microsoft's NetMeeting videoconferencing software was based on the H.323 protocol.

An H.323 application relies on defined network components for its session. The most important of these elements are terminals, multiple control units (MCUs), gateways, border elements, and gatekeepers which perform name resolution. A path is defined between these different elements, which are called endpoints in H.323 applications. The minimum path definition is between two terminals.

### Inter-Asterisk eXchange Protocol

The Inter-Asterisk eXchange Protocol (IAX) is used by the open source Asterisk PBX system described earlier in this chapter. In its second version, IAX2 became a published protocol allowing many vendors to interoperate with VoIP products that are based on Asterisk. IAX2 can provide trunking where many clients share the same set of channels, and channel multiplexing over a single link.

IAX2 transports VoIP data over UDP, and is usually assigned to port 4569 on routers. The data stream is controlled by a set of commands and parameters that can provide the necessary control for multiplexing the VoIP signals and controlling the flow of traffic. IAX2 is both firewall- and NAT-friendly because signaling and data both use the same transit method. This compares with some of the other protocols described in this section, including SIP, H.323, and MGCP. Those methods rely on RTP communication for session control, which is an out-of-band method. By out-of-band it is meant that the RTP communication is using a different channel.

### Media Gateway Control Protocol

The Media Gateway Control Protocol (MGCP) describes an architecture that can be used to control gateway devices on an IP or on the public telephone networks. The protocol describes a set of signal and control commands that are used to control VoIP traffic, and is often used by both H.323 and SIP traffic. MGCP is the internal protocol used by a Media Gateway Controller (MGC) and the Media Gateway (MG). The Media Gateway Controller is the device that performs call handling making the connection between the IP signaling device. MGCP uses a Call Agent and a Media Gateway to convert VoIP signals traversing different circuits.

MGCP became popular in VoIP applications because it does not perform encoding, nor does it transport VoIP traffic. These features are deferred to the other protocols mentioned in the previous paragraph. MGCP provides the switching mechanism and the signal and path management functions used by various media gateways.

# Computer Telephony Integration

Computer telephony integration (CTI) is the use of computers to manage the set of services used in call centers. A CTI system can route calls to the correct person, pop up a window with the calling person's phone number, name, and history, and perform any additional actions that are required. CTI requires specialized software, often leveraging the telephony APIs that are in networked operating systems, as well as the necessary hardware to connect the computer to the different telephone assets. CTI can be deployed on a single computer, making it appear as if that one system is a call center, or it can be client/server software that runs an actual call center.

CTI has a very broad set of capabilities that are highly dependent on the software, hardware, and, of course, the developer. A few of the more commonly encountered features are:

- Authentication
- Call queue management
- Call routing or automated call distribution
- Caller ID, also called Automatic Number Identification (ANI)
- Customer assistance
- Robocalls (call campaigns) integrated with predictive dialing
- Telemarketing
- Video conferencing
- Voice recognition and interactive voice response (IVR)

These services are supported by Microsoft's Window Telephony Application Programming Interface (TAPI) and related programming interfaces such as AT&T/Lucent/Novell's Telephone Service Application Programming Interface (TSAPI) to link those applications to hardware more easily.

Telcordia (formerly Bell Communications Research) developed the Advanced Intelligent Network (AIN or IN) telephone architecture to make CTI extensible without having to rely on built-in capabilities in switches and routers. The International Telecommunications Union (ITU) used the model of AIN to develop a version that they call Capability Set 1 (CS-1). AIN works at the switch or Service Switching Point (SSP) and forwards phone calls to the logic located at the Service Control Point (SCP). The logic analyzes the numbers entered in dialing and matches them to the service that the caller requires. In some cases the logic might return information to the caller; in other cases the call is passed off to another device or Intelligent Peripheral (IP) that is attached to another SSP where the calls are processed further. These terms are defined as part of the AIN model.

One service provided by AIN is called Local Number Portability. When you switch carriers, but retain your phone number, a call is routed at a switch to your new phone service for handling.

The Computer Supported Telephony Applications (CSTA) is an integration standard of the European Computer Manufacturer's Association (ECMA) that has been ratified as a standard by the ITU.

# Video Telephony

Video telephony enables two users to talk with one another while looking at a synchronized video stream. A video telephone, or videophone if you will, was demonstrated by AT&T in their pavilion at the 1964 New York World's Fair and at Expo 67 in Montreal. Dubbed the Picturephone, it was introduced by AT&T in 1971 for the consumer market; it sold very poorly and was discontinued in 1974. It wasn't clear at the time if the price was too high or if people didn't want to be seen while talking on a phone. A more recent introduction of H.324 video using LG-Nortel videophones in Mexico in 2006 doesn't seem to be gaining traction.

One of the more popular video conferencing solutions is Skype, a VoIP application that can also support instant messaging, video transmission, and file transfer. VoIP was written by the same team of developers who did the Kazaa peer-to-peer network, and Skype became equally as popular. Skype became very popular because it offered many services such as international calling for free from computer to computer. Additional services can be purchased that allow phones to call over Skype. Skype was purchased by eBay, but is currently being spun off as a separate company. Shown in [Figure 26.6](ch26.html#a_videoconference_inside_a_skype_window) is a video conference in Skype.

![A videoconference inside a Skype window; the small picture shows the sender.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2606.png)

**Figure 26.6. A videoconference inside a Skype window; the small picture shows the sender.**

## Mobile VoIP

Mobile VoIP is an area of active development that enabled video telephony on a wireless network. The particular technology used is a function of the network, and its speed.

One approach is to use a SIP phone client to communicate with the network using RTP packets for the voice channel. This is the most widespread method used. Another approach is to create gateway software to send data to a SIP server where SIP and RTP can be converted into wireless network protocols.

Some GSM (Global System for Mobile Communications) phones use a technology called Unlicensed Mobile Access (UMA) Generic Access Network (GAN) for VoIP transport on the GSM backbone. UMA is a brand name, and 3GPP GAN is the technology. GAN networks transmit SIP over IP networks.

High-speed EVDO rev. A (Evolution-Data Optimized), HSDA (High-Speed Downlink Packet Access), Wi-Fi, and WiMAX (Worldwide Interoperability for Microwave Access) are fast enough that they are capable of transmitting video messages. As a general rule, Wi-Fi networks are cheaper to use than EVDO or HSDPA, but the latter two networks offer broader coverage and better audio.

Video telephony is becoming widely available on cell phones that operate on 3G (Universal Mobile Telecommunications System, or UMTS) GSM networks. According to Wireless Intelligence, in Q2, there were over 130 million cell phones capable of video telephony sold. GSM is available worldwide in 59 countries. No data is available that measures the usage of this feature, but its availability seems to be growing rapidly and the video capture feature is being widely used, something any YouTube devotee can attest to.

Video telecommunications is a boon to people who are deaf or have speech difficulties. In the United States, the Federal Communications Commission (FCC) regulates a program with cell phone providers called the Video Relay Service that sets up videophone sessions for sign language interpretation to communicate.

## Webcams

Business applications for videoconferencing and telephony seem to have broader acceptance and could become much more important as business travel becomes more expensive. A number of manufacturers sell systems for videoconferencing or integrate it into telecommunication suites. Cisco's Unified Communications Manager is one example, but there are many others. The speakerphone vendor Polycom supports the addition of video to their system.

There have also been a number of laptops introduced that have cameras built into them; examples include models of the Apple Macintosh, Sony Vaio, Dell XPS, and the Asus Eee notebook. The cameras are usually placed at the top of the laptop screen and support video services for VoIP. They are essentially Webcams. You find video conferencing support in programs as varied as AOL Instant Messenger (AIM), Skype, Windows Live Messenger, Yahoo Messenger, iChat, Camfrog, and others; the capability is widespread.

Webcams also are widely used as security devices for surveillance. Some of these cameras plug into computers through phone line connections, and others can be connected to Ethernet networks. A class of these Webcams are appliances; they have Web servers built into them whose output can be viewed in a browser. Axis, Panasonic, and others sell these cameras, sometimes under the name *network camera*.

Webcams have sprouted up everywhere, and many have been made publicly available. There are Webcams that survey the scene at Old Faithful Geyser in Yellowstone National Park (see [Figure 26.7](ch26.html#the_national_park_service_apostrophy_s_s)), in Times Square in New York City, and worldwide.

![The National Park Service's streaming Webcam at Old Faithful in Yellowstone National Park.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2607.png)

**Figure 26.7. The National Park Service's streaming Webcam at Old Faithful in Yellowstone National Park.**

Some of these Webcams are set up to send static pictures, usually once every minute or so; however, the newer models stream real-time video. [Figure 26.7](ch26.html#the_national_park_service_apostrophy_s_s) shows a newer streaming Webcam, although the older still-image Webcam is still available on the National Park Service site.

Several sites on the Internet catalog and link to these cameras; the best known of them is `Earthcam.com`. It's a great diversion when you get the urge to travel but don't have the budget, or when you want to check out the conditions in a place you are going to.

# Summary

In this chapter, the subjects of computer telephony and VoIP applications were introduced. Telephony is the use of telephones with computers either on phone or Ethernet networks, or both.

Operating systems enable telephony with native APIs that application vendors can build on. Computers can connect and manage phones and form the basis for PBX systems. Telephony applications built using application frameworks form the basis for CTI. Very sophisticated telephone systems are built with CTI technology.

Applications that combine voice and video were also described. These include videophones, Webcams, and video conferencing software.

The next part begins a set of chapters on network security. It covers some of the security protocols, such as HTTPS and SSL. You learn how they work, where they are used, and what networked services they protect.
