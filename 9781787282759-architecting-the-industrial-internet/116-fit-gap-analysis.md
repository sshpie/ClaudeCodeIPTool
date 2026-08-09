# Fit gap analysis

Here are some criteria that can be useful for the IIoT Platform and applications gap analysis:

- Completeness of the solution (edge and cloud)
- Different modes of sensing and actuation technologies, protocol support at the edge, edge analytics
- Privacy and security of the data and compliance
- Data ingestion and data store capabilities
- Analytics and workflow capabilities
- Applications availability
- Developer ecosystem and marketplace for services and applications

We introduced a generic supply chain optimization problem in the previous chapters. Here, we'll look at how this could apply to the manufacturer of cementing trucks. We will use a hypothetical case study of a company that manufactures and services cementing trucks, called **CEMENTruck Inc.**, for performing the fit gap analysis of the Industrial Internet platform and applications.

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/8ba5a0b9-b036-4b06-858c-b745743d69c6.png)

CEMENTruck's Main Product - Cementing truckThe following is an extensive list of points that we need to consider for our case study:

- CEMENTruck Inc., manufactures concrete-mixing trucks, which cost about $250K each
- CEMENTruck supply chain is facing the following problems:
  - Growing cost concerns and complexity in managing the fleet services
  - Loss of competitive footing
  - Reliability and throughput issues in the factories
  - Increased dependency on supply chain system and related ecosystem
- CEMENTruck's increasing dependency arises from the following:
  - Business partners such as distribution networks and repair shops sharing maintenance history
  - Suppliers - raw materials and parts performance
  - Multiple third-party vendor tools and equipment
  - Rising in-house IT costs in maintaining ERP, and data warehouse and analytics solutions with little demonstrable benefits
- CEMENTruck's executive leadership (board mandate) is keen to understand the following:
  - How to maximize operational efficiency of the fleet operations
  - How to address supply-chain management
  - How to prevent competition from after-market parts and services providers outside of their network
  - How to address IT/OT integration issues

We extract the functional requirements from this case study and then look at available options to meet these. Since the main product of CEMENTruck Inc. is a cementing truck, which is a complex asset, it fits nicely with the need for Industrial Internet platform and application. Since the company is responsible for the warranty, services, and parts, when the trucking fleets are in use in the construction sites, it calls for connected trucks. These connected trucks can then send the sensor, environment, and related data to the platform. The platform should provide the edge connectivity to the trucks and secure communication to the platform.

The need for monitoring the health of the trucks in the field and the ability to provide predictive maintenance calls for APM application. This can get them started with the descriptive analytics. As part of the gap analysis, the company would have to evaluate if the analytics needed to create meaningful alarms and provide diagnostics support is provided by the APM application provider of the needs to be custom developed. Very likely, the predictive and prescriptive analytics would have to be developed by CEMENTruck's internal resources. However, what they need to evaluate is how easily they can port their legacy analytics to this new platform. Hence, they would have to evaluate if the legacy analytics languages such as C/C++, Java, and .NET are supported in the new platform being evaluated. Consider the illustration of the practical Internet connected truck at [https://hbr.org/2014/11/the-internet-connected-engine-will-change-trucking](https://hbr.org/2014/11/the-internet-connected-engine-will-change-trucking).

The alternative would be to rewrite these legacy analytics in the newer languages such as R, Python, Java, Node.js, or Go. In addition, multiple analytics may need to be orchestrated to create the end-to-end analytics workflow. An example of such a workflow for truck data could be the one shown here:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/9186ea00-bc80-4530-bae0-7d4b3269d38f.png)

As we work through the fit gap analysis for the case study of CEMENTruck's requirements, we can see how the previous section of this chapter applies where we had reviewed the capabilities of the APM application and the different kinds of analytics that are needed to unlock the full potential of the IoT data. Let's now look at some of the elements of the platform architecture in the context of this case study. We noticed that the company wants to move away from in-house IT systems to free up internal resources from routine *keeping the lights on* type of technology work. This leads us to look at how the Industrial Internet platform is delivered to the customer. This leads us to look at the on-premises versus cloud-based architecture.

CEMENTruck realizes that when the cementing trucks are in the field and operating in customer premises or the construction job sites, they are outside the corporate network. This would make the use of public cloud delivered platform a good option. The trucks will need wireless connectivity to the cloud platform in a secure fashion. This is often achieved via a gateway device on the truck. The gateway device would have to be provided and secured by edge management software to allow the 12,000 trucks that could be potentially connected over the next year. From an architectural standpoint, it maps to the edge and the platform tier. Since the current enterprise systems run on premises, the platform tier on public cloud, would have to connect to the IT systems for the necessary IT/OT integration.

As we continue our fit gap analysis, we will now look at the manufacturing side and the tie-in to the supply chain system. Another important element is the field services execution and delivery applications. As the trucks are being manufactured in the factories of the company, there are reliability issues leading to challenges with the throughput. This leads to challenges with the supply chain as the company is not able to provide good visibility and demand forecast to the upstream suppliers. To alleviate some of these issues, the company should look at collecting sensor data from the manufacturing assembly lines, material movement status in the shop floor, and the quality data. Such capabilities are collectively referred to as smart manufacturing. We will take a deep dive into this application family later in this chapter.

Next, we will focus on the gaps in providing the vital link between the manufacturing to the field operations of the cementing trucks in terms of the warranty and maintenance services. We noticed that the company is facing challenges in being able to provide timely services to its assets, and this is a threat as third parties can enter the parts and services business. Once the trucks are connected to the Industrial Internet platform and APM applications start providing the predictive maintenance advisories, CEMENTruck would need a system in place for the execution and delivery of the field services. A gap that seems to jump out is a field service management solutions for the service technicians out in the field and the maintenance managers. We must explore such service applications to meet this gap. We will look at this class of application in the subsequent section of this chapter.
