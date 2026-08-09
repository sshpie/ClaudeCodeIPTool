# 6: Industrial Network Protocols

## Abstract

Understanding how industrial networks operate requires a basic understanding of the underlying communications protocols that are used, where they are used, and why. There are many highly specialized protocols used for industrial automation and control, most of which are designed for efficiency and reliability to support the economic and operational requirements of large industrial control system architectures. Industrial protocols are designed for real-time operation to support precision operations involving deterministic communication of both monitoring and control data.

### Keywords

Communication; Ethernet; Fieldbus protocols; Industrial protocols; Smart gridInformation in this chapter• Overview of Industrial Network Protocols• Fieldbus Protocols• Backend Protocols• AMI and the Smart GridUnderstanding how industrial networks operate requires a basic understanding of the underlying communications protocols that are used, where they are used, and why. There are many highly specialized protocols used for industrial automation and control, most of which are designed for efficiency and reliability to support the economic and operational requirements of large industrial control system (ICS) architectures. Industrial protocols are designed for real-time operation to support precision operations involving deterministic communication of both monitoring and control data.

This means that most industrial protocols forgo any feature or function that is not absolutely necessary for the sake of efficiency. More unfortunate is that this often includes the absence of even basic security features such as authentication or encryption, both of which require additional overhead. To further complicate matters, many of these protocols have been modified to run over Ethernet and Internet Protocol (IP) networks as suppliers moved away from proprietary networks and networking hardware and leveraged commercial off-the-shelf technologies. This, however, has now left these “fragile” protocols potentially vulnerable to cyberattack.

## Overview of industrial network protocols

Industrial network protocols are deployed throughout a typical ICS network architecture spanning wide-area networks, business networks, plant networks, supervisory networks, and fieldbus networks. Most of the protocols discussed have the ability to perform several functions across multiple network zones, and so will be referred to here more generically as industrial protocols.

Industrial protocols are real-time communications protocols, developed to interconnect the systems, interfaces, and instruments that make up an industrial control system. Many were designed initially to communicate serially over RS-232/485 physical connections at low speeds (typ. 9.6–38.4 kbps), but have since evolved to operate over Ethernet networks using routable protocols such as Transmission Control Protocol (TCP)/IP and User Datagram Protocol (UDP)/IP.

