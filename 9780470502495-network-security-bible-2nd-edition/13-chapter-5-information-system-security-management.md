# Chapter 5. Information System Security Management

**IN THIS CHAPTER**

- **Understanding security policies, standards, guidelines, and procedures**
- **Conducting security awareness training**
- **Managing the technical effort**
- **Developing business continuity and disaster recovery plans**
- **Implementing physical security**
- **Understanding legal and liability issues**

Information system security management comprises a variety of techniques that can significantly reduce the risk of compromise to confidentiality, integrity, and availability of information systems. Management tools and techniques, although not as glamorous as high-tech approaches, can be highly effective in implementing and maintaining information system security at a reasonable cost. Such tools include security policies, vacation scheduling, employee background checks, awareness training, and contingency planning. These controls focus on the "people" problem within an organization. When it comes to security, people (employees and contractors) are your greatest asset and your greatest liability.

One of the biggest people-problem threats is social engineering or human manipulation. Just as social engineering can easily help you acquire information that would require large expenditures of time and resources to obtain by technical means, information security management practices can produce significant reductions in risk at reasonable cost.

This chapter describes the tools and techniques of information system security management, including administrative procedures, recovery methods, backup of critical data, physical security, and legal or liability issues.

# Security Policies

A security policy (referred to in the following text just as a policy) is a document that states what is or is not acceptable behavior within an organization. Such a policy deals directly with the people problem.

Remembering that security is all about managing, controlling, and mitigating risk to your critical assets, you'll realize that each statement in a policy should map back to a risk. To be more specific, each statement in a policy should refer back to a personnel risk that you're trying to reduce.

It's important to remember that a key requirement of a policy is that it be something everyone can read and understand. Therefore, a policy should be no more than 15 pages and written in a common language that employees can comprehend.

High-level policies are general statements of management's intent. Policies are mandatory; however, if a policy is not properly enforced, some policies within an organization are going to be either strong recommendations or informative resources. Ideally, every statement in a policy should be a mandatory requirement that is uniformly enforced; anything not mandatory should be in a guideline. To help with enforceability it's important to make this distinction so there is no confusion among employees about what has to be followed and what is merely a recommendation.

A policy should be applied throughout the organization in a consistent manner and provide a reference for employees in the conduct of their everyday activities. A well-thought-out and well-written policy also provides liability protection for an organization and its senior management. In order for a policy to be enforceable it must be clear, consistent, and uniformly enforced for everyone. Some of the big problems that organizations have with policies are:

- **Policy is unenforceable and vague**. If a statement is not enforceable it should not be in the policy. Policy statements should be clear and concise, with the ability to measure whether someone is compliant or not. For example, a speed limit sign is an example of an enforceable policy. It is clear, concise, and easy to read, and because it is an exact number it is easy for law enforcement to measure.
- **Policy is not consistently enforced**. In many cases, employees sign or agree to the policy in its entirety. Therefore, if there is one statement in that policy that is not enforced, in many cases this makes the entire policy null and void. Therefore, it's important to remember that any statement in the policy must be something the organization intends to enforce. If not, it should be moved to the guidelines.
- **Policy is interpreted differently**. The policy needs to be written so that there is a single interpretation of the policy. If a policy can be interpreted in different ways, it's difficult to enforce.

## Senior Management Policy Statement

The senior management policy statement sets the tone and guidance for the standards, guidelines, baselines, and procedures to be followed by the organization. For a security policy, this statement declares the importance of securing the networks and computing resources of the organization, management's commitment to information system security, and authorization for the development of standards, procedures, and guidelines. This senior management policy statement might also indicate individuals or roles in the organization that have responsibilities for policy tasks.

Specific instantiations of senior management policy statements are *advisory*, *regulatory*, and *informative* policies. The National Institute of Standards and Technology (NIST) defines additional polices for use by U.S. government agencies. These polices are program-specific, system-specific, and issue-specific.

### Advisory Policies

Even though policies are usually considered mandatory, *advisory* security policies are strong recommendations. These policies recommend courses of action or approaches but allow for independent judgment in the event of special cases. The advisory policy can provide guidance as to its application and indicate circumstances where it might not be applicable, such as during an emergency.

### Regulatory Policies

*Regulatory* policies are intended to ensure that an organization implements the standard procedures and best practices of its industry. These policies apply to institutions such as banks, insurance companies, investment companies, public utilities, and so on.

### Informative Policies

*Informative* policies provide information and, generally, require no action by the affected individuals. An informative policy, however, might prohibit and specify penalties for certain activities, such as downloading objectionable material on an organization's computer. The policy would, therefore, inform the user of the prohibited activities and resultant consequences of practicing those activities.

### U.S. Government Policy Types

The NIST provides guidance in the area of information system and network security policies for government agencies. NIST Special Publication 800-12, "An Introduction to Computer Security," divides computer system security policies into three categories:

- **Program policies** are strategic statements addressing an organization's computer and network security program.
- **System-specific policies** are concerned with the technical aspects of a particular computer, network, or device type.
- **Issue-specific policies** focus on specific situations on a non-technical, strategic basis. An example of an issue-specific policy would be directives concerning unlicensed use of software packages.

## Standards, Guidelines, Procedures, and Baselines

