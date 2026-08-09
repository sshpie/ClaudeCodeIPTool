# CHAPTER 11  
Attack Vector Trends and Hospital Network Breaches with IoMT Devices

Hospital network breaches via connected medical devices are a growing threat in healthcare. In recent years, the distribution and implementation growth of IoMT devices has introduced more cybersecurity risks to hospital networks with the increased attack surface. I wrote a novel that depicts some of the latest attack vectors from the perspective of real human impact in a target healthcare environment. It's called *Silent Intrusions*, and you can download it from your favorite marketplaces. As healthcare IT professionals, it's crucial to understand these vulnerabilities and their impact and implement robust security measures.

Connected devices such as insulin pumps, infusion systems, patient monitors, imaging devices, and implantable cardiac devices enhance patient care and clinical efficiency. These devices streamline operations, enable real‐time monitoring, and improve outcomes, establishing themselves as critical tools in modern healthcare. However, this technology landscape also introduces a complex array of cybersecurity challenges.

Recent statistics highlight the alarming vulnerabilities inherent in IoMT devices. These vulnerabilities have far‐reaching implications, endangering individual patient safety and the integrity of entire healthcare networks. Cybercriminals exploit weaknesses such as outdated software, weak authentication protocols, unencrypted communication, and insufficient patch management. The inherent complexity of healthcare environments exacerbates these issues, where flat network structures, inadequate segmentation, and the rapid adoption of internet‐connected devices expand the attack surface.

This chapter examines the risks of IoMT devices, exploring their role in healthcare network breaches and how vulnerabilities arise from technological, procedural, and human factors. As cyber threats grow increasingly sophisticated, healthcare organizations face the urgent challenge of safeguarding patient data, maintaining operational continuity, and building trust in an era of connected care.

## Understanding the IoMT Risk Landscape

IoMT devices encompass a wide range of connected medical equipment, including the following:

- Insulin pumps
- Infusion systems
- Patient monitors
- Imaging devices
- Implantable cardiac devices

These devices offer tremendous benefits in patient care but also present unique security challenges. My research from studies has revealed alarming statistics about IoMT device vulnerabilities, such as the following:

- **Infusion pumps:** In general, 75% of infusion pumps were found to have known security gaps that put them at increased risk of being compromised by hackers. Fifty‐two percent of analyzed infusion pumps were susceptible to two critical vulnerabilities disclosed in 2019. Twenty‐seven percent of infusion pumps have unpatched critical severity CVEs.
- **Medication dispensing systems:** More than 80% contained unpatched vulnerabilities, and more than 30% operated on unsupported Microsoft Windows versions.
- **General medical devices:** On average, each medical device harbors around six vulnerabilities, with more than 40% nearing end‐of‐life and lacking adequate manufacturer support.

These findings underscore the pressing need for enhanced cybersecurity measures to safeguard patient safety and data integrity in healthcare settings.

### Key Vulnerabilities of IoMT and Healthcare Network Breaches

IoMT has introduced vulnerabilities in healthcare networks, leading to breaches compromising patient data and critical systems. These risks arise from outdated infrastructure, weak security protocols, and the complexity of interconnected medical devices.

Many healthcare organizations still use legacy systems that lack modern security features, making them susceptible to cyberattacks. Devices like infusion pumps and imaging systems often run on outdated operating systems without essential security updates, providing attackers with easy entry points. Weak authentication protocols, including default or hard‐coded passwords, expose IoMT devices to unauthorized access.

Unencrypted or poorly encrypted communication channels also pose a significant risk, allowing attackers to intercept sensitive patient data or manipulate device functions. Additionally, healthcare institutions often fail to implement timely software patches due to regulatory concerns, leaving vulnerabilities unaddressed for extended periods.

Poor network segmentation enables attackers to move laterally across systems once a single device is compromised. The growing number of internet‐connected medical devices increases the attack surface, as many lack built‐in security protections. Human error and insider threats further exacerbate cybersecurity risks, with inadequate training leading to unsafe practices such as password reuse and susceptibility to phishing attacks.

Ransomware attacks have become particularly damaging. They exploit IoMT weaknesses to disrupt hospital operations and delay patient care. Third‐party vendors' role adds another layer of vulnerability, as security gaps in vendor‐supplied devices and services can be exploited to breach healthcare networks.

Mitigating these threats requires a comprehensive approach, including regular software updates, strong authentication measures, robust encryption, network segmentation, and enhanced cybersecurity training for healthcare professionals. Addressing these vulnerabilities is crucial to safeguarding patient data and ensuring the security of interconnected medical systems.

