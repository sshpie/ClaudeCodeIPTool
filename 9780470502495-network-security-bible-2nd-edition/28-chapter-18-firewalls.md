# Chapter 18. Firewalls

**IN THIS CHAPTER**

- **Understanding the importance and use of a firewall**
- **Determining the different types of firewalls**
- **Identifying how to configure a firewall**

Prevention is a key to stopping an attacker. We want to prevent as many attacks as possible, and when we can't prevent an attack we want to detect it as soon as possible. On most networks firewalls are the main method of preventing attacks. Therefore it's important to understand how to design and configure a firewall to provide the highest degree of security possible.

This chapter will explore the different types of firewalls and critical rules that need to be applied when using a firewall. A firewall will be effective only if it is designed and configured correctly.

# Firewalls

There are many reasons for an organization to employ firewalls to secure its networks from other, insecure networks.

- **Poor authentication**—Most network services and applications do not directly use authentication and encryption features, as they could be too cumbersome or costly. When such applications are accessed from the outside, the applications themselves may not be able to distinguish between legitimate and fake users.
- **Weak software**—Most purchased software and free software, known as freeware (many of the commonly used remote login, file transfer, and e-mail programs), are not optimized for security features. Using them could create vulnerabilities in the respective networks. A firewall can be highly effective in scanning and logging Internet traffic using these applications.
- **Spoofing**—Address spoofing has been a security problem for a long time. Because routing commonly uses both source and destination addresses, it is relatively easy for an attacker to read packets of communication sessions and acknowledge the respective addresses. Once this is done, the hacker by sophisticated mechanisms can spoof the source address to the destination and vice versa. This can place resources directly under the control of the attacker who can wreak havoc in no time.
- **Scanners and crackers**—Scanners are usually network tools employed by an attacker to monitor and read network data and communication ports. When the attacker finds vulnerable ports or sensitive data, he or she uses these weak spots to initiate attacks on the network. Crackers are software programs that an attacker uses to launch dictionary attacks on passwords and other sensitive authentication information present on internal networks.

