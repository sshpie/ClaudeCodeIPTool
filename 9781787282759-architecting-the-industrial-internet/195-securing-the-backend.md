# Securing the backend

We will now turn our attention to strategies for securing the backend components. The following diagram indicates the components we will consider, as shown in the shaded area:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/c969798c-bc9d-4752-b424-5d0659c3d0ec.png)

Figure 8.6: Backend SecurityThe streaming analytics engines provide a location to deploy applications, such as those that apply machine learning algorithms, on transient data. The security mechanisms for streaming analytics engines are less sophisticated today when compared to the data-management systems (such as the data lake, data warehouse, and data mart that are pictured). This is due, in part, to the limited requirements for administrative capabilities, but also due to streaming analytics engines being relatively new.

The primary means for assuring secure streaming analytics is through authentication using methods that can include using Kerberos, LDAP, or Active Directory. Authorization is generally tied to authorized logins for initiating applications. Once the credentials are verified and jobs are initiated on the streaming analytics engine, the credentials for the job typically can't be changed.

For the batch data-management systems, administrators usually manage security. The administrators can have many roles with privileges that must be well-protected, including the following:

- Installation and configuration of the data-management system
- Management of users, groups, and privileges
- Management, monitoring, and securing of data files (including backup and recovery and encryption policies)
- Monitoring of security and auditing
- Performance monitoring and tuning

The ISO/IEC 27001 Security Standard

 Though we will describe various certifications and standards related to governance in the next chapter, introducing this standard here is particularly relevant as it mandates how information must be secured under strict management control. The standard describes the implementation, monitoring, and maintenance requirements as well as best practices in documentation, responsibilities, availability, access control, security, auditing, and corrective and preventive measures that should be taken.Administrators and security specialists must focus on many possible undesirable exposures of the backend infrastructure. Among the areas they typically focus on and monitor are the following:

- Unauthorized SQL injections
- Broken authentication and session management
- Unsecure direct references
- Redirects and forwards that are not validated
- Security misconfiguration
- Sensitive data exposure
- Missing ACLs
- Components with known vulnerabilities

We will now take a deeper look at security considerations for the data-management systems.
