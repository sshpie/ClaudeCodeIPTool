# Data lakes

A data lake is a repository of data in its natural format and can consist of data of all types, schema, structured, and semi-structured. Its purpose is to serve as a repository for all analyzable data, including raw and transformed structured data from applications and relational systems, semi-structured data such as document collections (for example, email), logs, clickstreams, devices, geolocation trails, social media, and weather using HDFS. Unstructured data such as images, video, and audio can also be included in a data lake. Data can simply be dumped in the data lake with no consideration for integration and transformation.

Data stored in its native format can later be parsed for analysis. It can serve as a staging area for a data warehouse or can be accessed by data scientists to *discover* correlations, connections, or classifications and other intelligence.

The data lake provides a way to explore and analyze data without moving or duplicating it. A data lake makes data collection more efficient for industries, where data of high or unknown value is generated at high velocity.

Data lakes do not enforce a rigid metadata schema as in relational databases or data warehouses. Instead, data is bound to a dynamic schema created during query execution in which users build a custom schema into the query. This technique is called late binding or schema on read, and shifts the schema design from the data warehouse architect, who may not be familiar with the data or its use, to the data scientist or analyst.
