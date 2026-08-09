# Chapter 6. Access Control

**IN THIS CHAPTER**

- **Understanding the different access control models**
- **Understanding the different access control types**
- **Defining identification, authentication, authorization, and accountability**
- **Reviewing databases and database security**
- **Implementing remote access security and controls**

Controlling access to a network and its associated resources is the cornerstone of network security. Access control is the key component of protecting organizations' information and minimizing the harm that can be caused by an attacker. In today's distributed computing environment, where large amounts of computing power and sensitive intellectual property reside on individuals' desks, access control is crucial to any organization. It is important that the confidentiality, integrity, and availability of the information be always properly preserved.

This chapter describes methods used to categorize access controls, the different types of controls, and means for providing for secure and verifiable local and remote login.

# Control Models

Access control is designed to control who has access to information and mitigate access-related vulnerabilities that could be exploited by threats to a network. A *threat* is an event or activity that has the potential to cause harm to the network. In this case, the threat would have the potential to bypass or foil access control mechanisms and allow an attacker to gain unauthorized access to a network. This unauthorized access could include disclosing, altering, or denying access to critical information. A *vulnerability* is a weakness that can be exploited by a threat, causing harm to the network. The probability that a threat will materialize and result in harm to the network is defined as *risk*.

In discussing access control, the terms "subject" and "object" are used. A *subject* is an active entity (such as an individual or process) and an *object* is a passive entity (such as a file). Subjects perform some action on objects. One of the key goals of access control is to limit or give a subject the least amount of access it needs to access an object. For example, Eric (a subject) can have only read access to file X (the object). It is important to remember that these roles can change. For example, in the previous example Eric was the subject and file X was the object. However, if file X were an .exe file that Eric executed which now runs as a service on the system and accesses other files, its role has now changed; file X would now have turned into a subject because it is actively accessing and changing other objects.

Access control models can be classified as discretionary, mandatory, and non-discretionary. The classification is based on who can control and change the access that is allowed.

## Discretionary Access Control

With *discretionary access control* (DAC), the owners of objects get to decide within their discretion (following policy and procedures), what objects a given subject can access.

