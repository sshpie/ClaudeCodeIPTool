# Chapter 23. Intrusion Detection and Response

**IN THIS CHAPTER**

- **Understanding intrusion detection mechanisms**
- **Understanding honeypots and their application**
- **Reviewing incident handling**

Detecting and responding to network attacks and malicious code is one of the principal responsibilities of information security professionals. Formal techniques and procedures have been developed by expert practitioners in the field to provide a structured approach to this difficult problem.

This chapter discusses these techniques as well as the different response mechanisms performed during an incident.

# Intrusion Detection Mechanisms

Intrusion detection (ID) comprises a variety of categories and techniques. The prominent approaches involve determining if a system has been infected by viruses or other malicious code and applying methods for spotting an intrusion in the network by an attacker. Virus-scanning and infection-prevention techniques are used to address the virus problem, and intrusion detection and response mechanisms target network intrusions.

## Antivirus approaches

Virus scanning and virus prevention techniques are normally used to prevent viruses from compromising valuable network resources.

### Virus scanners

Virus scanners use pattern-matching algorithms that can scan for many different signatures at the same time. These algorithms include scanning capabilities that detect known and unknown worms and Trojan horses. These products scan hard disks for viruses and, if any are found, remove or quarantine them. Antivirus software also performs auto-update functions that automatically download signatures of new viruses into the virus-scanning database.

### Virus prevention

Virus prevention software usually resides in memory and monitors system activity, or filters incoming executable programs and specific file types. When an illegal virus accesses a program or boot sector, the system is halted and the user is prompted to remove that particular type of malicious code.

## Intrusion detection and response

Intrusion detection and response are the tasks of monitoring systems for evidence of intrusions or inappropriate usage and responding to this evidence. Response includes notifying the appropriate parties to take action to determine the extent of the severity of an incident and to remediate the incident's effects. ID, therefore, is the detection of inappropriate, incorrect, or anomalous activity.

An intrusion detection and response capability has two primary components:

- Creation and maintenance of intrusion detection systems (IDSs) and processes for host and network monitoring and event notification.
- Creation of a computer incident response team (CIRT) for the following tasks:Analysis of an event notificationResponse to an incident if the analysis warrants itEscalation path proceduresResolution, post-incident follow-up, and reporting to the appropriate parties

An IDS is a system that monitors network traffic or host audit logs to determine whether any violations of an organization's security policy have taken place. An IDS can detect intrusions that have circumvented or passed through a firewall or that are occurring within the local area network (LAN) behind the firewall.

Various types of IDSs exist. The most common approaches to ID are *statistical anomaly detection* (also known as *behavior-based*) and *signature-based* (also known as *knowledge-based* or *pattern-matching*) *detection*. Intrusion detection systems that operate on a specific host and detect malicious activity only on that host are called *host-based ID systems*. ID systems that operate on network segments and analyze that segment's traffic are called *network-based ID systems*. Because there are pros and cons of each, an effective IDS should use a combination of both network- and host-based IDSs. A truly effective IDS will detect common attacks, including distributed attacks, as they occur.

### Network-based IDSs

Network-based IDSs reside on a discrete network segment and monitor the traffic on that segment. They usually consist of a network appliance with a network interface card (NIC) that is operating in promiscuous mode and is intercepting and analyzing the network packets in real time.

A network-based IDS involves looking at the packets on the network as they pass by some sensor. The sensor can see only the packets that happen to be carried on that particular network segment. Network traffic on other segments and traffic on other means of communication (such as phone lines) can't be monitored properly by a network-based IDS.

Packets are identified to be of interest if they match a signature. Three primary types of signatures are as follows:

- **String signatures**—String signatures look for a text string that indicates a possible attack.
- **Port signatures**—Port signatures watch for connection attempts to well-known, frequently attacked ports.
- **Header condition signatures**—Header signatures watch for dangerous or illogical combinations in packet headers.

A network-based IDS usually provides reliable, real-time information without consuming network or host resources. A network-based IDS is passive when acquiring data and review packets and headers. It can also detect DoS attacks. Furthermore, because this IDS is monitoring an attack in real time, it can respond to an attack in progress to limit damage.

One problem with a network-based IDS system is that it will not detect attacks against a host made by an intruder who is logged in at the host's terminal. If a network IDS along with some additional support mechanism determines that an attack is being mounted against a host, it is usually not capable of determining the type or effectiveness of the attack being launched.

### Host-based IDSs

