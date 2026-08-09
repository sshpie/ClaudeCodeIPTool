# Mapping analytics architecture to reference architecture

Industrial analytics can span the functional domains we previously described in [Chapter 4](c15efc6c-ceb2-4fcf-ba6b-21343a317dbb.xhtml), *Mapping Requirements to a Functional Viewpoint*. As a review, the domains in IIoT functional architecture include the following:

- **Control domain**: It provides functions for asset management, sensing, actuation, communication, entity abstraction, and modeling
- **Operations domain**: It enables provisioning, management, monitoring, diagnostics, and optimization of devices in the control domain
- **Information domain**: It consists of data ingestion, quality and cleansing, transformation, persistence, cataloging, analytics, and governance
- **Application domain**: It includes logic, rules, models and interfaces addressing business requirements
- **Business domain**: It includes enterprise resource planning, human resources, asset management, billing and payments, work planning and scheduling, and customer relationship applications

The following diagram illustrates these domains and where the analytics are primarily applied:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/8949bdf7-b721-40fc-880e-4324268e61c6.png)

Analytics in the control domain consists of edge analytics that provides real-time insight into operations. Here, the device time horizon can be milliseconds or less. Analytics and resulting actuation that occurs in the control domain is usually automated.

Analytics applied in the application and operations domains requires responses measured in seconds, and these responses are also usually automated. Such responses based on results from streaming analytics might include automatic fault detection and diagnosis, or automated adjustments to improve efficiency.

Analytics relevant to the business domain can aid in business planning, improve processes, and enable intelligent business processes. These analytics are typically used for planning, and the required response time to make a business decision can be measured in days. Batch analytics is more typically applied here.
