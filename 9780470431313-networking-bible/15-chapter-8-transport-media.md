# Chapter 8. Transport Media

**IN THIS CHAPTER**

- Wiring standards
- Twisted-pair, coaxial, and fiber-optic cables
- Ethernet wiring
- The behavior of light in fiber optics
- Wireless communications links

In this chapter, I cover three types of transport media that occupy the physical layer of a network: wired cables for electrical current, fiber-optic cables for light, and wireless links using mainly radio and microwave frequencies.

Different cable types require different methods for running cable, connecting together, and organization. This chapter describes some of the considerations you need to make when installing a network in a building.

# Wired Media

Most people don't pay enough attention to the physical layer of their network. Given that wiring is something that might last 10 to 15 years, it's worth considering which type of wired media will support your network, not only for its present capabilities but also for future ones.

There are four main types of wired media in use:

- **Twisted pair**. Shielded, copper-based, twisted-pair cable. This form of cabling is used in local area networks, particularly older types of networks.
- **Coaxial**. Copper-based coaxial cable. Coaxial cable is thick, multiwire cable that can be used for both high bandwidth and high connectivity connections.
- **Ethernet**. Unshielded, copper-based, twisted-pair cable. The unshielded twisted-pair wiring is the most commonly used network cable and is used on most versions of Ethernet.
- **Fiber optic**. Glass or plastic-based fiber-optic cable. Optical cable is the basis for high-speed and high-capacity networks.

Each of these cable types offers different connection speeds, has a different bandwidth, and requires different network topologies and physical connections. In the sections that follow, good wiring solutions are discussed and the four wire types are considered in more detail.

### Note

The physics of signals traveling on wires is described in [Chapter 5](ch05.html).

## Wiring the physical plant

Good wiring solutions require some preparation, especially when there are many cable runs and when runs must span rooms, floors, and buildings. Many localities have specific building codes for wiring that include standards — such as the use of conduit — that must be met. For that reason, a licensed electrician may be required to install network cable to comply with the codes and to validate the work. Cable runs need to be insulated, and should be routed in a way that makes it easy to adapt to changing systems.

