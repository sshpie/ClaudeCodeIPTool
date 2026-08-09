# Chapter 2. The Network Stack

**IN THIS CHAPTER**

- How standards are developed
- Introduction to standards organizations
- The Open Systems Interconnection Reference model
- How to use the network stack to understand products and services
- Each layer of the OSI model and their application
- Interfaces, services, and protocols
- Examples of where the OSI isn't an accurate description
- The TCP/IP Reference model
- Comparing the OSI and the TCP/IP Reference models

The network stack refers to an architectural model that is used to describe network transactions starting at one computer system and ending at another system. Models were developed to standardize devices and services, and to allow industry standards to evolve that allowed communications from one level of the network to another.

This chapter discusses the two most important network models in use today: the ISO's Open Systems Interconnection model and the Internet or TCP/IP model. Each model subdivides the different types of network devices, services, and software into a set of architectural layers, the definitions and relationships of which provide a means to categorize and discuss modern network technology. The vocabulary described in this chapter provides a means of framing the discussions in the remaining chapters in this book.

# Standard Development Organizations

As networking standards developed in the 1970s and 1980s, the computer industry was faced with the common problem of making vendors' products interoperate with each other. Operating systems vendors such as Microsoft were able to create a de facto standard like Windows; but computer network hardware and software had no such dominant vendor. Standards could only emerge by consensus from the joint work of industry and academic standards organizations. When a new technology such as Ethernet arrived, the packet-based network protocols that communicated over this new medium arose as a set of standards from groups of vendors.

Standards committees are typically formed by standards organizations that manage many groups of standards, or they can be created by an industry group that is organized for the sole purpose of standardizing one technology or a related set of technologies. An example of a standards organization is the American National Standards Institute, or ANSI.

In either case, the development of any standard requires a process, and the more open, the better. As a result, you will find that the standards process is organized around a set of stages, which include any of the following:

1. **Formation** of a group that represents the industry.
2. **Request for a proposal** (RFP) of a standard, draft of a proposed standard, or the receipt of a proposed standard for review.
3. **Request for comments** (RFC) on the proposed standard or standards from the community.
4. **Testing and modification** of the proposed standard. Plugfests are often organized to test interoperability. A plugfest is an industry meeting where product vendors test their hardware and software with other vendors' products in order to ensure compatibility and to establish new standards.
5. **Draft standards**, which are the proposed standards that have not yet been fully codified.
6. **Accepted standard**, which is the final version of a particular standard. A standard can develop over time through iteration, such as the 802.11*x* Wi-Fi standards, which include a, b, g, and n.

Considering the time and effort involved in creating standards, as well as the stakes involved in their commercialization, standards are prone to considerable controversy. Not all standards survive far beyond their introduction. Consider the effort that went into creating both the Betamax and VHS videotape standards, or more recently, HD DVD and Blu-ray, where the latter standard of each pair is the one that survived. The clout of the organization is important and can often override a superior technology.

In the networking industry, the following standards organizations are important:

- **American National Standards Institute (ANSI;** `www.ansi.org`**)**. ANSI is a non-profit organization that creates standards for products and services.
- **International Organization for Standardization (ISO;** `www.iso.org`**)**. ISO standards are found in various data communications fields, including the standards and model described in this chapter.
- **International Telecommunications Union-Telecommunications Group (ITU-T;** `www.itu.int`**); Radiocommunications Group (ITU-R); and Telecom Development (ITU-T)**. ISO is a member of the ITU. Each group develops communication standards.
- **Internet Engineering Task Force (IETF;** `www.ietf.org`**)**. IETF creates Internet standards and is part of a group of bodies that define the TCP/IP and Internet protocols.
- **Institute of Electrical and Electronics Engineers (IEEE;** `www.ieee.org`**)**. IEEE ("I triple E") is the main standards body for wire and radio communications.
- **Storage Networking Industry Association (SNIA;** `www.snia.org`**)**. SNIA defines storage network standards for fiber channel, high-speed Ethernet, iSCSI, and others.
- **World Wide Web Consortium (W3C;** `www.w3.org`**)**. W3C is the central standards body for the World Wide Web, and defines HTML and related standards, as well as protocols used by Web servers.

