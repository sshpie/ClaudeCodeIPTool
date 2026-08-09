# The speed layer and field gateways

Earlier in this chapter, we pictured a speed layer in our architecture consisting of an IoT hub and/or event hub(s) serving as a cloud gateway and a streaming analytics engine. A cloud gateway is paired with a field gateway at the edge, or the cloud gateway will sometimes communicate directly with the smart devices themselves.

Some organizations deploy the speed layer on-premises instead of in the cloud to be located close to their existing batch layer systems. If transmission of data occurs to a central on-premises location, the gateway architecture would be similar, except an on-premises gateway would be pictured in our earlier diagram instead of the cloud gateway. This is especially common in organizations that built Industrial Internet solutions prior to public clouds gaining in popularity and the functionality required for these types of solutions.

Field gateways gather event data at the edge from smart devices and sensors. They are usually sized based on the number of data streams that will occur, the data collection rate (events/second), and the data storage duration desired. These gateways might be custom developed or provided by vendors. OSIsoft and ThingWorx are two such popular vendors deployed as part of many custom-built solutions.

Field gateways ingest messages, filter data, provide identity mapping, and log messages (for auditing purposes) as well as provide linkage to cloud or on-premises gateways. A newer trend has emerged to also perform stream analytics and machine learning within the field gateways. The ability to push these applications to the edge is now provided by some of the public cloud vendors. In a sense, this extends the speed layer to the edge. When these capabilities are deployed at the edge, you will need to consider CPU and memory sizing implications when sizing the field gateway platforms.

Within the speed layer that is deployed in a central location, the packaging of components varies among vendors. Among various public cloud vendors focused on IIoT solutions, the following functionality can be found in their offerings and/or those of their partners:

- IoT hubs that enable **device to cloud** (**D2C**) via messaging protocols and **cloud to device** (**C2D**) communications contain information about the smart devices, support revocable access control for devices, enable operations modeling, and support message routing to event hubs or service buses
- Event hubs without the management capabilities of the IoT hub, but specifically designed for just handling rapid message ingress with data transfer rates of up to 1 MB/second typical in cloud deployment
- Streaming analytics engines providing a place to analyze data in motion with using machine learning algorithms or to view the current streaming data through business intelligence tools.

Since we are focused on data and analytics in this chapter, we will pay special attention to how quickly we can transmit data in the speed layer. The hubs can be scaled as needed. Our goal is not to create any bottlenecks.

Message volume and hubs

 Most message volume comes from D2C transmissions of data from the devices. Of course, other volume is generated through file transmission, device identity management, job management, connectivity monitoring, and other tasks. Some of this data is transmitted C2D.The hubs are not meant to be locations where data is stored for significant periods of time. Usually, a maximum of 24 hours of data records being stored is recommended, though it is possible to extend the length of time that data records are stored. The batch layer is the proper location for storing longer histories.

The streaming analytics engine enables real-time analysis of data that is being transmitted from the sensors and smart devices. Typical average data rates today are about 50 MB/second. As mentioned earlier, data can be directly queried from business intelligence tools. Data might also be queried using SQL, or machine learning scripts might be applied on an ongoing basis.

Data is typically then loaded into a batch layer data-management system (data lake, NoSQL database, or relational database). Immediate actions might be initiated after the analysis of incoming data, so scripts might be pushed upstream via event hubs or service bus queues.

In our supply chain optimization example introduced earlier, three critical success factors were identified:

- Operating factories at maximum capacity (24x7)
- Delivery of all needed components (parts) to factories just-in-time
- Maximized revenue from production by meeting product demand

The speed layer serves several purposes in this example. It provides the point of ingestion for data gathered from factories and transportation vehicles and transmitted by smart devices through field gateways at the edge. The streaming analytics engine analyzes the real-time flow of data and might initiate some of the following actions:

- Slow production rates if critical supplies are delayed
- Seek alternate delivery routes if supplies in transit are delayed
- Reroute transportation vehicles to alternate distribution centers if supplies are predicted to become critically low and the current distribution center is unable to fulfill demand for parts
- Initiate reordering of supplies if damage to components in transit is believed to be occurring (gathered by observing unusual temperature readings or vibration levels)
- Send alerts to supply chain and factory managers and finance if production disruption is likely due to supply chain issues
