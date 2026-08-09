# Securing devices and the edge to the cloud gateway

Devices on the edge are typically located some distance from the backend data center and require unique physical, software-related, and data-security precautions. The data the devices gather is sometimes transmitted to other devices or is transmitted directly to cloud gateways or via field gateways onto the cloud.

In the following diagram, the shaded area indicates the components and networks that we will discuss securing in this section of the chapter:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/2ae6515a-68cb-4bd7-8438-473b05fe77cb.png)

Figure 8.3: Device to cloud security Connections and routes are established when peering occurs between the devices and the gateways. Secure devices never accept unsolicited network connections. They might be peered directly with cloud gateways or first with field gateways that are then peered with cloud gateways. Transmissions are secured at the transport and application-level protocol layers and authenticated to the services or gateways that they are connected to.
