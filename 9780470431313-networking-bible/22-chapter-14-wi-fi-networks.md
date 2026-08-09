# Chapter 14. Wi-Fi Networks

**IN THIS CHAPTER**

- Wi-Fi and how it works
- 802.11 standards
- Build wireless links and networks
- Available wireless devices

The IEEE 802.11*x* wireless networking standards known as Wi-Fi have sparked a revolution in computer networking over the last decade. In this chapter you will learn about the different standards, their performance characteristics, and how you can create networks or network links with this technology. Wireless networks support two different types of architectures: ad hoc and infrastructure modes.

The commonly used standards are all radio frequency communication links over public bands in the 2.4 GHz or 5 GHz frequency range. Wi-Fi separates the bandwidth into channels and then uses a form of spread spectrum transmission that either creates a direct sequence of overlapping transmissions or transmits using a frequency-hopping scheme. This chapter presents both Direct-Sequence Spread Spectrum (DSSS) and Frequency-Hopping Spread Spectrum (FHSS) in detail. Signals are encoded onto the carrier waves that DSSS and FHSS create using a number of different modulation technologies that you learn about in this chapter. In particular, Phase Shift Keying methods are popular.

The 802.11*x* frames are similar to Ethernet frames and are described here. The main method for sending frames uses Carrier Sense Multiple Access with Collision Avoidance. Methods for handshaking, traffic control, and connection management are described.

Access points, gateways, and routers are the wireless devices that are used by wireless clients to connect to networks. The characteristics of these different devices are described. Methods for extending networks, including repeaters, distribution systems, and special antennas (such as smart antennas) are touched upon in this chapter.

Software that you can use to discover wireless network devices and learn about wireless traffic are surveyed. This chapter also presents the different forms of wireless network security methods in common use today.

# Wireless Networking

The dominant form of wireless networking uses radio frequency transmission over either the 2.4 GHz or 5 GHz bands of the electromagnetic spectrum. These bands were chosen because they are in the public domain, and because they can accept the introduction of ad hoc network links that wireless networks create without disruption of other systems. It is safe to say that the emergence of the 802.11*x* family of standards has been as revolutionary to computer networking as cellular phones have been to the telephone industry. There are four main standards of 802.11 wireless equipment on the market in wide use today: 802.11a, 802.11b, 802.11g, and 802.11n. Products based on the 802.11n standard are finally becoming popular after a relatively long gestation period in which products were based on draft standards.

