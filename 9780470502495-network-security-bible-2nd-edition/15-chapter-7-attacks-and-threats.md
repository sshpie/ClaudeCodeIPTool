# Chapter 7. Attacks and Threats

**IN THIS CHAPTER**

- **Malicious code**
- **Review of common attacks**
- **External attack methodologies overview**
- **Internal threat overview**

Attacks are going to occur so knowing how to detect and respond to attacks is a critical skill set for working in cyber security. Formal methods and procedures have been developed to provide a structured approach to this difficult problem. By understanding the various attacks and threats an organization can build more robust defensive measures.

This chapter discusses these techniques as well as the different types of attacks.

# Malicious Code

Malicious code is intended to harm, disrupt, or circumvent computer and network functions. This code can be mobile, such as Java applets or code in the Active X environment. It can also attach itself to legitimate code and propagate; it can lurk in useful applications or replicate itself across the Internet. The following sections describe these different types of *malware*.

## Viruses

A *virus* is code that attaches to a host program and propagates when the infected program is executed. Thus, a virus is *self-replicating* and *self-executing*.

Viruses are transmitted in a variety of ways, including as part of files downloaded from the Internet or as e-mail attachments.

Viruses and closely related types of code fall into the following categories:

- **Macro viruses**— These viruses are one of the most common types found and these infect applications such as Microsoft Word or Excel. Recall that a macro is a set of low-level instructions within an application that is useful in performing repetitive operations, including modifying and deleting files. In operation, macro viruses attach to an application's initialization sequence. When the application is opened, the virus executes instructions before transferring control to the application. Following this activity, the virus replicates itself and attaches to other code in the computer system.
- **File infectors**— File infector viruses usually attach themselves to executable code, such as .com or .exe files. The virus is then installed when the code is loaded. Another version of a file infector associates itself with a file by creating a virus file with the same name, but with an .exe extension. Therefore, when the file is opened, the virus file will execute.
- **System or boot-record infectors**— Boot-record viruses attach to the master boot record on hard disks or the boot sector on diskettes. When the system is started, it will look at the boot sector and load the virus into memory, where it can propagate to other disks and computers.
- **Polymorphic viruses**— These viruses conceal themselves from identification through varying cycles of encryption and decryption. They employ a variety of different encryption schemes requiring different decryption routines. In practice, the encrypted virus and an associated mutation engine are, initially, decrypted by a decryption program. The virus proceeds to infect an area of code. The mutation engine then develops a new decryption routine and the virus encrypts the mutation engine and a copy of the virus with an algorithm corresponding to the new decryption routine. The encrypted package of mutation engine and virus is attached to new code and the process repeats.
- **Stealth viruses**— Stealth viruses take over system functions to conceal themselves. They do this by compromising virus-scanning software so that the software will report an infected area as being uninfected. These viruses conceal any increase in the size of an infected file or changes to the file's date and time of last modification.
- **Trojan horses**— A Trojan horse is a program that hides in a useful program and usually has a malicious function. A major difference between viruses and Trojan horses is that Trojan horses do not self-replicate. In addition to launching attacks on a system, a Trojan horse can establish a back door that can be exploited by attackers. For example, a Trojan horse can be programmed to open a high-numbered port, which could be scanned and make the system vulnerable to attackers.
- **Logic bombs**— A logic bomb is malicious code that is appended to an application and is triggered by a specific occurrence, such as a logical condition, a specific time, a specific date, and so on.
- **Worms**— Worms differ from viruses in that they do not attach to a host file, but are self-contained programs that propagate across networks and computers. Worms are commonly spread through e-mail attachments, which, when opened, activate the worm program. A typical worm exploit would involve the worm sending a copy of itself to everyone in an infected computer's e-mail address book. In addition to conducting malicious activities, a worm spreading across the Internet and overloading e-mail servers can result in denial-of-service attacks against nodes on the network.
- **Droppers**— A dropper is a program used to install viruses on computers. In many instances, the dropper is not infected with malicious code and, therefore, might not be detected by virus-scanning software. A dropper can also connect to the Internet and download updates to virus software that is resident on a compromised system.

