# Chapter 1. Networking Introduction

**IN THIS CHAPTER**

- Network and transmission types
- Topologies
- pLANs, LANs, MANs, CANs, and WANs

A computer network is a connection or set of connections made between two or more computers for the purpose of exchanging data. Networks are built from a variety of building blocks: computers, switches, cables, and so forth. In order to classify networks into different types, you need to consider factors such as the number of elements, distribution of objects, and connection methods. In this chapter, different types of networks are described, as well as how the different network types impact their design.

The smallest network is a direct attachment between two computers with a cable. Peer-to-peer systems are used in computer workgroups where there are a small number of systems that don't require a central service. Some computer buses are configurable and thus are considered small networks. These are called personal LANs, or pLANs, and Bluetooth is an example of this type of network. USB is not configurable and is therefore not a network.

A network that spans an office, floor, or building is called a local area network, or LAN. LANs can support multiple protocols, and connect different types of clients. A LAN that is separated by a bridging element would be considered a separate LAN. When the bridge separates multiple LANs that are geographically dispersed, it is considered a wide area network, or WAN.

You can analyze and categorize network topologies in terms of graph theory. Networks can be formed in a variety of ways that involve forming lines or chains, stars or hubs, rings, or mesh topologies. Different topologies offer different capabilities and have different requirements. The processes of mapping a network's topology can be done for physical or logical network elements, or based on how signals propagate through the network.

# Defining Computer Networking

To be considered a network, a collection of elements needs to have the following: connection software, systems, and network elements (such as switches, physical transmission media, and an addressing system). Any computer network has the following essential components:

- The connected systems
- Connection software
- Networking hardware
- Physical transmission media
- An addressing system for each of the aforementioned components

This definition is sufficiently broad to allow us to discuss not only systems composed of computers, but also cell phones and other aspects of telephony, storage devices, Wi-Fi, streaming, broadband connections, and a wide range of disparate systems that you are likely to want to network together in some way.

Connection software is ubiquitous in all systems that must be networked together. You will find network software inside your computers' operating systems, inside your networking hardware (routers or firewalls), in custom ASICs (Application Specific Integrated Circuit) or flash memory in network cards or hubs, and even inside the physical transmission medium if the medium is intelligently switched or amplified.

The physical transmission medium refers to any medium that can transmit an electromagnetic signal. A signal is a time varying pattern in signal amplitude, voltage, or frequency that represents information in the form of data that can be propagated some distance and recognized by a receiver. Signals can be continuously variable (analog), or they can be discrete and limited to specific states (digital). Although analog computers exist, in nearly all circumstances the systems in use are digital, and more specifically binary. Binary systems transmit information in one of two states: ON or OFF, 1 or 0, YES or NO, or voltage 1 or voltage 2. Digital computers use binary signals and Boolean logic because signaling is relatively simple and fast, and because binary signals can be made to represent any character or solve nearly any mathematical equation.

The transmission of binary signals for the data stream between two systems in a network means not only that the physical media can be wires and cables, but also that any part of the electromagnetic spectrum can theoretically be used to transmit data. When you open a browser on a cell phone, you are connecting to a network with a radio frequency connection. When a cellular network wants to transmit data across a long distance, it does so by using microwave transmitters. The 802.11 Wi-Fi standards are radio frequency transmissions. You can get interference from a 900 MHz wireless telephone that overlaps with the 802.11b standard, or from a microwave oven that operates at 2.4 GHz and interferes with the 802.11g Wi-Fi standard. Most of the networks described in this book use fixed wires to connect computer systems. However, radio frequency connections have no physical transmission medium.

### Note

Radio frequency connections are covered in [Chapters 5](ch05.html), [8](ch08.html), and [14](ch14.html).

Any operations where data isn't transmitted automatically aren't part of our network definition. For example, if you copy data on one computer to a USB key and walk that USB key over to another computer, that wouldn't be considered a computer network. The term we use to describe manual data transfer is *sneakernet*; this is not a network because it doesn't conform to the principle that networks allow data to be sent to a system based on an address or identification scheme — the data in the USB key isn't being sent to any address.

