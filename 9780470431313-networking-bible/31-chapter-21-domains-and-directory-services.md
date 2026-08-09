# Chapter 21. Domains and Directory Services

**IN THIS CHAPTER**

- Learning what a directory service is
- How information enables intelligent network applications
- Directory services organize networks into domains
- Microsoft Active Directory

Directory services play a central role in the current network operating systems' client-server architecture. They provide a name service, store information about objects on the network, and allow this information to be propagated to other servers and applications. There are many directory services in use today, and modern networks use them heavily.

The smallest fundamental unit in a directory service is the domain. A domain is a collection of systems that share the same security database. Domains can be of various types and contain elements such as organizational units, user and machine accounts, and other objects that can be addressed using a unique Distinguished Name.

Most modern directory services are based on the X.500 standard. The LDAP version of X.500 was created for TCP/IP networks and is used for most of the products that are available today. The different directory services and their characteristics will be described. Among the features presented are policy engines, replication and synchronization, single sign-on, namespaces, identity management, and role-based access control.

Microsoft Active Directory (AD) is the best known and most widely used directory service. AD was built to store objects of various kinds, and includes aspects of security properties. The different classes of objects stored in AD are described, as is the way that domains are deployed and relate to one another.

# Directory Services and Domains

Large computer networks create a problem for the designers of network operating systems working in the client-server model. How do you account for and manage a large number of systems, users, peripherals, and other items that run on the network? The solution boils down to storing this information in a database somewhere on the network so that the information can be accessed quickly and reliably. The software that manages this information is referred to as a *directory service*, and the fundamental unit used to store a network's information is called a *domain*. Usually a domain is associated with its own security database.

Network architects realized that they could store information about services and applications that ran on the networks, who could access those applications and how they could do so, and many other properties besides. They also realized that this information could serve as the key in a mechanism that authenticates and authorizes access, and that the system could be infinitely extensible. That meant that these databases could serve additional needs going forward that couldn't be anticipated during the initial design.

You've already seen an example of a directory service in previous chapters. The Domain Name Service is a directory service.

### Note

DNS is covered in [Chapter 19](ch19.html).

The networked databases that were developed came to be known as directories, and they serve a function that is similar to a dictionary. The name harkens back to the idea of a phone book listing; the word *directory* was applied to many large database projects in the 1970s. Because this directory was designed to provide a network service, the term that eventually stuck was directory services. The standardization of directory services under a few industry models led to a proliferation of directory services for all of the network operating systems, and has been applied to large enterprise applications that manage data stores of all kinds.

Because the information contained in these central network databases would be clearly sensitive, they would have to be highly secure, and that security needed to be intimately related to and managed by this central information store. Some of these directory services incorporated network security in a single entity, while others worked with external security systems.

A directory service may be built using any type of database system: flat file, relational, hierarchical, peer-to-peer, and so on. The most popular directory services are the ones that are semi-relational, hierarchical, highly saleable, and that store object data. Scalability is important because you want to be able to preserve all of your information as your network grows and changes.

While directory services are similar to relational databases, there are some significant differences. Directory information is read from a lot more than they are written to; therefore, mechanisms like transaction rollbacks aren't as necessary, nor are they as well implemented as they are in Relational Database Management Systems (RDBMS). Directory services also don't have the same requirements for performance or for normalization (optimization) that relational databases do. You'll find that many directory services create redundant data sets in multiple locations if that helps to improve performance. A relational database can be tightly designed because it is built to serve a specific function. A directory service may be called on to store a variety of diverse data that are related in random ways, and thus requires a less structured schema.

## Banyan VINES

The area of directory services owes much to the development of Banyan VINES in the early 1980s. VINES was an acronym for the **V**irtual **I**ntegrated **NE**twork **S**ervice, and was a computer network operating system that was based on UNIX. For its network stack, VINES used the Xerox Network Services (XNS) protocol suite, which was popular at the time, and ran a variant called the VINES Internetwork Protocol (VIP). VINES networks were packet based, used automatic client addressing, and had a routing protocol and an Internet control protocol. Upper-level application protocols included standard file and print services. None of the technologies are particularly noteworthy; what made VINES unique was their upper-level name service, called StreetTalk.

### Note

XNS was a packet-based LAN protocol suite that was used in the 1980s and 1990s as the basis for Novell NetWare, 3COM, and others. TCP/IP networking has entirely replaced the XNS networking technology.

StreetTalk was one of the early directory services. It created a namespace for the entire internetwork based on a distributed replicated database, and allowed different networks to share resources. In StreetTalk, an address was formed from a hierarchical naming scheme that reproduced an object hierarchy in the form, `object@group@organization`. An object could be a network or printer share, or it could be a user account. At the time, VINES clients were MS-DOS and Windows 3.x systems. There were no domains in a VINES network.