# Review of Common Attacks

Attacks against network resources are common in today's Internet-dependent world. Attacks are launched for a variety of reasons, including monetary gain, maliciousness (as a challenge), fraud, warfare, and to gain an economic advantage. Attacks are directed at compromising the confidentiality, integrity, and availability of networks and their resources and fall into the following four general categories:

- **Modification attack**— Unauthorized alteration of information
- **Repudiation attack**— Denial that an event or transaction ever occurred
- **Denial-of-service attack**— Actions resulting in the unavailability of network resources and services, when required
- **Access attack**— Unauthorized access to network resources and information

Specific instantiations of these types of attacks are discussed in the following sections.

## Denial-of-service (DoS)

A denial-of-service (DoS) attack hogs or overwhelms a system's resources so that it cannot respond to service requests. A DoS attack can be effected by flooding a server with so many simultaneous connection requests that it cannot respond. Another approach would be to transfer huge files to a system's hard drive, exhausting all its storage space. A related attack is the distributed denial-of-service (DDoS) attack, which is also an attack on a network's resources, but is launched from a large number of other host machines. Attack software is installed on these host computers, unbeknownst to their owners, and then activated simultaneously to launch communications to the target machine of such magnitude as to overwhelm the target machine.

Examples of DoS attacks include the following:

- **Buffer overflow**— A process receives much more data than expected. If the process has no programmed routine to deal with this excessive amount of data, it acts in an unexpected way that the intruder can exploit. For example, a ping-of-death attack exploits the Internet Control Message Protocol (ICMP) by sending an illegal ECHO packet of more than 65K octets of data, which can cause an overflow of system variables and lead to a system crash. Buffer overflows usually try to push exploit code on the stack and then modify the return pointer to execute the malicious code.
- **SYN attack**— In this attack, an attacker exploits the use of the buffer space during a Transmission Control Protocol (TCP) session initialization handshake. The attacker floods the target system's small "in-process" queue with connection requests, but it does not respond when a target system replies to those requests. This causes the target system to time out while waiting for the proper response, which makes the system crash or become unusable.
- **Teardrop attack**— The length and fragmentation offset fields in sequential Internet Protocol (IP) packets are modified. The target system then becomes confused and crashes after it receives contradictory instructions on how the fragments are offset on these packets.
- **Smurf**— This attack involves using IP spoofing and the ICMP to saturate a target network with traffic, thereby launching a DoS attack. It consists of three elements: the source site, the bounce site, and the target site. The attacker (the source site) sends a spoofed ping packet to the broadcast address of a large network (the bounce site). This modified packet contains the address of the target site. This causes the bounce site to broadcast the misinformation to all of the devices on its local network. All of these devices now respond with a reply to the target system, which is then saturated with those replies.

## Back door

A back-door attack takes place when someone creates an alternative way into a system bypassing the traditional security controls. This is normally done using dial-up modems or asynchronous external connections. The strategy is to gain access to a network through bypassing control mechanisms, getting in through a back door such as a modem.

## Spoofing

IP spoofing is used by an intruder to convince a system that it is communicating with a known, trusted entity to provide the intruder with access to the system. IP spoofing involves an alteration of a packet at the TCP level, which is used to attack Internet-connected systems that provide various TCP/IP services. In this exploit, the attacker sends a packet with an IP source address of a known, trusted host instead of its own IP source address to a target host. The target host may accept the packet and act upon it.

## Man in the middle

A man-in-the-middle attack involves attackers injecting themselves in the middle of communications — for example, attacker A, substituting his or her public key for that of another person, P. Then, anyone wanting to send an encrypted message to P using P's public key is unknowingly using A's public key. Therefore, A can read the message intended for P. A can then send the message on to P, encrypted in P's real public key, and P will never be the wiser. Obviously, A could modify the message before resending it to P.

## Replay

