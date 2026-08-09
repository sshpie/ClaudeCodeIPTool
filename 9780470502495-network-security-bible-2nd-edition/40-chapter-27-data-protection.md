# Chapter 27. Data Protection

**IN THIS CHAPTER**

- **Understanding the importance of data protection**
- **Identifying issues with endpoint security**
- **Determining the dangers and methods for dealing with insider threats**

The most critical part of an organization is its intellectual property. While an organization never wants its systems to be compromised, if the impact is minimal and no sensitive data is compromised, the damage is contained. However, if critical intellectual property is compromised, the impact could not only be devastating but could impact the ability of the organization to continue performing its mission.

In this chapter, we will look at the importance of data protection and how it ties into endpoint security and insider threats.

When dealing with protecting data or critical information the following are the key sections to focus on.

## Identifying and classifying sensitive data

Data should be clearly labeled via a digital signature, which denotes its classification and importance to the organization. The classification level should be used to determine to what extent the data should be controlled, and to reflect its value in terms of business assets. This value should be able to change each time data is created, amended, enhanced, stored, or transmitted. Using this metric allows for filtering to occur to assist in controlling user access, to prevent data from leaving an organization, and to avoid improper storage. However, other controls should be in place to prevent users from falsifying the classification level. For example, only select privileged users should be able to downgrade the classification of data.

## Creating a data usage policy

A policy, to name just a few things, should specify access types, conditions for data access based on classification, who has access to data based on classification, and what constitutes correct usage of data. Other topics should be added based upon the needs of your particular business and situation. Also, all types of policy violations should have clear consequences.

## Controlling access

Controls should be in place to restrict access to information, based on a principle of providing least privilege. These controls can be physical, technical, or administrative, and should be extremely restrictive. This helps to ensure that only appropriate personnel can access that data, and only under special conditions. For the most sensitive data, users should not be allowed to copy or store sensitive data locally. Instead, they should be forced to manipulate the data remotely. The cache of both systems, the client and server, should be thoroughly cleaned after a user logs off or a session times out, or else encrypted RAM drives should be used. Sensitive data should ideally never be stored on a portable system of any kind. All systems should require a login of some kind, and should have conditions set to lock the system if questionable usage occurs.

## Using encryption

All critical business data should be encrypted while in storage, or in transit via portable devices or a medium such as network traffic. Portable systems should use encrypted disk solutions if they will hold important data of any kind.

## Hardening endpoints and network infrastructure

Any place where business data could reside, even temporarily, should be adequately secured based on the type of information that system could potentially have access to. This would include all external systems that could get internal network access via remote connection with significant privileges, as the network is only as secure as the weakest link. However, usability must still be a consideration, and a suitable balance between functionality and security must be determined. This result should form part of the basis of an acceptable-risk policy.

## Physically securing the work environment

Your workspace area and any equipment should be secure before being left unattended. For example, check doors, desk drawers, and windows, and don't leave papers on your desk. All hard copies of sensitive data should be locked up, and then be completely destroyed when they are no longer needed. Also, never share or duplicate access keys, ID cards, lock codes, and so on.

## Backing up data

Critical business assets should be duplicated to provide redundancy, and serve as backups. Backups should be located in geographically different places to prevent disasters such as acts of nature or accidents (e.g., hurricanes, fire, or hard-disk failure) from destroying the business's IT core. Backups should be performed incrementally across multiple disks and servers, and on different time schedules (daily, weekly, and monthly).

Preferably these incremental backups should save a base copy and each modification should reflect only the changes to the base copy, or a closely matching previous version. This allows for proper versioning, and can help to serve as a form of data control.

## Improving education and awareness

Training should be provided to make users aware of the company data usage policies. Also, this serves to make employees aware that the company takes this issue seriously and will actively enforce the policy. In addition, users should be periodically reeducated and tested, to reinforce and validate comprehension. Company awareness campaigns can be used to further reinforce mindfulness. For example, simple tasks such as reminding employees to lock their computers whenever they have to be away from the system can have a huge effect in assuring the security of data.

