# Edge connectivity

The following figure explains the different communication technologies that can be used for the edge tier. The *X* axis is the distance over which the devices need to connect with each other. It could be the sensor or a collection of sensors connecting to the gateway device, such as several temperature sensors in the factory environment connecting to the gateway device. The possible options here are as follows:

- **Wired**: Use of RS-232, commonly called the **serial port**, is one option to connect the sensor pack to the gateway device via a wired connection. This is good for distances in the range of 15 m or 50 ft. To extend this range up to 300 m or 1,000 ft, low-capacitance cables could be used in some cases. RS-485 can be used for distances up to 1,200 m or higher data rates over shorter distances.
- **Wireless**: The sensors could communicate wirelessly to the gateway device using Bluetooth or Wi-Fi. Depending on the power level or class, Bluetooth could be used in the 1-100 m range. Wi-Fi, using protocols such as 802.11a, 802.11b, 802.11g, or 802.11n, would operate typically in the 2.4 GHz to 5 GHz range. The coverage is in the range 50 to 100 m, but provides higher data rates over Bluetooth. Image or video sensing may need higher data rates compared to temperature or pressure sensing:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/d5ac87c9-7848-479d-bee1-245eb5f4036e.png)

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/d7a1bafb-7a6d-4a69-8d8c-dc3ebb0b9187.png)

Figure 7.9: Edge communication and connectivityFor Industrial Internet scenarios where the asset is mobile, connectivity technologies from the two boxes on the right are useful, as explained here:

- **Cellular**: Cellular technologies such as 3G and 4G are commonly used, and 5G is being introduced. These services are provided by telecom companies such as AT&T, Verizon, or Vodafone. Typically, the SIM (Subscriber Identity Module) card can be used in the device to provide the connectivity to the cloud, for IoT data. NB-IoT is a low-power technology for Wide Area Network (WAN) and enables a wide range of IoT devices to be connected using cellular telecommunications bands. This is meant for lower cost and for relatively lower bandwidth needs compared to the 4G or 5G technology. Likewise, LTE-M can be a lower-cost, lower-power (longer battery life), and lower-data-rate (about 100 kbits/s) option for connectivity.
- **LPWAN / LoRa / SIGFOX**: These are some of the technologies best suited for longer battery life and connectivity at lower cost but for distances much larger than typically covered by wired or wireless (Wi-Fi or Bluetooth). Some of these standards are still evolving, but greenfield Industrial Internet solutions should look at these technologies for connectivity.
