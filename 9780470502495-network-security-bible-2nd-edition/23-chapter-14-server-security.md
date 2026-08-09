# Chapter 14. Server Security

**IN THIS CHAPTER**

- **Introducing general server risks**
- **Designing for security**
- **Operating servers safely**
- **Exploring server applications**

In a simplistic view, network security can be grouped into three categories: the user workstation, the network devices, and the servers. The user workstation is important to secure because it potentially holds all the information to which a particular user may have access. Additionally, if the workstation is compromised, its attacker can (usually) do everything that a user would be authorized to do. Network devices allow users to interact with other users and servers. Network devices are often targeted because they are usually configured more for performance than security. The third category, servers, has its own reasons for being a security target, which are explored in this chapter. In should be noted that in this chapter MAC stands for mandatory access control.

# General Server Risks

In the past, most of the attacks on networks have been focused on servers. Network servers are prime targets for the following reasons:

- **They hold large volumes of critical data**. In the same way that banks are robbed because "that's where the money is," hackers are very interested in servers and the data that they hold.
- **If compromised, a server may provide the attacker access to many workstations**. Most setups are such that the server is trusted and the workstation must authenticate to the server. This may leave the workstation vulnerable to attack if the server has been compromised.
- **Servers often are easy to find**. Most setups are such that the workstation easily finds the server and uses authentication to restrict access. Attackers are likely to attack servers they can reach, as opposed to workstations that they cannot.
- **Server applications, on average, are more costly and difficult to develop**. In many cases, developers will reduce the cost and risk of this development by using common software packages such as Microsoft IIS Web server. When common software is used, attackers are able to focus their efforts on a piece of software that they know very well.

# Security by Design

In the past, security for server applications has been an afterthought, only to be considered after threats and vulnerabilities have arisen. This led to many instances of security being retrofitted into an operating system or application. One of the lessons learned from retrofitting is that it is very costly and time consuming to try to put in security after an application and system have been developed and deployed. In most cases, the system cannot be made completely secure.

A conservative estimate is that it's 10 times cheaper to build security into a product than to attempt to retrofit it after deployment. If the cost benefit is so great, why then does security still have a difficult time being part of the requirements in most software development efforts? Some of the factors affecting security in the design phase of a development effort are as follows:

- The software developers and security professionals (network engineers) historically came from different communities. This is still an issue today, although more software developers are attending security training and security conferences.
- The security threat was not well publicized. Security has made the front page more often in recent years. However the items that are being publicized are not the real issues that organizations need to focus on.
- In many cases, the software developer is working on a topic that the developer has never coded before. However, a network engineer who designs a network has probably designed dozens of networks in the past.
- Until recently, software developers could not justify time spent on security features because they did not seem to affect the bottom line from management's perspective.
- In the highly competitive marketplace for software, there has been a natural rush-to-market approach to beat the competition.

Even with the heightened attention to security in today's world, it is still an uphill battle to get security rooted into the initial requirements and design of a development effort. Several steps can be taken to improve the security in server applications under development, including the following:

- Maintain a security mindset in the organization and in the development group.
- Establish a secure development environment and train developers on secure coding techniques.
- Use secure development practices.
- Test frequently and at all levels.

## Maintain a security mindset

Having a security mindset is the first step in developing a secure product or having a secure environment. Security improvements will come at a cost of time, money, and convenience. If an organization does not have a mindset that values security, it will be difficult to implement the needed controls. Following are some approaches to improving the security during the software design and development process:

- **Base security decisions on the risk**. Security can be like insurance; the risk must be known to determine the coverage needed.
- **Use defense in depth**. Having numerous security controls is preferable to a single point of protection.
- **Keep things simple**. Simplicity and clarity will support a more secure product.
- **Respect the adversary**. Do not underestimate the interest and determination of the attacker.
- **Work on security awareness**. Security training is needed at all levels of an organization.
- **Use encryption**. Be paranoid and expect the worst.

### Risk-based security controls

Management is often confronted with issues such as "What actions should I take to improve security? How much should we spend on securing this product?" These are common questions every project manager asks when considering security. How to address security is confounded by a number of confusing and ironic aspects of the problem, including the following:

- The technologies involved are very high-tech and not fully understood by most in management.
- The threat is usually discussed in terms that don't readily translate to dollars.
- The greatest threat is from the inside; but the corporate culture has learned to trust and rely on only those within the organization.
- The items at risk are not physical and perhaps less tangible—information, reputation, and uptime.
- People have been shouting "the sky is falling" for a while and nothing serious has happened, yet.
- There are many solution providers offering security products and services. For the most part, they only provide a partial solution.
- Spending is not predictive of the security received. A $30 modem can bypass the security of a $200,000 firewall installation.

The risk to a server application should be based on the likelihood of an attack to occur and business impact if it does occur. The business impact is best determined by informed stakeholders. Some examples of the stakeholders may be the organization that developed the server application, the organization hosting the service, and the users of the service.

### Defense in depth

The defense-in-depth principle is best thought of as a series of protective measures that, taken as a whole, will secure the product. The most memorable example is the medieval castle. The king protected his crown jewels (literally) with a series of progressive defenses, including the following:

- The chosen site for the castle was on a hilltop. It was and always will be easier to defend the top of a hill.
- Stone walls and terraces were placed around the approaches to the top of the hill.
- Sharp sticks pointing toward an approaching attacker were placed on the hillside. In today's world, these would be mine fields.
- A moat was dug around the hilltop.
- Vile waste was placed in the moat, sure to discourage the fainthearted from crossing.
- The outer castle walls were tall and thick.
- Rocks and hot oil could be dropped from the outer walls, slowing down the attack.
- There was an inner, smaller fortress to which the population could retreat in the event the outer walls were breached.

No single defense of a castle was relied upon for the ultimate protection. The defenses as a whole were designed to weaken and discourage the attackers. Some defenses were easy and cheap to implement (sharp sticks). Others required significant resources (the outer walls). But taken as a whole, the defense was much stronger than the simple sum of each protective feature.

The defense-in-depth principle applies to software development and server applications as well. Two important features to note are as follows:

- All the security resources should not be concentrated on a single protection. The classic case of this is when a company spends its entire security budget on a $200,000 firewall to protect it from the Internet. All of this investment can then be circumvented by a $30 modem because there was no security awareness program to train users as to the risk of connecting to ISPs directly from their workstations.
- A protective measure (a security control) is worth implementing even if it seems to be a redundant protection. For example, the use of strong passwords is advised even on internal networks in which all users are trusted.

### Keep it simple (and secure)

Complexity, confusion, and uncertainty aid the attacker in exploiting a system or an application. If an application is clear and transparent in its operation, it is more easily secured. The more open the application is to its operations, the more readily security flaws will be seen and corrected. While a transparent development process does not guarantee a good design, a closed process can hide a bad design. It is through bad designs that the most costly security issues arise. If a bad design is not caught early, it may not be correctable from a security perspective.

The designers of a server application are not necessarily the developers and are usually not the operators and maintainers of the service. Clear and concise documentation with respect to security requirements and assumptions are important when an application is handed from one group to another. If the design's security is predicated on a certain feature (such as 128-bit encryption), this information must be passed along for the life of the server application.

In a very complex server application, different components will have different responsibilities with respect to the security of the system. For example, one component may authenticate users, while another determines what access a user can have to the database data. The logical interfaces between these components are sometimes referred to as *trust boundaries*. Software designers should easily be able to draw out the trust boundaries between all the components of the application or system. If this is a difficult task, perhaps the design is not as simple and therefore not as secure as it might be.

### Respect the adversary

Software developers are experts at making an application perform as it was designed to perform. Hackers are experts at making server applications do things they were never designed to do.

