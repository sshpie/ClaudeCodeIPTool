# Baggage and cargo handling

Travelers can readily relate to problems caused by missing baggage or baggage that arrives late at a destination. According to The Baggage Report by SITA (2017), about 22 million bags were mishandled in 2016 globally. This translates to about six mishandled bags per 1,000 bags checked in. Mishandled bags generally fall into one of three categories:

- Delayed (77 percent)
- Damaged (16 percent)
- Lost (7 percent)

The **International Air Transport Association** (**IATA**), a trade association of the major airlines, announced IATA Resolution 753 that will come into effect in June 2018. It promises to deliver major improvements in airline baggage services over and above the incremental improvement seen in recent years, with the goal of improving customer satisfaction. IATA Resolution 753 is an example of GRC at an industry vertical level. An IIC Testbed called **Smart Airline Baggage Management Testbed** ([http://www.iiconsortium.org/baggage-management.htm](http://www.iiconsortium.org/baggage-management.htm)) is creating an Industrial Internet solution to help airlines achieve compliance with this resolution.

The following airline baggage flow visual shows the typical flow of airline baggage from the arrival at the airport to the destination:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/b51c4f02-7f7b-40e8-889d-99274e469c91.png)

The passenger drops the bag at the drop-off location. The bag tag is printed either at the self-service kiosk or by the airline staff. The following figure is a typical baggage tag with a bar code indicating the flight details and the airline passenger (PAX) information as well as a readable portion:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/1b5f8511-2ad5-465d-9de4-b25684f69e32.png)

The bags are transported via baggage belts and carts to the aircraft. The following baggage transfer should look familiar to anyone who has flown an airline:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/3e2c6b8f-f1d3-4c70-a28c-8b37cf561ca5.jpg)

The passenger journey may consist of a direct flight or connections. Accordingly, the bags are routed to the next aircraft at the transfer point. Today, the bags are constrained to travel no faster and no slower than the airline passenger, as most countries do not allow accompanied bags to fly in-flight. In other words, since bags must fly in the same flight as the passenger, bags cannot move faster than the passenger and make a tight connection, so the passenger misses it. Likewise, baggage cannot move too slowly or else the flight must wait for the bag to be loaded. As a net result of this, over 10 million bags were mishandled at the transfer point in 2016.

The typical points for mishandling baggage are as follows:

- **Tagging errors**: The airline bag tag is placed incorrectly, swapped between the bags of different passengers, or not pasted properly and falls off (a more common occurrence at self-service bag drop kiosks)
- **Security checks**: When a checked-in bag is flagged for additional security screening, it might get delayed and not make it in time for its designated flight
- **Failure to load**: The bag might not make it to the correct aircraft in time, go to the wrong aircraft, or fall off the baggage belt or cart and not be detected in time
- **Transfer issues**: Failure to route baggage to the right handlers and carts in time
- **Weather issues**: Inclement weather conditions may cause a reduction in cargo weight and lead to bags not being loaded on designated flights
- **Arrival issues**: At the arrival airport, the bag may not get unloaded from a flight that has a stopover at the passenger's final destination or the bag might get routed to the wrong bag carousel
- **Theft**: On rare occasions, there could be theft of the bag or other security breaches

Today, the use of printed bag tags with the bar code is prone to reading errors due to line-of-sight scanning. We refer to it as 2D scanning, and multiple scanners are used on the baggage belt. The currently used airline baggage tag has printed bar codes. These bar codes can be scanned in the line-of-sight only. Mainly two types of scanners are used:

- **Hand-held scanner**: This is often used by the airline staff or ground handling crew while transferring the bag from the cart to the aircraft and vice versa.
- **In-line arrays**: These are built into the baggage conveyor system and use a 360-degree array of lasers to read the bar code tags from multiple angles. It tries to account for any shift in the baggage and the orientation as the bag travels through the conveyor belt system.

The airlines paste a few bar code stickers on different sides of the bag to increase the scan changes. These are printed at points where the bags change hands or at kiosks in the airport.

Though the previously mentioned baggage-mishandling issues might seem unique, most (if not all) of the conditions could impact cargo handling by air carriers and other transportation carriers such as trucks and trains. To solve these sorts of issues, **Radio-Frequency Identification** (**RFID**) tags have been used for many years on cargo shipping containers. As RFID tags became cheaper over the years, they have appeared on much smaller shipping containers and pallets.

The use of RFID tag can improve the read efficiency as it becomes 3D scanning. The RFID readers are not limited by line of sight. The use of active or passive RFID as a bag tag essentially makes it an IoT end point.

The Smart Airline Baggage Management solution uses connected bags using RFID tags, connected readers, and other connected fixed and mobile assets for ground handling at the airports. This near real-time tracking of bags will help save the air transport industry about $3 billion. Once the airlines implement this solution, they will be able to do the following:

- Demonstrate delivery of baggage when custody changes
- Demonstrate acquisition of baggage when custody changes
- Provide an inventory of bags upon departure of a flight
- Exchange information about these events with other airlines as needed (data sharing by use of Baggage **eXtensible Mark-up Language** (**XML**)).

What is a Baggage XML?

 It is a new messaging standard that is being developed by IATA using XML, based on established best practices. It will allow future developments at a reasonable cost using technology that is almost universally adopted in other industries. The Baggage XML project is striving for a sustainable standard for messaging related to airline baggage.The high-level architecture of the solution is illustrated in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/b5e18c9b-7859-422c-b356-05ebb14a6c26.jpg)

In this solution, the RFID tags contain information that is traditionally stored in the printed barcode tag. RFID tags can be active or passive, which will determine the range and storage capability. The data from RFID tags is read via the connected reading devices. It is then sent to the IoT Cloud Platform via a secured connection. The sensor data is stored in a time series data store. The enterprise data elements from the different airline systems are stored in an airline data model (the Oracle Cloud component pictured). The integrations between the two systems provide the necessary data for real-time scenarios and batch mode analytics scenarios.

The real-time scenarios help track the bag in near real time and react to exceptions, such as the bag falling of the conveyor belt and not getting scanned at the next point in the expected range of time. The batch mode can be used to help figure out which kinds of bag exception are occurring at a site and then come up with mitigation strategies.
