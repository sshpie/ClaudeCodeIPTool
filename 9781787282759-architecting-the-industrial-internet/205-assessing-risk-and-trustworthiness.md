# Assessing risk and trustworthiness

Governance activities that secure edge, backend, and networking components and data at rest and in motion are usually the domain of security specialists in IT. Relevant legal and regulatory requirements regarding cybersecurity, including privacy and civil liberties, must be understood, so IT will often partner with company lawyers having a background in securing data in an organization. Many begin by researching standards, such as those published by the **International Society of Automation** (**ISA**), **Information Systems Audit and Control Association** (**ISACA**)'s **Control Objectives for Information and Related Technologies** (**COBIT**), the **International Organization for Standardization** and **International Electrotechnical Commission** (**ISO** / **IEC**), and the **National Institute of Standards** (**NIST**). As we'll soon see, this is just the beginning. You will likely quickly discover additional compliance requirements that are defined by a host of other standard bodies in your country and/or industry. Your solution should be designed to conform with these standards to mitigate potential risks and meet business objectives.

At this point, you will begin to assess risks to the project. You might find some external legal and regulatory requirements to be quite challenging and compliance difficult to achieve. Your response to these risks will likely depend on the perceived gravity of the risks, the cost associated with eliminating the risks, your ability to transfer risks to a third party, and the potential danger to your data and business. These criteria can help you prioritize the need to mitigate potential risks and initiate corrective action and design changes in your architecture.

*NIST Special Publication 800-53* identifies security and privacy controls for United States federal information systems and organizations. By targeting government agencies, NIST guidance and nomenclature often finds its way into other standards, so it serves as a useful place to start our discussion. Much of the content in this NIST publication eventually made its way into ISA standards used in establishing an industrial automation and control system security program (ISA 99.02.01).

NIST suggests a three-tiered approach to risk management, targeting the organization, mission and business processes, and information systems, as pictured in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/31bb7c9e-79e7-4e89-b41d-d935e91dfd3c.png)

Some of the fundamental tasks and policies recommended to overcome risk include the following:

- Clearly documented security requirements and specifications
- Well-designed and current hardware, firmware, and software
- Sound systems and security principles and practices for integration of components
- Well-documented security practices and training that becomes part of daily routines
- Continuous monitoring of the organization and infrastructure to determine effectiveness of security controls and changes in systems, operations, and compliance
- Ongoing data and infrastructure security planning and life cycle management

NIST defines a **Risk Management Framework** (**RMF**) that describes the security life cycle in six major steps. We've adapted some of the nomenclature to fit broader Industrial Internet solutions as pictured in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/ac51d451-1903-414e-958a-415f4349861a.png)

RMF begins with an architecture description and input from the organization regarding potential security risks and considerations. Devices and systems (endpoints) as well as the networking between them are categorized. Security controls are selected for each, implemented, and then assessed for effectiveness. Devices and systems are authorized, and then, the security controls are monitored. As new components are introduced, the process repeats itself.

ISA 99.01.01 provides definitions for **security assurance levels** (**SALs**) that are relevant to steps along the life cycle. Assurance is an ongoing process and the basis for trusting that policies are implemented. Multiple kinds of SALs are defined. Target SALs are the desired levels of security. Capability SALs are the security levels that can be provided when components are properly configured. Design SALs are planned levels of security. Achieved SALs are the actual level of security provided.

SALs are based on foundational requirements defined in the standard. The following foundational requirements are evaluated for each kind of SAL:

- Access control through identification and authentication
- Use control through specified privileges
- Data integrity (data protected against unauthorized manipulation)
- Data confidentiality (data protected against eavesdropping or exposure)
- Restricted data flow (flow eliminated beyond acceptable zones or conduits)
- Timely response to an event (including real-time response to attacks)
- Resource availability, preventing DoS attacks

SALs are evaluated for each zone of the IIoT architecture solution. Zones are defined in ISA documents as the industrial network (consisting of edge devices in field locations such as plants and local networks), the industrial/enterprise DMZ (the edge to backend network), and the enterprise network (backend systems and networking residing in a data center in the cloud or on-premises).

SALs help us determine the trustworthiness of the IIoT solution. The degree by which the solution is deemed trustworthy is determined by the confidence in preserving the confidentiality, integrity, and availability of data that is being processed, stored, or transmitted by the systems and devices when facing a range of threats. A trustworthy solution can operate within defined risk tolerances and deliver desired business solutions despite the environmental disruptions, human errors, structural failures, and attacks that might be expected.

Next, we'll explore standards and compliance requirements. We will begin by describing international compliance certifications that many of these solutions must meet.
