# Chapter 28. Putting Everything Together

**IN THIS CHAPTER**

- **Understanding critical problems organizations face**
- **Top issues in network security**
- **Coming up with an organizational plan for network security**
- **Network security best practices**

This book discusses all the critical areas of network security. However, in a real environment it is not the individual components that will make you secure, but the integration of all the components together. While endpoint solutions and technology are important, security is about integrated solutions that are built into existing processes. This chapter looks at network security from a more holistic viewpoint, looking at strategies that can be implemented, and common problems and how they can be avoided.

# Critical Problems Facing Organizations

On the surface, security seems like an easy problem to address; however, those of us who have worked in this area for a long time know it is anything but easy. Network security is very difficult to implement because in solving one problem you could introduce five new problems. Unexpected pitfalls can await you around each corner. The important thing to remember is that security is about managing and controlling risk to your critical assets and information. By focusing on managing risk, you can ensure that you are addressing the real problems that need to be fixed. To keep you on track, remember to review the following questions for each item:

- What is the risk?
- Is it the highest priority risk?
- Is it the most cost-effective way of reducing the risk?

This section looks at critical problems facing a network security professional and what can be done to avoid or minimize the impact these problems can have.

## How do I convince managers that security is a problem and that they should spend money on it?

Selling security to upper management to get the proper budget can be a difficult problem. The fundamental miscalculation that many security professionals make is to assume that management and upper-level executives understand security and how bad the problem is. I was recently leading a round-table discussion that was attended by Fortune 1000 executives. I started off by asking how many of them felt that their organizations have had more than 100 attempted intrusions over the last six months. None of them raised their hands. A couple executives said that there might have been one or two, but definitely not a number that was in the double digits. I was shocked and amazed by that answer, especially when I knew that several organizations had 400 to 500 attempted intrusions a week occurring. The executives clearly did not know or understand the reality of the situation at their organizations.

Now some people claim that it is not the executives' job to understand and know the specifics of network security problems; that is why they hire us. While that is true at a detailed level (they do not need to understand configuration issues), they should have a high-level understanding of what and how bad the problem really is. How can executives spend the appropriate money on security if they have no idea of the problem or how bad it is?

In most organizations where people are having a hard time convincing management there is a problem it's usually because the security professionals have not given them any information on what is really happening. I know many organizations that are so concerned about presenting any bad information to executives that the security team will paint a rosy picture of how perfect everything is. Taking this approach is very dangerous because giving executives a false impression will only make things worse for you in the long run. In most cases, convincing managers there is a problem is so difficult because the only information they have to go on is positive information. Now, there is a proper balance in terms of the information you provide because you do not want to make the situation seem so dire that management thinks you haven't been doing your job. However, management does need to understand that threats exist, and will continue to exist, and that the company needs to be more focused on possible damage to the organization and on data theft than in the past. Therefore, new ways of dealing with the problem must be created. In essence, the message you want to send is that just as the attacker is evolving, the organization's security needs to evolve also. The protection that was used in the past will not scale as well as you move forward.

What I recommend in terms of helping management understand there is a problem is that you provide high-level graphs of the number of attempted attacks that are occurring against your organization each week. I would also recommend speaking their language in terms of attacks. Instead of talking about firewalls and intrusion detection systems, talk the language of executives: dollars and cents. If you go to management and say, "We need to buy a new firewall because there was an increase in NetBIOS attacks," that means nothing to them. However, if you say, "We have a risk that cost us $300,000, it has an 80 percent chance of occurring again, and we need $40,000 to prevent it," that is something an executive can understand and make a decision on. Spending $40,000 to prevent a $300,000 loss that could occur multiple times is a good return on investment (ROI), and if they have clear data to understand this is a real threat, chances are they will spend the money to fix it.

### Note

Potential risks are assigned value based on how much damage they do. This allows you to be proactive and fix problems before they turn into breaches.

## How do I keep up with the increased number of attacks?

This is a difficult problem because to keep up with the increased number of attacks you need to change your security role from reactive to proactive. However, if there are so many attacks that you are constantly being reactive, how can you ever find time to be proactive? This is one of those vicious cycles that you just have to address. In most cases, you have to slowly peel off time to fix security problems before there is an issue, not after. In addition, if you have a limited staff, security might be more of an advisory role where you work with and task other organizations to fix security problems proactively, while you still play a reactive role.

The more you do, the easier your job becomes. If you harden a server by turning off services and closing ports, it is now more secure. In making it more secure, you have actually made your job easier because now there are fewer things for an attacker to use to break in; therefore, you will have fewer attacks and be required to spend less time fixing breaches across your organization. This is the place where security truly becomes a business enabler because a good security plan reduces cost and creates a more efficient and more secure organization.

To get to a better end state, you have to have a plan for what you want to do. Figure out the critical problems and come up with a phased network design that will limit your exposure and increase your organization's security. Redesigning an entire network can be very time consuming, but you can slowly move critical servers to a different segment, harden those servers, and run automated auditing scripts that will only notify you if there is a problem. Now your systems can stay secure without your having to put in a lot of effort.

## How do you make employees part of the solution and not part of the problem?

Like it or not, no matter how well a network is designed, employees or users will always be a necessary evil. They will either be part of the security problem or part of the solution. Employees are your greatest asset (you cannot run an organization without them) and your greatest liability (they often account for many of the vulnerabilities that cause harm to an organization). Frequently, how you treat them and educate them will dictate their behavior. One way to deal with them is through fear, historically an excellent motivator. However, this usually creates an adversarial role, which might give short-term benefits but long-term headaches. This is usually not recommended, except in extreme circumstances.

A better approach is to first design the network and the employees' systems in a way that will minimize what they can do across the organization. You have to let employees have the access they need to do their jobs, but too often we give them additional access that is not needed. A big problem for organizations is spyware, and most of the systems that get infected with spyware should not have allowed the user to install any software. Most employees do not need to install software and allowing them to have this extra access can cause security problems. Understanding what employees need to do and setting up an environment that controls and limits their span of access greatly reduces the problems.

While designing systems to minimize access is important, employees must still be educated. Employees can always find a way around the system if they want to. Even though you will never impact all employees, educating employees still reaps a big benefit. Most employees want their company to be successful and want to do the right thing. The problem is they do not really understand why security is important and perceive security as just a nuisance. If you do it correctly, user awareness training can go a long way in educating employees on why security is important and what they can do to help resolve the problem. Also, while not ideal, if employees clearly know what they are supposed to do (policy), have the skills for doing it (training), understand why it is important (awareness), and still do not do it, you now have a point of enforcement to take action against the employees.

## How do you analyze all the log data?

