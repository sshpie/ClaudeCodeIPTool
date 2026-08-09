# Device considerations

When customized devices and sensors must be considered to provide the necessary metrics, the design phase assumes even more importance in minimizing the possibility of future security breaches. The hardware should be scoped to minimum requirements at access points such as I/O ports and should be made tamper proof. Secure software upgrade procedures for firmware and applications must also be planned.

In many situations, you will be faced with defining security measures around predefined devices that lack the features needed to put into place adequate security measures. In these situations, much of the focus often turns to securing field gateways at the edge to control unauthorized access from the outside world.

Many of the sensors and devices encountered in an Industrial Internet deployment are designed to function with minimal power requirements. These devices are typically networked using the IEEE 802.15.4e specification (instead of 802.3 Ethernet or 802.11 wireless). The IPSO Alliance has defined a protocol stack for these devices, as shown in the following figure:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/a9e424f9-8d8e-4f80-9cd5-dc164eed8b0b.png)

Figure 8.4: IIoT Protocol StackIn the Industrial Internet, such devices will often use the **Constrained Application Protocol** (**CoAP**) for data transfer, a variation of the HTTP protocol that was defined by the **Internet Engineering Taskforce** (**IETF**). CoAP is promoted as a standard by the **Open Mobile Alliance** (**OMA**) and is intended for usage when resources are constrained, such as for low power transmissions over a **Wireless Sensor Network** (**WSN**). The protocol is designed to easily bridge to standard HTTP-based networks such as the internet and connect to nodes located there.

To assure proper authentication, data integrity, and confidentiality (such as for preventing eavesdropping of messages), the **Datagram Transport Layer Security** (**DTLS**) protocol is used with CoAP and deployed over UDP-based networks and upon low-power wireless personal networks (6LowPAN). The 6LowPAN networks feature a typical range of up to 20 meters in a WSN.

Alternatively, proper authentication, data integrity, and confidentiality can be assured via the IPSec protocols, an IETF standard for deployment over IP networks. IPsec can be deployed over IPv6 upon a 6LowPAN network.

Because of its limited 20 meters range, an alternative to 6LowPAN is sometimes sought for WSNs. The **Bluetooth Low Energy** (**BLE**) protocol can be used by enabling connections with a range of up to 100 meters. BLE is packaged with its own passkey authentication for the pairing of devices and encryption capabilities.

It is sometimes desirable to use a mobile phone to directly access a device to manage it or check its status. While BLE provides one option for doing this, a second option is to use **Near Field Communications** (**NFC**) protocols. NFC protocols enable the mobile phone or mobile device to establish communications only when it is within a few centimeters of the second device, so strong pairing is enforced by distance limitations.

When power is not an obstacle, the traditional internet protocol stack is deployed. This well-known stack is illustrated here:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/558ee21b-7319-4d76-98b6-512a9b3c14d3.png)

Figure 8.5: IP Stack**Transport Layer Security** (**TLS**), the more recent replacement for SSL, enables proper authentication, data integrity, and confidentiality to be maintained. For example, DoS attacks instigated against device-to-device communications networks are typically prevented by implementing TLS using PSKs.

A **trusted platform module** (**TPM**) is recommended for storing keys in on-chip circuitry where possible so that keys can't be disclosed to unauthorized parties. When hardware-based security is not present in the device, a **Hardware Security Module** (**HSM**) might be added, usually as a plug-in USB device or SD card inserted into the device.

IPsec might also be deployed here as an alternative to TLS. Generally, IPsec is preferred to meet site-to-site communications security needs since it can provide full access to a local network.

Data storage provided in the devices can be susceptible to tampering and information disclosure. Data encryption can be applied to prevent this when devices support cryptography. Digital signatures and **access control lists** (**ACLs**) are used for control access and encryption and de-encryption of data. The operating system images are sometimes signed to prevent someone from tampering with them.
