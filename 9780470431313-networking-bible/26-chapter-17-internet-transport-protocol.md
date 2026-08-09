# Chapter 17. Internet Transport Protocol

**IN THIS CHAPTER**

- How data is transported on the Internet
- Factors that influence IP network performance
- What is contained in an IP packet
- How data flow is managed
- Connections and ports

Transmission Control Protocol (TCP) and Internet Protocol (IP) are the two protocols that give rise to the acronym TCP/IP. TCP/IP is a set of protocols or agreed standards that are used to send and manage communications on a packet switched network. TCP is the technology that establishes a virtual connection between systems, manages data transmission, and ensures that the data has been reliably transferred. The data that is contained in a packet is TCP data. The mechanism used to get packets to their destination is IP. The way TCP does what it does impacts the majority of Internet communications, as well as how applications are built; it also affects network performance. IP, which is discussed in [Chapter 18](ch18.html), is the method used to package data sent across a packet switched network and includes the methods for not only packaging data but for addressing as well.

TCP solves the problem of how to ensure reliable communications when the medium you transmit over is inherently unreliable. Packets may take different routes to get to their destination, arrive out of sequence, or be dropped entirely. TCP assembles the data by sequencing the packets, ensuring that all packets are valid, and requesting retransmission of any packet that is missing or damaged.

Devices connected over a TCP/IP network can have greatly different capabilities; for example, a PDA (personal data assistant) can be slow while a computer can be fast. TCP implements features such as flow control to vary the rate at which data is transferred and provides for multiplexing, which runs simultaneous processes to speed up performance. It can also alter the size of packets.

Not all communications require the overhead of reliable data transmission. When you send rapidly changing data such as voice or video, losing a frame doesn't dramatically impact quality. For those applications, the User Datagram Protocol, or UDP, is used. This chapter describes UDP and compares it to the TCP protocol.

# Transmission Control Protocol

The Transmission Control Protocol, or TCP, is the most widely used transport protocol on computer networks today. TCP provides control mechanisms that manage the data contained in the message, ensuring that the data is sent in manageable pieces, that it arrives intact, that the data can be sequenced, and that the reassembled data is a faithful copy of the data that was sent. TCP contains a set of control commands that can vary the amount of data transferred in individual packets, as well as the rate at which packets are sent. Among the applications that rely on TCP are browsers and Web servers, e-mail programs, and file transfer programs.

TCP was developed to solve the problem of reliable communications on an inherently unreliable network. When data must be sliced into IP packets and transmitted as a set of IP requests, there needs to be a mechanism to control IP data flow. TCP allows a program to issue a single send data command and then let TCP handle the details of the data transfer.

An IP packet consists of a data chunk composed of a header section followed by the body section. Encoded in the header are the details of what the packet destination is, any preferences for the route that the packet should take, the size of the data contained in the body portion, a checksum to ensure the validity of the data, and the position in the data sequence into which this packet's data should be placed. You can think of the header and associated IP content as metadata that describes the TCP data contained in the body.

The Internet was designed to be a highly redundant mesh structure that could survive any outages to a substantial portion of the network and still be operable. When data is sent from one system to another, the system doesn't ensure that packets will travel the same route, arrive in sequence, and all arrive correctly. As a matter of fact, packets can take multiple paths to their destination, arrive out of sequence, and be lost along the way.

TCP has a control language that creates a connection between two systems, sends messages that indicate what the next required packet in the sequence is, requests retransmission of packets when required, and acknowledges when the data has been successfully reassembled. On the sending side, TCP's internal timer resends the last required packets if an acknowledgment command isn't received by a certain time. All of the additional packets sent represent an overhead that the TCP system imposes and that can dramatically lower performance.

### Note

The TCP protocol was defined in RFC 793, "Transmission Control Protocol." RFC 768, "User Datagram Protocol," defines the use of UDP. An additional protocol, RFC 1122, entitled "Requirements for Internet Hosts—Communication Layers," contains details that outline the transport of both of these protocols.

TCP is designed to be a reliable means of data delivery, but it is not optimized for performance. When TCP is used, there can often be delays while packets are requested and resent, and those delays can run several seconds or more. You can get a sense for the round-trip time by performing a `TRACEROUTE` command to the system that is sending data. `TRACEROUTE` (`TRACERT` on Windows) is a command that sends packets to a destination and has all intermediate nodes send back messages indicating the path and time spent getting to the node to the original source.

TCP is implemented in any operating system that must run on a TCP/IP network, which today is almost any operating system that you would find on a user's desktop, as well as any connected server. Routers, gateways, and firewalls also implement TCP, as evidenced by their ability to respond to `PING` operations and to be inventoried and managed by SNMP (Simple Network Management Protocols) applications; also, in the case where their management console can be viewed in a browser, they support the HTTP browser protocol.