## Enforcing compliance

Data loss prevention (DLP) and auditing techniques should be used continuously to monitor and enforce data usage policies. This should consist of both behavior and signature-based monitoring. The goal is to know how data is actually being used, where it is going or has gone, and whether this meets compliance standards. When an event is noted, real-time notifications should be sent out to alert administrators to inappropriate or potentially inappropriate data use. An investigation will occur, and if necessary violators should face appropriate consequences as outlined in the company policies. This way all end users are held accountable and are constantly reminded about the importance of data security.

## Validating processes

Implementations of policies should be regularly tested and audited to ensure compliance and to measure policy and process effectiveness. Appropriate changes should be made as needed. Third-party auditors can help to measure effectiveness because they provide objective reviews of processes and implementation.

# Endpoint Security

In today's business environment, it is increasingly important that an organization have the appropriate endpoint security tools and policy in place to deal with the evolving avenues of exploitation. The endpoints of your network are under attack constantly, so having the endpoint security infrastructure in place to deal with them is crucial to preventing data breaches. Unpatched applications, unauthorized programs, and advanced malware (i.e., rootkits) are some of the things that are encompassed in endpoint security.

With the increased usage of mobile devices, the endpoints of the network are expanding and becoming more and more undefined. Keeping mobile data protected is also going to be a difficult challenge in the future. Managers and executives are traveling with laptops and PDAs containing information that could lead to a security breach. Laptops are being stolen at an increasingly alarming rate, and because of this, the appropriate endpoint security policy measures must be in place to mitigate these threats.

This section will discuss the core areas that your endpoint security infrastructure should encompass along with the best ways of achieving your goals.

## Hardening the OS baseline

The first step to securing your endpoints is making sure the operating system's configuration is as secure as possible. Out of the box, most operating systems come with unneeded services running that serve only to give an attacker additional avenues of compromise. The only programs and listening services that should be enabled are those that are essential for your employees to do their jobs. If something doesn't have a business purpose, it should be disabled. It may also be beneficial to create a secure baseline image OS that is used for the typical employee. And if that person needs additional functionality, those services or programs will be enabled on a case-by-case basis. Windows and Linux are two popular end-user operating systems.

### Windows

Windows is by far the most popular operating system used by consumers and businesses alike. But because of this, it is also the most targeted operating system with new vulnerabilities announced almost weekly. There are a number of different Windows versions used throughout different organizations, so some of the configurations mentioned here may not translate to all of them. Here are some things that should be done to enhance security:

- Disable LanMan authentication.
- Ensure that all accounts have passwords regardless of whether the account is enabled or disabled.
- Disable or restrict permissions on network shares.
- Remove all services that are not required, especially telnet and ftp, which are clear-text protocols.
- Enable logging for important system events.

### Linux

Linux is an operating system that has become more popular in recent years. Even though some claim that it's more secure than Windows, some things still must be done to harden it correctly:

- Disable unnecessary services and ports.
- Disable trust authentication used by the "r commands."
- Disable unnecessary setuid/setgid programs.
- Reconfigure user accounts for only the necessary users.

## Patch management

Ensuring that all versions of the applications that reside on your endpoint system are up to date is no easy task but it's essential for good endpoint security. When new vulnerabilities are found in a Web browser used by the end user, patches must be implemented immediately so that a compromise does not occur. There are groups that will dissect security patches and develop exploits for them that will compromise unpatched hosts, making it essential that you patch as soon as possible.

Patch management also involves updating the signature files used by your automated endpoint security tools such as your antivirus software. If these signatures are not up to date, new exploits could infect machines — exploits that would be detected if the signatures were up to date.

One of the best ways to ensure security is to make the signature and patch updates automatic. But organizations don't always implement automatic updates. For critical infrastructure, patches need to be thoroughly tested to ensure that no functionality is affected and no vulnerabilities are introduced into the system.

