# Chapter 7. The Network Interface

**IN THIS CHAPTER**

- Physical and logical interfaces
- Physical and logical interface addresses
- The binding and provider order's effect on performance
- Multihomed isolation and routing
- Network card features

An interface occurs where two different media or substances form a boundary. Each of the connections in a network is a network interface, and that interface represents the boundary between the physical transport layers that transfer communication and the layers that prepare data for use with applications. A network interface is addressable, that is, a signal can be sent over physical media meant for that specific interface.

In most networking books, the concept of a network interface isn't clearly defined and is discussed only in relation to various topics. However, I begin this chapter by defining a network interface. Network connections and their properties are important concepts that apply to networks of all types and are also covered in this chapter. From an outside perspective, the network interface is the only representation of a networked device that an outside observer sees.

# What Is a Network Interface?

Let's begin by defining what a network interface is. A network interface is the boundary between two different types of networking media. *Network interface* is a loose term that can be applied to any of the following:

- The point where two different networks meet, particularly in a topological or architectural diagram
- A network card, an ASIC (Application Specific Integrated Circuit) chip on a motherboard, a PC Card in a laptop, a USB/Ethernet connector, or some other similar kind of hardware device
- A virtual operating system object that can be manipulated programmatically
- The name given to each network connected to a router, which is an intelligent network switch
- The point at which a terminal connects to a network
- The point at which a switched public telephone network connects to a private telephone network

You may encounter the term *network interface unit* (NIU), which is used to refer to any network interface device that connects devices to or in a *local area network* (LAN). The NIU performs the function of sending and receiving data, as well as translating the communications into a protocol that is capable of being sent to the particular network type that the NIU serves. It is common for an NIU to contain a memory buffer so that if the communications must be resent, the data will still be in the NIU and will not have to be fetched from the sender.

## Physical network interfaces

A *network interface card* (NIC), also referred to as a network adapter or less frequently as a LAN adapter, is an example of a physical network interface device. In the ISO/OSI Reference model that you learned about in [Chapter 2](ch02.html), a network card is both a Layer 1 and Layer 2 device, spanning both the Physical and Data Link layers, respectively. A NIC's function is to receive communications from the network and to provide the necessary translation services so that the communications can be either forwarded to another network address or transmitted in a form that another networking component can modify so that the data it contains can be prepared for use by an application. A NIC is a type of NIU.

The network card doesn't alter the data being sent, but processes the packets or frames to modify the header or wrapper portion of the data, if required. For most network cards, the processing is directed by the chipset on the card but performed by a system's CPU. Network I/O is one of the key performance metrics that can place a limit on a system's performance.

Busy network interfaces can consume a system's processor resources and bring a computer to its knees. For desktop systems this is rarely a problem, but in high-performance networking where systems are I/O limited, it is a major issue. Web servers rely on network I/O for their performance, and are often I/O bound. Some NICs and advanced motherboards now incorporate special ASICs to offload the processing of the entire TCP/IP stack to a network controller, a technology called TCP offloading. The *TCP Offload Engine* (TOE) is optimized to process TCP headers.

### Note

[Chapter 16](ch16.html) covers TCP offloading in more detail.

Network interface chips are now built into nearly all motherboards because the network chipsets are inexpensive, and on-board networking is a very convenient feature to have. Many high-performance motherboards, such as those used in gaming, workstations, and servers, come with two network interfaces, which provides a number of different configuration opportunities. Three network interfaces are:

- **Redundant**. If one interface fails, you still have a second operational network interface to work with.
- **High performance**. The two interfaces can both be communicating at the same time.
- **Isolated**. Each network interface can be assigned to different networks, which is the essential function of a router.

## Logical network interfaces

Network interfaces have both a physical and a logical implementation. Most of the definitions in the bulleted list above describe a physical network interface. However, a network interface can be the logical point of connection between a system and a network. You can think of a logical network interface as being a software module or routine that emulates a hardware device. A logical network interface can accept network traffic, as well as send network traffic; it also behaves as if it is an I/O redirector. Keep in mind that logical network interfaces (or adapters, if you will) still use a system's physical network interfaces to handle network traffic.

One important example of a logical network interface (also called a virtual interface) is the loopback adapter. The loopback adapter is a software routine that emulates an internal NIC card that can accept system requests and reply to those requests. The loopback adapter is used to test whether network functions are operating correctly.

