# Chapter 28. Firewalls, Gateways, and Proxy Servers

**IN THIS CHAPTER**

- See how firewalls can be used to protect networks
- Learn about filters you can apply
- Use Network Address Translation to keep systems hidden
- Deploy proxy servers to keep network services secure

In this chapter you learn about several different kinds of network services that are used to secure networks: firewalls, gateways, and proxy servers. These services can be implemented in software or in hardware. The use of these services helps protect a network, making it much harder for outsiders to gain unauthorized entry to private networks.

Firewalls evaluate traffic and decide which traffic to forward and which traffic to drop or return. The criteria for deciding which action to take is called a filter, and filters can be based on information in packet headers such as source address, protocol used, and many other factors. Advanced firewalls can look into packets at the Application layer performing Deep Packet Inspection. The placement of firewalls at different points in the network for different purposes is explored.

These devices perform Network Address Translation (NAT), which is explained in detail in this chapter. NAT takes a request from clients on the public network and forwards them to systems inside on a private network. This feature allows private network systems to maintain their anonymity while allowing the network to route otherwise unroutable traffic.

Gateways are systems that serve as the interface between two different networks. Gateways are Application layer (Level 7) devices. There are Security Gateways that are sold for these purposes. A proxy server is a cross between a gateway and a firewall. Proxy servers serve as the surrogate for systems on a private network, fielding all requests and serving all replies. Many proxy servers perform caching; others configured as reverse proxy servers can perform many of the functions of the applications and network services that they front.

# Firewalls

In a building, a firewall is a partition that is made of fireproof material that can isolate and protect one side from fire on the other. On a network, a firewall is a set of security routines that isolate and protect systems from malicious activity by erecting a protective barrier. This protection can take the form of separating the networks using different hardware devices (physical network interfaces) using a multihomed device; this type of mechanism is referred to as physical isolation. Alternatively the firewall can speak to an outside network using one network protocol and to the inside network using another protocol; this type of mechanism is referred to as protocol isolation. The nature of modern computing is such that it is very imprudent to have a system connected to the Internet without the use of some sort of firewall.

Firewalls can be relatively simple, or they can be very complex. Firewalls can be implemented in software, or as software installed on dedicated hardware servers and appliances. A firewall can be run on top of an operating system such as Linux, UNIX, or Windows; or it can be a "black box," a self-contained unit that runs its own proprietary operating system. Firewalls can be categorized into the following groups:

- Personal firewalls such as the Windows firewall, ZoneAlarm, and others
- Router firewalls
- Hardware firewalls, either low end or high end
- Proxy firewalls
- Server firewalls

Most often, firewalls have features that span more than one of these categories. When comparing one firewall to another, three factors come into focus: features, performance (as measured by throughput), and price. Firewalls are one network device for which there are no standardized performance benchmarks, and manufacturers, knowing that their customers use their firewalls in many different ways, are loathe to quote a performance metric to potential buyers.

## Firewall features

Whatever the nature of a firewall's deployment, firewalls function by applying a set of rules to the traffic that flows through them. The firewall then either forwards the traffic on or drops the packets. A firewall can be a Network layer (Level 2) filter or an Application layer (Level 7) filter, or any level between Levels 2 and 7 in the OSI model.

Here are some features to look for when evaluating firewall products:

- **Packet filtering**. Packet filtering reads the fields of IP packet headers and uses rules to allow traffic into the system. Packet filtering can also be applied to outbound traffic.
- **Network interface input filters**. These filters block traffic based on the source IP address or range, port numbers, and protocols used.
- **Network Address Translation (NAT)**. NAT is a conversion system that takes incoming traffic from one subnet and changes the addressing to forward it onto systems on another subnet. NAT uses a lookup table to make the translation and is capable of working with non-routable private networks. Private networks are non-routable in the sense that traffic cannot be directed from outside the network to a specific system inside the network; routing within the private network is fully enabled. NAT isn't strictly a firewall feature — it is more commonly associated with routers and proxy servers — but it does provide technology that conceals the IP address of internal systems, which is a valuable function.
- **Stateful inspection**. A stateful inspection examines any outgoing packets and logs the destinations into a state table. When traffic is sent back from the system outside the firewall, the state table is used to determine if the packets should be forwarded on. As a general rule, stateful filters require more overhead and are slower than static packet filters.
- **Circuit inspection**. In a Circuit-level filter, sessions are managed instead of simply referencing packets or a connection in a state table. Sessions require a request from a system inside the firewall and can support applications that create multiple connections. Protocols with multiple connections include HTTP browser sessions, FTP transfers, and streaming media transfers.Circuit-level inspection makes it difficult for IP spoofing, Denial of Service (DoS), and network reconnaissance attacks to succeed, while the related stateful inspection filters tend to be less effective against DoS attacks.
- **Proxy firewalls**. A proxy firewall serves as a go-between with the client outside of the firewall and a system or server on the inside. There is no direct connection through the firewall. Proxy firewalls create two distinct connections, one on each side of the firewall. The outside client only communicates with the proxy, which, from the standpoint of the client, is their connection endpoint. Proxy servers can add efficiencies by caching commonly or recently used data, can validate the protocols that are passed through the firewall, and can be managed so that requests are forwarded based on the user IDs and/or group memberships.Of all of the aforementioned features on this list, a proxy firewall requires the most resources and is the slowest filter. However, proxy firewalls can protect networks against DoS, IP spoofing, and network reconnaissance, as well as viruses, Trojans, and worms. Proxy firewalls offer only limited Application-level protection.
- **Application filtering**. Application layer filtering is a deep packet inspection technology. It is both the most complex and slowest performing of the firewall filters in this list. This filter examines packets for the data they contain and can modify those packets as necessary.

These features and filters are discussed in more detail individually in the sections that follow.

### Personal firewalls

