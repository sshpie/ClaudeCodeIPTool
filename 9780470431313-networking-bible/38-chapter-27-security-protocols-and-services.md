# Chapter 27. Security Protocols and Services

**IN THIS CHAPTER**

- Securing networks
- Different attacks and exploits
- Protecting systems
- Methods of encryption
- Kerberos network security system

Network security is best achieved by a set of layered and overlapping technologies. In this chapter, you learn about the different points of attack that can be used to compromise networked systems and gain access to them and the data that they contain. Network vulnerabilities can be scanned for, and some standard tools such as the National Vulnerability Database and related resources are described.

This chapter presents a checklist of the most important steps you can take to secure a network.

Two adaptive network security technologies are presented. One is called Location Awareness, and it can be used to detect the status of a network connection and its state and adjust system policies appropriately. Another technology called Network Access Protection can proactively quarantine systems that don't conform to a system health policy.

Sending traffic over the Internet involves insecure connections. You will learn about three different Internet security protocols in this chapter: IPsec, Transport Layer Security/Secure Socket Layer, and HTTPS. These technologies either encrypt data or create secure connections through tunneling and other methods.

Different methods used to encrypt network traffic are considered in this chapter. Various forms of encryption are used in cryptography, and the use of symmetric and asymmetric key algorithms is considered. These ciphers can be used to authenticate and validate data, as well as prevent the data from being compromised. As an example of these types of technologies, the Kerberos security system is described.

# Network Security Overview

Your network is under attack by increasingly sophisticated and constantly evolving means. Today's news always seems to include the latest virus, Trojan, or worm; your mail contains a letter from your bank telling you that your credit card information has been hacked. If your network seems flaky or some system is acting up, you are excused for feeling paranoid. Keeping your network secure is a little like the cartoon *Spy vs. Spy*. These are uncertain times we live in, but you can discourage attackers by hardening your network, thus directing them away from your network and toward softer targets.

There is no single method for protecting a network. Any security system can be cracked or compromised, if not from the outside then certainly from the inside. The best way to secure a network is to have different layers of security so that an attacker must compromise two or more systems in order to gain access. Changing security parameters such as passwords regularly and securely partitioning different portions of a network are two other methods that are invaluable. In this chapter, you learn about some of the technologies used to secure networked systems and the traffic that flows over a network.

## Network vulnerabilities

Network vulnerability is a weakness that can be exploited to gain access to that system. There are any number of ways that a system can be compromised: through poor password selection, viruses or Trojans, software bugs, an executable or script running inside the system, or through code injection. When a vulnerability becomes known and is used by others to attack similar systems, it is referred to as an exploit. Exploits travel as quickly as viruses do.

All software contains bugs or routines that can be compromised. The patches that companies offer on a regular basis, such as Microsoft Update, are meant to remove these vulnerabilities once they are discovered. When patches are released, they are analyzed for the flaws that they are meant to fix by people interested in attacking systems. An attack based on that flaw is then rushed out, and is very effective because it takes a while for systems to be updated. Attacks of this type are referred to as Zero Day exploits. Believe it or not, there are companies that provide a subscription service that informs their clients how to use Zero Day exploits to attack systems, and other companies that provide this information to clients so that they can protect themselves. Spy versus spy.

The best-practice recommendation for managing Zero Day exploits is to update and patch all systems as soon as patches become available. Many system administrators cringe at this suggestion as a best practice because patches can introduce their own problems. Patches can fix some problems while creating other problems. Automatically updating production systems introduces an element of uncertainty that wouldn't be there if the system's software were static.

One method used to uncover network vulnerabilities is to probe a network with a risk analysis tool, which is sometimes called a vulnerability scanner. Vulnerability scanners work by scanning a network for all assigned IP addresses, determining which ports are open, and building a list of applications and operating systems that are running on the various systems. Scanners of this type are port scanners, network scanners, and Web site scanners, as well as dedicated tools contained in management frameworks. Once the initial survey is complete, the scanner may either build a map of the network or create a report. If the scanner uses SNMP, WMI, or another management protocol, it can query systems and applications to determine not only what they are, but also their version numbers and patch levels. Vulnerability ratings can be assigned that provide administrators with check lists for actions that they need to perform in order to secure their network further.

An industry standard for measuring the severity of computer system vulnerability is called the Common Vulnerability Scoring System (CVSS). This metric is based on a set of measurements, and includes base or intrinsic vulnerability, perceived threats over time or temporal metrics, and deployment or environmental metrics. For more information on how this scoring system is structured, you can go to the CVSS FIRST (Forum of Incident Response and Security Teams) Web site at `www.first.org/cvss/`. The CVSS Special Interest Group, or SIG, develops this standard, which is currently at version 2. The metrics can be entered into an online calculator provided by the National Vulnerability Database in the CVSS scoring section to obtain the specific ratings (see the following section).

Several of these tools are publicly available; one example is Microsoft's Baseline Security Analyzer (MBSA; `http://technet.microsoft.com/en-us/security/cc184924.aspx`), version 2.1 being the latest one released. The MBSA uses the Microsoft Update infrastructure and a local agent to determine if a Windows system is secure and up to date. According to Microsoft, this Web-based service performs a vulnerability assessment on some three million systems a week. MBSA can not only scan systems such as Vista/Server 2008 but can also scan Windows CE and Embedded, Microsoft SQL Server, and Microsoft Internet Information Server. An MBSA sample report is shown in [Figure 27.1](ch27.html#a_sample_vulnerability_report_created_by).

![A sample vulnerability report created by the Microsoft Baseline Security Analyzer](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2701.png)

**Figure 27.1. A sample vulnerability report created by the Microsoft Baseline Security Analyzer**

Information used to determine network vulnerability is maintained by a number of companies and organizations, including:

- Common Vulnerabilities and Exposures (`CVE;` `http://cve.mitre.com`)
- Computer Emergency Response Team (`CERT;` `www.cert.org`) at Carnegie Mellon University
- Microsoft Security Response Center (`www.microsoft.com/technet/archive/community/columns/security/essays/vulnrbl.mspx`)
- Open Source Vulnerability Database (`OSVDB;` `www.osvdb.org`)
- Open Web Application Security Project (`www.owasp.org/index.php/Category:Vulnerability`)
- SANS Institute (`www.sans.org`)
- Secunia vulnerability archive (`http://secunia.com`)
- SecurityFocus vulnerability archive (`www.securityfocus.com/bid`)
- Secwatch vulnerability archive (`http://secwatch.org`)
- VUPEN security vulnerability archive (`www.vupen.com/english/security-advisories/`)

Vulnerability scanning or network reconnaissance is also used by attackers attempting to gain entry to a network and is a feature of some worms.

## The National Vulnerability Database

