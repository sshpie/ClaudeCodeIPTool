# CHAPTER 7  
Replay and Spoofing Attacks in IoMT

Patient care has been modernized with real‐time monitoring, automated treatments, and seamless data exchange. Devices like infusion pumps, heart monitors, and insulin delivery systems are now integral to clinical workflows, improving efficiency and patient outcomes. However, this growing reliance on connected medical devices introduces cybersecurity challenges, particularly in the form of replay and spoofing attacks. These attacks exploit vulnerabilities in device communication and authentication.

Replay attacks occur when an adversary intercepts and records legitimate data transmissions, such as medication commands, patient vitals, or authentication tokens, and later replays the data to deceive the receiving system. The system, unable to distinguish between genuine and replayed transmissions, may act on outdated or falsified instructions, potentially causing life‐threatening consequences for patients. For instance, replaying an old configuration command to an infusion pump could administer an incorrect medication dosage, while replaying vital sign data from a heart monitor could mask a patient's deteriorating condition.

On the other hand, spoofing attacks involve attackers impersonating legitimate devices, systems, or users to gain unauthorized access or manipulate medical operations. By mimicking trusted devices or communication endpoints, attackers can inject false data, mislead healthcare providers, or even enter critical systems. A spoofed glucose monitor, for example, could send falsified readings to an insulin pump, leading to improper insulin administration. Likewise, a rogue device could impersonate a legitimate system on the network, exfiltrating sensitive patient information or disrupting care delivery.

Replay and spoofing attacks exploit critical vulnerabilities within IoMT ecosystems, such as weak encryption, outdated authentication mechanisms, and insecure device pairing. Legacy systems, insufficient device security, and the complex operational demands of healthcare environments often exacerbate these vulnerabilities.

The implications of these attacks are far‐reaching. Beyond immediate risks to patient safety, replay and spoofing attacks can compromise the integrity of diagnostic data, erode clinician trust in connected systems, and result in operational disruptions or regulatory violations. In a sector where every second counts, the consequences of inaccurate data, delayed responses, or compromised devices can be catastrophic.

To safeguard healthcare systems and protect patient lives, it is imperative to understand how replay and spoofing attacks occur, identify the vulnerabilities they exploit, and implement mitigation strategies. This chapter will explore these attacks and provide insights into their real‐world implications and potential exploits in healthcare environments. Additionally, it outlines practical defense strategies to build more resilient IoMT ecosystems.

## Understanding Replay Attacks in IoMT

As mentioned, a replay attack is a deceptive cyberattack in which an adversary intercepts legitimate data transmissions between two devices or systems, stores that data, and replays it later. The goal is to trick the receiving system into believing the message or data is genuine, leading to unauthorized actions, disruption, or manipulation of the system. These attacks exploit the fact that many systems trust the incoming data without verifying its timeliness or the integrity of the source.

Replay attacks present a significant threat to healthcare within the IoMT ecosystem. Medical devices such as infusion pumps, heart rate monitors, and insulin delivery systems rely on real‐time communication with centralized systems or mobile applications. If this communication is intercepted and replayed, it can compromise patient health, the integrity of the data transmitted, and the efficiency of a healthcare system's operations.

## How Replay Attacks Work in IoMT Systems

Replay attacks in IoMT systems start with capturing device communications. Attackers begin by positioning themselves within the communication pathway of devices. This is typically achieved through packet sniffing, which uses specialized software to intercept and log network traffic, and MITM attacks (discussed in [Chapter 6](c06.xhtml)), which insert themselves between the medical device and its intended recipient. The attacker then captures legitimate data exchanges, such as the following:

- Vital sign transmissions (e.g., heart rate, blood oxygen levels) from patient monitors to nursing stations
- Configuration commands sent to devices for medication dosage control
- Authentication tokens or session identifiers to establish secure connections

Once the attacker has captured valid communications, they can replay this data later. The replayed data often appears legitimate because it matches a previously valid transmission. Many IoMT systems may lack timestamp verification or nonce (number used once) mechanisms, making them vulnerable to accepting outdated commands.

There are many examples of replay attack consequences, but here are two of the most common:

- Replaying an outdated command could lead to incorrect dosage administration.
- Resending old diagnostic data might cause healthcare systems to display inaccurate patient readings, potentially leading to misdiagnosis.

An additional consideration is timing. Attackers may wait for specific moments to replay data, such as during shift changes when vigilance might be lower. They might also choose to replay only certain parts of captured communications to achieve specific malicious goals. Additionally, replay attacks can be used with other techniques, like spoofing or injection attacks, to create more complex and harder‐to‐detect threats.

## Implications of Replay Attacks in Healthcare

As described, replay attacks in healthcare involve intercepting and replaying previously transmitted data, often maliciously, to manipulate medical devices or systems. I’ll explore the implications in more detail. Patient safety risks are among the most concerning outcomes of replay attacks, especially when critical medical devices are targeted.

Medication delivery devices like infusion pumps are vulnerable to attackers who can replay instructions to administer repeated or incorrect dosages. This could lead to life‐threatening overdoses or ineffective treatments, particularly for patients relying on medications like insulin or chemotherapy drugs. Similarly, implantable devices, such as pacemakers and cardioverter‐defibrillators or ICDs, can be manipulated to alter heart rhythms, deliver unnecessary shocks, or disable critical alarms. Such interference could result in immediate harm or even death. Patient monitors in high‐acuity environments, such as ICUs, are also at risk. Replay attacks could mask deteriorating conditions by displaying outdated, stable readings or generate false alarms that trigger unnecessary interventions, delaying responses to actual emergencies.

Data integrity and diagnostic errors present another layer of risk. Replay attacks can compromise diagnostic tools by injecting outdated imaging results, such as X‐rays or MRIs, leading to missed diagnoses or delayed treatments for progressing conditions. Laboratory systems with replayed test data might produce inaccurate reports, impacting clinical decisions. Additionally, electronic health records can be corrupted when old data packets overwrite recent updates, resulting in errors like incorrect medication orders, overlooked allergies, or outdated treatment plans. Even clinical decision support systems, which rely on real‐time inputs, can be manipulated to suppress critical alerts or trigger inappropriate warnings, undermining the reliability of automated assistance.

The operational disruption caused by replay attacks can also strain healthcare facilities. Device malfunctions are common, with compromised devices freezing, crashing, or behaving erratically, leading to downtime and costly repairs. Attackers can also replay emergency signals, creating false alarms that overwhelm staff with unnecessary alerts, potentially leading to alarm fatigue, where legitimate emergencies are ignored. Additionally, network congestion caused by large‐scale replay attacks can flood hospital networks, slowing down systems like EHRs or Picture Archiving and Communication Systems (PACS), essential for accessing real‐time diagnostic images and patient data. Scheduling and resource management systems are not immune, either. Replay attacks can introduce old appointment or resource allocation data, resulting in double‐booked operating rooms, overcommitted diagnostic equipment, and inefficient staffing schedules that delay patient care.

## Use Case of a Replay Attack on an Infusion Pump

An advanced wireless infusion pump system that delivers precise doses of pain medication to patients could be a good use case in a hospital setting. The pumps communicate with a central control system, allowing authorized medical staff to adjust medication dosages remotely.

- **Attack Execution Steps**
  1. **Interception****:** An attacker posing as a visitor uses a concealed radio frequency (RF) scanner to capture wireless communications between the central system and infusion pumps.
  2. **Data Capture****:** The attacker intercepts a legitimate command to increase morphine dosage for a post‐operative patient from 2mg/hour to 5mg/hour.
  3. **Analysis****:** The attacker uses specialized software to decode the captured data packet, identifying the command structure and authentication tokens.
  4. **Replay****:** The attacker replays the intercepted command multiple times over the next hour using a small, disguised transmitter.
- **Impact**
  - The infusion pump receives and executes each replayed command, incrementing the dosage by 3mg/hour each time.
  - Within an hour, the patient's morphine dosage has increased to dangerous levels (e.g., 20mg/hour).
  - The patient experiences severe respiratory depression, requiring emergency intervention.
- **Detection and Response**
  - A nurse notices the patient's deteriorating condition during routine checks.
  - The discrepancy between the prescribed dosage and the pump's output is discovered upon investigation.
  - The hospital's IT security team is alerted and begins analyzing network logs, identifying the repeated, identical commands.
