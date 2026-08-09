# Chapter 4. Network Discovery and Mapping

**IN THIS CHAPTER**

- The methods used to browse networks
- The properties of connections are described
- How SNMP is used to manage network devices
- Network mapping

*Network discovery* is the way systems and devices are located on a network. There are various mechanisms that are used to enumerate devices, including node advertisement or broadcasting, browse lists, polling, and direct connections. Many times, combinations of these approaches are used. These different approaches are protocol independent, although many protocols are developed with a particular method of discovery in mind.

Network discovery uses a separate set of processes and protocols from name resolution. In order to be useful, both must work properly on a network. The methods used to look up names on a network are described. They include checking the `HOSTS` file; doing a DNS lookup; checking the NetBIOS name cache, WINS servers, and ARP broadcasts; and checking the `LMHOSTS` file.

A network connection is a defined path with two endpoints. Different types of network connections can be defined. Paths (or circuits) and endpoints can be either physical or virtual devices. A private circuit or channel can also be defined that is the basis for virtual private networks. Connections can be either stateful or stateless. A *stateful* connection retains the definition of a connection during and sometimes between sessions. *Stateless* connections are used when the path isn't defined.

Simple Network Management Protocol, or SNMP, is the Internet Protocol used to provide rich information about managed network devices. It works with local agents on managed nodes and stores data in a database with a standard structure. SNMP can be used to map networks and to send commands to and change the configuration of systems and devices.

*Mapping* is a process by which discovered network elements are graphically displayed in relationship to one another. Discovery creates a populated database of network objects: devices that are endpoints, wires that are network paths, and other elements. Discovery then establishes how different objects are connected. Mapping relies on the discovery process to establish the current condition of the network. Because networks change and different objects may appear or disappear over time, the state of any network map is often necessarily incomplete.

# Network Discovery

Network discovery is a set of processes by which one system or device finds other network systems and devices. Discovery can take the form of advertising network elements using a broadcast message, by collecting and distributing a list of network elements through browsing, by polling which uses a broadcast request/response mechanism, and also by directly communicating between different nodes or systems. All of these mechanisms are used, and each mechanism has different characteristics that make it useful in different circumstances.

