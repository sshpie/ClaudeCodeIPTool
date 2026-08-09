# Appendix B. Denial of Service

![Denial of Service](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

In February 2000, denial-of-service attacks were the hot topic. With a network of more than 2,000 compromised systems, most of them via a DNS buffer overflow, attackers shut down major high-profile Internet sites such as CNN and eBay. Although the end of this chapter covers these attacks, they are the exception and not the rule for denial of service. In general, denial-of-service attacks groan on and on, doing little harm besides wasting people’s time and bandwidth and occasionally crashing a system. In the vast majority of these attacks, the source address is faked or “spoofed.” Please be very slow to phone the owners of the address space that you think just hit you with a denial of service and read them the riot act! One day it might be your address that is spoofed. This is a short chapter divided into two sections. The first section deals with denial-of-service brute-force attacks that are widespread and regularly detected even if they are not all that well known. The second section includes additional well-known attacks, but these are more elegant; in fact, they tend to be one-packet kills—that is, a single attacker packet that can freeze or shut down a system.

# Brute-Force Denial-of-Service Traces

These brute-force patterns have reached a point that they are known by almost all Internet institutions. The curious thing is that I still find sites and systems vulnerable to these attacks. Keep in mind that one of the characteristics of many of the denial-of-service attacks is that the attacker can use one of your systems to cause harm to someone else. The fixes are well published and well understood; *please* implement them. Only you can prevent SYN floods, UDP floods, Smurf, and Echo-Chargen!

## Smurf

The Smurf attack has no effect except to consume bandwidth. The most important thing to consider with regard to the effectiveness of Smurf is that for your site’s Internet connection to run smoothly, you depend on the security policy of other people’s sites. This is a very old attack, but you still see it deployed with the most current attack tools. Smurf is still deployed for exactly one reason: It still works. In the following case, `spoofed.pound.me.net` almost certainly did not really send the echo request to `192.168.1.255`. Instead, an outside computer interjects this into the network, as shown in [Figure B.1](apb.html#app02fig01). The poor spoofed addressee will potentially get hit with a large number of ICMP echo replies. If spoofed is on a slow Internet connection, this might be harmful; and if a large number of hosts reply to the Smurf, damage can be done to fast networks.

![ICMP denial of service.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/apbfig01.gif)

**Figure B.1. ICMP denial of service.**

Cisco published the following field notice titled “Minimizing the Effects of ‘Smurfing’ Denial of Service Attacks.” The following quotation is from that document:

**A Scenario:** Assume a co-location switched network with 100 hosts, and that the attacker has a T1. The attacker sends, for example, a 768 kbps stream of ICMP echo (ping) packets, with a spoofed source address of the victim, to the broadcast address of the “bounce site.” These ping packets hit the bounce site’s broadcast network of 100 hosts. Each of them takes the packet and responds to it, creating 100 ping replies outbound. By multiplying the bandwidth, you see that 76.8 Mbps is used outbound from the “bounce site” after the traffic is multiplied. This is then sent to the victim (the spoofed source of the originating packets).1

1[www.cisco.com/warp/public/707/5.html](http://www.cisco.com/warp/public/707/5.html)

I chose to reference a Cisco technical manual because Cisco routers—the most widely deployed routers in the world—are one of the primary keys to eliminating Smurf attacks. Let’s examine how the attack works and then the countermeasures:

```
00:00:05.327 spoofed.pound.me.net > 192.168.15.255: icmp: echo request 
00:00:05.342 spoofed.pound.me.net > 192.168.1.255:  icmp: echo request 
00:00:14.154 spoofed.pound.me.net > 192.168.15.255: icmp: echo request 
00:00:14.171 spoofed.pound.me.net > 192.168.1.255:  icmp: echo request 
00:00:19.055 spoofed.pound.me.net > 192.168.15.255: icmp: echo request 
00:00:19.073 spoofed.pound.me.net > 192.168.1.255:  icmp: echo request 
00:00:23.873 spoofed.pound.me.net > 192.168.15.255: icmp: echo request 
```

**All for One**

Many denial-of-service attacks and network-mapping probes use broadcasts, packets addressed to all members of a network, to accomplish their purposes. RFC 919 sets several standards for broadcasts, including the rule that 255.255.255.255 must not be forwarded by a router or routing host.

How did 255.255.255.255 come to be? The local network layer can always map an IP address into a data link layer address. Think about switched networks—that is exactly how they work. So, the choice of an IP “broadcast host number” is somewhat arbitrary. Something needed to be selected, and it seemed reasonable that it should be one that was not likely to be assigned to a real host. The number whose bits are all 1s had this property. Keep the idea of all 1s in mind; we will look at patterns where the broadcast is not 255.255.255.255 due to subnet masking, but the all 1s remains true.

The address 255.255.255.255 denotes a broadcast on a local hardware network, which must not be forwarded by a router or routing host. This address might be used, for example, by hosts that do not know their network number and are asking some server for it. A common case of this is a diskless workstation; as it is booting up, it broadcasts a request for help in finding its operating system. Its server hears the request and answers, providing the next step in the boot up process and then the customized files this system needs to do its job.

Therefore, a host on net 36, for example, might do the following:

- Broadcast to all of its immediate neighbors by using 255.255.255.255
- Broadcast to all of net 36 by using 36.255.255.255

(Note that unless the network has been broken up into subnets, these two methods have identical effects.)

If the use of “all 1s” in an octet of an IP address means “broadcast,” using “all 0s” could be viewed as meaning “unspecified.” There is probably no reason for such addresses to appear anywhere but as the source address of `a bootp. bootp is` one of the protocols used to help diskless systems and routers load their operating systems and configuration files. Although there is a legacy ICMP Information Request datagram, these are obsolete and should not occur in normal traffic. As a notational convention, however, we refer to networks (as opposed to hosts) by using addresses with 0 fields. For example, 36.0.0.0 means “network number 36,” whereas 36.255.255.255 means “all hosts on network number 36.”2

2 [www.library.ucg.ie/Connected/RFC/919/7.htm](http://www.library.ucg.ie/Connected/RFC/919/7.htm)

### Directed Broadcast

If you detect a pattern such as the following 255.255.255.255, the odds are that it was sent as a simple broadcast and has been expanded by your router, as shown here:

1. A packet originally destined for 172.20.4.255 assumes a netmask of 255.255.255.0, the size of a Class C network. This broadcasts to all hosts of the 172.20.4 network.
2. A router, possibly in your organization, has the 172.20.4 interface. When it copies the packet from the Internet and rebuilds it on the 4 interface, it expands the broadcast, thereby referencing all hosts served by that interface. Therefore, it rewrites to broadcast as 255.255.255.255.

In the following trace, the broadcast has been expanded. The all 1s broadcast is as described earlier, and the legacy all 0s broadcast has been expanded to the network portion of the netmask. Who answers these expanded pings? Every system that hears them! Therefore, one packet coming in from a spoofed address ends up being amplified to hundreds or thousands of packets. Sites that do not block incoming ICMP are known as *Smurf amplifiers*. You can find a listing of these, including the top 10, at [www.powertech.no/smurf](http://www.powertech.no/smurf) or [www.netscan.org](http://www.netscan.org). (In this case, it is not a great honor to be in the top 10.) Take a look at the trace:

```
05:20:48.261 spoofed.pound.me.net > 192.168.0.0:     icmp: echo request 
05:20:48.263 spoofed.pound.me.net > 255.255.255.255: icmp: echo request 
05:21:35.792 spoofed.pound.me.net > 192.168.0.0:     icmp: echo request 
05:21:35.819 spoofed.pound.me.net > 255.255.255.255: icmp: echo request 
05:22:16.909 spoofed.pound.me.net > 192.168.0.0:     icmp: echo request 
05:22:16.927 spoofed.pound.me.net > 255.255.255.255: icmp: echo request 
05:22:58.046 spoofed.pound.me.net > 192.168.0.0:     icmp: echo request 
05:22:58.061 spoofed.pound.me.net > 255.255.255.255: icmp: echo request 
```

In terms of countermeasures, you can build perimeter defenses that are denial-of-service resistant. Instead of connecting a proxy or application gateway firewall directly to your Internet connection, you might want to have a router first. After all, they are more efficient at blocking high-bandwidth attacks simply because they are designed to operate at “wire speeds.” You should also block outgoing packets that have a source address not from your network; this is known as *egress filtering*. You can find examples of egress filtering for a large number of routers and firewalls in the GCFW practical assignments at [www.giac.org/cert.php](http://www.giac.org/cert.php). Many denial-of-service attacks use spoofed source addresses. If you do not let them on the Internet, you are being a good net-neighbor. Needless to say, if one of your systems is sending out spoofed addresses, that is a clue that this box might have been compromised.

## Echo-Chargen

Echo-Chargen is another example of a classic brute-force attack that uses poorly defended sites and poorly configured systems as amplifiers. This attack mostly looks for UNIX systems as amplifiers, so it is not quite as potent as Smurf, which uses any system. You know how they depict the audiences of tennis matches on cartoons? Everybody’s head goes back and forth following the ball. This pattern is just like that except that the heads would have to oscillate at just under the speed of light. Echo is UDP port 7; if it receives a packet it echoes back the payload. If you send echo an “a,” it replies with an “a.”

Chargen (character generator) is UDP port 19. If you send Chargen any characters, it replies with a pseudo random string of characters.

In the following trace, an outsider spoofs a number of connections to various hosts’ Chargen ports. The hope here is that they will reply back to the echo port and a game of Echo <--> Chargen ping-pong will begin burning bandwidth and CPU cycles.

You can still detect this in actual use, but it is becoming more rare. You can help make it even more rare. There is no reason to allow packets addressed to these ports through your organization’s firewall or filtering router. These services should be commented out of your UNIX system’s inetd.conf files:

```
08:08:16.155354 spoofed.pound.me.net.echo > 172.31.203.17.chargen: udp 
08:21:48.891451 spoofed.pound.me.net.echo > 192.168.14.50.chargen: udp 
08:25:12.968929 spoofed.pound.me.net.echo > 192.168.102.3.chargen: udp 
08:42:22.605428 spoofed.pound.me.net.echo > 192.168.18.28.chargen: udp 
08:47:21.450708 spoofed.pound.me.net.echo > 172.31.130.93.chargen: udp 
08:51:27.491458 spoofed.pound.me.net.echo > 172.31.153.78.chargen: udp 
08:53:13.530992 spoofed.pound.me.net.echo > 172.31.146.49.chargen: udp 
```

I studied martial arts for many years and eventually became an instructor. Twice a year we would have a black belt test. The school’s master would invite other masters to form a panel for the test. Of course, it is customary to bow to these masters, and they bow back. I have a mischievous streak, and from time to time I would bow, they would bow, I would bow again, they would bow again, and so on, until they finally looked up with a pained expression and walked away. I cannot look at an Echo-Chargen trace without thinking about that little trick.

The example trace is UDP, but I have found you can make the oscillation with the TCP variant of these services as well, although I haven’t figured out how to spoof the address and make it work. For fun, if you have Cisco routers, telnet to your router’s Echo or Chargen port. For instance, `$ telnet myrouter` `7` accesses the TCP echo port. Many Cisco routers seem to have these open by default.

# Elegant Kills

Brute-force attacks tend to rely on spoofed addresses to provide a bit of cover for the attacker. One packet kills can operate with a much lower footprint. They take advantage of flaws in the IP stack’s capability to deal with illegal conditions, or even bad programming. The following sections look at several of these, including Echo-Chargen, Teardrop, Land, and a fun little attack against an adventure game called Doom.

## Teardrop

Smurf and Echo-Chargen work by brute force; Teardrop works by finesse. It takes advantage of a simple fact: Network protocol stacks are not good at math. They are especially bad at negative numbers. This is another ancient attack, and although it is still in use, I do not see it that often. My intrusion-detection students must complete a practical assignment to achieve certification. The assignment varies in the details, but essentially it is to collect and analyze about 10 network traces. Quite often, they instrument their cable modems and collect data for a while, and Teardrop shows up on many of the practical assignments. Therefore, it is still being tried. The next question is this: Does it still work? Sure, but only on unpatched or older operating systems. The following is an example of a Teardrop trace:

```
10:25:48.205383 wile-e-coyote.45959 > target.net.3964: udp 28 (frag 
242:36@0+) 
10:25:48.205383 wile-e-coyote > target.net: (frag 242:4@24) 
```

Because it has been a long time since [Chapter 3](ch03.html), “Fragmentation,” perhaps a reminder is in order. The top line shows a fragment named 242 with 36 octets of data for offset 0. The second line shows 4 more octets of data for offset 24. Therefore to service this packet, the operating system would have to rewind from 36 to 24. Negative numbers can translate to very large positive numbers, and so the operating system is likely to scribble all over some other program’s section of memory. Try this a couple times and you kill the system.

The core problem is that many IP stacks do not know how to deal with negative, or illegal, numbers. I most recently saw this when the PROTOS toolkit was released along with a CERT advisory on February 12, 2002. HD Moore, a security researcher, was running the toolkit against a Red Hat, Linux 7 box and caused a segmentation fault. We tried to look at this packet with Ethereal, but it killed Ethereal. A TCPdump trace is shown here:

```
18:49:54.519006 10.0.0.1.59108 > 10.0.0.2.161:  GetRequest(33) 
.1.3.6.1.2.1.1.5.0[len3<asnlen4294967295] (DF) 
4500 004c 0000 4000 4011 269f 0a00 0001 
0a00 0002 e6e4 00a1 0038 0efc 302e 0201 
0004 0670 7562 6c69 63a0 2102 0206 9202 
0100 0201 0030 1530 1306 082b 0601 0201 
0105 0044 84ff ffff ff02 0100 
```

Notice that, at the top of the trace, TCPdump is trying to tell us something about the Abstract Syntax Notation (ASN.1) length being over 4 billion bytes long. Even with modern systems, that is one heck of a lot of memory to allocate to a single packet. The `84ff ffff ff02` near the end of the hex dump is the value in the length field, if you were just dying to know that.

It is just a matter of time until someone finds another field in the IP stack to do this trick with.

Note that another characteristic of fragmentation is that it eludes some intrusion-detection systems that do not support packet reassembly.

## Land Attack

The Land attack is famous for two reasons: It is a very elegant one- or two-packet kill, and it is the “hello world” of intrusion-detection filters. As soon as I heard about it, I wrote a filter to detect it—after all, you cannot ask for an easier signature. But we never captured an attack. I was afraid we had made some kind of silly error in the filter, so I downloaded the attack exploit and compiled it. Now what system could I run it against? I needed something that had intrusion detection running so that I could get a trace of the attack. At that time, we had only intrusion detection in the DMZ. What about the web server? It was in the DMZ. So, I put the web server’s IP address into the exploit script, fired the exploit, and boom, the web server crashed as advertised. I hurried over to reboot the web server and never gave the experiment a second thought. Well, until our intrusion-detection analyst called. She was so excited because she had found an actual Land attack and had already reported it to our CIRT. I just kind of said, “Great job,” and spent the rest of the day quietly whistling to myself. The detect she saw is shown in the trace below:

```
12/03/97 02:19:48         192.168.1.1         80       -> 192.168.1.1 
80 
12/03/97 02:21:53         192.168.1.1         31337 -> 192.168.1.1 
31337 
```

I hope the statute of limitations for this deed has passed by the time this book gets printed.

## We’re Doomed

I love the culture I live in. First, they convince my kid to play with dolls; they just call them action figures. When he finally gets too old to play with dolls, he trades his plastic action figures in for cyber action figures. Some of the great cyber action figures, complete with horns and everything, live in the game of Doom.

Doom is played on port 666. So what is going on in the following trace?

```
12/03/97 02:19:48        0 206.256.199.8         19 -> 192.168.102.3 
666 
12/03/97 02:21:53        0 206.256.199.8         19 -> 164.256.23.100 
666 
12/03/97 02:28:20        0 206.256.199.8         19 -> 164.256.140.32 
666 
12/03/97 02:30:29        0 206.256.199.8         19 -> 192.168.18.28 
666 
12/03/97 02:30:44        0 206.256.199.8         19 -> 164.256.67.121 
666 
12/03/97 02:34:47        0 206.256.199.8         19 -> 164.256.140.32 
666 
12/03/97 02:35:28        0 206.256.199.8         19 -> 147.168.130.93 
666 
12/03/97 02:36:56        0 206.256.199.8         19 -> 192.168.18.28 
666 
12/03/97 02:39:23        0 206.256.199.8         19 -> 147.168.153.78 
666 
12/03/97 02:41:55        0 206.256.199.8         19 -> 147.168.130.93 
666 
```

Apparently, some individuals are so bored that they are spoofing a bunch of addresses, such that if these attackers chance on folks playing Doom, the Chargen output might disrupt the game in some way (and a single packet can be enough to do the trick).

The following simulated reconstructed trace shows the cause and effect of such an action, finding a Doom server. Again, 147.168.153.78 in this case is spoofed, and the activity is being caused by an unknown IP address. Although Doom traffic is becoming more rare these days, a similar game called Quake still generates a packet or two. Here is the Doom trace:

```
12/03/97 02:39:22        0 147.168.153.78       666 -> 206.256.199.8 
19 
12/03/97 02:39:23        0 206.256.199.8         19 -> 147.168.153.78 
666 
```

Actually, I had not seen this trace in a long time and was going to remove it from the material; then the following variant showed up again in January 1999. Note that the intrusion-detection system did flag this. What tips us off and lets us know that?

```
17:58:13.725824 doomer.echo > 172.20.196.51.666: udp 1024 (DF) 
17:58:13.746748 doomer.echo > 172.20.196.51.666: udp 426 (DF) 
18:03:24.133079 doomer.echo > 172.20.46.79.666: udp 1024 (DF) 
18:03:24.157238 doomer.echo > 172.20.46.79.666: udp 426 (DF) 
21:05:22.503299 dns1.arpa.net.domain > doomer.domain: 42815 (44) 
21:05:26.152327 doomer.domain > dns1.arpa.net.domain: 42815* 2/0/0 (98) (DF) 
23:50:15.728480 doomer.echo > 172.20.76.2.666: udp 1024 (DF) 
23:50:15.751821 doomer.echo > 172.20.76.2.666: udp 426 (DF) 
```

Sure! The domain lookup is a big hint! We have already discussed Echo and Chargen, and we have seen them show up together. What is going on? The attacker is bouncing off an open echo port to cover his tracks, the receiving computer will see the system with echo port in the source address field, not the attacker. The attacker spoofs the address of the target machine to a machine, and then bounces traffic off these ports onto the game. The preceding signature is a tough one; 7 to 666 is also a classic signature of a UDP flood denial-of-service program called Pepsi. However, Pepsi scanners do not usually pause for a refreshing DNS lookup.

As this discussion shows, both brute-force attacks and elegant denial-of-service attacks take advantage of flawed site and system protection. How do they know which systems to take advantage of? In some cases, attackers simply try all the addresses, hoping to get lucky. In other cases, they perform reconnaissance. One of the best tools, bar none, to do this is nmap.

# nmap

nmap is the most versatile scanner available at any price for Windows and UNIX (and the price is *free*). This software can create a large number of traces, and in early 1999 was being called the most potent denial-of-service engine available. Some of the best information about the denial-of-service effects of nmap was published by the `National Infrastructure Protection Center` `(`NIPC). NIPC produces biweekly reports called CyberNotes. Electronic copies are available on the NIPC web site at [http://www.nipc.gov](http://www.nipc.gov). CyberNotes lists specific vulnerabilities that nmap exploits. Issue 99-2, for example, reports a scan on port 427 that causes the dreaded blue screen of death on Windows 98 systems running the Novell Intranet Client. I certainly do not disagree with NIPC, but if a piece of networking software dies because it receives a packet on a certain port, we should not blame the vulnerability scanner. Packets happen. In fact, in the years since nmap was first released, many stacks have crashed, but this has forced the manufacturers to fix their products because nmap is so prevalent.

nmap is a vulnerability scanner, but it operates in several powerful modes, including some that can knock out unpatched systems. These modes include the following:

- Vanilla TCP connect() scanning
- TCP SYN (half open) scanning
- TCP FIN, Xmas, or Null (stealth) scanning
- TCP FTP proxy (bounce attack) scanning
- SYN/FIN scanning using IP fragments (bypasses packet filters)
- UDP raw ICMP port unreachable scanning
- ICMP scanning (ping-sweep)
- TCP Ping scanning
- Remote OS identification by TCP/IP fingerprinting
- Reverse-indent scanning

nmap was integrated starting with Shadow 1.6. It is great. When the analyst sees a connection to a system from the Internet that causes concern, the analyst can scan the *internal* system. Shadow’s default is to use the vanilla TCP connect, although all modes are available. The purpose is to quickly determine what services the internal system has available. And yes, from time to time when OS fingerprinting, I have crashed a system or two. I guess the good news is that it is really hard for the attackers to compromise the system if you crash it when fingerprinting it!

**Mutant Packet Arms Race**

In mid-1998, I was talking with the development team for Cisco’s vulnerability scanner, Net Sonar. Members of the team were discussing the great pains they took to avoid crashing systems while scanning them.

Today, nmap has some serious competition from hping2 when it comes to generating some seriously funky packets. I hope that an arms race does not develop between the two of them to see which can do the most harm the fastest.

# Distributed Denial-of-Service Attacks

Before the millennium rollover, I ran into a former coworker who, within the past five years, had retired from her computer-related job. After exhausting more pertinent topics, I asked her whether she planned to fly home to Nebraska for the Christmas holiday. Indeed, she was staying into the New Year. I was curious whether she had any fears about the possibility of Y2K computer problems and flying. She admitted no anxiety and asked me whether there was anything that she should be concerned about. I calmly mentioned a minor inconvenience of a massive denial-of-service against *all* infrastructure systems such as power grids, airlines, and banks continuing for days, weeks, or even years to assuage her nonexistent anxiety. Innocently enough, she replied, “What’s a denial of service?” Believe me, this is a sharp woman, and I thought nothing less of her because of her question; I just realized that my fears were based on my exposures, and her peace of mind was based on her exposures.

I believe, however, that exposure for most of the rest of the media-connected world changed with the denial-of-service attacks against some of the major Internet players, such as Yahoo! and eBay, in February 2000.You could not help but hear on the nightly news or read on the front pages of the newspapers about these attacks that felled these giants of e-commerce. Months later, the media still buzzes about the lack of consumer confidence associated with these attacks much as years ago you couldn’t read or hear about the Russian space station Mir without hearing the word “beleaguered.”

The software responsible for these and many more attacks is known as *distributed denial of service* (DDoS) because it is a denial of service originating from many different source hosts. Thankfully for us as authors and perhaps unfortunately for you as readers, we haven’t captured any traffic associated with these attacks. But, no discussion of denial of service today is respectable unless the distributed denial-of-service attacks are covered.

## Intro to DDoS

Remember the powerful Smurf attack that used an intermediate site and all its responding hosts to amplify a denial-of-service attack? That is a drop in the ocean compared to the magnitude of some of the distributed denial-of-service attacks. If you look at the architecture of the Smurf attack, you will discover that there is really one hostile origin of the attack: A malicious user at one host crafts one or many ICMP echo requests to a broadcast address of the amplification site with a spoofed source IP of the target host. Many amplification hosts can magnify the intensity of the attack.

In a DDOS attack, many different “hostile” hosts enlisted are directed to attack a target site. These so-called hostile hosts are compromised hosts that have had distributed denial-of-service software installed on them. Maybe this new public awareness about these attacks will eliminate some of the naive attitudes of “why would someone want to break into my computer…it’s got nothing worth stealing.”

DDoS software comes in many different incarnations, each with different terminology and techniques. Among all, however, there is a notion of a controlling computer that directs the compromised hosts to attack a site. Therefore, you have multiple origins of hostile hosts simultaneously attacking the victim site. The intent is to clog the portals of the victim site by consuming the resources for handling legitimate traffic. The victim site has to figure out a way to block the DDoS traffic while still allowing the legitimate traffic.

## DDoS Software

Historically, four different DDoS programs were known: Trinoo, *Tribe Flood Network* (TFN), TFN2K, and Stacheldraht (German for barbed wire). With each new release, they seem to have evolved into more complex packages with richer functionality. Most work on Linux or Solaris hosts, and TFN2K works on Windows NT hosts. Reports of new Windows-like DDoS are surfacing.

Some new terminology must be introduced. At the top of the DDoS attack, you have a host, usually known as the client, which is used by the person coordinating the attack. Next, at a layer below that, you have a host or hosts known by the term *master* or *handler*. The master controls subservient hosts to launch attacks. Finally, at the bottom, you have hosts known both as *agents* or *daemons*, which actually launch the attacks. The terminology gets tricky because it sometimes differs for the individual attacks.

### Trinoo

This software uses controlling hosts known as masters, and attacking hosts known as daemons. The communications between the client and the masters and the masters and the daemons is done using TCP and UDP. There are standard ports, but these can be altered. Trinoo can send only UDP floods to random destination port numbers on the victim host. Communications between hosts in an unaltered configuration are as follows:

```
client   → master:   destination port TCP 27665 
master   → daemons:  destination port UDP 27444 
daemons  → master:   destination port UDP 31335 
```

### TFN

[Chapter 4](ch04.html), “ICMP,” discussed TFN. Basically, there are TFN masters and daemons, which again represent the controlling hosts and the attacking hosts. The communication between master and daemon is done via an ICMP echo reply. The ICMP echo reply can direct the daemon to send a UDP flood, TCP SYN flood, ICMP echo flood, or a Smurf attack. The master can manipulate the IP identification number and payload of the ICMP echo reply to identify the type of attack to be launched. TFN can also spoof the source IP to hide the origin of the attack.

### TFN2K

TFN2K was the first of the DDoS programs to be transported to Windows. The communications between the master and agents can be encrypted and can be over TCP, UDP, or ICMP with no identifying ports. The master can spoof the source IP so that if it is detected, the real master cannot be identified. The agent can attack using a TCP SYN flood, a UDP flood, ICMP flood, or Smurf (as we saw with TFN). Additionally, the attacking agent can alternate among these types of attacks for any given attack. And, the agent-generated attack packets have a spoofed source IP by default.

### Stacheldraht

Stacheldraht is a combination of Trinoo and TFN with encryption added to communications between the client and handler and the handler and the agents. Agents can generate TCP SYN floods, UDP floods, ICMP floods, and Smurf attacks against the victim. Default communications are as follows:

```
client    → handler: TCP port 16660 or 60001 
handler   → agent:   TCP port 65000 or ICMP echo reply 
agent     → handler: TCP port 65000 or ICMP echo reply 
```

Today, since the discovery of the leaves worm with the f.exe malicious code in June 2001, the main emphasis seems to be on controlling systems from IRC channels or using flooding IRC bots. If you see traffic entering or leaving your network on TCP 6667 (actually TCP 6660–6670) you probably should consider taking a close look at it, unless you are sure the owner of the system is actually using IRC to chat.

# Summary

In denial-of-service attacks, the source address is probably spoofed. Please report them to your CIRT anyway. Many of the denial-of-service attacks are very old and well understood; this does not mean they aren’t effective. Although there is nothing impressive about Echo-Chargen, I was just talking with a major Internet service provider that lost a T3 circuit for three hours to an oscillation.

As far as DDoS attacks, you can do little right now if you become a victim site. A document is available from [www.incdents.org](http://www.incdents.org) to guide you step by step if you think one of your UNIX hosts might be infected with one of these Trojans. A wise analyst will download and read this from [www.incidents.org/react/trojan.php](http://www.incidents.org/react/trojan.php) before she has to deal with an infected system. And, you certainly can take some measures for preventing your site from becoming a launching ground. First, make sure you have egress filtering that allows packets to leave your network only if they contain source IPs from your network. There is an excellent paper on egress filtering available from Incidents.org, [www.incidents.org/protect/egress.php](http://www.incidents.org/protect/egress.php). This prevents source IP spoofing used by many of the attacks. Also, you can configure your intrusion-detection system to look for some of the signatures so that you have detection capabilities if you do become a launching site. And, as trite it sounds, you have less chance of a host compromise if you block unnecessary traffic into your sites and your hosts are well patched and maintained. This prevents the compromises necessary to install the DDoS software.
