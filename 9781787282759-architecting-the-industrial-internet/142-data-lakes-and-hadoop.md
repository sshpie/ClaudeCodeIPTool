# Data lakes and Hadoop

Hadoop was invented early in this century to enable analysis of data streams common in solving search engine problems. Given that Industrial Internet problems are also solved through analysis of streaming data, Hadoop became an important technology component deployed in many such projects.

Hadoop is supported as an endpoint from IoT and event hubs enabling loading from the speed layer into the batch layer. Events containing data can arrive continuously, and the data is simply appended providing the real-time loading needed for such data volumes.

Hadoop features a utility often used in loading streaming data called Kafka. Some organizations use Kafka to replace traditional message brokers. When Kafka is deployed, producers of messages write to topics and consumers read data in the topics. Consumers can be gathered into consumer groups when reading a topic. In Hadoop, topics are partitioned across the many nodes in the cluster. Kafka can handle messages storing objects in any format (string, JSON, and Avro are common). Keys can be attached to messages to direct them to specific partitions.

The streaming data from devices is often described as semi-structured. It has some identifiers or metadata and values embedded in the data stream that needs to be parsed. Hadoop has, as one of its earliest foundations, the ability to map data that arrived as streams and reduce it to the data of value through programming (hence, the MapReduce capability).

Though Hadoop was not initially noted for ease of use or speed of processing, much has changed in the past dozen years. Hive was introduced to provide SQL compatibility, and Spark in-memory processing now enables response times closer to those of relational database engines. Spark's in-memory processing engine runs on Apache Hadoop YARN (Yet Another Resource Negotiator) that is included in the major Hadoop distributions. Spark's APIs are used to enable fast execution of streaming, machine learning, and SQL workloads that often occur in frequent iterations.

Data entering the data lake arrives in its raw format and is typically not cleansed. This is often seen as desirable by data scientists who want to perform machine learning and advanced analytics on undisturbed data. In some organizations, data from transaction-processing systems or data warehouses also makes its way into the data lake if needed as part of the analysis.

Once the data lands, some organizations rationalize data in Hadoop, creating cleansed data sets. Some will also put structure around some of the data using HBase. As noted earlier, the tools of choice by data scientists and business analysts can include machine learning, data wrangling, and business intelligence tools in analyzing and manipulating this data.

The tremendous data volumes analyzed by search engine vendors (in the Exabytes and beyond) led to the introduction of next generation data-management engines separating compute from storage. Some popular next-generation engines leverage the Hadoop capabilities using YARN linked to more scalable backend data storage solutions (including BLOBs) that are now appearing in offerings from some public cloud vendors.

BLOBs and other data

 Object data stores are also popular for managing other data in IIoT projects, such as captured images, engineering drawings, and other documents.Compute nodes are sized based on processing demand (CPU type and speed) and in-memory Spark processing needs (memory size). The volume of data transmitted and retention requirements drive storage sizing. By default, data in Hadoop is triple replicated for performance and availability, so replication as well as compression must be considered when sizing storage.
