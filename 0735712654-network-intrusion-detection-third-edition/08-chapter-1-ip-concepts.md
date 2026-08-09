# Chapter 1. IP Concepts

![IP Concepts](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

As you read this chapter, it will become apparent that you belong in one of two categories: the beginner category or that of the seasoned veteran. The Internet Protocol (IP) is a large and potentially intimidating topic that requires a gentle introduction for uninitiated beginners so as not to overwhelm them with foreign acronyms, details, and concepts. Therefore, the purpose of this first chapter is to expose newcomers to terms, concepts, and the ever-present acronyms of IP. The suite of protocols covered here is more commonly known as Transmission Control Protocol/Internet Protocol (TCP/IP). These protocols are required to communicate between hosts on the Internet—the worldwide infrastructure of networked hosts. Indeed, communication protocols other than TCP/IP exist (for instance, AppleTalk for Apple computers). These protocols are typically found on intranets, where associated hosts talk on a private network. Most Internet communications require TCP/IP, which is the standard for global communications between hosts and networks.

Those seasoned veteran readers who dabble in TCP/IP daily might be tempted to skip this chapter. Even so, you should give it a quick skim. If you ever need to explain a concept about IP (perhaps to the individual who signs off on your pay raise or bonus, for example), you might find this chapter’s approach useful. Those of you who are getting your feet wet in this area will certainly benefit from this introduction.

This is an around-the-world introduction to TCP/IP presented in a single chapter. Many of the topics discussed in this introductory chapter are covered in much greater detail and complexity in upcoming chapters; those chapters contain the core content, but you need to be able to peel away the theoretical skin to understand them. Specifically, this chapter covers the following topics:

- ****The TCP/IP Internet model.****This section examines the foundations of communications over the Internet, specifically communications made possible by using a common model known as the TCP/IP Internet model.
- ****Packaging of data on the Internet.****This section reviews the encapsulation of data to be sent through different legs of a journey to its destination.
- ****Physical and logical addresses.****This section highlights the different ways to identify a computer or host on the Internet.
- ****TCP/IP services and ports.****This section explores how hosts communicate with each other for different purposes and through different applications.
- ****Domain Name System.****This section focuses on the importance of host names and IP number translations.
- ****Routing.****This section explains how data is directed from the sending computer to the receiving computer.

# The TCP/IP Internet Model

Computer users often want to communicate with another computer on the Internet for some purpose or another (to view a web page on a remote web server, for instance). A response from a web server can seem almost instantaneous, but a lot of processes and infrastructures actually support this seemingly trivial act behind the scenes.

## Layers

[Figure 1.1](ch01.html#ch01fig01) shows a logical roadmap of some of the processes involved in host-to-host communications. You begin the process of downloading a web page in the box labeled “Web browser.” Before your request to see a web page can get to the web server, your computer must package the request and send it through various processes and layers. Each layer represents a logical leg in the journey from the sending computer to the receiving computer. After the sending computer packages the data through the different layers, it is delivered to the receiving computer over the Internet. The receiving computer unwraps the data layer by layer. An individual layer gets the data intended for it and passes the remainder of the message to upper layers.

![The TCP/IP Internet model.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig01.gif)

**Figure 1.1. The TCP/IP Internet model.**

Although discussed in more detail later in this chapter, it is important now to briefly look at each layer. The following four layers comprise the TCP/IP Internet model:

- ****Application layer.****The application layer is the topmost layer (the request for a web page in the preceding example). Software on the sending and receiving computers supports the implementation of the application (the web browser and web server, for instance).
- ****Transport layer.****Below the application layer lays the transport layer. This layer encompasses many aspects of how the two hosts will communicate. This transport layer is often concerned with providing reliability over other inherently unreliable layers.Two transport layers protocols will be covered: TCP, which is referred to as a reliable protocol because mechanisms ensure data delivery, and User Datagram Protocol (UDP), which makes no promise of reliable delivery. In this example application, TCP is required because of the unacceptability of data loss.
- ****Network layer.****Below the transport layer is the network layer, which is responsible for moving the data from the source computer to the destination computer (the web server in this case), often one hop or leg of the journey at a time. This hop is between a computer and a router or a router and a router, but it ultimately takes the data closer in routing space to its destination.
- ****Link layer.****The bottom layer is the link layer, which is the component that takes care of communications from a host to the physical medium on which it resides. In this case, that component is Ethernet. This layer is concerned with receiving and sending data from the host over a specific interface to the network.

## Data Flow

Look at [Figure 1.1](ch01.html#ch01fig01) again. In theory, the data flow activity is this: The request for a web page “descends” the sender’s layers, often referred to as the TCP/IP stack. It gets directed to the destination computer and “ascends” its TCP/IP stack. The vertical arrows between layers represent the up and down flow on the same computer. The horizontal arrows between computers signify that each layer talks to its “peer” layer on the communicating host. The two computers do not directly interact with each other, per se. When the request descends the sending computer’s TCP/IP stack, it is packaged in such a manner that each layer has a message for its counterpart layer, and so they appear to be talking directly.

This concept is quite important and crucial to understanding this chapter and the TCP/IP model, in general. Therefore, it is important to reiterate the poignant points and elaborate on terminology. The term TCP/IP stack is used to denote the layered structure of processing a TCP/IP request or response. A process known as encapsulation does the implementation of the layering. This means that data on the sender’s host gets wrapped with identifying information to assist the receiving host in parsing the received message layer by layer. Each layer on the sending host adds its own header, and the receiving host reverses the process by examining the message, stripping it of its header, and directing it to the appropriate layer. This process is repeated for the higher layers until the data reaches the uppermost layer, which finally processes the web page request. When the response is sent back, the entire process is repeated; now the web server host packages the data to be sent, it is delivered and received, and the web browser host strips the received message to pass to the application layer supporting the web browser.

# Packaging (Beyond Paper or Plastic)

At a very granular level, data exchanged between hosts must be bundled in some kind of standard format. A host is a generic term that can reference a workstation on your desk, a router, or a web server to name just a few examples. The important distinction is that these computers are connected to a network capable of transporting data to and from the computer. In the generic sense, the packaging of associated data is called a packet. The problem in terminology arises because this data package is labeled differently at various layers of communication between the source application and the destination application located on different hosts. This section discusses some of the key concepts related to data packaging, including bits, bytes, packets, data encapsulation, and interpretation of the layers.

## Bits, Bytes, and Packets

The atom of computing is a bit, a single storage location that has a value of either 0 or 1 (also known as binary). Although succinct and compact, you cannot actually store or convey a lot of information with a single bit, so bits are grouped into clumps of eight. A unit of eight bits is a byte (or octet, if you prefer). Eight times a very small amount of information is still pretty small, but an octet can contain an American Standard Code for Information Interchange (ASCII) character, such as the letter a or a comma (,). It can also hold a large integer number, as high as 255 (28-1).

**Bits, Bytes, and Binary**

[Figure 1.2](ch01.html#ch01fig02) shows a byte. Because this discussion is focusing on bits, binary is the language used— the language of 0s and 1s. Each bit is represented as a power of 2, the base of binary. Notice that a byte spans powers of 2 from 20 through 27. If all bits have a value of 0, the byte is obviously 0. Now, imagine that all bits are 1s. Add up all the individual bit values, starting with the smallest value (20 = 1, any base with an exponent of 0 is 1); you will have 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128. The total value is 255, and that is the maximum value that a given byte can have. This value is examined later when the discussion turns to IP addresses.

![Bits, Bytes, and Binary](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig02.gif)

You just saw an example of how binary-to-decimal conversion is done. If you are given a byte of data, just re-create this byte with the appropriate powers of 2 and their associated decimal values. Any bit that is set is assigned the accompanying decimal value of that bit. Then, just total up all the decimal values; voila, the conversion is done. This is not really rocket science after all.

Multiple bytes, or octets, are grouped together for shipping across a network by packaging them into packets. [Figure 1.3](ch01.html#ch01fig03) shows one of the great truths of networking: An overhead cost accrues when slinging packets around the network.You have to go through a lot of trouble to package your content for shipping across a network and then to unwrap it when it gets to the other side (and even more trouble, of course, to finish the job with a tamper-proof seal). A field known as the cyclical redundancy check (CRC), or checksum, is used to validate that the frame (the name given to the packet on the wire) has not been damaged or corrupted in transit.

![Portrait of a packet.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig03.gif)

**Figure 1.3. Portrait of a packet.**

Like an envelope addressed for mailing, IP packets need to include the addresses of both the sending and receiving hosts (see [Figure 1.3](ch01.html#ch01fig03)). If you live in a house with a street address, you can think of that as your hardware address, the address assigned to your house. In networking, at least with Ethernet networks, this is analogous to a network interface card’s (NIC) Media Access Controller (MAC) address. This hardware address is assigned to the NIC when the card is constructed. The MAC address is 48 bits long, which means it can hold a very large number (248-1). The “[Addresses](ch01.html#ch01lev1sec3)” section later in this chapter discusses the differences between MAC addresses and IP addresses.

To create a frame, which is the name the packet acquires when transmitted on physical media, you construct the packet using various protocol layers and then include the physical information. Finally, the frame is placed on the networking medium by the NIC. The frame has a frame header of 14 bytes, with fields such as the source and destination MAC addresses, frame data that can vary in length, and a trailer of 4 bytes that represents the CRC.

## Encapsulation Revisited

[Figure 1.4](ch01.html#ch01fig04) represents the concept of the layered packaging configuration. Different layers of protocols theoretically “talk” to like layers of protocols on the source and destination hosts. The layers are stacked atop one another— hence, the origin of the term “TCP/IP stack.” At each layer of the stack, the packet consists of a header of its own and data, sometimes known as the payload. All the encapsulation is done for the purpose of sending some kind of content, but the encapsulation requires different header information at different levels in its journey from source to destination.

![One layer’s header is another layer’s data.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig04.gif)

**Figure 1.4. One layer’s header is another layer’s data.**

Suppose that you have a message or other content to send. It is first collected by the application, which could be a program such as telnet or electronic mail; these TCP applications are discussed in more detail in the section “[IP Protocols](ch01.html#ch01lev1sec5).” The TCP packet is known as a TCP segment and includes the TCP header and TCP data. If this were UDP, the packet would be known as a datagram, which is confusing because it is redundant with the name at the IP layer.

At this point, the TCP segment is handed down from the TCP layer of the TCP/IP stack to the IP layer. The IP layer prepends (that means appends at the front) header information to the TCP segment and becomes known as an IP datagram. Really, the TCP header and data become invisibly enmeshed as data for the IP datagram, which has its own header. The IP datagram is delivered to the link layer of the TCP/IP stack, and it is known as a frame. The link layer prepends the frame header to the IP datagram to carry it across the physical medium, such as Ethernet.

The process is repeated in reverse when the frame arrives at the destination host and all headers are stripped away and passed to the proper upper-layer protocols. Each layer of the TCP/IP stack with its embedded message converses with the similar layer of the receiving host.

## Interpretation of the Layers

With all the layering going on, the bottom line is that you have a bunch of adjacent 0s and 1s. How do you know how to interpret them? Suppose that you are looking at the IP header; how do you know what kind of embedded protocol you will find following it? Surely that must be known to properly interpret the protocol. The term *protocol* is meant to denote a set of agreed upon rules or formats. Each protocol (such as IP, TCP, UDP, and ICMP) has its own layouts and formats.

[Figure 1.5](ch01.html#ch01fig05) shows an example of the organization of the IP header. You can see that a certain number of bits are allocated for each field in the header. A Protocol field identifies the embedded protocol. Each row that you see in the IP header is 32 bits (0 through 31, inclusive), which means four (8-bit) bytes. To complicate matters a little, counting starts with 0 when talking about bit and byte locations. The first row represents bytes 0 through 3; the second row represents bytes 4 through 7; and the third row represents bytes 8 through 11. Notice that the circled Protocol field is in the third row. The preceding time-to-live (TTL) field is 1 byte long, which makes it the 8th byte; and the Protocol field, which is also 1 byte long, represents the 9th byte. This means that the 9th byte (actually, it’s the 10th byte, but remember counting starts at 0) is examined to find the embedded protocol. The point is that most packets at their respective levels are positional; fields can be discovered by going to known displacements in the packet.

![Positional layouts.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig05.gif)

**Figure 1.5. Positional layouts.**

Now that you have counted your way to the Protocol field, what is it and what does it do? The value in this field tells you what protocol is found in the embedded data. Suppose that the value you find in this byte is 17. You might find the protocol value expressed in hexadecimal. A hexadecimal 11 is the same as a decimal 17. This means that a UDP packet is embedded after the IP header. A value of 6 means that the embedded packet is TCP, and a value of 1 means that it is Internet Control Message Protocol (ICMP).

**Base 16, Hexadecimal**

Okay, so you have learned that binary is base 2 and is made up of 0s and 1s. This is the numbering system used by computers to represent data. So, why complicate the matter with another entirely new numbering system, base 16 (or hexadecimal)? The real dilemma is that it takes a lot of bits to represent any sizable number and, therefore, binary becomes very unwieldy very soon. Hexadecimal assists in referencing binary numbers in a more abbreviated notation. You can replace 4 binary bits with 1 hexadecimal character (24 = 16).

Consider, for example, the IP header protocol field; it is 8 bits. That can be converted into 2 hex characters. A decimal 17 in the protocol field, as mentioned earlier, means that the embedded protocol is UDP. How do you go from a decimal 17 to a hexadecimal 11?

```
27 26 25 24     23 22 21 20 
0  0  0  1      0  0  0  1 
```

The binary powers of the 8 bits are shown. To arrive at 17, you need to have the bit corresponding to 16 (or 24) set to 1, and the bit corresponding to 1 (20) set to 1—that is, 16 + 1 = 17. These have been grouped as two hex digits, two 4-bit clumps. The 4 bits (or hex character) that are leftmost (also known as high-order or most significant bits) have a value of 0001. Likewise, the 4 bits that are rightmost (also known as low-order or least significant bits) have a value of 0001. Each hex character represents values of 0 through 15. And each of these has a low-order bit of 1 set (20), and so we arrive at the value of 11 hexadecimal (also known as 0x11, in which the 0x distinguishes this as hex, not decimal).

# Addresses

Most likely, you have heard the term IP address. But, what does it really represent and what does it really do? And, exactly how do hosts address each other? These are some of the topics covered in this section.

## Physical Addresses, Media Access Controller Addresses

You can scour the headers of IP packets looking for physical layer MAC addresses until you turn blue, and you will not find them. MAC addresses do not mean anything to IP, which uses logical addresses; they are not part of the protocol. For all intents and purposes, they may as well not exist.

By the same token, physical MAC addresses are how the Ethernet card interfaces with the network. The Ethernet card does not know a single thing about IP, IP headers, or logical IP addresses. So, you are faced with the signature line of Cool Hand Luke: “What we have here is a failure to communicate.” Clearly, if things are going to work, an operation process is required that facilitates the correspondence between logical IP and physical MAC addresses.

Do you know the IP address of your desktop computer? If you don’t, you are not really one down at all; it is absolutely normal not to know it. It is normal for several reasons, one being that in these days most of you don’t even own or even get to keep the same IP address. IP address space is a precious commodity. When you connect to the network, many of you are loaned an address for that session, or possibly longer by an Internet service provider (ISP) or network service provider via applications, such as Dynamic Host Configuration Protocol (DHCP).

**Leasing an IP Number: Dynamic Host Configuration Protocol**

DHCP is a protocol that permits dynamic assignment of IP numbers. This replaces the labor-intensive process of IP address management, in which every host is configured with a static IP number assigned to it. DHCP allows the centralization and automation of the IP assignment process. Hosts are leased an IP number for a given amount of time, and this makes the process of managing and administering large networks more efficient. This is good for the network administrator, but makes the security administrator’s job more complicated (for example, when some IP number and associated temporary owner have to be chased down for questionable activity).

Exactly how many possible IP numbers are there? The exact number is 232 (because the address is comprised of 32 bits), which is a number higher than 4 billion. But, every single IP number is not available; reserved ranges decrease the possible numbers. With the explosive growth of the Internet worldwide, the sad realization has dawned that the IP addresses are being rapidly depleted. What are some remedies for the address depletion?

First, a particular site can use DHCP and assign IP numbers temporarily for the duration of their use. This means that not all hosts will be active at any given time and a smaller pool of possible IP numbers is required. The other remedy is something known as reserved private addresses. The governing body of the Internet, the Internet Address Numbers Authority (IANA), has set aside blocks of IP addresses to be used for internal addresses only. For instance, the 192.168 and 172.16 subnets are to be used for hosts talking within a particular network. This traffic should not leave the site’s gateway. This allows a site with an insufficient number of IP addresses to use these Class B network addresses for internal purposes and to save the assigned IP addresses for other purposes.

Okay, go ahead and smirk now; some of you did know your IP address. That is good. However, do you know your host’s MAC address by heart? The answer would most likely be “no,” because almost no one knows his MAC address. There are several reasons for this, but the primary one is that a 48-bit address with no provisions for human memorization is hard to lock into the brain.

The Address Resolution Protocol (ARP) enables you to resolve the translation of physical MAC addresses to logical IP addresses. ARP is not an IP protocol per se; it is the process of sending an Ethernet frame to all systems on the same network segment. This is known as a broadcast. If a message is a broadcast message, it is sent to all the machines on part of or the entire network. A point worth emphasizing is that ARP is for locally attached hosts only on the same network; this cannot be done between hosts on different networks.

The source host broadcasts the ARP request, and then presumably the destination host picks it up and replies with its MAC address. During this transaction, both the source and destination host, and any listening hosts on the network, cache (or save) what they have learned about the other host, thereby storing the IP and MAC addresses. This storage cuts down on the number of new ARP requests required. Ultimately, on the same network segment, the communications will occur between MAC addresses and not IP addresses. They might begin as a TCP/IP transaction with two hosts communicating between the same layers of TCP/IP, but when the actual delivery occurs, communication is between two hosts’ MAC addresses.

Why are MAC addresses so huge? After all, 48 bits is a lot of address space. The idea was that they would be unique for all time and space! That sounds good if you say it real fast, but future plans are to expand this value to 128 bits to accommodate its current limitations in allowing each NIC manufacturer to have a unique vendor code embedded in the MAC address.

## Logical Addresses, IP Addresses

An IP address has 32 allocated bits to identify a host. This 32-bit number is expressed as four decimal numbers separated by periods (for example, 192.168.5.5). These are not just random or sequential assignments. The initial portion of the IP number tells something about the size of the network on which the host resides. The remainder of the IP number distinguishes hosts on that network. Addresses are categorized by class; classes tell how many hosts are in a given network or how many bits in the IP address are assigned for the unique hosts in a network (see [Table 1.1](ch01.html#ch01table01)). A grouping known as Class A addresses assigns the initial 8 bits for a network portion of the address, for example, and the final 24 bits for the host portion of the address. Because 24 bits have been allocated for the hosts, more than 16 million (224-1) hosts can possibly be in the network. An example of a Class A network is the 18.0.0.0 through 18.255.255.255, IP space assigned to Massachusetts Institute of Technology.

**Table 1.1. 32 Bits for IP Address Space**

| **Class** | **Network Bits** | **Host Bits** | **Number of Hosts** |
| --- | --- | --- | --- |
| A | 8 | 24 | 16 million+ |
| B | 16 | 16 | 65,000+ |
| C | 24 | 8 | 255 |

The IP address classes range from Class A addresses to Class E. Classes A, B, and C are unicast addresses; when you send a packet to them, presumably you are addressing a single machine. Class D is known as a multicast address used to communicate with a designated set of hosts. Class E is reserved for experimental use. [Table 1.2](ch01.html#ch01table02) shows the address range associated with each class.

**Table 1.2. Address Classes and IP Ranges**

| **Class** | **Beginning IP** | **Ending IP** |
| --- | --- | --- |
| A | 0.0.0.0 | 127.255.255.255 |
| B | 128.0.0.0 | 191.255.255.255 |
| C | 192.0.0.0 | 223.255.255.255 |
| D | 224.0.0.0 | 239.255.255.255 |
| E | 240.0.0.0 | 247.255.255.255 |

**House Rules of CIDR**

You might hear a new term, classless inter-domain routing (CIDR) to refer to addresses. For the longest time, addresses were part of a particular class and that meant your network was allocated either 16 million+, 65,000+, or 255 hosts. The most common situation was networks that required between 255 and 65,000 hosts. Because many of these sites were allocated Class B networks, many IP numbers went unassigned. Given that IP numbers are finite commodities, a remedy was needed to allocate networks without class constraints.

CIDR assigns networks, not on 8-bit boundaries, but on single-bit boundaries. This allows a site to receive the appropriate number of IP numbers, and thus reduces waste. CIDR uses a unique notation to designate the range of hosts assigned to a site. If you want to specify the 192.168 address range in CIDR, it would look like 192.168/16. The first part of the notation is the decimal representation of the bit pattern allocated to the network. It is followed by a slash and then the number of bits that represent the network portion of the address. This example is the same as a Class B network, but it can be modified easily enough to represent smaller networks.

## Subnet Masks

Another concept you need to be aware of is something known as the subnet mask. This mask informs a given computer system how many bits in its IP address have been relegated to the network and how many to the host. Each bit that is a network bit is “masked” with a 1. A Class A address, for instance, has 8 network bits and 24 host bits. In binary, the 8 consecutive bits (all with a value of 1) translate to a decimal 255. The subnet mask is then designated as 255.0.0.0. Other classes have other subnet masks. A Class B network has a standard subnet mask of 255.255.0.0, and a Class C network has a standard subnet mask of 255.255.255.0. Why is this needed if you can tell what class and how many bits have been reserved for the network by examining the IP address? Some network administrators subdivide their networks. For instance, a Class C network could be divided into four individual subnets by assigning an appropriate subnet mask.

# Service Ports

This section is a “bit” easier. TCP and UDP have 16-bit port number fields in their respective header fields. This means they can have as many as 65,536 different ports, or services, and they are numbered from 0 to 65,535. One very important point to register in your long-term memory is that even though a service is usually located at its assigned port number, nothing guarantees this as true. Telnet, for instance, is almost universally found on TCP port 23. There is nothing stopping your nonconformist side from offering it at port 31337. And, what better way for a hacker who has broken into a computer to hide his tracks than by offering a service at an unexpected port? If a hacker were to run telnet at some high-numbered port rather than port 23, it would make his unauthorized connection more difficult to find and identify. Any service can be run at any port. On the other hand, if you want to network with other hosts, it is best to follow the standards. For UNIX hosts, the /etc/services file can be an excellent resource to match TCP or UDP port numbers with the expected, or well-known, services likely to be offered at that port number.

You see some very common port numbers and service examples from the /etc/services file. An excerpt here shows you the format of the file and the associated services. You see that a service known as domain (Domain Name Service, or DNS) can be offered on both TCP and UDP. This is unusual, but not abnormal; most services are offered on either TCP or UDP, but there are some exceptions (such as DNS).

```
ftp         21/tcp 
telnet      23/tcp 
smtp        25/tcp 
domain      53/udp 
domain      53/tcp 
```

[Figure 1.6](ch01.html#ch01fig06) shows how the service is specified in the packet. In this case, a UDP header has a 16-bit field known as the destination port. This is where the desired service or port is found. In this example, the value in the UDP header’s port number field would be 53, signifying that this datagram is destined for the Domain Name Service.

![Not just any port.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01fig06.gif)

**Figure 1.6. Not just any port.**

At one time in history, special significance was attached to ports below 1024. Those lower-numbered ports were the so-called trusted ports (chuckle) because only root could use them. The term *trusted port* originated because ports below 1024 were allocated to system processes. Therefore, if a foreign host saw an incoming connection with a source port less than 1024, it was assumed to be trusted because it ostensibly came from a system process. This made much more sense when the Internet was a safer place. This is much less true today, but the ports above 1024 have special significance. These are often called the ephemeral ports, which means they could be used by most any service for most any reason.

# IP Protocols

Turn your attention again to the four primary layers of the TCP/IP model (refer back to [Figure 1.1](ch01.html#ch01fig01)). You (as the user) use an application to interact with the IP communications stack. You use a program such as FTP to transfer files, telnet as a terminal emulator, and email to forward tired jokes and stories to 50 of your closest friends. The application takes the message, the information from the user or user process, and prepares it to be sent down through the IP stack. The remaining three layers are transport, network, and link.

Two different transport models are discussed at this point: a connection-oriented model (TCP) and a connectionless model (UDP). Connection-oriented means just what it sounds like: The software does everything that it can to ensure that the communication is reliable and complete and begins the process by establishing a connection known as a handshake. Connectionless, on the other hand, is a send-and-pray delivery that has no handshake and no promise of reliability. Any offered reliability must be built in to the application. [Table 1.3](ch01.html#ch01table03) shows some of the TCP and UDP attributes.

**Table 1.3. Attributes of TCP Versus UDP**

| **TCP** | **UDP** |
| --- | --- |
| Reliable | Unreliable |
| Connection-oriented | Connectionless |
| Slower | Faster |

UDP is the easiest communication protocol to comprehend—after all, you just assemble packets and fire them into the network. The destination host scoops them up, demultiplexes (strips the headers off at one layer and sends it to the appropriate upper-layer protocol), and extracts the message. Certainly, a few datagrams might get lost along the way, but that is often okay; for plenty of applications, this is not an issue. If you were broadcasting audio, for instance, and a word got lost, your mind could probably compensate for this and fill in the missing word. If you were sending video, perhaps there would be a little blank spot where some packets got lost. Most of the time, this is acceptable. The data that travels over UDP is not necessarily unreliable; it is just that UDP itself is not responsible for it. The application must ignore the missing pieces or ask for the missing pieces.

What if you have an application that cannot tolerate the loss of packets? That is when TCP is used. It ensures that all data sent is received. Several mechanisms are in place to verify delivery and proper sequencing of TCP data. One means of control is an acknowledgement.

An acknowledgement (ACK) is an important part of the TCP protocol. TCP is so reliable because each packet is acknowledged after the destination host receives it. If a packet is not received (and therefore not acknowledged), it is resent. Thus, TCP ensures that all the packets are received, and so is deemed a reliable service. This is a much slower way of doing business, but you can set certain optimizations to speed up the process. That said, TCP will always be slower than UDP.

The final IP protocol discussed here is the Internet Control Message Protocol (ICMP), which is a fascinating lightweight set of applications originally created for network troubleshooting and to report error conditions. The most well-known ICMP application is certainly the echo request/echo reply (or ping). You can use a ping to determine whether a given network host is reachable. Other ICMP applications are used for such things as flow control, packet rerouting, and network information collection (to name just a few of the functions). [Chapter 4](ch04.html), “ICMP,” discusses ICMP and its related functions in more detail.

# Domain Name System

Naming a thing is not the same as knowing a thing, but it is often the first step. I remember when I first started hearing about the Domain Name System (DNS). At the time, the major database software vendors were all talking about their distributed database products that would be available “real soon now,” and then the next thing I knew I was running distributed database software. It didn’t cost me a thing, and it worked from day one. DNS is a distributed database because the entire address table is not stored on a single host; instead, it is distributed across many servers.

At one point, the IP addresses and names were kept in tables that were downloaded nightly. As the Internet kept growing, this became impractical for a number of reasons related to the size of the table and issues surrounding single point of failure. Take a look at this excerpt of the static host file /etc/hosts maintained on a UNIX host:

```
/etc/hosts 
127.0.0.1     loopback 
172.20.1.41   relay relay.sans.org 
172.20.31.19  goo goo.sans.org 
```

Although UNIX and Windows 2000 hosts still maintain a small local hosts file to identify local and frequently used hosts, this function has been augmented by adding DNS capabilities. Most UNIX and Windows 2000 hosts are configured to search the host’s file first and if a host is not found there, to search DNS for the resolution for the host. This offloads most of the maintenance burden from the system administrator to individual administrators who maintain DNS servers.

Before jumping into the DNS, a discussion of DNS domains is needed. A domain is really just a logical division of DNS or the DNS database. The initial seven well-known “generic” domains have the three-letter endings such .com, .org, .edu, .net, and to a lesser extent .int, .gov, and .mil. The list of top-level domains has been expanded to include .aero, .biz, .coop, .info, .museum, .name, and .pro. There are also two-letter domains, which often appear as country codes (.us, .fr, and .uk for the United States, France, and the United Kingdom). Within each of those generic domains are the domains used every day (for example, yahoo.com and sans.org). Each of these domains represents a slice of the entire DNS pie.

Now that you have been introduced to the concept of DNS domains, how does DNS name resolution really work? At a very rudimentary level, there are basically two resolving routines: gethostbyaddr and gethostbyname. When you do some kind of DNS resolution, a host needs to either translate an IP number into a host name or a host name into an IP number. The real issue at hand is that people refer to hosts by their God-given host names, whereas computers refer to hosts by their binary-derived IP numbers. After all, there is no field in an IP datagram for the host name, only the IP number.

The gethostbyaddr call issued by your host delivers an IP number to a DNS server and tells it to resolve the host name and return it. There is much more to the process than meets the superficial eye, and this is discussed in [Chapter 6](ch06.html), “DNS.” Conversely, a gethostbyname call delivers a host name to a DNS server and requests resolution to an IP number. Understand that this explanation of DNS is a gross oversimplification of the processes and issues involved because it is intended to be a very introductory exposure.

# Routing: How You Get There from Here

Do you remember reading about TCP/IP as a four-layer protocol stack: application, transport, network, and link?

Some time was taken to explain what the application and transport layers do, but the explanation stopped at the network layer. Well, the network layer is concerned with routing and how to get from one host to another host regardless of the physical interconnection or the layout of the network. A better name for this layer might be the IP layer because this is the layer at which IP addresses are used and routing occurs. It is significant to understand that IP doesn’t concern itself with the underlying physical link.

You have already learned about the mechanism used to direct traffic to a host that resides on a network with the same network ID and subnet mask as the sending host. ARP is used to broadcast a request to all hosts on the local network asking one to respond with a MAC address that matches the desired destination IP number. How then is traffic directed to other networks since ARP is broadcast only on the local network? That is where routing comes in.

Each host has a routing table that knows about a default router. When the destination host is not on the local network, the traffic to be sent is directed to the default router. The router is responsible for forwarding the traffic one hop closer to its destination. This hop can be to another router or to the destination host itself if it resides on a network directly connected to the router’s interface. The question then becomes, how do routers know how to correctly direct the traffic and how do they receive updated information? After all, this has to be a dynamic process given that routes change because of problems and growth.

Routers maintain tables of routes that they know about. They use dynamic routing protocols to update their tables.

Routing protocols are divided into two major categories: Interior Gateway Protocols (IGPs) and Exterior Gateway Protocols (EGPs). The Interior Gateway Protocols support routing traffic within a network that is under the same administrative control, also known as an Autonomous System (AS). This is a fancy name for all the routers for which a site has responsibility. The Routing Information Protocol (RIP) is a widely deployed IGP. RIP is a simple protocol, which requires very little configuration and is supported by essentially every device. Another IGP is Open Shortest Path First (OSPF). These two protocols differ in the way that they receive routing updates and their perspective on finding best routes.

Exterior Gateway Protocols are required when packets must travel between different Autonomous Systems. These protocols bridge separate Autonomous Systems into a single network in which all of the computers on the network can interact seamlessly with each other. The Border Gateway Protocol (BGP) is a widely used Exterior Gateway Protocol. Currently, BGP provides the routing protocol that supports the Internet backbone. BGP servers on the Internet backbone must maintain routing tables that include all of the external addresses on the Internet—a pretty daunting task.

# Summary

A lot of new and diverse topics have been jam-packed into this introductory chapter. Details aside, you need to take away some core concepts with you to understand the upcoming chapters on TCP/IP.

First, visualize the transfer of data between two networked hosts as a series of layers, much like a stack. On the sending end, the message to be delivered is encapsulated in a series of headers as it is passed down the stack. On the receiving end, the process is reversed and the encapsulating headers are stripped and delivered to the associated layer of the stack for processing. Each layer on the sending host really communicates with its peer layer on the receiving host. Data is exchanged and packaged in different bundles with different names depending on the purpose of the data and the layer at which it is found in the TCP/IP stack.

Hosts are addressed as both IP numbers and MAC numbers at different layers of the TCP/IP stack. Remember that port numbers are used with TCP and UDP to designate a specific application, such as sendmail or telnet. TCP is the connection-oriented protocol that promises delivery, whereas UDP makes no such promise and is considered unreliable. DNS is used to translate host names to IP addresses and vice versa. Finally, routing is responsible for transporting the datagram from source to destination host. TCP/IP is a vast and complex topic.Various aspects of it will be examined in more detail in subsequent chapters of this part of the book.
