# Components of backend infrastructure cost models

How the backend infrastructure relates to how costs are tallied is heavily dependent on the deployment scenario used. Traditional on-premises backend infrastructure cost models for IIoT projects include the following:

- Software licensing and support
- Computer servers and maintenance
- Disk storage and maintenance
- Networking (in the data center)
- Data center power and cooling (and data center expansion if needed)

We will break the software costs into applications, middleware and data management, operating system, and virtualization layers. Each of these have licensing and support costs in the on-premises model. This breakdown will help us explain the components included the subscription costs of the various public cloud-based offerings:

- **Infrastructure as a Service** (IaaS)
- **Platform as a Service** (**PaaS**)
- **Software as a Service** (**SaaS**)

We will illustrate the on-premises model using the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/49e55a64-e547-47b9-bc17-36e4816cbcfc.png)

An IaaS deployment in the public cloud includes server operating systems, virtualization software, computer servers, disk storage, networking, and other data center costs (including maintenance) in the subscription price models. This is illustrated by the following diagram's shaded areas:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/3b135b41-3154-4e29-8827-494c03bdd36b.png)

In IaaS, organizations follow a w model for middleware and data-management software, and for applications software, or sometimes a *pay as you go* model. They also pay maintenance to those software vendors just as they would in the on-premises model.  
 PaaS deployed in public clouds additionally includes middleware and data-management software licensing and support (including maintenance) in the subscription costs. So, we will illustrate that here by adding middleware and data management as a shaded area to our previous diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/4c26f509-b6bd-4f4f-adab-ba843bdb7a39.png)

SaaS solutions also includes applications in the subscriptions. These applications can include the specific applications and application logic required for the Industrial Internet solution, as well as modern business applications that become closely linked to, and part of, the project. So, the entire diagram appears shaded as pictured here since all backend infrastructure costs are included in the subscriptions:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/9710b136-1ec9-44de-bd1e-ccbda8ae38c5.png)

The way that an organization accounts for costs can impact whether on-premises or cloud-based solutions are chosen. Some prefer to purchase data center infrastructure since they can account for such purchases as Capital Expenditures, or CapEx. CapEx is defined as the acquisition of permanent assets in a non-recurring manner, where the benefits accrue over a lengthy time and the assets can be amortized or depreciated.  
 CapEx has been particularly favored in organizations that receive budget increases and approval through governing bodies (such as in utility companies where rate increases are reviewed by government commissions). Many regulated companies continued to deploy their latest solutions on-premises even as cloud-based deployment strategies were becoming popular in other industries.

Cloud-based subscription models fit into the **Operational Expenditures** (**OpEx**) model for cost accounting purposes, and many companies find this better aligned with how they run their business. It is noteworthy that cloud-based solutions have also experienced significant subscription price decreases over time as the major public cloud providers gain benefits from massive scale and repeatable footprints deployed around the world. Such price fluctuations in a beneficial direction further align with the OpEx strategy for cost accounting.

About on-premises cloud solutions

 As this book was being published, several public cloud providers had begun offering the same cloud software stack on platforms designed to be deployed in traditional data centers. While these share some similarities in cost models to public cloud IaaS, PaaS, and SaaS solutions, there are some differences that impact cost. The power, cooling, and data center space must be provided by the company hosting the solution. Local networking is also the responsibility of the hosting company. The servers, storage, and networking are less elastic since they must be pre-installed in anticipation of future growth (if on-demand growth is to be provided). They are typically not shared among multiple companies. Since platform growth is guessed at, the growth typically occurs in larger cost increments than in a public cloud-based solution, where shared resources are available and added on-demand. So, such on-premises cloud deployment strategies tend to be higher cost than deploying in public clouds.
