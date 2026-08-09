# Chapter 10. Home Networks

**IN THIS CHAPTER**

- Features of a home network
- Broadband connection technologies
- Wireless connections
- Different approaches to connecting areas of your home
- Phone line and power line networks

Home networking is becoming more advanced, easier to use, and more prevalent. The major reasons people install home networks are to share Internet connections, resources, and network applications.

Home networks tend to be a mixture of different technologies. If you need to have mobile devices, then Wi-Fi networks will be one part of the mix. The two essential decisions you make concerning your home network are how to connect to the Internet and how to bridge different areas of your home together.

In this chapter, some of the common choices for home networking media are discussed in terms of their suitability. Ethernet, HomePNA, and HomePlug networking are described.

HomePNA is a phone line technology, while HomePlug is a power line connection technology. HomePNA and HomePlug are relatively new, and offer higher speeds than older technologies. With HomePNA, you connect devices by plugging adapters into a phone outlet. HomePlug uses adapters to allow devices to plug into your power lines. The Power over Ethernet standard is also described; this standard allows you to have mobile devices wherever an Ethernet cable can be run. These technologies are convenient alternatives to connecting areas of your home by pulling Ethernet cable through the wall.

Different broadband connection technologies are described in this chapter. Common technologies currently being offered — ISDN, DSL, cable modems, satellite connections, and fiber-optic connections — are described.

Home network servers offer the potential for managing your home network from a central location, as well as being able to share important network services. Microsoft Home Server is described briefly. Other home network appliances of this type have come to market but have not gained traction in the marketplace.

# Features of a Home Network

Home networking has experienced something of a renaissance over the last couple of years. Part of the current interest is due to people staying home more for entertainment, in part due to the proliferation of home computers, and part due to the public becoming more knowledgeable about networks. The advancement in home networking is also due to a number of new technologies that have been brought to market, and the fact that several other leading-edge technologies are also maturing. You see this trend in the home network market with the introduction of home servers, high-speed networking components, more sophisticated firewalls, and many other technologies. In this chapter, you see different types of wired technologies that you can use in your home to connect one device to another, often very conveniently over phone or power lines.

Most people create home networks to allow for the following functions:

- Share an Internet connection between two or more systems
- Share resources such as storage, printers, and other peripherals
- Back up systems remotely
- Transfer audio/video content for home entertainment purposes
- Use Voice over IP (VoIP) telephony
- Allow for system mobility for laptops, PDAs, and other mobile devices
- Play multiplayer games using computers or gaming consoles

These needs make certain choices entirely predictable:

- If you need mobile connectivity, you should opt for Wi-Fi on your network in the locations where you move devices around.
- If you want to transfer large files, then you need to examine the throughput of the links that will carry the traffic. As a general rule of thumb, AV multimedia content requires at least 100 Mbits/s throughput to be practicable, and the more the better.
- If you have different unconnected areas in your home, consider how you connect them. Common choices for connecting different areas in the home are to pull Ethernet cable, phone line, or power line connections, or to bridge the distance with Wi-Fi.
- Sharing an Internet connection argues for the use of a security appliance such as a firewall/gateway/router or a server or appliance that provides a function such as Network Address Translation (NAT). Placing a firewall between the Internet and your home network is the single best investment you can make to safely share an Internet connection.
- Networked resources such as printers, file shares, and other peripherals are supported in all of the commonly used desktop operating systems. Depending upon the granularity of access required, you may be satisfied with peer-to-peer network access; for a greater numbers of systems, and finer control, you may want to consider a server or server appliance with a central security system.

Common choices for home network connectivity are:

- Ethernet (wired/RF over wires)
- Wi-Fi based on IEEE 802.11x (wireless)
- Phone line (wired) based on HomePNA, for example
- Power line (wired) based on HomePlug, for example
- Bluetooth (wireless/RF)

