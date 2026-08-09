# Data warehouse security

Data warehouses and data marts have been deployed on relational database-management systems for decades. They feature extremely mature capabilities for assuring secure access and security of data in the architecture.

Relational databases are provisioned by users with operating system administrative roles. Once provisioned, relational databases are managed through the administrative tools they feature that are accessible to users that who defined administrator roles. Administrators can assign usernames, tie users to groups and roles, and define user privileges. Basic user authentication is through a combination of usernames and passwords with identification management typically through LDAP or Active Directory. Many relational databases also support Kerberos for additional authentication.

Relational databases typically feature audit logs where data containing usernames, session identifiers, physical user device information, schema objects accessed, operations performed or attempted, and data and time of operations are collected. During auditing activities, this data can be used to report privileged user access, data access, account management activities, and failed login attempts.

Administrative users and roles and relational databases

 While most relational databases have an all-powerful administrator user and role, in large-scale deployment, various administrative roles might be divided among a team of users to balance their workload but also to enforce security policies in the organization.Advanced database features can include support for virtual private databases, label security, and data redaction. A virtual private database implementation uses fine-grained access control, and appropriate rows of data are accessible to a user based on their role in an organization (for example, they might have access to details about the customers that they manage, but they will lack such access to other customers). Label security matches appropriate roles to security levels granted (such as top secret, secret, and public). Data redaction obscures certain predefined data items (such as credit card numbers) that are returned in response to a query.

Many relational databases provide **transparent data encryption** (**TDE**) for data in the database and traversing network connections. Some cloud providers also provide encryption of data managed by these engines and the operating system on disk storage via **BitLocker** in Windows and the **DM-Crypt** feature in Linux.
