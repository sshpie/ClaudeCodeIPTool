# Chapter 20. Network Operating Systems

**IN THIS CHAPTER**

- Network operating system protocols and services
- Important features of a network operating system
- UNIX, Linux, Solaris, Novel NetWare, and Windows servers

A network operating system, or NOS, is one that is optimized to provide network services. The development of network operating systems has driven the development of computer networks, and vice versa. Both are intimately related.

Each NOS must provide operating system support for hardware, run protocols and services, and provide those services or applications for client systems. Beyond these basic services, an NOS may offer administration and management utilities, naming and directory services, file and print services, Web services, backup, security, and network routing, as well as serve as the operating system upon which network applications can be installed and run.

An NOS that has a broad range of capabilities is typically referred to as a *platform*. Examples of platforms are UNIX, Linux, and Microsoft Windows. Some NOSs are optimized for special purposes; an example of this kind of NOS is Cisco's IOS operating system that runs on its routers and switches.

In this chapter, different NOSs are described, and several of the more commonly found and popular NOSs are described in some detail, particularly those that are deployed on server hardware and in the client/server or n-tiered architectural model.

UNIX is the prototype NOS and has had the greatest impact on all of the other NOSs that have come after it. A brief history of UNIX and its design goals is presented in this chapter. Important features of UNIX networking, such as the POSIX, SUS, sockets, and STREAMS, are described.

The family of UNIX-like operating systems described as Linux is also considered in detail, as is the Sun Microsystems Solaris operating system. Also described is Novell NetWare and its contribution to NOS development, including Novell's latest version called the Open Enterprise Server (OES).

The last NOS to be considered is Microsoft Windows Server. Each of these three NOSs is a leader in some aspect of server deployment. In this chapter, you learn about some of their strengths and weaknesses.

# What Is a Network Operating System

A network operating system (NOS) is an operating system that is optimized to provide network services to other systems on a network. Nearly every commercial computer operating system built over the last 50 years has had some networking component.

True distributed network operating systems became necessary with the introduction of the first generation of personal clients. Early examples of network operating systems included products like Artisoft's LANtastic (now at version 8.0; `http://pcmicro.com/lantastic/`), which was described as a peer-to-peer NOS. LANtastic could network MS-DOS, Novell NetWare, and OS/2 clients, providing shared access to applications, files, printers, and optical drives. LANtastic was a very successful product prior to the introduction of Windows 95, but as operating system vendors began to focus on networks of personal computers, the functionality in native PC operating systems eclipsed the need for products like LANtastic.

In the early computer networking market, Novell's NetWare was the market leader on PC hardware, and was the first commercially successful NOS. Novell based NetWare on the Xerox Network Services stack, emphasizing the concept of file sharing. The first version of NetWare appeared in 1983, and achieved early market success based on IBM's validation of the product in 1984 at the time that IBM introduced the IBM PC. Early versions of NetWare ran on MS-DOS systems as Terminate and Stay Resident (TSR) programs, and could map network volumes to local drive letters. NetWare exhibited the full range of a true NOS; it could restrict access based on a user login, and be a print server. The Apple Macintosh, also released in 1984, had its own built-in networking capability, AppleTalk, which Apple continued to develop up until the dominance of TCP/IP networks.

By the time Novell released NetWare version 4 in 1995, the company was a major force in the personal computer industry. Microsoft's release of first Windows for Workgroups in 1993 and then Windows 95 did little to dent Novell's influence. It was only with the release of Windows NT that Microsoft was able to catch up.

Novell's IPX network protocol was widely used, but IPX has been deprecated in favor of TCP/IP. In fact, if you can point to one factor that shook out the computer NOS market and separated the current products from the early NOS, it was the rise of the Internet.

## Protocols and services

Today, an NOS can have a broad set of capabilities. Every NOS must perform the following three functions:

- Provide operating system support for the hardware that it runs on
- Run different network protocols and services such as addressing
- Run server applications that client systems — or for peer-to-peer networks, other peers — can access

An NOS may also provide some of the following network services:

- Network administration and management.
- Names and other directory services.
- Shared file and print, Web services, backup, or replication services.
- Security services, access control, and logins. A network operating system may function as a "Triple A" server, offering authentication, authorization, and accounting.
- Traffic routing on the networks and the control of access to ports.
- Participation in high availability options such as fail-over, clustering, or run on fault tolerant (FT) or highly redundant systems.
- Scalability features such as load balancing or support systems with large processor counts (either Symmetric Multiprocessor [SMP] or Non-Uniform Memory Access [NUMA]).

## General versus Special-Purpose NOS

Some NOS, such as Microsoft Windows, Novell NetWare, Sun Solaris, various flavors of Linux, and so forth, either come with nearly all of the aforementioned protocols and services in the box or have readily available add-on components that enable them. Therefore, operating systems of this type are referred to as *platforms* or, less frequently, as general-purpose NOS. Not all NOS need to be so broadly defined.

An example of a specialized NOS is Cisco Systems' IOS (which originally stood for Internetwork Operating System). IOS runs on nearly all of Cisco's routers and switches using a proprietary operating system. By contrast, Juniper Networks' JUNOS software, which the company describes as a router operating system, runs atop an implementation of FreeBSD. Special-purpose operating systems become valuable when a market category becomes large enough that the functions the category requires need to be emphasized and optimized. So, while early Internet routers often were built on various forms of Linux and the SunOS, Cisco was able to turn out even more capable routers at lower costs by creating a specialized NOS, and created an extremely successful company by doing so.

The development of general-purpose NOS has followed a somewhat different path. For the most part, platform NOSs are deployed on server hardware or as virtual machines. The tendency over the last decade has been to develop NOSs of this type as unified projects so that both the server and the client operating systems are derived from the same code base. Microsoft started this type of development effort with Windows 2000, and Windows 2003/XP and Windows 2008/Vista have followed in this mold.

Many server operating systems are now essentially the same core system as their desktop clients. The differentiation between the two arises when additional features are added, some features turned off, and other features are limited in some way. For example, Microsoft imposes a ten-connection limit for clients accessing a Web server on a Windows workstation. If you want to explore this topic in some detail, you can read about how to convert Windows Server 2003 into a Windows XP workstation at `www.msfn.org/win2k3/`. The process adds DirectX, Themes, System Restore, Java, and a number of other services back into Windows Server 2003.

Several server distributions of Linux follow this same pattern, but this isn't a universal pattern. Sun, for example, makes no distinction between Solaris as a server or a desktop operating system.