Host-based IDSs use small programs (intelligent agents) that reside on a host computer. They monitor the operating system, detecting inappropriate activity, writing to log files, and triggering alarms. Host-based systems look for activity only on the host computer; they do not monitor the entire network segment.

A host-based IDS can review the system and event logs to detect an attack on the host and to determine whether the attack was successful. Detection capabilities of host-based IDSs are limited by the incompleteness of most host audit log capabilities.

In particular, host-based IDSs have the following characteristics:

- They monitor accesses and changes to critical system files and changes in user privileges.
- They detect trusted insider attacks better than a network-based IDS.
- They are relatively effective for detecting attacks from the outside.
- They can be configured to look at all network packets, connection attempts, or login attempts to the monitored machine, including dial-in attempts or other non–network-related communication ports.

An IDS detects an attack through one of two conceptual approaches: a signature-based IDS or a statistical anomaly-based IDS. These two mechanisms are also referred to as knowledge-based and behavior-based IDSs, respectively.

### Signature-based IDSs

In a signature-based IDS or knowledge-based IDS, signatures or attributes that characterize an attack are stored for reference. Then, when data about events is acquired from host audit logs or from network packet monitoring, this data is compared with the attack signature database. If there is a match, a response is initiated. This method is more common than using behavior-based IDSs. Signature-based IDSs are characterized by low false alarm rates (or positives) and, generally, are standardized and understandable by security personnel.

A weakness of the signature-based IDS approach is the failure to characterize slow attacks that extend over a long period of time. To identify these types of attacks, large amounts of information must be held for extended time periods. Another issue with signature-based IDSs is that only attack signatures that are stored in their databases are detected. Additional disadvantages of signature-based IDSs include the following:

- The IDS is resource-intensive. The knowledge database continually needs maintenance and updating with new vulnerabilities and environments to remain accurate.
- Because knowledge about attacks is very focused (dependent on the operating system, version, platform, and application), new, unique, or original attacks often go unnoticed.

### Statistical anomaly-based IDSs

Statistical anomaly- or behavior-based IDSs dynamically detect deviations from the learned patterns of "normal" user behavior and trigger an alarm when an intrusive activity occurs. Behavior-based IDSs learn normal or expected behavior of the system or the users and assume that an intrusion can be detected by observing deviations from this norm.

With this method, an IDS acquires data and defines a "normal" usage profile for the network or host that is being monitored. This characterization is accomplished by taking statistical samples of the system over a period of normal use. Typical characterization information used to establish a normal profile includes memory usage, CPU utilization, and network packet types. With this approach, new attacks can be detected because they produce abnormal system statistics. The advantages of a behavior-based IDS are as follows:

- The system can dynamically adapt to new, unique, or original vulnerabilities.
- A behavior-based IDS is not as dependent upon specific operating systems as a knowledge-based IDS.
- They help detect abuse-of-privileges types of attacks that do not actually involve exploiting any security vulnerability.

Some disadvantages of a statistical anomaly-based IDS are that it will not detect an attack that does not significantly change the system-operating characteristics, and it might falsely detect a non-attack event that caused a momentary anomaly in the system. Also, behavior-based IDSs are characterized by the following:

- High false alarm rates. High positives are the most common failure of behavior-based ID systems and can create data noise that can make the system unusable or difficult to use.
- Activity and behavior of the users of a networked system might not be static enough to effectively implement a behavior-based ID system.
- The network may experience an attack at the same time the intrusion detection system is learning the behavior.

## IDS issues

Many issues confront the effective use of an IDS. These include the following:

- Increases in the types of intruder goals, intruder abilities, tool sophistication, and diversity, as well as the use of more complex, subtle, and new attack scenarios
- The use of encrypted messages to transport malicious information
- The need to interoperate and correlate data across infrastructure environments with diverse technologies and policies
- Ever-increasing network traffic
- The lack of widely accepted IDS terminology and conceptual structures
- Volatility in the IDS marketplace, which makes the purchase and maintenance of IDSs difficult
- Risks inherent in taking inappropriate automated response actions
- Attacks on the IDSs themselves
- Unacceptably high levels of false positives and false negatives, making it difficult to determine true positives
- The lack of objective IDS evaluation and test information
- The fact that most computing infrastructures are not designed to operate securely
- Limited network traffic visibility resulting from switched local area networks (faster networks preclude effective real-time analysis of all traffic on large pipes)

