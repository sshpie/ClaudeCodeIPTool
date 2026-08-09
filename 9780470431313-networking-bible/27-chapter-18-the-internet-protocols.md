# Chapter 18. The Internet Protocols

**IN THIS CHAPTER**

- How the Internet Protocol is used to send packets
- How addresses are created and assigned
- Different network sizes and how to create subnets
- Create and use networks that have IPv6

The Internet Protocol, or IP, is the primary protocol used to provide an end-to-end delivery of packets over a TCP/IP network. Two versions of IP exist: IPv4, which is in widespread use, and IPv6, which is being phased in. Both are described in detail in this chapter.

IP is a transport-independent protocol that works over a wide variety of networks. It was designed to be connectionless, fault tolerant, and routable. There are four different types of IPv4 routing: unicast, broadcast, directed broadcast, and multicast. IPv6 expands multicast, eliminates broadcast, and adds an anycast routing function.

The address spaces of IPv4 and IPv6 are very different. IPv4 is a 32-bit address space where addresses are usually written in a dot decimal format, `###.###.###.###`. The address space can be divided into different-sized blocks by a masking technique, blocks can be subnetted, and other techniques such as NAT are used to extend the address space. Address assignment by DHCP is described in this chapter.

IPv6 is a 128-bit address space and has addresses that are usually written in a hexadecimal format, with eight blocks in the format, `nnnn:nnnn:nnnn:nnnn:hhhh:hhhh:hhhh:hhhh`, where `n` is the network ID and `h` is the host ID. There are different ways to express IPv6 addresses. IPv6 is autoconfigurable, and it allows for multiple addresses for each network interface. Addresses are scoped to belong to particular zones.

The reduced header size of IPv6 and the additional functionality built into the IPv6 and ICMPv6 protocols make IPv6 easier to implement on networks. A feature called Neighbor Discovery makes ad hoc networking, browsing, and router optimization particularly convenient.

It is believed that IPv4 will run out of available addresses by 2010 or 2011, making the adoption of IPv6 inevitable.

# Internet Protocol Overview

The Internet Protocol is the Network Layer protocol responsible for maintaining the endpoints of an Internet connection. IP defines the addressing scheme used by TCP packets and the encapsulation of the data into the datagram format that is transported over an internetwork. IP is a stateful, but connectionless, protocol. That is, while the endpoints are known and can be either real or virtual, the path between the endpoints is left undefined.

Because IP makes no demands on the connection, other than that the packets arrive without error, IP traffic can flow over different types of networks and can adapt to network conditions, switching routes as needed. The IP protocol was developed to work over packet-switched internetworks running Ethernet, ATM, FDDI fiber, 802.11*x* wireless, and other autonomous system (AS) networks, and to survive nuclear attacks where a large percentage of the network might be rendered inoperable. There are three defined ASNs:

- **Multihomed**. The AS has two or more independent connections to the internetwork.
- **Stub**. The AS has one connection to the internetwork and one connection to another AS.
- **Transit**. The AS has two independent connections to two different autonomous systems.

The Internet, as originally conceived, was meant to connect a number of different networks into routing groups, each with a unique prefix. Each routing prefix and the hierarchical tree it defined would be managed by an Internet Service Provider or another entity that was characterized by having multiple independent connections to the internetwork and a registered Autonomous System Number (ASN) in the IANA ASN database. The Border Gateway Protocol (BGP) uses the 16-bit address space of 65,536 ASNs to route traffic to each network on the Internet. The following assignments exist for ASNs:

- **0**. This is reserved for non-routable networks or local use.
- **1–54,271**. These are assignable for network use.
- **54,272–64,511**. These are reserved for IANA and may not be routed.

IANA has assigned all but 5,000 of these addresses and so needs a larger address space for future growth. They have adopted a 32-bit address space that adds a 16-bit word to the beginning of the original address space in the form: `new.old`. In the new scheme adopted in 2007, the old assignment of 12,345 would be written as 0.12345. The expanded 32-bit namespace reserves the ASNs 1.old and 65535.65535. All other ASNs are available.

Packet switching means that IP networks are routable, using either an Interior Gateway Protocol (IGP) or an Exterior Gateway Protocol (EGP). Decisions are made at each router and potentially at any device or host on the network that determine how a packet is forwarded. In order to resolve addresses for IP traffic flowing over heterogeneous networks, IPv4 uses the Address Resolution Protocol (ARP), and IPv6 uses the Neighbor Discovery Protocol (NDP).

### Note

IP routing is discussed in detail in [Chapter 9](ch09.html).

IPv4 traffic can be unicast, broadcast, or multicast, depending upon the destination address chosen. They have the following purposes:

- **Unicast**. A unicast packet is one that carries a single destination address such as 4.2.2.1, which might be a DNS request to the `Verizon.net` DNS server that my network uses.
- **Multicast**. Multicast packets are duplicated at the router and sent to multiple destinations. The IPv4 address range that is reserved for multicasts is 224.0.0.0–239.255.255.255.The range 224.0.0.0–224.0.0.255 is reserved for multicast link-local addresses — that is, addresses that are connected by the Data Link layer protocols but are not routable. Typically, link-local addresses are those that are autoconfigurable and on the same subnet.
- **Broadcast**. Sometimes you want to broadcast a packet to every host on a network (the local subnet, actually); to do this, you would send the message to the address 255.255.255.255. Broadcasts are used for polling, requests for service, and other operations.
- **Directed Broadcast**. If you want to broadcast to a specific subnet that is different from the sending host, you would send the message to an address, ###.###.###.255.

