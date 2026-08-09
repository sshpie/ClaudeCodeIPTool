# The batch layer

The batch layer is the location of data-management systems storing historical data in our architecture. Incoming data streams from the speed layer commonly land in a NoSQL database. Initially, a variety of NoSQL key-value pair databases were commonly used and scaled through a technique called sharding, the horizontal partitioning of a database across multiple database servers. Some organizations use this type of NoSQL database in PoCs for rapid deployment or as pre-processing engines in production solutions.

In the past few years, Hadoop clusters have gained in popularity as the landing spot and serve as a data lake in the Lambda architecture you saw in the diagram. They can support the large data volumes of historical data that are often present in IIoT projects and are an optimal location to run machine learning embedded solutions.

Relational databases continue to have a role in deployment strategies as the underpinning for data warehouses and data marts. These often provide the historic database of record for transactions in an organization and can provide important data needed to answer business questions.

The batch layer in the architecture is most often built in a public cloud today. Data volumes tend to grow tremendously over time and smaller data samples in separate engines must sometimes be spun up quickly. A public cloud provides the elasticity needed to meet these demands.
