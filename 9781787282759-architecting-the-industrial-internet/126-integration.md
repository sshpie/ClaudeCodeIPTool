# Integration

The components and applications in an IIoT solution produce varied data specific to their respective functions. This data was traditionally retained in their respective silos in field locations. To achieve a more thorough understanding of the business, data integration across these silos is required. For example, in telecom companies, revenue leakage occurs when calling services are provided, but these billable calls are not passed on to the billing system. Integrating network usage data, linked to devices with the billing systems, can uncover these unbilled calls.

Traditional systems use a process of **extraction, transformation, and loading** (**ETL**) to extract data from one or more source systems, integrate and transform the data, and load the resulting data into a target system. This transformation frequently includes performing aggregation or other functions to enable analysis. Where large data volumes are at play, the processing often more closely follows an ELT pattern where transformations occur in the target.

In IIoT systems, heterogeneous devices can have different syntax, semantics, and APIs. A transformation to a common semantic framework is often necessary for effective analysis. Domain transformation might be used for protocol conversions.

IIoT integration challenges can be addressed by taking the following steps:

- Address the APIs first to determine the integration requirements and if your existing integration capabilities are sufficient
- Identify the communication requirements for the devices and select the most appropriate technology, taking into consideration how the technology can handle the number and types of devices, while determining the network topology that best meets the requirements
- Leverage cloud-based deployment models to integrate IIoT platforms with business processes
- If the IIoT system data and applications are on-premises, or mostly on-premises, you might consider using traditional integration tools already in-house, but keep in mind that these tools might not be optimal for IIoT connectivity or cloud service integration
- Add an API management solution to your IIoT project, especially if the project has many APIs, or the APIs have large numbers of consumers or return restricted or sensitive data
