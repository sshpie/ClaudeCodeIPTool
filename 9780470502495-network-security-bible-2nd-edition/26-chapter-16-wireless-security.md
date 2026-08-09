# Chapter 16. Wireless Security

**IN THIS CHAPTER**

- **Understanding the electromagnetic spectrum**
- **Understanding wireless transmission systems**
- **Defining the generations of wireless technologies**
- **Reviewing spread spectrum technology**
- **Understanding 802.11 wireless LAN specifications**
- **Identifying and securing wireless communication**

Wireless cellular technology has made the cellular phone a must-have accessory that enables us to instantly communicate with friends, relatives, and business associates. Similarly, computers can also be free of wired connections when they are part of a wireless local area network (LAN) network. However, with this increased freedom comes increased risk of information compromise, particularly in wireless LANs.

This chapter explains cellular phone and wireless LAN technologies and addresses the associated wireless network security vulnerabilities and safeguards.

# Electromagnetic Spectrum

Before exploring the details of cellular phones and wireless LANs, a review of some fundamental terminology might be helpful. In wireless technology, the information is transmitted through the air similar to radio signal transmissions. The immediate issue from a security perspective is that anyone can intercept the communication, even if it is encrypted. While encryption would stop someone from reading the content of the information, interception of the wireless signal allows for interference and other types of attacks.

