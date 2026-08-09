# Chapter 16. Architectural Issues

![Architectural Issues](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

This chapter considers some of the tradeoffs, capabilities, and issues facing intrusion-detection system users and builders. This is a bit more theoretical than some parts of the book, but I use real-world examples to try to keep the material useful and pragmatic. We invest some time talking about *events of interest* (EOI). This is an important concept because an analyst gets better results from an intrusion-detection system if she understands what she is searching for and tunes the IDS to find it, as opposed to letting the IDS tell the analyst what to look for. We also discuss severity. All incidents are not created equal and should not be treated so. There is a great debate, a religious war in intrusion detection, about whether the sensor should be placed inside or outside the firewall. This chapter covers this and other sensor-placement issues as well.

One of the great myths that have occurred in the industry is the need to work in *real-time*. I have even seen this specified in procurement documents. What marketers mean by real-time is that intrusion-detection analysts are supposed to respond to beeps and alarms. Real-time, of course, is almost impossible, at least for human reaction, because the packet is traveling at the speed of light. [Figure 16.1](ch16.html#ch16fig01) shows the detect occurring just after real-time. The illustration was added to the book in case you ever need to point this out to your management because they are overemphasizing response time. In fact, UNIX and Windows NT computer systems do not support either real-time or even deterministic delay. We discuss these issues in push versus pull architectures, which leads into a section on the analyst console. Moreover, as we will shortly discuss, the intrusion analyst will run filters through second and even third passes over the data looking for EOI.

![Time and ID response.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig01.gif)

**Figure 16.1. Time and ID response.**

Every intrusion-detection maker falls short in providing a really great analyst interface. This is currently the primary thrust of development of course, so we will take some time to discuss the interface. What exactly does an analyst need?

The next section discusses some of the tradeoffs, or “tuning knobs,” that should be considered as you design or enhance your intrusion-detection capability. These include false positives and negatives and sensor focus.

# Events of Interest

Chapters [13](ch13.html), “Introduction to Snort and Snort Rules,” and [14, “Snort Rules Part II,”](ch14.html) introduced events of interest in the sense that when you write a filter, you design it to find something you are interested in. For instance, if you are using the Snort rule content option to find the hex pattern 0xdead or 0xbeef, a pattern that has its roots as a test pattern but is sometimes used by attackers in their code, and you come across a packet with this pattern, this is potentially an EOI. There are three main issues surrounding the subject of EOI in intrusion detection:

- The balance between false positives and false negatives
- Targeting or focusing the sensor to ensure we detect EOI
- The effects of the limits of our system on our capability to detect

The false negative/false positive problem is a serious one in intrusion detection and a lot of our energy is invested in customizing filters to detect EOI and not to generate false alarms or false positives. On the other hand, false negatives would mean missing something we would have wanted to detect. I would like to illustrate what an analyst might do with a simple example. Attackers are known to use certain strings, numbers, and hex patterns in the software they create to do reconnaissance, denial of service, or direct exploits. Some of the classics are:

- The decimal patterns 31337 and 666
- The ASCII string, skillz
- The hex patterns 0xdead and 0xbeef

Suppose we create a filter looking for hex 0xdead as shown below:

```
alert icmp  any any -> 192.168.5.0/24 any       \ 
      (msg: "0xdead hex pattern seen";             \ 
      content: "|DE AD|";) 
```

Would such a rule create false positives? Certainly it would. If the content of an ICMP packet happened to have these hex characters in this order, these simple content filters would alert. Would I want to run this rule in real-time? No, probably not. On the other hand, if we started seeing a lot of 0xdead 0xbeef, that could be significant. One of the lessons from the Shadow project was secondary analysis. Keep a couple of days of data and run programs to scrub the data looking for interesting events. I probably wouldn’t even bother manually examining a single occurrence of 0xdead or 666 in a couple of day’s worth of data, but if I saw a dozen, I would certainly think about pulling those connections and examining them.

The stories you learned about in Chapters [10](ch10.html), “Real-World Analysis,” and [11](ch11.html), “Mystery Traffic,” almost all have the same root. An analyst, looking at the data, saw something odd and said, “That’s funny.” When Judy and I were working together as active analysts for the Army and Navy respectively, we discovered a number of attacks for the first time. People would ask how we did it. I used to answer, “Pure, dumb luck.” Now you know better. We would write scripts to slice and dice that data looking for those events of interest.

Another great classic script is to take a week or so of data and search for odd protocol activity as shown in the following .bpf filter:

```
not tcp and not udp and not icmp and not igrp and not igmp 
```

You certainly would not want to run this in real-time; but, as a way to run through your data looking for events of interest that you might otherwise miss, this is obviously attractive. After you know your network and get your filter optimized, most likely you will rarely detect anything with this filter. I don’t recommend that you run it interactively and watch the results, because you might get bored and quit running it. However, if you schedule the job to run once a week and only design the system to alert you if it finds results, you have a tool that might strike pay dirt one fine day. If you are shopping for these new correlation consoles or enterprise security managers, one feature you might want to look for is the capability to schedule and run scripts to examine your data.

Now we complete our study of EOI with a consideration of overall system limitations on the lower detect limit. Let’s start with the bottom line: It is important to have a fairly clear understanding of what you are looking for and what events you are interested in, because you cannot collect or detect everything. [Figure 16.2](ch16.html#ch16fig02) shows both the data actually observable by your intrusion-detection system and the data you cannot observe.

![Sources of data.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig02.gif)

**Figure 16.2. Sources of data.**

# Limits to Observation

As shown in [Figure 16.2](ch16.html#ch16fig02), the sensor or event generator might not be able to observe all events. This is often quite a surprise for folks who pay good money for an intrusion-detection system, and they slowly find out just how limited it is in practice. What kinds of things can’t we observe?

- ****Events on a different network.****Unauthorized “backdoor” connections into a network are very common; every machine with a modem has the potential to permit a backdoor. This issue shows up prominently in advertisements for host-based intrusion-detection systems because they can make the “we’re here, we’re there, we’re everywhere” claim.
- ****Sensor is not functioning.****Events that happen right in front of the IDS, but they are not observed because the IDS is brain dead. By brain dead, I mean anywhere between hard crashed like the blue screen of death, to pingable while not functioning. A good measure of IDS reliability might mean time between having to reboot the system, because that seems to be the fix for both Windows NT- and UNIX-based systems. I have personally experienced this joy multiple times with Shadow, NFR, NID, Snort, and RealSecure. Naturally, you only discover these systems need rebooting on rainy days when they are in a different building from your analyst console. Some systems are more robust than others, of course. What is the most effective Windows NT remote management tool? A car. If the sensor’s disk fills up, this will also prevent collection.
- ****No habla SNA or SS7.****Events in a protocol that the intrusion-detection system cannot decode are not observable. What if you need an intrusion-detection system that can decode Signaling System 7 or IBM’s SNA? Is there a need for such a thing? For most of us, the answer is no; however, one fairly common event is when we detect a protocol we don’t know. For instance, I know a number of people who have detected IP Protocol 54, NHRP (Next Hop Resolution Protocol), at their DMZs and have never seen an IDS decode this.
- ****Exceeding bandwidth limit.****Events that occur above the sensor’s maximum bandwidth-handling capability cannot be observed. At some point, the sensor has to start dropping packets and we enter what analysts euphemistically call statistical sampling. If you ask network-based IDS vendors what their upper limits of speed are, you get a lot of curious answers ranging from “80Mbps” to “it depends.” *Hint:* Trust the person who says “it depends” more than the one who gives you a fixed number, especially a fixed number above T-3 speeds (45Mbps). The number of rules a sensor has to process is one primary factor in the sensor’s upper detection limit for many systems, however the primary factor is the critical path. This is the longest execution path a given packet might cause the sensor to take. If a sensor is still processing one packet when another arrives, the packet will be dropped.

To recap what was just covered, intrusion-detection systems cannot look at every possible event. The reasons for this include the following:

- The event happened on another network.
- The IDS is dead.
- The IDS has no understanding of the protocol.
- The IDS has reached its maximum bandwidth limit, or has hit critical path on a given packet and has dropped packets that came later.

The bad news is there are events we can’t even observe. The good news is that we find there are events that we can capture. Of all the packets that we can capture, some will match our filters in some way, and they are represented by the space of the inner circle. Finally, some of the total number of detects in the inner circle are valid and have value. We can refer to these as the EOI, the genuine, no-false-positive-about-it detects. They are the reason we go through all the trouble of deploying and operating intrusion-detection systems. Detecting an attack, especially a clever attack, is a lot of fun.

# Low-Hanging Fruit Paradigm

Today, the primary standard in intrusion detection is the Snort ruleset. There used to be two major rulesets, but with the present legal troubles of Max Vision, his ruleset is no longer available. It has been inspiring to watch the community come and work together to build the rules, improve the port list, and explain the vulnerabilities. In some sense, I feel like a heel saying a single word against this worthy effort, but there is a risk to us that we at least need to be aware of. We have already discussed the basic issues of false positives and negatives when we covered signatures and filters to detect signatures. Now we need to consider the effect of the low-hanging fruit paradigm on false negatives. What do we mean by the low hanging fruit?

I live on the island of Kauai. Many things are in short supply, but we certainly have enough banana trees and free range chickens. After a hurricane seven years ago, many of the chicken coops were blown apart freeing the chickens. There are no natural predators, so now the island is overrun by chickens. My neighbor recently had a bumper crop of bananas in his garden. I have never stopped to think about just how many bananas can grow on one of these trees, but it can be more than one hundred pounds. As the tree began to bend a bit with the weight of the bananas, they came in range of the chickens, at least the lower ones. They would line up under the banana tree and jump/partially fly and nip at the exposed bananas. It was quite a sight to watch and many a banana was ruined as its bottom was nipped off. So, the low hanging fruit is the easily harvested, vulnerable fruit that any one or any thing can reach.

Suppose a number of intrusion-detection vendors were secretly downloading the Snort ruleset and using this as a foundation for their own rules. What if their other major process was to go to a couple of well known sites for attack code to download the exploits to their labs, run the exploits, determine their signatures, build effective filters to detect these exploits, and then load these filters in the intrusion-detection systems we all use? If this were to happen, we would begin to establish a lowest common denominator. At first blush, that sounds like a good thing; as a consumer, you could expect any IDS to meet at least a minimum standard defined by the Snort ruleset and the most available attacks (most of which are covered in the Snort ruleset, of course). The problem is that an attacker can then analyze the Snort ruleset and craft small changes to her attacks to make them evade the IDS. If a number of commercial vendors copy these rules, this becomes an interesting problem. It allows them to treat the ruleset, a tremendous asset to the community, as low hanging fruit.

Although the preceding paragraph is partially true, there are lots of ways to mitigate the problem. Many intrusion-detection vendors and researchers culti-vate contacts with the computing underground and have access to a larger library of attacks than those commonly published. Several research efforts attempt to collect attacks and exploits and to define vulnerabilities. The problem is they use different names and descriptions. Mitre ([http://cve.mitre.org](http://cve.mitre.org)) manages a project called the *Computer Vulnerabilities and Exposures* (CVE), which enjoys broad industry support. Their goal is to develop a common nam-ing system, primarily to serve as a thesaurus for vulnerability descriptions, but also to support IDS development.

Also, it is sometimes possible to write a general filter to detect a family of exploits. We have already examined a general filter to detect web server attacks. During the discussion of that filter, you learned about a number of CGI-BIN attacks against web servers that attempt to acquire the system’s password file for offline decryption. The most famous is the phf attack. Several hundred others exist, however, including php and aglimpse. In the past, each of these had cgi-bin and /etc/passwd files somewhere in the packet, so it was possible to write a general filter to detect each of these and their cousins as well. Today, with the advent of shadow password files, we do not see many attacks against /etc/passwd; however we commonly see the following string:

```
id;uname –a; w 
```

The command **id** gives you your effective userID; the semicolon delimits different commands; **uname –a** gives the exact operating system and patch level; and finally **w** tells you who is logged on to the system. It is also possible (and very advisable) to write general filters that detect odd events (things that just shouldn’t happen) and to report them. A TCP packet with all flags set, or no flags set, and packets with unknown IP protocols are examples of these kinds of filters. Although you can increase the sensor-detection capability in many ways, the bottom line should be somewhat sobering: If an IDS depends on signatures and doesn’t have a filter to look for that signature, how will it make a detect?

# Human Factors Limit Detects

Another factor that limits the EOI we can detect and report is that people are part of the system. A typical day as an operator of an intrusion-detection system includes the recording and possible reporting of some number of detects. If you were to examine a year’s worth of detects from a site, you might find that the detects cluster as 12 IMAPs, 5 portmaps, 25 ICMP ping sweeps, 30 Smurfs, 8 mscans, 4 portscans, 5 DNS zone Xfer attempts, 4 WinNukes, and so forth. If you check the site’s Computer Incident Response Team (CIRT), you find that yup, these are the kinds of things being reported by those sites that do bother to report. So what’s wrong with this picture? Not only does the IDS fail to report many events of interest because it does not have a signature for them, many times the analyst chooses not to report many of the events that are detected.

If you were to spend a day or two on the Internet doing web searches, you could easily collect a hundred different software implementations of exploits. Some won’t compile easily, and others have limited documentation. Still others are variations on a theme. The simple fact remains, however, that you can easily collect more attacks than are commonly being detected and reported. So what’s the problem? One part of the problem is the signature issue previously discussed. If the design of the system relies on signatures and a filter doesn’t exist, the box cannot make the detect. Other factors that limit the detect capability of the system as a whole relate to the intrusion-detection analysts and the CIRTs to which they report.

## Limitations Caused by the Analyst

Part of the reason for missed detects has to be laid at the feet of the intrusion-detection analyst. There are several issues here. Sometimes, an analyst might mentally evaluate an intrusion attempt and decide it isn’t worth investigating. I have been guilty of this multiple times. Here is a classic example: Code Red is still active, because some people don’t have the gumption to patch their IIS boxes. On a given day, I see a number of detects on port 80, but I do not tend to evaluate them in depth. I just figure it is Code Red. However, in February 2002, when the Apache PHP vulnerability was reported, I had to suddenly change my ways. After all, I run Apache.

Does an analyst report something he doesn’t understand? Unknown patterns are challenging and require a significant understanding of TCP/IP and computer system processes to run to ground. What if the analyst doesn’t trust her intrusion-detection system? It takes a lot of faith to sign a report based on a little picture on a console telling you such and such just happened. It takes even more faith to do this when the same IDS reports two email Wiz attacks (Wiz is a very, very old email attack) per day and six SYN floods per hour (and these are obviously false positives). Therefore, analysts are most certainly a weak link in the system. The reasons for this include the following:

- Failing to report what the IDS detects
- Lack of training needed to investigate new attack patterns
- Lack of understanding about TCP/IP, protocols, and services
- Lack of trust in the IDS itself

## Limitations Caused by the CIRTs

Could part of the problem of missed detects be the CIRTs? If your CIRT gets a report for an IMAP, portmap, ICMP ping sweep, Smurf, mscan, portscan, DNS zone Xfer, WinNuke, or whatever, no problem. They have a database pigeonhole to put it in, and everyone is happy. If the CIRT gets a report saying, “Unknown probe type, here is the trace, whatever it is it turns my screens blue,” what do they do with that? The person getting the report is probably entry level and so there is a hassle because a database pigeonhole doesn’t exist. The advanced analysts have a lot of work to do, and the seasoned CIRT workers have been burned by a false positive or two and aren’t that likely to take action unless they get a similar report from a second source. In intrusion time, this can be a serious problem. From the moment I first heard about the klogin vulnerability in May 2000, it was less than eight hours before we were dealing with our first compromised system.

This is a serious issue because the CIRT is almost certainly understaffed. Real people are on the phone begging for help because their systems are compromised and their organization never had the funding to take security seriously. Real people screaming for help with compromised systems has to take priority over unknown probe types that turn screens blue. At the end of the month or quarter or whatever, the CIRT puts out their report: We logged this many portmaps, ICMP ping sweeps, Smurfs, mscans, portscans, DNS zone Xfers, WinNukes, and so forth. The new analyst who reported the unknown probe type sees that the report makes no mention of the unknown probe, shakes her head, and silently decides, never again. The analyst doesn’t know whether the CIRT thinks she is nuts or whether the CIRT just doesn’t care. This is why we made a conscious choice with Incidents.org, an all volunteer CIRT and analysis organization, to be willing to post a new pattern before the whole world and write as our commentary, “We have no idea what this is, can anybody help us?” More than once I have been embarrassed by the answer, because it was a pattern I should have known. Over time, that has led us to act more like a conventional CIRT, to be cautious about what we post, to wait until we know more. This keeps the word from getting out, and may allow an attack more time before we understand it well enough to detect it and defend against it. We know we shouldn’t clam up, but it is hard to fight human nature.

A brief recap of EOI is now in order. We cannot observe every event. Of the things that we can observe, some are dismissed as unimportant when in fact they are attacks—these are the false negatives. Others are flagged as attacks when they aren’t—these are the false positives. The goal of the system designer and intrusion-detection analyst should be to maximize the events that can be observed while minimizing the false positives and negatives. A number of systems and program design issues arise here, but there are also human issues to consider. Although complete efficiency might never be achieved, you should accept nothing less as your goal.

# Severity

Several schools of thought propose ways to reduce severity to a metric, a number we can evaluate. This section discusses some of the primary factors that should be used to develop such a number. Let’s start, however, with a basic philosophical principle: Severity is best viewed from the point of view of the system (and its owners) under attack. This is an important principle because the further removed the evaluator is from a given attack, the less severe it is (at least to the evaluator).

**It Happens All the Time**

The intrusion-detection team that I worked with for several years was once invited to spend the day with a very large CIRT. The CIRT had an analysis team that had just accepted delivery of a spiffy new intrusion-detection capability, an analyst interface that could watch a large number of sensors. We all thought it might be interesting to sit with the Shadow team analysts at this CIRT’s workstations and see how effective they could be with the new spiffy interface. Within four minutes, one of the Shadow analysts had found a signature indicating a root-level break-in to one of our sister sites. She wanted to call the site and tell them, but the CIRT workers laughed and said, “It happens all the time.” No doubt that was true from their perspective. These folks operate well over a hundred sensors of their own in addition to all the reports they receive. They probably deal with more compromises in a year than I will experience in my entire working career. The trip still seems odd to me, however, because I know how much trouble and pain a compromised system can be to the system owners and those who have to assist them. Severity is best viewed from the point of view of the system under attack and its owner(s).

Although we do want to keep the human element in mind as we discuss the severity of attacks, we need to be able to sort between them so that we can react appropriately. At every emergency room, there is an individual in charge of triage, making sure that care is given to those who need it the most. This way, a patient with an immediate life-threatening injury doesn’t have to wait while the medical personnel attend to a patient with a stubbed toe. In a large-scale attack response, resources become scarce very quickly, so an approach to triage for computer assets is required. [Figure 16.3](ch16.html#ch16fig03) introduces this concept at a high level.

![Severity at a glance.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig03.gif)

**Figure 16.3. Severity at a glance.**

Are nontargeted exploits for vulnerabilities that do not exist within your computer systems actually no-risk? When you study risk more formally, you will learn that part of the equation is your level of certainty; how sure are you that none of your systems have the vulnerability? I tend to be on the conservative side. In the examples that follow, I consider nontargeted, nonvulnerable exploits to be of no risk only if they are also blocked by the firewall or filtering router. In fact, there is a sense in which this is negative risk. The attacker using a nontargeted script exploit against a well-secured site is at a higher risk than the site because the attack will be reported. If the attacker succeeds in breaking in and doing damage somewhere else, the odds are at least fair that he can be tracked down.

What might be a reasonable method to derive a metric for severity? What are the primary factors? How can we establish an equation? How likely is the attack to do damage? And, if we sustain damage, how bad will it hurt? Clearly, these are all factors.

## Criticality

How bad will it hurt is one of the most important issues to consider in risk management. I was giving a talk in Washington, DC and wanted to make a point about anti-virus and personal firewalls so I asked, “How many of you travel multiple times a year?” Most of the hands went up, which makes sense for a government headquarters crowd. Then I asked, “How many of you carry Cipro?” Cipro is the antibiotic that was prescribed during the Anthrax attacks. Because there had not been an anthrax attack since October 2001, nobody was thinking about that. However, I can just imagine what would happen if I were in a strange city and started feeling the worst case of the flu in my entire life. How would I get access to top-quality medical care? At home, I have my doctor, who knows me, and a medical record and friends that are doctors. In Houston, or Seattle, or New York City, the answer is go to the emergency room. Do you know that it is not impossible to wait 12 hours just to be seen in an emergency room? How bad will it hurt? This is the question that should drive us. Now, just so you don’t think I am totally off my rocker for carrying Cipro, I also travel internationally a lot, and though I try not to drink the water and to cook it, peel it or forget it, having something like Cipro is an important tool if things go wrong. What does any of this have to do with antivirus or a personal firewall? If you don’t have these things and you are exposed, you are in a heap of trouble, just like anthrax and no Cipro.

It would be bad for me to be poisoned with anthrax, but it would be so much worse for the President of the United States to be poisoned with it. The major determinant for “how bad will it hurt?” is how critical the target is. If a desktop system is compromised, it is bad in the sense that time and work might be lost. Also, that system could be used as a springboard to attack other systems. If an organization’s *domain name system* (DNS) server or email relay is compromised, however, a much more serious problem exists. In fact, if an attacker can take over a site’s DNS server, the attacker might be able to manipulate trust relationships and thereby compromise most or all of a site’s systems. When developing a metric, we need a way to quantify criticality. We can use a simple five-point scale, as follows:

|  |  |
| --- | --- |
| 5 points | Firewall, DNS server, core router |
| 4 points | Email relay/exchanger |
| 2 points | User UNIX desktop system |
| 1 point | MS-DOS 3.11 |

## Lethality

The lethality of the exploit refers to how likely the attack is to do damage. Attack software is generally either application or operating system specific. A Macintosh desktop system isn’t vulnerable to a UNIX tooltalk buffer overflow, or an rcp.statd attack. A Sun Microsystems box running unpatched Solaris might quickly become the wholly owned property of Hacker Incorporated if hit with the same attacks. As an intrusion-detection analyst, I get nervous when an attacker can go after a specific target with an appropriate exploit. This is an indicator that the attacker has done his homework with recon probes and that we are going to have to take additional countermeasures to protect the target. Again, a five-point scale applies:

|  |  |
| --- | --- |
| 5 points | Attacker can gain root across network. |
| 4 points | Total lockout by denial of service. |
| 4 points | User access (via a sniffed password, for example). |
| 1 point | Attack very unlikely to succeed (Wiz in 2002, for example). |

The last example, 1 point for Wiz, introduces a really important point when calculating severity, and that is the effect of time. This is known as the lethality curve. The attackers have a term they call zero day, and it references an attack that works before it is publicly known. The exploit works fine, but it is tightly held by a fairly small number of people who are breaking into systems with it. This is a time of extreme lethality, but the number of uses is fairly low.

Eventually, the attack is discovered and published. Now the community knows about it and so do the attackers. We enter a race condition—attackers race to get the exploit, learn to use it, and attack our systems. Defenders rush to apply patches, download new IDS signatures, or implement other countermeasures. During this phase, the attack is still pretty lethal, but the lethality is dropping; however, the incidence of attack attempts goes way up. Finally, we reach the crest of the wave. More and more defenders are patching their systems and applying other countermeasures, and over time, the attack becomes less and less destructive.

# Countermeasures

What about firewalls or system patches or operating systems running from CD-ROMs? Countermeasures certainly affect severity and can logically be divided into system countermeasures and network countermeasures.

The five-point scale for system countermeasures is as follows:

|  |  |
| --- | --- |
| 5 points | Modern operating system, all patches, added security such as TCP Wrappers and secure shell |
| 3 points | Older operating system, some patches missing |
| 1 point | No TCP Wrappers/allows fixed unencrypted passwords |

The five-point scale for network countermeasures is as follows:

|  |  |
| --- | --- |
| 5 points | Validated restrictive firewall, only one way in or out |
| 4 points | Restrictive firewall, some external connections (modems, ISDN) |
| 2 points | Permissive firewall (The key question is this: “Does the firewall allow the attack through?”) |

# Calculating Severity

Analysts trained in the GIAC approach to intrusion detection use the following formula to calculate severity:

```
(Criticality + Lethality) - (System + Net Countermeasures) = Severity 
```

Take a look at a couple examples. These are taken from the practical project required to achieve GIAC Intrusion Analyst certification. To put the examples in context, the entire analysis process is shown, even though the current focus is on severity.

The approach described here helps reinforce that attacks vary in severity. This discussion examines some of the factors that affect severity. You can cite these factors to help others understand when they ask, “What is it about? This attack that has you spun up?” Having a method to calculate severity can be handy when the handler is in the situation of having to triage, or choose how to deploy finite defensive assets. To the system owner, his system is the most important one in the world (much like everyone’s own child is the cutest kid). You can use a severity-grading technique like this one to explain why you applied defensive assets to one owner’s system rather than to someone else’s.

## Scanning for Trojans

This first example comes from a trace that David Leaphart selected for use in his practical. To help get you started, the first trace is saying that on March 24 at 1:54 A.M. source host computer 24.3.57.38 connected from source port 11111 to destination host computer 24.3.21.199 on destination port TCP 12345:

```
Mar 24 01:54:58 cc1014244-a kernel: securityalert: tcp if=ef0 from 
24.3.57.38:11111 to 24.3.21.199 on unserved port 12345 
Mar 24 03:14:13 cc1014244-a kernel: securityalert: tcp if=ef0 from 
171.214.113.228:2766 to 24.3.21.199 on unserved port 1243 
Mar 24 04:45:01 cc1014244-a kernel: securityalert: tcp if=ef0 from 
208.61.109.243:3578 to 24.3.21.199 on unserved port 1243 
Mar 24 04:45:06 cc1014244-a kernel: securityalert: tcp if=ef0 from 
208.61.109.243:3832 to 24.3.21.199 on unserved port 27347 
Mar 24 05:40:42 cc1014244-a kernel: securityalert: udp if=ef0 from 
24.24.100.172:2147 to 24.3.21.199 on unserved port 137 
Mar 24 14:56:08 cc1014244-a kernel: securityalert: udp if=ef0 from 
63.17.79.40:4294 to 24.3.21.199 on unserved port 137 
Mar 24 17:20:44 cc1014244-a kernel: securityalert: tcp if=ef0 from 
62.6.100.45:1828 to 24.3.21.199 on unserved port 27374 
Mar 24 20:50:47 cc1014244-a kernel: securityalert: tcp if=ef0 from 
194.27.62.179:4857 to 24.3.21.199 on unserved port 27374 
```

### Analysis

The following questions prove very useful for determining the severity of any intrusion. Here they have been applied to the trace preceding identified:

- **Evidence of active targeting?**Yes. The traffic from the source is detected at the host’s interface.
- **Identify the history?**No. Previous traffic from the source address was noted in the detect report.
- **Identify the technique?**TCP and UDP packets were directed at a specific host. The SYN packets were directed at TCP ports 12345, 1243, 27347, and 27374. The UDP traffic was directed at UDP port 137. The sources are hoping for a SYN-ACK, or no response in the case of UDP. The port scan is coming from different sources over a number of hours. All the source addresses are active on the Internet and do not appear to have been spoofed.
- **Evidence of intent?**This detect is a port scan of the victim looking for various vulnerabilities. These can be summarized as follows: Port 12345 Netbus and also the TrendMicro listening port Port 1243 SubSeven and Backdoor-G Trojans Port 27374 SubSeven 2.0 Port 27347 Possibly a typing error for port 27374 Port 137 NetBIOSThe analyst needs to check the victim for evidence of Trojans and ensure that NetBIOS is not a problem.
- **Identify hostile individuals and groups?**Based on Whois, these source addresses came from various locales. They appear to be unrelated both in geography and time. The last address is of a little more concern, however, because it originates in Turkey. These scans appear to be hostile, but the victim seems to be rebuffing the scans.

### Severity

I would assess the severity of this breach as follows:

- ****Criticality.****This is a 2, presuming this is not a critical server.
- ****Lethality.****This is a 4, because these exploits can be damaging.
- ****Countermeasures.****This is a 5, assuming that the OS is fully patched.
- ****Net countermeasures.****There doesn’t seem to be a firewall, so this is a 0.

## Host Scan Against FTP

Consider one more example. Eric Brock submitted [Table 16.1](ch16.html#ch16table01). He used a FireWall-1 firewall to collect the information he used for his practical.

**Table 16.1. Example of Data Gathered on a Host Scan Against FTP**

| **ID** | **Date** | **Time** | **SourceIP** | **Source Port** | **DestIP** | **DestPort** | **Protocol** | **Info** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 661530 | 21Feb2000 | 9:09:24 | 195.243.30.140 | 4858 | 10.10.1.1 | FTP | TCP | len 60 |
| 661531 | 21Feb2000 | 9:09:24 | 195.243.30.140 | 4857 | 10.10.1.0 | FTP | TCP | len 60 |
| 661532 | 21Feb2000 | 9:09:24 | 195.243.30.140 | 4860 | 10.10.1.3 | FTP | TCP | len 60 |
| 661533 | 21Feb2000 | 9:09:24 | 195.243.30.140 | 4859 | 10.10.1.2 | FTP | TCP | len 60 |
| … | … | … | … | … | … | … | … | … |
| 661632 | 21Feb2000 | 9:09:25 | 195.243.30.140 | 1144 | 10.10.1.252 | FTP | TCP | len 60 |
| 661633 | 21Feb2000 | 9:09:25 | 195.243.30.140 | 1145 | 10.10.1.253 | FTP | TCP | len 60 |
| 661634 | 21Feb2000 | 9:09:25 | 195.243.30.140 | 1146 | 10.10.1.254 | FTP | TCP | len 60 |

### Analysis

So as we analyze the attack, we want to begin with the fact the packets came to our DMZ; you could call this active targeting. It is important to determine the history. In the list below we consider it only from our DMZ’s perspective, but by using Dshield ([http://www.dshield.org/ipinfo.php](http://www.dshield.org/ipinfo.php)) we can also look at the history of the source IP address at other sites. We describe the technique that was used and then make are best assessment as to the purpose of the packets, the intent, the reason we saw these packets, and begin to make our final analysis conclusions.

- ****Existence.****Someone claiming to be IP address 195.243.30.140 is visiting us.
- ****History.****There is no history of this address visiting our network.
- ****Techniques.****The visitor is sending one FTP packet to each address in our subnet. They are being sent extremely fast.
- ****Intent.****The visitor is attempting to find hosts on our network that will respond on the FTP port.
- ****Targeting.****Our entire network is being targeted, but no specific servers are being targeted.
- ****Analysis.****This visitor is performing a scan of our network, looking for ftp servers. The visitor could be planning a denial-of-service attack against an ftp server, or he could be looking for an anonymous ftp server to see what he can download from it, or to see what he can upload to it.

### Severity

Severity is made up of a number of dimensions, the criticality of the target, how lethal the attack is, and any system or network countermeasures that might mitigate the attack.

- ****Criticality.****This is a 3, because no specific servers are targeted.
- ****Lethality.****This is a 4, because there are many known ftp vulnerabilities.
- ****System countermeasures.****This is a 2, because all operating systems are running the latest patches, but some are listening on the ftp port.
- ****Network countermeasures.****This is a 4, because the firewall blocks all incoming ftp.
- ****Severity score.****This severity score is 1. The formula is this:

```
Severity = (Criticality + Lethality) – (System Countermeasures + Network 
Countermeasures) 
```

# Sensor Placement

A network-based intrusion-detection system isn’t going to work unless there is a sensor. It will not work optimally if the sensor is not placed correctly. Generally, somewhere in the vicinity of the firewall is a good location for the sensor.

# Outside Firewall

Usually, intrusion-detection sensors are placed outside the firewall in the DMZ (as shown in [Figure 16.4](ch16.html#ch16fig04)). This allows the sensor to see all attacks coming in from the Internet. However, if the attack is TCP and the firewall, or filtering router, blocks the attack, the intrusion-detection system might not be able to detect the attack. Many attacks can be detected only by matching a string signature. The string is not sent unless the TCP three-way handshake is completed.

![A sensor, or event detector, is used to instrument the DMZ.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig04.gif)

**Figure 16.4. A sensor, or event detector, is used to instrument the DMZ.**

Although some attacks cannot be detected by a sensor outside the firewall, this is the best sensor location to detect attacks. The benefit to the site is that analysts can see the kinds of attacks to which their site and firewall are exposed. One of the reviewers of the book puts it this way: “Outside the firewall is *attack* detection, and inside it is *intrusion* detection.” Well put!

During late 1997 and early 1998, a large number of sites detected attempts against the portmapper port (TCP/UDP 111). Sites with active portmappers are likely locations for rpc.statd. I ran a vulnerability scanner internally at two locations to see whether any risk existed. The scan turned up more than 50 systems that would answer an rpcinfo –p request (which means an unsecured portmapper) and further analysis showed that they were running statd. The firewall at both locations blocked the attacks, both via portmapper, and any attempt to directly access statd. Having information that sites I was concerned with protecting were under a concerted attack and that there was an internal exposure redoubled my efforts in the never-ending battle to get those portmappers secured and see whether patches were available from vendors for statd. For more information, refer to [www.cert.org/advisories/CA-97.26.statd.html](http://www.cert.org/advisories/CA-97.26.statd.html).

DMZ (demilitarized zone) is the area between an ISP and the outermost firewall interface.

## Sensors Inside Firewall

A school of thought says that sensors should be placed inside firewalls. Several reasons compel this placement. If attackers can find the sensor, they might attack it so that there is less chance of their activities being audited. Systems inside firewalls present less vulnerability than systems outside firewalls. If the sensor is inside the firewall and exposed to less noise, it might generate fewer false positives. Also, inside the firewall, you can detect whether a firewall is misconfigured (if attacks get through that are supposed to be stopped, for example).

It is certainly true that well-configured firewalls stop most low-end exploit attempts. It is also true that far too much attention is devoted to detection and analysis of these low-end attacks.

## Both Inside and Outside Firewall

More is better. Best of both worlds. You have heard both of these slogans. For me, they are more than mere slogans. I deploy sensors on both sides of the firewall. If your organization can afford a sensor both inside and outside the firewall, this has certain advantages, such as:

- You never have to guess whether an attack penetrated a firewall.
- You might be able to detect insider, or internal, attacks.
- You might be able to detect misconfigured systems that can’t get through the firewall so that you can help the system administrator.

If your organization is using an expensive IDS solution, this is not worth the cost and effort. If you do deploy dual sensors, the sensor on the inside of the firewall is the one to set up to page you in an emergency.

**Misconfigured Systems**

Intrusion-detection systems and their analysts should be able to troubleshoot the network. When I was involved in deploying Shadow, we usually spent the first week or two helping the site fix problems with the network. This is just as true today. Below are some of the common problems:

- localhost 127.0.0.1 or 127.0.0.2 broadcasting to an internal subnet.
- Misconfigured DNS files. These read from right to left; so if your site’s network ID is 172.20.0.0/24 and you detect a host (172.20.30.40) doing a broadcast to 255.30.20.172, that could be a clue that someone didn’t get the word that domain files read right to left.
- Incorrect subnet mask. Broadcast to 172.20.255.255 rather than to 172.20.30.255.
- Backdoors. When you see a packet coming from the Internet to 172.20.30.255 (using the network ID from the preceding example), there is a pretty good chance your network has sprung a leak—that is, a packet should not be coming from you, to you, outside your firewall.

## Additional Sensor Locations

The most common place for a sensor is outside the firewall, but it is certainly not the only place that benefits an organization. Many intrusion-detection systems can be used to support the organization in a variety of additional locations, including the following:

- Partner networks, to which you have direct connections to customers and suppliers often inside your firewall.
- High-value locations, such as research or accounting networks.
- Networks with a large number of transient employees (consultants and/or temps, for example).
- Subnets that appear to be targeted by outsiders, or that have shown indications of intrusions or other irregularities.

A final issue in sensor placement is what the sensor is connected to. Networks today operate almost exclusively on switched VLAN environments. Sensors *can* operate in these environments. If the switches’ spanning ports are not configured properly, however, intrusion detection is all but impossible. One thing to be aware of is that spanning puts a load on the switch. If a sensor is to be operated in a switched network, the implementation must be tested. TCP is a duplex protocol, and the analyst should ensure that the sensor is receiving both the source and destination side of the conversation. The sensor should also be tested to ensure that it sends data reliably from the switched location. It might be necessary to configure the sensor with two interface cards. The first can monitor in promiscuous mode (listening to all packets regardless of whether they are addressed to the sensor) attached to a spanning port. The second interface would be placed on a separate VLAN to communicate with the analysis station. Of course, throwing money at the problem is always a handy trick in intrusion detection. If you are having load and configuration problems, here are a couple of options:

- Consider a network tap. These are connected directly to the media and allow the sensor to see the data that passes by the tap.
- TopLayer, [www.toplayer.com](http://www.toplayer.com), has a switch designed to copy data from the network to an IDS.
- Cisco Catalyst 6000 switches can support an optional Policy Feature Card that allows you to control the data copied to the IDS in about the same way the TopLayer does.

# Push/Pull

Now that you have determined where you want to place your sensor, how will you extract the data from it? The preferred behavior, at least when you first deploy a sensor or event generator, is to *push* events to the analysis system as they occur. When the sensor detects an event, it creates a packet with the pertinent data and shoots it to the analysis station. An obvious protocol for this would be something like an SNMP trap. Most commercial products have their own proprietary protocol for communications between the sensor and analysis station. The number-one feature potential customers look for when they compare intrusion-detection systems is “real-time” response.

**Pushy Intrusion-Detection Systems**

One of the more interesting selling points for intrusion-detection systems is how obnoxious they can behave. It seems like a good idea when looking for a system that the IDS will beep the console, send us email, page us, or call our cell phones. It usually takes only a couple weeks to turn off these handy real-time notification features. Even the most dedicated analyst will accept only so many false alarms at three o’clock in the morning.

Real-time is *not* possible until the intrusion-detection capability exists in the network switch fabric and computer system operating system and programs themselves. Even so, prospective customers of intrusion-detection systems want the event-detection information available to them as quickly as possible, and that makes a whole lot of sense. Certainly then, push is the correct architecture for network-based intrusion detection, right?

Push-based architectures have one very severe flaw. If their behavior is such that they generate a packet in response to a detect, and if the sensor can be observed, it is fairly easy to determine how it is configured. Over time, this would allow an attacker to determine what the sensor ignores. This kind of effort and patience is unlikely with low-end script-kiddie attackers, but almost guaranteed behavior from the high end, such as high-value economic espionage. The obvious solution to this problem is to push out the events on a regular basis as a stream. This gives the same, just a little later than real-time response, capability and masks what the sensor detects. If there are no detects, the stream is just filled with encrypted null characters.

[Figure 16.5](ch16.html#ch16fig05) shows the differences in architecture between push and pull systems. On the whole, push is the better architecture for intrusion detection. One of the best applications for pull is a covert sensor, which can be employed in an investigation. It can be focused on a particular computer system. It can also just passively monitor communications until a key phrase occurs, and then it can be used to capture the communication stream. Most of the sniffers deployed by hackers to collect user IDs and passwords are pull-based systems. They collect data until the collected data is retrieved.

![Push or pull?](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig05.gif)

**Figure 16.5. Push or pull?**

# Analyst Console

So, you have determined where to place your sensors and have selected between push, pull, or both paradigms to acquire the EOI information. Now you can finally get to work. The intrusion-detection analyst does her work at the analyst console. If an election was won with the mantra, “It’s the economy, stupid,” someone better tell the intrusion-detection vendors that, “It’s the console, stupid.” An organization typically looks for the following factors when shopping for an IDS:

- Real-time
- Automated response capability
- Detects everything (no false negatives)
- Runs on Windows XP/UNIX/Commodore 64 (whatever the organization uses)

That gets the box in the door, but will it stay turned on? I have visited several sites that deployed commercial intrusion-detection systems very early in the game, and although they are still connected to the network, the console has a thin layer of dust on its keyboard. After the organization has been using the system for several months, the feature set tends to be as follows:

- Faster console
- Better false positive management
- Display filters
- Mark events that have already been analyzed
- Drill down
- Correlation
- Better reporting

Most major commercial IDS system consoles were so bad that the Department of Defense funded a number of alternate designs. Several of these are now hitting the market as products in the Enterprise Security Console market. Most organizations can’t afford to develop alternative interfaces; so if you are in the market for an IDS, this list might help you select one you can actually use. The following sections explore the console factors in greater detail.

## Faster Console

The human mind is a tragic thing to waste, but that is exactly what happens when we put trained intrusion analysts’ minds in a wait state. Here is what happens: The analyst has a detect, he starts to gather more information, he waits for the window to come up, he waits some more, and suddenly can’t remember what he was doing.

I was working with the sales engineer of an IDS company recently and tried to point out that the interface was very slow. His answer of course was to buy a faster computer. (This was a twin 1.2Ghz Pentium IV with a gigabyte of RAM, which was still fairly current for January 2002.) One simple technique for improving the console performance is for the system to always query the information for any high-priority attack and have it canned and ready for the moment the analyst clicks on it. This way, the computer can wait for the analyst, rather than the other way around.

## False Positive Management

False positives happen. Sometimes we can’t filter them out without incurring false negatives, so we must ask: What we can do to manage them?

The Code Red web attacks serve as a good example. If we write a filter that dampens probes to port 80 (and most of us did), we stand the risk of a massive false negative. If we don’t use such a filter, we will cause a large number of false positives (false positive in the sense that if we are not running a vulnerable version of IIS, we don’t need to be concerned with Code Red). Because Code Red is a Windows problem, we could get part of the way towards handling this problem with a better filter. If our filter language supports it, we could put in basic passive fingerprinting information for Windows into our filter. For instance, a Windows system defaults to a TTL of 128 and TCP window sizes between 5,000 and 9,000 for Windows NT and between 17,000 and 19,000 for Windows 2000; so if we see a TTL of greater than 128 and a window size that is not within spec, perhaps we could afford not to display the detect. We still collect it, but we do not bother the analyst with it. When the analyst selects any event in the potential false positive class, the console should display the regular normal information that it always does, but also the additional data to enable the analyst to make the determination.

**Responsibility for False Positive**

IDS vendors’ feet need to be held to the fire for better false positive management. The Snort ruleset is getting better and better about providing information in the help file that tells an analyst whether there are possible false positives and what they are. But this is not good enough. Vendors must be diligent in reducing them, because false positives are the biggest hurdle to successful incident management. Vendors should fix filters that cause too many false positives, make sure that filters vulnerable to them are tunable, and delete filters that are useless and cause too many false positives. If nothing else, they must carefully document exactly the traffic pattern triggering the filters to report false positives.

## Display Filters

The false positive management technique just discussed is used on some commercial IDS systems and should be considered a minimum acceptable capability. To reach a goal of detecting as many events of interest as possible, you have to accept some false positives. Display filters are one way to manage these. This is not a new idea; network analysis tools, such as NAI’s Sniffer, have always had both collection and display filters.

## Mark as Analyzed

Unless you are a second-level (supervisor, trainer, or regional) intrusion analyst, life is too short to inspect events that have already been manually analyzed. After an analyst has inspected an event, it should be marked as done. This is not rocket science. After all, the web browsers we all use mark the URLs we have already visited. Ideally, this would be more like the editing functions on modern word processors such as Microsoft Word—the event gets a tag with the date and time it was analyzed and the username of the analyst, and whether it was rejected as a false positive or accepted and reported.

## Drill Down

We certainly wouldn’t want to provide users an interface that intimidates them! When an organization first starts performing intrusion detection, it might be quite happy with the system displaying a GUI interface with a picture, the name of the attack, date, time, and source and destination IPs. The happiness often ends when the organization finds out that it has reported a false positive. At this point, the analyst starts to desire to see the whole enchilada and it should be available with one mouse click. Drill down is a very powerful approach. Analysts get to work with big-picture data, and then as soon as they want more detail, they just click. The analyst should not have to leave the interface he is using—that discourages research. Analysts certainly should not have to enter a separate program to get to the data—that is inexcusable.

Drill down is not possible unless the data is collected (and it certainly ought to include the packet headers). No analyst should have to report a detect he can’t verify!

## Correlation

Every analyst has seen a detect and scratched his head saying, “Haven’t I seen that IP before?” Intrusion analysts at hot sites (sites attacked fairly often) frequently detect and report between 15 and 60 events per day. After a couple of weeks, that is a lot of IP addresses to keep track of manually. It also is not hard for the analysis console to keep a list of sites that have been reported and color those IP addresses appropriately.

## Better Reporting

Two kinds of reports make up the bread and butter of the intrusion analyst: event-detection reports and summary reports. Event reports provide low-level detailed information about detects. Summary reports help the analyst to see the trends of attacks over time and the manager to understand where the money is going.

### Event-Detection Reports

Event-detection reports are either done event by event or as a daily summary report. They are usually sent by electronic mail. The IDS should support flexibility in addressing and offer PGP encryption of the report. The reports might be sent to groups that specialize in collecting and analyzing this information such as Incidents.org or SecurityFocus or the organization’s CIRT or FIRST team, the organization’s security staff. If you are shunning the attacker or plan to take action, another powerful technique is to file the report as a memo to record. For every detect displayed on the console, the analyst should have the opportunity to report with a single mouse selection accepting the detect. The system should then construct a report, which the analyst reviews and annotates before sending.

If you are shopping for an intrusion-detection system or Enterprise Security Console, sit down at the console and see how long it takes you to collect the information needed to report an event and to send it via email (or other format such as XML) to a CIRT or FIRST team. If you can’t access raw or supporting data, take your hands off the keyboard and walk away from the system. If it takes more than five to seven minutes and your organization intends to report events, keep shopping. If you can collect the information including raw or supporting data and send it in within two minutes, please send me email telling me about the product so I can get one too.

### Weekly/Monthly Summary Reports

Management often wants to stay abreast of intrusion detects directed against the sites for which they are responsible. Event-by-event or even daily reporting might prove too time consuming, however, and doesn’t help them see the big picture. Weekly or monthly reports are a solution to this problem. In general, the higher level the manager, the less frequently she should be sent reports.

# Host- or Network-Based Intrusion Detection

The more information we can provide the analyst, the better chance she has of solving the difficult problems in intrusion detection. What is the best source of this information, host based or network based? If you read the literature on host-based intrusion-detection products, you might conclude that host based is a better approach. And, of course, if you read the literature of companies that are primarily network based, theirs is the preferred approach. Obviously, you want both capabilities, preferably integrated, for your organization. Perhaps the best way to consider the strengths of the two approaches is to describe the minimum reasonable intrusion-detection capability for a moderately sized organization connected to the Internet, such as shown in [Figure 16.6](ch16.html#ch16fig06).

![A common architecture for a moderately sized organization.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/16fig06.gif)

**Figure 16.6. A common architecture for a moderately sized organization.**

The sensor outside the firewall is positioned to detect attacks that originate from the Internet. DNS, email, and web servers are the target for about a third of all attacks directed against a site. These systems have to be able to interact with Internet systems and can only be partially screened. Because they face high overall risk, they should have host-based intrusion-detection software that reports to the analyst console as well. This shows the need for both capabilities, host and network based, even for smaller organizations. As the size and value of the organization increases, the importance of additional countermeasures increases as well.

This minimum capability does not address the insider threat. Much of the literature for (primarily) host-based solutions stresses the insider attack problem. I keep seeing studies and statistics that state the *majority* of intrusions are caused by insiders. This is beginning to change and most experts agree that the majority of attacks come from the Internet. Malicious code has become a huge problem, however, and in some sense Trojans and information-gathering viruses can be thought of as insiders after they are in your systems. If insider attacks are a primary concern for your organization, additional measures to achieve a minimum capability are required, such as the following:

- Use taps or spanning ports on network switches so that you are not blind on the inside.
- Configure the filters on your DMZ sensor so that they do not ignore your internal systems.You must keep tabs on outgoing traffic as much as incoming. This is especially true because malicious code has become such a major problem.
- Configure the filters on your border router or firewall to allow only outbound traffic if the addresses correspond to your assigned Internet addresses. This is called *egress filtering* and there is a how-to paper available at the Incidents.org web site ([http://www.incidents.org/defend/egress.php](http://www.incidents.org/defend/egress.php)).
- Deploy network-based sensors at high-value locations such as research and accounting.
- Deploy honeypot systems at juicy locations with files that appear to be anything you think insider attackers might be trying to steal.
- Place additional sensors from time to time on user networks as a random spot check.
- At the very least, you should deploy host-based intrusion-detection code on all server systems as well as corporate officers and other key personnel. Many personal firewalls are available for less than $75 a station, and they are easy to deploy (Tiny, ZoneAlarm, BlackIce, and Symantec Internet Security, for example).
- Establish a reward system for those who report on employees who misuse or steal from the organization.

# Summary

Very often, the features that seem most desirable when searching for an intrusion-detection system don’t prove to be all that important in actual use. The first one to go is usually the capability to send alerts to the analyst’s pager.

For various reasons, intrusion-detection systems cannot even look at every possible event. Why? This chapter identified a few possible reasons: The event happened on another network. The IDS is dead. The IDS has no understanding of the protocol. Perhaps the IDS has reached its maximum bandwidth limit and dropped the packet. Further, the network-based IDS is limited to the capabilities of the spanning port on a switch, and encrypted packets prevent IDS identification.

An analyst gets better results from an intrusion-detection system if he understands what he is searching for and tunes the IDS to find it, as opposed to letting the IDS tell the analyst what to look for.

If you have only one sensor, place it outside your firewall.

When you have evidence that your site is under a targeted attack, and that the attacker knows the type of operating systems you have and is targeting them accurately, take additional countermeasures swiftly.

If possible, implement a balanced intrusion-detection capability with both network- and host-based solutions.
