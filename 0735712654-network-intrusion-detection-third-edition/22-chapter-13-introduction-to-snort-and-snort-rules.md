# Chapter 13. Introduction to Snort and Snort Rules

![Introduction to Snort and Snort Rules](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

Snort is an open source free NIDS that was developed by Marty Roesch. It was initially written so that Marty could do traffic sniffing at his job and has grown to a full-featured NIDS. Along the way, Marty has attracted a vast following of admirers and coders who work collectively to enhance the code and issue new releases. In early 2002, Snort was downloaded from its home at [www.snort.org](http://www.snort.org) over 10,000 times a week to protect government, corporate, home, and educational sites.

Snort is a signature-based NIDS that uses a combination of rules and preprocessors to analyze traffic. The rules offer a simple and flexible means of creating signatures to examine a single packet. The preprocessor code allows more extensive examination and manipulation of data that cannot be done via rules alone. Preprocessors can perform a variety of tasks such as IP defragmentation, portscan detection, web traffic normalization, and TCP stream reassembly, to name a few. Preprocessors give Snort the capability to look at and manipulate streams, as opposed to the single-packet-at-a-time view rules use.

The current version of Snort in March 2002 is 1.8.3 and is a compact 1.8 megabytes of source code. It is extremely portable and currently runs on approximately 23 different platforms including Linux, Solaris, BSD, IRIX, HP-UX, Mac OS X, and Win32. Snort is also easily configurable and flexible, allowing users to create their own signatures and alter the base functionality through the use of plug-ins. Plug-ins are code that can optionally be compiled into Snort at installation time and offer features such as active response to malicious traffic.

The focus of this section of the book is writing filters and signatures, so many aspects of Snort will not be discussed, such as installation, configuration, and output. If you would like more information on these topics about Snort, please visit [www.snort.org](http://www.snort.org). This chapter will cover an introduction to Snort, the anatomy of a Snort rule, and explore fields and possible values found in the first part of a Snort rule known as the rule header. The next chapter will continue rule writing by discussing the second part of the rule known as the rule options. It will also cover writing more advanced rules.

# An Overview of Running Snort

Snort can be run in various modes from simply dumping sniffed traffic to the screen, to NIDS mode where Snort is able to compare the network traffic with a preconfigured set of signatures known as rules that are housed in one or more files. The latter is the most common mode in which to run Snort.

Snort is typically run from the command line, whether it is run on a UNIX or Windows host. There is software offered known as IDScenter, which provides a Windows GUI interface, as well as Demarc/Puresecure, which provides a Windows and UNIX GUI interface. There are many command-line options that can be used, but the most practical one (-c snort.conf) allows the user to place Snort in NIDS mode by informing it of the configuration file to be used. As the name implies, this is where Snort configuration occurs, including assigning variables used in the rules values, informing Snort which preprocessor options to use, and telling Snort which rules to include in traffic analysis. A skeleton configuration file named snort.conf is provided in the Snort download directory. The user must customize this file for his site.

When Snort is run in NIDS mode, by default, it places the output of events of interest triggered by the rules in various files. Snort allows an *action* to be assigned to each rule, indicating what to do when the rule is triggered. An action of *alert* means to write the offending packet to a file named alert, which is created in /var/log/snort on many UNIX hosts, by default. On Windows hosts, the alert file is created in the *log* subdirectory in the current directory from which Snort is run. Here is an example of a Snort alert file entry:

```
[**] NMAP TCP ping [**] 
03/21-13:33.51:880120 1.2.3.4:1029 -> 192.168.5.5:80 

TCP TTL:46 TOS:0x0 ID:19678 
******A* Seq: 0xE4F00003 Ack: 0x0  Win: 0xC00 
```

There is an identifying message associated with the alert that the user can assign when the rule is created. This is optional; however, it informs the analyst of the perceived problem. The message for the preceding alert is “NMAP TCP ping”. On the next line, there is a date and timestamp followed by source IP address (1.2.3.4) and port (1029), direction of the traffic (source to the left of the arrow and destination to the right of the arrow), and the destination IP address (192.168.5.5) and port (80) of the offending packet. The third line indicates that the traffic is TCP, it has an arriving time-to-live value of 46, a type of service value of 0, and an IP identification number of 19678. The final line lists the TCP flags set; the A signifies that the acknowledgement flag is set. It is followed by a hexadecimal representation of the TCP sequence number, the acknowledgement number, and the TCP window size. All of these fields can provide more details about the packet that triggered the alert.

This alert appeared because there is a rule that examines TCP segments with an acknowledgement flag set but an accompanying acknowledgement value of 0. Most of the time when this is observed, it is a telltale sign of nmap attempting to discover a live host. If the acknowledgement is allowed to reach the destination host, the host should respond to the unsolicited acknowledgement with a reset, regardless of whether the port is listening or not. That is why the message accompanying the alert is “NMAP TCP ping.”

The alert action causes the activity to be logged as well. There is a separate action, log, which only logs the triggered activity. When activity is logged, it is recorded in a human readable format that can provide more verbose information about the packet, such as the payload. The logged packets are written to files and directories based on the IP addresses in the packet being logged. These are further segregated by the transport layer protocol and source and destination ports involved in the connection. Look at the contents of FTP activity that was logged:

```
 [**] Attempted anonymous ftp access [**] 
04/24-12:11:08.724441 192.168.143.15:3484 -> 192.168.143.16:21 
TCP TTL:64 TOS:0x10 ID:30124  DF 
*****PA* Seq: 0x93EE0AB7   Ack: 0xB8352E61   Win: 0x7D78 
TCP Options => NOP NOP TS: 112024246 27551686 
55 53 45 52 20 61 6E 6F 6E 79 6D 6F 75 73 0D 0A  USER anonymous.. 
```

The logged output contains the same information that the alert does, but it also has the payload if the decode (-d) command-line option was supplied. This message indicates that we have a rule to inspect ftp command-line traffic to destination port 21 for a user of anonymous. We will examine how this is accomplished in [Chapter 14](ch14.html), “Snort Rules—Part II,” but the payload from the previous output indicates that there was an anonymous user attempt. The hexadecimal representations of the ASCII values in the payload are also included in the logged packet.

The log and alert files can be a cumbersome way of analyzing output from Snort, so it allows you other options via configuration file changes. Activating available output options can enable writing output or alerts to spool files via a backend known as Barnyard, or directly to a database, to name a few of the possible options.

# Snort Rules

Snort supports both header and payload inspection methods, allowing you to fully specify in a single rule what is considered a suspect packet. This flexibility allows you to build rules customized to your site that greatly aid in minimizing false positives, but in a format that is very readable. Remember all the heartache and toil involved in writing TCPdump filters, especially one to inspect a packet for a particular TCP flag setting? Well, writing an identical rule in Snort is almost trivial, as you will soon see.

As a short but important digression, what qualities does one look for in a good NIDS? There are many, but one of the most important is the capability to inspect and alter signatures. Believe it or not, there are NIDS available that do not allow the user to see the active signatures or alter them in any way. This blindsides the analyst and does not allow her to distinguish between false positives and real alerts. When an alert appears, it is presented as an irrefutable statement that a problem has appeared, and there is no way to validate it using the NIDS alone. If the analyst can examine the signatures and the packet that caused the alert, there is a better chance that a more accurate assessment can be made.

Additionally, signatures that allow an analyst to look at any field, either header or payload, from different perspectives potentially improve the quality of the NIDS. In other words, if a NIDS only allows the analyst to create rules that inspect packets for a given IP or port or protocol, it lacks the range to examine payloads or header fields on a more granular level such as TCP flag settings. Perhaps the analyst is interested in inspecting the payload for specific contents when the acknowledgement flag is set. Because other flags may be set along with the acknowledgement flag, it would be handy for the signature to allow for this specification as well.

The capability to inspect just about any field in a packet is an area in which Snort excels. There are many options available to configure a rule to specify just about any field in the packet and examine the value of that field in a variety of ways. And, the few fields that cannot be inspected via current Snort rule options can always be examined by supplying a filter at the end of the command line or by resorting to a command-line switch (-F) that allows Berkeley Packet Filters (BPF) to be specified in a file. Berkeley Packet Filters are what we have been calling TCPdump filters, which can be used to select the desired field. For instance, Snort doesn’t have an option to examine the IP version field found in the high-order nibble of the zero byte offset of the IP header. Snort might be run to examine packets off the wire or from a binary file of captured TCPdump data using a BPF filter to find any packets with an IP version that does not equal 4. Here is the command that would perform this inspection reading packets from the network:

```
snort –v 'ip[0] & 0xf0 != 0x40' 
```

As explained in more detail in [Chapter 12](ch12.html), “Writing TCPdump Filters,” this will mask out the low-order nibble of the zero byte offset of the IP header and look for a value of 4 in the high-order nibble of that field and write the output to the screen (-v).

Another benefit of using Snort is that it comes with a very large set of rules. It is not recommended that all of the rules be used on installation because the more active rules used, the slower the traffic inspection becomes. The analyst must decide which rules are appropriate for the site. And, amazingly, new Snort rules are released sometimes as soon as hours after a new exploit is discovered. This is by virtue of having so many savvy users and developers of Snort who respond almost instantly to develop and test new rules for these exploits.

However, a word of caution must be added about some Snort rules. Just because a rule becomes available shortly after an exploit is released, doesn’t mean that it is a good rule—that is to say, just because a rule matches a given compiled version of an exploit’s output doesn’t mean that it is necessarily a rule that may find variations of the exploit from making minor changes in the source code. It is imperative that the rule writer understands not only the exploit code and output, but also the protocol against which it runs.

A good rule anchors on fields and values that must remain static for the exploit to succeed. For instance, if there is some kind of DNS exploit that generates a DNS identification number of 0xBEEF, this is not a good field or value to use in the rule. It is trivial to change this in the source code, and the exploit will most likely succeed regardless of the value of the DNS identification number.

**Hidden Signatures**

As a contractor for a client, I once had the opportunity to visit a commercial NIDS vendor about integrating output from its NIDS to some kind of correlation tool. Frankly, I believed the output from the NIDS wasn’t worth trying to correlate since there was no way to validate if the generated alerts were real because there was no access to either the signatures or the packets that caused the alert. Why synthesize garbage? But, the client had requested my presence at the meeting, so I dutifully attended.

While there, I asked if there was any way that we could get access to the signatures. The vendor rep balked and asked why I would ever need to see the signatures. “Well, I want to know if we have a real detect or false positive,” I politely responded. The rep replied that if I believed we had seen a rare false positive, I could call the support line and ask for help. With the number of false positives generated by the vendor’s NIDS, I could only imagine that it had stock in the Baby Bells to answer so foolishly. Indignantly, I pressed on and asked the rep what the problem was with releasing his signatures. The response was that if I could see the signatures, so could the hackers! Honest to goodness, that was the best dog-ate-my-homework excuse he could come up with. More than anything, I suspect it was that he feared that the competition might pirate his product’s signatures, but he didn’t have the spine to say that. How are you supposed to take these guys and their proprietary signatures seriously? Okay, so we’re not all blessed with the power to either make or influence the decision of which NIDS to buy. What if you happen to work at a site where you have a NIDS that has either a limited or no view of the signatures and traffic—do you throw in the towel? Well, if lobbying for a better NIDS fails, you can become resourceful! You can always run TCPdump in the background mode either alone or as part of Shadow. Or, you can try to do correlation with other sources of information such as firewalls, routers, or host logs. This is not ideal, but it prevents you from being totally blind.

We were running Shadow along with the deficient NIDS mentioned previously. An analyst called me to report that the NIDS was alerting on a Loki attack and asked if I could examine the TCPdump output to discover whether this was a real alert or not. I knew that Loki had a telltale signature years ago of a value of 0xf001 or 0x01f0 in the ICMP sequence number. The analyst was able to give me the source and destination IP numbers for the suspected Loki traffic. I searched the TCPdump records and discovered ICMP packets that matched the signature; however, this was just a case of coincidental use of those values in the ICMP sequence number in an innocuous ICMP echo request/response pair. This was an awkward and time-consuming way of dealing with this false positive, but it was better than putting full trust in the NIDS.

## Snort Rule Anatomy

An individual rule is broken into two general parts. The first part, the rule header, defines who must be involved in order for the traffic to be considered by the rule options. The second part, the rule options, defines what must be involved. This includes packet header information (such as TCP flag settings) or the contents of the payload.

Generally speaking, both sections are used for most rules. It is possible to specify rules with only a rule header so that the given action can be taken for the provided hosts and ports. This is typically the case where pass rules are used to ignore traffic between specific hosts and ports, such as port 53 traffic coming from a site’s DNS servers.

All conditions specified in both the rule header and the rule options must be true in order for an alert or some other kind of action to be triggered. It is also important to understand the Snort rules are stateless. In other words, each rule inspects one and only one packet. The rules themselves have no way of knowing what activity occurred in a packet preceding or following the current one. Snort attempts to build in functionality for state using a preprocessor such as IP defragmentation or TCP stream reassembly, but there are limits to what can be discovered when not examining traffic statefully.

Also, Snort triggers on the first rule that a packet matches and does not examine the remaining rules. The order that rules are listed in the rules files is important, but Snort does some ordering of its own. By default, Snort orders all rules by their action value in the following order: alert, pass, and log. This can be overridden by a command-line option that will be discussed later in the section, “[The Action Field](ch13.html#ch13lev4sec1).” However, Snort does some further ordering by grouping identical headers that is beyond the scope of this chapter. For more information, see [www.snort.org/docs/faq.html#3.13](http://www.snort.org/docs/faq.html#3.13).

Look at [Figure 13.1](ch13.html#ch13fig01) to see a sample Snort rule.

![The anatomy of a Snort rule.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/13fig01.gif)

**Figure 13.1. The anatomy of a Snort rule.**

You see a rule header that gives the details of the action to be taken if the rule triggers and the information pertaining to the who values in the packet. In this rule, we alert when TCP traffic is observed that originates from a network that is not 10.1.1.x from any source port destined for network 10.1.1.x to any destination port. We assume that our internal network is the 10.1.1.x network, so this rule triggers when an outsider attempts to make an internal TCP connection.

If you turn your attention to the rule options, we further specify the what of the packet attributes. In this instance, the anomalous TCP flag pair of SYN and FIN is sought, and if found, a message of “SYN-FIN scan” is associated with the alert. The rules keywords will be described more thoroughly in the following sections.

Rumor has it that the rules syntax will change radically when Snort version 2.0 makes its debut. So, if you are reading this chapter after the release of Snort 2.0, it is best to refer to Snort documentation because the information presented here might be obsolete.

### Rule Header Fields

As briefly mentioned, the rule header is responsible for specifying the action used to respond to a triggered rule, as well as specifying the protocol and source and destination addresses and ports. These who conditions must be met if the rule options are to be examined. Rule options will be explored in [Chapter 14](ch14.html).

#### The Action Field

The first field in the rule header is the action field. This field instructs Snort on what to do if the rule is triggered. The valid values for the action field are the following:

- ****Alert.****This value instructs Snort to create an entry in the alert file and to log the packet as well. The alert file is a single file that contains all detects that were made. The information written to this file in the default alert mode consists only of the packet header information. For the log entry, the same information (optionally including the payload if the -d command-line option is specified) that is written to the alert file is written to individual files found in a directory that usually has the name of the hostile IP number.
- ****Log.****This value instructs Snort to only make a log entry. No record of the traffic is made in the alert file when the log action is used. The log files might have data from the application payload if the command-line option to decode the application (-d) is used.
- ****Pass.****When a rule is triggered that has pass specified as the action, Snort does no further packet inspection—essentially dropping the packet from the detection engine. This is useful, for example, if you want to monitor anonymous ftp attempts on your network to non-anonymous ftp servers. You would write a pass rule to ignore anonymous ftp attempts to your valid anonymous ftp server. You would then use a second, normal, alert rule to log all other anonymous ftp attempts.
- ****Activate.****These rules, when triggered, not only alert, but are also used to turn on other rules (dynamic) that remain idle until turned on.
- ****Dynamic.****These remain idle (do not trigger) until turned on by an activate rule. After they are turned on, their behavior is the same as log rules.

Note that the activate and dynamic actions are being replaced by the tag option, which is found in the rule options. The tag option allows dynamic capture of packets for a given amount of time or a specified number of packets after the rule triggers.

It’s also possible to define your own action types, which can be used to route rule output to various destinations. This sophisticated usage is not covered here, but can be explored at Snort’s web site ([www.snort.org](http://www.snort.org)). As briefly mentioned, the default order in which rules are processed is alert rules first, pass rules second, and log rules last. To change this default behavior, you must specify the -o command-line option when running Snort, which changes the order the rules are processed. Using the -o option changes the rule processing order to pass rules first, alert rules second, and log rules last. This was done when Snort was developed for public use to avoid having an errant pass rule accidentally disable every alert and log rule in the system. The –o option was developed as an expert mode for people after they understood how the rules system worked.

#### The Protocol Field

The protocol field in the rule header tells Snort which protocol to examine. Snort currently supports four different types of network traffic: TCP (Transmission Control Protocol), UDP (User Datagram Protocol), ICMP (Internet Control Message Protocol), and IP (Internet Protocol). Additional protocols may be added in the future such as ARP, RARP, GRE, OSPF, RIP, and IPX. Snort understands only IP version 4, though it will note that it has seen an IP version 6 packet. And, Snort is not IPSec aware, so it cannot decode unencrypted fields of those packets.

#### The Source and Destination IP Address Fields

The source and destination IP address fields identify where the hostile traffic is coming from and where it is going. It is possible to specify the IP addresses as a host, a subnet, or multiple hosts or subnets. The IP addresses are specified in classless inter-domain routing (CIDR) notation, an easy to write and understand format. This format includes as much of the address as needed, along with the number of bits in the network mask. Let’s examine the format and some examples of IP addresses.

Format:

```
Address/netmask or any or 
[address/netmask,address/netmask…] 

Address = x.x.x.x 
Netmask = bits of network mask 
24.0.0.0/8 =           Class A 
135.1.0.0/16 =         Class B 
192.168.5.0/24 =       Class C 
192.168.5.5/32 =       Host address 
```

Special keywords:

```
any - match all addresses 
! -   negate address 
$HOME_NET – variable defined elsewhere in rules file 
```

CIDR notation details the base address and the number of bits of the base address that are associated with the network. For instance, the representation 24.0.0.0/8 means that this is a Class A address that has the first octet (24) allocated to the network and all the remaining octets associated with hosts on the network. Although the standard Class A, B, and C CIDR notations are seen in the previous examples, the beauty of CIDR notation is that the network bits don’t have to fall on byte boundaries, so they might represent all network masks.

You can specify an IP address list by enclosing all IP addresses or networks between brackets ([ ]) and delimiting each of the list values by commas (but no spaces in between—the Snort rule parser doesn’t allow spaces in the comma delimited list). If you want to examine traffic to destination host 1.2.3.4 or subnet 2.3.4.x, the following IP address list could be used:

```
[1.2.3.4,2.3.4.0/24] 
```

A special keyword *any* can be used when any IP address is the matching criteria. And, as you’ve seen, the exclamation point (!) can be used to negate the IP address value when all IP addresses but the specified one are to be considered. Finally, to add more flexibility and portability to the rules, a variable can be used to indicate the IP address. The $HOME_NET variable is one that is used in many of the rules included with Snort to indicate the user’s/analyst’s home network. You can assign your internal network any variable name you want, but because many of the rules already reference $HOME_NET, it is best to use it. This variable must be defined in a rules file, the configuration file, or on the command line (-S) before it is referenced.Variables can be used in other fields in the rules as well.

#### The Source and Destination Port Field

The port fields are used to detail the source and destination ports of the traffic. The ports can be listed as a specific number, range of numbers, or the keyword any, which represents all possible source ports. Here are some possible port representations:

|  |  |
| --- | --- |
| static port: | 111 |
| all ports: | any |
| range: | 33000:34000 |
| negation: | !80 |
| less than or equal: | :1023 |
| greater than or equal: | 1024: |

The first and most common port value is a static one, such as port 111, to represent the port associated with the Remote Procedure Call (RPC) portmapper. As with IP addresses, a generic port value can be supplied using the keyword any. A range of port numbers can be specified, such as ports 33000 through 34000 inclusive (33000:34000), which might represent UNIX traceroute UDP ports. Negation is also supported with ports as we are looking for any port but port 80 (!80) above. Ports can be indicated as a less than or equal to condition or a greater than or equal to condition. The “:1023” identifies that we want to look for all ports less than or equal to 1023 or the reserved port range. Finally, the “1024:” is used to say that all ports greater than or equal to 1024 should be considered—the ports typically found in the ephemeral source port range. You could also specify a port as a variable so long as you assigned a value to the variable before referencing it.

You might be wondering if you have to indicate a port for the ICMP protocol because it does not use ports like TCP and UDP. The rule syntax requires ports, so you must specify some kind of placeholder value. Although no port value makes sense, the value “any” is often used. Let’s look at some possible port values.

#### Direction Indicator

The traffic direction field allows you to indicate the direction the packet must be traveling. Two options are available, allowing you to indicate a specific direction of flow, or that direction doesn’t matter. Using the notation that looks like an arrow (->), the packet must be traveling from a source to a destination. The source information is specified to the left of the arrow, and the destination is to the right. The packet must be traveling in the listed direction; if it is traveling in the opposite direction, the packet will not pass the rule header test and will not be inspected any further against the rule.

If you use the notation that looks similar to a double-headed arrow (<>), the packet can be traveling to or from either address/port pair. For this notation, either side can represent the source or destination depending on the packet flow in the connection.

# Summary

Snort provides a very good NIDS at no cost for the software. Understand that although it is free to use, there are costs associated with the hardware, as well as costs associated with customizing rules and making sense of the output. Snort is most useful when run in packet-sniffing mode where it compares the network traffic against a set of rules. This can be done either in real-time mode, or traffic can be captured in binary format and retrospectively analyzed later by feeding it back into Snort as an input file.

Snort rules provide a flexible and easily configurable means of specifying most header fields to inspect, as well as analyzing any data in the payload. The rules allow the user many different ways to indicate values for particular fields in addition to permitting the use of variables to represent values. Snort rules also provide the granularity necessary to be very explicit about the attributes of the packet that are to be inspected or ignored. The result is that there should be far fewer false positives and false negatives if the rules are properly configured for the site.
