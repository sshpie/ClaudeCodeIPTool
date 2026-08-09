# 1: Introduction

## Abstract

An overview of the book, how it is organized, who the intended audience is, and key learning points.

### Keywords

Industrial cybersecurity; Introduction; Organization; OT; OutlineInformation in this chapter• Book overview and key learning points• Book audience• Diagrams and figures• The smart grid• OT, IoT, IIoT, and xIoT• How this book is organized• Changes made to the third addition
## Book overview and key learning points

This book is now in its third edition, published over a decade since the first edition's release in 2011. In some ways, a lot has changed during that time, and yet in others ways, very little has changed. In 2011, the entire concept of industrial cyber security was relatively new. Today, it is possible to specialize in this discipline and dedicate one's career to it. Formal education is offered by many universities as well as organizations such as the Cybersecurity and Infrastructure Security Agency (CISA), the International Information System Security Certification Consortium (ISC2), the SANS Technology Institute, and others. At the same time, for many readers coming from backgrounds in both industrial control (“OT”) and information technology (“IT”), the idea of industrial cyber security will be entirely new.

One thing that has definitely changed: it is no longer optional to ignore the subject of securing industrial automation and process control environments from the ever rising threat of a cyberattack.

Since the first edition, this book has attempted to define an approach to industrial network security that considers the unique network, protocol, and application characteristics of an **industrial control system** (**ICS**) while also taking into consideration a variety of common compliance controls. For the purposes of this book, a common definition of ICS will be used in lieu of the more specific **supervisory control and data acquisition** (**SCADA**) or **distributed control system** (**DCS**) terms. Note that these and many other specialized terms are used extensively throughout the book. While we have made an effort to define them all, an extensive glossary has also been included to provide a quick reference if needed. If a term is included in the glossary, it will be printed in bold type the first time that it is used.

One term that is new is the aforementioned “**OT,**” or “**operational technology.**” The acronym “OT” is widely used today to discuss any and all aspects of industrial cyber security. While it provides a simple and convenient way to reference an otherwise complex and nuanced subject, it is often misleading, and so it will be discussed in more detail in [Chapters 2](../B9780443137372000142/CH0002_11-43_B9780443137372000142.xhtml) and [3](../B9780443137372000099/CH0003_45-64_B9780443137372000099.xhtml).

Although many of the topics described herein—and much of the general guidance provided by regulatory standards organizations—are built upon common enterprise security methods and reference readily available information security tools, there remains little information available about how to implement these tools in an industrial network. This book attempts to rectify this by providing deployment and configuration guidance where possible, and by identifying why security controls should be implemented, where they should implemented, how they should be implemented, and how they should be used.

## Book audience

To adequately discuss industrial network security, the basics of two very different underlying communication systems need to be understood: the Ethernet and Internet Protocol (IP) networking communications used ubiquitously in the enterprise, and the control and field bus protocols are used to manage and/or operate automation systems.

As a result, this book possesses a bifurcated audience. For the plant operator with an advanced engineering degree and a decade of programming for process controllers, the basics of industrial network protocols in [Chapter 4](../B9780443137372000117/CH0004_65-90_B9780443137372000117.xhtml) have been presented within the context of security in an attempt to not only provide value to such a reader but also to get that reader thinking about the subtle implications of cyber security. For the information security professional, familiar tenant of information security and basic information security practices have been provided within the new context of an OT environment.

There is an interesting dichotomy between the two that provides a further challenge. IT security typically strives to protect digital information by securing the users and **hosts** on a network, while at the same time enabling the broad range of open communication services required within modern business. OT, on the other hand, strives for the efficiency and reliability of a fine-tuned OT system, while always addressing the safety of the personnel, plant, and environment in which they operate. While there has been a long-standing friction between these two groups, only by giving the necessary consideration to both sides can the true objective be achieved: a secure industrial network architecture that supports safe and reliable operation, minimizes risk, and provides business value to the larger enterprise. This latter concept is referred to as “operational integrity.”