An issue with the implementation of intrusion detection systems is the performance of the IDS when the network bandwidth begins to reach saturation levels. Obviously, there is a limit to the number of packets that a network intrusion detection sensor can accurately analyze in any given time period. The higher the network traffic level and the more complex the analysis, the more the IDS may experience high error rates, such as the premature discard of copied network packets.

Another issue with IDS is the proper implementation of IDS sensors in a switched environment. This issue arises from the basic differences between standard hubs and switches. Hubs exclude only the port the packet came in on and echo every packet to every port on the hub. Therefore, in networks employing only hubs, IDS sensors can be placed almost anywhere in the infrastructure.

However, when a packet comes into a switch, a temporary connection in the switch is first made to the destination port and then the packets are forwarded. This means more care must be exerted when placing IDS sensors in a switched environment to assure the sensor is able to see all the network traffic.

Some switches permit spanning port configuration, which configures the switch to behave like a hub only for a specific port. The switch can be configured to span the data from a specific port to the IDS port. Unfortunately, some switches cannot be guaranteed to pass all the traffic to the spanned port, and most switches allow only one port to be spanned at a time.

# Honeypots

A different approach to intrusion detection and response is the use of a *honeypot*. A honeypot is a monitored decoy mechanism that is used to entice a hacker away from valuable network resources and provide an early indication of an attack. It also provides for detailed examination of an attacker during and following a honeypot exploitation. A definition of a honeypot provided by the Honeynet Project is, "an information system resource whose value lies in unauthorized or illicit use of that resource." The Honeynet Project is a non-profit research organization of volunteer security professionals dedicated to advancing the state of the art in information system security.

## Purposes

Honeypots are employed primarily for either research or production purposes. In the research mode, a honeypot collects information on new and emerging threats, attack trends, motivations, and, essentially, characterizes the attacker community.

In the production category, honeypots are applied to preventing attacks, detecting attacks, and responding to attacks. The methods for accomplishing these tasks are summarized in the following sections.

### Preventing attacks

Honeypots are effective in preventing attacks by doing the following:

- Slowing or impeding scans initiated by worms or automated attacks by monitoring unused IP space and detecting scanning activity
- Consuming an attacker's energy through interaction with a honeypot while the attack is detected, analyzed, and handled
- Deterring an attack by a cracker who suspects a network employs honeypots and is concerned about getting caught

### Detecting attacks

Network security, no matter how conscientiously and effectively applied, cannot prevent all attacks all the time. Therefore, honeypots offer a means to detect an attack that is taking place or has occurred. Honeypots have the following advantages in detecting attacks:

- They can capture new and unknown attacks.
- They can capture polymorphic code.
- They can handle encrypted data.
- They reduce the amount of data that has to be analyzed by capturing only attack information.
- They are capable of operating with IPv6.

### Responding to attacks

Responding to an attack is challenging and not always effective. There are constraints that hamper the response process, such as not being able to take a critical application offline to analyze the attack and having to sort through myriads of IDS data.

Honeypots offer solutions to these situations in that a honeypot can be taken offline to analyze data and prepare a response because the honeypot is not an application used on the network. Secondly, as stated previously, honeypots generate small amounts of data that are the direct result of an attack, so the data can be reviewed more efficiently and a response implemented in a shorter time.

## Honeypot categories

In general, there are two types of honeypots: low-interaction honeypots and high-interaction honeypots. In this context, *interaction* refers to the level of activity provided by the honeypot to the attacker.

### Low-interaction honeypots

A low-interaction honeypot supports a limited emulation of an operating system and system services. Thus, a cracker's actions are limited by the low level of emulation that the honeypot provides. An obvious advantage of this type of honeypot is its lack of complexity and ease of deployment.

Because the honeypot has minimal capabilities, it also reduces the risk of an attacker compromising the honeypot to launch an attack on other network resources. Conversely, the simplicity of a low-interaction honeypot is one of its weaknesses, in that its limited interaction makes it easier for an attacker to determine that he or she is engaged with a honeypot. An example of a low-interaction honeypot is Honeyd, which is further discussed later in this chapter.

### High-interaction honeypot

High-interaction honeypots are more complex than low-interaction honeypots in that they provide for more complex interactions with attackers by incorporating actual operating systems and services. This type of honeypot can capture a large amount of information about an attacker and his or her behavior. But, as a consequence of its use of actual operating systems, a high-interaction honeypot is susceptible to compromise and being used as a base to launch an attack against other network components. Also, a high-interaction honeypot requires additional resources for deployment and maintenance.

## When to use a honeypot

