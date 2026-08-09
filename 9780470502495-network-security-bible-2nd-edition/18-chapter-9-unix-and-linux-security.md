# Chapter 9. UNIX and Linux Security

**IN THIS CHAPTER**

- **Focusing on UNIX/Linux security**
- **Understanding physical security**
- **Controlling the configuration**
- **Operating UNIX safely**
- **Hardening UNIX**

UNIX, Linux, and other similar operating systems are gaining in popularity and market share. UNIX is still a dominant player in the server arena. Most of the growth in UNIX popularity has been in the workstation arena.

Most of the security issues raised in [Chapter 8](ch08.html) apply to operating a UNIX workstation safely. However, some of UNIX's unique aspects are covered in this chapter.

# The Focus of UNIX/Linux Security

UNIX, Linux, FreeBsd, AIX, and so on (all referred to as UNIX in this chapter) have great potential for both being very secure and being exploited. Some of the same features that make UNIX a good target for security attalks make it powerful enough to be operated safely.

## UNIX as a target

There is an ongoing debate among system administrators as to whether Windows or UNIX is the more vulnerable operating system. This debate often degrades to a mere count of vulnerabilities applicable to one side or the other. The bottom line is that both systems are susceptible to attacks and need to be properly secured. In any case, it is useful to start with an examination of why UNIX and Linux might be a target of security attacks. The following lists the four main reasons that UNIX is a target:

- Linux (and much of the other UNIX implementations) are open source.
- UNIX installations are easy to obtain, both in terms of being inexpensive (often free) and readily distributed.
- Most hacking tools are available for UNIX.
- UNIX is a good environment to exchange hacks and code.

### Open source

Open source means products made available along with the source code needed to rebuild or recompile the products. Open source does not mean free of cost or licenses, although it is in many cases.

Many people view open source as a major security threat. In fact, this has not turned out to be the case. While it is true that a hacker can get a head start on finding security issues by examining the code, this concern is certainly overrated because of the extremely long hours that would be required to walk through the thousands of lines of code. However, once a flaw is identified, the source code can be very useful to the hacker in developing an exploit. But remember that the security professional also has access to the source code and has the ability to find similar vulnerabilities.

Ironically, over time, the ultimate effect of having code open to all may be that the code is better and more secure. Problems tend to be quickly fixed and thoroughly vetted. This is discussed in more detail in the section "[Open source issues](ch09.html#open_source_issues)" later in this chapter.

### Easy-to-obtain operating system

That Linux is low cost and freely distributed on the Internet makes it a popular operating system for experimentation. Many public forums exist in which novices can get help and support for their Linux implementation. Even solutions for complicated and obscure problems can be found with a minimal amount of searching on the Internet. If it is a popular operating system to use, it can be expected to be popular for hacking as well.

### Network and development tools

Another attractive feature of UNIX and Linux for the hacker is the abundance of network tools available. Most networking tools are developed under Linux or FreeBSD first and later ported to other operating systems. Certainly the open source software and the plethora of code examples contributed to the early development of tools on UNIX.

Some examples of the free network tools that support hackers in their quest for vulnerabilities and exploits include the following:

- **tcpdump** — A low-level traffic capture application that sniffs traffic at the International Standards Organization (OSI) model's layers 2, 3, and 4; tcpdump comes standard on most UNIX installations and supports a wide variety of layer 2 media. Because tcpdump is so universally available, its output is often used as input into traffic analysis tools.
- **WireShark** — A network traffic–sniffing application. WireShark also provides a nice interface to work with traffic captured with other low-level tools such as tcpdump.
- **tcpreplay** — This allows for traffic captured in tcpdump to be put back on the wire. This permits the hackers to better analyze traffic and ultimately to debug their own applications.
- **nmap** — A popular port-scanning tool. It will check the status of ports on a system from the network by attempting to connect to the ports. The method of connection can be varied; likewise, nmap can run more or less aggressively through the hosts and ports.
- **Nessus** — A vulnerability scanner that calls nmap to discover open ports, then tests the ports for possible vulnerabilities. Nessus has over 500 tests and can detect most older vulnerabilities.
- **Perl, sh, and ksh** — Scripting languages that, in the hands of the hacker, become a powerful tool for automating procedures.

In addition to network tools, UNIX systems come with a fully functional development environment. All the compilers and libraries needed to completely rebuild the kernel and operating system are available as open source resources. With these development tools, the hacker can produce everything from kernel module root kits to sophisticated attack tools of their own.

### Information Exchange

UNIX is an attractive platform for the exchange of tools and techniques under development by hackers. Hackers are able to exchange source code and then readily recompile the applications. The hacker community has a lot of expertise in UNIX and this expertise is shared in the form of code and advice.

## UNIX/Linux as a poor target

UNIX has some characteristics that make it a less attractive target for security attacks. Some of these characteristics are as follows:

- There are many versions and builds.
- Users are generally more expert.
- Scripts are not as easily run (compared with Outlook).
- File ownership limits malware spread.

### Many versions and builds

While code and hacks are easily exchanged, specific exploits may not work on a majority of UNIX platforms. For example, a kernel root kit initially developed for Linux 2.4.20-8 on Red Hat may have to be tested and adapted to be useful on other systems, such as Debian. This requires a level of discipline and configuration management that is not normally a trait of the typical troublemaking hacker. As a result, there may be many exploits developed for UNIX, but few of them are universally dangerous.

### Expert users

UNIX has not made great inroads as a popular desktop workstation for the masses. It is still primarily used on servers, embedded systems, and software development platforms. All of these uses tend to make the average UNIX user more knowledgeable about the operating system and security. Therefore, if the technical expertise of the average user is greater, attacks against their platforms will, on the whole, be less frequent and harder to accomplish.

Attackers, like most forces, will seek the path of least resistance. Attacking a workstation that is managed by a non-technical person will certainly be easier than attacking one managed by an expert.

### Scripts not as easily run

There are many scripting techniques in UNIX. They range from Perl to the Bourne shell. However, unlike Windows, the scripting is not tightly integrated into common applications (such as Outlook and Word). In UNIX, scripts can be integrated into applications such as mail and word processing, but this is not the default configuration. This makes UNIX much less vulnerable than a Windows system that is running Outlook and commonly allows users to run powerful Visual Basic scripts.

### File ownership

It is not uncommon for malware to take advantage of commonly run executables to propagate an attack. In these cases, the malware writes itself to a file that is later executed by the unaware user. This kind of attack is made possible because to perform normal computing functions, restricted users are permitted to run executables that have root or administrator-level access to system resources. This is true for UNIX as well.

Where UNIX has an advantage is in that the file ownership is different than file execution permission. Although users may be able to run a critical application, they usually do not own the application and therefore would not normally be able to write or alter the executable. The inability of a common user to alter an executable is a severe restriction on viruses and worms that depend on users to propagate their malware.

## Open source issues

The first thing that comes to mind when considering the security issues pertaining to open source is that anyone can see the code. This means that hackers looking to cause trouble can spend countless hours analyzing your code to find logical errors, as in the following situations:

- Hackers will look for embedded passwords or back doors. The software developer may hard code a password authentication into the application as a convenience feature to the end user. This is clearly a poor practice because the passwords are easily detected and acquired. Attackers can then use the passwords to gain access to the resources outside of the constraints of the application.
- Hackers may identify places in the code where input is not properly checked. Most programmers have tunnel vision when writing code; they assume they will receive the proper input from the end user (or from another function). For code to be truly secure, programmers must assume that they will receive completely irrelevant input from the user. The programmer must really think outside the box about validating input. For example, special characters and Unicode should be considered. Simple checks on the input data may not detect data put in following a \0 (NULL terminator). If hackers find locations where the input is not properly checked, they will attempt to exploit this by entering strange data. The result may be that the application reacts in a totally unpredicted manner, giving hackers a means to exploit the application.
- Hackers will examine the open source code for variables that are set but not properly checked. Programmers should check that their variables do not go out of range, meaning that only valid values are assigned to the variables. If a variable goes out of range, it may clobber memory or have other unintended consequences. If hackers can manipulate the application in such a way as to cause variables to go out of range, the application's behavior may be unpredictable. Under these circumstances, the application may exhibit a vulnerability that can be exploited.
- Hackers will look for instances in the open source code in which the user's input is used as code or instructions. A common example of this might be when an end user is allowed to build a SQL query. The query might then be passed to a function that executes the query. This is a dangerous practice. Merely checking the input for proper format will not suffice in this case. The end user's input should not be processed directly; rather an interpreter should be written to read the input and rebuild the SQL necessary to run the queries. This interpreter must be very restrictive in the calls it will use and make.

Having found potentially vulnerable points in the code, hackers can attempt to exploit the vulnerabilities. This is still not a simple process, but hackers are well ahead of the game just by knowing where to concentrate their efforts.

In addition to exposing the open source code to the hacker community, the code is also scrutinized by the user community. The user community does not spend time reading source code for logical (security) flaws. The user community will only identify logic errors that are encountered during an examination of the code for some other reason, the most common reasons being that the code is faulty (does not work for that user), or the user wants to extend or improve the code to cover his or her particular circumstances.

While not as good as employing an army of "white hat" hackers (persons who test applications to find flaws to better the product, not exploit it) to scrutinize the code, software developers have hundreds of extra eyes going over their code when they make it open source. Because most people are honorable and reputable, this appears to be a net gain for software developers, from a security perspective.

When logic problems are found and brought to the attention of the user community, in open source software, they tend to be corrected quickly due to the following:

- Software developers can't pretend that the flaws don't exist because they are there for the whole world to see.
- The user community will often contribute to making the fix.

Open source has an added benefit of allowing security to influence the evolution of software products. For the reasons stated earlier, the development of software in an open source manner may contribute to the improvement of software available for a given need. Most user requirements have a number of applications that could satisfy the need. Except in the case of a monopoly, the user community will eventually decide which of the applications survive and become popular. When open source is subjected to this selection process, it can be assumed that the security (lack of logic errors) of the code will be a factor when the user community chooses its favorite applications. All things being equal, users will choose a secure application over a risky one.

# Physical Security

The first (or last, depending on your perspective) line of defense against a security threat is physical security. Some measures can be taken to improve the security of a UNIX workstation in the event that an attacker gains physical access to the device. The following UNIX-specific methods to improve the physical security of a workstation are discussed here:

- Limit access to the UNIX workstation during boot operations.
- Detect hardware changes to understand any physical changes to the system.
- Disk portioning can lessen the impact of damage from a security problem.
- Prepare for the inevitable security attack.

## Limiting access

It is a general principle that any network device (such as a UNIX workstation) can be compromised if an attacker has physical access to the device. The type of compromise varies depending on the network device. For a UNIX workstation, the following are some possible means to achieve this compromise:

- **Reboot** — If the workstation can be rebooted with a USB or CD, an attacker can boot an operating system of the attacker's choice, and in this way can have full access to all the workstation's resources.
- **Data collection** — If an attacker installs a covert monitoring device, such as a keystroke capturer, sensitive information may then be stored on the monitoring device. The device may either phone home the information to the attacker or the attacker may get physical access to the box a second time and retrieve the device.
- **Theft** — An attacker who can remove a hard drive from the premises will have sufficient time and resources to extract all the information on the drive.
- **BIOS control** — If an attacker is able to reboot the workstation and get into BIOS, the person may set a BIOS password to lock everyone else out of the workstation. This would constitute an effective denial-of-service (DoS) attack.

The following steps will improve the physical security of the UNIX workstation. These measures should be considered part of a defense-in-depth methodology because all these steps together will still not completely secure a workstation that has been physically compromised:

- **Enable the BIOS password**. BIOS changes will be protected from change if this password is set. Also, if the BIOS password is in the disabled state, the attacker can enable it and set a password. This can result in a denial-of-service attack because legitimate users will not be able to boot and use the workstation.
- **Change BIOS settings**. BIOS settings should be changed to prevent booting from a floppy or CD. These are typically infrequent events; therefore the impact will, in most cases, be minimal.
- **Set the boot loader password**. Typically, this involves the Linux Loader (LILO) or Grand Unify Bootloader (GRUB) loaders. If an attacker can modify the boot loader configuration, he or she will be able to access and change resources that were otherwise off limits.