- **Consequences**
  - **Patient safety****:** The patient suffers potentially life‐threatening complications due to opioid overdose.
  - **Operational disruption****:** The ICU implements manual medication administration procedures while investigating the wireless system.
  - **Reputational damage****:** News of the security breach erodes patient trust in the hospital's technology.
  - **Regulatory penalties**: The hospital faces fines for violating HIPAA security rules and FDA guidelines on medical device cybersecurity.
  - **Financial impact****:** Costs include potential litigation, cybersecurity upgrades, and extended patient care due to the incident.

This case study demonstrates the critical importance of implementing security measures for wireless medical devices, including strong encryption, authentication, and anomaly detection systems to prevent and rapidly identify replay attacks.

## Other Examples of Replay Attacks in IoMT

Some additional examples of replay attacks on IoMT devices include:

- **Heart rate monitor manipulation****:** Attackers could intercept data transmitted from a wearable heart rate monitor and replay old, stable readings to healthcare providers, preventing the system from detecting critical changes in a patient's cardiac health.
- **Remote pacemaker attack****:** A malicious actor could intercept and replay old commands to a pacemaker, causing the device to deliver incorrect pacing commands to a patient's heart.

## Strategies for Mitigation of Replay Attacks

Given the life‐and‐death nature of healthcare operations, defending against replay attacks requires a comprehensive, multilayered security strategy that addresses technical vulnerabilities and operational safeguards. I'll discuss these more in [Chapter 16](c16.xhtml) on best practices, but this section provides an overview focusing on reducing the risk of replay attacks.

Implementing strong encryption serves as the foundation for secure communication across medical devices and networks. Healthcare organizations should adopt modern encryption standards, such as TLS 1.3, to protect data in transit, ensuring that information exchanged between devices remains confidential and tamper‐proof. End‐to‐end encryption should be prioritized to safeguard data from the point of origin to its destination, minimizing the risk of interception. Regular audits and updates to encryption algorithms must be part of routine security practices, as they address newly discovered vulnerabilities. Secure key management, including frequent key rotation and proper storage, further strengthen encryption defenses.

Utilizing nonces and timestamps in communication protocols adds another layer of protection against replay attacks. Nonces, which are random numbers used only once, prevent attackers from successfully replaying old messages because each session generates a new identifier. Similarly, timestamps help verify the freshness of transmitted data by enforcing time limits for validity. Nonces and timestamps provide a robust mechanism for validating communication sessions, reducing the risk of unauthorized message reuse. Implementing strict validation processes for these features ensures attackers cannot bypass them.

Mutual authentication is another critical defense, ensuring that the communicating devices and systems verify each other's identities before exchanging data. Healthcare organizations should deploy certificate‐based authentication using PKI to establish trust between devices. Multifactor authentication (MFA) further enhances security, particularly for accessing critical systems. Regularly rotating and revoking authentication credentials adds another layer of protection, while device attestation helps verify that devices remain uncompromised and trustworthy during operation.

IDS plays a vital role in identifying replay attacks in real time. Network‐based IDS can monitor traffic patterns across medical device networks to detect anomalies, while host‐based IDS focuses on individual devices to flag suspicious activity. Advanced tools that leverage machine learning algorithms can enhance detection capabilities by recognizing subtle attack patterns that traditional methods might miss. Integrating these systems into an SIEM platform streamlines monitoring and provides actionable insights for security teams to respond quickly to threats.

Regular device updates and patch management are essential to addressing vulnerabilities in medical devices and associated software. Healthcare organizations should establish strict patch management policies and work closely with vendors to ensure the timely delivery of security updates. Before deployment, updates must be rigorously tested in a controlled environment to avoid unintended disruptions. Automated update mechanisms for devices that support it can further simplify this process while ensuring systems remain up to date against evolving threats.

Securing IoT medical devices, particularly those used in healthcare, such as remote monitors and implantable devices, requires vendor collaboration to implement security‐by‐design principles. Devices must include built‐in encryption, secure communication protocols, and secure provisioning processes during onboarding. Network segmentation can further reduce risk by isolating IoT devices from critical systems, limiting the impact of a potential breach.

## What Is a Spoofing Attack in IoMT?