The network operating systems in common use are shown in [Table 20.1](ch20.html#common_platform_network_operating_system).

**Table 20.1. Common Platform Network Operating Systems**

| NOS Name | Owner | Current Version | Runs On |  |
| --- | --- | --- | --- | --- |
| AIX | IBM | 6.1 | 64-bit RISC systems | `www-03.ibm.com/systems/power/software/aix/index.html` |
| BSD | FreeBSD Project, NetBSD,OpenBSD | 7.1 4.0.1 4.4 | Alpha, ARM, x86, IA64, MIPS, PPC, SPARC64, SunOS4, and Xbox | `www.freebsd.org/www.netbsd.org/www.openbsd.org/` |
| Digital Unix (TruUnix) | Hewlett-Packard (through acquisition) | 5.1B-5 | Alpha (ends 2012) | `www.hp.com` |
| HP-UX | Hewlett-Packard | UNIX System V Release 4 | IA64, PA-RISC (ends 2012) | `www.hp.com` |
| IOS | Cisco Systems | 12.4 | Cisco routers and switches | `www.cisco.com/web/psa/products/index.html?c=268438303` |
| IRIX | Silicon Graphics | 6.5.23 | SGI systems, PowerPC processors | `www.sgi.com/products/software/irix/` |
| Mac OS X | Apple Computer | 10.5 | x86, PowerPC, and ARM v6 | `www.apple.com/macosx/` |
| NetWare (superseded by OES) | Novell | 6.5 SP7 (equivalent to OES 2) | x86 | `www.novell.com` |
| Open Enterprise Server | Novell | OES 2 SP1 | x86 | `www.novell.com/products/openenterpriseserver/` |
| OpenVMS | Hewlett-Packard (through acquisition) | 8.0 Itanium, 8.2 (maintenance) | Alpha, VAX, IA64 (Itanium) | `www.hp.com` |
| Red Hat Linux | Red Hat | 5 | x86, IA64 | `www.redhat.com/products/` |
| SCO OpenServer 6 | The SCO Group | 6.0.0 MP3 | x86 | `www.sco.com/products/openserver6/` |
| Solaris | Sun Microsystems | 10 | SPARC, x86, IA64 | `sun.com/solaris/` |
| Ubuntu | Canonical | 8.10 | x86, IA64 | `www.ubuntu.com` |
| Windows | Microsoft | 2008 | x86, IA64 | `www.microsoft.com/windows` |
| z/OS (formerly MVS) | IBM | 1.10 | IBM zSeries (MVS ran on System 360/390 mainframes) | `www-03.ibm.com/systems/z/os/zos/index.html` |

# NOS Systems and Software

In the previous sections, you've seen some of the general features of an NOS. There are literally hundreds of different types of NOS available on the market today; however, space precludes a complete description of all of the individual NOSs on the market. In the sections that follow, the most popular NOSs in use today are described in more detail, in particular:

- UNIX
- Linux
- Solaris
- Novell NetWare and Open Enterprise Server
- Windows Server

## UNIX

UNIX is characterized as a multi-tasking, multi-user, time-sharing NOS. It was designed around a kernel that could be more easily ported to other machine architectures (processor families) than previous operating systems, and separated user functions from kernel operations. The guiding philosophy, now sometimes referred to as the "UNIX philosophy," was to make the NOS and its components both modular and reusable.

UNIX was developed at Bell Labs for AT&T in the late 1960s and for which Dennis Ritchie developed the C programming language in 1972. Originally available under license from AT&T, the UNIX trademark is now owned by The Open Group, and the name UNIX or Unix is used by operating systems that are compliant with the Single UNIX Specification (SUS) that is described in more detail later in this chapter. Examples of UNIX operating systems include AIX, HP-UX, Solaris, and other systems that are based on UNIX System V, or alternatively, the last AT&T release, called Seventh Edition UNIX, Version 7 Unix, or simply V7 Unix. Caldera Systems acquired the rights to V7 Unix and released it into the public domain in 2002. UNIX is considered to be the enterprise NOS standard against which other enterprise NOSs are compared.

### Note

Is it UNIX or Unix? You see both variants of the name in common use. UNIX in all caps is a trademark of The Open Group, and the official name given to any version of Unix that is SUS compliant and licensed. As a general class of operating system, the mixed-case version of Unix is perfectly acceptable to my way of thinking.

Other operating systems derived from UNIX concepts, but not SUS compliant, are considered "UNIX-like" — the various distributions of Linux being a good example. The impact of UNIX on NOSs that came after it cannot be underestimated — that impact has been profound. You can get an idea of just how many NOSs are either UNIX or related to UNIX by examining the Levenez UNIX family tree (`www.levenez.com/unix`) shown in [Figure 20.1](ch20.html#the_unix_family_tree)

UNIX became a standard because AT&T distributed UNIX and the C programming language widely. The availability of UNIX for government and military applications, as well as a very liberal policy for distribution of UNIX to universities, led UNIX to be ported to more system types than any other operating system. UNIX became known as an "open system," although initially the license fees for commercial ventures ensured that it was not open. Versions of the UNIX operating system were developed at universities, particularly at the University of California at Berkeley (where BSD UNIX was developed) and at the Carnegie-Mellon Institute in Pittsburgh (which developed the MACH kernel). As these open versions became the leading-edge versions of UNIX, they greatly influenced AT&T's decision to make UNIX more widely available.

![The UNIX family tree](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2001.png)

**Figure 20.1. The UNIX family tree**

### POSIX

The UNIX interface and standardization around the C language eventually led to a set of design guidelines and APIs that became an NOS model architecture. POSIX (`www.pasc.org/`) or Portable Operating System Interface is an Application Programming Interface (API) defined by the IEEE 1003 and ISO/IEC9945 standard. The X in POSIX arises from the IEEE-IX version of the standard. POSIX makes NOSs interoperable and therefore has been nearly universally adopted. [Figure 20.2](ch20.html#the_posix_reference_architecture) shows some of the standard components in a POSIX reference architecture.

Familiar features of modern NOSs — including the hierarchical file system, stored plain text, the command line interpreter, inter-application or inter-process communications (IPC), concepts of shared memory, messaging and queues, semaphores, sockets, and others — were UNIX inventions, although they were not part of the original AT&T UNIX; they were added to later versions as it became necessary to support asynchronous I/O. The reliance on a system of storage, based on chunks of storage (bytes) rather than on a database record structure, also became an NOS standard.

![The POSIX reference architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2002.png)

**Figure 20.2. The POSIX reference architecture**

Perhaps the most important development from the standpoint of network services is that UNIX moved these services and the protocols that they required out of the operating system kernel, thus allowing developers to more readily adapt the operating system to rapidly changing networking advances. The adaptability of UNIX's networking is as responsible for its long-lasting impact as was the portability of the kernel.

### STREAMS and sockets

STREAMS and sockets are the two methods that UNIX uses to instantiate a network interface, and so they play a central role in establishing network services.

A socket is an endpoint for a network connection. When the socket allows for bidirectional IP data flow, it is referred to as an *Internet socket*; when a socket uses other types of protocols, it is referred to as a *network socket*, or more simply, a socket. Internet sockets have certain properties such as the protocol in use; an assigned IP address, port, or service number; and (once the connection is made) the remote IP address and port. These characteristics give sockets a unique identity.

Network operating systems use the concept of a socket as the interface between an application process and the network stack, allowing data to flow between the two. Sockets are an interface between a system and network I/O. The development of socket-based architecture has played an important role in the evolution of modern NOSs, and has made it easier to develop consistent network driver models and have different NOSs interoperate with one another.

You can list the available sockets in UNIX and UNIX-like systems (such as Linux) by issuing the command `netstat -an`. An alternative switch, `netstat -b`, lists sockets that have been established by different applications. [Figure 20.3](ch20.html#the_netstat_-an_command_allows_you_to_vi) shows a partial output of the `netstat -an` command on Windows Vista.

Perhaps the best known of all of the network socket architectures is the Berkeley Sockets API that was originally introduced with BSD UNIX v 4.2. That API was an AT&T copyright until UC Berkeley released a version of UNIX in 1989 that was open for public adoption with license. Today, Berkeley Sockets is considered to be a standard model for network socket design.

STREAMS is an alternative to Berkeley Sockets. STREAMS appeared first in UNIX System V. STREAMS is the network architecture used in UNIX System V for I/O to allow device or special file systems to communicate through a device driver to peripheral devices using standard I/O system calls. STREAMS is modular in construction and allows drivers (which are modules) to be chained together into a STREAM. STREAMS requires more overhead than Sockets does, and in all of the operating systems that continue to use STREAMS, a Sockets API is also included. STREAMS was a required component in the original Single UNIX Specification, but in the current SUS v3, STREAMS is an optional component.

![The netstat -an command allows you to view the status of network interfaces and sockets.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2003.png)

**Figure 20.3. The `netstat -an` command allows you to view the status of network interfaces and sockets.**

### Single UNIX specification

When most people think of UNIX, they tend to think of the many different versions of UNIX that are based on AT&T's venerable network operating system. The following network operating systems are all UNIX variants:

- IBM AIX 5L V5.2
- HP-UX 11i v3
- Mac OS X Server 10.5 (Leopard)
- SCO UnixWare 7.1.3 and SCO OpenServer 5
- Sun Solaris 10
- DEC Tru64 UNIX V5.1A (now owned and supported by Hewlett-Packard)
- IBM z/OS 1.9

These variants are currently certified as complying with the Single UNIX Specification (SUS). Linux and various versions of BSD UNIX are considered to be "UNIX-like" operating systems and are non-conforming to the SUS standard.

### Note

To learn more about SUS, you can read the SUS FAQ at `http://opengroup.org/austin/papers/single_unix_faq.html`.

The Single UNIX Specification is the result of an effort to standardize UNIX that was begun in the 1980s by the IEEE and the Open Group. Those efforts resulted in the POSIX.1 (from the acronym Portable Operating System Interface for unIX) standard that influenced the development of many NOSs in the 1980s and 1990s to set UNIX standards, which became known as the "UNIX wars" and led some of the leading UNIX vendors to form the Common Open Software Environment (COSE). COSE's most important achievement was the creation of the Common Desktop Environment (CDE), which blends the X11 environment with the OSF Motif user interface and toolkit.

From all of the aforementioned activity, the Austin Common Standards Revision Group (`www.opengroup.org/austin/`), or more simply the Austin Group, arose. SUS publishes a set of user and software interfaces that standardize programming for the POSIX shell, as well as a number of operating system utilities and services including file, terminal, and network services. All of the UNIX operating systems listed in the bulleted list are SUS compliant.

## Linux

Linux is a UNIX-like operating system that uses the open source Linux kernel. It appears that Linux may be the most widely deployed Internet server currently in use, at least from the statistics that can be determined from Internet usage studies. Netcraft (`www.netcraft.com/`), an organization that tracks Web servers in current use on the Internet, reports that the various versions of Linux ran on half the Web servers, FreeBSD ran on 30 percent, and Windows Servers accounted for the remaining 20 percent. Other studies based on hardware sales that seek to measure the overall server market show Linux to have a market share around 15 percent.

Linux's penetration as a desktop operating system is much more limited, although the Ubuntu distribution appears to have captured a few percent of the desktop market. Linux has become popular in the emerging "netbook" market, appearing in systems such as the ASUS Eee and Acer Aspire One.

Versions of Linux run on systems from small, embedded devices up to supercomputers. Among the supported platforms are x86, SPARC, IA64, PowerPC, Motorola 68000, and IBM s390. Linux has broad support from the major computer equipment vendors: Dell, IBM, Hewlett-Packard, Sun Microsystems, and Nokia all sell systems that run the Linux operating system and support the open source development effort. Linux also represents nearly 88 percent of the most powerful supercomputer systems listed on the Top 500 Supercomputer Sites (`www.top500.org/stats/list/32/osfam`), a statistic that surprises most people who first encounter it.

A number of major Internet sites are built using fleets of Linux systems, including four of the largest: Amazon, eBay, Google, and Yahoo!. A number of countries have made Linux their standard operating system for their government, including, most notably, some of the BRICK countries — Brazil, Russia, India, and China — as well as both Germany and France.

### Distributions

There are currently perhaps 100 active distributions of Linux based on the Debian, Gentoo, RPM, or Slackware-based distribution. Among the best known of the Linux distributions are Linspire and Ubuntu (which are Debian-based versions), and Caldera Linux, Red Hat Linux, and SUSE Linux (which are based on RPM). The classes of Linux are organized around the following features:

- Debian Linux, which uses the .deb package format and ships with a broad range of software that desktop systems tend to prefer
- Gentoo Linux, which uses the Portage package system and is usually highly optimized for performance on smaller, less capable devices
- Fedora Core, which uses the RPM file format
- Red Hat Enterprise Linux, another version that uses the RPM file format and is optimized for the server market

### Note

Wikipedia maintains a long list of Linux distributions with links on a jump page at `http://en.wikipedia.org/wiki/List_of_Linux_distributions`

The first version of the Linux kernel was released by its developer Linus Torvalds in 1991. The current version of the kernel as of February 20, 2009 is version 2.6.28.8. Most of the additional utilities and libraries arose out of the GNU open source operating system, which was begun in 1983 by Richard Stallman and the Free Software Foundation at the Massachusetts Institute of Technology's Media Labs.

The GNU project is also responsible for the GNU General Public License (GPL), now at version 3.0 (`www.gnu.org/licenses/gpl-3.0.txt`), under which Linux is distributed. The term *copyleft* is sometimes applied to the GNU license. Copyleft requires that a program or other artistic work (such as Linux) be distributed free of charge, and that all modified and extended versions of the work also be distributed freely. Companies such as Red Hat and Novell that distribute commercial enterprise-class versions of Linux charge for their distributions, which does not conform to the GNU GPL. Those companies are charging for support, as well as their modifications. To conform to the GPL standards, companies selling commercial versions of Linux support open source versions of Linux that do conform.

### LAMP

Linux tends to be deployed on commodity hardware and achieves large scale through horizontal scale out. Many Linux servers install what has come to be known as the LAMP software bundle. LAMP refers to the following components:

- Linux, as the operating system
- Apache, as the Web server
- MySQL, as the database server
- P, as one of the programming or scripting languages, PHP, Perl, or Python

Linux was designed using many of the design principles of UNIX that were described in the previous section. The Linux kernel is monolithic and contains process and memory management, drivers and I/O modules, device files, sockets, and the file system. Other functionality, such as the command interpreters (shells), utilities, and graphical user interfaces (GUIs), consists of user space functions. Linux is designed to comply with POSIX standards, and most distributions adopt many of the principles of SUS that you learned about in the previous section. An effort to standardize Linux is under way, known as the Linux Standard Base, which is described in the next section.

A wide variety of GUIs are available for Linux distributions, but most of these are based on the X Window System and the Motif interface guidelines. The most popular GUIs are KDE, GNOME, and Xfce, and many distributions allow you to install more than one GUI if you want. Higher-performance network servers tend to run without a GUI, relying on a Command Line Interface (CLI) and running in what is called "headless" mode — that is, without an attached monitor, keyboard, or mouse. Control of a headless server is performed over the network, often from a terminal session (graphical terminal emulator) or command prompt. Most UNIX distributions support headless mode because it provides a little more overhead for running processes. Microsoft Windows Server added a headless mode in version 2008.

### Linux Standard Base

The Linux Standard Base (LSB) is a project managed by the Linux Foundation (`www.linuxfoundation.org/`) to standardize features of Linux so that different distributions will be more compatible with one another. As with SUS, described previously, LSB has a compliance certification. LSB specifies standard libraries, commands, utilities, file system components, print subsystem features, POSIX, and X Windows System extensions. LSB also specifies the nature of the RPM package format used to install Linux software. The last released version of LSB is version 3.2, released in 2008, that is submitted as ISO/IEC 23360.

## Solaris

Sun Microsystems's Solaris operating system is the most commonly deployed UNIX network operating system in use today. Solaris was introduced in 1992 to replace the SunOS operating system, and to introduce an advanced network stack to support TCP/IP networking. Solaris exists in two versions: a version that runs on Sun's SPARC-based hardware systems and an x86 version that runs on the Intel standard architecture. Solaris has been positioned by Sun as one of the premier network operating systems for large enterprises, and as a preferred platform for storage network management.

The most recent version of Solaris is version 10 (SunOS 5.10). The operating system can be downloaded in either of its two architectures (SPARC x86 or IA64) from its Web site at `http://sun.com/solaris/` and is free for testing and non-commercial uses. The Solaris installation allows for installation on either a server or workstation. You can install core network services alone, user services, developer services, or the entire package containing the complete network management and policy management utilities.

Although the original versions of Solaris were based on a proprietary code base, Sun has been transitioning Solaris to an industry-standard, open source model. The current version of Solaris now has the majority of its code base published as the open source version of Solaris, called OpenSolaris. Sun's commercial version of Solaris is certified as conforming to the Single UNIX Specification described in the previous section.

The original network stack for Solaris 1.x was based on a version of BSD. To improve Solaris' performance, Sun migrated the network stack in Solaris 2.x to the AT&T SVR4 architecture. Various versions of 2.x continued the transition toward the STREAMS network stack that has become the basis for networking functionality in UNIX System V. STREAMS is noted for both its modular nature and its message-passing capabilities between those modules. When you create a connection in the STREAMS architecture, there is a significant overhead, but for the long session times associated with protocols such as FTP or NFS, this overhead was not a problem.

However, as Sun moved its hardware base to more powerful multiprocessor systems, the fact that STREAM cannot easily be optimized for multiprocessor processing became a major issue. As packets are processed in a STREAM architecture, multithreading with more than one processor results in considerable context switching (kernel/user mode flips) that cannot be programmed away. By the late 1990s, Sun servers and workstations became a favorite platform both for routing and as application servers running Web server software. Internet protocols, particularly HTTP, are short-lived connections where the STREAM architecture is at a distinct disadvantage. Sun set about re-architecting its network stack with its development of Solaris 10.

### Note

Solaris 2.0 to 2.6 corresponds to the SunOS version 5.0 to 5.6. Sun started numbering Solaris as whole integers starting with Solaris 7 (SunOS 5.7), with the latest version being Solaris 10 (SunOS 5.10), originally released on January 31, 2005. Solaris is the successor to the SunOS, but Sun has maintained the numbering scheme for both names.

The Solaris 10 operating system's network stack was rebuilt using what was called the "FireEngine" architecture, which merged all of the protocol layers into a single STREAM module with full multithreading. This approach allows for a CPU synchronization that in turn allows for serial network queue abstractions ("squeue") and binds the squeue to a single processor. Solaris 10 replaces a message-passing architecture with one that uses a BSD function call-type interface.

Solaris 10 supports the NFS 4.0 file system and is architected to support network throughputs of up to 10 Gbits/s. Using a feature called Solaris Zones, multiple instances of the operating system can be run on the same hardware as virtual machines. Using the Grid Container technology, a Sun server can create a disk partition for individual users that gives those users the appearance that they are running their own operating system, essentially turning a Sun server into a terminal server.

Solaris can also attach to the ZFS (originally codenamed the Zettabyte File System), which has some unique enterprise features. ZFS supports very large volume sizes, comes with high storage capacities, and integrates both file system and volume management. In addition to built-in snapshots and cloning, ZFS introduced a data replication scheme called RAID-Z, with the entire technology taken as a whole having some very unique self-healing capabilities. Sun released ZFS into the public domain as open source software as part of the OpenSolaris project (`www.opensolaris.org/os/community/zfs/`).

Solaris ships with a utility called DTrace (Dynamic Tracing), which diagnoses network application performance and determines where existing bottlenecks are occurring. This information can be fed to the fault manager for remediation and optimization and/or reported to system administrators who can then run scripts on their servers to correct the network or system behavior. DTrace was the first of the OpenSolaris components to be open sourced as part of the OpenSolaris project. OpenSolaris (`http://opensolaris.com/`) is an open source version of the Solaris operating system.

## Novell NetWare and Open Enterprise Server

Novell's NetWare has had an important position in the area of NOS development. For nearly a decade, NetWare was the preeminent NOS for PCs, and particularly for file and print services and heterogeneous networks containing many different types of clients. As Microsoft Windows Server and particularly Linux servers became more popular, NetWare as an NOS platform became less popular. Novell focused its development on network management tools such as ZenWorks, enterprise-class directory services such as eDirectory, and other products that continue to represent the state of the art in these various fields.

As a consequence of these market factors, Novell still retains leadership in these areas, but after continuing to develop NetWare through version 6.5 (first released in August 2003), the company has moved both its desktop and server offerings to Linux distributions. Netware 6.5 was superseded by the Open Enterprise Server (OES), which, at version 2 SP1, has the identical NetWare kernel. OES 1 appeared in March 2005, and OES 2 was released in October 2007.

OES is a 64-bit NOS that can be run as a virtual machine inside a Xen hypervisor atop the SUSE Linux Enterprise Server (SLES) 10. Both Xen and SUSE were Novell acquisitions. SUSE Linux is also available as openSUSE, now at version 11.1 (`www.opensuse.org`) for users, and SUSE Linux Enterprise, an open source server version. SUSE Linux Enterprise Desktop (`www.novell.com/products/desktop/`) is Novell's commercial desktop client for OES.

OES 2 is an NOS that can run on top of either a NetWare or Linux kernel. Novell has OES positioned as an enterprise solution for file, print, directory, and Web applications. When run atop the NetWare kernel, the product is referred to as OES-NetWare and can add NetWare Loadable Modules (NLMs) to add a variety of applications, most prominently Apache, eDirectory, GroupWise, iPrint, NSS, OpenSSH, Tomcat, and others. An NLM is an execution module or add-in that extends the NetWare kernel.

## Windows Server

Windows Server is noted as the general-purpose server that has the strongest and broadest network application support of all of the NOS that have been discussed. Microsoft's unique advantage is that Windows controls nearly 90 percent of the worldwide desktop computer market, which makes a number of valuable features such as automated deployments, a strong NOS policy engine, and other features possible.

Microsoft also sells an extensive set of server applications under the banner of Microsoft Servers. Examples of Microsoft Server products include Biz Talk Server, Commerce Server, Exchange Server, Internet Information Server (bundled with Windows Server), ISA Server, SQL Server, Windows Storage Server (as a separate Windows edition), and others. The various versions of Windows Server itself range from Windows Home Server to Windows Small Business Server all the way up to Windows Datacenter Edition. Of all of the applications on the previous list, Microsoft Exchange has achieved a dominant position in the enterprise mail market, and SQL Server is the best-selling commercial enterprise-class database server.

Microsoft's server technology began first as a codevelopment project with IBM of the OS/2 operating system. Microsoft abandoned OS/2 and initiated the Windows NT project led by David Cutler, with the first 32-bit commercial version appearing in July 1993, and was numbered as version 3.1 to bring it into harmony with Microsoft's current desktop client. Subsequent versions of the server OS have been branded Windows Server 2000, Windows Server 2003, and Windows Server 2008.

The original design goal of NT was to create an operating system that was highly portable and could run on many different processor types. The NT hybrid kernel was isolated from machine architecture by a Hardware Abstraction Layer (HAL), and the kernel mode is separated from the user mode. Of the original architectures that included x86 (IA32), PowerPC, MIPS R3000/4000, DEC Alpha, and IA64 (Itanium and AMD64), only the x86 and IA64 versions survive. The user mode supports a number of different system APIs, including Win32, OS/2, and POSIX. The original network stack was based on the OS/2 LAN Manager, which would eventually be redesigned based on BSD UNIX. The NTFS file system is native to Windows Server and has been continually developed throughout the lifetime of the operating system. Microsoft Windows is known for very strong driver support through the Windows Driver Foundation (also known as Model), for industry-leading device support in terms of breadth, and for strong adherence to the practice of making their operating system software as backwards-compatible as possible.

Each new version of the Windows Server operating system tends to introduce a small number of major new NOS subsystems, and a long list of new features. Windows Server 2000 was notable for the introduction of the Active Directory, which was refined with Windows Server 2003. Windows Server 2003 had major improvements in the policy engine, in reliability, and in system management. Windows Server 2008 is noted for its support for a number of Web-based technologies that support distributed applications based on the .NET Framework, for new graphics routines, and for its Hyper-V virtualization technologies.

Windows Server 2008 also saw a complete redesign of the Windows TCP/IP network stack, the architecture of which is shown in [Figure 20.4](ch20.html#the_next-generation_tcp_solidus_ip_netwo). NDIS is shown at the bottom and is the Windows device driver layer.

Microsoft's latest versions at the time of printing were Windows Server 2008 R2 and Vista R2 client. Windows 7, expected to be released in late 2009 or early 2010, is an optimized version of VistaWindows Server and runs on the x86 and IA64 (Itanium) systems.

![The next-generation TCP/IP network stack that was introduced in Windows Server 2008/Vista](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2004.png)

**Figure 20.4. The next-generation TCP/IP network stack that was introduced in Windows Server 2008/Vista**

# Summary

A network operating system, or NOS, provides network services to clients. It is important to understand NOS in order to understand how computer networking developed.

Every NOS must support the hardware it runs on, run protocols and services, and provide those services or applications for client systems. An NOS may offer a number of other services as well. When an NOS has broad capabilities, it is called a *platform*. UNIX, Linux, Solaris, NetWare, and Microsoft Windows Server are some of the platform NOSs that you learned about in this chapter.

In the next chapter, you learn about one of the essential NOS services, directory services. A directory service stores information about network objects for use in a variety of contexts.
