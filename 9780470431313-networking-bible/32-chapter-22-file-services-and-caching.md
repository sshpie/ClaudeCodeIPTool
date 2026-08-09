# Chapter 22. File Services and Caching

**IN THIS CHAPTER**

- File-oriented network services and protocols
- How NAS works
- File service protocols
- Install Samba on Linux
- How DFS can improve network performance

Network file access is one of the most important services that a network can provide. It represents a large share of the network traffic that you are likely to have. For this reason, a number of approaches are used to improve the response of networks to file requests, to secure content, and to make sure that content is protected.

Any networked operating system can be configured to serve files to clients. Usually these systems are not optimized for file services. A class of storage servers called Network Attached Storage (NAS) is an optimized file server that you can use on your network. NAS often behaves as if it is a network appliance, and can be used by many different types of clients. The difference between a NAS and a storage area network (SAN) is that NAS transfers files, while SANs and storage arrays do block transfers.

To efficiently send a file across a network, there are a number of file services in use. The most prominent of these protocols is the Network File System (NFS) and Common Internet File System/Server Message Block (CIFS/SMB) protocol. NFS is common on Linux and UNIX, while CIFS/SMB is used on most network operating systems. Samba is an example of a CIFS/SMB server, and in this chapter a copy of Samba is installed on Ubuntu.

File service protocols provide a number of important services. They authenticate clients' access to network shares, maintain access lists, provide a network browsing function, and manage access to files by providing for file and record locking. Some of these protocols offer network printing.

Another approach to distributing file content across a network is to create a distributed file system (DFS). In this technology, you create copies of your content in various places and then have the DFS server's namespace point clients to the location of the file that is closest to them. DFS is available in Windows servers, and as third-party solutions.

# Network Attached Storage

Network Attached Storage, or NAS, consists of file servers that provide file access to network clients. NAS devices range in size from small Snap Servers that aren't much larger than an external hard drive up to wardrobe-sized servers with multi-terabyte capacities like the EMC Celerra NSX server. Network Appliance Inc., now called NetApp Inc., refer to their systems as *filers*.

Many NAS systems are literally appliances, particularly the small ones. You plug the NAS into an electric socket, connect an Ethernet cable, and turn them on — they do all the rest. The NAS operating system advertises for a DHCP and DNS server, is assigned an IP address lease, and then appears on the network automatically. At that point you configure file shares, add users and groups, set access rights, and perform other functions associated with file servers. Most NAS systems are built to be promiscuous: they come with several different networking protocols built into them so that they can share files with different operating systems.

Most NAS systems implement browser-based management utilities, although the larger servers and enterprise-class devices come with a variety of powerful programs for backup, replication, and many other file-oriented features. Most NAS devices are designed to be headless — that is, they don't require a monitor — and some do not include keyboard, video, and mouse (KVM) functionality.

The development of file servers predates the introduction of NAS. Novell Netware and Sun Microsystems servers appeared in 1983 and 1984, and using the NCP and NFS protocols, they could make network shares available to clients. However, these were general-purpose servers configured as file servers, but not optimized. Another significant development was the introduction of LAN Manager by Microsoft and 3Com, which led to the development of NetBIOS over TCP and could be used by Windows clients. In 1985, the 3Com 3Server and 3+Share software appeared; it allowed system vendors to create dedicated file servers. It was clear by the 1990s that this was a significant product category.

Storage industry insiders consider Auspex Systems, founded in 1987 by Larry Boucher, to be the pioneer of the NAS category. Many of the engineers and managers from that company went on to create other companies such as NetApp, and Boucher himself became one of the founders of Adaptec. With the introduction of the NetApp filer in 1995 — more formally known as the NetApp Fabric Attached Storage (FAS) server that supported the UNIX NFS and Windows CIFS protocols — the category for dedicated and proprietary NAS servers was established. Today you will find NAS systems offered by a very wide range of vendors.

