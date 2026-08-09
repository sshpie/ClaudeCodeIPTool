# GRC in the supply chain optimization example

In the previous chapter, we described securing the supply chain optimization example through secure networking and alluded to the other approaches we would need to take to secure the rest of the infrastructure. To ensure that our solution will remain available and avoid security compromises, we should make sure that our architecture follows appropriate guidelines and standards and that a GRC strategy can be put into place.

We begin with an assessment of governance and certifications requirements already in place at the organization that must be followed. We then assess any additional standards that we must comply with.

In the CEMENTruck Inc. example, a relevant industry group is the **National Ready Mixed Concrete Association** (**NRMCA**). Such industry groups sometimes self-regulate, determine best practices, educate members regarding relevant industry regulations, and lobby for favorable terms. The **Federal Motor Carrier Safety Administration** (**FMCSA**) governs the hours of service for drivers in this industry. The relevant guidelines come from 49 CFR Part 395 ([https://www.law.cornell.edu/cfr/text/49/part-395](https://www.law.cornell.edu/cfr/text/49/part-395)). Increasingly, IoT is being used for compliance-related activities. Use of **Electronic Logging Devices** (**ELDs**) ([https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/FMCSA-ELD-Final-Rule_12-10-2015.pdf](https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/FMCSA-ELD-Final-Rule_12-10-2015.pdf)) is governed by Section 395.24. This section lists the cementing truck driver's responsibilities as follows:

- A truck driver must correctly provide the information that the ELD requires as prompted by the system and required by the motor carrier
- A driver must input the driver's duty status by selecting among the following categories available on the ELD:
  1. Off Duty, OFF or 1
  2. Sleeper Berth, SB or 2 when sleeper berth is used
  3. Driving or D or 3
  4. On-duty but not driving or ON or 4

- A driver must also provide the following:
  1. Manual entry of this information in the ELD:
    - Annotations when applicable
    - Driver's location description when prompted by the ELD ([https://goo.gl/CrtPes](https://goo.gl/CrtPes))
    - Output file comment when directed by an authorized safety officer
  2. Manual input or verify the following information on the ELD:
    - Commercial motor vehicle power unit number
    - Trailer number(s) if applicable
    - Shipping document number if applicable
  3. An authorized safety official can request that a driver produce and transfer from an ELD the driver's hours-of-service records in accordance with the instruction sheet provided by the motor carrier:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/ea1b8d46-edda-4398-abaf-a56a58db1816.jpg)

The ELD for Hours of Service in Trucking Industry ([https://calhountrucklines.com/wp-content/uploads/2014/11/electronic-logging-device.jpg](https://calhountrucklines.com/wp-content/uploads/2014/11/electronic-logging-device.jpg)) illustrates industry-specific compliance and provides the Industrial Internet architect with more than simply best practices. In this case, we can see the metadata needed for system design (from the pick list for drop-down options in the user interface) and the supporting data structures underneath.

The architect must understand such regulatory landscapes to do the following:

- Properly design the Industrial Internet solution so that country- or region-specific compliance can be handled (using appropriate cloud regions and availability zones)
- Propose how IIoT solutions can be used to help the management comply with GRC (such as how wearables can self-report the different states of the driver automatically and remove any human data entry errors)

Many companies involved in Industrial Internet projects, such as the company in our example, place importance on the ISO 9001 standard and certification. The IIoT architecture developed should support processes for optimizing performance, managing risk, and continual improvement. The design should also include components useful in assuring data quality so that fact-based business decisions can be made.

The proposed design in our example includes the networking of devices over a private network and public networks (with VPN deployed there). This part of our design will be evaluated using the IEC 62443 guidelines.

When choosing a public cloud service provider, we'll first check their certifications for compliance with relevant international, domestic, and industry standards. In our example and our organization, several ISO /IEC standards as well as NIST standards are relevant.

Though CSPs certify the footprint they provide can meet these standards, it is up to us to implement an architecture that fully complies with the standards. As we create our architecture, we will also create a preliminary GRC plan to assure that standards will be met throughout the life of the project and the solution.
