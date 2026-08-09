# Incremental upgrades

In most IIoT systems, components, software, protocols, and so on will need to be upgraded incrementally as newer versions are released and older ones become obsolete. The connectivity framework needs to provide backward and forward compatibility for communications protocols and data structures to enable incremental upgrades.

Sustaining engineering requires the prototyping and testing of upgrades and enhancements. Prototypes and testing need development and test platforms where ongoing patching and upgrades can be developed and tested before deployment. These environments typically need to be included and supported within the connectivity framework and network. The tested component can be provided to the system via the provisioning network. As new components are added to the system, the provisioning framework manages the chain of trust and delivers certificates for authentication.

Virtualized or cloud environments make upgrades easier, as the entire upgraded component can be dropped in rather than installing and configuring upgrades.

Edge devices, network systems, analytics, and other components may necessarily be added, upgraded, or replaced over time. New devices go through an enrollment processes to configure and authenticate themselves to the network. As new components are added to the system, the provisioning framework manages the chain of trust and delivers certificates for authentication