Some versions of Linux can be booted directly into a root account (often referred to as single user mode) using one of the following commands at the boot prompt:

```
linux single
```

or

```
linux init=/bin/sh
```

In the first case, Linux boots using the single user mode. This mode, in UNIX, gives someone root access to all the resources on the host machine without needing to log in with a password. Requiring a password during the boot process will provide additional security. Single-user mode access will require a password if the following line is inserted in the `/etc/inittab` file after the `initdefault` line:

```
~~:S:wait:/sbin/sulogin
```

In the second case, `linux init=/bin/sh`, Linux is booted and runs a Bourne shell instead of the init process. This provides the user with root access. To add a password to the LILO prompt, put the following lines in the `/etc/lilo.conf` file:

```
restricted
password="<root password>"
```

The boot loader password takes effect after rebooting. When prompted, enter the root password. Now when the workstation is rebooted, any additional boot arguments will require the root password.

## Detecting hardware changes

The application kudzu detects and configures new and/or changed hardware on a Linux system. When started, kudzu detects the current hardware and checks it against a database stored in `/etc/sysconfig/hwconf`, if one exists. It then determines if any hardware has been added or removed from the system. If new hardware is found, the user is prompted to configure the hardware. If hardware is expected but not found, the user can remove the configuration. Kudzu then updates the database in `/etc/sysconfig/hwconf`. If no previous database exists, kudzu attempts to determine what devices have already been configured by looking at `/etc/modules.conf`, `/etc/sysconfig/network-scripts/`, and `/etc/X11/XF86Config`.

The following are just a few of the pieces of hardware identified and stored in the hwconf database. The full listing can be obtained with the command `kudzu -p`. Shown in the following listing are a network interface card (NIC), a floppy drive, a CD-ROM drive, and a hard drive. By storing this information and comparing it with current values, any changes in the physical hardware can be found.

```
class: NETWORK
bus: PCI
detached: 0
device: eth
driver: 3c59x
desc: "3Com Corporation|3c905C-TX/TX-M [Tornado]"
vendorId: 10b7
deviceId: 9200
subVendorId: 1028
subDeviceId: 00d5
pciType: 1

class: FLOPPY
bus: MISC
detached: 0
device: fd0
driver: unknown
desc: "3.5" 1.44MB floppy drive"

class: CDROM
bus: SCSI
detached: 0
device: scd0
driver: ignore
desc: "Matshita CDRW/DVD UJDA740"
host: 0
id: 0
channel: 0
lun: 0
generic: sg0
```

```
class: HD
bus: IDE
detached: 0
device: hda
driver: ignore
desc: "FUJITSU MHT2060AT"
physical: 116280/16/63
logical: 7296/255/63
```

## Disk partitioning

Partitioning of disks on a UNIX platform can be a physical security issue. Older UNIX versions had a serious problem with the loss of a partition due to a physical error. For example, a sudden power loss may cause a mismatch between the file pointers (inodes) stored in memory and those already written to disk. Such a mismatch could cause the loss of some data on the partition. This risk is greatly mitigated with the new versions of the UNIX file systems. These file systems, such as ext3 in Linux, use *journaling* to make the recovery of damaged file systems more reliable. Journaling provides for a fast file system restart in the event of a system crash. By using database techniques, journaling can restore a file system in a matter of minutes, or even seconds, versus hours or days with non-journaled file systems. In addition to ext3, jfs, xfs, and reiserfs are also journaling file systems.

Even with journaling, data in a file system (partition) can be lost due to disk damage. One measure that can be taken to reduce this risk is to spread files (based on their use) across different partitions. One partition should contain non-changing operating system files. This is usually the `/usr` directory. If this partition is lost due to some physical problem, the partition can readily be restored either from backup, or by re-installing the operating system. Because this partition will rarely change, incremental backups can be done quickly.

The directory `/usr/local` is one place under `/usr` where applications may install themselves. Even though this appears to be on the `/usr` partition, it can be mounted as a separate partition during the boot process. The most common way to do this is in the `/etc/fstab` with a line such as the following:

```
/dev/hda6      /usr/local         ext3    defaults       1 2
```

It is advisable to put the `/home` directory on a separate partition. This partition holds the home directories of the users who can log in to the workstation. In many cases, these directories will hold configuration information for the individual users.

There should also be one or more partitions that hold the data that will be used by the organization or the particular workstation (referred to here as the `/data` directory). The advantage to having the data in a separate partition is that it can be backed up and restored separately. Also, when the UNIX operating system is upgraded, the `/data` directory can be brought forward without the need to copy it off and then back onto the workstation.

Consider directories that could grow very large and, as a result, cause a denial of service for the whole workstation. Typically, these are the `/tmp` and `/var` directories. These should each be put on a separate partition. If the `/tmp` or `/var` partition fills up, performance and operations may be impacted or impaired, but recovery will be simple. If, instead, the */* directory is filled up (because `/tmp` was on the same partition) the operating system might hang and not be able to reboot without special procedures.

## Prepare for the eventual attack

You can take certain steps to prepare a UNIX workstation for the inevitable attack. From a security perspective, these steps are usually put under the category of incident response or disaster recovery.

Preparing for an attack is a three-part process — backup, inventory, and detection.

- The frequency and extent of the backups (copying data and files and moving them off the workstation) should be determined by the risk of losing the files or data. The more frequently the data changes and the more critical would be the loss, the more frequent the backups should be. It is not uncommon in a rapid development environment to see several backups daily. However, other environments, such as a home user environment, might do weekly or monthly backups.
- Backups should be done in a manner consistent with the sensitivity and attention given to the workstation. In most cases, daily backups are recommended. A normal backup cycle is for incremental backups to be done every day and full backups to be done on Friday. How long the backups will be kept or, in the case of reusable media, re-used depends on the sensitivity and attention placed on the workstation. The more sensitive the data, the longer the backups should be kept. In some cases, financial data might be kept for years. If the workstation does not get a lot of monitoring and it is suspected that an attack might not be readily detected, the backups should be kept for a longer period than normal.
- Inventory involves the system administrator knowing the key files on the workstation that must be checked in the event of an attack. From an operating system perspective these include password files `(/etc/passwd`) and startup scripts `(/etc/rc.d/init/*`). However, individual organizations will have other equally critical files that control the mission, such as database files.
- Detection is key to any preparation against an attack. Detection or monitoring allows for the initiation of a timely response. This can be a significant factor in limiting the damage done by the attack.

If any of these three protective measures—backup, inventory, or detection — is missing or weak, the other two may be hindered to the point of not being effective. Consider the following scenarios:

- **Backups without detection** — Without adequate detection, an attacker may be on the workstation for a period of time that spans a number of backups. If the compromise is then detected and the system administrator attempts to restore from backup, they may be restoring compromised files.
- **Inventory and weak detection** — It is important to keep an inventory or status of key files on the workstation to be better prepared to respond to an attack or incident. However, without quick detection of an attack, users and administrators may change some of these files over the course of normal business. If the valid users make changes on top of an attacker's changes, it will be very difficult to determine what was done by the attacker and how to mitigate the risk.
- **Detection without inventory and backups** — If inventories of key files and backups are adequately conducted, prompt detection can lead to a response that will limit the attacker's abilities to continue the attack. However, if inadequate backups were done, the recovery from the attack can be hampered. In such cases, the entire workstation may have to be taken offline and the operating system rebuilt from scratch.

The bottom line in responding to an attack or a compromised system is if you can't be 100 percent assured that you have found and corrected everything that an attacker has done, you should take the workstation offline, rebuild the operating system, and reharden the workstation, hopefully, taking the opportunity to establish good backups, inventories, and detection capabilities.

# Controlling the Configuration

Controlling the configuration of a UNIX workstation is important for network security. Even stripped down and hardened, a UNIX workstation can be a powerful tool from which to launch attacks on the network or on other hosts. The configuration concerns will be addressed in two areas:

- **Installed packages or applications** — Eliminating unneeded applications and keeping required ones properly patched is key to a defense-in-depth strategy.
- **Kernel-related issues** — Because the kernel has root-level control over resources and processes, it is a critical part of the UNIX system to keep under configuration control.

## Installed packages

It is important for an administrator to know what packages are installed. The "Operating Safely" section later in this chapter discusses how to control which applications are running. Even if an application is not running or is not planned to run, its installation should still be limited or controlled. Attackers may seek to take over a workstation to use its resources. By stripping the available software packages down to a minimum, the workstation becomes a less valuable target to the attacker. Additionally, if the workstation is overtaken, the usefulness of it to the attacker is reduced.

Following are some typical packages that should not be installed unless they have a legitimate use:

- **Mail server** — Sendmail (or an equivalent application) is commonly installed on UNIX systems. While the mail server may not be used by the average UNIX user, it is a useful tool to an attacker who has taken over control of the workstation.
- **Automatic update servers**—If automatic update services are not being used, these services should not be installed. For example, on Red Hat systems, rhnsd is a daemon process that runs in the background and periodically polls the Red Hat Network to see if there are any queued actions available. If any actions are queued, they are run and the system is automatically updated.
- **File-sharing services** — On UNIX systems, smbd is a server daemon that provides file sharing and printing services to Windows clients. The server provides filespace and printer services to clients using the Server Message Block (SMB) or Common Internet File System (CIFS) protocol. This is compatible with the LANManager protocol, and can service LANManager clients.
- **File transfer services** — The File Transfer Protocol (FTP) service is a program that allows a user to transfer files to and from a remote network site. Attackers have been known to activate FTP capabilities to use systems for their personal file transfer.

On Linux, the command `rpm -qai` will list all installed rpm packages. This produces information on each package. Following is the information available for a typical sendmail package:

```
Name        : sendmail                   Relocations: (not relocatable)
Version     : 8.12.8                     Vendor: Red Hat, Inc.
Release     : 4                          Build Date: Mon 24 Feb 2009
07:16:00 PM EST
Install Date: Wed 15 Oct 2003 09:36:17 PM EDT  Build Host:
stripples.devel.redhat.com
Group       : System Environment/Daemons    Source RPM: sendmail-8.12.8-
4.src.rpm
Size        : 4389045                          License: BSD
Signature   : DSA/SHA1, Mon 24 Feb 2003 11:30:42 PM EST, Key ID
219180cddb42a60e
Packager    : Red Hat, Inc. <http://bugzilla.redhat.com/bugzilla>
Summary     : A widely used Mail Transport Agent (MTA).
Description :
The sendmail program is a very widely used Mail Transport Agent (MTA).
MTAs send mail from one machine to another. Sendmail is not a client
program, which you use to read your e-mail. Sendmail is a behind-the-scenes
program which actually moves your e-mail over networks or the Internet to
where you want it to go. If you ever need to reconfigure sendmail, you
will also need to have the sendmail.cf package installed. If you need
documentation on sendmail, you can install the sendmail-doc package.
```

## Kernel configurations

The kernel is a relatively small program that controls the most critical resources on the system, such as the hard drives, memory, and video card. The kernel allows for many applications to run simultaneously by controlling their access to critical resources. Applications access these resources through system calls.

Most of the kernel code consists of device drivers — over 90 percent of which are probably not needed by any one particular workstation. Usually, the installation of UNIX or Linux does not include a compilation of the kernel. As a result, the kernel must be prepared to support a wide variety of architectures and hardware configurations. This leads to a lot of code that is not used. As a general security principle, there is no advantage to keeping unused kernel code around. Note that most of this unused code is not compiled directly into the kernel but is available to be loaded as a module when needed. Kernel modules are discussed later in this chapter in the "Kernel modules" section.

UNIX has two modes: supervisor mode and user mode. In user mode, library functions are used. These functions then make system calls, which execute on behalf of the libraries. Because the system calls are part of the kernel itself, they have privileged access to critical system resources. Once the task (system call) is completed, control is returned to user mode.

### Kernel options

A typical kernel has many options, perhaps as many as 1,300 or more in the Linux 2.4 kernel. Some of the more significant security-related options are as follows:

- **iptables** — Iptables is a powerful firewall that can be used on UNIX workstations. Because iptables operates at the kernel level, it must be compiled into the kernel.
- **IP forwarding** — With forwarding turned on, the workstation can function as a gateway or router. Traffic sent to the workstation but destined for a different IP will be routed according to the workstation's route table. This can be a security risk. Certain network safeguards may be circumvented because the traffic will appear to come from the workstation instead of the originator. Additionally, if the workstation is multihomed (two or more NICs on different subnets), the workstation may allow traffic onto a different network. This may circumvent security controls for that network, such as a firewall or proxy. If not disabled in the kernel, IP forwarding can also be disabled after a system has booted. In Linux, the file `/proc/sys/net/ipv4/ip_forward` should contain 0 to disable forwarding.
- **Support for multiprocessors** — If multiple processors are detected on your workstation, the installation process may configure your boot loader to load a multiprocessor version of the kernel. In most cases, this will not make a difference in the security of the workstation. However, if the workstation is doing development and testing of kernel modules and system calls, the multiprocessor kernel might introduce unwanted effects.
- **Source-routed frames** — The kernel can be configured to drop source-routed frames. A source-routed frame is a packet that contains all the information needed for the packet to traverse the network and reach its destination. This source routing is not normally needed and is most often used as a small part of a larger attack. By configuring the kernel to drop source-routed frames, an added measure of security is gained.

The typical UNIX kernel comes with many features enabled that are not required. By rebuilding the kernel and eliminating these options, you will increase the overall security of the workstation. Any unneeded code is a potential source of vulnerability. Additionally, if the workstation is compromised, these unneeded features may be useful to the attacker. Following is a short list of some options that have been turned on. You can see from this small sample that a wide variety of configuration items are possible.

```
CONFIG_SCSI_CONSTANTS=y
CONFIG_AIC7XXX_TCQ_ON_BY_DEFAULT=y
CONFIG_AIC7XXX_OLD_TCQ_ON_BY_DEFAULT=y
CONFIG_AIC79XX_ENABLE_RD_STRM=y
CONFIG_SCSI_EATA_TAGGED_QUEUE=y
CONFIG_SCSI_G_NCR5380_PORT=y
CONFIG_SCSI_NCR53C7xx_FAST=y
CONFIG_SCSI_NCR53C7xx_DISCONNECT=y
CONFIG_SCSI_PCMCIA=y
CONFIG_IEEE1394_PCILYNX_PORTS=y
CONFIG_IEEE1394_SBP2_PHYS_DMA=y
CONFIG_NETDEVICES=y
CONFIG_APPLETALK=y
CONFIG_DEV_APPLETALK=y
CONFIG_COPS_DAYNA=y
CONFIG_COPS_TANGENT=y
CONFIG_IPDDP_ENCAP=y
CONFIG_IPDDP_DECAP=y
CONFIG_NET_ETHERNET=y
CONFIG_NET_VENDOR_3COM=y
```

### Kernel Modules

Kernel modules are dynamic extensions to the kernel that can be added without requiring a kernel rebuild or even a reboot. Kernel modules allow for the following:

- **The dynamic extension of kernel capabilities after the detection of new hardware** — When a Personal Computer Memory Card International Association (PCMCIA) card is inserted into a UNIX laptop, the operating system can load the appropriate kernel modules. Adding a Universal Serial Bus (USB) device invokes a similar response.
- **The rapid testing and modification of kernel capabilities under development** — The system call developer does not have to go through time-consuming rebuilds and reboots just to test a new version.
- **The size of the kernel loaded at boot time can be kept smaller** — Many capabilities are designated as loadable modules, so the boot time size of the kernel is kept small and manageable.

A UNIX administrator must know how to check for root kits that have been loaded as a kernel module. The `lsmod` command will list kernel modules that have been loaded. The following is a subset of typical modules loaded in a Linux 2.4 kernel:

```
Module                  Size  Used by    Tainted: PF
i810_audio             27720   1  (autoclean)
ac97_codec             13640   0  (autoclean) [i810_audio]
soundcore               6404   2  (autoclean) [i810_audio]
```

```
agpgart                47776   3  (autoclean)
nvidia               2126120   6  (autoclean)
parport_pc             19076   1  (autoclean)
lp                      8996   0  (autoclean)
parport                37056   1  (autoclean) [parport_pc
lp]
ipt_state               1048   3  (autoclean)
iptable_nat            21720   0  (autoclean) (unused)
ip_conntrack           26976   2  (autoclean) [ipt_state
iptable_nat]
iptable_filter          2412   1  (autoclean)
ip_tables              15096   5  [ipt_state iptable_nat
iptable_filter]
sg                     36524   0  (autoclean)
sr_mod                 18136   0  (autoclean)
ide-scsi               12208   0
scsi_mod              107160   3  [sg sr_mod ide-scsi]
ide-cd                 35708   0
cdrom                  33728   0  [sr_mod ide-cd]
keybdev                 2944   0  (unused)
mousedev                5492   1
hid                    22148   0  (unused)
input                   5856   0  [keybdev mousedev hid]
usb-uhci               26348   0  (unused)
usbcore                78784   1  [hid usb-uhci]
ext3                   70784   7
jbd                    51892   7  [ext3]
```

### System calls

A system call is a request to the operating system kernel for access to critical resources. System calls are accomplished using special instructions that allow a switch to the supervisor mode. These calls are the services provided by the kernel to application programs. In other words, a system call is a routine that performs a system-level function on behalf of a process. All system operations are allocated, initiated, monitored, manipulated, and terminated through system calls.

System calls can assist an administrator in evaluating an application's security. By examining calls that an application makes to the kernel, an administrator can determine if a security risk is involved. By viewing the system calls made by a process, it can be determined if the hard drive is being accessed when it should not be. Also, the system calls will reveal network access in a process that has no business on the network.

On a Linux system, the `strace` command is a system call tracer tool that prints out a trace of all the system calls made by a process or application. The `ltrace` command will similarly print out all library calls made. On FreeBSD you can use `ktrace`, and on Solaris `truss`.

The following example is a session that shows the use of `strace` on a simple Hello World program. First the program source is listed:

```
# cat helloworld.c
/*
```

```
* helloworld - simple hello world program
 */

