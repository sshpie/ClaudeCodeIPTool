# Chapter 16. High-Speed Interconnects

**IN THIS CHAPTER**

- Different high-speed network standards
- Techniques for offloading network processing
- High-performance networked computers
- Grid, mesh, edge, and cloud computing

High-performance computing requires networks to function. They can be powerful systems that use high-speed networks, or distributed systems that have many members and can use low-speed networks. In this chapter, you look at both types of solutions.

Ethernet is a pervasive networking standard. The current leading-edge Ethernet systems use 10 Gigabit Ethernet (GbE). This standard is described, as well as the future forms of Ethernet that are currently under development.

Networks currently can carry more traffic than most computers can process. To make computers more efficient, a number of technologies have been introduced. TCP Offload Engines (TOEs) can remove most of the network I/O and make computers much more efficient.

Another set of technologies that are similar to TOEs are called *zero copy networks*. They create a virtual network interface that also offloads network processing. The Virtual Interface Architecture and the InfiniBand peripheral bus are examples of zero copy networks that are examined. Five of the ten most powerful computers in the world were built using this high-performance bus.

A number of different network cluster types are discussed. These include fault-tolerant systems that provide failover, load-balanced solutions that help achieve better utilization on server farms, and pervasive utility computing where distributed systems are networked together into a virtual supercomputer.

Grid or mesh computing is an important and growing area of networked computers. The largest computer projects ever built were of this kind. Examples such as Folding@home and SETI@home are considered. Grid systems are being developed to enable cloud computing, with a view toward creating computer utilities.

# High-Performance Computing

*High-performance computing*, or HPC, is a term used to describe systems capable of high speed or high output. The term has been applied to mainframes, supercomputers, clustered computers, and more recently, cloud, distributed, and grid computing. Most HPC systems rely on their network systems to provide the services necessary to make their architecture work.

In some cases, networks must use advanced networking hardware such as 10 Gbits/s Ethernet (and beyond), high-speed peripheral interconnects such as InfiniBand, and special function network adapters such as TOEs and the Virtual Interface Architecture. In this chapter, these technologies are discussed, as well as why they are important and where they are used currently.

You can also get high performance by using slow and unreliable connections, such as the Internet running on low-power computers or consuming a fraction of the resources of high-power computing if the scale of the project is large enough. The largest computing projects yet attempted, the ones that have performed the most compute cycles, are distributed systems that run on volunteer computers all over the world. Essentially systems of this type are massively parallel-processed supercomputers. While they aren't free for the people who pay the electric bills, they are low cost when the systems are shared for a common purpose, and they enable expensive projects to be done that otherwise wouldn't be possible.

With the emphasis on computer networking as a utility and software as a service, there is a lot of interest in computer systems that create a cloud to enable what has come to be called *pervasive computing*. That is, the availability of the network wherever you might be. The industry is moving toward this type of system both in software through operating systems and remote applications and by using virtualization technologies. That will make grid systems and distributed networks much more popular going forward.

If you are sitting in front of your PC, you might reasonably ask what does a chapter like this have to do with my network? The answer is, of course, that these technologies tend to become less expensive over time and tend to show up in next-generation hardware. It isn't unreasonable to expect to see the technologies in this chapter brought to bear on massively multicore desktop computers running parallel-processing operating systems in about five years time.

