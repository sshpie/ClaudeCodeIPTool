# Chapter 11. Peer-to-Peer Networks and Personal LANs

**IN THIS CHAPTER**

- Personal Local Area Networks
- Peer-to-peer (P2P) network models
- Large P2P systems
- Computer buses that can connect many devices

Personal Local Area Networks, or pLANs, are networks that have a small number of users and/or cover a small physical area. In this chapter, you look at several different technologies that implement networks of this type.

You also examine peer-to-peer (P2P) networks. A workgroup is an example of a P2P network that is composed of a dozen or less members. P2P networks can also be created by distributed applications. For a system to be P2P, all nodes must be both client and server; there is no central network management or services, and no routing function exists.

Peer-to-peer networks exist in many types. A pure P2P network is one that has no central service of any kind. A hybrid P2P may have a central index or lookup function, but the peers perform all of the data sharing between themselves.

In this chapter, you examine some of the more famous examples of P2P networks and the impact that they have had on network application architecture. Among the examples you look at are the pure P2P Gnutella and Freenet file sharing systems that use peer-to-peer discovery and an ad hoc mechanism to retrieve data. Napster and BitTorrent are given as examples of hybrid P2P systems.

The security and anonymity afforded by friend-to-friend (F2F) networks are considered.

Some computer buses play the role of personal networks. The three that are examined from a network and architecture viewpoint are the Universal Serial Bus (USB), FireWire (IEEE 1394), and Bluetooth. USB uses a tree structure, FireWire uses a daisy chain, and Bluetooth relies on an ad hoc form of networking called a piconet or scatternet.

# Peer-to-Peer Networks

A peer-to-peer (P2P) network is one in which all nodes can be a client and a server, as well as have direct connections to one another; it is also a network on which there is no central point of management. The term is applied equally to a network of computers that share a common LAN, as well as to distributed software applications sharing resources across a LAN, or more frequently a WAN.

Peer-to-peer networking's prime attraction is that it can share distributed resources, thus avoiding duplication and additional cost. One or more computers can share files, printers, optical drives, and other resources. Distributed software can make vast amounts of data ubiquitous or can allow projects with enormous processing requirements to be accomplished on many computers.

The first personal computer networks were P2P networks. The first personal computer to ship with P2P networking was the Macintosh Plus in 1984. For Microsoft Windows, the first networked version, released in October 1992, was called Microsoft Windows for Workgroups 3.11. WfW, as it was then abbreviated, used SMB (Server Message Block) Application layer file sharing, NetBIOS Session layer identification, and NBF/IPX (NetBIOS Frames and Internetwork Packet Exchange) as the Transport layer protocols. WfW's network program was VSHARE.386, which was a virtual device driver that performed file locking. For most networks of any size, the introduction of low-cost networked operating systems such as Windows NT has made P2P networks mainly a small office or home technology.

Peer-to-peer networking lives on in Windows in each of its desktop versions as the "workgroup feature," although the protocols and capabilities have changed radically over the years. Workgroups usually begin to have performance issues when they reach anywhere between 12 and 20 connections. For Windows XP and Vista, Microsoft has set a connection limit of 10, although this is an artificial limit.

When you log into a Windows workgroup, your security is maintained by your local system, and your files are local. The resources that you publish on the network are referred to as *shares*, and an administrator on a peer can set the security for that resource based on users and groups. This arrangement isn't nearly as secure as having a central authority managing security, and most networks that need security move to a client/server network, preferably with a directory service installed. The options that you have in a Windows workgroup, for example, are limited compared to a domain.

However, a server adds significant cost and complexity, which is why there are still a lot of workgroups in use. It can be argued that the lack of security, poor performance, and distributed management, as well as lack of central resource protection, make P2P a more expensive technology over the lifetime of the network; however, workgroups definitely have a lower barrier to entry.

Software can also be distributed using a peer-to-peer model. In this model, all nodes that have the software installed are peers and can see all other peers. In the sections that follow, you will see the different types of peer-to-peer networks, with examples of some of the better-known products in that area.

Peer-to-peer software has had a tremendous impact on the architecture of modern software. This kind of software can make vast amounts of data available, often for an insignificant price. In some instances, peer-to-peer software can be assembled in a common task into a powerful distributed network that can perform the work of a supercomputer such as solving complex protein folding problems, looking for aliens in outer space, and other computationally intensive tasks.

## Pure P2P networks

Pure P2P networks are those in which all network services are provided on a peer-to-peer basis. For a network to be considered a pure peer-to-peer system, it must have the following traits:

- All peers are both clients and servers.
- There are no network servers available.
- Clients can manage their own services; there is no central management console.
- There is no router function; every peer can see every other peer.