#include <stdio.h>
int main(int argc, char **argv) {
        printf("Hello World\n");
}
```

Now the program is executed normally:

```
# ./a.out
Hello World
```

Finally, the program is executed with `strace`:

```
# strace ./a.out
execve("./a.out", ["./a.out"], [/* 35 vars */])=0
uname({sys="Linux", node="localhost.localdomain", ...})=0
brk(0)                                =0x8049510
old_mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, −1,
0)=0x40016000
open("/etc/ld.so.preload", O_RDONLY)  =−1 ENOENT (No such file or
directory)
open("/etc/ld.so.cache", O_RDONLY)    =3
fstat64(3, {st_mode=S_IFREG|0644, st_size=81158, ...})=0
old_mmap(NULL, 81158, PROT_READ, MAP_PRIVATE, 3, 0)=0x40017000
close(3)                              =0
open("/lib/tls/libc.so.6", O_RDONLY)  =3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0'V\1B4\0"..., 512)
= 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1531064, ...})=0
old_mmap(0x42000000, 1257224, PROT_READ|PROT_EXEC, MAP_PRIVATE, 3, 0)=
0x42000000
old_mmap(0x4212e000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED,
3, 0x12e000)=0x4212e000
old_mmap(0x42131000, 7944, PROT_READ|PROT_WRITE,
MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, −1, 0)=0x42131000
close(3)                              =0
set_thread_area({entry_number:−1 -> 6, base_addr:0x400169e0,
limit:1048575, seg_32bit:1, contents:0, read_exec_only:0,
limit_in_pages:1, seg_not_present:0, useable:1})=0
munmap(0x40017000, 81158)             =0
fstat64(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(136, 3), ...})=0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, −1, 0)
= 0x40017000
write(1, "Hello World\n", 12Hello World)         =12
munmap(0x40017000, 4096)              =0
exit_group(12)                        =?
```

When `strace` is run on a program that accesses the network, you see certain calls that belie that access:

```
# strace ping -c 1 192.168.131.131
execve("/bin/ping", ["ping", "-c", "1", "192.168.131.131"], [/* 35 vars
*/])=0
    <lines deleted>
socket(PF_INET, SOCK_RAW, IPPROTO_ICMP)=3
getuid32()                             =0
setuid32(0)                            =0
socket(PF_INET, SOCK_DGRAM, IPPROTO_IP)=4
connect(4, {sa_family=AF_INET, sin_port=htons(1025),
sin_addr=inet_addr("192.168.131.131")}, 16)=0
getsockname(4, {sa_family=AF_INET, sin_port=htons(32796),
sin_addr=inet_addr("192.168.123.10")}, [16])=0
close(4)                                 =0
setsockopt(3, SOL_RAW, ICMP_FILTER,
~(ICMP_ECHOREPLY|ICMP_DEST_UNREACH|ICMP_SOURCE_QUENCH|ICMP_REDIRECT|ICMP_T
IME_EXCEEDED|ICMP_PARAMETERPROB), 4)=0
setsockopt(3, SOL_IP, IP_RECVERR, [1], 4)=0
setsockopt(3, SOL_SOCKET, SO_SNDBUF, [324], 4)=0
setsockopt(3, SOL_SOCKET, SO_RCVBUF, [65536], 4)=0
getsockopt(3, SOL_SOCKET, SO_RCVBUF, [131072], [4])=0
brk(0)                                  = 0x8062c80
brk(0x8063c80)                          = 0x8063c80
brk(0)                                  = 0x8063c80
brk(0x8064000)                          = 0x8064000
fstat64(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(136, 6), ...})=0
    <lines deleted>