It's best not to be too doctrinaire when using the addressing requirement, however. Broadcast communications would be considered network communications, although there is no specific address to a receiving system. Any system that fits the definition of a receiver can accept broadcast communications. Indeed, broadcast communications are essential in most network technologies. Systems send out broadcasts to indicate that they are available to perform a service, or that they exist and can service a request. Broadcast communications are used to identify a system or to browse the network. Implicit in the definition of a broadcast is that any system that conforms to the requirement meets one of the following conditions:

- It is on the same network, or runs the same identification protocol, such as Windows NetBEUI or WINS; or
- It has the software installed to accept and manage a data stream and can participate in broadcast communications.

In this book, I define a computer network as simply a connection or set of connections made between two or more computers for the purpose of exchanging data. Using this as a guiding principle, I cover the most common problems encountered by network administrators in business networks; by average users connecting to various important services (such as e-mail); or by people who require fundamental networking skills to manage the collection of devices that are typically found in a connected household. This book teaches you the basic principles of computer networking, which can help you solve some of the problems you might encounter in your daily work or play.

# Network Type Overview

Networks are categorized by distribution, size, and architecture. A network can be as simple as a single serial, parallel, or USB cable joining two computers in a peer-to-peer relationship. When you connect a cable between two computers for the purpose of moving your installed software, you are creating a peer-to-peer network. These relationships can be *ad hoc*, meaning that the network is configured as needed when it is needed. Most people wouldn't consider two systems connected in this manner to be a network. However, if you had several systems joined in a workgroup and connected though a hub, then this would fit the definition of a peer-to-peer network. A *workgroup* is a collection of computers that do not share a common security database, and where network services can be provided by any member of the workgroup as required.

The smallest networks from a distribution standpoint are personal area networks, which have come to be called pLANs (alternatively abbreviated as PANs). A pLAN is usually applied to a set of peripheral devices that connect to a single computer system. Bluetooth is a good example of a pLAN. Bluetooth devices are radio frequency connections that use frequency hopping spread spectrum technology (the communication channel constantly changes) that segments the data stream and transmits it over 75 different frequencies with approximately a 30-foot (10-meter) range. Although this kind of network is small in size, pLANs can be quite sophisticated in terms of their technology. Bluetooth has the ability to self-configure, be secured, and advertise each device's available abilities and services. Some phones, headsets, mice, keyboards, printers, GPS devices, game consoles, and PDAs use Bluetooth technology and are common examples of Bluetooth devices.

Bluetooth certainly fits this book's definition of a network because it has all of the necessary components of a network. Bluetooth is discussed in this book because it is something that you have to configure. On the other hand, Universal Serial Bus (USB) can connect up to 127 devices per host controller, but it is self-configuring and is therefore considered a computer bus. All of the aforementioned Bluetooth devices can be connected to a computer using a USB connection. So while they are devices on a Bluetooth pLAN, they are more correctly described as peripheral devices. While USB is very capable of transferring data, it is only described as needed in this book.

### Note

For more on USB, see [Chapter 11](ch11.html).

A large portion of this book is dedicated to the subject of local area networks, or LANs. The term *local* is subjective. A LAN is a connected set of systems that spans a single room, floor, or building, and can be as small as a couple of systems connected through a hub. LANs are differentiated by their addressing scheme, as well as by the set of rules or protocols that they use to communicate. Therefore, an AppleTalk and a Netware network are considered to be separate LANs. Heterogeneous networks are common, and so you may find that a LAN has a Windows network with a domain server that contains Macintosh clients and Netware servers. Those Macintosh and Netware systems can still participate on an AppleTalk or Netware network, but the software and addressing used are separate for each particular LAN.