While earlier editions focused on introducing each audience to the basics of the other's field, this edition aims to provide more nuanced information and guidance for a third audience: the OT Cybers Security Professional, who already understands the basics of both fields, but who is struggling to actually establish an OT security program, or to improve on the program that is currently in place.

## Diagrams and figures

The network diagrams used throughout this book have been intentionally simplified and have been designed to be as generic as possible while adequately representing ICS architectures and their industrial networks across a very wide range of systems and suppliers. As a result, the diagrams will undoubtedly differ from real ICS designs and may exclude details specific to one particular industry while including details that are specific to another. However, they will provide a high-level understanding of the specific industrial network security controls being discussed.

## The smart grid

Although the smart grid is of major concern and interest, for the most part, it is treated as any other industrial network within this book, with specific considerations being made only when necessary (such as when considering available **attack vectors**). As a result, there are many security considerations specific to the smart grids that are unfortunately not included. This is partly to maintain focus on the more ubiquitous ICS security requirements; partly due to the relative immaturity of smart grid security and partly due to the specialized and complex nature of these systems. Although this means that specific measures for securing synchrophasers, meters, etc. are not provided, the guidance and overall approach to security that is provided herein is certainly applicable to smart grid networks. For more in-depth reading on smart grid network security, consider *Applied Cyber Security and the Smart Grid* by Eric D Knapp and Raj Samani (ISBN: 978-1-59749-998-9, Syngress).

## OT, IoT, IIoT, and xIoT

As mentioned above, “OT” or “operational technology” is a convenient way to reference “industrial automation and control systems, industrial networks, and the assets that comprise them. While “OT” and “ Internet of Things (IoT)” are often conflated, they are actually very different.

