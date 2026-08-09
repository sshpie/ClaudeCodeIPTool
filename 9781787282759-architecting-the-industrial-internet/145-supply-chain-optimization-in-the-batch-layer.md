# Supply chain optimization in the batch layer

As we described the speed layer in our supply chain optimization examples, we noted that we will have multiple types of streaming data being gathered. We wish to store this data for historical analysis, including machine learning. Hence, we will include a Hadoop cluster in our architecture, serving as a data lake.

In an earlier chapter, we noted the presence of data warehouse platforms. We will link our data warehouse(s) and data lake to enable queries across both engines and to load tables in our data warehouse after cleansing the raw data.

Business intelligence and machine learning tools will access all the engines in our architecture. We believe that our data scientists will develop predictive models using the data lake.