Incidents cause damage and monetary loss to an organization. An incident is like a fire; the earlier you catch it, the less damage it will cause. The longer you allow an incident to go undetected the more damage it will inflict and the more resources will be needed to fix it. An incident is composed of events, so to know whether you have an incident and to be able to detect it in a timely manner, you must have the events available to look at. An event is an entry in a log file, and capturing your logs and reviewing them on a regular basis is a critical aspect of proactive security.

The trick with log analysis is to automate as much as you can and only pull in humans for the minimal amount of analysis to see if there is a problem later on. Having a list of set queries that will look for unusual or suspicious events helps. Then, instead of having to look through 50 pages of logs, you have to review only a small subset that has the critical information you need to make a decision. The focus should be on using clipping levels to look for potentially suspicious actions and then analyzing that information.

Another strategy that works very well is to create scripts using tools such as grep, which will go through the logs and put all critical entries into different bins. For example, anything involving the Web goes into one bin, anything involving SMTP goes into another. Then within the Web bin, anything involving logons goes into one bin and anything involving CGI access goes into another. In essence, you start off with one big bin and you divide into smaller bins. You take those smaller bins and continue to divide them until you arrive at bins with a small enough number of entries that you can use that information to quickly make an analytical decision.

## How do I keep up with all of the different systems across my enterprise and make sure they are all secure?

Rome was not built in a day, and a company cannot be secured in a day. Not every system across your organization is equal in importance; some are more critical than others. Going by your disaster recovery plan, one system or business process is going to be the highest priority for your organization and restored first. Therefore, having a prioritized list of systems helps you focus on which systems are the most important, and those systems should also be the most secure. Then you can incrementally work down the list fixing the next highest priority system.

While this strategy seems to work, it does not always scale very well. As a result, configuration management is the key. Creating a secure baseline installation is another approach that ties into this. Every new system that gets rolled out is built from a security baseline that has been tested and is known to be secure. Now, instead of each administrator securing a system in a different manner and getting mixed results, every system is secure from the beginning. Then strict change control procedures need to be put in place (through a CCB or configuration control board) to approve any changes that are made later so the system does not start off secure and deteriorate over time because no one is monitoring or controlling what changes are being made to it.

While this previous strategy works for new systems that are being rolled out, what about existing systems? It does not make practical sense to go in and rebuild existing systems. This would take too long and could be a troubleshooting nightmare if existing applications stop working. So, in the case of securing existing systems, hardening scripts works very well. The trick is to do incremental hardening and incremental rollout. Instead of going in and applying a script to all systems, you would take a small subset of the script and apply it to one box and see if there is any impact. If there is an impact, you can roll it back. If there is no impact, you can apply it to the next system. While this approach takes longer, it is much safer than an across-the-board rollout. If you go in and apply a robust script to all your systems and the systems crash, you have a major problem on your hands. If you apply a small portion to one system and it crashes, you can easily recover from that.

## How do I know if i am a target of corporate espionage or some other threat?

People often ask me whether their company is a target for attack or corporate espionage. The short answer is *yes*. Every organization, whether it is commercial, not for profit, or government, has something of value that it needs to protect. If an organization had nothing valuable or unique that it needed to protect, why would it exist? In an organization having something of value, there are always going to be people who are going to want to gain access to that information or compromise it. Therefore, protecting that information is critical.

Even though network security is still not very robust in many organizations, trying to find and compromise data across the Internet can still be difficult. In many cases, especially with organizations that carefully protect their trade secrets, the easiest way to compromise a piece of information is by getting a trusted insider who works at the company. Employees have access to critical data and, if someone wants to compromise that data, it is much easier to compromise an individual and let the individual compromise the data on your behalf. Corporate espionage is a real threat and it is occurring all around us. However, because it is being committed by trusted insiders, many companies do not even know it is occurring. Those who know it is occurring rarely publicize it, and that's one reason why most people do not believe it is a problem — they never hear about it in the news. Because every company is a target of corporate espionage and insider threat, you need to build your security posture to address this threat.

Besides the preceding threats, anyone connected to the Internet is a potential target of attack. There are worms, viruses, and attackers that just want to compromise computers so they can get access to the resources; they often do not really care about the data. In this particular case, your data is not at risk, but, if your systems and networks are compromised, it could affect business operations and still cause monetary loss across your organization.

## Top 10 common mistakes

Because the title of this book is *Network Security Bible*, it is only appropriate to have the 10 commandments of network security. Actually, these commandments are written in the form of 10 common security mistakes that you want to avoid.

1. **Presuming that one line of defense is adequate**—There is no silver bullet when it comes to network security. The only way that you are going to be secure is by having multiple lines of defense. A good network architecture starts with many layers, where each layer addresses a different threat.
2. **Insufficiently understanding the technology and its nuances, including the many approaches a hacker can take to attack you**—Knowledge is power and ignorance is deadly. Only by understanding the offense and the capabilities it possesses will you be able to build a robust, defensive posture. Too many organizations build security that does not address the true threat and, therefore, it is ineffective at securing an organization.
3. **Thinking enablement, as opposed to disablement**—When your approach to an organization's security is trying to prevent employees or users from doing things, chances of success are much lower. However, when your approach to security is as an enabler and as a way to allow people to be successful, selling security across the organization becomes much easier. Remember, in general, if you tell people they cannot do something (even if they do not need to do it), they will show resistance. However, if you tell people what they can do, they are usually more enthusiastic to help.
4. **Forgetting that security is part of a life cycle**—Security is not an afterthought or an add-on. Security must be designed into an organization and as an ongoing process. Just because you are secure today does not mean you will be secure tomorrow. Because organizations are constantly changing, security must also adapt and be an ongoing life cycle as opposed to a one-time task.
5. **Overlooking the physical aspects of security**—Buildings, rooms, data centers, physical computer access, and so on must be taken into consideration. An organization is only as strong as its weakest link. Preventing network security breaches means paying attention to the importance of strong physical and personal security.
6. **Relying on excessively weak trust or authentication mechanisms**—Authentication and validating who is allowed to do what across your organization is paramount. In many organizations, authentication is the first and only line of defense, so if it can be bypassed through weak authentication, security of the enterprise is at risk.
7. **Failing to understand exposure to attacks on information and infrastructure**—Security goes beyond having a firewall or intrusion detection systems. Security means knowing where your exposure points are, prioritizing them, and fixing them in a timely manner.
8. **Failing to understand and address the relationships between network, application, and operating system security**—Just because all the single pieces of an organization are secure does not mean that when you put the pieces together the overall system will be secure. You must not only verify the individual components but also the comprehensive system as a whole.
9. **Architecting a system that issues too many false alarms**—Unfortunately, there is usually a tradeoff between false positives (system giving an alert when it should not) and false negatives (system not giving an alert when it should). Because false negatives represent a breach, most systems are designed to err on the side of false positives; however, neither option is good and both should be reduced.
10. **Inadequately addressing the risk of security breaches from those within your organization**—Most networks are designed to prevent attacks from occurring from the Internet. While this is an important vector, insider threat and attacks are just as critical. It is important that organizations understand all potential threats and address them accordingly.