Designers should plan for the unexpected. Attackers will throw everything they can imagine at the server application trying to invoke an unintended response. Attackers do not play by the rules, and developers should not expect that they will. Designers should clearly state what the expected normal user interaction should be. These interactions should then be screened for abnormal use of the application. In this way, tests and reviews can consider what bizarre treatment the application might receive at the hands of an attacker.

All applications and hardware fail eventually. When they do, they should fail in as safe a manner as can be predicted. Attackers will seek to crash systems to circumvent security controls. Many serious exploits begin with a service being overloaded and crashing. The attacker then moves on to compromise the system. If fail-safe requirements are stated early in the design process, there is a better chance of the design withstanding these attacks.

### Security awareness

A key ingredient to maintaining a security mindset is a strong security awareness program. Security awareness involves educating developers and network engineers about the security risks involved in a development effort. Following are some key lessons to be covered in an awareness program:

- **Security policies and the roles and responsibilities when developing applications**—Management should ensure that there are formal roles and responsibilities for developers regarding security-related items. The policy itself offers limited protection. If developed in an open and collaborative process, the big benefit is the security awareness gained.
- **Product-specific requirements**—A number of domains have external requirements that must be met by a product operating in that domain. For example, financial institutions are responsible for the Gramm-Leach-Bliley Act (GLBA) requirements, and certain credit card companies may impose requirements, such as the Visa Cardholder Information Security Program (CISP) 12-point program. The GLBA, which is also known as the Financial Services Modernization Act of 1999, provides limited privacy protections against the sale of your private financial information. Additionally, the GLBA codifies protections against *pretexting*, the practice of obtaining personal information through false pretenses. The Visa CISP is a 12-point program designed to assist anyone who processes credit cards, where the customer is not present, to secure the credit card information. These top-level principles apply to all entities participating in the Visa payment system that process or store cardholder information and have access to it through the Internet or mail-order or telephone-order. The following requirements are provided by Visa:Install and maintain a working network firewall to protect data accessible via the Internet.Keep security patches up to date.Encrypt stored data.Encrypt data sent across networks.Use and regularly update antivirus software.Restrict access to data by business on a need-to-know basis.Assign a unique ID to each person with computer access to data.Don't use vendor-supplied defaults for system passwords and other security parameters.Track access to data by unique ID.Regularly test security systems and processes.Maintain a policy that addresses information security for employees and contractors.Restrict physical access to cardholder information.
- **Security basics**—This includes passwords, physical security, security policies, roles, and responsibilities.
- **Security awareness testing**—It is very important to test the basic training. Testing provides insight into risk areas and the need for future training.

### Business impact

The impetus and justification for setting up the environment should be to minimize the security risk and reduce the business impact of any attacks. Risk and business impact are covered in detail in [Chapters 1](ch01.html), [2](ch02.html), [7](ch07.html), and [18](ch18.html). Business impact in this case is considered to be the loss avoided, due to the investment. This is the business impact of the risk that is mitigated by the security controls or measures taken to improve security. Some typical business impacts to be considered are as follows:

- If significant credit card information is lost, the business impact will be hundreds of man-hours.
- If a security incident leads to an extensive internal investigation, the business impact will be dozens of man-hours.
- Damage to customer relations can result in a loss of future business.
- An organization's public image may be damaged.
- There will be legal costs to investigate and defend a loss.

Because an organization should base its environment on its own specific risks and needs, the recommendations put forth here should be considered a starting point or general practices.

When considering the threat, developers should keep in mind that the internal LANs and WANs can reach the far corners of an organization. The project manager has a certain amount of insight into the means, access, and motives of his developers, and he may also be informed about other personnel in his location. However, when it comes to employees on the WAN, he has to blindly trust that they will not attack his servers.

The business impact if an attack is successful is a judgment call that only each organization is qualified to make. By way of example, consider the following thought process for the fictitious Acme Publishing company. A vulnerability to mail viruses exists. The threat of a virus hitting Acme's mail servers is high in the next year. The vulnerability and threat combine to give a 5 percent likelihood of getting hit with a virus and losing a day's e-mail. The business impact on Acme from losing e-mail is $50,000 per day. Only Acme can determine that this is the cost or impact. Therefore, it is worth (0.05 × 50,000 = 2,500) $2,500 to install a virus protection defense. In this example, the security risk for this vulnerability/threat/impact combination is $2,500 annually.

Note that the business impact must include the cost of embarrassment and the loss of good will. Some vulnerabilities have a business impact that is just too high to accept at any threat level. Such a vulnerability, for example, is the mishandling of credit card numbers. An attack resulting in a loss of credit card numbers would have a crippling impact on business. Consider the impact of the loss of credit card information in California, alone, which is leading the nation in new, tougher privacy laws concerning the disclosure of sensitive data such as credit cards.

## Establishing a secure development environment

Having a security-oriented mindset is not sufficient for developing secure server applications. An organization must also establish and maintain a development environment that promotes security. The development environment should address the risk and business impact and cover the following areas:

- Management
- Security awareness
- Software development
- Configuration control
- Network security

### Management

Secure software cannot be developed without significant management support. Management must value the time and effort put into making a product secure. This value should be based on the reduction of the business impact that can result from a poorly developed product. Management should provide the time and resources to support a secure product development. Additionally, management should establish a security officer and a configuration control process.

Developing a secure product is more costly in the short run. Security requires more design and expertise at the beginning of the software development effort. It takes strong and insightful management to see this need and to provide the resources and guidance to incorporate security early on in the development process. As discussed earlier, the total cost of developing a secure product is reduced when security is designed into the effort from the beginning. Also, a case can be made that the total cost of a secure product is less than a nonsecure product when the business impact (translated into dollars) is taken into account.

A security officer is key to having a central point of contact for security across all projects and development efforts. A security officer can provide checks and balances for the development leadership, which is often more concerned about performance and keeping to budgets and schedules. The security officer can be the go-to guy when a developer or operator has a security concern or if a security incident arises. The security officer would then be able to escalate the issue to the proper level for its business impact analysis. The security officer should not have authority over the development process but rather act a sounding board and conscience.

### Configuration Control Board

Management should establish a configuration control process that supports the developers in design and development of complex applications. Generally, this process is centered on a Configuration Control Board (CCB). The CCB can be responsible for the following:

- **Establishment of formal change management in development**—Random or uncontrolled changes should be viewed as openings for security vulnerabilities. It is rare that an unforeseen configuration change will make an application more secure. All the effort put into making a secure design can be undercut by not controlling the changes that are inevitable during a development process. The annals of security blunders are full of examples of how previously patched vulnerabilities are reintroduced into a product with a subsequent patch or upgrade.
- **Establishment of formal requirements and testing program**—Over time or during development, an application may be diverted from the original security requirements set down for the application. It is not uncommon for the design document to have requirements that are not fulfilled because they were not goals of acceptance testing and regression testing.
- **Coordination of developers, deployment, and networking responsibilities**—The CCB monitors the progress of development and deployment, with an eye to security needs. The board coordinates the actions required in response to high-level changes in the product, platform, or network. The members of the CCB use the information provided by other members of the board to plan their own security activities. The CCB should be chaired by the security officer. The membership includes representatives from the developers, the project delivery groups, and the network administrators. [Figure 14-1](ch14.html#the_ccb_coordinates_and_informs_on_secur) illustrates the coordination that the CCB provides.

### Network support for development

Generally speaking, software developers and network engineers have different backgrounds and career paths. As a result, neither camp fully appreciates or understands what the other does. In many organizations, this leads to a throw-it-over-the-wall attitude in which software is designed, developed, and tested in a development environment and then given to network engineers and deployment personnel to be placed in an operation setting. This can result in a misunderstanding as to what the security requirements are for a given server application.

Following are some ways in which the network engineers and developers can work more closely together to maximize the products security:

- **Establishment of a test environment**—Most testing is currently done on either development systems or archived copies of deployed systems. Network administrators and developers need more flexibility to make configurations and changes.
- **Establishment of formal change management for the development and operational networks**—If the networks associated with the server application are not securely maintained, there is a risk that a logic bomb or malicious code (virus, and so on) could be inserted into the application. Software developers generally are not network engineers and may not be able to recognize whether a supporting network is secure or not. Network engineers may not appreciate the risk to the software under development when configuring the network. A body overseeing both the network and the development effort, such as the CCB, can be effective in securing the network environment, as needed.![The CCB coordinates and informs on security issues.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1401.png)**Figure 14.1. The CCB coordinates and informs on security issues.**
- **Establishment of a program for continuous network assessment**—Critical software development networks should require a high level of network security. Often, a development network is well inside an organization and away from the Internet. In many organizations, this would lead to an increased trust of users on the network and less monitoring for suspicious activity. A configuration control program or CCB should require that network engineers apply a high level of scrutiny on the development networks and aggressively pursue any discrepancies. In most cases, this involves continuous monitoring with intrusion detection systems (IDS) and periodic security scans.
- **Use of a firewall or establishment of a VLAN for developers**—Developers should be exposed to a firewall, or functionally grouped in a virtual local area network (VLAN) to prevent nondevelopment personnel without a need to know from getting access to development workstations and servers. (If not already implemented, this should be done for other sensitive groups, such as Human Resources and Finance, as well.)

## Secure development practices

There are many methods for developing code. Any of them can be used to develop a secure application. Every development model must have both requirements and testing. In some models the requirements may emerge over time. It is very important that security requirements be laid down early in the development process.

Security in an application tends to be subtle and invisible. Security is prominent only two times in the development life cycle: requirements definition and testing. At other times, deadlines, capabilities, performance, the look and feel, and dozens of other issues tend to push security to the back. This is why it is important to be sure that security requirements are prominent at the beginning of the development life cycle.

In many respects, the tools and techniques used to design and develop clean, efficient applications will support the development of secure code, as well. Some special interest, however, should be taken in the following areas:

- **Handling of data**—Some data is more sensitive and requires special handling.
- **Keeping the code clean**—Care must be taken not to expose too much information to a would-be attacker.
- **Choosing a coding language**—Consider the strengths and weakness of the language used.
- **Avoiding content injection**—Data (content) entered by a user should never be able to be put directly into a command or query.

### Handling data

As the Internet continues to be a driving force in most of our everyday lives, more and more personal and sensitive information will be put on servers. Requirements for handling this private information did not exist five years ago, while other data, such as passwords, has always required special handling. Following are some special cases for the handling of sensitive or critical data:

- Passwords should never be transmitted in the clear. They should always be encrypted.
- Passwords should never be viewable on the user's screen as they are entered into the computer. Even though asterisks (*) are being displayed, care must be taken to make sure that it is not just because the font is all asterisks. If that is the case, someone could steal the password by copying and pasting the password from the screen.
- If possible, passwords should always be encrypted with one-way hashes. This will ensure that no one (not even a system administrator) can extract the password from the server. The only way to break the password would be through brute force cracking. With one-way hashing, the actual passwords are not compared to authenticate the user; rather the hashed value is stored on the server and is compared with the hashed value sent by the user. If the passwords cannot be decrypted, the user cannot be provided their passwords when they forget them. In such cases, the system administrator must enter a new password for the user, which the user can change upon re-entering the application.
- Credit card and other financial information should never be sent in the clear.
- Servers should minimize the transmissions and printing of credit card information. This includes all reports that may be used for internal use, such as troubleshooting, status, and progress reports.
- Sensitive data should not be passed to the server as part of the query string, such as in the following. The query string may be recorded in logs and accessed by persons not authorized to see the credit card information. For example:http://www.server-site.com/process_card.asp?cardnumber=1234567890123456

### Keeping code clean

When it comes to information put into server code, a good motto might be, "Be paranoid. Don't disclose any more than necessary." Attackers will spend countless hours gathering information looking for the nugget that will make their task easier. Much of that time will be spent examining HTML and scripts for information that can be used to make their attack easier.

Comments should be stripped from operational code. Names and other personal information, in particular, should be avoided. HTML comment fields should not reveal exploitable information about the developers or the organization. Comments are not bad per se, but those embedded in the HTML or client script and which may contain private information can be very dangerous in the hands of an attacker.

Many times third-party software packages, such as Web servers and FTP servers, will provide banners that indicate the version of the software that is running. Attackers can use this information to narrow their search of exploits to apply to these targets. In most cases, these banners can be suppressed or altered.

### Choosing the language

One of the most frequently discovered vulnerabilities in server applications is a direct result of the use of C and C++. The C language is unable to detect and prevent improper memory allocation, which can result in a buffer overflow.

Because the C language cannot prevent buffer overflows, it is left to the programmer to implement safe programming techniques. Good coding practices will check for boundary limits and make sure that the function was properly called. This requires a great deal of discipline from the programmer and, in practice, even the most experienced developers can overlook these checks occasionally.

One of the reasons Java is so popular is because of its intrinsic security mechanisms. Malicious language constructs should not be possible in Java. The Java Virtual Machine (JVM) is responsible for stopping buffer overflows, the use of un-initialized variables, and the use of invalid opcodes.

### Input validation and content injection

All input from the user that cannot be trusted must be verified and validated. If the system is to process data that has been provided by an untrusted entity, the data must be validated first. In most client-server interactions, it is difficult for the server to validate the client, so the client should be considered untrusted.

Content injection occurs when the server takes input from the user (client) and applies the content of that input into commands or SQL statements. Essentially, the user's input gets injected into the command that is executed by the server. Content injection can occur when the server does not have a clear distinction and separation between the data input and the commands executed.

There is a fundamental paradigm difference between the developer and the attacker that must be considered when designing Web-based applications. The developer assumes that the user's goals and that of the application are the same. This tends to lull the developer into expecting the user to provide the correct input for the task at hand. The developer may expect errors in the input, but generally he or she expects the user might make honest mistakes. The attacker, on the other hand, looks to use input as a key method of disrupting and disturbing the application. The attacker knows that little is to be gained by proceeding through the application as the developers expect.

As a result, it is essential that developers test all inputs carefully. The checks should assume nothing at the offset. Inputs should be checked for proper characters and proper length. If special characters are allowed in the input, extra care should be taken. Special characters can often have uses in a shell context that are unknown to developers. For example, in a UNIX shell, a dot (.) is the equivalent to "execute the following in this shell." And back ticks (') around a statement are equivalent to "execute this statement in a new (sub) shell."

#### Cross-site scripting

All the dynamic Web applications on the Internet depend on being able to differentiate between two users hitting the same Web site. Maintaining state like this is normally done using some kind of cookie. Cookies are small pieces of data stored on the client machine and returned with each request to a particular Web site. Cookies can be used to remember a user between visits or to prevent a user from having to log in repeatedly to the same Web application.

One of the security considerations of cookies is that they are supposed to be returned only to the site that issued them. This is important so that a banking cookie isn't sent when visiting a news site and vice versa. But there is a vulnerability that allows rogue scripts to trick a client browser into submitting cookies to a third party. One of the exploits using this vulnerability is cross-site scripting.

Cross-site scripting gets its name from the capability of a script to call up a completely different Web site and, in the process, capture the cookies and information exchanged between the user and that site.

The cross-site scripts are typically embedded in Web pages or sent via e-mail. Users may not even have to click on anything if they access a Web page with compromised code on it. Server applications should not interpret (open links and load Web pages) unless the source of the HTML can be assured to be safe.

#### SQL injection

SQL injection is the practice of manipulating a database to perform actions that it was not intended to by adding SQL commands to the Web application and having them execute against the database. This is not only a problem for username and password screens, but anywhere the user has interaction with the database. Consider the following script from a server application:

```
sql = "select username from users
  where userid  = ' " & request("userid")   & " '
    and password = ' " & request("password") & " '  "
```

This code produces a SQL select command to query the database to check a username and password. The code gets a username and password from the user. The request functions provide the user's input. The SQL command is built by putting double quotes (") and single quotes (') around the user's input. If the SQL command is successful, the username/password combination was found in the database and the user is authenticated.

The preceding SQL select code looks simple and straightforward. However, the SQL injection problem arises if the user enters nothing for the password and the following in response to the prompt for a username:

```
any_bogus_name' or 1=1 --
```

The resulting SQL query executed on the database is as follows:

```
select username from users where
   userid='any_bogus_name' or 1=1 -- 'and password = ''
```

As you can see, the bogus username was inserted into the query, however, the select command will still be successful (authenticating the user) because the username lookup will be '`or'ed with 1=1` (which is always true). The double dashes (--) comment out the remainder of the select statement, thus rendering the password input useless.

#### Stored procedures

In today's environment, a common security breach occurs when an external or internal user gains access to the network and begins monitoring traffic between the application and the database. This approach can help a hacker learn where key data, such as passwords, are stored. To mitigate this, the application server should not use any direct Structured Query Language (SQL). Instead, when modifications, additions, or deletions of database information are needed, a stored procedure should be used to perform the function. The SQL statements will not have any rights to access data in the tables; only stored procedures will be able to access data. Someone hacking the system could do a SELECT and pull back all of a table's data if SQL were allowed. However, because stored procedures allow data to be retrieved only in the built-in amount, format, and rules, the system would limit the amount of data a hacker could retrieve.

#### Dynamic scripting

Dynamically executing scripts based on user inputs can be very risky. The onus is put on the developer to check and guard against every possible input that is not expected. Recall the paradigm discussion earlier—the attacker is probably more practiced and creative about thinking up abnormal input. Additionally, the attacker, in many cases, has a lot more time to devote to this one task than does the developer. If possible, dynamic scripting should be disabled at the database level or at the Java environment level. A module developer should not even have the option of using dynamic scripting.

#### Screen for all unusual input

An attacker will do something you don't expect—count on it. It is easier for a developer to know what the normal action or response to a Web page is than to predict every unusual one. Software developers need to test user input aggressively for normal responses and block everything else. The challenge is to be able to capture normal input in a set of rules that does not give the attacker enough room to abuse the server.

The testing of input from the user must include that absence of expected responses. For example, a POST command sent without POST data may not return from the server. It may or may not be using up server resources. If the TCP connection remains open, there is potential for a denial-of-service (DoS) attack. A common method of DoS attacks is to initiate hundreds of connections that don't fully complete. The server must keep the half-open connections in memory because the algorithms expect the connection to either be completed or to be reset. When the available memory for new connections fills up, no one else can connect to the server. In some cases, when the memory fills up, the server crashes.

### Use encryption

Encryption can go a long way toward maintaining the confidentiality of the data in any application. The price for encryption is performance or the cost of additional hardware or software. Additional hardware may be needed to increase the bandwidth and improve the application's performance. The use of encryption is a security control multiplier; it enhances any security posture. Encryption can be used in storage, transmission, or data verification.

Using encryption for data storage adds another defense to the defense-in-depth model for a given server application. Data stored encrypted in the database or on the hard drive is protected against a breakdown in physical security, such as a server host being stolen or lost. Encrypted data storage also protects against an attack in which the server's host is compromised and the attacker attempts to access the data directly from the operating system.

Encryption should be used for transmissions any time sensitive or private data is involved. This would include information such as the following:

- Names, addresses, and phone numbers
- Credit card numbers, bank account numbers, and Personal Identification Numbers (PINs)
- Financial data such as reports, balances, and transactions
- Salary information
- Personal information such as shopping carts and wish lists

The two most common means of encrypting during transmission are using Secure Sockets Layer (SSL) and a Virtual Private Network (VPN). SSL encrypts the application's traffic. SSL-compatible clients, such as a Web browser, are readily available, so there is no practical impedance to its use. Using a VPN is a general solution to encryption in which all the network traffic is encrypted and tunneled. Because both ends of the VPN must be compatible and coordinated, it is not a solution for the general public, but rather for a small set of users, such as employees working from home.

Encryption can also be used to verify the integrity of data being transmitted. Consider, for example, the following data that is passed in a cookie from a Web server to a Web browser.

```
SessionID=9si82kjskjwiue092
ValidUser=Y
UserID=JohnDoe
```

If this information were encrypted, it might read as follows:

```
SessionData=ks92ieiufjmkw74ujrjfkkshsdyyuisklfjghsyy3kekksyywksllbns29js
```

This would protect the identity of John Doe in the first cookie. Because the cookie was encrypted by the server, only the server has the key to decrypt the cookie when it is returned from the Web browser.

The cookie's integrity could also be maintained by adding a hash field to the information in the cookie. A hash algorithm can take the data from the original cookie and pass it through a one-way encryption process that produces a short string. Any change in the original cookie would result in a different hash, therefore, the integrity of the cookie data can be verified. After running the original cookie through a hash function, the cookie is now as follows:

```
SessionID=9si82kjskjwiue092
ValidUser=Y
UserID=JohnDoe
Hash=2o29e7jhtw5uedkfhgf73
```

Now, if any of the fields in the cookie are altered, the server will know because the cookie sent back to the server will not hash out to the same value as that stored in the cookie.

The use of encryption and hashing to ensure the privacy and integrity of the information in the cookie adds very little overhead to the overall server application, while providing additional defense in depth.

Web-based applications may be subject to hijacking, replay, and man-in-the-middle attacks. These attacks can lead to a Web session being overtaken by a third party (hijacking) or a transaction being replayed. Using SSL will prevent hijacking and replay attacks under most circumstances.

Encryption can provide an extra measure of security in addition to all the other security controls implemented. The SSL protocol runs above TCP/IP and below higher-level protocols such as HTTP or IMAP. It uses TCP/IP on behalf of the higher-level protocols and in the process allows an SSL-enabled server to authenticate itself to an SSL-enabled client, allows the client to authenticate itself to the server, and allows both machines to establish an encrypted connection. In general, SSL can be added to an application with little impact on the developers.

The negative impact that SSL can have is on performance and cost. The following is from an SSL FAQ:

> How will SSL affect my machine's performance?
> 
> *The performance problems associated with most HTTP servers are CPU and memory related (this contradicts the common assumption that it is always the network which is the problem). The CPU has to process the HTTP request, write out HTTP headers, log the request and put it all on the TCP stack. Memory bandwidth is also a problem (the operating system has to make a lot of copies to put packets onto the network). SSL makes this bottleneck more severe:*
> 
> - Bandwidth: *SSL adds on average 1K bytes to each transaction. This is not noticeable in the case of large file transfers*.
> - Latency: *SSL with client authentication requires two round trips between the server and the client before the HTTP session can begin. This typically means at least a 500ms addition to the HTTP service time*.
> - Bulk encryption: *SSL was designed to have RC4 and MD5 in its cipher suite. These run very efficiently on a 32-bit processor*.
> - Key exchange: *This is where most of the CPU bottleneck on SSL servers occurs. SSL has been optimized to require a minimum amount of RSA operations to set up a secure session. Avoid temporary RSA keys, which can cause a massive performance hit*.

Netscape has published figures suggesting that the throughput (in hits per second) of an SSL-enabled server is as low as 20 percent of that of an unencrypted server. The greatest performance hit occurs when the server and client exchange handshake messages for authentication and key generation or exchange. These operations are performing computationally intensive public key operations. Subsequent hits use the session restart feature of SSL. This allows the server and client to simply use the previously negotiated secret key.

## Test, test, test

A secure design is very important, but no application ends up exactly as designed. It is the very nature of security flaws that they are likely to take advantage of any deviation from the design. Testing is important to both find deviations from design and to detect any unforeseen flaws that might have been introduced during the development process. Testing is also one of the best ways to provide feedback to designers and planners to improve future requirements. Glaring security concerns that are noticed at testing stand a good chance of being put into future requirements.

Having a 100 percent secure application is a nearly impossible task. Security flaws will be introduced in any development process that is creative and flexible. However, good requirements and testing can minimize the security risk introduced into a creative development process.

![Testing V](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1402.png)

**Figure 14.2. Testing V**

You should begin security testing on a new application while it is still on paper. Paper attempts to break the application will surely lead to issues to be addressed. Later rounds of testing should include source code analyzers to ensure that logical errors are not included in the code. These analyzers can perform pattern matching to identify functions or constructs that are potentially flawed. Finally, after being fully developed, testers should use network sniffers and application-level scanners to verify the operation of the application. The sniffers will allow the testers to examine the low-level packets emanating from the server, looking for flaws such as transmitting passwords in the clear. The scanners will test the server's boundaries and see if it can be coaxed into an unexpected behavior.

There are many ways to visualize requirements testing. [Figure 14-2](ch14.html#testing_v) shows the Testing V used by the Department of Defense (DoD). While this is a complicated figure, it conveys the following principles:

- Tests should be directly based on the requirements at the same level—high-level tests for high-level requirements.
- Tests should be written when the requirement is written, but not tested until the application has been developed to that level.
- Requirements should start at a high level and be refined over time.
- Requirements should be completely refined before coding.
- As coding is completed and increasing levels of requirements are satisfied, it should be tested.
- The final testing will be a high-level user acceptance testing.

# Operating Servers Safely

Even the most securely developed server application must be placed in a secure operational environment. To operate the server securely, an organization must establish a plan with associated procedures. These procedures should include the following key aspects:

- **Control the server configuration**. The server must be configured to minimize exposure to an attack. Periodic backups can mitigate the risk if an attack does occur.
- **Control users and access**. A need-to-know and need-to-access environment should be established regarding the server's data and access.
- **Monitoring, auditing, and logging**. Security does not stop with deployment of the server. In today's environment, continuous monitoring is required to ensure a server remains safe.

## Controlling the server configuration

Operating the server safely extends beyond the key application being served up. The host platform must also be secured. Three important considerations when securing the host system are as follows:

- Physically secure the system.
- Minimize the risk to the host system by removing unneeded services.
- Back up the host system to mitigate the risk in the event that an attack does occur.

### Physical security of the system

Any server is vulnerable to an attacker with unlimited time and physical access to the server. Additionally, physical problems could cause the server to have downtime. This would be a loss of availability, which is considered one of the key principles of security—to maintain confidentiality, integrity, and availability (CIA). The following should be provided to ensure the availability of the server:

- Provide an uninterruptible power supply (UPS) unit with surge protection.
- Provide fire protection to minimize the loss of personnel and equipment.
- Provide adequate cooling and ventilation.
- Provide adequate lighting and workspace for maintaining and upgrading the system.
- Restrict physical access to the server. Unauthorized persons should not get near the server. Even casual contact can lead to outages. The server space should be locked and alarmed. Any access to the space should be recorded for later evaluation should a problem occur. Inventory should be tightly controlled and monitored.
- The physical protections listed here should extend to the network cables and other devices (such as routers) that are critical to the server operation.

### Minimizing services

As discussed earlier, servers are natural targets for attack. It should be expected that attackers will seek the path of least resistance in an attempt to compromise the server. The attacker will look to break in through any of the services running on the server. For this reason, separation of services is a good security practice.

Separation of services dictates that each major service should be run on its own protected host. If any one service or server is compromised, the others are unaffected. In this way, the damage done is limited to the one server. This mitigates the risk to all the servers.

Most server operating systems will have a number of services enabled or on by default. Care must be taken to ensure that these extraneous services are disabled or even deleted from the system. The following list shows typical services that should be disabled from a host if not needed:

- **Telnet**—This service transmits data in the clear and should not be used under any circumstances. The secure alternative, Secure Shell (SSH), should be used instead, if needed.
- **Simple Mail Transfer Protocol (SMTP)**—Mail server applications are frequent targets of attacks and, as a result, the software requires frequent upgrades and updates.
- **File Transfer Protocol (FTP)**—FTP has a number of vulnerabilities and must be properly configured to be safe.
- **Finger**—Finger can be used to learn information about a computer system that can then be used to launch other attacks.
- **Netstat, Systat**—These services can disclose configuration and usage information.
- **Chargen, Echo**—These services can be used to launch data-driven attacks and denial-of-service (DoS) attacks.
- **Domain Name System (DNS)**—This service requires frequent patches and upgrades to be secure.
- **Remote Procedure Calls (RPC)**—Unless the server application explicitly uses RPC to communicate with other systems, this should be disabled.

### System backups

System backups are an important security control to mitigate the risk and damage that can be inflicted by an attack. No matter what steps are taken to prevent an attack, they should still be expected. Therefore, every server and server application should have backups as part of the normal operation of the server.

The frequency of the backup should be determined by the critical nature of the data or service. The determination should be made based on a risk and business impact analysis. Typically, data is backed up on a daily or weekly basis. If the loss of a day's worth of data cannot be tolerated, a zero-down time failover system is usually called for.

Backups can aid in a post-attack reconstruction. The compromised system can be compared with the backup to determine which part of the system was attacked. This may also provide insight into the extent of the damage inflicted by the attacker.

## Controlling users and access

The operating systems and hosts that run server software are general computing devices. These devices are designed for multiple users running multiple applications. To take a general computing device and make it secure for a particular service, the system administrator must establish a need-to-know environment. Data access should be limited on a need-to-know basis and users should be limited on a need-to-access basis. The basic principle of least privilege is that no user (or developer) should have any more access and control than is needed to perform that person's functions.

User activity on a server is typically grouped into sessions. Cookies are often used to identify users and maintain session objects. These objects hold information to keep track of user-specific information while a user navigates the site, without asking for them to identify themselves at every request from the server. Servers should employ a session timeout feature that will log off users due to inactivity. The user will then be required to re-authenticate to continue using the service.

The session tracking information should also be used to ensure that a user only starts one session at a time. During each logon attempt the server should determine if a session is active. If an active session is detected, further access to the application is denied.

The server should require special access to update and maintain sensitive information. Some system functions and operations may be exceptionally sensitive and require special authorization and annotation. Authorize the transaction by entering the user's username and password. Each adjustment must be accompanied by an explanation in the comment field.

## Passwords

Strong passwords should be required on the servers. Following are guidelines for strong password criteria:

- The password length should be a minimum of seven characters. The longer the password the more difficult it is to break it using brute force.
- The passwords should contain some nonalphanumeric characters such as ~!#$% ^ &*()_-><.?/|\. By increasing the alphabet that can be used in a password, the time required to use brute force or crack the password is dramatically increased.
- Dates, names, common words, and reversed names cannot be used.
- The password should expire in 45 to 90 days. At that time the user will be required to enter a new password.
- Passwords for any given user cannot be re-used until five password changes have occurred. Users should not be permitted to make five rapid changes of their passwords just to get back to a favorite one. The password list will also check for a number appended to the end of the previous passwords to keep users from trying to trick the system.

Passwords should be stored as encrypted data in the system. In the event of a user forgetting a password, the system administrator should not give it out. Instead, the system administrator should assign the user a temporary password. The user can then log back onto the system and immediately change the password.

Users should be allowed three tries to input the correct username and password. If the username and password combination is still incorrect after the third try, the system should lock the account. The user should then be required to contact the system administrator to unlock the account.

## Monitoring, auditing, and logging

Monitoring, auditing, and logging are critical to detecting attacks on servers and responding quickly. Logging is the act of recording key information about the server and service. The logs can be generated both by the operating system (event logs) and the application. Logs can be useful in reconstructing an attack or incident. However, the greatest benefit of logs is their use when monitoring the server.

Monitoring is the periodic review of the logs and other server information. Monitoring is typically done continuously, hourly, or daily. Continuous monitoring is usually done by a help desk, with watch standers having scrolling logs and other status information at their stations. The watch stander is likely to spot patterns and problems in the logs that a computer might not see. Regular monitoring identifies points of exposure and incidents of policy and procedural violation, which can then be acted upon. The determination of how much monitoring is required is usually done during an audit.

Auditing is the process of verifying that logging and monitoring are being done according to plan or procedures. Auditing is typically only done quarterly or semi-annually. Audits may also be done if an incident occurs or if there is a major configuration change. The result of an audit is usually a change in the logging and monitoring procedures.

Logging and monitoring are passive yet effective forms of intrusion detection. Consistent monitoring can increase the likelihood of detecting an attack against a server.

# Server Applications

The two most popular server applications are Web servers and e-mail servers. Three more categories of server activity are as follows:

- **Data sharing server**—This consists mostly of FTP servers, Lightweight Directory Access Protocol (LDAP) servers, and simple NetBIOS shares.
- **Peer-to-peer information exchange**—In this case, files are transferred directly from client to client, but may at first be coordinated through a central server.
- **Instant messaging (IM) and Internet relay chat (IRC)**—These client-server applications allow for direct and immediate communication between users.

## Data sharing

Data-sharing applications are a natural target for attackers because they often hold an organization's most valuable information and data. The most popular means of sharing files are using NetBIOS, FTP servers, and LDAP.

### FTP servers

Exchanging files with the public or with unknown users will often involve the use of FTP. Many server operating systems will come with FTP as a means for transferring files to the server. If not locked down, an FTP server can be a point of compromise for the server and network as a whole.

Anonymous FTP is particularly risky and open to various attacks. As the name implies, anyone can transfer files without being authenticated with a password. When prompted for a username, the word *anonymous* is provided. When prompted for a password, the user is expected to enter his or her e-mail address. Most FTP sites do not check that the e-mail address is valid or even that the domain in the e-mail matches the domain being used by the user.

Some sites configure their anonymous FTP servers to allow writable areas (for example, to make available incoming or *drop-off* directories for files being sent to the site). If these files can be read by anonymous FTP users, the potential for abuse exists. Abusers often gather and distribute lists describing the locations of vulnerable sites and the information these sites contain. The lists commonly include the names of writable directories and the locations of pirated software; they may also include password files or other sensitive information. These drop-off sites are used as data repositories for the abusers to share information.

Unfortunately, in many cases, system administrators are unaware that this abuse is taking place on their archive. They may be unfamiliar with this type of abuse (and so haven't taken steps to prevent it), or they may think that they have configured the archive to prevent abuse when, in fact, they have not. System administrators at the sites being used to place or pick up items from the drop-off area may also not be aware that their users are participating in this activity.

Finally, an anonymous archive server actually may be misconfigured or compromised. This misconfiguration or compromise could, in addition to the abuses previously mentioned, provide someone with the ability to run processes under the User ID (UID) of the FTP daemon. If a file can be placed in the writable area of the anonymous FTP server and this area is also readable, anyone who can connect to the anonymous FTP server can obtain a copy of the file. Specifically, abusers do the following:

- Store and retrieve information. This information is often placed in unusual or hidden files.
- Gather information about the availability of sites where the anonymous FTP areas are abused, then compile a comprehensive listing (known as a *warez list*) of the locations.
- Use this information for personal, commercial, or political gain, or to carry out attacks against other individuals or organizations.
- Abuse a vulnerable archive site for a short span of time and then move on to other sites.
- Leverage this access or exploit system configuration weaknesses to gain other privileged access.

An FTP server can be run securely, but may require constant monitoring. Following are recommendations to minimize the risk when using an FTP server:

- Lock down the server's host. The server should not run any other services. If possible, place the server behind a firewall that only permits FTP access to the server. Other hosts on the same network should not consider the FTP server trusted.
- Turn off the FTP server when it's not actually needed. In many cases, the server's administrator expects one or more users to access the FTP server in a certain window of time. The administrator should let the users know the window of time for which the server will be up so the users can get the files they need.
- Do not allow anonymous access to the FTP server. Anonymous FTP has a number of vulnerabilities. If anonymous FTP is enabled, any files on the root directory will be available for downloading. Also, Trojan horses and back-door applications might be uploaded, leading to the eventual rooting of the server.
- If anonymous FTP is required, set up a separate server to handle this traffic. Do not put any sensitive files on the same host as the anonymous FTP server.
- Turn on extensive logging on all the FTP servers.
- Closely monitor the logs and activity to the FTP server. Be prepared to stop and isolate the server in the event it exhibits any unusual behavior.

### LDAP

LDAP is a directory-access protocol derived from X.500. LDAP runs over TCP/IP or other connection-oriented transfer services. LDAP is defined in RFC2251, "The Lightweight Directory Access Protocol (v3)."

LDAP is similar to a database, but can contain more descriptive information. LDAP is designed to give quick response to high-volume lookups or searches.

LDAP uses a tree structure where each node or object in the tree contains a set of attribute-value data. Each object belongs to one or more object classes, which define the mandatory and optional attributes. The original application of both X.500 and LDAP was to provide a white pages directory service, where most objects in the tree represented people and the tree had a geographic or organizational structure.

The security issue regarding LDAP is one of privacy. An attacker could very quickly acquire all the data in the LDAP server by running a simple script, as follows:

```
#!/usr/bin/perl -w
use Net::LDAP qw(:all);
my $server = 'ldap.psu.edu';
my $base  = 'dc=psu, dc=edu';
my $ldap  = new Net::LDAP($server) or die "$@";
$ldap->bind( version => 3 );
for ( my $sn1 = ord('a'); $sn1 <= ord('z'); $sn1++ ) {
   my $c1 = chr($sn1);
   for ( my $sn2 = ord('a'); $sn2 <= ord('z'); $sn2++ ) {
      my $c2 = chr($sn2);            my $filter = "sn=$c1$c2\*";
      my $mesg = $ldap->search ( base => $base,
                 filter => $filter,
             ) || die ("Failed on search.$!");
      foreach $entry ($mesg->all_entries) {
         if ( 0 ) {
            $entry->dump;
         } else {
            my $asn = $entry->{asn};
            my $name;
            my $email;
            ATTRIBUTES: foreach my $attr (@{$asn->{attributes}}) {
               if ( $attr->{type} eq 'CN' ) { print "\n"; }
               if ( $attr->{type} ne 'PGP' ) {
                  print "$attr->{type}:";
                  my $val = $attr->{vals};
                  print join('|',@$val);
                  print "||";
               }
            }
         }
      }
   }
}
$ldap->unbind;
```

Another security issue with LDAP is that anyone on the same LAN as a legitimate user can listen in on the LDAP transactions. When a client binds to the LDAP service, it sends everything in the clear over the network. On most networks, sending usernames, passwords, and private information in the clear is inherently insecure.

## Peer to peer

Peer-to-peer (P2P) applications refer to the direct communication and transfer of files between two clients without an intermediate server. In some cases, such as Napster, a central server is needed to introduce the two clients and to provide some indexing information for files that are available for exchange. In other cases, such as Gnutella, the clients communicate from client to client across the Internet sharing their indexing information one step at a time.

P2P is an interesting and potentially useful computing paradigm that's still in the early stages of popularity. It may someday find an indispensable niche to rival e-mail and Web browsing. Along the way, it will definitely expose some flaws in the current protection needed on client machines and on organizational boundaries (firewalls, and so on).

P2P applications do raise some security concerns and issues, as follows:

- The exchange of copyrighted information (music and movies) may be a concern to the organizations hosting the clients. A lot of this discussion is focused around universities, which have many client machines, a large population of users who like music, few firewalls, and a history of permissiveness when it comes to Internet usage.
- P2P applications consume a lot of network bandwidth. While this probably does not rise to the level of a denial-of-service (DoS) attack, it does impact the logging and monitoring at very large organizations such as universities.
- P2P applications consume a lot of system and network administrators' time. The questions of legality and bandwidth usage make the P2P issue one that administrators cannot ignore.
- Most P2P applications are not limited to sharing music and movies. Viruses and Trojan horses can be exchanged, as well. If attackers can get a Trojan horse to run on a remote machine, they can do anything the user is allowed to do.
- One of the attractions to sharing files is the ability to share new applications and games. Exchanging applications in this manner makes a security professional cringe. These applications must be assumed to come from dubious persons, with motives unknown, without testing or verification. Users who engage in this behavior might as well set their workstations up on the public sidewalk and put up a big sign advertising free and unfettered access to all their personal files and activities.

## Instant messaging and chat

Instant messaging (IM) and Internet relay chat (IRC) are user-to-user communication applications that use an intermediate server. The popular IM forums are America Online (AOL IM or AIM), Yahoo, and Microsoft Subscription Network (MSN). IRC is operated over dozens of servers and is administered and moderated by the server administrators and the IRC community itself.

IM and IRC have certain inherent security risks that should be weighted by users when using these services, including the following:

- Both IM and IRC send text in the clear, so it can be sniffed and captured; this becomes a privacy issue.
- IM is usually between persons who know each other. However, IRC is most often communication between strangers. Users must be very careful not to fall prey to social engineering attacks, because the motives of strangers are not known.
- It is common to exchange and run robots (or bots) on IRC clients and servers. Bots can be very useful for administrators, as they manage their servers. However, bots can also be very destructive and are cause for concern for an unsuspecting IRC user. The casual IRC user should be able to operate without the need for any bots, and, therefore, should avoid the temptation to download and run them.
- IM has the capability to have direct peer-to-peer file transfer. For this to happen, the two clients must exchange IP addresses. Providing your IP address to an untrusted entity may increase your risk of attack.
- Care should be taken when acquiring IM and IRC clients. Because all these clients are acquired cost free, the means of distribution may not always be controlled. Launching an unsafe application can place all the data and all future transactions on the host at risk. Using the IM and IRC clients requires an inherent trust of the application developers and distributors.
- Operating IM and IRC through a central server implies a certain amount of trust in the server. All personal and confidential data that is communicated can be captured and used by third parties with or without the knowledge of the server's administrators.

# Multi-Level Security and Digital Rights Management

Multi-level Security (MLS) and Digital Rights Management (DRM) are technology objectives that have in common the need to control how digital content is shared among users. Contemporary Trusted Computing (TC) is an emerging technology that promises to fulfill that need. Many see the development of TC to be motivated by corporations' DRM objectives: to minimize revenue loss from unauthorized sharing of copyrighted information. The literature has recently acknowledged the importance of Mandatory Access Control (MAC) schemes commonly associated with MLS in meeting DRM goals. MLS is strongly associated with classical TC, but there is not much utilization of contemporary TC in building systems with MLS goals. Here the parallels and interactions between MLS, DRM, and TC (in both its senses) are explored, with particular attention paid to the possibilities of applying contemporary TC to MLS systems, perhaps even to meet the standards of classical TC.

## Background

The current usage of the term TC differs from its historical meaning, now often distinguished as "classical TC." Classical TC refers to U.S. Department of Defense criteria for evaluating and categorizing high security computer systems for government use. In particular, it is associated with the categories of systems deemed to be suitable for extremely sensitive applications, which were certified as meeting certain standards of mandatory and verified protections as specified in DOD 5200.28-STD in 1985. The term TC has since been co-opted by industry associations called the Trusted Computing Platform Alliance and the Trusted Computing Group to refer to computing technologies built upon devices with an embedded hardware security component providing cryptographic operations and key storage. This contemporary TC promises a revolutionary change in computers if ever adopted on a large scale. Both relate to the challenge of information control posed by MLS and DRM.

MLS, the goal of protecting information at multiple classification levels from unauthorized disclosure, is what classical TC is all about. It is because of this important goal that the criteria of DOD 5200.28-STD were established. That standard calls computers that meet its criteria "trusted" because they are trusted to reliably implement mechanisms which meet the goal. If the computers are faulty, information can leak. These trusted computer systems have sometimes been called "felony boxes" because the leakage of classified information is in many circumstances a felony offense, and the computers' capacity to enforce protections was often—and not unrealistically—viewed cynically.

DRM is also about protecting information. Rather than the classified information MLS is concerned with, DRM calls for the protection of copyrighted information from unauthorized usage and sharing (a.k.a., "piracy"). Contemporary TC has widely been seen as motivated by DRM.

## The challenges of information control

Government is interested in MLS; big copyright-holding media companies are interested in DRM; their needs may differ in the specifics, but both want control over their digital information. Government wants to hold its information tight to its chest, allowing sharing only under carefully controlled conditions. Media companies want their information spread far and wide, but don't want to lose a handle on it. Digital information cannot be controlled without control over the software that has access to it. In turn, that software cannot be controlled without control over the hardware it runs on. The goal of TC is to make it possible to control software without control of hardware.

What does it mean for someone who does not control hardware to control software? This person cannot install whatever software he wants, regardless of the wishes of the hardware owner, necessarily. But this person can refuse to allow access to information unless he can be certain the software, which will be receiving it, will comply with his policies for its use. In practice, this may mean dictating the choice of software and demanding proof that it is running unmodified and isolated from other software on the system. TC makes it possible to give this sort of proof, in the form of a "remote attestation."

Prior to TC, information control could only be successful in two settings: mainframes with dumb terminals, and closed devices such as cell phones. Control was possible in those settings because the hardware was under control. In the mainframe world, the computing environment was such that users did not have physical access to the central computing hardware and the terminals had no computing capability of their own. This sort of environment is a thing of the past. The other setting for successful information control not only still exists, but is even expanding, in the form of mobile devices and video gaming platforms. Proprietary, closed devices built on tamper-resistant hardware are an ideal platform on which to build control. Consumers still demand general-purpose open platforms, however, and even within government these have compelling advantages. That is why TC remains important: it makes it possible to build control on top of an open platform (i.e., a PC).

Whether built on top of a closed or a TC-enabled open hardware platform, an operating system that provides for information control must be capable of enforcing Mandatory Access Control (MAC) rules and strongly isolating processes. The commonly used commercial operating systems of today do not meet these criteria, and this has proven a stumbling block for adoption of TC. MLS systems, on the other hand, have long relied on MAC. It is the primary defining characteristic of classical TC systems rated at the B level or higher in the DoD standard.

## Building systems for information control

Although MLS systems have been developed since the 1970s, the defense and intelligence communities have preferred another approach to protecting classified information. Because of death of the mainframe and the move to networks of smaller computers, a new approach had to be taken to controlling information. The goal has been achieved by segregating information at different classification levels on to separate networks, not connected to each other (the "air gap" firewall). This approach is called MILS, or Multiple Independent Layers of Security. It is the approach most commonly used today in the defense and intelligence communities. If meeting the MLS goal on a single system was a challenge, providing for the protection of multiple levels of classified material on a single network has commonly been considered too difficult to even attempt. TC brings new hope to this old dream. [Figure 14-3](ch14.html#mls_vs._mils_colon_in_mls_comma_users_wi) contrasts MLS and MILS.

The MLS goal, alone, is not a comprehensive security strategy. For example, it does nothing to protect users who have the privilege of accessing classified information from the potential dangers of accessing it. In exchanging data at the same classification level, users may be transmitting viruses or worms, or carrying out attacks on each other. Furthermore, because users at a high privilege level can generally also read information classified at a lower level, users who can create information at the lower level have the potential to launch Trojan horse attacks of a technical, social-engineering, or combined nature. There is also the danger of covert channels. Although restrictions on the flow of classified information might be effectively implemented, overlooked means of conveying information present the opportunity for leaks.

MLS systems should allow only upward flow of information. People or processes with high access levels can access less classified information, but people or processes with lower levels of access privilege can never access more classified information. Also, people and processes can only create information at their highest level of access. Thus, a high classification privilege program, reading low classification information from two or more sources, can only write out the combination of that information at the higher level it runs at. In this way MLS facilitates security in one half of the cycle of intelligence information processing (collection and analysis) while hampering the other half (dissemination and usage).

In order to complete the cycle, less classified information must be derived from more classified information. This is sometimes referred to as the "sensor-to-shooter" challenge. The military has sophisticated spy satellites, for example, among other sources of classified information. It also has ground-level fighters who need that information—or information derived from it. In order to flow against the direction permitted by MLS systems, special "guard" processes can be used which have the ability to reduce the classification of information. These will be heavily audited and constrained to responsible authorized use. They increase the complexity of the system and are another potential avenue for leaks.

The goal of MLS is accomplished by a system implementing Mandatory Access Controls (MAC). In everyday computers, where access controls are present, they are discretionary. For example, a user can make a file readable only by himself. But he can also change the protections on that file to later make it readable by others. In a MAC scheme, certain aspects of access control are enforced by the system and are not changeable by users. These are the aspects relating to classified information flow, of course. The MAC rules can coexist with the ordinary user/group/other permissions or access control lists (ACLs), but the classification labels on files and other objects exist separately and are maintained by the system.

In contrast to successful if small deployments of MLS, current attempts at DRM have been referred to as "speed bumps" because they're acknowledged to be easily subverted and serve merely to make unauthorized use less convenient. This is because they have been based on open systems, which as discussed previously, are not a suitable platform for information control. The problem is that with global connectivity, DRM need only be subverted at one point, from which copies of information no longer protected by controls can spread. Thus, while the mission of DRM in securing a single piece of information may not seem great compared to MLS (who cares whether one extra copy of a particular song exists? vs. who cares whether one extra copy of a list of secret agents exists?), the importance of securing any given copy is magnified by the ease with which additional copies can spread from it.

At the same time, the market places another constraint on DRM solutions. Because consumers would rather have copies of information unencumbered by the inconveniences necessary for DRM (inconveniences imposed even on authorized use), they can benefit from turning to the black market for satisfaction. They need not break the DRM themselves, but rather can turn to worldwide networks of file sharers. Furthermore, the market for DRM-protected information (all commercial music, movies, books, and other forms of digital copyrighted content) is far larger than the MLS market (government classified information). Thus, the solution space for the two problems diverges along certain lines.

![MLS vs. MILS: In MLS, users with different degrees of access share a network which handles information at all levels of classification—devices must be trusted to enforce information protection rules; in MILS, there are separate networks for users with different degrees of access (e.g., Top Secret, Secret, and Unclassified)—devices do not have to be trusted to protect information.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1403.png)

**Figure 14.3. MLS vs. MILS: In MLS, users with different degrees of access share a network which handles information at all levels of classification—devices must be trusted to enforce information protection rules; in MILS, there are separate networks for users with different degrees of access (e.g., Top Secret, Secret, and Unclassified)—devices do not have to be trusted to protect information.**

This difference is reflected in the existing implementations that try to meet the goals of MLS and DRM. Whereas MLS systems have been expensive, special-purpose, highly assured (often by independent evaluators), and conformant with various government guidelines for security, DRM systems have been haphazard stabs at providing some modicum of protection without sacrificing too much convenience for consumers. The relative success of the two has to be understood in terms of the different environments they have faced. MLS has been implemented on hardware and in operating systems designed for the task. DRM has had to deal with the commodity open systems consumers choose to use.

The environment of MLS is changing to some degree. There is a greater demand now, even in government circles, to move MLS from special purpose systems to more standard ones. In fact, to be completely honest in evaluating its history, one has to acknowledge that to a large degree MLS has been passed over in favor of separate networks of standard systems for each classification level. New demands for information sharing are driving renewed interest in MLS systems. Here we consider the general problems faced by systems that attempt to control the use and distribution of (potentially) classified information. This problem is important because of the need for such systems in government, particularly in the military and intelligence areas.

In the architecture of MLS systems, reference monitors enforce MAC rules, controlling information flows in accordance with MLS policies. It is a design requirement that the reference monitor cannot be bypassed or subverted. It is generally accepted that in order to achieve a high degree of assurance, the monitor must meet the requirement that it have a relatively small code base, in order that it be easy to analyze and rigorously test. Further, the design of the overall system must be such that there can be a high degree of assurance the monitor is called to make policy judgments by every part of the system where it is appropriate to do so. In order for this to be the case, the generally accepted wisdom is that a microkernel or exokernel design is necessary: that is, the typical monolithic kernel structure is insufficiently modular for an analyst to be reasonably sure it behaves correctly with respect to MLS goals in every situation.

Unfortunately, merely dropping in TC is not enough. Re-architecting the structure of the OS is necessary to support the modularity required for high-assurance content management, whether MLS or DRM.

Let us step back now and examine the relevant details of TC. As mentioned, the distinguishing characteristic of contemporary TC is the addition of a hardware security module. This is referred to as the Trusted Platform Module (TPM). The reason there's been so much controversy over it and so little agreement on what it implies for the future of computer security is that it is essentially useless without operating system support, and current operating systems are not structured in a manner to properly support it. This is the reason that it still seems to be vaporware and that predictions are running rampant, without any actual implementations to be found. There is enormous potential for it to change things, but the scene first has to be set by changes in operating systems. And in fact those changes in the structure of operating systems would dwarf in significance the addition of the TPM to computer platforms.

What is required for TC is, essentially, the very sort of isolation and protection needed for MLS. That is, MAC. What TC would then do, however, is allow MLS to be extended from a single system to a network of systems. This is a very important distinction. Recall that the primary reason MILS is used instead of MLS is the fact that networks are a necessary part of modern information infrastructure, but MLS has not previously been a realistic goal across networks. TC would make this possible by allowing the systems on a network to prove to each that they run secure software and that they are enforcing the correct protections on information.

Where TC with just a TPM falls short is in hardware attacks. A user with full access to the hardware can circumvent protections by snooping on I/O lines, among other techniques. While Microsoft and Intel work on standards to extend protection to all parts of the computer, TPM-only TC is still a powerful tool in environments where the computers are not expected to fall under physical attack, or where sensors and monitoring can protect them from such attack. These environments include government and corporate offices. Thus, while TPM-only TC may not be useful for DRM, it can be useful for MLS applications in cases where, for economic reasons, one weak spot allowing content to be extracted means the entire scheme is broken, and practical reasons preclude monitoring users' computers.

# Summary

Servers are favorite targets for attackers. Servers have the advantage of being widely used (so attackers can concentrate their efforts) and accessible by the attacker. Additionally, the attacker knows that servers are likely to hold a wealth of data that can be exploited.

The problems with insufficient security in software applications are magnified by the development of server applications. Security should be incorporated into a server application from the very beginning in the software requirements. If security must be retrofitted into an application, it will be very expensive and not completely effective. Additionally, software development organizations should spend more time and effort testing the application before releasing it to customers. It is all too common that developers test performance, but the general public tests security.
