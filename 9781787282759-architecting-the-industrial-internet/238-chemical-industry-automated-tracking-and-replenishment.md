# Chemical industry automated tracking and replenishment

Next, we'll look at applying IIoT to the tracking and replenishment of industrial gas containers.

Replenishment of industrial gas containers or cylinders requires many manual steps. Often, cylinders are moved using manually operated transporters. People sort and clean the cylinders, attach them to the appropriate hoses, ,and fill the cylinders with the right amount of gas. These manual steps result in operational inefficiencies and are prone to human error.

The chemical industry uses an **air separation unit** (**ASU**) to separate atmospheric air into its primary components, typically nitrogen and oxygen, and sometimes also helium, argon, and other rare inert gases. After the gases are separated, they are supplied either by gas pipelines or cylinders. The composition of air is shown in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/a5b41995-484f-4cce-9ed2-8a8a8323963b.png)

A unique characteristic of this industry is that the raw material is air, obtained freely from the atmosphere. Most of the complexity is in the plant equipment and the replenishment and distribution of the cylinders. Air Separation by Cryogenic Distillation is illustrated in the following diagram ([http://www.chemicalprocessing.com/articles/2011/digital-positioner-aids-air-separation/](http://www.chemicalprocessing.com/articles/2011/digital-positioner-aids-air-separation/)):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/0aa54b33-2fd4-499e-8e01-6fff65962a9c.jpg)

At a simplistic level, the manual steps in the process of filling and refilling the cylinders are as follows:

- Cylinders are transported to the plant by truck
- Sorting and cleaning of the cylinders occurs
- Cylinders are moved to the filling station
- The cylinder is connected to the right hose for filling
- The hose is disconnected
- Measurement, testing, and labeling of the cylinder occur
- The cylinder is dispatched based on an order

In our future state, optimizing operations leverages IIoT with the help of RFID-based asset tracking and use of robots. The following simplified steps take place:

- Cylinders are transported to the plant by truck, and cylinders are identified by RFID-based asset tracking
- Automated fork-lifts move the cylinders to the cleaning station during the sorting and cleaning operation
- Automated fork-lifts move cylinders to the filling station
- Data from the PLC drives the robotic actions to connect the cylinder to the right hose for filling
- Data from the PLC drives the robotic actions to disconnect the hose
- Digital gauges record a reading during the measurement, testing, and labeling phases
- An automated fork-lift moves the cylinder when an order is received for its dispatch

The high-level architecture of the robotic solution is shown here:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/f8272c85-4552-4a9a-ac8d-b52851332df4.jpg)

As you can readily tell, we've eliminated much of the potential human error that can occur during the sorting, cleaning, refilling, and transport of the cylinders using this approach ([https://www.researchgate.net/figure/268209377_fig4_Figure-4-Vehicle-Level-Health-Reasoner-Overview-Diagram-with-information-exchange-data](https://www.researchgate.net/figure/268209377_fig4_Figure-4-Vehicle-Level-Health-Reasoner-Overview-Diagram-with-information-exchange-data)).