exit_group(0)                         =?
```

### /proc File System

The `/proc` directory is a pseudo-file system used as an interface to kernel data structures rather than reading and interpreting kernel memory.

Most of `/proc` is read-only, but some files allow kernel variables to be changed. The kernel variable that determines whether the system can act as a router and forward IP packets is one such example. If IP forwarding is to be turned on, a `1` should be written into the file or variable at `/proc/sys/net/ipv4/ip_forward`. Without IP forwarding enabled, a value of `0` is in this file.

The `/proc` directory contains many parameters and kernel values needed by system calls to maintain a stable environment. The Linux manual pages describe the available pseudo-files. A few that might be of interest to a network security administrator are as follows:

- **Process ID** — There is a numerical subdirectory for each running process. The subdirectory is named by the process ID. Each subdirectory contains pseudo-files and directories. Two pseudo-files in these subdirectories are as follows:**cmdline** — This holds the complete command line for the process, unless the whole process has been swapped out or the process is a zombie. In either of these two cases, there is nothing in this file (a read on this file will return 0 characters). The command line arguments appear in this file as a set of null-separated strings, with a further null byte after the last string.**cwd** — This is a link to the process's current working directory. To determine the current working directory of process 2250, enter the following command:ls -l /proc/2250/cwdThis will produce the following output showing the current working directory of `/root`:lrwxrwxrwx 1 root root 0 Sep 29 22:28 /proc/2250/cwd -> /root/
- **cmdline**—This pseudo-file contains the arguments passed to the Linux kernel at boot time.
- **kcore**—This file represents the system's physical memory and is stored in the Executable Linking Format (ELF) core file format. With this pseudo-file and an unstripped kernel (`/usr/src/linux/vmlinux`) binary, the `gdb` command can be used to examine the current state of any kernel data structures. To see all the data in the kernel, it needs to be compiled with the `-g` option. The total length of the file is the size of physical memory (RAM) plus 4KB.
- **net** — This subdirectory contains various `net` pseudo-files, all of which give the status of some part of the networking layer. These files contain ASCII structures and are, therefore, readable with the `cat` command. However, the standard netstat suite provides much cleaner access to these files.
- **net/arp**—This holds an ASCII readable dump of the kernel Address Resolution Protocol (ARP) table. It will show both dynamically learned and pre-programmed ARP entries.
- **sys**—This directory contains a number of files and subdirectories corresponding to kernel variables. These variables can be read and sometimes modified using the proc file system and the sysctl system call.
- **kernel/ctrl-alt-del**—The `ctrl-alt-del` pseudo-file controls the handling of Ctrl-Alt-Del from the keyboard. When the value in this file is 0, Ctrl-Alt-Del is trapped and sent to the init program to handle a graceful restart. When the value is > 0, Linux's reaction will be an immediate reboot, without even syncing its dirty buffers.
- **domainname, hostname**—The files `domainname` and `hostname` can be used to set the NIS/YP domain name and the hostname of your box in exactly the same way as the commands `domainname` and `hostname`.

# Operating UNIX Safely

UNIX is a powerful operating system with many tools and capabilities. Even a system that has been properly configured and hardened is still a security risk if users and processes are not properly controlled and monitored.

Any network security attack on a workstation ultimately will come down to running code. The code can fall into one of two categories:

- **Malcode/Malware**—This consists of viruses, worms, and Trojan horses. This code is either run by the user or on the user's behalf by some scripting application, such as a Web browser.
- **Host services**—In this case, the attacker comes in from the network and remotely gets a foothold or access to the workstation by exploiting an open port and its associated service. This is discussed further in the next section, "Controlling processes."

The protection against malcode is twofold: Use antivirus protection and don't engage in risky behavior. Avoiding risky behavior includes the following:

- Don't open, launch, download, or execute anything that comes from a questionable source. In other words, "Don't talk to strangers." This needs to be periodically reinforced to every level of an organization. The weakest-link principle definitely applies here.
- Whenever possible, disable scripting capabilities on e-mail clients, word processing, and other office productivity products.

Note that encryption can enhance the security of any workstation. This is discussed briefly in the "Encryption and certificates" section of this chapter.

## Controlling processes

In the early days of UNIX, installations tended to be bare boned, meaning that only the bare essentials were brought into a system during installation. As UNIX and Linux got more popular, installations were made easier and the trend now is to bring in many features. All these unneeded features or applications are potential security risks.

In terms of security, you can group processes or services into three categories, as follows:

- **Avoid if at all possible**. Certain services are either out of date or so inherently insecure that they should be avoided and alternatives found.
- **Use as needed**. A small group of services are probably worth the risk and are generally more helpful.
- **Probably not needed**. Most processes probably fall into this category. Under certain circumstances they have a use but should not be run on most UNIX workstations.

### Services to avoid

For the security of the UNIX workstation and the network, it is important that system administrators be kept abreast of the processes running. Because many applications in UNIX operate in a daemon or server mode, they can be ready targets for attackers to exploit.

It is a security principle that unneeded applications or services should not be running. Here are a few services commonly found on a UNIX workstation that are not normally needed.

- **FTP (vsftpd or wuftpd)**—FTP is a widely available method of transferring files. It has some vulnerabilities if anonymous access is permitted and it sends passwords in the clear (unencrypted). For these reasons, more secure methods of file transfer, such as scp or sFTP, should be used instead.
- **Network File System (NFS)**—Designed for sharing files over a network but not over the Internet. NFS is a remote procedure call (RPC) service using portmap. NFS makes the spreading of malcode such as Trojan horses easier for the attacker.
- **nfslock**—The NFS file locking service. If NFS is not being used, this service should be disabled.
- **RPC**—This protocol has some inherent security problems and should be avoided if not needed. Few applications these days use RPC. Most users could operate their workstations for years and never need to use RPC. Therefore, it is advisable to turn off RPC services unless otherwise needed. Most implementations of RPC deal with homegrown remote control of the computer or distributed processing. Both of these circumstances are rare.
- **portmap**—This service uses RPC to support nfslock.
- **r commands (rsh, rcp, rlogin)**—These protocols have weak authentication and pass information in the clear (unencrypted). There are a number of better replacements, such as SSH and scp.
- **telnet**—This very simple service allows remote access to a UNIX workstation. Information is passed in the clear, so a third party could easily capture passwords and other sensitive information. Telnet sessions can easily be hijacked and taken over or redirected.

### Useful Services

The following services should be used if needed. In some cases, they can be made more secure by blocking their ports from the network.

- **iptables**—This is a kernel resident packet filter that works off rules controlling packets on input, output, and when they are forwarded through the workstation's network interfaces. Iptables adds another layer of security and is an important defense-in-depth addition to the UNIX workstation.
- **keytable**—This script loads a keyboard map and system font during the boot.
- **kudzu**—This is a hardware-detection program that runs during the boot. It is useful if your workstation frequently has hardware changes, such as a laptop that changes docking stations frequently. If the workstation is stable and does not change, this service can be disabled.
- **network**—This script starts the network interfaces and is required if the workstation is connecting to the network.
- **pcmcia**—This is the script that inserts pcmcia kernel modules for PCMCIA cards on laptops. Even though laptops probably constitute only a small percent of installed UNIX workstations, this service is often on by default. If not applicable to the workstation's hardware, it should be disabled.
- **Print daemons (cupsd, lpd)**—These processes allow the UNIX workstation to print to network printers. While useful for that purpose, these services should not be accessible from the network. Iptables should be used to block these ports.
- **random**—This script provides for the random seed for the system.
- **rawdevices**—This service enables raw Input-Output (IO).
- **sshd**—This is the server that supports remote access to the workstation using a Secure Shell (SSH) client. If remote access into the workstation is not needed, this may be disabled.
- **syslog**—This process supports the logging of system messages, which can be sent to a central server for analysis and auditing.
- **xfs**—The X Font server shares fonts with other machines to speed up font rendering and to support TrueType–style fonts. This process may be required for XWindows to function efficiently. In these cases, the port can be blocked with iptables. Also, XWindows can be started without the feature of xfs looking out to the network. To do this, start X with `startx – -nolisten tcp`.
- **xinetd (inetd)**—This service starts other services on demand. xinetd is responsible for starting many of the common, small networking daemons. It only runs the daemon when a connection request is made for the particular service. For example, when the machine receives a pop3 request, xinetd starts up the ipop3d daemon to respond to the request. Any service can be made available via xinetd. A simple configuration file identifying the port and the service to run is put in the `/etc/xinetd/` directory. The following are typical services run via xinetd. None of these should be needed for a typical UNIX workstation that is not functioning as a server.**chargen** — A service that continuously generates characters until the connection is dropped. The characters look something like this: # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefg.**cups-lpd** — An on-demand version of the print daemons discussed earlier.**daytime** — A service that gets the current system time then prints it out in a format such as "Wed Nov 13 22:30:27 EST 2008."**echo** — A service that echoes characters back.**finger** — A service that displays information about users on a system. With the advent of brute force and social engineering attacks, it is no longer advisable to provide user information to non-authenticated users over the network.**imap** — A service that allows remote users to access their mail using an Internet Message Access Protocol (IMAP) client such as Mutt, Pine, fetchmail, or Netscape Communicator.**imaps** — A service that allows remote users to access their mail using an IMAP client with Secure Sockets Layer (SSL) support, such as Netscape Communicator or fetchmail.**ipop2** — A service that allows remote users to access their mail using a POP2 client such as fetchmail. In most cases, clients support POP3 instead of POP2, so enabling this service is rarely necessary.**ipop3** — A service that allows remote users to access their mail using a POP3 client such as Netscape Communicator, Mutt, or fetchmail.**ktalk** — A K Desktop Environment (KDE) version of the talk server (accepting talk requests for chatting with users on other systems).**ntalk** — A server that accepts ntalk connections, for chatting with users on different systems.**pop3s** — A service that allows remote users to access their mail using a POP3 client with SSL support such as fetchmail.**rexec** — A server for the rexec routine. The server provides remote execution facilities with authentication based on user names and passwords.**rlogin** — A server for the rlogin program. The server provides a remote login facility with authentication based on privileged port numbers from trusted hosts.**rsh** — A server for the rcmd routine and, consequently, for the rsh(1) program. The server provides remote execution facilities with authentication based on privileged port numbers from trusted hosts.**rsync** — A server that allows Cyclic Redundancy Check (CRC) checksumming.**servers** — A service that lists active server processes. This is discussed in detail in a later section.**sgi_fam** — A file-monitoring daemon. It can be used to get reports when files change.**talk** — A server that accepts talk requests for chatting with users on other systems.**telnet** — An on-demand daemon of the telnet service discussed earlier.**time** — This protocol provides a site-independent, machine-readable date and time. The time service sends back to the originating source the time in seconds since midnight on January 1, 1900.

### Uncommon services

The following services are useful and applicable in certain circumstances. Often these processes only apply to servers, as opposed to workstations. The system administrator should take a hard look at all these processes and if they are not needed, disable them.

- **anacron** — This service is an enhanced cron replacement. It can run jobs that were scheduled for execution while the computer was turned off.
- **atd** — This service runs scheduled batch jobs.
- **autofs** — This service auto mounts file systems on demand.
- **arpwatch** — This service is used to construct and monitor an ARP table, which keeps track of IP address-to-MAC address pairings.
- **apmd** — This is the advanced power management daemon, primarily used on laptops and other battery-backed devices. The apmd daemon senses the hardware and suspends or shuts down the workstation or laptop.
- **crond** — This service is used to schedule jobs for later execution. Many system administrator tasks can be run with cron. If this can't be disabled, authorization to run cron jobs should be limited to a few users.
- **gpm** — This service is the text-mode cut-and-paste daemon. This service has been a source of security concerns and performance problems in the past. Unless specific text-based applications are being used that require this mouse support, gpm should be disabled.
- **httpd** — This service is the Apache Web server. Web servers are a high visibility target for attacks. It is unlikely that a user's workstation needs to be running a Web server. In the vast majority of cases, this service should be disabled.
- **innd** — This service is the INternet News System (INN) news server. Normally this is run on a server and not a workstation.
- **irda** — This service is the Infrared TTY manager. Infrared is rarely used on a UNIX workstation, so this should be disabled.
- **mysqld and postgresql** — This service provides SQL database services. Usually, SQL databases are run on servers and not workstations.
- **named** — This service is the BIND name server used when running a Domain Name Service (DNS). This service will allow the host to resolve domain names into IP addresses. It is unusual for this service to be running on a workstation. DNS has important security concerns and needs to be configured and maintained carefully.
- **nscd** — This service provides password and group lookup services for use with network authentication such as that used in Lightweight Directory Access Protocol (LDAP).
- **ntpd** — Network Time Protocol (NTP) time synchronization services. If time synchronization is important, the network administrator should set up a local server to reduce the security risk.
- **netfs** — This service mounts NFS file systems.
- **RIP** — Routers use Route IP Protocol (RIP) to pass routing information. It is unlikely that the UNIX workstation is acting as a router, so this should be disabled. Plus this is an insecure routing protocol.
- **sendmail** — This service is a mail transport agent that enables users to send mail from the workstation. Normally, the network administrator will set up one mail server to service many users and workstations. If the workstation must run its own mail server, consider using qmail or postfix, which are more secure.
- **smb** — This service runs the smbd and nmbd SAMBA daemons, which allows the sharing of files with Microsoft Windows platforms.
- **snmpd** — Runs the supporting daemon for the Simple Network Management Protocol. Unless absolutely needed, this service should be disabled due to past and present security issues.

### Detecting services

Because the system administrator should disable unneeded processes, he or she must be able to detect and manage these services. Three good applications for this are ps, netstat, and nmap.

#### The ps command

This process gives a snapshot of the current processes running. The `ps` command will need to be run as root to pick up all the processes on the workstation. Following is a shortened output from `ps`:

```
# ps -aux
USER       PID %CPU %MEM   VSZ  RSS TTY      STAT START   TIME COMMAND
root         1  0.2  0.0  1376  440 ?        S    19:44   0:04 init [3]
root         2  0.0  0.0     0    0 ?        SW   19:44   0:00 [keventd]
root         9  0.0  0.0     0    0 ?        SW   19:44   0:00 [bdflush]
root         5  0.0  0.0     0    0 ?        SW   19:44   0:00 [kswapd]
root       217  0.0  0.0     0    0 ?        SW   19:45   0:00 [kjournald]
root       278  0.0  0.0     0    0 ?        SW   19:45   0:00 [knodemgrd]
root       498  0.0  0.0  1440  508 ?        S    19:45   0:00 syslogd -m
0
root       502  0.0  0.0  1372  424 ?        S    19:45   0:00 klogd -x
root       558  0.0  0.0  1496  480 ?        S    19:45   0:00
/sbin/cardmgr
root       623  0.0  0.1  3508 1132 ?        S    19:45   0:00
/usr/sbin/sshd
root       790  0.0  0.0  2264  440 ?        S    19:46   0:00 login –
root
root       791  0.0  0.0  1348   56 tty2     S    19:46   0:00
/sbin/mingetty tty2
root       796  0.0  0.0  4340  352 tty1     S    19:47   0:00 -bash
root      1637  0.0  0.0  2832  888 pts/2    R    20:18   0:00 ps -aux
```

#### The netstat Command

The `netstat` command prints all of the following:

- Network connections
- Routing tables
- Interface statistics
- Masquerade connections
- Multicast memberships

`netstat` can display a list of open sockets identified either by their port number or by the service assigned to that port as listed in `/etc/services`. If you don't specify any address families, the active sockets of all configured address families will be printed.

Knowing what ports are open on the workstation and accessible from the network is important to operating UNIX safely. The administrator should recognize every open port and understand the need for the application that is using that port. If the administrator does not recognize the port or service, he or she must track down the service and understand why that service needs to be running on that particular workstation.

Following is a sample listing of open ports and sockets used as reported by `netstat`. Note that the `-p` option provides the application that is responsible for the open port. Knowing the application is important in tracking down and closing ports.

```
# netstat -ap
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address   Foreign Address   State       PID
/Program name
tcp        0      0 *:ssh                   *:*       LISTEN      559
/sshd
tcp        0      0 localhost.localdoma:ipp *:*       LISTEN      584
/cupsd
udp        0      0 *:bootpc                *:*                   474
/dhclient
udp        0      0 *:631                   *:*                   584
/cupsd
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node Path
unix  2      [ ACC ]  STREAM  LISTENING     1209   /tmp/.font-unix/fs7100
unix  2      [ ACC ]  STREAM  LISTENING     1343   /tmp/.X11-unix/X0
unix  2      [ ACC ]  STREAM  LISTENING     1368   /tmp/ssh-
XXobUrxB/agent.808
unix  2      [ ACC ]  STREAM  LISTENING     1835   /tmp/.ICE-unix/dcop877-
1086703459
unix  2      [ ACC ]  STREAM  LISTENING     1960   /tmp/mcop-root/m_r_tmp-
037e
unix  7      [ ]      DGRAM                 956    /dev/log
unix  2      [ ACC ]  STREAM  LISTENING     2005   /tmp/.ICE-unix/906
```

Note that this powerful tool will also provide the current routing table. Following is router table information provided by `netstat`:

```
# netstat -r
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt
Iface
192.168.123.0   *               255.255.255.0   U         0 0          0
```

```
eth0
169.254.0.0     *               255.255.0.0     U         0 0          0
eth0
127.0.0.0       *               255.0.0.0       U         0 0          0
lo
default         pix             0.0.0.0         UG        0 0          0 eth0
```

#### The nmap Command

`nmap` is a very good port scanner that ships with many UNIX distributions and is available for all; `nmap` is designed to allow system administrators to scan hosts to determine what services are running. nmap supports a large number of scanning techniques, such as the following:

- UDP
- TCP connect()
- TCP SYN (half open)
- ftp proxy (bounce attack)
- Reverse-ident
- ICMP (ping sweep)
- FIN
- ACK sweep
- Xmas Tree
- SYN sweep
- IP Protocol
- Null scan

The following shows the output of two nmap scans of a Linux host. nmap can be run over the network or against the host that it resides on, as in these scans. The `-sT` option tells nmap to run a TCP Connect scan; therefore, nmap will attempt to connect to every port to determine the service running on that port. The first scan is against the host's external interface. The second scan of the localhost interface avoids the iptables (firewall) filtering that protects the host. Notice that port 631 is being blocked by iptables. Iptables is discussed in detail in the "Hardening UNIX" section of this chapter.

```
# nmap -sT 192.168.1.5
Starting nmap V. 3.00 ( www.insecure.org/nmap/ )
Interesting ports on  (192.168.1.5):
(The 1600 ports scanned but not shown below are in state: closed)
Port       State       Service
22/tcp     open        ssh
Nmap run completed – 1 IP address (1 host up) scanned in 5 seconds