A replay attack occurs when an attacker intercepts and saves old messages and then tries to send them later, impersonating one of the participants. One method of making this attack more difficult to accomplish is through the use of a random number or string, called a *nonce*, which changes with time. If Bob wants to communicate with Alice, he sends a nonce along with the first message to Alice. When Alice replies, she sends the nonce back to Bob, who verifies that it is the one he sent with the first message. Anyone trying to use these same messages later will not be using the newer nonce. Another approach to countering the replay attack is for Bob to add a timestamp to his message. This *timestamp* indicates the time that the message was sent. Thus, if the message is used later, the timestamp will show that an old message is being used.

## TCP/Hijacking

An attacker hijacks a session between a trusted client and network server. The attacking computer substitutes its IP address for that of the trusted client and the server continues the dialog believing it is communicating with the trusted client. Simply stated, the steps in this attack are as follows:

1. A trusted client connects to a network server.
2. The attack computer gains control of the trusted client.
3. The attack computer disconnects the trusted client from the network server.
4. The attack computer replaces the trusted client's IP address with its own IP address and spoofs the client's sequence numbers.
5. The attack computer continues dialog with the network server (and the network server believes it is still communicating with the trusted client).

## Fragmentation attacks

A fragmentation attack is used as a method of getting packets around a packet-filtering firewall. In a basic fragmentation attack, packets are broken into fragments with the first packet containing the complete header data. The remaining packets do not contain any header information. Because some routers filter packets based on this header information, the remaining packets without header data are not filtered and pass through the firewall.

Two examples of fragmentation attacks follow:

- A *tiny fragment attack* occurs when the intruder sends a very small fragment that forces some of the TCP header field into a second fragment. If the target's filtering device does not enforce minimum fragment size, this illegal packet can then be passed on through the target's network.
- An *overlapping fragment attack* is another variation on a datagram's zero-offset modification (similar to the teardrop attack). Subsequent packets overwrite the initial packet's destination address information, and then the second packet is passed by the target's filtering device. This action can happen if the target's filtering device does not enforce a minimum fragment offset for fragments with non-zero offsets.

## Weak keys

For many cryptographic algorithms, some keys are weaker than others (that is, some keys are not as secure as other keys). Strong keys are generated using truly random number generators. For specific algorithms, keys can be tested for their strength. For example, the data encryption standard DES has only 16 weak keys out of its 256 possible keys. Because weak keys for an algorithm can be identified, they should not be used.

When an algorithm has keys that are all of equal strength, it is said to have a *linear* or *flat key space*. Conversely, if an algorithm has keys that are not all of equal strength, it has a *nonlinear key space*.

The same use of randomness applies to passwords in that the more random the choice of letters and characters in a password, the more secure the password is. However, the more random the sequence of letters and characters in a password, the more difficult it is for a person to remember.

## Mathematical attacks

Mathematical attacks refer to the use of mathematics to break passwords or cryptographic algorithms as opposed to other approaches, such as brute force, which try all possible combinations of patterns.

A good example of a mathematical attack is the use of factoring algorithms to break the RSA public key cryptography algorithm. Recall that the hard problem in RSA is determining the prime factors of a large number. Numbers on the order of 129 digits have been factored using factoring algorithms and thousands of computers on the Internet. One of the better factoring algorithms is the number field sieve (NFS).

## Social engineering

This attack uses social skills to obtain information such as passwords or PIN numbers to be used against information systems. For example, an attacker may impersonate someone in an organization and make phone calls to employees of that organization requesting passwords for use in maintenance operations. The following are additional examples of social engineering attacks:

- E-mails to employees from a cracker requesting their passwords to validate the organizational database after a network intrusion has occurred
- E-mails to employees from a cracker requesting their passwords because work has to be done over the weekend on the system
- E-mails or phone calls from a cracker impersonating an official who is conducting an investigation for the organization and requires passwords for the investigation
- Improper release of medical information to individuals posing as doctors and requesting data from patients' records
- A computer repair technician convincing a user that the hard disk on his or her PC is damaged and unrepairable and needs to be replaced. The technician then takes the original hard disk to extract information and sells the information to a competitor or foreign government.