# General Tips for Protecting a Site

This book has covered a wide range of network security issues and concepts. This section summarizes six key points that must be covered to have a proper level of security. No matter how large or small your organization is, these tips are critical to having a secure infrastructure:

- Defense in depth
- Principle of least privilege
- Know what is running on your system
- Prevention is ideal but detection is a must
- Apply and test patches
- Regular checks of systems

## Defense in Depth

When it comes to security, everyone is looking for the one technology that will solve all of a company's security problems. Sadly, it does not exist. As with anything in life, there is no free lunch; if you want to achieve a goal, you have to work hard and make a lot of sacrifices. Security is no exception. Companies are not only going to have to spend money, but also invest in people and resources to have a secure enterprise. The more protection measures a company has in place the better, and this is the fundamental concept of the principle of defense in depth. A company must have multiple measures in place to secure the organization. As previously mentioned, a very good example of defense in depth is medieval castles. The people who designed and built those castles knew a thing or two about defense in depth and incorporated a number of protection measures into the castle:

- Castles are always built on a hill so it makes it more difficult for someone to attack. It also makes it easier to see if someone is trying to attack you.
- At the bottom of the hill is a stone fence, usually only a couple of feet high. This fence is not meant to stop the attackers but to slow them down.
- Around the castle is a moat, which also makes it more difficult for someone to gain access.
- At periodic intervals around the perimeter there are fortified towers, where defenders of the castle are not only on the lookout, but also in a better position to fight back.
- There is only one way in and one way out of the castle. Having a single point of entry makes it easier to defend. You do not have to spread out your resources and defend four different areas; you can concentrate all your resources in one area.

The builders realized that any single measure could be defeated but by putting several measures together you achieve a much higher level of security. The goal was ideally to prevent attack, but in cases where these couldn't be prevented, enough measures were put in place so that attackers were detected before they gained full access.

This same principle should be used when building a company's network security. So many companies install a firewall and think they are secure. A firewall is a good starting point, but you must combine firewalls with intrusion detection systems, host-based protection, encryption, and any new technologies that come along.

Employing multiple defensive measures is key; another key measure is to give entities (which can be users or computers) the minimum amount of access needed to do their jobs. This is called principle of least privilege and is discussed in the next section.

## Principle of least privilege

Whenever anyone or anything is given more access than needed the potential for abuse increases. When it comes to security, people and programs should only be given the least amount of access needed to perform their jobs and nothing else. This is the foundation for the principle of least privilege. I consulted for one company where everyone who worked in IT had domain administrator access. When I questioned people about this their response was, "Because someone might need that access at some point, we figured it was better that they have it than have to ask for it later." In this case, the company was adhering to a principle of most privilege, giving users the most access they would ever need, and they wondered why they had so many security issues. Users will always want more access than they need to do their jobs. The way I get around this is this: instead of having users tell me what access they need, I have them tell me what job functions they need to perform. Based on those functions, appropriate access can be provided to them.

From an application or software standpoint, this can be a bigger problem. If an application is running as root and an attacker can compromise the program, they immediately have root access to the system. All applications should be reviewed to see what access they require to run correctly and be given the least amount of access necessary. Limiting the access that both users and applications have to a network will go a long way to protecting it from potential abuse. Of course, to limit access to applications and software, you must be aware of exactly what is running on your systems.

## Know what is running on your system

The only way that you can secure your systems and network is if you know what is running on them. Things that you must be aware of are operating systems versions and patch levels, applications and versions, open ports, and so on. An attacker is most likely going to compromise your system by taking advantage of an open port or a vulnerability in the software that you are running. If you do not know what is running on your system, you will not be in a position to protect and defend against these types of attacks.

So many companies install servers and run applications but have no idea what is actually running on their system. A common way that attackers break into a system is by compromising test or sample scripts that were automatically installed on a system when the software was installed. In most cases, the company did not know the software was present on their system.

If you know what is running on your systems, including key systems, you will be able to decrease the number of successful attacks against your system. Even with strong security, an attacker will still potentially be able to penetrate your defenses; in those cases you need to be able to detect the attack as soon as possible.

## Prevention is ideal, but detection is a must

Ideally, a company would like to set up its security so to prevent all attacks. If this were possible, a company would set up security once and be done with it. Unfortunately, not only does security constantly change, but as soon as a company connects to the Internet, preventing every single attack becomes impossible. There will always be some attacks that sneak through. This is true mainly because a company connects to the Internet to provide additional functionality to the company and their employees. As long as legitimate traffic needs to flow in and out of the company, other traffic will be able to sneak in. The only way a company could come close to preventing all attacks is if they deny all inbound and outbound traffic, and doing so defeats the purpose of connecting to the Internet. When it comes to functionality versus security, functionality always wins. Hopefully, as awareness increases, a better balance will be struck and the importance of security will be properly weighed.

Because a company cannot prevent all attacks, when an attacker does sneak into a network, the company must be able to detect it. If an attacker can gain access to a network and the company is not able to detect him, the attacker will have full access to the entire network. The sooner a company can detect an attack, the less overall damage the attacker will cause. A strong perimeter is a good starting part, but having mechanisms in place for early detection and warning is key.

Not only is detection key, but if a company increases the security of its hosts by applying the latest security patches, it can decrease the chance of a potential compromise.

## Apply and test patches

New exploits are discovered on a regular basis. In most cases, they take advantage of an error in the underlying operating system or application. Therefore, the only way to protect against these exploits is to apply the appropriate patch from the corresponding vendor. Most vendors have special areas of their Web site where they post known security vulnerabilities in their software and where they make the patch to fix the problem available. You need to find these Web sites and review them on a regular basis. When a new patch comes out you can apply it before an attacker breaks in. A key thing to remember is that if a vendor acknowledges a vulnerability, you can assume that all the attackers also know about it. Every day that passes without your system being patched is an open invitation for an attacker to compromise your system. Also, not only should patches be applied on a regular basis, but they should also be tested before they are loaded on an operational system. Just because a vendor releases a patch does not mean that when you load it on your system the system will continue to work properly. The only way to guarantee this is to test every patch on a test server before applying it to your production servers.

The fact that new patches are released all the time means that new vulnerabilities are being discovered constantly. So just because a system is secure today does not mean it will be secure tomorrow. A company's security is constantly changing, and to keep up with it, checks of the system must be done on a regular basis.

