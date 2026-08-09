# The information domain

Though some data collection and analysis can take place in the control domain to actuate immediate responses in the edge devices, a much broader and larger data collection and analysis repository is established in the information domain. Here, data can be gathered from multiple control domain locations and from business domain data sources to enable better business operations decision making and to optimize business processes.

In our example, the information domain could be deployed adjacent to control domains in manufacturing plants and distribution centers or on mobile equipment or platforms. The information domain is more commonly established in a central repository in the public cloud or on-premises with the ability also to gather data from back-office business applications.

The following diagram illustrates the information domain in the public cloud as represented by the shaded area:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/89ea5d84-f049-4e81-935f-903179911130.png)

Several data-related operations take place in this domain, including the following:

- Data ingestion from sensors in the control domain and operations data sources
- Data quality and cleansing activities
- Data transformation (to rationalize data from various sources into common formats)
- Data persistence and storage
- Data cataloging establishing common metadata
- Analytics applied to data in motion and at rest
- Data governance

We will cover the architecture for the delivery of these capabilities in more detail in [Chapter 6](08fea60c-06cf-406c-959e-f29c48e894f6.xhtml), *Defining the Data and Analytics Architecture*, but will introduce key components here that provide the necessary functions.
