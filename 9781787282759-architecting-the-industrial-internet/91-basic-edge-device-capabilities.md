# Basic edge device capabilities

Not all edge devices that could be considered will align with our deployment strategy. We will need to specify viable devices consistent with our business goals, the functionality we need, and the rest of our architecture.

The control domain and the edge devices must be managed. Asset management functionality is needed for the on-boarding of devices, configuration of devices, setting policies, and deployment of system software and firmware updates to devices. The control domain receives direction from the operations domain (we'll cover the operations domain in the next section).

We need to assess the placement of sensors in our devices and the metrics the sensors can gather. These metrics must align with the data we need populated in our backend infrastructure, that will be used by the business community in making decisions.

Sometimes, our smart devices need to take immediate action (termed as providing actuation) as data is still being processed within the edge devices. These actions are typically critical tasks that would cause damage and safety concerns, or impact production or yield, if not immediately corrected.

Data is transferred from the edge devices to the backend infrastructure for analysis of many devices at scale over lengthy periods of time. The edge devices are directly attached or networked to field gateways that then use messaging protocols to send data to the backend infrastructure. Examples of typical messaging protocols include the following:

- **Advanced Message Queuing Protocol** (**AMQP**)
- **Message Queue Telemetry Transport** (**MQTT**)
- AMQP or MQTT over web sockets
- **HyperText Transfer Protocol** (**HTTP**)
- Custom protocols

Some field gateways can communicate using a choice of multiple messaging protocols. Others are limited to a single protocol. You will need to decide the protocol to be used prior to selecting the edge devices and field gateways. This is often driven by the protocol(s) that your backend infrastructure is set up to support. If you are going to deploy your backend infrastructure in a public cloud, the public cloud provider can provide you with a list of available protocols that they or their partners support for IIoT projects.

Communication is typically bi-directional (**device to cloud** (**D2C**) and **cloud to device** (**C2D**) when the backend infrastructure is in the cloud). The messaging that must occur at scale includes data transfer, requests for data transfer and replies, and device management. For example, the sending of messages to the cloud can trigger delivery receipts, expired message notifications, and device communication error messages. Understanding message volume and transfer rates is extremely important when evaluating functionality required in this domain.

In addition to selecting field gateways based on protocols, you'll need to look at other features of the gateways. These can include the networking and device connection options that they offer, environmental operating characteristics (such as the recommended temperature and humidity range), power requirements, and their processing power, memory, and storage specifications. The gateways should buffer data when the network is down and support data transmission retries. They are also evaluated on their ability to batch messages and support connection multiplexing for better messaging volume scalability.
