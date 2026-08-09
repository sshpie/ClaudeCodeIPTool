# 15: Common Pitfalls and Mistakes

## Abstract

Even with best of intentions, a qualified staff, a strong budget, and time it can be difficult to implement strong security measures into any network, and even more so into an industrial network … but who realistically has all of these things? In reality, most industrial cybersecurity experts are trying to do their best with insufficient resources. Therefore, it should be clear that the intention of sharing these common pitfalls and mistakes is to learn, and maybe laugh a little. The intent is not to shame anyone, even though these issues are all derived from actual conversations with me, the author. However, I have heard these often enough that I felt it important to discuss them here, to help others avoid making the same mistakes … and perhaps to end this book on a lighter note.

### Keywords

Cyber attacks; Cybersecurity; Industrial internet of things; Operational technology; VulnerabilityInformation in this chapter• The Basics• Lack of Operationalization• Lack of Awareness• Misunderstanding Vulnerability• Worlds are Colliding!• The Mistake that You are Making Right NowEven with best of intentions, a qualified staff, a strong budget, and time it can be difficult to implement strong security measures into any network, and even more so into an industrial network … but who realistically has all of these things? In reality, most industrial cybersecurity experts are trying to do their best with insufficient resources. Therefore, it should be clear that the intention of sharing these common pitfalls and mistakes is to learn, and maybe laugh a little. The intent is not to shame anyone, even though these issues are all derived from actual conversations with me, the author. However, I have heard these often enough that I felt it important to discuss them here, to help others avoid making the same mistakes … and perhaps to end this book on a lighter note.

## The basics

The first edition of this book was written over a decade ago, and yet some industrial control operators are still making basic mistakes. There's simply no excuse for this anymore: if this is you it's time to get motivated and improve!

### The KISS of death

“Our network is pretty basic …”

The acronym “Keep is Simple, Stupid” is often used to extol the virtues of avoiding complexity. However, this is a bad idea when it means your industrial network consists of a single subnet that is connected directly to the internet. Yes, network segmentation can be complicated. Yes, firewalls can be difficult to properly configure and manage. But if you choose simplicity in these circumstances … consider it a Fail.

### Password123

“I don’t think we ever changed it …”

Everything is a target. If something comes with a default password, you can bet that the attackers know what it is, which makes it an *easy* target. If the industrial network is also connected directly to the internet, you're a few Internet searches away from being part of a botnet.

### People are people

“We don’t need that particular security control, because we’ve told our people they’re not allowed to do that.”

Not to sound like a pessimist, but people don't always do what they're told. An employee might understand that they aren't allowed to use USB devices, but if they *really* need to charge their phone, or if they *really* need to move that one file … you never know what someone might do. Not all misuse is intentional or malicious, but it is inevitable.

### The Air Gap myth

“We’re safe — we’re fully air-gapped.”

Open networking protocols and wireless networks are ubiquitous, yet many still believe that a true Air Gap exists, protecting critical industrial systems because they somehow can't be reached.