For IP version 4, the loopback adapter is found at

```
127.0.0.1
```

and for IP version 6, the address is

```
::1
```

You can `PING` these addresses, and they respond when a system's networking function is active. In instances where a system's NIC cards are malfunctioning or improperly configured, some operating systems return the address of the loopback adapter for any `PING` that initiates from the local system. The loopback adapter is a diagnostic function that isn't accessible from outside of the system being tested.

Modern operating systems implement a network interface as an object whose properties can be manipulated programmatically. Object-oriented programming languages can instantiate (create) a network interface, query the network interface to determine its properties, send data to the interface, or change the properties of the object and therefore change the operating parameters for the interface.

In the Java programming language, for example, you might use the `java.net.NetworkInterface` object class to create network interface instances. You can query a system to enumerate all instances of network interfaces; use the `getInetAddresses()` command to list the IP addresses of a network interface; use other methods to act on an interface; and programmatically alter an interface's properties. These types of commands and network interface objects exist for all other programming languages. The Microsoft .NET Framework also has a rich network interface object that can be manipulated using the C# programming language.

### Note

For a brief tutorial on how to manipulate network interfaces with the Java programming language, go to `http://java.sun.com/docs/books/tutorial/networking/nifs/index.html`. A similar online reference for .NET may be found at `http://msdn.microsoft.com/en-us/library/system.net.aspx`.

# Network Addressing

From a network viewpoint, the network interface *is* the system, as the interface stores the system's unique address and also provides the means by which network I/O can be directed to and sent away from any system. The address in a network interface is something that must differentiate one specific network card from another, even when both cards are identical models from the same manufacturer.

## Physical addresses

In Ethernet networks, that address is a unique 48-bit number that is called the *Media Access Control* (MAC) address. MAC addresses are contained in every single network card; they are a unique address given to it by the manufacturer at the time of its manufacture and encoded in a *read-only memory* (ROM) card. In Ethernet networks, the *Institute of Electrical and Electronics Engineers* (IEEE) defines the standards by which vendors assign their MAC addresses using a unique registry. When you create a virtual network interface, a MAC address is assigned to the interface by the virtualization environment.

The MAC address is a physical address, as it is bound to a device. MAC addresses may be spoofed (faked), but they can't be duplicated.

In order to allow a network interface to seamlessly move from one network to another, each interface is assigned a network address. You can consider this assignment to be equivalent to giving the interface a logical address, and network addresses can be assigned at will. A network address that is assigned permanently to a network interface is called a *static address*. One that is temporarily assigned is called a *dynamic address*. For a network to function properly, no two network addresses on the same network may be the same. Network addresses can be reused on different networks or network ranges, called *subnets*, but duplicates on the same subnet will result in network errors.

A common form used to address a physical network interface is exemplified by the Solaris nomenclature:

```
<driver-name> <physical-unit-number>
```

The interface would then be named

```
hme0
hme1
```

and so on. Other forms of UNIX and variants of Linux use similar schemes, but Windows uses long names for network interfaces.