TCP is highly processor intensive, and in systems with large network I/O, such as Web servers and terminal servers, I/O can be the major performance bottleneck. There has been an effort over the last few years to develop specialized network interface adapters that contain ASICs (Application Specific Integrated Circuits) with a TCP engine built into them that takes the TCP processing load off of a system's CPU and processes it on the network interface card (NIC). These devices are called TCP Offload Engines (TOEs). Alacritech developed the first of these network adapters, and they may appear as specialized chips on motherboards in the years to come. At the moment, the technology is expensive and difficult to implement, but the results can be impressive. The addition of these cards to servers running at 80 percent or more CPU utilization can reduce this percentage to as little as single-digit utilization at the same load.

Not all data transmission requires reliability; some applications work perfectly fine when a large portion of their data arrives. Those applications work best when the data transfer rate is high. An example is streaming video. In a video application, it hardly matters if one frame of the movie drops out when there are 30 frames per second going by. However, if the data rate is high, then the movie can use a higher resolution, and that certainly matters to the viewer. Therefore, applications such as video streaming or Voice over IP (VoIP) tend to use special streaming protocols and use the User Datagram Protocol (UDP) in place of the TCP protocol. UDP is covered later in this chapter.

# Packet Structure

A TCP packet consists of a header with many sections and the body of TCP data with a variable size, as determined by the current value of the receive window. [Figure 17.1](ch17.html#the_packet_structure_of_a_tcp_packet_com) shows a schematic of a TCP packet. The receive window is a negotiated value that is used to prevent a TCP memory buffer overrun at the receiving system by signaling to the sender when to send data and when to delay sending data. This form of traffic management is described in more detail later in the chapter.

![The packet structure of a TCP packet, with all of the header sections shown](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1701.png)

**Figure 17.1. The packet structure of a TCP packet, with all of the header sections shown**

## Header fields

The first four fields in the header are the Source port, Destination port, Sequence number, and Acknowledgement number. Ports are similar to a TV channel in that they represent the type of data being sent or received. A port is described as transmitting outgoing data or listening for incoming data. When data arrives at port 8080, it is recognized as data meant for a proxy server such as Microsoft Internet Security and Acceleration (ISA) Server and is sequenced and sent to that application. Port 8080 is for Alternate HTTP. If data came in on port 110, then it would be recognized as being POP3 (Post Office Protocol 3) data, and when the data is sequenced it would be sent to your mail program. Ports are described in the "[Ports](ch17.html#ports)" section at the end of this chapter.

The Sequence number and Acknowledgement number are fields used for traffic control. If the Synchronize (SYN) flag is set to 1 (on), then the Sequence number field indicates that the number is the initial sequence number and is the start of the data. When the SYN flag is set to 0 (off), this sequence number is used to place the first byte of TCP data into the sequence that will be built. The Acknowledgment number indicates the next byte that the receiving system needs in the current sequence that it is building when the Acknowledgement (ACK) flag is set to 1 (on). This system allows the receiver to rebuild the data in the original order starting with the first, middle, and last fragments sequentially.

## Flags

The block that begins at bit offset 96 contains a number of flags that are used to determine the states of different fields and the purpose of the data. The Data Offset field at the end of the header ensures that whatever the size of the options below, the size of the TCP header is always the same; therefore, the Data Offset size is from 20 to 60 bytes. The Reserved block isn't defined and should be set to zero. What follows next is a set of eight 1-bit blocks called *Flags* or *Control bits*. Flags specify the following:

- **CWR**. Congestion Window Reduced is a flag that is set to 1 (on) when the sending system receives TCP data with the ECE flag set to 1.
- **ECE**. Echo (alternatively ECN) is set to 1 (on) when the system can perform an echo during a three-way handshake.
- **URG**. The Urgent bit is set to 1 (on) when the Urgent pointer field contains data that must be processed with priority before all other traffic.
- **ACK**. The Acknowledgement flag is set to 1 (on) when the Acknowledgement field value needs to be read.
- **PSH**. The Push flag tells TCP to send the data from this message to the Application layer immediately.
- **RST**. The Reset flag is set to 1 (on) to indicate that the connection should be reset.
- **SYN**. The Synchronize flag indicates that the Sequence number field is significant and needs to be processed.
- **FIN**. The Final flag is set to 1 (on) when there is no more data that will be sent by the sender.

## Checksum field

The Checksum field contains a value that is used to determine if the entire packet has arrived correctly at its destination, and includes checks on both the header and body of the data. The value of the checksum varies, depending upon whether the packet is transmitted over an IP version 4 or an IP version 6 network, although the TCP header format is the same for both versions.

To get the checksum in IP version 4, the complement of all of the 16-bit words in the packet are found and then summed to create a 16-bit word checksum. If the packet has an odd number of octets (words), then the last octet is padded with zeros to complete the 16-bit checksum word. At the receiving end, the checksum field is padded with zeros and then the complement arithmetic is performed again.

The details of checksums aren't particularly important in the general discussion in this chapter. If you are interested in the details, they are given in RFC 793 for IP version 4 and RFC 2460 for IP version 6. However, it is worth noting that the two checksum methods used are very weak compared to methods like cyclic redundancy checks (CRCs) that are used at the application level. Indeed, most applications apply more advanced data validity checks of their own.

## Control fields

As part of traffic control, the Window field specifies the size of the receive window. The size of the data block that is transferred isn't specified by TCP. It can be as small as a single byte or as large as a kilobyte, or anything in between. If a message has a size of 2048KB, then any combination of data block size that adds up to 2048KB may be used. The receiving system can set a value for the Window, based on how much room remains in the TCP memory buffer.

The Urgent pointer field is used when the Urgent (URG) flag is set to 1 (on). This field gives the offset from the sequence number for the last urgent data byte in an urgent sequence.

The Options block contains a number of different values that can be set, ranging from 0 to 8. They are as follows:

1. End of options list
2. No operation
3. Window scale
4. SACK, or Selective Acknowledgement
5. Data Offset (if required)
6. Data Offset (if required)
7. Data Offset (if required)
8. Data Offset (if required)
9. Timestamp

## Data field

The final block of data is the Data field. This is the TCP data portion of the packet and contains data in the form of an Application layer protocol. Any data format that can be sent over TCP can be used in the Data field, including HTTP, FTP, POP3, SMTP, and many others; but only one type of data may be sent in a packet, and it must be sent to the port that listens for that data type.

The Data field's size isn't a set value. It can be as small as a byte and as large as the maximum window size allows. TCP has a built-in mechanism that allows the Data field's size to be set as required by conditions as part of TCP's congestion control mechanism.

# Protocol Operation

TCP works by creating a connection between two systems or hosts. The connection is a virtual connection because, although the endpoints are known, the paths to the endpoints are not. An endpoint is defined by two parameters: the IP address and the port number.

To initiate a TCP transaction, a connection established by a three-way handshake is often used, as follows:

1. The sending host sends a synchronization or SYN request to the receiving host.
2. The receiving host then acknowledges the message by returning a SYN-ACK response to the sending host. An initial sequence number (ISN) for the first packet is exchanged between the two systems. That number is different with each connection.
3. The sending host then sends an ACK message to indicate that the connection has been established and that each endpoint is now an Internet socket.

Once the connection is established, data transfer can occur. A connection is defined by four parameters: the sending system's IP address, the sending port number, the receiving system's IP address, and the receiving system's port number. Because TCP supports multiplexing, a full description of the connection would include the transport protocol used to create a full-duplex description or full association:

```
(TCP, Send-IP, Send-Port, Receive-IP, Receive Port)
```

Connections can also be described in terms of their one-way relationship, which is called a half association, as follows:

```
(TCP, Send-IP, Send-Port)
```

one way, and

```
(TCP, Receive-IP, Receive Port)
```

in the opposite direction. The concept of a half association is really only valuable when different protocols are used. For example, if you click a link to download a file by FTP in your browser, your outgoing connection is HTTP and sent over port 80, while the incoming file is sent by FTP over port 21.

Active data transfer is characterized by the following actions:

1. The sending system begins to send IP packets in a size and at a rate that was negotiated in the previously described handshake.
2. The receiving system collects packets into a memory buffer and begins to reassemble them. The checksum field in each packet is used to determine whether the packet has been received correctly.
3. If a packet is missing, a retransmission is requested by the receiving system.
4. At regular intervals, the receiving system transmits an ACK command with the position of the last packet (sequence number) that was successfully assembled to the sending system. The sequence number is incremented by the number of bytes received, which is called *cumulative acknowledgment*, and the scheme is sometimes referred to as a *Positive Acknowledgement with Retransmission* (PAR) scheme. Each ACK command can set a flag that alters the rate of packet transmission, as well as the size of the data contained in each packet.
5. If the sending system doesn't receive an ACK command with instructions on which packet in the sequence it should send, then it proceeds to rebroadcast the previous set of packets.
6. When the receiving system gets the ACK message from the sending system with the current last assembled packet, the sending system continues sending additional packets from that point in the sequence.
7. When the receiving system assembles the last packet in the sequence, it performs a data check and then sends the LAST-ACK message.

TCP doesn't send an end-of-message marker with the last packet. The message is complete when the receiving computer has transmitted all of the assembled sequence into data that has been transferred to the application that consumes that data. There is no structure to the TCP data stream; TCP has no knowledge of what the data contains. It can't sequence one database record before another, or send one file before another. Any ordering or data handling is handled by the application. Therefore, it is up to the application to signal when the connection is no longer required. The lack of an application signal is the reason that connections are left in an open state when they are no longer needed.

A connection is terminated through the use of another handshake process. Each endpoint terminates the connection independently.

To terminate a connection, these steps are followed:

1. Endpoint 1 sends a FIN packet to Endpoint 2.
2. Endpoint 2 sends back an acknowledgment, or ACK, to Endpoint 1. Endpoint 1 closes its half of the connection, giving the connection a half-open status.
3. Endpoint 2 sends a FIN packet to Endpoint 1.
4. Endpoint 1 sends back an acknowledgment, or ACK, to Endpoint 2. Endpoint 2 closes its half of the connection, ending the connection entirely.

The previous summary describes a four-way handshake that employs four different transmissions. Most connection terminations employ a three-way handshake by combining step 2 and step 3 into a single FIN & ACK command.

To summarize, endpoints in an Internet socket can be in any of the following states:

1. LISTEN
2. SYN-SENT
3. SYN-RECEIVED
4. ESTABLISHED
5. FIN-WAIT-1
6. FIN-WAIT-2
7. CLOSE-WAIT
8. CLOSING
9. LAST-ACK
10. TIME-WAIT
11. CLOSED

In [Figure 17.2](ch17.html#the_state_diagram_for_a_tcp_system), the different states of TCP connections are illustrated, along with the methods used for moving between the different states. Indicated are the steps for the three-way handshake that establish a connection, as well as the relationship of the Active Open and Passive Open states.

![The state diagram for a TCP system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1702.png)

**Figure 17.2. The state diagram for a TCP system**

# Connections

The TCP host environment for many systems installs the TCP part of the network stack into the operating system in a manner that makes it appear to programs as if TCP is just another file system. This is the case for the proprietary Winsock interface from Microsoft, as well as the BSD Sockets interface that is used on many UNIX systems such as Macintoshes. BSD is the Berkeley Software Distribution or Berkeley Unix operating system. TCP communicates through the IP module, which requires a device driver to communicate with the network.

Programs wanting to use TCP for their data transfers have the following broad classes of connection-related system calls:

- OPEN
- CLEAN
- SEND
- RECEIVE
- STATUS

The parameters passed with these program commands are the half associations that provide the address and port of the target system. Other parameters that are part of these commands are used to set the security and other factors.

Connections are therefore a response to an OPEN call to the TCP module in the sending system's network stack. That module then communicates with the receiving system's TCP module, and both of these modules use their IP modules for the transfer mechanism. When a connection is made, a return call to the application passes a handle back to the application, by which the connection may be identified. A handle is a small integer value, and that value, along with other connection parameters, is stored in a transmission control block (TCB) within the program.

Programs make two types of OPEN calls: either for an Active OPEN connection or a Passive OPEN connection. An Active OPEN command has the TCP module send a message to the receiving system that a connection is to be opened. If the receiving system returns an Active OPEN command, then the connection is made and data transfer can begin.

A Passive OPEN command puts the receiving system's TCP module into a state in which it is prepared to accept incoming packets from a sending system. A Passive OPEN command can be passed the parameter of the sending system's endpoint, in which case the TCP program is listening for those particular packets. Alternatively, the Passive OPEN command can have no endpoints, in which case the TCP module accepts any incoming communications once it receives a connection request (SYN) from any sending system. That incoming SYN request originates because of an OPEN command on the sending system.

An application that issues a Passive OPEN command places itself into a wait state. TCP then informs the application when the connection is made by passing an Active OPEN command from the sending system along to the waiting application. At that point, the Passive OPEN state on the receiving system is changed to an Active OPEN state, and data transfer begins.

# Flow Control

The TCP flow control mechanism works by establishing an initial transmission rate and packet size, and then altering these parameters as needed during data transfer. The size of the packet header doesn't change, but the amount of TCP data in the body of the packet can be altered. The maximum segment size (MSS) parameter controls the size of a single segment that can be used, something that is established during the handshake, subject to the maximum transmission unit (MTU) size allowed by the network's Data Link layer.

## Sliding windows

The flow control protocol used is referred to as a *sliding window* because as the packets are received and assembled, the receive window field's value can be altered by the receiver to indicate to the sender how much data it can buffer at the moment. The sending system then sends only that amount of data until the next ACK message is received, and the receive window parameter tells the sender to send that additional amount of information. [Figure 17.3](ch17.html#a_receive_sliding_window_allows_data_to) illustrates how a Receive Sliding window operates.

![A Receive Sliding window allows data to be transferred efficiently without buffer overrun.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1703.png)

**Figure 17.3. A Receive Sliding window allows data to be transferred efficiently without buffer overrun.**

A TCP window can be from 2 to 65,535 bytes. Some systems employ a technique called *window scaling* that is negotiated in the TCP handshake. This option can increase the maximum window size up to as much as 1GB. Window scaling is reported to be problematical with many routers and firewalls, and with Vista and Linux hosts.

## Congestion control

The receiver can also halt data flow. To do so, it sets the window size to zero. When the sending system detects a stop signal, it turns on a persist timer that controls the timeout for data sending. When the timer reaches its value, the sending system sends a small packet, which triggers an ACK from the receiver with a new receive window size to send. This system ensures that the data transfer doesn't permanently stop if the receiving system's next ACK message is lost.

Another method that can be used to interrupt the TCP data stream is to send additional data marked as urgent. When packets arrive with this marker, TCP stops processing data in the current stream and processes the urgent packets before returning to finish processing the original stream. Urgent packets are referred to as out-of-band (OOB) data. An example of an OOB process would be if you sent an interrupt or abort sign from the program on the sending host.

As an optimization, TCP allows the use of selective acknowledgments (SACKs). The receiver can send a SACK message at any point when a block of packets are received that can be assembled but require some previous packets in order to be a correct sequence. The SACK message has the same structure as the ACK, but provides the start and end sequence numbers that were received. For example, if bytes 0 to 2044 were received and the SACK block has the sequence numbers 4088 to 9696 for the range that was received, then the sending system would retransmit packets with the sequence numbers 2045 to 4078. SACK is optional, but widely used.

Flow control also includes mechanisms that alter the transmission rate as a function of network performance. Based on how often the sending system receives ACKs back from the receiving system, the network performance can be estimated. Longer intervals between ACKs indicate network congestion and are based on a retransmission time that estimates the round-trip time. Each TCP message contains a timestamp. TCP has a set of algorithms called slow start, congestion avoidance, fast retransmit, and fast recovery, which were developed to control the transfer rate.

## Multiplexing

Multiplexing is a feature that allows a data stream to be sent using several different processes. TCP includes multiplexing as an option. When an application supports it, multiplexing can be used to speed up or optimize TCP data transfers. You see an example of multiplexing when a browser transfers a Web page using the HTTP protocol, or when a file transfer utility transfers a file over multiple connections. TCP can assemble that data from the different data streams.

Applications send their data over either a well-known port or a registered port. Apple iTunes uses port 3689 to receive data using the Digital Audio Access Protocol (DAAP). When you refresh your list of podcasts (a set of RSS feeds), multiple connections using the same port number are opened. If you have a larger video file, such as NBC's Nightly News or Meet the Press video, and no other podcasts are being downloaded, then the three streams that iTunes creates are dedicated to transferring that video file. If you have multiple podcasts to download, then those three streams are distributed between the different podcasts. [Figure 17.4](ch17.html#this_is_an_example_of_multiplexing_three) illustrates multiplexing by showing three concurrent TCP streams.

![This is an example of multiplexing three individual file streams with the same protocol and port.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1704.png)

**Figure 17.4. This is an example of multiplexing three individual file streams with the same protocol and port.**

TCP doesn't know the details of which stream is associated with which podcast. It is up to iTunes to take the data and properly populate the podcast files into the correct folders so that they show up in the application. It is also up to iTunes to determine which files it wants to download and in which order. As a user, you can modify the download order by moving files up or down in the download list, pausing a download, or deleting the download entirely.

# User Datagram Protocol

The User Datagram Protocol, or UDP, is an Internet Protocol that creates stateless connections between two hosts on an IP network. UDP creates a short data transfer format called a *datagram* and a connection called a *Datagram socket* between two endpoints. The virtual connection that is created uses the same concept of a port for sending data of different types between hosts. *Stateless* refers to the transfer mechanism, which doesn't attempt to ensure the validity of the data that is sent. The receiving system reconstructs data from the datagrams that arrive, without regard to whether they are in proper order or whether the sequence is complete.

### Note

You sometimes see UDP referred to as the Universal Datagram Protocol, or tongue-in-cheek as the Unreliable Datagram Protocol. However, User Datagram Protocol is the formal name, as specified in RFC 768.

The fact that UDP doesn't maintain the overhead that TCP does means that UDP transfers are much faster than TCP. This makes UDP a better choice when reliable data isn't required, either because the message is short or because there is a lot of redundant or optional data being sent. Name resolution services, such as the Domain Name System (DNS) that you learn about in [Chapter 19](ch19.html), use UDP because their messages are short and the system is a broadcast system that retransmits queries when the answers haven't yet arrived. Voice, music, and video applications use UDP because if a frame drops out of a movie or a fraction of a second of Voice over IP (VoIP) is lost, the user experience isn't degraded much. Nearly all streaming media applications use UDP as their transfer protocol on IP networks.

UDP datagrams have the very simple message format shown in [Figure 17.5](ch17.html#the_structure_of_a_udp_datagram). The only features found in the datagram are the checksum used to determine the validity of the datagram and the ability to multiplex (or mux) datagrams, which provides for the transmission of multiple data streams for applications that support it. Both of these features are optional, as is the specification of the source port when IP version 4 is used, but a checksum is required for IP version 6.

![The structure of a UDP datagram](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1705.png)

**Figure 17.5. The structure of a UDP datagram**

Unless a network is using a lot of media applications, UDP tends to be a minor but important component of traffic on the network. Some very important protocols use UDP, however. Not only does DNS use UDP, but the Dynamic Host Configuration Protocol (DHCP) that supplies IP addresses to clients, the Routing Information Protocol (RIP) that is used to provide dynamic routing on LANs, and the Simple Network Management Protocol (SNMP) that is used for most network management packages use UDP as well. That makes UDP a critical protocol in the Internet Protocol Suite.

In networks where there are a lot of media applications in use, UDP can crowd out TCP traffic. When TCP detects network congestion, it has mechanisms that throttle back TCP packet production to combat the congestion. This allows UDP to consume even more of the network's bandwidth, which can effectively crowd out critical traffic required by network services. TCP applications such as database access, which require the reliable data transfer of TCP to operate, can be slowed or halted until the situation is rectified. This problem has led many networks to either ban or limit the amount of streaming services that can run on the network.

# Ports

Both TCP and UDP Transport Protocols use what is called a port to communicate between endpoints of an Internet socket. When data packets arrive at their destination, they are examined for their source address, source port number, destination address, and destination port number. The port number is assigned by agreement to different types of data communications and maintained in a registry by the Internet Assigned Numbers Authority (IANA; `www.iana.org/assignments/port-numbers`).

Each computer manages its own ports independently of any other computer. A logger process, or on Linux/UNIX a super daemon process, monitors port numbers, especially the well-known ports, to determine when traffic is received.

There are three different ranges of ports:

- **Well-Known Ports**. These are ports used by common protocols and are in the range of 0 to 1023; they are administered by IANA. A selection of well-known ports is shown in [Table 17.1](ch17.html#common_well-known_ports_open_parenthesis).
- **Registered Ports**. These are ports that send or receive traffic for specific applications that are registered by vendors, industry trade groups, and other individuals and organizations. Registered ports are given the range 1024 to 49151. Registered ports are not controlled by IANA, but are listed in their registry.
- **Dynamic and/or Private Ports**. These ports are left unassigned for use. In some applications, ports are chosen randomly during a connection to improve security. These are referred to as *ephemeral ports*, and they lose their significance when the connection closes. The range for dynamic and private ports is from 49152 to 65535.

### Note

Ports greater than 1023 can be assigned on the fly. Those types of ports are called *transient ports*, and they are specific to the particular TCP module in use.

**Table 17.1. Common Well-Known Ports (0 to 1023)**

| Port | Assignment |
| --- | --- |
| 0 - T, U | Reserved |
| 1 - T, U | TCP Port Service Multiplexer |
| 2 - T, U | Management Utility |
| 3 - T, U | Compression Process |
| 5 - T, U | Remote Job Entry |
| 7 - T, U | Echo |
| 13 - T, U | Daytime - (RFC 867) |
| 17 - T, U | Quote of the Day |
| 18 - T, U | Message Send Protocol |
| 19 - T, U | Character Generator |
| 20 - T, U | FTP - Default Data |
| 21 - T, U | FTP - Control command |
| 22 - T, U | SSH Remote Login Protocol |
| 23 - T, U | Telnet |
| 25 - T, U | Simple Mail Transfer Protocol (SMTP) |
| 33 - T, U | Display Support Protocol |
| 37 - T, U | TIME Protocol |
| 38 - T, U | Remote Access Protocol |
| 39 - T, U | Resource Location Protocol (RLP) |
| 41 - T, U | Graphics |
| 42 - T, U | ARPA Host Name Server Protocol |
| 42 - T, U | WINS (Unofficial) |
| 43 - T, U | WHOIS Protocol |
| 48 - T, U | Digital Audit Daemon |
| 49 - T, U | TACACS Login Host Protocol |
| 50 - T, U | Remote Mail Checking Protocol |
| 53 - T, U | Domain Name System (DNS) |
| 63 - T, U | whois++ |
| 65 - T, U | TACACS - Database Service |
| 66 - T, U | Oracle SQL*NET |
| 67 - T, U | Bootstrap Protocol (BOOTP) Server |
| 68 - T, U | Bootstrap Protocol (BOOTP) Client |
| 69 - T, U | Trivial File Transfer Protocol (TFTP) |
| 70 - T, U | Gopher Protocol |
| 79 - T, P | Finger Protocol |
| 80 - T, P | Hypertext Transfer Protocol (HTTP) |
| 82 - T, U | XFER Utility |
| 88 - T, P | Kerberos |
| 92 - T, U | Network Printing Protocol |
| 105 - T, U | Mailbox Name Nameserver |
| 107 - T, U | Remote Telnet Service Protocol |
| 109 - T, U | Post Office Protocol 2 (POP2) |
| 110 - T, U | Post Office Protocol 3 (POP3) |
| 113 - T, U | Authentication Service |
| 115 - T, U | Simple File Transfer Protocol (SFTP) |
| 118 - T, U | SQL (Structured Query Language) Services |
| 119 - T, P | Network News Transfer Protocol (NNTP) |
| 123 - T, U | Network Time Protocol (NTP) |
| 129 - T, U | Password Generator Protocol |
| 137 - T, U | NetBIOS Name Service |
| 138 - T, U | NetBIOS Datagram Service |
| 139 - T, U | NetBIOS Session Service |
| 143 - T, U | Internet Message Access Protocol (IMAP) |
| 152 - T, U | Background File Transfer Program (BFTP) |
| 153 - T, U | Simple Gateway Monitoring Protocol (SGMP) |
| 156 - T, U | SQL Service |
| 161 - T, U | Simple Network Management Protocol (SNMP) |
| 162 - T, U | Simple Network Management Protocol Trap (SNMP TRAP) |
| 170T | Print-srv, Network PostScript |
| 177 - T, U | X Display Manager Control Protocol (XDMCP) |
| 179T | Border Gateway Protocol (BGP) |
| 194T | Internet Relay Chat (IRC) |
| 201 - T, U | AppleTalk Routing Maintenance |
| 213 - T, U | IPX |
| 218 - T, U | Message Posting Protocol (MPP) |
| 220 - T, U | Interactive Mail Access Protocol (IMAP), version 3 |
| 389 - T, U | Lightweight Directory Access Protocol (LDAP) |
| 401 - T, U | Uninterruptible Power Supply (UPS) |
| 427 - T, U | Service Location Protocol (SLP) |
| 443T | Hypertext Transfer Protocol over TLS/SSL (HTTPS) |
| 444 - T, U | Simple Network Paging Protocol (SNPP), (RFC 1568) |
| 445T | Microsoft-DS Active Directory, Windows shares |
| 445/UDP | Microsoft-DS SMB file sharing |
| 464 - T, U | Kerberos Change/Set password |
| 500/UDP | Internet Security Association and Key Management Protocol (ISAKMP) |
| 513T | Login |
| 513/UDP | Who |
| 514T | Shell |
| 514/UDP | Syslog |
| 515T | Line Printer Daemon |
| 520/UDP | Routing – RIP |
| 524 - T, U | NetWare Core Protocol (NCP) |
| 525/UDP | Timed, Timeserver |
| 530 - T, U | RPC |
| 531 - T, U | AOL Instant Messenger (IRC) (Unofficial) |
| 540T | Unix-to-Unix Copy Protocol (UUCP) |
| 546 - T, U | DHCPv6 client |
| 547 - T, U | DHCPv6 server |
| 548T | Apple Filing Protocol (AFP) over TCP |
| 554 - T, U | Real Time Streaming Protocol (RTSP) |
| 631 - T, U | Internet Printing Protocol (IPP) |
| 660T | Mac OS X Server Administration |
| 666/UDP | Doom |
| 691T | MS Exchange Routing |
| 860T | iSCSI (RFC 3720) |
| 953 - T, U | Domain Name System (DNS) RDNC Service |
| 993T | Internet Message Access Protocol over SSL (IMAPS) |
| 995T | Post Office Protocol 3 over TLS/SSL (POP3S) |

# Problems with TCP

TCP communications have suffered from a number of different types of attacks. In a Denial of Service (DoS) attack, the intruder can send multiple SYN packets originating from a spoofed IP address. This attack, referred to as a SYN flood, forces the receiving system (usually a server) to respond to these SYN requests and use up its resources managing bogus connections.

Another problem with TCP traffic is that the header isn't encrypted and can be read by packet sniffers that are monitoring the data. It is possible to hijack a connection by examining the sequence number and then creating a packet that has the correct sequence number in the stream. That packet doesn't need to be complex; it only needs to contain enough information to break the synchronization between systems. Once the connection is broken, the hacker has to take control of the packet routing to make their system the substitute endpoint. The incorporation of a randomly selected ISN makes it much more difficult to fall prey to connection hijacking. This form of attack is a variation of what is called the "Man-in-the-Middle" attack.

As mentioned earlier, TCP traffic can suffer when other types of broadcast traffic, such as UDP, become the majority of the network traffic. It is for that reason that TCP implements congestion control, lowering the size of the receive window to slow down transmission. At some point, TCP traffic can be brought to a standstill, a condition referred to as *congestion collapse*. There are solutions to this problem, some of which are problematical themselves.

The first solution is to limit the use of streaming media on the network. If you are in an office that uses productivity applications and don't require much multimedia content, then limiting multimedia isn't an issue. However, if your work requires the use of large amounts of streaming media, then other methods of control need to be employed. One potential solution is to employ quality of service (QoS) applications to maintain a stated level of traffic flow. Many network operating systems are beginning to implement QoS services into their core services. To get advanced QoS, many companies invest in sophisticated routers.

Another issue that crops up in high-traffic situations occurs when there is a large data stream and the receiving system starts to send back ACKs to the sender with a very small receive window. The sender then begins to send back very small packets with only a few bytes of data in them. This behavior is highly inefficient and has been given the name of silly window syndrome (SWS). To combat this behavior, newer implementations of TCP include sender-side logic, called Nagle's algorithm, which detects this condition and corrects it.

Nagle's algorithm, which is described in "Congestion Control in IP/TCP Internetworks" (RFC896), is used to address the problem of congestion caused by too many very small packets being sent at the same time. Many processes such as keystrokes from Telnet systems send data in chunks as small as 1 byte, and because all TCP headers are at least 40 bytes (20 for TCP and 20 for IPv4) the overhead in sending data of this type can be enormous. What Nagle's algorithm does is to coalesce many small outgoing messages and send them as a single unit provided that there is no response from the receiving system to messages already sent.

Nagle's algorithm is as follows:

```
IF there is new data to send
  IF the window size >= MSS AND available data is >= MSS
    SEND complete MSS segment now
  ELSE
    IF there is unconfirmed data still in the pipe
      enqueue data in the buffer until an acknowledge is received
```

```
ELSE
      SEND data immediately
    END IF
  END IF
END IF
```

Nagle's algorithm has one noticeable disadvantage; it leads to bad results when TCP delayed acknowledgments are used—the so-called ACK delay. Many TCP implementations do not use Nagle's algorithm or turn it off because common delay settings of 500 milliseconds (1/2 second) can lead to multiple application writes. Delays can be turned off using the TCP_NODELAY command; however, most solutions to the problem buffer commands in the application to avoid congestion due to small packet storms.

The phenomena where a receive window is sent large numbers of minute packets and is therefore starved of data to operate on is called the tinygram syndrome, and it contrasts to the silly window syndrome where the receive window is entirely filled and can't receive additional information.

# Summary

This chapter described the two most important transport protocols used on TCP/IP networks: the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP is used when the data must be delivered intact with complete fidelity. UDP is used by applications that can tolerate lost data and out-of-sequence packets.

Both of these protocols create virtual connections and use the concept of ports to send data of different types from a sending system to a receiving system. Connections are made between two hosts and are independent of the path that the data takes to get there.

TCP has a number of different mechanisms to ensure that data arrives correctly. A sequencing scheme is used to reconstruct packets, and the protocol sends back acknowledgments when data arrives or when data is required. In this chapter you learned about the different flow control and congestion controls used to maintain quality.

UDP is important to streaming media applications. UDP has much less overhead than TCP and is used in situations where applications use very small broadcast messages, or in streaming applications.

In the next chapter you learn about the Internet Protocol, which controls the addressing scheme used to send packets across a TCP/IP network. In this chapter both IP version 4 and IP version 6 are described. The concepts of networks and subnets are fully disclosed.
