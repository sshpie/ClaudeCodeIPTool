# Chapter 3. Fragmentation

![Fragmentation](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

At different times, attackers use fragmentation both to mask and facilitate their probes and exploits. Some intrusion-detection systems and packet-filtering devices do not support packet reassembly or perform it correctly and therefore do not detect or block activity where the signature is split over multiple datagrams. Availability or denial-of-service attacks use highly fragmented traffic to exhaust system resources. These are some of the reasons you might want to learn about fragmentation and some of the topics covered in this chapter.

By understanding how this facet of IP works, you will be equipped to detect and analyze fragmented traffic and discover whether it is normal fragmentation versus fragmentation used for other purposes. Fragmentation can be a naturally occurring effect of traffic traveling through networks of varying sized maximum transmission units (MTU). The theory and composition of normal fragmentation is discussed first in this chapter to acquaint you with how it should operate.

# Theory of Fragmentation

Fragmentation occurs when an IP datagram traveling on a network has to traverse a network with a maximum transmission unit that is smaller than the size of the datagram. For instance, the MTU or maximum size for an IP datagram for Ethernet is 1500 bytes. If a datagram is larger than 1500 bytes and needs to traverse an Ethernet network, it requires fragmentation by a router directing it to the Ethernet network. Fragmentation can also occur when a host needs to put a datagram on the network that exceeds its own network’s MTU.

Fragments continue on to their destination, where the destination host reassembles them. Fragments can even become further fragmented if they cross an MTU smaller than the fragment size. Although fragmentation is a perfectly normal event, it is possible to craft fragments for the purposes of avoiding detection by routers and intrusion-detection systems that don’t deal well with fragmentation.

What kind of information must the fragments carry for the destination host to reassemble them back to the original unfragmented state? The following list answers this question:

- All fragments from the same datagram must be associated with each other fragment by using a common fragment identification number. This is cloned from a field in the IP header known as the IP identification number, also called the fragment ID.
- Each fragment must carry what its place or offset is in the original unfragmented packet.
- Each fragment must tell the length of the data carried in the fragment.
- Finally, each fragment must know if more fragments follow it. This is done using the More Fragments (MF) flag.

**The Fragment ID Number/IP Identification Number**

The IP identification value is a 16-bit field found in the IP header of all datagrams. This uniquely identifies each datagram sent by the host. Typically, this value increases by one for each datagram sent by that host.

When the datagram becomes fragmented, all fragments created from this datagram contain this same IP identification number, or fragment ID. The following TCPdump output shows an IP identification number of 202 for this unfragmented output:

```
ping.com > 192.168.244.2: icmp: echo request (ttl 240, id 202) 
```

If this datagram were to become fragmented on the way to its destination, all fragments created from this datagram would share a fragment ID of 202. This TCPdump output was generated using the -vv option. This is a verbose option that says to list the time-to-live (TTL) value and the IP identification values at the end of the standard output.

This information is contained in the IP header. The IP header is placed in an IP datagram followed by an encapsulated fragment. As you have learned, all TCP/IP traffic must be wrapped within IP because IP is the protocol responsible for getting the packet delivered.

## Visualizing Fragmentation: Seeing Is Understanding

This discussion uses Ethernet as the example link layer medium to demonstrate the packaging of datagrams. [Figure 3.1](ch03.html#ch03fig01) depicts the configuration of a datagram that is not fragmented. As previously mentioned, a datagram traveling on Ethernet has an MTU of 1500 bytes. Each datagram must have an IP header, which is typically 20 bytes, but can be more if IP options, such as source routing, are included.

![Ethernet datagram packaging.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig01.gif)

**Figure 3.1. Ethernet datagram packaging.**

As a quick refresher, recall that the IP header contains information such as the source and destination IP numbers. It is considered the “network” portion of the IP datagram because routers use the information found in the IP header to direct the datagram toward its destination. Some kind of data is encapsulated after the IP header. This data can be an IP protocol such as TCP, UDP, or ICMP. If this data were TCP, for instance, it would include a TCP header and TCP data.

[Figure 3.2](ch03.html#ch03fig02) shows a datagram of 4028 bytes. This is an ICMP echo request bound for an Ethernet network that has an MTU of 1500. This is an abnormally large ICMP echo request that is not representative of normal traffic, but it is used to illustrate how fragmentation occurs. So, the 4028 byte datagram will have to be divided into fragments of 1500 bytes or less. Each of these 1500-byte fragmented packets will have a 20-byte IP header like the initial fragment, leaving 1480 bytes maximum for data for each fragment. [Figure 3.3](ch03.html#ch03fig03) examines this same datagram, but shows the allocation of bytes per fragment. The following sections examine the contents of each of the individual three fragments.

![Original 4028 byte fragment broken into three fragments of 1500 bytes or less.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig02.gif)

**Figure 3.2. Original 4028 byte fragment broken into three fragments of 1500 bytes or less.**

![Byte allocations per fragment.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig03.gif)

**Figure 3.3. Byte allocations per fragment.**

### All Aboard the Fragment Train

Turn your concentration to the initial fragment in the fragment train shown in [Figure 3.4](ch03.html#ch03fig04). The “original” IP header will be cloned to contain the identical fragment identification numbers for the first and remaining fragments.

![The fragment engine.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig04.gif)

**Figure 3.4. The fragment engine.**

The first fragment is the only one that will carry with it the ICMP message header. This header is not cloned in subsequent associated fragments and this concept of the first fragment alone identifying the nature of the fragment is significant, as you will soon learn. The first fragment has a 0 offset, a length of 1480 bytes of length, 1472 bytes of data, and 8 bytes of ICMP header; and because more fragments follow, the More Fragments flag is set.

[Figure 3.5](ch03.html#ch03fig05) explains the configuration of the first fragment in the fragment train. The first 20 bytes of the 1500 bytes are the IP header. The next 8 bytes are the ICMP header. Remember that this was an ICMP echo request that has an 8-byte header in its original packet. The remaining 1472 bytes are for ICMP data.

![The guts of the fragment engine.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig05.gif)

**Figure 3.5. The guts of the fragment engine.**

In addition to the normal fields carried in the IP header, such as source and destination IP and protocol (in this instance of ICMP), there are fields specifically for fragmentation. The fragment ID with a value of 21223 is the common link for all the fragments in the fragment train. There is a field known as the More Fragments flag, which indicates that another fragment follows the current one. In this first fragment, the flag is set to 1 to indicate that more fragments do follow. Also, the offset of the data contained in this fragment relative to the data of the whole unfragmented datagram must be stored. For the first record, the offset is 0. Finally, the length of the data carried in this fragment is stored as the fragment length—in this fragment, the length is 1480. This is the 8-byte ICMP header followed by the first 1472 bytes of the ICMP data.

### The Fragment Dining Car

Take a look at [Figure 3.6](ch03.html#ch03fig06) to focus on the next fragment in the fragment train. An IP header is cloned from the “original” header with an identical fragment identification number, and most of the other data in the IP header (such as the source and destination numbers) is replicated for the new header. Embedded after this new IP header is 1480 ICMP data bytes. As you can see, the second fragment has an offset of 1480 and a length of 1480 bytes; and because one more fragment follows, the More Fragments flag is set.

![The fragment dining car.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig06.gif)

**Figure 3.6. The fragment dining car.**

Continuing with fragmentation in [Figure 3.7](ch03.html#ch03fig07), you can examine the IP datagram carrying the second fragment. As with all fragments in this fragment train, it requires a 20-byte IP header. Again, the protocol in the header indicates ICMP. The fragment identification number remains 21223. And, the More Fragments flag is turned on because another fragment follows. The offset is 1480 bytes into the data portion of the original ICMP message data. The preceding fragment occupied the first 1480 bytes. This fragment is 1480 bytes long as well, and it is composed entirely of ICMP data bytes.

![The guts of the fragment dining car.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig07.gif)

**Figure 3.7. The guts of the fragment dining car.**

It is worth repeating that the ICMP header in the first fragment does not get cloned along with the ICMP data. This means that if you were to examine this fragment alone, you could not tell the type of the ICMP message—in this case, an ICMP echo request. This becomes an important issue with regard to packet-filtering devices (as discussed later in this chapter).

### The Fragment Caboose

Examine the final fragment in the fragment train in [Figure 3.8](ch03.html#ch03fig08). Again, an IP header is cloned from the “original” header with an identical fragment identification number, and other fields are replicated for the new header. The final 1048 ICMP data bytes are embedded in this new IP datagram. You see the third fragment has an offset of 2960 and a length of 1048 bytes; and because no more fragments follow, the More Fragments flag is 0.

![The fragment caboose.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig08.gif)

**Figure 3.8. The fragment caboose.**

[Figure 3.9](ch03.html#ch03fig09) depicts the last fragment in the fragment train. Again, 20 bytes are reserved for the IP header. The remaining ICMP data bytes are carried in the data portion of this fragment. The fragment ID is 21223, and the More Fragments flag is not set because this is the last fragment. The offset is 2960 (the sum of the two 1480-byte previous fragments). Only 1048 data bytes are carried in this fragment comprised entirely of the remaining ICMP message bytes. This fragment, like the second one, has no ICMP header and therefore no ICMP message type to reflect that this is an ICMP echo request.

![The guts of the fragment caboose.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig09.gif)

**Figure 3.9. The guts of the fragment caboose.**

## Viewing Fragmentation Using TCPdump

Take a look at the following TCPdump output. As you can see, the three different records represent the three fragments discussed earlier. This means that the host running TCPdump has collected the ICMP echo request after the fragmentation occurred. Here are the records:

```
ping.com > myhost.com: icmp: echo request (frag 21223:1480@0+) 
ping.com > myhost.com: (frag 21223:1480@1480+) 
ping.com > myhost.com: (frag 21223:1048@2960 
```

The first line shows ping.com sending an ICMP echo request to myhost.com. The reason that TCPdump can identify this as an ICMP echo request is because the first fragment contains the 8-byte ICMP header that identifies this as an ICMP echo request. Now, look at the fragmentation notation at the right side of the record. TCPdump convention for displaying fragmented output is that the word *frag* appears, followed by the fragment ID (21223, in this example), followed by a colon. The length of data in the current fragment follows, 1480, followed by an at (@) sign, and then you see the offset into the data (0, because this is the first fragment). The plus (+) sign indicates that the More Fragments flag is set. This fragment knows the purpose of the traffic, knows it is the first fragment, knows that more fragments follow, but doesn’t know what or how many follow.

The second record differs somewhat. Notice that there is no ICMP echo request label. This is because there is no ICMP header to tell what kind of ICMP traffic this is. The IP header will still have the protocol field set to ICMP, but that is all you can tell looking at this fragment alone. You see the TCPdump output lists the fragment ID of 21223, the current data length of 1480, and the offset of 1480. The plus sign signifies that the More Fragments flag is set. This fragment has an affiliation, a follower, and a sense of placement, but is essentially clueless about its purpose—sounds like freshman year at college.

The last line is very similar to the second one in format. It shows the same fragment ID of 21223, it has a length of 1048, and a displacement of 2960. No More Fragments flag appears in the final record, however, as you would expect. This fragment has an affiliation, no sense of purpose, and no followers.

**How the Fragment Offset Is Stored**

Although TCPdump nicely computes the fragment offset for you, it is stored in the packet differently. Be forewarned that if you ever examine a fragment offset in a packet—perhaps from a TCPdump hex dump—you will need to do some manipulation before arriving at the actual byte offset.

The fragment offset is found in part of the sixth byte and the entire seventh byte offset of the IP header. It is a 13-bit field that can represent a maximum value of 8191 (213 – 1). Yet, theoretically, though rarely indicative of normal fragmentation, the offset can be greater than 8191 because the maximum datagram size is 65,535 (216 – 1) bytes. To represent the offset value found in the packet as bytes, multiply it by 8. For those of you who want to know the mathematical origin of this, 65,536 (216) divided by 8192 (213) is 8.

## Fragmentation and Packet-Filtering Devices

This section covers fragmentation and how a packet-filtering device, such as a router or firewall, might deal with it. The problem arises when such a device attempts to block fragmented traffic.

Because only the first fragment of a fragment train will contain any kind of protocol header such as TCP, UDP, or ICMP, only this fragment is prevented from entry into the network guarded by a packet-filtering device incapable of examining state of a header field. What I mean by *state* is it appears obvious to you that any fragment sharing the fragment ID of the blocked one should also be blocked. But, some packet-filtering devices don’t maintain this information. They myopically look at each fragment as an individual entity and don’t connect it with previous or subsequent packets. Intuitively enough, this is not a particularly good architecture, so why is it used? Think about the overhead required to maintain state. It means that each fragment must be examined and stored; this is expensive in terms of time, processing, and memory. Eventually, fragments must be allowed or rejected access and that too consumes more resources. It is far simpler to have an atomic architecture that scrutinizes on a per-packet basis.

If a particular packet doesn’t match the blocking criteria, in this instance, because of the absence of a protocol header, it is allowed into the network. Fragmented TCP or UDP datagrams might contain their respective header information in the first fragment only. Blocking decisions are often based on header information, such as TCP or UDP destination ports. This means that fragmented TCP and UDP are susceptible to the same shortcomings of a stateless packet-filtering device.

One final point to remember is that IP is not a reliable protocol, and it is very possible for the first fragment that contains the protocol header information to be lost. When this occurs, the packet-filtering device has an even more difficult job of allowing or denying traffic. In fact, if one of the fragments does not arrive at the destination, all must be resent.

## The Don’t Fragment Flag

In some of the TCPdump output you have looked at, you might have seen the letters DF in parentheses. This means the Don’t Fragment flag is set. No sur-prises here; as the name implies, if this flag is set, fragmentation will not be done on the datagram. If this flag is set and the datagram crosses a network where fragmentation is required, the router discovers this, discards the datagram, and sends an ICMP “unreachable—need to frag” error message back to the sending host.

The ICMP error message contains the MTU of the network that required fragmentation. Some hosts intentionally send an initial datagram across the network with the DF flag set as a way to discover the path MTU for a particular source to destination host. If the ICMP error message is returned with the smaller MTU, the host then packages all datagrams bound for that destination in small enough units to avoid fragmentation. This is often used with TCP because TCP requires a lot of overhead. Fragmentation can introduce ineffi-ciency because if one fragment is lost, all must be sent again; that is one reason it is desirable to avoid fragmentation. As you can surmise, a malicious user also can use this mechanism to discover the MTU of a segment of your network to be used later for fragmentation exploits. The user could craft datagrams with different lengths and the DF flag set and observe when an ICMP error message is received. This assumes that the targeted network doesn’t disable the ICMP error message from being sent. The following TCPdump output shows an ICMP message in which a router discovered that fragmentation was necessary, but the Don’t Fragment flag was set.

```
router.ru > mail.mysite.com: icmp: host.ru unreachable - need to frag (mtu 
308) (DF) 
```

The stimulus for this reply was that mail.mysite.com attempted to send a datagram larger than 308 bytes to host.ru with the DF flag set before this packet was sent. router.ru finds that the datagram must traverse a smaller network with an MTU of 308 bytes and fragmentation is necessary.

When router.ru examines the record, it finds that the Don’t Fragment flag is set and an ICMP message is sent back to mail.mysite.com informing it of the problem. Now, mail.mysite.com either must package the datagrams to be smaller than the MTU of 308 so that fragmentation doesn’t occur or it must remove the DF flag so that fragmentation can occur and then resend the datagram.

# Malicious Fragmentation

There is no rest for the weary analyst when it comes to malicious fragmentation. Fragmentation, it seems, has provided a field day of play and plunder for the hackers, and they have produced a bevy of attacks.

This advice is repeated for other protocols and at other times in this book, but be especially alert and watchful when analyzing fragmentation. Some of the best analysts I know have been mockingly accused of paranoia by envisioning everyone attacking their networks in every different way. Well, I would like to invite you to join the misfits’ bandwagon of paranoia when it comes to fragmentation. If your IDS cannot be tuned to give special scrutiny to fragmentation, you might be missing a chunk of the action. If your IDS can correctly maintain state, reassemble fragments, and then make some kind of intelligent assessment, you appear to be well-armed.

One of the most infamous denial-of-service attacks associated with fragmentation, Ping of Death, is discussed in [Appendix B](apb.html), “Denial of Service.” The next sections examine a couple of other fragmentation attacks.

## TCP Header Fragments

nmap is an excellent scanning tool that runs on many UNIX platforms and is available from [www.insecure.org/nmap](http://www.insecure.org/nmap). It does conventional port scanning to discover what ports are open on a target host and does stealth scanning that looks for open ports, but also makes an attempt to elude detection by intrusion-detection systems. An nmap command-line option (-f) fragments the 20-byte TCP headers in multiple fragments in an attempt to avoid detection. The following TCPdump output was generated using the command:

```
nmap -f -sS -p 53  target.com 
```

This sends a fragmented SYN connection to port 53 of target.com:

```
truncated-tcp 16 (frag 25096:16@0+) 
fragger.org > target.com: (frag 25096:4@16) 
truncated-tcp 16 (frag 4265:16@0+) 
fragger.org > target.com: (frag 4265:4@16) 
truncated-tcp 16 (frag 34927:16@0+) 
fragger.org > target.com: (frag 34927:4@16) 
```

The preceding TCPdump output shows a scan that fragmented the TCP header. This is a scan from fragger.org that scanned port 53 on target.com using a standard TCP SYN request. This is not obvious, however, because of the small fragments involved.

Looking at the first line of data, you see a fragment with 16 bytes of truncated TCP data. The minimum TCP header is 20 bytes with no options. Because this is not a complete TCP header, TCPdump reports this as `truncated-tcp`. In the next record, the additional 4 bytes of TCP header are sent. It is possible that an intrusion-detection system might not capture or report this kind of stealth scan.

## Teardrop

Now that you are familiar with the way fragmentation should work, take a look at the following TCPdump output. See if you can detect a problem with the fragmentation generated by a malicious program known as Teardrop:

```
evilfrag.com.139 > target.net.139: udp 28 (frag 242:36@0+) 
evilfrag.com > target.net: (frag 242:4@24) 
```

The first fragment delivered is a UDP datagram that has a fragment ID of 242, a length of 36 data bytes, and an offset of 0. This is represented in [Figure 3.10](ch03.html#ch03fig10) by the patterned rectangles. It spans bytes 0 through 35, inclusive.

![Teardrop fragment mutation.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/03fig10.gif)

**Figure 3.10. Teardrop fragment mutation.**

Now, the second fragment comes along. It is associated with the first fragment because of fragment ID of 242, it has a length of 4, and it begins at an offset of 24 bytes into the data portion. It is depicted in [Figure 3.10](ch03.html#ch03fig10) in the solid color in the middle. As you can see, it actually overlaps bytes 24 through 27 of the first fragment.

The Teardrop attack exploits weaknesses in the reassembly process of fragments. The Teardrop program creates fragments with overlapping offset fields. When these fragments are reassembled at the destination host, some systems will crash, hang, or reboot. This attack was first reported in 1997, yet it provides a good example of how malformed fragments can wreak havoc on a target host.

A malformed or an incomplete set of fragments still presents problems for some hosts. More recently, a program known as Jolt2 that will be discussed in more detail in [Chapter 5](ch05.html), “Stimulus and Response,” can cause a denial of service via resource starvation simply by repeatedly sending a non-zero offset fragment to Windows hosts as recent as Windows 2000.

So many problems exist because hosts, routers, and intrusion-detection systems have to deal with many aspects of fragmentation. First, they have to make sure that all the fragments in a fragment train are received. Second, they have to make sure that they are properly formatted—none may overlap—and in aggregate, they may not exceed the maximum datagram size of 65,535. Finally, they must check that no shenanigans are attempted by fragmenting protocol headers. This is a tall order because it requires fragment reassembly and detection of mutations. To do this correctly, this requires a commitment of memory and allocation of CPU power, and if not implemented correctly, it can cause denial of service or other problems.

**Analyzing Fragmentation**

Believe it or not, fragmentation is not really so complicated after you understand a little theory and get comfortable with the notation associated with it. Many times as a network analyst, in the process of examining TCPdump output, I have gone through the mental exercise of “what’s wrong with this fragmentation?” It is more than an academic skill; it is required theory in your arsenal of knowledge to analyze traffic on your network and safeguard it against fragmentation types of exploits.

If you do discover some kind of genuine mutant fragmentation, you might experience an initial and well-deserved feeling of triumph. But, realize that the discovery is just the first step in unraveling the mystery. Next, you have to figure out what the intended purpose of the weird fragmentation is, and this is not always obvious. One common explanation is some kind of denial of service, either a degradation of service or an outright disabling of the target host. Other explanations are to evade detection or circumvent shunning by monitoring or filtering devices incapable of fragment reassembly. Take a look at what is happening on the network in general and the target host specifically to make your assessment.

Finally, if you think that your site is well-protected at the perimeter and you don’t have a firewall or filtering router that is stateful, think again! With such a gaping hole, it is almost trivial for even an inexperienced intruder to bypass your weak defense.

# Summary

Normal fragmentation involves separating and packaging the original datagram into new packets less than or equal to the size of a smaller MTU. Each new fragment becomes a packet of its own with a new IP header consisting of many cloned fields (IP numbers, IP identification number, and so on) from the IP header of the original unfragmented datagram. However, each new fragment will contain some unique identifying information such as the offset into the fragment train, the number of data bytes in the fragment, and whether more fragments follow.

Malicious fragmentation comes in many different forms. Ultimately, the purpose might be a denial of service or an opportunity to sneak some traffic into a network that might normally block an unfragmented incarnation of this traffic. Some packet-filtering devices do not handle fragmentation well, if at all, allowing these fragments entry into the network. By having an appreciation and understanding of fragmentation, in general, you will be better able to detect malicious fragmentation and recognize normal fragmentation.