Keep in mind that a patch is the vendor putting you on notice that there is a known vulnerability in its product. Therefore, a patch is an accident waiting to happen.

## Regular checks of systems

In a company environment, new systems are always being added, new applications are being loaded, and older applications are being removed. To maintain a secure environment, systems must be scanned on a regular basis looking for any unusual changes. For example, if new user accounts appear or new ports are open, this could indicate either an attempted or successful compromise. Security is not something you set up once and forget about; it must be constantly reviewed and updated.

# Security Best Practices

The following are best practices that should be deployed within any organization.

## Create security policy statements

The most important security practice, that which all other security controls and on which protections are based, is the creation and enforcement of security policies. Every organization must have an overall policy that establishes the direction of the organization and its security mission, as well as roles and responsibilities. There can also be system-specific rules to address the policies for individual systems and data. Most important, the appropriate use of computing resources must be addressed. In addition, policies can address a number of security controls from passwords and backups, to proprietary information. There should be clear procedures and processes to follow for each policy. These policies should be included in the employee handbook and posted on a readily accessible intranet site.

The organization's security policies should address applications, services, and activities that are prohibited. These can include, among others, viewing inappropriate material, spam, peer-to-peer file sharing, instant messaging, unauthorized wireless devices, and the use of unencrypted remote connections such as Telnet and FTP. Appropriate-use policies should outline users' roles and responsibilities with regard to security. They should provide the user community with an understanding of the security policy, its purpose, guidelines for improving security practices, and definitions of security responsibilities. If an organization identifies specific actions that could result in punitive or disciplinary actions against an employee, these actions and ways to avoid them should be clearly explained in the policy.

It is also a good idea to create an administrator acceptable-use policy. This policy addresses procedures for user account administration, policy enforcement, and other administrator-specific roles and responsibilities. Administrator requirements should be included in training and performance evaluations.

## Create and update the network diagram

It is surprising how many organizations don't even have a network diagram. In order to implement the best security practices, an organization must know what it is protecting. An organization must know the following:

- Physical topologies
- Logical topologies (Ethernet, ATM, 802.11, VoIP, and so on)
- Types of operating systems
- Perimeter protection measures (firewall and IDS placement, and so on)
- Types and location of devices used (routers, switches, and so on)
- Location of DMZs
- IP address ranges and subnets
- Use of NAT

In addition, the location of the diagram must be known and it must be regularly updated as changes are made. Network management software, such as HP Openview, can perform network device discovery to make this effort easier. It can then produce an alert when new devices come online. One word of caution regarding a network diagram being made available publicly: this type of information is very valuable to attackers and therefore should be kept private.

## Place systems in appropriate areas

To protect systems from unauthorized access, they must be placed in areas of the network that give users of the system the least amount of privileges necessary. Only systems that are semi-public are kept in the DMZ. This includes external Web servers, external mail servers, and external DNS. Limited access to these systems is allowed from the Internet. A split-architecture may be used where internal Web, mail, and DNS are also located on the internal network. In addition to internal Web, mail, and DNS servers, the internal network also includes databases, application servers, test and development servers. Access to these systems is limited to internal users only and they are not accessible from the Internet.

## Protect internal servers from outbound communications

Internal servers should not connect out to the Internet. Sometimes organizations have had administrators who use internal servers as their personal systems and perform normal activities on it such as accessing the Internet and checking e-mail. Internal and other servers should never be used as personal systems. It is also a good idea to add rules to the internal firewalls to block internal servers from outbound traffic. If the server needs to access other network segments, a specialized rule can be created for that, or just block the internal server's outbound access at the Internet connection perimeter firewall. If effective security controls are used on the firewalls and intrusion detection systems, not only will the servers be denied access outside the network, but if the server attempts to access the outside, an alert will be generated and the administrator notified of a potential problem.

## Assess the infrastructure

Identifying the critical business systems and processes is the first step an organization should take in order to implement the appropriate security protections. Knowing what to protect helps determine the security controls, and knowing the critical systems and processes helps determine the business continuity plan and disaster recovery plan process. Critical business systems and processes may include an e-commerce site, customer database information, employee database information, the ability to answer phone calls, the ability to respond to Internet queries, and so on.

In addition to identifying the critical business systems and processes, it is important to identify the possible threats to those systems as well as the organization as a whole. Considerations should be made for external and internal threats and attacks using various entry points (wireless, malicious code, subverting the firewall, and so on). Once again, this will assist in implementing the appropriate security protections and creating business continuity and disaster recovery plans.

An organization must understand how an outage could impact the ability to continue operations. For example, it must be determined how long systems can be down, the impact on cash flow, the impact on service level agreements, and the key resources that must keep running.

## Protect the perimeter

Multiple layers of security should provide protection at the perimeter. This includes a border router with access control lists that perform ingress and egress filtering, a stateful inspection firewall, and application proxy firewalls. Intrusion detection systems should also be placed at the perimeter. There should be a default deny rule on all firewalls to disallow traffic that is not explicitly permitted. This is more secure than explicitly denying certain traffic because that can create holes and oversights on some potentially malicious traffic.

## Create a strong password policy

Most system compromises are the result of weak passwords. Users create easy-to-guess passwords, administrators often forget to remove default accounts and passwords on devices, and unused accounts contain passwords that don't change. For systems that rely upon password protection for authentication, users should select good passwords and periodically change them. Password guessing and cracking attacks are common ways of gaining unauthorized entry to networks, and even the best passwords can eventually be broken, given enough time. The use of strong passwords provides a firm deterrent against password guessing attacks and buys additional time against cracking attacks.

The following guidelines enforce a strong password policy:

- The password must be at least eight characters.
- It should contain both alphanumeric and special characters.
- A user can't reuse his/her last five passwords.
- Passwords must change every 60 days.
- Accounts are locked out after three failed login attempts.

UNIX systems should be using the shadow password feature. Previously the encrypted user passwords were readable in the /etc/passwd file. Shadow password removes the encrypted passwords to a protected /etc/shadow file.

A strong password policy is one of the best security measures to prevent unauthorized access. However, encouraging users to adhere to the policy is difficult because they will want to create passwords which are easy to remember and don't change. Most operating systems now have mechanisms to enforce strong password policies. The following examples allow the enforcement of the password policy at the operating system level:

- **Password aging**—Allows forcing the user to change his password periodically
- **Minimum length**—Allows the enforcement of a minimum password length
- **Non-dictionary words**—Allows stopping the user from selecting a password that is in a standard dictionary
- **Password uniqueness**—Allows specifying the number of new passwords that users must select before they can reuse a previous one
- **New password**—Allows setting a minimum number of characters required for the new password that is different from the previous password

## Create good passwords

The following best practices provide additional guidelines for creating strong passwords:

