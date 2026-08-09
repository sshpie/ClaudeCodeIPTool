# Chapter 3. Architecture and Design

**IN THIS CHAPTER**

- Different network topologies
- How network connections influence network types
- Segments and routing
- Different network architectures

In this chapter, you learn about different aspects of network design and architecture. Designs can be based on different connection types and topologies; architectures are network systems based on a common protocol. In determining whether you are considering an architecture or topology, an argument based on the highest-level protocol used is presented. Topologies are based on physical transport, while architectures use higher-level protocols.

Different point-to-point connections are considered. Four different types of connections between endpoints can be specified: physical connections, virtual connections, transient connections, and links where there is no defined (unique) connection. These different types are the basis for all modern networks.

A collection of nodes sharing a common physical medium is called a *segment*. Segments are the basic unit of networks; they do not have to have their traffic mediated, and nodes share a common logical address as opposed to a node's physical (e.g., Media Access Control or MAC) address. Segments also define collision domains.

To separate segments, you add connection points such as switches or routers. Networks with multiple segments must have traffic travel over defined routes. These routes may have any of the four kinds of connections. Routing can be 1:1 or *unicast*, 1:many or *multicast*, 1:all or *broadcast*, and 1:any or *anycast*. The effect of switched and packet transfer on networks will be considered.

Several different network architectures will be briefly considered from an overall network design viewpoint. They include peer-to-peer (P2P), client-server, multi-tier, and thin client/server architectures. These different network types determine how network resources must be deployed, where systems can be located, and which of the many different network protocols they may use.

# Network Architecture and Topology

The methods used by systems to communicate on a network are referred to as the *network architecture*. The manner in which the physical infrastructure is deployed to connect a network is referred to as the *network topology*. A topology describes the physical means for transporting data; an architecture describes the technology used to manage and manipulate data.

In some instances, a particular architecture will dictate that a particular topology be used, and in other instances a particular topology will only be suitable for a particular architecture. However, it isn't always the case that an architecture and a topology are so tightly bound.

Most of the time, an architecture is selected to support a particular geographic distribution, organizational structure, user or system load, performance requirements, and the staff available to manage the infrastructure.

The most common architectures in use are described as:

- Peer-to-peer networks
- Client/server (two-tier) networks
- Multi-tier networks
- Directory service or federated networks
- Grid or distributed networks
- Hybrid combinations of the above

### Note

Directory services are covered in [Chapter 21](ch21.html).

### Note

Hybrid networks are just two or more of the aforementioned architectures.

You can determine whether a description of a technology represents a network architecture or a network topology by the highest layer of the OSI model that the technology requires. A topology describes technology that operates at the Physical and perhaps the Data Link layer. An architecture describes technology that operates at the Network level and above.

The difference between topology and architecture can be illustrated by some examples. Ethernet describes a technology that involves frame-based communication over media. While there are variants of Ethernet that run over twisted-pair copper, there are also versions that run over fiber optic cable. The highest layer that the Ethernet standard operates at is the Data Link layer, where a common addressing format based on Media Access Control (MAC) addressing is defined. Ethernet is a network topology. There are many different ways in which Ethernet networks may be constructed — linear buses, hierarchical trees, rings, and so forth — but all of them still are limited to MAC addressing as the single highest protocol that Ethernet supports.

### Note

For more discussion on Ethernet network construction, including linear buses, hierarchical trees, and rings, see [Chapter 1](ch01.html).

The Internet is governed by a number of protocols or standardized agreements on how data should be composed and managed. As a group, those protocols are referred to as the *Internet Protocol suite*. Much of this book is concerned with explaining Internet Protocols, because this form of networking is so overwhelmingly prevalent today, and indeed you are likely very familiar with them.

The Transport Control Protocol and Internet Protocol (TCP/IP) are the two core protocols that give the Internet much of its flavor. Transport Control Protocol (TCP) is a Transport layer protocol, and the Internet Protocol (IP) is a Network layer protocol in the OSI model. Actually, IP is more often described in terms of a different networking model, the TCP/IP networking model, where IP is part of the Internet layer. The TCP/IP Internet layer overlaps with the Network layer in the OSI model, but the OSI model includes certain technologies that involve address resolution in the Network layer that would be better placed into the Link layer of the TCP/IP model. The Address Resolution Protocol (ARP) is the one example that is commonly mentioned. The main reason that these two models diverge is that OSI makes no distinction between communication that is connection oriented and communication that has no defined connection. Be that as it may, if you were to examine the different layers of the TCP/IP model, you would find that nearly all of them are above what would be the Data Link layer of the OSI model; also, many of them, particularly routing protocols, are Application layer protocols. The higher-level protocols make the Internet Protocol an architecture.

