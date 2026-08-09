# Topology

Local network topologies in IIoT systems include the following:

- **Point-to-point**: The network connects only two hosts, or devices, or network nodes, and communication only takes place between the two nodes, or devices, such as a Bluetooth link to a wireless device.
- **Hub-and-spoke**: An edge gateway provides a hub to connect clusters of edge nodes to each other and to the wide area network. This topology can quickly run out of capacity. Upgrading requires shutting down the hub, which in turn brings down the spoke sites.
- **Meshed (peer-to-peer)**: This is like hub-and-spoke, but some edge nodes have routing capability and must capture or transmit data, and serve as relays for other nodes. This topology is well suited for the broad area coverage of low-power, low data rate applications on resource-constrained and geographically distributed devices. Meshed networks are more complex than point-to-point or hub-and-spoke, and have higher network latency.

Advantages of meshed network topology are as follows:

- **Parallel communications**: Data can be transmitted simultaneously from different devices, enabling high-traffic communications
- **Reliability**: Other components are available in the event a component fails
- **Scalability and flexibility**: Changes and additions to the topology can be done without disrupting other nodes

Multiple networks and topologies can by bridged using connectivity gateways. The transport may require or exclude a network topology, but should not restrict it.
