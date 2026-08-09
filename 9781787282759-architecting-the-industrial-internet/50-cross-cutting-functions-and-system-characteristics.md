# Cross-cutting functions and system characteristics

The business, usage, functional, and implementation viewpoints bring together the requirements and concerns of their respective stakeholders, and help provide a framework for developing the IIoT architecture. In general, the business viewpoint determines the mission and the boundaries for the usage viewpoint, ultimately driving the requirements for the functional and implementation viewpoints. In turn, the functional and implementation viewpoints may influence or impose limitations on the business viewpoint. For example, if the business viewpoint requires that field engineers must react immediately to certain events, in all conditions, then the usage viewpoint may determine they need heat-proof, waterproof, shockproof devices with unlimited connectivity to receive the information. The business viewpoint may then determine it is not cost-effective to provide all field engineers with such devices.

Cross-cutting functions support activities across the functional components and cut across the generic IIoT system capabilities. These enabling functions include data management, connectivity, and analytic capabilities.

System characteristics are system-wide properties required to manage the interaction of the parts of the IIoT system. System characteristics focus on how the system works rather than what the system does from a functional or business perspective. These functions are typically only noticed by end users when they fail. These characteristics include security, privacy, scalability, safety, resilience, and reliability. These interconnected characteristics contribute to the trustworthiness of the system. Trustworthiness also depends on how well the system characteristics are integrated into the functional components and their interactions. Basically, trustworthiness is dependent on the weakest link; for example, privacy cannot be protected if security is weak. *Figure 2.8*illustrates the relationship between functional domains, cross-cutting functions, and system characteristics.

A strong architecture incorporates cross-cutting functions and system characteristics while also ensuring the proper functioning of the fundamental capabilities:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/911692b7-9b77-4d66-bf91-44dfb6366348.png)

Figure 2.8:  Functional domains, crosscutting functions, and system characteristics