The sole job of some tools residing on the endpoint system is to check patch levels of applications. These programs can be beneficial to an organization's overall endpoint security if patch management has become a problem.

## Automated tools

Automated tools that reside on the endpoint system are essential to mitigating the effectiveness of malware. The next sections will cover some of the core elements of each of these tools.

### Antivirus

Antivirus software is one of the most widely adopted security tools for either personal or commercial use. There are many different antivirus software vendors in the market, but they all use pretty much the same techniques to detect malicious code, namely signatures and heuristics.

Signatures, the most popular way to detect malicious code, are collected from malware specimens by the antivirus vendors. These signatures are basically the malware's fingerprints, which are collected into huge databases for use in an antivirus scanner. That's why it is critical that the antivirus application stays up to date—so that the latest signatures are present.

A slightly more advanced technique is heuristics. Instead of relying on malware that has been seen in the wild, as signatures do, heuristics tries to identify previously unseen malware. Heuristics detection will scan the file for features frequently seen in malware such as attempts to access the boot sector, writing to an EXE file, or deleting hard-drive contents. A threshold must be set by the administrators to determine what will trigger malware detection. This threshold must be set just right for heuristics scanning to be effective.

### Personal firewall

A personal firewall is a program installed on the endpoint machine that controls the network traffic to and from a host system. Unlike a normal firewall that sits between networks or security domains, personal firewalls reside only on end-user systems. Many personal firewalls will prompt the user each time a connection is attempted; whether they deny or allow the connection will modify the security policy for the user. For an organization, you don't want to leave this decision up to the users, so it it's important to set the security policy on a global scale across the organization.

### Host IDS/IPS

Traditional intrusion detection systems (IDS) and intrusion prevention systems (IPS) will perform deep packet inspection on network traffic and log potential malicious activity. Host IDSs, on the other hand, will monitor only the internals of a computing system. A host-based IDS will look at the system state and check whether contents appear as expected. A technique called integrity verification is used by most host-based IDSs. Integrity verification works on the principle that most malware will try to modify host programs or files as it spreads. Integrity verification tries to determine what system files have been unexpectedly modified. It does this with computing fingerprints, in the form of cryptographic hashes, of files that need to be monitored when the system is in a known clean state. It then scans and will issue an alert when the fingerprint of a monitored file changes. The main problem with integrity verification is that it detects the malware infection after the fact and will not prevent it.

### Anti-spyware/adware tools

Anti-spyware and adware tools do exactly what their name implies. They are designed to remove or block spyware. Spyware is computer software installed without the user's knowledge. Usually its goal is to find out more information about the user's behavior and to collect personal information. Anti-spyware tools work very closely to the way antivirus tools work; many of their functions overlap. Most have signatures that need to be updated and most will scan the Window's registry or other system files looking for signatures of known specimens.

### Centralized security management console

Because of the many different tools running on a given endpoint, managing them all can be a difficult task. That's why it is best practice to use a security management console that consolidates the configuration of all these applications into one area. A centralized console cuts down the management time of these applications significantly and allows managers to focus their efforts in other areas.

## Client access controls

Having tight controls in place that restrict what the user of an endpoint can and cannot do is an important part of endpoint security. System critical files, start-up scripts, and other important data should have tight controls on what users and groups are allowed to read, write, or execute. In the security industry, the term that describes the proper use of these concepts is the *principle of least privilege*.

Following the principle of least privilege should be a key component of endpoint security in every organization. Basically, the principle states that users should be given only the rights required to do their jobs, for the minimum time necessary. When malicious code is run on a machine, it generally runs with the permissions of the user launching the code. So the more privileges a user has the more damage malicious code can do when executed. Giving administrator privileges to users at your endpoint when they do not specifically need them creates greater risk to the network.

Examples of following the principle of least privilege include reducing the number of administrator or root accounts to a minimum with strong passwords. Also, super-user accounts should be used only when absolutely necessary. Checking e-mail and doing routine tasks should not be done in these accounts. Another important task that would fit into this principle is setting your resource permissions properly. The system tools and configuration files that are the most targeted by attackers should have their permissions tightened so that these malicious users can't gain a foothold in the network.

