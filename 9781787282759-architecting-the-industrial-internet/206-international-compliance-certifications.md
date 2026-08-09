# International compliance certifications

ISA standards often eventually become part of the IEC standards and extend interpretations of existing IEC standards. For example, the previously mentioned ISA 99.0.1 standards became IEC 62443 for industrial network and system security. This standard's pedigree includes earlier defined ISO / IEC 27000 series standards.

IEC 62443 addresses securing external network communications paths into device networks, including the control network interconnect, interactive remote access to the control network, inter-control center access to the shared control net, standalone embedded devices, portable engineering computers and devices, and portable storage medium. It also addresses securing internal network communications paths within device networks for inter-area communications, control center networks within a single control area, and field control networks within a single control area. Finally, it addresses securing devices within their networks, including the control network host and field device.

It joins a host of other standards created by ISO/IEC, including ISO 27001, 27002, 27003, 27017, 27018, and 22301 that we'll describe here. Each has applicability in an IIoT architecture.

ISO 27001 defines the requirements for *establishing, implementing, maintaining, and continuously improving an Information Security Management System (ISMS)*. Adherence to the standard requires that an organization systematically examines security risks, including threats, vulnerabilities, and impacts. Architecture design and implementation must include a suite of information security controls or handle risk in other ways (such as a documented means of risk transfer or avoidance). The controls must be managed on an ongoing basis to ensure security.

The standard focuses on the controls in the following areas:

- Information security policies
- Organization of information security
- Human resource security
- Asset management
- Access control
- Cryptography
- Physical and environmental security
- Operations security
- Communications security
- System acquisition, development, and maintenance
- Supplier relationships
- Information security incident management
- Information security aspects of business continuity management
- Compliance with internal requirements (policies) and external requirements (laws)

The standard evolved over time, initially focusing primarily on planning and execution with later focus on measuring and evaluating how well the ISMS is performing. This guidance further evolved to address the impact of cloud computing. As noted in earlier chapters, the cloud is commonly used today in deployment of IIoT backend components.

ISO / IEC 27002 is an advisory standard that aligns to the same controls covered in ISO / IEC 27001 and describes the best practices for each. ISO/IEC 27003 provides additional guidance for these same controls with the goal of making the management systems consistent in structure and form, especially for ISMS certification purposes.

ISO/IEC 27017 provides further guidelines for information security services in cloud deployment related to provisioning and usage. ISO/IEC 27018 focuses on protection of **Personally Identifiable Information** (**PII**) in the cloud.

ISO/IEC 22301 provides standards for assuring business continuity so that the IIoT solution will continue to operate in some form and/or return to normal as quickly as possible when a disruptive incident occurs. This standard defines the role of a **Business Continuity Management System** (**BCMS**). Business continuity goals can be achieved by the following:

- Defining scope based on the organization's needs
- Gaining proper leadership and resources
- Identifying risks and setting clear objectives and criteria for success
- Ensuring that individuals with proper skills and communications channels are available when incidents occur
- Performing business impact analyses and risk assessments to take a balanced approach to proper planning and performing exercises and tests to prove objectives can be met
- Evaluating and auditing performance
- Defining actions to improve BCMS

As we've just seen, many of these standards form a basis for performing detailed assessments. The Cloud Security Alliance, a coalition of companies and stakeholders, teamed with the British Standards Institution in 2013 to create a Security, Trust & Assurance Registry, known as CSA STAR. CSA STAR is used in publishing these GRC self-assessments. It includes a **Cloud Controls Matrix** (**CCM**), a framework covering security principles in 16 domains, and a **Consensus Assessments Initiative Questionnaire** (**CAIQ**) used to assess compliance with GRC best practices. The 16 domains covered are as follows:

- Application and interface security
- Audit assurance and compliance
- Business continuity management and operational resilience
- Change control and configuration management
- Data security and information life cycle management
- Data center security
- Encryption and key management
- Governance and risk management
- Human resources
- Identity and access management
- Infrastructure and virtualization security
- Interoperability and portability virtualization
- Mobile security
- Security incident management
- Information security across the information supply chain (third party)
- Threat and vulnerability management

Many Industrial Internet solutions can impact the financial results of an organization once they are deployed. You will recall that we discussed financial justification for a project in the supply chain optimization example covered in the earlier chapters of this book. The **System and Organization Controls** (**SOC**) provides a suite of services that CPAs can use to audit these deployments and determine their service level controls.

SOC 1 is based on the **Statement on Standards for Attestation Engagements** (**SSAE 16**) and the **International Standards for Assurance Engagements** number 3402 (**ISAE 3402**). These provide the basis for performing audits of **cloud service providers'** (**CSPs'**) internal controls affecting financial reporting.

SOC 2 audits determine how well the CSP follows the AICPA Trust Service Principles and Criteria (AT Section 101). SOC 3 is an abbreviated version of SOC 2.

Finally, a broader standard mandated in many organizations is ISO 9001. The certification can apply to many aspects of the business, including the deployment and management of IIoT solutions. This standard is based on quality management principles, including a strong customer focus, leadership by top management establishing unity of purpose, a process approach to optimizing performance and managing risk, and continual improvement.