# nmap -sT localhost
Starting nmap V. 3.00 ( www.insecure.org/nmap/ )
```

```
Interesting ports on localhost.localdomain (127.0.0.1):
(The 1599 ports scanned but not shown below are in state: closed)
Port       State       Service
22/tcp     open        ssh
631/tcp    open        ipp
Nmap run completed – 1 IP address (1 host up) scanned in 1 second
```

### Processes controlling processes

In addition to knowing what processes are running, the system administrator must be able to schedule the proper services to run at the proper time. UNIX provides four means of controlling processes: inti, xinetd (inetd), chkconfig, and service.

#### The init process

After the UNIX kernel boots, it will place the operating system into one of several runlevels. The runlevel will determine which processes and services are started (or stopped). The following describes the seven runlevels in Linux:

- **Runlevel** — This is the shutdown state. When a system is properly shut down, it is transitioned into this runlevel. During that transition, certain processes or services will be killed (stopped), as defined in the `/etc/rc.d/rc0.d` directory.
- **Runlevel 1** — This is the single-user mode. The system has one session (the command prompt) and the user is always root. This state is typically used to troubleshoot the workstation or when conducting backups. Some administrators might prefer to pass through this runlevel when starting up and shutting down the workstation. The processes started and stopped in runlevel 1 are governed by the files in the `/etc/rc.d/rc1.d` directory.
- **Runlevel 2** — This is multi-user mode without networking. This state is rarely used. The processes started and stopped in runlevel 2 are governed by the files in the `/etc/rc.d/rc2.d` directory.
- **Runlevel 3** — This is multi-user mode with networking. This is the normal state to which the system will boot. Some systems are configured to boot directly into XWindows (runlevel 6). The processes started and stopped in runlevel 3 are governed by the files in the `/etc/rc.d/rc3.d` directory.
- **Runlevel 4** — This is unused on many versions of UNIX. The processes started and stopped in runlevel 4 are governed by the files in the `/etc/rc.d/rc4.d` directory.
- **Runlevel 5** — This is typically the XWindows mode. Systems are sometimes configured to boot into this state. Otherwise, this runlevel is entered by starting XWindows (startx) from runlevel 2 or 3. The processes started and stopped in runlevel 5 are governed by the files in the `/etc/rc.d/rc5.d` directory.
- **Runlevel 6** — This is the reboot state. When reboot or a similar command is issued, the system transitions into this runlevel. The processes started and stopped in runlevel 6 are governed by the files in the `/etc/rc.d/rc6.d` directory. All of the files in this directory are set to either kill processes or to start processes, which will in turn kill all other processes and force the reboot.

The scripts in the `/etc/rc.d/rc<runlevel>.d` directories begin with an `S` to start a process or with a `K` to shut down (kill) a process. The numbers following the letters (`S` or `K`) determine the order of execution from lowest to highest.

When UNIX boots, the kernel executes `/sbin/init`, which starts all other processes. The init process determines which runlevel to load by reading the `/etc/inittab` file. For example, the kernel will boot into the runlevel in the initdefault line in the `/etc/inittab` file, such as follows:

```
id:5:initdefault:
```

In this case, the default is runlevel 5, or XWindows.

The `/etc/inittab` file describes which processes are started at bootup and during normal operation (for example, `/etc/init.d/boot`, `/etc/init.d/rc`, `gettys` ...). init distinguishes multiple runlevels, each of which can have its own set of processes that are started. Valid runlevels are 0 through 6 plus A, B, and C for on-demand entries. An entry in the `inittab` file has the following format:

```
id:runlevels:action:process
```

An important security feature that can be controlled by init is the process that runs when a user simultaneously presses the three keys Ctrl+Alt+Delete. The system administrator may need to limit a non-root user's ability to shut down a key server. The following line in the `/etc/inittab` file will set the Ctrl+Alt+Del interrupt to run the exit process. This would log off the user but would not reboot the machine.

```
ca::ctrlaltdel:/sbin/shutdown -nh now
```

Use the command `ps -aux` to view all process on your machine.

#### The xinetd process

The xinetd process (inetd on some platforms) is a service that starts other services on demand. It only runs the daemon when a connection request is made for the particular service. A simple configuration file identifying the port and the service to run is put in the `/etc/xinetd/` directory. The following is a listing off one of these configuration files for the POP3 service:

```
# cat /etc/xinetd.d/ipop3
# default: off
# description: The POP3 service allows remote users to access their mail \
#              using an POP3 client such as Netscape Communicator, mutt, \
#              or fetchmail.
service pop3
{
        socket_type           =stream
        wait                  =no
        user                  =root
        server                =/usr/sbin/ipop3d
        log_on_success  += HOST DURATION
```

```
log_on_failure  += HOST
        disable               =yes
}
```

Of particular interest is the last line of the configuration, `disable=yes`. This will prevent xinitd from responding to a request on the POP3 port. To enable POP3, the `yes` is changed to `no`.

Note that the port for POP3 is not provided in the preceding configuration file. When the port is not designated, xinetd uses the port listed in the `/etc/services` file, as follows:

```
# grep pop3 /etc/services
pop3            110/tcp         pop-3           # POP version 3
pop3            110/udp         pop-3
pop3s           995/tcp                         # POP-3 over SSL
pop3s           995/udp                         # POP-3 over SSL
```

Because the services controlled by xinetd are on demand, they will not run until the associated port is hit from the network. Assuming that the POP3 service is enabled (`disable=no` in the configuration file), you will see the open port in the following (shortened) netstat output:

```
# netstat -ap
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address  Foreign Address  State   PID/Program
name
tcp        0      0 *:pop3         *:*              LISTEN  2295/xinetd
```

However, when you look at the ps output, you do not see POP3 running because the port has not yet been hit from the network.

```
# ps -aux | grep pop3
root      2307  0.0  0.0  3568  624 pts/2    S    07:44   0:00 grep pop3
```

The xinetd process can control processes in numerous ways. There are means for special logging and controlling of the services. There are several ways to lower the risk of a denial-of-service (DoS) attack.

### Note

The man pages for `xinetd.conf` provide a detailed listing of these options.

#### The chkconfig command

`chkconfig` provides a command-line tool for maintaining the `/etc/rc[0-6].d` directory hierarchy. This is a big aid to the system administrators who would otherwise have to directly manipulate the numerous symbolic links in those directories.

The tool manipulates services in the following manner:

- **Adds a new service for management** — `chkconfig` will ensure that the symbolic links are in the proper directories.
- **Removes services from management** — The symbolic links are removed.
- **Lists the current startup information for services** — `chkconfig` gives a very readable status of what services will run in which runlevels. This is convenient for the system administrator, who would otherwise have to scrutinize symbolic links to determine what will run.
- **Changes the startup information for services** — `chkconfig` can add symbolic links to start or stop services for particular run levels.
- **Checks if a particular service is to be run at a certain runlevel** — This feature differs from the previous listings in that no output is provided. Instead, `chkconfig` returns `TRUE` or `FALSE` for use in a batch shell script.

Following are a few lines from the output of `chkconfig` showing which services are scheduled to be run at each of the runlevels:

```
# chkconfig –list
postgresql      0:off   1:off   2:off   3:off   4:off   5:off   6:off
squid           0:off   1:off   2:off   3:off   4:off   5:off   6:off
vmware          0:off   1:off   2:off   3:off   4:off   5:off   6:off
rclocal         0:off   1:off   2:off   3:on    4:on    5:on    6:off
network         0:off   1:off   2:on    3:on    4:on    5:on    6:off
syslog          0:off   1:off   2:on    3:on    4:on    5:on    6:off
random          0:off   1:off   2:on    3:on    4:on    5:on    6:off
pcmcia          0:off   1:off   2:on    3:on    4:on    5:on    6:off
rawdevices      0:off   1:off   2:off   3:on    4:on    5:on    6:off
```

The following shows a few of the symbolic links in the `/etc/rc.d/rc3.d/` directory (runlevel 3). It is evident that the format from `chkconfig` is much more convenient and informative than listing all the directories.

```
K15postgresql -> ../init.d/postgresql*
K25squid -> ../init.d/squid*
K08vmware -> ../init.d/vmware*
S05rclocal -> ../init.d/rclocal*
S10network -> ../init.d/network*
S12syslog -> ../init.d/syslog*
S20random -> ../init.d/random*
S24pcmcia -> ../init.d/pcmcia*
S56rawdevices -> ../init.d/rawdevices*
```

#### The service command

The `service` command can affect the running of a process or report on the status of the process. The service function essentially runs the process through the `init.d` scripts found in the `/etc/init.d/` directory. According to convention, these scripts take the following options:

- `start`—Force a start of the process, regardless of the current runlevel.
- `stop`—Force a stop of the process and clean up as appropriate.
- `restart`—Stop and then start the process.
- `condrestart`—Process-dependent, but usually the same as restart.
- `status`—Process dependent, but will print some information about the process. For example, in the case of iptables, the current rules are listed.

With the `—status-all` option, the tool lists the status of every service that is in the `/etc/rc.d/init.d/` directory. In addition to whether the service is running, other pertinent information is displayed. Following is a shortened display of currently running processes:

```
# service –status-all
anacron is stopped
apmd is stopped
atd is stopped
Configured Mount Points:
-----------------------
Active Mount Points:
--------------------
crond is stopped
gpm is stopped
httpd is stopped
sshd (pid 638) is running...
syslogd (pid 528) is running...
klogd (pid 532) is running...
tux is stopped
winbindd is stopped
xfs (pid 817) is running...
xinetd is stopped
```

## Controlling users

In addition to controlling processes, it is necessary to have controls over the users of the UNIX workstation. This consists of controlling the user's access to files and their ability to run processes. The UNIX file permission scheme determines what access a user will have to any given file. Controlling a user's access to processes mostly concerns controlling root access.

### File permissions

UNIX design expects individual users to log in to workstations with their own user IDs and passwords. The file permissions method used is predicated on classifying the user into one of three categories. Each file in UNIX is then flagged with certain permissions based on the category of the user. The individual login is required to properly place a user in the categories. A user will belong to each of these categories:

- **World** — Every user is a member of this category. Permissions granted to the world would be granted to any user on the UNIX workstation.
- **Group** — Every user should be a member of at least one group. Permissions granted to the group are granted to all the individual users in that group.
- **Owner** — Every user will own (create) some files. The permissions granted to the owner apply to the user who is the file creator. File ownership can also be changed after creation.

Passwords and user information are stored in the `/etc/passwd` file. If shadow passwords are used, the passwords are stored in the `/etc/shadow` file. Group membership is stored in `/etc/group`. A user may be in more than one group. Only the administrator can create new groups or add and delete group members.

[Figure 9-1](ch09.html#unix_file_permissions) provides a sample listing of assigned file permissions.

![UNIX file permissions](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0901.png)

**Figure 9.1. UNIX file permissions**

Now that the users are categorized as World, Group, and Owner, you need to put flags on each file to correspond to the user category. The flags may also be used for more than just permissions. The permission flags are read left to right, as shown in [Table 9-1](ch09.html#file_permission_flags).

**Table 9.1. File Permission Flags**

| Position | Permission or Type |
| --- | --- |
| 1 | Not a permission, the first flag is the file type, `d` if a directory, `-` if a normal file, `c` or `b` for special devices |
| 2,3,4 | Read, write, execute permission for Owner of the file |
| 5,6,7 | Read, write, execute permission for members of the Group assigned to the file |
| 8,9,10 | Read, write, execute permission for the World (any user) |

A dash (`-`) in any position means that a flag is not set. The flags of *r*, *w*, and *x* are shorthand for *read*, *write*, and *executable*. When an *s* is in place of an *x*, it means the User ID (UID) bit is on. When a *t* is in place of an *x* the sticky bit is set. The sticky bit is used to protect the renaming or removal of files in a directory. If the owner of a directory sets its sticky bit, the only people who can rename or remove any file in that directory are the file's owner, the directory's owner, and the superuser.

If a world or group user can execute the file while the UID bit is on, the execution will run as though the owner is running the file. Any permissions or access granted to the owner is thus applied to that execution. There are some security concerns when creating an executable or script that has the UID bit set. All the normal access permissions that UNIX provides to limit a user might be circumvented if the user can execute a file owned by root with the UID bit set.

For a directory, the setgid flag means that all files created inside that directory will inherit the directory's group. Without this flag, a file assumes the primary group of the user creating the file. This property is important to people trying to maintain a directory as group accessible. The subdirectories also inherit the `set-groupID` property.

The sticky bit is used to ensure that users do not overwrite each other's files. When the sticky bit *t* is set for a directory, users can only remove or rename files that they own.

To read a file, you need execute access to the directory it is in and read access to the file itself. To write a file, you need execute access to the directory and write access to the file. To create new files or delete files, you need write access to the directory. You also need execute access to all parent directories back to the root. Group access will break if a parent directory is made completely private.

When a new file or directory is created, the file permissions will be set to the *umask* that is set in the user's environment. Because this is a mask, use XOR to determine the file permissions to be set. Typically, the default configuration is equivalent to typing `umask 22`, which produces permissions of `-rw-r—r—` for regular files, or `drwxr-xr-x` for directories. This can lead to giving read access to files such as saved e-mail in your home directory, which is generally not desirable.

Care must be taken when assigning a group or changing the group access on a file or directory. The `/etc/group` file should be checked to ensure that only the intended users are given access. Consider, also, that the administrator may change the group membership at a later date, giving more persons access to files assigned to a group.

### Set UID

Normally, when a user executes a program, it is run with the user or group ID (U/GID) and the program has the same privileges and access as the user or group. The program can access the same resources permitted to the user or group. Any files created by the process are owned by the user.

However, there are times when the processes executed on the user's behalf need to have root privileges, not user privileges. A typical example is the mount process, which calls the kernel to mount file systems.

A process or program has the privileges of the owner of the program (as opposed to the user) when the set UID (SUID) flag is set on the program's file permissions. As a security measure, only root is permitted to set the UID flag.

The following series of commands demonstrates the setting of the Set UID flag on an executable. First, you see from the long listing of the file that the permissions are set to `rwx r-x r-x` and no set UID flag is set.

```
# ls -l fake_exe
-rwxr-xr-x    1 root     root            0 Jun 13 12:25 fake_exe
```

Now the mode is changed to set the UID flag. You then see from another long listing that the `chmod` command has set the UID flag and the file permissions are now `rws r-s r-x`.

```
# chmod +s fake_exe

