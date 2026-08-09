# Chapter 3. Interfacing with the Organization

**IN THIS CHAPTER**

- **Understanding how security fits within an organization**
- **Determining a methodology for implementing enterprise security**
- **Identifying core areas of focus for security**
- **Knowing the key questions and information that must be provided to executives**

Many organizations have security policies, security teams, and security budgets, but that is not enough for an organization to be secure. Most organizations that have had security incidents had policies, budgets, and security personnel in place; however, they did not have security integrated within the organization and mapped to risk. Managing and controlling the risk to critical information and communicating this to executives is a critical part of a successful security program.

This chapter defines an enterprise methodology that can be used for managing security within an organization. Security cannot be successful if there is not buy-in from the executives, and if the executives do not understand and know the risks that are present to their organization. Therefore, once a methodology is defined, key questions that every manager must be able to answer are defined with appropriate responses.

# An Enterprise Security Methodology

"What actions should I take to improve security?" "How much should I spend on security?"

These are common questions all CEOs, presidents, and CFOs ask themselves in these vulnerable times.

How to address security is confounded by a number of confusing and ironic aspects of the problem, such as the following:

- The technologies involved are very high tech and not fully understood by most in senior management.
- The threat is usually discussed in terms that don't readily translate to dollars.
- The greatest threat is from the inside; but the corporate culture has learned to trust and rely only on those within the organization.
- The items at risk are not physical and perhaps less tangible — information, reputation, and uptime.
- People have been crying "the sky is falling" for a while and nothing serious has happened to us, yet.
- There are many solution providers offering security products and services. For the most part, they provide only partial solutions.
- Spending is not predictive of the security received. A $35 modem can bypass the security of a $100,000 firewall.

From senior management's perspective, information security should be viewed as classic insurance. No corporation would consider operating without fire insurance. Management understands that fires happen. The likelihood of a fire can be reduced, but there is always a significant chance that all precautions will break down and a fire will occur. Therefore, insurance is required. Senior management views the acquisition of fire insurance as part of its fiduciary responsibilities.

Information security spending is very similar to fire insurance. Management should, by now, understand that security attacks happen. The likelihood of an attack can be reduced, but there is always a significant chance that all the precautions will break down and an attack will occur. Therefore, spending on information security is required. Senior management should view this spending also as part of its fiduciary responsibilities.

Although the decision is not easy, senior management usually makes the correct choice of the amount of fire insurance to acquire. This is an area in which managers have experience and they are qualified to make the choice. The problem of how much to spend on information security is much more difficult.

This section describes a process for evaluating the threat, vulnerability, and risk with regard to an information security program. The risk is then used to determine controls and spending needed to mitigate the risks. Following this process, the enterprise is secured to the maximum extent necessary while maintaining a good return on investment (ROI) relative to the resources expended.

## The methodology

The methodology proposed will ensure that an enterprise receives the maximum protection for the dollars invested. Additionally, this methodology will have an enterprise establish protective measures (security controls) only if these are cost effective from a business perspective. This methodology is not new and innovative; it is just comprehensive and methodical. It is derived from classic risk management practices that have been used for centuries, whatever they may have been called. Any project manager will recognize the fundamentals in this approach even though the wording or jargon may be unique to security.

First, let's define the terms of this methodology. By clearly defining these terms and using them consistently throughout, the process as a whole will be more easily understood. I want to remove any fear, uncertainty, and doubt about methodology. In the end, I would hope that an enterprise recognizes the methodology as easy to understand. The implementation will not be easy—there are no easy security solutions. But senior management should be able to recognize that this method will lead to a cost-effective and maximally secure enterprise. Here are the terms:

**Vulnerability**— A specific and known weakness in a system or device that has been determined makes the system or device potentially open to attack. The determination may be a result of an "exploit" (defined later) or an academic review of the weakness. Vulnerabilities in themselves are not security problems to be corrected. Vulnerabilities do not necessarily lead to risks (described later). More analysis than just determining a vulnerability is needed to determine risk. Vulnerabilities do not necessarily need to be corrected. Corrective measures should result from a determination of what security controls to implement.

**Exploit**— A set of steps that allows an attacker to breach the security of a system. Hackers take vulnerabilities and develop specific attacks. Exploits can be very troublesome if they are put into scripts and made widely available to "script kiddies." Often, security professionals identify exploits after they have successfully been used to attack a system.