Network devices advertise themselves as being attached to the network, or when asked by another device to respond to a discovery request, as shown in [Figure 4.1](ch04.html#network_discovery_using_a_broadcast_adve).

The simplest form of network discovery is through a broadcast message that advertises the availability of a network element. In this scenario shown in [Figure 4.1](ch04.html#network_discovery_using_a_broadcast_adve), node A initiates a broadcast after initializing its network interface. The workstation labeled A in the figure appears on the network and sends out a short message indicating that the system is now up and giving the system's interface address. Systems that receive the broadcast from node A add that node to their network list.

An example of a protocol that uses network advertisement would be the Bootstrap Protocol (BOOTP), where an advertisement is sent to obtain a dynamic IP address. In a broadcast advertisement system, the message indicating the system's availability is added to routing tables on a router, and to individual systems. Broadcast advertisement is a reasonable mechanism for obtaining information from a single system, such as a DHCP server, on small networks and for workgroups; but on medium and large networks, a broadcast mechanism is a very inefficient method for network discovery.

Because assigned friendly names change over time, broadcasts do not usually provide a system's friendly name. Networks rely on name resolution services to translate a network address into a friendly name. Examples of name resolution services are the Domain Naming Service (DNS), NetBEUI, NFS, and others.

Network discovery is most often the result of an Application layer event, such as opening a Network folder or a Get (Open) or Put (Save) dialog box that requires the network be displayed. What happens next is a function of the particular applications, the protocols in use, and the operating system.

![Network discovery using a broadcast advertisement mechanism](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0401.png)

**Figure 4.1. Network discovery using a broadcast advertisement mechanism**

A more efficient mechanism is to create a list of network elements that is dynamically updated. That list is often called a *Browse list* because when a system initiates a network discovery, the list is used to populate the network in the application. The system that manages the Browse list is called the *Browse Master*, and different NOSs and protocols handle this process in different ways. In workgroups, the Browse master is based on an election; in domains, the Browse master may be a domain server. In any event, a browse operation finds the Browse Master and requests the Browse list in order to store a local copy. Browse lists usually have an expiration period after which a system will attempt to refresh its local copy. A browse mechanism will sometimes be missing systems that have appeared on the network recently or show systems that are unavailable, but the mechanism has the advantage of greatly reducing network traffic compared to a broadcast mechanism and is a fast process.

[Figure 4.2](ch04.html#network_discovery_using_a_browse_mechani) shows a browse operation. A network window is opened on B which causes a browse request to be issued. That request finds the Browse Master, which returns the current Browse list. The Browse list is then used to populate the network window. Notice that nodes A, C, and D do not need to be involved in a Browse operation.

![Network discovery using a browse mechanism](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0402.png)

**Figure 4.2. Network discovery using a browse mechanism**

Another broadcast mechanism is called *polling*. In polling, as shown in [Figure 4.3](ch04.html#network_discovery_using_polling_or_direc), a node broadcasts a message requesting that other network elements respond and make themselves known. As responses come back, the responses of the network elements are used to populate the network list. A common use of a polling mechanism is in the area of router discovery where a router builds it routing table or Routing Information Base (RIB) through this mechanism. Polling has all of the disadvantages of any broadcast mechanism and is a slow process.

![Network discovery using polling or direct communication mechanisms](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0403.png)

**Figure 4.3. Network discovery using polling or direct communication mechanisms**

The last of the discovery mechanism involves enumeration of network elements through direct communication. If a node maintains a list of network elements, it can use a direct communication to talk with nodes that it knows about and get those nodes to tell it about nodes that they know about, and so on. A direct communication method coupled with polling is the preferred method for discovery in routers today.

Network discovery is ubiquitous, and it's built into all networked devices at a fundamental level. Network Interface Cards (Network Adapters or NICs), routers, switches, and even printers all store what is called a Media Access Control (MAC) address in their firmware. A MAC address is unique and is assigned by the manufacturer during the manufacturing process. Two identical MAC addresses represent a fundamental network error.

### Note

Although MAC addresses are unique, they can be spoofed. Spoofing incorrectly identifies the MAC address in communicated data and is an attempt to disguise the true origin of the sender. MAC addresses can sometimes be changed in software.

Notice that so far, I've made no mention of any particular technology used to implement the processes described in this list. Most books tell you that some networks use the Small Message Block, or SMB, protocol for browsing, or that they use NetBIOS over TCP/IP (NBT) for name resolution, or that they use the Address Resolution Protocol (ARP) to broadcast over IP networks; and, indeed, later chapters in this book will say the same thing. You might not remember those TLAs (three-letter acronyms), but chances are you can remember the general principles in this chapter. As a group, discovery technologies tend to be treated in a fragmented manner by many networking books, often as almost an afterthought. However, network discovery is fundamental to every modern network's function and needs to be grasped on a conceptual level.

It's important to understand that while there are many different network protocols in use for the network discovery functions just described, it is the functionality that drives the protocols and not the other way around. All modern network operating software, management software, and just about any application or utility you use relies on discovery to perform the services and functions that the software provides. You can't open a `GET` (Open command) or a `PUT` (Save or Save As command) operating system dialog box that involves an external device without initiating a discovery operation.

Some discovery services can be very rich, indeed. A rich discovery service not only advertises the existence of devices, but it also passes a set of attributes from the responding device. Rich discovery services give, at a minimum, the device status and may contain a listing of hundreds of attributes that you can query, or these services may provide a command and control function that can reconfigure devices. Some discovery services can automatically map networks — even complex networks with tens of thousands of network nodes — which is an amazing process to behold. Mapping is used for asset management, network optimization, and a truly varied range of capabilities that make modern networks practicable.

The most widely used rich discovery method is the Simple Network Management Protocol (SNMP), which is described in more detail later in this chapter. The Windows Management Interface (WMI) is another technology that extends the Windows driver model to provide device characteristics on Windows networks. Both store device information in a database format: a Management Information Base (MIB) file for SNMP devices, and a Common Information Model (CIM) repository. A technology called Web-Based Enterprise Management (WBEM), and pronounced "Web-em," is related to CIM and is yet another systems management function that is briefly mentioned later in this chapter. All these technologies are based on the Common Information Model.

Network management systems rely on these technologies for their operation. Any device that can be managed in network software is discoverable; the denial of discovery is the basis for many security devices such as firewalls. Network management tools can make difficult tasks easy, such as automatically deploying an operating system to many systems on a network, or complying with Byzantine licensing regulations scattered over a diverse collection of hardware.

## Node advertisement

In node advertisement, a system or device wants to establish that it is available to provide a service, and so it broadcasts its availability, as shown in [Figure 4.1](ch04.html#network_discovery_using_a_broadcast_adve). Some broadcast methods request a response when they reach their target system, or when the first located system that meets the criteria of the broadcast replies. In this section, you learn about some of these broadcast discovery protocols.

There are four common broadcast services that use this type of approach on current networks:

- Dynamic Host Configuration Protocol (DHCP)
- Bootstrap Protocol (BOOTP)
- Routing table updates
- Simple Network Management Protocol (SNMP)

### Note

Routing is described in [Chapter 10](ch10.html), and ARP is covered in [Chapter 19](ch19.html).

DHCP is the method used for dynamic IP assignments on networks. DHCP is a required broadcast service because it needs to be found by any system that requires a dynamic address assignment, when that system requests a dynamic address. Similarly, the BOOTP protocol is used to advertise for systems that haven't yet loaded their operating systems and need to obtain an IP address from a pool that the BOOTP server maintains. The BOOTP protocol is used to push an operating system image down to a bare metal computer (one that has no software), or to boot a thin client that has no hard drive and runs its software on a terminal server.

All of the common routing protocols use a broadcast technology to update their routing tables on the network. These protocols include the following: the Routing Information Protocol (RIP), which is used in UNIX systems such as BSD (Berkeley Software Distribution) in the routed daemon; Open Shortest Path First (OSPF); the External Gateway Protocol (EGP); and the Border Gateway Protocol (BGP). RIP is referred to as an Interior Gateway Protocol (IGP) and uses a distance vector routing algorithm for updates that time out after a certain number of seconds. OSPF is the most commonly used IGP on large networks. Of the two Exterior Gateway Protocols (EGP) used today on the Internet, the most commonly used is BGP, which uses a broadcast discovery technology.

### Note

Routers are described more fully in [Chapter 9](ch09.html).

SNMP is covered later in this chapter.

## Browsing

When you open a Network folder to view connected systems, you are performing a browse operation. The fact that the result is so simple — items show up in the window — is the result of many different processes that are going on. It includes actions that have previously occurred, and actions that your system and the network take, based on your browse request. [Figure 4.4](ch04.html#a_browse_operation) shows a browse sequence. The sequence for actions would start with the opening of a network window on system B. If a current Browse list is cached locally, then that is used to populate the Network window. If not, a Browser request may be made using a protocol such as NetBEUI to the Browse Master and the Browse list is obtained from that system.

![A browse operation](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0404.png)

**Figure 4.4. A browse operation**

A network browse command can rely on the following preexisting network characteristics:

- Systems and devices that have already registered themselves on the network, are on the Browse list found on the Browse Master.
- The router maintains a router table containing other routers and known addresses.
- Systems and devices have announced their presence on the network to the Browse Master when they are polled, updating the lists.
- Clients that have previously queried the Browse Master may cache the list of machine names for later use.

Depending upon the system used, a browse list can take a long time to populate. The refresh interval is something that can often be modified, either as a Registry entry in Windows or as a preference in the Browse Master software, such as `nmdb` on a Samba server. A Browse Master is a network service running on a system that maintains a master list of network elements.

Different operating systems and software can replicate the Browse Master across a set of systems to improve performance, add fault tolerance, and work with different protocols. You may find that a browse system contains not only a Browse Master but also a Domain Master, Local Master, Preferred Master, or some other type of system list management server. The Browse Master does not need to be a domain server. In a workgroup, it can be any system. Some applications also have this capability; on a Samba file server, for example, you can elect to have that system be the Browse Master. A domain server is a system that maintains the security database for member systems of a network domain.

The browse command can initiate the following actions:

- Go to the local name cache to start the browse process, and partially populate the browse operation if the system has been started and is running for a while. Keep in mind that the browse list can take up to an hour to populate accurately.
- Go out to the Browse Master and obtain the browse list stored on that system.
- Send out a request for available systems (polling is discussed in the following section).

The discovery of network systems and devices is only half of the problem; many services and protocols must match a network address to an assigned or friendly name. When a system wants to communicate with another system or device, it requires a network address; only a few services can work with machine names directly. That address is determined as a lookup operation in a table maintained by a service that is queried as part of the name resolution process.

### Note

[Chapter 19](ch19.html) covers the different technologies used to determine addresses on TCP/IP networks.

A lookup operation may include any of the following steps and is performed in the order listed below:

1. Look up the system name in the `HOSTS` file.
2. Perform a DNS lookup.
3. Check the `NetBIOS` name cache (on Windows). Note that NetBIOS over TCP/IP is being deprecated in favor of DNS.
4. Query the WINS server (on Windows), if one exists.
5. Perform an ARP broadcast name lookup over UDP.
6. Check the entries in the `LMHOSTS` (on Windows) file. `LMHOSTS` stands for the LAN Manager `HOSTS` file, and is the Windows version of the `HOSTS` file.

## Polling

Polling is a much slower process than finding a list cached somewhere on the network and returning the list to build a network list. Polling is a slow process that requires clients' responses to build a browse list. [Figure 4.3](ch04.html#network_discovery_using_polling_or_direc) shows an example of polling. Because of the overhead involved in polling, only the Address Resolution Protocol (ARP) is in common use. ARP provides a fallback protocol for name resolution when other methods fail. ARP is used on all types of networks, not just TCP/IP networks. You can use ARP on any LAN network — Token Ring, 802.11*x* wireless, or IP over ATM — to resolve IP addresses. ARP's major disadvantage is that it is a non-routable protocol. As a Link Layer protocol, ARP cannot be broadcast across a router; it applies to a single subnet.

### Note

DHCP is discussed in [Chapter 18](ch18.html).

## Connections

A network connection or *circuit* is a communication path between two endpoints. Network connections can have a variety of characteristics, some of which are universal and others which are dependent on the type of network in use.

An endpoint is an addressable entity that can send and receive network traffic. Endpoints are the network interface and not the systems or devices that the network interface resides in. To be even more specific, a NIC is simply an add-in card and a packaging device for an application-specific integrated circuit (ASIC), which is the integrated circuit that is part of the Physical and Data Link layers in the OSI model. To be precise, the endpoint of a network connection is defined by a set of software routines that can send and receive network traffic over the wire, with some portion of the interface defined by the physical implementation of digital signal processing required to turn data into signals that are transmitted.

The concept that an endpoint can be captured in software leads you naturally to a central concept in computer science, that of virtualization. Virtualization is where a system or device is emulated in software. It is possible to create a virtual endpoint or virtual interface in software whenever you need it. If you work in a virtual machine environment, and many systems create these types of emulated machines, then not only is the computer's operating system virtualized, but devices such as network interfaces are also virtual. Virtualization abstracts function from implementation, and appears in systems where emulation is required, in products like Virtual Server and VMWare, and in many other applications besides.

A path or circuit is the second part of a connection's definition. A path can be a dedicated physical circuit that can be traced from one endpoint to another over a wire that can be identified and is unchanging. Some networks work in this manner, mostly smaller networks where the number of connections is manageable. However, because network fan-out creates an exponential number of possible connections, most networks do not define persistent physical circuits because that would be prohibitively expensive. Instead, networks use a switching technology to create a transient circuit, depending upon network conditions. Transient circuits are created and then released after their use. They are contrasted to permanent circuits where the same path is used for an entire session, and not just for a data transfer. Network traffic is routed over a transient circuit, based on sophisticated routing algorithms that determine the shortest path, least congestion, highest-performing switch, fastest transmission medium, and whatever other factors the switch or router designers want to model.

Not all network connections are designed to be either persistent or transient. When designing a network that is inherently unreliable, different methods must be used. This is exactly the problem that the designers of the Internet were trying to solve. How do you create a highly fault-tolerant network when large portions of the network are disrupted? The solution to this problem was to use packet-switched networks, which send a stream of packets from one endpoint to another. A packet is a specially formatted segment of transmitted data. When you talk about network connections on a packet-switched network, you are describing a virtual circuit; the path is undefined or dynamically assigned and can change at any moment depending upon conditions. One packet in a stream may travel over one route, and the next may travel over another.

Virtual circuits can be created within a connection as a separate channel that carries only a certain type of data. This is the basis for Virtual Private Networks (VPNs), where secured traffic flows from one endpoint to another. To create a VPN, two applications must negotiate a set of connection parameters that define the behavior of the virtual circuit.

### Note

For more information on VPNs, see [Chapter 29](ch29.html).

In describing connections, I have used the terms *persistent* and *transient* to indicate the path definition. The terms used in computer science for these two types of connections are *stateful* and *stateless*. A stateful connection is one in which the connection is defined between two endpoints for an entire session and can be invoked after the session is complete to recreate the original connection. A stateful connection also stores attributes of the connection that will be reestablished. The term stateful is also applied to any process that takes the nature of the contents of communications into account. A firewall performs stateful inspection when it examines not only the headers of packets but also the contents.

[Figure 4.5](ch04.html#five_different_types_of_network_connecti) illustrates the different types of circuits in a graphic form. The endpoints are the circles at the end of the lines, which represent connections or paths. A solid line or circle indicates that the network element is persistent; an empty circle or dotted line indicates that the network element is transient. In the bottom case (private connection), the small solid line is contained within an empty larger line, indicating that the connection is not only transient, but secure.

[Figure 4.5](ch04.html#five_different_types_of_network_connecti) shows five different types of network connections that can be defined.

![Five different types of network connections](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0405.png)

**Figure 4.5. Five different types of network connections**

In comparison, stateless connections are those in which the path used is indeterminate and only the endpoints are known and the connection is transient. No details of the connection are retained or managed. An example of a stateless connection is communications using the HTTP protocol over a TCP/IP network. As previously mentioned, packets can travel by any convenient route between the two endpoints. A measure of "statefulness" can be applied to stateless connections without changing the classification of the connection type by recording transient information in a manner that allows the information to be retrieved later. That is exactly what Web sites do when they put a cookie on a computer; it stores information about the user, prior sessions, and other details.

Connections are named objects in all network operating systems and are programmatically accessible in any of the object-oriented programming languages in current use. Network objects have a number of attributes that describe them and that are important in understanding how connections function. Those attributes include the state of the connection, the protocols in use, and other factors. Another defined object related to connections is that of a *session*. A session is a defined period during which a network connection is engaged in a communication of a defined type. For some system functions, the session may be defined as the entire time that a network interface is up and running, sending and receiving traffic. Applications use the concept of a session to set rules such as the allowed bandwidth, the Time to Live (TTL) parameter that packets have, and others. The attributes of connections and sessions allow two systems and devices to negotiate the connection properties.

# Simple Network Management Protocol

As networks became more complex historically, the need to discover, manage, and control devices on the network became an important concern. The Simple Network Management Protocol (SNMP) was developed within the framework of the Internet Engineering Task Force (IETF) to provide a means to address these needs. SNMP is an Application layer (Layer 7) protocol that has become the most widely used method for managing network systems.

SNMP has five built-in elements that are part of networked devices:

- **SNMP protocol**. Used to communicate between devices and SNMP-enabled software over TCP/IP networks.
- **Managed objects**. Respondent devices such as Network Interface Cards (NICs), routers, switches, printers, and a panoply of other devices.
- **Agents**. A small software module that is resident (running) on a managed object. It collects data from the object and from network traffic and makes it available to SNMP queries.
- **Management Information Bases (MIBs)**. MIBs comprise an object database that stores information about managed objects. Many, if not most, data objects used by SNMP devices are `READ-only` (the Device Model, for example). Other data objects are `READ`/`WRITE` (the Device Name, perhaps) and are therefore variables that are used to manage objects.
- **Management console**. Where data queries are collected using SNMP-enabled software.

SNMP software can communicate with these elements to develop a picture of the network, create an inventory of the device's state or functions, and receive and react to those events. The model used by SNMP is used by other vendors as the model for their own management systems. The Windows Management Interface (WMI) from Microsoft, which is discussed later in this chapter, is one example of a proprietary SNMP implementation.

SNMP network management uses SNMP commands to send and retrieve data collected from the SNMP agents on managed nodes. [Figure 4.6](ch04.html#snmp_network_discovery_and_management) shows how SNMP discovery and management works. A management console collects SNMP responses and stores and displays the information to users. The console can also be used to send SNMP commands that modify device settings. A managed node, labeled as a circled N in the figure, is one that can accept and act on SNMP commands. The circled A represents SNMP agents, which are small software programs that can send and receive SNMP information. SNMP has very broad product support.

[Figure 4.6](ch04.html#snmp_network_discovery_and_management) shows how these different SNMP elements interact with one another.

Control console management software sends and receives SNMP commands from other devices on the network. Console management software is an application that can store device information, display it to a user, and change device settings through user commands. Devices that can initiate and respond to SNMP commands are referred to as a *party*, a name that is formalized within the SNMP version 2 definition. A party is a single identity that has a unique network location. Each party in an SNMP communication has an authentication and privacy protocol that it uses to establish a secure link with other parties. Devices that are SNMP-enabled (entities) may contain multiple parties within them, provided that each is unique. An example of an entity would be a router, where each individual port of the router would be a party. A router can be managed down to each individual port level.

![SNMP network discovery and management](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0406.png)

**Figure 4.6. SNMP network discovery and management**

Network management software works by installing small software modules called *agents* on managed devices. Usually the software is installed with deep hooks into the operating system so that the agents are difficult to remove. Agents can also be installed by a vendor as part of the hardware on any device that can be managed, but not all vendors go to the expense or trouble to incorporate SNMP agent software. There is a range of software that can discover, manage, or map network devices using SNMP, including the following: shareware applications that you can download for free from sites like `Download.com` or `Tucows.com`; commercial packages such as WhatsUp Gold (`www.whatsupgold.com`) from Ipswitch; and many of the components of the large network framework management systems, including LANtastic, HP OpenView, IBM Tivoli, CA NSM (formerly Unicenter), Altiris, ZENworks, and many others.

SNMP is a broadcast technology that operates at the upper layer of the network model, the Application layer or Layer 7. Software can send out a request or query to any party that can listen for it, and to which another party can respond. SNMP uses a small command set that should be very familiar to anyone with knowledge of how the HTML protocol works. Commands used by SNMP, such as `GET`s, are used to communicate with specific agents on managed devices. Variants of these commands, such as `GETBULK` or `GETNEXT`, can be used to communicate with multiple devices. Agents also advertise their availability by sending out `INFORM` or `TRAP` commands that can be collected by management systems. Any data object that is writable can be changed using a `SET` command.

The Management Information Bases (MIBs) collect data on a managed node or system. The data that an MIB contains is defined by the device type but is extensible. SNMP makes no demands on the type of information stored on a device, or which device attribute can be a variable. What SNMP specifies is the manner in which information is stored in the MIB files, and the manner in which the information is exposed.

SNMP devices can change states at any time, and so the model requires that a device can advertise a change of state without waiting to be polled on its state. The MIB module on the device stores events that occur and then advertises these events by issuing what is called an SNMP trap for that event. Listening devices can intercept the trap and then request the details if required. SNMP is traveling over packet-switched networks such as TCP/IP, and so a management console can't assume that it has received all of the available traps that have been issued. Therefore, SNMP management software will, at an interval defined in the software, poll each managed device to update its status. Trap-directed polling requests that specific devices update their status, and because both parties in the communication are known, the traps are reliably received and updated. When an important trap is received, the interval between status updates is changed so that updates from the device are done more frequently.

In SNMP, MIB files are organized into a hierarchical namespace, an upside-down tree structure where each node is an object identifier, or OID. Individual OIDs may be `READ, SET`, or both. The ISO's Open Systems Interconnection (OSI) Abstract Syntax Notation (ASN.1) standard defines the syntax by which a MIB file is queried, and is something that is platform independent, using a set of rules that describe the MIB file called the Structure of Management Information (SMI). You can examine the structure and contents of an MIB file using any number of SNMP-enabled utilities.

Shown in [Figure 4.7](ch04.html#oidview_professional_is_an_snmp_manageme) is OidView Professional (`www.oidview.com`), one of the many SNMP utilities that are available to view MIB files, their structure, and the data that they contain. OidView performs SNMP analysis and presents the data in an MIB Browser. Different panes can display a searchable and navigable data tree, data analysis, graphs and traces, captured SNMP traps, and different MIBs from the different SNMP agents located on the network.

The Structure of Management Information (SMI; `http://en.wikipedia.org/wiki/Structure_of_Management_Information`) is information collected as text files onto which a structure or schema is imposed. What SMI means in practical terms is that if you are using a management console to perform network discovery for devices, then it doesn't matter if the devices you are polling are on the Ethernet network of the management console or on a network of some other kind. Nor does it matter what operating system you are using or what the device is. The information is simple text, and to use it the management console need only be able to parse the information correctly, something that is very easy to achieve.

Storage networking is a type of heterogeneous networking where storage data is segregated onto a separate network connected with Fibre Channel, while hosts and clients are on a separate Ethernet network. A heterogeneous network is one that supports multiple NOSs on the same network. The two networks are connected through one or more switches so that each network can communicate with devices on each side, and so that storage traffic is separated from data communications. [Figure 4.8](ch04.html#a_fibre_channel_storage_area_network_ope) shows this type of network.

![OidView Professional is an SNMP management tool.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0407.png)

**Figure 4.7. OidView Professional is an SNMP management tool.**

### Note

For more on storage networking, see [Chapter 15](ch15.html).

If you place an SNMP management console on the Ethernet network, it doesn't matter whether the SNMP application software runs on a Windows or a Sun Solaris workstation or server because SMI is agnostic (it doesn't favor a particular NOS). The management console provides what is called out-of-band management for the devices on the Fibre Channel network, which is the in-band network. It is out-of-band because the TCP/IP traffic looks like a different stream from the Fibre Channel data. A management console running software such as StorageWorks from HP can discover both the devices on the Ethernet and storage network at the same time. Not only are switch ports discoverable, but so are Host Bus Adapters (HBAs), as are the intelligent hard drives that are part of storage systems. HBAs are the network interfaces that storage devices connect to. Considering that some storage systems can contain literally hundreds of disk drives, the ability to discover and address each individual disk drive enables very powerful network management tools, such as Storage Resource Management packages, that can reconfigure volumes on the fly. That is the power that SNMP provides to intelligent network software.

![A Fibre Channel Storage Area Network (SAN) attached to a LAN](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0408.png)

**Figure 4.8. A Fibre Channel Storage Area Network (SAN) attached to a LAN**

# Windows Management Instrumentation

Windows Management Instrumentation (WMI) is a Microsoft extension of the Common Information Model (CIM) as exposed through the Web-Based Enterprise Management (WBEM) network management system. WMI creates a repository of data from managed objects and makes this information available to management software through an API, which is an extension of the Windows Driver Model (WDM). WMI is the interface by which the data repository can be queried, and through which commands and configuration settings can be passed to managed network devices on Windows networks. WMI commands can be applied inside a VBScript or Windows PowerShell script, or they can be entered as a command line.

WMI provides a rich management system that can control a large number of devices and give a detailed description of their current states, but WMI is Windows-specific technology.

WMI's enterprise management framework can take existing data from SNMP-managed nodes and agents and from any data source that works under the Desktop Management Interface (DMI) standard and make the data available to management software under a uniform access model. A number of Microsoft Office applications, servers, and even the Microsoft Internet Explorer extend the CIM mode to add their information to the CIM data repository that WMI manages as a WMI class with associated properties. WMI's repository has its own namespace and its own query language, which is called the WMI Query Language (WQL). The overall CIM repository contains the namespaces for the Active Directory (RootDirectoryDAP), for SNMP (RootSNMP), and for the Internet Information Services (RootMicrosoftIISv2).

Here are some of the many things you can do with WMI:

- Start or stop a process on a network system
- Restart a remote computer
- Compile a list of installed applications on a networked system
- Have a process run at a specified time
- Query the Windows event logs on a networked system

Microsoft exposes WMI in the form of a set of providers. As of Windows Server 2008 and Vista, there are around 100 providers that have been published. In addition to the scripting tools previously mentioned, a wide variety of management software can be WMI consumers, including Microsoft System Center Operations Manager, HP OpenView, BMC Software Distributed Systems Management, and others. WMI provides not only an automation interface, but also a .NET management interface, and for older applications, a COM/DCOM interface. Providers can access WMI remotely with DCOM and SOAP and can consume WMI events.

# Mapping

Network mapping is the automated discovery of systems and the connections between them. Different mapping software packages use different techniques to map a network, but one common technique is to start with each subnet that the software knows about and then `PING` each of the possible network addresses to see which nodes respond. This process enumerates any device that is currently active on the network and is an active discovery method. You can do this kind of mapping using a utility such as `nmap` on Linux, Microsoft Windows, Solaris, and BSD, and Mac OS X. nmap (`www.nmap.org`) runs as a command line utility, but there are several graphical front ends such as Zenmap (`http://nmap.org/zenmap/`), which is shown in [Figure 4.9](ch04.html#a_zenmap_network_scan).

There will be nodes on the network that may be unavailable at a particular time, and so an active method won't find devices that aren't active. Nor will it find any nodes that aren't on subnets that the mapping software's system knows about. To find more nodes, various passive exploration methods must be used.

![A Zenmap network scan](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0409.png)

**Figure 4.9. A Zenmap network scan**

The problem with active network discovery tools is that many operating systems now come with personal firewalls that block their discovery and prevent their detection. If the system is a laptop, then that system won't always be available for discovery, and so any software that intends to build an accurate network map needs to use both active and passive methods to have any chance of building a complete map. Passive exploration looks in places that store network addresses such as router tables and browse lists to extract endpoints from those sources. By contrast an active exploration would have to discover the devices themselves. Those tables provide information on how to discover the entire network, and they extend the discovery process to the additional subnets, within the number of hops from the network's routers that the system wishes to explore.

There are several different techniques used to map networks:

- Active identification of the different points of attachment that devices have on a network.
- Examining packet routing through the mining of routing tables.
- Payload inspection to determine the sending system, as well as any intermediate locations that have added addressing to the packets.
- Mining the data in available Authentication, Authorization, and Accounting (AAA) servers. AAA servers include dial-in, RADIUS, and other remote access servers.
- Network access credentials. By examining user and machine logins, additional mapping can be accomplished.

Many software packages can map networks and include the following: SNMPWalk, Cheops, SNMPutil, WhatsUp Gold, and PacketTrap.

The purpose of network discovery is to map the network; determine what systems, devices, and software are on the network; and improve the network health and security. Network discovery can find unknown systems as well as determine methods for discovering systems on the network that aren't meant to be discovered.

A network map is able to accumulate all kinds of data. When a system is profiled, it is possible to determine which processor the system has (type and ID), what version of the operating system it has (type and install ID), when it was last patched or upgraded, the specific hard drive (type and ID), and so on, in great detail. This information allows you to create an asset inventory of your entire network that you can use for any purpose. Organizations that have network management systems in place with asset management modules, systems such as LANtastic or Altiris, can produce detailed reports of the nature and location of their assets, which can be invaluable in planning, deployment, and utilization.

# Summary

In this chapter, you learned about different methods for network discovery and name resolution. These methods are independent of the protocols used, but often determine how protocols are constructed.

Connections are paths with defined endpoints. Different types of connections can be defined, a combination of physical and virtual paths and endpoints.

You learned about SNMP and how it is used to store device information and provide that information to other applications. SNMP can not only provide device information but it can also allow an application to send commands and change the configuration and state of devices. With SNMP, you can map networks and do deep asset analysis.

In the next chapter, you will learn about aspects of network performance related to bandwidth and throughput.
