# Chapter 12. Local Area Networking

**IN THIS CHAPTER**

- Introduction to LANs
- How broadcast technology solves some network issues
- How Ethernet works
- Token Ring and FDDI networks
- How industry creates network automation systems
- Automate a home using RF over power lines and X10 networks

This chapter surveys the major classes of networks that are used to create Local Area Networks (LANs), with the exception of wireless LANs. It describes the different technologies and how they are implemented. The network types described are Ethernet, Token Ring, Fiber Distributed Data Interface (FDDI), X10, and different industrial automation bus standards. The many IEEE 802.x standards that have codified these different network types are also listed.

Ethernet is an example of a frame-based broadcast network. Frames are constructed that include standard fields for source and destination addresses, synchronization, error checking, and more. The construction of an Ethernet frame is fully described. Ethernet frames sometimes arrive at the same time, resulting in a collision. Ethernet uses Carrier Sense Multiple Access with Collision Detection (CSMA/CD) to detect and correct data loss that results from collision.

Token Ring networks use a different method for network access. On these networks, endpoints get the chance to broadcast on the network when they receive a special token frame. Token Ring networks are now largely an IBM technology. FDDI networks are token rings that use optical fiber to create high-speed systems. They have been widely deployed in the past, particularly in the telecommunications industry.

The X10 RF over power-line networks allows you to automate a home. The signaling technology is explained, and related automation networking standards are briefly introduced.

Industrial automation networks are described. Those networks aggregate the data from sensors, actuators, switches, valves, and other devices and make that data available to a control station with a Human Machine Interface system. Process control systems that include the Modbus device bus, Programmable Logic Controllers, OLE for Process Control (OPC) data interchange, and Supervisory Control and Data Acquisition (SCADA) systems are detailed.

# Introduction

Local Area Networks, or LANs, are networks that are limited in scope, private, and have a limited number of administered entities such as domains and subnets. The characteristics of a LAN are best summarized by these factors:

- Topology
- Transmission media
- Technology standards
- Size
- Management characteristics

In [Chapter 3](ch03.html), different topologies are described, [Chapter 8](ch08.html) discusses media, and [Chapter 30](ch30.html) describes management technologies. In this chapter, you learn about technology standards and network sizes, in terms of node counts, connections, and run lengths. A few of the most important LAN network standards are discussed in this chapter, including:

- Ethernet, the dominant network broadcast standard
- Token Ring, a method for synchronized network access
- Fiber Distributed Data Interface (FDDI), a high-speed Token Ring network protocol
- X10 power-line radio frequency (RF) networks, and other home automation network types
- Industrial automation bus and data exchange standards

These five LAN network types serve to frame the subject of what a LAN is, how you design a LAN, and how data on a LAN is processed. Wireless technology is also popular in constructing LANs and is becoming increasingly popular as time goes by. To completely explore the subject of modern-day LANs, you would have to include the different Wi-Fi network standards in use today. However, to keep this chapter to a reasonable length, Wi-Fi networks are covered in [Chapter 14](ch14.html), where the topic is expanded and more fully explored.

In order for different types of Ethernet components to interoperate, they must be based on tested industry standards. Most of the Ethernet standards are the result of efforts of committees of the IEEE (Institute of Electrical and Electronics Engineers, pronounced "eye triple E"). In the next section, you will learn about the different versions of IEEE standards that have been and are now in use. A fundamental feature of a network is the area over which communication can be transmitted without requiring modification, called the broadcast domain. Broadcast domains and their relationship to Ethernet networks are explored in the section that follows the IEEE standards.

## The IEEE 802 LAN standards

As LAN standards have been developed, the IEEE has created a set of standards that mirror the real-world networks in use. These Ethernet standards can arise out of the work of a single vendor, such as the Token Ring technologies from IBM, a small group of vendors, such as the DIX (DEC, Intel, and Xerox) group that created Ethernet, or the result of an industry working group of some type.

Whenever possible, IEEE committees generalize the specification of the standard so that as many other vendors' products can interoperate as possible. So while the IBM Token Ring technology might require a specific medium, the IEEE standard would generalize this requirement. These different standards go through a proposed stage where different aspects of the standards exist fully specified as Request for Comment documents, or RFCs. Many RFCs live very long lives, eventually being modified or replaced by other RFCs. IEEE eventually formalizes some of these standards, and when it does, it publishes the standards as a set of reference manuals based on the standard's components.

