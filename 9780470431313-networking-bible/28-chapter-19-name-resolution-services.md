# Chapter 19. Name Resolution Services

**IN THIS CHAPTER**

- Why mapping is needed
- Using a HOSTS file on a local system
- Using WINS for NetBIOS name resolution
- DNS and its importance on the Internet
- Name resolution versus directory services

Nameservers are a collection of networking services that translate a machine or network address into a "friendly" or readable name. When you open a Network folder on your computer and browse the network, the name service polls the systems on the network for their availability and returns their names and related information. A name service is central to the successful operation of your network. Without a functioning nameserver, your network may only display your computer's information.

There are many different name services in use. The Internet relies on the Domain Name System (DNS) protocol to translate IP addresses, such as 170.149.173.130 into `nytimes.com`.

While DNS is the most widely used name service, there are many other name services that are in current use. This chapter describes the simplest method, and one of the earliest, for name resolution — the `HOSTS` file. With the `HOSTS` file, your system can perform a lookup on a listing of systems that are known, even if your automated name service fails.

Windows networks use the Windows Internet Name Service (WINS) to enumerate systems using the NetBIOS protocol. This system can provide high performance on Windows networks and is commonly used.

DNS can be set up to run on a LAN and provide a name service for systems in a workgroup or, more frequently, a domain. DNS uses resource records to point to resources and describe their properties. Queries against the underlying DNS database provide a means to find network resources.

Directory services extend the idea of name servers to store information on many other aspects of network objects. Most directory services are based on Lightweight Directory Access Protocol (LDAP), which is based on the even more complex X.500 Directory Service. LDAP is the basis for the directory services used by network operating systems.

# HOSTS Files

The first system that was used to perform name resolution on TCP/IP networks was the `HOSTS` file, and the first `HOSTS` file was stored on ARPAnet on a computer at Stanford Research Institute (SRI). The `HOSTS` file is a text file that lists the IP address in one column and the related friendly name of the host (computer system) in the second column. The system provides a lookup based on this simple database. The `HOSTS` file is largely of historical interest, but has some utility because it is searched in any name resolution before your DNS servers are queried. If an entry is found in the `HOSTS` file, then that entry is used as the definitive response for resolution.

Every computer operating system still creates a `HOSTS` file, and this file is checked during name resolution. Because the file must be manually maintained, most people tend to ignore it, relying on automated services such as DNS. In a network of any size, changing the entries in a `HOSTS` file on every computer is a daunting task. Even on a small network, if dynamic addressing is used for address assignment (as is the case for DHCP), then that severely limits the use of the `HOSTS` file. However, because the `HOSTS` file can be accessed by the local system administrator, there are still some uses for the `HOSTS` file that you might want to consider.

