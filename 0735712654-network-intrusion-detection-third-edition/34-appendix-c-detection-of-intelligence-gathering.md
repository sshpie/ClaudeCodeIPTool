# Appendix C. Detection of Intelligence Gathering

![Detection of Intelligence Gathering](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

[Chapter 16](ch16.html), “Architectural Issues,” raised the issue that CIRTs have to focus primarily on compromised systems. And they do! How would you feel if you were on the phone with your CIRT trying to get information you need to deal with the latest nasty Trojan horse code and they said, “Sorry we are devoting all our resources to a new intelligence-gathering technique?”

Wise intrusion analysts devote a lot of attention to the prevention, detection, and reporting of mapping techniques. They know that recon is just part of the game. As attackers amass high-quality information about the layout of networks and distribution of operating systems, it enables them to specifically target their attacks. You do not want to allow your organization to get in a one-exploit, one-kill situation!

The line between exploit/denial of service and recon probe couldn’t be thinner. Any exploit that fails (or succeeds) also provides intelligence about the target.

This appendix contains many traces showing information-gathering techniques and reviews some of the ways an attacker might map the network and its hosts. This appendix also briefly covers NetBIOS-specific issues because there are so many deployed Windows systems. The appendix concludes by examining some of the so-called stealth mapping techniques.

# Network and Host Mapping

The goal of host mapping is just to determine what hosts or services are available in a facility. In some sense, the odds are in the analysts’ favor; we are, after all, defending very sparse matrices. Suppose you have a Class B network, 172.20.0.0 (which is 65,536 possible addresses). There are also 65,536 TCP ports and 65,536 UDP ports possible per host. That means that the attacker has 23 trillion+ possible targets. Scanning at a rate of 18 packets per second, it would take a shade under 5 million years to completely scan the network. Because computers have a life span of between three and five years, the rate of change confounds the usefulness of the scan.

Now to be sure, attackers are coming up with smarter and faster scanning techniques. An attacker has no need to consider all possible port numbers. Fifty TCP and UDP ports account for the probable services, so the target space is something in the range of 163 million (which could be scanned in less than four months at 18 packets per second). Hmmmm, that is achievable! And if the site doesn’t have intrusion detection, the site owners will probably never know whether the attacker’s scan randomizes the addresses and ports a bit.

If the attackers can get an accurate host map, however, they can turn the tables on those of us who defend networks big time. Many address spaces are lightly populated. If the attacker can determine where the hosts are, they have a serious advantage. Suppose our Class B network is populated with only about 6,000 computers, for instance, and the attacker can find them. Now the attacker can scan the populated hosts on the network, at 18 packets per second, in less than 10 days—and there are still much more efficient ways to do the scan. In fact, if we allow ICMP echo request broadcasts, they can ping map our network with only 255 packets.

The point of the story is obvious. If attackers cannot get intelligence information about our site, they are forced to guess about a very sparse matrix. If we do let their intelligence-gathering probes succeed, they don’t have to do much guessing at all.

So how can an attacker get such an accurate host map? Many sites still make a *host table* available for FTP download. Other sites allow DNS zone transfers. Or, perhaps the attacker has to work to discover this information with host scans.

[Chapter 4](ch04.html), “ICMP,” covered some of the more rudimentary ICMP mapping techniques. The crudest of them all tried to send ICMP echo requests to individual hosts and created a lot of noise doing so. We also saw the broadcast ICMP echo requests that attempted to map a network by sending the ICMP echo requests to the .0 and .255 addresses, possibly making the process more efficient and less noisy. This section describes another mapping attempt using the echo request and revisits the network-based broadcast in more detail.

## Host Scan Using UDP Echo Requests

In the following trace, the attacker is targeting multiple network addresses. Two were detected by this sensor constellation, but it is very probable there were many more. By interleaving the scan, the attacker has managed to space the UDP echo requests far enough apart that the probe will not be detected by most scan detect codes. The scrambled addresses are also a nice touch. The `udp 6` refers to UDP payload with 6 bytes of data. As discussed in the last section in this chapter, stealth in intrusion detection has a fairly specific meaning, but I consider the low and slow approach the best stealth technique. Here is the trace:

```
02:08:48.088681 slowpoke.mappem.com.3066 > 192.168.134.117.echo: udp 6 
02:15:04.539055 slowpoke.mappem.com.3066 > 172.31.73.1.echo: udp 6 
02:15:13.155988 slowpoke.mappem.com.3066 > 172.31.16.152.echo: udp 6 
02:22:38.573703 slowpoke.mappem.com.3066 > 192.168.91.18.echo: udp 6 
02:27:07.867063 slowpoke.mappem.com.3066 > 172.31.2.176.echo: udp 6 
02:30:38.220795 slowpoke.mappem.com.3066 > 192.168.5.103.echo: udp 6 
02:49:31.024008 slowpoke.mappem.com.3066 > 172.31.152.254.echo: udp 6 
02:49:55.547694 slowpoke.mappem.com.3066 > 192.168.219.32.echo: udp 6 
03:00:19.447808 slowpoke.mappem.com.3066 > 172.31.158.86.echo: udp 6 
```

Instead of relying on the ICMP echo request to find hosts, this scan is seeing whether any host will reply on the echo port. The echo port echoes back (imagine that) any characters sent to it. Good system administrators should not have this port listening and good network administrators should not allow in traffic to this port.

**A Word About Detecting Scans**

Until some brilliant researcher comes up with a better technique, scan detection boils down to testing for *X* events of interest across a *Y*-sized time window. An intrusion-detection system can and should have more than one scan detect window. For instance, we have seen several scans that exceed five events per second. By using a short time window in the range of one to three seconds, the system can detect a high-speed scan and alert in near real-time, three to five seconds after the scan begins. Nipping such scans in the bud is one of the best uses of automated reaction. The next reasonable time window is on the order of one to five minutes. This detects slower but still obvious scans. The Shadow intrusion-detection system has had some success with a scan detect of five to seven connections to different hosts over a one-hour window.

I developed code that was enhanced by Bill Ralph that implemented a scan detect process designed to examine a 24-hour time window to investigate the TCP half-open scans and mildly low and slow scans. Now that most intrusion detection systems feed databases, a major focus of console development is detection of low and slow scans. Scans have been detected using database queries with rates as low as five packets from a single IP address over 60 days. A scan rate that low makes sense only if it is interleaved (executed in parallel from multiple source addresses) to the extreme. We have documented scans of about 2,500 hosts working together and the entire w32.leaves worm network was about 30,000 compromised hosts, so distributed slow scans are in the hands of attackers.

## Netmask-Based Broadcasts

Which of the echo requests in the following trace are broadcasts? All of them! We all recognize the 0 and the 255, but they are all broadcast packets under the right conditions, and the point of this trace is to test for these conditions. What are these right conditions? They are networks that have a different subnet mask than the usual one. Take a look:

```
02:21:06.700002 pinger> 172.20.64.0: icmp: echo request 
02:21:06.714882 pinger> 172.20.64.64: icmp: echo request 
02:21:06.715229 pinger> 172.20.64.63: icmp: echo request 
02:21:06.715561 pinger> 172.20.64.127: icmp: echo request 
02:21:06.716021 pinger> 172.20.64.128: icmp: echo request 
02:21:06.746119 pinger> 172.20.64.191: icmp: echo request 
02:21:06.746487 pinger> 172.20.64.192: icmp: echo request 
02:21:06.746845 pinger> 172.20.64.255: icmp: echo request 
```

I once worked in a facility that charged for network addresses. A single host address was $50/month and a subnet with a netmask of 255.255.255.0, or 256 possible addresses, was $1,000/month. The facility had a Class B address space assigned to it, 172.29.0.0, which they broke up into subnets. It turns out that if we bought a router and leased a subnet from them, we could bring our address space tax way down. Here is how.

Rent one subnet 172.29.15.0 for $1,000/month. The expected subnet mask would be 255.255.255.0. That gives us 256 possible addresses, but 0 and 255 are not usable for hosts, so that leaves 254 usable addresses. At $50/month, that is $12,700/month; so getting the subnet for $1,000/month is already a big win. With our own router, however, we could make the subnet mask anything we wanted on “our” side of the router.

Suppose we could find three more small groups as cheap, er frugal, and ruggedly individual as we are. We could use 2 bits of our address space for internal subnets to create four subnets with 6 bits of address space each. 26 is 64. The netmask for this is 255.255.255.192, or in hex 0xffffffc0. We could each have our own subnet to do with as we please and split the $1000/month for just a little more than the price of five individual addresses. Great, but what is the broadcast value for a subnet mask of 255.255.255.192?

255 – 192 = 63, which is the broadcast value for an “all 1s” broadcast, which means 0 or 64 is the value for an “all 0s.” If that is too easy, however, consider this:

```
c      0    in hex is 
1100   0000 in binary. 
^^          the two high order bits were lost to the NETID 
  ^^   ^^^^ so we have 6 bits of host ID to play with 
```

6 bits all set to 1s = 32 + 16 + 8 + 4 + 2 + 1 = 63.

Now, the pattern we see in the trace above is an ICMP echo request to 0, 64, 63, 127, 128, 191, 192, and 255.

Could 127 and 128 also be broadcasts? Sure, if we have a situation in which we need lots of subnets, but each one can have a lower number of hosts if we can steal 1 bit from the HOSTID space and use it for subnets. If we use 25 bits for the NETID (33,554,432 possible subnets) each with 7 bits of HOSTID space (128 possible addresses), this would be a subnet mask of 255.255.255.128. What is the broadcast address? 255 – 128 = 127. 127 is the “all 1s” broadcast.

Could 191 and 192 also be broadcasts? If we have a situation in which we need lots and lots of subnets, but each one can have a low number of hosts, we can use 27 bits for the NETID (134,217,728 possible subnets) each with 5 bits of HOSTID space (32 possible addresses). This is a subnet mask of 255.255.255.64. 255 – 64 = 191.

Of course if we allow ICMP in, they could just send one packet with an ICMP netmask request and be done with it! If the site answers a netmask request, it returns the network mask that it is using, eliminating the guesswork.

## Port Scan

Time for an easier trace. The following trace is a basic port scan. After our attacker has found a host, he may want to scan it to see what services are active. This trace is TCP, and the scan counts down on the destination port. The skips in the source ports are interesting. This may be a very busy machine or more than one scan may be going on. This is a good example of a bursty trace; compare the arrival times at the beginning of the trace to the end. In the beginning of the trace, there is a lower number of packets per second arriving than at the end. Any number of factors can influence this. If we can correlate this trace to other traces from other sensor systems and they are also bursty, however, we can begin to make some assumptions about the source machine. The skipped source ports indicate the source of the burstiness may be the source computer and not the network in between. If we can match up the source ports of our detect with a detect from another sensor, we may be able to make assumptions as to whether multiple scans are occurring, or whether this scan is being initiated from a busy multiple-user computer. The trace follows:

```
09:52:25.349706 bad.guy.org.1797 > target.mynetwork.com.12: S 
09:52:25.375756 bad.guy.org.1798 > target.mynetwork.com.11: S 
09:52:26.573678 bad.guy.org.1800 > target.mynetwork.com.10: S 
09:52:26.603163 bad.guy.org.1802 > target.mynetwork.com.9: S 
09:52:28.639922 bad.guy.org.1804 > target.mynetwork.com.8: S 
09:52:28.668172 bad.guy.org.1806 > target.mynetwork.com.7: S 
09:52:32.749958 bad.guy.org.1808 > target.mynetwork.com.6: S 
09:52:32.772739 bad.guy.org.1809 > target.mynetwork.com.5: S 
09:52:32.802331 bad.guy.org.1810 > target.mynetwork.com.4: S 
09:52:32.824582 bad.guy.org.1812 > target.mynetwork.com.3: S 
09:52:32.850126 bad.guy.org.1814 > target.mynetwork.com.2: S 
09:52:32.871856 bad.guy.org.1816 > target.mynetwork.com.1: S 
```

## Scanning for a Particular Port

So what service runs on TCP 7306? Durned if I know. As I mentioned in [Appendix A](apa.html), it never hurts to ask [www.google.com](http://www.google.com), because all of the port lists I have looked at are incomplete. This trace was collected in late December 1998, which was the beginning of a number of interesting scans that all seemed to be targeting strange ports. This scan is well crafted; there is no obvious signature.

The first and last packet in the following trace resolve to a host name; the middle four don’t, as is obvious from the fact that the Internet address is shown for these rather than a name. This can indicate that the attacker is “shooting in the dark,” that he does not have an accurate network map. Often a reason some names do not resolve is that they don’t exist. Take a minute to look at the last packet in the trace; source ports usually increase, but this decreases by 22. Because the initial sequence number (49684211) is also lower, this packet probably got lost along the way and arrived out of order:

```
09:54:40.930504 prober.3794 > lula.arpa.net.7306: S 49684444:49684444(0) win 
8192  (DF) 
09:54:40.940663 prober.3795 > 192.168.21.20.7306: S 49684454:49684454(0) win 
8192  (DF) 
09:54:41.434196 prober.3796 > 192.168.21.21.7306: S 49684945:49684945(0) win 
8192  (DF) 
09:54:41.442674 prober.3797 > 192.168.21.22.7306: S 49684955:49684955(0) win 
8192  (DF) 
09:54:41.451029 prober.3798 > 192.168.21.23.7306: S 49684965:49684965(0) win 
8192  (DF) 
09:54:41.451049 prober.3776 > host.arpa.net.7306: S 49684211:49684211(0) win 
8192  (DF) 
```

## Complex Script, Possible Compromise

The next trace is comprised of multiple individual probes and attacks. It is shown here in five parts. The accesses to portmap (SUNRPC) imply this attacker is attempting a compromise or gathering intelligence. Further, the system answers back, which is a bad thing. Portmap should be blocked by the filtering router or firewall, and secure portmap code should be on any system that runs SUNRPC. Note that these attacks are directed against two systems: host 16 and host 17. From the ports accessed, I assume these are UNIX systems. It is quite possible that these two systems have a trust relationship so that if one falls, they both fall.

Then we see the access to TCP port 906, which is unassigned, and the target system answers back. This could well indicate that malicious code has been installed on the system. Instead of sending or receiving data, however, the attacker closes the connection. Two hours later, the attacker pings to see whether the systems are still there. Take a look:

```
00:35:33.944789 prober.839 > 172.20.167.16.sunrpc: udp 56 
00:35:33.953524 172.20.167.16.sunrpc > prober.839: udp 28 
00:35:33.984029 prober.840 > 172.20.167.17.sunrpc: udp 56 
00:35:33.991220 172.20.167.17.sunrpc > prober.840: udp 28 

00:35:34.046598 prober.840 > 172.20.167.16.906: S 2450350587:2450350587(0) 
win 512 
00:35:34.051510 172.20.167.16.906 > prober.840: S 1996992000:1996992000(0) 
ack 2450350588 win 32768  (DF) 

00:35:34.083949 prober.843 > 172.20.167.17.sunrpc: udp 56 
00:35:34.089272 172.20.167.17.sunrpc > prober.843: udp 28 

00:35:34.279472 prober.840 > 172.20.167.16.906: F 117:117(0) ack 69 win 32120 
00:35:34.284670 172.20.167.16.906 > prober.840: F 69:69(0) ack 118 win 32768 
(DF) 

02:40:43.977118 prober > 172.20.167.16: icmp: echo request 
02:40:43.985138 172.20.167.16 > prober: icmp: echo reply 
```

The preceding trace is fairly significant, and as an analyst I would be concerned and recommend further investigation. Let’s talk about response for a minute. We want to back up, investigate, contain, and clean. If these were my systems, I would direct the following:

- Take your hands off the keyboard and keep them off.
- Pull the network cable immediately; we will be right there.
- After you are on the scene, one of your top priorities is to back up the system(s).
- Treat the backup tape as evidence.

The port 906 bears further investigation. The easiest thing to do is bring a laptop and a small hub to the system you expect may be compromised. Plug the laptop and one of the possibly compromised systems into the hub. Then, load your own copies of system utilities (ls, ps, netstat, for example) into a directory on the suspect system and set your path to that directory, or get them from a CD that you have created. From the laptop, telnet to the possibly compromised system on port 906. Run your versions of netstat and ps and such on the suspect system to see what is active. Also, examine the .rhosts and /etc/hosts.equiv on the suspect system to see what other systems are trusted by our dynamic duo.

**An Alternative Approach**

There is no way I can do justice to incident handling in a few paragraphs. *Incident Handling Step by Step* is a collaboration of more than 90 incident handlers. It is available from [www.sans.org](http://www.sans.org). One best practice technique if the system is down, or must be rebooted, is to use a bootable CD-ROM. Then, you can mount the system disk as a data drive. If at all possible, keep the original hard drive as evidence.

When you are finally satisfied that you understand what is going on with port 906, unless you are totally certain the system was not compromised, the following is the best course of action.

Turn to the system owners and ask when the last full backup was made. Make sympathetic clucking noises as they say “never” or “two years ago” and nod your head sadly. Look them in the eye and ask whether any data absolutely must be saved. Back up data files only, format the hard drive, and tell them to be sure to install all the appropriate security patches before putting the system back in business. Hook your laptop to the local area network. Scan the local net for SUNRPC and also for systems that answer on port 906, whatever else you have learned. Continue nuking from high orbit until the infection is sanitized.

Does this sound draconian? The death of a thousand cuts is far worse. By the way, we have talked about Loki and distributed denial of service tools like Trinoo using echo requests and replies for other purposes. Perhaps you would want to take a close look at the content of that ping in the trace as well.

## “Random” Port Scan

This scan was well on its way to setting a speed record. This is another example of scanning ports that don’t make any sense. There is no detectable signature; the purpose of the scan is unknown:

```
11:48:42.413036 prober.18985 > host.arpa.net.794: S 1240987936:1240987936(0) 
win 512 
11:48:42.415953 prober.18987 > host.arpa.net.248: S 909993377:909993377(0) 
win 512 
11:48:42.416116 prober.19031 > host.arpa.net.386: S 1712430684:1712430684(0) 
win 512 
11:48:42.416279 prober.19032 > host.arpa.net.828: S 323265067:323265067(0) 
win 512 
11:48:42.416443 prober.19033 > host.arpa.net.652: S 1333164003:1333164003(0) 
win 512 
11:48:42.556849 prober.19149 > host.arpa.net.145: S 2112498338:2112498338(0) 
win 512 
11:48:42.560124 prober.19150 > host.arpa.net.228: S 1832011492:1832011492(0) 
win 512 
11:48:42.560824 prober.19151 > host.arpa.net.840: S 3231869397:3231869397(0) 
win 512 
11:48:42.561313 prober.19152 > host.arpa.net.1003: S 2435718521:2435718521(0) 
win 512 
11:48:42.561437 prober.19153 > host.arpa.net.6: S 2632531476:2632531476(0) 
win 512 
11:48:42.561599 prober.19165 > host.arpa.net.280: S 2799050175:2799050175(0) 
win 512 
11:48:42.563074 prober.19166 > host.arpa.net.845: S 2065507088:2065507088(0) 
win 512 
11:48:42.563115 prober.19226 > host.arpa.net.653: S 1198658558:1198658558(0) 
win 512 
11:48:42.563238 prober.19227 > host.arpa.net.444: S 1090444266:1090444266(0) 
win 512 
11:48:42.565041 prober.19274 > host.arpa.net.907: S 2414364472:2414364472(0) 
win 512 
```

Okay, we don’t know the purpose of the scan, and that is frustrating. So as an analyst, what do we know about this? We know it is fast and we know that the source port behavior is unpredictable—sometimes it skips, and sometimes it doesn’t. Why doesn’t the trace make sense? Why in the world is someone scanning so many unknown ports? I am not sure that we will ever know these answers. In the past few years, there have been a lot of very odd scan patterns. The best guess I have is that someone was using nmap, hping2, isic, packetx, or a similar tool to craft scans that had no possible purpose, probably from spoofed source addresses. That answers how, but not why!

Here is a guess: to drive intrusion-detection analysts crazy; to see what they would report and what they wouldn’t; to see whether the scanners could cause a CNN news report that the world was under some horrid new cyber attack. Granted, it is far fetched, but it is the best I can come up with. How should the analyst react to this trace and other unknown seemingly random scans? I do recommend reporting stuff like this, because you never know what piece of information will help your CIRT. If your firewall is set to deny everything not specifically allowed, and none of your hosts answer back, however, don’t get stressed. The best idea is to create a directory named “Scans_From_Mars” and file these detects there.

## Database Correlation Report

I am a strong fan of allowing analysts to “fire and forget”—that is, when they see a detect, just report it and move on. When we first started doing fairly large-scale intrusion detection (five sites, 12,000 computers or so), the analyst had to manually check all the sensors for a correlation of source port, source IP, destination port, destination IP, and so on. Back then, if you were looking for something like correlation of TTL field or some behavior of the sequence number, it might take days to sort it out.

Life is too short for that kind of madness. After a pattern has been detected and reported, the database looks to see whether any correlations exist. This is what such a report might look like. This report was generated by a military correlation system known as Dark Shadow. It is based on an Oracle database. When an analyst detects and reports an intrusion attempt, Dark Shadow checks for that pattern across its data window of *X* sensor locations for *Y* months. If it finds a match, it creates a correlation report. This is why the analyst can operate in a fire-and-forget mode.

Note that from the source port ranges, it appears that two processes are running (destination port 111 is contacted by source ports from 617–1023, and destination port 25 by ports 2294–29419) on scanner, one to check email and the other to check portmapper. The two processes are probably bound by a shell script and reading from a file of target IP addresses. The probability is very high that this scan is interleaved across many more addresses. Here it is:

```
06/04/98 03:20:25   scanner    622      172.20.1.41    111  t 
06/04/98 04:02:35   scanner  21091       172.20.1.1     25  t 
06/04/98 04:02:36   scanner    890       172.20.1.1    111  t 
06/04/98 04:06:04   scanner  21242    172.20.10.114     25  t 
06/04/98 04:09:15   scanner    617    172.20.10.114    111  t 
06/04/98 07:24:47   scanner   2295    192.168.229.18    25  t 
06/04/98 07:28:06   scanner   1017    192.168.229.18   111  t 
06/04/98 07:28:21   scanner   2333      172.20.1.41     25  t 
06/04/98 07:31:40   scanner    729      172.20.1.41    111  t 
06/04/98 12:46:21   scanner  20553    172.20.48.157     25  t 
06/04/98 12:49:40   scanner   1023    172.20.48.157    111  t 
06/04/98 16:05:22   scanner  29276       172.20.1.1     25  t 
06/04/98 16:08:33   scanner    803       172.20.1.1    111  t 
06/04/98 16:08:52   scanner  29419    172.20.10.114     25  t 
06/04/98 16:08:53   scanner    900    172.20.10.114    111  t 
```

## SNMP/ICMP

The *Simple Network Management Protocol* (SNMP), even before the exploits that followed the release of the PROTOS toolkit in early 2002, could provide an attacker with a lot of information about your hosts and network configuration. According to the RFC NSMP is port 161 TCP and UDP. I have never seen a TCP version of SNMP in practice, but for safety, ) port 161 TCP and UDP should be blocked from the Internet.

It is amazing how many devices, such as micro hubs, x-terminals, and printers, have SNMP agents. By default, these devices are protected by a well-known password (community string), typically “public.” Many security-conscious organizations change this password, usually to one of the following:

- Private
- Internal
- The name of the organization

*Note:* Forgive me if you thought I was serious. The choices of private, internal, or the name of the organization for SNMP community strings are not advised. Pick something hard to guess.

In the following trace, notice the use of broadcast for both SNMP and ICMP. This is a very effective mapping technique because the attacker doesn’t have to send many packets to potentially collect a lot of information.

```
17:31:33.49 prober.1030 > 192.168.2.255.161: GetNextRequest(11)[|snmp] 
17:31:33.73 prober.1030 > 255.255.255.255.161: GetNextRequest(11)[|snmp] 
17:31:33.73 prober > 255.255.255.255: icmp: echo request 
... 
17:43:17.32 prober > 192.168.1.255: icmp: echo request 
17:43:17.32 prober.1030 > 192.168.1.255.161: GetNextRequest(11)[|snmp] 
```

## FTP Bounce

We have another trace courtesy of the correlation database engine. In this case, the analyst is searching for FTP-DATA (TCP port 20) without an initiating FTP (TCP port 21). This can be the result of FTP bounce. The advantage to the attacker of using FTP bounce is that his identity is hidden. This is just like using an open proxy server, except that the source port will always show as TCP 20 for FTP-DATA. To do this, they just log on to a vulnerable FTP server as anonymous and open up arbitrary ports to probe the intended victim. This is not usually a very serious threat, unless the FTP server is a trusted host by its organization. Then, an attacker may be able to use the FTP server to probe the organization. FTP bounce is the subject of a CERT advisory, which you can find at [www.cert.org/ftp/cert_advisories/CA-97.27.FTP_bounce](http://www.cert.org/ftp/cert_advisories/CA-97.27.FTP_bounce).

In some implementations of FTP daemons, the **PORT** command can be misused to open a connection to a port of the attacker’s choosing on a machine that the attacker could not have accessed directly. There have been ongoing discussions about this problem (called “FTP bounce”) for several years, and some vendors have developed solutions for this problem.

When we uncovered the traffic in the following trace, we went back to prober and it was an FTP server, it supported anonymous FTP, and we were able to use the **port** command as advertised. The interesting thing is this trace was detected long before going to unknown ports became a fad. The following trace represents all the connections from prober to the protected network (172.20.152):

```
date     time        source IP  src port dest IP        dest port 
04/27/98 10:17:31    prober     20       172.20.152.2   3062 t 
04/27/98 10:27:32    prober     20       172.20.152.2   4466 t 

05/06/98 06:34:22    prober     20       172.20.152.2   1363 t 
05/06/98 09:12:15    prober     20       172.20.152.2   4814 t 
05/06/98 09:15:07    prober     20       172.20.152.2   1183 t 
05/06/98 10:11:30    prober     20       172.20.152.2   1544 t 
```

# NetBIOS-Specific Traces

This section examines some traces that appear to be targeted at Windows systems. NetBIOS uses 135–139 TCP and UDP. It is certainly true that other systems than Windows use NetBIOS (SAMBA, for example), but as a general rule NetBIOS traffic can be expected to be generated by and targeted against Windows systems.

## A Visit from a Web Server

One of the characteristics of NetBIOS is that traffic to destination port UDP 137 is often caused by something a site initiates. If you send email to a site running Microsoft Exchange, for example, the site will often send a port 137 attempt back. The following trace turned up because we saw 137s and then we started searching for the cause factor. To find the answer, we pulled all traffic for jellypc and found the web access. Then, we did the same for jampc and it was the same pattern. Being able to pull all the traffic for a host is very valuable when doing analysis. If your IDS does not support this, beat on your vendor!

**Public Safety Announcement**

Although this section focuses mostly on NetBIOS, let me take a minute to mention that there are hostile web servers on the Internet. When a system from your site visits a web server, that server can collect a lot of information about you, including your operating system and browser version. If your site doesn’t use *Network Address Translation* (NAT), the web server will have your IP address. It is often possible to extract the web client’s email address. Some sites open a connection back to the client and perform what we believe is TCP stack analysis. (And we haven’t even discussed cookies.)

The web server in the jellypc trace wasn’t satisfied with just the information it could collect from the HTTP headers; the server wanted more, so another system from the same subnet comes back to the hosts that visited the web server to collect the information available from the NetBIOS Name Service.

Here is the pattern:

```
12/02/97 08:27:18   jellypc.arpa.net 1112 -> www.com     http 
12/02/97 08:27:19        0 bill.com        137 -> jellypc.arpa.net       137 

12/02/97 17:06:03  jampc.arpa.net 2360 -> www.com     http 
12/02/97 17:08:10        0 bill.com        137 -> jampc.arpa.net       137 
```

I got on the phone and had a great chat with a technical type who runs the network there. It turns out that they are using a piece of commercial software for marketing purposes that creates a comprehensive database of your likes and dislikes.

If you want to see what kind of information is available about a particular Microsoft Windows host, the command is called nbtstat and it runs on Windows NT systems. A Windows host that runs NetBIOS cannot refuse to answer an nbtstat. A sample trace is shown here:

```
C:\>nbtstat -a goo 

NetBIOS Remote Machine Name Table 

   Name               Type         Status 
---------------------------------------------
Registered Registered Registered 
MAC Address = 00-60-97-C9-35-53 

GOO            <20>  UNIQUE 
GOO            <00>  UNIQUE 
KD2            <00>  GROUP 
KD2            <1C>  GROUP 
KD2            <1B>  UNIQUE 
GOO            <03>  UNIQUE 
SRN0RTH        <03>  UNIQUE 
INet~Services  <1C>  GROUP 
IS~GOO         <00>  UNIQUE 
KD2            <1E>  GROUP 
KD2            <1D>  UNIQUE 
..__MSBROWSE__.<01>  GROUP 
```

The NetBIOS name of my machine, Goo, can be picked up as well as my workgroup, KD2. The logon name I use on that machine is srnorth. It is also possible to determine that I have a master browser cookie.

Perhaps this application of the wildcard request doesn’t concern you, but I have been able to use nbtstat queries to determine an entire organizational structure as well as most of the logon names.

## Null Session

But wait, there’s more. Null sessioning has been described as analogous to finger. In essence, it is logging on to a system as a nobody user. Although you cannot modify anything, you can learn about the system. A sample command string is as follows:

```
net use \\172.20.244.164\IPC$ "" /USER:"" 
```

This generates literally pages of information, a section of which is shown here:

```
2/18/98 1:39 AM - Jsmith - \\192.168.4.22 
UserName 

Administrator 
   Groups,Administrators (Local, 
Members can fully administer the computer/domain) 
   AccountType,User 
   HomeDrive 
   HomeDir 
   PswdCanBeChanged,Yes 
   PswdLastSetTime,Never 
   PswdRequired,Yes 
   PswdExpires,No 
   AcctDisabled,No 
   AcctLockedOut,No 
   AcctExpiresTime,Never 
   LastLogonTime,11/20/98 3:24 PM 
   LastLogonServer,192.168.4.22 
   Sid,S-1-5-21-706837240-361788889-398547282-500 
```

Null sessioning can be prevented on Windows 2000 and if you will give me a second, I will test it on Windows XP Professional. Yup, it works—Control Panel, Administrative Tools, Local Security Policy.

# Stealth Attacks

The first time I heard the term *stealth* was in a paper by Chris Klaus titled “Stealth Scanning—Bypassing Firewalls/SATAN Detectors.” He was describing what people now usually refer to as “half open”—that is, intentionally violating the TCP three-way handshake. There are a number of variations of half scans, and we are going to examine all the common ones. These are not all that hard to detect in and of themselves, but as you will learn in the discussion on coordinated attacks, they are getting some help. Nowadays, some folks use stealth to mean null flags (no flags or code bits set). The only approaches I find actually stealthy are those based on either low and slow, or highly distributed, packet delivery. As time goes on, static packet filters continue to be less and less common; half-open scans are less and less an issue. They certainly should not be called stealth because they stand out like a sore thumb. The Snort web page, [www.snort.org](http://www.snort.org), lists a number of effective rules to detect these probes.

This is a season of advanced scans; attackers with the skill to type, make, and actually compile software are using tools that give them the look and feel of “eleetness.” Three years ago it was jackal; at the turn of the century, hping and nmap; and today, distributed scanners.

In the book, *Inside Firewalls* by Robert Ziegler (New Riders), I commented that I continue to be astounded by the security provided by Network Address Translation (NAT). My most important files are on a vmware version of Linux 7.2 on my Windows laptop, and the Linux system is behind a NAT. So, if attackers can get through my home perimeter defenses, which also include a NAT, and break into my XP laptop, they still have another NAT to go through. With appliance firewalls available as cheap as $300, you can afford a number of NATs in your organization, which will foil most of this scanning. There is also a strong argument that nothing penetrates a well-configured, proxy-based firewall (although we will dispute this in a moment). None of the deception tools will elude a well-trained analyst with an IDS that collects all the traffic and has a supporting database. If your site has chosen a lesser path, you may be in for a wild ride.

> As we get ready to launch into some traces of stealth techniques, take a minute to read the opening comment from the original 1997 jackal.c source code. /* Jackal -Stealth/FireWall scanner. With the use of halfopen ports and sending SYNC (sometimes additional flags like FIN) one can scan behind a firewall. And it shouldnt let the site feel we’re scanning by not doing a 3-way-handshake we hope to avoid any tcp-logging. Credits: Halflife, Jeff (Phiji) Fay, Abdullah Marafie. Alpha Tester: Walter Kopecky. Results: Some firewalls did allow SYN | FIN to pass through. No Site has been able to log the connections though during alpha testing. ShadowS [shadows@kuwait.net](mailto:shadows@kuwait.net) Copyleft (hack it i realy dont care). */

It was a brilliant idea! If the filtering router tests for SYN, feed it a SYN/FIN. However, the statement that jackal had never been logged by any site misses the mark. In [Appendix A](apa.html), “Exploits and Scans to Apply Exploits,” you saw the IMAP traces with the SYN/FIN set, which were detected by the Shadow system. Competent intrusion-detection systems were able to log and analyze anything sent by jackal (or hping or nmap). In fact, today when attackers set SYN/FIN, they make our job easy.

## Explicit Stealth Mapping Techniques

The two well-known explicit mapping techniques are the SYN/ACK and the FIN scan. Both of these generate a RESET, if they hit an active host. They also get an ICMP error message back if the host is unreachable. Explicit stealth mapping is more efficient than inverse mapping (described later), but is possibly more obvious.

### FIN Scan

I have never detected a FIN scan in the wild and have chosen not to simulate one. In the case of a FIN scan, one would detect a large number of packets with the FIN flag set where there was no three-way handshake ever established. We have already discussed using a database to find FTP bounce. A good intrusion-analysis system should provide the capability to look for spurious traffic such as FINs, to connections that were never established. I have seen ACKs only and have seen them penetrate a Check Point firewall.

### Inverse Mapping

Inverse mapping techniques can compile a list of networks, or hosts, that are not reachable and then use the converse of that map to determine where things probably are. We will also show a DNS example of all replies and no queries. Before we go on, though, if you absolutely cannot do NAT and must use public IP addresses, make sure you do not allow ICMP unreachables out of your network. That will not stop all inverse mapping techniques, but it will quench a large number of them. As you look at the trace that follows, keep this in mind: the answers by router.mynet.net are doing all the harm:

```
02:58:05.490 stealth.mappem.com.25984 > 172.30.69.23.2271: 
     R 0:0(0) ack 674719802 win 0 
02:59:11.208 stealth.mappem.com.50620 > 172.16.7.158.1050: 
     R 0:0(0) ack 674719802 win 0 
02:59:20.670 stealth.mappem.com.19801 > 192.168.184.174.1478: 
     R 0:0(0) ack 674719802 win 0 
02:59:31.056 stealth.mappem.com.7960 > 192.168.242.139.1728: 
     R 0:0(0) ack 674719802 win 0 
02:59:42.792 stealth.mappem.com.16106 > 172.16.102.105.1008: 
     R 0:0(0) ack 674719802 win 0 
03:00:50.308 stealth.mappem.com.8986 > 172.16.98.61.1456: 
     R 0:0(0) ack 674719802 win 0 
03:00:58.939 stealth.mappem.com.35124 > 192.168.182.171.1626: 
      R 0:0(0) ack 674719802 win 0 
03:00:58.940 router.mynet.net > stealth.mappem.com: 
      icmp: host 192.168.182.171 unreachable 
```

### Answers to Domain Queries

Another variation of inverse mapping is shown here. The probing computer sends answers to domain questions that were never asked. The goal is to stumble across a subnet or host that doesn’t exist, which will generate an ICMP unreachable message. As stated earlier, this pattern tends to evade detection. It can be found with scan detect code if the attacker gets greedy and probes too many hosts too quickly. It can also be detected by retrospective analysis scripts or database searches for application state violations. Here is the example of inverse mapping:

```
05:55:36.515566 stealth.com.domain > 172.29.63.63.20479: udp 
06:46:18.542999 stealth.com.domain > 192.168.160.240.12793: udp 
07:36:32.713298 stealth.com.domain > 172.29.185.48.54358: udp 
07:57:01.634613 stealth.com.domain > 254.242.221.165.13043: udp 
09:55:28.728984 stealth.com.domain > 192.168.203.163.15253: udp 
10:38:53.862779 stealth.com.domain > 192.168.126.131.39915: udp 
10:40:37.513176 stealth.com.domain > 192.168.151.126.19038: udp 
10:44:28.462431 stealth.com.domain > 172.29.96.220.8479: udp 
11:35:40.489103 stealth.com.domain > 192.168.7.246.44451: udp 

11:35:40.489103 stealth.com.domain > 192.168.7.246.44451: udp 
11:35:40.489523 router.mynet.net > stealth.com: 
                     icmp: host 192.168.7.246 unreachable 
```

Because IP spoofing, usually part of a denial-of-service attack, is so common, you may be asking, “Why isn’t the explanation for this IP spoofing of the 172.29, 192.168, and so forth addresses and directing them to stealth.com?” Couldn’t this just be seeing the echoes of this activity directed back to our network? The problem is that this doesn’t resemble normal DNS responses. It doesn’t have any indications that some kind of DNS query was issued.

To investigate this further, you might try to find out whether stealth.com is really a DNS server. You use the **nslookup** command and change servers to stealth.com and try to resolve any address. If it works, you know that stealth.com is a true DNS server and the mystery intensifies. (Tragically, nslookup, at least on UNIX, is being deprecated by the more obscure dig program.) If it doesn’t respond, chances are it is not a DNS server, and it really is the aggressor. It is also possible that it is a DNS server, but you might not have access to it.

### Answers to Domain Queries, Part 2

The following activity is similar to what you just saw because both use source port of 53 or domain. This output is TCP and came from multiple different sources, however, unlike the preceding activity. Any guesses about what is going on here?

```
11:19:30.885069 host1.corecomm.net.53 > myhost1.com.21: S 7936:7936(0) win 
1024 
11:17:29.375069 host1.corecomm.net.53 > myhost1.com.139: S 7936:7936(0) win 
1024 
11:15:32.115069 host1.corecomm.net.53 > myhost1.com.23: S 7936:7936(0) win 
1024 
11:11:17.485069 host1.corecomm.net.53 > myhost1.com.43981: S 7936:7936(0) win 
1024 
11:09:12.945069 host1.corecomm.net.53 > myhost1.com.880: S 7936:7936(0) win 
1024 
12:01:05.060000 host70.corecomm.net.53 > pc112.com.880: S 1738:1738(0) win 
1024 
12:03:24.820000 host70.corecomm.net.53 > pc112.com.139: S 1738:1738(0) win 
1024 
12:06:12.620000 host70.corecomm.net.53 > pc112.com.21: S 1738:1738(0) win 
1024 
12:09:09.940000 host70.corecomm.net.53 > pc112.com.43981: S 1738:1738(0) win 
1024 
12:09:57.960000 host70.corecomm.net.53 > pc112.com.23: S 1738:1738(0) win 
1024 
```

This appears to be a scan of myhost1.com, pc112.com, and many other hosts not shown in this abbreviated output of some common destination ports such as 21 (FTP), 23 (telnet), and 139 (NetBIOS Session Manager). But, there are some funky destination ports along with those common ones that aren’t readily identifiable, such as 43981 and 880. You can round up all the usual suspect explanations for the unconventional ports, but in this case, your analysis should concentrate more on the source port used.

TCP source port 53 might be allowed into many networks because this can be indicative of activity from a long DNS response. Remember from [Chapter 6](ch06.html), “DNS,” that UDP DNS responses of more than 512 bytes are reissued to the DNS server to destination port TCP 53. When the response returns to your network, the source port will be 53 and you need to allow that back in to receive that response. A smart network administrator qualifies this so that it is allowed back in only if it was established inside the network of origin, and only if the destination port is greater than 1023 (indicative of an ephemeral port), which is the case in the long DNS responses.

That is not the case in the preceding scan, but the scanner is banking on the packet-filtering device being open on source port 53 without any further qualification. This way, the scanner might circumvent a normally protective packet-filtering device.

It is interesting to note that the TCP sequence numbers you see in the scan are repeated for each of the same source-to-destination port scans. These should change for each new TCP segment created. Another forensics tidbit about this scan that is not obvious unless you look at many more records than are shown, gives some insight into the nature of the TCP sequence number crafting. The preceding scan shows two TCP sequence numbers: 7936 and 1738. Considering that the TCP sequence number field is 32 bits long, these are very small initial sequence numbers—quite unusual. All the TCP sequence numbers from this scan were lightweight, and when the activity was dumped in hex, the reason why was discovered. The high-order 16 bits of the TCP sequence number were always 0s. This is confirmation that some kind of sequence number manipulation was performed, and it becomes a signature of this activity.

### Fragments, Just Fragments

Consider this final example of an inverse mapping technique. As you have already learned, only the first fragment chunk comes with protocol information. Attackers using this technique (along with some interesting variations) were able to penetrate older firewalls and filtering routers. The firewalls would assume that this was just another segment of traffic that had already passed their access lists. Needless to say, this has been fixed in most vendors’ products.

In this case, however, the prober isn’t particularly interested in firewall penetration. Once again, if one of the target hosts does not exist, the router sends back an unreachable message. The attacker can then compile a list of all the hosts that do not exist and, by taking the inverse of that list, has a list of the hosts that do exist. This is why this class of techniques is called inverse mapping. Take a look:

```
18:32:21.050033 PROBER > 192.168.5.71: (frag 9019:480@552) 
18:32:21.109287 PROBER > 192.168.5.72: (frag 9275:480@552) 
18:32:21.178342 PROBER > 192.168.5.73: (frag 9531:480@552) 
18:32:21.295332 PROBER > 192.168.5.74: (frag 9787:480@552) 
18:32:21.344322 PROBER > 192.168.5.75: (frag 10299:480@552) 
18:32:21.384284 PROBER > 192.168.5.76: (frag 10555:480@552) 
18:32:21.431136 PROBER > 192.168.5.77: (frag 11067:480@552) 
18:32:21.478246 PROBER > 192.168.5.78: (frag 11579:480@552) 
18:32:21.522631 PROBER > 192.168.5.79: (frag 11835:480@552) 
```

# Measuring Response Time

Lately, we’ve seen a lot of traffic coming from all over the place directed to DNS servers, but not for the purpose of querying for DNS information or ostensibly of malicious intent. What is happening is that companies have developed software that tries to deliver the best possible response time to web requests. It has been demonstrated that most users will tolerate about an eight-second delay in receiving responses and after that they might go to a competitor site with better response time. It has become a matter of e-business survival and profitability to offer good response time, and because necessity is the mother of invention, software has been created to accomplish the mission. The patterns explained in this section are from a product known as 3DNS.

One technique is to associate the user request with an authoritative DNS server for the user’s host and find the response time to the DNS server. This assumes that the authoritative DNS server and the user’s hosts are geographically close, which might not always be the case. Why not just find the distance to the user’s host? Indeed, this seems more logical, but many sites are well protected, and access to the user’s host is not always available. They figure there is a better chance of having some kind of access to the DNS server, which may or may not be the case.

There has been a lot of hue and cry from analysts who see their IDS fired because of the traffic generated by this software. Many sites feel violated because traffic is directed to the sacred DNS server, of all hosts. And, many more sites don’t understand what is happening and perceive this activity to be an attack of some sort. The final objection is that this is unauthorized information gathering, regardless of whether it benefits the end user.

Let’s take a look at some of the signatures associated with this type of traffic. One thing that you should keep in mind is that many different web sites use this software and so you will see many different source IPs. Because of the unique signatures generated from multiple source IPs, this has been mistaken for some kind of coordinated attack. As you will see, however, it really isn’t.

## Echo Requests

No surprise with the following TCPdump activity to measure response time to your DNS server. The echo request is issued and the response time is measured based on receipt of an ICMP echo reply, if there is one:

```
10:25:44.070000 216.32.68.13 > mydns.com: icmp: echo request 
10:25:44.070000 216.32.68.13 > mydns.com: icmp: echo request 
10:25:44.070000 216.32.68.13 > mydns.com: icmp: echo request 
10:30:01.530000 216.32.68.13 > mydns.com: icmp: echo request 
10:30:01.530000 216.32.68.13 > mydns.com: icmp: echo request 
10:30:01.550000 216.32.68.13 > mydns.com: icmp: echo request 
10:30:25.660000 209.67.29.8 > mydns.com: icmp: echo request 
10:30:25.660000 209.67.29.8 > mydns.com: icmp: echo request 
10:30:25.670000 209.67.29.8 > mydns.com: icmp: echo request 
10:32:12.520000 209.67.78.200 > mydns.com: icmp: echo request 
```

As you have learned, however, many sites block ICMP echo requests because ICMP has capability to map sites both actively with a ping, and also by eliciting error messages that give away the position of hosts and routers in a site. And, if this is the case, an attacker, or even a service provider using a tool like 3DNS might focus their reconnaissance on the DNS server.

## Actual DNS Queries

If the user’s DNS server didn’t respond to the ICMP echo request and the server using the 3DNS probing software is configured to continue to try to make contact with the DNS server, more activity is sent, as shown here:

```
216.32.68.11.3200 > mydns.com.53: 0 [0q] Type0 (Class 0)?. (36) 
mydns.com.53 > 216.32.68.11.3200: 0 FormErr [0q] 0/0/0 (12) DF 
216.32.68.11.3201 > mydns.com.53: 256 [0q] Type0 (Class 0)? . (36) 
mydns.com.53 > 216.32.68.11.3201: 0 FormErr [0q] 0/0/0 (12) DF 
216.32.68.11.3202 > mydns.com.53: 512 [0q] Type0 (Class 0)? . (36) 
mydns.com.53 > 216.32.68.11.3202: 0 FormErr [0q] 0/0/0 (12) DF 
```

A real DNS query is not issued, but one is sent to UDP port 53 with a DNS message of all 0s. TCPdump performs some integrity checking of the DNS message and if it discovers what it considers to be noteworthy fields, it reports them. The `0q` means that there were zero queries in the DNS message, for example. Normally, for types other than inverse queries there will be at least one query. That is why TCPdump reported it and all other 0-padded fields it considers to be odd. This elicits an error response from mydns.com, which is then used to compute the round-trip time.

## Probe on UDP Port 33434

Here is yet a third type of activity directed at the DNS server if the others have failed:

```
209.67.78.203.3310 > mydns.com.33434: udp 36 [ttl 1] 
209.67.78.203.3311 > mydns.com.33434: udp 36 (ttl 2) 
216.32.68.10.3307 > mydns.com.33434: udp 36 [ttl 1] 
216.32.68.10.3308 > mydns.com.33434: udp 36 (ttl 2) 
216.32.68.10.3307 > mydns.com.33434: udp 36 [ttl 1] 
216.32.68.10.3308 > mydns.com.33434: udp 36 (ttl 2) 
209.67.78.200.3411 > mydns.com.33434: udp 36 [ttl 1] 
209.67.78.200.3412 > mydns.com.33434: udp 36 (ttl 2) 
```

This output is much like you might see with a UNIX traceroute. Traceroute has the signature of attempting a UDP connection to a high-numbered port in the 33000+ range, such as seen here. This is slightly different because the standard implementation of traceroute uses incrementing destination ports. These are to static UDP destination port of 33434. The anticipated response will be a port unreachable error, in which case response time can be computed when the 3DNS software receives the response. The incrementing TTL values can also be a signature of Traceroute, if the DNS server is inside the sensor that captured this activity.

## 3DNS to TCP Port 53

A final attempt to establish a connection to TCP port 53 is made if all others fail. This attempt differs from most SYN connections because you will see that 64 bytes have been included in the payload. Normal traffic has no payload until after the three-way handshake has been completed. The 64 data bytes are sent to approximate a reasonable-sized payload, one that is neither too small nor too large. The anticipated response will be either a SYN/ACK from a listening server or a RST/ACK from one that is not listening:

```
209.67.78.202.2202 > mydns.com.53: S 997788921:997788985(64) win 2048 
209.67.78.202.2200 > mydns.com.53: S 869896644:869896708(64) win 2048 
209.67.78.202.2201 > mydns.com.53: S 1386586413:1386586477(64) win 2048 
216.32.68.11.3102 > mydns.com.53: S 765045139:765045203(64) win 2048 
216.32.68.11.3100 > mydns.com.53: S 865977968:865978032(64) win 2048 
216.32.68.11.3101 > mydns.com.53: S 565178644:565178708(64) win 2048 
```

This approach seems destined to fail for many sites, especially if this is the final attempt when all others have failed because of blocked access to the other methods. The problem is that most security-conscious sites block access to TCP destination port 53 because that can be used to download the DNS maps that contain all registered hosts and their IP numbers. Therefore, if traffic is blocked, perhaps they could do the measurements from an ICMP unreachable received from the router blocking the access. What if the block was done by a router that has been silenced from delivering host unreachable errors? This is just as fruitless as the other failed attempts.

# Worms as Information Gatherers

If all users at your site share a common mail server, and it is configured to examine mail for viruses that have been identified, many might be eliminated before they can infect the target host. But, users might not all use the same mail server; they might not run virus eradication software; and if they do, they might not update it frequently. This increases the risk of infection.

Viruses and worms have not been viewed conventionally as information gatherers. We are starting to see a new class of worm that acts as some kind of agent to harvest or seek information. This might involve attempting connections to other hosts after a host has been infected. If this is the case, and there is some kind of IDS at an egress point of the infected host, we can observe the activity. Two such worms are examined here: Pretty Park and RingZero.

## Pretty Park Worm

I was reviewing an alert about outbound blocked activity at one of our sites and discovered that an internal host was attempting to connect to an Internet Relay Chat (IRC) port 6667 on many different destination IPs. This site had blocked outbound activity to many of the conventionally used IRC ports just because the site was hard pressed to find redeeming quality in many. I’m sure it can be argued that there are many reputable and upstanding chat rooms, but often times users gravitate to ones that aren’t work related. And, every summer when the new crop of cyber-connected summer students arrived, this site usually saw a couple of them try to engage in IRC activity and fail.

It was late February, a Friday afternoon to be exact, and I was seeing this activity. I reported it to the appropriate contact, and he said that he had informed the owning administrator of the detected activity. I also dumped logs of the rejected outbound activity, but didn’t give them much scrutiny. Had I been more thorough, I would have discovered that the host was attempting connections to IRC sites about five times a minute. This either reflects an obsessive-compulsive desire to connect or an automated program.

On the following Monday, I received another alert about outbound IRC activity—no big deal. I just thought it was the same host I had already identified trying once again. But, I searched the logs again and found four more hosts engaged in similar activity. The scary part was that they were all going to the same destination hosts, many of them in foreign countries. And, so the inevitable thought of horror arose in my paranoid analyst’s brain: We had suffered multiple compromises using a common vulnerability, and the intruder was trying to contact her home base to report the triumph. Another, more comforting (compared to a compromise) thought occurred that maybe there was some kind of worm infection.

Sure enough, when my Windows-savvy coworker examined one of the infected hosts, he located some strange programs running (FILES32.VXD and PRETTY PARK.EXE) and identified this as the Pretty Park worm. Using netstat, he discovered that the host had sent a TCP SYN to destination port 6667. Apparently, Pretty Park is a worm that arrives via an email attachment and one of the duties of the worm is to go to these IRC sites in hopes of sending back information about the hosts—things such as passwords and details about the infected host. You can get a more thorough description of Pretty Park at [http://vil.nai.com/vil/wm98500.asp](http://vil.nai.com/vil/wm98500.asp).

Here is an excerpt of the activity captured by TCPdump. The destination port is 6667, and the destination hosts change:

```
09:30:34.470000 infected.com.1218 > ircnet.grolier.net.6667: S 
662405:662405(0) Âwin 8192 (DF) 
09:30:37.370000 infected.com.1218 > ircnet.grolier.net.6667: S 
662405:662405(0) Âwin 8192 (DF) 
09:30:43.370000 infected.com.1218 > ircnet.grolier.net.6667: S 
662405:662405(0) Âwin 8192 (DF) 
09:30:55.370000 infected.com.1218 > ircnet.grolier.net.6667: S 
662405:662405(0) Âwin 8192 (DF) 
09:31:04.050000 infected.com.1220 > irc.ncal.verio.net.6667: S 
691990:691990(0) Âwin 8192 (DF) 
09:31:06.970000 infected.com.1220 > irc.ncal.verio.net.6667: S 
691990:691990(0) Âwin 8192 (DF) 
09:31:12.970000 infected.com.1220 > irc.ncal.verio.net.6667: S 
691990:691990(0) Âwin 8192 (DF) 
09:31:24.970000 infected.com.1220 > irc.ncal.verio.net.6667: S 
691990:691990(0) Âwin 8192 (DF) 
09:32:34.130000 infected.com.1222 > mist.cifnet.com.6667: F 
722101:722101(0) ack 1426589426 win 8680 (DF) 
09:32:43.070000 infected.com.1224 > krameria.skybel.net.6667: S 
782083:782083(0) Âwin 8192 (DF) 
09:32:55.070000 infected.com.1224 > krameria.skybel.net.6667: S 
782083:782083(0) Âwin 8192 (DF) 
09:33:04.170000 infected.com.1226 > zafira.eurecom.fr.6667: S 
812112:812112(0) Âwin 8192 (DF) 
```

The lesson here is that the theory of fusing host-based and network-based software yields the best results.

On the host-based side, we would like to believe that worm-eradication software prevents infection, but this doesn’t work for all hosts. Detection was network-based in this case because logging the denied traffic was what identified a possible problem.

## RingZero

Another worm, a Trojan horse known as RingZero, that sent out network traffic was discovered in September 1999. The first identified traffic pattern associated with RingZero was a Shadow detect of a scan of many different hosts for TCP port 3128, the squid proxy server port. Here is a sample of the captured activity seen by Shadow:

```
12:29:48.230000 4.3.2.1.1049 > 172.16.54.171.3128: S 9779697:9779697(0) win 
8192 Â<mss 1460> (DF) (ttl 19, id 9072) 
12:29:58.070000 4.3.2.1.1049 > 172.16.54.171.3128: S 9779697:9779697(0) win 
8192 Â<mss 1460> (DF) (ttl 19, id 29552) 
12:30:10.960000 4.3.2.1.1049 > 172.16.54.171.3128: S 9779697:9779697(0) win 
8192 Â<mss 1460> (DF) (ttl 19, id 39792) 
12:44:54.9600001.2.3.4.3243 > 172.16.187.212.3128: S 356330349:356330349(0) 
win Â8192 <mss 1460> (DF) (ttl 242, id 962) 
12:44:57.930000 1.2.3.4.3243 > 172.16.187.212.3128: S 356330349:356330349(0) 
win Â8192 <mss 1460> (DF) (ttl 242, id 11714) 
12:45:03.930000 1.2.3.4.3243 > 172.16.187.212.3128: S 356330349:356330349(0) 
win Â8192 <mss 1460> (DF) (ttl 242, id 22466) 
12:45:15.930000 1.2.3.4.3243 > 172.16.187.212.3128: S 356330349:356330349(0) 
win Â8192 <mss 1460> (DF) (ttl 242, id 33218) 
12:46:13.070000 1.1.1.1.2262 > 172.16.99.110.3128: S 20315949:20315949(0) win 
Â8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 116, id 35676) 
12:46:16.080000 1.1.1.1.2262 > 172.16.99.110.3128: S 20315949:20315949(0) win 
Â8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 116, id 46428) 
12:46:22.070000 1.1.1.1.2262 > 172.16.99.110.3128: S 20315949:20315949(0) win 
Â8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 116, id 57180) 
12:46:34.080000 1.1.1.1.2262 > 172.16.99.110.3128: S 20315949:20315949(0) win 
Â8192 <mss 1460,nop,nop,sackOK> (DF) (ttl 116, id 2397) 
```

Three hostile hosts (1.1.1.1, 1.2.3.4, and 4.3.2.1) scanned different internal 172.16 hosts for port 3128. When an additional investigation was performed, it was discovered that the scanning host also attempted connections to destination ports 80 (HTTP) and 8080 (alternate HTTP). Shadow filters don’t look for those destination ports because they are likely to trigger a lot of false positives. A lot of sites saw similar activity, and it appeared to be coming from many different source hosts from all over the world with as many as a half dozen different scans per hour. Most of these scans hit destination addresses that didn’t exist, indicating that no prior reconnaissance had been done or it hadn’t been done well.

One theory concluded this was from one host that was just spoofing source IPs. In the preceding scan output that was executed with the TCPdump **–vv** option, (this is the reason you see the additional information in parenthesis), the TTL value is displayed. The **–vv** option also displays a field known as the IP identification number that appears as “id #.” If this activity were all from one spoofed source IP, the arriving TTL value should have remained relatively constant unless it was being crafted.

When traceroutes were attempted back to many of the source IP addresses, the hop counts to get from my site back to the alleged source IP appeared credible. If you can estimate the initial TTL assigned by the source IP and figure out the difference between that and the arriving TTL, you can approximate the hop counts. The difficulty is guessing the initial TTL. If you look at the chart found at [www.honeynet.org/papers/finger/traces.txt](http://www.honeynet.org/papers/finger/traces.txt), most times you can figure out a reasonable initial TTL.

Not only were the hop counts believable, but all the source IPs appeared to be alive and pingable, something not typically found with randomly pirated source IPs. Finally, in the preceding scan, notice that the final scanning IP, 1.1.1.1, has different TCP options (nop, nop, sackOK) from the other records. This points more to the source’s hosts being genuinely different and real, rather than a crafter taking the time to artificially introduce these differences.

In conjunction with a SANS call for help in determining the cause of these scans, a very astute network administrator, Ron Marcum of Vanderbilt University, discovered a PC on his network scanning hosts on other networks looking for ports 80, 8080, and 3128. The RingZero Trojan appeared to be the culprit. It looked for any hosts that were using open proxy servers found on ports 3128, 80, or 8080 and, at least for a while, collected ones it did find on an FTP site. There is value in knowing where an open proxy server is; it enables hackers to hide their true source IP identities. Open proxy servers enable you to tunnel through them and assume that IP number as the source IP. Some questions still remain about RingZero; it is not known how the Trojan infects a particular host, and it has not been determined what IPs the Trojan scans when downloaded.

# Summary

The attacker community is investing an incredible amount of effort to scan the Internet. The single most important service for your site to block is ICMP echo requests. Reconnaissance probes should be taken seriously; if attackers can learn where your hosts are, they can make fairly short work of determining what services these hosts run. If they cannot determine which of the hosts in your network address space are active, they have a very sparse matrix with which to work. One great defense is to use RFC 1918 private address space instead of using public address space. If you have public address space and do not have split horizon DNS, attackers can just ask your DNS server where your hosts are with reverse lookups. Also, when possible, a NAT is a fantastic defense against probing. I recommend several layers of NATs. Finally, try to configure your perimeter not to allow ICMP unreachable error messages out of your network.

Also, with the new class of viruses and worms being released, infiltration of your well-guarded site might come from within. This is a natural evolution of information-gathering techniques because many sites have become more proficient at shunning reconnaissance from the outside.
