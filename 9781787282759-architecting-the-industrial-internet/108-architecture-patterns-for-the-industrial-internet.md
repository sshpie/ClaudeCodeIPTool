# Architecture patterns for the Industrial Internet

A carefully selected architecture pattern represents an easy way to understand the abstraction of the IIoT implementation scenario. It allows reuse of best practices, alongside the flexibility to experiment with variations, within reason. We will look at the commonly used three-tier architecture pattern here. The three tiers are typically as follows:

- Edge tier
- Platform tier
- Enterprise tier

The edge tier is mainly used to gather the sensor and machine data from the edge nodes. It uses the localized or the proximity network. The architectural features of the edge network include the nature of the localized or proximity network. The distribution and the location of the devices are other considerations at this stage. Deciding whether all the data collected is forwarded to the platform tier or data aggregation or processing is needed may help design this edge tier and its processing and storage capabilities.

The platform tier can be in a private data center or in the private cloud. This tier receives the data, and ingests and organizes it before storing it in the appropriate data store. This tier may also be used to send the control commands from the enterprise tier to edge tier. The platform tier may aggregate, process, or analyze the data flows from the edge tier. Optionally, it may provide edge management capabilities for the devices and other similar assets in the edge. Often, querying and reporting on the data and the different kinds of analytics takes place in this tier.

The enterprise tier carries out industry domain-specific business applications and related decision support systems. This tier provides interfaces to the business end users, operators such as field service technicians, or the monitoring and diagnostics center operation specialists. The enterprise tier may often receive the data flows from the edge and platform tier. This tier could also originate the control commands to the platform tier and the edge tier.

In a general case, an implementation of the three-tier pattern in an Industrial Internet system will not prevent multiple implementations in each of the tiers. An example could be many instances of the edge tier due to different categories of the edge devices being connected to the platform tier in a heterogeneous solution. Even in such scenarios, the architecture pattern definition will represent each tier only once in each tier.

After looking at the architecture patterns for Industrial Internet, we will look at considerations for the building and implementation of software solutions. In the world of enterprise software, ERP, CRM, and **Human Capital Management** (**HCM**) applications are mature and are often referred to as packaged software. Common examples of ERP include Oracle EBS or Cloud ERP and SAP R/3 or business applications. The CRM world has seen Salesforce.com and Siebel CRM, which was acquired by Oracle. In the arena of HRM, PeopleSoft and Workday are common examples. The corresponding applications are emerging in the Industrial Internet area. One of the common application families today is **Asset Performance Management** (**APM**).
