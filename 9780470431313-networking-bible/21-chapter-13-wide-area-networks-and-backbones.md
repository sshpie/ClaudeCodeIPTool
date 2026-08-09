# Chapter 13. Wide Area Networks and Backbones

**IN THIS CHAPTER**

- Wide Area Networks
- Circuit switching networks and the phone system
- ISDN and DSL phone connections
- Connect WANS with high-speed carrier links and SONET
- Packet switching networks
- Packet protocols — X.25, ATM, and Frame Relays
- Internet and Internet2 infrastructure

A Wide Area Network, or WAN, is a collection of networks connected through a public service or covering a large geographical area. To enable a WAN requires a routing or switching technology and a set of protocols that create paths from one point to another. There are four kinds of WANs: circuit switching, packet switching, cell relay, and leased lines.

The Public Switched Telephone Network (PSTN) is used as an example of a circuit switching network. The PSTN is built hierarchically. Different methods for connecting to the PSTN for data services are described. In particular, two of the most popular connection types, ISDN and DSL, are described in detail. The backbone technologies for connecting networks are through T- and E-carrier networks. Different standards and grades exist, and the higher-speed grades require optical fiber cables. SONET/SDH is the most popular protocol for data transfer on these backbones. Data that flows over SONET can be in the form of Asynchronous Transfer Mode (ATM) or Packet over SONET (PoS).

Packet switching networks define endpoints but not the routes. IP networks are built from packet switching, with the Internet being the prime example. Protocols such as X.25, Frame Relay, and ATM, which are used on packet switching networks, are described in this chapter.

The Internet is an internetwork or group of internetworks that consist of predominantly TCP/IP traffic. The connection points of the Internet are Internet Exchange Points (IPX). The Internet2 Network, a high-speed next-generation 10 Gbits/s backbone, and the capabilities it enables, are briefly described.

# What Is a WAN?

A Wide Area Network, or WAN, is a network of networks, or internetwork, that has a broad geographical reach. WANs link Local Area Networks (LANs) together through the use of links maintained by a public service provider. When a WAN is confined to a small geographical area such as a business park or university, it is sometimes referred to as a *Campus Area Network* (CAN). WANs defined by their coverage of a city are called *Metropolitan Area Networks* (MANs). The name WAN is often used interchangeably with CAN or MAN to indicate the multi-network aspect of the internetwork. The telephone system is a WAN. The Internet is the ultimate example of a WAN.

There are two essential aspects of WAN technology that you need to be familiar with. The first is the manner in which LANs are linked and data is transferred, the connection type. When an interconnection is high capacity, it is call a *backbone*; the term is also applied to any circuit within a LAN that offers high capacity. The second function is switching and routing. Routers are used throughout networks, but the routers at the boundaries of networks, edge routers, are essential to determining the characteristics of a WAN. This chapter describes the various network protocols for the ISO/OSI Data Link layer and Session layer protocols (Levels 2 and 3).

Connections can be made over a variety of media and using a variety of different protocols. A key differentiation is whether the WAN uses the concept of a state in the form of a circuit or path and a mechanism for switching paths as the need arises; this is referred to as a *circuit switching network*. As a rule, the need to create dedicated circuits makes this type of network more expensive than networks where virtual circuits that are constructed on the fly are used.

Alternatively, a WAN can use a stateless mechanism where only the endpoints of the connection are defined and the route or path through the system is determined by an intelligent routing function. This type of WAN is a *packet switching network*, a packet being an encapsulation technique for data of different types. Similar to packet switching is cell relay technology. In a cell relay network, data and its formatting and addressing are divided into small, fixed-length data called *cells*, which are then sent over a switching or virtual circuit.

WANs can be divided into four broad categories:

- **Circuit Switching**. This is the type of WAN used by the phone company. It uses dedicated circuits between endpoints. There is overhead involved in provisioning the connection. Protocols that use this type of network include PPP (dial-up), ISDN, and DSL.
- **Packet Switching**. A packet switching WAN creates virtual circuits to send packets from one host to another, which allows many systems to share the same links. Transmission can be unicast (point-to-point) or multicast (point-to-multiple points). Protocols of this type include X.25, Frame Relay, and PoS.
- **Cell Relay**. Cell relays are similar to packet switching but use smaller fixed-length cells for data transport. The technology relies on synchronization techniques, which tend to make this slower due to overhead. The protocol most associated with cell relay is ATM.
- **Leased Line**. A leased line is a dedicated connection between two endpoints. Because traffic must come from a defined source and go to a defined destination, these WAN links are secure, often fast, and tend to be expensive. Lease lines use Data Link protocols as their control mechanisms.

No single network type dominates all WAN technology. The mixture is a compromise of cost, distance, reliability, and complexity. As a result, a host of technologies have been employed to enable WAN connections. Many were designed for the telephone company and then adapted to provide data services. Some technologies were fresh attempts to create high-speed networks. Others aimed at providing new services while retaining backwards compatibility to older standards.

# Circuit Switching Networks