[Figure 7.1](ch07.html#network_interfaces_appear_in_the_network) shows the Network Connections dialog box in Windows Vista 64. This dialog box shows that the computer has four network interfaces. Local Area Connection and Local Area Connection 2 are physical interfaces that are 1000Base-T ports associated with the Realtek I/O chipset on the motherboard; one is running and the second is unplugged (which is indicated by the X on the icon). VMnet1 and VMnet8 are virtual network interfaces. VMnet1 is associated with Ubuntu 8.04 (Hardy Heron) running in a VMware virtual machine. VMnet8 is associated with Windows Server 2008 Enterprise Edition running in a second virtual machine.

![Network interfaces appear in the Network Connections dialog box in Windows (in this figure, Vista 64).](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0701.png)

**Figure 7.1. Network interfaces appear in the Network Connections dialog box in Windows (in this figure, Vista 64).**

Different network types use different addressing schemes, but all network types rely on the assigned network address being unique on a network. When duplicate addresses are detected, the operating system should post an error message, but in some instances you may simply encounter strange network behavior.

## Logical addresses

A logical network interface appends an additional identifier to the names given to physical network interfaces. In an operating system such as Sun Solaris, the format would be

```
<driver-name> <physical-unit-number>:<logical-unit-number>
```

The *logical unit number*, or LUN, means that there can be multiple logical network interfaces for the same system. You can configure logical network interfaces or virtual interfaces so that they can be assigned a number of IP addresses, and those IP addresses do not need to be in the same range (subnet) as the physical network interface. This allows a single system to appear as if it is many systems to the network.

### Note

LUNs become important when network interfaces are attached to resources connected to servers. Storage servers use LUNs to connect to disk systems and RAID arrays. Because a LUN is a unique network path, its specification provides security features, protocol assignments, and other features that network interfaces offer to computer systems to the data contained on these storage assets.

Instances of LUN naming convention would include

```
hme0:1
hme0:2
hme0:3
```

and so on.

For example, if you run a virtual machine environment such as Microsoft Virtual PC or VMware Workstation, then each of the virtual machines you create can have one or more virtual interfaces. Each of those logical interfaces is not only assigned a unique IP address but can also be assigned a unique host name. That's the case shown in [Figure 7.1](ch07.html#network_interfaces_appear_in_the_network), where you see two virtual network interfaces: one for Ubuntu and another for Windows Server 2008.

The use of multiple virtual network interfaces can be applied to:

- **Mission critical systems**. Redundant adapters can be configured to fail over when there is a problem with the primary adapter.
- **Improved performance**. Multiple adapters can be load balanced to optimize performance.
- **Application isolation**. An interface can be assigned to a specific application, or instance of an application.

For example, modern Web server software such as Internet Information Services (IIS) from Microsoft, or Apache, allows you to create virtual Web sites, to which a unique logical network interface can be assigned. From the standpoint of a network client, the individual Web servers appear as if they are separate systems on the server.

When you create and use virtual network interfaces, you are creating a software emulation, which has no additional cost. You can access an individual host more directly with a virtual network interface, and that makes it easier to specify tasks such as network backups, or to administer systems on a host-by-host basis.

Keep in mind that all virtual network interfaces still require a physical NIC or similar NIU through which network communication must flow. The more virtual interfaces you create, the heavier the network load can be during production. Also, when you start up a system, each of the network interfaces must be instantiated, which adds more time to the system startup. Network interfaces are complex data objects, and so when you have many network interfaces (both real and virtual), startup time can increase dramatically.

# Configuring Network Interfaces

Network interfaces are so central to the successful operation of a computer system that every network operating system has at least two, and usually more, methods for querying, creating, and modifying them. For network adapters that use the TCP/IP protocol, you can query all of your system's network interfaces using the following procedures.

In Windows:

1. Click Start![Configuring Network Interfaces](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U001.png)
2. Type **CMD**, and then press Enter.
3. Type **IPCONFIG /ALL**, and then press Enter.

A listing of your network adapters, their MAC addresses, network addresses, and status appears in the Command Prompt window, as shown for Windows Vista 64 in [Figure 7.2](ch07.html#the_ifconfig_solidus_all_command_in_wind)

![The IFCONFIG /ALL command in Windows Vista 64 shows the status of all network adapters.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0702.png)

**Figure 7.2. The `IFCONFIG /ALL` command in Windows Vista 64 shows the status of all network adapters.**

In Ubuntu 8.04:

1. Click Applications![The IFCONFIG /ALL command in Windows Vista 64 shows the status of all network adapters.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U001.png)
2. Type **IFCONFIG**, and then press Enter.

[Figure 7.3](ch07.html#the_ifconfig_command_in_ubuntu_linux_lis) shows the output of the Ubuntu Terminal window, with one emulated Ethernet adapter (`eth0`) and the loopback adapter (`lo`).

![The IFCONFIG command in Ubuntu Linux lists your network adapters.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0703.png)

**Figure 7.3. The IFCONFIG command in Ubuntu Linux lists your network adapters.**

Notice that the physical address, called a MAC address in Windows, is called the HWaddr in Ubuntu, and that it appears on the first line that is returned for each adapter. The second line in [Figure 7.3](ch07.html#the_ifconfig_command_in_ubuntu_linux_lis) displays the assigned network address for IP version 4, and the third line is the IP version 6 address.

The `IPCONFIG` on Windows and the corresponding `IFCONFIG` commands on Macintosh/Linux/Solaris/Unix can take a large number of switches and options that can be used to create and modify network interfaces. Although the `IFCONFIG` commands are very similar from one operating system to another, particularly when it comes to UNIX, Linux, and Macintosh, there are differences between each operating system. Therefore, you should check the MAN pages for these operating systems, or the help page for Windows, to learn more about these commands. [Figure 7.4](ch07.html#the_ifconfig_command_man_page_in_ubuntu) shows the Ubuntu MAN page for `IFCONFIG`. A MAN page is the online manual's explanation for that particular command.

### Tip

Search engines, such as Google, index the online compilation of operating system manuals. They are particularly good at finding commands. If you type IFCONFIG, for example, several different Linux distributions appear at the top of the returned results. If you want the syntax of the Sun Solaris `IFCONFIG` command, then type the search term IFCONFIG `site:Sun.com`.

![The IFCONFIG command MAN page in Ubuntu Linux](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0704.png)

**Figure 7.4. The `IFCONFIG` command MAN page in Ubuntu Linux**

Modern operating systems are replete with graphical utilities for working with network interfaces. In Windows, as you have already seen, you can use the Network Connections dialog box to view your network interfaces; and you can get to this dialog box through either the Network Control panel or through network icons in the System Tray. Nearly all common network operating systems have some version of a Network Control panel from which you can start to configure your network adapter and interfaces.

Another method that is used to configure network interfaces involves scripting languages and network management interfaces. SNMP (Simple Network Management Protocol)-enabled hardware can be queried directly for its properties, and can be modified, as can WMI (Windows Management Instrumentation) on Windows. Virtual network interfaces don't have a physical existence, and so they can't be directly managed. A virtual adapter is a creation of an operating system; therefore it is the system object that must be queried. UNIX has a rich *command-line interface* (CLI) for managing system properties, which include network functions. In Windows, a progression of more powerful scripting environments has been introduced over the years, resulting first in the Windows Scripting Host and more recently (with Vista/Windows Server 2008) the PowerShell command-line scripting system.

# Bindings and Providers

The collection of software modules that reside between the NIC's Level 2 Data Link layer software and the applications found in the Level 7 Application layer in TCP/IP networking (based on the ISO/OSI networking model) is referred to as the *network stack* or *TCP/IP stack*. As incoming communication is transformed to data, it travels up from Level 3 through to Level 6. When data is outgoing, it is transformed into communications as it travels down from Level 6 to Level 3. The details of this discussion are described in [Chapter 2](ch02.html).

In the Windows TCP/IP stack, for example, all of the installed network components are bound to each of the installed network adapters by default. That means that as different types of data and communication traffic passes through the stack, there are different pathways that the data can take. As the stack is traversed, the operating system sends the data and communications to the first module or protocol in the list of components. If that protocol isn't able to correctly handle the information, then the next protocol is sent the information until the entire stack is traversed.

The order in which components are used in the network stack is referred to as the *binding order*, and it is something that you can modify, and by doing so optimize network performance. When an operating system imposes a binding order, it has no idea which protocols you might use, and which you won't. When you don't have the requisite protocol, that particular class of networking doesn't work on your system. The solution to the problem is obvious: you add the component you need to your binding order. When you have protocols that you don't need, you impose unneeded network overhead on your system.

Each adapter stores and maintains its own binding order, and so you can add or remove components and/or protocols from each adapter, as well as change the order in which the components are expressed in the binding order. Not all operating systems allow you to manage the binding order, which is considered to be a more advanced feature, but most network operating systems used on servers do. On a desktop, modifying the binding order probably doesn't change the performance of the system, as most of the time desktops have modest network I/O. However, in systems that are network I/O limited, optimizing the network stack can make a significant difference in system performance, lowering CPU processor loading and improving data throughput. Systems of this type include Web servers, thin client terminal servers (such as Citrix server products and Windows Terminal Server), telephony servers, director- (enterprise-) class switches and routers, and many other server types.

To access the binding order in either Vista or Windows Server 2003, do the following:

1. Click Start![Bindings and Providers](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U001.png)
2. Click the Network and Sharing Center link, and then click the Manage network connections link.
3. In Vista, press Alt to view the menu (not necessary in Windows Server 2008), click Advanced, and then select Advanced Settings.
4. Click the Adapter and Bindings tab, and then select the connection you want to view or modify.
5. Click Bindings for <*ConnectionName*> and then use the Up and Down arrow buttons to modify the binding order, as shown in [Figure 7.5](ch07.html#the_binding_order_comma_as_shown_in_vist).![The binding order, as shown in Vista 64](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0705.png)**Figure 7.5. The binding order, as shown in Vista 64**
6. Click the Provider Order tab (shown in [Figure 7.6](ch07.html#the_provider_order)) to view or modify the network provider order (NPO); the network interface uses the provider order to prioritize communication with the other devices on the network. You can use the arrow buttons to modify this order.

Changing the order of either the bindings or the providers will affect your interface's performance, so be sure to test the impact of any new settings.

Windows uses the term *network provider* to describe a dynamic link library (DLL) that contains the routines necessary to connect with other network types, such as Novell, which is exposed through a network provider API. Each provider is a client of a Windows network driver and is responsible for creating and managing connections.

![The provider order](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0706.png)

**Figure 7.6. The provider order**

There's no rule that the network stack must be an operating system function, although that architecture allows new features to be added and code to be optimized more easily than code embedded in hardware. The transition from the Windows XP/Server 2003 core to the Windows Vista/Server 2008 core included a completely rebuilt network stack that exhibited some dramatic improvements in areas such as Server Message Block (SMB) file transfers.

# Isolation and Routing

A general-purpose computer or a special-purpose computer that functions as a network appliance can have two or more network adapters. When there is only a single adapter, the system is referred to as *single homed*; with two network adapters it is *dual homed*; and when there are multiple network adapters, the system is referred to as *multihomed*.

There are many good reasons to have multiple network adapters in the same system, among which are the following:

- **Improved performance**. You get additional throughput when you add more network adapters.
- **Fault tolerance**. A system can be configured so that if one network adapter fails, traffic is directed to a backup.
- **Multipurpose Use**. One network interface can be used for network communications, while a second network interface can be used for system management, fault tolerance, or high-performance connections.Early dual network-ported motherboards used one high-speed interface and a low-speed interface, such as 100Base-T (100 Mbits/s) Ethernet and 10Base-T (10 Mbits/s) Ethernet, respectively, in combination. Later variants used 1000Base-T (Gigabit, or GigE) Ethernet along with a 100Base-T connection. As high-speed Ethernet chips have dropped significantly in price, it is rare to find a motherboard that offers two network interfaces that doesn't have both as high-speed network interfaces.
- **Routing**. Two or more network adapters define a path or route that can be managed, based on factors you specify.
- **Isolation**. Routing provides two very desirable features that are essential for secure networking: physical isolation and protocol isolation, each of which is described briefly in the sections that follow.

All of these are good reasons to have an additional network interface in any computer. Networking functions are among the most heavily used system components, and they tend to fail more often than many other functions. The older any computer system becomes, the more likely it is that a newer network interface card will add more speed, better security, and most importantly, more up-to-date device driver support. The network interface device driver is a fundamental factor in determining the speed, stability, and compatibility of the network interface in any system.

## Physical isolation

In order for one device on a network to discover another device, the network interface of both devices must share the same network address range, or more precisely, be on the same subnet. If you have one computer with an IP address of 4.2.2.1 (which happens to be Verizon's DNS server address) and another computer with an address of 4.2.3.1, then you will not be able to browse the other system on your network; however, if the second system's network address were 4.2.2.224, then you would. This assumes that you are using a Class C subnet mask of 255.255.255.x. That is called physical isolation, and it is a fundamental method that firewalls, gateways, routers, and other devices use for security.

You may have encountered physical isolation if you have configured a firewall, gateway, cable modem, or wireless router on your network. When a vendor ships a device of this type, the device contains two network interfaces. One interface connects to the external network and is configured to accept a dynamic address from a service running on a server on the external network. That dynamic address for TCP/IP networks is assigned from a pool of addresses belonging to the external network. The second network interface in the device is given a private network address by the device's vendor that you need to change. Most often this address is drawn from a pool of private IP addresses that are reserved for use on internal networks and can't be used on a wide area network such as the Internet.

Let's say for the sake of argument that the device's internal LAN interface is set to the Class C network 192.168.1.1 and the computers on your LAN use the IP range of 192.168.3.1 to 192.168.3.255. Your system has an address of 192.168.3.52. That device will not be available to browse from your system using either your network discovery protocol (Windows NetBEUI, for example) or your browser's HTTP broadcast function. To view the device, you first need to change your system's network adapter to the range 192.168.1.x, and then browse for the device.

Now with both devices on the same subnet, you can browse for the device and configure it in the manner that the device vendor allows. Older devices used management utilities for device configuration, and many large servers and systems that play the role of physical isolation still do. However, newer devices and nearly all consumer-level network devices ship with small Web servers and are configured through your browser. Therefore you would open a browser, and enter the following address into the address bar:

```
http://192.168.1.1
```

That address should take you to a login page, which, after you supply the necessary credentials, will allow you to modify the device's LAN interface, which includes the address. If you change the device's address to 192.168.3.2 (which usually requires a device restart), then the device is now visible to members of your network. It will also be available to the system you are using after you change the network interface from 192.168.1.x back to 192.168.3.52.

### Tip

Make it a point to change the default login name and password, as well as the default LAN address of a device providing physical isolation. These defaults are known to hackers trying to gain access to networks.

Physical isolation works because communications arriving at the external network interface are only aware of that network interface's address. External communications have no idea what the address of a device on the internal network might be and require a mechanism to identify the internal address that only exists in the routing device. That mechanism might be a network address translation table (called a NAT) in a router, or it could be a forwarding system that is part of a proxy server. A proxy server is a server that receives communications from external devices, acts on them in some way (filtering, caching, anonymizing, or some other function), and then redirects the communications to another system. Internet Security and Acceleration Server (or ISA Server) from Microsoft is an example of a proxy server.

## Protocol isolation

Protocol isolation works by using one network protocol for external network traffic and a second protocol for internal LAN communication. With a transport protocol such as TCP/IP, the packets are routable; given enough time and resources, it is possible for an outside user to circumvent different methods of security. Protocol isolation adds yet another layer of complexity to the task presented to intruders. If the internal network is running another network protocol such as NetBEUI from Microsoft or IPX/SPX protocol from Novell, then access to shared resources such as a file share requires the use of communications formatted using those protocols. Because both of these protocols are non-routable, communications in this form cannot originate from an external network.

Protocol isolation is helpful for securing data on the network, but it provides no additional barrier to intrusion from the external network. Unless some means is provided to block TCP/IP traffic, systems that are on the internal LAN are discoverable by other systems. However, because these systems aren't sharing any of their resources over TCP/IP, there are no resources that an external system can connect to. Protocol isolation is best used for devices that don't require TCP/IP to communicate with other devices. An example of this type of system is storage servers running the SAMBA file sharing service, which can use the Server Message Block (SMB) protocol to communicate with servers. Should you want to make a SAMBA file server available to external network systems, you still require a gateway or a network adapter on the internal device with both protocols bound to it.

# Bus Interfaces for NICs

Network interfaces come in a wide variety of forms and are used for a variety of different networks. Among the types of network interfaces you will encounter are interface chips found in:

- On-board (on the motherboard) network controller chipsets
- Add-in cards for common expansion buses
- Wired peripheral buses such as USB
- Wireless technologies such as 802.11*x* or Bluetooth

Network cards follow the current technology of the day. For PCs, the first add-in network adapters were ISA (Industry Standard Architecture) cards. The most common network cards found today are PCI (Peripheral Component Interconnect) cards.

High-performance network cards appear first on the higher-performance bus types, which for PCs today is the PCI-X interface. Therefore, you will find network cards available for PCI-X that include single-channel Ethernet adapters that fit into the small 1X PCI-X slots on a motherboard. 1X-Ethernet cards currently range in price from $20 to $100, and because they offer no compelling performance advantage, they really just represent a replacement of the current generation of PCI network cards by newer technology. PCI-X cards are backwards compatible with the PCI bus, provided that the voltages are compatible. Older PCI cards were 5 volts, while the current PCI Revision 3.0 uses a voltage of 3.3 volts. Therefore any PCI-X card rated at 3.3 volts can be used in a PCI slot. PCI cards can also be used in a PCI-X slot provided that the PCI card has the right voltage and that it can physically fit into the edge connector.

PCI-X has twice the bus width and runs at up to four times the clock rate, but uses the same bus protocol and electrical settings. The theoretical throughput of a PCI-X (1X) bus slot is 1.06 GB/s, which compares to 532 MB/s for the PCI bus. The speed used by either the PCI or PCI-X bus is limited to the speed of the slowest card used. You will find that current motherboards separate their PCI-X slots into separate channels to improve system performance.

PCI-X has a number of additional features that make it attractive, including the ability to restart or hot swap cards, and scalability. Hot swapping allows you to remove and add a card while a system is running, which is important for any server that must be highly available. PCI-X slots come in 4-channel (4X) and 16-channel (16X) versions with theoretical throughput rates of 4.2 GB/s and 17 GB/s, respectively. Therefore you find that server network cards that have multiple ports and advanced interface standards such as InfiniBand or iSCSI that need these higher throughputs come in 4X and 16X form factors.

The expansion card for laptops in widespread use was called a PCMCIA Card, now thankfully shortened to PC Card. The original acronym stood for Personal Computer Memory Card International Association, and the standard is now at PCMCIA 2.0.

The PC Card standard is not a bus standard, per se; it is a packaging standard. PC Cards were first made for memory expansion and were then expanded to modems and even hard drives. However, the most common use for PC Cards has always been for the addition of network interfaces to laptops. There are four standards in use — Types I, II, III, and IV — with the primary difference being the thickness of the card. Type II is the common size for NICs, which are between 5 and 5.5 mm thick, offer either a 16- or 32-bit interface, and usually run at 3.3 volts. At that form factor, PC Cards can support RJ45 Ethernet connections.

In another example of adapting a network adapter to an available computer bus, you can attach a network adapter to a USB port. Wired and wireless Ethernet adapters are both common and valuable devices to have handy. Should your computer networking cease to function properly, you can plug this device into a spare USB port and check to see if it connects properly.

**PCI-X bus versus the PCI Express (PCI-E) bus**

The PCI-X bus is different from the PCI Express (PCI-E or PCIe) bus, although they are often confused because their names are similar. PCI-E is a full-duplex serial bus that is used for high-speed peripheral devices such as storage arrays or RAID systems. PCI-X is a parallel bus that is a half-duplex bidirectional device. In a half-duplex device, half of the channels must be outgoing and half must be incoming. A full-duplex bidirectional device can communicate with any number of channels incoming or outgoing.

These buses are electrically different, and the cards that they use are keyed differently. The current standard of PCI-E 1.0 x1 offers 32 lanes of up to 250 MB/s for a throughput of 16 GB/s, up to 8 GB/s incoming and 8 GB/s outgoing. The serial architecture makes PCI-E easier to manage, and allows each lane to automatically negotiate the best throughput speed; however, PCI-X is limited to the slowest device speed.

## A sample network adapter

The D-Link DGE-560T Gigabit PCI-X adapter shown in [Figure 7.7](ch07.html#the_d-link_dge-560t_pci-x_network_adapte) illustrates some of the common features found in network cards. The 560T fits into a PCI-X 1X slot and allows Ethernet transfer speeds of up to 2 Gbits/s, on either a 16- or 32-bit bus. A 2 Gbit/s throughput corresponds to 0.25 GB/s or 250 MB/s. The card supports a number of management protocols such as SNMP, remote network boot using either Preboot Execution Environment (PXE) or RPL (Remote Initial Program Load protocol), Advanced Power Management, and Wake-on LAN, as well as being hot-plug capable.

![The D-Link DGE-560T PCI-X network adapter](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0707.png)

**Figure 7.7. The D-Link DGE-560T PCI-X network adapter**

The largest black chip on the card is the network controller. This card is 10Base-T, 100Base-T, and 1000Base-T compatible, and like many multispeed cards has activity lights to indicate its condition. The light above the RJ45 connection is an activity light; it lights up as data is being sent or received. The light below the RJ45 connection is dark when a 10Base-T connection is detected, green when communication is at the 100Base-T level, and yellow when the adapter is operating at 1000Base-T. Many adapters actually have two or three separate lights for this purpose. An interesting feature of this particular card is that it ships with a utility that can detect if there is a problem with the cable attached to the NIC.

If you are running a version of Windows, you should be aware that the Windows operating system can display a network interface activity icon in the System Tray. In Vista, you enable this option in the Notification Area tab of the taskbar and Start Menu Properties dialog box; in Windows XP, it is enabled on a case-by-case basis in the Properties dialog box for each network interface. The icon isn't merely for show, but serves the same function as the activity lights on a NIC card. As shown in [Figure 7.8](ch07.html#the_windows_status_tray_network_interfac), the network icon is composed of two different computers.

The front computer is the local computer, and it lights up when the network interface is receiving data. The back computer is the remote system, and that icon lights up when your local system is sending data to a remote system. So the animation of the blinking lights in the icon is a good way to analyze your system's network interface function at a glance. Other operating systems have similar utilities, including Performance Monitor applications that allow you to monitor network I/O with much finer granularity.

![The Windows Status Tray Network Interface icon](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0708.png)

**Figure 7.8. The Windows Status Tray Network Interface icon**

## Network drivers

All of these different network interface form factors work because each card or adapter has a network controller chip that can be addressed over the particular bus used. There may be many different NIC vendors, and many different NIC forms, but there are only a few network controller chipsets in use. The software required to communicate with different chipsets and network drivers is often bundled into an operating system's distribution. Operating systems that have an automatic configuration option load the correct driver when the system recognizes that particular chipset. Windows Plug and Play (PnP) architecture is an example of an automatic configuration system.

Unlike graphic cards, where the driver software changes frequently, network drivers don't often change substantially for a particular operating system. It's not uncommon to find that a network driver that works for an older version of an operating system such as Windows Server 2003 will also work for Windows Server 2008. However, it is considered to be best practice to use the latest driver for a NIC. The latest driver is probably considered to be the one that the card vendor — or for an embedded controller, the motherboard vendor — has on their Web site.

Don't assume that the disk in the box with your card or operating system distribution is the most current one. The operational differences between a current and an earlier version of a network driver may be subtle, but they may also be important. You may find that the newer version improves performance, cuts down on error rates, or improves compatibility. This isn't always the case, of course, and some drivers make things worse. But for the most part, vendors tend to improve their software over time.

Modern operating systems use a standard application programming interface, or API, to communicate with NICs. The Microsoft API is called the Network Driver Interface Specification, or NDIS. It was developed jointly by 3Com and Microsoft, at a time when 3Com dominated the Ethernet NIC category. NDIS is conceptually part of the Logical Link Control layer that occupies a sublayer that is part of Layer 2 of the ISO/OSI model, serving as the interface between that layer and the Network layer, which is Layer 3. Below the Logical Link Control layer is the Media Access Control, or MAC, device driver that is part of Layer 1, the Hardware layer. NDIS is part of Windows low-level network plumbing, creating and removing the addressing and wrappers that encapsulate data transmission.

Some Linux distributions ship with software that allows them to use NDIS-compliant network cards, but other operating systems use different network API standards to communicate with NIC cards. On Macintosh systems, Apple uses the Open Data-Link Interface (ODI) that they developed with Novell for their Logic Link Control layer software. ODI is similar to NDIS in that it is meant to be NIC card-vendor neutral.

Other network driver interface software that you may encounter includes the Uniform Driver Interface (UDI), which is a project that is trying to standardize a portable interface for device drivers. UDI may show up in a number of Linux or UNIX variants. The Universal Network Device Interface (UNDI) API is used by motherboard chipset vendors such as Intel to allow a NIC card to be accessed by the PXE protocol by a computer's BIOS. The PXE allows an administrator to remotely manage systems, install new operating systems, and perform system maintenance from a small, independent operating system.

# Summary

A network interface is a named operating system object that is configurable through software. Each network interface has a number of associated properties that are unique to that object. Among the properties is a unique physical address, called a MAC address, that is encoded by the NIC or controller vendor. Logical addresses that are meaningful to the particular network type that you use — TCP/IP, for example — are assigned to a network interface.

Network interfaces can be physical devices, as well as logical devices. A logical network interface is created by an operating system for use with virtual machines, as part of software that requires network redirection, and for many other purposes. From the standpoint of configuration, a logical network interface is a complete network interface, except that any logical network interface must still use a physical network adapter to send and receive network traffic.

One aspect of network interfaces that determines their capabilities is the network components that are enabled for use with that interface. This list is called the binding order, and the set of network types that can be used is called the provider order. The order of both determines how data is processed as it comes and goes from the network and travels through the network stack to an application. Both of these orders can be managed and modified.

When you have two or more network interfaces in a computer, it is referred to as multihomed. The ability to have different network addresses on these cards allows computers to be physically isolated from one another. When different network interfaces run different networking protocols or use different network providers, the system has the ability to isolate one adapter from another using protocol isolation.

In the next chapter, you learn about the different types of transport media used to build networks. These include wired cables, wireless connections, and other types of media.