Industrial protocols for the purposes of this book will be divided into two common categories: fieldbus and backend protocols. Fieldbus is used to represent a broad category of protocols that are commonly found in process and control (see [Chapter 5](../B9780443137372000038/CH0005_91-128_B9780443137372000038.xhtml), “Industrial Network Design and Architecture”). Beginning in the early 1980s, there was a push from ICS vendors and end users to establish a global fieldbus standard. This effort continued for over 20 years and resulted in the creation of a wide range of standards devoted to industrial protocols. The International Electrotechnical Commission (IEC) 61158 standard was one of the early documents that established a base of eight different protocol sets called “types.” Some of the major protocols at that time (HART and CIP to name two) were missing from this list. The IEC 61784 standard was introduced in the early 2000s to amend the list originally contained in the IEC 61158 standard, and includes a total of nine protocol “profiles”: FOUNDATION Fieldbus, CIP, PROFIBUS/PROFINET, P-NET, WorldFIP, INTERBUS, CC-Link, HART, and Serial Real-time Communications System (SERCOS).[1](#fn1) Fieldbus protocols in this book are commonly deployed to connect process-connected devices (e.g., sensors) to basic control devices (e.g., Programmable Logic Controller [PLC]), and control devices to supervisory systems (e.g., ICS server, Human-Machine Interface [HMI], historian).

Backend protocols are those protocols that are commonly deployed on or above supervisory networks and are used to provide efficient system-to-system communication, as opposed to data access. Examples of backend protocols include connecting a historian to an ICS server, connecting an ICS from one supplier to another supplier's systems, or connecting two ICS operation control centers.

Four common industrial network protocols will be discussed in some depth, others will be touched upon more briefly, and many will not be covered here. There are literally dozens of industrial protocols, many developed by manufacturers for their specific purposes. The two fieldbus protocols analyzed include the Modicon Communication Bus (Modbus) and the Distributed Network Protocol (DNP3). Two backend protocols will also be discussed in detail; Object Linking and Embedding for Process Control (OPC) and the Inter-Control Center Protocol (ICCP, also referenced by standard IEC 60870–3 TASE.2 or Telecontrol Application Service Element). These particular protocols have been selected for more in-depth discussion because they are all widely deployed and they represent several unique qualities that are important to understand within the context of security. These unique qualities include the following:

1. • Each is used in different (though sometimes overlapping) areas within an industrial network.
2. • Each provides different methods of verifying data integrity and/or security.
3. • The specialized requirements of industrial protocols (e.g., real-time, synchronous communication) often make them highly susceptible to disruption.

It should be possible to assess the risks of other industrial network protocols that are not covered here directly by understanding the basic principles of how to secure these protocols.

## Fieldbus protocols

Modicon communication bus (Modbus)

The PLC dates as far back as 1968 when General Motors set out to find a new technology to replace their hard-wired electromechanical relay system with an electronic device. The first PLC was developed by Bedford Associates and designated 084 (representing the Bedford's 84th project), and released by the product name Modicon or MOdular DIgital CONtroller.[2](#fn2) This Modbus protocol was designed in 1979 to enable process controllers to communicate with real-time computers (e.g., MODCOMP FLIC, DEC PDP-11), and remains one of the most popular protocols used in ICS architectures. Modbus has been widely adopted as a de facto standard and has been enhanced over the years into several distinct variants.

Modbus' success stems from its relative ease of use by communicating raw messages without restrictions of authentication or excessive overhead. It is also an open standard, is freely distributed, and is widely supported by members of the Modbus Organization, which still operates today.

### What it does

Modbus is an application layer messaging protocol, meaning that it operates at layer 7 of the OSI model. It allows for efficient communications between interconnected assets based on a “request/reply” methodology. Extremely simple devices such as sensors or motors use Modbus to communicate with more complex computers, which can read measurements and perform analysis and control. To support a communications protocol on a simple device requires that the message generation, transmission, and receipt all require very little processing overhead. This same quality also makes Modbus suitable for use by PLCs and Remote Terminal Units (RTUs) to communicate supervisory data to an ICS system.

Because Modbus is a layer 7 protocol, it operates independently of underlying network protocols residing at layer 3, allowing it to be easily adapted to both serial and routable network architectures. This is shown in [Figure 6.1](#f0010).[3](#fn3)

#### How it works

Modbus is a request/response protocol using three distinct Protocol Data Units (PDUs): Modbus Request, Modbus Response, and Modbus Exception Response, as illustrated in Figures [6.2](#f0015) and [6.3](#f0020).[4](#fn4)

Modbus can be implemented on either an RS-232C (point-to-point) or RS-485 (multidrop) physical layer. Up to 32 devices could be implemented on a single RS-485 serial link, requiring each device communicating via Modbus be assigned a unique address. A command is addressed to a specific Modbus address, and while other devices may receive the message, only the addressed device will respond. Implementations using RS-232C were relatively simple to commission; however, do to the many variations in the way RS-485 could be implementing (2-wire, 4-wire, grounding, etc.), it was sometimes very challenging to commission a multidrop topology when using devices from many different vendors.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-01-9780443137372.jpg)

*[Figure 6.1](#Bf0010)  Modbus alignment with OSI 7-layer model.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-02-9780443137372.jpg)

*[Figure 6.2](#Bf0015)  General Modbus frame.*

A “transaction” begins with the transmission of an initial Function Code and a Data Request within a Request PDU. The receiving device responds in one of two ways. If there are no errors, it will respond with a Function Code and Data Response within a Response PDU. If there are errors, the device will respond with an Exception Function Code and Exception Code within a Modbus Exception Response.

Data are represented in Modbus using four primary tables as shown in [Table 6.1](#t0010). The method of handling each of these tables is device specific, as some may offer a single data table for all types, while others over unique tables. Careful review of the device documentation is needed in order to understand the device's data model, because the original Modbus definitions provided for only addresses in the range 0–9999. The specification has since been appended to allow up to 65,536 addresses across all four data tables. Another caveat within the standard is the original definition provided for the first digit of the register to identify the data table.

Function Codes used in Modbus are divided into three categories and provide the device vendor with some flexibility in how they implement the protocol within the  device. Function codes in the range of 01–64, 73–99 and 111–127 are defined as “Public” and are validated by the Modbus-IDA community and are guaranteed unique. This range is not entirely implemented, allowing codes to be defined in the future. “User-Defined” function codes in the range 65–72 and 100–110 are provided to allow a particular vendor to implement functionality to suit their particular device and application. These codes are not guaranteed to be unique and are not supported by the standard. The final category of codes represents “Reserved” functions that are used by some companies for legacy products, but are not available for general public use. These reserved codes include 8, 9, 10, 13, 14, 41, 42, 90, 91, 125, 126, and 127.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-03-9780443137372.jpg)

*[Figure 6.3](#Bf0020)  Modbus protocol transaction (error-free).*

Function Codes and Data Requests can be used to perform a wide range of commands. Some examples of Modbus commands include the following:

1. • Read the value of a single register.
2. • Write a value to a single register.
3. • Read a block of values from a group of registers.
4. • Write a block of values to a group of registers.
5. • Read files.
6. [Table 6.1](#Bt0010) Modbus Data Tables Data table Object type Access Data provided by Register range (0–9999) Register range (0–65535) Discrete input Single Bit Read-only Physical I/O 00,001–09,999 000,001–065,535 Coil Single Bit Read-write Application 10,001–19,999 100,001–165,535 Input register 16-bit Word Read-only Physical I/O 30,001–39,999 300,001–365,535 Holding register 16-bit Word Read-only Read-write 40,001–49,999 400,001–465,535
7. 
8. • Write files.
9. • Obtain device diagnostic data.

#### Variants

The popularity of Modbus has led to the development of several variations to suit particular needs. These include **Modbus RTU** and **Modbus ASCII**, which support binary and ASCII transmissions over serial buses, respectively. Modbus TCP is a variant of Modbus developed to operate on modern networks using the IP. **Modbus Plus** is a variant designed to extend the reach of Modbus via interconnected busses using token passing techniques.[5](#fn5)

##### Modbus RTU and Modbus ASCII

These similar variants of Modbus are used in asynchronous serial communications, and they are the simplest of the variants based on the original specification. Modbus RTU ([Figure 6.4](#f0025)) uses binary data representation, whereas Modbus ASCII ([Figure 6.5](#f0030)) uses ASCII characters to represent data when transmitting over the serial link. Modbus RTU is the more common version and provides a very compact frame over Modbus ASCII. Modbus ASCII represents data as a hexadecimal value coded as ASCII, with 2 characters required for each byte of data (ASCII PDU is twice the size of RTU PDU). Each uses a simple message format carried within an Application Data Unit (ADU) (see [Figure 6.2](#f0015)), consisting of an address, function code, a payload of data, and a checksum, to ensure the message was received correctly.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-04-9780443137372.jpg)

*[Figure 6.4](#Bf0025)  Modbus frame (Modbus RTU).*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-05-9780443137372.jpg)

*[Figure 6.5](#Bf0030)  Modbus frame (Modbus ASCII).*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-06-9780443137372.jpg)

*[Figure 6.6](#Bf0035)  Modbus frame (Modbus over TCP/IP).*

##### Modbus TCP

Modbus can also be transported over Ethernet using TCP in two forms. The basic form takes the original Modbus RTU ADU (as shown in [Figure 6.4](#f0025)) and applies a Modbus Application Protocol (MBAP) header to create a new frame ([Figure 6.6](#f0035)) that is passed down through the remaining layers of the communication stack adding appropriate headers ([Figure 6.7](#f0040)) before being placed on the Ethernet network. This new frame includes all of the original error checking and addressing information. This protocol behavior is very common with older, legacy devices that contain a Modbus RTU serial interface: the devices connect to a “device server” that converts serial data so that it can be transmitted on an industrial network; and is received by a similar “device server” that converts it back to serial RTU form.

Modbus TCP is the more common form and uses TCP as a transport over IP to issue commands and messages over modern routable networks. Modbus/TCP removes the legacy address and error checking, and places only the Modbus PDU together with an MBAP header into a new frame (see [Figure 6.8](#f0045)). The “Unit ID” acts as the new network  device address and is part of the MBAP. Error checking is performed as part of the composite Ethernet frame.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-07-9780443137372.jpg)

*[Figure 6.7](#Bf0040)  Modbus ADU with supplemental headers.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-08-9780443137372.jpg)

*[Figure 6.8](#Bf0045)  Modbus frame (Modbus/TCP).*

##### Modbus plus or Modbus+

Modbus Plus is actually not a variant of the base Modbus protocol, but a different one that utilizes token passing mechanisms to send embedded Modbus messages over an RS-485 serial communications link with transmissions rates up to 1Mbps using single (nonredundant) and dual-cable (redundant) topologies. The network supports the ability to broadcast data to all nodes and allows “bridges” to be added to network creating segmented Modbus networks that each can contain up to 64 addressable nodes. This allows for very large Modbus networks to be created. Modbus + remains a proprietary protocol to Schneider-Electric.[6](#fn6)

#### Where it is used

Modbus is typically deployed between PLCs (slave) and HMIs (master), or between a master PLC and several slave devices such as PLCs, drives, and sensors as shown in [Figure 6.9](#f0050). Modbus devices can act as a “master” to some, while acting at the same time as a “slave” to other devices. This function is common in a Master Terminal Unit that is  polling data as a master from several slave PLCs and intelligent electronic devices (IEDs), while supporting requests for data as a slave to other master devices like ICS servers and HMIs.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-09-9780443137372.jpg)

*[Figure 6.9](#Bf0050)  Typical Modbus use within the industrial network architecture.*

#### Security concerns

Modbus represents several security concerns:

1. • Lack of authentication. Modbus sessions only require the use of a valid Modbus address, function code, and associated data. The data must contain the values of legitimate registers or coils contained in the slave device, or the message will be rejected. This requires additional information of the target in order to provide a valid message; however, this can be obtained from either analysis of network traffic or the configuration of the device. Modbus supports additional function codes that can be used without specific knowledge of the target (e.g., function code 43). There is no verification that the message originated from a legitimate device allowing for simple man-in-the-middle (MitM) and replay style attacks.
2. • Lack of encryption. Commands and addresses are transmitted in clear text and can therefore be easily captured and spoofed or replayed due to the lack of encryption. Network packet capturing of communications to/from a Modbus device can also disclose significant information pertaining to the configuration and use of the device.
3. • Lack of message checksum (Modbus/TCP only). A command can easily be spoofed by building up the Modbus/TCP ADU with the desired parameters, as the checksum is generated at the transmission layer, not the application layer.
4. • Lack of broadcast suppression (serial Modbus variants only used in a multidrop topology). All serially connected devices will receive all messages, meaning a broadcast of unknown addresses can be used for effective denial of service (DoS) to a chain of serially connected devices.

#### Security recommendations

Modbus, like many industrial control protocols, should only be used to communicate between sets of known devices, using expected function codes. In this way, it can be easily monitored by establishing clear network zones and by baselining acceptable behavior. This baseline behavior can then be used to establish access controls on the conduit into the zone via appliances that provide protocol inspecting and filtering capabilities (e.g., industrial firewall with deep-packet inspection capabilities). It is also possible at the network level to create fingerprints of normal behavior patterns that facilitate network **whitelists** that can be implemented on in-line and out-of-band devices. For more information about creating whitelists, this topic is discussed in detail in [Chapter 11](../B9780443137372000129/CH0011_331-381_B9780443137372000129.xhtml), “Anomaly and Threat Detection.”

Some specific examples of Modbus messages that should be of concern include the following:

1. • Modbus TCP packets that are of wrong size or length.
2. • Function codes that force slave devices into a “listen only” mode.
3. • Function codes that restart communications.
4. • Function codes that clear, erase, or reset diagnostic information such as counters and diagnostic registers.
5. • Function codes that request information about Modbus servers, PLC configurations, or other device-specific, need-to-know information.
6. • Traffic on port 502/tcp that is not Modbus or is using Modbus over malformed protocol(s).
7. • Any message within an Exception PDU (i.e., any Exception Code).
8. • Modbus traffic from a server to many slaves (i.e., a potential DoS).
9. • Modbus requests for lists of defined points and their values (i.e., a configuration scan).
10. • Commands to list all available function codes (i.e., a function scan).

ICS-aware intrusion protection systems can be configured to monitor for these activities using Modbus signatures such as those developed and distributed by Digital Bond under the QuickDraw project. In more critical areas, an application-aware firewall, industrial protocol filter, or application data monitor may be required to validate Modbus sessions and ensure that Modbus has not been “hijacked” and used for covert communication, command, and control (i.e., the underlying TCP/IP session on port 502/tcp has not been altered to hide additional communications channels within otherwise normal-looking Modbus traffic). This device can also be used to limit function codes communicated into the zone to only those allowed for normal operation. This is discussed in detail in [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits.” [Figure 6.10](#f0055) illustrates configuration of an application-layer firewall on the conduit into an EIP zone separating four HMIs, one Engineering Workstation (EWS) and two PLCs.

CautionIntrusion prevention systems are able to actively block suspect traffic by dropping packets or resetting TCP connections. However, intrusion prevention systems deployed on industrial networks should be only be configured to block traffic after careful consideration and tuning. Unless you are confident that a given signature will not inadvertently block a legitimate control command, the signature should be set to alert, rather than block (i.e., operate in “detection” mode rather than active “prevention” mode).
### Distributed network protocol (DNP3)

DNP3 began as a serial protocol much like Modbus designed for use between “master stations” or “control stations” and slave devices called “outstations. It is also commonly  used to connect RTUs configured as “master stations” to IED “outstations” in electric substations. The Inter-Control Center Communication Protocol (ICCP) discussed later in this chapter is commonly used for communication between master stations. DNP3 was initially introduced in 1990 by Westronic (now GE-Harris Canada) and was based on early drafts of the IEC 60870-5 standard. The primary motivation for this protocol was to provide reliable communications in environments common within the electric utility industry that include high level of electromagnetic interference (EFI) and poor transmissions media (at that time based on analog telephone lines). DNP3 was extended to work over IP via encapsulated in TCP or UDP packets in 1998 and is now widely used in not only electric utility, but also oil and gas,[7](#fn7) water, and wastewater industries. One of the leading reasons for some industry migration from Modbus to DNP3 includes features that apply to these other industries including report by exception, data quality indicators, time-stamped data including sequence-of-events, and a two-pass “select before operate” procedure on outputs.[8](#fn8) Other markets, including Europe, have adopted the IEC 60870-5 versus of the protocol as it was ratified. Though DNP3 was based on IEC 60870-5, differences do exist between the two.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-10-9780443137372.jpg)

*[Figure 6.10](#Bf0055)  Application-layer firewall—Modbus/TCP zone protection. Image courtesy of Tofino Security—A Belden Brand.*

One distinction of DNP3 is that it is very reliable, while remaining efficient and well suited for real-time data transfer. It also utilizes several standardized data formats and supports time-stamped (and time-synchronized) data, making real-time transmissions  more efficient and thus even more reliable. Another reason that DNP3 is considered highly reliable is due to the frequent use of cyclical redundancy checks (CRCs)—a single DNP3 frame can include up to 17 CRCs: one in the header and one per data block within the payload (see the section “How it Works”). There are also optional link-layer acknowledgments for further reliability assurance, and—of particular note—variations of DNP3 that support link-layer authentication as well. Because all of this is done within the link-layer frame, it means that additional network-layer checks may also apply if DNP3 is encapsulated for transport over Ethernet.

Unlike Modbus and ICCP, DNP3 is both bidirectional (supporting communications from both Master to Slave and from Slave to Master) and it supports exception-based reporting. It is therefore possible for a DNP3 outstation to initiate an unsolicited response, in order to notify the master station of an event outside of the normal polling interval (such as an alarm condition).

#### What it does

Like the other industrial protocols, DNP3 is primarily used to send and receive messages between control system devices—only in the case of DNP3, it also does it with a high degree of reliability. Assuming that the various CRCs are all valid, the data payload is then processed. The payload is very flexible and can be used to simply transfer informational readings. It can also be used to send control functions, or even direct binary or analog data for direct interaction with devices such as RTUs and IEDs.

Both the link-layer frame (or LPDU) header and the data payload contain CRCs, and the data payload actually contains a pair of CRC octets for every 16 data octets. This provides a high degree of assurance that any communication errors will be detected. DNP3 will retransmit the faulty frames if any errors are detected. There are also physical layer integrity issues in addition to frame integrity. However, it still remains possible that a correctly formed and transmitted frame will not arrive at its destination. DNP3 uses an additional link layer confirmation to overcome this risk. When link layer confirmation is enabled, the DNP3 transmitter (source) of the frame requests that the receiver (destination) confirms the successful receipt of the frame. If a requested confirmation is not received, the link layer will retransmit the frame. This confirmation is optional because although it increases reliability, it adds overhead that directly impacts the efficiency of the protocol. In real-time environments, this added overhead might not be appropriate.[9](#fn9)

Once a successful and (if requested) confirmed frame arrives, the frame is processed. Each frame consists of a multipart header and a data payload. The header is significant as it contains a well-defined function code, which can tell the recipient whether it should confirm, read, write, select a specific point, operate a point (initiate a change to a point), directly operate a point (both selecting and changing a point in one command), or directly operate a point without acknowledgment.[10](#fn10)

These functions are especially powerful when considering that the data payload of the DNP3 frame supports analog data, binary data, files, counters, and other types of data objects. At a high level, DNP3 supports two kinds of data, referred to as class 0 or static  data (data that represent a static value) and event data (data that represent a change such as an alarm condition). Event data are rated by priority from class 1 (highest) to class 3 (lowest). The differentiation of static and event data, as well as the classification of event data, allows DNP3 to operate more efficiently by allowing higher-priority information to be polled more frequently, for example, or to enable or disable unsolicited responses by data type. The data itself can be binary, analog input or output, or a specific control output.[11](#fn11)

#### How it works

DNP3 provides a method to identify the remote device's parameters and then use message buffers corresponding to event data classes 1 through 3 in order to identify incoming messages and compare them to known point data. In this way, the master station is only required to retrieve new information resulting from a point change or change event on the outstation.

Initial communications are typically a class 0 request from the master station to an outstation, used to read all point values into the master station's database. Subsequent communications will typically either be direct poll requests for a specific data class from the master station; unsolicited responses for a specific data class from an outstation; control or configuration requests from the master station to an outstation; or subsequent periodic class 0 polls. When a change occurs on an outstation, a flag is set to the appropriate data class. The master station is then able to poll only those outstations where there is new information to be reported.

This is a major departure from constant data polling that directly results in improved responsiveness and more efficient data exchange. The departure from a real-time polling mechanism does require time synchronization because the time between a change event and a successful poll/request sequence is variable. This means that all responses are time-stamped so that the events between polls can be reconstructed in the correct order.

Communication is initiated by the master station to the outstation, or in the case of unsolicited responses (alarms) from the outstation to the master station, as shown in [Figure 6.11](#f0060). Because DNP3 operates bidirectionally and supports unsolicited responses, as shown in [Figure 6.12](#f0065), each frame requires both a source address and a destination address so that the recipient device knows which messages to process, and which device to return responses to. The addition of a source address does add some overhead. Remember that with purely master/slave protocols, there is no need for a source address as the originating device is always the master. This overhead provides a return benefit of dramatically increased scalability and functionality. As many as 65,520 individual addresses are available within DNP3, and any one of them can initiate communications. An address equals one device (every DNP3 device requires a unique address), although there are reserved DNP3 addresses, including one for broadcast messages (which will be received and processed by all connected DNP3 devices).[12](#fn12)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-11-9780443137372.jpg)

*[Figure 6.11](#Bf0060)  DNP3 protocol operation.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-12-9780443137372.jpg)

*[Figure 6.12](#Bf0065)  DNP3 protocol operation: unsolicited responses allow remote alarm generation.*

#### Secure DNP3

Secure DNP3 is a DNP3 variant that adds authentication to the response/request process, as shown in [Figure 6.13](#f0070). Authentication is issued as a challenge by the receiving device. A challenge condition occurs upon session initiation (when a master station initiates a DNP3 session with an outstation), after a preset period of time (the default is 20 min), or upon a “critical” request such as writes, selects, operates, direct operates, starts, stops, and restarts. It is possible to know which requests are critical because the data types and functions of DNP3 are well defined.[13](#fn13)

Authentication occurs using a unique session key that is hashed together with message data from the sender and from the challenger. The result is an authentication method that verifies authority (checksum against the secret key), integrity (checksum against the sending payload), and pairing (checksum against the challenge message) at the same time. In this way, it is very difficult to perform data manipulation or code injection, or to spoof or otherwise hijack the protocol.[14](#fn14)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-13-9780443137372.jpg)

*[Figure 6.13](#Bf0070)  Message confirmation and secure DNP3 authentication operation.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-14-9780443137372.jpg)

*[Figure 6.14](#Bf0075)  DNP3 protocol framing.*

The DNP3 layer 2 frame provides the source, destination, control, and payload, and can operate over a variety of application layers including TCP and UDP transports over IP (defaults include 19,999/tcp when using Transport Layer Security (TLS) for confidentiality and 20,000/tcp or 20,000/udp when using application layer only secure authentication). The function codes are resident within the CNTRL bytes in the DNP3 frame header, as shown in [Figure 6.14](#f0075).

#### Where it is used

DNP3 is primarily used between a master control station and an RTU in a remote station as shown in [Figure 6.15](#f0080), Transmissions medium can include wireless, radio, and dial-up. DNP3 is also widely used between to interconnect RTUs and IEDs. It can be applied in many applications like the Modbus protocols through a typical ICS architecture. Unlike Modbus, however, DNP3 is well suited for hierarchical and aggregated point-to- multipoint topologies in addition to the linear point-to-point and serial point-to-multipoint topologies that are supported by Modbus.[15](#fn15)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-15-9780443137372.jpg)

*[Figure 6.15](#Bf0080)  Typical DNP3 use within the industrial network architecture.*

#### Security concerns

While much attention is given to the integrity of the data frame, there is no authentication or encryption inherent within DNP3 (although there is within Secure DNP3). It then becomes relatively easy to manipulate a DNP3 session because of the well-defined nature of DNP3 function codes and data types in much the same way as it was the Modbus protocol.

DNP3 does include security measures; however, this added complexity of the protocol increases the chances of vulnerabilities. As of this writing, there are several known vulnerabilities with DNP3 that have been reported by the Industrial Control System Cyber Emergency Response Team (ICS-CERT). Proper system hardening, regular security assessments, and patching of DNP3 interconnections (both master stations and outstations) are recommended because there are known exploits in the wild and DNP3 is a heavily deployed protocol.

Some examples of realistic hacks against DNP3 include the use of MitM attacks to capture addresses, which can then be used to manipulate other system components. Examples of such manipulation include the following:

1. • Turning off unsolicited reporting to suppress alarms.[16](#fn16)
2. • Spoofing unsolicited responses to the master station to falsify events and trick an operator into taking inappropriate actions.
3. • Performing a DoS attack through the injection of broadcasts, creating storm behavior within the full extent of the DNP3 system.
4. • Manipulating the time synchronization data, resulting in synchronization loss and subsequent communication errors.
5. • Manipulating or eliminating confirmation messages forcing a state of continuous retransmission.
6. • Issuing unauthorized stops, restarts, or other functions that could disrupt operations.

#### Security recommendations

Because a secure implementation of DNP3 is available, the primary recommendation is to implement only Secure DNP3. This can pose problems with legacy installations due to backwards compatibility, as Version 5 of the standard (adopted as IEEE-1815-2012) is not backwards compatible, and Version 2 (adopted as IEEE-1815-2010) is now deprecated and should be upgraded. It may not always be possible to implement Secure DNP3 due to varying vendor support and other factors. Secure use of the transport layer protocol is advised in these cases, such as the use of TLS. In other words, treat your encapsulated DNP3 traffic as highly sensitive information and use every TCP/IP security best practice to protect it.

DNP3 master stations and outstations should always be isolated into a unique zone consisting only of authorized devices (multiple zones can be defined for devices communicating to multiple clients, or for hierarchical Master/Slave pairs), and the zone(s) should be thoroughly secured using standard defense-in-depth practices, including an industrial firewall and/or intrusion protection system that enforces strict control over the type, source, and destination of traffic over the DNP3 link across conduits between zones. Preference should be given to security practices that are capable of deep-packet inspection of DNP3 traffic. Many of the recommendations described for Modbus are equally applicable for DNP3, including the creation of network baselines and deployment of network whitelists.

Many threats can be detected through monitoring of DNP3 sessions, and looking for specific function codes and behaviors, including the following:

1. • Use of any non-DNP3 communication on a DNP3 Port (19,999/tcp, 20,000/tcp, 20,000/udp).
2. • Use of configuration function code 23 (Disable Unsolicited Responses).
3. 
4. • Use of control function codes 4, 5, or 6 (Operate, Direct Operate, and Direct Operate without Acknowledgment).
5. • Use of application control function 18 (Stop Application).
6. • Multiple, unsolicited responses over time (Response Storm).
7. • Any unauthorized attempt to perform an action requiring authentication.
8. • Any authentication failures.
9. • Any DNP3 communication sourced from or destined to a device that is not explicitly identified as a DNP3 master station or outstation device.

As with other industrial protocols, ICS-aware intrusion protection systems can be configured to monitor for these activities using DNP3 signatures such as those developed and distributed by Digital Bond under the QuickDraw supervisory control and data acquisition (SCADA) IDS project. An application-aware firewall or application data monitor may be required to validate DNP3 sessions.

CautionIntrusion prevention systems are able to actively block suspect traffic by dropping packets or resetting TCP connections. However, intrusion prevention systems deployed on industrial networks should be only be configured to block traffic after careful consideration and tuning. Unless you are confident that a given signature will not inadvertently block a legitimate control command, the signature should be set to alert, rather than block (i.e., operate in “detection” mode rather than active “prevention” mode).
### Process fieldbus (PROFIBUS)

PROFIBUS (PROcess FIeldBUS) is a fieldbus protocol that was originally developed in the late 1980s in Germany by a group of 21 companies and institutions known as the Central Association for the Electrical Industry (ZVEI). ZVEI published their first protocol specification known as PROFIBUS FMS (Fieldbus Message Specification) designed primarily to allow PLCs to communicate with host computers. This protocol was found to be too complex to implement in process control applications, so in 1993 the PROFIBUS DP (Decentralized Periphery) specification was released providing easier configuration and faster messaging. In 1989, the PROFIBUS User Organization (PROFIBUS Nutzer-organization or PNO) was established to maintain the specifications and ensure device compliance and certification. A larger user community was established in 1995 called PROFIBUS International to continue the advancement of PROFIBUS on a global level.

Several specialized variants of PROFIBUS exist, including PROFIBUS PA (for instrumentation used for process automation (PA)), PROFIsafe (for safety applications), and PROFIdrive (for high-speed drive applications). The most widely deployed variant is PROFIBUS DP, which itself has three variants: PROFIBUS DP-V0, DP-V1, and DP-V2, each of which represents a minor evolution of capabilities within the protocol. There are also three profiles for PROFIBUS communication: asynchronous, synchronous, and via  Ethernet using ethertype 0x8892. PROFIBUS over Ethernet is also called PROFINET[17](#fn17) and will be discussed separately as part of a category of protocols referred to as “Industrial Ethernet.”

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-16-9780443137372.jpg)

*[Figure 6.16](#Bf0085)  PROFIBUS DP communications.*

PROFIBUS is a master-slave protocol that supports multiple master nodes through the use of token sharing: when a master has control of the token, it can communicate with its slaves (each slave is configured to respond to a single master). [Figure 6.16](#f0085) illustrates how this token-based, master-slave topology operates. In PROFIBUS DP-V2, slaves can initiate communications to the master or to other slaves under certain conditions. A master PROFIBUS node is typically a PLC or RTU, and a slave is sensor, motor, or some other control system device.

PROFIBUS DP supports several different physical layer deployments with RS-485 as the most common. The existing RS-485 specification was extended to allow PROFIBUS to operate at speeds up to 12Mbps using two wires. The PA specification was developed to address the unique needs of field instrumentation in a manner similar to FOUNDATION Fieldbus. These installations must support wiring and communication with devices that are commonly installed in hazardous areas where explosive vapors and dusts are common. A concept known as “intrinsic safety” is used to limit the amount of available power on these communication lines to levels below that necessary to ignite the dust or vapor. The Manchester-encoded, bus-powered, intrinsically safe physical layer is used in these cases to address this requirement providing both limited levels of device power and communication on a single pair of wires.

#### Security concerns

PROFIBUS lacks authentication inherent to many of its functions, allowing a spoofed node to impersonate a master node, which in turn provides control over all configured slaves. A compromised master node or a spoofed master node could also be used to  capture the token, inject false tokens, or otherwise disrupt the protocol functions, causing a DoS. A rogue master node could alter clock synchronization to slave devices, snoop query responses (across all masters), or even inject code into a slave node. It is important to remember that PROFIBUS DP utilizes a serial connection between the master and slave devices, so the security concerns mentioned require physical access to connect to the DP network. This means that a DP network is not generally susceptible to industrial network-based attacks. However, the master device is typically connected to an Ethernet network and is therefore no less susceptible to attack from authorized network access than any other Ethernet-connected device. PROFINET is a real-time Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of Ethernet. When used over the IP, it is also susceptible to any vulnerabilities of IP.

NoteStuxnet (see Chapter 3, “Industrial Cyber Security, History and Trends”) is an example of PROFIBUS exploitation. Stuxnet compromised PLCs (PROFINET devices acting as PROFIBUS DP master nodes) via an initial network attack on an EWS or HMI. It then monitored the PROFIBUS DP network and looked for specific behaviors associated with frequency controllers (PROFIBUS DP slave nodes). Once the sought-after conditions were detected, Stuxnet then issued commands to the relevant slave nodes to sabotage the mechanical equipment (centrifuges used to enrich Uranium) by altering their operating parameters (speed of the centrifuges).
#### Security recommendations

PROFIBUS DP is a naturally segmented serial network utilizing a topology that is generally contained within a small geographical area such as a section of a plant or manufacturing process. The network and connected devices are very susceptible to attack if unauthorized physical access is obtained. For the purposes of this book, physical security must always be provided, since the threat events that can be performed via local access are relatively easy and can provide significant disruption to the operation of the ICS. This is outside the scope of this book.

## Industrial ethernet protocols

Industrial Ethernet is a term used to reference the adaptation of the IEEE 802.3 Ethernet standard to real-time industrial automation applications. One of the primary objectives of these extensions is the move toward more “synchronous” mechanisms of communication in order to prevent data collisions and minimize jitter inherent with “asynchronous” communications like standard Ethernet. This will allow the technology to be deployed in critical time-dependent applications like safety and industrial motion control. This concept may seem abstract in a time when 1Gbps switched networks are readily available;  however, as one moves into the industrial sector, the applications must be applicable to not only “lightweight” and simple devices that may not have the capacity for these modern IT networks, but also the deployment of network topologies on the factory floor that be more suited for bused or trunked style topologies (e.g., automobile networks).

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-17-9780443137372.jpg)

*[Figure 6.17](#Bf0090)  Methods for real-time Ethernet implementation.*

Industrial Ethernet also provides physical enhancements to “harden” the office-grade nature of standard Ethernet technologies with ruggedized wiring, connectors, and hardware designed to meet the environment of industrial applications. Conditions that are addressed with Industrial Ethernet include electrical noise and interference, vibration, extended temperatures and humidity (high and low), power requirements, and extensions to support real-time performance (low latency, low jitter, minimal packet loss).[18](#fn18)

There are some 30 different varieties of Industrial Ethernet[19](#fn19); however, for the purposes of this book, attention will be given to five as they are not only widely accepted and deployed in industry global (e.g., market leaders), but they introduce new concepts and concerns regarding industrial network security. These include Ethernet/IP, PROFINET, EtherCAT, Ethernet POWERLINK, and SERCOS III. Studies conducted by Institute of Management Services and ARC Advisory Group show that approximately 75% of all Ethernet installation in industrial environments use EtherNet/IP, PROFINET, or Modbus/TCP (already discussed), with the next two leading technologies based on POWERLINK and EtherCAT.[20](#fn20) [Figure 6.17](#f0090) provides an illustration of how these various technologies compare.

### Ethernet industrial protocol (EtherNet/IP)

It is important to understand the Common Industrial Protocol (CIP) in order to appreciate its versatility and application to the Ethernet/IP implementation. CIP, originally known as “Control and Information Protocol,” is a publicly available protocol managed through the Open DeviceNet Vendors Association (ODVA). CIP is an application layer protocol that provides a consistent set of messages and services that can be  implemented in a variety of ways using different network and link layer techniques, all supporting interoperability. These variations include EtherNet/IP (CIP on Ethernet), DeviceNet (CIP on CAN), CompoNet, and ControlNet (CIP on Concurrent Time Domain Multiple Access [CTDMA]) with extensions that include safety (CIP Safety), motion control (CIP Motion), and synchronization (CIP sync). [Figure 6.18](#f0095) illustrates the deployment model for CIP against the OSI layers.[21](#fn21)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-18-9780443137372.jpg)

*[Figure 6.18](#Bf0095)  Overview of common industrial protocol. [22](#fn22),[52](#fn52)*

NoteThe Controller Area Network (CAN) is a bus developed in 1985 by Bosch and adopted as international standard ISO 11898 in 1993 originally used for vehicle networks. It is a low-cost network utilizing a trunk-drop technology while suppling by power and signal to interconnect simple devices.NoteCTDMA provides the enhancements over traditional Carrier Sense Multiple Access/Collision Domain found in Ethernet to support deterministic, high-speed communication of time-critical I/O and control data. The design allows for all addresses to have access to the network through the implementation of a time slice algorithm that provides both “scheduled’ and “unscheduled” data transfers.EtherNet/IP (EIP) or CIP on Ethernet uses standard Ethernet frames (ethertype 0x80E1) in conjunction with the CIP suite to communicate with nodes. As with all CIP implementations, EIP supports integration of I/O, control, data collection, and device configuration on a single network. For real-time I/O and control-related data, EIP utilizes a connectionless multicast UDP transport called “implicit messaging” using port 2222/udp. This mechanism optimizes performance by establishing a “producer-consumer” relationship between devices sending data and those devices requiring the data—a common communications model within ICS architectures. A unicast TCP transport is also available to transmit larger quantities of data commonly associated with device configuration, diagnostics, and event information using an “explicit messaging” service commonly found on port 44,818/tcp.

NoteThe “IP” in Ethernet/IP derives from “Industrial Protocol” and not “Internet Protocol,” because of the use of the Common Industrial Protocol (CIP). Similarly, the acronym “CIP” meaning “Common Industrial Protocol” should not be confused with “Critical Infrastructure Protection” of NERC CIP.CIP uses object models to define the various qualities of a device. Each CIP object possesses attributes (data), services (commands), connections, and behaviors (relationships between attribute values and services). There are three types of objects:

1. • Required Objects: define attributes such as device identifiers such as the manufacturer, serial number, date of manufacture, etc. (Identity Object), routing identifiers for object-to-object messaging (Message Router Object), and physical connection data (Network Object)
2. • Application Objects: define input and output profiles for devices
3. • Vendor-specific Objects: enable vendors to add proprietary objects to a device

Objects (other than vendor-specific objects) are standardized by device type and function, to facilitate interoperability. If one brand of pump is exchanged for another brand, for example, the Application Objects will remain compatible, eliminating the need to build custom drivers. The wide adoption and standardization of CIP has resulted in an extensive library of device models, which can facilitate interoperability but can also aid in control network scanning and enumeration (see [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessments”).

While the Required Objects provide a common and complete set of identifying values, the Application Objects contain a common and complete suite of services for control, configuration, and data collection that includes both implicit (control) and explicit (information) messaging.[23](#fn23)

#### Security concerns

EIP is a real-time Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of Ethernet. EIP implicit messaging over UDP is transaction-less and so there is  no inherent network-layer mechanism for reliability, ordering, or data integrity checks. CIP also introduces some specific security concerns, due to its well-defined object model.

The following concerns are specific to Ethernet/IP:

1. • The CIP does not define any explicit or implicit mechanisms for security.
2. • The use of common Required Objects for device identification can facilitate device identification and enumeration, facilitating a targeted attack.
3. • The use of common Application Objects for device information exchange and control can enable broader industrial attacks, able to manipulate a broad range of industrial devices.
4. • Ethernet/IP's use of UDP and multicast traffic—both of which lack transmission control—for real-time transmissions facilitate the injection of spoofed traffic or (in the case of multicast traffic) the manipulation of the transmission path using injected Internet Group Management Protocol controls.

#### Security recommendations

EIP is a real-time Ethernet protocol using TCP and UDP transports making it necessary to provide Ethernet and IP-based security at the perimeter of any EIP network. Consideration should be given to placing EIP devices in dedicated zones that include either an application layer appliance capable of performing inspection in EIP packets and only allowing required functions within the zone. A stateful, packet-filtering firewalls that can be used to limit unnecessary inbound traffic (such as device configuration) to the zone. [Figure 6.19](#f0100) illustrates configuration of an application-layer firewall on the conduit into an EIP zone separating four HMIs, one EWS and two PLCs.

It is also recommended that passive network monitoring be used to ensure the integrity of the EIP network, ensuring that the EIP protocol is only being used by explicitly identify devices, and that no EIP traffic is originating from an unauthorized, outside source. This can be accomplished using an ICS-aware intrusion prevention system or other network monitoring devices capable of detecting and interpreting the EIP. Additional guidance can be obtained through ODVA.[24](#fn24)

### PROFINET

PROFINET is an open standard Industrial Ethernet developed by the PROFIBUS User Organization (PNO) and Siemens and is included as part of the IEC 61158 and IEC 61784 international standards for fieldbus communications. PROFINET was designed for scalability, and can be deployed at varying degrees of determinism and network performance. The first version of PROFINET utilized standard Ethernet and TCP/IP packets without modification for nonreal time automation applications and generation integration. The software-based real-time technology included in version 2 added support for time-critical communications with cycle times of 5–10 ms incorporating an optimized protocol stack bypassing OSI layers 3 and 4, limiting communications to a single  broadcast domain with no routing capability. PROFIBUS Isochronous Real Time (IRT) was introduced in version 3 of the standard, and provides cycle times of less than 1 ms with jitter less than 1 μs common in high-speed motion control applications. PROFIBUS IRT is a hardware-based solution that incorporates extensions to the Ethernet stack (OSI layer 2) requiring special application-specific integrated circuits at the device level and IRT-compatible network switches designed to minimize jitter. IRT is a layer 2 technology, so there is no routing capability possible with these data packets. [Figure 6.20](#f0105) illustrates the different classes of PROFINET.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-19-9780443137372.jpg)

*[Figure 6.19](#Bf0100)  Application-layer firewall—EtherNet/IP zone protection. Image courtesy of Tofino Security—A Belden Brand.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-20-9780443137372.jpg)

*[Figure 6.20](#Bf0105)  PROFINET implementation.*

#### Security concerns

PROFINET is a real-time Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of Ethernet. The extend of the risk is highly dependent on the technology deployed, since newer devices can utilize proprietary hardware making unauthorized network access more challenging than the general-purpose TCP/IP implementation. When used over the IP, it is also susceptible to any vulnerabilities of IP; however, the real-time implementations of PROFINET also employ nonroutable network communications offering some protection against remote or adjacent network vectors.

#### Security recommendations

As with many fieldbus protocols, the inherent lack of authentication and vulnerability of the protocol requires strong isolation of the bus. PROFINET TCP/IP represents the greatest risk as it can be transmitted over standard business and industrial networks. It should be tightly controlled, and when used within less-trusted business networks, it should be limited to authenticated and encrypted networks. It is not possible to segment PROFINET networks that contain devices that must communicate with each other (e.g., virtual local area networks (LANs) are not supported between PROFINET devices for logical segmentation); therefore, careful consideration in the deployment of zones and  conduits should be taken (see [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits”). Monitoring of Ethernet networks for unauthorized or suspicious use of PROFINET should be implemented including monitoring of all conduits into PROFINET zones. Firewalls and ICS-aware Intrusion Prevention Systems should be configured to explicitly deny PROFINET traffic outside of well-defined areas. Additional guidance can be obtained through PNO.[25](#fn25)

### EtherCAT

EtherCAT is another real-time Ethernet-based fieldbus protocol classified as “Industrial Ethernet” (see PROFINET for more information), which uses a defined ethertype (0x88A4) to transport ICS communications over standard Ethernet networks. These messages can either be transported directly in an Ethernet frame or encapsulated as a UDP payload using port 34980/udp (0x88A4). EtherCAT communicates large amounts of distributed process data with a single Ethernet frame to maximize the efficiency of distributed process data communications requiring only a few bytes per cycle over Ethernet frames that may vary in size from 46 to 1500 bytes. This means that only one or two Ethernet frames are required for a complete cycle allowing for very short cycle times with low jitter easily allowing network synchronization tasks to occur as required by the IEEE 1588 Precision Time Protocol (PTP) standard. EtherCAT is able to meet the requirements of PTP without any additional hardware (not the case with other industrial protocols discussed). Slaves pass the frame(s) to other slaves in sequence, appending its appropriate response, until the last slave returns the completed response frame back.[26](#fn26)

#### Security concerns

EtherCAT is a real-time Industrial Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of standard Ethernet. EtherCAT over UDP is transaction-less and so there is no inherent network-layer mechanism for reliability, ordering or data integrity checks.

EtherCAT is sensitive and highly susceptible to DoS attacks as with many real-time Ethernet protocols. EtherCAT is easily disrupted via the insertion of rogue Ethernet frames into the network to interfere with time synchronization and is subject to spoofing and MitM attacks due to the lack of bus authentication, requiring the separation of EtherCAT from other Ethernet systems.

#### Security recommendations

EtherCAT is a real-time Industrial Ethernet protocol making it is necessary to provide Ethernet-based security at the perimeter of any EtherCAT network. It is also recommended that passive network monitoring be used to ensure the integrity of the EtherCAT network, and that the EtherCAT protocol is only being used by explicitly identified devices. No EtherCAT traffic should be allowed that is originating from an unauthorized, outside source. This can be accomplished using an ICS-aware intrusion prevention  system or other network monitoring device capable of detecting and interpreting the EtherCAT protocol via UDP/IP. Static Ethernet address tables (MAC address) can be deployed to further protect real-time EtherCAT devices from external attack. Many switches provide features to provide MAC address control as well as tables to further restrict communications between EtherCAT devices. A network monitoring product or probe can also be used to detect Ethernet packets using EtherCAT's specific ethertype.

### Ethernet POWERLINK

Ethernet POWERLINK is also an “Industrial Ethernet” technology that uses Fast Ethernet as the basis for real-time transmission of control messages via the direct encapsulation of Ethernet frames without a master node that is used to initiate and synchronize cyclic polling of slave devices. Communication is divided into three time periods, with the first being the transmission of a master “Start of Cycle” frame that provides a basis for the network synchronization. The master then polls each station. The second time period is devoted to synchronous communication allowing the slaves to respond only if they receive a poll request frame, ensuring that all master/slave communications occur in sequence. Slave responses are broadcast, eliminating source address resolution. Asynchronous communication occurs in the third period where larger, nontime-critical data are transmitted. POWERLINK is best used homogeneously because collisions are avoided solely via the carefully controlled request/response cycles. The introduction of other Ethernet-based systems could disrupt synchronization and cause a failure.[27](#fn27)

POWERLINK is often used in conjunction with CANopen, an application layer protocol based on CAN. CANopen enables the communication between devices of different manufacturers, and the protocol stacks are widely available including open-source distribution for both Windows and Linux platforms. The open nature of CANopen makes POWERLINK/CANopen a desirable combination for industrial networks requiring inexpensive solutions in Linux environments.[28](#fn28)

#### Security concerns

POWERLINK is a real-time Industrial Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of other forms of Ethernet communication.

As with many real-time Ethernet protocols, POWERLINK is sensitive and highly susceptible to DoS attacks. POWERLINK is easily disrupted via the insertion of rogue Ethernet frames into the network, requiring the separation of POWERLINK from other Ethernet systems. The protocol itself is sensitive and highly susceptible to DoS attacks.

#### Security recommendations

POWERLINK implementations will most likely have a clear demarcation from other networks because sensitivity of the cyclic polling mechanism requires separation from other non–POWERLINK Ethernet services. This demarcation can be leveraged to further isolate the industrial protocol, through the establishment of appropriate security zones  and the definition of strong perimeter defenses at these boundaries. Static Ethernet address tables (MAC address) can be deployed to further protect real-time POWERLINK devices from external attack, since these are pure Ethernet-based messages and typically represent the most critical communications. Many switches provide features to provide MAC address control as well as tables to further restrict communications between EtherCAT devices.

### SERCOS III

SERCOS is a standardized open digital interface for communication between industrial controls, motion devices, and I/O devices. Versions I and II of the interface were based on a fiber-optic ring to establish interdevice communication. Version III of the interface is an “Industrial Ethernet”–based implementation of the SERCOS interface that supports deterministic real-time control of motion and I/O applications. Like EtherCAT and POWERLINK, SERCOS III has the ability to directly place Ethernet frames on the network in order to obtain high-speed communications with very low jitter.[29](#fn29) Networks can support up to 511 slave devices in either straight or ring topologies.

SERCOS III is a master-slave protocol that operates cyclically, using a mechanism in which a single Master Synchronization Telegram is used to communicate to slaves, and the slave nodes are given a predetermined time (again synchronized by the master node) during which they can place their data on the bus. All messages for all nodes are packaged into a Master Data Telegram, and each node knows which portion of the MDT it should read based upon a predetermined byte allocation.[30](#fn30)

SERCOS III dedicates the use of the bus for synchronized real-time traffic during normal cycles; however, like other Industrial Ethernet protocols discussed, it allows unallocated time within a cycle to be freed up for other network protocols such as TCP and UDP data using IP. This “IP Channel” allows the use of broader network applications from the same device—for example, a web-based management interface that would be accessible to “office and wide area networks.”[31](#fn31)

#### Security concerns

SERCOS III is a real-time Industrial Ethernet protocol, and as such it is susceptible to any of the vulnerabilities of other forms of Ethernet communication. SERCOS III introduces new security concerns through the option to support embedded, open TCP/IP, and UDP/IP communications. With this option enabled, a compromised RTU or PLC using SERCOS III could be used to launch an in-bound attack into other corporate communications systems, including industrial and business networks.

#### Security recommendations

As with other Industrial Ethernet–based protocols, static Ethernet address tables (MAC address) can be deployed to further protect real-time SERCOS III devices from external attack, since these are pure Ethernet-based messages and typically represent the most  critical communications. Many switches provide features to provide MAC address control as well as tables to further restrict communications between SERCOS III devices. SERCOS III should be isolated to control loops that require the protocol, and the use of IP channels should be restricted and avoided if possible. If IP channels are used, the extent and reach of the IP channel should be enclosed within an explicitly defined zone consisting of the SERCOS III master node and only those TCP/IP network devices that are absolutely required. Strong perimeter defenses should be installed in-band for all conduits into this zone using least privilege principles. Active monitoring of security device logs on the perimeter should be enabled due to the heightened risk from pivoting through networks using SERCOS III.

## Backend protocols

Object linking and embedding for process control

OPC is not actually an industrial protocol, but “a series of standards specifications”[32](#fn32) designed to simplify integration of various forms of data on systems from different vendors. In order to appreciate the impact OPC had on industrial automation, a brief history of OPC is warranted.

The original standard released in 1996 provided a mechanism for a standardized way for systems to exchange data across an Ethernet network using a core set of Microsoft technologies including: Object Linking and Embedded (OLE), Component Object Model (COM), and Distributed Component Object Model (DCOM). The specification included standard sets of “objects,” “interfaces,” and “methods” to support this interoperability in industrial applications. The underlying mechanism to support this communication was based on interprocess communications using the Remote Procedure Call (RPC) protocol. The original set of standards that utilized the COM/DCOM infrastructure is today commonly references as “OPC Classic.”

OPC has evolved significantly since its introduction nearly 20 years ago, and for that reason, the OPC Foundation (the organization that oversees the standards) has introduced new meaning to the dated acronym including “Open Platform Communications” and “Open Productivity and Connectivity.” The “classic” set of standards originally focused on real-time data access (OPC-DA released 1996), historical data access (OPC-HDA released 2001), and alarms and events data (OPC-AE released 1999). This set was expected to include data access via web services using extensible markup language (OPC-XMLDA released 2003), server-to-server and machine-to-machine communications (OPC-DX released 2003), and batch applications (OPC Batch released 2000). Since OPC relied on the DCOM infrastructure, users encountered significant problems in trying to manage OPC communication across security zones that were protected with firewalls including the lack of network address translation support and session callbacks.

Technology was moving away from the DCOM infrastructure and toward the .NET Framework. Using Windows Communication Foundation OPC.NET (formerly known as  OPC-Xi or eXpress Interface) incorporates the functionality of DA, HDA, and AE on a simplified data model. This new technology provided users with significant security improvements to how OPC.NET traffic was managed on industrial networks across zones. The downside was that there was little vendor support for this enhanced standard resulting in a relative small number of “gateway” type products.[33](#fn33)

All standards up to this point depended on some form of underlying Microsoft technology—COM, DCOM, or .NET. This significantly limited the deployment within ICS architectures much below the supervisory networks due to the fact that most of the embedded devices (Controllers, PLCs, RTUs, etc.) were not based on a Windows operating system that would support these classic standards. The idea was to move the communications model from COM/DCOM to a cross-platform service-oriented architecture to support broader deployment to non-Windows devices, and … better security! The OPC Unified Architecture (OPC-UA) specification was first released in 2006, and offers numerous improvements to the “classic” specifications while still supporting the underlying data integration requirements.

OPC Data Access “classic” is still one of the most widely deployed OPC specifications, and for the purposes of this book, is the one that will be discussed in more detail.

### What it does

OPC is one of the major “backend” protocols because it is designed to provide a higher level of integration between systems and subsystems, versus a fieldbus protocol that generally provides low-level data access and configuration.

OPC was originated motivated by the needs of end “users” and not system “vendors” to provide a common communications interface between diverse ICS components. The idea was to create a process industries technology that mirrored what Microsoft had done with device drivers in there newer Windows object-oriented operating systems. To digress briefly, many remember the days of Windows 3.11 and the requirement for every application to possess drivers necessary to utilize a dot-matrix printer. Microsoft solved that problem when they released Windows 95. The manufacturing community was no different—significant time and effort was spent in the 1980s and 1990s simply providing basic integration between the various systems that now are common components with in integrated ICS architecture.

This was accomplished by leveraging Microsoft's DCOM communications API, reducing the need for device-specific drivers. In place of specific communications drivers for each device, simple device drivers could be written to interface with OPC. The use of OPC therefore minimized driver development and allowed for better optimization of core OPC interfaces.[34](#fn34)

OPC's strengths and weaknesses come from its foundation, which is based upon Microsoft's OLE technology. OLE is used extensively in office document generation allowing the presentation of data to be separated from the application that generated it. A Word document can either “link” to a value calculated by a local or remote spreadsheet, or “embed” the spreadsheet inside the document. This not only allows  OPC-connected devices to communicate and interact with minimal operator feedback (as in the case of the Office documents). The concept of cyber security did not really exist in 1996, which meant that there were significant security challenges that lie ahead to those implementing OPC.[35](#fn35)

#### How it works

OPC works in a client/server manner, where a client application calls a local process, but instead of executing the process using local code, the process is executed on a remote server. The remote process is linked to the client application and is responsible for providing the necessary parameters and functions to the server, utilizing an RPC.

In other words, the stub process is linked to the client, but when a function is performed, the process is performed remotely, on the server. The server RPC functions then transmit the requested data back to the client computer. The client process then receives the data over the network, provides it to the requesting application, and closes the session, as shown in [Figure 6.21](#f0110).

In Windows systems, the requesting application typically loads RPC libraries at run-time, using a Windows dynamic link library.[36](#fn36)

OPC is more complex than previous client/server industrial protocols because of this interaction with the calling application and the underlying DCOM architecture. It interacts with various aspects of the host operating system, tying it closely to other host processes and exposing the protocol to a very broad attack surface. OPC also inherently supports remote operations that allow OPC to perform common control system functions.[37](#fn37)

One aspect that makes OPC and DCOM very challenging when characterizing industrial networks and the communications that occur across these networks and through various conduits is how DCOM begins the session on one port and then transfers to another. [Figure 6.22](#f0115) illustrates a typical OPC session that does not incorporate server “callbacks.”

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-21-9780443137372.jpg)

*[Figure 6.21](#Bf0110)  Typical OPC protocol operation.*

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-22-9780443137372.jpg)

*[Figure 6.22](#Bf0115)  OPC client-server communications.*

This figure shows how an initial request from an OPC Client to a corresponding OPC Server begins using a DCE BIND request to the Endpoint Mapper service listing on 135/tcp of the Server. Once the Client is authenticated against the Server and an OPC Instance created on the Server, the sessions shifts to a different connection, where the actual exchange of OPC data occurs. If a custom port range is not configured, this new port can be any randomly assigned port between 1024 and 65535 depending on the operating system. If Server callbacks are used, the original session actually disconnects after the OPC Instance is created, and the OPC Server initiates a new session with the OPC Client. In other words, the OPC Server is now the network “source address” and the OPC Client is now the “destination address.” A “tunneler” application can be installed to address this problem by allowing a point-to-point tunnel be created using a single predefined port where all RPC traffic (135 and the subsequent session port) are directed. The tunneler must be installed on both OPC Client and Server hosts, and should be qualified by the respective vendor to ensure that there is no impact to the performance of the other applications and services.

#### Where it is used

As the name implies, OLE for “Process” Control is primarily used within industrial networks (i.e., not a common business network technology), including data transfer to data historians, data collection within HMIs, connectivity between serial fieldbus protocols like Modbus and DNP3 and ICS servers, and other supervisory controls, as shown in [Figure 6.23](#f0120). The deployment of OPC servers within ICS architectures can greatly simplify the data integration in the core ICS servers allowing all proprietary protocols and interfaces to be managed via local, distributed OPC Servers that contain the appropriate physical and application connectivity to a particular subsystem or device. This Server is then connected to various ICS servers and components using a single, consistent mechanism. OPC is a Windows interconnection, so all communications occur either between Windows-based devices, or via OPC gateways that translate the RPC to the native fieldbus format. Because of the common use of RPC protocols within OPC, this opens the ICS environment to a very broad attack surface.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-23-9780443137372.jpg)

*[Figure 6.23](#Bf0120)  Typical OPC use within the industrial network architecture.*

#### Security concerns

Modular attack frameworks including Trisis, Industroyer, and Incontroller are able to directly manipulate OPC-DA and OPC-UA, both for reconnaissance and enumeration of industrial systems, and also to read and write specific parameters for manipulation of control (see [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), “Hacking Industrial Control Systems” for details on these attack frameworks).

OPC's use of DCOM and RPC makes it highly vulnerable to attack using multiple vectors, as it is subject to the same vulnerabilities as the more ubiquitously used OLE.[38](#fn38) Classic OPC is rooted in the Windows operating system and is therefore susceptible to attack through exploitation of any vulnerability inherent to the OS.[39](#fn39) Support for the Windows XP with Service Pack 3 ended on April 2014 (XP-SP2 ended July 2010), meaning that OPC applications hosted on unsupported OS can introduce significant risk to the integrity of manufacturing operations and potential health, safety, and environment impact.

OPC and related ICS vulnerabilities can be tracked via a variety of sources including the U.S. Department of Homeland Security ICS-CERT and the Open Source Vulnerability Database. Many OLE and RPC vulnerabilities exist and are well known, including exploit modules for a variety of open-source and fee-based security frameworks like Metasploit and Canvas (see [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), “Hacking Industrial Systems”). It is difficult to patch production systems within an industrial network (see [Chapter 8](../B9780443137372000026/CH0008_231-291_B9780443137372000026.xhtml), “Risk and Vulnerability Assessments” and [Chapter 10](../B978044313737200004X/CH0010_315-330_B978044313737200004X.xhtml), “Implementing Security Controls”) so many of these vulnerabilities may still be in place, even if there is an available patch from Microsoft. The SQL Slammer worm actually caused global damage despite the fact that Microsoft released a patch to correct the vulnerability 6 months prior to the release of the worm.

Many basic host security concerns apply because OPC is supported on Windows. RPC requires local authentication to occur on both client and server hosts. This requires the creation of either a local or domain-based account that can be used by RPC for the OPC sessions. This account can introduce significant risk if it is not properly secured using a least privilege approach for just the essential OPC/DCOM services. This account is common to all hosts utilizing OPC, and if not properly protected and managed can lead to a widespread compromise in large ICS architectures. Many OPC hosts utilize weak authentication, and passwords are often weak when authentication is enforced. Many systems support additional Windows services that are irrelevant to ICS systems, resulting in unnecessary processes, which often correspond to open “listening” communication ports accessible via the network. Inadequate or nonexistent logging exacerbates these potential weaknesses by providing insufficient forensic detail should a breach occur, as Windows 2000/XP auditing settings do not record DCOM connection requests by default.[40](#fn40)

Unlike the simple and single-purpose fieldbus protocols discussed earlier, OPC must be treated as an overall system integration framework, and implemented and maintained according to modern OS and network security practices.

Other security concerns of OPC include the following:

1. • Legacy authentication services—systems within industrial networks are difficult to upgrade (due to limited maintenance windows, compatibility and interoperability concerns, and other factors); insecure authentication mechanisms remain in use. For example, Windows 2000 LAN Manager (LM) and NT LAN Manager (NTLM) authentication mechanisms are still used by default in many systems (enabled by default up to and included Windows XP and 2003 Server). These and other legacy authentication mechanisms may be vulnerable and susceptible to exploitation.[41](#fn41)
2. • RPC vulnerabilities—OPC uses RPC making it susceptible to all RPC-related vulnerabilities, including several vulnerabilities that are exposed prior to authentication. Exploitation of underlying RPC vulnerabilities could result in arbitrary code execution, or DoS.[42](#fn42)
3. • Unnecessary ports and services—OPC supports network protocols other than TCP/IP, including NetBIOS Extended User Interface (NetBEUI), Connection Oriented NetBIOS over InterNetwork packet Exchange (IPX), and Hyper Text Transport Protocol (HTTP) Internet services.[43](#fn43)
4. • OPC Server Integrity—it is possible to create a rogue OPC server and to use that server for disruption of service, DoS, information theft through bus snooping, or the injection of malicious code.[44](#fn44)

#### Security recommendations

The newer Unified Architecture (OPC-UA) specification was designed for security and should be used where possible in place of OPC-DA.

Regardless of the OPC specification used (Classic or Unified Architecture), all unnecessary ports and services should be removed or disabled from the OPC server. This includes any and all irrelevant applications, and all unused network protocols. All unused services may introduce vulnerabilities to the system that could result in a compromise of the Windows host, and therefore the OPC network.[45](#fn45)

OPC servers should be isolated into a unique zones consisting only of authorized devices, and the zones(s) should be thoroughly secured using standard defense-in-depth practices, including a firewall and/or intrusion protection system that enforces strict control over the type, source, and destination of traffic to and from the OPC zone. Consideration should be given to application-aware firewalls that are capable of following the RPC session from the initial request (via 135/tcp) to response (a different port) and possible server “callbacks.”

Because OPC is primarily used in a supervisory capacity, intrusion “prevention” systems can be considered in place of “detection” only, understanding that an IPS may block legitimate ICS traffic and result in a lack of visibility into control system operations potentially causing a Loss of View (LoV) or Loss of Control (LoC) situation. If information loss will be damaging to the control process or detrimental to business operations, use only an IDS.

Many threats can be detected through monitoring OPC networks and/or OPC servers (server activity can be monitored through the collection and analysis of Windows logs), and looking for specific behaviors, including the following:

1. • The use of non-OPC ports and services initiated from the OPC server (requires DCOM services to be configured to use specific port range to eliminate wide range of “randomly” generated response ports).
2. • The presence of known OPC (including underlying OLE RPC and DCOM) exploits.
3. • OPC services originating from unknown OPC servers (indicating the presence of a rogue server).
4. • Failed authentication attempts or other authentication anomalies on the OPC server.
5. • Successful authentication attempts on the OPC server from unknown or unauthorized users.

Most commercially available IDS and IPS devices support a wide range of detection signatures for OLE and RPC and therefore can also detect many of the underlying vulnerabilities of OPC. Most open-source and commercial log analysis and threat detection tools are capable of collecting and assessing Windows logs.

TipOPC vulnerabilities may require the use of an ICS-aware intrusion protection system rather than an enterprise equivalent. Enterprise devices typically detect exploits via inspection of OLE, RPC, and DCOM but may not be able to detect all threats targeting OPC. In some cases, enterprise IDS/IPS devices may be able to detect a wider range of OPC threats, using industrial protocol preprocessors and detection signatures.
### Intercontrol center communications protocol (ICCP/IEC 60870-6 TASE.2)

The Inter-Control Center Communications Protocol (also known as TASE.2 or IEC60870-6, but more commonly referred to as simply ICCP) is a protocol designed for communication between control centers within the electric utility industry. Unlike fieldbus protocols like Modbus and DNP3, ICCP is classified as a “backend” protocol like OPC because of the fact it was designed for bidirectional Wide Area Network (WAN) communication between a utility control center and other control centers, power plants, substations, and even other utilities.

Much like the fundamental driver in the process industries developing OPC, electric utilities were also faced with ICS vendors and equipment suppliers utilizing many custom and proprietary protocols. A common protocol was needed to allow for reliable and standardized data exchange between utility control centers—especially when these control centers are operated by different owners, produce different products, or perform different operations. Standardization became necessary to support the unique business  and operational requirements of the electrical utilities that require careful load balancing within a bulk system operated by many disparate facilities. In North America, the division of utilities among several responsible regional entities requires a means of sharing information between utilities as well as the regional entity. National and global energy markets require real-time information exchange for load distribution and trading that spans the boundaries of individual utilities.

A working group was formed in 1991 to develop and test a standardized protocol and to submit the specification to the IEC for ratification and approval. The initial protocol was called ELCOM-90, or Telecontrol Application Service Element-1 (TASE.1). TASE.1 evolved into TASE.2, which is the most commonly used form of ICCP.[46](#fn46)

#### What it does

ICCP is used to perform a number of communication functions between control centers, including the following:

1. • Establishing a connection.
2. • Accessing information (read requests).
3. • Information transmission (such as email messages or energy market information).
4. • Notifications of changes, alarms, or other exception conditions.
5. • Configuration of remote devices.
6. • Control of remote devices.
7. • Control of operating programs.

#### How it works

The ICCP protocol defines communication between two control centers using a client-server model. One control center (the server) contains application data and defined functions. Another control center (the client) issues requests to read from the server with appropriate server responses. Communications over ICCP occur using a common format in order to ensure interoperability.

ICCP support is typically integrated either directly into an ICS, provided via a gateway product, or provided as software that can then be installed to perform gateway functions.

ICCP is primarily a unidirectional client-server protocol; however, most modern implementations support both functions, allowing a single ICCP device to function as both a client and a server, supporting bidirectional communication over a single connection.

ICCP can operate over essentially any network protocol, including TCP/IP; however, it is commonly implemented using the ISO transport on port 102/tcp, as defined in RFC 1006. ICCP is effectively a point-to-point protocol due to the use of a “bilateral table” that explicitly defines an agreement between two control centers connected with an ICCP link, as shown in [Figure 6.24](#f0125). The bilateral table acts as an access control list that identifies which data elements a client can access. The permissions defined within the bilateral tables in the server and the client are the authoritative control over what is accessible to each control center. The entries in the bilateral tables must also match on  both the client and the server, ensuring that the permissions are agreed upon by both centers (remembering that ICCP is used to interconnect to other organizations in addition to internal WAN links to substations).[47](#fn47)

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-24-9780443137372.jpg)

*[Figure 6.24](#Bf0125)  ICCP protocol operation.*

#### Where it is used

ICCP is widely used between control system zones and between distinct control centers, as shown in [Figure 6.25](#f0130). It is also commonly deployed between two electric utilities, between two control systems within a single electric utility, and between a main control center and a number of substations.

#### Security concerns

ICCP represents several security concerns much like most of the other fieldbus and backend protocols discussed. ICCP is susceptible to spoofing, session hijacking, and any number of attacks made possible because of:

1. • Lack of authentication and encryption—ICCP does not mandate authentication or encryption, most often deferring these services to lower protocol layers. Although “Secure ICCP”[48](#fn48) does exist, it is not ubiquitously deployed.
2. • Explicitly defined trust relationships—the exploitation of bilateral tables could directly compromise security of ICCP servers and clients.
3. • Accessibility—ICCP is a Wide Area Protocol making it highly accessible and susceptible to many attacks including DoS attacks from being exposed to public and/or shared networks versus traditional closed or private industrial networks within a plant environment.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-25-9780443137372.jpg)

*[Figure 6.25](#Bf0130)  Typical ICCP use within the industrial network architecture.*

The limited security mechanisms within ICCP are configured on the ICCP server, meaning that the successful breach of the server through an MitM or other attack opens the entire communication session up to manipulation.

#### Security improvements over Modbus

ICCP offers several improvements over more basic fieldbus protocols such as Modbus and DNP3, including the following:

1. • ICCP's use of bilateral tables provides basic control over the communication path by explicitly defining which ICCP clients and servers can communicate.
2. • A secure version of ICCP exists that incorporates digital certificate authentication and encryption.

#### Security recommendations

Secure ICCP variants should be used wherever possible and supported by the current vendors installed within a particular site. There are several known vulnerabilities with ICCP that have been reported by ICS-CERT. Proper system hardening and regular system  assessments and patching of ICCP servers and clients are recommended because there are known exploits in the wild and ICCP is a WAN protocol.

Extreme care should be taken in the definition of the bilateral table. The bilateral table is the primary enforcement of policy and permissions between control centers. Malicious commands issued via ICCP could directly alter or otherwise impact control center operations.

ICCP clients and servers should also be isolated into a unique zone consisting only of authorized client-server pairs (multiple zones can be defined for devices communicating to multiple clients), and the zones(s) should be thoroughly secured using standard defense-in-depth practices, including a firewall (industrial grade if installed in production environments) and/or intrusion protection system that enforces strict control over the type, source, and destination of traffic over the ICCP link. As with other industrial protocols, preference should be given to security practices that are capable of deep-packet inspection of ICCP traffic, if available. Many of the recommendations described for other industrial protocols are equally applicable for ICCP, including the creation of network baselines and deployment of network whitelists.

Many malicious behaviors can be detected through monitoring of the ICCP link, including the following:

1. • Intruders gaining unauthorized access to the control center network, via overlooked access points such as dial-up or remote access connections to partner or vendor networks with weak access control mechanisms.
2. • Insider threats, including unauthorized information access and transmission, alteration of secure configurations, or other malicious actions can be the result of a physical security breach within a control center, or of a disgruntled employee.
3. • A DoS attack resulting from repeated information requests (“spamming”) that utilize the server's available resources and prevent legitimate operation of the ICCP link.
4. • Malware infecting the ICCP server or other devices on the network could be used to exfiltrate sensitive information for purposes of sabotage (e.g., theft of command function codes), financial disruption (e.g., alteration of energy metrics used in trading), or various other malicious intents.
5. • Interception and modification of ICCP messages (i.e., MitM) attacks.
6. Monitoring of ICCP protocol functions can also detect suspicious or malicious behavior, such as
7. • Function “read” codes that could be used to exfiltrate protected information.
8. • Function “write” codes that could be used to manipulate client or server operations.
9. • Traffic on port 102/tcp that is not ICCP or other authorized protocol (PROFINET utilizes 102/tcp ISO-TSAP for its industrial Ethernet communications).
10. • ICCP traffic that is not sourced by and destined to defined ICCP servers or clients.

An ICS-aware intrusion protection system can be configured to monitor for these activities using ICCP signatures such as those developed and distributed by Digital Bond under the QuickDraw SCADA ICS project. An application-aware firewall, industrial protocol filter, or application data monitor may be required to validate ICCP sessions and ensure that ICCP or the underlying RFC-1006 connection have not been “hijacked” and that messages have not been manipulated or falsified.

CautionIntrusion prevention systems are able to actively block suspect traffic by dropping packets or resetting TCP connections. However, Intrusion prevention systems deployed on industrial networks should be only be configured to block traffic after careful consideration and tuning. Unless you are confident that a given signature will not inadvertently block a legitimate control command, the signature should be set to alert, rather than block (i.e., operate in “detection” mode rather than active “prevention” mode).
### IEC 61850, 60870-5-101, and 60870-5-104

IEC 61850 and IEC 60870-5 are communication protocols used primarily in electric power systems. While there are numerous standards of this nature, IEC 61850, IEC 60870-5-101, and IEC 60870-5-104 are mentioned here specifically because there is known malware capable of manipulating these protocols (see [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), “Hacking Industrial Control Systems” for details on the Industroyer and Industroyer 2 attack frameworks).

IEC 60870 is a communication protocol used in SCADA systems and other applications for monitoring and controlling electrical power systems. It is designed to provide reliable and interoperable communication used in power plants, substations, and control centers. It is a part of the IEC 60870-5 series of standards, which define telecontrol protocols for SCADA systems. IEC 60870-5-101 is designed for serial communications, while 60870-5-104 is designed for communication over TCP/IP networks. [Gordon R. Clarke et al, Practical modern SCADA protocols: DNP3, 60870.5 and related systems, Newnes, 2004 ISBN 0-7506-5799-5]

IEC 60870-5-101 and IEC 60870-5-104, often referred to more simply as IEC-101 and IEC-104 for convenience, both function in a client–server model. The control center acts as the client, and the remote device act as servers. The control center sends requests for data to devices, and the devices respond.

IEC 61850 is a communication protocol specifically designed for electrical substations, providing a standardized method for communication between IEDs like circuit breakers, transformers, and protection relays. The protocol helps improve interoperability, reliability, and flexibility in the management and control of power systems.

#### How they work

60870-5-101 and 60870-5-104

Requests and responses are organized into Application Service Data Units (ASDUs), which include a 1 byte Type Identification field (TI), a 1 byte Variable Structure Qualifier, a variable sized Cause of Transmission (COT) field, a variable Common Address field.  The remainder of the ASDU consists of an information object: the actual data elements contained within the ASDU. This object could consist of a data value such as a measurement, a command, or a status response. [International Electrotechnical Commission (IEC). International Standard IEC 60870-5-101. Second Edition. IEC. Geneva 20, Switzerland. 2006.]

ASDUs, encapsulated with Application Protocol Data Units (APDUs), are transmitted over either serial (IEC-101) or TCP/IP (IEC-104).

Communication typically consists of the control center sending a request for data or a control command to one or more devices. The devices then respond with the requested information (in the case of a data request) or a command confirmation (in the case of a control command). Data requests could consist of alarms, measurements, or status information. Once the exchange is finished, either the client or the server can close the connection.

##### IEC 61850

IEC 61850 uses an object-oriented approach for modeling devices and their data. Each device is represented as a hierarchy of logical nodes, data objects, and data attributes. These models can be used to provide highly interoperable communications between devices, over a variety of communication protocols.

In substation applications, data is exchanged primarily via Generic Object-Oriented Substation Events (GOOSE) and Sample Values (SVs) messages. GOOSE messages are used for event-driven communication, like alarms or interlocking, while SV messages are used for transmitting high-speed sampled analog data, such as current and voltage measurements. Messages are exchanged using high-speed Ethernet networks and TCP/IP.

A single GOOSE message sent from one device can be received and used by several other devices, using standard broadcast and multicast mechanisms within IP, and a publish/subscribe data exchange model. One device (the sender) publishes information, while one or more other devices (the subscribers) receive that data act upon it. The action performed by each receiver upon receiving data depends on its configuration and functionality, as defined by its IEC 61850 device model. This enables automation of substation control, including protection. [Bill Lydon. IEC 61850 Power Industry Communications Standard. [Automation.com](http://Automation.com). Feb 07, 2009. [https://www.automation.com/en-us/articles/2003-1/iec-61850-power-industry-communications-standard](https://www.automation.com/en-us/articles/2003-1/iec-61850-power-industry-communications-standard)].

#### Security concerns

As with most industrial protocols, the increased connectivity and reliance on digital communication also introduces new cybersecurity risks and challenges. Some of the key cybersecurity implications of these protocols are:

1. • These protocols are vulnerable to known cyber-physical attack frameworks, including Industroyer and Industroyer 2 (see [Chapter 7](../B9780443137372000014/CH0007_181-229_B9780443137372000014.xhtml), “Hacking Industrial Control Systems” for details on these attack frameworks).
2. 
3. • These protocols have been successfully manipulated to disrupt electrical distribution systems.
4. • The ability to monitor devices remotely using these protocols can be exploited by adversaries to obtain valuable information about the target systems, which can be used to develop targeted attacks.
5. • The ability to control devices remotely using these protocols can be exploited by adversaries to manipulate a process, potentially damaging physical equipment and/or introducing hazardous conditions.
6. • The ability to intercept and manipulate data can be used to hide malicious activities from operators.
7. • Network-based DoS attacks can disrupt communication between devices, leading to LoC, reduced situational awareness, and potential process failures.

#### Security recommendations

Devices communicating using these IEC protocols should be isolated into a unique zones consisting only of authorized devices, and the zones(s) should be thoroughly secured using standard defense-in-depth practices, including a firewall and/or intrusion detection or protection system that enforces strict control over the type, source, and destination of IEC traffic within this zone.

Because these protocols are often used to communicate between highly distributed systems, e.g., power substations, the integrity of communications should not be assumed. Monitoring relevant devices and the communications between those devices for abnormal behavior is recommended.

#### AMI and the smart grid

The smart grid is a term encompassing many aspects of modern power generation, transmission, and distribution. Although smart grid technology might seem irrelevant to many industrial network systems outside of the electric utility industry, it is discussed briefly here because of its broad reach and vulnerable attack surface. The smart grid is a widely distributed communication network that touches both power generation and transmission systems, along with many end user networks. The smart grid represents an easily accessible network that contains many vectors to many possible targets. Once compromised, an attacker could use the network to attack the power utility's network, or to attack the networks of connected home and businesses.

The term “smart grid” is widely used and generally refers to a new era of energy distribution built around an Advanced Metering Infrastructure (AMI). AMI promises many new features designed to increase the efficiency and reduce the costs of energy distribution. Common AMI features include remote meter reading, remote billing, demand/response energy delivery, remote connect/disconnect, and remote payment and prepayment.[49](#fn49)

At a high level, the smart grid requires coordination among the following systems:

1. • Bulk Electric Generation Systems
2. • Electric Transmission Systems
3. • Electric Distribution Systems
4. • Customer Information and Management Systems
5. • Usage and Meter Management Systems
6. • Billing Systems
7. • Interconnected network systems, including neighborhood area networks (often using wireless mesh technologies); metropolitan area networks; home area networks (HANs); and business area networks (BANs)

The smart grid is essentially a large, end-to-end communications system interconnecting power suppliers to power consumers (see [Figure 6.26](#f0135)). It is made of highly diverse systems, using diverse protocols and network topologies. Smart grids even introduce new protocols. To support home- and business-based service portals, smart metering introduces HAN and BAN protocols, such as Zigbee and HomePNA, as well as power line protocols such as IEC 61334, Control Network Power Line (PL) Channel Specification, and Broadband over Powerline (BPL). The data link and application protocols are too numerous to discuss in detail, though it is widely accepted that TCP/IP will be leveraged for network-layer communications.[50](#fn50)

These specific protocols will not be discussed within this book, but it is still important to recognize that the disparate nature of these systems requires that several distinct operational models and network architectures combine to form a single end-to-end communications path, as illustrated in [Figure 6.23](#f0120). This means that while many distinct smart grid protocols may be used, the smart grid as a whole should be considered as a single, readily accessible communications network that is vastly interconnected.

![image](/api/v2/epubs/urn:orm:book:9780443137389/files/IMAGES/B9780443137372000063/main.assets/f06-26-9780443137372.jpg)

*[Figure 6.26](#Bf0135)  Smart grid operational areas and protocols.*

#### Security concerns

The security concerns of the smart grid are numerous. AMI represents an extremely large network that touches many other private networks and is designed with command and control capabilities in order to support remote disconnect, demand/response billing, and other features.[51](#fn51) Combined with a lack of industry-accepted security standards, the smart grid represents significant risk to connected systems that are not adequately isolated. Specific security concerns include the following:

1. • Smart meters are readily accessible and therefore require board- and chip-level security in addition to network security.
2. • Smart grid protocols vary widely in their inherent security and vulnerabilities.
3. • Neighborhood, home, and business LANs can be used both as an ingress to the AMI, and as a target from the AMI.
4. • Smart grids are ultimately interconnected with critical power generation and distribution systems.
5. • Smart grids represent a target to private hackers (for financial gain or service theft) as well as to more sophisticated and serious attackers (for sociopolitical gain or cyber warfare).

#### Security recommendations

The best recommendation for smart grid security at this point is for electric utilities to carefully assess smart grid deployments and to perform risk and threat analysis early in the planning stages. A similar assessment of the system should be performed for end users who are connected to the smart grid who could become a potential threat vector into the business (or home) networks.

Clear delineation, separation of services, and the establishment of strong defense-in-depth at the perimeters will help to mitigate the risk from threats associated with the smart grid. This could represent a challenge (especially in terms of security monitoring) for smart grid operators, due to the broad scale of smart grid deployments, which could contain hundreds of thousands or even millions of intelligent nodes. It may be necessary then to carve out smart grid deployments into multiple, smaller and more manageable security zones.

#### Industrial protocol simulators

One way to learn and understand how an industrial protocol operates is to purchase the appropriate hardware (i.e., PLC) and software (SCADA). This can be both expensive and time consuming. Another more practical approach is through the deployment of client and server simulators capable of mimicking the protocol within a physical or virtualized computing environment.

Simulators are readily available for royalty-free protocols like Modbus/TCP, but can be limited for the licensed protocols. In the latter cases, one alternative approach is the  use of “trial” or “demonstration” software packages. The products below were available at the time of publishing, and are provided for illustrative purposes only.

#### Modbus/TCP

There are a range of Modbus simulators that will support both Modbus RTU and ASCII formats using both serial and Ethernet communication. The ModbusPal package available on SourceForge is particularly interesting because it is based on Java allowing it to be easily transported between different platforms (Windows, Mac, Linux). It also features an “automation” capability allowing it to vary inputs and outputs providing the ability to change data at the source. ModbusPal supports “user-defined” commands using function codes 65–72 and 100–110.

Triangle Microworks Communication Protocol Test Harness provides not only protocol simulation, but actual simulation of a variety of devices as well, allowing this to be a tool used by ICS software developers as part of protocol compliance testing. The Test Harness supports a range of protocols including Modbus/TCP, DNP3, and IEC 60870-5, and is available as a paid download or a 21-day evaluation version.

Modsak is a software package from Wingpath Software Development that supports either master or client modes. A 3-day trial version is available that offers a range of features, including support for Modbus “user-defined” functions.

#### DNP3

The Axon Group offers a free simulation package for both DNP3 and IEC 60870-5. The Communication Test Harness from Triangle Microworks also supports DNP3 and can operate as both the master station and outstation. More advanced options are available through a variety sources that provide DNP3 protocol libraries for custom application development.

#### OPC

Matrikon and Kepware are two leading suppliers of OPC products to a variety of ICS industry segments, both offering demonstration versions of their OPC applications. Matrikon offers a set of free OPC test tools that support the creation of OPC clients and servers, as well as trial versions of most of their applications including various system interface servers, protocol tunnelers, and more. Kepware offers similar trial licenses for their OPC server, as well as a linking package that can be used to connect two OPC servers.

#### ICCP/TASE.2

Triangle Microworks IEC 60870-6 (TASE.2/ICCP) Test Tool is available as a paid license or a 21-day evaluation version with support for both client and server roles. The package supports ICCP blocks 1, 2, and 5 with full support of writes, reads, controls, dynamic data sets, and dataset transfer sets. It also allows for models to be created via .csv files and .xml files.

#### Physical hardware

Investing in physical hardware to support a training and test laboratory does not have to be overly expensive. Many suppliers including ABB, Allen–Bradley, Schneider Electric, Siemens, and Wago offer affordable, compact programmable devices that can support multiple protocols within a single device. Nearly all products will offer support for Modbus/TCP due to its widespread use, but can also be supplied with Ethernet/IP, PROFINET, and EtherCAT capabilities. Another very economical method of obtaining physical hardware is through reseller or auction websites like eBay.

## Summary

Industrial networks use a variety of specialized protocols at multiple layers in the network to accomplish specific tasks, often with careful attention to synchronization and real-time operation. Each protocol has varying degrees of inherent security and reliability, and these qualities should be considered when attempting to secure these protocols. All of these protocols are susceptible to cyberattack using relatively simple MitM mechanisms because industrial network protocols, in general, lack sufficient authentication or encryption. These attacks can be used to disrupt normal protocol operations or potentially alter or otherwise manipulate protocol messages to steal information, commit fraud, or potentially cause a failure of the control process itself including mechanical equipment sabotage (e.g., Stuxnet).

These protocols can be reasonably secured by understanding them and isolating each into its own carefully defined security zone with related conduits (see [Chapter 9](../B9780443137372000130/CH0009_293-314_B9780443137372000130.xhtml), “Establishing Zones and Conduits”). The creation of zones based purely on physical devices is possible and relatively simple because each protocol has specific uses within a control system. Since industrial network protocols are used more widely over Ethernet and TCP/IP–UDP/IP, the creation of clean zone boundaries becomes more difficult, as these boundaries begin to overlap. The use of “business” network protocols to transport fieldbus protocols should be avoided unless absolutely necessary for this reason, and be especially scrutinized and tested where they are necessary.

---

[1](#cfn1)  IEC 61784-1:2010 “Industrial communication networks - Profiles - Part 1: Fieldbus profiles”, published June 1, 2011.

[2](#cfn2)  “Schneider Electric Modicon History”, [http://www.plcdev.com/schneider_electric_modicon_history](http://www.plcdev.com/schneider_electric_modicon_history) (cited: January 7, 2014).

[3](#cfn3)  Modbus Organizations, “Modbus Application Protocol Specification”, Version 1.1b, Published December 28, 2066.

[4](#cfn4)  Ibid.

[5](#cfn5)  Ibid.

[6](#cfn6)  AEG Schneider Autotmation, “Modicon Modbus Plus Nework Planning and Installation Guide”, 890-USE-100.00 Version 3.0, April 1996.

[7](#cfn7)  Triangle MicroWorks, “Using DNP3 & IEC 60870-5 Communication Protocols in the Oil & Gas Industry”, Revision 1, published March 26, 2001.

[8](#cfn8)  Triangle MicroWorks, “Modbus and DNP3 Communication Protocols”, [http://trianglemicroworks.com/docs/default-source/referenced-documents/Modbus_and_DNP_Comparison.pdf](http://trianglemicroworks.com/docs/default-source/referenced-documents/Modbus_and_DNP_Comparison.pdf) (cited: January 8, 2014).

[9](#cfn9)  The DNP Users Group, DNP3 Primer, Revision A. [http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf](http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf), March 2005 (cited: November 24, 2010).

[10](#cfn10)  R. Clarke, Deon Reynders Practical Modern SCADA Protocols: DNP3, 60870.5 and Related Systems, Newnes, Oxford, UK and Burlington MA, 2004.

[11](#cfn11)  The DNP Users Group, DNP3 Primer, Revision A. [http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf](http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf), March 2005 (cited: November 24, 2010).

[12](#cfn12)  Ibid.

[13](#cfn13)  Digitalbond SCADAPEDIA, Secure DNP3. [http://www.digitalbond.com/wiki/index.php/Secure_DNP3](http://www.digitalbond.com/wiki/index.php/Secure_DNP3), August 2008 (cited: November 24, 2010).

[14](#cfn14)  Ibid.

[15](#cfn15)  The DNP Users Group, DNP3 Primer, Revision A. [http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf](http://www.dnp.org/About/DNP3%20Primer%20Rev%20A.pdf), March 2005 (cited: November 24, 2010).

[16](#cfn16)  A.B.M. Omar Faruk, Testing & Exploring Vulnerabilities of the Applications Implementing DNP3 Protocol, KTH Electrical Engineering, Stockholm, Sweden, June 2008.

[17](#cfn17)  V.M. Igure, Security assessment of SCADA protocols: a taxonomy based methodology for the identification of security vulnerabilities in SCADA protocols, VDM Verlag Dr. Müller Aktiengesellschaft & Co. KG, 2008.

[18](#cfn18)  “Industrial Ethernet: A Control Engineer's Guide”, Cisco, April 2010.

[19](#cfn19)  Prof. Dr.-Ing. J. Schwager, “Information about Real-Time Ethernet in Industry Automation”, Reutlinger University, [http://www.pdv.reutlingen-university.de/rte/](http://www.pdv.reutlingen-university.de/rte/), (cited: January 10, 2014).

[20](#cfn20)  Industrial Ethernet Facts, “System Comparison: The five Major Technologies”, Ethernet POWERLINK Standardization Group, Issue 2, February 2013.

[21](#cfn21)  Ibid.

[22](#cfn22)  Open Device Vendors Association (ODVA), “Common Industrial Protocol”, PUB00122R0-ENGLISH, 2006.

[23](#cfn23)  Ibid.

[24](#cfn24)  Open-Device Vendors Association, “Securing Ethernet/IP Networks”, PUB00269R1, 2011.

[25](#cfn25)  PROFIBUS Nutzerorganisation e.V., “PROFINET Security Guidelines: Guideline for PROFINET”, Version 2.0, November 2013.

[26](#cfn26)  The EtherCAT Technology Group, Technical introduction and overview: EtherCAT—the Ethernet Fieldbus. [http://www.ethercat.org/en/technology.html#5](http://www.ethercat.org/en/technology.html#5), May 10, 2010 (cited: November 24, 2010).

[27](#cfn27)  P. Doyle, Introduction to Real-Time Ethernet II. The Extension: A Technical Supplement to Control Network, vol. 5, Issue 4, Contemporary Control Systems, Inc., Downers Grove, IL, July 2004.

[28](#cfn28)  Ethernet POWERLINK Standardization Group, CANopen. [http://www.ethernet-powerlink.org/index.php?id=39](http://www.ethernet-powerlink.org/index.php?id=39), 2009 (cited: November 24, 2010).

[29](#cfn29)  SERCOS International, Technology: Introduction to SERCOS interface. [http://www.sercos.com/technology/index.htm](http://www.sercos.com/technology/index.htm), 2010 (cited: November 24, 2010).

[30](#cfn30)  SERCOS International, Technology: Cyclic Operation. [http://www.sercos.com/technology/cyclic_operation.htm](http://www.sercos.com/technology/cyclic_operation.htm), 2010 (cited: November 24, 2010).

[31](#cfn31)  SERCOS International, Technology: Service & IP Channels. [http://www.sercos.com/technology/service_ip_channels.htm](http://www.sercos.com/technology/service_ip_channels.htm), 2010 (cited: November 24, 2010).

[32](#cfn32)  OPC Foundation, “What is OPC?”, [http://www.opcfoundation.org/Default.aspx/01_about/01_whatis.asp?MID=AboutOPC](http://www.opcfoundation.org/Default.aspx/01_about/01_whatis.asp?MID=AboutOPC), (cited: January 9, 2014).

[33](#cfn33)  OPC Foundation, “Certified Products”, [http://www.opcfoundation.org/Products/Products.aspx](http://www.opcfoundation.org/Products/Products.aspx), (cited: January 9, 2014).

[34](#cfn34)  Ibid.

[35](#cfn35)  Digital Bond, British Columbia Institute of Technology, and Byres Research. OPC Security White Paper #2: OPC Exposed (Version 1-3c), Byres Research, Lantzville, BC and Sunrise, FL, November 13, 2007.

[36](#cfn36)  Microsoft Corporation, RPC Protocol Operation. [http://msdn.microsoft.com/en-us/library/ms818824.aspx](http://msdn.microsoft.com/en-us/library/ms818824.aspx) (cited: November 4, 2010).

[37](#cfn37)  European Organization for Nuclear Research (CERN), A Brief Introduction to OPC Data Access. [http://itcofe.web.cern.ch/itcofe/Services/OPC/GeneralInformation/Specifications/RelatedDocuments/DASummary/DataAccessOvw.html](http://itcofe.web.cern.ch/itcofe/Services/OPC/GeneralInformation/Specifications/RelatedDocuments/DASummary/DataAccessOvw.html), November 11, 2000 (cited: November 29, 2010).

[38](#cfn38)  “OPC Security Whitepaper #3: Hardening Guidelines for OPC Hosts”, DigitalBond, British Columbia Institute of Technology, Byres Research, November 13, 2007.

[39](#cfn39)  Digital Bond, British Columbia Institute of Technology, and Byres Research. OPC Security White Paper #2: OPC Exposed (Version 1-3c), Byres Research, Lantzville, BC and Sunrise, FL, November 13, 2007.

[40](#cfn40)  Ibid.

[41](#cfn41)  Ibid.

[42](#cfn42)  Ibid.

[43](#cfn43)  Ibid.

[44](#cfn44)  Ibid.

[45](#cfn45)  Ibid.

[46](#cfn46)  J.T. Michalski, A. Lanzone, J. Trent, S. Smith, SANDIA Report SAND2007-3345: Secure ICCP Integration Considerations and Recommendations, Sandia National Laboratories, Albuquerque, New Mexico and Livermore, California, June 2007.

[47](#cfn47)  Ibid.

[48](#cfn48)  J. Michalski, A. Lanzone, J. Trent, S. Smith, “Secure ICCP Integration: Considerations and Recommendations”, Sandia Report SAND2007-3345, printed June 2007.

[49](#cfn49)  UCA International Users Group, AMI-SEC Task Force, AMI System Security Requirements, UCA, Raleigh, NC, December 17, 2008.

[50](#cfn50)  National Institute of Standards and Technology, NIST Special Publication 1108: NIST Framework and Roadmap for Smart Grid Interoperability Standards, Release 1.0, February 2010.

[51](#cfn51)  UCA International Users Group, AMI-SEC Task Force, AMI system security requirements, UCA, Raleigh, NC, December 17, 2008.

[52](#cfn52)  Open Device Vendors Association (ODVA), “Common Industrial Protocol”, PUB00122R0-ENGLISH, 2006.