- Use passwords with upper and lower case letters. Don't just capitalize the first letter, but add other uppercase letters as well.
- Use a combination of uppercase, lowercase, numbers, and special characters.
- Create a password that can be typed quickly without having to look at the keyboard. This deters "shoulder surfers" from attempting to steal passwords.
- The more critical an account, the more frequently it should change. Root and Administrator passwords should be changed more frequently than users' passwords.
- Never use the username in any form as a password.
- Never use first names, middle names, last names, initials, or nicknames as a password.
- Don't use words contained in dictionaries.
- Don't use personal information that is easily identified, such as pet names, children's names, car make or model, address, and so on.
- Don't use a password containing just numbers or characters.
- Don't write down passwords.
- Don't tell anyone a password.
- Don't use shared accounts.
- Don't use a password that is overly long. Long passwords are difficult to remember and it is more likely that it will have to be written down.
- Make a password easy to remember but hard for others to guess.
- Use passphrases instead of passwords. A passphrase is a sentence that you type in as a password. While it does take longer to type it, it is easier for the user to remember and harder for an attacker to guess.

## Audit passwords

Regular password auditing should be performed to check the strength of passwords and to enforce the password policy. Make sure before performing any password auditing that approval is received from the legal department. Once this is done, create a process for regular password auditing. Password cracking tools such as Cain or John the Ripper can also be used. When the password cracking is complete, note the passwords that do not follow the proper policy and lock out the accounts of those in violation. Next, send an e-mail to the users of these accounts with a copy of the password policy. Require them to sign a copy of the policy before unlocking the account. Multiple violations may result in disciplinary action.

Be sure when performing password cracking to perform the cracking on an offline system and do not store the cracked passwords on a computer. If these are forgotten about and left on the system an attacker or malicious user may stumble across them and use them to the attacker's advantage.

## Use strong authentication

Because passwords are created, managed and used by humans, there are still vulnerabilities with their use. If something more secure is desired, use some other form of strong authentication. One example is a one-time password system such as SecurID by RSA. With one-time passwords, if an attacker did compromise the password token, it would only be good for that one session. One-time passwords are becoming more common for Administrator accounts and for remote users.

## Remove service accounts

As mentioned previously, administrators often forget to remove default accounts and passwords on devices. These default accounts are usually service accounts that allow maintenance or other privileges. They often have either system- or domain-administrator-level privileges. These accounts are often forgotten about and left unused for long periods of time. Attackers regularly scan for these accounts and their default passwords. An attacker who discovers or cracks the password of a service account inherits the privileges of that account and can often use the account for long periods of time undiscovered.

## Create a patching policy

It is a common best practice to patch systems as soon as a new patch is released. Unfortunately, many organizations don't patch regularly and tend not to patch critical systems because they don't want to risk downtime. However, critical systems are the most important to patch. Unpatched systems have been the leading contributor to the recent worm attacks. The Blaster and Slammer worms are two good examples of exploits that could have been easily mitigated had patches been applied in a reasonable amount of time. A worm finds an unpatched system, exploits the vulnerability, and uses that system to continue scanning for other unpatched systems in order to propagate. Thus, a worm that is wreaking havoc on the Internet means there are a lot of unpatched systems!

Regular maintenance downtime must be scheduled to patch systems. As vulnerabilities are discovered, attackers often release exploits even before system patches are available. Therefore, it is imperative to patch systems as soon as possible. Security patches from the system vendors, such as service packs, maintenance updates, and software updates, can close most of the known security holes. New releases of patches from the vendors of the systems must be monitored. While some systems offer an automatic update process, others require a visit to the Web site or require a subscription to an e-mail list. Subscribing to a vendor's patch release bulletin and having support contracts with vendors is one way to ensure that you get the latest information automatically.

Different strategies may be adopted when applying security patches suitable to the system architecture. One method is to apply every relevant and available security patch to operating systems and applications. Another method is to verify the need for a particular patch to the system and install it if required. In either case, whenever a new security patch is available, carefully study the details of vulnerability and its impact on the systems and environment. Depending upon the risk, it is necessary to decide how to proceed with the patching strategy.

Keep in mind the following patching information:

- Fully patch systems before connecting them to the network.
- Continually update systems as patches are released.
- Re-patch the system if adding an additional service or application to the system.
- Test patches in a lab environment before applying them to check for adverse effects.
- Keep system backups in case there isn't time to test a patch first, or in case the patch causes problems even after testing.
- Keep a list of patches and service packs that are applied to critical systems in case of a rebuild.
- Make use of the free automated tools such as the Microsoft Baseline Security Analyzer.
- Incorporate scanning for patch level compliance into regular vulnerability assessments.

## Perform regular vulnerability assessments

Regular vulnerability assessments are essential to maintaining the ongoing security of an organization and should be performed as often as possible. Scanning should be scheduled to allow adequate time to look through the reports, to assess changes, and to mitigate any vulnerability. Awareness of vulnerabilities enables organizations to take corrective action before an attacker exploits them. Various commercial and open source tools are available for vulnerability scanning. These tools scan systems and look for open holes and known exploits. As vulnerability scanners are updated, they require new signatures, similar to antivirus tools. The scanning tool provides a report of the results with a criticality rating of each vulnerability and recommends corrective actions. However, it is up to the administrator to analyze any vulnerability, assess its impact, and apply the appropriate corrective actions. Critical vulnerabilities should be addressed immediately. Otherwise, plan on fixing any non-critical vulnerabilities during scheduled system downtime. Lastly, once a corrective action is applied, scan the system again to ensure the vulnerability no longer exists. It is not uncommon for one patch to undo a certain corrective action from a previously applied patch. Every time a system is altered, assume that a vulnerability may exist. Thus, repeated scannings after each alteration can ensure that the system is secure.

## Enable logging

Some administrators don't enable logging because they get a barrage of log events and it ends up being too much information. However, it is critical to log events. Focus on logging only those events that either alert administrators to problems or in some way help manage the system better. Too much logging generates useless data and hides the important information. Logs provide an audit trail and evidence in case of an attack. Once attacked, without logs, there is little chance of discovering what the attacker did. Without that knowledge, it isn't clear whether a system should be completely rebuilt or whether a certain problem needs to be fixed. Because the length of the attack is unknown, backups could be compromised as well. Logs provide the historical detail of what systems are being attacked or misused, what systems are having unauthorized access, and what systems have been compromised in some way. Enabling system logging is usually an easy task for most operating systems.

## Review logs

Enabling logging only works if the logs are being reviewed. One of the biggest mistakes an organization can make is failure to review logs. Logs should be reviewed every day. This includes IDS logs, system logs, management station logs, and so on. Interesting events in the logs should be investigated daily. However, it can be a tedious task for a single person to perform log review every day (unless this person really enjoys it). It is better to have a log review rotation system among the security team. Log review is also typically part of a penetration test. The penetration testing team intentionally leaves traces of its activities in logs to test whether the security administrators are actually reviewing the logs.