### Anatomy of a Healthcare Cyber Attack

I'll get into another case study that's more than just bits and bytes. It's about human ingenuity, both in attack and defense. It's also about the silent guardians who protect our digital lives and the shadowy figures who seek to disrupt them. Imagine for a moment you're sitting at your desk, sipping your morning coffee, when suddenly your computer starts acting strangely. Pop‐ups appear out of nowhere, and your browser is redirected to unfamiliar sites. You feel a creeping sense of unease. Something is not right, but you can't put your finger on it. This is how our study begins, not with blaring alarms but with a whisper of doubt.

This isn't science fiction. It's the reality that healthcare professionals can face when a subtle digital intruder infiltrates their systems, slipping past their defenses. As I peel back the layers of this incident, I want you to put yourself in the shoes of these people. A nurse could have unwittingly opened the door to this threat through a seemingly innocent email—the IT professional who first noticed the anomalies and raised the alarm. The cybersecurity team worked tirelessly, piecing together digital breadcrumbs to uncover the full extent of the intrusion.

I'll also explore the human side of threat detection: the late nights, frustration, and breakthrough moments. I'll briefly examine the mindset of both the defenders and the attackers, understanding their motivations, techniques, triumphs, and failures. But this isn't just about looking back. It's about learning, adapting, and growing stronger. Every cyber incident is a teacher if we're willing to listen. I'll discuss the lessons learned, not just in terms of technology but human behavior, organizational culture, and the critical importance of awareness and education.

I encourage you to reflect on your experiences. Have you ever felt that nagging suspicion that something is wrong with your computer? Have you ever been the one to spot an anomaly and raise the alarm? Or perhaps you've been on the other side, part of a team working to unravel a complex cyber incident?

I'll begin our journey into the anatomy of this cyber‐attack, which showcases the stages that threat actors typically follow (such as the one shown in [Figure 11‐](#c11-fig-0001)[1](#c11-fig-0001)). But as I do, remember that people are behind every line of code, security alert, and incident response. People are working to protect, learning to defend, and striving to create a safer digital world. This is more than just a technical analysis. It's an example of an incident that can have a real impact on people's lives.

Understanding this process is crucial to better defend against and respond to such attacks. Why? Because signs of the early stages of an attack are called *indicators of attack* (IOAs). In the industry, I hear more about indicators of compromise (IOCs). IOCs include malware signatures, suspicious IP addresses, and unusual outbound network traffic. IOAs include unusual enumeration and account behavior, suspicious process execution, and attempts to escalate privileges. The key distinction is that IOCs tell you what happened after (or during) an attack, while IOAs help you detect and potentially stop an attack in progress. IOCs are more reactive, while IOAs are proactive in cybersecurity defense strategies. IOCs and IOAs provide a more comprehensive approach to threat detection and response.

