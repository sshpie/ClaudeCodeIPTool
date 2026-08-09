# Networking considerations

IIoT systems rely on data-sharing mechanisms between the things, the Internet, and industrial systems, and can encompass a multitude of connectivity technologies and standards. These technologies are often optimized for domain-specific use cases; however. IT networks were intended to support business applications, and to connect client or middleware to server (or server to server to) support business processes spanning organizational units. Networks do not generally embed technologies that generate data for the enterprise. OT networks were largely self-contained environments designed for factory and process automation. Prior to the IoT, the two networks were completely segregated. The challenge in IIoT is to develop a connectivity framework that enables data and communications sharing across the system to connect IT and OT, and realize the potential of IIoT.

IIoT systems require data to be exchanged among many endpoints in the system, with a growing trend toward including IT decision making in the industrial process. Big data analytics against large volumes of data collected across end points would be impractical to perform across the network and drive the requirement to perform analytics first against smaller datasets to reduce load on the network.

A connectivity function is needed to share data within and across functional domains within the system, and it provides interoperable communications among endpoints to enable component integration. It fulfils the functional requirements within each domain and cross-cutting function, and ensures that an endpoint can communicate with other endpoints via a gateway. Trade-offs need to be made between system, data, performance, scalability, availability, deployment, and operational considerations.

The IIoT connectivity stack model consists of the layers and protocols involved in connecting the physical model, or endpoints, to the information layer via a network layer and connectivity layer in which connectivity is a defined as a cross-cutting function.

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/b344d32d-1f5e-4f7d-9f39-ac88c8c79413.png)

Figure 7.7: Industrial Internet connectivity stack model