Many networks route their wiring through what is called a *patch panel*, or a collection of patch panels, which is often called a *wiring closet*. The purpose of a patch panel is to allow connections to be quickly modified when systems are moved, or when projects require different connections. An example of a patch panel is shown in [Figure 8.1](ch08.html#a_patch_panel). Good cable management dictates that you adopt a color-coding system so that you can visually tell which cable is for what connection. Administrators often organize these tables into Excel worksheets, and number and label cables at both ends for greater clarity. For groups of cables running to a server rack or into a room, cables are tied together into bundles that make it clear which group they are running to. This organizational system can save a lot of time and frustration later on when you are trying to troubleshoot problems on a network.

Building codes may require that cable be surrounded by an insulator. Insulators can be Teflon (PTFE, also called plenum), Polyvinyl Chloride (PVC), or more frequently, Polyethylene (PE). Teflon is the most expensive of the three but is fire retardant. PVC, although cheaper, will burn and give off toxic gas in a fire. Polyethylene is flammable, but its fumes are non-toxic.

Cabling that is exposed to bending and flexing, tread underfoot, stretched, or crimped is subject to failure. Failure is often the best-case scenario for problems of this type because it is relatively easy (although time consuming) to replace a failed cable. The major problems occur when a network cable fails intermittently. Intermittent failure makes it hard to diagnose the problem, and harder still to locate it. You never know whether the failure is due to hardware or software, a connection setting, a bad port in a switch or router, and so on. Because it is intermittent, the amount of time you spend grows exponentially. Many times, you never find the problem and are forced to simply live with it. So an ounce of prevention is worth a pound of cure.

![A patch panel](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0801.png)

**Figure 8.1. A patch panel**

There are many ways to route cable conveniently and safely. If a room has a suspended ceiling, then routing cable above the suspension harness is a good method. You can also buy hangers and special cabling tracks that can be added to ceilings to achieve the same effect. You can use special runners to protect cable that is routed on a floor. In computer rooms, raised flooring serves the same purpose for routing cable as suspended ceilings. [Figure 8.2](ch08.html#an_enclosed_cable_raceway) shows a raceway that uses a two-part design. The lower part holds the wire, and the upper part snaps on to seal the raceway. Alternative designs are open-wire baskets (for hanging), wall mounts, ceiling mounts, and floor runs.

It is also a good idea to route network cables in a conduit. However, you should never use network conduits to run electric power lines with your network cable. Electric lines interfere with the signal in copper network cable by creating a voltage that can degrade the signal or, in severe cases, damage equipment that the network cable is attached to. The dynamo effect that creates a current when a wire is placed near a moving magnet also creates a magnetic field (an applied voltage) when electricity passes by a metallic object.

![An enclosed cable raceway](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0802.png)

**Figure 8.2. An enclosed cable raceway**

Electric motors, fluorescent lights, motors such as pumps or refrigerators, and any other devices that have high magnetic fields and can cause electromagnetic interference, or EMI. Similarly, devices such as wireless routers, microwave ovens, even wireless telephones can be a source of radio frequency interference, or RFI, which can give rise to spurious signals and degrade communication on network cables. For this reason, cables should be routed away from these various sources or adequately shielded in order to protect the network cable from these outside interferences. Longer cable runs tend to exacerbate these problems, as network signal strength decreases over longer segments.

## Twisted pair

Twisted-pair wiring is the most common network cable in use today, particularly unshielded twisted pair. It is used to carry both analog and digital signals. Indeed, the very first telephone transmission by Alexander Graham Bell was over twisted-pair wiring. The wiring used in plain old telephone service (POTS) lines is composed of two sets of twisted-pair wiring, two wires of which are unused. It is these unused wires that allow for the installation of DSL, ISDN, or network connections to run over telephone lines in houses and offices.

Twisted pair is popular because it is relatively cheap to produce and is both insulated and shielded. The twisted wire offers the benefit of averaging out the impact of external magnetic or electrical fields and lowering the amount of crosstalk or interwire signal interference. Twisted-pair wiring offers many of the benefits of coaxial cable. [Figure 8.3](ch08.html#unshielded_twisted-pair_wiring_and_an_rj) shows twisted-pair wiring in its unshielded form, along with the common RJ-45 jack that is used to connect twisted-pair wiring together through couplers

![Unshielded twisted-pair wiring and an RJ-45 male plug](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0803.png)

**Figure 8.3. Unshielded twisted-pair wiring and an RJ-45 male plug**

Shielded twisted-pair (STP) wiring was introduced by IBM in the early 1980s and is still in use on Token Ring networks. It never achieved the popularity of unshielded twisted-pair (UTP) wiring, probably because of the extra cost of the cables and their bulky nature, which made them hard to work with.

In STP, there are two wire pairs, each pair of which is twisted around its mate. STP shielding is composed of either a foil or braided wire, and must be grounded at one end. When foil is used, the wire may be referred to as *foil twisted pair*, or FTP, but this is an uncommon designation.

While the twisted wire helps to reduce crosstalk in the wires over its run, STP suffers from crosstalk and EMI degradation at the ends of the wire. The more twists per meter, the more protection is afforded against crosstalk and the fewer data errors are incurred. The twist rate is referred to as the *pitch* of the twist (turns per meter) and is usually varied between wire pairs in order to suppress signal degradation.

### Note

The acronyms NEXT and FEXT are used to describe Near End Crosstalk and Far End Crosstalk. NEXT measures the interference of two cables in a pair as measured at the same end of the cable. FEXT measures the interference of the two pairs at either end of the cable, with the cable as the transmitter of the signal.

UTP is widely used in many different network types. UTP wiring is constructed from pairs of copper wire that are twisted but not insulated. UTP is the cable used in Ethernet networks and often in telephony applications. When used in T-1 lines, twisted-pair wiring requires that the signal be refreshed by a repeater every 1.8 km (1.1 miles).

UTP categories are an EIA/TIA (Electronic Industries Alliance/Telecommunications Industry Association) standard. CAT 5 is the most common wiring in current use for networks; it was introduced in 1988. CAT 3 is used for telephony, and on older networks as runs from a central wiring cabinet. The colors of the wires are standardized. Most UTP cable conforms to the Underwriters Laboratories (UL) standards and lists the category on the outside of the cable. UTP cable is connected to RJ-45 connectors, which are extended versions of the typical phone plug, with more connections.

[Table 8.1](ch08.html#twisted-pair_cables) lists some of the more commonly encountered forms of twisted-pair wiring, both UTP and STP, but it is not a complete listing. The various types of backbone UTP cabling used aren't listed. Many backbone UTP cables come assembled from combinations of 25 pair cables.

**Table 8.1. Twisted-Pair Cables**

| Category of Type | Maximum Data Rate | Wire Pairs | Application |
| --- | --- | --- | --- |
| CAT 1 (UTP) | < 1 Mbps | 2 | Analog data, POTS telephony, ISDN |
| Type 1 (STP) |  | 2 | Token Ring networks |
| CAT 2 (UTP) | 4 Mbps | 2 | Token Ring networks |
| Type 2 (STP) |  | 4 | Voice/Data |
| CAT 3 (UTP) | 16 Mbps | 4 | Voice/Data, 10BASE-T Ethernet, Telephony |
| CAT 4 (UTP) | 20 Mbps | 4 | Token Ring |
| CAT 5 (UTP) | 100 Mbps - 1 Gbps | 4 | 10BASE-T, 100BASE-T, Gigabit Ethernet, ATM, FDDI |
| CAT 5E (UTP) | 100 Mbps | 4 | ATM, FDDI |
| CAT 6 (UTP) | > 100 Mbps | 4 | Broadband |
| CAT 6e | 10 Gbps | 4 | Gigabit Ethernet |
| Type 6 (STP) |  | 2 | Token Ring |
| CAT 7 (UTP) | 1.2 Gbps | 4 | Gigabit Ethernet, VIA, high-speed interconnect, audio/visual |
| Type 8 (STP) |  | 2 | Data |
| Type 9 (STP) |  | 2 | Backbone |

The designation of "Types" for STP cable categories is based on older IBM standards for Token Ring networks. These STP cables connect to Multi-station Access Units (MAUs) with IBM data connectors, which are hermaphroditic (male and female) connectors that can be connected to one another with a locking clip. Unconnected token ring cables are a complete self-contained loop, to which is added one or two IBM data connectors and often an RJ-45 jack. STP Type cabling has largely been replaced on Token Ring networks by the more popular and cheaper UTP cabling.

## Coaxial cable

Coaxial cable is a packaging method for running cable that is very popular. It was the original cable used in Ethernet networks and is still used almost universally for television connections. Coaxial cable was introduced in 1929 and became the original long-distance cable that AT&T used as their network backbone before the introduction of fiber-optic cable in the 1980s.

The structure of a coaxial cable is shown in [Figure 8.4](ch08.html#a_cutaway_view_of_coaxial_cable). Every coaxial cable has a central copper wire that is surrounded by an insulator called the *dielectric*. In higher-cost coaxial cable, the copper wire may be coated with silver in order to improve the high-frequency transmission characteristics of the copper. Surrounding the dielectric is a wire braid or foil wrapping that serves to shield the copper wire from EMI and RFI interference. The outer shell of the coaxial cable is usually a plastic casing or plenum (Teflon or Kynar).

![A cutaway view of coaxial cable](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0804.png)

**Figure 8.4. A cutaway view of coaxial cable**

There are many different kinds of coaxial cable in use today, as described in [Table 8.2](ch08.html#coaxial_cables). They vary in terms of their thickness, their ability to carry current, their resistance, and the applications that they are used for. Alternative forms of coaxial cable include Twinaxial (Twinax), which bundles two coaxial cables in the same jacket, and Triaxial (Triax), which bundles three coaxial cables in the same jacket.

The use of coaxial cable for both Thin Ethernet (Thinnet) and Thick Ethernet (Thicknet) applications is very limited. The main use of coaxial cable is in audio/visual (AV) applications such as cable TV, CCTV cameras, and other high-bandwidth applications. Gradually, coaxial cable is being replaced by fiber-optic cable as fiber becomes cheaper.

**Table 8.2. Coaxial Cables**

| Coaxial Type | Core Diameter (mm) | Resistance((c), ohms) | Application |
| --- | --- | --- | --- |
| **RG-6** | 1.0 | 75 | Cable TV |
| **RG-8** | 2.17 | 50 | 10BASE-5 (Thicknet). This was the original cable used for Ethernet, and was replaced by twisted-pair wiring. |
| **RG-11** | 1.63 | 75 | Cable TV |
| **RG-58/U** | 0.9 | 50 | 10BASE-2 (Thinnet) |
| **RG-58 A/U** | 0.9 | 50 | Thinnet |
| **RG-58 C/U** | 0.9 | 50 | Thinnet |
| **RG-59** | 0.81 | 75 | Cable TV and ARCNET |
| **RG-62** | 6.4 | 93 | ARCNET and IBM 3270 mainframes (legacy systems) |

Transmission lines based on coaxial cable use a tube construction technique that bundles many coaxial cables along with wire pairs inside a protective sheath that is composed of paper wrapping, thermoplastic cement, and a polyethylene jacket. [Figure 8.5](ch08.html#coaxial_carrier_cable) shows a diagram of a coaxial cable transmission line. The last Transcontinental Cable System L-carrier standard, introduced in 1972, was L-5. That cable had 22 coax per cable, operated at 57 MHz, required repeaters every 2 miles, and carried 132,000 voice circuits per coax. *Coax* is the term used for the individual inner conductors.

## Ethernet wiring

Ethernet cabling uses a nomenclature to describe the different types of cable standards that exist. If you have wired a network with 100BASE-T network cable, each part of the name signifies a different property. The acronym BASE is short for baseband, which describes a signal within a frequency range that can be measured from zero to a maximum level. A system that uses frequency multiplexing can't be described in this way. Baseband is analogous to a low-pass system (a filter with a cutoff), and is the opposite of a pass-band system, where all frequencies in a range are allowed down the wire.

![Coaxial carrier cable](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0805.png)

**Figure 8.5. Coaxial carrier cable**

The "T" in BASE-T Ethernet means that it uses twisted-pair wiring. The commonly available Ethernet cables are comprised of four wire pairs ending in 8-pin connectors using RJ-45 connectors. This cable type supports any combination of sessions, from four full-duplex to up to eight half-duplex communication. Not all Ethernet runs on twisted-pair wiring. When the standard is designated as BASE-TX, it refers to Ethernet over twin axial cable. 10BASE-2 is a BASE-TX technology and uses BNC barrel-type connectors or T-connectors. Names such as 100BASE-T are used to define a particular Ethernet technology for which an IEEE standard exists. For example, 802.3 (14) is the standard that defines 10BASE-T, and 802.3 (24) is the standard that defies 100BASE-TX.

The CAT system defines a particular wiring type, whereas the standard defines the electrical signals traveling over the wires and the manner in which wires are connected. For example, CAT 5 cable is the current standard for high-speed Ethernet. To make a 100BASE-TX system, you would use a particular type of signaling, and CAT 5 copper wire cabling with two twisted pairs. At speeds beyond 1 Gbit/s, CAT 5E and CAT 6 are becoming more widely used. All Ethernet wire supports wire speeds from its maximum rating down to the slowest speed, 10BASE-T.

Twisted-pair CAT 5 Ethernet has the connections designated by the TIA/EIA (Telecommunications Industry Association and the Electronics Industry Alliance, two trade organizations) using the two standards listed in [Table 8.3](ch08.html#tia_solidus_eia_ethernet_wiring_codes). Notice that they differ only by exchanging the transmitting (Tx) and receiving (Rx) set of pairs.

Different Ethernet standards specify different line voltages. For 10BASE-T, the two Tx voltages are +/- 2.5 V, as is 100BASE-T. The three 100BASE-TX Tx voltages are +/- 1.0 V and 0 V.

Gigabit Ethernet or 1000BASE-T uses different signaling voltages, depending upon the implementation. For a Pulse Amplitude Modulation (PAM), the three voltages are +/- 2.0 V, +/- 1.0 V, and 0 V. In practice, you might find that the actual voltages are more like +/- 1.0 V, +/- 0.5 V, and 0 V. The wiring of the cable is matched within the host adapter and need not be standard.

**Table 8.3. TIA/EIA Ethernet Wiring Codes**

| Standard | Pin Count | Pair | Wire Polarity* | Color |
| --- | --- | --- | --- | --- |
| EIA/TIA (Electronic Industries Alliance/Telecommunications Industry Association); *Tip is a positive connection, and Ring is a negative connection. |  |  |  |  |
| 568-A | 1 | 3 | Tip | White/green stripe |
| 568-A | 2 | 3 | Ring | Green |
| 568-A | 3 | 2 | Tip | White/orange stripe |
| 568-A | 4 | 1 | Ring | Blue |
| 568-A | 5 | 1 | Tip | White/blue stripe |
| 568-A | 6 | 2 | Ring | Orange |
| 568-A | 7 | 4 | Tip | White/brown stripe |
| 568-A | 8 | 4 | Ring | Brown |
| 568-B | 1 | 2 | Tip | White/orange stripe |
| 568-B | 2 | 2 | Ring | Orange |
| 568-B | 3 | 3 | Tip | White/green stripe |
| 568-B | 4 | 1 | Ring | Blue |
| 568-B | 5 | 1 | Tip | White/blue stripe |
| 568-B | 6 | 3 | Ring | Green |
| 568-B | 7 | 4 | Tip | White/brown stripe |
| 568-B | 8 | 4 | Ring | Brown |

Standard connections are connected so that the pin numbers match through a connection; that is, Tx-Rx to Rx-Tx to Tx-Rx, also called a straight-through connection. Some cables are constructed so that the wires cross from end to end, and so that when the cables are connected, they connect Tx-Rx to Tx-Rx; this is commonly referred to as a crossover cable. For 10BASE-T and 100BASE-T, only two wire pairs are used; 1000BASE-T (GbE) uses all four pairs. A common scheme transmits signals from a node or computer on pins 1 and 2 and receives those signals on pins 3 and 6. When a node connects to a network device, the network device receives signals on pins 3 and 6 and transmits signals on pins 1 and 2.

### Tip

When you use a crossover cable in applications that require a straight-through connection, the cable will not work. To quickly differentiate a crossover cable from standard CAT 5 cables, adopt a convention that crossover cables are a particular color (I use red), or carefully label the cable at both ends with a permanent label or marking.

If you wanted a connection between two nodes or computers (or two network devices), then you would need to use a crossover cable as the connection. The one node would send signals on pins 1 and 2, and the other would send signals on pins 3 and 6. The first node would receive signals on pins 3 and 6, and the other node would receive signals on pins 1 and 2. Ethernet NICs can automatically detect the connection type used, and when a crossover is required, supply the necessary signal routing; only the older host adapters lacked this feature.

When connecting one hub or switch to another where a crossover cable is required, manufacturers implement a crossover connection internally as an Uplink or X-connection so that you can connect the two devices with a straight-through cable. You may need to push a button to enable the Uplink feature. Otherwise, if you connect two standard ports of different hubs together, you would need a crossover cable to allow the two hubs to communicate with one another. Many newer hubs and switches do away with Uplink ports and automatically detect the state of the connection, allowing a straight-through connection to function as a crossover cable, a feature referred to as *Auto-Uplink* or *Auto-MDI-X*. MDI refers to a Medium Dependent Interface, and the X means that it is an embedded crossover or internal crossover type. A Medium Dependent Interface is a port on a hub, router, or switch that can connect to another hub, router, or switch without the use of a crossover cable. The reason that this is required is that the standard port connection to an NIC has the outgoing signal from a device going to the input of the NIC and the output of the NIC going to the input of the switching device. MDI-X provides a means to reverse the transmit and receive signals on the wires.

[Figure 8.6](ch08.html#straight-through_and_crossover_connectio) summarizes the difference between straight-through and crossover connections with three examples. In the top example (straight-through connection), the signal from one NIC port travels over a straight-through cable to the connecting port or NIC through an uplink port connected to an MDI-X port, which performs the crossover. Some devices contain the crossover wiring internally in the device, as shown in the middle example (internal crossover). Finally, you can use a crossover cable to perform the signal swapping, which is shown in the bottom example (crossover cable link). A crossover cable looks like an ordinary Ethernet cable but has the wired connections transposed. Crossover cables are normally labeled as such on the cable's plenum (plastic jacket).

![Straight-through and crossover connections using MDI and MDI-X ports](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0806.png)

**Figure 8.6. Straight-through and crossover connections using MDI and MDI-X ports**

The earlier types of Ethernet used 10BASE-5 or Thicknet and 10BASE-2 or Thinnet. Thicknet was often used for ceiling runs, and was connected to a drop line using either an N connector or what is called a *vampire tap*. A vampire tap literally bites into the cable connecting to the inner core. [Figure 8.7](ch08.html#a_thicknet_ethernet_segment_and_drop_con) shows a common network segment for these Thinnet/Thicknet segments. These Ethernet connections required that the shielding be grounded on one end and that the cable be terminated on both ends. Transceivers were required at the endpoint of connections that weren't attached to the host controller. The connections were made with a 15-pin D-connector called an Attachment Unit Interface (AUI). Thicknet and Thinnet are more expensive to implement than twisted pair and slower, and so this type of Ethernet is largely of historical interest.

![A Thicknet Ethernet segment and drop connections](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0807.png)

**Figure 8.7. A Thicknet Ethernet segment and drop connections**

## Fiber-optic cable

Fiber-optic cable (sometimes called optical fiber) uses silica, glass, or plastic as its transport medium. AT&T was issued the first patent for optical signal transport in 1934, but practical devices didn't appear until the 1960s. By 1970, Corning Glass Works (now Corning Incorporated) had developed a patented process that dropped the attenuation of fiber-optic cable made from glass from more than 1000 dB/km to less than 20 dB/km. The early 1990s saw the development of much cheaper forms of fiber optics, based on plastic and plastic-clad silica (PCS).

Single-mode fiber is meant to carry a single signal, while multimode carries several different signals. Multimode fiber has a relatively short effective distance because of modal dispersion. Modal dispersion occurs in multimode fibers because the signal tends to spread out over time due to the propagation velocity of the optical signal being different for the different modes. Multimode fiber is used less frequently than single-mode fiber because of the modal dispersion problem.

An optical transmission system is composed of a light source, fiber-optic cable (or another transmission medium), and a detector. The light source must be able to emit a pulse, and when the signal is detected, that represents a 1 or ON condition. The absence of a signal is taken as a 0 or OFF condition. The faster the light can be turned on and off, the more data can be transmitted down the fiber. The two different types of light source that are used to "light a fiber" are light emitting diodes (LEDs) and semiconductor lasers. Light travels down the core from one end to another, reflecting off of the boundaries between layers of different refractive indexes.

### Note

When fiber-optic cable is laid down but isn't carrying a signal, it is called *dark fiber*. The massive amounts of dark fiber-optic submarine cable between the continents that was laid in the 1990s sparked a worldwide computer networking revolution.

Fiber-optic cable isn't affected by EMI or RFI, but is subject to an entirely different set of issues. Perhaps the most important issue with fiber-optic cable is that it is much more fragile than copper cable. Fiber is only glass or plastic, after all. Fiber cable networks can be much more difficult to stage, and they are also a lot more expensive than copper cables.

In the next sections that follow, the nature of data traveling as light through a fiber-optic medium is considered from a theoretical standpoint.

### Attenuation and dispersal

The particular type of material for a fiber-optic cable is chosen to allow a certain limited range of light wavelengths to pass through it with little loss of signal over the cable run. This diminishment of the signal is referred to as *attenuation*. Attenuation is the result of both scattering and absorption of the light. Light scattering is the effect of signal loss due to the deviation of some of the light from the intended path. Absorption of light occurs through the transfer of energy to the glass or impurities in the glass resulting in a lower signal strength as the light travels onward.

The attenuation of single-mode fiber-optic cable ranges between 0.25 and 0.5 dB/km. Attenuation is the ratio of transmitted power divided by received power, as shown in the following expression:

|  |
| --- |
| Attenuation (dB) = 10 log10 (transmitted power/received power) |

The attenuation of the optical signal going down the wire is determined by several factors. At a glass/air boundary, light is refracted or bent so that the signal is bounced internally back into the wire at an angle that is equal to, but opposite, the incident angle. The ratios of the refractive index of the core and clad determine the amount of bending that is allowed, as calculated by

|  |
| --- |
| Qc = arc cosine (n2/n1) |

where Qc is the critical angle as measured from the center line of the core, above which injected light will not travel down the fiber, n2 is the index of refraction of the cladding, and n1 is the index of refraction of the core. For typical values of n, this might work out to be around 8.5 degrees of angle, a very narrow beam.

You can modify the equation above to account for light entering the core from air by defining an external angle Qext and the refractive index of air, n0 (1.00029) as follows:

|  |
| --- |
| Qext = arc sin [(n1/n0) sin (Qc)] |

When air is taken into account, the critical angle expands to about 12.5 degrees.

At a certain angle of incidence above a critical value, essentially all of the light is trapped internally in the fiber. Below this angle, there is signal loss. [Figure 8.8](ch08.html#fiber-optic_light_refraction) illustrates the refraction effect using an LED as the light source that travels down the optical fiber. The core is the glass part, the cladding is a physical enclosure, usually plastic or some other material. The cone with the vertical lines represents the angles of light that can enter the wire and be reflected from the core/cladding interface down the length of the wire to the receiver. Light with a greater angle passes through the interface and is lost in the wire.

![Fiber-optic light refraction](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0808.png)

**Figure 8.8. Fiber-optic light refraction**

You can create fiber that filters for a small range of wavelengths by using very thin fiber. This is what single-mode fiber optic does. Light travels down the single-mode fiber as if the wire were a wave guide. With multimode fiber optics, there are many different light paths, each of which is defined by different angles of refraction or modes. The different modes travel down the fiber without interfering with one another.

As pulses of light travel down a fiber, they have a tendency to disperse or spread out over distance and interfere with other modes of light traveling down the same fiber. The amount of dispersion is a function of the wavelength and can be decreased by either slowing down the signaling rate or altering the shape of the pulse.

[Figure 8.8](ch08.html#fiber-optic_light_refraction) illustrates the case for multimode fiber transmission where the difference between the two indexes of refraction changes sharply over a short distance, called a *step index*. If the diameter of the core is smaller and closer to the wavelength of the light, then the light that is able to enter the core is at a very small angle indeed, and tends to travel down the core without refracting. Another technique creates a graded index of refraction that varies gradually from core to cladding. A graded multimode fiber allows a larger number of different angles of light down the core, creating a sharper output signal than a step multimode fiber optic. [Figure 8.9](ch08.html#single-mode_versus_multimode_transmissio) illustrates three different types of light transmission through different fiber-optic lines. In the top scenario a glass core with a very sharp transition or step index is characteristic of a single-mode step index. Light can travel down the glass fiber with little loss; however, this type of fiber only allows light that is highly calumniated to pass through it, which is what single mode means. The term *mode* refers to the different angles of light that can enter the core.

In the figure the wavelength range of the light is illustrated by the three identical parabolas or light pulses on the left. The triangular cone shown to its right illustrates the different angles or modes of light that can successfully pass through the fiber. At the right of the fiber is shown a profile of the index of refraction. The index of refraction is a measure of the ability of a medium to slow the speed of light relative to light traveling in a vacuum. Light is bent or refracted when it encounters materials of different optical density. When light is bent sufficiently it reflects and is transmitted down the fiber and emerges as the output pulse shown at the far right of the three figures. When light isn't sufficiently bent the light is lost from the fiber. The top index profile is of a single step function which reflects the light arriving within the cone shown to the left of the fiber. This single-mode fiber supports only straight-on angles where the light travels down the core without reflections. You need highly focused light sources such as lasers to work with this sort of fiber.

In the middle figure is light transmission through a multimode step index fiber. The index of refraction of the fiber supports a set of different modes and can reflect a broader range of input light angles, as illustrated by the wider cone of light entering the fiber. Unlike the output pulse shown for the single-mode figure at the top, which has an identical shape and some amplitude loss, the multimode output pulse is broadened and flattened out.

In the final scenario shown at the bottom of [Figure 8.9](ch08.html#single-mode_versus_multimode_transmissio), the fiber is a multimode fiber with a graded index. Unlike the two figures above it, which are step functions and reflect narrowly defined angles or modes of light, a grade index will reflect a range of modes and results in a cleaner output signal as shown on the right of the bottom figure. In this more complex scheme, the light is both dispersed and broadened, which is a disadvantage when trying to send signals down the fiber. Step function profiles are a better choice for long transmission lines.

![Single-mode versus multimode transmission](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0809.png)

**Figure 8.9. Single-mode versus multimode transmission**

**Solitons**

One shape that is related to the reciprocal of a hyperbolic cosine allows dispersion effects to cancel each other out in all directions. Pulses that have this shape are called solitons, and they have the property that they can travel vast distances (thousands of Km) without being degraded. Solitons or self-reinforcing solitary waves occur when two or more waves behave like particles and travel with constant shape and velocity.

In the figure, two waves of different amplitude and speed are approaching each other. (Waves with different wavelengths can travel through a medium with different speeds.) They merge, and the larger and faster wave (Wave 1) splits from the merged wave (Wave 1+2) with nearly the same size and shape that it had before it merged with the slower wave (Wave 2). John Scott-Russell observed this type of wave in a canal near Edinburgh in 1834, but it took 50 more years before the mathematical theory could be worked out. You see soliton-like behavior in the tidal bore on the Bay of Fundy. Solitons may also play a role in long-range neural electrical transmission in the nervous system, although this is still a controversial theory. Solitons have been created in optic fibers and studied, but the technology is not yet available and is under research.

![Solitons](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/U0801.png)

### Physical description

The core in fiber-optic cables is extruded with a width of either 50 or 62.5 (M (microns), which is the size of a human hair. The conductor is covered in a refractive coating with a lower index of refraction than the core. This refractive coating is called *cladding* and is added to all types of fiber-optic cable. The cladding keeps the light from escaping and reflects the light down the length of the fiber. The fiber and cladding together form a fiber that has a diameter of 125 (. Single-mode fiber has a core with a diameter of 9 (, and cladding is then added to bring the width of the spun fiber up to 125 (. You may see these different types of fiber specified as 50 (/125 (, 62.5 (/125 (, or 9 (/125 (. In any case, the fiber is surrounded by an insulator such as fiberglass, Kevlar, or steel, and then surrounded by a jacket (coating) made of plenum insulator. The combination of the core, cladding, and coating is collectively referred to as the *strand*. [Figure 8.10](ch08.html#fiber-optic_cable-007) shows a diagram of a fiber-optic cable.

![Fiber-optic cable](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0810.png)

**Figure 8.10. Fiber-optic cable**

Single-mode fiber has essentially unlimited bandwidth, while multimode fiber has a lower bandwidth. Both have excellent signal quality, but single mode's quality extends over much greater distances. The main attenuation factor in single-mode fiber is chromatic dispersion, while for multimode fiber it is modal dispersion. In chromatic dispersion, light is refracted based on its wavelength; the classic example of chromatic dispersion is white light passing through a prism to create a rainbow of colors. Modal dispersion is where the signal traveling down multimode fibers spreads out in time because the propagation velocity of different modes of light varies along the fiber length. Fiber optic is treated to vary the index of refraction across the diameter of the wire. Some processes create a gradual or graded index; others create a step index. Multimode uses both types of grading, while single-mode fiber uses a step index. As a rule, single-mode fiber optic is universally used, especially where Ethernet wiring is concerned. Multimode fiber optic finds occasional use in Ethernet, analog video, and communications over short distances.

Fiber-optic cable is combined in pairs for duplex communications and then bundled together with additional cables to create bundles of up to 96 strands of single-mode fiber placed inside a tube. Fiber-optic cables can be contained either as loose or tight strands inside a buffer tube. Tight buffer cable is used outside buildings and for longer cable runs because of the physical stability that form factor provides. Other uses for fiber cable include aerial, buried, duct, and submarine cables.

Unlike copper cabling, fiber-optic cable isn't affected by electric, magnetic, and radio frequency interference. Fiber-optic runs also have a much greater bandwidth and longer runs between repeaters than copper cable does. Light sources used are either light emitting diodes (LEDs) or, when longer length runs are required, lasers. The different methods used to modulate the light pulses are

- **Amplitude shift keying (ASK) or intensity modulation**. The output (amplitude) of the source is varied by a modulating signal. Intensity modulation is used with LEDs and in connection links in LANs.
- **Phase shift keying (PSK)**. This modulation technique is a digital modulation that changes the phase of a carrier wave using a pattern of binary bits.
- **Frequency shift keying (FSK)**. The FSK technique encodes digital information in the changing frequency of a carrier wave.
- **Polar modulation**. In polar modulation the carrier wave's polarity is modified and that variation encodes data.

[Table 8.4](ch08.html#led_versus_semiconductor_light_sources) compares LED to semiconductor laser-light sources as signal generators.

**Table 8.4. LED versus Semiconductor Light Sources**

| Property | Light Emitting Diode | Semiconductor Laser Diodes |
| --- | --- | --- |
| **Cost** | Cheap | Expensive |
| **Light source lifetime** | Long | Short |
| **Reliability** | High | Moderate |
| **Mode** | Multimode only | Single or multimode |
| **Power** | Moderate | High |
| **Linearity** | High (broader pulse) | Low (sharper pulse) |
| **Coupling efficiency** | Moderate | High |
| **Propagation distance** | Short | Long |
| **Signal rate** | Low | High |
| **Temperature sensitivity** | Small | Large |

A single-mode fiber cable is used for applications that don't require duplex operation. They can run as long as 3 km between repeaters. Long-distance fiber backbones that are pumped by lasers may only need to have repeaters placed every 100 km or 31.1 miles. Most LAN applications use LEDs, but backbones use lasers. Runs of several kilometers between repeaters are common on fiber-optic cable.

There are several different connector types used with single-mode fiber cables, including SMA screw-on (types 905 and 906), ST (straight tip), and SC (subscriber connector) connections. Many single-mode fiber cables are paired to create duplex communication. The SC connector usually has a square shape with a keyed tab size to ensure that a cable cannot be crossed with its other end during installation. Each proximity connection in a fiber-optic line results in about a 10 to 20 percent loss of signal strength, depending upon the nature of the fiber (glass, plastic, graded, or step). When you fuse two fibers together, the signal loss is much less, but the bond is permanent.

Fiber-optic cable is more expensive than copper cable, for the most part. However, it is widely used in high-speed Ethernet, SONET (optical Token Rings), Asynchronous Transfer Mode (ATM), 10BASE-F, and FDDI networks. The greater bandwidth, longer runs, resistance to EMI and RFI interference, and greater security make them desirable. The enhanced security arises out of how difficult it is to tap into a fiber-optic line. Fiber-optic cable can be tricky to work with. It is finicky, easy to break, hard to terminate, and must be protected using a pipe or conduit. You also need to be attentive to matching the particular fiber-optic cable type to the application for which you want to use it.

### Fiber-optic networks

Several network elements dictate the topologies that are allowed in fiber-optic networks. In addition to the wire elements of emitter, transmission medium, and receiver, the connections may require a repeater, or a T-junction as a tap to connect other media to.

T-junctions are either passive or active. A T-junction is a set of fused optical fibers that allow signals to be split or combined. A passive junction passes the signal through with some signal loss, while an active junction amplifies the signal before passing it on. A passive T-junction has two taps that are fused onto the main fiber-optic cable, with an attendant loss of signal strength.

Active T-junctions have an emitting laser diode or light emitting diode (LED) on one side and a photodiode receptor at the other end of the T-connection that leads off the network to a host or node. The straight-through portion of the T-connector is passive, as shown in [Figure 8.11](ch08.html#a_fiber-optic_t-junction). If any component of the active connection were to fail, then the host (network interface for a system) would go offline, but the network portion, which is passive, would remain operational. This makes fiber-optic networks very reliable.

![A fiber-optic T-junction](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0811.png)

**Figure 8.11. A fiber-optic T-junction**

Light traveling down fiber-optic cables can have a long effective run. However, every few kilometers, it is necessary to insert an active fiber-optic repeater to restore signal strength and quality. Early repeaters used optic-electrical conversion to capture the signal, and then used an emitter to retransmit the signal at the desired power. More recent devices are based on optical signal capture, do not perform a conversion, and thus can operate at much higher bandwidths than the older copper wire–based repeaters. A repeater has the same components as the T-junction shown in [Figure 8.11](ch08.html#a_fiber-optic_t-junction), but without the additional tap (connected fiber line) leading off to a host.

Most fiber-optic networks are built with ring topologies. SONET, which is described in [Chapter 13](ch13.html), is a prominent example. A break in the ring would remove one of the redundant connections but may not bring the network down. Many ring topologies are built with bidirectional links, making each link in the ring a self-contained loop. Unidirectional link topologies will fail when a single link fails.

In some instances, fiber-optic networks are built with a passive star topology, as shown in [Figure 8.12](ch08.html#a_passive_star_with_fiber-optic_connecti). The passive star is constructed using a central device that is a large silica cylinder, which is an optical hub. Incoming fiber-optic lines are connected in such a way that a portion of the light from each emitter can be seen by each of the receivers. The other outgoing end of the cylinder leads to fiber-optic cables going to the various emitters. Each optical network interface has a transducer to receive signals and an emitter to send signals over the network.

![A passive star with fiber-optic connections](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0812.png)

**Figure 8.12. A passive star with fiber-optic connections**

The passive star system allows different network segments and nodes to communicate directly with one another. The hub's construction allows light from any input to be transmitted to any output. The fan-out of a passive star is dependent upon the sensitivity of the photodiode receivers that the network uses.

# Wireless

Wires aren't the only medium that can be used for network communications. Signals can be sent through air, thin air, and even the vacuum of space. Somewhere out there in the cosmos, 57 light-years away, another advanced civilization is just tuning into the first episode of "I Love Lucy."

The following sections look at how the electromagnetic spectrum determines the characteristics of different network connections.

## Electromagnetic radiation

Frequency and wavelength are intimately related to one another by constraints imposed on radiation by the speed of light. In a vacuum, radiation travels at the speed of light such that

|  |
| --- |
| *c* = *¦*λ or λ = *f* / *c* |
| The relationship of energy to wavelength and thus to frequency is given by the following equations: |
| E = *h* λ or E = (*h c*) / λ |

where *¦* is frequency, λ is wavelength, *c* is the speed of light (3 × 108 m/sec), and *h* is Planck's constant (6.6 × 10–34 J/sec). In a vacuum, that speed translates into roughly 1 meter every 3 nanoseconds. Radiation travels through a vacuum unimpeded; however, when light travels through different media such as glass or water, the speed is reduced to around two-thirds and one-half of the speed of light, respectively. Electromagnetic waves traveling through conductors such as copper and fiber optics (also glass) are also slowed to about two-thirds the speed of light. Recent research has even shown that you can stop light inside the magnetic containment of a Bose-Einstein condensate, something that may one day be used to store information.

Current technologies use a portion of the electromagnetic spectrum for data communication — radio, microwaves, infrared, visible light, and ultraviolet radiation. The high-energy short wavelength X-rays and gamma rays are too energetic to be economically reasonable and practical. The low-energy long wavelength sub-radio frequencies are too slow to be useful as network connections as that would introduce too much latency into any connections. The International Telecommunications Union (ITU) categorizes the electromagnetic spectrum as divided into the ranges shown in [Table 8.5](ch08.html#frequency_ranges).

**Table 8.5. Frequency Ranges**

| Band | ITU Radio Frequency Class | Frequency | Wavelength | Energy (Power) |
| --- | --- | --- | --- | --- |
| Radio ranges Long Wave (LW; 153–279 kHz), Medium Wave (MW; 531–1620 kHz), and Short Wave (SW; 2310–25820 kHz) are not part of the ITU specifications. |  |  |  |  |
| γ (Gamma rays) | - | 30 EHz to 300 EHz | 10 pm to 1 pm | 124 keV to 1.24 MeV |
| HX (Hard X-rays) | - | 3 EHz to 30 EHz | 100 pm to 10 pm | 12.4 keV to 124 keV |
| SX (Soft X-rays) | - | 30 PHz to 3 EHz | 1 nm to 100 pm | 1.24 eV to 12.4 eV |
| EUV (Extreme Ultraviolet) | - | 3 PHz to 30 PHz | 100 nm to 10 nm | 12.4 eV |
| NUV (Near Ultraviolet) | - | 300 THz to 3 PHz | 1 μm to 100 nm | 1.24 eV to 12.4 eV |
| NIR (Near Infrared) | - | 30 THz to 300 THz | 10 μm to 1 μm | 124 meV |
| MIR (Mid Infrared) | - | 3 THz to 30 THz | 100 μm to 10 μm | 12.4 meV |
| FIR (Far Infrared) | - | 300 GHz to 3 THz | 1 mm to 100 μm | 1.24 meV |
| EHF | EHF (Extremely High Frequency) | 30 GHz to 300 GHz | 1 cm to 1 mm | 124 μeV |
| SHF | SHF (Super High Frequency) | 3 GHz to 30 GHz | 10 cm to 1 cm | 12.4 μeV |
| UHF | UHF (Ultra High Frequency) | 300 MHz to 3000 MHz | 1 m to 10 cm | 1.24 μeV |
| VHF | VHF (Very High Frequency) | 30 MHz to 300 MHz | 10 m to 1 m | 124 neV |
| HF | HF (High Frequency) | 3 MHz to 30 MHz | 100 m to 10 m | 12.4 neV |
| MF | MF (Medium Frequency) | 300 kHz to 3000 kHz | 1 km to 100 m | 1.24 neV |
| LF | LF (Low Frequency) | 30 kHz to 300 kHz | 10 km to 1 km | 124 peV |
| VLF | VLF (Very Low Frequency) | 3 kHz to 30 kHz | 100 km to 10 km | 12.4 peV |
| VF/ULF (Voice Frequency) | ULF (Ultra Low Frequency) | 300 Hz to 3000 Hz | 1,000 km to 100 km | 1.24 peV |
| SLF | SLF (Super Low Frequency) | 30 Hz to 300 Hz | 10,000 km to 1,000 km | 124 feV |
| ELF | ELF (Extremely Low Frequency) | 3 Hz to 30 Hz | 100,000 km to 10,000 km | 124 feV 12.4 feV |

In music, sound is broken up into ranges, based on the powers of two, called *octaves*. Octaves are a general concept that defines the range of frequencies in the electromagnetic spectrum divided by a power of two. With each 2x increase in frequency, power increases by a factor of 4 or +/- 6 dB/octave (decibels). An amplifier or electronic filter can be said to have a response of an octave if its power or voltage spans the same factor of 4 or +/- 6 dB. An alternative system divides frequencies using powers of ten, defining a range called a *decade*. The response of a factor of 10 or a decade would be +/- 20 dB/decade.

You can detect signals in the electromagnetic spectrum with a range of about 65 octaves (radio to gamma rays). It is theorized that 81 or more octaves exist, from the longest wavelength possible (the size of the universe, perhaps?) down to the Planck wavelength of 1.6 × 10–35 m, at which point the laws governing electromagnetic radiation break down, scale and time are presumed to be no longer measurable, and no information can be exchanged.

Electromagnetic radiation propagates as a periodic or oscillating wave in two coordinate axes, with the wave front moving outwards along the third axis in three dimensions. Consider [Figure 8.13](ch08.html#electromagnetic_radiation_and_wave_propa), where a point source (the happy sun) is emitting radiation. She is wearing sunglasses because the light being emitted is polarized in one direction (the XZ plane). So polarization simplifies [Figure 8.13](ch08.html#electromagnetic_radiation_and_wave_propa) by eliminating the other rotational angles of electric and magnetic fields.

![Electromagnetic radiation and wave propagation](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0813.png)

**Figure 8.13. Electromagnetic radiation and wave propagation**

There are several features to notice about this conceptual diagram. The wave is composed of equal amplitude electric and magnetic field vectors that are in phase with one another. Those vectors are displayed in the upper-right coordinates. Electromagnetic radiation obeys what is called the right hand rule. If you examine the right hand in the upper-left corner of [Figure 8.13](ch08.html#electromagnetic_radiation_and_wave_propa), the thumb points along the direction of motion (V pointed along the X-axis), the index finger points along the direction of electric current (E pointed along the Z-axis), and the middle finger points along the direction of the magnetic field or flux (B pointed along the Y-axis). The three axes indicate motion, magnetic field, and electric field. When polarized, the light travels down the X-axis, the electric field is the oscillation in amplitude in the Z-axis direction, and the magnetic field is along the Y-axis. The right hand rule shows which direction is positive by the way the fingers point. It is useful to keep these ideas in mind as you consider how different emitters and receivers can interpret signals sent over wireless media.

## Information and transmission

The electromagnetic spectrum is used to transmit information wirelessly by modulating or changing the waves in some manner. The three most important methods used are

- **Pulse modulation (PM)**. PM creates signals by simply turning the light source on and off. When the light is on, it is a logical 1, and when the light is off, it is a logical 0.
- **Amplitude modulation (AM)**. AM creates signals by using a change in the amplitude of the wave as its signal. When the amplitude is above a certain threshold value, it is a logical 1, and when it is below that value, it is a logical 0. Usually, AM uses a carrier wave and then adds the signal onto the carrier wave.
- **Frequency modulation (FM)**. FM creates signals by alternating the frequency of the wave. When the frequency is above a certain threshold value, it is a logical 1, and when it is below that value, it is a logical 0. FM also uses a carrier wave and then adds the signal onto the carrier wave.

[Figure 8.14](ch08.html#three_different_modulation_techniques_fo) shows these three different methods for signaling transmission. In the top signal, the carrier wave is modified by a phase modulation technique. The carrier wave is turned on for a 1 and off for a 0. When the wave switches from 0 to 1, the waveform has a different phase than it had before. Information is carried by the changes in the phase of the signal. Phase modulation is less commonly used than frequency modulation or amplitude modulation.

Shown in the middle signal in [Figure 8.14](ch08.html#three_different_modulation_techniques_fo), frequency modulation alters the frequency of the carrier wave depending upon whether the signal is on or off. For an on signal, a higher frequency is used, and for an off signal, a lower frequency is used. The changes in frequency encode information.

Perhaps the easiest modulation to visualize is amplitude modulation, shown in the bottom signal. The waveform's amplitude is above a threshold value when an on state is being communicated and below when an off state is sent.

![Three different modulation techniques for carrying a signal over a wireless link](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/0814.png)

**Figure 8.14. Three different modulation techniques for carrying a signal over a wireless link**

The relationship between the frequency of an electromagnetic wave and the amount of data a wave can carry is a fundamental limit imposed on all systems by signal theory. To get a sense of the absolute limit for signals, the relationship between frequency, wavelength, and the speed of light can be solved for frequency and then differentiated with respect to wavelength to get the formula shown here:

|  |
| --- |
| (*f*/*d*λ) = (*c*/λ2) |

### Note

The relationship of frequency modulation and amplitude modulation to multiplexing signals traveling over a wire is described in [Chapter 5](ch05.html).

Because signals are carried by the overall change in the waveform (amplitude or frequency, for example), you are really only interested in how often this equation changes sign. Put another way, you are interested in the number of times per second that the slope of the curve (the differential) changes sign. The equation can be rewritten as a set of finite differences, which provides absolute values, as follows:

|  |
| --- |
| Δ*f* = (*c* Δλ) /λ2 |

Now consider a wireless radio emitter that provides a signal centered at the 2.4 GHz frequency that is ten 64 Kbits/s DS0 channels wide (five on each size). The band would go from 2.08 to 2.72 GHz. The calculated wavelength for the 2.4 GHz band would be 0.125 m, the difference in wavelength would be 10 units of 64 Kbits/s, or 640 Kbits/s, and the calculation would yield 33.3 Mbits/s. If a wider bandwidth is used, say perhaps 1.28 Mbits/s, then the data rate would be 64.6 Mbits/s. It is usual to have a very low ratio of **Δ***f*/*f*, and in these two cases, the ratios would be 1.4 percent and 2.8 percent, respectively.

## Wireless connections

There are some general factors that influence a wireless connection. Regardless of the frequency or wavelengths used, a wireless data connection still requires three components:

- Transmitter
- Transport medium
- Receiver

Nearly all of the computer network links use air or vacuum as the transport medium. The transmitter and receiver must be reasonably constructed and priced in order to be used. The transmitter used delivers some electromagnetic radiation at some frequency and power. Power correlates with the wave amplitude, which must be large enough for the type of receiver used to detect the signal at the distance required by the connection. Let's consider an example, involving radio transmission.

### Radio links

Radio transmission covers a very large range of frequencies, as you can determine from [Table 8.5](ch08.html#frequency_ranges). According to SETI, the following radio astronomy bands are recognized as significant and observed: 3.36-13.41, 25.55-25.67, 73.00-74.60, 150.05-153.00, 406.10-410.00, and 1400.0-1427.0 MHz. The range of 73, 150, and 406 MHz are active for pulsar signals, and the 1400 MHz band is where hydrogen lines fall. That means that radio astronomy is "connecting" using very powerful, extremely distant transmitters, and extremely large antennas and arrays, some on the order of a kilometer in size. The ITU categories for these bands fall in the HF, VHF, and UHF ranges, with wavelengths between 100 m and 50 cm.

Even with the enormously large scale of both the emitter and detector, the vast distance that these radio waves take to make the trip makes the signal vanishingly small. To get a sense of how small the power of these radio waves can be, consider this fact: The total amount of energy collected by all of the radio telescopes since the beginning of radio astronomy is estimated to be less than the energy that is needed to power a flashlight bulb for less than a millionth of a second. That correlates to a heat source emitting these radio waves as its maximum having a temperature of just a few degrees above absolute zero; not much higher than the cosmic background radiation.

Let's scale this radio connection down a bit. AM radio operates between 520 and 1620 KHz, and in the U.S., the highest power allowed is a 50,000-watt transmitter. These radio wave broadcasts can be received by radios approximately 100 miles away during daytime and can penetrate buildings to a certain degree. At night, AM radio waves can be made to reflect off of the ionosphere 100 to 500 km up in the earth's atmosphere; then the signal can be received hundreds of miles away, depending upon conditions.

Radio transmitted omni-directionally loses power as a function of 1/r3, where r is the radius of the sphere created by the point source.

Radio transmitters can be built to operate at higher frequencies, shorter wavelengths, and more power. The 2.4 GHz Wi-Fi with a wavelength of 12.5 cm (about 5 inches) is powerful enough to penetrate walls. Typical devices may have enough power to be received by another Wi-Fi device 150 to 300 feet away. If you focus the radio transmitter and the receiver so that they are highly directional and focused in one direction, then radio links can be extended to a kilometer. However, focusing the beam and the distance involved reduces the strength of the signal to the point that even intervening tree foliage is enough to interfere with the signal. To get more directional signals requires a more powerful transmission.

### Microwave links

Microwave radiation is used to transmit data over long distances because it provides good bandwidth over line-of-sight transmission links. Microwave communication is used for backbone links in cellular networks, as radio relay links for TV and telephony, and as satellite links, and provides a relatively low-cost method for installing high-bandwidth connections.

At a frequency of around 200 MHz, the wavelength of the microwave is under 2 m, allowing a focusing transmitter to narrow the transmission very effectively and a dish antenna to very effectively collect the signal. The line-of-sight requirement means that a transmitter atop a 30-story building would need a repeater about 100 km away.

### Tip

You can calculate microwave line-of-sight links using a Google Maps Microwave Link Planning Tool. Go to `http://members.chello.at/stephen.joung/indexDistanceElevation.html` and enter the coordinate. With this data in hand, you can set the characteristics of the microwave link at `http://members.chello.at/stephen.joung/indexMW_Distance20.html`, and you see how antenna size, frequency, and power affect performance.

Microwaves are far less effective in penetrating buildings than radio waves because the shorter wavelengths increase the interactions of microwaves with solid material. That's why microwave ovens are effective, but radio frequency ovens are not. RF ovens would require a much higher intensity to heat materials.

As the distance of the microwave link increases, the beam diverges and may be refracted by atmospheric layers. When the signal arrives, the receiver may experience what is called multipath fading, slowly moving in and out of tune. You can experience the same effect in radio transmissions.

If you are in your car listening to a weak radio station and you pull to a stop, you may notice that the strength of the signal can be changed dramatically by moving a few feet forward or backward. That is the result of multipath fading.

In the U.S., the following frequencies have been dedicated to wireless communication:

- 1.7 MHz (AM)
- 27 MHz (FM)
- 43 to 50 MHz (FM)
- 902 to 928 MHz (worldwide open use, cell phones and Wi-Fi)
- 1920 to 1930 MHz (worldwide open use, cell phones)
- 2.4 GHz (worldwide open use, cell phones and Wi-Fi)
- 5.8 GHz (worldwide open use, cell phones and Wi-Fi)

The band between 2.4 and 2.484 GHz is dedicated worldwide for open use. This band, sometimes referred to as the Industrial Scientific Medical band, is where devices such as cell phones and Wi-Fi operate without government licensing. Cell phones operating at 900 MHz and at 2.4 GHz with 100 MW power transmission have a range of about 30 m (100 ft).

# Summary

This chapter covered the different wiring standards that you can use to create a network. Twisted-pair and coaxial cable wiring were highlighted, and their application to Ethernet networks was explored.

Fiber optics offers a high-bandwidth network connection. Light from a laser or LED is sent down a glass or plastic fiber, over either a single-mode or multimode link. The principles of light transmission were described.

Wireless communications can transmit radio and microwave frequency radiation across either air or a vacuum. The properties of the electromagnetic spectrum and how it is used to convey information were illustrated.

The next chapter describes how networks intelligently connect devices with one another.