The transmitted waves can be described in terms of a sine wave, as shown in [Figure 16-1](ch16.html#sine_wave_characteristics). The important definitions associated with a sine wave are as follows:

- **Period and wavelength**—The *period* of a sine wave is defined as the time elapsed from one reference point on the sine wave to the next nearest identical point as the sine wave repeats. This distance is called the *wavelength* of the sine wave. The wavelength is denoted by the Greek letter lambda, λ, measured in units of length, such as feet, inches, or angstroms. As shown in [Figure 16-1](ch16.html#sine_wave_characteristics), one angstrom equals 10−10meters. The period is measured in units of time such as milliseconds or seconds, and the sine wave is said to have gone through one *cycle* in a period.
- **Frequency**—The number of sine wave cycles that occur in one second is called the *frequency* of the sine wave, which is measured in cycles per second or hertz. Thus, a sine wave that makes 1,000 cycles in a second is said to have a frequency of 1,000 cycles per second, 1,000 hertz, or 1kHz.
- **Relationship**—The relationship between the frequency of a sine wave and its wavelength is given by the formula, f = c/ λ, where f is the frequency in cycles per second, c is the speed of light constant (3 × 1010cm/sec), and **λ** is the wavelength in cm.

![Sine wave characteristics](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1601.png)

**Figure 16.1. Sine wave characteristics**

The electromagnetic spectrum is the range of frequencies characteristic of different applications and natural phenomena, as shown in [Figure 16-2](ch16.html#the_electromagnetic_spectrum).

The cellular phone and wireless LAN networks operate in the Ultra-High Frequency (UHF) band. The UHF band is shown relative to other frequency bands in [Figure 16-3](ch16.html#uhf_and_other_frequency_bands).

![The electromagnetic spectrum](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1602.png)

**Figure 16.2. The electromagnetic spectrum**

![UHF and other frequency bands](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1603.png)

**Figure 16.3. UHF and other frequency bands**

# The Cellular Phone Network

The cellular telephone network comprises a variety of components to effect a connection from one mobile unit to another. These components have to recognize a mobile phone, verify that it is a "legal" phone, note its location, retrieve information about the phone's account, establish the connection, generate billing information, and so on. The cellular network components that accomplish these tasks are summarized as follows:

- **Mobile station**—The mobile phone or mobile equipment, uniquely identified by the International Mobile Equipment Identity (IMEI). The IMEI consists of a six-digit Type Approval Code (TAC), a two-digit Final Assembly Code (FAC), and a six-digit Serial Number (SNR).
- **International Mobile Subscriber Identity (IMSI)**—A unique identifier assigned to a mobile subscriber that comprises a 15-digit maximum word containing a Mobile Country Code (MCC), a Mobile Network Code (MNC), and a Mobile Station Identification Number (MSIN). The IMSI is independent of the IMEI to provide for user mobility.
- **Subscriber identity module (SIM)**—A smart card that plugs into the mobile station to provide user mobility. The SIM card can plug into any mobile terminal and enable the user to make and receive calls from that terminal. The SIM card holds a secret key for authentication purposes and the IMSI. SIM card security is provided through the use of a PIN number or password.
- **Electronic Serial Number (ESN)**—A 32-bit unique identifier assigned to a mobile station by its manufacturer. Used in equipment prior to the adoption of the IMEI.
- **Cell tower**—The cellular communication facility that covers one hexagonal geographic area or cell. The cellular network is divided into cells that are each covered by a cell tower.
- **Base transceiver station (BTS)**—Incorporates the radio transceivers for a particular cell and communicates with the mobile station.
- **Base station controller (BSC) or base station**—Controls a cluster of cell towers. It manages the cellular call initiation and controls the transfer of the call from one cell tower boundary to the next when the mobile station moves across these boundaries. The BSC manages the radio capabilities for multiple BTSs and provides the connection from the mobile stations to the mobile switching center.
- **Mobile switching center (MSC)**—The point to which the base stations connect. The MSC transmits and receives the communications among subscribers on the cellular network, including connections to fixed networks. It also provides additional services, including mobile station registration, authentication, roaming, and routing for mobile subscribers. To accomplish these functions, the MSC connects to the following cellular network components:**Home location register (HLR)**—Tracks subscriber information and maintains a record of the last time the mobile cell phone was registered on the network. It contains account information of each registered subscriber on the network and tracks the current location of the mobile station. The HLR maintains all the necessary information for initiating, terminating, or receiving a call.**Visitor location register (VLR)**—Stores a subset of information contained in the HLR for each mobile station currently in the geographical area controlled by the VLR. For a roaming user, the VLR obtains this information from the user's HLR. Thus, the VLR maintains temporary user information to manage requests for subscribers who are out of their home area.**Authentication center (AuC)**—Uses a protected database to authenticate and validate services for each mobile device attempting to use the network. The authentication is accomplished through the use of a copy of a subscriber's SIM card secret key that is stored in the AuC database. The secret key can also be used for encryption of communications over the radio channel.**Equipment identity register (EIR)**—A database employed within mobile networks that contains a list of all valid mobile equipment on the network, based on the IMEI. If a mobile station has been stolen or is of a type that is not approved for the network, its IMEI will be tagged as invalid.

The topology of these major network cellular components is illustrated in [Figure 16-4](ch16.html#the_major_cellular_network_components).

![The major cellular network components](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1604.png)

**Figure 16.4. The major cellular network components**

# Placing a Cellular Telephone Call

The sequence of events for placing a cellular phone call, involving the cellular network components, is as follows:

1. The mobile station radio transceiver transmits a message request to the nearest base station.
2. The base station receives the call signal and sends it to the mobile switching center.
3. The mobile switching center queries the home location register to determine if the call is being placed to another mobile station within the local cell or if it is a roaming call. If it is the latter, the mobile switching center accesses the visitor location register.
4. The mobile switching center queries the equipment identity register and authentication center for location, service qualification, features, and authentication.
5. If everything is in order, the call is routed to the same base station, another base station, the Internet, or a land line.

## Cellular network evolution and transition to 4G

Recently, the proliferation of second-generation cellular technologies has been tremendous. Voice-centered first-generation cellular networks have grown to serve data-centric architectures and applications in the second generation. Highly sophisticated technologies, such as Global Systems for Mobile Communication (GSM), Code Division Multiple Access (CDMA), and IS-136 based United States Time Division Multiple Access (US-TDMA), have made it possible to set goals for second-generation cellular technologies.

### Note

As wireless technologies improved, they were categorized into generations, using a number and the letter G. For example, first-generation technology is labeled 1G, second-generation 2G, and so on.

There have also been significant developments in the synergy between circuit switched voice-based networks, such as the PSTN, and packet switched data-based networks, such as the Internet. The influence of IP (Internet Protocol) has been tremendous in Ethernet-based and the later wireless-based local area network services. This influence has also been seen in the cellular and wireless community in recent years. Packet-based networks for cellular services such as the General Packet Radio Networks and the Enhanced Data Rates for GSM Evolution (EDGE) are predominantly based on IP technology. Highly robust and versatile Internet Protocols such as IPv6 have been contemplated and experimented with to make the convergence of cellular and local area networks possible. IPv6 would be highly beneficial for handling the explosion of devices forming the network to support 4G.

Although third-generation technologies, such as the UMTS/WCDMA in Europe and CDMA2000 in the United Status, have been standardized by the Third Generation Partnership Project, other governmental standardization organizations have not been yet able to deliver user-friendly bandwidth and quality of service requirements. The third-generation cellular technologies unleashed many trends such as messaging systems (SMS), multimedia streaming, and Wireless Application Protocol for interactive web browsing. [Table 16-1](ch16.html#standard_technologies_through_cellular_e) shows the different technologies that have formed the various generations and the continual evolution of cellular technologies. These technologies are the forerunners of the fourth generation. A particular trend with third-generation systems is the multiplying of independent technologies such as GPRS, IMT-2000, WLAN, and HyperLAN. A main goal of 4G should be finding feasibility solutions for the inter-working of these varied technologies with a focus on developing new technologies that can deliver the requirements of 4G itself. One major feature of 4G is the seamless integration of wireless technologies such as cellular and LANs and provision for all IP-based networks. Such a scenario could be highly user efficient, as in the following example:

Alice makes a call from her PDA/cell phone from an airport to locate a particular pharmaceutical product for her ailing mother, who is in a hospital at the destination city. Alice has to crisscross a wireless LAN operator at the airport, a mobile operator covering different cities, and a global positioning system to discover the hospital's location. This could mean confusion in terms of the quality-of-service guarantee, security, and other vendor-specific parameters such as cost and billing. With the coming of 4G-based technologies, Alice could use a single carrier to accomplish the connection that she wants.

**Table 16.1. Standard technologies through cellular evolution**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | First Generation 1G | Second Generation 2G | Second/Third Generation 2.5G | Third Generation 3G |
| GSM Based Technologies | Analog | GSM | EDGE GPRS | WCDMA UMTS |
| CDMA Based Technologies | Analog | CDMA | CDMA2000 | CDMA2000 DCMA2000 |

## System infrastructure

Fourth-generation devices are highly mobile and have to work across all the frequency band assignments that current cellular operators utilize in order to achieve seamless integration of vendor-specific technologies. This puts a major constraint on antenna systems and their design for fourth-generation mobile devices. Traditional antenna systems are formed of an analog reception/transmission front end, and a data converter and a digital signal processing back end. Modern antenna systems have only a single transmitter/receiver (although Multiple Input/Multiple Output, or MIMO-based, antenna are being heavily researched), and the design of low noise amplifiers for such systems cannot incorporate transmission and reception on a large frequency spectrum.

Furthermore, with devices becoming mobile, smart, and adaptive, antennas are in high demand that can make intelligent decisions when the user roams from one cellular network segment to another. This makes a terminal "roamable" across any standard air interface and connectable to any wireless access point by exchanging configuration software. However, for smart antennas to work efficiently, the data converters need to have high precision and resolution. With power requirements and signal-to-noise ratio constraints, the design of high precision data converters and low noise amplifiers (LNA) becomes a challenge.

## Location discovery and handoff

One of the main factors in the design of any cellular technology is the design of location discovery and handoff mechanisms. Location discovery involves finding out the physical location of any device (mobile or non-mobile) and signaling communication with it. Handoff mechanisms maintain communication when two communicating entities move over different cellular segments. Because 4G attempts to put all IP-based and UMTS-based coverage, which includes all operators such as GSM, CDMA, and so on, under one entity for service seamlessness, location discovery and handoff procedures become extremely complicated. The complication arises because different operators may have different bandwidth and quality-of-service specifications, and dynamically selecting the best choice for the user based on the nature of the service can be tedious. Because more than one operator is generally involved in a UMTS-based network setup, inter-operator handoffs in addition to intra-operator handoffs are also essential.

For designing a location discovery and handoff strategy for 4G, a mobile IPv6 handoff strategy called MIPv6 has been proposed. Mobile IP is a standard draft of the IETF (Internet Engineering Task Force) for mobile devices to maintain connectivity to their home networks when they roam across different networks. MIPv6 is the higher version of this, and incorporates Internet Protocol version 6. Internet Protocol version 6 would be a more suitable candidate for 4G technology as the number of devices forming a single network in 4G is great. Mobile IP devices have special addresses, referred to as *care-of addresses* in addition to their normal home addresses. A binding agent would be responsible for direct routing of any communication for a device that has left its home network and has moved into a care-of network. Handoff processing in such cases involves many computations, possibly leading to quality-of-service issues.

## Synergy between local area and cellular networks

Fourth-generation technologies basically aim at bringing about anytime-anywhere networking using an all-IP-based network system. This means that non-IP-based technologies, such as WCDMA-, CDMA2000-, and UMTS-based voice delivery systems, should be remodeled. On the positive side, data networks such as WiFi and HyperLAN are highly flexible and could easily suit different requirements. Accessing anywhere-anytime information — with a seamless connection to a wide range of information and to such services as data, voice, and multimedia — will be the first priority for 4G cellular technology. Future 4G infrastructures will consist of a set of various networks using IP (Internet Protocol) as a common protocol so that users are in control and able to choose every application and environment. [Figure 16-5](ch16.html#representation_of_an_all-ip_network) shows how the interconnecting technologies of 4G bring about synergy between all forms of networks, whether local area networks or cellular networks, to form an all-IP network.

The synergy between the various operators of cellular and WLAN networks can be brought about by many different combinations and possibilities in the network stack. Tunneling over the different networks that operate today seems to be an easy solution. In this model, each operator and technology has its own individual network stack (the stack representing the operator's core cellular network embedded in an all-IP-based Internet), with an overall tunnel infrastructure running on top of each operator's layer. No modification to the existing network stacks of the different cellular operators is required.

However, such a model using a tunnel would be a severe burden on the bandwidth offered, latency, and quality-of-service requirements. A second option is to use a network-level model that interfaces with the Internet and the network stacks of the different cellular operators. The main drawback with this method, compared to the tunneling model, is the severe architectural changes the existing Internet and other IP-based networks would have to make in order to assure seamless functioning of cellular systems.

Given the size of the Internet, this might take years to accomplish. However, quality-of-service provisioning, sustenance, and other requirements would not be as highly compromised as with the tunneling model. A third model, integrating the various cellular technologies, could be brought about at the physical and link layers of the cellular network stack. This would optimize quality of service requirements and provide maximum bandwidth.

![Representation of an all-IP network](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1605.png)

**Figure 16.5. Representation of an all-IP network**

## Fault tolerance and network security

Survivability of a cellular network is directly dependent on how robust and fault tolerant the system is. Many of these aspects are still under study and it would take a completely established and operating 4G network to analyze them. Cellular networks, unlike IP-based networks, are highly centralized structures. Centralized entities such as base stations, domain servers, and QoS brokers make it very difficult to apply self managing architectures. If at any point any of these centralized entities were to fail, a portion of the whole network served by them could be down until manual maintenance takes place. Power failures of devices and base stations that may be battery dependent could easily lead to disastrous situations in cellular networks that require power control techniques to be embedded with designs for fault tolerance. Fault tolerance has been a less understood metric even with well established network systems such as the Ethernet, and could take more than a decade to completely mature for 4G-based cellular technologies.

Security is another vital segment of 4G networks. With 4G effectively combining the Internet world and the cellular world, commercial transactions such as credit card processing and password authentication could begin to operate for mobile phones and PDAs and in highly insecure environments as wireless hotspots and public Internet cafes. Today's cellular networks provide high security voice and data communication whether it is GSM, CDMA2000, or some other system, but they do this independently. For the security chain to be completely tight in 4G systems, security algorithms should become interpretable. However, many key management schemes, encryption algorithms, and authentication systems are proprietary to the individual operator even in 3G systems; it would take a tremendous amount of legal activity for standards to be adopted. Wireless LAN security schemes (such as RADIUS and WEP) have not yet gained the confidence of the public and are highly vulnerable to exploitation. WEP, in particular, has been shown to be easily compromised and is very weak; other methods such as using AES, WPA-2, and EAP extensions are being used instead. Carrying over such schemes to the cellular world would mean increasing security risks associated with cellular operators.

Furthermore, a whole range of new exploits such as malware, spamming, denial-of-service attacks, and spoofing — which are not prevalent in the cellular world today — would be dangers in 4G technologies. Sophisticated research schemes should be developed to maintain network security and integrity in such environments. Network management issues such as billing and accounting could be compromised by an attacker, leading to innocent users having to pay. No present account schemes (even the brokering service architecture for billing) could correctly manage accounts under the 4G concept. This makes it highly difficult for 4G to become commercial because the goal is to design a scheme that is robust enough to deal with 4G networks yet secure enough to prevent billing errors and malicious activities.

The evolution to 4G depends on a vast number of features that face both the cellular and local area networking sectors during their development. In addition to providing higher speed and bandwidth compared to present cellular systems, 4G contemplates the convergence of IP-based networking and the non-IP-based cellular sector. This would be an enormous change from all the generations through which the cellular sector has evolved until now. Factors such as multiple input/multiple output antennas, quality of support provisions, and bandwidth improvement have been the focus of the research community and have shown significant improvements. However, there are still important issues, such as fault-tolerance, self configuration, network management, and customer billing. Similar aspects of all-IP networks also face problems, considering the high number of non-proprietary network layer protocols that are run by several organizations. But standardization efforts both on the technical and legal fronts can still bring 4G into practice.

# Wireless Transmission Systems

A number of wireless technologies are in use globally, most of which are not compatible with the others. Wireless networks have evolved from analog-based equipment to sophisticated digital devices. In addition, efforts are in place to develop a global standard so that wireless equipment will be able to operate internationally. This section discusses the different types of wireless transmission system technologies and their evolution through a number of generations.

Before describing the different wireless transmission systems, this chapter covers three important technologies used in these systems. These technologies are Time Division Multiple Access (TDMA), Frequency Division Multiple Access (FDMA), and Code Division Multiple Access (CDMA).

## Time Division Multiple Access

TDMA is a digital transport mechanism that provides for multiple channels over the same medium by allotting a time slot for each conversation. Thus, user 1 can use the medium for a fixed period of time, then user 2, then user 3, and so on, until the cycle repeats. The TDMA concept is widely used in 2G wireless systems and is illustrated in [Figure 16-6](ch16.html#tdma_operation).

![TDMA operation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1606.png)

**Figure 16.6. TDMA operation**

## Frequency Division Multiple Access

FDMA is technology wherein multiple calls are made by assigning each call to a separate frequency or channel. Because the calls are on different frequencies, they can be separated at the receiving end. In full duplex FDMA, in which communication can occur simultaneously in both directions, separate channels are required for transmitting and receiving. FDMA is used in 1G analog systems. FDMA is shown in [Figure 16-7](ch16.html#fdma_operation).

## Code Division Multiple Access

CDMA uses codes to distinguish among simultaneously transmitted signals. One instantiation of CDMA is spread spectrum technology, which spreads the transmitted information over a wider bandwidth than conventional systems. This spreading provides for increased immunity to noise interference and jamming. To send multiple messages over the spread spectrum, unique codes are assigned to each call at the transmitting end. The receiver then uses one of the assigned unique codes to decode a call and distinguish it from the other overlaid calls. The principal radio interface for 3G wireless systems, specifically IMT-2000, is a 3-mode, wideband version of CDMA. The CDMA scheme is shown in [Figure 16-8](ch16.html#cdma_operation).

![FDMA operation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1607.png)

**Figure 16.7. FDMA operation**

![CDMA operation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1608.png)

**Figure 16.8. CDMA operation**

## Wireless transmission system types

The application of TDMA, FDMA, and CDMA technologies to mobile phone systems is discussed in the following sections.

### Advanced Mobile Phone System

The Advanced Mobile Phone System (AMPS) is a first generation analog wireless technology family of standards and is the U.S. standard for analog cellular service. The AMPS standards were developed by the TR-45 committee within the Telecommunications Industry Association (TIA). AMPS uses FDMA and operates in the 800-MHz frequency band using 30kHz wide channels. Another version of AMPS, N-AMPS, uses 10kHz wide channels and offers three times the capacity of conventional AMPS. AMPS is being replaced by the fast-growing digital networks. When used with a modem, AMPS can provide circuit-switched data communications.

A version of AMPS, called D-AMPS, for digital cellular AMPS, was implemented in the TIA IS-54 standard. The next-generation standard, TIA/EIA-136, divides a 30kHz cellular channel into three time slots of 8kbps each for three users.

## Global System for Mobile Communications

The Global System for Mobile Communications (GSM) is a version of TDMA that operates in the 1800MHz range, providing eight time slots in 200 kHz-wide channels. GSM is very popular in Europe and is widely deployed. Wireless networks that operate in the 1800 or 1900MHz frequency band are also Personal Communications Systems (PCS). A version of GSM TDMA cellular is known as PCS1900.

### Cellular Digital Packet Data

Cellular Digital Packet Data (CDPD) is a North American wireless specification that is an enhancement to conventional analog services and operates on AMPS networks. It is based on the OSI model and uses the TCP/IP protocol to connect to the Internet and other public packet-switched networks. CDPD supports the ISO Connectionless Network Protocol (CLNP) as well as the IP protocol, including multicast service. Because it is an analog technology, a modem is required at the transmitting and receiving ends. CDPD has a raw data rate of 19,200 bps but an effective throughput rate of 9,600 bps.

### Personal Digital Cellular

Personal Digital Cellular (PDC) is a TDMA-based, Japanese digital cellular standard that employs three time slots on a 23kHz carrier. It operates in the 800MHz or 1.5 GHz frequency bands. PDC is a second-generation technology and is being replaced by third-generation technologies, such as W-CDMA.

### Total Access Communication System

Total Access Communication System (TACS) is a first-generation Motorola analog FM technology, similar to AMPS, operating in the 900MHz frequency range. It was used extensively in Europe and in Asia. An enhanced version of TACS with additional channels is called ETACS. TACS and ETACS have been replaced by GSM.

### Nordic Mobile Telephone

Nordic Mobile Telephone (NMT) refers to the original Nordic Mobile Telephone system that came into service in 1981, covering large portions of Norway, Sweden, Denmark, Finland and much of Europe. It was a first-generation analog system using FDMA.

### International Mobile Telephone Standard 2000

The International Mobile Telephone Standard 2000 (IMT-2000) is the International Telecommunications Union specification for a 3G mobile standard. It provides services for fixed, voice, mobile, data, multimedia, and Internet communications, and supports seamless global roaming. IMT-2000 is designed for transmission rates of 2Mbps for walking and stationary callers and 348 Kbps for users in moving vehicles. It also provides for integration of satellite services with the cellular network. The IMT-2000 standard is designed to work with five radio interfaces and FDMA, TDMA, and CDMA technologies. [Figure 16-9](ch16.html#imt-2000) shows these interfaces and technologies.

![IMT-2000](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1609.png)

**Figure 16.9. IMT-2000**

### Universal Mobile Telecommunications Systems

Universal Mobile Telecommunications Systems (UMTS) is a 3G mobile communications system that uses the IMT-2000 standard. It is being developed under the European Telecommunications Standards Institute (ETSI) and can provide data rates of up to 2 Mbps. UMTS operates in the 1885 to 2025MHz and 2110 to 2200MHz frequency bands, with the 1980 to 2010MHz and 2170 to 2200MHz designated for the satellite.

UMTS can operate in the following three modes defined by IMT-2000:

- **Time Division Duplex (TDD) mode**—Uses TD-CDMA and supports asymmetrical and symmetrical data rates up to 2Mbps in public micro and pico cell environments
- **Frequency Division Duplex (FDD) mode**—Uses Wideband Code-Division Multiple-Access (W-CDMA) and supports data rates up to 384kbps and 2Mbps in public macro and micro cell environments
- **Multimode Terminal mode**—Employs GSM and UMTS FDD and TDD

W-CDMA is a 3G technology that is more complex than 2G systems in that it can accommodate multiple simultaneous users transmitting at different rates as a function of time.

The first commercial W-CDMA network was implemented in 2001 in Japan and, since then, other W-CDMA networks have been established in a number of European countries.

CDMA2000 is another 3G technology similar to W-CDMA. It can be deployed in the following phases:

1. **CDMA2000 1x**—Provides an average of 144kbps packet data in a mobile environment
2. **CDMA2000 1x-EV-DO**—Provides data rates up to 2Mbps on a dedicated data carrier
3. **CDMA2000 1x-EV-DV**—Provides higher peak rates than the other phases and also supports simultaneous voice and high-speed data

[Table 16-2](ch16.html#wireless_cellular_systems_summary) provides a summary overview of the previously discussed wireless cellular systems.

A 2.5 G technology known as Enhanced Data rate for GSM Evolution (EDGE) builds on the General Packet Radio Service (GPRS) protocol. GPRS is an IP-based, packet-switched technology that supports burst transmission up to 1.15 Mbps. EDGE enables GSM operators to use existing GSM radio bands to offer wireless multimedia IP-based services. EDGE supports theoretical maximum speeds of 384kbps with a bit-rate ranging from 48kbps to 69.2kbps per time slot, depending on conditions.

# Pervasive Wireless Data Network Technologies

Two types of technologies are of critical importance in the implementation of wireless data networks: spread spectrum and orthogonal frequency division multiplexing (OFDM), a variation on spread spectrum. This section explores these technologies in detail.

## Spread spectrum

Spread spectrum is an RF communications mechanism in which the baseband signal is spread over a wide frequency range through the injection of another high-frequency signal input. It falls under the general category of CDMA.

### Note

Interestingly, spread spectrum technology was patented in 1941 by Hollywood actress Hedy Lamarr and her pianist, George Antheil. They were granted U.S. Patent No. 2.292.387.

Spread spectrum wireless operates in the unlicensed industrial, scientific, and medical (ISM) band of frequencies, from 2400MHz to 2483.5 MHz. It is used in the IEEE 802.11 wireless LAN standards as well as in cordless phones, wireless CCD cameras, and similar products.

## Spread spectrum basics

The basis for understanding the operation of spread spectrum technology begins with the Shannon/Hartley channel capacity formula:

> C = B × Log2(1 + S/N)

In this formula, C is the channel capacity in bits per second, B is the required channel bandwidth (range of frequencies required) in Hz, and S/N is the signal-to-noise power ratio.

**Table 16.2. Wireless Cellular Systems Summary**

| System Acronym | System Name | Subscriber Receiver Bandwidth | Subscriber Bandwidth Transmitter | Multiple Access Method | Channel Spacing | Bit Rate |
| --- | --- | --- | --- | --- | --- | --- |
| AMPS | Advanced Mobile Phone Service | 869–894 MHz | 824–849 MHz | FDMA | 30 KHz | n/a |
| TACS | Total Access Communication System | 916–949 MHz | 871–904 MHz | FDMA | 25 KHz | n/a |
| ETACS | Enhanced Total Access Communication System | 916–949 MHz | 871–904 MHz | FDMA | 25 KHz | n/a |
| NTACS | Narrow-Band Total Access Communication System | 860–870 MHz | 915–925 MHz | FDMA | 25 KHz | n/a |
| NMT-450 | Nordic Mobile Telephone System | 463–468 MHz | 453–458 MHz | FDMA | 25 KHz | n/a |
| NMT-900 | Nordic Mobile Telephone System | 935–960 MHz | 890–915 MHz | FDMA | 12.5 KHz | n/a |
| IS-54/136 | North American Digital Cellular | 869–894 MHz | 824–849 MHz | TDMA/FDM | 30 KHz | 48.6 kbps |
| GSM | Global System for Mobile Communication | 935–960 MHz | 890–915 MHz | TDMA/FDM | 200 KHz | 270.833 Kbps |
| PDC | Personal Digital Cellular (Japan) | 810–826 MHz | 940–956 MHz | TDMA/FDM | 25 KHz | 42 Kbps |
| PDC | Cellular (Japan) | 1429–1453 MHz | 1477–1501 MHz | TDMA/FDM | 25 KHz | 42 Kbps |
| CDPD | Cellular Digital Packet Data (WAN) | 869–894 MHz | 824–849 MHz | FDMA | 30 KHz | 19.2 Kb/s |
| UMTS (Europe) | High Tier PCS-1900 (based on GSM) | 2110–2170 MHz | 1900–1980 MHz | TDMA/FDM | 200 KHz | 64 Kbps – 2 Mbps |
| IMT-2000 | High Tier PCS CDMA (based on IS-95) | 2110–2160 MHz | 1918–1980 MHz | CDMA/FDM | 1250 KHz | 1.2288 (Japan) Mbps |

In other words, C is the amount of information allowed by the communication channel, the maximum data rate for a fixed bit error rate. The following example illustrates a typical calculation.

Assume that a communications channel has a 40kHz bandwidth. What is the channel capacity for a signal-to-noise power ratio of 20 decibels, or 20 dB?

Before you can use the formula, you have to convert the signal-to-noise ratio in dB to a straight power ratio, recalling the formula for calculating dB from a power ratio is as follows:

> dB = 10 log10 (S/N)

Thus, you can state the power ratio of the problem as follows:

> 20 dB = 10 log10 (S/N)

For this equation to be true, log10 (S/N) must equal 2, so S/N must equal 100. Therefore, the straight power ratio to be used in the Shannon/Hartley equation is 100.

Substituting the problem values into the Shannon/Hartley equation yields the following:

> C = 40 × 103 × log2(1 + 100) = 40 × 103 × log2(101)

or

> C = 40 × 103 × 6.65821 = 266.328 kbps

A profound result of the Shannon/Hartley equation is that the capacity of a communication channel for a given signal-to-noise ratio can be increased by increasing the channel bandwidth. This means that if there is a large amount of noise or jamming on a channel, the channel capacity can be increased by spreading the signal over a larger bandwidth. This condition is shown in the following analysis.

The Shannon/Hartley equation can be changed to incorporate the natural log, loge, which is represented by the symbol, ln, by applying the following rule:

> log2 A = loge A/ loge 2 = loge A/0.6930 and, therefore,
> 
> log2 A = 1.443 ln A
> 
> Thus, C = [B × ln(1 + S/N)(1.443)] and
> 
> C = 1.443B[ln(1 + S/N)]

Using the MacLaurin series expansion, that states

> ln(1 + x) = x - x2/2 + x3/3 - x4/4 + ... yields
> 
> C = 1.443B[S/N - 1/2(S/N)2 + 1/3 (S/N)3 - 1/4 (S/N)4 + ...

Assuming the signal-to-noise ratio is low, meaning there is a lot of noise relative to the signal being transmitted, the equation can be approximated by the following:

> C = 1.443B (S/N) or for a very rough approximation,
> 
> C = B (S/N)

Thus, to maintain the maximum channel capacity for a very low signal-to-noise ratio, increase the bandwidth of the transmitted signal.

The two principal types of spread spectrum technology are *direct sequence spread spectrum (DSSS)* and *frequency hopping spread spectrum* (FHSS).

### Direct sequence spread spectrum

DSSS uses a bit pattern called a *chip* or *chipping code* that is combined with the data to be transmitted and expands the bandwidth occupied by the transmission. On the receiving end, the same code is combined with the received information to extract the original data stream. This system offers increased immunity to noise or jamming signals in that any noise bursts superimposed on the RF signal being transmitted through the air are spread out and reduced in energy during decoding at the receiver. This process is summarized in [Figure 16-10](ch16.html#dss_transmission_and_reception_in_the_pr).

![DSS transmission and reception in the presence of noise](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1610.png)

**Figure 16.10. DSS transmission and reception in the presence of noise**

The encoding and bandwidth spreading of the data at the transmitting end are accomplished by using the Exclusive Or function for the data bit stream with that of a higher frequency chip signal generated by a pseudorandom code generator. The Exclusive Or function's output is fed into the modulating portion of the transmitting system, combining with the local oscillator to generate the RF signal to be transmitted.

### Frequency Hopping Spread Spectrum

FHSS technology also spreads the transmitted signal over a wideband, but accomplishes this by hopping the carrier frequency among different frequencies. The transmitter and receiver must be synchronized so that they are on the same frequency at the same time.

The hopping rate determines whether the particular instantiation of FHSS is low frequency hopping spread spectrum (LFHSS) or fast frequency hopping spread spectrum (FFHSS). In LFHSS, multiple consecutive data bits modulate the carrier frequency, where, in FFHSS, there are multiple frequency hops per data bit. If there are *n* frequency slots used in FHSS, the total bandwidth of the frequency-hopping signal equals Bn, where B is the bandwidth of each frequency hop channel. [Figure 16-11](ch16.html#frequency_hopping_example) illustrates the frequency hop signal.

![Frequency hopping example](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1611.png)

**Figure 16.11. Frequency hopping example**

The FCC requires that FHSS use a minimum of 75 frequencies with a maximum dwell time on one frequency of 400 ms. With the randomness of frequency hopping, multiple FHSS systems can exist in close proximity without interfering with each other's transmissions.

### Orthogonal Frequency Division Multiplexing

Orthogonal Frequency Division Multiplexing (OFDM) is a spread spectrum variation of FDM. It divides the signal to be transmitted into smaller subsignals and then transmits them simultaneously at different carrier frequencies. These carrier frequencies are spaced at specific frequencies. This technique makes OFDM resistant to cross talk and interference from multipath transmissions (that is, the same transmission arriving at the receiver at different times because of different length paths taken).

The basic concepts behind OFDM are as follows:

- By using a rectangular carrier pulse, modulation is accomplished by performing an Inverse Fast Fourier Transform (IFFT).
- By Fourier analysis, the rectangular pulse shape yields subcarriers defined by the function sin (x)/x, as shown in [Figure 16-12](ch16.html#ofdm_subcarriers).

The orthogonality in OFDM comes from the subcarrier spacings, as shown in [Figure 16-12](ch16.html#ofdm_subcarriers). The IFFT modulation of the square pulse produces subcarrier spacings, at which, when sampled at the points shown in [Figure 16-12](ch16.html#ofdm_subcarriers), all other signals are at zero value. Thus, the subcarrier is orthogonal to all the other signals. At the receiving end, a Fast Fourier Transform is applied to recover the original data. OFDM is used in the IEEE 802.11 Wireless LAN standard, Asymmetric DSL, and for digital television in Australia, Europe, and Japan.

![OFDM subcarriers](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1612.png)

**Figure 16.12. OFDM subcarriers**

# IEEE Wireless LAN Specifications

The IEEE 802.11 family of wireless LAN standards specifies an interface between a wireless client and a base station or access point, as well as among wireless clients. Work on the first standard, 802.11, began in 1990 and evolved from various draft versions; approval of the final of 802.11 draft occurred on June 26, 1997.

The 802.11 specification identifies an over-the-air interface between a mobile device wireless client and a base station or between two mobile device wireless clients.

The IEEE 802.11 standard specifies parameters of both the physical (PHY) and medium access control (MAC) layers of the network.

## The PHY layer

The PHY layer is responsible for the transmission of data among nodes. It can use DSSS, FHSS, OFDM, or infrared (IR) pulse position modulation. The family of standards supports data rates ranging from 2Mbps to 54 Mbps, with the early draft of a proposed new standard, 802.11n, targeting 100 Mbps.

## The MAC layer

The MAC layer is a set of protocols responsible for maintaining order in the use of a shared medium. The 802.11 standard specifies a carrier sense multiple access with collision avoidance (CSMA/CA) protocol for the wireless LANs. The MAC layer provides the following services:

- **Data transfer**—CSMA/CA media access.
- **Association**—Establishment of wireless links between wireless clients and access points in infrastructure networks.
- **Reassociation**—An action that occurs in addition to association when a wireless client moves from one Basic Service Set (BSS) network to another, such as in roaming. A BSS is a group of 802.11-compliant stations that comprise a fully connected wireless network.
- **Authentication**—The process of proving a client identity through the use of an 802.11 authentication mechanism.
- **Privacy**—In the 802.11 family of standards, there are options for different levels of protection of the transmitted data. These options are discussed in detail in a later section of this chapter.

802.11 offers two operational modes: ad hoc and infrastructure.

The *ad hoc mode* refers to Independent Basic Service Set (IBSS) networks, which do not have a backbone infrastructure and involve at least two wireless stations. IBSS is not intended for long-range use, but is normally implemented in rooms or sections of a building. Ad hoc mode is a peer-to-peer networking paradigm in which each mobile client communicates directly with other mobile clients in the network and only clients within the same cell can communicate. Communication outside of the cell can take place if a cell member operates as a routing service.

The *infrastructure mode* refers to BSS networks that incorporate access points to communicate between mobile devices and the wired network or other wireless networks.

Some of the commonly used 802.11 standards are: 802.11, 802.11a, 802.11b, 802.11g, and 802.11e. 802.11e differs from the others in that it focuses on providing for quality of service (QoS) in a wireless LAN. A proposed standard that is in development at this time is standard 802.11n. [Table 16-3](ch16.html#ieee_802.11_wireless_lan_standards) summarizes the characteristics of the 802.11 family.

**Table 16.3. IEEE 802.11 Wireless LAN Standards**

| Standard | Band | Technology | Transmission Speed | Comments |
| --- | --- | --- | --- | --- |
| 802.11 | 2.4 GHz | FHSS or DHSS | 1 or 2 Mbps | Original wireless LAN standard |
| 802.11b | 2.4 GHz | DSS | 11 Mbps, but decreases to 5.5 Mbps, 2 Mbps, or 1Mbps as a function of signal strength | Extension to 802.11; known as Wi-Fi |
| 802.11a | 5 GHz | OFDM | 54Mbps | Extension to 802.11 |
| 802.11g | 2.4 GHz | OFDM | 54Mbps | Extension to 802.11 |
| 802.11e |  |  |  | Guaranteed timely Quality of delivery of application Service data to specified (QoS) destinations; provides Standard guaranteed bandwidth; supports streaming multimedia files; incorporates error correction. |
| 802.11n | 5 GHz | OFDM proposed | Targeting 100 Mbps | Currently under proposed development; probability standard of using Multiple-In, Multiple-Out (MIMO) scheme. MIMO uses multiple transmitting antennas, tuned to the same channel, with each antenna transmitting a different signal. The receiver has the same number of antennas that listen to all transmitters. The received signals are recombined to recover the transmitted data. |

# IEEE 802.11

Project Ethernet at the Xerox Palo Alto Research Center (PARC) in the '70s was a tremendous success in the field of communication networks. Wired networks (local area networks) were able to gain the confidence of public and private sectors in fields ranging from finance and banking to hospitals. With the advent of Ethernet technology, worldwide networks such as the Internet had a tremendous boost. Places with access to computers had easy access to data and information both on the Internet and on other secure enterprise networks. However, a stumbling block that impeded growth was the need for computer users to have physical hardware interfaces to achieve connectivity in this wired world. Furthermore, remote connectivity could not be easily achieved using wired networks. Many solutions such as Mobile IP and virtual private networks (VPNs) were put forward for the remote user, yet the necessity of wired connections always made network setup and administration difficult. For example, with Mobile IP a remote user can leave the premises of an enterprise in order to get connectivity, but doing so makes routing all the more complicated. This extra complexity with routing made Mobile IP not a very feasible option for easy deployment. Some of these problems were solved with the advent of wireless technology for local area networks. With wireless channels and transceivers, users were able to achieve typically the same level of connectivity (in comparison to wired networks) while dispensing with physical wiring. The major motivation and benefit from wireless local area networks was increased mobility. Without direct attachment to conventional networks, network users were able move almost without restriction and access local area networks from nearly anywhere. Standardization processes were taken up mainly by the IEEE so that seamless connections could be made all over the world—and thus the IEEE 802.11 and the Wi-Fi Alliance were chartered. Many contemporary and competing wireless technologies such as HomeRF, HIPERLAN (mostly in Europe), and Bluetooth emerged alongside WiFi, but WiFi was able to establish its prominence for local area networks due to its relative ease of deployment and customer satisfaction.

## Wireless channels

The network stack for IEEE 802.11 is almost the same in comparison to the wired Ethernet standards with changes incorporated at the lowest level (the physical or PHY layer) and the next level (media access control or the MAC layer). Changes in these layers were brought in to incorporate wireless channels and radio frequency mediums as against conventional Ethernet transmission. Media access control protocols were modified to incorporate the CSMA/CA (Carrier Sense Multiple Access/Collision Avoidance) scheme compared with the CSMA/CD (Carrier Sense Multiple Access/Collision Detection) scheme followed in conventional Ethernet. The physical layer that handles data transmission between nodes at the lowest hardware level can use either direct sequence spread spectrum (DS), frequency-hopping spread spectrum (FH), or infrared (IR) pulse position modulation.

Spectrum distribution has always been a sensitive issue in regard to wireless deployments. When wireless technology for local area networks matured, most radio frequencies used by communication systems were already distributed to various commercial and private vendors and military operators. However, a portion of unlicensed spectrum, called the ISM (industrial-scientific-medical) band, was reserved for universal use. Wi-Fi appliances that use infrared waves (other than normal radio waves) for communication were allocated a certain portion of the infrared spectrum. Although use of infrared for communication is mentioned in the standard, no large commercial and practical installations are normally seen.

The IEEE 802.11 has a multitude of sub-drafts pointing to the time and technology developments in Wi-Fi technology. The most prominent ones are 802.11a, 802.11b and, and 802.11g. In addition to the above-mentioned standards, other main 802.11 sub-drafts include 802.11e (for quality of service recommendations), 802.11i (for security considerations), 802.11s (for mesh networking), and 802.11v (for network management issues). The three prominent standards—802.11a, 802.11b, and 802.11g—have their own respective wireless frequency bands, modulation schemes, wireless channels, data rates, and other operational features (see [Table 16-4](ch16.html#allocated_spectrum_for_ieee_802.11b_soli)).

**Table 16.4. Allocated Spectrum for IEEE 802.11b/g Operations**

|  |  |
| --- | --- |
| United States | 2.4000–2.4835 gHz |
| Europe | 2.4000–2.4835 gHz |
| Japan | 2.471–2.497 gHz |

The 802.11a specification operates at radio frequencies between 5.15 and 5.875 gHz, and the 802.11b and 802.11g specifications operate at radio frequencies in the 2.4 to 2.497 gHz range. [Table 16-4](ch16.html#allocated_spectrum_for_ieee_802.11b_soli) shows the operating radio frequency ranges that wireless local area networks are supposed to use in various parts of the world for 802.11b/g networking. Orthogonal Frequency Division Multiplexing (OFDM) is used for channel multiplexing in 802.11a, while 802.11b and 802.11g use spread spectrum techniques such as Direct Sequence Spread Spectrum (DSSS) and Frequency Hopping Spread Spectrum (FHSS).

Also notice that the amount of frequency spectrum available to 802.11a is relatively higher (at a higher center frequency) than that of 802.11b and 802.11g (both use the same frequency band) and thus would be able to accommodate more non-overlapping channels. In the United States, the wireless spectrum available for Wi-Fi is partitioned into 11 equally spaced channels. But channel interference by one channel to its neighbors could exist when modulation schemes are not highly sophisticated. Penetration abilities (ability to go through obstacles) are relatively less for high frequency radio waves compared to low frequency waves. This gives a slight edge for 802.11b and 802.11g devices for most indoor applications (where waves need to penetrate numerous obstacles) compared to 802.11a devices. The first major large-scale deployment of wireless networks began with 802.11b technology as opposed to 802.11a devices because it was more conducive for indoor applications. In the beginning of 2003, IEEE 802.11g began to replace 802.11b as it offered higher transmission rates within the same frequency band. 802.11g devices were highly backward compatible with 802.11b devices (802.11g devices had the ability to work at both data rates 54Mbps with other 802.11g devices and 11Mbps with conventional 802.11b devices) which facilitated the transition between them highly seamlessly.

## Deployment and management

There are basically two modes in which wireless networks following the 802.11 technology could be set up: Client-Server (infrastructure) based network mode and ad hoc (infrastructureless) network mode. An ad-hoc or infrastructureless network is a simple network where communications are established between multiple stations in the network in a given coverage area without the use of a centralized routing mechanism. The centralized routing or switching mechanism is generally called an access point (AP). Any node that wishes to join an infrastructure-based network initiates a communicational setup routine with the access point and, if properly identified, forms a part of the network. It would automatically lose communication and would be eliminated from the network if the node were to digress too far spatially from the centralized access point. Typically for 802.11b/g devices, this range is within 10 to 50 meters around the access point. The access points must be fair in providing for all of the catered nodes by it for quality of service, bandwidth, and security criteria. The standard proposes that the wireless media should be shared fairly by all the nodes within a specified base service set (all nodes in view of an access point and that form a network). The access point in most cases would be the bridge between mobile nodes to a bigger wireless or wired network domain. This makes roaming (and mobility) of nodes from one place to another possible, which is a highly inhibited feature in wired networks. [Figure 16-13](ch16.html#infrastructure-based_wireless_lan) shows how mobile wireless nodes could interact with an access point and thus be a part of larger networks on the other side of the access point. Sophisticated queuing algorithms are used in access points for time scheduling and bandwidth distribution to the various nodes that form the network. This arrangement allows for point coordination of all of the stations in the basic service area and ensures proper handling of the data traffic. The access point also routes data between the stations and other wireless stations, or to and from the network server, thus partially taking responsibility for routers and gateways. The other mode of network setup is the ad hoc mode wherein no centralized entity is found to coordinate network management and activities. The individual nodes themselves form a distributed system capable of managing network functions. These systems are comparatively simple to be deployed as no access point infrastructure is required and could be easily conceived for emergency and on-the-fly circumstances.

## Operational features

The physical layer in IEEE 802.11b devices follows DSSS and FHSS technology. Spread spectrum techniques come in handy for transferring base band signal content that is packed in a small frequency band over a larger frequency range. This process has sophisticated noise shaping advantages that are highly conducive to over-the-air transmission. Any signal (bit) to be transmitted is modulated with a chirp that is 11 times its frequency to get the spread spectrum signal, which is noise-like in character. The chirp signal (Barker sequence or Complementary Code Keying sequence) combined with the data signal are then transmitted. Matched filters able to recognize the chirp signal and its associated data (by correlation techniques) are employed at the receivers. These filter out the intended data signal for the spread spectrum during a process called *despreading*. Any interference signal or noise present in the spread spectrum signal is despread over a high range of frequencies with relatively less power compared to the intended signal, and can be filtered easily at the receiver.

This technique is similar to CDMA (Code Division Multiple Access) technology in the cellular sector; however, multiuser detection with a bank of chirp signals is a major aim in CDMA. Frequency Hopping Spread Spectrum (FHSS) sends its transmissions over a different carrier frequency at different times. A bank comprising a range of predetermined bands is permuted to get pseudo-random patterns. The transmission signal is allowed to hop over the various bands of a realized pattern for designated periods of time. The intent of the pseudo-random hopping pattern is to avoid interfering signals by not spending very much time on any specific frequency. If interference is present on any of the channels in the hopping pattern, even though the RF signal will experience interference from time to time, it will be minimized by the small amount of time spent transmitting on that frequency (see [Figure 16-13](ch16.html#infrastructure-based_wireless_lan) and [Figure 16-14](ch16.html#ad_hoc-based_wireless_lan)).

![Infrastructure-based wireless LAN](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1613.png)

**Figure 16.13. Infrastructure-based wireless LAN**

![Ad hoc-based wireless LAN](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1614.png)

**Figure 16.14. Ad hoc-based wireless LAN**

802.11a ventured into a different frequency band, the 5.2 GHz UNII (Universal Networking Information Infrastructure) band, and the specifications were supposed to achieve data rates up to 54 Mbps. This was seen as a big incentive for 802.11a against 802.11b, which had only a maximum of 11 Mbps. 802.11a uses a discrete multi-tone modulation technique called orthogonal frequency division multiplexing (OFDM), unlike 802.11b, which has just a single carrier at any one time. OFDM is a scheme that allows data to be reliably transmitted over channels, even in multi-path environments. OFDM divides the given band into chunks of smaller bands whose carriers are arranged in a particular pattern. The frequency spacing and time synchronization of the carriers in the various bands are chosen in such a way that the carriers don't interfere with each other. This gives the name "orthogonal" to the otherwise normal frequency division multiplexing. It uses 12 discrete channels with adaptive bit rates at 6, 9, 12, 18, 24, 36, 48, and 54Mbps. A drawback with 802.11a is that it places operations in the 5.2 GHz frequency range, which is also used by the military in various parts of the world and could trigger security issues.

In the later part of 2001, the IEEE 802.11 group felt a necessity to enhance the operating rates in the 2.4 GHz ISM band to match those of the IEEE 802.11a standard. With the adoption of a variety of technologies by various commercial vendors (Intersil, TI, and others), IEEE 802.11g provided a standard that would give 54 Mbps, yet retain compatibility with the 802.11b devices. The main intention of the 802.11g standard was to maintain compatibility with the already existing 802.11b devices that made a total adoption of OFDM technology unsuitable. Yet 802.11g was able to combine the merits of both 802.11a and 802.11b without any commercial issues. It uses OFDM technology at higher data rates (>20 Mbps) and Complementary Code Keying (CCK) Spread Spectrum for low bite rate operations to maintain compatibility with 802.11b devices. This makes 802.11g a wholesome technology and a definite extension of 802.11a/b in every respect. Data rates are normally dynamic to encourage proper selection of bit rates depending on received signal strength, distance between two communicating devices, and other environmental factors. IEEE 802.11g has 1, 2, 5.5, and 11Mbps for CCK modulation and 6, 9, 12, 18, 24, 36, 48, and 54 MBPS for OFDM operation.

Market and deployment issues always have considerable weight when any technology is adopted. Initially, IEEE 802.11b devices were prevalent as it was the first successful technology to make headway as a full-fledged wireless technology. Because IEEE 802.11a was totally non-compliant with 802.11b devices, their emergence was relatively curtailed. Moreover, deployment, management and security issues had a considerable impact on the emergence of wireless local area networks. Because the wireless medium is highly susceptible to noise and has a comparatively higher bit error rate compared to wired mediums, devices were sought for sophisticated coding and modulation schemes. Security issues such as authentication and encryption over the air are still major stumbling blocks for adoption of wireless technologies in sensitive areas. Security breaches such as war driving (the activity of looking for unprotected wireless access points) could be easily achieved because no definite limitations exist for wireless transmissions. The emergence of IEEE 802.11g to suit the higher bandwidth market was certainly a welcome development, but it has yet to be an answer to all questions.

# IEEE 802.11 Wireless Security

The original 802.11 wireless LAN specifications defined a security option, Wired Equivalent Privacy (WEP). In WEP, a shared key is configured into the access point and its wireless clients. In the 802.11 standard, data is transferred in the clear by default. If confidentiality is desired, the WEP option encrypts data before it is sent. The WEP algorithm is the RC4 symmetric cipher. The algorithm employs a secret key that is shared between a mobile station (for example, a laptop with a wireless Ethernet card) and a base station access point to protect the confidentiality of information being transmitted on the LAN. The transmitted packets are encrypted with a secret key and an Integrity Check (IC) field composed of a CRC-32 check sum attached to the message.

WEP is not considered secure today so, at a minimum, WPA should be used; if the hardware supports it, WPA2 provides even more security.

By removing the need to wire a network in the home, the cost of adoption and benefit of mobility within the home and low cost of components make wireless networking an efficient way to install a home network. This segment of the market is much less aware and less concerned about the security implications associated with wireless networks. At the same time, wireless adoption within the corporate world and by medium-sized businesses has been severely inhibited by security concerns associated with transmitting sensitive corporate data over the air. While home users are less aware and less concerned about the security implications associated with wireless networks, wireless LANs have struck a nerve with security conscious IT departments. Until recently, there has been no straightforward, cost effective way to deploy wireless security. IT departments have been forced to forbid the deployment of wireless networks, overlook the security concerns, or install costly Virtual Private Network solutions to build protected data tunnels between each wireless user and the core network.

## The wireless network security stack

This section will look at the various security protocols that can be used in wireless networks.

### Physical security and Wired Equivalent Privacy

The lowest level of security that can be deployed in a wireless network is the Wired Equivalent Privacy standard (WEP). WEP allows for 40-bit or 128-bit keys to be entered in both the access point and the client's computer or network to encrypt the traffic between the PC and the access point. The challenge however, is the inherent weakness of WEP security. With a little digging, unauthorized users can easily find software on the Internet that can be used to crack WEP encryption by capturing the network traffic over the air and deciphering the key. Once the WEP key is deciphered, the traffic can be read in the clear, overcoming the encryption on the network traffic.

Another challenge of WEP-only encryption is the need to key each client device and each access point with the same encryption key. In environments with more than 10 users, the management of these keys, and manual re-keying whenever a user is removed from the network, can be burdensome. To address the inherent flaws of WEP, the Wi-Fi Alliance has created a new standard called Wi-Fi Protected Access (WPA). WPA combines two components to provide strong security for wireless networks. The first component is called Temporal Key Integrity Protocol (TKIP), which replaces WEP with a much stronger protocol. TKIP provides data encryption enhancements including a key mixing function, a message integrity check, and a re-keying mechanism that rotates through keys faster than any sniffer software can decode the encryption keys. Through these enhancements, TKIP addresses all of WEP's known encryption vulnerabilities. A more robust replacement for TKIP being debated in the IEEE standards committees is a new encryption standard called 802.11i. This standard will require new hardware components. The second component of WPA is 802.1X security, which addresses the key management issue with user authentication. 802.1X is the second layer of security, which, when combined with TKIP, provides a strong level of wireless security. 802.1X provides a security mechanism through which a user must be authenticated before he is allowed access to the network.

### Extensible Authentication Protocol

The WEP-based encryption is completely breakable. Realizing this lapse of WEP, the IEEE work group "1x" is working on a new layer-2 protocol called the EAP (Extensible Authentication Protocol). Under 802.1x, switches and access points act as the gatekeepers to the network. EAP creates a framework for transportation of request authentication and encryption information. It also provides a mechanism for supporting various authentication methods over wired and wireless networks. An authentication, authorization, and accounting (AAA) client (also known as a network access server), such as an access point that supports EAP, need not have any understanding of the specific EAP type used in the EAP authentication process. The network access server tunnels the authentication messages between the peer (user machine trying to authenticate) and the AAA server (such as RADIUS). The network access server is aware only of when the EAP authentication process starts and when it ends. There are EAP types, such as LEAP (from Cisco Networks) and EAP-TLS (Transport Layer Security), in which the authentication is mutual: server authenticates user, and user authenticates server. Mutual authentication is usually required in a WLAN environment. One of the limitations of 802.1x is that the authenticator, an access point in a wireless network, is never authenticated by the client. The 802.1x authentication runs before the client gets assigned an IP address. In order to provide an IP address based on authentication results, a mechanism (DHCP) has to be used. In this case, when a client is successfully authenticated, using TLS over EAP for example, the AP saves authentication results locally. These results are appended by the access points to DHCP requests sent by the client. The DHCP server may use this information to select an address from the appropriate pool. Even when the authentication protocol running on top of EAP provides mutual authentication, this occurs between the client and the authentication server.

### Key management

Key management has been one of the biggest hurdles from a security perspective in maintaining large scale network installations. Public Key Infrastructure (PKI) functions permit detection of messages that have been tampered with or altered during transmission. Furthermore, PKI-enabled digital commitments are legally binding and cannot be falsely denied later. Managing the distribution of keys for the various parties involved is a very sensitive issue as the keys themselves have to pass the network when the involved parties are remote. The SSL in wired network setups would not be as effective in the case of wireless access devices. Many problems arise when key management is attempted in ad-hoc networks. The *resurrecting duckling (the ability to re-use keys)* solution proposed by Anderson is quite manageable for present network limits in ad hoc setups. In the future, when ad-hoc networks begin to gain ground in many security-sensitive environments (battlefields, fire rescue, natural disaster relief, and the like), and the number of nodes itself increases, a newer, more robust solution will have to be employed. Even though the perception that the security levels of any operation are often dictated by user applications, a firm base line security feature is good to have for all operations.

### Lightweight Extensible Authentication Protocol

Cisco offers its own flavor of EAP, called LEAP, which is implemented in Cisco access points. Because Cisco hardware is prevalent in the corporate world, some network administrators may want Wi-Fi clients that support LEAP. Cisco is licensing LEAP and other features that leverage a Cisco Wi-Fi infrastructure to suppliers of chipsets for Wi-Fi clients as part of a program it calls Cisco Compatible Extensions (CCX). If you plan to deploy or have deployed Cisco access points, seek out hardware that is CCX-certified. WPA is now available in Wi-Fi client hardware. For those who implemented wireless networks before WPA was available, many Wi-Fi chipset vendors offer software or firmware updates to bring older wireless networks in line with the WPA security level. The next developments in Wi-Fi security are being defined by the 802.11 security task force, the IEEE 802.11i working group. Basically, 802.11i combines WPA with the U.S. government encryption standard, the Advanced Encryption Standard, or AES. WPA is an interim security step. If you are looking to future-proof your wireless clients, look for Wi-Fi chipsets with hardware-based AES that provide the latest functionality without the performance penalty expected from implementations of AES in software.

### Tunneled TLS and Protected Extensible Authentication Protocol

Both Tunneled TLS and PEAP use the inherent privacy of the TLS tunnel to safely extend older authentication methods, such as username/password or token card authentication, to the wireless network. Both are two-stage protocols that establish a strongly encrypted "router" tunnel LS tunnel in stage one and then exchange authentication credentials through an "inner" method in stage two. Both Tunneled TLS- and PEAP-capable RADIUS servers can be used with existing authentication systems. RADIUS proxy abilities can extend existing databases, directories, or one-time password systems for use with wireless LANs. Tunneled TLS uses the TLS channel to exchange "attribute-value pairs" (AVPs), much like RADIUS. The flexibility of the AVP mechanism allows TTLS servers to validate user credentials against nearly any type of authentication mechanism. Tunneled TLS implementations today support all methods defined by EAP, as well as several older methods (CHAP, PAP, MS-CHAP, and MS-CHAPv2). PEAP uses the TLS channel to protect a second EAP exchange.

### Wireless WAN security

Most of the security concerns affecting wireless LANs are found in wired LANs, too. Fundamentally, there are two different means a mobile network may offer to transfer data in wide area networks: It can provide a packet-data network or it can use circuit-switched connections. CDPD (Cellular Digital Packet Data), Mobitex, and GPRS are all examples of packet data networks. In these cases, the mobile device has an IP address and it transfers data through the mobile network, which is connected to the Internet. If the IP address given to the device is fixed, then a minimal amount of authentication is also implicit in any packets originating from it.

Data communication over primarily voice networks, such as GSM, IS-136, and IS-95, is not quite as straightforward. Typically, a Point-to-Point Protocol (PPP) connection must first be made from the device to a dial-in server. The dial-in servers assign IP addresses and relay all the traffic between the device and any application servers. This implies some configuration at the mobile end. The user must specify a phone number and then authenticate to the dial-in server using an authentication protocol such as PAP, CHAP, or EAP. The Password Authentication Protocol (PAP) is based on unencrypted plain-text password exchange, which is highly prone to eavesdropping. The Challenge-Handshake Authentication protocol (CHAP) does not involve unencrypted password transfers; instead, the server issues a challenge to the remote location. The remote node responds to the challenge through the use of a hashing algorithm encrypting its username, session ID, and password. The server has the ability to change the encryption value by periodic checks conducted on the authenticity of the remote node, thus avoiding key reuse.

Wireless networks create challenges for network and security administrators. Close inspection using the three main security issues (authentication, confidentiality, and integrity) should be completed before ever deploying a wireless network. While few solutions are fully able to pass the authentication, accounting, and encryption test, a combination of technologies can provide satisfactory security. Standards such as 802.1x and 802.11i will alleviate many of the present wireless security concerns. Wide area networks are another major area into which wireless network security needs to be extended. I will discuss 802.1x in detail later in the chapter.

As pointed out, the WEP implementation is weak in both confidentiality and authentication, and with tools readily available on the Internet, WEP is easily broken and messages compromised. As a result, stronger privacy systems have been implemented for 802.11. The following sections will not only discuss the details of WEP security issues but will also provide more details on the solutions mentioned above.

## WEP

As previously noted, WEP uses the RC4 symmetric key stream cipher to protect the confidentiality of the transmitted messages. WEP also provides for a weak authentication of the user station to the access point, but not vice versa. This authentication is usually accomplished using a shared secret key to encrypt the data frames. The WEP symmetric key is comprised of two components, a variable, 24-bit Initialization Vector (IV) and a fixed 40- or 104-bit secret key. Because the secret key is seldom changed, the purpose of the IV is to thwart cryptanalysis against WEP by having the client use a different IV when encrypting message packets.

Because of the limited processing power in commodity-produced access points, the RC4 stream encryption algorithm is off-loaded to custom hardware. The hardware functions encrypt each message packet with a key that comprises the concatenation of a base secret key with an IV. The packet construction and the key composition are illustrated in [Figure 16-15](ch16.html#a_wep_message_and_key).

![A WEP message and key](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1615.png)

**Figure 16.15. A WEP message and key**

Note that the IV is transmitted as plaintext in the packet. When the packet is received at the access point, the hardware function retrieves the base secret key that it knows, concatenates it with the IV in the transmitted message packet, and uses this key to decrypt the packet.

However, because the IV is relatively short, packet monitoring will show repetitions of the IV and, thus, enable attackers to obtain the base secret key. One approach is to use the plaintext IV and discover WEP RC4 weak keys to mount a known plaintext attack. Researchers at UC Berkeley (`www.isaac.cs.berkeley.edu/isaac/wep-faq.html`) have shown that WEP security can be easily broken. Subsequently, a freely available program called AirSnort (additional tools for wireless security are discussed next) was widely distributed on the Internet; it can be used to break WEP encryption and read transmitted messages. WEP is also vulnerable to forgery and replay attacks, wherein an attacker can modify packets and retransmit them or capture packets and retransmit them at a later time.

WEP provides for open and shared key authentication. The following sections describe each option and their associated vulnerabilities.

### WEP open authentication

In WEP open authentication a client station provides a *Service Set Identity (SSID)* that is common to the stations on its network segment and its access point. This SSID authorizes and associates a client station to the access point. A vulnerability exists with this approach in that the access point transmits the SSID in the clear at intervals in management frames. Thus, the SSID is easily available to attackers to establish an association with the access point.

### WEP shared key authentication

The WEP *shared key architecture* was intended to implement secure authentication of the client by the access point through the following steps:

1. The client station transmits an authorization request.
2. The access point returns a challenge string in the clear.
3. The client chooses an IV.
4. Using the IV and secret base key, the client encrypts the challenge string.
5. The client station sends the IV and encrypted challenge string to the access point.
6. The access point also encrypts the challenge string using the transmitted IV and the same secret base key.
7. If the client's encrypted challenge string is identical to the challenge string sent by the client station, the association occurs.

The vulnerability in this process is that cryptanalysis can use the intercepted plain-text/cipher text pair and IV to determine the RC4 key. This attack is possible when all the IVs have been exhausted for a session and the IVs have to be reused. In this situation, when IV1 in a message is equal to IV2 in another message, the cryptanalysis proceeds as follows:

1. Ciphertext C1 = Plaintext P1 XOR [Stream Cipher RC4 with key generated through the use of K, IV1]
2. Ciphertext C2 = Plaintext P2 XOR [Stream Cipher RC4 with key generated through the use of K, IV2]
3. If IV1 = IV2, proceed to Step 4.
4. C1 XOR C2 = {Plaintext P1 XOR [Stream Cipher RC4 with key generated through the use of K, IV1]} XOR {Plaintext P2 XOR [Stream Cipher RC4 with key generated through the use of K, IV2]} = P1 XOR P2, the XOR of the two plaintexts.

With the Exclusive Or of the two plain-text items known corresponding to the transmitted cipher text items, dictionary attacks can be applied to determine the plain-text items.

## WEP security upgrades

Because of the weaknesses in WEP security, IEEE 802.11 established Task Group i (TGi) to develop approaches to address WEP problems. TGi had to consider a number of issues and constraints. One path was to redesign 802.11 security so as not to include any legacy WEP functions. Another path was to upgrade WEP security while keeping the same WEP architecture. Both approaches were chosen, resulting in the completely new 802.11i standard and the upgraded WEP encryption and integrity method called the *Temporal Key Integrity Protocol* (TKIP). The latter approach was necessary to accommodate the huge base of existing wireless WEP devices already deployed and to have improved security in place because of the anticipated delay in developing and finalizing the 802.11i standard. The installed WEP implementations have hardware-based WEP functions that cannot be easily modified, so the TKIP solution was chosen because it can be installed as a software upgrade to the legacy systems. In addition, because of the limited additional computing capability remaining on extant access points, the TKIP upgrade could not be computing resource–intensive. TKIP uses the *802.1X authentication architecture* as a basis for secure key exchange, so the next section briefly describes 802.1X as a precursor to an overview of the TKIP algorithms.

### 802.1X authentication

802.1X is a port-based authentication mechanism that operates under the *Extensible Authentication Protocol (EAP)* transport protocol (RFC 2284). For wireless LANs, the EAP protocol is known as EAP over LAN (EAPOL). EAPOL is applied to the exchange of challenges and responses between client stations, or *supplicants*, as they are called in the protocol, and an authentication server. The third entity in 802.1X is the *authenticator*, a dual access control port, similar to the access point. The authentication server is usually a RADIUS server, but other authentication servers can be employed. In this discussion, a RADIUS server is used. EAPOL supports a number of protocols, including Transport Layer Security (TLS), RFC 2246. A typical authentication process employing EAPOL proceeds as follows:

1. The supplicant sends credentials to the RADIUS server.
2. The RADIUS server provides credentials to the supplicant.
3. Upon mutual authentication, the protocol is used to establish session keys.
4. The session keys are used to encrypt the client station message.

In more detail, the sequence occurs in the following steps:

1. A conventional 802.11 association is established.
2. At this point, all non-802.1X traffic is blocked.
3. The RADIUS server sends a challenge to the supplicant (client station).
4. The client hashes the user-provided password as a response to the RADIUS server. This hash is sent to the RADIUS authentication server through the authenticator.
5. The RADIUS server uses the same process to compute the hash based on its database of user passwords.
6. If a match of the hashes is obtained, the RADIUS server generates a dynamic WEP secret key and sends it to the authenticator.
7. The WEP secret key is sent to the client via EAPOL key frames.
8. The secret keys are updated at specified intervals.

Because employing 802.1X for WEP encryption does not eliminate weak IV and IV collision vulnerabilities, TKIP was developed to address these and other WEP security weaknesses.

### Temporal Key Integrity Protocol

TKIP is built around the existing WEP security algorithm because of the necessity of not adding complex cryptographic algorithms whose execution would far exceed the spare CPU cycles available on most of today's deployed access points. [Table 16-5](ch16.html#tkip_upgrades_for_wep_weaknesses) lists the upgrades provided by TKIP in terms of the security weaknesses addressed.

**Table 16.5. TKIP Upgrades for WEP Weaknesses**

| Weakness | TKIP Upgrade |
| --- | --- |
| Correlation of IVs with weak keys | Per-packet key mixing function |
| Replay | IV sequencing discipline |
| Key reuse | Rekeying approach |
| Susceptibility to forgery | Message Integrity code (MIC) called Michael |

### Per-packet mixing function

The TKIP *per-packet key mixing function* addresses the problem of correlating IVs with weak keys by using a key that varies with time, or temporal key, as the WEP secret base key. It then uses the packet sequence counter and temporal key to construct the per-packet key and IV. These operations hide the relationship between the IV and the per-packet key and are illustrated in [Figure 16-16](ch16.html#tkip_per-packet_mixing_function).

![TKIP per-packet mixing function](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1616.png)

**Figure 16.16. TKIP per-packet mixing function**

The process in [Figure 16-16](ch16.html#tkip_per-packet_mixing_function) shows that using the Exclusive Or function for the local MAC address with the temporal key results in different client stations and access points generating correspondingly different intermediate keys. Thus, the per-packet encryption keys are different at every client station. The result of the total process is a 16-byte packet that corresponds to the input that is expected by existing WEP hardware.

### IV sequencing discipline

As a control against replay attacks, TKIP applies an IV sequencing discipline in which a receiver determines if a packet is out of sequence. If that condition is true, the receiver assumes it is a replay and discards the packet. A packet is defined as out of sequence if its IV is less than or equal to that of a previously correctly received packet. By using the WEP IV field as a packet sequence number, the procedure for detecting and countering replays is as follows:

1. New TKIP keys are used.
2. Receiver and transmitter initialize the packet sequence number to zero.
3. As each packet is transmitted, the packet sequence number is incremented by the transmitter.
4. The IV sequencing discipline is applied to determine if a packet is out of sequence and a replay has occurred.

This procedure is illustrated in [Figure 16-17](ch16.html#tkip_replay_sequence_checking).

![TKIP replay sequence checking](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1617.png)

**Figure 16.17. TKIP replay sequence checking**

#### Message Integrity Codes against forgery

An ideal *Message Integrity Code (MIC)* is a unique, unambiguous representation of the transmitted message that will change if the message bits change. Thus, if an MIC is calculated using an authentication key by a transmitting entity and sent with the message, the receiver can similarly calculate another MIC based on the message and compare it to the MIC that accompanied the message. If the two MICs are identical, in theory, the message was not modified during transmission.

In TKIP, the 64-bit MIC is called *Michael* and was developed by Niels Ferguson, an independent cryptography consultant based in Amsterdam, Holland. The TKIP MIC process is illustrated in [Figure 16-18](ch16.html#tkip_mic_generation_and_verification).

![TKIP MIC generation and verification](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1618.png)

**Figure 16.18. TKIP MIC generation and verification**

### Rekeying against key reuse

To protect against key reuse, 802.1X uses a hierarchy of master keys, key encryption keys, and temporal keys. The 802.1X temporal keys are used in the TKIP authentication and confidentiality processes. A temporal key set comprises a 64-bit key for the MIC process, as described in the previous section, and a 128-bit encryption key. A different set of temporal keys is used in each direction when an association is established. The material used to generate the temporal keys must be protected from compromise and this protection is accomplished by use of key encryption keys. The master key is needed to set up the key encryption keys. This process is summarized as follows:

- 802.1X defines that the authentication server and client station share a secret key, the master key.
- 802.1X defines that the authentication server and access point share a secret key, derived by the authentication server and client station from the master key and distributed by the authentication server to the access point.
- A new master key is used with each session (a session covers the time from authentication to when the key expires, is revoked, or when a client station no longer communicates).
- The master key is used to protect the communication of key encryption keys between a client station and the access point.
- The key encryption keys are employed to protect the transmitted keying material used by the access point and client to generate sets of temporal keys.
- The pairs of temporal keys are used for integrity protection and confidentiality of the data.

[Figure 16-19](ch16.html#key_hierarchy_for_rekeying) shows the relationships and locations of the three types of keys.

![Key hierarchy for rekeying](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1619.png)

**Figure 16.19. Key hierarchy for rekeying**

## 802.11i

The 802.11i wireless security standard was ratified in June of 2004. The IEEE 802.11 committee considers this specification a long-term solution to wireless security. It incorporates TKIP, 802.1X, and the Advanced Encryption Standard (AES). AES is a block cipher and, in 802.11i, processes plain text in 128-bit blocks. It uses the following set of keys:

- **A symmetric master key**—Possessed by the authentication server and client station for the positive access decision
- **A pairwise master key (PMK)**—A fresh symmetric key possessed by the access point and client station and used for authorization to access the 802.11 medium
- **A pairwise transient key (PTK)**—A collection of the following operational keys:**Key encryption key (KEK)**—Used to distribute the group transient key (GTK), which is an operational temporal key used to protect multicast and broadcast data**Key confirmation key (KCK)**—Binds the PMK to the client station and access point**Temporal key (TK)**—Protects transmitted data

Thus, 802.11i employs a 128-bit key, combines encryption and authentication, uses temporal keys for both functions, and protects the entire 802.11i packet. In relation to the authentication server and EAP, RADIUS and EAP-TLS are not officially a part of 802.11i, but are de facto standards for use in 802.11i.

The next sections explore the AES and its employment in 802.11i because it is the major component of and provides the increased security capabilities in the new standard.

### AES Counter and Cipher-Block Chaining modes

The two modes of operation of AES relative to 802.11i are Counter (CTR) and Cipher-Block Chaining (CBC).

In the CTR mode of operation, AES employs a monotonically increasing counter. The encryption process in the CTR mode is summarized as follows and is shown in [Figure 16-20](ch16.html#aes_ctr_mode):

1. The Message, M, is broken into 128-bit blocks: M1, M2, ... Mn.
2. The key is determined.
3. The counter is initialized to zero.
4. For each block processed, increment the counter by one.
5. For each block, the counter value is encrypted.
6. The encrypted counter value is XORed with the plain-text block, Mi, to generate the cipher text block, Ci.
7. When all the plain-text blocks have been encrypted, the initial counter value is prepended to the cipher text blocks to generate the message (counter0) C= (counter0){C1, C2,...Cn}.
8. The message is transmitted.
9. The receiver decrypts the message by reversing the process. It uses the prepended initial counter value as a starting point.

For security, the CTR mode requires a new, different key for every session.

The AES CBC mode employs an initialization vector for enhanced security and operates in the following steps:

1. The Message, M, is broken into 128-bit blocks: M1, M2, ... Mn.
2. A random initial IV value is chosen.
3. This first IV value is XORed with plain-text block M1.
4. Encrypted block C1 is generated by encrypting the result of the XOR in the previous step with the encryption key, K. C1 also becomes the next IV to be used in the XOR function with M2.
5. This process iterates until all plain-text blocks are encrypted.
6. The message to be transmitted is assembled by prepending the initial IV to the cipher text C= C1, C2, ...Cn.
7. The receiver performs decryption by using the prepended initial IV value and reversing the process.

![AES CTR mode](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1620.png)

**Figure 16.20. AES CTR mode**

A different, initial IV must be used for each new message to maintain security.

The steps in the CBC mode are shown in [Figure 16-21](ch16.html#aes_cbc_mode).

The AES CBC mode can also be employed to generate an MIC and ensure that a message has not been modified during transmission. The MIC is generated as follows:

1. The Message, M, is broken into 128-bit blocks: M1, M2, ... Mn.
2. An initial IV value that is known to the transmitter and receiver is chosen.
3. This first IV value is XORed with plain-text block M1.
4. A Tag block, MIC1, is generated by encrypting the result of the XOR in the previous step with the encryption key, K. MIC1 also becomes the next IV to be used in the XOR function with M2.
5. This process iterates until the last Tag block, MICn, is generated.
6. The Tag block, MICn, is appended to the transmitted message as an integrity check.

The receiver generates an MICn using the same algorithm and initial IV as the transmitter and compares it to the MICn received with the message. If the values match, the message is assumed to have been transmitted without modification.

[Figure 16-22](ch16.html#cbc_mode_for_mic_generation) illustrates AES MIC generation.

![AES CBC mode](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1621.png)

**Figure 16.21. AES CBC mode**

![CBC mode for MIC generation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1622.png)

**Figure 16.22. CBC mode for MIC generation**

### Application of AES in 802.11i

The AES is applied in 802.11i in the form of the AES — Counter with CBC-MAC (AES-CCM) protocol. AES-CCM applies the AES CTR mode for confidentiality of data and combination CBC-MAC mode for data integrity.

AES-CCM uses the same AES key for encryption and for generating an MIC. In addition, AES-CCM employs a 48-bit packet sequence counter. This counter is then applied in the CTR mode and in the generation of the CBC-MAC mode initialization vector. The following steps describe this process:

1. Concatenate the source MAC address, the packet sequence counter, a 16-bit per-packet block counter, and a 16-bit string to form the CTR mode counter and CBC MAC-IV. The 16-bit string differentiates the two concatenation results as being the CTR mode counter or the CBC-MAC IV.
2. Increment the packet sequence counter.
3. The CCM-MAC IV and secret AES key are used to compute an MIC over the message packet, including the source and destination addresses.
4. Truncate the MIC to 64 bits.
5. Encrypt the packet and append MIC, applying the CTR mode counter and secret AES key.
6. Insert the packet sequence counter number in between the 802.11 header field and the encrypted message data.
7. Transmit the packet.

On the receiving end, the packet sequence counter is obtained from the message packet and checked for replay. If the message is valid, the packet sequence counter is used to generate the CTR mode counter and the CBC-MAC IV. Then, the process steps used in the transmission process are reversed.

The AES-CCM mode protects against forgeries through the use of an MIC, protects against replays by checking the packet sequence counter, encrypts the source and destination addresses, and does not use an initialization vector or counter value with the same AES secret key.

### Additional 802.11i capabilities

802.11i provides for pre-authentication for roaming and, also, a Pre-Shared Key (PSK) mode. In this mode, there is no authentication exchange and a single private key can be assigned to the entire network or on a per-client station pair. PSK is amenable for use in ad-hoc and home networks. The PSK mode uses the PKCS#5v2.0PBKDF2 key derivation function to produce a 256-bit PSK from an ASCII string password. RFC 2898, PKCS #5: Password-Based Cryptography Specification Version 2.0 describes this operation, which applies a pseudorandom function to derive keys. The PSK mode is vulnerable to password/passphrase guessing using dictionary attacks.

### Tools for testing and security wireless

The following are some tools that can be used to test and validate the security of a wireless network:

- **Kismet** is an 802.11 layer2 wireless network detector, sniffer, and intrusion detection system. Kismet will work with any wireless card that supports raw monitoring (rfmon) mode, and can sniff 802.11b, 802.11a, and 802.11g traffic. It will work on most Linux and UNIX platforms.
- **bsd-airtools** is a package that provides a complete toolset for wireless 802.11b auditing. It contains a WEP cracking application, a netstumbler clone, and a few tools for Prism2 debug modes. Most of the utilities only fully work with a Prism2 chipset-based card.
- **Aircrack** is a 802.11 WEP key cracker. It implements the so-called Fluhrer-Mantin-Shamir (FMS) attack, along with some new attacks by a talented hacker named KoreK. When enough encrypted packets have been gathered, aircrack can almost instantly recover the WEP key. It runs under Linux and Windows.
- **AirSnort** is a wireless LAN (WLAN) tool that recovers encryption keys. AirSnort operates by passively monitoring transmissions and computing the encryption key when enough packets have been gathered. It uses the Prism2 chipset.
- **Hotspotter** passively monitors the network for probe request frames to identify the preferred networks of Windows XP clients, and will compare it to a supplied list of common hotspot network names. If the probed network name matches a common hotspot name, Hotspotter will act as an access point to allow the client to authenticate and associate with it.
- **Wellenreiter** is a wireless network discovery and auditing tool. Prism2, Lucent, and Cisco based cards are supported. It can discover networks (BSS/IBSS), and automatically detects ESSID broadcasting or non-broadcasting networks and their WEP capabilities and the manufacturer. DHCP and ARP traffic are decoded and displayed to give you further information about the networks. An ethereal/tcpdump-compatible dumpfile and an Application savefile will be automatically created. There are two versions for Linux, a GTK/Perl version and a newer C++ version with a QT front end for desktop and an Opie front end for Linux handhelds such as the Zaurus.
- **WepLab** is a tool designed to teach how WEP works, what different vulnerabilities it has, and how they can be used in practice to break a WEP-protected wireless network. WepLab is more of a Wep Security Analyzer, designed from an educational point of view. The author has tried to leave the source code as clear as possible, running away from optimizations that would obfuscate it. Weplab works under any flavor of Linux for i386 and PPC, MacOSX and Windows NT/2000/XP.
- **Prismtumbler** is a wireless LAN (WLAN) that scans for beacon frames from access points. Prismstumbler operates by constantly switching channels and monitors any frames received on the currently selected channel. Prismstumbler uses AirSnort.
- **WEPCrack** is a tool for breaking 802.11 WEP secret keys. WEPCrack was the first of the WEP encryption cracking utilities.
- **SNR tool** helps the network administrator collect signal/noise-rate statistics from Lucent Wireless AccessPoint devices via SNMP, store it in a MySQL database, and view summary graphs via CGI-module.
- **APTools** is a utility for Windows and UNIX that queries ARP Tables and Content-Addressable Memory (CAM) for MAC Address ranges associated with 802.11b access points. It will also utilize Cisco Discovery Protocol (CDP) if available. If a Cisco Aironet MAC address is identified, the security configuration of the access point is audited via HTML parsing.
- **The Rice Monarch Project** develops protocols for adaptive mobile and wireless networking. The project was formerly hosted at CMU.
- **KOrinoco** is is a KDE clone of the Lucent Orinoco client manager.
- **Wavemon** is a monitoring application for wireless network devices. It currently works under Linux with devices that are supported by the wireless extensions by Jean Tourrilhes (included in Kernel 2.4 and higher), e.g. the Lucent Orinoco cards.
- **GNOME Wireless Applet** is a wireless link quality monitor panel applet for GNOME. It reads the link quality out of `/proc/net/wireless` and reports quality by altering color, like a mood ring.
- **Gkrellm wireless plug-in** monitors the signal quality of your wireless networking card (if its driver supports the Linux wireless extension API or you use Freebsd's wi0 interface).
- **NetStumbler** displays wireless access points and SSIDs, channels, checking whether WEP encryption is enabled and signal strength. NetStumbler can connect with GPS technology to accurately log the precise location of access points.
- **Ministumbler** is a smaller version of NetStumbler designed to work on PocketPC 3.0 and PocketPC 2002 platforms. It provides support for ARM, MIPS, and SH3 CPU types.
- **Btscanner** allows you to extract as much information as possible from a Bluetooth device without the requirement to pair. It extracts HCI and SDP information, and maintains an open connection to monitor the RSSI and link quality.
- **Fake AP** is the polar opposite of hiding your network by disabling SSID broadcasts. Black Alchemy's FakeAP generates thousands of counterfeit 802.11b access points. As part of a honeypot or as an instrument of your site security plan, FakeAP confuses Wardrivers, NetStumblers, Script Kiddies, and other scanners.
- **Redfang v2.5** is an enhanced version of the original Redfang application that finds non-discoverable Bluetooth devices by brute-forcing the last six bytes of the device's Bluetooth address and doing a `read_remote_name()`.
- **SSID Sniff** is a tool to use when looking to discover access points and save captured traffic. It comes with a configured script and supports Cisco Aironet and random prism2 based cards.
- **WiFi Scanner** analyzes traffic and detects 802.11b stations and access points. It can listen alternatively on all 14 channels, write packet information in real time, and search access points and associated client stations. All network traffic may be saved in the libpcap format for post analysis.
- **wIDS** is a wireless IDS. It detects the jamming of management frames and could be used as a wireless honeypot. Data frames can also be decrypted on-the-fly and re-injected onto another device.
- **WIDZ** is a proof-of-concept IDS system for 802.11 wireless networks. It guards access points (APs) and monitors local frequencies for malicious activity. It detects scans, association floods, and bogus/Rogue APs. It can also be integrated with SNORT or RealSecure.

# Bluetooth

Bluetooth is a peer-to-peer, short-range protocol named after Harald Bluetooth, the king of Denmark in the late 900s. It is used to connect cellular phones, laptops, handheld computers, digital cameras, printers, and so on. It is defined in IEEE standard, IEEE 802.15 and has the following characteristics:

- **FHSS**—Hops 1,600 times per second among 79 RF channels
- **Transmission rate**—1 Mbps
- **Transmission distance**—About 30 feet
- **Frequency band**—2.4 Ghz to 2.5 Ghz
- **Transmitting power**—1 milliwatt, which minimizes interference with other networks (cell phones can transmit up to 3 watts of power)
- **Transmission range extension**—Range can be extended to 300 feet by increasing transmitting power to 100 milliwatts
- **Number of devices on the network**—8

Because FHSS is used, other Bluetooth networks can exist in the same area without any mutual interference. Bluetooth devices operate by setting up a personal area network (PAN) called a *piconet* based on the devices' assigned addresses. A Bluetooth piconet operates in the following manner:

- As an ad hoc network.
- All Bluetooth devices are peer units.
- Different piconets have different frequency hopping sequences to prevent interference.
- All devices on the same piconet are synchronized to the frequency hopping sequence for that piconet.
- One device operates as a master and the other devices operate as slaves (point-to-multipoint topology).
- A maximum of seven active slaves can exist on a piconet, each assigned a 3-bit active member address.
- Up to 256 inactive (*parked*) slaves that are synchronized to the frequency-hopping sequence can be assigned to the piconet. They can activate rapidly because they are synchronized.

Bluetooth security uses challenge response protocols for authentication, a stream cipher for encryption, and dynamic session keys.

# Wireless Application Protocol

The Wireless Application Protocol (WAP) is widely used by mobile devices to access the Internet. Because it is aimed at small displays and systems with limited bandwidth, it is not designed to display large volumes of data. In addition to cellular phones and PDAs, WAP is applied to network browsing through TV and in automotive displays. It has analogies to TCP/IP, IP, and HTML in wired Internet connections and is actually a set of protocols that covers Layer 7 to Layer 3 of the OSI model. Because of the memory and processor limitations on mobile devices, WAP requires less overhead than TCP/IP.

WAP has evolved through a number of versions, the latest being version 2.0. WAP 2.0 includes support for the transmission and reception of sound and moving pictures over telephones and other devices, as well as providing a toolkit for development and deployment of new services, such as Extensible Hypertext Markup Language (XHTML).

The WAP architecture comprises the following levels:

- **Application layer**—Contains the wireless application environment (WAE) and is the direct interface to the user. The Application layer includes the following:The Wireless Markup Language (WML)A microbrowser specification for Internet accessWMLScript (development language)
- The Handheld Device Markup Language (HDML) is a simpler alternative to and actually preceded WML. HDML contains minimal security features, however. Another alternative is Compact HTML (C-HTML). Used primarily in Japan through NTT DoCoMo's i-mode service, C-HTML is essentially a stripped-down version of HTML. Because of this approach, C-HTML can be displayed on a standard Internet browser.
- **Session layer**—Contains the Wireless Session Protocol (WSP), which facilitates the transfer of content between WAP clients and WAP. This layer provides an interface to the WAE through the following activities:Connection creation and release between the client and serverData exchange between the client and serverSession suspend and release between the client and server
- **Transaction layer**—Provides functionality similar to TCP/IP through the Wireless Transactional Protocol (WTP). WTP provides transaction services to WAP, including acknowledgment of transmissions, retransmissions, and removal of duplicate transactions.
- **Security layer**—Contains Wireless Transport Layer Security (WTLS). WTLS is based on Transport Layer Security (TLS) and can be invoked similar to HTTPS in conventional Web browsers. WTLS supports privacy, data integrity, DoS protection services, and authentication. WTLS provides the following three types of authentication:**Class 1 (anonymous authentication)**—The client logs on to the server, but in this mode, neither the client nor the server can be certain of the identity of the other.**Class 2 (server authentication)**—The server is authenticated to the client, but the client is not authenticated to the server.**Class 3 (two-way client and server authentication)**—The server is authenticated to the client and the client is authenticated to the server.Authentication and authorization can be performed on the mobile device using smart cards to execute PKI-enabled transactions. A specific security issue that is associated with WAP is the WAP GAP. A WAP GAP results from the requirement to change security protocols at the carrier's WAP gateway from the wireless WTLS to Secure Sockets Layer (SSL) for use over the wired network. At the WAP gateway, the transmission, which is protected by WTLS, is decrypted and then re-encrypted for transmission using SSL. Thus, the data is temporarily in the clear on the gateway and can be compromised if the gateway is not adequately protected. To address this issue, the WAP Forum has put forth specifications that will reduce this vulnerability and support e-commerce applications. These specifications include WMLScript Crypto Library and the WAP Identity Module (WIM). The WMLScript Crypto Library supports end-to-end security by providing for cryptographic functions to be initiated on the WAP client from the Internet content server. These functions include digital signatures originating with the WAP client and the encryption and decryption of data. The WIM is a tamper-resistant device, such as a smart card, that cooperates with WTLS and provides cryptographic operations during the handshake phase. A third alternative is to use a client proxy server that communicates authentication and authorization information to the wireless network server.
- **Transport layer**—Supports the Wireless Datagram Protocol (WDP), which provides an interface to the wireless networks. It supports network protocols such as GSM, CDMA, and TDMA. It also performs error correction.

The Public Key Infrastructure (PKI) for mobile applications provides for the encryption of communications and mutual authentication of the user and application provider. One concern associated with the mobile PKI relates to the possible time lapse between the expiration of a public key certificate and the reissuing of a new valid certificate and associated public key. This "dead time" may be critical in disasters or in time-sensitive situations. One solution to this problem is to generate one-time keys for use in each transaction.

# Future of Wireless

Over the past 10 years or so, an alternative to wired LAN structures has evolved in the form of the wireless LAN. The first-generation wireless LAN products operated in the unlicensed 900–928MHz Industrial Scientific and Medical (ISM) band, with low range and throughput offering (500 Kbps). They were subject to interference and came to market with little success in some applications. But they enjoyed a reputation of being inexpensive due to breakthroughs in semiconductor technologies. On the other hand, the band became crowded with other products in a short time, leaving no room for further development. The second generation in 2.40–2.483 GHz ISM band WLAN products boosted by the development of semiconductor technology was developed by a huge number of manufacturers. Using spread spectrum technology and modern modulation schemes, this generation's products were able to provide data rates up to 2 Mbps, but again the band became crowded since the most widely used product in 2.4 GHz is the microwave oven, which caused interference. Third-generation products assembled with more complex modulation in the 2.4 GHz band allow an 11Mbps data rate. In June 1997, the IEEE finalized the initial standard for wireless LANs: IEEE 802.11. The first fourth-generation standard, HiperLAN, came as a specification from the European Telecommunication Standard Institute (ETSI) Broadband Radio Access Network (BRAN) in 1996, operating in the 5 GHz band. Unlike the lower frequency bands used in prior generations of WLAN products, the 5 GHz bands do not have large potential interferers such as microwave ovens or industrial heating systems as was true in 900MHz and 2.4 GHz. In late 1999, the IEEE published two supplements to the 802.11: 802.11b and 802.11a, following the predecessors' success and interest from the industry. ETSI's next-generation HiperLAN family, HiperLAN/2, was proposed in 1999, operating on the same band with its predecessor, with the goal of providing high-speed (raw bit rate 54 Mbps) communications access to different broadband core networks and moving terminals.

## Broadband wireless–Wimax

Broadband 802.16 wireless technology (WiMax) can help service providers meet these challenges because it has the ability to seamlessly inter-operate across various network types. It also provides the flexibility to support very high bandwidth solutions where large spectrum deployments (i.e., > 10 MHz) are desired. As a result, 802.16 can leverage existing infrastructure, keeping costs down, while delivering the bandwidth needed to support a full range of high-value, multimedia services. 802.16 technology can provide wide area coverage and quality of service capabilities for applications ranging from real-time delay sensitive Voice-over-IP (VoIP) to real-time streaming video — all to ensure that subscribers get the performance they expect for all types of communications. Industry standards will help contribute to economies of scale for 802.16 solutions, so that high performance can be provided at reasonable cost.

## WiMax and 3G cellular technologies

WiMAX could be a serious threat to 3G because of its broadband capabilities, distance capabilities, and ability to support voice effectively with full QoS. This makes it an alternative to cellular in a way that Wi-Fi can never be, so that while operators are integrating Wi-Fi into their offerings with some alacrity (looking to control both the licensed spectrum and the unlicensed hotspots), they will have more problems accommodating WiMAX. But as with Wi-Fi, it will be better for them to bring down their own networks than let independents do it for them, especially as economics and performance demand force them to incorporate IP into their systems. Handset makers such as Nokia, Erickson, and Samsung will be banking on this as they develop smart phones that support WiMAX as well as 3G. WiMAX can slash the single biggest cost of deployment: access charges for linking a hotspot to a local phone or cable network. A high frequency version of 802.16 would allow entrepreneurs to blast a narrow, data-rich beam between antennas miles apart. A standards-based long distance technology will avoid many of the problems of high upfront costs, lack of roaming, and unreliability — problems that those pioneers encountered — but it will still need to gain market share rapidly before 3G takes an unassailable hold. Given the current slow progress of 3G, especially in Europe, and the unusually streamlined process of commercializing WiMAX, the carriers are indulging in wishful thinking when they say nothing can catch up with cellular.

## Beyond the future: IEEE 802.20

Meanwhile, another, separate IEEE standard in development seems to have significant overlap with WiMAX and IEEE 802.16e: the IEEE 802.20 standard. WiMAX and 802.16e are targeted for mobile users moving at speeds of up to 60 mph inside a WiMAX region (laptop users moving across a corporate campus, for example). But 802.20 is focused more on high-speed mobile users traveling across an extended metropolitan area at speeds of up to 150 mph. WiMAX/802.16 also differs from 802.20 in that it supports substantially higher data rates (up to 70 Mbps) than 802.20 (up to 1 Mbps). Both WiMAX/802.16e and 802.20 provide for mobility while enabling broadband connections across a much larger area than Wi-Fi and at higher data rates than what is commonly available to mobile clients today. Barring unexpected problems with the technology, it's likely we'll see both 802.16 and 802.20 products and services entering the market over the next few years, and we'll have to wait to see which standard gains traction for various user groups and applications.

Future architecture and building of wireless networks would depend on a variety of factors such as quality of service, transmission efficiency and range, bandwidth allowed, and mobility of the devices involved. With the increase in speed and range of wireless devices and communication, networks that were constrained basically to LANs have been able to grow and achieve MAN (Metropolitan Area Network) standards. Hotspots and other public area networks have shown proliferation over the past couple of years to substantiate that wireless networks will make the eventual difference. The emergence of WiMax/Broadband wireless devices as a standard has made this transition plausible. However commercial implications of wireless devices have been on the back burner because of issues such as security, transition cost, and management policy. Yet in the future, wireless technologies have the ultimate potential to coexist with conventional wireline networks to achieve higher advancements in the field of communication and networking.

# Summary

Nearly every industry has benefited from wireless technology. Hospitals and medical professionals can get instant updates on patients without being physically present at the hospital. Travelers can get confirmation of flight schedules on the run. Many commercial vendors have set up wireless network access available to their customers that may heighten customer interest. Many other applications could be conceived easily and implemented without great difficulty. However, wireless technology also has some of its own drawbacks: wireless channels may not be as fast (they have less bandwidth) compared to conventional wired channels. Also, the range of wireless access may not be very high. Security may be highly affected as wireless networks become more popular because administrators cannot direct the flow of wireless information easily, and coding and channel access schemes are different compared to wired channels. This will necessitate equipment manufacturers' adding the functionalities.

This chapter also reviewed the electromagnetic spectrum and focused on the UHF band for cellular phone communications. The major components of the cellular phone network were described, including the mobile station, cell tower, subscriber identity module, base transceiver station, and mobile switching center. The chapter explained TDMA, FDMA, and CDMA technologies along with a subset of CDMA, spread spectrum technology. In particular, DSS, FSS, and OFDM spread spectrum implementations were discussed. The chapter reviewed different generations of cellular systems development, including AMPS, TACS, NMT, GSM, UMTS, and IMT-2000. The chapter also explained and summarized the 802.11 wireless LAN standard, including its various upgrades and instantiations, such as 802.11, 802.11a, 802.11b, 802.11g, and 802.11i. The related 802.11 wireless security issues were explored and the various solutions to the original 802.11 WEP security deficiencies were developed. You also learned a little about Bluetooth piconets and the WAP protocols.
