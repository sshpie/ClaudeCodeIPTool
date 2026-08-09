# Chapter 14. Network Automation Architecture

This book has covered and introduced many concepts, technologies, and tools for network automation. However, there is a big leap from learning a new technology or concept to stitching them together to create a plan that can be used to drive enterprise adoption of network automation. This chapter aims to give you a comprehensive strategy to start building network automation solutions, including the ones described in [Chapter 2](ch02.html#netautomation).

It is common to build network automation solutions to address an specific domain (e.g., Campus, Data Center, Security, and Cloud), but this isolation adds complexity and doesn’t help in breaking down silos and reusing automation among teams. To mitigate this, we dare to propose a *network automation architecture* to help you organize the tasks to be automated in an easy-to-understand and easy-to-apply way. This architecture will provide you with a structured view to ease the definition of requirements and dependencies, which will lead to better decisions when choosing how to design and implement each task that will be automated by the network automation solution with a holistic approach.

This chapter starts by presenting a structured approach to a network automation architecture, followed by a deep dive into each component within this architecture. Finally, an example of how to apply this methodology in a real use case will show you how you can leverage it.

###### Note

In this chapter, you will find many references to other chapters in this book. We are aiming to connect the dots, to help you understand how each topic plays its role in the big picture of network automation.

Without further delay, let’s get to know the network automation architecture.

# Introducing the Network Automation Architecture

Even though every network automation solution may have different implementations or tools, all of them end up sharing some common patterns. Being able to identify and classify these patterns will help you adopt a systematic approach to building new solutions and evolving them while keeping them aligned to their specific functionalities. This is the goal of the network automation architecture proposed here.

[Figure 14-1](#net-arch) depicts the six components of the network automation solution. Each component in the architecture has one or more functional goals (based on implementation), and connects with the other components to achieve the desired goals of the solution. By understanding each component, you will be able to determine where to map each action required to implement a network operational workflow, and easily identify the challenges to address and the available options for implementation.

![npa2 1401](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1401.png)

###### Figure 14-1. Network automation architecture

To get started, the following provides a short introduction to each architecture component:

Network infrastructure[Chapter 1](ch01.html#trends) presented the new trends in network infrastructure (e.g., NFV and cloud/controller-based services). All of them, including traditional network physical devices, are contained in the scope of the *network infrastructure*. This component has already been covered throughout the book: exploring the available management interfaces in [Chapter 10](ch10.html#apis), discovering new networking paradigms in [Chapter 4](ch04.html#cloud), and emulating them in [Chapter 5](ch05.html#developmentenvironments).

User interactionsOne way or another, human beings will interact with the network automation solution. You may be interfacing with Git if you’re adopting a GitOps workflow; you may interface via a ticketing system if you’ve adopted self-service for nontechnical users. Each use case requires a proper *interface*, and choosing the right one for each case will have a big impact on the solution’s adoption. Getting this right is extremely important. The user interactions align culture and people to network automation. The worst thing that can happen is to expose an interface that does not end up getting used. In [“User Interactions”](#user-interactions), we describe various forms it can take, such as service portals, dashboards, and messaging applications.

Source of truthEvery network automation solution needs data to act upon it. In simple solutions that are not persistently managing a network, data can be provided ad hoc. For instance, a user could trigger a script to do a small automation task. However, when the network automation solution has to constantly manage the network state, that solution requires reference data that we define as the *intended* state (the state you want your network to be in). As you will see in [“Source of Truth”](#source-of-truth), describing the network state could include multiple data use cases that are required to deploy and manage a network—like IP addressing, VLANs, routing protocols, ACLs, and much more. Moreover, to properly implement a source of truth, you need to understand the constraints and trade-offs around data management.

Automation engineThis component includes all the tasks related to changing the state of (or more generally, interacting with) the network infrastructure. It takes data from user interactions and/or from the source of truth as input in order to interact with the network via the proper interfaces. As you will see in [“Automation Engine”](#automation-engine), the automation engine includes all the aspects related to configuration management and other operational tasks (e.g., a device reboot). In this section, you will identify the role of the tools introduced in [Chapter 12](ch12.html#automationtools) or of scripts using libraries from [Chapter 10](ch10.html#apis).

Telemetry and observabilityContrary to the automation engine, the telemetry and observability component is focused only on retrieving (*read-only*) the network’s operational state. In [“Telemetry and Observability”](#telemetry-and-observability), you will learn about how to collect, store, and consume this state, providing a proper visualization or alerting to trigger other automation tasks when the actual state of the network doesn’t meet the expectations defined in the source of truth.

OrchestrationThis component implements the glue between the other components, defining the logic to chain tasks to create orchestrated workflows. Most automation solutions don’t have a single execution path. Depending on success, failure, or approval, different paths will be traversed. As an example, the orchestration would kick off a task in the automation engine when an alert from the observability is received, enabling closed-loop solutions. In [“Orchestration”](#orchestration), you will go over the characteristics of a workflow engine and how it can enable event-driven automation solutions.

###### Note

Even though not explicit in the architecture (depicted as dotted arrows in [Figure 14-1](#net-arch)), every component implements APIs to facilitate communications with other components within the architecture, as well as external services. Depending on the complexity of your API implementation, you may need to implement advanced API architectures (e.g., API gateways), but these are not covered in this book.

This reference model could be generalized to any infrastructure automation solution, only replacing the network infrastructure block with a more generic one. However, because of the unique characteristics of the networking domain, with its own unique interfaces and use cases, we are focusing only on describing how to use this architecture to build network automation solutions.

It is important to know that this architecture and framework arose from years of experience designing and implementing network automation solutions. This architecture helps map tasks into high-level building blocks in order to better understand their purpose and their interconnections. We believe it will help you better understand how to apply all the concepts introduced in this book to build complete solutions.

###### Note

There are other available architectures, with more low-level details. A recent initiative by the IETF is the [Intent-Based Networking informational RFC 9315](https://oreil.ly/AecOb). If you read it, you will find a lot of familiar ideas because *intent-based networking* has its root in the concept of the “source of truth,” and the implementation follows closed-loop automation, as does the one proposed here.

You should not overlook the fact that a network automation solution is just another software solution. Therefore, when you build it, you should consider all the architectural factors that apply when building and running software applications. Your final solution could be composed of commercial tools, open source software, and possibly custom extensions or add-ons. Each should be carefully integrated into the overall system.

How to build your own software components is beyond the scope of this book (many other books cover this topic), but in short, we strongly recommend following software development best practices to consolidate and deploy your applications, as introduced in Chapters [11](ch11.html#sourcecontrol) and [13](ch13.html#cicd), respectively. Likewise, for the sake of brevity, we don’t cover considerations about the scalability, resiliency, or security of the implemented solutions. However, you should take these into account when building your real solutions.

Before getting started with the components deep dive, let’s stress a key rule about approaching automation. Network automation is about transforming and improving existing operational workflows. But *you can’t automate what you don’t understand*. Therefore, the first step will always be to understand the current process. One way to adopt this mindset is described in [“Understanding the Architecture with an Example”](#architecture-example).

Now, it’s time to go deeper into each one of the architecture components.

# Overview of the Architecture Components

With the overall view of the network automation architecture ([Figure 14-1](#net-arch)), you hopefully have a basic understanding of the role of each component. In this section, you will learn more about the purpose, features, common use cases, and related challenges of each.

###### Note

As commented before, we don’t cover the network infrastructure component here because it has already been covered throughout Chapters [1](ch01.html#trends), [4](ch04.html#cloud), [5](ch05.html#developmentenvironments), and [10](ch10.html#apis). However, we want to stress that all types of networks are in the scope of the architecture.

Throughout this section, we explain how the components are interrelated and also give some references about products and tooling that can be leveraged to implement them. As you will see, most of the tools cover multiple components of the architecture, but we classify them by their main and most common role. For instance, Ansible (see [Chapter 12](ch12.html#automationtools)) as a configuration management tool is referenced in the *automation engine* component, but it also comes with a CLI that could be a valid *user interaction* tool in some use cases.

Moreover, you will find references to tools that provide you with most of the features you would need to implement your solution. In some cases, you would add some configuration (e.g., defining your own Ansible playbooks) or add a small code extension. Reusing, if possible, is always preferred because of the resources needed to build and maintain a solution versus leveraging external solutions. However, you may end up building your own application when your requirements can’t be addressed. This dilemma is named *build versus buy*. In the case of *build*, always consider the consequences for your company, in the present and future.

###### Tip

When working on any architecture design, it’s strongly recommended that you document your decision-making process, in order to help others understand your conclusion and the constraints you took into account. A good reference in this area is the [Architectural Decision Record process](https://adr.github.io) used by GitHub.

The ultimate goal of this section is to provide a reference of the key points to tackle when designing a network automation solution and materializing them into a concrete implementation. The first step is understanding how users will interact with the solution.

## User Interactions

Even though we are building automation solutions, we shouldn’t forget that an end user is always interacting with them. Understanding each persona’s role (skills and motivation) is a crucial part of choosing the right interface in order to tailor the user’s experience and improve the solution’s adoption.

For example, imagine you are managing an internet content provider with myriad points of presence (PoPs) and BGP peerings to sustain your network. In your organization, the network operations team would likely be fond of a CLI-like interface that could offer a well-known way to troubleshoot any issue. On the other side, the network capacity team would be more comfortable interacting with a dashboard offering easy-to-consume data. Only changing the UI can transform the UX without changing the underlying system.

One unstoppable trend transforming the way consumers are interacting with network services is consuming the *network as a service*. Nowadays, with the massive adoption of cloud-based solutions, everyone has gotten used to consuming infrastructure in almost real time. So, being able to offer a similar experience for the network service will match users’ expectations and remove friction on its adoption. Without a doubt, creating a network as a service is a complex challenge with many facets, but user interaction is the front end of the solution, and it needs to be ready to allow the proper UX.

To give you an overview of the alternatives for this component, we cover both graphical and text-based interfaces. In both cases, you will find options for managing the network state or simply observing it. In addition, the knowledge share (or documentation) solutions are covered because of their relevance to understanding, operating, and extending the network automation solution.

Most of the user interactions we introduce next won’t be new for you. You have likely used some of them before. However, the trick here is to leverage these tools to their full potential so that they are no longer simply human-facing interfaces but the first line of network automation. Tailoring them to match the expectations from both sides—the user and the automation—makes the process smoother and prevents wasting time. As we mentioned earlier, users are looking for a self-service experience when consuming any IT service, and this aligns with a more efficient use of time from the network engineering team.

One common challenge for all the user interactions is defining the data in both directions, data in and data out:

Data inThe data ingested by the user should match the expectations of the other architecture components. From the beginning, the data must adhere to well-known schemas to enforce data quality. The data will conform to a structure, and its content could follow validation rules. Suppose that the input data contains a host IPv6 address; the UI can’t accept any format not compliant with the RFC defining the IPv6 address format.

On top of that, another important aspect is simplicity: request only the minimum data needed by the user and leave data extension for an automated process. It makes the data input process less tedious and minimizes human errors. As an example, if there is a request to provision a new device in a location, and the device’s name follows a naming convention, the user would not need the option to set the device name but rely on automation to auto-define it.

###### Note

Data quality is not the sole responsibility of user interactions but a shared responsibility. Following the previous IPv6 example, in a later stage of the network automation process, other validation steps could raise an issue because the IP address is already in use or does not match the routing design.

Data outEvery user needs information, but depending on their role in the automation process, the best data content and format will vary. To illustrate, if the workflow starts via a ticketing system, the data out will likely be an update on the ticket. The data should contain all the relevant information required to understand the outcome of the executed task and use text, hyperlinks, and images as required.

However, do not understand data out as the final workflow execution output. During automated workflow execution, multiple data elements can be exposed to the user to indicate progress or to ask for interaction (for example, a task approval request).

After this brief overview of user interactions, we begin with the description of graphical user interfaces.

### Graphical user interfaces

*Graphical user interfaces* (*GUIs*) serve a myriad of purposes, every one with its own characteristics. In this section, we review three of the most popular GUIs: IT service management systems to make service requests, dashboards to observe the services, and ChatOps to allow human language interactivity.

However, as we go over the architecture’s components described in [Figure 14-1](#net-arch), you will realize that a lot of other tools also offer GUIs, even though their main goal is not to interact with the end user but to offer a low-barrier interface to interact with their functionalities. Most tools offer capable UIs for network engineers but may not be suitable for all end users. Always take into account the end user’s point of view to pick the right tool.

#### IT service management

*IT service management* (*ITSM*) systems, also known as *self-service portals*, offer an entry point to request any type of service available in the organization’s *service catalog*. Every service has a definition of how it will be delivered, containing multiple stages in the process. The simplest implementation performs as a ticketing system that manages the request lifecycle (including approvals, traceability, and notifications).

Naturally, network service offerings have been moving to ITSM services because of its advantages versus other communication systems that make coordination harder, like email loops. But this is just the first step. Using an ITSM doesn’t imply any automation per se. You can manually implement all the steps in the service delivery. The goal of a network automation strategy is to transform the service management steps into tasks that can be performed by a machine. Through the automation journey, you will incrementally improve the process, adding more and more automated tasks. However, it’s not all or none. Sometimes it makes sense to leave some manual tasks or human judgment gates throughout the process.

Modern ITSM platforms come with a lot of features to promote automation because it optimizes delivery time and resource efficiency. Some key ITSM features that support automation are as follows:

- Configurable data input, with validation and conversion to structured data. Keeping simplicity in mind, the user should provide the relevant data needed to deliver the service, and this data should conform to custom conventions that match the expectations of the next steps in the workflow.
- Input integrations to fetch data from several sources to help users. For example, if the user has to enter a location to deliver a service, being able to retrieve the available location from a facility management system makes the input process simpler and more reliable.
- Triggering integrations with external components (via APIs). Automated tasks often require starting an external process, and this process is not going to be completed immediately. The requested system, when done, should be able to notify the ITSM of the operation result and resume the process.
- Notification systems to interact with humans participating in the service delivery—for instance, requesting approval from a qualified team member.

In [Figure 14-2](#servicenow), a screenshot from an ITSM (ServiceNow) ticket shows a new VLAN that has been requested by a user and, once accepted, the change is scheduled and an external Ansible playbook is triggered to execute the change. These kinds of tools, with proper integrations, facilitate user interaction with network automation.

![npa2 1402](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1402.png)

###### Figure 14-2. IT service management

###### Tip

Change management is a subject of its own. We encourage you to get a good understanding of your organization’s change management process to build network automation solutions that fit well into it.

#### Dashboards

On the other side of ITSMs, *dashboards* offer read-only visualization to present a large amount of information in a condensed and effective format. The information may come from a myriad of sources and take multiple forms, depending on the needs of each use case.

In [“Telemetry and Observability”](#telemetry-and-observability), we cover in more detail the use of dashboards to visualize the operational state collected from the network infrastructure. There, you will learn the importance of leveraging normalized and enriched data in order to perform advanced queries to obtain relevant information.

For each purpose, you can find specialized tooling. For instance, in the business intelligence area, you have commercial products like [Tableau](https://www.tableau.com) and [Microsoft Power BI](https://oreil.ly/zw0GJ). IT engineering has its own multiple flavors, and two popular open source projects that have gained a lot of traction lately are [Grafana](https://oreil.ly/IYL46) and [Kibana](https://oreil.ly/cyPyG).

When choosing a dashboard tool, you should consider two key factors:

Data source integrationsHow many existing data source integrations exist? How easy is it to develop new ones? The first point is especially relevant if you have limited capacity in house to develop your integrations, but the reality is that it’s unlikely that integrations would be available for all your data sources. Thus, it’s important that the tooling offers an easy way to develop new integrations (via APIs) when needed.

Dashboard customizationOnce you have data connected, understanding the options to visualize it can make its use more effective. Typical dashboard types are bar/line charts, histograms, heatmaps, and Sankey diagrams. Another important feature is the ability to define these diagrams as code, to make their management more effective and efficient.

#### ChatOps

Nowadays, almost every organization has adopted instant messaging applications. These solutions—including [Slack](https://slack.com), [Microsoft Teams](https://oreil.ly/EJoAY), [Cisco Webex](https://www.webex.com), and [Mattermost](https://mattermost.com)—support asynchronous communication between people. But you can replace a person with a *bot* and expose, in a low-barrier way, some functionalities of the network automation solution. This is commonly known as *ChatOps*.

In a ChatOps bot, you can wrap multiple types of operations, including triggering a workflow, updating the source of truth, or getting the actual state of the network to support troubleshooting while sharing with the rest of the team. This occurs all without exposing all the complexity and simplifies its usability and effectiveness.

In [Figure 14-3](#chatops-example), the output of a ChatOps command from the [Nautobot ChatOps application](https://oreil.ly/1LxPh) locates the switch and interface where an IP/MAC address is connected, using the command `/netops find ip 10.1.1.3`. It’s a conversation that starts with a message, and the automation handles the rest. This is a simple example, but every command can be crafted to the needs of every network team and evolve over time with improvements contributed by the whole team.

![npa2 1403](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1403.png)

###### Figure 14-3. ChatOps example

###### Tip

An interesting benefit of using ChatOps for network operations is the cumulative effect. Your commands will keep improving over time as more and more experience and knowledge are contributed back to the logic. As an example, you may have created an MPLS troubleshooting script that other engineers have been adding more features to over time. Furthermore, if some of these engineers leave the company, their knowledge will persist.

Chat-based interfaces like these could be further augmented with advances in artificial intelligence and natural language processing to provide a more organic, conversational UX in interacting with network automation architectures. For instance, the recently popular ChatGPT (by OpenAI) offers access to a large language model (LLM) that enables humans to “converse” with the model, which generates, word by word, a response according to the context.

This could allow for many impactful features, such as analyzing logs to propose a root cause, translating network device configurations to other platforms, performing configuration compliance analysis, or generating code snippets in any programming language to solve a specific need. On top of that, you can integrate plug-ins that allow interaction with other sources of information via APIs (for example, getting real-time operational data from the network or fetching the network intent from a source of truth).

Even though GUIs are really useful for user interactions, text-based interactions are convenient for some use cases and/or personas. We explore them next.

### Text-based interactions

As with GUIs, you have multiple text-based UIs to consider. Let’s start with an old friend for network engineers: the command-line interface (CLI).

If you have been in network engineering for more than five years, you’ve likely used CLIs to interact with network devices. Even though, as you’ve noticed throughout this book, the trend is to move away from them, CLIs can be a useful way to interact with your network automation solutions because a lot of your network automation users (other network engineers) feel comfortable with them. Actually, if you recap the tools described in [Chapter 12](ch12.html#automationtools), Ansible and Terraform offer a CLI too.

###### Note

You can also build your own CLI. You can use popular libraries for Python (such as [Click](https://oreil.ly/RbouD) or [Rich](https://oreil.ly/Q-xCZ)) or libraries for Go such as [Cobra](https://oreil.ly/VqHqg).

Finally, let’s look at how network automation can create documents and reports for various types of users.

### Documentation and reporting

Each user has different requirements regarding documentation and reporting. Network engineers are used to understanding network designs in diagrams. Leadership members are interested in compliance reports to validate that standards are implemented. Without automation, generating each type of document can be costly, and once created, those documents are instantly outdated because networks are constantly changing. This is when automation comes to the rescue.

In [Chapter 12](ch12.html#automationtools), we showed an example of how to create a report taking actual data, using the Markdown language to be rendered later to HTML. Markdown is not the only markup language that can be used to generate user-friendly documentation. Alternatives include [AsciiDoc](https://oreil.ly/X8f2b) and [reStructuredText](https://oreil.ly/Q0WPP), popular languages to generate documentation *as code*. The final documentation is rendered in the desired format (e.g., HTML, PDF, DOCX, etc.). Other languages are focused on generating diagrams and graphs: [Structurizr](https://oreil.ly/X7UXa) for C4 modeling and [Mermaid](https://oreil.ly/Iayo1) for complex diagrams.

###### Note

This book was written in AsciiDoc format.

Let’s generate a network diagram as code with Mermaid. This could come from a network inventory system or the network state (e.g., LLDP). Imagine that you have a network with two spines and two leaves, and you want to generate a diagram with the network topology and the servers connected to the leaf switches. In the source of truth, the data could look like this:

```
---
connections:
    - side_a: sw1-spine
      side_b: sw1-leaf
      ip_prefix: 192.0.2.0/29
    - side_a: sw1-spine
      side_b: sw2-leaf
      ip_prefix: 192.0.2.8/29
    - side_a: sw2-spine
      side_b: sw2-leaf
      ip_prefix: 192.0.2.4/29
    - side_a: sw2-spine
      side_b: sw1-leaf
      ip_prefix: 192.0.2.12/29
    - side_a: sw1-leaf
      side_b: serverA
      ip_prefix: 10.0.0.0/29
    - side_a: sw2-leaf
      side_b: serverA
      ip_prefix: 10.0.0.4/29
```

And, using the Jinja syntax you learned in [Chapter 9](ch09.html#templating), you can define the following template:

```
graph TD
{% for connection in connections %}
{{ connection.side_a }}({{ connection.side_a }}) ---|{{ connection.ip_prefix }}|
  {{ connection.side_b }}({{ connection.side_b }})
{% endfor %}
```

Bringing both together, you can render the following Mermaid snippet (which can be included in a Markdown document). This code generates the diagram in [Figure 14-4](#mermaid):

```
graph TD
sw1-spine(sw1-spine) ---|192.0.2.0/29| sw1-leaf(sw1-leaf)
sw1-spine(sw1-spine) ---|192.0.2.8/29| sw2-leaf(sw2-leaf)
sw2-spine(sw2-spine) ---|192.0.2.4/29| sw2-leaf(sw2-leaf)
sw2-spine(sw2-spine) ---|192.0.2.12/29| sw1-leaf(sw1-leaf)
sw1-leaf(sw1-leaf) ---|10.0.0.0/29| serverA(serverA)
sw2-leaf(sw2-leaf) ---|10.0.0.4/29| serverA(serverA)
```

![npa2 1404](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1404.png)

###### Figure 14-4. Network diagram as code

###### Note

You can render Mermaid diagrams with the live editor available at [*https://oreil.ly/3ihAv*](https://oreil.ly/3ihAv).

Being able to generate *live* documentation provides access to data in almost real time and in a consistent format that can be reproduced and adapted as needed—moreover, with much less effort. You define the logic once, and you get the outcome many times. Because the data used can be provided from either the desired or the actual state, you can easily provide snapshots of one or the other. Therefore, you can generate the desired network design (from the source of truth) or represent the actual network status (from the operational state).

After reviewing some basic characteristics of user interfaces, we transition next to the cornerstone of any network automation solution: defining *how* the network should be.

## Source of Truth

In this book, we have mentioned several times how every automation solution must be built on top of structured data. However, this is not a new idea. As you will see in [“Data use cases”](#data-use-cases), concepts such as data center infrastructure management and IP address management have been around for a while. The big shift now is that data is no longer used only for documentation or as a representation of what is deployed. When network automation kicks in, the data will drive the network operations.

The *source of truth* (*SoT*) is a broadly accepted concept in the industry that indicates the *intended* state of the network. Even though the name *source of truth* is singular, it’s an abstract concept that may be implemented by one or more systems. However, as you will see in [“Data quality”](#data-quality), it should *behave* as one consistent data set.

Adopting the SoT as the pillar of network operations is likely the biggest mental shift for a network engineer. We have been used to describing the network design in documents or diagrams. However, as introduced in [“Documentation and reporting”](#documentation), the paradigm changes and the authoritative reference becomes the SoT that later renders into the most appropriate format to consume the data. Only after adopting an SoT strategy that defines the intended state of the network can you successfully deploy network automation.

The role of the network engineer in an automated network includes managing data in an SoT. They define what the network state *should be* as the intent. And this intent is represented as *structured data*. If you are already defining YAML fines in a Git repository, you may have already started deploying an SoT strategy without knowing it. The data will be used by other architecture components to change and validate the operational state.

###### Tip

A data-first strategy to drive network management will save you a lot of manual work and unexpected errors while translating from the network design to the actual configuration artifacts.

As the scope of automation grows, the SoT also grows. What initially starts as data populated by humans, or as one-time import scripts, could eventually incorporate data managed by third-party systems that must be integrated to have a consolidated representation of the intended state of the network. Like any data management process that collects, normalizes, and persists data (also known as extract-transform-load, or ETL), it must be carefully designed to keep the SoT’s data in good shape. For example, you may have in the SoT all the interfaces and circuits described, but the intent of these circuits may vary over time because of scheduled maintenance. Including the circuit provider’s intent in your SoT will provide more educated data to operate the network.

In this section, we cover several aspects to take into account when designing and implementing an SoT strategy:

Data qualityThe SoT is all about data, and it’s going to be as good as the data it manages. Even though the definition of data quality may have several interpretations, we explain the basic dimensions to assess.

Data use casesThe SoT concept applies to any IaC solution. Focusing on network-related data use cases would give you a more concrete example in this domain.

Data modelingMaybe one of the most critical aspects when working with data is to define the right data models. These should be good enough to define the network intent but simple enough to facilitate data operation.

PersistenceTo keep our network working without disruptions, the data that defines its state must persist. We have several options, with pros and cons to consider.

Data populationTo finally use the SoT requires populating data into it. We will comment on the most common approaches.

Distributed SoTAs we introduced previously, the SoT may be composed of many data systems that require integration to provide a consistent network intent as a whole.

Let’s start with defining what we understand as *good data*.

### Data quality

In any automation solution, data is king. It is the data that is going to be used by the automation engine to ensure that the network intent is applied to the network infrastructure. Therefore, this network infrastructure state will be as good as the data used. You must ensure that the data adheres to quality principles to be considered reliable. This is what we understand as *data quality*.

Even though its definition may vary among data domains, we recommend keeping the following questions in mind to help you understand whether your data complies with basic quality principles. As an example reference, let’s assume your goal is to generate a BGP configuration for a network device; the questions are as follows:

CompletenessDoes this data cover all the necessary information to fulfill the network operation needs? Are all the BGP attributes defined so the final configuration is complete?

ConsistencyIs the data holistically providing a consistent view, or do conflicts exist? If the BGP attributes are coming from two data sets, one containing the BGP peerings and the other the IP addresses, a one-to-one mapping should exist between them, without overlaps.

ValidityIs the data adhering to the business rules and in the proper format? If the BGP neighbor is defined as an IP address, that data should adhere to the expected format and values. A value of `300.1.1.1` should not be accepted as an IPv4 address.

UsabilityIs the data easy to modify and consume? Your system may need to expose via API the addition of BGP peers, and then use the data to render the proper configuration.

RelevanceIs the data relevant at the right moment in time? Past, present, and future? Maybe you want to deprovision a BGP peer, so the data should express the desired status now and also be available to expose the previous status for reporting.

AccuracyHow well does this data reflect the network intent? Are there any gaps between the design and the data models storing it? To improve the accuracy of the BGP peer IPs, you could add a validation of the peer IPs and the ASN to check whether both belong to the same entity.

###### Note

You can delve deeper into data quality with the following books: [*Data Quality Fundamentals*](https://learning.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) by Barr Moses et al. (O’Reilly) or [*Fundamentals of Data Engineering*](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/) by Joe Reis and Matt Housley (O’Reilly).

Next, before exploring the challenges of data management in the SoT, we present the common data use cases in a network SoT.

### Data use cases

The data models you need for describing your network’s intended state have likely already been defined by someone else. Unless you have very specific needs, we recommend getting started with solutions that already come with battle-tested models and easy extensibility to adapt to your needs.

In this space and as open source projects, some tools address only one use case—for example, [NIPAP](https://oreil.ly/LDAGI) to manage IP addresses or [Peering Manager](https://oreil.ly/NdZJ4) to manage BGP peerings. Others try to cover more data use cases in one tool, such as [Nautobot](https://oreil.ly/c18X_) and [NetBox](https://oreil.ly/Gs224). In all these cases, you get out-of-the-box opinionated data models ready to use.

###### Note

In this section, we use the Nautobot public demo instance, available at [*https://demo.nautobot.com*](https://demo.nautobot.com), to illustrate the content type examples because it covers all of them, but you could get similar data models from other projects.

We will explore a few Nautobot network models via its REST API. You could complement this exploration via the GUI to get a more visual representation. With this code snippet, you are ready to start interacting via the Python Requests library using the demo token:

```
>>> import requests, json
>>> url = "https://demo.nautobot.com"
>>> token = "a" * 40
>>> headers = {"Authorization": f"Token {token}"}
```

We start with the network inventory, or more generally, infrastructure inventory. It must contain all the devices under the scope of automation, and it serves as the reference for the rest of the data use cases.

#### Network inventory

As you may recall from our Ansible, Nornir, and Terraform coverage in [Chapter 12](ch12.html#automationtools), the inventory data is fundamental. In Ansible and Nornir, it comes with connection details and extra variables attached to each element. On the other side, for Terraform, the inventory is defined as the variable data to provision the infrastructure resources.

There is no strict definition of what an inventory item contains, but the following list is a good summary of the most common attributes:

NameA human-friendly identifier of the device.

LocationWhere the device is placed. For example, in an on-premises environment, it could be a rack within a data center, and in a cloud platform, the region.

TypeWhich type of network service/platform? It could be the device model or the type of network cloud service.

Connection detailsHow to connect to manage the device. If it’s a standalone device, the details would be its IP or FQDN, and if it’s a cloud service, a well-known API. Proper credentials must be provided to get the right level of access to the management.

StatusTo represent the intended state of the object. For instance, whether it’s *active* or *planned*.

In [Example 14-1](#nautobot-devices), the Nautobot REST API retrieves the *devices* that in Nautobot represent part of the inventory (other options exist, but we leave them out for simplicity).

##### Example 14-1. Exploring a Nautobot device as inventory

```
>>> response = requests.get(f"{url}/api/dcim/devices", headers=headers) 
>>> devices = response.json()["results"]
>>> print(json.dumps(devices[1], indent=4))
>>>
{
    "device_role": {"name": "edge"},
    "device_type": {"model": "DCS-7280CR2-60"},
    "id": "9d512f81-5523-456d-8508-506da78fe6e2",
    "name": "ams01-edge-01",
    "platform": {"name": "Arista EOS"},
    "primary_ip": {
        "id": "6983eaad-3b82-46c8-8533-ffa382508895",
        "address": "10.11.128.1/32",
    }
    "site": {"name": "AMS01"},
    "status": {"value": "active"},
    # Output trimmed for brevity
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

It uses the `url` and `headers` variables defined previously.

In [Example 14-1](#nautobot-devices), you can observe (some of) the attributes of a device exposed via the REST API. If you explore the result by yourself, you will see much more data that is aggregated from other data use cases related to this device model as the anchor reference.

# REST API Versus GraphQL

REST APIs, explained in [Chapter 10](ch10.html#apis), are the most popular way to interact programmatically with applications. However, other API protocols can be extremely helpful when data needs to be aggregated and customized by the client. *GraphQL*, developed by Meta (formerly Facebook), can achieve in one single API call what would require several when using REST.

In this example, you can easily compare how to get the same data. The GraphQL API allows embedding a *query* that defines exactly what needs to be returned. Using the REST API, you need to access multiple REST API endpoints one by one (green/dotted lines) and, finally, combine the data in the client. On the other side, in GraphQL, the client accesses only one endpoint (red/dashed lines) with a *query* that defines exactly which information is needed.

![npa2 1405](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1405.png)

###### Figure 14-5. REST versus GraphQL APIs

Let’s reproduce [Example 14-1](#nautobot-devices) but using a *query* definition that gets passed to the API path via the POST method. The query may contain filters with variables, and the nested attribute selection within connected models (e.g., select the `name` under `platform`):

```
>>> query = """
... query {
...   devices (name: "ams01-edge-01"){
...     name
...     platform {
...       name
...     }
...   }
... }
... """
>>> response = requests.post(
...     f"{url}/api/graphql/",
...     json={"query": query},
...     headers=headers,
... )
>>> print(json.dumps(response.json(), indent=4))
{
    "data": {
        "devices": [
            {
                "name": "ams01-edge-01",
                "platform": {
                    "name": "Arista EOS"
                }
            }
        ]
    }
}
```

We don’t cover GraphQL in detail here, but hopefully this brief comparison has shown you some of its unique benefits in contrast to REST APIs. GraphQL can allow you to be more *effective* in retrieving the data you want, while also being more *efficient*, requiring far fewer requests to retrieve the data. You can extend your knowledge through the official [GraphQL learning page](https://graphql.org/learn).

Once the inventory is in place, it’s time to enrich the data with other related content.

#### Data center infrastructure management

In physical network environments, *data center infrastructure management* (*DCIM*) defines how the network devices should be placed and connected. It may include information about the racks, device hardware, power feeds, cables, circuits, or any other details required to build the network physically.

[Example 14-2](#nautobot-tracing) uses the device from [Example 14-1](#nautobot-devices) to retrieve the *intended* cable tracing, from its first interface to another device.

##### Example 14-2. Exploring Nautobot cable tracing

```
>>> device_id = '9d512f81-5523-456d-8508-506da78fe6e2'
>>> response = requests.get(
>>>     f"{url}/api/dcim/interfaces/?device_id={device_id}", headers=headers)      
>>> interfaces = response.json()["results"]
>>> response = requests.get(
>>>     f"{url}/api/dcim/interfaces/{interfaces[0]['id']}/trace", headers=headers) 
>>> trace = response.json()                                                        
>>> print(json.dumps(trace, indent=4))
[
    [
        {
            "device": {"name": "ams01-edge-01"},
            "name": "Ethernet1/1",
            "cable": "e1472be1-056b-4b4d-b135-e5c287d9b570"
        },
        {"status": {"value": "connected",},},
        {
            "device": {"name": "ams01-edge-02"},
            "name": "Ethernet1/1",
            "cable": "e1472be1-056b-4b4d-b135-e5c287d9b570"
        }
        # Output trimmed for brevity
    ]
]
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We retrieve the interfaces for a specific device using its ID.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

For a specific interface ID, we retrieve the trace for the cable.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The trace information contains both ends and other information such as the state.

The DCIM data can be used for multiple purposes, from providing accurate guidance for on-field engineers to serving as the reference to validate the network topology by comparing it with the state. If the retrieved LLDP information from a connected interface shows different information than the intent, for example, we know that a mismatch needs to be solved.

###### Note

Even though this content type could seem irrelevant for cloud-based network services because there are no racks, console cables, or cables (exposed to the consumer), some of this content can be reused and adapted as *virtual* concepts—for example, virtual interfaces or virtual circuits.

#### IP address management

Tools for managing IP address objects have been around for a while because of the conflicts that an IP address/prefix overlap may cause. IPAM solutions have usually been wrapped as DDI platforms: DNS, DHCP, and IPAM, because all three typically share common relationships.

In [Example 14-3](#nautobot-ipaddress), we reuse the `primary_ip` identifier from the device to explore, in more detail, all the attributes contained in the IP address model such as the DNS name, the attached VRF, or the NAT mapping.

##### Example 14-3. Exploring the Nautobot IP address

```
>>> ip_address_id = "6983eaad-3b82-46c8-8533-ffa382508895"
>>> response = requests.get(
>>>     f"{url}/api/ipam/ip-addresses/{ip_address_id}/", headers=headers)
>>> print(json.dumps(response.json(), indent=4))
{
    "family": {
        "value": 4,
        "label": "IPv4"
    },
    "address": "10.11.128.1/32",
    "assigned_object_type": "dcim.interface",
    "assigned_object": {
        "device": {
            "name": "ams01-edge-01"
        },
        "name": "Loopback0",
        "cable": null
    },
    "dns_name": "edge-01.ams01.atc.nautobot.com",
    # Output trimmed for brevity
}
```

#### Network properties

This category includes any other network-related data that is required to define the intent of your network. These properties will differ depending on each network design. In this group, we can find VLANs, ACLs, VRFs, BGP, OSPF, or any network services, including DNS or NTP.

The myriad network protocols and features are more specialized than the previous ones that are common in all the networks. Because of this, there are fewer predefined data models available in the general-purpose SoT projects, but it is evolving as network automation adoption is becoming mainstream.

###### Note

Don’t confuse the data models defined in the SoT with the data models used by model-driven protocols (e.g., NETCONF or gNMI). Both are data models but with different purposes. The latter should be complete and cover all the potential use cases a network device supports. But in the SoT, the data model should be as simple as possible to improve manageability while addressing your network design needs. We provide more details in [“Data modeling”](#data-modeling).

Still exploring Nautobot, in [Example 14-4](#nautobot-bgp), you can see how a BGP peer endpoint is modeled.

##### Example 14-4. Exploring a Nautobot BGP model

```
>>> response = requests.get(
>>>     f"{url}/api/plugins/bgp/peer-endpoints", headers=headers) 
>>> bgp_peer_endpoints = response.json()["results"]
>>> print(json.dumps(bgp_peer_endpoints[0], indent=4))
{
    "routing_instance": {
        "display": "dfw01-edge-02 - AS 65535",
    },
    "source_ip": {
        "address": "10.9.192.10/32"
    },
    "autonomous_system": null,
    "peer_group": {
        "name": "EDGE-to-LEAF",
    },
    "peer": {
        "display": "dfw01-leaf-02",
    },
    "import_policy": "",
    "export_policy": "",
    "secret": null,
    # Output trimmed for brevity
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The BGP model is not included in the core application but as extensions under the `/api/plugin` endpoint.

It may happen that you can’t find a preexisting data model for the network services you are interested in. Don’t stress; you can always craft your own data models, either extending existing solutions on top of databases (as in [Example 14-4](#nautobot-bgp)) or simply using structured data (JSON or YAML) and storing it in Git. You will understand the implications of each approach in [“Data modeling”](#data-modeling).

#### Configuration templates

The data represented in the SoT should be agnostic to the platforms where the network services will be running. The data should work well for different vendors, versions, or network interfaces. Thus, at this level of abstraction, the data can’t be directly used to configure the network infrastructure. If you can use it directly, then, the data model is likely so specific that it could not be reused for other platforms.

To fill the gap between the data in the SoT and the required configuration artifact syntax for each platform and interface (e.g., CLI, XML, or JSON), you can use configuration templates. As you learned in [Chapter 9](ch09.html#templating), you can use Jinja templates or equivalent solutions to *render* the configuration artifacts that you will put into action in [“Configuration management”](#configuration-management).

Because of their nature (they don’t get too much benefit from database features), configuration templates are usually stored in version control systems such as Git. This allows a peer-review process and continuous integration (to validate the syntax and/or the expected operational state) to enforce that the rendered configuration is consistent with the network infrastructure expectations.

###### Tip

When testing configuration templates, keep the template’s input data and expected output consistent, avoiding testing two aspects at a time.

After covering the most representative data use cases in the networking area, next we review recommendations for creating *good* data models to represent them.

### Data modeling

The SoT data models must be capable of describing the intended network state, but, at the same time, they should provide the right level of accuracy, completeness, validity, and usability. You need to find the right balance.

Defining data models requires the ability to translate a network design into data structures that can represent it. As already covered in detail in [Chapter 8](ch08.html#dataformats), data formats (e.g., JSON or YAML) allow us to serialize structured data, and data modeling languages (e.g., YANG) let us define the rules and relationships of the data regarding a specific use case.

The data modeling can leverage group-based design to simplify the amount of data. Suppose that all the upstream interfaces use a common set of attributes (e.g., MTUs and VLANs); these attributes can be grouped in a role type that applies to multiple interfaces at the same time.

Luckily for you, you won’t always need to create your own data models. If you are using an existing SoT project, like Nautobot or NetBox, they come with opinionated models that have worked well for other networks. However, you would likely need some customization to represent your own network design. This is where options for extending existing data models, with new attributes or links to other data use cases, would be helpful.

If you don’t find a capable data model, your last resort is to create it from scratch. You can use data models from other SoT projects or complete data models used as configuration artifacts, such as the models defined in YANG by the OpenConfig consortium or the IETF.

#### A structured approach

Coming up with a final data model to support your network design may take a while, and usually an incremental and iterative approach is recommended (especially in brownfield network environments). The following steps may help you structure this process:

1. Understand your network design. Find out which configuration items are static or variable, and identify patterns at different levels to reduce the amount of data required. Having a simple network design will make things easier.
2. Define the scope. Limit the network environment to model, and use it as your inventory. You don’t need to automate the whole network at once.
3. Choose some part of the configuration. Modeling a full configuration may be a complicated task. But you can start small and model only some configuration sections to get started and show value.
4. Sketch the data model. Define the data structures required to track the variable data of the configuration part (you will use representative configuration snippets from the selected inventory), understanding where the data will be stored. The static data will go into configuration templates.
5. Create the configuration templates. Establish the configuration templates to create the configuration artifacts using the variable data coming from the data model. To support multiple network platforms and interfaces, you will verify that the data model is capable of solving various use cases.
6. Start using the model. Get started with low-risk tasks, such as validating configuration compliance (more in [“Configuration management”](#configuration-management)), that will show the value of using the SoT as the north star of the network automation.

#### Data modeling example

Let’s do a small exercise to help you understand what data modeling looks like in a real scenario.

First, you get the actual interface configuration snippets from various vendors and for some network devices (the scope):

*Cisco IOS*

```
interface gigabitethernet 1/0/2
 ip address 192.0.2.1/24
 switchport mode access
 switchport access vlan 123
```

*Juniper Junos*

```
set interfaces ge-1/0/2 native-vlan-id 123
set interfaces ge-1/0/2 unit 0 family inet address 192.0.2.1/24
set interfaces ge-1/0/2 enabled
```

From the configuration, you observe that each interface configuration has some values that change (the interface name, IP address, and VLAN ID) and others that remain constant (the mode access and the *enabled* mode).

Sketching the *interface* data model using YAML format, covering multiple interfaces, results in the following:

```
interfaces:
  - name: "gigabitethernet 1/0/2"
    vlan: 123
    address: "192.0.2.1/24"
```

Notice that the data model works well for both vendors. Then it’s time to define the Jinja templates that work well with the data model, as you have seen in Chapters [9](ch09.html#templating) and [12](ch12.html#automationtools):

*Cisco IOS*

```
{% for interface in interfaces %}
interface {{ interface["name"] }}
 ip address {{ addr["address"] }}
 switchport mode access
 switchport access vlan {{ interface["vlan"] }}
{% endfor %}
```

*Juniper Junos*

```
{% for interface in interfaces %}
set interfaces {{ interface["name"] }} native-vlan-id {{ interface["vlan"] }}
set interfaces {{ interface["name"] }} unit 0 family inet
  address {{ interface["address"] }}
set interfaces {{ interface["name"] }} enabled
{% endfor %}
```

And, combining both, you are ready to re-create your intended configuration from the SoT. It’s important to note that both the data model and the templates work together to create the configuration artifacts, and when data does not change, it is stored in the templates.

As you may guess, the data in the SoT must be persisted, and choosing one option or another will come with different trade-offs.

### Data Persistence

Defining a data structure and saving its content in memory is only the first step to storing the network intent. This data must be available at any point in time, even though the ingestion system goes down.

We have several options to persist the data, and deciding one way or another will come with different features and constraints. We focus on two popular options to store the SoT data:

Version control systemStoring files in a version control system like Git (covered in [Chapter 11](ch11.html#sourcecontrol)) is more accessible for collaboration, and offers great historical traceability and rollback functionality.

DatabaseStoring data in a proper database gives us a structured, schema-driven way to store and organize our data, and guarantee scalable and efficient consumption of that data.

###### Tip

Most of the time, the final SoT solution will be composed of different persistence options, taking the best of each type. We go deeper into this topic in [“Distributed source of truth”](#dsot).

Beyond the scope of this book but worth mentioning is the a set of properties known as [ACID](https://oreil.ly/HLlR3) that define how a data transaction should behave. With that noted, let’s do a quick overview of the characteristics of these two common persistency options.

#### Version control systems

From [Chapter 11](ch11.html#sourcecontrol), you are already aware of the benefits of using version control systems to manage files. This approach empowers the collaboration of multiple engineers working on the same files and introduces requirements to *merge* their work. These files can contain any kind of data: a script, a Jinja template, or structured data (e.g., YAML or JSON).

Using a version control system makes integration with CI pipelines easier (as seen in [Chapter 13](ch13.html#cicd)). This integration facilitates running validation tests on any change in the data. For example, a version control system can check whether the result of rendering the data with the templates is creating a valid configuration artifact. Finally, via peer review, you can make sure that any update on the SoT has been reviewed and accepted by more than one engineer. Also, because the *history* comes for free, it’s trivial to check who added a new ACL entry a few months ago.

###### Note

Using Git to manage infrastructure operations is known as *GitOps*. Integrating code with pipelines enables powerful collaboration and automation, such as kicking off a configuration deployment process (see [“Configuration deployment”](#config-provisioning)).

However, this ingestion process, which works well for updating some types of data or configuration templates, can become cumbersome when the SoT is updated frequently or is integrated with other data sources, such as a service portal. Also, data consumption is limited to managing structured data files, without a query language that could provide convenient data manipulation for read and write operations. You can’t use relationships as in databases, and the only option is to create static references between objects in the structured data files.

You should not forget about enforcing data validation when using structured data documents. As mentioned in [Chapter 8](ch08.html#dataformats), every one of these formats has available some schema validation tools, like JSON Schema, to make sure that the data conforms to predefined rules. Using schema definitions will save errors on data ingestion (running in during the CI pipeline) or on data consumption (fetching data from an external source).

#### Databases

Databases are the most popular ways to store and consume data. The most popular type, the *relational* database, organizes data in *tables* (representing an object type), and every *column* represents an attribute or an interconnection to other tables via *relationships*. Using the database *schema*, you can enforce constraints such as uniqueness or type of attributes. In [Example 14-1](#nautobot-devices), you can infer that the *device* and *site* are stored in different tables, with a relationship between them (for example, Nautobot and NetBox use a relational database). To consume the data, SQL allows sophisticated queries to read or write exactly the data you want. Many open source SQL databases exist, such as [MySQL](https://oreil.ly/NPIoV), [PostgreSQL](https://oreil.ly/C8bmn), and [MariaDB](https://oreil.ly/w__yL).

###### Note

Learning SQL is not mandatory at all for a network engineer. You will find multiple frameworks that allow using SQL via a programming language. However, if you want to apply advanced features, we recommend reading [*Learning SQL*](https://learning.oreilly.com/library/view/learning-sql-3rd/9781492057604/), 3rd Edition, by Alan Beaulieu (O’Reilly).

Nowadays, we have other types of databases, known as *NoSQL* databases. Without the *relational* characteristic, there is more flexibility to define the data models, optimizing for different aspects such as scalability or performance. It’s beyond the scope of this book to provide a detailed analysis of these types. Regarding the SoT or IaC, the *Graph* databases offer a more intuitive representation between entities (nodes) and the properties of these relationships (edges). Two examples of this type are [Neo4j](https://oreil.ly/V-ntH) and [EdgeDB](https://oreil.ly/pPSYk).

#### When to use Git or a database

There is no simple answer when you’re trying to decide between using Git or a database. *It depends*. The most common scenario, in complex network automation solutions, is to have a mix of both to get the best of both worlds.

The rule of thumb is to store data that doesn’t change often (usually coming from the network architecture team) in Git, and store information that changes frequently (usually coming from the users or the network operations team) in databases.

For example, say you need to create an automated solution for managing firewall rules exposed to the user (which you’ll see in [“Understanding the Architecture with an Example”](#architecture-example)). The firewall rules will go into the database, enforcing valid attributes, because frequent changes are likely expected. In parallel, in Git, you may have an *acceptable* firewall policy defined and maintained by the security team and used to validate that the firewall rules adhere to it before deploying them.

###### Note

The dilemma of choosing between Git and a database is something that new databases are trying to solve by offering a Git-like operation on top of SQL. One example of this approach is [Dolt](https://oreil.ly/y2yXc), an SQL database with documentation describing it as “Git versions files, Dolt versions tables. It’s like Git and MySQL had a baby.”

So far, you have learned how to define data models ([“Data modeling”](#data-modeling)) and how to store them to build an SoT. The next step is to get data in.

### Data population

Once your SoT is ready to use, it’s time to populate the data that defines your network intent. As introduced in [“Data use cases”](#data-use-cases), you’ll have different types of content to define. You need to set up the inventory first and then, incrementally, enrich it with more data as required by your network automation solution.

How to get started depends mostly on whether your network is already running (a brownfield environment) or only planned and will be provisioned afterward (a greenfield environment).

#### Brownfield environments

In a brownfield environment, the network is already up and running. A reasonable assumption is to take the actual operational state as the *initial* intended state. To import this state, a common approach is to define a one-time operation (per device) to retrieve the configuration from the network devices (with a predefined list of devices or via auto-discovery) and convert it into the SoT data models.

###### Note

You may argue that retrieving the configuration from network devices is *never a one-time operation*. Well, the idea is to trust the actual configuration state then, and from now on, always give precedence to the data present in the SoT. So, later configuration retrievals will be used to compare and understand whether a drift has occurred.

However, this import process requires curation. Assuming that no automation was in place before, the configuration across the network likely won’t be 100% consistent, so you can’t trust all the data as valid. For instance, the VLANs in an interface may include some leftover ones. When your import process detects issues, it could try to autocorrect them, follow some rules, or raise a warning to manually correct them.

After this first load, you must flip the paradigm (if not, you will be in an endless loop). From now on, the SoT data represents the desired state, and any subsequent changes should be reflected there first. This applies only to the configuration defined from the SoT. In brownfield environments, it’s common to start with only some coverage and leave some configuration out of the SoT in the initial stage, to import later after automation has been working.

#### Greenfield environments

In a greenfield environment, you might start by defining the network intent in the SoT and configure the network afterward. Defining this intent may require you to manually input a lot of data, to represent all the configuration aspects your network requires. This may become a tedious process.

To make things easier and more consistent, we recommend you use automated processes to generate all the necessary data from the minimum input data. To show you what we mean, to create a complete leaf-and-spine data center architecture, the automation could require only the location and the number of leaves. Automatically, using design logic, an automated process would create the required definition of leaf and spine devices, their interface configuration and cable interconnection, IP addresses, routing protocol setup, and any other necessary data.

###### Tip

Automating data generation for new deployments lowers the adoption barrier of the SoT strategy and allows enforcing a consistent network design.

Finally, the last topic to cover is how to operate with a distributed SoT.

### Distributed source of truth

Throughout this chapter, we refer to the SoT as a single entity. The reality proves to be slightly different. Most organizations maintain data relevant to network management in different data sources. For instance, the network inventory data may be part of the company-wide asset management system, and the IP addresses may be defined together with DHCP and DNS configuration.

The data management strategy may need to align with organizational (e.g., allowing domain-specific policies) or technical (e.g., representing specific data use cases) constraints—and in this case, both must be taken into account when designing this part of your network automation architecture. However, the goal of the SoT remains the same: to represent a consistent network intent. Thus, a key aspect is to identify which data store owns each data set, also known as the *authoritative source* or a *system of record (SoR)*. Honoring data ownership is crucial to avoid data inconsistencies.

Designing a data management solution that includes a distributed SoT can be done in several ways:

Establish integrations with every data storeThe SoT consumer defines and manages integrations with every data source. This decentralized approach offers higher flexibility than a centralized approach, but implies more complexity on the customer side because it has to implement data validation and normalization and define the logic to interconnect data coming from each source. Furthermore, the complexity of this full-mesh integration (between consumers and data sources) grows exponentially.

Consolidate data into a single SoTThe strategy here is aggregating data from multiple data stores into a single entity that adapts and combines the data in a centralized fashion. This makes the clients’ implementation and data management much simpler. Also, it allows source data enrichment, extending the original model with extra information available in the central source of truth. Sometimes this aggregation means decommissioning the original source, and other times, the source remains as the SoR, so the aggregated data is only read-only (to keep consistency). In this second case, we have to keep in mind the implications of data being temporarily out of sync for a while (during the time between the sync and the present).

Aggregate data stores behind one facadeThis approach offers a single pane of glass for the network intent, but data is not stored in a single place but aggregated on-the-fly. It’s a similar pattern to API gateways, which aggregate multiple APIs behind a single one. This aggregation enforces data validation and normalization in each integration and takes the data directly from the SoR. However, it is more complicated to enrich the data and fulfill custom needs because the process requires creating new properties to extend the original objects.

###### Tip

In our experience, in the distributed SoT environments, the most sustainable strategies are consolidating and/or aggregating data stores, simplifying the client-side implementation, and offering a central place to control the SoT.

Once the network intent is defined in the SoT, it’s time to start using it. This is the role of the automation engine component.

## Automation Engine

The automation engine encompasses the operations to manage the network state and perform network tasks such as upgrades. You learned about tools to build automation engine tasks in several chapters. In [Chapter 12](ch12.html#automationtools), you learned about tools to manage infrastructure, including Ansible, Terraform, and Nornir. In [Chapter 10](ch10.html#apis), you learned about the most popular interfaces and libraries for interacting with network infrastructure (e.g., NETCONF, RESTCONF, gNMI).

The first thing to recall, from [Figure 14-1](#net-arch), is that this block interacts with the network infrastructure, together with the telemetry and observability blocks. However, there is a big distinction. While the latter focus on data collection, the automation engine *impacts* the network state, so you should proceed carefully. We have two key recommendations:

- Get started by implementing dry-run tasks to gain confidence in the automation. This execution mode should provide a detailed report of what would change in the network infrastructure before it actually happens.
- Leverage continuous integration ([Chapter 13](ch13.html#cicd)) and emulation solutions ([Chapter 5](ch05.html#developmentenvironments)) to validate the effect of changes before deploying in production.

This section will help you understand, at a high level, the key functions of this architecture component. It can be split into two main groups: configuration management and operations. Other tasks may not fall into these categories, but most of them do.

Choosing the best solution(s) depends on several factors (remember to always consider the *buy versus build* dilemma):

Supported network interfacesThe network infrastructure in use strongly influences the available options. However, usually you will have several options, each with the characteristics mentioned in [Chapter 10](ch10.html#apis).

Existing toolingIf you are not starting from scratch (some automation is already in place), you should always assess reusing existing tools before adopting new ones.

Team skillsAny automation solution requires you to set it up, maintain it, and operate it. Choose the solution that better fits your team by considering questions like programming language versus data formats.

IntegrationsVia either user interaction or APIs, it’s important to define how automation users or automated processes (respectively) will interact with the automation engine tools.

###### Tip

Don’t overthink your tooling choices. If the goal and scope are well-defined, jumping from one to another will be easy when needed.

### Configuration management

The main goal of most network automation solutions is to automatically manage the network state. But, zooming in, you can identify four stages that can be incrementally adopted to fulfill a complete configuration management solution; see [Figure 14-6](#config-management).

![npa2 1406](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1406.png)

###### Figure 14-6. Configuration management

The four stages are as follows:

Configuration backupRetrieves and persists the configuration state of the network, to be used as the reference of the actual state. The configuration backup can also be used to return the network to a previous state (e.g., via a rollback operation).

Configuration renderingCreates the proper configuration artifacts (per interface), combining the data and templates from the SoT.

Configuration complianceCompares the actual configuration (from configuration backup) with the intended one (from configuration rendering), and calculates the drift between them.

Configuration deploymentUpdates the state of the network infrastructure using the proper configuration artifacts generated in the configuration rendering. It may include some processing to move the configuration state from where it is to where it should be.

###### Tip

A few open source solutions offer all four configuration management features together. [Nautobot Golden Config](https://oreil.ly/lo6br) provides a framework to implement all but the deployment stage (at the time of writing).

#### Configuration backup

Configuration backup and archiving have been around for a long time. You may be familiar with [RANCID](https://oreil.ly/CQAF6), a popular tool for maintaining router configuration files in Git or Subversion. This and similar solutions have been used long before network automation was a trend, with the main purpose to retrieve and store configurations from devices. These configuration files were used to compare the state between specified moments in time and to roll back configurations to a *stable* point when an undesired behavior was observed.

[Example 14-5](#config-backup-example) compares two configuration outputs by using versioning capabilities to spot the differences.

##### Example 14-5. Configuration backup diff

```
$ git diff
diff --git a/nyc/nyc-leaf-02.infra.ntc.com.cfg b/nyc/nyc-leaf-02.infra.ntc.com.cfg
index 0f3fa95..4e14e60 100644
--- a/nyc/nyc-leaf-02.infra.ntc.com.cfg
+++ b/nyc/nyc-leaf-02.infra.ntc.com.cfg
@@ -189,9 +189,9 @@ ip route 0.0.0.0/0 10.0.0.2
 router bgp 65255
    router-id 10.0.20.7
    neighbor 10.11.11.17 remote-as 65253
-   neighbor 10.11.11.17 maximum-routes 12000
+   neighbor 10.11.11.17 maximum-routes 14000 
    neighbor 10.11.11.25 remote-as 65253
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The BGP `maximum-routes` parameter changed.

Using version control systems is the most common way to store backup configurations because of the features around file versioning and comparison. But if you are storing your backup configuration files in clear text, be sure to remove any secret before persisting it—for instance, the BGP MD5 keys or the user (hashed) passwords.

###### Note

Comparing configuration artifacts (we are not talking only about CLI) is useful to understand changes between configuration states, but keep in mind that the intended configuration is always the one coming from the rendering of data from the SoT. Use it as your reference.

#### Configuration rendering

A solid network automation solution defines the intended state in the SoT (see [“Source of Truth”](#source-of-truth)). But this intent is useless if we can’t translate it into actual configurations, adapted to each networking platform. This is exactly the role of the configuration rendering. It combines data (explained in [“Data modeling”](#data-modeling)) with templates (covered in [Chapter 9](ch09.html#templating)), both part of the SoT, to create the configuration artifacts expected by the network infrastructure (see [Chapter 12](ch12.html#automationtools) for a configuration rendering example with Ansible).

The configuration rendering uses the inventory as the starting point and extends the data with related data—for example, IP addresses, interfaces, circuits, and any other relevant content types, as expected by the template. This data manipulation process usually involves a hierarchy for combining and merging the data. Imagine you have global NTP servers, but for some locations, you may have different servers. When incorporating the NTP servers into the device data, you should take the more specific ones. This is the rule of thumb—the more specific wins—but in some cases, you may want to use *weights* to have more control over the logic.

###### Tip

Every network can embrace automation. However, the effort and complexity in automating a *standardized* network versus one without clear patterns (also known as a *snowflake*) differ significantly. If every device has its own configuration knobs and custom design, the number of statements in your automation solution would result in spaghetti code that’s hard to maintain and extend. We strongly recommend that before starting the configuration management journey, you take a while to reflect on your standard network design and the exceptions that need to be corrected eventually. This will make your automation effort more efficient and robust.

Being able to render the *intended* configurations, partial or complete, is a great step toward commanding your network from the SoT. In brownfield environments, it makes sense to start with only a subset of the configuration to gain confidence incrementally. In new network deployments, configuration rendering is an opportunity to build the full configuration from scratch, to drive the network from the beginning.

#### Configuration compliance

Once you have the actual configuration (from backup) and the intended one (from rendering), you are ready to see whether the configuration state is in sync or some deviation exists. This is the goal of configuration compliance.

Becoming aware of configuration inconsistencies (the first step in a *network assurance* strategy) opens the door to, eventually, remediating them. The final goal is to automate the process end to end, but getting started on the automated configuration management is helpful, as this read-only operation is low-hanging fruit. We strongly recommend checking configuration compliance regularly to detect deviations (maybe introduced by a manual intervention), to bring the network back to matching the network’s intended state.

Configuration compliance applies to all types of configuration artifacts: CLI-based or API payloads (JSON, XML, YANG). Indeed, comparing structured data is easier, but when the configuration is not structured (CLI), parsing it is still possible with tools such as [Batfish](https://oreil.ly/sK1Y8), [Cisco pyATS/Genie](https://oreil.ly/t7N9p), or [NTC Templates](https://oreil.ly/baeb9); see [Chapter 10](ch10.html#apis) for an example.

###### Note

Even though CLI-based configurations are harder to manage (expect some vendor formatting weirdness, including reordering of lines), the reality is that they are still common in 2023.

#### Configuration deployment

The final step in configuration management is to change the state of the network infrastructure to match the intended one. This change may be a complete configuration deployment or a partial one, targeting only a specific part of the configuration. Both options are valid, and using one or the other will depend on how far along you are on the configuration management journey. In the early stages, you focus only on managing the state of network features that are especially relevant for you (e.g., managing the BGP state on a neighbor when the circuit is expected to enter a maintenance period). Later, you can increase the coverage while your automation experience evolves.

In the scope of configuration deployment, configuration *remediation* changes the network state starting from the current state, and calculates the changes to move to the desired state. You need to provide the configuration elements in a particular order to achieve the final state using an *imperative* mode; in contrast, the *declarative* approach defines the target state independent of the current one.

In both cases, implicit in changing the configuration is being ready to return to a stable state when things go wrong. This is known as configuration *rollback*. In [Chapter 10](ch10.html#apis), we mentioned the native support in NETCONF, but in general, you will need to create a plan to return the configuration to a previous state when needed. Features like *commit-confirm*, which requires validating a change after deploying it, are a first safeguard to avoid losing access permanently to a device because of a configuration change.

You have many options to implement configuration deployment, depending on the type of network infrastructure being automated:

- Custom applications using multiplatform libraries (e.g., Netmiko, NAPALM, ncclient, Scrapli, gNMIc), specific vendor SDKs (e.g., Cisco Meraki SDK, Juniper Networks Junos PyEZ, AWS Boto3), or directly via APIs calls
- Multipurpose open source tooling (e.g., Terraform, Ansible)
- Vendor platforms (e.g., Cisco Crosswork Network Services Orchestrator, or NSO, and Juniper Apstra)

Unattended network changes may sound scary for some operation teams, especially for those with little understanding of what’s going on behind the scenes of automation. We recommend first testing the changes in dry-run mode to increase awareness, and then start with a lab environment or less critical infrastructure before eventually targeting critical ones.

You should never underestimate the risks of automated configuration deployment and should add the protection mechanism that makes you feel in control. Pre-deployment tests, change review processes and approvals, or deploying changes via one of the deployment strategies covered in [Chapter 13](ch13.html#cicd) are all recommended to help manage this risk. It’s a common practice to connect configuration deployment with the observability component of the automation architecture for a post-validation of the network infrastructure state after the configuration changes have been deployed. This validation can be composed of multiple checks to validate that the operational state after the change matches the expectations defined in the SoT. Sometimes validation simply entails checking that the state hasn’t changed since the configuration change. Test frameworks like [PyATS](https://oreil.ly/3n4iI) or the [Robot Framework](https://robotframework.org) can help implement this validation.

Another common use case in this area is *zero touch provisioning* (*ZTP*). Here, a network device is automatically configured from scratch when it is connected to the network. You still need to render the intended configuration, but the difference is that you need a discovery mechanism in the device (e.g., DHCP) to find out where to pull the configuration from, self-identifying via its MAC address or serial number.

### Operations

Still, in the automation engine scope, there are network operations that are not related to configuration management. These operations have been exposed, traditionally, via a CLI, but as introduced in [Chapter 10](ch10.html#apis), the new programmatic interfaces offer access to RPC operations (e.g., gNOI or NETCONF).

Some common operations in networking are system reboot, ping and traceroute, file transfer, NOS activation, and certificate management. Using only these operations, without configuration management, you can implement several network automation solutions. As an example, a NOS upgrade solution could encompass the following tasks:

1. Pre-validate that the device has enough space to store the NOS files.
2. Make a local copy of the configuration for rollback.
3. Transfer the new NOS files.
4. Activate the new NOS and reboot.
5. Post-validate the device status with a ping and a traceroute.

Next, we focus on the antagonist of the automation engine, the one focused on retrieving the operational state, not changing it.

## Telemetry and Observability

In networking, we have been doing network monitoring (or network performance management) since the beginning (SNMPv1 was standardized in 1990). The need for more insight into the state of network services has motivated a continuous evolution that brings us to the present moment. Nowadays, the DevOps approach, where development and operations work side by side, requires better understanding of networking performance within the whole context of IT services.

Thus, the *telemetry and observability* component, within the network automation architecture, goes further than the previous network monitoring scope. Knowing *what* is wrong is not enough; this component has to point out *why* it is wrong (so it can be mitigated) and how it connects to the business impacting the user experience. In other words, telemetry and observability have to provide *network assurance* or verification that the network state matches the intended one (coming from the SoT) and correlate that with how it impacts any applications running on top. If drift occurs, this component can trigger a closed-loop automation process (via orchestration) to remediate the drift, or at least support troubleshooting efforts.

###### Note

Most of the concepts in this section are not networking specific but apply to all types of IT services.

The key characteristics of these solutions are as follows:

- Convergence of multiple data sources, with optimized and higher-performing retrieval
- Flexible data manipulation and enrichment
- API-driven data consumption with powerful query languages
- Scale-out capacity and easy service composability

With these features, you will get better capacity planning and anomaly detection or advanced alerting decisions to trigger other automation workflows (implementing closed-loop solutions). Also, because of the extensibility of the stack, it is possible to connect new solutions, such as analytic ones (based on artificial intelligence), to enhance the capabilities.

However, all these benefits come with the challenges of more complex architecture and orchestration. To better tackle these challenges, we propose a stack reference, covered in [“Telemetry and observability stack”](#telemetry-stack), to help you understand the role of each component and its design.

But before getting into the stack, it’s worth doing a quick recap of the type of data we would collect and its source.

### Operational state data

Automation is about data. As presented in the [“Source of Truth”](#source-of-truth), you need to use structured data to express the intent of your network design. Here, data is king again, because it’s going to *tell* you about what is going on in the network and the surrounding automation solutions (don’t forget that automation becomes an indistinguishable part of your network).

In this section, we provide a high-level description of the various data use cases that a telemetry and observability solution could take into account. And the data will come from multiple sources and formats. However, as you may guess, the same data quality principles (introduced in [“Data quality”](#data-quality)) are still valid here. Therefore, the data will be transformed and normalized to make it comparable.

Next, we describe several data types you should consider in scope. Don’t feel pressured to use all of them on day one; choose wisely where to start and evolve from there. We start with the common ones in IT: metrics, logs, and traces. Then we also look at network-specific ones: flows and packet traces.

###### Note

In [Chapter 4, The Three Pillars of Observability](https://oreil.ly/dso_ch4), from *Distributed Systems Observability* by Cindy Sridharan (O’Reilly), you will find a more detailed description of metrics, logs, and traces.

#### Metrics

*Metrics* are the simplest type of data, only a number. However, metrics are really useful to represent network state—for instance, the amount of received/sent octets in an interface, the observed latency on an ICMP echo/reply, or the state of a BGP session (where each state maps to an integer). This information is the raw data used to create other metrics by mathematically processing it. From the difference, in a period of time, of received octets, you can obtain the incoming bits per second rate.

> Metrics are a numeric representation of data measured over intervals of time.
> 
> *Distributed Systems Observability*, Cindy Sridharan

Everything about the network state can be expressed as metrics. In networking, most of these metrics are well-defined using SNMP MIBs or YANG models, but you can define any metric you consider relevant for your use case, including the applications running on top of the network. For example, you can define a metric that tracks how many automated firewall rules have been created to track the activity in an automated firewall rule process.

One historical limitation of metrics for monitoring has been the lack of *context* around a *sample* (a metric value at a concrete moment). Modern metric storage systems allow enriching metrics with extra metadata along with the sample. [Figure 14-7](#prometheus-metric) shows the four parts of a metric in the Prometheus metric format (you’ll learn more about Prometheus and other TSDBs in [“Storage”](#telemetry-storage)). Notice how the contextual information can enrich the metrics with data you consider relevant (usually taken from the SoT).

![npa2 1407](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1407.png)

###### Figure 14-7. Prometheus metric format

In [Example 14-6](#prometheus-example), three samples from Prometheus indicate the attributes illustrated in [Figure 14-7](#prometheus-metric).

##### Example 14-6. Prometheus metric

```
bgp_sessions_prefixes_sent{collection_method="execd",device="ceos-01",         
device_platform="arista",device_role="router",host="telegraf-01",local_as="65111",
neighbor_address="10.1.7.2",net_os="eos",peer_as="65222",peer_type="external",
region="lab",router_id="10.17.17.1",session_state="active",site="lab-site-01"} 

0 @1671966244.39                                                             
3 @1671966247.39
2 @1671966250.39
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`bgp_sessions_prefixes_sent` is the name of the metric.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The key-value pairs are the labels or metadata associated with the metric. We could later consume the metric using it.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`0`, `3`, and `2` are the values of the metric at three specific times.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`1671966244.39`, `1671966247.39`, and `1671966250.39` are the metric sampling times as timestamps.

###### Tip

In heterogeneous network environments, you would get data from different sources but with the same meaning. Being able to transform all to the same format would ease later comparison and consumption.

#### Logs

*Logs* are produced by the network infrastructure and network automation applications to notify of any activity that deserves attention. Syslog is the de facto logging protocol, available in almost every network device.

> An event log is an immutable, timestamped record of discrete events that happened over time.
> 
> *Distributed Systems Observability*, Cindy Sridharan

The syslog message contains five main components: the message (the content), the facility (type of the system originating the message), the priority (severity of the message), the source IP, and the timestamp. However, this information comes unstructured in free-form text that varies from vendor to vendor. To make use of the data programmatically, it must be parsed and converted into structured data.

Almost every log collector provides parsers that help define the rules to *interpret* the syslog message. For example, the [Logstash log collector](https://oreil.ly/yPDFT) has the grok filter to define the parsing logic in the templates to extract the data fields.

In [Example 14-7](#parsed-logs), a log message is transformed into a structured object.

##### Example 14-7. Log parsing

Raw log message:

```
Sep 20 08:01:13: <10.0.0.10> %LINEPROTO-5-UPDOWN: Line protocol on Interface
GigabitEthernet0/5, changed state to up
```

Structured data output:

```
{
  "source_ip": "10.0.0.10",
  "severity": "5",
  "facility": "LINEPROTO",
  "facility_process": "UPDOWN",
  "message": "Line protocol on Interface GigabitEthernet0/5, changed state to up",
} 1663660873000
```

###### Tip

Log patterns are likely available to match the messages you are interested in. Furthermore, the [napalm-logs library](https://oreil.ly/3uM0Q) comes with predefined parsers for some popular [platforms](https://oreil.ly/zM3DX), providing a structured output following the OpenConfig or IETF YANG models.

Structured logs are an example of *high-dimensional structured data*. By definition, this type of observed data contains multiple features. For instance, the log entry from [Example 14-7](#parsed-logs) has a timestamp, a facility, an IP, etc., versus being a raw string (as it was originally before structuring it). The network automation realm has other high-dimensional structured data: traces, flows, and packet captures.

###### Warning

Having more data dimensions offers many advanced options for analyzing it. However, this increment requires extra effort for its processing and/or analysis (sometimes exponential). This trade-off was named the *curse of dimensionality* by mathematician Richard E. Bellman.

#### Traces

Maybe they’re not commonly related to networking operations, but with software entering into the networking space as a control plane or automation, traces are becoming important for understanding how the network-related applications are behaving. *Traces* are used extensively in distributed applications to track process executions, such as a request traversing several services. This is especially relevant for microservice architectures, to understand the end-to-end processing, and capturing relevant data in multiple control points, like the time spent in each stage.

Newer than metrics and logs, traces have been the main factor in promoting a standardized format to ease integration between senders and receivers. In 2019, the OpenTelemetry project was created at the [CNCF](https://www.cncf.io). The project’s goal is to provide standardized vendor-agnostic SDKs, APIs, and tools for ingesting, transforming, and sending observability data. Its scope is not only traces but also metrics and logs. The solutions to analyze traces are commonly named application performance management (APM), and examples include [Cisco AppDynamics](https://www.appdynamics.com), [Elastic Observability](https://oreil.ly/WJ_SR), and [Honeycomb](https://www.honeycomb.io).

#### Flows

A specific high-dimensional structured data type for networking is the *flow* that describes communication between two IP addresses. Nowadays, several formats coexist. It started with NetFlow, developed by Cisco in the late 1990s. NetFlow v9 served as the basis for the standard version of Internet Protocol Flow Information Export (IPFIX). Another protocol in use is sFlow, developed by InMon Corp. and supported by the [sFlow consortium](https://sflow.org), which also offers packet data capturing (which has been added to IPFIX too).

With its own format specifics, a flow contains some common information: the source and destination IP address and TCP/UDP port, the packet/byte count, plus other information. This data is useful for capacity planning, flow-based billing, security monitoring, or application discovery, for example. The following is a simplified representation of a flow:

```
| Timestamp  | Src IP    | Src Port | Dst IP    | Dst Port | Intf  | Prot | Bytes |
| 1671966244 | 192.0.2.1 | 32541    | 192.0.2.2 | 443      | Gi0/0 | TCP  | 1234  |
```

###### Warning

Keep in mind the extra cost of flow export because it’s a computational task. Capturing flows in all your network ports or using aggressive sampling could impact your network devices.

#### Packet capture

Yet another source of operational network data is *packet captures*. Networks move packets, so these packets provide the most detailed information about their behavior. Like flows, packet captures also require a lot of resources, especially on memory (depending on how much information from a packet is persisted).

You are likely aware of popular tools like Linux [tcpdump](https://www.tcpdump.org) and [Wireshark](https://www.wireshark.org), using the libpcap/Npcap libraries to capture network data. The following example shows the two packets (only summary data) for a ping conversation (ICMP request and reply):

```
18:48:46.439907 IP 192.2.0.2 > 192.2.0.1: ICMP echo request, id 31, seq 0, length 64
18:48:46.455567 IP 192.2.0.1 > 192.2.0.2: ICMP echo reply, id 31, seq 0, length 64
```

###### Tip

You could argue that the preceding example is not structured data, and you would be right. To get structured data, you need to interact with the libraries or parse the output as we did for the logs.

These data sources offer different information that can be relevant for different purposes. Choosing which data sources are needed, and how those have to be aggregated to correlate information, is part of your architectural decisions.

### Options to collect network operational data

The next question to solve is, how to obtain the data? In addition to the mechanisms we already mentioned (syslog for logs or NetFlow for flows), in this part, we discuss other common ways to collect operational state from the network.

#### SNMP

SNMP has been the king of network monitoring for years. It works well for device monitoring and has been widely adopted by all vendors, which makes it a reliable way to retrieve data. It exposes the data structured in MIBs and implements a *pull* approach: the client *asks* for data every time it needs it. However, SNMP comes with limited support for *push* notifications (called *traps*).

MIB structure adds complexity that requires correlation to obtain relevant information. For example, to create the metric `interface_out_octets{interface="GigabitEthernet0/1"} 1234` (again, using Prometheus syntax), you need to combine two pieces of data because the index, `3`, doesn’t provide enough context:

```
interfaces.ifTable.ifEntry.ifOutOctets.3 = Counter32: 1234
  corresponds to
interfaces.ifTable.ifEntry.ifDescr.3 = GigabitEthernet0/1
```

#### Syslog and flow exporters

Even though syslog and flow protocols deal with different data, both share similar patterns. They run directly on a process in the network device, and they send the data via UDP to a target (the collector). In both cases, the information is sent without a guarantee of reception.

Each one has its own basic configuration options. For syslog, you select the *facilities* (processes) and the *severity* level of the messages. And, for flow exporters, the key configuration is the interfaces under observation and the packet sampling (the percentage of actual packets exported).

#### CLI

The other traditional way to get network state is the CLI. Network engineers have used it for troubleshooting, and sometimes it provides information that is not available via other interfaces. However, CLI data comes unstructured and must be retrieved as text and parsed. In this example, you can observe how much relevant BGP information can be obtained from the CLI output, but it would require parsing it to extract the data and allow its consumption:

```
Router# show ip bgp 192.0.2.3 255.255.255.255

BGP routing table entry for 192.0.2.3/32, version 35
Paths: (2 available, best #2, table default)
Multipath: eBGP
Flag: 0x860
  Advertised to update-groups:
     1
  200
    203.0.113.166 from 203.0.113.166 (192.168.0.102)
      Origin incomplete, localpref 100, valid, external, backup/repair
      Only allowed to recurse through connected route
  200
    203.0.113.165 from 203.0.113.165 (192.168.0.102)
      Origin incomplete, localpref 100, weight 100, valid, external, best
      Only allowed to recurse through connected route
```

###### Note

As we’ve mentioned several times throughout this book, retrieving data by scraping text from a CLI is error prone, slow, and requires fragile and difficult-to-maintain parsing logic. It should be avoided if at all possible. That said, sometimes scraping is the only option, and even with all these caveats, it can still be integrated with a telemetry and observability solution.

#### Model-driven telemetry

As introduced in [Chapter 10](ch10.html#apis), model-driven management protocols (NETCONF, RESTCONF, and gNMI) offer an alternative for configuration management and operational state retrieval, overcoming the limitations of existing interfaces (SNMP and CLI). Regarding the state retrieval, they come with a meaningful data structure (using YANG models) and a *streaming telemetry* to improve the time to detect a change. You can review the model-driven telemetry features in [Chapter 10](ch10.html#apis), but as a reminder, this is the output of a telemetry subscription on the interface counters of a specific interface:

```
{
  "source": "eos-spine1:6030",
  "subscription-name": "default-1664428777",
  "timestamp": 1664428775338387214,
  "time": "2022-09-29T05:19:35.338387214Z",
  "prefix": "interfaces/interface[name=Management0]/state/counters",
  "updates": [
    {
      "Path": "out-octets",
      "values": {
        "out-octets": 723727
      }
    },
    {
      "Path": "out-unicast-pkts",
      "values": {
        "out-unicast-pkts": 4500
      }
    }
  ]
}
```

#### REST API

As introduced in [Chapter 1](ch01.html#trends), network infrastructure is served as a service behind cloud- or controller-based platforms. These services are usually managed via REST APIs. Each has its own data model that covers the features offered by the service, in a simplified fashion compared with the level of control over NOSs.

As an example, documentation of the VPN service offered by AWS offers the following information via its REST API, mixing configuration and operational state (under the `VgwTelemetry` key):

```
{
    "VpnConnections": [
        {
            "CustomerGatewayId": "cgw-01234567abcde1234",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-1122334455aabbccd",
            "TransitGatewayId": "tgw-00112233445566aab",
            "Options": {
                "StaticRoutesOnly": true,
                "LocalIpv4NetworkCidr": "0.0.0.0/0",
                "RemoteIpv4NetworkCidr": "0.0.0.0/0",
                "TunnelInsideIpVersion": "ipv4"
            },
            "VgwTelemetry": [
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2023-07-29T10:35:11.000Z",
                    "OutsideIpAddress": "203.0.113.3",
                    "Status": "DOWN",
                    "StatusMessage": ""
                }
            ]
            // some information omitted for brevity
        }
    ]
}
```

#### Network protocols

Another option to get network operational data is to participate in distributed routing protocols. For instance, running a process that speaks OSPF or BGP would give access to the inner information exchanged by these protocols. Extensions can provide more information, including the BGP Monitoring Protocol (BMP) to monitor BGP updates from the sender’s point of view.

[Several open source projects](https://oreil.ly/qGFxn) allow interacting with network protocols or simply receiving and replying with crafted messages, such as [ExaBGP](https://oreil.ly/YYG7E). To illustrate, using ExaBGP (from its documentation), you can obtain structured BGP data:

```
{
    "exabgp": "4.0.1",
    "time": 1560371099.404008,
    "host" : "2.113.0.203.in-addr.arpa",
    "pid" : 37750,
    "ppid" : 10834,
    "counter": 1,
    "type": "update",
    "neighbor": {
        "address": { "local": "127.0.0.1", "peer": "127.0.0.1" },
        "asn": { "local": 1, "peer": 1 } ,
        "direction": "in",
        "message": {
            "update": {
                "attribute": { "origin": "igp", "med": 200, "local-preference": 100 },
                "announce": {
                    "ipv4 unicast": {
                        "198.51.100.1": [
                            { "nlri": "192.0.2.0/32", "path-information": "0.0.0.0" }
                        ]
                    }
                }
            }
        }
    }
}
```

#### Synthetic monitoring

All the previous information is about observing the operational state without any *direct* interaction. It does not take into account the user’s perspective. Synthetic monitoring tries to emulate the user’s experience to understand how the network is behaving, from this specific point of view.

The overall idea is simple. Inject data in one point of the network and compare it with the data outputting at the other end. The outcome may be a success (with information about the delay) or a partial/total loss of information.

Here, the key point is to reproduce as well as possible the communication pattern you want to observe. It can be as simple as doing ICMP or TCP/UDP tests from your network gear (e.g., IP SLA in Cisco or Juniper probes) to distributed solutions running agents that work coordinately to reproduce the interesting traffic under observation (e.g., DNS, SSL, gRPC).

###### Tip

The internet ecosystem has an interesting initiative, [RIPE Atlas](https://atlas.ripe.net), that gives you community insights about internet connectivity and allows performing customized measurements to simulate the end user’s experience.

After this general overview of the various types of data under the scope of the telemetry and observability solution, it’s time to present the building blocks of a modern stack implementation.

### Telemetry and observability stack

The takeaway from the previous section should be that retrieving data is not a simple task. You have many options to collect data, so network monitoring solutions should be flexible enough to integrate multiple systems to store and consume that data. However, traditional monitoring systems took the form of a monolith, integrating all the features into one tool.

This makes getting started easier but constrains the system’s evolution and adaptability. The best option would be to have orchestration solutions to ease the integration and configuration of the components. Lucky for us, this is an ongoing trend in the whole IT community, and many options are available nowadays.

###### Note

You can build capable monolithic solutions, but you will be constrained to choose the best tool for a purpose or to scale only parts of the stack.

To be able to choose the right tool, you need a clear understanding of the components of a modern telemetry and observability solution for network monitoring. [Figure 14-8](#telemetry-stack-figure) depicts the main components of a modern monitoring stack.

![npa2 1408](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1408.png)

###### Figure 14-8. Telemetry and observability stack

As an overview, these are the seven functions of the stack:

CollectorGathers the data, any type of data required

Data distribution and processingHelps move collected data around to allow scaling complex scenarios

StoragePersists the data, and offers a consumption interface

VisualizationRenders the data in the form of graphs or reports to be interpreted

AlertingRaises alerts to trigger actions when data matches expectations

SoT enrichmentAdds extra metadata to the data, allowing more attributes to query data

OrchestrationManages how all the telemetry stack components are configured and operated sustainably

Through this section, we will go step by step, explaining the relevant challenges that must be addressed and how to approach them. But before getting into each one, you should consider some general questions as a clear guide on making decisions:

- What is the data to be collected? (see [“Operational state data”](#data-use-cases-telemetry))
- How much data is expected?
- What is the extensibility and scalability of the designed system?
- Who will consume the data (and how)? (Capacity Planning team? NOC?)
- What is the required level of automation to orchestrate the stack? How will the organization deploy new applications?
- How will the system’s load be distributed? (Regional pods?)

Some well-known stacks have tools that usually work together. [Table 14-1](#table-telemetry-stacks) lists some of the most adopted. It is just a simplified example; all of them could incorporate other tools to extend their functionalities.

| Function | TPG[a](ch14.html#id1995) | TIG[b](ch14.html#id1996) | ELK[c](ch14.html#id1997) |
| --- | --- | --- | --- |
| Visualization | [Grafana](https://oreil.ly/dDJUd) | Grafana | [Kibana](https://oreil.ly/V84Me) |
| Storage | [Prometheus](https://oreil.ly/KcED3) | [InfluxDB](https://oreil.ly/cW4hB) | [Elasticsearch](https://oreil.ly/Hr1t-) |
| Collector | [Telegraf](https://oreil.ly/0uRn_) | Telegraf | [Logstash](https://oreil.ly/9T77s) |
| [a](ch14.html#id1995-marker) Telegraf/Prometheus/Grafana[b](ch14.html#id1996-marker) Telegraf/InfluxDB/Grafana[c](ch14.html#id1997-marker) Elasticsearch/Logstash/Kibana |  |  |  |

###### Note

In this book, we do not cover how to set up a telemetry stack in detail. A good reference is *Open Source Network Management* by Josh VanDeraa (Leanpub), which covers the TPG option.

While some tools implement all the components to offer complete solutions, no tool is likely to cover 100% of your needs. Thus, being able to integrate with other tools is key. Composability in all the layers of the stack allows you to extend the features as needed without the constraints of a monolithic solution. As an example, a specialized open source tool for network state observability is [Suzieq](https://oreil.ly/lkxF2), which offers the capacity to collect network data (e.g., LLDP, routing table, ARP/ND table, BGP), and analyze it to verify the state of the network’s protocols. Suzieq exposes a GUI and a CLI, but also a REST API or Python objects to interact with and integrate with other components of your observability stack.

Now it’s time to dig into the components depicted in [Figure 14-8](#telemetry-stack-figure), starting with the first one in the process, the collector.

### Collector

Everything starts with the *collector*, as it retrieves the observed data, either from the network infrastructure or from other sources (e.g., synthetic monitoring). But first you must determine which data you are interested in and how you can get it. In [“Operational state data”](#data-use-cases-telemetry) and [“Options to collect network operational data”](#data-sources), you have the most relevant options, respectively. This decision comes from the needs of the network automation solution—which data is required to validate the outcome of the workflow? Naturally, as more workflows are incorporated into the solution, these needs will evolve, and you’ll need to consider more and more options.

###### Tip

Processing and storing observability data come with a cost. We recommend adding data only as needed to keep focus and save resources (and money)!

You will always be able to extend the types of collected data later, but focusing initially on a certain type helps to get started. Later you will extend the coverage to other data types, supported by the network infrastructure, that are relevant to you. Once you determine the data type (e.g., metrics), you need to choose the proper interface to collect it (e.g., SNMP, NETCONF, gNMI, REST API, or CLI).

###### Note

Determining how to retrieve the data may vary among network infrastructure providers. Some legacy devices may support only SNMP and CLI, while more modern ones offer newer options like gNMI. In either case, take care to avoid duplicating your data sources.

Traditionally, in networking, collectors have been deployed *externally* to the network device, because running user applications on the NOS wasn’t possible. This has changed since vendors started opening their NOSs to allow running user processes (such as collectors), as happens on any server. External deployment is still the only option for cloud- or controller-based services. Both options work, so use the one that better suits your environment.

Once the collector retrieves the data, the first task is to *structure* it (if it’s not already). For instance, whether it’s a raw log message or a CLI output, the collector should parse it and give every part of the data some meaning (according to a template strategy).

The next step is data *normalization*, to make it comparable among sources (and formats). In [Figure 14-9](#normalization-enrichment), the same metric data coming from SNMP or gNMI is homogenized into a compatible format, using the same metric name. In the example, the data from SNMP (`interface_ifHCInOctets`) and the data from gNMI (`in_octets`) is renamed to `interface_in_octets`.

![npa2 1409](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1409.png)

###### Figure 14-9. Normalization and enrichment

You have many options for collectors available today; note that they’re also sometimes known as *agents*. Some specialize in different data types and have multiple output options available (where data is sent after being collected). One of the key factors in choosing a collector is its extensibility to adapt to different collector methods.

Here is a summary (not exhaustive at all) of some popular open source projects:

Metrics[Telegraf](https://oreil.ly/DWqAn)

Logs[Logstash](https://oreil.ly/MOZ4H)

[Fluentd](https://oreil.ly/gWyBJ)

[Promtail](https://oreil.ly/fnhnn)

Flows[pmacct](https://oreil.ly/PvNcy)

[GoFlow](https://oreil.ly/uwspn)

[GoFlow2](https://oreil.ly/aUn7Q)

[Pktvisor](https://oreil.ly/WXqVZ)

Packet capture[libpcap](https://oreil.ly/Rt_Cs)

[pktvisor](https://oreil.ly/eyyub)

Traces[Jaeger](https://oreil.ly/Z3uuG)

[Zipkin](https://oreil.ly/dNXkT)

The collector may also have the responsibility of *enriching* the data. This is an important step, as it allows adding more context to the data, which will be useful later when visualizing or querying it.

### SoT enrichment

We can’t forget that, within a network automation architecture, a lot of potential exists to add contextual data from the SoT to the collected data, to add more dimensionalities for later consumption.

In [Figure 14-9](#normalization-enrichment), you can see how metrics can be enriched with extra labels—for example, adding the role and site of the device or the provider of the circuit. This metadata can be used later when grouping or filtering the data by these labels. We might, for instance, visualize all the packet loss statistics for the interfaces belonging to a specific network service provider.

This enrichment or processing can happen in the same place where the data is collected or in a specific process for this purpose. This disaggregation leads us to the next stage: data distribution.

### Data distribution and processing

Even though, for most use cases, the collector agent can collapse most functions before sending the data to the storage layer, some complex use cases require an extra layer. This is the case for highly distributed environments with high scalability needs.

In those cases, between the collector and the storage is a distribution layer. Its key aspect is the scalability to support high-throughput rates without stressing any component of the stack. These solutions are called *message queues* or *message brokers*, and implement a publish-subscribe paradigm. These transport mechanisms provide advanced features such as predefined schema validation for safer data consumption.

###### Note

Message queues are used for many machine-to-machine use cases, where scalability and asynchronous communications are required.

Several open source projects exist in this area: [Apache Kafka](https://oreil.ly/HFXfd), [RabbitMQ](https://oreil.ly/8dloG), [EMQX](https://oreil.ly/EueiM), and [Eclipse Mosquitto](https://oreil.ly/lq1JB). The last ones implement the MQTT (an ISO standard), which is a lightweight format especially suited for telemetry and Internet of Things (IoT) use cases.

### Storage

In [“Databases”](#sot-databases), we presented some databases for storing the network intent. Here, in the context of operational data, a new attribute gains extra relevance: *time*. In the SoT, the network intent is something more or less stable; it is not changing every second. But, regarding the observed state, time is everything.

###### Note

In the SoT, being able to attach a time to intent is important too. You may want to define an intent in the future—for example, defining a maintenance window for next week.

In traditional network monitoring, it was common to store data in the Round Robin Database Tool, or [RRDtool](https://oss.oetiker.ch/rrdtool). It handles time-series data by using a circular buffer database that keeps the storage size constant over time. This tool is the backend of classic network monitoring projects including [Cacti](https://www.cacti.net) and Multi Router Traffic Grapher, or [MRTG](https://oreil.ly/VtB0K).

Modern telemetry uses new time-series databases (TSDBs) to overcome the limitations of the RRDtool. TSDBs have the following:

- High transaction volumes to support a high rate of data ingestion and persistence over time.
- A flexible data schema so the user can define how data is organized and how to scale data via sharding and replication.
- A powerful consumption language, accessible via the API. Every TSDB comes with its own language and features. [InfluxDB](https://oreil.ly/1BxVa) has InfluxQL, [Prometheus](https://oreil.ly/x-w4o) has PromQL, and [TimescaleDB](https://oreil.ly/4ZwOu) uses full SQL (based in PostgreSQL).

As an example, this is what a PromQL query looks like:

```
rate(interface_in_octets{device_role="backbone"}[2m])*8
```

The inner part of this function filters the metrics that belong to a specific `device_role` (actually, a label enriched from the SoT in the collector process). Then it creates a *rate* (in 2 minutes), and finally, the result is converted to bits multiplied by 8. You could use this same query in a dashboard, an alerting system, or a script.

###### Note

An important consideration when choosing the right TSDB is the type of data it can store. For example, Graphite and Prometheus support only numeric data, InfluxDB supports numeric data and strings, and TimescaleDB supports any type (supported by PostgreSQL).

TSDBs work really well for metrics, but not for high-dimensional data like logs or flows. In these cases, other databases suit better. Search engines are NoSQL databases dedicated to searching for data content. They allow searching for complex expressions or full text, and then grouping the results. They are also optimized for stemming (identifying words based on their grammatical stem) or for distributing searches to support high scalability. The most popular open source search engine is [Elasticsearch](https://oreil.ly/Snl2j), which offers a SQL-like query language accessible via a REST API.

Another challenge in the persistency layer is the high volume of data for long-term storage that requires scale-out and easy consumption capabilities. Some projects on top of the previous TSDBs provide these functionalities. As a reference, for Prometheus, you have [Grafana Mimir](https://oreil.ly/5h5B6) or [Thanos](https://oreil.ly/e8y5H).

###### Tip

Determining your storage requirements, such as the retention period, has a big impact on your decisions about tooling, and, eventually, on the cost of the solution.

### Visualization

In [“User Interactions”](#user-interactions), you learned about dashboards as a user-interaction solution offering visualization of the network’s operational state. Dashboards are the most common way to present observed data to end users. The data is queried from the storage layer and rendered as defined.

When selecting a visualization tool, you should consider three key aspects:

- Correlating multiple observability data sources in one tool
- Having the flexibility to customize dashboards
- Including data from the SoT to use as a reference

[Figure 14-10](#visualization-example) shows an example that brings this all together. This dashboard (from Grafana) comes with custom panels for different types of data (metrics and logs), and the data from the SoT adds contextual information. Combining enriched metrics and logs (vertical dotted lines) in the same panel allows you to make more educated guesses about why a metric changes the value (i.e., because of a BGP session change). Also, notice that the BGP state metric (originally a number) is translated to something easier to understand: Idle or Established.

![npa2 1410](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1410.png)

###### Figure 14-10. Network dashboard

The visualization tool should be flexible enough to create custom dashboards for several use cases. For instance, you might want to visualize the network topology with links colored based on the BGP state or to show the utilization of the links in a network topology.

Even though visualization is a key component of observability, it is not the only one. In the next section, you will see how to use the observed state to trigger actions.

### Alerting

The other *consumer* of the observed state is the alerting component. Its main goal is to raise awareness (an event) of any deviation from the normal. This event can then be used for multiple purposes, like sending a notification to the on-call engineer or triggering an orchestration action.

In alerting, the most important point is to define what is *normal*. This can be a reference value (a threshold), taken from the SoT (e.g., an SLA defining 0.5% of packet loss), or can be *deduced* from previous behavior. In this second case, this deduction can arise from simple math like comparing the 95th percentile to the actual data or advanced machine learning solutions that automatically deduce what is not normal.

###### Note

Artificial intelligence and machine learning (AI/ML) can provide educated *suggestions*, improving the criteria that decide when to alarm or not. AI/ML can dynamically process a huge amount of data to produce outcomes. For instance, as network engineers helping with capacity management, we may have reviewed traffic graphs to identify when an interface may hit its limit in the future. With AI/ML, you could get similar conclusions, but scaling the process to hundreds of thousands of interfaces. AI/ML is still incipient in networking, but its potential impact on network planning, design, and operations (aka AIOps) is huge as it can help with automating any type of decision (or help with suggestions).

AI/ML is a huge topic that we can’t cover in this book, so we refer you to *Machine Learning for Network and Cloud Engineers* by Javier Antich (self-published) to better understand how these solutions are defined and *trained* to help in automating decisions.

[Figure 14-11](#alerting-engine) depicts alerting system behavior. The alert engine is the heart of the system and takes three inputs: user-defined alert rules including the reference values coming from the SoT (e.g., the circuit SLA to understand whether a 1% packet loss is acceptable), silencing rules (to avoid unnecessary events), and the operational state data. The alert engine is also in charge of avoiding duplicating alerts by grouping them. Finally, it sends the alerts to various integrations, including instant messaging systems; email; incident management tools such as [Opsgenie](https://oreil.ly/rMgcQ), [Alerta](https://alerta.io), or [PagerDuty](https://www.pagerduty.com); or orchestration endpoints ready to trigger automatic mitigation.

![npa2 1411](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1411.png)

###### Figure 14-11. Alerting engine

###### Note

To learn more about alerting, see *Site Reliability Engineering* by Betsy Beyer et al. (O’Reilly). [Chapter 6 covers monitoring distributed systems](https://oreil.ly/oJnOZ).

Determining when an alert should be triggered is not trivial. It should come at the right time (expired events are useless to act on) and be relevant to avoid false-positive and nonactionable alerts. Nonactionable alerts (following an “alert on all the things” behavior) will inevitably be ignored because of oversaturation and on-call exhaustion.

The criteria used to trigger alerts, and their severity, should be based on the impact on the service and the capacity to act. One common rule for anomaly detection is to use *standard deviation* as a reference to see whether values are deviating from the *normal* ones. Imagine that an interface usually running at 10% of utilization jumps to 40%; this 4× increment could raise an alert, not for the value but for the increment.

###### Tip

Don’t forget to *watch the watcher*. Applying the concept of the *deadman switch*, the alerting system should alert when an expected metric isn’t available. There are different ways to mitigate this alerting gap. You could pre-initialize all your metrics, ensuring that all your applications initialize them on start (with the consequent increase of storage cost). Alternatively, you could use the SoT as a reference, so if you *know* that there is an active switch in the inventory, but no related metrics, you’ll know something is wrong with the state of the device.

Finally, to complete the architecture walk-through, it’s time to focus on how we can connect the dots between its components.

## Orchestration

Each component in the architecture has a purpose in the overall strategy. But, like a symphonic orchestra, a *director* is required for coordination. This analogy represents the role of *orchestration* in a network automation solution. Of course, for simple solutions, you may decide to omit orchestration, but when several steps are involved, its role is principal. Naturally, orchestration can be overarching or focused on certain processes.

As we noted before, network automation translates manual network operation workflows into automated ones; most of the repetitive work is performed by computers instead of humans. The orchestration solution should allow concatenating these tasks according to the desired flow, gluing all the tasks together.

As you can read between the lines, this is a precious skill for any network engineer evolving into a network automation engineer. You have to learn how to identify the current operational workflows to convert them into automated ones. Often this is not an easy task, because of the lack of procedures or the number of steps and interactions required.

Our recommendation is to apply a top-down iterative process. You start with understanding the global workflow, and iteratively break it into more detailed steps:

1. Identify how the step is kicked off and by whom.
2. Understanding this step as a black box, determine the required input and output data (i.e., external interactions, APIs, or humans). At this point, evaluate whether this step is necessary, so it could be omitted or consolidated in other tasks.
3. Normalize the data into structured data; minimize the required fields, and define the corresponding data validation schema to validate it before and after the workflow stage.
4. Determine whether it makes sense to break this step into smaller ones that require repeating the process.

###### Tip

Approach this discovery process with an open mindset, ready to look for unknown data. Even if you are already familiar with the workflow, you may find surprises.

In the early stages of network automation adoption, workflow management may be seen as not so important. However, as you try to solve more complex operations, the orchestration becomes necessary, and workflow engines become your allies.

Workflow automation is a very open space where multiple products may do the job. Any solution that allows an *if this, then that* logic can implement some workflow orchestration. So, in its essence, a simple script with an `if/else` statement could handle the job. Indeed, the *gitops* approach, which checks changes in Git to trigger other tasks, uses this approach. However, some tools provide several features to facilitate implementing complex workflows. We could split this overall group into two main subgroups:

- Automation pipelines, such as [Jenkins](https://oreil.ly/bT8Ej), [GitHub Actions](https://oreil.ly/E7cKT), and [GitLab CI/CD](https://oreil.ly/G8Z1V).
- Workflow engines, including [AWX](https://oreil.ly/0BN1-), [Rundeck](https://oreil.ly/V_i9w), [Prefect](https://oreil.ly/6YSEr), and [StackStorm](https://oreil.ly/KmtkO).

Having so many options, these are our recommended factors when evaluating these solutions (in addition to common software topics like scalability):

- How can a workflow be defined? Which language is used to define the workflow?
- How does a user interact with it (e.g., CLI or UI)? Is it customizable?
- How many integrations are available? Is it easier to extend them with new ones?
- How are events received or created? Maybe using webhooks, publish/subscribe mechanisms, or scheduler triggers?

Closely connected to orchestration, there is a subtopic worth mentioning: *event-driven automation*. We cover it in the next section.

### Event-driven automation

The *event-driven* approach is a popular topic in network automation. The idea behind it is to establish a closed-loop solution that receives events and determines the appropriate response. These events can come from external integrations or any other of the architecture components—for instance, a webhook triggered from the SoT when an object is modified or an alert raised by the telemetry and observability stack. In both cases, the event-driven solution should have a related action to apply (or default to a fallback one).

The core of any event-driven solution is the *mapping* between the events and the follow-up actions without involving manual human intervention. This approach speeds up response to any event coming from the network and its mitigation or, at least, the gathering of information to help with troubleshooting. Some open source projects used for event-driven network automation use cases are [StackStorm](https://oreil.ly/HJovy), [Salt](https://oreil.ly/nmocP), and [Ansible](https://oreil.ly/8dOxW).

###### Note

StackStorm and Salt are not explicitly covered in this edition of the book, but we have made the content from previous versions available at [*https://oreilly-npa-book.github.io*](https://oreilly-npa-book.github.io).

[Figure 14-12](#event-driven) describes a potential workflow for event-driven automation on top of the proposed architecture.

![npa2 1412](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1412.png)

###### Figure 14-12. Event-driven automation

Here are the six steps of the workflow:

1. The network operational state changes.
2. After evaluating the new status versus the intended status (from the SoT), a new event is generated.
3. The event is received by the orchestration system, which triggers a new workflow execution.
4. Notifications are sent to inform users of the ongoing event.
5. The task to remediate the state is triggered in the automation engine that uses the intended state to determine the appropriate action.
6. The network infrastructure returns to the expected operational state, so no more events will follow.

To illustrate the practical benefits of event-driven network automation, suppose the current network OS has a known bug: a specific syslog message indicates an unrecoverable error, requiring a module to be rebooted. Upgrading the affected modules might require several weeks, and a solution is needed in the interim. Traditionally, this might be handled by paging an on-call network engineer in the middle of the night, who then logs into the network devices and manually reboots the module. With a workflow engine in place, you can write a rule to watch for a specific syslog message and, upon receipt, automatically schedule the run of a Python function or an Ansible playbook to reboot the module at a specific, less consequential time.

This section completes the walk-through of the architecture’s components. Now that you’ve gained a good understanding of them, it’s time to see how everything comes together with an example.

# Understanding the Architecture with an Example

The goal of this example is to provide you with a mental reference to better comprehend how to approach building a network automation solution with the proposed architecture. Take it as a high-level overview of the process you would apply, in much more detail, when you face building your own solutions.

For this example, we have chosen a common network operational task: firewall rule management. [Figure 14-13](#arch-example-1) illustrates an (extremely) simplified hybrid network setup, with on-premises and cloud network infrastructure. Our goal is to design an automated solution to provision the necessary firewall rules between two *applications*.

![npa2 1413](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1413.png)

###### Figure 14-13. Firewall rule automation example

This scenario doesn’t provide relevant details such as *what* will be the user’s interface, *which* data will the user provide, or even *how* an application is defined. Sometimes you get part of this information, but more often you will obtain the responses throughout the design process. This vague context leads us to the first step in the process: *understanding* what the process/workflow looks like or should look like.

## Determine the Operation’s Workflow

To automate something, you must first understand it. Thus, you should gather information about the process in place today, to establish the minimum expected outcome of the automated version. This information may be in the form of documentation (e.g., diagrams or checklists) or tribal knowledge. Nevertheless, even unknown unknowns can be discovered through low-level detailed conversations.

As recommended in [“Orchestration”](#orchestration), you could use a structured approach to understand the process from various perspectives and roles (e.g., network engineers and network users), and from multiple individuals in the same role (as each engineer may do things slightly differently). For instance, in the example, it would be especially relevant to understand the requirements of the security team that defines the security policy, but also the steps followed by the engineer to decide how to implement the security policy.

###### Tip

Humans are creative by nature. Therefore, following checklists for common operations could incorporate some deviations. Take this into account in your analysis!

At this point, automation is not the main concern. You should focus on capturing, step by step, what happens in the current workflow. In our firewall automation example, steps could look like this:

1. An application owner notifies the network team about the source and destination IPs and ports.
2. A network operator checks whether the policy matches the security policy rules.
3. If so, they run some traceroutes to determine which devices must be updated.
4. The network engineer prepares the required configuration updates (using a diagram and previous examples of configuration snippets), and a change window to apply them is defined.
5. On the time window, a network engineer connects to the devices, one after the other, updating the configuration as planned.
6. Once the configurations are updated, the network engineer sends a notification to the requester with information about the change.

A lot of details and alternative flows have been omitted, but you can grasp what the current workflow looks like. This is the starting point, the minimum requirements the automation should address. Documenting this process is key to later understanding whether something is missing or is not accurate enough.

With this reference in place, you have to translate it into a workflow that utilizes the benefits of automation.

## Translate the Workflow Steps to Automated Tasks

The first step in transforming a manual workflow into an automated one is to simplify user interactions and remove manual interactions. The first improves the UX and decreases the data validation effort, and the second speeds up processes and increases reliability.

Starting from the previous workflow definition, you could propose some changes or improvements (highlighted in the following list):

1. An application owner *creates a request* defining *the application names*.
2. The requested communication flow is *validated against the security policy automatically*.
3. If the communication is *accepted*, an *analytical path discovery* is calculated to determine the devices in the path (using the IP data from the application definition).
4. A *scheduled task* is created to trigger an *automatic render of the configuration* that is *pre-validated* before moving forward.
5. When the scheduled time comes, *the automation engine deploys the configuration* to the different network infrastructure, and a *post-validation check validates that the operational state is correct*.
6. Once the configurations are pushed, *an automated notification with all the relevant information is sent* to the application owner, who can *use a dashboard to observe* the outcomes of the change.

In this proposed workflow, the user needs to define only the application name, hiding the complexity of IP addresses and ports, making the user input easier to validate (the application definition is an omitted step that happens before this workflow). Moreover, if desired, no further human intervention in the process is necessary. This process simplification allows adding new steps (e.g., post-validation), which adds more value without significantly slowing the delivery time.

###### Tip

When automating a workflow, don’t worry about automating all the steps at once. Sometimes the effort needed to automate a task could block progress on easier ones. Delaying complex tasks until your automation journey is ready could be a smart decision.

Now that you have a clear plan of what the automation solution has to implement, it’s time to map it to the network automation architecture.

## Map the Automated Tasks to Architecture Components

With the steps defined, you will start noticing synergies among them, which will help group some of them. Then these groupings will map to various architectural components. As we mentioned in [“Orchestration”](#orchestration), every task should be small enough to fit in one block. If that’s not the case, choose the one that better aligns with the task’s goal.

[Figure 14-14](#arch-example-2) depicts the automated workflow in a sequence diagram; the *objects* are the architecture components.

![npa2 1414](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1414.png)

###### Figure 14-14. Automated workflow in a sequence diagram

In this diagram, you can observe how the tasks are related to the architecture components. This classification is important to understand the requirements needed in each block. As a high-level summary, we can summarize the requirements of each component in this scenario as follows:

User interactionsOffer a bidirectional communication channel to submit requests and get notifications of the process updates. Also, they allow direct access to visualize the dashboards representing the state of firewall operations.

Source of truthNormalizes and validates the data received from the user, and performs extra data processing, including verifying the policy against the reference security policy, and discovering the devices that will be in the path of the communication flow. It also stores the *application* definition or provides a dynamic update of the servers registered for this *application* (i.e., a dynamic application service). Finally, it exposes the data and templates to generate the configuration artifacts, and, afterward, validates the operational state.

OrchestrationCoordinates the automation process either via a manual trigger from the user or scheduled after the changes in the SoT. Even though this sequence diagram shows only the *golden path*, it would handle any decision path to, in the end, communicate back to the user, via *user interactions*.

Automation engineUses the data and templates (defining the intent) to generate the configuration artifacts, pre-validates them to check whether they would provide the expected operational state, and then deploys the configuration to the network platforms.

Telemetry and observabilityGathers operational state continuously, and comparing to the intended one, it offers a post-validation check, besides providing access to relevant data (e.g., network flows or metrics) for visualization.

Once you understand what is expected from each component, you are ready to move to the next step, where you pick the tools to implement these functionalities.

###### Note

Keep in mind that, in a real-life scenario, you would gather more low-level information to better determine the requirements of each task.

## Choose the Tools to Implement Each Component’s Tasks

The first question to answer when approaching this phase, is the *build versus buy* dilemma. If you don’t have really special requirements, you likely won’t need to reinvent the wheel and build a complete solution from scratch. In this chapter, we have shared many open source solutions for each component, but many more options are available, both commercial and open source. Thus, you should evaluate which tools make more sense in your own environment regarding support, features, and extensibility.

Another key factor to consider here is your current tech stack and your team skills. If tools are already in place that can implement the new requirements, it seems reasonable to reuse them, if possible.

###### Tip

As a rule of thumb, look for other options only when you identify a key requirement that can’t be fulfilled with the current stack.

Resuming with the example, we propose a set of open source tools that could implement the automated workflow depicted in [Figure 14-14](#arch-example-2). Consider this one of the many ways to solve the proposed example and not as any kind of recommendation:

User interaction[Mattermost](https://oreil.ly/kpIZB) is an instant messaging application to allow user interaction, and [Grafana](https://oreil.ly/ztVwv) offers dashboards for network metrics visualization.

Source of truth[Nautobot](https://oreil.ly/-M6RM) defines the network inventory and the related models for application definition and firewall rules using the [Firewall Models](https://oreil.ly/Hrv1A) app. It also allows integration with [Git repositories](https://git-scm.com) to keep track of the Jinja templates for CLI-based firewalls, and [HashiCorp Consul](https://oreil.ly/zK1g5) provides a dynamic mapping of application to IP addresses and ports.

Orchestration[AWX](https://oreil.ly/IBMH1) manages the workflow execution. It can be triggered manually by a network operator or via a webhook from [Nautobot](https://oreil.ly/-M6RM) when a new firewall rule is created, updated, or deleted.

Automation engine[Batfish](https://oreil.ly/96QMA) provides pre-validation of network configurations rendered by [Ansible](https://oreil.ly/nbGmd), using the data from the SoT. Ansible configures the on-premises firewalls too. For cloud services, [Terraform](https://oreil.ly/bqBlD) is used to provision/update the services, also using the data from the SoT.

Telemetry and observabilityThe [Telegraf](https://oreil.ly/MwBF9) collector retrieves network data metrics from the firewall services and stores them in [Prometheus](https://oreil.ly/Ux0ig) for later consumption in a post-validation script, or via [Grafana](https://oreil.ly/DNFmi) dashboards.

This high-level design is just the beginning of the story. It serves as a reference to start implementing the automation solution, but you should always be open to new requirements or improvement ideas that may impact the initial decision process. As we pointed out before, it’s a good practice to document your architecture decisions, in order to make reviewing them later an easier task for you and others. And, trust us, you will eventually need to review them. Maybe some changes to the original workflow will appear or a new workflow will be implemented in parallel. With well-documented decisions, you will be able to either choose to reuse (and extend) the tooling in place or replace it with a new one.

###### Tip

Because so many tools are available, choosing one over another could be overwhelming. But don’t get blocked by the *premature optimization* trap, spending too much time now on solving a future issue (that may not even happen). Using the proposed architecture, you will be able to replace any tool with a new one when the necessity arises.

Hopefully, this section helped you get into the network automation *mindset* and consolidate the content of this chapter.

# Summary

This chapter had the ambitious goal of proposing an architectural approach to guide the design of network automation solutions. Technological knowledge that you learned throughout the book is an important foundation, but things get more complicated when you have to glue all these technologies (and tooling) together.

Our proposed network automation architecture gives you an easy-to-understand framework to map the functionalities of an operational workflow to a few components that summarize the main roles of a network automation solution (which is also mostly reusable for other IT infrastructure). Each architecture component has its role and relevance, but we stressed the importance of shifting to an intended approach where data drives the rest of the tasks, and integrations allow creation of complete solutions that can be adapted as needed.

Luckily, a lot of useful tools are out there to help you build solutions without having to start from scratch—but remember that automation is not about tooling, and you should never start your design with the tool. First, you need to make sure you understand the requirements and the expected outcomes. Then you can start mapping the features to the architecture and select which implementation fits your environment (better leaving the door open for future revisions).

We hope this architecture will help you get started building your first network automation solutions or improving your already implemented ones. This chapter closes the book, but this is only the beginning of your network automation journey. We encourage you to keep learning and exploring new technologies and tools to improve your automation skills. This book is a good starting point, but the network automation world is constantly evolving, and you should keep up with the latest trends and best practices while trying to apply them to your own projects.
