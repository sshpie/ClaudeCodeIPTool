# The industrial data analytics framework

The industrial data analytics framework describes dig data analytics management systems on Industrial Internet systems data, which often take the form of the following data:

- **Relational data**: This format is best suited for metadata of assets and things, and as it captures the system configurations and relations to enterprise data systems. Commonly used relational database systems are Oracle, Microsoft SQL Server, IBM DB2, MySQL, and PostgreSQL.
- **Time series data**: This is a series of discrete data points in time order, often equally spaced in time. For industrial assets and sensors, this may be the bulk of the data. Such data is often stored in historian software that records the historical information and trends about industrial processes. NoSQL databases are also used to manage this type of data.
- **Object related data**: This form of bulk object storage is best suited for images, blobs, and other unstructured data. Examples of this type of storage are Amazon S3, Microsoft Azure blob storage, and Scality that can be deployed on-premise.

To run industrial analytics on such a variety of data formats, real-time and batch capabilities are required. The ability to orchestrate multiple analytics workflows is also required.

The stakeholders for analytics can be data scientists, analytics developers, architects, as well as **subject matter experts** (**SMEs**). The following diagram illustrates the typical life cycle of the development of industrial analytics:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/351eeb50-d514-4a4e-bce7-317a437e2711.png)

This is an iterative process and suitable for agile development. An important characteristic of the industrial analytics is the ability to not only pull the aggregated and summary data to the analytics but also to be able to push down the analytics to near real-time data feeds. This is due to the extremely large data volumes that devices transmit and the frequent nature of these transmissions.

In subsequent chapters, we will talk about such near real-time analytics technologies and discuss the emergence of the NoSQL database and Hadoop-based data management solutions fundamental to solving these problems. Architects of Industrial Internet solutions must embrace skills in industrial analytics and new data paradigms to be able to design effective solutions.
