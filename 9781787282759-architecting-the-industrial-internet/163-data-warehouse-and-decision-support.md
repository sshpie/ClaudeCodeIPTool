# Data warehouse and decision support

**Decision Support Systems** (**DSS**) and data warehouse technologies were developed to address the reporting and analysis shortcomings of the 3NF schemas employed by enterprise applications. A data warehouse is a subject-oriented integrated copy of data in one or more applications or operational systems. A data warehouse is made up of an ecosystem of several functions with the end goal of maintaining an operational history, and enabling and performing analytics to support decision making. As many enterprises have grown through acquisitions, they may have multiple systems performing the same function at various locations from different vendors. As they are from different vendors, there is no integration between them.

Characteristics of data warehouses are as follows:

- **Data integration**: Data from many sources is integrated
- **Subject oriented**: Data is limited to one or more related subjects and organized accordingly
- **Time variant**: Data warehouses include past historical and current data
- **Nonvolatile**: Data is added, but not altered once stored in the data warehouse

Many data warehouses are used to store only aggregated data (that is, sales by region), but not the raw data, and enable time-series analysis of trends and analysis of correlations between disparate data sets. An operational data store is a type of data warehouse used to store data from an application. This data may be maintained for a short-term analysis, usually a few months, and then purged to make room for newer data, while the KPIs, analytic results, and aggregate data are preserved long term.

Functions of a data warehouse are as follows:

- Integrate, organize, and standardize data for analysis and reporting
- Preserve data and maintain data history
- Analyze and query substantial amounts of data
- Enable decision support

The following figure illustrates the data warehouse architecture:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/696c6d63-5905-4254-93ad-8f34e2896880.png)

Figure 7.5: Data warehouse architecture
