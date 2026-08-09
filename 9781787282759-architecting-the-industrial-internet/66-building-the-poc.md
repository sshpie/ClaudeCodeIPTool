# Building the PoC

To build the PoC, the implementation viewpoint prescribes selection and deployment within the scope of the project.

Most IIoT systems share a common platform that provides the basic processing, network, and operating systems needed by the IIoT services. The platform foundation could be performed by cloud solutions such as hosted databases and big data services, and **infrastructure as a service** (**IaaS**).

The IIoT platform's connectivity management services provide services and functions to connect devices and sensors to a network and manage the communications between them. Development, deployment, and application management are provided by application-enabled services. The following services, illustrated in *Figure 2.14*, are commonly shared across applications in IIoT systems:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/ae9f397e-7b0d-458a-8fa4-d87541e30c62.png)

Figure 2.14: IIoT platform service functionsThe tactical and strategic concerns of the architectural viewpoints are mapped to formulate strategic platform considerations for each viewpoint. These considerations should also be factored into platform-selection criteria. Platform investment decisions should consider specific requirements, market opportunities, long-term roadmap, and other factors.

The IIoT world brings into play a myriad of various technologies, including hardware and software. If market and competitive demands are critical, internal execution capabilities need to be examined. Organizations may find it necessary to augment technology and expertise from outside sources. Whether the components will be built, bought, or shared, engineering, software development, integration, or network consulting services may be necessary to augment the project team. The Industrial Internet is quickly becoming a fluid ecosystem of complementary and competing technologies in which organizations cooperate and partner on some projects and compete on others.

Various commercial technologies may be available to fill the identified use case gaps; therefore, build versus buy decisions may need to be considered. Building a solution in-house presents benefits and risks. In-house development enables the solution to exactly fit the requirements; however, it may require extensive man hours, and new skill sets that are not available internally. Consideration should also be given into how the solution will be maintained and upgraded if only a few engineers or developers understand the internal workings of the components. The inclusion of a commercially available technology reduces development time and mitigates skill shortfalls. Adopting an already proven technology reduces the risk, and best practices may be available.

When evaluating technologies and third-party partnering, many factors are considered:

- Enterprise alignment and synergy
- Opportunities from partnering
- Fulfillment for capability shortfalls
- Fulfillment for resource shortfalls
- Solution's fit to the requirements
- Cost of the technology and support
- How is it implemented and how does it integrate with existing systems
- How is it monitored, managed, updated?
- The technology roadmap, and how do future upgrades impact the IIoT systems
- What level of support can the vendor offer
- Availability of skill and expertise in the technology
- Security and privacy protections meet legal and organizational compliance requirements

There is a growing trend in IIoT towards the use of shared resources. Cloud services are an example of shared resources, where some of the infrastructures and software are *shared* in a hosted environment. Infrastructure, data storage, analytics, and applications are readily available as cloud services. Cloud service prices are based on subscription and usage, and may allow you to forego large expenditures and setup time for the required servers and software.

Open source technologies are another example of shared resources, with a seemingly endless supply of offerings, from operating systems to machine learning tools and solutions; however, reliability, and sustainability should be thoroughly studied. The sharing of commodity platforms and systems allows the PoC project team to spend more time and energy developing new and innovative technologies that have the potential to contribute directly to the organization's competitiveness.