Policies are at the top of the hierarchy of policies, standards, guidelines, baselines, and procedures, as shown in [Figure 5-1](ch05.html#hierarchy_of_policies_comma_standards_co).

![Hierarchy of policies, standards, baselines, guidelines, and procedures](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0501.png)

**Figure 5.1. Hierarchy of policies, standards, baselines, guidelines, and procedures**

Policies and procedures go hand in hand. A policy specifies what to do and a procedure specifies how to do it. A policy statement might be one line while a procedure might be several pages long. For example, a policy statement might say, "Passwords must be changed every 60 days." The procedure would explain in detail how passwords need to be changed for every system the organization has.

Standards and baselines also go together. Standards are high level (similar to policy) and baselines are the details (similar to procedures). Standards specify the high-level hardware and software an organization will use, and baselines specify the details of how that hardware/software is configured. For example, the standard might say all computers must use Windows Vista, and the baselines would specify how to configure the operating system in a particular environment.

Guidelines provide recommendations on how to effectively utilize the policy, procedure, standard, and guideline documents, but it is important to remember that a guideline is not a mandatory document.

The following is an example of how all the pieces fit together:

- **Policy**— All servers must be properly hardened.
- **Standard**— Administrators must use Windows 2008 as the base operating system.
- **Baseline**— The specific settings for Windows 2008 should match those in the CIS security template.
- **Procedures**— The template should be applied when a system is built.
- **Guidelines**— To ease the application of templates, local GPOs can be used to roll out the changes.

In summary: standards, guidelines, procedures, and baselines flow from the high-level policy statements and help to implement the high level policy.

- **Standards** are compulsory and usually refer to specific hardware and/or software. For example, an organization might specify a standard operating system or standard platform that must be used by all its employees. By employing standards, an organization can implement security controls effectively for the enterprise.
- **Guidelines** are suggestions to the personnel of an organization on how to effectively secure their networks and computers. Guidelines provide flexibility and allow users to implement security controls in more than one way. They also can be used to ensure that important security measures are not overlooked.
- **Procedures** are compulsory, detailed steps to be followed in order to accomplish specific tasks. The step-by-step activities described in a procedure serve to implement the higher-level policy statement, standards, and guidelines. Examples of procedures are those used in preparing new user accounts or assigning privileges.
- **Baselines** are similar to standards and represent a level of implementation of security controls that provides protection that is equivalent to the protection available to other similar reference entities. The baseline of controls should be applied consistently across an organization, and provides the basis for development of the computer and network security architectures. The baseline level of protection is compulsory and can be used to develop the required organizational information system security standards.

# Security Awareness

In terms of validating and making people aware of the policy, three core pieces go together:

- **Policy**—Specifies what to do
- **Training**—Provides the skill for performing it
- **Awareness**—Changes behavior so everyone understands the importance of the policy

Senior management has the obligation to ensure that the employees of an organization are aware of their responsibilities in protecting that organization's computers and networks from compromise. Similarly, employees should be diligent in their everyday work habits and embrace good information system security practices. *Security awareness* refers to the collective consciousness of an organization's employees relative to security controls and the application of these controls to the protection of the organization's critical and sensitive information.

Employees' security awareness can have a significant impact on detecting fraud, reducing unauthorized computer- and network-related activities, and preventing security compromises in general.

Demonstrating that there are consequences for violating an organization's security policy can emphasize the importance of security awareness and good information system security practices. Employees found in violation of the security policy should be issued a warning, be reprimanded, or, in extreme cases, be fired for compromising the organization's computer and network security. Security awareness can also be reinforced through bulletins, newsletters, incentives, recognition, and reminders in the form of log-on banners, lectures, and videos.

## Training

Training is a tool that can increase employees' security awareness and capabilities in identifying, reporting, and handling compromises of confidentiality, integrity, and availability of information systems. Some typical types of security training and target audiences are given in [Table 5-1](ch05.html#types_of_information_security_training).

**Table 5.1. Types of Information Security Training**

| Training Type | Target Audience |
| --- | --- |
| Awareness | Personnel with security-sensitive positions |
| Security-related job training | Operators and other designated users |
| High-level security training | Senior managers, functional managers, and business unit managers |
| Technical security training | IT support personnel and system administrators |
| Advanced information security training | Security practitioners and information systems auditors |
| Specific security software and administrators, security practitioners, and selected users | Operators, IT support personnel, system hardware product training |

## Measuring Awareness

Information security awareness should be an institutionalized characteristic of an organization and practiced as part of employees' everyday activities. The level of practiced security awareness should be sampled at reasonable intervals to obtain assurance that related training and reminders are effective. Questionnaires, interactive meetings, and hypothetical problem exercises can be used to measure employees' security awareness. For example, one can obtain a fairly accurate picture of the level of security awareness in an organization by asking the following questions of a sampling of its personnel:

- Does your organization have an information security policy?
- Do you have a copy of that policy?
- Do you refer to that policy frequently?
- Do you know what security awareness means?
- How often does your organization conduct security awareness training and refresher sessions?
- Do you feel your security awareness training provides with the necessary knowledge and skills to handle information security incidents?
- Are you aware of what would be considered an information security incident?
- If you think an incident has occurred, what actions would you take?
- To whom would you report an incident?
- Do you feel comfortable in handling an information security incident?

# Managing the Technical Effort

Security engineering should be an integrated component of the overall development effort of a product or service. A successful security system engineering activity is the result of early and competent planning as well as effective management. A program management plan supports proper planning and also serves in the development of a systems engineering management plan that incorporates the system security engineering requirements. A key individual in carrying out these plans is the program manager. These elements are addressed in the following sections.

## Program Manager

A *program* is defined as a number of related projects that are managed as a whole by a program manager. A *program manager* must administer processes that are used to develop complex systems and is responsible for the system budget, schedule, and performance objectives. These systems are the result of the integration of systems engineering, systems security engineering, risk management, advanced planning, and effective management techniques.

The program management plan and the systems engineering management plan are tools used by the program manager to control the variables associated with a program and ensure delivery of a quality product.

One of the organizations that has developed and refined program management techniques is the U.S. Department of Defense (DoD). By its very nature, the DoD has to acquire, manage, and maintain complex systems ranging from healthcare records to missile systems. Thus, the DoD approach provides a good example of effective program management principles and practices.

**Department of Defense (DoD) Regulation 5000.2-R Change 3, Mandatory Procedures for Major Defense Acquisition Programs (MDAPs) and Major Automated Information System (MAIS) Acquisition Programs**

In the U.S. Department of Defense, a program manager is responsible for controlling many critical factors, including performance, costs, schedules, personnel issues, and applicable regulations. For network security, the program manager is responsible for ensuring that the security requirements are integrated into the system architecture and the resulting risk is acceptable. According to DoD Regulation 5000.2-R, Change 3, March 15, 1996:

> *... every acquisition program shall establish an Acquisition Program Baseline (APB) to document the cost, schedule, and performance objectives and thresholds of that program beginning at program initiation.... The program manager, in coordination with the user, shall prepare the APB at program initiation ... at each subsequent major milestone decision, and following a program restructure or an unrecoverable program deviation.... The APB shall contain only the most important cost, schedule, and performance parameters. The most important parameters are those that, if the thresholds were not met, the Milestone Decision Authority (MDA) would require a reevaluation of alternative concepts or design approaches.... At each milestone review, the PM shall propose exit criteria appropriate to the next phase of the program.... Exit criteria are normally selected to track progress in important technical, schedule, or management risk areas. The exit criteria shall serve as gates that, when successfully passed or exited, demonstrate that the program is on track to achieve its final program goals and should be allowed to continue with additional activities within an acquisition phase or be considered for continuation into the next acquisition phase*.

## Program Management Plan

The *program management plan* is a high-level planning document for the program and is the basis for other subordinate-level documents. The PMP also includes the high-level system requirements. The systems engineering management plan and a test and evaluation master plan evolve from the program management plan.

## Systems Engineering Management Plan

The *systems engineering management plan* integrates all the lower-level planning documents and supports the requirements in the high-level system specifications. It is the highest-level technical plan that supports the integration of subordinate technical plans of various disciplines. It contains the following:

- Directions for development of an organizational team
- Design tasks for the system development effort
- Concurrent engineering methods
- References for conducting systems security engineering tasks
- Delineation of responsibilities

Some of the principal headings in a typical systems engineering management plan include the following:

- System Engineering ProcessOperational RequirementsTechnical Performance MeasuresSystem Level Functional AnalysisSystem Test and Evaluation
- Technical Program Planning and ControlStatement of WorkOrganizational InterfacesWork Breakdown StructureScheduling and Cost EstimationTechnical Performance Measurement
- Engineering IntegrationElectrical EngineeringMechanical EngineeringOther Engineering DisciplinesSecurity Engineering
- Configuration Management
- Data Management
- Risk Management
- Reference Documents

Key components of the systems engineering management plan (the statement of work, work breakdown structure, technical performance measurement, and the test and evaluation master plan) are discussed in detail in the following sections.

### Statement of Work

A *statement of work* is a detailed description of the tasks and deliverables required for a given project. It is derived from the general statement of work given in the program management plan. The statement of work includes the following:

- A listing and description of the tasks to be accomplished
- Items to be delivered and a proposed schedule of delivery
- Input requirements from other tasks
- Special requirements and conditions
- References to applicable specifications, standards, and procedures

### Work Breakdown Structure

The *work breakdown structure* (WBS) is a systematic organization of activities, tasks, and subtasks that must be performed to complete a project. It is a deliverable-oriented grouping of project components that organizes and defines the total scope of the project; work not in the WBS is outside the scope of the project.

The WBS is applicable across a variety of applications and disciplines. A good overview of the WBS is provided in the U.S. *Department of Defense Handbook*, "Work Breakdown Structure," MIL-HDBK-881, dated January 2, 1998. It formally defines the WBS as having the following characteristics:

- "A product-oriented family tree composed of hardware, software, services, data, and facilities. The family tree results from systems engineering efforts during the acquisition of a defense materiel item."
- "A WBS displays and defines the product, or products, to be developed and/or produced. It relates the elements of work to be accomplished to each other and to the end product."
- "A WBS can be expressed down to any level of interest. However, the top three levels are as far as any program or contract need go unless the items identified are high cost or high risk. Then, and only then, is it important to take the work breakdown structure to a lower level of definition."

The WBS generally includes three levels of activity:

- **Level 1**— Identifies the entire program scope of work to be produced and delivered. Level 1 may be used as the basis for the authorization of the program work.
- **Level 2**— Identifies the various projects, or categories of activity, that must be completed in response to program requirements. Program budgets are usually prepared at this level.
- **Level 3**— Identifies the activities, functions, major tasks, or components of the system that are directly subordinate to the Level 2 items. Program schedules are generally prepared at this level.

Appendix A of MIL-HDBK-881 provides an example of a WBS for an aircraft system, as shown in [Table 5-2](ch05.html#wbs_levels_for_an_aircraft_system).

**Table 5.2. WBS Levels for an Aircraft System**

| Level 1 | Level 2 | Level 3 |
| --- | --- | --- |
| **Aircraft System** |  |  |
|  | **Air Vehicle (AV)** |  |
|  |  | Airframe |
|  |  | Propulsion |
|  |  | AV Applications Software |
|  |  | AV System Software |
|  |  | Communications/Identification |
|  |  | Navigation/Guidance |
|  |  | Central Computer |
|  |  | Fire Control |
|  |  | Data Display and Controls |
|  |  | Survivability |
|  |  | Reconnaissance |
|  |  | Automatic Flight Control |
|  |  | Central Integrated Checkout |
|  |  | Antisubmarine Warfare |
|  |  | Armament |
|  |  | Weapons Delivery |
|  |  | Auxiliary Equipment |
|  | **Sys Engineering/Program Management** |  |
|  | **System Test and Evaluation** |  |
|  |  | Development Test and Evaluation |
|  |  | Operational Test and Evaluation |
|  |  | Mock-ups |
|  |  | Test and Evaluation Support |
|  |  | Test Facilities |
|  | **Training** |  |
|  |  | Equipment |
|  |  | Services |
|  |  | Facilities |
|  | **Data** |  |
|  |  | Technical Publications |
|  |  | Engineering Data |
|  |  | Management Data |
|  |  | Support Data |
|  |  | Data Depository |
|  | **Peculiar Support Equipment** |  |
|  |  | Test and Measurement Equipment |
|  |  | Support and Handling Equipment |
|  | **Common Support Equipment** |  |
|  |  | Test and Measurement Equipment |
|  |  | Support and Handling Equipment |
|  | **Operational/Site Activation** |  |
|  |  | System Assembly, Installation and Checkout On-site |
|  |  | Contractor Technical Support |
|  |  | Site Construction |
|  |  | Site/Ship/Vehicle Conversion |
|  | **Industrial Facilities** |  |
|  |  | Construction/Conversion/Expansion |
|  |  | Equipment Acquisition or Modernization |
|  |  | Maintenance (Industrial Facilities) |
|  | **Initial Spares and Repair Parts** |  |

In [Table 5-2](ch05.html#wbs_levels_for_an_aircraft_system), the highest level of the WBS, Level 1, is an Aircraft System. The next level in the hierarchy, Level 2, comprises subsystems or tasks associated with the Aircraft System, such as the Air Vehicle itself, system test and evaluation, and communications support equipment. Level 3 of the WBS is a breakdown of the Level 2 categories. For example, under the Air Vehicle, Level 3 components include the airframe, propulsion system, and fire control system.

### Technical Performance Measurement

Technical performance measurement (TPM) is another useful tool for managing complex programs. As with the WBS, the DoD has developed excellent references for TPM.

The old MIL-STD-499A (USAF), "Engineering Management," U.S. Department of Defense, dated May 1, 1974, and the Systems Engineering Fundamentals document, of January 2001, Supplementary Text (`www.dau.mil/pubs/gdbks/sys_eng_fund.asp`) prepared by the Defense Acquisition University Press, Fort Belvoir, Virginia provide excellent descriptions of TPM. The purposes of TPM are given as follows:

- Provide visibility of actual vs. planned performance
- Provide early detection or prediction of problems that require management attention
- Support assessment of the program impact of proposed change alternatives

MIL-STD-499A also states "TPM assesses the technical characteristics of the system and identifies problems through engineering analyses or tests which indicate performance being achieved for comparison with performance values allocated or specified in contractual documents."

A TPM integrates the existing cost, schedule and technical performance information that is generated by a program's prime contractors and other team members.

The Office of the Secretary of Defense (OSD) publication, "Technical Performance Measurement—Integrating Cost, Schedule and Technical Performance for State-of-the-Art Project Management," graphically depicts TPM, as shown in [Figure 5-2](ch05.html#technical_performance_measurement_flow_c).

### Test and Evaluation Master Plan

The *test and evaluation master plan* (TEMP) provides direction for the technical and management components of the testing effort. The activities involved in producing a TEMP are as follows:

- Develop a detailed test plan that provides for complete test coverage of the system under test.
- Communicate the nature and extent of the tests.
- Establish an orderly schedule of events.
- Specify organizational and equipment requirements.
- Define the testing methodology.
- Compose a deliverables list
- Determine the expected outputs.
- Provide instructions for the execution of the tests.
- Maintain a written record of the test inputs.
- Exercise system limits and abnormal inputs.

![Technical performance measurement flow chart](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0502.png)

**Figure 5.2. Technical performance measurement flow chart**

The testing and evaluation activities performed under the TEMP can be separated into different categories, depending on their functions and goals. A summary of these categories is given in [Table 5-3](ch05.html#categories_of_test_and_evaluation).

**Table 5.3. Categories of Test and Evaluation**

| Test and Evaluation Type | Function and Goal |
| --- | --- |
| Analytical | Evaluations of design conducted early in the system life cycle using computerized techniques such as CAD, CAM, CALS, simulation, rapid prototyping, and other related approaches. |
| Type 1 test | The evaluation of system components in the laboratory using bench test models and service test models, designed to verify performance and physical characteristics. |
| Type 2 test | Testing performed during the latter stages of the detailed design and development phase when preproduction prototype equipment and software are available. |
| Type 3 test | Tests conducted after initial system qualification and prior to the completion of the production or construction phase. This is the first time that all elements of the system are operated and evaluated on an integrated basis. |
| Type 4 test | Testing conducted during the system operational use and life-cycle support phase, intended to provide further knowledge of the system in the user environment. |

# Configuration Management

*Configuration management* is the process of tracking and approving changes to a system. It involves identifying, controlling, and auditing all changes made to the system. It can address hardware and software changes, networking changes, or any other change affecting security. Configuration management can also be used to protect a trusted system while it is being designed and developed.

The primary security goal of configuration management is to ensure that changes to the system do not unintentionally diminish security. For example, configuration management might prevent an older version of a system from being activated as the production system. Configuration management also makes it possible to accurately roll back to a previous version of a system in case a new system is found to be faulty. Another goal of configuration management is to ensure that system changes are reflected in current documentation to help mitigate the impact that a change might have on the security of other systems, while in either the production or planning stages.

Configuration management is a discipline applying technical and administrative direction to do the following:

- Identify and document the functional and physical characteristics of each configuration item for the system
- Manage all changes to these characteristics
- Record and report the status of change processing and implementation

Configuration management involves process monitoring, version control, information capture, quality control, bookkeeping, and an organizational framework to support these activities. The configuration being managed is the verification system plus all tools and documentation related to the configuration process. In applications development, change control involves the analysis and understanding of the existing code, and the design of changes and corresponding test procedures.

## Primary Functions of Configuration Management

The primary functions of configuration management or change control are as follows:

- To ensure that the change is implemented in an orderly manner through formalized testing
- To ensure that the user base is informed of the impending change
- To analyze the effect of the change on the system after implementation
- To reduce the negative impact that the change might have had on the computing services and resources

Five generally accepted procedures exist to implement and support the change control process:

1. Applying to introduce a change
2. Cataloging the intended change
3. Scheduling the change
4. Implementing the change
5. Reporting the change to the appropriate parties

## Definitions and Procedures

The five major components of configuration management and their functions are as follows:

- Configuration identification
- Configuration control
- Configuration status accounting
- Configuration auditing
- Documentation change control

These components are explained in the following sections.

### Configuration Identification

Configuration management entails decomposing the verification system into identifiable, understandable, manageable, trackable units known as *configuration items* (CIs). The decomposition process of a verification system into CIs is called *configuration identification*. A CI is a uniquely identifiable subset of the system that represents the smallest portion to be subject to independent configuration control procedures.

CIs can vary widely in size, type, and complexity. Although no hard-and-fast rules exist for decomposition, the granularity of CIs can have great practical importance. A favorable strategy is to designate relatively large CIs for elements that are not expected to change over the life of the system, and small CIs for elements likely to change more frequently.

### Configuration Control

*Configuration control* is a means of ensuring that system changes are approved before being implemented, that only the proposed and approved changes are implemented, and that the implementation is complete and accurate. This activity involves strict procedures for proposing, monitoring, and approving system changes and their implementation. Configuration control entails central direction of the change process by personnel who coordinate analytical tasks, approve system changes, review the implementation of changes, and supervise other tasks such as documentation.

All analytical and design tasks are conducted under the direction of a corporate entity called the *Configuration Control Board* (CCB). The CCB is headed by a chairperson who is responsible for ensuring that changes made do not jeopardize the soundness of the verification system and assures that the changes made are approved, tested, documented, and implemented correctly.

The members of the CCB should interact periodically, either through formal meetings or other available means, to discuss configuration management topics such as proposed changes, configuration status accounting reports, and other topics that may be of interest to the different areas of system development. These interactions should be held to keep the entire system team updated on all advancements to or alterations in the verification system.

### Configuration status accounting

*Configuration accounting* documents the status of configuration control activities and, in general, provides the information needed to manage a configuration effectively. It allows managers to trace system changes and establish the history of any developmental problems and associated fixes. Configuration accounting also tracks the status of current changes as they move through the configuration control process. Configuration accounting establishes the granularity of recorded information and thus shapes the accuracy and usefulness of the audit function. The configuration accounting reports are reviewed by the CCB.

### Configuration Auditing

*Configuration auditing* is the quality assurance component of configuration management. It involves periodic checks to determine the consistency and completeness of accounting information and to verify that all configuration management policies are being followed. A vendor's configuration management program must be able to sustain a complete configuration audit by a review team.

### Documentation change control

It's important to update all relevant documentation when system changes occur. Such changes could include the following:

- Changes to the system infrastructure
- Changes to security policies or procedures
- Changes to the disaster recovery or business continuity plans
- Facility environment changes, such as office moves or HVAC and electrical changes

Documentation control is a cornerstone of configuration management. Configuration management specifies strict adherence to documenting system changes, and the process of the documentation itself.

# Business Continuity and Disaster Recovery Planning

*Business continuity planning* addresses the preservation of the business in the face of major disruptions to normal operations. Business continuity includes the preparation, testing, and updating of the actions required to protect critical business processes from the effects of major system and network failures.

A disruptive event is any intentional or unintentional occurrence that suspends normal operations. The aim of business continuity planning is to minimize the effects of a disruptive event on a company. The primary purpose of business continuity plans is to reduce the risk of financial loss and enhance a company's capability to recover from a disruptive event promptly. The business continuity plan should also help minimize the cost associated with the disruptive event and mitigate the risk associated with it.

*Disaster recovery planning* is concerned with restoring the operation of the business's information systems following a harmful event.

The following definitions clarify some of the relevant terminology:

- **Contingency plan**— The documented, organized plan for emergency response, backup operations, and recovery maintained by an activity as part of its security program that will ensure the availability of critical resources and facilitates the continuity of operations in an emergency situation.
- **Disaster recovery plan**— The plan and procedures that have been developed to recover from a disaster that has interfered with the network and other information system operations.
- **Continuity of operations plan**— The plan and procedures documented to ensure continued critical operations during any period where normal operations are impossible.
- **Business continuity plan**— The plan and procedures developed that identify and prioritize the critical business functions that must be preserved and the associated procedures for continued operations of those critical business functions.

## Business continuity planning

Business continuity plans should evaluate all critical information processing areas of the organization, such as workstations and laptops, networks, servers, application software, storage media, and personnel procedures.

A wide variety of events can have an impact on the operations of a business and the information systems used by that business. These events can be either natural or man-made. Examples of such events include the following:

- Sabotage
- Arson
- Strikes
- Bombings
- Earthquakes
- Fire
- Floods
- Fluctuations in or loss of electrical power
- Storms
- Communication system failures
- Unavailability of key employees

### Business continuity planning goals and process

The business continuity planning process consists of four major elements:

- **Scope and plan initiation**— Creating the scope and the other elements needed to define the parameters of the plan.
- **Business impact assessment**— A process to help business units understand the impact of a disruptive event.
- **Business continuity plan development**— Developing the business continuity plan. This process includes the areas of plan implementation, plan testing, and ongoing plan maintenance.
- **Plan approval and implementation**— Final senior management signoff, enterprise-wide awareness of the plan, and implementing a maintenance procedure for updating the plan as needed.

These elements are discussed in more detail in the following sections.

#### Scope and Plan Initiation

The scope and plan initiation phase is the first step to creating a business continuity plan. It entails creating the scope for the plan and the other elements needed to define the parameters of the plan. This phase embodies an examination of the company's operations and support services. Scope activities could include creating a detailed account of the work required, listing the resources to be used, and defining the management practices to be employed.

#### Business Impact Assessment

A business impact assessment is a process used to help business units understand the impact of a disruptive event. This phase includes the execution of a vulnerability assessment. A business impact assessment is performed as one step during the creation of the business continuity plan. It is similar to a risk assessment.

The purpose of a business impact assessment is to create a document to be used to help understand what impact a disruptive event would have on the business. The impact might be financial (quantitative) or operational (qualitative, such as the inability to respond to customer complaints).

A business impact assessment has three primary goals:

- **Prioritization of critical systems**— Every critical business unit process must be identified and prioritized, and the impact of a disruptive event must be evaluated.
- **Estimation of downtime**— The business impact assessment is used to help estimate the *maximum tolerable downtime* that the business can tolerate and still remain a viable company; that is, what is the longest period of time a critical process can remain interrupted before the company can never recover. It is often found during the business impact assessment process that this time period is much shorter than expected.
- **Identification of resource requirements**— The resource requirements for the critical processes are identified at this time, with the most time-sensitive processes receiving the most resource allocation.

A business impact assessment is usually conducted in the following manner:

1. **Gather the appropriate assessment materials**. The business impact assessment process begins with identifying the critical business units and their interrelationships. Additional documents might also be collected in order to define the functional interrelationships of the organization.As the materials are collected and the functional operations of the business are identified, the business impact assessment will examine these business function interdependencies with an eye toward several factors, such as the business success factors involved, establishing a set of priorities between the units, and what alternate processing procedures can be utilized.
2. **Perform the vulnerability assessment**. The vulnerability assessment usually comprises quantitative (financial) and qualitative (operational) sections. The vulnerability assessment is smaller than a full risk assessment and is focused on providing information that is used solely for the business continuity plan or disaster recovery plan. A key function of a vulnerability assessment is to conduct a loss impact analysis.Quantitative loss criteria include:Incurring financial losses from loss of revenue, capital expenditure, or personal liability resolutionThe additional operational expenses incurred due to the disruptive eventIncurring financial loss from resolution of violation of contract agreementsIncurring financial loss from resolution of violation of regulatory or compliance requirementsTypical qualitative loss criteria comprise:The loss of competitive advantage or market shareThe loss of public confidence or credibility, or incurring public embarrassmentThe vulnerability assessment should address critical support functions such as the physical infrastructure, accounting, payroll, and telecommunications systems.
3. **Analyze the compiled information**. Analyzing the information as part of the business impact assessment includes:Identifying interdependenciesDocumenting required processesDetermining acceptable interruption periods
4. **Document the results; present recommendations**. All processes, procedures, analyses, and results should be documented and presented to management, including associated recommendations.The report will contain the previously gathered material, list the identified critical support areas, summarize the quantitative and qualitative impact statements, and provide the recommended recovery priorities generated from the analysis.

#### Business Continuity Plan Development

The *business continuity plan* is developed by using the information collected in the business impact assessment to create the recovery strategy plan to support the critical business functions. This process includes the areas of plan implementation, plan testing, and ongoing plan maintenance.

#### Plan approval and implementation

The object of this activity is to obtain the final senior management signoff, creating enterprise-wide awareness of the plan, and implementing a maintenance procedure for updating the plan as needed.

- **Senior management approval**— Because senior management is ultimately responsibility for all phases of the business continuity plan, they must have final approval. When a disaster strikes, senior management must be able to make informed decisions quickly during the recovery effort.
- **Plan awareness**— Enterprise-wide awareness of the plan is important and emphasizes the organization's commitment to its employees. Specific training may be required for certain personnel to carry out their tasks, and quality training is perceived as a benefit that increases the interest and the commitment of personnel in the business continuity planning process.
- **Plan maintenance**— Because of uncontrollable events, such as reorganization, employee turnover, relocation, or upgrading of critical resources, a business continuity plan might become outdated. Whatever the reason, plan maintenance techniques must be employed from the outset to ensure that the plan remains fresh and usable. It's important to build maintenance procedures into the organization by using job descriptions that centralize responsibility for updates. Also, audit procedures should be put in place that can report regularly on the state of the plan.

### Roles and responsibilities

The business continuity planning process involves many personnel from various parts of the enterprise. Creation of a business continuity planning committee represents the first enterprise-wide involvement of the major critical functional business units. All other business units will be involved in some way later, especially during the implementation and awareness phases.

- **The business continuity planning committee**— A business continuity planning committee should be formed and given the responsibility to create, implement, and test the plan. The committee is made up of representatives from senior management, all functional business units, information systems, and security administration. The committee initially defines the scope of the plan, which should deal with how to recover promptly from a disruptive event and mitigate the financial and resource loss due to a disruptive event.
- **Senior management**— Senior management has the ultimate responsibility for all phases of the plan, which includes not only initiation of the plan process but also monitoring and management of the plan during testing, and supervision and execution of the plan during a disruptive event. This support is essential, and without management being willing to commit adequate tangible and intangible resources, the plan will not be successful.Because management is required to perform due-diligence activities, stockholders might hold senior managers as well as the board of directors personally responsible if a disruptive event causes losses that adherence to base industry standards of due care could have prevented. For this reason and others, it is in the senior managers' best interest to be fully involved in the business continuity planning process.

## Disaster recovery planning

Disaster recovery planning is concerned with the protection of critical business processes from the effects of major information system and network failures, by quickly recovering from an emergency with a minimum impact to the organization.

### Goals

A disaster recovery plan is a comprehensive statement of consistent actions to be taken during and after a disruptive event that causes a significant loss of information systems resources.

Disaster recovery plans are the procedures for responding to an emergency, providing extended backup operations during the interruption, and managing recovery and salvage processes afterwards, should an organization experience a substantial loss of processing capability. Another objective of a properly executed disaster recovery plan is to provide the capability to implement critical processes at an alternate site and return to the primary site and normal processing within a timeframe that minimizes the loss to the organization.

### Disaster recovery process

The disaster recovery planning process involves developing the disaster recovery plan, testing the plan, and executing it in the event of an emergency.

#### Developing the disaster recovery plan

This first step involves developing the recovery plans and defining the necessary steps required to protect the business in the event of a disaster.

Automated tools are available to assisting in the development of the disaster recovery plan. These tools can improve productivity by providing formatted templates customized to the particular organization's needs.

#### Determining recovery time objectives

Early in the disaster recovery planning process, all business functions and critical systems must be examined to determine their recovery time requirements. Recovery time objectives are assigned to each function or system in order to guide the selection of alternate processing procedures. [Table 5-4](ch05.html#recovery_time_frames) summarizes the rating classes and associated recovery time frame objectives.

### Establishing backup sites

An important component of disaster recovery planning is maintaining a backup site that provides some degree of duplication of computing resources located away from the primary site. The types of backup sites are differentiated primarily by the extent to which the primary computing resources are replicated.

**Table 5.4. Recovery Time Frames**

| Rating Class | Recovery Time Frames |
| --- | --- |
| AAA | Immediate |
| AA | Full functional recovery within 4 hours |
| A | Same business day |
| B | Up to 24 hours down time permitted |
| C | 24 to 72 hours down time acceptable |
| D | Greater than 72 hours down time acceptable |

*Hot sites*, *warm sites*, and *cold sites* are the most common types of remote off-site backup processing facilities. They are differentiated by how much preparation is devoted to the site and, therefore, how quickly the site can be used as an alternate processing site. The following are the primary characteristics of these sites:

- **Cold site**— A designated computer operations room with HVAC that has no computing systems installed and, therefore, would require a substantial effort to install the hardware and software required to begin alternate processing. This type of site is rarely useful in an actual emergency.
- **Warm site**— An alternate processing facility with most supporting peripheral equipment, but without the principal computing platforms.
- **Hot site**— A site with all required computer hardware, software, and peripherals installed to begin alternate processing either immediately or within an acceptably short time frame. This site would be a duplicate of the original site and might only require an upgrade of the most current data to duplicate operations.

Additional options for providing backup capabilities include the following:

- **Mutual aid agreements**— An arrangement with another company that might have similar computing needs. Both parties agree to support each other in the case of a disruptive event by providing alternative processing resources to the other party. While appealing, this is not a good choice if the emergency affects both parties. Also, capacity at either facility might not be available when needed.
- **Rolling or mobile backup**— Contracting with a vendor to provide mobile power and HVAC facilitates sufficient to stage the alternate processing.
- **Multiple centers**— In a multiple-center concept, the processing is spread over several operations centers, creating a distributed approach to redundancy and sharing of available resources. These multiple centers could be owned and managed by the same organization (in-house sites) or used in conjunction with a reciprocal agreement.
- **Service bureaus**— An organization might contract with a service bureau to fully provide alternate backup-processing services. The advantages of this type of arrangement are the quick response and availability of the service bureau, the possibility of testing without disrupting normal operations, and the availability of the service bureau for more additional support functions. The disadvantages of this type of setup are the expense and resource contention during a large emergency.

### Plan testing

The disaster recovery plan must be tested and evaluated at regular intervals. Testing is required to verify the accuracy of the recovery procedures, verify the processing capability of the alternate backup site, train personnel, and identify deficiencies. The most common types of testing modes, by increasing level of thoroughness, are as follows:

- **Checklist review**— The disaster recovery plan is distributed and reviewed by business units for its thoroughness and effectiveness.
- **Tabletop exercise or structured walk-through test**— Members of the emergency management group meet in a conference room setting to discuss their responsibilities and how they would react to emergency scenarios by stepping through the plan.
- **Walk-through drill or simulation test**— The emergency management group and response teams actually perform their emergency response functions by walking through the test, without actually initiating recovery procedures. This approach is more thorough than the table-top exercise.
- **Functional drill**— This approach tests specific functions, such as medical response, emergency notifications, warning and communications procedures, and equipment, although not necessarily all at once. It also includes evacuation drills, where personnel walk the evacuation route to a designated area where procedures for accounting for the personnel are tested.
- **Parallel test or full-scale exercise**— A real-life emergency situation is simulated as closely as possible. It involves all the participants who would be responding to the real emergency, including community and external organizations. The test may involve ceasing some real production processing.
- **Full-interruption test**— Normal production is shut down and the disaster recovery processes are fully executed. This type of test is dangerous and, if not properly executed, can cause a disaster.

### Implementing the Plan

If an actual disaster occurs, there are three options for recovery:

- Recover at the primary operating site.
- Recover to an alternate site for critical functions.
- Restore full system after a catastrophic loss.

Two teams should be organized to execute the recovery, the *recovery* and *salvage* teams. The functions of these teams are as follows:

- **The recovery team**— Restore operations of the organization's critical business functions at the alternate backup processing site. The recovery team is concerned with rebuilding production processing.
- **The salvage team**— Repair, clean, salvage, and determine the viability of the primary processing infrastructure immediately after the disaster.

The disaster recovery plan should also address other concerns such as paying employees during a disaster, preventing fraud, conducting media relations, and performing liaison with local emergency services.

# Physical Security

Physical security is concerned with the protection of personnel, sensitive information, facilities, and equipment through the use of physical controls. Safeguards such as fencing, lighting, guard dogs, biometrics for identification, closed-circuit television, and physical lockdown devices are examples of physical control measures.

Threats to physical security include the following:

- Vandalism
- Sabotage
- Loss of electrical power
- Environmental conditions
- Strikes
- Natural disasters
- Water damage
- Toxic material release
- Earthquakes
- Extremes of temperature and humidity
- Smoke particles

To protect the confidentiality, integrity, and availability of networks and associated information systems, controls are implemented in accordance with cost considerations and best practices.

## Controls

Controls in physical security can be partitioned into physical, technical, and administrative types. These types of controls complement each other in providing effective protections for network security.

### Physical Controls

*Physical controls* are the most familiar types of controls. They usually control access and involve traditional deterrent items such as guards, lighting, fences, motion detectors, and so on. These types of controls are listed as follows:

- **Guards**— Guards can apply human judgment to interpret sensor presentations in addition to providing deterrent, response, and control capabilities.
- **Dogs**— Dogs are used primarily for perimeter physical control.
- **Fencing**— Fencing is the primary means of perimeter/boundary facility access control. Fences deter casual trespassing by controlling access to entrances.
- **Mantrap**— A mantrap is a physical access control method where the entrance to a facility or area is routed through a set of double doors. One door must be closed for the next door to open. It may or may not be monitored by a guard.
- **Lighting**— Protective lighting of entrances or parking areas can discourage prowlers or casual intruders. Common types of lighting include floodlights, street lights, Fresnel lights, and searchlights.
- **Locks**— Locks can be divided into two types: preset and programmable.**Preset locks**— Preset locks include key-in-knob, mortise, and rim locks. These all consist of variations of latches, cylinders, and dead bolts.**Programmable locks**— These locks can be either mechanically or electronically based. A mechanical programmable lock is often a typical dial combination lock. Another type of mechanical programmable lock is the common five-key push-button lock that requires the user to enter a combination of numbers. This is a very popular lock for IT operations centers. An electronic programmable lock requires the user to enter a pattern of digits on a numerical-style keypad, and it may display the digits in random order each time to prevent shoulder surfing for input patterns. It is also known as a cipher lock or keypad access control.
- **Closed-circuit television**— Visual surveillance or recording devices such as closed-circuit television are used in conjunction with guards in order to enhance their surveillance ability and to record events for future analysis or prosecution.
- **Perimeter intrusion detectors**— The two most common types of physical perimeter detectors are based either on photoelectric sensors or dry contact switches.**Photoelectric sensors**— Photoelectric sensors receive a beam of light from a light-emitting device, creating a grid of either visible white light, or invisible infrared light. An alarm is activated when the beams are broken. The beams can be physically avoided if seen; therefore, invisible infrared light is often used.**Dry contact switches**— Dry contact switches and tape are probably the most common types of perimeter detection. This can consist of metallic foil tape on windows or metal contact switches on doorframes.
- **PC physical controls**— Because of the proliferation of distributed computing and, particularly, laptops, inventory control for PCs is critical. Controls that address this issue include the following:**Cable locks**— A cable lock consists of a vinyl-covered steel cable anchoring the PC or peripherals to the desk. They often consist of screw kits, slot locks, and cable traps.**Port controls**— Port controls are devices that secure data ports (such as a floppy drive or a serial or parallel port) and prevent their use.**Switch control**— A switch control is a cover for the on/off switch, which prevents a user from switching off the file server's power.**Peripheral switch controls**— These types of controls are lockable switches that prevent a keyboard from being used.

### Technical Controls

Technical controls supplement physical and administrative controls and are typically used in highly secure facilities. Examples of technical controls are smart cards and biometric devices.

**Understanding Biometrics**

Biometrics are used for identification in physical access control, and for authentication in technical (logical) access control. In biometrics, *identification* is a one-to-many search of an individual's characteristics from a database of stored images. *Authentication* in biometrics is a one-to-one search to verify a claim to an identity made by a person. The three main performance measures in biometrics are as follows:

- **False rejection rate (FRR), or Type I error**— The percentage of valid subjects that are falsely rejected
- **False acceptance rate (FAR), or Type II error**— The percentage of invalid subjects that are falsely accepted
- **Crossover error rate (CER)**— The percent in which the FRR equals the FAR

In most cases, the sensitivity of the biometric detection system can be increased or decreased during an inspection process. If the system's sensitivity is increased, such as in an airport metal detector, the system becomes increasingly selective and has a higher FRR. Conversely, if the sensitivity is decreased, the FAR will increase.

Other important factors that must be evaluated in biometric systems are enrollment time, throughput rate, and acceptability. *Enrollment time* is the time it takes to initially register with a system by providing samples of the biometric characteristic to be evaluated. An acceptable enrollment time is around two minutes.

The *throughput rate* is the rate at which individuals, once enrolled, can be processed and identified or authenticated by a system. Acceptable throughput rates are in the range of 10 subjects per minute.

*Acceptability* refers to considerations of privacy, invasiveness, and psychological and physical comfort when using the system. For example, one concern with retina scanning systems may be the exchange of body fluids on the eyepiece. Another concern would be the retinal pattern that could reveal changes in a person's health, such as the advent of diabetes or high blood pressure.

Acquiring different data elements reflecting a biometric characteristic can greatly affect the storage requirements and operational speed of a biometric identification or authentication system. For example, in *fingerprint* systems, the actual fingerprint is stored and requires approximately 250KB per finger for a high-quality image. This level of information is required for one-to-many searches in forensics applications on very large databases. In *finger-scan* technology, a full fingerprint is not stored—the features extracted from this fingerprint are stored using a small template that requires approximately 500 to 1000 bytes of storage. The original fingerprint cannot be reconstructed from this template. Finger-scan technology is used for one-to-one verification using smaller databases. Updates of the enrollment information may be required because some biometric characteristics, such as voice and signature, can change with time.

#### Smart Cards

A smart card used for access control is also called a security access card. This card comprises the following types:

- **Photo-image cards**— Photo-image cards are simple identification cards with the photo of the bearer for identification.
- **Digital-coded cards**— Digitally encoded cards contain chips or magnetically encoded strips (possibly in addition to a photo of the bearer). The card reader may be programmed to accept or deny entry based on an online access control computer that can also provide information about the date and time of entry. These cards may also be able to create multi-level access groupings.
- **Wireless proximity readers**— A proximity reader does not require the user to physically insert the access card. This card may also be referred to as a wireless security card. The card reader senses the card in possession of a user in the general area (proximity) and enables access.

#### Biometric Devices

Biometric access control devices are technical applications in physical security. Biometric technologies can be used for identification or authentication.

The following are typical biometric characteristics used to uniquely identify or authenticate an individual:

- Fingerprints
- Retina scans
- Iris scans
- Facial scans
- Palm scans
- Hand geometry
- Voice
- Handwritten signature dynamics

### Administrative Controls

Administrative controls are related to personnel and facility issues. They include emergency procedures, personnel control, planning, and policy implementation.

Administrative controls are composed of the following:

- Administrative personnel controls
- Facility planning
- Facility security management

#### Administrative Personnel Controls

Administrative personnel controls include personnel-related processes commonly applied during employee hiring and firing. Examples of these controls include the following:

- Pre-employment screening, including employment, references, or educational history checks, and background investigation or credit-rating checks for sensitive positions
- Ongoing employee checks, such as security clearances, generated only if the employee is to have access to classified documents, and employee ratings or reviews by his or her supervisor
- Post-employment procedures such as exit interviews, removal of network access and change of passwords, and return of company equipment, including magnetic media, documents, and computer upon termination

#### Facility Planning

Facility planning is concerned with issues such as location of the facility, visibility of the facility, neighboring buildings and tenants, access to emergency services, and environmental considerations.

#### Facility Security Management

Facility security management includes the application of audit trails and emergency procedures. An audit trail is a record of events, such as the date and time of the access attempt, whether the attempt was successful or not, where the access was granted, who attempted the access, and who modified the access privileges at the supervisor level.

Audit trails contain critical information and should be protected at the highest level of security in the system. Audit trails serve to assist in determining the nature of the intrusion and tracking down the intruder after the fact.

## Environmental Issues

Clean, steady power is required to maintain the proper personnel environment as well as to sustain data operations. Many elements can threaten power systems, the most common being noise, brownouts, and humidity.

### Electrical Power

Electrical power systems service many different types of devices, ranging from electric motors to computers. Devices such as motors, computers, and radio transmitters superimpose fluctuations of different frequencies on the power line. These disturbances are referred to as electromagnetic interference and radio frequency interference. Electromagnetic interference usually refers to noise from motors and radio frequency interference refers to adverse interference caused by radio waves.

Interference on power lines can be reduced or eliminated by shielding data cables, proper grounding, and putting equipment containing motors on separate transformers than those supplying sensitive computers and related equipment.

### Note

As one example of such guidelines, the United States government created the TEMPEST standard to prevent electromagnetic interference eavesdropping by employing heavy metal shielding. TEMPEST is a classified program, and official information on the topic is difficult to obtain. However, there have been reports written on the fundamentals of TEMPEST. One such document is Technical Report Number 577, Cambridge University Computer Laboratory, UCAM-CL-TR-577, ISSN 1476-2986, entitled "Compromising Emanations: Eavesdropping Risks of Computer Displays" by Markus G. Kuhn (`www.cl.cam.ac.uk/`).

### Humidity

The correct level of humidity is critical to the operation of electronic components. If the humidity is too high, condensation will cause corrosion and possibly short circuits on printed circuit boards. Conversely, if the moisture content in the air is too low, high static charges can build up and, when discharged, can damage circuit components. The ideal operating humidity range is defined as 40 percent to 60 percent humidity.

Humidity can be controlled through the use of anti-static floor mats and anti-static sprays.

## Fire Suppression

Fire can obviously affect the operation of an information system. As with any other emergency, the safety of personnel is paramount. Preservation of data and system components should be considered only after the safe evacuation of personnel.

Fires are categorized into different classes as a function of the type of combustible material and the extinguishing agents. This information is summarized in [Table 5-5](ch05.html#fire_suppression_mediums).

**Table 5.5. Fire Suppression Mediums**

| Class | Description | Suppression Medium |
| --- | --- | --- |
| A | Common combustibles | Water or soda acid |
| B | Liquid | CO2, soda acid, or Halon |
| C | Electrical | CO2 or Halon |

A fire requires a fuel source, oxygen, and heat. From [Table 5-5](ch05.html#fire_suppression_mediums), soda acid suppresses the fuel source, water reduces the temperature, CO2 suppresses the oxygen supply, and Halon suppresses combustion through a chemical reaction.

Examples of the National Fire Protection Association (NFPA) fire class ratings are given in [Table 5-6](ch05.html#combustible_materials_fire_class_ratings).

**Table 5.6. Combustible Materials Fire Class Ratings**

| Fire Class | Combustible Materials |
| --- | --- |
| A | Wood, cloth, paper, rubber, most plastics, ordinary combustibles |
| B | Flammable liquids and gases, oils, greases, tars, oil-base paints and lacquers |
| C | Energized electrical equipment |
| D | Flammable chemicals such as magnesium and sodium |

### Fire Extinguishing Systems

Fires can be extinguished by means of gas discharge or water sprinkler systems. The characteristics of these systems are shown in [Table 5-7](ch05.html#types_of_fire_extinguishing_systems).

**Table 5.7. Types of Fire Extinguishing Systems**

| Type | Operation |
| --- | --- |
| Wet pipe | Water resides in a pipe under pressure and is released by a fusible link in the nozzle that melts if the temperature exceeds 165° F. |
| Dry pipe | Water is held back from the nozzle by a clapper valve. In the event of a fire, the clapper valve opens, air is discharged from the pipe, and the water emerges after a time delay. This delay allows some time to power down computer systems before they are inundated with water. |
| Deluge | Similar to a dry pipe system, but designed to discharge a much larger volume of water. |
| Preaction | Combines the clapper valve of a dry pipe system with the heat-sensitive nozzle of the wet pipe system. |
| Gas discharge | Uses an inert gas to retard combustion and the gas is usually delivered from under a raised floor. CO2 is one of the gases used. Halon was also popular, but because of personnel safety and environmental issues, Halon substitutes are required for new installations. |

## Object reuse and data remanence

*Object reuse* refers to using data that was previously recorded on a storage medium. For example, a Zip disk loaned to someone might contain your bank records. A related concept is having data remain on a storage medium after you think it has been erased. This phenomenon is called data remanence. Data can be removed from storage media by destroying the media; degaussing the media with a magnetic field, sometimes referred to as purging; and overwriting the media with other non-critical information. With the latter method, it is sometimes necessary to overwrite the data many times to ensure complete protection of the original information.

# Legal and Liability Issues

The field of investigating computer crime, or *computer forensics*, is the collecting of information from and about computer systems that is admissible in a court of law. To address computer crime, many jurisdictions have expanded the definition of property to include electronic information.

**Infamous Computer Crimes**

The following are some of the better-known examples of computer crimes that have made headlines in recent years in the general and technical press:

- The 2003 Sapphire or Slammer worm and the 2001 Code Red worm that randomly searched for IP addresses to infect.
- The 2002 Klez worm—alias ElKern, Klaz, or Kletz worm—contained hidden messages aimed at antivirus researchers.
- The 2000 distributed denial-of-service attacks perpetrated against Amazon.com and Yahoo!.

## Types of Computer Crime

Computer crimes range from applying social skills to obtain passwords to critical information systems to flooding servers with so many connection requests that the servers are overwhelmed. [Table 5-8](ch05.html#examples_of_types_of_computer_crimes) provides examples of the different types of computer crimes.

**Table 5.8. Examples of Types of Computer Crimes**

| Crime | Activity |
| --- | --- |
| Social engineering | Applying social skills to trick people in order to obtain information, such as passwords or PIN numbers, to be used in an attack against computer-based systems. The book *The Art of Deception: Controlling the Human Element of Security* by Kevin D. Mitnick, William L. Simon, and Steve Wozniak provides detailed insight into the field of malicious social engineering. |
| Network intrusions | Obtaining unauthorized access to networked computers. |
| Illegal content of material | Downloading pornographic material or sending offending e-mails. |
| Denial of service (DoS) and distributed denial of service (DDoS) | Flooding an information system with vast numbers of requests for service to the point where the information system cannot respond and is consuming so many resources that normal processing cannot occur. |
| Malicious code | Code such as viruses, Trojan horses, and worms that infect a computer and negatively affect its operation. |

## Electronic Monitoring

A gray area is the right of an employer to monitor an employee's computer communications or those of an outsider accessing an organization's computer network. An organization can be on firmer legal ground if it frequently and unambiguously notifies all who access the network that their activities are subject to monitoring. This notification can take the form of a logon banner stating that by logging on to the system, the individual consents to electronic monitoring and is subject to a predefined punishment if the system is used for unlawful activities or if the user violates the organization's information security policy. It should also state that unauthorized access and use of the system is prohibited and subject to punishment. It is important that the notification and monitoring be uniformly applied to all employees.

## Liability

Upper management of an organization is ultimately responsible for protecting the organization's intellectual property. Best practices require that management apply the *prudent man rule* that "requires officers to perform duties with diligence and care that ordinary, prudent people would exercise under similar circumstances." The officers must exercise *due care or reasonable care* to carry out their responsibilities to the organization. Examples of due care include ensuring the proper information security controls are in place and functioning, appropriate security polices exist and are applied, business continuity plans have been developed, and appropriate personnel screening is conducted.

The criteria for evaluating the legal requirements for implementing safeguards is to evaluate the cost (C) of instituting the protection versus the estimated loss (L) resulting from exploitation of the corresponding vulnerability. If C < L, then a legal liability exists.

# Summary

Managing information system security proceeds from the top down. Senior management must generate, distribute, and enforce the organization's information security policy. An important aspect of the policy is that the appropriate personnel are trained to be security aware and understand the policy requirements. When a policy and the associated procedures are in place, management tools should be applied to ensure the resulting corporate products meet their quality requirements. A component of the corporate policy is the DRP/BCP plan, which maintains the continuity of the operation of the organization in the event of a disaster.

Another component of managing security is the implementation of appropriate physical security measures to protect the organization's information systems. Organizational management must understand the responsibilities and liabilities associated with its role in ensuring that the organization's intellectual property is not compromised.
