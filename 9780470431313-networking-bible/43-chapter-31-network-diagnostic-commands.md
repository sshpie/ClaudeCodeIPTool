# Chapter 31. Network Diagnostic Commands

**IN THIS CHAPTER**

- Command line interface network management
- How network commands isolate faults
- Command shells
- Telnet, NetShell, and PowerShell

This chapter focuses on the various command line tools for diagnosing network problems, determining network conditions, and modifying different network parameters. These tools allow you to sequentially test individual network components, continually narrowing down the range of potential problems until the malfunctioning part or system is located.

Command shells have been a part of computer technology since time immemorial. They remain popular with users and network administrators alike, as they allow for both powerful network command and control, as well as a lightweight environment in which testing may be done. The various command shells or command line interfaces (CLIs) used for network management are described. Many of these shells are not only single command line processors but can also run small programs or scripts. As an example of the use of the CLI in testing and isolating faults, the use of `PING` and `IPCONFIG` to test a broken Internet connection is described.

This chapter presents a collection of network-related commands for the most widely used shells in Linux, Windows, and UNIX, as well as their description and syntax. The syntax shown is a sample that varies slightly, depending upon the platform involved.

Windows NetShell's NET commands have been used since Windows NT to manage network elements. At the NETSH command line, you can manage services, change device settings, configure and attach to network resources, and gain access to Windows Management Instrumentation (WMI) objects over the network. Microsoft introduced a more powerful command line environment called PowerShell with Windows Server 2008/Vista that performs these functions and more. PowerShell is described in some detail.

# Network Diagnostics

Network problems can be difficult to isolate and often require knowledge of a number of specialized tools. As network operating systems have matured and embraced a wide range of technologies, vendors have incorporated many network tools into their products. Many of these tools are command line utilities, often with powerful capabilities, while still other tools are expressed as functionality within the graphical interface of the operating system or inside a graphical utility. This chapter describes a range of network tools that you can use to diagnose problems and solve them, as well as different approaches you can use in this endeavor. Many of these tools have been presented to you in previous chapters, but in this chapter, many more new tools are described which should help give you some context of how and when to apply a specific tool.

The best approach to network diagnostic problem solving is a methodical one:

1. Document the problem requiring a solution.
2. Collect any required information regarding systems and connections involved.
3. Select the correct diagnostic tool or tools, and examine their results.
4. Continually narrow the scope of the problem.
5. Segment, isolate, and test potential faults using a process of testing, substitution, and/or swapping.
6. Confirm your hypothesis by demonstrating the removal of the fault.

# Network Commands

Commands entered at the command line provide a powerful method for determining the status of a network, modifying conditions, and performing many other tasks. In the sections that follow, the various CLIs or shells found in Linux, Windows, and UNIX are briefly described and the important network-oriented commands are listed.

## Command line tools

The command shell or command line interpreter is a text-based interface to a program that takes user input and translates it into commands that the operating system can act on. Different command line tools use different programming languages, and those differences, combined with differences in the way that vendors implement network operating systems, means that there is considerable variation in the syntax of network commands and the manner in which options are implemented. CLIs have been on computers since the early 1960s, and the minimal requirements of this environment, speed of command entry, and low overhead have ensured that every network operating system, or NOS, available today ships with a native CLI. Many third-party CLIs are available, and most of them are available cross-platform. Network CLI utilities form a major portion of the available command set for most systems, and this section highlights some of the more important utilities.

### Note

As a general rule, working with a CLI offers a knowledgeable person more control and power over their computer environment than a GUI utility; however, it is much harder to master. I recommend that you concentrate on the purpose of the utilities and use the help within the CLI or online help to find the information you need for a specific task. Different operating systems and shells use different methods for displaying help. Among the more common methods are entering the command itself, using the `/?` switch, and entering MAN <utilityname>. Googling a command usually takes you to detailed information on the command.

Command shell programs include:

- **CMD.COM**. This utility is responsible for the command prompt in Windows 7, Vista, Windows Server, Windows CE, and OS/2.
- **SH, BASH, CSH, and KSH**. These UNIX shells stand for the Bourne Shell (SH), Bourne Again Shell (BASH), C Shell (CSH), and Korn Shell (KSH). Depending upon your version of UNIX or Linux, different shells can be the default, and the system may run more than one shell. Less commonly encountered UNIX shells include the Almquist Shell (ASH) and its Debian counterpart (DASH), TENEX C Shell (TCSH), ES Shell, Easy Shell (ESH), Friendly Interactive Shell (FISH), RC Shell, Scheme Shell (SCSH), Stand-alone Shell (SASH), Windows SSH (or Secure Shell), and Z Shell (ZSH).
- **TCLSH and WISH**. These are shells used with the Tcl scripting language.
- **EFI**. The Extensible Firmware Interface (EFI) Shell runs as the BIOS replacement for modern processors.
- **Windows Script Host (WSH)**. This is used on Windows to automate different Active Scripting language routines based on JScript, VBScript, PerlScript, and others (it is extensible). It is an automation technology that provides an enhanced version of batch programming capabilities. Common uses of WSH are for logon scripts, system configuration, and network management.
- **PowerShell**. This Windows scripting language is implemented as a command line shell for Windows 7, Vista, Server 2008/2003, and XP (SP2/SP3). PowerShell uses the .NET Framework to run scripts that perform administrative tasks.
- **REXX**. IBM's scripting language shell.
- **PHPsh**. A shell for the PHP language.
- **Python**. The Python interpreter can be opened in a CLI.
- **JavaScript and BeanShell**. JavaScript is an interactive interface to the JavaScript scripting language; BeanShell is a shell for Java itself. Several different versions of JavaScript exist.

### Note

You can find a comparison table for command shells at `http://en.wikipedia.org/wiki/Comparison_of_computer_shells`.

There are many more CLI shells, but the previous list compiles the ones with the most extensive networking capabilities.

The following utilities are part of the TCP/IP command suite: `ARP, FINGER, FTP, HOSTNAME, IPCONFIG/IFCONFIG, LPQ, LPR, NBTSTAT, NETSTAT, NSLOOKUP, PING, RCP, REXEC, ROUTE, RSH, TFTP`, and `TRACERT`. They have been covered in detail in previous chapters.

### Note

Many of the TCP and IP commands are covered in [Chapters 17](ch17.html) and [18](ch18.html), respectively.

Let's consider one set of commonly encountered problems for which the command line utilities are particularly convenient and powerful: a browser that does not connect to the Internet. To fix a broken Internet connection, you might do the following:

1. Open a second browser and verify that the first browser isn't the reason that Internet data can't be browsed.
2. Open a command prompt and enter **PING** `WWW.YAHOO.COM`.A successful `PING` indicates that you have a working Internet connection and that you can resolve DNS names to IP addresses. The problem is probably related to the browser in question. Yahoo was selected as an example because it is a site that is almost always available, and one that hasn't turned its `PING` response off. Any other similar site will do.
3. At the command prompt, enter **PING 69.147.76.15** (This is the IP Address for `www.yahoo.com`).A successful `PING` indicates that you have a working Internet connection, but that you couldn't resolve external DNS queries. To fix this problem, you would check your DNS references, and if you were running a DNS server, you would check the DNS server.
4. At the command prompt, enter **PING** <Gateway IP address>.The Gateway address to use is the one entered into the network interface used for the Internet connection. If the `PING` isn't successful, you should check the conditions of the gateway (or firewall) as well as any cables leading to the gateway.
5. At the command prompt, enter **PING** <Network Node Name>.The node can be any network system or router that allows you to trace the route back from the gateway to your host. The command `PING` *<Network Node Address>* can also be used to check systems and DNS settings. If you have eliminated any connection errors leading up to your system, then the last set of settings to check is the local host itself.
6. At the command prompt, enter IPCONFIG (on Windows or Macintosh) or IFCONFIG (on UNIX or Linux).If the address settings are incorrect, then change them; if there is no assigned dynamic IP address, refresh your DHCP settings or check the status of your DHCP server. Use `IPCONFIG/RELEASE` and `IPCONFIG/RENEW` for this purpose. (Different platforms use slightly different switches.)

`PING` always returns one of these responses:

- **Normal response**. The host is alive within the Time-to-Live parameter (usually 1 to 10 hops).
- **Destination does not respond**. No answer was returned.
- **Unknown host**. The host is unknown and cannot be reached.
- **Destination unreachable**. The target is known but the default gateway cannot reach the target.
- **Network or host unreachable**. There is no entry in the route table for the host or network.