Just in case you are curious, the `Top500.org` project collects statistics on the most powerful computers in the world twice a year. They store the information on their site in a form that allows you to see which vendors, technologies, countries, and installations have reached specific performance levels. Top500 numbers are based on LINPACK statistics submitted by people either working for or associated with the computer systems they list. Their list was published in June 2008 to coincide with the International Supercomputer Conference, and in November when the U.S. IEEE Super Computer Conference meets. [Table 16.1](ch16.html#top_10_computers) shows the top ten computers in November 2008.

**Table 16.1. Top 10 Computers**

| Rank | Rmax, Rpeak[[a]](ch16.html#ftn.CHP-16-TFN-1) (TFLOPS) | Code Name | Details | Vendor | Site |
| --- | --- | --- | --- | --- | --- |
| [[a]](#ftn.CHP-16-TFN-1) |  |  |  |  |  |
| 1 | 1105, 1457 | Roadrunner | IBM BladeCenter QS22/LS21122400 (Cell/Opteron) | IBM | Los Alamos Laboratory, United States, 2008 |
| 2 | 1059, 1381 | Jaguar | Cray XT5 QC 2.3 GHz | Cray | Oak Ridge National Laboratory, United States, 2008 |
| 3 | 487, 609 | Pleides | SGI Altrix ICE 8200EX | SGI | NASA/Ames Research Center/NAS |
| 4 | 478, 596 | Blue Gene/L | eServer Blue Gene Solution212992 (Power) | IBM | Lawrence Livermore National Laboratory, United States, 2008 |
| 5 | 450, 557 | Intrepid | Blue Gene/P Solution163840 (Power) | IBM | Argonne National Laboratory, United States, 2008 |
| 6 | 433, 579 | Ranger | SunBlade x6420, Opteron QC 2.3 GHz, InfiniBand | Sun | Texas Advanced Computer Center, United States, 2008 |
| 7 | 266, 356 | Franklin | Cray XT4 Quadcore 2.1 GHz 2008 | Cray | NERSC/Lawrence Berkeley Labs |
| 8 | 205, 260 | Jaguar | Cray XT4 30976 (Opteron) | Cray | Oak Ridge National Laboratory, United States, 2008 |
| 9 | 204, 284 | Red Storm | Sandia/Cray Red Strom XT 3/4 | Cray | NNSA/Sandia National Laboratories |
| 10 | 181, 233 | Dawning 5000A | Dawning 5000A, QC Opteron 1.9 GHz, Infiniband, Windows HPC | Dawning | Shanghai Computer Center |
| [[a]](#CHP-16-TFN-1)Rmax is the highest LINPACK score, and Rpeak is the theoretical peak as measured in teraflops. |  |  |  |  |  |

# Beyond Gigabit Ethernet

Gigabit Ethernet, or GbE (also abbreviated as GigE), is the current commodity standard for Ethernet networking. That is, you can purchase GbE switches, routers, and hubs for prices that make them a practical choice for small offices and home networks. One of the most, if not the most, popular GbE cards is the Intel Pro/1000 GT. It currently sells for around $36 ($23 OEM). Ethernet is such a pervasive standard that in this section, you'll be taking a look ahead to see what the Ethernet roadmap has in store for high-performing networks.

Ethernet standards have followed a progression where the speed increases by a factor of ten times with each new generation. So far, you have seen the following:

- 10 Mbits/s Ethernet, 10Base-T
- 100 Mbits/s Ethernet, 100Base-T
- 1 Gbits/s Ethernet, 1 GbE
- 10 Gbit/s Ethernet, 10 GbE

### Note

The term *Base-T* refers to Ethernet running over a twisted pair of copper cables.

The 10 Gigabit Ethernet IEEE 802.3ae standard appeared in 2003 and currently is the fastest defined Ethernet standard on the market. Versions of 10 GbE have appeared for optical fiber, twisted-pair copper wire (10GBase-T), and over copper twin-ax (InfiniBand) cable. The standard defines full-duplex connections (two-way traffic) and does not support half-duplex CSMA/CD. The current market for 10 GbE technology is somewhat more than 1 million ports per year and is sold in the storage, fabric network, and virtualization markets.

You should note that there are several different 10GBase-T connection types. For optical fiber, you will find versions of 10GBase connections in R (standard Range), SR (Short Range), LR (Long Range), LRM (Long Range Multimode), ER (Extended Range), ZR, and LX4. On copper, the connection standards for 10GBase are T (802.an-2006), CX4 (802.ak), SFP+ Direct Attach, KX4, and KR. KX4 and KR are 802.3ap standards used in backplanes such as routers, switches, and blades.

### 10GBase-T

The 10GBase-T is the most popular connection and can be used over twisted-pair cables up to 100m in length, but it isn't the fastest of the connection types just mentioned. 10GBase-T is backwards compatible with 1GBase-T, and its ports can automatically negotiate the port speed. This standard uses RJ-45 connectors and Category 6 cabling, preferably augmented Cat6a cables. The additional partitioning in the cable helps to reduce crosstalk.

The connection modules for 10 GbE cables are called PHYs, and they connect a link layer device (a MAC) to the copper or optical fiber cable. A PHYceiver is the chip that enables a physical layer connection to a 10 GbE cable, and it comes packaged with a microcontroller in a pluggable module that fits into the backplane of a 10 GbE switch or router. PHYs exist for both LAN and WAN 10 GbE modules, but the WAN PHY, while slower, shares the same type of optics. PHYs encode and decode data for transmission and reception, and have two separate subsystems: a Physical Coding Sublayer (PCS) and a Physical Medium Dependent Layer. Other technologies that use PHY chips are USB, SATA, IrDA (sometimes), and many embedded systems.

### Tip

Current information on 10 GbE products may be obtained from `10GbE.net`.

You can buy 10 GbE network interface cards (NICs) from a number of vendors, including Intel, Chelsio, NetXen, Silicom, HP, Neterion, LeWiz, Tehuti Networks, and Myricom. One vendor, NetEffect, was recently purchased by Intel. NICs use PCI-X or PCI express and are connected with different types of PHY modules. The current recommendation is to buy the CX4 copper standard for 10 GbE connections less than 15m, and fiber for any distance greater than that.

### Higher-Speed Gigabit Ethernet

The growing need to have faster switch and backbone connections is being driven by many factors. The use of video on sites such as YouTube, Google's only video download site, is one example of a business that has enormous bandwidth issues. The concentration of traffic onto high-speed optical backbones also makes technologies above 10 GbE attractive. To set standards for a next-generation Ethernet, a number of large companies have formed the IEEE Higher Speed Study Group (HSSG).

The current work of the study group has been to achieve a consensus among vendors on the speed of the next generation of GbE. There was contention between a set of vendors who wanted to release a 40 GbE standard that would work with the OC-768 optical backbones and support server-to-switch connections, and those who wanted to release a 100 GbE standard for switch-to-backbone connections. The result was that the study group opted to support products at both speeds.

The 802.ba standard products should appear in 2010 on either multimode fiber optic cable (for lengths greater than 100m), or on copper (less than 100m). Single-mode fiber optic cable with support of length in the 10km to 40km range but offering no multi-wavelength WDM capability will also be available. The expectation is that the 100 GbE devices that provide a switch-to-backbone capability will become available in 2011.

# TCP Offloading Engines

A *TCP Offload Engine*, or TOE, is a special type of network interface that contains a dedicated TCP/IP stack and a custom ASIC dedicated and optimized for a network I/O processor. Current TOE solutions have focused on 10 Gigabit Ethernet (GbE) network interface cards, as those technologies are the most popular.

As early as 1990, Auspex created a UDP offload technology that became known as Functional Multiprocessing (FMP). Alacritech, which was formed by Larry Boucher and other Auspex engineers, became the first company to offer a TCP offloading NIC in 2001. Their current SEN2102ET 10 GbE copper wire TOE card is shown in [Figure 16.1](ch16.html#the_10_gbe_alacritech_copper_wire_pci-e). The Microsoft Chimney Offload (previously the Partial TCP Offload Architecture) is based on technologies from Alacritech, as is Broadcom's TCP Chimney Offload Chips.

TOE is implemented in the following ways:

- **iSCSI HBAs**. These TOE HBAs are disk controllers on the computer side, and iSCSI initiators on the network side. This is a full TCP offload technology.
- **TCP Chimney Offload**. The TCP Chimney Offload technology, as it was implemented by Microsoft and Broadcom, is a partial offload system. A Chimney TOE system offloads TCP processing but allows the CPU to retain control over the connection between TCP endpoints. This addresses a major criticism of the TOE technology. TOE's detractors argue that it makes systems less secure because the system becomes unaware of the connection and the potential exists that connection can be manipulated by an outside party.
- **Parallel Stack Offload**. In a Parallel Stack Offload technology, the entire TCP/IP stack is duplicated; this is called a *Full Offload*. One stack runs on the host CPU, and the second stack runs on the TOE engine. This second TCP stack is called a *vampire trap*; it intercepts and redirects TCP traffic made by applications to the main TCP stack.

![The 10 GbE Alacritech copper wire PCI-e 1X Ethernet TOE card. The custom ASIC is the large, black chip with the running man in the lower-right side of the card.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1601.png)

**Figure 16.1. The 10 GbE Alacritech copper wire PCI-e 1X Ethernet TOE card. The custom ASIC is the large, black chip with the running man in the lower-right side of the card.**

### Note

The TCP is described in detail in [Chapter 17](ch17.html) .

The TCP is the Transport layer (OSI Level 3) of the Internet Protocol (IP). TCP does the following things:

- Establishes and terminates the endpoints of an IP connection through handshaking
- Provides a messaging protocol
- Establishes a packet sequence
- Provides an error-checking mechanism
- Offers a sliding window congestion control
- Acknowledges packet reception

TCP does these things by adding a header to data and creating a packet. To this packet, the IP adds the addressing that defines the source system, and the address needed for the packet to make its way to the endpoint of the connection. TCP requires a significant amount of processing to manage the packets. On GbE networks, computer systems that perform a significant amount of network I/O become processor-limited. These types of systems include Web servers, terminal servers, file servers, backup servers, and many other application servers.

### Note

The process of adding the header is called encapsulation, and removing it is called expansion or unpacking. Strangely, de-encapsulation isn't an English word. In networking, the terms used for establishing and breaking a logical connection over a virtual circuit are called setting up and tearing down, respectively.

If you analyze the amount of time spent by data sent by one networked application to another on a standard network without offload, the amount of time spent processing a data transfer is nearly ten times the amount of time that the data spends moving on the wire. These processor resources are stolen from the actual computing that the system is meant to be calculating. When you employ offload techniques such as TCP Offload, processor utilizations on single-core processors that were in the 85 to 95 percent range can drop to as little as 10 to 15 percent. TOE is also especially valuable in streaming multimedia applications.

TOE combines a processing function with a complete functional TCP stack. A TOE subsystem reads and writes the headers of IP packets, sends and reads the TCP messaging, and performs connection setup and teardown without the computer's CPU (or CPUs) being involved. TOE also uses forms of Direct Memory Access (DMA) to read and write to memory buffers without the CPU. Indeed, with a TOE-enabled computer, the application that is generating the request for TCP traffic only needs to have the processor send a request to the TOE systems to transfer the data, and TOE does the rest.

TOE does have one other important performance benefit. Because TOE sits on a PCI-e NIC, much of the processing and data transfer overhead is prevented from traveling over the PCI bus interface. PCI doesn't handle large numbers of small messages as well as it does large amounts of data contained in a few messages. By removing the messaging traffic from the PCI bus, the latency that PCI introduces in network traffic can be greatly reduced.

While TOE does have significant performance benefits in current networked computer technology, given the imbalance between high network versus low processor capabilities, the technology does have some disadvantages. Perhaps the most significant criticism is the one already mentioned: security. TOE takes responsibility for an essential network function away from the networked operating system. Therefore, when there are security threats, you are relying on the TOE vendor to protect your network subsystem. Because TOE removes connection information from the host, it also impacts a system's ability to manage session characteristics such as packet filtering and Quality of Service parameters.

TOE cards are expensive and aren't yet commodity items, and so they tend to be marketed as NICs for servers or they show up as chips on some Intel server motherboards. It is possible that the technology could become cheaper and more pervasive in the years to come, but at the moment TOEs are sold as proprietary systems by a limited number of vendors.

Because the Virtual Interface Architecture (VIA) uses TOE, the section on VIA later in this chapter returns to this topic.

# Zero Copy Networks

A zero copy network uses a CPU offload technology to transfer information in special dedicated memory from one computer to another. This frees the CPU system resources to work on other computational tasks, making the computer more efficient. Network I/O is also improved because user-level applications can direct the kernel to transfer data without sending the data back to the application. Data is accessed using a form of direct memory access (DMA) without the need for the kernel to intervene further once the command is sent. The latency introduced by kernel/user-level context switching, which is required to cycle through different processor states when data moves from one to the other, is removed.

To enable a zero copy system, a computer must have intelligent network adapters with their own network protocol stacks. ASICs on the adapter enable it to control specialized device drivers, use file system extensions, and use DMA methods to have a Memory Management Unit copy and map data from memory to the adapter for network transfer. Most of the vendors that sell network systems of this type provide both hardware and software. However, there is growing support within networked operating systems for zero copy operations. The Linux APIs `sendfile` and `sendfile64` have zero copy support, as does Java's class libraries on UNIX and Linux through the `transferTo()` method in the `java.nio.channels.FileChannel`.

[Figure 16.2](ch16.html#zero_copy_versus_standard_copy_transfers) shows a schematic of zero copy file transfers versus a standard file transfer. There are two context switches for zero copy, and four for standard copy operations. In the Zero copy scenario, data is read from disk and requires a single User level command to move the data from the read buffer to the socket buffer where it can be read by the NIC. In the standard file copy, the data is read from the read buffer and then copied to the socket buffer with two User level commands. Any time you issue a User level command, you perform a context switch that changes the state of the CPU twice. A context switch interrupts the processing queue and adds significant overhead to any operation, which is why Zero copy offers a substantial benefit.

Remote Direct Memory Access (RDMA) in these systems allows application data on a sending computer to be sent to the receiving computer's memory without the use of either system's operating system. RDMA requires some special memory access programming and must populate memory with the data that is required to be transferred.

Zero copy technology shows up in very powerful distributed parallel-processing systems where the speed of the network has outpaced the computers' ability to process output.

![Zero copy versus standard copy transfers](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1602.png)

**Figure 16.2. Zero copy versus standard copy transfers**

## Virtual Interface Architecture

*Virtual Interface Architecture*, or VIA, is a high-speed cluster networking standard that was created by a consortium of companies including Intel, Microsoft, and Compaq (now part of HP) at the end of 1997. Clusters of computers were becoming popular as replacements for mainframes and supercomputers of the past, and VIA was meant to help them scale more efficiently. VIA was meant to be an open interoperable standard that would replace proprietary cluster networking solutions.

VIA is used in the following:

- **InfiniBand**. A switched fabric network architecture
- **Internet Wide Area RDMA Protocol (iWARP)**. An expanded version of VIA for IP networks
- **Emulex (formerly GigaLAN) cLAN**

The primary bottleneck in high-performance computer networking is the latency introduced by the excessive amount of processor utilization required to maintain all of the I/O traffic that moves from system to system. In high-performance cluster networks without some form of CPU offload technique, high-speed networks consume enough processor resources to dramatically impact system performance.

[Figure 16.3](ch16.html#via_system_components) shows a schematic of the virtual network interface created by VIA. The VI architecture can be described by a VI service consumer, which is an application layer function that interacts with a Vi service provider that includes a user agent overlying kernel level functions. Commands sent to the VI provider from the application are managed by a VI kernel agent, whereas data goes directly from the VI application to the virtual NIC for processing. The two agents perform tasks such as queue management and prioritization; processor intensive tasks such as addressing and packetization are performed at the VI NIC level. Notice that the data channel goes directly from the User level to the VI NIC without having to be processed by kernel level functions.

![VIA system components](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1603.png)

**Figure 16.3. VIA system components**

Data copies and file transfers follow what has been called the 80/80 rule:

- Eighty percent of the copy operations copy data of 256 bytes or less for control and synchronization.
- Eighty percent of the data required is contained in data of 8K or more.

These factors introduce tremendous overhead in copying operations and network file transfers. It is these kinds of problem that VIA solves.

### Note

VIA networks are called System Area Networks (SANs), a usage that predates Storage Area Networks (also called SANs). To avoid confusion, this book uses the term VIA network when describing this technology. VIA is also the name of the integrated circuit manufacturer in Taiwan that makes a low-power X86 CPU that powers many laptops.

VIA is a zero copy networking protocol that bypasses the kernel mode and virtualizes the network interface. User-level applications can control and signal the network interface without CPU processing, greatly reducing processor overhead. The virtual interface is called a *provider* and the application that accesses that interface is referred to as the *consumer*. The control path is used to set up and tear down a connection. The data path sends and receives Send/Receive and Remote DMA READ/WRITE messages. VIA access is provided through the use of the Virtual Interface Provider Library (VIPL).

The Internet Wide Area RDMA Protocol, or iWARP, is an IETF standard that is another superset of VIA, one that is used on TCP/IP networks. The network interface controller for iWARP is an Ethernet TCP Offload Engine that uses the Direct Data Protocol (DDP) to initiate the zero copy operation. TCP is the transport protocol used for iWARP. iWARP uses a verb interface (like InfiniBand). Other protocols that can use iWARP are defined by the OpenFabrics Alliance for Linux, and by Winsock Direct from Microsoft.

## InfiniBand

InfiniBand is derived from an industry initiative to create the next-generation replacement of the PCI bus by a couple of industry groups. The InfiniBand Trade Association (`www.infinibandta.org`) was formed in 1999 to create a new high-performance server peripheral and switched fabric network bus. The two original technologies were called Next Generation I/O (NGIO) and Future I/O (FIO), and when merged, they were called System I/O. InfiniBand was the result.

The InfiniBand architecture is a superset of VIA and implements connections between computer systems, high-performance storage systems, and other devices. The InfiniBand standard has been defined to grow over time and has been released in three different speeds: 1X (2 to 8 Gbits/s), 4X (8 to 32 Gbits/s), and 12X (24 Gbits/s), with the ranges defined by the use of Single, Double, and Quad Data Rate memory (SDR, DDR, and QDR).

InfiniBand doesn't implement an API that vendors can program against. Instead, the standard specifies a set of verbs and actions that must be implemented. A vendor then uses a programming language of their choice to create a control and messaging system.

An InfiniBand connection is a bidirectional link that has a 10-bit channel, 8 bits of which are data and 2 bits of which are dedicated for control signals. The faster speeds are links that are aggregated as multiples of 4 and 12 single links. A link is defined as the connection between channel adapters, which has the same role for InfiniBand that NICs have for Ethernet. A Host Channel Adapter (HCA) and a Target Channel Adapter (TCA) on a computer and a peripheral device negotiate security protocols and define QoS parameters for the connection. Channel adapter vendors include Cisco, Mellanox, and QLogic. InfiniBand switches are made by Cisco, HP, Mellanox, QLogic, and Voltaire.

InfiniBand has become the interconnect of choice for very high performance cluster computer systems. If you look at [Table 16.1](ch16.html#top_10_computers), you can see that five of the top ten highest-performing computers in the world are currently InfiniBand clusters.

However, InfiniBand has seen slow adoption in the industry. Some of the reluctance to adopt InfiniBand has been due to people waiting for higher-performance Ethernet standards to be developed. Fibre Channel is also hard to displace in switched fabric storage networks. Vendors are working on a Fibre Channel over InfiniBand (FCoIB) technology that they hope will make InfiniBand more popular in the Storage Area Network marketplace.

[Figure 16.4](ch16.html#infiniband_can_function_as_a_high-speed) shows a hypothetical InfiniBand WAN with an emphasis on storage device connections.

![InfiniBand can function as a high-speed and highly redundant component of a WAN.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1604.png)

**Figure 16.4. InfiniBand can function as a high-speed and highly redundant component of a WAN.**

# Network Clusters

Computer clusters are one area in which fast networking standards play a central if not critical role. A cluster can be created using two computers sharing a common peripheral bus. However, once you start connecting multiple computers together, separating them into server farms, or distributing them into a grid architecture, peripheral buses are replaced by networks. In the sections that follow, you look at two different types of network clusters: those that are powerful and require speedy connections and those that are just as powerful but operate with a large number of computers and use a standard network.

Network clusters are formed for the following purposes:

- **Fault tolerance**. Mission-critical applications that require zero or close to zero downtime. [Table 16.2](ch16.html#fault_tolerance_requirements) shows different levels of fault tolerance.
- **Utilization**. Server farms that work by having a front-end system that performs load balancing where the emphasis is on server utilization.
- **Pervasive utilities**. Distributed computing where the desired result is the creation of a computer utility that can support pervasive computing applications.

**Table 16.2. Fault Tolerance Requirements**

| Percent Uptime | Downtime per Year | Platform | Implementation |
| --- | --- | --- | --- |
| 90 (one nine) | 36 days, 12 hours, 36 minutes | Standard PC/server | No fault tolerance required |
| 99 (two nines) | 87 hours, 46 minutes | Departmental server | Restore from image |
| 99.9 (three nines) | 8 hours, 46 minutes | Highly available | Failover to a mirrored or backup server |
| 99.95 | 4 hours, 23 minutes | Highly available | Failover to mirrored or backup servers |
| 99.99 (four nines) | 52 minutes, 33 seconds | Mission critical | Cluster failover to another node |
| 99.999 (five nines) | 5 minutes, 35 seconds | Fault tolerant | Entire computer duplicated for very fast failover |
| 99.9999 (six nines) | 31.5 seconds | Continuous | Stratus FT systems, and a few others |

Fault tolerance in clusters is created by implementing a failover system. That failover system can be as simple as a heartbeat circuit that is constantly checking to see if one node of the cluster is still up and running. The heartbeat circuit sends out periodic messages asking if the system is running and waits a certain period before retrying or issuing a command to fail over to the secondary system in the cluster.

The earliest Microsoft clusters were two-node clusters with a shared storage solution, as shown in [Figure 16.5](ch16.html#a_simple_two-node_failover_cluster). The two computers were in a master-slave relationship; if one failed, then the cluster failed over in just a few seconds or so to the other system. The shared storage was a RAID solution that was highly unlikely to fail. These types of clusters can be share-something, share-nothing, or share-everything systems. Nearly all of the server hardware and network operating system vendors currently offer clustered solutions.

Failover clusters or fault-tolerant computers can be as complex as a multiply redundant computer system that is constantly updating all nodes at once. An example of a share-everything system is the Stratus FT series, which is deployed in highly mission-critical applications where failure cannot be tolerated. Their Lockstep system architecture with fully redundant systems is shown in [Figure 16.6](ch16.html#the_stratus_lockstep_architecture_has_mu). This system is capable of *six nines* reliability (99.9999 percent) with a downtime of less than 31.5 seconds a year.

![A simple two-node failover cluster](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1605.png)

**Figure 16.5. A simple two-node failover cluster**

In [Figure 16.6](ch16.html#the_stratus_lockstep_architecture_has_mu) you can see that data is written simultaneously to three separate symmetric multiprocessing (SMP) systems containing N-processors/processor cores. Stratus populates these systems with proprietary chipsets: the Status North PCI (SNP) and Stratus South PCI (SSP) ASICs (Application Specific Integrated Circuits) that maintain transactional coherency as data is processed. The SNP and SSP chips are able to simultaneously communicate with the passive backplane, which is an I/O (Input/Output) interface that communicates with peripheral devices, or through network interfaces to other systems.

Networked cluster computers are among the most powerful computers ever built. The most powerful monolithic computer yet built according to `Top500.org`, the Roadrunner at Los Alamos Laboratory in New Mexico, was built by IBM from a BladeCenter QS22 Cluster connected by a Voltaire InfiniBand network. In June 2008, Roadrunner was reported to be the first computer to demonstrate a PFLOPS (P = peta) per second performance.

FLOPS is an acronym for Floating Point Operations Per Second and is measured using a benchmark application such as LINPACK. A hand calculator runs at about 10 FLOPS, and an Intel Quad-core QX9775 is reported to run at 51 GFLOPS. By comparison, a petaFLOPS is 1015 FLOPS, and one million GFLOPS. The highest-performing computer system in terms of FLOPS is the Folding@Home distributed computing network, which recorded 4.1 PFLOPS.

![The Stratus Lockstep architecture has multiple redundant systems that are continuously updated.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1606.png)

**Figure 16.6. The Stratus Lockstep architecture has multiple redundant systems that are continuously updated.**

## Load balancing

Server farms utilize a form of clustering called *load balancing*. Load balancing is useful when a system is I/O limited and you want to scale your servers out (more servers) rather than up (a more powerful server). Servers can be added and removed upon demand. Load-balanced clustering makes no demands upon the network speed for either the incoming or the outgoing connections, nor does it require that a load be balanced equally.

In this system, a server, router, or director switch with middleware software routes incoming IP traffic so that the work is shared across a group of servers. If a server goes offline, then it is removed from the pool and work is sent to other computers. These solutions often utilize caching to buffer incoming network traffic at peak times.

Load-balancing systems can be of the following architectural types:

- **Round robin scheduling**. A table of IP addresses are sequentially loaded.
- **Bridge load balancing**. This is done with Layer 2 devices using a virtual IP address on a LAN. Traffic to the LAN is sent to the virtual address and then forwarded to the servers that can process the request.
- **Routed load balancing**. This form of load balancing adds intelligence to the way in which servers are loaded. Typically these are Layer 3 devices, and they serve as firewalls or proxy servers spanning two subnets.

Examples of router load-balancing hardware solutions are:

- F5's BIG-IP (`www.f5.com`)
- Citrix NetScaler MPX (`www.citrix.com/english/ps2/products/product.asp?contentID=21679`)
- Coyote Point Systems Equalizer (`www.coyotepoint.com`)

An example of load balancing done in software is the load-balancing module that is built into Windows Server 2003 and 2008. Nearly every network server operating system that you have read about in this chapter ships with load-balancing modules. Examples of load-balancing software are:

- Balance (`www.inlab.de/balance.html`)
- Queue (`www.gnu.org/software/gnu-queue/`)
- Linux Virtual Server (`www.linuxvirtualserver.org/`)

Any network service is a candidate for load balancing. That includes DNS, DHCP, FTP, NNTP servers, and others. Web servers are an example of applications used in load-balanced server farm applications. Load balancers on IP networks work by listening to ports for the traffic type that is being balanced, and then forwarding the request to the backend server. Essentially they act like intelligent routers, and they are transparent to the traffic that flows through them. [Figure 16.7](ch16.html#load-balanced_clusters_optimize_server_u) shows a load-balancing solution.

![Load-balanced clusters optimize server utilization by sharing the workload to a server farm over a network.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1607.png)

**Figure 16.7. Load-balanced clusters optimize server utilization by sharing the workload to a server farm over a network.**

Edge computing is a form of distributed load balancing that is done to push content out to geographically distributed sites. Distributed content servers distribute content to geographically close systems on the Internet, and often those content servers are configured to be mirror sites of the original. Akamai (`www.akamai.com`) pioneered this category of Web service and provides their mirroring and routing servers to serve customer content. Typically edge servers don't work well with dynamic content, as coordination and replication become too difficult. Vendors typically offer QoS services and performance guarantees, and these services are mature enough that they are cost effective for businesses of all sizes. Depending upon the vendor and their network topology, edge systems can also be grid or mesh systems.

## Grid systems

Grid systems are distributed systems of networked computers where the workload is shared amongst the members of the grid. In grid computing, the network can be the Internet, the connection can be slow, and the protocols can be standard Internet protocols. They are called *grid* systems because they were designed to function like a utility, providing computing power on demand. They are also called *mesh networks*. Grid computing can use a client-server model, an n-tiered model, or a peer-to-peer model, depending upon how the organized software is deployed.

Grid computing has the following advantages:

- It improves utilization rates and lessens they need to build rarely used additional capacity.
- It can create the equivalent of a supercomputer at a fraction of the price.
- It can serve the goal of interested communities.
- It could be the basis for pervasive computing where services are always on and universally available.

If enough computers are part of the grid, then even if only a fraction of these computers are working on a project at any one time, the net result can be equivalent to the largest supercomputers available today. Indeed, several grid computer systems are among the highest-performing systems in use today. Folding@home is a 4 PFLOPS system based at Stanford that is four times more powerful than the fastest supercomputer that has been created. It is used to solve protein-folding configurations.

It is a little bit of a misnomer to call a grid computer a computer; they are really virtual computer systems and their work is coordinated by a server or servers, depending upon the number of member systems. Grid systems have performed some very important work in biochemistry, economics, astronomy, and many other fields.

Many grid systems offer clients on several platforms, and their software only runs when the client computer is idle. The use of idle computer cycles is referred to as *CPU-* or *cycle-scavenging*, and other less genteel names.

SETI@home is another volunteer community of computers that is based out of the Space Sciences Laboratory at the University of California at Berkeley. SETI stands for Search for Extra Terrestrial Intelligence, and the grid aids in the search for little green men from outer space. The client software has been used on 5.2 million computers (about 300,000 active clients in over 200 countries) and runs as a screen saver (see [Figure 16.8](ch16.html#the_seti_at_the_rate_home_screen_saver)). With an aggregate of two million years of computer time, SETI@home is the largest computation project in history according to Guinness World Records. The SETI project created the Berkeley Open Infrastructure for Network Computing (BOINC), one of the largest volunteer grid systems in use.

Grid systems are the focus of a lot of industry effort as vendors evolve desktop software into applications that run on the "cloud." There's little difference between a cloud system and a grid system; both terms imply a remote service on demand. National grid systems are currently being developed and are in the prototype stage. The European Union is sponsoring a grid for physics, biology, and earth science research. A National Technology Grid is being built in the United States to test the concept of a public, on-demand computation utility.

![The SETI@home screen saver](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1608.png)

**Figure 16.8. The SETI@home screen saver**

Cloud computing is being enabled by a wide variety of network operating system vendors under initiatives such as Software as a Service (SaaS), Service Oriented Architecture (SOA), the Microsoft .NET Framework, and Web 2.0 applications, among others.

Sun offers software called the Sun Grid Engine (`www.sun.com/software/gridware`), or SGE, which is an open source batch queuing system that is deployed on a computer cluster or computer farm. Grid deployments of these types have much in common with load-balancing solutions. The Sun Grid utility computer system was built on SGE. A commercial product called the Sun N1 Grid Engine (N1GE) is also offered by Sun, which describes this technology as Distributed Resource Management (DRM) software.

# Summary

In this chapter, you learned about high-performance networked computer systems. Powerful systems tend to use high-speed networks, while distributed systems can use standard network types.

Ethernet is so widely used that any new Ethernet standard tends to be deployed widely. Currently available 10 GbE is used with high-speed servers and switches. Faster standards are currently under development.

To address processor overload, a number of network offload techniques have been developed. You looked at the TCP Offload Engine (TOE) and zero copy networks. The Virtual Interface Architecture (VIA) and the InfiniBand peripheral bus are the zero copy networks that you examined.

Networked cluster computers were described. Three types are used to provide failover, load-balanced solutions, and utility computing. Grid computing and cloud computing were briefly examined.

The next chapter begins a new section on TCP/IP networks. You also learn about the TCP transport protocol.