As discussed earlier in this chapter, a honeypot is used in either a research or production mode. The research type of honeypot has high levels of interaction with an attacker and performs the following functions:

- Through a honeynet, it captures information on the behavior, intentions, characteristics, and identity of attackers. A *honeynet* is an architecture comprising a controlled network of high-interaction honeypots that are intended to be targets of attacks.
- It provides information on the activities of specific organizations and associated threats.
- It gathers data on attacks occurring globally (distributed research honeypots).

The production honeypot is designed to emulate an actual operating system and services on a computer system for the express purposes of identifying vulnerabilities and acquiring information that can be used to detect and apprehend attackers. Specifically, a production honeypot can do the following:

- Determine how an attacker gained access to the network.
- Monitor the attack in real time.
- Indicate that an attack is occurring.
- Isolate the attacker from the remainder of the network.
- Acquire information about the attacker.

## When not to use a honeypot

Deploying a honeypot requires careful consideration of the legal issues involved with monitoring, gathering information on, and prosecuting an individual based on the use of a honeypot. Some of the legal concerns are as follows:

- The liability of your organization if your honeypot is used to attack another organization's network
- Privacy rights of individuals being monitored on your network
- The possibility that an attacker apprehended through the use of a honeypot will claim entrapment
- Relevant laws of different jurisdictions outside of the United States

Uninformed deployment and use of honeypots without legal advice can lead to civil and criminal penalties for violating an individual's privacy rights through illegal monitoring of his or her activities. For example, evidence obtained by an agent of the U.S. government or a private individual acting at the behest of an agent of the U.S. government can be in violation of the Fourth Amendment of the U.S. Constitution through illegal monitoring activities. The Fourth Amendment states, "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." A private individual who is not acting as an agent of the U.S. government is not bound by the Fourth Amendment and can deploy a honeypot. However, that individual is still bound by state and federal privacy laws that might be applicable to monitoring of a person's communications.

Another legal consideration is the 1968 Federal Wiretap Act, which is sometimes referred to as Title III. This Act was expanded in 1986 and establishes procedures for court authorization of real-time surveillance of electronic communications. The types of activities for which wiretaps can be authorized were increased by the USA PATRIOT Act. Under certain circumstances, this Act provides privacy protections related to interception of communications that might be violated by use of a honeypot if precautions are not taken in advance.

An additional area of concern to an organization is if a honeypot is used to launch attacks on other networks or used as a repository for stolen information or illegal material.

Finally, an apprehended attacker might cry enticement/entrapment if he or she were caught as a result of a honeypot. A sympathetic judge might agree with that interpretation but, in most cases, the entrapment defense is weak in that the attacker has to illegally penetrate the security perimeter to get to the honeypot. Thus, the situation is more akin to enticement than entrapment, and enticement is not a legal violation.

## Current solutions

Two specific examples of honeypot applications are the Honeyd honeypot and the Honeynet Project.

### Honeyd

Honeyd is a low-interaction, open-source honeypot developed by Niels Provos. Honeyd was released under the GNU General Public License (GPL). At his Honeyd Web site, (`www.honeyd.org/`), Provos states, "Honeyd is a small daemon that runs both on UNIX-like and Windows platforms. It is used to create multiple virtual honeypots on a single machine. Entire networks can be simulated using Honeyd. Honeyd can be configured to run a range of services such as FTP, HTTP, or SMTP. Furthermore, a personality can be configured to simulate a certain operating system. Honeyd allows a single host to claim as many as 65,536 IP addresses." Honeyd operates in the following fashion:

- It monitors connection attempts to unused IP space.
- It checks connections to ports such as TCP and UDP.
- It intercepts connections and pretends to be a system service or OS.
- It logs an attacker's interaction with the service or OS emulated by the honeypot.
- It captures information such as passwords, IDs, command instructions, and attack targets.

### Honeynet Project

The Honeynet Project was established in 1999 as a network security research activity using honeynets and honeypots to explore and discover a cracker's behaviors, motives, tools, and approaches, and to apply the lessons acquired from this effort. During the first two years, the Honeynet research group was limited to 30 members. One of the members, Dr. Eric Cole, is an author of this book. In 2002, the Honeynet Research Alliance was formed to include a larger number of contributors, including researchers from India, Mexico, Greece, Brazil, and Ireland. The team members volunteer their time and contribute hardware and software to the project.

The project evolved in the following four phases:

- **Phase I**—This phase was initiated in 1999 and served as a proof-of-concept effort to deploy and test first-generation (GenI) honeynet approaches.
- **Phase II**—Begun in 2002, the intent of this phase was to develop GenII honeynets with advanced monitoring techniques and improved methods to control attackers' activities when interacting with the honeynet. Additional tasks included incorporating the ability to handle encrypted information and making honeynets easier to deploy.
- **Phase III**—The third phase began in 2003 and transported GenII honeynet technologies to bootable CD-ROM for ease of distribution and deployment.
- **Phase IV**—Started in 2004, activity is focused on developing user interfaces and a centralized data collection system to correlate information from distributed honeynets.

# Incident Handling

One of the key drivers of incident handling is the organization's information system security policy. This security policy defines the rules that regulate how an organization manages and protects computing resources to achieve security objectives. Well-documented, communicated, and properly enforced intrusion detection policies and processes prepare the organization to respond to intrusions in a timely and controlled manner.

A networked system security policy should require that designated system and network administrators and response team members be trained in the use of intrusion response tools and environments. This training should include participation in response practice drills or simulations using the tools and environments.

Also, the security policy should require that the inventory of all applications software, operating systems, supporting tools, and hardware be kept up to date. It should mandate rapid accessibility to backups in an emergency, even if these are stored at a remote site. This requirement may include defining procedures that give specific managers the responsibility to authorize such access.

Often, the policy will state that staff members dealing with an intrusion may require access to restricted systems and data. This specification usually includes criteria for access, establishment of authority for access, and means for tracking and documenting access.

The critical issues associated with incident handling are as follows:

- Protecting the assets that could be compromised
- Protecting resources that could be utilized more profitably if an incident did not require their services
- Complying with (government or other) regulations
- Preventing the use of your systems in attacks against other systems (which could cause you to incur legal liability)
- Minimizing the potential for negative exposure

A number of organizations have developed and published best practices for incident handling. The recommendations of two of these organizations, the Carnegie Mellon University CERT Coordination Center (CERT/CC) and the Internet Engineering Task Force (IETF), are presented in the following sections.

## CERT/CC practices

The CERT/CC recommended practices for handling incidents are as follows:

1. PREPAREEstablish policies and procedures for responding to intrusions.Prepare to respond to intrusions.
2. HANDLEAnalyze all available information to characterize an intrusion.Communicate with all parties that need to be made aware of an intrusion and its progress.Collect and protect information associated with an intrusion.Apply short-term solutions to contain an intrusion.Eliminate all means of intruder access.Return systems to normal operation.
3. FOLLOW UPIdentify security lessons learned.Implement security lessons learned.

The following sections expand on these recommended actions.

### Establishing response policies and procedures

Response procedures describe how the response policies will be implemented throughout your organization (for example, whom to notify, at what point in the response procedure, and with what types of information). From these procedures, all concerned parties are able to determine what operational steps they need to take to comply with your policies and, thereby, respond in a manner that upholds the security objectives for your organization's information and networked systems.

This practice describes a subset of the topics your intrusion response policies and procedures should address. Additional policy and procedure information is contained in the other practices of this module where it is most applicable. This language needs to be tailored to reflect the specific business objectives and security requirements of your organization and its computing environment. The details of procedures used to address specific types of intrusions may vary.

Establish guidelines and rules at the management level for responding to intrusions and include these in your organization's networked systems security policy, as follows:

- Document your configuration redundancy policy.
- Document a response procedure that implements your intrusion response policies.
- Conduct a legal review of your policies and procedures.
- Train designated staff about your response policies and procedures.

### Preparing to respond to intrusions

Preparation includes selecting, installing, and becoming familiar with tools that will assist you in the response process and will help you collect and maintain data related to an intrusion. You need to perform the following preparatory steps well in advance of an intrusion:

- Build an archive of boot disks and distribution media for all applications and all operating systems and versions.
- Build an archive of security-related patches for all applications and all operating systems and versions.
- Identify and install tools that support the reinstallation of systems, applications, and patches.
- Ensure that your backup procedures are adequate to recover from any damage.
- Build an archive of test results that describe the expected state of your systems.
- Ensure that high-capacity, removable, and write-protected media and supporting equipment are available to make and restore system backups.
- Build and maintain a database of contact information.
- Set up secure communication mechanisms.
- Identify and install tools to access directories and other sources of contact information.
- Build a resource kit of tools and hardware devices.
- Ensure that test systems and networks are properly configured and available.

### Analyzing all available information

