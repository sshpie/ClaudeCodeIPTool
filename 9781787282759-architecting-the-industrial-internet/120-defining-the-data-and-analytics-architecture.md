# Defining the Data and Analytics Architecture

Now that we've considered some of the benefits of *buy* versus *build* by looking at what Industrial Internet applications can provide, it is time to take a closer look at the underlying architecture and considerations around key components. When we are deploying applications, much of this is under the surface. However, since you might choose to create a largely customized solution, and almost any IIoT deployment requires some degree of customization, understanding how to piece together the underlying architecture is required and is probably a big reason why you are reading this book.⌈

In [Chapter 4](c15efc6c-ceb2-4fcf-ba6b-21343a317dbb.xhtml), *Mapping Requirements to a Functional Viewpoint*, we described the information domain and the functional requirements it fulfills. You might recall that this domain delivers the metrics needed to run the business. Some of the functions that must be provided include ingestion and cleansing of data, data management, and data analysis through machine learning algorithms and business intelligence tools.

Here, we'll focus on the information domain components that must be part of our architecture. We'll also describe the roles of some of the tools and locations for processing analytics and machine learning inside the information domain, and at the edge (in devices and field gateways) in the control domain.

This chapter covers the following topics:

- Data and analytics requirements and capabilities
- The Lambda architecture and IIoT
- Analytics, machine learning, and analyst tools
- Early Industrial Internet applications and historians
- The speed layer in the architecture
- The batch layer in the architecture

As in the previous chapters, we'll describe how these components could be included in the architecture of the supply chain optimization example (CEMENTruck Inc.). By reading this chapter, you should gain an understanding of how you might include these components in your own architecture designs and solutions.