Steps 1 to 6 illustrate the practice of continually narrowing the scope of your troubleshooting and thus are theoretically considered best practice. In the real world, however, a problem with the local host is a more likely event than other steps on the list, and so I tend to try an `IPCONFIG/IFCONFIG` early in the process. [Figure 31.1](ch31.html#a_sample_session_attempting_to_diagnose) shows a sequence similar to the one described.

![A sample session attempting to diagnose a network connection for browser connectivity](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3101.png)

**Figure 31.1. A sample session attempting to diagnose a network connection for browser connectivity**

Let's assume that you performed all of the steps above and that your network interface is up, all of your intermediate nodes respond to `PING`s, and you can resolve DNS queries to get a named Internet site to respond to a `PING`. All parts of your Internet connection are functioning, but your browser still doesn't operate correctly, and information isn't displaying correctly. The next steps that you need to take check for other aspects of connectivity. Examine the response times to see if they are reasonable. Usually, long response times are associated with a certain number of "did not respond" responses. You may want to use the `TRACEROUTE` command to check the path used to destination sites, as well as the performance of each hop on the route.

The next step in checking connectivity is to determine if the particular protocol you are using can be sent and received. A `PING` traverses the same port that your browser's HTTP traffic does, the well-known port 80, or if your firewall supports it, a port that maps to port 80. Microsoft ISA Server, for example, uses port 8080 for HTTP traffic by default. You should check your firewall settings — both your network firewall and any local firewall — to determine that HTTP traffic is allowed, and, more importantly, that this particular browser is an approved application to use the HTTP port.

In [Table 31.1](ch31.html#command_line_commands_for_networking), various CLI networking commands for Linux (L), Windows (W), and UNIX (U) are highlighted. Although syntax for these commands is listed in [Table 31.1](ch31.html#command_line_commands_for_networking), the syntax varies depending upon which shell you are using, and in the case of Windows, which particular version of that operating system you are using. The syntax shown for Windows is based on `CMD.COM` for Windows XP. You should check your current platform's documentation to obtain the correct syntax and to get an explanation of the various options and switches.

**Table 31.1. Command Line Commands for Networking**

| Command | Platform | Description | Syntax |
| --- | --- | --- | --- |
| Legend: W = Windows, Italic text indicates variable data, bold text indicates required text that must be entered, items inside brackets ([]) are optional, and those between braces ({}) are a set of choices from which only one may be used. For more details about the individual elements of these commands, refer to the source shown above. |  |  |  |
| Source: `http://technet.microsoft.com/en-us/library/bb490864.aspx`. |  |  |  |
| `AC` | L/U | Print user connect time statistics. | `AC` [ **-d** \| *--daily-totals* ] [ **-y** \| *--print-year* ] [**-p** \| *--individual-totals* ] [ *people* ] [ **-f** \| *--file filename* ] [ **-a** \| *--all-days* ] [ *--complain* ] [ **--reboots** ] [ **--supplants** ] [ **--timewarps** ] [ **--compatibility** ] [ **--tw-leniency num** ] [ **--tw-suspicious num** ] [ **-z** \| *--print-zeros* ] [ **--debug** ] [ **-V** \| *--version* ] [ **-h** \| *--help* ] |
| `ARP` | L/U/W | Displays and modifies entries in the Address Resolution Protocol (ARP) cache, which contains one or more tables that are used to store IP addresses and their resolved Ethernet or Token Ring physical addresses. There is a separate table for each Ethernet or Token Ring network adapter installed on your computer. | `ARP` [-**a** [*InetAddr*] [-**N** *IfaceAddr*]] [-**g**[*InetAddr*] [-**N** *IfaceAddr*]] [-**d** InetAddr [IfaceAddr]] [-**s** *InetAddr* EtherAddr [*IfaceAddr*]] |
| `ATMADM` | W | Monitors connections and addresses that are registered by the ATM Call Manager on an asynchronous transfer mode (ATM) network. You can use `atmadm` to display statistics for incoming and outgoing calls on ATM adapters. Used without parameters, `atmadm` displays statistics for monitoring the status of active ATM connections. | `ATMADM` [/**c**][/**a**] [/**s]** |
| `BASH` | L/U | Starts the BASH Shell. | `BASH`[*options*] |
| `CHDIR (CD)` | L/W/U | Displays the name of the current directory or changes the current folder. Used with only a drive letter (for example, `CHDIR` C:), `chdir` displays the names of the current drive and folder. Used without parameters, `chdir` displays the current drive and directory. | `CHDIR` [[/**d]** [*Drive*:][*Path*] [..]] [[/**d**] [*Drive*:][*Path*] [..]] `CD` [[/**d]** [*Drive*:][*Path*] [..]] [[/**d**] [*Drive*:][*Path*] [..]] |
| `CHKDSK` | W | Creates and displays a status report for the disk. The `CHKDSK` command also lists and corrects errors on the disk. The `CHKDSK` command with the parameters listed below is only available when you are using the Recovery Console. The `CHKDSK` command with different parameters is available from the command prompt. | `CHKDSK` [*drive*:] [/**p**] [/**r]** |
| `CMSTP` | W | Installs or removes a Connection Manager service profile. Used without optional parameters, `CMSTP` installs a service profile with default settings appropriate to the operating system and to the user's permissions. | *ServiceProfileFileName*.**exe /q**:**a /c**:"**cmstp.exe** *ServiceProfileFileName*.**inf** [/nf] **[/ni**] **[/ns**] [**/s**] **[/su**] [**/u]**" **cmstp.exe** [**/nf**] [**/ni**] [**/ns**] [**/s**] [**/su**] [**/u**] "[*Drive*:][*Path*]*ServiceProfileFileName*.**inf**" |
| `COMP` | W | Compares the contents of two files or sets of files byte by byte. `COMP` can compare files on the same drive or on different drives, and in the same directory or in different directories. When `COMP` compares the files, it displays their locations and filenames. Used without parameters, `COMP` prompts you to enter the files to compare. | `COMP` [*data1*] [*data2*] [**/d**] [**/a**] [**/l**] [**/n**=*number*] [**/c**] |
| `COMPACT` | W | Displays and alters the compression of files or directories on NTFS partitions. Used without parameters, `COMPACT` displays the compression state of the current directory. | `COMPACT`[{/**c\|/u**}] [**/s**[:*dir*]] [**/a**] [**/i**] [**/f**] [**/q**] [*FileName*[...]] |
| `COMPRESS` | L/U | Compresses a file and adds the `.Z` extension. | `COMPRESS`[**-c**][**-f**][**-v**] *filenames* |
| `COPY (CP)` | L/W/U | Copies one or more files from one location to another. | `COPY` [**/d**] [**/v**] [**/n**] [{**/y\|/-y**}] [**/z**] [{/**a\|/b**}] *Source* [{/**a\|/b**}] [**+** *Source* [{**/a\|/b**}] [**+** ...]] [*Destination* [{**/a\|/b**}]] |
| `CRONTAB` | L/U | Creates and lists files that run on a schedule. | `CRONTAB`[**-e**] [**-l**] [**-r**] [*filename*] |
| `CSH` | L/U | Starts the C Shell. | `CSH`[**-b**] [**-c**] [**-e**] [**-f**] [**-i**] [**-n**] [**-s**] [**-t**] [**-v**] [**-V**] [**-x**] [**-X**] [*scriptname*]] |
| `DHCLIENT` | L/U | The Dynamic Host Configuration Protocol Client automatically assigns IP addressing to a DHCP client | `DHCLIENT` [ **-p** *port* ] [ **-d** ] [ **-e** *VAR=value* ] [ **-q** ] [ **-1** ] [ **-r** ] [ **-lf** *lease-file* ] [ **-pf** *pid-file* ] [ **-cf** *config-file* ] [ **-sf** *script-file* ] [ **-e** *ENVVAR=value* ] [**-s** *server* ] [ **-g** *relay* ] [ **-n** ] [ **-nw** ] [ **-w** ] [**if0** [ ...**ifN** ] ] |
| `DIG` | L/U | The DNS lookup utility automatically converts friendly names to IP addresses. | `DIG` [*@server*] [**-b** *address*] [**-c** *class*] [**-f** *filename*] [**-k** *filename*] [**-p** *port#*] [**-t** *type*] [**-x** *addr*] [**-y** *name:key*] [**-4**] [**-6**] [**name**] [**type**] [**class**] [**queryopt**...] |
| `DIRCMP` | L/W/U | Compares files in two directories and indicates whether they are identical or not. | `DIRCMP` [**-d**] [**-s**] [**-w** *n*] *directoryone directorytwo* |
| `DISKCOPY` | W | Copies the contents of the floppy disk in the source drive to a formatted or unformatted floppy disk in the destination drive. Used without parameters, `DISKCOPY` uses the current drive for the source disk and the destination disk. | `DISKCOPY` [*drive1*: [*drive2*:]] [**/v**] |
| `EXPAND` | L/W/U | Expands one or more compressed files. This command is used to retrieve compressed files from distribution disks. | `EXPAND` [**-r**] *Source* [*Destination*] `EXPAND` **-d** *source*.*cab* [**-f**:*files*] `EXPAND` *source*.*cab* **-f**:*files Destination* |
| `FINGER` | L/W/U | Displays information about a user or users on a specified remote computer (typically a computer running UNIX) that is running the Finger service or daemon. The remote computer specifies the format and output of the user information display. Used without parameters, `FINGER` displays help. | `FINGER` [**-l**] [*User*] [*@host*] [...] |
| `FTP` | L/W/U | Transfers files to and from a computer running a File Transfer Protocol (FTP) service such as Internet Information Services. `FTP` can be used interactively or in batch mode by processing ASCII text files. | `FTP` [**-v**] [**-d**] [**-i**] [**-n**] [**-g**] [**-s**:*FileName*] [**-a**] [**-w**:*WindowSize*] [**-A**] [*Host*] |
| `GETFACL` | L/U | Shows file attributes. | `GETFACL`[**-a**] [**-d**] *file* |
| `GETMAC` | W | Returns the Media Access Control (MAC) address and list of network protocols associated with each address for all network cards in each computer, either locally or across a network. | `GETMAC`[**.exe**] [**/s** *Computer*[**/u** *Domain\User* [**/p** *Password*]]] [**/fo** {**TABLE**\|**LIST**\|**CSV**}] [**/nh**] [**/v**] |
| `GPRESULT` | W | Displays Group Policy settings and Resultant Set of Policy (RSOP) for a user or a computer. | `GPRESULT` [**/s** *Computer* [**/u** *Domain\User* **/p** *Password*]] [**/user***TargetUserName*] [**/scope** {**user\|computer**}] [**/v**] [**/z**] |
| `HOST` | L/U | The DNS lookup utility converts friendly names to IP addresses. | `HOST` [**-a***CdlnrTwv*] [**-c** *class*] [**-N** *ndots*] [**-R** *number*] [**-t** *type*] [**-W** *wait*] [**-4**] [**-6**] {*name*} [*-**] |
| `HOSTNAME` | L/W/U | Displays the host name portion of the full computer name of the computer. | `HOSTNAME` |
| `IPCONFIG` | W | Displays all current TCP/IP network configuration values and refreshes Dynamic Host Configuration Protocol (DHCP) and Domain Name System (DNS) settings. Used without parameters, `IPCONFIG` displays the IP address, subnet mask, and default gateway for all adapters. | `IPCONFIG` [**/all**] [**/renew** [*Adapter*]] [**/release** [*Adapter*]] [**/flushdns**] [**/displaydns**] [**/registerdns**] [**/showclassid** *Adapter*] [**/setclassid** *Adapter* [*ClassID*]] |
| `IFCONFIG` | L/U | *An identical command to* `IPCONFIG`*on Windows with platform-specific parameters*. | `IFCONFIG` [**-L**] [**-m**] **interface** [*create*] [*address_family*] [**address**[/*prefixlength*] [*dest_address*]] [*parameters*] `IFCONFIG` **interface** *destroy* `IFCONFIG` **-a** [**-L**] [**-d**] [**-m**] [**-u**] [*address_family*] `IFCONFIG` **-l** [**-d**] [**-u**] [*address_family*] `IFCONFIG` [**-L**] [**-d**] [**-m**] [**-u**] [**-C**] |
| `IFUP / IFDOWN` | L/U | Closes or opens a network interface. | `IFUP` [**-nv**] [**--no-act**] [**--verbose**] [**-i FILE**\|*--interfaces=FILE*] [**--allow CLASS**] **-a**\|**IFACE**... `IFDOWN` [**-nv**] [**--no-act**] [**--verbose**] [**-i FILE**\|*--interfaces=FILE*] [**--allow** *CLASS*] **-a**\|*IFACE*... |
| `IPSECCMD` | W | Configures Internet Protocol Security (IPSec) policies in a directory service or in a local or remote registry. `IPSECCMD` is a command line alternative to the IP Security Policies Microsoft Management Console (MMC) snap-in. `IPSECCMD` has three modes: dynamic mode, static mode, and query mode. | To add a rule: `IPSECCMD` [\\*ComputerName*] **-f** *FilterList* [**-n** *NegotiationPolicyList*] [**-t** *TunnelAddr*] [**-a** *AuthMethodList*] [**-1s** *SecurityMethodList*] [**-1k** *MainModeRekeySettings*] [**-1p**] [**-1f** *MMFilterList*] [**-1e** *SoftSAExpirationTime*] [**-soft**] [**-confirm**] [{**-dialup** \| **-lan**}] To delete all dynamic policies: `IPSECCMD` **-u** |
| `IPXROUTE` | W | Displays and modifies information about the routing tables used by the IPX protocol. Used without parameters, `IPXROUTE` displays the default settings for packets that are sent to unknown, broadcast, and multicast addresses. | `IPXROUTE` **servers** [**/type**=*x*] `IPXROUTE` **ripout** *network* `IPXROUTE` **resolve** {**guid** \| **name**} {*guid* \| *AdapterName*} `IPXROUTE` **board**= *n* [**def**] [**gbr**] [**mbr**] [**remove**=*xxxxxxxxxxxx*] `IPXROUTE` **config** |
| `IRFTP` | W | Sends files over an infrared link. Used without parameters or used with **/s**, `IRFTP` opens the Wireless Link dialog box, where you can select the files that you want to send without using the command line. | `IRFTP` [*Drive*:**\**] [[*Path*] *FileName*] [**/h**] `IRFTP` **/s** |
| `KSH` | L/U | Starts the Korn Shell. | `KSH`[**-a**] [**-b**] [**-C**] [**-e**] [**-f**] [**-h**] [**-i**] [**-k**] [**-m**] [**-n**] [**-o**] [**-p**] [**-s**] [**-t**] [**-u**] [**-v**] [**-x**] [**+ o** *option* ] [**+A** *name*] [ *arg* ] |
| `LODCTR` | W | Registers new Performance counter names and Explain text for a service or device driver, and saves and restores counter settings and Explain text. | `LODCTR` [*\\ComputerName] FileName* [**/s**:*FileName*] [**/r**:*FileName*] |
| `LOGMAN` | W | Manages and schedules performance counter and event trace log collections on local and remote systems. | `LOGMAN` [**create** {*counter \| trace*} *collection_name* ] [**start** *collection_name*] [**stop** *collection_name*] [**delete** *collection_name]* [**query** {*collection_name*\|**providers**}] [**update** *collection_name*] |
| `LPQ` | L/U/W | Displays the status of a print queue on a computer running Line Printer Daemon (LPD). Used without parameters, `LPQ` displays command line help for the `LPQ` command. | `LPQ` **–S** *ServerName* **-P** *PrinterName* [**-l**] |
| `LPR` | L/U/W | Sends a file to a computer running Line Printer Daemon (LPD) in preparation for printing. Used without parameters, `LPR` displays command line help for the `LPR` command. | `LPR` [**-S** *ServerID*] **-P** *PrinterName* [**-C** *BannerContent*] [**-J** *JobName*] [{**-o \| -o l**}] [**-d**] [**-x**] *FileName* |
| `MII-TOOL` | L/U | A utility that views or sets the network interface Media Independent Interface (MII) unit. Fast 433333 Ethernet adapters use this function to negotiate link parameters. | `MII-TOOL` [**-v**, *--verbose*] [**-V**, *--version*] [**-R**, *--reset*] [**-r**, *--restart*] [**-w**, *--watch*] [**-l**, *--log*] [**-A**, *--advertise=media*,...] [**-F**, *--force=media*] [*interface* ...] |
| `MKDIR` | L/W/U | Creates a directory or subdirectory. | `MKDIR` [*Drive*:]*Path* `MD` [*Drive*:]*Path* |
| `MOUNT` / `UMOUNT` | L//U | Mounts or unmounts file systems and remote system resources. | `MOUNT` [**-p** \|**-v** ] `MOUNT` [**-F** *FSType* ] [ *generic_options* ] [**-o** *specific_options* ] [ **-O** ] **special** \| *mount_point* `MOUNT` [ **-F** *FSType* ] [ *generic_options* ] [**-o** *specific_options* ] [**-O** ] **special mount_point** `MOUNT` **-a** [**-F** *FSType* ] [ **-V** ] [ *current_options* ] [**-o** *specific_options* ] [ *mount_point* ... ] `UMOUNT` [ -V ] [ -o specific_options ] special \|mount_point `UMOUNT` -a [ -V ] [ -o specific_options ] [ mount_point... ] |
| `MOUNTVOL` | W | Creates, deletes, or lists a volume mount point. `MOUNTVOL` is a way to link volumes without requiring a drive letter. | `MOUNTVOL` [*Drive*:]*Path VolumeName* `MOUNTVOL` [*Drive*:]*Path* **/d** `MOUNTVOL` [*Drive*:]*Path* **/L** `MOUNTVOL` *Drive*: **/s** |
| `MOVE (MV)` | L/W/U | Moves one or more files from one directory to the specified directory. | `MOVE` [{**/y\|/-y**}] [*source*] [*target*]`mv` [**-f**] [**-i**] [*source* ] [*target* ] |
| `NBTSTAT` | W | Displays NetBIOS over TCP/IP (NetBT) protocol statistics, NetBIOS name tables for both the local computer and remote computers, and the NetBIOS name cache. `NBTSTAT` allows a refresh of the NetBIOS name cache and the names registered with Windows Internet Name Service (WINS). Used without parameters, `NBTSTAT` displays help. | `NBTSTAT` [**-a** *RemoteName*] [**-A** *IPAddress*] [**-c**] [**-n**] [**-r**] [**-R**] [**-RR**] [**-s**] [**-S**] [*Interval*] |
| `NETSTAT` | L/W/U | Displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols). Used without parameters, `NETSTAT` displays active TCP connections. | `NETSTAT` [**-a**] [**-e**] [**-n**] [**-o**] [**-p** *Protocol*] [**-r**] [**-s**] [*Interval*] |
| `NSLOOKUP` | L/W/U | Displays information that you can use to diagnose Domain Name System (DNS) infrastructure. Before using this tool, you should be familiar with how DNS works. The `NSLOOKUP` command line tool is available only if you have installed the TCP/IP protocol. | `NSLOOKUP` [*-SubCommand* ...] [{*ComputerToFind*\| [*-Server*]}] Subcommands: `EXIT, FINGER, HELP, LS, LSERVER, ROOT, SERVER, SET, SET ALL, SET CLASS, SET D2, SET DEBUG, SET DEFNAME, SET DOMAIN, SET IGNORE, SET PORT, SET QUERYTYPE, SET RECURSIVE, SET RETRY, SET ROOT, SET SEARCH, SET SRCHLIST, SET TIMEOUT, SET TYPE, SET VC`, and `VIEW` |
| `PATHPING` | W | Provides information about network latency and network loss at intermediate hops between a source and destination. `PATHPING` sends multiple Echo Request messages to each router between a source and destination over a period of time, and then computes results based on the packets returned from each router. Because `PATHPING` displays the degree of packet loss at any given router or link, you can determine which routers or subnets might be having network problems. `PATHPING` performs the equivalent of the `TRACERT` command by identifying which routers are on the path. It then sends pings periodically to all of the routers over a specified time period and computes statistics based on the number returned from each. | `PATHPING` [**-n**] [**-h** *MaximumHops*] [**-g** *HostList*] [**-p** *Period*] [**-q** *NumQueries* [**-w***Timeout*] [**-T**] [**-R**] [*TargetName*] |
| `PERFMON` | W | Allows you to open a Windows Performance console. | `PERFMON`**.exe** [*file_name*] [**/HTMLFILE**:*converted_file settings_file*] |
| `PING` | L/W/U | Verifies IP-level connectivity to another TCP/IP computer by sending Internet Control Message Protocol (ICMP) Echo Request messages. The receipt of corresponding Echo Reply messages is displayed, along with round-trip times. `PING` is the primary TCP/IP command used to troubleshoot connectivity, reachability, and name resolution. | `PING` [**-t**] [**-a**] [**-n** *Count*] [**-l** *Size*] [**-f**] [**-i** *TTL*] [**-v** *TOS*] [**-r** *Count*] [**-s** *Count*] [{**-j** *HostList* \| **-k** *HostList*}] [**-w** *Timeout*] [*TargetName*] |
| `PRINT` | W | Sends a text file to a printer. | `PRINT` [**/d**:*Printer*] [*Drive*:][*Path*] *FileName* [ ...] |
| `RASDIAL` | W | You can automate the connection process for any Microsoft client by using a simple batch file and the `RASDIAL` command. The `RASDIAL` command starts a network connection by using a specified entry. | `RASDIAL` *connectionname* [username [password \| *]] [/domain:domain] [/phone:phonenumber] [/callback:callbacknumber] [/phonebook:phonebookpath] [/prefixsuffix] The `RASDIAL` command disconnects a network connection by using the following syntax: `RASDIAL` [connectionname] /disconnect |
| `RCP` | L/U/W | Copies files between a Windows XP computer and a system running `RSHD`, the remote shell service (daemon). Windows XP and Windows 2000 do not provide `RSHD` service. | `RCP` [{**-a** \| **-b**}] [**-h**] [**-r**] [*host*][*.user*:] [*Source*] [*Host*][*.User*:] [*Path\Destination*] |
| `RELOG` | W | Extracts performance counters from performance counter logs into other formats, such as text-TSV (for tab-delimited text), text-CSV (for comma-delimited text), binary-BIN, or SQL. | `RELOG` [*FileName* [*filename* ...]] [**-a**] [**-c** *Path* [*path* ...]] [**-cf** *FileName*] [**-f** {**bin\|csv\|tsv\|SQL**}] [**-t** *value*] [**-o** {*output file \| DSN!counter_log*}] [**-b** *M/d/yyyy [[hh:]mm:]ss*] [**-e** *M/d/yyyy [[hh:]mm:]ss*] [**-config** *FileName*] [**-q**] |
| `RENAME`(`REN`) | W | Changes the name of a file or a set of files. | `RENAME` [*Drive*:][*Path*] *filename1 filename2* `REN` [*Drive*:][*Path*] *filename1 filename2* |
| `REMSH (rsh)` | L/U/W | The remote shell command allows you to run a command on a different system. | `REMSH`[*options*] [ **-l** *username* ] *hostname* [*#port*] *command* |
| `REPLACE` | W | Replaces files in the destination directory with files in the source directory that have the same name. You can also use `REPLACE` to add unique filenames to the destination directory. | `REPLACE` [*drive1:*][*path1*] *FileName* [*drive2*:][*path2*] [**/a**] [**/p**] [**/r**] [**/w**] `REPLACE` [*drive1*:][*path1*] *FileName*[*drive2*:][*path2*] [**/p**] [**/r**] [**/s**] [**/w**] [**/u**] |
| `REXEC` | L/U/W | Runs commands on remote computers running the `REXEC` service (daemon). The `REXEC` command authenticates the username on the remote computer before executing the specified command. Windows XP and Windows 2000 do not provide the `REXEC` service. | `REXEC` [*Host*] [**-l** *UserName*] [**-n**] [*Command*] |
| `RMDIR (RD)` | L/U/W | Removes (or deletes) a directory. | `RMDIR` [*Drive*:]*Path* **[/s**] **[/q**] `RD` [*Drive*:]*Path* [**/s**] [**/q**] |
| `ROUTE` | W | Displays and modifies the entries in the local IP routing table. | `ROUTE` [**-f**] [**-p**] [*Command* [*Destination*] [**mask** *Netmask*] [*Gateway*] [**metric** *Metric*]] [**if** *Interface*]] |
| `RSH` | W | Runs commands on remote computers running the `RSH` service or daemon. Windows XP and Windows 2000 do not provide an `RSH` service. | `RSH` [*Host*] [**-l** *UserName*] [**-n**] [*Command*] |
| `SH` | L/U | Runs jobs through the Bourne Shell. | `SH` [**-a**] [**-c**] [**-C**] [**-e**] [**-E**] [**-f**] [**-h**] [**-i**] [**-I**][**-k**] [**-m**] [**-n**] [**-p**] [**-r**] [**-s**] [**-t**] [**-T**] [**-u**] [**-v**] [**-x**] [ *argument* ] |
| `SHUTDOWN` | L/U/W | Allows you to shut down or restart a local or remote computer. Used without parameters, `SHUTDOWN` will logoff the current user. | `SHUTDOWN`[{**-l\|-s\|-r\|-a**}] [**-f**] [**-m** [*\\ComputerName*]] [**-t xx**] [**-c "***message***"**] [**-d**[**u**][**p**]*:xx:yy*] |
| `SUBST` | W | Associates a path with a drive letter. Used without parameters, `SUBST` displays the names of the virtual drives that your system knows about. | `SUBST` [*drive1*: [*drive2*:]*Path*] `SUBST` *drive1*: **/d** |
| `TASKKILL` | W | Ends one or more tasks or processes on a local (default) or remote system. Processes can be killed by process ID or image name. | `TASKKILL` [**/s** *Computer*] [**/u** *Domain\User* [**/p** *Password*]]] [**/fi** *FilterName*] [**/pid** *ProcessID*]\|[**/im** *ImageName*] [**/f**][**/t**] |
| `TASKLIST` | W | Displays a list of applications and services with their Process ID (PID) for all tasks running on either a local or a remote computer. | `TASKLIST` [**.exe**] [**/s** *computer*] [**/u** *domain\user* [*/p password*]] [**/fo** {**TABLE\|LIST\|CSV**}] [**/nh**] [/**fi** *FilterName* [**/fi** *FilterName2* [ ... ]]] [**/m** [*ModuleName*] \| **/svc** \| **/v**] |
| `TCMSETUP` | W | Sets up or disables the TAPI client. | `TCMSETUP` [**/q**] [**/x**] **/c** *Server1*[*Server2*...] `TCMSETUP` [**/q**] **/c /d** |
| `TELNET` | L/W/U | The `TELNET` commands allow you to communicate with a remote computer that is using the Telnet protocol. You can run `TELNET` without parameters in order to enter the Telnet context, indicated by the `TELNET` prompt (`TELNET`>). From the `TELNET` prompt, use the following commands to manage a computer running Telnet Client: `CLOSE, DISPLAY, ENTER, OPEN, QUIT, SET, STATIS`. `UNSET`, and `?/HELP` with their appropriate parameters. | `TELNET` [\\*RemoteServer*] Telnet Sessions are discussed later in this chapter. |
| `TFTP` | L/U/W | Transfers files to and from a remote computer, typically a computer running UNIX, that is running the Trivial File Transfer Protocol (TFTP) service or daemon. | `TFTP` [**-i**] [**Host**] [{**get** \| **put**}] [*Source*] [*Destination*] |
| `TRACERPT` | W | Processes event trace logs or real-time data from instrumented event trace providers and allows you to generate trace analysis reports and CSV (comma-delimited) files for the events generated. | `TRACERPT` [*FileName* [*filename*...]] [**-o** [*FileName*]] [**-report** [*FileName*]] [**-rt** *session_name*[*session_name* ...]] [**-summary** [*FileName*]] [**-config** [*FileName*] |
| `TRACERT` | W | Determines the path taken to a destination by sending Internet Control Message Protocol (ICMP) Echo Request messages to the destination with incrementally increasing Time-to-Live (TTL) field values. The path displayed is the list of near-side router interfaces of the routers in the path between a source host and a destination. The near-side interface is the interface of the router that is closest to the sending host in the path. | `TRACERT` [**-d**] [**-h***MaximumHops*] [**-j** *HostList*] [**-w** *Timeout*] [*TargetName*] |
| `TRACEROUTE` | L/U | An identical command to `TRACERT` on Windows with platform-specific parameters. | `TRACEROUTE` [**-d**] [**-F**] [**-I**] [**-n**] [**-v**] [**-x**] [**-f** *first_ttl*] [**-g** *gateway* [**-g** *gateway*] \| **-r**] [**-i** *iface*] [**-m** *max_ttl*] [**-p** *port*] [**-q** *nqueries*] [**-s** *src_addr*] [**-t tos**] [**-w** *waittime* ] **host** [*packetlen*] |
| `TREE` | W | Graphically displays the directory structure of a path or of the disk in a drive. | `TREE` [*Drive*:][*Path*] [**/f**] [**/a**] |
| `TYPEPERF` | W | Writes performance counter data to the command window, or to a supported log file format. To stop `TYPEPERF`, press Ctrl+C. | `TYPEPERF` [*Path* [*path* ...]] [**-cf** *FileName*] [**-f** {*csv\|tsv\|bin*}] [**-si** *interval]* [**-o** *FileName*] [**-q** [*object*]] [**-qx** [*object*]] [**-sc** *samples*] [**-config** *FileName*] [**-s** *computer_name*] |
| `UNLODCTR` | W | Removes Performance counter names and Explain text for a service or device driver from the system registry. | `UNLODCTR` [\\*ComputerName*] *DriverName* |
| `W32TM` | W | A tool used to diagnose problems occurring with Windows Time. | `W32TM` {/**config [/computer**:*ComputerName*] [ [**/update**] [**/manualpeerlist**:*ListOfComputerNames]* ] [**/syncfromflags**:*ListOfFlags*] ]\|**/monitor**\|/**ntte**\|**/ntpte**\|**/register**\|**/resync** [{*:ComputerName*] [**/nowait**]\|[**/rediscover**}]\|**/tz**\|**/unregister**} |
| `W` | L/U | Shows the current users and tasks. | `W` [**-husfVo**] [*user*] |
| `WHOIS` | L/W/U | Displays the Internet username directory service. | `WHOIS` [ **-h** *host* ] *identifier* |
| `XINIT` | L/U | Starts the X window system. The `STARTX` script is used as the interface for `XINIT` | `X`[*options*] |
| `XCOPY` | W | Copies files and directories, including subdirectories. | `XCOPY` *Source* [*Destination*] [**/w**] [**/p**] [**/c**] [**/v**] [**/q**] [**/f**] [**/l**] [**/g**] [**/d**[:*mm-dd-yyyy*]] [**/u**] [**/i**] [**/s** [**/e**]] [**/t**] [**/k**] [**/r**] [**/h**] [{**/a\|/m**}] [**/n**] [**/o**] [**/x**] [**/exclude**:*file1*[+[*file2*]][+[*file3*]] [{**/y\|/-y**}] [**/z**] |

`IPCONFIG` and its Linux/UNIX equivalent `IFCONFIG` may be the most useful TCP/IP commands in your arsenal. In addition to displaying the state of a network interface, `IPCONFIG` also allows you to change a static IP address, as well as release and renew any dynamic IP address.

# Network Shells

Network shells are command line interfaces that support network management tools, particularly for remote administration. Consoles that are network shells exist on all platforms and are supported by local processes installed either by the operating system or by management software. A network shell has the following two requirements:

- An agent, daemon, or process must exist on the remote system that can accept a command, usually in the form of a remote process call (RPC) command.
- A client utility or shell is required that can format and send a command to the remote process.

Network shells for Windows include the NetShell environment that ships with all versions of Windows, as well as PowerShell, an administration command/scripting environment that shipped with Windows Server 2008/Vista. PowerShell is meant to replace NetShell and other Windows CLI scripting tools. The sections that follow briefly look at some of these environments.

## The Windows NetShell

Windows NT introduced a command line tool for network administrators called NetShell. Using the NetShell CLI, you can carry out batch commands and scripts, or enter single commands from a central console that modifies the settings and actions of remote systems. The NetShell API, which is part of the Microsoft Windows Software Development Kit (SDK), allows developers to create helper DLLs (Dynamic Link Libraries) that implement the various NetShell commands in their programs.

A NetShell command operates in a particular context, which is scoped for a certain area of networking capabilities. For example, NetShell commands operating through a helper DLL can link to a dynamic library that controls a certain networking function and modify that function. The example usually cited is modification of the Dynamic Host Configuration Protocol (DHCP) where NetShell commands are directed to the `DHCPCSVC.DLL` dynamic link library that releases, renews, or refreshes dynamic addresses.

When NetShell loads, it proceeds to read the Windows Registry to obtain a list of helper DLLs, many of which ship with Windows and to which additional extensions can be added. Microsoft publishes the list of helpers in their various Resource Kits.

The main benefit that the NetShell commands offer to the average Windows user or administrator is that you can enter the NetShell Shell environment and enter commands at that command line. To enter the NetShell root context, you would do the following:

1. In Windows, enter **CMD** in the Start menu Run dialog box, and then press Enter.
2. At the `C:\` prompt, enter **NETSH** and press Enter.You see the `NETSH>` prompt appear, indicating that you are in the NetShell root context. The `EXIT` and `BYE` commands allow you to leave the NetShell environment.

There are so many uses of the NET Commands that the entire chapter could be used to illustrate their versatility. You can simulate most of the functions of Windows Explorer from within the NetShell, as the following examples demonstrate. [Figure 31.2](ch31.html#a_display_of_commands_available_in_the_r) shows a Command Prompt session in Vista where you enter the NetShell and display the various commands that NetShell's root context offers. Other contexts available are `ADVFIREWALL, BRIDGE, DHCPCLIENT, FIREWALL, HTTP, INTERFACE, IPSEC, LAN, NAP, NETIO, P2P, RAS, RPC, WINHTTP`, and `WLAN`. If you had opened this session on a Windows Server, you would see NetShell contexts associated with server functions. [Table 31.2](ch31.html#netshell_commands) lists some of the more common `NETSH` commands.

**Table 31.2. NetShell Commands**

| Command | Context | Description |
| --- | --- | --- |
| Source: Microsoft Technet (`technet.mircrosoft.com/en-us/library`). |  |  |
| `..` | Global | Moves up one level |
| `?` or `HELP` | Global | Displays command-specific help. |
| `AAAA` | Global | Enter the `AAAA` context. |
| `AAAA ADD/DELETE/SET/SHOW ACCTSERVER` | RAS | Configures or displays RADIUS accounting servers. |
| `AAAA ADD/DELETE/SET/SHOW AUTHSERVER` | RAS | Configures or displays RADIUS authentication servers. |
| `AAAA SET/SHOW ACCOUNTING` | RAS | Configures or displays the accounting provider. |
| `AAAA SET/SHOW AUTHENTICATION` | RAS | Configures or displays the authentication provider. |
| `ADD ALIAS` | Global | Adds an alias to a command. |
| `ADD HELPER` | Global | Adds a Netsh helper DLL. |
| `ADD/DELETE/SHOW AUTHTYPE` | RAS | Configures or displays the permitted authentication types. |
| `ADD/DELETE/SHOW AUTHTYPE` | RAS | Configures or displays the permitted authentication types. |
| `ADD/DELETE/SHOW CLIENT` | RAS | Configures or displays currently connected remote access clients. |
| `ADD/DELETE/SHOW CLIENT` | RAS | Configures or displays currently connected remote access clients. |
| `ADD/DELETE/SHOW LINK` | RAS | Configures or displays the configuration of software compression and link control protocol (LCP) extensions. |
| `ADD/DELETE/SHOW MULTILINK` | RAS | Configures or displays Multilink and Bandwidth Allocation Protocol (BAP) settings. |
| `ADD/DELETE/SHOW REGISTEREDSERVER` | RAS | Configures or displays whether the specified remote access server computer is a member of the RAS and IAS Servers security group in the Active Directory directory service of the specified domain. |
| `ADD/DELETE/SHOW REGISTEREDSERVER` | RAS | Configures or displays whether the specified remote access server computer is a member of the RAS and IAS Servers security group in the Active Directory directory service of the specified domain. |
| `APPLETALK SET ACCESS` | RAS | Configures whether AppleTalk traffic from remote access clients is forwarded to the networks to which the remote access server is connected. |
| `APPLETALK SET NEGOTIATION` | RAS | Configures whether AppleTalk is negotiated for remote access connections. |
| `APPLETALK SHOW CONFIG` | RAS | Displays AppleTalk remote access configuration. |
| `CMD` | Global | Opens a command window. |
| `COMMIT` | Global | Commits changes made in offline mode. |
| `DELETE ALIAS` | Global | Deletes an alias from a command. |
| `DELETE HELPER` | Global | Removes a `NETSH` helper DLL. |
| `DHCP` | Global | Enters the `DHCP` context. |
| `DUMP` | Global | Writes configuration to a text file. |
| `EXEC` | Global | Executes a script file which contains `NETSH` commands. |
| `FLUSH` | Global | Discards changes in offline mode. |
| `INTERFACE` | Global | Enter the `INTERFACE` context. |
| `INTERFACE IP` | Global | Enter the `INTERFACE IP` context. |
| `INTERFACE IPV6` | Global | Enter the `INTERFACE IPV6` context. |
| `INTERFACE PORTPROXY` | Global | Enter the inte`r` face `PORTPROXY` context. |
| `INTERNET PROTOCOL SECURITY` | Global | Enter the `IPSEC` context. |
| `IP ADD/DELETE RANGE` | RAS | Adds or removes a range of addresses from the static IP address pool. |
| `IP ADD/DELETE/SET/SHOW FILTER` | Routing | Adds, deletes, configures, or displays IP packet filters on a specified interface. |
| `IP ADD/DELETE/SET/SHOW INTERFACE` | Routing | Adds, deletes, configures, or displays general IP routing settings on a specified interface. |
| `IP ADD/DELETE/SET/SHOW PERSISTENTROUTE` | Routing | Adds, deletes, configures, or displays persistent routes. |
| `IP ADD/DELETE/SET/SHOW PREFERENCEFORPROTOCOL` | Routing | Adds, deletes, configures, or displays the preference level for a routing protocol. |
| `IP ADD/DELETE/SET/SHOW RTMROUTE` | Routing | Adds, deletes, configures, or displays a non-persistent Route Table Manager route. |
| `IP ADD/DELETE/SET/SHOW SCOPE` | Routing | Adds, deletes, or displays a multicast scope. |
| `IP ADD/DELETE/SHOW BOUNDARY` | Routing | Adds, deletes, or displays multicast boundary settings on a specified interface. |
| `IP AUTODHCP ADD/DELETE EXCLUSION` | Routing | Adds or deletes an exclusion from the DHCP allocator range of addresses. |
| `IP AUTODHCP SET/SHOW GLOBAL` | Routing | Configures or displays global DHCP allocator parameters. |
| `IP AUTODHCP SET/SHOW INTERFACE` | Routing | Configures or displays DHCP allocator settings for a specified interface. |
| `IP DELETE POOL` | RAS | Deletes the static IP address pool. |
| `IP DNSPROXY SET/SHOW GLOBAL` | Routing | Configures or displays global DNS proxy parameters. |
| `IP DNSPROXY SET/SHOW INTERFACE` | Routing | Configures or displays DNS proxy parameters for a specified interface. |
| `IP IGMP ADD/DELETE/SET/SHOW INTERFACE` | Routing | Adds, deletes, configures, or displays IGMP on the specified interface. |
| `IP IGMP SET/SHOW GLOBAL` | Routing | Configures or displays IGMP global settings. |
| `IP IGMP SHOW GROUPTABLE` | Routing | Displays the IGMP host groups table. |
| `IP IGMP SHOW IFSTATS` | Routing | Displays the IGMP statistics for each interface. |
| `IP IGMP SHOW IFTABLE` | Routing | Displays the IGMP host groups for each interface. |
| `IP IGMP SHOW PROXYGROUPTABLE` | Routing | Displays the IGMP group table for the IGMP proxy interface. |
| `IP IGMP SHOW RASGROUPTABLE` | Routing | Displays the group table for internal interface used by the remote access server. |
| `IP NAT ADD/DELETE ADDRESSMAPPING` | Routing | Adds or deletes a NAT address mapping. |
| `IP NAT ADD/DELETE ADDRESSRANGE` | Routing | Adds or deletes an address range to the NAT interface public address pool. |
| `IP NAT ADD/DELETE PORTMAPPING` | Routing | Adds or deletes a NAT port mapping. |
| `IP NAT ADD/DELETE/SET/SHOW INTERFACE` | Routing | Adds, deletes, configures, or displays network address translation (NAT) settings for a specified interface. |
| `IP NAT SET/SHOW GLOBAL` | Routing | Configures or displays global network address translation (NAT) settings. |
| `IP OSPF ADD/DELETE/SET/SHOW AREA` | Routing | Adds, removes, configures, or displays an OSPF area. |
| `IP OSPF ADD/DELETE/SET/SHOW INTERFACE` | Routing | Adds, removes, configures, or displays OSPF on a specified interface. |
| `IP OSPF ADD/DELETE/SET/SHOW VIRTIF` | Routing | Adds, removes, configures, or displays an OSPF virtual interface. |
| `IP OSPF ADD/DELETE/SHOW NEIGHBOR` | Routing | Adds, removes, configures, or displays an OSPF neighbor. |
| `IP OSPF ADD/DELETE/SHOW PROTOFILTER` | Routing | Adds, removes, configures, or displays routing information sources for OSPF external routes. |
| `IP OSPF ADD/DELETE/SHOW ROUTEFILTER` | Routing | Adds, removes, configures, or displays route filtering for OSPF external routes. |
| `IP OSPF SET/SHOW GLOBAL` | Routing | Configures or displays global OSPF settings. This feature is not available on the Itanium-based versions of the Windows operating systems. This content is not available in this preliminary release. |
| `IP OSPF SHOW AREASTATS` | Routing | Displays OSPF area statistics. |
| `IP OSPF SHOW LSDB` | Routing | Displays the OSPF link state database. |
| `IP OSPF SHOW VIRTIFSTATS` | Routing | Displays OSPF virtual link statistics. |
| `IP RELAY ADD/DELETE DHCPSERVER` | Routing | Adds or removes a DHCP server IP address to the list of DHCP server addresses. |
| `IP RELAY ADD/DELETE/SET INTERFACE` | Routing | Adds, removes, or configures DHCP Relay Agent settings on a specified interface. |
| `IP RELAY SET GLOBAL` | Routing | Configures DHCP Relay Agent global settings. |
| `IP RELAY SHOW IFBINDING` | Routing | Displays IP address bindings for interfaces. |
| `IP RELAY SHOW IFCONFIG` | Routing | Displays DHCP Relay Agent configuration for each interface. |
| `IP RELAY SHOW IFSTATS` | Routing | Displays DHCP statistics for each interface. |
| `IP SET ACCESS` | RAS | Configures whether IP traffic from remote access clients is forwarded to the networks to which the remote access server is connected. |
| `IP SET ADDRASSIGN` | RAS | Configures the method by which the remote access server assigns IP addresses to incoming connections. |
| `IP SET ADDRREQ` | RAS | Configures whether remote access clients or demand-dial routers can request their own IP addresses. |
| `IP SET NEGOTIATION` | RAS | Configures whether IP is negotiated for remote access connections. |
| `IP SET/SHOW LOGLEVEL` | Routing | Configures or displays the global IP logging level. |
| `IP SHOW BOUNDARYSTATS` | Routing | Displays IP multicast boundaries. |
| `IP SHOW CONFIG` | RAS | Displays IP remote access configuration. |
| `IP SHOW HELPER` | Routing | Displays all Netsh utility subcontexts of IP. |
| `IP SHOW MFE` | Routing | Displays multicast forwarding entries. |
| `IP SHOW MFESTATS` | Routing | Displays multicast forwarding entry statistics. |
| `IP SHOW PROTOCOL` | Routing | Displays all running IP routing protocols. |
| `IP SHOW RTMDESTINATIONS` | Routing | Displays destinations in the Route Table Manager routing table. |
| `IP SHOW RTMROUTES` | Routing | Displays routes in the Route Table Manager routing table. |
| `NETWORK BRIDGE` | Global | Enter the `BRIDGE` context. |
| `NETWORK DIAGNOSTICS (DIAG)` | Global | Enter the `DIAG` context. |
| `OFFLINE` | Global | Sets the mode to offline. |
| `ONLINE` | Global | Sets the mode to online. |
| `POPD` | Global | Pops a context from the stack. The stack is a stored buffer of recent commands. |
| `PUSHD` | Global | Pushes the current context on the stack. |
| `QUIT OR BYE OR EXIT` | Global | Exits `NETSH`. |
| `RAS SET/SHOW AUTHMODE` | RAS | Configures or displays whether and when dial-in connections are authenticated. |
| `REMOTE ACCESS` | Global | Enter the `RAS` context. |
| `ROUTING` | Global | Enter the `ROUTING` context. |
| `RPC HELPER` | Global | Enter the `RPC` context. |
| `SET AUDIT-LOGGING` | Global | Turns logging on or off. |
| `SET LOGLEVEL` | Global | Sets level of logging information. |
| `SET MACHINE` | Global | Sets the system to which NetShell commands are applied. |
| `SET MODE` | Global | Sets the mode to online or offline. |
| `SET/SHOW AUTHMODE` | RAS | Configures or displays whether and when dial-in connections are authenticated. |
| `SET/SHOW CREDENTIALS` | Interface | Configures or displays the user name, password, and domain name on a demand-dial interface. |
| `SET/SHOW INTERFACE` | Interface | Enables, disables, connects, disconnects, and displays the configuration of demand-dial interfaces. |
| `SET/SHOW TRACING` | RAS | Configures or displays tracing settings. |
| `SET/SHOW USER` | RAS | Configures or displays remote access settings for user accounts. |
| `SHOW ACTIVESERVERS` | RAS | Displays current servers running Routing and Remote Access on your network. |
| `SHOW ACTIVESERVERS` | RAS | Displays current servers running Routing and Remote Access on your network. |
| `SHOW ALIAS` | Global | Displays all defined aliases. |
| `SHOW AUDIT-LOGGING` | Global | Displays audit logging settings. |
| `SHOW HELPER` | Global | Displays the `NETSH` helper DLLs. |
| `SHOW LOGLEVEL` | Global | Displays the level of logging information. |
| `SHOW MACHINE` | Global | Displays the system to which NetShell commands are applied. |
| `SHOW MODE` | Global | Displays the current mode. |
| `SHOW NETDLLS` | Global | Displays version of the `NETSH` helper DLLs. |
| `SHOW VERSION` | Global | Displays the version of Windows and `NETSH` utility. |
| `WINS` | Global | Enters the `WINS` context. |

A very common use of NetShell is to start and stop network services. The command has the following syntax:

```
NET [START/STOP/PAUSE/CONTINUE] <ServiceName>
```

These commands duplicate the action of going into the Windows Services console and clicking the Start, Stop, Pause, and Continue buttons. If you have a service that you think might have hung up and may be malfunctioning, you can use the following sequence to restart that service.

- `NETSH>NET STOP DHCP`
- `NETSH>NET START DHCP`

![A display of commands available in the root context of NetShell](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3102.png)

**Figure 31.2. A display of commands available in the root context of NetShell**

NetShell allows for the following major classes of commands:

- `NET`, to manage network resources
- `MODE`, to configure a system device
- `SC`, to allow for service control
- `PsService`, to provide a means to view and control services
- `WMIC Service`, to allow a user to access WMI control over services

## Telnet sessions

Telnet stands for the Telecommunications Network protocol, one of the earliest of the Internet's standard protocols. With a Telnet client, you can use a CLI to perform commands on a remote system. Because of its long history, Telnet is supported natively on all network operating systems, and there are many third-party Telnet clients available. While Telnet has some limited popularity on UNIX systems, particularly with old timers, most modern courses on network administration tend to teach other methods for light-footprint, character-based command session systems.

Telnet is an 8-bit text transfer protocol where commands are carried as 7-bit ASCII with a single character of the upper ASCII character set referred to as a "Telnet character." TCP port number 23 is the well-known Telnet port. Although early versions of Telnet were not standardized, versions after 1973 tended to conform to what is called the "New Telnet" standard, which extends IETF RFC 15. The extensions used mean that Telnet is slightly different from one NOS to another.

While Telnet is convenient, easy to learn, and easy to use, the general consensus is that Telnet is insecure and that it should be deprecated. The reasons for this are evident:

- Telnet sessions send and receive clear text, not encrypted data, and are therefore subject to interception.
- Telnet daemons (processes) have been hacked into several times and have not been sufficiently strengthened.
- Telnet sessions do not provide a means to determine that the endpoints of a connection are authentic; the user simply provides a login that can be intercepted.

There have been sporadic attempts to add security to the Telnet protocol, but for the most part, SSH clients have turned out to be adequate for remote command line sessions and have replaced these clients. You may still encounter Telnet's use on mainframe and legacy systems, as an entry into routers and switches, and in some other specialized situations. The open source PuTTY (`www.chiark.greenend.org.uk/~sgtatham/putty/`) utility is a combination Telnet/SSH client that you can use for Windows and UNIX, and as an `XTERM` terminal emulator.

Starting with Windows Vista, Microsoft stopped installing the Telnet client as part of their standard installation; however, you can add the Vista Telnet client back into Vista as an add-on system component. You can find a listing of the various Telnet commands at `http://technet.microsoft.com/en-us/library/bb491013.aspx`.

## PowerShell

PowerShell is the latest expression of the command line interface introduced in Windows Server 2008/Vista (also available for Windows Server 2003/XP) for administration of systems. PowerShell unites a CLI with a standardized command language composed of over 60 verbs, and with the capability to run scripts. PowerShell was designed to be backwardly compatible with many older Microsoft technologies, as well as other common CLIs from other platforms. PowerShell commands can act on thousands of Windows, Office, .NET Framework objects, and the WMI objects, among others. PowerShell commands can act on both local and remote systems, registries, the Active Directory, and services. The intent at Microsoft is to rewrite the command consoles of their enterprise applications, with PowerShell as the underlying command structure. The latest version of Exchange was the first application to ship with a management console of this type.

Among the various features that you can control with PowerShell are:

- Local and remote system management
- System services, processes, and the Registry
- ActiveX Data Objects (ADOs), Component Object Model (COM) objects, and .NET Framework objects
- Active Directory Service Interface (ADSI) objects
- Windows Management Instrumentation (WMI) objects
- Terminal Server configuration and management
- Internet Information Services 7.0 configuration and management
- XML-based data or HTML files
- Scripts written in various scripting languages, or deployed with the Windows Scripting Host

Windows PowerShell is both a Windows shell and command interpreter environment with a built-in scripting language. The PowerShell runtime engine contains its own command parser as well as automation for binding command parameters. PowerShell 1.0 initially shipped with 129 built-in command utilities called CMDLETs (pronounced "command-lets") that can operate on objects, some of which can be used to format and display command results with the PowerShell CLI.

### Note

PowerShell's Web site is located at `www.microsoft.com/powershell`, along with information about the download of this command environment. Version 1.0 runs on Windows XP/Server 2003/Vista/Server 2008/7 and is available for x86, x86-64, and IA-64 (Itanium) systems. Version 2.0 is available in preview form and will be released soon after this book has shipped. Later versions of these operating systems have PowerShell as an optional Windows add-on in the standard operating system distribution.

To start PowerShell from the command prompt:

1. Click Start, click Run, and then enter **CMD** in the Run dialog box, or press the Windows logo+R keystroke.
2. Press the Enter key to open a command prompt.
3. Change directories to the one that contains the PowerShell program by entering **%SystemRoot%\System32\WindowsPowerShell\v1.0** and then pressing the Enter key.
4. Enter **PowerShell.exe -NoProfile** to start PowerShell without a profile file that is used to modify the program.

Alternatively, you can start PowerShell from the Start menu command, as follows: click Start, click All Programs, click Windows PowerShell 1.0, and then click Windows PowerShell to start the program.

When PowerShell runs, it loads the console and snap-ins (collections of `CMDLET`s and providers), and then profile files are processed. You can think of a profile as a script that customizes the PowerShell environment, adding aliases, changing the console configuration, and adding special functions. Profiles can apply to an administrator, all users, a single user, or a group of users. PowerShell has a feature called the "Execution Policy" that limits users from running scripts without certain safeguards.

PowerShell uses a collection of `CMDLET`s or providers that are snap-ins of related functionality. Each snap-in runs in its own namespace. For example, the Core snap-in's namespace is Microsoft.PowerShell.Core. Core `CMDLET`s alter the way the PowerShell engine operates. Other snap-ins are Host, Management, Security, and Utility snap-ins. To see which snap-ins are part of your installation, enter the following command:

```
GET-PSSNAPIN.
```

To determine which `CMDLET`s are in a snap-in, you can use the following command:

```
GET-COMMAND -COMMANDTYPE CMDLET | WHERE-OBJECT {$_.PSSNAPIN -MATCH "<snapin_name>"}
```

Or, to see which providers are included, use this command:

```
GET-PSPROVIDER | FORMAT-TABLE NAME, PSSNAPIN
```

[Table 31.3](ch31.html#powershell_1.0_cmdlets) lists some of the important PowerShell `CMDLET`s.

**Table 31.3. PowerShell 1.0 CMDLETS**

| Name | Definition | Description |
| --- | --- | --- |
| The ellipses in the table signify that you can add additional terms to the command identical to the one that is shown previous to the ellipses. |  |  |
| `ADD-CONTENT (AC)` | `ADD-CONTENT [-Path] <String[]> [-Value] <Object[...` | `Add content to an item` |
| `ADD-HISTORY` | `ADD-HISTORY [[-InputObject] <PSObject[]>] [-Pass...` | `Add entries to the session history.` |
| `ADD-MEMBER` | `ADD-MEMBER [-MemberType] <PSMemberTypes> [-Name]...` | `Add a member to a particular PowerShell object.` |
| `ADD-PSSNAPIN` | `ADD-PSSNAPIN [-Name] <String[]> [-PassThru] [-Ve...` | `Add a snap-in to the console.` |
| `CLEAR-CONTENT (CLC)` | `CLEAR-CONTENT [-Path] <String[]> [-Filter <Strin...` | `Remove the content from an item or specific location.` |
| `CLEAR-HOST (CLEAR/CLS)` | `Clear-Host or CLS` | `Clears the display.` |
| `CLEAR-ITEM (CLI)` | `CLEAR-ITEM [-Path] <String[]> [-Force] [-Filter ...` | `Remove the content from a variable or alias.` |
| `CLEAR-ITEMPROPERTY (CLP)` | `CLEAR-ITEMPROPERTY [-Path] <String[]> [-Name] <S...` | `Remove a property from an item.` |
| `CLEAR-VARIABLE (CLV)` | `CLEAR-VARIABLE [-Name] <String[]> [-Include <Str...` | `Clear a variable value.` |
| `COMPARE-OBJECT` | `COMPARE-OBJECT [-ReferenceObject] <PSObject[]> [...` | `Compare objects to one another.` |
| `CONVERTFROM-SECURESTRING` | `CONVERTFROM-SECURESTRING [-SecureString] <Secure...` | `Convert a secure string to an encrypted standard sting.` |
| `CONVERT-PATH (CVPA)` | `CONVERT-PATH [-Path] <String[]> [-Verbose] [-Deb...` | `Convert a PS path to a provider path.` |
| `CONVERTTO-HTML` | `CONVERTTO-HTML [[-Property] <Object[]>] [-InputO...` | `Convert the input into an HTML table` |
| `CONVERTTO-SECURESTRING` | `CONVERTTO-SECURESTRING [-String] <String> [[-Sec...` | `Convert an encrypted standard string into a secure string.` |
| `COPY-ITEM (COPY/CP/CPI))` | COPY-ITEM [-Path] <String[]> [[-Destination] <St... | `Copy an item from the location in the namespace.` |
| `COPY-ITEMPROPERTY (CPP)` | `COPY-ITEMPROPERTY [[-path]\| [-literalPath] ] string[]` `[[-destination] string[]]...` | `Copy a property along with its value.` |
| `DO` | `[:Loop_label] DO` `{` `command_block` `} while (condition)` | `Continue a loop while a condition is true.` |
| `COPY-ITEMPROPERTY` | `COPY-ITEMPROPERTY [-Path] <String[]> [-Destinati...` |  |
| `EXIT` |  | `Quit PowerShell or exit a script.` |
| `EXPORT-ALIAS` | `EXPORT-ALIAS [-Path] <String> [[-Name] <String[]...` | `Export an alias list to a file.` |
| `EXPORT-CLIXML` | `EXPORT-CLIXML [-Path] <String> [-Depth <Int32>] ...` | `Create a CLIXML listing of PowerShell objects.` |
| `EXPORT-CONSOLE` | `EXPORT-CONSOLE [[-Path] <String>] [-Force] [-NoC...` | `Export the console configuration to a file.` |
| `EXPORT-CSV (EPCSV)` | `EXPORT-CSV [-Path] <String> -InputObject <PSObje...` | `Export to Comma Delimited Values (a spreadsheet format).` |
| `FOR` | `FOR (init; condition; repeat) {command_block}` | `Loop through items that match a condition.` |
| `FOREACH (FOREACH)` | `FOREACH (item in collection) {ScriptBlock}` | `Loop for each value in the pipeline.` |
| `FOREACH-OBJECT` | `FOREACH-OBJECT [-Process] <ScriptBlock[]> [-Inpu...` | `Loop for each object in the PowerShell pipeline.` |
| `FORMAT-CUSTOM (FC)` | `FORMAT-CUSTOM [[-Property] <Object[]>] [-Depth <...` | `Create a custom format for output in a view.` |
| `FORMAT-LIST (FL)` | `FORMAT-LIST [[-Property] <Object[]>] [-GroupBy <...` | `Format the output of a view as a list of properties.` |
| `FORMAT-TABLE (FT)` | `FORMAT-TABLE [[-Property] <Object[]>] [-AutoSize...` | `Format the output as a table.` |
| `FORMAT-WIDE (FW)` | `FORMAT-WIDE [[-Property] <Object>] [-AutoSize] [...` | `Format the output as a table listing a single property.` |
| `GET-ACL` | `GET-ACL [[-Path] <String[]>] [-Audit] [-Filter <...` | `Get the permissions for a file or registry key.` |
| `GET-ALIAS (GAL)` | `GET-ALIAS [[-Name] <String[]>] [-Exclude <String...` | `Return the alias name for a Cmdlet.` |
| `GET-AUTHENTICODESIGNATURE` | `GET-AUTHENTICODESIGNATURE [-FilePath] <String[]>...` | `Get the signature object of a file.` |
| `GET-CHILDITEM (DIR/LS/GCI)` | `GET-CHILDITEM [[-Path] <String[]>] [[-Filter] <S...` | `Get the contents of a folder or registry key that pertains to a child item.` |
| `GET-COMMAND (GCM)` | `GET-COMMAND [[-ArgumentList] <Object[]>] [-Verb ...` | `Return command description.` |
| `GET-CONTENT (CAT/TYPE/GC)` | `GET-CONTENT [-Path] <String[]> [-ReadCount <Int6...` | `Get the content from an item or specific location.` |
| `GET-CREDENTIAL` | `GET-CREDENTIAL [-Credential] <PSCredential> [-Ve...` | `Get a security credential (username/password).` |
| `GET-CULTURE` | `GET-CULTURE [-Verbose] [-Debug] [-ErrorAction <A...` | `Get the regional information of the system.` |
| `GET-DATE` | `GET-DATE [[-Date] <DateTime>] [-Year <Int32>] [-...` | `Get the current date and time.` |
| `GET-EVENTLOG` | `GET-EVENTLOG [-LogName] <String> [-Newest <Int32...` | `Get the eventlog data.` |
| `GET-EXECUTIONPOLICY` | `GET-EXECUTIONPOLICY [-Verbose] [-Debug] [-ErrorA...` | `Get the execution policy for the shell.` |
| `GET-HELP (HELP)` | `GET-HELP [[-Name] <String>] [-Category <String[]...` | `Open the help file.` |
| `GET-HISTORY (HISTORY/H/GHY)` | `GET-HISTORY [[-Id] <Int64[]>] [[-Count] <Int32>]...` | `Get a listing of the sessions command history.` |
| `GET-HOST` | `GET-HOST [-Verbose] [-Debug] [-ErrorAction <Acti...` | `Get the host (system) information.` |
| `GET-ITEM (GI)` | `GET-ITEM [-Path] <String[]> [-Filter <String>] [...` | `Get a file or registry object, or another namespace object.` |
| `GET-ITEMPROPERTY (GP)` | `GET-ITEMPROPERTY [-Path] <String[]> [[-Name] <St...` | `Retrieves the properties of an object.` |
| `GET-LOCATION (PWD/GL)` | `GET-LOCATION [-PSProvider <String[]>] [-PSDrive ...` | `Get and display the current location.` |
| `GET-MEMBER (GM)` | `GET-MEMBER [[-Name] <String[]>] [-InputObject <P...` | `List the properties of an object.` |
| `GET-PFXCERTIFICATE` | `GET-PFXCERTIFICATE [-FilePath] <String[]> [-Verb...` | `Get pf certificate information.` |
| `GET-PROCESS (PS/GPS)` | `GET-PROCESS [[-Name] <String[]>] [-Verbose] [-De...` | `Get a list of running processes on a machine.` |
| `GET-PSDRIVE (GDR)` | `GET-PSDRIVE [[-Name] <String[]>] [-Scope <String...` | `Get the DriveInfo for a defined PSDrive.` |
| `GET-PSPROVIDER` | `GET-PSPROVIDER [[-PSProvider] <String[]>] [-Verb...` | `Ge information about the specified provider.` |
| `GET-PSSNAPIN` | `GET-PSSNAPIN [[-Name] <String[]>] [-Registered] ...` | `List the PowerShell snap-ins in use on the computer.` |
| `GET-SERVICE (GSV)` | `GET-SERVICE [[-Name] <String[]>] [-Include <Stri...` | `Get a list of services.` |
| `GET-TRACESOURCE` | `GET-TRACESOURCE [[-Name] <String[]>] [-Verbose] ...` | `Get components that are instrumented for tracing.` |
| `GET-UICULTURE` | `GET-UICULTURE [-Verbose] [-Debug] [-ErrorAction ...` | `Get the ui culture information.` |
| `GET-UNIQUE (GU)` | `GET-UNIQUE [-InputObject <PSObject>] [-AsString]...` | `Get the unique items in a collection.` |
| `GET-VARIABLE (GV)` | `GET-VARIABLE [[-Name] <String[]>] [-ValueOnly] [...` | `Get a PowerShell variable.` |
| `GET-WMIOBJECT (GWMI)` | `GET-WMIOBJECT [-Class] <String> [[-Property] <St...` |  |
| `GROUP-OBJECT (GROUP)` | `GROUP-OBJECT [[-Property] <Object[]>] [-NoElemen...` | `Group objects that contain the same value for a shared property.` |
| `IF` | `If (condition) {commands_to_execute}[ elseif (condition2) {commands_to_execute} ] else {commands_to_execute} ...` | `Perform a command based on the state of a condition.` |
| `IMPORT-ALIAS (IPAL)` | `IMPORT-ALIAS [-Path] <String> [-Scope <String>] ...` | `Import an alias from a file.` |
| `IMPORT-CLIXML` | `IMPORT-CLIXML [-Path] <String[]> [-Verbose] [-De...` | `Import a CLIXML file and use it to rebuild the PS object.` |
| `IMPORT-CSV (IPCSV)` | `IMPORT-CSV [-Path] <String[]> [-Verbose] [-Debug...` | `Get the values from a CSV file and send objects to the pipeline.` |
| `INVOKE-EXPRESSION` | `INVOKE-EXPRESSION [-Command] <String> [-Verbose]...` | `Run a PowerShell expression.` |
| `INVOKE-HISTORY(R/IHY)` | `INVOKE-HISTORY [[-Id] <String>] [-Verbose] [-Deb...` | `Invoke a previously run Cmdlet from history.` |
| `INVOKE-ITEM (II)` | `INVOKE-ITEM [-Path] <String[]> [-Filter <String>...` | `Invoke an executable file or open a file.` |
| `JOIN-PATH` | `JOIN-PATH [-Path] <String[]> [-ChildPath] <Strin...` | `Combine a path and child-path.` |
| `MEASURE-COMMAND` | `MEASURE-COMMAND [-Expression] <ScriptBlock> [-In...` | `Measure the running time of a Cmdlet.` |
| `MEASURE-OBJECT` | `MEASURE-OBJECT [[-Property] <String[]>] [-InputO...` | `Measure the properties of an object.` |
| `MOVE-ITEM (MOVE/MV/MI)` | `MOVE-ITEM [-Path] <String[]> [[-Destination] <St...` | `Move an item to a new location.` |
| `MOVE-ITEMPROPERTY (MP)` | `MOVE-ITEMPROPERTY [-Path] <String[]> [-Destinati...` | `Move a property from one location to another.` |
| `NEW-ALIAS (NAL)` | `NEW-ALIAS [-Name] <String> [-Value] <String> [-D...` | `Create an alias.` |
| `NEW-ITEM (NI)` | `NEW-ITEM [-Path] <String[]> [-ItemType <String>]...` | `Create a new item in a namespace.` |
| `NEW-ITEMPROPERTY` | `NEW-ITEMPROPERTY [-Path] <String[]> [-Name] <Str...` | `Set a new property of an item at a location.` |
| `NEW-OBJECT` | `NEW-OBJECT [-TypeName] <String> [[-ArgumentList]...` | `Create a new .NET object.` |
| `NEW-PSDRIVE (MOUNT/NDR)` | `NEW-PSDRIVE [-Name] <String> [-PSProvider] <Stri...` | `Create a new PSDrive.` |
| `NEW-SERVICE` | `NEW-SERVICE [-Name] <String> [-BinaryPathName] <...` | `Create a new service.` |
| `NEW-TIMESPAN` | `NEW-TIMESPAN [[-Start] <DateTime>] [[-End] <Date...` | `Create a timespan object.` |
| `NEW-VARIABLE (NV)` | `NEW-VARIABLE [-Name] <String> [[-Value] <Object>...` | `Create a new variable.` |
| `OUT-DEFAULT` | `OUT-DEFAULT [-InputObject <PSObject>] [-Verbose]...` | `Send output to default.` |
| `OUT-FILE` | `OUT-FILE [-FilePath] <String> [[-Encoding] <Stri...` | `Send command output to a file.` |
| `OUT-HOST (OH)` | `OUT-HOST [-Paging] [-InputObject <PSObject>] [-V...` | `Send the pipelined output to the host.` |
| `OUT-NULL` | `OUT-NULL [-InputObject <PSObject>] [-Verbose] [-...` | `Send output to null.` |
| `OUT-PRINTER (LP)` | `OUT-PRINTER [[-Name] <String>] [-InputObject <PS...` | `Send the output to a printer.` |
| `OUT-STRING` | `OUT-STRING [-Stream] [-Width <Int32>] [-InputObj...` | `Send objects to the host as strings.` |
| `POP-LOCATION (POPD)` | `POP-LOCATION [-PassThru] [-StackName <String>] [...` | `Set the current location from the stack.` |
| `POWERSHELL` | `PS` | `Launch a PowerShell session.` |
| `PUSH-LOCATION (PUSHD)` | `PUSH-LOCATION [[-Path] <String>] [-PassThru] [-S...` | `Push the current location onto the stack.` |
| `QUEST AD CMDLETS` |  | `Read/Write to the Active Directory.` |
| `READ-HOST` | `READ-HOST [[-Prompt] <Object>] [-AsSecureString]...` | `Read a line of input from the host console.` |
| `REMOVE-ITEM (RM/DEL/ERASE/RDRI/RMDIR)` | `REMOVE-ITEM [-Path] <String[]> [-Filter <String>...` | `Remove an item.` |
| `REMOVE-ITEMPROPERTY (RP)` | `REMOVE-ITEMPROPERTY [-Path] <String[]> [-Name] <...` | `Delete the property and its value from an item.` |
| `REMOVE-PSDRIVE (RDR)` | `REMOVE-PSDRIVE [-Name] <String[]> [-PSProvider <...` | `Delete a defined PSDrive.` |
| `REMOVE-PSSNAPIN` | `REMOVE-PSSNAPIN [-Name] <String[]> [-PassThru] [...` | `Remove a PowerShell shap-in from this computer.` |
| `REMOVE-VARIABLE (RV)` | `REMOVE-VARIABLE [-Name] <String[]> [-Include <St...` | `Remove a variable.` |
| `RENAME-ITEM (REN/RNI)` | `RENAME-ITEM [-Path] <String> [-NewName] <String>...` | `Remove an item.` |
| `RENAME-ITEMPROPERTY (RNP)` | `RENAME-ITEMPROPERTY [-Path] <String> [-Name] <St...` | `Rename the property of an item.` |
| `RESOLVE-PATH (RVPA)` | `RESOLVE-PATH [-Path] <String[]> [-Credential <PS...` | `Resolves the wildcards in a path.` |
| `RESTART-SERVICE` | `RESTART-SERVICE [-Name] <String[]> [-Force] [-Pa...` | `Stop and restart a service.` |
| `RESUME-SERVICE` | `RESUME-SERVICE [-Name] <String[]> [-PassThru] [-...` | `Resume a suspended service.` |
| `RUN/CALL (&)` | `& [Cmdlet]` | `Run a command (the call operator).` |
| `SELECT-OBJECT (SELECT)` | `SELECT-OBJECT [[-Property] <Object[]>] [-InputOb...` | `Select the properties of objects.` |
| `SELECT-STRING` | `SELECT-STRING [-Pattern] <String[]> -InputObject...` | `Search strings and files for matches to patterns.` |
| `SET-ACL` | `SET-ACL [-Path] <String[]> [-AclObject] <ObjectS...` | `Set permissions.` |
| `SET-ALIAS (SAL)` | `SET-ALIAS [-Name] <String> [-Value] <String> [-D...` | `Create or change an alias.` |
| `SET-AUTHENTICODESIGNATURE` | `SET-AUTHENTICODESIGNATURE [-FilePath] <String[]>...` | `Put a signature into a file or .ps1 script.` |
| `SET-CONTENT (SC)` | `SET-CONTENT [-Path] <String[]> [-Value] <Object[...` | `Sets the content from an item or specific location.` |
| `SET-DATE` | `SET-DATE [-Date] <DateTime> [-DisplayHint <Displ...` | `Set the current date and time for the system.` |
| `SET-EXECUTIONPOLICY` | `SET-EXECUTIONPOLICY [-ExecutionPolicy] <Executio...` | `Modify the execution policy for the shell based on user preferences.` |
| `SET-ITEM (SI)` | `SET-ITEM [-Path] <String[]> [[-Value] <Object>] ...` | `Change the value of an item.` |
| `SET-ITEMPROPERTY (SP)` | `SET-ITEMPROPERTY [-Path] <String[]> [-Name] <Str...` | `Set the value of a property.` |
| `SET-LOCATION (CD/CHDIR/SL)` | `SET-LOCATION [[-Path] <String>] [-PassThru] [-Ve...` | `Set the current working location.` |
| `SET-PSDEBUG` | `SET-PSDEBUG [-Trace <Int32>] [-Step] [-Strict] [...` | `Trun script debugging on or off.` |
| `SET-SERVICE` | `SET-SERVICE [-Name] <String> [-DisplayName <Stri...` | `Change the start mode or properties of a service.` |
| `SET-TRACESOURCE` | `SET-TRACESOURCE [-Name] <String[]> [[-Option] <P...` | `Trace a PowerShell component.` |
| `SET-VARIABLE (SET/SV)` | `SET-VARIABLE [-Name] <String[]> [[-Value] <Objec...` | `Sets or saves a value to a variable.` |
| `SORT-OBJECT (SORT)` | `SORT-OBJECT [[-Property] <Object[]>] [-Descendin...` | `Sort objects by property value.` |
| `SPLIT-PATH` | `SPLIT-PATH [-Path] <String[]> [-LiteralPath <Str...` | `Return part of a path.` |
| `START-SERVICE (STSV)` | `START-SERVICE [-Name] <String[]> [-PassThru] [-I...` | `Start a service.` |
| `START-SLEEP (SLEEP)` | `START-SLEEP [-Seconds] <Int32> [-Verbose] [-Debu...` | `Suspend shell, script, or runspace activity.` |
| `START-TRANSCRIPT` | `START-TRANSCRIPT [[-Path] <String>] [-Append] [-...` | `Start the transcript of a command shell session.` |
| `STOP-PROCESS (KILL/SPPS)` | `STOP-PROCESS [-Id] <Int32[]> [-PassThru] [-Verbo...` | `Stop a running process.` |
| `STOP-SERVICE (SPSV)` | `STOP-SERVICE [-Name] <String[]> [-Force] [-PassT...` | `Stop a service.` |
| `STOP-TRANSCRIPT` | `STOP-TRANSCRIPT [-Verbose] [-Debug] [-ErrorActio...` | `Stop the transcription process.` |
| `SWITCH` |  | `Multiple if statements.` |
| `SUSPEND-SERVICE` | `SUSPEND-SERVICE [-Name] <String[]> [-PassThru] [...` | `Suspend a running serivce.` |
| `TEE-OBJECT` | `TEE-OBJECT [-FilePath] <String> [-InputObject <P...` | `Send input objects to two places.` |
| `TEST-PATH` | `TEST-PATH [-Path] <String[]> [-Filter <String>] ...` | `Return a true if the path exists, else return false.` |
| `TRACE-COMMAND` | `TRACE-COMMAND [-Name] <String[]> [-Expression] <...` | `Trace a command or expression.` |
| `UPDATE-FORMATDATA` | `UPDATE-FORMATDATA [[-AppendPath] <String[]>] [-P...` | `Update and append format data files.` |
| `UPDATE-TYPEDATA` | `UPDATE-TYPEDATA [[-AppendPath] <String[]>] [-Pre...` | `Update the current extended type configuration.` |
| `WHERE-OBJECT (WHERE)` | `WHERE-OBJECT [-FilterScript] <ScriptBlock> [-Inp...` | `Filter objects that are passed to the pipeline.` |
| `WHILE` | `WHILE (condition) {command_block}` | `Loop when a condition is true.` |
| `WRITE-DEBUG` | `WRITE-DEBUG [-Message] <String> [-Verbose] [-Deb...` | `Write a debug message to the host display.` |
| `WRITE-ERROR` | `WRITE-ERROR [-Message] <String> [-Category <Erro...` | `Write an object to the error pipeline.` |
| `WRITE-HOST` | `WRITE-HOST [[-Object] <Object>] [-NoNewline] [-S...` | `Display objects using the host user interface.` |
| `WRITE-OUTPUT (ECHO)` | `WRITE-OUTPUT [-InputObject] <PSObject[]> [-Verbo...` | `Write an object to the pipeline.` |
| `WRITE-PROGRESS` | `WRITE-PROGRESS [-Activity] <String> [-Status] <S...` | `Display a progress bar.` |
| `WRITE-VERBOSE` | `WRITE-VERBOSE [-Message] <String> [-Verbose] [-D...` | `Write a sting to the host's verbose display.` |
| `WRITE-WARNING` | `WRITE-WARNING [-Message] <String> [-Verbose] [-D...` | `Write a warning message.` |
| `#` | `# <String>` | `Make a comment or leave a remark.` |

What you find is that nearly all providers are in the PowerShell Core, that the Certificate provider is part of the Security snap-in, and that additional providers are added by third parties to support management functions.

Many of PowerShell's commands allow for the optional use of various UNIX commands. For example, you can enter the command Get-Help, or alternatively use the alias MAN (for UNIX Manual pages) for the same command. There are numerous aliases built into the PowerShell CLI.

One of PowerShell's often used capabilities is the enumeration of services, as well as service management. You can see what services are running on a system by using the GET-SERV`I`CE command by itself, so that `START-SERVICE` <*servicename*> will start a service, and `STOP-SERVICE` <*servicename*> will stop that service. This capability is useful to examine a remote system using the following syntax (which is available in version 2.0 and later):

```
GET-SERVICE -COMPUTERNAME <systemname>
```

Similarly, you can use `GET-PROCESS` to display all running processes on your local system, or filter the list by using the `NAME <string>`. As you experiment with the `GET-PROCESS` command, you will find that you can expose many more parameters about processes than are found in the Task Manager. PowerShell gives you much finer control over services and processes, as well as access to remote systems for which you have access privileges. [Figure 31.3](ch31.html#the_get-process_pipe_more_command_lists) shows the `GET-PROCESS CMDLET` in action.

![The GET-PROCESS | MORE command lists all processes running on a system.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3103.png)

**Figure 31.3. The `GET-PROCESS | MORE` command lists all processes running on a system.**

You can navigate file systems in PowerShell in much the same manner that you navigate file systems in MS-DOS using the `SET-LOCATION` command. PowerShell creates an abstraction called a PowerShell Drive that provides access to a data store. PowerShell allows you to map the Registry as drives, as well as the Certificate store. The Registry maps to the HKCU: and HKLM: drives, which are the Hive Key Current User and Hive Key Local Machine, respectively. The Certificate store mounts as the CERT: drive. In this regard, PowerShell is unique. You can't access the Registry in either CMD.EXE or a program such as Windows Explorer, and this PowerShell cmdlet gives an administrator powerful access to system settings both on local and remote systems.

To see a complete list of all WMI objects, you can use the following command:

```
GET-WMIOBJECT -LIST
```

PowerShell will return 200 to 300 WMI providers. If you want to get information about a specific service, you can enter it by name. When you use the command GET-WMIOBJECT WIN32_PROCESS, you may be surprised by the depth of information that WMI provides. PowerShell maintains a help topic on WMIOBJECT that you can access by entering GET-HELP WMIOBJECT. If you enter the following command:

```
GET-WMIOBJECT WIN32_SERVICE -COMPUTERNAME <IP ADDRESS or systemname>
```

PowerShell will return the services running on the system whose IP address you specify.

A PowerShell script is a text file with the `.ps1` file extension. You execute a script by entering <path>\<scriptname.ps1> at the prompt. The path must be a fully qualified path, but the `.ps1` extension is optional.

In PowerShell, you must set an execution policy that allows a script to run. Scripts won't run unless you validate them, and you can use a digital signature as part of that validation. To learn more about digital signing, enter the command **GET-HELP ABOUT_SIGNING**.

PowerShell supports WSH scripts, and while both offer access to COM automation objects, PowerShell has the ability to provide an interactive command session.

Going forward, anyone interested in command line management of Windows networked systems should concentrate on learning and using PowerShell instead of the older tools such as the NET commands, Windows Scripting Host (WSH), and other technologies in this area.

# Summary

This chapter described command line tools for network management. Command shells or command line interpreters allow for network command and control as well as being a lightweight environment in which testing may be done. The various command shells or CLIs used for network management were described. Many of these shells are not only single command line processors but can also run small programs or scripts.

Shells used in Linux, Windows, and UNIX were described. Windows NetShell's NET commands and PowerShell were described in some detail.

In the next chapter, remote networking utilities are described.
