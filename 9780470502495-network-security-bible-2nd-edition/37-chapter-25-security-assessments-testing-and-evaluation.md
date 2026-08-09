# Chapter 25. Security Assessments, Testing, and Evaluation

**IN THIS CHAPTER**

- **Understanding the Systems Security Engineering Capability Maturity Model**
- **Discussing other assessment methodologies**
- **Understanding certification and accreditation**
- **Exploring penetration testing**
- **Reviewing audit and monitoring procedures**

Assurance is defined as the measure of confidence that the security features and architecture of an information system accurately mediate and enforce an organization's information system security policy. A number of different approaches and methodologies have been developed to evaluate assurance. These techniques range from formal methods to probing and testing a network for vulnerabilities. This chapter addresses the most prominent approaches for assurance evaluation and testing developed by government and private organizations.

# Information Assurance Approaches and Methodologies

An effective means to assess information system assurance is to determine if an organization has the appropriate technical, administrative, and organizational processes in place to enforce the organization's security policy. This section explores some methodologies that employ the process approach and derivatives thereof. Remember that the entire process is driven by understanding, managing, controlling, and mitigating risk to an organization's critical information.

## The Systems Security Engineering Capability Maturity Model

The Systems Security Engineering Capability Maturity Model (SSE-CMM) is based on the principle that information system security is a result of having good system security engineering processes in place. It is based on the Systems Engineering Capability Maturity Model (SE-CMM) and is maintained by the International Systems Security Engineering Association (ISSEA) at `www.issea.org`. The SSE-CMM defines the dimensions of domain and capability, which are used to measure the capability of an organization to perform specific activities. The *domain* dimension consists of all the practices that collectively define security engineering. These practices are called *base practices* (BPs) and they are grouped into *process areas* (PAs). The *capability* dimension represents *Generic Practices* (GPs) that indicate process management and institutionalization capability.

