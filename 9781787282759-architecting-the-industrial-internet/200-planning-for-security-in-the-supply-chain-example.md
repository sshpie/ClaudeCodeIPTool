# Planning for security in the supply chain example

You will recall from the generic supply chain example and the CEMENTruck Inc. example that data is captured from sensors on equipment in the plants and from vehicles in transit. This data is transmitted to cloud-based backend systems for real-time streaming analytics processing and for batch processing in a data lake and data warehouse infrastructure.

The following diagram represents such a scenario:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/5dc3fe2e-b822-4b5c-b84e-57b0979f707a.png)

Figure 8.7: IIoT End-to-End SecurityTo ensure a secure infrastructure, we will need to put in place many of the security measures that we previously discussed in this chapter in the devices and vehicles, across the networks, and in the backend engines. We'll also need to be able to assess the ability of our infrastructure to prevent compromised security proactively and detect and respond to security threats on an ongoing basis.

In the preceding diagram, we noted that device-to-device communications use CoAP and DTLS for secure WSN transmissions. Devices can be monitored by our operations personnel using mobile phones connected via NFC. At our field gateway in the plants, we are converting the protocol for transmission to MQTTS and using a private network to connect to the cloud for data transmissions. From the vehicles, we are transmitting using HTTPS over a VPN connection into the cloud to its virtual networks there.

In completing the design and planning for securing our IIoT architecture in the supply chain example, we would also focus on the following:

- Minimize any device and sensor vulnerability and data loss
- Perform secure firmware and software patching and updates to devices and sensors
- Manage gateway and firewall security
- Assure network resiliency (in addition to authenticating and authorizing data transfer and assuring data privacy through methods noted in the preceding diagram)
- Securely manage network changes and traffic
- Ensure data privacy, validity, and security in backend systems

For example, we might specify using OMA LW2M2M to manage the devices. We could specify larger gateway sizes and procedures to ensure that no data loss occurs if network connections are lost. We could begin to define procedures and tools to be used in the administration of the pictured backend data-management systems.
