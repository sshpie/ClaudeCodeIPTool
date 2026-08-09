# Chapter 26. Validating Your Security

**IN THIS CHAPTER**

- **Understanding the importance of validating and testing the security of an organization**
- **Understanding the difference between a security assessment and a penetration test**
- **Identifying the tools and techniques used to test the security of a network**
- **Determining the method attackers use to break into a system**

Systems are complex and there's a good chance that any computer connected to a network has vulnerabilities that could potentially be broken into. Because any system connected to a network will most likely be scanned by an attacker, its potential for compromise is high. You have to stay one step ahead of the attacker. Therefore, it's critical that organizations perform penetration testing of their networks to better identify and proactively fix vulnerabilities.

In this chapter we'll learn about the various types of tests that can be performed and how they can be used to increase the overall security of a network. We'll also learn how attackers break into systems and use this knowledge to build more effective testing techniques.

# Overview

Everyone has used or heard the buzzwords "penetration test" or "security assessment." Some even view the terms as synonymous. This section is going to identify the differences in the two types of tests and how they can be used to complement each other for the overall security of your network.

## Penetration test

At the most basic level, a penetration test ("pen test"), red team exercise, and ethical hacking are all methods to simulate what an attacker would do against a network. The difference is that attackers won't tell you how they compromised your system, but a penetration tester will. The penetration test should be considered one tool of many to ensure the security of the information infrastructure. Penetration tests are actually broken into three general phases:

- Network mapping and identification
- Information analysis and network exploitation
- Report

A penetration test is the physical identification of the target network. The pen tester may or may not have prior knowledge of the network, so some of the things that will be identified during this portion of the penetration process are:

- IP addresses
- Open ports
- Operating system identification
- Running services

