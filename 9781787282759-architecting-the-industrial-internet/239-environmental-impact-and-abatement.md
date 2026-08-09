# Environmental impact and abatement

Many companies pursuing Industrial Internet applications face environmental impact and abatement challenges. These can include companies involved in agribusiness, alternative energy and environmental control, construction, logistics and transportation, manufacturing and GPGs, oil and gas, pharmaceuticals, medical equipment and healthcare, and utility companies. In fact, an IIoT project is often considered is specifically to address these challenges.

In this section, we will describe IIoT for noise detection and abatement. Though we return to an aviation example, the architecture has wide applicability in all the industries just mentioned.

The three airports in the San Francisco Bay Area handle a large amount of air traffic. Airplanes arriving, taxiing, departing, and circling generate a lot of noise that can adversely impact residents near airports and under flight patterns. The following diagram captures the typical flight patterns in a 24-hour period in the Bay Area ([https://speier.house.gov/sites/speier.house.gov/files/documents/NoCal-Initiative-Phase-One-Report.pdf](https://speier.house.gov/sites/speier.house.gov/files/documents/NoCal-Initiative-Phase-One-Report.pdf)):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/0a450b4f-9b1e-4d0a-969c-260f49ebc6e0.png)

The Federal Aviation Authority (FAA) has an initiative to address noise concerns in Santa Cruz, Santa Clara, San Mateo, and San Francisco counties. This is a multi-phase approach, including review and response to community proposals, and explores such areas as flight procedure criteria and the overall fly ability of proposed **Performance Based Navigation** (**PBN**) procedures. Procedural modifications such as speed and altitude adjustments, airspace changes, rerouting over water, altered braking patterns on the runway, and increased night time operations are considered.

Airport authorities must ensure that they meet or exceed all Federal and State aircraft noise regulations and that flights operate as quietly as possible. If residents complain about noise, the airport must pay for noise reduction in those buildings.

The main source of noise pollution is the landing approach of the aircraft to the runway and the engines. Often the engine keeps running after the aircraft is already at the gate. This leads to unnecessary noise pollution. The **San Francisco airport** (**SFO**) is addressing this noise problem by implementing an IIoT solution involving noise sensors that gather data, and reporting and analytics solutions for analysis of the data. The goal is to create a safer and quieter airport environment that operates with a cleaner emissions footprint to benefit both the airline passengers and other nearby community stakeholders.

Noise sensors help pinpoint which aircraft have engines and **Auxiliary Power Units** (**APUs**) still running when they are not required to. SFO will monitor APU usage by aircraft at each of its gates. The data collected from noise sensors is monitored in real-time events and is also used in historical analysis.

Technical requirements of the solution include the following ones:

- Monitoring APU noise-detection levels per aircraft in alignment with SFO noise policies
- Visualization of noise levels per aircraft in real time
- The ability to sense, detect, store, and transfer noise data digitally and with low latency
- Accurate detection of acoustic data for individual aircraft within a specified area (apron, gate, parking location) without distortion and negative effects from other sound sources such as adjacent aircraft, runways, and airfield vehicles
- Seamless integration of the solution with SFO's technology systems, both physically and logically

The simplified solution architecture will consist of these three tiers:

- **Edge tier**: This tier includes IIoT sensors for capturing the noise level at various locations
- **Platform tier**: Noise data will be stored in the data store in the platform tier and analytics will help locate the precise location of the aircraft (the main challenge being the isolation of the source of noise when there may be several aircraft in the line of sight)
- **Enterprise tier**: This tier will combine IIoT data with enterprise systems from the airport and provide the end user with decision support reports

A potential sample of the reporting solution might be as follows:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/fd7af242-0b48-45da-8821-adaa53c42a6a.png)