Wireless technologies are very popular in home settings because of their flexibility, and so most home networks include wireless access. Wireless technologies such as Wi-Fi and Bluetooth are described in detail in [Chapter 14](ch14.html), but are mentioned to provide context in this chapter. Most people opt for a mix of technologies in their home networks. [Table 10.1](ch10.html#home_networking_technologies) shows some of the common technologies in use on home networks and compares important characteristics such as speed or throughput, technology types, cost, reliability, security and privacy, along with a summary of pros and cons of each.

**Table 10.1. Home Networking Technologies**

| Type | Throughput/Range | Used With | Cost | Reliability | Security and Privacy | Pros | Cons |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Ethernet (802.3, 802.5)** | 1 Gbits/s over Cat5e cable. Range 500 ft. or 164 m for 10Base-T. Others vary. | AV, C, R, and S | High | High | High | Fastest method used. Widest standard and largest number of devices sold. Greatest flexibility. | Expensive, especially as a retrofit. Requires dedicated wiring. Installation can be involved. |
| **Bluetooth (Bluetooth Special Interest Group, or SIG)** | 1 Mbits/s over RF range of 30 ft. (10 m) | C, CD, and M | Moderate | Good | Moderate | Self-configuring and mobile. Low cost. Supported by computers, peripherals, and handhelds. A small amount of setup is required. | Low speed and small range. |
| **Wi-Fi (IEEE 802.11x standards)** | 600 Mbits/s for 802.11n, 54 Mbits/s for 802.11g over either 2.4 or 5 GHz RF bands. Range 300 ft. for 802.11n omni-directional, 2 mi. with highly directional antennas. | AV, C, M, and R | Low to high | Good | Moderate | Standards-based, large number of devices available. Flexible, newer standards are fast. Good interoperability. | Costly, and limited range. Subject to interference and noise. Requires some setup. |
| **HomePNA phone networking (HomePNA Association 3.1 and ITU G9954)** | 320 Mbits/s over phone lines. Range 1,000 ft. or 333 m. | AV, C, CD, R, S | Low | High | Good | Can be fast, uses wiring in place. Low cost. Minimal installation. | Devices still require network connectivity. |
| **HomePlug power line networking. (IEEE P1901)** | 200 Mbits/s for AV, 14 Mbits/s for 1.0. Range ca. 3,000 ft. or 1,000 m. | AV, C, CD, M, R, and S | Moderate | Low to moderate | High | Fast, uses power line wiring in place. Very convenient. Minimal installation. | Very difficult transmission environment. Requires that power lines be locally available. |

### Note

Legend: AV = Multimedia, C= Communications, CD = Control devices, M = Mobile devices, R = Resource sharing, and S = Scheduling.

# Broadband Connections

The word broadband has many different meanings. It can refer to a wide spectrum of frequencies over which communications are sent, or it can apply to a high-speed connection to a network or the Internet. It is as a high-speed feed for the Internet that most home users would apply the term. Broadband penetration as a percentage of the population is considered by many economists to be a leading economic indicator.

By one definition, broadband is defined by the throughput through the system, with the lowest transmission speed being several times higher than is possible to achieve with a dial-up modem. The United States Federal Communications Commission in 2008 defined a broadband connection as one that has a download throughput of over 768 Kbits/s. In Europe, the International Telecommunications Union Standardization Sector set the base for broadband at 1.5 Mbits/s, or the speed of primary rate ISDN.

The minimum requirement for broadband tends to rise over time. The definition in terms of download speed is made intentionally because most people's broadband connections are much faster downloading than uploading content; that is, most broadband connections are asymmetric.

When an ISP rates its broadband connection speed, it typically does so under favorable conditions. Many services that share bandwidth among a group of subscribers, such as a neighborhood or apartment building, tend to slow down considerably at times of high usage. To combat this problem, many ISPs have resorted to techniques such as traffic shaping, throttling, or transfer limits in order to maintain an acceptable performance.

The most common broadband connections in the United States at the moment are based on digital subscriber line, or DSL, technology and cable modems. Fiber-optic networks are in the process of being rolled out by several companies and are available in limited geographical areas.

Among the broadband technologies in common use are:

- **Integrated Service Digital Network (ISDN) telephone-based data service**. ISDN is sold either in a basic rate format (ISDN-BRI) with two channels of DS0, 64 Kbits each, for a total of 128 Kbits/s, or as a primary rate format (ISDN-PRI) with 23 DS0 lines having a bandwidth of 1.544 Mbits/s. In Europe, ISDN-PRI involves 30 DS0 channels and has a bandwidth of 2.048 Mbits/s. ISDN has become less popular as consumers opt for either DSL or cable modem technologies.DS0 is a holdover from phone line systems; it represents the allocation of a 64 Kbits/s channel for voice communications.NoteISDN and DSL are is described in more detail in [Chapter 13](ch13.html).
- **Digital Subscriber Lines (DSLs)**. DSL uses telephone lines to provide digital services and Internet connectivity to customers. Most DSL sold is Asymmetric DSL, or ADSL. Download throughput over DSL lines ranges from 256 Kbits/s to 2.4 Mbits/s; upload speeds of 128 Kbits/s to 256 Kbits/s are typical for this technology.
- **Cable modems**. This technology is popular in North America, Europe, Australia, New Zealand, and parts of Central America. Typical throughput using a cable modem varies between 1 Mbits/s to 6 Mbits/s for downloads, and between 128 Kbits/s and 768 Kbits/s uploads. The technology is theoretically capable of supporting speeds as high as 30 Mbits/s. Cable modems use a shared connection among local users, and so speeds depend on the level of activity at any one time.Cable modems are network bridge (Data Link layer, or Level 2) devices that connect home networks to the Internet through a cable television system. On the network side, cable modems support Ethernet, and on the cable side, they support DOCSIS (Data Over Cable Service Interface Specification) as the Physical layer technologies. DOCSIS was created out of Motorola's CDLP (Cable Data Link Protocol) Physical layer technology and the MAC layer created by LANcity for use with NTSC broadcasts. In Europe, a version of the technology compatible with the PAL broadcast standard, called EuroDOCSIS, is used.
- **Satellite connections**. The use of satellites to provide Internet access is popular in rural areas where it is impractical to run different forms of cables. Systems use geostationary orbit satellites that are as high as 22,236 mi. (35,786 km) above sea level on the Earth, or 42,164 km from the Earth's center. An antenna must be fixed to the direction of the satellite.**Communications through satellites** suffer a considerable latency (about 200 milliseconds) because of the distance involved. As a general rule, download throughput is competitive with other broadband technologies, between 256 Kbits/s and 2.048 Mbits/s, but much slower for uploads, between 64 Kbits/s and 128 Kbits/s. The latency and slow upload speeds have tended to limit the use of satellite broadband technology.
- **Fiber-optic connections**. Fiber-optic broadband connections are now being offered in the United States by companies such as Verizon (FiOS), SBC, and Qwest, among others. These connections allow Internet access, telephone, and TV services to be delivered to consumers who are using a fiber-optic connection. The service can be sold in a number of different speeds, ranging from 10 Mbits/s to 50 Mbits/s download, and 2 Mbits/s to 20 Mbits/s upload.

# Wireless Connections

Wireless connections are a very convenient method for networking various devices on a home network. Some home networks rely entirely on wireless connections for all devices, but most use wireless connections for devices that are mobile in a home or as links between areas of the home that aren't conveniently wired together. Many ISPs provide broadband routers with wireless capabilities as part of their service.

Nearly all wireless networking devices sold for the home market are based on one of the IEEE 802.11 standards, which define a set of technologies that use public radio frequency bands that fall in the 900 MHz to 5 GHz frequencies. The technology goes under the trademark Wi-Fi, an industry trade group that manages the standards and ensures that chipsets and the devices that use them are interoperable.

### Note

[Chapter 14](ch14.html) describes wireless network technologies in detail. It is entirely devoted to the Wi-Fi standard and goes into great detail on the nature of each of the standards, how the bands are utilized, and how to build Wi-Fi networks or links from different components. [Chapter 14](ch14.html) also describes the different methods used to encode Wi-Fi signals, as well as how Wi-Fi connections need to be configured.

# Wired Connections

In the previous section, your home network's broadband connection to the Internet was considered. If you connect a wireless router to your Internet connection and all of your devices are wireless, or if you were lucky enough to move into a new house that is wired for Cat5e or Cat6 cable in every room, then your work is done. Most people aren't so lucky. The most common situation is that you have devices scattered around in different areas of your home and you've networked those areas individually, but are faced with the problem of connecting the areas together. Different areas in a home exist when you have rooms that aren't connected together by a network connection, for example an upstairs bedroom, a den on the first floor, and an office in the basement.

You could decide to have an electrician come in and pull cable through the wall to connect those areas together, or do it yourself. Pulling cable is difficult and often expensive, but it does provide the fastest speed connections when you are done. There are many homes in which pulling cable simply isn't practical or even worthwhile. In the sections that follow, different alternatives are presented that show how you can use wiring that is already in your home and in place (phone lines and power lines) to provide the missing links that connect up all of those separate networked areas. Among the technologies that are described in the following section are Ethernet wiring, HomePNA phone line connections, Power over Ethernet (PoE), and HomePlug Powerline networking over power lines.

## Ethernet

Direct Ethernet connections to WANs are uncommon in the area of home Internet connections. However, this technology is offered as a business service and may someday become available for consumers. The IEEE 802.3ah standard defines a set of protocols for Ethernet used on first or last mile connections.

Ethernet in the First Mile (EFM) can be used over:

- **Copper wire**. EFM over Copper (EFMCu) is used over voice-grade wiring and can be aggregated into multiple concurrent connections. The two types of EFMCu defined are 2BASE-TL and 10PASS-TS.
- **Long wavelength fiber**. Ethernet can connect using either single or dual strand fiber.
- **Point to Multipoint (P2MP) fiber**. Ethernet connections of this type are sold under the name Ethernet over Passive Optical Networks (EPON).

IEEE's EFM standard also describes how to install, manage, and administer Ethernet connections, as well as how to have these technologies interoperate with other commonly used technologies. EFM EPON development is now part of the IEEE Metro Ethernet Forum group; they are currently working on a 10 Gbits/s version of EPON called XEPON.

### Note

Ethernet is discussed further in [Chapter 12](ch12.html).

## Phone lines

For many years, vendors have offered devices to network computers over phone lines in buildings. One early system called PhoneNet, from a company called Farallon (now Netopia), allowed Macintoshes to network without having to use Apple LocalTalk. This technology worked by using the spare wiring in the telephone line as its physical medium. This was back in the days when a single telephone line was all that anyone ever had coming into their house. Now it seems that anything that moves has a phone number attached to it, and there is no such thing as a spare set of phone wires.

The latest versions of phone networking are designed to work over the telephone wires that are in use. They do this by working at frequencies that aren't in use for voice communication. They also use different modulation technologies to ensure that the data arrives correctly at its destination. The most widely used phone line networking technology in current use is HomePNA. If you are familiar with the older phone line networking technologies that poked along at 10 Mbits/s on a good day, you may want to take a look at the latest HomePNA standard; it was built to transfer large multimedia files at relatively high speeds.

[Figure 10.1](ch10.html#homepna_allows_you_to_connect_your_netwo) shows different devices in a home network using HomePNA network technology. In this figure a HomePNA router is connected to the Internet and to an Ethernet line. That router provides Internet access to other devices on the network by connecting through Ethernet/PNA adapters that plug into existing telephone lines. In each of the different areas of the home an Ethernet/PNA adapter is plugged into a phone outlet and Ethernet is connected to networked devices. Three different areas of the home are shown connected to the PNA network — Area 1 with a set of wired devices, Area 2 with devices connected through a wired hub, and Area 3 where a wireless access point serves wireless clients in that area of the house.

Telephone line networking is extremely convenient. You can connect up to the telephone line directly from a telephone network interface or through an Ethernet-to-telephone connector or bridge. It doesn't matter what kind of phone service you have; telephone networking uses the telephone wires as its physical medium and works regardless of the phone service type. However, the phone lines used must be on the same circuit. If you have an additional phone line or lines installed, you will need to use one of those lines for each of your network connections.

![HomePNA allows you to connect your network using standard telephone lines without any additional modification needed.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1001.png)

**Figure 10.1. HomePNA allows you to connect your network using standard telephone lines without any additional modification needed.**

A current generation of home phone networking products is organized around the HomePNA 3.1 standard, created by the HomePNA (Home Phone Networking Alliance) industry alliance (`www.homepna.org`,) that delivers IP services such data, VoIP, and IPTV (the so-called "triple play services" shown in [Figure 10.2](ch10.html#phone_networking_separates_voice_comma_i)) over existing coaxial cables and telephone lines. The International Telephone Union (ITU) G.9953 standard, ratified in January 2007, is based on HomePNA 3.1.

In [Figure 10.2](ch10.html#phone_networking_separates_voice_comma_i) a graph of power versus frequency for signals traveling over a phone line is shown. HomePNA networking supports triple play networking because it is able to support different technologies such as telephone signals (a narrowband service) as well as DSL and Ethernet over distinctly different frequencies. The signals carried over the same physical medium do not interfere with one another.

![Phone networking separates voice, Internet, and home network traffic into three distinct bands over the same wire.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1002.png)

**Figure 10.2. Phone networking separates voice, Internet, and home network traffic into three distinct bands over the same wire.**

The HomePNA standard is based on work done at Broadcom and Copper Solutions. Broadcom sells the two custom ASIC chip sets needed to communicate with other devices as part of the core reference architecture. The Broadcom MC4100 analog front-end is a transceiver or digital-analog converter that converts signals sent to or received from the phone line, and the Broadcom BCM4210 PCI/MSI controller chip sends data to or reconstructs the data at the transceiver. HomePNA uses Frequency Division Multiplexing (FDM) to send signals over the same two wires that a phone service uses.

Connections are made from an RJ-11 wall jack to computer systems that are equipped with a HomePNA network adapter. This adapter takes the form of an add-in PCI or PC Card, or a USB device. Connections can be up to 1,000 feet, and up to 50 devices are supported. HomePNA states that the building can be no bigger than 10,000 square feet (929 square meters). Version 3.1 has a projected throughput of up to 320 Mbps over coaxial cable, with current devices offering up to 128 Mbits/s. HomePNA is mainly aimed at ISPs and telephone companies, as it allows remote management and diagnostics, QoS, and features such as unified billing. HomePNA claims that the system is compatible with 99 percent of the homes in the United States. In instances where telephones or fax machines generate too much noise, those devices should be connected to a low-pass filter, just as you would for any DSL connection.

Among the products tested and certified are set-top boxes, ADSL and VDSL residential gateways, Ethernet-HomePNA 3.1 bridges, and residential gateways with a Wi-Fi access point included. You can find the current list of certified products at the following Web page, with links to their manufacturers: `www.homepna.org/en/certification/member_products.asp`.

## Power over Ethernet

Power over Ethernet (PoE) connects devices over Ethernet, and provides both data and power from one device, called the Power Sourcing Device (PSD), to the other device, called the Power Device (PD). This makes the PD mobile as it can be plugged into an Ethernet port without requiring a nearby power socket. This technology was developed at Cisco and first released in 2000 as "inline power." PoE's primary goal was to create a technology that would make it easy to use IP telephony devices, wireless access points, Web cams, and other appliances wherever a network exists.

PoE became an IEEE standard with the release of the IEEE 802.3-2005 (802.3af) specification, and nearly all devices made since that time conform to this standard. The part of that standard relating to PoE is referred to as 802.3af. PoE devices span a range, from simple wall plug adapters that connect a power outlet to one or two Ethernet RJ-45 connections up to Enterprise-level switches that can be connected through up to 48 PoE Ethernet cables to devices or systems. PoE relies on the wiring that most likely already exists in place in homes and buildings. No power main voltages are exposed. Should a building suffer a power outage, the PSD can be kept active by being backed up by a UPS (uninterruptible power supply) and connections will remain active. PoE connected devices can be moved to any networkable location, and in the case of wireless LANs, this makes it easy to reconfigure your Wi-Fi network's coverage.

The 802.3af standard transfers data and power over the two unused pairs of the four wire pairs in CAT3/CAT 5e wiring. PSDs and PDs can be run over either the signal pair or the spare pair of the Ethernet cable, but not both. Any connection can use one of these two configurations, supplying 13W of power with a voltage at 48V. [Figure 10.3](ch10.html#the_two_different_configurations_possibl) shows these two different configurations, one sending power over spare pins and the other showing power over data pins.

PoE connected devices can be managed through SNMP (Simple Network Management Protocol), and remotely restarted or turned off. While in discovery, the PSE (power sourcing equipment) sends a small voltage over each of the Ethernet cables and detects the 25k ohm resister that is present in the transmitter (TX) and receiver (RX) of the PD. When detected, the entire 48V is then sent down that wire with a signal. At first, the current to the PD is limited, and when the discovery process is completed, full power is applied. As part of the discovery process, developers can include a negotiation that sets the amount of current that the PD supplies.

## HomePlug Powerline

HomePlug devices use the power lines in a building to connect Ethernet devices together, sending data over the power lines. Depending upon the modulation in use, the throughput for this technology is between 1.0 Mbits/s and 13.8 Mbits/s. There are two versions of the HomePlug standard: HomePlug 1.0 and HomePlug AV. HomePlug AV is meant to support audio-visual applications such as HDTV over the network and achieves speeds of 200 Mbits/s.

![The two different configurations possible with Power over Ethernet](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1003.png)

**Figure 10.3. The two different configurations possible with Power over Ethernet**

PoE connected devices can be managed through SNMP (Simple Network Management Protocol), and remotely restarted or turned off. While in discovery, the PSE (power sourcing equipment) HomePlug is based on the HomePlug Powerline Alliance's specification, and not on the 802.3af standard. The IEEE is developing a standard called IEEE P1901 that may unite HomePlug's technology with its competitors, which include Panasonic and the Universal Powerline Association.

[Figure 10.4](ch10.html#a_powerline_network_connecting_three_dif) shows how Powerline networks can be used to connect different areas of the home together. The technology for Powerline uses an identical topology shown previously for HomePNA networks. A HomePlug router connects the Internet to the powerlines in your home or building over an Ethernet connection using Powerline Ethernet Bridge devices that are plugged into a power outlet. Each area of the home is connected to the network using another Powerline Ethernet Bridge.

Powerline uses network routers, bridges, and other adapters to connect areas with different needs. A typical arrangement plugs a wall socket adapter into the electrical outlets of a home and connects that wall plug through USB or Ethernet to the devices that are part of the network. Wireless access points are sold using Powerline technology. This type of home network connectivity is relatively new. Look for the next generation of Powerline devices that run at the faster network speeds. Also, you should be aware that older home wiring can limit the use of Powerline, and that the technology is sensitive to interference. Either test your wiring or ensure that if these adapters don't work in your home network that you can return or replace them with different models before purchasing.

The fact that you can send data over power lines is quite amazing, as power lines are full of random noise and fluctuating conditions. The loads at each connection have different impedances, and the conductors often vary from place to place. A power line signal's amplitude and phase can vary with frequency, often dramatically, so that some frequencies are attenuated dramatically while others are not attenuated at all. Channel conditions can also change with time, depending upon the load being driven through the line. Many devices also create interference on a power line. Halogen lights, brush motors, and switching devices put oscillations or spikes into the line at different places that can mask signals.

### Note

HomePlug adapters must be plugged directly into the socket. Plugging them into a power strip interferes with the RF signal transmission.

### HomePlug modulation

HomePlug uses a transmission technology called Orthogonal Frequency Division Multiplexing (OFDM). It is the same technology used in DSL, wireless TV, and Wi-Fi 802.11a and 802.11g networking.

OFDM creates data channels by slicing up the spectrum into narrow bands, which for HomePlug is a set of 84 equally spaced subcarrier bands centered between 4.5 MHz and 21 MHz. The signal is sent through several adjacent channels so that the subcarriers overlap and are orthogonal to one another. Different modulation techniques are used; for HomePlug, it is mainly DBPSK (Differential Binary Phase-Shift Keying) and DQPSK (Differential Quadrature Phase-Shift Keying). Each channel's signal strength should drop off as a constant to a set of flat and fading channels. From the strengths of parts of the signal, the whole signal can be determined, without the use of electronic equalization to restore the signal shape. It can be restored mathematically using forward error correction and data interleaving. Forward error correction (FEC) is a method for sending redundant data in a transmission to provide an error check that the data received is correct. Data interleaving is a technique that sends data over a variable time period so that adjacent errors in the data stream may be corrected.

![A Powerline network connecting three different areas of the home](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1004.png)

**Figure 10.4. A Powerline network connecting three different areas of the home**

Because the power line conditions vary at different locations, the HomePlug technology measures the transfer rates of individual subchannels and turns off any subchannels that are heavily attenuated or impaired, a process that is called *Tone Allocation*. Depending upon the characteristics of the connection, different modulations such as DBPSK 1/2, DQPSK 1/2, and DQPSK 3/4 can be chosen, and that, combined with Forward Error Correction, greatly lowers the transfer error rate. This technology is called channel adaptation, and it is essentially a link optimization technology.

Because a link is essentially point to point, different techniques need to be applied when using HomePlug for broadcast transmissions. What is done in this case is to use the DBPSK modulation, send multiple copies of each bit down the wire at different times and at different frequencies, and apply error correction to all of that data, which HomePlug calls ROBO modulation. The structure of the frames that are sent is also modified for the channel adaptation done in ROBO.

### Frames and sequences

The HomePlug Medium Access Control (MAC) protocol is based on the Ethernet IEEE 802.3 frames, both of which are long frame formats, which is why there is a high compatibility between HomePlug and Ethernet networks, with little additional processing required. HomePlug's MAC encrypts the frames entering HomePlug devices from Ethernet networks, and appends them to the HomePlug header before they are sent over power line connections. HomePlug frames are then sent to the receiving device. The receiving device reassembles the segmented frames and then decrypts the data before sending it on. If the Ethernet frame is encrypted (with IPsec, for example) before it enters the power line connection, it remains encrypted when it leaves the receiving device.

HomePlug uses both a messaging frame that is called Short Frame, and the Long Frame for data encapsulation that was described in the previous paragraph. The structure of these two frames is illustrated in [Figure 10.5](ch10.html#long_and_short_homeplug_frames). Message frames are used to indicate whether frames have arrived correctly, whether data needs to be retransmitted, and for other purposes. Long frames contain start of frame and end of frame sections with a number of control fields. Since frames must be a sandard size, data is padded (PAD) to length. The FCS field contains error correction data.

The Short Frame is used to initiate a Stop and Wait automatic repeat, or ARQ, which is used to get the transmitting device to resend data that did not pass its error correction validation. Short Frames use a Response Delimiter, which has a Preamble and Frame Control information field. The Preamble is a spread spectrum signal, which signals the start of the delimiter. Frame Control information encoded in HomePlug's Turbo Product Code is used to allow detection of this message at very low amplitude, several dB below the ambient noise according to their specification. The Long Frame's Payload (data) is also indicated through the use of this special delimiter field, and the encoding can vary, based on the channel adaptation method used.

As is common for 802.3 frame types, the first 17 bytes of the Frame Header contain the source address, the destination address, and the segmentation number to be used for sequencing the frames. The reason that the very first bytes have addressing in them is that even if part of the frame is corrupted, the first bytes provide the means to send a message back for the frame to be resent. The payload is padded (PAD) to bring it to standard length. FCS is the Frame Control Sequence used.

![Long and short HomePlug frames](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1005.png)

**Figure 10.5. Long and short HomePlug frames**

As frames are sent over a power line, a form of Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) is used to provide traffic flow control and lower the collision rate. CSMA/CA listens using both Physical Carrier Sense (PCS) and Virtual Carrier Sense (VCS) for an idle period before transmitting additional frames, with HomePlug providing a prioritization scheme along with a resolution mechanism. PCS is a Physical layer protocol used to detect the preamble. VCS is a MAC layer protocol and uses the information in the delimiter to determine the following:

- **Start of Frame delimiter**. The type of response required, frame length, priority, and tone map index or channel adaptation used to send it.
- **End of Frame delimiter**. The type of response required and the priority.
- **Response delimiter**. A response (Resp) can require an ACK (acknowledgment), NACK (negative acknowledgment), or FAIL response (negative acknowledgment due to resources), and also includes the priority of the preceding frame.

Priority resolution is based on assigned user priorities for application classes, and has a backoff algorithm that detects contention and lowers priorities appropriately. This system allows HomePlug to offer several different Quality of Service features that support streaming applications such as VoIP, multimedia, and other technologies.

### Security

Each device comes with a label showing the master password given to it by the manufacturer; that password provides access to create other passwords. To access the encryption features of a HomePlug device, you need to install the software that came with that device. Most of these devices come with software for Windows. If you are using a Macintosh or Linux computer, check to see if this software is available for your operating system, or is browser based.

The security scheme used is based on a 56-bit Data Encryption Standard (56-bit DES) technology. A HomePlug station (the connection endpoint) stores a table with encryption keys and the Encryption Key Select (EKS) values used to encrypt frames. EKS is an index value used to identify an encryption key; the EKS value is stored inside the frame header and used by the receiving station for key selection for the decryption. For each network, an individual shared Network Encryption Key is used and an associated EKS is on every station in the network.

Note that the optimization of the channel selection done in channel adaptation provides an additional level of security.

# Home Network Servers

Home network servers are created to serve the needs of small networks of users in a residential environment. Home servers are engineered to be easy to use and to support a range of functions needed for networks of this type. The small number of computers on a home network means that the hardware needs of a home server are usually modest. Many people turn older computers into home servers, and many vendors use older or more limited versions of the network server operating systems as the basis for a home server. The Microsoft Windows Home Server is based on the Windows Server 2003 operating system, has some administrative features turned off, and comes with a number of wizards included to make configuration easier. Many home servers are sold as appliances, and are based on Linux distributions or BSD UNIX.

Many home servers include the following elements:

- Network addressing services such as DHCP and DNS
- Firewall or proxy services for Internet connections
- Web servers for use by computers on the network for an intranet, and in rarer instances, for Internet use
- Resource sharing of storage (file sharing), printers, and other peripherals
- Remote access capabilities that allow users to connect from outside
- Media streaming capabilities for audio/visual files
- An e-mail or instant messaging (IM) server
- Network security
- Application software for the home, such as group calendars, to-do lists, and more

As a category, home servers have had only a very tiny impact on the market. In the two years that Microsoft Home Server (`www.microsoft.com/windows/products/winfamily/windowshomeserver/default.mspx`) has been available, it is estimated that less than 100,000 home servers have been sold.

Over the past decade, several home server appliances have appeared in the marketplace, none of which has fared as well as Microsoft Home Server. One example of a home server appliance is the Toshiba Magnia, which was released in 2001 and based on Red Hat Linux. This appliance provided a browser administrative interface, DHCP, DNS, FTP, a Web server, print server, firewall, filtering, and Web caching, all in a package the size of a laptop. Some other examples of appliances in this category were the Sun Cobalt Qube, EmergeCore Network's IT-100, Mirra Personal Server, Greencomputer Innovation's PowerElf II, IOGEAR BOSS, Tritton Technologies ASAP, and Chili Systems ChiliBox; all were aimed at the Small Office Home Office (SOHO) market. Of this list, only the IT-100 is still available.

The idea of having a home server on your network makes sense, even if it hasn't been a market success. It may well be that people who are technically inclined simply opt for standard versions of networked server operating systems such as Windows Server, Solaris, Red Hat Linux, or something else. Still that doesn't stop people from trying to introduce new products in this area. One group of Ubuntu devotees have gotten together to start a Ubuntu Home Server project (`www.ubuntuhomeserver.org`), but this project is still in development. Other rumors I've read are that Apple is developing a competitor for the Microsoft Home Server, but one never knows with Apple.

As it stands now, Microsoft Home Server is the only real game in town, and it is certainly worth considering if you are interested in centralized home network services. Home Server is a very smooth product, and over 60 third-party products have been built to support it. Just the network backup service, mirroring, and the ability to aggregate all of the disks it can see make this product a worthwhile investment for any home network of four computers or more. HP, Acer, Shuttle, and Via all offer Windows Home Server appliances. [Figure 10.6](ch10.html#microsoft_home_server_uses_any_disk_it_c) shows the Microsoft Home Server storage console.

![Microsoft Home Server uses any disk it can find for storage.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1006.png)

**Figure 10.6. Microsoft Home Server uses any disk it can find for storage.**

# Summary

In this chapter, home networks were described, and their common features were listed. Home networks let you share resources, which is a great savings of time and money. Usually home networks use different technologies mixed together for maximum convenience, and minimum cost and complexity.

This chapter focused on two essential home network problems: how to connect to the Internet and how to bridge different areas of your home together. Ethernet, HomePNA, and HomePlug networking were described. Wi-Fi was briefly described.

In the next chapter, peer-to-peer networking technologies are described. This category of networks also includes networks based on different computer bus standards.