- **Reconnaissance** Let's start with the first stage of most cyber‐attacks: reconnaissance. This is where attackers gather information about their target, much like a burglar casing a house before a break‐in. The goal is to build a comprehensive picture of the target's digital landscape, identifying potential vulnerabilities and weak points that can be exploited later.
- **Enumeration** Once the initial reconnaissance is complete, attackers typically move on to enumeration. This stage involves a more detailed probe of the identified systems and networks. This stage is all about gathering specific technical information that can be used to plan the actual attack. It's like creating a detailed map of the target's digital territory, focusing on identifying weaknesses to attack.
- **Penetration** With a clear picture of the target environment, attackers now attempt to gain initial access. This is where they validate and exploit vulnerabilities identified in the previous stages. The goal here is to establish a foothold in the target system, no matter how small. ![A flow of a cyber attack. The stages in the attack include discovery, enumeration, penetration, becoming root, data theft, log bashing, and planting a backdoor. The initial stage of discovery involves locating and footprinting a target.](/api/v2/epubs/urn:orm:book:9781394349418/files/images/c11f001.png) [**Figure 11-1:**](#R_c11-fig-0001) Common stages of an anatomy attack
- **Escalation of Privileges** Once inside the system, attackers typically don't have complete access. The next step is to escalate privileges, often aiming to gain root or administrator‐level access. Root access is crucial as it gives the attacker full control over the compromised system.
- **Data Exfiltration** With high‐level access secured, attackers can now focus on their primary objective: stealing valuable data. Depending on the attacker's motives, the type of data stolen can vary widely, from personal information to intellectual property or financial data.
- **Covering Tracks** Sophisticated attackers don't want to leave evidence of their presence. After achieving their primary objective, they'll take steps to cover their tracks. The goal is to make the attack as challenging to detect and investigate as possible, often leaving defenders unsure if an attack occurred.
- **Establishing Persistence** Finally, many attackers want to ensure they can regain access to the system in the future. To this end, they establish persistence by planting a backdoor. These backdoors are often disguised as legitimate system processes, making them difficult to detect.

Understanding the anatomy of a cyberattack is crucial for many reasons, but here are the top three:

- Helps security teams think like attackers, improving their ability to anticipate and prevent attacks.
- It guides the development of comprehensive defense strategies that address each stage of an attack.
- It aids in incident response, helping teams understand what to look for when an attack is suspected.

Remember, while I've presented these stages linearly, they can overlap or occur in a different order, and many variations and tangents could be their full manuscripts of content. Sophisticated attackers are adaptive and may adjust their approach based on their encounters. Once inside the environment, attackers do not necessarily need to execute the attack immediately. Many prefer to infiltrate and gather data until executing further on the attack chain when most advantageous. This emphasizes the need for constant vigilance on the part of the internal cybersecurity team.

Cyber defenders make each stage as tricky as possible for attackers. By implementing strong security measures at each point, from limiting publicly available information to robust logging and monitoring, we can significantly increase our chances of detecting and stopping attacks before attackers succeed.

## Attack Vector Trends and Landscape

I'll dive into the cyberattack landscape because it's been wild. Let's start with the big picture. According to Check Point Research, there's a staggering 75% surge in cyberattacks worldwide toward the third quarter of 2024 compared to the same period the previous year. As shown in [Figure 11‐](#c11-fig-0002)[2](#c11-fig-0002), organizations face an average of more than 1,800 weekly attacks. That's not just a number, folks; it's a wake‐up call.

![A bar graph depicts the data on yearly cyber attacks. The attack increased from 700 in 2021 to 1800 in 2024. It is determined from 2021 to 2024.](/api/v2/epubs/urn:orm:book:9781394349418/files/images/c11f002.png)

*[**Figure 11-2:**](#R_c11-fig-0002) Average weekly cyberattacks*

This cyberattack activity is undoubtedly staggering, and it correlates with six significant trends:

- Increased sophistication of ransomware attacks
- Rise in cloud‐based attacks
- AI‐enhanced cyber threats
- Increased targeting of critical infrastructure
- Supply chain and vendor attacks
- Identity‐based attacks

I’ll briefly talk about identity‐based attacks and provide examples from my research.

- **Increased Sophistication of Ransomware Attacks** Ransomware attacks continue to plague organizations globally. In the first half of 2024, there was a 50% year‐on‐year increase in ransomware activity. But it's not just about quantity; it's about sophistication. The big story is the rise of double extortion and even triple extortion tactics. Attackers aren't just encrypting data anymore; they're stealing it and threatening to leak it publicly. Some are even contacting the victim's customers or partners to increase pressure. A prime example is the attack on McLaren Health Care in August 2024. The attackers encrypted critical systems and exfiltrated sensitive patient data, threatening to release it unless a ransom was paid. This attack disrupted healthcare services and put patient privacy at risk. You can read more about this at the HIPAA Journal at `www.hipaajournal.com`.
- **Rise in Cloud‐Based Attacks** With more organizations moving to the cloud, there is a corresponding rise in cloud‐targeted attacks. CrowdStrike reported a 75% increase in cloud intrusions in 2024. These attacks often exploit misconfigurations or use stolen credentials to access cloud environments. Once inside, attackers use legitimate tools to blend in with everyday activities, making detection challenging. A notable example is the breach of Toyota North America's cloud infrastructure in August 2024. The ZeroSevenGroup claimed responsibility, stating they accessed 240GB of data, including employee and customer information, contracts, and financial data.
- **AI‐Enhanced Cyber Threats** There has been a significant uptick in cybercriminals' use of AI. Generative AI creates more convincing phishing emails, develops sophisticated malware, and even automates parts of the attack process. Artificial intelligence creates new content, such as text, images, music, and code, by learning patterns from large datasets. It uses advanced machine learning models, deep learning, and neural networks to generate human‐like outputs. In early 2024, a sophisticated phishing campaign targeted U.S. government officials. The attackers used AI to generate highly personalized and convincing emails, which increased their success rate in compromising accounts.
- **Increased Targeting of Critical Infrastructure** Attacks on critical infrastructure have intensified, focusing on energy, healthcare, and government sectors. Many of these attacks have geopolitical motivations. A stark example is the 2023 attack on the Danish power grid, attributed to Russian hackers. This attack caused temporary power outages and highlighted the vulnerability of national infrastructure to cyber threats.
- **Supply Chain and Vendor Attacks** Cybercriminals are increasingly targeting supply chains and vendors to maximize their impact. By compromising one service provider, attackers can access multiple organizations.In January 2024, a SolarWinds‐style attack on a major IT service provider affected multiple sectors. This attack involved inserting malicious code into software updates, which were then distributed to thousands of clients.
- **Identity‐Based Attacks** Identity threats have exploded, and attackers use sophisticated methods to steal or bypass authentication, including SIM‐swapping, MFA bypass, and API keys. The Scattered Spider group has been particularly active in this area. They've been using a combination of social engineering, phishing, and purchased credentials to gain rapid initial access to target systems. SIM swapping, also known as SIM hijacking, is a form of identity theft where attackers convince a mobile carrier to transfer a victim's phone number to a new SIM card controlled by the attacker. This allows them to intercept calls, text messages, and one‐time passwords sent to the victim's phone number, potentially bypassing two‐factor authentication on various accounts. Multifactor authentication (MFA) bypass refers to techniques attackers use to circumvent multi‐factor authentication systems. Standard methods include the following: API keys are secret tokens to authenticate and authorize access to APIs or Application Programming Interfaces. When these keys are stolen or leaked, attackers can do the following: Stolen API keys are particularly dangerous because they often grant high access levels and can be challenging to detect if misused. They're frequently targeted in attacks on developers and organizations, often by scanning public code repositories or intercepting network traffic.
  - Phishing attacks to trick users into revealing MFA credentials
  - MFA fatigue attacks, where users are bombarded with authentication requests
  - Session hijacking to take more than an active authenticated session
  - Exploiting vulnerabilities in MFA implementation or integration
  - Access sensitive data or functionality exposed by the API
  - Perform unauthorized actions on behalf of the legitimate user or application
  - In some cases, such as with cryptocurrency exchanges, they manipulate trades or withdraw funds

### Attack Vector Trends Takeaways

So, what do the attack vector trends mean for organizations and individuals? Well, consider these as they correlate with some of the best practices I'll review later in [Chapter 16](c16.xhtml):

- The importance of a robust, multilayered security approach has never been greater. This includes strong endpoint protection, network security, and cloud security measures.
- Employee training is crucial. With the rise of AI‐enhanced phishing and social engineering attacks, your staff must be more vigilant than ever.
- Identity and access management should be a top priority. Implement strong authentication methods and regularly audit access privileges.
- Cloud security needs special attention. Ensure your cloud configurations are secure and regularly audited.
- Have a solid incident response plan in place. In the event of an attack, you need to be able to respond quickly and effectively. Exercise this plan regularly to ensure success when the attack occurs.
- Stay informed about the latest threats and trends. The cybersecurity landscape is constantly evolving, and staying up to date is crucial for maintaining effective defenses.

## Malware Analysis for Digital Forensics Investigations

Next, before I discuss an actual incident in our case study, I'll walk through the key steps in malware analysis. This process is crucial for understanding how malicious software operates, as it is the root cause in the case study. It helps us develop better defenses and incident response strategies.

- **Preparation** Our first step is preparation, where I set up a secure, isolated environment for our analysis. I typically use virtual machines or sandboxes to contain the malware and prevent it from infecting our main systems. At this stage, I also gather our analysis tools, such as disassemblers, debuggers, and network monitoring software. Remember, safety first! Never run malware on production systems.
- **Static Analysis** Next, I move to static analysis, examining the malware without executing it. I look at things like file metadata, strings within the code, and the overall structure of the executable. Tools like PEiD can help us identify whether the malware is packed or obfuscated. Static analysis gives us our first clues about what the malware might do, but it's limited because many malware samples use sophisticated techniques to hide their true nature.
- **Dynamic Analysis** Dynamic analysis is where things get interesting. In dynamic analysis, I run the malware in our controlled environment. I watch how it behaves: what files it creates or modifies, what registry changes it makes, and what network connections it attempts. Tools like Process Monitor and Wireshark are invaluable here. This step often reveals behaviors that weren't apparent in static analysis.
- **Memory Analysis** After running the malware, I analyzed the system's memory. This can reveal hidden processes, injected code, and other artifacts that the malware leaves behind. Tools like Volatility are great for this. Memory analysis can be particularly useful for detecting sophisticated malware that tries to hide its presence on the system.
- **Network Analysis** With network analysis, I focus on the malware's network activity. I look at DNS queries, IP addresses they connect to, and the data types they send and receive. This can help us identify command‐and‐control servers, data exfiltration attempts, and other network‐based behaviors. Wireshark is a key tool in this step.
- **Reporting** Finally, I compile all my findings into a comprehensive report. This isn't just about documenting what I found; it's about providing actionable intelligence. I include IOCs, details about the malware's capabilities, and recommendations for detection and mitigation. This report becomes a valuable resource for our security teams and potentially for the broader security community.

Remember, malware analysis is often an iterative process. As I uncover new information, I might repeat these steps multiple times. It's like solving a puzzle, where each piece leads to new questions and new investigative areas.

### Key Tools and Challenges

Now, let's talk about essential tools, challenges in malware analysis, and some best practices to keep in mind. First, regarding tools in malware analysis, I broadly categorize them into four main types:

- Static analysis tools, like IDA Pro, Ghidra, pestudio, and Joe Sandbox allow us to examine malware without executing it. They're crucial for understanding the structure and potential behavior of malicious code.
- Dynamic analysis tools, such as Cuckoo Sandbox and Any.Run. These tools let us observe malware in action within a controlled environment. They're invaluable for understanding how malware behaves when it's running.
- Memory analysis tools, such as Volatility, help us examine the memory of infected systems. This can reveal hidden processes or data that might not be visible through other means.
- Network analysis tools like Wireshark. These are essential for monitoring and analyzing the network traffic generated by malware, helping us understand its communication patterns and potential command and control infrastructure.

However, malware analysis isn't without its challenges. I'm constantly up against challenges, such as the following:

- **Evolving malware techniques:** Cybercriminals constantly develop new ways to obfuscate their code and evade analysis. Techniques like anti‐analysis measures can make our job significantly more difficult.
- **Time constraints:** In cybersecurity, time is often of the essence. I frequently need to analyze malware quickly to prevent further damage or infection.
- **The sheer volume of new malware variants and families:** The volume makes keeping up with the latest threats a constant challenge that requires ongoing learning and adaptation.

To address these challenges and make the most of our tools, I follow some best practices:

- **Always maintain a secure and isolated analysis environment:** This is crucial to prevent accidental infections and to ensure our analysis doesn't impact production systems.
- **Regularly update our analysis tools and knowledge:** The threat landscape is constantly evolving, and so should our tools and skills.
- **Collaborate with other analysts and share threat intelligence:** While no one can keep up with every new threat alone, we can stay ahead of the curve by working together and sharing information.

Remember, malware analysis is as much an art as a science. It requires the right tools, up‐to‐date knowledge, and a methodical approach. By understanding these key tools, recognizing our challenges, and adhering to best practices, we can effectively analyze and combat the ever‐evolving malware threat.

### Findings of a Healthcare Security Event

We're all aware of many notable breaches and data compromises. Still, I'll focus on a simulated event with some peppered in forensics and remediation and then think about how many of those trends apply. I'll start with the basics. A security team was brought in to conduct an extensive analysis of a web browser build called Wave Browser. This software was involved in a breach that affected dozens of healthcare clinics.

The Wave Browser has mixed reviews because there are many versions or builds, and it is customizable for good or not‐so‐good. Some say it's safe, some say it's a potentially unwanted program (PUP) such as adware, and others say it's malware. It's not out there; it's primarily breaching networks or holding data for ransom. But that doesn't mean it's harmless. Overall, Wave Browser has been reported to facilitate unwanted pop‐up ads, create new tabs, redirect links, and modify browser settings. I would classify this behavior under two risk categories: Adware and Evader.

So, there were two versions of the Wave Browser in a production environment—the original and one after it was updated. Reverse engineering revealed some other concerns:

- The browser is connected to a domain that injects ads into search results. Malvertising has been reported in banner and other ads.
- Wave Browser used a software updater domain and was hosted on one of the world's leading cloud platforms.
- Wave Browser was able to be installed without elevated user rights or consent.

Now, let's talk about patient zero in the affected clinic network. How did Wave Browser get in?

The culprit was determined to be a malicious ad embedded in a phishing email. It's important to note that at the time of installation, a Windows 10 desktop had several n‐day vulnerabilities that made it an easy target since their patching cycle was 60 days. These included the following:

- A security feature bypass vulnerability allowing attackers to bypass Microsoft Office macro policies
- A remote code execution vulnerability in Microsoft Word
- A remote code execution vulnerability in the Windows Graphics Component
- A vulnerability in Windows Common Log File System that could allow attackers to achieve SYSTEM privileges

So, these vulnerabilities appear to have rolled out the red carpet for Wave Browser.

In a malware analysis, 55 sources were utilized, and only 4 flagged anything but safe. Two identified four files associated with Wave Browser as low‐to‐medium risk, categorizing them as potentially unwanted programs and two as malware.

Now, let's discuss what Wave Browser was doing on the network. Through sandboxing, reverse engineering, and disassembly, the browser was programmed to access a long list of domains and subdomains, including variations of `wavebrowser.com`, `wavebrowserbase.com`, and `mywavehome.net`.

If I rewind the clock and reiterate, the analysis revealed that Wave Browser first appeared in the environment two months before the investigation. It was installed on a desktop in a clinic and used by a nurse. The installation originated from personal web browsing and email use through an affected advertisement correlated with a low‐rated phishing attack that is assumed, based on some indicators, to have been crafted using AI.

The Wave Browser was also set as the default browser on this machine, and logs show that the user was accessing online applications via `office.com` and `office.net` using the browser. However, after the software was updated, logs indicated callouts and payloads pointed to China‐hosted known malware repositories. One final note is that at a point, bad actors also attempted to leverage known RMM software, in this case called Landesk, used by a partner to support eScreen readers on the nurses' desktops. The eScreen readers were used to assist in reading and processing electronic medical records, health documents, and test results.

### Technical Analysis

Let's dig into more of the technical analysis of the clinics and affected assets. At the time, and somewhat even today, the industry did not categorize the Wave Browser as a computer infection, Trojan horse, or a file encrypting malware that can impair computers. While the Wave Browser isn't reported as doing anything malicious, it has been reported as facilitating unwanted pop‐up ads, new tabs, page redirect links, and browser modifications.

I'll walk through a technical analysis of the incident, starting with the software and working my way into the injection point and malicious intent. I'll also discuss the real impact. As mentioned, the Wave Browser software behavior correlates with two cybersecurity risk classification categories: *Adware* and *Evader* and *PUP with Adware and Browser Hijacker Characteristics*.

Reverse engineering of the software depicts the behavior of a connection to `api.wavebrowserbase.com`, which injects ads into web search results. It is important to note that the Wave Browser can be installed without elevated user privileges or user consent. This is an extract from the Joe Security platform analysis. You can search their website for detailed reports on the Wave Browser.

**Behavioral Analysis:**

- **Process manipulation**:
  - Creates threads in other processes (thread injection).
  - Creates processes in suspended mode, likely for code injection.
  - These behaviors are often associated with malware attempting to hide its activities.
- **Anti‐analysis techniques**:
  - Attempts to detect debuggers and virtual machines.
  - Contains functionality for execution timing checks.
  - These are common evasion tactics used by malware to avoid detection and analysis.
- **Data harvesting**:
  - Tries to harvest browser information (history, passwords).
  - Contains capabilities for clipboard reading.
  - This suggests potential privacy and security risks for users.
- **System control**:
  - Can launch processes as different users.
  - Has system shutdown/reboot functionality.
  - These capabilities could be used for legitimate purposes but also malicious activities.

These characteristics, especially the invalid checksum and nonstandard sections, often indicate potentially malicious software.

Network activity also suggests potential command‐and‐control communication or data exfiltration with ingress and egress to locations in China. While this does not directly address “ChinaNet,” it illustrates a pattern of cyber activities associated with some bad actors in China. These activities involve malware, vulnerability exploitation, and attempts to compromise critical infrastructure and communication networks. The activities range from pre‐installed malware on hardware to sophisticated state‐sponsored cyber operations targeting various sectors.

I mentioned that clinics have eScreen reader devices that communicate with the `escreen.com` domain, which a third party manages. However, this traffic correlates with the Wave Browser events from a timeframe perspective, which could indicate attackers may have tried to leverage the platform. These included unencrypted pages that allow for the download and installation of the LANDesk agents (for remote control) without any form of authentication. There's also a link to a console that pulls in an authentication form.

A note about next generation security information and event management (SIEM) platforms. I mentioned them in previous chapters, but know that they significantly enhance digital forensics investigations in the following ways:

- **Comprehensive data collection:** Next‐gen SIEMs collect and centralize data from various sources across an organization's IT infrastructure, providing investigators with a holistic view of the environment.
- **Advanced analytics:** These platforms use machine learning and AI to detect anomalies and patterns that might indicate a security incident, helping investigators focus on relevant data.
- **Automated attack timelines:** Next‐gen SIEMs can automatically piece together elements of an attack and present them on a visual timeline, speeding up the investigation process.
- **User and entity behavioral analytics (UEBA):** By establishing baselines of regular activity, these systems can highlight suspicious behaviors that may be part of an attack.
- **Rapid search and correlation**: Investigators can quickly search through large volumes of data and correlate events across different systems, aiding in root cause analysis.
- **Forensic data preservation:** Next‐generation SIEMs often include features to ensure the immutability of collected data, which is crucial for maintaining the integrity of evidence.
- **Incident reconstruction:** These platforms can help reconstruct the sequence of events leading up to and following a security incident.
- **Integration with threat intelligence:** Next‐gen SIEMs can provide context to potentially malicious activities by incorporating up‐to‐date threat intelligence.
- **Automated reporting:** They can generate detailed reports that can be used as evidence in investigations or for compliance purposes.

By leveraging these capabilities, digital forensics investigators can conduct more thorough and efficient investigations, uncovering evidence that might be missed with traditional methods. In this case, I'm focusing on Rapid7 InsightIDR, a platform I'm very familiar with, which can create forensics reporting in many ways, including the following:

- **Comprehensive data collection:** InsightIDR collects data from various sources across an organization's IT infrastructure, including endpoint devices, authentication logs, and network security tools.
- **Unified data view:** The platform aggregates and normalizes data, attributing events to specific users and assets, providing a holistic view of the environment.
- **Automated investigation timelines:** InsightIDR automatically creates detailed, visual investigation timelines for each alert, correlating events across different data sources.
- **Endpoint forensics:** The Insight Agent allows real‐time endpoint scanning and collecting forensic data such as running processes, DNS cache, installed services, and registry keys.
- **Log analysis:** InsightIDR enables searching and analyzing raw logs, which can be added to investigations for context.
- **UEBA**: The platform uses behavioral analytics to detect anomalies and suspicious activities.
- **Customizable reporting:** Users can generate detailed reports on threat trends and the overall effectiveness of the security team.
- **Integration with DFIR tools:** For advanced forensic capabilities, InsightIDR Ultimate integrates with Velociraptor, a Digital Forensics and Incident Response (DFIR) tool.
- **Automated response actions:** The platform supports automation workflows for actions like quarantining assets or creating tickets, which can be included in forensic reports.
- **Data export:** InsightIDR allows for exporting of investigation data, enabling the creation of customized forensic reports.

By leveraging these features, InsightIDR enables security teams to create comprehensive forensic reports that include detailed timelines, endpoint data, log analysis, and behavioral insights. These reports provide a thorough overview of security incidents for investigation and compliance purposes.

The framework approach monitors all devices spanning to the edge and sends logs, vitals, running processes, and traffic to a local collector. The collector will securely send data for analysis that federates alarms to folks. This is a synopsis of key steps to take when running a digital forensics investigation using a log analysis tool:

1. **Identification and preservation:**
  1. Identify all relevant log sources (servers, applications, network devices, etc.)
  2. Ensure logs are preserved and secured to maintain chain of custody
  3. Create forensic copies/images of log data to work from
2. **Collection:**
  1. Ingest logs into the log analysis tool
  2. Verify data integrity during ingestion
  3. Apply any necessary parsing or normalization to standardize log formats
3. **Analysis:**
  1. Use the tool's search and filtering capabilities to identify relevant events
  2. Look for indicators of compromise or suspicious activity patterns
  3. Correlate events across different log sources to build a timeline
  4. Apply any built‐in threat detection or anomaly detection capabilities
  5. Use visualization features to identify trends or anomalies
4. **Documentation:**
  1. Document all steps taken during the investigation
  2. Record search queries used and results obtained
  3. Capture screenshots of relevant findings
  4. Maintain an audit trail of all investigative actions
5. **Reporting:**
  1. Use the tool's reporting capabilities to generate investigation summaries
  2. Include key findings, timelines, and supporting evidence
  3. Ensure reports are clear and understandable for non‐technical stakeholders
6. **Presentation:**
  1. Prepare visualizations or dashboards to present findings
  2. Be ready to explain the methodology and tools used
  3. Ensure all presented evidence maintains integrity and chain of custody

Strict access controls must be maintained throughout the process on the log data and investigation results to preserve confidentiality and integrity. The log analysis tool should provide features to support each of these steps in a forensically sound manner.

Another benefit of InsightIDR is its centralized deception technology. This allows us to create an illusion for attackers that they have found something of interest within our customer's environment. When intruder traps are deployed on a network, they act as a virtual trip wire. Once an attacker is tricked into touching the trap, InsightIDR fires an alert to our team.

So why is this useful? Some stealthy attacks can be difficult to discern from regular activity, allowing attackers to sneak past security controls. Distracting intruders by placing traps often helps us find them earlier and take action to block them.

In conclusion, Wave Browser and the folks from China didn't cause catastrophic damage in the scenario, as it was detected and mitigated just after updating. Those connections serve as a wake‐up call. They remind us that threats can come in many forms, and even seemingly benign software can pose significant risks to our networks and data.

Among a long list of recommendations, for brevity, the organization would implement stricter controls on personal web use, enhance email filtering, conduct more frequent vulnerability assessments, and ensure assets are patched within 30 days of release after an upgrade to Windows 11. The customer would also implement GEO blocking and start doubling down on user education because, as this incident shows, the users were the first line of defense and the weak link.

### Post‐Event Lessons Learned

This simulated case highlights many of the severe consequences of cybersecurity breaches in healthcare, affecting not only the financial stability of organizations but also the quality and continuity of patient care and the overall trust in the healthcare system. Here is an overview of the average (some say on the low side) financial and human impacts on healthcare organizations from the example:

- **Financial Impacts:**
  - Direct cost is approximately $300,000.
  - Lost revenue due to service disruptions and operational downtime for weeks.
  - Increased cybersecurity insurance premiums can rise by approximately 26%.
- **Human Impacts:**
  - Disruption to patient care includes delayed treatments, surgeries, and inability to access and transfer some patient records.
  - Stress and increased workload for healthcare and IT staff dealing with the aftermath of attacks and implementing workarounds.
  - Some reported job losses are likely due to organizational financial and operational strain.
  - The erosion of trust between some affected patients and the healthcare provider could lead to patients avoiding or delaying necessary care.
  - Delayed advancements in patient treatments and therapies.

## Key Takeaways from Hospital Network Breaches with IoMT Devices

This chapter highlights the urgent need for a multilayered, proactive approach to securing IoMT devices and healthcare networks. Lessons from past breaches serve as a roadmap for preventing future incidents and safeguarding healthcare systems. While IoMT has significantly improved patient care through technologies like infusion pumps, patient monitors, and imaging systems, these advancements also introduce substantial cybersecurity risks. The interconnected nature of these devices creates a broad attack surface, making them prime targets for cybercriminals. Many IoMT devices operate with outdated software, unpatched vulnerabilities, and weak security features, such as default credentials and insufficient encryption, exposing them to exploitation.

One critical risk is poor network segmentation, which allows attackers to move laterally across hospital systems after compromising a single IoMT device. Flat network structures connect critical systems, such as electronic health records and imaging devices, making them accessible from a single breach point. Additionally, human error, including weak password practices and falling victim to phishing attacks, remains a major factor in cybersecurity incidents. Insider threats, whether intentional or accidental, further increase the risk of system compromises.

The rise of publicly accessible IoMT devices has expanded the attack surface, exposing them to external scanning and exploitation. Cybercriminals increasingly employ sophisticated tactics such as ransomware and man‐in‐the‐middle attacks to target these vulnerable systems. Attacks typically progress through multiple stages, including reconnaissance, penetration, privilege escalation, data exfiltration, and persistence, emphasizing the need for early threat detection. Case studies, such as ransomware attacks on healthcare institutions and third‐party vendor breaches, illustrate the devastating impact of IoMT vulnerabilities, leading to operational disruptions, data breaches, and financial losses. Beyond monetary damages, cyberattacks delay surgeries, disrupt patient care, and erode public trust in healthcare providers.

To address these risks, healthcare organizations must implement strategic defense measures. Network segmentation can help isolate IoMT devices from critical systems, reducing the potential attack surface. Timely patching, updates, and strong collaboration with manufacturers are essential for mitigating vulnerabilities. Advanced detection and response mechanisms, including intrusion detection systems and anomaly detection, can identify and neutralize threats proactively. Continuous cybersecurity education for healthcare staff is crucial in minimizing human error, while vendor accountability ensures that third‐party providers uphold stringent security standards.

A proactive approach to threat management, integrating IOAs with IOCs, enables healthcare organizations to detect, respond to, and prevent cyber threats more effectively. Emerging technologies, such as deception techniques, behavioral analytics, and centralized monitoring, further enhance security. Ultimately, securing IoMT devices requires collaboration between healthcare providers, device manufacturers, cybersecurity experts, and regulatory agencies. By adopting industry best practices, including secure‐by‐design principles and zero‐trust architectures, the healthcare sector can significantly reduce cybersecurity risks and ensure the safety and integrity of connected medical devices.