The best defense against social engineering attacks is an information security policy addressing social engineering attacks and educating the users about these types of attacks.

## Port scanning

A cracker can use scanning software to determine which hosts are active and which are down; this is a technique to avoid wasting time on inactive hosts. A port scan can gather data about a single host or hosts within a subnet (256 adjacent network addresses). A scan can be implemented using the Ping utility. After determining which hosts and associated ports are active, the cracker will initiate different types of probes on the active ports. Examples of probes are as follows:

- Gathering information from the Domain Name System (DNS)
- Determining the network services that are available, such as e-mail, FTP, and remote logon
- Determining the type and release of the operating system

## Dumpster diving

Dumpster diving involves the acquisition of information that is discarded by an individual or organization. In many cases, information found in trash can be very valuable to a cracker. Discarded information may include technical manuals, password lists, telephone numbers, and organization charts. It is important to note that one requirement for information to be treated as a trade secret is that the information be protected and not revealed to any unauthorized individuals. If a document containing an organization's trade secret information is inadvertently discarded and found in the trash by another person, the other person usually can use that information because it was not adequately protected by the organization.

## Birthday attacks

Birthday attacks are made against hash algorithms that are used to verify the integrity of a message and for digital signatures. A message processed by a hash function produces an output message digest (MD) of fixed length, independent of the length of the input message. The MD uniquely characterizes the message. For a strong hash algorithm, H, and message M, the following is true:

- It should be computationally infeasible to find two messages that produce a common message digest (that is, H(M1) ≠ H(M2)).
- If there exists a message and its corresponding message digest, it should be computationally infeasible to find another message that generates that specific message digest.
- It should be computationally infeasible to find a message that corresponds to a given message digest.
- The message digest should be calculated using all the data in the original message.

The birthday attack refers to the probability of finding two random messages that generate the same MD when processed by a hash function. This question is analogous to asking how many people must be in a room to have a greater than 50 percent chance of at least two of them having the same birthday. The answer is 23.

## Password guessing

Because passwords are the most commonly used mechanism to authenticate users to an information system, obtaining passwords is a common and effective attack approach. Access to a person's password can be obtained by looking around the person's desk for notes with the password, "sniffing" the connection to the network to acquire unencrypted passwords, using social engineering, gaining access to a password database, or outright guessing. The last approach can be done in either a random or systematic manner.

### Brute force

Brute-force password guessing means using a random approach by trying different passwords and hoping that one works. Some logic can be applied by trying passwords related to the person's name, job title, hobbies, or similar items.

### Dictionary attack

A dictionary attack is one in which a dictionary of common passwords is used in an attempt to gain access to a user's computer and network. One approach is to copy an encrypted file that contains the passwords and, applying the same encryption to a dictionary of commonly used passwords, compare the results. This type of attack can be automated.

## Software exploitation

Vulnerabilities in software can be exploited to gain unauthorized access to information systems' resources and data. Some examples of software exploitation follow:

- **AIX operating system**—Passwords can be exposed by diagnostic commands.
- **Web server**—An attacker can cause a DoS buffer overflow by sending a large GET request to the remote administration port. This causes the data being sent to overflow the storage buffer and reside in memory as executable code.
- **IRIX operating system**— A buffer overflow vulnerability enables root access by an attacker.
- **Windows**— A vulnerability enables an attacker to locate system and screensaver passwords, thereby providing the attacker with means to gain unauthorized log on access.
- **Windows XP**— Privilege exploitation software used by an attacker can gain administrative access to the operating system.
- **Windows Vista/Windows 7**— Stack overflow issue in the kernel allows administrator access.

Many software-related vulnerabilities can be avoided by applying good software-engineering techniques during the software development process and anticipating possible attacks. For example, proper parameter checking can be incorporated into software to prevent buffer overflow attacks.

Additional software-related issues are described as follows:

- **Antivirus management**— If personnel can load or execute any software on a system, the system is more vulnerable to viruses, to unexpected software interactions, and to the subversion of security controls.
- **Software testing**— A rigid and formal software testing process is required to determine compatibility with custom applications or to identify other unforeseen interactions. This procedure should also apply to software upgrades.
- **Software utilities**— System utilities can compromise the integrity of operating systems and logical access controls. Their use must be controlled by a security policy.
- **Safe software storage**— A combination of logical and physical access controls should be implemented to ensure that the software and copies of backups have not been modified without proper authorization.

## Inappropriate system use

This activity relates to the use of business computers and resources for non-business or personal use, such as downloading inappropriate material from the Internet, conducting personal stock trading transactions, making personal travel reservations, conducting outside business, and so on. Strictly speaking, this is an attack against an organization's resources by using them for unauthorized purposes.

## Eavesdropping

Eavesdropping attacks occur through the interception of network traffic. This situation is particularly prevalent when a network includes wireless components and remote access devices. By eavesdropping, an attacker can obtain passwords, credit card numbers, and other confidential information that a user might be sending over the network. Examples of the various manners of eavesdropping include the following:

- **Passive eavesdropping**— Unauthorized, covert monitoring of transmissions
- **Active eavesdropping**— Probing, scanning, or tampering with a transmission channel to access the transmitted information

## War driving

In war driving or walking, an attacker scans for 802.11-based wireless network information by using a laptop computer with a wireless adapter in promiscuous mode and scanning software such as NetStumbler or Kismet. Also, a Global Positioning System (GPS) might be used to note the location of compromised nodes.

## TCP sequence number attacks

In this type of attack, the attacker makes the target believe it is connected to a trusted host and then hijacks the session by predicting the target's choice of an initial TCP sequence number. This session is then often used to launch various attacks on other hosts.

## War-dialing/demon-dialing attacks

In war dialing, an attacker uses a program that automatically places calls to a group of telephone numbers in hopes of finding numbers that are connected to modems. In demon dialing, a brute-force, password-guessing approach is used to gain access to a system through a modem.

# External Attack Methodologies Overview

The hacker threat, whether it's a single person, or a nation state, is on the rise. The Estonia Cyberwar of 2007 highlighted the threat of one nation taking offline the critical infrastructure of another. This is an illustration of how a political event — taking down a physical statue — offended another country, which decided to launch a denial-of-service attack against Estonia's connectivity to the Internet. Since Estonian business relies heavily on the Internet, this had an economic impact to the country. While the methods were not new, the focus and apparent support from a nation state served as a proof of the concept of possible attacks to come. These methodologies, once understood, can be mitigated by counter-measures in order to better prepare and reduce the risk from such attacks in the future.

## Distributed denial-of-service attacks (DDoS)

DDoS attacks are simple and effective, with the intent of bringing your network's availability to a screeching halt. DDoS attacks fall into the following types:

- Consumption of network/system resources
- Changing network configurations to reroute or interrupt network connectivity
- Network session resets
- Disruption of network switches/routers, resulting in connectivity loss for a number of systems

Examples of some denial-of-service types are discussed in the sections that follow:

### TCP SYN flood attacks

This type of flood attack abuses the client/server three-way handshake. During a normal three-way handshake, a client sends the server a SYN message and the server sends back a SYN-ACK, with the client finally sending an ACK back, completing the handshake. TCP SYN flood attacks abuse this process by setting up a client to not send back the final ACK message, causing what is known as a "half-open" connection. This half-open connection can be easily created via IP spoofing. An attack client will send a spoofed SYN packet to the target server, but when the server tries to send an SYN-ACK back, the spoofed IP is unable to close the handshake with an ACK.

As a result, the server fills up its memory with data describing all these pending connections. Once this memory is filled, new legitimate connections will be rejected until the memory is cleared. Servers will eventually time-out the spoofed requests, which can be filled again by the attacking client. In some cases the system may crash from the constant requests.

There are a few countermeasures to TCP SYN floods, depending on the type of services the network is providing. Placing servers behind a firewall configured to stop inbound SYN packets will prevent this type of attack. For those devices that provide public Web services requiring random SYN requests, a number of configurations can be set to increase the size of the connection queue and to decrease the time-out on the open connections.