After you have been alerted by your intrusion detection mechanisms or another trusted site that an intrusion has been detected, you need to determine to what extent your systems and data have been compromised and you need to respond. Information, as collected and interpreted through analysis, is key to your decisions and actions throughout the response process.

Your goal is to determine the following:

- What attacks were used to gain access
- What systems and data an intruder did access
- What an intruder did after obtaining access
- What an intruder is currently doing when an intrusion has not been contained or eliminated

The analysis process entails the following:

- Back up the compromised systems.
- Isolate the compromised systems.
- Search on other systems for signs of intrusion.
- Examine logs generated by firewalls, network monitors, and routers.
- Identify the attacks used to gain access to your systems.
- Identify what an intruder did while accessing your systems.

### Communicating with all parties

Those with key roles in responding to an intrusion need to be notified and kept informed at the appropriate times to fulfill their responsibilities. You need to notify immediately the responsible mid-level and senior managers, your local computer security incident response team (CSIRT) if one exists, your public relations staff, and the affected system administrators (if they are not already involved) based on your organization's information dissemination policy. Executing your information dissemination procedures may include contacting users affected by an intrusion, security personnel, law enforcement agencies, vendors, and other CSIRTs external to your organization. You should do the following:

- Execute your information dissemination procedures taking the specifics of an intrusion into account.
- Use secure communication mechanisms.
- Inform upstream and downstream sites of attacks and intrusions.
- Maintain a detailed contact log.
- Maintain current contact information for your systems and sites.

### Collecting and protecting information

All information about the compromised system or systems and causes of an intrusion needs to be captured and securely stored. This may include system and network log files, network message traffic, user files, results produced by intrusion detection tools, analysis results, system administrator console logs and notes, and backup tapes that capture the before-intrusion and after-intrusion states of the affected system. All information must be carefully collected, labeled, catalogued, and securely stored at each stage of intrusion analysis.

- Collect all information related to an intrusion.
- Collect and preserve evidence securely.
- Preserve the chain of custody for all evidence.
- Contact law enforcement immediately if you decide to pursue and prosecute an intruder.

### Applying short-term containment solutions

Containment consists of short-term, tactical actions whose purpose is to stop an intruder's access to compromised systems, limit the extent of an intrusion, and prevent an intruder from causing further damage. It may include the following steps:

- Temporarily shut down the compromised system.
- Disconnect the compromised system from a network.
- Disable access to compromised file systems that are shared with other computers.
- Disable system services, if possible.
- Change passwords or disable accounts.
- Monitor system and network activities.
- Verify that redundant systems and data have not been compromised.

### Eliminating all means of intruder access

Complete eradication of the root cause(s) of an intrusion is a long-term goal that can only be achieved by implementing an ongoing security improvement process. In response to a specific intrusion, you need to ensure that the affected systems are protected against the same or similar types of access and attacks in the future, after an intrusion is contained and systems are returned to normal operation. That may involve the following steps:

- Change all passwords on all systems to which the attacker may have had access.
- Reinstall compromised systems if your preparation was insufficient.
- Remove any means for intruder access, including changes made by an intruder.
- Restore executable programs (including application services) and binary files from original distribution media.
- Review system configurations.
- Determine if you have uncorrected system and network vulnerabilities and correct them.
- Improve protection mechanisms to limit the exposure of networks and systems.
- Improve detection mechanisms to enable better reporting of attacks.

### Returning systems to normal operation

Restoring and returning a compromised system to normal operation permits your staff to have access to that system again. This is best accomplished after all means of intruder access are eliminated. Doing so prevents the same or similar types of intrusions from occurring or, at the very least, ensures timely detection and notification by your updated intrusion detection mechanisms.

- Determine the requirements and timeframe for returning the system to normal operations.
- Enable system and application services.
- Restore user data from trusted backup media.
- Re-establish the availability of previously disconnected file systems.
- Reconnect the restored system to the network.
- Validate the restored system.
- Watch for additional scans or probes that may signal the return of an intruder.

### Identifying and implementing security lessons learned

It is important to learn from the successful and unsuccessful actions taken in response to an intrusion. Capturing and disseminating what worked well and what did not will help reduce the likelihood of similar intrusions and will improve the security of your operation. This can be accomplished by performing a post-mortem review with all involved parties and then communicating the results of the review, as follows:

- If further notification is required (per policies and procedure), execute the notification.
- Manage ongoing press aspects of an intrusion, if any.
- Hold a post-mortem analysis and review meeting with all involved parties.
- Revise security plans, policies, procedures, and user and administrator training to prevent intrusion recurrence.
- Determine whether or not to perform a new risk analysis based on the severity and impact of an intrusion.
- Take a new inventory of your system and network assets.
- Participate in investigation and prosecution, if applicable.

