# Chapter 8. Examining IP Header Fields

![Examining IP Header Fields](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

This is the first of two chapters that examines fields in the IP packet. This chapter focuses on fields in the IP header, whereas the following chapter looks at fields in the embedded protocol (TCP, UDP, and ICMP) headers. As we continue our journey of looking at traffic from many different perspectives, another view we can assume is to look at the functions of fields in the headers and normal and abnormal values found in those fields. If we are familiar with the purpose of the fields and acquainted with normal values, we should be able to detect mutant or malicious values. When you begin to look at NIDS output or even TCPdump output on a regular basis, this knowledge will come in very handy for detecting problem packets or identifying the nature of malicious traffic.

# Insertion and Evasion Attacks

Before we look at individual fields in the IP header, we’ll make a digression about types of attacks that might thwart a NIDS’ capability to detect malicious activity. As we examine fields in the datagram, we will reference possible insertion or evasion attacks that may be done by manipulating certain field values.

There is a landmark paper written in 1998 called “Insertion, Evasion, and Denial of Service: Eluding Network Intrusion Detection.” The authors Thomas Ptacek and Timothy Newsham discuss attacks that can elude detection by the NIDS by using methods of sending traffic that will cause the NIDS and the destination host to interpret packets differently. The paper is an excellent treatise of different conditions that can cause a NIDS to improperly analyze potentially malicious traffic. The authors conducted several different tests against NIDS to prove their theory.

Along with the denial of service of a NIDS, the paper basically discusses the idea of individual attacks to confuse the NIDS. The first is known as insertion. This is where the attacker sends traffic to a target destination host. One or more of the packets sent is accepted or seen by the NIDS, yet it never reaches the destination host; or if it does, the destination rejects it as faulty. The point that the authors make is that the NIDS and the destination host evaluate traffic differently or perhaps even see different traffic.

A second attack is known as evasion. This involves the same idea of sending traffic to a target destination host. Although the destination host sees the same traffic that the NIDS does, it scrutinizes the packets differently than the NIDS. Perhaps the NIDS rejected one or more packets, but the destination host accepted them. Again, the NIDS and the destination host see the traffic differently. Although the term *reject* brings up some semantic issues especially when compared with actions of packet-filtering devices, it is the terminology used in the paper itself. An evasion attack is successful because the NIDS fails to analyze the packet or data in the packet as the destination host does, allowing the destination host to see a packet or data that the NIDS does not.

## Insertion Attacks

Examining how an insertion attack might work, let’s say we have a NIDS that is on a different network, such as the DMZ, from many of the hosts that it is guarding. Further, let’s also say that the NIDS is looking for signatures that might indicate some kind of problem or notable traffic. One of those signatures might be to look for traffic to telnet, TCP port 23, with a content of REWT as a sign of some backdoor account to telnet.

Now, we have an attacker who has remained undetected in planting a Trojan telnet on a target host and now wishes to log in to that host using the REWT account. The attacker has done some reconnaissance on our network and knows more about the network topology and behavior than we care for him to know. It is possible for the attacker to elude notice of the NIDS if he can make the NIDS accept a packet that the end host will not accept or will never see.

In [Figure 8.1](ch08.html#ch08fig01), the attacker sends three different packets destined for TCP port 23 of the target host, each with one or more characters in the payload. The first contains the letter R, which both the NIDS and the end host receive, examine, and accept. A second character of O is sent that has a bad TCP checksum. Checksums validate the integrity of the packet and if they are not correct, the packet should be discarded. Let’s say that the NIDS sees this packet, is not programmed to validate the TCP checksum, and blindly accepts the packet as a valid part of the stream of characters being sent to the destination host. The destination host receives the packet, validates that the TCP checksum is incorrect, and discards the packet. The attacker has managed to insert a character that causes the NIDS to fail to recognize a real attack or action against the end host. Finally, a third packet is sent with a payload of EWT that both the NIDS and the destination host receive and accept.

![A sample insertion attack.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/08fig01.gif)

**Figure 8.1. A sample insertion attack.**

The NIDS has assembled the TCP stream and concludes it is not a threat because the NIDS does not have a signature for TCP port 23 with a content of ROEWT. Yet, the destination host reassembles this stream as REWT and happily starts a telnet session with a user of REWT that is undetected by the NIDS. Note: This is an oversimplified discussion of this attack; TCP sequence numbers need to be synchronized correctly for this to work properly.

## Evasion Attacks

In the case of evasion depicted in [Figure 8.2](ch08.html#ch08fig02), the destination host sees or accepts a packet that the NIDS rejects. In this case, we are still looking for a telnet session with user REWT to the target destination host. If the attacker can send the traffic in such a manner that the NIDS rejects a packet that the end host accepts, this eludes detection.

![A sample evasion attack.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/08fig02.gif)

**Figure 8.2. A sample evasion attack.**

A possible scenario for this attack is sending data on the SYN connection. Although not typical of normal connections, sending data on SYN is valid per RFC 793. The data on a SYN connection should later be considered part of the stream after the three-way handshake has been completed. Let’s say we have a first packet that arrives on the network with a SYN packet destined for TCP port 23 of our target host. It has a payload of R in the SYN packet. The NIDS only looks for payload after the three-way handshake has been completed, so it totally misses that data. The destination host receives the same packet and knows to store the R for the stream after the three-way handshake is completed. We then have the packets that complete the three-way handshake, each with no data in them, as expected. Finally, we have a normal packet with the letters EWT as the payload destined for the target host TCP port 23.

The result is that the NIDS reassembles the TCP stream for destination host port 23 with a complete payload of EWT. This doesn’t match any signature it knows. The destination host, on the other hand, reassembles the stream as REWT and happily starts the Trojaned telnet session.

To summarize the paper mentioned earlier, there are many techniques that can be used for insertion and evasion attacks against a NIDS. Although the paper doesn’t cover application layer attacks such as HTTP obfuscations, we find that application attacks are a growing trend in evasion. Many of the various attacks are successful just because the NIDS cannot predict the reaction of every possible destination host’s TCP/IP stack to various attacks. There are many facets of the TCP/IP stacks that differ among operating systems.

Although keeping track of a lot of this information is feasible for the NIDS, understand that as you require the NIDS to perform more functions and duties, the NIDS will become slower in processing all traffic to the point where it might begin to drop packets. Ultimately, it is a tradeoff of functionality and speed, and speed is the current winner. One way to deal with the possibility of evasion or insertion attacks is to install a host-based IDS on resources that require more protection or scrutiny. The host-based IDS sees the same packets that the host sees, but this is as far as its resistance to evasion goes. The host would still need the application-level savvy to handle application-based evasion attacks.

This paper can be found at: [www.robertgraham.com/mirror/Ptacek-Newsham-Evasion-98.html](http://www.robertgraham.com/mirror/Ptacek-Newsham-Evasion-98.html).

# IP Header Fields

Let’s begin our examination of the fields in the IP header. Each field will be discussed in terms of its function, any pertinent information about normal and abnormal values, reconnaissance that may be obtained from examining the field, and evasion or insertion attacks possible using the field.

## IP Version Number

The only valid IP version numbers currently in use are 4 and 6, for IPv4 and IPv6, respectively. IPv4 is the most common and pervasive version number thus far. IPv6 is not yet in wide use in user networks in North America, although it is slowly being deployed in the Internet backbone. It is also being used in Europe and Asia.

The IP version field must be validated by a receiving host and if not valid, the datagram is discarded and no error message is sent to the sending host. RFC 1121 states that the datagram must be silently discarded if an invalid value is discovered. So, crafting a datagram with an invalid IP version would serve no purpose other than to test if the receiving host complies with the RFC.

Also, if a packet arrives at a router with an invalid IP version, it should be discarded silently. Using this as a means of an insertion attack is rather difficult unless the attacker is on the same network as the NIDS. If this is the case and a series of packets is sent to the end host with an invalid IP version and a NIDS does not discard them, this is an insertion attack—something the NIDS accepts that the destination host or intermediate router after the NIDS should surely reject.

## Protocol Number

You have already learned that the IP protocol number indicates the type of service that follows the IP header. A list of all the supported protocol numbers and names can be found at [www.iana.org/assignments/protocol-numbers](http://www.iana.org/assignments/protocol-numbers). Conveniently, later versions of nmap have the capability to scan a host for listening protocols. This is done using the **–sO** option. The target host is scanned for all 256 possibilities of protocols. Protocols are deemed listening when no ICMP “protocol unreachable” message is returned. The following text shows an nmap scan for live protocols and the returned nmap assessment:

```
nmap –sO target 

Starting nmap V. 2.54BETA1 by fyodor@insecure.org ( www.insecure.org/nmap/ ) 
Interesting protocols on myhost.net (192.168.5.5): 
(The 250 protocols scanned but not shown below are in state: closed) 

Protocol    State       Name 
1           open        icmp 
2           open        icmp 
6           open        tcp 
17          open        udp 
```

Here is a sample of the traffic that the protocol scan generated:

```
07:30:31.405513 scanner.net > target.com: ip-proto-124 0 (DF) 
07:30:31.405581 scanner.net > target.com: ip-proto-100 0 (DF) 
07:30:31.405647 scanner.net > target.com: ip-proto-166 0 (DF) 
07:30:31.405899 target.com > scanner.net: icmp: target.com protocol 124 
unreachable (DF) 
07:30:31.788701 scanner.net > target.com: ip-proto-132 0 (DF) 
07:30:32.119538 target.com > scanner.net: icmp: target.com protocol 166 
unreachable (DF) 
07:30:34.098715 scanner.net > target.com: ip-proto-236 0 (DF) 
07:30:34.098782 scanner.net > target.com: ip-proto-129 0 (DF) 
07:30:34.098849 scanner.net > target.com: ip-proto-229 0 (DF) 
07:30:32.779583 target.com > scanner.net: icmp: target.com protocol 236 
unreachable (DF) 
07:30:34.099557 target.com > scanner.net: icmp: target.com protocol 109 
unreachable (DF) 
```

The nmap scan examines all 256 different protocol types. A host that receives this type of scan should respond with an ICMP “protocol unreachable” message to any protocols that it doesn’t support.

Although the supported protocols of a host are interesting, another possible piece of reconnaissance from this type of scan is that the host is alive. This is a more stealthy type of scan that might not cause an intrusion-detection system to alarm. However, if the site has a “no ip unreachables” statement on the outbound interfaces of the gateway router or if it blocks all outbound ICMP, this information is not leaked to the scanner. In that instance, the scan is useless.

There is a flaw in the logic used by nmap to discern listening protocols. Nmap assumes that the absence of an ICMP “protocol unreachable” message means that the protocol is listening. Yet, conditions such as the scanned site blocking outbound ICMP messages prevent the nmap scanner from getting these messages. There are other conditions, such as dropped packets, that might also cause the loss of packets and falsely influence nmap. However, the author of nmap tried to consider such situations. Nmap sends duplicate packets for each protocol to deal with the problem of packet loss. Also, if nmap gets no ICMP protocol unreachable messages back, it doesn’t assume all protocols are listening. Instead, it wisely assumes that the traffic is being “filtered” and reports this.

**A Bloody Simple Analogy**

Nmap uses the philosophy of the absence of communication is the confirmation of a condition to determine listening protocols. In other words, the absence of an “ICMP protocol unreachable” message is the confirmation that the protocol is listening. As we’ve seen, there are some flaws associated with this method.

This philosophy reminds me of the real-world situation of going to the doctor’s office for some blood work. Because the doctor and staff are very busy people, they usually tell you on your way out that they will not call you unless they discover something wrong. They are basically telling you that the absence of communication, the lack of a phone call, is a confirmation of a condition, that you are healthy as a horse.

Yet, if you are even a bit cynical, you understand the possible problems with this situation. All kinds of things can go wrong such as losing your blood in the doctor’s office before it gets sent to a lab, losing your blood on the way to or from the lab, or even losing your blood at the lab. Just because you don’t hear from the good doctor doesn’t necessarily mean that everything is copasetic.

Similar problems can beset a packet. A packet can get lost in transit or it can be dropped or blocked at many points in its journey. Nmap attempts to deal with some of these problems, yet the absence of communication might not always be a confirmation of a condition.

## Differentiated Services Byte (Formerly Known as Type of Service—The Prince of Fields)

It seems that the former Type of Service byte has undergone several rounds of alterations since its incipient creation. One of these alterations in RFC 2481 and more currently RFC 3168 calls for the two low-order bits of the differentiated services byte to be used for Explicit Congestion Notification (ECN). The purpose here is that some routers are equipped to do Random Early Detection (RED) or active queue management of the possibility of packet loss.

When congestion is severe, it is possible that a router can drop packets. RED attempts to mitigate this condition by calculating the possibility of congestion in the queue to a router interface and marking packets that might otherwise have been dropped as experiencing congestion.

There are two possible values of the ECN bits to inform that the sending host is ECN-capable. The ECN-capable Transport (ECT) bit settings can either be 01 or 10 in these two low-order bits of the differentiated services byte in [Figure 8.3](ch08.html#ch08fig03). These settings indicate that the sender is ECN-aware. If the sender is ECN-aware, a router that uses RED attempts not to drop the packet, but instead sends it with the Congestion Experienced (CE) bits enabled, and the receiver reacts to this. The bit setting for Congestion Experienced is 1s in both of the ECN bits. We’ll discuss the receiver’s response in more detail when we cover the TCP fields in the next chapter.

![The Differentiated Services byte and ECN.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/08fig03.gif)

**Figure 8.3. The Differentiated Services byte and ECN.**

## The Don’t Fragment (DF) Flag

The Don’t Fragment (DF) flag is a field in the IP header that is set when fragmentation is not to occur. If a router discovers that a packet needs to be fragmented, but the DF flag is set, the packet is dropped and an ICMP message “unreachable - need to frag (MTU size)” is delivered to the sending host. Most current routers include the maximum transmission unit (MTU) size of the smaller link that required the fragmentation.

Fragmentation comes with some overhead, so you should avoid it altogether. If one fragment of the fragment train is not delivered, all fragments must be re-sent. Because of this, when some TCP/IP stacks send data, they first send a discovery packet with the DF flag set. If the packet goes from source to destination without any ICMP errors, the selected datagram size of the discovery packet is used for subsequent packets. If an ICMP message is returned with an “unreachable error – need to frag” message and the MTU is included, the packet is resized so that fragmentation does not occur. This assumes the site allows these ICMP messages inbound.

Some operating system TCP/IP stacks set the DF flag on certain types of packets, and nmap uses this as one of the tests to try to fingerprint the operating system. Also, an attacker can use the DF flag as a means of an insertion attack. This means the NIDS would have to be on a network with a larger MTU than the final destination host. In this case, one or more packets among a series of others have the DF flag set. The NIDS receives the packet(s) and accepts it, but the end host never receives the packet(s) because fragmentation is required, yet the DF flag was set.

# The More Fragments (MF) Flag

The More Fragments (MF) flag tells you that one or more fragments follow the current one. All fragments except the final one should have the MF flag set. The way that a receiving host detects fragmentation is that this flag is set or the fragment offset field in the IP header is set to a non-zero value.

## Mapping Using Incomplete Fragments

Another mapping technique is to try to elicit an ICMP IP “reassembly time exceeded” message from hosts on a scanned network. This can be done by sending an incomplete set of fragments to hosts that are being mapped. For this to work properly, the destination host has to be listening on the port that is scanned if the traffic is TCP or UDP. When the scanned host receives the first fragment, it sets a timer. If the timer expires and the receiving host has not received all the fragments, it sends the ICMP “IP reassembly time exceeded” error back to the sending host.

It is important to note (according to RFC 792) that for the ICMP “IP reassembly time exceeded” error to be generated, the first fragment must not be the missing one. If no first fragment is received, the host receiving the fragments never sets the timer. RFC 1122 recommends that the timer expire between 60 seconds and 2 minutes, though we’ll see that is not always the case.

```
hping2 –S –p 139 –x win98 

06:49:36.986218 verbo.2509 > win98.netbios-ssn: S 1980004944:1980004944(0) 
win 512 (frag 38912:20@0+) 
06:50:41.636506 win98 > verbo: icmp: ip reassembly time exceeded 

hping2 –S –p 21 –x  linux 

11:56:04.064978 verbo.2450 > linux.ftp: S 1198423806:1198423806(0) win 512 
(frag 39067:20@0+) 

11:56:34.056813  linux > verbo: icmp: ip reassembly time exceeded [tos 0xc0] 
```

Hping2 is freeware that is used to generate different types of traffic. Hping2 is first executed with the **–S** option to send a packet with a SYN, a destination port of 139, **-p 139**, and the **–x** option to set the More Fragment flag. One packet is sent to the destination host win98, which as you might guess is a Windows 98 host listening on TCP port 139.

The fragment sent is actually the entire SYN packet—20 header bytes and a 20-byte TCP header. There is no data to send, but the receiving host has no way of knowing this because the MF flag is set. You can see that the MF flag is set by looking at the + in the previous output of TCPdump. The Windows host took approximately one minute and five seconds to time out the fragment reassembly clock. That is when you see the ICMP “IP reassembly time exceeded” message returned.

The next hping2 test is tried on a Linux (2.2 kernel) host on a listening ftp port. The Linux host took about thirty seconds to time out on incomplete fragments sent to destination port 21.

## IP Numbers

IP numbers are 32-bit fields. The source IP number is located in the 12th through 15th bytes offset of the IP header; the destination IP number is located in the 16th through 19th bytes offset of the IP header.

What are some unnatural values for source IPs entering your network? If you see an IP number entering your network that purports to be from your network, there is a problem. Most likely, someone has crafted this packet and is spoofing an IP address in your range. A packet-filtering device should shun this traffic. Additionally, you should never see source IPs coming from the loopback address 127.0.0.1, nor should you see any source IPs that fall in the Internet Assigned Numbers Authority (IANA) reserved private network numbers defined in RFC 1918. These address ranges can be found at [www.iana.org/assignments/ipv4-address-space](http://www.iana.org/assignments/ipv4-address-space). Their intended use is for local internal networks only.

As far as traffic leaving your network, it should have a source IP number that reflects your network’s address space. If you see an IP number coming from inside your network that has an IP number of a different address space, it is either being spoofed or there is a misconfiguration problem with a host inside your network. In either case, this traffic should not be allowed to leave your network. This prevents hosts in your network from participating in distributed denial of service attacks because participant or zombie hosts usually use spoofed source IP numbers so that they cannot be located. Other types of scans use decoy or spoofed source IP’s as a smokescreen. By disallowing outbound traffic that is not part of your address space, these scans will be ineffective as well.

You should also never see a source IP with the loopback 127.0.0.1 address leaving your network because that identifies the local host. And, you should never allow source IP’s in the reserved address ranges to leave your network.

Finally, you shouldn’t allow traffic with a broadcast destination IP address into or out of your network. Such destination addresses are typically used to quickly map other networks or use them as Smurf amplification sites.

## IP Identification Number

The IP identification value is found in bytes 4 and 5 offset of the IP header. For each new datagram that a host sends, it must generate a unique IP ID number. This value is normally incremented by 1, although some use an increment of 256, for each new datagram sent by the host.

This unique value is required in case the datagram becomes fragmented. All fragments from the datagram share this same IP ID number. This is also referred to as the fragment ID number. It is the number that is used by the receiving host to reassemble all fragments associated with a common datagram.

The range for IP ID values is 1 through 65,535 because this is a 16-bit field. Usually, you don’t see IP ID numbers with a value of 0. When the maximum value of 65,535 for the IP ID value is reached, it should wrap around and start again. Different source IPs directing traffic to your network should manifest a different chronology of IP ID values. So, if you see different “alleged” source IPs sending traffic to your network and they appear to have a chronology of incrementing IP ID numbers, it is possible that the source IPs are being spoofed.

As with just about any other field or value in the IP datagram, this value can be “crafted” so as to render it meaningless for interpretation. For instance, if an attacker used a tool that sent all packets with the identical IP ID, they would offer no meaningful forensic value about the attacker’s host. The **–vv** option of TCPdump can be used to display the IP ID number along with the time-to-live (TTL) value.

## Time to Live (TTL)

The TTL is an 8-bit value that is set by the host sending the datagram. Initial TTL values are different depending on the TCP/IP stack used, as you can see in [Table 8.1](ch08.html#ch08table01) that was obtained at `project.honeynet.org/papers/finger/traces`. As we have discussed, each router that the packet travels on its way to the destination host must decrement the TTL value by 1. If a router ever discovers a value of 0 in the TTL, it must discard the packet and return an ICMP “time exceeded in-transit” message back to the sender. This banishes lost packets such as those stuck in a routing loop. This can be used as a possible insertion attack if the NIDS sees the packet, yet the TTL is low enough to be expired by a router before it reaches a target host.

**Table 8.1. Initial TTL Values by Operating System**

| **OS** | **Version** | **Platform** | **TTL** |
| --- | --- | --- | --- |
| Windows | 9x/NT | Intel | 32 |
| AIX | 4.3.x | IBM/RS6000 | 60 |
| AIX | 4.2.x | IBM/RS6000 | 60 |
| Cisco | 11.2 | 7507 | 60 |
| IRIX | 6.x | SGI | 60 |
| Linux | 2.2.x | Intel | 64 |
| OpenBSD | 2.x | Intel | 64 |
| Solaris | 8 | Intel/Sparc | 64 |
| Windows | 9x/NT | Intel | 128 |
| Windows | 2000 | Intel | 128 |
| Cisco | 12.0 | 2514 | 255 |
| Solaris | 2.x | Intel/Sparc | 255 |

What if you want to test to see if a packet is from the source IP it says it is from? You can look at the arriving TTL, estimate the initial TTL by using [Table 8.1](ch08.html#ch08table01), and subtract the arriving TTL from the initial TTL to give you the hop count for the packet to arrive on your network. Then, a traceroute could be executed to see if the number of hops taken back to the alleged source IP approximates the number of hops originally taken into your network. It is possible that the route back to the alleged source IP might be different than the route taken to your network because of the dynamics of routing, but they often do have close hop counts, assuming that there are no major router or traffic problems along the way.

Chances are, if you have different source IPs concurrently entering your network, they have different arriving TTL values. If you see different source IPs entering your network at the same time, doing the same type of activity, with identical arriving TTLs, it is possible that this might be source IP spoofing.

Be aware that some scanning programs purposely randomize the initial TTL value just to eliminate this vestige of the true origin of the datagram.

**Looking at the IP ID and TTL Values Together to Discover Spoofing**

Examine the following output:

```
07:31:57.250000 somewhere.de > 192.168.104.255: icmp: echo request 
(ttl 246, id 5134) 
07:34:18.090000 somewhere.jp > 192.168.104.255: icmp: echo request 
(ttl 246, id 5137) 
07:35:19.450000 somewhere.ca > 192.168.104.255: icmp: echo request 
(ttl 246, id 5141) 
```

This output shows traffic from three purportedly different source IPs to the same infrequently referenced destination IP. The timestamps are within minutes of each other, and the chronology of the IP identification values is worth examining. What is strange about the IP identification values, and why might someone send traffic such as this?

What are the odds that the IP identification values are coincidentally incremental from three alleged different sources to the same destination IP— 192.168.104.255? The particular subnet 192.168.104 does not have active hosts, so this makes the traffic even more suspicious. Although this could be a huge coincidence, it is more likely that someone on one host was sending ICMP echo requests (ping) to the infrequently referenced internal 192.168.104.255 address.

Recall that the IP identification value is a 16-bit field with a range of values from 1 to 65,535. The clustering of values between 5134 and 5141 is highly unlikely for three unique sources. It also appears to be a particularly inactive host (perhaps a single user PC) sending the packets, judging by the small increments in the IP identification values over several minutes. This assumes that the IP identification numbers have not been crafted.

As with much unusual traffic seen on the network, the *what* is far easier to figure out than the *why*. Maybe this was a mapping attempt with one real source and two spoofed sources. This emits a smokescreen effect; even if we noticed this, chances are we wouldn’t be able to identify the real source IP anyway.

Let’s examine this same traffic, but now let’s look at it in terms of the TTL values. Oddly, all the arriving TTL values are identical. This tends to confirm the speculation that all three packets originated from the same host. What are the chances that three different source IPs sending traffic to our network had a probable (uncrafted) initial TTL of 255 *and* each was 9 hop counts away *and* they all had an interest in the same IP address at approximately the same time?

Using the **–vv** option of TCPdump can give us two additional fields of display that can assist in determining if suspicious traffic has been spoofed.

When this traffic was detected on the network, traceroutes were executed back to the alleged source IPs in an attempt to determine if they were real or spoofed source IPs. Here are the results of the traceroutes:

```
traceroute somewhere.de 
   arriving TTL:              246 
   probable initial TTL:      255 
   expected hop count back:   9 
   actual hop count back:     13 

traceroute somewhere.jp 
   arriving TTL:              246 
   probable initial TTL:      255 
   expected hop count back:   9 
   actual hop count back:     13 

traceroute somewhere.ca 
   arriving TTL:              246 
   probable initial TTL:      255 
   expected hop count back:   9 
   actual hop count back:     12 
```

This example of using traceroutes isn’t very conclusive. Each of the three different source IPs had approximately 12 or 13 hops back from the network upon which the sensor sniffed the packets. However, it does offer an example of the mechanics used to attempt to validate the authenticity of the source IP.

The hop count back from the traceroute is believably close to the expected hop count. Yet, using the IP identification values in conjunction with these results, these source IPs probably were spoofed. A hop count back to the source IP that varies widely from the expected hop count is a better indication that the source IP was spoofed. Also, if the actual hop counts back to the three different source IPs differed more substantially from each other, this too would be a better indicator of spoofing.

There are a couple of caveats associated with using traceroute for forensics. First, you might be unable to do traceroutes to/from your network because of router/firewall blocks of ICMP traffic, specifically “time exceeded in-transit” and “port unreachable” messages. Second, note that traceroute to a real IP might not be desirable because it can potentially illuminate your interest in a site.

## IP Checksums

Checksums are used to ensure that data has not gotten corrupted from source to destination. The algorithm used for TCP/IP is to divide the data that is being checksummed into 16-bit fields. Each 16-bit field has a 1’s complement operation done on it and all of these 1’s complement values are added. The final value is considered to be the checksum.

The IP checksum is found in the 10th and 11th bytes offset of the IP header. The IP checksum covers all fields in the IP header only. This checksum is different than the checksums that are computed for the embedded protocol fields because it is validated along the path from source to destination. Embedded protocol checksums such as TCP, UDP, and ICMP are validated by the destination host only. The IP checksum is validated by each router through which it passes from source to destination and finally is validated by the destination host as well.

If the computed checksum does not agree with the one found in the datagram, the datagram is discarded silently. No attempt is made to inform the source host of a problem. The idea is that higher-level protocols or applications will detect this and deal with it.

The formula for the IP header checksum is used for all other embedded checksums as well. First, we divide the IP header into 16-bit fields. Because the IP header length is always a multiple of 4 bytes, we do not have to worry about extra fields that do not fall on 16-bit boundaries.

After all of the fields are separated, we take the 1’s complement of each. This operation simply flips the bit. All of these individual 1’s complement values are added to form the checksum. For example:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 4 | 5 | 0 | 0 | Hex Representation |
| 0100 | 0101 | 0000 | 0000 | Binary Representation |
| 1011 | 1010 | 1111 | 1111 | 1’s Complement |

In the previous output, you see the first 16 bits of a very common beginning to an IP header. Each hex value is represented in four binary bits and each of these bits is flipped. This becomes the 1’s complement value. This operation is commutative so you can add the hex values of the 16-bit fields and then take the 1’s complement and the resulting checksum should be the same.

The IP checksum is examined and recomputed for each hop on the way from source to destination. Intermediate routers validate the IP checksum, and if it is correct, the TTL value is decremented by 1. The IP header checksum must be recomputed to reflect this change in the IP header. Remember that this checksum validates the fields in the IP header only, not the rest of the datagram that consists of the embedded protocol header and data.

The rationale for checking the IP checksum for each hop makes sense when you think about it. The worst-case scenario is that the destination IP becomes corrupted. It makes no sense to forward a packet that has been corrupted because the corruption might alter the intent of the packet.

Although the IP checksum and all other checksums found in the datagram find most packet corruption, there is a problem. It is possible for entire 16-bit fields to be swapped and yet the checksum will remain the same.

```
4500  003c 

4500 = 0100 0101 0000 0000         1011 1010 1111 1111 
003c = 0000 0000 0011 1100         1111 1111 1100 0011 
                                   1011 1010 1100 0010 

003c  4500 

003c = 0000 0000 0011 1100         1111 1111 1100 0011 
4500 = 0100 0101 0000 0000         1011 1010 1111 1111 
                                   1011 1010 1100 0010 
```

Look at the previous output. We swap the first two 16-bit fields (`4500 003c`) in the IP header. The computed checksum for the correct sequence of these 16-bit fields is 1011 1010 1100 0010 (this doesn’t include the high-order bit carryover). But, if we reverse the fields and compute the checksum, it is exactly the same. A datagram with 16-bit fields swapped is a vastly different datagram in meaning and resolution when fields are swapped. So, this is obviously a drawback of using this computation.

Why not use a more complicated and reliable algorithm for the checksum? This computation is done for each packet that a router receives. The simpler the algorithm, the quicker the computation time. The checksum algorithm is a fast and mostly reliable algorithm, and the clean swap of 16-bit fields is a rare occurrence. To read more about IP checksums, look at RFC 1071.

# Summary

Let’s summarize some of the ideas conveyed in this chapter. First, although your NIDS is a necessary tool for risk mitigation, it is not a panacea for detecting all malicious traffic. One reason for this is that insertion and evasion attacks can cause the NIDS to incorrectly scrutinize network traffic. There are many different attacks that can be used and it is simply impossible for a NIDS to know how every different target host on a network will react to a packet. A NIDS cannot know the nuances of each individual host’s implementation of the TCP/IP stack. As well, the NIDS is not aware of network topology differences that can be used in some of the attacks such as packets with low TTL numbers that will never reach the target host. The use of host-based IDS can be used to fortify the security provided by the NIDS.

A savvy analyst should be aware of the types of fields and possible values that are found in the IP header. This is valuable knowledge when examining packets for anomalous values. Recognizing mutant values might not explain the intended purpose of the packet, but it should draw your attention to the packet. From there, it might be possible to determine the nature of the traffic.