This has resulted in a set of 15 (and growing) standards that have been created or are in development from work that now spans nearly 30 years. These standards are summarized in [Table 12.1](ch12.html#ieee_802_lan_standards). Each standard may have multiple substandards, and some of these substandards get reduced to practice and are commercially viable, while many other substandards are not. If you have followed the development of Wi-Fi standards over the past decade, you will remember that the 802.11 standard has produced the 802.11a, 802.11b, 802.11g, and 802.11n substandards.

## Broadcast channels

LANs all face the central problem of how to broadcast over a shared network. The solution to this problem is the fundamental decision that separates one type of LAN from another. Because point-to-point network connections involve an exponential number of circuits, this approach to building networks isn't practical. You could use switches to build circuits, the way you do when you create a virtual link (point to point) over a WAN. However, populating a network with a large number of switches on a single network isn't practical either.

In [Chapter 5](ch05.html), you learned about the concept of a channel. A channel is a defined state of a network that allows information to pass through it, as implemented in the Medium Access Control portion of the Data Link layer. Channels can be single or multiple; they can also be dedicated, multiple access, or random access. In networks that use virtual channels such as telephony, techniques such as Frequency Division Multiplexing (FDM) slice up the bandwidth into portions that are assigned to each user. Traditionally, for voice, those slices are called DS0, and if you recall from previous discussions they are allocated in chunks of 64 Kbits/s.

**Table 12.1. IEEE 802 LAN Standards**

| Standard | Application | Substandards |
| --- | --- | --- |
| Merged and abandoned standards are not listed. |  |  |
| WiMAX stands for Wireless Interoperability for Microwave Access; it is called Wireless Broadband, or WiBro, in South Korea. |  |  |
| 802.1 | LAN/MAN Bridging and Management | 802.1b, LAN/MAN Management; 802.1D, MAC Bridges; 802.1e, System Load Protocol; 802.1f, Definitions and Procedures for IEEE 802 Management Information; 802.1G, Remote MAC Bridging; 802.1H, Ethernet MAC Bridging; 802.1Q, VLANs; 802.1x, Port-based Network Access Control; 802.1AB, Station and Media Access Control Connectivity Discovery (LLD); 802.1ad, Provider Bridging; 802.1AE, MAC Security; 802.1af, MAC Key Security; 802.1ag, Connectivity Fault Management; 802.1ah, Provider Backbone Bridge (PBB); 802.1aj, Two Port Mac Relay (TPMR); 802.1ak, Multiple Registration Protocol (MRP); 802.1ap, MIBs; 802.1aq, Shortest Path Bridging (SPB); 802.1AR, Secure Device Identity (DevID); 802.1AS, Time and Synchronization for Time Sensitive Applications in Bridged LANs; 802.1Qat, Stream Reservation Protocol; 802.1Qau, Congestion Management; 802.1Qav, Forwarding and Queuing Enhancements for Time Sensitive Streams; 802.1Qaw, Management of Data Driven and Data Dependent Connectivity Faults; 802.1Qay, Provider Backbone Bridge Traffic Engineering (PBB-TE); 802.1Qaz, Enhanced Transmission Selection; 802.1BA, Audio Video Bridging (AVB) Systems. |
| 802.2 | Logical Link Control | No sub-standards. LLC manages data link communication and link addressing. It defines Services Access Points (SAPs), and provides sequencing. |
| 802.3 | CSMA/CD | Ethernet standards. [Table 12.2](ch12.html#ethernet_standards) lists the 802.3 sub-standards. |
| 802.4 | Token Bus | 802.4a, LAN: Fiber Optic Token Bus |
| 802.5 | Token Ring | 802.5a, LAN: Station Management Supplement to 802.5; 802.5n, Unshielded Twisted Pair at 4/16 Mbps; 802.5q, LAN: [Part 5](pt05.html): Media Access Control Revision; 802.5, LAN: Dedicated Token Ring Station Attachment. |
| 802.6 | Distributed Queue Dual Bus (DQDB) | 802.6bm, Premises Extension of DS3-Based 802.6 MAN; 802.6e, Eraser Node for DQDB MAN; 802.6g, Layer Management for 802.6 MAN; 802.6i, Remote LAN Bridging Using 802.6 MAN; 802.6l, Point-to-Point Interface for Subnetwork of MAN; 802.6m, Subnetwork of MAN. |
| 802.7 | Broadband LAN |  |
| 802.8 | Fiber Optic LAN/MAN |  |
| 802.9 | Integrated Services | 802.9a, Supplement to Integrated Services LAN: 802.9 Isochronous with CSMA/CD MAC; 802.9b, Support for Functional Specifications for AU to AU Interworking 802.9; 802.9c, Supplement to 802.9: Management. Object Conforming Statement; 802.9d, Supplemental to 802.9: Protocol Implementation Conforming Statement; 802.9e, Asynchronous Transfer Mode (ATM) Cell Bearer Mode; 802.9f, Remote Terminal Line Power for Integrated Services for Terminal Equipment (ISTE). |
| 802.10 | LAN/MAN Security | 802.10, Standard for Interoperable LAN Security (SILS); 802.10a, Interoperable LAN Security (SILS) - The Model; 802.10c, SILS - Key Management; 802.10d, SILS - Security Management; 802.10g, Standard for Security Labeling Within Secure Data Exchange; 802.10h, Support to Interoperable LM Security: PICS Proforma/Secondary Data. |
| 802.11 | Wireless LAN | 802.11a, 5 GHz, 54 Mbits/s; 802.11b, 2.4 GHz, 11 Mbits/s; 802.11c, Bridge operations procedures; 802.11d, International roaming extensions; 802.11e, QoS Enhancements; 802.11g, 2.4 GHz, 54 Mbits/s; 802.11h, Spectrum Managed 802.11a (Europe); 802.11i, Enhanced Security; 802.11j, Extensions for Japan; 802.11k, Radio resource management enhancements; 802.11m - Maintenance of the standard; 802.11n - Higher throughput improvements using MIMO (multiple input, multiple output) antennas, 5 GHz or 2.4 GHz, 600 Mbits/s (over 4 × 40 MHz channels); 802.11p, WAVE - Wireless Access for the Vehicular Environment (such as ambulances and passenger cars); 802.11r, Fast roaming (in progress); 802.11s, Mesh Networking, Extended Service Set (ESS) (in progress); 802.11T, Wireless Performance Prediction (WPP) - test methods and metrics; 802.11u, Interworking with non-802 networks (for example, cellular) (projected); 802.11v, Wireless network management (projected); 802.11w, Protected Management Frames (projected); 802.11y, 3650-3700 MHz Operation in the U.S.; 802.11z, Extensions to Direct Link Setup (DLS) (in progress); 802.11aa, Robust streaming of Audio Video Transport Streams (in progress). |
| 802.12 | High-Speed LAN | 802.12a, Operation at Greater than 100 Mbits/s; 802.12b, 2-TP PMD Medium Dependent Interface and Link Specifications; 802.12c, 100 Mbits/s Operation: Full Duplex Operation; 802.12d, 100 Mbits/s Operation: Redundant Links. |
| 802.13 | The LAN to Nowhere | This standard was never defined for the same reason that there are no thirteenth floors in buildings: Triskaidekaphobia. |
| 802.14 | Cable TV-Based Broadband Communication Networks |  |
| 802.15 | Wireless Personal Area Networks (WPANs) | 802.15.1, Bluetooth; 802.15.2, Coexistence for WPAN and Wireless LANs; 802.15.3, High-Rate WPANs. |
| 802.16 | Broadband Wireless Access (WiMAX, or WirelessMAN) | First mile, last mile connections. 802.16e, Mobile; 802.16f, MIB definition; 802.16g, Management Plane Procedures and Services; 802.16h, Improved Coexistence for License Exempt Operation (in progress); 802.16i, Mobile MIB (in progress); 802.16j, Multihop Relay Specification (in progress); 802.16k, Bridging; 802.16m, Advanced Air Interface (proposed). |
| 802.17 | Resilient Packet Ring (RPR) | Used in high-speed SONET networks; 802.17b, Spatially aware sublayer (SAS). |
| 802.18 | Radio Regulatory |  |
| 802.19 | Coexistence |  |
| 802.20 | Mobile Broadband Wireless Access | Standard for Local and Metropolitan Area Networks, Standard Air Interface for Mobile Broadband Wireless Access Systems Supporting Vehicular Mobility, Physical and Media Access Control Layer Specification. |
| 802.21 | Media Independent Handoff (MIH) | Enables information exchange between cellular, GSM, GPRS, Wi-Fi, Bluetooth, 802.11, and 802.16 networks through a set of handover mechanisms. MIH is similar to Unlicensed Mobile Access (UMA), a roaming and handover protocol that works between GSM, UMTS, Bluetooth, and 802.11 networks. |
| 802.22 | Wireless Regional Area Networks (WRAN) | WRAN transmits over white spaces in the TV frequency range. This is a new group with a proposed technology. |

FDM is fine for network traffic that is predictable, where there are only a few users at any one time, and the data is cached or buffered en route to accommodate traffic fluctuations. Once the number of users grows, the traffic load becomes unpredictable, the size of the data being transmitted varies, and traffic becomes bursty; the FDM model is no longer efficient. Time Division Multiplexing (TDM) sets network allocation using time slicing, and for all of the same reasons it fares no better than FDM. These are the reasons that all modern LAN technologies adopt a broadcast model. Information is sent onto the LAN where it competes with other pieces of information until it gets to the destination specified.

Broadcast communication uses the concept of a "channel" to describe a path or multipath that exists over a physical medium. A multipath is a routing technique that can use multiple alternative pathways through an existing network. A channel can be assigned in any of the following ways:

- **Unichannel single sequential access**. There is one channel and it is shared among many stations, one at a time (time slotted), based on a predetermined order. This scheme ensures that data doesn't contend with other traffic on the network, but is inefficient as there is no prioritization of the data being sent.Unichannel technologies aren't efficient for full-duplex operations, but are fine for half-duplex operations. However, there is no additional channel for sending a message between endpoints, which introduces some inefficiency into the system.
- **Unichannel tokenized access**. The token scheme uses a metaphor of passing the baton from one station to the next. The station with the token gets network access and then uses an algorithm to determine whether to use the access rights or pass it along. Tokenized networks do not suffer contention, and they allow for very large data transfers; however, they run at slower speeds than other broadcast methods.
- **Unichannel multiple access with collisions**. All stations broadcast data onto the network; there are no time slots or master clocks. When two pieces of data arrive at the same time at the same end station and a collision occurs, collision correction mechanisms force retransmission of the data.
- **Carrier sensing**. Stations broadcast onto the network when they determine that the network is quiet. This reduces, but does not eliminate, collisions and is more efficient than a situation where no carrier sense detection technology is used.
- **Multichannel broadcast**. A multichannel broadcast offers the most throughput and is more efficient for full-duplex operations. On a multichannel network, one channel can be sending data while the other is either controlling the process or messaging, which adds extra efficiency. Multichannel networks require additional buffering and caching, and extra coordination. They also allow for dedicated channels.

# Ethernet

Ethernet is the dominant wired network technology in use on LANs today. The standard defines frames broadcast over Physical Layer media and Data Link Layer signaling methods based on Carrier Sense Multiple Access with Collision Detection (CSMA/CD). Ethernet is defined by the IEEE 802.3 standard. Nodes on an Ethernet network are identified by the globally unique 48-bit MAC address. There are two classes of network nodes on an Ethernet network:

- **Data Terminal Equipment (DTE)**. This category includes any component that represents the target or source of an Ethernet frame. Computers, servers, printers, and other devices of this kind are sometimes called *end stations*.
- **Data Communications Equipment (DCE)**. Any network device that receives and forwards Ethernet frames is a DCE. This includes switches, routers, bridges, repeaters, and any network interfaces such as NICs or modems.

### Note

A packet transmitted over a wire is called a frame.

Ethernet was developed at Xerox PARC in the 1970s where the CSMA/CD protocol was created by Robert Metcalfe, David Boggs, Chuck Thacker, and Butler Lampson. (Metcalfe went on to found 3COM.) The name Ethernet arises from the idea that the network was similar to the *ether*, derived from the Greek personification of the pure air or sky. In the development of science, various ethers are promoted as a transport medium for electromagnetism, light, gravity, as well as where matter disappeared to in early chemistry, and a host of other unexplained phenomena.

### Note

In [Chapter 8](ch08.html), the various wiring standards used by Ethernet are described.

The Ethernet prototype ran at 3 Mbits/s and was designed to provide high network throughput even when the network was heavily loaded. In 1980, Digital Equipment Corporation, Intel, and Xerox created the first released version, Ethernet 1.0 (dubbed the DIX standard), which ran at 10 Mbits/s. The 802.3 standard is based on Ethernet 1.0.

An early version of Ethernet, called StarLAN, ran over unshielded twisted pair (UTP) and served as the basis for the early LANs, eventually categorized as 1BASE5 Ethernet. In the early 1980s, StarLAN was unique because you could use a standard RJ-45 telephone connector to use the wiring in a building as the network medium. Today this method is commonplace. The 10BASE-T adopted StarLAN's modulation scheme, its link detection, and its wiring assignments.

### Note

10BASE-T is covered in [Chapter 8](ch08.html).

The name 10Base-T indicates both the speed of 10 Mbits/s and the transmission medium, which is twisted pair. For 100Base-T4, the speed would be 100 Mbits/s and the medium would be four twisted-pair cables. The 1000Base-LX refers to Ethernet using a long wavelength traveling over fiber optic cable. Ethernet uses the term *Base*, which is short for Baseband, a signal-filtering mechanism that is described in [Chapter 5](ch05.html). Today Ethernet travels over broadband connections, with multiple data paths defined by frequency or amplitude without regard for the signaling rate, but it is rare to see the term 100Broad used even when high-speed connections are used, even though it is appropriate. The two other signaling methods of wideband and narrowband do not apply to Ethernet.

In [Table 12.2](ch12.html#ethernet_standards) the various forms of 802.3 Ethernet standards are listed. The 802.3 standard codifies the important types of wired Ethernet that are so important for modern local area networks. The numbers in parentheses indicate the theoretical throughput that each standard has.

**Table 12.2. 802.3 Ethernet Standards**

| Substandard | Date | Purpose |
| --- | --- | --- |
| **Experimental Ethernet** | 1972 | 2.94 Mbits/s (367 KB/s) over coaxial cable (coax) cable bus |
| **Ethernet II (DIX v2.0)** | 1982 | 10 Mbits/s (1.25 MB/s) over thin coax (Thinnet); frames have a Type field. This frame format is used on all forms of Ethernet by protocols in the Internet protocol suite. |
| **IEEE 802.3** | 1983 | 10BASE5 10 Mbits/s (1.25 MB/s) over thick coax (Thicknet); the same as DIX except that the Type field is replaced by Length, and an 802.2 LLC header follows the 802.3 header. |
| **802.3a** | 1985 | 10BASE2 10 Mbits/s (1.25 MB/s) over thin coax (Thinnet or cheapernet) |
| **802.3b** | 1985 | 10BROAD36 |
| **802.3c** | 1985 | 10 Mbits/s (1.25 MB/s) repeater specs |
| **802.3d** | 1987 | FOIRL (Fiber-Optic Inter-Repeater Link) |
| **802.3e** | 1987 | 1BASE5 or StarLAN |
| **802.3i** | 1990 | 10BASE-T 10 Mbits/s (1.25 MB/s) over twisted pair |
| **802.3j** | 1993 | 10BASE-F 10 Mbits/s (1.25 MB/s) over fiber optic |
| **802.3u** | 1995 | 100BASE-TX, 100BASE-T4, 100BASE-FX Fast Ethernet at 100 Mbits/s (12.5 MB/s) with autonegotiation |
| **802.3x** | 1997 | Full Duplex and flow control; also incorporates DIX framing, and removes the DIX/802.3 split |
| **802.3y** | 1998 | 100BASE-T2 100 Mbits/s (12.5 MB/s) over low-quality twisted pair |
| **802.3z** | 1998 | 1000BASE-X Gbit/s Ethernet over fiber optic at 1 Gbit/s (125 MB/s) |
| **802.3ab** | 1999 | 1000BASE-T Gbit/s Ethernet over twisted pair at 1 Gbit/s (125 MB/s) |
| **802.3ac** | 1998 | Maximum frame size extended to 1522 bytes (to allow "Q-tag"); the Q-tag includes 802.1Q VLAN information and 802.1p priority information. |
| **802.3ad** | 2000 | Link aggregation for parallel links |
| **802.3ae** | 2003 | 10 Gbits/s (1250 MB/s) Ethernet over fiber; 10GBASE-SR, 10GBASE-LR, 10GBASE-ER, 10GBASE-SW, 10GBASE-LW, 10GBASE-EW. |
| **802.3af** | 2003 | Power over Ethernet |
| **802.3ah** | 2004 | Ethernet in the First Mile |
| **802.3ak** | 2004 | 10GBASE-CX4 10 Gbit/s (1250 Mbits/s) Ethernet over twin-axial cable |
| **802.3an** | 2006 | 10GBASE-T 10 Gbit/s (1250 MB/s) Ethernet over unshielded twisted pair (UTP) |
| **802.3ap** | 2007 | Backplane Ethernet (1 and 10 Gbits/s [125 and 1250 MB/s] over printed circuit boards) |
| **802.3aq** | 2006 | 10GBASE-LRM 10 Gbits/s (1250 MB/s) Ethernet over multimode fiber |
| **802.3as** | 2006 | Frame expansion |
| **802.3at** | 2008 | Power over Ethernet enhancements |
| **802.3av** | 2009 | 10 Gbits/s EPON (Ethernet Passive Optical Network) |
| **802.3az** | 2007 | Energy-Efficient Ethernet |
| **802.3ba** | 2009 | Higher-Speed Study Group. 40 Gbits/s over 1m backplane, 10m Cu cable assembly (4x25 Gbit or 10x10 Gbit lanes) and 100m of MMF and 100 Gbits/s up to 10m or Cu cable assembly, 100m of MMF or 40km of SMF, respectively. |

Ethernet encodes its information in a timed sequence of signals that are distorted as they travel over the network. Sometimes the receiving system must filter the incoming data, compensate for drift (baseline wander), or synchronize the data to the correct clock rate in order to extract the data from the incoming signal. Different encoding schemes are used to fix these problems. Early Ethernet used Manchester encoding (described later in this chapter), while GigE moved to a system using forward error correcting codes. Only bit errors are detected by Ethernet; other errors are passed up the protocol stack for further error checking.

## Ethernet frames

Frames are chunks of data that are packaged for transmission over a network. They are created in software at the Data Link layer where the data may have to be fragmented or padded to reach the appropriate size for that frame's format. The data portion, sometimes called the *payload*, is wrapped or encapsulated with a number of starting and ending bits that represent additional information on what the data is, where it comes from and goes to, error checking or diagnostic features, and more. Ethernet frames are the prototypical example of the use of frames on a network. You don't need to be on a packet-switched network like TCP/IP and the Internet to use frames, although that is probably the best-known example.

Frames are helpful because they provide a context in which a receiving system can understand the data that is being sent and interpret it. From the standpoint of any system listening to the network, signals are being received nearly all the time, depending upon current network utilization. A starting sequence, once recognized, provides the timing and synchronization required to know when the first bit starts and how long the frame is. The following features are characteristic of nearly all frame structures that you will encounter:

- Frames have a purpose: some transmit data, others give commands, and others provide information or messages.
- Frames have starting and ending sequences or fields called delimiters.
- Frames generally contain a character count field that indicates the size of the frame and is part of the error-checking mechanism. Some frames are defined to be of uniform length and don't require a character count field, as it is built into the standard.
- Data fields may be variable or fixed length, and may or may not be required, depending upon the frame's purpose. It may be necessary to pad the data field (usually with zeros) to achieve a certain field length, also referred to as *bit stuffing*.
- An error-checking sequence is included that is used to determine the validity of the data sent.

Error checking is a critical function in frame transmission, as there is no other way to be completely certain that a frame arrived correctly at its destination. On a frame network, different frames are meant to be separated by a quiet period between frames, but that is not a reliable frame delimiter. If two frames arrive at a destination at roughly the same time (a collision), it may appear that they both belong to the same frame — that is, until the data is error checked. Even with error checking, some errors creep into the system, but those additional errors (usually in the data itself) are left to the higher-layer protocols to diagnose.

You are used to 8-bit character assignments based on translation tables such as ASCII, but this octet size is just one possible way of representing characters. Larger character sets use wider bit representations, with Unicode being a prime example. There is no reason why 8-bits or even a multiple of 8-bits are used as characters or words, and from a network standards perspective, there needs to be flexibility when it comes to the number of bits. That is one reason why frame data is delimited and bit stuffing is used to bring the data up to a required length.

[Figure 12.1](ch12.html#ethernet_layers_and_their_relationship_t) shows the portion of the OSI reference model that corresponds to the various Ethernet networking component protocols. Ethernet defines protocols at the OSI Physical level (Layer 1) and the OSI Data Link Layer (Level 2). Different Physical layer protocols are used depending upon whether the wiring used is copper-based or fiber-based media. While both media types use the same MAC addressing, the different sublayers that connect the medium to the MAC layer vary based on media type, as shown on the right of the figure.

![Ethernet layers and their relationship to the OSI model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1201.png)

**Figure 12.1. Ethernet layers and their relationship to the OSI model**

The Medium Access Control (MAC) layer is where data encapsulation and media access control is performed. This includes frame sequence, assembly, and error detection, both during reception and after verification. The MAC portion initiates frame transmission and provides the means to retransmit frames when errors occur.

The Logical Link Control shown is the MAC client and applies when the end station is a Data Terminal Equipment (DTE) node. Above the MAC client are the upper-layer protocols such as TCP/IP and others. However, if the MAC client is a bridging unit or Data Communications Equipment (DCE) device, then there are no upper-layer protocols, and the connection is Ethernet-to-Ethernet.

### Frame structure

Ethernet frames consist of up to 11 different fields transmitted serially without any spaces or gaps. [Figure 12.2](ch12.html#the_structure_of_an_ethernet_open_parent) shows the structure of an Ethernet 802.3 frame with 11 fields that serve the following purposes:

- **Preamble (PRE)**. A sequence of 7 bytes of `10101010` that serves to alert receiving end stations that a frame follows. The alternating pattern helps to synchronize the medium-dependent interface of the Physical Layer.
- **Starting Delimiter (SD)**. The start-of-frame delimiter is the 1-byte sequence `10101011` with the final two ON bits of `1` indicating that the next bit starts the Destination Address field.
- **Destination Address (DA)**. A 6-byte field that indicates the end station or group of end stations (multicast) to which the frame is directed. The first bit is a `0` when the address is to a single end station or a `1` when it is directed to a group. The final bit is a `0` when the address is globally administered or a `1` when it is locally administered. The middle 46 bits are the unique MAC address of the destination: an end station (unicast), group of stations (multicast), or all stations (broadcast).
- **Source Address (SA)**. A 6-byte field that indicates the sending station. The first bit is always `0`, and the address is 46 bits long.
- **VLAN Type ID (VT)**. This optional 2-byte field specifies that the frame is a VLAN frame. (VLAN is discussed later in this section.) For VLAN to operate, all the end stations involved require that this feature be operational.
- **Tag Control Information (TCI)**. This optional 4-bit field for VLAN gives the priority of the frame and the VLAN group ID that the frame is meant for.
- **Length/Type (LT)**. A 2-byte field that indicates the size of the data field (46 to 1500 bytes) or that can be used to give the frame type ID for an optional format by using a value greater than 1536.
- **Data**. The payload being transmitted, from 46 to 1500 bytes. When the data is smaller than 46 bytes, it must be padded with zeros in order to bring the length up to 46 bytes.
- **Padding to Length (PAD)**. The PAD portion of the Data field adds enough non-data characters (typically zeros) to bring the frame up to the standard length.
- **Frame Check Sequence (FCS)**. A 4-byte field that has a 32-bit CRC (Cyclic Redundancy Check) value used to check for errors. [Figure 12.2](ch12.html#the_structure_of_an_ethernet_open_parent) shows the bits that are used to generate the CRC as indicated by the bar at the top of the figure labeled FCS Generation Span. The fields below that bar are used to generate the CRC value and placed into the FCS field just to the right of the included fields. Since the FCS Generation Span plus the FCS field are used in error detection, the second bar from the top labeled FCS Error Detection Coverage (CRC) indicates the portion of the frame used for error checking.
- **Extension**. The 12-byte Extension field is a non-data field used to make it easier to send Ethernet frames over Gigabit Ethernet networks. It is set to 416 bytes for 1000Base-X and 520 bytes for 1000Base-T.

![The structure of an Ethernet (802.3) frame](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1202.png)

**Figure 12.2. The structure of an Ethernet (802.3) frame**

Ethernet frames vary, depending upon the type of Ethernet network, although all follow the general format shown in [Figure 12.2](ch12.html#the_structure_of_an_ethernet_open_parent). Among the various versions of Ethernet frames that have been used are Novell's Raw 802.3 frame (no LLC header), IEEE 802.2 LLC, 802.2 LLC/SNAP, and Ethernet II (version 2). To support these different versions, the Length/Type field (also referred to as the EtherType field) is added into the MAC header just after the Source Address field. With the EtherType field specified, it is possible to have different versions of Ethernet running over the same network concurrently.

### Burst mode

With the advent of Gigabit Ethernet, a high-speed burst mode was added to CSMA/CD. In burst mode, a sequence of bursts is transmitted up to about 8192 bytes (65,536 bits), enclosing multiple frames separated by interframe gaps (IFGs). Using frame bursts, a source can control the network longer and get up to three times more throughput for small frames than GigE could normally attain. Only GigE can be bursty; slower versions of Ethernet do not support the Extension field that maintains control of transmission by suppressing other stations from sending data. [Figure 12.3](ch12.html#gigabit_ethernet_burst_mode) shows a GigE frame burst, with the carrier cycle indicated by the longest length that can carry a maximum burst.

![Gigabit Ethernet burst mode](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1203.png)

**Figure 12.3. Gigabit Ethernet burst mode**

### VLAN frames

A VLAN, or virtual LAN, is a set of nodes that are grouped into a logical broadcast domain that is independent of their physical locations. Data sent from a node on one network to a node on another network appears as if the remote network is part of the local network. VLAN traffic can be prioritized, grouped, and administered from a single console. A VLAN is a Layer 2 definition of a segregated grouping and is used to create the equivalent of subnets on Layer 3 of IP networks.

### Note

Products based on a VLAN are described in [Chapter 16](ch16.html).

To support a VLAN's features, two fields are inserted into the Ethernet frame just before the Length/Type field (EtherType). The first field is the 2-byte VLAN Type ID field, which identifies the frame as a VLAN frame; the second field is the 2-byte Tag Control Information field, which contains a priority number from 0 to 7 (highest) and the VLAN ID (group identifier). When Ethernet frames are tagged with VLAN fields, all nodes participating in the VLAN must have that option installed.

## Carrier Sense Multiple Access with Collision Detection

Carrier Sense Multiple Access with Collision Detection (CSMA/CD) is a half-duplex communications protocol that used to allow the traffic from many nodes to broadcast over a common medium concurrently. It was meant to be an alternative to token-based networks and to allow a network to be used as close to its capacity as it could be. Because it is possible to have two or more stations send an Ethernet frame that overlaps, the receiving station may not be able to detect the different bit streams, and an error occurs. This type of error is referred to as a *collision*. CSMA/CD provides for error detection and recovery when collisions occur.

The name is derived from the following:

- **Carrier Sense**. This provides the rules needed so that end stations can determine the start and end of frames based on transmission gaps.
- **Multiple Access**. Any station can transmit on the network when it detects that the network is quiet.
- **Collision Detection**. When two (or more) sending stations detect that a collision has occurred, they must resend the frame after a period of time that is determined by a back-off algorithm that generates a pseudo-random number.

Ethernet CSMA/CD networks exist in one of three states:

- **Transmission**. Data is traveling from source to destination over the network.
- **Quiescence (idle)**. No data is in transit.
- **Contention (collision)**. Data from two sources are traveling over the network at the same time.

Collisions on Ethernet networks occur all of the time; the higher the network utilization, the higher the percentage of frames that are involved in collisions. However, it has been demonstrated that Ethernet can still attain a throughput of 90 percent of its theoretical carrying capacity because of the use of recovery that CSMA/CD provides.

Longer network runs lead to time differences in the detection of collisions by different stations. It is this fact that sets the maximum run length for Ethernet, which is balanced by the frame size that was chosen. When Ethernet moved to faster standards (100 Mbits/s and greater), the time delay for collision detection shrank, and this balance of run length and frame size needed to be altered. For 100 Mbits/s Ethernet, the decision was made to keep the frame size the same and reduce the run lengths, while for 1 GigE, the run length was kept the same as 100 MHz, and an extension field was added to the end of the Ethernet frame. This non-data Extension field makes it appear as if the frame is larger than it is, and was set to 416 bytes for 1000Base-X, and 520 bytes for 1000Base-T. [Table 12.3](ch12.html#ethernet_frames_versus_run_lengths_1) summarizes frame sizes and connection lengths for different Ethernet speeds.

**Table 12.3. Ethernet Frames versus Run Lengths 1**

| Factor | 10 Mbits/s | 100 Mbits/s | 1000 Mbits/s |
| --- | --- | --- | --- |
| 1.Calculated for half-duplex operation. 2. The maximum collision diameter is the longest distance between any two stations (DTEs) in any collision domain. |  |  |  |
| **Minimum frame size** | 64 bytes | 64 bytes | 416 bytes for 1000Base-X and 520 bytes for 1000Base-T |
| **Maximum collision diameter**2 | 100 UTP | 100 UTP412m fiber | 100m UTP316m fiber |
| **Maximum distance allowed between repeaters** | 2500m | 205m | 200m |
| **Number of repeaters allowed in a path** | 5 | 2 | 1 |

To transmit an Ethernet frame using CSMA/CD, the following sequence occurs:

1. The frame is prepared for transmission.
2. The carrier (medium) is sensed for activity by the sending station.
3. If the medium is idle, then transmission occurs. If the medium is busy, then transmission is delayed for a period that is determined by the protocol, which in Ethernet is called the interframe gap (IFG), interframe spacing, or interpacket gap (IPG).
4. The sending station monitors the wire to determine if the bits it receives back are the same as the bits it sent, which is a test for a collision. When collisions are detected, the sending system or systems stop transmitting and perform a collision remediation scheme, as described in the next procedure. The mechanism in this step is important because it limits the amount of time that a wire is captured by any one sending station.
5. Upon acknowledgment from the end station, the sending station ends transmission and sets the CSMA/CD counters to zero.

The IFG is the minimum idle time that must be observed on an Ethernet network before a device is allowed to send a frame. This quiet period allows other devices to reset their network stacks so that they can receive the frame that is about to be sent. The length of the gap is protocol dependent. Typical values are:

- 10 Gigabit Ethernet (10 GigE) — 9.6 nsec (nanoseconds, 10-9 seconds)
- 1 Gigabit Ethernet (1 GigE) — 96 nsec
- Fast Ethernet (100 Mbits/s) — 960 nsec
- Ethernet (10 Mbits/s) — 9.6 (sec (microseconds, 10-6 seconds)

These numbers are not inviolate. Network interface card vendors with faster chip sets often reduce the IFG to improve data throughput. The Intel EtherExpress PRO/100B NIC is an example of a card that uses this feature. Network repeaters, devices that amplify signals for longer-distance transmission, also shrink the IFG. As frames arrive at their destinations, network conditions can also act to reduce the IFG due to transit of a repeater, packet assembly en route, or network congestion. The IFG can tolerate a reduction that is equivalent to 40 bit times (5 bytes) for 10 GigE, 64 bit times (8 bytes) for 1 GigE, or 47 bit times for 10 Mbits/s Ethernet.

Upon detection of a collision, CSMA/CD performs the following steps:

1. Sends additional packets so that all receivers detect a collision.
2. Raises the CSMA/CD counter.
3. At maximum transmission, attempts ceiling abort transmission.
4. Pauses for an amount of time, based on how many collisions were detected.
5. Starts over transmitting the frame, as is described in the previous procedure.

## Full-duplex operation

Faster versions of Ethernet have tended to switch from CSMA/CD half-duplex communication to full-duplex communications. In a full-duplex connection, data travels in both directions without collisions. This allows for faster transmission, smaller Ethernet frames due to the elimination of the Extension field, and a network bandwidth that is roughly two times greater. Frames sent over a full-duplex point-to-point connection are separated by interframe gaps (IFG), just the way they would be on a half-duplex network, and frames are transmitted as they become ready at the sending station.

To make full duplex practical, Ethernet has to enforce flow control at the switch or router so that network congestion is avoided, and separate frame buffers must be established for data traveling in each of the two directions. A pause frame is transmitted at the receiving node and sent to the sending station when the rate of dropped packets is detected beyond a certain threshold. Pause frames are constructed so that they are unique and can't be processed beyond the MAC client layer.

Full-duplex communications and flow control can be used on any type of Ethernet and at any speed. In order for this method to be implemented, the link involved must have the appropriate physical layer equipment needed to support the full-duplex mode.

# Token Ring Networks

In a relay race, one runner passes the baton to the next runner, who then runs to the next station and hands the baton off once again. In a token-based network, the baton is a token frame that gives the right to send data on the network from one node to the next. The time that any one node has control over traffic is short. Because there is only one node that is communicating, token-based networks don't suffer from the inefficiencies of collisions and dropped data, and they can send data in much larger chunks than Ethernet can. In order to have periodic or cyclic data access, token-based networks are always built as topological rings, as shown in [Figure 12.4](ch12.html#a_token_ring_apostrophy_s_logical_topolo).

On the left in [Figure 12.4](ch12.html#a_token_ring_apostrophy_s_logical_topolo) is a single token ring wired into a single MAU or Multiple Access Unit. A MAU is a routing device with an In port, a number of additional ports (numbered 1–6 in the figure), and an Out port (shown on the right). Each dot is a node having two wires, one for incoming and another for outgoing data. Data traffic travels in one direction around the ring. You can expand a token ring by adding multiple token rings together as shown in the figure on the right.

![A token ring's logical topology (left), and four rings concatenated together (right)](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1204.png)

**Figure 12.4. A token ring's logical topology (left), and four rings concatenated together (right)**

IBM developed Token Ring networks in the late 1970s at the same time that Ethernet was being developed at Xerox PARC and that ARCnet was being deployed. The original Token Ring standard has a line speed of 4 Mbits/s compared to the 10 Mbits/s Ethernet of the time. In 1989, a 16 Mbits/s Token Ring standard was introduced. Token Ring networks had a competitive performance advantage over Ethernet early on because, even though they ran at slower speeds than Ethernet, they could transmit much larger packet sizes, resulting in greater throughput.

That early advantage of Token Ring networks over Ethernet was squandered by the higher prices of the switches and network adapters, and by the fact that all competing Token Ring technologies, such as the ones Apollo Computer and Proteon introduced, wouldn't interoperate with IBM's version. The IEEE 802.5 standard is based on the IBM Token Ring but generalizes it so that it isn't dependent upon a particular media type or topology.

ARCnet largely disappeared from the LAN marketplace in the mid-1980s, displaced by Ethernet, although it remains in limited use in the embedded systems market. Fast Ethernet (100 Mbits/s) also overtook Token Ring technology. By the time Fast Ethernet appeared, switch vendors had developed methods to significantly reduce collisions on Ethernet networks. The lower cost of implementing Ethernet removed Token Ring technology's chance to dominate the LAN marketplace. Today, you are hard-pressed to find Token Ring technology anywhere outside of an IBM-based shop. However, Token Ring technology has played an important role in the development of network technology and continues to have an influence on the development of future network technologies, and so a brief discussion on how it works is valuable.

Token Ring networks are logical rings in the sense that the wiring is looped from the point of attachment back to the switch. In the case of IBM's Token Ring, the switch is called a Multiple Station Access Unit (MAU or MSAU). If you were to install a Token Ring network, you would begin by locating the MAU in a central location such as a wiring closet, and then run a wire from the MAU to each of the hosts (called end stations) on your network.

The network is a physical star topology, with spokes radiating outward from a central hub. The "ring" of the Token Ring network is implemented inside the MAU. Each host is connected by a Type-1 twisted-pair wire called a *lobe cable*, a hermaphroditic connector which, taken together, is IBM's Structured Cabling System. Token Ring networks span the OSI data model from the Physical Layer through the Network Layer to include Data Link Layer components. Each MAU has an input port and an output port, which can be used to expand the token ring.

[Figure 12.5](ch12.html#a_network_of_four_concatenated_token_rin) shows a set of four token rings that have been concatenated together to form a larger network. Each MAU can connect to six end stations, but for clarity, only two are shown connected to a MAU. [Figure 12.5](ch12.html#a_network_of_four_concatenated_token_rin) is the physical implementation of the topological figure shown on the right side of [Figure 12.4](ch12.html#a_token_ring_apostrophy_s_logical_topolo). Note that there are patch cables that extend the Token Ring. Those patch cables run from each MAU and connect all four MAUs. Data travels in one direction on the patch cable, but in two directions in the lobe cables. An exploded view of the lobe cable is shown in the lower center of [Figure 12.5](ch12.html#a_network_of_four_concatenated_token_rin).

The token in a Token Ring network is a 3 (8-bit) byte frame that is passed from one node to another. When a node has network control, it can send a data frame. When that data is correctly received at the destination node, that node converts the data frame to a token frame and transmits that token frame to the next node on the network. While the data/command frame is circulating, no other tokens can be on the network unless the network supports a feature called *early release*. On a 4 Mbits/s Token Ring network, only a single token could be passed, but on the 16 Mbits/s standard, several tokens could be circulating on the network concurrently. The system essentially eliminates frame collisions, which makes it a very robust network with predictable data delivery.

![A network of four concatenated token rings](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1205.png)

**Figure 12.5. A network of four concatenated token rings**

Token rings implement traffic control using a priority bit, set to between 0 and 7. When a node receives a token that has a priority that is less than its own, the node changes the priority bit and retransmits the token. The token passes around the network until it reaches a node with the highest priority setting. At that point, the token is changed to the highest setting, and sent around the ring until it returns to the highest-priority node, which then receives a data frame. After the data has been received, the token's priority is reset to the value it had when it first arrived at the node with the highest-priority setting. In this manner, nodes are serviced based on their priority settings.

[Figure 12.6](ch12.html#token_ring_frame_structures) shows the structure of a Token frame, a Data or Command frame, and an Abort frame. The Data or Command frame carries a payload that can be any size up to 18,200 bytes. The Starting Delimiter (SD) field, shown at the bottom of [Figure 12.6](ch12.html#token_ring_frame_structures), shows the different values that it stores. Those values set the priority that the data transmission has, which is used to control which source has access to the network at the moment. The SD field also provides the token, as well as the values required to provide the Quality of Service functions provided by the value of the Monitor value as well as the Reservation value.

Token ring frames use a time-based encoding method called *Manchester encoding*, which maintains clock rate by providing a data transition (1 to 0 or 0 to 1) at a regular interval. To create a Manchester code, you would perform an XOR (exclusive OR) of the clock and the data, as shown below for a four-digit number:

- Data String: `1100`
- Clock String: `1010`
- XOR Manchester code: `0110`

Manchester encoding has also been used in Ethernet but has given way to differential Manchester encoding (Conditioned Diphase), where the data and the clock signals are synchronized. In differential Manchester encoding, it is the transition itself that encodes the logical value. The strings are combined as follows:

- Data String: `11001100`
- Clock String: `10101010`
- Differential Manchester code: 1`0100101`

Differential Manchester encoding is part of the 805.2 Token Ring protocol specification and is used in IBM's Token Ring.

Because there is always the possibility of network errors, an end station called an *Active Monitor* is always evaluating the state of the token and correcting any errors it detects. Because this is a mission-critical function on a Token Ring network, a backup or standby monitor can be deployed. When two token rings are joined, one monitor is selected to be the active monitor, and only that station monitors the network. Election of a new active monitor can also be initiated when there is no signal on the network, when the active monitor isn't detected, or when a token frame isn't detected within a certain time period. Any end station can be a monitor, as it is built into the Token Ring protocol.

The Active Monitor plays a critical timing role in a Token Ring network. It runs the network clock, inserts a buffering delay, suppresses token circulation when a data/command frame is being sent, and ensures that tokens are indeed circulating. A Token Ring algorithm called *beaconing* tests the network and creates a beacon frame when a fault is detected. Beaconing can initiate an auto-reconfiguration, which is essentially a diagnostic or reboot of the MAU. During a beaconing operation, data cannot be passed over the token ring.

Token Ring networks are not the only networks that use tokens. FDDI networks, which are described in the next section, are the other major example of token-based networks.

![Token Ring frame structures](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1206.png)

**Figure 12.6. Token Ring frame structures**

# Fiber Distributed Data Interface Networks

Fiber Distributed Data Interface (FDDI) is a Token Ring network protocol that is used to create high-speed Local Area Networks. The protocol is specified as the IEEE 802.4 standard, and the technology is the ANSI standard X3T12. FDDI is differentiated from 802.5 Token Ring networks by its use of a timing mechanism for token exchange. FDDI uses optical fiber as its physical medium; a related technology using the same protocol but with copper wire is referred to as CDDI. [Figure 12.7](ch12.html#the_relationship_of_the_fddi_protocol_to) shows how different portions of the FDDI protocol correspond to the OSI reference model.

In [Figure 12.7](ch12.html#the_relationship_of_the_fddi_protocol_to) the two OSI layers are labeled in the left column above the Media layer. The Token Ring protocol has the SMT spanning the Physical Layer and part of the Data link layer. By contrast, although the Logical Link Control layers for FDDI and Token Ring protocols are the same, the Station Management Task portion of Token Ring is split into a MAC layer and into different and separate Physical layer protocols. Depending upon whether FDDI uses fiber- or copper-based media (wiring) the protocols are PMD and PHY or TP-PMD and TP-PHY, respectively.

![The relationship of the FDDI protocol to the OSI model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1207.png)

**Figure 12.7. The relationship of the FDDI protocol to the OSI model**

There are two types of devices that are defined on an FDDI network:

- **Stations**. Stations are computers, printers, and other active devices. They can be Single Attached Stations (SAS) or Dual Attached Stations (DAS).
- **Concentrators**. Concentrators are devices that connect an SAS to the FDDI network. When connected to a ring, concentrators are Dual Attached Connectors (DACs) and have three port types: A (Primary ring), B (Secondary ring), and M (Master). Concentrators can also be Single Attached Connectors (SACs), and through their M port, connect to the single Slave (S) port of a SAS.

There are three different connection types:

- **Single Attached Stations (SAS)**. SAS devices.
- **Dual Attached Stations (DAS)**. DAS are ring connected and must be operational for the ring to be fully functional.
- **Dual Homed**. Dual homed has a concentrator or DAS connected to two other concentrators. It is equivalent to two SAS links.

As shown in [Figure 12.4](ch12.html#a_token_ring_apostrophy_s_logical_topolo), where the token ring exists within an MAU, FDDI rings also are implemented inside Dual Attached Concentrators. This allows for a simple stand-alone FDDI ring structure. If you have a Dual Homed concentrator, then you can create fault-tolerant paths to Dual Attached Stations. Both of these scenarios are shown in [Figure 12.8](ch12.html#a_stand-alone_concentrator_versus_a_dual). M-S connections can be either fiber optic or UTP cabling. In [Figure 12.8](ch12.html#a_stand-alone_concentrator_versus_a_dual) the primary ring is indicated by the dark lines in the figure while the secondary ring is indicated by the gray lines. Data travels in the directions indicated by the arrows at the head of the line.

![A stand-alone concentrator versus a Dual Homed concentrator](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1208.png)

**Figure 12.8. A stand-alone concentrator versus a Dual Homed concentrator**

To add more nodes to an FDDI network, you connect the one or more AB ports on a root concentrator to other concentrators and iterate this connection; this creates a hierarchical tree of concentrators. You can also create a ring of trees by replacing a root concentrator with a dual FDDI ring structure. The ring-of-trees topology is often used for campus-wide LANs. In many instances, FDDI networks are connected to Ethernet networks to create a mixed network type. Mixed networks require that FDDI/Ethernet IP routers be placed as the edge devices separating the three network types — tree of concentrators, ring of trees, and mixed FDDI/Ethernet networks.

[Figure 12.9](ch12.html#three_different_types_of_fddi_network_to) shows these three topologies. The three different network types illustrate different approaches to utilizing FDDI in increasingly larger types of network. FDDI can be used as a backbone of concentrators as shown in the Tree of Concentrators topology. The Ring of Trees topology allows for a hierarchical fan out of FDDI with each concentrator on the main ring serving the function of a root in its particular tree. Each level in the Ring of Trees is referred to using the name Primary, Intermediate, and Horizontal distribution frames. You can also create a mixed FDDI/Ethernet network by combining an FDDI ring with connections to Ethernet networks through FDDI/IP routers.

![Three different types of FDDI network topologies: Tree of concentrators, ring of trees, and mixed FDDI/Ethernet network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1209.png)

**Figure 12.9. Three different types of FDDI network topologies: Tree of concentrators, ring of trees, and mixed FDDI/Ethernet network**

FDDI has been widely used in the telecommunication industry as a core network system but is being displaced by high-speed Ethernet, as have other Token Ring networks. Version 2 of the FDDI standard (FDDI-II) added circuit switching to this network type. There has been a considerable investment in FDDI networks in the past, and they are used for both voice and video transmission. FDDI networks are now often connected to Synchronous Optical Network (SONET), which is used as a backbone for modern high-speed networks.

### Note

SONET is described in [Chapter 13](ch13.html).

FDDI is constructed using two token rings, each sending data in opposite directions; these dual-ring networks are often deployed in room-sized LANs. The primary ring runs at 100 Mbits/s and the counter ring either performs backup or adds another data channel to the network that extends the throughput of the network to 200 Mbits/s. FDDI network interfaces on FDDI routers connect to both rings, making them dual-homed or dual-attached systems. Hosts connecting to an FDDI network are single attached. As is the case with other optical networking systems, devices called concentrators allow multiple hosts to communicate through the network using a single fiber connection.

If the second token ring is configured to be a backup, and ring connections are dual homed, then the network can fail over to the secondary ring should the primary active token ring suffer a broken connection. [Figure 12.10](ch12.html#fddi_is_a_highly_fault-tolerant_high-spe) shows an FDDI network that has suffered two points of failure: a failed cable and a failed Dual Attached Station (DAS). One point of failure leaves the network functional; a second point of failure divides the network into two smaller networks.

![FDDI is a highly fault-tolerant high-speed LAN; even two faults simply segment this basic dual-ring network.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1210.png)

**Figure 12.10. FDDI is a highly fault-tolerant high-speed LAN; even two faults simply segment this basic dual-ring network.**

FDDI is notable for its combination of speed, potential long-distance connections, and high host connection count. FDDI can connect to 500 DAS or 1000 SAS nodes. Optical cable runs for an FDDI link can be up to 125 miles (200 km) and are for networks that have thousands of connected users. The rings themselves can be half that distance, 62 miles (100 km). This distance is the reason that FDDI is a very popular Metropolitan Area Network (MAN) technology.

CDDI (FDDI over copper wire), by comparison, has a maximum rated throughput of 16 Mbits/s, and a maximum connection length of 250m for shielded twisted-pair (STP), or 72m for unshielded twisted-pair (UTP) wiring.

# Automation Networks

Networks don't just exist to connect computers, although the bulk of this book is dedicated to computer networks. Networks exist to connect a wide variety of devices. Cars and planes have networks, which are LANs with a set of connected computers, a host of sensors, and other devices that make them very sophisticated systems. You only have to watch a mechanic hook up an automobile diagnostic handheld computer to appreciate how useful networked components are.

If you have been interested in smart houses, you may be familiar with the X10 standard for home automation, which is described in the following section. Go into any modern high-rise building and you will probably find that the HVAC (Heating, Ventilation, and Air Conditioning) and lighting systems are computer controlled, often from a single console or computer. More generally, you will find that network systems are built to sense and control all manner of industrial equipment. Automotive assembly-line robots, pharmaceutical plant recipes, railroad train movement, package tracking, and other activities form networks that rely on control functions to operate.

All of these automation networks find different ways of abstracting networked devices from the software that is used to detect and control them. Some networks connect sensors, switches, valves, and activators to network hubs or switches that can recognize the output of device drivers on network devices. If you connect those switches to a computer or a network of computers, software can be used to analyze the signals and send commands that control these devices. Systems of this type are sometimes referred to as Human Machine Interface (HMI) systems, or alternatively, Supervisory Control and Data Acquisition (SCADA).

The methods that these computers use to discover network devices are often industry standards that you've already learned about, such as SNMP. The devices used to aggregate automated device signals and distribute commands, sometimes referred to as Programmed Logic Controllers, may communicate using proprietary software or open standards such as Sun's Java, Microsoft's OLE, DCOM, or even .NET Framework components.

Many of these types of networks are proprietary to the manufacturers that build these systems, but there are some network types that are open standards. In the sections that follow, you'll learn about some of the more successful open standards, how they are implemented, and where they are used.

## X10 and home automation

The X10 standard is an open standard for signal communication and control of devices over power lines. It is widely used to automate homes by creating home automation networks that have been dubbed *smart homes* or *domotics*. X10 defines a protocol for radio transmission signals over a carrier wave. Very short low-power RF bursts are transmitted synchronously with the power line signal such that the signal which corresponds to the power wave's inflection points (zero amplitude) is a logical one, and any inflection point without a signal is a logical zero.

Because the signal is at a higher frequency than the carrier wave, the signal is actually repeated two times between inflection points, between 0 and π, and two more times again between π and 2π. Those additional signals are used for timing and aren't measured as an X10 signal, although they do play an important role. Many encoding schemes don't simply rely on a signal being recognized as a 1 or 0. Instead, what they do is to have two signals, the first bit of which is the signal and the second bit of which is a synchronization bit. To generate a 1, not only must the first bit be a 1, but the second bit must also be a 0; that is, a High-Low signal pair is recognized. For a 0, the first bit would be 0 and the second bit would be 1 — a Low-High signal pair. It is that transition that makes the bit boundaries easier to locate and less prone to error. [Figure 12.11](ch12.html#x10_radio_signals_on_a_power_line_carrie) shows the carrier wave and signal, with a 1 msec bar indicated as part of the legend below the figure.

If you have an X10 controller, either a remote control or a virtual button on a console, and you press a button, a binary code is transmitted over the power line. The code is a set of three binary identifiers: a START CODE (4 bits, `1110`), HOUSE CODE (8 bits), and CONTROL CODE (10 bits), which defines an X10 frame. The CONTROL CODE can be a NUMBER CODE or FUNCTION CODE and uses alternating inflection points to encode its binary signal, ignoring the bit in between. [Figure 12.12](ch12.html#an_encoded_x10_signal._the_intermediate) shows a sample encoding, which requires 11 full cycles and illustrates the full length required by a CONTROL CODE for transmission. The different lengths and spacing of the codes make them all unique and make it possible for a translation table to be built.

The X10 standard has a complete set of the codes sent twice back to back, a space of three power line cycles, and a repeat of the codes. Also, any time commands are used that are sent to different devices, there must be three cycles of null bits transmitted. The codes for bright and dim settings are meant to be sent continuously with no spacing between the codes, and with at least two and preferably more repetitions. [Table 12.4](ch12.html#x10_command_codes) shows the X10 translation code.

X10 works by plugging a receiver unit into a power outlet in your house, and then plugging the device being controlled into the X10 receiver. Devices can be lights, televisions, temperature controllers, fans, and other household appliances. Different devices require different types of X10 modules. In some cases, modules are designed so that they have local control and can be turned on by a physical switch. Many light modules also have a feature called *local dimming*, which allows for the light to be turned on and off through progressive settings. [Figure 12.13](ch12.html#some_of_the_devices_inside_a_home_that_c) shows some of the devices that can be controlled in an X10 network inside a home. For example, the hose shown at the lower right of the figure is controlled by a metering switch that is plugged into an X10 switch.

![X10 radio signals on a power line carrier wave](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1211.png)

**Figure 12.11. X10 radio signals on a power line carrier wave**

![An encoded X10 signal. The intermediate timing signals have been omitted for clarity.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1212.png)

**Figure 12.12. An encoded X10 signal. The intermediate timing signals have been omitted for clarity.**

![Some of the devices inside a home that can be controlled by an X10 network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1213.png)

**Figure 12.13. Some of the devices inside a home that can be controlled by an X10 network**

Each X10 receiver is assigned a unique address so that it can receive signals. The X10 transmitter can be a remote control keypad, or it can be a software program on a PC that is interfaced to the X10 system through a transceiver that is also plugged into a power outlet. When a keypad is used, it uses one of the command codes shown in [Table 12.4](ch12.html#x10_command_codes) to communicate with specific devices.

**Table 12.4. X10 Command Codes**

| Code | Bit 1 | Bit 2 | Bit 3 | Bit 4 |  |
| --- | --- | --- | --- | --- | --- |
| [[a]](#ftn.CHP-12-TFN-1) |  |  |  |  |  |
| START | 1 | 1 | 1 | 0 | - |
| **House Code** | **Bit 1** | **Bit 2** | **Bit 3** | **Bit 4** |  |
| A | 0 | 1 | 1 | 0 |  |
| B | 1 | 1 | 1 | 0 |  |
| C | 0 | 0 | 1 | 0 |  |
| D | 1 | 0 | 1 | 0 |  |
| E | 0 | 0 | 0 | 1 |  |
| F | 1 | 0 | 0 | 1 |  |
| G | 0 | 1 | 0 | 1 |  |
| H | 1 | 1 | 0 | 1 |  |
| I | 0 | 1 | 1 | 1 |  |
| J | 1 | 1 | 1 | 1 |  |
| K | 0 | 0 | 1 | 1 |  |
| L | 1 | 0 | 1 | 1 |  |
| M | 0 | 0 | 0 | 0 |  |
| N | 1 | 0 | 0 | 0 |  |
| O | 0 | 1 | 0 | 0 |  |
| P | 1 | 1 | 0 | 0 |  |
| **Key Codes** | **Bit 1** | **Bit 2** | **Bit 3** | **Bit 4** | **Bit 5** |
| 1 | 0 | 1 | 1 | 0 | 0 |
| 2 | 1 | 1 | 1 | 0 | 0 |
| 3 | 0 | 0 | 1 | 0 | 0 |
| 4 | 1 | 0 | 1 | 0 | 0 |
| 5 | 0 | 0 | 0 | 1 | 0 |
| 6 | 1 | 0 | 0 | 1 | 0 |
| 7 | 0 | 1 | 0 | 1 | 0 |
| 8 | 1 | 1 | 0 | 1 | 0 |
| 9 | 0 | 1 | 1 | 1 | 0 |
| 10 | 1 | 1 | 1 | 1 | 0 |
| 11 | 0 | 0 | 1 | 1 | 0 |
| 12 | 1 | 0 | 1 | 1 | 0 |
| 13 | 0 | 0 | 0 | 0 | 0 |
| 14 | 1 | 0 | 0 | 0 | 0 |
| 15 | 0 | 1 | 0 | 0 | 0 |
| 16 | 1 | 1 | 0 | 0 | 0 |
| All units off | 0 | 0 | 0 | 0 | 1 |
| All lights on | 0 | 0 | 0 | 1 | 1 |
| On | 0 | 0 | 1 | 0 | 1 |
| Off | 0 | 0 | 1 | 1 | 1 |
| Dim | 0 | 1 | 0 | 0 | 1 |
| Bright | 0 | 1 | 0 | 1 | 1 |
| All lights off | 0 | 1 | 1 | 0 | 1 |
| Extended code | 0 | 1 | 1 | 1 | 1 |
| Hail request[[a]](ch12.html#ftn.CHP-12-TFN-1) | 1 | 0 | 0 | 0 | 1 |
| Hail acknowledge | 1 | 0 | 0 | 1 | 1 |
| Preset Dim | 1 | 0 | 1 | - | 1 |
| Extended Data Analog | 1 | 1 | 0 | 0 | 1 |
| Status On | 1 | 1 | 0 | 1 | 1 |
| Status Off | 1 | 1 | 1 | 0 | 1 |
| Status Request | 1 | 1 | 1 | 1 | 1 |
| [[a]](#CHP-12-TFN-1)Three blank cycles between each pair of transmissions is required, except for dim and bright. |  |  |  |  |  |

In software, devices can be programmed up to the limit of the sophistication of the program. They can be used to control home theaters with custom-made interfaces, run event schedules, log events, send messages upon events, and almost any other action you can think of. Among the best-known home automation software programs are Central Home Automation Director (CHAD) Software, HAL 2000 Voice Control Software, Home Controls, HAI Web-Link, HomeSeer Software, Indigo, PowerHome, Smarthome Manager PLUS, Superna ControlWare, and Thinking Home.

The X10 protocol also allows for radio frequency devices such as keypads, keychains, burglar alarms, IR switches, and other devices. In the U.S. the radio frequency is 310 MHz, and in Europe it is 433 MHz. A radio receiver provides the bridge needed to transmit X10 commands over the wired network. Some of the devices that can be on an X10 network are shown in [Figure 12.14](ch12.html#devices_inside_and_outside_a_house_that).

![Devices inside and outside a house that can be controlled by X10](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1214.png)

**Figure 12.14. Devices inside and outside a house that can be controlled by X10**

### Tip

Perhaps the best-known commercial Web site for home automation products is `www.Smarthome.com`.

While X10 is the best known of the home automation networking systems, there are many other systems in use that you might want to consider. These alternatives include INSTEON, UPB, ZigBee, and Z-Wave. [Table 12.5](ch12.html#common_home_automation_networks) lists some of the standards used in home networks and compares them to different computer standards.

**Table 12.5. Common Home Automation Networks**

| Network Type | Medium | Throughput | Connection Limit |
| --- | --- | --- | --- |
| **Bluetooth** | RF | 1 – 10 Mbits/s | 10 – 20m |
| **Ethernet** | UTP or fiber optic | 10 Mbps – 1 Gbits/s | 100m – 15 km |
| **HomePlug** | RF over power lines | 14 – 200 Mbits/s | 200m |
| **HomePNA** | Telephone line | 10 Mbits/s | 300m |
| **INSTEON** | RF over power lines |  |  |
| **IRDA** | Infrared | 9.6 Kbits/s – 4 Mbits/s | 2m (line of sight) |
| **LonWorks** | UTP, RF over power lines, RF, IR, or Ethernet | 1.7 Kbits/s – 1.2 Mbits/s | 1,500 – 2,700m |
| **Wi-Fi (IEEE 802.11)** | RF | 11 – 248 Mbits/s | 30 – 100m |
| **X10** | RF over power lines | 50 – 60 bits/s | 500m |
| **Z-Wave** | RF | 9.6 – 40 Kbits/s | 30m |
| **ZigBee** | RF | 20 – 250 Kbits/s | 10 – 75m |

In [Table 12.5](ch12.html#common_home_automation_networks) the different types of home networking automation systems are described. Networked automation also plays an essential role in industrial systems as well. In the section that follows, different process control systems for industry are described.

## Process control systems

Industrial automation networks that control processes are most often built with some form of distributed control system (DCS). An industrial process control might include controlling oven temperatures in a bakery, part delivery on an assembly line, lights on a factory floor, or any other controllable feature of a plant or factory. Elements of the network are deployed at the point of service for the devices that they monitor and/or control. These network elements provide output through a bus to an aggregation/translation device where the signals from the different elements can be converted into a form that is compatible with the network that the control system is on. DCS systems are used in chemical plants, electrical power grids, HVAC, oil refining and transportation, pharmaceuticals manufacturing, sensor networks, vehicles, water treatment and management, and hundreds of other industries.

The best way to think about a DCS system is that there are usually two networks involved, connecting three layers of devices. The distributed part of the system is the group of sensors, controls, actuators, and other devices that are performing their role in the systems that the network is meant to control. This defines what can be called the device layer.

[Figure 12.15](ch12.html#a_process_control_network_with_three_dif) shows a process control system. In this type of system, a control console or SCADA system (Supervisory Control and Data Acquisition) is used to interact with the automate system. The SCADA typically shows a graphical HMI or Human Machine Interface display indicating the current state of the system and allowing an operator to make modifications. Commands go to the PLC or Programmable Logic Control, as does the input and output of data from connected devices. The PLC connects to devices that send data (output devices) or that take data (commands) such as the input devices shown. This is a distributed architecture with a top level network such as Ethernet, a device bus, and a layer of devices.

Simple processors or ASICs in these devices transmit what are called field signals, and many receive and process controls using a wire protocol that the devices understand. These field signals that are transmitted can be analog or digital values, Booleans (ON or OFF, 1 or 0), arrays of values all updating in real time; data can flow out of many devices in a flood in such a large amount that only a small percentage of the signals may be sampled. Many sensors sample their circuits and output values at a rate in the millisecond range, creating hundreds of values per second. Software that collects the data and graphs it or creates a historical log file for later replay or analysis will usually discard most of the data, and sensors send and sample it in manageable intervals.

The device layer is connected through a device bus to a module that serves to multiplex/demultiplex the field signals. These modules go by a number of names, depending upon the protocol, technology, vendor, and other factors. One common type of aggregation device is a Programmable Logic Controller, or PLC. PLCs are special-purpose computing devices with extensive I/O capabilities. They were developed in the late 1960s in an effort to integrate automation in the automobile industry in a way that would expose devices to a multivendor solution.

PLCs are real-time devices that take the input from distributed devices and make that data available to control systems. Some PLCs have internal logic that allows them to maintain a steady state using a feedback loop created with the data from a connected device. For example, if you had a reactor that required a certain temperature, the PLC would read the field data from a temperature sensor and then adjust the voltage to a heating element appropriately.

A PLC often serves as the interface between two or more heterogeneous network types. PLCs allow for multiple I/O connections, can read analog or digital data, respond to limit settings, and can control motors, cylinders, relays, solenoids, and many other devices. The "programmable" portion of the name refers to the ability of these devices to accept commands from other devices. PLCs may be configured with RS 232 or RS 485 serial ports, RJ-45 Ethernet, and other connections. Most PLCs are not only configurable, but also expandable. They come as chassis into which you insert PLC modules with the interface that you need.

![A process control network with three different network layers](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1215.png)

**Figure 12.15. A process control network with three different network layers**

PLCs often communicate with devices using a protocol such as Modbus or DF1, or with a variety of field buses such as DeviceNet or Profibus. There are many proprietary protocols and buses that are in use. Among vendors of PCL systems are ABB, Allen-Bradley, IDEC, Honeywell, Omron, General Electric, Mitsubishi, Siemens, and others.

Not all DCS systems rely on PLC-type devices. Some technologies require extremely high speed control signals that PLC devices can't keep up with; aircraft controls are a good example. Some automation tasks are repetitive and can be automated using mechanical timing devices at much lower cost. Devices called Remote Terminal Units (RTUs) were used in place of PLCs and have very similar characteristics, but RTUs lack the ability to be as extensively programmed as a PLC and are now less commonly used. Increasingly though the functions of PLCs and RTUs are merging.

These days, the differences between DCS, PLC, and RTU-based systems are rather hard to discern. I tend to associate DCS systems with large, expensive, and proprietary industrial automation networks. Some of the projects can run into the millions of dollars. PLCs tend to work with the newer open system standards that are vendor independent. "Open" automation systems are not open in the usual sense in that they are not platform independent. That is, with open standards, while you can mix and match hardware and software vendors, the technology is locked onto a particular network interapplication communication architecture. One technology is Microsoft's OLE for Process Control (and later DCOM), which spawned the OPC standards for automation systems. Automation systems have been built around Java, the .NET Framework, and other standards.

The third part of a DCS system, beyond the devices and the device bus, is the network containing the control software, which includes the SCADA software. SCADA software can be implemented as command line software but is more typically developed into graphical displays called HMIs that can be secured and locked in a manner that allows an operator to observe, maintain, or control systems at the level of access and privilege that the developer allows. A SCADA system built on top of an operating system such as Microsoft Windows would make full use of the modern object-oriented programming, offering fine granularity of control: users and groups, object security ACLs, scripting, and other features.

In the next sections you learn about two of the more important and commonly used device buses: Modbus and BACnet, as well as the OPC standards for data communication over Windows networks.

### Modbus

Modbus is the most commonly encountered serial data communications protocol in use on automation networks. This open standard was first published in 1979 by Modicon (now part of Schneider Electric) for use with their PLC systems. Versions of Modbus exist for serial port links and Ethernet, and the protocol can be transported over a TCP/IP network. There are variants of Modbus in use, including a lightweight version Modbus RTU (which encodes data in binary), Modbus ASCII (which translates data into readable but verbose text), Modbus+, or MB+ (which is Modicon's proprietary version of the protocol), and Modbus/TCP for Ethernet. The different types of network connections for these different versions of the Modbus protocol and network types are shown topologically in [Figure 12.16](ch12.html#different_types_of_modbus_networks_and_t).

In [Figure 12.16](ch12.html#different_types_of_modbus_networks_and_t) the Modbus protocol can be run over different network types. At the top the horizontal TCP/IP network (usually Ethernet) runs Modbus. Three switches above this network connect left to right to a control station (HMI) and to different devices, PLCs, and network storage systems (drives). Modbus can also run over other network types. Shown on the left, Modbus has been deployed over a MB+ network, in the center it is deployed over a serial bus network RS 232, and finally on the right Modbus is deployed over the two-wire half-duplex multipoint serial network designated as RS-485.

![Different types of Modbus networks and the connections that they support](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1216.png)

**Figure 12.16. Different types of Modbus networks and the connections that they support**

All forms of Modbus data use checksums to validate the data sent and require that the data stream be sent without gaps in the data. Therefore, Modbus devices that receive data over the wire must buffer out the gaps before either acting on the data or retransmitting it. [Figure 12.17](ch12.html#a_general_modbus_frame) shows a general Modbus frame. Address and Error Check are transport data that is added by the Transport layer protocol to create the Application Data Unit (ADU) frame. Contained within the ADU is the simple Protocol Data Unit (PDU), which is independent of the communication layers. The function code field is a set of values from 1–255 that tell a server what type of action to perform on the data that the frame contains. The data field is sent from client to server devices and contains additional information that the server uses to perform the action. The data can be items such as discrete or register addresses, number of quantity of items, and field byte counts, among other things. The data field can also be left out, indicating that the server's action is the default action and does not take any additional input.

![A general Modbus frame](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1217.png)

**Figure 12.17. A general Modbus frame**

On a Modbus, bus devices are assigned a unique address, with up to 247 devices on a single Modbus. Depending upon the Modbus type, devices can be in a master/slave relationship, or if they are on Ethernet, a peer-to-peer relationship. A master system is the only one that can initiate commands on the bus. Typical commands alter a value setting at the PLC or RTU, read or set a value stored in a register (address in memory), read a value in real time from a port I/O, and perform other actions.

### Note

To read the Modbus protocol specification, go to `www.modbus.org/specs.php`.

The data types used on Modbus (and other wire protocols) are:

- Floating point
- Boolean
- 8-bit and 32-bit data (32-bit is a Modbus extension)
- 32-bit Integer
- Exponential multipliers
- Mixed data
- 16-bit Word
- Binary Large Object Binary (BLOB) data (on other buses, but not Modbus)

If you had a switch that could be either open or closed, then that switch would store its condition as a 1 or 0 in its assigned register. To change its state, the supervisory station would issue a command to switch the value to 0 or 1, respectively. That value would then generate an action such as a voltage change that forces the switch to open and close.

### BACnet and LonTalk

The Buildings Automation and Control Networks data protocol, called BACnet, is an alternative to Modbus. This is an open standard that is supported by ANSI, ASHRAE (American Society of Heating, Refrigeration and Air Conditioning Engineers), and ISO. The BACnet standard predates Modbus, and when it was released in 1996 it was adopted by a number of vendors in the building automation industry.

BACnet was designed to be an object-oriented protocol with both device and object name and attribute discovery built in. The defined object types include the following: Analog Output and Value; Binary Input, Output, and Values; Event Enrollment Command; Device; File; Multistate Input and Output; Notification Class; Program; and Schedule. BACnet communications can be transported over ARCNET, BACnet over IP, Ethernet, Point-to-Point (P2P over RS 232), Token Ring (Master-Slave over RS 485), and LonTalk. BACnet is vendor independent and does not require any special hardware support.

LonTalk protocol predates both Modbus and BACnet and, although it was once a proprietary protocol of the Echelon Corporation, it is now an open ANSI standard. It is often mentioned as an alternative to both of these other protocols and is used in industrial, home, transportation, and building automation. The name comes from Local Operating Network, and the protocol depended upon an ASIC called the Neuron Chip. There are now multiple processors that are sold that support LonTalk.

### OPC

Microsoft's Object Linking and Embedding interapplication communications technology became the basis for the automation control industry OLE for Process Control (OPC). The process control industry developed OPC standards to exchange process data using Windows servers and clients. The OPC standards are developed by the OPC Foundation (`www.opcfoundation.org`) and define a set of methods (interface and protocols) for accessing data from devices on a network. OPC provides an open ("Microsoft-centric") standards-based approach for connecting data sources such as PLCs, controllers, I/O devices, databases, and so on with HMI client applications for graphics, trending, alarming, and other applications.

As Microsoft's networking technology moved from the Common Object Model (COM) to Distributed COM (DCOM), the OPC standard evolved with it. Applications using OPC were expressed as a set of ActiveX controls that could be added to a container object. Today, OPC embraces the .NET Framework with a version of OPC called OPC-Universal Access, or OPC-UA, that is under active development.

A number of versions of OPC exist, including:

- OPC Data Access (OPC-DA), which is used to connect to real-time data from devices
- OPC Alarm & Events (OPC-AE), which allows event data to be processed
- OPC Historical Data Access (OPC-HDA), which is an event- and data-logging standard
- OPC Batch, which is the standard used to automate batch processes
- OPC Data eXchange, which is used for server-to-server communications, monitoring, configuration, and management
- OPC Commands, which sends control commands to devices
- OPC XML-DA, which defines an interchange format for real-time data
- OPC Security, which is a technology for securing OPC data selectively from clients
- OPC Complex Data, which allows for communication of binary data and XML
- OPC Unified Architecture, which is the newest technology based on the .NET Framework

The three most important standards are OPC-DA, OPC-AE, and OPC-HDA.

OPC provides the interface between client and server applications by providing a universally supported and well-documented mechanism to communicate data from a data source to any client application. The standard includes the methods used to pass the data, as well as specific information on other attributes to supplement those data, such as range information, data type, quality flags, and date and time information. OPC servers collect the data from OPC devices aggregated at a PLC and make that data available to clients on a network. [Figure 12.18](ch12.html#an_opc_client_solidus_server_network) shows what an OPC network looks like.

In [Figure 12.18](ch12.html#an_opc_client_solidus_server_network) a three-tiered OPC network is shown. The topology is similar to the one you saw in [Figure 12.15](ch12.html#a_process_control_network_with_three_dif), except that the three different levels are inverted in this figure. At the bottom level is shown the client layer with an HMI (Human Machine Interface) control system. The alarm event viewer displayed on the monitor is shown at the bottom right. The client accepts event data and sends commands over the LAN to a variety of OPC servers that represent the middleware layer. In the OPC Server layer are shown an OPC Data Access (DA), Horizontal Data Access (HDA), Alarms & Events (AE), and Universal Access (UA) servers. Those servers take data from the Device layer or send commands from the Client layer to the Client layer and Device layer systems, respectively.

![An OPC client/server network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1218.png)

**Figure 12.18. An OPC client/server network**

The developing OPC-UA standard unites OPC-AE, OPC-DA, and OPC-HDA (Historical Data Access) into a complete specification. OPC-UA adopts a Service-Oriented Architecture (SOA) with an application model, namespace, and security scheme based on the Windows .NET Framework Architecture. OPC-UA has the following features:

- Data buffering, where data is transmitted and acknowledged so that its delivery is ensured.
- Data redundancy with alternate pathways, failover to mirrors, and other technologies.
- Heartbeat signals that provide a timing function that establishes the state of a connection and additional actions.
- A Security Model, which defines an access mechanism to OPC data based on authentication and authorization, and which uses encryption and access through a certificate and signature model.
- An Address Space Model that allows data sources and their values to be mapped.
- Backward compatibility to Data Access, Alarms, and Conditions, and Historical Access servers.
- Services and Service Mappings that allow data sources to be managed by a network or internetworking service model. Communication is through a set of OPC-UA APIs (for .NET, Java, and so on) that allow applications to access these services.

# Summary

In this chapter, you learned about different types of Local Area Networks and the technologies behind them. Ethernet, Token Ring, FDDI, X10, and different industrial automation bus standards, as well as all IEEE 802.x standards were detailed. Ethernet is a frame-based broadcast network. You learned why frames are used, and how they are constructed.

Token Ring networks use a special token frame to give network access to end stations. Fiber Distributed Data Interface (FDDI) networks are token rings that use optical fiber to create high-speed systems.

This chapter also looked at different automation networks. X10 RF over power-line networks can automate a home. Industrial networks use different technologies. Those networks aggregate the data from sensors, actuators, switches, valves, and other devices and make that data available to computers running monitoring and supervisory (control) software.

In the next chapter, you learn about Wide Area Networks, or WANs. WANs are characterized as being a collection of networks (internetworks) or networks with long-distance links.
