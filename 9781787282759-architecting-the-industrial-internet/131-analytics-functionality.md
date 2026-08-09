# Analytics functionality

Industrial analytics footprints must provide certain features to deliver solutions to functional and non-functional requirements while addressing the complexity present in this multi-domain architecture. These features include the following:

- **Visualization**: Displays and manipulates data and analytic results using charts and graphs
- **Exploration**: Ad-hoc querying of stored data
- **Design**: Analytics automation for data quality, mining and machine learning, and business intelligence
- **Orchestration**: Distributes requests over clusters of computing resources to collect and aggregate data
- **Connection**: Exchange of data and work between components
- **Cleansing**: Removal of irrelevant and duplicated data and noise, and merging data from multiple sources
- **Computation**: Execution of statistical and machine learning calculations
- **Validation**: Governance ensuring analytic results are accurate
- **Application**: Analytic results used to improve or correct automation, or aid human decision making
- **Storage**: Historical archival of incoming data
- **Supervision and management**: Monitoring, updating, correcting, and optimizing the information model, metadata, data sources, processes, and computing resources

Industrial analytic activities depend on the availability and access to the data from industrial processes and assets. The distributed nature of IIoS, and the need for analytics to produce results in time to take meaningful actions, sometimes pushes the analytics to the edge or in middle tiers where data is streaming. Once the analytics are performed, the values might be archived via batch feeds to data management systems where further analysis is possible by data scientists and SMEs. There, they might interpret and validate readings or recommend additional filtering or sampling. If further analysis is not deemed necessary, the raw data can be discarded.

To enable the continuous processing of industrial data, an analytics workflow can be developed within the data framework and automated. The workflow automation orchestrates the transformation of raw data into analytic results and performs execution of the analytic prescriptions. Workflows and their content can be improved and fine-tuned to improve accuracy and produce better result as more is learned about the processes and should be versioned.

Finally, the analytic results should be communicated in an understandable format that improves human understanding and decision making. They will want to interact and visualize the data in diverse ways. Some might want to drill through aggregations to details via hierarchies and related items.

As the analytics are honed over time, increasingly meaningful patterns can be discovered. Anomalies might be detected and alerts can be sent to operators along with supporting data as required. The root cause of anomalies and faults can be diagnosed, and prescribed actions might be taken automatically or through human intervention. By applying analytics to optimize the operating parameters and operational efficiency, failures can be avoided. Failures caused by human error can be reduced or eliminated.

Applying analytics to improve operational efficiency can result in optimal operation of devices, equipment, and reduced human stress. However, the proper data must be provided at the proper time and appropriate analytical models and algorithms must be applied, guided by engineering and business domain knowledge.
