# Chapter 5. Stimulus and Response

![Stimulus and Response](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

Up until this chapter, you have been exposed to mostly stimulus activity. Not much time or discussion has been invested presenting the unique responses from different stimuli. This served you well when new theories and concepts were introduced so as not to add layers of complexity to new material. Hopefully, now that you understand the basic theory, you are ready to diversify your exposure.

Most current network intrusion detection systems have very high rates of false positives. In other words, they cannot yet make wise decisions on whether traffic coming across a given network is harmful or innocuous. So, the network intrusion-detection system (NIDS) often errs on the side of caution, and alarms when there is no problem. There are many reasons for this, but the short explanation is that most times the signatures or rule set that the NIDS uses to determine suspicious traffic are too generic. If these signatures cannot be or are not more precisely customized, the NIDS will often alert when no problem exists.

Therefore, the analyst must make the distinction between false positive and valid alarms. You examine the traffic associated with the alarm and determine whether it is a false alarm. To make such a determination, you need to have a foundation in what seemingly normal or abnormal traffic looks like. Common sense dictates that all aspects of standard stimuli and responses cannot be covered in this chapter. The intention is to impart some general knowledge, however, so that you can make a more intelligent determination of the kind of traffic you observe on different networks.

This chapter first exposes you to the expected behavior of typical applications and protocols. Next, you learn about a category of activity that manifests expected, yet uncommon behavior. Finally, you descend from the sublime to the ridiculously abnormal activity.

This is much like the evolution of a budding courtship. Both partners are on their best behavior at first because good manners are expected. The comfort zone seeps in after awhile, and the expected fine etiquette deteriorates from furled pinkies while drinking tea to random slurps. Familiarity certainly breeds bad manners as time passes and the first hardy belch rumbles.

**The Personal Hazards of Working with False Positives**

Several months ago, I was driving to work when I saw a simultaneous red flash of both the battery and brake indicator lights appear on the dashboard of my car. They disappeared immediately, but it concerned me. This happened several more times on the remainder of the commute.

I am the first to admit that I am a mechanical moron and should never question anything my car professes to tell me because it is far smarter than I am about its health. Yet, it seemed strange to me that these seemingly unrelated lights flashed together. After all, unless I had battery-powered brakes (and I was almost certain I didn’t), there was no logical correlation in my mechanically challenged mind of the two different lights. I tried to explain it away as a false positive convincing myself that perhaps a loose wire of some sort was the culprit instead of real mechanical problems.

Some time passed and the problem got worse, so I gave in and called the service shop. I told the service manager about the problem and her response told me she was doing her very best not to yell, “You moron! “ into the phone. Despite her training in customer relations, she could barely contain her rage at my stupidity. She told me that it was my car’s alternator and I could be stranded— or some other catastrophic things could happen like the car could blow up, or I could put an eye out, yadayadayada. Needless to say after hearing the “sky-is-falling” prognosis of my car and my life, I brought the car in to be repaired right away, and the problem went away.

I got to thinking about the incident and began to reflect that I had been a relatively conservative and cautious person most of my life who, years ago, would have taken the car into the shop at the first sign of trouble. What had changed in all these years? My only guess is that I’m so used to looking at NIDS outputs of false positives that I try to explain everything away in that same light. In other words, I believe nothing any more because everyone and everything is a liar!

# The Expected

What the heck is normal traffic anyway? It would be an exercise in futility— and undoubted head-bobbing boredom—to try to demonstrate all aspects of normal behavior. To make this a more manageable and interesting task, this section reviews situations and traffic patterns that are likely to be the bulk of what you will see on your network. Specifically, the response behaviors of hosts and routers are examined when different traffic is sent and received under different conditions with different protocols.

A very hard challenge in developing this material was trying to elucidate what is “normal.” Because expected behavior entails so many facets and dimensions, it is impossible to discuss them all here. Ironically, normal might best be described as not abnormal. For this reason, this book discusses many examples of deviant behavior.

## Request for Comments

Is there some kind of standard baseline for what is expected? Request for Comments (RFCs) contain the foundation documentation for the Internet. They elaborate the expected standards for individual protocols. The Internet is best viewed as a series of different protocols, each documented by one or more RFCs. RFCs do not change after they are issued; protocol enhancements are documented by issuing new RFCs. Some of the most pertinent RFCs for this section include the following:

- ****RFC 793.****This RFC discusses the Transmission Control Protocol (TCP), describing the functions to be performed by TCP, the program that implements it, and its interface to programs or users requiring its services.
- ****RFC 768.****This RFC discusses the functioning of the User Datagram Protocol (UDP), which is an unreliable connectionless protocol.
- ****RFC 791.****This RFC discusses the Internet Protocol (IP), the protocol that provides for transmitting blocks of data called datagrams from sources to destinations.
- ****RFC 792.****This RFC discusses the Internet Control Message Protocol (ICMP), the protocol that deals with errors in datagram processing.

You can find more information about RFCs at [www.rfc-editor.org](http://www.rfc-editor.org).

## TCP Stimulus-Response

This section examines responses to an attempted telnet connection made under various conditions such as a host that doesn’t listen on the telnet port or a router blocking the connection. Telnet is used as a representative TCP application. You will see some of the varied responses to the identical stimulus. Obviously, this is not an exhaustive list of all conditions that might be encountered with an attempted telnet connection. The particular set of conditions has been selected for illustration because it represents some of the most common.

### Destination Host Listens on Requested Port

A host, tel_client.com, attempts to telnet to myhost.com, which listens on port telnet (TCP port 23).

Stimulus:

```
tel_client.com.38060 > myhost.com.telnet: S 3774957990:3774957990(0) win 8760 
<mss 1460> (DF) 
```

myhost.com offers telnet and connection is permitted.

Response:

```
myhost.com.telnet > tel_client.com.38060: S 2009600000:2009600000(0) ack 
3774957991 win 1024 <mss 1460> 
```

The previous TCPdump output examines the expected response when client host tel_client.com attempts to connect to the telnet port on destination host myhost.com. You have already been exposed to the concept of the three-way handshake for TCP session establishment. If you remember, the first part of the process is for the client to initiate a TCP connection with the SYN flag set to the server to signal the desire to connect. tel_client.com issues such a SYN connection request to myhost.com to connect to the telnet port.

Now, if myhost.com offers telnet, access is permitted, and no other impediments arise; you see the expected response of myhost.com replying to the request with a SYN/ACK. This says that myhost.com is listening at the telnet port and can establish this telnet connection. The final part of the three-way handshake not shown would be tel_client.com responding to myhost.com with a TCP connection with only the ACK flag set.

### Destination Host Not Listening on Requested Port

Look at the following TCPdump output to see the response from the same attempted telnet connection. This time, the scenario changes and myhost.com does not listen for telnet connections. The expected response is a RESET/ACK that is an abrupt termination to the connection.

Stimulus:

```
tel_client.com.38060 > myhost.com.telnet: S 3774957990:3774957990(0) win 8760 
<mss 1460> (DF) 
```

myhost.com does not offer telnet.

Response:

```
myhost.com.telnet > tel_client.com.38060: R 0:0(0) ack 3774957991 win 0 
```

In the response, you see that the ACK number 3774957991 from myhost.com is one more than the tel_client.com’s SYN of 3774957990. This means that myhost.com received the telnet attempt, and this would be the expected sequence number of the next data byte.Yet, the R in the response indicates a connection RESET or termination because myhost.com does not listen on port telnet. After the RESET/ACK is issued by myhost.com, there should be no reply from tel_client.com.

### Destination Host Doesn’t Exist

What happens if tel_client.com attempts a telnet connection to myhost.com, but myhost.com doesn’t exist? Looking at the following TCPdump output, you see an example of such an exchange. Often a router responds to a situation such as this in which a host cannot respond. In this case, router.com, the default router for the subnet on which myhost.com was formerly found, informs tel_client.com using ICMP that myhost.com is unreachable.

Stimulus:

```
tel_client.com.38060 > myhost.com.telnet: S 3774957990:3774957990(0) win 8760 
<mss 1460> (DF) 
```

myhost.com doesn’t exist.

Response:

```
router.com > tel_client.com: icmp: host myhost.com unreachable 
```

This implies that myhost.com is a host with a registered domain name system (DNS) IP address, but the IP number is no longer active or the host is currently down or suffering from some kind of misconfiguration preventing it from responding. The response from router.com informs of this unreachable error condition using ICMP as the protocol to deliver the message to tel_client.com.

### Destination Port Blocked

The next TCPdump output shows another possible condition. What if a filtering router blocks the telnet port? What kind of response will you see? Again, the router for myhost.com, router.com, informs tel_client.com that myhost.com is unreachable and qualifies that this is because of an `admin pro``hibited filter`, meaning that the access was blocked. router.com was just trying to be helpful and informative in this and the previous situations examined, but it is giving out some valuable reconnaissance information if someone is probing your network. It is possible to silence Cisco routers by putting a `no ip` `unreachables` statement in the access control list of the appropriate interface as you learned in [Chapter 4](ch04.html), “ICMP.” This prevents the router from being as verbose and limits the information that it divulges.

Stimulus:

```
tel_client.com.38060 > myhost.com.telnet: S 3774957990:3774957990(0) win 8760 
<mss 1460> (DF) 
```

Router responds to blocked telnet request.

Response:

```
router.com > tel_client.com: icmp: myhost.com unreachable - admin prohibited 
filter 
```

### Destination Port Blocked, Router Doesn’t Respond

This TCPdump output illustrates what happens when a router blocks traffic, but the router has been muzzled from issuing unreachable messages. Because no ICMP error message informs tel_client.com that something is amiss, it stubbornly continues to send retries to connect. The number of retries and the time intervals in which they are sent are based on the TCP/IP stack of the operating system of the host sending the retries. Finally, the host tel_client.com gives up on the connection after it has exhausted the maximum number of retries.

Stimulus:

```
17:14:18.726864 tel_client.com.38060 > myhost.com.telnet: S 
3774957990:3774957990(0) win 8760 <mss 1460> (DF) 
```

Router does not respond to blocked telnet request.

Response:

```
17:14:21.781140 tel_client.com.38060 > myhost.com.telnet: S 
3774957990:3774957990(0) win 8760 <mss 1460> (DF) 
17:14:27.776662 tel_client.com.38060 > myhost.com.telnet: S 
3774957990:3774957990(0) win 8760 <mss 1460> (DF) 
17:14:39.775929 tel_client.com.38060 > myhost.com.telnet: S 
3774957990:3774957990(0) win 8760 <mss 1460> (DF) 
```

The topic of retries or retransmissions will be examined in greater detail in [Chapter 9](ch09.html), “Examining Embedded Protocol Header Fields.”

## UDP Stimulus-Response

A DNS query is used in this section to examine how UDP responds to different stimuli. Specifically, a listening domain port and a nonlistening port are inspected. Because the other stimuli examined in the previous section for TCP (such as a host that doesn’t exist or the domain port blocked at the router) elicit very similar responses for the UDP DNS query, they don’t merit repetition.

### Destination Host Listening on Requested Port

Looking at the following example, you see nslookup.com does a DNS query to myhost.com on a port domain from the preceding TCPdump output. [Chapter 6](ch06.html), “DNS,” explains the TCPdump DNS output more thoroughly. You see a DNS identification number, 51007, which is used to pair up responses with requests. myhost.com receives the query and responds. myhost.com communicates on port domain (53) to nslookup.com, responding to DNS identification number 51007. The 1/0/0 is TCPdump DNS jargon for returning one answer resource record, no authority records, and no other records. As with TCP, you see that the UDP exchange was done using an ephemeral port, 45070, on the client and the well-known domain server port. The response from myhost.com uses these established ports.

Stimulus:

```
nslookup.com.45070 > myhost.com.domain: 51007+ (31) (DF) 
```

myhost.com runs the domain service and responds.

Response:

```
myhost.com.domain > nslookup.com.45070 51007 1/0/0 (193) (DF) 
```

### Destination Host Not Listening on Requested Port

Observe the following TCPdump output. In this case, myhost.com responds with an ICMP message that UDP port domain is unreachable. Again, this produces some good reconnaissance about what services a target host does or does not offer. This time it is a loose-lipped host, not a router that offers more detail than necessary.

Stimulus:

```
nslookup.com.45070 > myhost.com.domain: 51007+ (31) (DF) 
```

myhost.com doesn’t run the domain service and responds.

Response:

```
myhost.com > nslookup.com: icmp:myhost.com udp port domain unreachable 
```

In [Chapter 9](ch09.html), you will learn that nmap can scan for listening UDP ports. It attempts to do this by assuming that scanned target host UDP ports for which no ICMP “port unreachable” messages are returned are listening ports. This is sometimes referred to as inverse mapping because there is no direct indication that the ports are listening.

Unlike listening TCP ports that respond at the TCP protocol level with a SYN/ACK, most UDP ports will not respond at the UDP protocol level with a simple connection request. For instance, the previous DNS query to UDP port 53 received a response because it was communicating at the levels above the protocol level such as the application level. If you were to examine the embedded payload, you would find a properly configured DNS query. The nmap UDP port scanning sends 0 bytes of payload and therefore cannot communicate above the protocol level.

## ICMP Stimulus-Response

ICMP, as you have learned, differs from TCP and UDP. Naturally, the expected set of responses differs as well. This very brief summary explains ICMP’s uniqueness:

- ICMP doesn’t use protocol ports to converse.
- ICMP can be a one-way transmission to inform of an error condition with no observed response.
- ICMP can be a request with an expected reply.

The error responses that might be encountered using ICMP are typically availability issues, such as if the host exists or whether access is allowed to the host. These are similar to those observed with the TCP examples. Rather than rehash more of the same, the Windows **tracert** command is introduced to demonstrate normal ICMP response used to discover a route from a source to destination host.

### Windows tracert

The **tracert** command uses the ICMP echo request and ICMP echo reply pair, also known as ping, to discover the routers through which a datagram passes on its path from source to destination host. The command output looks like this:

```
tracert target.my.com 
Tracing route to target.my.com [1.2.3.4] 
over a maximum of 30 hops: 
  1   129 ms   126 ms   130 ms  router.my.com [1.2.3.1] 
  2   229 ms   124 ms   118 ms  target.my.com [1.2.3.4] 
  Trace complete. 
```

When you execute the **tracert** command, you see the intermediate routers through which the ICMP echo request passes. This example shows only one, router.my.com, before reaching the destination host target.my.com.

Each router and the destination host receive three separate ICMP echo requests, and **tracert** output displays the round-trip time for each of those datagrams to reach the router or destination host. For instance, the first three ICMP echo requests sent to router.my.com took 129, 126, and 130 milliseconds to complete the round-trip with an ICMP echo response. The multiple iterations to one router or host are done in case one or more ICMP echo requests or replies is dropped or lost because of network problems. Next, target.my.com receives three ICMP echo requests and replies with three ICMP echo replies.

### TCPdump of tracert

This following TCPdump output is the result of executing the previous **tracert** command:

```
tracer.net > target.my.com: icmp: echo request [ttl 1] 
router.my.com > tracer.net: icmp: time exceeded in-transit 
tracer.net > target.my.com: icmp: echo request [ttl 1] 
router.my.com > tracer.net: icmp: time exceeded in-transit 
tracer.net > target.my.com: icmp: echo request [ttl 1] 
router.my.com > tracer.net: icmp: time exceeded in-transit 
tracer.net > target.my.com: icmp: echo request 
target.my.com > tracer.net: icmp: echo reply (DF) 
tracer.net > target.my.com: icmp: echo request 
target.my.com > tracer.net: icmp: echo reply (DF) 
tracer.net > target.my.com: icmp: echo request 
target.my.com > tracer.net: icmp: echo reply (DF) 
```

**tracert** sends the first ICMP echo request in an IP datagram with a time-to-live (TTL) value of 1. The TTL is a value set by a sending host and decremented by each network device through which the packet traverses. TTL provides a means of discarding packets that have overstayed their welcome on the Internet and might be bouncing aimlessly. If a router decrements the TTL and the value becomes 0, the packet must be discarded and an ICMP “time exceeded in-transit” error message is returned.

In the previous output, after a TTL with a value of 1 is observed, the router router.my.com sends an ICMP “time-exceeded in-transit” message. This is because it decremented the TTL and discovered a value of 0. It must then discard the packet and inform the sending host.

When used for **tracert**, however, the original source host receiving this ICMP error message records the router from which it came. If necessary, **tracert** then sends another ICMP echo request in an IP datagram, but increments the TTL value by 1. This process repeats until the ICMP echo request finally makes its way to the destination host and receives an ICMP echo reply.

By default, three different ICMP requests are sent to each new hop for redundancy in case a packet is dropped. Notice that tracer.net sends an ICMP echo request to target.my.com. Immediately, you see the reply from router.my.com complaining via the ICMP “time exceeded in-transit” message that the TTL value has been decremented to 0. This is seen for all three different ICMP echo requests. The host tracer.net then increments the TTL to 2, which is enough to allow it to get to the actual destination host, target.my.com. The reason that you do not see TCPdump display the TTL value of 2 is because the default behavior of TCPdump is to print the TTL only when it has a value of 1 to warn of an impending problem. target.my.com responds to all the ICMP echo requests with echo replies. If you want to examine the TTL regardless of value using TCPdump, use the command line option **–vv**.

# Protocol Benders

Between the expected and abnormal falls a netherland of applications that exhibit normal, yet unconventional, behavior. These applications deviate from the expected behavior because they were designed differently. These patterns are presented so that if you encounter them, you will understand that this is normal traffic.

Specifically, FTP and UNIX Traceroute will be discussed. FTP is considered to be a protocol bender because it defies the convention of using one ephemeral and one server port for the duration of the FTP connection. The UNIX Traceroute is an unusual application because it combines ICMP and UDP to navigate from source to destination and record all routers on the way.

## FTP

The expected behavior of TCP that you have witnessed so far is to establish the two ports used by the client and server during the three-way handshake. The client usually selects an ephemeral port greater than 1023, and the server listens on a well-known port. Throughout the remainder of the established TCP session, the client and server talk only on these established ports. FTP differs from most other TCP services, because it communicates using two different server ports. The first port is port 21, which is known as the standard FTP command port. The second port is used for data passed between the client and the server. The actual port used is different for active and passive FTP, as you will soon see.

## Active FTP

Active FTP is so named because the FTP server opens up the data connection to the client. Both active and passive FTP use port 21 to issue FTP commands, such as those to retrieve or store a file. But, in active FTP, the second is port 20 for FTP data passed between the client and the server. The FTP data port is used to exchange a file between the two hosts or to send a listing of file directories from the server to the client.

Look at the following TCPdump output for an active FTP session to see an unusual, but normal, change of TCP ports:

Session negotiation:

```
ftp.client.com.35955 > ftp.server.com. 21: S 1884312222:1884312222(0) 
ftp.server.com.21 > ftp.client.com.35955: S 3113925437:3113925437(0) ack 
1884312223 
ftp.client.com.35955 > ftp.server.com.21: . ack 1 
ftp.server.com.21 > ftp.client.com.35955: P 1:24(23) ack 1 
ftp.client.com.35955 > ftp.server.com.21: . ack 24 
```

**dir** command issued by the user:

```
ftp.server.com.20 > ftp.client.com.35956: S 3558632705:3558632705(0) 
ftp.client.com.35956 > ftp.server.com.20: S 1901007864:1901007864(0) ack 
3558632706 
ftp.server.com.20 > ftp.client.com.35956: . ack 1 
```

In the preceding example, the FTP connection is established between ftp.client.com using ephemeral port 35955 and server port 21. The three-way handshake is completed and some data (usually a welcoming message) is passed between the two. This is similar to what you have witnessed with other TCP protocols.

Next, the user issues the FTP **dir** command from the client requesting a listing of the directories on the server. A new connection is established from source port 20 of the server to the ephemeral port 35956 on the client. Although you do not see it in the output, the client informed the server that it would be listening on ephemeral port 35956 via the FTP **port** command. After this new three-way handshake is completed, ftp.server.com can send the directories to ftp.client.com on this established connection. Additional exchanges of data cause the establishment of new connections and the selection of new ephemeral ports. This is called active FTP because the FTP server initiates the data connection to the client. As you might guess, this presents some problems for packet-filtering devices that would have to indiscriminately allow traffic into the network coming from source port 20. Passive FTP avoids these problems by having the internal FTP client make the data connection.

### Passive FTP

Passive FTP differs from active FTP in the manner in which the data connection is established. It uses the identical method of connecting to FTP port 21 to establish the command port. But, as you observed with active FTP, the problem arises when a packet-filtering device must allow initial SYNs in from source port 20 to a high-numbered port inside the packet-filtering device. What is to keep a hacker from using this hole as a way into the network? After all, the packet-filtering device might not be examining the content of the packet using this hole and cannot be sure it is indeed FTP traffic.

Passive FTP avoids this problem altogether by having the client initiate the connection to the server. Remember that active FTP required that the server initiate the connection to the client. Look at the following output of a passive FTP session establishment:

Session negotiation:

```
ftp.client.com.44890 > ftp.server2.com.21: S 4276284026:4276284026(0) win 
8760 <mss 1380> (DF) 
ftp.server2.com.21 > ftp.client.com.44890: S 1669630260:1669630260(0) ack 
4276284027 win 8280 <mss 1460> (DF) 
ftp.client.com.44890 > ftp.server2.com.21: . ack 1 win 9660 (DF) 
```

**dir** command issued by the user:

```
ftp.client.com.44891 > ftp.server2.com.3967: S 4282611109:4282611109(0) win 
8760 <mss 1380> (DF) 
ftp.server2.com.3967 > ftp.client.com.44891: S 1669768808:1669768808(0) ack 
4282611110 win 8280 <mss 1460> (DF) 
ftp.client.com.44891 > ftp.server2.com.3967: . ack 1 win 9660 (DF) 
```

When ftp.client.com issues the **dir** command on the current command connection, it causes a data connection to be established. You don’t see this in the TCPdump output, but ftp.server2.com informs the client via the FTP port command that it will be listening on port 3967. The client issues the SYN connection to that port and the server responds with a SYN/ACK. The directory listing is done via this connection. Because the client is making an outbound connection to the server, the subsequent responses from the server can be allowed back in the packet-filtering device with relatively strong confidence that this is a “safe” connection. This involves less risk than allowing active FTP connections by permitting all inbound source port 20 through the packet-filtering device.

## UNIX Traceroute

The UNIX Traceroute program discussed next shows a combination of UDP and ICMP to discover the path that a datagram takes from source to destination. This traceroute program is similar in function to the Windows Tracert; instead of using ICMP to discover the routers and destination host, however, it uses UDP.

The intermediate routers that are discovered respond as you saw in the Windows Tracert with ICMP “time-exceeded in-transit” messages when an IP datagram has a TTL value decremented to 0. Again, this process is repeated until the UDP datagram makes its way to the destination host by incrementing the starting TTL value by 1 for each new hop to be forged beyond the previous one. The UDP destination port chosen is one typically in the 33000–33999 range—one that almost surely does not listen. The intention is to elicit an ICMP “UDP port unreachable” message that signals to traceroute that the destination host has been found. Like tracert, the default behavior for traceroute is to send three different connections to each router or host. This example alters the behavior to send only one for simplicity:

```
tracer.com.62615 > target.com.33456: udp 12 (DF) [ttl 1] 
router.com > tracer.com: icmp: time exceeded in-transit 
[tos 0xc0] 
tracer.com.62615 > target.com.33457: udp 12 (DF) 
target.com > tracer.com: icmp: target.com udp port 33457 unreachable (DF) 
```

In the preceding output, you see tracer.com send a UDP datagram to destination port 33456 of target.com. The initial TTL value is set to 1. As soon as this packet hits router.com, it decrements the TTL value to 0 and returns an ICMP “time exceeded in transit” message to tracer.com. When tracer.com receives this, it sends another UDP datagram to target.com. This is different from the first one because it increments the destination port to 33457 and, while you cannot tell from the standard TCPdump output, it increments the initial TTL to 2. This allows the datagram to traverse the first router, router.com, and take one more hop. That additional hop takes it to the destination host target.com that does not listen on port 33457 and returns an ICMP “port unreachable” message.

You should be aware that both the UNIX traceroute and the Windows tracert only work if specific ICMP messages are allowed into the network of the host executing the commands. Both versions require that ICMP “time exceeded in-transit” messages be allowed into the network. The UNIX traceroute requires that ICMP “port unreachable” messages be allowed, and Windows tracert requires that ICMP echo requests be allowed.

You are probably asking whether these types of ICMP messages should be permitted inbound to your network. This really depends on the security posture you adopt. At the most protected and restricted sites, this is not necessarily recommended. The risks might far outweigh the benefits because it is possible to use these ICMP messages for purposes other than the ones for which they were designed, as was witnessed with the discussion of Loki in [Chapter 4](ch04.html).

However, if your site is a more open one and you are willing to accept the risks, allowing these ICMP messages can provide some obvious benefits of route discovery along with informative feedback to internal hosts in your network.

## Summary of Expected Behavior and Protocol Benders

Here is a brief synopsis of what has been covered so far in this chapter. The RFCs are the standards documents upon which TCP/IP and the Internet were built. They describe how things are supposed to work when everyone conforms to the same rules. Unfortunately, hackers have discovered that different implementations of TCP/IP react differently to deliberate violations of the RFC standards. That’s one of the foundations of hacking: deliberately exploiting exceptional conditions that the implementers of the TCP/IP code believed would never happen. Hackers often attempt to identify operating systems by sending strange stimuli and observing the host’s responses. The final part of this chapter looks at some of the reactions of systems to these deliberate deviations.

As previously discussed, there are unique responses for the same stimulus depending on the circumstances and availability of the requested service. Responses also depend on a host or router’s capability to respond to a particular connection. Each of the different protocols has different expected responses. Finally, you see in protocol benders some unusual, but not abnormal, behavior exhibited by some applications.

# Abnormal Stimuli

This section examines some of the blatantly anomalous behaviors that hackers might throw your way. These behaviors have many purposes, and each is examined for the different categories discussed. These categories and anomalies are not all-inclusive; you might find many more.

## Evasion Stimulus, Lack of Response

You see a port scan of victim.org from stealthy.com with the FIN flag alone set in the TCPdump output that follows. This is a sneaky way of determining whether a given port is active. The expected behavior per RFC 793 is that a listening port that is scanned should not respond; a port that is not listening should respond with a RESET/ACK. This maps the services that a target host offers. Take a look:

```
stealthy.com.50141 > victim.org.5: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.3: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.26: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.45: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.17: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.7: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.51: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.52: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.30: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.53: F 0:0(0) win 4096 (DF) 
stealthy.com.50141 > victim.org.20: F 0:0(0) win 4096 (DF) 
```

The reason that this scan is considered more stealthy than a scan that probes ports with an attempted SYN connection is that some intrusion detection systems might not pick up a FIN scan. Historically, probes of open ports were done using SYN scans, and earlier intrusion detection systems were developed using this signature. When the hackers realized that their scans were being detected, however, they tried to elude notice by launching FIN scans that would map the active ports but might not be noticed. This scan can be launched using **nmap –sF victim.org** to inform nmap to do a stealthy FIN scan.

## Evil Stimulus, Fatal Response

Denial-of-service (DoS) attacks might attempt to starve a host of resources needed to function correctly. There are many different varieties of DoS attacks. Jolt2 is an attack that consumes so much of the target host’s memory resources that it cannot function. Here is some sample output from Jolt2:

```
10:48:56.848099 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848099 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848295 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848295 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848351 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848351 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848420 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848420 verbo.com > win98.com: (frag 1109:9@65520) 
10:48:56.848584 verbo.com > win98.com: (frag 1109:9@65520) 
```

Jolt2 sends an endless stream of ICMP echo requests (by default, although other protocols can be used) to a target Windows host. These are sent as fragments with the same fragment ID but also with duplicate non-zero fragment offsets.

Because all fragments but the first in the fragment train carry only data, not protocol headers, the receiving host only knows the embedded protocol is ICMP. A problem exists for certain Windows 98, Windows NT, and Windows 2000 hosts when they do not receive the initial 0 offset fragment. The target host becomes consumed with packet reassembly, and memory usage shoots way up leading to a DoS.

When looking at the TCPdump output of the Jolt2 activity, all you know is that host verbo.com is sending some kind of packets to the win98.com host. You see a repeated fragment ID of 1109, a fragment length of 9, and a fragment offset of 65520. The Jolt2 source code assigns the fragment offset a static value of 65520. This brings the total close to the 65535 maximum. Initially, you might think this worked because of the fragment offset number. However, when this value was changed in the source code to something quite a bit lower and the code was recompiled, the DoS still occurred.

To test the response of the target host, a ping process was executed on the malicious host verbo.com to win98.com before and during the time the Jolt2 code was run. The DoS was almost immediate after the Jolt2 code was executed. The win98.com host neither responded to pings nor keyboard input. It recovered after the attack was stopped and did not require rebooting.

**The Motivation Behind Scanning**

One of the first phases in any attempt to break into a host on a network is to do some kind of reconnaissance on the network or a particular host. An attacker might have a new piece of code that was just released that enables him to get root access if he can find a vulnerable host. Or, an attacker might just be interested in getting into a host or multiple hosts in any way possible. Different hackers have different goals for hacking. Perhaps the host or network is being sought to participate in a distributed denial-of-service attack. Or, perhaps the interest is in compromising a host from which to launch other attacks and hide the true identity of the hacker.

The attacker must scan the network in some fashion to discover live hosts, and later discover hosts susceptible to exploits by scanning service ports. For instance, the attacker might have acquired some software that could gain root access on hosts offering vulnerable DNS servers. Chances are good that he would scan the network for any host listening on the DNS port. After discovering those, the attacker might try to execute the DNS exploit code on hosts running DNS.

The scanning phase is one that might be done blatantly at night when it is less likely that a network is being watched. It might be done from a compromised host so that when it is discovered, the attacker’s identity will not be known. Or, the hacker might try to launch the scans using methods that might go undetected, known as stealth scans. These scans are considered more furtive because they use unconventional techniques that NIDS are not likely to pick up. Some of the scanning techniques also attempt to fingerprint the operating system. Many times a given exploit might plague a subset of operating systems. For the hacker to have a better chance of success, reconnaissance must be done to find hosts running a particular operating system.

## No Stimulus, All Response

This is really just a fancy name for IP spoofing. [Appendix A](apa.html), “Exploits and Scans to Apply Exploits,” discusses this in more detail. In the following TCPdump output, it appears that many 1.2 hosts are receiving ICMP “time exceeded in-transit” messages. They are being informed that traffic, which they sent to a host, had a TTL expire in a datagram. Naturally enough, this implies that all the 1.2 hosts sent some kind of traffic that elicited these responses. That is not the case, however; no outbound traffic is found from these hosts. Here is the output:

```
router.com > 1.2.10.72: icmp: time exceeded in-transit 
router.com > 1.2.18.13: icmp: time exceeded in-transit 
router.com > 1.2.11.67: icmp: time exceeded in-transit 
router.com > 1.2.16.13: icmp: time exceeded in-transit 
router.com > 1.2.19.1: icmp: time exceeded in-transit 
router.com > 1.2.1.252: icmp: time exceeded in-transit 
router.com > 1.2.13.56: icmp: time exceeded in-transit 
router.com > 1.2.143.6: icmp: time exceeded in-transit 
router.com > 1.2.13.15: icmp: time exceeded in-transit 
```

Can you guess the explanation for this traffic? Given the title of the section, it should be a no-brainer. The 1.2 hosts were spoofed, and traffic was sent to a foreign network using them as a source IP. The reason for this is sheer speculation because you see only one side of the action; however, the most likely explanation is that some kind of flood of activity or harassment against the foreign network was undertaken.

How do you know that source IP router.com is not doing some kind of reconnaissance of the destination 1.2 hosts? Couldn’t this type of traffic elicit some kind of response from a router, if not a host? The problem is that this is an ICMP error message, and RFC 1122 dictates that an ICMP error message cannot elicit another ICMP error message because that might lead to some kind of endless loop when an error condition was encountered. Because no other protocol would respond to this activity, the spoofing theory is the most logical.

**Backscatter**

A very interesting study was conducted and a paper was written about attacks such as the one discussed in the section, “[No Stimulus, All Response](ch05.html#ch05lev2sec11).” The authors nicknamed the attacks *backscatter*. The authors studied activity on their class A network on the Internet over an extended time. They were able to infer backscatter attacks on the Internet by examining different protocol responses for which there were no requests. This indicated that IP addresses from their network were being spoofed. Using this information, they were able to deduce the number and types of attacks that occurred on the Internet during that time. The frequency and types of activity occurring on the Internet are pretty amazing. The study, “Inferring Internet Denial-of-Service Activity,” can be found at [www.cs.ucsd.edu/~savage/papers/UsenixSec01.pdf](http://www.cs.ucsd.edu/~savage/papers/UsenixSec01.pdf).

## Unconventional Stimulus, Operating System Identifying Response

This section discusses some examples of attempts to fingerprint the operating system of a target host by sending unconventional stimuli and then evaluating the target host’s responses. The nmap program is one scanning tool that can remotely attempt to identify a target host’s operating system.

The reason that malicious hackers attempt to identify a host’s operating system is because they can then pair appropriate exploits with vulnerable operating systems. It is potentially damaging reconnaissance information if someone can determine the operating system of a remote host. Sure, some sites are open enough that the operating system type and version can be harvested from banners associated with telnet or FTP connections. These might not be readily available for all sites, however; and even if they are, they might not be accurate. Every operating system has a TCP/IP stack implementation that differs slightly. If a hacker or software can send specific packets, knowing how a particular operating system should respond, the hacker can tell Linux from Solaris, (sometimes) without requiring any other information.

nmap sends some unexpected stimuli, including the following, to identify a host’s operating system based on the replies:

- ****An unsolicited FIN to an open port.****There should be no response according to RFC 793, but some hosts do respond with a RESET. The output was examined in the previous section, “Evasion Stimulus, Lack of Response,” to show how this traffic can be used to map listening ports with more stealth than conventional SYN scans.
- ****Bogus “reserved” TCP flag values.****nmap sends these to see whether the target host resets the bits to 0 for those nonexistent flags. Many operating systems think these bits are bogus; however, those that are ECN-aware might not, as discussed in the following section.
- ****Anomalous TCP flag combinations.****Mutant flag combinations are sent with the expectation that most target hosts will not respond, but a handful might respond, uniquely identifying their operating system.
- ****No TCP flag values.****nmap sends these to see how the target host handles this anomalous situation.

### Bogus “Reserved” TCP Flags

One fingerprinting method is to send bogus TCP flag settings. [Figure 5.1](ch05.html#ch05fig01) shows the configuration of the TCP flag byte. The TCP flag byte contains all the possible TCP flag settings. Remember from [Chapter 2](ch02.html), “Introduction to TCPdump and TCP that the TCP flag settings tell much about the purpose of a given TCP segment. Because there are only six TCP flags, there are 2 extra bits in the TCP flag byte. Before the invention of something known as Explicit Congestion Notification (ECN), these high-order reserved bits were expected to have a value of 0. ECN is discussed more thoroughly in [Chapter 9](ch09.html).

![TCP flag byte.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/05fig01.gif)

**Figure 5.1. TCP flag byte.**

To examine all the bits set in the TCP flag byte, you need to execute the standard version of TCPdump with the -x option that dumps the collected datagram in hexadecimal. You cannot check the value of the 2 high-order bits with standard TCPdump output.

A byte is represented as two hexadecimal characters, or nibbles. The low-order nibble contains the bit settings for the PUSH, RESET, SYN, and FIN flags. Turn your attention to the high-order nibble to examine the value of the reserved bits. The bogus TCP flag settings that nmap tests attempt to give these bits a value. If the high-order nibble has a value greater than 3, this indicates that one or both of the reserved bits are set. You can arrive at this value because the ACK bit when set has a value of 1 times 20 (or 1) and the URG bit when set has a value of 1 times 21 (or 2). These two values combined equal 3. Any value greater than 3 in the high-order nibble is anomalous unless ECN is being used.

The following TCPdump output shows an nmap scan that attempts to discover more about the behavior of the TCP/IP stack of target.com to help identify the operating system. This particular attempted connection set one of the reserved TCP flag bytes—specifically, the bit to the left of the URG bit. First, you see the regular TCPdump output, but it gives no clue to the underlying bogus TCP flag bit settings. The following hexadecimal output shows all fields, including the TCP flag byte field:

```
scanner.com.44388 > target.com.domain: S 403915838:403915838(0) win 4096 
<wscale 10,nop,mss 265,timestamp 1061109567 0,eol> (DF) 

[4500 003c 7542 4000 3b06 15bd 0102 0304 
0102 0305] ad64 0035 1813 443e 0000 0000 
a042 1000 fa4c 0000 0303 0a01 0204 0109 
080a 3f3f 3f3f 0000 0000 0000 
```

Looking at the hexadecimal output, the first 20 bytes of the IP header are in brackets. The TCP header and any data follow this; the 13th byte into the TCP header (marked in bold) is the TCP flag byte. You see that the value is a hexadecimal 42. Looking at the high-order nibble (or the value of 4), it is greater than 3, meaning that the low-order reserved bit has been set. The scanner’s hope is that the response to this bogus flag setting indicates something unique about the operating system.

Now, take a look at the response of target.com to scanner.com. Our interest and nmap’s interest is the response to the bogus TCP flag bit set. Again, the normal TCPdump output display does not show the reserved bits of the TCP flag byte. The hexadecimal dump that does show the TCP flag byte follows this:

```
target.com.domain > scanner.com.44388: S 4154976859:4154976859(0) ack 
403915839 win 8855 <nop,nop,timestamp 16912287 1061109567,nop,wscale 0,mss 
265> (DF) 

[4500 003c e04e 4000 ff06 e6af 83da d684 
83da d683] 0035 ad64 f7a7 ea5b 1813 443f 
a012 2297 fd3f 0000 0101 080a 0102 0f9f 
3f3f 3f3f 0103 0300 0204 0109 
```

Look at the response to the bogus TCP flag bits in the preceding TCPdump output. target.com responds with a SYN/ACK—nothing rancid here. It appears that target.com did not react to the abnormal TCP flag bit set. How do you know? The hexadecimal output of the transaction shows that the response has the SYN and ACK bit set in the TCP flag byte with a hexadecimal value of 12 (in bold). The ACK bit is in the low-order bit of the high-order nibble, so it represents the value 1. The SYN bit is in the low-order nibble, second bit from the left, and represents the 2 value. Therefore, the response discarded the bogus TCP flag bit. Another operating system might have preserved that bit, and it would have been reflected in the TCP flag byte.

## Anomalous TCP Flag Combinations

RFC 793 elaborates normal TCP flag state settings and transitions in extensive detail. It seems likely that most operating system TCP/IP stacks would conform to the specifications. For the most part, they do, but there are the rare exceptions that do not conform and are therefore identifiable by their lack of conformity. Look at the following TCPdump output from an excerpt of traffic produced by running nmap in operating system fingerprinting mode (**-O** command line option) for a host named win98:

```
nmap –O win98 

20:33:16.409759 verbo.47322 > win98.netbios-ssn: SFP 861966446:861966446(0) 
win 3072 urg 0 <wscale 10,nop,mss 265,timestamp 1061109567[|tcp]> 

20:33:16.410387 win98.netbios-ssn > verbo.47322: S 49904150:49904150(0) ack 
861966447 win 8215 <mss 1460> (DF) 
```

The scanning host sends a packet with the TCP flags of SYN, FIN, and PUSH simultaneously set. Logically, it appears that this is an anomalous flag trio because a SYN flag starts a connection, a FIN flag closes a connection, and a PUSH flag sends data after a connection is opened or before a connection is closed. It would seem a natural reaction that a host receiving this connection would ignore it or perhaps RESET it because it makes no sense.Yet, the Windows 98 target host appears to interpret this as session establishment and responds with a SYN and an ACK. This unique reaction helps identify the responding host as having a Windows TCP/IP stack.

### No TCP Flags

As another example of nmap fingerprinting, look at the following TCPdump output. It shows a TCP segment with no TCP flag bits set. This is another instance of sending a mutant TCP flag byte setting. In this case, no flag bits have been turned on; this is also known as a null session:

```
scanner.com.44389 > target.com.domain: . win 4096 <wscale 10,nop,mss 265, 
timestamp 1061109567 0,eol> (DF) 

[4500 003c 7543 4000 3b06 15bc 0102 0304 
0102 0305] ad65 0035 1813 443e 0000 0000 
a000 1000 fa8d 0000 0303 0a01 0204 0109 
080a 3f3f 3f3f 0000 0000 0000 
```

Look at the previous hexadecimal output. The TCP flag byte field, which is in bold, has a value of 00. This means that no TCP flags have been set. Most hosts will not respond to a null session, yet some must, otherwise nmap would have no reason to send this kind of traffic.

A normal TCP flag byte has at least one flag bit set. The host target.com did not respond at all to this null session TCP segment. The lack of response provides some clue about the operating system. Another operating system might distinguish itself by responding differently, perhaps by replying with a RESET.

**Using TCP Options for OS Identification**

Look at the following TCPdump output from an nmap scan with the focus on the bolded TCP options:

```
scanner.com.44388 > target.com.domain: S 403915838:403915838(0)
 win 4096 
<wscale 10,nop,mss 265,timestamp 1061109567 0,eol> (DF) 
target.com.domain > scanner.com.44388: S 4154976859:4154976859(0)
 ack 
403915839 win 8855 <nop,nop,timestamp 16912287 1061109567,nop
,wscale 0,mss 
265> (DF) 
```

One of the other methods that nmap uses to identify a particular operating system is to send many different TCP options. Some operating systems do not support all these options, and the response discards some. Also, some operating systems set different values for some of the TCP options, further differentiating the fingerprint. Unlike the other examples discussed so far, these are not unconventional stimuli, but are mentioned because they help identify the remote operating system.

Finally, different operating systems will store these options in a different order in the TCP header, which is indicated by the order in which TCPdump lists them. All this information can contain a bounty of identifying clues. As you see in the response to the preceding options, the order has been changed and some of the values have been altered (such as the wscale changing from 10 to 0 in the response). Also notice that the nop and eol options are rearranged or disappear in the response. These fields are used to pad TCP options to 4-byte boundaries and might not be needed in the response.

For an in-depth discussion of TCP options, take a look at RFC 1323. Some of the TCP options seen in the TCPdump output are as follows:

- **`-wscale`.**This option allows the TCP window size to increase to a value greater than 65535 bytes. This is typically used to increase throughput of TCP over high-bandwidth, long-delay networks.
- **`-timestamp`.**This option records round-trip time measurements. These measurements are often necessary to optimize throughput based on changes in network conditions.
- **`-nop`.**This option is used to add a 1-byte pad to TCP options. TCP options must fall on 4-byte boundaries; and if they are less than 4 bytes, the nop is used to pad.
- **`-eol`.**This is the end-of-list option used to pad a final byte to a 4-byte boundary.

## Summary of Abnormal Stimuli

You see that there are many variations of abnormal activity. Different types of abnormal activity have different purposes. Some try to evade the vigilant eye of NIDS or circumvent filtering. Others are blatantly hostile because they attempt a denial of service against a target host.

You must also be aware that sometimes what you might perceive to be hostile activity is actually a response from a host responding to your spoofed addresses. Finally, programs, such as nmap, use unique stimuli to elicit responses with identifying characteristics of the target operating system

# Summary

As far as expected responses are concerned, remember there are no absolutes. Not every operating system’s TCP/IP stack is from the same mold shaped by a set of identical defining RFCs. Some operating systems do not follow the RFCs’ expected behavior. This does not necessarily indicate some kind of mutant response. This is more a reflection of a lack of standardization.

There is a very important point to learn from stimulus-response theory. A common knee-jerk reaction from observing traffic that appears to be some kind of scan or repeated activity directed against your network is to jump to the immediate conclusion that you are under attack from the source IP. You are likely to label the source IP as the aggressor. Take a moment and think before you automatically make such an assessment. Granted, many times you will be correct. But, think about the possibility that this was an elicited response. (There might have even been some kind of catalyst to which the alleged aggressor is responding.) For instance, your source IPs might have been spoofed. This concept is easy to assimilate in theory, but hard to remember in practice.

Conversely, when you get some kind of response activity, such as an unsolicited ICMP echo reply, it is very possible that the source host is indeed the aggressor. As discussed in [Chapter 4](ch04.html), the Tribe Flood Network (TFN) attack uses an ICMP echo reply as the communication vehicle between the master and daemons to launch or control a distributed denial of service (DDoS) attack. If you have any doubt about observed activity, the best advice is to examine the entire captured datagram and scrutinize the header fields and payload for anomalies.You have to adopt the attitude that nothing is predictable all the time when you examine network traffic.
