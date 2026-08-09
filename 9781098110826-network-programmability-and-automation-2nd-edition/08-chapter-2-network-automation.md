# Chapter 2. Network Automation

In this chapter, we’re focused on providing a baseline of high-level network automation concepts so that you are better equipped to get the most out of each chapter going forward. To accomplish this, the following topics are included in this chapter:

Why network automation?Examines various reasons to adopt automation and increase the efficiencies of network operations while proving there is much more to automation than delivering configurations faster to network devices.

Types of network automationExplores various types of automation, from traditional configuration management to automating network diagnostics and troubleshooting, proving once again that there is more to automation than decreasing the time it takes to make a change.

Evolving the management plane from SNMP to device APIsBriefly introduces a few API types found on network devices of the past and present.

Network automation in the SDN eraProvides a short synopsis of why network automation tooling is still valuable when SDN solutions, specifically referring to controller-based architectures, are deployed.

###### Note

This chapter is not meant to provide deep technical content but rather an introduction to the concepts of network automation. This chapter simply lays the foundation and provides context for the chapters that follow.

# Why Network Automation?

Network automation, like most types of automation, is considered a means of doing things faster. While accomplishing tasks more quickly is nice, reducing the time for deployments and configuration changes isn’t always a problem that needs solving for many IT organizations.

In this section, we take a look at a few reasons, including speed, that IT organizations of all shapes and sizes should be looking at gradually adopting network automation. You should note that the same principles apply to other types of automation as well (application, systems, storage, telephony, etc.).

## Simplified Architectures

It is still common today that network devices are configured as unique snowflakes (having many one-off, nonstandard configurations), and network engineers take pride in solving transport and application issues with one-off network changes that ultimately make the network not only harder to maintain and manage but also harder to automate.

Instead of network automation and management being treated as a secondary project or an add-on, it needs to be included from the outset as new architectures are being created. This includes ensuring a proper budget for personnel and tooling. Unfortunately, tooling is often the first item cut in budget shortage.

The end-to-end architecture and associated day 2 operations need to be one and the same. You need to think about the following questions as architectures are created:

- Which features work across vendors?
- Which extensions work across platforms?
- What type of API or automation tooling works with particular network device platforms?
- Is there solid API documentation?
- What libraries exist for a given product?

When these questions get answered early in the design process, the resulting architecture becomes simpler, repeatable, and easier to maintain *and* automate, all with fewer vendor-proprietary extensions enabled throughout the network.

Even after the simplified architecture gets deployed with the right management and automation tooling, remember that minimizing one-off changes is still a necessity, to ensure that the network configurations don’t become snowflakes again.

## Deterministic Outcomes

In an enterprise organization, change review meetings take place to examine upcoming changes on the network, their impact on external systems, and rollback plans. In a world where a human is touching the CLI to make those upcoming changes, the impact of typing the wrong command can be catastrophic. Imagine a team with 3, 4, 5, or 50 engineers. Every engineer may have their own way of making that particular upcoming change. Moreover, the ability to use a CLI and even a GUI does not eliminate or reduce the chance of error during the control window for the change.

Using proven and tested network automation to make changes helps achieve *more predictable* behavior than making changes manually, and gives the executive team a *better chance* at achieving deterministic outcomes, moving one step closer to ensuring that the task at hand will get done right the first time, without human error. This task could be anything from a VLAN change to onboarding a new customer that requires several changes throughout the network.

Moreover, these deterministic outcomes imply lower operating expenses (OpEx) because less manual labor is involved in executing network changes, increasing the efficiency of the overall network operations (e.g., automating time-consuming processes like upgrading the operating system on a network device). The operating time saved by network engineers can be used to focus on more strategic projects, to keep improving the process.

## Business Agility

Since the advent of server virtualization, systems administrators could deploy new applications almost instantaneously. And the faster applications are deployed, the more questions are raised as to why it takes so long to configure network resources such as VLANs, routes, firewall policies, load-balancing policies, or all of the above if deploying a new three-tier application.

It should be fairly obvious that by adopting network automation, the network engineering and operations teams can react faster to their IT counterparts for deploying applications. More importantly, automation helps the business be more agile. From an adoption perspective, it’s critical to understand the existing, and often manual, workflows before attempting to adopt automation of any kind, no matter how good your intentions are for making the business more agile.

If you don’t know what you want to automate, that lack of knowledge will complicate and prolong the process. Our *number one* recommendation as you start your network automation journey is to always understand existing manual workflows, document them (e.g., average time to complete, the number of times each step occurs), and understand the impact they have on the business. Then, the implementation of an automation solution becomes simpler and more effective.