A LAN ceases to be a LAN when the addressing changes in some meaningful way, or when there is a bridging function that links two or more networks. For example, if you had a network of computers and chose to give one group of computers one set of related addresses and another group of computers a different set of addresses, then that arrangement would still be considered a LAN. You can do this with Internet Protocol (IP) networking by using a different IP range (192.168.1.x versus 192.168.3.x), or by defining a part of any range as two or more subnets (192.168.1 through 192.168.1.99 and 192.168.1.100 through 192.168.1.199). In either case, this would still be considered a LAN. If you put a couple of routers or bridges, which are intelligent switches, in between the two network types, you would now have a set of distinct networks. The case is even more compelling when the connection between the two switches is long or when there are additional switches in between the two that provide entry to the different networks.

A variety of terms are used to describe long-distance networks or multinetwork scenarios. The most common term is the wide area network, or WAN, which is applied to any network of networks. The Internet is the most common example of a WAN, and the term *internetworking* is occasionally used to describe this scenario. Other terms in use are campus area networks, or CANs (uncommon), and metropolitan area networks, or MANs. CANs span a set of buildings, while MANs span a city.

Large, geographically dispersed networks typically use a high-capacity interconnect such as fiber optic cable with signal repeaters to span the distance. A high-capacity line is referred to as a *backbone*. For example, if a bank on Wall Street in New York City were to back up or mirror their data over a fiber optic line under the Hudson River to a data center in New Jersey, then that would be considered a MAN.

# Transmission Types

Networks use two different types of data transmission: Point-to-point communication and broadcast communication.

## Point-to-point communication

Point-to-point network communication creates named connections between two systems in the network: the sending and receiving systems. In point-to-point communication, there may be one or more intermediate systems that process the data stream along its intended route. Many point-to-point networks have redundant paths through the network, often of differing length. Therefore, the role of routers in a point-to-point network is a key factor in determining network performance.