# ls -l fake_exe
-rwsr-sr-x    1 root     root            0 Jun 13 12:25 fake_exe
```

The ability of a user to run a process with root powers is a definite security concern. System administrators should keep track of all applications with the UID flag set. Programs that set the UID to root are a potential avenue for users or attackers to gain root access. [Table 9-2](ch09.html#uid_comma_gid_comma_and_sticky_bits) shows a search of all files on a UNIX workstation that has the UID, GID, and sticky bit set.

To minimize the risk of a program with the UID flag set, the system administrator should decide if non-root users need to run the program. For example, a case can be made qwqthat normal users do not need to test network connections using applications such as ping and traceroute.

### Chroot

The `chroot` command runs a service with an alternative root directory. For example, if the DNS bind service was launched with `chroot` under the alternative directory of `/opt/dns/`, when the bind process refers to the `/` directory, it will really be accessing the `/opt/dns/` directory. The bind configuration file, normally at `/var/named.conf`, will need to be copied to `/opt/dns/var/named.conf`. The same is true for all files (libraries, executables, and data) that bind will need to run.

The security gains are well worth the effort of setting up the alternative root directory. Now, if compromised, the service will only have at risk the files in the alternative root directory and all subdirectories. The service cannot "see" above the alternate root directory and neither will the attacker. This can be a huge security advantage because only the minimal number of supporting files needs to be put in the alternative root directory tree to support the service. This limits the data that the attacker has access to. Also, if the service is compromised, the attacker is less likely to be able to spread the attack to other services on the host.

The service is launched by `chroot` with the following command:

```
chroot <alternative root directory> <service with command line options>
```

The alternative root directory setup is not trivial. Any supporting file that the service will need must be copied into the new data structure. This may include a reduced `/bin`, `/usr/lib`, and `/usr/local`, among others.

### Root access

You'll recall from earlier discussions on the kernel that UNIX has only two modes: supervisor (root) and normal (user). In this scheme, root has complete control and access over the entire workstation. For users, on the other hand, not only is their access restricted, but if a user-run application attempts to access memory that is restricted to root access, a segmentation fault will occur, stopping the attempt.

**Table 9.2. UID, GID, and Sticky Bits**

| Files with UID Flag Set | Files with GID Flag Set | Files with Sticky Bit Set |
| --- | --- | --- |
| # find / -perm +4000 | # find / -perm +2000 | # find / -perm +1000 |
| /usr/bin/chage /usr/bin/gpasswd /usr/bin/chfn /usr/bin/chsh /usr/bin/newgrp /usr/bin/passwd /usr/bin/at /usr/bin/rcp /usr/bin/rlogin /usr/bin/rsh /usr/bin/sudo /usr/bin/crontab /usr/bin/lppasswd /usr/bin/desktop-create-kmenu /usr/bin/kcheckpass /usr/lib/news/bin/inndstart /usr/lib/news/bin/rnews /usr/lib/news/bin/startinnfeed /usr/libexec/openssh/ssh-keysign /usr/sbin/ping6 /usr/sbin/traceroute6 /usr/sbin/usernetctl /usr/sbin/userhelper /usr/sbin/userisdnctl /usr/sbin/traceroute /usr/sbin/suexec /usr/X11R6/bin/XFree86 /bin/ping /bin/mount /bin/umount /bin/su /sbin/pam_timestamp_check /sbin/pwdb_chkpwd /sbin/unix_chkpwd | /tmp/app /usr/bin/wall /usr/bin/write /usr/bin/lockfile /usr/bin/slocate /usr/bin/kdesud /usr/sbin/lockdev /usr/sbin/sendmail.sendmail /usr/sbin/utempter /usr/sbin/gnome-pty-helper /usr/sbin/postdrop /usr/sbin/postqueue /sbin/netreport | Read, write, execute permission for Owner of the file/dev/shm /var/lib/texmf /var/tmp /var/run/vmware /var/spool/vbox /var/spool/samba /var/spool/cups/tmp |

It should, therefore, be obvious that attacks on a UNIX workstation focus around getting root access. To reduce the risk to the workstation, system administrators should be reluctant to provide root access to users. Following are some of the problems that can arise if a normal user has root access:

- Users with root access can change the configuration of the workstation and potentially alter the security controls that the system administrator put in place. For example, a particular service may have been set up to run only in an alternative root directory with `chroot`. If a user unknowingly launches the service from the command line, this `chroot` protection will be lost.
- Users may launch services that open the workstation up to potential attacks. For example, Web servers are high-visibility targets and require significant hardening and configuration to be secure. Typical users will not apply the needed level of security for their locally run Web server.
- Simple mistakes made by the user can be magnified. Every administrator at one time or another has lost track of the directory he or she was in and inadvertently run the following command: `rm -rf *`. This, if you don't recognize it, will delete every (non-hidden) file in the current directory and recursively into all subdirectories, without question. Generally, administrators learn these lessons early on and such control (power) is safe in their hands. However, this may not be the case for the average user. This example is the very kind of thing that can be minimized if the user is logged in as other than root. The user can still do a lot of damage, but it is usually self-inflicted and probably will not delete files owned and controlled by root.

Several steps can be taken to limit the use of the root account on a UNIX workstation. The following lists a couple of the key steps:

- **Limit access to the workstation directly as root**. All users should be required to log in to the workstation under their limited privilege user account and then `su` to root if they need to do root-level activities. This can be done by setting the root login shell to `/sbin/nologin` in the `/etc/passwd` file. The `su` command is sometimes referred to as the super user command because it allows a normal user to assume root-level privileges, assuming that the proper root password is provided.
- **Limit remote access to the workstation by root**. Services that permit remote login, such as sshd, should be configured not to allow root. The system administrator will have to log in as a normal user and then su to root. Each service has its own configuration method, but in the case of sshd, root access is controlled by adding the line `PermitRootLogin no` to the `/etc/ssh/sshd_config` file.

Denying root the ability to log in directly to the UNIX workstation has some important effects from a security perspective, as follows:

- The activity conducted by root can be attributed to an individual. The logs on the workstation will log the normal user's login and the user's transition to root via `su`. Should a problem arise from the activity, an individual can be queried to account for the changes made.
- If the root password is compromised and acquired by a normal user, the user will not be able to use it to log in directly as root.
- Because any user must su to root to perform root-level activities, limiting the users who can run su can add a layer of protection. This is done by controlling which users are in the wheel group in the `/etc/group` file because only these users are permitted to su to root. So, even if a normal user acquires the root password, this user can be prevented from getting root access, through the `su` command, by not being put into the wheel group.

The protections discussed so far—limit the direct access of the root and control which users are in the wheel group—add significant security to the workstation. But these security gains can be reduced if every user is added to the wheel group (granting every user the ability to su to root). This can easily happen if the average user needs to perform a relatively trivial root activity. A good example of this is mounting a CD-ROM or floppy. Because of one activity (mounting), all users might be given root-level access (put into the wheel group). This is obviously a security risk. The solution to this problem is the `sudo` command.

The `sudo` command allows normal users to execute certain commands that would normally be limited to root. In the case of mounting a floppy, the command would be as follows:

```
sudo mount /dev/fd0 /mnt/floppy
```

Now certain users will be able to execute a limited number of root-level commands. The system administrator controls which users and which commands can be run by `sudo` through the configuration file `/etc/sudoers`.

## Encryption and certificates

The defense-in-depth strategy toward security requires system administrators to take every possible action to improve security. One significant improvement to security can be obtained by widespread use of encryption. With respect to the UNIX workstation, the following are security advantages to be gained:

- If a workstation gets compromised and taken over by an attacker, previously encrypted files are likely to be protected. This assumes that passphrases used to encrypt the data are kept in the users' memory and not on the workstation.
- By encrypting traffic on the local area network (LAN), the risk of being attacked from a local source is greatly reduced. Many organizations consider their biggest security feature to be the firewall between the LAN and the Internet. However, other workstations on the LAN also pose a significant threat. For example, if the LAN is hubbed, any workstation can listen in on all instant messaging to and from another workstation. Even if the network is switched there are readily available tools, such as ettercap, that can monitor all traffic in and out of a workstation.
- Much of the traffic that travels over the Internet, such as e-mail or FTP, is in the clear or unencrypted. The only protection afforded to this traffic is security through obscurity. In other words, the telnet, e-mail, and FTP traffic can be read in many places as the traffic is routed, but who would want to? Most users would not find this level of security very comforting.

As with most things in life, the decision to use encryption is based on a cost-benefit analysis. The benefits are huge. Because encryption is getting easier to implement the cost is certainly being reduced. It is now reasonable for an organization to encrypt all telnet, e-mail, and FTP traffic.

### GNU Privacy Guard

GNU Privacy Guard (GPG) is a UNIX implementation of the popular and robust Pretty Good Privacy (PGP) encryption program by Phil Zimmerman. Files encrypted by one can be decrypted by the other (and vice versa). GPG is free and available for all versions of UNIX.

GPG is most commonly used to encrypt files and e-mail messages. E-mail clients, such as Evolution, integrate well with GPG. If an e-mail client does not support GPG integration, the messages must be saved as a file before decrypting.

GPG uses the public-key method of encrypting data. Public-key encryption (also called asymmetric encryption) involves a pair of keys—a public key and a private key—associated with the user. A user's public key can be widely distributed and used to encrypt a file or message being sent to the user. The user then uses his or her private key, which is protected with a passphrase, to decrypt the file or message. In simple terms, a file encrypted with the public key can only be decrypted with the private key, and vice versa.

In addition to encrypting files and messages, GPG can be used to sign an e-mail message. A signed message allows the recipient to verify the sender. The recipient can verify that the message was signed with the sender's private key.

Users must protect their passphrase and private key. Both are needed to decrypt a file or message. If a user's private key is stolen, an attacker could attempt a brute force attack on encrypted data. Therefore, a strong (hard-to-guess) passphrase is also important. If someone obtains a user's private key and passphrase, the person would be able to impersonate the user in e-mail traffic.

### The Secure Shell program

The Secure Shell (SSH) program supports logging into and executing commands on a remote machine. It is intended to replace rlogin and rsh and provide secure encrypted communications over a network. XWindows connections and TCP/IP ports can also be forwarded over the secure channel.

The SSH application uses public-private key technology to exchange a session key. All the SSH traffic is then encrypted with the session key.

The SSH application can be used to forward ports through the secure tunnel. The following is an example of using SSH to secure the transfer of e-mail to and from a mail server. The command is shown spanning multiple lines, to aid in this discussion.

```
ssh -l user1 \
    -L 110:smtp.somedomain.org:110 \
    -L 25:smtp.somedomain.org:25 \
     smtp.somedomain.org