In the sections that follow, the features of networked file servers are considered, as is the difference between NAS and SAN network storage. NAS is very useful for caching content on a network and delivering that content to distributed systems, a topic which follows.

## Features

A NAS filer requires four things:

- An optimized network I/O function
- An optimized disk I/O function
- A powerful file system
- A lot of disk storage, preferably in a protected form such as a Redundant Array of Inexpensive Disks (RAID)

Most of the additional functionality in general-purpose network operating systems can be stripped away in order to improve the performance in these areas. Indeed, NAS devices typically have very stripped-down operating systems that are surprisingly lightweight. NAS devices can be powered by small, embedded application-specific integrated circuits (ASICs), and some can fit on floppy disks or small USB keys.

You can build a NAS system with just about any operating system, but the majority of devices sold today are based on Linux distributions. A number of open source NAS distributions are available, the best known of which is probably FreeNAS. FreeNAS is a version of BSD (Berkeley Software Distribution) with reduced functionality that is less than 32MB in size. You can configure FreeNAS to run on a Live CD, which is a boot disk with all required operating system functionality. Other free NAS distributions include NASLite and Sun Open Storage.

[Figure 22.1](ch22.html#the_freenas_home_page) shows the FreeNAS home page where you configure your NAS device. The range of features that you see in FreeNAS is common to NAS devices as a category.

![The FreeNAS home page](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2201.png)

**Figure 22.1. The FreeNAS home page**

NAS devices typically support:

- A wide range of services and protocols so that they connect to clients in a heterogeneous network
- Software/hardware Redundant Array of Inexpensive Disks (RAID); RAID 0, 1, 0+1, and 5 are common
- Advanced disk utilities such as disk formatting and partitioning tools
- Active Directory integration, as well as Network Information Service (NIS) integration into UNIX/Linux directories
- System management tools, usually browser-based
- Network interface management, and protocols for accessing shared storage such as iSCSI

Microsoft has a very good NAS operating system, Windows Storage Server 2003 R2, which has appeared on a number of OEM (Original Equipment Manufacturers) systems such as HP's (Hewlett-Packard's) NAS.

Nearly all of the major computer OEMs have NAS systems in their portfolios. For Dell, their line is called the PowerVault series. HP's home NAS devices are the Media Vault service, their mid-level models are in the ProLiant Storage Server, and several NAS models are in their StorageWorks lines. HP has a large storage portfolio because they acquired Compaq, and Compaq had acquired Digital Equipment Corporation, both of which had large storage divisions. Sun Microsystems is another large vendor in the NAS area, and they have a line of Sun StorageTek NAS systems. Examples of small home NAS devices are the Snap Server, Kuro Box, TeraStation, and LinkStation.

## NAS versus SAN

There is some confusion regarding the difference between NAS devices and Storage Area Network (SAN) storage servers. The two categories of devices are illustrated by considering two enterprise-class storage devices from the same vendor, EMC: the Celerra, which is a NAS server, and the Symmetrix servers, which are enterprise-class storage arrays. The difference between the two is in how data is transferred to a client.

A NAS device is a storage server with an operating system and a file system. When a client views a file on a NAS device, it does so by viewing the NAS file system. The selected file is transferred as a file to the client upon demand. By contrast, a storage array has nearly the same components as a NAS, but when you view a file stored on a storage array, you are viewing the file in your operating system's own file system. When you request a file or directory from a storage array, a mapping table maps that request to a set of blocks on a particular set of disks. It is those blocks that are transferred to you system, which is then responsible for managing the file or files contained within them.

The difference is subtle from a user's perspective: they see a file in a directory in a file system, and it is transparent to them where that file might be. However, from a system architecture standpoint, the difference between a NAS and a SAN storage array is fundamental. There are some high-performance NAS devices, but because they have the overhead of managing files, their performance is slower than storage arrays where the only overhead is direct disk access. Storage arrays are particularly good at applications such as backup and restoring, but offer no advantages when the operation is file-based. For example, when the application being accessed over the network is file-based, such as a large, streamed video file, a NAS filer is a superior solution. [Table 22.1](ch22.html#nas_versus_san-037) details some of the important differences between a NAS and a SAN.

