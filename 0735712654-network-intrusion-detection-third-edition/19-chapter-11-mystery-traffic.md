# Chapter 11. Mystery Traffic

![Mystery Traffic](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

Many times as a security analyst, you see some kind of interesting traffic and wish that you had the time or resources to investigate it or understand it better. You have a much better chance of being able to do this if you are in a research position rather than a busy operational environment where your exclusive purpose is to make sure that no unauthorized access occurs.

One such opportunity to do analysis of an event of interest arose at a site where Shadow was used to capture traffic. The site was the target of some extensive unexplained activity directed at TCP destination port 27374, which is often used by SubSeven.

The explanation and findings of the traffic are discussed in this chapter. When we witnessed this activity, we had a gut feeling that we were seeing something unique just because of the sheer volume of it. We used Shadow’s collected TCPdump records to analyze different fields and aspects of the packet to come to our conclusions. This was a team effort conducted with the help of co-workers Vern Stark and David Heinbuch.

My suspicion is that many people who gravitate to the position of security analyst enjoy working puzzles or mysteries. The mystery of this traffic was unraveled simply using TCPdump record capture, Perl programming to examine and summarize different aspects of the traffic, and Excel to plot the findings. Working on this puzzle was not only a great learning experience of doing traffic evaluation, and recovery after making errant assumptions, but it provided a lot of entertainment to some true bit-heads.

# The Event in a Nutshell

Examination of an hour’s traffic on June 29, 2001 at 12:00 captured by a Shadow sensor positioned outside a monitored site’s perimeter firewall revealed a large number of source hosts scanning what appeared to be the site’s Class B address space for TCP destination port 27374. Shadow retrospectively analyzes each hour’s traffic for anomalies. Anomalies, or more accurately, events of interest, are culled by running the previous hour’s collected TCPdump traffic through a series of TCPdump filters. One of the filters looks for attempted TCP SYN connections from outside the network to a host in the network.

TCP destination port 27374 is associated with a Trojan known as SubSeven that can allow full access to the victim’s machine. We have seen plenty of large scans to the SubSeven port; however, we had never seen a scan that generated such a large volume of traffic—nor had we seen one that had come from multiple concurrent sources.

**Correlation of Similar Activity**

About this same time, the System Administration, Networking, and Security (SANS) Internet Storm Center released a report on June 26, 2001 about a Microsoft Windows worm named W32.leave.worm. The speculation was that this worm was used to make the infected host a participant host, also known as a zombie, in distributed denial of service (DDoS) attacks. According to the report, the worm spread via connections to hosts listening on TCP port 27374. The report noted that the worm scanned predetermined network blocks associated with @Home and Earthlink for destination port 27374. However, it made no mention of synchronized scanning, nor did it mention scanning of networks other than those previously mentioned. Although the described worm activity appeared to be different than the activity that was witnessed at the monitored site, it was possible that the worm activity had mutated since the initial report.

# The Traffic

The following output represents a handful of TCPdump records to provide the general “flavor” of the activity. The source and destination hosts are bold. These are the first ten records associated with the activity on June 29; there are four different source hosts involved in scanning ten different destination hosts.

The timestamps associated with the records should be regarded with caution. The sensor that captured these records is running Redhat Linux 7.1 with a packet-capturing mechanism known as turbopacket compiled into the kernel. It is supposed to contain a method for more efficient buffering, but it also appears that the timestamp precision has been lost. Timestamps should have microsecond fidelity, but these timestamps appear to have 10-ms resolution:

```
12:16:31.150575 ool-18bd69bb.dyn.optonline.net.4333 > 192.168.112.44.27374: S 
542724472:542724472(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
13444) 
12:16:31.160575 ool-18bd69bb.dyn.optonline.net.4334 > 192.168.112.45.27374: S 
542768141:542768141(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
13445) 
12:16:31.170575 24.3.50.252.1757 > 192.168.19.178.27374: S 
681372183:681372183(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117,id 
54912) 
12:16:31.170575 24-240-136-48.hsacorp.net.4939 >192.168.11.19.27374: S 
3019773591:3019773591(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, 
id 39621) 
12:16:31.170575 ool-18bd69bb.dyn.optonline.net.4335 > 192.168.112.46.27374: S 
542804226:542804226(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
13446) 
12:16:31.170575 cc18270-a.essx1.md.home.com.4658 > 192.168.5.88.27374: S 
55455482:55455482(0) win 8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
8953) 
12:16:31.170575 24.3.50.252.1759 > 192.168.19.180.27374: S 
681485650:681485650(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
54914) 
12:16:31.170575 cc18270-a.essx1.md.home.com.4659 > 192.168.5.89.27374: S 
55455483:55455483(0) win 8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
9209) 
12:16:31.170575 24.3.50.252.1760 > 192.168.19.181.27374: S 
681550782:681550782(0) win 16384 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
54915) 
12:16:31.170575 cc18270-a.essx1.md.home.com.4660 > 192.168.5.90.27374: S 
55455484:55455484(0) win 8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 117, id 
9465) 
```

# DDoS or Scan

At first, it was not apparent if this was some kind of attempted DDoS or an actual coordinated scan of some sort. During the examination of the activity, we were fortunate (from the analysis perspective) to receive additional activity on July 2, 2001 at 16:00 that was remarkably similar. After we received the second scan, we began in earnest to look at individual fields found in the received packets of both sets of activity to interpret the nature and intent of the activity.

## Source Hosts

In the first scan, 132,706 total packets were received and there were 314 unique source hosts involved. Of those hosts, only 17 (approximately 5.4 percent) did not have DNS registered host names. In the second scan, 157,842 total packets were received. There were 295 unique source hosts with only 24 (approximately 8.1 percent) with unresolved host names. This alone is quite telling. Two choices for categorizing the source hosts are that they either do or do not reflect the genuine source host that is sending the traffic. If the source host reflects the actual sender, no subterfuge is used in sending the packet. If the source host is not the actual sender, a spoofed source IP number is placed in the packet.

Typically, when source IP numbers are spoofed, it is a random generation of different IP numbers in the instance of a flood. Other attacks might use a selection of one or more source IP numbers that might be either a decoy or an eventual target of some kind. When the source host reflects the true sender, the intent is more likely than not to be able to receive a response to the sent traffic.

Therefore, it appears that the activity that was seen is using genuine source IP numbers. If this were a flood and the source IPs were spoofed using randomly generated IP numbers, it is statistically unlikely that these IP numbers would resolve to host names 91.9 to 94.6 percent of the time. It would be unusual that IP numbers would be spoofed using a predetermined set of IP numbers that resolved to host names, because this takes a lot of effort for little or no gain.

It can be speculated that, because of the sheer number of source hosts involved, they most likely represent zombie hosts that have somehow been exploited and owned. Many of these source networks are associated with cable modem or DSL providers such as @Home and AOL. This corroborates the speculation of zombie hosts because home users are more likely to be unaware of security threats and less protected than most commercial or larger networks with some kind of perimeter protection.

## Destination Hosts

Next, the analysis moved to examination of the destination hosts to provide more evidence of a scan. The scanned network is Class B with the possibility of 65,535 IP numbers to scan. The first scan targeted 32,367 unique destination hosts and the second scan targeted 36,638 unique destination hosts. An initial unsubstantiated reaction to missed subnets was that there was some prior reconnaissance performed to directly target live hosts. After more thorough examination of the destination hosts, it was evident that many of the destination IP numbers that were scanned had no associated live hosts.

The more plausible explanation for the missing destination subnets and destination hosts is that perhaps the zombie or zombies that were assigned the mission of scanning those subnets were somehow not active or responsive during the scan and did not participate. A single missing destination host in an otherwise scanned subnet might be interpreted as a dropped initial packet rather than an omitted destination IP number.

Although one unique source host scanned most destination hosts, multiple source hosts scanned some destination hosts. The scanner appears to have some redundancy of scanned hosts to ensure a response.

## Scanning Rates

Another indication of a scan versus a flood was the scanning rate of the source hosts. Both scans sustained some kind of activity for five or six minutes; however, the ramp-up time was fast, and there was a burst of activity for the first two minutes.

The measure of bandwidth consumption was as follows. Each packet was a SYN packet with TCP options and no payload. Most packets had a length of 48 bytes, a few had more, and a few had 4 bytes less, depending on the number and types of TCP options used. Packets had a standard 20-byte IP header with no IP options. Because the majority of packets had a length of 48 bytes, this was used as the packet length for the computation of bandwidth consumption. Because throughput or bandwidth is measured in bits per second, the packet length was 384 (48 * 8) bits.

The scan on June 29 reached a maximum rate of 1.7Mbps at peak. The second scan on July 2 reached a maximum rate of 2.4Mbps at peak. This did not adversely affect the monitored site, but a site with a smaller ingress pipe such as a T-1 with 1.554Mbps capacity might have suffered a temporary denial of service as a side effect of the scan. [Figure 11.1](ch11.html#ch11fig01) shows the bits per second during peak scan minutes.

![Bits per second.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig01.gif)

**Figure 11.1. Bits per second.**

Looking at the plots in [Figure 11.1](ch11.html#ch11fig01) together, it is apparent from the general contours that the scanning rates for both scans were very similar. In fact, both scans reached peak scanning rates at exactly 21 seconds after the scan began. As discovered later, after examining the traffic using different representations, this peak activity indicated some kind of coordination by the “commander” who allocated scanning assignments and rates for the zombies.

Peak rates could have occurred because there were more scanning hosts during that second or because the number of packets sent by hosts increased. Further scrutiny of the data revealed that the peaks and valleys correlated with an increased number of scanning hosts.

The 21-second peak rate that was observed yet again on a third scan on November 1 was indeed a mystery. However, it was observed that the scanning hosts sent retries of initial SYN connections that received no response. This is typical TCP behavior, and many TCP/IP stacks will attempt 3 retries after the initial SYN, with a formula of waiting 3 seconds before the first retry, doubling the wait time to 6 seconds for the second retry and doubling the wait time yet again to 12 seconds for the third and final retry. Hence, the aggregate time that passes between the initial SYN and the final retry is 21 seconds. And so, when initial SYN attempts only were plotted by time as in [Figure 11.2](ch11.html#ch11fig02), the 21-second peak disappears.

![June 29, 2001 initial SYN attempts.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig02.gif)

**Figure 11.2. June 29, 2001 initial SYN attempts.**

This only partially explains the 21-second peak. If this peak were due strictly to retries alone of the same hosts, similar peak activity should be observed at 3 and 9 seconds as well. [Figure 11.3](ch11.html#ch11fig03) shows two separate types of connection attempts by time for the June 29 scan—the solid line shows initial SYN attempts and the dashed line shows retries of those initial SYN attempts. This more completely explains the 21-second peak.

![June 29, 2001 initial SYNs and retries.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig03.gif)

**Figure 11.3. June 29, 2001 initial SYNs and retries.**

Peak activity occurs at 12:16:52. As expected, this corresponds to the 3rd retry of the spate of attempted SYN connections sent at 12:16:31. Furthermore, it corresponds to the second retry of the deluge of another set of initial SYN attempts sent 9 seconds before peak activity at 12:16:42. More so, in both scans, it appears, at least at first, that the wave of initial SYN connections comes in 12-second intervals. The overlap of retries from this particular timing pattern is why the 21-second peak activity was witnessed.

**The 21-Second Mystery**

One of the most intriguing revelations of the examination of this SubSeven traffic was the 21-second time preceding the peak activity for the initial two scans, and later a third, that were observed. It was clear that there was some meaning and explanation associated with this; this couldn’t be a mere coincidence because it occurred three times.

I have an annoying habit: When I’m stumped and frustrated by my inability to figure something out, I start plaguing colleagues. Most have learned to dismiss me with some plausible excuse like, “There are free donuts in the cafeteria. See you later.” But, I cornered my co-worker and longtime bicycling buddy, Vern, and asked him to ponder this mystery. Within seconds, and still a good chance to get those cafeteria donuts, he said, “Oh, that’s easy; it’s the combined backoff times for retries.” This insight made us rethink our approach, and we eventually plotted the traffic separately for initial SYNs and retries, allowing us to discover that the 21-second peak rate was an overlap of retries from different initial waves of SYN activity.

# Fingerprinting Participant Hosts

The assumption now is that the zombie hosts have been “infected” with some malware that is generating the scanning activity. The question then becomes this: Is there a specific operating system that has been exploited, transforming the host into a zombie for this scan? An examination of passive fingerprints can assist in identification of zombies’ operating systems. This assumes that the packets coming from these hosts are not crafted to change default values, such as TCP window size, initial TTL, and TCP options.

Passive fingerprinting categorizes operating systems by looking at unique field values in the packets that have been sent. As we have discussed, different operating system TCP/IP stacks choose unique values for certain fields, such as Time to Live (TTL), TCP window size, and TCP options. There are also other fields that can be examined, such as the Type of Service (TOS) value and the don’t fragment (DF) flag. But, because most operating systems use a default TOS value of 0 and set the DF flag, this might only determine the small percentage of unusual values sent from other operating systems. And, these two fields are best examined in conjunction with other fields and not alone.

[Table 11.1](ch11.html#ch11table01), provided by the Honeynet Project, was used in determining some of the scanning hosts’ operating systems. The lines that are highlighted represent the operating system and associated fingerprints of the majority of the scanning hosts that were observed for this activity.

**Table 11.1. Passive Fingerprinting Values by Operating System**

| **# OS** | **VERSION** | **PLATFORM** | **TTL** | **WINDOW** | **DF** | **TOS** |
| --- | --- | --- | --- | --- | --- | --- |
| #--- | ------- | -------- | --- | ----------- | -- | --- |
| DC-OSx | 1.1-95 | Pyramid/NILE | 30 | 8192 | n | 0 |
| **Windows** | **9x/NT** | **Intel** | **32** | **5000-9000** | **y** | **0** |
| NetApp | OnTap | 5.1.2-5.2.2 | 54 | 8760 | y | 0 |
| HPJetDirect | HP_Printer |  | 59 | 2100-2150 | n | 0 |
| AIX | 4.3.x | IBM/RS6000 | 60 | 16000-16100 | y | 0 |
| Cisco | 11.2 | 7507 | 60 | 65535 | y | 0 |
| DigitalUnix | 4.0 | Alpha | 60 | 33580 | y | 16 |
| IRIX | 6.x | SGI | 60 | 61320 | y | 16 |
| OS390 | 2.6 | IBM/S390 | 60 | 32756 | n | 0 |
| Reliant | 5.43 | Pyramid/RM1000 | 60 | 65534 | n | 0 |
| FreeBSD | 3.x | Intel | 64 | 17520 | y | 16 |
| JetDirect | G.07.x | J3113A | 64 | 5804-5840 | n | 0 |
| Linux | 2.2.x | Intel | 64 | 32120 | y | 0 |
| OpenBSD | 2.x | Intel | 64 | 17520 | n | 16 |
| OS/400 | R4.4 | AS/400 | 64 | 8192 | y | 0 |
| SCO | R5 | Compaq | 64 | 24820 | n | 0 |
| Solaris | 8 | Intel/Sparc | 64 | 24820 | y | 0 |
| FTX(UNIX) | 3.3 | STRATUS | 64 | 32768 | n | 0 |
| Unisys | x | Mainframe | 64 | 32768 | n | 0 |
| NetWare | 4.11 | Intel | 128 | 32000-32768 | y | 0 |
| **Windows** | **9x/NT** | **Intel** | **128** | **5000-9000** | **y** | **0** |
| **Windows** | **2000** | **Intel** | **128** | **17000-18000** | **y** | **0** |
| Cisco | 12.0 | 2514 | 255 | 3800-5000 | n | 192 |
| Solaris | 2.x | Intel/Sparc | 255 | 8760 | y | 0 |

This table of information was obtained at [http://project.honeynet.org/papers/finger/traces.txt](http://project.honeynet.org/papers/finger/traces.txt).

## Arriving TTL Values

If you recall, the arriving TTL values can be used to help identify the scanning host’s operating system. Different operating systems use different initial TTL values when sending a packet. Each router through which the packet travels on its journey from source to destination host examines the TTL value and decrements it by 1. This becomes an indication of the number of “hops” that the packet has traveled. If a router ever discovers a TTL of 0, it discards the packet and sends back an ICMP error message of “time exceeded in-transit” to the sending host. This informs the sending host that the packet has exceeded its welcome on the Internet. This is a mechanism that is used to discard lost packets, such as ones that have become caught in a routing loop.

Initial TTLs of many operating systems have typical values of 32, 64, 128, and 255. These might be different per protocol—TCP, UDP, or ICMP. For instance, Windows NT 4.0 Service Pack 6 has an initial TTL value of 128 for TCP and an initial TTL value of 32 for ICMP packets sent. Fortunately, this examination is limited to TCP so there is no need to account for protocol differences. The arriving TTL values are examined and are helpful in estimating the initial TTL values. The caveat here is that although most operating systems will be configured to use the default initial TTL values, these can be changed. All that can be determined with absolute certainty from the arriving TTL is that it is less than the initial TTL. Of course, this assumes that the source host and destination host are not directly connected to the same local network, in which case the packet could pass from source to destination without the TTL being decremented.

Examination of [Figure 11.4](ch11.html#ch11fig04) for June 29, 2001 shows that there are three clusters of arriving TTL values for the scans. More specifically, the closest scanning host appears to be 8 hops away, and the most distant appears to be 25 hops away from the capturing sensor interface. The assumption is that the scanning hosts had initial TTL values of 128, 64, and 32, and the arriving TTL values are associated with an initial TTL value that is greater than the initial TTL value by the least amount. For instance, if an arriving TTL is 50, it is assumed to have an initial TTL value of 64 and not 128, although either initial TTL value would be valid.

![June 29, 2001 arriving TTL values.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig04.gif)

**Figure 11.4. June 29, 2001 arriving TTL values.**

In the June 29 scan, the largest percentage of scanning hosts, 92.13, had an estimated initial TTL of 128. More than 37 percent of the hosts with an initial TTL of 128 were approximately 11 to 13 hops away from the sensor. According to [Table 11.1](ch11.html#ch11table01), an initial TTL value of 128 is indicative of Windows 9x/NT/2000. An initial TTL value of 32 is Windows 9.x/NT, which comprised 2.66 percent of the scanning hosts. The initial TTL value of 64 is associated with many of the UNIX platforms, including the Linux 2.2.x kernel. The percentage of hosts with an initial TTL of 64 was 5.2.

Examination of [Figure 11.5](ch11.html#ch11fig05) for July 2, 2001 shows the same clustering. More specifically, the closest scanning host appeared to be 8 hops away, and the most distant appeared to be 27 hops away from the capturing sensor interface.

![July 2, 2001 arriving TTL values.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig05.gif)

**Figure 11.5. July 2, 2001 arriving TTL values.**

Looking at the July 2 scan, the largest percentage of scanning hosts, 92.29, had an initial TTL of 128. More than 37 percent of the hosts with an initial TTL of 128 were approximately 11 to 13 hops away from the sensor. 2.36 percent of the scanning hosts had an initial TTL of 32. Finally, 5.35 percent of the scanning hosts had an initial TTL of 64.

The determination from this is that the scanning hosts are not exclusively Windows hosts, but it appears that Windows hosts are the majority of the scanners. This means that whatever malware is exploiting the scanning hosts, it is not exclusive to Windows.

Although the x-axis scaling for plots in Figures [11.4](ch11.html#ch11fig04) and [11.5](ch11.html#ch11fig05) doesn’t readily show this, there was a very distinct clustering around the estimated initial TTL values. For instance, in the June 29 scan, there is a noticeable gap or absence of packets with arriving TTL values between 22 and 42 and between 56 and 103. Similar behavior is observed for the July 2 scan.

## TCP Window Size

A host advertises the TCP window size when it attempts to make an initial connection. The window size is a dynamic value that changes as information is exchanged between hosts and represents the current TCP buffer size for the incoming data. This buffer allows multiple packets to be sent and queued before passing them to TCP and the application. More simply, a given operating system has a default value for the TCP window size, and the window size can change dynamically as data is received and processed.

But, the initial window size can be used to fingerprint the operating system. The user or administrator can customize this, but commonly the default is used.

As you can see in [Figure 11.6](ch11.html#ch11fig06), the bulk of the connections had an initial window size of 8192. This is associated with Windows 9x/NT connections according to [Table 11.1](ch11.html#ch11table01). Although the table doesn’t have a window-size entry for 16384, research has discovered it is associated with Windows 2000. Table 11.1 alludes that a window size of 65535 is associated with Cisco. However, it appears that the high percentages associated with this window size would include other operating systems.

![Scanning host TCP window size.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig06.gif)

**Figure 11.6. Scanning host TCP window size.**

Search engines on the Internet failed to find any operating system associations with a window size of 65535. Attempts were made to examine a week’s collection of TCPdump data for the monitored site to find hosts that had a window size of 65535. Only a dozen of approximately 5,500 hosts were found with a window size of 65535. A scan by nmap could not determine the operating systems. Some of the hosts had ports open, such as 135 and 139, which would indicate Windows versions prior to Windows 2000. Others had port 445 listening, which was introduced in Windows 2000 to support Server Message Block (SMB) talking directly over TCP/IP without the need for the intermediate layer of NetBIOS over TCP/IP (NBT). Yet, other hosts with a window size of 65535 listened at ports 111 (portmapper), 515 (line printer daemon), and 6000 (X11), which are all associated with UNIX hosts. No conclusions could be reached about the operating system associated with a window size of 65,535 based on these findings.

Other unique window sizes that were seen were 32120, associated with Linux, which was found in the June 29 scan only and comprised .19 percent of the total scanning hosts. A window size of 8760 was seen in both scans and reflects a Solaris host. The first scan had 5.21 percent hosts with this window size, and the second scan had 6.60 percent hosts with this window size.

The conclusion that can be drawn examining the TCP window size is the same as examining the arriving TTL values. Looking at [Figure 11.6](ch11.html#ch11fig06), most of the scanning hosts appear to have a window size associated with Windows, yet it also appears that operating systems other than Windows are involved in the scanning too.

## TCP Options

Another interesting field for examination is the Maximum Segment Size (MSS), which is found in the TCP options. This represents the maximum amount of payload that a TCP segment can carry. This does not include the TCP header and the IP header. Generally speaking, the MSS is 40 bytes less than the Maximum Transmission Unit (MTU), assuming a 20-byte IP header with no IP options and a 20-byte TCP header with no TCP options. The MTU can then be used to determine the media on which the sending host resides.

In some instances, although not this one, the MTU, and hence the MSS, might reflect the path MTU. The sender might send a “discovery” packet that looks for the smallest MTU from source to destination by setting the DF flag on the packet. If no ICMP error messages are returned, it is assumed that using the size of the local MTU for packaging packets will not cause fragmentation. If an ICMP error message “unreachable – need to frag (mtu ###)” is returned, it contains the MTU size (`###`) of the link that is smaller than the size of the local MTU. The sender can decrease the size of the packets to avoid fragmentation. The point is that it is possible that the MSS might not reflect the local MTU. However, because there is no indication of discovery packets or that path MTU was used, the assumption is that the MSS does reflect the local MTU.

[Figure 11.7](ch11.html#ch11fig07) reveals that the greatest percentage of scanning hosts resided on a link with an MTU of 1500. This is indicative of Ethernet, found in LAN connections or DSL. The MTU of 576 is associated with PPP or ISDN. Finally, the MTU of 1454 is associated with PPP over Ethernet that is also found on DSL connections.

![MSS/MTU values.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/11fig07.gif)

**Figure 11.7. MSS/MTU values.**

Although the MSS of 536 is associated with PPP and dial-up modems, it is supposed that most of the hosts reside on ISDN, which uses the same MSS. The scenario is that these are all zombie hosts that are directed to do some type of activity at a given time. Either they respond to a catalyst or they all have some kind of time synchronization and are directed to respond at a given time.

The idea of participants from dial-up modems is worth some reflection. First, if a zombie is associated with a dial-up connection, this might not be a sustained connection unless there is some kind of dedicated phone line for the traffic. Additionally, many dial-up connections are at the mercy of Dynamic Host Configuration Protocol (DHCP) with a leased IP number for a certain period of time. How would the “commander” direct a zombie with a changing IP number to launch the activity? One guess is that the zombies report home to the commander periodically. Therefore, only ones that are active and online just before the attack are directed to participate in the attack.

Another question arises from this discussion. It has already been determined that zombies have assignments of mostly unique address ranges to scan. Is there some kind of formula used to assign the address ranges to scan so that the maximum numbers of hosts get scanned?

The suspicion is that most of the participating zombies have a sustained and dedicated Internet connection, but this doesn’t adequately explain the missing destination hosts and subnets.

## TCP Retries

As mentioned, when a source host attempts a TCP connection to a destination host and is unsuccessful, yet gets no indication of the failure, it attempts one or more retries. A source host is not notified of a failure if the connection packet never gets to the destination or the destination host’s response doesn’t get back to the source. In the case of our scanned network, the activity to port 27374 was blocked.Yet, the firewall that blocks the activity “silently” drops the packet with no notification in the form of an ICMP error message to the original source host that there is a problem. The purpose of the silent drop is so that no additional reconnaissance is disseminated about our network perimeter and defense.

For the purposes of this investigation, a TCP retry is defined as one that has the same source and destination hosts, ports, and TCP sequence numbers as the initial attempt. The number of successive retries and the backoff time between retries is TCP/IP stack dependent.

Retries are associated with source code that uses socket connections. In other words, the source code is written so that the socket calls go through the proper layers of the TCP/IP stack. In this case, the socket uses the TCP and IP layers to form the appropriate headers and values for those headers.

The alternative is known as a raw socket, which does not use the TCP/IP stack to form the packet. Instead, the programmer is responsible for supplying the appropriate headers and data. This packet is written directly to the network interface card. Many scanners such as nmap and hping2 use raw sockets.

This scan manifested multiple retries when the destination host was unresponsive. What does this mean? That regular and not raw sockets were used? First, the scanning host really wanted to maximize the opportunity to elicit a response from the destination host—more indicative of scan behavior than flood behavior. Flood behavior would likely send packets using raw sockets as fast as possible. Second, raw sockets require an additional level of complexity because they require the installation of an application programming interface for packet capture on the scanning host—either winpcap for Windows or libpcap for UNIX. The use of standard sockets simplifies the setup required to scan.

# Summary

The determination is that this was a very efficient scan looking for hosts listening on TCP port 27374. The scan was conducted by zombie hosts, which were mostly Windows hosts. It appears that hosts with other operating systems were involved, yet they played only a small part in the percentage of scanning hosts. The significance of this is that the means of infection of the zombie hosts does not appear to be Windows-specific. It is unknown whether the percentage of Windows-based scanning hosts and the percentage of scanning hosts that have other operating systems actually mirror the percentage of Windows versus all other operating systems that are found on the Internet. The implication here would be that the operating systems of the zombie hosts might be consistent with a normal distribution found on the Internet. Another implication is that the percentage of zombie hosts having a particular operating system might represent the ease of compromise for that operating system.

Is the sole purpose of this scan to efficiently identify hosts listening on port 27374? It can be surmised that not all of the zombie hosts were exploited by the SubSeven Trojan. SubSeven is a Windows-based Trojan, and it appeared that not all the zombie hosts were Windows. Perhaps there are SubSeven Trojans that have been developed for other operating systems as well. Whatever the exploit used to “own” the zombies, the “commander” knew about the owned zombie hosts and had no need to scan to find them. Is it possible that this scan search was to find other candidate zombies owned by another commander? This assumes that these new zombie hosts would be Windows-based because they would be listening at the SubSeven port. The new zombies may be used for activity other than the scanning that was witnessed at our site.

Whatever the purpose of this scan, it looks like a pretty sophisticated way to maximize a scan. In a couple of minutes, over 30,000 destination hosts were scanned. This activity demonstrates the evolving sophistication in zombie activity and malicious code in general, as we have witnessed with Code Red and nimda worms. It also shows the burgeoning number of exploited hosts that can be marshaled into active duty because of the innocence or disbelief of home users, paired with always-on connectivity, and operating systems and applications that come ready-assembled for looting and pillaging.
