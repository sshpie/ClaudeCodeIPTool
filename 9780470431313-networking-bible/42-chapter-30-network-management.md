# Chapter 30. Network Management

**IN THIS CHAPTER**

- Categories of network management
- How tools can be used to track down network faults
- How events are used to determine performance
- Network management systems in use today

Network management tools are essential for a network of any size. The development of large networks in the telephone industry and the military started a process of standardization that has led to a number of standard network protocols used to manage modern networks. This chapter uses the ITU-T classification for management software called *FCAPS* to organize different types of management tools. FCAPS stands for Fault, Configuration, Accounting and Administration, Performance, and Security.

Fault management software detects specific events associated with errors and helps you determine what has gone wrong. Events can be viewed inside event viewers, and the different properties associated with each event allow you to identify them. Because faults can generate many duplicate events and lead to event cascades, determining faults is a challenging enterprise.

Configuration management software allows you to determine the configuration of different network devices, change that configuration, and save your modifications. The related topics of network software deployments, upgrades, patch management, and system lifecycles are described in this chapter.

The different factors involved in managing network event accounting, security, and performance monitoring are described. All of these topics involve trapping events of the right type and analyzing their behavior. Performance monitoring tools extend event logging to determine quantitative values and metrics that can be used to troubleshoot networks as well as optimize performance. The concept of counters and agents is explored as related to their use in measuring events.

A number of network management systems are sold that allow you to perform management functions. Some of these tools are framework applications, while others are proprietary solutions. Some of the leading products in this area are described.

# The Importance of Network Management

Network management is an issue for networks of any size. The potential problems you can encounter increase exponentially as the number of network nodes grows. As networks grow beyond the size of a small workgroup, the cost of labor involved in managing systems greatly outpaces the cost of the automated systems described in this chapter that help you manage them. Network management software therefore has a very high return on investment (ROI) and very short payback periods that are often measured in months and not years.

Unfortunately, many networks grow quite large before their owners make the connection between the cost savings that management automation can achieve and the cost of continually adding IT staff to perform tasks more or less manually. Certainly the additional $250 to $500 that management frameworks add to the annual cost of each networked computer is a barrier to their adoption, as is the tendency of each of these products to lock customers into specific technologies. Until the true costs of working without network management software are calculated, IT staff responsible for administering the network must spend an increasing amount of their working hours troubleshooting network-related problems.

In the sections that follow, some of the more important features of network management packages are considered. FCAPS, an acronym that describes the terms: fault, configuration, accounting and administration, and security has been used to standardize management packages and is considered first. These different aspects of network management are considered sequentially.

## FCAPS

Most of the standards and vocabulary in the area of network management come from the two main areas that had the earliest experience in heterogeneous networking: the telephone industry and the military.

As discussed in [Chapter 13](ch13.html), the telephone industry was a pioneer in large switched network design and maintenance. By the 1970s, the telecommunication industry, through various working groups, set about standardizing many aspects of their technologies. Some of the impetus for this work was the breakup of Ma Bell (the AT&T network) into the Baby Bells. Eventually, the network management portion of the work was consolidated in the ITU-T group of the OSI. The ITU-T group created a network management model that is often called the ISO Telecommunications Management Network model. Like its much better known Open Systems Interconnect (ISO/OSI) seven-layer protocol model, the management network model was meant to be an open system with each area of management having its own protocol set.

The acronym FCAPS was coined to cover the major areas in the ITU-T network management standard. These initials stand for:

- **F**ault. Fault management includes event logging, error analysis, error remediation, and data recovery.
- **C**onfiguration. Configuration management includes asset management, inventorying, software deployment, package management, and service and network provisioning.
- **A**ccounting and Administration. These functions include statistical reporting and integrated billing functions.
- **P**erformance. Performance management extends event monitoring to collect network system and component metrics, as well as providing software metering functions.
- **S**ecurity. Security management either installs or works with a policy engine, and can manage user and system identities either through self-contained functionality or in concert with directory services.

Although the ISO's initial concept was to create separate protocols for each of these five different areas under an umbrella that was to be called the Systems Management Overview (SMO) standard, it became clear during development that all areas could be supported by a common approach with a single protocol. From this work, the Common Management Information Protocol (CMIP) emerged as ITU-T Recommendation X.700 (`www.itu.int/rec/T-REC-X.700/en`). CMIP systems work with managed objects, each having a unique descriptor in a namespace, known as a Distinguished Name (DN). The concepts are very similar to the one for X.500 directory services (LDAP) that is described in detail in [Chapter 21](ch21.html).

CMIP is a competitor to the much more widely used IETF Simple Network Management Protocol (SNMP) standard, but CMIP has many more capabilities than SNMP. CMIP includes a number of different actions in the form of verbs or commands that modify managed network elements. SNMP, in contrast, only allows you to change the state of a managed element through the use of a `SET` command. `SET` is essentially a `WRITE` operation to an object value. The reason that SNMP is so widely known and CMIP is not is that most networked devices on TCP/IP networks come with SNMP support. SNMP hardware benefits both from economy of scale and by being less complex; it is also cheaper to implement, making them cheaper to fabricate and deploy.

### Note

SNMP is described in detail in [Chapter 4](ch04.html).

Systems management has had a long history within the computer industry and there are many standards that apply to managing desktops, deploying systems, and other management tasks. You've already seen some of these management protocols, such as SNMP and WEBM. Here are some other protocol standards that you might encounter:

- NETCONF (`www.ietf.org/html.charters/netconf-charter.html`), which, like SNMP, is an IETF standard
- Common Information Model (`www.dmtf.org/standards/cim/`), WS-Management (a SOAP protocol; `www.dmtf.org/standards/wbem/wsman`), and SMASH (Systems Management Architecture for Server Hardware; `www.dmtf.org/standards/smash/`), all of which are DMTF standards or initiatives. The Desktop Management Interface (DMI; `www.dmtf.org/standards/dmi/`) standard is another DMTF framework for PC management but has been deprecated in favor of the newer CIM standard.
- JMX (Java Managed Extensions; `java.sun.com/products/JavaManagement/`), which is a Java initiative for managing network objects (MBeans or Managed Beans)

There are many more protocol standards that are either industry specific or so poorly known that they are not worth mentioning here.

While FCAPS isn't nearly as well known as the seven-layer ISO/OSI networking model, FCAPS is a convenient organizational scheme for describing the different functions of network management. The sections that follow are named after the FCAPS model, after which some examples of network frameworks are considered.

## Fault management

A fault is an error in hardware or software that leads to an undesired result. The goal of fault management is to identify when a fault has occurred, isolate the cause of the fault, and provide the necessary information so that you can remediate the cause of the error. Most operating systems and applications are great at producing error reports, and fault management systems are also great at capturing and displaying errors. What they are not great at is helping you determine the exact nature of what has gone wrong.

Fault management systems work by detecting specific events that are associated with error conditions or by determining a fault from a collection of events. All modern network operating systems and their desktop counterparts are event-driven; that is, the software sits in a wait state until it receives a command that it needs to act on. Some events are maintenance items, others check memory integrity, and so on. Events are typed and may be trapped selectively, with the ones of interest logged to an event log (usually a database file) and/or sent over the network in a standard Application layer protocol such as SNMP, or for some vendors, in a proprietary protocol. The isolation and understanding of events of different types is the first line of defense in any fault management routine.

In the next sections, you learn about how events can be logged, how events can trigger alarms based on conditions, and how analyzing events is your first line of defense in solving problems and optimizing your network.

### Event log files

