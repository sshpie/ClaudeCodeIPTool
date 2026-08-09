# IIoT security core building blocks

The IIC has defined a security framework that consists of several overlapping building blocks, including endpoint (edge to cloud) protection, communications and connectivity protection, security monitoring and analysis, and security configuration and management. These are surrounded by a data protection layer that is, in turn, surrounded by a security model and policy layer, as shown in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/357e1124-6c13-428a-b7e8-782cee5f3ede.png)

Figure 8.2: Building blocks of securityProtecting your IIoT infrastructure relies on taking the proper steps needed to protect physical components, related software components, and data.

The four core building blocks are defined as follows:

- Endpoint (edge-to-cloud components) protection, including defensive capabilities such as physical security, cyber security, and authoritative security
- Communications and connectivity protection based on authorizations linked to identities required to access components from the edge to the cloud over networks and the authentication and authorization of related data traffic
- Security monitoring and analysis used in capturing data from endpoints and in motion between endpoints, detecting possible security violations or threats and then responding appropriately
- Security configuration and management capabilities used to define system functionality and security changes

Physical component security focuses on providing limited physical access to the devices and the data center (in the cloud or on-premises). These security measures include defined procedures for gaining access and limiting available physical connections to devices and systems.

Endpoint protection and communications and connectivity protection rely heavily on proper authentication. Authentication is the first step in gaining access to a platform.

Endpoints

 The IIC uses endpoints to describe any smart device, gateway, or computational engine in the IIoT architecture. Each should be secured, including cloud-based or on-premises backend systems.You are likely very familiar with authentication as a concept as you, no doubt, provide a password when you log into platforms today. Your username and password combination proves that you are who you say you are and should therefore gain access. In a world in which these combinations are sometimes compromised, it is becoming increasingly common for multi-factor authentication to be required. This is usually accomplished by having you verify that you are attempting to log in by acknowledging it through a PIN or other recognition of you from your personal device. The same concepts are applied in IIoT infrastructures, albeit in a bit more complicated model.

Authentication of devices and gateways often relies on the presence of an X.509 certificate issued by a certificate authority. The certificate contains a private key that is matched to a public key shared between devices or gateways. When matches are made, data transmissions are allowed. Given the real-time nature of these transmissions, **pre-shared keys** (**PSKs**) are typically used.

Authentication in the backend services often relies on the presence of a directory of users that is also a source of user access rights and credentials. Commonly used directories include the **Lightweight Directory Access Protocol** (**LDAP**) and Active Directory. Authentication might also rely on more complex schemes such as those offered by **Kerberos**, an authentication method that relies on a service ticket issued by a key distribution center to validate credentials.

Proper authorization is also needed to prevent compromises at endpoints and over communications channels and connectivity locations. Access rights to data-management servers are typically defined for specific roles by data lake and database administrators managing those engines. **Access Control Lists** (**ACLs**) can provide a granular way to manage authorization across the infrastructure.

Data is the lifeblood of the IIoT ecosystem. Data must be protected while it is at rest, in use, and in motion. Methods to protect data include confidentiality controls, integrity controls, access controls, isolation, and replication. Protection of data often includes encoding it to hide its content from unauthorized devices and people. Encryption algorithms are most commonly applied to data prior to its transmission (data in motion) and when it is at rest (in storage). When data is read by valid users and devices, it is unencrypted into plain text.

During architecture design, it is not too early to think about the current security models and policies in place in the organization or mandated by regulatory compliance requirements. The policy defines the security objectives of the architecture. The model provides a formal representation as to how the policies can be enforced. Security policies that need to be addressed include the following:

- Configuration and management policy
- Monitoring and analysis policy
- Communications and connectivity policy
- Endpoint security policy
- Data protection security policy

While the IIC security framework is a suitable place to start, there are other cybersecurity frameworks that also deserve our attention.
