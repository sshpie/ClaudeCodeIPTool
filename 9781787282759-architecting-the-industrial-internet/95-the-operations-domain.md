# The operations domain

The operations domain provides life cycle management of the control domain. The scope of management includes device grouping, authenticating and provisioning the devices for service, configuring them (including ongoing updates and applications), and monitoring changing conditions in devices for health, security, and remediation (including retirement).

As you might expect, the components underlying the operations domain overlap heavily with the control domain since many of the operations are pushed to the devices. We will illustrate this in the shaded area of the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/4ee013fd-42c8-4f26-b812-8bb49f00f144.png)

Management of millions of devices is possible today. The devices managed might have varying hardware, software, and messaging protocol characteristics. Identification, logging, and management of devices occurs in the cloud gateway or in an on-premises gateway if the backend infrastructure is not located in the public cloud.

Key management functions that should be provided, and that you should evaluate, include the following:

- Synchronization of properties between cloud and device *twins* when monitoring and responding to changes on the device
- Ability to take interactive device actions (referred to as **methods**)
- Broadcasting and scheduling of twin changes and methods at scale in the form of *jobs*
- Dynamic reporting of device status and health through queries
- Ability to perform firmware updates, rebooting, and factory resets of devices, and configuration management of device behavior
- Authentication of devices (typically using X.509 certificates)
- Support for secure and encrypted data messaging via AMQPS, MQTTS, or HTTPS
- IP filtering to reject or accept specific IP addresses

Device and digital twins

 Device or digital twins refer to a hardware agnostic approach to representing device input, device state, device metadata and device configuration. The use of device twins can shield management of the devices from underlying protocols and can be useful for testing device driven applications in agile development environments.SDKs for devices, services, and field gateways are often offered as complementary to the management products in this domain. Custom software might be developed in the cloud or on-premises development environment, and then deployed to the device(s) using the capabilities we outlined in this section.

In our supply chain optimization example, many of these actions will be critical to the success of the project. To deliver value to the business, the infrastructure must be well managed and secure. When shortages of critical components or possible damage to those components in transit are detected, we must take appropriate actions to ensure production continues so that key optimization critical success factors can still be achieved. Periodically, we will issue software and firmware updates to the smart devices to improve their functionality and security.