```

The first part of the command calls ssh with a `-l` [ell] option that gives the user name to be used to log into the mail server. The next option, `-L`, designates that port `110` on the local host should be forwarded to the POP3 port `110` on the `smtp.somedomain.org`. This means that to retrieve e-mail with the POP protocol from the remote host, the user only needs to retrieve e-mail from the local 110 port. In a similar manner, the SMTP port `25` is also forwarded. And, finally, the host to which the SSH session connects is given.

The `scp` command copies files between hosts on a network. This command uses SSH for data transfer, and uses the same authentication and provides the same security as SSH. The user's password is required for `scp`. The syntax for `scp` is as follows:

```
scp  -r  smpt.somedomain.org:/var/spool/mail/user1  /tmp
```

In this example, `scp` copies the mail box of `user1` from the host `smtp.somedomain.org` to the local directory of `/tmp`.

# Hardening UNIX

Any workstation connected to a network needs to be hardened against attack. Following are some general principles that should be applied when hardening a system:

- Assume that default installations of any distribution will be inherently unsafe until hardened.
- Limit software, processes, and access to the minimum needed to perform the mission of the workstation.
- Use more secure alternatives to insecure services (such as using SSH instead of telnet).
- Keep current with security patches and upgrades for software packages.
- Use iptables to back up the hardening of the workstation.

## Configuration items

Hardening an operating system usually consists of many small steps. Here are some that apply to UNIX workstations:

- Run high visibility services accessed from the network as chroot, if possible. Recall the earlier discussion on chroot. Good candidate services are Domain Name Server (DNS) and Web servers.
- Disable unneeded services.
- Remove unneeded software packages.
- Run iptables to filter traffic coming in from the network.
- Set `nosuid`, `noexec`, `nodev` in `/etc/fstab` on ext2 partitions, such as `/tmp`, that are accessible by everyone. This reduces the risk of a Trojan horse attack.
- Use strong passwords. In a nutshell, a strong password is not based on common words and cannot be cracked with a brute force attack (in a reasonable amount of time).
- Enable password shadowing.
- Configure `/etc/login.defs`. Among other things, the following can be set:PASS_MAX_DAYS—Maximum number of days a password may be used.PASS_MIN_DAYS—Minimum number of days allowed between password changes.PASS_MIN_LEN—Minimum acceptable password length.PASS_WARN_AGE—Number of days warning given before a password expires.
- Add a wheel group to designate which users are allowed to `su` to root.
- Disable root logins and have administrators use `su` to get root access.
- Limit TTY and root access in `/etc/security/access.conf`.
- Set limits in `/etc/security/limits.conf`. Limits can be assigned to individual users or by groups. Items that can be limited include the following:`core`—Limits the core file size (KB)`data`—Maximum data size (KB)`fsize`—Maximum filesize (KB)`memlock`—Maximum locked-in-memory address space (KB)`nofile`—Maximum number of open files`rss`—Maximum resident set size (KB)`stack`—Maximum stack size (KB)`cpu`—Maximum CPU time (MIN)`nproc`—Maximum number of processes`as`—Address space limit`maxlogins`—Maximum number of logins for this user`priority`—The priority to run user process with`locks`—Maximum number of file locks the user can hold
- Disable root and anonymous FTP access in `/etc/ftpusers`.
- Protect log files by limiting access to root. Log files are an important means to detect and counter an attack. The early stages of an attack often deal with deleting and disabling logging. Consider setting up a loghost and have critical systems send their logs to a central log server for greater protection and monitoring.
- Consider burning operating system and services on a CD and booting from that CD. This is only practical for stable non-changing servers.
- Disable remote X by adding `—nolisten tcp` to the X command line (usually `startx`).
- Train system administrators and users on security issues and attack prevention.

## TCP wrapper

TCP wrapper can be a powerful tool for the system administrator to minimize the risk of an attack. Here is how `www.cert.org` describes this tool:

> *Servers on UNIX systems usually either provide their services via the TCP/IP protocol stack to everyone or no one. In addition to this conceptual weakness, logging of connections is minimal and does not include, for example, source or timestamp. Connection attempts can be an early warning signal that a site is under attack so you want to capture as much information as possible*.
> 
> *Tcpd, the program implementing the tcp wrapper, was developed as a result of an actual attack. It provides (1) some level of access control based on the source and destination of the connection request and (2) logging for successful and unsuccessful connections. tcp wrapper starts a filter program before the requested server process is started, assuming the connection request is permitted by the access control lists. All messages about connections and connection attempts are logged via syslogd*.

## Checking strong passwords

To protect the network from attacks, a system administrator can verify that strong passwords are in place. The most effective way to test passwords is to run a password-cracking program against the workstation.

A number of good password-cracking applications are easily acquired. The site `www.redhat.com` reports on the following password crackers:

- **John The Ripper** — A fast and flexible password-cracking program. It allows the use of multiple word lists and is capable of brute-force password cracking. It is available at `www.openwall.com/john/`.
- **Crack** — Perhaps the most well-known password-cracking software, Crack is also very fast, though not as easy to use as John The Ripper. It can be found at `www.users.dircon.co.uk/~crypto/index.html`.
- **Slurpie** — Slurpie is similar to John The Ripper and Crack except it is designed to run on multiple computers simultaneously, creating a distributed password-cracking attack. It can be found along with a number of other distributed attack security evaluation tools at `www.ussrback.com/distributed.htm`.

## Packet filtering with iptables

As the last line of defense against an attack from the network, the UNIX workstation can run a host-based firewall, such as iptables. Iptables is a packet filter that works off rules controlling packets on the input, output, and when they are forwarded through the interfaces.

A packet filter such as iptables will examine the header of packets as they pass through and process the packet in one of the following three ways:

- **Deny the packet**. Discard the packet with no trace of having received it.
- **Accept the packet**. Let the packet go through.
- **Reject the packet**. Similar to deny, but the sender is notified that the packet was rejected.

The typical iptables configuration for a UNIX workstation is as follows:

- Allow all network-bound traffic to leave the workstation. Generally, outbound traffic does not pose a threat to the workstation itself. It may be advisable to limit outbound traffic to prevent the spread of viruses and worms. Unfortunately, these often function similarly to how a user might (sending e-mail, for example) and are, therefore, difficult to block on the outbound path.
- Block all incoming traffic that is not specifically allowed. With only a few exceptions, the world (everyone coming in from the network) does not have a need to reach ports on the workstation.
- Explicitly open individual ports (services) that are needed from the network. On a UNIX workstation, this is usually just SSH (port 22) for remote access, but even that may not be needed. Other typical services that might be allowed are usually on dedicated servers, such as HTTP Web service (port 80), FTP file transfer (port 21), and SMTP e-mail (port 25).

The second configuration item in the preceding list ("block all incoming traffic") is the key defense-in-depth backup to other security preparations taken on the UNIX workstations. Unneeded services should not be running, but if they are, they can still be blocked from use by the network with iptables. Unneeded software should not be available on the workstation, but if it is found and launched as a service by an attacker, it can still be blocked by iptables.

As with most operating systems, most versions of Linux come with a personal firewall installed and sometimes configured for your system. As with most personal firewalls, iptables installs hooks (call back functions) into the network stack of the operating system. As a result, every time a packet arrives at your machine, a function is called that is able to parse the packet and determine what, if anything, should be done with it. The basic options for most firewalls are to either drop packets that fit a certain user-defined description, or to allow the packet to enter the system and be processed by any potentially waiting applications, such as a Web server. While having the ability to drop packets is enough to protect your system from unwanted packets, iptables also allows the ability to log such packets. This will be discussed more in the section "[Logging Blocked Traffic](ch09.html#logging_blocked_traffic)." Iptables also has the ability to match packets, or a set of packets with more abstract settings, such as limiting the amount of traffic that enters or leaves your system. This can be very beneficial in preventing or slowing the spread of computer viruses. This will be discussed further in the section "[Advanced Blocking Techniques](ch09.html#advanced_blocking_techniques)." While the details covered in the remainder of this article are specific to iptables, the principles can be applied to any personal firewall.

### Blocking incoming traffic

Initially, the packets that you want to prevent from entering your system are those attempting to make a connection to some port on your computer. In most cases the average workstation or home computer will never have a service running that should be accepting packets, unless that connection has first been initialized by your computer. For example, when a Web browser attempts to visit a site, the Web browser initiates a connection with the Web server. Packets are then sent back and forth between your computer and the Web server. However, it is important to note that it was your Web browser that sent the packets initializing the request. With most workstations there will never be an instance where someone else's computer will initiate a connection to your workstation. To drop all packets that attempt to make a connection to your computer the following command can be issued using iptables:

```
iptables  -A INPUT -p tcp -m tcp !
-tcp-flags SYN,RST,ACK SYN -j ACCEPT
```

This command tells iptables that you would like to add a rule to the `INPUT` chain. The `INPUT` chain handles all of the packets that come into your system. The `-p` flag is for the protocol and the `-m` flag is for matching. These flags are explained in much more detail in the manual page for iptables; however, the flags that follow `–tcp-flags` require a bit more commentary because they are the essence of this rule. When a computer attempts to make a connection to another computer using the TCP protocol, a SYN packet is first sent to the host. This SYN packet tells the server that an attempt is being made to setup a connection with it. By simply blocking these packets, you can prevent all users from making connections to your computer, through TCP, thus achieving our goal. This command, however, accepts packets that are not SYN packets. At first this seems a bit counterintuitive until it is stated that security should almost always be set up by denying everything, and then allowing only what is needed. The same is true for personal firewalls. All packets into your computer should be by default dropped, unless explicitly allowed to enter. This rule allows for explicitly letting non-SYN packets into your computer, but first the default action of dropping must be turned on. To drop all packets coming into your computer by default the following command is issued:

```
iptables -P INPUT DROP
```

Now your computer drops all packets by default, unless they are non-SYN packets. Using a default rule of drop and allowing only non-SYN packets into your system is actually quite a strong default setup. In fact in most cases the only other setup that is needed will be to allow incoming SYN packets to specific ports where programs are running and listening for traffic. These programs can be anything from SSH to some piece of custom administrative software. To allow access to your computer via SSH, for example, the following command can be issued:

```
iptables -A INPUT -p TCP –destination-port 22 -j ACCEPT
```

This will allow connections from any computer to yours through SSH. The same can be done for any other program that someone might need to connect to on your computer, by simply substituting the proper port number. It's normally a good idea not to add any of these rules at the beginning, but to add them as problems arise. This prevents opening up a port on a computer where there is a process listening on that port, but the device is not properly configured, such as a Web server.

Once you have your computer configured to drop all packets by default and to allow only those packets that are not trying to make connections to your computer, you will notice that your computer can no longer make connections to Internet hosts. This is because DNS is being blocked, so your computer is unable to translate addresses such as `www.sysadminmag.com` into the IP address of 66.77.24.5. To enable DNS you have to let UDP packets through, with a source port of 53. This can be done by issuing the following command:

```
iptables -I INPUT 1 -p udp -destination-port 53 -j ACCEPT
```

By using the `-I` flag with the number 1, this rule goes to the top of the list because every time your computer connects to another machine it must resolve the name. It is a good idea to put this rule at the top of the list. However, much care and time has been put into the design of iptables so that looking up rules is very, very fast.

If you have issued the commands outlined previously, without any other commands, your iptable configuration should look something like this:

```
Chain INPUT (policy DROP)
target     prot opt source     destination
ACCEPT     udp  --  0.0.0.0/0  0.0.0.0/0        udp spt:53
ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0        tcp flags:!0x16/0x02
ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0        tcp dpt:22
```

This can be obtained by using the following command:

```
iptables -L -n
```

As far as packets entering your system, this makes for quite a strong system. However, packets can still freely leave your computer without being checked. While this is normally not as dangerous as packets entering your system, some consideration should be made for packets leaving your computer.

### Blocking outgoing traffic

To drop packets that leave your computer, rules are established using the `OUTPUT` chain instead of the `INPUT` chain. Establishing rules for packets leaving your computer can help to prevent the effects that a virus can have on a network. This can be seen by going back to the example of the Code Red virus. If there is a rule in your personal firewall to allow only outgoing HTTP connections to the Internet or your network's proxy, the spread of Code Red would by very marginal inside your network. Most of the damage that was caused by Code Red was simply that of slowing down the network by having the virus on a few computers attempt to infect a number of other servers. This can be prevented right at the workstation by using a strictly configured personal firewall. Using the simple rule shown here would prevent HTTP connections to any machine on the internal network.

```
iptables -I OUTPUT -p tcp -d 192.168.0.0/24
-destination-port 80 -j DROP
```

Because the default rule for packets leaving the system is to allow them to go through, the logic you use for your rules must be in reverse. This is why we are explicitly setting the type of packet leaving the system that we want to drop. This appears to break the rule of security established before, that only access that is needed should be granted. However, it is all right to work in reverse in this case because enumerating through all the rules that would be needed for outgoing packets would be a large task. Also, outgoing packets usually do not have a negative effect on your computer, but rather on the network it is connected to.

In most situations, when dealing with outgoing traffic, only the proxy or Internet will ever need to be contacted. Usually very little peer-to-peer traffic is needed. Yet, if explicit rules are not set for packets leaving a system, the system's traffic, from viruses attempting to infect other computers for example, will still be allowed to clog the network. While these packets will not make it to their destination because of input rules on the personal firewall, the traffic will still be routed and cause congestion. Blocking packets from leaving one's system is all too often overlooked, and yet allowing the system to send packets to any host on the network can have an impact on the network as a whole.

### Logging blocked traffic

While we have seen a few ways to block packets from entering and exiting the system, almost all information is lost about these packets when they are dropped. Logging of information can play a major role in tracking down network problems and alerting administrators as to when a virus or other such malicious program infected the system. Proper logging and auditing can be almost as important as configuring the right rules to deny packets. There is a bit of logging that iptables does automatically for you. Iptables keeps a record of how many times a rule has affected a packet. This information is easy to retrieve by simply issuing the following command:

```
iptables -L -v
```

This tells iptables to list all of the rules and to be verbose when doing so. This will give an output that looks similar to the following:

```
Chain INPUT (policy DROP 129 packets, 20831 bytes)
 pkts bytes target  prot opt in  out source   destination
   25  2644 ACCEPT  udp  --  any any anywhere anywhere udp spt:domain
 523K  675M ACCEPT  tcp  --  any any anywhere anywhere tcp !SYN
    1    60 ACCEPT  tcp  --  any any anywhere anywhere tcp dpt:ssh