An authorizing entity or the subject has authority, within certain limitations, to specify the objects that can be accessed. One means of specifying discretionary access control is through a table. The table contains the subjects, objects, and access privileges that are assigned to the subjects relative to the objects. This table is sometimes called an *access control list* (ACL). [Table 6-1](ch06.html#access_control_list) is an example of an ACL.

**Table 6.1. Access Control List**

| Subject | Object 1 | Object 2 | Object 3 |
| --- | --- | --- | --- |
|  | **File Salary** | **File Benefits** | **Process Evaluation** |
| Program salary | Read/write | Read | Execute |
| Ms. Jones | None | Read | None |
| Mr. Tops | Read/write | Read/write | None |
| Process average | Read/write | Read | None |

[Table 6-1](ch06.html#access_control_list) shows that the program named Salary can read or write data from the file named Salary and has read privileges for the file named Benefits. Also, the program Salary can execute the process called Evaluate.

A user who has the right to alter the access privileges to certain objects operates under *user-directed* discretionary access control. Usually the owner of an object is the person who has the right to make changes. On many systems, the creator of an object becomes the owner. Therefore, ownership must be carefully managed and controlled to make sure subjects are always given the least amount of access they need to perform their jobs.

With DAC, because owners can essentially make any access control changes to an object, it is critical that proper auditing be put in place to provide checks and balances for this process.

The benefits of DAC include ease of implementation because this functionality is built into almost every operation system and application available today. The drawback is that inadvertent changes can be made and strong auditing is required as a validation point.

If more robust, systematic protection is required, mandatory access control might be more appropriate.

## Mandatory access control

In *mandatory access control* (MAC), means must be found to formally match the authorizations allocated to the subject to the sensitivity of the objects that are the target of the access request. One approach is to use *labels*. The subject's authorization can be in the form of a *clearance* that is to be compared to *classification* of the object. In the United States, the military classifies documents as unclassified, confidential, secret, and top secret. Similarly, an individual can receive a clearance of confidential, secret, or top secret, and can have access to documents classified at or below his or her specified clearance level.

With MAC, a subject can access only objects that are equal or lower in classification to the clearance level the subject maintains. Thus, an individual with a secret clearance can access secret and confidential documents, but not top secret information. An additional level of protection that can be applied is called the *need to know*. Need to know means that the subject must have a need to access the requested classified document to perform its assigned duties.

Because all access requests from subjects to objects must be carefully guarded, MAC-based systems utilize a reference monitor. The reference monitor is implemented by the security kernel and is one of the most trusted components of the system. All requests must go through the reference monitor and it can never be bypassed or disabled.

MAC-based access control is very common in multi-level secure (MLS) systems. These are systems in which the objects have different classifications and the subjects have different clearances. In this system, it has to be guaranteed that if users with confidential clearances log in, they cannot access top secret or even secret information.

The benefits of MAC-based access control are that it cannot be overwritten or bypassed and that it strongly enforces all requests. The disadvantages are that it requires custom operating systems to implement the reference monitor and requires all entities to be assigned labels.

## Non-discretionary access control

In *non-discretionary access control*, access privileges might be based on the individual's role in the organization (*role-based*) or the subject's responsibilities and duties (*task-based*). Role-based access control is often used in an organization where there are frequent personnel changes, to eliminate the need to change privileges whenever a new person takes over that role.

Access control can also be characterized as context-dependent or content-dependent. *Context-dependent access control* is a function of factors such as location, time of day, and previous access history. It is concerned with the environment or context of the data. In *content-dependent access control*, access is determined by the information contained in the item being accessed.

One of the more popular non-discretionary access controls is role-based access control (RBAC). RBAC creates roles for each user, and an individual can only be a member of a single group at a given time. This goes beyond traditional groups that organizations use today. One of the main problems with using groups is that a user can be a member of multiple groups at the same time. Therefore, the longer someone works at an organization the more access that person has because he or she keeps getting added to additional groups. With RBAC, if users change jobs, they are moved to a new role. And when they are added to the new role, they are automatically removed from the previous one.

# Types of Access Control Implementations

Access controls are used to prevent attacks, to determine if attacks have occurred or been attempted, and to bring the network back to its pre-attack state if an attack was successful. The three common types of controls are called *preventive, detective*, and *corrective*, respectively. One of the key mottos I use is "Prevention is ideal but detection is a must." While I prefer to prevent and stop all attacks, that is not practical. Therefore in cases where I cannot prevent or stop an attack, I have to be able to detect it in a timely manner. However, whenever I detect an attack, that means the preventive measures failed. I would than deploy a corrective measure to fix the problem so that I can prevent it in the future.

There are many other subcategories of controls including directive, deterrent, and reactive; however, initially we will focus on the core components of prevention and detection. This maps with the key assessment methodology of assess, prevent, detect, and react.

To effect these controls, administrative, technical (logical), and physical means are employed. *Administrative controls* include activities such as creating policies and procedures, security awareness training, and background checks. *Technical (logical) controls* involve the use of approaches that include encryption, smart cards, and transmission protocols. *Physical controls* are more familiar and comprise guards, building security, and securing laptops. By joining the control types and implementation means, different control combinations are obtained. Examples of the key combinations are listed in the following sections.

## Preventive/administrative

Preventive and administrative controls include the following:

- Organizational policies and procedures
- Background checks
- Employee termination procedures
- Employment agreements
- Security awareness training
- Labeling of sensitive materials
- Vacation scheduling

## Preventive/technical

Preventive and technical controls apply technology to prevent violations of an organization's security policy. Technical controls are also known as logical controls and can be built into the operating system, can be software applications, or can be supplemental hardware or software units. Examples of preventive and technical controls include the following:

- Protocols
- Biometrics for authentication
- Encryption
- Smart cards
- Menus
- Constrained user interfaces
- Passwords
- Limited keypads

In the preceding list, constrained user interfaces limit the functions available to a user, for example, by "graying out" choices on the user menu that cannot be selected. Similarly, limited keypads restrict the choice of functions to those available on the keys provided.

## Preventive/physical

This category is concerned with restricting physical access to areas with systems holding sensitive information. Preventive and physical controls include the following:

- Guards
- Man-traps (consisting of two doors physically separated so that an individual can be "trapped" in the space between the doors after entering one of the doors)
- Fences
- Biometrics for identification
- Environmental controls (temperature, humidity, electrical)
- Badges

## Detective/administrative

Detective and administrative controls comprise the following:

- Audit record review
- Sharing of responsibilities
- Organizational policies and procedures
- Background checks
- Vacation scheduling
- Labeling of sensitive materials
- Behavior awareness

## Detective/technical

Detective and technical controls apply technical means to identify the occurrence of an intrusion or other violations of an organization's security policy. These measures include the following:

- **Intrusion detection systems (IDSs)**— These devices are characterized by the technology used to detect an intrusion or its location. For example, a host-based ID system (HIDS) resides on a computer and performs well in detecting attacks on the host because it has details about the system it is protecting. However, this type of IDS is not effective in detecting network intrusions and does not scale very well. Conversely, a network-based IDS (NIDS) is a passive detector (sniffer) of real-time intrusions. IDSs detect intrusions by two principal methods. One approach is to profile a "normal" usage state for a network or host and then detect deviations from this state; this is known as *anomaly detection*. The other approach is to acquire "signatures" of attacks and then monitor the system for these signatures when an attack occurs.
- **Violation reports generated from audit trail information**— These reports can indicate variations from "normal" operation or detect known signatures of unauthorized access episodes. *Clipping* or threshold levels can be employed to limit the amount of audit information flagged and reported by automated violation analysis and reporting mechanisms. Clipping levels can set a threshold on the number of occurrences of an event, below which the event is not reported.

## Detective/physical

Detective and physical controls normally require a human to evaluate the input from sensors for a potential threat. Examples of these types of control mechanisms include:

- Video cameras
- Motion detectors
- Thermal detectors

## Centralized/decentralized access controls

Centralized access control is usually characterized by centrally managed resources and knowledgeable professionals with experience in the various types of control mechanisms. Centralized access control systems and protocols, such as RADIUS, TACACS+, and diameter, are discussed later in this chapter.

On the other hand, decentralized access controls are closer to the user and, consequently, should reflect the user's concerns and requirements. A paradigm for decentralized access control is the establishment of *security domains*, in which participants are under the same management and follow common security policies.

Decentralized systems have the need for strong access control. An example would be an organization using the World Wide Web to facilitate communications and cooperation among its subentities. Generally, these systems exhibit the following characteristics:

- Encryption of passwords and IDs.
- Formal access control rules.
- Each subentity authenticates its respective clients.
- Additional subentities can be added to the network.

# Identification and Authentication

*Identification* is the act of a user professing an identity to a system, usually in the form of a logon ID. Identification establishes user accountability for his or her actions on the system. *Authentication* is verification that the user's claimed identity is valid, and it is usually implemented through a user password at logon time. Authentication is provided through a variety of means from secret passwords to using biometric characteristics. In general, authentication is accomplished by testing one or more of the following items:

- Something you know, such as a personal identification number (PIN) or password; this factor is known as Type 1 authentication.
- Something you have, such as an ATM card or smart card; this factor is known as Type 2 authentication.
- Something you are (physically), such as a fingerprint or retina scan; this factor is known as Type 3 authentication.

Obviously, using more than one factor adds additional credence to the authentication process. For example, *two-factor authentication* refers to using two of the three factors, such as a PIN number (something you know) in conjunction with an ATM card (something you have).

Identification and Authentication are part of AAA — authentication, authorization, and accountability. After authentication, a user is granted rights and permissions to access certain computer resources and information. This allocation is known as *authorization* of the user. Once users are given access, all their actions should be logged, to hold them accountable for what they do on the system.

## Passwords

Passwords are, by far, the most popular factor used for authentication. Therefore, protecting passwords from compromise and unauthorized use is crucial.

Similar to a one-time pad in cryptography, a *one-time password* provides the highest level of password security. Because a new password is required every time a user logs on to the network, an attacker cannot use a previously compromised password. A password that changes frequently is called a *dynamic password*. A password that is the same for each logon is called a *static password*. An organization can require that passwords change monthly, quarterly, or at other intervals, depending on the sensitivity of the protected information and the password's frequency of use.

In some instances, a passphrase can be used instead of a password. A *passphrase* is a sequence of characters that is usually longer than the allotted number of characters for a password. The passphrase is converted into a virtual password by the system.

Passwords can be generated automatically by credit card–sized memory cards, smart cards, or devices resembling small calculators. Some of these devices are referred to as *tokens*. These password generators are Type 2 devices, something you have.

## Biometrics

*Biometrics* is defined as an automated means of identifying or authenticating the identity of a living person based on physiological or behavioral characteristics. Biometrics is a Type 3 authentication mechanism because it is based on what a person "is." Biometrics is useful in both identification and authentication modes.

For identification, biometrics is applied as a *one-to-many* search of an individual's characteristics from a database of stored characteristics of a large population. An example of a one-to-many search is trying to match a suspect's fingerprints to a database of fingerprints of people living in the United States. Conversely, authentication in biometrics is a *one-to-one* search to verify a claim to an identity made by a person. An example of this mode is matching an employee's fingerprints against the previously registered fingerprints in a database of the company's employees. When it comes to access control, biometrics is used for identification in physical controls and for authentication in logical controls.

Performance measures of a biometric system range from technical characteristics to employees "feeling comfortable" with their use. The following are examples of performance measures:

- **Type I Error or False Rejection Rate (FRR)**— The percentage of valid subjects that are falsely rejected.
- **Type II Error or False Acceptance Rate (FAR)**— The percentage of invalid subjects that are falsely accepted.
- **Crossover Error Rate (CER)**— The percent in which the FRR equals the FAR. The smaller the CER, the better the biometric system.
- **Enrollment time**— The time that it takes to initially "register" with a system by providing samples of the biometric characteristic to be evaluated. An acceptable enrollment time is around two minutes.
- **Throughput rate**— The rate at which the system processes and identifies or authenticates individuals. Acceptable throughput rates are in the range of 10 subjects per minute.
- **Acceptability**— The considerations of privacy, invasiveness, and psychological and physical comfort when using the system. For example, a concern with retina scanning systems would be the retinal pattern, which could reveal changes in a person's health, such as the onset of diabetes or high blood pressure.

The following are typical biometric parameters that are in use today:

- Retina scans
- Iris scans
- Fingerprints
- Facial scans
- Palm scans
- Hand geometry
- Voice
- Handwritten signature dynamics

## Single Sign-On

In *Single Sign-On* (SSO), a user provides one ID and password per work session and is automatically logged on to all the required network resources and applications. Without SSO, a user normally must enter multiple passwords to access different network resources. In applying SSO, passwords should be transmitted or stored in encrypted form for security purposes. With SSO, network administration is simplified, a stronger password can be used, and resources can be accessed in less time. The major disadvantage of many SSO implementations is that once a user obtains access to the system through the initial logon, the user can freely roam the network resources without any restrictions. In addition, if those credentials are ever compromised, an attacker would have significant access to network resources.

SSO can be implemented in the following ways:

- Through scripts that replay the users' multiple logins.
- Through Enterprise Access Management (EAM). EAM provides access control management services, including SSO, to Web-based enterprise systems. In one approach, SSO is implemented on Web applications residing on different servers in the same domain by using nonpersistent, encrypted cookies on the client interface.
- Using authentication servers to verify a user's identity and encrypted authentication tickets to permit access to system services.

A popular authentication server approach that can implement SSO is the Kerberos system.

### Kerberos

Kerberos is named after a three-headed dog that guards the entrance to the underworld in Greek mythology. Kerberos is based on symmetric key cryptography and was developed under Project Athena at the Massachusetts Institute of Technology (MIT). It is a trusted, third-party authentication protocol that authenticates clients to other entities on a network and provides secure means for these clients to access resources on the network.

Kerberos assumes that client computers and network cables are publicly accessible in insecure locations. Thus, messages transmitted on a Kerberos network can be intercepted. However, Kerberos also assumes that some specific locations and servers can be secured to operate as trusted authentication mechanisms for every client and service on that network. These centralized servers implement the Kerberos-trusted Key Distribution Center (KDC), Kerberos Ticket Granting Service (TGS), and Kerberos Authentication Service (AS). The basic principles of Kerberos operation are summarized as follows:

- The KDC knows the secret keys of all clients and servers on the network.
- The KDC initially exchanges information with the client and server by using these secret keys. (Knowledge of the secret key is how you authenticate.)
- Kerberos authenticates a client to a requested service on a server through the TGS and by issuing temporary symmetric session keys for communications between the client and KDC, the server and the KDC, and the client and server.
- Communication then takes place between the client and the server by using those temporary session keys.

A Kerberos exchange begins with a user entering his or her password into a Kerberos client workstation. The user's password is then converted to the user's secret key in the workstation. This secret key resides temporarily on the workstation. Then, the client transmits the user's ID in unencrypted form to the Ticket Granting Service, as illustrated in [Figure 6-1](ch06.html#initial_client_to_tgs_exchange).

![Initial client to TGS exchange](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0601.png)

**Figure 6.1. Initial client to TGS exchange**

In response, the TGS sends the client a TGS-client session key, which is called Ktgs,c, encrypted with the user's secret key. In addition, the TGS also sends a ticket granting ticket (TGT) encrypted with a key known only to the TGS. This exchange is shown in [Figure 6-2](ch06.html#tgs_and_client_session_key_solidus_tgt_e).

![TGS and client session key/TGT exchange](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0602.png)

**Figure 6.2. TGS and client session key/TGT exchange**

Upon receipt of these messages, the client decrypts Ktgs,c with the user's secret key. For this example, the user is requesting access to a print server, PS. So, the client sends a request to the TGS for a print server ticket. This request, shown in [Figure 6-3](ch06.html#client_to_tgs_request_for_ps_ticket), comprises an authenticator, A, and time stamp, both encrypted with Ktgs,c, and the TGT encrypted with the key known only to the TGS.

In the next step of the sequence, the TGS transmits a client-print server session key, Kc,ps, to the client. This session key is encrypted with the key Ktgs,c. The TGS also sends the client a ticket for the print server encrypted with a key known only to the print server. This communication is illustrated in [Figure 6-4](ch06.html#tgs_to_client_print_server_session_key_t).

To access the print server, the client sends the time-stamped authenticator, A, encoded with Kc,ps, to the print server. The client also transmits the ticket encoded with a key known only to the print server. The print server decodes the ticket and obtains Kc,ps, the client-print server session key. The print server then uses Kc,ps to communicate securely with the client. [Figure 6-5](ch06.html#client_to_print_server_service_exchange) shows this exchange.

![Client to TGS request for PS ticket](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0603.png)

**Figure 6.3. Client to TGS request for PS ticket**

![TGS to client print server session key transmission](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0604.png)

**Figure 6.4. TGS to client print server session key transmission**

![Client to print server service exchange](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0605.png)

**Figure 6.5. Client to print server service exchange**

The primary goal of Kerberos is to protect the confidentiality and integrity of information. Because of the exposure and vulnerability of the workstations and network cables, it does not directly address availability. Because all the secret keys of the clients and other network resources are stored at the KDS and TGS, these servers are vulnerable to attacks and are a potential single point of failure. Replay can be accomplished on Kerberos if the compromised tickets are used within an allotted time window. Also, because a client's password is used to initiate a Kerberos authentication exchange, Kerberos is vulnerable to guessing of passwords. Similarly, because a client's secret key is stored temporarily on the client workstation, the secret key is subject to possible compromise.

### SESAME

With the advent of public key cryptography, a common paradigm is to use a public key cryptosystem to securely transmit the secret keys to be used in symmetric key cryptosystems. This hybrid approach is used by another SSO implementation, the Secure European System for Applications in a Multivendor Environment (SESAME). SESAME uses the Needham-Schroeder public key authentication protocol and a trusted authentication server at each host to reduce the key management requirements. SESAME also incorporates two certificates or tickets that provide for authentication and access privileges. SESAME is also subject to password guessing.

### KryptoKnight

As with Kerberos, the IBM KryptoKnight SSO system uses a trusted KDC that stores the network users' secret key. One of the differences between Kerberos and KryptoKnight is that there is a peer-to-peer relationship among the parties and the KDC in KryptoKnight. To implement SSO, there is an initial exchange from the user to the KDC comprising the user's name and a value, which is a function of a *nonce* (a randomly generated, one-time use authenticator) and the password. The KDC authenticates the user and sends the user a ticket encrypted with the user's secret key. The user decrypts this ticket and can use it for authentication to obtain services from other servers on the system.

# Databases

Another access control means is the application of database technology to screen the information available to a variety of users. In particular, the relational model developed by E. F. Codd is useful in network security applications.

## Relational databases

A relational database model comprises data structures in the form of tables and relations, integrity rules on allowable values in the tables, and operators on the data in the tables. A *database* can formally be defined as a persistent collection of interrelated data items. Persistency is obtained through the preservation of integrity and through the use of nonvolatile storage media. The following terms describe some of the different database attributes:

- **Schema**— The description of the database.
- **Data Description Language (DDL)**— Defines the schema.
- **Database management system (DBMS)**— The software that maintains and provides access to the database. Relative to access control, a particular user can be restricted to certain information in the database and will not be allowed to view any other information.
- **Relation**— A two-dimensional table that serves as the basis of a relational database. The rows of the table represent *records* or *tuples*, and the columns of the table represent the *attributes*.
- **Cardinality**— The number of rows in the relation.
- **Degree**— The number of columns in the relation.
- **Domain**— The set of allowable values that an attribute can take in a relation.

In a relation, a unique identifier or *primary key* unambiguously points to an individual tuple or record in the table. If an attribute in one relation has values matching the primary key in another relation, this attribute is called a *foreign key*. A foreign key does not have to be the primary key of its containing relation.

### Example relational database operations

A number of operations in relational algebra are used to build relations and operate on the data. The following items are examples of relational database operations:

- **Select**— Defines a new relation based on a formula
- **Union**— Forms a new relation from two other relations
- **Join**— Selects tuples that have equal numbers for some attributes

An important database operation related to controlling the access of database information is the *View*. A View does not exist in a physical form, and it can be considered a virtual table that is derived from other tables. (A relation that actually exists in the database is called a *base relation*.) These other tables could be tables that exist within the database or previously defined Views. Views can be used to restrict access to certain information within the database, to hide attributes, and to implement content-dependent access restrictions. So, an individual requesting access to information within a database will be presented with a View containing the information that the person is allowed to see. The View hides the information that individual is not allowed to see. In this way, the View can be thought of as implementing Least Privilege.

In statistical database queries, a protection mechanism used to limit inferencing of information is the specification of a minimum query set size, but prohibiting the querying of all but one of the records in the database. This control thwarts an attack of gathering statistics on a query set size M, equal to or greater than the minimum query set size, and then requesting the same statistics on a query set size of M + 1. The second query set would be designed to include the individual whose information is being sought surreptitiously. When querying a database for statistical information, individually identifiable information should be protected. Requiring a minimum size for the query set (greater than one) offers protection against gathering information on one individual.

### Data Normalization

*Normalization* is an important part of database design that ensures that attributes in a table depend only on the primary key. This process makes it easier to maintain data and to have consistent reports. Normalizing data in the database consists of three steps:

- Eliminating any repeating groups by putting them into separate tables
- Eliminating redundant data (occurring in more than one table)
- Eliminating attributes in a table that are not dependent on the primary key of that table

## Other Database Types

Relational databases have been extensively researched for network security applications and are well suited to textual applications. Other database types are useful for multimedia and textual, multimedia, or security applications. Two of these types are summarized in the following sections.

### Object-oriented databases

*Object-oriented databases* (OODB) are useful in applications involving multimedia, computer-aided design, video, graphics, and expert systems. An OODB has the following positive and negative characteristics:

- Ease of reusing code and analysis
- No restrictions on the types or sizes of data elements, as is the case with relational databases
- Reduced maintenance
- Easier transition from analysis of the problem to design and implementation
- A steep learning curve
- A high overhead of hardware and software required for development and operation

### Object-relational Databases

The *object-relational database* combines the features of object-oriented and relational databases. The object-relational model was introduced in 1992 with the release of the UniSQL/X unified relational and object-oriented database system. Hewlett Packard then released OpenODB (later called Odapter), which extended its AllBase relational Database Management System.

# Remote Access

Authentication, authorization, and accounting are important requirements during a remote access session. A number of services and protocols are used to provide these capabilities. These services and protocols are discussed in the following sections.

## RADIUS

A central authentication service for dial-up users is the standard Remote Authentication and Dial-In User Service (RADIUS). RADIUS incorporates an authentication server and dynamic passwords. The RADIUS protocol is an open, lightweight, UDP-based protocol that can be modified to work with a variety of security systems. It provides authentication, authorization, and accounting services to routers, modem servers, and wireless applications. RADIUS is described in RFC 2865.

Radius comprises the following three principal components:

- **A network access server (NAS)**— Processes connection requests and initiates an access exchange with the user through protocols such as the Point-to-Point Protocol (PPP) or the Serial Line Internet Protocol (SLIP). This activity produces the username, password, NAS device identifier, and so on. The NAS sends this information to the RADIUS server for authentication. The user password is protected by encryption in protocols such as the Password Authentication Protocol (PAP) or the Challenge Handshake Authentication Protocol (CHAP).
- **Access client**— A device (router) or individual dialing into an ISP network to connect to the Internet.
- **The RADIUS server**— Compares the NAS information with data in a trusted database to provide authentication and authorization services. The NAS also provides accounting information to the RADIUS server for documentation purposes.

## TACACS and TACACS+

Terminal Access Controller Access Control System (TACACS) is an authentication protocol that provides remote access authentication and related services, such as event logging. In a TACACS system, user passwords are administered in a central database rather than in individual routers, which provides an easily scalable network security solution. A TACACS-enabled network device prompts the remote user for a username and static password, and then the TACACS-enabled device queries a TACACS server to verify that password. TACACS does not support prompting for a password change or for the use of dynamic password tokens. TACACS has been superseded by TACACS+, which provides for dynamic passwords, two-factor authentication, and improved audit functions.

TACACS+ comprises the following elements, which are similar to those of RADIUS:

- **Access client**— A person or device, such as a router, that dials in to an ISP.
- **A network access server (NAS)**— A server that processes requests for connections. The NAS conducts access control exchanges with the client, obtaining information such as password, username, and NAS port number. Then, this data is transmitted to the TACACS+ server for authentication.
- **The TACACS+ server**— A server that authenticates the access request and authorizes services. It also receives accounting and documentation information from the NAS.

## Password Authentication Protocol

Another authentication mechanism is the *Password Authentication Protocol* (PAP). In PAP, a user provides an unencrypted username and password, which are compared with the corresponding information in a database of authorized users. Because the username and password are usually sent in the clear, this method is not secure and is vulnerable to an attacker who intercepts this information. PAP is described in RFC 1334.

In operation, after a communication link is established between the remote user and PAP, a user ID and password are transmitted repeatedly until authentication is completed or the communication is terminated.

PAP is vulnerable to ID and password guessing and to replay attacks.

An improved approach is the Challenge Handshake Authentication Protocol.

## Challenge Handshake Authentication Protocol

The *Challenge Handshake Authentication Protocol* (CHAP), described in RFC 1994, provides authentication after the establishment of the initial communication link between the user and CHAP. CHAP operation comprises a three-way handshaking procedure summarized in the following steps:

1. The CHAP authentication mechanism sends a "challenge" to the user following the establishment of the communication link.
2. The user responds to the challenge with a string produced by a one-way hash function.
3. The hash value transmitted by the user is compared with a hash result calculated by the authentication mechanism. If the two hash values are identical, authentication of the user is verified. If the values do not match, the connection is terminated.
4. For increased security, Steps 1 through 3 are repeated at random time periods. This procedure provides protection against replay attacks.

# Summary

Access controls are crucial in protecting the network and its associated resources. In establishing an access control architecture, it is useful to limit the number of areas of administration. SSO environments, such as Kerberos and SESAME, support this concept. Mandatory access control paradigms are particularly useful in protecting information and preventing major compromises of intellectual property.

Databases are another important tool in providing access controls and implementing the concept of least privilege through database Views. Remote access systems and protocols, such as RADIUS and CHAP, provide secure means for authenticating those seeking access through the use of dynamic passwords and challenge-response procedures.
