# Risk assessments and best security practices

A secure IIoT deployment strategy begins with architecture planning. As a design comes together, an evaluation of the proposed components' capabilities for supporting authentication and authorization capabilities, encryption of data, and configurability of software and firmware should begin. Proposed interfaces, such as those to be provided by the network, edge devices, and gateways, as well as user access, are also evaluated.

As the design nears completion, many choose to perform a risk assessment, identifying potential threats to the planned IIoT implementation and their consequences. Threats can come in many ways including through physical attacks, network attacks, attacks on software, attacks on operators, and attacks on the IIoT supply chain itself. The assessment is used to understand both classic information system risks and the physical consequences of errors and attacks.

The Center for Internet Security, a non-profit organization consisting of over 180 members, defined 20 areas that can provide the foundation of a risk assessment of an IIoT architecture and deployment of the solution. During the architecture definition, the ability of the proposed architecture to provide these capabilities should be evaluated:

- Inventory of authorized and unauthorized devices
- Inventory of authorized and unauthorized software
- Secure configurations for hardware and software on devices, laptops, workstations, and servers
- Continuous vulnerability assessment and remediation
- Malware defenses
- Application software security
- Wireless access control
- Data recovery capability
- Security skills assessment and appropriate training to fill gaps
- Secure configurations for network devices such as firewalls, routers, and switches
- Limitation and control of network ports, protocols, and services
- Controlled use of administrative privileges
- Boundary defense
- Maintenance monitoring and analysis of audit logs
- Controlled access based on the need to know
- Account monitoring and control
- Data protection
- Incident response and management
- Secure network engineering
- Penetration tests and red team exercises

Choosing trusted component builders and providers and trusted systems implementers is essential. Some risks can be mitigated by defining security perimeters around devices and deploying networks and information systems using best practices (or relying on cloud providers to do so). Once IIoT solutions are deployed, trusted systems owners and operators will help assure that security is maintained.

Understanding the best practices that should be put into place after deployment is recommended at an early stage as these can influence the architecture and selection of components. Foundational controls should be placed on hardware and software configurations that are defined.

Once the solution is deployed, vulnerabilities must be assessed continuously and remediated. Certainly, monitoring of audit logs in data-management systems is required.  Ensuring software and firmware upgrades are secure while keeping software up-to-date as security patches are released is fundamental. However, as much data is also processed in real time, detection and response to real-time threats is also required.

Detection often focuses on targeting specific signals and monitoring behavior. When problems are detected, automated responses might include blocking and a quarantine of suspicious devices, elevation of access requirements based on identity risks, revoking access to data, blocking risky applications, and wiping untrustworthy device data. Public cloud-based solutions are sometimes chosen for backend deployment because of the advanced machine learning these cloud vendors put in place to detect threats and respond immediately by taking actions such as these.

Once IIoT solutions are implemented, security methods should be tested via simulations to determine where vulnerabilities exist. Some organizations create teams of people who try to defeat the security measures to test the robustness of the solution. Architects and operations planners will sometimes specify that some duplicate devices, networking, and backend components be placed in a development lab and be utilized for testing security vulnerabilities and procedures.
