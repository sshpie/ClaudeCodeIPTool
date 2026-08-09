# Chapter 19. Business Case for Intrusion Detection

![Business Case for Intrusion Detection](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

“Where do I start? What is the best ID tool to use?” A student asked this question after he had just completed the most advanced class we teach on the subject of intrusion detection, our hands-on, immersion curriculum. I was more than a little surprised by that question. We had spent the past six days and evenings hands on, learning about covert channels, malformed packets, and TCP fingerprinting within a connection. We had worked and worked to show the students why there is no silver bullet, why every IDS needs to be backed up by a network recorder that captures all the traffic. I decided to answer with a question. To the questioner, I must have sounded like someone from Oz, but what I said was, “If your organization doesn’t currently have an intrusion-detection capability, why should they acquire one now? What’s changed?” If your organization doesn’t currently have an intrusion-detection capability, it will often be an uphill effort to champion one. To paraphrase Newton, an organization at rest tends to remain at rest.

We are coming to the close of this book and before we move to our final chapter, the future of intrusion detection, I would like to consider the business case for intrusion detection. This is an important subject. The chapters that precede this one give the sense that the knowledge required to be an analyst is very technical, but fun. Also, I am sure you have a sense that the job of the intrusion-detection analyst with new detects and live attacks is exciting and challenging. Everyone that I know in the field is having a great time, but that isn’t a good reason to deploy intrusion detection in your organization. If you made it past the first half of the book, you probably have a technical bent; so do I. But that isn’t enough. Three of my heroes in intrusion detection, Ron Gula, Marcus Ranum, and Marty Roesch, have all started to say, “As a businessman….” Each of us is in business in some sense. This is still true if we work for the government, a university, or a not-for-profit. If you are even thinking about intrusion detection, your organization probably is fairly well funded. We have taken pains to develop a technical and architectural framework, but also to consider the business issues of risk management. If your ID capability does not fit in your organization’s business model, it will be a source of friction. Let’s work together to develop the strategies and processes needed to package intrusion detection for an organization.

This chapter was written for security professionals who:

- Don’t currently have an intrusion-detection capability and are considering the merits of acquiring one
- Have a rudimentary capability and are considering a follow-on procurement or upgrade
- Have an existing capability and the organization is downsizing or restructuring and is in the process of evaluating this job function

In these cases, you aren’t going to succeed by “wowing ‘em” with technology. Appeals to duty or alarmist cries, “The hackers are coming, the hackers are coming,” will not suffice to keep this project funded for the long haul— although it might well shake loose money for an additional purchase.

This chapter lays out a three-part plan that shows the importance of intrusion detection. The first part of the plan covers management issues, what I call the “fluffy stuff.” Part one isn’t technical, but it serves as the backdrop to allow management to support the intrusion-detection plan.

Part two of the plan answers the question “Why intrusion detection?” This is where you discuss the threat and the vulnerabilities; this is where you draw heavily on what you have learned about risk.

Part three offers your solutions and tradeoffs. The goal is to create a written report that serves as the project plan and justification. I have tried to lay this out so that it makes a nice presentation as well, because that is how one normally briefs senior management these days. Each item in a bulleted list is a suggestion for a PowerPoint slide. For extra credit, cut and paste the appropriate material from your written report into the notes section of the PowerPoint slides and suggest they be printed with notes pages showing. Few people take the time to do notes pages, so this will show you have it together.

All presentations and reports to management should start with an introduction called an Executive Summary. This is where you sum up the three most important points you are going to make. When you brief senior management, always be prepared to have your time cut short. “Can you do it in five minutes?” is not an unheard of request. In that case, you will show exactly three slides: your Executive Summary, Cost Summary, and Schedule. The Executive Summary is followed by a Problem Statement, in which you define the problem you are trying to solve. You probably want to extract a nice sound bite from the information in part two of the report for this. Your third slide is a roadmap where you define the structure of the presentation.

# Part One: Management Issues

Your goal is to show management that this is part of an overall integrated information-assurance strategy that has tangible benefits to the organization. The key to doing this is to show that your proposed solution has the following characteristics:

- Bang for the buck.
- The expenditure is finite and predictable.
- The technology will not destabilize the organization.
- This is part of a larger, documented strategy.

## Bang for the Buck

You need to be realistic. Intrusion detection is fairly costly. You need two fast computers ($2.5k each). If you choose commercial intrusion-detection solutions, the software license ($10k, to start), means that it costs $15k just to say *intrusion detection*. The network might need to be altered and there is the __ work-year salary and overhead for the intrusion-detection analyst; you could easily be talking $100k. But wait, there is more, bandwidth is increasing, so you need six sensors and a Top Layer switch just to watch the web farm, add another $100K. You need a database to search for slow speed scans and a correlation engine with a hardware RAID to hold all this data, add another $150K easily. In an environment focused on cost reduction, you are going to have to show a significant benefit to justify this expense.

The good news is that you can do exactly that. Risk is part of the business equation. In fact, there are markets that buy and sell denominated risk every day. Did you skip over the risk chapter? What is one way an intrusion-detection system helps reduce the *annualized loss expectancy* (ALE)? By observing the attacks against your organization, the analyst can assist the organization in fine-tuning its firewall and other defenses to be resistant to these attacks. Is that worth $100k - $350k? If not, here is another way an intrusion-detection system helps reduce loss. To conduct business, you might find that certain applications, or situations, require that some vulnerabilities need to be left on systems. A common example is that when you apply the recommended security patches to a system, it breaks some application. The intrusion detection can be focused on that particular vulnerability. In fact, this is an ideal opportunity to use that Reset kill you have been itching to try. There is a bang for the buck using intrusion-detection systems.You can show it, and you can quantify it.

**Intrusion Detection Using Firewalls**

One of the incredible changes on the market has been firewalls that log full binary data. OpenBSD’s IPFilter and the commercial Raptor firewall can log data in BPF format. This binary logging allows you to run Snort or TCPdump filters against this information. This is incredible! I have already mentioned hogwash and UnityOne, firewall appliances with an IDS capability built in. My personal preference is to use two devices—if one fails the other continues to run.

Also, firewalls that do not have a binary logging capability can still be used in intrusion detection. As an example, Dshield ([www.dshield.org](http://www.dshield.org)), the technology that powers incidents.org, uses firewall data for its large-scale intrusion-detection capability. Firewalls certainly can be sensors. To be sure, firewalls that do not log most of the TCP header field values, such as TCP flags, only allow for very limited analysis. If you have a firewall with the fidelity of a Linux firewall (such as IPtables, for example), however, you can do a lot of the traffic-analysis techniques you have learned in this book.

If you do not have an IDS available, you can and should begin to apply what you have learned from this book by reviewing your organization’s firewall logs. Needless to say, get permission first and be slow to raise alarms!

## The Expenditure Is Finite

You know the old adage about a boat being a hole in the water you throw money into. I was reading a Sunday paper column recently titled, “Ten Tips on How to Increase Your Personal Wealth.” One of the tips was don’t buy a boat; if you have a boat, sell it. I am not so interested in wealth that I am ready to ditch my boats, but they do keep costing money (and they are mostly sea kayaks).

Here is one more house story that will help you understand a senior manager’s concerns about containing expense. One day, I realized that everything I did was done on a small fleet of laptops and a cell phone with a trillion monthly minutes. In that moment, I realized I could live anywhere I want as long as the area has cell towers and DSL or better. My wife and I settled on Hawaii, and as luck would have it, DoD called the next day and asked me to do two weeks of consulting on an IDS visualization project on Oahu, so Kathy and I flew down to the islands. Two weeks later, we bought a dream house on Kauai on the rim of a canyon overlooking the Wailua River halfway between the rainforest and the beach. A month after we moved in, the dream house became a nightmare house as it suddenly settled into the soft earth of what had formerly been a pineapple field. A parade of insurance agents came through claiming it was not covered, followed by structural engineers saying they had never seen this before. Finally, a wise local pointed me to the best contractor on the island, Luis Soltren—truly the best contractor I have ever seen—but the house was totaled. Luis, like anyone who is the best at what he does, is not cheap. It was the money pit, (never watch that movie if you are remodeling), up close and personal. Every time they pulled a piece of sheetrock or a tile, we would find more problems. Luis would shout for one of us and we would look and shudder. I did remodeling in college, have built a house, and roofed dozens, so I know a bit about the trade, and Luis was spot on—these were all must-do repairs. The bill kept getting higher and higher. When it crossed, no joke, $200k, I was sick to my stomach, and it kept going. We are finally done, and I learned a very important lesson. The phrase total cost of ownership is very popular in information technology, and I never really considered it until I was caught in a project, my house, where it wasn’t possible to calculate what the final costs were going to be; they just kept going up.

Now, let’s apply what we have learned from this story to intrusion detection and your organization’s senior management. Keep in mind that good managers treat every dollar as if it is their own, and uncontrollable costs make them feel the way my house made me feel.

When it comes to intrusion detection, management might well be willing to pay the $100k or whatever, but management needs to be shown why the expenses you propose in your plan are probably correct and that you aren’t going to have to come back for more and more money. For instance, a classic error is to plan on using older, last-generation PCs for the intrusion system. I propose the opposite. Buy the latest-generation PCs for intrusion detection, and after six months to a year, roll them out as desktop machines.

Management will appreciate this as an honest and workable approach. It gives the organization the best possible intrusion-detection capability and the hardware upgrades are essentially free because buying new desktops is part of the computing life cycle.

## Technology Used to Destabilize

The signature line of the hymn “Amazing Grace” is “I once…was blind, but now I see.” This is what an intrusion-detection system does: It helps an organization go from a blind state to a seeing state. Time and time again, students who take the intrusion-detection curriculum we teach at SANS go back and start looking at their data and they realize they really need to change the way they do business. This is a good thing! However, it is a change, and people are suspicious of and resistant to change. When you propose intrusion detection, you must be sensitive to the potential for organizational change and make every effort to show that the IDS will “fit in.” Some of the potential impacts to the organization are the configuration of the network, the effects on behavior of employees, and the need for additional policy support.

### Network Impacts

We have discussed the challenges of deployment on switched networks. This needs to be carefully coordinated with the network operations people before the purchase order for the IDS is cut. The best thing to do is to get the spanning port working with a protocol analyzer; most network operations groups have one or more protocol analyzers. If the spanning port is difficult for your networks operations people to configure and maintain, network taps should be considered for the listening ports on the IDS. Many people feel that good practice for an IDS sensor is to be provisioned with multiple interface cards:

- Listening ports in promiscuous mode but without IP addresses. This makes it hard for attackers to find the sensor’s listening ports.
- One interface, with an IP address, is used to communicate with the sensor.

The IDS will almost certainly require a firewall modification. Commercial vendors all seem to think that writing their own proprietary protocol for communications among their IDS consoles, sensors, and databases sets them apart from their competition. And of course, they are literally correct. Do your homework and research what ports need to be opened. If the IDS can be modified to use an existing hole in the firewall, use that. Even proxy-based firewalls often have a pass-through hole; a “suck-and-spit” proxy with no protocol knowledge already running to support some application or another. It will be great when the Intrusion Detection Working Group (IDWG) finishes its work and there is a standard transport protocol based on beep ([www.beepcore.org/beepcore/docs/profile-idxp.html](http://www.beepcore.org/beepcore/docs/profile-idxp.html)) for intrusion-detection systems.

### IDS Behavioral Modification

Behavioral modification is another aspect of running an IDS. You already know that I have concerns about using the IDS as big brother, even though many organizations are losing a lot of money to wasteful activities. The IDS is a data collection and analysis tool, however; so even if you aren’t looking for trouble, you might still find it. You need to be prepared as an organization to deal with what you find now that you are no longer blind to network traffic. Let’s use an IRC server as an example scenario.

You turn the IDS on and soon realize that a bright young kid in the computer operations department has set up one of your internal systems as an IRC server. How did you find this out if you weren’t monitoring for IRC? We have discussed the fact that DNS, web, and email servers draw a lot of fire. That is nothing compared to the fire IRC servers draw! What the analysts see is a ba-zillion attacks and probes directed at a system in computer operations. When you look into it further, you find out the rest of the story. Obviously, the organization wants to turn this around and get the problem cleaned up. The wise analyst and organization will have established policy before the IDS was powered on to handle these things.

### The Policy

I suggest that the organization consider an initial amnesty policy. By this, I mean the first 10 or so violations of the organization’s acceptable-use computer policy be dealt with quietly and in a lenient fashion. A memo can be sent out that doesn’t name anyone, but lists some of the examples and warns that in the future these activities will not be tolerated. I know of organizations that have turned on their shiny new IDS and examined their traffic for the first time. Imagine their surprise when they see things they do not approve of entering and leaving their network. They are now at an important decision point. If the organization reacts in a knee-jerk fashion and walks the employee straight to the door, the IDS will always be viewed with suspicion and hatred. Be especially careful with the way you deal with systems and network administrators; they are used to doing whatever they want. If you walk someone from the computer or network operations group to the door because they broke an acceptable-use policy you just started enforcing, your IDS might break down or suffer blindness caused by loose cables a lot in the future!

Management knows all about firestorms—hate and discontent and the interactions between folks with strong personalities. Managers deal with this kind of stuff every single working day. If your implementation plan shows that you are sensitive to the other players in the organization and that the IDS is not guaranteed to produce Excedrin headache number 36, they will be far more supportive of your plan.

## Part of a Larger Strategy

This book is focused on helping the analyst of a network-based intrusion-detection system. However, we have also talked about system security, risk, vulnerability scanners, unauthorized use, incident handling, and now, business issues. You need to always be ready to show how intrusion detection fits in as part of the organization’s information-assurance program.

To be honest with you, when I was younger, I didn’t get it. I thought my mission in life was to implement the best technology at the most affordable price possible to help the research lab that I worked for be “world class.” Phrased that way, it even sounds like a laudable mission. I would approach my boss with a technology and its technical tradeoffs and he would say, “Yes, but show me the big picture.” It used to drive me crazy. I was convinced he was a total idiot with a personal goal of being named Luddite of the year. Fifteen years later, I am just starting to really understand. You can’t play a song on a harp with one string. Any technology, no matter how wonderful, is useless unless it complements the existing business processes of the organization. When you brief management on the spiffy IDS you want to buy, be sure to include the hooks to system security, risk, vulnerability scanners, unauthorized use, incident handling, and business issues in your plan. Please allow me to do a quick repeat from [Chapter 17](ch17.html), “Organizational Issues” (see [Listing 19.1](ch19.html#ch19pro01))

**Procedure 19.1. Listing 19.1 The Seven Most Important Things to Do If Security Matters [[1]](#ftn.ch19footnote01)**

1. Write the security policy (with business input).
2. Analyze risks, or identify industry practice for due care; analyze vulnerabilities.
3. Set up a security infrastructure.
4. Design controls, and write standards for each technology.
5. Decide what resources are available, prioritize countermeasures, and implement top-priority countermeasures you can afford.
6. Conduct periodic reviews and possibly tests.
7. Implement intrusion detection and incident response.

If your intrusion-detection proposal is written against a process like this, it will be obvious to management that it is part of a larger strategy. Senior management does not have the time to accept information piecemeal; it is responsible for broad business strategies. Take a bit of your time to make its job easier.

We have spent considerable time on the four issues that management needs to see in an intrusion-detection plan. If we do not cover these bases, their paradigms will not let them even consider the plan. Again, they are as follows:

- Bang for the buck.
- The expenditure is finite and predictable.
- The technology will not destabilize the organization.
- This is part of a larger, documented strategy.

Now we can move on to the technical stuff; this will be part two of your plan or proposal.

# Part Two: Threats and Vulnerabilities

The second part of the plan is where you lay out the threats and compare them to your vulnerabilities and the value of your assets. The purpose of this is to answer the question, “Why do we need additional security measures?” I think that the highest and best purpose of network intrusion detection outside the firewall is to help assessment of the attacks directed against your organization and to ensure the internal hosts are hardened against these attacks. But before you have an IDS, how do you assess these threats? You want to examine the problem, the threats, and the vulnerabilities before you offer intrusion detection as the solution. [Chapter 17](ch17.html)’s focus on risks gave the foundation you need to approach this section of the plan. Part two’s elements are as follows:

- Threat assessment and analysis
- Asset identification
- Valuation
- Vulnerability analysis
- Risk evaluation

## Threat Assessment and Analysis

A risk assessment purist would say you need a dictionary that enumerates all possible threats, and then you need to analyze each threat. For a plan to support an intrusion-detection system that is designed to be readable by management, this is a bad idea.Your goal is not to show all possible threats, but rather a sampling of probable treats. Management and the intrusion-detection analyst would do well to focus on what is likely to happen to it and how it is going to happen. I cover these in reverse order. The following list is my take on how these attacks are going to arrive. The primary threat vectors are as follows:

- Outsider attack from network
- Outsider attack from telephone
- Insider attack from local network
- Insider attack from local system
- Attack from malicious code

### Threat Vectors

Let’s just take a second to be sure of the term *threat vector*. If you go to the restroom of a restaurant, there is often a sign saying, “Employees Must Wash Their Hands Before Returning to Work.” It has been well established that skipping this sanitary step is a disease vector. The dirty hands are the pathway, the conduit that allows the food poisoning.

A network-based intrusion-detection system might be able to detect outsider attack from the network, insider attack from the network, and possibly attack from malicious code (remember the Macro virus and PKZip examples from [Chapter 17](ch17.html)).

A host-based intrusion-detection system with an active agent might be able to detect all five vectors.

### Threat Determination

Your goal for the purposes of establishing a business case for intrusion detection is to list well-known, probable threats as opposed to all threats. How do you find these threats? Sources might include the following:

- Newspaper or web articles on attacks at other places. If it happens to them, it could happen to you.
- Firewall/intrusion-detection logs for specific threats.
- System audit trail logs.
- Demonstration of an intrusion-detection system.

Many commercial intrusion-detection vendors allow you to take their systems for a test drive, with a 30-day trial or something similar. If you are serious about wanting to implement an IDS capability, I can’t stress how important this is to do. It gives you a list of actual attacks against your network; this is helpful for establishing the threat. It helps establish the groundwork for part three of the plan when you show why you recommend an intrusion-detection system as opposed to, say, another firewall. And, it gives you experience with a couple commercial offerings. All too often, folks make their decision either based on something they read or on how friendly the salesperson is. If you have tried a few “loaner” IDSs, in part three of the plan, you can make honest statements about the tradeoffs between various systems.

If you can find the time to do it, interviews with folks in various parts of your organization can be a rich source of threats and vulnerabilities that you might otherwise have missed. I have had people tell me about shockingly bad practices when I ask them what they consider the largest dangers to the organization’s information assets to be. Yet, they never came forward with the information on their own. As they say in Alabama, “Whaay-el, you never asked.”

## Asset Identification

[Chapter 17](ch17.html) discussed asset valuation. Now, you focus on the concept a bit more. The huge value is the investment in data. If most of your workers use computers most of their workday, the value of the data on the computer is the cost of putting that worker in front of the console. The threats to that data are that it will be copied, destroyed, or modified.

We have touched on this throughout the book. So that we are really clear, however, I will reiterate: The most probable threat to that data is destruction from the system owner. As my Catholic friends would point out, this could be by a sin of commission, or a sin of omission. By commission, I mean an overt act, deleting the data accidentally, or on purpose, and never telling anyone so that it can be recovered. By omission, I mean the failure to back up the data properly, and that includes off-site backup. At least for the things that are within your power to change, work to ensure your data is backed up.

It turns out to be an almost impossible task to ensure that all the data throughout the organization is protected from being copied, destroyed, or modified. In the same way, making sure every data element is backed up, on and off site, is beyond the capabilities of any organization that I know of. This is a great lead-in to the notion of crown jewels, or *critical program information* (CPI) as they say in security texts.

## Valuation

All your data is not of the same value. In fact, a small portion of the information that exists in your organization is what distinguishes you from your competition. Although all your data has value, crown jewels are the information that has critical value and must be protected.

You reflect this in the threat section of your plan. Find as many of the crown jewels as possible. Consider the threat vectors, and the known common threats, and use these as the examples of threats and vulnerabilities in part two of your intrusion-detection business plan.

In part three, you will discuss countermeasures to protect these clusters of high-value information. These might include the following:

- Host-based IDS software on the critical systems.
- Honeypot files. If your organization has sensitive documents, you can add special tagged strings into the document. One way to do this is invent acronyms that do not actually exist. Then you can program your IDS watch for these with a string, or content matching rule. This would tell you if these files are entering or leaving your network.
- Instrumenting internal systems with personal firewalls. (Technically oriented employees often enjoy doing this.)
- Network-based IDS in high-value locations.

## Vulnerability Analysis

Vulnerabilities are the gateways by which threats are made manifest. All the threats in the world don’t matter if there are no vulnerabilities.

Were you disappointed because I didn’t give a long list of vulnerabilities from which to work? Well, they change almost daily so you need a pointer to a current list, not a static one that will be obsolete before the book is even printed. I like the Computer Vulnerabilities and Exposures (CVE) project (`cve.mitre.org`) the best because it cross-indexes a number of great vulnerability lists such as bugtraq and ISS’s X-Force. However, you do not need to do this manually. Getting your general threat list as well as an assessment of your vulnerabilities is a fairly simple matter. A number of good vulnerability assessment tools are available. These tools test for specific threats, and they find potential vulnerabilities. Let’s consider three classes of tools: system-vulnerability scanners, network-based scanners, and also phone-line scanners.

Tools such as COPS, SPI, tiger, and STAT are examples of system-vulnerability scanners. They work within the system looking for missing patches, incorrectly set file permissions, and similar problems.

Tools such as nmap, nessus, saint, ISS’ Internet Scanner, and Axent’s NetRecon are examples of network-based scanners. These are fairly fast and effective and scan the network looking for unprotected ports or services.

While conducting vulnerability assessments, you might also want to assess your risk from the attackers who scan your phone lines looking for active modems. Toneloc, available from fine hacking sites everywhere, is the most used tool for this. Phonesweep from [http://www.sandstorm.net](http://www.sandstorm.net) is a commercial tool with some additional features.

If at all possible, your vulnerability assessment should offer three views:

- ****A system view.****Taken from selected systems with system scanners.
- ****A network view.****Done from an internal scan of your network.
- ****An Internet view.****Done from outside your firewall and, if possible, a phone scan as well.

Of course, you want some juicy vulnerabilities to spice up your report, but please also scan your firewall, DNS, mail, and web servers, as well as systems related to your crown jewels. These are the systems that your organization depends on.

Whew! Sounds like a lot of work, doesn’t it? Correct, it is a lot of work and vulnerability assessments are not something that should be done only once. Why does it make sense for the intrusion-detection analyst to be involved in vulnerability assessments? It keeps you aware of specific problems and where in the organization your vulnerabilities are located.

## Risk Evaluation

You have a lot of data. What do you do with it? Just because you collected it, do not stuff it all in your report, even as labeled appendixes. On the other hand, you do want it organized and available. Whenever you brief senior management, you want at least one supporting layer of data available—that is, if your slide says 12 systems are deemed to contain CPI, you darn sure want to be able to list those systems and explain the rationale for choosing them and not others.

Okay, we have answered the question of what you are not going to put in the second section of the report. What *should* you provide?

- A top-level slide with the value of the organization’s information assets. Suppose you have 100 computers with a five-year life cycle, for instance. The hardware, software, and maintenance costs are $200k/year with information valued at $1 million.
- A network diagram that defines the boundary you are trying to protect.
- A basic description of the threat vectors.
- A general summary of your general vulnerability assessment.
- A description of the crown jewels: where they are, their value, and so on (include the firewall, DNS, mail, and web servers).
- Specific threats against the crown jewels.
- Specific vulnerabilities of the systems that host the crown jewels.

This should exist as a written report as well as a view-graph presentation. If you are doing a PowerPoint presentation (which is recommended), expand each of the preceding bullets to be a PowerPoint slide with three to five bullets each.

# Part Three: Tradeoffs and Recommended Solution

Finally, you get to pitch your intrusion-detection system! You can hardly wait to get behind the console of that shiny new intrusion.com special and smell that new IDS smell. Slow down a little longer.You need to offer some tradeoffs, and also remember, you are going forward with a package. Intrusion detection by itself is a hard sell. From a risk-assessment, textbook standpoint, the next thing you are supposed to do is establish risk-acceptance criteria. This approach is to put management on the spot and have it define what levels of risks it is willing to accept. Then, you go back and design comprehensive countermeasures for all risks greater than what management is willing to accept. Good luck!

Therefore, you should do the following:

- Define an information-assurance risk-management architecture.
- Identify what is already in place.
- Identify the immediate steps you recommend.
- Identify the options for these countermeasures.
- Produce a cost-benefit analysis.
- Implement a project schedule.
- Identify the follow-on steps illustrating where you want to go in the future.

## Define an Information-Assurance Risk-Management Architecture

This sound like a hard chore, but it is really simple. You have defined the threats. You know the primary countermeasures. It could be as simple as implementing the following:

- Firewall from the Internet
- Network-based IDS outside the firewall
- Internal firewalls for crown jewels
- Network-based IDS covering crown jewels
- Host-based IDS on crown jewels’ platforms
- Tagged honeypot files on crown jewels’ platforms
- Basic hardening for all systems, antivirus programs, patches, and good configuration management to prevent silly file permission settings
- Organizational network-based backup with off-site storage
- Scanning of the internal network for vulnerabilities quarterly
- Certificate-based encryption for transmissions over the Internet with customers and suppliers as well as home and off-site workers
- Strong authentication for dial-ins
- Disk encryption and personal firewalls for laptops

This list might not be completely appropriate for your organization, but this is my view of the big picture for information assurance.

## Identify What Is in Place

Every briefing or report to senior management should include a status slide, something that defines where you are now. If you follow your definition of your information-assurance architecture with your current status, it is a nice set up for the things you want to do next.

## Identify Your Recommendations

Finally, you get to pitch the intrusion-detection system of your dreams. You want the pitch to be balanced. It is perfectly reasonable to pitch an intrusion-detection system and a vulnerability scanner (or whatever is appropriate for your organization) at the same time. For the pitch to be solid, it should include options, cost, and schedule information.

I just cry when I see someone take an hour of a senior manager’s time to brief him on a problem and possibly recommend a solution when the presenter doesn’t have the cost and backup information. The senior executive doesn’t think she has enough information to make a decision, so she puts the matter off. What happens, however, is a very subtle characteristic of human nature. When you first hear about a scary problem, you are shocked and might well be moved to action. If you do not act, however, you have been inoculated against the problem. The next time you hear about it, you are less scared and less moved to action. Therefore, you need to be prepared to sell your project the first time!

## Identify Options for Countermeasures

I hate doing this! I know what I want! I have done a market survey. Why should I have to justify the product I have selected? Well, if you didn’t know this before, I’ll let you in on a potential “gotcha.” The commercial intrusion-detection system vendors aren’t dumb! They are trying hard to reach the CIOs and other top executives of your organization with non-technical, high-level issues-oriented briefings. For instance, the host-based companies are pushing the insider threat really hard. Therefore, if you come marching into your CIO with your report and it doesn’t mention the insider threat or consider host-based systems as options, you might be one down instantly.

**Personal Firewalls**

If you are facing management and the issue of the insider threat comes up, keep in mind that internal firewall and personal firewall data can come in very handy. In some sense, these serve as burglar alarms and can alert you to internal problems. Before asking senior management who is responsible for the organization’s risk management, funding, and support, it is a good idea to know as much about the probable risks as possible.

Take the time to list at least one optional approach and to consider at least one alternative product for your recommended procurements. You don’t have to pitch these slides; in fact, you shouldn’t pitch these slides. But you do want them in case the issue comes up. While you are at this point, you need to take a second for an integrity check. Are you trying to buy a toy and help get the job skills to enhance your career or are you trying to secure your organization? Have you really taken the time to examine those firewall logs? If they have good fidelity, and you are honestly more concerned about your organization’s security, perhaps you should consider spending the time and money on a different aspect of your information-assurance architecture.

## Cost-Benefit Analysis

The cost aspect of this section is more important than the benefit section. This is where you give management a warm, fuzzy feeling that you know how much the recommended countermeasures are going to cost. As a program manager, when I hear something that I know I want to do, I really don’t need a lot more information—just tell me what it will cost and when I can have it. Earlier, we talked about the case of having to present the whole package in five minutes. In that situation, you would use three slides: the Executive Summary, the Cost Summary, and the Schedule.

**Why Cost-Benefit Matters**

Cost-benefit analysis doesn’t sound sexy to an intrusion analyst, but going through the exercise for even a one-page financial analysis is really worth the time. I used to have an employee who was very bright, but she had an uncanny knack for coming up with the projects guaranteed to fail. Because she was so smart, when she would suggest that we ought to do something, I would think, “Yeah, that makes sense, let’s do it.” The next thing I knew, it was crash and burn time, and I would look silly again in front of senior management. Then what do you suppose happened? She came up with one of those, “I think we should….” My heart started pounding, my brain racing. I could feel my stress level go up. A wiser manager would have sat down with her and taught her to calculate the cost, the risk, and the potential benefits of a course of action. It is easy after you have done it once. Not me, though. I just reminded her of the failures, and in so doing, probably lost any chance of hearing another idea from a brilliant software engineer.

Not all benefits are tangible and that is important, but this is where you want to support your bang-for-the-bucks slide. This is the point where you list the costs. In the written report, you should list all the costs; in a presentation, you should present only the summary costs. If there are questions, refer management to the written report.

Have you ever given a pitch and had a member of the management team challenge you? And just out of the blue, they say, “I don’t think that is going to work.” They don’t even give a reason. They might have a double-digit IQ, but the spotlight is on you! This is where it really helps to be prepared. Let me make it plain for you: There is a better-than-even chance management will ask the following questions, and you will have to give the answers shown. Will an intrusion-detection system:

- Actually stop attacks? No.
- Detect everything? No.
- Cost a significant amount of money in equipment and salary? Yes.

So you see, you really do want to be prepared! As backup material, I strongly recommend you have at least one ALE (annualized loss expectancy) or SLE (single loss expectancy, as explained in [Chapter 12](ch12.html), “Writing TCPdump Filters”) calculation for what you think is the biggest general threat against the organization. You should also have a couple examples of specific threats against crown jewels if possible. Select your cases carefully so that they support your choice of countermeasures. If you end up needing these slides, your pitch is in trouble; so do a good job on them.

**Business Plan**

I am a passionate, vision-driven person and I need to be honest with you about something. I am physically incapable of labeling anything I write a “cost-benefit analysis.” Let’s be careful here, 9 out of 10 consultants would agree that is the correct title and form for what you should take to management for a final approval of a project. It is probably what decision-making management expects. So, after telling you plainly that I am outside the normal and customary in this regard, please let me share what I do. I produce a business plan, often it is only a couple of pages long, but it helps me focus on the issues. It has the same basic content as a cost-benefit analysis. I deal with costs, advantages, tangibles, and intangibles, but there is one added factor: It will help advance the business. It seems to me that anything you do should serve two purposes: It should solve the problem at hand, and it should advance the business. The energy and capital you invest should help your organization achieve or maintain the lead in your field. “Oh come on Stephen,” you might say, “intrusion detection is an overhead function; you can’t make money on it!” Wanna bet? Baseball, I mean intrusion detection, has been very, very, good to me, and to many of my friends as well. Don’t shortchange yourself and skip learning the material in this chapter. Learn to write a business plan or a cost-benefit analysis. This skill might literally pay off for you.

## Project Schedule

I have written software (badly) for 15 years or so, but I have also managed some pretty skilled coders. I try to get estimates from them so that I can pass up milestone information on future deliverables. Depending on the person, I either double or triple their estimates. Software people invariably think something is a simple matter of a few lines of code until they get into the problem.

The point I am trying to make is that managers develop a radar, a sixth sense for bogus schedules. You are on the next-to-last slide of your presentation, or next-to-last section in your report. You do not want to blow it here.

If you are not experienced at project management, here are some gotchas with fudge factors of items that will take longer than you probably estimated:

- Procure anything and everything (2×)
- Compile and run any free software (2×)
- Get management approval for any policy (5×)
- Install the software and test it (2×)
- Get the sensor to work on a switched network (5×)
- Get the analysis station to connect to the sensor through the firewall (3×)
- Get clearance to install host-based intrusion-detection software on production systems (5×)
- Sweep your phone lines for vulnerabilities (5×)
- Fix problems you find with a network vulnerability sweep (5×)

The preceding list was partly done in fun, but I also am serious. If these items are part of your critical path, you might want to give your schedule a second look.

## Follow-On Steps

At this point, you have finished everything we need to do to pitch your solution. We have defined and quantified both the problem and the solution with options. What could possibly be lacking? Will installing this solution solve all the organization’s problems? If not, you should identify some of the next steps. If you are recommending a network-based intrusion-detection system, for instance, your next steps might be as follows:

- Host-based perimeter defenses for critical systems
- Database for trend analysis, especially with the emergence of enterprise security modules that allow you to consider data from NID, HID, firewall, router, and system log files
- Internal network-based IDSs for high-value locations
- Organization-wide host-based perimeter defense deployment

Each of these steps should include a high-level estimate for timeframe and cost. Taking the time to show the next steps helps management in two important ways. It shows you have technical vision—that there really is a well thought out plan. Also the budget planning cycle for capital purchases at many organizations is done several years in advance. By presenting the follow-on steps, financial planners can use your information as budget “wedges” for future years.

# Repeat the Executive Summary

You know the drill. Tell them what you are going to tell them, tell it to them, and then tell them what you told them. This is an excellent time to repeat your Executive Summary points.

# Summary

I hope this chapter and this book have been helpful to you. This chapter was tailored for security professionals who don’t have an intrusion-detection capability, want to upgrade their capability, or have these job positions under scrutiny. In much of the book, we try to give you a bit of insight into the enemy. In this chapter, we have tried to give you insight into management and business processes.

The most important thing to keep in mind, both for yourself and when you brief management, is that intrusion detection should be an integral part of your organization’s information-assurance strategy. In fact, intrusion detection should be a part of every nation’s information-assurance strategy. The events of this coming year with massive IRC bot driven distributed denial-of-service attacks, SNMP/ASN.1 exploits, and polymorphic attacks will prove this to be true. You don’t need an IDS to detect a DDoS attack, but it will help you find the compromised hosts before they can be used to hurt someone. Now, let us take some time to discuss the future of intrusion detection in our final chapter in this book.

---

[[1]](#ch19footnote01)Courtesy of Matt Bishop, Alan Paller, Hal Pomeranz, and Gene Schultz