**Table 22.1. NAS versus SAN**

| Feature | NAS | SAN |
| --- | --- | --- |
| Network Types | TCP/IP, FDDI, ATM | Fibre Channel |
| Wire Protocols | TCP/IP, NFS, CIFS, HTTP | Encapsulated SCSI |
| Device Types | Any connected LAN system that can use the wire protocols. | A server with SCSI Fibre Channel that connects to a separate SAN network. |
| Data Transferred | Files and file metadata, security, user identity, and file locks. Files are identified by their position on disk. | Block data is transferred based on the block number of the disk. |
| Connected clients | Any network client that can connect through a wire protocol. | File sharing is through the file system of the connected operating system. |
| File system | Managed by the NAS. | Managed by the connected server OS. |
| Backups/Mirrors | Usually snapshots or images that are file-based, often capturing incremental changes. | Block-by-block copy, volumes are duplicated as direct copies. |

[Figure 22.2](ch22.html#a_nas_versus_san_topology) shows a conceptual diagram of a NAS attached to a network of computers. Notice that the SAN is actually an internetwork of two different network types: Ethernet and Fibre Channel. The storage arrays are attached to the Fibre Channel network, which is referred to as the *in-band* network, while the Ethernet network connected to hosts is called the *out-of-band* network.

This separation between NAS and SANs is historically accurate and currently the rule, but future protocols may allow for Fibre Channel protocols to travel over IP networks and will blur this distinction, and products are being developed that blur the difference between NAS and SAN. Two examples of this new trend are the LeftHand Networks embedded virtual storage system and the open source Openfiler operating system, which provide both file and block-level access to storage.

## Network file caching

One application of file servers is to push content out to different locations on the network. This is done in many ways. One approach is to use mirrors, replicating the entire content at different locations. This approach places a large burden on networks and can be impractical when an entire mirror must be replicated. In scenarios such as these, companies pre-build file servers and then ship them to the location where they will be deployed.

![A NAS versus SAN topology](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2202.png)

**Figure 22.2. A NAS versus SAN topology**

Another approach deploys NAS devices with special software that turns those filers into large, intelligent network file caches. The file cache is populated from client file requests, and so only the data that is requested is pushed out to the cache. Some of these systems set up distributed networks of caches with replication schemes. The fact that a subset of the data is cached makes this a much more efficient solution.

Many companies offer network-caching solutions. For information about Cisco's technology, go to `www.cisco.com/en/US/docs/internetworking/technology/handbook/Net_caching.html`. NetApp developed a line of network file-caching servers, but has sold this business to Blue Coat Systems, Inc. (`www.bluecoat.com`), which sells these systems under the ProxySG name.

File-caching solutions play a prominent role on the Internet. One company that specializes in this technology is Akamai (`www.akamai.com`). Capacity on their edge-caching network is sold as a set of solutions to various industries as Web site and Web application accelerators, for media delivery and streamed content, and for electronic software delivery. *Edge caching* is a term used to describe the distribution of content from a Web server to file caching servers that are geographically closer to the clients that use that content. Edge caching is usually sold as a service, so that if you go to a site such as `XYZ.com` that uses a caching solution, your request is redirected to the closed file caching server in the system.

# File Service Protocols

There are several different file service protocols that are examined in this chapter, notably Network File System (NFS), Andrew File System (AFS), and Server Message Block/Common Internet File System (SMB/CIFS). The purpose of these file service protocols is to provide clients remote access to storage: these protocols make files and directories located remotely appear as if the storage were local on the client's system.

The benefits of using file services for remote file access are:

- Storage can be consolidated and protected
- The need for storage on client systems is diminished
- A user's home directory can be maintained on a file share and be made available from anywhere on the network
- Storage devices such as optical drives can be shared over the network with attendant economies

File service protocols are Applications layer protocols, but these protocols rely on Presentation layer software to manage data transfer, and remote procedure calls to access remote system data, as described in the next section.

## Network File System

The Network File System, or NFS, is a protocol that is popular on UNIX and Linux, and that gives a computer access to networked file shares. It serves the same purpose as CIFS/SMB. It was developed by Sun Microsystems in 1983, and was subsequently taken over by the Internet Engineering Task Force (IETF), which was responsible for Version 4, the last released version. Sun's WebNFS software, which allows NFS file shares to be viewed and managed within a browser, has also recently been open sourced.

NFS was heavily influenced by the Andrew File System (AFS), as was the distributed file system (DFS) that is described later in this chapter. AFS is a distributed file system that contains a Kerberos security system for authentication and access control lists (ACL) for directories. AFS was developed at Carnegie Mellon University, and is named after Andrew Carnegie and Andrew Mellon. Versions of AFS are Transarc (from IBM), OpenAFS, and Aria.

NFS is considered to be a mature file transfer protocol, and is supported by nearly all networked server operating systems, although it isn't used as widely as CIFS/SMB or the NetWare Core Protocol (NCP). There is NFS support on Microsoft Windows, Novell Network, Mac OS, and the IBM AS/400 line.

NFS is implemented in Layer 7, the Application layer, as a set of routines for managing files over the network, called the NFS Procedures and Operations functions. The entire NFS protocol actually spans Layers 5 to 7, because NFS has a language set called the External Data Representation (XDR) language, which is used to define data types that can be exchanged with the network. XDR is best thought of as Presentation layer software, and is an interchange format.

### Note

NFS versions 1 and 2 used UDP instead of TCP, which tended to make the system unreliable, especially across subnetworks and on internetworks. Version 3 and later use TCP and are more reliable.

The last module at the session level is the remote procedure call, or RPC, service. RPC is a component of all file services. It is these three subprotocols together that comprise the NFS system. RPC was developed as part of NFS, but has become a standard that is used for system interoperation throughout the computer industry in client-server applications (like the .NET Framework) that run over TCP/IP. RPC is the portion of the NFS module that is responsible for passing messages back and forth, and for maintaining the connection state.

NFS must be configured on both the server where the file share is and on the client. Many NAS systems come with NFS installed and allow you to simply designate a new share as an NFS share. In Windows Server 2008, the Add a Share Wizard presents you with a step that selects either NFS or NTFS access (or both) of the share as a check box selection; subsequent steps allow you to set up user and group permissions. On the client side, in Windows it is necessary to bind the NFS protocol to the network interface to provide client access.

The installation of NFS on Ubuntu Linux requires that you set up users and groups, and install NFS on the server:

1. Set up user and group permissions.
2. Install the NFS Server.
3. Create the server shares, and then export them to clients.
4. Install NFS on the client.
5. Mount the remote folder on the client, either manually or automatically at startup.
6. Test your client's NFS share access.

For more details on the exact steps, go to the Ubuntu SettingUpNFSHowTo page at `https://help.ubuntu.com/community/SettingUpNFSHowTo`. Another general procedure for FreeBSD may be found at `www.freebsd.org/doc/en/books/handbook/network-nfs.html`.

## Server Message Block/Common Internet File System

The Server Message Block (SMB) is an Application layer protocol (less frequently a Presentation layer protocol) that is used to share files, printers, serial ports, and other network resources. Resources can also include access to network application programming interfaces, or APIs, named pipes (or connections), and other virtual objects. SMB uses a variety of Transport layer protocols.

SMB uses a client/server request/response mechanism to create connections between resources on one host with another host. An SMB client requests a resource such as file access from an SMB server, and SMB creates an opportunistic lock on the resource for its use.

SMB was developed by IBM for the IBM PC in 1985, and Microsoft and other companies added to it as it became a public standard. SMB is native to all versions of Windows, from Windows NT onward, OS/2, and Linux, and it was the protocol used by the LAN Manager software. There is support for SMB for nearly all networked operating systems.

SMB commands are sent using NetBIOS over TCP/IP (what Microsoft refers to as NBT) to create stateless connections between hosts. Commands include session control packets that create the connection to a network resource; file access packets that can access file shares: open, read, and write files; and depending upon the security in place, create files and directories; and a set of general message packets. The general message category includes packets that have commands that send data to printers, query for resource status, and manipulate named pipe, MailSlots, and other virtual connections. SMB has two security modes — share level and user level — both of which are described more fully later in this chapter.

Microsoft, SCO Group, and some other vendors created the Common Internet File System (CIFS), an extended version of SMB. There are many different dialects of SMB, and CIFS is considered to be one of them.

The Microsoft version of the SMB/CIFS protocol provides the following services:

- Protocol negotiation between various SMB dialects
- Opportunistic locks on network resources
- File and record locking
- Notification of file and directory modification
- Authentication and authorization for file, directory, and share access
- Extended file attribute support
- Unicode support
- Network printing
- Network browsing or services announcement

SMB/CIFS is one of the two important file transfer systems in use today; NFS is the other one. As an example of a CIFS server, the next sections take a look at the Samba file server.

# Samba

Samba is the most widely used file sharing software, and it is the basis for a wide range of products. You install the Samba application on the operating system of your choice, and Samba file shares can be viewed over a network by a wide variety of clients and hosts. Samba (`www.samba.org`) is open source software; it takes its name from the Server Message Block (SMB) protocol, which is the same protocol that the Windows network file system uses. Samba is one of the best examples of a CIFS/SMB file server.

A Samba server can join a Windows domain as a file and print server, and even be installed on a Domain Controller, to provide file services to a domain. Samba's native CIFS/SMB file transfer protocol is the Windows native file transfer protocol; Common Internet File System (CIFS) is an extended version of SMB used by Windows and OS/2. As a Windows application, Samba supports Windows domain services. It can log into the Active Directory and be a domain member compatible with all of the Windows security protocols.

When a Windows client connects to a Samba share, it can do so using the NetBIOS over TCP (NBT) protocol. The Samba host appears to be just like any other Windows system in the Network folder. Samba also supports the Microsoft Remote Procedure Call (MSRPC), which makes Samba compatible with Web-enabled applications that are built with the .NET Framework. You can install the Samba Web Administration Tool, or SWAT, which is included with Samba distributions, to manage a Samba server from a remote browser.

Indeed, it is hard to find an operating system that you can't run a version of Samba on. Samba version 3 runs not only on Windows, but also on a variety of Linux and UNIX systems. There are versions for Sun Solaris, Netware, IBM OS/2, IBM AIX, IBM System 390, OpenVMS, Amigo OS, and Mac OS X clients. Many versions of Linux include Samba in their distribution, install the software as part of their base installations, or have a version readily available for download. SMB is universally used, but to use CIFS on some versions of Linux or UNIX, you may need to install third-party software that supports it. You can install the `smbclient` utility that is part of the Samba suite to allow UNIX clients to connect to Samba shares, send and receive files, and work with printer shares.

If you install Samba on a Windows system, then the SMB file share behaves as if it is a local hard drive, even if it is running on a remote system. If you install Samba on a UNIX system and join that system to a Windows domain, then the shares you create from UNIX directories appear in the Windows network as if they were standard Windows folders. In order for UNIX shares to appear on Windows, you must mount the shares first. You can use `smbclient` for this purpose.

When you install Samba on Linux systems, those systems format their Samba partitions with the SMB file system (smbfs). smbfs is derived from the Samba code base, but smbfs is not maintained by `Samba.org`, although you will find it on Samba's Linux distributions. Linux can mount an SMB share that uses smbfs directly into a Linux directory. When you browse the SMB file share, it looks just like any other local Linux directory and gives you full access rights.

## Samba security

The Samba suite of programs implements all four aspects of CIFS services that you learned about in the previous section. The SMB Daemon (smbd) is responsible for the file and print functions, as well as the authentication and authorization required by either share mode or user mode. The difference between the two modes is that in share mode, a single password provides access to any authorized share user. In user mode, each user has their own user account and must supply their username and password to gain access to the share. User accounts are created and managed by the Samba System Administrator. Samba can also be placed into Active Directory (AD) security or server mode, bringing the number of security modes available in version 3 to four.

When Samba is on a Windows domain, it takes its authentication from Windows domain services or from the AD. Samba version 2 was the first version to provide Windows domain compatibility. By Samba version 3, a Samba server is able to function as a complete Domain Controller — albeit not the latest and greatest version, but at least highly compatible with current Windows networks. Samba domain servers can use the `tbdsam` password backend as their authentication system, but this limits their use as stand-alone PDCs to small networks. For larger networks, an LDAP authentication backend, such as OpenLDAP, must be used. As I mentioned earlier, you can also install Samba directly on a Windows Server PDC.

To summarize, Samba can be placed into any one of the following four security modes:

- **User mode**. Access to Samba is through a user account and password.
- **Share mode**. Access is on a per-share basis by user account and password.
- **Active Directory Security**. All authentication is passed through to the Windows domain controller.
- **Server mode**. This is a deprecated feature of previous versions of Samba. In this mode, the client system logs into the Samba server as if the server is in user mode.

## Samba name resolution and browse lists

The second major application is the `nmdb` program, which supports name resolution and browsing. Name resolution and browsing can be either a broadcast technology that involves a request/response mechanism, or a point-to-point client/server system. In the first instance, the sender builds a network resource list, while in the second instance, the server passes a previously built list of resources from a server to a client. Microsoft Windows Internet Name Service (WINS), which is a version of the NetBIOS Name Server (NBNS) used on other operating systems, builds a small database of available systems when a WINS client is detected. When name resolution is required, a query is made to the WINS server database, which takes the friendly name and then returns the IP address. The NetBIOS name service client, or `nmblookup`, that is included with Samba distributions can be used to locate NetBIOS names, resolve their IP addresses, and download those systems' browse lists.

NBNS servers can build browse lists across subnets, and unlike DNS, the browse list is dynamic. Access to an NBNS browse list isn't protected on a system-by-system basis, and so if you can obtain access to a particular network, then you can browse all of the resources in that network.

Compare NBNS' behavior to DNS, where records are added more or less permanently to the database and for which the common query is to resolve a name from an IP address. Reverse DNS queries exist, of course, but DNS suffers from problems related to frequent enough updates that would validate a particular system's availability or existence. With an NBNS server like Samba, the browse list is dynamic, and the systems have been or are currently registered and online; however, being a looser system than DNS, there are instances where conflicts arise.

NBNS also manages a browse list of network resources, including file shares and printer shares, by electing a Local Browse Manager (LBM) that maintains the list of NetBIOS names. When a client opens the Network folder, the browse list is obtained from the LMB (Local Master Browser) and that list is used to populate the folder.

Windows domains create a Domain Master Browser (DMB), which participates in creating a browse list with any other domain that that has a trust relationship with the first domain. If there is an LMB on the network, then the LMB will synchronize its browse list with the DMB. Each server in the domain, such as a Samba server, will eventually obtain the browse list through replication. However, the replication process can be slow, depending upon the type of network connection and the number of hosts.

## Samba on Ubuntu

Samba can be installed on a Ubuntu system as a file and print server, or it can be accessed as a client when the smbmf file system is installed.

To install Samba as a server:

1. Open a terminal window and type the command **sudo aptitude install samba**.
2. Provide your root access password, and then press Enter. Samba is installed on your system. [Figure 22.3](ch22.html#installing_samba_on_ubuntu_linux) shows the results.

![Installing Samba on Ubuntu Linux](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2203.png)

**Figure 22.3. Installing Samba on Ubuntu Linux**

You do not need to install Samba on Ubuntu to access a Samba share over the network. Ubuntu is configured to connect to a Samba server using its native `SMBCLIENT` utility. This utility offers a command line function similar to FTP in that you can navigate the Samba share using commands such as `CD, LS, GET`, and `PUT`.

If you want to create a file system that Samba can use on your Ubuntu client, then you need to install the SMBFS software, as follows:

1. Open a terminal window and type the command **sudo aptitude install smbfs**.
2. Provide your root access password, and then press Enter.

As installed, Samba creates publicly accessible shares. That means in Ubuntu they are browsable from the Network Places folder and that a password is not required. If you need security for Samba shares, then you need to enable this feature in the Samba `smb.conf` file.

To turn security on and create users:

1. View and edit the `smb.conf` file by typing the following command in the Terminal window: **sudo gedit /etc/samba/smb.conf**. You can use another text editor instead of `gedit` for this purpose, if desired.
2. Change the line `; security = user` to the following two lines:security = user username map = /etc/samba/smbusersSamba will check the `smbusers` file to retrieve the user accounts. [Figure 22.4](ch22.html#the_smb.conf_file_with_user_security_ena) shows the `smb.conf` file with the changes from Step 2.![The smb.conf file with user security enabled](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2204.png)**Figure 22.4. The smb.conf file with user security enabled**
3. Save your changes to `smb.conf`; then close your text editor.

At this point, you have Samba installed and user security turned on. To access the Samba share, a Samba user must be created and added to the `smbusers` file, as follows:

1. Open the Terminal window and create a new user with the `smbpasswd` program by typing the following command: **sudo smbpasswd -a <username>**.Alternatively, you can open the Ubuntu Users and Groups administration utility and add the new user in the GUI.
2. Open the `smbusers` file with the following command: **sudo gedit /etc/samba/smbusers**.
3. Add the line **<ubuntuusername> = <samba username>**; then save and close the file.
4. In the Terminal window, type the following command: **sudo gedit /etc/samba/smb.conf**.
5. To create Samba user home directories (shares), change the text to add the following lines to the Share Definitions section:[homes] comment = Home Directories browseable = yes writeable = yesThe `smb.conf` file should appear similar to the one you see in [Figure 22.5](ch22.html#the_smb.conf_file_with_home_shares_for_u).![The smb.conf file with home shares for users enabled](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2205.png)**Figure 22.5. The smb.conf file with home shares for users enabled**
6. Save the file and close your text editor.

At this point, you should be able to browse the user share you just created on Ubuntu from your Windows system. The path to the share would be \\<*hostname*>\<*username*>.

# Distributed File System

The distributed file system, or DFS, is a client-server architecture that can turn SMB file shares located across a network on many systems into a distributed file system. A client generally has access to only part of the entire file system. When a client requests access to a share in the DFS, the DFS server can direct the user to that share in a manner that makes the share appear as if it is a local resource.

DFS is particularly useful in large, geographically dispersed networks because copies of network shares can be deployed across the network to improve performance and reduce internetwork traffic. Nodes are typically distributed on a per-LAN basis. Clients can then be directed to the nearest copy of the data. Distributed file systems are extremely valuable in branch office environments, not only because of the performance advantages they offer, but also because, should any of the other nodes of the DFS become unavailable, the local node will still continue to operate without suffering any loss of content.

[Figure 22.6](ch22.html#the_dfs_system_directs_a_user_to_a_local) illustrates the use of DFS on an internetwork.

### Note

The concept of a distributed data store shares some of the characteristics of a DFS, but is a different technology. A distributed data store creates group storage on a collection of peer-to-peer network nodes. User data is then copied between peers.

Microsoft has long been a supporter of DFS (its version is sometimes referred to as Dfs). Versions of DFS can run on any version of Windows Server, NT, and later. A DFS root can be hosted on a Windows NT 4.0 and Windows 2000 Server, as well as on a Samba Server. Later versions of Windows Server, 2003, and 2008 Enterprise and Datacenter servers can support multiple DFS roots on the same server. When DFS is part of a domain, its information is stored in the Active Directory and hosted on a domain controller. Microsoft DFS includes a replication and synchronization feature that propagates changes between DFS servers using the Microsoft File Replication Service (FRS).

The key to understanding DFS is the namespace that the DFS server maintains. That namespace maps to physical folders located in one or more locations. DFS namespaces map a list of folders to a list of target folders specified by their uniform naming convention (UNC) path. Targets are given a priority that determines which folders are replicated in what order. Should a client not be able to contact a folder in the namespace, it is possible to create a failback folder on another server. DFS doesn't require that you create a mapped namespace, but the feature makes DFS a much more powerful system.

![The DFS system directs a user to a local copy of replicated data.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2206.png)

**Figure 22.6. The DFS system directs a user to a local copy of replicated data.**

[Figure 22.7](ch22.html#namespace_mapping_and_hierarchy) shows you a namespace mapping, along with its hierarchy.

Each object in the namespace is specified by a UNC path. Replication can take up a lot of bandwidth, and so you want to pay particular attention to the replication performance over low-bandwidth connections. For this reason, companies sometimes pre-stage a new DFS server when they are at the end of a low-bandwidth connection, such as a branch office. It's also valuable to create replication groups so that most replication traffic communicates over high-bandwidth connections.

You can choose to have DFS exist as stand-alone roots or as domain-based DFS roots. In the former case, the DFS file system can only be accessed on the system that it is installed on; stand-alone DFS does not participate in the replication and synchronization scheme that domain-based DFS servers do.

![Namespace mapping and hierarchy](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2207.png)

**Figure 22.7. Namespace mapping and hierarchy**

There have been many distributed file systems created over the years. CIFS/SMB, which was described earlier, is the most widely used distributed file system. Among the other more prominent examples of this technology are:

- Andrew File System (AFS)
- Apple Filing Protocol (AFP)
- DCE Distributed File System (DCE/DFS)
- Netware Core Protocol (NCP)
- Network File System (NFS)
- Coda
- InterMezzo

### Note

There have been a large number of distributed file systems released over the years. Some of the higher-performance systems are distributed parallel file systems that stripe data across servers in a cluster or array. Some of these systems are built to also be fault tolerant. A discussion of these systems is outside the scope of this chapter. For more information on distributed file systems, disk file systems, memory file systems, record-oriented (database) file systems, shared disk file systems, peer-to-peer file systems, and other miscellaneous file systems, go to the Wikipedia List of File Systems page, found at `http://en.wikipedia.org/wiki/List_of_file_systems`.

Unfortunately, DFS isn't used as much as it should be, but it is definitely technology that is worth exploring if you have a large enough network to justify its deployment.

# Summary

In this chapter, various technologies for making files available over a network were described. Although general-purpose file servers are deployed, a specially optimized file server, called a Network Attached Storage server, is an even more elegant solution.

Different file services are used to create network shares and make their content available to clients. NFS is a common protocol for UNIX clients, but SMB/CIFS is even more commonly used. SMB is the native protocol of Samba, an open source file server. In this chapter, you learned about what Samba can do, and how to install it on Ubuntu Linux.

Another technology for distributing file contents across a network is DFS. The distributed file system allows you to deploy copies of file systems across a network, and then use a DFS server to direct users to the nearest available copy of the data.

In the next chapter, Web services are described. This chapter explains what a Web server is, the HTTP protocol, and other related services.
