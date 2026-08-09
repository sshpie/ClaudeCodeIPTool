# A supply chain optimization information domain

Our list of required functions in our example includes the following:

- This information domain could introduce a need for many skills that are not present in the company's IT organization. We'll need to assess the skills present and begin developing strategies to address those gaps. Typical options considered include skills development through training, hiring consultants to initially provide support, or leveraging the managed services offered by public cloud providers.
- Data will be ingested from sensors located throughout the manufacturing facilities and in transportation vehicles, and we will be gathering production, location, and temperature data every minute with transmission volume expected to reach 100,000 messages per hour.
- Some data cleanup will be needed prior to storage and analysis due to incomplete or corrupted transmissions that will occur.
- The equipment in the manufacturing plants is of various ages and from different vendors, so rationalization of inconsistent data formats will be necessary.
- The streaming nature of a significant amount of incoming data and the history we will need for more accurate analysis will influence our data management strategy toward inclusion of a Hadoop engine. We expect tens of terabytes of data to be gathered here, growing into the hundreds.
- As structured data from several existing systems in the business domain will be required as part of the analysis and there is already a data warehouse in place, we will include that in our design.
- Given data will exist in multiple locations. We'll create a data catalog to help business analysts find the data and understand its meaning.
- Alerting is needed if temperature extremes occur or there are anomalies in production that could cause safety concerns driving a requirement for streaming analytics to be part of the solution.
- We will be proactive in protecting our data and require procedures and careful monitoring of data access and encryption of all data.
- Because this system will be so critical to factory operations, we will include plans for high availability and disaster recovery in all key information domain components.