A Windows workgroup is an example of a pure P2P model system. There are also some applications that use the pure P2P model. Applications that use this model tend to be file and content transfer utilities, streaming media, IRC chats, and telephony.

### Small world networks

A small world network is one where most of the nodes on a network aren't nearest neighbors, but in which any node on the network can connect to any other node through at least one, and usually more, paths. These types of networks can be analyzed by graph theory, and they form the basis for a wide variety of systems, including social systems and computer networks. The theory that everyone is related by no more than six degrees of separation, commonly referred to as the Kevin Bacon theory, is an example of a small world network. Short-term memory is known to use a small world network of neurons. Pure P2P networks are another example of this network type.

A totally randomized small world network has the smallest average "shortest paths." Most small world networks are not random and tend to form higher-traffic paths among a group of nodes. Also, there is usually at least one short path that connects any pair of nodes. Small world networks are populated with a large number of hubs, which are nodes of high connectivity; and a much smaller number of edge nodes. When a small world network has a higher number of hubs than you might expect, this is called a fat-tailed distribution.

### Gnutella

Perhaps the best-known pure P2P application is the popular Internet file sharing system called Gnutella. The name comes from the developers' love of the hazelnut-and-chocolate spread called Nutella and their intent to release the software under the GNU general license. Gnutella was released to circumvent some of the problems that Napster was experiencing. (Napster is discussed later in this chapter.) Gnutella is a system that allows peers to view files on other peers' computers without the need for a central database.

There are many systems that use Gnutella, as well as a large number of Gnutella clients for all available platforms. The most popular clients include BearShare, Gnucleus, LimeWire, Morpheus, WinMX, and XoloX.

When you launch a Gnutella client, it first searches for one or more available peers. Sometimes the software comes with a listing of possible peers, and other times the client is configured to consult a Web cache. In early versions of Gnutella, the client first searches for another peer, and will continue to look for more clients up to a small limit that is usually around five systems. Each node also has five known peers so that when a request for a file goes out, the request can be forwarded to all peers within seven hops of the first peer, within the limit of the request's Time to Live (TTL) parameter. This fan-out can connect to up to 78,125 systems if necessary. Any systems that respond to the recognition ping by the first peer with a pong are listed in a table that is stored by the Gnutella client for later use.