Various technologies are applied in point-to-point networks to ensure that the connection is made correctly, particularly when the connection spans multiple subnets, as it would in a WAN, as shown in [Figure 1.1](ch01.html#a_packet-switched_wan). The WAN in [Figure 1.1](ch01.html#a_packet-switched_wan) has three subnets — a ring network, a bus, and a wireless LAN. One technique of data transfer, called store-and-forward, takes an incoming packet sent by one router, and at a second router stores those packets until the desired point-to-point connection or connections become available. Once the connection is free, the packet is sent onto its destination. This mechanism is sometimes referred to as *packet switching*. A packet-switched network composed of small, equally sized packets referred to as *cells* is important in the area of wireless telephony, and is the basis for the cellular networks in common use today.

## Broadcast communication

Broadcast communication networks take a message from the sending system and then transmit that message to all systems on the network. A satellite network is an example of a broadcast network. When a broadcast network is configured to send a message from one system to a subset of the available nodes (communication endpoints), that process is called *multicasting*. Multicasting is common for systems that stream media, as the same data stream can be targeted to multiple systems.

![A packet-switched WAN](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0101.png)

**Figure 1.1. A packet-switched WAN**

Broadcast packets contain addressing that specifies which system is to be the receiving system or systems. The receiving system can be a single computer or multiple systems, but every node on a broadcast network gets to examine the packet. When the broadcast packet arrives at a node on the network, the address is examined and if the address matches, it is processed. When the address doesn't match, the system ignores the packet.

### Tip

As a general rule, the larger a network is in terms of geographical distribution, the more likely it is to be a point-to-point network. A smaller network can more efficiently utilize broadcast technologies.

# Topologies

Another classification for computer networks is the topology that they use. A topology is the distribution or arrangement of network elements, usually both devices as well as connections. Because anything that can get an address is considered a network element, you can define a logical or virtual network element in software, and these two must be accommodated in any topological description.

A network may be described in terms of a physical topology, which describes the relationship between devices or elements; a logical topology, which describes a relationship or hierarchy between entities on the network; or a hybrid topology, which is a combination of the two into a single topological design. In very rare circumstances, a network may be described in terms of a signal topology. A logical topology might be mapped to indicate how the nodes of a network are arranged and communicate with each other. Physical topology would define the network in terms of the physical connections and the physical structure of the network. A signal topology might be constructed to show how specific types of signals move about the network. The physical and logical topologies may be identical, but they often are entirely different.

The mathematical study of linked systems is part of graph theory, and this discipline can make predictions as to the number of nodes required for different topologies, the number of links or fanouts, and so forth. The specific topology used by any network can be the same, regardless of the speed of the network, the protocols used to communicate, the network node, or the connection types. Topology only refers to the relative arrangement of the elements.

## Physical topologies

A physical topology describes the arrangement of devices used to implement the network. Topological devices can be either nodes or endpoints, or they can be connections or links. A physical topology can take many forms:

- **Buses**. Where nodes attach to a linear trunk line
- **Stars**. Where multiple nodes connect through a single node to one another
- **Rings**. Where nodes are connected to a cyclical trunk line
- **Meshes**. Where nodes are connected to other nodes directly (a web)
- **Trees**. Where the nodes in a network radiate outward like the branches of a tree

Many networks are combinations of these types.

It is possible to calculate the required number of connections that a theoretical mesh network would have when each node is connected to every other node. With a single-link, a permanent point-to-point mesh topology between nodes is both the simplest arrangement that exists and the most impractical. To service *n* endpoints would require 2(*n* + 1) connections, which for any large network would require an unsupportable infrastructure of permanent connections. Most point-to-point networks, like the telephone networks, are switched, eliminating the need to have point-to-point connections between every node. Switching can be done either in hardware through *circuit switching* or by altering the addressing within the data stream, which is referred to as *packet switching*.

Robert Metcalfe, who was one of the main developers of Ethernet technology, described the value of switched networks in terms of the number of users. Metcalfe's law states that the value of a telecommunication network is proportional to the square of the number of users in the network. The number of unique connections N in a point-to-point system is equal to

```
N = n(n-1)/2
```

where *n* is the number of nodes. As the number of nodes grows, it becomes asymptotically proportional to the curve for *n*2. An asymptote is an equation that approaches some function or value as one of its variables gets larger. In the example above when n becomes large the equation (*n*2-*n*)/2 would be dominated by *n*2 and that curve would be 1/2 the size of *n*2.

### Bus systems

A bus is a common transmission medium that connects to two or more network nodes called *endpoints*. An endpoint is equivalent to a node, and on a network it has the fundamental property that it is addressable; that is, it is assigned an address. A computer NIC can be a node or endpoint and so can a router. From a fundamental perspective, a port on a switch or router can also be an endpoint or node.

A backbone or trunk line is an example of a linear bus (see [Figure 1.2](ch01.html#a_linear_bus_system)) because all data travels from one endpoint to another over the bus line. In [Figure 1.2](ch01.html#a_linear_bus_system) the bus is defined as the collection of connections or links, and each circle is a network node or endpoint. Data traveling from one node on a bus to another starts off by traveling down the bus to the next node, where it announces its intended recipient. If that node isn't the recipient, then the signal continues down the bus until the intended recipient is reached. This behavior introduces a propagation delay, but in modern networks, these delays are small.

![A linear bus system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0102.png)

**Figure 1.2. A linear bus system**

All endpoints in a bus system (see [Figure 1.2](ch01.html#a_linear_bus_system)) require that they be logically differentiated from one another, and come with devices that perform this function, which are called *terminators*. Termination takes the signal and absorbs it so that it prevents data from continuing on down the bus. Termination is designed to match the impedance of the transmission line and is often a simple resistor. Some terminators are active devices that have an electrical circuit that eliminates the signal reflection.

A linear bus system that uses a backbone or trunk transmission line is an efficient technology, but is not very flexible. By flexible I mean that it's difficult to adapt a linear bus system to changes in the number of hosts, locations of hosts, and other changes that might take place. To improve the adaptability of a bus network, it is common to use a distributed bus technology. A distributed bus adds more branches to the transmission line so that it connects additional nodes. In nearly all respects, a distributed bus is similar in function to a linear bus. Nodes still require termination. A distributed bus is often confused with a tree topology, which is the kind of topology that a file system uses. However, in a distributed bus, there is no central node that connects to all the other nodes, and there is no hierarchy defined. [Figure 1.3](ch01.html#a_distributed_bus_structure) shows a distributed bus structure.

![A distributed bus structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0103.png)

**Figure 1.3. A distributed bus structure**

### Star networks

The star network is a very common network topology. In a star network, point-to-point connections radiate out from a central node, in an arrangement that is also called a hub and spoke, as shown in [Figure 1.4](ch01.html#a_star_or_hub-and-spoke_network). In a star network, all data traveling over the network must flow through the central node. The simplest star network is constructed using a single connection point such as a punch down block, or it can be an active connection that retransmits data, performing error correction first and then signal amplification. A punch down block, or more simply a punch block, is an electrical connection matrix with open ends on both sides that allow you to connect wires together by punching the wire into the holes in the matrix.

Star networks can be constructed so that the hub connects two or more star networks together, as is the case for both extended star and distributed star topologies. An extended star uses one or more repeaters in-line to extend the distance that the signal can be propagated from the hub to a spoke. When you replace a repeater in an extended star with a switch, you create a hybrid topology that is sometimes called a physical star topology. [Figures 1.5](ch01.html#an_extended_star_topology) and [1.6](ch01.html#a_distributed_star_topology) show examples of an extended star and a distributed star topology, respectively.

![A star or hub-and-spoke network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0104.png)

**Figure 1.4. A star or hub-and-spoke network**

![An extended star topology](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0105.png)

**Figure 1.5. An extended star topology**

![A distributed star topology](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0106.png)

**Figure 1.6. A distributed star topology**

A distributed star topology connects multiple star networks with a daisy chain in a linear fashion. The distributed star has no hierarchy and no central or primary connection from which a set of stacked hubs emerge. All of the star networks in a distributed star network are peers.

When star networks use a broadcast, they are referred to as *broadcast multi-access* networks, and the signal is sent to all of the spokes on the network. Some star networks use addressing to send signals from one node to another through the hub, and they are called *non-broadcast multi-access* (NBMA) networks.

### Rings

A ring network, shown in [Figure 1.7](ch01.html#a_ring_network), is a closed loop topology where each node in the network is both the beginning and endpoint of any data transmission. In a ring network, data travels in one direction around the ring from node to node until the receiving system accepts the data. The reason that data travels in one direction is to prevent signal contention and interference. Such interference leads to signaling errors. A dual ring topology provides the potential to transmit traffic in two directions (one on each ring), or to use the second ring as either a control circuit or a failover circuit for improved fault tolerance. A failover is the process that replaces a faulty component with another component.

![A ring network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0107.png)

**Figure 1.7. A ring network**

The most famous examples of a ring topology are token ring (IBM), ARCNET, token bus, and fiber distributed data interface (FDDI) networks. In a token ring, an identifier called a token is passed around the ring's nodes in sequence until the correct node has the token. The node with the token is the system that can actively work with the data that is circulating on the ring. Token ring networks are wired using a star or hub-and-spoke system, but each spoke has two connections to the hub that creates the ring. In an 802.5 Token Ring network, the central node or hub is referred to as a *multistation access unit*.

### Mesh networks

A mesh network is one in which each node in the network can be connected through a point-to-point connection to another node, as shown in [Figure 1.8](ch01.html#a_partially_connected_mesh_network). In this regard, mesh networks are an extension of the bus system described earlier. Mesh networks are described by Reed's law as having a value that is proportional to the exponent of the number of nodes,

```
2n-n-1
```

where *n* is the number of nodes. As a consequence, mesh networks exhibit what is called high fan-out. Their value grows exponentially greater than either the number of nodes, *n*, or the number of pair connections, *n*(*n*-1)/2, which was derived as Metcalfe's law.

![A partially connected mesh network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0108.png)

**Figure 1.8. A partially connected mesh network**

A mesh network can be either partially connected (as shown in [Figure 1.8](ch01.html#a_partially_connected_mesh_network)) or fully connected (as shown in [Figure 1.9](ch01.html#a_fully_connected_mesh_network)), depending on whether each node in the network is connected to each other node with a point-to-point link. You almost never find a fully connected mesh network except in small networking, because the number of links required to complete a mesh network tends to make them too costly to construct. In a partially connected mesh network, some nodes, and often most nodes, are connected to more than one node with a point-to-point link. The lack of unique connections introduces some latency into mesh networks, but this is something that can be managed through the use of intelligent routing, so that when the direct path isn't available, another route is chosen. An example of a partially connected mesh network is the Internet.

![A fully connected mesh network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0109.png)

**Figure 1.9. A fully connected mesh network**

### Trees or hierarchical networks

A tree network starts out with a highest level or root level, where a single node is connected to nodes in a second level of the hierarchy. Second-level nodes each connect to one or more nodes in the third level, and each level fans out further. There must be at least three levels in a hierarchy, as two levels define a star topology.

The number of connections in a tree topology may be calculated using the formula

```
L = n - 1
```

where *L* is the number of point-to-point links and *n* is the number of nodes.

The number of nodes attached to a parent is referred to as the *fan-out* or *branching factor*. Some networks impose symmetric branching, and if so, the branching factor (*f*) must be 2 or more, as a factor of 1 only defines a linear topology. Although this is called a tree network, its shape is usually drawn with the root at the top of the diagram, which means that the tree is upside down, as you can see in [Figure 1.10](ch01.html#a_tree_network).

Most file systems, databases, and directory systems adopt a hierarchical topology. This is because search algorithms are much more efficient in a hierarchy than in linear or mesh type topologies. This is especially the case when the values stored at any node are indexed. As a search algorithm descends the tree, moving to the next level below eliminates 1/*f* of the tree's population.

One disadvantage that is noted for hierarchical topologies is that any overhead associated with data transmission between levels is amplified as you move up the hierarchy. The nodes in each level above add to the overhead needed to process data communication.

![A tree network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0110.png)

**Figure 1.10. A tree network**

## Hybrid topologies

All of the aforementioned topologies may be combined with one another to form hybrid topologies, which provide more complexity, as well as more flexibility, into a single topological design. You can create the following topologies:

- **Star-bus**. A star-bus network connects two or more physical star networks along a single common network bus. In practice, this requires that a network line be terminated by two or more hubs, with each hub's uplink port connected to another hub that fans out to create the physical star. From the standpoint of the network, each of the uplink ports is connected to the star hub through the use of drop cables. As you learn in [Chapter 9](ch09.html), an uplink port is a port on a switch that can be set so that two connected switches behave as one.
- **Hierarchical star**. In a hierarchical star network, each node of the tree hierarchy is a hub from which spokes radiate. Each subsequent level in the hierarchy is a hub with spokes radiating out. There is no common bus that connects the different stars, with only point-to-point connections existing in this topology. Sometimes the root node is connected to a high-speed interconnect backbone or trunk line, which further hybridizes this technology.
- **Star-ring**. The star-ring hybrid consists of a central hub where the signals are routed sequentially between all available spokes attached to the hub to simulate the ring portion of the network. The spokes from the central hub are point-to-point connections to individual nodes.
- **Hybrid mesh**. A hybrid mesh combines a mesh topology, with one or more nodes of the mesh being connected to different network topologies. A hybrid mesh technology is highly redundant and fault tolerant, and so it finds widespread use. The Internet uses a partially connected hybrid mesh topology.

## Logical topologies

Logical topologies map out the path that data takes as it travels from node to node. A logical topology requires that a node be available on the network by the protocol used for data communications. To be available, a device has to have a unique identification number, referred to as a *MAC address*, which refers to Media Access Control, a method for determining that node on a network. Virtual network interfaces can be created, and they can also be assigned MAC addresses. When you use intelligent routers and switches on a network, the configuration of the logical topology can be dynamically changed, depending upon conditions. Logical daisy chain, logical star, and logical mesh are all types of logical topologies, and are described in the following sections.

### Logical daisy chain topology

A daisy chain network is a logical topology that can be implemented as either a linear or a ring topology, as shown in [Figures 1.11](ch01.html#linear_daisy_chain_network) and [1.12](ch01.html#a_ring_daisy_chain_network._data_can_flo), respectively. As you add systems to a linear daisy chain, you add a two-way connection between the new system and its neighbor or neighbors. A system in the middle of the chain must have one transmitter and one receiver for each of the connections to adjacent systems. The terminus system in the chain requires only one receiver and transmitter. In a daisy chain configured in a ring topology, the data travels around the ring in one direction, and so each node requires only a single receiver and transmitter. Ring topologies have greater latency because the data can take up to twice as long to get to its destination compared to a linear topology, but this makes them much cheaper to implement.

![Linear daisy chain network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0111.png)

**Figure 1.11. Linear daisy chain network**

![A ring daisy chain network. Data can flow either clockwise or counterclockwise, and links can be either half duplex (one direction) or full duplex (both directions).](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0112.png)

**Figure 1.12. A ring daisy chain network. Data can flow either clockwise or counterclockwise, and links can be either half duplex (one direction) or full duplex (both directions).**

### Logical star topology

Star networks exist as both physical and logical topologies. In a logical star Ethernet network, the central node broadcasts a signal from any node to all of the other nodes attached to the network. When the signal is acknowledged by the proper system, the data is transmitted. Logical star networks can fail spectacularly when the central node fails, but the failure of any point-to-point connection only affects the function of the node attached to that spoke.

Star networks can be categorized as either passive or active. In a passive star network, the sending node must be able to recognize its own signal echo returned to it from the central node. An active star network has circuitry in the central node to prevent a signal being echoed back to its originating system. Network switches are used in the various star topologies that build lookup tables of data transmission types, and the destinations and ports that were used to process them. As the lookup table becomes populated, the data that corresponds to the parameters stored in the lookup table serves as the routing table, and the data is sent to the stored destination directly.

If you create a set of logical star networks and connect them in a hierarchy, you create a tree topology. Hubs in a logical star network typically either repeat or regenerate data as it moves through the network, although networks of this design usually distribute the workload between the different hubs. Each node in the star has one point-to-point connection. So the logical star network has the entire leaf of the tree fail when a hub fails, but only the single node fails when the point-to-point connection is broken.

Logical star networks can also be configured in hybrid network forms. Two common hybrids are the star ring and the star bus network.

### Logical mesh topology

A logical mesh topology is one where there are additional paths between network node pairs. [Figure 1.13](ch01.html#a_grid_network_is_an_example_of_a_logica) shows an example of this kind of topology. There are several logical mesh designs. Highly distributed mesh networks built using a linear or ring topology are referred to as a *grid network*. Mesh networks can also be constructed using a toroidal or multi-ring topology, or using hypercubes.

As with physical mesh topologies, logical mesh topologies can be either fully connected or partially connected. Partially connected mesh networks are much more common than fully connected mesh networks due to the expense involved in creating the complete set of connections. Some fully connected mesh networks exist where highly redundant connections are required, typically in mission-critical applications. However, one fully connected *ad hoc* network that you might encounter is that used by the BitTorrent file sharing system. When a user initiates a torrent to perform a file transfer, pieces of the file are found on multiple systems. Those systems are temporarily connected while their pieces of the file are transmitted, and then the connection is broken.

![A grid network is an example of a logical mesh topology.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0113.png)

**Figure 1.13. A grid network is an example of a logical mesh topology.**

# Summary

In this chapter, you learned the different types of networks and how to classify them. Networks can be differentiated based on their geographical distribution as personal, local, wide, campus, or metropolitan local area networks. Each network type generally uses its own specially designed industry-standard protocol that is meant to optimize the network for the types of devices that are in use.

You can also characterize networks based on their shape or topology. Common topologies are buses or chains; stars or hub; and spokes, rings, and meshes. Various hybrid topologies exist that mix and match these topologies with one another. When you map a network, you can form the topology based on the arrangements of physical elements, or using logical elements, as well as by observing the paths that signals use to traverse the network.