## Physical security

Physical security is often overlooked when discussing endpoint security; you hear about the latest antivirus and personal firewalls but physical security is often left out. In reality, having a poor policy on physical security for your endpoints could lead to a full compromise of your data or even network. With the increase in mobile devices in today's organizations, it's extremely critical that these devices be protected properly.

One of the first steps toward good endpoint security is the protection of the physical cases for your endpoint computers. Each workstation should be locked down so that the case cannot be removed from the immediate area. Also a lock should be placed so that the case cannot be opened up, exposing the internals of the system. If the case is not locked, hard drives or other sensitive components that store data can be removed and easily compromised. It's also good practice to implement a bios password to prevent attackers from booting into other operating systems using removable media. For desktop systems that store critical or proprietary information, encryption of the hard drives can also be implemented. This will help avoid the loss of critical information even if there is a breach and computers or hard drives are missing.

Business users are constantly on the go, so the use of laptops and mobile devices has increased and will continue to do so. Mobile devices can include such items as PDAs, USB flash drives, iPods, and Bluetooth devices. For these devices, the correct policies must be in place and followed by users in order to effectively secure the devices.

With laptops, the biggest issue is loss and theft. There continue to be cases of laptop theft that end by exposing to malicious parties the personal data left on the hard drive. Full-disk encryption should be used on every laptop within an organization. Also, using public wi-fi hotspots is never a good idea unless a secure communication channel such as a VPN or SSH is used. Account credentials can be easily hijacked through wireless attacks and can lead to compromise of an organization's network. Because a laptop is likely to be used in numerous different network environments, it's also important that all other endpoint security practices be followed.

Mobile devices can carry viruses or other malware into an organization's network and extract sensitive data from a business. Because of these threats, mobile devices need to be controlled very strictly. Devices that are allowed to connect should be scanned for viruses, and removable devices should be encrypted.

It is important for organizations to focus in on the data, not the form factor of the device it resides on. Often people have cell phones that contain sensitive information, yet there is minimal security protection applied to the device. If a laptop and cell phone contain the same information they should be protected in the same manner. Organizations usually have fairly good protection on laptops and minimal protection on cell phones. If they have the same information, they should have the same-length passwords.

## Vulnerability assessments

Some people may not think that vulnerability assessments belong in the category of endpoint security, but they can be an effective tool when used properly. Vulnerability assessments usually consist of port scanners and vulnerability scanning tools such as nmap and Nessus. What these tools do is scan the endpoint systems from an external machine, looking for open ports and the version numbers of those services. The results from the test can be cross-referenced with known services and patch levels that are supposed to be on the endpoint systems, allowing the administrator to make sure that the systems are adhering to the endpoint security policies.

## Endpoint policy management/enforcement

It's critical that you have the right policy in place to deal with all the issues that arise in endpoint security. It is also important that people are aware of the policies and that they are properly enforced by your administrative or IT team.

### User education

User education is extremely important for endpoint security and security in general. It's important that users know the do's and don'ts of what they are allowed to do on their endpoint systems. Security measures are in place to limit what users can do but those tools aren't perfect. If users open every attachment in every e-mail, chances are that some zero-day attack or other exploit, the signature of which is not in your antivirus database, will compromise a machine. Bad surfing habits and downloading files from vendors you don't trust are just a sampling of things users do that undermine the security of a system or network. Because of this, users need to be educated about the responsibilities and best practices of proper computer usage.

### Remote access

Remote access to corporate networks is also becoming commonplace. Users are working from home at an increasing rate, which is one reason it's critical to lock down and secure the connections that are used for remote access. Strong authentication is essential when connecting remotely. It is also important that the machines users are employing for remote access to the network are also secured properly. These machines are, in essence, now endpoints of the network, and proper security measures should be in place to make sure malware doesn't spread from them into the internal network.

