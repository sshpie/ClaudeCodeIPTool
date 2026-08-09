# Airline proactive and preventive maintenance

Maintaining aircraft in good condition is a prerequisite for improved aviation safety and maintaining service levels. Aircraft maintenance is divided into four checks that are carried out at predetermined intervals based on the number of flight cycles (landings and take-offs) or flight time. These checks originated from Boeing's Maintenance Steering Group (MSG) in 1968 and were designed to ensure the safety of the Boeing B747-100 aircraft.

The checks are defined as follows:

- **A Check**: This is a *light* check usually carried out overnight at an airport gate. This check is carried out every month or every 500 flight hours (depending on the type of aircraft).
- **B Check**: This *light* check is also carried out overnight at an airport gate, normally every 3 months.
- **C Check**: A *heavy* maintenance check is usually carried out every year or 1.5 years. Since this check includes the disassembly of critical parts, it is performed in an aircraft hangar.
- **D Check**: This check is also known as an overhaul check or heavy maintenance check; it is performed every 4-5 years and inspection of the entire aircraft is carried out.

With this MSG-3 approach, the aviation industry moved away from the tradition of MRO activities at fixed time intervals to one that considered the operations and intervals needed to keep the aircraft safe. This approach was successful due to time and money savings, and due to unnecessary interference with components. Boeing started to recommend the same approach to all their aircraft models.

When an airline is scheduled to fly, the crew performs several checks apart from those just mentioned to assure the plane is safe to fly. Some potential problems are difficult to detect using traditional checks. Landing gear falls into that category.

Often, landing gear problems are not detected until the plane pushes back from the gate. Uncovering problems with the landing gear during this taxi out stage could result in an unscheduled flight delay. Each delay costs the airline between $25,000 and $40,000 and impacts customer satisfaction. If the delay occurs in the morning, it can have a cascading effect that impacts the entire day's flights. Problems with landing gear have traditionally had unclear causes that could not be determined until repair crews began working.

The following diagram illustrates the complexity of the components present in the landing gear ([https://www.faa.gov/regulations_policies/handbooks_manuals/aircraft/amt_airframe_handbook/media/ama_Ch13.pdf](https://www.faa.gov/regulations_policies/handbooks_manuals/aircraft/amt_airframe_handbook/media/ama_Ch13.pdf)):

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/a5a37ab3-84e4-479d-9a8b-6c015682603b.png)

The mechanical motion of the landing gear initially limited the use of sensors due to the amount of wiring required and the potential for problems. In older aircraft, sensors were limited to capturing the following:

- Position (extension or retraction)
- Wheel speed
- Weight on wheel
- Skid (and antiskid)

Today, additional sensors can improve the analysis of the state of landing gear and provide the intelligence needed for predictive maintenance. The sensors use wireless communications to the **Quick Access Recorder** (**QAR**), and data is downloaded when the plane reaches the gate. Additional information is collected in this manner, including the following failures and conditions:

- Failing to retract/extend
- Failing to get up-locked after retraction / down-locked after extension
- Exceeding retraction/extension time limits
- Failing to give indications in cockpit of down-locking, transit, and up-locking
- Loss in nitrogen pressure and oil in oleos due to leak
- Loss in pressure in tires due to leak
- Binding of wheel bearings and brakes
- Fully worn out friction pads
- Brake unit-related issues, such as overheating of brake unit
- Leakage of brake fluid and sponginess in brake pedals
- Failure of antiskid
- Leakage of nitrogen pressure in emergency extension cylinder
- Low brake pressure in emergency accumulator
- Low line pressure in emergency system
- Low brake line pressure
- Low battery voltage in emergency system

The following diagram indicates typical placement of these sensors:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/8bdab0d5-fd7a-4bed-ba6b-c672758ca299.png)

Source: [https://www.faa.gov/regulations_policies/handbooks_manuals/aircraft/amt_airframe_handbook/media/ama_Ch13.pdf](https://www.faa.gov/regulations_policies/handbooks_manuals/aircraft/amt_airframe_handbook/media/ama_Ch13.pdf)

To solve problems related to potential brake pad heating and hydraulic oil pressure problems in the landing gear, we can use sensors in the landing gear subsystems to gather data on the wearing of the brake pads and the hydraulic pressure profile. The data gathered from such sensors can be used to test a digital twin of the landing gear.

In this case, a solution team identified 34 sensors that can be applied to provide data for the early detection of wear or malfunction related to the brake pads and hydraulic oil pressure. Using the data from these 34 sensors, a digital twin of each aircraft's physical landing gear is tested and analytics is applied. The digital twin is updated as new data comes in, typically after each flight. This enables the MRO crew to diagnose the current issues. The remaining useful life can be predicted based on the accumulated historical data and the manufacturers' specifications.

The MRO crew would use a dashboard like the following one to understand potential hydraulic pressure issues and when it might make sense to replace a pump based on when failure thresholds will be reached:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/1230e8e6-aaee-4790-8a38-fa8bd0a7791a.png)

The MRO team might view a dashboard like the following one to understand brake pad temperatures and the optimal time to replace brake pads:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/7c4cb2f7-15bd-443e-8b62-a8bcc8f90188.png)

The data pictured in these illustrations was collected from the sensors and transmitted to the GE Predix Platform. Data services were used to persist the time series data and an asset service was used to model the sensors and subsystems in the landing gear. Analytic services, including custom algorithms, were applied against the asset model to determine anomalies and the remaining useful life of the subsystems.

The GE's Predix architecture for this solution is shown in the following diagram:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/1296e67a-743d-47d3-a4f7-4070a6938743.png)

We'll describe the importance of this framework and some of the other emerging frameworks in the next chapter of this book.

Automated Service Requests

 Airlines, aircraft manufacturers, and other transportation companies are experimenting with applying algorithms to use predictive failure information such as that presented here to optimally schedule service-based parts availability, the availability of skilled technicians able to perform the work, and the likelihood of parts failure, impacting schedules.
