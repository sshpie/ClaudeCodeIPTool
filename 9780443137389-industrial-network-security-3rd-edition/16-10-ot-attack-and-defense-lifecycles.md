# 10: OT Attack and Defense Lifecycles

## Abstract

Malware has been around since the dawn of personal computing: the first virus being the Creeper virus in 1971, a proof-of-concept virus that spread through ARPANET-connected computers,1 and the first personal computer being attributed to the Kenbak-1 computer2 also in 1971. However, malware has advanced significantly since then, and cyberattacks very rarely depend on a single piece of malware. Instead they have evolved into campaigns that consist of multiple steps. Instead of singular actions that result in a single outcome, attack campaigns coordinate multiple actions to produce a more sophisticated outcome. The sophistication of both attack and defense techniques have grown to a degree where each involves multiple steps that occur, intertwined in a dance of attack and defense. The stronger the defense posture of an organization, the more sophisticated the moves of the attacker must become. Likewise, when faced with a more capable attacker, the defender must be able to anticipate the next move in order to prevent it or be well positioned to react quickly if it cannot be prevented. This is only possible with an understanding of how both attack and defense efforts progress.

### Keywords

Attack Lifecycles; Cyberattack; Industrial network; Kill Chain; MITREInformation in this chapter• Attack Lifecycles and Kill Chains• Defense Lifecycles• The Importance of Understanding LifecyclesMalware has been around since the dawn of personal computing: the first virus being the Creeper virus in 1971, a proof-of-concept virus that spread through ARPANET-connected computers[1](#fn1), and the first personal computer being attributed to the Kenbak-1 computer[2](#fn2) also in 1971. However, malware has advanced significantly since then, and cyberattacks very rarely depend on a single piece of malware. Instead they have evolved into campaigns that consist of multiple steps. Instead of singular actions that result in a single outcome, attack campaigns coordinate multiple actions to produce a more sophisticated outcome. The sophistication of both attack and defense techniques has grown to a degree where each involves multiple steps that occur, intertwined in a dance of attack and defense. The stronger the defense posture of an organization, the more sophisticated the moves of the attacker must become. Likewise, when faced with a more capable attacker, the defender must be able to anticipate the next move in order to prevent it or be well positioned to react quickly if it cannot be prevented. This is only possible with an understanding of how both attack and defense efforts progress.

## Attack lifecycles and kill chains

The many steps of an attack that “enable access and provide sufficient information to devise an effect”[3](#fn3) are often referred to as a campaign. SANS analysts Michael J. Asante and Robert M. Lee,[4](#fn4) have framed the attack campaign within the “Cyber Kill Chain” model, which is a military model originally created by Eric M. Hutchins, Michael J. Cloppert, and Rohan M. Amin of Lockheed Martin.[5](#fn5) The result is a two-phase attack lifecycle: to create a cyber-physical outcome, the attacker must first breach the industrial network; and then begin the second phase of executing a cyber-physical attack on the industrial control system itself.[6](#fn6) Each of these phases is a dance of its own, with a necessary progression from the initial planning to the final execution.

Phase 1 obtaining access to industrial networks[7](#fn7)

- 1. Planning (reconnaissance)
- 2. Preparation (Weaponization, targeting)
- 
- 3. Intrusion (Delivery, exploitation, installation and modification)
- 4. Enablement (Command and Control, or C2)
- 5. Execution (Action)

Phase 2 manipulation of industrial networks[8](#fn8)

- 1. Attack Development & Tuning (Develop)
- 2. Validation (Test)
- 3. Industrial Control System Attack (Deliver, Install/Modify, and ICS Attack Execution)

It can be helpful to visualize each phase of an attack as a linear progression, as illustrated in Figures [10.2](#f0015) and [10.3](#f0020). Each step within each phase takes time, and each step must be completed to some degree of efficacy before the next stage can begin.

Understanding this progression can be extremely helpful as defenders need to respond differently as an attack proceeds. Knowing how far the attack has already progressed, and what the next necessary steps are likely to be, helps the defender to make more informed decisions (see “Defensive Lifecycles” below). If, in doing so, a defender can prevent an adversary from completing a necessary step within the attack lifecycle, it may be possible to prevent an incident entirely. If a defender is able to force an attacker to rush through important steps, the attack may be less effective. For example, by interrupting or hindering C2 communications during “enablement,” the defender could prevent the attacker from obtaining data needed to fully develop and validate their attack before executing it ([Figure 10.1](#f0010)).

In practice, “understanding where an attacker is within the progression of the attack lifecycle” is not always obvious. As a defender, we do not always see what an attacker is  intending to do; we only see evidence of their actions (and only if there are detection and monitoring tools in place to allow us to see). To make this easier, there is another important model that should be considered: the MITRE ATT&CK frameworks. The ATT&CK frameworks map attack behaviors to specific stages of an attack lifecycle. The frameworks are described by MITRE as a “curated knowledge base for cyber adversary behavior” that are specifically designed to illustrate the various stages of the attack lifecycle,[9](#fn9) and there are three frameworks available at the time of this writing—one for enterprise, mobile, and ICS attacks. Each focuses on the specific tactics and techniques used against these target categories.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-01-9780443137372.jpg)

*[Figure 10.1](#Bf0010)  Initial attack phase of a cyber-physical kill chain.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-02-9780443137372.jpg)

*[Figure 10.2](#Bf0015)  Industrial attack phase of a cyber-physical kill chain.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-03-9780443137372.jpg)

*[Figure 10.3](#Bf0020)  Mapping kill chain ICS attack phases to MITRE ATT&CK stages.*

Unlike the Kill Chain model, the ATT&CK frameworks go into significantly more detail, providing the specific techniques used by an attacker. While this makes ATT&CK more complex, it also makes it extremely useful in day-to-day security management and response efforts. This is because ATT&CK tactics and techniques can be mapped directly to specific security events and indicators of compromise. In fact, many cybersecurity monitoring tools (i.e., SIEM) will map events to the ATT&CK framework automatically, letting cybersecurity professionals immediately gain the context of the attack progression.

The two ATT&CK frameworks that are relevant here (ATT&CK for enterprise and ATT&CK for ICS) can be loosely mapped to Purdue levels 2 through 4 and 0 through 2 respectively and can also be loosely mapped loosely to the initial- and industrial-attack phases referenced in the Kill Chain model.[10](#fn10) In other words, the ATT&CK for enterprise model consists of early intrusion into business systems and initial pivots into operations management, while ATT&CK for ICS is focused on techniques and tactics used once the adversary has access to supervisory control, control, and process I/O.

The terms “tactics” and “techniques” refer to the tactical goals of an adversary and the specific actions and/or the results of specific actions taken by the adversary to achieve that goal, respectively. Tactics—what the attackers are trying to do—remain fairly consistent over time, while techniques—the way the attackers try to achieve that—can evolve and adapt very rapidly.[11](#fn11)

The tactics listed in [Table 10.1](#t0010) begin with “initial access” and then progress to “execution,” “persistence,” “privilege escalation,” and “evasion.” Attacks then progress to “discovery,” “lateral movement,” “collection,” and “command and control,” before finishing with “inhibit response function,” “impair process control,” and “impact.” They overlap somewhat with the two phases of the kill chain, with “initial access” mapping to the “planning,” “preparation,” and “intrusion” steps within the initial attack phase, and the remaining tactics mapping to the industrial phase of the cyber-physical kill chain, as illustrated in [Figure 10.3](#f0020).

Each tactic can be achieved by a number of techniques, as illustrated in [Figure 10.4](#f0025). Many techniques also include sub-techniques.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-04-9780443137372.jpg)

*[Figure 10.4](#Bf0025)  MITRE ATT&CK for ICS matrix. © 2023 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.*

[Table 10.1](#Bt0010)

| ID | Name | Description |
| --- | --- | --- |
| [TA0108](http://TA0108) | Initial Access | The adversary is trying to get into your ICS environment. |
| [TA0104](http://TA0104) | Execution | The adversary is trying to run code or manipulate system functions, parameters, and data in an unauthorized way. |
| [TA0110](http://TA0110) | Persistence | The adversary is trying to maintain their foothold in your ICS environment. |
| [TA0111](http://TA0111) | Privilege Escalation | The adversary is trying to gain higher-level permissions. |
| [TA0103](http://TA0103) | Evasion | The adversary is trying to avoid security defenses. |
| [TA0102](http://TA0102) | Discovery | The adversary is locating information to assess and identify their targets in your environment. |
| [TA0109](http://TA0109) | Lateral Movement | The adversary is trying to move through your ICS environment. |
| [TA0100](http://TA0100) | Collection | The adversary is trying to gather data of interest and domain knowledge on your ICS environment to inform their goal. |
| [TA0101](http://TA0101) | Command and Control | The adversary is trying to communicate with and control compromised systems, controllers, and platforms with access to your ICS environment. |
| [TA0107](http://TA0107) | Inhibit Response Function | The adversary is trying to prevent your safety, protection, quality assurance, and operator intervention functions from responding to a failure, hazard, or unsafe state. |
| [TA0106](http://TA0106) | Impair Process Control | The adversary is trying to manipulate, disable, or damage physical control processes. |
| [TA0105](http://TA0105) | Impact | The adversary is trying to manipulate, interrupt, or destroy your ICS systems, data, and their surrounding environment. |

© 2023 The MITRE Corporation. This work is reproduced and distributed with the permission of The MITRE Corporation.

TipMany security monitoring tools will map specific security events to MITRE ATT&CK techniques. This can help operationalize security monitoring efforts by providing a clue as to where a specific event or group of events falls within the attack lifecycle. However, it should also be understood that consistent tactics and techniques are used in both ATT&CK for enterprises (i.e., phase one) and ATT&CK for ICS (i.e., phase two). There are also numerous examples of when an adversary might utilize common techniques at multiple stages of an attack. For example, “spoof reporting messages” is a technique used when attempt to evade detection in the early stages of an attack, but it is also used in the later stages of an attack while attempting to “impair process control.” Additional context of the event(s) must be considered to determine at what actual point within the overall cyber-physical attack lifecycle a specific technique truly applies.
### Obtaining access to industrial networks

As discussed in [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), the initial attack phases of a cyber-physical attack are primarily concerned with gaining access to the industrial network environment. This typically requires establishing an initial foothold outside of the industrial network (typically the business network of the organization) and then pivoting into the industrial environment.

The initial attack phases starts with planning and preparation. Initial reconnaissance helps to identify targets and plan a successful infiltration of that target. This enables the adversary to begin laying the foundation for the execution of an attack that will penetrate the industrial network. The initial will typically include extensive data exfiltration efforts and the establishment of command and control so that attackers can learn about their target environment and develop a more targeted attack to ultimately penetrate the industrial network, as shown in [Figure 10.5](#f0030).

#### Planning

The first step of an attack is all about information gathering. Reconnaissance can include any number of activities, including: researching the target company or its employees (e.g., using OSINT) or identifying weaknesses in a target's attack surface (e.g., identifying Internet-facing assets using Shodan). Using publicly available information (including  social media), details of an industrial control system, such as the DCS equipment vendor(s) used, can be determined.[12](#fn12) Social engineering can be highly effective for information gathering. It is also important to remember that a cyber-adversary targeting industrial networks may be heavily resourced, and reconnaissance efforts can include everything up to and including professional espionage and spycraft. At this early stage, anything that can be used to support an attacker in their attempt to infiltrate their target and execute an attack is useful to the attacker.[13](#fn13)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-05-9780443137372.jpg)

*[Figure 10.5](#Bf0030)  Attack tactics mapped to initial phase of an ICS attack kill chain.*

#### Preparation

The next step is preparation. As defined by SANS, this step often includes using malware (e.g., a weaponized Word document containing a Macro virus) for the purpose of enabling the attacker to progress to further steps.[14](#fn14) This might seem confusing to some because it is easy to think of malware as “the attack” and the execution of that malware the successful “execution” of the attack. In simpler times, and perhaps within the context of less sophisticated cyberthreats, this might be true. However, in the context of an attack campaign, there will likely be many types of malware used along the way. Here, it is used to help identify targets and identify potential weaknesses in those targets that might be exploitable, in order to facilitate the next step: intrusion.[15](#fn15)

#### Intrusion

The Intrusion step means gaining access to the defender's environment. This could be directly accessing the defender's network (e.g., through compromised VPN credentials) or a system one the defender's network (e.g., infecting a domain server using malware planted on a USB drive). This step typically consists of some sort of delivery mechanism, enabling an initial infection that will in turn allow the attacker to develop and deliver additional capabilities in the “enablement” step. To do this, malware must be successfully delivered so that it can perform its intended malicious function: typically the installation of additional malware, with additional capabilities; however, not all exploits require malware and the attacker could simply modify or misuse legitimate system functions (e.g., PowerShell).[16](#fn16)

#### Enablement

The enablement step is perhaps the most important. To develop and validate the end-goal of the attack, the adversary needs to learn more about the target environment. This requires an active command and control capability, to allow the attacker to interact with the environment.[17](#fn17) The methods of establish C2 are varied and often creative. Leveraging existing communication paths is easy and effective but also more likely to be detected if the defender is preforming any degree of network monitoring. In the “USB Hardware Threat Report” published by Honeywell, Inc., numerous methods of implanting covert communications were identified, providing an impressive array of wireless and even cellular access directly to the attached host and bypassing the defender's network security controls entirely.[18](#fn18)

#### Execution

This is the culmination of the initial phase of a cyber-physical attack. It is important to understand that there may by multiple initial attacks to achieve different goals associated with the overall cyber-physical attack. That is, several instances of the initial phase could be occurring simultaneously or asynchronously to achieve different goals. For example, one attack might attempt to exfiltrate credentials for remote access VPNs necessary to reach an HMI system within a substation, as used in the Black Energy attack, while another might focus on compromising a level 3.5 DMZ firewall to enable deeper penetration to industrial networks (see [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), “Hacking Industrial Control Systems”).

### Manipulation of industrial networks

The successful completion of one or more initial attacks will provide the attacker with access to the industrial network and will begin the second phase of a cyber-physical attack. This “industrial phase” shares some of the same tactics at a high level, as shown in [Figure 10.6](#f0035), with an important distinction: the target is now the process control environment, and the goal is to manipulate that environment to create a specific cyber-physical outcome. The industrial phase includes additional stages of reconnaissance, often in the form of data exfiltration using established command and control channels. This is necessary to learn as much as possible about the industrial control system in order to develop and execute a targeted attack against it.[19](#fn19)

#### Development and test

Once inside the industrial network, the first thing an attacker needs to do is develop their second- or industrial-phase attack: that is, the “physical” side of the “cyber-physical” attack. To develop an attack that will create a specific physical impact against a unique ICS operation—with specific assets, process logic, physical and environmental parameters, etc.—the minutia of the entire process control system must be taken into consideration. To identify potential hazard conditions that could be created also requires  a significant amount of testing and validation. This leads an attacker with few choices: they can develop on their target's system, which is likely to be discovered; or they can exfiltrate sufficient information to develop and test their attack offline in a lab environment.[20](#fn20) A more audacious attacker might develop their attack live on a softer or weaker targets first in order to develop attack capabilities, with the intention of leveraging their findings on their true target at a later date, although this would also likely be discovered and allow the intended target to prepare for such an attack. With lab testing being the only viable option, attackers face the same challenges that defenders do when performing cyber-physical threat modeling: truly replicating an industrial environment in its entirety is expensive and challenging. Obtaining access to process simulation software to virtualize this process may be an option for well-resourced adversaries, but even then an extensive amount of data exfiltration would be needed. (See [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessments: Cyber-Physical Threat Modeling”).

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-06-9780443137372.jpg)

*[Figure 10.6](#Bf0035)  Attack tactics mapped to the industrial phase of an ICS attack kill chain.*

#### Delivery, installation, and modification

As with the initial phase, once there is an attack, steps need to be taken to deliver and install malware or to modify existing systems.[21](#fn21) In the industrial attack phase, however, these steps are arguably simpler, as the control system itself is the “existing system” that can be directly modified to achieve the attacker's goals. The delivery and installation of malware on a system within the industrial network may facilitate this and can provide a modular framework from which specific capabilities can be initiated by that attacker, as was the case with Industroyer.[22](#fn22)

#### Execution

The attack is realized in the final step of the second phase of the cyber-physical attack. It is here that process control systems are altered in precise and calculated ways to achieve the attacker's specific, intended impact. This step could involve process logic changes, set point changes, manipulation of variables, direct manipulation of actuators, or any combination thereof.[23](#fn23) The more complex the outcome, the more aspects of the system may need to be manipulated to achieve the attacker's desired outcome. If the target control system is designed with a consideration for cyber resilience, it will be more difficult for an attacker to sufficiently manipulate the system.

## Defense lifecycles

Cyberdefenses have a similar lifecycle and consist of multiple tactics and techniques that occur in a natural progression that is important to understand. Perhaps, the most recognized cyber security defensive framework is the NIST Cyber Security Framework or NIST CSF. Introduced in 2015, the NIST CSF is a useful and concise reference. Currently available as v1.1 at the time of this publication, the NIST CSF breaks defensive efforts down into five stages:

1. • Identify
2. • Protect
3. • Detect
4. • Respond
5. • Recover

While often described as a list of distinct defensive steps, the CSF is cyclical and constantly repeats itself with a goal of continuous improvement. Like attack kill chains, these defensive efforts can also be made in concurrence, which each stage potentially introducing new awareness that can instigate these concurrent efforts. For example, in reaction to the detection of a new type of threat, response, and recovery efforts will be instigated. If multiple threats are detected together as part of a cyber-attack campaign, multiple response and recovery efforts might be justified as part of an overall response and recovery goal. At the same time, the identification of new type of threat might instigate the implementation of new security controls, which in turn might improve detection efficacy, which could lead to additional detections, ad infinitum*.*

To simplify this process, we can loosely map defensive efforts to the attack lifecycle to show the interdependencies of attack and defensive efforts. This is illustrated in Figures [10.7](#f0040) and [10.8](#f0045).

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-07-9780443137372.jpg)

*[Figure 10.7](#Bf0040)  Defensive tactics mapped loosely against the initial phase of the cyber-physical attack lifecycle.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B978044313737200004X/main.assets/f10-08-9780443137372.jpg)

*[Figure 10.8](#Bf0045)  Defensive tactics mapped loosely against the industrial phase of the cyber-physical attack lifecycle.*

### Identify

The first function of defense as defined by NIST is “identify,” and like most of the functions in NIST CSF is covers a lot: identifying threats, vulnerabilities, risk, assets, users, policies, etc, in order to “develop an organizational understanding to manage cybersecurity risk.”[24](#fn24)

To facilitate the target outcomes of this function (asset management; business environment; governance; risk assessment; and risk management strategy[25](#fn25)):

1. • Maintain an inventory of all assets. There are many commercial products that claim to automate this process. These tools can be useful for maintaining accurate inventories and detecting new assets that connect the industrial network; however, due to limitations in the efficacy of these tools, the initial inventory should be built by performing a manual assessment, and regular assessments should be performed periodically even if automated tools are in place.
2. • Perform periodic vulnerability assessments, prioritizing any systems that could enable access to industrial control assets. Industrial control systems, once accessed by an attacker, do not require specific exploits in order to perform industrial-phase cyber-physical attacks—the attacker can simply use the control system as designed. Cyber-physical threat modeling will help identify the assets to prioritize.
3. • Threat assessment can be challenging and multifaceted. For purposes of broader policies and identification of risk, a quantifiable understanding of the threat landscape is required. This could include participation in information sharing initiatives, subscription to threat intelligence programs, and similar strategic efforts. However, understanding threats is also required a tactical level, which requires a real-time understanding of the cyberthreats facing your environment. This requires at least some degree of threat detection capability as well. While the CSF breaks out detection as a discreet category, the results of detection efforts need to be considered as part of the overall identification of risk.
4. • For detailed guidance on risk assessment and risk management in industrial systems, please refer to [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessment.”

### Protect

Protection requires the implementation of various safeguards to minimize and contain the impact of a potential cybersecurity incident. These safeguards range from: administering policies (training personnel to increase cybersecurity awareness, implementing procedures to improve cybersecurity hygiene and best practices, etc.), to maintenance efforts, which can improve system resilience, to implementing hard cybersecurity controls (identity management, access controls, antimalware technology, network security controls, etc.), which can potentially interfere with interrupt the cybersecurity attack process.[26](#fn26) This stage can be challenging because it uses the term “protective technology” very broadly, and there is a vast and diverse market of cybersecurity controls that are available to chose from. Many organizations question which protective technologies they  should invest in. The only correct answer is “whichever control(s) are needed to progress from the current level of cybersecurity protection to the desired level of cybersecurity protection.” This requires awareness of where an organization is on their individual cybersecurity journey and requires ongoing assessment of cybersecurity risk (see [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessment”).

To facilitate this stage:

1. • Harden assets to minimize the attack surface. This means uninstalling unnecessary applications, disabling unused ports and services, and configuring each asset with the end goal of limiting the functionality of that asset to *only* its intended purpose. The Center for Internet Security has published numerous benchmarks to facilitate hardening efforts, available at [https://www.cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks)
2. • Establish zones and conduits to isolate systems based on security levels. The greater the degree of network segmentation that is implemented, the more likely that a cybersecurity event can be effectively contained.
3. • Implement strong identity management and access control (IMAC). The best segmentation efforts provide little benefit without also having enforceable access controls in place. Consider a “zero trust” model where all access is denied by default: any access to networks, assets, and even specific applications can be controlled and managed on a per-user basis.
4. • Active cybersecurity controls should be used to enforce policies. This should be considered before implementing “protective technology,” to ensure that technology investments are aligned with actual needs.
5. • Also consider other aspects of the CSF when planning protective technology investment. Does a specific cybersecurity control support detection efforts? Does it provide information about the infrastructure that can contribute to identification efforts? Does that same information facilitate response and recovery efforts?

### Detect

Detection is critical to observing active stages of a cyberattack. The earlier that detection occurs in relation to the attack lifecycle, the more time is available for the defender to recover and respond. The target outcomes of this function include anomalies and events, security monitoring, and detection processes,[27](#fn27) which are all discussed in detail in [Chapters 12](../B9780443137372000051/CH0012_383-408_B9780443137372000051.xhtml), [13](../B9780443137372000105/CH0013_409-446_B9780443137372000105.xhtml), and 11, respectively.

When considering detection functions, remember the following:

1. • Detection of active threat activity requires a combination of people, process, and technology. Technology is required to detect intrusion attempts, malware activity, anomalies, process deviations, etc. Without processes in place to support this technology, and without the people in place to follow through on those policies, there is little value to be realized
2. • Detection efficacy varies, but is never 100%. Always assume that there is threat activity occurring, but that it is not being detected.
3. 
4. • Detection technology can support other areas of the CSF by providing valuable data points, but only if implemented and operationalized correctly. Always ensure that logging and alerting features are fully enabled, and that the event data that is produced is fully utilized (e.g., collected, analyzed, monitored, and stored appropriately).
5. • Anomaly detection solutions that look for abnormal industrial protocol behavior are extremely popular at the time of publication. While useful, these solutions will typically produce high rates of false positives. Without adequate resources to review the results, these solutions can be problematic.
6. • It is easy to think of “detection” technology only within the context of point solutions for detecting malware on a host, or intrusions on a network, etc. However, SIEM, XDR, SOAR, and other solutions are also capable of detecting more complex threats that make up an attack campaign, and some may be able to “connect the dots” to detect campaigns in their entirety. This will facilitate response and recovery efforts.
7. • The ability to map threat data to the MITRE ATT&CK framework is also extremely useful to support response efforts.

### Respond

Response can begin as soon as there is something to respond to. This could theoretically include responses to intelligence gathered during the “identify” stage or responses to weaknesses discovered during the “protect” stage, but it is most commonly in response to activity detected during the “detect” stage. The outcomes defined here include more than what many think of as “incident response” efforts, however: response planning, analysis, and improvements are some of the additional identified outcomes defined by NIST.[28](#fn28) This supports the framework's overall objective of supporting continuous improvement.

To facilitate this stage:

1. • Remember that segmentation makes containment easier, enabling compromised systems to be quarantined on the network. Dynamic segmentation (any segmentation that can be reconfigured on a production system without interruption) allows this with minimal (if any) impact on network administration.
2. • Practice! Response plans that are not put into practice have minimal value. Response exercises should be performed regularly. Introduce unexpected variations in response exercises so that responders are ready to overcome any challenge.
3. • Understand that even with a well-trained, practiced team, a situation might occur that is beyond their capability. Understand the limits of response personnel and establish an escalation process for these situations. This could include a contract with a dedicated third-party incident response provider, contact procedures for relevant government agencies, etc.
4. • Document everything: communications, analysis, and improvement efforts can benefit from proper documentation, in particular.

### Recover

The recovery process is all about resiliency. Plans for how to recover, training on how to execute those plans, and how to improve associated processes as a result of recovery efforts all fall under the umbrella of the “recover” function.[29](#fn29)

To facilitate in this stage:

1. • Remember that recovering servers and workstations is only part of the process. If an industrial attack reached the second phase (the industrial phase) of the kill chain, the process may have been impacted, altered, or even stopped. Process recovery and validation efforts should be factored into the recovery process.
2. • Validate backups. Recovery without validated backups requires a lot more time and effort. Back up critical systems regularly, validate the backups, and practice the “3-2-1” backup strategy: keep at least three copies of your data; store two copies on different storage media; and store one copy off site.
3. • Remember that recovery of an industrial automation process consists of far more than bringing servers and workstations back online. Depending on the process, and how and when it was disrupted, there could be larger recovery efforts required, including: replacement of damaged assets, validations of process logic, potential engineering changes, environmental cleanup efforts, etc.

## The importance of understanding lifecycles

Attack lifecycles are important to understand, as they directly impact (and are in turn directly impacted by) an organization's defensive efforts, in the “dance” of attack and defense efforts referenced at the beginning of this chapter. As a defender, a primary goal is to minimize the MTTR.

This could be accomplished by:

1. • Preventing an attack from occurring in the first place, and thereby eliminating the need to recover.
2. • Prevent an attack from executing successfully
3. • Detecting an attack in the early stages, in order to mitigate the threat before it can progress. For example, by detecting a threat at the “intrusion” stage, and mitigating the threat before it can become “enabled” (establish C2, exfiltrate data, deploy new payloads, etc.) impact of the “execution” phase can be minimized or avoided altogether.
4. • Detecting an attack in later stages of the initial phase of a cyber-physical attack can determine the target(s) of the industrial phase and help mitigate the threat to the process.

While the NIST framework is designed for continuous improvement across all functions[30](#fn30), within the context of an ongoing attack, there are certain activities and  outcomes that are reactive in nature: it is not possible to detect threat activity until that activity is performed; it is not possible to respond to an incident that has not happened, and it is not possible to recover without first experiencing a failure. Figures [10.7](#f0040) and [10.8](#f0045), illustrate this, showing how the attack lifecycle maps to detection, remediation, and recovery windows. However, the framework does offer guidance on how to perform these functions proactively in support of continuous improvement. Many outcomes of the NIST functions—such as vulnerability identification, hardening, response planning, training exercises, system backups, etc.—can and should be performed during peace time. It is useful to think about these defensive functions within the narrower context of an ongoing attack because it helps visualize the effort required to respond to an attack, which helps understand mean time to recovery (MTTR) and the need to minimize it.

### Minimizing MTTR

To minimize overall MTTR, we can focus on three areas where a defensive action is taken in direct respond to an offensive action. In a 2021 study published by the SANS Institute, these areas are identified as compromise to detection (CtD), detection to containment (DtC), and containment to remediation (CtR). Consider a simplified version of the overall attack process:

- 1. First the attacker must compromise the industrial target. This is the execution of the initial attack phase that gains entry to the industrial network and begins the second phase of the ICS Kill Chain.[31](#fn31)
- 2. The attacker then needs to deliver the initial payloads necessary to further develop the targeted industrial attack.[32](#fn32)
- 3. Finally, the attacker leverages these payloads to refine their attack, enabling the execution of the targeted ICS attack.[33](#fn33)

At the same time, defenders must:

- 1. Detect the initial compromise.[34](#fn34)
- 2. Identify the full extent of the compromise and contain it.[35](#fn35)
- 3. Remediate the threat once it has been contained.[36](#fn36)

Remembering that these efforts take time for both attackers and defenders, it can be seen how the minimization of the time it takes between the attacker's first action (compromise) and the defender's first action (detection) could change the overall outcome of the attack. If the CtD time is immediate, the defender can begin containment efforts early, while the attacker is still attempting to develop an effective targeted attack. If the time it takes for the defender to contain the attack once it has been detected, is also immediate, the attacker could be prevented from execution of the final industrial attack. In other words, the faster the defender can react, the greater the chance of breaking the ICS attack kill chain.[37](#fn37)

Unfortunately, the same study showed that average reaction times were less than optimal: 42% of surveyed operators took more than 2 days to detect an initial compromise,  with 23% taking longer than one week, and 14% taking longer than 1 month. Similarly, the time from detection to containment took more than 2 days in 31% of cases, and more than a week in 9% of cases.[38](#fn38) It can be clearly seen that once a threat is detected, containment can be achieved relatively quickly, while the initial detection can take longer.

SANS further quantified these limitations by identifying the types of industrial assets with the highest perceived risk, and comparing that to the types of data most commonly collected for cybersecurity analysis. The results showed that the highest risk areas had the least amount of data collection, with one exception: Servers running commercial operating systems had the highest instances of data collection at 76%. However, connections to other internal systems, connections to field control networks, and embedded controllers and components had poor collection rates at 54.5%, 38.9%, and 18.7%, respectively.[39](#fn39)

This is not surprising: there are numerous information security tools available commercially that facilitate data collection from servers running common operating systems; network data collection is slightly more difficult within and between industrial networks due to the prevalence of legacy infrastructure; and embedded devices such as PLCs and IEDs can be extremely difficult to collect data from, and in some cases, these types of assets may not produce security log or event data at all.

Improving detection rates may therefore require the use of specialized monitoring tools. Some examples include:

1. • Control system alarm management systems that are able to produce data related to process variations or errors that may be relevant to cyber security efforts
2. • Network monitoring tools deployed inline or on a network span or tap, that are capable of producing network flow data that may be relevant to cybersecurity efforts
3. • Network monitoring tools deployed inline or on a network span or tap that are capable of identifying process control activity and detect anomalies that may be relevant to cybersecurity efforts
4. • Host cybersecurity controls that are able to produce highly relevant cybersecurity event data

Unfortunately, the specific cybersecurity controls and detection technologies that are required to close the compromise to detection gap can be difficult to implement in an industrial network. Once implemented, the data generated by these tools can be difficult to collect and analyze in a manner that is useful to industrial operations.

## Summary

Attacks against industrial systems require many steps to be successful, and likewise, there are multiple steps that defenders must take when attempting to minimize (or eliminate) the success of an attack. Understanding these individual lifecycles and how they are intertwined is extremely beneficial. Through continuous improvement of cybersecurity functions, the job of the defender will be easier overall. Through the efficient response to specific stages of an attack, threats can be further minimized when they occur, and the overall response and recovery times can be minimized.

---

[1](#cfn1)  Val Saengphaibul. *A Brief History of The Evolution of Malware*. Fortigaurd Labs Trheat Research. Fortinet. March 15, 2022.

[2](#cfn2)  Computer History Museum. *What was the First* PC? 1986.[https://www.computerhistory.org/revolution/personal-computers/17/297](https://www.computerhistory.org/revolution/personal-computers/17/297)

[3](#cfn3)  Michael J. Assante, Robert M. Lee. *The Industrial Control System Cyber Kill Chain*. SANS Institute. 2021.

[4](#cfn4)  Ibid.

[5](#cfn5)  Eric M. Hutchins, Michael J. Cloppert and Rohan M. Amin, Ph.D., “Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains”. [https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)

[6](#cfn6)  Ibid.

[7](#cfn7)  Michael J. Assante, Robert M. Lee. *The Industrial Control System Cyber Kill Chain*. SANS Institute. 2021.

[8](#cfn8)  Ibid.

[9](#cfn9)  The MITRE Corporation. *MITRE ATT&CK Framework v13.1*. [https://attack.mitre.org](https://attack.mitre.org)

[10](#cfn10)  Otis Alexander, Misha Belisle, Jacob Steele. *MITRE ATT&CK for Industrial Control Systems: Design and Philosophy*. The MITRE Corporation. Project No 01DM105-OT. March 2020.

[11](#cfn11)  The MITRE Corporation. *MITRE ATT&CK Framework v13.1*. [https://attack.mitre.org](https://attack.mitre.org)

[12](#cfn12)  Michael J. Assante, Robert M. Lee. *The Industrial Control System Cyber Kill Chain*. SANS Institute. 2021.

[13](#cfn13)  Ibid.

[14](#cfn14)  Ibid.

[15](#cfn15)  Ibid.

[16](#cfn16)  Ibid.

[17](#cfn17)  Ibid.

[18](#cfn18)  GARD Threat Research. *2023 USB Industrial Threat Report*. Honeywell, Inc. September 2023.

[19](#cfn19)  Ibid.

[20](#cfn20)  Michael J. Assante, Robert M. Lee. *The Industrial Control System Cyber Kill Chain*. SANS Institute. 2021.

[21](#cfn21)  Ibid.

[22](#cfn22)  Cherepanov, Anton. "Industroyer: Biggest threat to industrial control systems since Stuxnet". [www.welivesecurity.com](http://www.welivesecurity.com). ESET. June 17, 2017.

[23](#cfn23)  Michael J. Assante, Robert M. Lee. *The Industrial Control System Cyber Kill Chain*. SANS Institute. 2021.

[24](#cfn24)  National Institute of Standards and Tecehnology (NIST). Framework for Improving Critical Infrastructure Cybersecurity. Version 1.1. April 16, 2018.

[25](#cfn25)  Ibid.

[26](#cfn26)  Ibid.

[27](#cfn27)  Ibid.

[28](#cfn28)  Ibid.

[29](#cfn29)  Ibid.

[30](#cfn30)  Ibid.

[31](#cfn31)  Michael J. Assante, Robert M. Lee. The Industrial Control System Cyber Kill Chain. SANS Institute. 2021.

[32](#cfn32)  Don C. Weber. Responding to Incidents in Industrial Control Systems: Identifying Threats/Reactions and Developing the IR Process. SANS Institute. May 2020.

[33](#cfn33)  Ibid.

[34](#cfn34)  Ibid.

[35](#cfn35)  Ibid.

[36](#cfn36)  Ibid.

[37](#cfn37)  Ibid.

[38](#cfn38)  Ibid.

[39](#cfn39)  Ibid.