[Figure 30.1](ch30.html#the_windows_event_viewer) shows the Event log for a Windows Vista 64 system, with an error event in the System log highlighted. Different operating systems come with a core set of events that are very similar to one another, although different names are used. The Windows Event Viewer is representative of this class of utilities. Notice that each event has an associated set of properties, an EventID or Reference Type, Date and Time, Source, and the name of the log file the event was recorded into. Because there are so many events, all event viewers allow you to set filters that control the particular events that are viewed. Although the Event Viewer here shows a local view, you can also use this utility to log onto a remote system and view that system's various event files.

### Tip

Error IDs, their descriptions, and other properties that network operating systems and applications disclose are often described in technical notes on the Web sites of the vendors who create them. Often the best way to determine what an error means is to simply Google these terms.

![The Windows Event Viewer](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3001.png)

**Figure 30.1. The Windows Event Viewer**

This particular Event Viewer is a Microsoft Management Console (MMC) component and can be launched either as a stand-alone utility or, as is the case with Windows Server 2008, within the Server Manager console (described later in this chapter).

Different versions of UNIX and Linux store their events into either a `MESSAGES` or `SYSLOG` file, which can then be viewed with different command line and GUI tools. In Ubuntu, by default, the System logs are found in the `/VAR/LOG` directory, which includes the `SYSLOG, DMESG, KERN.LOG`, `DAEMON.LOG`, and other log files. Provided you have Monitor system log privileges, you can use the System Log Viewer in Ubuntu to open a utility that looks very similar to [Figure 30.1](ch30.html#the_windows_event_viewer). These log files are stored as delimited text, and so you can open a Terminal session and use a reader command such as `GREP` to view the contents of the individual files.

There are two types of event trapping systems: counters and agents. Counters are built into an application or operating system by its developers, while agents are lightweight executables that are installed by other programs to monitor counter values. As a general rule, counters run with higher privileges and have lower-level access to event information than agents do. However, a well-executed network management package such as Altiris will install a local agent on a system that is low level and difficult to remove. In either case, the data being captured by a counter or agent should be identical.

Counters and agents are not only used to `READ`/`WRITE` to event logs but also provide empirical data that is used to measure performance. Because event viewers are strictly viewer applications, you don't have control over counters and agents from within an event viewer application. To alter how events are monitored, or if they are even monitored at all, you need to work within performance monitoring applications, which are covered later in this chapter.

### Alarms

In addition to detecting faults, fault management functions will also create alarms. An alarm is a detected error condition that may be categorized in terms of type and severity and logged to a database or sent out in some form of notification. Because error conditions are detected by the appearance of an event alarm, management systems are just another form of event viewer with filters for types of events, and some rules on how to handle events of the type being monitored.

When the device or system function automatically sends out an alarm, the system is referred to as a passive management system. When a program is polling devices listening for a "heartbeat," a response to a `PING` for example, that system is an active management system. Depending upon the system function and the manner in which the network management package is written, its functions can be either active or passive, or both.

Alarms may be categorized as being either analog or digital. A digital alarm is a binary system with two states: `ON` or `OFF`, 1 or 0, or `TRUE` or `FALSE`. The 1 or 0 value is what is actually stored in the alarm register, and what you see is simply a function of how you format the output. A register is simply an address in memory that can be referenced and contains a value related to some variable. In some rare instances, binary alarm management systems supply a third value, which either appears as `NULL, NA` (for Not Available), or simply leaves the output display blank. Many database applications handle binary fields in this manner.

An analog alarm is one that can take a range of values. An example of an analog field might be one that measures dropped frames. Analog alarms have a value property that can be any number in its range, or if no range is defined, any value at all within the limits of the number of numeric places supported by that alarm's register. You may find that the management application that you are working with allows you to set individual portions of the range in a manner similar to this:

- Low-Low: 0 – <20 percent
- Low: 20 – <35 percent
- Middle: 35 – <65 percent
- High: 65 – <80 percent
- High-High: 80 – 100 percent

Because analog values are generally more useful with performance metrics, they tend to provide rates or quantities, such as number of frames dropped per second or number of nearest neighbor routers that respond to a discovery command and are often built into performance monitoring tools.

Alarm management applications are most often put in place because they flag faults that need to be corrected. Therefore, these applications most often come with a notification feature. There are a wide variety of methods used to notify other applications about an error condition: the error may be displayed in a GUI application such as an Alarm Human Machine Interface (HMI) console, the alarm may generate an SNMP event that is sent to another application, the alarm may be placed inside an e-mail and sent using SMTP to a mail server, or the alarm may be sent as a fax (old school) or as an SMS text message (nu schl).

### Event correlation

Fault management packages must be written in such a way that they can recognize when many events are all caused by the same error condition, a process referred to as event correlation. In any system where a fault or error has occurred, it is uncommon for only a single error event to be generated. For example, if an action requires access to a USB device and that connection has failed, the system may attempt to contact the device many times over the action's timeout period, generating an error event each time. It is not useful to have a fault management system report hundreds of error events when in reality there is only one error being described. Nearly all fault management packages will suppress or summarize duplicate error events so that meaningful data is presented to the user.

The engine that performs the analysis of event correlations is called the event correlator, and these systems can rise to the level of being artificial intelligence systems. The four common stages of an event correlation are:

- **Filtering**, discarding irrelevant events.
- **Aggregation**, or event de-duplication, which removes duplicates of the same event.
- **Masking**, which results in hiding events that are the result of an error and do not pertain to the actual error. Some references refer to this function as topological masking.
- **Root Cause Analysis (RCA)**, which is the methodology that uses event dependencies to create an environment model that allows for the error's ultimate explanation to be exposed. A root cause analysis will result in information such as "disk XXX is full" in place of "disk `WRITE` to XXX fails," for example.

Many event correlation systems are bundled into help desks and work in concert with what is called a Trouble Ticket system, or alternatively, an Incident Management (IcM) system. When an error is detected, it is assigned an ID; a ticket is then entered into the database and logged. As information regarding the error is determined, it is added to the database until an explanation or fix is uncovered. These systems often have status assignments that allow organizations to use them in project development. They are as useful in network management as they are in software development projects.

More problematical is the situation where a fault gives rise to an event cascade. Returning to the errant USB device, let's assume that the device is a USB key with a file stored on it that must be used by another program. That program sends out a `READ` command for the file, which the operating system redirects. After multiple attempts, the file can't be accessed and the whole process begins to generate multiple distinct errors in the system's event log. The cause might be the key itself, or a damaged USB port, and the USB bus reports the error. As the error moves up the food chain, a cascade of related error events are generated. The operating system can report errors, the application can report errors, and so on. All these errors relate to the same fault, but because they all appear in an error log, it is left up to you, gentle user, to figure out the cause of the pattern.

The more sophisticated a fault management package is, the better that package is at parsing the related errors and defining the underlying fault. Even the most discriminating management package will often present the user with multiple related errors that will need to be put into context in order to determine the ultimate cause. So my advice to you, if you are ever in the position of having to evaluate one network management package over another, is to focus on how well the package handles event cascades and duplications as one of the key differentiators of performance, and how well it is able to translate that ability into ascertaining the relationship between events and causality.

## Configuration management

Configuration management refers to the tasks involved in managing the configuration and identity of systems and users on a network, as well as attending to modifications that may be needed.

Tasks that fall under the banner of configuration management are:

- Setting up computers and network devices
- Installing and configuring software, known as software configuration management (SCM)
- Managing the different users and groups on a network, including their accounts and roles
- Updating and patching software and systems as required
- Provision of dedicated network connections
- Documenting the configuration of all of these network components

The goal of configuration management is to set up systems to automate repetitive tasks, reduce complexity by requiring a set of standards, and actively monitor systems for conditions. One way that you can reduce complexity to make configuration management easier is to set reference standards for the hardware and software that you allow to run on your network. A standard system that's been tested and certified forms a reference platform that may be rolled out (duplicated or cloned) and reduces much of the work involved in individual system configuration.

Most system management packages use consoles to monitor and manage networks. The next section describes some of the more common aspects of consoles. A key management task is to manage network system lifecycles, which is the topic covered after the discussion on consoles.

### Consoles

Local configuration management is an onerous task, and so most management solutions are remote solutions, preferably performed in a centralized management console or dashboard. This dashboard feature has long been a staple of management framework applications, but is found now as a management feature in operating systems as well. As Microsoft has continued to develop their MMC technology, they've been able to consolidate most of the utilities for networked system management within a saved console on Windows Server 2008 called the Server Manager, an example of which is shown in [Figure 30.2](ch30.html#the_windows_server_2008_server_manager_i).

The structure of the Server Manager display collapses the view from dozens of tools to the hierarchical tree control in the left pane of the window, letting you manage your local and remote systems from one place. When you highlight a tool such as the Reliability Monitor, it is displayed in the central panel of the console, and although it isn't shown in this particular figure, when a tool has available options, a third panel on the right appears with the appropriate commands. Using the Server Manager, you can have several of these tools open at a time, such as the Active Directory configuration utility, the Policy tool, and others, and save the configuration for later use.

![The Windows Server 2008 Server Manager is an MMC framework application that helps bring order to chaos.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3002.png)

**Figure 30.2. The Windows Server 2008 Server Manager is an MMC framework application that helps bring order to chaos.**

While other features in Windows Server 2008, such as PowerShell, may turn out to be more important in the long run, from an administrative point of view, no other feature will have more impact than the consolidation of utilities within the Server Manager. It isn't that this console view is unique or even that it breaks new ground, but simply that it is both comprehensive and part of the OS that will ensure its use.

A central console is an enormous time saver, and the care and quality of such a console is a desirable feature in any management tool. All of the network frameworks described later in this book provide a container application such as the MMC into which applications may be installed. Some of these management packages are closed and proprietary, but many framework vendors publish their APIs, thus allowing third parties to create modules for the framework.

### Note

Microsoft publishes the interface for creating MMC snap-ins: `http://msdn.microsoft.com/en-us/library/ms692755(VS.85).aspx`.

### Software lifecycles and deployments

All software and hardware have lifecycles during which they are useful, and after which they are not. The goal of configuration management is to ensure that the lifecycles of network components are as long as they are practicable, and to maximize the utility of systems during their lives.

Systems — which include both hardware and software — progress through a set of six common conditions or states. The sections that follow consider these stages in order from the start of the system's life to the end. All of these stages make different requirements of configuration management software, and while each management package handles configuration differently, there are some universal themes that may be associated with each stage. Deployment technology — also referred to as electronic software distribution (ESD), desktop management, or automated software delivery — is the number one requested feature in network framework technology. If this functionality isn't in the base framework package, it is usually the first add-on module that is purchased for use.

#### State 1. Systems are newly acquired and current.

In State 1, the management package must add the acquired system to its inventory and be capable of monitoring the system. If the acquired system isn't purchased as a completely installed system, management software must be able to configure the system as described in State 2. In this stage, a management package must be able to install an agent and register the various properties of the system into an asset database. Among the many properties that might be stored for view are:

- An asset ID tag or software license number
- The serial numbers and types of components associated with the system
- Specific model or product names, as well as their version numbers
- Assigned values such as system names stored in a directory service

Not all management frameworks ship with full accounting and inventory modules; in some systems, this is an add-on module that must be purchased later. However, all management frameworks require some means of identifying systems in order to be able to identify systems that are to be deployed or upgraded. Not all systems must be managed, and it may even be desirable from a cost or security standpoint to isolate non-managed systems from outside monitoring.

#### State 2. Systems are in inventory or to be deployed.

Configuration management software can create and store system states, either in the form of installable software packages of some type, or for complete computer systems as an installable container file that is referred to as an image file. Most people are familiar with various image files, and they come in a wide variety of forms. The best-known image files are ISO files, the name being taken from the International Organization for Standardization. ISO files are sometimes called archive files or disk images and their definition arises from the manner in which the ISO 9660 file system on CD-ROMs was organized. The 9660 file system has been replaced by the Universal Disk Format (UDF; ISO/IEC 13346 or ECMA-167), which is maintained by the Optical Storage Technology Association (OSTA) for use on all sorts of optical media.

Other image file formats include Microsoft Windows Imaging Format (WIM) files, Symantec's Ghost (from General Hardware Oriented System Transfer) GHO files, Acronis True Image Server, and many more. All of these file formats have as their properties the same general concept: they store an index that you can browse that describes the contents of the individual files/directories/drives that the image contains, and the data is stored either in its native form (and can therefore be directly copied) or as a compressed version that must be extracted to recover. Because images are containers, most utilities allow you to add additional content or remove files, thus providing for drive snapshots, custom installations based on some subset of the files contained in the image, and other features. [Figure 30.3](ch30.html#acronis_true_image_tib_files_are_disk_im) shows an Acronis TIB file, Acronis's native True Image Backup file format.

The use of image files for system installation has had a very interesting effect on the manner in which Microsoft is now distributing its different versions of Windows. In Windows prior to Windows Server 2008/Vista, different versions of Windows would require separate builds and installation media. Starting with 2008 and going forward, Microsoft consolidated all of the files into a WIM container file, and through user selection of the version type, one build served all with great economy.

Image files are not only used by backup utilities, but they are also at the heart of all deployment utilities. In a tightly managed network, organizations acquire systems and validate configurations that they are willing to support. Those reference systems are then deployed onto the network. A reference system may include a number of feature restrictions designed to narrow the number of support issues that network IT staff must deal with, such as the following: support for only certain hardware and software; lockdown of user privileges and desktop features; and restrictions on what may be installed. Deployment typically takes place by supplying a script to the system that points to the image on a network share and provides whatever automation is required.

![Acronis True Image TIB files are disk image container files and can be used for backup and recovery, disk cloning operations, and deployments.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3003.png)

**Figure 30.3. Acronis True Image TIB files are disk image container files and can be used for backup and recovery, disk cloning operations, and deployments.**

Microsoft distributes a set of network deployment tools under the name of Microsoft Deployment Toolkit (`www.microsoft.com/downloads/details.aspx?FamilyID=3bd8561f-77ac-4400-a0c1-fe871c461a89&displaylang=en`) that is packaged as a framework solution. With this tool, you can deploy Windows Server 2003/XP and Windows Server 2008/Vista images customized with appropriate drivers, Windows update packages, and service packs, and with Microsoft Office or other applications installed. This toolkit is an excellent means for learning about deployment technologies, and many of the lessons it teaches are applicable to the other network management framework deployment packages that are available.

The deployment tools that are part of this package include the following:

- **Application Compatibility Toolkit**, which compares applications with a compatibility database.
- **Microsoft Assessment and Planning**, which compares hardware with the Hardware Compatibility List.
- **Microsoft Deployment Workbench**, a browser-like interface to all of the tools and to reference resources such as white papers on best practices.
- **Windows Automated Installation Kit (WAIK)**, a set of tools for creating and deploying system images, which includes the Windows System Image Manager for managing an image library; ImageX, a command line utility for creating images; Windows Preinstallation Environment (Windows PE); and User State Migration Tool (USMT) for capturing user profile information.
- **Windows Deployment Services**, a new version of the Microsoft Remote Image Server.

[Figure 30.4](ch30.html#the_windows_system_image_manager_tool) shows the Windows System Image Manager tool. This tool allows you to select system images in the Windows WIM format, customize those images with drivers and installation packages, build "answer files" (which are the scripts needed to run automated Windows installations), and set the network shares that serve as the distribution shares for network installation.

![The Windows System Image Manager tool](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3004.png)

**Figure 30.4. The Windows System Image Manager tool**

Once configured under the Microsoft Deployment Toolkit, images can be scheduled to be rolled out using either what is called a Zero Touch (automated with no user intervention or user interaction) or Lite Touch (set up manually for deployment upon request by an administrator) deployment method. The images you create can be deployed using Microsoft System Center Configuration Manager 2007, or the older version of this management framework package, Microsoft System Management Server 2003 (SMS).

With hardware support, all late-version computers support what is known as the Preboot Execution Environment, or PXE. In a system configured to boot to PXE and enabled in the BIOS to do so, a computer will boot up into a very minimal operating system and begin a discovery process for a PXE server over the network. If the system discovers the PXE server, they exchange credentials and begin a process by which the entire system image is sent over the wire from server to client. PXE is used in thin client-server applications, but it can also be used to remotely deploy a disk image to a computer system.

### Tip

If your intent is to bring a system back to the same state after a user has completed their session, there are better methods to refresh a system than doing an over-the-wire restore from a system image. Consider using a tool such as Windows SteadyState (`www.microsoft.com/windows/products/winfamily/sharedaccess/default.mspx`) or Faronics Deep Freeze (`www.faronics.com/`). Doing so avoids having to service all of the traffic involved in moving gigabytes of data about the network.

Configuration management software may aid in testing and validating standard system reference images, managing image libraries, and performing remote installation of these images across a network.

#### State 3. Systems are aging and must be monitored.

As systems age, configuration management software not only provides the ability to allow for asset management (as described later in the chapter), but it also allows intelligent decisions to be made based on the age, utilization, license requirements, and performance of these systems. There are a large number of network monitoring packages available on the market to service this particular function. Among the important features of a monitoring package are:

- Device auto discovery (almost all monitor programs use SNMP) and mapping
- Agent deployment and distributed monitoring
- Event logging, triggers, and alerts
- Trend data, charting, reports (including Service Level Agreement, or SLA), and prediction
- Inventory
- License compliance
- Scripting and extensibility through plug-ins
- Web interface

Different packages support different sets of the features in the list above.

### Note

A jump page comparing a number of different network monitoring software systems is maintained at `en.wikipedia.org/wiki/Comparison_of_network_monitoring_systems`. Another jump page for network monitoring tools may be found on the Stanford SLAC Web site at `www.slac.stanford.edu/xorg/nmtf/nmtf-tools.html`.

#### State 4. Systems require a patch or minor upgrade that must be applied.

While there are many different systems for applying system patches, application upgrades, or full service packs, many organizations simply allow their users or systems to automatically update themselves. However, patches, upgrades, and any software that needs to be deployed slipstream into a production system are best configured using a policy engine. With a policy engine, you can set rules that determine who gets which software and when, and you can script or automate these upgrades as network installations. In carefully managed systems, any software upgrade is tested before deployment.

#### State 5. Systems are obsolete and must be significantly upgraded.

The computers produced over the last few years are often significantly more powerful than the original operating system that they shipped with required. Therefore, it is certainly possible that as the system ages, updating the system contains additional value that a networked organization can capture. There are three different methods used for upgrading systems:

- **Bare Metal**. This is a fresh installation onto a system that removes all previous data.
- **In-Place Upgrade**. The system is upgraded by a new version installed over the old system. For most network operating systems and applications, in-place upgrades are supported if the version difference isn't too great. This upgrade retains user settings.
- **Side-by-Side Upgrade**. In a side-by-side upgrade, applications and settings are migrated from the old system to a system containing a newer version of the operating system. This is the most difficult upgrade to perform.

As a general rule, bare metal installations create the cleanest, most stable system but do not preserve the investment the user has in their system's configuration. In-place upgrades are a reasonable compromise that creates a workable system that may require additional work to eliminate faults. Side-by-side upgrades are the most difficult to achieve and require special software that compares applications to a database of known good, compatible versions.

In Microsoft's deployment technology, the Application Compatibility Toolkit (ACT) performs this application validation function. ACT works by deploying a set of agents on systems that will be upgraded, and collecting system information. That information is then collected and compared at a management console, which is populated with information from the online Microsoft Compatibility Exchange service. That service also provides a resource that can be used to obtain additional information about compatibility, as well as discuss online with other professionals experiences that they are having. Microsoft System Center Operations Manager (SCOM) may be used to deploy ACT agents and to manage this process.

[Figure 30.5](ch30.html#microsoft_act_is_an_agent-based_network) shows how ACT works in concert with Microsoft's Compatibility Exchange operating through a network framework management console. In [Figure 30.5](ch30.html#microsoft_act_is_an_agent-based_network), systems on a LAN/WAN have a set of agents deployed on them: inventory, user settings, browser, and others. Those agents report on the condition of individual systems and send the data in XML format to a Log Processing server, which stores the data in a SQL database. The data in the database is used by the Application Compatibility server to determine in concert with the Microsoft Compatibility Exchange service what steps must be taken to correct deficiencies.

![Microsoft ACT is an agent-based network inventory system that can work with Microsoft System Center, and which is used to check application compatibilities for upgrade deployments.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3005.png)

**Figure 30.5. Microsoft ACT is an agent-based network inventory system that can work with Microsoft System Center, and which is used to check application compatibilities for upgrade deployments.**

System upgrades are, like any operating system deployment, installable over a network using network management tools. However, unlike fresh installations, system upgrades often require network tools to capture, store, and restore the customization and personalization settings as well as user data from the old system to the upgraded system. These settings are a "user state," which is not only the user's profile (in Documents and Settings on a Windows system, for example) but also their data. When a system is multiuser, you need to capture multiple user states. Microsoft's deployment technology uses a command line tool called `SCANSTATE` to capture user states, and a complementary tool called `LOADSTATE` to restore state data.

#### State 6. Systems are obsolete and must be replaced.

The last stage is the recognition that a system is no longer useful. Systems that are at the end of life may find use in less demanding applications such as a router, a PBX, or some similar applications. Some systems may also be useful to others, while some simply need to be discarded.

## Accounting and administration

The accounting function in network management tools refers to the measurement of usage data for the purposes of billing customers or departments, ensuring that services are being distributed fairly, or validating that an organization has met its Service Level Agreements (SLAs) for network services. Accounting services rely on trend data supplied by performance-monitoring tools with the additional ability to determine which users or groups are either responsible for or the beneficiary of that particular activity.

Examples of common network functions that are collected for billing purposes are:

- The amount of data flowing through a connection
- The number of particular events related to an activity such as creating a remote connection
- The amount of a particular network resource, such as a shared disk, that has been consumed
- Peak usage rates

Accounting functions are built into a number of different protocols, including RADIUS, TACACS, and Diameters, all of which are referred to as AAA services. AAA, as you will learn in [Chapter 30](ch30.html), stands for Authentication, Authorization, and Accounting. RADIUS, for example, is a connection protocol that stands for Remote Authentication Dial-In User Service and is used by ISPs, e-mail services, network access points, Web servers, and many other network functions where security and accounting operations both need to be performed. AAA servers typically pass some functions, such as authentication, through to other network services.

Accounting is available in many network framework products, although typically this function is purchased as an add-in module and is not part of a core product that you might buy from a vendor. The exceptions to this rule are network framework products that service industries such as the ones mentioned previously.

Because many networks do not require an accounting function, the term *administration* has been used as an alternate function to satisfy the FCAPS acronym. Administrative functions would include the management of users and groups, setting access to resources, and providing access to important network functions, such as setting policies, running backup or replication, managing backups, and configuring storage, among other tasks. The different administration functions in network framework tools vary considerably, and there is some overlap in the administrative function with other areas in FCAPS, such as security and configuration.

## Performance management

The goal of performance management is to establish how a network performs under standard conditions as well as providing the means needed to optimize performance. The measurement of network performance establishes a baseline against which future changes can be compared. Performance monitors extend the use of counters and agents to quantitatively measure the information that these systems provide. The data collected by performance monitors can measure a very broad set of variables that affect the network. Here are some of the more important functions of a performance monitor:

- Network traffic as a function of the protocol used
- Network loading and throughput by node or segment
- Collision rate
- Frame error rate
- Network traffic as a function of node

The key to working with performance monitors is to understand the use of counters. Counters play an essential role in operating system development. When developers "bring up" an operating system, the counters that they add to the different modules of the operating system provide the developers with immediate feedback on the impact of the changes in the programs that have been made. So in addition to trapping and recording events, some event types are measured for frequency, duration, value, or whatever parameter is most useful to understand the particular subsystem that the counter monitors. For CPUs, you will find counters such as processor utilization, processor queue length, processor time, and so forth; for disks, you will find counters such as disk accesses, amount of data transferred, queue length, and so forth. When you open a performance monitor application, and each operating system has one, the data you see is based on counters. Any application that has been performance optimized has a set of counters that were used, and so counters are found in most enterprise-class applications such as large databases.

In [Figure 30.6](ch30.html#to_measure_different_aspects_of_system_a), the Windows Performance Monitor's Add Counters dialog box is shown. Many objects whose performance is of interest, such as network interfaces, offer numerous measured parameters that their counters are able to supply. Counters you add show up as charts in the Performance Monitor.

If you have worked with a performance monitor tool, then you know that you first select the counters to observe from what is usually a long list organized by class, and then wait for the data to populate the tool. Different operating systems give their counters with different names, and expose different sets of installed counters, although the concepts being used are nearly the same. Many counters are not exposed to users because they impact system performance when they are turned on. For example, Microsoft doesn't expose some of their disk counters, and if you are interested in those particular counters, you must first know about them and then install them. Different application vendors have different policies on the use of their counters: some expose them, others don't, and unfortunately, many application vendors don't go to the trouble of optimizing their products and therefore may not have any counters to offer. To learn more about counters, you will need to do a little research on the particular product of interest.

![To measure different aspects of system and network performance, you need to add the counters to performance monitor tools.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3006.png)

**Figure 30.6. To measure different aspects of system and network performance, you need to add the counters to performance monitor tools.**

Performance studies using performance monitors can be an invaluable tool in determining network and system faults. The clearest picture is obtained by considering event types as well as event metrics. Broadly speaking, network management tools are either an event monitor or a performance monitor; a few are both. Every network operating system ships with a performance monitor. Windows performance monitor `PERFMON` is an MMC snap-in that can be launched as a stand-alone utility, as a component of the Task Manager (the utility you see when you press the Ctrl+Alt+Del keystroke), or as part of the Reliability and Performance Monitor, shown in [Figure 30.7](ch30.html#windows_vista_apostrophy_s_reliability_a), that shipped with Windows Server 2008/Vista.

One particular class of network-performance monitoring tools are sniffers. These tools are known by a variety of names: packet analyzer, network analyzer, packet sniffer, Ethernet sniffer, or protocol analyzer. A packet sniffer intercepts traffic flowing over a network so that the contents may be read and analyzed, and possibly written to a log file. A packet sniffer can also decode the contents of the packet and categorize the nature of the protocols used.

### Warning

Packet sniffers are the weapons of choice for many hackers. When you deploy them, you need to ensure that unauthorized personnel do not get access to these tools running on your network.

![Windows Vista's Reliability and Performance Monitor includes the PERFMON tool, as well as fault management (reliability) tools.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3007.png)

**Figure 30.7. Windows Vista's Reliability and Performance Monitor includes the `PERFMON` tool, as well as fault management (reliability) tools.**

Packet sniffers can be configured so that they intercept traffic on a segment, at a switch port on a router or host, or on what is referred to as a monitor port. A monitor port takes all incoming packets to a switch and duplicates them, sending the originals onto their destination while capturing the duplicate packets for analysis. In the case of wireless networks, Wi-Fi sniffers usually capture the traffic on an individual channel. Packet sniffers are among the most widely used performance-monitoring tools available; they can be used for a range of tasks, including:

- Network fault analysis
- Detecting security breaches
- Gathering network usage statistics, creating reports, and optimizing performance
- Determining the protocols in use, and rule-based packet filtering
- Capturing sessions

There are a number of packet sniffers that you can download; most are distributed freely. Microsoft Network Monitor (`NETMON`; `www.microsoft.com/downloads/details.aspx?familyid=f4db40af-1e08-4a21-a26b-ec2f4dc4190d&displaylang=en&tm`) is perhaps the best-known sniffer used on Windows. Kismet, tcpdump, and Wireshark are available for Windows, Mac OS X, Linux, BSD, and Solaris. Sun distributes the utility `SNOOP` for packet sniffing on Solaris.

A high-end commercial packet sniffer is WildPackets OmniPeek (`www.wildpackets.com/`), a network server (hardware) and software package. OmniPeek comes with a plug-in API that allows network monitoring to be automated. OmniPeek starts at $1,200 at the time of this writing, and with plug-ins, it can remotely monitor Cisco switches and access points, Linux hosts, and other vendors' network devices. Hardware appliances of this type are sometimes referred to as network management systems (NMS).

[Figure 30.8](ch30.html#microsoft_network_monitor_is_a_packet_sn) shows a session being captured inside Microsoft Network Monitor. The frame on the left shows the different endpoints of network traffic, while the central frame on the right has the data from the actual packets. Network Monitor can run in what is called promiscuous mode, where the complete contents of a packet can be viewed.

![Microsoft Network Monitor is a packet sniffer that you can use to evaluate traffic on your network.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/3008.png)

**Figure 30.8. Microsoft Network Monitor is a packet sniffer that you can use to evaluate traffic on your network.**

## Security management

The security management function in network management tools provides the means to allow or deny access to networked resources to users and groups. Most network operating systems include security management as part of the operating system, and so for those operating systems, security management software provides a means of accessing and modifying operating system settings. This may mean that the utility provides a view of important network settings stored in directory services, access to environmental variables on systems, and other functions. For network systems that don't have directory services, the security management utility may provide the entire service.

Network security relies on two important functions: authentication of users and systems, and protection of data traveling over the network through the use of methods such as encryption. Security management software may create a key-based infrastructure, be an encyptor/decryptor, or perform other functions that allow these services to be performed. Another important category of services that security management software provides is risk assessment and risk analysis.

# Network Management Software Categories

A network management framework refers to a form of system management software package that is used to integrate different categories of network utilities under a common user interface and with a common application API. The framework supplies the necessary services, such as remote agent deployment and network communications, that enable the applications to function. Some frameworks are proprietary and closed, and others are extensible and open. Most framework applications are sold in different configurations or "levels," which usually include a base or core functionality along with an a la carte menu of potential add-ons.

Pricing for these systems is highly variable and can include a base system cost, based on the number of consoles or management servers deployed, client licenses based on the number of seats, or nearly any pricing scheme that you might imagine. Because many of these installations are customized for the organization that purchases them, many network management framework vendors do not advertise pricing, and quote custom pricing on a per-job basis.

Because a framework application is designed to be customizable and therefore accommodate many different types of applications, describing the functionality of the category is similar to describing the different types of software that run under any network operating system. In some respects, a network framework is similar to a network operating system, except that a network operating system operates at all levels of the network model, whereas a network management framework is an Application layer system with elements such as remote agents and transport protocols operating at the Network layer and above.

In the list that follows, I've tried to order the different network system management functions that are typically available in the market-leading products in the order from most commonly deployed functions at the top to least commonly deployed functions at the bottom. The list has another very important characteristic that it defines: The higher up on the list a function is, the more likely it is that the function is included in the core or base network framework product. The lower down on the list a function is, the more likely it is to be purchased as an add-on module at additional cost.

The system management functions found in framework applications are:

- User and system activity monitoring
- Network resource utilization monitoring
- Asset management and inventorying
- Operating system and software deployments
- License compliance
- Backup management
- Anti-virus and anti-spyware monitoring
- Storage management
- Security management
- Directory services management

# Network Frameworks

A network framework is a design specification based on published APIs (Application Programming Interfaces) that are used to create software that can be run in a similar manner or in a similar environment. With systems such as Microsoft .NET Framework or Sun's Java, the framework refers to a set of libraries, utilities, methods of programming or scripting, and other elements that are used to construct a software module. Vendors often publish the APIs for their frameworks in the hopes that developers will create applications that are useful for customers.

The Microsoft Management Console (MMC) is an example of a framework application where the goal is to provide a common interface into which modules called snap-ins may be placed so that the MMC can be configured to provide a console appropriate to the type of management or configuration that an administrator needs to do.

[Table 30.1](ch30.html#network_management_packages) lists some of the better-known and widely used network management packages in an approximate order in terms of their market share:

- Hewlett-Packard OpenView
- Microsoft SMS/Service Center Manager
- Novell ZENworks
- BMC Patrol
- IBM Tivoli Framework
- CA NSM (formerly Unicenter)
- Avocent LANDesk
- Symantec Altiris

### Note

Hewlett-Packard's OpenView has gone through a couple of rebrandings over the last few years. The products are now part of a group of products under Hewlett-Packard Software and Services, but the names and functionality of the products remain the same.

Some of these management frameworks have a very long history to them, and support large numbers of related applications: OpenView and Tivoli are notable in this regard. Space precludes a full description of all of the tools that are available for these products, but if you want to get a sense for the range of functionality that can be managed within a network management framework, take a look at their descriptions on the Web sites noted in [Table 30.1](ch30.html#network_management_packages).

**Table 30.1. Network Management Packages**

| Product Name | Owner | FCAPS | Platform | Reference |
| --- | --- | --- | --- | --- |
| FCAPS stands for the following: F = Fault Management, C = Configuration Management, A = Accounting and Administration, P = Performance Management, and S = Security Management. |  |  |  |  |
| Altiris Management Suite | Altiris | FCAPS | Proprietary | `www.symantec.com/business/theme.jsp?themeid=altiris` |
| CA NSM (formerly Unicenter Network and Systems Management) | Computer Associates | FCAPS | Proprietary | `www.ca.com/us/system-management.aspx` |
| CiscoWorks LAN Management Solution | Cisco Systems | FCAP - | Proprietary | `www.cisco.com/en/US/products/sw/cscowork/ps2425/index.html` |
| IBM Director | IBM | FC - - - | Proprietary | `www-03.ibm.com/systems/management/director/` |
| KACE | KACE Networks | - CA - S | Proprietary, uses SNMP, WMI, and PXE | `www.kace.com/` |
| LANDesk Management Suite | LANDesk | FCAPS | Proprietary | `www.landesk.com/` |
| NetDirector | Emu Software | FC - - S | Proprietary, XML-RPC | `www.netdirector.org/` |
| Netrac | TTI Telecom | FC - P - | Proprietary | `www.tti-telecom.com/` |
| OpenView | Hewlett-Packard | FCAPS | Proprietary | `www.managementsoftware.hp.com/` |
| PATROL | BMC Software | - CAP - | Proprietary | `www.bmc.com` |
| Realité | SMILabs/Digital Zone | - CA - S | Proprietary | translate.google.ru/translate?prev=_t&hl=en&ie=UTF-8&u=http%3A%2F%2Frealite.ru%2F&sl=ru&tl=en&history_state0= |
| Spiceworks IT Desktop | Spiceworks | F - A - - | Open source | `www.spiceworks.com/` |
| System Center Configuration Manager (formerly Systems Management Server, or SMS) | Microsoft | - CA - S | Proprietary, uses SNMP and WMI | `www.microsoft.com/smserver/default.mspx` |
| TeamQuest Performance Software | TeamQuest Corporation | - CAP - | Proprietary | `www.teamquest.com/` |
| Tivoli Framework | IBM | FCAPS | Proprietary, uses COBA, SNMP, WMI, and CIM | `www-01.ibm.com/software/tivoli/` |
| WhatsUp Gold | Ipswitch Systems | FCAPS | Proprietary | `www.whatsupgold.com/` |
| ZABBIX | ZABBIX SIA | - - AP - | Open systems, uses SNMP, ICMP, and others | `www.zabbix.com/` |
| Zenoss Core | Zenoss | FCAP - | Open system, uses SNMP, WMI, XML-RPC, and SSH | `www.zenoss.com/product/advantage` |
| ZENworks | Novell | FCAPS | Proprietary | `www.zenoss.com/product/advantage` |
| Zyrion Traverse | Zyrion | F - - P - |  | `www.zyrion.com/` |

Another increasingly popular network management option is the use of a Managed Service Provider (MSP) that specializes in these types of monitoring and maintenance activities.

# Summary

In this chapter, you learned about different categories of network management tools and how they are used to improve network performance and eliminate errors. This chapter used the FCAPS classification to describe network management software types. FCAPS stands for Fault, Configuration, Accounting and Administration, Performance, and Security.

Understanding events and the software that can monitor them is essential to performing network management. Events can be monitored by system counters and by agents, both of which are essentially small programs. Performance monitoring tools can be used to troubleshoot networks as well as optimize performance.

Faults can generate many duplicate events and lead to event cascades; determining faults is a challenging enterprise. Configuration management software allows you to change the configuration of different network devices, and deploy software over the network. Network deployments, upgrades, patch management, and system lifecycles were described in this chapter.

Network management systems are suites of utilities that allow you to perform various management functions. Leading framework applications and proprietary products in this area were presented.

In the next chapter, some of the tools you learned about in this chapter are applied to diagnosing different common network problems.