For nearly a decade from 1985 onward, VINES was the product of choice when you wanted to install an operating system with a directory service embedded in it. It achieved market success with a number of large deployments. Eventually, Novell introduced Novell Directory Services and Microsoft introduced the Active Directory, both of which helped to displace VINES in the marketplace. Jim Allchin, the chief architect at Banyan VINES, joined Microsoft in the mid-1990s and was important in the development of the Active Directory. Banyan grew increasingly obsolete and abandoned their brand in 1999.

## Domain types

Every information system is organized around a basic unit. In databases that unit is a record, in file systems the unit is a file, and in a directory service the basic unit is a domain. A network domain describes a group of systems and associated resources that are organized by a directory service and share a common security database or security model.

There are many different schemes that are used to organize domain types. Among the more commonly encountered are the following, or some combination of any of these:

- A central master domain with a domain tree, hub, or star as shown in the single master case
- A multiple master domain structure
- Resource domains
- Remote domains where the links represented by either a trust relationship and/or replication are WAN connections
- Application-specific domains

[Figure 21.1](ch21.html#different_domain_topologies) illustrates these different domain types.

![Different domain topologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2101.png)

**Figure 21.1. Different domain topologies**

## Interoperability

Migrating an established directory for a large network to another directory is one of the more painful tasks an organization's IT staff can be called on to perform. The task is much more difficult than moving data from one enterprise database to another one for two reasons: most databases either come with import/export functions or have third-party tools readily available, and directories are burdened with security functions and proprietary structures that make them difficult to crack and difficult to move data out of.

A heterogeneous directory service stores information about systems with different operating systems, a feature that would be valuable for any number of reasons. How well alien systems are represented in a directory service is a function of how hard the directory system vendor wants to work to make that happen. For some directory services, heterogeneity isn't necessarily a benefit, and homogeneity is preferable.

It isn't uncommon to have many directory services all operating on different servers throughout the network. You might see a directory service for each of the major network operating systems; some may be associated with Web servers such as APACHE, while others might be part of an enterprise mail application, such as Microsoft Exchange or Lotus Notes.

In very large organizations, there might be as many as 50 different directory services in use, and that introduces a significant amount of overhead into managing all of this information scattered about the network. To this end, directory services often try to connect to as many of these different systems as possible and exchange information with them. Any system that tries to consolidate information in this manner is often referred to as a federated service. An example of a federated database system is SAP's Enterprise Resource Planning (ERP) technology suite, which is a master database of databases.

# Domain Servers

The computer system that runs the directory service is referred to as the network's domain server, or alternatively, a domain controller. For security reasons, nearly all directory services store their data and related security information on the same domain server.

In small networks, domain servers can look after a few different services beyond the directory service. An example of this type of system is the Microsoft Small Business Server (SBS). Early versions of SBS were a directory server, a DHCP/DNS server, an Exchange Server, an IIS Web Server, a Microsoft Internet Security and Acceleration (ISA) server, and perhaps a SQL Server. All of these applications are there in the SBS "box," and if the server is powerful enough, then with a maximum of 50 allowed connections, this server could perform reasonably well. The later version of SBS allows for up to 100 connections, with just a little more power required. Many installations of SBS install only a subset of these available applications.

Security experts will tell you that the fewer extraneous applications and services that a directory server runs, the safer it is. In larger networks of hundreds and thousands of users and connections, domain servers become heavily loaded with requests. In order to manage requests, different directory server systems create either duplicate peer domain servers and replicate data between them, or a class of backup domain servers. These different approaches have advantages and disadvantages with respect to system failures and preserving data coherency.

Depending upon the nature of the domain and directory service and the tasks that are being performed, a domain can have as many as one domain server for two or three systems. Some home server appliances based on Linux are marketed for this size of network. For larger networks, domain servers can service anywhere from 50 to 500 systems before they are taxed. The other servers in the domain that aren't domain servers are called resource servers and application servers; they may also be named based on the task that the server performs: file and print, backup, security, or whatever scheme the directory server enforces.

# Directory Services

Directory services store metadata, or data about data. In an object database that stores network data, metadata provide the context that allows the system to determine how the data set is organized. The directory schema defines a set of object classes, to which are assigned a set of required and optional attributes. When possible, most directory services use the object classes, attributes, and ID numbers that are registered by the Internet Assigned Numbers Authority, or IANA, as standards. Every object that is a secured resource is attached to an Access Control List (ACL) that determines who can use the object.

Metadata provides the relational context that offers what is essentially a map to system resources. Many information systems have this characteristic, a separation of data from context.

A schema overlays the data in a database to provide the template used in the construction of records and files; an XML schema file serves the same function for XML data, allowing a structured document to be recreated. Because directory services are databases, it shouldn't be too surprising that they use a schema as their architectural blueprint. A directory service is an abstraction layer that separates the physical reality of clients, servers, and resources from the logical assignments with a mapping function based on a namespace assignment.

You need a directory service when your network requires the following:

- Centralized management of network services
- A defined security policy with granular privileges and rights
- The ability to delegate responsibility for different resources to different individuals
- The ability to scale your network to support more users than a peer-to-peer model supports
- The ability to support a variety of clients and operating systems
- The ability to audit network events

Directory services are not all sweetness and light; they have a downside as well. They add additional cost and complexity to a network and require that domain services always be available for the network to function properly. These additional requirements limit the use of domains on small home and office networks of fewer than 20 connected systems in most instances.

## Synchronization and replication

Directory services are among the most active network services that are in use. For fault tolerance and improved performance, directory services are replicated on different servers and in different locations. Once these services have been replicated, there is a need to propagate the changes occurring on the different locations through some sort of replication scheme. Replication is a process by which data is transferred to another system, and updated frequently. An important point to note about replication is that it doesn't maintain a record of the state of the system, just its current form. The methods used by directory services to synchronize and replicate data are the same mechanisms that are used by other distributed enterprise applications such as database systems, and they vary from product to product.

Replication can be a single execution unit that is propagated from one system to many systems, or it can be an ongoing process during which changes are propagated as a set of transactions over time. Replication can require that the same change be made at every copy, something that is called active replication. Active replication works with a small number of systems with reasonable network connections, but removes many of the benefits of replication when the number of copies grows or they are on a WAN. The alternative is to make changes at one directory server and then transmit the changes between all of the other directory servers; that is referred to as passive replication. Nearly all schemes used by directory services use a passive replication scheme.

If a single copy is designated as the master copy, the replication topology is a master/slave system. This is the method used with the early versions of Microsoft Active Directory with its system of Primary Domain Controller and Backup Domain Controllers. The advantage of a master/slave system is that it is simpler to create and doesn't require some method for controlling concurrent changes to the same record. When you move to a multi-master topology, you gain performance and the added fault tolerance of not being dependant on a single master; however, this is gained at the expense of having to manage concurrency, perhaps by employing a distributed lock management service or some other form of data conflict resolution. Microsoft moved Active Directory to a multi-master system with Windows Server 2003.

Multi-master replication can suffer from inconsistencies introduced into the system by network latency because it is an asynchronous process. This type of replication doesn't always conform to the rules of providing ACID transaction, as most database management systems require. ACID stands for Atomicity, Consistency, Isolation, and Durability, and it is a method of determining whether a database transaction has the necessary properties to be processed with guaranteed certainty of being correct. For these reasons, AD doesn't use a pure multi-master replication scheme.

AD uses an update pattern that updates all directory servers, but requires a time interval to complete the update. The system for AD replication has been described as a Floating Single Master Operations system or alternatively, an Operations Masters system, and it is flexible enough to scale to a large number of domains and accommodate links of varying bandwidths.

## Single sign on

In an environment where there are multiple security apparatuses, each validating a user's access to different resources, it can be quite troublesome if logon requests keep popping up. This problem has been referred to as password fatigue. You encounter the problem of password fatigue when you browse the Internet and are forced to log into one Web site after another. There are solutions to the problem of logging into a Web site. You can use a Firefox extension like BugMeNot and assume another alias (effective, but not nice), or you can use a product like RoboForm to store all of your passwords and automate your logon. However, neither of these approaches provides a universal response to the problem of password fatigue.

Directory services in large networks are constantly interacting with different directory services, domains, applications, and resources. In an effort to solve the problem of recurring logons, some directory services offer what has come to be called a single sign on (SSO) capability, or in an enterprise, an enterprise single sign on (E-SSO). The user signs on once in their domain and their credentials are stored and passed to other security objects in a form that those objects can accept. So if you entered your network operating system credentials, those credentials would be accepted by your enterprise mail program or another application.

The best of these systems require a combination of authentication that includes at least two of the following three "Somethings":

- Something that you know (your ID and password)
- Something that you have (a Smart Card)
- Something that you are (your fingerprint, your eyeballs, or your smile)

### Note

Some of the security mechanisms used by SSO systems are described in [Chapter 27](ch27.html).

SSO isn't an easy technology to implement because authentication methods for different systems can use very different technologies. They are also criticized because an SSO system removes the ability of different systems to individually challenge a request, thus lowering the overall security of the network. Only a few directory services offer this feature, often as a very expensive add-on module. For most directory services, you need to turn to third-party programs to implement this feature, such as Citrix Password Manager.

## Namespaces

A directory service defines a namespace for all of the objects it contains. You've already seen the use of a namespace with the Domain Naming Service (DNS) that the Internet uses to address locations on the Internet. To be effective, a namespace must create a unique designation that should be the logical composite of the various branches of the tree. For DNS, this is called the Uniform Resource Identifier (URI).

Many organizations adopt a naming scheme for their domains that parallels how DNS would label the directory structure of a Web site. There are some good reasons to do this, foremost of which is that it enables the domain structure to be exposed to the Internet at some later date with no significant name changes. However, there is a distinct difference between how you would name a private network and how you have to name a network that is connected to the Internet, as you can see in [Figure 21.2](ch21.html#a_public_versus_private_network_and_asso).

With a directory (like Active Directory, for example) the Directory Namespace can include the .com suffix. The name is built up from the composite of the individual nodes of the tree. The path to a node in DNS is obtained from the folder hierarchy, as follows: `www.XYZ.com/ABC/GHI`.

### Note

Should you choose to use a public DNS namespace such as .COM, .GOV, or .EDU on a private network, you need to ensure that the internal and external domain names don't collide. The public DNS server should be configured to forward address requests to the internal DNS server of the private network.

![A public versus private network and associated namespaces](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2102.png)

**Figure 21.2. A public versus private network and associated namespaces**

## Policy engines

When you store network object information in a database, it is possible to create a set of rules that determine how objects are used. These rules are stored separately from the security engine that a network operating system uses, although some policy rules overlap.

A policy would define some feature of network behavior, including the following:

- Client desktop configuration
- Update or patch frequency
- Audit behavior
- Password complexity
- Logon and logoff actions

A group policy engine is the mechanism used to enforce a set of operational rules that you define for a network. They serve the same functions as business rules saved as stored procedures with a relational database system.

The best-known policy engine is Group Policies from Microsoft. Group Policies are stored in Active Directory. There are many other instances of policy engines associated with network operating systems. The Sun Solaris Resource Manager (SRM) offers policy management for setting resource limits. Within the SRM, you can set the number of allowed processes, connected users, number of logons, and other policies. Through scripting, SRM can set new policies upon execution. Every network operating system implements some form of policy management.

Once you start to look at third-party policy engines, you find that there are a vast number of choices available. Space precludes a fuller discussion of this topic, but one product of note is the Novell ZENworks suite of applications. These products offer many of the capabilities of policy engines and work well in a heterogeneous network environment. [Figure 21.3](ch21.html#the_zenworks_suite_offers_a_number_of_po) shows the installer page for ZENworks, which gives you an idea of the capabilities of this product.

Let's use Microsoft Active Directory as an example of what is possible for a policy engine to implement. In [Figure 21.4](ch21.html#different_forms_of_group_policy_and_dele), you can see how various Group Policies can be defined to control who has access to which resources, how responsibilities can be delegated, and what policies apply to which systems. This system of policy management began with Windows 2000 and applies to all systems (client and server) that have been released since then. With every subsequent release of a new operating system, additional policies are added to the Windows Group Policy Engine. Windows Server 2008 shipped with nearly 2,400 policy settings.

![The ZENworks suite offers a number of policy enforcement capabilities.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2103.png)

**Figure 21.3. The ZENworks suite offers a number of policy enforcement capabilities.**

The central domain is subdivided into two different trees under Organizational Unit 11 (OU_11) and OU_12. The Domain Admin has delegated responsibility to control the network from OU_111 down to another Admin, print operations from OU_112 to the Print Operator, and OU_12 down to the OU Admin. Because the OU_12 Admin has full control, they have delegated the administration for OU_121 to an administrator with even narrower responsibilities. Delegation is performed as part of the security engine, which may or may not be part of the policy engine. For Windows Active Directory, the storage of security policies is in a separate database, but the control over these features is exposed in the central management console of the server, along with policy features, as well as throughout the other elements of the Windows GUI.

Active Directory lets you set a general policy that you can apply to a domain, and using a system of Administrative Templates, modify those policies. Policies in Windows can be changed using a utility called the Group Policy Object Editor, a snap-in for the Microsoft Management Console. Policy objects are also exposed in the Group Policy Management Console. The policies that you set in Active Directory (see [Figure 21.5](ch21.html#group_policy_precedence_in_active_direct)) apply to Windows systems; you can use a product like Centrify DirectControl (`www.centrify.com/directcontrol/overview.asp`) to extend policy management to UNIX, Linux, and Mac clients in a Windows network.

![Different forms of group policy and delegations](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2104.png)

**Figure 21.4. Different forms of group policy and delegations**

At any point in the network, you can apply a group policy that alters the behavior of network nodes at that level or below. Group Policy Objects may be targeted at sites, domains, and Organizational Units (OUs), and are applied in that order of precedence; the group policy of the OU would be the last applied. In [Figure 21.4](ch21.html#different_forms_of_group_policy_and_dele), two local policies are defined: Group Policy_11 where user and password policies are set for systems at OU_11 and below; and Group Policy_122 where a set of machine policies are applied to systems in OU_122 and below. Local group policies take precedence over general group policies according to a set of rules that Microsoft defines but are scoped to individual servers or systems.

![Group Policy precedence in Active Directory](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2105.png)

**Figure 21.5. Group Policy precedence in Active Directory**

The ability to record different events into logs is an important set of policies that are referred to as auditing. Many directory services include the ability to create and store audit policies on a per-object basis. Auditing is applied in a granular fashion and can be logged for directory or resource access, replication events, and any service changes. Auditing can generate a very large volume of data, so as a general rule, audit functions are usually turned off by default in order to maintain the highest performance. However, auditing can provide the information necessary to diagnose system errors, provide metrics to improve performance, and determine how the security system reacted to an event. In Windows Server 2008, you can turn auditing on for four different categories of directory service events: access, changes, replication, and detailed replication.

## Role-Based Access Control

Many network operating systems implement different classes of users that may be referred to as roles and implement a form of access that is called Role-Based Access Control (RBAC). These roles are often organized in a hierarchy with an order of precedence. Roles impart rights and impose constraints on what may be done when an action is taken. Among the systems that use RBAC are Microsoft Active Directory, Sun Solaris, SELinux, SAP R/3, Oracle, and FreeBSD.

In Windows, you find "built-in user groups," and include categories such as Administrator, Domain Admins, Domain Users, Power Users, Guests, and Print Operators. Related machine groups are defined, including Domain Controllers, Domain Computers, and Replicator. Of course, you can also create your own.

Sun Solaris RBAC appeared in version 8 and was greatly expanded by version 10. It provides a number of similar roles: All, Primary Administrator, System Administrator, Operator, Basic Solaris User, and so forth. RBAC roles have an access list that creates a profile describing what the role is capable of. In Solaris, you can work with RBAC from the command line, or using the Solaris Management Console (SMC). The SMC is shown in [Figure 21.6](ch21.html#the_solaris_management_console_provides). In it, you can attach user accounts to roles, and manage the different roles that Solaris offers.

RBACs are policy neutral; they are applied to objects, regardless of a policy in place that might contradict the role. They are meant to simulate job function and are defined in order to speed up the management of delegation assignments. With a role may come a set of permissions that allow actions such as add a user, or print to this printer. Unlike Access Control Lists, which are associated with a particular system or network object, the permissions associated with an RBAC are attached to the operation that the role allows. This is a higher-level function, more often associated with an application.

![The Solaris Management Console provides access to RBAC features in the Solaris operating system.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2106.png)

**Figure 21.6. The Solaris Management Console provides access to RBAC features in the Solaris operating system.**

## Identity management

Directory services store information on users, their accounts, and a number of related properties. As such, directory services are intimately related to the concept of identities and can store information managed by identity services and servers. Identity spans both user management and security functions and can be implemented as a service of either function or its own independent service.

In large organizations, the identity of users on the network may be stored in many different places. Identity services can help to synchronize the different information sources so that the data they contain is the same. This includes the synchronization of passwords and access rules, the ability to provision new users, and the ability to remove users who have left the organization so that network security isn't compromised.

Just like SSO described earlier, an Identity and Access (IDA) server needs to function across different network systems in order to be useful. For an IDA server, it may be necessary to:

- Manage certificates and smart cards and connect to the various certificate services.
- Provide a federated service among different directory services that are on the network to mediate identities between them. The most important directory services you might want to work with include Microsoft Active Directory, Sun Directory Server, Novell eDirectory, and IBM Tivoli Directory Server.
- Work with e-mail and messaging services' identities, and if necessary, synchronize with them. Lotus Notes and Microsoft Exchange are two examples of servers that store identities that often interact with identities in directory services.
- Manage network database identities so that a user can't log on without a valid identity. Oracle, IBM DB2, and Microsoft SQL Server are examples of database management systems that can store their own user accounts.
- Work with enterprise applications such as SAP, telephony applications, and others.

Microsoft refers to this concept of identity services as Identity Lifecycle Management and adds this capability into the Microsoft Identity Information Server (MIIS). MIIS provides a repository that gives a unified view of directory data contained in an organization. With MIIS, you could perform directory consolidation, account provisioning, synchronization, and password management.

# X.500 and LDAP

The telecommunications industry created a standard to allow their different directories to interoperate with one another; this standard has come to be called the X.500 Directory Access Protocol (DAP). This protocol is applicable for any kind of network. The DAP standard could store information on objects from any of the seven layers of the ISO/OSI model. In X.500, a client can query a server in the directory service using DAP for its communication. The Directory System Agent (DSA) or database that stores the information then returns a response. DSAs are hierarchical and are connected to one another using the Directory Information Tree (DIT). The Directory User Agent (DUA) is a program like `WHOIS, FINGER`, or a GUI command that accesses a DSA.

### Note

Lightweight Directory Access Protocol (LDAP) and DAP compliance is performed by The Open Group (`www.opengroup.org`). For more information about X.500, go to `X.500Standard.com`. Compliance is a determination of a product's interoperability with directory service standards.

The four different X.500 protocols are used in a complete X.500 scheme:

- **Directory Access Protocol (DAP)**. DAP (X.511) defines a list of operations that a client using the full OSI model must support. These include Add, Bind, Compare, Delete, List, Modify, ModifyRDN, Read, and Search. Because there are so few networks that use the full OSI model, DAP never saw widespread use. However, a variety of LDAP directory services, such as Novell eDirectory, adopted this command set.
- **Directory Information Shadowing Protocol (DISP)**. X.500 defines two different mechanisms for replicating directory information: caching and shadowing. Shadowing is a negotiated mechanism for replicating the stored information securely, and DISP is the protocol used for the exchange and for updates. Caching stores information in a repository for later use by other users. Caching is considered to be less reliable and secure because it can store information from privileged sources that less privileged users may be able to access.
- **Directory Operational Bindings Management Protocol (DOP)**. This protocol is used to establish the agreement for data replication.
- **Directory System Protocol (DSP)**. The DSP allows a Directory System Agent to talk to another Directory System Agent or to a Directory User Agent. The protocol provides access to information without having to know where the information is located.

When computer network architects began to create directory services, they only needed to apply the X.500 to TCP/IP networks and thus could narrow the definition of X.500 to only that protocol. The resulting standard was called the Lightweight Directory Access Protocol (LDAP), although the term "lightweight" is really a misnomer. LDAP is complex but is a narrower version of X.500.

## Network Information Service

The Network Information Service (NIS) is an RPC-based client-server directory system that stores user and system names for a computer network in a database. NIS also defines a set of processes used to manage and access the diectory service. With NIS, an administrator can define an NIS domain that shares a common set of configuration files. Adding those configuration files to new systems or modifying them may be done remotely and relatively easily.

NIS is widely used on UNIX networks and was originally developed by Sun Microsystems. Originally called the Yellow Pages, a trademark dispute with British Telecom led to the service being renamed NIS. However, NIS command line commands all begin with the `yp` prefix. For example, `ypbind` enables an NIS client through RPC to access the NIS server. The command `ypserv` initiates the NIS process on the NIS server, while `rpc.yppasswdd` initiates the daemon that NIS clients use to change their passwords without having to log onto the master NIS domain server.

### Note

A tutorial on configuring NFS may be found at: `http://www.freebsd.org/doc/en/books/handbook/network-nis.html`

In NIS there are three types of systems:

- **NIS master server**. These servers can contain the files for one or more NIS domains.
- **NIS slave server**. These servers contain replicated copies of the NIS database and are used to provide both redundancy and load balancing to clients. Clients attach to the NIS server that they get the first response from.
- **NIS client**. Systems that use the NIS service for security information.

NIS stores its information in text-based tables on an NIS server. These database files are referred to as NIS maps and are stored in the `VAR/YP` directory. NIS maps are generated on the NIS master using configuration files found in the `/ETC` directory, although the `MASTER.PASSWD` file is not generated in this manner to keep it hidden. The User list is found in the `/ETC/PASSWD` directory; other files such as master, group, and hosts store other NIS information in different locations. Data in NIS may be encrypted using DES, although this method isn't as secure as more modern directory services based on LDAP offer. NIS requires that you remove system account information from the NIS accounts list before initializing the NIS map.

## LDAP servers

Today, nearly all modern computer network directory services are based on LDAP, which provides a measure of interoperability (albeit a small measure) to different vendors' implementations of this standard. Two notable exceptions are the Domain Naming System (DNS) and the Network Information System (NIS), which were both developed prior to the standardization of X.500 and LDAP.

Following are just a few of the many directory services based on LDAP:

- **Microsoft Active Directory** (`www.microsoft.com/windowsserver2008/en/us/active-directory.aspx`)
- **Novell eDirectory** (once NetWare Directory Services, or NDS; `www.novell.com/products/edirectory`)
- **Fedora Directory Server** (`directory.fedoraproject.org`)
- **OpenDS** (`https://opends.dev.java.net`)
- **Sun Java System Directory Server** (`www.sun.com/dsee`)
- **IBM Tivoli Directory Server** (`www-306.ibm.com/software/tivoli/products/directory-server`)
- **Apple Open Directory** (for Apple OS X Server; `www.apple.com/server/macosx/open_directory.html`)
- **ApacheDS** (`directory.apache.org`)

## LDAP Data Interchange Format

The LDAP Data Interchange Format (LDIF) is a text-based interchange format that allows different LDAP servers to send and receive LDAP records. Each record contains the data associated with an object and can be retrieved for directory requests or for updates. LDIF is maintained as an IETF standard and was last modified in 2000 as a proposed standard. OpenLDAP, Netscape, Mozilla, and Microsoft all have tools for importing and exporting information in this format. There are also tools such as JXplorer, which allow you to open and edit LDIF data.

### Note

To read the current RFC for LDIF, go to `http://tools.ietf.org/html/rfc2849`.

LDIF records take the following form:

```
DN: CN=Administrator,OU=departmentname,DC=servername,DC=com
objectClass: domain admin
CN: Administrator
```

where DN is the Distinguished Name, CN is the Conical Name, OU is the Organizational Unit, and DC is the Domain Component. An LDIF file contains one or more entries of this type, and may list multiple single-valued attributes. Commands such as `ADD, REPLACE, DELETE`, and so forth are embedded into the records in the following manner.

```
DN: CN=Barrie Sosinsky,OU=Writing,DC=Sample,DC=com
changetype: modify
replace: Location
Location: Room B23
-
DN: CN=Elysian Fields,OU=Evangelism,DC=Sample,DC=com
changetype: modify
add: Location
Location: Room 666
-
and so on...
```

The single hyphen line is required to separate records.

## Novell eDirectory

Novell eDirectory is an object-oriented hierarchical database that supports users and groups, roles, systems, applications, and services with global and local properties. Global and local indicate scoping (of a policy, for example) to a domain or an individual server. The database may be partitioned and uses multi-master replication. Novell eDirectory is the main competitor to Microsoft Active Directory, which is covered later in this chapter. It is also the current version of what was once NetWare Directory Services (NDS) and is currently deployed on some of the largest networks using directory services. NDS predated AD and is an X.500-based directory service.

eDirectory has a very wide range of interoperability and includes Windows, Linux, NetWare, Solaris, HP-UX, and IBM AIX clients and servers; it is reported to be deployed on as many as 80 percent of the Fortune 1000 companies.

Among the protocols that directory services use to communicate with network objects are:

- **LDAP**. The Lightweight Directory Access Protocol allows directory services to be queried over TCP/IP, as described earlier in this chapter.
- **SOAP**. The Simple Object Access Protocol is used to exchange structured XML information on the Web.
- **JDBC**. The Java Database Connectivity protocol is a method for querying databases in the Java environment.
- **ODBC**. The Open Database Connectivity protocol is an API used to create SQL database queries on Windows.ODBC and JDBC are similar technologies on two different platforms.
- **DSML**. The Directory Service Markup Language reproduces a directory service using XML.
- **JNDI**. The Java Naming and Directory Interface is a Java API that Java clients can use to query a directory service.
- **ADSI**. The Active Directory Service Interface allows clients to query Active Directory.

## Distinguished Names

LDAP directories all share a set of defined objects and a common addressing method that creates a Distinguished Name (DN) for the object. Common features of an LDAP directory are:

- **Directory tree**. The tree is hierarchical with directory objects as the nodes.
- **Nodes**. Nodes are named container objects or entities that are associated with a set of properties or attributes. LDAP allows objects to be extensible; that is, additional properties can be defined.
- **Attributes**. An attribute is a property, and its name is referred to as the type or description. An attribute can be single- or multi-valued.
- **Entries**. An entry is the unique instance of an object type. The object can be assigned a Distinguished Name, and by comparison to its parent node, a Relative Distinguished Node (RDN) may be assigned.

The DN is important because it allows the system to find and retrieve information. DNs provide a means to know how an object relates to many other objects. Essentially, they are a way of providing one-to-many relationships that aren't supported directly in directory services.

Microsoft Active Directory would use a DN in the following form:

```
/DC=<DomainName>/O=<OrganizationName>/OU=<DepartmentName>/
CN=<ServerName>
```

where DC is the Domain Component, O is the Organization, OU is the Organizational Unit, and CN is the Common Name. All of the range of possible objects within this addressing scheme defines what is called the namespace. A namespace defines the range of possible objects that your directory collects, and not any and all objects that could exist.

Because a directory service is dynamic, you can move an object from one place to another, and when you do so, the DN for the object changes. When you move Server_1's machine account from Domain_1 to Domain_2, the DN for the server changes accordingly. To ensure that an object such as this computer is easily identifiable, LDAP assigned a unique ID to a system when the operating system is installed called a Universal Global Unique Identifier (UUID).

In Microsoft Active Directory, the UUID is called the Microsoft Globally Unique Identifier (GUID) and is a number assigned to the computer when you install the Windows operating system on it. The name is chosen from a namespace containing 2122 possible numbers, or 5.3 × 1036. That is significantly larger than the calculated number of stars in the universe, which has been estimated to be 7 × 1022.

# Microsoft Active Directory

The most widely used network directory service today is Microsoft Active Directory (AD). It first appeared in Windows Server 2000 and has been upgraded with every version of Windows Server that has been released. Depending upon how you judge these things, AD is currently in its third major release.

In AD, a domain is a collection of systems that are grouped together using the Microsoft Security Account Manager database. It is a logical grouping based on a security model that applies to member systems within the same LAN, member systems located across a WAN, remote systems that intermittently log into the domain, and any other member system that can be defined and that the domain server can connect to. Any system that belongs to the domain is called a domain member, and a server is called a domain server. Any other server may be referred to as a member server, or less frequently, an application server or a resource server.

AD establishes a broad class of objects that can be managed. Users and groups are objects in the directory, and the collections of these properties, rights, and privileges are called their User and Group accounts. Computers are also objects organized by accounts, which, in this case, is called a Machine account. [Figure 21.7](ch21.html#objects_in_the_active_directory) shows the different objects organized by AD. [Table 21.1](ch21.html#sample_objects_stored_in_the_active_dire) lists the main objects stored in the Active Directory.

![Objects in the Active Directory](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2107.png)

**Figure 21.7. Objects in the Active Directory**

**Table 21.1. Sample Objects Stored in the Active Directory**

| Object Name | Description |
| --- | --- |
| Users | A security object type, a person |
| Groups | A security object type, a group of user accounts |
| Computers | A security object type, specific workstations or servers |
| Distribution Groups | Application-specific objects |
| Domain | Active Directory core collection object |
| Organizational Unit | Active Directory collection object |
| Contact | Administrator for a specific object |
| Connection | A path, usually defined for replication between two systems |
| Shared folder | Path to a file system and access to files contained within |
| Printer | Shared printer object |
| Site | A container object usually defined for a geographical location |
| Site link | A connection object between sites |
| Site settings | Objects stored related to a site |
| Subnet | A group of network addresses that are local to one another |
| Subnet container | A container object storing subnet objects |
| Trusted domain | Pass through authentication security object |

AD uses an LDAP version based on the X.500 naming scheme. The Distinguished Name (DN) in AD takes the form:

```
/DC=<OrganizationName>/OU=<DepartmentName>/CN=<ServerName>
```

where DC is the domain object class, OU is the organization unit, and CN is the conical name. Every object in AD is given a GUID, which is a unique 128-bit identifier that cannot be changed. Some objects in AD have a User Principle Name (UPN) and take the form *UserName*@*DomainName*. AD supports names in the form of UNC, URL, and LDAP URL.

AD begins with the creation of a root domain, a process that can be accomplished either through the use of the Add a Domain Wizard in Windows Server 2008, or with the `DCPROMO` command. Additional domains can be created in a hierarchy beneath the root in a domain tree. These sub-domains are considered to be children, grandchildren, and other more distant relatives of the root. Any domain that you create in an AD topology that is private doesn't need to have its name registered with ICANN for use on the Internet.

Organization units are created to separate functions, groups, or departments, or for geographical locations. An alternative designation called a site is defined when the physical characteristic of a portion of the network changes, examples of which might be a remote office or a subnet.

A collection of domains can be associated together into a forest, with each domain having its own security database. In order to allow users and systems in different domains to communicate with one another over the network, you must establish a trust relationship. Domain controllers in a forest contain information about other domains in the forest through replication. [Figure 21.8](ch21.html#the_relationship_of_forests_to_domains_a) shows the relationship of domains in a forest. A *transitive trust relationship*, as shown in [Figure 21.8](ch21.html#the_relationship_of_forests_to_domains_a), is one where if an automatic trust relationship exists between domain A and B and between B and C, then a trust relationship exists between A and C. In an Active Directory forest, this is expressed in terms of an automatic trust relationship between parent, child, and root domains.

![The relationship of forests to domains and organizational units](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2108.png)

**Figure 21.8. The relationship of forests to domains and organizational units**

The AD database stores information about a forest in three separate contexts or partitions:

- **Configuration**. The Configuration partition stores the physical structure of a forest.
- **Domain**. The Domain partition stores the topology and configuration of a forest.
- **Schema**. The Schema partition stores all of the objects and their attributes.

Microsoft has been slicing and dicing AD for the various edition of Windows. In Windows Server 2003, AD could be configured in the Active Directory Application Mode (ADAM). ADAM allows Microsoft to deploy an application such as SQL Server or Exchange on a network as a stand-alone application with a functional directory service, and without having to create a domain server on the same server running the application. ADAM added SSL and LDAP ports to these application servers, and includes its own events in the application log.

Windows Server 2008 saw the various identity and access services segmented into a set of AD role services, shown in [Figure 21.9](ch21.html#windows_server_2008_active_directory_rol), including certificate, rights management rights, federated, and domain services. ADAM was renamed as the Active Directory Lightweight Directory Services (LDS).

![Windows Server 2008 Active Directory role services](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2109.png)

**Figure 21.9. Windows Server 2008 Active Directory role services**

## Replication

Domain controllers are very active network services. Because they are considered mission critical, domain controllers are either backed up or replicated. The first version of Active Directory that appeared in Windows Server 2000 created a Primary Domain Controller (PDC) as a master, and replicated the data to one or more Backup Domain Controllers (BDCs). When the PDC went offline or needed maintenance, you could use `DCPROMO` to promote a BDC to a PDC. The system of promotion and demotion was unwieldy.

Starting with Windows Server 2003 and refined in Windows Sever 2008, Microsoft moved to a multi-master system of replicated Domain Controllers (DCs), eliminating PDCs/BDCs, to few peoples' disappointment. Now, any server that isn't a DC is a member server. The replication process replicates all of the data from the Configuration partition and the Schema partition to all DCs. The third partition, the Domain partition, is only replicated to DCs in the same domain.

Domain replication for a newly created DC can lead to significant network traffic, and is impractical for low-bandwidth WAN links. To allow for remote deployment of new DCs, Microsoft has created what they call a Read Only Domain Controller, or RODC. An RODC is a domain controller that hosts a read only version of the Active Directory database. Features of an RODC include unidirectional replication, limited credential caching, read only DNS, filter attribute set of configuration, and optimized WAN characteristics.

# Summary

In this chapter, you learned what a directory service is and why it is important. Directory services provide much of the information that a network needs to be intelligent.

Directory services create a namespace and organize a network into domains and other smaller units. A domain is a collection of systems that share the same security database.

Most directory services are based on LDAP, which is a variant of the X.500 DAP standard. You learned about some of the features that directory services enable, including policy engines, replication and synchronization, single sign on, namespaces, identity management, and Role-Based Access Control. Microsoft Active Directory was presented in some detail.

In the next chapter, you learn about network file services and how they are deployed and used.
