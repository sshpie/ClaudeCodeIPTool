# Using microservices and containers to speed DevOps

The **virtual machines** (**VMs**) on hypervisors that include operating systems remain popular as deployment vehicles in public clouds and on-premises data centers. However, at the time of writing this book, many organizations were adopting development strategies that promised more agility and built upon previous SOA development skills.

Such skilled development teams now often build microservices, single function entities that can be executed on their own while having generic interfaces (such as HTTP) for integration. Though microservices can be deployed in VMs, they are most often deployed using containers. The container is used to provide scope insulation and establish the necessary dependencies among the microservices.

Containers include minimal operating system code as they use a shared operating system kernel, thus helping to reduce the size of the modules produced and speed their distribution. They communicate to the operating system via APIs, which become quite important when the security and data persistence services provided by the O/S are needed. Docker has gained in popularity and provides containers available in the major cloud vendor offerings. Most of these cloud vendors provide container services capable of managing Docker.

Containers, by themselves, are especially useful when building and deploying GUIs that require little in the way of stored data resources. When stored data is needed, container clusters are created, deployed, and managed using cluster managers. Popular cluster managers include Docker Swarm, Kubernetes, and Mesos. Multiple container clusters are deployed when multiple data repositories are needed to provide data for applications.

In addition to container configuration management, several other management tasks are required. These tasks include container service discovery and distributed configuration storage with dynamic scaling, container networking, scheduling of containers on hosts, along with cluster management of containers, hosts, services and interactions. Management of scheduling is handled through tools that provide orchestration (such as Ansible, Chef, and Puppet).

An IIoT development team's ability to use this approach and maximize the agility of custom solution development and integration will largely be determined by their familiarity with these technologies, their skills, culture, and organization. If such skill sets are not present but the approach is desired, systems integrators might be selected for design and implementation.

Of course, much custom development can be avoided if the desired Industrial Internet solutions are available as predefined, prepackaged, and pre-integrated applications. Though flexibility might be sacrificed, at the end of the day, the right approach is one that delivers business value to the company quickly and positions it for long-term success.
