# Chapter 4. Information System Security Principles

**IN THIS CHAPTER**

- **Reviewing the principles of network security**
- **Understanding the systems engineering and Information Systems Security Engineering process**
- **Summarizing the System Development Life Cycle (SDLC)**
- **Relating information systems security and the SDLC**
- **Managing risk**

A number of organizations have defined terminology and methodologies for applying systems engineering (SE) principles to large tasks and undertakings. When information systems and networks are involved, companion Information System Security Engineering (ISSE) processes should be practiced concurrently with SE at project initiation.

This chapter defines the fundamental principles of network security and explains the SE and ISSE processes. It also describes the steps in the systems development life cycle (SDLC) and reviews how network and information technology (IT) security practices can be incorporated into the SDLC activities.

The chapter concludes with coverage of risk management techniques and the application of risk management in the SDLC.

# Key Principles of Network Security

Network security revolves around the three key principles of confidentiality, integrity, and availability (C-I-A). Depending upon the application and context, one of these principles might be more important than the others. For example, a government agency would encrypt an electronically transmitted classified document to prevent an unauthorized person from reading its contents. Thus, confidentiality of the information is paramount. If an individual succeeds in breaking the encryption cipher and, then, retransmits a modified encrypted version, the integrity of the message is compromised. On the other hand, an organization such as Amazon.com would be severely damaged if its network were out of commission for an extended period of time. Thus, availability is a key concern of such e-commerce companies.

## Confidentiality

Confidentiality is concerned with preventing the unauthorized disclosure of sensitive information. The disclosure could be intentional, such as breaking a cipher and reading the information, or it could be unintentional, due to the carelessness or incompetence of individuals handling the information.

## Integrity

There are three goals of integrity:

- Preventing the modification of information by unauthorized users
- Preventing the unauthorized or unintentional modification of information by authorized users
- Preserving the internal and external consistency:**Internal consistency**— Ensures that internal data is consistent. For example, in an organizational database, the total number of items owned by an organization must equal the sum of the same items shown in the database as being held by each element of the organization.**External consistency**— Ensures that the data stored in the database is consistent with the real world. Relative to the previous example, the total number of items physically sitting on the shelf must equal the total number of items indicated by the database.

## Availability

Availability assures that a system's authorized users have timely and uninterrupted access to the information in the system and to the network.

## Other Important Terms

Also important to network security are the following four C-I-A–related terms:

- **Identification**— The act of a user professing an identity to the system, such as a logon ID
- **Authentication**— Verification that the user's claimed identity is valid, such as through the use of a password
- **Accountability**— Determination of the actions and behavior of a single individual within a system, and holding the individual responsible for his or her actions
- **Authorization**— The privileges allocated to an individual (or process) that enable access to a computer resource

# Formal Processes

The processes associated with specifying, designing, implementing, operating, and maintaining network-based systems are amenable to formal methods. These methods provide a structured approach to achieving effective and maintainable networks and systems. In particular, applying the disciplines of systems engineering and systems security engineering (SSE) in the systems development life cycle can yield functional, secure, robust, and cost-effective networks and systems. These processes are described in the following sections.

## The Systems Engineering Process

There are a myriad of definitions of systems engineering, ranging from the view of government and military establishments to commercial organizations. A sampling of these definitions follows:

- "The function of systems engineering is to guide the engineering of complex systems ... A system is a set of interrelated components working together toward some common objective." (Kossiakoff and Sweet, *Systems Engineering, Principles and Practices*, John Wiley & Sons, 2003.)
- The branch of engineering concerned with the development of large and complex systems, where a system is understood to be an assembly or combination of interrelated elements or parts working together toward a common objective. (General, widely used definition.)
- The selective application of scientific and engineering efforts to:Transform an operational need into a description of the system configuration that best satisfies the operational need according to the measures of effectivenessIntegrate related technical parameters and ensure compatibility of all physical, functional, and technical program interfaces in a manner that optimizes the total system definition and design.Integrate the efforts of all engineering disciplines and specialties into the total engineering effort. (From the Carnegie Mellon Software Engineering Institute (SEI) "Systems Engineering Capability Model [SE-CMM-95-0I]" document, version 1.1.)
- Systems engineering integrates all the disciplines and specialty groups into a team effort forming a structured development process that proceeds from concept to production to operation. Systems engineering considers both the business and the technical needs of all customers with the goal of providing a quality product that meets the user's needs. (The International Council on Systems Engineering [INCOSE], `www.incose.org`.)
- A process that will:Transform approved operational needs and requirements into an integrated system design solution through concurrent consideration of all life-cycle needs (that is, development, manufacturing, testing and evaluation, deployment, operations, support, training, and disposal).Ensure the interoperability and integration of all operational, functional, and physical interfaces. Ensure that system definition and design reflect the requirements for all system elements: hardware, software, facilities, people, and data.Characterize and manage technical risks.Apply scientific and engineering principles, using the system security engineering process, to identify security vulnerabilities and minimize or contain information assurance and force protection risks associated with these vulnerabilities. (DoD regulation 5000.2-R)

## The Information Assurance Technical Framework

The Information Assurance Technical Framework Forum (IATFF) is an organization sponsored by the National Security Agency (NSA) and supports technical interchanges among U.S. industry, U.S. academic institutions, and U.S. government agencies on the topic of information assurance. The Forum generated the Information Assurance Technical Framework (IATF) document, release 3.1, which describes processes and provides guidance for the protection of information systems based on systems engineering principles. The document emphasizes the criticality of the *people* involved, the *operations* required, and the *technology* needed to meet the organization's mission. These three entities are the basis for the Defense-in-Depth protection methodology described in [Chapter 2](ch02.html) of the IATF document, release 3.1. The principles of Defense-in-Depth are presented in the next section.

### Defense-in-Depth

Defense-in-Depth is a layered protection scheme for critical information system components. The Defense-in-Depth strategy comprises the following areas:

- Defending the network and infrastructure
- Defending the enclave boundary
- Defending the computing environment
- Supporting infrastructures

The enclaves in the U.S. federal and defense computing environments can be categorized as public, private, or classified.

The Defense-in-Depth strategy is built on three critical elements: people, technology, and operations (or processes).

#### People

To implement effective information assurance in an organization, management must have a high-level commitment to the process. This commitment is manifested through the following items and activities:

- Development of information assurance policies and procedures
- Assignment of roles and responsibilities
- Training of critical personnel
- Enforcement of personal accountability
- Commitment of resources
- Establishment of physical security controls
- Establishment of personnel security controls
- Penalties associated with unauthorized behavior

#### Technology

An organization has to ensure that the proper technologies are acquired and deployed to implement the required information protection services. These objectives are accomplished through the following processes and policies for the acquisition of technology:

- A security policy
- System-level information assurance architectures
- System-level information assurance standards
- Information assurance principles
- Specification criteria for the required information assurance products
- Acquisition of reliable, third-party, validated products
- Configuration recommendations
- Risk assessment processes for the integrated systems

#### Operations

Operations emphasize the activities, processes and items necessary to maintain an organization's effective security posture on a day-to-day basis. These activities and items include the following:

- A visible and up-to-date security policy
- Enforcement of the information security policy
- Certification and accreditation
- Information security posture management
- Key management services
- Readiness assessments
- Protection of the infrastructure
- Performing systems security assessments
- Monitoring and reacting to threats
- Attack sensing, warning, and response (ASW&R)
- Recovery and reconstitution

The Defense-in-Depth strategy is defined to defend against the following types of attacks, as described in IATF document 3.1:

- **Passive**— Passive attacks include traffic analysis, monitoring of unprotected communications, decrypting weakly encrypted traffic, and capture of authentication information (such as passwords). Passive intercept of network operations can give adversaries indications and warnings of impending actions. Passive attacks can result in disclosure of information or data files to an attacker without the consent or knowledge of the user. Examples include the disclosure of personal information such as credit card numbers and medical files.
- **Active**— Active attacks include attempts to circumvent or break protection features, introduce malicious code, or steal or modify information. These attacks may be mounted against a network backbone, exploit information in transit, electronically penetrate an enclave, or attack an authorized remote user during an attempt to connect to an enclave. Active attacks can result in the disclosure or dissemination of data files, denial of service, or modification of data.
- **Close-in**— Close-in attacks consist of individuals attaining physical proximity to networks, systems, or facilities for the purpose of modifying, gathering, or denying access to information. Close physical proximity is achieved through surreptitious entry, open access, or both.
- **Insider**— Insider attacks can be malicious or nonmalicious. Malicious insiders intentionally eavesdrop, steal, or damage information; use information in a fraudulent manner; or deny access to other authorized users. Nonmalicious attacks typically result from carelessness, lack of knowledge, or intentional circumvention of security for such reasons as "getting the job done."
- **Distribution**— Distribution attacks focus on the malicious modification of hardware or software at the factory or during distribution. These attacks can introduce malicious code into a product, such as a back door to gain unauthorized access to information or a system function at a later date.

To resist these types of attacks, Defense-in-Depth applies the following techniques:

- **Defense in multiple places**— Deployment of information protection mechanisms at multiple locations to protect against internal and external threats.
- **Layered defenses**— Deployment of multiple information protection and detection mechanisms so that an adversary or threat will have to negotiate multiple barriers to gain access to critical information.
- **Security robustness**— Based on the value of the information system component to be protected and the anticipated threats, estimation of the robustness of each information assurance components. Robustness is measured in terms of assurance and strength of the information assurance component.
- **Deploy KMI/PKI**— Deployment of robust key management infrastructures (KMI) and public key infrastructures (PKI).
- **Deploy intrusion detection systems**— Deployment of intrusion detection mechanisms to detect intrusions, evaluate information, examine results, and, if necessary, to take action.

Implementing the Defense-in-Depth approach can be resource intensive. To assist in the cost-effective implementation of Defense-in-Depth, there are the following guidelines:

- Make information assurance decisions based on risk analysis and keyed to the organization's operational objectives.
- Draw from all three facets of Defense-in-Depth—people, operations, and technology. Technical mitigations are of no value without trained people to use them and operational procedures to guide their application.
- Establish a comprehensive program of education, training, practical experience, and awareness. Professionalization and certification licensing provide a validated and recognized expert cadre of system administrators.
- Exploit available commercial off-the-shelf (COTS) products and rely on in-house development for those items not otherwise available.
- Periodically assess the IA posture of the information infrastructure. Technology tools, such as automated scanners for networks, can assist in vulnerability assessments.
- Take into account not only the actions of those with hostile intent, but also inadvertent or careless actions.
- Employ multiple means of threat mitigation, overlapping protection approaches to counter anticipated events so that loss or failure of a single barrier does not compromise the overall information infrastructure.
- Ensure that only trustworthy personnel have physical access to the system. Methods of providing such assurance include appropriate background investigations, security clearances, credentials, and badges.
- Use established procedures to report incident information provided by intrusion detection mechanisms to authorities and specialized analysis and response centers.

### Systems Engineering Processes

A number of paradigms are applicable to implementing systems engineering and some useful approaches are listed here:

- IEEE STD 1220-1998 processes:Requirements AnalysisRequirements VerificationFunctional AnalysisFunctional VerificationSynthesisDesign Verification
- DoD 5000.2-R processes:Requirements AnalysisFunctional Analysis/AllocationSynthesis

A commonly used set of processes in the U.S. government is described in the IATF document, and this set is the basis for deriving information system security engineering (ISSE) processes. These "generic" SE processes are as follows:

- Discover needs
- Define system requirements
- Design system architecture
- Develop detailed design
- Implement system
- Assess effectiveness

These processes emphasize the application of SE over the entire development life cycle.

## The Information Systems Security Engineering Process

The Information Systems Security Engineering (ISSE) processes are based on the generic SE processes, as shown in the following pairings:

- Discover information protection needs—Discover needs
- Define system security requirements—Define system requirements
- Design system security architecture—Design system architecture
- Develop detailed security design—Develop detailed design
- Implement system security—Implement system
- Assess information protection effectiveness—Assess effectiveness

The six ISSE processes are comprised of the activities discussed in the following sections.

### Discover Information Protection Needs

The objectives of this process are to understand and document the customer's needs and to develop solutions that will meet these needs. The information systems security engineer should use any reliable sources of information to learn about the customer's mission and business operations, including areas such as human resources, finance, command and control, engineering, logistics, and research and development. This knowledge can be used to generate a *concept of operations* (CONOPS) document or a *mission needs statement* (MNS). The Committee on National Security Systems (CNSS) Instruction No. 4009, "National Information Assurance (IA) Glossary" defines a CONOPS as "a document detailing the method, act, process, or effect of using an information system (IS)."

Then, with this information in hand, an *information management model* (IMM) should be developed that ultimately defines a number of *information domains*. Information management includes the following:

- Creating information
- Acquiring information
- Processing information
- Storing and retrieving information
- Transferring information
- Deleting information

The information management model should take into account information domains that comprise the following items:

- The information being processed
- Processes being used
- Information generators
- Information consumers
- User roles
- Information management policy requirements
- Regulations
- Agreements or contracts

The principle of *least privilege* should be used in developing the model by permitting users to access only the information required for them to accomplish their assigned tasks.