The test can be conducted on either the external facing system or the internal network. The process and methods are the same. In general, the test tries to gain an understanding and mapping of the network, as shown in [Figure 26-1](ch26.html#mapping_of_a_network_performed_during_a).

![Mapping of a network performed during a penetration test](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2601.png)

**Figure 26.1. Mapping of a network performed during a penetration test**

Once that phase of penetration testing is completed, the information is analyzed to determine the best approach for the next phase of testing. The information is used to identify possible security vulnerabilities or avenues that may allow the pen tester to gain access to the system. If a security vulnerability is identified, then there may be an attempt to exploit this vulnerability if it is within the scope of the test; otherwise, the security vulnerability will be documented only.

The purpose of the penetration test is to identify and mitigate any security risks on the network. The information obtained during the pen test can be used to correct security issues that might otherwise not be identified until an actual incident occurs. The final report will outline the testers' findings along with recommendations to guide the organization to the best business practices to ensure network security and/or government compliance.

There are legal liability issues also associated with conducting a penetration test. The testing team has to be protected against liability in the event data is destroyed or the system is taken down. Some considerations of the team include:

- Protect information uncovered during the penetration test
- Limitation of liability
- Comply with relevant laws and regulations
- Conduct business in an ethical manner
- Remain within the scope of the assignment
- Develop a testing plan

## Security assessment

While a penetration test looks at a network from an attacker's perspective with minimal knowledge of the system, a security assessment is an in-depth look at a network, evaluating the configuration of all systems and analyzing the network diagram. The definition of an assessment taken from ISC2 is:

> *the effort to gain insight into system capabilities and limitations. This may include document reviews, controlled environment testing, or limited live testing. The testing is not considered rigorous enough in itself to allow a determination of the effectiveness of the current security state. The outcome of an assessment is to provide the customer with information for them to determine the best use of resources to protect information*.

Some of the key areas that are evaluated during a security assessment include:

- Document review or gap analysis
- Policies and procedures
- Disaster recovery plans
- Laboratory testing of programs and process
- Laboratory testing of applications
- Limited live testing of internal systems

Security assessments are used frequently and provide much needed information to the customer. The focus of the security assessment is on the internal infrastructure and processes.

# Current State of Penetration Testing

The term *penetration testing* is used very loosely in the security field, and to the security professional it can mean many different things. To some it may mean breaking into an organization's network just to prove that it can be done or scanning a network to document all the known vulnerabilities found. It could also involve a remote attack from outside the perimeter of an organization's network, a physical penetration of a work site, or social engineering attacks. The test could be performed by a third-party team with custom tools and exploits or by an internal team with commercial or proprietary vulnerability scanning tools. All of these methods would be considered different types of penetration tests, so the test used should be dependent on the organization and its security objectives.

Penetration teams may also have different degrees of knowledge before the tests are carried out. There are zero, partial, and full-knowledge tests. As the name implies, a *zero knowledge test* is one where the team has no knowledge of the target and must start from ground zero. *Full knowledge*, on the other hand, means the team has intimate knowledge of the target, which might be the case for internal teams auditing their own organization. Another distinction made is between internal and external tests. Internal tests simulate the damage a disgruntled employee could do from inside the network. External, of course, simulates an outside hacker. In some cases, in order to test the effectiveness of their information system security team, an organization will not inform their team of the ethical hacker's activities. This situation is referred to as operating in a double-blind environment.

At the end of the test, a report is generated and given to management describing the vulnerabilities that were identified and their severity. The report should also provide suggestions on how to deal with the problems found and steps that could be taken to mitigate them. It is from there that the organization can decide how to deal with the vulnerabilities found and what countermeasures to implement.

## Current penetration testing flow

The following is the general flow that is performed during a penetration test:

- **Discovery**—Footprinting (determining the type of system) and gathering information**Social engineering**—Involves tricking a victim into revealing sensitive information through social interactions.**Dumpster diving**—Process of looking through an organization's trash for discarded sensitive information.**Physical break-in**—Attacker gains access to facility and to an internal network or steals equipment containing sensitive data.**Web search engine (Google)**—Used to research targets and gain additional knowledge using Google search directives.**Newsgroups**—Postings by employees of technical questions on public forums.**Whois database**—Provides information about a target's Internet address, domain names, and contacts.**DNS servers**—These hold information about mapping of domain names to IP addresses, a list of mail servers for an organization, and other organization name servers.
- **Enumeration**—Port scans and resource identification**Wireless access points**—Detect wireless access points of an organization.**Modems**—Find unsecure modems using war dialing or old or forgotten-about modems with weak security.**Network mapping**—Used by attackers to determine the network topology and to create an inventory of target machines.**Port scanning (Nmap)**—Used to determine which ports have listening services on a target host.**OS fingerprinting**—Used to determine the underlying operating system of a target based on protocol behavior.**Firewall settings**—Determining the rules implemented on a packet-filtering firewall.
- **Vulnerability mapping**—Identifying vulnerabilities in systems and resources**Vulnerability scanners**—These are tools that have the ability to check a target network for hundreds of vulnerabilities by employing a database of configuration errors, system bugs, and other problems.**Web application attacks**—These attacks target the users of an improperly coded site that could allow cross-site scripting, SQL injections, buffer overflows, and other flaws.**Common errors**—These include weak passwords, common misconfiguration of devices, and other user-created vulnerabilities.
- **Exploitation**—Exploiting vulnerabilities to gain unauthorized access**Metasploit**—An exploitation framework that helps automate the production and use of exploits, such as stack or heap-based buffer overflows.**Password attacks**—These involve guessing default or simple passwords, or password cracking which involves an automated tool that determines the original password with the use of the hash.**Sniffing**—Attacker gathers information from a LAN. This could be user IDs and passwords that are in clear text, e-mails, or files that are sensitive. This information could be used to escalate privileges.**Denial-of-service**—Attacker prevents legitimate users from accessing the system, either by stopping a service or by resource exhaustion.
- **Report to management**A report should be clear and easy to understand for the penetration test to be valuable. So for the technical people a list of vulnerabilities and recommended solutions are needed, and for managers/executives a broader overview and assessment of business risks associated with the vulnerabilities are necessary.

## Automated vulnerability scanners vs. manual penetration testing

Manual testing by a team of skilled white-hat hackers may be the most effective way to penetration test a network but it is also expensive. Because of this many organizations rely on running commercial scanning products that are less expensive and can be run more frequently.

Manual testing isn't perfect; there are pros and cons as with any other solution. One positive aspect is that it tests the effectiveness of your current security products against real-world attack scenarios. This allows you to make sure your security incident response and recovery teams are effective and know how to deal with malicious attacks. Also, with manual testing, social engineering and the education of your user base can be evaluated. This allows manual penetration teams to call up different parts of your organization with a spoofed caller ID or send out spoofed e-mails with malicious attachments to see how your users respond. Manual testers can also test Web application security, which recently has been a popular avenue of attack. Most scanners have trouble testing this avenue because of its difficulty to automate.

Some of the negative aspects of manual testing are that it's expensive, can be intrusive or disruptive, and is dependent on the penetration team's skill set to be effective. To an organization that depends on its computer infrastructure to do business, having servers go down even for a short time can cost a lot of money. So you really have to trust that the penetration team has the skill to avoid those situations. It also might not be an efficient way to find all the vulnerabilities for your organization. For example, the testers might find a few holes that they can use to gain access, but they most likely won't find all the vulnerabilities present.

Automated vulnerability scanners have their own benefits and problems. As mentioned earlier, they are inexpensive. They can be used with greater frequency, and tests can be run privately with no disruption of business. Being able to run tests with greater frequency is an advantage because it ensures that you are not vulnerable when changes or patches are applied to your network. In addition results are consistent and repeatable with reports being generated automatically.

But scanning tools also have their limitations. Some scanners rely too heavily on patch levels and software versions, and false positives can be abundant. The tools don't test users, and they aren't always up to date on the latest exploits. Because of these reasons scanners aren't always a true simulation of a skilled attacker. High-level attackers can use sophisticated traffic masking and hiding techniques and most scanners don't simulate this very well.

Some key problem areas of penetration testing have now been covered, so that an organization can understand and, it's hoped, avoid them. If an organization can standardize its procedures for manual testing so that the results are actually repeatable and consistent, this is extremely helpful. Such standardization also increases confidence that your team didn't miss testing any attack vectors and makes it simpler to fix problems with disruption and clean-up when the tests are over. If the team compromises a large number of the organization's computers, it might forget some back doors, rootkits, or sniffers that were used when exploiting the network. And those mistakes could leave an organization open to malicious hackers if they are not cleaned up appropriately. Standardization helps mitigate this.

At present, penetration tests and vulnerability analyses are mainly reactive in nature. Hackers will come up with other exploits. Thus, penetration testing teams will adopt new tools and eventually the scanners will update their databases. To be more proactive, vulnerability analysis techniques need to be run on the critical applications that hackers are likely to exploit. Fuzzing frameworks can be implemented that test those applications for stability and vulnerabilities. Fuzzing is the process of testing input fields, looking for vulnerabilities and conditions that can be exploited. Also, code can be audited for security, and if the code is a closed source then debuggers can be used to test those applications. This process would be particularly helpful for the Web-facing applications that are usually running from the network DMZ. The web services are available over the Internet and would benefit from the extra assurance provided.

The reporting process after a penetration test is completed could also be improved. Once a pen testing team completes a test it gives the organization a list of ways to patch or fix the holes discovered. This can lead to a cycle referred to as "penetrate and patch," which is a losing game. Once the pen test is completed the team should suggest better security design and architecture changes that will better help the organization. Instead of just securing it from the "vulnerability of the month" the test team can actually work with the organization's network and security engineers and help them come up with better solutions from a security standpoint. Of course this does have some limitations — for one it's probably more expensive. And changing core aspects of your security design is no easy feat. You would also need pen testers who are knowledgeable not only in attack techniques but also network architecture and design. But teams of this nature will be more effective in the long run.

Assessing your organization's security is a key component of any good vulnerability risk assessment. The results can be extremely helpful and can fix critical vulnerabilities that you hadn't realized were present. One thing is for sure — with enough time and energy vulnerabilities can be found in any network. That's why it's so important that organizations use layered security architectures for their networks; this way a single vulnerability won't compromise the whole network. It's crucial for penetration testers to understand this concept and be able to recommend structural and architectural changes to an organization that is found to be consistently vulnerable to the latest exploits.

# Formal Penetration Testing Methodology

The following is a formal penetration testing methodology that can be followed by an organization. It presents in easy-to-see outline form some of the main points touched on earlier:

## Pre-attack phase

### Defining scope of assessment

It is critical to be able to define the scope that the assessment is going to cover:

- Determine if the assessment will be comprehensive or limited to only a subset of the network.
- Define the terms of the service level agreement (SLA) that determine the actions to be taken in the event of a serious service disruption.
- Define other important terms of the test:Desired code of conductProcedures to followOrganizational interactions
- Plan and schedule the duration of the assessment.
- Take detailed notes of the results of every step in the penetration test.

### Discovery/information gathering

Once the scope has been identified, you will see which systems are visible and gather information about the in-scope systems:

- Use the Whois database to find information about a target's internet address, domain names, and contacts.
- DNS holds information about mapping of domain names to IP addresses, a list of mail servers for an organization, and other organization name servers. Use DNS enumeration to locate all the DNS servers and corresponding records for an organization.
- "Dumpster dive" to find discarded sensitive information in an organization's trash.
- Utilize the practice of social engineering to trick victims into revealing sensitive information through social interactions:Impersonating an employee or valid userPosing as an important userCalling technical supportShoulder surfing (looking over someone's shoulder as the person types in a password)Phishing
- Query Web search engines (i.e., Google) to research the target organization.Find information about the company or employee.Corporate job postings can provide information as to the type of infrastructure devices.Other information could include IP addresses, e-mail addresses, phone numbers, and corporate policies or procedures.
- Check newsgroup and blog postings by an organization's employee for technical data.

### Enumeration/scanning

After a list of visible systems has been put together, you will find out as much information as possible about each system, including open ports and services:

- Map the network by scanning for active hosts and create network diagrams of all the live or responding machines.
- Check for open ports by port scanning the identified live hosts.
- Identify the services running on each host by using the identified open TCP/IP ports on the system.
- Determine the operating system running on each host by using OS fingerprinting techniques that determine the underlying OS based on protocol behavior.
- Determine the rules implemented on a packet-filtering firewall.
- Perform war dialing to look for rogue modems that have been forgotten about or connected as a backup.
- At the organization's physical location check for any wireless access points that are currently deployed.
- Perform surveillance of the organization's physical security, looking for any holes that can be exploited to allow you physical access.

### Vulnerability mapping

Once services and ports are determined, vulnerabilities will be identified across each system:

- Use a vulnerability scanning tool that has the ability to check a target network for vulnerabilities by employing a database of configuration errors, patch levels, system bugs, and other problems.
- Identify the Web applications used by an organization and check it for potential cross-site scripting, SQL, buffer overflow, or other vulnerabilities that might be present.
- Check for misconfigurations that could have been missed by the scanner, weak or default passwords, and other user-created vulnerabilities.

## Attack phase

Once key information has been identified, the attack phase will begin:

### Gaining access

The first part of exploiting a system is gaining access to a resource:

- If a hole in physical security is found, exploit it with the end goal of gaining physical access to a server, client machine, or a network port.Install a keylogger or another type of malware.Collect data by sniffing the network for passwords or collecting data that can be used later to crack passwords.Plant a rogue access point to create an open wireless network with access to the wired network.Steal sensitive electronics or documents.
- Attack the wireless network to gain access to internal resources:Use cracking encryption for WEP or dictionary attacks on WPA passphrases.Use wireless sniffing or eavesdropping on other users' confidential information.Use access point masquerading or spoofing by pretending to be a legitimate access point.
- Penetrating from the perimeter firewall or from the internal network using the data gathered in the pre-attack phase.Use an exploitation framework that helps automate the production and use of exploits, such as stack or heap-based buffer overflows.Run new or custom-made exploits against vulnerable targets, including servers, hosts, or networking devices.
- Run or develop Web application attacks that were found in the vulnerability scanning phase.
- Check if the organization is vulnerable to denial-of-service or resource exhaustion attacks. Make sure this is approved first because it will temporarily stop certain services from responding.

### Escalating privileges

Once access has been gained to a system, you will try to evaluate privileges and gain additional access:

- After gaining access to a system, escalate the privileges from a regular user into an administrative or root account if needed.Use the user access to the system to understand the system better; then run the appropriate exploit code against the system to gain more access.
- Evaluate the trust relationships between the exploited machine and other network hosts looking for other exploitable targets.
- Recover the encrypted password files stored locally on the machine and start running password crackers against them.
- Install a network sniffer to look for unencrypted passwords or other information going across the network.

### Repeating steps

Repeat the previous steps from your current location until all leads on possible vulnerabilities are followed and the entire network is tested within the scope defined earlier by the organization.

## Post-attack phase

After the attack is complete you would have to clean up the systems:

### Restoring compromised systems

The first post attack step is to restore the compromised system to its original state:

- Remove files that were used in the penetration testing process.
- Revert any network setting changes to their original values.
- Network cards in promiscuous mode or ARP poisoning from sniffing needs to be corrected.
- Registry settings or any other system configurations that were altered during the attack process should be fixed.

### Analyzing results

- Once the test is complete, use the notes documented throughout the assessment to start analyzing the security posture of the organization.

### Compiling data into comprehensive report

- Create a technical report that lists the vulnerabilities found and recommended solutions for the network and security engineers of the organization.
- For executives and managers, create a document with a broader overview that contains the business risk associated with the vulnerabilities found.
- Complete the rating scheme for the organization that scores it based on vulnerabilities and exploits found.

# Steps to Exploiting a System

In order to effectively test and validate the security of an organization, it's critical that you understand how attackers exploit and break into a system. An attacker can go about gaining access or exploiting a system in many different ways. No matter which way an attacker goes about it, there are some basic steps that have to be followed. This list has been composed by analyzing the various ways that attackers have broken into networks. They are:

- Passive reconnaissance (Step 1)
- Active reconnaissance or scanning (Step 2)
- Exploiting the system (Step 3)Gaining accessOperating system attacksApplication-level attacksScripts and sample program attacksMisconfiguration attacksElevation of privilegesDenial-of-service
- Keeping access: Back doors and Trojans (Step 4)
- Covering one's tracks (Step 5)

It is important to note that it is not always necessary to perform all of these steps, and in some cases it is necessary to repeat only some of the steps. For example, an attacker might perform the active and passive reconnaissance steps and, based on the information gathered about the operating systems on certain machines, try to exploit the system. After repeating Step 3 several times, trying all sorts of operating system attacks, and finding these unsuccessful, the attacker might then go back to Steps 1 and 2. At this point, the attacker's active reconnaissance will probably become much more in-depth, focusing in on other applications that are running, possible scripts that are on the system, and even what information is available about the operating system, such as revision and patch levels. With this information, the attacker would then go back to attacking the system.

One would hope, for the sake of protecting the systems, that this process would take a long time to accomplish and that the attacker would get frustrated and give up without gaining access. But as we have seen, most attackers are very persistent and have a lot of time. Ideally, a company should have proper IDS (intrusion detection systems) in place so that it can detect an attack and protect against it before it does any damage.

Even if a company cannot prevent an attack, just increasing the number of times an attacker must try before compromising the system increases the chance that someone will detect the attack. Remember that prevention is ideal but detection is a must. Most companies are so vulnerable and wide open that in many cases an attacker can go through each step once and be highly successful, with a minimal chance of detection. The steps in the reconnaissance schema outlined earlier are explained in more detail in the sections that follow.

## Passive reconnaissance

In order to exploit a system, attackers must have some general information; otherwise they won't know what to attack. Robbers plan which house to rob by performing passive reconnaissance, looking at specific houses in specific locations. Much the same thing happens with hacking. Once an attacker picks a company to go after, this person has to have some information about the company and know where it is located on the Internet.

Other activities that would be considered passive reconnaissance include finding out the physical location of the company. Information can also be gleaned just by being outside the building at different times of the day. By watching a loading dock, an attacker can tell what type of hardware and software a company is having delivered. The attacker can also see access points that can be used to launch a physical attack. Observing employee badges can also be useful to an attacker because many companies use an initial and last name as part of an employee's computer access procedure.

Information collected passively is not always directly useful, but it paves the way for other steps including the active reconnaissance that will eventually be needed.

## Active reconnaissance

At this point, an attacker has enough information to try active probing or scanning against a site. (In the robbery analogy, the thief has checked on fences and dogs, and is now trying windows, door locks, and visible alarms. He's still gathering information but in a more active way.)

With the Internet, an attacker probes the system to find additional information of the kind in the following list:

- Hosts that are accessible
- Location of routers and firewalls
- Operating systems running on key components
- Ports that are open
- Services that are running
- Version of any applications that are running

The more information attackers can gain at this stage, the easier it will be when they try actually to attack the system. The usual approach is to find out some initial information in as covert a manner as possible and then try to exploit the system. If they can exploit it, they move on to the next step. If not, they go back and gather more information. A skilled attacker gathers no more information than needed, especially if gathering extra information would set off alarms and raise the suspicion level. The process is iterative — the attacker gathers a little, tests a little, and continues in this fashion until access is gained. Keep in mind that as attackers perform additional active reconnaissance, their chance of detection increases because they're actively performing some action against your company. It's critical that you have some form of logging and review in place to catch active reconnaissance; if you can't block attackers at this point, your chance of detecting them decreases significantly.

Attackers trying to break into a system usually run some tests to figure out the IP address of the firewall and routers. Then they try to determine the type of firewall and router and the version of the operating system that's running, to see if there are any known exploits for those systems. If so, they'll then try to compromise those systems. By gaining access to the external router or firewall, they can gather a lot of information and do serious damage. At that point attackers try to determine which hosts are accessible and then scan those hosts trying to determine which operating system and revision levels these are running. For example, if a server is running Windows 2008 OS, attackers can then scan for all vulnerabilities with that version and try to use these to exploit the system.

As explained earlier, gaining access is an iterative process in which attackers keep trying until they either succeed or give up. A company's goal in protecting its computers and networks is to make it so difficult for someone to gain access that the attacker gives up before getting in.

One major mistake many people make is to treat security as all or nothing. If a company can't achieve top-notch security then they give up and leave their systems with no security. What they need to realize is that some security is better than none, and that by starting somewhere they can eventually get to the point where they have a very secure site. Also, in most cases a small percentage of exploits account for a large number of security breaches. Therefore, some level of protection can increase a company's security tremendously.

Another important avenue of reconnaissance or information gathering is social engineering. In social engineering an attacker tries to impersonate a legitimate user in order to gather information that normally would not be available.

## Exploiting the system

When most people think about exploiting a system, they only think about gaining access, but there are actually two other areas: elevation of privileges and denial-of-service. All three are useful depending on the type of attack one wants to launch. There are also cases where these can be used in conjunction with each other. For example, an attacker might be able to compromise a user's account to gain access to the system but still not have root access to copy a sensitive file. At this point, the attacker would have to run an elevation of privileges attack to increase the attacker's level and thus gain access to the appropriate files.

### Gaining access

Because one of the most popular ways of exploiting a system is gaining access, let's start with that type of attack. Attackers can gain access to a system in several ways, but at the most fundamental level they have to take advantage of some aspect of an entity. That entity is usually a computer operating system or an application, but if we include physical security breaches it could be a weakness in a building.

A robber always exploits some weakness in a house, and the weakness is often there because of its usefulness to the owner. Who would want a house without windows or doors? This same principle holds for computer systems. As long as they are useful to a company, they will have weaknesses that can be compromised. The key is to minimize those weaknesses to provide a secure environment.

The following are some ways that someone can gain access to a system:

- Operating system attacks
- Application-level attacks
- Scripts and sample program attacks
- Misconfiguration attacks

For a computer to be useful it has to have an operating system installed. An operating system takes a hunk of metal and turns it into a useful device. The operating system does for a computer what windows and doors do for a house. They take an entity and make it useful and enjoyable to its owner.

The problem is that most operating systems weren't designed with security in mind. If one adds to this the complexity of most operating systems and the speed with which they were developed, it is almost guaranteed that any operating system will have many security holes that can be exploited.

Also, most operating systems were not designed for the way they are currently used. For example, neither Windows nor UNIX was designed to be used out-of-the-box with default installations, as servers or workstations with a high level of security. They were not designed to be firewall operating systems or to house secure Web servers. With a considerable amount of effort and knowledge, they can be turned into that, but they weren't designed for this. Yet most companies take an out-of-the-box default install of an operating system and use it to house their firewalls.

#### Operating system attacks

An attacker breaks in by finding the doors and windows into a computer system. In a lot of cases the operating system provides that gateway because the real doors and windows of an operating system are the services it is running and the ports it has open. Thus, the more services and ports that are open, the more points of access. Based on that, one would hope that a default install of an operating system would have the least number of services running and ports open. Then if you needed a service or ports you could install these on your system and thus control the points of compromise in the system. Yet in reality the opposite is done; the default install of most operating systems has a large number of services running and ports open. The reason most manufacturers do this is simple: money. They want a consumer of their product to be able to install and configure a system with the least amount of effort and trouble. They know that every time a consumer has a problem with the product and has to call for support, it costs the customer money. Also, the fewer calls a user needs to make, the less frustration a user experiences, which increases satisfaction with the product.

If customers installed operating systems and the services they needed — such as Web and authentication — were not present, most customers would have to call for help. So, the argument runs: just install everything by default — then if it's needed it's there. Not all such services are actually needed, however. In fact, the customer may not even realize such a default service is there until an attacker has used it to hack his company. From a software manufacturer's standpoint it makes sense to have these services — the manufacturer gets fewer calls. But from the consumer's standpoint it doesn't make sense because by default his company has installed a very non-secure operating system, which most companies don't know to fix. They're not familiar enough with operating systems to realize how vulnerable they really are. To make matters worse, once the operating system is installed companies think their job is done and they fail to apply patches and updates. This leaves a company with an outdated operating system, which has a large number of vulnerabilities. Not a good position to be in from a security perspective.

#### Application-level attacks

A major problem with most software under development is that the programmers and testers are under very tight deadlines to release a product. Because of this, testing is not as thorough as it should be. The problem is even worse because software being developed has so much added functionality and complexity that even with more time the chances of testing every feature would still be small. Also, until very recently, consumers were not especially concerned about security. If the software had all the great features they needed they were happy, regardless of the number of security vulnerabilities. Security cannot be an add-on component; it has to be designed into an application from the beginning.

#### Scripts and sample program attacks

Extraneous scripts are responsible for a large number of the exploits. When the core operating system or application is installed, the manufacturer distributes sample files and scripts so that the owner of the system can better understand how the system works and can use the scripts to develop new applications. From a developer's standpoint, this is extremely helpful. Why go in and recreate the wheel, when you can use someone else's script and just build on it.

An area with many sample scripts is Web development. The earlier versions of Apache Web Server and some Web browsers came with several scripts and most of them had vulnerabilities. Also, a lot of the new scripting tools that come with Web browsers enable developers with minimal programming knowledge to develop applications quickly. In these cases, the applications work but what's going on behind the scene is usually pretty scary from a security standpoint. There's usually a lot of extraneous code and poor error checking, which creates an open door for attackers. Active server pages (ASP) are a perfect example. A lot of early ASP development introduced back doors that attackers were able to exploit.

#### Misconfiguration attacks

Sometimes systems that should be fairly secure are broken into because they weren't configured correctly. In order to maximize your chances of configuring the machine correctly, remove any unneeded services or software; this way the only things left on your system are the core components you need, and you can concentrate on making these secure. With some other issues, such as problems with the operating system and applications, you're at the mercy of the vendor. But misconfiguration is one thing you can control because you're the one configuring the system. So make sure you spend the time to do it right. Remember, if you don't do it right the first time, attackers will break in and there won't be a second time.

### Elevating privileges

The ultimate goal of any attacker is to gain domain administrator or root access to a machine. Attackers sometimes gain root access at the start, but at other times they get a lower level of access. For example, some keep guest accounts active with limited access. These are used by consultants or traveling employees to gain minimal access to the system. An attacker may compromise the guest account because it is fairly easy to do, and then try to upgrade their access with additional privileges.

Elevating privileges makes a lot of sense because getting a foot in the door at a low level is relatively easy and opens the way for additional access. Attackers take the course of least resistance. If it's going to take them three weeks to gain root access directly, but only a day to get guest access and another day to use that access to gain root privileges, that's much more efficient from the attackers' standpoint.

### Denial of service

One of the last ways to exploit a system is to deny access for legitimate users. In this case, the attacker would either overload the machine so it can't process legitimate requests, or crash the machine. For example, if users at a particular company store large amounts of data to the file server, an attacker can have a program write random data to the file server until all of the hard-disk space is full. Then when legitimate users try to save files, they will be denied access because there's no space left on the system.

Unlike attacks to gain or increase access, denial-of-service doesn't provide direct benefits for attackers. For some attackers it's enough just to have the satisfaction of denying access. But if the site being attacked is a competitor, who is taken off line and forced out of business, then the benefit to the attacker may be real enough.

Another purpose of a denial-of-service attack may be to take a system offline so that a different kind of attack can be launched. One common example is session hijacking. With session hijacking an attacker takes over an existing active session. In order to do this, one of the machines that is communicating needs to be taken off-line so that the attacker can take over its session. In order to do this, the attacker would launch a denial-of-service attack against that machine so that it can no longer reply.

## Uploading programs

Once attackers have gained access, they usually perform some set of actions on the server. There are few cases where someone gains access just for the sake of gaining access. Most often they either upload or download files or programs from the system. Why would attackers waste time gaining access if they weren't going to do anything with it? From an information theft or corporate espionage standpoint, once access is gained the goal is to download information in as covert a manner as possible and exit the system.

In most other cases, the attacker wants to load some programs to the system. These programs can be used to increase access, compromise other systems on the network, or upload tools that will be used to compromise other systems on the Internet. Why should attackers use their own machines when they can use someone else's? These hijacked machines may be faster and it's harder for someone to trace the attack to its source.

## Keeping access: Back doors and Trojans

Once attackers gain access to a system, they usually want to put in a back door so they can get back in whenever they want to. A back door can be as simple as adding an account to the system. This tactic has a high chance of detection if the company reviews active accounts. However, if there are thousands of users, there's still a good chance no one will notice.

What's scary is that most companies don't track what's on their system or who has access to the system. This means if attackers gain access they can make sure they'll continue to have it for a long time. Attackers also want to maintain access so they can use those computers as a staging area to launch attacks against other companies. One way they do this is by loading large amounts of programs and code to the server. Then when they want to launch an attack they log on to the system and run the code from the remote host. This has two benefits. First, from a traceability standpoint, it will look as if the company whose machine is being used is launching the attacks. And from a resource standpoint, there's a good chance that the company being used has faster machines and more disk space than the attacker, who now can use that capacity to run attacks against other sites.

A more sophisticated type of back door is to overwrite a system file with a version that has a hidden feature. For example, an attacker could overwrite the logon daemon that processes request when people log on to the system. For most users the logon process works properly but if the attacker provides a certain user ID, it will automatically allow root access into the system. These modified programs are commonly referred to as Trojan horse programs because they have a primary feature (overt) and a hidden feature (covert). Another type of back door is to install a program running on a certain port. The attacker connects and gains full access to the system or even the network.

Usually with a back door an attacker has already gained access to a system and just wants to restore that access at a later time. But what if an attacker wants to gain access and create a back door at the same time? A common way is to give the user a program with a hidden feature that creates a way for an attacker to gain access. These programs are commonly referred to as Trojan horses. A Trojan horse is a program that has an overt and a covert feature.

## Covering one's tracks

Once an attacker has compromised a machine and created a back door for later access, the last thing to do is to avoid getting caught. What good is creating a back door if someone can easily spot and close it? Therefore, the final step is to cover one's tracks. The most basic thing to do is to clean up the log files. The log files keep a record of who accessed what and when; if anyone looks at the log file they'll know an unauthorized person was in the system and exactly what was done. So the attacker wants to knows where the log file is so it can be cleansed of entries relating to the attack.

It would be easy to delete everything from the log file, but also very suspicious. Besides this, most systems put an entry in the log file indicating that the file has been cleared — a red flag that should raise fear in the heart of any system administrator. This is why it's so important to send logging to a different machine and ideally have the log information go to a write-only medium. This minimizes the chances of someone being able to go back and clean up the log file.

A common technique of attackers is to turn off logging as soon as they gain access to a machine. This way they don't have to worry about going back and cleaning up the log files — and no one will know what they did. This requires additional expertise but is extremely effective. But the thing to remember is that if logging is done correctly, even attackers turn off logging the system will still record that they entered the system, where they entered from, and other useful information.

If an attacker has modified or overwritten files, part of the clean-up process is to make sure the changed files do not raise suspicion. Most files have dates showing when they were last accessed and the size of the file. There are programs that can be run to make sure this information has not been changed and to raise a flag if it has been. But even so, there are still ways an attacker can fool the system.

Some mechanisms that can be used to hide programs and files and for covering tracks include hidden directories, hidden attributes, tunneling, steganography, and Alternate Data Streams (ADS). ADS is a compatibility feature of the Windows NT File System (NTFS) that provides the ability to fork file data into existing files without modifying characteristics such as the file's size or function. This feature provides a means of concealing rootkits and other malicious code, which can be executed in a hidden manner. NTFS regards a file as a set of attributes such as the data in the file and the name of the file.

# Summary

An accurate picture of network security cannot be obtained by using only one method. Each test has a specific purpose and meets specific needs independently. To obtain an accurate snapshot of security implementations and adherence to policies, both testing methods (penetration testing and security assessments) should be conducted.

Security assessments allow for the review of key documents and the security framework for the given network. When a good security assessment incorporates a full penetration test this allows the audit professionals an opportunity to provide full value for the customer's dollar. The customer receives a complete report outlining the status of network security implementations, inside and out, and a determination can be reached as to the customer's overall compliance with its own policies and the requirements of any federal laws or mandated procedures.

A security assessment is crucial to meet security objectives and requirements, but without the added benefit of the penetration test, gaps may be left in the security architecture.

Penetration testing is the process of simulating attacks on a network and its systems at the request of the owner or senior manager. It uses a set of tools and procedures, similar to those of malicious attackers, to measure an organization's resistance to attack and to evaluate any other security weaknesses found. Some organizations use periodic penetration tests to assess their network security posture and to make sure their current security measures are working effectively.
