# The Lambda architecture and IIoT

Industrial Internet solutions gather data from smart devices "at the edge" in field locations that are often remote. These devices typically stream data that eventually ends up in cloud-based or on-premises data-management systems.

Many of you might be more familiar with traditional on-line transaction processing systems feeding data warehouses via batch data loads. Streaming data is data in motion, and that introduces the need for another analysis layer called the speed layer. This multi-layer approach is described by what is popularly called the Lambda architecture.

Traditional online transaction-processing systems feed the batch layer directly. Devices at the edge feed streaming data directly into a speed layer. The data usually then makes its way into the batch layer and is added to the data at rest.

The following diagram illustrates the main building blocks included in a Lambda architecture. The direction of most of the flow of data among these building blocks is indicated by the arrows:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/211e4427-fb61-42fd-b6ea-9cc68ede20e9.png)

The following diagram shows the components we introduced in [Chapter 4](c15efc6c-ceb2-4fcf-ba6b-21343a317dbb.xhtml), *Mapping Requirements to a Functional Viewpoint*, and how they align to the Lambda architecture, including the presence of the speed layer for analysis of streaming data and the batch layer:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/150826d1-db5c-4f6d-a5e0-fa79945a1db1.png)

A serving layer is sometimes described to be part of the Lambda architecture. This layer provides indexing of views of data at rest for faster queries and is usually deployed as part of the data-management systems. The results of queries are presented in the business intelligence and analytics tools pictured in this diagram.

Business intelligence tools refer to a broad classification of tools used by the lines of business to retrieve, analyze, and transform data and report on business results. Interfaces typically include table and hierarchy definitions used to drill to detail. More modern tools often include native-language-like questioning and are beginning to leverage cognitive interfaces. We will describe how cognitive capabilities will play an increasingly important role in providing interfaces for humans using Industrial Internet solutions in the final chapter of this book.

The Lambda architecture works quite well for most organizations that have already built batch feeds to data warehouses and now are adding streaming data sources as part of their Industrial Internet project. In the supply chain optimization example introduced in earlier chapters, there is important data in legacy data warehouses that needs to be included in our analyses. So, we will design and deploy our solution as a Lambda architecture.

More recently, some organizations starting with an entirely new infrastructure have decided to eliminate batch feeds and process all incoming data as streaming data. This variation is called the **Kappa architecture**. The downstream data store only appends incoming data in this design, so a Hadoop cluster serving as a data lake is frequently chosen as the final landing spot for all data when this approach is taken.