[Figure 18.1](ch18.html#the_four_types_of_ipv4_routing) illustrates these four forms of IPv4 routing.

![The four types of IPv4 routing](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1801.png)

**Figure 18.1. The four types of IPv4 routing**

# Internet Protocol Version 4

The first version of the Internet Protocol, version 4 (IPv4), is the dominant standard. It is recognized by the use of a quartet of octet addresses, ###.###.###.###, which is sometimes referred to as the dot decimal notation.

Let's consider a simple example of how IPv4 addressing works. If you `PING` `www.nytimes.com`, the address for the New York Times Digital Web site resolves to the server at 199.239.136.200. If you open up a browser such as Microsoft Internet Explorer and enter this address into the address bar, then you are taken to the New York Times Web site. You can convert IP addresses in the dot decimal format into other formats such as dotted hexadecimal, dotted octal, hexadecimal, decimal, and octal. The value for the decimal notation corresponding to `nytimes.com` is 3354364104, and if you enter this number into the address bar in Internet Explorer, it takes you to the New York Times Web site. Most browsers resolve the IP address in these alternate formats correctly.

## Addressing

IPv4's octet addressing scheme defines a 32-bit address space. Each of the four numbers can range from 0 to 255 (28), which defines a limit of 4,294,967,296 unique addresses in the address space. When the designers of IP developed the protocol, they could never have imagined how popular the protocol would become, and so it seemed eminently reasonable that four billion addresses could never be consumed. At the time that IPv4 was specified in 1980, the population of the entire world was estimated to be 4.5 billion people, and so the IPv4 standard allowed for an IP address for every person alive at the time. In an era when refrigerators, toasters, sensors, and almost anything you can think of takes an IP address, IPv4's days are numbered (so to speak). This problem has been called IP address exhaustion. By comparison, IPv6 defines a 128-bit address space, which defines 3.4 × 1038 unique numbers.

### Note

IPv4 is defined in IETF RFC 791, and in MIL-STD-1777.

To solve the problem of IPv4 address exhaustion, three different extensions to IP addressing have been introduced:

- Classless Inter-Domain Routing (CIDR)
- Variable Length Subnet Masks (VLSM)
- Subnet masking

These technologies are discussed in this chapter.

### Dividing the namespace

In the early 1980s when IP was being developed, the original namespace consisted of a network ID, which was the first three numbers or octet in the address, which was followed by the host ID of three more octets, for a total of four octets. The original scheme allowed for networks with a number from 0 to 255, or 256 networks in total.

#### Classes

As more networks were required, the designers of IP realized that while some networks might be large, most networks would be small, with some of intermediate size. The addressing scheme was changed so that the number of octets defining the network ID could vary between one and three octets, while the number of octets assigned to host IDs would vary between three and one octets. A network that required only one octet for the network ID would allow for 224 (16,777,216) hosts; one with two octets for the network ID would allow for 216 (65,536) hosts; and small networks where three octets were used to define the network would allow for only 28 (256) hosts. This is where the notion of network classes comes from. The original assignments for Classes A through E are shown in [Figure 18.2](ch18.html#ipv4_apostrophy_s_original_network_class).

![IPv4's original network class assignments](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1802.png)

**Figure 18.2. IPv4's original network class assignments**

Classes were meant to allocate blocks of addresses to organizations based on their size and on the type of traffic that the network carried, either unicast or multicast. So a set of contiguous network addresses could be doled out to an organization such as AOL, while a smaller set of contiguous network addresses could be doled out to the XYZ company. These classes aren't in use today, but they often crop up in network references and books due to their historical interest. In some instances, classes are used to describe the number of addresses in a subnet that a netmask allows, as is described later in this chapter. [Table 18.1](ch18.html#network_class_types) lists the different class types, as defined by RFC 791.

**Table 18.1. Network Class Types**

| Class | Leading Bits | Begin | End (Routing block-CIDR) | Default Subnet Mask |
| --- | --- | --- | --- | --- |
| Reference: `http://tools.ietf.org/html/rfc791` |  |  |  |  |
| **Class A** | 0 | 0.0.0.0 | 127.255.255.255 (/8) | 255.0.0.0 |
| **Class B** | 10 | 128.0.0.0 | 191.255.255.255 (/16) | 255.255.0.0 |
| **Class C** | 110 | 192.0.0.0 | 223.255.255.255 (/24) | 255.255.255.0 |
| **Class D (multicast)** | 1110 | 224.0.0.0 | 239.255.255.255 (/4) | NA |
| **Class E (reserved)** | 11110 | 240.0.0.0 | 255.255.255.255 (/4) | NA |

#### Classless Inter-Domain Routing

Classes became less relevant as the Internet became a public utility and the address space needed to be sliced and diced into millions of pieces. Classes eventually gave way to what is now called Classless Inter-Domain Routing (CIDR), and blocks of addresses are doled out to organizations and ISPs in all kinds of sizes. In the CIDR routing scheme published by IETF in 1993 (RFC 1518), IP addresses are assigned in a hierarchical structure that allows the addresses to be routed to the correct network, and if the address is routable, past the network portion to the correct host.

The CIDR removes the strict restriction that classes imposed, that networks be segregated based on the octet system, and in doing so, it makes it easier to route traffic on the Internet. The system creates what is called a Variable Length Subnet Mask (VLSM) and allows contiguous subnets to be aggregated into supernets. Aggregation has the effect of allowing addresses to be used more efficiently, and just as importantly, it reduces the number of router entries by hiding all of the subnets within a VLSM supernet as a single entry in the router table.

The CIDR scheme breaks the IPv4 address space into blocks that can be doled out, and represents those blocks. Each block is defined by appending a range number to an octet, in the form, ###.###.###.###/N, where N is a number from 0 to 32. (For IPv6, the range number is from 0 to 128.) The range number is in binary, and although it is appended to a dot decimal representation of the IP address, it is necessary to perform a conversion in order to establish the block size. Dot decimal is a 32-bit address space, and the numbers of N represent the excluded portion of the IP range. The larger the number, the smaller the range of addresses in the block.

To obtain the block size, you use the following formula: 232-N, which for the value 24 would yield 28 or 256 numbers (an octet), but for 18 would yield 214 or 16,384 addresses in the block. If you specified the address 199.239.136.200/24, then that CIDR block would include all addresses from 199.239.136.0 to 199.239.137.0, a full octet of numbers. The address 199.239.136.200/28 would have a range of 199.239.136.192 to 199.239.136.207, and any address from 199.239.136.217 and above would fall outside this block assignment.

[Table 18.2](ch18.html#cidr_block_sizes) lists the conversion of Classes to CIDR block prefixes. So you can see how the VSLM assignment allows for very efficient block assignments of any size.

**Table 18.2. CIDR Block Sizes**

| CIDR Block Prefix | Class Equivalency | Unique Nodes |
| --- | --- | --- |
| Block sizes smaller than /27 aren't usually assigned by an ISP. Block sizes larger than /13 are restricted to Regional Internet Registries. |  |  |
| **/28** | 1/16 Class C | 16 |
| **/27** | 1/8 Class C | 32 |
| **/26** | 1/4 Class C | 64 |
| **/25** | 1/2 Class C | 128 |
| **/24** | Class C | 256 |
| **/23** | 2 Class C | 512 |
| **/22** | 4 Class C | 1,024 |
| **/21** | 8 Class C | 2,048 |
| **/20** | 16 Class C | 4,096 |
| **/19** | 32 Class C | 8,192 |
| **/18** | 64 Class C | 16,384 |
| **/17** | 128 Class C | 32,768 |
| **/16** | 256 Class C or 1 Class B | 65,536 |
| **/15** | 512 Class C or 2 Class B | 131,072 |
| **/14** | 1,024 Class C or 4 Class B | 262,144 |
| **/13** | 2,048 Class C or 8 Class B | 524,288 |
| **/12** | 4,098 Class C or 16 Class B | 1,048,576 |

With the CIDR block assignments, it is no longer necessary to store routes to individual hosts in Internet routers. Instead, using routing prefix aggregation, routes are summarized into the supernets that the blocks represent. If you had four /26 contiguous blocks, that would represent 4 × 232-26, or 256 addresses. The designation of /26 represents a 1/4 C class network. In the routing table, a single entry for the starting IP address in the form ###.###.###.###/24 would be advertised, thus consolidating all of the blocks in the range.

For a larger supernet, consider the address ###.###.0.0/16, which uses a subnet mask of 255.255.0.0. The /16 indicates that this network is equivalent to 256 contiguous C class networks or one B class network, and defines an address space with 65,536 hosts. The router entry 200.100.0.0/16 is sufficient to represent all of these hosts within a single entry. It's easy to see the flexibility and economy that this system offers. This aggregation system has collapsed the global routing tables to approximately 35,000 entries. [Figure 18.3](ch18.html#aggregating_ip_names_using_the_cidr_sche) shows a hypothetical IPv4 address aggregation scheme.

![Aggregating IP names using the CIDR scheme](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1803.png)

**Figure 18.3. Aggregating IP names using the CIDR scheme**

#### Regional Internet Registries

The Internet is broken up into a set of geographical regions, each with their own large ranges, which are then further broken up into progressively smaller ranges. This hierarchy suppresses most of the entries that would exist if supernets weren't defined, and allows for very efficient routing based on both address and geography.

IP addresses are controlled by the Internet Assigned Numbers Authority (IANA), and the individual portions of the namespace hierarchy are organized into a set of regional databases or registries that segregate IP addresses on a geographical basis, as shown in [Figure 18.4](ch18.html#the_current_set_of_regional_internet_reg). Regional Internet Registries, or RIRs, are /8 or "Net-Eight" address blocks with 16,777,216 addresses, which corresponded to what was once called an A-class network. These RIRs list the IP assignments and provide a `WHOIS` lookup of the registry that enables the public to determine who a particular IP address is registered to. Among the services RIRs provide are:

- IPv4 and IPv6 address allocation
- `WHOIS`
- ASNs
- Internet Routing Registry
- Reverse DNS lookup

![The current set of Regional Internet Registries](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1804.png)

**Figure 18.4. The current set of Regional Internet Registries**

The acronyms in [Figure 18.4](ch18.html#the_current_set_of_regional_internet_reg) stand for:

- **ARIN**. American Registry for Internet Numbers (North America)
- **LA CNIC**. Latin American and Caribbean Internet Address Registry (Latin America and the Caribbean)
- **AFRINIC**. African Network Information Centre (Africa)
- **RIPE NCC**. Ripe Network Coordination Centre (Europe, the Middle East, and Central Asia)
- **APNIC**. Asia-Pacific Network Information Centre (Asia-Pacific)

### Note

The IP assignments in the RIRs are separate from domain names, which are registered with the ICANN.

### Reserved addresses

Not all of the addresses in the IPv4 address space are available for use; some ranges are set aside for use on private networks, while others are reserved for multicast networks. The different reserved addresses take the following forms:

- **(<*NetworkID*>, 0)**. This is reserved for the name of the network.
- **(<*NetworkID*>, -1)**. The -1 entry indicates that you replace all bits with 1s. This address is used to broadcast to the network.
- **(-1, -1)**. The all 1s address is used for local network broadcast.
- **(0, 0)**. This address indicates that the system is both the local network and the local system — essentially that it is "this host." It is encountered when a system sends a request to a BOOTP server to obtain a valid network address. It is also encountered as the entry in a router that points to the default router (also known as the default gateway).
- **(0, <*HostID*>)**. This address refers to the host that is assigned to the host ID number on the local network.
- **(127, <*all*>)**. This address represents the loopback adapter; all traffic is sent to the loopback adapter.

A private network, as defined in RFC 1918, is one that cannot be used on the Internet and is not routable. Any packet that comes from a device with an address in the private network ranges will be dropped by a router on the Internet.

Most LANs used in homes and offices use private IP address ranges, either for IPv4 or using the IPv6 private address ranges that have been defined. Incoming traffic to a private network must pass through a gateway or a proxy server, and requires a mechanism such as Network Address Translation (NAT) to forward incoming packets to the correct address. The use of NAT has taken some of the pressure off of moving to IPv6, but only for a while. As the IPv4 address space becomes filled, IP networking will slowly migrate to the second version of the protocol, version 6 (IPv6).

### Note

Care should be taken when two or more networks use the same private network subnet so that conflicts do not occur.

The localhost or local computer describes the loopback network interface. The loopback adapter's address range is also private. The localhost refers to an address that belongs to the host device, or more accurately, to the network interface. When packets are directed (`PING`ed) to the localhost, they are returned with an incoming address that is the same as the outgoing packets, just as if they traveled on a virtual network. For this reason, the localhost is referred to as the loopback adapter or a loopback device. The loopback adapter is used to test that the network interface is up and running. The most common way of testing the loopback adapter is to use the command `PING 127.0.0.1`. The IANA has a number of other address blocks that are reserved for private use, or kept in reserve for other purposes. [Table 18.3](ch18.html#iana_reserved_addresses) lists some of the reserved blocks.

**Table 18.3. IANA Reserved Addresses**

| Address Block | Block Size (addresses) | Used For | RFC |
| --- | --- | --- | --- |
| Reference: `www.iana.org`. |  |  |  |
| 0.0.0.0/8 | 24 (16,777,216) | Local network (used locally) | 1700 |
| 10.0.0.0/8 | 24 (16,777,216) | Private | 1918 |
| 14.0.0.8/8 | 24 (16,777,216) | Public (private before February 2008) | 1700 |
| 127.0.0.0/8 | 24 (16,777,216) | Loopback | 3330 |
| 128.0.0.0/16 | 16 (65,536) | Reserved by IANA | 3330 |
| 169.254.0.0/16 | 16 (65,536) | Link local | 3927 |
| 172.16.0.0/16 | 16 (65,536) | Private | 1918 |
| 191.255.0.0/16 | 16 (65,536) | Reserved for IANA | 3330 |
| 192.0.0.0/24 | 8 (256) | Reserved for IANA | 3330 |
| 192.0.2.0/24 | 8 (256) | Documentation and sample code | 3330 |
| 192.88.99.0/24 | 8 (256) | IPv6–IPv4 relay | 3068 |
| 192.168.0.0/16 | 16 (65,536) | Private | 1918 |
| 198.18.0.0/15 | 17(131,072) | Network testing | 2544 |
| 223.255.255.0/24 | 8 (256) | Reserved for IANA | 3330 |
| 224.0.0.0/4 | 28 (268,435,456) | Multicast (D class) | 3171 |
| 240.0.0.0/4 | 28 (268,435,456) | Reserved (E class) | 1700 |
| 255.255.255.255 | 0 (1) | Broadcast |  |

In the old class network designations, the address ending in 0 was assigned as the network identifier, while the address ending in 255 was reserved for broadcasts to all of the systems on the subnet. For example, you would not assign the addresses 192.168.0.0 or 192.168.0.255 for a C class block defined by that range.

With the advent of the CIDR scheme, the situation changes and only networks that have a subnet mask between /24 (255.255.255.0) and /32 (255.255.255.255) would reserve these addresses. In a subnet defining a larger block, only the first address and the last address need to be reserved. So if you considered the block 100.100.0.0/16, the subnet mask would be 255.255.0.0, and the number of allowed addresses would be 65,536 and would define a range from 100.100.0.0 up to 100.100.255.255. In that range, 100.100.0.0 and 100.100.255.255 must be reserved, but any other numbers ending in 0 or 255 would be allowed. Examples of allowed numbers in this range would be 100.100.1.0 and 100.100.254.255.

### Zero Configuration addressing

Link-local addresses are used for local networks and cannot be routed. If you are using a dynamic IP assignment from a DHCP server, then you may see an address in the range 169.254.0.0 to 169.254.255.255 when the DHCP server is unavailable and no address can be assigned. In IPv4, the link-local range 169.254.0.0/16 is assigned using a mechanism called IPv4 Link-Local or IPV4LL, which is specified in RFC 3927.

It is common to have link-local addresses assigned by automatic addressing services for local use, through a technology that is sometimes referred to as Zero Configuration Networking. Zeroconfig or Zeroconf is a service that supplies IP addresses on a network without the use of any server such as DHCP or BOOTP. Zeroconfig is responsible for the following services when it is enabled:

- Assign link-local addresses to networked devices
- Perform name resolution
- Provide a browse function
- Automatically discover network services such as printing

Microsoft's service discovery technology is called the Simple Service Discovery Protocol, and it is part of the Universal Plug and Play (UPnP) protocol. Apple's service discovery technology is called Multicast DNS/DNS-SD (mDNS). This area of technology is one that has yet to be standardized, although the IETF has proposed a standard called the Service Location Protocol (SLP), which has appeared on both Linux and Solaris. Microsoft and Apple continue to use their own technology.

You probably know these technologies by their branded names. The Apple version of the Zeroconfig is Bonjour (formerly Apple Rendezvous). The Microsoft version of this addressing scheme is called the Automatic Private IP Address (APIPA) or the Internet Protocol Automatic Configuration (IPAC) system. On Linux and BSD, the Avahi version of Bonjour can be deployed.

Recently, it has become a practice by some systems to adopt IANA reserved ranges for their internal use. For example, the Hamachi VPN service uses the 5.0.0.0/8 network range for their nodes. Because VPN is encapsulated traffic, the network addresses are hidden within routable packets; they are not exposed on the Internet and dropped. Provided that two private networks don't share the same address range, although IANA private network use is discouraged, it doesn't cause any problems.

### IP datagrams

The IP header is added to the beginning of TCP data and consists of a number of standard fields that identify the source, destination, and format of the IP protocol used. Of the 13 fields, all except the optional field are required. By convention, the IP protocol writes data in big endian format. Big endian is the format used by the Sun SPARC processors, and by the Motorola processors that used to run older versions of the Macintosh. The Intel X86 architecture uses a little endian format, which means that when an IP is either sent to or received on an Intel system, the data must be converted from big endian to little endian.

In big endian notation, the most significant bit is written first, that is, bit endian numbers have the highest-order bits written first. In the IP header diagram shown in [Figure 18.5](ch18.html#ip_header_structure), the first field for version stores the value for decimal "4", which translates to 0100 in binary. Big endian writes the value in the order of left to right.

The fields in the IP header are used for the following purposes:

- **Version**. This is the 4-bit value for the IP version number: 4 or 6.
- **Internet Header Length (IHL)**. This field accounts for the use or lack of an Options field and sets the overall header length. When combined with the Fragment Offset, it allows the data portion to be reliably read.
- **Type of Service (TOS)**. This field is meant to be used to specify a Quality of Service type, and has seen little use. The current use of the TOS field is to assign a Differentiated Services (DiffServe) or Explicit Congestion Notification (ECN) value that will assign IP priorities in streaming media services.This 8-bit field allows assignments of precedence, delays, throughput, and reliability. When streaming data is sent, throughput is emphasized and reliability is deemphasized. For file transfers, the opposite settings might be used.
- **Total Length**. This defines the size of the total datagram, up to 216 bytes (65,535). The minimum value required is 576, and when a packet requires more than 216 bytes, the datagrams are split into fragments.
- **Identification**. The Identification (ID) field is used to identify the fragment order of a split IP datagram.
- **Flags**. There are three 1-bit fields that are flag settings; the first always takes a zero value, and the other two indicate whether the datagram can be fragmented (Don't Fragment, or DF) as well as if there are additional fragments (More Fragments, or MF). The DF field aids in routing or suppressing fragmented packets. When data is fragmented, all of the packets have the MF field set to 1, except for the final packet.
- **Fragment Offset**. The Fragment Offset field indicates where the data in a packet fits into the original unfragmented IP datagram's sequence. In any fragmentation, the first packet takes an offset value of zero, and this field allows for 13 bits of 8-byte units, or 65,528 bytes. That allows for 8,192 fragments per datagram.
- **Time To Live**. The Time To Live (TTL) 8-bit field is a limitation that tells a host or router whether or not to continue to forward the packet. Originally this setting referred to seconds, but it has been changed to indicate the number of hops that a packet can take. Every time the packet is forwarded, the field is decremented by one, and when the field is set to zero, it is dropped by the next router. When TTL expires, the last host or router sends an ICMP message that the packet exceeded its TTL.
- **Protocol**. IP can carry a number of different protocols. This 8-bit field carries the IANA protocol assignment. Some of the more common assignments are 0, IPv6 hop-by-hop; 1, ICMP (Internet Control Message Protocol); 2, IGMP (Internet Group Management Protocol); 6, TCP (Transmission Control Protocol); 17, UDP (User Datagram Protocol); 27, RDP (Reliable Datagram Protocol); 89, OSPF (Open Shortest Path First); 129, SMP (Simple Message Protocol); and 133, FC (Fibre Channel).
- **Header Checksum**. This 16-bit field contains a checksum that is matched at each hop in the route. When a host or router finds that the checksum doesn't match the checksum it calculates based on the header's contents, it drops the packet. The checksum is only used for the transport of the packets; TCP, UDP, and other transport and application protocols use their own checksums to determine the validity of the data once it arrives.The checksum algorithm examines each 16-bit word in the header, a half word at a time, takes the complement, and sums all of the complements to obtain a result. That result is then complemented, and then this result is used in the checksum. To complement means that you change any 1 to 0 and vice versa.
- **Source Address**. This is the IPv4 address written in binary code.The translation works as follows: for the address 192.168.1.1, you would have the four binary octets 11000000.10101000.00000001.00000001, which would populate this 32-bit field with the string 11000000101010000000000100000001.NoteThe address that you sniff in the Source Address field is the address of the sender. This address can be altered by Network Address Translation (NAT) to be the address of the translator device. Source addresses can also be spoofed by various methods.
- **Destination Address**. The destination address is the same type of 32-bit binary address that was entered into the Source Address field.
- **Options**. The Options field allows for additional information to be added to a packet, and was included to allow for changes and additions to the IP. This field can be left blank, or the various options can be added. Options start with a single byte that represents the option type, followed by data for that option. The Option field ends with a 0 x 00 value representing the End of Options List (EOL). An EOL is only required when the Options field doesn't complete the header because the Options field must be a multiple of four bytes. [Table 18.4](ch18.html#ip_options) lists the current options. Any option not supported by a router or host is ignored.Alternate uses of the Options field include a set of options that set the security level, specify a complete path (Strict Source Routing) or required set of routers (Loose Source Routing), have routers add their address to the header (Record Route), and add a timestamp (Timestamp) for each router address that has been appended. These fields are deprecated; security restrictions on many modern routers drop packets that contain these older options.
- **Data**. The data portion of the datagram is the payload portion of the packet. This is data in the form indicated by the Protocol field, most often TCP or UDP data.

![IP header structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1805.png)

**Figure 18.5. IP header structure**

**Table 18.4. IP Options**

| Field | Bits | Purpose |
| --- | --- | --- |
| The Copied, Option Class, and Option Number fields can be combined into an 8-bit field called the Option Type. |  |  |
| **Copied** | 1 | The value is 1 when the option field needs to be included in all packet fragments. |
| **Option Class** | 2 | The value 0 indicates a control option, the value 2 indicates debugging and measurement, and values 1 and 3 are reserved. |
| **Option Number** | 5 | Indicates an option. |
| **Option Length** | 8 | The size of the option with the length field included. This is not always used. |
| **Option Data** | Variable | Option data. This is not always used. |

Refer to [Table 18.5](ch18.html#iana_protocol_numbers) to view the different supported protocol types.

**Table 18.5. IANA Protocol Numbers**

| Decimal | Keyword | Protocol |
| --- | --- | --- |
| **0** | HOPOPT | IPv6 Hop-by-Hop Option |
| **1** | ICMP | Internet Control Message |
| **2** | IGMP | Internet Group Management |
| **3** | GGP | Gateway-to-Gateway |
| **4** | IP | IP in IP (encapsulation) |
| **5** | ST | Stream |
| **6** | TCP | Transmission Control |
| **7** | CBT | CBT |
| **8** | EGP | Exterior Gateway |
| **9** | IGP | Any private interior gateway |
| **10** | BBN-RCC-MON | BBN RCC Monitoring |
| **11** | NVP-II | Network Voice |
| **12** | PUP | PUP |
| **13** | ARGUS | ARGUS |
| **14** | EMCON | EMCON |
| **15** | XNET | Cross Net Debugger |
| **16** | CHAOS | Chaos |
| **17** | UDP | User Datagram |
| **18** | MUX | Multiplexing |
| **19** | DCN-MEAS | DCN Measurement Subsystems |
| **20** | HMP | Host Monitoring |
| **21** | PRM | Packet Radio Measurement |
| **22** | XNS-IDP | XEROX NS IDP |
| **23** | TRUNK-1 | Trunk-1 |
| **24** | TRUNK-2 | Trunk-2 |
| **25** | LEAF-1 | Leaf-1 |
| **26** | LEAF-2 | Leaf-2 |
| **27** | RDP | Reliable Data |
| **28** | IRTP | Internet Reliable Transaction |
| **29** | ISO-TP4 | ISO Transport Protocol Class 4 |
| **30** | NETBLT | Bulk Data Transfer |
| **31** | MFE-NSP | MFE Network Services |
| **32** | MERIT-INP | MERIT Internodal |
| **33** | DCCP | Datagram Congestion Control |
| **34** | 3PC | Third Party Connect |
| **35** | IDPR | Inter-Domain Policy Routing |
| **36** | XTP | XTP |
| **37** | DDP | Datagram Delivery |
| **38** | IDPR-CMTP | IDPR Control Message Transport Proto |
| **39** | TP++ | TP++ Transport |
| **40** | IL | IL Transport |
| **41** | IPv6 | IPv6 |
| **42** | SDRP | Source Demand Routing |
| **43** | IPv6-Route | Routing Header for IPv6 |
| **44** | IPv6-Frag | Fragment Header for IPv6 |
| **45** | IDRP | Inter-Domain Routing |
| **46** | RSVP | Reservation |
| **47** | GRE | General Routing Encapsulation |
| **48** | DSR | Dynamic Source Routing |
| **49** | BNA | BNA |
| **50** | ESP | Encap Security Payload |
| **51** | AH | Authentication Header |
| **52** | I-NLSP | Integrated Net Layer Security TUBA |
| **53** | SWIPE | IP with Encryption |
| **54** | NARP | NBMA Address Resolution |
| **55** | MOBILE | IP Mobility |
| **56** | TLSP | Transport Layer Security Protocol using Kryptonet key management |
| **57** | SKIP | SKIP |
| **58** | IPv6-ICMP | ICMP for IPv6 |
| **59** | IPv6-NoNxt | No Next Header for IPv6 |
| **60** | IPv6-Opts | Destination Options for IPv6 |
| **61** |  | Any host internal protocol |
| **62** | CFTP | CFTP |
| **63** |  | Any local network |
| **64** | SAT-EXPAK | SATNET and Backroom EXPAK |
| **65** | KRYPTOLAN | Kryptolan |
| **66** | RVD | MIT Remote Virtual Disk |
| **67** | IPPC | Internet Pluribus Packet Core |
| **68** |  | Any distributed file system |
| **69** | SAT-MON | SATNET Monitoring |
| **70** | VISA | VISA |
| **71** | IPCV | Internet Packet Core Utility |
| **72** | CPNX | Computer Protocol Network Executive |
| **73** | CPHB | Computer Protocol Heart Beat |
| **74** | WSN | Wang Span Network |
| **75** | PVP | Packet Video |
| **76** | BR-SAT-MON | Backroom SATNET Monitoring |
| **77** | SUN-ND | SUN ND PROTOCOL-Temporary |
| **78** | WB-MON | WIDEBAND Monitoring |
| **79** | WB-EXPAK | WIDEBAND EXPAK |
| **80** | ISO-IP | ISO Internet |
| **81** | VMTP | VMTP |
| **82** | SECURE-VMTP | SECURE-VMTP |
| **83** | VINES | VINES |
| **84** | TTP | TTP |
| **85** | NSFNET-IGP | NSFNET-IGP |
| **86** | DGP | Dissimilar Gateway |
| **87** | TCF | TCF |
| **88** | EIGRP | EIGRP |
| **89** | OSPFIGP | OSPFIGP |
| **90** | Sprite-RPC | Sprite RPC |
| **91** | LARP | Locus Address Resolution |
| **92** | MTP | Multicast Transport |
| **93** | AX.25 | AX.25 Frames |
| **94** | IPIP | IP-within-IP Encapsulation |
| **95** | MICP | Mobile Internetworking Control Pro |
| **96** | SCC-SP | Semaphore Communications Sec. Pro. |
| **97** | ETHERIP | Ethernet-within-IP Encapsulation |
| **98** | ENCAP | Encapsulation Header |
| **99** |  | Any private encryption scheme |
| **100** | GMTP | GMTP |
| **101** | IFMP | Ipsilon Flow Management |
| **102** | PNNI | PNNI over IP |
| **103** | PIM | Protocol Independent Multicast |
| **104** | ARIS | ARIS |
| **105** | SCPS | SCPS |
| **106** | QNX | QNX |
| **107** | A/N | Active Networks |
| **108** | IPComp | IP Payload Compression |
| **109** | SNP | Sitara Networks |
| **110** | Compaq-Peer | Compaq Peer |
| **111** | IPX-in-IP | IPX in IP |
| **112** | VRRP | Virtual Router Redundancy |
| **113** | PGM | PGM Reliable Transport |
| **114** |  | Any 0-hop protocol |
| **115** | L2TP | Layer Two Tunneling |
| **116** | DDX | D-II Data Exchange (DDX) |
| **117** | IATP | Interactive Agent Transfer |
| **118** | STP | Schedule Transfer |
| **119** | SRP | SpectraLink Radio |
| **120** | UTI | UTI |
| **121** | SMP | Simple Message |
| **122** | SM | SM |
| **123** | PTP | Performance Transparency |
| **124** | ISIS over IPv4 |  |
| **125** | FIRE |  |
| **126** | CRTP | Combat Radio Transport |
| **127** | CRUDP | Combat Radio User Datagram |
| **128** | SSCOPMCE |  |
| **129** | IPLT |  |
| **130** | SPS | Secure Packet Shield |
| **131** | PIPE | Private IP Encapsulation within IP |
| **132** | SCTP | Stream Control Transmission |
| **133** | FC | Fibre Channel |
| **134** | RSVP-E2E-IGNORE |  |
| **135** | Mobility Header |  |
| **136** | UDPLite |  |
| **137** | MPLS-in-IP |  |
| **138** | manet | MANET |
| **139** | HIP | Host Identity |
| **140-252** |  | Unassigned |
| **253** |  | Use for experimentation and testing |
| **254** |  | Use for experimentation and testing |
| **255** | Reserved |  |

As IPv4 packets are transported over the network, the packet headers are verified using a CRC checksum, and if the header doesn't pass verification the packet is dropped. In most instances, nothing more happens and the source is required to send a duplicate packet when the destination sends a message the packet didn't arrive. When Quality of Service methods are in place, it is possible to use the Internet Control Message Protocol (ICMP) to signal when a packet was dropped.

# Subnetting

When our favorite company XYZ gets a block of IPv4 network addresses, those network addresses are logical entities, essentially pointers to the hosts that are assigned to them. The problem with this approach is that many networks are composed of different parts that are on different physical networks, separated by geography, separated by a low-bandwidth (for example, WAN) connection, belong to more than one domain and thus have different security settings, or have some other reason why you might want to address each group separately. Just the simple act of aggregating more addresses on the same ASN results in slower routing as traffic is sorted, and in much less efficient throughput due to higher network traffic and collisions. These are all reasons why networks are subdivided.

A subdivided network is called a subnet, which is short for subnetwork, although you almost never hear the latter term in use. Subnets are created by applying a "subnet mask" to the network address space. A subnet mask is a bit mask that hides the network identification portion of a network, along with any range of host values you specify. It's a simple and elegant system for carving up a network.

Let's consider a common example that you are probably familiar with, what was once called a C-class network consisting of 256 contiguous network addresses. Most private networks set their systems up with this size of network. In a private network with the range 192.168.1.0 to 192.168.1.255, which is referred to as 192.168.1.0/24 in CIDR, a subnet mask of 255.255.255.0 is applied to hide the network identification. This mask allows any of the 256 values for the host that are possible with the last octet. Suppose that you wanted to create two separate but equal-sized subnets from this range. To do this, you would apply a subnet mask of 255.255.255.128 to your systems, and any address belonging to the range 0-127 would be in subnet 1 and any address in the range of 128-255 would be in subnet 2. You can verify this by entering the information into `Subnet-Calculator.com`.

### Tip

The Subnet Calculator at `www.subnet-calculator.com` can be used to calculate subnet masks, bits, hosts, and other factors or to check your calculations. The site also offers a CIDR calculator.

The systems on each subnet are invisible to one another. However, all systems are visible from outside the network, regardless of any subnets that you define. That's why subnetting a network doesn't require that you change network interface settings or alter registrations in address databases that are outside your network.

Subnetting is a lot less mysterious than it might seem at first, if you think in terms of binary addressing. What subnet masking does is take bits that were part of the host's identification portion of the network block and mask them off so that those bits appear to be part of the network identification portion; as a result, those bits can't be changed. [Figure 18.6](ch18.html#subnetting_a_solidus_24_network_into_two) shows how this example looks in binary numbers. Note that the subnet mask suppresses the available range in the last octet.

![Subnetting a /24 network into two identical subnets](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1806.png)

**Figure 18.6. Subnetting a /24 network into two identical subnets**

Should you want to carve a /24 network into more subnets, you can use the subnet mask values in [Table 18.2](ch18.html#cidr_block_sizes) to do so. Every bit that is masked beyond the network identification portion of the address is referred to as the subnet identifier. In [Figure 18.6](ch18.html#subnetting_a_solidus_24_network_into_two), the subnet identifier is 1. Referring to [Table 18.6](ch18.html#subnetting_a_solidus_24_network), the network identifier for the subnet mask 255.255.255.240 would be 4.

**Table 18.6. Subnetting a /24 Network**

| Last Octet in Dot Decimal | Last Octet in Binary | Unique Hosts[[a]](ch18.html#ftn.CHP-18-TFN-1) | Number of Possible Subnets | Effective CIDR |
| --- | --- | --- | --- | --- |
| [[a]](#ftn.CHP-18-TFN-1) |  |  |  |  |
| [[b]](#ftn.CHP-18-TFN-2) |  |  |  |  |
| 255 | 11111111 | NA[[b]](ch18.html#ftn.CHP-18-TFN-2) | NA[[b]](ch18.html#ftn.CHP-18-TFN-2) | /32 |
| 254 | 11111110 | 2 (point to point) | 128 | /31 |
| 252 | 11111100 | 2 | 64 | /30 |
| 248 | 11111000 | 6 | 32 | /29 |
| 240 | 11110000 | 14 | 16 | /28 |
| 224 | 11100000 | 30 | 8 | /27 |
| 192 | 11000000 | 62 | 4 | /26 |
| 128 | 10000000 | 126 | 2 | /25 |
| 0 | 00000000 (no mask) | 256 | 1 (no subnet) |  |
| [[a]](#CHP-18-TFN-1)The unique hosts are reduced by two due to the reserved 0 and 255 values required in classful addressing. CIDR removes this restriction in almost all cases.[[b]](#CHP-18-TFN-2)These are usually not defined at the router. |  |  |  |  |

Subnets are numbered based on the length of the subnet mask and incremented based on the number of subnets you create. With no network identifier defined, the network is left unaffected and you see the Base network. In a C-class network with eight subnets defined, the subnets are labeled from 0 to 7, as shown in [Figure 18.7](ch18.html#the_subnet_numbering_scheme_for_an_8-sub).

When you create a subnet, you alter the routing tables to include subnet information. As packets come in, they are compared with the subnet mask to determine which subnet they reside on. Only the unmasked portion of the host's identification needs to be considered. The router then sends the packets onto the router responsible for that subnet, where the packet is then sent onto its destination.

![The subnet numbering scheme for an 8-subnet partitions C-class network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1807.png)

**Figure 18.7. The subnet numbering scheme for an 8-subnet partitions C-class network**

# Setting an IP Address

It's important to be able to find your network interface IP configuration, and to change it when necessary. There are five main methods for setting a device's IP address:

- **Command Line Interface**. From the command line using a command such as `IPCONFIG` for Windows or `IFCONFIG` for Linux/UNIX/Solaris/Macintosh.The use of switches such as `/ALL` produce a verbose listing of addresses, and you can use other switches such as `/RELEASE` or `/RENEW` to change a dynamically assigned network address. Check your help system or `MAN` pages for more details.NoteThe various command line utilities rarely show IPv6 address zone information if zones are defined.
- **Graphical User Interface utility**. Typically a control panel utility found in nearly all GUI operating systems.
- **Menu or browser-based systems**. Devices such as routers, switches, and network appliances use these systems.
- **Dynamic network service such as DHCP (version 4 or 6) or BOOTP**. All network hosts and devices are capable of being a DHCP client; BOOTP clients are restricted to enabled hosts.
- **The Neighbor Discovery Protocol for IPv6**. This Link Layer protocol finds other nodes on an IPv6 link and determines the addresses of the neighbors as well as which router and routes or paths are best used to communicate with them.

An assigned IP address is stored in a number of different places. During a session, the IP address is retained in memory (RAM). In many cases, it is recorded to one or more system files, of which the HOSTS file is a prime example.

In the two sections that follow, you will learn about static IP addresses and dynamic IP addresses. A static IP address is one that you assign that remains unchanged over time. Static IP addresses are required for certain types of servers and may be used on small networks. Dynamic IP addresses are assigned by a network service and are both flexible and configurable. Dynamic IP addresses are used in networks where a pool of IP addresses must be used, in mobile devices, and in many other instances.

## Static addressing

A static IP address is one that is assigned to a host or device that doesn't change with time. When you set a static address, that address stays fixed unless you physically go and change it. Some network devices require a static address to function correctly: DHCP and DNS servers, network gateways, routers, Web servers, and domain servers, to mention just a few. These systems require that devices always be able to find them at the same address whenever their services are required. For hosts and other devices that aren't required to provide services to other devices, there is no significant advantage to using static addressing.

On small networks of a dozen hosts or devices, the necessity of organizing static IP addresses so that there are no duplicate assignments or remembering which system belongs to which address is not an onerous task. There is no compelling reason not to use static IP addresses, and doing so allows you to hard-code these addresses into your HOSTS file.

On my home network, I set the following static IP addresses:

- **Host ID = 1**. This address is assigned to the network gateway.
- **Host ID = 2**. This address is assigned to the DNS server, when one is used.
- **Host ID = 3**. This address is assigned to the domain server, when one is used.
- **Host IDs = 4–20**. These addresses are used for any other device that provides a standard network service.
- **Host IDs = 21–80**. These addresses are assigned to clients.
- **Host IDs = 81–99**. I reserve these static addresses for wireless devices such as access points or routers.
- **Host IDs = 100–110**. I use these addresses for the address assignments of my TiVo's network interface.
- **Host IDs = 150–200**. These addresses form the pool of dynamic IP addresses that the DHCP server can use.

You'll notice that even though this scheme tends more often than not to assign static IP addresses to hosts, I don't religiously assign all network devices static IP addresses, nor would I want to. There are many instances when a new network device is introduced, or when a network interface loses its IP address for some reason (an operating system install, for example). In those instances, DHCP assigns an address from its pool. This scheme works for me because the network is small. If I had more than 16 to 20 network addresses to assign, I would use DHCP more extensively, and in large networks, most systems are assigned dynamic IP addresses.

To summarize, you need static IP addresses for the following systems:

- For fixed network services such as routers
- For network devices that must be accessible from outside of your network: Web servers, e-mail servers, FTP servers, and other application servers
- For some terminal service applications
- In some licensing schemes where the license is tied to a specific IP address (rare)
- For streaming services where the connection endpoints must be permanently set

## Dynamic addressing

You do not need static IP addresses for clients that are requesting services, such as browsing the Internet, sending and receiving e-mail, using an Instant Messaging service, downloading or uploading files, and similar tasks. Dynamic IP addressing offers the advantage of automatically providing address configuration, which can be a very time-consuming task on a network of any significant size (greater than 50 devices). It frees the network administrator from having to remember to reset an address when a system is moved from one subnet to another.

Against these conveniences is the requirement that the dynamic address assignment service (DHCP) and the name resolutions service (DNS, for example) must be running at all times in order for the network to function correctly. However, once a dynamic address is assigned to a device, that device retains the address and only loses the assignment when the address assignment service recognizes that the device has lost its address "lease." The lease is a dynamic IP address' "Time To Live" feature.

There is a minor security benefit to be gained by using dynamic addressing. If a hacker gains access to a system on your network at a known IP address, that address will not be available to them over time if it is a dynamic address.

# Dynamic Host Configuration Protocol

The Dynamic Host Configuration Protocol (DHCP) is a network broadcast service that assigns and manages dynamic IP addresses on DHCP clients. DHCP servers can be found in network switches, routers, network appliances, and on all network operating systems whether run on a server or workstation. The service is normally turned off by default so that networks don't run into the problem of having multiple conflicting DHCP servers running at the same time. DHCP also needs to be enabled on the client side in many cases.

A DHCP client sends a broadcast request when it first connects to the network or at timed intervals that are configurable. Any listening DHCP servers on the network are requested to either supply or update its Internet Protocol information. A DNS server responds to the query, validates the request, and then provides the necessary configuration parameters. Once the address is accepted, the client may initiate an ARP query to determine if the address is unique. The address process, often referred to as ROSA (for Request, Offer, Selection, and Acknowledgment), is illustrated in [Figure 18.8](ch18.html#dhcp_apostrophy_s_rosa_process). An assigned address is removed from the address pool, as shown by the strike-out text in the address listing at the lower left of [Figure 18.8](ch18.html#dhcp_apostrophy_s_rosa_process).

![DHCP's ROSA process](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1808.png)

**Figure 18.8. DHCP's ROSA process**

DHCP configuration supplies the following pieces of information:

- IP address
- Subnet mask
- Domain name
- DNS server(s) address
- Default gateway (outbound router, proxy server, and so on)

## Configuration

DHCP servers are most often set up to provide dynamic addresses. When an address is assigned from the DHCP address pool, the address has a lease during which time the address is valid. That lease can be long — 30 days is typical in enterprises — or it can be short, often on the order of 48 hours when the DHCP address is assigned by an ISP to a remote client over a broadband connection or through a Point-to-Point Protocol (PPP) dial-up or ISDN connection. Every so often, the server polls the clients for their DHCP settings, or a client queries the server to find out if its settings are still valid. If the lease has expired, the server either refreshes the address or offers a different set of addresses for the client to select from.

Different DHCP services handle these details in different ways. Large ISPs supporting many remote clients typically reassign an address for a lease that expires if the client doesn't respond to its polling. They do this because they know that the client will check its DHCP settings the next time that they connect. Although DHCP is almost always a dynamic address service, it is often possible to configure DHCP so that the address is automatically supplied to a client permanently. In some instances, the client can manually select the address from the pool, as is shown in [Figure 18.8](ch18.html#dhcp_apostrophy_s_rosa_process); this is uncommon, however.

Some DHCP servers support a feature called *static allocation*, where any assigned IP address records the MAC address of the client in a lookup table. Some systems do this automatically; others require that the administrator manually enter the MAC address. Static allocation is not a standard feature, and if you implement it, you need to ensure that not only does your DHCP server offer it, but that any routers on your network that the DHCP client needs also support the feature. There is a plethora of names used to describe static allocation, including the following:

- Cisco (and now Linksys, too) calls it Static DHCP.
- Older Linksys routers such as WRT54G (54GL and 54GS) wireless routers using the DD-WRT Linux firmware call it Static DHCP assignment.
- MAC/IP binding.
- Reserved IP Address (see [Figure 18.9](ch18.html#the_dhcp_configuration_web_page_for_a_ne)), or IP reservation.

![The DHCP configuration Web page for a Netgear FVS318 router/firewall](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1809.png)

**Figure 18.9. The DHCP configuration Web page for a Netgear FVS318 router/firewall**

## Securing DHCP

DHCP offers no security mechanisms to protect a network against unauthorized address assignment, and requires vigilance on your part to ensure that your network doesn't have either an unauthorized DHCP server or client on the network. This is one of the reasons that you need to take care that you don't install a second DHCP server on the network inadvertently. An unauthorized DHCP server can provide a means for unauthorized clients to gain access to your network; and it is easier to have an unauthorized DHCP server on the network than you might think. DHCP is included on so many devices that it is easy to check the wrong box on a router setup wizard or move a server with an active DHCP service onto another subnet.

There is an authentication method that has been developed for DHCP (`http://tools.ietf.org/html/rfc3118`), and while you may find it available in your DHCP server and it is widely supported, most organizations don't adopt the Authentication for DHCP Messages option. When security is a concern, most networks adopt authentication using the IPsec protocol suite. You can also provide some security to the network by ensuring that the DNS server that provides name resolution only provides this service to systems whose network interface MAC addresses are registered as belonging to the IP address that they display, using static allocation as described in the previous section.

### Note

IPsec is described in [Chapter 27](ch27.html).

Many firewalls and routers provide a DHCP server, as you can see in [Figure 18.9](ch18.html#the_dhcp_configuration_web_page_for_a_ne). DHCP traffic is transported over UDP. If your firewall or router needs to support DHCP for incoming or outgoing traffic, you will probably need to enable this feature as well as open the following ports: Outgoing DHCP port 68 (UDP) and Incoming DHCP port 67 (UDP) at the firewall, and Outgoing DHCP port 67 (UDP) and Incoming DHCP port 68 (UDP) at the client. Incoming broadcast packets with source 0.0.0.0 and destination 255.255.255.255 must be allowed, as must outgoing packets from the DHCP server if the ROSA system is allowed to work. These are the same ports that BOOTP uses.

## Bootstrap Protocol

The Bootstrap Protocol, or BOOTP, is a predecessor to the DHCP service, and is still in use today. BOOTP works similarly to and is compatible with DHCP. BOOTP is a UDP network protocol that assigns an IP address upon request during the bootstrap part of a system's startup, whereas DHCP must first load an operating system and the DHCP client before it can issue the address request. BOOTP broadcasts are sent by instructions in the Read Only Memory (ROM) of a network interface card (NIC) or from instructions in the motherboard's BIOS. The BOOTP service sends an address to the system.

BOOTP is significantly easier to use and requires little if any setup to implement. Unlike DHCP, which allows for reconfiguration once the system is running, BOOTP works only in the startup phase. It is used most often in thin clients of terminal servers where the client is a diskless workstation where the operating system is loaded as part of the boot process after the address is obtained.

# Internet Control Message Protocol

The Internet Control Message Protocol (ICMP) defines the message system used to acknowledge or request actions and events related to IP data transfer. It is important for controlling traffic and congestion, signaling if a packet has arrived correctly or needs to be resent, and controlling routing. The Time To Live (TTL) parameter expiration is one event that generates an ICMP error message.

ICMP is required for the proper functioning of the IP protocol and must be correctly operating for IP communications to function. There are two versions of this protocol, one for IPv4 and another for IPv6; IPv6 is described toward the end of this chapter.

ICMP messages are generated from IP datagrams that require an ICMP action. IP encapsulates the ICMP header that contains the error, and adds the appropriate destination to the message field in the header. Because ICMP is carried over a single datagram, it doesn't require the verification features of TCP and is usually sent over UDP transport. That makes ICMP an unreliable messaging format. The message type is indicated by a field inserted into the IP header after bit 160, or later if the IP header Options field has been populated. [Figure 18.10](ch18.html#the_icmp_header_structure) shows the structure of an ICMP header.

![The ICMP header structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1810.png)

**Figure 18.10. The ICMP header structure**

The essential fields that define the ICMP message are the type and code fields. These fields are standardized by the IANA and are described in Table.

**Table 18.7. ICMP Types**

| Type | Code | Description |
| --- | --- | --- |
| Source: `www.iana.org/assignments/icmp-parameters` |  |  |
| 0 - Echo Reply | 0 | Echo Reply (used by `PING`) |
| 1 |  | Destination Unreachable (ICMPv6) |
| 2 |  | Packet too big (ICMPv6) |
| 3 - Time Exceeded |  | Time exceeded (ICMPv6) |
| 3 - Destination Unreachable | 0 | Destination network unreachable |
|  | 1 | Destination host unreachable |
|  | 2 | Destination protocol unreachable |
|  | 3 | Destination port unreachable |
|  | 4 | Fragment required, Don't Fragment (DF) flag set |
|  | 5 | Source route failed |
|  | 6 | Destination network unknown |
|  | 7 | Destination host unknown |
|  | 8 | Source host isolated |
|  | 9 | Network administratively prohibited |
|  | 10 | Host administratively prohibited |
|  | 11 | Network unreachable for Type of Service (TOS) |
|  | 12 | Host unreachable for TOS |
|  | 13 | Communication administratively prohibited |
| 4 - Source Quench | 0 | Source quench for congestion control |
| 4 - Parameter Problem |  | Parameter Problem (ICMPv6) |
| 5 - Redirect Message | 0 | Redirect Datagram for the network |
|  | 1 | Redirect Datagram for the host |
|  | 2 | Redirect Datagram for TOS and network |
|  | 3 | Redirect Datagram for TOS and host |
| 6 |  | Alternate Host Address |
| 7 |  | Reserved |
| 8 - Echo Request | 0 | Echo request (used by `PING`) |
| 9 - Router Advertisement | 0 | Router Advertisement |
| 10 - Router Solicitation | 0 | Router discovery/solicitation/selection |
| 11 - Time Exceeded | 0 | TTL expired en route |
|  | 1 | Fragment reassembly time exceeded |
| 12 - Parameter Error: Bad IP Header | 0 | Pointer error |
|  | 1 | Missing an option |
|  | 2 | Bad length (checksum error) |
| 13 - Timestamp | 0 | Timestamp |
| 14 - Timestamp Reply | 0 | Timestamp reply |
| 15 - Information Request | 0 | Information request |
| 16 - Information Reply | 0 | Information reply |
| 17 - Address Mask Request | 0 | Address Mask request |
| 18 - Address Mask Reply | 0 | Address Mask reply |
| 19 |  | Reserved for security |
| 20–29 |  | Reserved for fault tolerance testing |
| 30 - Traceroute | 0 | Information request |
| 31 |  | Datagram conversion error |
| 32 |  | Mobile host redirect |
| 33 |  | Where are you? (IPv6) |
| 34 |  | Here I am! (IPv6) |
| 35 |  | Mobile registration request |
| 36 |  | Mobile registration reply |
| 37 |  | Domain name request |
| 38 |  | Domain name reply |
| 39 |  | Simple Key Management for Internet Protocol (SKIP Algorithm Discovery Protocol) |
| 40 |  | Security failures |
| 41 |  | Experimental mobility protocols |
| 42–99 |  | Reserved |
| 100 |  | Private experimentation |
| 101 |  | Private experimentation |
| 102–126 |  | Reserved |
| 127 |  | Reserved for future ICMPv6 information messages |
| 128 |  | Echo request (ICMPv6) |
| 129 |  | Echo reply (ICMPv6) |
| 130–199 |  | Reserved |
| 200 |  | Private experimentation |
| 201 |  | Private experimentation |
| 255 |  | Reserved for future ICMPv6 information messages |

# Internet Protocol Version 6

The second version of the Internet Protocol, version 6 (IPv6), is the successor to IPv4. IPv6 was designed to provide a significantly larger address space, better granularity (self-autoconfiguration and improved routing), and improved security. For the most part, all of the Internet Protocols that work with IPv4 work with IPv6. Some Application layer protocols, such as FTP or NTPv3, that encapsulate IP network addresses fail to make the transition without being reworked due to the very different structure of IPv4 and IPv6 headers.

IPv6 solves a lot of problems that have made IPv4 networking a difficult proposition. IPv6 headers are simpler and have a native Quality of Service (QoS) mechanism, called flow labeling, built into them. The incredibly large address space means that subnets become an abstraction and not a necessity, and that Network Address Translation (NAT), which is the bane of many protocols trying to traverse a router, disappears. Just eliminating NAT removes a significant portion of network configuration errors. Voice over IP (VoIP), BitTorrent, Session Initiation Protocol (SIP), and other streaming and peer-to-peer protocols all have difficulty with NAT on IPv4 routers because they can't identify their target systems.

Routing has been greatly improved in IPv6. There are improved multicasting, anycasting, and unicasting routing mechanisms. In many instances, you don't even need routers to create LANs. Because the various subnets on an IPv6 are embedded in the network prefix, network traffic can be directed to the correct host on the correct subnet by the address alone. This ad hoc network is specific to a site and does require a router for outside traffic.

The IPv6 Neighbor Discovery (ND) Protocol can not only discover neighboring hosts and devices, but it can also discover network prefixes and the address autoconfiguration method, perform address resolution, find the next hop, detect duplicate addresses, and determine whether a neighbor is available or offline. ND consolidates these many important functions into a core networking protocol that can work in the background automatically.

Because autoconfiguration of addresses is built into IPv6, DHCP becomes largely irrelevant, although a version of DHCPv6 does exist. Autoconfiguration of IPv6 addresses is normally done by sending a query to the router. You can configure link-local addresses to be unique in IPv6, which eliminates the problem of having network collisions when two hosts on connected networks use the same IPv4 address.

In order to send IPv6 packets over an IPv4 network, it is necessary to encapsulate IPv6 packets within IPv4. This is known as tunneling, and can be set up as either an automatic system or by using predefined configured tunneling. Other tunneling methods can use UDP packets as the link layer protocol, or the ISATAP protocol to make an IPv4 network appear as if it is an IPv6 local-link. One technology, called Toredo, uses automatic tunneling over UDP to transport IPv6 packets across NAT routers. Toredo is found in Windows XP SP2 IPv6, Windows Vista, Windows Server 2003 and 2008, and Mac OS X Leopard. These technologies are meant to bridge the transition of networking from IPv4 to IPv6 and allow IPv6 to be more easily deployed in dual-stack networks.

### Note

IPv5 was assigned to a streaming protocol for audio and video traffic and was unavailable for use as an IP addressing protocol.

IPv6 has turned out to be much more slowly adopted than any of its developers would have predicted due to the technologies described in the previous sections: NAT, CIDR, and subnetting in particular. However, it is only a matter of time until IPv6 becomes the dominant IP addressing protocol. IANA tracks the usage of IPv4 and has predicted that unallocated IPv4 addresses will be exhausted around May 2010 and that the Regional Internet Registries would use up their address allocations by April 2011. So if all the good reasons I've given you don't convince you that IPv6 is worth your time, then consider that at some point you will simply have no choice but to adopt it.

## Addressing

IPv6 defines a 128-bit address space, which is an almost inconceivably large number. The host portion of the address is either assigned as a sequential number or derived from the network interface MAC address. The network identification and the host identification portions of the address are both 64 bits wide and are always kept separate from one another. This separation means that when you add an entry for an IPv6 network identifier into a router, it then defines the entire network. Just this one simple fact, that one network prefix routes the entire network, means that the router tables on IPv6 networks are greatly reduced compared to IPv4 networks, which leads to much better router performance. The reduced complexity of the IPv6 header is another factor in improving router performance.

In standard hexadecimal notation, a Global Unicast IPv6 address would be written as eight 4-digit groups, each separated by a colon, as follows:

```
2001:0db8:3c4d:0015:0000:0000:abcd:ef14
```

where `2001:0db8:3c4d:` is the global prefix, `0015:` is the subnet ID, and `0000:0000:abcd:ef14` is the host identifier (network interface).

There is no need to specify a subnet or the network identification of any routers along the path to that network. The addition of the network identification changes the routing for the entire set of systems on that IPv6 network.

The network classes used in IPv4 no longer apply in IPv6. A block of contiguous network addresses defining a single network can be defined by the size of the prefix. The following two addresses represent the start and end of a network range:

```
2001:0db8:3c4d:0000:0000:0000:0000:0000
2001:0db8:3c4d:ffff: ffff: ffff: ffff: ffff
```

You can use CIDR to indicate the size of the network prefix, just as you would in IPv4. In the addresses above, this would allow you to write this network block in the following form:

```
2001:0db8:3c4d::/48
```

Recall that IPv6 is a 128-bit address space, and that each of the eight blocks in the address represents 16 bits of data as written in the form of four hexadecimal characters. The three network prefix blocks indicate that the CIDR mask size is /48. This still leaves 280 or 1.21 × 1024 addresses that can be assigned. Larger CIDR values reduce the number of unique addresses that are assignable, but the size of IPv6 is so vast that even a full 64-bit network prefix still leaves 264 or 1.84 × 1019 unique addresses — over 3 billion addresses for every living person on Earth.

Subnetting doesn't disappear in IPv6 networks; however, its usefulness as anything other than a comparative metric loses its meaning. Typically a /48 network is used by large organizations allowing the 80-bit address space mentioned previously. A small network might use a /56 prefix, which allows for a 72-bit address space. A /48 network can define 65,536 (216) subnets, while a /57 network would allow for 128(27) subnets. Because autoconfiguration requires a full 60 bits in the address for assignment, you never see subnetting in IPv6 use more than the allowed 60 bits, which is not subnetted.

All IPv6 hosts must support the following features:

- Link-local addresses
- Multicast to all other nodes
- Unicast
- Anycast
- Selective multicast
- Loopback address (::1)

These various forms of routing are described in more detail later in this section.

### IPv6 compressed notation

If you think that an IPv6/IPv4 address is weird, check out the full address that is used for the localhost:

```
0000:0000:0000:0000:0000:0000:0000:0001
```

It would be ugly to have to enter all of these zeros, and thankfully IPv6 doesn't require you to do so. IPv6 has a feature that is called compressed notation. With compressed notation, you can simply eliminate any block in the address that is all zeros. This compresses the localhost address down to the shortcut `::1`, which is pretty handy. Similarly, you can compress the IPv6/IPv4 composite address that you saw a couple of paragraphs ago to the compressed notation `::192.168.1.52`.

Compressed notation can also be applied to any blocks that have all zeros, but that are inside the address. The zero blocks do not have to be leading zeros. For example, the address

```
2001:0db8:3c4d:0015:0:0:abcd:ef14
```

may be shortened to

```
2001:0db8:3c4d:0015::abcd:ef14.
```

Compressed notation allows you to remove only one group of zeros, and with good reason. If you consider the address

```
2001:0:0:0015:0:0:0:ef14
```

compressed to

```
2001::0015::ef14
```

you would not be able to discern whether the address should be expanded to

```
2001:0:0:0:0: 0015:0: ef14,
```

or

```
2001:0:0:0: 0015:0:0: ef14,
```

or

```
2001:0:0: 0015:0:0:0: ef14,
```

or

```
2001:0: 0015:0:0:0:0: ef14.
```

If you understand these few principles of compressed notation, then you can see that the following addresses are all equivalent to one another:

```
2001:0db8:0000:0000:0000:0000: abcd:ef14
2001:0db8:0000:0000:0000:: abcd:ef14
2001:0db8:0:0:0:0: abcd:ef14
2001:0db8:0:0:: abcd:ef14
2001:0db8:: abcd:ef14
2001:db8:: abcd:ef14
```

which at first glance would be wildly confusing.

You may encounter compressed notation with a CIDR suffix appended to it. For example, an address such as `2001:0db8: abcd::ef14/128` indicates that the address has only one interface route. A different suffix, such as `/48`, indicates another router configuration for that address.

### IPv6 calculators

There may be creatures somewhere who actually live in IPv6 address space. You can identify them by eight digits that they have on their two hands and feet, or some other combination that adds up to 32.

Because I have stopped growing digits some time ago, I prefer to rely on one of the many Web sites, utilities, or lookup tables that exist to support the various forms of IP-related conversions. One that I've used is called Bitcricket, and is shown in [Figure 18.11](ch18.html#bitcricket_may_be_used_to_do_ipv4_solidu). This utility can calculate subnets for IPv4/IPv6 and for CIDR routes, as well as perform conversions between dotted decimal, decimal, hexadecimal, dotted hexadecimal, dotted binary, and binary numbers. The program is available in both Windows and Macintosh formats, and can be obtained from `www.bitcricket.com/ip-subnet-calculator.html`.

[Figure 18.11](ch18.html#bitcricket_may_be_used_to_do_ipv4_solidu) shows the IPv6 page of the Bitcricket utility with the different defined interfaces enumerated.

An alternative IP6 calculator utility for Linux/UNIX is IPv6calc, which can be downloaded from `www.deepspace6.net/projects/ipv6calc.html`.

![Bitcricket may be used to do IPv4/IPv6 conversions and discovery.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1811.png)

**Figure 18.11. Bitcricket may be used to do IPv4/IPv6 conversions and discovery.**

### Dual-stack IPv6/IPv4 addresses

The address space for IPv6 and IPv4 is not backwards compatible, and so, although you can run both protocol versions on the same computer or network, they operate independent of one another. Because most of the world is using IPv4 addresses, IPv6 would be useless if it didn't encode for an IPv4 address. To create an IPv4 address in the IPv6 address format, you would write it in the following manner:

```
0000:0000:0000:0000:0000:0000:192.168.1.52
```

Notice that the address above has only seven blocks defined by the colon delimiters and that I told you that an IPv6 address requires eight blocks. The reason that the IPv6/IPv4 address has only seven blocks is that the IPv4 block encodes for 32 bits and not the normal 16 bits for each of the IPv6 blocks. That means that the IPv4 portion of the IPv6 address is a double block.

IPv6 can use what have been generally called compatible addresses, where you mix six higher-order groups of hexadecimal digits with four groups of decimal digits in the low-order octets that IPv4 uses. Using this scheme, let's look at an address of the form

```
h:h:h:h:h:h:d.d.d.d
```

where `h` is a high-order byte and `d` is a low-order byte. This form of address allows for the following substitution:

```
::ffff:192.168.2.52
```

which in the original address is equivalent to the following notation:

```
::ffff: c0a8:0234
```

This type of notation for a dual-stack address is not universally supported, and so you will want to check first before using it.

### Address scopes and zones

An IPv6 address is defined for a particular address scope. One way to think of an address scope is that it represents the connection's endpoint limits for that network interface. A connection can span a region defined as a local link, site, or global network. If you examine IPv6 addresses on a system, you may find that there is a link-local address and a global address for the same network interface. Although a network interface must have at least one unicast IPv6 address, you can define as many IPv6 addresses to an interface as you desire.

The different address scopes that have been defined are:

- **Link-local address**. These are private network non-routable addresses and are confined to a single network or subnetwork. These addresses can be supplied by autoconfiguration technologies such as SLAAC and DHCPv6, both of which are described later in this section.
- **Unique local address**. Unique local addresses (ULAs) are private network, non-routable addresses that are guaranteed to be unique. When two network segments with these types of addresses are joined, there are no host IP address conflicts.
- **Global unicast address**. These addresses are public network addresses and are routable to other networks.

The site-local address scope defined by the original RFCs was phased out as of 2004 and is no longer in widespread use.

Any network interface connected to a particular address scope is part of a scope zone. Scope zones require that each network interface have a unique address within that zone. Addresses do not have to be unique across different zones. When you examine an IPv6 address returned from an `IPCONFIG /ALL` command in Windows, it takes the following form:

```
Link-local IPv6: fe80::1198:de1d:9fb3:bd11%8(Preferred)
```

The title indicates that this address is scoped to the link-local zone. The address is the string `fe80::1198:de1d:9fb3:bd11`, while the `%8` indicates the zone index number `8`. The definition of a zone obviates the need for network broadcasts, and the prefix `fe80` is the local scoping. A link-local address has the same routing prefix, `fe80::/10`.

Consider the situation of a dual-homed host with two link-local addresses, the first at `fe80::a/64` and the second at `fe80::b/64`. Both of these interfaces connect to a network that has a host at `fe80::c/64`. The host at `fe80::c/64` wants to send packets to the dual-homed host at `fe80::a/64`, but because the `fe80::b/64` interface share the same link-local address, there is no way to tell which interface (`a/64` or `b/64`) that `fe80::c/64` should send the packets to. This is the problem that address scoping solves. You alter the link-local addresses to include the zone in the following manner:

```
<IPv6_Address>%<Zone_Index>
```

Different operating systems indicate the Zone Index in different ways: Microsoft Windows IPv6 uses integers such as `%1`; and Linux/UNIX use the interface name, `%eth0.`

Multicasting, which is a required field in the IPv6 header, may be used to send a packet to all of the hosts in a zone, such as the local-link `all hosts` multicast group. Multicast in IPv6 replaces broadcast that was part of IPv4. Multicasting sends packets to every network interface that is a member of the multicast group, as registered at a router; if no members are listed at that particular router, the packets are dropped. Multicasting doesn't suffer from the defect that broadcasting does, where unintended recipients receive what is called a broadcast storm.

An IPv6 host can send packets to multiple network interfaces that all have the same IPv6 anycast address. In anycast communication, any node with the destination anycast address can accept the packet, and whichever node happens to hear the packet first takes delivery. Delivery is to the nearest or best node and represents an approach toward improving reliability and failover in replicated systems. Anycast combines elements of unicast, multicast, and broadcast; probably the best way to think about anycast is that it is a shared set of unicast links.

### Note

Anycasting and other IP routing technologies are discussed in detail in [Chapter 9](ch09.html). Many DNS servers on the Internet use anycast for replication.

IPv6 anycast is supported by a specific type of address that includes a set of fields to support anycasting. To have anycast packets arrive correctly, you need to set the various network interfaces to the appropriate anycast address, and IPv6 manages the delivery of packets to those various interfaces.

[Table 18.8](ch18.html#ipv6_iana_address_ranges) lists the IANA IPv6 address ranges. Many of the ranges are reserved by the IETF for future use or experimentation. Of the following ranges listed in the table, only `0000::/8, 2000::/3, FC00/7, FE80::/10`, and `FF00::/8` are publicly available as either a loopback address or broadcast range.

**Table 18.8. IPv6 IANA Address Ranges**

| Prefix | Allocation |
| --- | --- |
| Reference: `www.iana.org/assignments/ipv6-address-space`. The RFCs that define the IPv6 address space include 1881, 1888m 3879, 4048, 4147, 4193, 4291, and 4548. |  |
| `0000::/8` | Reserved by IETF. The "unspecified address," the "loopback address," and the IPv6 Addresses with Embedded IPv4 Addresses are assigned out of the `0000::/8` address block. `0000::/96` was previously defined as the "IPv4-compatible IPv6 address" prefix. This definition has been deprecated. |
| `0100::/8` | Reserved by IETF |
| `0200::/7` | Reserved by IETF. `0200::/7` was previously defined as an OSI NSAP-mapped prefix set. This definition has been deprecated. |
| `0400::/6` | Reserved by IETF |
| `0800::/5` | Reserved by IETF |
| `1000::/4` | Reserved by IETF |
| `2000::/3` | Global Unicast, addresses that are publicly routable. The IPv6 Unicast space encompasses the entire IPv6 address range with the exception of `FF00::/8`. IANA Unicast address assignments are currently limited to the IPv6 Unicast address range of `2000::/3`. IANA assignments from this block are registered in the IANA registry: `iana-ipv6-unicast-address-assignments`. |
| `2001::/32` | The address `2001:0DB8::/32` is reserved for examples and documentation, as in EXAMPLENET-WF. |
| `3fff:ffff::/32` | These addresses are reserved for examples and documentation. |
| `4000::/3` | Reserved by IETF |
| `6000::/3` | Reserved by IETF |
| `8000::/3` | Reserved by IETF |
| `A000::/3` | Reserved by IETF |
| `C000::/3` | Reserved by IETF |
| `E000::/4` | Reserved by IETF |
| `F000::/5` | Reserved by IETF |
| `F800::/6` | Reserved by IETF |
| `FC00::/7` | Unique Local Unicast |
| `FE00::/9` | Reserved by IETF |
| `FE80::/10` | Link-Local Unicast |
| `FEC0::/10` | Reserved by IETF. `FEC0::/10` was previously defined as a Site-Local scoped address prefix. This definition has been deprecated. |
| `FF00::/8` | Multicast |

There are two methods in use for address autoconfiguration with IPv6: the Stateless Address Autoconfiguration (SLAAC) and the DHCPv6, which is stateful. An IPv6 system initiates stateless discovery by sending an ICMPv6 router solicitation request as a multicast packet when it connects to a link-local zone. The IPv6-enabled router returns a router advertisement packet with the required configuration details. Not every IPv6 device can use this stateless mechanism to obtain an IPv6 address; routers, for example, require a stateful assignment. DHCPv6 can be used to supply IPv6 configuration information to clients that has been manually entered into the configuration table and allows the administrator to send additional information that is not discoverable by SLAAC. For the most part, autodiscovery on IPv6 networks uses SLAAC, while DHCPv6 is rarely used. When neither mechanism works correctly, the link-local address is supplied to the network interface as a default backup.

## IPv6 datagrams

IPv6 datagrams are both larger and simpler than their IPv4 counterparts. The header portion of the packet is shown in [Figure 18.12](ch18.html#ipv6_header_structure). Notice that IPv6 doesn't use IP header checksums to verify the validity of a transmitted packet; instead, it relies on other protocols to determine the validity. This has the effect of making IPv6 faster than IPv4.

![IPv6 header structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1812.png)

**Figure 18.12. IPv6 header structure**

The different fields in the IPv6 header have the following purposes:

- **Version**. This is indicated by a four-bit representation of the number 6 (0110).
- **Traffic Class**. This field provides a packet priority range that is used to control packet traffic based on network conditions. Network messages indicate the amount of congestion on the network that needs to be accommodated.
- **Flow Label**. This is a QoS label that is defined for real-time services and is meant to serve the same function as the Service Type field in IPv4. This field is not in current use.
- **Payload Length**. This indicates the size of the payload in bytes. A field setting of all zeros indicates that the packet is a "Jumbogram," which is a packet that can be anywhere from 64KB up to 4GB in size. Jumbo frames require specific network hardware support and a Maximum Transmission Unit (MTU) network protocol that supports their large sizes in order to be used.
- **Next Header**. This is equivalent to the Protocol field in the IPv4 header. It can also be used to add an additional header to the packet.
- **Hop Limit**. This is the number of network hops that are allowed. This is the current replacement for the Time-To-Live parameter that is used in IPv4.
- **Source Address**. This is the IPv6 128-bit address of the source.
- **Destination Address**. This is the IPv6 128-bit address of the destination.

## IPv6 Neighbor Discovery

The IPv6 Neighbor Discovery (ND) Protocol is an IPv6-only protocol that consolidates a number of important functions found in a number of IPv4 protocols, as well as adding a number of new ones. The protocol's name only provides insight into a small part of this handy technology's features. Through ND, a number of network parameters can be discovered and configured, and the IP protocol's basic functions are supported.

The Internet Protocol is a Network layer protocol in the ISO/OSI model, and the primary Internet Layer protocol of the Internet Protocol Suite. IP is responsible for datagram delivery and addressing, routing, and network interface configuration. In IPv4, the Address Resolution Protocol (ARP) provides a broadcast discovery method, and the Internet Control Message Protocol (ICMP) provides the messaging system between network hosts and devices that allows for acknowledgment, traffic control, Quality of Service, and other functions. Many of these functions are consolidated in IPv6 in ND.

As shown in [Figure 18.13](ch18.html#the_different_functional_components_of_t), ND includes router discovery and redirection, features that are part of ICMPv4. Address resolution in ND adds additional functionality to the services that the ARP provides and that IPv4 supplements. ND uses ICMPv6 messages such as Router Advertisement and Router Solicitation, Echo Request and Echo Reply, Neighbor Advertisement and Neighbor Solicitation to discover network elements. These commands and the information that they carry work with IPv6 messages such as Redirect and Router Renumbering to build optimized IPv6 routing tables.

![The different functional components of the Network Discovery (ND) Protocol in IPv6](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1813.png)

**Figure 18.13. The different functional components of the Network Discovery (ND) Protocol in IPv6**

The most important functions that ND offers are the following:

- **Address resolution**. A router address query can return a valid network ID to a host at startup or when required. Multicast is used for address resolution, which is more efficient than the broadcasts that ARP uses in IPv4.
- **Autoconfiguration**. ND provides the message function that allows router configuration queries and can return network parameters.
- **Next Hop Determination**. When one host sends packets to another host, ND examines the datagram header to determine if a router is required or if the communication can be direct. When local, the communication is direct. When it is determined that the address isn't on the link-local network, ND selects the correct router that is the "next-hop." In most instances, packets use the host's local destination cache to determine where datagrams should be sent. When a next hop determination is made (which is infrequently) for a particular datagram, the destination cache is updated.
- **Redirection**. The redirect function in ND analyzes the route assigned to datagrams to determine if the best route was selected. If a better route is available, ND creates an ICMPv6 Redirect message that changes the routing for any future datagrams with a connection containing the same endpoints.
- **Router discovery and selection**. The message function in ND allows the protocol to discover which routers are on the network, and constantly updates this information. The dynamic selection of routers and available devices that the router knows about allows ND to determine which nodes are active and online and which routers are used for forwarding messages to outside the network.
- **Security**. ND runs at the Network layer and can be transported over an IPsec connection.

## ICMPv6

ICMPv6 offers some additional capabilities that aren't part of ICMPv4's definition. As you can see in [Table 18.7](ch18.html#icmp_types), there are additional message types that are defined for error messages (1, 2, 3, 4, 100, 101, and 127) and for informational messages (128, 129, 200, 201, and 255) that are specific to ICMPv6. Because IPv6 contains additional routing functions, ICMPv6 has some additional requirements that must be met, including the following:

- A message that was the result of a unicast routing must have a reply sent to the sending host.
- If the message is a response to a multicast group address, to an anycast address, or to a unicast address that doesn't have an assigned mode, then the source address must be a unicast address that belongs to a node.

The biggest difference between ICMPv4 and ICMPv6 is that the additional message categories were added to support the ND Protocol that is described in the previous section. Of these, the Neighbor Solicitation and Neighbor Advertisement messages provide the discovery mechanism that ND uses to populate its browse functionality. The Router Solicitation and Router Advertisement messages support the ND redirection function that allows for more intelligent routing initiated by network hosts. Redirect messages are sent as a unicast to the device that sent the datagram that initiated the redirect.

A function called Router Renumbering sends messages containing a list of router prefixes to the routers that are to be renumbered. Using the renumbering feature, a router can check the other router prefixes to see if packet prefixes match any of the renumbered routers, and if they do, it forwards the packets to that router. Router renumbering is supported by the Router Renumbering Command and by the Router Renumbering Result message. Because this mechanism allows for the mass renumbering of routers, there are mechanisms built into this feature, such as a test mode and a Sequence Number Reset message, that are meant to prevent the abuse of these router optimization functions.

# Summary

In this chapter, you learned about the Internet Protocol and the central role that it plays in TCP/IP networking. IP provides the end-to-end delivery of packets but does not specify the connection or the method of transport.

IPv4 uses a 32-bit addressing scheme. You learned how addresses specify networks and interfaces, and how addresses can be manipulated to define networks and subnets. The different methods for automatic assignment of IPv4 addresses were described.

IPv6 is the more recent version of IP. It has a 128-bit address space, a simplified header, and improved routing functions. The methods used to address devices on IPv6 networks, create and work with networks, and interoperate in mixed IPv4/IPv6 dual-stack networks were described.

The next chapter describes name resolution services that translate addresses into friendly network names.
