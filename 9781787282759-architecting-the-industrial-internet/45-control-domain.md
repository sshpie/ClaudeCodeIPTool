# Control domain

The control domain consists of functions performed by industrial control systems and are typically performed in closed loops, for example, constantly reading temperature and pressure and opening a valve when they exceed a defined limit. *Figure 2.5,* *Control domain functions*, represents a typical control domain; however, the specific functions may vary depending on the industry and system.

The control domain typically consists of sensing functions and actuation. The sensing function reads data from sensors and may span hardware, firmware, device drivers, and software elements. The actuation function writes data and controls signals to an actuator to perform an actuation.

The third important function in the control domain is communication between the sensors, actuators, controllers, gateways, and other edge systems. Latency, bandwidth, jitters, reliability, and resilience can interrupt or delay communication and decrease **Quality of Service** (**QoS**), and must be considered in the architecture design, especially in critical systems. It may be appropriate to use APIs to expose a set of connectivity services, which may include additional connectivity features, such as auto-discovery.

Entity abstraction defines a virtual representation of the sensors, actuators, controllers, and respective higher level systems, and models the relationship between them, as well as providing a context from which to interpret and understand sensor data.

Modelling attempts to interpret and correlate data gathered from sensors, peer systems, and controlling systems into states, conditions, and behaviors. Models may simply interpret sensor readings, such as a time series of temperature readings, or may be complex artificial intelligence models. Models involved in local control systems are referred to as edge analytics, and are usually used in real-time applications when decisions must be made rapidly in local control systems and where it is impractical or expensive to send raw sensor data to a central processor for processing. Other functions may be employed to prepare data for analysis, including filtering, cleansing, transforming, and persisting.

Operations management of control systems is enabled by the asset management function. Asset management includes configuration, policy enforcement, system controls, and other life cycle operations.

An executor carries out control logic according to control objectives. This may be a sequence of actions applied through actuation and may involve interactions with peer or higher-level systems. Control logic may be straightforward, as in simple set-point algorithms to adjust room temperature, or they may be sophisticated, employing advanced cognitive and learning capabilities:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/f0876266-2c32-48e0-ade9-53a6a02e4c31.png)

Figure 2.5: Control domain functions
