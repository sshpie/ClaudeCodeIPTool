# Chapter 9. Routing, Switching, and Bridging

**IN THIS CHAPTER**

- Circuit versus packet switching
- Hubs, repeaters, bridges, routers, and gateways
- Routing methods
- Anonymous communication with onion routers

Networks require connection devices that can create circuits. Common connection devices such as hubs, bridges, switches, routers, and gateways are described and compared with one another. This chapter explains the two broad categories of networks: circuit switched and packet switched. A circuit is a defined path between two endpoints. Circuit switched networks are stateful and can be described in terms of endpoints and a path. Data travels over the circuit and arrives in sequence. Packet switched networks are stateless. They have endpoints, but the path varies for individual packets based on conditions.

Switching devices can be categorized by the highest level in the OSI data model that they operate on. Hubs and repeaters are the simplest devices; they are simply physical connections. Bridges are devices that span two different network segments, but do not provide protocol translation. A router can connect two different types of networks. Switches and gateways are general terms that describe a variety of different systems.

# Circuit versus Packet Switching

Broadly speaking, there are two types of switched networks in use: circuit switched and packet switched. A circuit switched network is defined by a physical or virtual circuit (or connection) that connects two endpoints and has a certain circuit bandwidth. A circuit only needs to be defined for the duration of the message transfer on a circuit switched network. Because switching devices can be used to redefine different connections, a circuit switched network can be reconfigured as needed.

The penultimate circuit switched network is the Public Switched Telephone Network, or PSTN. When you place a phone call to another party, a circuit is created between the two of you for the duration of the call. Circuit switched networks are data networks as well as voice networks. Another example of a circuit switched network is ISDN (Integrated Services Digital Networks).

The best way to think of what a circuit switched network does is to remember that circuit switched networks are stateful. Stateful means that you can define a message transfer in terms of:

- A source
- A destination
- A path of the circuit
- A cost for the path based on time, performance, or some other weighting

In a circuit switched network, you can represent nodes as a graph in graph theory, connections as weighted edges between nodes, and the actual defined or preferred paths through the graph, which are called routes. In real terms, messages are sent from endpoint to endpoint as a complete unit. If you have multiple IP packets (or datagrams), they all travel down the same route on a circuit switched network.

A packet switched network is based on a different concept, that of the best available route. On a packet switched network, individual packets are sent from a source to a destination by the best connection available at the switching device. This type of network is designed for inherently unreliable networks where connections are transient. If a connection drops out, the next packet is sent to a different next hop. A packet switched network cannot guarantee a path. A certain percentage of packets will reach a dead end where, as they say in Vermont, "You can't get there from here," and so some packets will get dropped or returned. Packets will also arrive out of sequence. Therefore, packet switched networks require a mechanism to ensure that all lost packets are resent and that packets can be sequenced to retrieve the data that they encode.

Of course, the prototypical packet switched network is the Internet, or more broadly speaking, networks based on the Internet Protocol. Other networks that are packet switched are X.25, Frame Relay, Asynchronous Transfer Mode (ATM), and Multiprotocol Label Switching (MPLS), among others.

The best way to think of what a packet switched network does is to remember that packet switched networks are stateless. Stateless means that you can define a message transfer in terms of:

- A source
- A destination
- The position of the packet in the sequence
- A Time-to-Live (TTL) for the packet, which may be based on a hop count or timeout parameter, and is the time after which the packet expires and is dropped at the next device that receives it.

### Note

A circuit is not the same thing as a connection. A connection is a defined transfer of data from one endpoint to another, and it may be stateful or stateless.

Circuit switched networks have their advantages and disadvantages over packet switched networks. A circuit switched network sends an entire message over the same circuit, which can be faster than sending parts of a message over many paths. When a message arrives, the data arrives in sequence and doesn't need to be reassembled. By contrast, a packet switched network makes better use of the network's capacity because it can distribute traffic over many connections. The extra overhead involved to sequence incoming packets and the loss of performance is offset by the more efficient use of the network and the much higher fault tolerance offered by packet switching. Neither model, whether circuit or packet switched, is better than the other; they are simply different.

What both circuit switching and packet switching have in common is that they both have switches that can change the network's topology. To understand modern networks, you need to understand how switches operate. Switches not only control the physical connections between network segments through electrical connections, but different classes of switches also have the intelligence to measure the performance of different paths, determine routes, and optimize the preferred paths or routes to nodes on the network in a stored but dynamic table. Internetworks and WANs would not function without the use of these types of routing devices.

