# Chapter 18. Automated and Manual Response

![Automated and Manual Response](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

When we were learning how to analyze network traces, we discussed stimulus and response in detail. Now, we use the same concept but apply it at the organizational level as we consider the defensive responses available to us. The stimulus will generally be a “successful” attack or attack attempt. A successful attack, if detected, invokes an incident-handling procedure. How do we define a successful attack? In the vein of “any landing you can walk away from is a good one,” we can say “any attack that causes us to take action above our normal filtering is a successful attack.” Do you agree? If not, keep in mind that if we respond in any non-automated, non-normal way, it has to cost us resources. What I would like to do is offer three attack examples. Take a look at each of these and consider whether they are successful attacks:

- ****Ping sweep.****A series of ICMP echo requests from a party conducting reconnaissance. Ping sweeps are usually launched from outside our intranet or autonomous systems to internal subnet broadcast addresses. They might be detected by a sensor such as a firewall or intrusion detection system.
- ****Disk-based survey.****An employee receives a letter with a disk. If he places the disk in his computer, answers all the questions, and mails the disk back, he receives a free T-shirt.
- ****TCP port 53 connections.****An Internet company that produces banner ads for web pages is observed pinging systems that have gone to these web pages and attempted to initiate connections to TCP port 53 on these systems.

What do you think? I would say that if your perimeter router or firewall blocks ICMP echo requests, the ping sweep is not a success. I have heard folks assert that this is just a reconnaissance probe, not an attack; but the question is, does it cost you resources? I was looking at a network trace recently in which the attacker was going after only actual live systems. It is kind of scary when they know what they are looking for.

The disk-based survey? Certainly, this is a successful attack. Most employees would never know which files were scanned or added to their system, but it is certainly true the attacker gets the benefit from the information the employee types into the survey—and your organization is footing the bill. As a security professional, you should inform your organization’s employees to throw these disk-based surveys straight into the trash, or if they must, take them home to fill them out.

The simple DNS lookups? DNS queries happen all the time, and it is hard to determine which queries might be reconnaissance as opposed to the function call **gethostbyaddr** that occurs whenever someone is web surfing. However, the HTTP protocol headers contain a lot of information about the client that is web surfing. Some of the fields include the following:

- Host operating system.
- Version of the browser being used.
- The last web server visited. This is the referrer field.

Web servers routinely collect this type of information for marketing purposes. The collected data helps the webmasters tune the look and feel of the pages as well as phrases that web clients are looking for. However, this information can also be used to collect information about the web clients. If you add DNS, and possibly netstat type information, you begin to compile an incredible amount of information about a given IP address, or IP address range.

You might notice that I did not use any “gulpers” for the examples (with the possible exception of the ping sweep; however, these are not script kiddie examples either). I am very impressed with the philosophy of Escrima, a martial art. The idea is to take whatever targets your adversary offers and cut them apart (literally, knives are the primary weapon) a piece at a time. This is a fundamental principal of information warfare. Folks are constantly employing a wide variety of techniques against your organization, taking whatever is vulnerable. This is why a sound protection scheme, including defense in depth and automated response, is so important.

# Automated Response

This section examines architectural issues of automated response, mechanisms available to us, and the most popular implementation—PortSentry—as well as the automated response capability of personal firewalls. Obviously, the cheapest and easiest response is the automated response. This form of incident handling should be widely practiced and, if done wisely and with care, is safe. There are a couple of gotchas we will address from the start. Because intrusion-detection systems have a problem with producing false positives, you might err and respond against a site that never attacked you. The good news is that you could take a number of passive defenses. These passive responses I describe do not cause harm. You would have to have rocks in your head to hit a suspected attacker back with an automated exploit due to the potential for error from IP spoofing and false positives.

The other problem is that if your attacker determines that you have automated response on, he might be able to use this against you. Imagine setting up the equivalent of an Echo-Chargen feedback loop involving two sites’ auto-responding intrusion-detection systems and a couple of spoofed addresses. Or, at a major deadline, the attacker could target a site with spoofed attacks from its partner/customer/supplier addresses and cause the firewalls to isolate from one another so that the deadline cannot be met.

## Architectural Issues

Because network-based intrusion-detection systems are generally passive, just tapping the bit stream, they do not usually respond to an attacker’s stimulus. However, many commercial implementations of intrusion detection have the capability to connect directly to the firewall and this combination allows for automated response. In fact, hogwash, a firewall implementation based on Snort, actually integrates the two functions, and there are similar commercial products under development. The DMZ or Internet connection is an obvious place to implement automated response, but there are other very effective options that include internal firewalls and the host systems themselves.

### Response at the Internet Connection

The closer to your site’s Internet connection that you apply automated response, the more effective it will be; but the risk of harm to the organization coming from spoofing and manipulation also rises quickly. A primary reason for this is that your Internet connection is generally unfiltered—that is, after all, where you put your firewall and filtering router. This means these devices can be hit with any possible address (spoofed or not), 65,535 TCP ports with any number of flag and options combinations, 65,535 UDP ports again with options, ICMP, fragmentation, and all of the IP protocol types. This is a lot of space to defend against. Now a “deny all that is not specifically allowed” policy will prevent the overwhelming bulk of these possibilities from penetrating your perimeter, but the risk comes when we try to interpret all this using an automated policy. The bottom line, though, is that in the face of a rapidly increasing threat, and with the need to respond in the time it takes to evaluate a single packet, automated response is probably going to be widely implemented. And because you get the biggest bang for your buck by putting the capability near the Internet connection, we will probably continue to see solutions like hogwash and Tippingpoint’s UnityOne ([www.tippingpoint.com](http://www.tippingpoint.com)).

### Internal Firewalls

Automated response using internal firewalls is much safer because the traffic an internal firewall receives generally is at least partially filtered. Also, you know your policy better. If you are defending five machines or so with your internal firewall, you have a pretty good idea with whom those hosts should be talking and on what ports. Of course, the catch is the automated response covers a lot less area. And there are cost issues both for hardware and software and also administration. The good news is a number of appliance and near-appliance devices need almost no configuration. The DSL and cable modem revolution has created a huge market for these, and there are a number of options including appliance products from Cisco, Linksys, Netgear, and Symantec. I really like the little $500 PIX, but try putting your hands on one; they seem to be permanently sold out. Because Network Address Translations (NATs) are so effective at preventing attacks and the lower end devices run about $250, there is no reason not to deploy them throughout your organization. If people do widely deploy boxes like that, I might have to find a new line of work. In fact, I am already working on my delivery: “Would you like a hot apple pie with that order?”

### Host-Based Defenses

Automated response on the host is clearly where you get the minimum bang for the buck, but this is widely practiced, and the risk from spoofing is much lower than a perimeter solution. The industry trend is twofold: internal appliance type firewalls and host-based firewall defenses. A number of people, especially in university environments, depend entirely on software such as Psionic’s PortSentry for their UNIX systems. PortSentry blocks an offending host from making any further connections and even drops the route so that the host cannot get back to try again. The PC world has a large number of personal firewall solutions. Because this is an automated response chapter, we should mention the amazing BackOfficer Friendly, [www.nfr.com/products/bof/index.html](http://www.nfr.com/products/bof/index.html). This is far more than a personal firewall! Perhaps we could consider it a honeypot or even an active defense solution. If you have a Windows system and want to get started learning about automated response, download this and give it a look. The only downside is that it hasn’t really been updated as the threats increase. Imagine what would have happened if they had managed to incorporate LaBrea technology early in the Code Red days! The good news is these host-based defense systems are very effective, becoming more prevalent, and are fairly easy to install, configure, and maintain. Why do people depend so heavily on these programs? Often, they are security-conscious administrators at sites with no filtering from the Internet whatsoever! There are four main sources for unfiltered addresses:

- Cable modems and DSL
- Commercial organizations that don’t care
- Universities in the name of academic freedom
- Connecting while on travel such as at an Ethernet equipped hotel

The cable modem and DSL world is going to be an ever-increasing threat to site defenders, so maybe I don’t have to worry about pushing hot apple pies on the fast-food drive-through after all. I have instrumented a number of cable modem connections and tend to receive between about 5 and 20 probes per day. Hundreds of people are hooking up to cable and DSL everyday, and most of them have unprotected systems. This is something we became very aware of in 2001 with Code Red, nimda, and Leaves. Most cable modem style defenses such as NATs and host-based firewalls do not implement automated response; but it isn’t a bad trade: intrusion protection for intrusion detection.

Commercial organizations that are inept or don’t care and connect to the Internet will not survive the transition to an information economy.Yet, a surprising number of sites either do not have a firewall or have inadequate perimeter protection. When you connect your organization to the Internet, you will be probed and tested. If your systems are not combat ready and can be seen from the Internet, they will fall. If you are lucky, you get the playful sorts of attackers, but even then your system will likely be used to attack and probe others. A commercial organization with a compromised system could share a far worse fate if the attackers decide to use it to acquire corporate secrets. As we suggested earlier, if I were in business, in addition to a main firewall, I would strongly consider the use of internal appliance type firewalls. After you get inside the perimeter of many facilities, they have neither detection nor protection capability. Key hosts would do well to have system level protections.

The interesting battleground that I have been watching for several years is the university world. Many of these sites have no firewalls or filtering at all. Already, I have seen departments set up their own firewalls in universities that don’t want to put one at the front door. And, system protections are popular with proactive administrators. A fully open Internet connection is an archaic and brain-dead throwback to academic freedom, and I doubt the practice will survive another four years. It will be fun to watch. The academics that claim all packets must be free to travel the Internet will probably back down soon enough. Just wait until their department’s budget suffers a 50 percent cut due to the university losing a major lawsuit brought by a dot.com that lost significant revenue when the university’s systems were compromised and used in an attack.

Connecting while on travel requires a bit of thinking. I often carry a small Linksys router hub with me, so that I have two layers of defense: the NAT and my personal firewall. Also, it allows my wife and I to be online at the same time; when you are used to being online for 14 hours a day, you aren’t very good at taking turns to check your mail. The NAT allows me to mitigate the risk to my relationship and my important documents—what could be sweeter?

I understand that you might have reservations about implementing automated response. I try to set things up in class and show a number of intrusion detects from December 24 and 25 and comment that Christmas is a special time of the year. Then, when we come to the automated response discussion, I point out that during the Christmas and Easter vacations people are normally not around, but systems are still up. This can be an excellent time to experiment with automated response at the Internet connection. Because very little work is getting done, especially at Christmas, this is a fairly low-risk time to take your automated response systems out for a spin and see what they are capable of.

Next, let’s work through our response options. It is a good idea to keep in mind the previous discussion about where the analysis and response functions are best accomplished.

## Throttling

This is a smart response to port scans, host scans, SYN floods, and mapping techniques. The idea is to begin to add delay as a scan or SYN flood is detected; and if the activity continues, continue increasing the delay. This can frustrate several script-driven scans such as ping mapping to 0 and 255 broadcast addresses because they have to rely on timing for the UNIX/non-UNIX target discrimination. Enterasys and Cisco both have rate limiting. In fact, any device you can interface with that supports Quality of Service should be usable in this fashion.

Throttling can also be done at the protocol level. For UDP, the IDS could forge a source quench. For TCP, if the traffic goes through a proxy firewall, the outbound interface could send a small window size. I would avoid using the LaBrea trick of a window size of 1. Attackers will be looking for that next time around, but 5, for instance, will drastically slow down the attack.

### Drop Connection

Dropping the connection is straight out of the string-matcher handbook. When I say “connection,” of course I am talking TCP primarily, but the same general effect for UDP can occur using a shun (as discussed in the next section).

The attacker establishes a connection to an active port. Then he sends the packet, or packets (for intrusion-detection systems such as Cisco Secure IDS or Snort with packet re-assembly capability), that contains the attack string, or exploit. This is the point of great danger for a vulnerable system. The IDS detects the string and orders the firewall to drop the connection. Now, you might have a compromised system, but the attacker can’t make use of the compromise directly. In the case of a buffer overflow, the victim computer is now running whatever code was beyond the command length and is probably running it as root. If it is a grappling hook type program (a small telnet daemon running on some predefined port), dropping the connection might only buy you a few seconds.

### Shun

I am going to continue the attack just described with the shun technique, and then discuss why shun might be one of the most important automated and manual techniques at your disposal.

As the attack progresses, you have a new process running as root that has opened up a telnet daemon or sent back an X Window or whatever open door into our victim system the attacker has chosen. Dropping the connection does not help, because he is already planning to initiate another connection; or in the case of an X Window, you have initiated the connection to him from our side. Shunning might buy some relief. When you shun, you do not accept any more traffic to or from the offending IP address. This is a good technique and can be executed on just the offending host or on its subnetwork. A capability to look for whether you want to implement shun is a “never shun” file (also called a white list); you can place the addresses of your customers and suppliers in this file. This protects you from an attacker being able to spoof these addresses with some obvious script kiddie attack just to isolate you from the systems you do business with.

Shunning does not help you if the attacker is using two address families, which is fairly common. My friend Pedro Vasquez sent me a trace from Brazil with a DNS buffer-overflow coordinated attack that did exactly this. The attack came from one host and the X Window was displayed to another host. Just because shunning does not help you in every case, however, doesn’t mean you shouldn’t employ the technique.

**Proactive Shunning**

It turns out that a number of Internet service providers and even whole countries cannot, or will not, manage their hosts. Over time, as you have been doing intrusion detection, you come to realize that an incredible number of the attacks that you and your friends deal with (you are sharing data, right?) come from the same network addresses. Why play with fire? Eventually, they will find a way to burn you! Block them. Let me take this a step further: be willing to block them at the two octet or 16-bit mask. Be willing to block a whole country. Nobody is getting arrested for hacking, and it doesn’t look like that is going to change any time soon. If countries that will not control their “research networks” start to be marginalized and are unable to reach large parts of the Internet, however, they will have to come to the table and talk turkey.

We have been experimenting with this on the SANS web server, and one single ISP that has open proxies has been the source network of more attacks than any other address group. We shunned them for about two months; they wrote and made promises, so we let them back into the site and within a day, we were attacked again. We are considering a permanent ban at this point.

## Islanding

Islanding is the auto-response of last resort. The idea is, if a sufficient number of attacks occur over a time period (usually during time periods during which no analyst is on duty), the intrusion-detection system sends a command to an X10 or similar logic-controlled relay and drops the power to the router. The result of this is isolation of the site from the Internet. Although there is serious potential for a denial-of-service condition, this can be a reasonable strategy for three-day weekends at high-security sites. This capability can be hacked together with a few lines of code with any intrusion-detection system that issues SNMP traps. On second thought, maybe that SNMP trap idea is not so smart. Automated response does have a risk of self-inflicted denial of service. Only do something like this if you are willing to have the deadfall occur on any given “red-alert” alarm condition.

## SYN/ACK

Suppose the intrusion-detection system knew the ports that a site blocked with its firewall or filtering router. Further, suppose that every time the IDS detected a TCP SYN packet to one of these blocked ports, it answered back with a forged SYN/ACK. The attackers would think they were finding lots of potential targets; however, all they would be getting is false positives. If you think about it, the latest generation of scanning tools has caused a lot of problems for the intrusion-detection community with their decoy capabilities. This would be a great way to answer back. I finally got to see this in action. Some friends of mine got a Raptor firewall. This works great. The attacker completes the three-way handshake and thinks he has a victim. He even sends data with the lone ACK, so you can see what he is up to.

## Reset

This is the so-called Reset kill or as the Snort folks say, session sniping. I have serious reservations about this technique. The Reset kill can tear down someone else’s TCP connection, and I have seen commercial IDS systems fire these kills based on false positives. The idea is if you see a TCP connection that has been established and the IDS detects a signature that requires action, you forge two Resets and send one to both sides to blow off the connection. It used to be possible simply to smack the initiating host, but attackers are learning to ignore Resets. This isn’t used all that often, although it is available in Snort and commercial intrusion-detection systems.

# Honeypot

An advanced site, in conjunction with throttling, can use its router to direct the attacker to a specially instrumented system called a honeypot. The honeypot could be used as a stand-in for the targeted host. We also have used honeypots with static addresses as stand-ins for internal hosts that have become “hot.”

Every once in a while, a host that you are protecting will suddenly stir up a lot of interest and you will keep seeing probes and exploit attempts directed to it. In such a situation, a fun course of action is to change both its name and IP address and install a honeypot in its place. However, the most common use we have at [www.incidents.org](http://www.incidents.org) for honeypots is to figure out what the attackers are doing by catching their attack in a honeypot. I have tried three types of honeypots: a proxy system, the *Deception Tool Kit* (DTK), and an “empty” computer, the Honeynet approach.

## Proxy System

During 1996 and 1997, I did a lot of research into hacker technology. The goal of the project was to collect as many exploit tools as possible. I took a Sun computer running SunOS 4.1.3, patched it as best I could, and installed the TIS toolkit. The system was named cray3. I copied an /etc/motd from a Unicos system and did everything I could to make it look like a cray. Thank goodness this was before TCP fingerprinting.

I used the TIS toolkit for the target services, ftp, telnet, SMTP, and so forth. Finally, I compiled Internet Relay Chat (IRC). The idea was to spend time on the hacker IRC channels, exchange code, get people to attack my system, and collect the techniques they used. There was only one small problem. I had never been on IRC! I knew that if I didn’t do it right that I would show up like I had five legs and a tail. So what to do? I decided to start in a channel other than #hack. So I tried #thirtysomething. I have never been good at flirting, so I ended up wasting hours watching words fly by on the screen.

Next, I decided to try #Jesus. I figured church people would be nice to me. BZZZZT, they kicked me off within 10 minutes. I was really crushed!

Finally, in frustration, I signed on to the #abortion channel because that was what was about to happen to my project. They were some great folks, although strongly polarized on both sides of the issue. Best of all, they were willing to let a newbie learn to chat. After a week or so practicing my social graces, I entered #hack, but there was just one last little hitch. We had agreed that any hint of entrapment was outside project parameters and because I was doing this for the DoD, I found myself on #hack with a .mil source address. Well, that brought back memories of elementary school and “Kick Me” signs taped to my back; kick me they did.

However, I won a TCP trivia challenge or two, and after a while, we managed to get things going. It was a lot of fun, and they couldn’t resist attacking the .mil system, so we were able to collect a lot of fun data.

## DTK

The Deception Tool Kit was authored by Fred Cohen and is available at [http://all.net/dtk](http://all.net/dtk).

It is written in a combination of Perl and C and emulates a large number of services. DTK is a state machine, can emulate virtually any service, and comes ready to do so out of the box for a number of them. It used to be pretty easy to compile and set up. As it has been improved to be more realistic, however, it has started to become a bear to build.

This state machine approach is essentially what BackOfficer Friendly is, and as I write this Marcus Ranum is writing another honeypot for SANS students to try.

## Empty System

Nothing looks more like UNIX than UNIX, or Windows NT than Windows NT. So in some sense, the perfect honeypot is just a system that is a little older and slower and has a smaller disk (the smaller the better, in case you loose the bubble). Then, you instrument the heck out of the system and collect information as folks try to exploit it. This has been taken to near science by the Honeynet team. Incidents.org is a member of the Honeynet alliance and has a vmware-, [www.vmware.org](http://www.vmware.org), based Honeynet with a firewall, intrusion detection system, and a couple of running operating systems all running on a single machine.Vmware is the closest thing to magic I have ever seen. Lately, there have been some troubling indications that some of the honeypots and Honeynets on the Internet have been identified and their IP addresses are being passed around in the underground so that they avoid these systems.

## Honeypot Summary

Honeypots are an advanced technique. They can be low yield for the effort one has to expend. On the other hand, if you block with your firewall or filtering router, you never get to collect the attack if you filter. A honeypot enables you to collect the attack. If you don’t have a hot system, the best thing to do is set your honeypot up as either your DNS, web, or email relay system. These systems are routinely added to attackers’ shopping lists. The good news is you can collect attacks; the bad news is you collect the same attacks over and over again.

# Manual Response

Intrusion-detection analysts often serve a double role as lead for incident handling, or as a handling team member. *Please* get one thing straight in your head right now:You are going to take a hit. Between the outsider threat from the Internet, the insider threat, and the malicious code threat, you are definitely going to take a hit. Analysts sometimes get in a mindset that they are responsible to protect the organization.You can’t! We don’t expect rescue-squad workers to ensure no accidents occur on I-95, right? We just ask them to help in a professional manner after the accident has occurred. Consider what I have said carefully. I have led a large intrusion-detection team with many sites and have seen several analysts develop a mindset that they are personally responsible to make sure no attacks get through.

If we are going to take a hit, a system compromise can’t be the end of the world. Rather, the point is to deal with it as effectively and efficiently as possible. Because there might be some stress involved, we want a clear, well-defined process to follow. Think about CPR; they have their pithy acronym, ABC. The ABCs of CPR are as follows:

- ****Airway.****Make sure it is clear.
- ****Breathing.****Are they?
- ****Cardiac.****Beating or not beating?

I found the following six-step process in a government publication in 1995. I have been working to refine this model ever since. The six steps are as follows:

- Preparation
- Identification
- Containment
- Eradication
- Recovery
- Lessons learned

This chapter doesn’t discuss preparation or identification; after all, most of this book is devoted to preparation and identification.

## Containment

In incident handling, you learn to maintain a reasonable pace; if you hurry, you make mistakes and that can be costly. There is one place to really move out, however, and that is containment. It is better to deal with two affected computers than four and better to deal with one compromised workgroup than a whole Windows domain. Good incident-handling teams can work in parallel. This is really important in cases in which multiple systems might be involved. As soon as the data has come in, I just make a copy, circle the addresses I need a team member to handle, and hand him the paper. Usually, I don’t have to say more than my trademark “take good notes people, good notes.”

The first thing to do in containment is to start reducing network connectivity.

### Freeze the Scene

My first course of action is to pick up the phone and call the person nearest the system console. The language in the following section has been developed over years of hard-knocks experience. You are a technical person; the person you are calling on the telephone might not be. Also, as he realizes there is a problem, he might be under some stress. Of course, you will develop your own scripts and techniques, but I call the individual with a suspected problem and say:

> Please take your hands off the keyboard and step away from the computer.
> 
> Thank you. Now, in the back of the computer there is a network connection, please find it and remove it from the computer.
> 
> My name is Stephen Northcutt, what is your name?
> 
> Pleased to meet you ______, and where is your office?
> 
> Sure, we know where that is. ________, can I get your phone number and any other office phones that you know?
> 
> You have done a fantastic job. We’ll be right there; now do you have a fax machine? Great; while the team is on its way, I am going to fax you a set of instructions. _______, we need your help and I would appreciate it if you would start as soon as your receive the incident-handling guide. Can you tell me what operating system the computer is?

These are critically important lines. The trick is to say as few words as possible to get the point across. However the “noise” or non-content words such as please, thank you, and fantastic, are very important; we need to de-stress the situation if possible. Despite the attackers, I keep learning the hard way that our biggest danger is what we do to our evidence and ourselves. I am also working on my voice inflection. I don’t have a really commanding, powerful voice, so I try to speak with authority, slower than my normal pace, and try to project kindness and empathy.

### Sample Fax Form

Security Office @UR Organization

On Site Computer Incident Response Form

Revision 2.1.1

Date: Time: Printed Full Name:

Thank you for notifying the security department of this incident and agreeing to help. Please do not touch the affected computer(s) unless instructed to do so by a member of the Incident-Handling Team. In addition, please remain within sight of the computer until a member of the team gets there and ensures that no one touches the system. Please help us by detailing as much information about the incident as possible. We need a list of anyone who directly witnessed this incident; please list their names below. If you need more space, please continue on a separate sheet of paper:

Witnesses:

1)

2)

3)

What were the indications that you observed that led you to notice the incident. Please be as specific and detailed as possible. Incident indicators:

This next section is very important. Please be as accurate as possible. From the time you noticed the incident to the time you called the Incident-Handling Team, or help desk, please try to list every command you typed and any file that you accessed.

Commands typed and files accessed:

Signature:______________________________________

### On-Site Containment

Whenever possible, we suggest two people be dispatched to the scene. One handles the site survey, and the second team member, the more experienced, should work at containing the computer system.

#### Site Survey

The survey member should use a portable tape recorder and describe the scene. Record the names of everyone in the vicinity, if possible. Order everyone in the vicinity who was not there when the incident occurred, does not normally work in the area, or isn’t the system owner, to leave. While the on-site handler is setting up the backup, interview the individual who phoned in the incident. Determine the indications of the incident. Work with the employees in the area to check the other computer systems to see whether there are indications of compromise on these systems. Be certain to continue to record what you are seeing, or if you can’t use a recorder, make sure to take good notes. Every few minutes, shoulder surf the incident handler and make a time-stamped notation of what you observe her doing; two records are better than one.

#### System Containment

The handler should try to get the normal system administrator for this system to ride shotgun. Ask him to help you take good notes. One of your primary goals is to make a backup of the system if at all possible.

Experienced handlers often have their own privileged binary applications and this includes backup programs. If you do not possess your own forensic-type backup and seizure tools, such as safeback, it might be wiser to copy all history files and log files to removable media before taking any other action. Incident handlers are supposed to write the contents of memory to removable media as well; while easily said, however, this has proven to be hard to do in practice. The best backups are bit-by-bit backups. If this option is not possible, the next question to answer is how critical the system is and how time pressing the incident is. If criminal activity is suspected and there is reason to believe that this actually is an incident, it might be best to do as follows:

- Power down the system
- Pop the drive
- Seal it in an envelope with a copy of your notes and the notes from the person who called in the incident
- Store the drive in an evidence safe or locked container with limited access

#### Hot Search

If it is a critical system and criminal prosecution is not a priority, you might have to search the system hot to find the problem. This is where a tool such as Encase or The Coroner’s Toolkit (TCT) can really come in handy. Both tools are available for both old Windows (FAT) and more modern Windows (NTFS) file systems. Before running either tool, I like to run Tripwire on both the search drive and my host operating system before I start. That way, if something goes horribly wrong, I have an idea where to look for the problem. There used to be a forensics tool called Expert Witness, but it died in a lawsuit. I was doing a hot search of a drive that was infected with a virus and the next thing I knew I was infected with a virus. Now of course, the forensics tool sales representative is going to tell you this could never happen with his tool and he is probably right, but why take the chance?

In any case, your goal is to determine whether the evidence on the system reasonably supports the reported indications. This is known as validating the incident, and it is not limited to the information on the suspect hard drive. A good team doesn’t leave a handler all alone; hopefully, someone is working the intrusion-detection system’s records and other sources of data looking for information about the affected system while you are focused on the suspect system’s hard drive.

## Eradication

Sometimes, it is possible to examine the situation and remove the problem entirely; other times, it is not. With eradication, we need to pause for an upwardly mobile career observation about incident handling. If folks in an organization have suffered one compromised computer or six, they are usually pretty scared. If your team comes in and you are courteous and professional and get the job done, they really appreciate it. When they see you in halls and staff meetings, they nod and kind of say thanks with their eyes—it is a good thing.You are sort of a hero.

I used to have this really cool job in the U.S. Navy where I flew around in helicopters waiting for jets to go smacking into the water. Then we would hover over the ejected pilots and I would jump out and swim up to them, hook the crew up to a cable hoist, and we would pull them out of the ocean. You want to know what they always said when I swam up to them? Whenever I ran into them on the ship after the rescue, there was that same nod and saying thanks with their eyes.

*However*: If you show up and do your work and the problem comes back the next day, you are not a hero; you are an incompetent idiot. It is critical that you succeed in eradication, even if you have to destroy the operating system to do it. Repeat after me, “Nukem from high orbit.” See, that isn’t hard to say. Or, “Total eradication is too good for ‘em.”

I have tried to inject a little humor, because we must deal with a serious issue. As an incident handler, you need to be pre-authorized to contain and destroy to save your organization. Please take the preceding sentence very seriously. The incident-handling team needs to have a very senior executive in the organization as its sponsor or champion. The handler must be able to look that very young, very successful program manager droid, who has axed many a promising technical person on a whim, in the eye and say, “Yes, I know how important this system is. We will save as much of the data as your people have properly backed up, but the operating system is toast.” Many times, the only way you can be certain the problem has been eliminated is to scrub that puppy to bare metal.

Oh yeah, when I swam up to these navy pilots, they always wanted to know “what happened?” They asked their questions in such a way that it was clear they wanted to know exactly one thing: Was it their fault? Might I suggest that when you handle an incident, the folks you come in contact will be very concerned that the incident was their fault. Why our culture is so bent on blaming the victim is beyond me! Be gentle and comforting when you speak. Don’t come to conclusions early. Many times, running an incident to ground is like peeling an onion a layer at a time. Even if you know in your very bones it is their fault, be kind and supportive during the incident. The time to deal with what happened comes soon enough!

## Recovery

The purpose of the incident-handling process is to recover and reconstitute capability. Throughout the process, we try to save as much data as we can, even if the system hadn’t been backed up in a long time. Often, we can mount a potentially corrupted disk as a data disk and remove the files we need from it. This is another good application for Tripwire. Before mounting a suspect disk on your field laptop, make sure you have a very current Tripwire running so that you can be certain malicious code doesn’t get on your computer.

*Emergency medical technician* (EMT) trainers use scenarios to drive home the academic points taught. One of the important lessons to teach EMTs is not to become a victim, because this makes the rescue even more problematic. If you see someone prostrate on the ground draped over a cable, for instance, don’t run up to him and touch him. What if the cable is the reason they are lying there dead? What will happen to you when you grab someone connected to a high-voltage cable? The point is to use situational awareness and take a few seconds to think about the circumstances that caused the computer to be compromised. In the exact same way that failing to eradicate the problem makes the incident handler look stupid, we do not want to put the system back in business with the same vulnerability that caused it to be compromised.

This is an important point, because we will probably alter the system in some way. In fact, many times, the system owners will want to use this as an unexpected opportunity to upgrade the system, or freshen the patches. I find it amusing when the same manager who looked me in the eye during the containment phase and said things like, “Do you know how critical this system is? You can’t shut it down,” suggests that we upgrade the operating system before returning to service.

It is all well and good to freshen the operating system. However, what happens when an outsider makes a change to one of our systems? I oversaw the installation of a firewall once at a facility that didn’t have one. For the next five years, every time someone couldn’t connect to something, or their software didn’t work right, I would get phone calls and/or email. “Is it the firewall?” This is a career risk vector to the incident handler. Remember our very young, very successful, hell-bent-on-rising-to-the-top executive? If anything goes wrong, he might use that to deflect attention from the fact that a system in his group was compromised. What countermeasures can we take?

During the incident-handling process, I like to keep the system owners informed. As long as they are in danger, they are very interested. As soon as they can see they are going to make it, they usually turn their attention to something else. It is imperative that early in the cycle, while the adrenaline is still flowing, to pull them aside and say something like this:

Sir, our primary objective is to get you back in business with as little downtime and as few problems as possible. I am sure you understand that because the system was compromised, we will have to make at least some minor changes to the architecture, or it is likely to happen again. To ensure that the changes we make do not impact your operations, we need a copy of the system’s documentation, especially design documents, program maintenance manuals, and most importantly, your system test plan. We will be glad to work with your folks to execute your system test plan before we close the incident.

Now, you and I both know that maybe five computers on the planet earth have an up-to-date, comprehensive test plan. There is no way on God’s green earth that our slick young manager is going to be able to produce it. Time to invoke the power of the pen. We produce our preprinted incident closure form. It has blocks on it for the system administrator, primary customer, and system owner to state that they have tested the recovered system and that it is fully operational. So you say something like this:

No test plan? Ummm, well sir I can’t close an incident out unless the system has been certified as fully operational. Tell you what, if you will get your people to run the tests they use to certify your systems and document those tests and sign the form, tonight, we can get this incident closed. I am willing to stay as long as it takes because as you know, the CIO’s goal for incident handling is for downtime to never exceed one day, and we can’t clear this system for operation until it has been tested.

I invested a couple of paragraphs making this public safety announcement. It is really a bummer when a promising young incident handler gets blamed for system problems after pouring her heart out to save a compromised system. Now that you know the risk, practice safe incident-handling procedures.

After a system has been compromised, it might become a hacker trophy. The attacker might post his exploit in some way. I have seen several instances in which after a system is compromised, recovered, and returned to service, the attackers come out of the woodwork to whack it again. Use your intrusion-detection capability to monitor the system closely. It might be possible to move the system to a new name and address and install a honeypot for a few weeks.

## Lessons Learned

At first, the incident was exciting and everybody on the planet wanted to get involved. There was the hunt for the culprit, sifting through clues to find the problem, and reconstructing the chain of events that led to the incident. Then comes the slow process of recovery and testing. This is less fun and folks are leaving, saying things like, “I guess you guys can take it from here.” Finally, we are done. The problem is contained, eradicated, and the system is recovered. We are all drained and possibly a bit punchy. The last thing in the world you want to hear is, “the job ain’t finished until the paperwork is done.”

Two disciplines distinguish the professional from the wannabe: The pro takes complete and accurate notes every step of the way and does a good follow up. Both of these are disciplines; they do not come naturally. Every time you handle an incident, mistakes will occur. Mistakes also had to occur or the incident could have never happened. But that is a touchy subject, so tread lightly. Things could always have been done better. It is okay to make mistakes, just make new ones.

“Lessons learned” is the most important part of the process when approached with the correct mindset. It should never be a blame thing, rather an opportunity for process improvement. Here is the approach that has worked for me.

The incident handlers are responsible for documenting the draft of the incident report. As soon as they finish it, typos and all, they send a copy to each person listed as a witness, primary customer, and system owner. Anyone can make any comment he wants, and his comments will be part of the permanent record. The handlers make the call whether to modify the report. Within a week of the incident, a mandatory meeting should be held. Book the room for exactly one hour and start on time. The only order of business at the meeting is to review the final incident report’s recommendations for process changes. One-hour meetings are not good places for the consensus approach. Just tally the votes for each item. The final report goes to the senior executive who is the sponsor of the team.

The most important section of an incident report is the executive summary. This is where you document why having a crack incident-handling team saved your organization a lot of money.

# Summary

We face risks with every user or program we add to our systems and with every service we open on our firewall. Effective response, both automated and manual, is an effective mitigation technique. It enables your organization to move a bit faster and a bit more aggressively in this fast-paced world. Some of the automated responses include throttling to slow down the attack, dropping connections, shunning the attacker if he attempts to reconnect, islanding from the Internet in serious attacks, protocol tricks such as sending SYN/ACKs even if the host or service does not exist, and Reset kills.

Every organization has an incident-handling team; some just haven’t formalized one. A formal team following the six-step process of preparation, identification, containment, eradication, recovery, and lessons learned will probably be more effective than an ad hoc response. The intrusion-detection analysts should always be members of the team and often are excellent choices for leading it.

One security model, time-based security, states that the time that we are protected is primarily based on the time it takes us to detect and react to an attack. As we tune our automated and manual responses, we train to react faster and hopefully better, increasing the protection we provide for our respective organizations.