Spoofing attacks in the IoMT exploit the trust relationships between devices, systems, and users in healthcare environments. I’ll examine three types of spoofing attacks, explaining how they work and their potential impacts:

- **Device spoofing****:** Attackers may create a rogue device that mimics the identity of a legitimate medical device, such as an infusion pump or patient monitor. This fake device could broadcast the same Bluetooth Device Address (BD_ADDR) as the legitimate device, tricking other systems into connecting. Once connected, the attacker could intercept sensitive patient data or inject false information into the healthcare network.
- **Data spoofing****:** In this attack, the attacker intercepts and modifies data packets transmitted between IoMT devices. For example, an attacker could alter the readings from a glucose monitor before they reach the insulin pump, potentially causing incorrect insulin dosages. This attack exploits vulnerabilities in the communication protocols IoMT devices use, particularly if they lack strong encryption or authentication mechanisms.
- **User spoofing****:** Attackers may impersonate healthcare providers by stealing or guessing login credentials. They could then access EHR systems or medical devices, potentially altering patient data or device settings. This type of spoofing often relies on social engineering tactics or weak authentication protocols in healthcare systems.

Malicious actors might execute these attacks by exploiting weaknesses in the Bluetooth pairing process or vulnerabilities in older encryption protocols. Although Bluetooth's Frequency‐Hopping Spread Spectrum (FHSS) can make these attacks more challenging, determined attackers may still find ways to synchronize with the target device's hopping sequence.

### How Spoofing Attacks Exploit IoMT Vulnerabilities

Spoofing attacks in the IoMT usually exploit critical security vulnerabilities, targeting gaps in authentication, communication, and device configuration. These attacks enable adversaries to impersonate legitimate devices, users, or systems within healthcare networks, leading to compromised patient safety, data breaches, and operational disruptions. In this section, I'll explain how these vulnerabilities are commonly exploited.

#### *Weak Authentication*

One of the most significant vulnerabilities that spoofing attacks exploit is the reliance on weak or outdated authentication mechanisms by IoMT devices and healthcare systems. This happens for several reasons. For example, many IoMT devices are shipped with default credentials (e.g., username: “admin,” password: “1234”) that are rarely changed, providing attackers with easy access. In addition, some systems do not support or are not in line with MFA. These systems rely solely on passwords, which can be brute‐forced, guessed, or stolen in phishing attacks. Some legacy devices lack any form of authentication, enabling attackers to connect directly and impersonate the device without credentials.

An example of exploitation is when an attacker spoofs a glucose monitor by connecting to the network using stolen credentials. Once connected, they could send falsified data to the healthcare system, causing clinicians to make incorrect decisions, such as administering unnecessary or harmful insulin doses.

#### *Lack of Secure Communication Protocols*

IoMT devices often use insecure or outdated communication protocols, leaving them vulnerable to data interception and manipulation. These weaknesses enable attackers to inject fake data or impersonate devices on the network. This occurs when there exists unencrypted communication. For example, some IoMT devices transmit data in plaintext or use deprecated encryption protocols like SSL or older versions of TLS, which can be easily intercepted and modified. Insufficient validation is another issue where devices may fail to validate the authenticity of incoming data packets, making them susceptible to data injection attacks. Also, consider what I explained in [Chapter 6](c06.xhtml) about MITM attacks. Attackers intercept communications and insert themselves between a medical device and its control system, relaying and modifying data to impersonate the device.

As an example of exploitation, a spoofing attack on a cardiac monitor could involve an attacker injecting fake heart rate readings into the communication stream. Clinicians relying on this data might miss signs of cardiac distress, delaying critical interventions.

#### *Insecure Device Pairing*

IoMT devices often rely on pairing processes to establish secure communication. However, these processes are frequently implemented with weak security practices, leaving them vulnerable to spoofing attacks. These are three common causes of how this happens:

- **Default pairing credentials****:** Devices often use factory‐default PINs or passwords during pairing, which are easily guessable or available online.
- **Weak pairing protocols****:** Some IoMT devices use outdated pairing protocols that lack proper encryption or authentication, making it easy for attackers to impersonate devices during the pairing process.
- **Broadcast discovery****:** Devices in discoverable mode may respond to pairing requests indiscriminately, allowing attackers to initiate unauthorized connections.

