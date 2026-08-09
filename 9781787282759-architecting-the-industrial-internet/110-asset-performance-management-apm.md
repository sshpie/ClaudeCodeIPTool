# Asset Performance Management (APM)

APM applications can be delivered via public cloud (SaaS) or can be for on-premises use. In this context, APM will stand for **Asset Performance Management**, another common use of the term APM in the field of information technology and systems management. This term implies **Application Performance Management**. In that context, APM monitors and manages the performance and availability of software applications. APM's goal is to help detect and diagnose performance problems in complex application and software platform. This in turn helps maintain an expected level of service or the **service level agreement** (**SLA**) by the software services provider. We will not use APM in that context in this book.

APM is a set of applications that generally provide a capability for asset health maintenance, where an asset is typically a physical device or a machine, in an industrial setting. Examples of such assets can be wind turbines operating in a wind farm or locomotives for transportation of goods train. The category can be thought of as **monitoring and diagnostic** (**M&D**) for assets.

Gartner defined APM as a collection of the capabilities of data capture and ingestion, integration, visualization, and analytics, all working together, for the explicit purpose of improving the reliability and availability of physical assets. Gartner's definition of APM includes the concepts of condition-based monitoring, predictive forecasting, and **reliability-centered maintenance** (**RCM**). This definition ties well to one of the common goals of APM, which is to reduce unplanned downtime of the assets.

LNS Research has another variation of the APM definition ([http://blog.lnsresearch.com/what-is-asset-performance-management](http://blog.lnsresearch.com/what-is-asset-performance-management)). According to LNS, APM is regarded as an approach to managing the optimal deployment of fleet of assets with the business goal to maximize profitability and predictability in the operations. The operation goal could be to focus on real margin contribution by the specific asset. Instead of looking at the physical asset on the accounting basis, such as the market value or depreciated value, companies can see how the asset is contributing to their revenues and profitability by looking at how individual assets are performing--whether inventory or **Plant, Property, and Equipment** (**PP&E**). This can allow the company to develop a vision of how they want to allocate resources and deploy the assets in the future. In this view of APM applications, it is not limited to a purely financial or even operational resource, rather one that cuts across functional lines. To realize this viewpoint of APM, it has to combine or connect to the best-of-breed **enterprise asset management** (**EAM**) software such as IBM's Maximo, with the need for near real-time information from production systems. APM has to use the power of the cross-functional data analysis and advanced analytics orchestration. Thus APM, broadly speaking, looks at the whole life cycle of an asset. This viewpoint of APM then enables organizations to make decisions that optimize not just their physical assets but also their operational and financial results while balancing the business risk.

APM applications can be used to monitor and prevent risk of the critical asset failure. APM applications often use analytics and data thresholds based on the properties and operating characteristics of the family of the asset or a specific asset. In more advanced APM applications, the operator may receive guidance for the optimal operating range and characteristics, in near real time. Likewise, an advisory could be related to repair versus sell or dispose decision for the asset or an expensive asset component.

The APM application would generally include capabilities to carry out the following activities:

- Provision the asset
- Capture the asset model, which will define the assemblies, subassemblies, components, and sensors
- Understand the relationship of the asset to the fleet and the whole network of assets
- Ingest data from the sensors and store it optimally
- Integrate other sources of data
- Design and/or deploy the analytics
- Create alarms and advisories based on execution of analytics and thresholds
- Display the visualizations of data and actionable items
- Optionally allow alarm disposition, case management, and trigger field services

Overall, APM applications will help reduce the total cost of ownership of the fleet of assets and improve the utilization, while balancing the risk to the company. This often results in lower unplanned downtime, reduced cost of maintenance, and better use of the scheduled maintenance windows. The following graphics shows how to balance a decision between preventive maintenance and scheduled maintenance cost for the physical asset to arrive at the minimum cost of replacement without compromising the business risk of operating the asset safely:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/e102193f-0951-40bc-842b-35e1ac1e07d4.png)

Source: [http://www.reliasoft.com/newsletter/v11i1/asset_management.htm](http://www.reliasoft.com/newsletter/v11i1/asset_management.htm)

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/6ed03a55-a82a-4ddd-9157-251aab04c68e.png)

The word *cloud* is a good representation of the common themes that accompany the APM. As a company is assessing APM, they should map their own requirements along these business themes while evaluating the capabilities and options for their APM suite.

The APM application used to monitor industrial assets like wind turbine can be built on the GE's Predix platform. It shows the three distinct tiers of the Industrial Internet platform. In this case, the industrial asset is a wind turbine operating in a wind farm, and it generates electricity. The wind turbine has sensors built in. Usually, the data from these sensors is collected via the control systems that are built in. Additional external sensors such as temperature, vibration, or wind speed can be retrofitted, when needed, to an existing asset. These, in turn, connect via a gateway device, in this case using the edge software called Predix Machine, to the Predix cloud via a secured means.

The Predix cloud understands the asset structure and its sensors and uses that information to store the data in a usable manner. This allows the analytics to consume this data easily. The business insights generated by these analytical applications such as predictive health monitoring alarms and advisories or operational guidelines can then be pushed to the enterprise tier for human consumption. Similar use case may apply to many other industry verticals such as energy (gas generator), healthcare (MRI machine), transportation (locomotive engine), or aviation (jet engine), but is not limited to just these types of industries. The following is the architecture of the GE's Predix platform:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/3d33b903-ed34-47db-a9ba-8fbd6ee5bed3.png)

As Industrial Internet architects evaluate the application and its architecture, the end-to-end view from sensors to business applications provides a good perspective to help future-proof their decisions. The complete solution stack caters to both the edge and the cloud with the ability to connect to the existing enterprise tiers.