### Virtual machines

Virtual machines are being used more frequently in organizations because these allow the organization to consolidate hardware, isolate applications, improve CPU utilization, and test more easily. But because all virtual machines share hardware resources, the compromise of one could lead to the compromise of other virtual machines on the device. So a policy has to be in place to make sure all virtual machines have good security practices. Each virtual machine is only as strong as the weakest one.

### NAC

Network access control or NAC is a fairly new security technology that does a lot to enhance the endpoint security of a network. Before giving you access to the network, NAC checks the system's endpoint security to ensure that it meets the predefined security policy. It will check to make sure that the host has the latest antivirus software or the latest patches; if the conditions are met, the host is granted access to the network resources. If the conditions are not met, NAC will quarantine the endpoint until the proper updates are made to permit access.

# Insider Threats and Data Protection

Organizations continue to spend an exceptional amount of time and money to secure the network at the perimeter from external attacks; however, insider threats are becoming more and more prominent and a key cause of data exposure. Many surveys and reporting groups have reported insider incidents to be greater than 50 percent of all attacks; however, most organizations don't report insider attacks out of fear of business loss, ridicule, and embarrassment. Insider threats are a growing concern that must be addressed.

Insider threats include attacks, or threats of attack, from both authorized and unauthorized insiders. An authorized insider is one who is known and trusted by the organization and has certain rights and privileges. An unauthorized insider is someone who has connected to the network behind the perimeter defenses. This could be someone plugged into a jack in the lobby or a conference room, or someone who is using an unprotected wireless network connected to the internal network. Insider attacks can include anything from sniffing data to abusing legitimate rights and privileges. Organizations often don't deploy as many, if any, monitoring systems on the internal network. They're mainly concerned with watching what is coming in through the perimeter from the Internet. However, insider attacks are more common and often more dangerous.

Organizations can combat insider threats with measures for both prevention and detection. Preventive measures are the classic methods of least privilege and access control. Data is protected by giving users the least amount of access they need to do their jobs. Other preventive measures include system hardening, anti-sniffing networks, and strong authentication. Among common detection measures are include many forms of user and network monitoring, among them both network and host-based intrusion detection systems. They are typically signature-, anomaly-, behavioral-, or heuristics-based. For example, a signature-based method may look for known attacks on the internal network. An anomaly or behavioral system may profile and monitor users as they use an application or database. When users perform an action that deviates from the profile, an alert is triggered. In more restrictive systems, automatic preventive measures can temporarily disable a user's account when he deviates from the profile. A policy-based prevention method to implement any of these involves user background checks and security clearances. This establishes a degree of trust for the users allowed inside, but does not entirely mitigate the potential problem.

Many current products can solve parts of the problem when implemented in a layered defense. Most mitigations are known techniques and come down to policy enforcement. System hardening and access control should be applied just as much to protect against insiders as it would be to protect against outsiders. Any open source or commercial IDS can be used to monitor the network.

# Summary

As you have seen, data protection encompasses a lot of topics and areas. It's critical for good network administrators and security professionals to keep all their security tools up to date and to use good policy management. With so many policies to enforce and applications to keep up to date, this would seem like a daunting challenge for any security team. That's why it's important to centralize endpoint security management so that a single console can be used to check patch levels, monitor system performance, and change system configurations. This makes life easier for administrators and allows them to do their jobs more efficiently, with time to keep tabs on the latest threats and update their policies accordingly.

Another challenge with data protection is minimizing the impact on the end user. None of the security tools running or configuration changes should affect the productivity of the user in any way. Also, programs such as antivirus, personal firewalls, and host intrusion detection systems tend to sap bandwidth and processing power from important end-user functionality. For this reason, when deciding what programs to use to protect end users, look carefully at how big a footprint the program uses and its memory utilization.

Mobile devices are adding additional complexity, but with the right policies and procedures it's not impossible to have good endpoint security for your organization. One of the key factors is keeping your users educated on the policies and on their responsibilities in keeping the network safe.