Chain OUTPUT (policy ACCEPT 372K packets, 25M bytes)
pkts bytes target  prot opt in  out source   destination

   5   300 DROP    tcp  --  any any anywhere 192.168.1.0/24 tcp dpt:http
```

The number of packets affected by a given rule is shown in the first column next to the rule. The number of bytes is also shown. There is also a total count for that chain, given in the parentheses. These numbers can help to provide a quick approximation of what's happening on your system, and what the rules are protecting you from.

To reset these numbers so that you can see what is happening at the current moment, the following commands are used:

```
iptables -Z INPUT
iptables -Z OUPUT
```

Once a chain has been reset, the information can then be listed again to see which rule is currently being used to stop packets, or which one is not doing what you need it to. During the midst of an attack this can be a very helpful and fast way to see if your rule is protecting your computer as you think it should. It might be necessary to add new rules and then check their count to see if they are having the desired effect.

However, in most cases this type of logging simply is not enough. More information such as the IP address and port can be helpful in tracking down the malicious user or problem. To log information about a rule you can add another rule to the system that is exactly the same except it logs the packet instead of accepting or denying the packet. While at first it seems as though this method is tedious for logging packets because it requires making a separate rule that is exactly the same, it has the added benefit of allowing you to create any rule that is then only logged. To log a packet that arrives at your system bound for SSH connections, the following command would be issued:

```
iptables -I INPUT -p tcp -destination-port 22 -j LOG
```

Now, any time an SSH connection is established it will be logged by syslogd or a similar daemon. These messages can usually be found in `/var/log/messages`. However, there are often a lot of messages in `/var/log/messages`. To help track down the information logged by a particular rule, you can add your prefix to the rule. To add the prefix "`SSH"` to your rule, the following command can be issued:

```
iptables -I INPUT -p tcp -destination-port 22 -j LOG -log-prefix "SSH"
```

Now, whenever a message is written to the log it will have that prefix. You will notice a space was left after SSH; this is to allow a space in the log. Otherwise your prefix will be right next to your rule, making it harder to parse like this:

```
kernel: SSHIN=eth0 OUT= MAC=ff:ff:ff:ff:ff:ff...
```

instead of like this:

```
kernel: SSH IN=eth0 OUT= MAC=ff:ff:ff:ff:ff:ff...
```

You can also set the amount of information that is recorded by iptables when this logging happens. This is set by the following flags: `-log-tcp-options` and `--log-ip-options`. Having these turned on is normally a good idea because too much information can only be a problem if you do not have enough space to store the logs. However, not having enough information can leave you guessing as to why this rule was triggered by iptables.

The logging of information is often overlooked when setting up a personal firewall. While the information that is logged by iptables is not in as nice a format as something like snort or another sniffer might give you, it is usually enough to tell what's happening to your system with respect to network traffic. Logging is an invaluable security tool, but is only helpful if the logs are audited in a routine fashion. Simply waiting for something to happen that is noticeable is usually too late. Scanning logs with a Perl script, or even just eyeballing the log once a week, is usually enough to detect patterns of harmful behavior.

### Advanced blocking techniques

Iptables also allows you the ability to block traffic based on burst rates and other matching criteria. This can be extremely helpful for both incoming and outgoing traffic. For example, you might want to allow traffic to be sent from peer to peer, but not want a single machine to be able to swamp the network with traffic. To accomplish this, match the limit of the traffic that is sent out of the computer. These limits, and the configuration for them, are outlined nicely in the manual page for iptables.

Another matching feature of iptables allows you to drop packets based on the size of the packet; matching may also be based on connections (when compiled into the kernel). These matching criteria can get very elaborate. However, they can also be very helpful in shaping the traffic entering or leaving a computer. For more details on all the matching criteria enabled by iptables, see the manual pages.

Personal firewalls come pre-installed on most systems today, but are vastly underutilized. All too often dedicated border firewalls are expected to protect internal machines from attack. However, all too often the attack originates inside of the network, and border firewalls do nothing to prevent this type of network congestion. Also, while most people think of a personal firewall as a last line of defense for a computer connected to the Internet, the firewall can often be used as the first step in protecting a network from unnecessary congestion. Limiting the hosts a computer is allowed to talk to by setting up rules in a personal firewall for outgoing packets can help prevent the spread of viruses. Personal firewalls should not be thought of as either the first or the last line of defense in securing a computer, but rather as just another piece in the puzzle to help secure a host.

# Summary

UNIX is a very powerful operating system that can be either very secure or very vulnerable, depending on how it is configured and operated. Some factors that make UNIX a good operating system for security are as follows:

- The source code for the operating system is available for scrutiny and analysis. This can lead to fewer vulnerabilities in the operating system and applications running in UNIX. In the case of some open source operating systems, such as Linux, the user community can fix flaws in the code and recompile or rebuild the system.
- The flexibility and configurability of UNIX support the administrators' need to harden the workstation against attack.
- UNIX operators tend to be more experienced and technical and, therefore, should be less vulnerable to attack.

Following are some reasons why UNIX can be more vulnerable as an operating system:

- Hackers are able to study the source code for the operating system and most applications and find flaws in the code. The hackers can thereby focus their efforts and potentially produce more exploits.
- Most servers on the Internet are running UNIX of one form or another. This makes it a favorite target for hackers.
- Many hacking tools have been developed on UNIX, so these tools are more likely to work against UNIX workstations from day one.
