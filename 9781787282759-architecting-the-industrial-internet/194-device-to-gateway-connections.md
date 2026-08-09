# Device to gateway connections

Devices might be paired with field gateways at the edge or directly to cloud gateways. Authorization and authentication of devices requires recognition of their identities. Device identities are typically stored behind cloud gateways in IoT hub databases. Indexes of these devices enabling rapid look-up are sometimes maintained in separate locations for enhanced security.

To fight spoofing, device identification and authentication typically uses TLS or IPSec. PSKs are used when devices do not support cryptography. Other directory services might be leveraged for authentication (such as Active Directory). IP filtering can be used to accept or reject specific IP addresses.

Devices commonly use their own pre-existing X.509 certificate to authenticate with gateways. Periodically, a certification authority generates new certificates for the devices and gateways to use. Obviously, keeping authentication keys safe is important in maintaining secure connections.

Careful control of granted authorizations is required to fight unwanted privilege escalation. These are often managed using access control lists associated with the devices.

Application payload data in transit is usually secured separately. The data is transmitted in encrypted form (encoded with Avro or some other means). Transmissions might use secure messaging protocols, referred to as AMQPS, MQTTS, and HTTPS, that are deployed with TLS. The secure messaging protocol implementations protect transmissions with a combination of encryption and security certificates.

Field gateways are sometimes subject to spoofing attempts that falsely represent the gateways as devices. Similar authentication methods to those previously mentioned should be used between the field and cloud gateways and a TPM is suggested for storing certificates. Memory in the device might be encrypted to protect data residing there.

Management of devices is through agents that are installed in the field gateways or on the devices themselves. These often follow standards such as the **OMA lightweight management standard for devices** (**OMA LW2M2M**) and are intended to work over power-constrained communication wireless networks. Based on a REST approach, OMA LW2M2M defines a resource and data model that is extensible and builds upon CoAP for secure data transfer.

Gateways can also be subject to unauthorized privilege escalation attempts, and the data stored in them and transmitted over networks can be subject to attempts at data eavesdropping and disruption. Access control lists are also used here to eliminate attempts to escalate privileges. Data at rest and in motion and gateway operating systems are often encrypted to maintain security.

Throttling limits in the cloud gateway

Cloud gateway throttling limits are imposed to help ensure that DoS attacks do not cause critical connections to become unavailable. Typically, limits can be put on identity registry operations, device connections, device-to-cloud sends, cloud-to-device sends, cloud-to-device receives (for devices using HTTP), file upload notifications, device twin reads and updates, job operations, and other parameters in certain IoT hubs.Architects will sometimes specify that IP-capable devices communicate over the internet directly to cloud gateways, provided they can establish secure communications. Transmission might occur using secure messaging protocols and/or a **virtual private network** (**VPN**). The VPN capabilities are sometimes provided by gateways or firewall devices paired in the field with those in the cloud-based or on-premises data center.

Communications might also occur over a private dedicated network between the edge and the data center that many often view as a safer and more secure alternative to transmitting over the internet.
