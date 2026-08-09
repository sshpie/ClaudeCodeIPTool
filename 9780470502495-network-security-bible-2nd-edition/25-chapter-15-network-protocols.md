# Chapter 15. Network Protocols

**IN THIS CHAPTER**

- **Reviewing the need for protocols**
- **Understanding the seven-layer OSI model**
- **Understanding the TCP/IP protocol**
- **Discussing address resolution**

For entities to communicate, they must agree upon a message format and define common practices for exchanging these messages. Computers and networks are no exception.

This chapter introduces layered communication models and explains the principal protocols used under these models for communication among computers.

# Protocols

The word protocol has a number of definitions, based on the context of its use, but in general protocols are rules of communication. In diplomacy, for example, a protocol can mean an agreement incorporating the results of a particular stage of a negotiation. For two or more people to communicate, they need to use a common language, such as English. The language is the protocol, or series of constructs, that enables people to form words from sounds, and then use words to create sentences. If constructed correctly the sentences create some meaning, as defined by the protocol. In the area of computer communications, a *protocol* is a formal set of rules that describe how computers transmit data and communicate across a network. The protocol defines the message format and the rules for exchanging the messages. This allows a computer to receive a series of 1s and 0s and to be able to interpret them into something meaningful.

Because of the complexity and multiple functions required to initiate, establish, conduct, and terminate communications among computers on a network, these functions are divided into manageable, individual layers. This decomposition is known as a *layered architecture*.

In a layered architecture, the protocols are arranged in a stack of layers in which data is passed from the highest layer to the lowest layer to effect a transmission. The process is reversed at the receiving end of the transmission, and the data is passed from the bottom of the stack to the top of the stack. Each layer in a protocol stack receives a service from the layer below and provides a service to the layer above.

The protocols and standards supported in each of the layers perform specific functions and attach information to the data (known as a header) as it passes through a particular layer. Thus, on the transmitting end, the data packet traverses the stack from the highest level to the lowest level, and each layer adds information as the data passes through. This process is called *data encapsulation*.

At the receiving computer, the process is reversed and the successive layers of information are stripped as the packet traverses the stack up to the highest layer. Each protocol detaches and examines only the data that was attached by its protocol counterpart at the transmitting computer.

The layers in the model range from providing application-oriented processes at the highest level to the generation of electrical or optical signals that are injected into the transmission medium, such as wires, optical fiber, or through the air (i.e., wireless), in the bottom layer. The intermediate layers perform additional functions, including setting up the communications session, transferring data, and detecting errors.

Two main protocol stacks are in use today: the OSI model and the TCP/IP model. When describing or talking about the layers in a protocol stack, the OSI model is always used. For example, layer 3 in the OSI model is called the IP (Internet Protocol) layer because this is the layer that uses the IP header for routing. While OSI is used to describe the various functions being performed in a network, the TCP/IP protocol stack is what is actually used in implementing the Internet protocols. For example, the Internet is known as a TCP/IP network because TCP/IP compromises the various protocols that are used across the global network.

# The Open Systems Interconnect Model

The International Standards Organization (ISO) developed the Open Systems Interconnect (OSI) model, circa 1981. The OSI model comprises seven functional layers, which provide the basis for communication among computers over networks.

