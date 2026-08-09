# Chapter 9. Examining Embedded Protocol Header Fields

![Examining Embedded Protocol Header Fields](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

This second chapter on examining header fields discusses the fields in the headers found after the IP header, namely the TCP, UDP, and ICMP headers. As we discovered in the previous chapter, it is imperative that anyone performing traffic analysis be familiar with the purpose of the fields and expected values. This is the only way to unearth values that are not normal and might be a reflection of some kind of malicious activity.

Because this is a fairly extensive topic, the chapter addresses fields in each of the protocols individually. Hopefully, this will partition the protocols into more manageable chunks of learning.

# TCP

Back in [Chapter 2](ch02.html), “Introduction to TCPdump and TCP,” we discussed that TCP is a reliable protocol. This means that TCP oversees the exchange of data and knows when there is a possible problem by using fields such as sequence and acknowledgement numbers to order and keep track of the exchanged data. There are many more fields in the TCP header than UDP and ICMP have because TCP needs to maintain state and provide optimal flow control between sender and receiver. We’ll examine these fields and others in the context of normal and abnormal use.

## Ports

The port fields are two separate 16-bit fields in the TCP header, one for source (bytes 0 and 1 offset from the TCP header) and another for destination (bytes 2 and 3 offset from the TCP header) port. The valid range of values is between 1 and 65535. The use of port 0 is anomalous and considered to be a unique “signature” of an improper port setting.

When a source host wishes to connect to a destination host, an ephemeral source port is typically selected in the range of ports greater than 1023. For each new connection that the host attempts that is not a retry, a different ephemeral port should be selected. The concept of TCP retries or retransmission will be covered later in this chapter in the section, “[Retransmissions](ch09.html#ch09lev3sec4).” In a scan scenario, you will likely see the source port value incrementing by 1 for each new connection.

One of the telltale signs of an nmap SYN scan to find open TCP ports is a static source port retained over multiple new TCP connections. For example:

```
nmap –sS sparky 

09:40:43.964215 verbo.47247 > sparky.1548: S 2401927088:2401927088(0) win 
2048 
09:40:43.964412 verbo.47247 > sparky.24: S 2401927088:2401927088(0) win 2048 
09:40:43.964465 verbo.47247 > sparky.1547: S 2401927088:2401927088(0) win 
2048 
09:40:43.964553 verbo.47247 > sparky.2564: S 2401927088:2401927088(0) win 
2048 
09:40:43.964604 verbo.47247 > sparky.1484: S 2401927088:2401927088(0) win 
2048 
09:40:43.964642 verbo.47247 > sparky.1460: S 2401927088:2401927088(0) win 
2048 
09:40:43.964695 verbo.47247 > sparky.628: S 2401927088:2401927088(0) win 2048 
09:40:43.964748 verbo.47247 > sparky.1112: S 2401927088:2401927088(0) win 
2048 
```

Although we would expect the source port of scanner verbo to change for each new SYN connection to new ports of target host sparky, the source port number remains constant as 47247.

In contrast, look at the default behavior exhibited by another scanning tool known as hping2. The **–S** option of hping2 performs a different kind of SYN scan. It increments the source port as expected, yet it attempts to open destination port 0 of its target. The intent of this type of scan obviously is not to find a listening port. This type of scan is used to elicit a RESET response to see if a host is alive, because there should be no hosts listening at port 0. Here’s the output from hping2:

```
hping2 –S sparky 

09:44:13.882207 verbo.1788 > sparky.0: S 1553132317:1553132317(0) win 512 
09:44:14.876837 verbo.1789 > sparky.0: S 1894028093:1894028093(0) win 512 
09:44:15.876836 verbo.1790 > sparky.0: S 2032501562:2032501562(0) win 512 
09:44:16.876832 verbo.1791 > sparky.0: S 851202745:851202745(0) win 512 
```

## TCP Checksums

As mentioned previously, the embedded protocols have checksums as well. These cover the embedded header and respective data for TCP, UDP, and ICMP. Unlike the IP checksum, these are end-to-end checksums calculated by the source and validated by the destination host-only. The TCP checksum has been chosen to represent the embedded protocol checksums. UDP does not require a checksum to be computed, unlike IP, TCP, and ICMP. However, it is highly recommended.

The embedded protocol checksums for TCP and UDP are computed using a pseudo-header in addition to the embedded protocol header and data. A pseudo-header consists of 12 bytes of data depicted in [Figure 9.1](ch09.html#ch09fig01): the source and destination IPs, the 8-bit protocol found in the IP header, and a repetition of the embedded protocol length (this is the protocol header length plus the number of data bytes). The zero-pad field found in the 8th byte offset is used to pad the 8-bit protocol field to 16 bits because checksums are performed on 16-bit blocks of data.

![TCP checksum pseudo-header fields.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/09fig01.gif)

**Figure 9.1. TCP checksum pseudo-header fields.**

Why is the pseudo-header necessary? This is a double check that is used by the receiving host to validate that the IP layer has not accidentally accepted a datagram destined for another host or that IP has not accidentally tried to give TCP a datagram that is for another protocol. If there is some errant corruption that occurs in transit, the validation of the IP checksum may or may not discover this, but some fields from the IP header are included in the pseudo-header checksum computation to help protect against this.

Let’s examine a very specific example of how the pseudo-header protects against delivering the packet to the wrong host. [Figure 9.2](ch09.html#ch09fig02) is offered to assist in visualizing the process. Assume that we have a host that sends a packet to destination IP 1.2.3.4. We will use TCP as the embedded protocol, but it really doesn’t matter if the transport layer is TCP or UDP because both use the pseudo-header. The transport layer checksum includes the pseudo-header fields in the checksum computation. Therefore, for the destination IP, a value of 1.2.3.4 is used in the TCP checksum computation.

![Pseudo-header checksum protection.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/09fig02.gif)

**Figure 9.2. Pseudo-header checksum protection.**

On its way from the sending host, the packet travels through a router that, as you remember, must validate the IP checksum before forwarding it. Suppose the router validates the IP checksum, decrements the TTL, and then needs to recompute the new IP checksum. For some unforeseen reason, the IP layer of the router somehow corrupts the destination IP to be 1.2.3.5. The IP checksum is recomputed using the corrupted destination IP. The IP checksum is valid so the packet continues on towards the wrong destination, IP 1.2.3.5.

Assume that the IP 1.2.3.5 exists. The corrupted packet arrives at the wrong destination IP. The IP layer validates the checksum and it is correct because destination IP 1.2.3.5 was used in the IP checksum computation by the corrupting router. The packet is pushed up to the transport layer where TCP uses the pseudo-header fields in the checksum validation. But, the TCP checksum validation uses destination IP 1.2.3.5 in the corrupted packet IP header for validation comparison against the packet’s actual TCP checksum. However, this does not match the TCP pseudo-header checksum from the sending host that used 1.2.3.4 as the destination IP in the pseudo-header checksum. Host 1.2.3.5 then discards the packet because the embedded protocol checksum does not match the computed checksum done by the destination host.

**A Cry for Help**

While reading literature on the purpose of the pseudo-header, it made perfect sense to me that it is used as an additional check to make sure that the packet isn’t sent to the wrong host or protocol. Yet, for the life of me, I couldn’t envision how this was done. I asked several colleagues, but they too shared my confusion when it came to giving an example. I ended up writing noted author and TCP/IP expert, Doug Comer, who shared the example of a router corrupting the destination IP number. I would like to extend many thanks to Mr. Comer for clearing up the confusion.

## TCP Sequence Numbers

The TCP sequence numbers are used to uniquely identify the beginning byte of each TCP segment that is sent. This is a way to keep track of all the TCP data that is sent and received in a TCP stream. Most times, there is more TCP data than can be sent in one TCP segment. Or, some services such as rlogin might send a character at a time over a TCP stream requiring multiple streams per session. Because TCP is a reliable protocol, we must have a mechanism to account for data being sent and received. In part, that is done using TCP sequence numbers.

These sequence numbers should not be repeated unless there is a retry of the same connection if an initial attempt fails and the sender receives no error from either the intended receiver or some kind of packet-filtering device. The initial sequence number (ISN) is the first sequence number that is used in the TCP exchange between the sending and receiving hosts. Each host in the exchange selects a unique initial sequence number when sending the initial SYN connection to the other host.

The formula that TCP/IP stacks use to select their initial sequence number is examined by nmap to help fingerprint the operating system. There is a file that comes with nmap, nmap-os-fingerprints, that has a list of many different operating systems and versions. Nmap performs a given set of tests against a target host. Nmap can categorize a particular operating system by matching the values in responses to different normal and abnormal stimuli sent by the scanning host with the expected values for a given operating system.

The first test executed by an operating system fingerprinting nmap scan is one that examines the initial sequence numbers generated by a receiving host from sent connections to a listening port. Different TCP/IP stacks use different formulas to generate the ISN. Some of the older operating systems used a predictable increment for the ISN for each new connection. But someone watching and sniffing could possibly predict and hijack a connection using this information, as was done in the infamous Mitnick attack. Other operating systems have a time-dependent formula that predictably increases the ISN based on a given time change. This, too, is not considered very secure. The most secure formula for ISN generation is a random, unpredictable one. As a tidbit of information, the SYN that we refer to as the flag to start a TCP connection is actually an abbreviation for synchronize sequence numbers. The following execution of nmap using the operating system fingerprint scan option (-O) shows open ports, TCP sequence number prediction difficulty, and guessed operating system.

```
nmap –O sparky 

(The 1495 ports scanned but not shown below are in state: closed) 
Port              State       Service 
23/tcp            open        telnet 
25/tcp            open        smtp 
111/tcp           open        sunrpc 
513/tcp           open        login 
32771/tcp         open        sometimes-rpc5 
32772/tcp         open        sometimes-rpc7 

TCP Sequence Prediction: Class=random positive increments 
                         Difficulty=46112 (Worthy challenge) 
Remote OS guesses: Solaris 2.6 - 2.7, Solaris 7 
```

Using **nmap –O** to scan the Solaris host sparky and identify the operating system discovers that the generation of initial sequence numbers is based on a formula using “random positive increments.” And, it reports that predicting a new TCP sequence number would be a “worthy challenge.” Sparky is a Solaris 2.7 host, and it appears to be fairly impervious to someone guessing a new TCP sequence number based on a previous one or based on time.

## Acknowledgement Numbers

The method that TCP uses to ensure that data is received is via an acknowledgement. The receiving host sets the acknowledgement flag and the acknowledgement number, which are validation that the receiving host did indeed get the data. The acknowledgement number sent by the receiving host actually represents the next expected TCP sequence number it should receive.

Because a SYN connection consumes one sequence number, and because the acknowledgement value is one more than this sequence number, a valid acknowledgement number must be greater than 0. There is one rare qualification of this. It is possible to use all 2 billion plus TCP sequence numbers available with the 32-bit field in which they are stored. If, by chance, the last TCP sequence number sent is the largest 32-bit number allowed, the receiving host wraps around and acknowledges that the next expected sequence number is 0. This is an infrequent occurrence.

Nmap can attempt to identify live hosts by sending a remote host a TCP connection with an unsolicited ACK flag set. This method of host identification is often more successful than pinging the host because many sites now block inbound ICMP echo requests. Yet, a router that doesn’t maintain state may allow in “established” traffic in which the ACK flag is set. The desired response to the unsolicited ACK is a RESET from the remote host, which indeed indicates that the remote host is alive regardless of whether the scanned port is listening. Current versions of nmap have a telltale signature because the ACK flag is set, yet the acknowledgement number is 0 as shown in the following output.

```
verbo.52776 > win98.netbios-ssn: . ack 0 win 4096 <wscale 10,nop,mss 
265,timestamp 1061109567[|tcp]> 
```

## TCP Flags

TCP flags are used to indicate the function of a given TCP connection or session. The SYN flag starts a session and the FIN flag terminates a session gracefully. A RESET is used to abort a session. The ACK flag is set to indicate an acknowledgement of data by the receiver. The ACK flag is set on all packets after the initial SYN. The PUSH flag is typically used to tell the sending host to write all of its buffered data to send to the destination host and for the destination host to PUSH it up to the TCP layer. It is actually possible to send data without the PUSH flag set when all of the data in the sending buffer is not completely emptied. Finally, the URGENT flag is used to indicate that data has the highest priority.

The TCP flags have many different valid combinations. And, there are many different invalid combinations that are used for different purposes. Early in the evolution of NIDS, many would examine traffic for initial SYN attempts only. Scanners realized this and would send a SYN/FIN combination that might elicit a response from a host. Different operating system TCP/IP stacks respond differently to mutant flag settings, so this is used to attempt to fingerprint the operating system. We will examine some of the situations in which valid and invalid flag combinations can occur over the next several sections.

### TCP Corruption

Just because you see mutant TCP flag combinations, it is not necessarily an indication of malicious behavior. Packets can and do get corrupted, and it is possible for TCP flags to be unnaturally set after some kind of corruption in the TCP portion of the packet.

Look at the following packet received on a Shadow NIDS. This was an attempted Napster connection back in the days when Napster was a free and legal method of exchanging MP3s:

```
host.home.com.1310 > napster.com.6699: SRP [bad hdr length] (DF) 
```

There are two anomalies that stand out looking at the record. The first is the mutant flag settings of SRP, meaning that all three of the SYN, RESET, and PUSH flags are set simultaneously. The next sign is TCPdump’s notation of `bad` `hdr length`.

A `bad hdr length` is an error generated by TCPdump when the specified TCP header length is greater than the actual TCP segment (header and data) length. Because there is no field in the IP datagram that holds the value of the TCP segment length (header and data), TCPdump computes this value by using fields it does have. It subtracts the IP header length from the IP datagram total length. For properly formatted packets, this reflects the true TCP segment length. One of the validity checks performed by TCPdump is to test if the packet’s specified TCP header length in bytes is greater than the computed TCP segment length. If this comparison is true, there is something definitely wrong with a length field, and that is when the `bad hdr length` error is displayed.

It will be become apparent why TCPdump believes this by examining the following hex dump output. First, the IP header is contained between the brackets and the TCP header between the less than and greater than signs:

```
[4500 0028 8974 4000 7406 a9c5 1804 ee22 
80f4 4c7b] <051e 1a2b 0000 029d 9efe a721 
a7ae 5010 2058 ac31 0047 0050> 
```

Now let’s turn our attention to the length fields in the packet. First, look at the IP total datagram length in the bolded 2nd and 3rd bytes offset of the IP header. You should see a 0x28 or 40-byte IP datagram length. The IP header length is found in the bolded low-order nibble of the 0 byte offset of the IP header. As we know, this value of 5 represents a 20-byte IP header.

The protocol field in the 9th byte offset of the IP header has been bolded to highlight the embedded protocol. Because we discover a 06 in that field, we know that a TCP header follows. The computed TCP segment length is then 40–20, giving us 20 bytes for TCP header and data. This is room enough for a TCP header with no options and no data such as might be found on a plain SYN attempt.

Yet, in the TCP header length, we find a length of 0xa in the bolded high-order nibble of the 12th byte offset, which indicates a 40-byte TCP header after we multiply it by 4 to translate from 32-bit words to bytes.

Using these fields, do you know why TCPdump generates the `bad hdr` `length` error? This is a datagram with a total length of 40, including a 20-byte IP header length, yet a TCP header that professes to be 40 bytes. We need a minimum IP datagram length of 60 to house this data if indeed there has been no corruption.

Is it possible that this packet has been corrupted and the checksum is invalid? Remember, if this involved packet corruption in the TCP header or data, the only host that will detect this is the destination host. The NIDS sensor typically does not validate a TCP checksum.

Here is what we can deduce about this packet. Chances are that the IP header is fine because the previous router did not drop it. Routers are supposed to validate the IP checksums and silently drop packets with inaccurate ones. Now, before reaching the destination host and having the TCP checksum validated, it passes by the sensor where TCPdump finds a problem with it. It is possible that the router corrupted the IP header after the checksum was computed, but the header otherwise appears to be normal.

At this point, we don’t know if the packet has been accidentally corrupted or intentionally corrupted for whatever reason. The only other ways to verify packet corruption is to manually compute the checksum of the received packet on the sensor or examine how the receiving host (napster.com) reacts. The problem with looking at how napster.com reacts is that if the checksum is invalid, we will see no response. Yet, if the checksum is valid, this weird combination of flags might not elicit a response either. If we do observe an unlikely response from napster.com (most likely a RESET), this means that the checksum is valid and the packet wasn’t corrupted on route from source to destination. This means that the packet was most likely crafted with mutant values at the source. Too, there is always the possibility of cleanly swapped 16-bit fields that would corrupt the packet, but there would be no manifestation of it in the checksum.

Vern Paxson, creator of an IDS named Bro, talks of traffic he has labeled “crud” in his paper “Bro: A System for Detecting Network Intruders in Real-Time.” His definition of crud is “innocuous implementation errors” that create traffic pattern pathologies that look similar to genuine attacks. He cites examples of an errant TCP/IP stack that routinely sets the URG flag on a SYN attempt and another that sets the DF flag on traffic fragments. Although this is different than packet corruption, the important point to keep in mind is that not all-anomalous traffic you witness is malicious. It is remotely possible that a very small amount is due to corruption, or crud.

### ECN Flag Bits

Until very recently, the two high-order bits of the TCP byte were known as the reserved bits. They had no purpose, and the value found in the bits should have been 0. However, when tools such as nmap came along, it was discovered that these bits could be used to try to help fingerprint a remote operating system. Different operating system TCP/IP stacks would respond uniquely when these bits were set.

Some would reset the bits to 0, and others would simply leave them with the current value. Hence, some insight could be made of the remote host’s operating system TCP/IP stack. This alone might not be enough to inform the scanner of the operating system, but used in conjunction with several other tests, the operating system could be conjectured with a high probability.

Remember back when we were discussing the differentiated services byte in [Chapter 8](ch08.html), “Examining IP Header Fields,” we introduced a new purpose for the two low-order bits known as Explicit Congestion Notification (ECN)? The intent was for a router to be able to notify a sender that there was congestion in the network and to reduce its sending rate.

How exactly does that occur? Currently, as discussed in the ECN RFC 3168, the only transport capable of reacting to that congestion notification is TCP. So, TCP must be prepared to deal with this. The RFC offers using the two high-order bits of the TCP flag byte (see [Figure 9.3](ch09.html#ch09fig03)) as fields for ECN. The bit to the right of the high-order bit is known as the ECN-echo bit. This bit is turned on when TCP receives a packet that has the Congestion Experienced bits set in the differentiated services byte of the IP header. This means that both end-points of the TCP conversation are ECN-capable, which is determined during the three-way handshake.

![The ECN bits of the TCP flag byte.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/09fig03.gif)

**Figure 9.3. The ECN bits of the TCP flag byte.**

If TCP sets the ECN-echo bit, the purpose is to inform the sender to reduce the rate at which it is sending data because there is congestion between the sender and receiver. Upon receipt of a TCP segment with the ECN-echo bit set, the sender reduces its congestion window, the size of the sending buffer, by half. After it reacts in this manner, it turns on the Congestion Window Reduced (CWR) bit to inform the other side of the conversation that remedial action to reduce congestion has occurred. This bit is found in the high-order bit of the TCP byte flag.

Although this mechanism helps reduce the number of packets dropped, it is anticipated that many existing NIDS will begin to alarm on these new TCP flag bytes being used. Right now, most uses of these bits are for scanning purposes only. Also, some packet-filtering devices will not allow inbound TCP segments with these bits set. So, much customization will have to be done to smoothly introduce ECN and distinguish it from the rogue scans.

### Operating System Fingerprinting

When nmap is placed in operating system fingerprinting mode with the **–O** option, it sends some mutant flag combinations when an open port is discovered. Look at the following output from nmap remote operating system scans:

```
nmap –O win98 

20:33:16.409759 verbo.47322 > win98.netbios-ssn: SFP 861966446:861966446(0) 
win 3072 urg 0 <wscale 10,nop,mss 265,timestamp 1061109567[|tcp]> 

20:33:16.410387 win98.netbios-ssn > verbo.47322: S 49904150:49904150(0) ack 
861966447 win 8215 <mss 1460> (DF) 

nmap –O sparky 
20:37:00.738412 verbo.50107 > sparky.echo: SFP 2326441544:2326441544(0) win 
2048 urg 0 <wscale 10,nop,mss 265,timestamp 1061109567[|tcp]> 

nmap –O linux 

20:44:50.370158 verbo.42318 > linux.ftp: SFP 1749165064:1749165064(0) win 
1024 urg 0 <wscale 10,nop,mss 265,timestamp 1061109567 0,eol> 
```

In the first scan of a Windows 98 host, the mutant flag combination of SYN/FIN/PUSH/URG is sent to the Windows port 139. This is a NetBIOS session service port, and the Windows host listens on this port. Yet, amazingly enough, it responds with an acknowledgement! This behavior is not what we expect.

In the second nmap scan, the same technique of sending the mutant combination of SYN/FIN/PUSH/URG flags to a listening Solaris port (echo) is attempted, and no response is elicited. This same combination of flags is sent to a listening Linux ftp port in the third scan, and no response is received. This is the expected behavior, which conforms to RFC specifications. Yet, you can see how this test can be used to distinguish Windows hosts from all others.

As a new analyst, it is often difficult to distinguish between what appears to be malicious behavior and TCP/IP stacks that don’t conform to the RFC specifications. It is hard to understand the intent when a response isn’t as you expect. Many times, even an experienced analyst does not know if abnormal TCP flag settings are an indication of some wayward TCP/IP stack or someone up to no good.

### Retransmissions

What if an initial TCP connection is attempted, yet the host attempting the connection doesn’t receive a response from the destination host? A destination host might not respond because it might not be up or might not exist. A router might attempt to deliver an ICMP message about the destination host being unreachable, but if the router has been silenced from delivering unreachable messages, the sending host will never know that there is a problem. A destination host might be sitting behind some kind of packet-filtering device that blocks the connection inbound, yet silently drops the connection without informing the sending host.

It is also possible that the destination host responds positively (SYN/ACK) or negatively (RESET/ACK), yet for some reason the sending host doesn’t receive these replies.

Additional attempts or retransmissions are made to contact the host in situations like this. The number of retransmissions and the time intervals in which they are attempted varies by TCP/IP stack. Eventually, the sending host ceases the connection attempts.

How can you distinguish retransmissions or retries from separate new TCP connections to a destination host? The source ports remain the same, and the TCP sequence numbers don’t change for retransmissions. This is not a fail-safe detection method. It is also possible that the sender is crafting packets that use the same source ports and TCP sequence numbers.

Examine the following set of retries—specifically, look at the time and the IP identification number changes. The IP identification numbers should change on a retry as well as a set of unique connections. The sending host generates an entirely new packet for the retry so the IP identification number should increment or wrap:

```
17:14:18.726864 1.1.1.1.62555 > 192.168.44.63.3128: S 20583734:20583734(0) 
win 8192 <mss 1380>(DF) (ttl 17, id 15697) 
17:14:21.781140 1.1.1.1.62555 > 192.168.44.63.3128: S 20583734:20583734(0) 
win 8192 <mss 1380> (DF) (ttl 17, id 33873) 
17:14:27.776662 1.1.1.1.62555 > 192.168.44.63.3128: S 20583734:20583734(0) 
win 8192 <mss 1380> (DF) (ttl 17, id 46113) 
17:14:39.775929 1.1.1.1.62555 > 192.168.44.63.3128: S 20583734:20583734(0) 
win 8192 <mss 1380> (DF) (ttl 17, id 54353) 
```

Now, look at the time changes between attempted retries. Between the first and second connection attempts, the wait is approximately 3 seconds. This doubles to 6 seconds between the second and third connections. And, finally, this doubles again to 12 seconds between the third and fourth attempts. This doubling of the backoff time might not always be witnessed—different TCP/IP stacks use different retry-time algorithms for the subsequent retries.

Often, analysts not familiar with the concept of retries misread what is happening here. They erroneously believe that an attacker is attempting multiple connections to the destination host. Instead, the retries are automatically generated by TCP.

#### Using Retransmissions Against a Hostile Host—LaBrea Tarpit Version 1

A very clever defender against the Code Red worm scans of web servers, Tom Liston, wrote a program that “tarpits” scanners looking for unassigned IP numbers. Typically, when you see activity to an unassigned IP address, it might mean someone is scanning hosts on your network. He named his code LaBrea after the La Brea Tar Pit.

Here is how LaBrea works. It is installed on a local host and first listens for ARP requests to unassigned IP numbers. Usually, a router generates this ARP request for the unknown IP number. When no ARP reply is generated by a real host after three seconds, the LaBrea host fakes a response to an ARP reply.

If a SYN follows from the scanning host (in this case, usually an infected Code Red host), the LaBrea host fakes a SYN/ACK response. LaBrea does not examine the destination port, so this program could be used against any TCP scan or attempted TCP connection to an unassigned IP number. The scanning host then completes the three-way handshake and attempts to send some data. The LaBrea host now deliberately fails to respond by never ACKing the data sent by the scanning host. Thus, the scanning host is tarpitted in retransmissions until it times out. This consumes resources on the scanning host and slows its capability to scan, especially if it waits for a response to proceed with further scanning.

Let’s examine what happens step by step in the LaBrea tarpit:

```
ARP request for unassigned IP 192.168.143.236 

18:34:32.757821 arp who-has 192.168.143.236 tell 192.168.143.1 
18:34:35.743528 arp who-has 192.168.143.236 tell 192.168.143.1 

After 3 seconds and no ARP reply, LaBrea host fakes reply 

18:34:35.743591 arp reply 192.168.143.236 (0:0:f:ff:ff:ff) is-at 
0:0:f:ff:ff:ff 
```

First, LaBrea looks for ARP requests on the local network. These usually come from the local routing device. If it sees no ARP reply after three seconds (this is the default wait time, however it can be changed by a command line option), it fakes an ARP reply. In this case, we see an ARP request for host 192.168.143.236 from the local router 192.168.143.1. This is an unassigned IP number. No ARP reply is seen and another ARP request is generated three seconds after the initial one.

After three seconds, the LaBrea host fakes an ARP reply and tells 192.168.143.1 that the MAC address for 192.168.143.236 is a bogus 0:0:f:ff:ff:ff. Neither the 192.168.143.236 address nor the MAC address is real. This is a way to allow the routing device to respond to the scanner without generating an ICMP unreachable error. Now, the LaBrea host will look for any traffic destined for the bogus MAC address going across the network.

After the bogus MAC address is generated by LaBrea, the scanning host’s SYN attempt is answered by the LaBrea host simulating a listening host and port as shown.

```
Infected Code Red host requests SYN 

18:34:35.743817 codered.victim.com.1113 > 192.168.143.236.www: S 
301190748:301190748(0) win 8192 <mss 1460,nop,nop,sackOK> (DF) 
LaBrea host spoofs ACK 

18:34:35.743940 192.168.143.236.www > codered.victim.com.1113: S 
2516582400:2516582400(0) ack 301190749 win 10 

Infected Code Red host completes three-way handshake 

18:34:35.744190 codered.victim.com.1113 > 192.168.143.236.www: . ack 1 win 
8576 (DF) 
```

In the previous output, you see the codered.victim.com host attempt a SYN connection to the unassigned destination IP address 192.168.143.236 destination port 80 (www). LaBrea then generates a response to this connection with a SYN/ACK from the non-existent IP address 192.168.143.236. And, as expected, the codered.victim.com host completes the three-way handshake. The connection is now “established.”

Next, the codered.victim.com host attempts to send 10 bytes of data to fill the receive buffer of the bogus web server 192.168.143.236 as can be seen in the following output:

```
Code Red host sends 10 bytes of data 
18:34:35.745555 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
Retransmission at +6 seconds 
18:34:41.746643 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
Retransmission at +12 seconds 
18:34:53.743027 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
Retransmission at +24 seconds 
18:35:17.735734 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
Retransmission at +48 seconds 
18:36:05.741181 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
Retransmission at +96 seconds 
18:37:41.911995 codered.victim.com.1113 > 192.168.143.236.www: . 1:11(10) ack 
1 win 8576 (DF) 
3 minutes 6 seconds later retransmissions stop 
```

There is no PUSH flag set as you are used to seeing because the PUSH flag is only set when the sending host empties its sending buffer. But, because codered.victim.com’s send buffer is greater than 10 bytes, the only flag you see is the ACK flag acknowledging receipt of the bogus initial SYN connection from 192.168.143.236.

Now, here comes the tarpit. There is no acknowledgement of the data sent by codered.victim.com. So, it must retransmit the data. The retransmission timer for this particular host has an exponential backoff where it doubles the time between retries. Of the several runs of LaBrea attempted, the first retry varied in wait time from three to twelve seconds after the initial try. Several attempts used the six-second wait as manifested in the previous output.

Five retries and three minutes and six seconds after the initial attempt to send data, the codered.victim.com host gives up. But it has expended resources and been delayed in its scanning for this duration. If the scanning host waits for the response from the LaBrea host before continuing the scan, it has been slowed down in its efforts. This is more effective if the scanning host is tarpitted over and over again for all unassigned IPs on this network.

Although it appears very tempting to use LaBrea, make sure that you understand the implications of doing so. First, as currently written, the tarpit is performed for any TCP connection for which there is no real destination IP, regardless of destination port number. If a real host in the network temporarily experiences problems and is unable to respond to an ARP request, legitimate connections might be erroneously tarpitted. Also, it appears that firewalls that maintain state tables of connections can become encumbered by the tarpitted connections. LaBrea code can be found at [www.hackbusters.net](http://www.hackbusters.net).

**La Brea Tar Pit**

La Brea Tar Pit is located in Los Angeles’s Hancock Park. It was the site of a natural accumulation of tar that formed over oil. During the Early Pleistocene time (about 2.5 million years ago), animals became tarpitted and died when attempting to drink at the site or cross the tar formation.

## TCP Window Size

The TCP window size is the method employed by a receiving host to inform the sending host of the current buffer size for data sent for that connection. This is a flow control mechanism because it is dynamic. The window size becomes smaller for all data that has been received, but not yet processed by the receiving host. If the receiving buffer ever becomes full, the window size becomes 0 informing the sending host to temporarily halt transmission of any more data. After the receiving host has processed some of the data in the buffer, it sends a window size update to the sending host to inform it to resume sending data.

As you can see, flow of control for TCP sessions is mostly done by the receiving host by use of the window size. We have a tendency to assume that the sender is really the one controlling the flow of data across the network. But, for the most part, the receiver is the director of the data flow.

Initial window sizes are used by nmap to determine the operating system. Different TCP/IP stacks select different initial window sizes, which is used to help fingerprint the operating system.

### LaBrea Version 2

If you recall, the original version of LaBrea was able to slow down a scanning or attacking host for the amount of time it took the attacker’s TCP connection to time out from lack of a response after the three-way handshake. Depending on the attacker’s TCP/IP stack implementation of the number of retries and the backoff time between timeouts, the attacker could be delayed several minutes.

LaBrea’s author, Tom Liston, improved on his own concept using another technique known as the TCP persist timer. As we just learned, if a receiving host’s TCP window is filled and it cannot accept any more data from the sender, it notifies the sender to cease sending data by setting the window size to 0. Ordinarily, when the receive buffer frees up space by sending the data to TCP, a TCP segment follows with a window size greater than 0. What if this new window advertisement is lost? Both sender and receiver would be frozen waiting for the other to act.

There is a mechanism to deal with this known as a window probe. After a timer expires and the sender has not received any new window advertisement from the receiver, the sender transmits a TCP window probe that carries 1 byte of payload with the exclusive purpose of soliciting a response from the receiver to discover if the window size has been increased. The sender persists in sending window probes until the window size increases or until either of the end-host applications terminates.

The new version of LaBrea uses the persist timer to tarpit the attacker for an indefinite amount of time, as you can see from the following TCPdump output. It works exactly like the previous version of LaBrea up through the three-way handshake. Instead of not responding, LaBrea reacts to the sender’s data with an acknowledgement, but with a window size of 0. It doesn’t increase the window size via a window update forcing the scanner to send a window probe. The LaBrea host responds to the window probe, but again advertises the window size as 0. This pattern of window probe and a response of a window size of 0 continues indefinitely. This tarpits the attacker into a persistent connection with the LaBrea host if there is no intervention. Take a look at the output:

```
19:28:07.577541 codered.victim.com.2045 > 10.10.10.155.www: S 
882335286:882335286(0) win 8192 <mss 1460,nop,nop,sackOK> (DF) 
19:28:07.577618 10.10.10.155.www > codered.victim.com.2045: S 
998514038:998514038(0) ack 882335287 win 5 
19:28:07.577879 codered.victim.com.2045 > 10.10.10.155.www: . ack 1 win 8576 
(DF) 

19:28:07.581366 codered.victim.com.2045 > 10.10.10.155.www: . 1:6(5) ack 1 
win 8576 (DF) 
19:28:07.581437 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
19:28:09.820965 codered.victim.com.2045 > 10.10.10.155.www: . 6:7(1) ack 1 
win 8576 (DF) 
19:28:09.821041 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
19:28:14.424567 codered.victim.com.2045 > 10.10.10.155.www: . 6:7(1) ack 1 
win 8576(DF) 
19:28:14.424646 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
19:28:23.621770 codered.victim.com.2045 > 10.10.10.155.www: . 6:7(1) ack 1 
win 8576 (DF) 
19:28:23.621845 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
19:28:42.016162 codered.victim.com.2045 > 10.10.10.155.www: . 6:7(1) ack 1 
win 8576 (DF) 
19:28:42.016237 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
19:29:18.804962 codered.victim.com.2045 > 10.10.10.155.www: . 6:7(1) ack 1 
win 8576 (DF) 
19:29:18.805038 10.10.10.155.www > codered.victim.com.2045: . ack 6 win 0 
```

We join our session after the faked ARP reply by the LaBrea host. For orienta-tion purposes, we see the three-way handshake completed by the Code Red victim host, codered.victim.com, and the LaBrea host pretending to be host 10.10.10.155. The codered.victim.com host then sends 5 bytes of data (in bold output) because that was the advertised window size of the bogus 10.10.10.155 host. The 10.10.10.155 LaBrea host responds with an acknowledgement of receipt of data, but a window size of 0. The codered.victim.com host waits a couple of seconds when it doesn’t get any notification of a window size increase and sends a 1-byte window probe to 10.10.10.155. The LaBrea host lazily responds to the window probe essentially telling the inquirer to chill out; it is still alive and running, but is not ready for any data just yet. As you witness, this cycle is repeated with the probing host increasing its wait time for future probes and becoming tarpitted indefinitely.

# UDP

UDP is a much less complicated protocol to discuss than TCP because it doesn’t have any of the fields that ensure reliable delivery. UDP does not make any guarantees that data will be delivered and leaves this function to applications to handle. This section will examine the fields found in the UDP header and how UDP port scanning is accomplished.

## Ports

Just as with TCP ports, UDP port fields are two separate 16-bit fields in the TCP header—one for source and another for destination. The valid range of values is between 1 and 65535; the use of port 0 is typically a signature of unusual activity.

When a source host wishes to connect to a destination host, an ephemeral port is typically selected in the range of ports greater than 1023. For each new sending connection, a different ephemeral port should be selected.

### UDP Port Scanning

Unlike TCP that responds with either a positive response (SYN/ACK) to a listening port or a negative response (RESET/ACK) to a non-listening port, UDP doesn’t respond to an initial connection with any positive feedback. But, a live host responds with a negative response of ICMP “port unreachable” to a non-listening UDP port. This is how scanners determine if the UDP port is listening or not. This is another more stealthy way to scan for live hosts, assuming the site does not block outbound ICMP error messages.

So, the absence of an ICMP “port unreachable” error is construed as an open port. What if the scanning packet got dropped on its way to the target host? Or what if the target host responds with an ICMP “port unreachable” message, but the site blocks outbound ICMP messages? Or what if the site blocks inbound UDP and blocks all outbound ICMP or ICMP unreachable messages so that the scanner cannot receive an ICMP “admin prohibited” message to know this? This can be misconstrued as a listening port. Nmap scans the same UDP ports many times to try to deal with the case of dropped packets. If one packet is dropped and the network is not under duress or having problems, chances are one of the repeated packets will not be dropped. And once again, nmap is intelligent enough to know that the lack of any response is more likely an indication of filtering of some sort by the destination site than it is of all UDP ports listening.

This is a UDP port scan in the 32771 to 34000 range to look for open Remote Procedure Call (RPC) ports on a Solaris host. Nmap found many of these ports open. It assumes that a port is open if no ICMP “port unreachable” message was returned. As we have discussed, this is not always true.

```
nmap –sU sparky –p 32771-34000 

WARNING:  -sU is now UDP scan -- for TCP FIN scan use -sF 
Starting nmap V. 2.12 by Fyodor (fyodor@dhp.com, www.insecure.org/nmap/) 
Interesting ports on sparky (1.1.1.100): 
Port    State       Protocol   Service 

32771   open        udp        unknown 
32772   open        udp        unknown 
32773   open        udp        unknown 
32774   open        udp        unknown 
32782   open        udp        unknown 
32783   open        udp        unknown 
32784   open        udp        unknown 
32785   open        udp        unknown 
32786   open        udp        unknown 
32797   open        udp        unknown 
```

The following TCPdump output shows a sample from UDP port scanning. Any port in the scanned range that sparky does not generate an ICMP “port unreachable” message for is assumed to be listening:

```
07:09:08.286810 verbo.62865 > sparky.32787: udp 
07:09:08.286847 verbo.62865 > sparky.32775: udp 
07:09:08.286878 verbo.62865 > sparky.32788: udp 
07:09:08.286924 verbo.62865 > sparky.32789: udp 
07:09:08.286969 verbo.62865 > sparky.32791: udp 
07:09:08.287046 verbo.62865 > sparky.32774: udp 
07:09:08.287094 verbo.62865 > sparky.32781: udp 
07:09:08.287162 verbo.62865 > sparky.32772: udp 
07:09:08.287229 verbo.62865 > sparky.32789: udp 

07:09:08.287793 sparky > verbo: icmp: sparky udp port 32788 unreachable (DF) 
07:09:08.977544 sparky > verbo: icmp: sparky udp port 32791 unreachable (DF) 
07:09:09.657361 sparky > verbo: icmp: sparky udp port 32781 unreachable (DF) 
07:09:10.157301 sparky > verbo: icmp: sparky udp port 32787 unreachable (DF) 
07:09:10.817315 sparky > verbo: icmp: sparky udp port 32789 unreachable (DF) 
```

## UDP Length Field

The UDP length is the number of bytes found in the UDP header plus the number of bytes found in the UDP payload. The UDP header is 8 bytes so the minimum length for the UDP length is 8 bytes. The maximum theoretical byte length of an IP datagram is 65535. Given this, and that the IP header is a minimum of 20 bytes long, the theoretical maximum UDP length value is 65515.

Many UDP applications limit the length of the UDP datagram to 8192 bytes, although we saw where DNS limited the DNS payload to 512 bytes. Also, the TCP/IP stack of a given operating system as implemented in the kernel might limit the length of the UDP datagram.

# ICMP

ICMP is another protocol that is fairly simple as far as the fields found in the header. Like UDP, ICMP does not guarantee delivery of the message, so its structure and fields are straightforward. ICMP fields will be examined in terms of normal and malicious use.

## Type and Code

Remember that ICMP has no ports. There must be a method indicating what type of ICMP message is being sent or received. The first two bytes of the ICMP message are the ICMP message type and code, respectively. The message code is a subcategory under the message type.

For instance, there are two possible message codes for a message type of 11, which represents the time exceeded category. If the message code is 0, it is a “time exceeded in-transit” message. If the message code is 1, it is an IP “reassembly time exceeded” message.Valid values of ICMP message types and codes are found at [www.iana.org/assignments/icmp-parameters](http://www.iana.org/assignments/icmp-parameters).

## Identification and Sequence Numbers

If you examine some ICMP requests such as the echo request, you’ll find some additional fields in the ICMP header. These are the ICMP identifier found in bytes 4 and 5 offset of the ICMP header and the ICMP sequence number found in bytes 6 and 7 offset of the ICMP header.

These fields are used in an echo request/echo reply pair to uniquely identify requests and match them with responses. For UNIX hosts, the ICMP ID is typically the process ID of the ping that generated the traffic. There can be several simultaneous ping commands so the identifier in both the echo request and echo reply informs the pinging host what reply is connected with what request. Each ping can generate several echo requests and the sequence number is the manner in which they are tracked in order to see if there are missing packets. Here is the output from a ping request that demonstrates the change in ICMP sequence numbers.

```
PING sparky (1.1.1.100) from 1.1.1.5 : 56(84) bytes of data. 

64 bytes from 1.1.1.100: icmp_seq=0 ttl=255 time=0.8 ms 
64 bytes from 1.1.1.100: icmp_seq=1 ttl=255 time=0.9 ms 
64 bytes from 1.1.1.100: icmp_seq=2 ttl=255 time=7.3 ms 

16:33:07.400700 verbo > sparky: icmp: echo request 

4500 0054 038d 0000 4001 bed1 0101 0105 
0101 0164 0800 9e12 c402 0000 0391 8439 
1d1d 0600 0809 0a0b 0c0d 0e0f 1011 1213 

1415 1617 181916:33:07.401479 sparky > verbo: icmp: echo reply (DF) 

4500 0054 7146 4000 ff01 5217 010018f64 
010018f05 0000 a612 c402 0000 0391 8439 
1d1d 0600 0809 0a0b 0c0d 0e0f 1011 1213 
1415 1617 1819 
```

Let’s examine the ICMP identifier and sequence numbers in the context of the previous output’s ping. We ping host sparky from verbo and see from the output that the sequence number begins at 0 and increments for each new echo request sent out. In this case, the ping process was aborted after the third echo request.

If you examine the hex dump, you’ll see that the identifier is a hex c402 or decimal 50178. Because the pinging host is a Linux host, we assume this is the process ID of the ping. This value will remain static for all echo requests and replies associated with this ping. The sequence number, on the other hand, will increase by 1 for each new echo request sent and will be cloned in the associated echo reply. Had all the echo requests and replies associated with this ping process been displayed, we’d see four additional records, two echo requests, and two echo replies. The identifier would be the same for all, but the sequence number would be 1 for the second set of echo requests and replies, and it would be 2 for the third set.

### Misuse of ICMP Identification and Sequence Numbers

Because the ICMP identifier and sequence number fields were not likely to receive careful scrutiny in the past, they were chosen to signal exploit traffic to the receiving host. In the case of the a DDoS known as Stacheldraht, the ICMP identifier value of 667 was used to initiate connections between handler and agent hosts in an ICMP echo reply. The ICMP identifier value of 666 was used to respond from agent to handler with another ICMP echo reply. In Tribe Flood Network, an ICMP identifier value of 456 was used to initiate a connection between client and daemon and a value of 123 was used to respond—both using ICMP echo replies too. Finally, Loki of many years ago had a static hex value of 0xf001 or 0x01f0 in the ICMP sequence number.

These are all valid values for those fields so tuning a NIDS to look solely for those values in those fields might generate some false positives. It is best to examine these packets statefully in the context in which they occurred.

# Summary

As we wind up our two-chapter scrutiny of header fields in the IP datagram, we finish our examination of the embedded protocol fields. By far, TCP is the busiest of the protocol headers because of all of the fields required to maintain reliability, state, order, and data flow control. As you would imagine, the initial values selected for some of these fields provide a wealth of information for nmap operating system fingerprinting scans. As well, some of the fields can be used for invasion or insertion attacks as we saw demonstrated with the TCP checksum example in the previous chapter.

UDP and ICMP header fields are uncomplicated in purpose. Still, UDP ports can be scanned using nmap by searching for ports for which no ICMP “port unreachable” message is returned. ICMP messages can provide reconnaissance when allowed to leave the network, and nmap makes use of examining the embedded messages after the ICMP header to identify remote operating systems. Finally, the ICMP identification and sequence numbers have been used for stealthy purposes in DDoS attacks or covert protocol exchanges.