In reality, even a real Air Gap (if one truly does exist) is of little use in defending against cyber attacks, because cyber attacks have evolved past physical wires. Many assets that were not designed or intended to support wireless network communications include embedded Wi-Fi capabilities at the microprocessor level,[1](#fn1) which can be exploited by attackers ranging from the skilled cyber terrorist, to a disgruntled worker with an understanding of wireless technologies.[2](#fn2)

In addition, there is the high possibility that a threat could be walked into a critical network, stepping across the Air Gap with the aid of a human carrier. Only strong security awareness and strong technical security controls can truly “gap” a networked system.

### The future is now

“We aren’t allowed to send any data outside of our plant.”

You can replace ‘plant’ with ‘region’, ‘country’, ‘organization’, or whatever other arbitrary identifier you want. This complaint, ironically, often comes via email: which in most cases is a clear example of data being sent outside of the supposed boundary.

In reality, there are established and legitimate data flows into and out of almost any environment. The restriction might be real, but take the time to determine what data is being transmitted and what the specific risks and regulations are in a given circumstance. It might not be an issue at all, or there might be specific controls or countermeasures that are required.

### IIoT is not spelled with a “d” in it

“IT and IoT are the same thing!”

This is, of course, simply not true. However it highlights a growing problem in an industry with a real labor shortage (at least at the time of publication): people don't know what they don't know. If based on cursory Internet searches, without prior experience to guide you, it might be easy to believe that Operational Technology (OT) and the Internet of Things (IoT) are the same. While this example is fairly harmless, misinformation can be counterproductive or even dangerous. Luckily you've read [Chapter 3](../B9780443137372000099/CH0003_45-64_B9780443137372000099.xhtml) already, so this isn't you.

## Lack of proper operationalization

Cybersecurity requires people, process, and technology. However, it remains common for some companies to invest in one without the others. Unless all three are considered, it is impossible to fully operationalize your cybersecurity efforts, and you'll be left with highly trained people with no tools, or (more commonly) an abundance of tools without trained personnel to utilize them, nor the processes in place to make the most of what these tools provide.

### Schrödingers event logs

“We collect tons of security logs. When I log into one of the firewalls, I can see if there are any alerts there.”

Security controls create event logs, and some of those event logs could be extremely important. If you have tools creating events, make sure there are people looking at them, who have the right tools at their disposal to manage them effectively. It doesn't always require a huge investment (there are many open source options available), but event logs that aren't being managed are useless. Maybe useful in certain cirmstances? Both.

### Planning versus practice

“We have an extremely thorough cybersecurity response plan. It fills three binders.”

This is great except the person explaining this also admitted to never once having practiced that plan. If the first step required in the event of incident is to find and read three binders full of documentation, don't expect the rest to go well.

### Inadequate staffing

“I just made a huge investment in cybersecurity controls. It’s on that shelf over there because there’s no one to use it!”

I have witnessed “Security operations centers” with fancy dashboards on screens, but without anyone looking at them. In one case, there wasn't even a desk or chair in the room, indicating that no one *ever* looked at them. In another case, I saw firewalls still their boxes, covered in dust. They weren't spares; they had never been deployed. Most cybersecurity tools have an operational requirement. Those that are more straightforward (such as security events from basic controls like firewalls and anti-malware software) can be automated to a degree, but someone still has to make sense of them all. Those controls that are more prone to false positives may require several dedicated team members. Those that are never unboxed? They dont require a lot of effort to use, at least.

## Lack of awareness

Cybersecurity is a journey, and like all journeys it is important to know where you are and where you are trying to get to. Without some degree of self-awareness, it's easy to get lost along the way. And without some awareness of the world around you, you're likely to crash into something unexpected.

### Driving without a map

“We have a flat network that’s connected directly to the Internet, so we need the most advanced monitoring tools that money can buy!”

Not everyone's cybersecurity journey is the same, but as a rule it's best to implement the basics first. If you're connecting your network directly to the Internet, that should probably be solved *before* implementing something more advanced like an industrial network anomaly detection product or an advanced SIEM or XDR solution. Otherwise, there's going to be a lot more to analyze and a lot more event data to sift through as your network gets continuously pummeled by outside traffic.

### One-and-done

“We were told we had to put a firewall in. We did that years ago, so what’s the problem?”

Every step on the cybersecurity journey is important, but no step is the last one. If the next step that you need to take isn't obvious, consider bringing in an outside agency to perform an assessment of where you and where you need to be.

### We're not at risk

“This is all ‘nation-state’ level stuff … we don’t have to worry about any of this, we’re not that important.”

Unfortunately, the threat has evolved in many ways. First, the threat of ransomware has put *all* industrial operators at risk, because any company represents a potential pay-out for the bad guys. Second, the techniques available by adversaries — even those that aren't nation-state actors — are the same techniques that were considered “nation state” level threats just a few years ago. Third, if you defend against a larger threat than you expect you need, you'll be that much more likely to succeed.

### Driving too slow in the fast lane

“We finished a project this spring to map out security levels and create zones and conduits. In next year’s budget cycle we’ll put in the request for the segmentation project, and if we get the funding, we’ll start procurement in the following year …”

The threat landscape is always evolving. To use the “cybersecurity journey” analogy once again, it's important to try and at least keep pace with adversaries — because they're on a journey too and if you can't keep up you will fall behind.

### Passing on the right

“We need to implement this security control ASAP!”

Usually in response to an incident, a very specific security control will become suddenly urgent. While urgency isn't a bad thing — as just stated, there is a need to keep up — I've seen at least half of the pitfalls mentioned here made while rushing into a response without proper consideration.

## Misunderstanding vulnerability

Vulnerabilities are often a top consideration of cybersecurity professionals. As we learned in [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), however, vulnerabilities and risk in industrial systems (like most things in industrial systems) require special consideration.

### Paralysis by vulnerability analysis

“We haven’t been able to start the segmentation project, because we’re tasked with implementing a new patching process and we’re being held up patching our OT assets by uncooperative vendors.”

If there's something in your plan that is difficult, move ahead on other projects while sorting it out. Don't let one stubborn process (yes, patching OT assets can be difficult) get in the way of other important work.

### We've patched all the vulnerabilities

“We invested a lot into a patching process that lets us keep everything up to date, within 24 hours of an available patch. We’re safe now!”

In reality, there are unknown threats that cannot be accounted for. Therefore, no security plan is fully complete without some method of accounting for unknown attacks. Assume all critical assets are vulnerable, and plan accordingly. Many industrial control assets are still unavailable to the broader cybersecurity research community; it is reasonable to assume that there are vulnerabilities that have not yet been identified and disclosed. If a vulnerability is unknown, a vulnerability scan is not going to identify it … yet the vulnerability still exists.

### Software versus systems

“Patching our industrial assets is the absolutely most important thing to do.”

Similar to the belief that being fully patched equals being fully secure, there are many who feel that patching industrial assets such as PLCs is absolutely the most important thing to keep an ICS safe from attack. In reality, an ICS is by design a command and control infrastructure; if you get access to the ICS, the whole system is vulnerable to misuse. Patched or not, an adversary that has breached the ICS will be able to manipulate that PLC. Yes, it's important to patch systems to make direct manipulation of assets more difficult, but industrial cybersecurity requires a holistic approach.

## Worlds are colliding!

“IT” and “OT” have been converging, and will likely continue to do so. Along the way, there’s been a lot mistakes made — from both sides.

### Cybersecurity for OT is just like IT

“OT uses Windows servers and they’re no different than the ones used in finance or other business functions”

The hardware is often the same, and the operating system is often the same. Although both might be older (even eold enough to be unsupported). Some aspects of the opporating system — such as network drivers — may be proprietary in order to support the low-latency, real-time communication, and redundancy requirements of an industrial control system. And of course the control system software itself is highly specialized, to the degree that vendors will typically only provide support for tested and certified configurations. In short, even though two computers might look the same on the surface, the operational and cybersecurity needs are very different.

### All processes are fragile

“If you breath on an industrial network wrong, you could tip the whole thing over!”

This is true in some very specific scenarios (e.g., unexpected network traffic that introduces latency or consumes unnecessary capacity in real-time networks), but it is untrue in others (e.g., control systems that are designed for robustness and resiliency). If a cybersecurity control is needed (e.g., as determined by a risk assessment), test it. If it impacts reliability, instead of abandoning the control, consider how to improve reliability in order to accommodate it.

### My process is resilient: It's unhackable!

“A properly designed ICS will keep running smoothly no matter what you throw at it.”

The inverse use case is to have too much confidence in the design of the system. Even extremely resilient environments can be manipulated by a determined attacker. It might be more difficult, but an adversary only needs to find one weakness to potentially disrupt an otherwise robust system.

## The mistake that you are making right now

Too much reading, not enough practice

“I can suggest a good book on the subject …”

I'm fond of recommending this book to those looking to learn industrial cybersecurity. While this book is huge, and you are at the end of it, it unfortunately isn't enough. You  will never be able to know all there is to know. Industrial network security is a broad and complex subject, and you've done great to get this far, but cybersecurity is not a purely academic discipline: everything you just learned now needs to be put into practice. If you're reading this as an industrial operator who needs to understand cybersecurity better: get some hands on training to get a feel for what “hacking” really means, and to get comfortable with the tools of the trade. If you're reading this as a cybersecurity expert who is looking to understand what “OT” is all about: complete your safety training, put on your PPE, and get your boots dirty. Good luck!

## Summary

With the proper intentions, a well informed network security administrator can plan, implement and execute best-in class security measures for any industrial network …. But mistakes can happen, and they often do. Laugh, and learn!

---

[1](#cfn1)  Jason Larson, Idaho National Laboratories. Control Systems at Risk: Sophisticated Penetration Testers Show How to Get Through the Defenses. In: Proc. 2009 SANS European SCADA and Process Control Security Summit; October 2009.

[2](#cfn2)  Jacob Brodsky, Anthony McConnell, Marco Cajina, and Dale Peterson. Security and reliability of wireless LAN Protocol Stacks Used in Control Systems. Proceedings of the SCADA Security Scientific Symposium (S4). Kenexis Security Corporation, 2010. Digital Bond Press.
