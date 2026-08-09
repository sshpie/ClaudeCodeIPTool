# The evolution of networking

Qualcomm ([https://www.qualcomm.com/news/onq/2017/05/16/private-lte-networks-industrial-iot-how-spectrum-sharing-will-expand-lte](https://www.qualcomm.com/news/onq/2017/05/16/private-lte-networks-industrial-iot-how-spectrum-sharing-will-expand-lte)) has been one of the pioneers in highlighting the emergence of private **Long-Term Evolution** (**LTE**) networks for Industrial Internet infrastructure and applications. The fifth-generation mobile networks or fifth-generation wireless systems, abbreviated as 5G, are the next proposed telecommunications standards beyond the current 4G standard. Carriers in the United States are targeting 2020 for widespread deployment of 5G technology. Marc Tracey, a Verizon spokesman, said, "*Basically, 5G will provide a wider pipeline and faster lanes"* for data-rich applications as such as IoT. However, until 5G becomes mainstream technology over the next few years, private LTE networks can help speed up the realization of benefits for Industrial Internet applications.

The following illustration shows some of the industries that can benefit from private LTE networks, according to *Harbor Research* (February 2017):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/c114aadd-f67d-42b7-b3aa-c2e7ccd72ae0.jpg)

The concept of private LTE networks implies that the enterprise customers run their own local network with dedicated equipment and settings, rather than relying on the carrier. The key characteristics of the private LTE networks are as follows:

- **Rapid deployment**: Due to the availability of shared and unlicensed spectrum, deployment of private LTE network can be done easily today
- **Local control**: This refers to the use of local deployment equipment at the enterprise customer's site; it is relatively immune to traffic surges and provides better and reliable performance
- **Optimization**: It can be optimized for the specific IoT applications by controlling the **Quality of Service** (**QoS**) and other network settings

As this book was being published, **Low Power wireless Wide Area Networks** (**LPWANs**) were being explored as an alternative in many organizations. LPWAN is designed for long-range communications at low bit rates and is ideal for sensors operating on battery power. Battery life can be extended to provide power for over 10 years or more. A variety of LPWAN protocols were undergoing development and beginning to establish themselves in 2017, including **LTE advanced for Machine Type Communications** (**LTE-MTC**), Haystack Technologies, LoRaWAN, Symphony Link, and **Ultra Narrow Band** (**UNB**). Given these technologies were in early adoption and many were initially considered proprietary, it was expected that it would require a few years to determine which would gain widespread adoption and become broad standards.

Recently, the **Open Platform Communications Unified Architecture** (**OPC UA**) has gained increased adoption for IEEE 802.1 based networks. OPC UA replaces an early OPC protocol that was Windows-based and relied on COM/DCOM as a communications model. The OPC UA architecture is built on **Time Sensitive Networking** (**TSN**), an extension of the IEEE 802.1 standard that enables network devices such as **programmable automation controllers** (**PACs**) to operate according to synchronized clocks. The following diagram illustrates this stack:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/0d608d97-9b3d-4508-bc75-62781e1c62d3.png)

Authentication over OPC UA is via X.509 certificates and provides better security than the original OPC stack. APIs are available for multiple programming languages.

An indication of the growing popularity of OPC UA is its adoption by multiple device manufacturers. For example, GE Energy utilizes OPC UA for transmitting weather data to real-time controls in some of its devices. Given the frequent changes in what is popular, most device manufacturers usually provide adapters for previous commonly used protocols as well.

Networking layers are sometimes simply represented in just three layers consisting of an applications layer, a controls layer, and an infrastructure or hardware layer. We'll use the following diagram to introduce two abstraction levels, SDN and NFV, that are growing in popularity and are pictured between the three layers as shown here:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/c37dd1e4-b02a-4e4a-b60e-e13655a6184a.png)

**Software-Defined Networking** (**SDN**) gained widespread data center adoption, especially among CSPs, in the past decade. It enables network management and control that is not tightly bound to underlying hardware and networks with centrally defined control policies for physical and virtual networks. SDN was expected to continue to move beyond data centers into wired and wireless networks, enabling programmability and automation across all networks in an IIoT architecture. Indeed, SD-WANs were growing in acceptance as a deployment strategy in IIoT architecture footprints as this book was being written.

**Network Functions Virtualization** (**NFV**) provides a layer of abstraction between the network applications and controls layer. Network functions (applications) are decoupled from hardware devices and under the control of a hypervisor. Network services previously provided by dedicated hardware devices such as routers, firewalls, and load balancers can instead be deployed using commodity servers. Many of the providers of dedicated hardware solutions have transitioned their software to supporting generic servers. Given that most public clouds are also built on massive numbers of generic servers, these configurations are particularly popular among CSPs.

Either of these abstraction layers can be deployed independently of each other. Since they reside between different layers of the stack, they can also be deployed in combination with each other.