The entry for Common Vulnerabilities and Exposures, or CVE, at the start of the bullet list in the previous section refers to a dictionary of security threats that is maintained by the MITRE Corporation for the National Cyber Security Division of the United States Department of Homeland Security. CVE uses a system of identifiers that uniquely identify known security risks. These risk factors are sometimes referred to as CVE Identifiers, names, numbers, ID, or simply CVEs and are listed in the database when identified by outside parties as a candidate risk factor. Candidate risk factors are given Candidate Numbers (or CANs), and promoted to CVEs once they are reviewed and authenticated.

MITRE Corporation's function in maintaining the database is to run the editorial board, be the Candidate Numbering Authority, and make the information available to the public. The CVE database is available to the public to use for free and lists threats known internationally, along with a description of the threat's exposure and severity. From the standpoint of the CVE, a vulnerability is a software error that provides access to a system or network. An error in applying software correctly or leaving a system open is not considered a vulnerability and is not listed in the database. For example, your network operating system may allow strong passwords to be set but you do not require passwords or enforce strong passwords; that would not be considered a vulnerability. (Short passwords are subject to dictionary and brute force attacks.)

Vulnerabilities occur when:

- The attacker can execute a command as if they were a different user
- The attacker can access data that they aren't privileged to see
- The attacker can spoof another identity
- The attacker can create a situation where service is denied to others

