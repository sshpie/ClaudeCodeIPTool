# Management considerations for data lakes

It’s easy to dump data into a data lake without a clear idea of what it will be used for or with the intention of using it later. Without some level of control, you can easily end up with a data swamp in which its difficult to manage or find relevant data, or worse, a data graveyard where data is stored but never used. A data lake needs a centralized index to keep track of data and information, and any different versions of it, and where it came from. It can also be useful to score the information as to how useful or accurate it is, and for which uses and applications and it's suitable how long it will be relevant or useful, with data governance to enforce retention and disposition policies.

Security and access rights also need to be considered, especially once it is aggregated and ownership becomes murky. As underlying Hadoop systems generally have minimal security, an analyst or data scientist with access to one cluster could easily access all the data. Depending on the level of data sensitivity or criticality, a corresponding governance process should be put in place to control authorization, access, and audit.

Some data refinery technologies are available to provide automated transformation to make a governed big data set available on demand for the business analyst.

Advantages of data lakes are as follows:

- Data is stored in its raw form, no integration or transformation or predetermined schema is required, and there is no need to classify data. Any data format and type can be stored and analyzed.
- Silos of data as in application databases and most data warehouses can be avoided. Data can be analyzed across the enterprise by different disciplines in different contexts for a variety of purposes.
- Maintains data provenance, lineage, and ownership.
- No need to make assumptions as to which data has value.
- Data integration requires fewer steps.
- Since the data lake resides on the HDFS, huge volumes of raw data can be stored for future reference.

Disadvantages of data lakes are as follows:

- Risk becoming a data graveyard in which data is dumped but never used
- Data silos and empty sandboxes are still possible without data-management discipline
- Data management techniques need to be employed to keep track of data
