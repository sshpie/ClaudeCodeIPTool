# Chapter 17. Network Architecture Fundamentals

**IN THIS CHAPTER**

- **Understanding different types of networks**
- **Reviewing Network Address Translation**
- **Discussing basic network architecture issues**
- **Understanding subnets and switching**
- **Understanding system design for insider threat**

Network communication has been a very significant development over the past 25 years. In particular, the 1990s saw a huge expansion of public access and public-oriented communication networks that had the ability to bind the entire world into a single network. Current networking technology has its roots in military and academic research projects initiated in the 1970s. Thus, networks are no longer a prerogative for the exclusive, but an essential tool and object in the routine life of everybody. The architecture of public networks and, more important, the Internet is very complex and sophisticated. Some of the vital applications and components incorporated into present day networks include the following:

- Web browsing
- File transfers
- E-mail
- Remote logins
- Multimedia
- Telephony
- Security services

Organizations such as the IETF and IEEE continually endeavor to enhance these vital components of public networks. This chapter focuses on some of the basic network components used in the present Internet and other network technology (most important, network security services).

# Network Segments

Over the past few years, there has been a heavy integration of network technologies, which has created highly unified and global network architectures. Yet business, commercial, and military requirements demand segregation of network segments into authorized domains or network segments. The boundaries of such network segments are established by devices capable of regulating and controlling the flow of packets into and out of the segment, including the following:

- Routers
- Switches
- Hubs
- Bridges
- Multi-homed gateways

These segments can be theoretically classified into the following:

- Public networks
- Semi-private networks
- Private networks

## Public networksxs

Public networks allow accessibility to everyone. The common Internet is a perfect example of a public network. On public networks there is a huge amount of trivial and unsecured data. Users normally pay for public network services, and security controls on these networks are weak. Most of the networks you find at Internet cafés, airports, hospitals, shopping malls, and so on are examples of public access networks. Typically, security measures for public access networks are quite restricted. A one-time password would be all that is required to log into publicly available machines and public access networks. Despite the lack of security, large volumes of unprotected data are transmitted worldwide over public networks because of their convenience and the variety of services they provide.

## Semi-private networks

Semi-private networks sit between public networks and private networks. Sometimes this is referred to as a DMZ which stands for de-militarized zone. From a security standpoint, a semi-private network may carry confidential information but under some regulations. Semi-private networks are most often exclusive subnets of large public networks such as the Internet. Large peer-to-peer networks that are designed to handle and share exclusive information (usually multimedia) among its users can also be classified under semi-private networks. A virtual private network uses public networks optimized with security features that only privileged users can use successfully.

## Private networks

Private networks are organizational networks that handle confidential and propriety data. Each organization at every geographical location may own a private network. If the organization is spread over vast geographical distances, the private networks present at each location may be interconnected through the common Internet or other public networks. Generally, most commercial organizations prefer not to lay down dedicated lines over vast geographical distances, mainly because of cost factors. Private networks may have exclusive addressing and protocols and do not have to be compatible with the Internet. Address translation schemes and various tunneling protocols could be used to have incompatible private and public networks interoperate.

# Perimeter Defense

In most cases, internal networks are composed of various network component blocks. Following are the most important of these:

- Application servers
- Proxy servers
- Middleware servers
- Data servers
- Presentation servers

