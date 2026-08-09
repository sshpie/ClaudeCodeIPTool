# The control domain

The control domain denotes the functions taking place in edge devices that serve as industrial controls. These functions include reading data from sensors in the devices, applying rules and logic to create fine-grained closed-loop processing, and providing control over the physical system through actuators. The devices might be networked together or highly distributed and are most often distant from a centralized data store containing historical data gathered from the devices. In the Industrial Internet, they are connected via a network connection back to this central data gathering point.

The following diagram pictures devices in the *field* (in manufacturing plants, distribution centers, or on transit vehicles in our supply chain example), cloud-based data processing components, and business **on-line transaction processing** (**OLTP**) systems and tools. The typical primary components in the control domain are in the shaded area:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/17d978f8-3053-4ff5-85dd-0317881ecef8.png)

As described in [Chapter 2](b0c77de8-768e-4317-83bd-c682a6f4aac0.xhtml), *Architectural Approaches for Success*, the IIC describes the essential functions in this domain as follows:

- Asset management
- Sensing
- Actuation
- Communication
- Entity abstraction
- Modeling

Asset management, sensing, actuation, and communication are basic functions that must occur in the edge device for it to be useful. Entity abstraction and modeling might take place in the edge device or in the backend infrastructure (depending on how *smart* the device is).

Understanding network requirements and careful planning here is needed to assure success. You would want to consider network reliability, message latency, and whether a persistent connection is required as you define the architecture for this domain. A benefit of deploying smarter devices is that they can operate on their own for periods of time even if the network to the backend infrastructure fails. Of course, smarter devices tend to cost more since they are providing computational engines and support additional functions.

SCADA applications

 The capabilities provided by applications in the control domain are sometimes referred to as SCADA or Supervisory Control and Data Acquisition applications. SCADA applications include the processes, systems, or machinery you want to monitor and control, the networking, and the network of smart devices and their interfaces that are provided.
