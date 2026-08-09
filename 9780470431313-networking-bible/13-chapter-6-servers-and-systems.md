# Chapter 6. Servers and Systems

**IN THIS CHAPTER**

- The most common types of network servers
- The range of network services
- Measuring network performance
- How to model networks and find bottlenecks

In this chapter, principles relating to servers and services on a network are presented. Different server types are considered, a server being described as a software application that provides a service to other networked systems. Because servers come in all shapes and sizes, a process model for a server system is shown.

Right-sizing server services by determining capacity and loading is an important part of having a well-functioning network. Different approaches to capacity planning include maintaining excess capacity, adding capacity as required, or matching capacity to demand. Projects that add server capacity to networks are best handled as part of a solution framework in a phased project. Different methodologies that you can use are described in this chapter.

To improve network performance, you need to be able to define the different levels of service that the network performs. Deconstructing response time into its components, measuring throughput, and defining network reliability, scalability, and other factors allow you to define the performance characteristics of a network.

In this chapter, you learn about different measurable performance data characteristics that you can use to derive fundamental network relationships. These relationships help you to determine which network resource is the bottleneck that is slowing down system performance, and allow you to eliminate those bottlenecks. Modeling networks is briefly described.

The chapter ends with a discussion of adding server capacity, by adding either more powerful systems (scale up) or more servers (scale out).

# Network Server Types

A server is a software program that provides a service to another computer over a network connection. Servers can run on the local system or on a remote system, but the software routine must provide this service to other systems or at least be capable of providing the service. Any service that does not have this shared component is more properly classified as a daemon, which is a local service.

The use of the word *server* is applied very loosely in modern computing. A server is also the name given to a computer that has been configured to run a particular shared application or service. To better enable server functions, most modern servers run a server operating system — what I've chosen to call a *network operating system* in this book. This chapter describes network servers and focuses on the characteristics of shared services and applications.

Often the network server operating system is simply a special version of the desktop version of the operating system, or to be more precise, the desktop operating system is simply a partially disabled, more general-purpose, performance-crippled version of the server operating system. This has been the case with the Microsoft Windows operating systems since the days of Windows Server/Professional 2000, and subsequent server projects such as Windows Server 2003/XP and Windows Server 2008/Vista have continued down this path. Other operating systems, such as Sun Solaris and versions of Linux, make no specific delineation between clients and servers allowing the power of the hardware and the configuration by the user to enable the required features.

### Note

[Chapter 20](ch20.html) covers network operating systems in more detail.

Another use of the word *server* refers to the specific applications that a hardware system runs. A server that hasn't been specifically configured for one application or service function is referred to as a *general-purpose server*. All other servers are described in terms of the major application function that they provide. The most common network server types found today are:

- **File and print servers**. On large networks, file and print servers often represent 25 percent of the servers deployed.
- **Application servers**. Application servers include database servers, Web servers, e-mail servers, and so forth. If the application server runs a branded piece of software, most people refer to the server as an Apache server, Oracle server, and so on. Application servers can usually be as much as 25 percent of the server population on enterprise networks.
- **Backup servers**. Most people are surprised to learn that backup servers are often the third-largest number of server types in an enterprise deployment. It is common to find that as many as 20 percent of all servers are dedicated backup servers.
- **Network servers**. The definition of a network server varies, but if you include services that provide a routing function, system identification such as DNS and DHCP, and similar services, then this class of servers can represent as much as 15 percent of an enterprise network.
- **Domain servers**. Domain servers are essential network servers for most large networks, but they represent perhaps 5 percent of deployed servers.

The percentages mentioned in the bulleted list are based on surveys taken among network administrators across a large population and can vary greatly, depending upon the type of organization and network type. In the list, the total percentage adds up to 90 percent, leaving a category of 10 percent of miscellaneous servers — or simply none of the above.

The server count, and therefore the percentages assigned to different categories of servers, can often be skewed by the deployment of what have come to be known as *server appliances*. A server appliance is a server hardware platform that has been specially configured to run an application or service with minimal human operation. A true server appliance (like a toaster) is one where you take it out of the box, plug in a power cord and network connection, turn it on, and forget about it. Examples of server appliances are routers, gateways, firewalls, print servers, Web servers, and others. The key differentiating factor that defines a server appliance, be it an Oracle 8i appliance or Google Search Appliance (`www.google.com/enterprise/gsa/`), is the ease of use.