[Table 4-1](ch04.html#information_management_model) provides an example of an IMM.

**Table 4.1. Information Management Model**

| Users | Rules | Process | Information |
| --- | --- | --- | --- |
| CEO | Read | Corporate Finance | Policy |
| Treasurer | Read/Write | Corporate Finance | Policy |
| Asst. Treasurer | Read/Write | Corporate Finance | Policy |

A similar example of the output domains of the IMM is given in [Table 4-2](ch04.html#imm_information_domain_example).

**Table 4.2. IMM Information Domain Example**

| Domain | Users | Rules | Process | Information |
| --- | --- | --- | --- | --- |
| Human | Director | Read/Write | Corporate Salary Schedule | Job Classifications, Resources' Salaries |
| Human | Benefits Staff | Read | Corporate Salary Schedule | Benefit Plans, Resources' Salaries, Employee Contributions |

The information systems security engineer must document all elements of the Discover Information Protection Needs activity of the ISSE process, including the following:

- Roles
- Responsibilities
- Threats
- Strengths
- Security services
- Priorities
- Design constraints

These elements form the fundamental concepts of an *Information Protection Policy* (IPP), which in turn becomes a component of the customer's *Information Management Policy* (IMP).

The information systems security engineer must also support the certification and accreditation (C&A) of the system. *Certification* is the comprehensive evaluation of the technical and nontechnical security features of an information system and the other safeguards, which are created in support of the accreditation process, to establish the extent in which a particular design and implementation meets the set of specified security requirements.

*Accreditation* is the formal declaration by a Designated Approving Authority (DAA) that an information system is approved to operate in a particular security mode by using a prescribed set of safeguards at an acceptable level of risk.

*Recertification* and *re-accreditation* are required when changes occur in the system or its environment, or after a defined period of time after accreditation.

### Define System Security Requirements

For this activity, the information systems security engineer identifies one or more solution sets that can satisfy the IPP's information protection needs. A solution set consists of the following items:

- Preliminary security CONOPS
- The system context
- The system security requirements

Based on the IP, the information systems security engineer, in collaboration with the customer, chooses the best solution among the solution sets.

The preliminary security CONOPS identifies the following:

- The information protection functions
- The information management functions
- The dependencies among the organization's mission
- The services provided by other entities

To develop the system context, the information systems security engineer performs the following functions:

- Uses systems engineering techniques to identify the boundaries of the system to be protected.
- Allocates security functions to the system as well as to external systems by analyzing the flow of data among the system to be protected and the external systems, and using the information compiled in the IPP and IMM.

The information systems security engineer produces the system security requirements, in collaboration with the systems engineers. Requirements should be unambiguous, comprehensive, and concise, and they should be obtained through the process of requirements analysis. The functional requirements and constraints on the design of the information security components include the following:

- Regulations
- The operating environment
- Targeting internal as well as external threats
- Customer needs

The information systems security engineer must also assess cryptographic needs and systems such as public key infrastructure (PKI).

Finally, the information systems security engineer reviews the security CONOPS, the security context, and the system security requirements with the customer to ensure that they meet the needs of the customer and are accepted by the customer.

### Note

An important consideration in the entire process is the generation of appropriate and complete documentation. This documentation will be used to support the C&A process and should be developed to meet the C&A requirements.

### Design System Security Architecture

In this stage, the information systems security engineer performs a *functional decomposition* of the requirements that can be used to select the components required to implement the designated functions. Tools and techniques such as timeline analysis, flow block diagrams, and a requirements allocation sheet are used to accomplish the decomposition. The result of the functional decomposition is the *functional architecture* of the information security system.

In the decomposition process, the performance requirements at the higher level are mapped onto the lower-level functions to ensure that the resulting system performs as required. Also, as part of this activity, the information systems security engineer determines, at a functional level, the security services that should be assigned to the system to be protected as well as to external systems. Such services include encryption, key management, and digital signatures. Because implementations are not specified in this activity, a complete risk analysis is not possible. General risk analysis, however, can be done by estimating the vulnerabilities in the classes of components that are likely to be used.

### Develop Detailed Security Design

The detailed security design is accomplished through continuous assessments of risks and the comparison of these risks with the information system security requirements. This design activity involves both the SE and ISSE professionals and specifies the system and components, but does not specify products or vendors.

In conducting this activity, the information systems security engineer performs the following functions:

- Develops specifications such as Common Criteria protection profiles
- Maps security mechanisms to system security design elements
- Catalogs candidate commercial off-the-shelf (COTS) products
- Catalogs candidate government off-the-shelf (GOTS) products
- Catalogs custom security products
- Qualifies external and internal element and system interfaces

The results of this effort should include a revised security CONOPS, identification of failures to meet the security requirements, meeting of the customer's design constraints, and placing of the design documents under configuration control.

### Implement System Security

This activity bridges the design phase and the operational phase. It includes a system effectiveness assessment that provides evidence that the system meets the requirements and needs of the mission. Security accreditation usually follows this assessment.

The information systems security engineer approaches this task by doing the following:

- Applying information protection assurance mechanisms related to system implementation and testing
- Verifying that the implemented system does address and protect against the threats itemized in the original threat assessment
- Providing input to the C&A process
- Providing input to and reviewing the evolving system life-cycle support plans
- Providing input to and reviewing the operational procedures
- Providing input to and reviewing the maintenance training materials
- Taking part in multidisciplinary examinations of all system issues and concerns

This activity identifies the specific components of the information system security solution. In selecting these components, the information system security engineer must consider the following items:

- Cost
- Form factor
- Reliability
- Availability now and in the future
- Risk to system caused by substandard performance
- Conformance to design specifications
- Compatibility with existing components
- Meeting or exceeding evaluation criteria (Typical evaluation criteria include the Commercial COMSEC Evaluation Program [CCEP], National Information Assurance Partnership [NIAP], Federal Information Processing Standards [FIPS], NSA criteria, and NIST criteria.)

In some cases, components might have to be built and customized to meet the requirements if no suitable components are available for purchase or lease.

In addition, the systems and design engineers in cooperation with the information systems security engineer are involved with the following:

- Developing test procedures to ensure that the designed system performs as required; these procedures should incorporate the following:Test planning, to include facilities, schedule, personnel, tools, and required resourcesIntegration testingFunctional testing to ensure that systems and subsystems operate properlyGeneration of test reports
- Tests of all interfaces, as feasible
- Conducting unit testing of components
- Developing documentation and placing documentation under version control; the documentation should include the following:Installation proceduresOperational proceduresSupport proceduresMaintenance proceduresDefects discovered in the procedures

### Assess Information Protection Effectiveness

This activity, even though listed last, must be conducted as part of all the activities of the complete ISSE and SE processes. [Table 4-3](ch04.html#assess_information_protection_effect-003) summarizes the tasks of the Assess Information Protection activity that correspond to the other activities of the ISSE process.

As noted previously, there is a one-to-one pairing of the SE and ISSE processes. This pairing is described in the IATF document 3.1 and summarized in [Table 4-4](ch04.html#corresponding_se_and_isse_activities).

**Table 4.3. Assess Information Protection Effectiveness Tasks and Corresponding ISSE Activities**

| Assess Information Protection ISSE Activity | Effectiveness Tasks |
| --- | --- |
| Discover information protection needs | Present the process overview. |
|  | Summarize the information model. |
|  | Describe threats to the mission or business through information attacks. |
|  | Establish security services to counter those threats and identify their relative importance to the customer. |
|  | Obtain customer agreement on the conclusions of this activity as a basis for determining the system security effectiveness. |
| Define system security requirements | Ensure that the selected solution set meets the mission or business security needs. |
|  | Coordinate the system boundaries. |
|  | Present security context, security CONOPS, and system security requirements to the customer and gain customer concurrence. |
|  | Ensure that the projected security risks are acceptable to the customer. |
| Design system security architecture | Begin the formal risk analysis process to ensure that the selected security mechanisms provide the required security services, and explain to the customer how the security architecture meets the security requirements. |
| Develop detailed security design | Review how well the selected security services and mechanisms counter the threats by performing an interdependency analysis to compare desired to actual security service capabilities. |
|  | Once completed, the risk assessment results, particularly any mitigation needs and residual risk, will be documented and shared with the customer to obtain their concurrence. |
| Implement system security | The risk analysis will be conducted or updated. |
|  | Strategies will be developed for the mitigation of identified risks. |
|  | Identify possible mission impacts and advise the customer and the customer's Certifiers and Accreditors. |

**Table 4.4. Corresponding SE and ISSE Activities**

| SE Activities | ISSE Activities |
| --- | --- |
| **Discover needs** The systems engineer helps the customer understand and document the information management needs that support the business or mission. Statements about information needs may be captured in an information management model (IMM). | **Discover information protection needs** The information systems security engineer helps the customer understand the information protection needs that support the mission or business. Statements about information protection needs may be captured in an Information Protection Policy (IPP). |
| **Define system requirements** The systems engineer allocates identified needs to systems. A system context is developed to identify the system environment and to show the allocation of system functions to that environment. A preliminary system concept of operations (CONOPS) is written to describe operational aspects of the candidate system (or systems). Baseline requirements are established. | **Define system security requirements** The information systems security engineer allocates information protection needs to systems. A system security context, a preliminary system security CONOPS, and baseline security requirements are developed. |
| **Design system architecture** The systems engineer performs functional analysis and allocation by analyzing candidate architectures, allocating requirements, and selecting mechanisms. The systems engineer identifies components, or elements, allocates functions to those elements, and describes the relationships between the elements. | **Design system security architecture** The information systems security engineer works with the systems engineer in the areas of functional analysis and allocation by analyzing candidate architectures, allocating security services, and selecting security mechanisms. The information systems security engineer identifies components, or elements, allocates security functions to those elements, and describes the relationships between the elements. |
| **Develop detailed design** The systems engineer analyzes design constraints, analyzes trade-offs, does detailed system design, and considers life-cycle support. The systems engineer traces all of the system requirements to the elements until all are addressed. The final detailed design results in component and interface specifications that provide sufficient information for acquisition when the system is implemented. | **Develop detailed security design** The information systems security engineer analyzes design constraints, analyzes trade-offs, does detailed system and security design, and considers life-cycle support. The information systems security engineer traces all of the system security requirements to the elements until all are addressed. The final detailed security design results in component and interface specifications that provide sufficient information for acquisition when the system is implemented. |
| **Implement system** The systems engineer moves the system from specifications to the tangible. The main activities are acquisition, integration, configuration, testing, documentation, and training. Components are tested and evaluated to ensure that they meet the specifications. After successful testing, the individual components—hardware, software, and firmware—are integrated, properly configured, and tested as a system. | **Implement system security** The information systems security engineer participates in a multidisciplinary examination of all system issues and provides input to C&A process activities, such as verification that the system as implemented protects against the threats identified in the original threat assessment; tracking of information protection assurance mechanisms related to system implementation and testing practices; and providing input to system life-cycle support plans, operational procedures, and maintenance training materials. |
| **Assess effectiveness** The results of each activity are evaluated to ensure that the system will meet the users' needs by performing the required functions to the required quality standard in the intended environment. The systems engineer examines how well the system meets the needs of the mission. | **Assess information protection effectiveness** The information systems security engineer focuses on the effectiveness of the information protection — whether the system can provide the confidentiality, integrity, availability, authentication, and nonrepudiation for the information it is processing that is required for mission success. |

## The systems development life cycle

National Institute of Standards and Technology (NIST) Special Publication 800-14, "Generally Accepted Principles and Practices for Securing Information Technology Systems," defines the SDLC in terms of five phases:

1. Initiation
2. Development/acquisition
3. Implementation
4. Operation/maintenance
5. Disposal

### Initiation

The need for the system and its purpose are documented. A sensitivity assessment is conducted as part of this phase. A sensitivity assessment evaluates the sensitivity of the IT system and the information to be processed.

### Development/Acquisition

In this phase, which includes the development and acquisition activities, the system is designed, developed, programmed, and acquired. Security requirements are developed simultaneously with the definition of the system requirements. The information security requirements include such items as access controls and security awareness training.

### Implementation

Implementation involves installation, testing, security testing, and accreditation. During installation, security features should be enabled and configured. Also, system testing should be performed to ensure that the components function as planned. System security accreditation is performed in this phase. Accreditation is the formal authorization for system operation by the accrediting official and an explicit acceptance of risk.

### Operation/Maintenance

The system performs its designed functions. This phase includes security operations, modification or addition of hardware or software, administration, operational assurance, monitoring, and audits. These activities include performing backups, conducting training classes, managing cryptographic keys, and updating security software.

### Disposal

This last phase includes disposition of system components and products (such as hardware, software, and information), disk sanitization, archiving files, and moving equipment. Information may be moved to another system, archived, discarded, or destroyed. Keys for encrypted data should be stored in the event that the information is needed in the future. Data on magnetic media should be purged by overwriting, degaussing, or destruction.

## Information Systems Security and the SDLC

A number of NIST documents describe methodologies and principles for incorporating information systems security into the SDLC. The primary documents are as follows:

- "Generally Accepted Principles and Practices for Securing Information Technology Systems," SP 800-14, National Institute of Standards and Technology. This publication defines eight system security principles and 14 practices.
- "Engineering Principles for Information Technology Security (EP-ITS), A Baseline for Achieving Security," SP 800-27, National Institute of Standards and Technology. This document develops a set of 33 engineering principles for information technology security, which provide a system-level perspective of information system security. These 33 principles incorporate the concepts developed in the 8 principles and 14 practices detailed in SP 800-14.
- "Security Considerations in the Information System Development Life Cycle," SP 800-64, National Institute of Standards and Technology. NIST SP 800-64 details a framework for incorporating information systems security into all the phases of the SDLC activity, using cost-effective control measures.

### Generally accepted principles for securing information technology

The Organization for Economic Cooperation and Development (OECD) guidelines (`www.oecd.org`) for the security of information systems were the foundation for the following eight information security principles of NIST Special Publication 800-14:

- Computer security supports the mission of the organization.
- Computer security is an integral element of sound management.
- Computer security should be cost-effective.
- Systems owners have security responsibilities outside their own organizations.
- Computer security responsibilities and accountability should be made explicit.
- Computer security requires a comprehensive and integrated approach.
- Computer security should be periodically reassessed.
- Computer security is constrained by societal factors.

### Common Practices for Securing Information Technology

NIST SP 800-14 also lists the following common IT practices for incorporating information system security into the SDLC:

- **Policy**— Have in place the following three types of policies:A *program policy* to create and define a computer security programAn *issue-specific policy* to address specific areas and issuesA *system-specific policy* to focus on decisions made by managementThese policies are sometimes referred to as plans, procedures, or directives.
- **Program management** — Management of computer security at appropriate multiple levels with centralized enforcement and oversight.
- **Risk management** — The process of assessing risk, taking steps to reduce risk to an acceptable level, and maintaining that level of risk.
- **Life-cycle planning** — Managing security by planning throughout the system life cycle. A security plan should be developed prior to initiation of the life cycle activities so that it can be followed during the life-cycle process. Recall that the IT system life cycle as defined in SP 800-14 is composed of the following five phases:InitiationDevelopment/AcquisitionImplementationOperation/MaintenanceDisposal
- **Personnel/user issues** — These issues relate to managers, users, and implementers and their authorizations and access to IT computing resources.
- **Preparing for contingencies and disasters** — Planning to ensure that the organization can continue operations in the event of disasters and disruptions.
- **Computer security incident handling** — Reacting quickly and effectively in response to malicious code and internal or external unauthorized intrusions.
- **Awareness and training** — Providing computer security awareness training to all personnel interacting with the IT systems.
- **Security considerations in computer support and operations** — Applying information system security principles to the tasks performed by system administrators and to external system support activities.
- **Physical and environmental security** — Implementing environmental and physical security controls, such as maintaining proper temperature and humidity and securing laptops and magnetic media.
- **Identification and authentication** — Implementing the access control measures of identification and authentication to ensure that unauthorized personnel do not have privileges to access the resources of an IT system.
- **Logical access control** — Technical means of enforcing the information system security policy to limit access to IT resources to authorized personnel.
- **Audit trails** — Recording system activity and providing the capability to accomplish individual accountability, detection of intrusions, reconstruction of past events, and identification of problems.
- **Cryptography** — Providing security services, including protecting the confidentiality and integrity of information and implementing electronic signatures.

### Engineering Principles for Information Technology Security

These 33 principles of NIST 800-27 (abbreviated as EP-ITS) are derived from concepts found in the 8 principles and 14 practices of SP 800-14 and provide a system-level approach to IT security.

1. Establish a sound security policy as the "foundation" for design.
2. Treat security as an integral part of the overall system design.
3. Clearly delineate the physical and logical security boundaries governed by associated security policies.
4. Reduce risk to an acceptable level.
5. Assume that external systems are insecure.
6. Identify potential trade-offs between reducing risk and increased costs and decrease in other aspects of operational effectiveness.
7. Implement layered security (ensure no single point of vulnerability).
8. Implement tailored system security measures to meet organizational security goals.
9. Strive for simplicity.
10. Design and operate an IT system to limit vulnerability and to be resilient in response.
11. Minimize the system elements to be trusted.
12. Implement security through a combination of measures distributed physically and logically.
13. Provide assurance that the system is, and continues to be, resilient in the face of unexpected threats.
14. Limit or contain vulnerabilities.
15. Formulate security measures to address multiple overlapping information domains.
16. Isolate public access systems from mission-critical resources (for example, data processes).
17. Use boundary mechanisms to separate computing systems and network infrastructures.
18. Where possible, base security on open standards for portability and interoperability.
19. Use common language in developing security requirements.
20. Design and implement audit mechanisms to detect unauthorized use and to support incident investigations.
21. Design security to allow for regular adoption of new technology, including a secure and logical technology upgrade process.
22. Authenticate users and processes to ensure appropriate access control decisions both within and across domains.
23. Use unique identities to ensure accountability.
24. Implement least privilege.
25. Do not implement unnecessary security mechanisms.
26. Protect information while it is being processed, in transit, and in storage.
27. Strive for operational ease of use.
28. Develop and exercise contingency or disaster recovery procedures to ensure appropriate availability.
29. Consider custom products to achieve adequate security.
30. Ensure proper security in the shutdown or disposal of a system.
31. Protect against all likely classes of attacks.
32. Identify and prevent common errors and vulnerabilities.
33. Ensure that developers are trained to develop secure software.

### Information System Development Cycle

Publication 800-64, "Security Considerations in the Information System Development Life Cycle," complements NIST Special Publications 800-14 and 800-27 and expands on the SDLC concepts presented in these two publications. [Table 4-5](ch04.html#information_systems_security_in_the_sdlc), taken from SP 800-64, illustrates information systems security as applied in the SDLC.

**Table 4.5. Information Systems Security in the SDLC**

|  | Initiation | Acquisition/ Development | Implementation | Operations/Maintenance | Disposition |
| --- | --- | --- | --- | --- | --- |
| SDLC | Needs determination: Perception of a need Linkage of need to mission and performance objectives Assessment of alternatives to capital assets Preparing for investment review and budgeting | Functional statement of need: Market research Feasibility study Requirements analysis Alternatives analysis Cost-benefit analysis Software conversion study Cost analysis Risk management plan Acquisition planning | Installation inspection Acceptance testing Initial user training Documentation | Performance measurement Contract modifications Operations Maintenance | Appropriateness of disposal Exchange and sale Internal organization screening Transfer and donation Contract closeout |
| Security considerations | Security categorization: Preliminary risk assessment | Risk assessment Security functional requirements analysis Security assurance requirements analysis Cost considerations and reporting Security planning Security control development Developmental security test and evaluation Other planning components | Inspection and acceptance Security control integration Security certification Security accreditation | Configuration management and control Continuous monitoring | Information preservation Media sanitization Hardware and software disposal |

The activities of each step in [Table 4-5](ch04.html#information_systems_security_in_the_sdlc), as described in NIST SP 800-64, are expanded in the following list:

- **Initiation phase:****Security categorization** — Defines three levels (low, moderate, or high) of potential impact on organizations or individuals should there be a breach of security (a loss of confidentiality, integrity, or availability). Security categorization standards assist organizations in making the appropriate selection of security controls for their information systems.**Preliminary risk assessment** — Results in an initial description of the basic security needs of the system. A preliminary risk assessment should define the threat environment in which the system will operate.
- **Acquisition and development phase:****Risk assessment** — An analysis that identifies the protection requirements for the system through a formal risk assessment process. This analysis builds on the initial risk assessment performed during the Initiation phase, but will be more in-depth and specific.**Security functional requirements analysis** — An analysis of requirements that may include the following components: a system security environment (that is, enterprise information security policy and enterprise security architecture) and security functional requirements.**Assurance requirements analysis security** — An analysis of requirements that address the developmental activities required and assurance evidence needed to produce the desired level of confidence that the information security will work correctly and effectively. The analysis, based on legal and functional security requirements, will be used as the basis for determining how much and what kinds of assurance are required.**Cost considerations and reporting** — Determines how much of the development cost can be attributed to information security over the life cycle of the system. These costs include hardware, software, personnel, and training.**Security planning** — Ensures that agreed-upon security controls, planned or in place, are fully documented. The security plan also provides a complete characterization or description of the information system as well as attachments or references to key documents supporting the agency's information security program (for example, configuration management plan, contingency plan, incident response plan, security awareness and training plan, rules of behavior, risk assessment, security test and evaluation results, system interconnection agreements, security authorizations and accreditations, and plan of action and milestones).**Security control development** — Ensures that security controls described in the respective security plans are designed, developed, and implemented. For information systems currently in operation, the security plans for those systems may call for the development of additional security controls to supplement the controls already in place or the modification of selected controls that are deemed to be less than effective.**Developmental security test and evaluation** — Ensures that security controls developed for a new information system are working properly and are effective. Some types of security controls (primarily those controls of a nontechnical nature) cannot be tested and evaluated until the information system is deployed— these controls are typically management and operational controls.**Other planning components** — Ensures that all necessary components of the development process are considered when incorporating security into the life cycle. These components include selection of the appropriate contract type, participation by all necessary functional groups within an organization, participation by the certifier and accreditor, and development and execution of necessary contracting plans and processes.
- **Implementation phase:****Inspection and Acceptance** — Ensures that the organization validates and verifies that the functionality described in the specification is included in the deliverables.**Security Control Integration** — Ensures that security controls are integrated at the operational site where the information system is to be deployed for operation. Security control settings and switches are enabled in accordance with vendor instructions and available security implementation guidance.**Security certification** — Ensures that the controls are effectively implemented through established verification techniques and procedures and gives organization officials confidence that the appropriate safeguards and countermeasures are in place to protect the organization's information system. Security certification also uncovers and describes the known vulnerabilities in the information system.**Security accreditation** — Provides the necessary security authorization of an information system to process, store, or transmit information that is required. This authorization is granted by a senior organization official and is based on the verified effectiveness of security controls to some agreed-upon level of assurance and an identified residual risk to agency assets or operations.
- **Operations and maintenance phase:****Configuration management and control** — Ensures adequate consideration of the potential security impacts due to specific changes to an information system or its surrounding environment. Configuration management and configuration control procedures are critical to establishing an initial baseline of hardware, software, and firmware components for the information system and subsequently controlling and maintaining an accurate inventory of any changes to the system.**Continuous monitoring** — Ensures that controls continue to be effective in their application through periodic testing and evaluation. Security control monitoring (that is, verifying the continued effectiveness of those controls over time) and reporting the security status of the information system to appropriate agency officials is an essential activity of a comprehensive information security program.
- **Disposition phase:****Information preservation**— Ensures that information is retained, as necessary, to conform to current legal requirements and to accommodate future technology changes that may render the retrieval method obsolete.**Media sanitization**— Ensures that data is deleted, erased, and written over, as necessary.**Hardware and software disposal**— Ensures that hardware and software is disposed of as directed by the information system security officer. After discussing these phases and the information security steps in detail, the guide provides specifications, tasks, and clauses that can be used in a request for proposal (RFP) to acquire information security features, procedures, and assurances.

# Risk Management

NIST Special Publication 800-30, "Risk Management Guide for Information Technology Systems," defines *risk management* as comprising three processes: risk assessment, risk mitigation, and evaluation and assessment.

Risk assessment consists of the following:

- Identification and evaluation of risks
- Identification and evaluation of risk impacts
- Recommendation of risk-reducing measures

Risk mitigation involves the following:

- Prioritizing appropriate risk-reducing measures recommended from the risk assessment process
- Implementing appropriate risk-reducing measures recommended from the risk assessment process
- Maintaining the appropriate risk-reducing measures recommended from the risk assessment process

Evaluation and assessment includes a continuous evaluation process. For example, the designated approving authority (DAA) has the responsibility for determining if the residual risk in the system is acceptable or if additional security controls should be implemented to achieve accreditation of the IT system.

The DAA is the primary government official responsible for implementing system security. The DAA is an executive with the authority and ability to balance the needs of the system with the security risks. This person determines the acceptable level of residual risk for a system and must have the authority to oversee the budget and IS business operations of systems under his/her purview.

## Definitions

It is important to understand key definitions associated with risk management. These terms are taken from SP 800-30 and are useful in the discussion of applying risk management to the SDLC process.

### Risk

*Risk* is "a function of the likelihood of a given threat-source's exercising a particular potential vulnerability, and the resulting impact of that adverse event on the organization." Risk defines the probability for loss or the likelihood that a threat will find a vulnerability and potentially compromise a system.

### Threat

A *threat* is defined as "the potential for a threat-source to exercise (accidentally trigger or intentionally exploit) a specific vulnerability." Threat is the potential for harm.

### Threat-source

A *threat-source* is defined as "either (1) intent and method targeted at the intentional exploitation of a vulnerability or (2) a situation and method that may accidentally trigger a vulnerability." Common threat-sources include *natural threats*, such as storms and floods, *human threats*, such as malicious attacks and unintentional acts, and *environmental threats*, such as power failure and liquid leakage. Cyber threats focus in on areas such as worms, viruses and phishing attempts.

### Vulnerability

A *vulnerability* is defined as "a flaw or weakness in system security procedures, design, implementation, or internal controls that could be exercised (accidentally triggered or intentionally exploited) and result in a security breach or a violation of the system's security policy." A vulnerability is a weakness that allows a threat to manifest itself against an organization.

### Impact

*Impact* refers to the "magnitude of harm that could be caused by a threat exploiting a vulnerability. The level of impact is governed by the potential mission impacts and in turn produces a relative value for the IT assets and resources affected (the criticality and sensitivity of the IT system components and data)."

## Risk Management and the SDLC

The risk management process minimizes the impact of threats realized and provides a foundation for effective management decision-making. Thus, it is very important that risk management be a part of the system development life cycle. The three risk management processes, risk assessment, risk mitigation, and evaluation and assessment, are to be performed during each of the five phases of the SDLC. [Table 4-6](ch04.html#risk_management_in_the_sdlc_cycle), taken from NIST SP 800-30, details the risk management activities that should be performed for each SDLC phase.

**Table 4.6. Risk Management in the SDLC Cycle**

| SDLC | Phase | Risk Management Activities |
| --- | --- | --- |
| Phase 1: Initiation | The need for an IT system is expressed and the purpose and scope of the IT system is documented. | Identified risks are used to support the development of the system requirements, including security requirements, and a security concept of operations (strategy). |
| Phase 2: Development | The IT system is designed, purchased, programmed, developed, or otherwise constructed. | The risks identified can be used to support the security analysis of the IT system that may lead to architecture and design tradeoffs during system development. |
| Phase 3: Implementation | The system security features should be configured, enabled, tested, and verified. | The risk management process Implementation supports the assessment of the system implementation against its requirements and within its modeled operational environment. Decisions regarding risks identified must be made prior to system operation. |
| Phase 4: Operation | The system performs its functions. Typically, the system is being modified on an ongoing basis through the addition of hardware and software and by changes to organizational processes, policies, and procedures. | Risk management activities are performed for periodic system reauthorization (or reaccreditation) or whenever major changes are made to an IT system in its operational, production environment (for example, new system interfaces). |
| Phase 5: Disposal | This phase may involve the disposition of information, hardware, and software. Activities may include moving, archiving, discarding, or destroying information and sanitizing the hardware and software. | Risk management activities are performed for system components that will be disposed of or replaced to ensure that the hardware and software are properly disposed of, that residual data is appropriately handled, and that system migration is conducted in a secure and systematic manner. |

To be effective, risk management must be supported by management and information system security practitioners. Some of the key personnel that should actively participate in the risk management activities are as follows:

- **Senior management**— Provides the required resources and meets responsibilities under the principle of due care
- **Chief information officer (CIO)**— Considers risk management in IT planning, budgeting, and meeting system performance requirements
- **System and information owners**— Ensures that controls and services are implemented to address information system confidentiality, integrity, and availability
- **Business and functional managers**— Makes trade-off decisions regarding business operations and IT procurement that affect information security
- **Information system security officer (ISSO)**— Participates in applying methodologies to identify, evaluate, and reduce risks to the mission-critical IT systems
- **IT security practitioners**— Ensures the correct implementation of IT system information system security requirements
- **Security awareness trainers**— Incorporates risk assessment in training programs for the organization's personnel

### Risk Assessment

Risk assessment comprises the following steps:

1. System characterization
2. Threat identification
3. Vulnerability identification
4. Control analysis
5. Likelihood determination
6. Impact analysis
7. Risk determination
8. Control recommendations
9. Results documentation

Each of these steps is summarized in the following sections.

#### System Characterization

This step characterizes and defines the scope of the risk assessment process. During this step, the following information about the system must be gathered:

- Software
- Hardware
- Data
- System interfaces
- IT system users
- IT system support personnel
- System mission
- Criticality of the system and data
- System and data sensitivity
- Functional system requirements
- System security policies
- System security architecture
- Network topology
- Information storage protection
- System information flow
- Technical security controls
- Physical security environment
- Environmental security

Questionnaires, on-site interviews, review of documents, and automated scanning tools are used to obtain the required information. The output from this step is as follows:

- Characterization of the assessed IT system
- Comprehension of the IT system environment
- Delineation of the system boundary

#### Threat Identification

This step identifies potential threat-sources and compiles a statement of the threat-sources that relate to the IT system under evaluation. Sources of threat information include the Federal Computer Incident Response Center (FedCIRC), intelligence agencies, mass media, and Web-based resources.

The output from this step is a statement that provides a list of threat-sources that could exploit the system's vulnerabilities.

#### Vulnerability Identification

This step results in a list of system vulnerabilities that might be exploited by potential threat-sources. Vulnerabilities can be identified through vulnerability analysis, including information from previous information assessments; audit reports; the NIST vulnerability database (`http://icat.nist.gov/icat.cfm`); FedCIRC and DOE security bulletins; vendor data; commercial computer incident response teams; and system software security analysis.

Testing of the IT system is also an important tool in identifying vulnerabilities. Testing can include the following:

- Security test and evaluation (ST&E) procedures
- Penetration-testing techniques
- Automated vulnerability scanning tools

This phase also involves determining whether the security requirements identified during system characterization are being met. Usually, the security requirements are listed in a table with a corresponding statement about how the requirement is or is not being met. The checklist addresses management, operational, and technical information system security areas. The result of this effort is a *security requirements checklist*. Some useful references for this activity are the Computer Security Act of 1987, the Privacy Act of 1974, the organization's security policies, industry best practices, and NIST SP 800-26, *Security Self-Assessment Guide for Information Technology Systems*.

The output from this step is a list of system vulnerabilities or observations that could be exploited by the potential threat-sources.

#### Control Analysis

This step analyzes the controls that are in place or in the planning stage to minimize or eliminate the probability that a threat will exploit vulnerability in the system.

Controls can be implemented through technical means such as computer hardware or software, encryption, intrusion detection mechanisms, and identification and authentication subsystems. Other controls, such as security policies, administrative actions, and physical and environmental mechanisms, are considered nontechnical controls. Both technical and nontechnical controls can further be classified as preventive or detective controls. As the names imply, preventive controls attempt to anticipate and stop attacks. Examples of preventive, technical controls are encryption and authentication devices. Detective controls are used to discover attacks or events through such means as audit trails and intrusion detection systems.

Changes in the control mechanisms should be reflected in the security requirement checklist.

The output of this step is a list of current and planned control mechanisms for the IT system to reduce the likelihood that a vulnerability will be exercised and to reduce the impact of an attack or event.

#### Likelihood Determination

This activity develops a rating that provides an indication of the probability that a potential vulnerability might be exploited based on the defined threat environment. This rating takes into account the type of vulnerability, the capability and motivation of the threat-source, and the existence and effectiveness of information system security controls. The likelihood levels are given as high, medium, and low, as illustrated in [Table 4-7](ch04.html#definitions_of_likelihood).

**Table 4.7. Definitions of Likelihood**

| Level of Likelihood | Definition of Likelihood |
| --- | --- |
| High | A highly motivated and capable threat-source and ineffective controls to prevent exploitation of the associated vulnerability |
| Medium | A highly motivated and capable threat-source and controls that might impede exploitation of the associated vulnerability |
| Low | Lack of motivation or capability in the threat-source or controls in place to prevent or significantly impede the exploitation of the associated vulnerability |

#### Impact Analysis

Three important factors should be considered in calculating the negative impact of a threat realized:

- The mission of the system, including the processes implemented by the system
- The criticality of the system, determined by its value and the value of the data to the organization
- The sensitivity of the system and its data

The information necessary to conduct an impact analysis can be obtained from existing organizational documentation, including a business impact analysis (BIA), or mission impact analysis report, as it is sometimes called. This document uses either quantitative or qualitative means to determine the impacts caused by compromise or harm to the organization's information assets. An attack or adverse event can result in compromise or loss of information system confidentiality, integrity, and availability. As with the likelihood determination, the impact on the system can be qualitatively assessed as high, medium, or low, as shown in [Table 4-8](ch04.html#definitions_of_likelihood-004).

The following additional items should be included in the impact analysis:

- The estimated frequency of the threat-source's exploitation of a vulnerability on an annual basis
- The approximate cost of each of these occurrences
- A weight factor based on the relative impact of a specific threat exploiting a specific vulnerability

The output of this step is the magnitude of impact: high, medium, or low.

**Table 4.8. Definitions of Likelihood**

| Impact Magnitude | Definition of Impact |
| --- | --- |
| High | Possibility of costly loss of major tangible assets or resources; might cause significant harm or impedance to the mission of an organization; might cause significant harm to an organization's reputation or interest; might result in human death or injury. |
| Medium | Possibility of costly loss of tangible assets or resources; might cause harm or impedance to the mission of an organization; might cause harm to an organization's reputation or interest; might result in human injury. |
| Low | Possibility of loss of some tangible assets or resources; might noticeably affect an organization's mission; might noticeably affect an organization's reputation or interest. |

#### Risk Determination

This step determines the level of risk to the IT system. The risk is assigned for a threat/vulnerability pair and is a function of the following characteristics:

- The likelihood that a particular threat-source will exploit an existing IT system vulnerability
- The magnitude of the resulting impact of a threat-source successfully exploiting the IT system vulnerability
- The adequacy of the existing or planned information system security controls for eliminating or reducing the risk

Mission risk is calculated by multiplying the threat likelihood ratings (the probability that a threat will occur) by the impact of the threat realized. A useful tool for estimating risk in this manner is the risk-level matrix. An example risk-level matrix is shown in [Table 4-9](ch04.html#a_risk-level_matrix_example). In the table, a high likelihood that the threat will occur is given a value of 1.0; a medium likelihood is assigned a value of 0.5; and a low likelihood of occurrence is given a rating of 0.1. Similarly, a high impact level is assigned a value of 100, a medium impact level 50, and a low impact level 10.

Using the risk level as a basis, the next step is to determine the actions that senior management and other responsible individuals must take to mitigate estimated risk. General guidelines for each level of risk follow:

- **High-risk level**— At this level, there is a high level of concern and a strong need for a plan for corrective measures to be developed as soon as possible.
- **Medium-risk level**— For medium risk, there is concern and a need for a plan for corrective measures to be developed within a reasonable period of time.
- **Low-risk level**— For low risk, the system's DAA must decide whether to accept the risk or implement corrective actions.

**Table 4.9. A Risk-Level Matrix Example**

| Likelihood of Threat | Low Impact (10) | Medium Impact (50) | High Impact (100) |
| --- | --- | --- | --- |
| High (1.0) | Low 10 × 1.0 = 10 | Medium 50 × 1.0 = 50 | High 100 × 1.0 = 100 |
| Medium (0.5) | Low 10 × 0.5 = 5 | Medium 50 × 0.5 = 25 | High 100 × 0.5 = 50 |
| Low (0.1) | Low 10 × 0.1 = 1 | Medium 50 × 0.1 = 5 | High 100 × 0.1 = 10 |

The output of the risk determination step is risk level of high, medium, or low.

#### Control Recommendations

This step specifies the controls to be applied for risk mitigation. To specify appropriate controls, the following issues must be considered:

- Organizational policy
- Cost-benefit
- Operational impact
- Feasibility
- Applicable legislative regulations
- The overall effectiveness of the recommended controls
- Safety, reliability

The output of this step is a recommendation of controls and any alternative solutions to mitigate risk.

#### Results Documentation

The final step in the risk assessment process is the development of a risk assessment report. This report is directed at management and should contain information to support appropriate decisions on budget, policies, procedures, management, and operational issues.

The output of this step is a risk assessment report that describes threats and vulnerabilities, risk measurements, and recommendations for implementation of controls.

### Risk Mitigation

Risk mitigation prioritizes, evaluates, and implements the controls that are an output of the risk assessment process. Because risk can never be completely eliminated and control implementation must make sense under a cost-benefit analysis, a least-cost approach with minimal adverse impact on the IT system is usually taken.

#### Risk Mitigation Options

Risk mitigation can be classified into the following options:

- **Risk assumption**— Accept the risk and keep operating.
- **Risk avoidance**— Forgo some functions.
- **Risk limitation**— Implement controls to minimize the adverse impact of threats realized.
- **Risk planning**— Develop a risk mitigation plan to prioritize, implement, and maintain controls.
- **Research and development**— Research control types and options.
- **Risk transference**— Transfer risk to other sources, such as purchasing insurance.

#### Categories of Controls

Controls to mitigate risks can be broken into the following categories:

- Technical
- Management
- Operational
- A combination of the above

Technical controls comprise the following:

- **Supporting controls**— These controls implement identification, cryptographic key management, security administration, and system protections.
- **Preventive controls**— Preventive technical controls include authentication, authorization, access control enforcement, nonrepudiation, protected communications, and transaction privacy.
- **Detection and recovering controls**— These technical controls include audit, intrusion detection and containment, proof of wholeness (system integrity), restoration to a secure state, and virus detection and eradication.

Management controls comprise the following:

- **Preventive controls**— Preventive management controls include assigning responsibility for security, and developing and maintaining security plans, personnel security controls, and security awareness and technical training.
- **Detection controls**— Detection controls involve background checks, personnel clearance, periodic review of security controls, periodic system audits, risk management, and authorization of IT systems to address and accept residual risk.
- **Recovery controls**— These controls provide continuity of support to develop, test, and maintain the continuity of the operations plan and establish an incident response capability.

Operational security controls are divided into preventive and detection types. Their functions are listed as follows:

- **Preventive controls**— These operational controls comprise controlling media access and disposal, limiting external data distribution, controlling software viruses, securing wiring closets, providing backup capability, protecting laptops and personal computers, protecting IT assets from fire damage, providing an emergency power source, and controlling humidity and temperature.
- **Detection controls**— Detection operation controls include providing physical security through the use of items such as cameras and motion detectors and ensuring environmental security by using smoke detectors, sensors, and alarms.

### Evaluation and Assessment

The risk that remains after the implementation of controls is called the *residual risk*. All systems will have residual risk because it is virtually impossible to completely eliminate risk to an IT system. An organization's senior management or the DAA is responsible for authorizing or accrediting the IT system to begin or continue to operate. The authorization or accreditation must take place every three years in federal agencies or whenever major changes are made to the system. The DAA signs a statement accepting the residual risk when accrediting the IT system for operation. If the DAA determines that the residual risk is at an unacceptable level, the risk management cycle must be redone with the objective of lowering the residual risk to an acceptable level.

# Calculating and Managing Risk

In some cases, it is important to be able to assign a numeric value to a risk to be used in future analysis. The general calculations for risk are *single loss expectancy* (SLE) and *annual loss expectancy* (ALE). The two formulas are:

> SLE = asset value × exposure factor
> 
> ALE = SLE × annualized rate of occurrence (ARO)

With SLE, the asset value is how much is the asset worth. Remember, security revolves around understanding and managing your critical assets. The exposure factor is how much of the asset will be lost if the threat occurs. This is often represented as a percent.

With ALE, the annualized rate of occurrence is how often this will occur. This is critical to understand the true impact a risk will have on an organization. In many cases, organizations will use the SLE, which severely underestimates the true damage of a risk. For example, if the SLE for a worm is $500,000, but this worm could impact the organization ten times in one year, the true damage is $5 million, not $500,000.

Once an organization calculates the risk, it can then be used to perform either quantitative or qualitative analysis. Quantitative analysis involves assigning exact numeric values to each risk. While this is often beneficial in business decision making because it assigns an exact dollar value to each risk, it is often not recommended for security because:

- Quantitative analysis is very time consuming. It often takes nine months to calculate the risk and nine months to fix it. With security, you should be spending more time on fixing the risk than identifying it.
- If it takes nine months to calculate the risk, by the time you are done determining it, it is no longer accurate because it is constantly changing and being updated.
- Because risk is always changing, an organization does not need to know numeric values for all of its risks; it just needs to know the top two or three items it should focus its energy on.

For these reasons, qualitative analysis is much more valuable because it involves binning, (putting items into categories)—that is, prioritizing risk into categories such as 1–5, where 5 is the highest risk and 1 is the lowest. Now an organization can focus in on the top risks and once these have been reduced, it can re-calculate the risks and focus on the next set of high priority items.

# Summary

The formal SE process and the corresponding ISSE process provide a solid framework for specifying, designing, implementing, and assessing high-quality and secure information systems. Similarly, risk management and information system security principles applied throughout the SDLC ensure that the target system maintains an acceptable level of risk from its development phase through to its disposal phase. The layered Defense-in-Depth strategy supports the SE, ISSE, SDLC, and risk management processes in providing an effective implementation strategy for securing the enclave boundary.