**Threat**— A somewhat nebulous collection of all possible activities and circumstances that could pose a danger to the enterprise. Whether or not the danger is real depends on the enterprise's vulnerabilities and a risk assessment. The threat exists whether or not an enterprise has any vulnerabilities to be exploited. Threat also sometimes refers to the person or persons who will possibly conduct an attack. The security professional determines the current threat by staying on top of the emerging issues in the community. Sources for this include Cert, NPIC, FBI, SANS, and others. NIST SP 800-30 defines a threat as "the potential for a threat source to exercise or exploit a vulnerability." It defines a threat source as "either (1) intent and method targeted at the intentional exploitation of a vulnerability or (2) a situation and method that may accidentally trigger a vulnerability."

**Business impact**— The determination of the value of services, capabilities, and data to the operation of the business. This determination should address the bottom line and be couched in terms of dollars. The determination should include both the cost for the loss of the service/data as well as the cost to restore the service/data. For example, what is the business impact for the loss of e-mail? Conducting a good business impact analysis is the most under-accomplished portion of a typical risk assessment. Security professionals should not be relied upon to provide the business impact analysis. They do not understand the business as well as the enterprise managers do. In practice, the business impact analysis is usually done jointly with enterprise management and the security professionals. The reason for this is that the security professionals have seen the process done numerous times and can facilitate the discussions.

