# Financial justification of our supply chain project

We will now apply cost models to our supply chain efficiency example, and then align those with benefits achieved as we determine return on investment at various stages of our project. In this example, we'll first compare the costs of deploying a solution using an on-premises backend infrastructure with one that includes deploying the backend infrastructure using a PaaS model.

Note that the numbers we present here are not meant to be specific to a vendor (though we hope you find them broadly representative and that they provide you with guidance as to how you might create similar models). Some of the cloud vendors provide useful TCO modelling tools and other pricing tools to help you understand the costs of deploying your backend infrastructure on their cloud offerings.

Traditional on-premises cost models are well understood. The models include price of hardware acquisition, software acquisition, networking and data center costs, and support. Subscription models are a bit more complex in PaaS deployments, as subscriptions are priced using various metrics that the cloud vendors determined align to utilization of the offering.

Pricing is generally reflected on a per month basis in PaaS. Pricing can vary across data center regions due to differences in electricity rates, staffing costs, and other factors. This could be one factor you consider when selecting a region to deploy in. You might also select a region based on other criteria, such as proximity to your on-premises location or the region's ability to meet data sovereignty requirements.

Some of the typical PaaS data management, data loading, and access-related components in IIoT projects and their associated metrics that you would need to define to gather costs include the following:

- **Hadoop compute engine**: Number of nodes, cores/node, hours of activity
- **Hadoop data lake storage**: Storage volume, read transactions, write transactions
- **NoSQL database**: Storage volume, utilization units
- **Relational database data warehouse**: Storage volume, utilization units
- **Extraction, load, and data transformation tools**: Number of activities and length of time that data movement occurs
- **Data egress**: Volume of data moved out of PaaS cloud
- **IoT hubs**: Number of messages per day
- **Authentication (directory and multi-factor)**: Number of users

Analytics and business intelligence components and related metrics include the following:

- **Data lake analytics**: Analytic utilization units, length of time utilized
- **Streaming analytics**: Analytic utilization units, length of time utilized
- **Machine learning tools**: Number of seats, length of time experiments occur
- **Business intelligence tools**: Number of sessions per month
- **Data catalog**: Number of users

Some of the core backend infrastructure components and metrics include the following:

- **Virtual machines**: Platform instance size, number of VMs, length of time available
- **Networking**: Port speed, data plan (metered or unlimited)
- **Support**: Most basic developers, standard, or extended / professional

With that as background, let's now compare on-premises backend deployment costs versus PaaS in the cloud for our supply chain efficiency example in a very simplified model.

Large-scale storage and compute is often needed in IIoT projects. These are major factors that drive configurations and costs. Here, we estimate that we are going to need about 80 terabytes of storage in the Hadoop cluster and about 20 terabytes of storage in a data warehouse to store and analyze the data coming from our smart devices. The following table compares the two backend deployment options that include the key components required over a 3 year period:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/c39e6c5f-782d-45ae-8001-604a57058fbc.png)

The PaaS option appears to be more cost effective in this example. We need to add several important additional cost items that we will assume to be the same here (for simplicity), regardless of whether or not we deploy the backend infrastructure on-premises or using PaaS. The items added include the cost of the smart devices (pre-assembled and in hardened containers), data transmission costs (based on the amount of data transmitted over time and the networking charges associated with the data volume), and the cost of custom development that includes implementation and training.

We have summarized these costs in the following table:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/f89fb78b-6163-4abf-88c5-6183047ed8c9.png)

We have consistently seen that deployment of Hadoop clusters (including procurement and set up of servers and storage) takes most IT organizations 6 to 8 months. For purposes of this exercise, we'll assume the total benefits achieved by building the IIoT project with the backend deployed either on-premises or as PaaS will be the same, but the benefits associated with the PaaS backend will begin to accrue 6 months earlier.

You might expect us to deploy the project stages in the order of the priorities we outlined earlier in this chapter. Based on those priorities, we'd begin with the product manufacturing solution, followed by the finance solution, and then the supply chain management solution. However, many of the benefits to be gained are directly attributable to solving supply chain issues, so we'll start that portion of the project sooner than might be expected.

The following illustration shows when key investments are made, when project stages are started, and the total costs and benefits accrued after the first 3 years using an on-premises backend deployment strategy:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/319a4533-be5e-406d-8105-03c4d9d145b5.png)

This diagram is aligned with our earlier logic indicating that about 8 months are needed to procure and install the new backend components (including Hadoop and other software, and related servers, storage, and networking) in the on-premises data center. At that point in the timeline, work on the manufacturing stage of the project can begin on the production systems.

In the PaaS environment, we simply configured the needed backend server, storage, and software components on our cloud-based platform. This can take place within days. Thus, development work on the backend production systems can start much sooner.

The following diagram shows how delivery of the project could progress using a public cloud-based PaaS backend:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/f6cc2226-90d5-42af-8786-f2fff2b627b2.png)

When comparing the two timelines, we can readily see the impact of deploying using the PaaS backend strategy. Since the backend platform is more quickly configured in the cloud, full development begins sooner (and more development spending begins earlier). However, much less platform money is needed up front, and significant business benefits begin to accrue much earlier.

In many ways, early benefits are even more important than the cost difference between the two (although the cloud-based approach is also less expensive during the timeline that is illustrated). Early attainment of significant benefits helps ensure that the value of the project is seen quickly. This can help guarantee that funding will remain in place for the project as it continues to roll out.

Net Present Value (NPV)

 The value of money fluctuates over time. NPV is calculated by a formula that adds the initial investment outlay to subsequent cash flows that are discounted based on prevailing rates of return on money over time. These formulas are often used by financial analysts to determine the viability of potential projects as they seek to understand when a positive return on investment might be expected while considering the changing value of money.The benefits in our example are quite spectacular and might not be fully believed by financial reviewers, even if backed up by our line of business sponsors (though we did get the numbers from them in our earlier discovery). So, we might choose to go back to the sponsors and suggest that we use more conservative numbers that can more easily be defended if there are any doubts about their validity.