[Figure 9.1](ch09.html#different_types_of_network_switching_dev) summarizes the different types of network switching devices in a single chart. Network switching devices are best characterized by the highest layer of the networking model that they can operate on. Physical layer (Level 1) switching devices have no intelligence; they are simply physical connections or, for a repeater, a physical connection with signal regeneration. Data Link layer (Level 2) devices are characterized as switches or bridges and add the ability to reconfigure connections through device management.

All of the network switching devices so far span networks of similar construction and that usually run the same network protocols. To span networks of different types, additional intelligence is required and devices must operate on higher-level protocols. Two classes of devices become important in internetworking: routers and gateways. Routers connect different network types at the Network layer (Level 3), while gateways connect networks running different protocols at the Transport layer (Level 4). As you ascend the chart of devices in [Figure 9.1](ch09.html#different_types_of_network_switching_dev), they become more capable and more intelligent, more manageable, and also more expensive. In [Figure 9.1](ch09.html#different_types_of_network_switching_dev) the different OSI layers are listed on the left from Level 1 at the bottom to Level 7 at the top. The different network connection devices that correspond with connections at that layer are shown. They are:

1. Physical layer (Level 1). Devices at this level include repeaters and bridges.
2. Data Link layer (Level 2). Devices at this layer include hub, and switches.
3. Data Link layer (Level 3). Devices at this layer are primarily routers.
4. Transport to Application layers (Levels 4 through 7). Devices of this type are called gateways.

All of these devices are discussed in the sections that follow. An explanation for why they are categorized as such is also discussed.

![Different types of network switching devices](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0901.png)

**Figure 9.1. Different types of network switching devices**

# Layer 1 and Layer 2 Connection Devices

Layer 1 and Layer 2 devices form the majority of switching devices sold today. These devices include hubs, repeaters, bridges, and switches. Repeaters (or active hubs) and passive hubs are unmanaged devices. Bridges and switches are more often managed devices. A managed device contains a network management protocol such as SNMP (Simple Network Management Protocol) and can be seen and modified within a network management program. An unmanaged device doesn't allow for remote configuration or diagnosis. The network switch is the most elusive of the devices described in this chapter. A switch is not defined by a standards body and is used by vendors to describe devices with a very large range of capabilities. In the sections that follow, repeaters, bridges, hubs, and switches are described.

## Passive hubs

A hub is a simple device that connects network devices together on the same network segment, usually twisted-pair wire or fiber optic cable. A hub is a passive hub when it serves to simply connect one connection to another. It is an active hub when the signal is amplified, and in that case it is most often called a repeater.

In the OSI model, it is a Physical layer (Level 1) device. Hubs play the same functional role that a connector performs, lengthening a network segment by joining two wires together. However, network hubs offer the additional feature of fan-out; they take an input connection and allow it to be connected to 4, 8, 16, or more other connections, with each path through the hub being a separate network segment. Hubs can be passive and simply pass signals through, or they can amplify the signal (repeat) and be classified as active hubs.

Hubs have little or no intelligence, per se, and are unmanaged devices. Every packet coming into the hub goes out through the other connections, and all connected network segments belong to the same collision domain. These two factors mean that traffic flowing through a hub suffers more collisions than through other connecting devices such as switches or routers. It also means that the collision rate tends to increase exponentially as a function of the number of hubs encountered while en route between connection endpoints. As a general rule, 100-Mbits/s Ethernet circuits are limited to no more than two hubs connecting three network segments.

The more modern hubs act as multiport repeaters. When they detect a collision, the hub sends a jam signal to all connected devices to stop transmitting; some hubs act when they detect a significant number of collisions on one port to partition that port so that it can no longer communicate with other connected ports.

Hubs often offer an uplink port, which, when enabled, makes the two hubs function as if they are a single hub. In some cases, a connection between two hubs can be a stack port, which improves the performance of the connection and allows more hubs to be used together. Stack ports use proprietary technology; therefore, you need two hubs from the same vendor to get them to work together. When you combine the ability to stack hubs together with an SNMP chip or VLAN support, the added features allow the hub to be a managed device, and many vendors refer to them as intelligent hubs.

In the past, hubs' main attraction was that they were cheap and reliable; however, hubs are now obsolete and very difficult to find in the marketplace. Although you can still purchase autosensing 10/100-Mbits/s Ethernet hubs, most devices sold today are switches. This is certainly true for any device that connects Gigabit-speed networks. Because most network devices are based on just a few vendors' chipsets, and because there is so little difference now in the cost of adding all of the intelligence of a switch to the chipset, there's no discernable difference between the cost of a hub and that of a switch.

You will find that nearly all devices are sold as switches, even if they use the word hub in their product name. Modern switches are only hubs in the sense that you can turn off all of the features that they offer and simply plug in your devices. The ability of a hub to copy data through broadcast to many connected devices at once is a desirable feature that is emulated in switches by a function called port mirroring.

## Repeaters

Repeaters, or active hubs, are Physical layer (Level 1) devices that extend the run length of the physical media by amplifying and retiming the signal before forwarding it. Signals can be degraded over the length of a connection losing their modulation. A repeater recreates the signal and retransmits it in the correct phase and frequency. Repeaters can connect different physical media together, and extend the collision domain without adding any new traffic. Repeaters cannot connect networks using different network architectures together, nor can they filter information. As a signal travels through a repeater, it suffers a small latency called its propagation delay. This factor tends to limit the number of repeaters that can be used on any single segment of a network.

Ethernet has such long run lengths relative to most LAN requirements that repeaters are uncommon. Most wired Ethernet repeaters are sold as "active hubs," and they are sometimes referred to as multiport repeaters. It's rare to find repeaters sold for Ethernet networks, as hubs and switches have become available at more affordable prices. For this reason, wired Ethernet repeaters are deprecated by most organizations. This is not the case for other types of networks.

### Tip

When using repeaters, try to use network segments of the same length in order to maximize the amplification feature.

Wireless 802.11*x* networks have limited coverage, and so it is common to add repeaters to the network to extend network coverage. Although you can buy special wireless repeaters, most of the devices used as repeaters are access points that have been placed in a state called *repeater mode*.

Repeaters become important in network media transmitting light waves. Depending upon the signal attenuation of the media, repeaters may be required at specific intervals throughout the network. This is the case with SONET networks, which are used to transmit much of the telephone data in the United States. As you move to WAN network connections, repeater technology becomes more important.

# Switches

A switch is an active device that connects two network segments together at one or more levels of the OSI network model. The term *switch* is applied to a broad variety of devices, and unlike the function of a *bridge*, which is defined by the IEEE 802.1D standard, no such definition exists for a switch. The term switch is more a marketing term than anything else, and is often used when describing a hub, repeater, or bridge when the switch vendor thinks that the term is more valued by the consumer. Indeed, Layer 2 switches are bridges under the IEEE 802.1D standard and are sold as switches by most vendors. Switches have the ability to define virtual circuits that pass through them, but often lack the additional intelligence to provide dynamic reconfiguration of their circuits on the fly without outside intervention. The ability to dynamically reconfigure circuits provides a means to reroute traffic from one input to a different output based on network conditions or as the result of an optimization algorithm.

Switches can be managed or unmanaged. An unmanaged switch cannot be configured over the network, while a managed switch can be. Managed switches usually include an SNMP (Simple Network Management Protocol) agent, Command Line Interface with console, or perhaps a Web browser interface. A smart switch is one that includes a small set of configurable settings and is differentiated from an enterprise-level, fully managed switch that has functions such as the ability to create and store different configurations. Enterprise switches usually have higher port counts and can be stacked into larger manageable units.

When considering switches, you should look for the following features:

- **Ports**. The port count, ability to prioritize ports, and port mirroring.
- **Speeds and feeds**. The port speed and duplexing capabilities affect the throughput of the switch.
- **Link aggregation**. The ability to send data over multiple connections to the same endpoint.
- **SNMP**. The ability to participate in network discovery and management.
- **Filtering**. The ability to segment traffic based on the physical identification of devices (for example, MAC filtering). Network Address Translation, or NAT, is considered to be a function of a firewall or router and generally isn't found in switches, although there are exceptions to this rule.
- **Network Access Control**. The ability of a switch to provide a bridging function between two different networks. This is important for wireless switches, which provide access to Wi-Fi networks.
- **VLAN**. The ability to create a logical group of systems comprised of a single broadcast domain. By segmenting networks into broadcast domains you can greatly isolate network traffic and reduce network utilization providing more network overhead.

You will find switches that have capabilities ranging from the Data Link layer (Level 2) up to the Application layer (Level 7, the top layer) of the OSI network model. Only passive Physical layer (Level 1) devices such as hubs and repeaters aren't called switches by some vendors.

In Ethernet networks, all ports on a hub receive the same broadcast data; there is no segmentation at the hub and all segments belong to the same collision domain. In order to limit collisions, hubs operate in the half-duplex mode over a shared connection. Switches segment communications so that each network segment has its own dedicated bandwidth, runs in its own collision domain without collisions, and can support a full-duplex mode.

Perhaps the most useful way to describe a switch is to define it in terms of the functionality at each of the levels it supports. A Layer 2 switch is one that technically satisfies the IEEE 802.1D standard for a network bridge. The function of a Layer 2 switch is described later in this chapter. Similarly, when a switch uses a Layer 3 protocol, it is serving the function of a router; this function is also described later in this chapter. Dense multiport switching devices, referred to as Director switches, are Layer 3 devices, and are used on different network types, such as PSTN and Fibre Channel SANs, to connect hundreds of devices together. Usually the situation isn't as clear-cut, and a switch can perform services at two or more layers. Switches of this type are sometimes referred to as multilayer switches.

You may encounter two other types of switch devices: Layer 4 and Layer 7 switches. A Layer 4 switch is one that has had network address translation, or NAT, added to it, and performs load balancing between ports. Layer 4 devices can include stateful firewalls, IPsec gateways, and VPN concentrators. Usually, Layer 4 switches are sold as firewalls, as this term seems to have more cachet with the market. Layer 7 switches offer Application layer services and are most often encountered serving as a content delivery server or as an Internet caching appliance. It's rare to find a Layer 7 switch described as such; more often, they are referred to as servers because that is the stronger marketing term.

# Bridges

A network bridge is a device that spans two network segments (one subnet) together at the Data Link layer (Level 2). Bridges examine network traffic using the MAC addresses of the destination and not any of the network protocols such as IP, IPX, NetBEUI, and others that are being used. Bridges are also used when you want to connect to different types of physical media, such as 100Base-T and Wi-Fi, or 100Base-T and100Base-TX.

A bridge on an Ethernet network often functions as a transparent network device or adaptive bridge, which means that it compares the MAC address to a forwarding table and then sends the frames on to the destination if an entry exists. When there is no entry or when the table is new, the frame gets broadcast, and when a response is given, that MAC address is recorded in the forwarding table with the associated route. Adaptive switching actually describes the ability of a bridge to switch between three other modes:

- **Frame store and forward**. This method buffers incoming frames, verifies the checksum, and then forwards the message onwards.
- **Cut through**. The frame's envelope is read to determine the destination MAC address, and then forwarded based on the forwarding table entry. No error check is performed.
- **Fragment free**. The first 64 bytes of the frame are read and checked for validity before being forwarded. The idea is that checking the address is almost always good enough to determine if the data is intact or if a collision made the data unusable. The duty of error checking is passed on to devices running higher-level protocols.

Bridges on Token Ring networks use a different method for resolving how to forward traffic, called Source Route bridging. This system broadcasts an All Route (AR) frame that has a certain Time-to-Live (TTL) measured in network segments or hops. As the AR moves around the Token Ring, each bridge registers its location, decrements the TTL counter, and records any new information. When the counter is set to zero, the AR frame is dropped. The system assigns a best route based on the identity of the first AR frame to arrive, ignoring any additional AR frames. Single Route frames that contain the data the network transports are then created with specific destinations and routed to the destination based on AR data stored at the bridge. The system of Source Route bridging tends to distribute data traffic throughout the network and responds to congestion by rerouting traffic over different paths.

Bridges are typically employed when you have two groups of computers for which most of the communication is intragroup, and a smaller portion of the communication is intergroup. An example would be a network with one floor of networked systems for accounting and another floor for engineering. Alternatively, it can separate different clustered groups of systems, such as Linux computers from Macintoshes. When used in this manner, a network bridge improves the performance of both groups by partitioning most of the traffic to half of the entire network, lowering the collision rate.

Nearly all of the devices you can buy that are labeled as a bridge are wireless access points configured to bridge between two networks or network segments. On a wired network Layer 2, switches are set into a bridging mode, and so you may encounter the term network switch as a synonym for a network bridge. In most instances, when the term bridge or network bridge is used on Ethernet networks, the term applies to any network device that conforms to the IEEE 802.D standard. The Spanning Tree Protocol that is described in detail later in this chapter is a routing standard that operates using interconnections described as bridge nodes.

A network bridge is characterized by the following features:

- A bridge doesn't interact with any network protocol at a higher level than Address Resolution Protocol (ARP), Neighbor Discovery Protocol (NDP), or Open Shortest Path First (OSPF), all of which are Link Layer protocols in the TCP/IP network model.
- A bridge separates two collision domains, processing and regenerating packets.
- Regardless of the number of ports available, a bridge has one port that forwards information and another that distributes information. That is, from a network standpoint, a bridge has only one network interface.
- A bridge does not determine routing, but can filter packets based on their destination MAC addresses.
- There are no limits to the number of network bridges on a network, and the limitations placed on network segments do not extend across a network bridge.
- A port is logically part of one bridge only.
- When a port is added to a bridge, it becomes unmanaged because network bridges are self-configuring.

A network bridge or an unmanaged switch is one that doesn't take an IP address and therefore can't be `PING`ed or respond to network commands. The datagram transfer function of a bridge spanning two different network segments doesn't require that a bridge be managed. However, many devices, such as switches functioning as logical bridges, are managed, have an IP address, participate in SNMP network communication, and can be accessed by commands such as Secure Shell (SSH), `TELNET`, or `RLOGIN`. Using these methods, you can work with a managed bridge to set the IP address of the virtual interface, which can communicate with other network interfaces. Traffic from other network endpoints is passed through the managed bridge without interaction.

If you have configured network interfaces on Windows XP or Vista, you might have encountered the Windows network bridge. The Windows network bridge is a software-based or virtual network interface that spans two or more different networks. If you have a wired network and a wireless network and you have a computer with two physical interfaces to both networks, you can use a network bridge to allow computers on both networks to access any network share that you create on that system. The bridge also provides a means for systems on one network to access resources on the other network through the network bridge.

### Note

Do not create a network bridge between a Windows Internet connection and your wired network, because it allows unsecured access to Internet users to your wired network.

To create a Windows network bridge, follow these steps:

1. Open the Network Connections folder.
2. Hold the Ctrl key and click the network connections (interfaces) that you want to add to the network bridge.
3. Right-click a selected interface and select Bridge Connections; if necessary, supply the administrative credentials required. [Figure 9.2](ch09.html#a_network_bridge_and_its_constituents_sh) shows the Network Connections window in Vista with a network bridge installed.

A network bridge is a virtual network interface and can be manipulated just like any other network interface. You can open its Properties dialog box and add or remove components, including additional network interfaces. To remove an interface from the network bridge or the network bridge itself, you can delete it from the icon's context menu.

![A network bridge and its constituents shown inside Vista's Network Connections dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0902.png)

**Figure 9.2. A network bridge and its constituents shown inside Vista's Network Connections dialog box**

Although bridging and routing are both methods for directing data on a network, routing refers to methods that are performed at the Network layer (Level 3). A router directs network traffic based on logical assigned addresses such as IP addresses, while a bridge uses only the hardware ID (MAC address). Therefore, routers can determine when different networks are in use while a bridge cannot, which makes routers less prone to errors than bridges. As a general rule, you would use bridges to connect network segments and routers when connecting different networks. Bridges are inexpensive devices, more expensive than hubs or repeaters but less expensive than switches (sometimes) or routers (always). Because bridges buffer frames while they are determining their forwarding status, they have less throughput than repeaters, which simply amplify the signal and forward it.

# Routers

A network router is a device that connects two different networks together. Routers separate collision domains, filter and block broadcasts, and determine the optimum path to use to route packets. Because routers operate at the Network layer (Level 3), you may hear routers referred to as Layer 3 switches in just the same way that bridges were referred to as Layer 2 switches. High-performance routers are powerful computers that can perform a considerable amount of data processing.

Routers, as a logical device, have the concept of a multihomed server as their origin. An early router was developed at BBN Technologies (formerly called Bolt, Beranek and Newman) and was eventually replaced by DEC PDP-11 systems configured to route IP traffic. Sun Microsystems popularized the low-cost SPARC servers as routers; when the Internet became commercialized in the1980s, many ISPs bought Sun servers for that purpose. A startup called Cisco, which turned routers into an appliance, is the dominant switch vendor today.

Routing is included in many server network operating systems, including UNIX, Linux, and Windows servers. The lower cost of Linux makes it very popular as a router. Cisco routers have the Internetwork Operating System (IOS) that was designed specifically for switching and routing, and uses a Command Line Interface. Many of the developments that you read about in this chapter were inspired by Cisco's work. Other vendors that have router operating systems include Juniper Networks (JUNOS) and Extreme Networks (XOS).

### Tip

Use a bridge instead of router if your primary aim is to segment traffic but you don't need routing capabilities or the protocol translation functions of a router.

Routing on small networks is not a processor-intensive application, and many people turn their obsolete personal computers into network routers. Among the software packages that you can use to create PC routers are:

- **Quagga (**`www.quagga.net`**)**. Open source OSPF, RIP, BPG, and Intermediate System to Intermediate System (IS-IS) routers for UNIX, Linux, and Solaris systems based on the Zebra project.
- **SmoothWall (**`www.smoothwall.org`**)**. An open source Linux distribution that provides an easy-to-use graphical user interface (GUI).
- **Untangle (**`www.untangle.com`**)**. An open source gateway application that creates a border router on which various anti-spyware, anti-virus software, filters, blockers, and a firewall can be installed.
- **XORP (**`www.xorp.org`**)**. The Extensible Open Router Platform is an open source router that includes RIP, OSPF, IGMP, BGP, and other routing protocols. Versions of XORP run on Linux, Mac OS X (9.2 and higher), and Windows Server 2003.

You may encounter the composite term *brouter*, which is short for bridge router. A brouter is a device that can function as a bridge or a router. When routable packets such as TCP/IP arrive, brouters perform the function of a router and route them from the source network to the destination network. Any packet with an unroutable protocol, such as NetBEUI, is simply forwarded like a bridge would do.

Routers are characterized by two different functional systems: their control planes and their forwarding planes, which select ports and send data to the correct outgoing interface. The methods used to determine how this is done are based on intelligent algorithms that optimize network performance. Depending on the protocol or protocols that the router supports, different topologies are created. These different aspects of routers are discussed in the sections that follow.

## Control plane

Routers are described as having two operating planes: *the control plane*, which determines which port to use to send packets onto their destination, and *the forwarding plane*, which sends a received packet from the incoming to the outgoing interface. The control plane participates with other network devices to construct the routing table used to route traffic; it is also responsible for filtering and blocking behaviors on the router, as well as any Quality of Service (QoS) protocols that the vendor has included. Filtering behavior is based on the destination endpoint.

The control plane stores the routing table, which primarily represents a set of addresses used for unicast communication with other network endpoints. It is possible to hardwire static routes manually in routers, or place rules on the use of different static routes. The latter is sometimes referred to as a floating static route. Some of the entries in the routing table may be for logical groups of systems, which are used for multicast operations. Most routers rely on the routing table or Routing Information Base (RIB) for their routing logic, but some routers also maintain a Forwarding Information Base (FIB) that is placed into fast memory by the control plane for the use of the forwarding plane.

Most networks choose to place the router into a dynamic mode in which the router participates with other routes or switches in determining the network logic that finds the preferred routes through a network. In most routing protocols, the router is assigned a routing priority, which is a major factor in determining what role a router can play, as well as what routes that router participates in.

Routers use physical connections to define routes through a network, but the interface used may also be a logical network interface. Routers have the ability to bind two or more logical interfaces to a physical interface, provided that they support virtual LANs (VLANs). Support for VLANs is based on the IEEE 802.1q standard. Some routers also support tunneling protocols, including the Generic Routing Encapsulation (GRE) and Multi Protocol Label Switching (MPLS) protocols. Tunneling is described in more detail in [Chapter 29](ch29.html).

## Forwarding plane

The forwarding (or data) plane of a router is the part of the router that examines packets at the inbound interface and transports those packets to the correct outbound interface. Routers often come with multiple forwarding planes connected with a crossbar architecture so that they can forward traffic in parallel. Forwarding planes can come as add-in cards with multiple ASICs for processing; the router itself provides a backplane or chassis into which the cards are placed. The physical structure of many routers is similar to the way blade servers are packaged. One method designed by the IETF's Benchmarking Working Group (BMWG; RFC 2544) to measure performance in routers uses half of the router ports to send packets and the other half to receive them.

This subsystem consults a lookup table that matches the network ID or MAC address to a route stored in the table. As mentioned in the previous section, the forwarding system sometimes uses a Forwarding Information Base stored in memory instead of the Routing Information Base as its lookup to speed up operations. These data stores are searched using algorithms developed for the IP address space, including binary tree, radix tree, Patricia tree, four-way tree, and a variety of proprietary algorithms that have been developed by the router vendor for their specific hardware.

Routers contain rules on what packets to pass and what packets to filter. Filtered packets are dropped (discarded), and no ICMP (Internet Control Message Protocol) messages are sent back to the source. This is done to make the router opaque to hackers. Should the source or destination address be missing in the router's cache or the router table and the packet not conform to a filter, the router sends an ICMP "destination unreachable" packet back to the source.

Because a router bridges different networks at the Network layer (Level 3), packets that use the same Network protocol can be passed directly through the router without processing, something that is referred to as the router's fast path. However, if the network protocols (IP versus IPX, for example) don't match, then the router has to process the packet to conform to the required protocol. Packets that require additional processing are on the router's slow path.

Routers also perform other functions. They serve as security devices by encrypting packets using the protocols that their technology supports. The part of the router that performs this processing is sometimes referred to as the service plane. To perform these functions, routers operate at the Data Link layer (Level 2) for decoding the packet header, processing and extracting the data contained in the packet, and, if necessary, reading other fields in the packet.

Routers also can enforce QoS requirements, segmenting packets if necessary. When the buffer is full, the router is unable to process additional packets and is forced to drop packets. The methodology used to determine which packets to drop varies by router, but three different techniques are commonly used:

- **Tail Drop algorithm**. This queue-management algorithm measures the cache contents, and when it exceeds a certain maximum level drops all incoming packets until the cache becomes available. Tail Drop (or Drop Tail) does not differentiate between types of packets, source, or any other factor in deciding which packets to drop.When the sending system detects that their packets are being dropped by an absence of ACK messages, the sending system goes into slow state until a steady stream of ACK messages are received. The problem with Tail Drop is that when systems begin to re-send packets, they do so all at once, creating a data flood.
- **Random Early Detection (RED)**. This is an algorithm that monitors the average queue size and drops packets based on a statistical probability function. RED's statistical behavior means that a source sending a lot of data has a high probability of having its packets dropped, while one sending a few packets will tend to get through. This mechanism avoids the problem of flooding or global synchronization that the Tail Drop method suffers from.
- **Weighted RED and Adaptive or Active RED**. Weighted RED uses the RED method but applies different priorities to packets. Active or Adaptive RED varies the statistical probability function, based on the condition of the queue.

## Routing topologies

Routing is the method used to select the path that data is sent over a network. All networks require routing because it is impractical to have dedicated physical circuits for every possible path that data can travel. In a network where traffic flows from a source to a destination through intermediate devices, there can be more than one possible path that can be used. The intelligence brought to bear in selecting these paths plays a major role in the performance of a network.

There are four different broadcast methods used by routing topologies:

- **Unicast**. A message is sent from one node to another node.
- **Broadcast**. A message is sent from one node to all other nodes.
- **Multicast**. A message is sent from one node to several nodes, typically nodes that have requested the message be sent.
- **Anycast**. A message is sent from one node to a group of nodes, and any member of that group can accept the message and act on it. Once the anycast is delivered at a node, the communication is complete.

[Figure 9.3](ch09.html#the_four_different_broadcast_topologies) shows the four different broadcast topologies. Each oval is a separate network or subnet.

Routing is essential not only because you can't physically create all of the possible paths but also because you can't just simply throw hardware at the problem. Consider the circumstance where finding that traffic between two endpoints is high, a network installs a backbone of similar capacity, but that is shorter and faster. Switches detect this new connection and recognize that this connection is now the lowest-cost route. All traffic is then sent over the new backbone, saturating it and reducing overall network performance. This is called Braess's paradox: extra network capacity is consumed when traffic always uses the least-cost path, and in some cases, reduces system performance. This is as true with networks as it is with traveling Boston's Route 128 or San Jose's Route 101 at rush hour. It is counterintuitive, but it has been demonstrated that closing busy roads often has the effect of distributing traffic, leading to better efficiency.

Braess's paradox arises out of a game theory developed by John Forbes Nash, the Princeton physicist who won a Nobel prize for his work. Any system of multiple actors, each acting in their own best interest when taking into account the actions of the other actors such that no actor can change their strategy unilaterally to gain improvement, is called the Nash equilibrium. As you can see from the previous paragraph, systems in Nash equilibrium do not always result in the best cumulative outcome. To get the best individual results, groups must deviate from the Nash equilibrium.

This is where routing comes in. To be efficient, routing must be dynamic. In a dynamic system, the network responds to events in order to continue to operate and will make selections for groups of systems that the individual systems themselves wouldn't have the intelligence to make. For example, if a backhoe inadvertently breaks a buried telephone trunk line, an adaptive routing protocol would reroute traffic over a different path. Or if a short, high-speed line becomes available, a dynamic routing scheme would distribute traffic so that congestion is balanced against overall system performance. In individual cases, the path taken would be longer, but overall, the system's efficiency would be optimized.

![The four different broadcast topologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0903.png)

**Figure 9.3. The four different broadcast topologies**

## Optimization methods

On very small networks, you can manually set the preferred paths between endpoints in a simple array called a routing table. The approach isn't practical for networks of any size, and so instead they use routes that either have been computed or are computed on the fly as needed. The PSTN used a system where tables of pre-computed preferred routes are stored, along with a set of backup routes to use when the primary route fails. As the telephone network has developed, it has begun to adopt adaptive routing technologies where the routing tables are generated by the routing protocols, thereby acting automatically to reroute traffic. On the Internet, the routing system is rather different; routing is entirely dynamic.

Routing systems operate either between autonomous systems or within them. An autonomous system (AS) is a collection of systems sharing a unified administration structure. They can be a network, a group of networks, an ISP's network range, or the entire Internet. Routing protocols that connect autonomous systems are called gateway protocols. An interior gateway protocol (IGP) is used to route packets on any collection of connected IP addresses, known also as an AS. IGPs are exemplified by RIP (Routing Information Protocol), Cisco's IGRP (Internet Gateway Routing Protocol), OSPF (Open Shortest Path First protocol), and IS-IS (Intermediate System to Intermediate System protocol). Exterior gateway protocols (EGPs) are used to determine the routing between two or more autonomous systems. The class of EGPs included the original EGP (now obsolete) and BGP (Border Gateway Protocol) and also can include backbone routers in the OSPF system. These different routing and gateway protocols are explained in the sections that follow.

## Distance vector routing

A distance vector (DV) algorithm assigns a cost to use of each network connection based on the number of hops. Messages are routed based on the lowest hop count of the individual connections summed over the route taken. Each node in the network constructs a distance table with its nearest neighbors, which then share that table with their neighbors. DV routing is very common on packet switched networks and forms the basis for both the Routing Information Protocol (RIP v1 and v2) and the proprietary Cisco Interior Gateway Routing Protocol (IGRP). Two other protocols use aspects of the DV methodology: the Border Gateway Protocol (BGP), which is the core protocol for routing on the Internet, and the Exterior Gateway Protocol (EGP), which is an older and now obsolete routing method.

While some protocols, such as the Spanning Tree Protocol (a Layer 2 protocol described later in this chapter), operate in such a manner that they detect network loops and eliminate them, distance vector methodology does not. Routing tables are created based on the path of delivered packets optimized over specific connection segments. A Bellman-Ford algorithm is applied to the distance vector table to optimize the calculated routes, and preferred routes are communicated with neighbors who update their routes based on new information.

### The Bellman-Ford algorithm

The Bellman-Ford algorithm uses a shortest-path calculation over weighted edges. It was developed by Richard Bellman in 1958 and Lester Ford Jr. in 1956, independently of one another. Most protocols that use Bellman-Ford use a distributed version of the protocol. The Distributed Bellman-Ford (DBF) uses three different mechanisms to populate the routing tables at each node:

1. **Start state**. Each router has a table listing the path or vector with the shortest hop count to directly attached networks, with entries in the form (Destination, Distance, Successor). A Successor is the router or node that is one step closer on the path to the destination, and is a nearest neighbor. Destination can be a simple hop count, a weighted cost based on throughput or connection speed, or some other factor.
2. **Send**. Each node sends its path vectors (Destination, Distance) to its immediate neighbors, periodically (a second to a minute) and immediately upon detection of an entry change.
3. **Receive**. On a network, each router calculates the least-cost path to other destinations based on the information it receives from its nearest neighbors. After the update, each router returns to Step 2 and sends its new information on to its nearest neighbors.

In [Figure 9.4](ch09.html#the_bellman-ford_algorithm_apostrophy_s), the Bellman-Ford algorithm is illustrated. In the figure, the top routing table is populated with nearest neighbor information. Because there is no way for router A to know the shortest route to router E, the vector entry is left blank (NA or Not Available). The middle routing table shows the first update going from D to B. Now router B can fill in a vector for the path from router B to router E of 5, although it is still unknown if this is the least-cost path B to E. Until the E-C vector is populated, router B can't know that BDE is indeed the lowest-cost path, at a cost of 5, because BCE has a cost of 8. The bottom routing table shows the router table after nearest neighbor updates, E to C update, and enough rounds of nearest neighbor updates needed to populate the table with lowest-cost vectors (shown in [Figure 9.4](ch09.html#the_bellman-ford_algorithm_apostrophy_s)).

The routing table that is stored at each router is shown in [Figure 9.5](ch09.html#the_routing_table_for_an_individual_rout) and is somewhat different than the least-cost path shown in [Figure 9.4](ch09.html#the_bellman-ford_algorithm_apostrophy_s). As an example, consider router B and its routing table, consisting of vectors with their entries (Destination, Distance, Successor) shown in table form. In this table the row is the destination, the column is the successor, and the distance is the values in the grid cells. Notice that many of the entries are not populated with the least-cost path.

Consider what happens when the B-D link breaks, as is shown in [Figure 9.6](ch09.html#the_impact_of_a_broken_link_on_a_bellman). The break is detected by both routers B and D, and an immediate update is triggered, followed by nearest neighbor updates. Multiple vectors in the table are altered by this update, each of which is shown with its cell's borders made bold.

![The Bellman-Ford algorithm's mechanism for populating a router table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0904.png)

**Figure 9.4. The Bellman-Ford algorithm's mechanism for populating a router table**

![The routing table for an individual router, shown here for router B](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0905.png)

**Figure 9.5. The routing table for an individual router, shown here for router B**

![The impact of a broken link on a Bellman-Ford routing table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0906.png)

**Figure 9.6. The impact of a broken link on a Bellman-Ford routing table**

### Count-to-infinity

In a distance vector system, any change in the dynamics, such as a link or device failure, is detected during regular updates, and the entries for that link or device are either modified or deleted. The change then ripples through the adjoining nodes' tables. Because only neighbors update, the progression is slower than updating the entire network at once and requires less bandwidth and a smaller amount of processing. It also means that until the downstream nodes learn of the change, they are still communicating the original configuration's validity. This problem is often referred to as the count-to-infinity problem.

Consider a sample network path, A-F, with each segment or hop costing one unit for packets to traverse. This is illustrated in [Figure 9.7](ch09.html#the_count-to-infinity_problem). The link A-B fails, and B, being the nearest neighbor, detects the problem. At the first update, B gets an update from C and, realizing that C has a route to A with a hop count of 2, B updates, or reactualizes, its routing entry to add the cost of the B-C route to C's cost and puts the value of 3 into its routing table entry, believing that the lowest-cost route to A now goes through C. C still believes that B is the lowest-cost path to A, and so when it looks at B's entry (now at 3), it readjusts its value to 4, and all of the downstream neighbors adjust their values as well. Update 3 performs the same legerdemain that Update 1 does, B looking at C and adding C's value to the hop count of B-C. The process continues on counting to infinity and eventually would immobilize the network. Count-to-infinity is circumvented by the use of a technique in Bellman-Ford called *relaxation*, where a test is performed periodically to determine if a shorter path exists than the one in the routing table entry.

### Routing Information Protocol

The earliest and best-known protocol using the DV routing algorithm is the Routing Information Protocol (RIP) that is used as an interior gateway protocol on both LANs and WANs. The original version was defined by IEEE RFC 1058 in 1988; version 2 was defined in RFC2453, and RIP became the original routing protocol used on the Internet. RIP uses a hop count as its cost metric. The maximum number of hosts is limited to 15, and the Time-to-Live for any one path is 180 seconds. RIP slightly randomizes updates so that the system isn't overloaded when too many routers update at once.

![The count-to-infinity problem](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0907.png)

**Figure 9.7. The count-to-infinity problem**

RIP was widely used, but is considered to be less effective than other link state routing protocols such as the OSPF and the OSI protocol IS-IS. A version of RIP exists for IPv6, called RIPng, which has several methods in place to ensure that obsolete or incomplete information doesn't propagate in the system. One rule, called *the split horizon*, prevents any router from advertising a route back to the router that it learned about the route from.

Split horizon effectively eliminates the count-to-infinity problem and suppresses the formation of network loops. In a network branch, with a message starting at router 1 and going through routers 2, 3, and 4 to get to router 5, a router with a higher number will never advertise the route to a router with a lower number. Should link 2-3 break, router 2 is prohibited from returning the packet back to router 1, which would form a loop.

A variation of the split horizon rule, called *split horizon with poison reverse*, actually marks routes back as unreachable, which is really only useful on a network where redundant pathways exist. The vector entries for the reverse routes are removed from the routing tables, whereas for split horizon, backwards routes are simply timed out. Poison reverse significantly increases the size of routing information exchanges, which is a disadvantage over slow network links such as WANs. In addition to RIP, IGRP, Enhanced Interior Gateway Routing Protocol (EIGRP), and VPLS (Virtual Private LAN Service), all use some form of split horizon.

### Destination-Sequenced Distance Vector Routing

The Destination-Sequenced Distance Vector Routing (DSDV) protocol is a variation of the DV system for routing on ad hoc Wi-Fi or mobile networks. DSDV adds an additional parameter to the routing table, a sequence number that is assigned to a given link and generated by the destination of the link and communicated back to the emitter. The entire routing table is transferred occasionally, while updates to the table trigger incremental vector transfers. The sequence number is usually an even number, or if a link is not detected from an update, then an odd number is used. An update for an existing link with a different lowest-cost route overwrites the route but not the sequence number. Every so often, routes that have not been used are purged from the table. DSDV was developed some time ago but never achieved commercial success. The Ad hoc On-Demand Distance Vector (AODV) Routing protocol that was developed for MANETS (Mobile Ad hoc Networks) is based on DSDV. AODV may find application in cell phone networks.

## Link state routing

The concept of link state routing is that each router informs the network about its neighbors. A link state routing system creates a topological map (graph) of the network at each router, centered at that router. These maps are used to calculate the shortest path, usually by applying Dijkstra's algorithm to calculate the shortest path over several links. While distance vector protocols work by sharing routing tables, a link state protocol only transfers information about the best next hops between neighbors. Whenever a link state changes (up to/ down from), an update is triggered and the information is sent to all nearest neighbors.

Link state routing works by using the following procedure:

1. Broadcasts over each port of any new router on the network establishe who its nearest neighbors are through their responses and record their information in the routing table.
2. Each route is given a sequence number by the link state routing algorithm.
3. A link state advertisement (LSA) is broadcast automatically every so often to neighbors, containing the information about nearest neighbors stored in the routing table.
4. If the sequence number of the announcement from a node hasn't been recorded, the new information is recorded in the routing table by the link state routing algorithm; if the information has a higher sequence number for an existing link, the new information, including the higher sequence number, overwrites the previous information.Steps 3 and 4 are repeated over the entire routing domain. Updates are sent by unicast to nearest neighbors, and occasionally link state exchange messages called HELLO packets are sent to ensure system integrity.
5. The link state algorithm then examines all stored valid links and creates a map of the network centered on the router the algorithm runs on. Valid links are those for which both endpoints have reported each as a nearest neighbor.
6. The accessibility of links is tested again when the link state algorithm repeats Step 1 and starts the sequence again.
7. A Dijkstra algorithm is then run on the router over the link information in the routing table to determine the shortest route between endpoints and records the information in the routing table.

The link state routing table is a hierarchical tree consisting of a set of least-cost paths connecting all of the network nodes. For any given destination, the next hop selected is the one that is the first node from the root of the hierarchy traversing the path down to the desired node. That is, if the source node is on the same branch as the destination, the route is direct. If they are on different branches, the best route travels through the node and then down the branch containing the destination node.

The most common link state routing protocols are:

- Open Shortest Path First (OSPF)
- Intermediate System to Intermediate System (IS-IS)
- Novell NetWare Link Services Protocol (NLSP)
- Apple Routing Table Maintenance Protocol (RTMP)
- Cisco Internet Gateway Routing Protocol (IGRP)

Depending upon the protocol, the least-cost route or shortest path can be based on line speed, available bandwidth, the actual cost in dollars to use a line, or other priorities that you can define. Link state routing methods are preferred for large networks because they respond faster to changes than distance vector methods do, and they are the dominant routing protocol on the Internet and with ISPs.

### Dijkstra's algorithm

Dijkstra's algorithm is a pathfinder mechanism that is easier to visualize than it is to describe. The process builds two tables: a link cost table and a routing table. Link cost is a complete list, while the routing table is the result of an iterative process that provides the shortest path from A to any other node. Dijkstra's algorithm forms the basis for a number of protocols, referred to as Shortest Path First (SPF).

The description that follows refers to [Figure 9.8](ch09.html#dijkstra_apostrophy_s_algorithm_example) and shows how the topological map for node A is built. The process starts by initializing all routes to an unknown state, marked as infinity in the drawing. In Step 1, node A contacts its nearest neighbors to get their link costs. All nearest neighbors have their link cost tables updated with the information provided by A, and because A-C, A-E, and A-F are all the lowest-cost paths, they are marked in the routing table as such. In Step 2, node F discovers its nearest neighbors and updates its link cost table. F notices that the link cost for A-E is longer than the link cost for A-F-E, and therefore takes the route A-E out of the routing hierarchy. In [Figure 9.8](ch09.html#dijkstra_apostrophy_s_algorithm_example), links found in the routing table are in bold, and any link that is not in the routing table is shown as a thin line. F's results also indicate that the link cost for C-F is greater than the link cost for C-A-F, and so C-F is removed from A's routing table as well. Once all F's link information is discovered, all of the nodes have their link cost tables updated.

![Dijkstra's algorithm example](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0908.png)

**Figure 9.8. Dijkstra's algorithm example**

In Step 3, node C begins its discovery process. C finds that A-C is the lowest-cost route. C-D-F-A is longer than C-A. The link C-D therefore remains unused in A's routing table. Similarly, the route C-F-A costs more than the route C-A, and so C-F also remains left out of A's routing table. C's discovery process adds no additional routing to A's table but does extend the entries in the link cost tables.

Step 4 shows the E node discovery results. E results indicate that the path D-E-F-A is shorter than D-F-A, and so the path D-F is removed from A's routing table. The additional information about D-E's link cost is then added to all nodes' link cost tables. Similarly, Step 5 discovers the link cost of B-D but is similarly unable to add any better low-costs paths to A's topological map. At this point, all of the link costs in the graph are known and the routing is complete. The process is finalized by D's discovery process in Step 6, which confirms the information you already have.

The important thing to realize about Dijkstra's algorithm is that it is always expanding out from its starting point, adding more nodes as time goes on. The iterative process involved ensures that eventually the routing table is populated with the shortest least-costs paths, even if other paths were used at an earlier time.

Issues arise with Dijkstra's algorithm when a link fails or a node becomes unavailable and the topological map varies at different nodes. In this case, network loops can form. This is the problem that the HELLO packets are designed to solve. Also, variations in the implementation of link state algorithms add additional concepts such as areas and other wrinkles that make the calculations more complex, but less susceptible to the network loop problem.

### Open Shortest Path First

The Open Shortest Path First (OSPF) protocol is the most widely used example of a link state routing protocol. It is in wide use as an interior gateway protocol on the Internet and many other networks. The latest version of this public protocol was version 3, as specified in RFC 5340 released in 2008, and includes support for IPv6.

The Open Shortest Path First algorithm operates similarly to Dijkstra's algorithm but adds a system of designated (primary) and backup routers. Routers are selected for these roles based on their priority number; routers with a priority of 0 cannot be designated or backup routers. The designated router for an area is responsible for sending Link State Advertisements (LSAs) to all other area nodes. OSPF routing packets on an OSPF routed network have a nine-field header, illustrated in [Figure 9.9](ch09.html#the_structure_of_an_ospf_packet). OSPF packet types include HELLO, database description, link state request, link state update, or link state acknowledgment.

OSPF is used on autonomous systems (AS). Autonomous systems are one or more networks under a common administrative structure. OSPF functions not only as the interior gateway routing protocol for the AS, but it can also send and receive routes from other autonomous systems. Each network in the AS is an area within a hierarchy defined within the AS, each area being a collection of contiguous hosts. In OSPF, a routing domain is an alternative description for all systems in an AS that share the same topological map. OSPF partitions areas into separate topologies so that each area is kept unaware of another area's routing traffic. This system is meant to lower the amount of overall network traffic and speed up the discovery process of shortest routes for an individual area.

![The structure of an OSPF packet](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0909.png)

**Figure 9.9. The structure of an OSPF packet**

Collections of areas are connected by OSPF border routers in an OSPF backbone. The backbone itself is organized as an OSPF area, and routing information for that area is also separate from the areas the backbone connects. It is possible to organize an OSPF backbone so that the backbone is composed of two or more unconnected groups. The backbone is made contiguous by defining a virtual link through routers in a non-backbone area to serve as the connection between backbone groups. The backbone of an OSPF system composed of border routers communicates with other exterior gateway protocols (EGPs) such as the Border Gateway Protocol (BGP) or the Exterior Gateway Protocol (EGP). [Figure 9.10](ch09.html#an_ospf_routing_network_with_several_are) shows an OSPF network with several areas, a backbone, and a virtual link.

### Intermediate System to Intermediate System Routing

Intermediate System to Intermediate System Routing (IS-IS) is the second-most widely used link state protocol used on packet switched networks. IS-IS tends to be employed on large ISP and enterprise-class networks as an interior gateway protocol for a network or autonomous system where it has a dominant position, and connects through exterior gateway protocols to other autonomous systems.

IS-IS was developed at the Digital Equipment Corporation as part of DECnet in the late 1980s and was published as the ISO standard, ISO/IEC 10589.2002. Because IS-IS isn't a public standard, it isn't used on the Internet, although the IETF republished 10589.2002 as RFC 1142 in 1990. The original version of IS-IS was extended to support IP routing over TCP/IP networks and is referred to as Integrated IS-IS in older literature.

IS-IS competes with OSPF and is also based on Dijkstra's pathfinder algorithm. Although they have many overlapping features, IS-IS is considered to be somewhat more stable than OSPF, while OSPF has better performance optimization features. The extra features in OSPF add additional messaging overhead and probably contribute to the fact that IS-IS scales better than OSPF.

![An OSPF routing network with several areas and a backbone](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0910.png)

**Figure 9.10. An OSPF routing network with several areas and a backbone**

IS-IS defines three different routing area types: Level 1 (intra), Level 2 (inter), and Level 1-2 (intra/inter). Level 1 and 2 routers can only exchange information with routers of the same level, while both can exchange information between Level 1-2 routers. Unlike OSPF, which uses a backbone (Area 0) for inter-area exchange and allows for an area border router to be a union point of two areas and part of both, IS-IS does not use a backbone and areas in the network never overlap.

## Path vector routing

Path vector routing is the last of the three main approaches to building routing tables in networks, the previously discussed distance vector and link state routing being the other two. Path vector routing is a derivative of the distance vector routing methodology. In the path vector system, a node gets distance vectors for a destination from its neighbor node, along with the entire path needed to reach that node. Knowing the path allows the algorithm to more easily detect and react to network loops than the distance vector method. In this system, a node stores two tables: a path table for the current path to any node and a routing table with the identity of the next hop for those routes.

### A path vector example

Let's consider a simple example of the path vector approach, as shown in [Figure 9.11](ch09.html#an_illustration_of_the_path_vector_routi). Vectors take the form:

|  |
| --- |
| (Destination, Cost, Path Node Count, Path Node List \| ...) |

where each | character separates one vector from another.

A sends a HELLO packet in Step 1 and learns about its neighbors, as does C. C then sends its vectors to node A, and in Step 3, A rebuilds its routing table based on the new information. C's vectors allow A to define a route to D but do not alter any of the other known routes, as shown in the lower-left table in [Figure 9.11](ch09.html#an_illustration_of_the_path_vector_routi). Condensing several steps into one, all nodes learn about their neighbors using a HELLO packet in Step 4. Now when E sends its vectors to A, as shown in Step 5, A is able to build a routing table to all nodes in the figure. The new information from E adds a route to B (AFB) and changes the routes to C (to AFB) and to D (to AED). In the final Step 6 A is able to communicate its routing table shown in the lower right with all of the other nodes.

In the path vector routing system, one or more nodes in a network, called *speaker nodes*, store the routing table for other connected nodes, and distances are calculated by the speaker nodes. Speaker nodes then advertise the paths available to reach them to other speaker nodes. Path vectors try to minimize the number of domains traversed by messages, which makes this method suitable for routing across autonomous systems. The widely used Border Gateway Protocol is based on the path vector routing methodology.

Of the three methods distance vector, path vector, and link state, only the path vector protocols are practical for inter-domain routing. In distance vector routing, every additional hop a message must traverse greatly raises the possibility that the path chosen may be out of date and dysfunctional. Link state routing requires that the network tolerate heavy broadcast traffic, and that significant computing resources be used to assemble the network maps at each node.

### The Border Gateway Protocol

The Border Gateway Protocol (BGP) is a highly scalable exterior gateway routing protocol for use between autonomous systems based on the path vector protocol described in the previous section. BGP is the protocol used to route traffic on the Internet, replacing the Exterior Gateway Protocol (EGP). EGP was the original Internet routing protocol developed by BBN Technologies in the early 1980s. The current version of BGP is version 4, which was specified by RFC 4271, published in 2006.

Unless you are an ISP or work in a very large network, chances are that you won't get hands-on experience working with BGP. However, because BGP powers the Internet, it is worth understanding some of the details of this important protocol. BGP is the only routing protocol that operates natively using TCP as its transport protocol, exchanging packets over port 179. BGP deployments are divided into two different types: the Exterior Border Gateway Protocol (EBGP) and the Interior Border Gateway Protocol (IBGP). A BGP router that is inside an autonomous system (AS) is an IBGP router, while a router that is between autonomous systems is an EBGP router. Any router inside an AS that communicates with another AS is called a border or edge router. By contrast a core router is one that operates on the Internet backbone.

![An illustration of the path vector routing mechanism](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0911.png)

**Figure 9.11. An illustration of the path vector routing mechanism**

Top ISP routers are currently storing BGP routing tables of around 150,000 routes, and so if you have a fast connection such as a T1 line to AT&T, Comcast, or Sprint, you would have to download 150,000 routes from each service you are connected to. BGP partitions routes by attributes or route parameters so that routing may be more efficiently managed. Attributes that are stored include:

- **Route cost or weight** (as Cisco refers to cost)
- **Next hop**. The first node on the path to the advertising router
- **Origin**. Where the routing information came from, EBGP or IBGP
- **AS_path**. The identity of the AS from which the route advertisement came
- **Local exit preference**. The preferred exit point from the AS
- **Multi-exit discriminator** (a Cisco attribute)
- **Community designation**. This can be no-export, no-advertise, or Internet (advertise to all)

As you move down the Internet hierarchy, the Classless Inter-Domain Routing (CIDR) protocol is used to further partition the routing tables so that related address blocks can be routed as a single unit to other BGP routers. The CIDR system, described in more detail in [Chapter 18](ch18.html), replaces the older notion of network classes.

## Network loops

One way to bring down a network is to create a network loop. You can do this by plugging an Ethernet cable into two ports on the same switch or router, or by inadvertently creating a loop with multiple switches and routers — hubs don't suffer this problem. Although the circuit has been shown with three routers, you could use any combination of computers, switches, or routers as endpoints in the circuit.

Suppose you have the circular path shown in [Figure 9.12](ch09.html#routing_failures_comma_infinite_loops_co). In the complete circular circuit shown in the upper-left diagram, Router_1 sends packets to Router_3 with Router_2 as the intermediary. If the connection between Router_2 and Router_3 breaks, Router_2 will return traffic meant to flow over that broken connection. Router_1 does not know about the break, and when Router_1 sends packets to Router_3 through Router_2, the packets are returned. Router_1, being ignorant of the broken connection, but still believing that the path Router_1-Router_2-Router_3 is the lowest-cost path for transmission, resends the traffic back to Router_2. Traffic between Router_1 and Router_2 bounces back and forth in an infinite loop, and the connection is quickly saturated, as shown in the upper-right scenario labeled as an infinite loop in [Figure 9.12](ch09.html#routing_failures_comma_infinite_loops_co). This is the problem that routing algorithms are created to solve.

Let's take this one step further. In the circular path described, both the connections between Router_1-Router_3 and between Router_2-Router_3 fail concurrently as shown in the diagram on the lower left labeled infinite loops. Having two wires fail at the same time is a very uncommon event, but the same result is achieved when Router_3 fails, which is a common event. Now, traffic that would flow from Router_1-Router_2-Router_3 ends at Router_2, where the message is returned. If Router_2 believes that the lowest-cost path to communicate with Router_3 is Router_2-Router_1-Router_3, then traffic along that route ends at Router_1, where it is returned. This routing loop would continue until a routing protocol determines that Router_3 is unreachable. This is the situation depicted in the lower-left example in [Figure 9.12](ch09.html#routing_failures_comma_infinite_loops_co).

![Routing failures, infinite loops, and failure cascades](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0912.png)

**Figure 9.12. Routing failures, infinite loops, and failure cascades**

It is at this point where you cross over into the Twilight Zone of computer networking, a failure cascade. At the bottom-right example in [Figure 9.12](ch09.html#routing_failures_comma_infinite_loops_co), an infinite loop occurs at the connection labeled 1, which then saturates. The traffic on adjacent connections labeled 2 and 3 begins to pile up, and they develop infinite loops of their own. As connections fail, the effects spread outwards. A cascade of failing links ripples through the network, expanding out through connections 4, 5, and 6... and beyond. The entire network is down, and the only way to diagnose the problem is to divide the network up into segments, locate the error, and continue segmenting until you isolate the problem to a single device or connection. This is, in essence, what routing protocols do in software.

## The Spanning Tree Protocol

The Spanning Tree Protocol (STP), as specified by the IEEE 802.1D standard, is an adaptive routing technology that solves the problem of network loops through adaptive and dynamic routing. STP is a central technology used on switched networks and establishes routes by creating virtual circuits, eliminating any network loops that it can detect. Connections are made at bridge nodes. Switches are commonly used for the connection points, and they are configured to serve the role of a bridge. Routers can also be set into a bridging mode to function in this capacity. However, the extra intelligence added to routers can be applied to different systems of routing.

The STP algorithm (DEC STP) was invented by Radia Perlman in 1985, while at Digital Equipment Corporation (now at Sun Microsystems), and predates the development of the World Wide Web. STP operates at the Network layer (Level 2) of the OSI model, above the Physical layer and inside devices such as switches and routers.

In a hierarchical network, the root node is connected to a certain number of Level 1 nodes, and the network continues to fan out. A hierarchical topology is a tree, albeit an upside-down tree where branches are linear and where the failure of any node or connection to a node in a branch renders the nodes at lower levels in the hierarchy inaccessible. A purely hierarchical topology also means that if a node in one branch wants to communicate with a node in another branch, it would have to traverse a path up the tree to the root node and back down to the target node. For these two reasons, only very small networks can be structured in a pure hierarchy.

The solution to these problems is to build cross-links between different branches. Cross-links provide shorter paths and thus better performance, and they provide a certain measure of redundancy because there are now multiple paths through the network for most connections you might want to make. Cross-links also provide a mechanism to create network loops.

In graph theory, a spanning tree is created by using an algorithm to compute a set of paths through a system of connected nodes such that every node is on at least one branch of the tree, but that no loops are defined. Nodes serve the function of a topological bridge, and therefore are often called bridges. [Figure 9.13](ch09.html#a_spanning_tree) shows a spanning tree. The solid lines represent branches of the spanning tree, while the dashed lines represent routes left out of the spanning tree.

There are many different ways that you can compute a spanning tree. In one scheme, each edge is given a weight (a weighted graph) and the spanning tree computes the paths through the system that has the lowest weights, thus providing what is called a minimum spanning tree, or alternatively, a minimum-weight spanning tree. In multi-domain systems, a union of minimum spanning trees is called a minimum spanning forest.

Other optimizations are possible, such as the minimum spanning tree with the most edges, the minimum diameter, fewest leaves, or minimum dilation. An edge is the path between two nodes calculated by the spanning tree algorithm. Leaves are each of the branches of the tree. The diameter is the number of switches traversed to link two switches in a bridged network together. Dilation represents the difference between the shortest path between two nodes in the tree and the path that the spanning tree algorithm calculates.

![A spanning tree](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0913.png)

**Figure 9.13. A spanning tree**

### Node/bridge hierarchy

In a network system, the goal is to define a spanning tree such that there are no loops, but that enough redundancy exists in the system to provide access even when a node or connection fails. Instead of using weighted edges, the notion of a least-cost path is used. To compute the least-cost path, the system defines two parameters:

- Node Priority
- Node Identifier

The cost, or weight, of a node is then computed using a combination of the two parameters. In the Spanning Tree Protocol, the node priority is considered first; the node with the lowest priority number is deemed to be the highest priority and takes precedence. Nodes are then compared using their MAC addresses, and the MAC address with the lowest value takes precedence over a node of the same priority. To set a node as the root (root bridge), the priority should be set below 10, while most devices using STP come with their priority set high. For Cisco switches/routers, their priority out of the box is set to 32768.

The STP algorithm computes a path through the system such that messages that travel from any endpoint to the root bridge do so over the least-cost path. The cost of a path is the total of the costs of each of the segments that the path traverses. Because each bridge point in the system has a configurable priority, the STP can change the least-cost path based on conditions. In computing a least-cost path, the following two rules are used:

- Determine the least-cost path from each bridge node.
- Determine the least-cost path for each network segment.

In a switch/router, the port connected to the least-cost path to the root is the root port; the port connected to the least-cost path to a network segment is called the designated port of that segment. For the purposes of this discussion, you can take the definition of a network segment to be a collection of nodes that are connected by the same Physical Layer system that share the same security model. Thus two subnets sharing the same LAN would be two segments, as would two different workgroups/domains.

Once the STP algorithm calculates the root and designated ports, any other active port then becomes a blocked port. It is often the case that two or more paths to the root from a bridge have the same lowest cost. In that case, the path through the bridge node with the lowest bridge ID becomes the root port. When there exist two or more bridges on the same network segment that have the least-cost path to the root, the designated port becomes the one on the bridge that connects to the bridge with the lowest bridge ID.

[Figure 9.14](ch09.html#a_network_system_to_which_the_spanning_t) shows a network system to which the Spanning Tree Protocol has been applied. To simplify the analysis, each network segment is assumed to have the same unit cost. The following analysis leads to the STP diagram that you see in [Figure 9.14](ch09.html#a_network_system_to_which_the_spanning_t):

1. The bridge node with priority 8 has the highest priority (lowest number) and becomes the root bridge. The root node is not necessarily the highest-capacity or most powerful device; typically, it is one that is most centrally located. Generally, the root node chosen is one that is the least modified or disturbed; for this reason, switches on network backbones are often chosen as a root node. Note that the root bridge is the only bridge in the network that does not have a root port.
2. Two paths lead to bridge nodes with priorities 10 and 12. Because 10 has the highest priority, it connects to the next-highest bridge node, which is 22.
3. Of the two nodes that are unconnected with values of 12 and 22, 12 now has precedence. The highest-priority node that 12 can physically connect to without creating a loop is 45, and that connection is made.
4. The two unconnected nodes compared now are 22 and 45. Bridge node 22 is connected to 50, the next-highest priority node.
5. Because the two bridge nodes compared at this point are 45 and 50, 45 takes precedence. The highest-priority bridge node that it can physically connect to is 125.
6. The three remaining bridge points are 77, 96, and 200, and they are connected in sequence. They become endpoints of each of the branches of the spanning tree.

![A network system to which the Spanning Tree Protocol has been applied](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0914.png)

**Figure 9.14. A network system to which the Spanning Tree Protocol has been applied**

It is still possible that the algorithm may not be able to break a tie to determine which of two or more bridges rank higher in the STP hierarchy. The situation arises when two bridges are connected to one another by two or more links. The selection is then made based on the port priority, and this port is assigned to be either a root or designated port.

### Network segment costs

[Figure 9.14](ch09.html#a_network_system_to_which_the_spanning_t) makes the assumption that each network segment has the same cost of traversal, which is generally not the case. As was stated in the previous section, the network segment cost is one parameter used to determine the least-cost path. Some network connections are fast, and some are slow. Even in relatively simple networks where bridge points connect to Fast Ethernet, there may be bridge points that connect to wireless devices. In order to optimize the Spanning Tree Protocol, the cost of the network segment is calculated based on the IEEE 802.1D standard from 1998. This standard was amended in 2001 by 802.1t to allow for more granular calculations. [Table 9.1](ch09.html#stp_network_segment_costs) shows the standard segment costs.

**Table 9.1. STP Network Segment Costs**

| Segment Throughput | Segment Cost 802.1t | Segment Cost 802.1D |
| --- | --- | --- |
| 10 Gbits/s | 2,000 | 2 |
| 2 Gbits/s | 10,000 | 3 |
| 1 Gbits/s | 20,000 | 4 |
| 100 Mbits/s | 200,000 | 19 |
| 16 Mbits/s | 1,250,000 | 62 |
| 10 Mbits/s | 2,000,000 | 100 |
| 4 Mbits/s | 5,000,000 | 250 |

### Dynamic optimization

In the example presented, all of the bridge nodes' priorities and network segments were assigned prior to applying the STP. The addition of a network discovery method greatly improves the value of the STP and allows it to adapt to changing network conditions. One method used for discovery is called the Bridge Protocol, and it works by multicasting special frames called Bridge Protocol Data Units (BPDUs) that contain information about current path segment costs and available bridge node IDs. With this updated information, the root path on the network can be adjusted. [Figure 9.15](ch09.html#a_bpdu_frame) shows the format used for a BPDU frame. The different fields in the BPDU contain information about the bridge ID, priority of the bridge, and the MAC address used by the switch. Other fields set the priority of the path and other parameters, such as the weight of the path (cost of path).

![A BPDU frame](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0915.png)

**Figure 9.15. A BPDU frame**

Switches and routers, which are the devices that serve as bridge nodes in modern networks, multicast a BPDU frame that includes the MAC address of the port that is the source, and an STP multicast address that, by convention, is set to 01:80:C2:00:00:00. Frames are sent out every few seconds and essentially provide a network heartbeat that STP uses to update its routing tables. The default setting for a standard exchange is every 2 seconds (called the "hello time"), but this is adjustable.

The Bridge Protocol defines three different types of BPDUs:

- Configuration (CBPDU)
- Topology Change Notification (TCN)
- Topology Change Notification Acknowledgement (TCA)

Any time a new device is added to a network port, that port enters a listening state where it detects the different BPDUs and learns about the network configuration. Devices are any endpoint that has a network interface. The default listening state is 15 seconds and is followed by a learning state of an additional 15 seconds. The total of listening and learning is a configurable value known as the forward delay, which is meant to allow the new device time to receive information from the root bridge. With a device such as a computer, server, or printer that cannot operate as a bridge when the port comes out of the learning state, it enters a forwarding state and starts to transmit BPDUs.

When a new bridging node is added to an existing port on a bridge node, a different procedure is followed. Any new switch or router could introduce a network loop into the topology, and therefore the port stays in the blocking mode after the listen/learn cycle completes. The port sends a Topology Change Notification (TCN) frame to the network's root bridge. When the TCN is detected at the root bridge, the change is recorded and a determination is made as to the appropriate port status. The root bridge then acknowledges back to the new port with a TCA frame that determines the port's status. From then on, the new port multicasts BPDUs at the standard regular intervals so that all other bridging nodes update their routing tables appropriately. The root bridge modifies its standard BPDUs to indicate that a change is in progress and then multicasts the change to all other bridge nodes in the system; those root bridges update their routing tables and then acknowledge that the change was made.

At any one time, a bridge node's (switch/router) port may have one of the following five states:

- **Listening**. Incoming BPDUs are received and processed with no frames sent.
- **Learning**. The port adds the addresses of bridge nodes to its routing table but does not forward any frames. A learning port has been incorporated into the active topology.
- **Forwarding**. The port can both send and receive data from the network, and STP continues to process any incoming BPDUs for changes. All ports in a root bridge and any root port are always in forwarding mode, and any designated port on a single LAN segment must also always be in forwarding mode.
- **Blocking**. The port is configured so that it can neither send nor receive data, but it does receive BPDUs and can change states if necessary. Any port in a bridge node that connects to other bridge nodes and isn't either a root port or a designated port must be blocked.
- **Disabled**. Ports can be disabled in software (using SMTP commands, for example), but not using STP.

### Rapid Spanning Tree Protocol

As originally conceived, the Spanning Tree Protocol could take up to a minute to reconfigure when a topology change is signaled. While this worked in 1995, by 1998, STP was required to compete with Data Link Level (Layer 3) protocols such as Open Shortest Path First (OSPF) and the Enhanced Interior Gateway Routing Protocol (EIGRP), which could reconfigure an alternative path through the system much faster than STP. For that reason, the IEEE defined what is called the Rapid Spanning Tree Protocol (RSTP) in the 802.1w standard released in 1998. In 2004, the IEEE bundled together the 802.1D, 802.1t-2001, and the 802.1w standards into a single 802.1D-2004 standard that includes them all. Many of the changes added to RSTP were part of Cisco's implementation of STP for switched Ethernet networks.

RSTP is based on STP, but makes some significant changes to the original protocol that allow a bridge node to reconfigure on the order of less than a single hello time (2 seconds) when a root node failure occurs.

### Note

The use of more than one type of STP can lead to unpredictable and undesired results.

In RSTP, blocked ports are separated into two additional states: alternative ports and backup ports. An alternative port is one that is receiving BPDUs from another bridge node of higher priority and is port blocked. A backup port is a port that is receiving BPDUs from the same bridge and is port blocked. The definition allows for a more rapid assignment of an alternative path to the root bridge when the root port fails. The backup port provides a redundant connection to the same network segment, but does not provide a connection to the root bridge. In other respects, the same criteria are used to calculate the topology in RSTP that is used for STP. [Figure 9.16](ch09.html#examples_of_an_alternative_and_a_backup) illustrates an example of alternative and backup ports.

![Examples of an alternative and a backup port](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0916.png)

**Figure 9.16. Examples of an alternative and a backup port**

The BPDU frame for RSTP was changed to allow for a faster aging of information, with BPDUs required as a keep-alive or heartbeat between bridge nodes. When three hello cycles pass without a BPDU, a failure is registered and the bridge node sets a flag in the BPDU frames it sends that indicates the failure and asks a lower-priority bridge to accept that node as its root bridge. A bridge receiving the proposal that has no other path to the root bridge and recognizes the higher-priority bridge will then reset its root port to the one connected to the proposing bridge node. However, if the proposed-to bridge still has a functioning path to the original root bridge, it then sends a BPDU to the proposing bridge node, informing it of the status of the original root and updating its routes, and STP reconfiguration is performed at the proposing node.

[Figure 9.17](ch09.html#rstp_failover_reconfiguration) shows the proposal concept and demonstrates how the links fail over. The top-right figure shows the original configuration. When a link breaks, as is the case in the top-middle figure, Node A proposes to Node B that it be made the Root node. Because B still is in contact with the Root, the proposal is declined and A is given B's routing information. The failover results in the reconfiguration is shown on the lower left with A's path through B to the Root.

In the case of two broken connections, the response to the proposal is different. When A makes the proposal to be the Root, B no longer knows it has a connection to the Root and therefore accepts the proposal. The result is shown in the figure on the lower right with A containing the Designated port and B having the Root port. The failover results in the direct link between A and B.

![RSTP failover reconfiguration](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0917.png)

**Figure 9.17. RSTP failover reconfiguration**

In a network that is routed by RSTP, any port that is connected to an end station cannot create a network loop because all end stations are by definition single-homed. All ports of this type are labeled as edge ports and put into a forwarding state without having to cycle through the standard STP listening and learning modes. Edge ports remain edge ports even when RSTP recalculates and juggles the topology of the spanning tree. Should an edge port receive a BPDU frame, the edge port converts instantly to a spanning tree port.

An instant conversion to a forwarding state can also be performed on ports that have point-to-point links. Ports that are operating in full-duplex mode are taken to be a point-to-point link; half-duplex mode ports are considered to be a shared port. Because nearly all modern switches operate their ports in full-duplex mode, RSTP can convert these ports very quickly to the forwarding state. Fast transition in RSTP occurs because the proposal/acceptance mechanism can ripple through the network, changing ports one link at a time.

[Figure 9.18](ch09.html#the_rstp_proposal_solidus_acceptance_fas) illustrates the fast transition that RSTP makes possible. In this scheme, the proposal to designate the Root port labeled 1 in the figure on the left side is responded to with an agreement labeled 2. Router 2 then begins a synchronization, which creates a Root port for the Root to 1 connection, blocks two of the ports, and specifies which port will be the Edge port. The proposal to designate the Root port then travels down the network without having to communicate back up to the Root. This makes the transition very fast.

![The RSTP proposal/acceptance fast transition mechanism](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0918.png)

**Figure 9.18. The RSTP proposal/acceptance fast transition mechanism**

RSTP also handles new links differently from STP. In a network system, if you add a link from the root bridge node to a secondary (or lower-hierarchy) node, you create a network loop. STP, sensing this loop, blocks the ports on the root bridge node and the primary node, placing those nodes into a listening state. STP also disables the new link until it can compute the new topology. The primary node now listens directly to the root bridge node and they exchange information. The primary node then sends BPDUs through the network down to the secondary node where the new link was added, and that node blocks its port leading to the primary node, and returns a BPDU back to the root node. Upon receipt of the BPDU, the root node adopts the new technology, enables the new link, and maintains the block on the port leading to and coming from what was the primary node. The primary node connected to the new network link then becomes the secondary node. The problem with this scenario is that there is a latency of twice the forward delay to enforce this change.

The same situation, as handled by RSTP, works somewhat differently. RSTP detects the new link and blocks the ports between the root and the primary node, as before. Now the root node sends a proposal to the primary node for a reconfiguration, at which point the primary node places a block on all designated ports, called a sync operation. The primary node then signals to the root node to unblock its port and place it into forwarding mode. This transition happens very quickly. Now the blocks are one level down from the root/primary link. The process is repeated, moving the blocks for ports on the router one more level down until the blocks reach the port for the secondary node with the new link connected to it. The end result of the RSTP is the same state as before, but instead of waiting for messaging to travel down the branch and return as STP does, RSTP initiates a set of individual transitions that are very fast. The more intermediate bridge nodes there are between the root node and the new link, the greater the difference in performance that RSTP offers.

RSTP is even more aggressive when it comes to propagating topology changes. In STP, when a node changes its topology, the information flows from that node to the root node where it is then sent back down to all of the other system bridge nodes. In RSTP, the originator of the topology change floods the change state throughout the network, essentially eliminating the latency incurred while the information travels to the root node.

You may encounter some proprietary STP variants when working with Cisco Catalyst switches. When routing over virtual LANs (VLANs), Cisco uses a spanning tree for each VLAN (IEEE 802.1Q) and calls their proprietary protocol the Per-VLAN Spanning Tree (PVST), or PVST+ when tunneling across other routing schemes is added. The Multiple Spanning Tree Protocol (MSTP), as defined in IEEE 802.1s/Q, extends RSTP to VLANs, creating a spanning tree for each VLAN group. Cisco's version of MSTP is called Multiple Instances Spanning Tree Protocol (MISTP). Another Cisco protocol called Rapid Per-VLAN Spanning Tree (R-PVST) combines RSTP and PVST to create one spanning tree per VLAN.

# Onion Routers

You know the drill, because you've seen the movie. The bad guys send messages to the good guys, which the good guys trace to a server in New York City. As the good guys get ready to chase the bad guys, the next message comes in from a server in Singapore, and the third message comes from Berlin. Every message after that comes from another server, making the location of the sender impossible to determine. Anonymous communication over the network is the idea behind onion routers.

In an onion router system, network messages are multiply (triply) encrypted at the source and sent randomly through an IP network of routers (onion servers), where each router removes one layer of encryption — just as you can peel the layers off an onion. The Entry Point server is chosen from a smaller set of onion router servers called Entry Guards and then randomly chosen from this set. Each of the three servers, the one chosen randomly from the Entry Guard group and the other two chosen randomly from available onion router servers worldwide, then use their public key to remove one layer of encryption at a time.

When the message arrives at its destination, the message is unencrypted but the receiver has no knowledge of where the message came from or what path it took to get there, only the last server to forward the data on. Not only is the receiver in the dark, but all of the intermediate nodes between the encryption source and the exit node also have no idea of the source, contents, or destination of the packets, making it impossible for anyone inside the onion network to be able to compromise the communication.

[Figure 9.19](ch09.html#the_onion_router_system_for_maintaining) shows how The Onion Router (Tor) system works. The Sending System gets a list of Tor servers from the Tor Directory Server (1). It then selects an entry server from a short list and sends the data to it triply encrypted (2). The Entry Server removes one layer of encryption and then passes the data along to a randomly chosen server (3), which removes another layer of encryption. That second server sends the data to a third server (4) where the final layer of encryption is removed and the data is sent unencrypted to its destination, the Receiving System (5).

![The Onion Router system for maintaining data anonymity](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0919.png)

**Figure 9.19. The Onion Router system for maintaining data anonymity**

The goal of Tor is to be able to prevent what is called traffic analysis attacks. In a traffic analysis attack, groups of messages are examined at both endpoints of the message path to determine which servers exist on the system and to look for traffic patterns. The greater the number of messages examined, the better. The state of the messages can be either encrypted or unencrypted, as the goal is to be able to intercept the messages that you are interested in. Decryption can be performed later; or more often, the goal of the exercise is to be able to interrupt the communication.

One type of attack that can be performed once the communication is intercepted is to create a Secure Shell link to the victim and examine the timing of the messages that are returned. The time interval between each character is statistically analyzed using a hidden Markov model, which can be used to deduce passwords. Tor systems are built to make this sort of attack very difficult, but apparently not impossible. Also keep in mind that the traffic exiting the onion router system is unencrypted and can be compromised, just as any other messages can be.

## Tor

Onion routing describes a technology that presently has one example, the open source Tor project. As you can imagine, secure communication is of primary importance to the military. The original developers of the first onion router were funded by the United States Navy Research Laboratory. A second-generation project called The Onion Router (Tor) was funded initially by the Electronic Frontier Foundation (`www.eff.org`) in 2004, and in 2006 became an open source project called The Tor Project (`www.torproject.org`) as part of a non-profit foundation.

Although onion routers represent a concept that anyone can implement, the Tor network is the only one based on this concept that has been reduced to practice. There are currently over 1,800 listings of Tor servers worldwide in one of the directory servers, although the number of servers active at any one time varies greatly.

## Tor clients

Tor traffic originates on an onion proxy that is installed on the sending system. The proxy consults a Tor directory and negotiates a virtual circuit through the network. The onion proxy software is a SOCKS interface; therefore, any application that can create a socket can use the proxy to send traffic through the Tor network over that virtual circuit. The message is then multiplexed and sent on its way. Among the applications that can use SOCKS are browsers, IM (instant messaging), and IRC (Internet Relay Chat) clients.

To fully configure a Tor proxy client, you need the following applications:

- **Privoxy (**`www.privoxy.org`**)**. The Privoxy application is a filtering, non-caching Web proxy. It can help maintain privacy, manage cookies, alter Web page data, intercept pop-ups and banners, and more. This freeware program was based on Internet Junkbuster and is at version 3.0.10.
- **Tor (**`www.torproject.org`**)**. The Tor client provides the Tor protocol and other components that let you use the Tor network.
- **Torbutton (**`https://torbutton.torproject.org`**)**. The Tor button installs in Firefox and can turn Tor on and off.
- **Vidalia (**`www.torproject.org/vidalia/`**)**. The GUI for Tor lets you monitor, control, and modify a Tor setup.

The developers of Tor make installation of these programs easy by bundling them together within a single installer. To obtain the Tor clients, you can go to these Web sites:

- **Windows installer:** `www.torproject.org/docs/tor-doc-windows.html.en`
- **Mac installer:** `www.torproject.org/docs/tor-doc-osx.html.en`
- **Linux/BSD/UNIX installer:** `www.torproject.org/download-unix.html.en`

Once you install the Tor client, you should test to see that it is correctly installed. One way to do this is to access a hidden server (described in the following section) on the Tor network. Enter **http://duskgytldkxiuqc6.onion/** in your browser, and after a transfer time of up to a minute, the Tor network should resolve the address for you.

## Hidden services

Tor servers form a private Tor domain with the .`onion` suffix. The private domain allows hidden services running network applications, such as a Web publishing server or an Instant Messenger server, to be configured to run "hidden" on the Tor network. Each of these services run independently of one another and are distributed across the Tor network. Tor allows users to configure their own hidden services and make those services available to others anonymously. When a Tor user uses a hidden service, neither the sender nor receiver is aware of either the network identity of each other or of the server that processes their requests.

To create a hidden service, you need a working Tor client and Web server. Tor's developers recommend Savant or Apache on Windows, or `thttpd` on UNIX or Mac OS X. The Web server must bind port 5222 to the local host. This binding ensures that an outside system is not able to ascertain that the service is running on your system. The Web server should be run as a separate instance from any other Web servers, especially Web servers that are exposed to the Internet or an intranet.

[Figure 9.20](ch09.html#hidden_services_on_the_tor_network) shows a schematic of how hidden services work. An installed hidden service advertises for clients by broadcasting its availability (1) using the hidden service protocol through random paths (virtual circuits) to servers and by storing its information and public key in the Tor Directory Server. Those servers accept the role of being an Introduction Point and store a public key for the hidden service (2). Because the path taken between the hidden service's server and the Introduction Points consists of random virtual circuits, there is no way for a client to be able to associate the two systems with one another or to learn the hidden server's IP address.

A Tor client learns about hidden services from the Tor Directory Server (3) and creates a Rendezvous Point. Then the Tor client communicates with one of the Introduction Point Servers (4). A Rendezvous Point contains both a public key and a cookie that are used to encrypt/decrypt information as well as supply information that allows the data to be forwarded from the hidden server to the Tor client. Once the Introduction Point transfers the Tor client's information to the Hidden Service Server, the virtual circuit shown as 7 with a large arrow is created. The system separates the Introduction Point from the Rendezvous Point, and by doing so ensures that the Tor client's information remains anonymous.

![Hidden services on the Tor network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0920.png)

**Figure 9.20. Hidden services on the Tor network**

The hidden service creates a hidden service descriptor with the public key, includes a description of the service, and then signs the hidden service descriptor with a private key. This hidden service descriptor is sent by as an encrypted message to a Tor directory server, and then replicated throughout the network, which hides the location of the service. The directory server creates an automatically generated domain name <*HiddenService*>.`onion` for the service, which can now be browsed by a Tor client. At this point, the configuration of the hidden service is complete.

When a client wants to learn about a hidden service, it downloads the hidden service descriptor from the Tor directory server. That descriptor contains the list of the Introduction Points and the public key. The client then connects to a random Tor server, requesting that the server act as a Rendezvous Point, and sends that server a cookie with a one-time secret. The hidden server's public key is then used to encrypt an Introduction message that contains the Rendezvous Point address and the cookie with the one-time secret. All of these exchanges pass through the Tor system in the usual manner.

The hidden server then uses the information contained in the Introduction message to build a circuit to the Rendezvous Point, and sends the one-time secret to that system to validate its connection to the Tor client. The Rendezvous Point sends a "connection established" message to the Tor client. With the virtual circuit between Tor client and hidden service server using the Rendezvous Point as a relay encrypted communication travels in both directions from client to server. This circuit has a set of six relays, of which three relays were chosen by the client's virtual circuit, three more relays were chosen by the server's virtual circuit, and the Rendezvous Point was a commonly chosen relay point.

# Gateways

A network gateway is a device or program that allows different types of networks to communicate with one another. Gateways translate addresses, network protocols, and data. Sometimes you purchase a gateway as an appliance, while in other instances you might install gateway software on a computer and have that computer serve the linking function. An example of a software gateway would be a program that takes the data from an order entry module on a Web site and transmits that information to a credit processing service, called a credit card gateway. Another example of a gateway is a firewall or proxy server. In any network interface for TCP/IP networks, the address of the gateway must be specified. Mail and host gateways are also common.

Gateways are therefore something of a marketing term, and need to be considered in this broader context. A router has different aspects of a gateway in it; even an Internet connection-sharing function on a computer serves the function of a gateway. What separates a gateway from other network connection devices like routers is its ability to function at higher levels of the OSI network model. Gateways either operate at the Transport layer (Level 4) or more often, at the Application layer (Level 7), the top layer of the hierarchy — routers may operate at Level 4 but never at Level 7.

# Summary

In this chapter, you learned about switching devices. Switches are required on both circuit switched networks and packet switched networks, and both network types were described conceptually in some detail.

Switching devices can be separated by the highest-level protocol that they operate with. Hubs and repeaters are physical connections. Bridges span two different network segments at the Network layer, but do not provide protocol translation. A router can connect two different types of networks because it can operate at the Transport layer. Switches and gateways are general terms that describe a variety of different systems.

The basis for routing was covered in detail in this chapter. The difference between core routers, edge routers, and border routers was also explained. You learned about The Onion Router (Tor) system and how it can be used to preserve anonymity.

In the next chapter, the various types of home networks are described.