You can perform a CVE search on the National Vulnerability Database (NVD), as found at `http://nvd.nist.gov/`. [Figure 27.2](ch27.html#the_national_vulnerability_database_list) shows the Web page for an NVD search. The database currently lists 34,977 known vulnerabilities and can be downloaded for offline use. The data in this database supports the U.S. Information Security Program (ISAP) and serves as the content repository for the Security Content Automation Protocol used to monitor network security and provide threat assessments.

The NVD uses a structured naming system for different types of information technology systems, software, and other packages that is similar to the syntax used in Uniform Resource Identifiers (URIs) that are used on the Internet. This naming system is called the Common Product Enumeration, or CPE, Product Dictionary, and it is maintained as part of the database in XML format, which is available for download. The CPE XML file can be downloaded at `http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.1.xml`.

![The National Vulnerability Database lists known network security threats and provides related information about their severity and potential fixes.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2702.png)

**Figure 27.2. The National Vulnerability Database lists known network security threats and provides related information about their severity and potential fixes.**

## Points of Attack

Most often, network security is breached from the outside in. Typical attacks involve attacks on software or hardware vulnerabilities. However, exploits that are able to get inside the network are often most effective because they can operate stealthily.

The most common points of attack are:

- **Outside: System availability**. Systems can be overloaded by a spoof ICMP broadcast that results in a flood of ECHO replies to the system being attacked, called a smurf attack.
- **Outside: Denial of Service (DoS)**. An attack where a service is overwhelmed by requests is referred to as a Denial of Service (DoS) attack. A DoS attack against domain name servers (DNS) is a common example of a DoS attack; when it is successful, it has the effect of making other system addresses on the Internet or intranet irresolvable and therefore makes those systems unavailable.Distributed Denial of Service (DDoS) attacks refer to attacks by a large number of compromised systems that are zombies and can turned into a botnet, literally a robot network.
- **Outside/Inside: Authentication**. In a spoof, the attacker assumes the identity of another user.
- **Data in transit:** Traffic intercepted in transit, modified, and then sent on to its destination is called a man-in-the-middle attack. Data can also be subjected to eavesdropping.
- **Inside: Worms, Trojans, and other backdoor exploits** provide an attacker with a method for controlling systems inside the network and can create zombie computers. Backdoor exploits can be an executable program or algorithm that is able to evade network authentication, perform actions, and remain undetected.Rootkits are a form of backdoor exploit where the program is able to hide as a low-level driver or kernel module and therefore escape detection. Rootkits do not show up in file systems and may appear in process lists as a normal system process.
- **Direct internal access**. Attacks can take the form of media such as optical disks, USB keys, portable drives, and other media.

Microsoft uses a threat assessment model that they call the STRIDE approach (`http://msdn.microsoft.com/en-us/magazine/cc163519.aspx`) in developing their software. STRIDE stands for the following:

- **S**poofed identity (authentication). This lets an attacker impersonate another user. Users and systems must be authenticated; authentication can be through passwords, digital certificates, and other methods.
- **T**ampering of data (integrity). Attackers alter data. Methods used to maintain integrity include performing error-checking routines on data.
- **R**epudiation (non-repudiation). Individuals deny responsibility for their actions.
- **I**nformation disclosed (confidentiality). Attackers gain access to sensitive information. Networks restrict access to data using security access lists, domains, directory services, and other features of network operating systems to only the people who should have access.
- **D**enial of Service (availability). DoS attacks can make an essential service unavailable. Users and systems must be reliably linked to events that they initiate. Event logs may be maintained that provide audit trails, user and system credentials can be added to data, and secure communication channels can be established for transfer of data. Backup systems for important systems should exist and provide failover.
- **E**levation of privilege (authorization). A user or system wants to acquire more rights than they are enabled to have. Resources must be available when needed. Systems for managing resource access must be secure, and users must be given the lowest level of access that is suitable for their work.

## Principles of secure network design

Security measures should focus on three separate levels:

- **Risk assessment and prevention**. Among the most effective technologies for risk prevention are user access control, cryptography, and firewalls. Firewalls are described in detail in [Chapter 28](ch28.html).
- **Threat detection**. Threat detection systems include virus and spyware scanners, intrusion detection systems (IDS), event auditing, and heuristic analysis of event logs.
- **Response**. Responses to intrusion and compromise can involve system or subnet quarantine, restoring to known good backups, remediation, and protection upgrades.

### Tip

Given the complexity of modern systems, a compromised system can never be repaired with 100 percent confidence that the system has been returned to perfect health. Hackers or crackers have become increasingly sophisticated in the methods that they use to infect or control systems, and may embed components as replacements for fundamental system components. Therefore, it is strongly recommended that you maintain multiple system images that you can use to return a system to a former state. For mission-critical systems, consider mirrors, Business Continuity Volumes (BCVs), and other forms of hot backup.

From the standpoint of expense and difficulty, each of the three levels of security is typically one order of magnitude more expensive than the level above it. That is, threat detection can cost 10 times what prevention measures might cost, and response can cost 100 times prevention measures as a rule of thumb. Think about how much installing virus and spyware scanning software or a firewall costs compared to the amount of time and expense it takes to remediate multiple systems that are compromised.

One of the important principles of secure network design is to minimize what is called the "attack surface" of a system or network. The attack surface is the exposed profile of a system that is available for view to a user or an attacker. The profile of an attack surface includes any of the following:

- Protocols running on the network or system
- Network interfaces that can respond to queries or messages
- Open ports
- Services running on an accessible system
- User input fields

With fewer avenues by which an attacker can penetrate a system, the security risks are lowered. However, once an attacker does gain entry to a system, a low attack surface doesn't limit the amount of damage that can be done.

Microsoft Internet Security and Acceleration (ISA) Server is an example of the concept of "secure by default." ISA Server is a content-caching gateway and proxy server and was developed from Microsoft's original Proxy Server. When you install ISA Server, all ports are closed, no protocols are active, and there are no defined entries into your network. You initialize ISA Server by opening the ports you want to allow traffic in and out on, and mapping traffic on HTTP port 80 to ISA's port 8080, and some additional ports for HTTPS, FTP, IMAP, or whatever service you want to allow. The next steps define which systems can send data, and which systems you will allow data to be received from. You define a set of rules, and those rules are applied in an order that imposes a hierarchy or precedence. It can be time-consuming to create the network security policy, but it does impose the smallest possible attack surface that ISA Server can be used for.

Here are the 14 Commandments of Network Security Practices:

1. **Use a firewall**. Always operate behind a firewall. Choose a hardware firewall in preference to a software firewall, and ensure that the firewall provides both physical and protocol isolation. A system attached to the Internet without a firewall can be compromised in minutes.
2. **Enforce strong passwords**. Always change any default password; use passwords that are at least eight characters long and combine upper- and lowercase alphabetic, numeric, symbol characters in strings that are not encountered in a dictionary.
3. **Install virus and spyware scanning software**, particularly at the gateways of your network.
4. **Have a robust system backup policy**. Keep system images for all systems.
5. **Patch your software**. Always apply patches as soon as they become available, but have backups available in case problems arise. Pay particular attention to any public network-facing software. It is particularly important to patch Web server and Web browser software, for example.
6. **Segment your network into subnets**. This provides physical isolation by IP addresses.
7. **Encrypt any sensitive data and use secure protocols for data transfer**. Don't send any data in plain text that you wouldn't allow to be published in the *New York Times*.
8. **Beware of downloadable content, hyperlinks, and unsolicited e-mail**. Turn off script execution as a default.
9. **Lower your attack surface**. Close all unnecessary ports, and turn off all unused network protocols.
10. **Beware of network shares and providing full access to shared resources**. Shares offer a potent mechanism for viruses, worms, Trojans, and other malicious software to propagate through a network. Use a strong network operating system access list control policy.
11. **Beware of mobile systems and mobile media**. Isolate traveling laptops until they are verified safe, and ensure that sensitive systems lock out media such as USB keys.
12. **Secure means secure**. Ensure that you have secure connections when using forms or HTTPS connections. Verify connections by checking the security certificates of sites. Close your browser when a secure session is completed; don't simply close a browser tab.
13. **Be a policy wonk**. Make good use of your network operating system's security policies.Security polices in Windows Server 2008 can lock resources by users and groups, deny software or device driver installation, prohibit the use of different device classes, lock down desktops and browsers, control access to e-mail attachments, prevent DVD burning, perform network quarantine, set user account protection actions, and perform other services. Perhaps 40 percent of the 2,400 policy settings in Windows Server 2008 are security related. Other network operating systems and add-on policy engine products, such as Novell ZenWare, offer security policy settings.
14. Be kind to your mother, to children and small animals, and to any network administrators that you encounter; and pay your taxes.

If you do all of these things on the list above, your network will be a hard target and you will be blessed.

# Location Awareness and Network Access Protection

There are so many different ways in which a network can be attacked that what you really need to combat a portfolio of threats is an adaptive network strategy. Microsoft has developed a couple of these strategies and shipped them with Windows Server 2008 and Vista. The first technology is called Network Location Awareness (NLA), and it refers to the ability of a Windows server to detect system, connection, and session states and adjust the policies applied to a client appropriately.

In many instances, network clients either use a `PING` or send an `ICMP` packet to determine if a network resource can be connected to. When a laptop connects to a Windows domain using `PING, PING` is the mechanism that the domain would use to ascertain the state of the client. So if `PING` fails, the domain will not be able to apply its Group Policy. `ICMP` is often turned off at firewalls, so that mechanism is also unavailable for client connection modification. To solve these problems, NLA is established and client information is exchanged using a VPN connection. Every time the VPN connection refreshes, the Group Policy for both users and machines also refreshes.

With Network Location Awareness, it is possible to make the following changes in client states:

- Options can be automatically set during a Pre-Execution Environment (PXE).
- A client's group policy is updated automatically when the client connects to the domain. Other events, such as connecting a mobile device, establishment of a VPN session, a client's arousal from hibernation or standby, or the promotion of a system isolated in quarantine to the production network, all fire a Group Policy refresh.
- Clients are configured based on the resources that are detected. When a network interface card isn't detected, the driver software for that card isn't loaded automatically. Suppression of unnecessary driver downloads provides shorter boot cycles.
- The bandwidth to a client can be made part of the policy that is applied when the client connects to the domain.

There is a second approach to network protection called Network Access Protection (NAP), and it is also a resource management approach based on defined policies. NAP evaluates the condition of enabled clients (Vista) when they attempt to log into a domain. Before the client is authenticated and provided with a network connection, they are evaluated to determine if any of the following policies are violated:

- The client's firewall is turned on.
- The client's anti-virus and anti-spyware software is running, their signatures are up-to-date, and a scan has been performed recently.
- All Microsoft patches have been applied.
- Other policies specific to your particular network are violated.

Failure to meet the requirements results in a system being quarantined until remediation can be done to the system to bring it up to full compliance. NAP provides the additional measures required to ensure that network security isn't compromised from within, and represents a new direction that many network operating systems will adopt to make networks more secure. These types of systems can be modified as system policies to adapt them to specific network configurations and needs. [Figure 27.3](ch27.html#network_access_policy_separates_healthy) shows a diagram of a NAP system implemented with Windows Server 2008.

In a fully configured NAP service, the NAP policy engine is supported by Health Requirement and Trusted Health Registration Authority servers. Supporting the identification and authentication of clients are Directory servers and a Certificate server. When a NAP client fails to meet the health policy requirement, it is logged into a separate subnet where it is managed by a Remediation server that addresses the client's deficiencies. [Figure 27.3](ch27.html#network_access_policy_separates_healthy) shows a graphical depiction of an Internet and wireless client login with a NAP system.

![Network Access Policy separates healthy clients from suspect clients onto different networks.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2703.png)

**Figure 27.3. Network Access Policy separates healthy clients from suspect clients onto different networks.**

# Internet Security Protocols

The Internet is an inherently insecure environment. In most instances, any traffic you send over the Internet can be intercepted and cached. To ensure that data can be sent confidentially over the Internet, several different communications protocols were developed that you can use to protect your data. In the sections that follow, you will learn about three different protocols: IPsec, Transport Layer Security (formerly Secure Sockets Layer), and HTTPS.

IPsec is a method for encrypting IP traffic and validating the integrity of the data once it arrives; the required use of IPsec is one of the main reasons that IPv6 is inherently more secure than IPv4. TLS and SSL are methods for encrypting data and sending the data over the Transport layer. HTTPS is an encryption technology combined with a secure connection, which creates a tunnel from client to server. These three methods make it possible for banks to operate over the Web, governments and the military to communicate, and all of the other conveniences you take for granted in modern internetworking to be accomplished.

## IPsec

Internet Protocol Security (IPsec) is a method for encrypting and validating traffic sent over TCP/IP networks and is an open standard covered in IETF RFC 2401 (`www.ietf.org/rfc/rfc2401.txt`). The suite of protocols includes a cryptographic key-based mechanism for establishing the unique identity of connection endpoints. To use IPsec, both of the nodes must be running the IPsec protocol locally. IPsec can be sent as either unicast or multicast, and when sent multicast, all destination nodes share the same security information.

IPsec has two modes of operation:

- Transport mode
- Tunnel mode

### Note

The spelling of IPsec with a lowercase s is recommended by the IETF. You will often see IPsec written IPSec, but this book follows the IETF's guideline.

In Transport mode, the IP packet's header is left in clear text and the data or payload is encrypted. Transport mode is used to send messages between nodes. In Tunnel model, the entire IPsec packet is encrypted and encapsulated inside an IP packet. Whereas IPsec Transport mode requires that endpoints and all connection points (routers and switches) in a data path support IPsec, Tunnel mode only requires the endpoints to be running the IPsec protocol. Tunnel mode traffic can pass through any host that supports IP traffic and is often used in Virtual Private Network (VPN) communication. [Figure 27.4](ch27.html#ipsec_transport_and_tunnel_mode_datagram) shows the two datagrams in use — IPsec Transport (top datagram) and Tunnel mode (bottom datagram) where the Encapsulating Security Protocol is used to create the packet.

It is also possible to use IPsec with only one connection point supporting the protocol; then IPsec is encrypted and encapsulated at the border (or other outbound) router, and is decrypted and extracted at the border router for the destination system. When you configure IPsec this way, the traffic is visible to each of the hosts on the two networks but secure when it leaves the subnetwork that the sending system is located on.

![IPsec Transport and Tunnel mode datagram structures](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2704.png)

**Figure 27.4. IPsec Transport and Tunnel mode datagram structures**

IPsec is a Network level (Level 3) protocol in the OSI model and an Internet Layer protocol in the TCP/IP model. The most important protocols in the IPsec protocol suite include the following three protocols:

- **Authentication Header (AH)**. AH provides the mechanism for guaranteeing the authenticity of packets delivered over stateless connections. The AH uses a hashing algorithm and a shared key to create an Integrity Check Value (ICV). ICVs serve the same function as a CRC data check. The destination decrypts the data, runs the same algorithm, and determines if the ICV that it computes is the same as the one in the datagram, which establishes the authenticity of the sender.
- **Encapsulating Security Payload (ESP)**. ESP encrypts the payload data used in IPsec communication providing the means to authenticate and protect the contents of either IP v4 or IP v6 data. ESP can be used in either an encryption-only or an authentication-only mode but is usually used with both features turned on. ESP does not protect the IP header. The bottom datagram in [Figure 27.4](ch27.html#ipsec_transport_and_tunnel_mode_datagram) shows an ESP packet in Tunnel mode.In Tunnel mode the complete IP packet is encapsulated and a new header and trailer are added for transport. The packet is entirely protected in Tunnel mode. ESP header data is layered on top of the IP protocol and uses the well-known port number 50. ESP authentication data is contained in a field that uses an Integrity Check Value (ICV) to verify that the contents of the encrypted packet are correctly transported.
- **Internet Key Exchange (IKE) v1 and v2**. The IKE protocol provides a handshaking mechanism between the two connection endpoints, determines what security protocols are available and which will be used, and then creates the encryption and authentication keys that are sent to the destination system so that the packet may be identified and decrypted. IKE is described in IETF RFC 2409 (`http://tools.ietf.org/html/rfc2409`).IKE uses the Internet Security Association and Key Management Protocol (ISCAMP) to exchange data and negotiate the SA (Security Association). ISCAMP is a framework that can support different methods for key exchange. The two common key exchange protocols are OAKLEY, which is used for the basis of most of the technology of IKE key exchanges, and SKEME, from which IKE borrows some features such as its public key encryption technology.

[Figure 27.5](ch27.html#the_structure_of_ipsec_authentication_an) shows the structure of both the AH and ESP headers in Transport mode and Tunnel mode. The Payload or Data field is of variable length.

![The structure of IPsec Authentication and Encapsulated Security Payload headers](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2705.png)

**Figure 27.5. The structure of IPsec Authentication and Encapsulated Security Payload headers**

ESP encrypts the data in an IPsec datagram using one of the following three cryptographic algorithms: AES-CBC, HMAC-SHA1, or TripleDES-CBC. The endpoints in an IPsec session each have a shared key, which the destination system uses to decrypt the data. ESP can be used alone or with the AH protocol. [Figure 27.5](ch27.html#the_structure_of_ipsec_authentication_an) showed the different components of an IPsec packet that are encrypted by ESP: the ESP Header, ESP Trailer, and ESP Data. The ESP Header shown in [Figure 27.6](ch27.html#the_secure_indicator_icon_in_mozilla_fir) has an SPI parameter with its Security Association data, and the Sequence Number used to resequence packets upon arrival. The Trailer contains Padding, Pad Length, and Next Header information. An optional feature in ESP can authenticate the data field by using an algorithm to create an ICV that can be compared using the shared key.

The placement of the components of IPsec in a datagram ensures that the data is followed by any needed padding in the trailer to conform to a standard block size that some algorithms require in order to process the data. If authentication is used, the ESP Authentication Data trailer is part of the encrypted data because it would be stripped away if it were in a header field. It must also come after the data in order to be available after encryption is performed.

Because IPsec operates at the same level as the IP protocol itself, it is application independent and can be used to securely send packets originating from any application. This is not true of other secure protocols such as SSL, which operate at higher levels and require applications to include support for them.

IPsec negotiates the method used to transfer datagrams in this format between endpoints. Two endpoints with a negotiated security policy are in a Security Association. A security policy specifies which packets are secured and whether they use AH or ESP. The algorithm(s) used for encryption and those used for authentication are selected from a list and shared, as are the keys necessary to decrypt the data for both processes. Policies are stored locally in each device's Security Policy Database (SPD), and security associations are stored in each device's Security Association Database (SAD). When an IPsec datagram arrives at a device for processing, the device looks up the Security Parameter Index in the SPD and then applies the association that is stored for that SPI in the SAD.

Whereas IPsec is an optional component of IPv4 communication, it is a compulsory part of and integral to IPv6. Therefore, if you aren't using IPsec now, rest assured that sometime in the future you will be.

## Transport Layer Security

Transport Layer Security (TLS) is a set of cryptographic protocols that is used to encrypt data over TCP/IP networks at the Transport layer. This developing standard is specified by IETF RFC 5246 (`http://tools.ietf.org/html/rfc5246`). TLS is a superset of the widely known Secure Socket Layer (SSL) developed by Netscape, and used for many years. SSL 3.0 was the first Web protocol chosen by the credit card companies for secure e-Commerce transactions.

TLS both encrypts and authenticates data sent from an application on one server to an unauthenticated client so that the communication is delivered securely. It is most widely used to allow Web servers to communicate with clients such as browsers, but it can be applied to all kinds of application traffic over TCP/IP.

### Note

TLS can run into problems when used with virtual servers due to the fact that virtual servers must share the same certificate on a host. In a situation where X.509 is used as the authentication, you may need to either add a wildcard certificate or reissue the certificate when a new virtual server is used.

In its simplest form, TLS uses an authenticated server and an unauthenticated client. If you have a Public Key Infrastructure (PKI) installed, TLS can be configured so that both ends of the TLS connection can be mutually authenticated. TLS uses three steps:

1. **Negotiated protocol support**. The client sends its list of supported ciphers and hash function to a TLS server, which selects the strongest ones for use. This portion is called the TLS handshake, and it can be a full but simple handshake without authentication or a client-authenticated TLS handshake.
2. **Key exchange and single or mutual system authentication**. The server returns to the client a digital certificate, which includes the server name and its trusted Certificate Authority (CA) credential. The client may verify this information with the CA server.
3. **Symmetric encryption and message authentication**. The client encrypts a random number with the server's public key and sends that session key to the server where it can be decrypted using the server's private key. Both the server and the client then have the random number seed that they can use to feed to the different algorithms selected to generate the appropriate keys.

TLS supports a number of different cryptographic algorithms for both key creation and exchange and authentication algorithms. When two endpoints perform negotiation, they choose a key exchange algorithm, and an authentication algorithm. Message authentication involves the use of message authentication codes (MACs) that are created using cryptographic hash functions with HMAC. By contrast, SSL used a pseudorandom function to create its MACs. Taken as a whole, TLS negotiation selects from what is called a cipher suite.

In order for applications to use TLS, they must have built-in support for TLS. While TLS is used mainly for HTTP traffic over TCP transport, it has also been used to secure SMTP, FTP, NNTP, and XMPP traffic. OpenVPN (`http://openvpn.net/`) uses TLS to create a VPN connection between two endpoints. With OpenVPN, any network protocol may be used, and the program makes it appear that the destination system is local to the source. One other area where TLS is being widely used is in Voice over IP traffic where Session Initiation Protocol (SIP) signaling is encrypted and authenticated.

For many applications that lack TLS support, there are third-party products that encapsulate TLS traffic and transport it from one endpoint to another. One program called stunnel (`http://stunnel.mirt.net/`) is a free, open source multiplatform TLS/SSL tunneling application that serves as a wrapper for TLS data and can use PKI to create a secure connection.

## HTTPS

The Hypertext Transfer Protocol Secure (HTTPS) combines the Hypertext Transfer Protocol (HTTP) with either the Transport Layer Security (TLS) or Secure Sockets Layer (SSL) protocol that was described in the previous section. An authenticated Web server uses HTTPS to create a secured connection to a browser client. When you connect with HTTPS, you enter the prefix https:// into the URL in place of the standard http:// address. HTTPS traffic uses port 443 by default, unless otherwise specified.

### Note

The appearance of a lock icon in your browser indicating an SSL/TLS encrypted connection is not a guaranteed measure of security. A browser can be hijacked and still show a lock icon. Always check that the certificate matches what you expect to see and be wary.

[Figure 27.6](ch27.html#the_secure_indicator_icon_in_mozilla_fir) shows a secured connection to a local bank in the Mozilla Firefox 3.0 browser. Note that the certificate organization's icon appears to the right of the URL, and that you can click the icon to open a dialog box with more detail. Microsoft Internet Explorer 8.0 duplicates this function by placing an icon to the right of the address bar, and will go so far as to color the address bar green when a verified HTTPS connection has been made.

![The secure indicator icon in Mozilla Firefox 3.0 offers information about a site's certificate.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2706.png)

**Figure 27.6. The secure indicator icon in Mozilla Firefox 3.0 offers information about a site's certificate.**

More information is provided by all browsers with detailed information about the certificate itself. Foxfire 3.0's Certificate Viewer dialog box is shown in [Figure 27.7](ch27.html#a_digital_certificate_detail_dialog_box). Whenever you are on a secure connection and have any doubts about its authenticity, you should open the Certificate details in your browser to check that all of the information fields are populated by reasonable data. Whereas it may be possible to create or spoof a secure connection, it is extremely unlikely that anyone can spoof the fields in the certificate dialog box, as those fields are populated by a third party — the Certificate Authority server.

![A digital certificate detail dialog box from Mozilla Firefox 3.0](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2707.png)

**Figure 27.7. A digital certificate detail dialog box from Mozilla Firefox 3.0**

The certificates used by Web servers use a public key certificate that is created in software and submitted to a Certificate Authority (CA) for validation. This certificate is digitally signed by the CA, which means that it provides the necessary public key to anyone interested in validating communication from the Web server that the information contained in the certificate is valid. In order for a Web browser to be able to verify a certificate, it must have the signing certificate of the CA, and because a CA's function would be useless without that, most of the major CAs are found in all major browsers.

It is possible for organizations and individuals to have their own CAs, but those CAs are only useful for encrypting the traffic so that others cannot view the data. Personal or organizational CAs will not authenticate the sender. However, if an organization sends data from their server to their browsers, then the organization's CA will establish the veracity of the sender in that instance. In addition to server certificates, organizations can also create client certificates and load them into individuals' browsers. Client certificates can verify user information to the server without a login being required, and allow the server to verify this information whenever it connects to the client. These are very useful features, indeed.

# Encryption and Cryptography

Cryptography is the study of methods for hiding information, and is studied as both an area of computer science and advanced mathematics. There are many methods for cryptographically securing information, including using passwords, biometrics, or devices for access to information, encrypting data with algorithms and/or with the use of keys, and a myriad of other ways.

Encryption refers to the process by which information is transformed into data so that it loses its context. Decryption is the reverse process by which the data is transformed back into information that can be read and understood. Taken together, the two algorithms that both encrypt and decrypt are called a cipher. Some ciphers require the use of a key, which is information that is used to modify the action of the cipher. Keys are generally kept secret, except when a set of keys is required by the cipher. In those instances, the sender and recipient may share a public key, but do not exchange the private or secret key(s) necessary to complete the cipher. To be truly secret, a key must be variable (that is, generated freshly with each use); otherwise, it loses its ability to protect the cipher from outsiders. All of these communications, the cipher, keys, and encrypted data are subject to authentication methods that validate that the information arrived correctly and is from whom it says it is from.

Modern-day ciphers are extremely good and difficult to crack. The three best-known cryptographic algorithms used on computers are:

- **Data Encryption Standard (DES)**, designed at IBM and selected by the National Bureau of Standards as the official Federal Information Processing Standard (FIPS) for the United States government in 1976. DES uses a symmetric key algorithm and a 56-bit key. Although DES is now considered to be insecure, variations of DES such as Triple DES and the Advanced Encryption Standard (AES) are in wide use.
- **Diffie-Hellman Key Agreement Algorithm** uses a shared secret key to encrypt communication sent over insecure networks with a symmetric key cipher. The D-H algorithm was first published in 1976 by Whitfield Diffie and Martin Hellman, and was based on work using public key distribution by Ralph Merkle in the United Kingdom that was kept secret until 1997. You may sometimes (rarely) encounter this cipher under the name Diffie-Hellman-Merkle for that reason. Diffie is now the Chief Security Officer at Sun Microsystems.
- **RSA Public Key Cryptographic Algorithm** was based on work by Ron Rivast, Adi Shamir, and Leonard Adleman at MIT, published in 1977 and patented in 1983. RSA algorithms involve key generation, encryption, and decryption using both a public and private key. The public key is used to encrypt data that can only be decrypted with the private key and vice versa.

These cryptographic technologies are described in more detail in the next section. Cryptography and encryption technologies are complex fields of study that could occupy the entire content of this book. In the sections that follow, you are presented with an overview on how these technologies are most commonly applied to securing computer networks.

## Brute force and ignorance

You can never prove that a cipher is unbreakable, and theoretically all ciphers are breakable, provided sufficient resources can be provided to test them, with one notable exception. That exception is a system where a one-time pad is used as the key and that pad uses verifiably random number generation. Claude Shannon proved that a one-time pad is unbreakable, provided that the pad is fully random, applied once, and has a length greater than or equal to the data being encrypted.

No modern encryption methods conform to a perfect cipher; that ideal system is too computationally demanding. However, when the potential number of variations in a data set becomes large enough, the ability of any system to break a cipher becomes practically impossible. The following example illustrates this.

A password is a key that unlocks access to a security account. If I told you that a system used a two-letter password, all lowercase, then you could manually enter each of the 676 combinations from the universe of 262 possible passwords into the computer, and in about an hour, give or take, discover the correct combination. For upper- and lowercase combinations, the universe is 2,704 in size (522), so that would take four times as long. This approach to guessing passwords is referred to as the brute force approach. A lock with four wheels, each offering numbers 0 to 9, provides a universe of 0 to 9,999 (or 10,000) possibilities, which could take the better part of a day to crack by hand.

### Note

You'll find two-letter combinations at `www.en.wikipedia.org/wiki/List_of_all_two-letter_combinationsandthree-lettercombinations`, or Three-Letter Acronyms (TLAs), spread out over 14 Web pages at the same site.

The speed of computers makes brute force attacks even more powerful. Modern desktop computers are quite powerful — they are the mainframes of the past sitting right there on your desk. A brute force attack by a modern PC can find a password of six letters in a few hours, or a six-character password containing upper- and lowercase letters, numbers, and punctuation in a few days. An eight-character password of the complete ASCII character set might take a month or two to crack. It is pretty amazing to watch a demonstration of how powerful an attack can be just using brute force methods.

As a rule of thumb, most people trying to crack their way into a network aren't going to be willing to spend any more than a day or two at it, unless they know that the contents of the target are worth the effort.

### Note

Many security systems come with a feature called a lockout that locks the account after a specified number of failed logon attempts. This feature is designed to defeat brute force or dictionary-based attacks.

Most brute force attacks combine random guesses with a prebuilt dictionary containing most of the short letter combinations (say, up to three or four places long), as well as all of the common names and words in one or more languages. By using a dictionary-based attack, it is possible to cycle through several million common possibilities in a couple of hours, and this approach is usually more effective than simple brute force approaches because few people use truly random passwords. You can see why complex random passwords offer so much more protection than just letters, and how the amount of work to crack a password goes up exponentially with each additional place.

### Tip

There are a number of random password generators that you can find available on the Web. Some of these tools generate random passwords on the Web page itself, while others are applications that you can download or buy. The best random password generators use numbers derived from phenomena such as temperature fluctuations of a microprocessor or something similar to obtain randomness. If you use a random password generator, be sure to store your passwords in a safe place where you can refer back to them.

There are limits to brute force. The Electronic Freedom Foundation built a system called the DES Cracker in 1998 for $250,000 containing 1,800 custom chips and demonstrated that they could crack 56-bit DES in a few days. Today, systems that can perform this feat can be built for under $10,000. As you increase the size of any key, the task grows exponentially. Current technologies, such as AES, Triple DES, Twofish, Serpent, and other standards, start at key sizes of 128 bits and can be set as high as 192 or 256 bits in length.

You can use physics to argue that a 128-bit symmetric key can't be broken. The von Neumann-Landauer equation sets a value for the lowest amount of energy that you would have to consume to do a bit flip. With a universe of 2128 values (3.40 × e38) and a computer operating at room temperature, this would consume 30 gigawatts of energy (1018 joules) for a year in order to perform 2128 – 1 bit operations, and this value doesn't even begin to estimate how much power it would take to test the validity of the key. The amount of time required to perform bit flips at the rate of 1018 bit flips per second would be 1013 years, or roughly the age of the universe. This assumes that the key is randomly generated.

Some day, we may have quantum computers that can operate at much higher speeds and near zero degrees absolute, and the fundamental assumptions of this argument may no longer apply. But to paraphrase Aragorn from *The Return of the King*, "Today is not this day."

## Symmetric key algorithms

The first of the key-based cryptographic algorithms that were available for use were of a type called symmetric key algorithms. The most commonly used symmetric key algorithms use a block cipher, stream cipher, or a hash function. A brief description of these ciphers follows.

### Block ciphers

With a block cipher, the algorithm operates on a block of text using a key that translates the output into a block of encrypted text of the same size. When the size of the message is greater than the block used, the algorithm uses the block and key to encrypt the next block-sized set of characters. The process repeats until all clear text characters are encrypted. Block ciphers can iteratively repeat the block encryption, or it can alter the algorithm used for every block that is encrypted.

The Data Encryption Standard (DES) and the Advanced Encryption Standard (AES) are block cipher algorithms. Although DES isn't used for highly secure communications, the standard remains very popular due to the high speed with which it can encrypt and decrypt data. Chances are that the e-mail cipher your e-mail client uses is DES-based, as are many ATM machine communications, as well as encrypted secure connections such as remote desktops.

### Stream ciphers

A stream cipher works by generating a long key as a stream, one character after another. The creation of the key is based on a process that can't be predicted in advance, such as the generation of random passwords based on thermal variation that was described in the previous section. The longer the key, the more secure the stream cipher is.

Stream ciphers make no demand on a real-time generation of a key; indeed, you can create and store a set of stream cipher keys and use them one at a time as needed. The most well-known use of a stream cipher in this manner is called a "one-time pad." In a one-time pad, each message is encrypted using a unique key, and once used, the key is discarded — just as you would tear the top page of a pad of paper off after you used it. The key feature of a stream cipher is that each key is random and unique.

The best-known stream cipher is the RC4 standard. RC4 was developed by Ron Rivest of RSA Security and released and trademarked in 1987, but the algorithm was a trade secret until 1994. The RC comes from either "Rivest Cipher" or "Ron's Code," and variants of RC such as RC2, RC5, and RC6 have been released. In 1994, the RC4 cipher was disclosed and is now in the public domain. The RC4 algorithm is used as the encryption standard for the WPA and WEP wireless security protocols that are described in [Chapter 14](ch14.html), and for Transport Layer Security (described earlier in this chapter).

RC4 creates a pseudorandom keystream from one of the 256 possible byte combinations and two 8-bit index pointers applying a Key Scheduling Algorithm (KSA) to create a key between 40 and 256 bits in length. This keystream is then used to encrypt clear text by applying an XOR (Exclusive OR) operation bit for bit. As RC4 works its way through the clear text, a pseudorandom generation algorithm (PRGA) increments the index values to modify the keystream. XOR takes two operands and performs a logical disjunction so that the result is one or the other values but not both. A truth table like the one shown in [Table 27.1](ch27.html#an_xor_operation_truth_table) shows this operation graphically. The decryption simply repeats the process, returning the cipher text to clear text.

**Table 27.1. An XOR Operation Truth Table**

| X | Y | Result |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

RC4 isn't airtight, although it is difficult to crack. For example, the 104-bit RC4 standard used in 128-bit WEP wireless encryption can be cracked by a tool called AIRCRACK-PTW in less than a minute.

### Hash functions

The last of the common key-based cryptographic algorithms is based on hash functions. A hash function takes a message of any size and applies a short, fixed-length hash to that message, returning a shorter length (than the original input) hash value. A hash function is a mathematical function that converts a string of any size into a smaller string integer that represents the original data. You can think of a hash function as returning an index value, and that value is the hash value, alternatively referred to as a digest, hash code, hash sum, or simply a hash. A hash value can be made public without concern that the input's original data may be exposed.

Hash functions are one-way functions. Their values can be computed, but the value offers no information or method for restoring the original data. That is because the hash value is a reduced data set and does not contain sufficient information to return the original method. A hash function that is shown to be beyond the range of computation to find another input that would yield the same hash value is described as being a weakly collision-free hash function. A hash function that can be proved to uniquely describe a hash value for each unique input is referred to as a strongly collision-free hash function. [Figure 27.8](ch27.html#the_use_of_a_hash_function_to_create_a_h) shows how a hash function is applied to a message to create a hash value starting with the message block on the left and moving to message blocks on the right, each block providing input to the hash that is obtained in the lower-right corner of the figure.

Hash functions are used in error-checking algorithms, checksums, fingerprints, and other technologies. You could use hash functions to search for duplicated records in databases, search for identical genomes in database sequences, and in a myriad of other applications.

When a cryptographic hash function is applied to data such as an e-mail message, it creates a hash that is in essence a digital signature. The receiver of the message can take the encrypted data, apply the hash value, and determine if the encrypted data is identical to what was sent. Just changing one character in an encrypted message of any length will result in a completely different hash value and a mismatch when the comparison is run. Therefore hash function cryptography is a fundamental tool in data validation methodologies as it creates what are essentially digital signatures. True digital signatures require asymmetric encryption that is a private/public key pair.

![The use of a hash function to create a hash value](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2708.png)

**Figure 27.8. The use of a hash function to create a hash value**

The best known of the cryptographic hash functions is the MD4 function (now cracked and deprecated), which has been replaced by the more secure MD5 function. MD4 stands for the Message Digest algorithm developed by Ronald Rivest at MIT in 1990. MD4 uses a 128-bit digest length hash to generate the digital signature. MD4 is used to create the password checks in Windows NT, Widows XP/Server 2003, and Windows Vista/Server 2008. Many of the current generation of hash functions, including MD5, the National Security Agency's (NSA's) Secure Hash Algorithm (SHA), and RACE Integrity Primitive Evaluation Message Digest (RIPEMD), are based on the MD4 technology.

A technology related to hash functions is the cryptographic Message Authentication Code (MAC) methodology. MAC uses an algorithm and a secret key to operate on input to output a MAC or tag that represents the input value. Because a secret key is involved, not only can the data be authenticated by the tag, but the data can also be verified. MAC doesn't require that the data being evaluated be encrypted when sent, but another secret key technology called Message Integrity Code (MIC) does. When a MIC is applied to a message, you will always get the same tag returned if the same algorithm is used. With MAC, the same message returns the same tag only if the same secret key is used. Because this technology is a symmetric key encryption, MAC cannot be used as a digital signature; that is, MAC doesn't prove that the sender of the document can be uniquely identified.

With a MAC, the secret key is generated by an oracle machine, which for our purposes may be considered a black box that has a Turing machine interface. You ask the oracle machine a question and it provides an answer. For MAC, the question is what secret key do you get for a specific message. The only way that an attacker can compromise a MAC is to have not only the message, but also access to the oracle machine that generates the message. Simple access to the oracle machine will not provide the key without submitting the message.

## Asymmetric or public key algorithms

The second broad class of cryptographic key-based technologies is called asymmetric or public key algorithms. These algorithms use a public key to encrypt data and a private or secret key to decrypt and/or verify a hash of the message or the message itself. The Diffie-Hellman-Merkel and RSA algorithms that were mentioned briefly at the beginning of this topic are two asymmetric key algorithm technologies. Other algorithms in this category include Cramer-Shoup cryptosystems, ElGamal encryption, and Elliptic Curve algorithms.

You run across asymmetric key encryption with digital signature technologies, as the two keys provide a means for the public key to sign the encryption with one algorithm and the private key to verify the signature with the second. Keys can be generated as two interrelated pairs at the same time, but it is computationally impossible to calculate one key from another. The two-key combination also means that the content can be uniquely identified as having originated at one particular computer. The development of public key cryptography is considered to be one of the most important inventions in computer science of the last 50 years.

Underlying these public key algorithms are key generation technologies based on solving very hard computational problems. The three methods used are an integer factorization where a large number is created by multiplying a large number of smaller integers. RSA uses integer factorization, and it has been shown that a 200-digit number required nearly 1.5 years of work roughly equivalent to 50 years of computer time to solve. D-H-M uses a technology based on a discrete logarithm calculation where a logarithm is determined to be the solution to an equation gx = h, where g and h are members of a finite cyclic group. The third algorithm looks to compute solutions to elliptic curves based on the formula y2 = x3 + ax + b. These three problems are very difficult to compute using current computer technologies.

Digital signatures are used in all of the important public key infrastructure technologies such as SSL/TSL, VPNs, Kerberos, and others. The two most widely used public key algorithms are the Rivest-Shamir-Adleman (RSA) algorithm and the Digital Signature Algorithm (DSA).

## Kerberos

The Kerberos protocol is a network authentication system that relies on a symmetric key infrastructure and a trusted third-party system to establish the identity of communicating parties and to ensure that the data has been delivered without interference or interception. Kerberos was created to allow data to be sent over insecure connections (the Internet, for example) while ensuring that the data hasn't been snooped or retransmitted as part of a man-in-the-middle or a replay attack. Kerberos has been extended in several ways since it was developed at MIT to include asymmetric key algorithmic authentication. [Figure 27.9](ch27.html#the_microsoft_server_2008_kerberos_infra) shows the current implementation of Microsoft's Kerberos mechanism as it shipped in Windows Server 2008/Vista.

![The Microsoft Server 2008 Kerberos infrastructure and mechanism is shown here.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2709.png)

**Figure 27.9. The Microsoft Server 2008 Kerberos infrastructure and mechanism is shown here.**

The Kerberos mechanism for authentication shown in [Figure 27.9](ch27.html#the_microsoft_server_2008_kerberos_infra) works as follows:

1. The client logs into the network and the logon information is sent to the Local Security Authority (LSA).
2. The LSA passes the request onto the Authentication Service with a Request for Authentication and authentication is granted from the LSA to the client.
3. A request is made to Get Credentials from the LSA, and the LSA sends the appropriate credentials to the Client.
4. The Client begins it session.
5. A Ticket Request for a particular application, session, or operation is made from the Client to the LSA and passed along to the Ticket Granting Service (TGS). The ticket created at the TGS is returned to the client.
6. A Request is made to a Web server for secure information from an E-Commerce system.
7. That Web server may make a request to an E-Commerce Server which then sends a Get Credentials command to an LSA which passes the request to a Certificate Service (CA).
8. The CA sends the Credentials to the LSA which will then issue an Allow Session command.
9. The Web server sends the information requested by the Client.

The name Kerberos comes from the three-headed dog (Cerberus in Latin) that guarded Hades. It was developed as part of the Project Athena efforts at MIT and first appeared as version 4 in 1988. A later version, number 5, appeared in 1993 and was published by the IETF as RFC 1510. The MIT Kerberos standard is freely available for use, and many of the major players on the Internet, Sun Microsystems, Microsoft, Google, Apple, and others, formed the Kerberos Consortium to continue the development of this standard at MIT. Kerberos is used by many of the network operating systems that you have read about in this book, including Sun Solaris, BSD UNIX, Windows networks (from 2000 on), Mac OS X, Red Hat Linux (v.4 and later), and many others.

### Note

To get information about any of the IETF's RFC you can get their description from links obtained from the IETF's RFC search page at `www.ietf.org/rfc.html`.

The original Kerberos used DES encryption, which led the United States government to place a ban on the export of the technology to other countries under the munitions export ban legislation, which was upheld until 2000. Windows Server 2000 was the first major network operating system to ship worldwide with Kerberos containing DES-56, and Microsoft has since begun to use RC4 as its Kerberos cipher. Other versions of Kerberos have been developed outside the United States that don't use DES. Among the best-known implementations are eBones and Heimdal.

Kerberos uses two communication protocols developed by Roger Needham and Michael Schroeder. The Symmetric Key Protocol uses a symmetric encryption algorithm to establish a session key between the endpoints of a connection. The Public Key Protocol used in Kerberos establishes the mutual authentication between the endpoints. The trusted third party in Kerberos is called a key distribution center (KDC) and is separated into two separate services: the Authentication Server (AS) and a Ticket Granting Server (TGS).

Tickets are distributed to enable a client to identify itself in a session. The KDC has a set of secret keys that it saves in a data store for each network node. The secret key is known only to the node and the KDC and to no one else. When a connection is being established, the KDC generates the session key that is used to validate the connection endpoints.

While a Kerberos mechanism involves at least eight different messages between client, TGS, and Server Service, these messages allow each node in the system to both identify itself and validate the message coming from another node. The success of each operation

1. Client logon
2. Client authentication
3. Client service authorization
4. Client service request

depends on both of the two messages exchanging tickets or session keys to match up. No message contains both pieces of information. Kerberos imposes overhead on the network, but the system is secure. However, Kerberos is not without its problems. For one, the TGS is a single point of failure and must be made fault tolerant.

Also, because Kerberos depends on the timestamps placed into the messages at each step, all systems must be in synchronization using a service such as the Network Time Protocol or the Windows Time Service (WTS). Kerberos can tolerate a certain amount of time asynchronicity, usually about ten minutes. Great time disparity leads the tickets to become invalid. These factors can be adjusted as part of domain policies and in the Kerberos settings.

The last concern is that because the Authentication Server stores all of the secret keys, if someone gains access to that server, all of the network's security can be compromised. At an individual level, a compromised client system can be made to disclose a user's password. Still, Kerberos is currently the state of the art as a network authentication and identification service and is illustrative of many of the principles that you have seen described in this chapter.

# Summary

In this chapter, you learned about different aspects of network security. You saw how there are many different places where a network can be attacked, and many different methods that can be used by an attacker. The key to securing a network is to use a multilayer, overlapping, and multi-pronged defense. In this chapter, you saw some commonsense rules that you can apply to make your network safer.

Three Internet security protocols were described in this chapter: IPsec, TLS/SSL, and HTTPS. Encryption technologies offer protection against data compromise. This chapter considered different key-based encryption technologies and showed how they work. The Kerberos system was also described in this chapter.

[Chapter 28](ch28.html) covers the topic of firewalls and network gateways in detail. A firewall is a primary tool for protecting a network, so the information in the next chapter extends what you have learned in this chapter.