Circuit switching networks were the first type of WANs to be widely used. They arose from networks that carried voice communication, were analog, and generally involved low data throughput. The telephone system is the best example, but even earlier, you could consider telegraph lines to be a circuit switching network. Circuit switching networks today transfer both analog and digital data through a defined connection path. A network can also assign circuits to individual paths to an endpoint; that kind of network is referred to as a *dedicated circuit network*, as shown on the right in [Figure 13.1](ch13.html#virtual_circuits_versus_dedicated_circui). Alternatively, a network can create circuits as required from a set of available potential connections, which is referred to as a *virtual circuit network* (as shown on the left in [Figure 13.1](ch13.html#virtual_circuits_versus_dedicated_circui)). The dedicated circuit is a set of defined stateful connections, whereas the virtual circuit creates circuits on the fly and tears them down when the data is passed through those connections.

[Figure 13.1](ch13.html#virtual_circuits_versus_dedicated_circui) shows the difference between these two network types. LANs can connect to the service provider using modems, multiplexers, channel service units (CSUs), or data service units (DSUs). CSUs and DSUs are network interfaces to the WAN.

Circuit switching networks build a circuit between two endpoints prior to data transfer; they use a cloud architecture where the path through the network can be drawn from a pool of available possible connections. Data is sent and received over that path, which is also referred to as a *channel*. Even though multiple data sources can be multiplexed so that they can be delivered on the same circuit over different channels, all circuit switching networks suffer from a certain degree of inefficiency due to the fact that some connections and channels are always idle. Weighted against that deficiency is the fact that a named connection imparts a certain guarantee of service without, or perhaps in addition to, any higher-level protocols that are used.

Some packet switching networks, which are covered later in this chapter, can behave as if they are circuit switching networks by creating a virtual circuit.

There is a latency involved with circuit setup (the call) and teardown that must be suffered over a circuit switching network. Most higher-speed circuit switching networks use control signals over a dedicated channel or channels to manage traffic, but it isn't a prerequisite. Low-speed networks, such as the plain old telephone service (POTS), do not reserve channels for signaling or data control.

![Virtual circuits versus dedicated circuits in a circuit switching network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1301.png)

**Figure 13.1. Virtual circuits versus dedicated circuits in a circuit switching network**

## The Public Switched Telephone Network

Digital service networks also allow circuit switching networks (such as POTS) to interoperate with packet switching networks such as TCP/IP. Both networks can be used for telephony, but their requirements are different.

The network of circuit switching telephone networks is referred to as the *Public Switched Telephone Network*, or PSTN. PSTN interoperability is governed by the ITU-T standard; the telecommunications numbering plan that codifies telephone numbers uses the ITU-E.164 standard.

In the United States, the telephone network was controlled by AT&T until the early 1980s. AT&T organized the U.S. telephone network into a hierarchical structure that included five levels or classes. The telephone exchange represented the three-digit prefix for a seven-digit phone number, and was managed from end offices in Class 5. There were approximately 20,000 end offices at that time. Toll centers in Class 4 concentrated exchanges into primary centers in Class 3, where area codes were managed. Further concentration occurred in Class 2 Sectional centers, finally ending up at a regional center in Class 1. Class 1 centers were connected to the International Gateway Exchange. Each of these different office levels are switching centers. These categories are shown in [Figure 13.2](ch13.html#the_original_atat_network_system_archite).

On January 1, 1984, AT&T was broken up to create the Regional Bell Operating Companies (RBOC), a set of seven companies called the Baby Bells. The original companies were:

- Ameritech
- Bell Atlantic
- BellSouth
- NYNEX
- Pacific Telesis
- Southwestern Bell
- U S West

There were two additional Bell System members that were non-RBOC companies: Cincinnati Bell and SNET, both of which AT&T owns minority interests in.

This breakup altered the nature of the Class 1 to 3 layers of the AT&T network so that today these layers aren't particularly relevant to phone internetwork architecture. Class 4 and Class 5 are still in use. After the breakup, the RBOCs worked together to create a number of new networking protocols that they could use as a group. Many of them were created by Bellcore.

### Note

To read about the divestiture and evolution of the Regional Bell Operating Companies in more detail, go to `http://en.wikipedia.org/wiki/Bell_System_divestiture`.

Today the United States phone network has undergone considerable consolidation, and the following companies exist:

- **AT&T**. This was originally Southwestern Bell, which acquired AT&T and renamed itself. It also acquired BellSouth.
- **Qwest**. U S West was acquired by Qwest.
- **SBC**. Southwestern Bell changed their name to SBC and acquired Ameritech and Pacific Telesis.
- **Verizon**. They were originally Bell Atlantic and changed their name. They acquired GTE and NYNEX.

![The original AT&T network system architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1302.png)

**Figure 13.2. The original AT&T network system architecture**

In a circuit switching network, a connection is made between two hosts as endpoints that remain in place while data is transferred. Depending upon network conditions, that circuit would likely be different every time you made a connection, but it would stay intact for the duration of the exchange. Circuit switching networks are stateful, and so their capacity is limited by the number of circuits that a system has. Each physical circuit has a limited number of connections that it can support, which can be large, but is limited.

On a packet switching network, data is fragmented and packaged into packets, and a virtual connection is made between two hosts as endpoints. The path that any single packet uses to travel to its destination is not important and can be individually different; what matters is the faithful reassembly of the data by the host. A packet switching network is stateless; their capacity is limited by the speed of the data transmission and by the efficiency of the methods used to encode the data.

The next two sections describes two of the more commonly used technologies for connecting networks to circuit switched networks: Integrated Services Digital Network (ISDN) and Digital Subscriber Line (DSL). Cable networks are also covered.

## Integrated Services Digital Network

An Integrated Services Digital Network, or ISDN, is a telephone network service that is a means of sending digital data over circuit switching telephone networks. ISDN allows phone companies to support both voice and data communications over the same lines, thus making it an integrated service. When purchasing an ISDN connection, the user purchases data pipes in 64 Kbits/s slices; with IDSN, connections to the Internet are typically 128 Kbits/s in both directions.

ISDN connects to the PSTN network through either an ISDN modem or a network terminator (NT-1 or NT-2) and a terminal adapter (TA). The network terminator serves the function of a hub, and the TA serves the function of a NIC for the connection. ISDN is a dial-up technology; when you want to access the network, the ISDN modem dials the service and connects to the remote router, providing its Service Profile Identifier (SPID).

ISDN was one of the earliest forms of broadband connections for the home market but required that the customer be within 18,000 ft (3.4 mi or 5.5 km) of a central phone office. At distances farther than that, a repeater must be used, which makes the cost of providing the service to individual consumers expensive.

ISDN networks defined the following three interfaces:

- **Basic Rate Interface (BRI)**. A 144 Kbits/s connection to copper telephone wire, BRI is segmented into two 64 Kbits/s data-bearing channels (B channels) and one 16 Kbits/s control or signal channel (Delta or D-channel). This format can be found in two- and four-wire connections, as a serial connection to a digital modem, or between a device and a TA.
- **Primary Rate Interface (PRI)**. This is a 1,544 (23B) or 2,048 (30B) Kbits/s service that is carried over either T1 or E1 networks, respectively, using a single D-channel for its signal control path. PRI is used worldwide and is often used to connect the telephone network to PBX systems.
- **Broadband Integrated Services Digital Network (B-ISDN)**. This was developed as an extension of ISDN in the 1980s. At the time, it was devised to support sending multimedia content such as video on demand and television, and as a high-speed data service for companies and scientific organizations such as universities and research labs. B-ISDN uses ATM for switching and SONET for high-speed networking. Neither ISDN nor B-ISDN achieved market success. B-ISDN is rarely used these days by any carriers.

ISDN can aggregate B channels into what are called *H channels*, as follows:

- H0 aggregates 6 B channels to 384 Kbits/s
- H10 aggregates 23 B channels to 1.47 Kbits/s
- H11 aggregates 24 B channels to 1.54 Kbits/s
- H12 aggregates 30 B channels to 1.92 Mbits/s

H12 is only available on E1 networks, mostly in Europe.

When ISDN was introduced in the 1990s, it was expected by the telephone industry to be the way most consumers would connect to the Internet. It did achieve some success in the United States, and more success in Europe, but nothing compared to early expectations. The PRI interface is widely used for telephone communications on telephone networks themselves, but the BRI circuits, which were optimized for data transfers, are more expensive and less popular than Digital Subscriber Line (DSL).

All of the forms of ISDN described in this section fall under the category of narrowband ISDN (N-ISDN). That differentiates these technologies from broadband ISDN (B-ISDN), which was discussed previously.

## Digital Subscriber Line

Digital Subscriber Line, or DSL (originally Digital Subscriber Loop), is one of the most popular methods in use today for connecting to the Internet through the phone system, rivaled only by cable modems offered by digital cable TV networks, and perhaps WiMax (802.16) in the future. DSL was introduced in 1998 and has largely replaced ISDN.

The most common version of DSL in use is Asymmetric DSL (ADSL), but occasionally Symmetric DSL is encountered. ADSL operates at anywhere from 256 Kbits/s up to 6.31 Mbits/s, the speed of which is a function of the level of service you purchase from a provider and the line condition. Speeds are more typically found in a range between 512 Kbits/s and 1.54 Mbits/s for downloads and 128 Kbits/s for uploads. The assumption made with ADSL is that most of the time, users want to download information. By skewing the line so that downloads are faster, the service provider is speeding up the overall service and improving customer satisfaction.

One important factor that influences DSL is the distance that the subscriber is from the repeater or local office. DSL requires that the subscriber be within 18,000 ft (3.4 mi or 5.5 km) of a central phone office, which is the same requirement that ISDN has. This distance can be extended by the phone company if they install an optical fiber cable from the repeater or office to the loop. The phone company can also install bridge taps to increase the service length of their DSL loops. Another factor in performance is the quality of the copper wire; larger gauges are better because there is less loss to resistance.

With ADSL, the download speed is faster than the upload speed, while for SDSL, the speed in both directions is about the same. DSL first appeared over ISDN lines, a technology that is now referred to as IDSL. ADSL can not only be used on a telephone line but also works on an ISDN connection using BRI circuits.

DSL operates over the local loop on a phone line (plain old telephone system, or POTS) by sending data at a higher frequency than voice does. That higher frequency means that it doesn't interfere with voice data when they are both sent down the line to a DSL Terminal Adapter (commonly called a DSL modem). A DSL modem is more properly called an ATU-R transceiver and can connect to a firewall, router, or gateway, or a computer using either its Ethernet or USB connection. In most instances, people opt to use the Ethernet connection.

Typically, voice is below 4 kHz and data is above 24 kHz. To ensure that data transmission doesn't affect the phones connected on the same phone loop, a low-pass DSL filter is placed between any phone and the wall connection. This filter screens out all signals above 4 kHz (the upper limit of DS0, the voice band).

Some DSL types require the installation of a splitter, while others do not. The terms DSL Lite, G.Lite, and Universal ADSL refer to splitterless DSL technologies that can be split in the telephone office. For systems that require splitters, there are two main methods used. The Carrier Amplitude/Phase (CAP) system shown in [Figure 13.3](ch13.html#the_carrier_amplitude_solidus_phase_open) divides the phone signals into three bands:

- Conversations are carried in the 0 to 4 kHz band (just like POTS).
- The upstream channel is carried over the 25 to 160 kHz band.
- The downstream channel (from the server to the user) begins at 240 kHz and goes up to a point that varies, depending on a number of conditions (line length, line noise, number of users in a particular telephone company switch) but has a maximum of about 1.5 MHz.

An alternative, called the *Discrete Multitone* (DMT) system, uses an entirely different scheme, as shown in [Figure 13.4](ch13.html#the_discrete_multitone_splitter_system). DMT divides the spectrum into 247 equal 4 kHz channels and then monitors each channel to ensure that the signal on that channel is good. As conditions change, DMT moves signals to different channels to optimize throughput and quality. The lower frequencies in the spectrum around 8 kHz are used for bidirectional traffic. CAP requires a lot of processing to operate, but makes much more efficient use of the bandwidth than the MDT system does. Most ADSL providers use the DMT systems on their lines.

![The Carrier Amplitude/Phase (CAP) splitter system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1303.png)

**Figure 13.3. The Carrier Amplitude/Phase (CAP) splitter system**

![The Discrete Multitone splitter system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1304.png)

**Figure 13.4. The Discrete Multitone splitter system**

[Table 13.1](ch13.html#dsl_types_and_characteristics) summarizes the different forms of DSL that are available worldwide, along with their speeds, requirements, and limitations.

As cellular technologies become more popular, more people in the United States are choosing not to have landline phones in their homes. This has led the Federal Communications Commission (FCC) in the U.S. to mandate that telephone companies provide DSL service, regardless of whether phone service is chosen. The use of a phone line for DSL without a phone is referred to as either *dry-loop DSL* or *naked DSL*.

**Table 13.1. DSL Types and Characteristics**

| DSL Type | Description | Data Rate (Downstream, Upstream) | Distance Limit | Application |
| --- | --- | --- | --- | --- |
| Source: `http://whatis.techtarget.com/definition/0,,sid9_gci213915,00.html`. |  |  |  |  |
| **ADSL** | Asymmetric Digital Subscriber Line | 1.544 to 6.1 Mbits/s downstream; 16 to 640 Kbits/s upstream | 1.544 Mbits/s at 18,000 feet; 2.048 Mbits/s at 16,000 feet; 6.312 Mbits/s at 12,000 feet; 8.448 Mbits/s at 9,000 feet | Used for Internet and Web access, motion video, video on demand, and remote LAN access. |
| **CDSL** | Consumer DSL from Rockwell | 1 Mbit/s downstream; less upstream | 18,000 feet on 24 gauge wire | Splitterless home and small business service; similar to DSL Lite. |
| **DSL Lite (G.Lite)** | "Splitterless" DSL without the "truck roll." *Truck roll* is the use of a dispatched truck and technician to install or modify equipment on site. | From 1.544 Mbits/s to 6 Mbits/s downstream, depending on the subscribed service | 18,000 feet on 24 gauge wire | The standard ADSL; sacrifices speed for not having to install a splitter at the user's home or business. |
| **HDSL** | High bit-rate Digital Subscriber Line | 1.544 Mbits/s duplex on two twisted-pair lines; 2.048 Mbits/s duplex on three twisted-pair lines | 18,000 feet on 24 gauge wire | T1/E1 service between server and phone company or within a company; WAN, LAN, server access. |
| **IDSL** | ISDN Digital Subscriber Line | 128 Kbits/s | 18,000 feet on 24 gauge wire | Similar to the ISDN BRI service, but data only (no voice on the same line). |
| **RDSL** | Rate-Adaptive DSL from Westell | Adapted to the line, 640 Kbits/s to 2.2 Mbits/s downstream; 272 Kbits/s to 1.088 Mbits/s upstream | Not provided | Similar to ADSL, the speed varies based on the length and quality of the phone line. |
| **SDSL** | Symmetric DSL | 1.544 Mbits/s duplex (U.S. and Canada); 2.048 Mbits/s (Europe) on a single duplex line downstream and upstream | 12,000 feet on 24 gauge wire | Same as for HDSL but requiring only one twisted-pair line. Requires exclusive use of the phone line for data, and so is mostly used for dedicated DSL. |
| **UDSL** | Unidirectional DSL proposed by a company in Europe | Performance of UDSL is somewhere between ADSL and VDSL at longer distances;four times VDSL at short distances in some locations | Not known | Similar to HDSL. Introduced by Texas Instruments, this is a relatively new format. |
| **VDSL** | Very high Digital Subscriber Line | 12.9 to 52.8 Mbits/s downstream;1.5 to 2.3 Mbits/s upstream; 1.6 Mbits/s to 2.3 Mbits/s downstream | 4,500 feet at 12.96 Mbits/s;3,000 feet at 25.82 Mbits/s; 1,000 feet at 51.84 Mbits/s | ATM networks;fiber to the Neighborhood. Very fast, but works over short connections. |

DSL can be used on either bridged networks or routed networks; of the two, bridged networks are more common in homes. On a bridge network, a group of subscribers in the same locale share a single subnet. When traffic is high, bandwidth to individuals can be affected. To prevent this, DSL providers tend to implement usage limits; the higher-speed versions of DSL that are more likely to be used by businesses, such as HDSL and VDSL, tend to be routed networks. In these instances, DSL is more likely to be connected to DSL routers or DSL gateways, which add features such as routing control, firewalls, and other services.

As local loops of DSL subscribers are aggregated, they are connected to the backbone networks of the telephone network by connecting to a Digital Subscriber Line Access Multiplexer (DSLAM). This device typically is placed in phone company offices, and multiplexes the input of multiple DSL loops into ATM, Frame Relay, or IP protocols. Some DSLAMs offer a mixture of multiplex conversions. DSLAMs are required on both ends of the communication, so that at the receiving end there must be a DSLAM to demultiplex the signals and route them.

Unlike the case with cable modems, where users share a common connection and are therefore affected by their neighbors' usage, ADSL provides a dedicated connection from the user to the DSLAM. The performance of one ADSL user does not impact the performance of another user on the same loop.

## Cable network

Cable modem Internet connections are often compared to DSL services. Cable companies use hybrid fiber coaxial cable (HFC) networks to provide both fiber and coaxial connections to the customer. The coaxial portion carries the television service, and the fiber optical cable carries the data connection. Cable modems generally follow the Data over Cable Service Interface Specification (DOCSIS) standard, but implementations vary by cable provider.

Cable networks are shared multipoint circuits, which means that data is shared over the particular circuit. Security can be an issue on these networks, as your data is potentially viewable by neighbors. The performance of cable modems can be theoretically as high as 27 and 35 Mbits/s downstream, and 2 to 10 Mbits/s upstream. With typical loading, a cable modem usually performs around 2 Mbits/s downstream and 200 Kbits/s to 2 Mbits/s upstream. Cable networks' WAN features use the other technologies described in this chapter.

# T- and E-Carrier Networks

Both circuit switching and packet switching networks use the concept of a channel to increase the capacity of the network. A channel is a path over a transmission medium that is either physically separated by using a multi-wire cable, or electrically separated by applying techniques such as Time Division Multiplexing (TDM, or time slicing) or Frequency Division Multiplexing (FDM). FDM over optical media is called *Optical Division Multiplexing* or *Wavelength Division Multiplexing* (WDM), which separates light with a diffraction grating.

With FDM, the available frequency spectrum is divided into discrete ranges, and all of these ranges become logical channels. AM radio provides an example of FDM, with each station representing a channel. Some countries allow AM band radio stations to create logical channels on the same frequency and to switch rapidly between the channels, which is an example of TDM. When you use Stereoscopic Liquid Crystal shutter glasses to view 3D video, the screen rapidly displays right and left images sequentially, an example of a two-channel TDM technology.

The L-carrier and coaxial cable connections used in mid-twentieth-century telephone networks could carry thousands of multiplexed voice connections over long distances using FDM. Over shorter distances, Bell used twisted-pair cables, such as the Bell System K- and N-Carrier media, that could enable 12 (double sideband) or 24 (single sideband) connections over four wires. To ensure signal quality, twisted-pair media required that the signal be amplified by repeaters every 10 km (6 mi) or so. DSL's use of Discrete Multitone (DMT) frequency switching is another example of FDM.

Modern telephone networks tend to use TDM. TDM is the method used in the Pulsed Code Modulation (PCM) systems, which are also referred to as Plesiochronous Digital Hierarchy (PDH) systems. PCM is the technology used on most digital networks today.

On a T1 line that uses the DS1 format, the T1 carrier is composed of 24 multiplexed channels. The point at which an analog signal is translated to a digital signal in the phone network is called a *codec*. Although different codecs multiplex in different ways, a common scheme is to have the different analog signal sampled consecutively and then interleaved into channels 1 to 24. The entire set of channels is then packaged into a frame, and that frame is then transmitted. The size of a frame is a function of the technology used. For an 8-bit signal, the frame would be 192 bits, plus one extra bit for framing code, or 193 bits. At a frequency of 125 μsec, the data rate would be 1.54 Mbits/s. An E1 line, by comparison, transmits 32 channels of 8-bit data sampled at a data rate of 2.05 Mbits/s and reserves of these channels for synchronization when data is transmitted instead of sampled audio.

As telephone lines converge, multiple T1 streams can be consolidated into higher carrier formats through the use of TDM. The scheme used in the United States is as follows:

- A stream of four T1 lines running at 1.54 Mbits/s concentrated into one line would form a T2 stream with a data transfer rate of 6.31 Mbits/s.
- When you concentrate six T2 streams into a single stream, you form a T3 stream that transfers data at the rate of 39.96 Mbits/s.
- Finally, seven T3 streams can be concentrated into a single T4 stream that would run at 274.18 Mbits/s.

[Figure 13.5](ch13.html#consolidating_t1_streams_into_higher_ord) illustrates this progression.

![Consolidating T1 streams into higher order carriers](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1305.png)

**Figure 13.5. Consolidating T1 streams into higher order carriers**

In Europe, the standard high-speed interconnect is called an *E-carrier*. It's a standard of the European Conference of Postal and Telecommunications Administrations (CEPT) and is analogous to the T-carrier standards used in the United States. T-carrier is a standard of the ITU-T. [Table 13.2](ch13.html#t-_and_e-carrier_speeds) compares T-carrier and E-carrier lines. E1 and E3 are the versions that are in common use, with E1 typically run over twisted-pair cables.

**Table 13.2. T- and E-Carrier Speeds**

| T-Carrier Level | E-Carrier Level | DS Level | Throughput | Voice Channels(Circuits) |
| --- | --- | --- | --- | --- |
| T-carriers are used in the U.S.; E-carriers are used in Europe. FT1 stands for Fractional T1 line. |  |  |  |  |
| FT1 | E0 | DS0 | 64 Kbits/s | 1 |
| T1 |  | DS1 | 1.54 Mbits/s | 24 |
|  | E1 |  | 2.05 Mbits/s | 30 |
| T2 |  | DS2 | 6.31 Mbits/s | 96 |
|  | E2 |  | 8.45 Mbits/s | 120 |
|  | E3 |  | 34.37 Mbits/s | 480 |
| T3 |  | DS3 | 44.38 Mbits/s | 672 |
|  | E4 |  | 139.27 Mbits/s | 1,920 |
| T4 |  | DS4 | 274.18 Mbits/s | 4,032 |
|  | E5 |  | 565.15 Mbits/s | 7,680 |

In digital telephone networks, PCM is used to carry multiple calls of four-wire, twisted-pair copper cables (either E-carrier or T-carrier) or fiber optic cable. Synchronous Digital Hierarchy (SDH) networks and the related, better-known Synchronous Optical Networking (SONET), use TDM to transmit over optical fiber. SONET is important for trunk lines on the Internet, as it allows several ISPs to transmit over the same optical line. The wireless GSM telephone system also uses TDM technology.

# Synchronous Optical Networking

Synchronous Optical Networking, or SONET, is a high-speed TDM Physical Layer or wire standard (like the Internet Protocol). It is used for sending telecommunications data in the form of light over fiber optic cables on a circuit switching network. The digital data is created by pulsed lasers or by light emitting diodes (LEDs). SONET is used in the telephone system for their trunk lines, and with the use of a SONET chipset and an adapter board, you can connect a computer to a SONET network.

SONET arose from research done by the Baby Bell company Bellcore in 1985. A few years later, the CCITT's (International Telegraph and Telephone Consultative Committee) version of SONET became known as Synchronous Digital Hierarchy, with only a few additional extensions added. SONET is used in North America, while SDH is used worldwide, and the two can be used over the same network.

SONET/SDH also specifies wire standards for bitrates, jitter, isolation, and signal correction, as well as a set of network management protocols such as the TL1 telecom language. SONET/SDH devices are managed using framework applications with SNMP or another management protocol.

### Note

Frame Relay, ATM, and Packet over SONET are each described in more detail in their own sections in this chapter.

SONET was designed to send voice data that could completely fill an entire 64 Kbits/s segment. With data of variable sizes such as packets, the TDM time slicing fills whatever remains in a DS0 segment with arbitrary data when the circuit isn't 100 percent utilized, leading to inefficiencies. The solution to this problem was the development of Frame Relay technology, which used statistical multiplexing to combine data and fill the SONET segments.

Frame Relay doesn't provide satisfactory QoS services and can't support higher-speed networks. To solve these problems, carriers have turned to ATM, which has enough QoS to provide connection quality and which could scale over fiber optic carriers. ATM is currently used on most SONET networks and satisfies the requirements of the slower optical carriers. However, on faster carrier grades, ATM suffers from overhead associated with translation of other transport protocols, such as Ethernet, into its cell structure. When a frame doesn't coincide with a cell boundary, the rest of the cell is padded to fill the cell; this creates an overhead called *cell tax*. At high speeds, ATM's efficiency falls off.

On the higher-speed optical networks that will be the WAN backbones of the future, the expectation is that ATM will be deprecated in favor of the PoS protocol. ATM and PoS can run on the same SONET network, as they are not mutually exclusive.

## SONET architecture

SONET networks are implemented as a ring structure. A SONET connection is called a *path*, and each part of the connection is called a *section*. In order to keep the signal strength high, repeaters are used. The system relies on signal multiplexers at the sending and receiving ends at a minimum, and if different networks connect, at the point of connection. Each connection between a multiplexer is called a *line*. [Figure 13.6](ch13.html#a_sonet_path_comma_line_comma_and_sectio) shows a diagram of a path.

![A SONET path, line, and section](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1306.png)

**Figure 13.6. A SONET path, line, and section**

SONET/SDH uses three different network topologies (see [Figure 13.7](ch13.html#sonet_topologies)):

- **Linear Automatic Protection Switching (LAPS)**. APS or 1+1 has two pairs of bi-directional fibers. Switching is done on a line-by-line basis, based on negotiation.In [Figure 13.7](ch13.html#sonet_topologies), the arrows indicate the direction of the path. The primary path is shown as a black line with a black arrow; the secondary or failover path is shown as a dotted line with a white arrow. The LAPS circuit contains two failover switches that route traffic over the alternate path when failure occurs.
- **Unidirectional Path Switched Ring**. SONET UPSR consists of redundant data paths sent around a ring structure. One circuit is working and one is standby, with both in the same direction. When the working circuit is interrupted, the standby circuit takes over. In SDH, the analogous technology is called Subnetwork Connection Protocol (SNCP), but is a mesh instead of a ring.
- **Bidirectional Line Switched Ring**. BLSR is a two- or four-fiber network with a ring structure that transmits redundant information. In the two-fiber configuration, each ring is both working and standby, with one circuit being the data channel and the other being the redundant path. In BLSR both rings are in use, both working and standby, whereas in unidirectional one ring is in standby mode.

## Framing

SONET circuits transfer data at a steady rate in multiples of 64 Kbits/s. A 64 Kbits/s segment is referred to as a *DS0 line*, and that is the standard throughput of a voice phone wired into homes.

The synchronization feature in SONET is maintained by a system of atomic clocks located throughout the system. Data travels over the SONET network as a collection of frames with encapsulated data such as Asynchronous Transfer Mode (ATM) or Packet over SONET/SDH (PoS), with the definition of the frames being slightly different for the two different versions of this standard.

SONET data is heavily multiplexed and can mix different communication types together into a virtual path envelope (container). SONET STS-1 (Synchronous Transport Signal Level - 1) operates at 51.84 Mbits/s, while the equivalent SHD standard STM-3C (Synchronous Transport Module - 3, concatenated) operates at three times the speed, at 155.52 Mbits/s. The main difference between SONET and Ethernet T1-4 streams is that SONET has a lower latency passing through switching equipment. For T1, that latency is 125 μsec, while for SONET/SDH the latency is 32 μsec. When SONET/SDH data travels over optical cable, the term OC-1 is used in place of STS-1, and the signal is in the OC-N format. An OC-3 standard contains three streams of STS-1 data.

### Note

An octet is a group of 8 bits. A byte is often 8 bits, but not always. Often both terms are used interchangeably.

![SONET topologies](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1307.png)

**Figure 13.7. SONET topologies**

[Chapter 17](ch17.html) discusses the structure of TCP packets, where a packet consists of a header portion with multiple sections followed by the TCP data as the payload. SONET frames use a different structure, where the overhead portion of the frame is interwoven with the data or payload. SONET and SDH use slightly different frame structures. Taking SONET STS-1 as an example, a frame consists of 810 octets, with a pattern of 3 octets of overhead followed by 87 octets of payload repeated nine times. For STM-3, the pattern components are three times larger. [Figure 13.8](ch13.html#an_810-octet_sonet_frame) shows a SONET frame.

![An 810-octet SONET frame](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1308.png)

**Figure 13.8. An 810-octet SONET frame**

The synchronization feature is such that every 125 μsec, a frame passes by a specific point on the network, and at 8-bit/125 μsec, the transfer rate would be 64 Kbits/s, the DS0 standard. Because both standards use the same clock rate, the signals from SONET and SHD are interoperable. [Table 13.3](ch13.html#sonet_solidus_sdh_standards_versus_carri) shows the different SONET/SDH speeds, which are obtained by concentrating the following streams:

1. Three STS-1 lines are sent through a 3:1 multiplexer and one STS line is output.
2. Four STS-3 lines are sent through a 4:1 multiplexer and one STS-12 line is output.
3. One STS-12 line is sent through a scrambler.
4. The output from Step 3 is sent through an electro-optic converter.
5. An OC-12 signal is sent down the fiber.

Refer to [Figure 13.5](ch13.html#consolidating_t1_streams_into_higher_ord) for an example of how multiple lines are concentrated for higher levels of throughput using T standard lines.

**Table 13.3. SONET/SDH Standards versus Carrier Levels**

| SONET Optical Carrier Level | SONET Frame Format | SDH Frame Format | Bandwidth (Kbits/s) | Throughput (Kbits/s) |
| --- | --- | --- | --- | --- |
| OC-1 | STS-1 | STM-0 | 50,112 | 51,840 |
| OC-3 | STS-3 | STM-1 | 150,336 | 155,520 |
| OC-12 | STS-12 | STM-4 | 601,335 | 622,080 |
| OC-24 | STS-24 | - | 1,202,688 | 1,244,160 |
| OC-48 | STS-48 | STM-16 | 2,405,376 | 2,488,320 |
| OC-192 | STS-192 | STM-64 | 9,621,504 | 9,953,280 |
| OC-768 | STS-768 | STM-256 | 38,486,016 | 39,813,120 |
| OC-3072 | STS-3072 | STM-1024 | 153,944,064 | 159,252,240 |

At the moment, the highest transfer rate commonly available with this kind of technology is OC-192 or STM-64, which can attain transfer rates of up to 10 Gbits/s. This is comparable with Gigabit Ethernet. STM-256, operating at 40 Gbits/s, is being introduced. To attain higher speeds, SONET data can be made to travel over several different wavelengths on a fiber pair using technology called *Wavelength Division Multiplexing* (WDM). The undersea fiber optic cable laid in quantity during the 1990s used a form of WDM called Dense Wave Division Multiplexing (DWDM).

## Packet over SONET

Packet over SONET, or PoS, is a packet transport protocol that uses a Point-to-Point (PPP) connection. It is anticipated that PoS will become the dominant transport over SONET/SDH over backbone fiber optic networks that run at high speed. This standard was developed by Cisco Systems, is supported by their high-speed routers, and is enabled in hardware. A significant amount of PoS traffic runs on OC-192 SONET rings.

PoS is a Data Link level (Layer 2) protocol in the ISO/OSI network model. PoS packets are encapsulated in SONET frames, and technology provides for alarm levels, performance monitoring, reliability switching, and synchronization. The PoS packet format makes it much easier to integrate Ethernet IP traffic into PoS frames, with lower header overhead.

PoS can run over SONET networks concurrently with TDM voice and ATM, provided that they use different time slots and suffer no contention. This independence has a number of benefits. For example, ATM can be used to provision Digital Subscriber Lines (DSL), digital cable, and traffic over Permanent Virtual Circuits (PVC) or Switched Virtual Circuits (SVC). All of these different inputs to ATM can be aggregated by ATM to the PoS routers, which then feed the input to the IP backbone optical fiber network. A Cisco 12000 series router is capable of ATM – PoS translation. [Figure 13.9](ch13.html#aggregating_atm_traffic_to_a_pos_router) shows this aggregation process.

Notice in [Figure 13.9](ch13.html#aggregating_atm_traffic_to_a_pos_router) that the Point of Presence (POP) links between the PoS and ATM routers are made into a fabric and are redundant. POP, being a point-to-point technology, is subject to failure and needs to be made redundant in order to ensure reliability. Backbone traffic is mission critical and cannot fail.

PoS routers can be connected to backbones in the following ways:

- Through a SONET multiplexer
- Through a Dense Wavelength Division Multiplexer (DWDM)
- Directly to a dark fiber backbone

When dark fiber is used, a laser or LED must be provided at the sending end, and a photodiode receiver must be provided at the receiving end. If the run is long enough, a SONET regenerator needs to be added in the line. An example of a SONET optical regenerator for an OC-48 backbone is the Cisco 15104. This procedure is given the name "lighting the fiber."

PoS frames have some specific requirements:

- **High order containment**. PoS frames must be properly encapsulated by SONET transport signals.
- **Octet alignment**. The data packet octet boundaries must align to the STS octet boundaries.
- **Payload scrambling**. Data in the payload portion must conform to rules that require a certain density of ones in the data. The requirement is needed for timing recovery and for network synchronization.

The high order containment process does the following three things:

- Encapsulates an IP datagram into a PPP frame
- Encapsulates PPP frames into a High Level Data Link Control (HDLC) frame
- Encapsulates an HDLC frame into a SONET/SDH frame

![Aggregating ATM traffic to a PoS router](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1309.png)

**Figure 13.9. Aggregating ATM traffic to a PoS router**

# Packet Switching Networks

Packet switching networks work by segmenting data into pieces called *packets* that are variable in length and are encapsulated with addressing and formatting information in a header portion of the packet. On a packet switching network, the endpoints for communications are defined, but the route packets taken between those endpoints may or may not be defined, depending upon the technologies used.

### Note

For a list of packet switched networks, go to `http://en.wikipedia.org/wiki/Packet_switched_network`.

Ethernet and the IP protocols are connectionless; the route the packets take is irrelevant. Some packet switching technologies use virtual circuits, while others may use permanent virtual circuits. The protocols that use connections are TCP (described in [Chapter 17](ch17.html)), X.25, ATM, and MPLS, all of which are described in the sections that follow.

Packets are created in a certain order or sequence, and they need to be reassembled in that sequence. To ensure that packets are correctly assembled, packet switching protocols use a number of different mechanisms. Each packet carries a sequence identification, and packet switching networks usually employ a messaging system when a packet needs to be re-sent. The validity of the packets is determined by error-checking mechanisms, at the end of each segment of the route and/or the point at which the data is reassembled (the endpoint).

Packet switching can employ an additional data construct called a *datagram*. Datagrams are part of a packet, a collection of packets, or some combination that is encapsulated within an envelope used to send and control the data communications. Multiprotocol Label Switching (MPLS) is one technology that uses datagrams.

Packet switching has an advantage over circuit switched networks in that it can more fully utilize network bandwidth. Packets can be routed over segments based on current conditions. The low latency involved in transient and often short connections (such as hops) makes packet switching faster to initiate than circuit switching technologies.

# X.25 Networks

X.25 is a digital packet switching protocol that was developed in the 1970s, prior to the Internet, as an ITU-T standard. X.25 was deployed on telephone grids before being replaced by faster networks that used ISDN, ATM, ADSL, and PoS starting in the 1990s. It has been displaced by the IP protocol. In the OSI model, the X.25 protocol provides services at Layers 1 to 3 (the Physical, Data Link, and Network layers). The Physical layer standard supporting X.25 is X.21.

Today, X.25 is used on legacy networks in developing countries, in Europe in some point-of-sale systems, for GPS tracking, and on wireless packet radio networks, such as the related AX.25 standard. X.25 is therefore largely of historical interest. Networks such as CompuServe, Telenet, Euronet, and Tymnet were built with X.25.

The X.25 architecture creates virtual calls that connect the Data Terminal Equipment (DTE) of the user or subscriber with Data Circuit Terminating Equipment (DCE) on the X.25 network. A DTE is usually a computer or a terminal, while a DCE can be a modem that is connected to the network. To a user, X.25 appears as if it is a point-to-point connection. X.25 defines both switched and permanent circuits — Virtual Calls (VC) and Permanent Virtual Circuits (PVC), respectively.

### Note

DCE is also called Data Communications Equipment or Data Carrier Equipment. It is typically a computer or device that performs signal conversion, encoding, and synchronization.

X.25 networks connected to asynchronous devices such as modems, terminals, and printers by sending data through a gateway device called a Packet Assembler Disassembler (PAD) device. The protocol used by a PAD was defined as X.3, between a terminal and PAD as X.28, and between a PAD and the network as X.29. For this reason, PADs were also called "Triple X" devices. PADs are a common element on all packet switching networks where they mediate the differences between the sending device's speed and the receiving device's speed. PADs must be on both ends of the connection.

X.25 was built to be a reliable data connection, and implemented various mechanisms to ensure that packets arrived correctly and in sequence at their destination. It included features that IP networks have carried forward: error correction, flow control, and messaging. These features limited X.25 to speeds of only 64 Kbits/s or DS0, which is the basic speed for voice data.

# Switched Multi-megabit Data Services

The Switched Multi-megabit Data Services, or SMDS, were developed by Bellcore in the early 1990s as a means for connecting LANs to MANs. At the time, the Regional Bell Operating Companies (RBOCs) could only create networks in a relatively small area that they referred to as *Local Access and Transport Areas* (LATA).

SMDS predates the development of Asynchronous Transfer Mode (ATM). Billed as a connectionless packet switching service, SMDS split datagrams into cells and sent those cells across SONET/SDH rings, allowing MANs to achieve a radius of 30 mi, or 50 km. The technology was part of the IEEE 802.6 standard that included the Distributed Queue Dual Bus (DQDB) technology.

The RBOCs and GTE deployed SMDS in the United States for several years, but the technology never became pervasive. In Europe, SMDS had more success. It was sold in those markets as Connectionless Broadband Data Service (CBDS) and was popular in countries that were both mainly metropolitan and small. However, by the mid-1990s, SMDS was replaced by Frame Relay, and by faster networks that ran Ethernet protocols such as PoE. IEEE has deprecated the 802.6 format, and SMDS is largely of historical interest.

# Asynchronous Transfer Mode

Asynchronous Transfer Mode (ATM) is a medium-speed connection-oriented network protocol. This protocol operates at the Data Link layer (Level 2) to define a data transfer format called a *cell*, and at the Physical layer (Level 1) to define a digital switching technology that connects endpoints together using a virtual circuit. ATM was meant to be a format that could run over both packet switching and circuit switching networks, as its features are compatible with both.

ATM is usually implemented in hardware in switches and NICs, and the technology is central to the SONET/SDH backbone of the telephone network that was described earlier. ATM is also the technology used in Broadband Integrated Services Digital Networks (B-ISDNs), which are widely used for multimedia applications and for ADSL. The cost and complexity of ATM has prevented its use on LANs.

ATM is designed to process real-time data such as voice and video. To do this, the cells that travel over an ATM network are designed to be 53 bytes wide. This uniform, small size results in an evenly spaced, high-speed data stream delivered to the codec that performs the digital-to-audio conversion, or vice versa. Datagrams that travel over ATM, regardless of the size, are broken up into 48-byte chunks, and a 5-byte ATM routing header is added for addressing and sequencing during assembly.

If a cell is lost in transmission or late, the codecs used for real-time processing in segmentation and reassembly (SAR) hardware are designed to transmit silence for audio or the previous frame for video, or to use some other method to make up for the missing data. The small size of the cells means that there is little discernable difference in the output; the missing audio would show up as brief noise, and the missing video frame can't be recognized by the human brain at normal playback speeds. The result of using ATM is that it can reduce jitters to less than 5 percent of a packet switching network at network speeds that were common at the time that ATM was developed.

ATM uses virtual circuits to define a connection. This is implemented as an 8- to 12-bit Virtual Path Identifier (VPI) and a 16-bit Virtual Channel Identifier (VCI) in the cell header. As a cell moves through an ATM network, each switch changes the two identifier values to move the cell along the circuit's route. Unlike TCP/IP, where the route is irrelevant and only the endpoints matter, ATM cells travel the same route, which is why less overhead is needed to manage the data stream.

ATM's developers used slightly different cell headers to separate cells used over WAN links from cells moving within the same LAN. Because LANs don't require the additional network information, the GFC is omitted. However, because ATM is rarely used on IP LANs, most cells use the User Network Interface cell format. [Figure 13.10](ch13.html#the_cell_structure_for_atm_on_wans_open) shows the UNI and NNI side by side.

Even though ATM is a lower-overhead protocol, it does have some mechanism in place to control traffic. ATM contains four bit parameters that enforce transfer rates: Constant Bit Rate (CBR), Variable Bit Rate (VBR), Available Bit Rate (ABR), and Unspecified Bit Rate (UBR). Setting these Quality of Service (QoS) parameters collectively comprises what ATM calls a *traffic contract*. A traffic contract controls the queuing and flagging of cells, which are referred to as *traffic shaping* and *traffic policing*, respectively. The VBR parameter is used by ATM to define burst mode. The receiving system does send a short message to the sending system when the packet arrives correctly.

![The cell structure for ATM on WANs (left) and on LANs (right)](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1310.png)

**Figure 13.10. The cell structure for ATM on WANs (left) and on LANs (right)**

Legend: GFC = Generic Flow Control; VPI = Virtual Path Identifier; VCI = Virtual Channel Identifier; PT = Payload Type; CLP = Cell Loss Priority; HEC = Header Error Control (CRC)

It's been 20 years since ATM was first developed by the ATM Forum and the ITU, and network technology has improved greatly since then. At the current speeds achieved by technologies such as 10 GbE over fiber, the transmission of packets, even full-sized 1600-byte packets, is very fast — on the order of 1.3 (sec. That speed reduces jitter significantly and tends to make ATM very expensive to implement. On high-speed IP backbones over optical fiber operating at speeds greater than OC-3, the common technology used for data transfer is Packet Over Ethernet (PoE). Although ATM will be used for many years to come, it is clear that other technologies will replace it on high-speed backbones of the future.

# Frame Relay

A Frame Relay service (see [Figure 13.11](ch13.html#a_frame_relay_system)) is a virtual leased line that provides a point-to-point connection between two network nodes, or between a set of nodes at two different sites. Frame Relay is a Layer 2 Data Link protocol. In a Frame Relay system, frames are routed from one node to the other based on the logic of the router or switch. The frame forwarding system operates like a relay race in the sense that frames are sent to the destination in a series of intermediate steps. Frame Relay systems are popular for sending voice and data between LANs over a WAN connection.

A DCE, or Data Circuit terminating equipment, is a modem, switch, router, or other networked device that sits between Data Terminal Equipment (DTE) on a data transmission circuit. A DCE manages line clocking, data coding, and signal conversion. Although many DCEs are separate devices and require attachment to a network interface on both ends of their connections, some systems build DCEs into their network interface. In the oldest network scenarios, a DTE was a computer and a DCE is a modem.

![A Frame Relay system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1311.png)

**Figure 13.11. A Frame Relay system**

Typical frames in a Frame Relay are 1600 bytes long, with a 10-bit ID number that identifies a particular virtual circuit from one host at a site to another host at a different site. The lease type places a limit on the size of the packets, the circuit provides a limit to the burst speed or maximum transfer rate, and the service contract places a limit on the average data transferred in a particular time period. The performance of Frame Relay running on T-1 lines falls between ISDN (128 Kbits/s) and ATM (155.5 Mbits/s).

A virtual leased line is different from a permanent leased line in that a leased line is dedicated to the lessee who can send data over the line at the full rated speed. A virtual leased line allows the lessee to share the capacity of a circuit in the manner described in the previous paragraph. Another way of looking at this is that virtual leased lines are essentially level-of-service agreements. Virtual leased lines usually cost a fraction of what a leased line costs. Frame Relay networks are meant to improve network utilization rates for service providers, and work well, provided that the service provider doesn't overload the system with too many subscribers.

Frame Relay technology has very little overhead; there is no flow control or acknowledgment messaging used. However, Frame Relay networks do have congestion control, which includes Admission Control for incoming connections, Committed Information Rate (CIR) for guaranteed throughput, Committed Burst Size (BC) for the largest rate allowed, and Excess Burst Size (BE) for an additional rate that will be attempted but not guaranteed. Two different control bits in the data header can be set to 1 (On) when there is congestion to control network actions; they are Forward Explicit Congestion Notification (FECN) and Backwards Explicit Congestion Notification (BECN). Those bits can then be used to adjust the data rate.

Unlike the older protocol X.25, which transports analog data, and on which Frame Relays are based, Frame Relay uses fast packet technology and does no error correction. When a frame fails the error checking routine, it is dropped. The Frame Relay service has a bit Command/Response (C/R) flag in the header, but the C/R flag is application specific and the Frame Relay service makes no demands on how or if it is used.

The technology relies on applications at each end of the virtual circuit to determine if a frame is missing and needs to be resent. It is the host's Transport and Session protocols that provide the messages used for control and context in which frame delivery can be understood. You can apply a priority flag to frames to implement QoS on Frame Relay networks.

Frame Relay services aren't universally used as WAN connections; indeed, their use is diminishing as broadband connections over dedicated lines such as DSL or cable modems are installed. Those lines, along with Virtual Private Networks (VPNs), use a different type of service called *Multi Protocol Label Switching*.

# Multi Protocol Label Switching

The Multi Protocol Label Switching (MPLS) protocol provides an alternative method for managing packets, frames, and cells on a variety of different network types. The protocol operates at both Layer 2 and Layer 3, the Data Link and Session levels of the ISO/OSI model, and can be used on both packet switching and circuit switching networks. MPLS is an IETF standard that provides Quality of Service features such as prioritization and service level control.

MPLS labels are applied to packets at the edge router of a network, called the *Label Edge Router* (LER). A label is a collection of routing information added to the header that includes the destination address, the allowed bandwidth and delay tolerated, the source IP address, the socket number used, and other service information. The information is entered after consulting the routing table of the LER. With this information, the LER assigns a Labeled Switch Path (LSP) to the packets and then places them into appropriate queues on the Label Switch Router (LSR). The information contained by MPLS labels makes MPLS traffic much more fault tolerant than SONET/SDH is.

The system of labeling is referred to a *Penultimate Hop Popping*, adding a label is called a *push*, and removing a label is called *pop*. When a packet arrives at a LER with a label on it, the LER adds a second label to that packet. As packets arrive at their interim destination, that additional label is removed, or popped; and when the packet arrives at its final destination, the last label is popped.

MPLS seeks to be the logical replacement for ATM networks, replacing all of the overhead involved with splitting data into cells and then having to signal and synchronize the traffic, which the speed of optical networks now makes unnecessary. As a Layer 2 to 3 protocol, MPLS offers a service that is similar to using datagrams and can be used for IP packets, as well as Ethernet, ATM, and SONET frames. MPLS relies on high-speed switches for its performance, and so it should come as no surprise that Cisco Systems was one of the main original developers of this "tag switching" technology; Ipsilon Networks was the other company involved, and was mainly responsible for the IP portion of the protocol.

MPLS finds an application on large, IP-based networks as a Quality of Service protocol, or as Cisco calls it, a Class of Service (CoS) application. It supports IP v.4 and v.6 and can be employed on ATM, Frame Relay, and T1 connections. The speed advantage of MPLS is no longer its main benefit, as network speeds have made switch speeds less important. The QoS support of data such as VoIP that requires high network efficiency (low latency) and other technologies with this requirement is the primary reason that MPLS is used.

# The Internet and Internet2

The Internet is a WAN composed of many other WANs. It is an internetwork of internetworks, if you will. About 95 percent of the protocols used for data transport on these networks are TCP/IP traffic. Those technologies are described throughout this book. One aspect of the Internet is worth considering from a WAN viewpoint: the connection points where different WANs are routed. The next section describes Internet Exchange Points in some detail.

As the Internet became more commercial, open, and congested, its initial purpose to support research and development at universities and laboratories became difficult. A number of newer networks have been developed that are building a next-generation Internet, also known as the Internet2 Network. A similar project in the UK is called JANET, and there are also projects of this type in Europe. The Internet2 Network enables a number of advanced applications and technologies and serves as a test bed for future development of the public commercial Internet.

## Internet Exchange Points

The original points of connection for large networks on the Internet in the United States were called Network Access Points (NAPs). The National Science Foundation (NSF) maintained the first NAP, and as the system expanded, three more were added that were managed by Sprint, Ameritech, and Pacific Bell. They were located in Washington, Chicago, California, and New Jersey. As the number of NAPs grew, certain urban areas with multiple ISPs established what became known as Metropolitan Area Exchanges (MAEs).

As the system expanded, the private sector greatly increased the number of network-to-network links. Today the points of connections between service providers and national networks are called Internet Exchange Points (IXP or IX), and the terms NAP and MAE are rarely used. An IXP is a switching facility managed by an ISP where traffic is exchanged between networks based on an exchange system called a *mutual pairing agreement*. IXPs route traffic from and to other IXPs without additional charges being imposed for the transit through the exchange. Data delivered to a receiving network upstream is billed for service, typically on the basis of the amount of traffic and level of service.

The proliferation of IXPs to provide internetwork connections provides the routing function that makes the Internet efficient and fault tolerant. The system of IXPs has another benefit as well. Each IXP connection is independent of the other IXP connections. If an ISP has a slow connection to another country, but fast connections internally, then their internal communications can run at full speed. The connections between countries separated by oceans are made using undersea or submarine optical fiber cable. [Figure 13.12](ch13.html#the_packet_clearing_house_is_a_resource) shows the Internet Exchange Directory on the Packet Clearing House Web site (`https://prefix.pch.net/applications/ixpdir/`), which lists IXPs by country along with their statistical data.

IXPs have a function that is purely switching. Any traffic shaping, filtering, or control over routing is controlled by the ISPs that participate in an exchange. The peering relationship between two ISPs connected through an exchange is defined by the Border Gateway Protocol (BGP), which builds a table of routers that serve as the entry points to various IP networks. Networks reached over this system are referred to as *Autonomous Systems* (AS), and the routes are called *path vectors*. AS are a collection of IP-connected routing prefixes that the ISP controls.

Not all traffic on the Internet flows through IXP facilities. Many ISPs have direct connections to one another. In those instances, it is only when the direct connection fails that traffic between the two ISPs is sent through the exchange. For ISPs that have no relationships, data exchange through IXPs is the only mechanism available.

As of October 2008, the top ten Internet Exchange Points in terms of traffic are listed in [Table 13.4](ch13.html#top_ten_internet_exchange_points), based on a compilation of available sources. The highest-rated U.S. IXP isn't shown on the chart. It was the New York International Internet eXchange (NYIIX), which was rated twelfth. NYIIX had 98 members, a maximum throughput of 23 Gbits/s, and an average throughput of 15 Gbits/s. This list is not definitive and is subject to seasonal changes. It is also noted that IXPs in the U.S. often don't disclose their traffic volumes.

![The Packet Clearing House is a resource for locating IXPs.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1312.png)

**Figure 13.12. The Packet Clearing House is a resource for locating IXPs.**

**Table 13.4. Top Ten Internet Exchange Points**

| Name | Location | Connected Members | Maximum Throughput(Gbits/s) | Average Throughput(Gbits/s) |
| --- | --- | --- | --- | --- |
| Amsterdam Internet Exchange (AMS-IX) | Amsterdam, Netherlands | 300 | 419 | 280 |
| Deutscher Commercial Internet Exchange (DE-CIX) | Frankfurt am Main, Germany | 250 | 428 | 210 |
| London Internet Exchange (LINX) | London, United Kingdom | 221 | 256 | 157 |
| Japan Network Access Point (JPNNAP) | Tokyo, Japan | 88 | 183 | 129 |
| Netnod Internet Exchange in Sweden (Netnod) | Stockholm, Sweden | 53 | 103 | 104 |
| Japan Internet Exchange (JPIX) | Tokyo, Japan | 107 | 73 | 55 |
| Spain Internet Exchange | Madrid, Spain | 43 | 72 | 61 |
| Hong Kong Internet eXchange (HKIX) | Hong Kong, China | 76 | 47 | 34 |
| Budapest Internet Exchange (BIX) | Budapest, Hungary | 52 | 35 | 26 |
| Polish Internet eXchange | Warsaw, Poland | 76 | 35 | 18 |

According to the site `InternetWorldStats.com`, as of June 2008, 1.46 billion of the world's 6.68 billion people were connected to the Internet, or about 21.9 percent. A recent estimate by the Discovery Institute of the amount of traffic that will flow over the Internet annually by 2015 predicts that it may reach one zettabyte, which is one million, million, billion bytes (1021), or 1000 exabytes. This is a factor of 50 times the size of traffic in 2006, which was 20 exabytes.

## Internet2

The Internet2 Network is a consortium of schools, corporations, research organizations, and government agencies that share in the use and development of an advanced internetwork. The goal of the project is to create a system for supporting leading-edge research, enabling next-generation technologies, and transferring the technologies to the public Internet. Among the technologies currently on The Internet2 Network are rich media libraries, video conferencing, advanced middleware, virtual laboratories, tele-immersion, tele-health, long-distance learning applications, and many more.

Internet2 is the trademark of the organization that created the first of these advanced network backbones, the Abilene Network. The Abilene Network connects all 50 of the states in the U.S. with a 10 Gbits/s pipe. Another project by this group established the National LambdaRail (NLR) regional optical network, which is an OC-192 optical backbone. Most of the articles written about Internet2 were written about the Abilene Network and not the consortium. Today, Internet2 has adopted the name "The Internet2 Network" as the new name for the Abilene Network. [Figure 13.13](ch13.html#the_internet2_network) shows the current extent of The Internet2 Network as of May 2009. Note that the Internet2 is a backbone service and doesn't cover the entire United States.

![The Internet2 Network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1313.png)

**Figure 13.13. The Internet2 Network**

# Summary

In this chapter, you learned about WANs and their characteristics. Routing and switching technology and the protocols required were also described.

The Public Switched Telephone Network (PSTN) is a circuit switching network that can support both voice and data services. The most popular connection types, ISDN and DSL, were described in detail.

The backbone technologies for connecting networks are through T- and E-carrier networks. SONET/SDH is the most popular protocol for data transfer on these backbones. Data that flows over SONET can be in the form of Asynchronous Transfer Mode (ATM) or Packet over SONET (PoS).

Packet switching networks are used for TCP/IP networks. Protocols such as X.25, Frame Relay, and ATM are used on packet switching networks. You also learned about how the Internet is connected by Internet Exchange Points (IXPs). The Internet2 Network was also briefly described.

In the next chapter, you learn how to create wireless networks.
