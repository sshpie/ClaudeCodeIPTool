# Usage viewpoint

The *usage viewpoint* identifies the users, parties, and roles of the IIoT system, and how they will interact with it. The usage viewpoint describes the coordination of activities throughout the system and its components, or how the system will be used; it becomes the input for the system requirements, and guides the design, deployment, operations, and evolution of the system.

The usage viewpoint is primarily concerned with executing tasks. Tasks are performed by parties who assume operational roles and do the work of the system. Roles consist of capacities and privileges to execute tasks or functions in support of specific activities. A party is any autonomous agent, either human or automated, whose job it is it to execute tasks and perform activities. A party must assume an appropriate role to execute the tasks required for the corresponding activities. A party may be assigned to one or more roles, and a role may be assumed by more than one party.

Tasks are defined within the context of a role. A functional map describes the functions and functional components mapped to the task. For example, a task analyzing temperatures may map to functions to analyze temperature data and aggregation functions to return the values for average, highest (maximum), and lowest (minimum) temperatures. An implementation map describes the implementation components necessary to execute the tasks. It also describes how a task's associated role(s) map to system components and operations.

Tasks may be combined in a coordinated fashion to perform an activity. Activities are sets of tasks required to perform a process in an IIoT system and are frequently executed repeatedly. An activity consists of a trigger, which initiates the activity, a workflow to control the sequence of task execution, and constraints, which define the boundaries of what the activity can do and preserves system characteristics such as data integrity.

Activities do not need to be described in detail initially, but should at least be described in the abstract, as potential activities are important in the design phase to define the requirements of the system.

The usage viewpoint ultimately drives the detail requirements, design, implementation, deployment, and sustaining engineering. An experience framework helps define how the desired human IoT experience maps to key usages and capabilities required to deliver the usage and experience:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/247ae7ee-4f00-4150-9fcb-a7295c490d56.png)

Figure 2.4:  IIoT experience frameworkIn this framework, each IIoT human-value experience is mapped to its key usages and the capabilities required for the usage. Focusing on usage sets the level of detail required for the use case.

The usage scenario approach can be used to:

- Identify current and future use cases and ensure the IIoT experiences are satisfied for the respective use cases
- Ensure coverage across the human-value experience for IIoT deployments by creating key usage scenarios that map to those values
- Provide guidance to bridge usage scenarios to the architecture framework

The experience framework allows the technical framework to be tracked back to key value experiences. Storyboarding each usage facilitates the definition of the usage requirements. Each pane in the storyboard has a detailed story with insights into what is happening, and can aid in identifying the entities, relationships, data sharing, and analysis needs. This decomposition exposes the architectural needs for each scenario.