The seven layers of the OSI model, from highest to lowest, are Application, Presentation, Session, Transport, Network, Data Link, and Physical (you can easily remember them using the mnemonic phrase **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing). [Table 15-1](ch15.html#iso_osi_seven-layer_model) lists these layers, their general functions, and corresponding protocols, services, or standards.

**Table 15.1. ISO OSI Seven-Layer Model**

| Layer | Function | Protocols or Standards |
| --- | --- | --- |
| Layer 7: Application | Provides services such as e-mail, file transfers, and file servers | HTTP, FTP, TFTP, DNS, SMTP, SFTP, SNMP, RLogin, BootP, MIME |
| Layer 6: Presentation | Provides encryption, code conversion, and data formatting | MPEG, JPEG, TIFF |
| Layer 5: Session | Negotiates and establishes a connection with another computer | SQL, X- Window, ASP, DNA SCP, NFS, RPC |
| Layer 4: Transport | Supports end-to-end delivery of data | TCP, UDP, SPX |
| Layer 3: Network | Performs packet routing across networks | IP, OSPF, ICMP, RIP, ARP, RARP |
| Layer 2: Data link | Provides error checking, and transfer of message frames | Ethernet, Token Ring, 802.11 |
| Layer 1: Physical | Interfaces with transmission medium and sends data over the network | EIA RS-232, EIA RS-449, IEEE 802 |

# The OSI Layers

The following sections discuss each of the OSI layers in turn, explaining their individual functions and the protocols they employ.

## The Application layer

Layer 7, the Application layer, is the interface to the user and provides services that deal with the communication portion of an application. It identifies the desired recipient of the communication and ensures that the recipient is available for a transmission session. Protocols associated with the Application layer include the following:

- **File Transfer Protocol (FTP)**—Provides for authenticated transfer of files between two computers and access to directories.
- **Trivial File Transfer Protocol (TFTP)**—Reduced version of FTP; does not provide authentication or accessing of directories.
- **Domain Name Service (DNS)**—A distributed database system that matches host names to IP addresses and vice versa. A popular DNS implementation is the Berkeley Internet Name Domain (BIND).
- **Simple Mail Transfer Protocol (SMTP)**—Supports the transmission and reception of e-mail.
- **Secure File Transfer Protocol (SFTP)**—A protocol that is replacing FTP. It provides increased security because it includes strong encryption and authentication. SFTP is a client that is similar to FTP and uses SSH or SSH-2 to provide secure file transfer.
- **Simple Network Management Protocol (SNMP)**—Supports the exchange of management information among network devices through a management entity that polls these devices. It is a tool for network administrators used to manage the network and detect problem areas.
- **Remote login (Rlogin)**—A command in UNIX that begins a terminal session between an authorized user and a remote host on a network. The user can perform all functions as if he or she were actually at the remote host. Rlogin is similar to the Telnet command.
- **Multipurpose Internet Mail Extensions (MIME)**—Enables the use of non–US-ASCII textual messages, nontextual messages, multipart message bodies, and non–US-ASCII information in message headers in Internet mail.

## The Presentation layer

Layer 6, the Presentation layer, is so named because it presents information to the Application layer. It puts information in a unified format so computers that represent data differently can still communicate. Layer 6 performs encryption, decryption, compression, and decompression functions, as well as translating codes such as Extended Binary-Coded Decimal Interchange Code (EBCDIC) or American Standard Code for Information Interchange (ASCII). Standards associated with Layer 6 include the following:

- **Motion Picture Experts Group (MPEG)**—The Motion Picture Experts Group's standard for the compression and coding of motion video.
- **Joint Photographic Experts Group (JPEG)**—Standard for graphics defined by the Joint Photographic Experts Group.
- **Tagged Image File Format (TIFF)**—A public domain raster file graphics format. It does not handle vector graphics. TIFF is platform independent and was designed for use with printers and scanners.

## The Session layer

Layer 5, the Session layer, provides services to Layer 4, the Transport layer, to support applications. It sets up the lines of communication with other computers, manages the dialogue among computers, synchronizes the communications between the transmitting and receiving entities, formats the message data, and manages the communication session in general. Even though networks are traditional packet switched networks, the session layer allows applications to behave as if they are going over a circuit switched network.

The functions of Layer 5 are summarized as follows:

- Establishing the connection
- Transferring data
- Releasing the connection

Session layer protocols include the following:

- **Structured Query Language (SQL)**—An application that supports multiple queries to the SQL database. SQL is a standardized language for obtaining information from a database. When applied to the Internet, it enables multiple users to log in to the Internet simultaneously.
- **X-Window System**—Supports developing graphical user interface applications.
- **Appletalk Session Protocol (ASP)**—Used to set up a session between an ASP server application and an ASP workstation application or process.
- **Digital Network Architecture Session Control Protocol (DNA SCP)**—A layered network architecture developed by Digital Equipment Corporation (DEC). DNA supports a number of protocols, including the Session Control Protocol. SCP translates names to addresses, sets up logical links, receives logical-link requests from end devices, accepts or rejects logical-link requests, and terminates logical links.
- **Network File System (NFS)**—Supports the sharing of files among different types of file systems.
- **Remote Procedure Call (RPC)**—Supports procedure calls where the called procedure and the calling procedure may be on different systems communicating through a network. RPC is useful in setting up distributed, client-server-based applications.

## The Transport layer

Layer 4, the Transport layer, maintains the control and integrity of a communications session. It delineates the addressing of devices on the network, describes how to make internode connections, and manages the networking of messages. In essence, the transport layer interfaces and prepares the application data to be sent across the network. The Transport layer also reassembles data from higher-layer applications and establishes the logical connection between the sending and receiving hosts on the network. The protocols of the Transport layer are as follows:

- **Transmission Control protocol (TCP)**—A highly reliable, connection-oriented protocol used in communications between hosts in packet-switched computer networks or interconnected networks. It guarantees the delivery of packets and that the packets will be delivered in the same order as they were sent. There is an overhead associated with sending packets with TCP because of the tasks it has to perform to ensure reliable communications.
- **User Datagram Protocol (UDP)**—UDP is not guaranteed delivery in that it transmits packets on a best effort basis. This is sometimes referred to as "send and pray" because there is no guarantee that the information will arrive. As a result, there is also no connection setup required, which reduces the overhead. It does not provide for error correction or for the correct transmission and reception sequencing of packets. In most cases TCP is preferred because having a guarantee that the information arrived is a good thing. So most protocols use TCP not UDP. However, there are three cases in which UDP is preferred:**Real time communication**—With real time audio and video, it does not make sense to retransmit a lost packet 10 seconds later because that point in the conversation has come and gone.**Repetitive information**—For example with network time protocol (NTP), the information is sent on a regular basis so if one packet is lost it has minimal impact on the application.**Excessive overhead**—Because TCP has an overhead associated with it, in some cases this extra transmission of information could cause performance issues on the network.
- **Sequenced Packet Exchange (SPX)**—A protocol maintained by Novell, Inc. that provides a reliable, connection-oriented transport service. It uses the Internetwork Packet Exchange (IPX) protocol to transmit and receive packets.

## The Network layer

Layer 3, the Network layer, sets up logical paths or virtual circuits for transmitting data packets from a source network to a destination network. It performs the following functions:

- Switching and routing
- Forwarding
- Addressing
- Error detection
- Node traffic control

The Network layer protocols include the following:

- **The Internet Protocol (IP)**—Provides a best effort or unreliable service for connecting computers to form a computer network. It does not guarantee packet delivery. A computer on the network is assigned a unique IP address. The transmitted data packets contain the IP addresses of the sending and receiving computers on the network, in addition to other control data. The data packets or *datagrams* traverse networks through the use of intermediate routers that check the IP address of the destination device and forward the datagrams to other routers until the destination computer is found. Routers calculate the optimum path for data packets to reach their destination.
- **Open Shortest Path First (OSPF)**—OSPF is a routing protocol that routers use to exchange information on how they are connected together. This information is used to determine how to route a packet across a network. A shortest path first (SPF) protocol selects the least-cost path from a source computer to a destination computer.
- **Internet Control Message Protocol (ICMP)**—A client server application protocol used to identify problems with the successful delivery of packets within an IP network. It can verify that routers are properly routing packets to the destination computer. A useful ICMP utility is the PING command, which can check if computers on a network are physically connected.
- **Routing Information Protocol (RIP)**—RIP is also a routing protocol but it is not as popular or in widespread use because it is not as efficient as OSPF. It sends routing update messages to other network routers at regular intervals and when the network topology changes. This updating ensures the RIP routers select the least-cost path to a specified IP address destination.
- Routers are often called Layer 3 devices because they open each packet to Layer 3 and use this information to determine the path a packet should take to traverse the network.

## The Data Link layer

Layer 2, the Data Link layer, encodes the data packets to be sent into bits for transmission by the Physical layer. Conversely, the data packets are decoded at Layer 2 of the receiving computer. Layer 2 also performs flow control, protocol management, and Physical layer error checking. It is also the layer that implements bridging.

The Data Link layer is divided into sublayers: the Media Access layer and the Logical Link layer.

The Media Access layer performs the following functions:

- Supports the network computer's access to packet data
- Controls the network computer's permission to transmit packet data

The Logical Link layer performs the following functions:

- Sets up the communication link between entities on a physical channel
- Converts data to be sent into bits for transmission
- Formats the data to be transmitted into frames
- Adds a header to the data that indicates the source and destination IP addresses
- Defines the network access protocol for data transmission and reception
- Controls error checking and frame synchronization
- Supports Ethernet and Token Ring operations

Data Link layer protocols include the following:

- **Address Resolution Protocol (ARP)**—A protocol that maps IP network addresses to the hardware Media Access Control (MAC) addresses used by a data link protocol. Every computer is assigned a unique MAC address by the manufacturer. A MAC address comprises a 6-byte, 12-digit hexadecimal number. The first 3 bytes of a MAC address identify the manufacturer. For example, the hex number 00AA00 would indicate that Intel is the manufacturer. The ARP protocol functions as a portion of the interface between the OSI network and link layers. The remaining 3 bytes represent the serial number of the device.
- **Reverse Address Resolution Protocol (RARP)**—A protocol that enables a computer in a local area network (LAN) to determine its IP address based on its MAC address. RARP is applicable to Token Ring, Ethernet, and Fiber Distributed-Data Interface LANs.
- **Serial Line Internet Protocol (SLIP)**—A protocol that defines a sequence of characters that frame IP packets on a serial line. It is used for point-to-point serial connections running TCP/IP, such as dial-up or dedicated serial lines.
- **Point-to-Point Protocol (PPP)**—A protocol that supports a variety of other protocols for transmitting data over point-to-point links. It does this by encapsulating the datagrams of other protocols. PPP was designed as a replacement for SLIP in sending information using synchronous modems. IP, IPX, and DECnet protocols can operate under PPP. Some subprotocols and terms of PPP used in accomplishing its functions are as follows:**Link Control Protocol**—A protocol that detects loopback links, accommodates limits on packet sizes, sets up encapsulation options, and optionally performs peer-to-peer authentication.**Network Control Protocol**—A protocol for configuring, managing, and testing data links.**Maximum Transmission Unit (MTU)**—A limitation on the maximum number of bytes of data in one transmission unit, such as a packet. Ethernet, for example, specifies an MTU of 1,516 bytes.

## The Physical layer

Layer 1, the Physical layer, transmits data bits through the network in the form of light pulses, electrical signals, or radio waves. It includes the necessary software and hardware to accomplish this task, including appropriate cards and cabling, such as twisted pair or coaxial cables. In addition to electronic interfaces, the Physical layer is also concerned with mechanical issues such as cable connectors and cable length. Standard Physical layer interfaces include Ethernet, FDDI, Token Ring, X.21, EIA RS-232, and RS-449. This level is addressed in the family of IEEE 802 LAN/WAN standards, which include the following areas:

- **802.1**—Internetworking
- **802.2**—Logical Link Control
- **802.3**—Ethernet (CSMA/CD)
- **802.3u**—Fast Ethernet
- **802.3z**—Gigabit Ethernet
- **802.3ae**—10 Gigabit Ethernet
- **802.4**—Token Bus
- **802.5**—Token Ring
- **802.7**—Broadband Technology
- **802.8**—Fiber Optic Technology
- **802.9**—Voice/Data Integration (IsoEnet)
- **802.10**—LAN Security
- **802.11**—Wireless Networking
- **802.15**—Wireless Personal Area Network
- **802.16**—Wireless Metropolitan Area Networks

# The TCP/IP Model

The Transmission Control Protocol (TCP) and Internet Protocol (IP) were developed in the 1970s, prior to the ISO OSI model. TCP and IP are part of a layered protocol model that is similar, but not identical to the OSI model. While not the same, there is a direct mapping between the functionality of OSI and the protocols of TCP/IP. The goal of TCP/IP was to enable different types of computers on different geographical networks to communicate reliably, even if portions of the connecting links were disabled. TCP/IP grew out of research by the U.S. Department of Defense (DoD) to develop systems that could communicate in battlefield environments where communication links were likely to be destroyed. The solution was to send messages in the form of packets that could be routed around broken connections and reassembled at the receiving end. TCP/IP provides this functionality through programs called *sockets* used to access the TCP/IP protocol services.

In the TCP/IP model, TCP verifies the correct delivery of data and provides error detection capabilities. If an error is detected, TCP effects the retransmission of the data until a valid packet is received. This function is based on an acknowledgment that should be sent back to the transmitting computer upon the receipt of delivered packets. If a packet is not acknowledged, the originating computer resends it. The receiving computer then organizes the received packets into their proper order.

The IP portion of TCP/IP is responsible for sending packets from node to node on the network until it reaches its final destination. It routes the information from a computer to an organization's enterprise network, and from there, to a regional network and, finally, the Internet.

The routing is accomplished through an IP address that is assigned to every computer on the Internet. This IP address is the four-byte destination IP address that is included in every packet. It is usually represented in decimal form as octets of numbers from 0 to 255, such as 160.192.226.135. For example, 255.255.255.255 is used to broadcast to all hosts on the local network. An IP address is divided into a portion that identifies a network and another portion that identifies the host or node on a network. Additionally, a network is assigned to a Class from A through E and this class representation further delineates which part of the address refers to the network and which part refers to the node. Classes A through C are the commonly used categories. The network classes and their corresponding addresses are given in [Table 15-2](ch15.html#ip_address_network_classes). IP and the details behind the addresses will be discussed in more detail later in the chapter.

**Table 15.2. IP Address Network Classes**

| Class | Network Address | Host Address | Example Address |
| --- | --- | --- | --- |
| Class A Address range = 1.0.0.1 to 126.255.255.254 | First 8 bits define network address. Binary address always begins with 0; therefore, the decimal address ranges from 1 to 126. (127 networks) | Remaining 24 bits define host address. (16 million hosts) | 110.160.212.156 Network = 110 Host = 160.212.156 |
| Class B Address range = 128.1.0.1 to 191.255.255.254 | First 16 bits define network address. Binary address always begins with 10; therefore, the decimal address ranges from 128 to 191. (127 is reserved for loopback testing on local host.) (16,000 networks) | Remaining 16 bits define host address. (65,000 hosts) | 168.110.226.155 Network = 168.110 Host = 226.155 |
| Class C Address range = 192.0.1.1 to 223.255.254.254 | First 24 bits define network address. Binary address always begins with 110; therefore, the decimal address ranges from 192 to 223. (2 million networks) | Remaining 8 bits define host address. (254 hosts) | 200.160.198.156 Network = 200.160.198 Host = 156 |
| Class D Address range = 224.0.0.0 to 239.255.255.255 | Binary address always begins with 1110; therefore, the decimal address ranges from 224 to 239. | Reserved for multicasting |  |
| Class E Address range = 240.0.0.0 to 254.255.255.254 | Binary addresses start with 1111; therefore, the decimal number can be anywhere from 240 to 255. | Reserved for experimental purposes |  |

# TCP/IP Model Layers

The TCP/IP model comprises four layers: the Application layer, the Host-to-Host layer or Transport layer, the Internet layer, and the Network Access layer. These layers and their corresponding functions and protocols are summarized in [Table 15-3](ch15.html#tcp_solidus_ip_model_layers-035).

As with the OSI model, encapsulation occurs as data traverses the layers from the Application layer to the Network Access layer at the transmitting node. This process is reversed in the receiving node. Encapsulation in TCP/IP is illustrated in [Figure 15-1](ch15.html#tcp_solidus_ip_encapsulation).

**Table 15.3. TCP/IP Model Layers**

| Layer | Function | Protocols or Standards |
| --- | --- | --- |
| Layer 4: Application | Equivalent to Application, Presentation, and Session layers of the OSI model. In TCP/IP, an application is a process that is above the Transport layer. Applications communicate through sockets and ports. | SMTP, POP, HTTP, FTP |
| Layer 3: Host-to-Host or Transport Layer | Similar to the OSI Transport layer; performs packet sequencing, supports reliable end-to-end communications, ensures data integrity, and provides for error-free data delivery. | TCP, UDP |
| Layer 2: Internet Layer | Isolates the upper-layer protocols from the details of the underlying network and manages the connections across the network. Uses protocols that provide for logical transmission of packets over a network and controls communications among hosts; assigns IP addresses to network nodes. | IP, ICMP |
| Layer 1: Network Access Layer | Combines the Data Link layer and Physical layer functions of the OSI model. These functions include mapping IP addresses to MAC addresses, using software drivers, and encapsulation of IP datagrams into frames to be transmitted by the network. It is also concerned with communications hardware and software, connectors, voltage levels, and cabling. | ARP, RARP, EIA RS-232, EIA RS-449, IEEE 802 |

The example protocols listed in [Table 15-3](ch15.html#tcp_solidus_ip_model_layers-035) have been discussed under the OSI model, except for the Post Office Protocol version 3 (POP3). Using POP3, an e-mail client can retrieve e-mail from a mail server. POP3 can be used with or without SMTP. A security issue with POP3 is that the password used for authentication is transmitted in the clear.

![TCP/IP encapsulation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1501.png)

**Figure 15.1. TCP/IP encapsulation**

The following are the core protocols that are used on TCP/IP networks and the OSI layers they operate at:

- **Layer 2**—Ethernet, Token Ring and 802.11
- **Layer 3**—IP and ICMP
- **Layer 4**—TCP and UDP
- **Layer 7**—SSH, DNS, HTTP, SSL, and so on

### Note

Whenever I talk about layers in the protocols (even TCP/IP) I always use the layers in the seven-layer OSI model to describe them.

# Internet Protocol

Today's Internet (IPv4) was developed in the 1970s, starting out as a robust technology for government contractors to connect to the U.S. Department of Defense (DoD). The Internet originated in the Advanced Research Projects Agency Network (ARPANET) as a standardized way for computers to communicate over the ARPANET network. Through open collaboration, the project saw expanded use in collaborate research amongst universities and government research facilities in the 1980s. Although slow to adopt commercially, the Internet has been growing exponentially since 1990, as more organizations enter cyberspace to facilitate business, research, and education. Not only are there more computers using up IP addresses, but there are also many more applications on the Internet than the original inventors ever could have imagined. The Internet is no longer a network of computers, but rather a single converged network of many kinds of devices, from everyday appliances to cell phones and media applications such as IPTV. The downside to this phenomenal success is that the Internet faces a serious shortage of IP addresses. In the early 1990s, people predicted that the last Class B IP address would be allocated in March 1994, a month dubbed the Date of Doom. Although researchers developed interim solutions to postpone the Date of Doom, today it's happening all over again: All current IP addresses will be depleted sometime between now and 2012, if the current rate of Internet growth continues (and predictions are correct).

## History of the Internet Protocol

The Internet has it roots with ARPANET, which connected government contractors for the U.S. Department of Defense (DoD). The research for ARPANET began in 1968. Researchers developed IP to standardize communication protocols in ARPANET network. Its developers assumed ARPANET would have fewer than several dozen networks of computers. They selected an address-space size of 32 bits. The first 8 bits represented the network (8 bits can identify 28, or 256 networks), and the remaining 24 bits represented the host. As ARPANET grew, its developers realized it would have more than 256 networks, so they separated the 32-bit address space into three classes: Class A, for large networks; Class B, for midsized networks; and Class C, for small networks. The flaw in this classification system is that it does not accommodate the needs of a large number of networks that fall between Class B and Class C. This single oversight caused the IP shortage scares in the 1990s, and even today.

IPv4's Class A 32-bit addresses begin with a 0 bit, followed by a 7-bit identifier (1–127) and a 24-bit host identifier. Thus, Class A addresses can identify 27, or 128, networks, each of which can have at most 224, or 16,777,216, hosts. Class B 32-bit addresses begin with the bits 1 0 (128.0.*x.x*–191.255.*x.x*), followed by a 14-bit network identifier and a 16-bit host identifier. Class B addresses can identify 214, or 16,384, networks, each with at most 216, or 65,536, hosts. Class C 32-bit addresses begin with the bits 1 1 0, followed by a 21-bit network identifier and an 8-bit host identifier. Class C addresses can identify 221, or 2,097,152, networks, each with at most 28, or 256, hosts. As you can see, there's a big difference between the number of hosts Class B addresses can handle compared with Class C addresses. Organizations that had or expected to have more than 256 hosts needed a Class B address, a very inefficient allocation of IP addresses. By 1992, the InterNIC had assigned about half of the available Class B addresses, and industry analysts projected the Date of Doom from the existing address-assignment rates.

## CIDR

Classless interdomain routing (CIDR) is an immediate solution to IP shortage. The idea behind CIDR is to give a block of contiguous Class C addresses, rather than a Class B address, to a company that has more than 256 but fewer than several thousand hosts. If a site needs, say, 1,000 addresses, it is given a block of 1,024 addresses (2nboundary) and not a full Class B address. In addition to using blocks of contiguous Class C networks, the allocation rules for the Class C addresses were also changed in RFC1519. The world is divided into the following four zones; each is given a portion of the Class C address space:

- 194.0.0.0–195.255.255.255 Europe
- 198.0.0.0–199.255.255.255 North America
- 200.0.0.0–201.255.255.255 Central and South America
- 202.0.0.0–203.255.255.255 Asia & the Pacific

This way each region has about 32 million addresses to allocate with 320 million Class C addresses from 204.0.0.0 to 223.255.255.255 held in reserve for the future. By using Class C addresses in this way, CIDR saved Class B addresses from depletion. Unfortunately, CIDR has not solved all problems associated IPv4 and the modern use of it. The InterNIC will allocate all IPv4 addresses within the next three to five years, according to current projections.

### Note

The hidden benefit of this IP address scheme is that you can determine where in the world the packet is coming from.

## NAT

Another well adopted proposal that is delaying IPv4 address exhaustion: network address translation (NAT). NAT was born from firewall technology. A company may allocate private non-external-routable IP addresses on its internal network using NAT techniques. NAT maps to a valid IP address once the traffic traverses the external network. As a result, NAT enhances its network security by hiding its internal IP addresses from the external network. Because a company wants to hide all of it machines behind a firewall anyway, using NAT, a company doesn't need globally unique or legitimate addresses for its private network. When NAT sits on the border between a company's network and the Internet, NAT maps the company's private IP address space to a small pool of globally unique addresses. However, in many cases, it is just a single IP address. Because acquiring a Class A or B address is difficult, many large companies use the private addresses that NAT creates for their internal networks. Using NAT does have a negligible drawback—NAT degrades performance in network throughputs. If the Internet were to only consist of computer networks, NAT would be a true solution for addressing problems. However, the convergence of all kinds of devices from cell phones (future) to VoIP to IPTV to online gaming boxes to many other Internet appliances with addressable IPs, means that NAT alone is not capable of solving those problems.

Because the designers of the Internet knew there would not be enough addresses for everyone to have a public address, they created the following three private addresses that anyone can use:

- **Class A**—10.0.0.0–10.255.255.255
- **Class B**—172.16.0.0–172.31.255.255
- **Class C**—192.168.0.0–192.168.255.255

The Internet Engineering Task Force (IETF) foresaw the diminishing IP address problem and other problems related to IP version 4 (IPv4) in the early 1990s. To address these problems, the IETF developed IP next generation (IPng), and in January 1995 published "The Recommendation for the IP Next Generation Protocol" in its Request for Comments (RFC) 1752. In addition to its 128-bit address space, which will solve the address-exhaustion problem, IPv6 uses a hierarchical address scheme, an efficient IP header (simplification of fields in IPv4), Quality of Service (QoS), host address autoconfiguration, authentication, and encryption. Knowing the importance of a migration path, IETF also proposes the migration strategy during the transition period, estimated to be about a decade.

Other less well-known drafts were also proposed after IPv6 was adopted as the next generation standard; the proposals mainly are IPv7 and IPv8. Although not officially recognized, it is interesting to look at its approach to solving the problem of IPv4.

## IPv6 solution

IPv6 overcomes the address space problem in IPv4 by defining a 128-bit address space. This address space is long enough to uniquely address every atom on earth. This alone allows for inefficient allocation without fear of the depletion scenario of IPv4. An IPv6 address contains eight sections separated by colons. Each section contains 16 bits expressed in four hexadecimal numbers. In addition to its 128-bit address space, IPv6 designates a hierarchical address for point-to-point communication. IPv6 calls this type of address an aggregatable global unicast address. IPv6 partitions this address into the hierarchical format shown in [Figure 15-2](ch15.html#ipv6_hierarchical_format).

![IPv6 hierarchical format](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1502.png)

**Figure 15.2. IPv6 hierarchical format**

The number at the beginning of the address is a format prefix that differentiates the aggregatable global unicast address from other types of addresses. At the top of the address hierarchy are top-level aggregators (TLAs). TLAs are public network access points (NAPs) that connect long-distance service providers and telephone companies. International Internet registries, such as Internet Assigned Numbers Authority (IANA) allocate addresses to TLAs. In turn, TLAs assign addresses to the next level in the aggregatable global unicast address hierarchy, the next level aggregator (NLA). NLAs are large Internet service providers (ISPs). An NLA allocates addresses to the next level in the aggregatable global unicast address hierarchy, the site level aggregator (SLA). An SLA, which is often called a subscriber, can be an organization such as a university or a small ISP. SLAs can assign addresses to their subscribers. In general, SLAs provide subscribers with a block of contiguous addresses so that organizations can create their address hierarchy to identify different subnets. The last level of the aggregatable global unicast address is the host interface ID, which identifies one host interface. Organizations assign host interface IDs by using a unique number on the subnet, or they can use the host's NIC (network interface card) ID (i.e., the media access control address MAC). This idea by itself raises privacy concerns because the NIC identifier is exposed over the Internet.

Currently, the routing table of an Internet backbone router contains tens of thousands of entries that it uses to look up the path to a destination network. Routing tables keep growing, but a large routing table degrades a router's performance and can cause routing instabilities. The design of the aggregatable global unicast address can reduce a routing table's size by route aggregation or summarization. For example, with aggregatable global unicast addressing, a U.S. backbone router needs only one entry (i.e., TLA) in its routing table for all networks in the UK. When the router receives a packet addressed to a network in the UK, it uses the TLA ID in the packet's destination address to find the path to the UK TLA in its routing table; then the router forwards the packet to the UK TLA. The UK TLA examines the NLA ID in the packet's destination address to determine the routing path to the NLA and sends the packet to the NLA. Finally, the NLA delivers the packet to its destination network according to the SLA ID in the destination address. This efficient global routing hierarchy operates similarly to the public telephone network (i.e. country codes, area codes and local exchange identifiers).

The aggregatable global unicast address is only a part of IPv6 address space. IPv6 defines three types of addresses: unicast, multicast, and anycast. Unicast traffic is the most common traffic on the Internet (a unicast address specifies one recipient). The aggregatable global unicast address is well designed for this point-to-point communication. IPv6 also defines two special unicast addresses for intranets. The first is the link local unicast address, and the second is the site local unicast address. The link local unicast address will let packets traverse on only one link or segment. Routers will not forward packets with link local unicast addresses. The site local unicast address is used to limit the packet delivery scope of the intranet. The edge router connecting the internal network to the external network will never forward packets with site local unicast addresses to the external network.

### IPv6 multicast

As in IPv4, IPv6 multicast addresses deliver packets from a single source to all recipient hosts in the multicast group. IPv6 supports two kinds of multicast addresses: permanent and transient. Permanent multicast addresses are well-known multicast addresses for special uses, such as for all routers in a local network. Transient multicast groups are used for on-demand applications such as an audio conference. The IPv6 multicast address contains a 112-bit multicast group ID, scoping can be specified, which can be node-local, link-local, site-local, or global. In IPv6, multicasting to all nodes in the network replaces the broadcasting capability in IPv4.

### IPv6 anycast

IPv6 introduces a third type of address, the anycast address. Anycast differs from multicast in that it delivers a message to any one of the nodes in a group rather than all. When one node, often the nearest node in the group, receives the message, anycast is finished. The application of this class of addressing is for a host to find the location of the nearest router/gateway or in the future Domain Name System (DNS). Currently, IPv6 limits anycast group members only to routers.

### IPv6 address autoconfiguration

In IPv4, a Dynamic Host Configuration Protocol (DHCP) server maintains a pool of IP addresses. A host can lease an address and obtain configuration information (such as a default gateway and DNS servers) from the DHCP server, which lets the host automatically configure its IP address. IPv6 inherits this autoconfiguration service from IPv4 and refers to it as *stateful* autoconfiguration.

In addition to stateful autoconfiguration, IPv6 introduces a *stateless* autoconfiguration service, which provides more flexible address management. In the stateless autoconfiguration process, a host first generates a link local unicast address by appending its 64-bit NIC ID to the link local address prefix 1111111010. (The Institute of Electrical and Electronics Engineers (IEEE) has changed the old NIC 48-bit globally unique ID (GUID) to a 64-bit GUID known as EUI-64. If the NIC ID is 48 bits, the NIC driver for IPv6 will convert the 48-bit NIC ID to a 64-bit ID according to an IEEE formula.) The host then sends a query, called *neighbor discovery*, to the same address to verify the uniqueness of the link local unicast address. If there is no response, the self-configured link local unicast address is unique. Otherwise, the host uses a randomly generated interface ID to form a new link local unicast address. Using this link local address as a source address, the host multicasts a request for configuration information, called *router solicitation*, to all routers on the local link. The routers respond to the request with a router advertisement that contains an aggregatable global unicast address prefix and other relevant configuration information. The host automatically configures its global address by appending its interface ID to the global address prefix it receives from the router. Now the host can communicate with any other host on the Internet.

### IPv6 transition

IETF recognized that it will be impossible for all systems on the Internet and corporate networks to upgrade from IPv4 to IPv6 at once. Mixed and heterogeneous IPv6 and IPv4 systems will need to coexist on the Internet for a long time. As part of the IPv6 development effort, IETF defined the processes that will drive the transition from IPv4 to IPv6, including three mechanisms: the IPv4-compatible IPv6 address, dual IP stacks, and IPv6 over IPv4 tunneling.

The IPv4-compatible IPv6 address is a special IPv6 unicast address that an IPv6 and an IPv4 node can use to communicate over an IPv4 network. This address has a prefix of 96 zero bits followed by a 32-bit IPv4 address. For example, if a node's IPv4 address is 192.56.1.1, its IPv4-compatible IPv6 address will be ::C038:101.

The dual IP stack mechanism implements both IPv6 and IPv4 stacks on one system, either a host or a router. Such a system, an IPv6 and IPv4 node, has both IPv6 and IPv4 addresses and can send and receive IPv6 and IPv4 packets.

Compared to the dual IP stack mechanism, IPv6 over IPv4 tunneling is a more complicated method. The tunneling mechanism encapsulates IPv6 data inside IPv4 packets to carry IPv6 data between an IPv6 node and an IPv4 node over existing IPv4 networks. Three steps are involved in the tunneling process: encapsulation, decapsulation, and tunnel management. In encapsulation, the tunnel entry point creates an IPv4 header, encapsulates the IPv6 packet in a new IPv4 packet, and transmits the packet. In decapsulation, the tunnel endpoint removes the IPv4 header, recovers the original IPv6 packet, and processes it. Finally, the tunnel entry point maintains the tunnel configuration information, such as the maximum transmission unit (MTU) size that the tunnel supports.

### IPv6 header

The newly simplified and enhanced header has the following fields (see [Figure 15-3](ch15.html#ipv6_simplified_header)):

- **Version**—4-bit-wide field that contains the hexadecimal value of 6 for IPv6
- **Priority**—Enables a source to identify the priority for this packet
- **Payload length**—Length of IP payload
- **Flow label**—Used for QoS functionality
- **Next header**—Type of header following IPv6 header
- **Hop limit**—Number of hops (TTL in IPv4)
- **Source Address**—128-bit source IP address
- **Destination Address**—128-bit destination IP address

![IPv6 simplified header](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1503.png)

**Figure 15.3. IPv6 simplified header**

Although the address fields are four times as long, the IPv6 header is only twice the size of the IPv4 header because the optimized IPv6 header eliminated IPv4 fields that are considered redundant or not useful. One such removed field that will tremendously increase the processing time of IPv6 as compared to IPv4 is the *header checksum* field. In today's routers the checksum needs to be recalculated for every packet traversing through the router because the TTL decrements. This alone will make IPv6 significantly faster than IPv4.

## IPv7 and IPv8 solutions

Shortly after the IPv6 was drafted, the IPv7 draft began circulating and was being touted as solving the IP shortage problem (although not many researchers took it seriously) by efficiently using the 32-bit addressing in the existing IPv4 addresses, keeping all other IPv4 protocol definitions intact. The plan is to redefine the IP classes altogether. The proposed definition is as follows:

- Class A-1—1-126 (126 networks and 2543 hosts)
- Class A-2—1-126 (1262 networks and 2542 hosts)
- Class A-3—1-126 (1263 networks and 254 hosts)
- Class B-1—128-191 (64 networks and 2543 hosts)
- Class B-2—128-191 (642 networks and 2542 hosts)
- Class B-3—128-191 (643 networks and 254 hosts)
- Class C-1—192-223 (32 networks and 2543 hosts)
- Class C-2—192-223 (322 networks and 2542 hosts)
- Class C-3—192-223 (323 networks and 254 hosts)
- Class D-1—224-239 (16 networks and 2543 hosts)
- Class D-2—224-239 (162 networks and 2542 hosts)
- Class D-3—224-239 (163 networks and 254 hosts)
- Class E-1—240-254 (15 networks and 2543 hosts)
- Class E-2—240-254 (152 networks and 2542 hosts)
- Class E-3—240-254 (153 networks and 254 hosts)

IPv7 introduces Supernetting, which is the aggregation of multiple divisions of an IP address class into one network, the same concept that CIDR uses to extend the life of IPv4. So in summary, IPv7 took what CIDR did and applied the concept to the full 32-bit IP address rather than just Class C.

IPv8 took on IPv7's IP definition and added a few new fields to the address, making it 48 bits long. The new fields are *IP S zone code* and *IP area code*, similar to the concepts proposed in IPv6 except it is taking up only 48 bits versus 128 bits.

In the end, both IPv7 and IPv8 were rejected by the IETF on grounds that IPv6 had already addressed all the problems and that IPv7/IPv8 only provided marginal improvement as compared to IPv6.

With the convergence revolution well underway requiring a single data network that is capable of handling voice, video, and data, and many other unique devices that will be connected today and tomorrow, the only logical choice for protocol, which has both the IETF and industry support, is IPv6. In many parts of Asia, IPv6 is already deployed, replacing the old network. IPv6 has already been built into many routers and into UNIX (Linux, BSD, and so on). The Internet backbone for IPv6 testing, 6bone, links 29 countries to develop IPv6 technologies. IPv6 will eventually arrive to replace the existing IP network. The motivation for change is not a technological one but rather the need to fill a void other protocols have not been able to fill. IPv6 is the long-term solution to building a reliable, manageable, secure, and high-performance Internet and IP network.

# VoIP

In the 1920s, twisted-pair copper wiring carried telephone service to homes across the country. More than 80 years later the system remains mostly unchanged. Copper and fiber optic lines carry analog voice (and data in the case of faxes) around the world over dedicated lines. The current phone system runs over the public switched telephone network (PSTN), also called POTS (plain old telephone service). These networks have evolved into high-reliability, high-quality systems that support such critical systems as 911 emergency services. When you pick up the phone, you expect it to work, no questions asked.

With the creation of the Internet in the mid 1980s, companies have spent billions of dollars on establishing a data network that far surpasses the phone systems. If those lines could be used to pass voice, it would eliminate the need for subscribers to pay for both phone and Internet service.

The Internet uses a packet-switched network. It breaks the data up into pieces and then sends it across the network, with multiple paths available to its destination. Voice over IP (VoIP) uses the packet transfer capability of the Internet to send its data more efficiently than a phone line can. It works by taking the caller's voice and converting it to a digital signal. It then treats this as data and sends it across the Internet to another user, recombines the packets, and plays the sound of the caller's voice.

While bandwidth is getting bigger and better all the time, VoIP requires a much higher level of quality and reliability than a normal data connection. If it takes an extra five seconds to load a Web page, that is not the same level of discomfort as a phone going dead for five seconds in the middle of a conversation. POTS users expect reliability when they pick up the phone that VoIP cannot always guarantee.

## Using VoIP

The interesting thing about VoIP is that there is not just one way to place a call. There are three different "flavors" of VoIP service in common use today:

### ATA

The simplest and most common way to place a call is through the use of a device called an ATA (analog telephone adaptor). The ATA allows you to connect a standard phone to your computer or your Internet connection for use with VoIP. The ATA is an analog-to-digital converter. It takes the analog signal from your traditional phone and converts it into digital data for transmission over the Internet. Providers such as Vonage and AT&T CallVantage are bundling ATAs free with their service. You simply crack the ATA out of the box, plug the cable from your phone that would normally go in the wall socket into the ATA, and you're ready to make VoIP calls. Some ATAs may ship with additional software that is loaded onto the host computer to configure it; but in any case, it is a very straightforward setup.

### IP phones

These specialized phones look just like normal phones with a handset, cradle, and buttons. But instead of having the standard RJ-11 phone connectors, IP phones have an RJ-45 Ethernet connector. IP phones connect directly to your router and have all the hardware and software necessary right onboard to handle the IP call. Wi-Fi IP phones are also available, allowing subscribing callers to make VoIP calls from any Wi-Fi hotspot.

### Computer to computer

This is certainly the easiest way to use VoIP. You don't even have to pay for long-distance calls. There are several companies offering free or very low-cost software that you can use for this type of VoIP. All you need is the software, a microphone, speakers, a sound card, and an Internet connection, preferably a fast one like you would get through a cable or DSL modem. Except for your normal monthly ISP fee, there is usually no charge for computer-to-computer calls, no matter the distance.

## The standard phone system: Circuit switching

Existing phone systems are driven by a very reliable but somewhat inefficient method for connecting calls called circuit switching.

Circuit switching is a very basic concept that has been used by telephone networks for more than 100 years. When a call is made between two parties, the connection is maintained for the duration of the call. Because you are connecting two points in both directions, the connection is called a circuit. This is the foundation of the Public Switched Telephone Network (PSTN).

Here's how a typical telephone call works:

1. You pick up the receiver and listen for a dial tone. This enables you to know that you have a connection to the local office of your telephone carrier.
2. You dial the number of the party you wish to talk to.
3. The call is routed through the switch at your local carrier to the party you are calling.
4. A connection is made between your telephone and the other party's line using several interconnected switches along the way.
5. The phone at the other end rings, and someone answers the call.
6. The connection opens the circuit.
7. You talk for a period of time and then hang up the receiver.
8. When you hang up, the circuit is closed, freeing your line and all the lines in between.

Let's say that you talk for 10 minutes. During this time, the circuit is continuously open between the two phones. In the early phone system, up until 1960 or so, every call had to have a dedicated wire stretching from one end of the call to the other for the duration of the call. So if you were in New York and you wanted to call Los Angeles, the switches between New York and Los Angeles would connect pieces of copper wire all the way across the United States. You would use all those pieces of wire just for your call for the full 10 minutes. You paid a lot for the call because you actually owned a 3,000-mile-long copper wire for 10 minutes.

Telephone conversations over today's traditional phone network are somewhat more efficient and they cost a lot less. Your voice is digitized, and your voice along with thousands of others can be combined onto a single fiber optic cable for much of the journey (there's still a dedicated piece of copper wire going into your house, though). These calls are transmitted at a fixed rate of 64 kilobits per second (Kbps) in each direction, for a total transmission rate of 128 Kbps. If you look at a typical phone conversation, much of this transmitted data is wasted.

While you are talking, the other party is listening, which means that only half of the connection is in use at any given time. Based on that, you can surmise that you could cut the file in half, down to about 4.7 MB, for efficiency. Plus, a significant amount of the time in most conversations is dead air—for seconds at a time, neither party is talking. If you could remove these silent intervals, the file would be even smaller. Then, instead of sending a continuous stream of bytes (both silent and noisy), what if we sent just the packets of noisy bytes when they were created? That is the basis of a packet-switched phone network, the alternative to circuit switching.

## VoIP uses packet switching

VoIP technology uses the Internet's packet-switching capabilities to provide phone service. VoIP has several advantages over circuit switching. For example, packet switching allows several telephone calls to occupy the amount of space occupied by only one in a circuit-switched network. Using PSTN, that 10-minute phone call we talked about earlier consumed 10 full minutes of transmission time at a cost of 128 Kbps. With VoIP, that same call may have occupied only 3.5 minutes of transmission time at a cost of 64 Kbps, leaving another 64 Kbps free for that 3.5 minutes, plus an additional 128 Kbps for the remaining 6.5 minutes. Based on this simple estimate, another three or four calls could easily fit into the space used by a single call under the conventional system. And this example doesn't even factor in the use of data compression, which further reduces the size of each call.

Let's say that you and your friend both have service through a VoIP provider. You both have your analog phones hooked up to the service-provided ATAs. Let's take another look at that typical telephone call, but this time using VoIP over a packet-switched network:

Here is how a VoIP call is made:

1. You pick up the receiver, which sends a signal to the ATA.
2. The ATA receives the signal and sends a dial tone. This lets you know that you have a connection to the Internet.
3. You dial the phone number of the party you wish to talk to. The tones are converted by the ATA into digital data and temporarily stored.
4. The phone number data is sent in the form of a request to your VoIP company's call processor. The call processor checks it to ensure that it is in a valid format. (The central call processor is a piece of hardware running a specialized database/mapping program called a soft switch.)
5. The call processor determines to whom to map the phone number. In mapping, the phone number is translated to an IP address. The soft switch connects the two devices on either end of the call. On the other end, a signal is sent to your friend's ATA, telling it to ask the connected phone to ring.
6. Once your friend picks up the phone, a session is established between your computer and your friend's computer. This means that each system knows to expect packets of data from the other system. In the middle, the normal Internet infrastructure handles the call as if it were e-mail or a Web page. Each system must use the same protocol to communicate. The systems implement two channels, one for each direction, as part of the session.
7. You talk for a period of time. During the conversation, your system and your friend's system transmit packets back and forth when there is data to be sent. The ATAs at each end translate these packets as they are received and convert them to the analog audio signal that you hear. Your ATA also keeps the circuit open between itself and your analog phone while it forwards packets to and from the IP host at the other end.
8. You finish talking and hang up the receiver.
9. When you hang up, the circuit is closed between your phone and the ATA.
10. The ATA sends a signal to the soft switch connecting the call, terminating the session. Probably one of the most compelling advantages of packet switching is that data networks already understand the technology. By migrating to this technology, telephone networks immediately gain the ability to communicate the way computers do.

## Deciding to use VoIP

Ethernet switch and router networks originally deployed in the 1990s were designed for data communications only and therefore were not ideal for handling real-time voice communications, where small changes in network characteristics can affect call quality. As a result, early adopters of VoIP faced new challenges when moving from traditional voice networks to IP networks. Issues such as transmission delay (including delays for encoding, decoding, and packetizing voice samples), network jitter, packet loss, and echo were found to seriously affect the Quality of Service (QoS) demands of real-time voice communications. In addition, a number of security issues have been identified that must be taken into consideration when implementing an IP telephony system.

The primary benefits of deploying an IP telephony system are:

- Cost savings and cost reduction
- System design and performance enhancements
- Ability to provide enhanced telecommunication features, functions, and applications

## Security issues

IP telephony systems and networks are vulnerable to the following security breaches:

- Access control
- Data control
- Disruption
- Eavesdropping

All servers, media gateways, gatekeepers, and IP voice terminals are susceptible to attack. There are a variety of IP telephony system security issues to be aware of. Security threats and resolutions include the following:

- Packet sniffing/call interception, resolved by using a switched LAN infrastructure to limit sniffing problems
- Virus and Trojan-horse applications, resolved by using host-based virus scanning software
- Unauthorized access, resolved by using host-based intrusion detection systems and application access control
- Application layer attacks, resolved by updating computer system software with the latest security fixes
- Caller identity spoofing, resolved by using software utilities that notify system administrators of unknown devices attached to network
- Toll fraud, resolved by using a system gatekeeper that denies network access to unknown phones attempting to log in
- Denial of service, resolved by segregating voice and data transport segments to reduce the likelihood of an attack
- Repudiation, resolved by authenticating users before they access a telephony device, thus reducing the likelihood of a later denial that a call ever occurred
- Trust exploitation, resolved by using a restrictive trust model and private VLANs to limit trust-based attacks

In addition to the techniques previously outlined, it is strongly recommended that you have media encryption integrated into the IP telephones and media gateways to prevent sniffing/eavesdropping of voice and signaling packets. Several encryption algorithms that are commonly used in these devices include: 3DES, AES, RC4, and RC5.

Whenever possible, endpoints with hardware acceleration for these functions are recommended over software implementations.

The challenges of securing a voice network may seem insurmountable, but in many cases much of the work may already be done. Voice over Internet Protocol, as its name implies, is a network service with many of the same security requirements demanded by a secure data infrastructure. An enterprise that has already done its due diligence may only need to address voice specific issues. Indeed, by re-examining the current infrastructure for voice security issues, existing data security is augmented. In any case, a multi-faceted security strategy will help ensure the availability of services, the successful introduction of new services, and the savings benefits of a fully converged infrastructure.

## Risk factors

A convergent network is one that has data and voice traveling through the same network devices. Some standard IP-related issues will have to be addressed.

Monitoring is the act or intercepting (but not necessarily interrupting) IP traffic. Monitoring VoIP is just as difficult, or easy, as monitoring data packets. All open source packet sniffers have plug-ins to interpret VoIP protocols. So while specialized hardware may be required when attempting to sniff a telephony network, a VoIP network is susceptible to all normal data sniffing methods. Encryption, when used, can decrease this risk, but is not always used.

Denial of service is a risk in all network environments. But because VoIP has to allow incoming as well as outgoing connections, there is an increased risk of a DoS attack. IDS can potentially reduce an attack from a single source, but blocking a distributed DoS attack then becomes an issue. The bigger problem with DoS is that both your data and your voice networks can go down if there is an attack.

Another kind of DoS attack for voice doesn't need to be as extreme as a DoS attack on data. The quality of service (QoS) required for a VoIP connection is much higher than for data. If a DoS attack slows mail down to a crawl, it may still eventually reach you, but if VoIP is slowed down, packets will begin to be discarded and retransmitted, even further complicating the situation.

## Network design

When designing a VoIP deployment, isolation is the name of the game. Data and voice should be on isolated and separate IP segments. The use of VLANs will facilitate the logical separation of data and voice. It is also one of the cheapest ways to maintain a high QoS for the voice segment. Using a VLAN can also help when data, voice and video are all coming from the same source, such as during live online multimedia presentations. VLANs also allow the network to perform MAC level security, only allowing registered devices to be used throughout the system. They will prevent rogue devices from connecting to the network. Then unneeded and unused ports should be disabled.

The use of non-routable addresses will prevent voice packets from going outside your network. The use of NATing within your voice network presents different issues. A call cannot be received by a NATed device without the use of some kind of redirector or proxy.

## Use of softphones vs. hardware phones

Soft phones use software that turns a desktop computer into a VoIP device. Because of the risk to the computer itself and the increased security required for VoIP, these devices provide an even greater risk than hardware phones. To isolate the voice segment, soft phone computers should be enabled with two NIC cards and configured to send all data out of the data side, and all VoIP over the second connection. This will prevent data and voice packets from traveling on non-native networks. Any soft phone host machines should be increasingly hardened to prevent OS vulnerabilities from being exploited. All hardware phones and soft phone software used should support VLAN functionality.

## Voice and data crossover requirements

Voicemail may be one enhancement to your VoIP system that may require connectivity between your data and voice networks.

Each VoIP connection requires four open ports: two for signaling and two for voice packets. VoIP traditionally uses any port above 1023 for its connections. By implementing Dynamic Port Mapping you can limit the upper bound of ports that VoIP can use. This should be implemented alongside a stateful firewall to allow connections to still traverse the network. All IP packets should be filtered at the firewall to prevent data packets from attacking the VoIP portion of the network. Firewalls that handle VoIP packets should be compartmentalized so that latency is not added to the connection because of excessive data packets.

The H.323 protocol may still have issues when WAN-to-WAN connections have higher ports. A special H323-aware firewall may be required to properly implement this kind of configuration.

## VoIP server environments

VoIP servers can be vendor-provided machines, or they can be built on top of Windows- or UNIX-based operating systems. All due considerations should be taken when using VoIP servers that use existing operating systems. These devices should be dedicated to provide VoIP services. All possible hardening should take place on servers in a VoIP environment. Extra services, protocols, and applications should be disabled. Remote administration should be discouraged. While this makes maintenance more convenient for administrators, the security risks are too great in most environments to allow access to VoIP configuration information from anywhere other than the console.

## VoIP protocols

VoIP protocols are broken down into two general categories: signaling protocols and media protocols. While signaling protocols are used for establishing and setting up the call, media protocols are used for taking the voice conversation and sending it across the network. While there are many proprietary protocols such as Skinny, the most common standards are SIP and H.323 for signaling protocols and RTP for media protocols.

### Session-Initiated Protocol

SIP is a call control protocol defined by the IETF. It was designed as a text-based protocol to send control messages for a VoIP network. SIP is a new protocol as far as protocols go, and with that, there are some things that need to be "enhanced" before its level of security is fully implemented for use in large-scale deployments.

Many SIP products allow for encryption and enhanced networking (using TCP instead of UDP) but they are not enabled by default. Because of the text-based nature of SIP, and weak encryption (when enabled), many kinds of attacks are possible—man in the middle attacks, proxy impersonation, denial of service, ARP poisoning.

The use of the UDP protocol to transmit data gives a connection less overhead because UDP is more streamlined than TCP. But this streamlining comes at a price of reliability and security. If an attacker is able to inject itself into the path of voice packets, by impersonating a user agent or voice proxy, then packets can be monitored, altered, recorded, manipulated, or dropped altogether. An increased vulnerability in VoIP is that because the QoS requirement is so high, a malicious user could actually flood all the proxy servers in a network except the one that has a sniffer attached to it and this would result in all the data being forced to go through that point.

### H.323

H.323 took the opposite approach of SIP. SIP was built specifically for voice and meant to be very lightweight. H.323 is a suite of protocols that is much more complex, which is one of the key disadvantages of it. However, one of the key benefits is that it is very feature rich, offering a lot of functionality to include a variety of security features.

While SIP seems to be winning on the signaling protocol side because of its simplicity, more and more organizations are enhancing their SIP implementation by using a variety of protocols from the H.323 suite.

# Summary

The ISO OSI seven-layer architecture encompasses the protocols required for reliable computer-to-computer communications. The earlier TCP/IP family of protocols is the basis for Internet and intranet communications and serve as a common standard for communication among a variety of platforms and operating systems.

The protocols that define the OSI and TCP/IP models provide a rich source of mechanisms for achieving effective and reliable digital communications.

The challenges of securing a voice network may seem insurmountable, but in many cases much of the work may already be done. Voice over Internet Protocol, as its name implies, is a network service with many of the same security requirements demanded by a secure data infrastructure. An enterprise that has already done its due diligence may need to address only voice-specific issues. Indeed, by re-examining the current infrastructure for voice security issues, existing data security is augmented. In any case, a multi-faceted security strategy will help ensure the availability of services, the successful introduction of new services, and the savings benefits of a fully converged infrastructure.