[Table 19.1](ch19.html#hosts_files-033) lists the location of the `HOSTS` file in various networked operating systems.

**Table 19.1. HOSTS Files**

| Operating System | Location | Notes |
| --- | --- | --- |
| Linux/UNIX | `/ETC/HOSTS` |  |
| Mac OS X | `/PRIVATE/ETC/HOSTS` |  |
| Mac OS 9 and earlier | `System Folder: Preferences` | In some versions, the `HOSTS` file is located in the System folder |
| OS/2 | `"Bootdrive":\MPTN\ETC\HOSTS` |  |
| Windows NT – Vista | `%SystemRoot%\SYSTEM32\DRIVERS\ETC\HOSTS` | The location of the file is controlled by the Registry key `\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\DataBasePath` |
| Windows ME/98/95 | `%WinDir%\HOSTS` |  |

You can view the current contents of your `HOSTS` file by opening the file in a text editor, terminal window, or command prompt.

In Windows, you can open and view the `HOSTS` file by doing the following:

1. Click Start![HOSTS Files](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U001.png)
2. Type **%SystemRoot%\SYSTEM32\DRIVERS\ETC\**, and then press Enter.
3. Double-click the `HOSTS` file icon in Windows Explorer. The Open With dialog box appears.
4. In the Open With dialog box, select Notepad as the application, and then click OK. [Figure 19.1](ch19.html#the_windows_vista_64_hosts_file_in_its_d) shows the `HOSTS` file in its default state.![The Windows Vista 64 HOSTS file in its default state](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1901.png)**Figure 19.1. The Windows Vista 64 HOSTS file in its default state**
5. Make any changes you require to the file.
6. Click File![The Windows Vista 64 HOSTS file in its default state](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U001.png)

If you recall from [Chapter 7](ch07.html), the addresses 127.0.0.1 and ::1 are reserved for the loopback adapter for IP version 4 and IP version 6, respectively. You add entries to the list by creating a new line, entering the address, and then adding one or more spaces followed by the system name. Here are some examples:

```
192.168.3.180 Maine # Carol's workstation
192.168.3.183 Duet # Allie's workstation
# This is a comment, both entries above are local systems
64.233.169.104 www.Google.com
...
```

You might initially want to add your common Web sites to your `HOSTS` files, and doing so will result in a small saving of time. However, the administrative overhead isn't worth the bother.

The `HOSTS` file is useful for blocking sites. If you want to block an outside system from getting a response from your system, you can assign that system to your loopback adapter. This technique can be applied to ad sites, spyware and malware locations, X-rated sites, and so on. For example, to block `GoogleAnalytics.com`, you would add the following line to your `HOSTS` file:

```
127.0.0.1 www.googleanalytics.com
```

The `HOSTS` file does not allow you to enter multiple sites by using wildcard symbols in the name or address, nor does it allow you to block individual directories. Only the top-level domain name is supported.

Alternatively, you can direct ad services such as `ad.Doubleclick.net` to an invalid IP address: 0.0.0.0 is a common choice, as it is the default assignment when a DHCP client fails to initialize properly and can't obtain a proper IP assignment. You can also assign the blocked site to an address that has no host on your internal network and reserve that address to always be unassigned. This type of blocking is actually a form of redirection. Redirection can be used to provide an alternative location for testing network software; however, malicious Web sites sometimes use this technique to hijack a computer.

You can imagine that a `HOSTS` file that blocks known bad sites would be a good idea, but that compiling the list of sites and maintaining that list would be a Herculean task. There are alternatives to this approach that you can try, and some work better than others. One approach is to download and use `HOSTS` files that are created by others, often communities of people who collaborate to create and maintain extensive `HOSTS` files.

I am not a big fan of using `HOSTS` files for anything other than enumerating local systems on my small network. Instead, I tend to rely on a collection of tools to block sites, including anti-virus and anti-spyware tools, and one tool in particular, SpywareBlaster from Javacool Software (see [Figure 19.2](ch19.html#spywareblaster_employs_a_blacklist_that)), which blocks sites using blacklists. SpywareBlaster is non-resident in memory and has a low overhead when Internet Explorer or Mozilla Firefox makes a name resolution request. Within Firefox, I install the Adblock Plus extension, which also uses a blacklist to block incoming ads; I also use the NoScript extension to defeat executing scripts.

Another layer of protection is to enable the trusted zones feature found in Web browsers. I don't tend to use this feature, but it is particularly valuable on corporate networks.

![SpywareBlaster employs a blacklist that you subscribe to in order to block unwanted Internet sites and content.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1902.png)

**Figure 19.2. SpywareBlaster employs a blacklist that you subscribe to in order to block unwanted Internet sites and content.**

# Address Resolution Protocol

The utility of the `HOSTS` file is limited by the requirement that it be manually updated. In order to automate the process of name resolution, the Address Resolution Protocol, or ARP, was developed. ARP creates a table of IP addresses and their associated physical addresses. An ARP table is dynamically maintained and then is stored in memory in an ARP cache. Dynamic entries in the ARP table are timed out, based on the ARP cache timeout setting, while static entries are maintained in the cache without timeout if the ARP cache table is operating correctly.

The ARP table consists of rows for each device that is registered:

- IP Address
- Physical Address
- IF Index (physical port or interface)
- Type of entry: 3 for dynamic; 4 for static; 2 for an invalid entry; and 1 for no assignment

ARP is encapsulated into the Data Link Layer Protocol, which means that ARP cannot be routed; it is useful for the local subnet only.

## ARP requests

When the ARP cache is queried, it performs a lookup for the IP address, and when it locates a match, it returns the physical address. If no match is found, then ARP sends out a broadcast message called an ARP request to all of the devices on the network. The ARP request contains the IP address, and when the correct device detects the request, it returns a response with its physical address. The ARP table is then updated to include this information.

The ARP request and response take the following forms:

- **Hardware Type:** 1 for Ethernet; 3 for X.25; 6 for IEEE 802.X; 18 for Fibre Channel; and so on.
- **Protocol Type:** 2048 for Internet Protocol (IP); 2053 for X.25 Level 3; 32823 for AppleTalk; and so on.
- **Hardware Address Length/Protocol Address Length:** Ethernet has a hardware value of 4 bytes; IP also has a protocol length of 4 bytes.
- **Operation Code:** The Operation Code, or Opcode, is 1 for an ARP request and 2 for an ARP reply.
- **Sender Hardware Address**
- **Sender IP Address**
- **Recipient Hardware Address**
- **Recipient IP Address**

Only the node in the network with the correct Recipient IP address can reply to an ARP request. When that node receives the request, it sequentially reads the information in the request to determine if it can reply using the hardware and protocols in the request and then sends a reply. Only the ARP cache tables that have an entry for the sender IP are updated by the new information from the reply. If an entry for this node already exists, then it is updated.

## Reverse Address Resolution Protocol

There are instances when a device doesn't have an IP address and can't create an ARP request or reply to one. This happens on a thin client device connecting to a terminal server where the processing is done on the server; when the client boots up, there is no assigned IP address. It can also happen when a system loses its DHCP lease. For these systems, the only address that the system has is the MAC address (or physical address) or the network interface card (NIC). To solve this problem, the Reverse Address Resolution Protocol (RARP) was developed.

A RARP request originates from a RARP client and broadcasts the physical address of the client to the RARP server. RARP requests and RARP replies have the same format that you saw for ARP. The difference between them is how the values in the different fields are entered.

Although RARP can be configured so that the reply must come from a RARP server with a particular IP address, most of the time the system accepts an answer from the first reply from any RARP server that can respond. The RARP reply is not a broadcast but is sent directly to the RARP client.

There are usually multiple RARP servers on a network because if the RARP server fails, RARP clients that start up will continue to broadcast RARP requests until a reply is received. If there are enough RARP clients sending out broadcasts, it can negatively impact network availability, a situation referred to as a *RARP storm*. A RARP failure renders a client inoperable as that client cannot start up.

RARP servers store a lookup table of IP addresses for specific nodes on the network. Each record in the table is keyed by a unique identifier specific to the RARP client. It is that unique identifier that must be sent to the RARP server to generate the RARP reply. Because a thin client cannot store an identifier (they can't be counted on to have storage), the protocol reads some other hardware-specific parameter.

## Viewing the ARP cache

Most versions of TCP/IP use the ARP command. This allows you to view the ARP cache from your workstation in Linux, UNIX, Macintosh, and any recent version of Windows. The ARP command takes several switches or parameters that modify its output, and so you want to be sure that you check the help system to determine the correct version of the command to use.

You can view the entire contents of the ARP cache using the -a (All) switch in most implementations. You can specify the IP address of a system's ARP cache, which allows you to view the contents of the ARP server. Because the records contain hardware identification, ARP is a valuable tool for resolving duplicate IP addresses. Otherwise, ARP tends to be rarely used now. [Figure 19.3](ch19.html#a_reply_to_an_arp_-a_command_discloses_t) shows the results of an ARP request for the local system cache on a Windows system. The output lists the different network interfaces, both physical and virtual, because, as you learned in [Chapter 7](ch07.html), a network interface behaves as logically as if it is a separate network device.

![A reply to an ARP -a command discloses the local ARP cache.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1903.png)

**Figure 19.3. A reply to an ARP -a command discloses the local ARP cache.**

# Network Basic Input/Output System

NetBIOS is a Session layer (Layer 5) service for PCs that exposes a network application programming interface (API) that allows older applications to communicate with one another over a local area network (LAN). The acronym stands for Network Basic Input/Output System. NetBIOS was an early PC protocol, developed by a company called Sytek for the IBM PC and introduced in 1983. It became an industry standard for personal computers, even though it was originally limited to enumerating only 80 systems.

Until Microsoft fully adopted DNS name resolution, NetBIOS was the primary method for name resolution on Windows networks. NetBIOS is required by many legacy applications on Windows networks and is also required when the NetBEUI protocol is in use. NetBEUI is an extended version of NetBIOS that allows the use of frames. Note that NetBIOS/NetBEUI is a non-routable protocol that is best used on a LAN, and NetBEUI is a newer and higher-performance version of this standard.

NetBIOS traffic is carried in a transport protocol such as TCP/IP (NetBIOS over TCP or NBT, IPX/SPX [Novell Netware's legacy native format], or IEEE 802.2 [NBF]; all of these are Layer 2 Data Layer protocols). The 802.2 protocol defines Logical Link Control (LLC) software.

NetBIOS names can be different from the names assigned to a system in TCP/IP; they are limited to 15 characters and can't include spaces or the following characters:

```
| ; " * ? / \
```

When you install Windows, the name that you enter for the system is a NetBIOS name. That name can be reassigned in the Computer Properties Computer Name tab. In most instances, the hostname used by DNS is created by prefixing the NetBIOS name to the Primary DNS Suffix. Thus, if the NetBIOS name is `MyComputer` and the Primary DNS Suffix is `MyCompany.com`, then the hostname used by DNS would be `MyComputer.MyCompany.com`.

NetBIOS name resolution is being deprecated in favor of DNS name resolution; Microsoft will not support NetBIOS name resolution on IP version 6 networks.

NetBIOS names are resolved through the use of broadcasts, which works well on small networks, or using a WINS Server, which provides NetBIOS name resolution on larger networks. WINS is described more fully in the next section. Depending upon how you configure the system, resolution can be B (broadcast only), P (peer or WINS only), M (mixed type, broadcast, then WINS), or H (hybrid, WINS, then broadcast).

The NetBIOS service does three things: it registers and resolves names, manages a Session service that is used during a connection, and sends datagrams (packets sent on a non-reliable network) that don't require a named connection.

Windows also uses a lookup file for NetBIOS name resolution that operates similarly to the `HOSTS` file that you saw in the previous section, called the `LMHOSTS` file. In Vista, this file is found at `C:\WINDOWS\SYSTEM32\DRIVERS\ETC` and the file takes a .sam file extension. It can be opened with the Notepad text editor, and is shown in [Figure 19.4](ch19.html#the_lmhosts_file_provides_a_lookup_for_n).

![The LMHOSTS file provides a lookup for NetBIOS, and takes precedence over a WINS Server lookup.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1904.png)

**Figure 19.4. The LMHOSTS file provides a lookup for NetBIOS, and takes precedence over a WINS Server lookup.**

# Windows Internet Name Service

Windows Internet Name Service, or WINS, is a Microsoft server technology for NetBIOS name resolution. WINS translates network addresses into NetBIOS names, just as DNS translates TCP/IP addresses into fully qualified domain names (FQDN). DNS is described in detail in the next section.

WINS is implemented as a database on a Windows server with a management interface. When a WINS client starts up, it sends a name registration request to the WINS server, and the name and associated address are registered as a record in the database. If another client needs to communicate with that first client, it sends a WINS query with the name of the first client to the server, which then responds to the request by sending the first client's IP address.

In large networks, WINS servers lower the amount of overhead in NetBIOS name resolution by providing a more efficient mechanism than broadcast queries. WINS is usually employed in large organizations as multiple servers and includes a replication service for propagating changes.

The Windows Computer Browser Service that populates the Network folder in Windows can use WINS to compose browse lists, and while NetBIOS is not routable, sending the browse lists can be routable.

WINS and DNS name resolution services can operate concurrently on the same network without conflicting with one another. Both store names in individual namespaces; DNS uses a hierarchical structure while WINS uses a flat structure. The WINS service is unaffected by the use of dynamic addressing in DNS using the DHCP service. WINS is important for networks that still contain Windows 2000, XP, or Windows Server 2003 clients. On networks that use both NetBIOS names and domain names, it is required that WINS and DNS services be available.

# Domain Name System

The Domain Name System, or DNS, is the system used to translate IP addresses into FQDN or friendly names. It is the one service used on the Internet and is now used on nearly all TCP/IP LANs. DNS also stores information about mail servers, and eventually the system could be expanded to include all manner of information, such as radio-frequency identification (RFID) tags.

DNS is the result of a set of RFCs that resulted in the development of the first DNS implementation in 1983. The most widely used version of DNS software in use today on the Internet is the one that was written for UNIX that appeared in 1984 from the University of California at Berkeley, and has been reworked and expanded over the years. This version of DNS software, named the Berkeley Internet Name Domain, or BIND, is now open source software that has been heavily tested and refined. BIND appeared on Microsoft Windows with the release of Windows NT. BIND is maintained by the Internet Systems Consortium (`www.isc.org/products/BIND/`).

DNS works by storing a record in a database on a nameserver that is responsible for the translation of a particular domain. The top-level nameservers on the Internet are the root servers for the domains, `.com, .net, .gov, .edu, .us, .uk, .ch`, and so forth, which are now administered by ICANN. These top-level nameservers distribute their content through replication to secondary DNS servers in different parts of the world in order to improve performance and fault tolerance in the DNS system.

### Note

Top-level domains (TLDs) are managed by ICANN, the non-profit Internet Corporation for Assigned Names and Numbers (`www.icann.org`) located in Marina del Rey, California.

You are probably familiar with basic domain name structure. The top-level domain (.com) is separated from the second-level domain (mydomain) by a dot, as in `mydomain.com`, which is sometimes referred to as an octet. Domains become further divided up based on the services they provide, so that `www.mydomain.com` would be one subdomain and `ftp.mydomain.com` would be another. It's important to note that `mydomain.com` and `www.mydomain.com` are not equivalent representations and that the latter is a subset of the former, but both of these addresses can be a hostname. The DNS specification allows for up to 127 sublevels, and up to 63 different octets.

## DNS requests

When you initiate a DNS request for a Web page from a particular Web site, the request doesn't go to either the primary or secondary nameserver for that domain. Instead, the request proceeds level by level, attempting to satisfy the request from the nearest possible DNS source. The request goes to your local system to see if the name is located in your DNS cache, and if so, it returns the result. The local DNS cache doesn't normally store many records. Not all operating systems turn on a local DNS cache, and so you may need to install a package on a Linux distribution to enable this feature.

In Windows, you can see the contents of your local cache with the following command: `IPCONFIG /DISPLAYDNS`. [Figure 19.5](ch19.html#to_view_the_current_contents_of_your_loc) shows an example of the output from a Windows Vista 64 system. The output of this command lists the name of the record in the domain, record types, time to live (TTL), and the address of the record in the final line. If you want to empty the contents of the local cache, then you can use the `IPCONFIG /FLUSHDNS` command.

![To view the current contents of your local DNS cache in Windows, use the IPCONFIG /DISPLAYDNS command.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1905.png)

**Figure 19.5. To view the current contents of your local DNS cache in Windows, use the `IPCONFIG /DISPLAYDNS` command.**

The local DNS cache doesn't store many records (depending upon how you configure it), and so if the record you need isn't in the cache or has run out of time to live, then the request is passed on to your local DNS server. If you are using DNS on a large network, and local DNS lookup is required, then your network is probably running its own DNS service. If you have a small network and use DNS for Internet name resolution, then the request is forwarded to the DNS servers that you have configured in your network interface's TCP/IP Properties dialog box, or the ones that are automatically assigned for you if you designated that option.

Many firewalls and Internet appliances come with DNS servers, and so using that as the primary DNS server for your connection is usually faster than waiting for a response from a DNS on the Internet. Most people assume that DNS requires that they enter the address for the DNS server for their Internet service provider (ISP) into their TCP/IP properties. However, that is not the case. You can use any highly available DNS server for this purpose.

Assuming your DNS request can't be satisfied by your local cache or by a DNS service on your LAN, the request is forwarded to a DNS server outside of your LAN. It arrives at the DNS server that you specified outside your LAN, or if you didn't specify one, at the DNS server of your ISP. That DNS server attempts to fetch the record relating the name you want the address of from its cache. If it doesn't find the record, it then queries the authoritative nameserver for the domain you are requesting. Eventually, the request may end up at a root nameserver, but that is very rare. The replication feature of DNS populates the vast majority of the addresses out to secondary servers. If you've ever wondered why changing an ISP for your domain takes 24 to 36 hours to take effect, this replication process is the reason.

DNS is a client-server architecture, and the client software is called a *resolver*. When a client issues a DNS query, it can be one of two types: either a recursive query or a non-recursive query. In a recursive query, the more commonly issued of the two types, the DNS server must return an answer within the time period allowed by the Time to Live parameter, even if the answer is a DNS error. In a non-recursive query, the DNS server can provide a partial answer or an error. The resolver may be configured to use either type of query, but it will iteratively move up the DNS domain structure until it can complete the entire DNS name.

Consider a request for an address for a hostname such as `www.mydomain.com`. The DNS query is made and sent to the root nameserver. The root nameserver doesn't contain the record, and so a response is sent to a software module called a DNS recurser with an address for the next nameserver in the chain. The recurser sends the request to the second nameserver at a lower level, which either has the record or sends a response back to the DNS recurser with the next nameserver in the sequence. The process continues iteratively until the IP address is returned.

When a successful query returns a result, the resource record (RR) for that response is stored in the cache, and the number of records retained is a function of both the cache size and the records' time to live. Not all queries are forward looking; that is, the query starts with an FQDN and the result returns an IP address. Some DNS queries are reverse queries; they try to match an IP address to an FQDN. Reverse queries are supported by third-party software.

In practice, the root nameservers and many of the upper-level DNS servers are cached at various places and almost never service DNS requests directly.

DNS is not without its defects. One problem that you can encounter when you register a DNS record that points to a nameserver and when you query that nameserver is that it points back to the original nameserver. This creates a circular dependency that cannot be resolved, and so nameservers are provided with a record that points to the previous nameserver in the chain so that circular dependencies can be broken.

## DNS topology

DNS is a hierarchical namespace, which means that it is an inverted tree structure similar to a drive's file system. The top-level node in the namespace is occupied by the authoritative nameserver or the primary or root nameserver. That nameserver contains what are called *resource records*, which link that nameserver to other nameservers that contain the resource records of other nameservers as the tree fans out.

Each subsequent branch in the tree is organized into what are called *zones of authority*, with all connected nodes (DNS servers) referring to the top of that branch as their authoritative nameserver. In the domain `MyCompany.com`, a zone might be composed of a server at `www.MyCompany.com`, which is given responsibility for the zone beneath it. In DNS parlance, the domain is indicated by a record referred to as the *Start of Authority*, or SOA, and that record is then associated with the domain controller.

If the primary DNS server in the subdomain is MyDNSServer, then its address is `MyDNSServer.MyCompany.com`. Because the authority has been delegated to `www.MyCompany.com`, that DNS server becomes the primary DNS server for the zone `MyCompany.com`, the owner of the server is root@`MyDNSServer.MyCompany.com`, and the address shown in the SOA record is root.`MyDNSServer.MyCompany.com`.

[Figure 19.6](ch19.html#a_representation_of_the_dns_namespace) shows a representation of the DNS namespace.

In [Figure 19.6](ch19.html#a_representation_of_the_dns_namespace) the top zone exists as the root DNS server. That server might be the root .COM, .GOV, .EDU or some other root server. As the tree subdivides, DNS delegates the authority to respond to DNS queries to a DNS zone server, and that server services all DNS requests for that zone and if necessary for the zones beneath it. Each level DNS zone server delegates the DNS authority to the subzones beneath it so that authority is passed from the top-level DNS server to servers at levels below. The goal of the DNS hierarchy is to push DNS requests down to the lowest possible level of the tree.

![A representation of the DNS namespace](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1906.png)

**Figure 19.6. A representation of the DNS namespace**

## Resource records

DNS is implemented as a database system that can be managed either through a set of commands in the command-line interface (CLI) or through the use of a graphical user interface (GUI) management utility. The system allows for secondary DNS servers, as well as replication schemes.

In Windows Server 2008, for example, DNS is a role that you can install on the server. For security reasons, Windows does not allow DNS to be installed on a domain controller (although it can be run on a Read-only Domain Controller [RODC]), but the DNS role can coexist with many other server roles. In a large domain, DNS activity is one of the more demanding roles that a server can engage in. It's common to dedicate a server to DNS alone.

With DNS installed, Windows Server 2008 adds the DNS Manager to the list of utilities available from the Administrative Tools folder. The DNS Manager (like other Administrative Tools) is an MMC snap-in that opens in the Microsoft Management Console, which is a framework application that supports different queries to underlying databases. [Figure 19.7](ch19.html#the_windows_server_2008_dns_manager) shows a sample domain in the DNS Manager. Notice that there are several different record types populating the Forward Lookup Zones node that is exposed in the figure.

![The Windows Server 2008 DNS Manager](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1907.png)

**Figure 19.7. The Windows Server 2008 DNS Manager**

[Figure 19.7](ch19.html#the_windows_server_2008_dns_manager) contains several common record types, with the exception of Pointer (PTR) records. that DNS uses to resolve queries. They include the following:

- **Start of Authority (SOA) record**. The SOA indicates which server is responsible for this particular zone.
- **Name Server (NS) record**. The NS record used by DNS displays the address of the nameserver for the domain. There must be one entry for any domain, and because nearly all domains employ multiple domain servers for failover and fault tolerance, it is more common to have two or more NS entries for redundancy.
- **Address (A) record**. An A record or host address should represent the bulk of the records in a DNS database for a network of any size. The A record provides the mapping of a hostname to an IP address.
- **Canonical Name (CNAME) records**. A CNAME record is an alias hostname. The alias points to the hostname indicated in the first field of the record. For the record shown in the figure, the CNAME record is the fourth record and the hostname is AliasName. CNAME records are sometimes used when you want to hide the real name of a system from a client.
- **Mail Exchange (MX) record**. An MX resource record is used to point to a mail server on the network.
- **Pointer (PTR) records**. PTR records (not shown in [Figure 19.7](ch19.html#the_windows_server_2008_dns_manager)) are used to map an IP address to the associated hostname. The reason you might want to establish PTR records is to support reverse lookups. For this reason, reverse lookups are sometimes called PTR queries. When you use PTR records, it is important to make sure that they are up to date and contain the same information for hosts that the Address or A records do.

This list details the most common DNS resource records in use for name resolution of hosts. However, as was mentioned earlier, DNS records can be created for a variety of resources. The Resource Record Type dialog box, shown in [Figure 19.8](ch19.html#the_resource_record_type_dialog_box), lists the different types of resource records that Windows Server 2008 currently supports. Refer to [Table 19.2](ch19.html#resource_record_types) for the listing of descriptions contained in the Resource Record Type dialog box.

![The Resource Record Type dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1908.png)

**Figure 19.8. The Resource Record Type dialog box**

**Table 19.2. Resource Record Types**

| Resource Record Type | Description |
| --- | --- |
| Source: Microsoft Corporation, Windows Server 2008 Record Resource Types dialog box. |  |
| AFS Database (AFSDB) | Andrew File System Database (AFSDB) server record. Indicates the location of either of the following standard server subtypes: an AFS volume location (cell database) server or a Distributed Computing Environment (DCE) authenticated nameserver. Also supports other user-defined server subtypes that use the AFSDB resource record format. (RFC 1183) |
| Alias (CNAME) | Alias record. Indicates an alternate or alias DNS domain name for a name already specified in other resource record types used in this zone. The record is also known as the canonical name (CNAME) record type. (RFC 1035) |
| ATM Address (ATMA) | ATM Address (ATMA) record. Maps a DNS domain name to an ATM address. |
| Host Address (A or AAAA) | Maps a DNS domain name to a 32-bit IP version 4 address (RFC 1035) or a 128-bit IP version 6 address. (RFC 1886) |
| Host Information (HINFO) | Host Information (HINFO) record. Indicates RFC 1700 reserved character string values for CPU and operating system types for mapping to specific DNS hostnames. This information is used by application protocols, such as FTP, that can use special procedures when communicating between computers of the same CPU and OS type. (RFC 1035) |
| Integrated Services Digital Network (ISDN) | Maps a DNS domain name to an ISDN telephone number. ISDN telephone numbers used with this record meet CCITT E.163/E.164 international telephone numbering standards. (RFC 1183) |
| Mail Exchanger (MX) | Provides message routing to a specified mail exchange host that is acting as a mail exchanger for a specified DNS domain name. MX records use a 16-bit integer to indicate host priority in message routing where multiple mail exchange hosts are specified. For each mail exchange host specified in this record type, a corresponding host address (A) type record is needed. (RFC 1035) |
| Mail Group (MG) | Adds domain mailboxes, each specified by a mailbox (MB) record in the current zone, as members of a domain mailing group that is identified by name in this record. (RFC 1035) |
| Mailbox (MB) | Maps a specified domain mailbox name to a host that hosts this mailbox. (RFC 1035) |
| Mailbox Information (MINFO) | Specifies a domain mailbox name to contact. This contact maintains a mail list or mailbox specified in this record. Also specifies a mailbox for receiving error messages related to the mailing list or mailbox specified in this record. (RFC 1035) |
| Next (NXT) | NXT resource records indicate the nonexistence of a name in a zone by creating a chain of all of the literal owner names in that zone. They also indicate what resource record types are present for an existing name. |
| Pointer (PTR) | Points to a location in the domain name space. PTR records are typically used in special domains to perform reverse lookups of address-to-name mappings. Each record provides simple data that points to some other location in the domain name space (usually a forward lookup zone). Where PTR records are used, no additional section processing is implied or caused by their presence. (RFC 1035) |
| Public Key (KEY) | Public key (KEY) record. Stores a public key that is related to a DNS domain name. This public key can be of a zone, a user, or a host or other end entity. A KEY resource record is authenticated by a SIG resource record. A zone level key must sign KEYs. |
| Rename Mailbox (MR) | Specifies the domain mailbox name for a responsible person and maps this name to a domain name for which text (TXT) resource records exist. Where RP records are used in DNS queries, subsequent queries can be needed to retrieve the text (TXT) record information mapped using the RP record type. (RFC 1183) |
| Responsible Person (RP) | Responsible Person (RP) record. Specifies the domain mailbox name for a responsible person and maps this name to a domain name for which text (TXT) resource records exist. Where RP records are used in DNS queries, subsequent queries may be needed to retrieve the text (TXT) record information mapped using the RP record type. (RFC 1183) |
| Route Through (RT) | Route Through (RT) record. Provides an intermediate-route-through binding for internal hosts that do not have their own direct wide area network (WAN) address. This record uses the same data format as the MX record type to indicate two required fields: a 16-bit integer that represents preference for each intermediate route and the DNS domain name for the route-through host as it appears elsewhere in an A, X25, or ISDN record for the zone. (RFC 1183) |
| Service Location (SRV) | Service Location (SRV) record. Allows administrators to use several servers for a single DNS domain, to easily move a TCP/IP service from one host to another host with administration, and to designate some service provider hosts as primary servers for a service and other hosts as backups. DNS clients that use an SRV-type query ask for a specific TCP/IP service and protocol mapped to a specific DNS domain, and receive the names of any available servers. (RFC 2052) |
| Signature (SIG) | Cryptographic signature (SIG) record. Authenticates a resource record set of a particular type, class, and name, and binds it to a time interval and the signer's DNS domain name. This authentication and binding is done using cryptographic techniques and the signer's private key. The signer is frequently the owner of the zone from which the resource record originated. |
| Text (TXT) | Text (TXT) record. Holds a string of characters that serves as descriptive text to be associated with a specific DNS domain name. The semantics of the actual descriptive text used as data with this record type depends on the DNS domain where these records are located. (RFC 1035) |
| Well-Known Services (WKS) | Well-Known Services (WKS) record. Describes the well-known TCP/IP services supported by a particular protocol on a particular IP address. WKS records provide TCP and UDP availability information for TCP/IP servers. If a server supports both TCP and UDP for a well-known service or if the server has multiple IP addresses that support a service, then multiple WKS records are used. (RFC 1035) |
| X.25 | X.25 (X25) record. Maps a DNS domain name to a public switched data network (PSDN) address, such as X.121 addresses, which are typically used to identify each point of service located on a public X.25 network. (RFC 1183) |

# Name Resolution versus Directory Services

Directory services are products that for the most part conform to the X.500 LDAP standard. Examples of directory services are Windows Active Directory, the Network Information Service used by Solaris and other UNIX/Linux implementations, Novell's excellent eDirectory, among others. The primary function of a directory service is to securely contain identification and properties for network objects. Network objects include systems, hostnames, and asset information; but they also include objects such as user and group accounts, operating system-specific domain organizational structures, application-specific data, and almost anything else that the operating system vendor and third-party vendors who extend these directories want to include in them. Directory services are extensible, and more importantly, they are secured and protected. Although name resolution is one of the main features of a directory service, it isn't the only feature and it isn't really the primary feature of these systems.

Name resolution services have a more limited role. They are focused on a mapping function and they have a severely limited ability to be extended. You can see the effect of this difference on the development of DNS. While DNS is the means used for system identification on the Internet and is nearly universally used for system identification on intranets and LANs, DNS isn't used for many of the record types that you saw in the previous section. The use of directory services suppresses the use of DNS in networked operating systems for other purposes.

# Summary

In this chapter, the need to map or translate friendly names to network addresses, and vice versa, was explained. Over the years, many systems have been developed to address this need.

The first system was the `HOSTS` file, which, although it still exists, sees very limited use. The ARP protocol was another early attempt and is still in use. The NetBIOS protocol provides a mechanism to allow Windows computers to be enumerated on a LAN. NetBIOS servers are called WINS servers, and most large Windows networks install WINS as a naming service because of its performance advantages.

The Domain Name System, or DNS, is the name resolution service that associates IP addresses with friendly names for the Internet. In this chapter, you learned how DNS networks are constructed and how queries for name resolution are conducted against the service. DNS can also be used on LANs, and DNS is valuable for providing a unified name resolution service that can be used on TCP/IP networks.

This chapter also described the difference between name resolution services, which are essentially mapping or translation services, and directory services. Directory services are secured databases that store all kinds of information on network objects and are extensible. Modern directory services are primarily based on the X.500 LDAP protocol.

In the next chapter, you learn about the different classes of Network Operating Systems (NOS), their common characteristics and features, as well as the factors that differentiate them.
