# IIoT security guidelines

Protecting the IoT, including IIoT deployment, is often seen as being in the national interests of a country. This has led to many of the standards from around the world, which we will describe in the next chapter.

In the United States, the US **Department of Homeland Security** (**DHS**) ([https://www.dhs.gov/securingtheIoT](https://www.dhs.gov/securingtheIoT)) stepped in to also provide guidelines regarding securing the IoT. The DHS defined the seven strategic principles for securing the IoT:

- Incorporate security at the design phase
- Promote security updates and vulnerability management
- Build on recognized security practices
- Prioritize security measures according to potential impact
- Promote transparency across IoT
- Connect carefully and deliberately

The strategic principles from the DHS are targeted toward several roles among security stakeholders. Architects and developers should consider security implications when defining, designing, and developing devices, sensors, services, or any other component of the solution. Device manufacturers should focus on improving the security of their devices. Service providers should adopt secure operating procedures and select secure devices and infrastructure for enabling their services. Finally, the Industrial Internet users in organizations deploying these solutions have a critical role in maintaining security.

The DHS is also actively promoting public-private partnerships to improve security. The DHS Science and Technology Directorate runs a **Silicon Valley Innovation Program** (**SVIP**) and funds companies to promote work involving IoT security ([https://www.dhs.gov/science-and-technology/news/2017/02/21/news-release-st-awards-nearly-1m-five-start-ups-phase-2-rd](https://www.dhs.gov/science-and-technology/news/2017/02/21/news-release-st-awards-nearly-1m-five-start-ups-phase-2-rd)). Innovative technology solutions to security issues are sought as part of this effort.

For example, in early 2017, the DHS funded five different companies, each to address a different area of innovation:

- Improved authentication of devices and data integrity through blockchain
- A distributed data-protection model to solve authentication, detection, and confidentiality challenges of devices
- Creation of a deployable open source and lightweight version of the SPECK cryptographic protocol to be run on devices
- Improved visibility and detection as components connect and disconnect from networks
- A secure wireless gateway for IoT devices conforming to IEEE 802.11 standards

SPECK

 SPECK is a software-based lightweight block cipher that is designed to run on small form factor IoT devices with about 256 K or more memory. It is based on publicly released work by National Security (NSA) in June 2013. SPECK offers performance characteristics that are half the size and yield twice the performance of the comparable AES encryption. The Machine-to-Machine Intelligence Corporation (M2Mi) was tasked with building the open source version of DHS as this book was being published.The DHS also hopes to improve situational awareness and security measures for protecting IoT domains related to critical infrastructure (such as airports) through these partnerships. Situational awareness addresses the following three capabilities:

- **DETECT**: This is the ability to know what IoT devices and components are connected to a given network or system
- **AUTHENTICATE**: This is the ability to verify the provenance of IoT components and prevent and detect spoofing
- **UPDATE**: This is the ability to securely maintain and upgrade components

In Germany, a similar partnership has formed between the government and various companies and organizations through formation of Industrie 4.0. It published a point of view on Industrial Internet security ([https://www.plattform-i40.de/I40/Redaktion/EN/Downloads/Publikation/it-security-in-i40.pdf?__blob=publicationFile&v=5](https://www.plattform-i40.de/I40/Redaktion/EN/Downloads/Publikation/it-security-in-i40.pdf?__blob=publicationFile&v=5)) titled *IT Security in Industrie 4.0*. Industrie 4.0 also created a working group on the security of networked systems with a goal of helping resolve *the outstanding issues concerning secure communication and secure identities of value chain partners* ([http://www.plattform-i40.de/I40/Redaktion/EN/Standardartikel/plattform.html;jsessionid=EFC5334B6C9902B04CF6A24303BC01C0#sicher](http://www.plattform-i40.de/I40/Redaktion/EN/Standardartikel/plattform.html;jsessionid=EFC5334B6C9902B04CF6A24303BC01C0#sicher)). In addition, the work group is addressing detection of cyber attacks on industrial production processes and evaluating their business implications. Finally, the work group is looking at the cultural transformation needed for employees in such companies, including additional knowledge and experience required to respond to security issues.

We'll now focus in the next two sections of this chapter on two specific regions of the IIoT architecture that align well with two centers of security expertise found in many organizations today: devices and connectivity from the edge to the cloud gateway and the backend services.
