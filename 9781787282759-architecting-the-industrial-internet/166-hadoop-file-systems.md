# Hadoop file systems

As Internet search engines were emerging, the requirement to provide search capabilities on unstructured, variable, and high-volume data increased dramatically. Unlike enterprise systems, there is little need to enforce referential integrity and perform deduplication or other data management functions on text data, photographs, social networks, and time-series measurements. The **Hadoop file system** (**HDFS**) provides inexpensive storage and search capabilities for highly variable, high-volume, high-velocity, and high-variety data, or the 4 Vs of big data, and provides inexpensive storage for very large volumes of data.

As described in [Chapter 6](67818c03-0aa5-44cb-82d4-5bb6d449173f.xhtml), *Defining the Data and Analytics Architecture*, the Hadoop storage platform distributes data across many inexpensive servers, enabling massive data sets to be analyzed in parallel and with a rapid response time. The file system maps data to its location on a cluster, and the data processing occurs on the server near the data, rather than in a centralized server. Hadoop also supports storage of unstructured data and data sets with variable schemas.

Advantages of Hadoop are as follows:

- **Scalability**: Additional nodes are easily added as the system grows.
- **Low cost**: Hadoop can operate on commodity hardware and provide enormous value through analytics.
- **Flexibility**: Hadoop does not require a schema, and enables a wide variety of data types and data sources.
- **Speed**: Query data is mapped, processed (reduced), and then transmitted. Hadoop can quickly process terabytes of data in minutes.
- **Resilience**: Data is duplicated across nodes. A failure in one node does not result in loss of data.

Disadvantages of Hadoop are as follows:

- **Interactive analytics**: Hadoop's design makes highly interactive analytics difficult.
- **Security**: The nature of the Hadoop file system makes securing sensitive data difficult.
- **Risky functions**: Hadoop is built on Java and is vulnerable to exploitation by hackers.
- **Big data only**: Hadoop doesn’t perform well on small data sets.
- **No optimization and inefficient execution**: Since there is no cost-based execution plan, Hadoop clusters tend to be larger than a normal database.
- **Limited SQL support**: Basic SQL functions such as *group by* and subqueries are not supported.
- **Expertise**: Hadoop requires specialized expertise, and savvy developers command very high salaries.
- **Open source**: Hadoop is open source software, with inherent problems in quality and security. There are several vendors working to extend and improve on Hadoop's shortcomings in their own versions of Hadoop.
- **Not designed for updates**: HDFS can insert all kinds of data, but there is no update function once it is stored.
