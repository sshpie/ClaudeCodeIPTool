# Multi-tenancy

Multi-tenant architecture consists of a single instance of software that is accessed by multiple tenants. Tenants are groups of users (from a subscribing organization) who share access rights and privileges to the software instance. In multi-tenancy, the business logic is shared by many subscribers, but the data privacy is preserved for each tenant. The hosting provider is responsible for ensuring their subscribers can only access their own data and not that of other subscribers.

Advantages of multi-tenancy are as follows:

- **Operational**: Like hosted systems, the provider maintains, updates, and backs up the applications and data
- **Cost savings**: Since many customers share the application logic and storage capacity, there is no need for dedicated servers for each customer

Disadvantages of multi-tenancy are as follows:

- **Scalability**: As many customers share the computing resources, resources may become overloaded.
- **Homogeneity and competitive advantage**: You’re relying on the same code base as all the other tenants. Customization capabilities are very limited and confined to some general configuration parameters.
- **Reduced control**: Updates to software may be deployed to your system without authorization. Bug fixes, enhancements, patches, and upgrades by the provider are performed on their schedule and prioritized according to the hosting providers' largest customers.
- **Security**: While hosting providers make every effort to maintain data privacy and security, the sharing of computing and storage resources increases the risk of another user accidentally or purposefully accessing your data compared to single-tenant systems.