The SSE-CMM specifies 11 security engineering PAs and 11 organizational and project-related PAs in the domain dimension. BPs are mandatory characteristics that must exist within an implemented security engineering process before an organization can claim satisfaction in a given PA. The 22 PAs of the SSE-CMM, divided into security engineering and organizational/project processes, are given in [Tables 25-1](ch25.html#sse-cmm_security_engineering_processes) and [25-2](ch25.html#sse-cmm_project_and_organizational_proce), respectively.

**Table 25.1. SSE-CMM Security Engineering Processes**

| Process | Name |
| --- | --- |
| PA01 | Administer Security Controls |
| PA02 | Assess Impact |
| PA03 | Assess Security Risk |
| PA04 | Assess Threat |
| PA05 | Assess Vulnerability |
| PA06 | Build Assurance Argument |
| PA07 | Coordinate Security |
| PA08 | Monitor Security Posture |
| PA09 | Provide Security Input |
| PA10 | Specify Security Needs |
| PA11 | Verify and Validate Security |

The GPs are grouped in five levels of security engineering maturity. *Maturity* implies a potential for growth in capability and indicates both the richness of an organization's processes and the consistency with which they are applied throughout the organization. The five levels of GP maturity and their attributes are listed in [Table 25-3](ch25.html#sse-cmm_gp_maturity_levels).

**Table 25.2. SSE-CMM Project and Organizational Processes**

| Process | Name |
| --- | --- |
| PA12 | Ensure Quality |
| PA13 | Manage Configuration |
| PA14 | Manage Project Risk |
| PA15 | Monitor and Control Technical Effort |
| PA16 | Plan Technical Effort |
| PA17 | Define Organization's Systems Engineering Process |
| PA18 | Improve Organization's Systems Engineering Process |
| PA19 | Manage Product Line Evolution |
| PA20 | Manage Systems Engineering Support Environment |
| PA21 | Provide Ongoing Skills and Knowledge |
| PA22 | Coordinate with Suppliers |

**Table 25.3. SSE-CMM GP Maturity Levels**

| Level | Maturity |
| --- | --- |
| Level 1 — Performed Informally | 1.1 BPs are performed |
| Level 2 — Planned and Tracked | 2.1 Planning Performance, 2.2 Discipline Performance, 2.3 Verifying Performance, 2.4 Tracking Performance |
| Level 3 — Well Defined | 3.1 Defining a Standard Process, 3.2 Perform the Defined Process, 3.3 Coordinate the Process |
| Level 4 — Quantitatively Controlled | 4.1 Establishing Measurable Quality Goals, 4.2 Objectively Managing Performance |
| Level 5 — Continuously Improving | 5.1 Improving Organizational Capability, 5.2 Improving Process Effectiveness |

## NSA Infosec Assessment Methodology

The Infosec Assessment Methodology (IAM) was developed by the NSA (National Security Agency) to evaluate an organization's security posture and combines a subset of the SSE-CMM with a specialized criticality matrix. The IAM is designed to be useful to INFOSEC assessment suppliers and consumers. It evaluates the mission, organization, security policies and programs, information systems, and the threats to information systems. The goal is to determine the vulnerabilities of information systems and recommend appropriate countermeasures. As a reference point in understanding the IAM, the NSA defines the following levels of assessments, as summarized in [Table 25-4](ch25.html#levels_of_infosec_assessment).

**Table 25.4. Levels of INFOSEC Assessment**

| Assessment Level | Activity |
| --- | --- |
| Level 1 — Cooperative | Non-intrusive baseline evaluation of the information system security posture of an automated system. |
| Level 2 — Cooperative | "Hands-on" security systems evaluation. |
| Level 3 — Usually non-cooperative | Red team assessment with penetration testing. A Red team plays the part of the opposition or attacker of an information system. The Red team thinks like an adversary and tries to expose weaknesses in a system. The Red team is usually a part of the development team and provides feedback and recommendations for improving proposed designs and implementations. |

The IAM is a Level 1 type of assessment and is conducted in three phases: preassessment, onsite, and postassessment. The *preassessment phase* involves identifying the system and its boundaries and beginning to develop an assessment plan. Acquiring data and documentation, conducting interviews, and providing initial assessment results are accomplished in the *onsit*e phase. Then, the *postassessment* phase provides a final analysis and delivers the resultant findings.

The principal tool used in the IAM is the organizational criticality matrix. In the matrix, the relevant automated systems are assigned impact attributes based on their importance to the organization and the effect a compromise would have on the confidentiality, integrity, and availability of information. [Table 25-5](ch25.html#an_example_iam_organizational_criticalit) provides an example of an organizational criticality matrix for a health-care institution.

**Table 25.5. An Example IAM Organizational Criticality Matrix**

| Subject | Confidentiality | Integrity | Availability |
| --- | --- | --- | --- |
| Admissions | High | High | Medium |
| Emergency | Medium | High | High |
| Pharmacy | High | High | Medium |

## Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE)

The Carnegie Mellon University Software Engineering Institute (SEI) has developed a self-guided assessment methodology called the Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE). OCTAVE is conducted by identifying an entity's critical assets and corresponding threats, discovering and listing the vulnerabilities that are subject to exploitation by the threats, and developing safeguards against the identified threats to preserve the organization's mission of the organization.

## Federal Information Technology Security Assessment Framework

The Federal Information Technology Security Assessment Framework (FITSAF) is a method that can be applied by U.S. government agencies to perform the following functions:

- Properly apply existing policy and guidance
- Evaluate the state of extant security programs relative to organizational policy
- Establish a target for improvement
- Assess security controls for critical information systems

FITSAF has five levels of security capability based on the SEI Capability Maturity Model (CMM), as shown in [Table 25-6](ch25.html#fitsaf_capability_levels). Government agencies are expected to eventually achieve Level 5.

**Table 25.6. FITSAF Capability Levels**

| Level | Capability |
| --- | --- |
| Level 1 | 1.1 Documented Security Policy |
| Level 2 | 2.1 Documented Procedures Based on Security Policy, 2.2 Documented Security Controls Based on Security Policy |
| Level 3 | 3.1 Procedures Implemented, 3.2 Security Controls Implemented |
| Level 4 | 4.1 Procedures Tested and Reviewed, 4.2 Controls Tested and Reviewed |
| Level 5 | 5.1 Integrated Procedures and Controls |

# Certification and Accreditation

The certification and accreditation process is a checks and balances effort to ensure that identified security requirements are executed, with any remaining risk accepted by someone in authority. When certifying anything, whether it be building code compliance, personal knowledge, or information systems, there must exist a standard process by which similar homes/people/systems can be evaluated against a baseline accurately, every time. Once this certification effort is complete, someone in a position of authority must sign off on the certification. The act of the authority taking responsibility for placing an information system into operation is accreditation. Building inspectors, certification organizations, and information systems will be accredited as complying with a certain standard. The C&A process is implemented differently depending on the organization, with the common theme of ensuring that the information systems meet identified security standards.

The Department of Defense (DoD), National Institute of Standards Technology (NIST), and National Security Telecommunications and Information Systems Security Committee (NSTISSC) have each developed and defined certification and accreditation methods for information systems. The following is an excerpt of the C&A definition:

|  |  |  |
| --- | --- | --- |
| DoD (DIACAP) | NIST (SP 800-37) | NSTISSC (NIACAP) |
| "A comprehensive evaluation and validation of a DoD IS to establish the degree to which it complies with assigned IA controls based on standardized procedures" | "Comprehensive assessment of the management, operational, and technical security controls in an information system, made in support of security accreditation, to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security requirements for the system." | "Comprehensive evaluation of the technical and nontechnical security features of an IS and other safeguards, made in support of the accreditation process, to establish the extent to which a particular design and implementation meets a set of specified security requirements." |

The common theme across these C&A processes is that of a comprehensive approach to ensure that standard security requirements are executed. Each process defines the security standards and implementation methods, along with documentation requirements and re-certification timelines. Applicability of each process is shown here.

| Organizations | Applicability |
| --- | --- |
| DoD DIACAP | All DoD organizations and military components |
| NIST SP 800-37 | Federal Agencies (Non National Security Systems) |
| NSTISSC NIACAP | Federal Agency National Security Systems (Non-DoD) |

Please note, there is an overlap of DIACAP and NIACAP, in that the DIACAP also includes national security systems. The NIACAP is applicable for those National Security Systems not a part of the DoD.

The National Information Assurance Glossary, CNSS Instruction No. 4009, defines *certification* as a "comprehensive evaluation of the technical and nontechnical security safeguards of an information system (IS) to support the accreditation process that establishes the extent to which a particular design and implementation meets a set of specified security requirements." It defines *accreditation* as a "formal declaration by a Designated Accrediting Authority (DAA) that an IS is approved to operate in a particular security mode at an acceptable level of risk, based on the implementation of an approved set of technical, managerial, and procedural safeguards."

## NIACAP

The National Information Assurance Certification and Accreditation Process is specified in the National Security Telecommunications and Information Systems Security Instruction (NSTISSI) No. 1000. The NIACAP supports the certification that an information system meets and maintains documented accreditation requirements throughout the system's life cycle. An important document in the NIACAP is the *System Security Authorization Agreement* (SSAA). The SSAA is an evolving, but binding agreement among the principals in the NIACAP process that defines the boundary of the system to be certified, documents the requirements for accreditation, describes the system security architecture, documents test plans and procedures, and becomes the baseline security document.

There are three types of NIACAP accreditation:

- **Type accreditation**—Evaluates an application or system that is distributed to a number of different locations
- **Site accreditation**—Evaluates the applications and systems at a specific, self-contained location
- **System accreditation**—Evaluates a major application or general support system

### The Four Phases of NIACAP

To conduct an NIACAP, it is necessary to understand the IS, the business needs, the security requirements, and the resource costs. The intended outcome is to ensure compliance with SSAA, certify the IS, receive accreditation, and operate the system in conformance with the SSAA. These activities are conducted in four phases, as shown in [Table 25-7](ch25.html#the_four_phases_of_niacap-069).

**Table 25.7. The Four Phases of NIACAP**

| Phase | Activities |
| --- | --- |
| 1 — Definition | Understand the IS architecture and business environment; determine security requirements, estimate levels of effort, define the certification and accreditation boundary, and develop and approve final phase 1 version of SSAA. |
| 2 — Verification | Verify evolving system compliance with information security and risk requirements specified in SSAA, refine the SSAA, conduct system development and integration, and conduct initial certification analysis in preparation for Phase 3 certification and accreditation. |
| 3 — Validation | Continue refining SSAA, conduct certification evaluation of IS, provide resulting recommendation to DAA, and obtain certification and accreditation decision and results. |
| 4 — Post Accreditation | Operate and maintain system in accordance with SSAA, maintain SSAA, perform periodic compliance validation, and implement change management. |

### Roles of NIACAP

To perform a security assessment and conduct the four phases of NIACAP, specific personnel roles are required. These roles and their duties are summarized in [Table 25-8](ch25.html#niacap_roles_and_functions).

The U.S. Department of Defense (DoD) requires certification and accreditation of its information systems and uses a process very similar to NIACAP. The DoD Information Technology Security Certification and Accreditation Process is discussed in the next section.

## DITSCAP

DoD Directive 5200.40, "DoD Information Technology Security Certification and Accreditation Process (DITSCAP)," defines the DITSCAP as the standard certification and accreditation process for the Department of Defense. This process assesses the impact of the IS operation on the Defense Information Infrastructure (DII) by evaluating the system architecture and mission.

**Table 25.8. NIACAP Roles and Functions**

| Role | Function |
| --- | --- |
| Program Manager | Responsible for ensuring that an acceptable level of risk is achieved based on integration of the appropriate security requirements; responsible for the IS throughout of the system life cycle, including system performance, cost, and on-time performance. |
| Designated Approving (Accrediting) Authority (DAA), or Accreditor | Responsible for implementing security for the IS; determines the acceptable level of risk and oversees IS budget and operations as the government representative. The DAA can grant accreditation or interim approval to operate until all security safeguards are in place and functioning. |
| Certification Agent | Conducts certification based on having appropriate technical or Certifier expertise; determines acceptable levels of risk and makes accreditation recommendation to DAA. |
| User Representative | Identifies user requirements, responsible for proper and secure operation of IS: represents user interests throughout life cycle of IS. |

DITSCAP is applicable to the following entities:

- Military departments
- Chairman of the Joint Chiefs of Staff
- Combatant commands
- Inspector General of the Department of Defense
- Office of the Secretary of Defense (OSD)
- Defense agencies
- DoD field activities
- DoD contractors and agents
- DoD organizations involved with the acquisition, operation, and sustaining of any DoD system that collects, stores, transmits, or processes unclassified or classified information

### The four phases of DITSCAP

The DITSCAP is composed of the same four phases as NIACAP: definition, verification, validation, and postaccreditation. The activities in these phases are essentially identical to those of the NIACAP.

### Roles of DITSCAP

The roles of personnel involved in the DITSCAP are similar, but not identical to those of the NIACAP. The DITSCAP personnel roles and their functions are given in [Table 25-9](ch25.html#ditscap_roles_and_functions).

**Table 25.9. DITSCAP Roles and Functions**

| Role | Function |
| --- | --- |
| System Program | Responsible for budget and engineering of a system; represents the Manager of the maintenance or acquisition unit for the system; responsible for system performance. |
| Designated Approving (Accrediting) Authority | Responsible for oversight of mission needs and system operations; determines system security needs; usually is the (DAA), or Accreditor's senior operations officer. The DAA can grant accreditation or interim approval to operate until all security safeguards are in place and functioning. |
| Certification Agent | Conducts certification based on having appropriate technical or Certifier expertise; determines acceptable levels of risks, and makes accreditation recommendation to DAA. |
| User Representative | Identifies user requirements, responsible for proper and secure operation of IS: represents user interests throughout life cycle of IS. |

# DIACAP

The DoD Information Assurance Certification and Accreditation Process (DIACAP) is the latest certification and accreditation vehicle for all DoD systems. It replaced DITSCAP in 2007; its objective is to bring a net-centric approach to risk management. DoD Information Systems would be scored against their baselines, risks would be documented, and accreditation statuses would be visible to the U.S. Congress level. Under DIACAP, the security baselines are standardized across all DoD systems via the implementation of DoDI 8500.2 IA Controls.

### The five phases of DIACAP

Much like DITSCAP, DIACAP follows a phased approach to certifying and accrediting DoD Information Systems.

| DIACAP | DITSCAP |
| --- | --- |
| Initiate and plan IA C&A | Definition |
| Implement and validate IA controls | Verification |
| Make certification determination and accreditation decision | Validation |
| Maintain authorization to operate and conduct reviews | Post-accreditation |
| Decommission |  |

The goal of this transition was to build information assurance into the system, rather than retrofitting during the verification and validation phases.

One difference from DITSCAP is in the intent of the C&A documentation. DITSCAP followed a "one document" approach, with numerous appendices to cover all aspects of security. This System Security Authorization Agreement (SSAA) would often have to be updated and reissued as a whole during the post-accreditation phase. In practice, this approach did not allow the flexibility needed to manage evolving threats and risks.

The DIACAP Comprehensive Package allowed for the security documentation to be modular. This flexibility allowed pieces and parts to be updated during the life cycle.

The comprehensive package consists of:

- **System Information Profile (SIP)**—A compilation of the information system characteristics, such as system identification, system owner, and system description, and any information that would be required to register with the DoD component.
- **DIACAP Implementation Plan (DIP)**—A list of those IA controls that are assigned to the information system during the Initiate and Plan phase. The plan includes the implementation status, responsible entities, resources, and estimated completion dates for those controls not in compliance.
- **DIACAP scorecard**—A summary report that shows overall compliance status as well as accreditation status of the information system.
- **IT Security Plan of Action and Milestones (POA&M)**—A record that identifies the tasks to be accomplished in order to resolve security weaknesses or vulnerabilities. Documents specific corrective actions, mitigations, and resources required to resolve the issue. Also used to document non-compliant IA controls, as well as those IA controls that are not applicable.
- **Supporting certification documentation**—Artifacts, validation results, processes, and procedures such as, but not limited to, disaster recovery plans, incident response plans, vulnerability management procedures, and any other documentation in support of IA control compliance.

So while the SIP or some supporting documentation would likely not change over the DIACAP life cycle, items such as the DIP, Scorecard, and POAM would be updated frequently to reflect the security posture of the information system. This allows only those modules of the overall package that change to be updated, with the intent to reduce documentation management, and to place an increased focus on risk management.

This comprehensive package is then presented to the Certifying Authority (CA), where a determination is made as to the information system's compliance with assigned IA controls, the overall residual risk of operating the system, and the costs to correct or mitigate the vulnerabilities as documented in the POA&M. Once this determination is made, the Designated Accrediting Authority (DAA) then formally assumes responsibility for operating the system at the predefined level of risk.

Another differentiator between the DITSCAP and DIACAP process is the inclusion and execution of the DoDI 8500.2 IA controls. As mentioned previously, these controls are tightly integrated into the DIACAP life cycle. These security requirements are selected dependent on the confidentiality of the system (Public, Sensitive, Classified) as well as the mission assurance category (MAC I/II/III). MAC represents the importance of data relative to meeting a system's objectives, and concerns the system's availability and integrity.

MAC I handles information that is vital to operational readiness or mission effectiveness, such as command and control. MAC II handles information that supports deployed forces, such as situational awareness systems. MAC III systems handles information necessary for day-to-day business, such as NIPRNET.

There are nine possible combinations of MAC/Confidentiality levels out of a total of 157 controls. MAC and confidentiality levels are independent of each other, as it is possible to have a classified system that handles only e-mail and other business support functions, or to have a MAC I system that processes public information that may be vital for defense.

The decision to accredit a system falls into one of the following areas: ATO—Authority to Operate (no provisions); IATO—Interim ATO (provisions set forth in POA&M required); IATT—Interim Authority To Test (inside given timeline only); and DATO—Denial of ATO (Reassess Implementation Plan.)

### DIACAP challenges

The goal of DIACAP is to bring standardization to the C&A process for the DoD. With the IA controls acting as the common baseline, this "one size fits all" rarely fits unique systems, such as command and control systems and weapons systems. Tailoring of the DIACAP and the IA controls is necessary to accurately reflect the security posture and risk to the information system. A vital part of the supporting documentation is a risk management process. This process details how system architecture is connected to NIPRNet, SIPRNet, etc., and how technical, physical and administrative controls mitigate those high risk IA controls to less risky ones.

For those systems under tight configuration control (for example, missile warning, missile defense, and weapons systems) certain IA controls are not possible, such as requiring constantly updating security baselines (IAVA). Others, such as requiring desktop screen locks, may interfere with mission functionality. The DIACAP must be tailored to fit the specific and evolving needs of the information system.

## Comparison and inclusion of other vehicles

As part of an ongoing effort to standardize certification and accreditation vehicles across the DoD as well as intelligence and other federal agencies, NIST has been tasked to develop a unified C&A process that all sectors will follow and accept. The NIST Special Publication 800-37 Rev 1 "Guide for Security Authorization of Federal Information Systems: A Security Life Cycle Approach" is in draft, but states:

> *The Director of National Intelligence, the Secretary of Defense, and the Chairman of the Committee on National Security Systems have agreed to follow these guidelines with augmentation and tailoring as needed to meet their organizational requirements*.

This guidance aims to bring to the forefront the concept of "near real-time risk management," adding a "risk executive" to the C&A team. The other accreditation vehicles, such as DCIC 6/3 and NIACAP, would still exist but would reference and follow the NIST 800-37 series of IA controls, tailored to meet the specific requirements of particular programs. NIST would add another level of robustness to the validation of IA controls. In the 8500.2 series, IA controls are statements of requirements such as "A disaster plan exists ..." or "An incident response plan exists ..." In the case of NIST, the requirement NIST IR-1 will not only require that an IRP exist, but also that it comply with NIST SP 800-12/61/83. SP 800-61 itself is 148 pages.

As new risks appear, the current C&A vehicles will continue to become more specific and robust in order to meet the challenges of risk management. With the transition from DITSCAP to DIACAP, a trend will continue for more verification, validation, and risk management of DoD information systems.

# Federal Information Processing Standard 102

Federal Information Processing Standard (FIPS) 102, from September 27, 1983, addresses setting up and conducting certification and accreditation activities. Its formal title is "The Guideline for Computer Security Certification and Accreditation." (The guideline was withdrawn by NIST on Feb. 8, 2005, but still is of historical interest.)

The guideline defines the following policies and procedures for certification and accreditation:

- A Senior Executive Officer should establish authority for the certification and accreditation program and allocate responsibilities.
- The Certification Program Manager should issue a program manual that includes the processes involved and covers the Program Manager's responsibilities.

FIPS 102 defines the certification and accreditation roles as follows:

- A Senior Executive Officer that allocates responsibilities and issues the program directive
- A Certification Program Manager that initiates the certification of an application, approves the Application Certification Plan, develops and issues the Program Manual, assigns an Application Certification Manager, and maintains certification and accreditation records.
- An Application Certification Manager that develops the Application Certification Plan, manages the security assessment, and produces the evaluation report
- A Security Evaluator that performs the security assessment required for the certification

FIPS 102 defines the following steps in conducting a certification and accreditation:

1. Planning
2. Data Collection
3. Basic Evaluation
4. Detailed Evaluation
5. Report of Findings
6. Accreditation

# OMB Circular A-130

The U.S. government Office of Management and Budget (OMB) issued Circular A-130 to establish policies for managing government information systems. It applies to all IT-related entities of the executive branch of the U.S. government.

Circular A-130 was developed in accordance with the following acts:

- The Paperwork Reduction Act (PRA), as amended (44 U.S.C. Chapter 35)
- The Privacy Act, as amended (5 U.S.C. 552a)
- The Chief Financial Officers Act (31 U.S.C. 3512 et seq.)
- The Federal Property and Administrative Services Act, as amended (40 U.S.C. 759 and 487)
- The Computer Security Act (40 U.S.C. 759 note)
- The Budget and Accounting Act, as amended (31 U.S.C. [Chapter 11](ch11.html))
- Executive Order No. 12046 of March 27, 1978
- Executive Order No. 12472 of April 3, 1984

In particular, the Paperwork Reduction Act requires that the Director of OMB perform the following functions:

- Oversee the development and use of information management principles, standards, and guidelines.
- Develop and implement uniform and consistent information resources management policies.
- Evaluate agency information resources management practices to determine their adequacy and efficiency.
- Determine compliance of such practices with the policies, principles, standards, and guidelines promulgated by the Director of OMB.

Relative to certification and accreditation, Appendix III of the Circular requires "accreditation for an information system to operate based on an assessment of management, operational, and technical controls. The security plan documents the security controls that are in place and are planned for future implementation." Specifically, Section 8a(9), "Information Safeguards," of Appendix III, directs that agencies protect government information in accordance with risk management and risk assessment techniques.

Appendix III also mandates a number of actions to be taken by government agencies regarding information security, including the following:

- Plan in an integrated manner for managing information throughout its life cycle.
- Integrate planning for information systems with plans for resource allocation and use, including budgeting, acquisition, and use of information technology.
- Train personnel in skills appropriate to management of information.
- Protect government information commensurate with the risk and magnitude of harm that could result from the loss, misuse, or unauthorized access to or modification of such information.
- Use voluntary standards and Federal Information Processing Standards where appropriate or required.
- Consider the effects of the actions of the IT-related entities of the executive branch of the U.S. government on the privacy rights of individuals, and ensure that appropriate legal and technical safeguards are implemented.

# The National Institute of Standards and Technology Assessment Guidelines

The National Institute of Standards and Technology (NIST) is a rich source of information and guidelines for assessing the assurance of information systems. This information is provided in the form of NIST Special Publications (SP) and is available at the NIST Web site (`www.nist.gov`). [Table 25-10](ch25.html#some_nist_information_assurance_special) provides a listing of some of the more popular information assurance SPs.

**Table 25.10. Some NIST Information Assurance Special Publications**

| SP | Title |
| --- | --- |
| 800-14 | Generally Accepted Principles and Practices for Securing Information Technology Systems |
| 800-27 | Engineering Principles for Information Technology Security (A Baseline for Achieving Security) |
| 800-30 | Risk Management Guide for Information Technology Systems |
| 800-64 | Assess Threat Security Considerations in the Information System Development Life Cycle |

## SP 800-14

NIST Special Publication 800-14 identifies 8 system security principles and 14 common IT security practices. The principles are based on the Organization for Economic Cooperation and Development (OECD) information system security guidelines. The system security principles of SP 800-14 are as follows:

- Computer security supports the mission of the organization.
- Computer security is an integral element of sound management.
- Computer security should be cost-effective.
- Systems owners have security responsibilities outside their own organizations.
- Computer security responsibilities and accountability should be made explicit.
- Computer security requires a comprehensive and integrated approach.
- Computer security should be periodically reassessed.
- Computer security is constrained by societal factors.

[Table 25-11](ch25.html#nist_sp_800-14_common_security_practices) lists the 14 common SP 800-14 security practices.

## SP 800-27

This publication incorporates the principles and practices of SP 800-14 into 33 system-level engineering principles for information technology security (EP-ITS). SP 800-27 also maps these system-level principles into the five system life-cycle phases of initiation, development and acquisition, implementation, operation and maintenance, and disposal.

## SP 800-30

SP 800-30, the "Risk Management Guide for Information Technology Systems," is compatible with Appendix III of OMB Circular A-130 and provides non-mandatory guidelines for reducing information system risk to an acceptable level. According to SP 800-30, "This guide provides a foundation for the development of an effective risk management program, containing both the definitions and the practical guidance necessary for assessing and mitigating risks identified within IT systems."

**Table 25.11. NIST SP 800-14 Common Security Practices**

| Practice | Activities |
| --- | --- |
| 1. Policy | Establish plans, procedures, and directives. |
| 2. Program Management | Centralized oversight and enforcement of computer security. |
| 3. Risk Management | Assess risk, reduce risk, and maintain acceptable risk level. |
| 4. Life Cycle Planning | Develop security plan, and maintain plan through system life cycle. |
| 5. Personnel/User Issues | Access control for users, managers, and implementers. |
| 6. Preparing for Contingencies and Disasters | Planning to ensure continuity of business operations after a disaster. |
| 7. Computer Security and Incident Handling | Respond effectively to malicious code and intrusions. |
| 8. Awareness and Training | Coordinate security. |
| 9. Security Considerations in Computer Support and Operations | Applying information system security principles to job functions of system administrators and external system support operations |
| 10. Physical and Environmental Security | Implementing physical and environmental controls. |
| 11. Identification and Authentication | Applying identification and authentication to assign access privileges to information system resources. |
| 12. Logical Access Control | Using technical mechanisms to limit access to information systems and to enforce the system security policy. |
| 13. Audit Trails | Logging system activity and enabling accountability, intrusion detection, and problem identification. |
| 14. Cryptography | Providing cryptographic protections for the confidentiality and integrity of information as well as electronic signatures. |

Risk management is necessary for an organization to accomplish its mission by securing and managing its IT resources effectively. Risk management also supports the certification and accreditation of information systems.

Key personnel that have roles in risk management include the following:

- Senior management
- Chief information officer (CIO)
- System and information owners
- Business and functional managers
- Information system security officer (ISSO)
- IT security practitioners
- Security awareness trainers

NIST SP 800-30 defines risk as "a function of the likelihood of a given threat-source's exercising a particular potential vulnerability, and the resulting impact of that adverse event on the organization."

SP 800-30 defines risk management as having the following three components:

- Risk assessment
- Risk mitigation
- Risk evaluation and assessment

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

### Risk mitigation

Risk mitigation prioritizes the recommended controls that result from the risk assessment activity. Controls are subject to cost-benefit analyses and are used to limit the risk to an acceptable level that enables accomplishment of the organization's mission. To mitigate risk, technical, management, and operating controls can be applied.

The following options are available for risk mitigation:

- Risk avoidance
- Risk assumption
- Risk limitation
- Risk transference
- Risk planning
- Research and development

### Evaluation and assessment

Because an organization usually experiences changes in personnel, network architecture, and information systems, risk management is a continuous process that requires ongoing evaluation and assessment. OMB Circular A-130 mandates that risk assessments be conducted every three years for U.S. government agencies. However, risk assessment should be conducted as necessary, such as after major alterations to networks or computers.

### Residual risk

Even after controls are in place as a result of the risk management process, some risk, *residual risk*, always remains. It is the DAA's responsibility to take into account the residual risk in the certification and accreditation process.

## SP 800-64

NIST SP 800-64, "Security Considerations in the Information System Development Life Cycle" (SDLC), is a guideline for incorporating information systems security in the phases of the SDLC. Examples of security functions for each of the five phases of the SDLC are given in [Table 25-12](ch25.html#examples_of_information_systems_security).

**Table 25.12. Examples of Information Systems Security in the SDLC**

| Initiation | Acquisition/Development | Implementation | Operations/Maintenance | Disposition |
| --- | --- | --- | --- | --- |
| Preliminary Risk AssessmentSecurity Categorization | Risk AssessmentSecurity, Functional, and Assurance Requirements AnalysisCost Considerations and ReportingSecurity Control Development | Inspection and AcceptanceSecurity Control IntegrationSecurity CertificationSecurity Accreditation | Configuration Management and ControlContinuous Monitoring | Information PreservationMedia SanitizationHardware and Software Disposal |

NIST SP 800-64 provides guidelines for acquisition, which is involved with identifying a need for a product or services, acquiring the product or services, and completing the contract for the product or services. In the acquisition process, requests for proposal (RFPs) are published to solicit bids for a product or service. An *acquisition initiator* represents the relevant program office in compiling the IT-related requirements and preparing for issuance of the RFP. After proposals in response to the RFP are received, an acquisition technical evaluation is conducted to review the technical merit of the proposals.

# Penetration Testing

A *penetration test* is designed to evaluate an information system's defense and discover weaknesses in the network and its resources. Penetration testing is sometimes called *ethical hacking* because, in some instances, the entity conducting the penetration test is employing techniques used by crackers. The difference is the ethical hacker is acquiring information about the network to improve its security as opposed to causing harm. A penetration test can determine how a system reacts to an attack, whether or not a system's defenses can be breached, and what information can be acquired from the system.

[Table 25-13](ch25.html#penetration_testing_phases) summarizes the different phases involved with conducting a penetration test.

**Table 25.13. Penetration Testing Phases**

| Phase | Activities |
| --- | --- |
| 1. Discovery | Acquire and evaluate information relevant to the organization and systems to be tested. |
| 2. Enumeration | Acquire IDs, versions of software installed, and information concerning the network to be tested. |
| 3. Vulnerability mapping | Characterize the information system environment and identify its vulnerabilities. |
| 4. Exploitation | Try to exploit the system vulnerabilities and gain access privileges to the target system. Care is taken not to cause harm to the system or its information. |
| 5. Report generation | Produce an executive overview report for management that profiles the network security posture and results of remediation activities, and generate an IT technical report for IT staff that details threats to the network, corresponding vulnerabilities discovered during testing, and remediation recommendations. |

Penetration tests can be classified in a number of ways. The most common categories of penetration tests are as follows:

- Internal
- External
- Null knowledge
- Partial knowledge
- Zero knowledge
- Closed box
- Open box

## Internal penetration test

This type of penetration test tries to complete the following activities while operating from inside the network perimeter:

- Obtaining unauthorized connection and access to the network
- Determining the network architecture
- Identifying the OS
- Identifying OS vulnerabilities
- Obtaining protected information from the network and its associated resources
- Evaluating response of any installed intrusion detection systems
- Determining if there are any unauthorized items connected to the network

## External penetration test

An external penetration test attempts to obtain network information while operating outside of the network perimeter. The following types of actions are performed during this type of test:

- Determining the network OS
- Determining OS vulnerabilities
- Obtaining unauthorized entry to the internal network
- Gathering information about the internal network
- Obtaining information stored on internal network resources
- Testing the external intrusion detection system (IDS)
- Testing the firewall

## Full knowledge test (white-box test)

The full knowledge test assumes an attacker has extensive knowledge about the network and its operation, increasing the opportunity for a successful penetration of the network.

## Partial knowledge test (gray-box test)

This test assumes that the penetration testing team has knowledge of some specific vulnerabilities in the network. Thus, the penetration test would include attacks aimed at those vulnerabilities.

## Zero knowledge test (black-box test)

As the name implies, the penetration test begins with no *a priori* knowledge of the network and its resources. Thus, information has to be gathered from any available sources to use in the testing process.

## Closed-box test

The closed-box test assumes the testing personnel have no access to the internal IT system code.

## Open-box test

For this test type, the testing team does have access to internal system code, such as code from open-source operating systems such as Linux.

# Auditing and Monitoring

Auditing and monitoring procedures for networks are used to ensure that security controls are operating and providing effective protection for the information systems. An *audit* is a one-time or periodic event to evaluate security whereas *monitoring* refers to an ongoing activity that examines either the system or the users.

## Auditing

Auditing is conducted by either a group internal to an organization or by third-party auditors. Third-party auditors are usually certified professionals such as CPAs or, in the information security field, Certified Information Assurance Auditors (CISAs). Internal auditors normally evaluate due-care practices and compliance with standards, and recommend improvements in safeguards and controls.

### Standards

The Information Systems Audit and Control Association (ISACA, at `www.isaca.org`) has developed standards and guidelines for auditing IT systems. The following are examples of some of the standard practices:

- The audit function is sufficiently independent of the area being audited to permit objective completion of the audit.
- The information systems auditor must adhere to the Code of Professional Ethics of the ISACA.
- The information systems auditor must maintain technical competence through the appropriate continuing professional education.
- During the course of the audit, the information systems auditor obtains sufficient, reliable, relevant, and useful evidence to achieve the audit objectives effectively.
- The information systems auditor provides a report, in an appropriate form, to the intended recipients upon the completion of the audit work.

### The audit process

A successful information systems audit comprises the following steps:

1. Plan the audit.
2. Determine the scope of the audit.
3. Determine the objectives of the audit.
4. Validate the audit objectives and plan with the stakeholders.
5. Plan for necessary resources.
6. Perform the planned tasks.
7. Document the audit procedures and results.
8. Validate the audit results.
9. Report audit results to stakeholders.
10. Obtain stakeholders' final approval.

*Audit trails* are logs of events that provide a history of occurrences in the IT system. They document these events and are used for tracing sources of intrusions, recording results of intrusions, and, in general, summarizing the history of activities that took place on a system. Audit trails enable the enforcement of individual accountability by reconstructing events.

Audit information comprises a history of transactions, including who processed the transaction, the date and time of the transition, where the transaction occurred, and related activities. An audit associated with information system security searches for the following:

- Internal and external attempts to gain unauthorized access to a system
- Patterns and history of accesses
- Unauthorized privileges granted to users
- Occurrences of intrusions and their resulting consequences

In addition, auditors evaluate contingency plans, development standards, transaction controls, and data library procedures.

Because of their importance, audit logs should be protected at the highest level of security in the information system.

## Monitoring

Monitoring is an active, sometimes real-time, process that identifies and reports security events that might be harmful to the network and its components. Examples of such events or situations include unauthorized network devices, unauthorized personal servers, and unprotected sharing of equipment. Examples of items monitored include LAN and Internet traffic, LAN protocols, inventories of network devices, and OS security functions.

Intrusion detection mechanisms, penetration testing, and violation processing are used to accomplish monitoring.

Intrusion detection (ID) is discussed in detail in [Chapter 17](ch17.html) and is applied to detect and analyze intrusion attempts. By using threshold or *clipping levels*, below which activities are deemed benign, the amount of information that has to be analyzed can be reduced significantly.

Penetration testing, discussed in a previous section of this chapter, probes and tests a network's defenses to determine the state of an organization's information security. Penetration testing can employ scanners, war dialers, protocol analyzers, and social engineering to determine the security posture of that organization.

Violation analysis uses clipping levels to detect potentially harmful events. For example, clipping levels can detect excessive numbers of personnel with unrestricted access to the system, personnel exceeding their authorization privileges, and repetitive mistakes.

Monitoring responsibility in an organization usually falls under the CIO or equivalent officer.

# Summary

Ensuring that network security controls are cost-effective and provide the required level of protection is the function of assurance evaluation mechanisms. Process models, such as the SSE-CMM and IAM, can evaluate assurance while the DITSCAP, NIACAP and DIACAP effectively certify and accredit information systems for operation.

The NIST SPs provide valuable guidelines for self-assessment and risk management and are complemented by auditing, monitoring, and penetration testing techniques.
