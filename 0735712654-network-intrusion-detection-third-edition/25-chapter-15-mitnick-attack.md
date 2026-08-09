# Chapter 15. Mitnick Attack

![Mitnick Attack](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

In the final section of the book, we will look at automated and manual responses, and architectural and organizational issues. We will use this chapter on the Mitnick attack to serve as a transition between this higher-level material and the more fundamental material that we have already covered. The Mitnick attack is one of the most famous intrusion cases to ever occur. If you are in the intrusion business, you should be aware of the techniques used by Mitnick to attack Tsutomu Shimomura’s systems. In this chapter, we will also introduce many important issues, including reconnaissance and scanning for trust relationships. We will also consider perimeter and host defenses that are related to intrusion detection for our future discussions.

A primary source for this information is drawn from Shimomura’s post on the Mitnick attack. If you want more information on the subject, or to get expanded versions of the quotations you see here, refer to [tsutomu@ariel.sdsc.edu](mailto:tsutomu@ariel.sdsc.edu) (Tsutomu Shimomura), comp.security.misc (date: 25 Jan 1995).

# Exploiting TCP

The techniques Mr. Mitnick used were technical in nature and exploited weaknesses in TCP that were well known in academic circles, but not considered by system developers. The attack used two techniques: SYN flooding and TCP hijacking. Although SYN floods today can disable systems, the operating systems at the time of the attack, 1994, were far more susceptible to attack. The SYN flood kept one system from being able to transmit. Although it was in a mute state, the attacker assumed its apparent identity and hijacked the TCP connection. Mitnick detected a trust relationship between two computers and exploited that relationship. Surprisingly, few things have changed since then; for instance, computer systems are still set up to be overly trusting, often as a convenience to the system administrators or users.

## IP Weaknesses

A number of reconnaissance, exploit, and denial-of-service attacks take advantage of flaws in the architecture or implementation of the Internet Protocol stacks. In [Chapter 4](ch04.html), “ICMP,” we discussed the use of broadcast ICMP in both network mapping and denial of service with Smurf. In [Chapter 3](ch03.html), “Fragmentation,” we discussed penetration of perimeters with fragments as well as malicious fragmentation with gaps and illegal offsets.

Some of these are older techniques, but new attacks based on programming flaws in IP implementations are being developed all the time. The following TCPdump trace is from the SNMP test tool PROTOS, released in February 2002:

```
18:49:54.519006 10.0.0.1.59108 > 10.0.0.2.161: GetRequest(33) 
.1.3.6.1.2.1.1.5.0[len3<asnlen4294967295] (DF) 
0x0000  4500 004c 0000 4000 4011 269f 0a00 0001 
0x0010  0a00 0002 e6e4 00a1 0038 0efc 302e 0201 
0x0020  0004 0670 7562 6c69 63a0 2102 0206 9202 
0x0030  0100 0201 0030 1530 1306 082b 0601 0201 
0x0040  0105 0044 84ff ffff ff02 0100 
```

When we first ran this test against a Red Hat Linux 7.0 box, two interesting things happened: The SNMP server application on the Linux box crashed, and the Ethereal network analyzer also crashed. Why did they crash? If you notice the ASN.1 length in the square brackets at the top of the trace, you will notice it is four billion some odd bytes. That is a lot of free memory to try to allocate, and attempting to do so crashed the SNMP and Ethereal applications. As we work our way into the Mitnick attack, we will see that available memory was a major issue in that attack.

One simple way to exhaust memory that is used every day is intentionally not completing the three-way handshake. The weakness of TCP that Mitnick exploited comes from a design flaw in the early implementations of TCP stacks; however, this approach still does harm to some IP stacks.

**TCP’s Roots**

When TCP was being developed, you couldn’t purchase much memory for machines. If you could get 4 megabytes on a server, you were doing quite well. Therefore, the implementers of IP protocol stacks were very conservative.

The Internet is an outgrowth of a project from the 1970’s by the US Department of Defense *Advanced Research Projects Agency* (ARPA). The ARPANET, as it was then called, was designed to be a non-reliable network service for computer communications over wide areas. In 1973 and 1974, a standard networking protocol, a communications protocol for exchanging data between computers on a network, emerged from the various research and educational efforts involved in this project. This became known as TCP/IP or the IP suite of protocols. The TCP/IP protocols enabled ARPANET computers to communicate irrespective of their computer operating system or their computer hardware.

For further information and the source of this quotation, see

[www.ie.cuhk.edu.hk/~shlam/cstdi/history.html](http://www.ie.cuhk.edu.hk/~shlam/cstdi/history.html).

Let’s take a closer look at this memory exhaustion problem. To an application program such as ftp or telnet, sockets are the lowest layer, a programming interface to networking hardware. IP is another layer and is above sockets. TCP sits on top of IP. Because TCP is connection oriented, it has to keep state information, including window and sequence number information. A typical Internet protocol stack contains information relating to sockets. TCP is connection oriented (or stateful), so the server must keep track of all condition states and sequence numbers.

The C code below came from my Unix workstation. It can be thought of as a database record with a number of fields. The key point is that each of these fields consumes memory.

```
struct ip {
#if defined(bsd) 
                u_char  ip_hl:4,                /* header length */ 
                ip_v:4;                              /* version */ 
#endif 
#if defined(powerpc) 
                u_char  ip_v:4,                 /* version */ 
                ip_hl:4;                            /* header length */ 
#endif 
        u_char  ip_tos;                     /* type of service */ 
        short   ip_len;                       /* total length */ 
                u_short ip_id;                        /* identification */ 
                short   ip_off;                        /* fragment offset field */ 
#define IP_DF 0x3000                            /* dont fragment flag */ 
#define IP_MF 0x4000                            /* more fragments flag */ 
                u_char  ip_ttl;                 /* time to live */ 
                u_char  ip_p;                  /* protocol */ 
                u_short ip_sum;             /* checksum */ 
                struct  in_addr ip_src, ip_dst;  /* source and dest address */ 
}; 
```

The preceding header file fragment is taken from an IP header file on a SunOS 4.1.3 system. A struct—in this case, `struct ip`—can be thought of as a database record and the items inside as fields for that record. Every time a new connection is processed, these structs have to be created for socket, ip, and other protocol information. That takes memory, and lots of it. After a server replies to a SYN, it has committed memory and must keep it committed until the timer, usually set at about sixty seconds, allows the memory to be released if the connection is never established. Because memory is finite, the designers of stacks have set limits. The SYN flood attack exploits the queue size limit of the number of connections that can be simultaneously waiting to be established for a particular service. Though some modern operating systems are more resistant to these SYN flood attacks today, many are not. An unpatched Solaris 2.5 with a GB of memory will still be DoSed after 32 SYNs.

## SYN Flooding

In a modern SYN flood, the goal is simply to throw hundreds or thousands of packets per second at a server to exhaust either system resources, as we have discussed, or even network resources when the rate is high enough.

When an attacker sets up a SYN flood, he has no intention to complete the three-way handshake and establish the connection. Rather, the goal is to exceed the limits set for the number of connections waiting to be established for a given service. This caused IP stacks in the 1994 era to be unable to establish any additional connections for that service until the number of waiting connections dropped below the threshold. Until the threshold limit is met, each SYN packet generates a SYN/ACK that stays in the queue (which was generally between 5 and 10 total connections), waiting to be established. Today, queues can be much larger; ranges between 100 and 1000 are reasonable.

**SYN Floods Five Years Later**

SYN flooding was in the news in February 2000 with the famous DDoS attacks that were used against Yahoo! and other high-profile Internet sites. In the intervening years since the Mitnick attack, there have been some improvements in system networking stacks and perimeter defenses. The answer of the attackers has been simple: raise the number of SYNs by several orders of magnitude. The SYN flood described here is fairly elegant; the ones common to the Internet today are pure brute force.

Each connection has a timer, a limit to how long the system waits for connection establishment. The hourglass in [Figure 15.1](ch15.html#ch15fig01) represents the timer, which tends to be set for about a minute. After the time limit has been exceeded, the memory that holds the state for that connection is released and the service queue count is decremented by one. After the limit has been reached, the service queue can be kept full, preventing the system from establishing new connections on that port with about 10 new SYN packets per minute.

![Getting down to it.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/15fig01.gif)

**Figure 15.1. Getting down to it.**

### Covering His Tracks

Because the only purpose of the technique is to perform a denial-of-service attack, it doesn’t make sense to use the attacker’s actual Internet address. The attacker is not establishing a connection; he is flooding a queue, so there is no point in having the SYN/ACKs return to the attacker. The attacker doesn’t want to make it easy for folks to track the connection back to him. Therefore, the source address of the packet is generally spoofed. The following IP header is from actual attack code for a SYN flood. At the very bottom, notice the `dadd` and `sadd` for destination and source address, respectively:

```
/* Fill in all the IP header information */ 
        packet.ip.version=4;            /* 4-bit Version */ 
        packet.ip.ihl=5;                /* 4-bit Header Length */ 
        packet.ip.tos=0;                /* 8-bit Type of service */ 
        packet.ip.tot_len=htons(40);    /* 16-bit Total length */ 
        packet.ip.id=getpid();          /* 16-bit ID field */ 
        packet.ip.frag_off=0;           /* 13-bit Fragment offset */ 
        packet.ip.ttl=255;              /* 8-bit Time To Live */ 
        packet.ip.protocol=IPPROTO_TCP; /* 8-bit Protocol */ 
        packet.ip.check=0;              /* 16-bit Header checksum (filled in 
below) */ 
        packet.ip.saddr=sadd;           /* 32-bit Source Address */ 
        packet.ip.daddr=dadd;           /* 32-bit Destination Address */ 
```

As the following code fragment shows, this technique even uses an error-checking routine to make sure the address chosen is routable, but not active. When the attacker enters an address, the attack code pings the address (notice the `slickping` line in the following code fragment) to ensure it meets these requirements. If the address is active, it sends a RESET when it receives the SYN/ACK for the system under attack. When the target system receives the RESET, it releases the memory and decrements the service queue counter, rendering the attack ineffective. From an intrusion-detection standpoint, these bogus packets assembled for the purpose of attacking and probing can be called *crafted packets*. Quite often, the authors of software that craft packets make a small error at some point, or take a shortcut, and this gives the packet a unique signature. You can use these signatures in intrusion detection. When you detect evidence of a crafted packet, you know the sender is up to something. Take a look:

```
case 3: 
                                if(!optflags[1]){
                                        fprintf(stderr,"Um, enter a host 
                                        first\n"); 
                                        usleep(MENUSLEEP); 
                                        break; 
                                } 
                                                /* Raw ICMP socket */ 

if((sock2=socket(AF_INET,SOCK_RAW,IPPROTO_ICMP))<0){
                                        perror("\nHmmm.... socket 
                                        problems\n"); 
                                        exit(1); 
                                } 
                                printf("[number of ICMP_ECHO's]-> "); 
                                fgets(tmp,MENUBUF,stdin); 
                                if(!(icmpAmt=atoi(tmp)))break; 
                                if(slickPing(icmpAmt,sock2,unreach)){
                                        fprintf(stderr,"Host is reachable... 
                                        Pick a new one\n"); 
                                        sleep(1); 
```

Now you have a technique to use as a generic denial of service. You hit a target system with SYNs until it cannot speak (establish new connections). Systems vulnerable to this attack can be kept out of service until the attacker decides to go away and SYN no more. In the Mitnick attack, the goal was to silence one side of a TCP connection and masquerade as the silenced, trusted party.

What would attackers use today to accomplish the same thing? Any good current denial-of-service tool—for instance, an attack against Windows computers that has been pretty effective is jolt.c, based on malicious oversize ICMP messages.

### Identifying Trust Relationships

So how did Mitnick identify which system to silence? How did he confirm a trust relationship existed? It turns out that many complex attacks are preceded by intelligence gathering techniques, or *recon probes*. Here are the recon probes detected by TCPdump, a network-monitoring tool developed by the Department of Energy’s Lawrence Livermore Lab and reported in Tsutomu’s post.

“The IP spoofing attack started at about 14:09:32 PST on 12/25/94. The first probes were from toad.com.” (This information was derived from packet logs.)”

```
14:09:32 toad.com# finger -l @target 
14:10:21 toad.com# finger -l @server 
14:10:50 toad.com# finger -l root@server 
14:11:07 toad.com# finger -l @x-terminal 
14:11:38 toad.com# showmount -e x-terminal 
14:11:49 toad.com# rpcinfo -p x-terminal 
14:12:05 toad.com# finger -l root@x-terminal 
```

Each of the commands shown—`finger`, `showmount`, and `rpcinfo—`can provide information about UNIX systems. If you work in a UNIX environment and haven’t experimented with these commands in a long while, it might be worthwhile to substitute some of your machine names for target, server, and x-terminal to see what you can learn. Here is the information you can glean from the following commands:

- **`finger`.**tells you who is logged on to the system, when they logged on, when they last logged on, where they are logging on from, how long they have been idle, whether they have mail, and when their birthday is (well, scratch the birthday). The analogous command for Microsoft Windows systems is **NBTSTAT**. finger Example: [root@toad /tmp]# finger @some.host.net [some.host.net] Login Name TTY Idle When Where chap Bill Chapman x1568 pts/6 3:11 Tue 17:26 picard chap Bill Chapman x1568 console 8:39 Mon 14:44 :0 [root@toad /tmp]#
- **`showmount -e`.**provides information about the file systems mounted with *Network File System* (NFS). Of particular interest to attackers are file systems that are mounted world readable or writable—that is, available to everyone. showmount Example: [root@toad /tmp]# showmount -e some.host.net Export list for some.host.net: /usr export-hosts /usr/local export-hosts /home export-hosts [root@toad /tmp]#
- **`rpcinfo`.**provides information about the remote procedure call services available on a system. `rpcinfo –p` gives the ports where these services reside.

```
rpcinfo  Example 
[root@toad /tmp]# rpcinfo -p some.host.net 
   program vers proto   port 
    100000    3   udp    111  rpcbind 
    100000    2   udp    111  rpcbind 
    100003    2   udp   2049  nfs 
    100024    1   udp    774  status 
    100024    1   tcp    776  status 
    100021    1   tcp    782  nlockmgr 
    100021    1   udp    784  nlockmgr 
    100005    1   tcp   1024  mountd 
    100005    1   udp   1025  mountd 
    391004    1   tcp   1025 
    391004    1   udp   1026 
    100001    1   udp   1027  rstatd 
    100001    2   udp   1027  rstatd 
    100008    1   udp   1028  walld 
    100002    1   udp   1029  rusersd 
    100011    1   udp   1030  rquotad 
    100012    1   udp   1031  sprayd 
    100026    1   udp   1032  bootparam 
```

These days, most sites block TCP port 79 (finger) at their firewall or filtering router, but it might be a good idea to try this from your home ISP account— get permission *first*! Again, hopefully your site blocks TCP/UDP port 111 (portmapper), but this is worth testing as well. In recent years, so-called secure portmappers have become available either from vendors or as an external package developed by Wietse Venema, available from the Coast archive at [ftp://coast.cs.purdue.edu/pub](ftp://coast.cs.purdue.edu/pub).

### Examining Network Traces

In the case of the Mitnick attack, however, none of these ports were blocked and toad.com acquired information that was used in the next phase of the attack. The following quotation is from Tsutomu’s post:

> We now see 20 connection attempts from apollo.it.luc.edu to x-terminal.shell. The purpose of these attempts is to determine the behavior of x-terminal’s TCP sequence number generator. Note that the initial sequence numbers increment by one for each connection, indicating that the SYN packets are not being generated by the system’s TCP implementation. This results in RSTs conveniently being generated in response to each unexpected SYN-ACK, so the connection queue on x-terminal does not fill up.

As you examine the following TCPdump trace, note how it is in sets of three packets—a SYN from apollo to x-terminal, a SYN/ACK (step two of the three-way handshake), and a RESET from apollo to x-terminal to keep from SYN flooding x-terminal.

**How to Read TCPdump Traces**

```
Timestamp      Source host.Source Port   > Dst host.Dst Port: TCP
 FLAG(s) 
14:18:25.906002 apollo.it.luc.edu.1000   > x-terminal.shell: S 
SEQ NUM: ACK NUM        TCP Window Size 
1382726990:1382726990(0) win 4096 
```

The following traces begin “flooding” x-terminal. Note that the `+++`s have been added to emphasize the packet triplets:

```
+++ 
14:18:25.906002 apollo.it.luc.edu.1000 > x-terminal.shell: S 
1382726990:1382726990(0) win 4096 
14:18:26.094731 x-terminal.shell > apollo.it.luc.edu.1000: S 
2021824000:2021824000(0) ack 1382726991 win 4096 

14:18:26.172394 apollo.it.luc.edu.1000 > x-terminal.shell: R 
1382726991:1382726991(0) win 0 
+++ 

+++ 
14:18:26.507560 apollo.it.luc.edu.999 > x-terminal.shell: S 
1382726991:1382726991(0) win 4096 

14:18:26.694691 x-terminal.shell > apollo.it.luc.edu.999: S 
2021952000:2021952000(0) ack 1382726992 win 4096 

14:18:26.775037 apollo.it.luc.edu.999 > x-terminal.shell: R 
1382726992:1382726992(0) win 0 
+++ 
```

Notice the bolded value in the preceding trace. This is the sequence number if we take the second set of packets and focus on the sequence number in x-ter-minal’s SYN/ACK; it is **2021952000**. The sequence number in the preceding set’s SYN/ACK is **2021824000**. If you subtract 2021824000 from 2021952000, the remainder is 128,000. Does this represent any value? Yes, if it is repeatable. Check one more set of packets:

```
+++ 

14:18:27.014050 apollo.it.luc.edu.998 > x-terminal.shell: S 
1382726992:1382726992(0) win 4096 

14:18:27.174846 x-terminal.shell > apollo.it.luc.edu.998: S 
2022080000:2022080000(0) ack 1382726993 win 4096 

14:18:27.251840 apollo.it.luc.edu.998 > x-terminal.shell: R 
1382726993:1382726993(0) win 0 

14:18:27.544069 apollo.it.luc.edu.997 > x-terminal.shell: S 
1382726993:1382726993(0) win 4096 " 

14:18:27.714932 x-terminal.shell > apollo.it.luc.edu.997: S 
2022208000:2022208000(0) ack 1382726994 win 4096 

14:18:27.794456 apollo.it.luc.edu.997 > x-terminal.shell: R 
1382726994:1382726994(0) win 0 
```

Again, 2022208000 – 2022080000 = 128,000. So it is repeatable, or perhaps a better word is *predictable*. We know that anytime we send a SYN to x-terminal, the SYN/ACK will come back 128,000 or higher, as long as it is the next connection. With the ability to silence one side of the TCP connection and trust relationship and the ability to determine what the sequence number will be, we are almost ready to take over the trust relationship and the connection. [Figure 15.2](ch15.html#ch15fig02) shows the basic approach.

![Ready for the kill.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/15fig02.gif)

**Figure 15.2. Ready for the kill.**

## Setting Up the System Compromise?

How can this attack on a trust relationship be possible? Surely the computers would notice that the attacker has the wrong IP address. Well, the IP address is spoofed, so there would be no chance of seeing that. The time-to-live (TTL) might be a bit odd, but that is in the IP layer, and all the work is occurring at the TCP layer. The route to the system changes, so potentially it would be possible to detect something is wrong at some point in the route. However, no one is using IP options like record route, so this would never be detected. Instead, the primary focus is the sequence number. If you send a packet with the wrong sequence number, the other side sends a RESET and breaks off the connection. This is why it mattered that in the Mitnick attack, x-terminal had a predictable sequence number. So, now we can silence one party (server) and make the other party (x-terminal) believe we are that party (server). What happens next? Again, we return to Tsutomu’s post:

> We now see a forged SYN (connection request), allegedly from server.login to x-terminal.shell. The assumption is that x-terminal probably trusts server, so x-terminal will do whatever server (or anything masquerading as server) asks. x-terminal then replies to server with a SYN-ACK, which must be ACK’d in order for the connection to be opened. As server is ignoring packets sent to server.login, the ACK must be forged as well.

Normally, the sequence number from the SYN/ACK is required to generate a valid ACK. However, the attacker can predict the sequence number contained in the SYN/ACK based on the known behavior of x-terminal’s TCP sequence number generator, and therefore can ACK the SYN/ACK without seeing it.

You can see this in the section below. In the first line x-terminal is stimu-lated by server to open the connection. Server never sees the SYN/ACK so that is why it is missing from the trace. However, he knows to add 128,000 plus 1 to the initial sequence number that x-terminal proposed when sending the SYN/ACK. After the lone ACK, the connection is open.

```
14:18:36.245045 server.login > x-terminal.shell: S 1382727010:1382727010(0) 
win 4096 
14:18:36.755522 server.login > x-terminal.shell: . ack 2024384001 win 4096 
```

Here, Mitnick exploits the trust relationship between x-terminal and server. The SYN packet is sent with a spoofed source address. The attacker sends this packet blindly; there is no way for the attacker to see the reply (short of a snif-fer planted on x-terminal or server’s network). Because Mitnick has used a fake source address, that of server, the SYN/ACK is sent to server. Server knows that it never sent a SYN packet, a request to open a connection. The proper response for server is to send a RESET and break off the connection. However, that isn’t going to happen. As shown here, 14 seconds before the main part of the attack, the server’s connection queue for the login port is filled with a SYN flood. The server cannot speak.

```
14:18:22.516699 130.92.6.97.600 > server.login: S 1382726960:1382726960(0) 
win 4096 
14:18:22.566069 130.92.6.97.601 > server.login: S 1382726961:1382726961(0) 
win 4096 
14:18:22.744477 130.92.6.97.602 > server.login: S 1382726962:1382726962(0) 
win 4096 
14:18:22.830111 130.92.6.97.603 > server.login: S 1382726963:1382726963(0) 
win 4096 
14:18:22.886128 130.92.6.97.604 > server.login: S 1382726964:1382726964(0) 
win 4096 
14:18:22.943514 130.92.6.97.605 > server.login: S 1382726965:1382726965(0) 
win 4096 
```

**The r-Utilities**

You would think that both telnet and r-utilities would have been completely replaced by a secure shell by now, but this simply is not the case. Both are still in wide use. The login service is also known as *rlogin,* and shell as *rshell*. These remote “convenience services” allow access to systems without a pesky password, which can get old if you have to enter it often. On UNIX computers, you can generally create a trust relationship for all users except root, or super user, by adding the trusted system and possibly the trusted account in a file called /etc/hosts.equiv. A root trusted relationship requires a file called /.rhosts. The r-utilities are obsolete and should not be used anymore; the secure shell service is a far wiser choice because it is harder for the attacker to exploit. In either the /hosts.equiv or the /.rhosts file, the plus sign (+) has a special meaning, that of the wildcard. For instance, a /.rhosts file with a “+ +” means to trust all computers and all users on those computers.

With the real server disabled by the SYN flood, the trusted connection is used to execute the following UNIX command with rshell: **rsh x-terminal “echo + + >>/.rhosts”**. The result of this causes x-terminal to trust, as root, all computers and all users on these computers (as already discussed). That trace is as follows:

```
14:18:37.265404 server.login > x-terminal.shell: P 0:2(2) ack 1 win 4096 
14:18:37.775872 server.login > x-terminal.shell: P 2:7(5) ack 1 win 4096 
14:18:38.287404 server.login > x-terminal.shell: P 7:32(25) ack 1 win 4096 
```

At this point, the connection is terminated by sending a FIN to close the connection. Mr. Mitnick logs on to x-terminal from the computer of his choice and can execute any command. The target system, x-terminal, is compromised:

```
14:18:41.347003 server.login > x-terminal.shell: . ack 2 win 4096 
14:18:42.255978 server.login > x-terminal.shell: . ack 3 win 4096 
14:18:43.165874 server.login > x-terminal.shell: F 32:32(0) ack 3 win 4096 
```

If Mitnick were now to leave the computer named server in its mute state and someone else were to try to rlogin, he would fail, which might bring unwanted attention to the situation. Therefore, the connection queue is emptied with a series of RESETs.

We now see RSTs to reset the “half-open” connections and empty the connection queue for server.login:

```
14:18:52.298431 130.92.6.97.600 > server.login: R 1382726960:1382726960(0) 
win 4096 
14:18:52.363877 130.92.6.97.601 > server.login: R 1382726961:1382726961(0) 
win 4096 
14:18:52.416916 130.92.6.97.602 > server.login: R 1382726962:1382726962(0) 
win 4096 
14:18:52.476873 130.92.6.97.603 > server.login: R 1382726963:1382726963(0) 
win 4096 
14:18:52.536573 130.92.6.97.604 > server.login: R 1382726964:1382726964(0) 
win 4096 
```

# Detecting the Mitnick Attack

As we have mentioned, this chapter serves double duty: to tell the story of the Mitnick attack and also to set the stage for the final section of the book. As we complete this chapter, let’s introduce the elements needed to detect and respond to an attack like this. The attack could have been detected by both host-based and network-based intrusion-detection systems. It could have been detected at several points, from the intelligence-gathering phase all the way to the corruption of /.rhosts file, when the target system was fully compromised. Intrusion detection is not a specific tool, but a capability, a blending of tools and techniques. In fact, a number of vendors, including NAI and ISS, offer hybrid systems that can perform log file analysis and packet analysis at the host system. As you read through the material in this book, you will see examples of detects by firewalls and by host-based and network-based intrusion-detection systems.

TCP spoofing is becoming harder all the time because many operating systems now randomize their initial sequence numbers, though Microsoft is a notable exception. With vulnerable operating systems, this is still a valuable technique for the more advanced attacker. SYN floods still work on many TCP stacks, although modern operating systems are much more resistant. And of course, even if a SYN flood will not work to take out one side of a trust relationship, there are denial-of-service attacks that can shut down an operating system. Much safer alternatives exist (secure shell, for example), but system administrators continue to use the r-utilities. If we cannot field a capability that enables us to detect the Mitnick attack, what can we detect? To restate, the Mitnick attack serves as an excellent indicator of intrusion-detection capability. Why make such a big deal of this? It turns out that almost a decade later, TCP hijacking is still almost impossible to reliably detect in the field with a single tool.Various products can demonstrate a detect in a lab, but the number of false alarms (false positives) in the field makes this system feature close to useless. The good news is most of the Mitnick attack was trivially detectable; so, let’s look at some ways to accomplish this.

# Network-Based Intrusion-Detection Systems

Network-based intrusion-detection systems can reliably detect the following entire recon probe trace. As an analyst, you will be tempted to ignore a single finger attempt, but the pattern in entirety really stands out and should never be ignored. Consider some of the ways network-based intrusion-detection systems might detect this recon probe:

```
14:09:32 toad.com# finger -l @target 
14:10:21 toad.com# finger -l @server 
14:10:50 toad.com# finger -l root@server 
14:11:07 toad.com# finger -l @x-terminal 
14:11:38 toad.com# showmount -e x-terminal 
14:11:49 toad.com# rpcinfo -p x-terminal 
14:12:05 toad.com# finger -l root@x-terminal 
```

## Trust Relationship

The scan is targeted to exploit a trust relationship. The whole point of the Mitnick probe was to determine the trust relationship between systems. There must have been some form of earlier intelligence gathering to determine which systems to target. If Mitnick could do this from a network, the site should be able to do the same thing, perhaps even better. Trained analysts who know their networks can often look at an attack to determine whether it is a targeted attack, but intrusion-detection systems don’t currently have this capability.

## Port Scan

Intrusion-detection systems can usually be configured to watch for a single attacker coming to multiple ports on a host. Port scans are a valuable tool for detecting intelligence gathering.You saw toad.com fire three probes to x-terminal. However, two of them (showmount and rpcinfo) will probably be directed at the same port (portmapper), which is at TCP/UDP 111. It is certainly possible to set the alarm thresholds to report connection attempts to two different ports on a host computer in under a minute. In actual practice, however, this would create a large number of false alarms. It wouldn’t take long for the analyst to give up and set the threshold higher. Therefore, a network-based intrusion-detection system probably would not detect this probe as a port scan.

## Host Scan

Host scans happen when multiple systems are accessed by a single system in a short period of time. In the example, toad.com connects to three different systems in as many minutes. Host scan detects are extremely powerful tools that force attackers to coordinate their probes from multiple addresses to avoid detection. In operational experience, we have found that one can employ a completely stupid brute-force algorithm (flag any host that connects to more than five hosts in an hour, for example) with a very acceptable false positive rate. If you lower the window from an hour to five minutes, connects to three or more hosts will still have a low false positive rate for most sites. If the intrusion-detection system can modify the rule for a host scan to eliminate the hosts or conditions that often cause false positives (for example, popular web servers, real audio, any other broadcast service), the trip threshold might be able to be set even lower than five per hour and three per five minutes. The host scan detection code in an intrusion-detection system should be able to detect the example recon probe.

## Connections to Dangerous Ports

The recon probe targets well-known, exploitable ports. For this reason, the recon probe is very close to a guaranteed detect. Network-based intrusion-detection systems can and do reliably detect connects and attempted connects to SUNRPCs. On the whole, the attacker has some advantages in terms of evading intrusion-detection systems; she can go low and slow, and she can flood the system with red herring decoys and then go for her actual target. She probably has to go after a well-known port or service to execute the exploit, however, and this is where the intrusion-detection system has an advantage. SUNRPCs are a very well-known attack point and every intrusion-detection system should be able to detect an attempt against these services.

# Host-Based Intrusion-Detection Systems

Because the attack was against a UNIX system, this review considers detecting the attack with two types of commonly used UNIX tools: TCP Wrappers and Tripwire. TCP Wrappers log connection attempts against protected services and can evaluate them against an access control list to determine whether to allow a successful connection. Tripwire can monitor the status of individual files and determine whether they were changed. When considering host-based intrusion-detection systems, you want at least these capabilities. Using tools such as PortSentry and LogSentry from [www.psionic.com](http://www.psionic.com), you can achieve an even greater level of detection and protection by watching the logs and the packets addressed to the host system.

## TCP Wrappers

TCP Wrappers or xinetd would detect the probes or attacks at the host level. For TCP Wrappers to work, you must edit the /etc/inetd.conf file to wrap the services that were probed, such as finger. It is also a good idea to add access control lists to TCP Wrappers. If a system is going to run a service such as finger, you can define which systems you will allow to access the finger daemon. That way, both the access would be logged and the connection would not be permitted. The following *fabricated* log entry shows what three TCP Wrappers finger connection events might look like on a system log facility (syslog):

```
Dec  24 14:10:29 target in.finger[11244]: refused connect from toad.com 
Dec  24 14:10:35 server in.fingerd[21245]: refused connect from toad.com 
Dec  24 14:11:08 x-terminal  in.fingerd[11066]: refused connect from toad.com 
```

One of the interesting problems with host-based intrusion detection is how much information to keep and analyze locally and how much to analyze cen-trally. This fabricated example shows that three different systems (target, server, and x-terminal) are reporting to a central log server. A single finger attempt logged and evaluated on the host computer might be ignored. Three finger attempts against three systems might stand out, however, if they were recorded and evaluated on a central or departmental log server.

An analyst would consider access attempts to portmapper higher priority than finger attempts. At the time of the Mitnick attack, secure portmappers were not widely available. This is no longer the case, and so it would be an indication of an archaic or poorly configured UNIX operating system if both logging and access control features were not available for portmap. Host-based intrusion-detection solutions should certainly detect attempts to access portmap.

## Tripwire

You could not reasonably use Tripwire to detect the recon probes. This is because it basically creates and stores a high-quality checksum of critical files, so that if the file or its attributes change, this fact can be detected. Tripwire could detect the actual system compromise, the point at which the /.rhosts file was overwritten. Unfortunately, even if the alarm goes off in near real-time, it is essentially too late. The system is already compromised, and a scripted attack can do a lot of damage very rapidly. Therefore, early detects are the best detects. If you can detect an intruder in the recon phase of his attack and determine the systems the attacker has an interest in, your chance of detecting the actual attack improves.

# Preventing the Mitnick Attack

Certainly, the attack could have been prevented at multiple points. A well-configured firewall or filtering router is remarkably inexpensive, easy to configure, and effective at protecting sites from information-gathering probes and attacks originating from the Internet. Even for its time, this site was left open to more services than was advisable.

If the recon probes and r-utilities had been blocked, it would have been much harder for the attacker, perhaps impossible. In general, a site should be blocking almost all incoming packets except for packets destined for ports that need to be open. A file that will point out some of the more dangerous ports, called the Top Twenty list, [www.sans.org/top20.htm](http://www.sans.org/top20.htm), will give you pointers on not just what to block, but also ports to watch attempts to connect to. As we will see in [Chapter 16](ch16.html), “Architectural Issues,” the perimeter is a core part of an intrusion-detection capability.

You have already read about host-based security and the use of access lists. Obviously, systems need to run services to accomplish their work efficiently, but it is often possible to specify which systems are allowed to access a particular service (for example, by using TCP Wrappers). In this case, the attacker must actually compromise a trusted host and launch the attack from that host. The Mitnick attack just had to spoof the identity of a trusted host, which is a lot easier than actually compromising the trusted host.

Even after the attack was launched, if it had been detected and responded to, it could have been stopped. In [Chapter 18](ch18.html), “Automated and Manual Response,” we will discuss ways to slow down, or even stop, an attack that is in progress.

# Summary

When doing a post mortem on a successful system compromise or attack, you can often determine that the attack was preceded by intelligence gathering “recon” probes. The harder issue is to detect recon probes, take them seriously, and increase the defensive posture of a facility or system. Many times these recon probes are used to locate and investigate trust relationships between computer systems.

Attackers often exploit a trust relationship between two computers. Many times, system administrators use such relationships as a convenience for themselves, even though they are aware that this is a “chink in the armor” for the system.

The Mitnick attack deliberately did not complete the TCP three-way handshake to SYN flood one side of the trust relationship. Many attacks and probes intentionally do not complete the three-way handshake.

Crafted packets include packets with deliberately false source addresses. These often have a signature that allows intrusion detection to detect their use.

Checking things only once is a general problem in computer security. When designing software or systems, build in the capability to check and then recheck.

The signature of TCP hijacking is that the IP addresses change during a TCP session, while the sequence numbers remain correct for the connection. Reliable detection of TCP hijacking is still beyond the reach of single-tool systems in real-world environments.

Intrusion detection is best thought of as a capability, not a single tool. The Mitnick attack serves as an excellent test case. Intrusion-detection systems that cannot detect this attack on a real-world network with a real-world load (such as a busy T-1 or higher), just mislead their users into thinking they are performing intrusion detection when in fact they are blind. Even the best intrusion-detection system will be blind to an attack that it is not programmed to detect. Many intrusion-detection analysts prefer to use systems that enable them to craft user-defined filters to detect new or unusual attacks. The next chapter presents examples of user-defined filters.
