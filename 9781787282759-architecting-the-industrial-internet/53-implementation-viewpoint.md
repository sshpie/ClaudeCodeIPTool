# Implementation viewpoint

The implementation viewpoint is the manifestation of each of the previous viewpoints. The business viewpoint ultimately drives the selection of technologies, with considerations for costs, time constraints, business strategy, regulation, and the vision for the future.

The implementation viewpoint describes the ultimate structure and distribution of the system components and how they are connected. The required interfaces, protocols, and behaviors are defined. Functional components defined in the usage viewpoint are mapped to implementation components.

IIoT implementations typically follow established architectural patterns, including the following:

- Three-tier architecture
- Gateway-mediated Edge connectivity
- Edge-to-cloud
- Multi-tier data storage
- Distributed analytics

Three-tier architecture consists of Edge, Platform, and Enterprise tiers. The functional domain determines the component requirements of the three-tier architecture, and the components generally map to the functional domains, or viewpoint, as in *Figure 2.9, Three-tier architecture*:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/36bdbce5-5d6d-4440-b097-cae933608079.png)

  Figure 2.9:  Three-tier architectureEach tier has a specific role corresponding to the usage viewpoint, and they are connected via three separate networks:

- The **Edge Tier** collects data from the edge nodes across the proximity network. Device-specific processing and control may occur in the **Edge Tier**, depending on the application.
- The **Platform Tier** receives and processes data from the enterprise tier to the edge tier, via a service network, and from the platform tier, via an access network. The platform tier performs management functions for the devices, and the detail and consolidated data can by queried or transformed for further analysis.
- The **Enterprise Tier** receives the data and integrates it with data from other systems, to perform analysis across business silos. The enterprise tier may also execute control commands on the edge or platform tier.

The functions depicted in *Figure 2.9* indicate the primary function of the tier, but are not exclusive to that tier. The same functions are implemented in each tier according to the usage within the tier level.

The tiers are connected by different types of network as follows:

- The proximity network connects sensors, devices, assets, control systems, and other components in the edge nodes. The edge nodes are typically grouped into clusters and bridge to a wide area network via the edge gateway or hub.
- The access network connects the edge- and platform-tier and enables data and control flows between them. This could be a corporate network, a 4G/5G network, or a private network on the public internet.
- The services in the platform tier connect to each other and to the enterprise tier via a service network. This can be a private network over the public internet (or the internet), and enables enterprise grade security between the end user and the services.

The three-tier architecture maps the components to the functional viewpoint (*Figure 2.10*). The edge tier encompasses the control domain, and the platform tier contains aspects of the information and operations domains. The information tiers provide services to each other in support of the functional domain, completing the end-to-end activities:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/7e3f5fc7-e472-4760-8cc1-4529fb050e09.png)

Figure 2.10:  Three-tier architecture mapping to the functional viewpointGateway-mediated edge connectivity and management defines the bridge between the edge nodes and a wider network, where the wide area network cannot access the edge nodes directly. An edge gateway in the edge node can perform local operations and controls. It may also be used to manage devices and serve as a conduit for aggregated data. This localization of control both reduces the complexity and enables the scaling up of assets and the network. Devices can be managed, and data can be aggregated by the edge gateway, thus enabling local control:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/70a42b1d-fc4e-4eba-9efd-179e8ff6c8bf.png)

Figure 2.11:  Gateway-mediated architecture patternThe local networks may follow the hub-and-spoke topology, where the edge gateway acts as the hub for a cluster of edge nodes and to the wide area network, and the hub connects directly to each edge node. A mesh, or peer-to-peer network, follows the *hub-and-spoke* topology, but some edge nodes have routing paths to other edge nodes or the edge gateway. In both topologies, the edge nodes are isolated from the wide area network and are only accessible through the edge gateway.

The edge gateway supports the following:

- Local connectivity
- Network and protocol bridging
- Local data processing
- Device and asset control and a management point
- Site-specific decision and application logic

The Layered Databus architecture pattern is commonly used in IIoT systems, as it enables systems to directly manage interactions between remote applications, including control and edge analytics. Peer-to-peer communications across the systems layer can be secured, and the inherent low latency minimizes delays between the transmission and receipt of data, as illustrated in the following architecture of Layered Databus:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/11086111-e305-4626-8d62-63347a932ed5.png)

Figure 2.12: Layered Databus architectureLow-level systems in this architecture pattern provide the local control and automation for smart machines, using databuses. Databuses are used in the higher level systems for monitoring and supervisory control.

A databus uses a common schema to communicate between endpoints. Each layer of the architecture employs its own databus, employing a schema specific to the endpoints in that layer. Adapters cross-match the data models between layers and can also be used as an interface for legacy systems or components using different protocols. This architecture facilitates operational monitoring, device management, provisioning, as well as applications and subsystems.

As data is collected at the lowest levels for local control, it is generally filtered and summarized for higher level systems that control a broader set of functions. A publish-subscribe model is used for communication of data and information, wherein applications on the databus publish their data output, and the consuming applications on the databus subscribe to the data they need. With the publish-subscribe model, components can share large volumes of data quickly.

Benefits of the layered database architecture include the following:

- Extremely fast delivery times for device-to-device integrations
- Scalability for integrating thousands of end points and actuators
- Automatic discovery of data and applications
- Extreme availability
- Isolation of subsystems

Additional architectural patterns include the following:

- Edge to cloud follows the gateway-mediated edge connectivity pattern; however, it is assumed that the wide area network can access the devices.
- Multi-tier data storage involves multiple types of storage tiers, with older data in a slower or less accessible archive tier, more current data in a capacity tier, and data needed for rapid operational decisions in a performance tier.
- Distributed analytics brings analysis and decision-making to the edge tier close to the devices. This creates additional challenges for the security of the devices as well as the data traffic.