### Smurf IP attack

This method uses ICMP echo requests targeted toward broadcast IP addresses. These ICMP requests are originated from a spoofed "victim" address. For instance, if the intended victim is 10.0.0.10, the attacker would spoof an ICMP echo request from 0.10 to the broadcast address of 10.255.255.255. This request would go to all IPs in the range, with all the responses going back to 0.10, thereby overwhelming the network. This process is repeatable, and is automated to generate huge amounts of network congestion.

This attack method depends on a few key capabilities of the network that can be disabled. One such configuration would be to disable IP-directed broadcasts at the routers. This would prevent the ICMP echo broadcast request at the network devices. Another option would be to configure the end systems to keep them from responding to ICMP packets from broadcast addresses. If a network device allows for ICMP echo broadcast requests, the systems on that network would simply not respond to the request.

### Ping of Death

This type of attack uses malformed IP packets to "ping" a target system with an IP size over the maximum of 65,535 bytes. IP packets of this size are not normally allowed, but by fragmenting the IP packet, once reassembled by the target a size larger than the maximum can be achieved. When attempting to reassemble the packet, the target system may experience buffer overflows and other crashes. Prevention of the Ping of Death can be accomplished by placing a firewall to check fragmented IP packets for maximum size. Those that are over the maximum are discarded.

### Botnets