Typically a constant stream of port scan attacks will be present in the logs. These are regular occurrences on the Internet because of attackers and worms. On a secure system, the logs should not be reporting very many substantial attacks, such as root compromises, back doors, or exploits, on systems. This would indicate that the security defenses are weak, patching may not be occurring, or other vulnerabilities exist.

A centralized logging and event correlation system assists with log review. Some products provide summaries and statistics in graphic or tabular format to make analysis easier. Some products also have sophisticated correlation engines to understand the big picture. These tools can also be used to analyze trends in the network or on systems and assist in mitigating performance issues. By using a centralized syslog server and automated tools, the administrator can easily review logs on a regular basis, recognize security alerts, perform system analysis, and save logs offline for future reference.

Last, an important aspect of logging, especially when using a centralized log server, is to protect the logs. Attackers love to gain access to logs, to see if they were detected and possibly cover their tracks. They may also use logs to gain valuable information about a network or system and the services installed. A properly configured and locked down centralized log server makes it much more difficult for an attacker to access logs or edit them.

## Use multiple detection methods

To provide the best level of detection, an organization should use a combination of both signature-based and anomaly-based intrusion detection systems. This allows both known and unknown attacks to be detected. The IDSs should be distributed throughout the network, including areas such as the Internet connection, the DMZ, and internal networks.

IDSs come loaded with default rule sets to look for common attacks. These rule sets must also be customized and augmented to look for traffic and activities specific to the organization's security policy. For example, if the organization's security policy prohibits peer-to-peer communications, then rules should be created to watch for that type of activity.

## Monitor outgoing communications

Organizations often focus on traffic and attacks coming into the network and forget about monitoring outgoing traffic. Outgoing traffic should be inspected before it leaves the network, looking for potentially compromised systems. Not only will this detect systems compromised by Trojans and back doors, but it will also detect potentially malicious or inappropriate insider activity.

## Perform content inspection

In addition to the content-level inspection performed by the IDS, specific content inspection should also be performed on Web server traffic and other application traffic. Some attacks evade detection by containing themselves in the payload of packets, or by altering the packet in some way, such as fragmentation. Content-level inspection at the Web server or application server will protect against attacks such as those that are tunneled within legitimate communications, attacks with malicious data, and unauthorized application usage. The types of content checking that should be performed include:

- **Binary code in HTTP headers**—Attacks can be launched by including executable code in HTTP headers. This violates the HTTP protocol standard. However, most firewalls don't check for this type of content.
- **HTTP or HTTPS tunneling**—Various types of communication can be tunneled through HTTP and HTTPS ports 80 and 443. This includes peer-to-peer (P2P) file sharing and instant mail and remote management software. They comply with protocol standards, so most firewalls do not block them. Tunnels also provide a means for attackers to install sniffers and Trojan programs, allowing them to eavesdrop on network communications and create back doors. Malicious traffic can also be tunneled over other protocols that are normally permitted by a firewall, such as DNS and SMTP.
- **URL directory traversal**—Directory traversal involves using the "..." notation within a file system to access restricted files and directories, and possibly execute code on the Web server. This is a very trivial attack to execute. By exploiting directory traversal vulnerabilities, an attacker can access files in other directories, such as the cmd.exe program on Windows, or the passwd file on UNIX. Another way to traverse directories is by using escape codes and Unicode in the URLs. All URL requests should be inspected and rejected if they contain any escape or Unicode characters.
- **Excessive URL header length**—HTTP URL and header length is not restricted in the HTTP protocol standard. However, excessive URLs and headers can be used in buffer overflow attacks. Buffer overflows can be exploited by excessive lengths in URLs, GETs, POSTs, and header fields.
- **Cross-site scripting**—Cross-site scripting (XSS) attacks exploit the client-server trust relationship on the Web by using specially crafted URLs containing malicious code. This code, usually JavaScript, VBScript, ActiveX, HTML, or Flash, can be hidden and inadvertently executed by unsuspecting users when they interact with the Web application.
- **Malicious URLs**—Malicious data can enter the network by being embedded in URLs and executed by the user, or automatically by a mail client.
- **Inspect file transfers**—Content filtering and access control should be performed at the application layer to regulate the transfer of file names containing certain keywords. For example, a firewall could deny the transfer of files with the words "passwords" or "proprietary" in the names. In addition, access control should also be applied to the content of the files. Files containing the words "password" or "proprietary" anywhere in them could be denied, too.
- **Inspect mail attachments**—Content filtering and access control should also be performed on incoming and outgoing mail attachments. Viruses and worms often spread via mail attachments. Therefore, both incoming and outgoing mail should have the attachments inspected for malicious code, and then sanitized or blocked.

## Control and monitor remote access

Remote access should be tightly controlled, monitored, and audited. It should only be provided over a secure communication channel that uses encryption and strong authentication, such as an IPSec VPN. Desktop modems, unsecured wireless access points and other vulnerable methods of remote access should be prohibited.

Organizations don't always consider wireless networks when referring to remote access. Part of knowing the network architecture includes knowing the location of wireless networks because they create another possible remote entry point for an attacker. It must also be determined whether they are being used for sensitive data and are sufficiently secured.

While not recommended, if you have no other choice, wireless access must at least use WEP with 128-bit encryption. Although this provides some security, it is not very robust, which is why the wireless network should not be used for sensitive data. Consider moving to the 802.11i standard with AES encryption or WPA/WPA2.

## Use defense in depth

Defense in depth means applying security in multiple layers. We mentioned previously how that can be applied at the perimeter. Defense in depth is actually applied throughout the network from the perimeter down to the actual desktop. In addition to routers with filters, stateful firewalls, proxies, and intrusion detection, system level protection must be implemented. Desktops should have a combination of antivirus software, personal firewall, and host-based intrusion detection. Each of these software packages must be regularly updated as new signatures are deployed. They should also be centrally managed and controlled.

Another layer of defense in depth is monitoring for any unauthorized modification of system files and configuration files. Various tools are available that enable those monitoring to determine if files are created or deleted or if permissions are modified. Typically these tools will build a database that includes information such as file size, permissions, digital signatures, number of files on the system, and so on. It then periodically computes a new database and compares it to the old one for changes. Tripwire is an example of a tool that performs file-system-level protection. Tripwire checks to see what has changed on the file system and provides an extensive report.

## Secure communications

Secure communications such as VPNs should be used for remote access and other sensitive communication. IPSec is a great choice for this purpose. Strong encryption protocols such as 3DES and AES should be used whenever possible. Web access to sensitive or proprietary information should be protected with 128-bit SSL. Remote system administration should use SSH. Sometimes file system encryption is also used to protect stored data.

