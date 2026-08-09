# Chapter 2. New Approaches to Cyber Security

**IN THIS CHAPTER**

- **Understanding the current nature of the threat**
- **Learning new approaches for dealing with the threat**
- **Identifying the mindset that is needed to properly secure an organization**

What makes security so exciting is that it is not static. It is always changing and new. Techniques that worked last year to secure a site are no longer effective. Therefore, it is important to constantly understand the mindset of attacks so new strategies can be created.

This chapter will introduce you to general trends and the mindset needed to protect an organization. A firewall and/or intrusion detection will not protect a site if it is not focused on the correct risks and configured to protect against high-likelihood threats. Only by understanding the problem can an organization create an effective way to deal with the problem.

# General Trends

No matter what field you work in, you can't help but notice the impact that the Internet has had on society. It has opened up opportunities and markets that people only dreamed of before. As with any new technology there are always positive and negative aspects to this. The positive side is the tremendous number of business opportunities. The negative side is the huge security risk now posed to so many companies—a potential danger few companies are truly aware of yet. It's like getting in a brand-new car and driving down the road at 80 mph, only to realize that the engineers did not equip the car with brakes. If a lot of cars were sold, the number of fatalities could be high. Something similar is occurring with the Internet. Companies have invested millions of dollars in it, only to find that proper security is not always built in, leaving their companies vulnerable.

Companies are vulnerable for several reasons, but a main one is lack of awareness. Often they have not realized the threat. If you are a soldier caught without your weapons you won't be able to defend yourself. On the other hand, if you are properly trained on weapons and know the limitations of the weapons the thief is using, you now have the upper hand. Giving IT professionals the tools and techniques attackers use to break into their sites equips those professionals with the knowledge they need to build proper defenses.

To have the right mindset for protecting yourself, it's important to look at what's currently occurring from an Internet-security perspective. Based on my experience, it's currently an attacker's gold mine on the Internet. Attackers can basically break into whatever systems they want with relative ease, and the chances of getting caught are slim. To make matters worse, complex attacks are being coded up so that anyone can run exploits against these systems any time they want. Now someone with minimal experience can break into sites, just as the experts do.

The other thing that makes matters worse is how companies have built their networks. In the past, every company's network and systems were different. In the late 1980s, companies hired programmers to customize their applications and systems, so if I wanted to break into your network, I had to learn a lot about your environment. That information did not help me when I tried to break into another company's network because its systems were totally different. Now every company uses the same equipment with the same software. If attackers learn Cisco, Microsoft, and UNIX, they can break into nearly any system on the Internet. Because networks are so similar and software and hardware so standardized, an attacker's job is actually easier.

One could argue that the security professional's job also is easier because once you learn how to secure a system you can share the techniques with everyone else. But there are two problems with this. First, for some reason the bad guys love to share but the good guys don't. Second, even though the operating systems and applications are the same, the ways they are configured are quite different. From an attacker's standpoint, that difference is insignificant, but from a security stance, it is quite significant. Server A may be running 2008 and be properly secured, but that doesn't mean we can just clone that configuration to server B, because it may be configured differently.

So to sum up the general trends, the job of attackers is becoming easier and easier, which means our job as security professionals is becoming harder and harder. Thousands of exploit scripts are available, and anyone can download and run these with minimal knowledge or expertise. I have seen companies of all types and sizes compromised, often without realizing it until several weeks later.

## Overview of security breaches

You can't open a newspaper or a magazine without reading about a breach in security. What's interesting is that even with all the talk about network security or the lack of it, a large percentage of companies still don't report security breaches. This is for one of two reasons. First, the company doesn't want the bad publicity associated with reporting the breach. Second, and far more likely, is that most companies do not know when a breach has been committed. If a perpetrator gains access to a system and compromises sensitive information without causing any disruption of service, chances are the company will not detect it.

The main reason most companies detect attacks is because the attacks result in a disruption of service or negative attention is brought to their site. Reflect on the following scenario. Company A should have made a large sum of money from a new idea that it was the first to market. Through a breach in security, a competitor was able to acquire the information and sell a competing product. Company A should have made $40 million but made only $30 million because of the compromise in security. In this example, unless the company had strong security to begin with, how would it ever be able to attribute the loss of funds to minimal network security? The loss would be written off to other factors that had no relation to the real cause.

## Current state of security

Protecting against attacks requires constant attention and monitoring. One security motto is, "Prevention is ideal but detection is a must." A company connected to the Internet will never be able to prevent every attack. Therefore, in cases where an attacker is successful, a company must be able to detect the attack as soon as possible.