As an example of exploitation, an attacker could spoof a telemetry device during the pairing process, gaining unauthorized access to sensitive patient data or sending false readings to the control system. For example, an infusion pump configured via insecure pairing could be manipulated to alter medication dosages.

#### *Insufficient Device Hardening*

IoMT devices are often designed with functionality as a priority, leading to insufficient security measures that attackers can exploit to carry out spoofing attacks. This can happen because some devices have hardcoded user credentials that cannot be changed, making them easy targets for spoofing.

There's also an issue with unused open ports. Some devices may have open communication ports that attackers can exploit to gain unauthorized access. Furthermore, I've seen legacy devices with firmware vulnerabilities in the field that allow attackers to modify device behavior and impersonate legitimate systems. For example, an attacker might exploit an open port on a ventilator to inject malicious commands, forcing the device to behave erratically or send false telemetry data to the central monitoring system.

#### *Lack of Network Segmentation*

Among this book's common themes is the lack of proper network segmentation in healthcare environments. Without segmentation, attackers can move laterally within the network, increasing the scope and impact of spoofing attacks. Without segmentation, all devices share the same network, allowing attackers who spoof one device to access others. Devices may also be configured to communicate with any system on the network, making it easier for spoofed devices to interact with critical systems.

A spoofed device, such as a mobile health monitoring app, could send falsified commands to other connected devices on the same network segment, disrupting multiple systems simultaneously.

### Real‐World Implications of Spoofing Attacks

Spoofing attacks targeting IoMT devices pose significant threats in healthcare environments, leading to potentially devastating outcomes. Falsified data or malicious commands can result in misdiagnoses, inappropriate treatments, or device malfunctions, jeopardizing patient health and lives. Data breaches are another serious consequence, with attackers impersonating legitimate devices to steal sensitive patient information.

Such incidents violate privacy laws and regulations, such as HIPAA, and can result in financial penalties and long‐lasting reputational damage for healthcare organizations. Additionally, operational disruptions caused by spoofed devices can compromise the functionality of essential medical equipment, leading to unexpected system outages, treatment delays, and interruptions in critical patient care.

## Mitigation Strategies for Spoofing Attacks in IoMT

Defending against spoofing attacks requires more than standard cybersecurity measures. It requires a multilayered approach that addresses vulnerabilities head‐on. To bring this topic to life, I’ll break down the key strategies for keeping these systems secure and provide some real‐world examples.

I’ll start with encryption, the first and most critical defense. Imagine a heart monitor transmitting a patient's vitals to a nurse's station. If that data isn't encrypted, an attacker could intercept it, alter the readings, or even inject false data, potentially leading to a misdiagnosis or harmful treatment. This is where AES‐256 encryption and TLS 1.3 protocols come in. These technologies ensure that even if someone manages to capture the data, they won't be able to read or modify it. Hospitals should also implement Mutual TLS (mTLS), which requires both the device and the server to verify each other's identities before sharing information, like a secret handshake to confirm they're talking to the right partner. Implementing mutual authentication between devices and servers is crucial for preventing man‐in‐the‐middle attacks and ensuring the integrity of communications.

Next up is authentication and access control. Think about an infusion pump administering medication to a patient. What if an attacker impersonated the pump to change the dosage? That's where MFA and certificate‐based authentication step in. By requiring multiple verification forms, like a password and a digital certificate, devices can prove their identity before connecting to the network. For example, a hospital using PKI certificates ensures that only authorized devices can access the network, making it virtually impossible for attackers to spoof a device without the correct credentials.

Another essential layer of protection is timestamps and sequence numbering. Picture this: a telemetry monitor transmitting a patient's vitals every minute. An attacker captures and replays old data to trick the system into believing the patient is stable when their condition deteriorates. By embedding timestamps and sequence numbers into each data packet, the system can detect and reject any message that's out of order or too old, protecting patients from harmful delays or false alarms.