## Internet Engineering Task Force guidance

The Internet Engineering Task Force (IETF) RFC 2196, in the *Site Security Handbook*, provides additional guidance on handling incidents. The handbook recommends the following approach to the handling of incidents:

1. Preparing and planning (what are the goals and objectives in handling an incident)
2. Notification (who should be contacted in the case of an incident)Local managers and personnelLaw enforcement and investigative agenciesComputer security incidents–handling teamsAffected and involved sitesInternal communicationsPublic relations and press releases
3. Identifying an incident (is it an incident and how serious is it)
4. Handling (what should be done when an incident occurs)Notification (who should be notified about the incident)Protecting evidence and activity logs (what records should be kept from before, during, and after the incident)Containment (how can the damage be limited)Eradication (how to eliminate the reasons for the incident)Recovery (how to reestablish service and systems)Follow up (what actions should be taken after the incident)
5. Aftermath (what are the implications of past incidents)
6. Administrative response to incidents

## Layered security and IDS

Computer security is most effective when multiple layers of security controls are used within an organization, and IDSs are best utilized when implemented using a *layered security* approach. This method specifies that multiple steps be taken to secure the data, thereby increasing the workload and time required for an intruder to penetrate the network. While a firewall is an excellent perimeter security device, it is only one element of an effective security strategy. The more elements, or layers, of security that can be added to protect the data, the more secure the infrastructure will remain.

Elements of an effective layered security approach include the following:

- Security policies, procedures, standards, and guidelines, including high-level security policy
- Perimeter security, such as routers, firewalls, and other edge devices
- Hardware or software host security products
- Auditing, monitoring, intrusion detection, and response

Each of these layers may be implemented independently of the others, yet they are interdependent when functioning. An IDS that generates alerts to unauthorized access attempts or port scanning is useless without a response plan to react to the problem. Because each layer provides elements of protection, the defeat of any one layer should not lead to a complete failure of protection.

## Computer Security and Incident Response Teams

Numerous Computer Security and Incident Response Teams (CSIRTs) have been organized to address the issues of coordination and communication in response to security incidents. Coordination includes the detection, prevention, and handling of security incidents; understanding the current state of security; and identifying trends in activity within their constituency. Because the Internet is a cooperative network, authority and responsibility for security is distributed across logical domains.