### Note

You can find an explanation of how standards organizations work, as well as a longer list of standards development organizations, or SDOs, at `http://en.wikipedia.org/wiki/Standards_organizations`.

# The OSI Reference Model

The most important networking model in use today is the ISO's Open Systems Interconnection (OSI) Reference model. This model divides network communications into seven different layers and highlights how each layer is used in the communication process. Each layer adds more information to data during the sending process, while using and removing that information during the receiving process. Documentation for the OSI model can be downloaded from the ITU-T under their X.200 series, from their Web site at `www.itu.int/rec/T-REC-X/en`.

The OSI model defines seven layers, using the numbers 1 to 7, in the following order: the Physical, Data Link, Network, Transport, Session, Presentation, and Application layers. The first four layers are hardware related, while the last three layers are essentially software.

The OSI model defines the following seven layers, as shown in [Table 2.1](ch02.html#the_osi_model_layers)

**Table 2.1. The OSI Model Layers**

| Layers | Traffic Type Supported | Function |
| --- | --- | --- |
| Application | Data | The Application layer manages the network connection between an application and the network. |
| Presentation | Data | In the Presentation layer, data is formatted into a form that can be processed at the receiving system. |
| Session | Data | The Session layer creates the unique connection between sending and receiving systems and ensures that the data was transferred correctly. |
| Transport | Segments or Datagrams | The Transport layer manages aspects of data transmission and reception. |
| Network | Packets | The Network layer controls the addressing used for data transmission. |
| Data Link | Frames | The Data Link layer manages hardware addresses. |
| Physical | Bits | The Physical layer defines the transmission medium, such as wire, radio, light beam, or some other transmission method. |

### Tip

Some common mnemonic devices are often used to remember the OSI model and the order of each layer. They are: All People Seem To Need Data Processing, or Please Do Not Take Sales-People's Advice.

It is very rare to find a network that uses these seven layers as the basis for its architecture. However, this is the most widely used model to describe different network devices and technologies.

An alternative model based on TCP/IP networking was developed that uses five different layers to describe packet switching networks (the TCP/IP Reference model). Most modern networks now use devices based on the TCP/IP Reference model, but it isn't as flexible in describing other network types. The TCP/IP Reference model is discussed later in this chapter.

# How Layers Communicate

All communication between two systems requires that the data being transferred travel down though the sending system's network stack, across the Physical layer, and then up through the receiving system's network stack. While the protocols used within a layer must be identical for peer devices, the protocols used at layer interfaces are undefined and can be changed.

Communication begins at the Application layer on the sending system with a command or perhaps some other kind of event. That event is interpreted into an Input/Output, or I/O, request (that either sends or seeks information from a device), and translated to data that is transmitted down through the different layers of the network stack to the Physical layer for transport. Data travels over the link at the Physical layer using the specific connection that leads back up the intended system's network stack. The data then ascends the different layers of the target system's network stack to arrive at the receiver's Application layer where the data is used in some way.

In order for data to be sent to the correct system or systems, additional information must be added to the data that describes the content and how to use it. That kind of information is commonly referred to as *metadata*, which is literally "data about data." The process by which metadata is added is referred to as *encapsulation*; when the metadata is removed, the process is referred to as *decapsulation*. As data passes down through the network stack, metadata is added; as that data ascends, the network stack metadata is removed.

Referring to [Figure 2.1](ch02.html#osi_data_encapsulation_and_transport), you can see that the encapsulation process begins by formatting and segmenting data so that it is the optimum size for transmission. Each layer of the OSI model adds a layer header to the data containing the information necessary to support the functionality of that particular layer's protocols. Application (L7H), Presentation (L6H), Session (L5H), Transport (L4H), Network (L3H), and Data Link layer (L2H) headers are successively added. Each header contains addressing information, parameters, and the instructions on how the different layers use the information encapsulated within. A trailing section is added to the packet at the Data Link layer, which identifies the end of the packet. This trailing section also includes a data check so that the transport of the packet over the physical layer can be verified as being correct. At the receiving system, the packet is read and each OSI layer of the receiving system strips away its particular header exposing the information contained within successively.

An algorithm such as a Cyclic Redundancy Check, or CRC, is applied to the data. This algorithm is run when a packet arrives at a destination (even an intermediate destination) to determine that the packet was correctly transmitted. If the calculated CRC value of the packet matches the value in the CRC data field, then the packet is assumed to be correctly received. A data check is done in the Data Link layer, but other layers may also include data check fields. The CRC is a hash function, and an algorithm is applied to the data contained in the communication to create an output value that is essentially unique, typically in the form of a 32-bit integer. The CRC is then used as a checksum to validate that the data sent matches the checksum contained within the data itself. The change of even a single digit in the data is enough to affect the value of the checksum and to require a retransmission of the data. Because data is binary, the CRC algorithm is very fast and efficient and doesn't add much overhead to the data transmission process. CRC-32 is now an Ethernet standard, and without this type of technology, network communications would be unreliable.

![OSI data encapsulation and transport](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0201.png)

**Figure 2.1. OSI data encapsulation and transport**

Seven layers are defined in the OSI model, each with its specific purpose representing a different area of networking technology. If only life were so simple. It is unlikely that you will ever work with a network comprised of seven different layers that correspond to each of these different areas; although rare, they do exist. However, economies of scale, as well as convenience provided by different packaging, costs, and other factors, lead to devices that might span two or more layers, and you should be aware that there are several other networking models that use fewer layers to define the network stack. Five layers is a common alternative.

### Tip

To get an idea how people subdivide the network stack, refer to the layer names table found at `http://en.wikipedia.org/wiki/Internet_Protocol_Suite`.

In practice, network devices and protocols will work at multiple layers in any networking model. The Cisco router is a good example of an appliance spanning multiple layers of the OSI model. Although the first routers were software that was built into operating systems such as UNIX or Solaris, Cisco achieved dominance in this area of technology by turning routing into an appliance, and by optimizing its performance. Cisco routers span both the Transport and the Network layers. However, the model still serves as the means for describing network communication and identifying devices, and it is the basis for a number of other models used to define Internet traffic, storage area networks (SANs), and more.

It's best not to take the OSI model too literally. However, it provides the vocabulary needed to frame different vendors' products, which is why it is so useful. The real value of the OSI model is that it provides you with an understanding of how components communicate with one another. Each layer in the model describes a protocol or set of protocols, and so the model is sometimes referred to as a *protocol hierarchy*. Each boundary between two levels represents a vertical relationship and requires that an application programming interface, or API, be used in order to communicate with the levels above and below it. A vertical relationship between layers 4 and 5 would be referred to as the Layer 4/5 interface. Implicit in the use of the word *interface* is the need for a communication mechanism based on an API.

Horizontal relationships, referred to as *Layer* n*protocols*, are considered to be peer layer communication, and often don't impose an API requirement. Horizontal relationships are only truly peers when two different entities on the same computer system use that same level: two mail applications, for example. When the same protocol layer is used by devices or entities on different computer systems, their relationship may be termed a peer relationship, but any communication between the two requires that both network stacks be traversed.

As data travels through the network stack, it does so across the boundaries in a set of named connections or channels. Some technologies use a single pipe, similar to a one-lane road, through which data travels in one direction only; this is *simplex* communication. You can also use a single connection to send traffic first in one direction and then in the reverse direction; this is referred to as *half-duplex* communication. When communications travel in both directions at the same time, this is referred to as *full duplex*. Full duplex can be achieved by having a channel that is wide enough to dedicate to each direction or by having multiple channels. The type of communication used is determined by the hardware and software involved and is not specified as part of the OSI model.

Each layer in the OSI model has one or more active elements that are sometimes referred to as an *entity*. An entity can be a software module or it can be dedicated logic on a chip that is part of a network function. An entity or set of entities in a layer that communicates to the layer above is referred to as a *service provider*, and the entity that uses the service in the layer above is the *service user*. The address that is used to access a service provider defines a Service Access Point, or SAP. Once two entities establish communications through an interface using an SAP, they pass what is called an interface data unit (IDU) through the SAP. Contained within the IDU is a service data unit (SDU), control information, and the data that is communicated.

Some layers require that the data be segmented in order to be processed. When that happens, each piece of data gets a header and is transmitted as a distinct unit of data called a protocol data unit (PDU). An example of PDUs is the packetization of data for transmission, and the reassembly of those packets once they are received, verified, and sequenced.

Services are the mechanism used to communicate between different layers in the OSI model. Services have a certain functionality and often can be accessed using an API. Services can operate between layers in either a connection or connectionless model. A connection model specifies that once your connection is established, that connection is dedicated to the service being provided. The best example of a connection-oriented service is the telephone network. The service establishes a connection by dedicating a circuit to the communications. When the call ends, the circuit is broken and released for use. A connection model offers some advantages in terms of reliability and in providing quality of service. However, once the connection is broken, the communication ends, which demonstrates the weakness of this approach: it is not fault tolerant or redundant.

The alternate model of a connectionless service is adopted by the Internet at the Physical layer and is accounted for by the TCP/IP or Internet model. The communication carries its own addressing, and the route taken to reach its destination is unspecified and can be different, depending upon conditions. Connectionless services are characterized by high fault tolerance, but with slower performance and some additional overhead as compared to a connection-oriented service model.

All data communication is characterized by the use of basic commands to initiate and control the connection. Connection-oriented services begin with a process called *negotiation*, where the characteristics of the connection are established. The squelches your modem makes with dial-up connections when it connects are its advertisement of its connection capabilities. Basic control commands or service primitives that play a role in the negotiation process take the following forms:

- **Initiation or connect request**. This is the advertisement for a service to perform an action.
- **Status or indication**. This is an informational event that provides information about the state of the software module or active element (entity) involved in providing the service.
- **Response**. The provider sends a message that it can respond to a request.
- **Confirmation**. The result of the communication is sent back to the initiating entity. Not all services use a confirmation as part of their service.

Keep in mind that the negotiation process takes place on two different systems. Therefore, although the negotiation involves the interface between two different layers in the network model, each control command travels either up or down between the two layers on one system and is then responded to in those same two layers on the second system. A service is defined by the set of operations or command primitives, as well as the two layers that are interfaced by it.

Services do not specify how the operations are implemented in practice. Implementation using services is left to specific protocols. A protocol is an agreed-upon set of rules for data format that can be used by peer entities within a layer to provide a service. By isolating the command set from the implementation, a network is able to switch protocols to accommodate different vendors' products, different network types, and other variables that affect performance.

# The Physical Layer

The Physical layer is the lowest level of the OSI model and in other related architectural models, and is the layer responsible for moving bits of data from one location to another. In defining the parameters of Physical layer devices, it is necessary to set the standards for what represents a Boolean value of 1 and 0, the voltage difference, and how long the bit should last before a new bit begins. Physical layer devices must include the electrical connections that are made, how different devices connect to one another, and other electrical and mechanical aspects.

The most commonly used media for the Physical layers are:

- Copper cabling or wires, which include different categories of Ethernet cable (designated by specifications such as CAT5 or CAT6), twisted pair wiring like the ones used in your phone lines or that were used for smaller peer networks such as AppleTalk from Apple, and others.
- Fiber lines where light travels through doped glass strands.
- Radio communications using the different Wi-Fi 802.11 standards, microwave, and other parts of the electromagnetic spectrum in the radio range.

The Physical layer also includes the devices that provide the connections between media, and includes computer network interface cards (NICs), modems, hubs, and other devices.

# The Data Link Layer

The Data Link layer connects the data in bits flowing through the media of the Physical layer with the connection that is the network path either to the receiving system or from the sending system. It provides the control mechanism that determines which path the data takes. As is the case with the Physical layer, the Data Link layer appears not only in the OSI networking model but also in other related models such as the model used to describe Internet traffic.

The control over the data link requires that this conceptual layer of the networking model format messages to mark the beginning and end of a message. It does so by breaking the data into data frames, or more simply, frames. A frame takes a large message and segments it into pieces that are between several hundred and several thousand bytes in size. The size of the frame depends upon the technology being used and can be adjusted somewhat by the user to improve performance and reliability. You might want to have a larger frame size when you are transmitting your data over a high-speed connection, or perhaps drop down to a small frame size when a low-speed or unreliable connection is in use.

The segmentation process for frames imposes a sequence on the transmission, and the Data Link layer must provide the necessary means to recombine the frames into data at its destination. Because data can be damaged by noise, and because multiple frames may arrive that duplicate each other, it is up to this layer of the model to resolve these problems. The Data Link layer does so by returning Acknowledgment frames to the sender to indicate which frames were received. The mechanism by which errors can be detected and corrected is part of the Data Link layer's action. Data can be corrupted for many different reasons, including noise in the physical media, and mistakes in transmission or dropped data. When an error is detected at the Data Link layer, a message is sent to the sender that the data needs to be retransmitted.

Part of the Data Link layer's function is to manage the speed of data transmission: too fast and data is lost, which requires that data be retransmitted; too slow and the communication wastes valuable bandwidth and isn't well optimized. The system by which the Data Link layer regulates the data transmission speed involves the use of frame buffers to store data as it is received. A frame buffer is a portion of memory set aside to contain frames that have been received recently. Data flowing into and out of the frame buffers requires flow regulation and error correction in order to be both efficient and well formed. Therefore, the Acknowledgment frames must contain current information about the state of the frame buffer. Because Acknowledgment frames travel over the same physical path as Data frames, one optimization that the Data Link layer uses is a piggyback scheme to send control data back to the sending system. In any broadcasting network communications, such as TCP/IP traffic flowing over Ethernet, the Data Link layer provides a control function in the medium access sublayer of the Data Link layer that determines which frames have access to shared data channels. A shared data channel is a network path that is used by two or more sending and receiving systems.

# The Network Layer

The Network layer provides a routing and control function that determines which path data packets use to travel from one network to another, and provides the flow control needed to ensure that a subnet isn't flooded with too many packets at any one time. The concept used to define Network layer communication is called the *session*, and the logic used to manage sessions relies on specific routes determined by the routing function.

Routing plays a fundamental role in switched networks because it provides the means by which traffic can adjust to dynamic changes in the network. When a router fails an acknowledgment request from a sending router, the router can fall back to the next best path. Routers store connections and routes in a routing table, which can either be statically or dynamically created. For small networks where the addresses rarely change, or for large networks where high-speed connections at well-known addresses exist, static routing tables make the most sense. For large networks, dynamic routing provides a better solution than static routing.

Different networks or subnets can require data to be formatted in different ways. This commonly occurs when data travels across international boundaries. Addresses can change across a boundary, and so too can the data rate or the protocol used for the transmission. Some subnets require packets to arrive with information that supports an accounting function to keep track of frames forwarded by subnet intermediate systems, to produce billing information. The network layer provides the necessary means to solve these incompatibilities.

Both the OSI model and the Internet model contain a Network layer. However, when network traffic is broadcast, it is sent out to any network system that requests the data. Broadcast data doesn't require most of the functions provided by the Network layer. Therefore, for broadcasting systems, the Network layer can be either minimal or completely missing.

# The Transport Layer

The Transport layer connects the Network layer above it and the Session layer below. The purpose of the Transport layer is to segment the data from a session and pass appropriately sized and formatted data to the Network layer. When data is received from the Network layer, the Transport layer is responsible for ensuring that all the packets have arrived correctly, reforming the session data, and acknowledging (an ACK command) the receipt of the transmission. The Transport layer can support either connection or connectionless data transmission.

The Transport layer manages the connection between its two adjacent layers — the Session layer and the Network layer — and when appropriate, it can create and manage multiple network connections for each Transport connection. Because the Transport layer is responsible for maintaining and managing the connection between the Session and the Network layers, it abstracts the upper layers of the network stack, which are software-based, from the hardware layers below it. As data is exchanged, the Transport layer is responsible for managing the multiplexed streams, and opening and closing connections as required. This management function is a form of flow control.

Transport layer connections provide the only direct link that exists between the two network stacks during any communication. Whereas all other layers of the network stack work independently of their counterparts in the other network stack, the Transport layers of the sending and receiving systems talk directly to one another through the use of their message headers and control messages. A message header is a special field within a packet that contains message information, while a control message is an entire packet (usually a very short one) that is a message. Indeed, the hardware layers can only establish a connection between adjacent layers because the systems involved in the connections between the Network, Data Link, and Physical layers are indeterminate. Depending upon network conditions, routing may employ any number of systems to make the connections required by hardware. The higher layers in the network stack — the Application, Presentation, and Session layers — are all single-channel, end-to-end communications.

# The Session Layer

The Session layer provides the means for creating and managing sessions, as well as providing the services needed to initiate those sessions. Security mechanisms, such as logons and other forms of dialog control, are a fundamental part of the Session layer.

Traffic can flow through the Session layer in one direction at a time, or in both directions: either using a half-duplex or full-duplex mode. When a single direction is used (half duplex), the Session layer passes an identifier called a token to the traffic in one direction when its turn comes to use the channel, and then when the token is released, it is passed to the communication going in the opposite direction.

As data flows through the Session layer, checkpoints or separation markers are inserted into the packet data so that if the transfer is interrupted, it can be reestablished without having to resend all of the session data. By synchronizing the data transfer, the Session layer ensures not only that the session is reliably transmitted but also that the transfer is efficient.

# The Presentation Layer

The Presentation layer formats Application layer data and can compress and encrypt data before handing the data off to the Session layer. When data from the Session layer appears at the Presentation layer, it is decrypted and decompressed if necessary, so that the data can be sent to the Application layer in a form that the Application layer can accept.

Presentation layer software takes the data objects that applications create in the different data types, such as character, integer, or binary, and converts that data into a form that can be passed along to a different system in a standard encoding format. Wire protocols bridge operating system and application differences so that a computer with one character code, such as ASCII, can communicate with another computer that has a different ASCII character set, or that is using Unicode as its character set.

# The Application Layer

The Application layer contains the software that a user interacts with. Application layer programs include Web browsers, e-mail clients, command shells (the Command Line Interface), and office applications to name but a few. The network operating system also contains a number of Application layer programs. Not all software is Application layer software. Microsoft Word, for example, is not exclusively an Application layer application; it contains many modules that work at different layers of the network model and many modules that aren't network related. However, when you initiate a command to perform network printing, the print subsystem used to communicate this action to the network is an Application layer application.

Application layer software is often described in terms of terminal session. A terminal session is an application that provides system status information, allows for system commands, and serves as an interface for user interaction to a system. When you open a terminal session and log into a remote system, you are using an Application layer program. In order for a terminal session to interact with a wide variety of programs, there must be a uniform way for those programs to communicate with the terminal session. Many terminal session programs use a network virtual terminal to standardize the interaction between applications such as text editors with all of the different terminals that exist so that variables such as screen resolution and keyboard equivalents are standardized.

The Application layer hosts a very rich range of services, and the particular services are highly variable from system to system. Applications are responsible for many application service functions, including the following:

- Display characteristics
- Initiating and managing I/O (Input/Output)
- File transfers
- E-mail
- Network printing
- Information lookups in directory services

The Application layer uses the largest set of network protocols. The Hypertext Transfer Protocol (HTTP) used by Web servers and browsers, File Transfer Protocol (FTP) used in uploads and downloads, Simple Mail Transfer Protocol (SMTP), and the Post Office Protocol (POP) used for e-mail transfers are all Application layer protocols.

# The TCP/IP Reference Model

Although the OSI Reference model is the best known, it is not the only layered network stack model in use. The best-known alternative model is called the TCP/IP model.

### Note

The TCP/IP model is discussed in more detail in [Chapter 18](ch18.html).

The TCP/IP model uses three different protocols for transport and data format. The Transmission Control Protocol (TCP) describes how to make connections between systems on the Internet, while the User Datagram Protocol (UDP) describes how to work with connectionless data communication. The third protocol, the Internet Protocol (IP), describes how to format packets for transmission. TCP and UDP are Transport layer protocols, while IP is a Network/Interface layer protocol.

The TCP/IP Reference model uses four different layers in its communication model. Layers 1 and 2 in the OSI model (Physical and Data Link) correspond roughly to the Host-to-Network layer in the TCP/IP model. Layer 3, the Network layer in the OSI model, corresponds directly to the Internet layer in the TCP/IP model; Layer 4, the Transport layer, exists at the same level in both. The TCP/IP model does away with Layers 5 and 6 (Session and Presentation). Finally, both models have a top-level Application layer, which was Layer 7 in the OSI model. [Figure 2.2](ch02.html#comparing_the_osi_and_tcp_solidus_ip_net) shows the OSI and TCP/IP models side by side.

![Comparing the OSI and TCP/IP network models](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0202.png)

**Figure 2.2. Comparing the OSI and TCP/IP network models**

# Comparing the OSI and TCP/IP Reference Models

Over the years, both the OSI and TCP/IP Reference models have shaped the vocabulary of the networking industry. However, they both contain flaws in their application to real-world networks that are important to understand. Whereas the TCP/IP model has expression in real products and technologies, based on a set of protocols that have become dominant standards, the OSI model is not supported by products to any significant extent. As a result, the OSI model is essentially an abstraction that is used to understand network communications.

Even in networks that adopt the OSI 7-layered model, some of the layers, particularly the Session and Presentation layers, are thinly populated, if at all. At the same time, the hardware layers, such as the Data Link and Network layers, have so many functions and services that any serious analysis of them would tend to segment those layers into several sublayers.

Part of the complexity of the OSI model is that it doesn't implement key technology in a single layer, but distributes command and control features such as flow control in each of the different layers. This redundancy makes the OSI Reference model more complex than it should be. In the real world, devices get around these issues by spanning several layers of the OSI model within the same device.

The main reason that the OSI model seems to have been adopted with seven layers is that the Systems Network Architecture (SNA) from IBM was a seven-layer architecture. In the 1970s, it was supposed that IBM could control the networking industry, and so the OSI model was constructed in a way that it could be applied to SNA technology without too many modifications.

While the TCP/IP Reference model is supported by a large number of products in the marketplace, it has been criticized for not being general enough to be applied to networks using other protocols. The delineation of interfaces, services, and how protocols are integrated into the model isn't clearly defined. For example, the Host-to-Network layer doesn't really implement separate protocols, and is more properly defined as an interface; there is also no formal Presentation or Session layer. This has generally been expressed in practice by the development of ad hoc protocol standards.

It's best not to take these network models too seriously. While OSI provides a highly flexible model that is widely used in theoretical discussion, and the TCP/IP model finds expression in products, neither model can be directly applied to real-world networks.

### Note

Perhaps the best compromise is one of the alternative formulations considered but not adopted when the OSI model was being developed that uses a five-layer system. These unnamed models eliminate the Session and Presentation layers in the OSI Reference model and blend their functions into the Application and Transport layers. Hybrid models left the Network, Data Link, and Physical layers intact.

# Summary

In this chapter, the OSI Reference model was presented as an architectural framework that can be used to describe computer networks and devices. This seven-layer protocol conceptualizes a network stack, beginning with applications and software at the top, formatting and data-handling layers in the middle, and hardware layers at the bottom. To communicate, data must travel from the sending system's network stack to the receiving system's network stack.

The boundary between each layer of a network model defines an interface that requires an API be used to create a service that connects the two layers. The OSI Reference model doesn't specify the interface or the service, but highlights its need and use.

Other architectures exist, including one based on the TCP/IP protocols. Whereas the TCP/IP model is expressed by more networks and devices, the OSI Reference model is more flexible and is more commonly used to describe aspects of computer networking. Hybrid models exist that use fewer layers than the OSI Reference model and reduce the OSI Reference model's complexity somewhat.
