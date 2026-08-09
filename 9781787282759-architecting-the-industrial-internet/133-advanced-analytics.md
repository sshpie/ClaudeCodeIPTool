# Advanced analytics

Advanced analytics involves applying mathematical functions to data to understand and forecast trends, define clusters using common features, and discover relationships. For example, in an industrial setting, advanced analytics can detect and predict potential faults.

Advanced analytics can be described in the following approaches:

- **Automated**: This performs continuous analysis and applies the results back into the system to improve optimization and performance.
- **Real-time**: Analysis occurs as data is received to provide immediate results and prescriptive actions
- **Streaming**: Analysis is performed on a data flow in memory or other transient location without loading the data into a full-fledged data-management system
- **Active**: Components share analytic results in real time to enable rapid response
- **Causal-oriented**: Physical and neural network deep learning are applied to identify causal relationships
- **Distributed**: Analysis is performed across domains and systems using shared processing

The unique characteristics of IIoT solutions often require additional robustness and speed and accuracy of the analytics, especially when the analyses impact viability of the business and safety.

Network latency and reliability are critical to taking real-time actions. Inadequate network bandwidth will inhibit the flow of data. If these limitations create timing constraints, analytics must be performed near both the data source and the target the analytic results are used to control.

In a control system where high-resolution time-series data is generated at high frequency, data volume constraints can overwhelm network bandwidth constraints. Real-time control can become impossible. In these systems, data needs to be dynamically bound to the analytic functions in the edge using dynamic composition and automated interoperability. High-volume data might then be transmitted periodically or on demand to analytic systems where it can be analyzed for patterns, anomalies, and causal relationships.

Now that we have provided the necessary background on data analytics requirements and capabilities, we will begin to explore the architecture in depth and then explore the components that are fundamental in the architecture.