Next is secure device pairing. Pairing is how devices like glucose monitors or infusion pumps connect to mobile apps or servers. If this process isn't secure, attackers can intercept the pairing attempt and take control of the device. Using Elliptic Curve Diffie‐Hellman (ECDH), as mentioned in [Chapter 4](c04.xhtml), key exchanges and disabling factory‐default PINs ensure that the pairing process is encrypted and resistant to tampering. For example, when a glucose monitor pairs securely with its app using encrypted credentials, it prevents attackers from hijacking the setup process and manipulating data.

Regular updates and patch management are other key defenses mentioned throughout this book. Outdated firmware is like unlocking the front door, inviting attackers to exploit known vulnerabilities. Hospitals should set up automated patch management systems to update devices without delays. Take this example after discovering a Bluetooth vulnerability. A hospital deployed a firmware update for its patient monitors, closing the security gap and preventing attackers from spoofing devices.

Network segmentation and isolation also play critical roles. Consider separating medical devices into locked rooms rather than leaving them all in one big open space. Virtual LANs prevent attackers from moving laterally across the network, limiting their ability to reach sensitive systems like electronic health records. Imagine infusion pumps isolated on a dedicated VLAN; an attacker who compromises one pump wouldn't be able to access patient databases or disrupt other devices.

Real‐time monitoring is the next layer of defense. Hospitals can deploy IDS and AI‐driven anomaly detection tools to catch unusual patterns before they escalate. For instance, an IDS might detect multiple failed connection attempts to a vital signs monitor, flagging them as potential spoofing attempts. These systems can then automatically quarantine the suspicious device, stopping the attack.

Finally, let's not forget the human element with training and awareness. Technology alone isn't enough. Healthcare staff need to know how to spot the signs of spoofing, like duplicate readings or devices behaving erratically. For example, a nurse noticing inconsistent vitals from a patient monitor can immediately report it to IT, allowing them to investigate and neutralize the threat. Regular training sessions and clear incident reporting protocols empower staff to act quickly and decisively in emergencies.

## Key Takeaways of Replay and Spoofing Attacks in IoMT

This chapter explored the growing cybersecurity threats in the IoMT, focusing on replay and spoofing attacks. While IoMT has revolutionized healthcare through real‐time monitoring and automated care, it also introduces significant security risks that can jeopardize patient safety and disrupt medical operations.

Replay attacks occur when malicious actors intercept and retransmit legitimate communications to deceive IoMT systems. This can have serious consequences, such as outdated insulin pump commands being replayed to administer incorrect doses or delayed identification of critical conditions due to manipulated patient vitals. Similarly, spoofing attacks involve an attacker impersonating trusted devices, systems, or users to gain unauthorized access or manipulate operations. Weak authentication and insecure communication channels enable these attacks, leading to falsified glucose readings, exfiltration of sensitive PHI, or disruptions in life‐saving medical procedures.

Several vulnerabilities contribute to the success of these attacks, including weak authentication mechanisms, insecure communication protocols, flaws in device pairing, unsegmented networks, and outdated firmware. These weaknesses expose healthcare systems to risks such as compromised patient safety, manipulated medical data, operational downtime, and potential regulatory violations, which can result in severe financial and reputational consequences.

To mitigate these threats, healthcare organizations must implement robust security measures, including encrypting communications with AES‐256 and TLS 1.3, enforcing multifactor authentication, deploying timestamps and nonces to prevent replay attacks, and securing device pairing with encrypted protocols. Regular software updates, network segmentation, and advanced monitoring systems can enhance security by detecting and responding to real‐time anomalies. Additionally, staff training is crucial in recognizing irregular device behavior and reinforcing best practices for secure device management.

Real‐world incidents underscore the urgency of these security concerns. Replay attacks on infusion pumps have led to dangerous overdoses, while spoofing attacks on cardiac monitors have injected false readings, misleading clinicians and delaying critical care. However, AI‐driven monitoring and multilayered defense strategies have shown promise in detecting and mitigating such threats before they escalate.

Ultimately, securing IoMT devices requires a proactive, multifaceted approach integrating strong encryption, authentication, network protections, and continuous monitoring. Collaboration with vendors to ensure secure‐by‐design devices and timely updates is essential, as is fostering cybersecurity awareness among healthcare professionals. By prioritizing these measures, healthcare organizations can safeguard patient data, uphold regulatory compliance, and reinforce trust in the integrity of medical technology.