[Table 23-1](ch23.html#csirts) shows some of the existing response teams in the government, military, university, and corporate sectors.

### CERT/CC

As previously referenced, the CERT/CC is a unit of the Carnegie Mellon University Software Engineering Institute (SEI). SEI is a federally funded research and development center and CERT's mission is to alert the Internet community to vulnerabilities and attacks, and to conduct research and training in the areas of computer security, including incident response.

**Table 23.1. CSIRTS**

| Response Team | Constituency |
| --- | --- |
| AUSCERT | Australia (sites in .au domain) |
| CERT © Coordination Center (CERT/CC) | The Internet |
| Cisco-PSIRT | Commercial Cisco customers |
| DFN-CERT | German sites |
| DOD-CERT | Department of Defense systems |
| Global Integrity (REACT) | Commercial and government customers |
| OSU-IRT | Ohio State University |
| OxCERT Oxford University IT Security Team | Oxford University |
| FedCIRC | U.S. Government |
| FIRST | INFOSEC Community at large |

### FedCIRC

The Federal Computer Incident Response Center (FedCIRC) is an organization that "establishes a collaborative partnership of computer incident response, security, and law enforcement professionals who work together to handle computer security incidents and to provide both proactive and reactive security services for the U.S. Federal government." The FedCIRC charter states: "FedCIRC provides assistance and guidance in incident response and provides a centralized approach to incident handling across agency boundaries." FedCIRC's mission is to do the following:

- Provide civil agencies with technical information, tools, methods, assistance, and guidance.
- Be proactive and provide liaison activities and analytical support.
- Encourage the development of quality products and services through collaborative relationships with federal civil agencies, the Department of Defense, academia, and private industry.
- Promote the highest security profile for government information technology (IT) resources.
- Promote incident response and handling procedural awareness with the federal government.

### FIRST

The Forum of Incident Response and Security Teams (FIRST) brings together a variety of computer security incident response teams from government, commercial, and academic organizations. FIRST aims to foster cooperation and coordination in incident prevention, to prompt rapid reaction to incidents, and to promote information sharing among members and the community at large.

FIRST's goals are as follows:

- To foster cooperation among information technology constituents in the effective prevention, detection, and recovery from computer security incidents
- To provide a means for the communication of alert and advisory information on potential threats and emerging incident situations
- To facilitate the actions and activities of the FIRST members including research and operational activities
- To facilitate the sharing of security-related information, tools, and techniques

## Security incident notification process

All potential, suspected, or known information security incidents should be reported to a CSIRT. The CSIRT will then assign personnel who will assemble all needed resources to handle the reported incident. The incident coordinator will make decisions as to the interpretation of policy, standards, and procedures when applied to the incident.

Law enforcement and investigative agencies will be notified, as needed and required, by the CSIRT. In the event of an incident that has legal consequences, it is important to establish contact with investigative agencies such as the FBI as soon as possible. Local law enforcement should also be informed as appropriate. Legal counsel should be notified of an incident as soon as it is reported. At a minimum, legal counsel should be involved to protect the legal and financial interests of your company.

The security incident notification process should provide some escalation mechanisms. To define such a mechanism, the CSIRT should create an internal classification scheme for incidents. Associated with each level of incident will be the appropriate procedures. The following list is an example of various levels of incidents:

- **Priority One**—Protect human life and people's safety; human life always has precedence over all other considerations.
- **Priority Two**—Protect restricted and internal data. Prevent exploitation of restricted systems, networks, or sites. Inform affected restricted sensitive systems, networks, or sites about penetrations that have already occurred while abiding by any applicable government regulations.
- **Priority Three**—Protect other data, including managerial, because loss of data is costly in terms of resources. Prevent exploitations of other systems, networks or sites and inform already affected systems, networks, or sites about successful penetrations.
- **Priority Four**—Prevent damage to systems (for example, loss or alteration of system files, damage to disk drives, and so on). Damage to systems can result in costly downtime and recovery.
- **Priority Five**—Minimize disruption of computing resources (including processes). It is better in many cases to shut a system down or disconnect from a network than to risk damage to data or systems. Each data and system owner must evaluate the trade-off between shutting down and disconnecting, and staying up. This decision must be made prior to an incident occurring. There may be service agreements in place that require keeping the systems up even in light of further damage occurring. However, the damage and scope of an incident may be so extensive that service agreements have to be overridden.

## Automated notice and recovery mechanisms

Automated notice and recovery mechanisms can provide automated capabilities in one or more of the following areas: intruder prevention, intruder detection, and damage assessment. A number of automated intruder responses have been implemented as part of intrusion detection systems. Some responses may be active, such as terminating processes, closing connections, and disabling accounts. Other responses are passive, such as sending an e-mail to the system administrator.

Damage assessment is normally performed after an attack. A number of vulnerability scanning tools, such as Tiger, may be used to perform damage assessment. Other tools, such as Tripwire, were specifically developed to aid in damage assessment. In addition, host-based IDSs, which perform real-time activity monitoring, can maintain a suspicion level for each user as well as an overall suspicion level of the monitored host.

Although not absolutely required, the ability of host-based IDSs to cooperate and share information to track users as they connect to other monitored hosts is also important.

Automated notice and recovery is appealing because it does not require continuous human oversight, it can act more rapidly than humans, and it can be tailored to, and will consistently follow, specified policies. Common automated response capabilities include session logging, session termination, posting events on the event console, and alerting personnel through e-mail, paging, and other means. The architecture to collect incident information consists of four crucial components: a sensor, collector, backing store, and an analysis engine.

However, most IDSs require a human operator to be in the loop. Given the current maturity of IDS technology, the dangers of automated response are significant, and outweigh the preceding advantages. With the frequency of false positives that exist in the current generation of IDSs, the potential for inappropriate response to misdiagnosis is too high. In addition, automated response could be exploited by a perpetrator whose aim is to induce a denial-of-service attack by spoofing an attack from a legitimate user. Also, many intrusion detection tools provide some form of automated intruder response, but few security tools perform any automated recovery.

# Summary

This chapter explored intrusion detection and response methodologies to counter the harmful activities of crackers. As an example of novel ideas in intrusion detection, the chapter provided an overview of honeypots and honeynets. These entities act as target decoys employed to ensnare malicious intruders and gather information that will thwart their efforts, characterize their behaviors, and lead to their apprehension.

The chapter concluded with best practices to handle and respond to incidents to counter aggressions against valuable computing and network resources.
