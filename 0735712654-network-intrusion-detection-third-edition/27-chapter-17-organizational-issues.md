# Chapter 17. Organizational Issues

![Organizational Issues](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

What does risk management have to do with intrusion detection? Every organization either consciously or subconsciously makes decisions about risk. Obviously, we decide how much risk we are willing to accept ourselves. The distributed denial-of-service attacks that became widely known in February 2000 and Code Red attacks in 2001 demonstrate clearly that we also decide how much risk we are willing to accept on others’ behalf. The security of my site depends, at least in part, on the security of your site. This chapter lays the groundwork that will enable you to present a cogent argument to your management that intrusion detection is one tool for managing risk, or part of an overall security architecture. The highest and best purpose of a network intrusion-detection system is to identify the attacks being directed against our perimeter defenses so that we can ensure our systems are hardened to withstand these attacks. In other words, intrusion detection must serve as instrumentation that enables us to define the metrics we need to manage risk intelligently. This chapter also ties risk-management techniques and concepts directly to intrusion detection.

# Organizational Security Model

To manage risk, we need a model, a way of describing the problem and what needs to be done from a process standpoint so that we can get our arms around the problem. A simple example of a model is the Top Twenty list. You can find one at [www.sans.org/top20.htm](http://www.sans.org/top20.htm). It lists the top twenty vulnerabilities that attackers exploit and how to fix them. Every major vulnerability scanner looks for evidence of these. This is a simple model, listing the twenty vulnerabilities most often exploited. Make sure there are tools to find these vulnerabilities, and describe the fixes so that all users can repair their systems. If a significant number of people do this, attackers will have a much harder time compromising systems, and everyone’s risk is reduced. Alan Paller, a good friend of mine, created this model. Alan Paller is the Director of Research for the System Administration, Networking, and Security (SANS) Institute, and he developed another more complex model while on an international flight with some of the top security minds in the world. During the long flight to Australia, he continued to interview and question these individuals to develop a comprehensive security model.

While working with this model, I have been impressed with the results it gives after you take the time to implement it. As I reflect on the efforts and challenges of directing the startup effort that created the Global Information Assurance Certification (GIAC) certification and SANS Immersion training tracks, I am deeply thankful to have had a model like this to use. After twenty years of government service, adjusting to the speed we have to move at makes it hard to remember which way is up some days.

What to do? When I worked for the *Ballistic Missile Defense Organization* (BMDO), I used this security model to help me sort out the many contradictory priorities. In the government, everything is so ponderous that you need a roadmap to remember what you are trying to do. With SANS and the GIAC, everything is “practice what you preach.” If we teach it, we do it. So, I am trying to implement the same model in a startup world where everything changes everyday. I did not develop this model; Alan Paller, Gene Schultz, Matt Bishop, and Hal Pomeranz did, but I have used it in the past and it has worked for me. I offer it to you in the hope that it helps you as well. As I describe it here, I will put an ID slant on the model, but you certainly can apply it in a more general way. [Listing 17.1](ch17.html#ch17pro01) shows the results of their work (courtesy of Matt, Alan, Hal, and Gene). Let’s take a look at it. Instead of three steps (determine the top twenty vulnerabilities, scan or test for these vulnerabilities on your systems, and fix these vulnerabilities if they are present), this model has seven steps.

**Procedure 17.1. Listing 17.1 The Seven Most Important Things to Do If Security Matters**

1. Write the security policy (with business input).
2. Analyze risks or identify industry practice for due care; analyze vulnerabilities.
3. Set up a security infrastructure.
4. Design controls and write standards for each technology.
5. Decide which resources are available, prioritize countermeasures, and implement the top priority countermeasures you can afford.
6. Conduct periodic reviews and possibly tests.
7. Implement intrusion detection and incident response.

## Security Policy

Wait! Please don’t close this book just because I wrote the words *security policy*. From my experience training analysts and teaching classes on intrusion detection, I know that the last thing an intrusion-detection analyst wants to do is write a security policy. When I teach, if I say “policy,” I can see the eyes glaze over instantly. But applying filters to an IDS is kind of neat, right?

Consider that the filter rule set you upload to a sensor is called a policy. This is true for most other commercial systems, and it is well named because these filter sets *are* a security policy. A firewall is just an engine that enforces network policy. So let’s recalibrate ourselves not to think of security policy as a pile of paper that took weeks to write and now sits gathering dust. For an intrusion-detection analyst, a security policy is a permission slip, the organization’s approval to install dynamic and active policy in security engines, such as firewall and intrusion-detection systems. That’s right, policy can serve as permission to do the right thing! At its heart, an IDS is a monitoring device and you should never monitor people without authorization. Policy is the umbrella that covers us when we execute the steps to actually use an IDS effectively.

## Industry Practice for Due Care

Both risk and vulnerabilities are discussed further, so for right now, let’s focus on due care, or *best practice*. Actually, I abhor the term best practice, perhaps we can use pretty good practice instead. Although every organization has pockets of expertise, no one group has all the answers. As you know, the technology rate of change is so high that none of us can keep up across all the subject areas. The best solution to this problem is to learn what people are doing and what is working for them. One of the greatest joys for me in being affiliated with the SANS Institute has been the consensus projects. Many of them are called *Step by Steps*, such as *Securing Windows 2000—Step by Step*. These are not the work of a single person, but many committed professionals who come together on a project to share their knowledge with others.

## Security Infrastructure

Robert Peavy, the Director for Security and Counter-Intelligence for the BMDO, prepared a talk for the Federal Computer Security Conference titled, “Security as a Profit Center—How to Sell Protection to Your Leadership.”

As much as anyone I have ever met, Robert Peavy understood that security, good security, requires people. This is at least as true in the intrusion-detection field as any other security domain. Intrusion-detection analysts are front-line troops. They often feel personally responsible for any attacks that penetrate an organization’s defenses and compromise systems. They get burned out and there are some turnover issues, especially if they are double-hatted with incident response as well. They need training to remain aware of the latest attacks, but there is limited high-quality training available for them. What does all this mean? It means the wise organization has some depth for the role of intrusion-detection analyst and that takes a security infrastructure to accomplish.

## Implementing Priority Countermeasures

As I am writing tonight, I have a great fear. I have run vulnerability scanners at a number of organizations that have both UNIX and now an increasing number of Windows 2000/XP computers. I am shocked by the number of systems that still have well known vulnerabilities as well as the number of systems that still have SNMP; and it has been two weeks since the CERT advisory on SNMP and the PROTOS test kit was released that searched for thousands of problems. Will this be the next rstatd?

Since 1997, an ever-growing number of Sun Solaris UNIX systems continue to be compromised using a buffer exploit against the rstat daemon. Several buffer-overflow exploits are available for DNS, so it certainly could happen. Last week, I scanned a UNIX system being placed outside a firewall. It had the Echo, Chargen, portmap, and r-utilities open. It reminded me of elementary school when we used to put those signs on our classmates saying, “Kick Me.”

How do you know whether something is a priority countermeasure in a world where everything is the number-one priority? If an attacker can exploit a vulnerability from the Internet as easily as a hot knife slicing through butter, you have to decide whether you want to fix the problem before or after the system is compromised. I continue to be astounded by the number of organizations that do not have time to do it right, but they do have time to do it over.

## Periodic Reviews

Wake up! If you are an intrusion-detection analyst, do not miss this! It is imperative that you review your filter set from time to time. When I worked on the Shadow intrusion-detection project, one of the things I forced myself to do every couple of months was to run the complement of our filter set against a week’s worth of data and manually parse through the results looking for anomalies. We must strive to continue to enhance our filter sets to reduce false negatives. If this month’s set of filters is picking up exactly the same attacks as three months ago, this is a bad sign.

So, besides setting filters to trap the things one normally ignores, how do we improve our filters? The bugtraq mailing list has proven to be an excellent source of information about new attacks, each of which might need new filters. Once again, if you can find another group doing intrusion detection and striving to do it well, and you can exchange information, as this is another excellent way to stay current.

Conducting periodic reviews is a more general security principle than just watching our filter set, of course. The intrusion-detection analyst also profits by examining the firewall filter set on a fairly regular basis.You might find what I call firewall creep. When the firewall was first installed, it had a fairly tight and orderly ruleset. As time goes on, however, this business interest and that new service become a set of exceptions, or modifiers, to the ruleset. As the rules grow, it becomes harder and harder to validate them. Also, from time to time, the firewall administrator might add in a special rule “just for testing” and forget that it is there. As an analyst you think, “No problem, we are blocking UDP port umpty clutch,” when in fact you aren’t. The real difficulty is tracking these changes; they happen when you least expect them and over a long period of time, a bit like a low and slow scan. I am starting to think that external scanning services with databases, so you can track what has changed, are a must. If you have never considered one of these, you might want to visit [www.qualys.com](http://www.qualys.com).

## Implementing Incident Handling

An exhaustive discussion of incident handing is beyond the scope of this book, but I want to touch on it as it relates to the model. Have you ever been certified to administer CPR? How confident would you feel if you had to administer CPR 3, 6, 12 months after your training? I call these “gulp” moments. I know I am qualified as an incident handler in some sense, but if I haven’t handled an incident in a couple of months, I really feel the rust.

What does incident handling have to do with intrusion detection? A lot! The analyst is likely to be the one to raise the alarm. In organizations with structured incident-handling capabilities, the analyst might be assigned to provide network information to the handlers. In organizations without these structured incident-handling capabilities, the handlers are likely to be you and a system administrator or two. In the “[Manual Response](ch18.html#ch18lev1sec3)” section of [Chapter 18](ch18.html), “Automated and Manual Response,” read carefully and make notes concerning the things you know you need to do before you have to handle a serious incident. If you do this, it will really help when the gulp moment comes.

# Defining Risk

What are the scariest three words an intrusion analyst is likely to hear?

We can’t reasonably manage risk if we don’t know what risk is. Risk occurs in the domain of uncertainty. If there is no uncertainty, there is no risk. Jumping out of an airplane two miles up without a parachute isn’t risky; it is suicide. For such an action, there is a nearly 1.0 probability you will go splat when you hit the ground, or an almost 0.0 probability you will survive. However, there is also risk to jumping out of perfectly good airplanes with parachutes, as several skydivers discover each year.

Let’s apply this concept to router protection filters. In many cases, these filters are connection events—that is, they are port number based. If we see a TCP connection at port 25, we identify it as sendmail and take whatever action is prescribed. However, any service can actually run at any port. There is the uncertainty; there is a risk that we will make the wrong decision. With the ephemeral ports (above 1024), this happens often. This uncertainty, coupled with the fact that an adverse action could be exploited (a service we intended to block could penetrate our site), leads to a risk. This is one reason many security professionals think that a filtering router does not serve as a firewall.

An intrusion-detection analyst needs to know the degree of uncertainty for specific filters. As an example, SYN flood filters often have a high degree of uncertainty. If an intrusion-detection analyst continues to report these, there is the potential for an adverse action. The CIRT might begin to trivialize this analyst’s reports. Therefore, a filter’s degree of uncertainty can result in risk to the analyst and the organization, especially in high-profile cases. Conversely, the expert analyst knows the conditions in which a filter is likely to perform well and also the conditions that lead to failure. These analysts develop the ability to “read between the lines.”

Perhaps, the simple issue of reputation doesn’t grab you. The same problem, uncertainty of filters, gets more interesting if a site employs automated response techniques.

I want to briefly mention one more potential adverse result of uncertainty with intrusion-detection filters. Several commercial IDS vendors provide lists of their filters. Sometimes, they rate their filters by their probability of producing a false positive and perhaps list conditions known to cause the false positives. This is a great service to the analyst. What if a company lists some of its filters as not having any chance of a false positive—that is, there should be no uncertainty, therefore there is no risk. Then, you dig in and find several of these filters do generate false positives. That realization can undermine your confidence in the company. I know; it happened to me. In fact, I started building test cases for the filters that according to the literature had no chance of a false positive and found several other filters had flaws. Well this really bugged me. Why say it doesn’t error if it does? Then, I remembered that I had been issued a brain to keep my heart in check. Why get mad at this company when they have the most complete filter documentation of any commercial IDS? So, I just updated my copy of the filter documentation and sent them traces of my test cases. What do I get for my effort? I know a lot more about which detects to be uncertain about and the conditions likely to cause the filters to error and generate a false positive.

What about the Snort ruleset? It is open and can be examined and has been subjected to exhaustive public review—are these rules uncertain? To be sure, there are great advantages to public review (and you can bet that more than one or two of those rules finds its way into other IDS systems), but the fact that it is open means an attacker can be aware of it and modify the attack just enough to evade the rule.

Oh yeah, the scariest three words to an intrusion-detection analyst. They are when the gruff old decision-maker who has to make a hard call looks you in the eye and asks, “Are you sure?”

# Risk

Risk happens. It is ridiculous to say I don’t want any risk in a given situation. Rather, we manage risk. I heard on TV once that the space shuttle often has backup systems for its backup systems. A shuttle flight is an exercise in strapping yourself to a rocket and heading for space. Space is an environment where any number of things can kill you: radiation, heat, cold, vacuum, and finally the reentry. If you approach a reentry with too steep an angle, the mistake will crash you; and if your angle is too shallow, it will bounce you into space. That is a lot of risk, which is one of the reasons astronauts get all the free Tang they can drink.

If you really think it through, the whole process is nuts and no sane person would do it. NASA actually has go/no go criteria. If anything is wrong, they do not go ahead with the launch, even though there are backup systems. This is judged an unacceptable risk. Other risks are considered acceptable, like the bit about strapping yourself to a rocket. With any risk, we must decide how we will deal with risk. We have three options for dealing with risk:

- Accept the risk as is.
- Mitigate or reduce the risk.
- Transfer the risk (insurance model).

## Accepting the Risk

If we don’t install a firewall and we connect to the Internet, in some sense we are as daring as the men and women who bolt themselves onto rockets; what we are doing is risky and we’ve chosen to accept that risk. If we have information assets of high value and we don’t do auditing on these hosts or use some form of intrusion detection, we are again choosing to accept the risk.

The concept of accepting risk is simple enough, but there is another aspect of this we need to consider. The elementary school bus driver who drinks a few too many beers before picking up the kids with his school bus is accepting risk all right, but he is accepting risk he does not have a right to accept. The firewall administrator who was just testing some service and mistakenly left it in the system might have caused the organization to accept a risk that it would not choose to accept. After all, why did it go through the trouble to buy and set up a firewall? One of the interesting problems of information security is that it is quite possible for an individual to accept a risk for an organization that he is not authorized to accept. I would like to illustrate this point with an intrusion-detection story.

Last week, we detected systems initiating file transfers from a site that we monitor. It was just odd enough that we decided to look into it a bit further. When we examined the payload of the ftps, it was clear each of these systems was sending a bit of information about itself. We weren’t sure what the information was until we saw a couple instances of “Preferred Customer.” It seemed like it had to be the registration field for Microsoft Office products. Our suspicions were quickly confirmed. A member of Human Resources had sent a memo as an attachment to an email message to all the senior managers of the organization. It was the fact they were senior managers that alerted me to further investigate the ftp sessions; these folks didn’t even read their own email! They had a secretary screen their mail, print it, and put the important messages in their inbox. The email message sent by Human Resources was infected with a macro virus that sent information out of the organization. It apparently didn’t do any serious harm. From an information warfare perspective, however, I was appalled, because it gives a clear potential infection vector into this organization, which could be exploited at a later time. This support employee, by just failing to maintain current virus software, accepted a high degree of risk for the entire organization. As Jimmy Kuo, a research fellow at NAI would say, “You are only as good as your last update.” How about one more example?

The same week we detected many more systems initiating file transfers than usual from the same site we monitor. We found five in one day. When we pulled the payload, we found they were all going to the same IP address, the same user ID, and the same password. They were downloading files to the desktop systems. In this case, it turned out to be a shareware program, PKZip. Now, this is no Trojan; this is no sneak attack. A paragraph on the shareware web site stated that when PKZip was installed it came with a bonus component that downloaded ads. None of the five users gave a second thought to what they were actually doing; they just wanted PKZip. So what’s the problem? Well, so long as the software is just downloading ads, there isn’t a problem. However, keep in mind that many sites configure their firewalls so that if a connection is initiated from the inside, it passes through the firewall without any problems. This means there are several potential attacks from such a behavior.

### Trojan Version

We have seen several examples of Trojan versions of legitimate software, such as the Trojan ICQs and Internet Relay Chat (IRCs). The user would not be aware that the program was actually uploading sensitive data from the system, or downloading tools that could be used to attack his organization’s network from the inside.

In the same vein, what if the advertisement company hired a malicious individual, or an expert in economic espionage? Think about what he could accomplish with robot code that downloaded arbitrary files every time a system was booted! If this seems like science fiction, consider the use of netbugs ([www.bugnosis.org](http://www.bugnosis.org)) and spyware that is so common today.

### Malicious Connections

There are a number of DNS attacks, but the idea in DNS cache poisoning is to manipulate the DNS system so that the client system goes to a malicious server rather than to the actual server. This is often done when a client answers a question, within a query.

The problem is complex; users of desktop Windows systems do not generally know what connections their systems are making. I honestly didn’t know that software programs on my Windows system could connect to the Internet without me clicking on them. Several years back, I bought a software package, McAfee Office, primarily to get the Pretty Good Privacy (PGP) that comes with it, but decided to play with most of the software. One of the programs was called GuardDog, which is a security program for Windows systems. I installed it, and imagine my surprise when I booted my computer and it barked at me, to warn me that one of the programs on my system was trying to connect to the Internet. It was Real Audio; I didn’t have the time to set up monitors and traps in my home lab to track it, so I just uninstalled it. Later, it turned out they were collecting information on users. Today, I use application-aware personal firewalls such as ZoneAlarm and Norton Internet Security.

We have gone through some important information, so let’s take a second to summarize some points. In the preceding two examples, macro virus and PKZip, users’ desktops initiated connections to the Internet without the users knowing about the connections. Both cases have the potential for harm to the organization, although mercifully the only real damage in these examples was my blood pressure shooting through 200. In both cases, one by inaction, one by action, the users make a personal decision to accept a risk that affects the entire organization.

**Expanding Our View of Intrusion Detection**

Neil Johnson, a researcher and faculty member at George Mason University, presented a really wonderful paper on intrusion detection and recovery against watermarked images at the SANSFIRE 2000 conference. If you spend a lot of time and money creating graphics, you might want to put a copyright seal on these graphics in some way. There are tools to do this. Then, it is possible to use World Wide Web worm technology to search the Internet looking for graphics to see whether your seal turns up on some server that didn’t license the graphic. Neil explained this and demonstrated both attacks and the recovery techniques. Now, you might be thinking, what do watermarks have to do with intrusion detection?

As we continue our study of risk and its application in the field of intrusion detection, keep in mind that the dangerous enemy is not the one aimlessly running three-year-old canned attacks! The dangerous enemy is the one who knows what he wants and uses a hard-to-detect technique to get it. *USA Today* ran a story in the wake of 9/11/2001 that Bin Laden used steganography to send messages related to the attack. There are more pragmatic examples. In the case of a graphics company, its images are its crown jewels. To the company, this is the nightmare scenario: an attacker who can remove the proof that it is the owner of the images and possibly even brand the images under another company’s name.

## Mitigating or Reducing the Risk

What if we decide that even though it is risky to strap ourselves to a rocket, the end result of doing so is worthwhile? Perhaps our objective is greater than just a free drink of Tang; perhaps we have an opportunity to be the first human to set foot on Mars. The enterprise is still very risky, but we are certain that this is something we want to do. In this case, if we aren’t foolhardy, what we do is try to find ways to make the endeavor less risky; we reduce the risk.

Have you ever thought about intrusion attacks against laptop computers? Most professionals carry them these days. They often have sensitive information about their organization on them. We have already mentioned information-gathering malicious code, but that can be directed against any system. How specifically are laptops vulnerable to attack? What can you do to mitigate their vulnerability?

### Network Attack

If the organization uses Internet service providers (ISPs) to connect for email rather than secured dial-in, there is an opportunity to attack the organization’s systems while they are on the net. They are outside the firewall and so the normal screening protections against NetBIOS and other Windows attacks that desktop systems enjoy inside the firewall are not available to them.

### Snatch and Run

I really hate putting my laptop on the X-ray machine conveyor belt at airport security checks. If I don’t make it through the metal detector, this is a golden opportunity for someone to steal it because I am physically separated from my briefcase in a dynamic, crowded environment. Worse, I only have one shoe on because thanks to the terrorist that tried to blow up the airplane with his shoes, mine are being inspected. Further, if someone does walk off with my laptop if I rush after them, I run the risk of getting shot by the National Guard with the M16s. There are also the situations when I get to my destination: Do I leave it in my hotel room when I go to dinner, or lug it?

I don’t know whether you are worried about the information that professionals in your organization put on laptops. After all, it is just stuff such as your design and business plans, sales and marketing information, perhaps a bid work-up or two. I write this tongue and cheek, but if you interview the folks who lug these laptops around, you might find that they do not often perceive the information on them as sensitive and needing protection.

I do know my situation. In writing, teaching, and reviewing I often find myself working with proprietary information. I have signed several Non Disclosure Agreements and have always tried to be careful with that information. If a large security and network company decides I have not protected its information properly, I have to face its army of lawyers (alone). So I am inspired to do the best job I can to protect my laptop; I look for tools to mitigate the risk. Because I know that connecting to the Internet is risky, what are some of the tools that help protect my system?

I have looked at several tools. ZoneAlarm is free for personal use and works well. A lot of my friends swear by BlackIce, and the traces it creates have nice fidelity; but, it has steadily dropped in quality since the company was acquired. I have found the Norton Internet Security tool actually runs on XP, which is a plus. PGP appears to have a personal firewall, but my boss installed it on his XP and lost his ability to connect to the Internet. I went through that with Windows ME when I installed PGP. In both cases the culprit was the PGPNet product. With the ME computer, I thought about it for a while, I knew I needed PGP, but was pretty sure I didn’t need ME so I just wiped out that system and rebuilt it as a Windows 2000 system. PGP also comes with PGPdisk that protects sensitive files should the laptop ever be stolen or suffer an intrusion, or you can use the Microsoft Encrypting File System on Windows 2000 and XP. Although PGP has a disk overwrite, data-destruction routine, I find BC Wipe from [http://www.jetico.sci.fi](http://www.jetico.sci.fi) to be a better tool for my purposes. There, that is my personal example of implementing countermeasures to mitigate risk.

## Transferring the Risk

Last week, when I wasn’t dealing with outbound ftps, I was dealing with flood damage. The toilet upstairs got stopped up (with a little help from my teenager). The chain that drops the stopper just happened to chink and not drop the stopper flush to seal the water. So, the water filled the toilet bowl and poured over onto the bathroom floor and began its journey in search of sea level. But wait, there’s more! This happened to be the day the city decided to flush the fire hydrants, which stirs up all kinds of rust, so it wasn’t clear water pouring through the house; it was blood red. When my wife got home, the water was pouring from the dining room chandelier like a fountain. The plaster ceiling had huge cracks and the wooden floor had already warped in two places. The water continued on, accumulating until the ceiling of my wife’s sewing room collapsed, spewing rusty water and soggy ceiling tile on her machine and the projects below. My wife called me at work, asking where she should begin. “Turn off the water, move away from the dining room, I’m on my way,” I answered.

I use the same incident-handling technique for everything. As I hung up the phone, it hit me that this had to be 20 to 30 thousand dollars worth of damage. I was very sad as I drove home and then busy as we tried to salvage what we could of my wife’s sewing room. It wasn’t until later at night that it hit me. I have insurance! In fact, I have insurance with a good company, one that has always treated me well. I always knew owning a home had risks that were beyond what I could financially accept. There just aren’t good enough home firewalls to expect them to defend against toilets that get jammed and stuck on a day that the city is purging the fire hydrants. Like most homeowners, we had chosen to transfer the risk. So I called Travelers. They came over, were very sympathetic, and said they were going to take care of us. Sure enough, I was only out $100 for the deductible; and the job would have been done except that no one told my wife the five little words you never say to a contractor. Still, even after a “while you are at it,” it only cost me an extra $2,500 and now I have crown moldings on the ceiling, something I am sure I always wanted.

So how does this notion of transferring risk apply to information assurance and intrusion detection? In the first place, there is a direct correspondence. Several agencies, including Lloyds and IBM, are now offering hacker insurance. They usually require the organization to do its part before insuring them, and their part is likely to include firewalls, vulnerability assessments, and intrusion detection, at least it would if I were offering such insurance.

We have discussed uncertainty and how it applies to risk. We have proposed that some risks we are willing to accept (whether or not we are authorized to do so), and other risks we are not willing to accept. In the last case, we need to either mitigate the risk or transfer it. Now, we need to deal with the issue of what agent is going to potentially do us harm; we call this the threat. Vulnerabilities are the gateways by which threats manifest themselves.

# Defining the Threat

“Umm, I wouldn’t go there if I were you”.

“Why not?”

“Bad things will happen to you if you go there.”

“What bad things?”

“Bad things.”

This is not a compelling scenario, true? Most of us would not be persuaded by it. Imagine giving a similar pitch to management: If you don’t fund an intrusion-detection system, bad things will happen to us.

We need to define and quantify bad things:

- What things?
- How bad?
- How likely they are to occur or repeat?
- How do you know?
- What support do you have for your answer?

So for each threat we can define and enumerate, we need to answer these questions.

## How Bad—Impact of Threat

In the end, risk is evaluated in terms of money. This is true even if life is lost; in the case of loss of life, it might be a lot of money. For any threat we have defined, we take the value of the assets at risk and multiply that by how exposed they are. This yields the expected loss if we were to get clobbered by the threat. This is called the *single loss expectancy* (SLE) and the formula to calculate SLE is as follows:

```
Asset value × exposure factor = SLE 
```

The exposure factor is an estimate, ranging from 0 percent to 100 percent of our loss of the asset. Consider the following calculation, the threat of a nuclear bomb exploding just above a small town whose total assets are worth 90 million dollars:

```
Example Nuclear bomb/small town ($90M × 100% = $90M) 
```

Now let’s bring it home. I have already mentioned that when I have conducted vulnerability scans of sites with UNIX computers I have found a number of systems with the tooltalk vulnerability. Can we apply this formula to these? First, we have to define the threat. Suppose we are a Class C site. The threat is a malicious attacker who gains root, exploits any trust models, encrypts the file systems, and holds the computers ransom for $250,000. The attacker scans the net and finds six vulnerable systems. The buffer-overflow attack quickly yields root. After exploiting the trust models of these systems, our attacker is able to root compromise four additional systems and therefore encrypt the disks of 10 UNIX workstations. So when the CEO of your organization comes in to work on Monday, his secretary finds the following in his email box:

```
To: John Smith, CEO 
From: Dark Haqr 
Subject: Rans0m 
I 0wN U L^m3r  It wi11 c0st u a kwart3r Mi11i0n t0 g3t ur dAtA b^k. 
```

What is our SLE at this point? We could say $250,000, but it might not be quite that simple. If there were backups, we might be able to restore from backups and just lose a day or two of work. If there aren’t backups (please, please ensure there are always backups), we have a more interesting problem. At this point, we don’t actually know if we will ever get the encryption key. The threat is that we will not. So, the value of the assets is the value of the data on these systems, plus the time to rebuild them from scratch, plus the loss from the downtime. How do we calculate the value of the data?

The value of data can be approximated by the burdened labor rate of the people who have been working on the system for the life of the project(s) on the system. To keep the numbers simple, we will consider each of the UNIX systems to be a professional’s desktop. They are working on a single project that is two years along and they each make $60k, but their burdened rate (benefits, office space, and so on) is $100k. Ten people at $100k, for two years is $2 million dollars. What is our degree of exposure? It’s 100 percent; the files are already encrypted. So, we quickly see that paying the quarter million and keeping our big mouths shut and not involving law enforcement is probably in our best interest. So in this scenario, we pay the money, get the key, and get back to work and everyone is happy. Now, what happens if we don’t fix the vulnerability?

## Frequency of Threat—Annualized

*Annualized loss expectancy* (ALE) occurs when a threat/vulnerability pairing can reasonably be expected to be consummated more than once in a given year. In a brief given to the Joint Computer Security Conference in March 2000, Dr. Gene Schultz postulated this might be an inadequate measurement. Given the nuclear bomb example in our small town, this can’t happen; indeed, we drop as many bombs as we want on the town, but we aren’t likely to cause any further damage. ALEs fit very well into models such as shoplifting, returns in the mail-order business, and defaults on loans. In a competitive environment (e-business, for example), however, how many ALEs events can you survive? Consider the case of distributed denial of service. If your web storefront is shut down four or five times in a month, some of that business goes to your competition. How do you recover from that? How do ALEs factor into information assurance and intrusion detection?

I mentioned earlier that intrusion-detection technology is easily applied to unauthorized use detection. I also think that this can be a waste of skilled intrusion-detection analysts. But, there is a powerful business argument that says this is a very wise use of the system and personnel. As we work through the following example, note that even though I kept the numbers ridiculously low, we still ended up with some serious money, enough to pay the burdened rate of those entry-level professionals the organization says it can’t afford. Use the following formula to calculate ALE:

```
SLE × Annualized rate occurrence = Annual loss expectancy 
```

This is nothing more than our SLE times the number of times it could be expected to occur in a year. This is why we ended the encrypted file system example with the question, “What happens if we don’t fix the tooltalk vulnerability?” Dark Haqr takes our money, goes out and buys a Beamer, his friends inquire of the means of his sudden fortune, and we get to play the game again.

Let’s do a common example: Web surfing on the job rather than working. First, we need to calculate an SLE. Say we have 1,000 employees, 25 percent of which waste an hour per week surfing:

```
$50/hr x 250 = $12,500 
```

To calculate the ALE we observe, they do it every week except when on vacation:

```
$12,500 x 50 = $625,000 
```

You can see why an organization might want to leverage its investment in intrusion-detection equipment and personnel to curb unauthorized use. Again, I kept the numbers much lower than what I have observed to be the case at many sites. Also, in the real world, the waste doesn’t tend to be spread evenly across employees, but rather is localized in a small number of employees. If these employees can be identified and canned (after all, if they weren’t working, they probably aren’t really needed), there are a number of potential savings for the organization.

## Recognition of Uncertainty

How reliable are the answers from these SLE and ALE calculations? If we are going to make decisions based on these calculations, we need to know how reliable they are. I spent a long afternoon with a gentleman who was trying to convince me to invest a lot of money in an intrusion-detection framework. This thing would do everything but wax your car: it had sensor fusion, automated correlation of vulnerabilities with incoming attacks, and even factored in virus reports in a very cool graphics display. “Best of all,” he says, “it has an expert system.”

He continued talking and I nodded from time to time, but I was already gone. I couldn’t help but remember phrases from my artificial intelligence (AI) classes. How about this one, “The reason expert systems don’t live up to their promise is that the rules we are putting in them aren’t very good. The knowledgeable engineer interviews the experts in the field, but what we are learning is that the experts aren’t very expert.” Here is another, “One of the biggest problems with AI is when the system doesn’t know what it doesn’t know. In that respect, AI systems are exactly like people.”

When we calculate SLEs and ALEs, we need to be sensitive to what we don’t know, to the places we fudge the numbers, to the cases where the models just don’t fit. “No problem,” you might be thinking. “I have no intention of calculating SLEs.” Umm, maybe you do something similar, but you do it in your head without a process or documentation.

I work in an organization that monitors networks, for instance, although I guess that doesn’t come as a surprise. I was listening to a new employee briefing and they were told very clearly that pornography was forbidden and that if caught, the responsible employees would probably be escorted out the door and fired. Let’s jump into the mind of one of these young new employees. Maybe he is curious to see whether the organization can detect him if he misspells a sexually oriented word on a search engine, or uses oblique references. The answer is probably yes. But then again, he might think, “Hmmmm, but I already know they don’t have a sense of humor, the SLE is just too high.” Well, maybe he wouldn’t use those exact words, but you get my drift.

Might I share one more example of uncertainty in answers with you? In mid-February 1999, I attended a working group for *Presidential Decision Directive 63* (PDD 63). The goal was to get the 50 or so top researchers (and me) to consider four problem areas necessary for allocating approximately half a billion dollars in research money for intrusion detection and information assurance. One of the tracks was called anomalous behavior, which is Washington D.C. speak for the trusted insider problem. So, we all worked away and then presented our results. The anomalous group presented a finding that research had been funded 100 times more for detecting outsiders than insiders. Someone asked, “What study did you find that ratio in, and what was your source?” The answer from our distinguished scientists was “We made it up, but it’s close.”

# Risk Management Is Dollar Driven

If you approach management and say you need $10,000 for an intrusion-detection system, they might want a bit more information. It is a good sign if they ask how much time it will take to run such a system; it shows they are listening and thinking clearly. A good manager knows the hardware and software costs are the tip of the iceberg and wants to get a handle on the whole picture. Managers want to understand how it fits into the business model. Risk management (and that includes intrusion detection) is dollar driven.

Whenever we are faced with a risk that is unsavory to us, we begin to wonder what can be done to reduce or mitigate the risk. As we pick our countermeasures, we should try to calculate what they would cost on a yearly basis. When you make a proposal to management, people really like it if you can give the cost breakdown and even an option or two. Remember those SLEs and ALEs; this is when they really come in handy. The countermeasure will cost some money, but look at the risk metrics!

Here is a very important aspect of pitching risk management to the organization’s management: Don’t nickel and dime. The bigger picture you can paint of all the risks, vulnerabilities, countermeasures, and get-well plans, the more receptive they are likely to be.

# How Risky Is a Risk?

I really like to hear host-based intrusion-detection sales folks give presentations. It has always been an uphill battle, and in these days of personal firewalls where anyone that wants host protection can get it for $40 to $60, it is becoming comical! The sales people get going on the insider threat and play that issue like a harp with one string. They have to do this; they are fighting a perception problem, or perhaps it would be better to state this as an education problem. What they are trying to do is get the potential customer to rate one risk higher than another. If you think about it, this is a common sales tactic.

In Virginia, they don’t get much snow, but at the beginning of winter, the auto ads are really pushing four-wheel drive vehicles. Never mind the fact that they cost more, are more mechanically complex, and get fewer miles per gallon than two wheel drives; if you buy one, you don’t have to be afraid of the snow. We can learn two things from this: to consider as many risks as possible and to keep things in perspective. We want to be able to rank risk. There are two basic approaches to ranking risk: the quantitative and qualitative approach.

## Quantitative Risk Assessment

The goal of this approach is to figure out what the risk is numerically. The most common way to do this is asset valuation using our friends the SLEs and ALEs. This is not worth doing for each desktop system in your organization! It can be a very effective tool at the organization level, however, and the numbers are not that hard to dig up. To calculate asset value (AV), use this formula:

```
AV = Hardware + Commercial software + Locally developed software + Data 
```

Your comptroller should be able to produce your organization’s hardware and software budget and actuals in a matter of minutes. The value of locally developed software is usually a bit trickier. You have to take the burdened cost of everyone paid to develop software for your organization for some number of years. Data is where it gets interesting! Isn’t it true that almost everyone in your organization uses a computer? If so, the value of the data is what your organization has paid to keep those people in front of computers for whatever is a reasonable life cycle for the data. (I usually use three years.) This is going to be a big number! It shouldn’t take longer than an hour to hammer out a reasonable value for your organization’s information assets. This can be a really good thing to have available if you need to persuade management to fund something, or to quit doing something really risky.

## Qualitative Risk Assessments

You can also apply a checklist approach to ranking risk. Generally, you have a list of threats, and you rank each item as a high, medium, or low risk. This works much better at the system level than the organization level. There are examples of a modified quantitative method and several checklist style qualitative method risk assessments at [http://www.nswc.navy.mil/ISSEC/Form/AccredForms/index.html](http://www.nswc.navy.mil/ISSEC/Form/AccredForms/index.html).

The accreditation “part II” forms at the web site are for the various architectures (Windows 95, NT, Macintosh, UNIX) are the qualitative method examples. The SCORE checklists at [www.sans.org/SCORE](http://www.sans.org/SCORE) are another resource. Finally, the Center for Internet Security [www.cisecurity.org](http://www.cisecurity.org) has a number of tools that you can run to assess your security posture. These tools pretend to be quantitative because they give you a numeric score; but if you look under the hood, you will quickly realize they are qualitative.

## Why They Don’t Work

In theory, both approaches to risk assessment work fine. In practice, they do not work so well. This is because we have a natural tendency not to tell the truth, because if we do show there is a vulnerability with a high risk, we have to do something to fix it. Therefore in practice, people who are performing a qualitative assessment come up with numbers that are really big. They know they cannot afford that much risk, so they do the assessment on smaller and smaller chunks until they get it down to the single desktop system, and that is silly! Guess which box (high, medium, or low risk) folks doing a quantitative assessment tend to pick. And if everything is a low risk, why bother?

# Summary

From the time of the Cuban Missile Crisis to the fall of the Berlin Wall, if you were in the Department of Defense and you wanted money, the strategy was to go to Congress and say, “The Russians are coming.” Despite the way TV and the movies portray the legislative branch, those folks aren’t dumb and a lot of them have been on the hill for a long time. So at some point, they start pointing out that they funded this and they funded that all because the Russians were coming. Why hasn’t that fixed the problem?

Now, we are doing it all over again to stop terrorism, or for the purposes of this book, to stop cyber-terrorism. If you don’t need your year’s worth of food and water and your thousand rounds of ammo for each gun to survive hackers, you certainly are going to need these things to survive the coming cyber-war. Sigh. This will work to extract money and attention for a season, but it is poor practice. This chapter has covered a sound organizational security model. We have looked at tools to assess and prioritize risk. We have a foundation for discussing what we do and why we do it with management. The next chapter discusses responses to attacks and system compromise. When we have these tools solidly in hand, we can discuss how the hackers are coming and how to survive a cyber-war in a reasonable manner.
