# The multi-tier IIoT architecture

Next, we will take a look at the tiers of the architecture and how they interact to produce the desired system behaviors. In subsequent chapters of this book, we will provide guidance on how to simplify the design and analysis of the subsystems and foster their reusability.

The most commonly used reference architectures for the Industrial Internet and IIoT have three-tiers: Edge tier, Platform tier, and Enterprise tier. The commonly used definitions of the three tiers are as follows:

- **Edge tier**: The Edge tier collects data from the deployed machines (the sources of data) using various connection types. The architectural concerns for the Edge tier can include the nature of sensors and the machines or devices where data is being collected from, their location, governance scope, and the type of network connection, as well as the storage, transmission, and the computing needs for the collected data.
- **Platform tier**: The Platform tier receives, processes, and forwards data and control commands from the Edge tier to the Enterprise tier and vice versa. It can provide structures for data ingestion, data stores, and asset metadata, and can store configuration data and provide non-domain-specific services such as data aggregation and analytics.
- **Enterprise tier**: The Enterprise tier can implement domain-specific applications, decision support, and business intelligence systems, and provide user interfaces to human consumers of the information.

Let's take a quick glance at the following diagram depicting the tiers mentioned earlier:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/650d1613-f53e-4824-b8df-28a8402c5bed.png)

The providers for Industrial Internet platforms and solutions decide what functionality to provide and which components to configure in each of the tiers. General Electric often uses the terminology *get connected*, *get insight*, and *get optimized*, which requires all the three tiers to fully realize outcomes from Industrial Internet. A more detailed review of typical IIoT platform strategies and solutions will be covered in subsequent chapters.
