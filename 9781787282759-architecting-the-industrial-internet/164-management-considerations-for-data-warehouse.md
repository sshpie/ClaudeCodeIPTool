# Management considerations for data warehouse

Since a data warehouse is a historical copy of data, the storage requirements will increase over time. In the case of an upgrade of the source system, the data warehouse may need to be updated accordingly.

Some application vendors provide a corresponding integrated data warehouse, but this is not typical. Most data warehouse systems are custom-built.

Advantages of data warehouses are as follows:

- Integrate data from heterogenous sources
- Perform historical analysis over large amounts of data without impacting operational systems
- Enable cross-functional analysis
- Improved data quality
- Converge disparate systems to a common semantic

Disadvantages of data warehouses are as follows:

- Usually require large IT investment to develop and maintain.
- Lag time in loading data from source systems.
- Data ownership, security, and access are important features. Data warehousing integrates data from multiple systems and locations. Many users access the data warehouse to perform analysis. Access rights to the data need to be carefully managed at the row level, and consideration needs to be given to who can access the aggregate data.
- Can require large, and growing, data storage requirements.
- Queries from business intelligence tools are usually ad hoc, which may result in a slow response if the system tuning is not optimal for the query.
- Assumptions must be made as to what data has value for inclusion in the warehouse.
- Data must be transformed to a common, inelastic schema.