## Back up frequently and regularly

As much as you would like to think that nothing bad will ever happen to your computer, unfortunately hardware does fail, systems are compromised, and other disasters make systems unusable. Thus, backing up a system is always a good practice. It is imperative to business continuity and disaster recovery to implement a reliable backup and recovery process. Built-in backup software included with the operating system or third-party solutions can be used. Some important considerations when planning a backup strategy include the following:

- Assess how frequently data should be backed up and what the best time is to back up.
- Decide how much data there is to back up.
- Determine if full configurations or partial (incremental/differential) configurations will be saved.
- Select the type of backup media to use (tape, disk, server, other location).
- Choose the software that will be used to back up systems (ArcServe, BackupExec, Networker, Norton Ghost, and so on).
- Verify which administrators will have primary and secondary backup responsibilities.
- Determine the location of offsite storage for backups.
- Decide how long the backup data should be stored.
- Prepare secure storage of the backup data.
- Document the backup and recovery process accurately.

A good backup policy includes weekly full backups with incremental backups performed daily. This includes all critical systems. In addition, the backups should be stored at an offsite location. Because backups include very valuable, easily accessible information, only trusted individuals should be performing them and have access to them. An organization should also encourage users to perform local backups as well.

Every organization should maintain full and reliable backups of all data, log files, and anything else that is necessary or useful for normal operations. Make sure to back up configurations, such as the Windows registry and configuration files used by the operating systems or applications. Also, archive all software, upgrades and patches off-line so they can be reloaded when necessary. Some other best practices for backups include the following:

- Verify and log that backups were completed successfully.
- Maintain a written log of media usage and properly labeled media.
- Write-protect media as appropriate.
- Check the media before usage.
- Determine the length of time the media will be saved and whether or not it will be reused.
- If using a hardware backup system, seek training if appropriate and review the manufacture recommendations for device maintenance.

The backup and recovery process is not complete until it is tested. Be sure to document the backup procedures and test them. Test the recovery process periodically to ensure that data is being backed up correctly and that the recovery process is correct and easy to follow.

## Protect sensitive information

Sensitive and proprietary information is knowledge that might give an advantage if revealed to persons not entitled to know it. It must be protected because its unauthorized disclosure, alteration, loss, or destruction will, at the very least, cause perceptible damage to someone or something. Thus, due care should be taken to protect sensitive information when in use, storage, transit, and disposal. We have previously addressed protecting data in storage and in transit by using encryption. There are also special methods of safely disposing of sensitive information. Hard copies of sensitive information should be destroyed by pulping, shredding, or incinerating. Sensitive information on hard drives and disks should be completely erased using special software or the disks must be destroyed. Simply deleting a file is not sufficient to prevent attackers from undeleting the file later. When disposing of a computer system, be sure to erase all sensitive files from the hard drive by using a wipeout utility.

## Create and test a disaster recovery plan

The destruction caused by natural disasters supports the fact that every organization must think about such disasters and have a plan in place to maintain business operations and handle the recovery. A disaster recovery plan (DRP) should include recovery of data centers and recovery of business operations. It should also include recovery of the actual physical business location and recovery of the business processes necessary to resume normal operations. In addition, the DRP should address alternate operating sites.

Unless tested regularly, at least once a year, the DRP will not be effective. The test will iron out problems in the plan and make the plan more efficient and successful if/when it is needed. Testing can include walk-throughs, simulations, or full-out implementations.

## Control and monitor the physical space

Physical security is a large topic that must be addressed by an organization. An example of physical controls include physical access controls (signs, locks, security guards, badges/PINs, bag search/scanning, metal detectors), CCTV, motion detectors, smoke and water detectors, and backup power generators.

Critical system consoles should be physically protected. The system should be located in a secure area where only authorized personnel are allowed. An unprotected console allows an attacker to easily access the system. There are bootable CD-ROMs that can reset or bypass root passwords. Most systems also have some sort of console password recovery procedure to break into the system as well. Do not leave the console logged in at any time while away. Make it a practice to log out or lock the screen every time after completing a task. If the system supports a timeout feature for the system console, be sure to use it.

## Educate users

Humans are always the weakest links in the security architecture. We have already addressed the human tendency to create weak passwords. Humans also tend to give out too much information about the network and systems, or to fall for attacker tricks out of compassion, sympathy, or plain ignorance.

Two common attacks that exploit the human factor are social engineering and phishing. A typical social engineering attack is known as the "helpless user," who is usually traveling or in a remote location. Here the attacker masquerades as a remote user with an important deadline to meet, often impersonating someone high up in the organization. Help-desk or other support personnel may be pressured into giving out passwords, or resetting them, or providing other types of information to the attacker because people tend to genuinely want to help the helpless. On the other side, another typical social engineering attack is when the attacker pretends to be a technical support person and gets information out of an innocent (but ignorant) user. This is often the easiest and best way to get passwords. Often, rank helps in this scenario, too. Phishing is a newer social engineering e-mail-based attack that tricks users into going to a Web page, which they think is authentic and entering their credentials. However, the Web page is an imitation used by an attacker to collect information such as account numbers, usernames, passwords, and credit card information. This attack has been popular for eBay and PayPal accounts. It is also closely related to identity theft.

The best way to protect against these types of attacks is to educate the users. Employees should attend security awareness training that explains the types of attacks, what to expect, and how to respond. There should also be a publicly posted incidents e-mail address to report suspicious activity. Users should also be constantly reminded and updated on secure practices through a security awareness program.

## Don't forget about the code

For a long time, security was driven at the network and system level. Not as much attention was given to application development security. Any development that is taking place in-house should include security from the beginning of the development process. Security needs to be a part of the requirements and testing. A test team should conduct code reviews to look for vulnerabilities, such as buffer overflows and back doors.

## Secure UNIX systems

Over the past few years, the popularity of freeware versions of UNIX has increased. This is due to the low cost, variety of supported hardware, and increased ease of use of the operating systems. However, due to this fact, the number of security incidents involving UNIX systems has also risen. This was mainly because freeware UNIX operating systems were inherently insecure out of the box. However, this is changing. Any organization or user running a UNIX operating system needs to make a serious and ongoing commitment to securing and maintaining the security of that system. Some general best practices for the security of UNIX systems include the following:

- Never let the root password travel the network in the clear—use SSH, SFTP, or other encrypted communications.
- Enforce a strong password policy.
- Get on a vendor's patch notification list.
- Remove unnecessary services from `/etc/inetd.conf`.
- Use the latest version of sendmail, if providing a mail service.
- Review logs and investigate unusual events.
- Run a file integrity software program such as Tripwire.