## Enhanced Security and Risk Reduction

Describing the networking-related workflows as code brings an implicit benefit of automation: the code captures and documents the step-by-step process definition and analysis, making it available for everyone, at any time. This exposure allows the introduction of peer review in the workflow (as other engineers share responsibility for the changes) as well as the automated processing to discover potential security issues or configuration errors before actually deploying the changes to the network. And, when the automation is in place, it will make sure that the network keeps operating as defined, remediating any deviations as needed.

In traditional network operations, the outcome of a task depends heavily on the network engineers’ experience performing it, and the available documentation, which is always hard to keep up-to-date. However, when the same task is automated, every time the workflow is executed, it will apply all the knowledge from all the engineers who have contributed to it.

Automation enables sharing of responsibility across the team and makes the process more effective and less prone to introducing problems because it enforces extra human review. Automation also enables processing by tools that can enforce rules, such as security policies, or even connecting with artificial analysis tools to *recommend* improvements from the context.

Furthermore, network automation is not a one-time effort. Unexpected issues or missing points will likely be detected, and every time this happens, the workflow code will need to be adjusted, becoming better than before. This continuously improving approach, over time, will merge all the contributions, from former and current team members, in an incremental improvement process.

From simplified architectures to continuous improvement, this section introduced some of the high-level reasons you should consider network automation. In the next section, we take a look at types of network automation.

# Types of Network Automation

Automation is commonly equated with speed, and considering that some network tasks don’t require speed, it’s easy to see why some IT teams don’t see the value in automation. VLAN configuration is a great example; you may be thinking, “How *fast* does a VLAN really need to be created? Just how many VLANs are being added on a daily basis? Do *I* really need automation?” These are all valid questions.

This section focuses on several other tasks for which automation makes sense: device provisioning, data collection and enrichment, migrations, configuration management, configuration compliance, state validation, troubleshooting, and reporting. But remember, as we stated previously, automation is much more than speed and agility; it also offers you, your team, and your business more predictable and more deterministic outcomes while reducing risk and increasing security.

## Device Provisioning

One of the easiest and fastest ways to get started with network automation is to automate creating the device configuration files used for initial device provisioning and pushing them to network devices.

If we break this process into two steps, the first is creating the configuration file, and the second is pushing the configuration onto the device.

To automate the creation of configuration files (or configuration data in general), we first need to decouple the *inputs* (configuration parameters) from the underlying vendor-proprietary syntax (CLI) of the configuration. We’ll end up with separate files: one file with values for the configuration parameters such as VLANs, domain information, interfaces, routing, and everything else; and another file that is the configuration template.

For now, think of the configuration template as the equivalent of a standard golden template that’s used for all devices getting deployed. By using *network configuration templating*, you can quickly produce consistent network configuration files specifically for your network. You’ll never have to use Notepad ever again, copying and pasting configs from file to file—​isn’t it about time for that?

Two tools that streamline using configuration templates with variables (data inputs) are Ansible and Nornir. In less than a few seconds, these tools can generate hundreds of configuration files predictably and reliably.

###### Note

