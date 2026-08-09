# Factory operation visibility and intelligence

Visualizing factory operations data is a challenge for many manufacturers today. One of the IIoT initiatives some manufacturers are pursuing today is providing real-time visibility in factory operations and the health of machines. The goal is to improve manufacturing efficiency. The challenge is in combining and correlating diverse data sources that greatly vary in nature, origin, and life cycle.

Fujitsu has conceptualized a **Factory Operations Visibility and Intelligence** (**FOV**I) solution based on experiences they gained from two of their factories:

- A factory in Shimane where notebooks are manufactured
- A factory in Yamanashi where network appliances are manufactured

Fujitsu's goals for the FOVI project are as follows:

- Timely product manufacturing and shipment
- Quality improvements and reduced rejection rates
- Reduced time for equipment repair
- Overall higher throughput in factory

FOVI's backend is to be deployed to Fujitsu's public cloud. BLE Beacons are to be used to locate and track products in the repair area in the Shimane factory. Video archives of operations will be generated and correlated with data from sensors. Factory personnel are traced using passive RFID. The architecture is designed to support simulations.

The following diagram provides a functional view of Fujitsu's FOVI architecture ([http://www.iiconsortium.org/images/test-beds/Figure-en.jpg](http://www.iiconsortium.org/images/test-beds/Figure-en.jpg)):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/1ef0453c-e87e-4f1e-b8e1-5e756a882d32.jpg)

Hershey's, a manufacturer of candies, has already deployed a similar architecture. Temperature data is gathered from sensors in extruders on the plant floor and transmitted to the Microsoft Azure cloud where machine learning algorithms are applied. Adjustments to temperature are made in near real time to optimize the production process, improving quality and yield.
