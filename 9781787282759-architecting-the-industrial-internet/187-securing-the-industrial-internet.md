# Securing the Industrial Internet

One aspect of architecture planning for an IIoT implementation that requires special attention is defining a secure Industrial Internet solution. This topic seems to spring to  mind whenever reports of hacking these solutions are prevalent. The downside to not considering protective and proactive security measures and their impact upon the architecture is the potential failure of the entire infrastructure at critical times. The resulting implications can include negative impact to the business, danger to safety, and exposure to ransomware.

The IIC defines IIoT security as simply protecting the Industrial Internet solution from unintended or unauthorized access, change, or destruction. Data and infrastructure confidentiality, integrity, and availability must be maintained to assure trustworthiness of the solution. Proper security can be measured in the reliability, resilience, privacy, and safety provided by the solution.

Designing a secure solution requires taking an holistic view of the devices provided by various manufacturers, device interconnects and networks, and backend infrastructure component providers. Architects, systems integrators, deployment specialists, and solutions operators all play a part in securing the implementation.

Most dangerous tactics meant to compromise the security of Industrial Internet solutions rely on ways of getting around authentication and authorization measures that are put in place and linked to roles. Authentication is the process of proving the validity of a party. Authorization is the permission granted to a party to perform a specific task.

The IIC defines a role as a set of capacities assumed by an entity to participate in the execution of tasks or functions in an IIoT implementation. Roles are assumed by parties that could be humans or automated agents.

One technique sometimes used to bypass authentication is spoofing. Spoofing can trick devices or systems by hiding or faking the identity of a party that would not otherwise be granted access. The bypassing of authorization limits for devices or users to obtain higher privileges can take place through rogue privilege escalation techniques.

Trustworthiness of the solution can also be destroyed in other ways. Data tampering, including its altering, destruction, or removal, can occur when access to devices and systems is gained without proper authorization. This is sometimes accomplished through unauthorized privilege escalation of authenticated users or agents. Unauthorized information disclosure might occur if non-repudiation capabilities are not in place to assure proper authentication of devices and users.

The entire infrastructure can become unavailable because of **Denial of Service** (**DoS**) attacks. These attacks prevent authorized processes and users from accessing devices and systems by flooding networks with data and/or overloading servers. In a variation called **Distributed Denial of Service** (**DDoS**) attacks, multiple devices are compromised such that they then work together to flood the networks and overload other components with data.

Understanding potential threats and where they might occur is critical to defining a secure architecture. One must evaluate the devices and sensors, gateways, the data stores, data flows, and external entry points. Proper operational techniques must also be implemented. Taking proactive steps to avoid and mitigate risk is just the first step.

Many security experts now believe that security breaches and compromises are inevitable. So, there is some acceptance of risk. To counter these eventualities, fast detection of threats, including identification of their nature with appropriate responses and recovery, are necessary. Rapid threat detection and response is a focus of public cloud vendors, as we will note later in this chapter.

We will begin the chapter by reviewing fundamental security concepts. Since this book focuses on architecture, we will then explore potential security issues and ways to protect against them from the edge (devices and sensors) to the data center in the next two sections of this chapter. Then, we'll introduce the scope of risk assessments and best practices used to assure security and apply what you have learned to the supply chain example.

In this chapter, we will cover the following topics:

- Examples of cybersecurity attacks
- IIoT security core building blocks
- NIST cybersecurity frameworks
- IIoT security guidelines
- Securing devices and the edge to the cloud gateway
- Securing backend services
- Risk assessments and best security practices
- Planning for security in the supply chain example

When you complete this chapter, you should be able to understand the potential vulnerabilities in the various IIoT architecture components and steps you can take to secure these components and counter the threats that will exist.