Currently, millions of systems infected with a Trojan are collected into what are known as "botnets" in order to carry out DoS attacks ([Figure 7-1](ch07.html#diagram_of_botnet_configuration)).

![Diagram of botnet configuration](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0701.png)

**Figure 7.1. Diagram of botnet configuration**

These techniques become effective when they are distributed across these botnets and focused on one or a few systems. One such potential botnet is created by the Conflicker worm, which is estimated to have infected between 1.5 and 2 million systems worldwide. The payload for these worms can be command and control software by which the target system can be controlled at any time for a centralized location. These bots or zombie systems are then instructed to carry out attacks against the target, often overwhelming the target's bandwidth and processing capabilities. These DDoS attacks are difficult to trace because of the large number of zombies located in differing geographic locations.

## Targeted hacks/espionage

When bringing down a network is not the goal, high-value targets may be attacked specifically for sensitive information. Whether it's a `monster.com` database, or the unclassified e-mail of the Pentagon, target attacks have the goals of being stealthy, patient, and focused on obtaining sensitive information for personal use, espionage, or for sale on the black market. Most targeted attacks follow a generic method of intelligence gathering, active scanning, exploitation, and maintaining access. Once access is maintained, the attacker can choose to rerun any of the phases to deepen the grip on the overall network.

[Figure 7-2](ch07.html#diagram_of_the_steps_in_an_attack) describes the overall cycle, with detail of each phase.

### Intelligence gathering

The first phase of a targeted attack, gathering intelligence about the target, assists the attacker in strategizing and preparing for the actual event. This phase may take some time as crucial information about the target is discovered. Part of this phase may include social engineering methods, where the attacker may call personnel within the target organization to gain details such as unlisted phone numbers, usernames and passwords, IP addresses, and any other inside knowledge that may assist with the attack.

![Diagram of the steps in an attack](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0702.png)

**Figure 7.2. Diagram of the steps in an attack**

Another physical technique is dumpster diving. The attacker will look through the target's trash for information that is simply thrown out. Sensitive information such as network diagrams, schematics, and organization telephone directories can be a treasure trove for an attacker.

In addition to the physical intelligence gathering, information can be gathered through passive scanning. Google searches on the target organization can result in basic organization charts, e-mail schema, and other information useful to the attacker. "Who is" queries can provide Internet addresses, domain names, mail servers, host information records, and points of contact. These techniques are known as passive scans because most of this information is publicly available without the risk of detection by the target organization.

### Active scanning

Using the information gathered during Phase 1, the attacker can now start to identify critical systems and vulnerabilities. Automated tools such as port scanners, vulnerability scanners, and network mapping programs are used to identify on the target network the points of potential failure. This phase is also known as footprinting, and is differentiated from Phase 1 due to the fact that the potential for detection increases.

### Exploitation

Potentially the most damaging phase of the attack, exploitation, uses the information from the previous phases to break into the target system. During this phase, the attacker penetrates the system defenses by way of a vulnerability that can occur over the local area network, or Internet. If the goal is to bring down the target system, the previous detailed denial-of-service techniques can be employed more effectively. The attacker's success depends on the target system's architecture and configuration, the skill level of the attacker, and the level of access gained (user, admin, domain admin, and so on).

### Maintaining access

Once the attacker has gained access, it will be important for that attacker to maintain the access without being discovered by the target system. The attacker can choose to continue to use the exploited system to gain further access to the target network, or to launch attacks from within. During this phase, the attacker will attempt to remove evidence of the initial attack, install trojans/rootkits/back doors to ensure repeat access, and may also choose to "harden" or patch the vulnerable system in order to prevent other attackers from gaining access via the same exploit. Once the system is "owned" by the attacker, sensitive information can be gathered and offloaded at will.

# Internal Threat Overview

Internal threats need not only apply to malicious activities. User error and ignorance play a large role in trusted individuals putting networks and systems at risk to outside agents. The Marine One incident in 2009 brought to light the risk of trusted individuals unknowingly sharing sensitive data on the Internet. Firewalls, intrusion detection systems, and other boundary defense mechanisms are not effective when circumvented by insiders.

## Unintentional filesharing

Laptops can provide companies and their employees the flexibility to conduct business while at home, or on the road. This flexibility also extends the network's security boundary outside the company's control, creating unintentional risks to sensitive information.

Filesharing programs, often referred to point-to-point (P2P) programs, are intended to share movies, music, and other files. By default many of these programs, such as limewire and bearshare, will scan your hard drive for folders containing media files, and share these folders out to the network. Other users on the network now have access not only to the media files, but to all other files within the directory.

In addition to the release of sensitive data, P2P programs can chew up network bandwidth.

While end user systems are connected to the corporate network, connectivity can be controlled at the boundary via firewalls. In addition, proper configuration control of the end systems can detect installation of unauthorized software such as P2P programs.

Another mitigation is tighter controls on what exactly the end user can do. Implementing a "least privileged" policy for end systems can mitigate many risks, including unintentional filesharing. By not allowing the end user to have administrative privileges, you can keep malicious software from being executed.

## Device loss and theft

Often the most embarrassing and damaging form of attack is that of property loss. Most newsworthy breaches involve stolen or lost laptops, many times containing millions of sensitive customer records, technical documents, or health records. For instance, the Veterans Affairs department had one of its laptops stolen in 2006. This particular laptop contained sensitive data for approximately 26.5 million vets and military personnel. The laptop, stolen from the employee's home, was ultimately recovered and no identity theft incidents were reported, but a few missteps caused this case to be an embarrassment to the VA. First, it was perceived that the VA was attempting to place blame on the employee. Documentation was later discovered that the employee had permission to work with this data from home. Second, this large amount of data was released unencrypted.

Since this incident, full hard-drive encryption has gotten the attention and application it deserves. HDD encryption works by requiring a user name and password to decrypt the hard-drive sectors and start up the operating system. By adding this level of protection, laptops and other devices that are lost or stolen only lose their physical value, and not the sensitive data they contain..

Cyber threats to sensitive data, whether from the malicious outsider, or the unknowing insider, will always present challenges to the way networks and systems are protected. Understanding the multiple attack vectors in which sensitive data can be lost can better prepare organizations with countermeasures to operate through the attack, minimize risk, and recover when an incident does occur.

# Summary

The only way to a good defense is to understand the offense. This chapter reviewed various threats that are used by attackers to disrupt and compromise information systems. Attacks can take the form of DDoS assaults, social engineering, war dialing, and brute-force password guessing to gain unauthorized access to critical infrastructures and valuable intellectual property. By building proper defenses, organizations can properly secure their enterprises from these threats.