## Install only essential services

It is best to maintain systems and servers with the minimum services and packages (applications). The more services and packages that are running, the greater the risk of exposing the system to exploitation. During the operating system installation, minimize the service components and packages installed. Install only essential services that are required for running the packages that are in use on the system. Additional services and packages can always be installed later as needed. Similarly, if the decision is made to remove an application package from a system later, remember to remove the associated underlying services if these are not necessary for other applications. The method used to disable services depends on the operating system. It may be necessary to disable it through the Services window in the GUI or by editing a services file, such as `/etc/inetd.conf`.

Also, make sure to close any unused TCP/UDP ports. Ports that are open can be found with the `netstat` command or by running a port scanning tool such as nmap. Open ports can indicate services that weren't closed, services that were unknown, or even back doors. Any open TCP/UDP port offers an attacker a possible entry point into the system. Thus, having any port open that is not absolutely necessary should be avoided.

## Deploy single-use servers

Multiple-use servers lead to multiple vulnerabilities. When running servers, it is best to run a dedicated server for each package, for example a mail server, a Web server, a DNS server, and so on. Installing all those packages on a single server not only creates performance issues but also opens up many avenues of attack on three critical systems in a single shot.

## Perform configuration management

It is a good practice to document any change in the system configuration, whether it be hardware or software. This assists in the disaster recovery process, intrusion detection, troubleshooting, and so on. Documentation is crucial when several system administrators are managing the same systems. It facilitates good communication and keeps everyone on the same page. It is recommended to maintain additional copies of the documentation on software backups or as a hard copy stored offsite. Taking configuration management one-step further, implementation of a configuration control board (CCB) is an option. This way, whenever a change needs to be made to a system, it must be approved by the CCB. Depending on the organization, this can be for major changes, such as adding a new package to a system, or even for smaller changes. The CCB reviews the change to assess its impact and possible consequences and then approves or denies the request. The CCB usually encompasses representatives from various parts of the organization including network administrators, system administrators, project managers, and so on.

## Use firewalls and IDS beyond the perimeter

This practice goes along with defense in depth. The perimeter is secured with multiple layers and the servers and desktops are secured with multiple layers. But don't forget about internal networks. If an attacker does successfully breach the network's perimeter, there must be other hurdles to protect internal network segments. For example, an attacker could also compromise a system in a department such as HR and use it to attempt to access another system in Accounting. Deploying firewalls to protect internal departments can stop these types of attacks. Additionally, using internal firewalls can protect against a malicious insider and worm propagation.

In order to implement firewalls between internal networks, the network must be segregated. This means that different departments should be physically and logically separated on the network. Different departments can be physically connected to different edge switches or use VLANs to perform the segregation. Unless there is a specific reason, internal departments should not need access to each other. For example, Payroll should not need access to Research and Development. A properly segregated network will cut down on the potential for insider abuse and limit the damage that an attacker who does gain entry can do, because the attacker will be limited to only a small portion of the internal network. Internal firewalling and network segregation also makes troubleshooting and pinpointing events easier.

If there is a breach in security or if some other malicious or unauthorized activity occurs, the IDS on the internal networks will detect this. IDSs should be deployed within each segment of the network and designed in a distributed fashion for centralized reporting. This allows the administrator to monitor a single alert station while having awareness of the entire network. While the goal of internal firewalls is to prevent unauthorized access, the goal of the internal IDS is to alert to unauthorized access, and therefore, mitigate any damage before it can occur.

## Question trust relationships

Beware of who is trusted when creating partner and extranet networks. Just because all the protections necessary to ensure the security of a network are applied, this doesn't mean that other organizations do the same. Even other, separate parts of the same organization may not be as secure. Attackers who compromise a system on a network that an organization network trusts can use that trust relationship to come right into the network. Anything that connects from an organization's network to another network can be considered a trusted relationship. When connecting to another entity, consider the following:

- Is this connection necessary?
- How much access does the connection require?
- What additional security controls will be needed to protect the trust relationship?
- What security controls does the other entity use?
- What policies does the other entity have in place?

Make sure there is a clear policy between each organization and the outside entities that outlines appropriate use and actions that will be taken in the event of inappropriate and unauthorized activity. A good way to secure the trust relationship is to segregate the trusted connections into the DMZ. Anything that can be done to limit trusted access will help in ensuring that the network remains secure and will not be comprised by another's lack of security.

## Use antivirus software

Today's viruses are very capable of hiding themselves and covertly monitoring the system and performing actions, such as keystroke logging and other malicious events. Install antivirus protection systems at critical points and keep them current. Critical points include servers (scanning files) and mail (scanning inbound and outbound e-mail attachments).

## Protect system accounts

Unused and unprotected accounts are an attacker's gold mine. Make sure to remove all unnecessary accounts. Simply disabling an account is not sufficient to protect it. Attackers can enter a system through one account and re-enable a disabled account to escalate privileges. In multi-administrator networks, a system administrator might not consider an account being re-enabled a problem because another administrator probably did it. This is where configuration management would be necessary. It is particularly dangerous to disable (instead of remove) a privileged account of an administrator, power user, or executive when they leave the organization. Some organizations simply disable the accounts until someone new comes to take that person's place. These placeholder accounts are very inviting to an attacker. When someone leaves an organization, no matter who it is, the account should be removed, not merely disabled. Also, be sure to remove default accounts such as maintenance accounts, guest accounts, and so on.

Another good practice is to rename default administrative accounts. Renaming these accounts makes it more difficult for the attacker to determine which accounts are privileged. This will slow down a skilled attacker, but will also defeat most automated tools and techniques used by script kiddies.

## Name servers securely

A name can say too much. Servers should be named in a way that does not give any information about them or their purpose. For example, people tend to name database servers db1, db2, and so on. Hostnames such as these advertise to a potential attacker a server's primary service or purpose, which leads to a search for the latest database vulnerabilities and exploits for that system. A server named "test" tells an attacker this could be an unsecured server, a server that is not likely to be monitored, a server with default accounts, a server that may be in a lab and not used every day, or a server that could be used as a stepping stone to other servers. The same goes for names such as lab, dev, and temp. It's also not a good idea to name servers after the departments that use them, such as HR, Payroll, Research, and so on. This gives an attacker an idea of goods these servers contain. It is best to pick an interesting naming scheme that's easy to remember and understand — and then stick to it.

# Summary

This chapter covered the core things an organization needs to focus on. Its goal is to increase your awareness of the threats that exist and to show you what can be done to protect against them. When it comes to network security and protecting your site, ignorance is deadly and knowledge is power. You should now have the knowledge to secure your company's assets and resources. Understanding what a company is up against is the only way to defend its network and systems from attackers.