Securing such enormous processing units often requires security solutions to be highly fortified at the network in addition to using individual server-based security systems. In most common environments, firewalls would be placed at the terminal ends of every network segment. Firewalls (independent or combined with routers) can be ideal choices for securing network perimeters. Demilitarized zones can be defined around the periphery for enhanced security features. Specialized application proxies normally placed at the boundaries of network environments can also function as perimeter defense systems. [Figure 17-1](ch17.html#perimeter_defense_strategies_employed_on) shows a comprehensive view of a network protected by perimeter systems (usually firewalls).

# Network Address Translation

Network Address Translation (NAT) is a scheme employed by organizations to defy the address deficiency of IPv4 networking. It basically translates private addresses that are normally internal to a particular organization into routable addresses on public networks such as the Internet. In particular, NAT is a method of connecting multiple computers to the Internet (or any other IP network) using one IP address. Though NAT's main goal is to increase the scope of IP addresses (this necessity is addressed to a great extent by IPv6 network architectures where there is an abundance of network addresses), security is an essential attribute that can potentially be achieved by NAT.

![Perimeter defense strategies employed on various segments of an internal network](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1701.png)

**Figure 17.1. Perimeter defense strategies employed on various segments of an internal network**

NAT complements the use of firewalls in providing an extra measure of security for an organization's internal network. Usually, hosts from inside the protected networks (with private address) are able to communicate with the outside world, but systems that are located outside the protected network have to go through the NAT boxes to reach internal networks. Moreover, NAT allows an organization to use fewer IP addresses in making entire networks operational, which aids in confusing attackers as to which particular host they are targeting; in this way security dimensions are increased. Many denial-of-service attacks such as SYN flood and ping of death can be prevented using NAT technology.

The main feature in NAT is the translation table that the NAT box maintains. A NAT box might be implemented with a laptop computer and the appropriate network interface cards. The translation table maps external unique IP addresses to internal private IP addresses. Normally, this mapping is not one-to-one. To conserve address space, a single global IP address may be mapped to more than one private IP address. Typically, port associations (on the NAT boxes) are created to achieve multiple mapping of public and private addresses. Any packets from the outside attempting to reach a particular host on the private network get routed with the NAT-specified global address. It becomes the responsibility of the NAT software to look up the translation table to find out the particular private address to which the packet has to be routed. [Figure 17-2](ch17.html#the_nat_methodology) shows the technique involved in NAT. Normally, translation tables are built using three methods:

- **Static**—In this configuration, the relationships among the global and private IP addresses are fixed.
- **Dynamic outbound packets**—In this mode, the translation tables get updated automatically as outbound packets are processed from the private network.
- **Domain name lookups**—When packets from the external Internet make domain name lookups of hosts inside the private network, the domain name lookup software takes the responsibility of updating the NAT tables.

![The NAT methodology](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1702.png)

**Figure 17.2. The NAT methodology**

# Basic Architecture Issues

Network architecture consists of various components. Each component has its own functionalities and responsibilities in effecting the various tasks involved in network communication. Many functions, such as quality of services, remote logins, security, and so on, require specialized components intended for a specific function or combination of functions. This section deals with certain building blocks (or components) that make the realization of these functionalities possible.

- **Demilitarized zone**—A demilitarized zone (DMZ) is a noncritical yet secure region generally designed at the periphery of the internal and external networks. Normally, the configuration of a DMZ is such that it is either separated by a firewall from the external network or sandwiched between two firewalls, one at the external periphery and the other at the internal. [Figure 17-3](ch17.html#a_web_server_in_a_dmz) shows a demilitarized zone setup for a Web server application.
- **Modems**—As functional end-user equipment, modems (*mo*dulators-*dem*odulators) are used to transmit digital signals over analog telephone lines. Thus, digital signals are converted by the modem into analog signals of different frequencies and transmitted to a modem at the receiving location. The receiving modem performs the reverse transformation and provides a digital output to a device connected to a modem, usually a computer. The digital data is usually transferred to or from the modem over a serial line through an industry standard interface, RS-232. Many telephone companies (who offer DSL services) and cable operators (offering Internet cables) use modems as end terminals for identification and recognition of home and personal users.![A Web server in a DMZ](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1703.png)**Figure 17.3. A Web server in a DMZ**
- **Hubs**—A hub is a device for connecting multiple LAN devices together. It also performs as a repeater in that it amplifies signals that deteriorate after traveling long distances over connecting cables. Hubs do not perform packet filtering or any addressing functions.
- **Bridges**—Bridges are devices that are used to connect two or more hosts or network segments together. Bridges work only at the physical and link layer level and use the hardware Media Access Control (MAC) addresses for transferring frames. The basic role of bridges in network architecture is storing and forwarding frames between the different segments that it connects. Typically, a single bridge can have more than two ports, which means that more than two networking elements can be combined to communicate with each other using a single bridge.
- **Switches**—Network switches generally have a more intelligent role than hubs. Strands of local area networks (LANs), normally belonging to the same collision domain, are usually connected using switches. Mainly working on the Layer 2 frames (Data Link layer), they are equipped with the ability to read the packet headers and process appropriately. Generally, switches have the ability to read the incoming packets' hardware addresses to transmit them to the appropriate destination. Frames could be lost if a particular host is either unreachable or disconnected. Switches play an important role in regulating traffic regulations on the segments they interconnect. Because switches directly connect one of many devices connected to its input ports to one of many devices connected to its output ports, a switch necessarily has a larger number of input/output interface cards than bridges.
- **Routers**—Routers are one of the main components of the chassis of networks. Routers are mainly involved in the transmission of packets to their destinations, routing a path through the sea of interconnected network devices. The packets are removed from the incoming frames and individually analyzed. Routers normally work at the Network layer (Layer 3 of the OSI model), which assigns the much familiar IP addresses. IP addresses are software or logical addresses that point to a logical location or connection on a network. Worldwide IP addresses of any connection are unique unless they are not defined for private use. Routers normally process connectionless network layer packets, otherwise known as *datagrams*. Packets originating from the same source and reaching the same destination as part of the same connection may be routed through different routes. IP packets are equipped with header fields that give the routers knowledge of where it originated from and its intended destination. There is a plethora of work on routing algorithms. Routing algorithms are the knowledge base of the routers. Routers, which hop packets from one point to the other, use the routing algorithms for effecting their decisions. Bellman-Ford, Distance vector, OSPF, and so on are some well-known routing algorithms used on the Internet. Proprietary organizations can have their own implementations of these routing algorithms.
- **Gateways**—As you move up in the network protocol stack, you find gateways. Gateways normally work around the transport and session layers of the OSI model. Typically, on and above the transport layer, there are numerous protocols and standards proposed by different vendors. The Internet uses the Transmission Control Protocol (TCP) at the Transport layer, but other protocols (mostly proprietary) do exist in this layer. Some of the other Transport layer protocols include:X.25Systems Network Architecture (SNA)Asynchronous Transfer Mode (ATM)Gateways are used when dealing with multiprotocol Transport layers and above. All of the following are important specifications at the gateway level of network architecture:Form factorNetwork typePerformancePortProcessor specificationsMemoryFeaturesCommon features for network gateways include stackable, rack mount, LED indicators, integrated firewall, and Virtual Private Networks. Application layer gateways are ideal choices for integrating multiple security services. Firewalls and intrusion detection systems are ideally suited to be at this layer of the network stack.

# Subnetting, Switching, and VLANs

Addressing is one of the main issues that network architecture is concerned with. Two major addresses are involved with all the major public access networks such as the Internet. They are the hardware (MAC) and IP addresses. MAC addresses are used to uniquely identify individual machines as hosts and are not as important from a routing standpoint. They are hard coded into the network card and most people are not even aware what they are. On the Internet, the most important addresses are IP addresses. An IP address points to a logical entity on the Internet and is normally unique in identifying itself. Addressing in IP version 4 (IPv4) uses 32 bits. Rather than providing for random addresses for incoming hosts, the Internet follows a particular hierarchy that could be logically used for various vital services such as routing, name resolution, and so on.

IPv4 divides the whole address range into five major classes: Classes A, B, C, D, and E. The 32-bit address is split into three distinct regions, as follows:

- Class-ID
- Net-ID
- Host-ID

The class-ID is usually represented in the first to the fourth bits of an IP address. This is followed by the net-ID and then the host-ID. With such a scheme, it's easy to inspect the address and discern which network and class a particular IP address host belongs to. This is highly useful when routing and resource discovery are in the picture. [Figure 17-4](ch17.html#ipv4_class_addressing) shows an IPv4 addressing representation. Classes A, B, and C are typically allotted to an individual host depending on how big the particular network segment is. Classes D and E are for multicasting and future use, respectively. Class A encompasses a relatively small number of networks compared to class B and class C (which holds the most number of network addresses). Huge networks are generally addressed using class A, rather than class B and class C (which can hold the minimum number of hosts among the different classes).

![IPv4 class addressing](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1704.png)

**Figure 17.4. IPv4 class addressing**

Subnetting is a technique followed in network architecture to reduce the burden of the routers in maintaining routing tables. Class B networks have approximately 64,000 different host addresses, though most organizations registered for class B addresses do not require that many hosts as they do not employ that many systems. In this case, many addresses get wasted and cumulatively there is a dearth of IP addresses with IPv4 because each network segment typically demands its own net-ID in the addressing scheme. Subnetting schemes are built in such a way that the traditional net-id/host-id barriers are broken so that any combination of addressing would fit per the size of the network. A subnet mask (a series of 1s followed by a series of 0s) is applied to the IP address to determine which subnet a particular destination is on in a particular network. This is a highly recommended feature for conserving addressing space and controlling router table explosions. Switching is then done based on the resolved subnet address and host address. A new technique called *classless interdomain routing (CIDR)* offers new features in this regard.

Switching techniques can be used to incorporate interesting architectural twists in networking. One such network architecture concept is the virtual local area network (VLAN). This architecture is useful in situations where organizations have geographically distributed divisions or departments and would still like to place all the entities under a single network segment. VLANs make this possible. VLANs use switching to achieve same broadcast domain relationships. [Figure 17-5](ch17.html#vlan_of_four_lan_segments_open_parenthes) shows how virtual networking for four different LAN segments (A, B, C, and D) is possible using switching technologies.

![VLAN of four LAN segments (A, B, C, D) using a switch](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1705.png)

**Figure 17.5. VLAN of four LAN segments (A, B, C, D) using a switch**

# Address Resolution Protocol and Media Access Control

The *Address Resolution Protocol (ARP)* and the *Media Access Control (MAC)* are basically Layer 2 and 3 control issues in the Transmission Control Protocol/Internet Protocol (TCP/IP) stack. It is impossible to associate individual IP addresses to every physical machine that has been manufactured. Instead, every machine can be uniquely identified by a second address called the Media Access Control address, commonly known as a hardware address. The ARP is used to determine the 48-bit MAC address corresponding to a 32-bit IP address.

Normally, one would intend to use static translation maps to achieve this process, but the enormity of IP and MAC addresses available that must be maintained make it almost impossible for static maintenance. TCP/IP designers have a novel way of dynamically solving this problem using ARP. Normally, any host that requires determining the hardware addresses of a particular IP address broadcasts address request packets all over the domain it is in. The host whose actual IP address is found on the requests replies to the intended source of the presence of the particular host with its IP and MAC address. If no host can be determined, default routing actions are taken. This information can be used for further communication between the two hosts. To speed up the resolution process, a small segment of memory is maintained to store short-term IP and MAC address mapping of other hosts on the network. This memory is called the ARP cache.

The ARP cache is the first thing that a host looks at for address resolution before it can start issuing the broadcast process. Because two parties that were involved in communication at some point in time are likely to communicate at a subsequent time, cache memory becomes very vital in speeding up processing in the protocol. The ARP caches are required to be refreshed at regular intervals of time (approximately every 25 or 30 minutes). This is very vital in determining changes that have occurred in recent history. In hosts where storage mechanisms are not available, a similar protocol called the Reverse Address Resolution Protocol (RARP) is used for IP address determination at bootup. [Figure 17-6](ch17.html#arp_message_data_structure) shows the pseudo data structure followed in ARP messages.

![ARP message data structure](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1706.png)

**Figure 17.6. ARP message data structure**

# Dynamic Host Configuration Protocol and Addressing Control

The *Dynamic Host Configuration Protocol (DHCP)* is a commonly employed technique to distribute IP addresses on networks where static address allocation may not be appropriate. Auto-configuration IP address distribution techniques such as DHCP may be very easily done where centralized servers are commonly available. However, there is also a need for autoconfiguration in architectures where individual clients communicate directly with each other and there is no centralized service. An example of this type of communication in wireless networks is the ad hoc network. Ad hoc networks are infrastructureless, multihop wireless networks that can be deployed without any pre-existing setup. Ad hoc networks are mobile in nature and any node can join and leave the network at any time. Due to their mobility, ad hoc networks must be able to configure themselves without human intervention. Configuration (such as address assignment) of a node in such a network is a critical issue. The nodes in an ad hoc network are basically a plug-and-play type, wherein any node can enter and exit a network configuration without much intervention from other nodes in the network. Zero-Configuration networks have a similar setup, but the main problem that arises when applying the techniques followed in Zero-Configuration networks to ad hoc networks is that a set of reserved IP address (169.254) exist for use in such networks, which may not be feasible for ad hoc network set ups. This section reviews some of the existing techniques for dynamic host configuration in ad hoc networks and their applicability.

The best method to assign IP addresses to network nodes in any network would be to assign them statically for each node in the network. This process could become highly tedious and vulnerable to errors for large-scale networks. This is one of the main reasons that DHCP was designed to automate the address assignment in IP-based networks. There are basically two modes of address assignment to a network configuration: stateful and stateless. In the stateful mode of configuration, a predefined set of IP addresses is dynamically issued either permanently or on lease to the individual nodes. In the stateless configuration (usually applied to IPv6 networks) a function of the hardware address is used to assign an IP address. For a variety of reasons, one generally cannot assign an IP address based on the MAC address even in IPv6 networks where one-to-one mapping of IP and MAC addresses is possible. For example, security reasons constrain the IP address to originate from a distinct set, and unavailability of unique hardware addresses is another reason. The fact that ad hoc networks are dynamically configured, combined, and divided makes them quite unsuitable for stateless modes of auto-configuration. Moreover, the IETF has recommended that stateful autoconfiguration be implemented for ad hoc networks. The mobile nature of ad hoc networks makes devising a suitable mechanism for dynamic host configuration with a predefined set of IP addresses very difficult. It should be noted that mobility is quite different from connectivity. A network can be independent of physical hardware connectivity (a wireless medium, for example) and yet be nonmobile. Ad hoc wireless networks combine these two aspects, independent connectivity and mobility, making it quite complex for most present-day configuration protocols.

# Zero Configuration Networks

People constantly talk about the complexities of networks and the infrastructure that is required to get even a simple network up and running. There is a song lyric that rings true with many people: "I should be able to get online without a Ph.D." In some large environments the sheer complexity of the networks is in direct correlation to the functionality that is needed. However, in other environments only a base functionality is needed, yet a large amount of the effort is still needed to get the network up and running. [Figure 17-7](ch17.html#networks_and_complexity) shows the complexity of a network versus the effort required to get it up and running.

![Networks and complexity](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1707.png)

**Figure 17.7. Networks and complexity**

You can see from this figure that whether you have a simple or a complex network the amount of effort needed to set up the network is fairly similar because there is a base functionality that is needed regardless of the size of the network. [Figure 17-8](ch17.html#infrastructure_for_simple_and_complex_ne) shows the basic infrastructure that is needed for both simple and complex networks.

![Infrastructure for simple and complex networks](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1708.png)

**Figure 17.8. Infrastructure for simple and complex networks**

Whether you have a simple or complex network you still need to have ways for your users to obtain IP addresses and network configuration information. The following is the minimum amount of information that every host needs in order to connect to a network:

- IP address
- Subnet mask
- Default gateway
- DNS servers (optional)

Therefore, a server must respond to DNS queries and respond in a timely manner. If users also want to surf the Web, a DNS server is needed to translate domain names into IP addresses. For a simple network, these services could reside on a single system, compared to a complex network where these services might be provided by several systems. But regardless of the number of servers, the amount of effort required to set up this infrastructure is similar.

For smaller networks there needs to be a better way to get a network up and running without all the extra effort that is required for a complex network. When most people think of simple networks they think of small offices; however, there are some simple networks where there is no corresponding infrastructure. A good example is embedded systems. These processors create a network so they can communicate but there is no way that you'll be able to set up DNS and DHCP servers so they can communicate. This example shows that a simple way of creating networks is not just a nice thing to have, but is a requirement for devices to function.

## Details of zero configuration networks

Zero configuration networks allow systems to communicate in a network with no prior configuration of the system and no prior infrastructure. The second part is extremely critical to remember when dealing with zero configuration networks. Some people argue that DHCP allows systems to communicate with no prior configuration of the host. Essentially you just plug in a system, and it pulls the IP information, and is able to connect. However, DHCP is far from being zero configuration because it requires building an infrastructure that contains a DHCP server, and the DHCP server must be configured before anyone connects. Also, from a fault tolerance standpoint, if the DHCP server crashes then the whole network also stops functioning. This highlights another key attribute of zero configuration networks. Because there is no prior configuration and no infrastructure, these networks also have a higher degree of fault tolerance. If a network is simple and has few components, it is less likely to go down.

Zeroconf is the protocol suite and specifications that implement a zero configuration network. In most literature, zeroconf refers to the general concept of zero configuration networks and the specific protocol implementations that roll out zero configuration networks in a given environment.

The clearest way to describe zeroconf is to look at a quote from the Zeroconf Working Group of the Internet Engineering Task Force (IETF):

> *The goal of the Zero Configuration Networking (Zeroconf) is to enable networking in the absence of configuration and administration. Zero configuration networking is required for environments where administration is impractical or impossible, such as in the home or small office, embedded systems "plugged together" as in an automobile, or to allow impromptu networks as between the devices of strangers on a train*.

You can see by this definition that zeroconf is really zero configuration, zero infrastructure, and zero administration. Zero administration is really just a consequence of the first two requirements. If there is no infrastructure and nothing to set up, then there is nothing to administer or control, which not only cuts down on what is required to set up a network but also cuts down on cost. Because there is no infrastructure, zeroconf networks are inexpensive, which allows these networks to be set up and torn down on a whim because there is no loss of revenue in doing so.

Zeroconf networks are starting to take off and get buy-in from many vendors.

Apple, Epson, Hewlett-Packard, Lexmark, Philips, Canon, Xerox, Sybase, and World Book all have zeroconf capabilities built into their products. More companies are likely to build in zeroconf capabilities or become zeroconf-enabled as the technology matures and becomes standardized and widespread.

At the end of 1999, an IETF working group on zeroconf was started. However, as with most technologies, it takes some time for a given technology to take off. Final standards are being finished.

The working group currently has two Internet drafts explaining the process, the protocols, and what is required for zeroconf:

- Requirements for automatic configuration of IP hosts
- Dynamic configuration of link-local IPv4 addresses

## What is required for zero configuration networks?

In order to understand when zeroconf networks should or should not be used, it's important to know what is required by zeroconf. Essentially, zeroconf replaces all the infrastructure items that are required for a computer to be connected to a network and for a computer to obtain services from the network. Therefore, the following services must be provided by zeroconf:

- Distribute IP information including IP address, subnet mask, and default gateway without a server such as a DHCP server on the network.
- Translate domain names to IP addresses without the use of a DNS server.
- Provide any necessary directory services without a domain controller or LDAP server.
- Allow for multicast addresses without a multicast server.
- Provide for any miscellaneous network servers that are required to support a network with a server or special protocol.

Essentially, what is required for zeroconf is for a network to be set up anywhere without any prior configuration or infrastructure. Based on the preceding requirements you can see that zeroconf will only work in certain situations.

## When should zero configuration networks be used?

Zeroconf is ideal for SOHO (small office/home office) type settings. Also, it is ideal in situations where networks need to be set up and torn down on short notice for a minimal cost. This could come into play with law enforcement or even military situations where, based on a crisis, a small network needs to be set up quickly so people can communicate and find out what's happening. The following examples demonstrate when zeroconf could be used:

- Remote office location where there is no technical support
- Temporary office location where it is not a good investment to build an infrastructure
- Multi-day meetings where a group of people need to communicate but only for a short time
- During a disaster where the network infrastructure is unavailable or destroyed but limited connectivity is still needed

In short, zeroconf should be used in situations where only basic network services are needed for a small group of people. As the type of network services and the number of people using the network increase, so does the complexity. With highly complex networks, zeroconf is not usually the solution.

## When should zero configuration networks not be used?

Following along with the preceding discussion, zeroconf should not be used in larger networks or environments where anything more than the basic services are needed because in large and complex networks some degree of administration is required, and complex services usually require dedicated servers. The following are some examples where zeroconf networks would not be appropriate:

- Large networks
- Any networks requiring complex services
- Any network needing a high degree of security
- Networks that need control of the IP space

## Security issues with zero configuration networks

Zeroconf was built to meet a functionality need, not a security need. However, because it was developed in 1999, when security wasn't as big a concern, the developers realized the importance of making sure they addressed security in current versions. But instead of building in specifics for it, they stated that zeroconf provides the same level of security as the other TCP/IP protocols. There is one big problem with taking this approach: the other protocols do not address security, which is why there have been so many problems. The traditional network protocols work great from a functionality standpoint but do not properly address security, which means that zeroconf has similar security issues. From a network security professional's standpoint this is a bad thing because it leaves the network vulnerable.

To make matters worse from a security standpoint, zeroconf is based on ARP (Address Resolution Protocol), which has a series of security issues because there is no secure authentication built into it. As a result, the translation between IP and MAC address can easily be spoofed. Also, ARP allows for gratuitous ARP requests, which means anyone can send out false information and the end system will act on that information.

## Ways to exploit zero configuration networks

Depending on how you look at the problem, zeroconf can be either very difficult or very easy to exploit. It can be difficult because there is no server to break into. Traditional exploit methodologies involve finding an open port on a server, finding weaknesses with the service that is causing that port to be open, and then gaining access. This is the standard way that buffer overflow and other network attacks operate. In this case, because zeroconf essentially removes or does not require any network infrastructure or servers, there is nothing to exploit.

On the negative side, even though there is no server there is still opportunity to exploit zeroconf. A good example of how this is possible can be seen by looking at ARP, which requires no server but can still be exploited through various spoofing and trust exploits. Because zeroconf is similar to ARP it is open to similar attacks. However, all the attacks are based on sidestepping the trust mechanisms of the protocol. Because there is not a specific server to attack, the attacks are launched directly against the client systems.

The following are some exploits that can be run against zeroconf networks:

- **Spoofing attacks**—Because there is no central server, someone who understands the protocol can go in and configure their system to impersonate someone else on the network. Because there is no built-in security or authentication with the protocol, there is no way to stop this type of attack.
- **Hijacking attacks**—Hijacking is similar to spoofing but instead of just impersonating someone on a network, you take over their existing session.
- **Chaos attack**—Essentially, zeroconf is an unmanaged or self-managed network. Because there is no central control, this means that someone can hook systems up to the network and make changes to the address and network that cause chaos across the network. In chaos attacks, things work only sporadically and there is no rhyme or reason to why they work or don't work.
- **Denial-of-service attacks**—With any network, someone can always flood it with extraneous traffic, called a denial-of-service attack. However, in the case of zeroconf, attackers can also send out false information so hosts think they are talking with given entities, but the information is actually reaching the attackers, not the intended receivers.

Any emerging technology fills some need. Zeroconf fills the need to set up a network with no prior configuration or infrastructure. However, as with most technologies, zeroconf's functionality is enhanced, but the door is also left open for security issues. Because zeroconf has no built-in security and is based on ARP, controlling the scope of zeroconf will be critical to limiting the type of attacks someone can launch against your network.

# System Design and Architecture Against Insider Threats

Organizations continue to spend an exceptional amount of time and money to secure the network at the perimeter from external attacks; however, insider threats are becoming more and more prominent. Many surveys and reporting groups have reported insider incidents to be more than 50 percent of all attacks; however most organizations don't report insider attacks for fear of losing business and suffering ridicule and embarrassment. Insider threats are a growing concern that must be addressed.

These threats include attacks, or the threat of attacks, from both authorized and unauthorized insiders. An authorized insider is one who is known and trusted by the organization and has certain rights and privileges. An unauthorized insider is someone who is connected to the network behind the perimeter defenses. This could be someone plugged into a jack in the lobby or a conference room, or someone who is using an unprotected wireless network connected to the internal network. Insider attacks can include anything from sniffing data to abusing legitimate rights and privileges. Organizations often don't deploy as many monitoring systems on the internal network as on the perimeter. Sometimes they don't employ any. They're mainly concerned with watching what's coming in through the perimeter from the Internet. However, insider attacks are more common and often more dangerous.

Measures for both prevention and detection can be taken to combat insider threats. Preventive measures are the classic methods of least privilege and access control. Data is protected by giving users the least amount of access they need to do their jobs. Other preventative measures include system hardening, anti-sniffing networks, and strong authentication. Detection includes monitoring of users and networks, using both network- and host-based intrusion detection systems. These are typically based on signatures, anomalies, behavior, or heuristics (past experience). For example, a signature-based method may look for known attacks on the internal network. An anomaly or behavioral system may profile and monitor users as they use an application or database. When users perform an action that deviates from the profile, an alert is triggered. In more restrictive systems, automatic preventive measures can temporarily disable a user's account when he deviates from the profile. A policy-based preventive method involves user background checks and security clearances. This establishes a degree of trust from the users allowed inside, but does not entirely mitigate the problem.

Many current products can solve parts of the problem when implemented in a layered defense. Most of the mitigations are known techniques and come down to policy enforcement. System hardening and access control should be applied just as much to protect against insiders as it would be to protect against outsiders. Any open source or commercial IDS can be used to monitor the network. However, there are very few (mostly experimental) user-profiling systems for applications and databases; these are usually developed in-house. This section addresses the architecture and design of a system-wide insider threat monitoring system. The system design includes monitoring insider activity and user profiling at the network, desktop, database, Web, instant messaging, and telecommunications level.

## Architecture and design

[Figure 17-9](ch17.html#insider_threat_monitoring_system_archite) depicts the architecture of the insider threat monitoring system. The data is collected via standard devices such as sniffers, intrusion detection system, and logs, as well as dedicated collectors for specific areas such as IM, Web, e-mail, and database. Once baselines are developed, any deviations should be investigated. The main aspects that are monitored by the system include:

- **Protocols**—Protocols are monitored and baselined to determine statistical information on the protocol types and usage on the network. This baseline is created on both an organization and user level. Protocol baselining includes both the wired and wireless network. Data for the baseline is obtained from routers, switches, firewalls, wireless APs, sniffers, and dedicated collectors. Protocol deviations could indicate tunneling information or the use of unauthorized programs to transmit information.
- **Web**—Web activity is monitored to determine the baseline of usage and sites visited. This baseline is created on both an organization and user level. Data is obtained from Web server logs, features built into the Web server, or a dedicated Web collector. Deviations could indicate tunneling or some other information transmission.
- **E-mail**—E-mail is monitored to determine the baseline usage and recipients. This baseline is created on both an organization and user level. Data is obtained from e-mail server logs, features built into the e-mail server, or a dedicated e-mail collector. Data is also monitored for specific keywords. Deviations could indicate users sending e-mail outside the organization at odd times.
- **IM**—Instant messaging is monitored to determine the baseline of usage and recipients. This baseline is created on both an organization and user level. Data is obtained from a dedicated IM collector. Data is also monitored for specific keywords. Deviations could indicate users sending information outside the organization or disclosing proprietary information through conversations.
- **Database**—Database interaction is monitored to determine the baseline of usage and queries. This baseline is created on both an organization and user level. Data is obtained from a dedicated database collector. Deviations could indicate users performing abnormal/normal queries and accessing information for unauthorized reasons.
- **Desktop/laptop**—Desktops and laptops are monitored to determine a baseline of usage and activity. A dedicated collector, as well as host-based firewall and intrusion detection logs, creates this baseline on a user level. Deviations could indicate users performing abnormal activities such as installing unauthorized programs or transmitting information.
- **Printer**—Network printers are monitored to determine a baseline of usage and activity. A dedicated collector and the printer log features create this baseline on a user level. Deviations could indicate users printing out unauthorized information.
- **Telecommunications**—Telecommunications systems, including phones, faxes, and modems are monitored to determine a baseline of usage and activity. A dedicated collector is used in conjunction with the PBX log features to create this baseline on a user level. Deviations could indicate users connecting to a modem at odd times, transmitting proprietary information via the modem, sending unauthorized faxes, or making unauthorized calls.
- **Physical Controls:** Lastly, physical controls should be monitored to ensure that equipment and data do not leave the building. Devices such as cameras, recorders, and camera phones should be prohibited.

![Insider threat monitoring system architecture](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1709.png)

**Figure 17.9. Insider threat monitoring system architecture**

Some challenges to implementing this system include the large quantities of data that must be analyzed, the development of profiling algorithms, and the incorporation of the overall correlation intelligence behind the system. These aspects are still being developed for each component of the system.

# Common Attacks

Many varieties of attacks can be detected by using sound architecture. Many of the attacks focus on altering user records and creating back doors for the attacker. Back doors serve as an entry point for attackers (the creator of the back door or others) to launch attacks at unexpected times. *Vulnerability analysis* deals with the detection and removal of such back doors so that they can't be used for exploits. In most cases, the attacker wants some personal gain out of an attack. Attackers may target bank accounts and financial organizations with the intention of embezzling money. In such cases, personal profiling of the attacker is highly recommended. Some of the well-known attack types are as follows:

- **Denial-of-service**—Attacks intended to deprive legitimate users from accessing network resources and functions. Constant attempts to log on to a server by the intruder can slow down the server's processing abilities and decrease or eliminate its ability to service legitimate users. Financial organizations run the risk of losing disgruntled customers when such attacks are prevalent. A typical example of a denial-of-service attack is the ping of death. Ping-of-death attacks occur when an attacker causes a sudden surge in ping messages to a particular host or network. If the target system's processing power is not well protected, a huge amount of power could be wasted in responding to the ping-of-death attack. When the target system exceeds its processing threshold, the entire system collapses. Detriment to the capacity of resources such as memory, bandwidth, and so on can fall under this category.
- **Spam**—Another well-known mode of interrupting legitimate activity on a network. A user receiving a flood of spam messages has to sort out these messages from legitimate e-mail, resulting in decreased efficiency at many organizations. IDSs should be capable of figuring out and fixing the spam issue.

### Note

A distributed denial-of-service attack is defined as a denial-of-service attack carried to more than one host. This happens when an attacker compromises a large number of geographically distributed hosts. The spreading of spam is an ideal task for such distributed denial-of-service attacks.

- **Scanning**—Scanning of network traffic or data may be another activity of interest to attackers. Scanning activities may be used to gain knowledge about the following:System parametersHost activitiesTypes of network on the secured systemTypes of resources involvedType of services providedOperating systems usedVulnerabilities present on the networkPort scanners and network scanners are common tools that an attacker uses for such activities.

# Summary

This chapter reviewed some of the most important segments in the design of networks. Security is one of the fundamental constituents of any network realization. The initial portion of the chapter focused on building blocks on which typical, day-to-day public networks are built. The chapter mainly focused on how internal networks (particularly private networks) can be protected from general-purpose and public networks.