A good example of a network server appliance is the series of DNS/DHCP/FTP/NTP/IPAM/RADIUS server appliances sold by Infoblox (`www.infoblox.com`). These appliances are security-hardened devices that run a real-time operating system, are zero configuration enabled, and can replace a number of different server types. [Figure 6.1](ch06.html#the_infoblox-2000_network_service_applia) shows the Infoblox-2000 Network Service Appliance.

![The Infoblox-2000 Network Service Appliance can replace a broad range of network servers.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0601.png)

**Figure 6.1. The Infoblox-2000 Network Service Appliance can replace a broad range of network servers.**

Servers come in a wide variety of form factors. Common server hardware form factors are stand-alone pedestal and tower systems, rack-mountable standard-width servers, and system frames into which complete servers mounted on long add-in cards called server blades are placed. You will find servers deployed in just about any form factor you can think of, and technology continues to make even smaller form factors possible.

Given that computer servers can be emulated in software — their services abstracted so that they can run anywhere and seem to be local, run inside virtual machines, and be made such that resources can be added or removed as needed — the best way to conceptualize a network server is to consider its function and building blocks. An example of the different units required to model a general-purpose server is shown in [Figure 6.2](ch06.html#an_operational_model_of_a_network_server). The parameters shown in the model are those that you can measure or derive.

![An operational model of a network server](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0602.png)

**Figure 6.2. An operational model of a network server**

[Figure 6.2](ch06.html#an_operational_model_of_a_network_server) shows the different functional units of a network operating system. In this figure the different subsystems that impact performance are shown. A service request is input from a network client A0 and the network server operates on the service request returning system output X0 with a certain efficiency represented by the system's throughput.

A service request is added to the Input queue and then submitted to the Central Processing Unit (CPU) for further handling. The Input Queue may have a certain queue length that is a prioritized number of service requests. As service requests are processed, they are removed from the Input Queue. The ability of the CPU to service requests is a function of its speed and the ability to run the operating system(s) and various applications. As requests are processed, instructions may be stored and retrieved from a set of different memory systems: RAM, cache, and disk storage in order of their diminishing speed and increasing capacity (generally speaking).

# Capacity and Loading

The capacity of a network server is its ability to perform a certain workload. Loading measures that portion of a server's capacity that is currently in use. There are many different ways in which capacity and loading of a server may be measured; some descriptions have a mainly theoretical interest, while other descriptions are purely practical. However, while the concepts may be warm and fuzzy, the impact that server capacity has on your network's performance and your company's bottom line is not. Your ability to understand, measure, and modify the capacity and loading of your network services is a fundamental skill.

There are different approaches to capacity planning, and in the next section three different approaches are considered. Capacity planning can be proactive, reactive, or analytical. Each approach requires a different mindset and set of actions. I also cover solution frameworks, which take a stepwise approach based on a team structure that forces organizations to confront project plans and sign off on them step by step to combat large project failures.

## Three approaches

Broadly speaking, there are three different approaches to capacity planning:

1. Maintain excess capacity at all times.
2. Add capacity as demand requires.
3. Match capacity to demand.

Each of these approaches has its own pluses and minuses, and each makes certain demands on the resources available. A lead strategy, which is the proactive approach where you always have excess capacity for any demand, requires that you either have resources in place or that you have access to resources. Because a lead strategy is wasteful of permanent resources, many networks that employ a lead strategy use a tiered approach where additional resources are brought to bear as needed.

Networks employ a lead strategy when they anticipate an increase in traffic and it is essential that they be able to react to that change. A general characteristic of a leading strategy is that the business captured is much more valuable than the cost of the resources. For example, a major company such as Amazon must employ a lead strategy, as the ratio of sales dollars to equipment costs is very large.

The second approach adds resources only when required and is called a reactive or lag strategy. Capacity is added only when the need is demonstrated. The downside to a lag strategy is that a certain amount of traffic will not be satisfied until the extra capacity is brought online. It is a characteristic of a lag strategy that the cost of deploying a network resource is usually larger than the loss associated with the lack of the resource. A lag strategy is a conservative approach, based on different assumptions. When demand is measured, the demand can be described either in terms of an average or mean level of traffic or in terms of the maximum level of traffic seen at peak times.

One approach is to have enough resources to satisfy the average or mean level of traffic, or perhaps more reasonably, a traffic level of a standard deviation so that only outliers are left unsatisfied. The standard deviation measures the *probability distribution* of a data set around a mean value. With a low standard deviation, data points cluster closely to the *mean*; high standard deviation has the data distributed over a large range of values.

While a lag strategy is considered conservative, many businesses operate with a lag strategy in order to maximize the use of a particular resource that may be in demand. A good example of this approach is used on packet-switched networks, which is the basis for the Internet and is used by ISPs. The network pipe is a limited resource and the goal of the ISP is to apportion the bandwidth in such a way as to maximize the utilization while promising the highest level of access that can be reasonably expected by a customer. At periods of high utilization, customers are throttled back or access times are increased, but it is rare that a customer experiences an outage. Or so it seems...

The third approach is the one Goldilocks prefers: "Just Right" or right-sizing the network to demand. This is the analytical approach. Here you modify the amount of system resources in an incremental way so that the network's capacity adapts to changing demand. A match strategy requires the implementation of a feedback loop bringing resources to bear as needed, and perhaps releasing those resources when they are no longer needed.

## Solution frameworks

It is a sad fact that the majority of all major IT projects fail — and you thought that economics was "the dismal science." For our purpose, failure may be defined as one of the following:

- **Cost overrun**. The project greatly exceeds its initial projected cost due either to specification problems or project creep.
- **Time overrun**. The project greatly exceeds its initial projected length before it is deployed or is never deployed.
- **Specification error**. The project solves a problem that doesn't exist, or the problem doesn't exist once the project is complete.
- **Resource misallocation**. The resources brought to bear are better used elsewhere, perhaps solving one problem while creating more substantial issues.
- **Benign neglect**. The project fails because it loses a champion needed to see the project through to completion.

Network deployment and modification projects are often large projects, and they can suffer from any of the aforementioned defects or any combination thereof. To combat large project failures, there have been several different approaches to managing system development and deployment. These solution frameworks take a stepwise approach based on a team structure that forces organizations to confront project plans and sign off on them step by step. As an example of how you might want to structure a large network project, let's consider two related approaches used in the industry based on focused task groups.

Perhaps the best known of these solution frameworks was developed by the Office of Government Commerce (OGC) of Great Britain. OGC publishes a set of policy guidelines for managing network information technology resources called the Information Technology Infrastructure Library (ITIL; `www.itil-officialsite.com/home/home.asp"`), which has become widely adopted, particularly in the European Common Market countries. Their methodology has been trademarked.

ITIL describes how to apply a set of best practices to network service strategies, designs, and operations, as well as how to provide a level of service as conditions evolve. ITIL has been published through three versions, the most recent being version 3.0, published in May 2007 in five volumes:

1. **Service Strategy**. A service strategy would include a description of the business, a best practices framework, service management description, key processes, and demand management.TipYou can lower costs and improve the quality of your project by doing a really thoughtful and detailed project assessment at the beginning of the project. Changes you make later in the project cost exponentially more to fix once the project is under way.
2. **Service Design**. This book describes the network system architecture, business rules, and documentation set. A Service Design Package (SDP) includes a service-level management catalog, business continuity plans, network security scheme, key suppliers, and staffing/role assignment.
3. **Service Transition**. The service transition referred to is the hand-off of prototype systems to production staff for live operation. This book also describes how to conceptualize new projects that modify the existing levels of service, and how to manage assets and configurations as well as configuration changes. Change management, knowledge management, and product release and deployment are tasked to the team that provides service transitions.
4. **Service Operation**. Service operation is described as a set of best practices developed to provide the levels of service that have been placed into the service design. A service operations team provides the day-to-day IT support that working production networks and systems require.
5. **Continual Service Improvement**. The CSI program is a proactive approach to improving a production system while in use. A CSI program would collect user input and feed the more valuable suggestions to one of the other teams for implementation into the product or a next version of the product. Other services covered by this team would include staff training, scheduling, role assignment, and reporting.

The iterative team-based approach used by solution management frameworks is illustrated in [Figure 6.3](ch06.html#a_team-based_approach_that_iteratively_c).

![A team-based approach that iteratively conceptualizes, tests, and deploys solutions has the highest chance of success.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0603.png)

**Figure 6.3. A team-based approach that iteratively conceptualizes, tests, and deploys solutions has the highest chance of success.**

In an iterative team approach, the following groups are created and the project proceeds as each group turns over their part of the project to the next group. The groups include:

- **Program Management**. This team initiates the project and creates the project goals. Their end product is a project plan.
- **Development**. The Development team takes the project plan and reduces it to practice.
- **Test**. The developed project is handed off to the Test team in order to determine that the project works according to specification and without error.
- **Release Management**. The Test team hands off the project to a Release Management team whose task is to roll the project out to the network.
- **User Experience**. A User Experience team works with users to ensure that the project is accepted and works according to user requirements.
- **Product Management**. The Product Management team provides end user support once the project is operational.

Iterative project programs typically include a final analysis of the proposed project and goals with the achieved results by the Program Management team.

As part of the ITIL program, it is possible to obtain a certification in these methodologies from the ITIL Certification Management Board. The OGC (`www.ogc.gov.uk/`), IT Service Forum International (itSMF; `www.itsmfi.org/`), Examination Institute for Information Science (EXIN; `www.exin-exams.com/`), and Information Systems Examination Board (ISEB; `www.bcs.org/`) all contribute to these certification exams, with the latter two organizations administering the exams. Qualifications awarded include Foundation, Practitioner, or Manager/Masters of ITIL Service Management, ITIL Application Management, and ICT Infrastructure Management.

The Microsoft Consulting Group adapted ITIL's team-based approach for use in their major projects. Their success led Microsoft to incorporate this approach into two different methodologies — Microsoft Operations Framework (MOF) and Microsoft Solutions Framework (MSF). With MOF, the goal is to run the network efficiently, while MSF aims to build the network well.

### Microsoft Operations Framework

Microsoft describes the Microsoft Operations Framework (MOF; `www.microsoft.com/mof/`) as a superset of ITIL, but it is probably better described as being a highly adapted version of ITIL. MOF offers operational guides, templates, assessment and support tools, access to white papers, courseware, and case studies. Microsoft also offers services related to MOF. MOF's emphasis is on how to meld people and processes in complex networking environments. MOF guidance tends to consider distributed and heterogeneous networks. MOF runs using the iterative team approach that was described previously.

### Microsoft Solutions Framework

Microsoft Solutions Framework (MSF; `www.microsoft.com/msf/`) offers solutions that the public can download and use. Among the solutions that can be obtained are product or platform deployments or rollouts such as Windows Server, Exchange Server, Visual Studio Team System, Web and E-commerce services, ERP, n-tiered transaction systems, and operation management systems, among others. Perhaps the best representative solution that you can download is the Microsoft Solution Accelerator for Business Desktop Deployment 2007 (BDD; `technet.microsoft.com/en-us/library/bb490308.aspx`), which is a solution framework that Microsoft distributes for the deployment of Windows Server 2008/Vista. Many of Microsoft's deployment tools are conveniently bundled in the BDD.

MSF is currently at version 3.0 and includes both Team and Process models; integration into the Microsoft Operations Framework; and project, risk, and readiness management disciplines. When you download one of the business solutions, you will find that it contains a set of guidelines on how to construct different teams and have them interact, what each team's deliverables are, a set of best practices, and a collection of other resources related to the projects being described. The framework presents a set of recipes that you can adapt for your own situation. [Figure 6.4](ch06.html#the_group-oriented_process_embodied_in_t) illustrates the relationships between teams and tasks in an MSF solution.

In [Figure 6.4](ch06.html#the_group-oriented_process_embodied_in_t) the project starts in the Envisioning stage and proceeds through Planning, Development, Stabilization, and Deployment phases using groups of the type that was described before for an iterative team approach. Each of the diamonds represents a milestone that is defined in the project plan, which for the inner circle is most often represented by hand-off from one group to the next. The outer circle represents concrete tasks and milestones required by the project.

The project proceeds clockwise from the top with both the inner stages path and the outer tasks paths synchronized. An MSF solution doesn't require complete hand-off from one group to another. There may be stages during which two or more groups may still be actively working on the project.

The MSF solution has a set of foundation principles that Microsoft describes as follows:

- **Shared vision**. Each team should have a shared vision for their task and for the project as a whole.
- **Accountability and responsibility**. Each deliverable should be clearly shared and assigned.
- **Open communication**. Keep communication open both inside the group as well as between project teams.
- **Empowerment**. Allow team members to take responsibility.
- **Delivery of value**. Match a need to a set of deliverables.
- **Quality**. Invest in quality, and be quantitative about it. Measure the results.
- **Risk management**. Continually monitor risks and be reactive when problems arise.
- **Learning from experience**. Completed project steps should be subjected to a post-project review.
- **Being agile**. Be open to change based on your experiences.

![The group-oriented process embodied in the design of a Microsoft Solution Foundations business solution](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0604.png)

**Figure 6.4. The group-oriented process embodied in the design of a Microsoft Solution Foundations business solution**

# Server and Systems Sizing

It is essential to understand your servers, services, and systems performance on a quantitative level in order to make good decisions going forward. If the technology is newly deployed, the best approach is to experiment with the system in a testing lab or scenario that provides a realistic diagnostic potential. In some instances, industry benchmarks are constructed using real-world scenarios that may be of use. For example, the Transaction Processing Performance Council's various benchmarks often simulate a real-world scenario such as an E-commerce or data warehousing application. The best metrics are the ones that you develop on your own network using your own systems.

## Defining levels of service

To quantify system performance, you need to measure the Quality of Service (QoS) levels in these areas: response time, throughput, availability, reliability, scalability, adaptability, and security. Several of these factors that are part of QoS, particularly reliability and adaptability, are intrinsic to the technologies that you choose and often need to be designed into the functional requirements for the network from the beginning. Quality of Service or QoS is essentially defined as providing a measured level of service based on an analytical assessment or performance measurement.

### Response time

Response time measures the time it takes for a request to be processed. Measuring the response time is equivalent to determining the rate-limiting step in a chemical mechanism. If you know the rate-limiting step, then you have a measure of the current factor that limits your system performance.

For a client/server application such as a browser making a request to a Web server, the response time can be broken into application, network, and server responses, as shown in [Figure 6.5](ch06.html#the_different_components_of_a_response_t). In [Figure 6.5](ch06.html#the_different_components_of_a_response_t) a service request is initiated and starts at the client in the outgoing stack at the top left of the figure. Client response times, network response times, and then server response times all contribute to the latency of the process as the request leaves the client and arrives at the server. Once the server has processed the response, it then sends the response out (Server I/O) and the factors involved in the incoming response components begin. The processes proceed from the top-right Outgoing stack to the bottom-right Incoming stack going right to left. Incoming factors include the network response time involved with the server and then client portions of network handling, and finally end when the client can display the result.

In practice, separating the different components of the response times into times you can measure can be difficult. You might measure the response time as the time between when you press the Enter key or click the OK button and the time the result appears on your screen, or you might measure the network response time as the time it takes for a message such as a `PING` to be sent to a network node.

![The different components of a response time for a client/server interaction](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0605.png)

**Figure 6.5. The different components of a response time for a client/server interaction**

### Throughput

A system's throughput is the number of operations or transactions that can be performed per unit time. When throughput is measured, it is important that the operational characteristics be defined in a meaningful way. Throughput may be quantified using the following formula:

```
Throughput = MINIMUM {server capacity, available workload}
```

Throughput can vary greatly under conditions of heavy server or network loading from the average or ideal conditions you might encounter or wish to encounter. A typical throughput curve will rise steadily toward 100 percent utilization, at which point the throughput may decrease as a component of the service becomes the gating factor. For example, many systems cache data to enhance performance or extend memory. At high levels of utilization, disk thrashing may begin eliminating the performance enhancement that the cache was designed to offer. Disk thrashing is a condition of low system performance where the system requires an excessive amount of disk I/O (paging) to service requests because the system has no free RAM to store the data that is required by current processes.

Throughput metrics include:

- millions of instructions per second (MIPS) for CPUs
- I/O per second (IOPS) and kilobytes transferred per second (Kbits/s) for disk drives
- packets per second (PPS) or megabytes per second (Mbits/s) for network segments
- transactions per second for applications
- page views per second
- HTTP requests per second, or kilobytes per second (Kbits/s) for Web servers or sites
- messages per second for an e-mail server
- searches per second or sessions per second for a database

Throughput is a measure of a quantity per unit time and is meaningful as long as the quantity and time are comparable. For example, it is unreasonable to compare metrics for an e-mail transfer of 4 K messages versus one that has a megabyte attachment associated with it.

A well-defined benchmark attempts to correct for these differences by performing a mixture of tasks so that some are performed with low priority, others with high priority, and other factors are varied. For example, the TPC-C V5.10 (`www.tpc.org/tpcc/default.asp`) executes a mixture of transactions using a typical Online Transaction Processing (OLTP) order entry system that a wholesale supplier would require, including entering and delivering orders, and monitoring the level of stock at warehouses. The benchmark measures the number of orders of this hypothetical system per minute as expressed in the metric tpmC.

### Note

There are lies, damn lies, statistics, and benchmarks. I can't stress enough that a benchmark is only useful when it compares two systems using consistent methodology. A benchmark that measures network performance for small packet transfers will likely be very different from one that measures the performance for large frame transfers. Be vigilant.

### Availability

Availability is defined as the fraction of time that a service is available, and is a fundamental network metric for many systems. An online store may seek to have an availability of four nines or 99.99 percent uptime; the system would then be unavailable for over 52 minutes a year. This uptime would be considered to be borderline "mission critical," but would obviously be inadequate for a system that monitors patients in a critical care facility. Availability is a fundamental network design parameter.

### Reliability

Reliability is a measure of the probability that the network will perform correctly over time. Many people fail to differentiate between availability and reliability; although these two concepts are related, they are sufficiently different to consider when designing or upgrading a network. A network can be available and still deliver operations that are not reliable. For example, in a packet-switched network under heavy loading, systems may still be available while an increase in the error rate reduces the network's reliability. As the reliability increases, its rate approaches the availability rate.

### Scalability

The term scalability is applied to a system that can add additional load without a degradation of performance. Load can be expressed as the number of users, the number of concurrent sessions, or some other factor. If adding more load changes the performance characteristics of a network (usually in a negative manner), the system is considered to not be scalable at the point at which the impact becomes significant.

### Adaptability

Adaptability, defined as the ability of a network to be extended to include other services, is a design consideration when installing or upgrading a network.

### Security

Security is a combination of providing data access, maintaining confidentiality, and verifying the actions of systems and users.

## Quantifying performance

It's good to have a general feeling for the Quality of Service factors that any service installation or upgrade requires; but it is much better to be able to quantify performance using a set of real system metrics to focus in on the tasks required to obtain the desired results. It is considered a best practice to maintain a set of performance logs collected over time in order to determine trends and isolate problems. Analysis of trends allows you to be proactive in upgrading or modifying your network; they allow you to diagnose errors because they serve as baseline measurements, and through event logs they allow you to get detailed information on network conditions.

The following set of data on resource utilization is useful to monitor:

- **CPU utilization**. The average and peak levels of CPU utilization were collected and analyzed to determine trends over time as well as utilization over the typical work week.
- **Memory utilization**. The amount of memory in use, the number of page faults, cache performance, and other factors were collected and analyzed.
- **Disk utilization**. The size of allocated disk space was tracked, as were factors such as disk IOPS, to determine trends over time and over a typical work week. Different disk structures and types were analyzed, including various types of RAID, dedicated storage arrays, and others.
- **Network utilization**. Factors that indicate the level of network performance were collected. These factors include throughput, response times, and collision rates, among others.

### Note

Modern network operating systems offer a great variety of performance counters. Only a few are typically running in a default system, so if you need additional types of counters, you may need to install them and/or enable them. Many applications, particularly enterprise server applications, come with their own set of counters that are installed as part of the application's installation process. You may want to consult your operating system and application vendor's documentation to determine which additional counters may be available. Be careful in your use of counters, as enabling them may impact the performance that you are trying to measure. This is particularly true of disk counters.

To obtain this data, different performance counters were turned on at the server, routers, and perhaps at some representative clients. The key observable performance data that you might want to collect is summarized in [Table 6.1](ch06.html#key_measurable_performance_data).

**Table 6.1. Key Measurable Performance Data**

| Symbol | Description |
| --- | --- |
| Source: Performance by Design, by Daniel A. Menasce, Virgilio A. F. Almeida, and Lawrence W. Dowdy, 2004, Prentice Hall. |  |
| **Measured Data (operational variables)** |  |
| `T` | Time period of observation |
| `K` | Number of resources used |
| `Bi` | The time the resource `i` was busy during `T` |
| `Ai` | The total number of service requests that are presented to resource `i` during period `T` |
| `A0` | The total number of service requests (of the type being studied) that were presented to the overall system during `T` |
| `Ci` | The total number of returned completed requests from resource `i` during period `T` |
| `C0` | The total number of returned completed requests from the system during period `T` |
| **Derived Data** |  |
| `Si` | The mean service time per completion at resource `i` is: `Si` = `Bi/Ci` |
| `Ui` | The resource utilization of `i` is: `Ui = Bi/T` |
| `Xi` | The throughput of resource `i` is: `Xi = Ci/T` |
| `λi` | The arrival rate at resource `i` is: `λi = Ai/T` |
| `X0` | The overall system throughput is: X0 = Ci/C0 |
| `Vi` | The average number of visits per request to resource `i` is: `Vi` = `Ci/C0` |

### Performance relationships

Utilization is a key factor in determining the need for additional resources. Once a resource is fully utilized, there is no more capacity available to perform the function (tasks) that the resource is busy doing. Utilization, as you can see in [Table 6.2](ch06.html#operational_laws), is defined as `Ui = Bi/T`. To calculate the average time that resource `i` took to complete a task, you multiply this equation by `Ci/Ci`, which yields the following equation:

```
Ui = (Bi/Ci) / (T/Ci)
```

Then, because `Bi/Ci` is the average service time `Si`, and `T/Ci` is the inverse of the resource throughput `Xi`, you reduce the equation as follows:

```
Ui = Si x Xi
```

The relationship derived above is referred to as the Utilization Law, and it states that a resource's utilization rate is the product of the average service time times the throughput. When the completion rate is such that all arrivals are processed during the observation period, `Ci = A`, then `Xi = λi` and the Utilization Law takes the form:

```
Ui = Si x λi
```

If the resource that you are studying has multiple instances — for example, multiple connections or wires, multiple processors, and so forth — then the Utilization Law accounts for these instances using the following generalization:

```
Ui = (Si x Xi)/m
```

where m is the number of servers that a resource has.

A service request almost always requires multiple uses of critical resources. For example, if you make an HTTP request to a Web server, completing the request might require several `READ`s to obtain the data objects necessary for the response. If the data objects are in cache, then the resource being utilized is RAM; if not, then multiple requests may need to be made from disk(s). When a set of requests are made using a resource, you can define a performance factor called a *service demand*. The service demand Di is the total average time spent by an average request of the type being analyzed for the resource `i`. The formula for service demand is then:

```
Di = (Ui x T)/C0 = Ui/X0
```

or alternatively,

```
Di = Vi x Si
```

This relationship, known as the *Service Demand Law*, states that the service demand is obtained from the visit count multiplied by the service time, or alternatively, the resource utilization divided by the overall system throughput. For any resource derived from multiple instances, you can generalize the equations to the following:

```
Di = Ui,r/X0,r = Vi,r x Si,r
```

where r represents the different classes of service demands, each class being computed individually.

When studying a resource i, you determine that the number of visits to the resource required by the request is 4, and the throughput of the resource is 3.5 requests per second. If this is a disk drive, for example, the 3.5 requests per second are in the form of disk I/O (READ/WRITE) and the units are in IOPS. To relate the resource's throughput `Xi` to the system's throughput `X0`, you would use the formula:

```
Xi = Vi x X0
```

which generalizes to

```
Xi,r = Vi,r x X0,r
```

This equation is referred to as the *Forced Flow Law*, and applying this law to our example, the throughput of the disk would then be 3.5 × 4, or 14, IOPS.

You can relate the average number of requests, the throughput, and the average time of a request using a formula that is called *Little's Law*, as follows:

```
Ai = Xi x Si
```

Consider the trivial circumstance where a disk subsystem either has a single request or there is no request at all. In this circumstance, the probability that the request is being serviced is equivalent to the disk subsystem's utilization. When there is no request, the probability is equivalent to the disk subsystem's idle time. The equation above is simply a restatement of the Utilization Law.

For a situation where there is a request queue and a certain number of active requests on the disk's subsystem, you can formulate the relationship between the queue length and active requests (`Ni`), the average time of the request (`Ri`), and the throughput (`Xi`) as follows:

```
Ni = Ri x Xi
```

This same equation reshuffled shows that if you know the queue length and the throughput, then you can calculate the response rate as follows:

```
Ri = Ni / Xi
```

Little's Law can be applied to a broad variety of resources and situations when evaluating system performance. However, there are some limitations that you need to be aware of. For Little's Law to function correctly, requests cannot be created or destroyed in the system. A request in the queue that is processed must at some time be completed by the system. The time that any one request spends in the queue isn't relevant; it can be random, Last In Last Out, First In First Out, or the like, as Little's Law is applied to average values.

Consider a client server system with multiple (`M`) clients accessing a server, as illustrated in [Figure 6.6](ch06.html#a_client_solidus_server_system_request_s). A client is either processing a request or the client is idle. The average number of clients in the request state is `Mavg` and the average number in the idle state is `Navg`. Because clients can be in either state, the sum of these two averages equals the number of clients:

```
M = Mavg + Navg
```

The system shown in [Figure 6.6](ch06.html#a_client_solidus_server_system_request_s) shows multiple client requests made to a server (the bottom set of multiple arrows on the left) and sent to the server on the right. The average time spent by a client in the idle state (Z) is shown by the bar on the left, and the average server response time (R) is shown by the bar on the right. Little's Law separately states that the average number of clients in the request state is related to the system's throughput (X0) multiplied by the server's response time as follows:

```
Mavg = X0 x Z
```

which states that the average number of requests per unit time or throughput equals the number of completed requests per unit time or system throughput (`X0`).

![A client/server system request/response model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0606.png)

**Figure 6.6. A client/server system request/response model**

Little's Law applied to the server leads to the relationship:

```
Navg = X0 x R
```

Combining the two expressions leads to the equation called the Interactive Response Time Law:

```
R = (M/X0) - Z
```

`or more generally for a multiple system`,

```
Rr = (Mr/X0,r) - Zr
```

The Interactive Response Time Law then states that the response of the server is equal to the number of clients divided by the throughput minus the idle time.

[Table 6.2](ch06.html#operational_laws) shows the five operational laws that have just been described.

**Table 6.2. Operational Laws**

| Law | Relationship | Description |
| --- | --- | --- |
| Source: Performance by Design, by Daniel A. Menasce, Virgilio A. F. Almeida, and Lawrence W. Dowdy, 2004, Prentice Hall. |  |  |
| **Utilization Law** | `Ui = Xi x Si = λi x Si` | Relates utilization to throughput and mean request handling time. The last term is true if all inputs are processed. |
| **Forced Flow Law** | `Xi = Vi x X0` | A resource's throughput is equal to the number of visits (requests) multiplied by the system throughput. |
| **Service Demand Law** | `Di = Vi x Si = Ui/X0` | A resource demand is related to the number of visits times the average request completion time, or to the resource utilization divided by the system throughput. |
| **Little's Law** | `Ni = Ri x Xi` | The queue length and active requests is equal to the t average time of the request times the throughput. |
| **Interactive Response Time Law** | `R = (M/X0) - Z` | In an interactive system, the response rate is equal to the number of clients divided by the system throughput minus the idle time. |

### Eliminating bottlenecks

The whole point of this exercise is to have the highest limit for throughput and the shortest response time possible, within the limits of the technology that you are working in, for any service demand that you are analyzing. To apply the five operational laws discussed previously, you need to be able to isolate the performance characteristics of the resource in question, which in complex network systems can be difficult to do. Still, these equations supply a theoretical framework for performance limits and you need to derive or at least approximate their values in order to input them into any performance model that you want to consider.

If you had to understand an entire network in order to improve performance, you would be faced with an intractable problem. In almost all cases, though, the performance for any service demand is entirely dependent on one subsystem or factor, and in rare instances perhaps two factors. Any factor that gates performance is called a *bottleneck*, and the nature of a bottleneck is that it is the system resource that has the highest utilization and lowest response rate, and has reached the limit of its available throughput. The rationale for improving performance is to successively eliminate bottlenecks until you achieve the desired result. For example, if you have a network containing a set of 10Base-T connections and the speed of the network is gated by these connections, then removing the slowest-performing link simply moves the bottleneck down to the next connection. Replacing all the 10Base-T links, however, would remove that class of bottleneck, revealing the next issue in performance, which might be the hubs that you are using.

Consider four hypothetical resources, A to D, where the utilization and throughput for each have been measured over a range of input. In [Figure 6.7](ch06.html#a_plot_of_utilization_versus_throughput), you see a plot of each of these resources mapped over their utilization range. Each of the symbols — plus, triangle, square, and circle — represent measured data points for each of the four resource curves shown. Resources B through D retain spare capacity throughout the input range that was measured. Resource A, however, approaches 100 percent linearly up to a throughput of 7 and greater where it can no longer service the requests efficiently and the curve flattens out. Enhancing the performance of A therefore eliminates this particular bottleneck.

![A plot of utilization versus throughput for four resources highlights resource A as a bottleneck.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0607.png)

**Figure 6.7. A plot of utilization versus throughput for four resources highlights resource A as a bottleneck.**

Because the Service Demand Law relates resource demand to utilization and throughput, you can use the experimental quantities you measured to calculate the overall resource service demands as follows

```
Di,r = Ui,r/X0 = A-DΣ Ui/X0 = UA/X0 + UB/X0 + UC/X0 + UD/X0
```

to obtain the total resource demand of the system based on the overall system throughput that you measure. The resource that is measured to have the highest service demand will have the highest utilization, and vice versa; it is therefore the bottleneck of the system and is governed by the equation:

```
X0 = < 1 /(MAX {Di})
```

This applies to resource A under heavy load in [Figure 6.7](ch06.html#a_plot_of_utilization_versus_throughput), and is referred to as the upper asymptotic bound throughput limit under heavy load.

Different types of resources have different levels of concern based on the utilization rates. For disk, you might start to monitor any disk system that is 50 percent utilized, worry about any disk that is 70 percent utilized, and worry harder about any disk that is 80 percent utilized. Many disk operations begin to fail when the disk system is more than 85 percent full. This is particularly the case with databases and graphics, which store copies of the entire data set to disk as temporary files.

You can also consider the number of visits or requests and its relationship to service demand and throughput to make predictions on the nature of the bottleneck resource under light loading, which is a different problem than the one you've just seen for a heavily loaded system. Little's Law is the relationship that provides this connection. In a lightly loaded system with N transactions and no queue, Little's Law predicts that:

```
N = X x R > = (KΣi=1 Di) x X0
```

Rearranging this equation and solving for `X0` leads to

```
X0 = < N /(KΣi=1 Di)
```

which is described as the upper asymptotic bound of throughput under light load. If you combine the two upper asymptotic bounds on throughput together in the same equation, you can derive the following relationship:

```
X0 = < MIN [(1 / MAX {Di}),(N /(KΣi=1 Di))]
```

[Figure 6.8](ch06.html#bounding_limits_under_light_and_heavy_lo) illustrates the relationship of the two upper asymptotic bounds on throughput for high and low loading and the impact that upgrading a bottleneck resource has on those relationships. The measured throughput for the original system is shown by the line with plus data points that approaches the heavily loaded system line, which is indicated by the line with triangle data points. In the original system, the throughput can approach this limit. When you upgrade the system and set a new heavily loaded limit line, shown as the line with square data points, the upgraded system can now approach this line as indicated by the upgraded system line with the circle data points.

A system under light load doesn't suffer from these limitations. In a lightly loaded system, the system can scale linearly. The two lines, the original system under light load with star data points and the upgraded system under light load with pentagon data points, scale throughout their range. The upgrade system is able to scale with a higher slope attaining greater throughput faster. Note, however, that there is a limit to the number of transactions that the lightly loaded system can accommodate and that the original system will support up to only six outstanding transactions while the upgraded system will scale up to nine outstanding transactions in the data queue.

![Bounding limits under light and heavy loads for an upgraded resource](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0608.png)

**Figure 6.8. Bounding limits under light and heavy loads for an upgraded resource**

### Network modeling

The process for modeling a computer network involves determining the different states that the network can be in, their probabilities, and the relationships between each state and other states. Given six states A to F, what are the relative probabilities that a particular state will lead to the other states? This type of modeling is referred to as a *Markov model* or*chain*, and defines a stochastic process that conforms to the Markov property limitation. In Markov models, the Markov property is that for any present state, transitions to future states are independent of the past states of the system. That is, the past does not determine the future.

### Note

The Google PageRank feature is based on a Markov chain.

To build a Markov model, you can start by considering a random walk through the state space, noting the probabilities at each step. The resulting map or graph is a set of nodes representing each state and relationships between nodes that represent transition probabilities. Consider a packet-switched network with four different routers A to D, each interconnected by network segments. [Figure 6.9](ch06.html#a_markov_diagram_for_four_routers_on_a_n) shows a Markov model representing the probability that a particular message has for navigating the network. Notice that the probability of leaving any one router is 1.0, and the probability of entering any one router is 1.0. You can determine the sum of the probabilities by adding all of the probabilities of arrows leaving the router and all of the probabilities of arrows entering the router. The arrows represent the next hop in the system.

![A Markov diagram for four routers on a network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0609.png)

**Figure 6.9. A Markov diagram for four routers on a network**

Having established the probabilities for transitions from router to router, you can use the Markov diagram to predict the behavior of this part of the network to solve for problems such as which router or network segment will be used most heavily. To solve these problems, you need to create a set of states to which a Mean Value Analysis (MVA) can be applied. For example, if a path through this router set is described as (Segment 1, Router, Segment 2), then you can fully describe the router space with a set of state transitions as follows:

```
(BA, A, AC), (BA, A, AD), (CA, A, AB)...(AD, D, DB), (BD, D, DC), (CD, D, DA)
```

Because you know the probability for each network segment, you can assign weights to the states or paths described. Some terms will drop out; other terms will be shown to have higher probabilities. The path vectors would then be written as:

```
(0.35 BA, A, 0 AC), (0.35 BA, A, 0.5 AD), (0.4 CA, A, 0.5 AB)...(0.5 AD, D, 0.6 DB), (0 BD, D, 0.1 DC), (0.4 CD, D, 0 DA)
```

The terms that are shown as strikeouts in the listing of path vectors are terms that drop out because they have a component that has a zero probability, making that path impossible to follow. Because all of these paths have relative weights, you can add up all of the paths, normalize the values, and obtain solutions to which paths have the highest probability and which router will see the most traffic.

Markov diagrams have a wide application. You could have chosen a set of disks in a disk array, a set of processors, processors and disks, or any other system you like that is not deterministic. Essentially, you use the Markov diagram to look into the black box that Little's Law abstracts processes into.

While Markov models are widely used in many disciplines, they can't be applied to many problems. As mentioned previously, they don't apply to situations where the previous state has an impact on the next state in a system. If one router is significantly slower than the other routers, or if self-loop paths influence the next path chosen, then either those factors must be incorporated into the Markov model or the model will not make accurate predictions. The more factors you add into the model, the more complex the problem becomes, and the more likely it is that the complexity will lead to inaccuracy.

Another problem with the Markov model is that it makes the assumption that the relative probabilities are fairly weighted. If a router has two paths leading out that have equal probabilities (50 percent) and the first packet out takes path B, then the probability that the next packet will take path A is still 50 percent. The probabilities make no specific demand on the path that the next packet takes, even though the population of probabilities will eventually apply. This is referred to as the exponential assumption, that probabilities are exponentially distributed. As an example of how probability can go awry, consider the fact that in the Super Bowl, the NFC team has won the coin toss the last 10 times. Go figure, the odds of that happening (for a fair coin toss) are 1 in 210 or 0.098 percent, even though every single pick by an NFC team still has only a 50/50 chance of being correctly picked

To use a Markov model that accounts for a path with two parts, you could decouple the two segments into individual states, each obeying the exponential assumption. This partitioning would then lead to a more accurate but more complex solution.

In theory, you can construct a Markov model to solve any problem. However, when the number of states rises to a certain level, the equations that solve problems in that state space become computationally onerous and the model no longer can be understood on an intuitive basis. To get around these types of problems, other variations of the Markov models are used, as are other model types. Because the topic of network modeling is more an applied mathematics problem than a networking problem, if you want to read more about performance modeling, you may want to read one of the texts on this area of study.

## Server upgrades

Let's consider a specific example of how you can use a Markov model to determine how to upgrade a specific network server. If you have a system of domain servers and notice that those servers are beginning to reach high levels of utilization, you might conclude that these servers must be upgraded. Here are some items that you will need to know in order to calculate the impact of upgrading one component versus another server component:

1. **Maximum load**. The period of highest workload is Monday mornings from 8:30 to 10:00 with a specific measured load level.
2. **Application characteristics**. The application characteristics are crucial in setting RAM requirements, disk sector size, network bandwidth, and other parameters.
3. **Disk performance**. When you match the application's I/O pattern to the disk configuration, you are able to improve performance dramatically and lower disk requirements.
4. **Server/storage abstraction**. By abstracting server functions from storage functions, the system is made more reliable, flexible, and available.
5. **Network performance**. The domain servers generate significant replication traffic that impacts the network, so fewer, more powerful servers are preferred. Replication traffic should occur over dedicated network segments. An availability level of 99.95 percent was deemed satisfactory for this particular network service.
6. **ROI calculation**. An understanding of the Return on Investment (ROI) of the upgrade/expansion project is performed to justify the expenditure. ROI forces you to examine factors that you might not normally think about, such as system and software life cycles, and so this is an important step that you don't want to ignore.

An upsizing project based on these results might have the following phases to it:

- Historical data analysis
- Capacity planning
- System selection and design
- Testing and fine-tuning
- Pilot phase
- Production and rollout

Based on the results of this study, it was determined that the domain servers should be consolidated and their power increased, and that a dedicated connection should be established between domain servers. The question is, what type of server consolidation is a best fit? Server consolidation can:

- **Scale Out**. Increase the processor count by adding more systems
- **Scale Up**. Increase the processor count by deploying fewer, but more powerful servers

The two approaches have very different effects, both on networked server applications and on the network infrastructure. [Figure 6.10](ch06.html#scale_out_open_parenthesis_left_close_pa) shows Scale Out and Scale Up graphically. When you scale out, once the server capacity is taxed, you just add another server to what is called the "server farm." When you scale up to a large server and you max out your server capacity, you add additional capacity to any particular application or task by dedicating more processors on the large server to the task at hand. Both approaches have their own set of benefits and penalties.

![Scale out (left) adds more servers, while scale up (right) adds fewer but more powerful servers.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0610.png)

**Figure 6.10. Scale out (left) adds more servers, while scale up (right) adds fewer but more powerful servers.**

Scale out can be done incrementally and offers more options in terms of vendors and configuration than scale up does. Scale out is usually less expensive because it relies on replicating commodity equipment to achieve additional scale. From a network perspective, scale out maximizes the number of channels and provides better opportunities for applying technologies such as load balancing and failover. The fact that equipment is less expensive and less reliable is offset by the flexibility that scale out offers. Scale out gives you the benefit of working with smaller server units, and achieves availability through redundancy. As a rule, scale out requires more management than scale up does.

If you have an application that doesn't create a persistent connection to a server (is stateless), such as a Web service, then that server service is a candidate for server scale out. The large server farms that run Internet sites, terminal server farms, and other similar types of applications are often architected using this approach. Applications that aren't CPU and memory limited, but are bottlenecked in network I/O, lend themselves to server scale out.

Scale up has its own advantages. When you scale up, you have fewer servers, there are fewer points of failure, and you have a simpler network architecture. This also provides fewer servers to manage, maintain, and upgrade. Large SMP system vendors pay more attention to the quality of their components, are able to run enterprise versions of network operating systems, and offer considerably better support to their customers. Scale up places your eggs into one basket, but a more robust and fault-tolerant basket.

As a general rule, dense SMP systems that support high processor counts and powerful processors don't usually emphasize network I/O. Applications that benefit from enhanced processing but aren't I/O limited benefit from a scaled-up system. For example, a data warehouse application requires the processing of large data sets, but the reported results require modest network connectivity, and so the application is a good candidate for a scale up approach.

# Summary

Servers play a central role in networks. They provide the services that other systems need. This chapter focused on how to determine capacity and loading in order to have a well-functioning network. Different project methodologies for adding server capacity were described.

Performance data allows you to derive fundamental network relationships. These relationships help you to determine which network resource is a bottleneck and allow you to figure out how to remove those bottlenecks. Modeling networks using a Markov model was presented.

In the next chapter, the concept of a network interface is described. Network interfaces, just like servers, are hardware, software, and a fundamental network component.
