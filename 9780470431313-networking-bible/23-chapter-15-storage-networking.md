# Chapter 15. Storage Networking

**IN THIS CHAPTER**

- The need for storage networks
- Different types of SANs
- Models for shared network storage
- Storage devices and services
- Fibre Channel storage networks
- Storage over IP technologies

Storage networks use a collection of technologies that share storage assets on the network. Storage I/O can represent a very large amount of data traffic, so there is a strong incentive to isolate storage traffic on its own dedicated network. This has led to the development of Storage Area Networks (SANs). Hubs, switches, routers, servers, disk arrays, tape libraries, and optical jukeboxes are among the many devices that you will find on a SAN. Storage network topologies can be direct attached, point-to-point, arbitrated loops, and fabrics.

A model is described that categorizes the architecture of shared network storage. This model naturally separates storage servers into block-oriented or file-oriented solutions. The model is extended for tape devices, and it will be shown how different network backups can be accommodated by the model, and how devices would be configured for these different scenarios.

The concepts behind separating physical disks from logical addresses are described. This separation allows storage to be easily virtualized. Aggregation is used to reassemble the data stored on disk into files and information that applications can use.

Fibre Channel is the dominant media connection technology used to create SANs. The Fibre Channel protocol, architecture, and components are described in this chapter. Fibre Channel networks were originally configured using a Fibre Channel Arbitrated Loop (FC-AL) topology, but most deployments are now in the form of a Fibre Channel Switched fabric (FC-SW) topology. The use of Fibre Channel switches and routers and their different types of ports are described. Elements in SANs, such as individual network interfaces and hard drives, are individually addressable, and elements can be both grouped and isolated by the zoning techniques you learn about here.

A number of technologies are being deployed to allow storage traffic to be sent over IP networks. Among those that are described in this chapter are Internet Small Computer System Interface (iSCSI), Fibre Channel over IP (FCIP), and Internet Fibre Channel Protocol (iFCP).

# Storage Networking

Many companies spend more than half of their technology budget on data storage. Queries to databases, backup and recovery operations, replication and mirroring, and the dozens of other important applications that require storage access lead to the situation where the bulk of network traffic is storage related. To alleviate the load placed on networks, storage traffic is often isolated on its own dedicated network, called a Storage Area Network (SAN). The term SAN may be applied to any network that isolates storage from other types of network traffic, regardless of the technology, topology, or protocols used.

### Note

IBM used the acronym SAN for the term "System Area Network," but this term has fallen out of favor and is used only infrequently.

The central importance of storage networks can be summed up by this one fact: If you consider that enterprise-class storage servers, such as an EMC Symmetrix DMX-4, can hold up to 2,400 1-TB hard disks (or 2.4 petabytes of storage), then each of these systems fully loaded often costs more than the buildings that they are housed in. No wonder there's such an incentive to share these resources effectively.

Some of the devices you find on SANs include the following:

- Hubs, switches, and routers
- Storage servers and disk arrays
- Tape libraries
- Optical jukeboxes
- Virtual devices such as Logical Unit Numbers (LUNs), which are SCSI protocol identifiers for a defined storage asset

SANs are most often built using Fibre Channel switches and hubs, and linked by either optical or coaxial cable connections. The spelling "Fibre" is correct; it denotes an architecture or topology, and not the use of thin wires, as is the case with fiber optics. SANs implement a fabric architecture that allows storage assets to connect to other storage assets over multiple pathways. Fibre Channel has its own set of protocols, addressing, vocabulary, and construction apart from other networking standards that you have learned about, such as TCP/IP. Storage assets are accessed by workstations and servers on Local Area Networks (LANs) through common interface devices.

Storage networking is a very dynamic area of technology, one in which there is always something new. Storage network connections can encapsulate storage data arising on a Fibre Channel network inside TCP packets, and then send or receive that traffic across Wide Area Network (WAN) connections. Alternatively, efforts to extend locally attached storage onto the network have led to SCSI bus commands and data encapsulated over TCP/IP, making the iSCSI protocol a very valuable method for sharing storage on LANs.

In this chapter, you learn about some of the more important storage networking terms and concepts, and how to apply them to your networks.

# Storage Network Types

Storage can be deployed in a number of different ways. Each type of storage offers the opportunity to share that storage asset with other networked computers.

The simplest shared network storage is created with an internal storage device, which is sometimes referred to as "captive disk." Storage that is internally connected to a host by a computer bus is referred to in the storage industry as Direct Attached Storage, or DAS. SCSI is most often used for a high-performance bus standard to captive disk.

These days, Universal Serial Bus (USB), FireWire, and external SATA (eSATA) are ubiquitous for connecting storage to desktop systems; higher-performance workstations and small servers tend to use SCSI or other higher-performance buses. In markets where storage capacity and price are more important than performance, SATA, or Serial ATA, storage is displacing SCSI at all levels of deployment, from desktops to enterprise-class storage servers. Small storage subsystems, such as external RAID arrays, are often connected to hosts using a direct point-to-point topology. Fibre Channel Point-to-Point (FC-P2P) is a single connection between two devices.

To form a network using low-level SCSI commands and data communication, that protocol must be transported over another transport protocol. The most widely used transport protocol is the Fibre Channel Protocol(FCP), which is described in detail later in this chapter. FCP is the transport of SCSI over TCP, which defines Fibre Channel networks. There are many other protocols in use that provide transport over IP networks, including:

- **ATA over Ethernet** (rarely used).
- **Fibre Channel over Ethernet (FCoE)**.
- **FICON over FC**. This protocol isn't used on SANs, but is used with IBM mainframes.
- **HyperSCSI**, a version of SCSI over Ethernet.
- **iFCP and SANoIP**, which transports FCP over IP.
- **iSCSI, or SCSI over TCP/IP**. iSCSI is described later in this chapter. A version of iSCSI for RDMA (ISER) transports iSCSI over the InfiniBand (IB) protocol. IB is described in [Chapter 13](ch13.html).

Both DAS and P2P topologies share these storage assets by creating disk or file shares within the host's operating system. The performance limits are set by the network connection (usually Ethernet), the computer bus bandwidth, and the host system's ability to process requests for storage access from other networked systems. DAS and P2P topologies are a bus architecture, and wouldn't be classified as a network.

When you have multiple Network Interface Cards (NICs) installed in a host, or dual-homed Fibre Channel NICs, you can create loop topologies. This is the architecture that IBM uses for its Token Ring networks. Dual-home Fibre Channel host bus adapters (HBAs) can create loops with up to 127 logical devices, called Fibre Channel Arbitrated Loops (FC-AL). FC-AL, once the dominant storage network topology, is now consigned to the connections in disk arrays.

The final topology in wide use in storage networks is called a switched fabric. Switched fabrics are created using either Fibre Channel or Gigabit Ethernet and offer many of the advantages of switched architecture in LANs and WANs. The main advantage is intelligent routing, but other important advantages include redundant pathways, interchangeable parts, and other factors that are described in more detail later in this chapter. Most SANs are constructed using a Fibre Channel Switched fabric (FC-SW) topology.