According to Gartner, “The **Internet of Things** (**IoT**) is the network of physical objects that contain embedded technology to communicate and sense or interact with their internal states or the external environment.”[1](#fn1) The term is widely attributed to a Kevin Ashton in 1999. Mr Ashton was MIT's Executive Director of Auto-ID Labs, and a pioneer in the use of RFID for automated inventory tracking.[2](#fn2) IoT became extremely popular in the early 2000s as more and more smart devices were introduced commercially. By the early 2020s, IoT devices are commonplace and include smart doorbells, surveillance cameras, sensors, and actuators used in industrial applications, medical devices, and more. As IoT evolved, so did the nomenclature. For example, IoT used for industrial applications is typically referred to as **Industrial Internet of Things (IIoT**). When referencing connected devices that could span many uses and specializations, the term **xIoT** (where the “x” represents a variable).

For purposes of industrial network security, IoT is something that needs to be acknowledged and understood. However, the focus on this book is on industrial networks, rather than IoT: that is, on structured networks used for industrial automation and control, rather than the Internet. IoT will not be discussed in depth, although the ubiquity of interconnected devices that are available across many industries needs to be acknowledged. An industrial automation and control system *could* include distributed devices that are interconnected via the Internet, either deliberately or accidently, and the introduction of such interconnected devices could have severe impact on the proper implementation of zones and conduits (see [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml): Establishing zones and conduits). This is especially true in industrial systems that are highly distributed by nature, such as smart cities and smart grid applications.

## How this book is organized

This book is divided into a total of 11 chapters, followed by three appendices guiding the reader where to find additional information and resources about industrial protocols, standards and regulations, and relevant security guidelines and best practices (such as **NIST**, **ChemITC,** and **ISA**).

The chapters begin with an introduction to industrial networking, and what a cyberattack against an ICSs might represent in terms of potential risks and consequences, followed by details of how industrial networks can be assessed, secured, and monitored in order to obtain the strongest possible security, and conclude with a detailed discussion of various compliance controls, and how those specific controls map back to network security practices.

It is not necessary to read this book cover to cover, in order. The book is intended to offer insight and recommendations that relate to both specific security goals as well as the cyclical nature of the security process. That is, if faced with performing a **security assessment** on an industrial network, begin with [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml); every effort has been made to refer the reader to other relevant chapters where additional knowledge may be necessary.

### [Chapter 2](../B9780443137372000142/CH0002_11-43_B9780443137372000142.xhtml): About Industrial Networks

In this chapter, there is a brief primer of ICSs, industrial networks, **critical infrastructure**, common cyber security guidelines, and other terminology specific to the lexicon of industrial cyber security. The goal of this chapter is to provide a baseline of information from which topics can be explored in more detail in the following chapters (there is also an extensive Glossary included to cover the abundance of new acronyms and terms used in OT networks). [Chapter 2](../B9780443137372000142/CH0002_11-43_B9780443137372000142.xhtml) also covers some of the basic misperceptions about industrial cyber security, in an attempt to rectify any misunderstandings prior to the more detailed discussions that will follow.

### [Chapter 3](../B9780443137372000099/CH0003_45-64_B9780443137372000099.xhtml): Industrial Cyber Security, History, and Trends

[Chapter 3](../B9780443137372000099/CH0003_45-64_B9780443137372000099.xhtml) is a primer for industrial cyber security. It introduces industrial network cyber security in terms of its history and evolution, by examining the interrelations between “general” networking, industrial networking, and potentially critical infrastructures. [Chapter 3](../B9780443137372000099/CH0003_45-64_B9780443137372000099.xhtml) covers the importance of securing industrial networks, discusses the impact of a successful industrial attack, and provides examples of real historical incidents—including a discussion of the **advanced persistent threat** and the implications of cyber war.

### [Chapter 4](../B9780443137372000117/CH0004_65-90_B9780443137372000117.xhtml): Introduction to ICS Systems and Operations

It is impossible to understand how to adequately secure an OT environment without first understanding the fundamentals of ICS systems and operations. These systems use specialized devices, applications, and protocols because they perform functions that are different than enterprise networks, with different requirements, operational priorities, and security considerations. [Chapter 4](../B9780443137372000117/CH0004_65-90_B9780443137372000117.xhtml) discusses control system **assets**, operations, protocol basics, how control processes are managed, and common systems and applications with special emphasis on smart grid operations.

### [Chapter 5](../B9780443137372000038/CH0005_91-128_B9780443137372000038.xhtml): ICS Network Design and Architecture

Industrial networks are built from a combination of Ethernet and TCP/IP networks (to interconnect general computing systems and servers) and at least one real time network or fieldbus (to connect devices and process systems). These networks are typically nested deep within the enterprise architecture, offering some implied layers of protection against external threats. In recent years, the deployment of remote access and wireless networks within industrial systems offers new entry points into these internal networks. [Chapter 5](../B9780443137372000038/CH0005_91-128_B9780443137372000038.xhtml) provides an overview of some of the more common industrial network designs and architectures, the potential risk they present, and some of the methods that can be used to select appropriate technologies and strengthen these critical industrial systems.

### [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml): Industrial Network Protocols

This chapter focuses on industrial network protocols, including **Modbus**, **DNP3**, **OPC**, **ICCP**, **CIP, Foundation Fieldbus, Wireless HART, Profinet** and **Profibus, Zigbee,** and others. This chapter will also introduce vendor-proprietary industrial protocols, and the implications they have in securing industrial networks. The basics of protocol operation, frame format, and security considerations are provided for each, with security recommendations being made where applicable. Where properly disclosed vulnerabilities or exploits are available, examples are provided to illustrate the importance of securing industrial communications.

### [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml): Hacking Industrial Systems

Understanding effective cyber security requires a basic understanding of the threats that exist. [Chapter 6](../B9780443137372000063/CH0006_129-179_B9780443137372000063.xhtml) provides a high-level overview of common attack methodologies, and how industrial networks present a unique **attack surface** with common attack vectors to many critical areas.

### [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml): Risk and Vulnerability Assessments

Industrial control systems are often more susceptible to a cyberattack, yet they are also more difficult to patch due to the extreme uptime and reliability requirements of operational systems. [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml) focuses on risk and vulnerability assessment strategies that specifically address the unique challenges of assessing risk in industrial networks, in order to better understand—and therefore reduce—the vulnerabilities and threats facing these real-time systems.

### [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml): Establishing Zones and Conduits

A strong cyber security strategy requires the isolation of devices into securable groups. [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml) looks at how to separate functional groups and where functional boundaries should be implemented, using the Zone and Conduit model originated by the Purdue Research Foundation in 1989 and later adapted by ISA 99 (now known as ISA/**IEC** 62,443). Specifics are then provided on how to secure not only the interior zones but also the conduits used to interconnect these zones, including common security products, methods, and policies that may be implemented.

### [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml): OT Attack and Defense Lifecycles

To successfully protect an industrial environment against cyberattacks, it is necessary to understand the basics of attack and defense lifecycles. This chapter includes discussion of attack lifecycles including the MITER ATT&CK framework, in order to understand how to best utilize defensive capabilities, cybersecurity controls, countermeasures, policies, and procedures.

### [Chapter 11](../B9780443137372000129/CH0011_331-381_B9780443137372000129.xhtml): Implementing Security and Access Controls

With a new understanding of how specific controls can influence attack and defensive lifecycles from [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), this chapter goes into more specifics about the various cybersecurity controls that are commercially available, and how they can be implemented. This chapter discusses various controls that are required to obtain cybersecurity data that are necessary for broader cybersecurity monitoring efforts.

### [Chapter 12](../B9780443137372000051/CH0012_383-408_B9780443137372000051.xhtml): Exception, Anomaly, and Threat Detection

Industrial control network monitoring and analysis tools have become increasingly popular: enough so to justify their won chapter. These tools can provide valuable insight  to the OT security teams responsible for cybersecurity monitoring and analysis. However, they can also bring new challenges, including unique deployment and operationalization considerations.

### [Chapter 13](../B9780443137372000105/CH0013_409-446_B9780443137372000105.xhtml): Security Monitoring of Industrial Control Systems

Completing the cycle of situational awareness requires further understanding and analysis of the threat indicators that you have learned how to detect in previous chapters. [Chapter 13](../B9780443137372000105/CH0013_409-446_B9780443137372000105.xhtml) discusses how obtaining and analyzing broader sets of information can help you better understand what is happening and make better decisions. This includes recommendations of what to monitor, why, and how. Information management strategies—including **log** and **event** collection, direct monitoring, and correlation using **security information and event management** (**SIEM**) and other tools—are discussed here, including guidance on data collection, retention, and management.

### [Chapter 14](../B9780443137372000154/CH0014_447-465_B9780443137372000154.xhtml): Standards and Regulations

There are many regulatory compliance standards applicable to industrial network security, and most consist of a wide range of procedural controls that are not easily resolved using IT. On top of this, there is an emergence of a large number of industrial standards that attempt to tailor many of the general-purpose IT standards to the uniqueness of ICS architectures. There are common cyber security controls (with often subtle but importance variations), however, which reinforce the recommendations put forth in this book. [Chapter 12](../B9780443137372000051/CH0012_383-408_B9780443137372000051.xhtml) attempts to map those cyber security–related controls from some common standards—including **NERC CIP**, **CFATS**, NIST 800–53, **ISO**/IEC 27,002:2005, ISA 62,443, **NRC** RG 5.71, and NIST 800–82—to the security recommendations made within this book, making it easier for security analysts to understand the motivations of compliance officers, while compliance officers are able to see the security concerns behind individual controls.

### [Chapter 15](../B978044313737200018X/CH0015_467-474_B978044313737200018X.xhtml): Common Pitfalls and Mistakes

Back by popular demand, this chapter highlights some common pitfalls and mistakes—including errors of complacency, common misconfigurations, and deployment errors. By highlighting the pitfalls and mistakes, it is easier to avoid repeating those mistakes.

## Changes made to the third edition

For readers of previous editions of industrial network security, securing critical infrastructure networks for smart grid, SCADA and other ICSs, you will find new and updated content throughout the book. However, the largest changes that have been made include.

1. • Revised diagrams, designed to provide a more accurate representation of industrial systems so that the lessons within the book can be more easily applied in real life.
2. • Better organization of topics, including major revisions to both introductory chapters ([Chapter 2](../B9780443137372000142/CH0002_11-43_B9780443137372000142.xhtml), that are intended to provide a more effective introduction of topics.
3. • The separation of “hacking methodologies” and “risk and vulnerability assessment” into two chapters, expanding each to provide significantly more detail to each very important subject.
4. • The expansion of “risk and vulnerability assessment” to expand further beyond network-scan-based assessments and include more system-level assessment guidance, including safety considerations, cyber-physical threat modeling, and cybersecurity HAZOPs discussions.
5. • The inclusion of wireless networking technologies and how they are applied to industrial networks, including important differences between general-purpose IT and specific ICS technology requirements.
6. • Much greater depth on the subjects of industrial firewall implementation and industrial protocol filtering—important technologies that were in their infancy during the first edition but are now commercially available.
7. • The inclusion of real-life vulnerabilities, exploits, and defensive techniques throughout the book to provide a more realistic context around each topic, while also proving the reality of the threat against critical infrastructure.
8. • An entirely new chapter on “OT Defense Lifecycle & Defensive Methods,” which discusses the OT cyber defensive lifecycle, from detection to response to recovery. This chapter acts as a precursor to the previous chapter on “Implementing Security and Access Controls,” which has been expanded to include newer security controls and to provide more specific guidance where available.
9. • For readers of earlier editions, or who have established careers or responsibilities in OT cyber security, new material has been added. Discussions of cyber security posture, cyber security maturity, and the lifecycle of a cybersecurity incident have been added, as well as expanded discussions of when, where, and how to implement OT cyber security controls.
10. • The closing chapter on “Pitfalls and Mistakes” is back! Since the first edition was published, the industry has made its share of new blunders. Do not be embarrassed if you have made these mistakes; learn from them; and maybe laugh a little along the way.

## Conclusion

Writing the first edition of this book was an education, an experience, and a challenge. In the months of research and writing, several historic moments occurred concerning ICS security, including the first ICS-targeted cyber weapon: Stuxnet. At the time, Stuxnet was  the most sophisticated cyberattack to date. Since then, its complexity and sophistication have been surpassed more than once, and the frequency of new threats continues to rise. There is a growing number of attacks, more relevant cyber security research (from both **blackhats** and **whitehats**), and new evidence of advanced persistent threats, cyber espionage, nation-based cyber privacy concerns, and other socio-political concerns on what seems like a daily basis.

Hopefully, this book will be both informative and enjoyable, and it will facilitate the increasingly urgent need to strengthen the security of our industrial networks and automation systems. Even though the attacks themselves will continue to evolve, the methods provided herein should help to prepare against the inevitable advancement of industrial network threat.

---

[1](#cfn1)  Gartner, Inc. “Gartner Glossary, Information Technology”. Document from the web, cited January 2023. [https://www.gartner.com/en/information-technology/glossary/internet-of-things](https://www.gartner.com/en/information-technology/glossary/internet-of-things)

[2](#cfn2)  Keith D. Foote, “A Brief History of the Internet of Things” January 14, 2022. Document from the web. [https://www.dataversity.net/brief-history-internet-things/](https://www.dataversity.net/brief-history-internet-things/)
