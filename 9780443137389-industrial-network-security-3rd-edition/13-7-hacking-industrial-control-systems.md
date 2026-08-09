# 7: Hacking Industrial Control Systems

## Abstract

An in-depth discussion on how an industrial network might be attacked, including possible target systems, and the potential consequences should those targets be compromised. Learn how a hacker thinks, how malware works, and what to do if your industrial network becomes infected.

### Keywords

Blackenergy; Cyber-physical; Cyberattack; Denial-of-service; Dragonfly; HID; Industrial networks; Industroyer; Keylogging; Pipedream; Replay; Rogue access device; Skywiper; Stuxnet; TRISISInformation in this chapter• Motives and Consequences• Common Industrial Targets• The Evolution of the Industrial Cyber Attack• Common Attack Methods• Examples of Advanced Industrial Cyber Threats• Attack Trends• Dealing with an Infection
## Motives and consequences

Industrial networks are responsible for continuous and batch processing and other manufacturing operations of almost every scale, and as a result, the successful penetration of a control system network can be used to directly impact those operations. Consequences vary and can range from relatively benign disruptions, such as the interruption of the operation (taking a facility offline) and the alteration of an operational process (changing the formula of a chemical process or recipe), to deliberate acts of sabotage that are intended to cause harm. Manipulating the feedback loop of certain processes could, for example, cause pressure within a boiler to build beyond safe operating parameters. Cyber sabotage, on the other hand, can result in environmental damage (oil spill, fire, toxic release, etc.), injury or loss of life, the loss of critical services (blackouts, disruption in fuel supplies, unavailability of vaccines, etc.), or potentially catastrophic explosions.

### Consequences of a successful cyberincident

A successful cyberattack on an ICS can have many undesirable consequences, including:

1. • Delay, block, or alter the intended process, that is, alter the amount of energy produced at an electric generation facility.
2. • Delay, block, or alter information related to a process, thereby preventing a bulk energy provider from obtaining production metrics that are used in energy trading or other business operations.
3. • Unauthorized changes to instructions or alarm thresholds that could damage, disable or shutdown mechanical equipment, such as generators or substations.
4. 
5. • Inaccurate information sent to operators could either be used to disguise unauthorized changes (see Stuxnet later in this chapter) or cause the operator to initiate inappropriate actions.