[Figure 11.1](ch11.html#the_gnutella_file_sharing_system_uses_a) shows Gnutella's very simple but effective pure P2P architecture. The figure shows that the system is a tree structure that fans out seven levels deep. A message can travel up to seven hops, illustrated by the dark tree shown on the left-hand side of the figure. The other trees and the ellipsis symbols illustrate that the actual network fans out to accommodate the additional levels. Space precludes showing all of the nodes. All of the peers in this figure are connected.

Some programs that use Gnutella use a system of leaf nodes that connect to three ultrapeers. Each of these ultrapeers can connect to 32 more ultrapeers. Up to four hops are allowed. The fan-out for this system is enormous; I calculate it as 4.38 × 1048. Peers use the Query Routing Protocol to exchange a Query Routing Table (QRT) containing hash values, and at the ultrapeer level, those peers merge the tables together. The query from a client travels down the chain until a hash value matches, at which point the peer that was responsible for the hash entry is contacted for a file match.

Once a match is located, the requesting peer contacts the peer with the content and they negotiate the file transfer. If the content peer is behind a firewall and can't respond to a request to transfer the file to the system outside the firewall (a pull request), then the requesting system sends a message asking the content peer inside the firewall to initiate the transfer (a push request). If that still doesn't work, then a push proxy (often the ultrapeer) is used as an intermediary.

Gnutella makes no requirements about the types of files that can be shared. It also isn't easy to trap Gnutella requests because they are ad hoc and the links can be transient. The distributed nature of the system and the lack of a central authoritative database also mean that it suffers from fewer performance problems and bottlenecks.

![The Gnutella file sharing system uses a pure P2P hierarchical structure for queries and data transfers.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1101.png)

**Figure 11.1. The Gnutella file sharing system uses a pure P2P hierarchical structure for queries and data transfers.**

### Note

The file sharing system Kazaa uses a system of pure P2P fan-out similar to the one that Gnutella uses.

### Freenet

Another example of a pure P2P system is the open source project called Freenet that is available under the GNU license. Freenet uses a key-based routing protocol in place of the distributed hash tables that Gnutella uses. The algorithm examines the keys and connects to those nodes that are closest to the requesting system or connecting peer. A key is a hash function that is based either on content or location; Freenet uses both.

Unlike other P2P systems, Freenet creates a distributed storage system or cache and populates that cache with content. Typically a peer donates about 10GB to the system. The act of adding a file or Web page to the cache is called *insertion*. The user does not control what is stored in his cache. Varieties of Freenet are Darknet, where users are connected to a selected number of trusted users or networks, and OpenNet, where no restrictions are made. Darknet can still fan out to fantastically large limits but must retain their trusted connections. Freenet is still under development but exists in stable forms that are in use.

## Hybrid P2P systems

A hybrid peer-to-peer network is one where clients are peers but some central services still exist. Hybrid P2P networks are widely used for distributed Internet applications, and have played a large role in popularizing these types of networks.

Peer-to-peer networks that are created by links in which any two nodes know about the existence of their peer before they form the connection are called *structured networks*. The hybrid P2P file sharing networks that follow, Napster and Torrents, are examples of this type of network. A structured network requires some kind of global protocol for maintaining pointers to content and systems. Many P2P networks store this information in a distributed hash table (DHT) of some kind.

### Napster

The music sharing service Napster started out as a P2P network designed by Shawn Fanning while he was a student at Northeastern University. His system created a central server on which the locations of MP3 songs were indexed and stored in a central database. This music was distributed on client system file shares, and when you selected a song from the database your file transfer was from its location on a peer client to your system. The software was commercialized and the company took Shawn's nickname, Napster, which came from his '50s-styled hairdo.

Napster became wildly popular and led to rampant music sharing, which became the object of a music industry lawsuit that argued copyright infringement. At its peak in February 2001, Napster had 24 million unique users worldwide. Napster's argument was that they were simply a listing service and that the act of file copying was done without their permission. Eventually the service was closed by court order.

The company's logo and brand were purchased and repositioned as a pay-for-download service, first by Roxio, and then in 2008 by the Best Buy retail chain. It has never recaptured its former level of usage. However, Napster did illustrate to everyone how powerful a hybrid P2P architecture can be. Today there are many companies, particularly on the Internet, that use this model.

### Torrents

BitTorrent is a hybrid P2P file sharing protocol developed using the Napster model. The protocol is widely used and, according to a number of studies, represents a significant percentage of current Internet traffic worldwide. The site `isoHunt.com` maintains a BitTorrent search engine that currently has a million indexed torrents listed. In 2008, isoHunt was able to document more than 1 petabyte of torrent traffic. Other popular torrent indexes are TorrentBox, and `isoHunt.com`. The BitTorrent protocol was developed by Bram Cohen and is made available by his company, BitTorrent.

There are numerous BitTorrent clients that you can download. The site `About.com` has a listing that ranks their users' top seven client software applications. They are:

1. mTorrent (`www.utorrent.com`), shown in [Figure 11.2](ch11.html#mtorrent_is_currently_the_most_popular_b)
2. BitComet (`www.bitcomet.com`)
3. ABC (`pingpong-abc.sourceforge.net`)
4. BitLord (`www.dailysofts.com/program/907/29391/Bitlord.html`)
5. Vuze (`www.vuze.com`)
6. The original BitTorrent client (`www.bittorrent.com`)

![mTorrent is currently the most popular BitTorrent client. The peer list view appears in the lower half of the application window.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1102.png)

**Figure 11.2. mTorrent is currently the most popular BitTorrent client. The peer list view appears in the lower half of the application window.**

When a client wants to share a file, the software creates a .`TORRENT` file that contains information about the file and about the server that will store the metadata pointing to the file. That .`TORRENT` file is then transferred to the Torrent server, which is called the *tracker*, where it is indexed in a database. The second client comes along and queries the server for the file to learn about its location. After the .`TORRENT` file is transferred to the second computer so that the location of the file is known, the peer-to-peer transfer of the file begins. The first client with the file is the initial *seeder*, and any client that provides a complete copy of the file is also called a seeder.

Eventually any file of interest is populated to many clients, often geographically dispersed clients. It no longer becomes necessary to download the entire file from a single client, and so the .`TORRENT` file directs the client to download pieces of the file from multiple clients. Multiple clients sharing a torrent are referred to as a *swarm*. This helps distribute the load off of any one system. [Figure 11.3](ch11.html#the_bittorrent_architecture) shows the P2P architecture that BitTorrent uses and illustrates the steps that BitTorrent follows:

1. Client to Tracker: Which computers have the movie file or pieces of it?
2. Tracker to Client: You can find the pieces here.
3. Tracker to Swarm: Send and receive file pieces from the client.
4. Seeds to Client: File is on the way.
5. Swarm to Client: Here are some of your missing pieces.

![The BitTorrent architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1103.png)

**Figure 11.3. The BitTorrent architecture**

In [Figure 11.3](ch11.html#the_bittorrent_architecture) the different steps shown in the previous list are illustrated. A streamed file, which in the figure is represented by a movie reel above the computer, is stored on the seed system as a complete file with all of its constituent frames (represented in black). Peers in the system only have a subset of the frames, as illustrated by the missing frames (represented in white) in the movie reel. As the BitTorrent sends the movie to the client system, the peers send their portions of the movie to the client, eventually resulting in the entire movie file being transferred.

You can imagine that this technology doesn't make the entertainment industry very happy, to say the least. Nor is it popular with ISPs because it was estimated by CacheLogic (an Internet traffic analyst firm in Cambridge, England in 2005) that *BitTorrent accounts for 35 percent of all Internet traffic*. Many ISPs use packet-shaping tools to sniff traffic and filter out BitTorrent packets.

If BitTorrent used a single well-known port, then it would be easy for providers to simply block that port. However, BitTorrent doesn't use port 80, which browsers use for HTTP data. Instead, BitTorrent breaks up the data and uses a few TCP ports to download data in a random or least-used sequence. This approach makes the torrent more efficient and harder to block; however, it adds extra overhead (particularly at the start of the torrent) as those multiple torrents are established. The protocol doesn't yet support streamed content because of this fragmented download approach.

The BitTorrent system breaks files up into a set of equal slices up to 4MB in size. To each piece is added a checksum, which is checked upon arrival and resequencing. BitTorrent has a number of competitors; some use a metadata server called a *tracker*, while others don't. In the trackerless services, the peer clients distribute the metadata amongst themselves. Trackerless systems are pure P2P systems, and not a hybrid like BitTorrent is.

BitTorrent by itself is not illegal. It is simply a method for sharing files. It is up to the application that uses BitTorrent to police itself. The BitTorrent company has licensed the software to many multimedia companies for use in distributing their own copyrighted content. The popular World of Warcraft massive multiplayer online game is a torrent service. There are also efforts underway to incorporate RSS feeds and podcasts into BitTorrents in order to share the cost of distributing these media types.

BitTorrent sites offer tremendous services, both legal and illegal. That aside, there are some aspects of these sites that you should be aware of. When you use BitTorrent, your system's address is known and you can be tracked either as a *seeder* (the one that does the seeding) or as a *seedee* (the one that receives the seeds). BitTorrent is also a bandwidth hog and requires a broadband connection.

To discourage people who download files but don't allow their computer to be a seeder, called *leeches*, the BitTorrent system can monitor the share ratio. If a peer has a ratio of less than 1 bit downloaded for every bit shared, it can withhold the final seed or take another action. To throttle a client is to "choke" them. A *lurker* is someone who downloads files but does not add any new content to the system. Lurkers do seed the system with the content that they download.

Given the flood of data stored in torrent systems, it is impossible for these services to monitor content. It's not uncommon for malicious users to upload files with nasty business in them. So be sure that you trust the sites you download from if you use this technology, and test any files appropriately.

In honor of September 19th, Talk Like a Pirate Day, it is difficult to leave the topic of P2P software without mentioning those counter-culture heroes at The Pirate Bay. The Pirate Bay (`thepiratebay.org`) is a Swedish Web site that is reportedly the world's largest BitTorrent tracker and one of the world's top 100 visited Web sites. It is also one of the most contentious, and ultimately one of the most amusing to follow. While current plans by the pirates to buy their own island nation seem to have run aground, one never knows where the skull and crossbones will wave.

# Friend-to-Friend Networks

An anonymous peer-to-peer network is one in which the identification of the user is kept hidden. Because peer-to-peer networking requires that nodes be able to connect to other peers, anonymity requires that the peer be hidden in some manner. Most often, this is done through a routing technique.

There are many reasons that people use anonymous P2P networking. They may want to maintain their privacy, prevent tracking, keep their information out of the public domain, avoid censorship, or escape controversy. Whatever the reason, anonymous P2P is not only of interest to people but to organizations and governments, as well.

The Freenet file sharing system that you read about is a popular one on which to implement anonymous networking. When that network is an OpenNet network, all peers are seen by all other peers. That type of network is difficult to be anonymous on. The Darknet network type is one where only trusted links are allowed. Sometimes, this kind of network is called a friend-to-friend (F2F) network.

F2F networks authenticate their links using passwords or digital signatures. An F2F network can be more secure because the link is protected cryptographically, and the link's bandwidth can be controlled and protected. However, an F2F link requires extra setup and perhaps teardown, and may not be available when it is needed.

Consider the situation where you have three nodes connected by two F2F links. The middle node is a friend of both endpoints, and no trust relationship exists between the endpoints. Data that is sent from endpoint to endpoint can be hidden from each by the middle node. Networks of this type can remove the original source's IP address prior to sending the packets on to their destination. This makes the middle node essentially a proxy for both endpoints.

When you have a network where a link such as the one between endpoints appears to be a combination of one network link that is known and another that is unknown, this type of link is called an *overlay*. An overlay network is one where it appears that one network is built on another network. Nodes are connected by virtual links, often through multiple physical links. The use of dial-up networking to connect through the phone company to the Internet is an example of an overlay. Overlay is a common characteristic of peer-to-peer networks. Gnutella and Freenet are examples of overlay P2P networks.

# Bus Networking

A computer bus is a physical connection to peripheral devices. It is either something that is built into a computer or that can be added to a computer through the use of an add-on card or a peripheral device. The term *computer bus* used to imply that only a few devices were connected to that physical subsystem. For example, the Small Computer System Interface, or SCSI, in its initial forms was limited to only 8 devices, of which the host was one. Later versions of SCSI could accommodate up to 16 devices. However, most people populate SCSI buses with only a small handful of devices.

Several computer buses allow you to attach a large number of devices, or nodes. This makes them the equivalent of a computer network, albeit one in which the whole network stack is contained in the computer itself. The bus provides the physical layer, and any data linking or network software is part of the bus driver software.

In the sections that follow, you'll look at three popular computer buses — the Universal Serial Bus (USB), FireWire (IEEE 1394), and Bluetooth wireless networks — and consider how these standards enable networks that you could classify as Personal Local Area Networks (pLANs).

## Universal serial bus

The universal serial bus, or USB, is almost universally used for peripheral connections. After 1999, you'd be hard-pressed to find a motherboard that didn't support this bus standard. The USB serial bus is theoretically capable of connecting up to 127 devices per host controller, although in practice the limit is quite a bit less than the address space allows. USB-IF, the USB Implementers Forum (`www.usb.org`), is the industry group that develops the standard. USB has gone through two major versions, 1.0 and 2.0; USB version 3.0 has been demonstrated and devices are expected to be available at the end of 2009.

The main attraction of USB is that devices are hot swappable and offer plug-and-play ability. Hot-swappable means that you can physically remove an active device and replace it with another device while the system is running. The standard allows for powered and non-powered devices and can be used to support input devices, output devices, network interfaces, and external expansion cards. USB is a low-power bus and can trickle-charge, or slowly recharge, devices. A version of the USB port called PoweredUSB adds an extra four pins to supply 6A at 5 V, 12 V, or 24 V to devices. Any device that requires significant amounts of power requires its own power adapters.

A USB is controlled by a root host controller, which attaches to devices to create a pLAN with a hierarchical star topology, as shown in [Figure 11.4](ch11.html#the_tiered_star_shares_elements_of_a_dai). In these topologies any device that connects to two or more USB devices is a hub, the endpoints are USB devices, and the lines represent the individual USB connection (wires). If you attach another USB host controller, you can create fan-out in the bus structure with up to five levels allowed. Additional host controllers are called *hubs*. The device limit of 127 applies to each host controller individually. Host controllers are found as chips on a motherboard, add-in PCI cards, or in USB hubs. The technology is ubiquitous and inexpensive, and so controllers are found on a wide variety of devices.

USB devices connect to the host controller using a set of logical channels that are called *pipes*. Unlike computer networks, only the end of the pipe on the device side is referred to as an endpoint. Each device can create 32 active unidirectional pipes, with a limit of 16 pipes in and 16 pipes out. One endpoint, called *endpoint zero*, is reserved for device control, and any group of endpoints sharing a common purpose is referred to as a *group*.

![The tiered star shares elements of a daisy chain and star topologies.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1104.png)

**Figure 11.4. The tiered star shares elements of a daisy chain and star topologies.**

When you connect a device to the USB bus, the host controller gets a signal to poll devices on the bus and enumerate them. The newly connected device is reset, and when it is recognized again, it is configured and assigned a unique 7-bit address. On a serial bus, there is one data path, and so device traffic is queued by device in a sequential (round robin) order.

USB host devices in USB 2.0 create what is called the Enhanced Host Controller Interface (EHCI). The interface supports device classes that are supported in the operating system. This allows operating system vendors to create a generic set of drivers that work with a broad range of devices automatically.

Version 2.0 supports the high-speed mode of 480 Mbits/s, as well as legacy 1.0 devices at the full speed of 12 Mbits/s and at the low speed of 1.5 Mbits/s. Version 3.0 supports the super-speed rate of 4.8 Gbits/s. These are speeds measured under favorable conditions; most current USB 2.0 devices attain about 65 percent of the rated speed. The USB cable is a twisted-pair wire supporting half-duplex communication, which can be captured by USB protocol analyzers when diagnostic work is being done.

USB data is transmitted as frames that are in 8-bit multiples, and begin with a synchronization header and end with a short end-of-packet signal. Communications begin with packets sent from the host controller to devices. If this is the host controller at the highest level of the bus, then the path is through the root hub. Devices respond to the host's communication by returning handshake packets that the host can acknowledge. Communication uses token, data (two types), and pre-packet types. The USB network uses what has been called a "speak when spoken to" model, with the host controller directing all communications.

USB cables have connectors that come in six varieties: Type A, Type B, Mini-A, Mini-B, Micro-A, and Micro-B. Type A and B have four pins, while Mini-A and -B and Micro-A and -B have six pins. There are both male and female connections. (The male plugs are shown in [Figure 11.5](ch11.html#usb_male_connector_types).) You can find cables that mix and match these connections. The B plugs are used on the device side. The reason that these cables are usually two-sided is to prevent users from creating USB loops, which would cause the bus to fail. The smaller mini plugs are used on small devices such as cell phones and cameras. Micro-USB is meant to replace the mini plugs. USB 3.0 connectors will come in one version that is similar to USB 2.0 Types A and B, and another with five pins. Optical cables and connectors are expected to be released as part of the 3.0 standard.

![USB male connector types](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1105.png)

**Figure 11.5. USB male connector types**

Standard USB cables are limited to around 5m, or 16.4 feet, in length because longer distances lead to unacceptable signal loss. It is possible to find repeaters that can boost signal strength, and using them allows you to significantly increase the cable length. These repeaters are actually mini-USB hubs connected to a USB cable. You can chain up to five USB hubs together and get an aggregate distance of 30m. For USB version 3.0, the cables change significantly; they look like Ethernet cables, are limited to 3m, and support full-duplex operation. You can find USB wireless hubs available from vendors, but they are proprietary. The USB-IF is currently working on an ultra-wideband wireless connection that should achieve rates of 480 Mbits/s.

## FireWire

FireWire is the Apple brand name for the IEEE 1394 serial bus standard. IEEE 1394 provides a high-speed alternative to USB 2.0, making it very popular for devices like digital scanners, digital audio and video peripherals, and hard disks. As such, it has replaced SCSI as a more convenient bus to work with and configure. While FireWire appears on many PC motherboards and can be added on, this bus standard isn't nearly as popular on PCs as it is on the Macintosh, where it was introduced. Other implementations of IEEE 1394 are Sony i.LINK for digital video cameras and Lynx from Texas Instruments.

The FireWire bus can link up to 63 devices in a hierarchical tree topology. In a tree, there is one root node that takes the highest of the ID numbers. During a bus reset, devices on the bus are assigned by a Depth First Search (DFS), with each device assigning itself an address. [Figure 11.6](ch11.html#the_depth_first_search_algorithm_used_to) shows an example of this tree traversal algorithm. Notice that the longest limb is assigned first, and then the algorithm moves backward up the tree. In this figure the search begins at the root node 1 and proceeds down the first branch 2 through 8 looking for a match. If no match is found, the algorithm begins tracing each of the other branches sequentially from top to bottom in the order of 9 then 10 through 14, and finally ending at 15.

DFS was chosen as the enumeration technique because it is simpler to implement than a Breadth First Search (BFS), and although it isn't an optimized search technique, the small size of the IEEE 1394 bus allows for the use of DFS.

Devices on IEEE 1394 are peers and are hot swappable and self-configuring (plug and play). FireWire enumerates devices based on their IEEE EUI-64 identification number, rather than using IEEE's 48-bit standard for Ethernet MAC addresses. The former is a superset of the latter, adding additional information that identifies the device type and protocols.

FireWire has gone through several standards since 1995. The original FireWire 400 (IEEE 1394-1995) and the enhanced version (IEEE 1394a-2000) are the most common device types. FireWire 400 allows for half-duplex communication at theoretical rates from 100 to 400 (S100 to S400) Mbits/s over cables that can be up to 4.5m in length.

![The Depth First Search algorithm used to enumerate the FireWire bus](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1106.png)

**Figure 11.6. The Depth First Search algorithm used to enumerate the FireWire bus**

Just as with USB, it is possible to extend the bus in a daisy chain up to a limit of 16 connections; FireWire has a much higher power requirement than USB and requires active repeaters — essentially FireWire hubs. The most common connection, a six-circuit FireWire 400 circuit, carries anywhere from 25 to 30 volts and allows a device to draw up to 8 watts from the circuit. This is enough to power moderate peripheral devices such as scanners and printers, which is considered to be an attractive feature to most users. [Figure 11.7](ch11.html#six-_and_four-pin_firewire_400_connector) shows the FireWire 400 connectors.

![Six- and four-pin FireWire 400 connectors](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1107.png)

**Figure 11.7. Six- and four-pin FireWire 400 connectors**

The demand for FireWire has been a fraction of the demand for USB. USB 2.0 runs a little slower than FireWire 400 due to a higher protocol overhead on USB. FireWire 800 runs at 3200 Mbits/s, while USB high speed runs at 25 percent that speed, at 480 Mbits/s. However, speed isn't the issue. It would seem that the cost of the bus devices are part of the problem, as is the fact that FireWire tends to be used for one or two powered devices. It is rare for a FireWire bus to be populated by more devices than that. The USB industry grew faster, and now those devices are the dominant peripheral bus or pLAN available.

FireWire has supported networks between computers using direct connections (peer-to-peer) or when a FireWire hub is connected. Devices can use IP v.4 or IP v.6 addressing. Among the operating systems that support or supported FireWire networking are Mac OS X, Free BSD, Linux, and Windows ME/2000/XP and Server 2003. Microsoft dropped FireWire network support in 2004. Even Sony's PlayStation 2, which first used an i.LINK connector for networking, has found that most users have switched to Ethernet adapters.

To combat these trends, the last released standard, called FireWire S800T (IEEE 1394c-2006), which appeared in June 2007, offers Ethernet interoperability. The port speed is 800 Mbits/s over twisted-pair Category 5e cable with RJ-45 connectors. This is the same cable used for Gigabit Ethernet, and the standard allows both Ethernet and FireWire devices to be auto-recognized and use that port. This standard, while quite intriguing, isn't yet expressed in any products that you can buy. If it can gain traction, it may make FireWire more attractive in the marketplace.

## Bluetooth

Bluetooth is a personal wireless LAN technology that creates secure connections to devices within a small distance. Bluetooth is best known for its use in cell phone connections to wireless headsets, but the technology is also used in desktop printers, keyboards, PDAs, GPAs, bar code readers, and other peripheral devices. Devices on a Bluetooth network can see and talk with other Bluetooth devices. The Bluetooth standard is developed by the Bluetooth Special Interest Group (`www.bluetooth.com`).

### Note

Harald Bluetooth was a tenth-century Danish king who united much of Norway, Sweden, and Denmark — three countries in close proximity.

The technology used for Bluetooth is similar to cellular phone technology; it is called frequency-hopping spread spectrum. The technology uses the 2.45 GHz band in the United States and in Europe. This band is considered to be an "open" band, and so many devices transmit on it. This is the same frequency range used by the 802.11g wireless standard, many cell phones, and other devices. Oddly enough, microwave ovens emit radiation in this frequency range, and they can interrupt 802.11g phones as well as Bluetooth.

The exact range is 2400 to 2483.5 in the United States, which is split into 79 separate 1 MHz channels. In Japan, the spread is 23 separate 1 MHz channels. Bluetooth uses a technique called Gaussian Frequency-Shift Keying (GFSK) to make physical connections between devices with a transfer rate of up to 1 Mbit/s.

Bluetooth devices contain transceivers that are categorized into three classes:

- Class 1 — 100 mW with a range of 100m
- Class 2 — 2.5 mW with a range of 10m
- Class 3 — 1 mW, with a range of only 1m

These three standards are used by transceivers that are omni-directional wireless transmitters. The low power output means that Bluetooth signals cannot travel through walls. Cell phones, by comparison, emit signals of over 3 watts. Connecting a device in a network class rated for a shorter-range communication (such as a Class 2 device) to a longer-ranged device (Class 1, for example) extends the range of the shorter-range device somewhat.

### Connections

To create a Bluetooth network, called a *piconet*, you need to have a Bluetooth hub that has its own transceiver. A piconet (see [Figure 11.8](ch11.html#a_bluetooth_piconet)) is defined as an ad hoc network of Bluetooth devices, both active and passive. Generally, it is a network that is decentralized and on which any node will forward data to any other nodes. The term *scatternet* has also been used to describe networks of this type. Many laptops and some devices such as the Logitech diNovo keyboard come with a Bluetooth hub built into them. You can also purchase Bluetooth hubs that plug into USB ports, are PC cards (PCMCIA), or are PCI expansion cards. A Bluetooth network allows for only eight connected peer devices.

Clients can join the network and leave the network at any time. Wireless networks are often created as ad hoc networks. The task of defining connections is made dynamically using an adaptive routing function.

![A Bluetooth piconet](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1108.png)

**Figure 11.8. A Bluetooth piconet**

The network can be aware of up to 28-1, or 255 devices. A piconet or scatternet can have eight devices, one master and seven slaves as indicated in [Figure 11.8](ch11.html#a_bluetooth_piconet). A device can be a master in more than one piconet, and devices can be both masters and slaves on two or more piconets. When registered devices are not active they are in the "parked" mode, indicated by devices marked P in [Figure 11.8](ch11.html#a_bluetooth_piconet). When a device is on, it initiates device discovery to see which devices are within communication range. To connect to a network, a device must have a name, an address in the form ##.##.##.##.##.## (six number pairs), and a Bluetooth passkey (PIN). The passkey is a shared secret password that the remote device provides, which can be used to cryptographically authenticate each of the endpoints in the connection. This is a unique identification number that is provided by the manufacturer of the device at the time of fabrication and is dependent upon the device category. That ID isn't used as part of the Bluetooth handshake; the user-assigned friendly name is used instead.

Data is transferred over a Bluetooth network in the form of packets up to 2,745 bits in size. About 80 percent of these packets are the payload or data, and those remaining are used for the header and for protocol settings. Communication begins when a device chooses one of the 79 random channels and starts sending data. Channels switch every 625 microseconds, or at a rate of nearly 1,600 cycles per second. A packet can be sent on up to five different time slices. Should another device pick the same channel, the error-checking routine recognizes that it is the wrong data and has the devices retransmit the packets.

Because the chances for the first collision are 1 in 79 (1.3 percent), the chances for two or more collisions are miniscule. The second collision would have 1 chance in 792 (0.016 percent), the third would have 1 chance in 793 (0.000021 percent), and so forth. However, you can see how much the odds change when the Bluetooth bus is fully populated with eight devices. Then the odds would be 7 chances in 79 (8.9 percent), 7 in 792 (1.6 percent), and 7 in 793 (0.00014 percent). It is the availability of frequency channels that limits the device count.

Bluetooth connections can be either full duplex or half duplex. In full duplex, a device can send and receive, but in half duplex it can only do one or the other. Full-duplex devices, such as a phone, transmit and receive voice at the rate of 64 Kbits/s. With that speed for a transfer rate, it is possible to have multiline phones that support multiple conversations. A half-duplex Bluetooth connection from a computer to a printer is much faster, up to 721 Kbits/s. When a computer-to-printer connection uses two half-duplex channels, they both operate at up to 432 Kbits/s.

Bluetooth connections can be categorized as either Synchronous Connection Oriented (SCO) or Asynchronous Connectionless Oriented (ACO). For the synchronous type (SCO) of Bluetooth connection, a master-slave relationship is formed; one master device can connect with up to three slave devices, with each connection having a data rate of 64 Kbits/s. These devices don't experience collisions during an exchange because the master device coordinates the channels that are used. The asynchronous type of connection (ACO) allows the master device to connect with only one slave, but still retains the property that the master initiates and manages all data that is exchanged.

### Profiles

Bluetooth devices use a system of profiles to establish their device characteristics so that the network provides the necessary services to them. Devices must transmit the name, class, a list of services, features, manufacturer, clock offset, and the version of Bluetooth that the device uses upon demand. Different profiles enable different protocols and contain information on the format of data that can be exchanged, as well as what is required from devices that are managed by a different profile. Perhaps the best way to think of a device profile is that it is a description of a Bluetooth network interface.

There are around 28 profiles defined by the Bluetooth SIG, with an additional 4 that are at review stage. As an example, let's look briefly at a couple of the networking profiles. When you have an older Bluetooth device that connects to a LAN, such as a Bluetooth hub, it might use the LAN Access Profile, or LAP. LAP allows a device to connect to an IP network through any physical connection. LAP specifies the use of the PPP over the RFCOMM (Radio Frequency Communications) Bluetooth protocol.

A more recent device might connect to the same network using the Personal Area Networking (PAN) profile, which employs a different Network layer (OSI Level 3) protocol. Or perhaps you have a laptop that connects to a network through a Bluetooth phone. In that instance, the profile used would probably be the Dial-Up Networking (DUN) profile, which is similar to the Serial Port Profile (SPP) and uses the common modem AT command set and PPP. This is information that is negotiated between the two endpoints of a Bluetooth connection and ensures that the correct data types are used.

# Summary

In this chapter, you learned about small networks called Personal Local Area Networks, or pLANs. They are small in terms of users and/or area of coverage.

Peer-to-peer (P2P) networks can also involve a small number of users, and sometimes a small geographical area. A workgroup is an example of a P2P network that is composed of a dozen or fewer members. P2P networks can also be distributed applications deployed on many systems and over a large area.

You learned about both pure P2P and hybrid P2P systems. Some of the examples that you looked at were Gnutella, Freenet, Napster, and BitTorrent.

Some computer buses play the role of personal networks. The three that were examined from a network and architecture viewpoint were the Universal Serial Bus (USB), FireWire (IEEE 1394), and Bluetooth.

In the next chapter, you will move up the network food chain to local area networks. [Chapter 12](ch12.html) looks at various ways of creating local area networks from the standpoint of software, addressing, and factors that aren't related to hardware.