Building and generating configuration files from templates are covered in much more detail in [Chapter 9](ch09.html#templating), while performing the templating process with Ansible and Nornir is covered in [Chapter 12](ch12.html#automationtools). This section is merely showing a high-level basic example.

Let’s look at an example of taking a current configuration and decomposing it into template and variable (input) files to articulate the point we’re making. In [Example 2-1](#config-snippet), you can observe a CLI configuration from a random vendor.

##### Example 2-1. Configuration file snippet

```
hostname leaf1
ip domain-name ntc.com
!
vlan 10
  name web
!
vlan 20
  name app
!
vlan 30
  name db
!
```

If we decouple the data from the CLI commands, this file is transformed into two files: a template and a data (variables) file. First, let’s look at the YAML definition in the variables file in [Example 2-2](#config-snippet-yaml) (we cover YAML in depth in [Chapter 8](ch08.html#dataformats)).

##### Example 2-2. YAML data

```
---
hostname: leaf1
domain_name: ntc.com
vlans:
  - id: 10
    name: web
  - id: 20
    name: app
  - id: 30
    name: db
```

Note that the YAML file contains only our *data*.

The resulting template that is rendered with the data file looks like [Example 2-3](#config-snippet-jinja) and is given the filename *leaf.j2*.

##### Example 2-3. Jinja template

```
!
hostname {{ inventory_hostname }}
ip domain-name {{ domain_name }}
!
{% for vlan in vlans %}
vlan {{ vlan.id }}
  name {{ vlan.name }}
{% endfor %}
!
```

###### Note

In [Example 2-3](#config-snippet-jinja), we’re showing the Python-based [Jinja templating language](https://jinja.palletsprojects.com). Jinja is covered in detail in [Chapter 9](ch09.html#templating).

In this example, the *double curly braces* denote a Jinja variable. This is where the data variables get inserted when a template is rendered with data. Since the double curly braces denote variables, and we see those values are not in the template, they need to be stored somewhere. Again, we stored them in a YAML file. Rather than use flat YAML files, you could also use a script to fetch this type of information from an external system such as a network management system (NMS) or IP address management (IPAM) system.

In this example, if the team members who control VLANs want to add a VLAN to the network devices, no problem. They just need to change it in the variables file and regenerate a new configuration file by using Ansible or the rendering engine of their choice (e.g., Salt, pure Python, etc.).

At this point in our example, once the configuration is generated, it needs to be *pushed* to the network device. The *push* and *execution* process is not covered here, as there are plenty of ways to do this, including vendor-proprietary provisioning solutions as well as a few other methods that we present in Chapters [10](ch10.html#apis) and [12](ch12.html#automationtools).

Additionally, this is only a high-level introduction to templates; don’t worry if the details are not 100% clear yet. As we’ve said, working with templates is covered in far greater detail in [Chapter 9](ch09.html#templating).

Aside from building configurations and pushing them to devices, something that is arguably more important is data collection, which happens to be our next topic.

## Data Collection and Enrichment

Monitoring tools typically use SNMP to poll certain management information bases (MIBs) for data. The data returned may be more or less than you actually need. What if interface stats are being polled? You may get back every counter displayed in a `show interface` command, but what if you need only interface resets and not cycling redundancy check (CRC) errors, jumbo frames, or output errors? Moreover, what if you want to see the interface resets correlated to the interfaces that have Cisco Discovery Protocol (CDP) or LLDP neighbors on them, and you want to see them *now*, not on the next polling cycle? How does network automation help with this?

Given that our focus is on providing you more power and control, you can leverage open source tools and technology to customize exactly what you get, when you get it, how it’s formatted, and how the data is used after it’s collected. This automated approach ensures that you get the most value from the data.

[Example 2-4](#netmiko-collect) is a *very* basic illustration of collecting data from a Cisco Internetwork Operating System (IOS) device via the Python library Netmiko, which we cover in more detail in [Chapter 10](ch10.html#apis).

##### Example 2-4. Netmiko script

```
from netmiko import ConnectHandler

device = ConnectHandler(
  device_type='cisco_ios',
  host='csr1',
  username='ntc',
  password='ntc123'
)

output = device.send_command('show version')
print(output)
```

The great part is that `output` contains the `show version` response, and you can parse it as you see fit based on your requirements. But the code also has a not-so-pretty part: the output of this CLI command is unstructured data, so you would end up implementing custom screen-scraping logic, which is difficult to maintain. Small output changes could break the whole parsing. As you will see in [Chapter 8](ch08.html#dataformats), most platforms nowadays are offering structured data formats that enable more robust automation, and screen scraping is used only as a *last resort*.

###### Note

In the preceding example, we are describing *pulling* data off the devices, which may not be ideal for all environments (but still suitable for many). Be aware that newer devices are starting to support a *push* model, often referred to as *streaming telemetry*: the device itself streams real-time data such as interface stats to an application server of your choice. You’ll see more details in Chapters [10](ch10.html#apis) and [14](ch14.html#architecture).

Of course, any data collection may require some up-front custom work but is totally worth it in the end—because the data being gathered is what you need, not what a given tool or vendor is providing you. Plus, isn’t that why you’re reading this book?

Network devices have an enormous amount of static and ephemeral data buried inside, and using open source tools or building your own gets you access to this data. Examples of this type of data include active entries in the BGP table, OSPF adjacencies, active neighbors, interface statistics, specific counters and resets, and even counters from ASICs themselves on newer platforms. Additionally, general facts and characteristics of devices can be collected too, such as serial number, hostname, uptime, OS version, and hardware platform, just to name a few. The list is endless.

###### Tip

Always consider these questions as you start an automation project: “Does it make sense to build, buy, or customize?” and “Does it make sense to consume or operate?”

But not least important in data collection is *how* we get the best of this data. As you will learn in [Chapter 14](ch14.html#architecture), after we collect the network state (metrics, logs, or flows), we can enrich it with metadata—such as adding a *tag* for the site an interface counter metric comes from. Then, in the analysis or visualization tooling, we could correlate all this data to get more educated outcomes. To make this happen, we need to get this information from someplace where a relationship exists between the device (owner of the interface) and the site where it is installed. This is the role of the *source of truth*, covered in the same chapter.

## Migrations

Migrating from one platform to the next is never an easy task. This may involve platforms from the same vendor or from different vendors. Vendors may offer a script or a tool to help with migrations to *their* platform, but you can use various forms of automation to build out configuration templates, just as in our example earlier, for all types of network devices and operating systems. You could then generate a configuration file for all vendors, given a defined and common set of inputs (common data model).

Of course, if you are using vendor-proprietary extensions, they’ll need to be accounted for too. The beautiful thing is that a migration tool such as this is much simpler to build on your own than having a vendor do it: whereas the vendor needs to account for all features the device supports, an individual organization needs only a finite number of features. In reality, this is something vendors don’t care much about; they are concerned with their equipment, not making it easier for you, the network operator, to manage a multivendor environment.

Having this type of flexibility helps with not only migrations, but also DR, as it’s common to have different switch models in the production and DR data centers, and even different vendors. If a device fails for any reason and its replacement has to be a different platform, you’d be able to quickly leverage your common data model (think parameter inputs) and generate a new configuration immediately. We’re starting to use the term *data model* loosely, but rest assured, we spend more time describing data models in [Chapter 8](ch08.html#dataformats).

Thus, if you are performing a migration, think about it at a more abstract level and think through the tasks necessary to go from one platform to the next. Then, see what can be done to automate those tasks, because only you, not the large networking vendors, have the motivation to make multivendor automation a reality. For example, think about adding a VLAN as an abstract step—​then you can worry about the lower-level commands per platform. The point is, as you start adopting automation, it’s extremely important to think about tasks and document them in a human-readable format that is vendor neutral, before putting your hands to the keyboard to type in CLI commands or write code (per platform).

## Configuration Management

As we’ve stated, configuration management is the most common type of automation, so we aren’t going to spend too much time on it here. We define *configuration management* as deploying, pushing, and managing the configuration state of a device. This includes anything as basic as interfaces’ descriptions to more complex workflows that configure ToR switches, firewalls, load balancers, and advanced security infrastructure, to deploy three-tier applications.

As you can see already through the forms of automation that are *read-only*, you do not need to start your automation journey by pushing configurations. That said, if you are spending countless hours pushing the same change across a given number of routers or switches, you may want to!

The reality is that there are so many ways to start a network automation journey, but when you start automating configuration management, remember, with great power comes great responsibility. More importantly, don’t forget to test new automation tools before rolling them out to production environments. You have several options to test your automation logic via emulation network platforms, as you will see in [Chapter 5](ch05.html#developmentenvironments).

# Lessons Learned from a Network Automation Outage

In October 2021, one of the largest automated networks in the world went down. Facebook, now Meta, provided an [outage report](https://oreil.ly/0jUqD) explaining that despite having an *audit control* for its configuration management system to prevent pushing harmful configurations, a BGP configuration change caused a global outage.

We shouldn’t forget that automation amplifies everything—the good and the bad. Thus, it is crucial to understand the importance of testing a network automation system with a *continuous integration* (CI) process (as it has been adopted in software development) before deploying to production. We explain how CI works in [Chapter 13](ch13.html#cicd). The Facebook outage is an example of how complex it is to get CI right.

Nowadays, tools such as Batfish can perform analytical network verification; from given configurations, these tools create a network model to simulate the state of the network—but this is only an approximation. Simulating *all* the options configured in a network is extremely complex (do you remember when we mentioned the importance of simplicity for automation?). As we stated before, network emulation tools can help us run network devices in on-demand environments. All these tools can be used in CI pipelines to verify how the network automation tooling interacts with the network devices before going into production, anticipating potential issues and unexpected collateral effects.

As expected, Facebook had its own homegrown audit control tool to validate changes via CI, but the chance of hitting an unexpected bug always remains. To mitigate this, we recommend you embrace uncertainty and adopt software development approaches, such as *canary deployments*, which progressively roll out changes to the fleet. This allows us to validate the outcome of a small subset of devices, and then, incrementally, continue releasing to the rest of the network.

The next few types of network automation we cover stem from automating the process of data collection. We’ve broken out a few of them to provide more context, and the first up is automating compliance checks.

## Configuration Compliance

As with many forms of automation, making configuration changes with any type of automation tool is seen as a risk. While making manual changes could arguably be riskier, as you’ve read and may have experienced firsthand, you have the option to start with data collection, monitoring, and configuration building, which are all *read-only* and *low-risk* actions.

One low-risk use case that uses the data being gathered is configuration compliance checks and configuration validation. Does the deployed configuration meet security requirements? Are the required networks configured? Is protocol *XYZ* disabled? When you have control over the tools being deployed, it is more than possible to determine whether something is `True` or `False`. It’s easy enough to start small with one compliance check and then gradually add more as needed.

Based on the compliance of what you are checking, it’s up to you to determine what happens next—maybe the data just gets logged, or maybe a complex operation is performed, making your application capable of auto-remediation. These are forms of event-driven automation that we also touch upon when we cover Ansible in [Chapter 12](ch12.html#automationtools).

Our recommendation is that it’s always best to start simple with network automation, but being aware of what’s possible adds significant value as well. For example, if you just log or print messages to see what an interface maximum transmission unit (MTU) is, you’re already prepared should you want to automatically reconfigure any undesirable MTU to the right value. You’d need just a few more lines underneath your existing log/print messages. Again, the point is to start small but think through what else you may need in the future.

## State Validation

A step further than configuration compliance—still read-only and low risk—is to validate the *result* of the configuration, the actual operational state of the network (also known as network assurance). Obviously, this requires the definition of the *intended* operational state alongside the configuration one. For instance, regarding a BGP neighbor configuration, configuration compliance would validate the configuration state, syntax, and data for the neighbor IP address, autonomous system number (ASN), and MD5 authentication key. In addition, the state validation checks the state of these sessions, expecting an `Established` status. The configuration could be right, but a network outage or a misconfiguration on the other end could rise a validation issue.

The state validation adds an extra control layer on top of the automation process. This validation can be used to verify that the rollout of a desired configuration change is not breaking the desired operational state, or to constantly verify the network state. The outcome, for example, could be raising warnings with relevant state data or triggering a mitigation process. Following the BGP example, when an unexpected BGP session state is detected, the automation will retrieve and attach the related BGP logs, and stats, into a notification to the network team.

###### Note

A common state validation type is the *pre/post change validation*. In this case, there is no predefined intended operational state. The intended state is simply taken from a snapshot collected before performing a future action. For instance, during an OS upgrade workflow, the operational state is collected before the upgrade and defines the desired state. After the upgrade, this state is validated against the actual state. If the final state is not successful, a rollback process could be triggered to use the previous OS version.

## Reporting

Once you start automating data collection, you may want to start building out custom and dynamic reports too. Maybe the data being returned becomes the input to other configuration management tasks (event-driven again or more basic conditional configuration), or maybe you just want to create reports.

Reports can also be easily generated from templates combined with the actual ephemeral data from the device that’ll be inserted into the template. Creating and using reporting templates follows the same process as for configuration templates that we touched upon earlier in the chapter (remember, we explore templates in much more depth in [Chapter 9](ch09.html#templating)).

Because of the simple nature of using text-based templates, you can produce reports in any format you wish, including, but not limited to, the following:

- Simple text files
- Markdown files that can be easily viewed on GitHub or another Markdown viewer
- HTML reports that are deployed to a web server for easy viewing

Your format choice depends on your requirements. The great thing is that the *network automator* has the power to create the exact type of report needed. In fact, you can use one set of data to generate different types of reports, maybe some technical and some higher level for management, and then select the best UI to send them, maybe via email or instant messaging.

Next up, we take a look at the value of automated troubleshooting.

## Troubleshooting

Who enjoys getting consistently pulled into break/fix problems, especially when you should be sleeping or focused on other things? Once you have access to real-time data and don’t need to do any manual parsing on that data, automated troubleshooting becomes a reality.

Think about *how* you troubleshoot. Do you have a personal methodology? Is that methodology consistent across all members of your team? Does everyone check Layer 2 before troubleshooting Layer 3? What steps do you take to troubleshoot a given problem?

Let’s take troubleshooting OSPF as an example:

- Do you know what it takes to form an OSPF adjacency between two devices?
- Can you rattle off the same answers at 2 a.m. or while on vacation at the beach?
- Do you remember that some devices need to be on the same subnet, have the same MTU, and have consistent timers, but forget that they need to be the same OSPF network type?
- Do we really need to remember all of this and the associated commands to run on the CLI to get back each piece of data?

And these questions are only a *few* of the things that need to match for OSPF.

In any given environment, these types of compatibility checks need to be performed. Can you fathom running a script or using a tool for OSPF neighbor validation versus performing that process manually? Which would you prefer?

Again, OSPF is only the tip of the iceberg. Think about these other questions, still just being the tip:

- Can you correlate particular log messages to known conditions on the network?
- What about BGP neighbor adjacencies? How is a neighbor formed?
- Are you seeing all of the routes you think you should in the routing table?
- What about port channels? Are there any inconsistencies?
- Do neighbors match the port-channel configuration (going down to the vSwitch)?
- What about cabling? Are all of the cables plugged in properly?

Even with these questions, we are just scratching the surface of the possibilities when it comes to automated diagnostics and troubleshooting.

###### Note

As you start to consider all the types of automation possible, start to imagine a closed-loop system: data is collected in an automated fashion, the data is then processed and analyzed in an automated fashion, and then you use advanced analytics to troubleshoot in an automated fashion. As these start to happen together and uniformly, the system becomes a closed loop, fully changing the way operations are managed within an organization.

If you are the rock star network engineer on your team, you may want to think about partnering up with a developer, or at the very least, start documenting your workflows so it’s easier to share your knowledge and it becomes easier to *codify*. Better yet, start your own personal automation journey so you can sleep in every so often and empower everyone else to troubleshoot by using some of your automated diagnostic workflows.

As you can see, network automation is much more than deploying configurations faster. After looking at several types of automation, we are going to shift topics now and look at a few ways automation tools and applications communicate with network devices.

# Evolving the Management Plane from SNMP to APIs

If you want to improve the way networks are managed and operated day-to-day, you must begin with the way you interface with the underlying devices being managed. This interface is how you and, more importantly, automation tools communicate with devices to perform the various types of network automation, such as data collection and configuration management.

In this section, we provide an overview of the methods available to connect to the management plane of network devices—starting with SNMP and then moving on to more modern ways such as NETCONF, RESTful APIs, RESTCONF, and gNMI. We then look at the impact of the *open networking* movement as it pertains to network operations and automation.

## Application Programming Interfaces

As a network engineer, you need to embrace APIs going forward and not fear them. Remember that an API is just a mechanism used for computer software on one device to talk to computer software on another device. APIs are used nearly everywhere on the internet today—​they just happen to finally be getting the focus they deserve from network vendors. Today we are seeing that APIs are becoming the primary means of managing new network devices.

While we cover specific network APIs in more detail in [Chapter 10](ch10.html#apis), this section provides a high-level overview of a few types of APIs that you’ll find on network devices today.

### SNMP

SNMP has been widely deployed for over 25 years on network devices. It shouldn’t be new to anyone reading this book, but SNMP is a protocol that is used quite commonly for polling network devices for information such as up/down status and CPU, memory, and interface utilization.

To use SNMP, there must be an SNMP agent on a managed device and a network management station, which is the device that functions as a *server* that monitors and/or controls the managed devices.

Each network device being managed exposes a set of data that can be collected and configured via the SNMP agent. This set of data that is managed through SNMP is described and modeled through MIBs. Only if an MIB is exposing a certain feature can it be monitored or managed. This includes making configuration changes through SNMP. Often overlooked, SNMP not only supports `GetRequest`s for monitoring but also supports `SetRequest`s for manipulating objects and variables exposed through MIBs. The issue is that not many vendors offer full support for configuration management via SNMP; when they do, they often use custom MIBs, slowing the integration process to network management platforms.

As mentioned, SNMP has been around for decades, but it was not built to be a real-time programmatic interface to network devices. We are already seeing vendors claim the gradual death of SNMP as it pertains to next-generation management and automation tooling. That said, SNMP does exist on nearly every network device, and Python libraries for SNMP also exist—​so, if you need to collect basic information from a vast number of device types, using SNMP may still make sense.

Just as SNMP has been used for years to perform network monitoring, SSH/Telnet and the CLI have been used for configuration management (and for retrieving state). Let’s take a look now at SSH/Telnet and the CLI.

### SSH/Telnet and the CLI

If you’ve ever managed a network device, you’ve definitely used the CLI to issue commands to perform an action on a device. You probably entered commands through the console and over Telnet and SSH sessions. As we stated in [Chapter 1](ch01.html#trends), the reality is that the migration from Telnet to SSH is arguably the biggest shift we’ve had in network operations over the past decade, and that shift wasn’t about operations; it was about security ensuring that communications to network devices were encrypted.

The most important point to realize as it pertains to managing devices via the CLI is that the CLI was built for humans. It was put on devices to improve usability for human operators. The CLI was *not* meant to be used for machine-to-machine communication (network scripting and automation).

If you issue a `show` command on the CLI of a device, you get raw text back. This output has no structure. The best options to *parse* the response are to use the *pipe* (`|`) and keywords such as `grep`, `include`, and `begin` to look for particular lines of configuration. You might check the description of an interface with the command `show interface Eth1 | include description`, for example. If you needed to know how many CRC errors were on an interface after issuing a `show interface` in a script, you’d be forced to use some type of regular expression or manual parsing to figure it out. This is unacceptable.

However, when all we have is the CLI, the CLI gets used. This is why plenty of network management platforms and custom scripts have been built over the past two decades that perform management and automated operations by using the CLI over SSH to deal with expect scripts and manual parsing. It’s not that SSH/CLI makes it impossible to automate; rather, it makes automation extremely error prone and tedious.

The network vendors started to realize this, and now most newer device platforms have some type of API that simplifies machine-to-machine communication (many are incomplete, so be sure to test your favorite device’s API). This change has yielded a much simpler approach to automation that is also more in line with general software development principles.

Now that we’ve introduced common protocols such as SSH and SNMP, let’s look at NETCONF, an API that is becoming quite popular as it pertains to network automation.

### NETCONF

Like SNMP, NETCONF is a network management layer protocol defined by the Internet Engineering Task Force (IETF). At the highest level, NETCONF can be compared to SNMP, as both are protocols used to make configuration changes and retrieve data from networking devices. The differences come in the details, of course. We cover a few high-level points here but spend more time on NETCONF in [Chapter 10](ch10.html#apis).

NETCONF is a connection-oriented protocol that commonly leverages SSH as its transport; the data transferred is encoded with XML. NETCONF supports remote procedure calls (RPCs) to send prearranged operations to the devices (i.e., the `edit-config` operation). Also, it uses data models represented in YANG to define the data structures supported. Don’t worry if you aren’t familiar with XML or YANG; we cover both in [Chapter 8](ch08.html#dataformats).

NETCONF devices expose the supported data models and operations via their *capabilities*, which differ from one platform to another. Just because two device platforms support NETCONF (or any common transport method) does not mean they are compatible from a tooling and developer’s perspective. Even with the assumption that both devices support the same NETCONF features and capabilities, the way the data is modeled is, more often than not, vendor specific.

Additionally, NETCONF offers value in that it supports transaction-based changes. If you are making more than one change in a given NETCONF session or single XML document, and one of those changes fails, the complete change is *not* applied to the device (of course, these types of settings can usually be overridden too). This is in contrast to sending CLI commands sequentially and ending up with a partial configuration due to a typo or invalid command.

### RESTful APIs

*REST*, which stands for *Representational State Transfer*, is a style used to design and develop networked applications. Thus, systems that implement and adhere to a REST-based architecture are said to be *RESTful*.

In the context of a network, the most common devices that expose APIs and adhere to the REST architectural style are network controllers. That said, network devices expose RESTful and general HTTP-based APIs too, including a derivative from NETCONF called RESTCONF. We cover HTTP-based APIs in [Chapter 10](ch10.html#apis).

While the terms *REST* and *RESTful APIs* are new from a network standpoint, you’re already interacting with many RESTful systems on a daily basis as you browse the internet via a web browser. We said that REST is a style used to develop networked applications. That style relies on a stateless client-server model in which the client keeps track of the session and no client state or context is held on the server. And best yet, the underlying transport protocol used is most commonly HTTP. Doesn’t this sound like most systems found on the internet?

This means that RESTful APIs operate just like HTTP-based systems. First, you need a web server accessible via a URL (i.e., *SDN controller* or *network device* to communicate with), and second, you need to send the associated HTTP request to that URL. For example, if you need to retrieve a list of devices from an SDN controller, you just need to send an HTTP GET to the given URL of the device, which could look something like this: `http://192.0.2.1/v1/devices`. The response that comes back would be some type of structured data like XML or JSON (which we cover in [Chapter 8](ch08.html#dataformats)).

### gNMI

Traditionally, network interfaces and protocols have been driven by standardization entities, such as NETCONF defined by the IETF. However, in 2017 the [OpenConfig consortium](https://www.openconfig.net), led by Google, released the [gNMI](https://oreil.ly/TuI43), a gRPC-based protocol to handle configuration management and state data collection via telemetry streams as a community open source project that could benefit from a faster development pace due to its simpler consensus process.

OpenConfig was created in 2014 to develop programmatic interfaces and tools for managing networks in a dynamic and vendor-neutral way. Since then, more and more [participants](https://oreil.ly/islad) have joined, representing some of the biggest networking organizations in the world. Their initial focus was on compiling a set of vendor-neutral data models based on actual operational needs to solve the use cases and requirements of their members.

gNMI supports RPC operations (e.g., `set` or `get`) and uses YANG data models like NETCONF. So, how do both protocols/interfaces differ? They have a few technical differences such as the transport (i.e., gRPC) or the encoding (i.e., protobuf). You’ll learn more about gNMI in [Chapter 10](ch10.html#apis). The main difference is in the development strategy, with its own feature roadmap. For instance, gNMI supported streaming telemetry via subscription from the beginning because it was a top priority for the OpenConfig consortium.

Next up is a short look at the impact *open networking* is having on the overall management of network devices.

## Impact of Open Networking

We’re seeing a growing trend of all things *open*—open source, open networking, open APIs, OpenFlow, Open Compute, Open vSwitch, OpenDaylight, OpenConfig, and the list goes on. While the definition of *open* can be debated, one thing is certain: the *open networking* movement is expanding what is possible when it comes to network operations and automation. With this movement, we are seeing drastic changes in network devices, and this is the primary reason for writing this book.

First, many devices now support running Python directly in them. This means that you can drop into the Python dynamic interpreter and execute Python scripts locally on each network device. We cover Python in much more detail in [Chapter 6](ch06.html#python), and you’ll see what we mean firsthand.

Second, many devices now support a more robust API other than SNMP and SSH. For example, we just looked at NETCONF, gNMI, and RESTful HTTP-based APIs. One or more of those APIs are supported on many of the newer device operating systems that have emerged in recent years. Remember, we cover device APIs in more detail in [Chapter 10](ch10.html#apis).

Finally, network devices are exposing more of the Linux internals that have been hidden from network operators in the past. You can now drop into a *bash* shell on network devices and issue commands such as `ifconfig`, write bash scripts, and install monitoring and configuration management tools via package managers such as `apt` and `yum`. You’ll learn about all of these things in [Chapter 3](ch03.html#linux). And with Linux, you can also run applications packaged as containers (covered in [Chapter 4](ch04.html#cloud)), changing the understanding of what we can achieve on network devices.

While *open networking* doesn’t always mean interoperability, network devices and controllers are opening themselves up to be operated in a much more programmatic manner that’s better suited for enhanced network automation. The net result, for you as an operator, is that you can take control of your networks and reduce the number of operational inefficiencies that exist today as you start using these APIs.

# Network Automation in the SDN Era

We’ll now take a look at the continued importance of network automation even when controller solutions such as OpenDaylight or even commercial offerings like Cisco ACI or VMware NSX are being deployed. The operations that the controllers perform on the network, such as acting as the control plane or managing policy and configuration, are irrelevant to this section.

The fact is that controllers are becoming common in next-generation architectures. Vendors such as Cisco, Juniper, VMware, Arista Networks, NVIDIA, and many others all offer controller platforms for their next-gen solutions, not to mention open source controllers such as OpenDaylight, ONOS, and TeraFlow.

Almost every controller on the market exposes northbound RESTful APIs, making controllers extremely easy to automate. While controllers themselves inherently simplify management and visibility through a single pane of glass, you can still end up making manual and error-prone changes through the GUI of a controller. If several pods or controllers are deployed, from the same or different vendors, the problems of manual changes, troubleshooting, and data collection are still relevant.

As we start to wrap up this chapter, it’s important to note that even in the new era of SDN architectures and controller-based network solutions, the need for automation, better operations, and more predictable outcomes does not go away.

# Summary

This chapter provided an overview of the value of network automation and various types of network automation; an introduction to common device APIs including SNMP, CLI/SSH, and more importantly, NETCONF, RESTful APIs, and gNMI ([Chapter 10](ch10.html#apis) takes a deep dive on them); and a brief mention of YANG, a data modeling language that we cover in more detail in [Chapter 8](ch08.html#dataformats).

The chapter closed with a brief look at the impact that the open networking movement is having on network operations and automation. Finally, we touched on the value of network automation even when SDN controllers are deployed.

In each subsequent chapter, we dive deeper into each technology, providing hands-on practical examples whenever possible, but at the same time reviewing the importance of the people, process, and culture required to adopt comprehensive automation frameworks and pipelines.