[Figure 3.1](ch03.html#comparing_the_osi_model_to_the_tcp_solid) compares the two different network models: OSI to the TCP/IP architecture. The TCP/IP architectural model is described in the IETF's RFC 1122 (`http://tools.ietf.org/html/rfc1122`). You will find a considerable amount of variation in the literature describing how these two models relate to one another, or indeed how the TCP/IP model is structured and named. As a result you should take [Figure 3.1](ch03.html#comparing_the_osi_model_to_the_tcp_solid) lightly. Some authors break the TCP/IP model into four or five different layers and refer to the different layers with different names. In some discussions, the Network Interface layer is referred to as the Link or Host to Network layer. In other discussions, the Network Interface is broken up into a Network Access/Physical, Data Link/Hardware, or Data Link/Physical coupling. The reason that the Application layer in the TCP/IP networking models consolidate the Application, Presentation, and Session layers into a single Application layer is because the upper layer IP protocols span the different layers.

![Comparing the OSI model to the TCP/IP architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0301.png)

**Figure 3.1. Comparing the OSI model to the TCP/IP architecture**

## Point-to-point

A point-to-point connection is the simplest network connection that can be defined for any two systems. Simple, that is, before you stop to think about how even just a few elements can be manipulated to radically change topology and architecture. There are three components to any connection: two endpoints and the path or connection between them. The variation in the condition of these elements defines the type of connection, and each connection type has a defined state that determines the properties of the connection. The state of a connection may be characterized by:

- **Physical**. The component (endpoint or connection) can be physical or virtual.
- **Logical**. The logical state is the name or identifier that is assigned to the endpoint or connection. That name can be an IP address or an actual pathway through a network (the wired and switched connection), or the address and path can be virtual or transient.
- **Signal**. Different types of connections can support one or more session, data sent as an entire message or packetized, and so forth.
- **Performance**. Based on the physical, logical, and signal types, different types of connections can support different levels of performance, and the component that is the rate limiting component varies.

The following sections discuss the four connection types. You can use the accompanying figure for each connection type to compare the connection types, the manner in which they may be physically or logically defined, and the implications that the connection type has on both the signal types that can travel over the connection and the performance characteristics and limitations. The chart next to each connection type in the figures is meant to summarize this.

### Physical point-to-point connections

The most straightforward connection is a point-to-point connection. [Figure 3.2](ch03.html#a_point-to-point_connection_and_its_conn) shows a physical connection with physical endpoints. Sp1 on the left is the sending system, and Sp2 on the right is the receiving system. The connection is made through a permanent medium, most often a wire or fiber, and most higher-level protocols dictate that a negotiation establish the session parameters. Depending upon the power and efficiency of the two network interfaces, as well as their sensed ability to transmit data over the connection, a speed is determined and data flows from left to right during a half-duplex session. If the session is full duplex, then traffic flows in both directions.

The table to the right of each connection type lists the various characteristics of the two endpoints (Sp1 and Sp2) and the Connection (Cp1). For the point-to-point connection type, the endpoints are physical network interfaces (NICs) and the connection is a physical wire. To describe this type of connection you would need to have an address that corresponds to each of the two endpoints, and you would be able to differentiate the circuit or exact path that a signal takes traveling from one endpoint to the other. That path's physical and logical definition wouldn't change for the time that the point-to-point connection was in force.

The advantage of a point-to-point connection is that it is capable of supporting multiple signals because the circuit includes a dedicated connection. The limiting factors of performance are the limiting factors of the physical elements involved. That is, the speed will be determined by the slowest of the following three factors: the signal rate that the sending endpoint Sp1 can send signals, the bandwidth of the network connection Cp1, or the speed at which the receiving endpoint Sp2 can accept incoming signals.

The speed of transmission is determined by a gating factor:

- The media's bandwidth
- The slower of the two endpoints
- The ability of the particular higher-level protocols to process the data

![A point-to-point connection and its connection state table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0302.png)

**Figure 3.2. A point-to-point connection and its connection state table**

If data is sent compressed and/or encrypted, the gating for performance is measured in terms of throughput (bits per second, for example) and may be determined by the ability of the endpoint system to transform the data into clear text — or whatever form is required. To some extent, content buffering can aid in intermittent data transfer, but if you have a connection operating at full speed for a length of time, buffering will only be effective so long as incoming data doesn't overrun the buffer.

A purely physical point-to-point connection is common in small networks and prevalent in peer-to-peer networking. Whereas a point-to-point connection is a topology, peer-to-peer is a network architecture. Picture, if you will, a network of many point-to-point connections forming a web, mesh, or grid of terrifying power (á la Twilight Zone); is that a topology or an architecture? These three different descriptions with a high order of connectivity to other network endpoints are described as a mesh or a grid architecture. If the mesh network exists simply to pass traffic around, then it is a topology; however, if the network distributes processing tasks, as is the case with distributed applications, then the grid is an architecture according to the rule that's been posited in this chapter.

### Note

Peer-to-peer networking is discussed at length in [Chapter 11](ch11.html), and large mesh or grid networks are described in [Chapter 17](ch17.html) where high-performance networks are discussed.

### Virtual point-to-point connections

In the second example of a point-to-point connection, shown in [Figure 3.3](ch03.html#a_virtual_point-to-point_connection_and), all three components of the connection are virtualized. The endpoints Sv1 and Sv2 are virtual network interfaces, and the connection Cv1 is a virtual circuit. A virtual network interface is a simulation in software of a physical network interface. In order to have one or more virtual network interfaces on a system, you must have a physical network interface that network traffic flows through, but any number of virtual interfaces may be defined and given logical addresses that use a physical interface. Network interfaces (including virtual ones) are described in [Chapter 7](ch07.html).

![A virtual point-to-point connection and its connection state table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0303.png)

**Figure 3.3. A virtual point-to-point connection and its connection state table**

The state table for a virtual point-to-point connection is shown in [Figure 3.3](ch03.html#a_virtual_point-to-point_connection_and). To describe this type of connection, you would need to have an address that corresponds to each of the two endpoints, but those addresses aren't unique to the physical interface that either Sv1 or Sv2 uses.

The path or connection is a virtual circuit, Cv1. This means the circuit is built at the start of a session and discarded or torn down when a session is complete. You would not be able to differentiate the circuit or exact path that a signal takes traveling from one endpoint to the other after a session ends because that path changes on a session-by-session basis. However, during a session, the virtual circuit is defined. The process of buildup and tear down of virtual circuits introduces latency into virtual point-to-point circuits that don't exist in a physical point-to-point circuit.

The advantage of a virtual point-to-point connection is that it is capable of utilizing all physical network interfaces and physical circuits because virtualizing all components allows this type of connection to use whatever is available. A virtual circuit is assigned to a session, and therefore, although endpoints can send single or multiple sessions over a virtual point-to-point connection, the circuit is still dedicated to the two endpoints involved, Sv1 and Sv2. Performance over a virtual point-to-point circuit is limited by the endpoint's signal rate or by the bandwidth that is allotted to the Cv1 connection.

A virtual point-to-point connection has the properties of a physical connection. Once the session is established, the signals travel over a circuit that is a dedicated connection. The limiting factors of performance are the limiting factors of the physical elements involved. That is, the speed will be determined by the slowest of the following three factors: the signal rate that the sending endpoint Sp1 can send signals, the bandwidth of the network connection Cp1, or the speed at which the receiving endpoint Sp2 can accept incoming signals.

A virtual connection is a circuit that is built for a particular session and exists for that session. When the session is over, the virtual circuit is released. Most LAN topologies build virtual circuits by providing the appropriate connections at a router or switch, because it is impractical to maintain a full set of physical circuits. In order to build a virtual circuit, the switching devices have to have knowledge of their neighbors and a method for optimizing routes, and there is a certain amount of system overhead involved in "building the virtual circuit" and "tearing the circuit down." That overhead can range from being very resource-intensive to insignificant, depending upon the technologies used. From the standpoint of desirability, once the circuit is built, there is no disadvantage to sending traffic over a virtual circuit versus a physical circuit because a virtual circuit uses a combination of physical connections as its route. Virtual circuits are the central construct necessary to create virtual private networks, which are the topic of [Chapter 29](ch29.html).

Virtualization is one of the great unifying concepts in computer science, one that becomes increasingly important as the industry attempts to optimize system performance. Virtual machine technology is becoming a standard method for all servers and will eventually migrate to the desktop. It is possible to virtualize anything in computer science, provided that you have at least one physical system to provide the needed hardware to perform the heavy lifting. In a sense, virtualization is a form of redirection and partitioning.

### Packet switched or transient connections

[Figure 3.4](ch03.html#a_packet_switched_or_transient_connectio) represents a completely different model for a point-to-point connection — packet-switched or transient connections — where no connection is defined. The connectionless or stateless model is the one that the Internet uses. The lack of a defined circuit completely changes the mechanism by which data is sent and received over the network.

![A packet switched or transient connection and its connection state table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0304.png)

**Figure 3.4. A packet switched or transient connection and its connection state table**

Referring to [Figure 3.4](ch03.html#a_packet_switched_or_transient_connectio), this type of connection uses what is essentially a connectionless model. The sending and receiving systems are shown as Sp1 and Sp2 as two physical endpoints, but they could just as well have been virtual endpoints Sv1 and Sv2, or any mixture of virtual and physical such as Sp1 and Sv2. I've just shown one case for simplicity. The nature of the endpoints is not the important differentiating factor here. The key differentiator is the lack of a defined path, which is shown as the dotted line Ct1 in the figure. No defined "circuit" means that the path varies and that traffic travels over whatever route is the best available route at the time. The best way to think about circuitless or stateless connections is that transmission proceeds on a "best efforts" basis.

This is the first of the point-to-point connections that is stateless; both A and B were stateful. There are some very important conclusions that you can draw from this difference. In a stateful connection, the circuit is defined, whereas in a stateless connection there is no path defined.

Stateful connections can be permanent, which supports sending traffic in a complete stream as a series of bits, bytes, and characters. Traffic sent this way arrives sequenced (in order) and doesn't require reassembly. Indeed, traffic might not even need to be fragmented at all, depending upon the size of the data being sent. In studies of corporate e-mail that I have been involved with, some fraction over 90 percent of the messages are quite small, 3KB or less, but the remaining 10 percent make up 90 percent of the data. With different applications, your mileage will vary, but the implication is that most data is fragmented because most protocols impose a limit on size in order to make their error correction mechanisms tractable.

By contrast a stateless connection uses whatever physical path is available or whichever is the solution of some optimization or routing algorithm. Data as it arrives at an endpoint can travel the same path or any other path. That means that packet-switched networks are able to more fully utilize the physical network than any other type of connection can. For this reason nearly all commercial network connections are based on a switching technology. Only high speed backbone connections tend to deviate from this route. As shown in the associated state table, circuit switched networks tend to send data in a fragmented form and use multiple paths. Performance is something that can be throttled allowing endpoints to vary the sending/receiving rate and modifying the amount of bandwidth allotted to the connection dynamically.

A point-to-point connection can also be defined, but can be intermittent or transient, as is the case in [Figure 3.3](ch03.html#a_virtual_point-to-point_connection_and). This is the case for token ring networks; hosts on the network get full use of the token ring but only on a prioritized basis and only for a session. It is also the case for Virtual Private Networks (VPNs) where the circuit is defined for the session.

To make a connection work when there is not a defined circuit, the sending system always chops data up into chunks, called packets, frames, or datagrams. Each chunk is prepared in sequence, encrypted if needed, tagged with a sequence number, made verifiable with an error correction mechanism (usually a checksum), almost always encapsulated, and sent on its way. As each chunk goes out, it is sent to a branch point in the network and routed by the best available path on a hop-by-hop basis.

If a link goes down, no problem — the chunks of data are sent by other routes. Stateless connections are highly fault tolerant; they will survive even limited nuclear war. Not only that, but because chunks may be routed over the best available path, the entire network can be utilized and bandwidth may be fully exploited. This is not the case with stateful connections. It is for these reasons that packet switched or transient circuit point-to-point connection technology dominates the networking industry.

Notice that I called packet switched circuits an architecture and not a topology. While endpoint addresses are known, the state of the connection cannot be defined. That means that higher-level protocols must always be employed to make sure that data arrives where it is intended to, above and beyond the Physical or Data Link layers.

Along the different routes, some packets will arrive faster than others and be out of sequence, other packets will hit dead ends and need to be resent from the source, and some may arrive corrupted. It is up to the destination endpoint to error check, resequence, and unencrypt the data. Stateless connections require that each node in the network, as well as the destination endpoint, be able to participate in messaging that makes requests for data and acknowledges receipt. Messaging is an additional overhead that stateless connections impose. In some cases, especially when there is a high error rate, overhead can be a very significant burden. When applying Quality of Service (QoS) protocols, it is always easier to manage QoS in a stateful connection and to guarantee a level of service than it is in a stateless technology.

### Switched connections

[Figure 3.5](ch03.html#a_switched_connection_and_its_connection) represents a switched point-to-point connection. When a circuit is available on a time-varying basis, there are two different methods that can be used to provide access to the circuit: *time slicing* and *negotiated access*. The public switched telephone network (PSTN) is the classic example of this connection type.

![A switched connection and its connection state table](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0305.png)

**Figure 3.5. A switched connection and its connection state table**

With time slicing, a node has access to the circuit at regular intervals. Time slicing is common in microprocessors, but extremely rare in network technology. When you time slice access to a CPU, there is nearly no latency involved in fetching information from a primary cache. On the other hand, time slicing access to a connection requires circuit buildup and teardown, and that introduces unacceptable latency into a network. That latency results in a very poor use of a network's bandwidth.

In [Figure 3.5](ch03.html#a_switched_connection_and_its_connection) the endpoints shown are physical endpoints Sp1 and Sp2. This is more commonly the case for switched networks because it is the lack of physical connections and many physical endpoints that typically drive the development of this network type. As with the packet-switched network described in the previous section, the circuit switched connection Cs1 is defined at the time the session is initiated. However, unlike packet switching, a circuit switched network's connection is complete during the entire session. The data sent over the connection may be fragmented, but it travels the same defined transient path. The advantage of a circuit switched technology is that it can support data streams, allows for the physical path to be divided into channels, and by allowing the signal quality to drop can support a bursty operation.

The predominant method used for a switched connection is a negotiated access to the network. Any network technology that uses a token passing system for network access simulates a switched network connection. Token passing is done on regular intervals so that even a node with a high priority can't entirely command a network's bandwidth indefinitely. From the standpoint of other users, a network that is controlled by a single node seems to be frozen and crashed.

Most network connections are switched to guarantee that a path exists between two endpoints. Some network connections, such as bridging links, backbones, and others, are dedicated connections, but they usually represent only a small fraction of the connections on most networks.

### Note

For more discussion on routers, bridges, and switches, see [Chapter 10](ch10.html). For more details on WANs and backbones, see [Chapter 13](ch13.html).

# Switched and Packet Networks

There's a lot of confusion regarding the terms *packets, frames*, and *datagrams* because their meanings are rather similar and depend upon the particular technology in use. A packet is a formatted data chunk that is sent over a packet switched network. Packet switching is a stateless technology that routes traffic on a packet-by-packet basis.

Packet switching was illustrated in [Figure 3.5](ch03.html#a_switched_connection_and_its_connection). On a packet switched network, the data is always sent as chunks that are encapsulated with addressing, and there is no circuit defined. The switching is done at a computer, switch, router, or some other device, and the only role that the packet plays in determining the route that it travels is to present its addressing, and perhaps other data such as priority to the routing device.

The term *circuit switching* is applied to a network that builds a stateful connection between two endpoints over which network traffic flows. The classic example of a circuit switched network is the plain old telephone system, or POTS. As you can see in [Figures 3.2](ch03.html#a_point-to-point_connection_and_its_conn) and [3.3](ch03.html#a_virtual_point-to-point_connection_and), circuits can be permanent or virtual. A circuit switched network can support the widest range of transport protocols because data can be sent as a continuous stream, in whole, intermittently, or in chunks such as packets. Because the endpoints "own" the circuit, at least for the session, the data can be sent in any way that can be successfully negotiated between those endpoints.

In order for packets to be sent and received correctly, the packet data or payload is encapsulated with supporting data such as addressing, checksums, and sequencing. This process is referred to as *framing* or *packet framing*, and the data that is sent is referred to as *frames*. So packetization is the process of chunking the data, and framing is a data format. This is entirely analogous to sending a letter to someone composed of text and then formatting the data inside a word processor document. The text is the letter and the formatting is the envelope.

Remember that packet switching also requires a messaging component. Messages are packetized, but because they may only require a command and no data, what's important for message frames is the data contained in the envelope.

The term *packet* can be applied to connections that are both stateful and stateless, as it refers to the chunking process and nothing else. The term *datagram* is used when the technology employed is over a stateless technology and uses what is considered to be an unreliable service. From the standpoint of this discussion, an unreliable service is one that requires that each step in the process of communication be matched by a messaging infrastructure.

### Note

[Chapter 17](ch17.html) describes the Transmission Control Protocol and the User Datagram Protocol. [Chapter 18](ch18.html) describes the Internet Protocol. A more complete discussion of stateful and stateless communication and the mechanisms used for each is contained in these chapters.

A reliable service that uses packets may or may not send a message back to the sending system that the data was received correctly, but an unreliable service always sends a message back to the sending system. Not only that, but an unreliable service may also send a message back at each individual node that a packet or frame reaches. The Transmission Control Protocol (TCP), when combined with the Internet Protocol (IP), constitutes what may be considered a reliable service, TCP/IP. TCP/IP was constructed to ensure that the data sent is the data that is reconstructed exactly at the receiving endpoint. As a rule, TCP/IP is slower than methods that don't enforce reliable delivery or impose a quality of service.

In the Internet Protocol suite, you can see the impact of messaging on a hop-by-hop basis when you issue a TRACERT command. That command builds a table from returned ICMP messages at each step along the path that the PING packets take to their destination.

By contrast, the User Datagram Protocol (UDP) over an IP network represents an unreliable service. UDP sends data in framed packets, but doesn't require that the data be faithfully reproduced at the receiving endpoint. UDP is used for streaming media and other applications where large amounts of data are being transferred and where the loss of some data isn't important. In a movie passing by at more than 30 frames per second, your mind can't perceive a frame that is missing or out of place. It's easy to remember what a datagram is if you remember that the *D* in UDP stands for *datagram* and that this is the technology used for streaming music and video. So for anything sent as a stream, the use of the term *datagram* is the correct one, although few people would ever correct you if you used the term *frame* or even *packet*, instead. It's a subtlety, but it's worth keeping in mind.

# Bus Architectures

The logical extension of a point-to-point connection is a set of point-to-point connections forming a bus structure, with many nodes sharing a common medium in a daisy chain topology (described in [Chapter 1](ch01.html)). Early Ethernet versions, such as 10BASE5 (which used vampire taps) and 10BASE2 with coaxial cable mated with BNC connectors, have this type of topology.

In a bus architecture, the network bus defines a network segment that is a logical subgroup of network nodes. Network segments not only have the property of common addressing but they also serve as the boundaries for broadcast messages and represent the portion of the network over which network collisions occur. Signals traveling on a network segment require that the signal not be endlessly reflected back and forth on a network segment in order to limit collisions and lower network traffic, which is accomplished by a mechanism called termination. A description of network segments, collision domains, and how termination works is described in the sections that follow.

## Network segments

A bus may be viewed as a set of one or more network segments that share common network characteristics and can communicate with one another with the least possible overhead. Every type of network has at least one network segment. At a minimum a network segment consists of two or more computers that share the same physical medium. Because a network segment represents a fundamental unit in networking technology, let's consider exactly how a network segment is defined and what characteristics it might have.

In some instances, a network segment is a single point-to-point connection, but more often, it is a collection of point-to-point connections. Some network devices, such as couplers, hubs, and repeaters, extend a network segment across both connections. On a token bus network, a network segment is defined as the physical layer between two different Media Access Units. Because a token bus network works by passing a token along the bus from beginning to end, token bus networks are considered a single network segment.

The definition of a network segment as one where systems share a physical network isn't universally applied. Many times, network segments are defined as that part of a network where systems can communicate with one another at the Data Link layer. That is, one system can communicate to another system based on the system's MAC addresses. Another way to look at this definition of a network segment is that it represents a collection of systems where messages can be broadcast to one another, or where all systems are on the same subnet.

Because a subnet is defined as all systems sharing a common IP routing prefix, by definition, all systems in a subnet are in the same broadcast domain. A system on a subnet should be able to browse or PING another system on that subnet. A router, by definition, separates two connections into individual network segments. A broadcast domain is bounded by any Network layer (Level 3) device such as a router or switch.

### Tip

A collision domain may be bounded by any Data Link layer (Level 2) device, such as a switch. A broadcast domain may be bounded by any Network level (Layer 3) device, such as a router. [Chapter 2](ch02.html) describes the OSI data model in detail.

Because a subnet is based on a routing prefix, in theory, each connection on the router should be an individual route. At the Physical layer, this is true, but a subnet is defined at a higher protocol level: at the Network layer in the OSI model, or for TCP/IP, at the Internet layer of the TCP/IP model. There is nothing that prevents having systems with the same subnet on both sides of a router, provided that the addresses of the systems are unique. So while in most cases, networks choose to isolate subnets on one connected link of a router for performance reasons, it isn't always the case. It's a subtle point, but one you should be aware of.

If you separate parts of a subnet across a router, you are separating those fragments into different broadcast domains. Therefore this book uses the term *broadcast domain* to represent any system in a group that can receive a broadcast from another system, which is not necessarily the same thing as a subnet.

## Collision domains

It is important to be able to recognize the boundaries of a network segment in Ethernet networks in particular, because they define what is known as a *collision domain*. A collision domain represents the physical layer over which collisions are possible. A collision domain is bounded by any Data Link layer (Level 2) device such as a switch. In designing networks, an important consideration is to limit the size of any one network segment in order to minimize the number of collisions that packets have. In a token ring or token bus network, only one node can communicate over the network at any one time, collisions are largely avoided, and the idea of a collision domain does not apply. As a general rule, collision domains are smaller than and contained inside broadcast domains.

[Figure 3.6](ch03.html#this_idealized_network_shows_different_c) shows a representation of collision domains and broadcast domains. The collision domains are indicated by the circles in the diagram, while the broadcast domains are bounded by the rectangles. On the left-hand side of the figure the two collision domains labeled PCs on Segment_1 and PCs on Segment_2 are two different subnets each separated by a switch. Each of those subnets has their own logical address (subnet) and is bounded by a Data Link layer (Level 2) switch which defines the collision domain. The collision domain indicated by PCs on Segment_3 includes Hub_2 since a hub is a logical Physical level (Layer 1) device. The broadcast domains include the switches that the subnets are connected to, but end at the routers, which are Network layer (Level 3) devices.

Collisions occur on networks that use a shared transmission medium. By the term *shared*, I mean that the wires are shared, as is the bandwidth of the connection. As mentioned previously, you can use different token passing techniques to restrict network access. Systems of this type typically have a node send data as a complete stream from the source to the destination. That means that for the time that the entitled system has network access, it is in possession of a "dedicated circuit," and the throughput of that particular transaction is high. A dedicated circuit is one that can only accept traffic from a single endpoint or network node. Data arrives at its destination in sequence and generally requires less error checking. However, not all networks operate in this way, nor is it desirable for them to do so.

![This idealized network shows different collision and broadcast domains.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0306.png)

**Figure 3.6. This idealized network shows different collision and broadcast domains.**

A network collision occurs when an endpoint or node starts to read the signals coming from one source, and before that data is completely received, it detects signals coming from another source and either appends the signals or intersperses them with the first source's data. Every type of network connection has a certain error rate due to collisions, and every network transport method employs a means for validating the integrity of the data it receives. The exception to this rule is a full-duplex circuit where traffic flows in both directions and each direction is separated from the other. As traffic on a network increases, the percentage of traffic suffering collisions rises, eventually becoming a significant burden.

To prevent network collisions, nearly all networking protocols include a messaging component that acknowledges successful receipt or requests retransmission of any suspect communication. There are different technologies employed to detect collisions. The two most common are:

- **Carrier Sense Multiple Access with Collision Detection (CSMA/CD)**. This is the protocol that many wired networks, such as IEEE 802.3 Ethernet, use. This method has network nodes listen (carrier sense) to the channel they are on for quiet periods before they transmit new data.
- **Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)**. With this protocol, nodes actively signal to the network that they are about to transmit before doing so. Collision avoidance is slower than collision detection because it adds additional steps to each data transfer.

### Note

The two CSMA protocols are discussed in detail in [Chapter 12](ch12.html) (for Ethernet CSMA/CD) and in [Chapter 14](ch14.html) (for Wi-Fi CSMA/CA).

## Signal termination

It is possible to have high collision rates, even on networks with low traffic, if the connections you use aren't properly configured. Many network technologies, just like system buses, require that segments be properly terminated at their endpoints. Failure to do so results in reflection of the signal and collisions. Termination is meant to reduce signal strength to a point where any reflected signal's amplitude falls below the threshold of a recognized signal and is ignored.

A dedicated circuit means that during the periods when that circuit is not in use, the bandwidth that the circuit represents is wasted. A dedicated circuit also means that the network must ensure that the circuit is always available in order to provide a certain level of QoS. When you want to maximize a network's bandwidth or you are sending data over links that may be transient or of varying quality, a different method must be used. That is the situation that the creators of the Internet faced, and the purpose that TCP/IP was designed for. In TCP/IP, data is sent in pieces over the best available route, and retransmitted when necessary. Packets arriving at their destination are resequenced and validated. This allows for maximum use of bandwidth and fault tolerance at the expense of additional overhead.

There are examples of network technologies that use neither a broadcast domain nor a collision domain. They are categorized by the creation of a single dedicated link, usually established at the Data Link layer (Level 2). Examples of these kinds of technologies are VPN and the Point-to-Point (PPP) protocol. PPP links are authenticated, and data sent over the link is both compressed and encrypted. PPP is used on many different types of Physical layer connections, from Unshielded Twisted Pair such as phone lines, serial cables, cell phone links, and even fiber optic connections, to Synchronous Optical Networking (SONET) networks. There is no broadcast domain because the endpoint of the communication is the endpoint of the PPP link. There is no collision domain because the link is dedicated and the PPP protocol does not support broadcast. However, the encrypted data within a PPP frame can include a broadcast, but that is handled by the system to which the data is forwarded.

# Connection Points

Few networking technologies use a bus topology anymore; the increasingly low cost of switches and routers have seen to that. Switches and routers serve as a locus at which a collection of endpoints may be connected. The problem is that a bus offers only limited upgrade capabilities and hardly any flexibility for moving things around. Most networks use connection devices of various types: hubs, repeaters, switches, routers, and gateways. [Chapter 9](ch09.html) describes these devices and how they operate in detail, but for the purposes of this chapter it is worth taking a moment to discuss why they are used and what complexity they offer in network design and architecture.

### Note

[Chapter 9](ch09.html) describes hubs, repeaters, switches, routers, and gateways. Token rings are described in [Chapter 12](ch12.html).

Hubs are the simplest devices; they are simply ways of extending a network segment. All devices connected to a hub are on the same network segment, and the hub is simply a Physical layer device that is almost like an extension of the wire. Signals travel through the low-resistance connections of a hub unimpeded. From the standpoint of network topology, hubs create star shapes or can be linked to create a hierarchical tree structure. A repeater is a hub that provides signal amplification. In a network segment that contains a hub, all of the previous discussion on a collision domain and network segment applies.

Switches can be Network layer (Level 3) or Data Link layer (Level 2) devices, and they introduce a physical separation between network segments. Routers are switches that are endowed with the ability to route data intelligently using protocols that they understand and algorithms that run on them, and by creating and exchanging stored routing data in memory or permanent storage. The concept that these devices introduce is the route. A route is a defined path through a network from the source to the destination. At a switch or router, the route would be defined as the path through a network from that connection point to the endpoint. A route is composed of the different hops taken through the network, which represents individual network segments.

Switches and routers are widely used on most networks today. They introduce great flexibility into a network, provide node fan-out, fault tolerance due to route switching based on conditions, and for routers, the ability to adapt and optimize the route that data takes. In networks with only switches, routing may be done at a host, but in networks with routers, the router is responsible for routing traffic.

Route optimization is necessary because there may be many paths from one endpoint to another and some may be very slow or even intermittent. There are different types of routing optimizations possible that algorithms try to calculate, one based on the time it takes for travel, one based on calculating the smallest number of network segments that must be traveled, and another based on maximizing throughput. In most instances, optimization is done by providing the fastest route or the route that offers the most throughput. It is possible to manually create and modify static routing tables.

### Note

Static routing tables are covered in [Chapter 9](ch09.html).

There are four common routing topologies and include the following:

- **Unicast (1:1)**. Communications that are sent from one endpoint to another endpoint are referred to as *unicast*, and the process of sending this kind of message is called *unicasting*. Unicasting represents a single destination system by whatever route or routes are used. Many streaming services, such as Real Audio, use unicast technology.
- **Broadcast (1:all)**. A broadcast is sent to any system on a network (usually a network segment) that can hear the message. Broadcasts are generally confined to a single network segment because they are very bandwidth intensive.
- **Multicast (1:many)**. Multicasting is a message delivered to a group of nodes, usually through a subscription or opt-in mechanism.
- **Anycast (1:any)**. Anycasting is a message sent to the nearest or best destination, where it is responded to by a single system.

[Figure 3.7](ch03.html#the_four_common_routing_topologies) shows these different routing topologies.

![The four common routing topologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0307.png)

**Figure 3.7. The four common routing topologies**

Gateways are Application layer (Level 7) devices. They are used to connect two different network types together at any level of the network model. You might use this type of device to connect an AppleTalk or IPX network to a TCP/IP network, although these days, most networks with Apple Macintoshes and Novell Netware use TCP/IP as the preferred protocol. Gateways can also work with applications, providing translations from an application such as a Web server to an e-Commerce server.

Bus networks are open networks where there are no close paths; but many networks are built using a ring topology. The most common examples of ring networks are the IBM Token Ring and Fiber Distributed Data Interface (FDDI) networks. Were it not for marketing, we might all be using Token Rings today instead of Ethernet, but that is another story. Rings are created in many ways. In Token Rings, they are often wired together using a star topology where hubs connect to nodes called stations, and one wire leads into the loop and another wire leads out. A ring topology has a single collision domain and theoretically is a single network segment.

On a ring network, if a connection fails, the segment would be broken and the ring destroyed. To alleviate this problem, ring networks use failover rings and MAUs. Many ring networks are built using two rings, and can either use the second ring as an additional data path or keep it in a hot backup capacity. The second technology uses devices that IBM calls Multistation Access Units, or MAUs. A MAU works at the Data Link layer (Level 2) to create a logical ring structure from a network comprised of star units.

To avoid collisions on a ring network, a method of network access called *token passing* is often used. A token is sent around the network, and each node that receives the token compares their priority to the one contained in the token. As data from one node is delivered, the arrival of a token then allows another node to begin communication. With a token passing scheme, only one node at a time has access to the network, but when that node is communicating, it is able to do so at the full network speed using the entire network bandwidth.

# Peer-to-Peer Networks

Peer-to-peer (P2P) networks are the first of a set of network architectures that will now be considered from a design standpoint. The previous networks described were bus networks that could be considered as simply a collection of unrelated connections. P2P networks are created as a logical extension of a collection of point-to-point links. P2P networks can use any one of a number of technologies, and even be composed on the fly, creating a network composed of ad hoc connections. The key differentiating factor that determines whether a network is P2P or some other architecture is whether each node participates in the network interaction as a nearly equal partner in processing data. [Chapter 11](ch11.html) covers the topic of P2P networks in detail, but it is valuable here to say a few words about P2P networks as context for other architectures such as client-server, X-architecture, and multi-tiered networks that follow.

### Note

[Chapter 1](ch01.html) covers the various network topologies that the different architectures can use, including bus, ring, mesh, and hybrid networks.

A peer-to-peer network has a different meaning, depending upon the context in which the term is used. Microsoft uses the term *workgroup* for a peer-to-peer network on their operating system. The services participating in a peer-to-peer relationship are the security service, file and print service, and a shared Internet connection. In a Windows workgroup, only those workgroup members that are on the same network segment using the TCP/IP protocol may share network resources of the workgroup of which they are members. Microsoft differentiates their workgroup from a domain network, which uses a directory service.

If you examine the situation more closely, you will find that Windows workgroups distribute the server functions on whichever member of the workgroup is either attached to and sharing the resource, such as a file or printer share, or attached to the first system on the workgroup to recognize that a particular network service such as a browser is required. Microsoft imposes connection limits on their workgroup members so that a personal Web server can only serve up to ten connections on a network. Microsoft Windows desktop operating systems are detuned versions of the core server operating system with restrictions placed in the code in several other important areas.

Microsoft packages different sets of modules and extensions that seem to differentiate these OS versions more substantially than they are in fact differentiated. If you are willing to spend a little time installing interface components, adding some additional features, and changing some of the runtime behavior of services, you can make a Windows Server appear to an outsider to be nearly identical to a Windows desktop. So even though it appears that workgroups are P2P, they are actually a fully distributed client-server system. A true P2P application, to my mind, uses other systems for data sources and processes each application locally. This is a fine point, but it is worth keeping in mind.

Many people skirt this definition and only say that on a P2P network, nodes are equal in terms of functioning as both a client and a server on the network. When you examine P2P applications such as BitTorrent, Kazaa, and other applications that use this architecture, they tend to use a pure P2P model for some functions and an ad hoc client-server model for other functions. You will find some P2P networks use centralized (server directed), decentralized, structured, and unstructured models, as well as hybrids of these types.

### Note

[Chapter 11](ch11.html) goes into detail on the architecture of some of the better-known P2P applications, such as BitTorrent and Kazaa.

# Client-Server Networks

A client-server network is a two-tiered software architecture where a server system performs processing that is used by a client system or systems. Client-server systems are currently the most commonly deployed form of distributed network computing and are often used in network applications such as databases, e-mail, browsers/Web servers, and other technologies that you are familiar with. Client-server technology requires that the server run server software and the client run client software; it also requires that these two pieces of software be either different or the same but serve different functions.

There is no restriction other than the ability to communicate with one another using the required protocols where the server and clients are located. In most instances, clients and servers are on different systems. In some instances, the server and the client are on the same system; this is called a single seat system.

In order to make a client-server application work properly, there must be a protocol that is used to request services from the server and a protocol that allows the server to provide data and/or transfer necessary data for processing from client to server. Often these protocols are part of a unified protocol. Commonly used network data transfer protocols include HTTP (Hypertext Transfer Protocol), SNMP (Sip), Java RMI, .NET remoting, TCP (Transmission Control Protocol), UDP, (User Datagram Protocol), Sockets, Windows Communication Foundation (WCF), CORBA, (Common Object Requesting Broker Architecture) and others.

The literature describes client-server interactions in terms of sequence diagrams — which are flow charts that illustrate how messages are related and sequenced — and store these diagrams in files formatted in a standard interchange file format. You may encounter the terms *timing diagram, event scenarios*, or even *event tracing diagrams* in place of the term sequence diagram. These days, sequence diagrams are stored most often in Unified Modeling Language (UML) files. [Figure 3.8](ch03.html#effexis_software_apostrophy_s_sequence_d) shows a sequence diagram in Effexis Software's Sequence Diagram Editor utility (`www.sequencediagrameditor.com`). This utility and others in its class allow you to design a sequence graphically and then save it out to a UML file.

![Effexis Software's Sequence Diagram Editor utility](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0308.png)

**Figure 3.8. Effexis Software's Sequence Diagram Editor utility**

In a classic client-server architecture, there is a clear differentiation between the actions of a client and a server. A client can initiate a request and processes the response when the reply is received. An application on the client that has made a request is dedicated to that request and waits for the server's reply. Clients can be connected to one or more servers concurrently, but most often there are a limited number of connections in order to preserve client performance. For example, Microsoft Internet Explorer can create and manage four connections, and Apple iTunes can manage three connections. Because actions at clients usually involve user interaction of some sort, clients often provide a graphical user interface, or GUI, application.

The term server can be applied to a specific application, program, or software module that can perform computing upon request. A server can also refer to a hardware platform or appliance that runs any of these categories of software. Servers can advertise the availability of their service, but do not send data to clients without a request. Servers can be configured using a configuration utility; sometimes they are GUI applications, and many times they are Command Line Interface (CLI) utilities. When a server is running, it creates a process called a service. Services related to operating system functions are often managed within the Services utility provided by the server's operating system.

Windows Server's services, for example, can be managed within a Microsoft Management Console (Services in Administrative Tools) for later versions of the operating system, or within a Control Panel for earlier versions. Services also appear in the Manage Your Server utility for Windows Server 2008. When a service is part of an application such as an enterprise database, it is common for the vendor to include a management utility or console in which services are configured and turned on and off. Services can be disabled, turned on automatically at startup or after a delay (Windows Server 2008), or set to be turned on manually.

# Multi-Tiered Networks

Multi-tiered architecture, sometimes referred to as *n-tiered* or n-layer architecture, is a form of client-server architecture where a middleware service negotiates transactions between client and server. In this architecture, the client talks to the middleware server, the middleware server talks to the server, and in return the server talks to the client through the middleware layer. Examples of middleware applications are the various transaction servers and Java 2 Enterprise Edition.

[Figure 3.9](ch03.html#two-tier_versus_three-tier_architectures) shows a two-tier or client/server versus a three-tier architecture. In nearly all deployed n-tier applications, a three-tier architecture is used. A client/server has two different layers only, the client and the server. The different layers in a three-tier architecture provide separation between different fundamental network functions as follows:

- The client layer or presentation tier provides user interaction and system management tools.
- The middleware layer or logic tier enforces the logical rules of the system and manages interactions in the form of discrete transactions.
- The server layer or data tier consists of server applications and services, which provide access to stored information.

![Two-tier versus three-tier architectures](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0309.png)

**Figure 3.9. Two-tier versus three-tier architectures**

Adding a third tier to a client-server architecture provides a number of very specific benefits. By decoupling client from server, you can use the middleware server as a translation service, talking to each with a different protocol. The middleware layer abstracts both the client and the server, making both locations transparent to the other, and allowing any transaction that reaches the middleware server intact to survive a loss of the client or server's connections or the loss of either system for any reason. Transactions provide the ability for exchanges to be message-based and to comply with the ACID (Atomicity, Consistency, Isolation, Durability) model. When there is a transaction failure on an n-tiered network, those transactions can be rolled back. The ACID model describes the properties that a database transaction must maintain in order to be reliably processed as a well-defined single logical operation.

Three-tier systems are much easier to scale and provide much greater range for modular design and non-disruptive upgrades. The reason that this is true is that the middleware layer essentially decouples the client layer from the server layer. Should you require a major upgrade or change to the middleware layer, you can create this new system and change the references in the client and server software to point to the new middleware systems. Often it is possible and desirable to deploy multi-tier systems with different operating system platforms.

# Thin Client/Server

The last of the network architectures that you will consider are client-server and server-client architectures based on *thin clients*. A thin client can be a terminal with networking and display subsystems but with little processing power. Thin clients can also be computers or portable devices running a lighter-weight operating system such as a stripped-down form of Linux, an embedded Real-Time Operating System (RTOS), or Windows CE. They can also be fully enabled computers running client software. Thin clients are thin because most of the processing is being done on a "server"; the thin client serves to provide input and display.

I've placed the term "server" in quotes because there are two different types of client-server networks in use; they both do more or less the same thing. X-windows calls the application running on the client the server and refers to the server or provider of the data as the client. X-windows runs graphical applications on workstations with the workstation being responsible for display and the server being responsible for processing everything else.

The second type of thin client/server is essentially the same thing, but reverses the naming convention. In Windows Terminal Server, for example, the thin client is the workstation that displays the application on its monitor, and the server is the system that does all of the processing. A Windows terminal is taking graphics information that was processed on the server and rendering that information. The key point is that a thin client/server has the workstation as the client, whereas in X-windows, the workstation is considered to be the server because that is the system that is initiating the commands (as is also the case for the client in a thin client/server system).

## Terminal servers

A terminal server is an example of a thin client network where the server runs processes for multiple connected clients. The best-known examples of this centralized computing model are Windows Terminal Server (a service of Windows Server 2008/3) and Citrix XenApp (formerly Citrix MetaFrame (`www.citrix.com/English/ps2/products/product.asp?contentID=186`). In these network systems, the server's memory is partitioned and instances of the unique portions of the desktop operating system are run on the server inside each partition. The parts of the operating system that are common to all running instances are runs in a shared memory space, which is why a server can run many terminal sessions at the same time.

When a thin client logs into the server using a special display transfer protocol such as Microsoft's Remote Desktop Protocol (RDP) or Citrix's Independent Computing Architecture (ICA), in both cases the display of the desktop running on the server is sent over the wire in compressed form to the thin client. Applications and services can be run in the client instances on the server, and the results appear as they are calculated and transferred with little data actually being exchanged.

The nature of terminal server technology means that a powerful server with enough memory can run many desktops on a single system, or that a server farm can be employed to distribute the processing load as needed. Because the server is under administrative control and the desktops closely constrained by system policy, the user has little opportunity to modify the software or alter the hardware in ways that would be problematical. Indeed, many thin clients are sold as diskless systems.

## X Window networks

The second type of thin client solution is the X Window System, which is based on the X11 network protocol. In an X Window system, the server is the application on the thin client (X terminal) that provides access to the system on which processing is occurring using the X display protocol. X Window calls the processing system the *client*. The oldest versions of X Window ran on UNIX and DEC OpenVMS, but modern versions of X Window can be downloaded for any desktop operating system you can name.

### Note

For information on X Window products go to: `www.x.org`, `http://xwinman.org/`, and `http://en.wikipedia.org/wiki/X-windows`.

The X Window System server opens a graphic user interface such as GNOME or KDE on Linux in the window. X Window is particularly useful when you want to run a process on a computer with a different operating system from another system on the network. X Window's applications are transparent over the network; what you see on the desktop (the display server) is running as an application on the client. X Window is a client-server technology, just as terminal servers are. However, here the server is the system giving the orders (user commands) and the client is the application. X Window considers that it is the application that is using the display services of the thin client as its server. Although the names applied are direct opposites, the underlying network architecture is the same.

X Window has a long history behind it and many unique features. If you are working on a heterogeneous network, it might be a technology you want to look at.

# Summary

This chapter presented a number of general network design principles imposed by different network devices. Among the topics described was how topology can relate to the type of network architecture. The difference between a topology and an architecture was considered.

Point-to-point connections are considered physical connections, virtual connections, transient connections, and links where there is no defined (unique) connection. When nodes share a physical medium, they are a segment. Segments define collision domains. Collections of segments are separated by connection points such as switches or routers. Different routing types, as well as switched and packet networks, were discussed.

In this chapter, you learned about peer-to-peer, client-server, multi-tier, and thin/client server architectures.

In the next chapter, you will learn about different methods for network discovery and how you can use them to map out a network and the resources that it contains.
