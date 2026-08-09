# Data and analytics requirements and capabilities

Industrial analytics are unique in that the results of analysis often directly impact the physical world operationally, and can also have safety implications. Taking actions based on analytics could be harmful or undesirable. Since industrial analytics interpret and prescribe actions that interact with other sensors and components, there is also the potential for conflict. Therefore, it is important to fully understand the various information streams so that correct decisions can be made. The following are some of the unique requirements for consideration:

- **Correctness**: Industrial analytics requires a higher level of accuracy to avoid undesirable and unintended consequences in the physical world
- **Timing**: Industrial analytics must deliver results within their prescribed time horizon to satisfy synchronization requirements and ensure reliable, high-quality operations
- **Safety**: Strong safety requirements are necessary to safeguard workers, users, equipment, and the environment
- **Contextualized**: Industrial analysis is always performed within the context of an activity, and an accurate and complete understanding of the analytic results requires an understanding of the processes and the states of the equipment and peripherals
- **Causal-oriented**: As industrial systems have complex and causal relationships, the analytics must be modeled with domain-specific subject matter expertise linked to physical modelling and statistical, data science, and machine learning knowledge
- **Distributed**: Many industrial systems include hierarchical tiers and are distributed geographically, and each tier or subsystem might have its own unique analytic requirements requiring localized analytics (requirements for timing and resilience can result in the analytics being distributed and implemented close to the source of data, and to the target of the analytic result)
- **Streaming**: Due to the continuous execution or batch processing of industrial systems, most analytic data and analytic results will be streaming in nature so that the analytics will be applied to live data as it is generated or transmitted (traditional batch-oriented analytics might also provide information to improve analytic models and human decision-making)
- **Automatic**: To support continuous operations, streaming analysis and application of analytic outcomes must be automated, dynamic, and continuous
- **Semantics**: To properly understand the data and produce accurate analytic results, data needs to be understood in context, attributed at the source, and communicated to improve the accuracy (data that is inferred or taken out of context will result in uncertainty)

To glean useful analytic results, the architecture that is deployed should first efficiently collect data and then stream or store the data, or both, and then transform it for analysis. Robust data management is necessary to facilitate this process.

Successful analytics requires the pre-processing of the data. Pre-processing techniques that are utilized are driven by the type and format of the data being produced, where the data is produced, and whether the rate of data generation allows for it to be processed in batches or requires streaming processing. The volume and speed of data in IIoT can present several challenges.

Data management in IIoT systems involves incorporation of various tasks and roles from a usage viewpoint, along with the functional components of the functional viewpoint. The activities for data management include the following:

- Reduction and analytics
- Publish and subscribe
- Query
- Storage, persistence, and retrieval
- Integration
- Description and presence
- Data framework
- Rights management