**Risk assessment**— The process by which the current threat, vulnerabilities, and business impact are determined for an enterprise or organization. The process takes input from the security professional to determine the state of the current threat. The risk assessment process determines the vulnerabilities by conducting interviews, scanning, sniffing traffic, examining systems and devices, doing architectural/design reviews, and applying other techniques. The risk assessment process also takes as input the business impact analysis. The result of a risk assessment is a very specific understanding of the threat, vulnerabilities, and business impact of an enterprise or organization at a specific point in time. [Figure 3-1](ch03.html#results_from_a_risk_assessment) illustrates the output or result of a risk assessment. Corrective measures will result from a risk loss analysis and a determination of what security controls to implement.

![Results from a risk assessment](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0301.png)

**Figure 3.1. Results from a risk assessment**

The discussion to this point might be considered the first phase of addressing methodology. We have examined the threat and the vulnerabilities as well as the business impact of systems, processes, and data that have the vulnerabilities. But what does the methodology do with all this information? Suppose there is a rise in RPC (remote procedure call) attacks (the threat), and a system has an RPC weakness (vulnerability). If that system goes down it costs the enterprise $1,000 per event (business impact). What should be done? Will a point solution such as a firewall help? Should code be rewritten? What are the costs of these solutions? This methodology offers a means to determine all these issues.

**Loss analysis**— The process by which the threat, vulnerabilities, and business impact are combined to determine the risk to the enterprise in bottom line terms (usually dollars). A number of formulas have been used over the years. We propose a simple one, described as follows:

> Frequency of occurrence (threat) × Damage per event (business impact)
> 
> = Expected dollar loss (risk)

In this formula, the threat for a given vulnerability observed on the enterprise's system is put in terms of "likelihood to occur per year." A significant amount of insight on the part of the security professional is required to make this determination. Factors in making this determination include the following:

- How predominant is this threat in the current environment?
- How difficult is it to exploit the vulnerability?
- Are exploits already developed for the vulnerability?
- What is the architecture and exposure of the system?
- Is there any history of the system being attacked?
- What's the experience of the industry with respect to this threat?

The result of this formula is an expected dollar cost that the enterprise will experience if the vulnerability is not addressed. This is the risk of the vulnerability before any mitigating or corrective action.

**Risk**— The value of the expected dollar cost for a given vulnerability or set of vulnerabilities. Risk is determined from the loss analysis process. As a stand-alone product, the risk that an enterprise has can provide a worthwhile insight into the value of its services and data. A summary of the risks can also provide senior management with a snapshot of the overall security of the enterprise. [Figure 3-2](ch03.html#risk_result_from_a_loss_analysis) illustrates the determination of risks.

![Risk result from a loss analysis](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0302.png)

**Figure 3.2. Risk result from a loss analysis**

**Mitigation**— Using this process, the IT department and security professionals determine what action can be taken to mitigate or eliminate the risk. It is important that the cost of mitigating the risks be determined at this time. The cost is important when deciding what controls to implement. The steps to be taken can fall into either of two categories:

- Actions that will reduce the likelihood that the vulnerability will be exploited. This typically involves steps such as patching the system or inserting a firewall.
- Actions that will reduce the damage if the exploit occurs. This typically involves steps such as conducting backups. By reducing the damage done by the attack, the business impact can be lessened.

**Determination of controls**— The process by which risks and their mitigations are prioritized and compared against a security budget. The result of this process is a set of security controls to be implemented. In this process, senior management decides what level of risk is acceptable and how much will be spent on mitigating that risk.

**Security controls**— These are a set of processes and activities that improve the security of the enterprise by mitigating risks. Security controls are measures taken on a continuous or daily basis that are not required for the normal operation of the network or operation. [Figure 3-3](ch03.html#management_determines_security_controls) illustrates the process from risks to security controls. The measures are additional actions to mitigate a known risk. Some common security controls are as follows:

- Specific policies and procedures
- Specific system backups
- A firewall and its rule set
- The requirement to log certain activity on servers
- Management review of log activity
- Hardening of operating systems before placing them in service
- Personnel training

At this point, the enterprise has completed a risk assessment, converted the threat, vulnerabilities, and business impacts to risks, and mitigated the risks with security controls. These controls are protecting the network and operations. However, security environments have aspects that require even more response on the part of the enterprise. The security environment is always changing because the threat is constantly evolving and the smallest hole could lead to big attacks. In addition, the enterprise environment changes—systems get upgraded, applications are added, and personnel change. Because of this changing environment, security controls need to be audited for relevance and compliance.

Small holes in an enterprise's security defense can often lead to severe attacks. Because this is the case, security controls cannot be taken for granted or assumed to be 100 percent complied with. An enterprise must audit security controls to ensure complete compliance.

**Audit**— The process by which examiners take the list of security controls and determine if the measures are being carried out as planned. Because the audit looks primarily at compliance in implementing security controls, audits should be able to be done quickly and frequently. Different security controls require different frequencies of auditing. Therefore, the schedule of audits may cover different security controls. In most cases, an audit schedule will have a daily, weekly, monthly, quarterly, and yearly component. Any verification of a security control done on a daily basis should take no more than a few minutes to complete. Quarterly and annual audits may require a day or two.

![Management determines security controls.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0303.png)

**Figure 3.3. Management determines security controls.**

Note that an audit is very different from a risk assessment and has a much narrower scope. Audits can be done by IT personnel and management, although these auditors should first receive training from security professionals.

Three general outcomes may result from an audit. The security controls may need to be modified, personnel may need training, or a new risk assessment may be needed. A security control will need to be modified when the audit discovers that the actions taken in the control are not meeting the intent. For example, suppose a security control is established to log scanning activity against a perimeter device. When an audit is conducted a month later, it is noted that the volume of logged data is too great to be useful. The security control should be modified to either post-process the logs to reduce them to a useable size or to modify the logging activity.

The result of the audit will often require personnel training. For example, a security control may be adequate but personnel may not have the knowledge or skills to implement the control. This is illustrated in [Figure 3-4](ch03.html#audits_verify_and_validate_security_cont).

![Audits verify and validate security controls.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0304.png)

**Figure 3.4. Audits verify and validate security controls.**

In rare cases, the audit will point out the need for another risk assessment. This occurs when systems, personnel, or data have changed sufficiently that the security controls no longer appear to be meeting the security needs. For example, an audit might be reviewing perimeter logs for an organization and discover that an entire branch office has not been logging. The reason may be that the branch was recently acquired and merged into the organization. A simple modification to the security controls would not cover this situation; rather, a new risk assessment is called for.

As can be seen, there is nothing new and innovative about this methodology that works from the threat and vulnerabilities, folds in the business concerns, and determines risks. The risks are then mitigated on a "business effective" basis and security controls are established. Because security is ever changing, the controls must be monitored and audited.

# Key Questions to Manage Risk

The following are 30 things all managers/executives should know the answer to in order to track and validate the security of their organizations.

**What does your network/security architecture diagram look like?**

The first thing you need to know to protect your network and systems is what you're protecting. You must know the physical topologies, logical topologies (Ethernet, ATM, 802.11, VoIP, and so on), types of operating systems, perimeter protection measures (firewall and IDS placement, as well as other measures), types of devices used (routers, switches, and others), location of DMZs, IP address ranges and subnets, use of NAT, and so forth. In addition, you must know where the diagram is stored and that it is regularly updated as changes are made.

**What resources are located on the DMZ (term taken from "demilitarized zone")?**

Only systems that are semi-public are kept in the DMZ. This includes external Web servers, external mail servers, and external DNS. A split-architecture may be used where internal Web, mail, and DNS are also located on the internal network.

**What resources are located on the internal network?**

In addition to internal Web, mail, and DNS servers, the internal network also includes databases, application servers, and test and development servers.

**Where is your organization's security policy posted and what is in it?**

There should be an overall policy that establishes the direction of the organization and its security mission as well as roles and responsibilities. There can also be system-specific policies to address policies for individual systems. Most importantly the policies should address appropriate use of computing resources. In addition, policies can address a number of security controls from passwords and backups to proprietary information. There should be clear procedures and processes to follow for each policy. These policies should be included in the employee handbook and posted on a readily accessible intranet site.

**What is the password policy?**

The password policy requires that a password be at least 15 characters long. It should contain both alphanumeric and special characters. The user should not be able to re-use the last five passwords. The password must change every 90 days, and it must be locked out after three failed attempts. In addition, you should be performing regular password auditing to check the strength of passwords, and this should also be included in the password policy.

**What applications and services are specifically denied by the organization's security policy?**

The organization's security policy should specify applications, services, and activities that are prohibited. These can include, among others, viewing inappropriate material, spam, peer-to-peer file sharing, instant messaging, unauthorized wireless devices, and the use of unencrypted remote connections such as Telnet and FTP.

**What type of IDSs are used?**

To provide the best level of detection an organization should use a combination of both signature-based and anomaly-based intrusion detection systems. This allows both known and unknown attacks to be detected. The IDSs should be distributed throughout the network, including areas such as the Internet connection, the DMZ, and internal networks.

**Aside from default rule sets, what activities are actively monitored by the IDS?**

IDSs come with default rule sets to look for common attacks. These rule sets must also be customized and augmented to look for traffic and activities specific to the organization's security policy. For example, if the organization's security policy prohibits peer-to-peer communications then a rule should be created to watch for that type of activity. In addition, outbound traffic should be watched for potential Trojans and back doors.

**What type of remote access is allowed?**

Remote access should be tightly controlled, monitored, and audited. It should be provided only over a secure communication channel that uses encryption and strong authentication, such as an IPSEC VPN. Desktop modems (including applications such as PCAnywhere), unsecured wireless access points, and other vulnerable methods of remote access should be prohibited.

**What is your wireless infrastructure?**

Part of knowing the network architecture includes knowing the location of wireless networks because these create another possible entry point for an attacker. You must also know whether they are being used for sensitive data and whether they are secured as well as possible.

**How is the wireless infrastructure secured?**

Wireless access must at least use WPA (Wi-Fi Protected Access). Although this provides some security it is not very robust, which is why the wireless network should not be used for sensitive data. Consider moving to the 802.11i standard with AES encryption when it is finalized with WPA2.

**What desktop protections are used?**

Desktops should have a combination of antivirus software, personal firewall, and host-based intrusion detection. Each of these software packages must be regularly updated as new signatures are deployed. They must also be centrally managed and controlled.

**Where, when, and what type of encryption is used?**

VPNs should be used for remote access and other sensitive communication. IPSEC is a great choice for this purpose. Strong encryption protocols such as 3DES and AES should be used whenever possible. Web access to sensitive or proprietary information should be protected with 256-bit or greater SSL. Remote system administration should use SSH. File system encryption should also be used to protect stored data.

**What is your backup policy?**

A good backup policy includes weekly full backups with incremental backups performed daily. This includes all critical systems. In addition the backups should be stored at an offsite location. Because backups include very valuable, easily accessible information, only trusted individuals should be performing them and have access to them. An organization should also encourage users to perform local backups as well.

**How is sensitive information disposed of?**

Hard copies of sensitive information should be destroyed by pulping, shredding, or incinerating. Sensitive information on hard drives and disks should be completely erased using special software, or the disks destroyed. Simply deleting a file is not sufficient to prevent attackers from undeleting the file later. If you are disposing of a computer system, be sure to erase all sensitive files from the hard drive by using a wipeout utility.

**What is your disaster recovery plan?**

The disaster recovery plan (DRP) should include recovery of data centers and recovery of business operations. It should also include recovery of the physical business location and recovery of the business processes necessary to resume normal operations. In addition, the DRP should address alternate operating sites.

**How often is the disaster recovery plan tested?**

The plan is no good unless it is tested regularly, and at least once a year. The test will iron out problems in the plan and make the plan more efficient and successful if/when it is needed. Testing can include walkthroughs, simulation, or a full-out implementation.

**What types of attacks are you seeing?**

Typically, an organization sees a constant stream of port scan attacks. These are a regular occurrence on the Internet as a result of attackers and worms. An organization should not be seeing many substantial attacks such as compromises, back doors, or exploits on systems. This would indicate that the security defenses are weak, patching may not be occurring, or other vulnerabilities exist.

**How often are logs reviewed?**

Logs should be reviewed every day. This includes IDS logs, system logs, and management station logs. Not reviewing the logs is one of the biggest mistakes an organization can make. Events of interest should be investigated daily. It can be a very tedious task for a single person to do this job as his or her only assignment (unless the person really enjoys it). It is better to have a log review rotation system among the security team and use automated security incident and event (SIEM) management tools.

**How often are you performing vulnerability scanning?**

An organization should be performing vulnerability scanning as often as possible, depending on the size of the network. The scanning should be scheduled to allow adequate time to look through the reports and discover anything that has changed, and mitigate the vulnerability.

**What physical security controls are in place in your organization?**

Physical security is a large area that must be addressed by an organization. Physical controls include physical access controls (signs, locks, security guards, badges/PINs, bag search/scanning, metal detectors), CCTV, motion detectors, smoke and water detectors, and backup power generators.

**What are your critical business systems and processes?**

Identifying the critical business systems and processes is the first step an organization should take in order to implement the appropriate security protections. Knowing what to protect helps determine the security controls, and knowing the critical systems and processes helps determine the business continuity plan and disaster recovery plan process. Critical business systems and processes may include an e-commerce site, customer database information, employee database information, the ability to answer phone calls, and the ability to respond to Internet queries.

**What are the specific threats to your organization?**

In addition to identifying the critical business systems and processes, it is important to identify the possible threats to those systems as well as to the organization as a whole. You should consider both external and internal threats and attacks using various entry points (wireless, malicious code, subverting the firewall, and so forth.) Once again, this will assist in implementing the appropriate security protections and creating business continuity and disaster recovery plans.

**What are the tolerable levels of impact your systems can have?**

An organization must understand how an outage could impact the ability to continue operations. For example, you must determine how long systems can be down, the impact on cash flow, the impact on service level agreements, and the key resources that must keep running.

**Are you doing content-level inspection?**

In addition to the content-level inspection performed by the IDS, specific content inspection should also be performed on Web server traffic and other application traffic. Some attacks evade detection by containing themselves in the payload of packets, or by altering the packet in some way, such as fragmentation. Content-level inspection at the Web server or application server will protect against attacks such as those that are tunneled in legitimate communications, attacks with malicious data, and unauthorized application usage.

**How often are your systems patched?**

Systems should be patched every time a new patch is released. A lot of organizations don't patch regularly and tend to not patch critical systems because they don't want to risk downtime. However, critical systems are the most important to patch. You must schedule regular maintenance downtime to patch systems. As vulnerabilities are discovered attackers often release exploits even before system patches are available. Thus, it is imperative to patch systems as soon as possible.

**How are you protecting against social-engineering and phishing attacks?**

The best way to protect against social-engineering and phishing attacks is to educate users. Employees should attend security awareness training that explains these types of attacks, what to expect, and how to respond. There should also be a publicly posted incidents e-mail address to report suspicious activity.

**What security measures are in place for in-house developed applications?**

Any development that is taking place in-house should include security from the beginning of the development process. Security needs to be a part of the requirements and testing. Code reviews should be conducted by a test team to look for vulnerabilities such as buffer overflows and back doors. For security reasons, it is not a good idea to subcontract development work to third parties.

**What type of traffic are you denying at the firewall?**

There should be a default-deny rule on all firewalls to disallow anything that is not explicitly permitted. This is more secure than explicitly denying certain traffic because that can create holes and oversights on some potentially malicious traffic.

**How are you monitoring for Trojans and back doors?**

In addition to periodic vulnerability scanning, outgoing traffic should be inspected before it leaves the network, looking for potentially compromised systems. Organizations often focus on traffic and attacks coming into the network and forget about monitoring outgoing traffic. Not only will this detect compromised systems with Trojans and back doors, but it will also detect potentially malicious or inappropriate insider activity.

# Summary

To be able to secure an organization, it's critical that you understand the risks and the information you are trying to protect. By properly analyzing your environment and empowering your executives to ask the correct questions, you can invest your resources in the proper areas to secure your organization.