Personal firewalls are designed to protect a single computer, or less frequently, a SOHO network that is sharing a single connection. Examples of personal firewalls include CA Personal Firewall, Comodo Firewall Pro, IPFilter, ipfirewall, Kaspersky Internet Security, Lavasoft Personal Firewall, Norton 360, Outpost Firewall Pro, PC Tools Firewall Plus, Sunbelt Personal Firewall, Sygate Personal Firewall, Trend Micro Internet Security, and ZoneAlarm, with ZoneAlarm being the best known of the group.

### Note

A chart of personal firewalls may be found at `http://en.wikipedia.org/wiki/Comparison_of_firewalls`.

Many operating systems now ship with personal firewalls. An example of a built-in firewall is Microsoft Windows Firewall, which began shipping with Windows XP SP1. The simple addition of this firewall had a major impact on making Windows systems much less vulnerable to outside attacks; it is a basic firewall, but it is effective. [Figure 28.1](ch28.html#the_windows_vista_firewall_application_c) shows Windows Firewall from Vista SP1, which, as it turns out, was a major upgrade from the original XP firewall. Vista Firewall can filter by IP source and destination address, source and destination TCP/IP ports, for inbound traffic (ingress), for outbound traffic (egress), and by user ID. The only basic feature missing from Vista Firewall that is included in nearly all of the products just mentioned is the ability to filter by the source or destination MAC address. XP's firewall, by comparison, lacks the ability to filter by destination IP address, source port (and to some extent destination port), and by user ID, and to set a filter for outbound traffic. To my way of thinking, it is worth replacing XP with another firewall, but using the firewall that ships with Vista.

![The Windows Vista Firewall application can specify open traversal of the firewall by port, protocol, or, as you see here, by application.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2801.png)

**Figure 28.1. The Windows Vista Firewall application can specify open traversal of the firewall by port, protocol, or, as you see here, by application.**

I am not a great fan of personal firewalls, although I recognize their utility. Many firewalls greatly impact a system's performance — particularly a lightly powered system like a laptop. Some firewalls, such as ZoneAlarm, constantly interrupt your work with status pop-ups and with dialog boxes seeking permission for some action that they want to take. When selecting a personal firewall, these are important factors that you want to pay particular attention to. A personal firewall should be both inexpensive (many are free) and easy to configure. Also, personal firewalls are meant to operate on their own. Running two or more firewalls at the same time should be unnecessary and is undesirable.

### Router firewalls

Many routers ship with firewall features in them. Inexpensive routers tend to support address and port blocking, and provide some version of NAT for hiding internal private network addresses from view. A low-end router is often sold as a connection to the Internet. Your ISP may install one on your home network as part of their cable or DSL connection. These routers are very much like an appliance, and they only take a few settings. It is important that a low-end router functioning as a firewall come from the manufacturer with settings that effectively block unwarranted Internet traffic; usually changing the administrator account ID and password should be all that is required to get started. Additional configuration can be done to these systems as needed.

The NETGEAR FVS318 ProSafe VPN Firewall is an example of a low-end router/firewall. It is based on technology developed by SonicWALL (`www.sonicwall.com`), one of the better-known companies in the firewall hardware field. The FVS318 is configurable within a browser. [Figure 28.2](ch28.html#the_service_settings_page_of_a_netgear_f) shows the Services settings page, which is where ports are enabled. Other features found on this basic router include NAT, port assignments, blocking by domains and IP addresses, assignment of static routing, Stateful Packet Inspection (SPI), and other features.

Router/firewalls tend to be priced based on the number of concurrent users that are allowed to connect, and often are extensible. SonicWALL's systems can have anti-virus scanning added, be updated automatically over the Internet, add different types of Application-level filters with deep packet analysis, and more. A high-end router with firewall features approaches the functionality of a dedicated firewall but generally has a lower price and a lower throughput than a hardware firewall.

Router/firewalls are a very convenient choice and can allow both functions to be managed as one entity. They can be quite low in cost (the current version of the FVS318 costs $130), with very capable systems available in the $500 to $2,000 range. As a rule, low-end routers have limited functionality, tend to provide only basic controls, require a lot of configuration to be effective, and have limited throughput, particularly when they are logging events.

![The Service settings page of a NETGEAR FVS318 router/firewall lets you enable ports and applications.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2802.png)

**Figure 28.2. The Service settings page of a NETGEAR FVS318 router/firewall lets you enable ports and applications.**

### Hardware firewalls

Hardware firewalls are devices that are dedicated to firewall functions and typically have limited routing capabilities. At the low end of this category are appliance devices that are essentially Plug and Play, and aimed at the SOHO (Small Office or Home Office market segment) or small business market. In many cases, these devices are using the same software that more expensive models in a vendor's line use, and with additional payment, those features can be unlocked.

You'll find that the cheapest devices in this category have static packet filtering, NAT, address and port filtering, remote filtering, and can support from 10 to a few thousand concurrent users, with 50 users being a more common lower limit. As appliances, these devices are typically inexpensive and simple to operate. They offer low performance and poor upgradeability. Combination router/firewalls tend to be more popular than low-end dedicated firewall hardware because they offer more functionality for about the same price.

High-end dedicated firewalls are an entirely different beast altogether. These devices are meant to be impenetrable, high-performance, highly available systems, and are meant for either enterprise-class networks or for network service providers. Fault tolerance is built into many of these products through the use of a hot backup or failover system.

The highest-performing hardware firewalls often come with some advanced features to improve performance. When evaluating these types of devices, look for the following features as differentiators:

- **Multiple gigabit Ethernet interfaces, or high-speed fiber connections**. Higher I/O speeds translate to faster throughput.
- **Robust data caching**. Advanced caching can greatly improve performance, but requires dedicated disk resources.
- **Proxy and Reverse Web Proxy services**. A proxy service is a service that acts on behalf of another service or application as if it is the server providing the services. A Web proxy is a Web server that takes requests from inside the network and either processes the request (from its cache, for example) or directs it to the appropriate Web server outside the network. Reverse Web proxy servers take requests from outside the network (the Internet, perhaps) and either processes the request or redirects it to a Web server inside the network.
- **IPSec encryption/decryption off-loading to dedicated subsystems**. IPSec encryption is used for VPN traffic and for publishing an internal network service to public networks or the Internet. IPSec is a particularly slow process on most firewalls, and so acceleration improves firewall performance.
- **SSL offloading**. SSL encryption is processor intensive. An SSL accelerator can lower the processor utilization of firewalls that are front ends to Web sites, and having a firewall be the endpoint of an SSL connection can improve Web site performance significantly.
- **Modularity and the ability to scale**. Modularity means that you can add additional subsystems as you need them.

Features that differentiate higher-end hardware firewalls from other devices include the ability to block ICMP messages, Application-layer filtering support, improved logging and alerts, upgradeability, strong vendor support, and, of course, a high price. A high-end dedicated hardware firewall can support from 5,000 to 500,000 concurrent sessions. The greater capabilities of this type of hardware means that an organization has to have trained support staff or outside services manage these devices.

### Server firewalls

While high-end hardware firewalls tend to run on proprietary hardware using a proprietary operating system, many vendors have chosen to implement firewalls on standard server operating systems as open solutions. The advantages of this approach are that the operation of the server is better known to support staff (so that they require less training and support), the hardware can be right-sized for the task, and a wider range of solutions may be available. Implementation of the firewall on a standard network operating system also means that any framework or management application that you use for your other server systems can be applied to this type of firewall, which is a great convenience. This category of firewall is noted for superior caching capabilities.

Functionally, there may be little difference between a high-end server firewall and a high-end hardware firewall. However, a server firewall is often easier to integrate, more scalable, and can be clustered or load balanced for greater availability than dedicated devices are. The main drawback to using server hardware in this type of application is that hardware firewalls are generally better optimized for their purpose, and so server firewalls may need higher-end hardware to perform at the same level. Also, with a well-known operating system, server firewalls are more susceptible to attack than a dedicated hardware firewall.

### Security gateways

A gateway is an Application layer (Level 7) device that acts as the interface between two networks. Gateways can be implemented as hardware devices or appliances, or as software. The term gateway is somewhat generic, and generally implies that some sort of protocol conversion is occurring. At the Application layer, a gateway may translate one file type for another; at the Presentation layer, that conversion might substitute one type of encryption for another, or some other function. Gateways can perform Transport level translations, or at the Network layer, from IP to AppleTalk. The fact is that gateways are a generic term for a device that can operate at any of the OSI levels. The result is that you will often see gateways described as "mail gateways," "Web gateways," and even "security gateways."

In order for a gateway to function between two networks, it often must be able to function as a router, providing address mapping, and as a switch for building the circuit that the data must follow through the device. It is common to have a gateway serve the role of a proxy server and a firewall. Therefore, if you see the term security gateway, be aware that this might refer to a device that fits into one of the categories of firewalls that you've already seen. For the term gateway to have any real meaning, in my opinion, the emphasis has to be placed on that system's ability to perform translations at the Application level.

## Network zones

Firewalls separate areas of a network into zones of different trust levels, as shown in the example of a three-tiered enterprise-class network in [Figure 28.3](ch28.html#different_types_of_firewalls_and_their_r). This network is divided into the following zones and networks:

- **The Internet**. The Internet is a zone of no trust. All packets coming in from the Internet are suspect until they are examined.
- **Border network**. The border network consists of a router that is discoverable by someone on the Internet. Routers are dual/multihomed, and this particular router has an outbound interface with the `Wiley.com` IP address and an inbound interface with the first of a set of private network addresses. Border networks end at the outgoing interface of the Perimeter firewall (192.168.1.2).A border router performs address translation and the two interfaces provide a physical isolation of one network from another. This is also true of other routers and firewalls in this example. With every change in network membership, particularly when private networks are involved, the amount of effort involved in being able to traverse the firewall without challenge goes up exponentially.![Different types of firewalls and their relative placements](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2803.png)**Figure 28.3. Different types of firewalls and their relative placements**So long as your internal systems are not compromised, it becomes nearly impossible to break through multiple firewalls. In a situation where a system on Subnet_1 is compromised, that system may learn about other Subnet_1 systems and the port on the Internal router that Subnet_1 connects to (192.168.3.3), but because routers provide port isolation (another form of physical isolation), that system should not be able to learn about other subnets provided that the directory service isn't compromised.
- **Border firewall**. The Border firewall, also known as the Perimeter firewall, exists to create the Demilitarized Zone (DMZ). As a general rule, the only traffic that should pass through the Border firewall is HTTP on port 80, HTTPS on port 443, and as limited a number of additional open ports as is possible. If you have an FTP server in the DMZ, then port 20 (for data), and possibly port 21 (for control commands) should be opened. Any other ports required to support the services found on the DMZ should also be opened.
- **Demilitarized Zone (DMZ) or Perimeter network**. The DMZ is an area of intermediate trust, and is often used for Internet-facing Web servers, e-mail relays, and FTP servers. The systems on the DMZ should only contain public information. Traffic entering the DMZ is allowed some freedom of action — they can run scripts on a Web server, for example — but most actions are still restricted. The DMZ extends from the incoming interface of the Perimeter firewall (192.168.2.1) to the outgoing interface of the Internal firewall (192.168.2.3). An isolated DMZ located on an intranet is called a screened network.The DMZ is a good place to restrict clients outside of the network that fail to pass tests that measure the system's health. If you have a network with a network access policy (NAP) server, that system might test mobile clients to see if their anti-virus programs are up to date and have scanned their system within a certain time period. Microsoft's NAP server tests systems to see if they are sufficiently updated, among other things. A failed system would be given access to the DMZ (or some similarly restricted subnet) where its deficiencies can be addressed before allowing the client access to the Internal LAN.
- **Internal firewall/proxy server**. The Internal firewall provides yet another network address translation leading to a different private subnet. Traffic from the DMZ to the Internal network is subject to a different set of rules, less restrictive than the Perimeter firewall used, and then passed onto the internal router. Some firewalls provide Application-level services. Firewalls performing these services analyze the types of packets and routes that traffic to the appropriate application server — firewalls of this type are playing the role of a proxy server.
- **Internal LAN/Private network**. The Internal LAN consists of systems that are trusted and are subject to the least number of restrictions of any subnet on the system.

The example shown in [Figure 28.3](ch28.html#different_types_of_firewalls_and_their_r) is complex so that you can see a range of firewall placements, and has many more components than a SOHO network would have. In a common setup, the Internet connection goes to a router (in the form of a cable modem or DSL modem, for example); that router connects to a firewall, which then connects directly to systems on the network either directly or through a switch. If the firewall has three or more interfaces, you could configure the network so that the router, LAN, and a screened subnet (DMZ) are each attached to different network interfaces on the firewall. Perhaps the most common SOHO setup has a cable modem connection to the Internet where the cable modem performs the function of a hub, switch, or Wi-Fi access point and lacks a router/firewall function.

## Stateless filters

The classic example of stateless firewalls is of those using packet filtering. Packet filtering is in nearly every firewall product, and was the first of the major technologies to be included in these types of products. In packet filters, packets are inspected and if the information contained in the packet matches an exclusion rule, the packet is dropped. Information that can be obtained from the packet consists of header fields that include destination and source address, protocol used, data type, and for TCP/UDP, the port number used for access or port filtering.

Packet filtering is a Network layer firewall technology. This type of filtering is considered to be "stateless," as it is the packet itself without regard for its context that is the determinant in matching the filter rule. The lack of context in applying a rule set means that stateless filters are unable to protect a network from traffic that spoofs the system into believing that it is from an approved source, of an approved data type, or some other violation when the data is really something else.

In rare cases, a firewall may be configured to return an acknowledgment that the packet was filtered, but in most cases, preserving the anonymity of the firewall is considered to be an important security feature.

## Stateful filters

Stateful firewalls analyze the connection used by each packet and uses that connection to determine if this is a new session and if it can allow the connection; one that is currently in use; or one that is unknown and must be denied. This type of filter is commonly referred to as a circuit filter. Because the firewall maintains a table of connections (routes) in a state table (or state list) for its different sessions, this type of firewall uses a "stateful" filter approach. A stateful filter is classified as a dynamic packet filtering technology, as it is session- or connection-based and changes based on interaction with clients outside the firewall.

A stateful filter uses stateful packet inspection (SPI) to manage network connections. An example of this sort of rule would be "Allow traffic from Subnet_1" or "Do not allow traffic from the domain `XYZ.com`." Stateful firewalls are Network layer technologies, just like stateless packet filtering.

Stateful filters solve a common security problem relating to arbitrary port usage. If an application such as FTP creates a connection to an arbitrary port above the range for well-known ports, a stateless firewall would not be able to determine if the traffic was legitimate and would drop the packet. However, a stateful firewall would have registered the FTP's connection in its connection table and associates the port number with the specific session, allowing subsequent packets to be passed through to the protected network.

The connection table contains attributes of each connection — source and destination IP addresses, port number(s) — and as packets traverse the system, it registers the sequence number. The entry in the connection table only exists for the period of the session and is deleted when the session ends.

A stateful connection enforces rules based on a current connection. [Figure 28.4](ch28.html#the_mechanism_used_by_a_firewall_apostro) shows a mechanism for handling out-of-sequence and out-of-range packets. Consider the simple example of a stateful filter where a session is under way, as shown in [Figure 28.4](ch28.html#the_mechanism_used_by_a_firewall_apostro). The last packet to pass through the firewall had a packet number of 53, and so the next packet should be 54. The IP header contains information that establishes the length of the data being sent, which for this example corresponds to a data stream 80 packets long, provided that the packet sizes are uniform.

Packet 54 is passed through the firewall automatically, but packet 60 requires a decision. In a strict firewall session, a packet with a sequence number of 60 arriving out of sequence might be cached, or more likely it would be rejected until packets 55 to 59 pass through the firewall. The condition of Packet 60 is uncertain which is why a question mark is shown in the lower-right sequence. To verify the status of Packet 60 an ACK might be sent to the sending system, asking that Packet 60 be retransmitted. A comparison can be done to establish that the new packet number 60 matches the first packet number 60. Any packet that has a packet number above 80 is automatically dropped, with the assumption that the data in it is invalid. Different stateful firewalls would have different rules for how to handle out-of-sequence packets, contention when two copies with the same sequence number arrive at roughly the same time, and other issues that arise.

![The mechanism used by a firewall's stateful filter](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2804.png)

**Figure 28.4. The mechanism used by a firewall's stateful filter**

There is overhead involved in setting up the connection and in the registration of the information. When TCP is the Transport protocol, the connection requires a successful negotiation in the form of a three-way handshake. When a system wants to create a connection, it sends a packet with the SYN bit set to `ON`. If the firewall examines the packet and finds that it comes from an approved source, the firewall sends a packet back with both the SYN and ACK bits set to `ON`. The connection is `ESTABLISHED` when the sending system sends back a second packet with the ACK bit set to `ON`.

Once a connection is established, packets conforming to the established session are allowed through the firewall. A logon request initiates a session, and subsequent packets with the correct session parameters will be allowed. Another client system that attempts a logon at the same time will have packets with header fields that do not have the necessary session parameters, and therefore those packets will be blocked from transit and dropped.

The reliance on a negotiated connection and the handshaking that is involved in setting up a connection make stateful firewall susceptible to Denial of Service (DoS) attacks. A DoS attack begins with multiple systems sending out large numbers of SYN packets requesting connections, called a SYN flood. The target starts to create the connections, eventually overflowing its connection state table, at which point no other connections can be made. DoS attacks are often implemented with zombie networks, large numbers of computers that have been infected silently by worms or Trojans.

Once the TCP connection is established, the transfer of data becomes efficient. Any packet that conforms to the connection parameters is passed through after a relatively simple read of header information. Stateful firewalls do not typically filter outgoing traffic from the destination system in the trusted zone to the system outside the firewall, the assumption being that the system inside the firewall is secure. Connections, once established, exist until a certain period of time passes without any traffic being detected, after which the connection is closed and the connection information is discarded. If an application wants to maintain the connection, it can broadcast a `keepalive` packet, or respond to a firewall's request for the application's connection state. Connections can be ended by request and do not always need to be timed out.

### Note

The structure of IP packets is discussed in [Chapter 18](ch18.html). [Chapter 17](ch17.html) describes TCP handshaking in some detail.

A connectionless Transport protocol such as UDP is handled differently by a stateful firewall than a connection state protocol such as TCP is. When a UDP SYN request appears, the connection goes to the `ESTABLISHED` state and the packets are passed through the firewall. The connection is maintained until a timeout period without data received is observed, at which point the connection is terminated. There is no mechanism for closing a UDP connection other than a timeout.

Once a stateful firewall establishes a connection, filtering incoming packets requires that the packets' header fields be read and checked against the connection state table. This turns out to be a low overhead process and is performed efficiently.

## Application filters

Application filtering filters traffic based on the application or protocols that were used to create or transmit the packet. Application filtering, which is sometimes called proxy-based filtering, is also able to determine if the traffic parameters do not match the well-known port assignment for that application type. Based on what it finds, the application filter can block, redirect, or modify packets as necessary. Application filters tend to be found on the more expensive and powerful firewalls, as they are the most sophisticated as well as the slowest filters in use.

An application filter extends the idea of a stateful filter to block traffic based on what protocol the packet is using, as well as how the protocol is being used. In a stateful filter, the firewall might have a rule that states "Allow all traffic through port 80," which is the well-known port for HTTP traffic. Many applications transport their data over HTTP in order to be compatible with browser-based interfaces. An application filter would then add the following rule: "Block HTTP traffic that contains VoIP data." Because an application filter can look inside the packets and determine what application is being used, it can apply this rule, whereas stateful and stateless filters cannot. An application filter may be considered an extension of a stateful filter.

An application firewall that examines traffic carried by the HTTP protocol and other related protocols such as HTTPS, SOAP, XML-RPC, or any other Web service for its content, is called a Deep Packet Inspection Firewall. Deep packet inspection can identify non-conforming content by comparing the data contained within the packet to a database of attack signatures, or by determining if the behavior of the Web traffic doesn't conform to normal application behavior.

Application filters are particularly useful because they can be dynamic and react intelligently to conditions. Consider the situation where an application filter monitors traffic coming into port 53, which is the well-known port for DNS. During a DNS DoS attack, requests for DNS assignments overwhelm the system and the firewall closes port 53 in response. If the firewall were a stateful firewall, it would simply close port 53. However, an application filter could determine if an internal system is requesting a DNS service from an outside system and dynamically open port 53 to let that request pass out of the firewall. Once the application filter passes the DNS request, it logs the request's state conditions into a state table. Now when DNS data is returned from an outside system in response to the internal DNS request, the application filter reads the data, recognizes that it is a valid response based on session data, opens port 53 for that incoming DNS data, and sends the response to the requesting system inside the network. It's easy to see how valuable it can be to have this feature. Even while under attack, your network would still allow the address resolution your network systems need for browsing and a myriad of other services to proceed.

Application filters tend to be added onto firewalls capable of processing them as needed. You may start out with a basic set of application filters such as a DNS filter, and then add or purchase filters for virus detection, content screening, lexical analysis, or site analysis.

### Note

Lexical analysis is the method used to convert a string of characters such as source code into a sequence of tokens, a token being a categorized block of text or lexeme such as a keyword, identifier, literal, or punctuation. During lexical analysis, lexemes are categorized by function, which provides their context or meaning. The process of categorization is called tokenization. Lexemes are sent to a parser where the sequence of tokens is analyzed according to the rules of grammar of the particular programming language that created them.

Keep in mind that Application-level firewalls typically support clear text analysis but aren't able to filter encrypted traffic. If you had a Web site with an online store that used SSL encryption, the protocol commands would be hidden in the encrypted data. Firewalls with Application-level filtering tend to handle encrypted communications in different ways. Among the approaches used are terminating the SSL packets at the firewall, decrypting and re-encrypting the packets on the firewall before sending them onto the Web server, or simply passing the SSL packets through the firewall to an internal server for further handling.

## Deny by default

A standard principle used by any highly secure technology is to have the device initialize to a *deny by default* state. Many firewalls, proxy servers, and other security systems come completely locked down out of the box. This can be something of a shock to anyone who hasn't encountered this situation before. When confronted with a completely blocked system, the administrator is advised to turn features on one at a time as needed. The following sequence of rules is typical:

- **Deny all traffic unless a rule specifically allows it**. This is the *deny by default* condition.
- **Block all incoming packets with internal addresses and all outgoing packets with external addresses**. These packets are typically either from attackers or errors.
- **Configure DNS traffic appropriately for both UDP- and TCP-based DNS queries**. Without address resolution, most other functions on a network won't work.
- **Enable HTTP and perhaps HTTPS traffic by opening port 80, and route this traffic appropriately**. If a proxy is used for this traffic, you'll want to configure it as a connection endpoint. For example, Microsoft ISA Server can be a Web proxy, and requires that HTTP traffic be routed over port 8080. The well-known port for HTTPS is assigned to port 443, so redirection of HTTPS traffic to either port 80 or 8080 is meant to provide a simplification for network administrators for internal traffic.
- **If you are using mail servers, enable SMTP and/or POP3 by opening their ports**.
- **If your network allows it, open the FTP ports 20 for data and 21 for control**.
- **Respond to pleas for help by individually turning on ports or routes as you learn about network functions that require access**.

These rules are applied starting at the bottom of the list and working their way up. That is, the rules have an order or precedence in which they are applied. In Microsoft ISA Server, different firewall scenarios are offered and a basic set of rules are generated from the network security template. [Figure 28.5](ch28.html#an_isa_server_apostrophy_s_firewall_rule) shows one of these scenarios in ISA Server 2006.

![An ISA Server's firewall rules when configured as a Three-Leg Perimeter firewall](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2805.png)

**Figure 28.5. An ISA Server's firewall rules when configured as a Three-Leg Perimeter firewall**

The point of this exercise is to keep your network as locked down as it can be while still allowing all necessary functions to be operable. With luck, you will be able to save your rules and export them to other devices of the same types.

## Network Address Translation

Network Address Translation (NAT) is a fundamental routing mechanism that allows the network addresses of datagrams or packets to be substituted based on entries in a mapping table. What makes NAT particularly valuable and a subject in a chapter on firewalls and gateways instead of routers is that NAT is able to route traffic to private network addresses, which are otherwise unroutable. Essentially, NAT expands a single, assigned static IP address into a network of addresses. Without NAT, IPv4 would have long ago run out of available IP addresses.

When a device applies NAT to an incoming packet, it rewrites the destination address in the packet header. The entire range of devices on the private network is hidden from outside view, with only the single address of the external network interface of the routing device exposed. NAT is a general function that can map any one address to other addresses, not necessarily private IP range addresses. Outgoing packets are subject to the reverse mapping; NAT rewrites the source address of the packets (which were private IP addresses) and replaces it with the IP address of the router's external network interface that is routable.

Examples of NAT software may be found in:

- Cisco's Internetwork Operating System (IOS)
- Microsoft Windows Internet Connection Sharing (ICS) feature
- IPFilter (`http://coombs.anu.edu.au/~avalon`), an open source package available in many UNIX implementations such as FreeBSD, NetBSD, and Solaris 10
- Packet Filter (PF), a NAT filter included with OpenBSD, and available on many other operating systems
- Netfilter, also known as iptables and included in some Linux distributions
- WinGate (`www.wingate.com`), an Integrated Gateway Management system for Windows
- Microsoft Internet Security and Acceleration Server, a proxy and caching server installable on Windows Server 2003 or 2008

When you set up NAT, you can hardwire the mappings in the map table to create what is known as static NAT. The basic form of NAT rewrites the destination of incoming packets and the source of outgoing packets during NAT traversal. The more advanced form of NAT alters the IP addresses as well as the source port and destination port assignments needed for port forwarding routed traffic. This form of NAT is referred to as Port Address Translation (PAT), Network Address Port Translation (NAPT), or by Cisco as NAT overloading. All versions of NAT require that packets have their CRC (Checksum) recalculated and the CRC fields of the packets' headers rewritten during each traversal.

### Note

In rare instances, packets do not have assigned port numbers; they appear on varying ports. This is true for the Internet Control Message Protocol (ICMP, which PING relies on), the Real-Time Control Protocol (RTCP), and the Real-Time Protocol (RTP), for example. RTP comes in on an even UDP port number, and any corresponding RTCP packets will then appear at the next higher odd port number. The RTP and RTCP protocols are described in detail in [Chapter 25](ch25.html), as is their method for NAT traversal called the Session Traversal Utilities for NATs (STUN) protocol.

While the effect of a NAT traversal is easy to understand, the manner in which NAT operates within the routing device is not that easily explained. There are several different ways to map ports to systems, addresses to ports, and addresses to addresses. Let's take a look at some of the common mapping schemes that were defined as part of the original STUN protocol. [Figure 28.6](ch28.html#four_different_nat_traversal_mapping_sch) shows four common NAT mapping schemes — One-to-one or Full Cone NAT, Address Restricted Cone NAT, Port Restricted Cone NAT, and Symmetric NAT. Below each diagram is the mapping table that the router/switch uses to create the virtual circuits over which data flows. Mapping entries may not always be unique, and so one hopes that the algorithm a device uses to map with at least picks an optimum traversal route.

The routes illustrating each of these different mappings appear in bold type in the map table, and to simplify the conversation, ports are shown in the half-duplex mode. The shapes you see in [Figure 28.6](ch28.html#four_different_nat_traversal_mapping_sch) illustrate four different systems that are involved in the communications:

- Client system, labeled 1, with two ports labeled S1 (Source 1) and D1 (Destination 1). In the case of Symmetric NAT, Client 1 contains two source ports, S1 and S4.
- NAT traversal device. In the center of each diagram, the NAT device has an internal and external side, both of which are labeled. Ports on the NAT are E1 and E2 (External 1 and 2), and I1 and I2 (Internal 1 and 2). Symmetric NAT has additional internal ports.
- Internal System labeled 2, with two ports labeled S2 and D2.
- Internal System labeled 3, with two ports labeled S3 and D3.

The first mapping shown in the upper-left corner of [Figure 28.6](ch28.html#four_different_nat_traversal_mapping_sch) is a one-to-one correlation of an internal port to an external port, called Full Cone NAT. In this scheme, ports E1-I1 and E2-I2 are each hardwired together. Traffic can flow from any client to any internal system or from any internal system to any client using either or both of these two routes. This type of NAT is simple and doesn't require much logic to implement. It tends to be used on lower-cost switches.

In the upper-right corner of [Figure 28.6](ch28.html#four_different_nat_traversal_mapping_sch), a scheme called Address Restricted Cone NAT is shown. Here the mapping from an internal system to an external system is based on the IP addresses of the two systems. NAT traversal begins when an internal system (shown as 2 here) negotiates a connection with an external client. Communication proceeds by mapping the addresses S2 to D1 and S1 to D2 with a unique route. Shown in the figure, the routes cross in the NAT, but they could also have been drawn as E1-I1 and E2-I2, as only the address mapping matters. When System 3 tries to communicate through either of the internal ports to Client 1, the NAT device recognizes that the address isn't mapped to a current session and blocks traffic in or out of the ports shown. For System 3 to communicate, it would have to establish a connection through another set of ports.

In the Symmetric NAT scenario shown in the lower-right corner of [Figure 28.6](ch28.html#four_different_nat_traversal_mapping_sch), all requests from an internal IP address and port combination to an external destination IP address and port combination are mapped to the same external IP address and port combination. When the same system sends traffic to two separate IP addresses, traffic is split so that each destination travels on a separate path. In the figure, Client 1 is sending data to two different IP addresses and as a result, each system IP/port address pair is unique. Communication from an external system requires that an internal system negotiate the connection first.

The final example, Port Restricted Cone NAT, shown in the lower-left corner, is similar to Address Restricted NAT but instead of blocking an IP address, the NAT restricts access to a port or ports. In this one example, port I1 is forced to operate in full-duplex mode to allow Client 1 to communicate with System 2, as port I2 is blocked.

Most vendors choose to combine different aspects of this mapping in their devices. For example, a common implementation chooses to combine Symmetric NAT with static port mapping, depending upon which direction the traffic originated from and is directed to.

![Four different NAT traversal mapping schemes](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2806.png)

**Figure 28.6. Four different NAT traversal mapping schemes**

Another scheme maps ports Ex to Ix, where x in both instances is the same number, and then directs traffic from any other internal systems to the same host to a randomly selected port. When a system of this type is examined, it would appear to be a Symmetric NAT when multiple ports are used to connect to the same host, and an Address Restricted Cone NAT at times when there is only one connection from internal systems to an external system.

Additional NAT techniques must be used to handle IP control packets such as ICMP, and to work around instances where the NAT translator cannot correctly parse TCP or UDP data. In those instances, NAT must recompute both the TCP/UDP header and a new CRC field. NAT can often have trouble parsing encryption, IPsec being one example. The lack of a standard technique to work with transport protocols is a major reason why the developers of IPv6 chose to stay well clear of NAT.

You may also encounter some vendor-specific NAT implementations. Destination NAT (DNAT) is a technique where the destination of a packet is changed when it is outgoing, and then changed back after the destination system replies. DNAT allows an internal service to be published at a public IP address, even though the data originates on a private network.

Many times, SNAT refers to the term Source NAT, but not always. Some large vendors use the term differently. The acronym SNAT is used by Microsoft as part of their Internet Security and Acceleration (ISA) Server to mean Secure NAT. To Cisco, SNAT stands for Stateful NAT. The IETF calls SNAT Software Network Address Translation, and the technology refers to the address translation required to connect IPv6 and IPv4 networks together.

With so many variations on a theme, it's no wonder that the original name for the STUN protocol — Simple Traversal of User Datagram Protocol through Network Address Translators — had to be changed to Session Traversal Utilities for NAT; it is anything but simple.

NAT is not a transparent process, and there are several different application and protocol types that break when they try to send data across a NAT translator. The most problems arise with applications that rely on different data streams to send data and to control a session, FTP and SIP being the most prominent examples. SIP is the control protocol for Voice over IP. It is for this reason that technologies such as STUN or Internet Connectivity Establishment (ICE) were developed to aid in NAT traversal. Other potential solutions to NAT traversal problems involve the use of automatic device discovery technologies such as Universal Plug and Play (UPnP) and Bonjour (NAT-PMP), when enabled by the NAT translator. Bonjour couples network address translation with the port mapping protocol.

# Proxy Servers

A proxy server is a computer or application that serves as an intermediary between a client and a network service. Client requests received at the proxy server are forwarded to the service, and the results are sent back to the proxy where they are forwarded to the client. The proxy service performs a redirection function, does none of the processing of the requests, and is the only system that the client or the service sees during this transaction. In this form, a proxy server may be called a gateway, or less often, a tunneling proxy.

Because the term *gateway* tends to be more appealing from a marketing standpoint than the term *proxy server*, you rarely encounter a proxy server that passes all requests and replies through the system unchanged. Proxy servers usually have additional actions associated with them. To my mind, a proxy server is a cross between a firewall and a gateway. A proxy server can communicate in HTTP to a Web server or to a client's browser, as well as communicate in SMTP to a mail server or FTP to an FTP server; this is so that applications behind the proxy server do not need to understand protocols other than the ones that they were designed to understand. Proxy servers are implemented as hardware or as software; they can be stand-alone servers, or they can be software (a proxy service) running on the same computer that has the application that the proxy server fronts for. [Figure 28.7](ch28.html#the_essential_functionality_of_a_proxy_s) shows the essential element of a proxy service as a high-level protocol translator and as a surrogate for Web access for clients.

![The essential functionality of a proxy server, a cross between a firewall and a gateway](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2807.png)

**Figure 28.7. The essential functionality of a proxy server, a cross between a firewall and a gateway**

Here are some of the better-known proxy servers:

- Apache HTTP Server (`http://httpd.apache.org`)
- Blue Coat SGOS (`www.bluecoat.com`)
- I2P (`www.i2p2.de`)
- Microsoft ISA Sever (`www.microsoft.com/forefront/edgesecurity/isaserver/en/us/default.aspx`)
- Novell BorderManager (`www.novell.com/products/bordermanager`)
- Privoxy (`www.privoxy.org`)
- Squid (`www.squid-cache.org`)
- Sun Java System Web Proxy Server (`www.sun.com/software/products/web_proxy`)
- Tinyproxy (`www.banu.com/tinyproxy`)
- Tor (`www.torproject.org`). Tor is discussed in detail in [Chapter 9](ch09.html).
- Varnish (`http://varnish.projects.linpro.no`)
- WinGate (`www.wingate.com`)
- yProxy (`www.yproxy.com`)
- Zeus Web Server (`www.zeus.com`)
- Ziproxy (`http://ziproxy.sourceforge.net`)

Proxy servers often have many of the features of a firewall. Some proxy servers can filter traffic based on content, domains, URLs, MIMEs, keywords, or on the basis of URL patterns and content attributes. Others can use whitelists to pass traffic through the proxy server or blacklists to deny access. Proxy servers are not effective when examining encrypted traffic and will pass encrypted traffic through without being able to apply content filtering to it.

Because many actions that proxy servers take are important events and may need to be analyzed at some point, nearly any proxy server will log information about its decisions into a log file, which is almost always in a standard database or spreadsheet format such as CSV. One important set of security filters that proxy servers should be able to apply is access to proxy services based on the user's security credentials; this may require a user login.

One common enhancement is to add a disk cache to the proxy server and the logic necessary to know when a request has already been served. A caching proxy will then return the matching results from the cache instead of passing the request again onto the service. Caching is always a feature associated with any proxy server that is handling Web traffic, and in those instances, the proxy may be referred to as a *Web proxy*. Nearly all Web proxy servers serve to mask the true identity of a user connecting from one network to another (most often the Internet), and as such, they can be considered either an open proxy or an anonymous proxy.

There are many instances where network services do not want to forward traffic from an open proxy server, with e-mail and IRC traffic being two instances. Some systems test for the presence of an open proxy, while others consult known lists of open proxy systems and deny transit of their data through the system.

## Transparent proxy servers and honeypots

Because a proxy server can hide the identity of users on one network from another network, it is possible to use proxy servers as a means to examine traffic that flows between two endpoints, which can be done for many purposes. When this is done for nefarious purposes, the proxy may be referred to as a hostile proxy; when it is done to intercept traffic and impose a set of policies, the proxy may be referred to as an intercepting proxy. An intercepting proxy has the functionality of a gateway and may be transparent to the user. Cisco uses the term *transparent proxy* to define a router Web Cache Control Protocol that is used to determine which routes to send traffic on based on the cache content, another form of redirection.

Another use of proxy servers is to create security traps called *honeypots*. A honeypot is used to lure unauthorized users of a network to that system, where their actions can be monitored and their identity can be discovered. Honeypots that appear to be open proxy systems are sometimes referred to as a *sugarcane*. A honeypot should not contain any data of value, nor should it be a production system. Because the idea is to allow an intrusion, it is important that the honeypot be carefully isolated from any other systems of value. Special programs, called victim hosts, are sometimes used to create seemingly important information. Victim hosts can be decoys that are meant to distract intruders; they can also be structured to provide detailed information about the nature of any attack.

## Reverse proxy servers

In all of the instances mentioned so far, the proxy server fronts a service. However, there is one form of proxy server, called a reverse proxy, where the service passes data directly to the proxy server instead. The most common example of a reverse proxy is when you have Web servers sending data to a local proxy server for additional processing.

The reverse proxy server may perform Secure Socket Layer (SSL) encryption/decryption for the Web servers using an SSL accelerator or offload module, and by doing so for multiple Web servers, the reverse proxy server can allow the Web servers to use the same SSL Server Certificate used by the reverse proxy server. A reverse proxy server may offer faster compression, and the ability to publish the service to another network, which is called Extranet Publishing. Caching content is almost always a feature of a reverse proxy server.

[Figure 28.8](ch28.html#a_reverse_web_proxy_appears_to_be_the_we) shows how a reverse Web proxy is deployed.

![A reverse Web proxy appears to be the Web server or servers themselves.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2808.png)

**Figure 28.8. A reverse Web proxy appears to be the Web server or servers themselves.**

On the left side of [Figure 28.8](ch28.html#a_reverse_web_proxy_appears_to_be_the_we), a request is made by a client outside the network for a static page called Web Page_1 from a Web server within. The request goes to the proxy server. As a first step, the proxy server, knowing that this is a static page, checks its cache, finds Web Page_1, and serves it up from the cache to the client. It has performed the service of the Web server. In the second scenario, the client asks for Web Page_2. After checking its cache and not finding that page, because dynamic pages should never be cached, the reverse proxy server sends a request to one or more of the Web servers to provide Web Page_2. Web Server_1 either finds the page (static content) or creates the page (dynamic content) and then sends it to the proxy server for forwarding to the client. Again, as far as the client is concerned, the proxy server is the Web server. A reverse proxy server plays the role of the application or service it fronts.

The benefits of this approach are that the cache accelerates performance, the proxy server can load balance between the three Web servers, and if one Web server needs content from another Web server, the proxy server can fetch it. As a result, the proxy server makes the Web servers much more efficient.

# Summary

Firewalls offer advanced protection against a number of network hazards. They increase protection of a network, making it much harder for outsiders to gain unauthorized entry to private networks. Firewalls use filters to decide how to handle incoming and outgoing traffic. Advanced firewalls can use Deep Packet Inspection to understand the content of packets. Firewalls are placed at different points in the network for different purposes.

Network Address Translation takes requests from clients on the public network and forwards them to systems inside a private network. This feature allows private network systems to maintain their anonymity.

Gateways are systems that serve as the interface between two different networks. A proxy server is a cross between a gateway and a firewall. Proxy servers serve as the surrogate for systems on a private network.

In the next chapter, you learn about Virtual Private Networks, which allow you to create secure communication channels between computers, regardless of where those computers are located.
