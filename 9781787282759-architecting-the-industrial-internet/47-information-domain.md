# Information domain

The information domain consists of functions concerned with gathering data predominantly from, but not limited to, the control domain. However, while the control domain monitors data in real time, analyzes it, and applies rules to perform local control of systems, the data gathered in the information domain is stored, or persisted, and transformed for analysis. It could also be applied to machine learning, potentially discovering deeper intelligence about the overall system and operations.

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/cb58bf8b-16d2-449b-804a-aa628ca2d9af.png)

Figure 2.7: Functional components of the business, information, and application domainData functions consist of ingestion, data quality, syntax, or formatting; that is, date formats, semantics, or context transformation, data persistence and storage, and data distribution.

IIoT data is typically generated and transmitted in online streaming mode, and the data is processed as it is received to provide real-time and near real-time analytics and feedback. Data collected in locations lacking sufficient connectivity may be collected and accumulated locally, and can be processed in offline batch mode.

The information domain also deals with data governance, including security, privacy, access control and rights management, and resilience. These functions may involve data replication, backup and recovery, snapshotting, and so on. Big data systems incorporate data replication as a fundamental part of their architecture, and are useful for inexpensive storage and the processing of very large data sets.

Analytics encompasses functions for data modeling, statistical and trend analysis, classifications, machine learning, data science, and other advanced processing. Analytics may be applied to data at rest in batch mode or on demand or on streaming data in motion, as it is received. Batch mode analytics are typically performed for consumption by the business domain, while streaming data analysis is typically performed for the operations and control domains.

IIoT systems typically generate large volumes of data at high speed. The volume and granularity of the data can quickly overwhelm networks, storage systems, and databases. Therefore, raw data can be stored on big data systems, and data that is known to have value for the business or operations domain can be extracted, typically as aggregated summaries, calculated **key performance indicator** (**KPI**), or snapshots. As there may be undiscovered value in the raw data, big data systems can store and process very large data volumes and can be analyzed and mined by advanced analytic tools and data scientists for insight into the operations.