The end result could be anything from financial loss to physical safety liabilities, with impacts extending beyond the plant, to the local community, state, and even federal level (see [Figure 7.1](#f0010)). Companies can incur penalties for regulatory noncompliance, or they may suffer financial impact from lost production hours due to misinformation or denial of service. An incident can impact the ICS in almost any way, from taking a facility offline, disabling or altering safeguards, to life-threatening incidents within the plant—up to and including the release or theft of hazardous materials or direct threats to national security.[1](#fn1)

The possible damages resulting from a cyberincident vary depending upon the type of incident, as shown in [Table 7.1](#t0010).

### Cybersecurity and safety

Most industrial networks employ automated safety systems to avoid catastrophic failures. However, many of these safety controls employ the same messaging and control protocols used by the industrial control network's operational processes, and in some cases, such as certain fieldbus implementations, the safety systems are supported directly within the same communications protocols as the operational controls on the same physical media (see [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml), “Industrial Network Protocols,” for details and security concerns of industrial control protocols).

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000014/main.assets/f07-01-9780443137372.jpg)

*[Figure 7.1](#Bf0010)  Consequences of a compromised industrial control system.*

[Table 7.1](#Bt0010)

| Incident type | Potential impact |
| --- | --- |
| Change in a system, operating system, or application configuration | Command and control channels introduced into otherwise secure systems. Suppression of alarms and reports to hide malicious activity. Alteration of expected behavior to produce unwanted and unpredictable results |
| Change in programmable logic in PLCs, RTUs, or other controllers | Damage to equipment and/or facilities. Malfunction of the process (shutdown). Disabling control over a process |
| Misinformation reported to operators | Inappropriate actions taken in response to misinformation that could result in a change to operational parameters. Hiding or obfuscating malicious activity, including the incident itself or injected code |
| Tampering with safety systems or other controls | Preventing expected operations, fail safes, and other safeguards with potentially damaging consequences |
| Malicious software (malware) infection | Initiation of additional incident scenarios. Production impact resulting from assets taken offline for forensic analysis, cleaning, and/or replacement. Assets susceptible to further attacks, information theft, alteration, or infection |
| Information theft | Leakage of sensitive information such as a recipe or chemical formula |
| Information alteration | Alteration of sensitive information such as a recipe or chemical formula in order to sabotage or otherwise adversely affect the manufactured product |

NoteCritical, risk-based safety operations implemented within the ICS typically follow separate standards regarding the use of programmable logic solvers, field devices, and communication protocols (e.g., IEC 61508/61511, NFPA 85, ISA 84) and how these safety instrumented systems (SIS) can be interfaced and integrated with other ICS components. It is important to realize that not all “safety” controls and interlocks are implemented against these standards, and that it is possible for these systems to share infrastructure (including the controller platform itself) with other ICS systems and components. Regulatory requirements typically require standards-based SIS implementations for safety functions that represent significant unmitigated risk in terms of human health, safety, and environmental impact, and not on production uptime or reliability.Although safety systems are extremely important, there is the perception that they have been used to downplay the need for heightened security of industrial networks. Research has shown that real consequences can occur in modeled systems. Simulations performed by the Sandia National Laboratories showed that simple man-in-the-middle (MitM) attacks could be used to change values in a control system and that a modest-scale attack on a larger bulk electric system using targeted malware (in this scenario, targeting specific ICS front-end processors) was able to cause significant loss of generation.[2](#fn2)

The European research team VIKING (Vital Infrastructure, Networks, Information and Control Systems Management) is currently investigating threats of a different sort. The Automatic Generation Control (AGC) system within the electric power network is responsible for adjusting the output of multiple generators on the grid in response to changes in demand. It operates autonomously from human interaction—that is, output actions are based entirely on processing of input states with the logic of the AGC. Rather than breaching a control system through the manipulation of an HMI, VIKING's research attempts to investigate whether the manipulation of input data could alter the normal control loop functions, ultimately causing a disturbance.[3](#fn3)

TipThink of security as separate from safety when establishing a cybersecurity plan. Do not assume that security leads to safety or that safety leads to security. If an automated safety control is compromised by a cyberattack (or otherwise disrupted), the necessity of having a strong digital defense against the manipulation of operations becomes even more important. Likewise, a successful safety policy should not rely on the security of the networks used. Both systems will be inherently more reliable by planning for safety and security controls that operate independently of one another. At the same time, safety systems are built around strong process assessments, to protect against identified physical risk conditions. These risk conditions may be the ultimate goal of a cyberattack, and so safety and security also need to work together within an organization to ensure that cyberdefenses are properly implemented.With attack frameworks capable of manipulating SISs (see “TRISIS”, and “Incontroller” below), it is more important than ever to consider safety controls from a cybersecurity perspective and to consider cybersecurity controls from a safety perspective. This concept is discussed in more detail in [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessments: Thinking of Cybersecurity in terms of Safety.”

## Common industrial targets

Industrial control systems may be comprised of similar components; however, each system is unique in terms of the exact composition, quantity, and criticality of these components. There are, however, some common targets within industrial networks despite these system differences. These include network services, such as active directory (directory services) and identity and access management (IAM) servers, which may be shared between business and industrial zones (though the best practice is to not share these services!); engineering workstations, which can be used to exfiltrate, alter, or overwrite process logic; operator consoles, which can be used to trick human operators into performing unintended tasks; and of course the industrial applications (SCADA server, historian, asset management, etc.), and protocols (Modbus, DNP3, EtherNet/IPI, etc.)  themselves, which can be used to alter, manipulate, blind, or destroy almost any aspect of an ICS. [Table 7.2](#t0015) highlights some of the common targets, how they are likely to be attacked, and what the consequences of such attacks might be.

## The evolution of the industrial cyberattack

There was a time when cyberattacks were simpler. Malware was often self-contained, and there was a direct correlation between exposure to malware and a subsequent infection. Cybersecurity threats have evolved considerably in the past decade, and a cybersecurity threat is better thought of as a campaign: a series of tactics and techniques that might leverage multiple, disparate, purpose-built malwares used at various stages of a larger coordinated attack effort. In addition, most cyber-physical attacks targeting industrial control require two distinct phases, each of which has its own lifecycle: the first phase involves the various steps of a cyberattack required to reach industrial control systems; the second involves the various steps of a subsequent cyberattack to target those industrial control systems.

This is discussed in depth in [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), “Attack and Defense Lifecycles” but is mentioned here for context. In addition, some of the topics described below are components that could be used as part of a larger campaign (e.g., “Common Attack Methods”), while some refer to the larger campaigns that could be comprised of those methods (i.e., “Weaponized Industrial Cyber Threats”).

Finally, the examples discussed below are obviously not a comprehensive list. There are billions of distinct malwares that have been discovered, and there are 14 categorized “tactics” as defined by MITRE, and hundreds of techniques utilized to achieve them.[4](#fn4) The examples discussed here are intended to understand attacks that are most relevant to industrial network security, but they are not all inclusive. The threat landscape changes continuously; try to imagine the unimaginable and to expect the unexpected!

### Common attack methods

There are many methods of attacking a target, once a target has been identified. MitM, denial-of-service (DoS), replay attacks, and countless more methods all remain very effective in industrial networks. The primary reason for this is a combination of insecure communication protocols, little device-to-device authentication, and delicate communication stacks in embedded devices. If an industrial network can be penetrated and malware deposited (on disk or in memory) anywhere on the network, tools such as Metasploit Meterpreter shell can be used to provide remote access to target systems, install keyloggers or keystroke injectors, enable local audio/video resources, manipulate control bits within industrial protocols, plus many other covert capabilities.

In some cases, the information that is available can be used as reconnaissance for further cyberattack capability. In many cases, systems can be attacked directly using disclosed exploits, with only basic system knowledge required. If an attack is successful,  persistence can often be established, enabling an attacker to gather intelligence over time. In systems that make up a nexus between other systems (such as a control room SCADA server), a persistent presence can also be used to launch secondary attacks against other portions of the industrial network—such as basic control and process control zones that reside within the supervisory zone.

[Table 7.2](#Bt0015)

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Access control system | - Identification cards - Closed-circuit television (CCTV) - Building management network - Software vendor support portal | - Exploitation of unpatched application (building management system) - RFID spoofing - Network access through unprotected access points - Network pivoting through unregulated network boundaries | - Unauthorized physical access - Lack of (video) detection capabilities - Unauthorized access to additional ICS assets (pivoting) |
| Analyzers/analyzer management system | - Subcontractor laptop - Maintenance remote access - Plant (analyzer) network | - Exploitation of unpatched application - Network access via insecure access points (analyzer shelters) - Remote access VPN via stolen or compromised subcontractor laptop - Remote access VPN via compromise of maintenance vendor site - Insecure implementation of OPC (communication protocol) | - Product quality—spoilage, loss of production, loss of revenue - Reputation—product recall, product reliability |
| Application servers | - Remote user access (interactive sessions) - Business application integration communication channel - Plant network - Software vendor support portal | - Exploitation of unpatched application - Installation of malware via unvalidated vendor software - Remote access via “interactive” accounts - Database injection - Insecure implementation of OPC (communication protocols) | - Plant upset/shutdown - Credential leakage (control) - Sensitive/confidential information leakage - Unauthorized access to additional ICS assets (pivoting) |
| Asset management system | - Plant maintenance software/ERP - Database integration functionality - Mobile devices used for device configuration - Wireless device network - Software vendor support portal | - Exploitation of unpatched application - Installation of malware via unvalidated vendor software - Remote access via “interactive” accounts - Database injection - Installation of malware via mobile devices - Access via insecure wireless infrastructure | - Calibration errors—product quality - Credential leakage (business) - Credential leakage (control) - Unauthorized access to additional business assets like plant maintenance/ERP (pivoting) - Unauthorized access to additional ICS assets (pivoting) |
| Condition monitoring system | - Subcontractor laptop - Maintenance remote access - Plant (maintenance) network - Software vendor support portal | - Exploitation of unpatched application - Installation of malware via unvalidated vendor software - Network access via unsecure access points (compressor/pump house) - Remote access VPN via stolen or compromised subcontractor laptop - Remote access VPN via compromise of maintenance vendor site - Remote access via “interactive” accounts - Database injection - Insecure implementation of OPC (communication protocols) | - Equipment damage/sabotage - Plant upset/shutdown - Unauthorized access to additional ICS assets (pivoting) |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Controller (PLC) | - Engineering workstation - Operator HMI - Standalone engineering tools - Rogue device in control zone - USB/removable media - Controller network - Controller (device) network | - Engineer/technician misuse - Network exploitation of industrial protocol—known vulnerability - Network exploitation of industrial protocol—known functionality - Network replay attack - Network DoS via communication buffer overload - Direct code/malware injection via USB - Direct access to device via rogue network (local/remote) PC with appropriate tools/software | - Manipulation of controlled process(es) - Controller fault condition - Manipulation/masking of input/output data to/from controller - Plant upset/shutdown - Command-and-control |
| Data historian | - Business network client - ERP data integration communication channel - Database integration communication channel - Remote user access (interactive session) - Plant network - Software vendor support portal | - Exploitation of unpatched application - Installation of malware via unvalidated vendor software - Remote access via “interactive” accounts - Database injection - Insecure implementation of required communication protocols - Exploitation of unnecessary/excessive openings on perimeter defense (firewall) due to insecure communication infrastructure between applications | - Manipulation of process/batch records - Credential leakage (business) - Credential leakage (control) - Unauthorized access to additional business assets like MES, ERP (pivoting) - Unauthorized access to additional ICS assets (pivoting) |
| Directory services | - Replication services - Print spooler services - File sharing services - Authentication services - Plant network - Software vendor support portal | - Exploitation of unpatched application(s) - Installation of malware via unvalidated vendor software - DNS spoofing - NTP reflection attack - Exploitation of unnecessary/excessive openings on perimeter defense (firewall) due to replication requirements between servers - Installation of malware on file shares | - Communication disruptions via DNS - Authentication disruptions via NTP - Authentication disruptions via LDAP/Kerberos - Credential leakage - Information leakage - file shares - Malware distribution - Unauthorized access to ALL domain-connected ICS assets (pivoting) - Unauthorized access to business assets (pivoting) |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Engineering workstations | - Engineering tools and applications - Nonengineering client applications - USB/Removable media - Elevated privileges (engineer/administrator) - Control network - Software vendor support portal | - Exploitation of unpatched applications - Installation of malware via unvalidated vendor software - Installation of malware via removable media - Installation of malware via keyboard - Exploitation of trusted connections across security perimeters - Authorization to ICS applications without sufficient access control mechanisms | - Plant upset/shutdown - Delay plant startup - Mechanical damage/sabotage - Unauthorized manipulation of operator graphics—inappropriate response to process action - Unauthorized modification of ICS database(s) - Unauthorized modification of critical status/alarms - Unauthorized distribution of faulty firmware - Unauthorized startup/shutdown of ICS devices - Process/plant information leakage - ICS design/application credential leakage - Unauthorized modification of ICS access control mechanisms - Unauthorized access to most ICS assets (pivoting/own) - Unauthorized access to business assets (pivoting) |
| Environmental controls | - HVAC control - HVAC (building management) network - Software vendor support portal | - Exploitation of unpatched application (building management system) - Installation of malware via unvalidated vendor software - Network access through unprotected access points - Network pivoting through unregulated network boundaries | - Disruption of cooling/heating - Equipment failure/shutdown |
| Fire detection and suppression system | - Fire alarm/evaluation - Fire suppressant system - Building management network - Software vendor support portal | - Exploitation of unpatched application (building management system) - Installation of malware via unvalidated vendor software - Network access through unprotected access points - Network pivoting through unregulated network boundaries | - Unauthorized release of suppressant - Equipment failure/shutdown |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Master and/or slave devices | - Unauthorized/unvalidated firmware - Weak communication problems - Insufficient authentication for “write” operations - Control network - Device network | - Distribution of malicious firmware - Exploitation of vulnerable industrial protocols via rogue PC on network (local/remote) - Exploitation of vulnerable industrial protocols via compromised PC on network (local) - Exploitation of industrial protocol functionality via rogue PC on network (local/remote) - Exploitation of industrial protocol functionality via compromised PC on network (local) - Communication buffer overflow via rogue PC on network (local/remote) - Communication buffer overflow via compromised PC on network (local) | - Plant upset/shutdown - Delay plant start - Mechanical damage/sabotage - Inappropriate response to control action - Suppression of critical status/alarms |
| Operator workstation (HMI) | - Operational applications (HMI) - Non-SCADA client applications - USB/Removable media - Elevated privileges (administrator) - Control network - Software vendor support portal | - Exploitation of unpatched applications - Installation of malware via unvalidated vendor software - Installation of malware via removable media - Installation of malware via keyboard - Authorization to ICS HMI functions without sufficient access control mechanisms | - Plant upset/shutdown - Suppression of critical status/alarms - Product quality - Plant/process efficiency - Credential leakage (control) - Plant/operational information leakage - Unauthorized access to ICS assets (pivoting) - Unauthorized access to ICS assets (communication protocols) |
| Patch management servers | - Software patches/hotfixes - Patch management software - Vendor software support portal - Business network - Plant network - Software vendor support portal | - Insufficient checking of patch “health” before deployment - Alternation of automatic deployment schedule - Installation of malicious software via trusted (supplier) media - Installation of malware via unvalidated vendor software | - Malware distribution server - Unauthorized modification of patch schedule - Credential leakage - Unauthorized access to ICS assets (pivoting) |
| Perimeter protection (firewall/IPS) | - Trusted connections (business-to-control) - Local user account database - Signature/rule updates | - Untested/unverified rules - Exploitation of unnecessary/excessive openings on perimeter defense (firewall) - Insecure office and industrial protocols allowed to cross security perimeter - Reuse of credentials across boundary | - Unauthorized access to business network - Unauthorized access to DMZ network - Unauthorized access to control network - Local credential leakage - Unauthorized modification of rulesets/signatures - Communication disruption across perimeter/boundary |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| SCADA servers | - Non-SCADA client applications - Application integration communication channels - Data historian - Engineering workstation - Control network - Software vendor support portal | - Exploitation of unpatched applications - Installation of malware via unvalidated vendor software - Remote access via “interactive” accounts - Installation of malware via removable media - Exploitation of trusted connections within control network - Authorization to ICS applications without sufficient access control mechanisms | - Plant upset/shutdown - Delay plant startup - Mechanical damage/sabotage - Unauthorized manipulation of operator—inappropriate response to process action - Unauthorized modification of ICS database(s) - Unauthorized modification of critical status/alarms - Unauthorized startup/shutdown of ICS devices - Credential leakage (control) - Plant/operational information leakage - Unauthorized modification of ICS access control mechanisms - Unauthorized access to most ICS assets (pivoting/own) - Unauthorized access to ICS assets (communication protocols) - Unauthorized access to business assets (pivoting) |
| Safety systems | - Safety engineering tools - Plant/emergency shutdown communication channels (DCS/SCADA) - Control (safety) network - Software vendor support portal | - Exploitation of unpatched applications - Installation of malware via unvalidated vendor software - Installation of malware via removable media - Installation of malware via keyboard - Authorization to ICS applications without sufficient access control mechanisms | - Plant shutdown - Equipment damage/sabotage - Environmental impact - Loss of life - Product quality - Company reputation |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Telecommunications systems | - Public key infrastructure - Internet visibility | - Disclosure of private key via external compromise - Exploitation of device “unknowingly” connected to public networks - Network access through unmonitored access points - Network pivoting through unregulated network boundaries | - Credential leakage (control) - Information leakage - Unauthorized remote access - Unauthorized access to ICS assets (pivoting) - Command and control |
| Uninterruptible power systems (UPS) | - Electrical management network - Vendor/subcontractor maintenance | - Exploitation of unpatched application (building management system) - Installation of malware via unvalidated vendor software - Network access through unprotected access points - Network pivoting through unregulated network boundaries | - Equipment failure/shutdown - Plant upset/shutdown - Credential leakage - Unauthorized access to ICS assets (pivoting) |
| User – ICS engineer | - Social engineering— corporate assets - Social engineering - personal assets - E-mail attachments - File shares | - Introduction of malware through watering hole or spear-phishing attack on business PC - Introduction of malware via malicious email attachment on business PC from trusted source - Introduction of malware on control network via unauthorized/foreign host - Introduction of malware on control network via shared virtual machines - Introduction of malware via inappropriate use of removable media between security zones (home - business - control) - Propagation of malware due to poor segmentation and “full visibility” from EWS - Establishment of C2 via inappropriate control-to-business (outbound) connections | - Process/plant information leakage - ICS design/application credential leakage - Unauthorized access to business assets (pivoting) - Unauthorized access to ICS assets (pivoting/own) |
| User – ICS technician | - Social engineering—corporate assets - Social engineering— personal assets - E-mail attachments - File shares | - Introduction of malware on control network via connection of unauthorized/foreign host - Introduction of malware on control network via shared virtual machines - Introduction of malware via inappropriate use of removable media between security zones (home - business - control) - Exploitation of applications due to unnecessary use of administrative rights - Network disturbances resulting from connection to networks with poor segmentation | - Plant upset/shutdown - Delay plant startup - Mechanical damage/sabotage - Unauthorized manipulation of operator graphics—inappropriate response to process action - Unauthorized modification of ICS database(s) - Unauthorized modification of status/alarms settings - Unauthorized download of faulty firmware - Unauthorized startup/shutdown of ICS devices - Design information leakage - ICS application credential leakage - Unauthorized access to most ICS assets (pivoting/own) |
| Table Continued |  |  |  |

| Target | Possible Attack vectors | Possible Attack methods | Possible consequences |
| --- | --- | --- | --- |
| Users – plant operator | - Keyboard - Removable media—USB - Removable media—CD/DVD | - Introduction of malware on control network via unauthorized/foreign host - Introduction of malware via inappropriate use of removable media between security zones (home—business—control) - Exploitation of applications due to unnecessary use of administrative rights | - Plant upset/shutdown - Mechanical damage/sabotage - Unauthorized startup/shutdown of mechanical equipment - Process/plant operational information leakage - Credential leakage - Unauthorized access to ICS assets (pivoting) - Unauthorized access to ICS assets (communication protocols) |

It is important to understand at this point the difference between *compromising* or “owning” a target and *attacking* a target. There is no formal definition that defines either, but for the purposes of this book, a compromise can be thought of as the ability to exploit a target and perform an *unknown* action (such as running a malicious payload). An attack, on the other hand, can be thought of as causing a target to perform an *undesirable* action. In this case, the device may be performing as designed, yet the ability to attack the device and cause it to perform an action that is not desired by the engineer may lead to negative consequences. Many ICS devices can therefore be attacked via the  *exploitation of functionality* versus the *exploitation of vulnerabilities*. In other words, issuing a “shutdown” command to a control device does not represent any particular weakness in the device per se. However, if the lack of authentication enables a malicious user to inject a shutdown command (i.e., perform a replay attack), this is a major vulnerability.

### Attack phases

Cyberattacks are complex and require multiple stages of development and execution if they are to be successful. This is an important consideration when planning cyber-defensive strategies and when responding to a cybersecurity incident. The attack that you are anticipating (from a defensive context) or are responding to (from an incident response context) might be part of a larger overall effort or attack campaign. Before an attack can even be developed, there is initial reconnassance that must be performed, and in many cases, initial cyberattack phases are needed to identify and enumerate target systems before further attack stages can be developed.

Understanding where a specific event falls within an overall attack strategy will help determine the best way to respond. To this end, frameworks such as the MITRE ATT&CK framework can be useful tools in understanding attack tactics and strategies. This will be covered in detail in [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), “OT Attack and Defense Lifecycles.” However, when discussing cyberattacks against industrial systems, it is important to understand the basic approach of a cyber-physical attack, and it will be discussed here briefly.

For industrial networks, the target infrastructure is not directly accessible, with the exception of specifically allowed network connections (see [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits”). Therefore, an attacker needs to divide their efforts into a minimum of two phases: an initial attack phase that is intended to gain access to the industrial network environment, followed by an additional attack phase once the industrial network has been breached.

#### Initial attack phases

Initial attack phases involve gaining access to the industrial network environment. Because industrial networks should be isolated from direct network connectivity, this means compromising an initial target to provide the attacker with a landing point from which to pivot into the industrial environment. This could be the penetration of nonindustrial networks within an organization, in an attempt to identify a method of reaching the target industrial network. This could be the discovery of legitimate communication paths in hopes of manipulating them, identifying architectural weaknesses such as a dual-homed server, etc.

The initial attack phases primarily concern nonindustrial networks and systems, and will typically require data exfiltration and some means of command and control, so that attackers can learn about their target environment and develop a more targeted attack to ultimately penetrate the industrial network.

#### Industrial attack phases

Once the attacker breaches the industrial network, additional attacks can be developed against the industrial environment. The various stages of the industrial attack phase differ because of the nature of industrial control systems and are the primary focus of this book. Industrial attack phases can include: additional stages of reconnaissance to learn as much as possible about the industrial control system and how it functions; implementation of remote access and command and control functions to allow an attacker to directly interact with the industrial environment; direct manipulation of the industrial control environment to develop and execute targeted cyber-physical outcomes; or perhaps something less sophisticated such as DoS disruptions, data destruction, or the encryption of highly critical systems for purposes of disruption and/or extortion (ransomware in particular represents a nonindustrial attack that can cause major disruption to industrial systems and will be discussed in more depth later in this chapter).

### Cyber-physical attacks

Cyber-physical attacks refer to any attack that leverages cyber techniques (the manipulation of a computing or other digital system) in order to produce a physical outcome (typically via the manipulation of an industrial automation or control system). In properly segmented networks, cyber-physical attacks almost always consist of the above two attack phases: the first to reach the industrial network, which provides access to control system assets, and the second to manipulate those assets. However, cyber-physical attacks can take many forms, including:

1. • Insider attacks. An insider with direct access to industrial control assets could directly manipulate the process control system to achieve a specific physical outcome.
2. • Unintentional local access. Accessing industrial control assets directly, without the knowledge or consent of the user, using corrupt or infected physical media (see “Keylogging/Keystroke Injections/HID Attacks” below).
3. • Lateral attacks. Manipulating one part of a process control system in order to cause a specific physical outcome in another part of that process. For example, manipulating a controller that is responsible for valve within a pipeline in order to create bubbles that could cause a physical failure of downstream hardware components (known as a “cavitation attack”).[5](#fn5)

### Rogue access devices

A rogue access device refers to any device capable of providing unwanted access to networks or computers. This could include anything from a misconfigured server to purpose-built covert hardware designed to provide a malicious backdoor to your network. Some examples include:

1. • A server that is unintentionally dual-homed to two networks.
2. • A server that is misconfigured to act as a WiFi access point, providing a wireless vector the physical network.
3. • A modem or remote access gateway that is installed by a service technician to facilitate troubleshooting, and then left operational.
4. • A server, such as a Raspberry Pi or other single-board computer, that is intentionally connected to the network to provide a covert backdoor to attackers.
5. • A server that is infected with remote access malware, allowing it to send unwanted communications over existing network paths.
6. • Networked devices such as smartphones that have broad communications capabilities, that are physically plugged into a computer (e.g., for charging).

Rogue access devices are not always malicious but present significant risk to industrial networks because they can be leveraged by an attacker to obtain information and establish command and control, which are necessary steps for many industrial cyberattacks (See [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), “OT Attack and Defense Lifecycles”).

Rogue access devices are also not always obvious. There are numerous hardware attack platforms that are designed specifically to penetrate networks with a host of capabilities including full penetration testing software suites, that also present a variety of wired and wireless network connectivity options. When successfully implanted into an industrial network, these devices can potentially bypass the cybersecurity controls at the industrial network perimeter, providing attacks with direct access to industrial systems and assets.

### Keylogging/keystroke injections/HID attacks

A common attack technique for industrial systems involves the manipulation of human interface devices (HIDs). Computers inherently trust input devices such as keyboards and mice; access controls apply to the user of the device, and it is therefore assumed that what the user is typing, pointing to, or clicking within the user interface is an intentional act of that user. This trust can be manipulated by attackers in several ways, including keylogging and keystroke injections.[6](#fn6)

Keylogging refers to the monitoring and capture of keystrokes. The most obvious use case is for the capture of login credentials, but keylogging can be used to capture any data that is input by the user.

Keystroke injection refers to the process of emulating keyboard interaction, tricking the computer into believing that the user typed something that they did not. Because HID devices operate with the same privileges as their user, anything that is “typed” via a keystroke injection will function as if typed by the keyboard's user. For example, if a user is logged in as an administrator any command typed into the Windows console can be executed with administrator privileges as well.

These types of attacks are often referred to as HID attacks. They may be a function of malicious software (malware), although they are increasingly leveraging custom  hardware, especially using the ubiquitous USB standard interface(s). Often referred to as a USB Attack Platforms, or UAPs, these devices are inexpensive and easily obtainable.[7](#fn7) Often sold as penetration testing tools (e.g., the USB Rubber Ducky), they make keystroke injections extremely powerful, scriptable, and easy to deploy by disguising the UAP as a legitimate USB device (e.g., a USB thumb drive). While these tools have been available for many years, they are very popular and are still being actively developed and enhanced. In addition, new variants of UAPs continue to be introduced. In 2020, the system-on-chip hardware used to build such tools became sufficiently miniaturized to enable the development of highly covert UAPs that appear identical to USB charging cables. The power of these devices also continued to improve, and UAP cables are currently available that include built in exfiltration, communications channels, network command and control, keylogging, and keystroke injection.[8](#fn8)

Keylogging and keystroke injection attacks are especially powerful when used together: first capturing information typed by a legitimate human user and then later injecting keystrokes as that same user. For example, capturing keystrokes in order to obtain the username and password of the user and then “typing” those credentials via keystroke injection after business hours to effectively log in to an unattended system.

When HID attacks are combined with network communications, these attacks can be developed and executed remotely, and if combined with rogue access devices, the network communications can occur via rogue networks that may bypass your organization's network security controls. That is, rather than communicating to a command and control server using your organization's network (which may be monitored), communication could occur via a dedicated Wi-Fi access point using an unmonitored wireless network, or communicate via a cellular network to provide reach.

While HID attacks are not limited to USB, the prevalence of USB devices and the ubiquitous support of USB devices by most computing platforms make USB a common vehicle for HID attacks. In addition, the USB standard's power delivery functionality allows UAP devices to power additional components (such as the aforementioned rogue access points). Please refer to [Chapter 11](../B9780443137372000129/CH0011_331-381_B9780443137372000129.xhtml), “Implementing Security and Access Controls” for specific guidance on how to protect against these types of attacks.

### Man-in-the-middle attacks

A man-in-the-middle attack refers to an attack where the attacker goes between communicating devices and snoops the traffic between them. The attacker is actually connecting to both devices, and then relaying traffic between them so that it appears that they are communicating directly, even though they are really communicating through a third device that is eavesdropping on the interaction. To perform a MitM attack, the attacker must be able to intercept traffic between the two target systems and inject new traffic. If the connection lacks encryption and authentication—as is often the case with industrial protocol traffic—this is a very straightforward process. Where authentication or encryption are used, an MitM attack can still succeed by listening for  key exchanges and passing the attacker's key in place of a legitimate key. This attack vector is somewhat complicated in industrial networks because devices can communicate via sessions that are established and remain intact for long periods of time. The attacker would have to first hijack an existing communication session. The biggest challenge to a successful MitM attack is successfully inserting oneself into the message stream, which requires establishing trust. In other words, the attacker needs to convince both sides of the connection that it is the intended recipient. This impersonation can be thwarted with appropriate authentication controls. Many industrial protocols unfortunately authenticate in clear text (if at all), facilitating MitM attacks within the various industrial control systems.

### Denial-of-service attacks

Denial-of-service attacks occur when some malicious event attempts to make a resource unavailable. This is a very broad category of attacks and can include anything from loss of communications with the device, to inhibiting or crashing particular services within the device (storage, input/output processing, continuous logic processing, etc.). DoS attacks in traditional business systems do not typically result in significant negative consequences if resolved in a timely manner. Access to a web page may be slowed, or email delivery delayed until the problem is resolved. However, while there are rarely physical consequences associated with the interruption of services, a well-targeted DoS could bring very important systems off-line, and could even trigger a shutdown.

Automation systems are deployed to monitor or control a physical process. This process could be controlling the flow of crude oil in a pipeline, converting steam into electricity, or controlling ignition timing in an automobile engine. The inability of a controller such as an SIS to perform its action is commonly called “Loss of Control (LoC)” and typically results in the physical process being placed in a “safe” state—shutdown! This means that even simple disruptions of control functions can quickly translate into physical plant disturbances that can further lead to environmental releases, plant shutdowns, mechanical failure, or other catastrophic events. In the case of the HMI, it is not directly connected to the mechanical equipment; however, in many manufacturing industries, the inability of the HMI to perform its function can lead to “Loss of View (LoV),” which often requires the manufacturing process to be shut down if view of data cannot be restored in a timely manner. In the case of an automobile's ignition control system, if the controller stops performing, the engine stops running!

A hacker typically does not boast of a DoS attack on an Internet-facing website (unless you are part of a hacktivist group) but because a DoS can result in LOV or LOC, a similar DoS attack on an ICS can lead to far greater consequences: an oil spill, a plant fire and explosion, or spoiled batches of products. DoS in industrial environments is much more than an inconvenience but can lead to significant consequences if not managed accordingly.

### Replay attacks

Initiating specific process commands into an industrial protocol stream requires an in-depth knowledge of industrial control system operations. It is possible to capture packets and simply replay them to inject a desired process command into the system because most industrial control traffic is transmitted in plain text. When capturing packets in a lab environment, a specific command can be initiated through a console, and the resulting network traffic captured. When these packets are replayed, they will perform the same command. When commands are in clear text, it is simple to find and replace a command from within captured traffic to create custom packets that are crafted to perform specific tasks. If traffic is captured from the field, authentication mechanisms (symmetric encryption, challenge-response, cleartext exchange, etc.) can be captured as well allowing an attacker to authenticate to a device via a replay attack, providing an authorized connection through which additional recorded traffic can be played back. This capability is actually part of many open-source and licensed industrial protocols and is why this can best be referred to as *exploitation of functionality*. If the device is a PLC or other process automation controller, such as the controller functions found in more advanced substation gateways, the behavior of an entire system could be altered. If the target is an IED, specific registers could be overwritten to inject false measurements or readings into a system.

Security researcher Dillon Beresford demonstrated a PLC replay attack at the 2011 Black Hat conference in Las Vegas, NV. The attack began by starting a Siemens SIMATIC STEP 7 engineering console and connecting to a PLC within a lab environment. Various commands were then initiated to the PLC via the STEP 7 console while traffic was being captured. This traffic included a valid STEP 7 to PLC session initiation, allowing the recorded traffic to be played back against any supported PLC to replay those same commands in the field.[9](#fn9)

Replay attacks are useful because of the command-and-control nature of an ICS. A replay attack can easily render a target system helpless because commands exist to enable or disable security, alarms, and logging features. Industrial protocols also enable the transmission of new programmable code (for device firmware and control logic updates), allowing a replay attack to act as a “dropper” for malicious logic or malware. Researcher Ralph Langner described how simple it could be to write malicious ladder logic at the 2011 Applied Control Systems Cyber Security Conference. He was able to inject a time-bombed logic branch with just 16 bytes of code that was inserted at the front of existing control logic that will place the target PLC into an endless loop—preventing the remaining logic from executing and essentially “bricking” the PLC.[10](#fn10)

For the subtle manipulation of industrial systems and automation processes, knowledge of specific ICS operations is required. Much of the information needed to attack a PLC can be obtained from the device itself. For example, in Beresford's example, packet replay was used to perform a PLC scan. Using SIMATIC requests to probe a device, Beresford was able to obtain the model, network address, time of day, password, logic files, tag names, data block names, and other details from the targeted PLC.[11](#fn11)

If the goal is simply to sabotage a system, almost anything can be used to disrupt operations—a simple replay attack to flip the coils in a relay switch is enough to break most processes.[12](#fn12) In fact, malware designed to flip specific bits could be installed within ICS assets to manipulate or sabotage a given process with little chance of detection. If only read values are manipulated, the device will report false values; if write commands are also manipulated, it would essentially render the protocol functionality useless for that device.

### Compromising the human-machine interface

One of the easiest ways to obtain unauthorized command and control of an ICS is to leverage the capabilities of a human-machine interface (HMI) console. Whether an embedded HMI within a control zone, or the centralized command and control capability of DCS, SCADA, EMS or other systems, the most effective way to manipulate those controls is via their console interface. Rather than attacking via the industrial network using MitM or Replay attacks, a known device vulnerability is exploited to install remote access to the console leading to a host *compromise*. One example would be to use the Metasploit framework or similar penetration testing tool to exploit the target system and then using the Meterpreter shell to install a remote VNC server. Now, the HMI, SCADA, or EMS console is fully visible to and controllable by the attacker. This allows the hacker to directly monitor and control whatever that console is responsible for, remotely. There is no knowledge of industrial protocols needed, no specific experience in ladder logic, or control systems operations—only the ability to interpret a graphical user interface, click buttons, and change values within a console that is typically designed for ease of use.

### Compromising the engineering workstation

The vectors used to compromise an Engineering Workstation (EWS) are not much different from those used previously with the HMI. The same vulnerabilities often apply because the system is managed consistently across all hosts. The same payloads (Meterpreter) can also be used to establish C2 functionality. What is important to consider in this case is the relative value of the logical assets contained on the EWS versus those on the HMI. The HMI does provide bidirectionality read/write capability with the process under control; however, many systems today incorporate role-based access control that may limit the extent of these functions in a distributed architecture consisting of multiple operators and multiple plant areas or units.

The EWS, on the other hand, is typically the single host that not only possesses the capability to configure such role-based access control mechanisms but also the specialized tools needed to directly communicate with, configure, and update the primary control equipment (PLC, BPCS, SIS, IED, etc.). It is also common for the EWS to contain significant amounts of sensitive documentation specific to the ICS design, configuration, and plant operation, making this target a much higher-valued asset than a typical HMI.

### Blended attacks

Many attacks are more than single exploits against a single vulnerability on a single target. Sophisticated attacks commonly use a blended threat model. According to SearchSecurity, “a blended threat is an exploit that combines elements of multiple types of malware and usually employs multiple attack vectors to increase the severity of damage and the speed of contagion.”[13](#fn13)

In the past, blended attacks typically contained multiple types of malware that were used in succession—a spear phishing attack to access systems behind a firewall that would drop a Remote Access Trojan (RAT) and then obtain the credentials needed to access the trusted industrial networks, where targets may be compromised or exploited further.

Recently, blended threats have evolved to a much greater degree of complexity. This was first observed with Stuxnet where a single complex and mutating malware framework was deployed that was capable of behaving in multiple ways depending upon its environment. This concept has now been taken even further, with the discovery of Skywiper (also known as Flame) and other complex malware variants.

## Weaponized industrial cyberthreats

Cyberattacks against industrial networks were, at one time, purely theoretical. We have now seen real cyberattacks targeting actual industrial systems. The first documented ICS cyber-attack “in the wild” was Stuxnet discovered in 2010, which was followed shortly by a string of incidents over the next few years. While many high-profile incidents occurred, often targeting the oil industry and countries of the Middle East, Stuxnet remains a strong example of what a modern, weaponized industrial cyberattack looks like. Stuxnet was very precise, sabotaging specific ICS devices to obtain a specific goal. Shortly after Stuxnet, Shamoon (also DistTrack) and Flame (also called Flamer or Skywiper) surfaced. Shamoon was widely publicized due to its highly destructive nature. Rather than performing a precision attack against target devices, like Stuxnet, Shamoon spread promiscuously and wiped systems clean, incurring huge impact to the computing infrastructure of infected companies. Flame showed signs of being a derivative of Stuxnet, with even greater sophistication. However, the intention of Flame seems to be espionage rather than sabotage or the direct destruction of target systems.

### Stuxnet

Stuxnet is the poster child of industrial malware. When discovered, it was the first real example of weaponized computer malware, which began to infect ICSs as early as 2007.[14](#fn14) Any speculation over the possibility of a targeted cyberattack against an industrial network has been overruled by this extremely complex and intelligent collection of malware. Stuxnet is a tactical nuclear missile in the cyberwar arsenal. It was not just a “ shot across the bow,” but rather it hits its mark and left behind the proof that extremely complex and sophisticated attacks can and do target industrial networks. The worst-case scenario has now been realized—industrial vulnerabilities have been targeted and exploited by a sophisticated threat actor more commonly called an advanced persistent threat (APT).

Although early versions of Stuxnet were released as early November 2007,[15](#fn15) widespread discussions about it did not occur until the summer of 2010, after an Industrial Control Systems Cyber Emergency Response Team (ICS-CERT) advisory was issued.[16](#fn16)

Stuxnet was armed with four 0-days in total at its disposal. Stuxnet was able to infect Windows-based computers covering four generations of kernels from Windows 2000 up to and including Windows 7/Server 2008R2. The primary target was a system comprising Siemens SIMATIC WinCC and PCS7 software along with specific models of S7 PLCs utilizing the PROFIBUS protocol to communicate with two specific vendors of variable frequency drives (VFD). These VFDs were used to control the centrifuges used in the process of enriching uranium.[17](#fn17) (PROFIBUS is the industrial protocol used by Siemens and was covered in [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml), “Industrial Network Protocols”.) The subsequent steps taken by the malware depend on what software was installed on the infected host. If the host was not the intended target, the initial infection would load a rootkit that would automatically load the malware at boot and allow it to remain undetected. It then would deploy up to seven different propagation methods to infect other targets. For those methods using removable media, the malware would automatically remove itself after the media infected three new hosts. If the target contained Siemens SIMATIC software, methods existed to exploit default credentials in the SQL Server application allowing the malware to install itself in the WinCC database, or to copy itself into the STEP 7 project file used to program the S7 PLCs. It also had the ability to overwrite a critical driver used to communicate with the S7 PLCs effectively creating a MitM attack allowing the code running in the PLC to be altered without detection by the system users.

Although little was known at first, Siemens effectively responded to the issue, quickly issuing a security advisory, as well as a tool for the detection and removal of Stuxnet. Stuxnet drew the attention of the mass media through the fall of 2010 for being the first threat of its kind—a sophisticated and blended threat that actively targets ICS—and it immediately raised the industry's awareness of advanced threats by illustrating exactly why industrial networks need to dramatically improve their security measures.

#### Dissecting stuxnet

Stuxnet is very complex, as can be seen by the Infection Process shown in [Figure 7.2](#f0015). It was used to deliver a payload targeting not only a specific control system but also a specific configuration of the control system including unique model numbers of PLCs and vendors of field-connected equipment. It is the first rootkit targeting ICS. It can self-update even when cut off from the C2 servers (which is necessary should it find its way into a truly air-gapped system) by enumerating and remembering a complex peer-to-peer network necessary to allow external access. It is able to inject code into the PLCs,  and at that point alter the operations of the PLC as well as hide itself by reporting false information back to the HMI. It adapts to its environment. It uses system-level, hard-coded authentication credentials that were publicly disclosed as early as 2008[18](#fn18) (indications exist that it was disclosed within the Siemens Support portal as early as 2006[19](#fn19)). It was able to install malicious drivers undetected by Windows through the use of two different legitimate digital certificates manufactured using stolen keys. There is no doubt about it at this time—Stuxnet is an advanced new weapon in the cyber war.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000014/main.assets/f07-02-9780443137372.jpg)

*[Figure 7.2](#Bf0015)  Stuxnet's infection processes.*

#### What it does

The full extent of what Stuxnet is capable of doing remains uncertain at the time of this writing. What we do know is that Stuxnet does the following:[20](#fn20)

1. • Infects Windows systems using a variety of 0-day exploits and stolen certificates and installing a Windows rootkit on compatible machines.
2. • Attempts to bypass behavior-blocking and host intrusion-protection-based technologies that monitor LoadLibrary calls by using special processes to load any required DLLs, including injection into preexisting trusted processes.
3. 
4. • Typically infects by injecting the entire DLL into another process and only exports additional DLLs as needed.
5. • Checks to make sure that its host is running a compatible version of Windows, whether or not it is already infected, and checks for installed **antivirus** before attempting to inject its initial payload.
6. • Spreads laterally through infected networks, using removable media, network connections, print services, WinCC databases, and/or Step 7 project files.
7. • Looks for target industrial systems (Siemens SIMATIC WinCC/PCS7). When found, it injects itself into an SQL database (WinCC) or project file (Step 7), and replaces a critical communication driver that will facilitate authorized and undetected access to target PLCs.
8. • Looks for target system configuration (S7-315-2/S7-417 PLC with specific PROFIBUS VFD). When found, it injects code blocks into the target PLCs that can interrupt processes, inject traffic on the Profibus-DP network, and modify the PLC output bits, effectively establishing itself as a hidden rootkit that can inject commands to the target PLCs.
9. • Uses infected PLCs to watch for specific behaviors by monitoring PROFIBUS.
10. • If certain frequency controller settings are found, Stuxnet will throttle the frequency settings sabotaging the centrifuge system by slowing down and then speeding up the motors to different rates at different times.
11. • It includes the capabilities to remove itself from incompatible systems, lay dormant, reinfect cleaned systems, and communicate peer to peer in order to self-update within infected networks.
12. • It includes a variety of stop execution dates to disable the malware from propagation and operation at predetermined future times.

What we do not know at this point is what the full extent of damage could be from the malicious code that is inserted within the PLC. Subtle changes in **set points** over time could go unnoticed that could cause failures down the line, use the PLC logic to extrude additional details of the control system (such as command lists), or just about anything. Another approach might be to perform man-in-the-middle attacks intercepting invalid process values received from the PLCs and forward to the WinCC HMI bogus values for display making the plant operator unaware of what is actually occurring in the plant. Because Stuxnet has exhibited the capability to hide itself and lie dormant, the end goal is still a mystery.

#### Lessons learned

Because Stuxnet is such a sophisticated piece of malware, there is a lot that we can learn from dissecting it and analyzing its behavior. A detailed white paper coauthored by one of the authors of this book has been developed that specifically analyzes Stuxnet in terms of its impact on industrial control systems, and how they are designed and deployed in actual operational environments.[21](#fn21) How did we detect Stuxnet? It succeeded largely  because it was so widespread and infected approximately 100,000 hosts searching for a single target. Had it been deployed more tactically, it might have gone unnoticed—altering PLC logic and then removing itself from the Siemens SIMATIC hosts that were used to inject those PLCs. How will we detect the next one? The truth is that we may not, and the reason is simple—our “barrier-based” methodologies do not work against cyberattacks that are this well researched and funded. Furthermore, since Stuxnet's propagation mechanisms were all LAN-based, the target host must be assumed on direct or adjacent networks to the initial infection. In other words, the attack originated from inside the targeted organization. They are delivered via 0-days, which means we do not detect them until they have been deployed, and they infect areas of the control system that are difficult to monitor.

So what do we do? We learn from Stuxnet and change our perception and attitude toward industrial network security (see [Table 7.3](#t0020)). We adopt a new “need to know” mentality of control system communication. If something is not explicitly defined, approved, and allowed to execute and/or communicate, it is denied. This requires understanding how control system communications work, establishing that “need to know” and “need to use” in the form of well-defined security zones with equally defined perimeters, establishing policies and baselines around those zones, and then implementing cyber security controls and countermeasures to enforce those policies and minimize the risk of a successful cyber-attack.

It can be seen in [Table 7.3](#t0020) that additional security measures need to be considered in order to address new “Stuxnet-class” threats that go beyond the requirements of  compliance mandates and current best-practice recommendations. New measures include layer 7 application session monitoring to discover 0-day threats and to detect covert communications over allowed “overt” channels. They also include more clearly defined security policies to be used in the adoption of policy-based user, application, and **network whitelisting** to control behavior in and between zones (see [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits”).

[Table 7.3](#Bt0020)

| Previous beliefs | Lessons learned from stuxnet |
| --- | --- |
| Control systems can be effectively isolated from other networks, eliminating risk of a cyberincident. | Control systems are still subject to human nature: a strong perimeter defense can be bypassed by a curious operator, a USB drive, and poor security awareness. |
| PLCs and RTUs that do not run modern operating systems lack the necessary attack surface to make them vulnerable. | PLCs can and have been targeted and infected by malware. |
| Highly specialized devices benefit from “security through obscurity.” because industrial control systems are not readily available, it is impossible to effectively engineer an attack against them. | The motivation, intent, and resources are all available to successfully engineer a highly specialized attack against an industrial control system. |
| Firewalls and intrusion detection and prevention system (IDS/IPS) are sufficient to protect a control system network from attack. | The use of multiple 0-day vulnerabilities to deploy a targeted attack indicates that “blacklist” point defenses, which compare traffic to definitions that indicate “bad” code are no longer sufficient, and “whitelist” defenses should be considered as a catchall defense against unknown exploits. |

TipThe axiom “to stop a hacker, you need to think like a hacker” was often used before Stuxnet. This simply meant that in order to successfully defend against a cyberattack you need to think in terms of someone trying to penetrate your network. This philosophy still has merit, the only difference being that now the “hacker” can be thought of as having a much greater knowledge of deployed ICSs, an understanding of the manufacturing processes, and how the ICS is used to control this environment, along with significantly more resources and motivation. The ISA 62443 family of industry standards provides the ability to address each of these aspects in terms of a security level. In the post-Stuxnet world, imagine building a digital bunker in the cyber war, rather than simply defending a network, and aim for the best possible defenses against the worst possible attack. In other words, “think like an insider.”
### Shamoon/DistTrack

Shamoon, or W32.DistTrack (often shortened to “DistTrack”), possesses both information gathering and destructive capabilities. Shamoon will attempt to propagate to other systems once an initial infection occurs, exfiltrate data from the currently infected system, and then cover its tracks by overwriting files, including the system's master boot record (MBR). The system is then unusable, and overwritten data are not recoverable once the MBR is destroyed. The result, Shamoon left a path of inoperable systems in its wake.[22](#fn22)

Shamoon accomplished this through three primary components:[23](#fn23)

1. • Dropper—a modular component responsible for initial infection and network propagation (often through network shares)
2. • Wiper—a malware component responsible for system file and MBR destruction
3. • Reporter—a component designed to communicate stolen data and infection information back to the attacker.

Much of the details around Shamoon are protected from disclosure; however, Shamoon reportedly infected business systems of Saudi Aramco (an oil and gas company in the Kingdom of Saudi Arabia) and caused the destruction of at least 30,000 systems. Luckily, this destruction did not spread to industrial network areas and therefore did not directly impact oil production, refining, transportation, or safety operations.[24](#fn24)

#### Flame/flamer/skywiper

Skywiper is an advanced persistent threat that spread actively, targeting Middle Eastern countries, with the majority of infections occurring in Iran. Like Stuxnet, Skywiper (Flame) redefined the complexity of malware in its time. Skywiper had been active for years prior to being discovered also like Stuxnet, mining sensitive data and returning them to a sophisticated C2 infrastructure consisting of over 80 domain names, and using servers that moved between multiple locations, including Hong Kong, Turkey, Germany, Poland, Malaysia, Latvia, the United Kingdom, and Switzerland.[25](#fn25)

Over a dozen modules are present within Skywiper, including:[26](#fn26)

1. • “Flame”—handles AutoRun infection routines (Skywiper is often referred to as Flame because of this package)
2. • “Gadget”—an update module that allows the malware to evolve and to accept new modules and payloads
3. • “Weasel” and “Jimmy”—handle disk and file parsing
4. • “Telemetry” and “Gator”—handle C2 routines
5. • “Suicide”—self-termination
6. • “Frog”—exploit payload to steal passwords
7. • “Viper”—exploit payload that captures screenshots
8. • “Munch”—exploit payload that captures network traffic

Skywiper seems to be focused on espionage rather than sabotage. No modules dedicated to manipulation or sabotage of industrial systems have been detected at the time of this writing. The modular nature of Skywiper would certainly allow the threat to include more damaging modules as needed, no doubt leveraging the “Gadget” update module to further evolve the malware into a directed cyber weapon.

### Dragonfly

Dragonfly is an example of a nondestructive cyber campaign targeting industrial control systems. In 2014, the first reports of Dragonfly emerged from F-Secure and Symantec. The Dragonfly campaign is named after the Dragonfly group (also known as “Energetic Bear”). This group “initially targeted defense and aviation companies in the US and Canada before shifting its focus to US and European energy firms in early 2013,” according to Symantec.[27](#fn27)

The Dragonfly campaign used several different malicious payloads. However, the Havex RAT (also known as Backdoor.Oldrea) was the primary malware utilized in approximately 95% of Dragonfly payloads.[28](#fn28) For this reason, Dragonfly is also referred to as Havex.

Dragonfly was initially believed to be a cyberespionage campaign targeting the energy sector,[29](#fn29) although subsequent reports claimed that the actual target was the pharmaceutical industry.[30](#fn30) Regardless of the intended target sector, Dragonfly is of interest largely because of the types of organizations that it was able to compromise and exfiltrate data from. In Symantec's analysis, “if they had used the sabotage capabilities open  to them, could have caused damage or disruption to the energy supply in the affected countries.”[31](#fn31)

Dragonfly is also of interest because of its clever vectors for targeting industrial control systems. Initially, the Havex RAT was distributed via spear phishing campaigns, but the Dragonfly group shifted tactics to watering hole attacks using several energy-related websites. Legitimate websites were compromised and malicious frames were injected that would redirect to an additional compromised website, which in turn compromised the victims' computers by exploiting either Java or Internet Explorer.[32](#fn32)

Finally, Dragonfly was able to compromise of a number of legitimate software packages from industrial control equipment vendors, inserting malware into software that the vendors had made available on their websites.[33](#fn33)

While nondestructive, Dragonfly is considered to have been a successful reconnaissance campaign, and one can speculate that the knowledge obtained contributed to the development of future industrial control attack techniques.

### BlackEnergy

Nearly a quarter of a million energy customers in Ukraine experienced a blackout on December 23, 2015, as the result of the first known real-world example of a successful, targeted cyberattack against the energy grid.[34](#fn34) The attack—often called “Black Energy” in reference to the attack's utilization of a malware tool named “BlackEnergy 3”—illustrates the effectiveness of a true attack campaign versus more autonomous malware frameworks. The attackers combined targeted malware with “careful planning, discipline in execution, and capability in many of the discrete tasks exhibited” over almost an entire year prior to the final stage of the attack.[35](#fn35)

The attack combined many techniques in a highly coordinated attack. This is perhaps best summarized in a DHS NCCIC in an Incident Alert issued in March 2016 that called for critical infrastructure owners to “implement enhanced cyber measures that reduce risks from the following types of adversary techniques:[36](#fn36)

1. • Theft of legitimate user credentials to enable access masquerading as approved users
2. • Leveraging legitimate remote access pathways (VPNs)[37](#fn37)
3. • The remote operation of human-machine interface (HMI) via company-installed remote access software (such as RDP, TeamViewer, or rlogin)[38](#fn38)
4. • The use of destructive malware such as KillDisk to disable industrial control systems (ICSs) and corporate network systems[39](#fn39)
5. • Firmware overwrites that disable/destroy field equipment[40](#fn40)
6. • Unauthorized scheduled disconnects of uninterruptible power supplies (UPS) to devices to deny their availability[41](#fn41)
7. • The delivery of malware via spear-phishing emails and the use of malicious Microsoft Office attachments[42](#fn42)
8. • Use of Telephone Denial of Service (TDoS) to disrupt operations and restoration”[43](#fn43)

After considerable research throughout the public and private sector, a more complete timeline of the attack became clear. In the report, “When The Lights Went Out: A Comprehensive Review Of The 2015 Attacks On Ukrainian Critical Infrastructure” the full extent of the campaign was described in 17 discrete steps[44](#fn44) including:

1. • Initial reconnaissance, development of initial malware, and development of documents with which to deliver the initial infections.[45](#fn45)
2. • The delivery of those documents via a phishing campaign and the subsequent installation of the BlackEnergy 3 RAT.[46](#fn46)
3. • BlackEnergy 3 establishes connectivity to attacker-owned command and control (C2) servers, the subsequent installation of additional malware plugins designed to harvest credentials, and the harvesting of credentials using these new plugins.[47](#fn47)
4. • Internal reconnaissance and lateral movement on both the targeted network and the industrial control system network to identify targets and the subsequent development of a malicious firmware update for identified serial-to-Ethernet converters.[48](#fn48)
5. • Ensuring planned disruptions to incident response efforts by placing the KillDisk malware on a network share and setting a policy on a domain controller to retrieve the malware and execute it upon system reboot. The attackers also scheduled an Uninterruptible Power Supply (UPS) disruption to cause a coordinated outage of UPS for telephone communication servers and data center servers.[49](#fn49)
6. • Using legitimate access and credentials to open breakers and disrupt power distribution, creating a blackout across three distribution areas.[50](#fn50)
7. • Delivering malicious firmware updates to the serial-to-Ethernet converters used to enable network access to the breakers, bricking the converters, and effectively cutting off the communication paths needed for remote recovery. A DoS attack on telephone call centers was also initiated in coordination with the abovementioned scheduled UPS outage, in a further attempt to hinder response efforts.[51](#fn51)
8. • Finally, critical system data were destroyed through the schedule execution of KillDisk, which among things destroyed system log data on impacted systems.[52](#fn52)

The incident illustrates that targeted campaigns consist of many discreet steps. Sometimes, referred to as a “Kill Chain”, these steps are all necessary for a successful attack. This is why it is important to understand both the lifecycle of an attack and also the lifecycle of defensive efforts against such attacks (see [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), OT Attack and Defense Lifecycles”).

### Industroyer

Industroyer (also referred to as Crash Override) caused a blackout in parts of Kyiv, Ukraine, in 2016, nearly 1 year after the blackouts caused by BlackEnergy. Like BlackEnergy, Industroyer was a sophisticated campaign that included preparatory  stages, establish C2, the development of targeted payloads, and an attempt to destroy key systems through the use of wiper malware. Unlike BlackEnergy, the Industroyer malware was designed specifically to attack the electrical grid, which it did by leveraging several of the industrial protocols used by the grid.[53](#fn53) There were four modules used: one for each of the four protocols leveraged. These included: IEC 60870-5-101, IEC 60,870-5-104, IEC 61,850, and OLE for Process Control Data Access (OPC-DA).[54](#fn54) These protocols are discussed in [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml), “Industrial Network Protocols.”

The ability for Industroyer to interact directly with relays over these protocols differentiates it from BlackEnergy, which relied largely on the harvesting of legitimate credentials and misuse of other legitimate network systems. As such, Industroyer has the ability to be used more easily as a part of less coordinated campaigns. While C2 remains a necessary function for Industroyer, the malware consisted of two command and control functions, for persistence in case the primary C2 was discovered and disabled.[55](#fn55)

### TRISIS/TRITON

TRISIS (also known as TRITON) was first discovered in 2017 by the analysts at Dragos, Inc.[56](#fn56) It is special in that it is the first known malware to target a SIS. TRISIS specifically targeted Schneider Electric's Triconex SIS, although it is feasible that other SISs could be targeted using similar methods. As such, TRISIS represents a new era of cyber-physical threats, where the safety controls put in place to prevent physical failures could potentially be manipulated by a cyberattack.

As malware, TRISIS does not seem that special. Unlike some of the other attacks discussed here, it is fairly simple in design. It consists of a compiled python script, using a python compiler (py2exe) to allow it run on target machines in an industrial environment, including SIS targets.[57](#fn57) It consists of four components: two embedded binaries that are designed to prepare the target for two external binaries. The external binaries contain replacement logic that is intended to alter the function of the SIS.[58](#fn58)

Because the specific instrumentation and control logic of an SIS is extremely specific to the system it is protecting, TRISIS must be tailored to a specific target. In the initial analysis, Dragos points out that the script takes its target as a command-line argument that is passed to it on execution, implying that the script is specific to the specific target SIS device (in this case the Triconex 3008 processor module).[59](#fn59) Other variants of TRISIS have been discovered in the wild, and the initial variant has also been discovered far outside of the initial targets, indicating that the scope of SIS attacks may be larger than first realized.

TRISIS requires access to a system that is able to communicate to the SIS, which requires an attacker to first gain access to such a system. Without prior knowledge of the environment, an attacker must first gain access and determine the specific SIS equipment to target, develop specific logic for TRISIS to implement, test that logic, and then deliver that specific logic for TRISIS to install and modify.[60](#fn60) On its own, this makes TRISIS less concerning. However, if utilized with other attack frameworks as part of a  larger targeted campaign that provides command and control to the attacker, TRISIS could be easily customized and weaponized, allowing an attacker to cause significantly greater impact. This is why SIS systems (and any critical high-value targets) should be segmented within specific and heavily monitored security zones, to limit access via the network and/or other vectors (TRISIS has also been discovered on USB drives being carried into process control environments).[61](#fn61)

### Industroyer2

Industroyer2 is a newer variant of Industroyer involved in another attack on against the power grid in Ukraine in April 2022.[62](#fn62) Industroyer2 is in some ways simplified from the original Industroyer, yet in some ways more sophisticated. Unlike Industroyer, Industroyer2 consisted of a single Windows executable, rather than a modular framework capable of importing malware plugins. Industroyer only included one industrial protocol, IEC 60870-5-104, and there were enough code similarities that analysts at ESET concluded that Industroyer2 was built using the source code from the original Industroyer's IEC 60870-5-104 payload.

While Industroyer2 is not modular, it is highly configurable. A detailed configuration capability was hardcoded into the body of the Industroyer executable, allowing it to utilize the 104 protocol in an extremely flexible manner.[63](#fn63) The lack of external configuration files means that each attack using Industroyer2 needs to be individually crafted and compiled; it also means that the entire attack is self-contained without the need to establish network communications to function.[64](#fn64) According to Mandiant, “[Industroyer2] shows a nuanced understanding of the victim environment … The actor's successful implementation of IEC-104 to interact with the targeted devices indicates a robust understanding of the protocol and knowledge of the victim environment. For example, in the samples we analyzed the actor manipulated a selected list of Information Object Addresses (IOAs), which are used to interact with power line switches or circuit breakers in a remote terminal unit (RTU) or relay configuration.”[65](#fn65)

Together, BlackEnergy, Industroyer, and Industroyer2 show the progression of targeted energy attacks over several years.

### Incontroller/pipedream

Incontroller, also known as Pipedream, represents a powerful and highly flexible cyber-physical attack platform. It includes three modular components for industrial control manipulation: TAGRUN, an OPC-UA tool for reconnaissance; CODECALL, a Modbus tool with the ability to interact with various PLCs using device-specific modules, and OMSHELL, a tool targeting Omron PLCs.[66](#fn66)

Each of these components is modular and extensible and highly capable. TAGRUN is able to brute force credentials to access OPC-UA servers and then scan for OPC-UA servers over the network, read the structure of those servers, and finally both read and write specific tag data.[67](#fn67) CODECALL is able to identify specific Schneider Electric  Modicon PLCs, as well as other Modbus-enabled devices on a network. It can connect to those devices using Modbus or Codesys (Schneider's proprietary protocol used by the Modicon PLCs). Using Modbus, CODECALL can request device IDs, read and write specific device registers, and manipulate command macros. When using Codesys, CODECALL can brute force PLC credentials, manipulate the filesystem (including downloading, uploading, and deleting files), manipulate network configurations, send custom raw packets over the network, and crash the device.[68](#fn68) OMSHELL is able to scan for compatible Omron devices, and manipulate them in a variety of ways including activating telnet, establishing a backdoor, capturing network traffic, wiping, and resetting the device, and connecting and controlling any attached servo drives.[69](#fn69)

Incontroller is interesting for several reasons. First, the presence of an OPC-UA toolkit allows it to gather information regarding the industrial environment via OPC-UA servers that could be deployed in higher levels of the Purdue model (levels 3.5 or 4. See [Chapter 5](../B9780443137372000038/CH0005_91-128_B9780443137372000038.xhtml), “Industrial Network Design and Architecture” and [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits”). There are also additional toolkits used by Incontroller to attack and exploit Windows systems, likely targeting HMI systems and engineering workstations,[70](#fn70) as well as providing backdoor and reconnaissance capabilities for command and control.[71](#fn71) This makes Incontroller the first cyber-physical attack framework since Stuxnet to provide end-to-end capability in both the initial cyberattack phases (required to reach the industrial control environment), and subsequent cyber-physical attack phases (manipulating the industrial control environment once it can be accessed).

Incontroller is extremely flexible: consisting of multiple toolkits, each of which is modular and configurable; these tools can be used all together in a coordinated end-to-end attack or individually. At the time of this writing, Incontroller has not been associated with any known cyber-physical attack campaign or incident.[72](#fn72) However, it “represents an exceptionally rare and dangerous cyber attack capability” that is “comparable to Triton … Industroyer … and Stuxnet.”[73](#fn73)

## Attack trends

While the techniques and tactics of industrial cyber threats will typically follow a logical progression (see [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), “OT Defense Lifecycle & Defensive Methods”). Trends can be discovered through the analysis of known cyberincidents. However, the exact nature of attack is difficult to predict; adversaries will continue to adapt to what is most effective. This could include, but is not limited to, a shift in the initial infection vectors, the quality of the malware being deployed, its behavior, and how it spreads through networks and organizations.

Early industrial threats evolved by trending “up the stack,” with exploits moving away from network-layer and protocol-layer vulnerabilities and more toward application-specific exploits, even more recent trends show signs that these applications are shifting away from the exploitation of Microsoft platform products (i.e., operating system  exploitation) toward the almost ubiquitously deployed client-side applications like web browsers (Internet Explorer, Firefox, Safari, Chrome), Adobe Acrobat Reader, and Adobe Flash Player.

Newer industrial threats have continued this trend through the direct manipulation of industrial device firmware, industrial protocols, and the development of modular cyber-physical attack frameworks.

Web-based applications became popular both for initial infections and for C2. The use of social networks, such as Twitter, Facebook, Google groups, and other cloud services, also became popular because they are widely used, highly accessible, and difficult to monitor. Even more interesting is that many users access these services on mobile and portable devices that typically contain no additional security software. Many companies continue to embrace social networking for marketing and sales purposes, often to the extent that these services are allowed open access through corporate firewalls. This is further compounded by privacy concerns relating to what corporate IT is actually allowed to monitor within the social media sessions. Issues around privacy are outside the scope of this book, but it is worth noting that regulations vary widely from country to country, and that the expansion of corporate networks across borders could introduce latent security vulnerabilities that should be accounted for.

In a properly segmented industrial network, web applications and social media should be of no concern. Connections to the Internet from within an industrial network should be prohibited or at the very least strictly monitored and controlled. Unfortunately, many industrial networks remain connected to the Internet, posing an increased risk.

One quality of cybersecurity that remains consistent is that it is always changing. As awareness increased and industrial networks became more protected and difficult to infiltrate, threat actors looked for new vectors. The malware itself also evolved. There is continued evidence among incident responders and forensics teams of the existence of deterministic malware and the emergence of mutating bots. Stuxnet is a good example again, as it was one of the earliest examples of malware that contained robust logic and that could operate differently depending upon its environment. Stuxnet spreads, attempts to inject PLC code, communicates via C2, lies dormant, or awakens depending upon changes to its environment. Since Stuxnet, malware has continued to evolve.

### Evolving vectors

As industrial control systems evolved and IT and OT began to converge (see [Chapter 2](../B9780443137372000142/CH0002_11-43_B9780443137372000142.xhtml), “Industrial Cyber Security History and Trends: The Convergence of OT and IT”), attack vectors have also evolved. In the early days of largely analogue systems and physical “air gap” security, the human element was the primary vector. Insider threats from a rogue employee were a primary concern, with the social engineering of friendly insiders being a close second.

As industrial systems became digitized, and as serial communications shifted to routable networks, the primary vector quickly shifted to the network. Most of the attack examples listed above utilize the network either as an initial attack vector or for C2 capabilities that are used to exfiltrate data and drop new malware.

As industrial network security has improved (something that the authors believe is at least partly because of the original publication of this book in 2011), attackers have been forced to adapt. Dragonfly's watering hole attacks using infected vendor files was likely an attempt to bypass the network perimeter of the ICS: instead of breaching the ICS directly, the attackers tricked an authorized user into downloading their malware, presumably onto an engineering or service laptop that would then be used by authorized users to install what they believed to be legitimate software into ICS systems. With the evolution of BlackEnergy to Industroyer to Industroyer2, we also saw a shift: reliance on network-based attacks was reduced; redundant C2 channels were introduced on the assumption that one would be detected and blocked; and ultimately payloads were developed with no network dependence at all.

A similar reaction to improved industrial network security is the use of removable media, most commonly USB thumb drives, and other portable media. Information has to flow into and out of an industrial network in order for the ICS to operate. Systems need to be patched, information needs to be managed, processes need to be refined, work orders need to be distributed, etc. All of this requires information flow. If information flow via the network is controlled too strictly, alternate methods of moving information will be necessary. USB thumb drives, and the ubiquity of USB interfaces, makes USB removable media a popular method of data transfer in industrial systems.

Unfortunately, attackers realize this also and so USB-based attacks have been developed. Initially, a USB drive might simply be a way to transfer malware in lieu of a network. However, newer and more dangerous USB attacks have been discovered. In a report by researchers at Ben-Gurion University, 29 different USB-based attacks were identified, falling into four main categories: Programable Microcontrollers; Maliciously Reprogrammed Peripherals; Not-Reprogrammed Peripherals; and Electricical.[74](#fn74) Together they include everything from methods of hiding malware on USB storage volumes to utilizing the USB communications standards themselves as an attack vector. Perhaps, the most well-known USB attack is the “USB Rubber Ducky,” a Programable Microcontroller, which is used for keyboard injection or “Human-Interface Device” (HID) attacks. See “Rogue Access Devices,” “Key-logging,” and “Keystroke Injections” above for more information on these common USB attacks methods.

How serious are USB-based threats? In 2019, Honeywell began publishing an annual USB Industrial Cybersecurity Report, which focuses solely on malware detected on USB removable media while entering or exiting an industrial control environment. The findings in 2022 (the most recent report published at the time of this writing) indicate that USB storage devices are being intentionally used to penetrate highly isolated networks such as control systems. This is inferred from the high percentage of malwares that: are designed to leverage USB devices for propagation; attempt to establish remote  access and command-and-control capability; and are capable of causing disruption to an industrial control system (52%, 51%, and 81%, respectively).[75](#fn75)

#### Supply chain vulnerabilities

Sometimes, vulnerabilities are found in commonly used operating systems, applications, or software packages that are widely used in industrial (and other) environments. When this happens, otherwise “hard” systems can suddenly become permeated with vulnerabilities. In industrial environments, this is especially problematic due to the difficulties in patching OT systems. A few examples of large-scale vulnerabilities that permeated the supply chain include vulnerabilities in the Portable Document Format (pdf), OpenSLL, and the java logging package Log4j.

#### Adobe Portable Document Format

Adobe Portable Document Format (PDF) is widely used as a means of reliably transferring documents with consistent formatting and a degree of data protection. Due to the popularity of the file format, PDF is a prime target for attackers looking to develop new trojan malwares. This allows the attack surface to expand significantly as there are far greater desktops to attack than servers. In some cases, the exploits utilize features within PDFs to call and execute code to perform malicious actions, rather than exploiting a specific bug or vulnerability. This occurs by either calling a malicious website or by injecting the code directly within the PDF file. For example:

1. • An email from a trusted source contains a compelling message; a properly targeted spear-phishing message. There is a PDF document attached to the email.
2. • This PDF uses a feature, specified in the PDF format, known as a “Launch action.” Security researcher Didier Stevens successfully demonstrated that Launch actions can be exploited and can be used to run an executable embedded within the PDF file itself.[76](#fn76)
3. • The malicious PDF also contains an embedded file named Discount_at_Pizza_Barn_Today_Only.pdf, which has been compressed inside the PDF file. This attachment is actually an executable file, and if the PDF is opened and the attachment is allowed to run, it will execute.
4. • The PDF uses the JavaScript function exportDataObject to save a copy of the attachment to the user's local computer.
5. • When this PDF is opened in Adobe Reader (JavaScript must be enabled), the exportDataObject function causes a dialogue box to be displayed asking the user to “Specify a file to extract to.” The default file is the name of the attachment, Discount_at_Pizza_Barn_Today_Only.pdf. The exploit requires that the users' naïveté and/or their confusion regarding a message (which can be customized by the malware author[77](#fn77)), they do not normally see to cause them to save the file.
6. • Once the exportDataOject function has completed, the Launch action is run. The Launch action is used to execute the Windows command interpreter (cmd.exe), which searches for the previously saved executable attachment Discount_at_Pizza_Barn_Today_Only.pdf and attempts to execute it.
7. 
8. • A dialog box will warn users that the command will run only if the user clicks “Open.”

This simple and effective hack is readily available in open-source toolkits like Kali Linux and the Social Engineering Toolkit (SET) and has been used to spread known malware, including ZeusBot.[78](#fn78) Although this attack vector requires user interaction, PDF files are extremely common, and when combined with a quality spear-phishing attempt, this attack can be very effective. Quality is typically measured by how trust is established with the recipient and their likelihood of opening the attachment.

Another researcher chose to infect the benign PDF with another Launch hack that redirected a user to a website, but noted that it could have just as easily been an exploit pack and/or embedded Trojan binary.

There are numerous other Adobe Reader-based vulnerabilities that employ alternate methods to compromise a victim's local computer. Adobes, and other popular client application developers, continue to struggle in keeping up with vulnerability disclosures and the creation of exploit code due to the widespread use and dependence on these applications.

#### Macros

Macros are interpreted programs built into many applications, most notably in Microsoft Office applications. Macros are powerful tools used for automation and can extend the functionality of a word processor or spreadsheet considerably. However, they also represent a vector for attack: the macro virus. By creating documents or document templates with malicious macros, the otherwise-legitimate document becomes a vessel for malware.[79](#fn79)

Macro viruses became so prolific that Microsoft took steps to prevent the accidentle use of macros as early as Windows 7, and in newer releases of Microsoft's applications macros are disabled by default. Now, macros are only effective if the attacker can convince users to turn on macros so that their malicious macro can run.[80](#fn80)

Macros are of interest to industrial operators because the systems and applications used are often older. In addition, documents that originate from inside an industrial organization (perhaps a work order or a procedural update) tend to be trusted.

TipConsider disabling macros and implementing cybersecurity controls that prevent macros from executing (e.g., Application Whitelisting, or AWS) and/or that prevent access to files that contain macros (e.g., policy-based file access controls). If using document macros is necessary as part of daily operations, more advanced security controls may be needed.
#### Secure sockets layers

“A missing bounds check in the handling of the TLS heartbeat extension can be used to reveal up to 64k of memory to a connected client or server.”[81](#fn81) This, the first sentence in a 2014 security advisory from OpenSLL that in total was just over 100 words long had profound impact on the Internet and on the tech community. CVE-20014-0160, dubbed “Heartbleed,” represents a critical flaw in OpenSSL versions 1.0.1 and 1.0.2 that can be used to reveal private keys used and decrypt sensitive data transferred within SSL sessions.[82](#fn82)

Beyond its CVSS score of 7.5, Heartbleed is important because of the popularity of OpenSSL, which at the time put an estimated 66% of active sites based on the market share of impacted web servers, and including 17% of SSL web servers using certificates issued by trusted authorities.[83](#fn83) In other words, Heartbleed put the secure connections used every day by web browsers around the world.

The vulnerability and the exploitation thereof are both relatively simple. The attacker simply provides a heartbeat to the SSL server, with a modified payload variable. By setting the payload_length to a value larger than the payload provided, the attacker tricks the server into copying additional bytes of memory into the heartbeat response. While this limits the data that can be obtained to what happens to be in memory at the time, this could include private keys, unencrypted messages, or other sensitive data.[84](#fn84)

### Log4j

In April 2022, a vulnerability in the popular java logging framework “Log4j” was disclosed with a CVSS score of 10 (the maximum severity score possible).[85](#fn85) Similar to Heartbleed, the extensive use of the Log4j package in many software applications put millions of software applications at risk of exploitation. Of particular note is that:

- 1. The vulnerability had existing for many years prior to discovery and disclosure
- 2. The vulnerability is exploitable, with evidence of wide-spread active exploitation.

The seriousness of Log4Shell has been widely acknowledged because of the simplicity of the exploitation and large attack surface it represents. The maximum CVSS score of 10 indicates that the vulnerability can be exploited easily, over the network, without authentication. Successful exploitation allows arbitrary code execution and can allow attackers to completely take control of target systems.[86](#fn86)

Log4j is used in a broad range of servers, network appliances, IoT devices, and even many cybersecurity appliances. As expressed by the Washington Post in, “The fact that log4j is such a ubiquitous piece of software is what makes this such a big deal. Imagine if a common type of lock used by millions of people to keep their doors shut was suddenly discovered to be ineffective. Switching a single lock for a new one is easy, but finding all the millions of buildings that have that defective lock would take time and an immense  amount of work.”[87](#fn87) It also makes the vulnerability a tempting target for attackers. According to Check Point software, 60 different variations of the original exploit were discovered in a single 24-h period immediately following the disclosure.[88](#fn88)

While initial attacks seemed primarily focused on bitcoin mining, there was evidence of state-backed hackers using the vulnerability to try to break into government and business targets as well.[89](#fn89)

### Ransomware and industrial control systems

Ransomware refers to malware that is intended to disable a system by encrypting some or all data on that system. Ransomware enables extortion of its victims via a promise of full system recovery once a payment has been made. If the attackers chose to honor that promise, fallowing the attacker can re-enable infected systems by providing decryption keys. Ransomware, like most cyberattacks, has evolved into more complex attack campaigns. They typically include attempts at lateral propagation, so that entire networks can be disabled in a coordinated fashion and may even seek to discover and disable online backup and recovery systems to make recovery more difficult. More recent campaigns often include various degrees of data theft, adding the threat of leaking sensitive information in an effort to increase the attacker's leverage over the victim.

Ransomware deserves some special consideration because it can be highly disruptive even if industrial systems are not infected. In 2021, Colonial Pipeline, an American oil pipeline that delivers fuel to much of the Southeastern United States, suffered a ransomware cyberattack that impacted computerized equipment managing the pipeline. While this was an IT incident and not an industrial control attack, the decision was made by Colonial Pipeline to shut down pipelines as a precaution to prevent ransomware from infecting industrial systems, which could have caused a much longer outage.[90](#fn90) The ransomware gang DarkSide, who was responsible for the attack, claimed no intention of disrupting critical infrastructure. The motive seemed limited to greed, with a reported $4.4 million ransom being paid.[91](#fn91)

Ransomware is obviously a threat against industrial operations even if the industrial networks were not at risk, simply because companies who operate industrial systems may be perceived as viable targets for financial extortion. The impact to the business systems and networks that supported the pipeline was sufficient to justify a manual shutdown of the operation. Some ransomware, such as Snake (also referred to as EKANS), specifically targets industrial systems. It leverages insecure configurations of RDP as a primary attack vector, likely with an understanding that RDP is widely used in many operational environments. The attack targets many specific processes, including ICS-and SCADA-specific processes, as well as remote management and Windows backups—presumably in order to disrupt process operations and inhibit recovery efforts.[92](#fn92) Ransomware that could infect actual process control assets, such as PLCs, RTUs, et. al., are also possible. Although no known examples of such an attack existed at the time of this writing, the malicious encryption of PLCs using a ransomware worm called “ LogicLocker” was demonstrated in 2017 by researchers at the Georgia Institute of Technology.[93](#fn93)

### Industrial application layer protocols

Adobe Reader exploits are highly relevant because many computing products—including ICS products—distribute manuals and other reference materials using PDF files and preinstall these on the ICS hosts. What is often the case as well is that the ICS software developers preinstall the Adobe Reader application, which oftentimes remains unpatched through traditional methods because it is not included with other vendor software update and hotfix notices. There are more directly relevant attacks that can occur at the application layer—industrial application attacks. Attack frameworks increasingly leverage these industrial protocols to achieve malicious outcomes. (See “Weaponized Industrial Cyber Threats,” above).

“Industrial applications” are the applications and protocols that communicate to, from, and between supervisory, control, and process system components. These applications serve specific purposes within the ICS, and by their nature are “vulnerable” because they are designed around control: either *direct* control of processes or devices (e.g., a PLC, RTU, or IED), or *indirect* control, via supervisory systems like a DCS or SCADA that are used by human operators to supervise and influence processes or devices.

Unlike typical application layer threats, such as in the case of Adobe Reader, industrial application layer threats do not always require that a specific vulnerability be exploited. This is because these applications are designed for the purpose of influencing industrial control environments. They do not need to be infected with malware in order to gain the control necessary to cause harm, since they can simply be used as they are designed but with malicious intent. By issuing legitimate commands, between authorized systems and in full compliance with protocol specifications, an ICS can be told to perform a function that is outside of the owner's intended purpose and parameters. This method can be thought of as the *exploitation of functionality* and when considered in the context of ICS security represents a problem that is not typically addressed through traditional IT security controls.

Digital Bond published one example of an industrial application layer attack in 2012 under the project name “Basecamp.” The research documented how the EtherNet/IP protocol could be manipulated to control a Rockwell Automation ControlLogix PLC. It should be noted that it was not a ControlLogix vulnerability that was exploited, but the underlying protocol, and as such, this exploit is widely applicable due to the prevalence of the EtherNet/IP protocol in ICS supplied by various vendors. A number of attack methods were disclosed, all sharing the common exploitation of EtherNet/IP:[94](#fn94)

1. • **Forcing a system stop.** This attack effectively shuts off the CIP service and renders the device dead by sending a CIP command to the device. This puts the device into a “major recoverable fault” state.[95](#fn95)
2. 
3. • **Crashing the CPU.** This attack crashes the CPU due to a malformed CIP request, which cannot be effectively handled by the CIP stack. The result is also a “major recoverable fault” state.[96](#fn96)
4. • **Dumping device boot code.** This is a CIP function that allows an EtherNet/IP device's boot code to be remotely dumped.[97](#fn97)
5. • **Reset device.** This is a simple misuse of the CIP system reset function. The attack resets the target device.[98](#fn98)
6. • **Crash device.** This attack crashes the target device due to a vulnerability in the device's CIP stack.[99](#fn99)
7. • **Flash update.** CIP, like many industrial protocols, supports writing data to remove devices, including register and relay values, but also files. This attack misuses this capability to write new firmware to the target device.[100](#fn100)

EtherNet/IP is not the only protocol that can be exploited in this way. In 2013, Adam Crain of Automatak and independent researcher Chris Sistrunk reported a vulnerability with certain implementations of the DNP3 protocol stack, which was found to impact DNP3 master and outstation (slave) devices from a large number of known vendors. The weakness was an input validation vulnerability received from a DNP outstation station that could put the master station into an infinite loop condition.[101](#fn101) This was not a specific device vulnerability, but a larger vulnerability concerning the implementation of a protocol stack, and because many vendors utilized a common library, it impacted a large number of products from multiple vendors. Of particular concern is that this vulnerability can be exploited via TCP/IP (by someone who has gained logical network access) or serially (by someone who has gained physical access to a DNP3 outstation).

Both of these examples represent weaknesses in protocols that were designed decades ago and are now being faced with new security challenges that were unforeseen at the time of their development. Since these also involve community-led open-source or licensed protocols that are not managed by a single vendor, their deployment can be very wide spread making it difficult to deploy patches and hotfixes that can be implemented in a timely manner. While vulnerabilities of this type are cause for concern, they can typically be mitigated through proper network and system design and through the implementation of appropriate cybersecurity controls (which, hopefully, is why you are reading this book). To put this another way, it is going to be a lot easier and less costly to deploy appropriate security controls to mitigate the risk from these open protocols versus attempting to retrofit and/or replace the affected ICS equipment.

An easy way to look at this is though the ICS devices themselves may be “insecure by design,” the overall ICS can be sufficiently secured from cyber threats using a “secure by redesign” approach, rather than a “secure by replacement” one. After all, a “secure” device today could likely have vulnerabilities disclosed in the future that makes it “insecure” at that time. This is why industrial security is always focused on the holistic “system-level” security rather than that of individual ICS components.

#### Antisocial networks: A new playground for malware

While social networks do not seem to have a lot to do with industrial networks (there should never be open connectivity to the Internet from an industrial zone, and certainly not to social networking sites), it is surprisingly relevant. Social networking sites are increasingly popular, and they can represent a serious risk against industrial networks. How can something as benign as Facebook or Twitter be a threat to an industrial network? Social networking sites are designed to make it easy to find and communicate with people, and people are subject to social engineering exploitation just as networks are subject to protocol and application exploitation.

They are at the most basic level a source of gathering personal information and end user's trust that can be exploited either directly or indirectly. At a more sophisticated level, social networks can be used actively by malware as a C2 channel. Fake accounts posing as “trusted” coworkers or business colleagues can lead to even more information sharing or provide a means to trick the user into clicking on a link that will take them to a malicious website that will infect the user's computer with malware. That malware could mine additional information, or it could be walked into a “secure” facility to impact an industrial network directly. Even if a company has strict policies on the use of laptops accessing such websites are these same companies as strict with the laptops used by their vendors and service subcontractors when connected to these same industrial networks? These same vendor/subcontractor computers are commonly connected directly to secure industrial networks. This is why it is equally important to consider the “insider” threats, and not focus entirely on external “outsider” originated attacks.

No direct evidence exists that links the rise in web-based malware and social networking adoption; however, the correlation is strong enough that any good security plan should accommodate social networking, especially in industrial networks. According to Cisco, “Companies in the Pharmaceutical and Chemical vertical were the most at risk for web-based malware encounters, experiencing a heightened risk rating of 543% in 2Q10, up from 400% in 1Q10. Other higher-risk verticals in 2Q10 included energy, oil, and gas (446%), education (157%), government (148%), and transportation and shipping (146%).”[102](#fn102)

Apart from being a direct infection vector, social networking sites can be used by more sophisticated attackers to formulate targeted spear-phishing campaigns, such as the “pizza delivery” exercise. Users may postpersonal information about where they work, what their shift is, who their boss is, and other details that can be used to engineer a social exploitation through no direct fault of the social network operators (most have adequate privacy controls in place). Spear phishing is already a proven tactic, yet it is easier and even more effective when combined with the additional trust associated with social networking communities.

TipSecurity awareness training is an important part of building a strong security plan, but it can also be used to assess current defenses. Conduct this simple experiment to both increase awareness of spear phishing and gauge the effectiveness of existing network security and monitoring capabilities:- 1. Create a website using a free hosting service that displays a security awareness banner.
- 2. For this exercise, create a Google Mail account using the name (modified if necessary) of a group manager, HR director, or the CEO of your company (again, disclosing this activity to that individual in advance and obtaining necessary permissions). Assume the role of an attacker, with no inside knowledge of the company; look for executives who are quoted in press releases, or listed on other public documents. Alternately, use the Social Engineering Toolkit (SET), a tool designed to “perform advanced attacks against the human element,” to launch a more thorough social engineering penetration test.
- 3. Again, play the part of the attacker and use either SET or outside means, such as [Jigsaw.com](http://Jigsaw.com) or other business intelligence websites, to build a list of email addresses within the company.
- 4. Send an email to the group from the fake “executive” account, informing recipients to please read the attached article in preparation for an upcoming meeting.
- 5. Perform the same experiment on a different group, using an email address originating from a peer (again, obtain necessary permissions). This time, attempt to locate a pizza restaurant local to your corporate offices, using Google map searches or similar means, and send an email with a link to an online coupon for buy-one-get-one-free pizza.

Track your results to see how many people clicked through to the offered URL. Did anyone validate the “from” in the email, reply to it, or question it in any way? Did anyone outside of the target group click through, indicating a forwarded email?Finally, with the security monitoring tools that are currently in place, is it possible to effectively track the activity? Is it possible to determine who clicked through (without looking at web logs)? Is it possible to detect abnormal patterns or behaviors that could be used to generate signatures and detect similar phishing in the future?The best defense against a social network attack continues to be security and situational awareness. Security awareness helps prevent a socially engineered attack from succeeding by establishing best-practice behaviors among personnel. Situational awareness helps to detect if and when a successful breach has occurred, where it originated, and where it may have spread to—in order to minimize the damage or impact from the attack and mitigate or remediate any gaps uncovered in security awareness and training.

Social networks can be used as a C2 channel between deployed malware and a remote server. One case of Twitter being used to deliver commands to a bot is the @upd4t3 channel, first detected in 2009 that uses standard 140-character tweets to link to base64-encoded URLs that deliver infosteeler bots.[103](#fn103)

CautionAlways inform appropriate personnel of any security awareness exercise to avoid unintended consequences and/or legal liability, and NEVER perform experiments of this kind using real malware. Even if performed as an exercise, the collection of actual personal or corporate information could violate your employment policy or even state, local, or federal privacy laws.This use of social networking as a malicious vector is difficult to detect, as it is not feasible to scour these sites individually for such activity, and there is no known way to detect what the C2 commands may look like or where they might be found. Application session analysis on social networking traffic could detect the base64 encoding once a session was initiated in the case of @upd4t3. The easiest way to block this type of activity, of course, is to block access to social networking sites completely from inside industrial networks. The wide adoption of these sites within the enterprise (for legitimate sales, marketing, and even business intelligence purposes) however makes it highly likely that any threat originating from or directly exploiting social networks can and will compromise the business enterprise. Special security considerations must be employed for this reason when evaluating the risk an organization faces from social networking.

### Polymorphic and adaptive malware

Polymorphic or metamorphic malware is malware with mutation logic capable of adapting its own code, typically in response to external variables. Adaptive malware uses conditional logic to direct activity based on its surroundings until it finds itself in the perfect conditions in which it will best accomplish its goal (spread, stay hidden, deploy a weapon, etc.).

Polymorphic malware often uses mutations to avoid detection: for example, to eliminate malicious code in response to detection attempts. Most modern advanced malware frameworks have both mutation and adaptation capabilities.

Once again, Stuxnet provides a solid example. The goal of Stuxnet was to find a particular ICS by spreading widely through local networks and “sneaker” networks. It then only took secondary infection measures when the target environment (Siemens SIMATIC WinCC/PCS7) was found. It then checked for particular PLC models and versions (Siemens models S7-315-2 and S7-417). Once these models were discovered, it looked for a specific make and model of VFDs (Fararo Paya model KFC750V3 and Vacon NX) before it injected process code into the PLC. If unsuitable targets were infected, it would lay dormant waiting for other hosts to infect.

Malware mutations are also already in use. Stuxnet at a basic level will update itself in the wild (even without a C2 connection), through peer-to-peer checks with other hosts also infected, and if a newer version of Stuxnet bumps into an older version, it updates the older version allowing the infection pool to evolve and upgrade in the wild.[104](#fn104)

Further mutation behavior involves self-destruction of certain code blocks with self-updates of others, effectively morphing the malware and making it more targeted as well as more difficult to detect. Mutation logic may include checking for the presence of other well-known malware and adjusting its own profile to utilize similar ports and services knowing that this new profile will go undetected. In other words, malware is getting smarter and at the same time, harder to detect.

### Dealing with an infection

Ironically, upon detecting an infection, you may not want to immediately clean the system of infected malware. This is because there may be subsequent levels of infection that exist yet are dormant and may be activated as a result. There could also be valuable information, such as the infection path used and other compromised hosts as in the case of Stuxnet. A thorough investigation should instead be performed, with the same sophistication as the malware itself.

The first step should be to logically isolate the infected host so that it can no longer cause any harm. Harm to not only other logical assets that may be on the shared network but also the physical assets that the ICS host may be controlling. Allow the malware to communicate over established C2 channels but isolate the host from the rest of the network and remove all access between that host and any sensitive or protected information. A well-established network segmentation philosophy based on common security criteria needs to be deployed in order to effectively isolate infected hosts. This topic is covered further in [Chapter 5](../B9780443137372000038/CH0005_91-128_B9780443137372000038.xhtml), “Industrial Network Design and Architecture” and [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits.” Collect as much forensic detail as possible in the form of system logs, captured network traffic, supplementing where possible with memory analysis data. Important information can be gathered that may result in the successful removal of the infection by effectively sandboxing the infected system.

When you suspect that you are dealing with an infection, approach the situation with diligence and perform a thorough investigation:

1. • Remember to consider the safe and reliable operation of the manufacturing process as the primary objective. Extra care must be given to ICS components in their operating mode for this reason, and is why it is important to have a documented and rehearsed incident response plan in place.
2. • Always monitor everything, collecting baseline data, configurations, and firmware for comparison.
3. • Analyze available logs to help identify scope, infected hosts, propagation vectors, and so on. Logs should be retrieved from as many components on the network as possible, including those that have not been compromised.
4. • Sandbox and investigate infected systems.
5. • Be careful to not unnecessarily power-down infected hosts, and valuable information may be resident in volatile memory.
6. 
7. • Analyze memory to find memory-resident rootkits and other threats that may be residing in user memory.
8. • Clone disk images when possible to preserve as much of the original state as possible for off-line analysis.
9. • Reverse engineer-detected malware to determine full scope and to identify additional attack vectors and possible propagation.
10. • Retain all information for disclosure to authorities.

NoteInformation collected from an infected and sandboxed host may prove valuable to legal authorities, and depending upon the nature of your industrial network, you may be required to report this information to a governing body.A “bare metal reload” may be necessary where a device is completely erased and reduced to a bare, inoperable state depending on the severity of the infection. The host's hardware must then be reimaged completely. Clean versions of operating systems, applications, and asset firmware should be kept in a safe, clean environment for this reason. This can be accomplished using secure virtual backup environments, or via secure storage on trusted removable media that can then be stored in a locked cabinet, preferably in a separate physical location from the asset archived. It is important to ensure that the images used for system restoration are free and clean of any malware or malicious code that may have triggered the initial incident when using a backup and recovery system.

TipThe ability to perform forensics on a compromised system can be an advanced task. To help in this, the National Institute of Standards and Technology has established the Computer Forensics Tool Testing (CFTT) project and offers a “Computer Forensics Tool Catalog.” Information can be found at: http://www.cftt.nist.gov.TipIf you think you have an infection, you should know that there are security firms that are experienced in investigating and cleaning advanced malware infections. Many such firms further specialize in industrial control networks. Before allowing anyone access to your ICS assets, it is encouraged to request and validate actual system experience—preferably on an ICS similar to yours. These firms can help you deal with infection as well as provide an expert interface between your organization and any governing authorities that may be involved.
## Summary

Cyberthreats are increasing at an alarming rate, making the technologies that everyone now takes for granted the easy criminal path into theft, espionage, and sabotage. Industrial control systems account for less than 1% of the total vulnerabilities listed by the OSVDB, yet the trends associated with ICS cyber-attacks should be alarming. The rate of cyberincidents directly impacting industrial systems has been steadily increasing over the past 30 years according to the Repository of Industrial Security Incidents (RISI).[105](#fn105) RISI's analysis also reveals that, although malware infections still account for a large number of cyberevents (28% in 2013), it has been steadily decreasing over the past 5 years indicating that ICS users are becoming more aware of the methods to provide malware from affecting ICS architectures. These data also confirm that the vectors involved in ICS cyberevents are shifting to more sophisticated mechanisms that are able to avert detection by traditional defenses, pivot through segmented networks, and exploit weaknesses in the underlying design of the ICS architecture.

Anyone who believes that they can prevent 100% of the possible cyberevents within a particular system is misinformed and likely to be disappointed. A well-rounded cybersecurity program is based on a thorough understanding of the threats that face industrial architectures, and blends security defenses that not only focus on event prevention but also postbreach detection and forensic capabilities to contain an event and minimize as best as possible the negative consequences to the manufacturing or industrial process that the ICS is designed to control.

---

[1](#cfn1)  K. Stouffer, J. Falco, K. Scarfone, National Institute of Standards and Technology, Special Publication 800-82 (Final Public Draft), Guide to Industrial Control Systems (ICS) Security, Computer Security Division, Information Technology Laboratory, National Institute of Standards and Technology Gaithersburg, MD and Intelligent Systems Division, Manufacturing Engineering Laboratory, National Institute of Standards and Technology Gaithersburg, MD, September 2008.

[2](#cfn2)  M.J. McDonald, G.N. Conrad, T.C. Service, R.H. Cassidy, SANDIA Report SAND2008-5954, Cyber Effects Analysis Using VCSE Promoting Control System Reliability, Sandia National Laboratories Albuquerque, New Mexico and Livermore, California, September 2008.

[3](#cfn3)  A. Giani, S. Sastry, K.H. Johansson, H. Sandberg, The VIKING Project: An Initiative on Resilient Control of Power Networks, Department of Electrical Engineering and Computer Sciences, University of California at Berkeley, and School of Electrical Engineering, Royal Institute of Technology (KTH), Berkeley, CA, 2009.

[4](#cfn4)  MITRE ATT&CK. Document from the Internet, cited March 15, 2023. [https://attack.mitre.org/resources/getting-started/](https://attack.mitre.org/resources/getting-started/)

[5](#cfn5)  Andy Greenberg. How Hackers Can Use ‘Evil Bubbles’ to Destroy Industrial Pumps. Wired. July 29, 2017.

[6](#cfn6)  Honeywell Forge. Honeywell Cybersecurity Report: USB Hardware Attack Platforms. October 2020. Honeywell, Inc.

[7](#cfn7)  Ibid.

[8](#cfn8)  mg.O.MG Keylogger Cable. 7 August 2020. [https://mg.lol/blog/keylogger-cable/](https://mg.lol/blog/keylogger-cable/)

[9](#cfn9)  Dillon Beresford. Exploiting Siemens SIMATIC S7 PLCs. Prepared for Black Hat USA+2011. Las Vegas, NV. 2011.

[10](#cfn10)  Ralph Langner. Forensics on a complex cyber attack – lessons learned from Stuxnet. Presentation at the 2011 Applied Control Solutions (ACS) Conference. September 20, 2011. Washington, DC.

[11](#cfn11)  Dillon Beresford. Exploiting Siemens SIMATIC S7 PLCs. Prepared for Black Hat USA+2011. Las Vegas, NV. 2011.

[12](#cfn12)  Dillon Beresford. Exploiting Siemens SIMATIC S7 PLCs. Prepared for Black Hat USA+2011. Las Vegas, NV. 2011.

[13](#cfn13)  SearchSecurity. Definition: Blended Threat. Document from the Internet. Cited Sep 4, 2012. Available from: [http://searchsecurity.techtarget.com/definition/blended-threat](http://searchsecurity.techtarget.com/definition/blended-threat)

[14](#cfn14)  G. McDonald, L.O. Murchu, S. Doherty, E. Chien, Symantec. Stuxnet 0.5: The Missing Link, Version 1.0, February 26, 2013.

[15](#cfn15)  Ibid.

[16](#cfn16)  Ind.ustrial Control Systems Cyber Emergency Response Team (ICS-CERT), ICSA-10-238-01—STUXNET MALWARE MITIGATION, Department of Homeland Security, US-CERT, Washington, DC, August 26, 2010.

[17](#cfn17)  E. Chien, Symantec. Stuxnet: a breakthrough., November 2010 (cited: November 16, 2010).

[18](#cfn18)  Open-Source Vulnerability Database (OSVDB). ID 66,441: Siemens SIMATIC WinCC SQL Database Default Password. (cited: December 20, 2013).

[19](#cfn19)  WinCC Database Problem. (cited: December 20, 2013).

[20](#cfn20)  N. Falliere, L.O Murchu, E. Chien, Symantec. W32.Stuxnet Dossier, Version 1.1, October 2010.

[21](#cfn21)  E. Byres, A. Ginter, J. Langill. “How Stuxnet Spreads - A Study of Infection Paths in Best Practice Systems,” Version 1.0, February 22, 2011.

[22](#cfn22)  ICS-CERT. Joint Security Awareness Report (JSAR-12-241-01B) Shamoon/DistTrack Malware - Update B. Document from the Internet. April 30, 2013. Cited December 22, 2013. Available at: [https://ics-cert.us-cert.gov/jsar/JSAR-12-241-01B-0](https://ics-cert.us-cert.gov/jsar/JSAR-12-241-01B-0)

[23](#cfn23)  Ibid.

[24](#cfn24)  Kelly Jackson Higgins. 30,000 Machines Infected In Targeted Attack On Saudi Aramco. Dark Reading. August 2012. Document from the Internet. Cited December 22, 2013. Available at: [http://www.darkreading.com/attacks-breaches/30000-machines-infected-in-targeted-atta/240006313](http://www.darkreading.com/attacks-breaches/30000-machines-infected-in-targeted-atta/240006313)

[25](#cfn25)  Kaspersky Labs. Virus News: Kaspersky Lab Experts Provide In-Depth Analysis of Flame's C&C Infrastructure. Document from the Internet. June 4, 2012. Cited Sep 18, 2012. Available from: [http://www.kaspersky.com/about/news/virus/2012/Kaspersky_Lab_Experts_Provide_In_Depth_Analysis_of_Flames_Infrastructure](http://www.kaspersky.com/about/news/virus/2012/Kaspersky_Lab_Experts_Provide_In_Depth_Analysis_of_Flames_Infrastructure)

[26](#cfn26)  Kaspersky Labs. Virus News: Kaspersky Lab Experts Provide In-Depth Analysis of Flame's C&C Infrastructure. Document from the Internet. June 4, 2012. Cited Sep 18, 2012. Available from: [http://www.kaspersky.com/about/news/virus/2012/Kaspersky_Lab_Experts_Provide_In_Depth_Analysis_of_Flames_Infrastructure](http://www.kaspersky.com/about/news/virus/2012/Kaspersky_Lab_Experts_Provide_In_Depth_Analysis_of_Flames_Infrastructure)

[27](#cfn27)  “Dragonfly: Cyberespionage Attacks Against Energy Suppliers,” Symantec Security Response v.1.21, July 7, 2014 (v1.0 first published June 30, 2014).

[28](#cfn28)  Ibid.

[29](#cfn29)  Ibid.

[30](#cfn30)  Joel T. Langill. Defending Against the Dragonfly Cyber Security Attacks. Belden. Oct. 22, 2014.

[31](#cfn31)  “Dragonfly: Cyberespionage Attacks Against Energy Suppliers,” Symantec Security Response v.1.21, July 7, 2014 (v1.0 first published June 30, 2014).

[32](#cfn32)  Ibid.

[33](#cfn33)  Ibid.

[34](#cfn34)  “IR-ALERT-H-16-043-01AP Cyber-Attack Against Ukrainian Critical infrastructure,” US Department of Homeland Security Industrial Control System Computer Emergency Response Team, March 7, 2016, accessed July 12, 2016, [https://info.publicin-telligence.net/NCCIC-UkrainianPowerAttack.pdf](https://info.publicin-telligence.net/NCCIC-UkrainianPowerAttack.pdf)

[35](#cfn35)  Ake Styczynski, Nate Beach–Westmoreland. When The Lights Went Out: A Comprehensive Review of the 2015 Attacks on Ukrainian Critical Infrastructure. Booz Allen Hamilton Inc. 2019.

[36](#cfn36)  “IR-ALERT-H-16-043-01AP Cyber-Attack Against Ukrainian Critical infrastructure,” US Department of Homeland Security Industrial Control System Computer Emergency Response Team, March 7, 2016, accessed July 12, 2016, [https://info.publicin-telligence.net/NCCIC-UkrainianPowerAttack.pdf](https://info.publicin-telligence.net/NCCIC-UkrainianPowerAttack.pdf)

[37](#cfn37)  Ibid.

[38](#cfn38)  Ibid.

[39](#cfn39)  Ibid.

[40](#cfn40)  Ibid.

[41](#cfn41)  Ibid.

[42](#cfn42)  Ibid.

[43](#cfn43)  Ibid

[44](#cfn44)  Ake Styczynski, Nate Beach–Westmoreland. When The Lights Went Out: A Comprehensive Review of the 2015 Attacks on Ukrainian Critical Infrastructure. Booz Allen Hamilton Inc. 2019.

[45](#cfn45)  Ibid.

[46](#cfn46)  Ibid.

[47](#cfn47)  Ibid.

[48](#cfn48)  Ibid.

[49](#cfn49)  Ibid.

[50](#cfn50)  Ibid.

[51](#cfn51)  Ibid.

[52](#cfn52)  Ibid.

[53](#cfn53)  Cherepanov, Anton. “Industroyer: Biggest threat to industrial control systems since Stuxnet”. [www.welivesecurity.com](http://www.welivesecurity.com). ESET. June 17, 2017.

[54](#cfn54)  Ibid.

[55](#cfn55)  Ibid.

[56](#cfn56)  Dragos, Inc. TRISIS Malware Analysis of Safety System Targeted Malware. December 2017.

[57](#cfn57)  Ibid.

[58](#cfn58)  Ibid.

[59](#cfn59)  Ibid.

[60](#cfn60)  Ibid.

[61](#cfn61)  Honeywell, Inc. Global Analysis Research and Defense Report: Industrial Cybersecurity USB Threat Report 2020. July 2020.

[62](#cfn62)  Daniel Kapellmann Zafra, Raymond Leong, Chris Sistrunk, Ken Proska, Corey Hildebrandt, Keith Lunden, Nathan Brubaker, “INDUSTROYER.V2: Old Malware Learns New Tricks”. April 25, 2022. Updated December 02, 2022. Mandiant. [https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)

[63](#cfn63)  Welivesecurity, by ESET. “Industroyer2: Industroyer reloaded This ICS-capable malware targets a Ukrainian energy company”. April 12, 2022. ESET Research. [https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/)

[64](#cfn64)  Ibid.

[65](#cfn65)  Daniel Kapellmann Zafra, Raymond Leong, Chris Sistrunk, Ken Proska, Corey Hildebrandt, Keith Lunden, Nathan Brubaker, “INDUSTROYER.V2: Old Malware Learns New Tricks”. April 25, 2022. Updated December 02, 2022. Mandiant. [https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)

[66](#cfn66)  Nathan Brubaker, Keith Lunden, Ken Proska, Muhammad Umair, Daniel Kapellmann Zafra, Corey Hildebrandt, Rob Caldwell. “INCONTROLLER: New State-Sponsored Cyber Attack Tools Target Multiple Industrial Control Systems”. Mandiant. April 13, 2022. Cited March 2022. [https://www.mandiant.com/resources/blog/incontroller-state-sponsored-ics-tool](https://www.mandiant.com/resources/blog/incontroller-state-sponsored-ics-tool)

[67](#cfn67)  Ibid.

[68](#cfn68)  Ibid.

[69](#cfn69)  Ibid.

[70](#cfn70)  Ibid.

[71](#cfn71)  Ibid.

[72](#cfn72)  Rob Lee. (February 2023). PIPEDREAM – Most Flexible & Capable ICS Malware To Date [Conference presentation]. S4X23 2023 Conference. Miami, FL, United States. [https://www.youtube.com/watch?v=H82sbIwFxt4](https://www.youtube.com/watch?v=H82sbIwFxt4)

[73](#cfn73)  Nathan Brubaker, Keith Lunden, Ken Proska, Muhammad Umair, Daniel Kapellmann Zafra, Corey Hildebrandt, Rob Caldwell. “INCONTROLLER: New State-Sponsored Cyber Attack Tools Target Multiple Industrial Control Systems”. Mandiant. April 13, 2022. Cited March 2022. [https://www.mandiant.com/resources/blog/incontroller-state-sponsored-ics-tool](https://www.mandiant.com/resources/blog/incontroller-state-sponsored-ics-tool)

[74](#cfn74)  Nir Nissim, Ran Yahalom, Yuval Elovici, “USB-based attacks” Computers & Security, Volume 70, 2017. [https://doi.org/10.1016/j.cose.2017.08.002](https://doi.org/10.1016/j.cose.2017.08.002)

[75](#cfn75)  Honeywell, Inc. Global Analysis Research and Defense Report: Industrial Cybersecurity USB Threat Report 2022. August 2022.

[76](#cfn76)  D. Stevens, Escape from PDF., March 2010 (cited: November 4, 2010).

[77](#cfn77)  J. Conway, [Sudosecure.net](http://Sudosecure.net). Worm-Able PDF Clarification., April 4, 2010 (cited: November 4, 2010).

[78](#cfn78)  86 Security Labs, PDF “Launch” Feature Used to Install Zeus., April 14, 2010 (cited: November 4, 2010).

[79](#cfn79)  “Frequently Asked Questions: Word Macro Viruses”. Microsoft. Archived from the original on 2011-06-04. Retrieved 2006-06-18.

[80](#cfn80)  Microsoft. “Macro Malware”. [https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/macro-malware?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/macro-malware?view=o365-worldwide)

[81](#cfn81)  OpenSSL Security Advisory [07 Apr 2014] [https://www.openssl.org/news/secadv/20140407.txt](https://www.openssl.org/news/secadv/20140407.txt)

[82](#cfn82)  Goodin, Dan (8 April 2014). “Critical crypto bug in OpenSSL opens two-thirds of the Web to eavesdropping”. Ars Technica. Archived from the original on 5 July 2017. Retrieved 14 June 2017.

[83](#cfn83)  Mutton, Paul (8 April 2014). “Half a million widely trusted websites vulnerable to Heartbleed bug”. Netcraft. Archived from the original on 19 November 2014. Retrieved 24 November 2014.

[84](#cfn84)  Robert Erbes, IOActive Insights. “Bleeding Hearts”. APRIL 10, 2014. [https://ioactive.com/bleeding-hearts/](https://ioactive.com/bleeding-hearts/)

[85](#cfn85)  “Apache Log4j Security Vulnerabilities”. Log4j. Apache Software Foundation. Retrieved 12 December 2021.

[86](#cfn86)  CISA. National Vulnerability Database, CVE2021-44,228 vulnerability detail. [https://nvd.nist.gov/vuln/detail/CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)

[87](#cfn87)  Hunter, Tatum; de Vynck, Gerrit (20 December 2021). “The ‘most serious’ security breach ever is unfolding right now. Here's what you need to know”. The Washington Post.

[88](#cfn88)  “Protect Yourself Against The Apache Log4j Vulnerability” CheckCheck Point Software Technologies. [https://blog.checkpoint.com/2021/12/11/protecting-against-cve-2021-44228-apache-log4j2-versions-2-14-1/](https://blog.checkpoint.com/2021/12/11/protecting-against-cve-2021-44228-apache-log4j2-versions-2-14-1/). Last updated: 20.12.2021 01:30 a.m. PST. Initially published: 10.12.2021.

[89](#cfn89)  Hunter, Tatum; de Vynck, Gerrit. “The ‘most serious’ security breach ever is unfolding right now. Here's what you need to know”. The Washington Post. 20 December 2021.

[90](#cfn90)  Sergiu Gatlan, Colonial Pipeline reports data breach after May ransomware attack. Bleeping Computer. August 16, 2021.

[91](#cfn91)  Robertson, Jordan; Turton, William (May 8, 2021). “Colonial Hackers Stole Data Thursday Ahead of Shutdown”. Bloomberg News. Archived from the original on May 9, 2021. Retrieved May 9, 2021.

[92](#cfn92)  Alexander Ivanyuk Snake/EKANS Ransomware Attacks Industrial Control Systems: Acronis Stops It. Acronis. February 10, 2020.

[93](#cfn93)  Formby, D., Durbha, S., & Beyah, R. (n.d.). Out of Control: Ransomware for Industrial Control Systems. Retrieved from [http://www.cap.gatech.edu/plcransomware.pdf](http://www.cap.gatech.edu/plcransomware.pdf)

[94](#cfn94)  Ruben Santamarta. Attacking ControlLogix. Digital Bond Project Base Camp. 2012.

[95](#cfn95)  Ibid.

[96](#cfn96)  Ibid.

[97](#cfn97)  Ibid.

[98](#cfn98)  Ibid.

[99](#cfn99)  Ibid.

[100](#cfn100)  Ibid.

[101](#cfn101)  Advisory (ICSA-13-291-01). DNP3 Implementation Vulnerability. ICS-CERT. Original release date: November 21, 2013.

[102](#cfn102)  Cisco Systems, 2Q10 Global Threat Report, 2010.

[103](#cfn103)  Nazario, Arbor networks. Twitter-based Botnet Command Channel., August 13, 2009 (cited: November 4, 2010).

[104](#cfn104)  J. Pollet, Red Tiger, Understanding the advanced persistent threat, in: Proc. 2010 SANS European SCADA and Process Control Security Summit, Stockholm, Sweden, October 2010.

[105](#cfn105)  Report “2013 Report on Cyber Security Incidents and Threats Affecting Industrial Control Systems,” Repository of Industrial Security Incidents (RISI), Published June 15, 2013.