[Figure 18-1](ch18.html#a_firewall_placed_between_the_internet_a) shows an example of a firewall placed between the Internet and an internal LAN to guard against attacks from the Internet.

![A firewall placed between the Internet and an internal LAN](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1801.png)

**Figure 18.1. A firewall placed between the Internet and an internal LAN**

## Packet-filtering firewalls

Packet filtering is a primary and simple means of achieving network firewalls. Filters are specialized components present in the firewall, which examines data passing in and out of the firewall. The incoming and outgoing firewall packets are compared against a standard set of rules for allowing them to pass through or be dropped. In most cases, the rule base (commonly known as the ruleset) is predefined based on a variety of metrics. Rules can include source and destination IP addresses, source and destination port numbers, and protocols used. Packet filtering generally occurs at Layer 3 and Layer 4 of the OSI model and employs some of the following metrics to allow or deny packets through the firewall:

- **The source IP address of the incoming packets**—Normally, IP packets indicate where a particular packet originated. Approval and denial of a packet could be based on the originating IP addresses. Many unauthorized sites can be blocked based on their IP addresses; in this way, irrelevant and unwanted packets can be curtailed from reaching legitimate hosts inside the network. For example, a significant amount of spam and unwanted advertisements are aimed at third-party businesses, causing wastage of bandwidth and computational resources. Packet filtering using source IP-based rulesets can be highly effective in eliminating many such unwanted messages.
- **The destination IP addresses**—Destination IP addresses are the intended location of the packet at the receiving end of a transmission. Unicast packets have a single destination IP address and are normally intended for a single machine. Multicast or broadcast packets have a range of destination IP addresses and normally are destined for multiple machines on the network. Rulesets can be devised to block traffic to a particular IP address on the network to lessen the load on the target machine. Such measures can also be used to block unauthorized access to highly confidential machines on internal networks. By blocking any packets going to a broadcast address, an organization can stop systems from being relay points for attacks.
- **The type of Internet protocols that the packet may contain**—Layer 2 and Layer 3 packets carry the type of protocol being used as part of their header structure, intended for appropriate handling at the destination machines. These packets could be any of the following types:Normal data carrying IP packetsMessage control packets such as ICMPAddress resolution packets such as ARPRARPBoot-up protocols such as BOOTPDHCPFiltering can be based on the protocol information that the packets carry. Though packet filtering is mainly accomplished at the OSI model's Layer 3 and below, Layer 4 attributes, such as TCP requests, acknowledgment messages, sequence numbers, and destination ports, can be incorporated in devising the filters.
- **Packet-filtering firewalls integrated into routers**—Such routers route packets and drop packets based on firewall-filtering principles. Information about the incoming port and outgoing port in the router of the packet can be utilized to define filtering rules.

The main advantage of packet-filtering firewalls is the speed at which the firewall operations are achieved. Because most of the work takes place at Layer 3 or below in the network stack, complex application-level knowledge of the processed packets is not required. Most often, packet-filtering firewalls are employed at the very periphery of an organization's secure internal networks because they can be a very handy tool in offering a first line of defense. For example, using packet-filtering firewalls is highly effective in protecting against denial-of-service attacks that aim to bog down sensitive systems on internal networks. The normal practice is to employ additional safety measures inside the DMZ with the packet filtering firewall set up at the external periphery.

Though cost effectiveness, speed, and ease of use are appreciable qualities of packet-filtering techniques, these have some significant flaws, too. Because packet-filtering techniques work at OSI Layer 3 or lower, it is impossible for them to examine application-level data directly. Thus, application-specific attacks can easily creep into internal networks. When an attacker spoofs network addresses such as IP addresses, packet filters are ineffective at filtering this Layer 3 information. Network address spoofing is a primary tool employed by willful attackers on sensitive networks. Many packet-filtering firewalls cannot detect spoofed IP or ARP addresses. In essence, the main reason for deployment of packet-filtering firewalls is to defend against the most general denial-of-service attacks and not against targeted attacks. Security inspections (such as cryptography and authentication) cannot be carried out with packet-filtering firewalls because they work at higher layers of the network stack.

## Stateful packet filtering

Stateful packet-filtering techniques use a sophisticated approach, while still retaining the basic tenets of packet-filtering firewalls for their operation. In networking communication, Layer 4 works with the concept of *connections*. A connection is defined as a legitimate single-source that's transmitting and receiving to and from a single destination. The connection pairs can usually be singled out with four parameters:

- The source address
- The source port
- The destination address
- The destination port

Normally, the Transmission Control Protocol (TCP) at Layer 4 of the OSI network stack uses such connection mechanisms for communication and thus differs from the connectionless Internet Protocol present at Layer 3.

Stateful inspection techniques employ a dynamic memory that stores the state tables of the incoming and established connections. Any time an external entity requests a connection to a networked host, the connection parameters are characterized by the state tables. Similar to the packet-filtering techniques, certain rules are laid down that must be satisfied for legitimate conversation to take place. Because stateful inspection techniques involve higher-layer network information, the design has to be carefully crafted. When too many restrictions are placed on the firewall's behalf on the transiting data, customers and legitimate remote users may find it exceedingly difficult to surpass the firewalls. This can result in loss of business or poor productivity for commercial organizations.

Stateful inspection techniques use TCP and higher-layer control data for the filtering process. The connection information is maintained in state tables that are normally controlled dynamically. Each connection is logged into the tables, and, after the connection is validated, packets are forwarded based on the ruleset defined on the particular connection. For example, firewalls may invalidate packets that contain port numbers higher than 1023 to keep them from transiting from application servers, as most servers respond on standard ports that are numbered from 0 to 1023. Similarly, client requests emanating from inappropriate ports can be denied access to the server. [Figure 18-2](ch18.html#stateful_inspection_firewall_architectur) shows the stateful packet-filtering process.

![Stateful inspection firewall architecture](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1802.png)

**Figure 18.2. Stateful inspection firewall architecture**

Even though stateful inspection firewalls do a good job of augmenting security features generally not present on filtering-based firewalls, they are not as flexible or as robust as packet filtering. Incorporation of the dynamic state table and other features into the firewall makes the architecture of such firewalls complex compared to that of the packet-filtering techniques. This directly influences the speed of operation of stateful inspection techniques. As the number of connections increases (as often is the case on large-scale internal networks), the state table contents may expand to a size that results in congestion and queuing problems at the firewalls. This appears to users as a decrease in performance speed. Most of the higher-level firewalls present in the market are stateful inspection firewalls. Other problems stateful inspection firewalls face include that they cannot completely access higher-layer protocol and application services for inspection. The more application-oriented the firewall is, the narrower its range of operation and the more complex its architecture becomes.

## Proxy firewalls

Application proxy firewalls generally aim for the top-most layer (Layer 7—the Application layer in the OSI model) for their operations. A proxy is a substitute for terminating connections in a connection-oriented service. For example, proxies can be deployed in between a remote user (who may be on a public network such as the Internet) and the dedicated server on the Internet. All that the remote user sees is the proxy, so he doesn't know the identity of the server he is actually communicating with. Similarly, the server sees only the proxy and doesn't know the true user. The proxy can be an effective shielding and filtering mechanism between public networks and protected internal or private networks. Because applications are completely shielded by the proxy and because actions take place at the application level, these firewalls are very effective for sensitive applications. Authentication schemes, such as passwords and biometrics, can be set up for accessing the proxies, fortifying security implementations.

In many cases, dedicated supplementary proxies can be set up to aid the work of the main firewalls and proxy servers. Proxy agents are application- and protocol-specific implementations that act on behalf of their intended application protocols. Protocols for which application proxy agents can be set up include the following:

- HTTP
- FTP
- RTP
- SMTP

The main disadvantage in using application proxy firewalls is speed. Because these firewall activities take place at the application level and involve a large amount of data processing, application proxies are constrained by speed and cost. Yet application proxies offer the best security of all the firewall technologies discussed here. Dedicated proxies can be used to assist the main firewalls to improve the processing speed. [Figure 18-3](ch18.html#comparison_of_firewall_technologies) shows a comparison of the firewall technologies.

![Comparison of firewall technologies](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1803.png)

**Figure 18.3. Comparison of firewall technologies**

## Disadvantages of firewalls

There are some inherent disadvantages of installing firewalls. The main disadvantage is the cost involved in installation. A thorough analysis of the protected architecture and its vulnerabilities has to be done for an effective firewall installation. Moreover, attackers can compromise the firewall itself to get around security measures. When firewalls are compromised by a clever attacker, he or she might be able to compromise the information system and cause considerable damage before being detected. Attackers could also leave back doors that may be unseen by firewalls. These back doors become potentially easy entry points for a frequently visiting attacker. When improperly configured, firewalls may block legitimate users from accessing network resources. Huge losses can result when potential users and customers are not able to access network resources or proceed with transactions.

# Firewall rules

Today's networks are continually growing and changing to meet the increased demands of organizations, by providing new services, creating extranets with suppliers, enabling remote office support, integrating company acquisitions, and carrying out a plethora of other tasks. This places numerous challenges on an organization's network infrastructure, most notably in deploying and managing security access control. Managing the additional access control devices and their associated rules can become a nightmare as more and more devices are added to meet these demands. Luckily, there are several methods you can use to keep access control rules consistent across the organization. We will examine ways you can maintain consistency in the face of change and industry best practices for managing rulesets.

## Tiered architecture

A tiered architecture provides the most secure, defense-in-depth approach to protecting a network and its assets. A complex environment often consists of multiple layers of access control including Layer 3 filtering via access control lists on the border router, stateful filtering on the firewall, and proxy capabilities on an application gateway. However, the biggest challenge to this type of architecture is keeping rules consistent among the various tiers. The set of rules should be consistent so that rules do not subsume or contradict one another.

It is critical to correctly order rules within a device and amongst tiered devices. Rules must be inserted in the correct order for consistency, performance, and to eliminate security holes. Adding or modifying rules requires careful policy analysis so that rules do not create policy conflicts resulting in different actions for the same traffic, thus leading to inconsistency and ambiguity. The following are some examples of rule conflicts:

- An upstream device blocks traffic accepted by a downstream device. This creates a rule that is never activated.
- An upstream device permits traffic denied by a downstream device. This causes additional unnecessary processing on the upstream device.
- A downstream device denies traffic already blocked by an upstream device. Redundant rules increase the policy size and waste performance.
- An upstream device blocks part of the traffic accepted by a downstream device or permits part of the traffic denied by downstream device. This creates ambiguity of action.

Each access control ruleset must be configured to deny any service and connection type unless it is expressly permitted. Rulesets should be built to be specific as possible with regard to the network traffic they control. Rulesets should be kept as simple as possible so as not to accidentally introduce holes in the access control that might allow unauthorized or unwanted traffic to traverse the device. For a tiered architecture each device is in charge of a specific piece of the overall firewall policy. For example, border routers with ACLs control ingress and egress filtering to block traffic such as private IP addresses, outgoing traffic with spoofed IP addresses, and so on. Stateful firewalls block unnecessary protocols and maintain state information and access control detail on the protocols that are permitted. Application proxies control access for certain applications on a more granular level including inspecting the payload of the traffic. Duplication of rules on multiple devices creates additional network latency; however, duplication of rules can also help tune access control devices. For example, if a rule is triggered on the application proxy it could indicate that the traffic or attack evaded the stateful firewall.

Regular testing of the rulesets must be performed at least quarterly. Devices should be tested for configuration errors, consistency of the firewall ruleset, and integrity of the devices. The rulesets can be tested using one or both of two methods. The first method is to obtain hard copies of the ruleset configurations and compare these copies against the expected configuration based on the overall firewall policy. The second method involves the use of tools to perform a vulnerability assessment. Tools such as Nessus are used for this assessment to indicate where the holes are in the overall policy. It is best to utilize both testing methods for a comprehensive analysis of your security rulesets.

Additionally, you should implement a formal approach for security rulesets by creating a configuration control board (CCB). The CCB approves modification to rulesets, insertion or removal of security devices, and other network changes that affect access control. For example, when new applications are being considered, a configuration control board could evaluate the implementation before any formal changes are made to the rulesets.

## Multiple entry points

Networks have evolved from a single point of entry to and from the Internet, to a porous conglomerate of external connectivity. Keeping rulesets consistent across multiple devices in a complex environment is a challenge. The most important step to managing multiple firewalls is that the initial build and configuration of each firewall must be fully documented. This provides a baseline description of the firewall system to which all subsequent changes can be applied. This permits tracking of all changes to ensure that a consistent and known state is maintained. In addition each firewall must provide the least amount of access that is necessary for that entry point. For example, if one entry point is for external supplier connectivity it should restrict suppliers to the resources necessary for the transaction, such as supplier-specific Web sites and databases.

Network address translation (NAT) and virtual private network (VPN) features further complicate the management of multiple firewalls. NAT uses internal private addresses that are managed by a security device that controls access to the Internet. VPN tunnels and their related security associations also create security policies in the form of rules. NAT rules and VPN rules must be compatible and consistent with firewall rules, especially when all three coexist on the same device.

Several tools are available to centrally manage heterogeneous firewall rulesets. These products offer support for various commercial and open source firewalls including rule management, firewall configuration, log correlation and aggregation, and centralized response to attacks. These products also allow the management and integration of NAT, VPN, and firewall rules all at once. Some even resolve conflicts.

Centralized policy management systems often provide version control, which is the ability to save and track changes made to a security policy. Security administrators need to know *what* was changed, *when* it was changed, and *who* did the changes. This means that whenever a modification to a firewall configuration is done, the actual modification is recorded along with the username of the administrator performing the modification. In addition, the current date and time and sometimes an optional version comment are stored. This allows an administrator to roll back to any given version in time, and deploy that configuration to a running firewall, knowing that it will operate in the exact same way it did when the configuration was first created.

## Automated modification of rules

Many devices such as intrusion prevention systems (IPSs) and active response devices have the capability to modify access control rulesets automatically. However, this creates a huge administrative nightmare in keeping rules consistent. If you are using this type of defense you must be actively logging each modification to the ruleset in detail for change control. Then the analyst must determine whether the modification is necessary and if it should be added to the overall security policy for all devices, or if it should be removed. It would be detrimental to allow the automated modification to be added to all security devices because in the case of a change that blocks certain traffic this could create a denial-of-service attack if it blocks legitimate traffic. A savvy attacker could cause thousands of new rules to be added to your ruleset, creating a denial of service on legitimate users and a lengthy cleanup process. This type of automated modification violates the idea of a configuration control board to institute formal changes to the ruleset. However, in some cases security devices will present the modification and let the analyst decide whether to implement it. This allows the analyst more control over changes made to the ruleset; however it requires a security operations center that is staffed full time by analysts ready to respond and make these decisions when necessary.

Another instance of automated modification of rules is in the case of mobile users. Mobile users often cause the firewall policy to change as they roam. Thus, the firewall ruleset snapshot may look different at different points in time.

The key things to remember about maintaining consistency across access control devices are the following:

- Use a default deny rule.
- Build rulesets specific for the type of traffic that each device controls.
- Keep rulesets as simple as possible.
- Regularly test your rulesets.
- Utilize a configuration control board for ruleset changes.
- Apply version control.
- Minimize the number of entry points.
- Fully document the initial build and configuration of each firewall.
- Centrally manage heterogeneous firewall rulesets.
- Minimize or tightly control automatic modification of rules.

The bottom line is to know your network, know your traffic, and maintain tight control over your security access control devices. In addition, continually review your logs and periodically test your organization's security.

## Products for Managing Multiple Heterogeneous Rulesets

Several tools are available to centrally manage multiple heterogeneous firewall rulesets. One such commercial product is Solsoft Policy Server (SPS), which provides multivendor support for centralized policy management. Solsoft Policy Server provides centralized security configuration management of all enterprise network devices including firewalls, routers, switches, and VPNs from leading security vendors. Among the products supported by Solsoft Policy Server are Juniper Networks' NetScreen ScreenOS, Check Point's FireWall-1, Nortel's Contivity VPN Switches, the Linux netfilter firewall, Symantec's Enterprise Firewall, and various Cisco products. Solsoft works with leading network security partners to ensure constant interoperability.

Firewall Builder is an example of an open source, multi-platform firewall configuration and management tool. It consists of a GUI and set of policy compliers for iptables, ipfilter, OpenBSD PF, and Cisco PIX. Being truly vendor-neutral, Firewall Builder can generate a configuration file for any supported target firewall platform from the same policy created in its GUI. This provides for both consistent policy management solutions for heterogeneous environments and possible migration paths. Policy compilers can also run sanity checks on firewall rules and make sure typical errors are caught before generated policy is deployed.

## Policy conflict examples in tiered architectures

Policy conflicts in tiered architectures, created by misconfigured rulesets, often result in redundancy, inconsistency, ambiguity, and sometimes security holes through the perimeter. The following are examples of possible rule conflicts that must be resolved. Please refer to [Figure 18-4](ch18.html#example_architecture) for the network architecture.

**Example 1:** The rule on firewall-2, shown in [Figure 18-5](ch18.html#ruleset_that_causes_unnecessary_processi), causes extra unnecessary processing of the rule on firewall-1 because the traffic firewall-1 permits will never be allowed into the network protected by firewall-2.

**Example 2:** The rule on firewall-1, shown in [Figure 18-6](ch18.html#example_of_a_rule_that_is_never_activate), is never activated because of the rule on firewall-2.

![Example Architecture](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1804.png)

**Figure 18.4. Example Architecture**

![Ruleset that causes unnecessary processing](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1805.png)

**Figure 18.5. Ruleset that causes unnecessary processing**

![Example of a rule that is never activated](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1806.png)

**Figure 18.6. Example of a rule that is never activated**

**Example 3:** The rules on both firewall-1 and firewall-2, shown in [Figure 18-7](ch18.html#example_of_redundant_firewall_rules), are redundant.

![Example of redundant firewall rules](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1807.png)

**Figure 18.7. Example of redundant firewall rules**

**Example 4:** The rule on firewall-1, shown in [Figure 18-8](ch18.html#example_of_a_ruleset_that_partially_bloc), blocks part of the traffic accepted by firewall-2.

![Example of a ruleset that partially blocks some traffic](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1808.png)

**Figure 18.8. Example of a ruleset that partially blocks some traffic**

# The Use of Personal Firewalls

We all know that the Internet is used by many different people trying to accomplish many different tasks. While the vast majority of Internet users are not malicious and are simply trying to access information, a few people use this vastly connected network of computers for malicious purposes. These malicious users attempt everything from chaining the data that has left your computer and is in flight to the next server or router, to trying to use your computer's connection to the Internet as a means for breaking into your computer. There are many different ways to protect your computer(s) from malicious users while being connected to the Internet, but none is as strong, and potentially easy, as setting up a personal firewall on your computer.

This section is an attempt to provide a broad view of firewalls and how personal firewalls can be used to help everyone from the corporate information technology administrator to the home user with just a few computers connected to a cable or DSL modem. To make the points more concrete, iptables, the default Linux personal firewall, is used in the examples and acts as a small tutorial for the program.

## Corporate vs. home firewalls

If you are a corporate information technology administrator, or the administrator of any large network of computers and servers, a lot of your time may be spent configuring and auditing your border firewalls. While it is of the utmost importance that such large border firewalls be installed on any large (or small) network, it is also important that individual hosts are properly protected.

Personal firewalls, or software-based firewalls are installed on each computer in the network. These personal firewalls work in much the same way as the larger dedicated border firewalls found in larger network settings. The point and purpose of these firewalls are different in detail, but ultimately they're much the same—they filter certain packets to prevent them from leaving or reaching your system.

The need for personal firewalls is often questioned, especially in the corporate setting where large dedicated firewalls are maintained to keep a strict division between the Internet and the internal network. This is often the environment where a personal firewall can be helpful, but the advantages are often overlooked. While it is true that dedicated firewalls installed on the network will keep potentially harmful traffic from reaching an internal computer from the Internet, these firewalls do little if anything to prevent attacks that originate from the internal network. These attacks are all too common and are usually much different from the ones seen coming into a network from the Internet.

Attacks that originate from inside a network are usually those carried out by viruses. Take the well-known Code Red virus. This virus worked by sending out traffic and attempted to exploit a hole in a common Web server. While the attack of Code Red probably could not have been completely prevented by firewalls alone, its impact on networks around the world could have been dramatically reduced if simple personal firewall rules had been used to prevent such traffic from flowing around inside a corporate network.

## Iptables

As with most operating systems, most versions of Linux come with a personal firewall installed and sometimes configured for your system. Iptables works like most personal firewalls by installing hooks (callback functions) into the network stack of the operating system. What this means is that every time a packet arrives at your machine a function is called that is able to parse the packet and determine what, if anything, should be done with it. The basic options for most firewalls are to either drop packets that fit a certain user-defined description, or to allow the packets to enter the system and be processed by any potentially waiting application, like a Web server. While having the ability to drop a packet is enough to protect your system from unwanted packets, iptables also allows the ability to log such packets. Iptables also has the ability to match packets, a group of packets, or certain parameters such as limiting the amount of traffic that enters or leaves your system. This can be very beneficial in preventing or slowing the spread of computer viruses.

### Blocking incoming traffic

The first packets that you want to prevent from entering your system are those attempting to make a connection to some port on your computer. In most cases the average workstation or home computer will never have a service running that should be accepting packets, unless that connection has first been initialized by your computer. For example, when a Web browser attempts to visit a site, the browser initiates a connection with the Web server. Packets are then sent back and forth between your computer and the Web server. However, it is important to note that it was your Web browser that sent the first packets initializing the request. With most workstations there will never be an instance where someone else's computer will initiate a connection to your workstation. To drop all packets that attempt to make a connection to your computer, the following command can be issued using iptables:

```
iptables  -A INPUT -p tcp -m tcp ! --tcp-flags SYN,RST,ACK SYN -j ACCEPT
```

This command tells iptables that you would like to add a rule to the `INPUT` chain. The `INPUT` chain handles all the packets that come into your system. The `-p` flag is for the protocol and the `-m` flag is for matching. The flags that follow `--tcp-flags` require a bit more commentary because they are the essence of this rule. When a computer attempts to make a connection to another computer using the TCP protocol, a SYN packet is first sent to the host. This SYN packet tells the server that an attempt is being made to set up a connection with it. By simply blocking these packets, you can prevent all users from making connections to your computer through TCP, achieving our goal. This command, however, accepts packets that are not SYN packets. At first this seems a bit counterintuitive until it is stated that security should almost always be set up by denying everything, and then allowing only what is needed. The same is true for personal firewalls. All packets into your computer should be by default dropped, unless explicitly allowed to enter. This rule allows for explicitly letting non-SYN packets into your computer, but first the default action of dropping must be turned on. To drop all packets coming into your computer by default the following command is issued.

```
iptables -P INPUT DROP
```

Now your computer drops all packets by default, unless they are non-SYN packets. Using a default rule of drop and allowing only non-SYN packets into your system is actually quite a strong default setup. In fact in most cases the only other setup that is needed will be to allow incoming SYN packets to specific ports where programs are running and listening for traffic. These programs can be anything from SSH to some piece of custom administrative software. To allow access to your computer via SSH, for example, the following command can be issued.

```
iptables -A INPUT -p TCP –destination-port 22 -j ACCEPT
```

This will allow connections from any computer to yours through SSH. The same can be done for any other program that someone might need to connect to on your computer, by simply substituting the proper port number. It is normally a good idea not to add any of these rules until problems arise. This prevents opening up a port on a computer where something is listening on that port but not properly configured, like a Web server.

Once you have your computer configured to drop all packets by default and to allow only those packets that are not trying to make connections to your computer, you will notice that your computer can no longer make connections to hosts connected to the Internet. This is because DNS is being blocked so your computer is unable to translate addresses. To enable DNS you have to let UDP packets through, with a source port of 53. This can be done by issuing the following command:

```
iptables -I INPUT 1 -p udp –destination-port 53 -j ACCEPT
```

By using the `-I` flag with the number 1, this rule goes to the top of the list. Because every time your computer connects to another machine it must resolve the name, it is a good idea to put this rule at the top of the list. However, much care and time have been put into the design of iptables so that looking up rules is very, very fast.

If you have issued the preceding commands without any other commands, your iptable configuration should look something like this:

```
Chain INPUT (policy DROP)
target     prot opt source     destination
ACCEPT     udp  --  0.0.0.0/0  0.0.0.0/0      udp spt:53
ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0      tcp flags:!0x16/0x02
ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0      tcp dpt:22
```

This can be obtained by using the following command:

```
iptables -L -n
```

As far as packets entering your system, this makes for quite a strong system. However, packets can still freely leave your computer without being checked. While this is normally not as dangerous as packets entering your system, some consideration should be made for packets leaving your computer.

### Blocking outgoing traffic

To drop packets that leave your computer, rules are established using the `OUTPUT` chain instead of the `INPUT` chain. Establishing rules for packets leaving your computer can help to prevent the effects that a virus can have on a network. Let's go back to the example of the Code Red virus. If there is a rule in your personal firewall to allow only outgoing http connections to the Internet or your network's proxy, then the spread of Code Red would be very marginal inside your network. Most of the damage that was caused by Code Red was simply that of slowing down the network by having the virus on a few computers attempt to infect a number of other servers. This can be prevented right at the workstation by using a strictly configured personal firewall. The following simple rule prevents HTTP connections to any machine on the internal network:

```
iptables -I OUTPUT -p tcp -d 192.168.0.0/24 --destination-port 80 -j DROP
```

Because the default rule for packets leaving the system is to allow them to go through, the logic you use for your rules must be in reverse. This is why we are explicitly setting the type of packet leaving the system we want to drop. This appears to break the rule of security established before that only needed access should be granted. However, it is okay to work in reverse in this case because enumerating all the rules that would be needed for outgoing packets would be a large task. Also, outgoing packets usually do not have a negative effect on your computer, but rather on the network it is connected to.

In most situations, when dealing with outgoing traffic, only the proxy or Internet will ever need to be contacted. Very little peer-to-peer traffic is ever needed. Yet if explicit rules are not set for packets leaving a system, the system's traffic, for example, from viruses attempting to affect other computers, will still be allowed to clog the network. While these packets will not make it to their destination because of input rules on the personal firewall, the traffic will still be routed and cause congestion. Blocking packets from leaving one's system is all too often overlooked, and yet allowing the system to send packets to any host on the network can have an impact on the network as a whole.

### Logging blocked traffic

While we have seen a few ways to block packets from entering and exiting the system, almost all information about these packets is lost when they are dropped. Logging of information can play a major roll in tracking down network problems and alerting administrators as to when a virus or other such malicious program has infected the system. Proper logging and auditing can be almost as important as configuring the right rules to deny packets. There is a bit of logging that iptables does automatically for you. Iptables keeps a record of how many times a rule has affected a packet. This information is easy to retrieve by simply issuing the following command.

```
iptables -L -v
```

This tells iptables to list all of the rules and to be verbose when doing so. This will give an output that looks similar to the following.

```
Chain INPUT (policy DROP 129 packets, 20831 bytes)
 pkts bytes target  prot opt in  out source   destination
   25  2644 ACCEPT  udp  --  any any anywhere anywhere udp spt:domain
 523K  675M ACCEPT  tcp  --  any any anywhere anywhere tcp !SYN
    1    60 ACCEPT  tcp  --  any any anywhere anywhere tcp dpt:ssh

Chain OUTPUT (policy ACCEPT 372K packets, 25M bytes)
pkts bytes target  prot opt in  out source   destination
  5  300 DROP   tcp  --  any any anywhere 192.168.1.0/24 tcp dpt:http
```

The number of packets affected by a given rule is shown in the first column next to the rule. The number of bytes is also shown. There is also a total count for that chain give in the parenthesis. These numbers can help to provide a quick approximation of what is happening on your system, and what the rules are protecting you from.

To reset these numbers out so that you can see what is happening at the current moment the following commands are used:

```
iptables -Z INPUT
iptables -Z OUPUT
```

Once a chain has been reset the information can then be listed again to see which rule is currently being used to stop packets, or which one is not doing what you need it to. During an attack, this can be a very helpful and fast way to see if your rule is protecting your computer as you think it should. It might be necessary to add new rules and then check their count to see if they are having the desired effect.

However, in most cases this type of logging simply is not enough. More information like the IP address and port can be helpful in tracking down the malicious user or problem. To log information about a rule you can add another rule to the system that is exactly the same except that it logs the packet instead of accepting or denying the packet. While at first it seems as though this method is tedious for logging packets (because you have to make separate rules that are essentially the same), it has the benefit of allowing you to create any rule that is then only logged. To log a packet that arrives at your system bound for SSH connections, the following command would be issued:

```
iptables -I INPUT -p tcp -destination-port 22 -j LOG
```

Now, any time an SSH connection is established, it will be logged by syslogd or a similar daemon. These messages can usually be found in `/var/log/messages`. However, there are often a lot of messages in `/var/log/messages`. So to help track down the information logged by a particular rule you can add your own prefix to the rule. To add the prefix "SSH " to our rule the following command can be issued:

```
iptables -I INPUT -p tcp -destination-port 22 -j LOG --log-prefix "SSH "
```

Now whenever a message is written to the log it will have that prefix. You will notice that a space was left after SSH to allow a space in the log. Otherwise your prefix will be right next to your rule, making it harder to parse as in the following:

```
kernel: SSHIN=eth0 OUT= MAC=ff:ff:ff:ff:ff:ff...
```

rather than this:

```
kernel: SSH IN=eth0 OUT= MAC=ff:ff:ff:ff:ff:ff...
```

You can also set the amount of information that is recorded by iptables when this logging happens. This is set by the following flags: `--log-tcp-options` and `--log-ip-options`. It is a good idea to turn on these flags because too much information can be a problem if you do not have enough space to store the logs. However, not enough information can leave you guessing as to why this rule was triggered by iptables.

The logging of information is often overlooked when setting up a personal firewall. While the information that is logged by iptables is not in as nice a format as Snort or another sniffer might give you, it is usually enough to tell what's happening to your system with respect to network traffic. Logging is an invaluable security tool, but is only helpful if the logs are audited in a routine fashion. Simply waiting for something to happen that is noticeable usually results in your being too late. Scanning logs with a Perl script, or even just eyeballing the log once a week, is usually enough to detect patterns of harmful behavior.

### Advanced blocking techniques

Iptables also allows you to block traffic based on burst rates and other matching criteria. This can be extremely helpful for both incoming and outgoing traffic. For example, you might want to allow traffic to be sent from peer to peer, but never for a single machine to be able to swamp the network with traffic. This can be done by matching a limit of the traffic that is sent out of the computer. These limits and the configuration for them are outlined nicely in the manual page for iptables.

Other matching features of iptables allow you to drop packets based on the size of the packet, or do matching based on connections (when compiled into the kernel). These matching criteria can get very elaborate; however, they can also be very helpful in shaping the traffic entering or leaving a computer.

Personal firewalls come pre-installed on most systems today, but are vastly underutilized. All too often dedicated border firewalls are expected to protect internal machines from attack. However, all too often the attack originates inside of the network, and border firewalls do nothing to prevent this type of network congestion. Also, while most people think of a personal firewall as a last line of defense for a computer connected to the Internet, it can often be used as the first step in protecting a network from unnecessary congestion. Limiting the hosts a computer is allowed to talk to by setting up rules for outgoing packets in a personal firewall can help to prevent the spread of viruses. Personal firewalls should not be thought of as the first or last line of defense in securing a computer, but rather just as another piece in the puzzle to help secure a host.

# Summary

For most enterprises, government institutions, and financial organizations, safeguarding private networks and communication facilities is a necessity. However, many organizations have application and financial demands that require them to place themselves on the Internet or other large-scale networks that are inherently insecure. The insecurity of such large-scale networks can lead to information mishandling, which can severely and negatively affect an organization. Thus, such organizations seek out network security firewalls and other features to safeguard their internal networks and resources. As is evident from the many news stories of Internet viruses, worms, and identity theft, the public Internet is becoming a dangerous place. One of the best ways to arm against the malicious activities on an open network is to employ firewalls at the connection point of the insecure network and the internal network.
