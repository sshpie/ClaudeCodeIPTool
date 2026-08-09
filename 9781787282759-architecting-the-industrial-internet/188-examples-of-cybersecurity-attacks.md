# Examples of cybersecurity attacks

The introduction of sensors and control systems on factory floors and in other Industrial Internet settings and their networking enabled the collection and analysis of big data, revolutionizing automation techniques and making manufacturing processes smarter. However, the growing frequency of cybersecurity attacks has now led to a growing focus on counter measures.

Today, most studies rank security concerns as a priority in IIoT implementations. This has been true for many years. A Gartner study from this year listed security concerns as the top *Barriers to IoT Success*. In a Morgan Stanley Automation World Survey in 2015, over 40 percent of the manufacturers rated cybersecurity as their top concern in IIoT adoption, outranking the lack of standardization, challenges presented by their legacy installed base, the need for significant upfront investments, lack of skilled workers, data integrity challenges, internal system barriers, liability of current technologies, and social and political concerns.

Given this focus, architects designing IIoT solutions must often deal with questions such as:

- What risk might be introduced by Industrial Internet solutions to the existing systems?
- How can sensitive data be protected during the information technology and operational technology integrations across multiple systems?
- How is data separated across the multiple tenants in public cloud solutions?

For example, in a manufacturing setting, IIoT attackers often try to intrude into SCADA systems. They tend to exploit the software vulnerabilities prevalent in **Human Machine Interfaces** (**HMIs**). Often, a human operator controls a SCADA system through the HMI installed in a network-enabled location. Ideally, the HMI should only be installed on an air-gapped system or isolated on an industrial-grade trusted network. However, in early real-world experience, this was rarely the case.

What is an HMI?

 An HMI enables the human operator and displays data from machines. It accepts commands from a human operator to machines. Via HMI, an operator monitors and responds to the system information. Modern generation HMI may also display the current state of the industrial control using advanced graphics-based visualizations.The following diagram illustrates a typical HMI for controlling filter operations and showing the status relevant to managing liquid stored in a tank ([http://www.pcmag.com/encyclopedia/term/44300/hmi](http://www.pcmag.com/encyclopedia/term/44300/hmi)):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/fefb35df-c474-4640-8e21-148d42e42ae2.png)

Figure 8.1: HMI for Industrial OperationsTo analyze the vulnerabilities of the industrial control systems, we will break down the industrial controls landscape into the following zones:

- **Zone 0**: Sensors and actuators
- **Zone 1**: **Programmable Logic Controllers** (**PLCs**) and **Remote Terminal Unit** (**RTU**)
- **Zone 2**: SCADA
- **Zone 3**: **Demilitarized zone** (**DMZ**)
- **Zone 4**: Corporate network

The internet or intranet are also frequently looked at for vulnerabilities.

Data obtained from the period of February 2013 to April 2016 indicates that 465 of 801 vulnerability disclosures impacted Zone 2. The devices in Zone 2, such as the HMI and engineering workstations, directly control the industrial processes. For example, in the attacks in the Ivano-Frankivsk region of the Western Ukraine on December 23, 2014 inside the Prykarpattyaoblenergo power plant, the attackers used the **BlackEnergy** malware propagated to the Zone 2 HMI to gain access to open and close the switches and actuators. This left about 230,000 residents in dark. The Ukrainian power grid attack impacted business operations and the public.

Computer malware has also been used to target other industrial control systems used in water-treatment facilities, gas pipelines, and related infrastructure facilities. In factory automation, SCADA and PLCs have been targeted.

**Stuxnet** is a typical form of malware that was first identified in 2010. It consists of three modules:

- **Worm**: This is used to execute the routines related to the main attack payload
- **Link file**: This is used to execute the propagated copies of the worm automatically
- **Rootkit**: This is a component responsible for hiding all malicious files and processes, which makes detecting the presence of Stuxnet harder

Zero-day vulnerabilities are security holes in software that the vendor is unaware of. Stuxnet has exploited such security holes in zero-day attacks before fixes were available or could be applied. It was first identified after being spread via the Microsoft Windows operating system and targeted Siemens industrial control systems. In one spectacular example, Stuxnet was used in an attack on an Iranian uranium-enrichment plant where the PLCs were compromised. Damage to the fast-spinning centrifuges led to them tearing themselves apart.

Malware was behind a DDoS attack in 2016, targeting servers that belonged to a company named Dyn, a provider of **Domain Name System** (**DNS**) services. The attack created a disruption of legitimate internet and e-commerce activities in the United States, including IIoT transmissions. The attackers targeted the DNS servers to create the disruption. Devices with **Mirai** malware directed massive spurious traffic at the targeted servers. The attackers exploited many internet-connected digital devices, such as surveillance cameras and home routers, to create a botnet. Even though each individual device was not very powerful in compute capacity, together they generated massive amounts of traffic enabling the DDoS attack to succeed.

What is a botnet?

 Botnets are networks of connected devices, each running one or more bots. Botnets can be used to orchestrate DDoS attacks or distribute spam and might be controlled by one or many outside sources. Control of the device is typically achieved by infecting it with malware, giving the attacker access. The device might seem to be operating normally even though it is part of a botnet being directed by the attacker.The **United States Computer Emergency Readiness Team** (**US CERT**) provided the following recommendations where it was believed that Mirai malware could be present in devices:

- Disconnect the device from the network or internet and reboot. While disconnected from the network and internet, perform a reboot. Since the Mirai malware resides in dynamic memory, the reboot clears the malware from the device.
- Change the default password to a strong password.
- Create a plan to periodically change the password (such as on dates when daylight saving comes into effect).
- Reconnect the device only after a reboot and change of password to prevent reinfection with the Mirai malware.

Obviously, it is better to proactively plan defenses against possible malware infection. The following measures, recommended by US CERT ([https://www.us-cert.gov/ncas/alerts/TA16-288A](https://www.us-cert.gov/ncas/alerts/TA16-288A)) should influence architecture design and policies:

- During installation, replace the default password with a strong password since default usernames and password for common devices can be easily found on the internet via sites such as [http://www.shodan.io](http://www.shodan.io)
- IoT devices should be updated with security patches as soon as they are made available
- **Universal Plug and Play** (**UPnP**) features on the routers should be disabled when not needed
- Buy IoT devices from credible manufacturers who have a proven record of secure devices
- Operate Wi-Fi-enabled devices with a secured Wi-Fi router only
- Medical devices that transmit data or can be operated remotely are also at a risk of being infected by malware with possible dangerous outcomes, so best practices from the device manufacturer should be closely followed to secure these devices
- **Internet Protocol** (**IP**) port 2323/TCP and port 23/TCP should be diligently monitored since these are often used for attempts to gain unauthorized control using the Telnet protocol over the IoT devices
- Infected IoT devices often try to spread malware using port 48101, so this port should be monitored for any suspicious traffic

As noted earlier, connected medical devices require special consideration. As early as 2007, when the United States vice president Dick Cheney had his implanted defibrillator replaced, there was debate about whether the wireless feature should be disabled. In the end, the doctor ordered the manufacturer to disable the wireless feature so that an attacker could not possibly send a signal to the defibrillator and shock him into cardiac arrest.

So, how do we create an architecture that can help protect our IIoT solution from attacks? We will begin exploring the core building blocks needed to ensure a secure IIoT architecture and solution in the next section.