The 802.11 networks formed using direct point-to-point links between two stations, or STAs, are called ad hoc networks and implement a set of services called the Independent Basic Service Set (IBSS). An ad hoc network can be formed from a set of STA links such that a closed loop is formed between the STAs. Ad hoc mode is sometimes referred to as peer-to-peer (P2P) mode. A network formed between stations and a transmitter/receiver called a wireless access point (AP) is referred to as an infrastructure network, and it implements a set of services called the Basic Service Set (BSS) and assigned a BSSID. [Figure 14.1](ch14.html#logical_802.11_wireless_network_types_m) shows these wireless network components.

Both ad hoc and infrastructure networks create a named network security object called the Service Set Identifier (SSID). The SSID is the wireless network's name, and SSIDs are used the same way that a network domain is used. When you initialize the first P2P client on the ad hoc network, you are asked to name the network. Similarly, when you set up your wireless access point, or a similar device such as a wireless router or gateway, you are asked to create an SSID.

The first P2P client, or the AP that created the wireless network, issues what is called an 802.11 beacon frame, advertising the network to potential wireless clients. Clients are then asked to provide the password needed to access the wireless network. In cases where no password was created, the wireless network is unsecured and any wireless client can simply join the network.

When two or more wireless networks are joined through area connections provided by overlapping access points, the network is referred to as a distribution system (DS). A DS is characterized by the ability to take a wirelessly connected STA attached to one access point and move it to a location where it can connect to another access point on the DS. When one STA communicates with an STA linked to a different AP, the communication requires a functional AP-AP bridge link; STAs do not connect directly with one another.

![Logical 802.11 wireless network types — ad hoc and infrastructure network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1401.png)

**Figure 14.1. Logical 802.11 wireless network types — ad hoc and infrastructure network**

When you have two or more wireless APs that communicate with one another, they must be part of the same subnet or network, and they implement what is called an Extended Service Set (ESS) and are assigned an ESSID. Although the DS illustrated in [Figure 14.1](ch14.html#logical_802.11_wireless_network_types_m) is an AP-AP connection, many wireless 802.11*x* infrastructure mode networks use wired networks as the DS. When a wired/wireless network is considered, the ESS spans the part of the network that includes the AP and its connected clients and does not extend to the wired network. When two Extended Service Sets share the same ESSID, a wireless client can roam from one to the other without reconfiguration.

[Figure 14.2](ch14.html#a_wireless_solidus_wired_heterogeneous_n) shows the corresponding diagram for an infrastructure network with a wired network connected to a set of access points.

![A wireless/wired heterogeneous network](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1402.png)

**Figure 14.2. A wireless/wired heterogeneous network**

## Wi-Fi networks

Wi-Fi is the trademark of the Wi-Fi Alliance and the generic name given to a set of technologies based on the IEEE 802.11*x* standards. Wi-Fi is meant to evoke a connection to Wireless Fidelity, just as Hi-Fi represents the idea of High Fidelity. Wi-Fi was created by the Interbrand Corporation in 1999 to replace the name IEEE 802.11b Direct Sequence, and it remains a brand name with no real relationship to the technology that it describes. The Wi-Fi logos have a yin-yang design that is meant to indicate the interoperability of the standards.

Wi-Fi is the predominant form of wireless networking for computers, and its standardization by the IEEE has made it nearly ubiquitous in the marketplace. If you purchase a wireless laptop, printer, streaming media server, or any of a host of devices, then it is almost certain that they contain some version of the 802.11 standards; and there is a relatively good chance that that device will interoperate with other wireless network devices you already own. There are some interoperability issues, and in this chapter you will learn what they are.

Wi-Fi isn't the only wireless technology in use. Many wireless technologies in cellular telephones, video games, remote controls, and other devices offer wireless connections based on Bluetooth, IR, radio, and a few other types of technologies. For the most part, these additional technologies are connection-oriented, which is why this chapter describes 802.11 networks in detail. The one exception, Bluetooth, is described in [Chapter 11](ch11.html), where personal LANs (pLANs) are discussed.

# IEEE 802.11*x* Standards

Each of the different 802.11*x* standards specifies a different modulation scheme and a different bandwidth that it operates at. Every standard uses the concept of a channel to separate one set of connections (a network or subnet) from another. For example, the 2.4 GHz band (S-Band ISM) used by 802.11b/g actually spans the range from 2.400 to 2.4835 GHz and is divided up into a set of 13 channels, each channel occupying 22 MHz with a space of 5 MHz between each channel. The channels are numbered from 1 (2.400 to 2.422 GHz) up to channel 13 (2.4823 to 2.4835 GHz). The highest signal is at the center point of each band, which would be 2.411 GHz for channel 1 and 2.472 GHz for channel 13.

There is some variation in the use of the different channels on a per-country basis worldwide, but not as much as there was a few years ago. The United States and some of the Central and South American countries allow the use of channels 1 to 11 in the 2.4 GHz band, while forbidding the use of channels 12 and 13, as well as a fourteenth band that is sometimes added at 2.4835 GHz (the top of the 2.4 GHz range). Japan and now France support the use of all 14 channels, but most of the rest of the world allows the use of only the 13 official bands.

In the 5 GHz band (C-Band ISM), where 802.11a and optionally 802.11n operate, the spectrum is divided into 42 channels. [Figure 14.3](ch14.html#the_802.11_channels_in_use_worldwide) summarizes the current usage of the different channels by country. Be aware that these assignments can change over time.

The size of the 2.4 GHz channels arises from their power distribution, which must be attenuated by 50 dB (reduced in amplitude) from the center frequency of the channel to the edges, 22 MHz on each side. The separation of the channels is 5 MHz, which means that each channel overlaps four channels to either side. [Figure 14.4](ch14.html#the_802.11b_solidus_g_2.4_ghz_channel_as) illustrates the overlaps of different channels in the 2.4 GHz radio band.

This effectively means that of the 13 or 14 channels in the 2.4 GHz band, only 3 channels may be assigned to physically adjacent wireless networks. In the United States, those channels are usually assigned as 1, 6, and 11. In Europe, the 1, 5, 9, and 13 channels are assignable.

As transmitters get farther away from one another, their ability to impact another receiver on an adjacent channel diminishes. So, while 1, 6, and 11 can be operating in the same room without problems, a transmitter on channel 1 on one side of a building might not impact another using channel 4 on the other. Still, it's best to observe the recommended assignments and not try to finesse the overlap problem.

![The 802.11 channels in use worldwide](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1403.png)

**Figure 14.3. The 802.11 channels in use worldwide**

![The 802.11b/g 2.4 GHz channel assignments](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1404.png)

**Figure 14.4. The 802.11b/g 2.4 GHz channel assignments**

The scheme used in [Figure 14.5](ch14.html#how_wireless_network_numbers_overlap) shows how you can lay out a set of access points so that channel numbers that are close to one another have little overlap. Using this methodology, it is possible to extend the coverage area without suffering much channel interference.

![How wireless network numbers overlap](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1405.png)

**Figure 14.5. How wireless network numbers overlap**

## 802.11 legacy

The original 802.11 standards, now referred to as simply 802.11 legacy mode, were released in 1997. They specified three different wireless connection types:

- **Diffuse Infrared**. When connected over a diffuse infrared link, speeds of up to 1 Mbits/s were achieved.
- **Radio Frequency with FHSS**. In the 2.4 GHz band, 802.11 could operate at 1 or 2 Mbits/s using Frequency Hopping Spread Spectrum (FHSS) modulation.
- **Radio Frequency with DSSS**. In the 2.4 GHz band, 802.11 could operate at 1or 2 Mbits/s using Direct Sequence Spread Method (DSSS) modulation.

Products based on 802.11 legacy became obsolete when the 802.11b standards were introduced.

### Note

In order to carry a signal over a radio frequency, a modulation technology must be used, as is discussed in some detail in [Chapter 5](ch05.html).

The 802.11b and 802.11g standards both use DSSS modulation over the 2.4 GHz Industrial Scientific and Medical (ISM) radio band. The 2.4 GHz band is crowded with other devices such as microwave ovens, phones, toys, baby monitors, walkie-talkies, and many other forms of detritus that modern civilization dictates one must connect to wirelessly. At this frequency, 802.11b/g can sometimes suffer from interference. Other radio technologies that use different forms of modulation don't suffer interference; Bluetooth, another 2.4 GHz technology that uses FHSS modulation, doesn't interfere with other ISM band products but can interfere (to a small degree) with 802.11b/g.

Because the 2.4 GHz band is crowded, the alternative 802.11a standard was developed in order to use the 5 GHz ISM band. Because it operates at higher frequencies, 802.11a has a higher throughput than 802.11b/g but is less effective at penetrating walls and has a lower effective range than 802.11b/g. Indoors, the range of 802.11a can be half that of 802.11b in most applications.

As it turned out, 802.11a reached the market after the 802.11b standards and therefore were used in the second wave of Wi-Fi devices that were introduced. The 802.11g standards were third, and now the 802.11n standards, which are the latest standards, are the fourth generation. Because the 802.11a standards operate at a different frequency than the 802.11b/g standards, 802.11a are unable to interoperate with 802.11b/g. When 802.11g networks detect an 802.11b device, the network speed drops down to be backwards compatible with the 802.11b standards.

Many devices are sold that include two or three of the different standards, and they go by a number of different and often proprietary names. Dual band devices were the earliest to market, and they most often included both 802.11a and 802.11b together. When 802.11g became available, products offering all three versions (a, b, and g) were most often called dual band/trimode.

The 802.11n draft standards add what is called Multiple Input Multiple Output (MIMO) to the 802.11 standards, as well as some other features. MIMO is a smart antenna technology that is described in the MIMO section later in this chapter. The 802.11n draft standards offer the ability to interoperate with 802.11b/g standards, as they are a "superset" of all of the previous standards. Although there are many n devices on the market based on the draft standards, they differ enough from one another to cause interoperability headaches for early adopters. The TGn working group of IEEE isn't expected to finalize 802.11n until December 2009. The strong recommendation given to interested parties is that if they adopt 802.11n based on the draft resolution, they only buy n devices from a single manufacturer.

[Table 14.1](ch14.html#x_characteristics) lists the different 802.11*x* standards and their characteristics.

**Table 14.1. 802.11*x* Characteristics**

| Standard | Band (GHz) | Modulation[[a]](ch14.html#ftn.CHP-14-TFN-1) | Throughput (Mbits/s) | Net/Gross Bit Rate (Mbps) | Range (indoor/outdoor, in meters) |
| --- | --- | --- | --- | --- | --- |
| [[a]](#ftn.CHP-14-TFN-1) |  |  |  |  |  |
| 802.11 | 2.4 | IR/FHSS/DSSS | 0.9 | 2 | 20/100 |
| 802.11a | 5.0 | OFDM | 23 | 54 | 35/120 |
| 80211b | 2.4 | DSSS | 4.3 | 11 | 38/140 |
| 802.11g | 2.4 | OFDM | 19 | 54 | 38/140 |
| 802.11n | 2.4 or 5.0 | OFDM | 74 | 600 | 70/250 |
| 802.11y | 3.7 | OFDM | 23 | 54 | 50/5000 |
| [[a]](#CHP-14-TFN-1)IR (infrared); FHSS (Frequency Hopping Spread Spectrum); DSSS (Direct-Sequence Spread Spectrum); and OSDM (Orthogonal Frequency Division Multiplexing). |  |  |  |  |  |

## 802.11y

The 802.11y standards approved in September 2008 add 3.7 GHz (3650 to 3760 MHz band), high-power (20 watt maximum) radio link connections that can operate over distances of up to 5 km (3 mi.). This band overlaps with some ground station/satellite communications, and so there are some limitations on where this kind of connection can be made. In order to use 802.11y in the United States, a license must be obtained for base stations for a small fee. This license is for the base station, and not for a particular location; it can be used anywhere in the United States. 802.11y clients don't require a license, but they do require that they successfully handshake with a base station before they can transmit data. The station's license, as well as their transmissions, make it possible to identify the operators, which is important in determining which transmission might be interfering with other local transmissions.

To allow for multiple 802.11y links in the same geographical area, an enhancement was added to carrier sensing in 802.11 called the Contention Based Protocol (CBP). This protocol will establish a set of rules so that the different sessions can coexist. When contention occurs, the current proposed standard seeks to resolve it first by technical methods, and if not, to provide a dispute resolution forum to resolve any issues.

Another new feature of 802.11y is the ability of base stations to sense channels based on their current noise and available bandwidth, and to dynamically switch channels as needed. In order to maintain connections to clients, a new messaging scheme called Extended Channel Switch Announcement (ECSA) lets the access station signal the change to clients and have them switch concurrently.

Any unlicensed 802.11y device is referred to as an STA. The 802.11y protocol requires that the base station or access point not only be able to enable a client but also be able to restrict access as well. The mechanism that is used to manage the connection is called the Dependent Station Enablement (DSE).

This method of access has been referred to as the light licensing model and may be applied to other bandwidths being considered for 802.11y usage, including 4.9 GHz and 5.0 GHz. A set of other bands, referred to as the IMT-Advanced candidate bands, are at 450-862 MHz, 2300-2400 MHz, 2700-2900 MHz, 3400-4200 MHz, and 4400-5000 MHz, and are under consideration for adoption by 802.11y. It is predicted that when these devices finally become available in the consumer market, they will achieve throughputs of around 100 Mbits/s for mobile applications and 1 Gbits/s for stationary links.

These bands represent fragments that are assigned but that are often available most of the time, even in dense urban areas. The availability of bandwidth isn't uniform; it varies both by time and by geographical location. For example, in some markets, different TV channel assignments make the white spaces between channels fall in different locations. The intent is to make these bands available using different multiband switching technologies based on switching both time and location of band usage.

## Modulation

The 802.11b standards, which were introduced in 1999, use the Complementary Code Keying (CCK) modulation scheme. Complementary codes are a set of sequences of the same length created so that the number of pairs of like states with a certain separation in one of the sequences is the same as the number of pairs of different states having the same separation in the other sequence. This modulation has the effect of making it easier to recognize the different states that code for symbols than the Barker codes that were used in 802.11 legacy.

The digital signal modulation used by 802.11*x* (with the exception of 802.11b/legacy) wireless technologies is usually a variant of Phase Shift Keying (PSK). Signals are encoded by the modulator by changing the phase of the carrier wave, with each of the phases used representing binary data. Patterns of phase changes encode for symbols (characters), which are demodulated and interpreted based on a stored signal map. When the PSK system performs a comparison to a reference set of signals, the technology is referred to as Coherent Phase Shift Keying (CPSK).

### Note

Digital signal modulation can be based on Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), or Phase Shift Keying (PSK).

There are many other variations of PSK. In one type, called Differential Phase Shift Keying (DPSK), the phase of the carrier wave is varied by a certain amount or a differential instead of being changed entirely. With DPSK, it is the variation in the phase that is used to extract character information based on a stored algorithm, and a reference signal isn't used. That makes DPSK easier than CPSK as well as faster, but it also introduces more demodulation errors.

PSK modulation can be viewed using what is called a constellation diagram. In this diagram, complex numbers are represented by the real portion of the number as the x-axis (the in-phase axis) and the imaginary portion as the y-axis (the quadrature axis). The diagram is drawn in two dimensions, referred to as an Argand plane, and the mapping is referred to as an Argand diagram. This mapping allows functions that are time-varying waves to be represented by their points on a circle. The modulation scheme shown at the top of [Figure 14.6](ch14.html#constellation_diagrams_for_bpsk_comma_qp) is called Binary Phase Shift Keying (BPSK), which is the simplest form of PSK available.

![Constellation diagrams for BPSK, QPSK, and 8-PSK.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1406.png)

**Figure 14.6. Constellation diagrams for BPSK, QPSK, and 8-PSK.**

Using this modulation, the phase shifts between two states, 180 degrees out of phase with one another. For that reason, this technique is sometimes called phase reversing keying. The fact that the two states are drawn on the real axis is not significant; they could be at any point on the circle as long as their axis bisects the circle.

Of all the modulation schemes, this one provides the lowest error rate because the difference between the two states is the most extreme. However, the modulation only carries one bit of information, making this the slowest modulation. Therefore, BPSK is often replaced with faster modulation.

You can see how a progression to higher-order modulation is represented in a constellation diagram by examining the middle Argand graph in [Figure 14.6](ch14.html#constellation_diagrams_for_bpsk_comma_qp). This modulation is referred to as Quadrature Phase Shift Keying (QPSK, 4-QAM, or 4-PSK), with QPSK being the most common abbreviation. In this scheme, four states are encoded, with each state representing two bits. Each adjacent symbol only differs from the next by a single bit, which is called Gray coding.

Although QPSK is shown as a single representation of four phases, mathematically, QPSK may be represented as two independent quadrature carriers, each with two phases (one phase change), modulated by BPSK. This analysis indicates that the error rate of QPSK is the same error rate you experience when you use BPSK. However, when you use QPSK, you double the data rate versus BPSK using the same bandwidth. Alternatively, you can carry more channels with this modulation, as you can have the same data rate as BPSK in half the bandwidth.

You can imagine creating a higher-order modulation scheme by doubling the states in the QPSK, which leads you to a constellation diagram containing eight states. This form of modulation is called 8-PSK, and each state encodes for three bits with Gray coding. The constellation diagram for 8-PSK is shown in the right diagram in [Figure 14.6](ch14.html#constellation_diagrams_for_bpsk_comma_qp). Practically speaking, 8-PSK is the highest order that can be achieved due to high error rates. To go beyond 8-PSK, other methods such as amplitude modulation are used, with one example being Quadrature Amplitude Modulation (QAM).

QPSK forms the basis for a number of techniques that can be used for modulation. One modulation separates the two quadrature portions of QPSK so that they are separated by time, with one carrier wave being a sine wave and the other carrier wave being a cosine wave; both are 180 degrees out of phase.

Another technique, called Offset Quadrature Phase Shift Keying (OQPSK) or Staggered Quadrature Phase Shift Keying (SQPSK), offsets the timing of the odd and even bits by a bit period; thus the in-phase (real or x-axis) and the quadrature (imaginary or y-axis) never vary by more than 90 degrees at a time. OQPSK offers better performance when signals are sent through a low pass filter, which is how many transmitters are constructed. The π/4-QPSK is another offset variation, which offsets the states by rotating them by 45 degrees, or π/4.

The 802.11a wireless standards, which use 52 carriers per channel spread over the 4915-5825 GHz band, have a channel separation of 20 MHz. 802.11a have been implemented using BPSK, QPSK, 16QAM, and 64QAM modulation, and a host of encoding schemes. This results in a net bit rate (throughput) of up to 54 Mbits/s with symbol length of 3.2 μsecs.

Now that you have seen how signals are encoded onto carrier waves, let's take a look at some of the multiplexing technologies used to create the carrier waves themselves. This includes the two types of spread spectrum technologies based on frequency hopping and direct sequences, and the now more widely used orthogonal frequency division multiplexing.

### Direct-Sequence Spread Spectrum

Direct-Sequence Spread Spectrum (DSSS) is the modulation that is used by 802.11b and was used by the 802.11 legacy standards. Spread spectrum refers to the manner in which a wide band of low, constant-power density is partitioned to carry multiple channels of radio signals. Spread spectrum signals require that the transmitted signal's bandwidth be much wider than the information bandwidth, and that the transmitted bandwidth can be determined independently of the information that it carries.

### Note

Please refer to the related discussion in [Chapter 5](ch05.html) on multiplexing for background information on modulation technologies.

In [Figure 14.7](ch14.html#a_dsss_versus_an_fhss_carrier_wave), you see the shape of a DSSS signal, just as you would if you hooked up a spectrum analyzer to the radio receiver. The graph plots the amplitude of the radio frequency (RF) signal on the y-axis (ordinate) and frequency on the x-axis (abscissa). The top graph shows DSSS technology; while the bottom graph shows FHSS technology. Compare the graph for DSSS technology to the graph for FHSS technology, which is commonly used in cell phones and discussed in detail in the next section.

Notice that the RF signal is spread out over a bandwidth that is 20 times wider than the signal. The common range for bandwidth-to-signal ratios is 20–250:1, and signals with ratios as high as 1000 have been demonstrated. That combination of a broad spectrum and low-power signal makes spread spectrum very hard to intercept and jam — which is why the technology has been so popular in the military for so long.

Direct sequence modulates a sine wave by applying a pseudo-random noise known as a chip. Chips are overlaid onto the radio wave at high frequency and have a very short duration. The chips, which are produced by a processor known as a chipper, create a signal structure that is known by the receiver beforehand. The pseudo-noise (PN) code at the receiver is applied using the same PN sequence to reconstruct the data. The transmitter sends a number known as a seed to the receiver beforehand, which is used by the pseudo-number algorithm to calculate the PN sequence.

Without the PN sequence, the high-speed sequence of 1 and _1 values appears to an independent observer to be white noise and spreads the energy of the signal carried over a wide band. Reconstruction of the signal, known as de-spreading, takes the PN sequence and multiplies the sequence using the highly synchronized pseudo-noise signal to obtain the data. Synchronization is achieved by transmitting a data sequence that provides access to a lookup table of channel sequences. Once the transmitter and receiver are synchronized, the future data sequences serve as a check of the current location of the sequence in the table.

![A DSSS versus an FHSS carrier wave](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1407.png)

**Figure 14.7. A DSSS versus an FHSS carrier wave**

A DSSS signal can be enhanced by increasing the PN sequence and using more chips per bit transmitted (improving the Signal-to-Noise ratio) within the limits of the technology employed, an effect referred to as process gain.

DSSS allows multiple channels to overlap because each signal has its own different PN sequence. This is the principle behind Code Division Multiple Access (CDMA), that multiple transmitters do not cross-correlate and the signals may be extracted independently of one another.

Spread spectrum transmission has a number of desirable features:

- Low power signals, which also helps to keep the Signal-to-Noise ratio low
- Ability to avoid other radio signals, or low narrowband interference
- Redundant transmission pathways
- Carrying capacity for multiple data streams, with each channel available to multiple users
- Security mechanism based on changing band assignments
- Low amount of fading and multipath interference

These features allow Wi-Fi to operate license-free over public radio bands. In addition to 802.11b/legacy, other devices that use DSSS are CDMA cell phones, wireless telephones (900 MHz, 2.4 GHz, and 5.8 GHz), GPS satellite (and the European Galileo equivalent), ZigBee digital radios based on the 802.15.4-2006 standards, and the automatic meter reading technology that is used by utility companies to read water, gas, and electric meters on houses.

### Frequency Hopping Spread Spectrum

The Frequency Hopping Spread Spectrum (FHSS) modulation was used by 802.11 legacy in one of its modes, but it isn't used on other Wi-Fi standards. It is, however, used by other telecommunication systems, and so I briefly present it to you here. In practice, it isn't much different from DSSS. The main difference is that FHSS spreads the information by rapidly switching the carrier wave to many different frequencies using the same kind of pseudo-random number sequence for signal generation and extraction that DSSS used.

[Figure 14.8](ch14.html#an_fhss_carrier_wave) illustrates an FHSS signal shape, just as you would see it if you hooked a spectrum analyzer to a radio receiver. Notice that the shape of the wave is very different than the DSSS sinusoidal [(sin x)/x]2 wave. FHSS uses a flat, narrow signal whose bandwidth is the width of a signal versus the number of times the signal repeats. A frequency hopper can be made to be regularly spaced, as shown in [Figure 14.8](ch14.html#an_fhss_carrier_wave), or it can skip parts of the band; the data it carries can be either analog or digital.

![An FHSS carrier wave](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1408.png)

**Figure 14.8. An FHSS carrier wave**

FHSS transmissions are hard to detect and intercept, as the spread signal and pseudo-random nature makes it appear as if it is background noise. In order to reconstruct the signal, a receiver would need the PN sequence, which also makes it hard to intercept. FHSS (like DSSS) can be transmitted over radio bands that are carrying other types of transmissions and successfully extracted by the receiver.

Of all of the FHSS technologies in use today, the one you are most likely to encounter is Bluetooth, which uses the Adaptive Frequency Hopping (AFH) spread spectrum as its modulation. AFH uses hops over preferred frequencies, avoiding frequencies that are found to be of low quality or experiencing interference.

### Orthogonal Frequency Division Multiplexing

Orthogonal Frequency Division Multiplexing (OFDM) is digital frequency division technology that is used by 802.11a/g/n/y. In this technology, multiple subcarrier waves are overlaid on top of each other with an offset so that the peak of one subcarrier overlaps with the trough of another. The use of multiple subcarriers is the multiplexing feature, while the overlap of one subcarrier is orthogonal to another. The overall carrier signal can be reduced by a Fast Fourier Transform by the transmitter and expanded by the receiver.

The easiest way to visualize how OFDM works is to consider how the signal is built up to form the carrier wave. [Figure 14.9](ch14.html#combination_of_orthogonal_subcarriers_in) shows a base subcarrier, which is then overlaid by five additional offset subcarriers. The top figure shows the base carrier and subcarriers, and the bottom figure shows the resultant carrier wave.

![Combination of orthogonal subcarriers into an OFDM carrier](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1409.png)

**Figure 14.9. Combination of orthogonal subcarriers into an OFDM carrier**

OFDM is widely used for the following reasons:

- Fast data transfer rates near the Nyquist theoretical limit, with bandwidth utilization
- Ability to suffer narrowband interference, fading, and multipath effects without loss of signal
- Ability to suffer time synchronization errors (However, OFDM is sensitive to frequency synchronization errors.)
- Efficient use of Fast Fourier Transforms for signal processing

All data transmission is degraded over distance, by resistance in wires, or for radio frequencies over wireless connection problems due to multipath or interference. *Multipath* is the term used to describe a radio signal that is sent or arrives at an antenna over two or more separate paths. This places limitations on the number of subcarriers that can be used and sometimes requires the use of a blank subcarrier called a guard band that provides additional time for signals to arrive, be buffered, and be processed before adding more data. The interference due to signal crowding is referred to as intersymbol interference (ISI), the term symbol being synonymous with an interpreted character. The guard band also helps to alleviate problems arising from imperfect orthogonality, which leads to signal degradation called intercarrier interference (ICI). Several other techniques make OFDM uniquely capable of tolerating severe interference while still being able to recover transmitted information, but ISI and ICI are two problems that OFDM suffers from.

One other disadvantage that does present a problem is that OFDM requires more power than other technologies.

Each of the subcarriers is then used to carry data, which is encoded using a modulation method such as Phase Shift Keying, quadrature amplitude modulation, or some other method. The data is therefore superimposed upon the carrier wave at a low bit rate (also called the symbol rate), and because there are a number of subcarriers, each carrying a part of the data stream, the throughput is equivalent to or higher than other forms of signaling technologies that rely on a single carrier.

OFDM is now the dominant form of multiplexing for all forms of wideband digital communication, be it wired technologies (such as ADSL, Powerline, or coaxial transmissions) or wireless technologies (such as Wi-Fi, digital radio, digital TV, and third-generation phone systems). The reason that OFDM multiplexing is so popular is that the technology allows new advances in modulation to be applied to the transmission without having to redesign the media or physical equipment.

## 802.11 protocol

The 802.11 protocol specifies the nature of 802.11 frames and their transport over the Physical and Media Access Control sublayer of the Data Link layer using the Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) protocol. The various 802.11*x* standards that were just described define the network access mechanisms and port assignments used by wireless devices to connect to Ethernet networks. [Figure 14.10](ch14.html#the_relationship_of_the_802.11_protocols) illustrates the placement of the different 802.11 standards in relation to the OSI networking model.

In this model, the MAC layer handles synchronization, power management, roaming, and the MAC-MIB. The Physical layer contains the Physical Layer Convergence Protocol (PLCP) and Physical Medium Dependent (PMD) sublayers. The PLCP is the layer that handles the Carrier Sensing part of the CSMA/CA protocol. The PMD modulates and encodes the signal in the 802.11 protocol. As you can see in [Figure 14.10](ch14.html#the_relationship_of_the_802.11_protocols), there are several different modulation schemes in use in the Physical layer. These include IR, CCK, FHSS, DSSS, and OFDM transmissions, which were described in the previous sections. CCK was described previously in the section on modulation.

![The relationship of the 802.11 protocols to the OSI data model](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1410.png)

**Figure 14.10. The relationship of the 802.11 protocols to the OSI data model**

### Collision avoidance

There are two main systems for collision avoidance that are used on 802.11 wireless connections— Distributed Coordination Function (DCF), also called the Physical Carrier Sense Method (PCSM), and point coordination function (PCF). In DCF, the station that will transmit data listens for a quiet period and then transmits a frame. The period between frame transmissions, while short, is randomized, and with DCF the transmitting station will then send a stop and wait for an Automatic Repeat reQuest (ARQ) packet after each packet it sends. The sending station then waits for an acknowledgment (ACK) or a negative acknowledgment (NAK) reply from the receiver before sending more packets. Other stations that want to break into the conversation are limited by the fact that the wait between ARQ and ACK/NAK is much shorter than the listening period.

The second technology employed for collision avoidance is PCF. Some references refer to this technique as the virtual carrier sense method. In situations where the transmitter and receiver are separated by enough distance, the time lag between an ARQ and an ACK/NAK may be too long to avoid interruptions. Other sending stations may transmit during the delay, introducing collisions into the wireless network at the point of convergence, which usually is at the access point. This phenomenon is called the hidden node problem, because two computers on a wireless network that are separated by enough distance may appear to be hidden from one another.

Ethernet, as you may recall from [Chapter 11](ch11.html), uses a similar version of CSMA called CSMA/CD, where instead of practicing collision avoidance, it manages collision detection. The reason for this difference is that it is difficult to detect collisions over a wireless medium, and so Wi-Fi adds additional mechanisms to avoid collisions in the first place, which unfortunately adds additional overhead and lowers throughput for wireless connections.

The potential solution to the hidden node problem is to create the equivalent of a shared managed circuit at the access point. PCF works by requiring transmitting stations to send a request to send (RTS) packet to the wireless access point. The RTS is then transmitted to other wireless nodes, and after a certain period, if the access point doesn't detect a transmission from another node, it sends a clear to send (CTS) packet to the transmitting node that sent the RTS and locks the circuit for that transmitter to use.

### 802.11 frame structure

The 802.11 MAC frame specification is shown in [Figure 14.11](ch14.html#the_structure_of_an_802.11_frame). It is similar in structure to Ethernet frames, which are described in detail in [Chapter 13](ch13.html). The frame consists of three parts: a Preamble, the PLCP Header, and the MAC PDU, which contains all of the data and the unique fields of the 802.11 protocol. When you examine the MAC PDU in detail, you find that it consists of three parts: the Header, Data, and a CRC32 checksum used to validate the frame. The Data portion is variable in length. Because the Data or payload portion of the frame originates at higher protocol levels, and CRC checksums use a standard algorithm, there's little more to say here about their use. In [Figure 14.11](ch14.html#the_structure_of_an_802.11_frame) the dotted lines indicate that that portion of the frame or field is expanded in the bar below it.

Continuing our Fantastic Voyage into 802.11 frames, you can see that the Header field contains all of the Session layer data. It is a little unique in that regard, because it contains four address fields where an Ethernet frame would contain two address fields: Sender and Destination. An 802.11 frame not only needs to account for the sender and target for the frame but it also needs to account for the MAC of the access point through which the frame must travel. Indeed, if the network is a peer-to-peer or ad hoc network, then a fourth address field is used that specifies the initial host in the P2P network that sends the beacon frames that other clients use to connect to that P2P network. Here is a summary of the address fields:

- ADDRESS_1 corresponds to the Receiver Address (RA) or destination.
- ADDRESS_2 corresponds to the Transmitter Address (TA) or sender.
- ADDRESS_3 corresponds to the Destination Address (DA), which is the ultimate destination of the frame.
- ADDRESS_4 corresponds to the Source Address (SA), which is the MAC address of the source that originally created and sent the frame.

![The structure of an 802.11 frame](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1411.png)

**Figure 14.11. The structure of an 802.11 frame**

The Duration field sets the amount of time that the frame is active (that is, can be forwarded before it is dropped), and a Frame Control field provides the mechanism that differentiates one form of 802.11 frame from another. In order to be able to sequence a set of frames, the Sequence Control field contains a 12-bit identifier for the Sequence number and a following 4-bit Fragment number for the frame's position in the Sequence number. A Sequence number is a counter that starts at 0 and is incremented to 4095 after which it is set back to zero. The Fragment number is incremented by one for each fragment as required, up to the limit of the field, which is 24 or 16.

The Frame Control field is the final expansion in [Figure 14.11](ch14.html#the_structure_of_an_802.11_frame) . This 16-bit field contains the following subfields:

- **Protocol Version**. This field displays the version of the 802.11 protocol used to create the frame. Any receiving STA can then determine if the frame can be properly handled based on that value.
- **Type**. The Type field contains a value that specifies whether the frame is a Control frame, Data frame, or Management frame. For example, Type 00 is a Management frame, and some of its allowed subtypes include 0100 Probe Req, 0101 Probe Resp, 1000 Beacon, and so forth.
- **Subtype**. Some frame types have an associated set of subtypes used to perform a specific operation. The Control frame subtypes include RTS, CTS, and ACK frames. A Data frame doesn't have a subtype. Management frames include the Beacon, Probe Request/Response, Association Request/Response, Reassociation Request/Response, Disassociation, Authentication, and Deauthentication.
- **To DS** and **From DS**. These two fields indicate if a frame is going to or coming from the inter-cell distribution center on a cell phone network, or to or from a router in a distributed network.
- **More Flag**. This Boolean field indicates whether there are more fragments of this particular frame being transmitted.
- **Retry (RTY)**. A Boolean field that indicates that this frame has been previously sent.
- **Power Management (PWR)**. A Boolean field that provides the state of the sending STA, either active or power-saving mode.
- **More Data**. A Boolean field that is used to signal a receiving STA that is in power-saving mode that more frames are on the way. APs that receive a frame with this field ON interpret it to mean that multicast or broadcast frames are being transmitted.
- **WEP**. This field indicates whether the Wireless Encryption Protocol (WEP) has been applied to the frame.
- **ORD**. The ORD field notifies the receiver that a sequence of frames with the ORD bit set to ON are to be processed in order.

### Connection example

Let's consider briefly the process involved in connecting an STA (wireless client) to a wireless access point in infrastructure mode. There are three separate parts to the process: scanning for a signal, authentication, and association. During association, the STA and AP are connected using a logically equivalent named object to a network connection for a wired network. [Figure 14.12](ch14.html#a_handshake_creating_a_connection_betwee) illustrates the handshake described in this section.

There are two separate types of scanning: active and passive. When actively scanning, the STA sends out Probe Req (Request) frames, and the AP then replies with a Probe Resp (Response) frame. In the passive scanning mode, the STA is monitoring the network, listening for a Beacon frame. The different frame types contain different fields in the Data or payload portion.

![A handshake creating a connection between an STA and AP on an open system](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1412.png)

**Figure 14.12. A handshake creating a connection between an STA and AP on an open system**

The authentication portion of the handshake depends upon whether an open connection, a shared key with WEP encrypted connection, or a WPA 802.11x connection is made. The open connection is easiest; the STA sends an Authentication frame and the AP sends an Authentication frame in reply.

To create an association based on a shared key and WEP, WEP must be enabled on both endpoints of the connection. The STA sends the Authentication frame, and the AP replies with an Authentication frame with a clear text challenge. The STA then replies to the challenge by sending back an Authentication frame with the encrypted challenge response. The AP decrypts the response and compares it to the challenge text. If there is a match, an Authentication frame is generated that is marked with a successful status and sent to the STA.

# Wireless Access Points and Gateways

A wireless access point (AP or WAP) is a transmitting and receiving device that is a node on a wireless network. An AP connects a wired network to a wireless one. The best way to think of an AP is that it is a wired-to-wireless bridge. An AP can also be a bridge between two wired networks when one AP connects to another AP. When you walk into a coffee shop and connect to a network, chances are that you are connecting to an AP. This type of networking is sometimes referred to as a Lilly Pad network, because wireless clients, like frogs, hop from hotspot to hotspot.

Most APs are limited to a single subnet of 255 clients, although performance limitations set a much lower practical limit for concurrent connections. You can buy an AP in 802.11a (rare), 802.11b (common), 802.11g (common), 802.11n (emerging), or combinations of two or three of these standards. Of the different combinations, 802.11b/g is the most common, 802.11a/g is less common, 802.11a/b/c is less common still, and 802.11n usually ships by itself.

Most home networks either purchase or have gateways installed at the interface of their broadband connection and the home network. Some of these gateways bridge the WAN to either a wired or wireless LAN, or both. A gateway is differentiated from an AP by the services it provides. Most gateways have DHCP and DNS servers that can be turned on, many have simple firewall functions such as Name Address Translation (NAT), and routing functions, and they often provide Universal Plug and Play (UPnP). Wireless gateways overlap with wireless routers, but are not nearly as robust in terms of their routing and firewall functionality. To designate devices that aren't pure gateways, the terms residential gateway, integrated gateway, or some other hybrid term is used.

Gateways offer the following services:

- 802.11 wireless connectivity
- Device association, setup, and configuration
- 802.3 router features and NAT traversal
- DHCP, DNS, IPv6
- Security (WEP and WPA)
- Device discovery and UPnP
- Diagnostics and utilities

In the next section, devices that extend the wireless network — repeaters and bridges — are described. Unlike gateways, which indicate network and broadcast boundaries, repeaters and bridges make the network bigger — that is, cover more area.

## Repeaters and bridges

A repeater, wireless range extender, or signal booster is a device that takes the signal that it receives and retransmits it at a higher signal strength. Repeaters use the same settings as the device they are repeating, and do not add additional complexity to the wireless network. When placed near the limit of an access point's range, the repeaters add an additional area of coverage for the signal. Many APs have a special mode that allows them to be a repeater. In [Figure 14.13](ch14.html#setting_the_repeater_mode_for_an_802.11), you can see the setting for defining a D-Link 802.11g Wireless Range Extender. A repeater may amplify the signal 50 percent or more, dependent upon the protocol, device, and antennas used.

![Setting the repeater mode for an 802.11 access point/range extender](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1413.png)

**Figure 14.13. Setting the repeater mode for an 802.11 access point/range extender**

### Tip

Repeaters can be finicky. When possible, use a repeater that is made by the same vendor as any AP, gateway, or router that it is repeating.

An AP can receive a signal from another AP on a different channel. When placed in repeater mode, the device needs to be set to the same channel and must also share the same SSID settings. Repeaters do reduce throughput, which limits their use on larger networks or for heavy traffic. Repeaters must both amplify a signal as well as broadcast it, which doubles the number of frames that the device transmits. However, for a home or a small office, repeaters are useful.

A good way to determine the number of wireless devices that you need is to draw a floor plan for your site with the different devices mapped out to show their coverage. This type of drawing can be valuable for determining when new devices are required, who needs to connect to which device, and many other assignments. An example of a wireless site plan is shown in [Figure 14.14](ch14.html#using_overlap_profiles_to_make_a_network).

![Using overlap profiles to make a network available throughout a floor](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1414.png)

**Figure 14.14. Using overlap profiles to make a network available throughout a floor**

Not all APs offer a bridging mode, and many that do aren't particularly efficient. Bridging tends to be better in enterprise wireless devices than those sold for the home market. It's always easier to bridge between two identical devices, and failing that, at least bridge between two devices from the same vendor using the same 802.11*x* protocol. To bridge two APs, do the following:

1. Open the wireless management software for AP_1 and set the device to point-to-point or wireless bridge mode.
2. Enter the MAC address for AP_2 into the bridge table.
3. Set the SSID and channel for AP_1.
4. Repeat Steps 1 to 3 for AP_2, entering the MAC address for AP_1 into that device's bridge table.
5. Position the devices and their antennas appropriately and test the connection.

You may find that vendors have different names for wireless bridging topologies: access point mode, workgroup bridge mode, point to point, redundant point to point, point to multipoint, and so on. The most common bridging topologies are:

- **Point-to-point**, a one-to-one topology.
- **Point-to-multipoint**, a one-to-many topology. Here, one access point is a root bridge and the others are non-root bridges. The root bridge is responsible for authentication and root assignment; bridge assignments should be unique and assigned the lowest bridge ID number. The root bridge should be placed in a central location to maximize throughput and coverage. In a point-to-point connection, when a root bridge isn't located the non-root bridge assumes the duties of a root bridge.
- **Redundant multipoint**. Duplicate pairs of APs are endpoints in a wireless connection, so that if one connection fails, the other can still support traffic between the two LANs.

## Wireless Distribution System

You can create a bridging link between two LANs using two access points in the Wireless Distribution System (WDS) mode. APs can be a main station that is connected to a LAN, a relay station, or a remote station. The relay station is a forwarding point between two other APs. Although this system bears a topological relationship to a bridge and is sometimes referred to as repeater mode, WDS also reduces the throughput of any wireless router/client connection by half, due to the forwarding traffic at the router that is connected to the wireless client.

WDS offers two different modes:

- **Wireless Bridging between two APs**, which only supports AP-to-AP communications
- **Wireless Repeating**, where the APs communicate with one another and with a wireless client

WDS isn't a Wi-Fi standard, and if you choose to implement this system, you will have a better experience if you use products from the same vendor when doing so.

### Note

Cisco's use of the acronym WDS refers to the Wireless Domain Service. This service is part of the Cisco Structured Wireless Aware Network (SWAN) that is used for roaming client services, and WLAN deployment and management.

Any wireless client that sends data to clients on a LAN through a remote AP has their frames forwarded to the relay or main AP without a change in the MAC addresses of the packets. Packets originating on the LAN are forwarded by the base AP to other members of the WDS automatically.

Each component in the WDS is assigned a different Service Set Identifier (SSI), and a table is created with each of the MAC addresses of APs in the WDS. Depending on the vendor, there may be a limit to the number of participants allowed. WDS must be configured so that all devices are on the same channel and are configured using the same security protocol (WEP or WPA) with the same keys. One problem with the current versions of WDS is that there is no mechanism for automatically changing the encryption keys during a session. This means that WDS works with WEP and with WPA-PSK, but does not support WPA2.

To set up a WDS connection, follow these steps:

1. In the network management utility, select the first two APs in your WDS system.
2. Find WDS and enable it on the first AP, entering the MAC address of the second AP into the first address box in the WDS table.
3. Select the channel of the first AP.
4. Open the management settings for the second AP, enable WDS, and enter the MAC address for the first AP in that device's WDS table.
5. Set the channel for the second AP to the same value as the first AP.
6. Continue to add APs, as required.

### Note

Care must be taken not to set up a WDS in such a way that it creates loops.

It is easy to create topological network loops with WDS, and when you do so, traffic will continue to circulate around the loop and cause network crashes. To avoid this problem, make sure that you avoid the following three scenarios:

- **Two APs with a WDS**, each connected to the same Ethernet link
- **Two APs connected by two WDS lines**, with one link being an 802.11a link and the other being an 802.11b/g link
- **Three APs connected with three links:** an 802.11b/g link, and two 802.11a links in a loop.

[Figure 14.15](ch14.html#examples_of_wds_loops_that_can_cause_net) illustrates the three loop conditions.

![Examples of WDS loops that can cause network crashes](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1415.png)

**Figure 14.15. Examples of WDS loops that can cause network crashes**

The following products are known to support WDS:

- 3COM Wireless 7760 11a/b/g PoE access point
- Alcatel Speed Touch (716 and 780)
- Apple Time Capsule, Airport Extreme, and Airport Express
- Asus WL-500g/gc/gU
- Belkin FD57230-4
- Cisco Wireless AP (Aironet)
- D-Link (DGL-4300, DWL-2100AP, DAP-1160)
- Motorola WR850G/GS
- Netgear ProSafe access point (WG102, WAG102, WG302, WAG302, and WG602v2/3)
- PLANET Wireless AP and Router (WAP-4000A, WAP-4033, WAP-4035, WAP-4036, WAP-4060PE, WRT-414, WRT-416, and WNRT-620)
- SMC EZ Connect g Wireless access point (SMCWEBT-G) SMC7988VoWBRA, SMC Barricade SMCWBR14T-G/G2
- USRobotics Professional access point (5453), MAXg (5432, 5441, 5451, 5455, 5461, 5465, and 9108), and Ndx (5454, 5464, and 9113)
- Zoom X6

These are just some of the WDS-supported devices that are available.

# Wireless Routers and Gateways

As you learned in [Chapter 9](ch09.html), routers are devices that connect two or more networks together and have some intelligence in them in the form of routing tables and algorithms for directing traffic along preferred routes. Routers are Layer 3 gateways, and function at the Network level in the OSI model.

A wireless router has the same functionality as a wired router, but adds a wireless interface so that it can function as an access point. Many small office home office (SOHO) routers have a few (four is typical) Ethernet ports, an 802.11 AP, and a parallel or USB port so that they can share a peripheral device such as a printer. The Linksys WRT54GL (802.11b/g), shown in [Figure 14.16](ch14.html#the_linksys_wrt54gl_broadband_router_is), is the classic example of a SOHO router.

![The Linksys WRT54GL broadband router is popular because it is Linux-based, relatively inexpensive (US$60), configurable, and easily customized.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1416.png)

**Figure 14.16. The Linksys WRT54GL broadband router is popular because it is Linux-based, relatively inexpensive (US$60), configurable, and easily customized.**

The one differentiating factor that separates an AP from a router is that an AP allows a client to browse or communicate with only one network, while a router allows a client to connect to two or more networks. Routers also examine IP packets to see what the destination is, and then route the packets based on the address. Access points do not examine the destination of packets, and forward all packets that they receive.

Consider using a router in place of an AP in the following situations:

- You have only one IP address to share. Routers provide DHCP and also DNS, as well as NAT for IP address sharing.
- You have to connect to multiple networks.
- You have a busy wireless network and require better network throughput than an AP provides.
- You require better network management, more powerful diagnostic tools, and browser-based control over a wireless network connection than most APs offer.
- You need more enhanced security, filters based on MAC addresses, IP addresses, domain names, time of day, and other features that are often offered by firewalls. Some routers support multi-session IPsec, VPN, WEP, and other security options.

## Router configuration

Most wireless routers are configured by browser-based utilities. You enter the IP address for the wired portion of the router, and log into the utility with an ID and password. Although you can set most routers up manually, most are configured using some form of wizard or easy setup function. To configure a router, in most cases, you will need to provide the following pieces of information:

- The IP address and the domain server for the broadband or WAN network. In many cases, this network interface is set by DHCP by an ISP, and you set the router to accept an address automatically.
- The IP address pool for the wireless network interface. If you turn on the router's DHCP, then clients can take a dynamic address; or clients can be assigned static addresses from the same subnet.
- The assigned service set identifier (SSID) and the channel number.
- The type of security that you want to implement, and a new administrator ID and password. Although you can use the default administrator account settings, these are well known by hackers who can use them to compromise your system.
- Any filter types that you want to implement, such as MAC address filtering.

## Router upgrades

There are many freeware or shareware router upgrades available. They turn a $60 router into the equivalent of a much more expensive router product with the advanced features added in software. An example of these is BrainSlayer's DD-WRT open source firmware upgrade (`www.dd-wrt.com/wiki/index.php/Main_Page`), which has a feature list that is too long to detail fully. Among the highlights are OpenVPN, QoS, Samba, Site Survey, WDS, MAC filtering, WPA over WDS, and others.

The Tomato router from `polarcloud.com` (`www.polarcloud.com/tomato`) is another significant upgrade to the software that many vendors include with their routers. It adds a friendly GUI, and has a number of advanced features such as a bandwidth monitor, QoS, access control, connection management (P2P), CIFS (Samba), WDS, Telnet, scripts, and wireless site survey.

The Tomato router is displayed inside a browser such as Firefox or Internet Explorer. [Figure 14.17](ch14.html#bandwidth_monitoring_is_one_of_the_featu) shows the Bandwidth Usage screen inside Tomato. Tomato is particularly strong in displaying reports. You can display charts on your connection distribution based on your QoS rules.

![Bandwidth monitoring is one of the features offered by the Tomato router software.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1417.png)

**Figure 14.17. Bandwidth monitoring is one of the features offered by the Tomato router software.**

The Tomato router software is a firmware upgrade for Broadcom-based router chipset products, including:

- Linksys WRT54G v1-v4, WRT54GS v1-v4, WRT54GL v1.x, WRTSL54GS (no USB support)
- Buffalo WHR-G54S, WHR-HP-G54, WZR-G54, WBR2-G54
- Asus WL500g Premium (no USB support)
- SparkLAN WX-6615GT

In particular, this is a very popular upgrade for the Linksys WRT54GL; the "L" in the name indicates that the router uses a Linux kernel. One feature offered by Tomato is called signal boosting. The WRT54GL is set to transmit at a default power of 42 mW, but can be boosted to 251 mW as a software setting, with 70 mW considered to be a safe setting. The one setting essentially doubles the coverage of the router, which alone makes it valuable.

Taken as a whole, the Tomato router isn't quite as powerful as DD-WRT, but it is much easier to work with. Both products dramatically improve the functionality of your wireless router, provided that the model you have supports the upgrade.

# OLPC XO Wireless Network

The One Laptop Per Child (OLPC; `www.laptop.org`) project developed as its networking technology a P2P ad hoc wireless network that is highly mobile, topology-independent, and self-healing. Each laptop can locate and find other laptops to create a network link, thus providing shared access to resources for all systems currently connected. The first model laptop, called the XO, has a number of unique features that space precludes describing here, but the wireless mesh network (WMN) that is created by XO is one of the most important features, as it enables communication on the system.

A self-configuring, self-healing mobile network is sometime referred to as a mobile wireless ad hoc mesh network, or MANET. When the wireless system involves vehicles, it may be referred to as a Vehicle Wireless Ad Hoc Network, or VANET.

The wireless mesh networking chip in the XO laptop runs software that is compliant with the IEEE 802.11s draft standards for mesh networking. It enables communications with other devices out of the box. The 802.11s standards extend the 802.11 MAC to support unicast and broadcast/multicast transmission over self-configuring multi-hop topologies. In the 802.11s mesh network architecture, each node is called a Mesh Point (MP). MPs can be standard 802.11 APs. [Figure 14.18](ch14.html#the_xo_laptop_with_the_space_mesh_neighb) shows the Space mesh view with discovered Wi-Fi devices.

![The XO laptop with the Space mesh neighborhood view. Each icon on the laptop screen represents the condition of a wireless device within connection distance.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1418.png)

**Figure 14.18. The XO laptop with the Space mesh neighborhood view. Each icon on the laptop screen represents the condition of a wireless device within connection distance.**

The 802.11s defines a routing protocol called the Hybrid Wireless Mesh Protocol, or HWMP, that is a mandatory component of the draft standards' compliance. HWMP is meant to be vendor-independent, allowing any device running 802.11s to participate in any MANET it finds.

The routing protocol for HWMP is based on elements of the Ad hoc On-Demand Distance Vector (AODV) routing protocol and a tree search algorithm. AODV was developed by university researchers and uses a distance-vector algorithm. AODV is currently in a draft standard and can be viewed at `http://tools.ietf.org/html/rfc3561`. A previous protocol called Destination-Sequence Distance Vector routing (DSDV), which AODV is based on, creates ad hoc networks using a dynamically populated lookup table of known hops; this is suitable for a network with a small number of nodes but can suffer from performance problems when a large number of paths must be calculated. AODV improves on DSDV by using an algorithm to calculate the metrics of a route, by taking into consideration both the hop count and the next hop performance information. It learns of different routes by transmitting a RouteRequest packet and waiting for a RouteReady reply.

The 802.11s standard allows for the use of a server on the network. The One Laptop Per Child server is called the OLPC XS school server. That server supports XO clients, up to 100 laptops per school server. The OLPC laptops and servers are currently the only products that you can buy with 802.11s built into them, although that will change rapidly over the next couple of years. Starting with Linux kernel version 2.2.26, the 802.11s standards will be built into the mac80211 layer of the operating system.

# Antennas

Antennas play a significant role in the ability of a wireless device to transmit or receive signals. Many antennas are omni-directional, some are directional, and a few are highly directional, depending upon the nature of their construction.

[Figure 14.19](ch14.html#antenna_directional_profiles) shows these three different types of antenna profiles. The top profile is omni-directional, and antennas of this type tend to be spherical in design. The middle profile is directional and is directed out over two of the three Cartesian axes. Antennas that project with a directional profile are exemplified by a corner antenna. Highly directional profiles are projected down a single axis of the three Cartesian axes. Yagi antennas look like long sticks or boom microphones and have a highly directional profile. These different antenna types are shown in [Figure 14.19](ch14.html#antenna_directional_profiles).

## Antenna characteristics

You measure the efficiency of an antenna by its gain, normally given as a rating in decibels (dB). The ratio of the output signal strength of an amplifier to the input strength of the signal is the gain. Gain is more often expressed in terms of the number of decibels that a hypothetical isotropic radiator would have in units of dBi. An isotropic radiator is one that radiates a signal equally in all directions. Antennas offer reciprocal gain (amplification both for transmission and reception). So adding a better antenna should improve the signal for both endpoints of a wireless connection.

![Antenna directional profiles](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1419.png)

**Figure 14.19. Antenna directional profiles**

Antennas are tuned for a specific frequency, or they are tunable. An antenna designed for an 802.11b signal won't work well for a higher-frequency 802.11g signal, although the reverse is commonly true.

Radio signals are subject to reflection effects that create interference patterns. The result is an effect called multipathing. A receptor locks onto the strongest signal, but at certain places in the path, signals interfere with one another and create dead spots. Moving a wireless antenna or changing its direction can often have a major impact on performance.

Wireless signals over air lose strength over distance, as described by the free space path loss equation. The loss varies as a square of the distance. Indoors, wireless signal loss is dependent upon the material involved. Concrete lowers a wireless signal more than wood. The amount of material is also important, and so signal strength is greater up through a ceiling than it might be traversing a wall at a highly oblique angle. Some wireless devices allow you to modify their power output, thus increasing their coverage area and the dispersion of any directional antenna attached to the device.

An omni-directional antenna radiates equally in all directions and usually takes the form of a thin rod or long, flat stick. A directional antenna is one with a wide dispersion of 80 to 120 degrees. Directional antennas are often used in room corners and radiate to all parts of the room. Directional antennas are parabolic reflectors, right-angle deflectors, and panel deflectors that concentrate the signal. Highly directional antennas use a line of perpendicular elements, a can (cylindrical enclosure), or both. The classic example of a highly directional antenna is a Yagi antenna. Some directional antennas can achieve connections in the range of 1 to 10 miles line of sight, but are very sensitive to obstructions.

The directional nature of an antenna is described by its Front-to-Back (F/B) ratio. The F/B ratio measures the center point beam strength in both directions and takes its ratio. Omni-directional antennas have F/B ratios approaching 1.0; for highly directional Yagi antennas, the ratio can be on the order of 5 or 6. [Figure 14.20](ch14.html#four_different_types_of_wireless_antenna) shows four different types of wireless antennas— a) Hawking HAI7SIP Hi-Gain 7 dBi Omni-Directional Antenna; b) Hawking HAI8DD Hi-Gain 8 dBi Directional Dish Antenna; c) Hawking HAI15SC Hi-Gain 15 dBi Corner Antenna; d) Wade J250-915-10 900 MHz 13 dB Yagi Antenna.

An antenna's radiation pattern shows the directional nature of the signal strength. The vertical slice of the radiation pattern or elevation cut can be very different from the horizontal slice of the radiation pattern, called the azimuth. This difference is important for any WLAN that spans floors or covers an entire building. An increase in the power of the signal can narrow either the elevation plane or the azimuth plane's coverage, or both for an antenna. A radiated signal can be circular, or it can be mainly horizontal or vertical.

The orientation of an antenna is affected by its polarization. In an antenna, the magnetic and electric fields are perpendicular. With a horizontally polarized antenna, the antenna is meant to be positioned so that its electric field is parallel with the ground. For a vertically polarized antenna, the electric field should be perpendicular to the ground. Both antennas participating in a wireless connection need to have their polarization aligned.

![Four different types of wireless antennas](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1420.png)

**Figure 14.20. Four different types of wireless antennas**

Antennas with a signal strength that is isotropic (the same in all directions) have a gain of 1 dB or 0 dB. A gain of 2 dB or 3 dB represents a doubling of the signal strength. Each additional 3 dB doubles the signal strength. You would use a higher-gain antenna to improve the transmitted signal. The limit for a wireless signal is set by law. The United States has a limit of 1000 mW, Japan's limit is 10 mW/MHz, and in Europe it is 100 mW (as measured by the Equivalent Isotropic Radiate Power, or EIRP). The gain can be different when transmitting or receiving.

An antenna's beamwidth is a measure of the angle at which a transmission drops off in each of the two principle axes. The angle is measured between the points at which the signal is half the maximum signal down the center of the beam. Narrow beamwidth antennas are more powerful and have a longer range.

## Multiple-Input Multiple-Output

Multiple-Input Multiple-Output (MIMO) is a multi-antenna technology that boosts the performance of wireless transmission and reception, part of a new generation of "smart antennas" that are changing the nature of 802.11*x* wireless communication. MIMO itself is part of the specification of 802.11n, 802.16e WIMAX broadband mobile, and will be found in all of the next-generation 4G networks.

MIMO works by creating multiple data streams over the same band concurrently using spatial multiplexing, which has the potential to double or triple throughput. The different streams can also take different paths from the transmitter to the receiver (reflecting off of surfaces if necessary), and with proper processing, all the received signals are superposed to create an enhanced reception, which increases gain and lowers multipath interference. [Figure 14.21](ch14.html#combining_mimo_antenna_signals_in_a_two-) illustrates the superposition of two antenna signals with MIMO, plotting the Signal-to-Noise Ratio (SNR) to the frequency.

![Combining MIMO antenna signals in a two-antenna array to enhance signal reception](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1421.png)

**Figure 14.21. Combining MIMO antenna signals in a two-antenna array to enhance signal reception**

MIMO antennas offer the following benefits:

- Resistance to fading
- Larger coverage, greater capacity, and increased data throughput
- Better spectral efficiency
- Reduced power consumption
- Lower network costs

Many wireless devices sport multiple antennas and can benefit to some degree from this superposition effect. For example, when you have multiprotocol access points, such as 802.11b/g, they may come with one antenna tuned for 802.11b and another tuned for 802.11g. What separates MIMO from these other devices is that MIMO antennas have a Digital Signal Processor (DSP) that breaks the carrier wave up into a set of carriers and then transmits the RF over each antenna separately. At the receiving end, each antenna collects a signal and feeds it back into a DSP for recombination. Using MIMO results in more power being transmitted, and it can be engineered to create a more focused beam; as a result, you get both increased power gain and array gain. [Figure 14.22](ch14.html#linksys_wireless-n_pci_adapter_with_mimo) shows the Linksys Wireless-N PCI Adapter with MIMO technology and antennas.

![Linksys Wireless-N PCI Adapter with MIMO technology and antennas](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1422.png)

**Figure 14.22. Linksys Wireless-N PCI Adapter with MIMO technology and antennas**

# Wireless Software

Because most Wi-Fi devices are managed either in the operating system or through the software that the manufacturer bundles with the devices, the most common category of Wi-Fi software that people install are network scanners. Network scanners are already built into most desktop operating systems. When you open the Windows network connections and scan for wireless networks, the software doing the scanning is a network scanner.

The results returned in Windows XP and Vista are a pictograph with five bars representing the connection strengths: poor, fair, good, very good, and excellent. [Figure 14.23](ch14.html#the_wireless_network_connection_status_d) shows the Wireless Network Connection Status dialog box from Vista. While this information is useful and lets you decide which wireless network to connect to based on reception, the speed of the network, and how long the interface has been up, it's not nearly enough information to diagnose a wireless network and get a good picture on how different systems are faring. To this end, there are a number of network scanning packages that you can install that give a wide range of information that is useful. Many of these programs were developed by enthusiasts and are free or inexpensive shareware that you can try and then purchase.

![The Wireless Network Connection Status dialog box in Microsoft Vista](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1423.png)

**Figure 14.23. The Wireless Network Connection Status dialog box in Microsoft Vista**

The granddaddy of network scanners is Marius Milner's Network Stumbler (`http://stumbler.net`), or NetStumbler, which is in version 4.0, released in 2004. This version detects 802.11a/b/g signals, provided that your Wi-Fi receiver supports them. Although this version doesn't yet work with Vista, it does work with Windows XP, 2000, and 9x. A version of NetStumbler that runs on the Windows CE operating system (handhelds and cell phones) has been released, and is called MiniStumbler.

Chances are that if you've seen a movie where the characters go wardriving, it is NetStumbler that they were using. Wardriving involves driving around town looking for a network that you can hop onto. The name comes from the 1983 film *WarGames*, where automated software would robo-dial numbers to connect to other systems.

Network scanners are useful for the following purposes:

- Checking wireless configurations
- Determining if there are unknown rogue access points
- Optimizing network connections
- Measuring the signal strength at different locations
- Finding sources of signal interference
- GPS mapping
- And, of course, wardriving for fun and profit

NetStumbler isn't an entirely passive observer. It collects network metrics by using an Active Scanning technology that transmits probe requests. This means that anyone listening can detect NetStumbler's use, particularly if there isn't a lot of competing Wi-Fi traffic in the area. Because NetStumbler relies on responses to its probe requests, it detects access points, but not standard wireless network nodes or stations.

Among the alternatives to NetStumbler are:

- **inSSIDer (**`www.metageek.net/products/inssider`**)**. This is an open source program that works with the Windows Wi-Fi API to survey wireless networks. inSSIDer is offered by MetaGeek; they have several other commercial products in this area, including Wi-Spy (a spectrum analyzer), Chanalyzer, and others. [Figure 14.24](ch14.html#inssider_is_an_example_of_a_wi-fi_networ) shows an inSSIDer Wi-Fi network scan.
- **iStumbler (**`http://istumbler.net`**)**. This is for Mac OS X, AirPort, Bluetooth, and Bonjour.
- **Kismet (**`http://kismetwireless.net`**)**. This is a scanner, sniffer (it examines 802.11 frames), and intrusion-detection software package that does passive scanning. Kismet runs on both Windows and Mac OS X.
- **MacStumbler (**`www.macstumbler.com`**)**. This is for the Macintosh (OS X version 10.1 or greater, an 802.11b/g scanner).![inSSIDer is an example of a Wi-Fi network scanner.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1424.png)**Figure 14.24. inSSIDer is an example of a Wi-Fi network scanner.**
- **Microsoft Vista netsh command**. This command can be used to discover access points. The format of the command is as follows: `netsh wlan show networks mode=bssid`.
- **Vistumbler (**`http://vistumbler.net`**)**. This is an AutoIT script that graphically displays the output of the `netsh` command. It is Vista-compatible.

This list is for freeware or shareware network scanners. Dedicated Wi-Fi sniffers and spectrum analyzers are also available from a variety of vendors. Some of the commercial software in this area can be high-end and rather pricey. A short list of Wi-Fi software may be found at `www.tech-faq.com/wi-fi-software-tools.shtml`.

# Security

Part of the 802.11*x* protocol definition includes the methods that are used to provide port access and to authenticate connections. The LAN port used to provide network access is called the Port Access Entity (PAE). A PAE doesn't have to be a physical port; it is a logical entity that is associated with a port. PAEs can be the requestor of access (or supplicant) or the provider of access (or authenticator), or they can play both roles.

Somewhere on the wireless network is an authentication server that stores the credentials of the supplicant and responds to authenticator requests that are used to provide or deny wireless access to network services. Authentication servers can be established within an AP, or requests can be forwarded to authentication servers. A common setup sends authentication requests in the Remote Authentication Dial-In User Server (RADIUS) protocol to a RADIUS.

The authentication server can differentiate between two different port types. An uncontrolled port is a port that allows for unauthenticated communications between the authenticator (usually the wireless AP) and a wired LAN. Frames that are sent by a client are never simply passed along by the AP; an uncontrolled port requires that the frames originate on the AP. A controlled port can also be defined where data is only exchanged between wireless clients and LAN nodes through the port when the wireless client has been authorized by the 802.11*x* authentication server. In order to prevent contention for access to a port, the authentication server creates a unicast session key for each client. Without a session key, the wireless client's frames are dropped at the controlled port.

## Wired Equivalent Privacy

Wired Equivalent Privacy (WEP) encrypts the data in 802.11 frames using a 40- or 104-bit RC4 symmetric stream algorithm that is sent over a wireless connection. The presence of encryption is indicated by the value in the WEP bit of the Field Control subfield of the Header field in an 802.11 frame. Security uses a shared key system, with each endpoint of the connection holding one of the two necessary keys. WEP defines a multicast/global key for use with multicast or broadcast sessions. A unicast session key for encryption of a point-to-point communication of unicast data that is sent between an AP and a wireless client, and for broadcast data sent from a wireless client to an AP, are also defined.

### Note

WEP is considered to be relatively weak protection, as the encryption has been broken. It is better than no security, but not nearly as good as WPA. When possible, enable WPA at your APs.

The WEP encryption process works as follows:

1. The Data or payload portion of an 802.11 frame is used to create a CRC checksum (also called an Integrity Check Value, or ICV) that is used to verify the data after decryption.
2. The CRC is inserted into the frame just after the Data portion.
3. A 24-bit Initialization Vector (IV) is calculated.
4. The IV is appended to the WEP encryption key.
5. The value "IV+WEP key" is then fed to a pseudo-random number generator (PRNG) to create a key stream, which is a sequence that is the same size as the IV+WEP sequence.
6. The key stream is combined with an XOR operation with the "Data+IV" sequence to create the encrypted payload.
7. The 802.11 frame is then composed, with the IV placed before the encrypted payload.

[Figure 14.25](ch14.html#the_wep_encryption_solidus_decryption_pr) illustrates the WEP encryption/decryption process.

![The WEP encryption/decryption process](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1425.png)

**Figure 14.25. The WEP encryption/decryption process**

Decryption is essentially the reverse of the encryption process, and works as follows:

1. The IV is extracted from the encrypted frame and appended to the WEP encryption key. The IV is the field in front of the payload.
2. The "IV+WEP" value is input into the same PRNG that created the encrypted key stream, and the output is the same key stream that was used to create the encrypted payload.
3. The key stream is then XORed with the payload (which was the encrypted "Data+CRC"), to decrypt the combined "Data+CRC" sequence.
4. The ICV is then used to calculate the IV, and if they match, the frame is valid and the data is used.

WEP was the first of the wireless security protocols to be implemented, and it is widely used. However, the WEP protocol has some serious issues related to it. The main issue is that the WEP encryption keys must be sent securely over the wireless link. Because WEP keys are clear text, they can be sniffed. Also, WEP keys aren't changed without manual intervention. If a hacker gets access to the WEP key, then that key can be used until the sender changes the key. There is also no mechanism to manage a set of keys, and so, as the network grows, WEP key management becomes impractical.

## Wi-Fi Protected Access

Wi-Fi Protected Access (WPA), and WPA2, which is the current-generation 802.11*x* authorization and encryption protocol, solves some of the problems of WEP by using the Temporary Key Integrity Protocol (TKIP) to generate keys. The TKIP key uses a 48-bit Initialization Vector and a 128-bit encryption key to generate a new key for every packet that is transmitted. WEP used the same key for all packets. The longer key length and varying encryption key make it impossible to gain access by simply sniffing data in transit. As with WEP, WPA provides unicast and global/multicast encryption.

With WPA, both endpoints in the association (connection) have a Pre-Shared Key (PSK), which means that the key can't be intercepted in transit; this makes WPA more secure and makes it suitable for small wireless networks. WPA ships in most modern APs after 2003, but it can be added with a firmware upgrade to older equipment from the 1999 to 2003 era. The WPA standard is maintained by the Wi-Fi Alliance, and products are submitted to their certification program for compliance, so that they can use the logo.

WPA2 is the full implementation of the mandatory requirements of the 802.11i security standard that was ratified in 2004. Any device that is WPA2-compliant must carry the Wi-Fi trademark and logo. This protocol uses the Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP), which uses an Advanced Encryption Standard (AES) algorithm. Not all older devices will work with WPA2, because not all of the older routers understand both TKIP (from WPA) and AES (from WPA2). So while WPA2 is more secure, it does not offer backwards-compatibility. [Figure 14.26](ch14.html#the_security_settings_for_the_netgear_wn) shows the security settings for a Netgear RangeMax router (Model WNR834B).

WPA has two levels of security defined: WPA Personal (WPA-PSK), and WPA Enterprise. WPA-PSK uses a Pre-Shared Key, which makes it convenient to use in small office home office, or SOHO, networks that don't have an 802.11*x* authentication server installed. To access a WPA-PSK secured network, a password is entered as either ASCII characters (8 to 63) or 64 hexadecimal digits (256 bits). With ASCII characters, a hash function combines those characters with the wireless network SSID to create a 256-bit pass-phrase string. WPA-PSK is subject to dictionary-based (lookup tables) brute force attacks, and so it's important to create strong passwords. The recommendation is for mixed password strings of 13 characters or more.

[Table 14.2](ch14.html#wireless_security_on_home_devices) lists some of the common media devices in use that offer wireless security.

![The security settings for the Netgear WNR834B router allow it to be configured for WEP and the different forms of WPA.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/1426.png)

**Figure 14.26. The security settings for the Netgear WNR834B router allow it to be configured for WEP and the different forms of WPA.**

**Table 14.2. Wireless Security on Home Devices**

| Media Player | WEP | WPA-PSK | WPA2-PSK |
| --- | --- | --- | --- |
| Asus Eee PC | Yes | Yes | Yes, in hardware |
| iPhone | Yes | Yes | Yes |
| Nintendo DS | Yes | No | No |
| Nokia N800/N810 | Yes | Yes | Yes |
| PlayStation 3 | Yes | Yes | Yes |
| PlayStation Portable | Yes | Yes | No |
| Wii | Yes | Yes | Yes |
| XBox 360 Wi-Fi | Yes | Yes | No |

In WPA Enterprise, a RADIUS server provides the authentication to any use requiring connection or access credentials. The AP forwards requests to the RADIUS server, which then either authenticates or denies the request based on data stored on the RADIUS server. If the RADIUS server is unable to decide the status of the request, it can request additional information from the source or a second password.

WPA is much more secure than WEP, particularly when a strong password is chosen. While AES and WPA2 are even more secure than TKIP and WPA, both are strongly preferred over WEP.

# Summary

In this chapter, you learned how to create and manage wireless connections based on the IEEE 802.11 Wi-Fi standard. Wireless networks may be classified as either ad hoc or infrastructure.

Wireless networking uses radio frequencies in the 2.4 GHz or 5 GHz frequency range. Channels are created and signals are sent over carrier waves using spread spectrum transmission. Signals are encoded onto the carrier waves using modulation. The 802.11*x* frames are similar to Ethernet frames. Frames are sent using Carrier Sense Multiple Access with Collision Avoidance. Methods for handshaking, traffic control, and connection management were described.

Access points, gateways, and routers are the wireless devices that are used by wireless clients to connect to networks. You learned about the characteristics of these different devices. Other topics covered included wireless software, and the different forms of wireless network security methods in common use today.

In the next chapter, you learn about storage networks and how they can be integrated into data networks to improve data availability and performance.
