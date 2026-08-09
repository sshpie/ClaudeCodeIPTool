# Chapter 4. ICMP

![ICMP](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

I*nternet Control Message Protocol* (ICMP) was conceived as an innocuous method of reporting error conditions and issuing and responding to simple requests. Perhaps because of its seemingly benign origins, some of the current mutations of ICMP for less-than-upstanding purposes seem all the more outrageous. In its pure state, ICMP is supposed to be a relatively simple and chaste protocol, but it has been altered to act as a conduit for evil purposes. Therefore, it is important to understand how this protocol is used both for its intended purposes and for malicious purposes.

This chapter examines several aspects of ICMP. First, you are introduced to some background about ICMP followed by how ICMP is used to find live hosts on a target network. Next, you learn about both the expected and unexpected uses of ICMP that you might see in your own network. You then put this ICMP theory into action by analyzing some unusual detected ICMP activity. Finally, the discussion focuses on protecting your network by blocking inbound ICMP activity and the accompanying repercussions of doing so.

# ICMP Theory

Before delving into examples of ICMP traffic, let’s flesh out ICMP a little by giving it some foundation and perspective. If you are already familiar with the theory of ICMP, or if the sound of ICMP theory isn’t high on your quiver quotient, you can skip to the section, “[Mapping Techniques](ch04.html#ch04lev1sec2),” and ping away.

## Why Do You Need ICMP?

As you will recall from [Chapter 2](ch02.html), “Introduction to TCPdump and TCP,” TCP is a connection-oriented protocol with lots of overhead involved in ensuring reliable delivery. *User Datagram Protocol* (UDP) is a connectionless protocol that doesn’t promise reliable delivery. Both UDP and TCP require a server port with which a client can communicate.

A simple request such as determining whether a host is alive, commonly known as ping, doesn’t need ports to communicate and doesn’t require reliable delivery. This request and several more use ICMP to deliver and respond to such traffic.

In addition, what if some kind of error condition is discovered by a router or a host, and that router or host needs to inform a sending source host of the problem? Because TCP is a more robust protocol, it handles some error conditions such as a nonlistening port by sending back a TCP response with the TCP flags of RESET/ACK set. If a TCP client or server receives too much information, it also has a mechanism to close down the receiving buffer by setting a window size of 0. This indicates that the receiving host cannot accept any more data until the current buffered data is processed.

However, UDP and IP aren’t robust enough to communicate error conditions. If a UDP port is not listening or too much data is sent to a listening port, UDP has no way to convey these conditions. That is where ICMP comes in: It provides a simple means of communicating between hosts or a router and a host to alert them to some kind of problem situation.

## Where Does ICMP Fit In?

The TCP/IP Internet layering model discussed in [Chapter 1](ch01.html), “IP Concepts,” is one representation of the different layers that form data and pass the data between hosts. [Figure 4.1](ch04.html#ch04fig01) illustrates this.

![TCP/IP Internet model.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/04fig01.gif)

**Figure 4.1. TCP/IP Internet model.**

Starting at the top, you can see the high-level application layer activity that might represent a TCP/IP application such as telnet. Next is the transport layer, with such protocols as TCP and UDP that provide the end-to-end communication between hosts. Beneath that is the Internet layer, which is responsible for getting the datagram from source to destination. Finally, there is the network layer, which transmits the datagrams over the network.

You can see from this that ICMP is in the same network layer as IP. ICMP is encapsulated in the IP datagram after the IP header, but it is still considered to be in the same layer as IP.

## Understanding ICMP

ICMP differs from TCP and UDP in several ways. For starters, ICMP has no port numbers like those found in the transport layer protocols UDP or TCP. The closest thing that ICMP has to a differentiation in services is an ICMP message type and code, the first 2 bytes in the ICMP header. These bytes tell the function of the particular ICMP message.

**ICMP Types**

Listing and exploring all the variations of ICMPs is beyond the scope of this book. However, [www.iana.org/assignments/icmp-parameters](http://www.iana.org/assignments/icmp-parameters) is a great reference for those who want to know more about this topic.

Next, there is really no such thing as a client and server. In fact, when ICMP error messages are delivered, the receiving host might respond internally but might not communicate anything back to the informer. ICMP also gives no guarantees about the delivery of a message.

One of the unusual traits about ICMP is that services or ports do not have to be activated or listening. Just about every operating system can respond to an ICMP echo request (ping). The hard part is turning off the default behavior of responding to an ICMP echo request.

Another unique trait about ICMP is that it supports broadcast traffic. TCP required an exclusive client/server unicast relationship, but ICMP isn’t nearly as exclusive. As the “[Smurf Attack](ch04.html#ch04lev2sec17)” section of this chapter shows, ICMP’s willingness to respond to broadcast traffic sometimes can cause problems.

A host uses ICMP for simple replies and requests, and it uses ICMP to inform another host of some kind of error condition. For instance, a receiving host might have a problem keeping up with the traffic that the sending host is delivering to it. One of the ways that a host can inform a sending host to throttle down the delivery rate is to send it an ICMP source quench message.

ICMP is used as a mechanism by routers to inform a sending host of some kind of problem. A router might deliver an ICMP “admin prohibited” message to a sending host. This means that the sending host attempted to send some kind of traffic that was forbidden by an access control list statement of a router interface.

In a situation such as this, you would expect the router to be the sender of the message because it is the one forbidding the activity. However, a router also might intervene to inform a sending host about a condition when a destination host cannot respond. If the destination host is unreachable, for example, the destination host can obviously not respond. In this instance, the router might reply instead.

Although a router might try to be helpful by informing the sending host of a problem, it also is providing information that could be used for reconnaissance purposes. The sender then could glean some knowledge about the type of activity that the router reports. A good security practice is to silence a router by preventing it from issuing ICMP unreachable messages to preclude the dissemination of unnecessary information. This will be discussed in more detail in the section, “[Host Unreachable](ch04.html#ch04lev2sec10).”

## Summary of ICMP Theory

Let’s quickly summarize what you’ve learned in this short section on ICMP theory. You have learned that ICMP is a means of delivering error messages between hosts. It is encapsulated in an IP header, but is considered part of the IP or Internet layer.

ICMP is a unique protocol because it doesn’t use ports to communicate like the transport protocols do. ICMP messages can get lost and not be delivered. In addition, ICMP can be broadcast to many hosts because there is no sense of an exclusive connection.

Finally, hosts and routers are the senders of ICMP messages. Hosts listen for ICMP, and most will respond unless they deliberately have been altered for silence.

# Mapping Techniques

Mapping a target network is a very strategic part of most intelligently planned attacks. This initial step in reconnaissance attempts to discover the live hosts in a target network. An attacker then can direct a more focused scan or exploit toward live hosts only.

If mapping is not done and a malicious user or program attacks a network, the attack can become very noisy by generating a lot of traffic on the target network and not be very productive. The latter quarter of 1999 saw an example of this kind of bull-in-a-china shop reckless scan. A Trojan named RingZero that infected Windows hosts appeared to scan foreign hosts for open Web proxy ports. One of the shortcomings of the RingZero scanning activity was that it appeared to scan random hosts on many networks. In doing so, many IP addresses that were not active were scanned along with the active ones. This was a noisy scan for intrusion-detection systems that saw it. Also, a lot of work had to be done to receive any valuable feedback about hosts that supported open Web proxy ports. This would have been a more directed and perhaps more informative scan if the IP numbers that were scanned had been live hosts.

**The Ubiquitous RingZero Trojan**

The observed RingZero attack in a monitored network involved many different source IPs scanning mostly inactive TCP ports: 3128 (squid proxy server), 80 (normal HTTP port), and 8080 (an alternative HTTP port). About half a dozen of these scans were detected on a Class B subnet every hour. Many other sites all over the world that were capable of detecting this activity reported seeing it, too.

An initial theory was that all this activity was coming from spoofed source IPs with an unknown intent. However, Ron Marcum, a system administrator at Vanderbilt University, discovered a Windows host in his network that was doing this kind of scanning and captured the software called RingZero. At the *System Administration, Networking, and Security* (SANS) conference in October 1999, the RingZero software was dissected.

When activated in a test network, the host on which it was installed began to scan random hosts for the Web proxy ports. If open Web proxy server ports were discovered, they were sent back to an ftp site that aggregated this information for the collector. It is assumed that the collector then planned to use this knowledge for some future plundering. To date, we still see RingZero scanning activity and it is still unknown what the infection method is and how an infected host selects the IP numbers to scan for proxy ports.

One of the most common methods of mapping is to issue ICMP echo requests. A host (or hosts) responds to an ICMP echo request with an ICMP echo reply to signal it is a live host. This is what the ping command does; it issues an ICMP echo request and waits for an ICMP echo reply. Many security and network administrators have responded to this invasive ICMP scrutiny with the knee-jerk reaction of blocking ICMP echo requests. This is a good and necessary reaction, but this is only a partial solution because it is only a minor impediment to the insistent pursuer. Blocking ICMP echo requests has motivated hackers to invent other scanning methods using other protocols.

In [Chapter 2](ch02.html), the section, “An ACK Scan,” showed how TCP scans can use the ACK flag to attempt to identify live hosts. This can be used as an alternative network scanning method that blocks ICMP echo requests. The next sections look at some of the conventional and esoteric mapping techniques used.

## Tireless Mapper

The following scan shows the classic mapping technique of sending individual ICMP echo requests to all hosts in a given subnet. In this case, the `192.168.117` Class C subnet is scanned for all live hosts. As you can see, this is a very noisy scan:

```
00:05:58.560000 scanner.net > 192.168.117.233: icmp: echo request 
00:06:01.880000 scanner.net > 192.168.117.139: icmp: echo request 
00:12:45.830000 scanner.net > 192.168.117.63: icmp: echo request 
00:15:36.210000 scanner.net > 192.168.117.242: icmp: echo request 
00:15:58.600000 scanner.net > 192.168.117.129: icmp: echo request 
00:18:51.650000 scanner.net > 192.168.117.98: icmp: echo request 
00:20:42.750000 scanner.net > 192.168.117.177: icmp: echo request 
00:26:36.680000 scanner.net > 192.168.117.218: icmp: echo request 
00:27:30.620000 scanner.net > 192.168.117.168: icmp: echo request 
```

If a site doesn’t specifically look for ICMP activity, however, this might go unnoticed. So, the age-old philosophical question becomes, if a hacker maps your entire network and no one is listening, does it make any noise? Alarming on individual ICMP echo requests likely would generate a lot of alerts from an IDS, so IDSs usually do not issue alerts for individual ICMP echo requests. Yet, an IDS that examines more generic scan activity that exhibits a one-to-many source-to-destination IP relationship would correctly trigger on such a scan. In other words, if the IDS looks for one source IP connecting to many different destination IPs in a given time period—for instance, seven connections per hour—it would discover the preceding scan.

## Efficient Mapper

Most likely, the preceding scan was automated so that it wasn’t a labor-intensive effort for the not-so-wily scanner. But why bother with all the volume if ICMP is a protocol that can be sent to a broadcast address and can ping many hosts with a couple of commands? That is what the following scanner attempts:

```
13:51:16.210000 scanner.net > 192.168.65.255: icmp: echo request 
13:51:17.300000 scanner.net > 192.168.65.0: icmp: echo request 
13:51:18.200000 scanner.net > 192.168.66.255: icmp: echo request 
13:51:18.310000 scanner.net > 192.168.66.0: icmp: echo request 
13:51:19.210000 scanner.net > 192.168.67.255: icmp: echo request 
13:53:09.110000 scanner.net > 192.168.67.0: icmp: echo request 
13:53:09.940000 scanner.net > 192.168.68.255: icmp: echo request 
13:53:10.110000 scanner.net > 192.168.68.0: icmp: echo request 
13:53:10.960000 scanner.net > 192.168.69.255: icmp: echo request 
13:53:10.980000 scanner.net > 192.168.69.0: icmp: echo request 
```

It appears that the scanner is attempting to map the 192.168 subnet. The third octet in the IP number changes from 65 to 69 in this excerpt from a larger scan. You can see the final octet fluctuate between 0 and 255. The 255 in the final octet is the classic broadcast address. The 0 in the final octet is a broadcast address for hosts that have a TCP/IP stack based on the UNIX *Berkeley Software Distribution* (BSD) operating system. Using both these broadcast addresses, all live hosts in an accessible network should respond.

This should convince you to deny into your network any activity destined for these broadcast addresses. I don’t know of any legitimate activity for traffic destined for broadcast addresses except for diagnostic activity. The section, “[Smurf Attack](ch04.html#ch04lev2sec17),” shows that disallowing this activity prevents Smurf amplification by your network.

## Clever Mapper

In examining the next scan, you can see a new variation on an old mapping scheme:

```
06:34:31.150000 scanner.net > 192.168.21.0: icmp: echo request 
06:34:31.150000 scanner.net > 192.168.21.63: icmp: echo request 
06:34:31.150000 scanner.net > 192.168.21.64: icmp: echo request 
06:34:31.150000 scanner.net > 192.168.21.127: icmp: echo request 
06:34:31.160000 scanner.net > 192.168.21.128: icmp: echo request 
06:34:31.160000 scanner.net > 192.168.21.191: icmp: echo request 
06:34:31.160000 scanner.net > 192.168.21.192: icmp: echo request 
06:34:31.160000 scanner.net > 192.168.21.255: icmp: echo request 
```

Look at the scanning pattern. You can see that ICMP echo requests are being sent to the Class C subnet of 192.168.21. Now look at the final octet of the IP address. You can see that the first request is sent to the 0 broadcast address, and the last one is sent to the 255 broadcast address. This isn’t new; you saw this in the preceding scan.

Notice in the final octet of the other IP numbers, however, that they seem to span 64 IP numbers. For instance, the first IP number has a final octet of 0, and the following one has a final octet of 63. That is 64 total IP addresses. What is the significance of 64? Well, a typical Class C subnet has 256 addresses between the 0 and 255 range.

It is possible to subdivide a Class C network so that you have multiple smaller networks by assigning an appropriate subnet mask. One way to do this is to have four individually addressable subnets with 64 hosts each. In this scheme, the network and broadcast addresses change accordingly. The network and broadcast addresses for those four subnets are the IP numbers that you see in the scan. So, it turns out that the scanner believes that this scanned network might have a different addressing scheme than the Class C “natural” division. If this were truly the addressing scheme for the 192.168.21 subnet, all live hosts might respond. Even if the subnet is a standard Class C and the activity is not blocked, this will still ping all hosts on the network because it uses the .0 and .255 broadcast addresses. If you need a refresher about address classes, reference the “[Logical Addresses, IP Addresses](ch01.html#ch01lev2sec7)” section in [Chapter 1](ch01.html).

## Cerebral Mapper

One final scan shows a different mapping technique using another ICMP request type. The ICMP address mask request queries a host for the subnet mask of the network on which it resides. Remember all the trouble that the preceding scanner went through to try to determine the addressing scheme? That could have been avoided entirely by using the following ICMP address mask request:

```
20:39:38.120000 scanner.edu > router.com: icmp: address mask request (DF) 
20:39:38:170000 router.com > scanner.edu: icmp: address mask is 0xffffff00 
(DF) 
20:39:39.090000 scanner.edu > router2.com: icmp: address mask request (DF) 
20:39:39:230000 router2.com > scanner.edu: icmp: address mask is 0xffffff00 
(DF) 
20:39:40.090000 scanner.edu > routerx.com: icmp: address mask request (DF) 
20:39:40:510000 routerx.com > scanner.edu: icmp: address mask is 0xffffff00 
(DF) 
```

This is not a classic mapping technique per se, but it can provide some initial reconnaissance. The quest here is to examine the subnet mask of different routers. Typically, only routers respond to address mask requests so the scanner might discover additional reconnaissance of the repliers. As discussed in [Chapter 1](ch01.html), the subnet mask assigned to a computer system tells it how many bits in its IP address designate the network and how many designate the host.

If a scanner can determine a subnet mask of a network, he knows exactly how many hosts need to be scanned. Although the subnet mask of a host usually can be determined from looking at the first octet of the IP number, this request might discover the networks that don’t have a “natural” subnet mask. That type of knowledge cannot be obtained from looking at the IP number alone. In this example, the scanned routers respond with subnet masks of a hexadecimal ffffff00. This translates to a decimal `255.255.255.0` subnet mask of the network on which they reside. This means that these hosts all belong to a Class C network. Querying for address masks is another type of ICMP activity that should be disallowed into the network, for obvious reasons.

## Summary of Mapping

Let’s briefly recap the discussion about mapping. Mapping can be done using the following methods:

- Sending individual ICMP echo requests to hosts in a network
- Sending ICMP echo requests to the broadcast addresses of a network
- Sending ICMP echo requests to network and broadcast addresses of subdivided networks
- Sending an ICMP address mask request to a host on the network to determine the subnet mask to better understand how to map efficiently

# Normal ICMP Activity

This section examines some of the expected uses of ICMP—specifically, several different error messages that ICMP sends to inform a host of some kind of problem situation. Looking at mutant ICMP activity is more intriguing, but you’ve got to be able to understand what’s normal before you can recognize abnormal ICMP activity.

## Host Unreachable

In the following ICMP output, you can see an error message to `sending.host`, which is attempting to send traffic to a target host:

```
router > sending.host: icmp: host target.host unreachable 
```

For some reason, the `target.host` is unreachable—perhaps no host resides at the requested IP address, perhaps the host is temporarily unavailable, or perhaps the host is suffering from some kind of misconfiguration that prevents it from responding.

In a situation such as this, the host obviously cannot send an error message, so the router that oversees the target host’s network intervenes to deliver the message. In this case, the router informs the sending host that the target host is unreachable. As you can probably guess, this gives a scanner valuable information that he can use to help him map the network. If a scanner is collecting information about live hosts in a network to later scan, those that have been identified as unreachable would likely not be scanned again. This makes any subsequent scans more focused.

The valuable reconnaissance information that can be gleaned from many of the ICMP unreachable commands can be detrimental to the security of a given network. Cisco router access control lists have a statement `no ip` `unreachables` that can silence the router interface from issuing the ICMP unreachable messages.

## Port Unreachable

The ICMP output that follows demonstrates how a target host informs a sending host that a requested UDP port is not listening. In this example, the sending host attempts to send traffic to the target host on the UDP *network time protocol* (ntp) port:

```
target.host > sending.host: icmp: target.host udp port ntp unreachable (DF) 
```

Therefore, the protocol used to deliver the error message is ICMP. Remember that when you examined TCP, that protocol had a different way of informing a sending host that a port was not active. It returned a packet with the TCP RESET flag set to indicate that the port was not listening. UDP has no built-in mechanism to report about this error, so it enlists ICMP to assist.

Again, you can see that valuable reconnaissance can be gained from this ICMP error message—namely that scanned UDP ports that do not respond with this message could be listening ports. But, it is also possible that scanned UDP ports that do not respond might never have received that scan due to packet loss. It is also possible that outbound port unreachable messages are blocked from leaving the network. So, you can see that the absence of a port unreachable message from a scanned UDP port is not a definitive confirmation that the port is listening.

## Admin Prohibited

Take a look at another possible problem situation with the following output:

```
router > sending.host: icmp: host target.host unreachable - admin prohibited 
```

In this scenario, a sending host is attempting to deliver traffic to a target host. A router is at the gateway of the target host network.

The router has an access control list that prohibits certain types of traffic from entering the network. This could be a port that is blocked, a protocol that is blocked, or possibly the source IP or subnet that is denied access, or the destination IP or subnet that is protected. A router might respond to this condition with an ICMP “unreachable - admin prohibited” message. Although this ICMP message does not indicate what is being blocked (a destination port, a source IP, or an IP protocol, for instance), an astute scanner can attempt different combinations of connections and figure out what is being disallowed into the network and possibly find other avenues into the network that are not blocked.

## Need to Frag

Another ICMP message warns that a desired host is unreachable because of a problem with fragmenting a datagram:

```
router > sending.host.net: icmp: target.host unreachable - need to frag (mtu 
1500) 
```

The DF output in TCPdump means that the Don’t Fragment flag is set. As the name implies, if this flag is set, fragmentation will not be done on the datagram. If this flag is set and the datagram crosses a network in which fragmentation is required, the router discovers this, discards the datagram, and sends an ICMP error message back to the sending host.

The ICMP error message contains the *maximum transmission unit* (MTU) of the network that required fragmentation. Some hosts conversing in TCP intentionally send an initial datagram across the network with the DF flag set as a way to discover the smallest MTU for a particular source-to-destination path. If the ICMP error message is returned with the smallest MTU, the host then packages all datagrams bound for that destination in small enough chunks to avoid fragmentation. The intent is to eliminate the overhead and inefficiencies in packet loss associated with fragmentation.

## Time Exceeded In-Transit

This ICMP message informs a sending host that a datagram has overstayed its welcome on the Internet:

```
routerx > sending host: icmp: time exceeded in-transit 
```

IP needs a way to flush a lost datagram from the Internet, perhaps one that is in some kind of routing loop in which it is bouncing aimlessly between routers. The means used to prevent wayward datagram activity involves a field in the IP header known as the *time-to-live* (TTL) value.

Different operating systems set different initial TTL values. To examine default initial TTL values set by operating systems, go to [http://project.honeynet.org/papers/finger/traces.txt](http://project.honeynet.org/papers/finger/traces.txt).

When a datagram traverses a router on its travel from the source to destination, each router decrements the TTL value by 1. If the value ever becomes 0, the router discards the datagram and sends an ICMP “time exceeded in-transit” message back to the sending host. [Chapter 5](ch05.html), “Stimulus and Response,” shows how traceroute uses this ICMP “time exceeded in-transit” message along with incrementing TTL values to discover and record interim routers along the path from a given source to destination.

## Embedded Information in ICMP Error Messages

It is helpful to understand that when an ICMP error message is returned, there is some additional information that is supplied in the datagram. Specifically, after the actual ICMP message, you will find the IP header followed by eight bytes of protocol header and data of the original datagram that caused the error, as seen in [Figure 4.2](ch04.html#ch04fig02). This information allows the receiving host to associate this error with the sending process and react appropriately. An external response to an ICMP error message is not expected because RFC 1122 describes this as one of the conditions for which no ICMP reply should be generated.

![ICMP error message format.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/04fig02.gif)

**Figure 4.2. ICMP error message format.**

It is also useful to be aware that not all TCP/IP stacks will precisely copy the IP header and following eight bytes. It would seem logical that the embedded information following the ICMP error message, reflecting the first 28 bytes of the offending packet, would exactly match the first 28 bytes of the offending packet. In fact, nmap can be used to discover a remote host’s operating system by sending normal and aberrant traffic to a target host. It looks for responses and behavior of the target host that will distinguish it from standard expected behavior to assist in operating system classification. One test in a series of traffic to the target host attempts to send a datagram to a closed UDP port. The desired response to this is an ICMP “port unreachable” message. But, nmap examines several of the fields in the ICMP error message containing the IP header and following eight bytes of the initial probe of the UDP port. It examines these fields to see if they match the fields in the datagram that elicited the error. This information is used to determine the operating system.

## Summary of Normal ICMP

In the previous sections, you examined some of the many ICMP messages that you might see while monitoring your network. You also saw many of the different informative ICMP error messages. As you noticed, these can be sent by either hosts or routers that discover a problem.

These sections also discussed the notion that some of the ICMP unreachable errors are best prevented from leaving your network if you are concerned about the reconnaissance information that could be gathered from them.

# Malicious ICMP Activity

Not unexpectedly, it was just a matter of time until ICMP became tainted in purpose. Today, ICMP has been corrupted for use in many different types of denial-of-service attacks, and it has been used in a most stealthy attack as a covert channel. This section examines some of these malicious uses of ICMP.

**Black Ice**

As I was driving to work one wintry morning after a night of precipitation, it occurred to me that the day’s commute was much like the philosophy of my job as a security analyst. I cautiously navigated the long, winding, snow-covered driveway; slowed my pace; shifted to a lower gear descending the steep hill out of the neighborhood; and safely drove around the abandoned car in my lane going uphill. I treated the identified hazards with due caution and respect, but it was the unseen dangers such as black ice that worried me.

Each day, as I analyze traffic to our sites, I have this omnipresent uneasy feeling about what it is I am not seeing—the black ice of our networks. I have seen firsthand the persistence, guile, and cleverness that the Internet pirates use to try to find and exploit what they want. As a security analyst, this “What am I missing?” semi-paranoid attitude is one you must adopt. If you become too complacent about the security of your site, your site could spin out of control from the unidentified perils.

## Smurf Attack

The infamous Smurf attack, shown in [Figure 4.3](ch04.html#ch04fig03), preys on ICMP’s capability to send traffic to the broadcast address. Many hosts can listen and respond to a single ICMP echo request sent to a broadcast address. This capability is used to execute a denial-of-service attack against a hapless target host or network.

![Anatomy of a Smurf attack.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/04fig03.gif)

**Figure 4.3. Anatomy of a Smurf attack.**

First, a malicious host must craft an ICMP echo request with a spoofed source IP to a broadcast address of an intermediate network. The spoofed source IP chosen is that of the victim target host/network. Next, the intermediate site must allow broadcast activity into the network. If it does, the ICMP echo request is sent to all hosts on the given subnet to which the broadcast was sent. Finally, all the live hosts in the intermediate network that respond send an ICMP echo reply to what they believe to be the sender, or the victim host. The victim host or network on which it resides can become choked with all the activity and can suffer a degradation or denial-of-service attack if the following conditions exist:

- The malicious user sends many ICMP requests to the broadcast address.
- The intermediate site allows inbound broadcast traffic.
- The intermediate site is large and has many responding hosts. On the other hand, many smaller intermediate sites might be used to achieve the same result.
- The target site has a slow Internet connection. To be more precise, the Internet connection must be susceptible of being overwhelmed by too many packets for the supported bandwidth. Although it is possible to inundate and clog *any* Internet connection given enough traffic, slower connections are more vulnerable.

Therefore, this is another reason that you want to deny broadcast traffic from entering into your network. Your site cannot be used as a Smurf amplification network if broadcast traffic is not allowed.

## Tribe Flood Network

The *Tribe Flood Network* (TFN) attack is another denial-of-service attack that uses ICMP for communication. [Figure 4.4](ch04.html#ch04fig04) depicts the attack. Unlike the Smurf attack, which originates from one source and uses one intermediate network as an amplification point, the TFN attack enlists the help of many distributed hosts, known as daemon or zombie hosts. Hence, the *term distributed denial of service* (DDoS) is a more accurate description of the use of dispersed hosts to participate in an attack.

![Tribe Flood Network attack.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/04fig04.gif)

**Figure 4.4. Tribe Flood Network attack.**

This attack requires a TFN master host and daemon hosts to be established. These are typically compromised hosts on which TFN was installed. The master TFN host then instructs the daemon hosts to attack a victim host, perhaps simultaneously. The communication between the master and daemon host is done using the ICMP echo reply. The daemons can send the target host a UDP flood, a TCP SYN flood, an ICMP echo request flood, or a Smurf attack. The master instructs the daemon what to do by sending commands in the ICMP echo reply. The ICMP identification number field in the ICMP header of the ICMP echo reply is used to direct the daemons of the action to take. The data portion of the ICMP echo reply is used to send arguments.

You might be wondering why this attack uses ICMP echo replies instead of ICMP echo requests. The reason is that more sites block ICMP echo requests because they are aware of the hazards of allowing them in the network. However, they may allow ICMP echo replies in to get responses from pings to hosts outside the network and because they don’t realize the threats posed by rogue ICMP echo requests.

As you have probably concluded, by using several distributed intermediate hosts simultaneously to flood the target host, a denial-of-service attack against the target network or target host is the anticipated outcome. If you want to read more about TFN, go to [www.cert.org](http://www.cert.org) and search for incident IN-99-07.

**Self-Inflicted Denial of Service?**

It was December 29, 1999. As I prepared to begin my stint at a Y2K center for the Office of the Secretary of Defense, I mulled over the rumors of impending cyberspace doom. The widespread consensus was that there would be massive denial-of-service attacks directed against infrastructure services such as power and transportation. Despite the hackers’ promised plans of drunken celebration with the masses, the prevailing sentiment was that the release of distributed denial-of-service tools such as TFN coincided with the arrival of the new millennium.

In response to the perceived threat, many sites all but shut down or greatly restricted access to their networks. The irony of this was noted by a coworker who said, “It seems rather funny to avoid a denial-of-service attack by turning off the services yourself.”

## WinFreeze

The WinFreeze attack essentially causes a susceptible host to attack itself—an ugly kind of self-mutilation:

```
router > victim.com: icmp: redirect 243.148.16.61 to host victim.com 
router > victim.com: icmp: redirect 110.161.152.156 to host victim.com 
router > victim.com: icmp: redirect 245.211.87.115 to host victim.com 
router > victim.com: icmp: redirect 49.130.233.15 to host victim.com 
router > victim.com: icmp: redirect 149.161.236.104 to host victim.com 
router > victim.com: icmp: redirect 48.35.126.189 to host victim.com 
router > victim.com: icmp: redirect 207.172.122.197 to host victim.com 
router > victim.com: icmp: redirect 113.27.175.38 to host victim.com 
router > victim.com: icmp: redirect 114.102.175.168 to host victim.com 
```

The ICMP redirect message informs a sending host that it has tried to use a nonoptimal router and tells the sending host to add a more optimal router to its routing table. The WinFreeze attack can cause a vulnerable Windows NT host to suffer a denial of service by flooding it with ICMP redirect messages. This is executed on a network on which the victim host resides and purports to send ICMP redirect messages from the router. When the Windows host receives a flood of these messages, it attempts to add these changes to its own routing table and could suffer from degraded performance.

In the preceding output, the router is informing victim.com to redirect its traffic to many different random IP numbers to itself. The host victim.com might be overwhelmed when trying to apply all those changes to its own routing table.

## Loki

Probably the most subversive and destructive use of ICMP to date is known as Loki. In Norse mythology, Loki was the god of trickery and mischief. So too is the Loki exploit the master of trickery. As you have seen, ICMP is intended to be used to inform of error conditions and to make simple requests. As such, intrusion analysts prior to the release of Loki regarded ICMP as a fairly harmless protocol, except for the denial-of-service attacks generated using it and for the network mapping information it could provide if not blocked.

Loki uses ICMP as a tunneling protocol for a covert channel. A covert channel is one that uses a transport method or data field in a secret or unexpected manner. In other words, the transport vehicle is ICMP; but operationally, Loki acts much like a client/server application. If a host is compromised and a Loki server is installed, it can respond to traffic sent to it by a Loki client. For instance, the Loki client could send a request to the Loki server to cat/etc/passwd to display the password file. The Loki client user then would see the output from the display, capture it, and possibly crack the password file. You can find more information on Loki at [www.phrack.com](http://www.phrack.com) issue 49, article 6.

The danger in this whole scheme is that a seemingly innocuous protocol is being used to do some very sophisticated and potentially damaging exchanges. Again, ICMP was never intended to support applications such as this. My advice to the intrusion analyst is to regard ICMP traffic with heightened suspicion and to stop just shy of outright paranoia.

## Unsolicited ICMP Echo Replies

Now, try your hand at some analysis and put into practice some of the theory you just learned about ICMP exploits by examining the output that follows:

```
reply.com >192.168.127.41: icmp: echo reply 
reply.com >192.168.127.41: icmp: echo reply 
reply.com >192.168.127.41: icmp: echo reply 
reply.com >192.168.127.41: icmp: echo reply 
reply.com >192.168.127.41: icmp: echo reply 
reply.com >192.168.127.41: icmp: echo reply 
```

What you observe here is a host, reply.com, sending the 192.168.127.41 host ICMP echo reply traffic. This would not be unusual if the 192.168.127.41 host had sent an ICMP echo request eliciting these responses. However, this is not the case; no outbound ICMP echo requests were sent from 192.168.127.41. Why might someone initiate such activity? You learn possible reasons in the next three sections.

One thing to keep in mind is that for this kind of activity to be detected, you must have some kind of IDS or supporting software capable of maintaining state. This means that you must be able to determine whether any prior traffic had issued ICMP echo requests. Many IDSs do not maintain state information and cannot detect such anomalous activity. Let’s examine some of the possible theories that might explain this anomalous activity.

### Theory 1: Spoofing

The first theory poses the possibility that you see this traffic because someone has borrowed the source IP 192.168.127.41 and has issued ICMP echo requests to reply.com using the spoofed source IP; reply.com then replies to the real 192.168.127.41 IP address. If you saw ICMP echo replies from many other hosts on the same network as reply.com, you could be a Smurf target.

A dramatic increase in spoofing activity has arisen, so this is the most common explanation for this type of activity. Typically, when you have witnessed unsolicited ICMP echo replies that appear to be using your spoofed source IPs (in this example, 192.168.127.41), you might see other unsolicited activity from the same intermediate host (in this example, reply.com). You usually don’t see this activity in isolation—you might see these replies going to many different 192.168.127 hosts, not just a single reply multiple times.

### Theory 2: TFN

A second theory involves the TFN attack. You learned that the TFN master communicates with its TFN daemons using ICMP echo replies.

Therefore, another possibility is that the host receiving the unsolicited ICMP echo replies, 192.168.127.41, has become a victim TFN daemon. Although the ICMP identification value field is used to direct the daemon host to attack the victim, the exact value found in this field might not be predictable if the attacker changes the default source code. The more obvious way to determine whether the 192.168.127.41 has become an unwitting TFN daemon is to examine the outbound activity from 192.168.127.41 after receiving the ICMP echo requests. If it sends a flood of unexplained traffic outbound, it is possibly participating in a TFN attack.

### Theory 3: Loki

The final theory is that this could be an exchange between a Loki client and a Loki server. When Loki traffic is exchanged, it might not have a pattern of each ICMP echo request generating a reply. It is possible for the Loki server to respond with multiple ICMP echo replies to a single ICMP echo request.

Original releases of Loki had a signature of a static value in the sixth and seventh bytes (starting with byte 0) of the ICMP message. This could be determined by dumping the traffic using TCPdump with hexadecimal output and observing the lack of change in this field that is the ICMP sequence number. This field is usually unique for each ICMP echo request sent out and, much like the IP header identification number, increments by 1 or 256 for each subsequent ICMP echo request. Later incarnations of Loki might use encryption and might not be decipherable in this manner.

As you have witnessed, ICMP echo traffic, whether request or reply, can facilitate some noxious activity. So, this is an excellent candidate for blocking by a packet-filtering device.

## Summary of Malicious ICMP Traffic

To wrap up this section, you learned that ICMP has been manipulated in use for other purposes than the intended ones. ICMP can be used in a denial-of-service attack, as you observed in the Smurf and WinFreeze attacks. ICMP was used more as a conduit for communication in the TFN attack. It might not be used directly as a denial-of-service attack, but it enables a denial-of-service attack to occur by providing the communication vehicle between the TFN master and daemons. Finally, you saw that Loki has completely altered the original purpose of ICMP by using it as a tunneling mechanism for malicious activity.

# To Block or Not to Block

After reading about all the havoc that ICMP now can wreak, it appears that ICMP left Kansas along with Dorothy and Toto. From a reconnaissance aspect, if you can elicit any of the following ICMP messages from a host, you know you have reached a live host:

- “protocol unreachable”
- “port unreachable”
- “IP reassembly time exceeded”
- “parameter problem”
- “echo reply”
- “timestamp reply”
- “address mask reply”

Also, if you can get a router to report ICMP `host unreachable` errors, it is possible to inversely map a network assuming that those hosts which do not have this error reported are indeed live hosts.

As if this isn’t enough information, the following common ICMP messages are sent by routers only so if you can elicit any of the following, you can identify a site’s routers:

- “fragmentation needed but don’t-fragment bit set”
- “admin prohibited”
- “time exceeded in transit”
- “network unreachable”
- “host unreachable”

And, finally, we can discover more reconnaissance by the following ICMP messages:

- “admin prohibited: can assist in examining what type of traffic the site blocks”
- “address mask reply: gives the subnet mask of the network on which the responding host resides”
- “time exceeded in transit: used in traceroute to discover routers and network topology”
- “protocol unreachable: can be used to inversely map a host’s listening protocols”
- “port unreachable: can be used to inversely map a live host’s listening UDP ports”
- “fragmentation needed but don’t fragment bit set: can be used to determine the MTU of links for use in attacks that use fragments”

Given all the reconnaissance that ICMP can supply, why not just unconditionally block all incoming and outgoing ICMP traffic? Some sites do just this, but let’s examine some of the repercussions of blocking all inbound ICMP.

## Unrequited ICMP Echo Requests

Obviously, your ability to do diagnostic activity using ping is broken when you block both inbound ICMP echo requests and echo replies. The good news is that ICMP echo requests and replies cannot be used as a front for stolen goods if blocked. The inconvenience suffered by this loss might be justified by the improvement of your security posture, eliminating a possible stealthy avenue into your network.

You might face a temptation to block only inbound ICMP echo requests, which would enable you to do diagnostics from your network and receive a response by virtue of the ICMP echo response gaining inbound access. The hackers know this, however, and as you have witnessed with Tribe Flood Network and Loki, they are relying more on the use of ICMP echo reply as a delivery mechanism.

## Kiss traceroute Goodbye

Whether you use the UNIX **traceroute** command or the Windows **tracert** command to discover the routers through which a datagram travels on its path from source to destination, blocking inbound ICMP prevents you from executing these commands from your network to other networks. These commands require inbound ICMP “time exceeded in-transit” messages to operate correctly. By preventing all ICMP into the network, you break your use of traceroute outbound.

The Windows **tracert** command uses the ICMP echo request, so blocking inbound ICMP precludes a user from doing a tracert to a machine in your network. The UNIX **traceroute** uses UDP as the protocol, however, so blocking inbound ICMP does not prevent someone from executing a UNIX **traceroute** to a host in your network.

## Silence of the LANs

As you learned in this chapter, ICMP can inform about unreachable conditions to a particular host or port. When you block all inbound ICMP messages, hosts or routers on your network cannot receive these informative messages. This does not produce catastrophic results, but it does cause some inefficiencies. As an example, a host on your network might attempt a TCP connection to another host that might be down. This could elicit a “host unreachable” message from a remote router, but the host attempting this connection doesn’t receive the ICMP unreachable message because it is blocked. The sending host retries until it times out, thereby sending unnecessary traffic.

## Broken Path MTU Discovery

As discussed previously, when possible, a host sending TCP traffic tries to avoid fragmentation of datagrams. This is done using path MTU discovery. As covered in this chapter, a sending host uses the Don’t Fragment flag in a discovery packet. The intent is for the discovery packet to reach the destination host without being fragmented, or for the sending host to receive an ICMP “need to frag” message with the value of the smaller MTU found in the message.

Therefore, blocking all inbound ICMP breaks this mechanism and causes some significant problems. A host sending the discovery packet expects to receive an ICMP “need to frag” message if fragmentation is required. Because it receives no such message due to the inbound ICMP block, it continues to send oversized datagrams with the Don’t Fragment flag set. These are dropped, but the sending host is never informed of this. Packets sent that are smaller than the smallest MTU along the path arrive at the destination, but larger ones do not.

So, if you choose to block ICMP, make sure that you make an exclusion to allow “host unreachable - need to frag” ICMP messages into your network.

# Summary

ICMP is a protocol that is supposed to be used to alert hosts of problem conditions or to exchange simple messages. It can be transmitted between two hosts exclusively, or it can be transmitted to multiple hosts using the broadcast address.

Regard ICMP as a potential threat. This chapter has identified some of the current known malicious uses of ICMP. No doubt, many more will come, with many new flavors of unknown subversions.

Block inbound ICMP, but do so wisely and selectively. Although you will prevent potentially malicious traffic from entering your network, make sure that you understand the adverse consequences to your own network of blocking inbound ICMP traffic.
