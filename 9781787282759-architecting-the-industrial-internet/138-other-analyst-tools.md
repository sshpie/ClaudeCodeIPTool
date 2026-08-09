# Other analyst tools

Other analysts in your organization likely want to simply understand what happened or the outcomes of predictive analyses prior to making business decisions. If the organization has a data warehouse, many will already be familiar with ad-hoc query and analysis business intelligence tools and the reports such tools can produce, or are downloading the data from the warehouse to manipulate it in Excel spreadsheets for this purpose.

As noted earlier, in a Lambda architecture defined for IIoT solutions, NoSQL databases and Hadoop clusters (data lakes) often reside alongside the legacy data warehouses. Over the past decade, SQL support in these data-management systems has improved, and the same business intelligence tools are often used with these engines.

Organizations also sometimes see a need to observe the real-time updates of activity in streaming analytics engines in the speed layer. Many business intelligence tools are now capable of displaying such activity. The following is an example of how live activity might be viewed in a meter and historical chart of environmental readings rendered by Microsoft Power BI:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/c8aa42e8-4a29-41c1-99d1-d1405b6fcd0a.png)

Finding the location of data in the multiple data-management systems in a Lambda architecture has sometimes been a challenge for business analysts and data scientists. As they access data using business intelligence and machine learning tools, great value can come from having access to a data catalog that uses previously extracted metadata from all of the data-management systems to provide guidance on what the data means and where it is found.

A data catalog can provide several important functions. It enables users of the catalog to register, enrich, discover, understand, and consume data sources. There are typically several classes of users. The most common business users can use the catalog to browse and search for data and better understand the context behind the data. Publishers can also register data sources and enrich or annotate the data. IT administrators apply policies to control access and track and monitor usage of the data catalog.

Data wrangling and information discovery tools

 A new class of tools emerged in the past decade to explore data residing in Hadoop clusters. Referred to as data wrangling or information-discovery tools, these tools can sample large data sets gathered from the huge volumes present in Hadoop and provide a business user interface to explore the relationships between entities defined in the data. They can also be used to generate new data sets and provide simple reporting and visualization of data.Before we describe a possible role for field gateways in performing analytics and the components in the speed and batch layers, it is worth taking a look at how many earlier Industrial Internet applications were deployed, especially those in process manufacturing, and how that footprint is evolving.