[Figure 15.1](ch15.html#the_four_main_storage_topologies) shows the four common storage topologies in use today.

![The four main storage topologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1501.png)

**Figure 15.1. The four main storage topologies**

# SANs versus NAS

SANs were first developed to support particular applications such as a data warehouse with a few storage assets organized into a group. These early SANs were referred to as "SAN islands." As it became necessary to link these various islands together, Storage Area Networks were conceived as federated systems and executed. Many of the standards described in this chapter were developed in industry groups such as the Storage Networking Industry Association (SNIA, `www.snia.org`) and the Fibre Channel Industry Association, or FCIA (`www.fibrechannel.org`).

A SAN can be as simple as a switch, two or more HBAs, and the cabling necessary to connect servers and storage. Several companies, including QLogic and Hewlett-Packard, offer what is called a "SAN in a Box," a kit that includes these components and SAN management software.

One storage system that isn't found on a SAN under normal circumstances is Network Attached Storage (NAS). NAS is best classified as a file server and is normally connected to LANs using TCP/IP. NAS uses file protocols such as NFS or SMB/CIFS transported over TCP/IP for communication. By contrast, SANs use block-oriented protocols. That is a broad difference, and in the majority of cases it does separate NAS from SANs. However, some vendors have created systems that are hybrids of SAN and NAS (and in rare cases, DAS) — NAS gateway systems like the EMC Celerra for SANs exist — and so it can sometimes be hard to tell which classification the device is in. A filer or file server without the server part (the storage) is called a NAS Head, and those may well be attached to SANs, as is described a little later in this chapter.

## Business Continuance Volumes

There are some applications that Storage Area Networks absolutely excel at, and for which they are invaluable. Backup and replication are the two applications that most often come to mind. Not only do SANs allow organizations to share storage assets, but they also provide the means necessary to make storage data highly fault-tolerant in a very effective way. If you have an application that is mission-critical, as many are in this 24/7 age of the Internet, you create fault tolerance by providing the means to fail over to a redundant system.

Take, for example, EMC's Business Continuance Volume (BCV) concept. A BCV is a copy of an active storage system that represents a point in time. If you want to work with the data you have, but you don't want to burden a mission-critical system, you create a BCV and then disconnect it from the primary system. The BCV is taken off-line and then connected to a different non-critical server where it can be:

- Backed up without affecting your production system or network
- Analyzed by an application such as a data warehouse analysis without impacting your primary server
- Optimized to reduce data redundancy or eliminate unnecessary data to streamline the data set
- Used as a fast secondary data system should the primary system go down, with a speed that is dependent only upon how long it takes to detach the primary storage and reattach to the BCV

BCVs can have many other uses, but the ability to remove network overhead makes the technology very attractive. EMC differentiates two different types of BCVs: a clone BCV created using mirroring and a snapshot BCV that uses a copy-on-write algorithm to propagate production changes incrementally. Snapshots are valuable in creating a historical record of file changes but are limited by the size of the storage resource that stores them.

## Storage virtualization

A fundamental concept in network storage is storage virtualization, the idea that physical storage is separated from logical storage by the creation of a mapping technology. Mapping at the block level may be done through the creation of a master index, whereas in the file system or database it may be done at the index, file, or record level. Wherever the mapping is done, in hardware or in software, storage is always virtualized.

Storage virtualization abstracts identity from location; you can think of it as a form of redirection. In a block-oriented server, a set of blocks may be assigned a logical unit identifier, or LUN. Each individual block is then given an offset number that identifies that block within the LUN, and the offset is called a Logical Block Address, or LBA. The offset refers to the point in the sequence of blocks in the LUN where the block is found. The complete storage map defines a name space, which for block devices is called a virtual disk, or vdisk.

Each LUN is mounted by and presented to the storage network by the storage controller. A storage controller can be a hardware device in the Host Bus Adapter (HBA), or it can be software farther up the network stack. A Host Bus Adapter is a network interface device that connects a computer to either a network or storage device; HBAs for SCSI, Fibre Channel, and eSATA are common. HBA is less commonly applied to a USB, FireWire, IDE, and even Ethernet adapters. LUNs themselves can be the result of a mapping operation, thus allowing even more flexibility. Disk virtualization can be done in software, at the operating system level, or in hardware where a mapping table stores the necessary metadata needed to perform storage I/O redirection.

Virtualization can be a very powerful feature, enabling storage to be more centrally managed from fewer consoles. In a fully implemented, heterogeneous, virtualized shared storage network, it is possible to perform live data migrations of storage data from one server to another, all the while taking and fulfilling requests for data access from different hosts. This feature can be invaluable in terms of several issues, including the following:

- Dynamic resizing of volumes
- Network application optimization
- Replication
- Mirroring (synchronous and asynchronous)
- Point-in-time snapshots
- Disaster recovery
- Capacity management
- Performance tuning, which involves moving higher-demand data to faster storage, and improving disk utilization

Virtualization enables what is called "thin provisioning," thus allowing storage to be an on-demand asset that can be supplied in small quantities when needed. Virtualization also makes it easier to enforce an Information Lifecycle Management policy where business rules are applied to where data should reside. The downside of storage virtualization is that it is often hard to implement as a multivendor, multiplatform solution and can be hard to install and complex to manage.

Storage virtualization software is most often positioned at:

- **Hosts**. The software can be contained in the operating system as a volume manager with a kernel-level device driver, as a file system (CIFS/NFS), or though an automounter such as `AUTOFS`. Examples in this category are the Windows Logical Disk Manager, LVM in UNIX and Linux, Symantec VERITAS Storage Foundation (for Windows or Solaris), NetApp MultiStore/FlexVol, and FalconStor Software's IpStor NSS VA.
- **Storage devices**. The storage controller provides RAID and storage pooling, stores metadata, and migrates and replicates data. The storage controller virtualizes the HBAs in the hosts that connect to it.
- **Network services**. Specialized network servers can provide virtualization by performing what is essentially a low-level I/O redirection or routing function. These servers sit in a layer between storage and hosts at the network level, and all storage communication flows through the server. The application that runs on the server performs the mapping function. Examples of this type of technology are Coraid VS21 EtherDrive VirtualStorage, EMC Invista, LSI StorAge SVM, and FalconStor Software IPStor NSS.
- **Switches or appliances**. These devices contain software that aggregates storage as part of their redirection mechanism.Virtualization devices can be in-band or symmetric, in which case they are in the data path between the host and the storage device, which usually means it is part of, but at the edge of, the storage network. Because in-band appliances are in the data path, they often provide caching functionality as a performance enhancement.Virtualization appliances or switches can also be out-of-band or asymmetric, which means that they are not in the data path. Out-of-band appliances used to direct storage I/O in SANs are located in the hosts' Ethernet network and are typically lower-performing solutions than in-band solutions. Caching is not possible in out-of-band virtualization.

Cisco has a feature built into their Fibre Channel switches that they call Virtual Storage Area Networks, or VSANs, which are now an ANSI standard. The technology can link a set of ports on multiple switches to create a virtual fabric architecture. Different ports on a switch can be assigned to different VSANs, or multiple switches can be bound to one or more ports to define a unique VSAN. VSANs were designed to be similar to the Virtual LAN architecture that is used on Ethernet networks.

A VSAN doesn't specify the network protocol that is used; it is a network layer assignment. It is possible to create VSANs that can use the Fiber Channel Protocol (FCP), Fibre Channel over IP (FCIP), IBM's Fiber Connectivity (FICON), and the iSCSI Transport protocols, and isolate traffic in the supported Transport protocol to the VSAN. VSANs contain different management services that include zoning (described later in this chapter), device accounts, security policy definitions, and the World Wide Name, or WWN, service. One particularly nice feature of a VSAN is that you can resize a VSAN by either adding or subtracting ports from it, instead of having to actually add or remove physical switches from a Fibre Channel network.

# The Shared Storage Networking Model

It is useful to have a framework within which to discuss how storage area networks are constructed, and what categories the different components, protocols, hardware, and software products fit. To this end, the Storage Networking Industry Association, or SNIA (`www.snia.org`), set about defining a unified theoretical model for storage networks along the lines of the seven-layer ISO/OSI or the alternative TCP/IP networking models. This model was created between 2000 and 2003 by Wayne Rickard, John Wilkes, David Black, and Harald Skadal, along with input from other SNIA members, and has become known at the SNIA Shared Storage Networking Architecture model. [Figure 15.2](ch15.html#the_snia_shared_storage_networking_archi) shows the last published version of the SNIA model.

![The SNIA Shared Storage Networking Architecture model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1502.png)

**Figure 15.2. The SNIA Shared Storage Networking Architecture model**

The SNIA shared storage model defines services, layers, and, most importantly, interfaces that storage devices must contain in order to be operable. For a completely functional storage request to be serviced, the request from an application must travel along one of the five different paths that are shown in [Figure 15.2](ch15.html#the_snia_shared_storage_networking_archi). You can use this model to describe how a device operates, and what type of device it must be, based upon the path it takes.

## The shared tape extension

A significant portion of shared network data resides on tape-managed robotic auto-loading tape libraries (also called tape silos or tape jukeboxes), where they often serve as backups or archival storage in organizations as diverse as the Internal Revenue Service, airline reservation systems, credit card data warehouses, and other large data stores. These libraries can contain hundreds of tape heads (streamers) accessing thousands of tape cartridges that store petabytes of data. The low cost of data storage on tape offsets the slower performance that these systems offer.

Tape is a serial medium where data must be accessed sequentially. This makes random access operations slow. However, when data is streamed in sequence, the throughput of tape is high.

Tape contents are described in terms of a unit called a tape image. A single tape can hold multiple tape images that are delineated by small separator sections, which also mark the position on the tape. Just like disks, tapes must be formatted in order to be read correctly by the tape head(s). There are many ways to write data to tape; some are linear, others are linear and serpentine, many are multi-track, some are helical, and most are proprietary. All these methods share a common structural organization that is illustrated in [Figure 15.3](ch15.html#a_logical_tape_structure).

In [Figure 15.3](ch15.html#a_logical_tape_structure) tape is spooled on the roll on the right and moves left to right onto the spool on the left. As the tape passes over the tape magnetic heads, one head reads data and another tape writes data. Tape images are broken up into a sequence of tape blocks called extents, and the tape almost always writes a header and sometimes writes a trailer section as part of the formatting and record-keeping operations. Extents are separated from one another by a gap called an *Extent separator*. When a portion of the tape image must be read, the `READ` head reads the table of contents in the Header and then moves the tape to the position where the data begins. When data needs to be written, the new data is appended to the end of the tape; the tape moves back to the Header table of contents and adds the changes.

Tape is serial data storage. It is very slow to read data from tape because of the mechanical transport speed, although writing data can be speedy. The advantage that tape offers is that it allows for massive amounts of storage at low prices.

In the Shared Storage Model, tape systems span all levels of the model, beginning at the top in the Application layer, as shown in [Figure 15.2](ch15.html#the_snia_shared_storage_networking_archi). A common application is backup software; many industrial-strength backup programs — such as CommValut Systems Galaxy, Computer Associates ARCserve Backup, EMC Legato Networker, HP OpenView Storage Data Protector and Archive Backup System (ABS), IBM Tivoli Storage Manager (TSM), and Symantec NetBackup (formerly VERITAS NetBackup) — either support tape devices natively (mainly smaller units) or provide modules at extra cost to support enterprise-class tape systems.

![A logical tape structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1503.png)

**Figure 15.3. A logical tape structure**

The tape format system spans the levels of the model from the application down to the host. The format operation is responsible for packing files or records into the tape extents and laying down those extents to record tape images. An open system tape solution is characterized by the tape format and all other host functions being isolated in the tape application software.

A tape is not a disk, and there isn't a direct correlation between a volume on a disk and an image on a tape. Tape is sequential, and the unit of aggregation is extents and not blocks. In the tape model, aggregation is contained in the host/network/device layers. Notice also that the model splits tape devices from tape media. This is required because tape is a removable media and would be required had this model been extended to optical jukeboxes that use removable CDs or DVDs. The split is doubly important for tape libraries because the tape heads and tape cartridge types can be mixed and matched as needed for each situation.

Different tape operation types are indicated in the tape model by arrow-headed lines in [Figure 15.4](ch15.html#the_tape_shared_storage_model). The arrow on the left in the tape section that goes through the tape format system, host, and extent aggregation corresponds to the operation of writing the file data to tape. A typical tape application that used this pathway would be the `TAR` command which READs data from disk. TAR is the UNIX tape archive command. That same left arrow in the tape section serves as the `WRITE` path for the `DUMP` command, which `READ`s the files in a file system that is written to the tape. The model concentrates on the tasks that get done, rather than the devices that do them.

![The Tape Shared Storage Model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1504.png)

**Figure 15.4. The Tape Shared Storage Model**

In the last scenario, the `TAR` command backs up files to virtual tape by first `READ`ing the data on disk and then passing the data to the backup software. The backup software then hands the data to the Tape Format system, which converts the data into tape format and passes the sequential data to the host, which then writes the virtual tape to disk.

The middle arrow that goes directly from the backup software through the network to the tape device is the `WRITE` to tape operation that takes as its input the `DD` command. `DD` performs a `READ` operation that performs a volume copy to tape.

[Figure 15.5](ch15.html#different_backup_commands_shown_in_the_s) shows these different backup scenarios.

Having now seen how network backup commands are processed to and from tape, let's take a brief look at how this architectural model uses devices. In [Figure 15.6](ch15.html#six_tape_backup_technologies), six different tape backup technologies are shown; the explanation that follows considers these examples, starting in the upper-left corner.

The simplest example is of direct attached tape backup, where data is copied from disk to tape over a system bus. Both that example and the network attached tape backup in the top center (where the disk and tape are externalized over a network) are backups where the bus or network spans all of the layers of the tape model. The same host bus is used for commands and for data transfer from a disk array to a tape library. In both instances, aggregation is host-based using the host file system.

![Different backup commands shown in the Shared Tape model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1505.png)

**Figure 15.5. Different backup commands shown in the Shared Tape model**

The simplest and perhaps most important backup deployment using a SAN is the one you see in the top-right corner of [Figure 15.5](ch15.html#different_backup_commands_shown_in_the_s), which is labeled Shared Tape Backup. This architecture enables what has come to be called LAN-Free Backup; commands go to the different devices from hosts, but backup traffic only flows through the storage network and not over the LAN. In this example, the tape library is shown as a single device, but many deployments of this type will partition the tape library so that multiple backups are occurring at the same time, and the backup software on different hosts is controlling different robotic tape selectors and drives.

Tape can be virtualized through the use of emulation and redirection. In the scenario shown in the lower-left example, labeled Virtual Tape Backup, a tape virtualization appliance is deployed in the data path, and from the standpoint of a host, the appliance appears as if it is a tape device. The abstraction allows a host to create a backup job and then pass that job along to the appliance for processing. The advantage of this approach over Direct Attached Tape is that the offload allows the host to work on other business. When a host is removed from the backup scenario, as is the case here, it is referred to as Server-Free Backup.

The fifth scenario is called the Tape Data Mover, shown in the lower center example in [Figure 15.6](ch15.html#six_tape_backup_technologies). The data is stored on a disk array, but an application requires the data be moved to a captive disk. Two movement appliances are deployed, one in each of the two data paths. The arrow with a dotted line indicates that the host gives the appliance commands, at which point the movement appliance processes the remainder of the job. The first job uses the data path that takes the data in its stored location on the disk array and moves the data through the first data appliance to an interim position on tape in a tape library. The second job copies the staged data from the tape library through the second movement appliance to the intended target, which is the captive disk. The Tape Data Mover scenario shares the great benefit offered by the Shared Tape Backup scenario: it is a LAN-free backup. To that benefit is added the offload of the backup management to the movement appliances.

![Six tape backup technologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1506.png)

**Figure 15.6. Six tape backup technologies**

The last scenario is shown in the lower-right example in [Figure 15.6](ch15.html#six_tape_backup_technologies) and illustrates a file server backup architecture with a data mover. The technology employed to control the backup is referred to as an NDMP 3-way backup. NDMP stands for Network Data Management Protocol, and it is a technology used by NetApp and Legato (now owned by EMC) to transport data directly to backup devices using a file server or NAS as the controller. NDMP is supported by nearly all enterprise-class backup software. The aggregation takes place in the NAS head, which receives NDMP commands from the host. The white, double-headed arrow between the movement appliance and the NAS head represents commands for working with blocks on the disk array.

## The Storage Domain

In the shared storage network model, the Storage Domain is a container that organizes information in the form of files. Files are pointers to information contained on disk, organized through the use of fields, records, and metadata that provide the necessary context to understand what the data is used for and how to use it. Metadata might include the datatype, the associated application needed to view and edit the data, sequencing, and other properties that make data into useable information.

At the top of the Storage Domain, the file/record layer provides the logic necessary to package information so that it can be stored in a useful way. In many instances, the amount of data is larger than the physical units in storage that are allocated; storage is allocated into blocks on disk. The file system or database must be able to segment the information into storable pieces that can be retrieved and sequenced when required. Often file systems and databases are united into a single structure. The file system or database uses a name space or object hierarchy that permits search and retrieval operations.

Not shown in the model is an object or file cache that is used to speed up performance in the system by storing the most recently used items in memory. All storage systems use different level caches to improve performance. The use of a cache makes it absolutely mandatory that a storage system contain the logic needed to determine whether data moving from or to storage is transmitted or sequenced correctly, and if the rules that were developed to maintain data integrity were followed. These rules of logic are called system coherency, and because cache information can either be newer than or older than stored data on disk, it is essential that the coherency logic be robust.

This differentiation between information in the form of files and records, and data in the form of blocks, is an essential defining concept in the shared storage model.

Data is stored at the lowest level, the Block layer. A block contains data but has no context describing the data. Blocks are merely addressable locations on a storage device such as a hard drive, Solid State Disk (SSD), optical disk, or tape. Blocks can be written, overwritten, erased, and moved, and their order bears no relationship to anything that a person or computer program would find useful. To be able to use the data that is in blocks, there needs to be a method to aggregate the blocks. Data aggregation supplies the critical lookup table that contains the pointers that map blocks to an organizational scheme.

## Aggregation

A file system or database can use information contained in blocks because they store information about which files or records correspond to which pointers in the block-oriented device, and in what order. That provides the means necessary to retrieve the information. From the standpoint of the file system or database, it is of no consequence where the physical data is stored. The system of mappings from file to pointer to storage allows the system to redirect the pointer's reference to a different block or an entirely different storage device.

This abstraction that aggregation provides is at the heart of a set of storage virtualization technologies that are critical in providing the flexibility needed to make storage networking practical. RAID, logical units and volumes, and volume manager software are all possible because of this mapping.

Not all storage operations require that data be presented in the form of usable information. In fact, the majority of operations only require that the data be handled without modification. When you back up one disk to another disk or one volume to another volume, the knowledge of which file uses which block (and vice versa) is needless overhead and is ignored. Enterprise backup and replication technologies ignore file structures and perform these operations at the block level, copying data from one location to another sector by sector, and block by block. Error-checking techniques determine whether the operations were successfully performed, but for the most part, the server or host that uses the data doesn't need to be involved in these operations. Most block-level operations are implemented by the storage systems themselves.

The bottom line is this: If you want fast data operations, you need to invest in block-oriented technologies. If you need to manage information, then you need file-oriented systems.

## Device models

The Shared Storage Model shown in [Figure 15.2](ch15.html#the_snia_shared_storage_networking_archi) shows five different paths requesting data contained in storage from the Application layer. There are actually eight paths through the four different interfaces that the model creates that can be defined; the ones shown are the most useful in terms of discussing device classes that you can buy and install.

The four interfaces in the model are:

- **Application/Operating System Layer**. This layer is usually defined by an API necessary to connect the services that both layers contain.
- **Operating System/File and Record Layer**. Another API is used to tie the operating system to information.
- **File Layer/Block Layer**. This interface is where the storage network protocols are used.
- **Block Layer/Storage Device**. This interface uses low-level bus commands like SCSI to manage data.

Interfaces, regardless of what one technology or vendor calls them, are important. When you use an open standard for an API at an interface, it provides you with a measure of supplier independence that you don't have when you use one storage vendor's proprietary API.

Block-oriented storage devices typify the classic concepts embodied in a Storage Area Network model, and can occupy as many as three of the bottom layers of the model. The block layer storage device does much of the heavy lifting when it comes to storage operations. Storage devices get commands from hosts and then independently carry out those operations. Among the operations that a block-oriented server can perform are direct device-to-device block transfers used for backups, copies, and transfers; replications; mirroring; and any other application that requires storage I/O. Intelligence built into the storage servers improves performance by pre-caching contents, scrubbing disks, and performing storage maintenance.

[Figure 15.7](ch15.html#different_conceptual_block-oriented_stor) shows how block-oriented storage servers fit into the storage networking architectural model.

![Different conceptual block-oriented storage devices](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1507.png)

**Figure 15.7. Different conceptual block-oriented storage devices**

Block-oriented storage systems work well when the application passes the storage devices a command such as "copy this volume," "perform a backup," or even "make this small change to this large file." Any operation that doesn't require an understanding of how the data stored on disk relates to files or information is more efficiently handled as a block operation. If you make a small change to a database, which changes the data in one sector, a block operation only needs to change that sector. However, when a filer or file-oriented server changes the file, the whole file needs to be rewritten. There are situations where filers greatly outperform block storage servers.

File-oriented servers can be constructed in the Shared Storage model as a complete NAS file server, as a NAS head that fronts a disk array, or as a host device where the file system/database relies on an aggregation appliance to mediate storage data transactions. The three different device types, Network Attached Storage, disk arrays, and direct disk, are shown in [Figure 15.8](ch15.html#different_conceptual_file-oriented_stora).

![Different conceptual file-oriented storage devices (from left to right): Network Attached Storage, disk arrays, and direct disk.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1508.png)

**Figure 15.8. Different conceptual file-oriented storage devices (from left to right): Network Attached Storage, disk arrays, and direct disk.**

In a file-oriented storage system, there is a mapping function that relates volumes, blocks, and sectors to files or tables, records, and tuples. From the standpoint of a networked storage system, the organizational scheme of a file system, a database, or an object-oriented version of either two is irrelevant; it is the mapping function that is important. Network Attached Storage (NAS) devices such as a NetApp filer run the specialized Write Anywhere File Layout (WAFL) operating system, the Windows Storage Server 2003 R2, which runs Windows Server 2003 R2, and even a database-oriented appliance like the discontinued Oracle8i Appliance or the current Netezza Data Warehouse Appliance, work equally well as file-oriented servers. NAS spans all of the layers of the Shared Storage model, from network hosts down to captive disk.

The other types of file-oriented storage servers are created by disaggregating functionality from a NAS. If you remove the storage devices from a NAS server, what you are left with is called a NAS Head. A NAS Head has a file-oriented operating system, applications for managing volumes and RAID, and the I/O functionality necessary to send commands and receive data from a storage device. However, a NAS Head doesn't perform the basic storage operations. That function is abstracted away by a storage server connected to the same SAN that the NAS Head is connected to. From the standpoint of an application or host, a NAS Head is identical to a self-contained NAS server. NAS Heads are highly flexible appliances; they can attach to hosts via a LAN or be connected to a host with LVM (Logical Volume Manager) software directly.

The next disaggregation removes the specialized file-oriented operating system of a NAS and has the host work with storage devices directly either as captive disk or through a storage network to a disk array. In the case of a Direct Attached Storage filer, the host must be able to create logical volumes using a piece of software called a Logical Volume Manager (LVM), and possibly be able to stripe and mirror disks to create RAID arrays. The use of software RAID, either inside the operating system or through the use of third-party software such as the VERITAS Volume Manager, may not be required because many HBAs ship with hardware RAID built right onto the board. All disk arrays ship with hardware RAID, and so when a host is connected to a disk array, it only needs the LVM to perform file-oriented storage operations.

File-oriented storage servers work well when the application passes the storage devices a set of commands such as "`READ` these sets of files," "reindex this file system," or "take an incremental snapshot or backup of this volume." Any operation where the information isolates the storage locations and sequences of data based on files introduces efficiencies that block storage devices can't match.

The classic example of an efficient file-oriented storage application is in streaming media — the bigger the better. If the application makes a request for a single, large, streamed file, it passes a sequence of locations on disk to the storage device, which then executes the `READ`s necessary to make the file available to the application at the host.

A block-oriented storage system wouldn't know how to process the streamed file. It would retrieve the information in one block and then request the location of the next block from the master index, which maps the file using a set of pointers, each to the next location. As the data in sequential blocks are being reassembled, there is a stream of commands for the pointers that represent the next segment that creates a significant overhead and attendant performance degradation for streaming in block devices, particularly in multiuser scenarios.

However, the smaller the files requested and the greater their number, the less the performance difference there is between the file-oriented and block-oriented storage systems. The mapping operations become comparable in complexity, with the only difference being that the mapping is done at the filer or at the storage array. The latency introduced by the network may be seen to be much smaller for passing pointers or storage locations than it is for transferring the actual files back across the storage network/LAN to the applications.

# Fibre Channel Networks

Fibre Channel (FC) is a high-speed interconnect that was first deployed on supercomputers as the High Performance Parallel Interface (HPPI). HPPI has since been adapted and expanded to become FC, which has become the dominant standard for storage networking. FC is defined by a set of ANSI standards that specify not only the cabling types and connections used for the network's Physical layer, but also the Fibre Channel Protocol (FCP) as the Transport protocol. FCP is designed to encapsulate commands and data in different formats such as SCSI (the majority), ATM, and IP. Fibre Channel interconnects can be either copper or fiber optics (both single and multimode fiber).

Sometimes Fibre Channel networks are described in terms of class levels. Class levels describe the types of topologies and connections that are made. There are six classes of Fibre Channel networks in use:

- **Class 1** designates end-to-end connections with each frame verified. Class 1 doesn't use negotiation; each device in the point-to-point connection controls data flowing over the wire. Class 1 is not a shared storage network; it is a closed system.
- **Class 2** is a frame-switched connection that is used in shared fabric connections. Frame delivery is verified, but frame delivery need not be sequenced. The lack of sequencing means that Class 2 FC can't communicate using SCSI data, which requires sequential data flow. The iSCSI protocol provides a solution to sending SCSI over Fibre Channel, removing the need for vendors to provide a proprietary solution to this class in their switches, as some once did.
- **Class 3** offers frame switching, but without receipt acknowledgment at the switch. Frame acknowledgment is a host function in this class. Class 3 uses a buffer flow control mechanism. Class 3 FC also doesn't sequence frames, but does include a broadcast feature that can send simultaneous traffic to more than one device.
- **Class 4** provides fractional bandwidth allocation — a virtual circuit. Class 4 can share connections.
- **Class 5** proposes isochronous (same time) just-in-time service.
- **Class 6** is a multicast service that offers dedicated fabric connections.

## Fibre Channel standards

Some will argue that because the standard only requires that ports be able to communicate with one another and that the interconnect be a serial bus structure, that Fibre Channel doesn't represent a true network. However, for the purposes of this book and given the number of different devices that can be attached to FC, it makes sense to treat collections of devices connected by FC as a network.

[Table 15.1](ch15.html#fibre_channel_standards-024) lists the different Fibre Channel standards that have been introduced since the first ANSI standard in 1994. Products based on the 8 Gbits/s standard and before are compatible with one another. The newer standards of 10 Gbits/s and 20 Gbits/s are not backwards compatible. Among the manufacturers who make Fibre Channel HBAs are ATTO, Brocade, Emulex, LSI Logic, QLogic, and others. These HBAs are sometimes sold through OEM agreements and rebranded by system vendors.

Fibre Channel cables, connections, and connectors are passive devices. The signal is sent and received by a transceiver. Every connection or connector contains two transceivers, and data flows down each of the two wires or channels in opposite directions. This system eliminates problems that occur in network connections where the signal travels over the same wire. This is the case with Ethernet where you see data loss due to interference and signal contention because of two-way traffic; additional overhead is placed on the system to employ measures to combat the problem. With Fibre Channel, you have a measure of fault tolerance due to the use of a loop topology, and most Fibre Channel HBAs are dual homed for this reason.

**Table 15.1. Fibre Channel Standards**

| Standard | Speed (Gbits/s) | Throughput (Mbits/s) |
| --- | --- | --- |
| 10GFC Parallel | 12.8 | Varies by connected devices |
| 20GFC | 10.5 | 2,000 |
| 10GFC Serial | 10.5 | 1,000 |
| 8GFC | 8.5 | 800 |
| 4GFC | 4.25 | 400 |
| 2GFC | 2.1 | 200 |
| 1GFC | 1.1 | 100 |

## Port designations

In Fibre Channel, a port is any logical entity that can be assigned a network address and from which, and to which, communication flows. This includes not only HBAs, but also physical and logical storage devices and hosts, switches, and hubs. [Table 15.2](ch15.html#fibre_channel_ports) summarizes the different types of Fibre Channel ports in use.

**Table 15.2. Fibre Channel Ports**

| Port Identifier | Name | Type | Purpose |
| --- | --- | --- | --- |
| [[a]](#ftn.CHP-15-TFN-1) |  |  |  |
| E_port | Extender Port | Switch | Connects switches into a cascade. |
| EX_port | Expansion Port | Switch/Router | Connects an FC router to an FC switch. At the router, it emulates an E_port, and at the switch, it is an EX_port. |
| F_port | Fabric Port | Switch | Connects a fabric to a node. |
| FL_port | Fabric + Loop Port | Switch | Connects a switch port to both a loop and a switch. |
| Fx_port | Autosensing Port | Switch | Can become an F_port when connected to an N_port, or can become an FL_port when connected to an NL_port. |
| G_port | General Port | Switch | Can be used to emulate any other port, usually an E_port or F_port. |
| L_port | Loop Port | Node | Connects a node to an FC loop as an NL_port or FL_port. |
| N_port | Network Port | Node | Connects a node to a switch. |
| NL | Network + Loop Port | Node | Connects a node to both a loop and a switch. |
| TE_port | Trunking Expansion Port[[a]](ch15.html#ftn.CHP-15-TFN-1) | Switch | A Cisco VLAN standard for switch-to- switch connections that emulates an E_port. |
| U_port | Universal Port | Node | A term applied to any arbitrated port. |
| [[a]](#CHP-15-TFN-1)A trunk may also be called a Port Channel or an EISL, depending upon the vendor and device. |  |  |  |

## The Fibre Channel Protocol

The Fibre Channel Protocol uses a five-layer architecture that includes a low-level signaling layer and higher-level service layers, as shown in [Figure 15.9](ch15.html#the_fibre_channel_protocol_architecture). Layers FC-0 to FC-2 are collectively referred to as the Physical Layers and include both the media and wire protocols. Different devices can span different layers in this model. An FC hub operates at Layer FC-0 only. FC switches span the protocol from FC-0 to FC-2. An intelligent FC router spans the protocol from FC-0 all the way up to FC-4 because many FC routers also serve as SCSI routers.

![The Fibre Channel Protocol architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1509.png)

**Figure 15.9. The Fibre Channel Protocol architecture**

The different layers have the following purposes:

- **FC-0**. The Physical Layer (FC-0) includes the fiber cables, connectors, and the specification of electrical and optical parameters that the hardware requires. When optical fiber is used, FC-0 employs the Open Fibre Control (OFC) system to lower the power level of the laser used so that it doesn't overwhelm the FC ports in use.
- **FC-1**. The Data Link Layer (FC-1) encodes and decodes commands and data in 8-bit serial format into a 10-bit Transmission Character. The small bit sizes make it easier to send and recover a serial bit stream in case of error.
- **FC-2**. The Network Layer (FC-2) is the layer that manages data transport on an FC network. It controls the creation and management of frames, ordered sets, sequences, exchanges, and the Fibre Channel protocols. The protocols include Primitive Sequence, Fabric Login, N_Port Login, Data Transfer, and N_Port Logout.To manage frame traffic, FC-2 uses a flow control mechanism based on the available buffer space. Different service classes can be defined for different traffic types.
- **FC-3**. The Common Services Layer (FC-3) contains the mechanisms for managing N_port striping, allowing multiple ports to transmit data in parallel as a single information unit over multiple connections. It also supports a feature called hunt groups, where more than one port can respond to a single alias address. Hunt groups improve performance by providing access to a storage device that might be busy or blocked on another port. The third technology implemented at FC-3 is multicasting, which for FC represents the idea of sending data to more than one port at the same time. You could, for example, send data to all or any of a fabric's N_ports.
- **FC-4**. The Protocol Mapping Layer (FC-4) is an application interface layer that maps network protocols to the FC layers below FC-4. The network and bus structure supported are Small Computer System Interface (SCSI), Intelligent Peripheral Interface (IPI), High Performance Parallel Interface (HIPPI) Framing Protocol, Internet Protocol (IP), ATM Adaptation Layer for computer data (AAL5), Link Encapsulation (FC-LE), Single Byte Command Code Set Mapping (SBCCS), and IEEE 802.2.

### Fibre Channel traffic management

The Fibre Channel Protocol uses a form of traffic management based on buffer credits. Each port on the network is assigned a traffic budget. When that budget is used, data traffic is directed to the next port in the sequence. Buffer credits are defined for end-to-end flow control with N_ports, L_ports, or NL_ports serving as the endpoints. Ports acknowledge frame receipt and then an additional credit is given to the sending port, which is placed in the traffic queue. A second type of flow control, referred to as buffer-to-buffer control, manages a set of credits between two adjacent ports. Buffer-to-buffer traffic control relies on the receiving port sending a ready-to-receive signal to the sending port.

Fibre Channel Switched fabric (FC-SW) uses a different mechanism for flow control. Node and processes send their status to different ports as part of a logon ritual. As each node logs onto the FC-SW, the initiator and target ports authenticate the node logon and negotiate the connection properties, including the type of protocols used and the data transfer rates. FC-SW uses the FCP-SCSI protocol. This process logon authentication and negotiation occurs for any type of FC-SW connection, even those that use a direct attached Fibre Channel connection.

### Fibre Channel flow control

Fibre Channel frames have start and end markers. The header defines the frame and contains addresses, data, error correction, and a validation data set that performs acknowledgment as well as data recovery. Frames encapsulate data in other wire protocols so that a Fibre Channel frame maps to other upper-level protocols such as SCSI, IP, HIPPI, FICON, ESCON, 802.2, and Virtual Interface Architecture (VIA). [Figure 15.10](ch15.html#fibre_channel_frames) shows the structure of an FC frame.

![Fibre Channel frames](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1510.png)

**Figure 15.10. Fibre Channel frames**

## Fibre Channel Arbitrated Loops

Fibre Channel Arbitrated Loops, or FC-AL, is a topology used to connect hosts with storage devices. It was once the predominant technology used for SANs, but is now mainly used to connect the many disks in large disk arrays with host controllers. An arbitrated loop is a serial bus that can address from as few as 2 to as many as 127 logical devices or ports. The FC-AL command set is compatible with SCSI bus commands. Unlike IBM's Token Ring, an FC-AL allows multiple devices to address the bus, up to the limit of the bus's bandwidth, which is shared by all of the connected devices. As shown in [Figure 15.11](ch15.html#fibre_channel_arbitrated_loop_nodes), FC-AL can connect to an FC switch, and through that switch, to switched fabric networks, as is indicated by the arbitrated loop on the right in [Figure 15.11](ch15.html#fibre_channel_arbitrated_loop_nodes).

![Fibre Channel Arbitrated Loop nodes](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1511.png)

**Figure 15.11. Fibre Channel Arbitrated Loop nodes**

### Note

While the theoretical limit of Fibre Channel is 127 devices, the practical limit is approximately 40 to 60 nodes.

The arbitration scheme used by an FC-AL is based on the SCSI bus arbitration scheme. In FC-AL, the port with the highest priority gets access to the wire to send and receive frames. SCSI uses a priority based on the bus electrical characteristics; with FC-AL, the priority is established in software as commands. This frees FC-AL to run on either copper wire or fiber optic wire.

An L_port or NL_port on an FC-AL starts communication by first issuing a ready-to-send command. As the command travels the loop, every node in turn compares its priority to the node that is requesting loop access, and then that node either takes the control command or passes the control command on. When the loop becomes available to the arbitrating port, data is exchanged and the priority changes. The next-higher priority node restarts the ready-to-send sequence and assumes command of the loop. Exchanges take place using a set of sequenced frame transfers, with frames typically in the rather small 2K range. The small size of the frame enables the communication to recover quickly from any loss because retransmission is not a lengthy process, which is essential in serial data communication.

Arbitrated loops can be constructed with either a ring or a hub (passive star). Rings are simpler to implement but have the disadvantage of failing when any device on the ring fails. Hubs still function when a device fails because each device is still on a logical ring while connected to the hub using a star topology.

FC-AL uses a subset of the different types of logical ports available. The Node Loop port (NL_port) and Fabric Loop port (FL_port) or L_ports are ports than can engage in arbitrated communication. NL_ports must be able to log onto a fabric and authenticate themselves if so connected. Name registration uses the Fabric Login (FLOGI) protocol. An NL_port would be the initiator for any communications to other nodes located on the fabric. An arbitrated loop that connects through an FL_port is considered a public loop, while an arbitrated NL_port that isn't connected to a fabric is considered to be a private loop. From the standpoint of the FC-AL protocols, a connection to a hub is not a port.

## Fibre Channel Switched fabrics

A Fibre Channel Switched fabric (FC-SW) network is one in which different devices on the network are connected to one another through intermediary intelligent Fibre Channel switches. Fabric topologies have many advantages, as you will see in [Chapter 17](ch17.html), when InfiniBand fabric and computer grid systems are described. Fabrics are scalable, fault tolerant, and flexible.

In order to implement an FC-SW, you require an FC switch, which, prior to 2003, tended to be expensive. The availability of lower-cost FC switches, as well as a drop in the per-port cost of the larger switches (called Fibre Channel Directors), have made FC-SW the dominant storage networking architecture. Brocade, Cisco, and QLogic are the best-known Fibre Channel Switch manufacturers, but there are many more. A Fibre Channel Director class switch is one that contains 128 ports or more.

### Fibre Channel addressing

An FC-SW has an address space with 224 logical addresses (16,777,216). When two or more switches are used in the same network, they can be configured so that they form a mesh network. Three different addressing schemes are used in FC-SW networks: the World Wide Name (WWN), port addresses, and Arbitrated Loop Physical Addresses (AL-PAs).

A WWN, which is sometimes referred to as a WWID, is assigned by IEEE convention to both Fibre Channel and Serial Attached SCSI storage devices. WWNs serves the same function on an FC-AL network that an Ethernet MAC address does on a TCP/IP network. There are two naming conventions in use for WWNs: one, called the WWNN, is the node WWN and applies to all ports on an HBA; the second is port WWN (WWPN) and is a unique port identifier.

WWNs use a manufacturer address assigned during fabrication. The address is composed of a hexadecimal prefix 10:00 or vendor prefix 2#:##, to which is added a 3-bit vendor ID, and a 3-byte serial number. The vendor prefix is called the Organizationally Unique Identifier (OUI). In the newer WWN naming scheme, the initial half-byte is a hexadecimal 5 or 6 to which is added the 3-bit vendor ID, and a 4 1/2-byte serial number.

Examples of some of the company identifiers are 00:60:69 for Brocade; 00:1B:32 for QLogic HBAs; 00:C0:DD for QLogic FC switches; 00:60:48 for EMC Symmetrix; 00:60:16 for EMC CLARiiON, 00:A0:98 for NetApp; and 00:50:76 for IBM, among others.

Port addresses are unique 24-bit addresses that are assigned to a port. This is similar to assigning an IP address to a network controller in a TCP/IP network. Assignment of port address numbers is determined by the person or organization that configures the FC SAN.

Arbitrated Loop Physical Address (AL-PA) is used on loop topologies to define an addressable and unique address. FC loops have a small number of nodes, and thus only an 8-bit identifier with 256 addresses is needed.

### Zoning

In an FC-AL storage network, you can implement a feature called zoning that segments storage assets in a manner that is similar to creating a subnet on an Ethernet network. There are four different types of zones supported by FC-AL fabrics:

- **Soft zoning**. When a soft zone is created, any host connected to the fabric will only be allowed to browse the names of the storage devices that the host has been allowed access to. Soft zoning only affects the browse function. Any host can still connect to any device if it provides the device address. So a soft zone is not a secure method for providing restricted storage access.NoteZoning is a feature of FC-AL networks and isn't implemented on the other types of Fibre Channel networks.
- **Hard zoning**. Hard zoning is a feature that not only restricts browsing for storage devices by name but also blocks traffic from a host to a storage device that the host doesn't have the privilege to connect to. Hard zoning is a secure method for controlling storage access and uses a frame filtering mechanism to determine the sending and receiving systems. Hard zoning is a feature of a Fibre Channel switch, and not all switches offer hard zoning.
- **Name zoning**. Every device on an FC-AL network is assigned a unique 8-byte World Wide Name (WWN). Name zoning is relatively secure, but can be spoofed.
- **Port zoning**. Zones can be created at the Fibre Channel switch port level so that ports on one switch are either allowed or denied access to ports on another switch. This feature requires switch support and usually that the two switches involved are from the same manufacturer.

The best security method uses a combination of zoning methods to secure storage network assets.

# Storage over IP

There is considerable effort under way to leverage IP network infrastructure for storage networking. To some extent, IP storage networking may displace some fraction of Fibre Channel storage networks, particularly in WAN links, small LAN deployments, and lower-performance LAN applications. In this section, you learn about three different emerging storage over IP technologies:

- **iSCSI**. iSCSI uses the SCSI command set and data format to send packets over an IP network. IP essentially extends the SCSI over a much greater distance, allowing a host with DAS to appear to other nodes on the network as if it is a shared network device.
- **Fibre Channel over IP (FCIP or FC/IP)**. FCIP is a tunneling protocol that encapsulates Fibre Channel frames within IP packets. FCIP is a point-to-point technology; the initiator and target encapsulate and de-encapsulate the packets to retrieve the FC frames.
- **iFCP**. iFCP adds Fibre Channel commands and data to IP packets and then sends the storage traffic as native transport over IP. It is very similar in concept to iSCSI in the sense that iFCP and iSCSI commands are wrapped by TCP for transport over IP networks. FCIP, by contrast, can only be used on Fibre Channel networks. IP packets are sent from an iFCP gateway to another iFCP gateway, and is routable; whereas FCIP is sent using a tunneling mechanism.

Storage networking and IP networking were built with two very different sets of requirements in mind. Storage networks were designed for throughput and reliable delivery. IP networks are fault tolerant, but were not designed for speed. Those differences control how any of these storage over IP protocols can be applied, as any application that is sensitive to IP networks' intrinsic latency isn't a good candidate for this storage over IP standard.

Data going from room to room may traverse one router or switch with one intervening "hop." Each hop introduces most of the latency encountered in TCP/IP networking. So a connection with one hop will probably operate satisfactorily for a high-performance connection, provided again that the bandwidth is sufficient. However, if the link must traverse a city, state, or country where the latency of multiple hops must be accommodated, then chances are that FCIP isn't going to be a satisfactory solution when connecting an OLTP database to networked storage.

You can't tell what the bandwidth of a link is without testing, and bandwidth is highly dependent on network conditions. You can, however, get some sense of the amount of latency that a small number of packets will have traveling the intended route of an FCIP connection, by simply performing a few `TRACEROUTE` operations at different times of the day (and week) and analyzing the latency of the different hops that are reported back. `TRACEROUTE` is the UNIX version of the command that is `TRACERT` on Windows, and `TRACEPATH` on Linux. [Figure 15.12](ch15.html#a_tracert_from_boston_to_new_york_with_h) shows the `TRACERT` command applied from my workstation out to Verizon's DNS server. The hops inside the LAN were a total of 2 ms (milliseconds), while each of the remaining hops from the Boston suburbs to New York represented a time of 372 ms, or 0.32 seconds. If the traffic is round-trip, then you need to double your estimate.

![A TRACERT from Boston to New York with hops' latency data shown](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1512.png)

**Figure 15.12. A `TRACERT` from Boston to New York with hops' latency data shown**

## iSCSI protocol

The iSCSI protocol packages SCSI commands inside TCP packets for transport over IP networks. iSCSI is a relatively new technology that allows a host to interact with storage as if it is direct attached or point-to-point, but to present the storage to an IP network as a shared asset. iSCSI offers a number of very important advantages over SANs and Fibre Channel. Because data is sent over IP networks, it is much cheaper to deploy iSCSI as you can leverage existing networks. The distance limitation of Fibre Channel does not apply to iSCSI, making WAN links much more practical.

iSCSI is enabled either in hardware at the HBA or in software using specialized device drivers to format the packets. The use of storage over IP as the storage network makes iSCSI very attractive for use in LAN deployments, departments, workgroups, and other scenarios where the network already exists.

iSCSI clients are called initiators, commands are formatted in the SCSI Command Descriptor Block (CDB) format, and the commands are then sent to the target. iSCSI uses unique identifiers to differentiate individual initiators and targets. There are three different and separate naming conventions:

- iSCSI Qualified Name (IQN)
- Extended Unique Identifier (EUI)
- T11 Network Address Authority (NAA)

IQN is the more common of the three different formats. It takes the form iqn.yyyy-mm {reverse domain name}. An example would be `iqn.2009-06.20.com.domainname:devicename.type.location`.

It's important to protect iSCSI traffic, because the commands are usually sent unencrypted using text. iSCSI uses different authentication methods to establish a session between initiator and target. The simplest method uses the Challenge and Response Protocol (CHAP); more secure authentication can be enforced by using IPsec as the Network protocol. Another method used to secure iSCSI traffic is to segregate that traffic to dedicated connections enforced at the switch port level or on a VLAN. iSCSI can also be set up so that the connection requires a specific logical unit number (LUN) authorization.

An iSCSI initiator is one endpoint of a SCSI session; it sends SCSI commands to a target but does not specify the eventual location of the data or the data's LUN. An initiator on a host system is most often a device driver that emulates an iSCSI HBA. The device driver uses the host's network stack to send and receive iSCSI commands. These iSCSI device drivers can be supplied by the operating system vendor, or are made available by the HBA vendor as part of their included software.

### Note

The Microsoft iSCSI page can be found at `www.microsoft.com/WindowsServer2003/technologies/storage/iscsi/default.mspx`.

Initiators are also contained in HBAs. The initiator function is embedded in firmware on the HBA, which usually adds some sort of TCP offload processing engine. iSCSI is a demanding protocol that requires a high-performance solution, and the offload function isolates much of the processing and data traffic to the HBA. iSCSI HBA is currently supported by either 10 Gigabit or Gigabit Ethernet speeds.

An iSCSI target is the endpoint of a SCSI session. It waits for commands from the initiator and responds to them. The target returns the location of the data, usually in the form of LUNs, and sends them to the initiator so that data can be requested. The iSCSI target is most often a logical disk unit of some type located on a storage system, but it can also be tape systems or optical changers. Targets can also include virtual resources such as virtual disk, virtual tape, or another virtual medium that is accessed by iSCSI software using the controllers that are internal to the devices that have virtualized components.

The software that serves as the target is a kernel-level device driver that is available in most operating systems or from the HBA vendors. Some vendors bundle iSCSI inside their disk arrays as a set of iSCSI targets that can communicate with multiple hosts.

A LUN is an addressable storage entity in a SCSI bus. It can be a single disk, a RAID set, or more often a volume that is defined from part of one of the first two physical storage assets. iSCSI treats a LUN as if it were a unique disk drive, and formats, mounts, and manages the file system on the LUN. In order to mount an iSCSI LUN, it must be formatted by an iSCSI system and its file system is then part of the iSCSI LUN definition.

iSCSI is the most popular of a number of storage networking protocols that encapsulate storage command. iFCP shares many of the characteristics of iSCSI that have been described in this section. In [Figure 15.13](ch15.html#a_native_and_heterogeneous_iscsi_san_dep), there are two different iSCSI topologies shown: one that uses only native iSCSI shown on the left side of [Figure 15.13](ch15.html#a_native_and_heterogeneous_iscsi_san_dep) and another that mixes iSCSI and Fibre Channel through an intermediate bridge that is labeled iSCSI Heterogeneous SAN on the right side of [Figure 15.13](ch15.html#a_native_and_heterogeneous_iscsi_san_dep).

![A native and heterogeneous iSCSI SAN deployment](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1513.png)

**Figure 15.13. A native and heterogeneous iSCSI SAN deployment**

## Fibre Channel over IP

Fibre Channel networks are impractical over long distances and require expensive infrastructure and specialized knowledge to implement and manage. There are vast hordes of network engineers who know TCP/IP networking and a tremendous amount of infrastructure available in that network protocol. For all of these reasons, Fibre Channel over IP, or FCIP, has an audience.

FCIP is currently used to connect "SAN islands" over WAN links. At each end of the link are FCIP gateways. From the standpoint of the network, it is irrelevant where the gateway devices are located. The major concern is whether it is possible to send the necessary traffic over the link using the bandwidth that you have available to you.

Many Fibre Channel SANs were built to provide the storage support for high-speed transactional database systems. A transactional system can sustain a wait period of a second or two to retrieve data, but longer wait periods result in serious performance degradation. The distance that an FCIP packet must travel has a fundamental impact on whether you can use FCIP in a transactional system.

There are processes that tolerate latency. Backup and replication are examples of applications where FCIP could be used. In a backup process, data is transmitted from one site to another. If there is latency, then the data throughput is simply slower. How much slower? At current speeds, data over an OC-3 IP connection takes about six times as long as over an FC SAN. Incremental backups that are sometimes called data vaults are good candidates for FCIP. A popular commercial application, called Carbonite, is a data vault. You specify a backup, and the system begins a very slow copy of all of the data. Once the data set is completely transferred (which may take days), the changes are copied with only a small delay.

Data vaulting is particularly important when the data it is protecting is valuable. Products that perform data vaulting of a live transactional system require special techniques to ensure that they capture data that the file system locks because it is in use. These programs tend to use a number of proprietary techniques to solve these types of problems. The Sarbanes-Oxley Act of 2002 in the United States included corporate record-keeping provisions that made data vaulting more popular.

## Internet Fibre Channel Protocol

The Internet Fibre Channel Protocol, or iFCP, is a tunneling protocol that enables Fibre Channel data to flow from one iFCP gateway to another iFCP gateway. The protocol was designed to allow fast point-to-point connections and to link SANs over IP links. Encapsulated data inside iFCP can contain SCSI commands or data formatted in Fibre Channel over IP (FCIP) and is contained within IP packets.

Much of the network overhead for an iFCP connection is performed by TCP/IP, including routing and switching, error detection, flow controls, and recovery. Packet formation is performed at the iFCP gateway, as is frame extraction from received packets.

# Storage Area Network Management

Storage Area Networks, or SANs, have hundreds if not thousands of elements that must be managed in order for the storage network to run optimally. These elements include port traffic, port assignments, disk activity, connection monitoring, host performance characteristics, and many other factors. Nearly all of the components installed on a SAN conform to industry standards, such as SNMP, so that they are discoverable and manageable. Most SAN management software is a framework that uses SNMP for command and control functions from a console (host).

The majority of these SAN management solutions are either Windows or Sun Solaris applications; many are browser-based and therefore platform independent. When Windows is used, it is common for the application to use the Windows Management Instrumentation (WMI) interface for device management.

WMI is an extension of the Web-Based Enterprise Management (WEBM) and Common Information Model (CIM) that was developed by the Distributed Management Task Force (DMTF) for standardizing instrumented components. That's a lot of acronyms, but WMI is interoperable with SNMP, and it allows Windows hosts to use the command line interface (WMIC) that Microsoft has developed for very convenient access to devices. The graphical utilities are simply front-ends for these commands.

SAN management software can be deployed in-band as an appliance or server at the edge of a SAN, or within the SAN as part of the data path. It can also be deployed as one of those devices as an out-of-band solution that is located on the data network (LAN), but that is not in the data path of storage I/O. These applications can perform discovery and mapping operations, monitor bandwidth utilization, and make changes in the environment. Examples of SAN management packages are Onaro's SANscreen (now owned by NetApp), EMC ControlCenter SAN Manager, and the IBM System Storage SAN Volume Controller (SVC). This category of software tends to be expensive but can have a very dramatic payback in terms of efficiencies.

A related area of software used in storage network management is called Storage Resource Management, or SRM, software. SRM can be deployed on networks of any type (LANs, SANs, and so on) and monitors storage assets down to the smallest level. Early SRM performed disk quota management, but with current SRM software, it is possible to determine which disks are close to full, which files are getting the most access, how many instances of a particular piece of data exist, and so forth. SRM is incredibly valuable in an enterprise and on a storage network, but its expense has kept the category relatively small. Windows Server 2008 shipped with a basic SRM application that allows you to check out this area of technology for yourself. SRM will likely become a standard module in all network operating systems sometime in the future.

## Internet Storage Name Service

The Internet Storage Name Service (iSNS) is a proposed IETF standard that would unify the methods used to manage iSCSI and FCIP devices on an IP network. A number of vendors offer iSNS servers, including the OpenSolaris Project, Microsoft iSNS Server 3.0, and Linux isns for iscsi, among others. The services iSNS provides includes the following:

- Name registration
- Discovery Domain (DD)
- Login authentication
- Storage resource discovery
- State Change Notification (SCN)
- Fibre Channel and iSCSI connection management

While the Fibre Channel part of iSNS is required for any implementation, the iSCSI part is optional. The protocol creates a set of management services that emulate a Storage Area Network switched fabric. There are four parts to an iSNS network:

- **Server(s)**. An iSNS server can service both iSCSI and FCIP traffic.
- **Client(s)**. A client is any iSNS-aware device.
- **Database(s)**. The iSNS database stores information about clients in its DD and events.
- **The iSNS Protocol (iSNSP)**. The protocol is used for communication between client, servers, switches, and other targets.

Establishing an iSNS management system allows target devices to register in the DD and to be managed using logical units such as storage groups. The stored logins can be applied to sets of storage units, which allows the storage network to manage a large number of assets. Control over parts of the management structure can be delegated.

# Summary

In this chapter, you learned about storage network technology and why it is so important. Some of the largest networks in use today are Storage Area Networks. Storage networks can be described in terms of their topology and the technologies that they use. One of the highlights of this chapter was a description of Fibre Channel networks. Storage network topologies can be direct attached, point-to-point, arbitrated loops, and fabrics.

The shared storage network model was presented so that you would have a vocabulary with which to describe different applications, devices, and technologies. Storage devices can be broadly categorized as either block- or file-oriented solutions. The shared storage model was extended for tape devices.

Concepts such as physical versus logical disks, storage virtualization, aggregation, and redirection make storage networks adaptable and easier to use.

In the next chapter, a number of high-performance network technologies are described.