Detection is the key to good security, yet that is the one area in which most companies do a terrible job, and the reason is simple. Detection requires a lot of time and resources because you are aiming at an ever-changing target. Most companies prefer to install a firewall, say they are secure, and forget about it, but this leads to a false sense of security, which most people would argue is worse than having no security at all. If companies really want to be secure, they need to realize that setting up systems to prevent breaches is only half the battle. Equally important is investing the necessary time and effort in detecting breaches that still occur. Detection is what is really going to keep your site safe.

Another issue is that when a company decides to invest in security, the cost benefits are not tangible. If you invest in a new network backbone you can see the increase in speed. If you invest in new servers, you can see an increase in performance. If you invest in security, you will minimize the chances of someone breaking into your site, but there's nothing tangible that management can see. When companies don't realize they're having security breaches, they wonder why they need the additional investment. As you can see, this is an issue of awareness. Companies need to realize that just because they haven't detected a breach (and in fact haven't been looking), this doesn't mean they haven't had a breach.

Not only do companies have to start making an investment in security, they also need to raise their awareness. If employees came to work one morning and found that several computers had been stolen, they would quickly notify law enforcement. Yet companies are reluctant to report computer crimes.

As noted earlier, attacks go unreported for at least two reasons. The first is ignorance; companies do not realize they are being attacked. While not all attacks can be prevented, early detection can minimize damage. Not detecting them can cause major problems for other companies because the company's site can now be used as a launching pad for attacks. This is a special problem with denial-of-service attacks, which depend on other sites being used as launching pads. Relying on millions of other sites for the security of my site does not help me sleep any easier at night.

Many companies also take the security-through-obscurity approach. This basically says that because no one knows about my network or really cares about my company, I don't need security because no one would try to break in. With the ease of breaking into sites this logic does not hold. Companies of all shapes and sizes in all different business areas have been broken into. Most companies have learned that when it comes to security, ignorance is deadly. Saying that no one would care enough to break in is simply false.

The second reason most attacks go unreported is fear of bad publicity. In most cases as soon as a company reports a security breach, it becomes public information. Think of the impact should the *Washington Post* report on its front page that Bank X has been hacked and has lost $20 million. If the bank reports the theft, it is more likely to suffer from bad press and lost customers—and would probably never apprehend the criminal because many such crimes go unsolved.

## Boundless nature of the internet

Another issue is the ease with which someone connected to the Internet can travel across local, state, and international boundaries. Accidentally typing one wrong number in an IP address can be the difference between connecting to a machine across the room or connecting with one across the world. When connecting to a machine outside this country, international cooperation is required in tracing who made the connection. Based on the ease of connecting to a machine anywhere in the world, attackers can hide their path by hopping through several computers in several countries before actually attacking the target machine. By picking countries that are not U.S. allies, they can almost guarantee they won't be traced. Rather than attacking a machine in California directly, an attacker can very quickly go through England, Russia, France, the Middle East, Israel, and the Far East before finally ending up in San Francisco. And tracing such a path would require much time and an unlikely degree of cooperation among countries.

Because we know that there's a major problem and that companies have a lot of work ahead of them, let's look at what types of attacks those companies are up against.

## Type of attacks

The following list of the types of network-based attacks occurring on the Internet is not meant to be all-encompassing but to give the reader an idea of what is occurring:

- Active attacksDenial of serviceBreaking into a siteIntelligence gatheringResource usageDeception
- Passive attacksSniffingPasswordsNetwork trafficSensitive informationInformation gathering

An active attack involves a deliberate action on the part of attackers to gain access to the information they are after. An example would be trying to telnet to port 25 on a given machine to find out information about the mail server a company is running. Someone is actively doing something against your site to try and get in. In the traditional sense, this would be equivalent to someone trying to pick the lock on your front door or throw a brick through a window in order to gain access. Because these are active attacks, they're fairly easy to detect if you are looking for them. However, even active attacks often go undetected because companies do not know what to look for or are looking at the wrong thing.

Passive attacks, on the other hand, are geared to gathering information as opposed to gaining access. This is not to say that active attacks cannot gather information and that passive attacks cannot be used to gain access; in most cases the two types are used together to compromise a site. But unfortunately most passive attacks do not necessarily involve traceable activity and therefore are much harder to detect. Another way to look at it is that active attacks are easier to detect and most companies are missing them; therefore, the chances of detecting a passive attack are almost zero.

### Active attacks

In most cases attackers use an active attack first, to properly position themselves, and then use a passive attack to gather the information they're after. For example, an attacker may break into a machine so that he can sniff passwords off the network when people log on each morning. Passive attacks can also be used to gain information that is needed to launch a successful active attack. In the traditional sense, a passive attacker would sit outside your house to determine your departure and arrival times. The attacker could then use this information to plan the opportune time to break into your house.

Each attack individually has some value but the real value is gained when you combine multiple technique or attacks. Giving a carpenter a single tool will allow him to build part of a house. When the carpenter is well trained and has several tools, he can build an entire house. These same principles hold for successfully breaking into a system or in our case preventing a successful break-in.

The two main types of active attacks are denial of service and breaking in. Denial-of-service attacks involve denying legitimate users access to a resource. This can range from blocking users from going to a particular Web site to disabling accounts so that users cannot log onto the network. For example, if you telecommute and dial-up to your company's server to work every day and someone goes outside your house and cuts the wire, this attacker has, in essence, caused a denial-of-service attack because you are unable to perform your work. Unfortunately, these attacks are fairly easy to perform on the Internet because they require no prior access. If you are connected to the Internet you are vulnerable to a denial-of-service attack. Also, tools for performing these types of attacks are readily available and easy to run.

In order to cause damage or acquire information, one must successfully break into a site and retrieve the necessary information. The Internet, however, adds a new dimension to this. In some cases the sole reason for breaking into a site is to use the resources for the attacker's own personal gain or to break into another site. Some of the tools that are used by attackers require significant processing power and a large connection to the Internet. What better way to acquire these resources than to break into a large site, upload the attacker's programs to its systems and run them? This type of attack also has an added benefit in that it makes it much harder for someone to trace the attack back to the attacker. If I am launching an attack from company A and I cover my tracks, and break into company B, that company will only be able to see that company A has attacked it. Because someone was able to break into company A in the first place, that usually means they have lax security. As a result, it would be extremely difficult for anyone to trace the attack back to the originator.

### Passive attacks

Passive attacks, by their nature, might not seem as powerful as active attacks, but in some cases they can be even more powerful. With passive attacks you do not directly get access, but in some cases you get something even better—guaranteed access across several avenues. One of the most popular types of passive attacks is sniffing. This involves sitting on a network segment and watching and recording all traffic that goes by. In some cases this yields very little information. For example, if you are looking for a specific piece of information, you might have to search through hundreds of megabytes of information to see if the data you are looking for is present. In other cases if you know the pattern of the packets you are looking for it could be quite easy. An example of this is sniffing passwords. There are programs you can run from a workstation that look for Windows authentication packets and when they find them can pull out the encrypted passwords and save them. One can then use a password cracker to get the plain-text password. To get a single password, this might seem like a lot of work. But imagine that you set this up to start running at 7 a.m. and stop running at 10 a.m. Because most people log onto the network during those three hours, you can gather hundreds of passwords in a relatively short time.

Another useful type of passive attack is information gathering. During this type of attack you can gather information that will help someone launch an active attack. For example, someone intent on attacking your system can sit near the loading dock of your company to watch deliveries. Most vendors print their logos on the sides of boxes and these are easy to spot. An attacker who notices that you've received several Sun boxes can be pretty sure that you're running Solaris. If shortly after the release of Windows 2008, a company receives boxes from Microsoft someone could probably guess that the company is upgrading its servers to the new operating system.

## New Way of Thinking

Companies are embracing the Internet for most aspects of their business, but they're often looking at it from a purely functional standpoint. Does the application that is using the Internet have the proper functionality it needs to be profitable? This is certainly a good start, but companies need to start changing their mindset and putting security in the picture. If you wait to think about security until you need it, it's too late — it's like waiting to install a telephone until you need to call 911. The proper security mechanisms need to be put in place so that when a breach occurs you can react accordingly and minimize the impact. In order to understand what mechanisms should be put in place, let's look at some general security principles and how they can address the current problem.

## Overview of General Security Principles

In order to properly design your network in a secure manner and to protect against hackers, it's important to understand some general security principles. The key principles for having a secure site are:

- Deny attackers the path of least resistance.
- Remember that prevention is ideal, but detection is a must.
- Provide defense in depth.

When an attack is planned on a company's site, the attacker will always try to take the path of least resistance. Therefore, it's critical that a company understand all its weaknesses and not concentrate all its security efforts in one area. Far too often I see a company investing heavily in a firewall configuration in order to protect its network. But it may forget that it has dial-up modems with no authentication that bypass the firewall. Why would attackers spend time trying to get through a secure firewall, when they can just dial up and bypass the firewall? A company always has to understand its weakest link and fix it. Of course, this creates an endless cycle, because as soon as a company fixes the weakest link, the second weakest link now becomes the weakest and has to be fixed in turn. All links will never be equally strong, of course. But only by understanding a company's security posture and having a plan in place to minimize one's risk can a company minimize this problem.

In order to have a secure site, companies must realize that there are two pieces to the puzzle — prevention and detection. Most companies concentrate their efforts on prevention and forget about detection. Probably more than 90 percent of large companies have firewalls installed, which is meant to address the prevention issue. The problem, however, is two-fold. First, a company cannot prevent all traffic, so some things will get through that could be attacks. Second, most prevention mechanisms companies put in place are either not designed or not configured correctly, which means they're providing only minimal protection, if any. I've been astonished by the number of sites I've seen that have firewalls installed with lines bypassing the firewall.

There is no silver bullet when it comes to security. Vendors at times would like to convince you otherwise, but the bottom line is that a company must have multiple approaches in order to have a secure situation — no one mechanism is going to do it all. A firewall is a good start, but it is only a start, not a solution. Once you add intrusion detection, multiple firewalls, active auditing, secure dial-in, virtual private networks, encryption, strong passwords, and access control lists, then you may be getting close to having a secure network. The key thing to remember is that any one mechanism can fail and only by having multiple mechanisms can a company truly have a secure site. This concept of having multiple mechanisms protecting a site is called *defense in depth*.

# The Changing Face of Cyber Security

Every day you can read the paper or watch the news and hear about another security breach that allows controlled information into the hands of those who would use it for criminal purposes. Unfortunately this is only a very small portion of what is actually happening on a daily basis. One might ask which is worse, the company that reports its data losses and is in the news for a few days, or the company that hides the fact it was compromised and 10,000 credit card numbers stolen. The fact is that no matter whether the breach is self-reported or uncovered later, both companies will have to endure days of news coverage as well as government investigations and possible lawsuits.

For years there has been this tendency to understate the impact when an incident occurs. However, being proactive to prevent the incident from occurring in the first place is a better approach. We are at a juncture in the technology evolution where process thinking is beginning to consider prevention as a complement to existing mitigation or detection measures.

The most important aspect of approaching cyber security is management buy-in. The decision makers must have an understanding of the importance of a strong cyber-security program. Without the support of management it becomes very difficult to make the transition from a reactive stance to a proactive stance. Once the buy-in is accomplished, responsibility falls on the IT experts. Detection and mitigation are still critical but the ultimate goal is to proactively forestall attacks before damage is done.

The key to a good cyber-security foundation is to introduce policies that mandate strong IT security practices. The policies, to name a few, should address common avenues of attack such as weak password policies, unauthorized media, and failure to limit Internet access and control what people use the Internet for.

Once all the groundwork has been laid, it is important to implement and maintain the key infrastructure that makes up a good cyber-security posture. There are many aspects to developing and maintaining such a posture. To meet the ever-growing cyber-security proactive position, numerous things have to be developed, maintained, and improved as time goes on. If this is not done, then the company will quickly revert to the mitigation stance. Mitigation is dealing with a problem after damage has occurred. While this is an important stance to have, ideally organizations should prevent or detect attacks before damage happens.

Some of the key areas include:

- Management buy-in
- Policy development with regular updates and revisions
- Policy reviews
- Knowledgeable network staff
- Training
- Tested processes
- Third-party assessments

Third-party assessments of network security are becoming more frequent and allow companies to validate their processes and make improvements. With the increasing number of government regulations requiring third-party assessments and the amount of IT work being subcontracted, it makes sense to take full advantage of the opportunity to improve the security of the systems.

Third-party validations have been designed to assist in the migration from mitigation to being proactive. The assessment helps to ensure that the company's actions and implementations meet today's standards and lessen the risk of a successful cyber attack. Some of the key points that are evaluated during an assessment are:

- Document review
- System and network testing
- Penetration testing if specified
- Network architecture review
- Final recommendations

A company can take the results of the assessment and improve the processes that are currently deficient, while also highlighting the processes that are up to standard. The outcome of the assessment is a company that has the information to make the move from the mitigation stance to the cyber-security proactive stance.

# Summary

Today the era of sitting back and hoping an attack doesn't happen to you is coming to an end. Consumers and government alike are expecting companies to take the initiative to be proactive and prevent a lot of the incidents that have plagued companies in the past 10 years. It is better to prevent a hundred attacks and not be the front-page story than to have one incident that could have been prevented.
