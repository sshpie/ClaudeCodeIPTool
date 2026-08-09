# Why is it time for the Industrial Internet?

In 2010, the IoT and Industrial Internet became familiar terminology. The World Economic Forum and others declared this to be the next generation of the Industrial Revolution. As in previous generations, several technological advancements came together to enable a new class of solutions and applications, changing business models and capabilities.

Sensors began to be mass produced at ever decreasing costs. As price points, size, weight, and power requirements for sensors decreased, engineers began to create device designs that included them in anticipation of being able to gather useful data on device status as soon as it became feasible. Since smart sensors can also be programmed and updated, they can evolve and become more "intelligent" over time. For example, inclusion of such smart sensors in automobiles led to rapid advancements in the development of autonomous vehicles.

The sensors themselves most often transmit semi-structured data in a streaming fashion. Coincidentally, analyzing mass quantities of semi-structured data became possible a decade earlier through development of NoSQL data engines (and Hadoop specifically) to solve the problems of Internet search optimizations and recommendations. Next generation platforms holding exabytes of data are deployed today by companies in the search engine business.

Exabytes

 Depending on when you read this book, the exabyte could be a new term to you. An exabyte is a unit of data storage equivalent to one quintillion bytes. A more common reference is that it is equivalent to one million terabytes or one thousand petabytes. In case you were wondering, the next bigger unit of scale you might hear about is the zettabyte, which is 1,000 exabytes. The amount of data that sensors can produce is driving us to define solutions with new data storage units.The development of new and innovative software solutions became more viable for start-ups and smaller organizations as cloud-based platforms became available (mostly eliminating an expensive upfront investment in infrastructure). The cloud also enabled faster time to deployment and elastic scalability that was difficult in classic data centers.

The cost of networking and bandwidth reduced over this time to provide ubiquitous connectivity for the IIoT. Some of the connectivity options and technologies used include **Radio-Frequency Identification** (**RFID**), Wi-Fi, **Bluetooth Low Energy** (**BLE**), and 2G/3G/4G with 5G on the horizon.

The growing popularity of open source software data management offerings and development tools also helped minimize early costs. Today, as the Industrial Internet has matured, we see many integrated solution footprints and applications that rely on underlying open source components.

The following diagram represents a common architectural pattern often seen in Industrial Internet implementations and is called a **Lambda architecture**:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/d8ffcae9-734e-47ee-833e-cf710a185a40.png)

The illustration shows streaming data feeds from smart devices. The streaming analytics engine analyzes this feed in real time and will sometimes have machine learning algorithms deployed to process the data. The data lake pictured is most often a Hadoop cluster and is designed to load and store massive amounts of data of all types. As in the previous generation, traditional data warehouses and data marts are batch fed. Business intelligence tools are shown pointed at the data mart, data lake, and streaming analytics engine in our illustration.

We'll describe these components in much more detail in subsequent chapters as we lay out the data and analytics architecture. Obviously, there is also a lot more detail in the information technology platform architecture, which we'll cover as well.

New manufacturing technologies are also now employed in Industrial Internet solutions. Robotics in manufacturing became common in industries where the cost of labor was high, such as in the automotive industry, around the turn of this century. The robotics that were deployed improved the consistency and quality of the products produced and helped to contain costs. The addition of intelligent or smart sensors to newer generations of these devices enabled more functional and flexible capabilities. The wider applicability and growing usage of robotics also led to decreases in their pricing, helping drive further adoption.

Many manufacturers and companies that design products are now experimenting with 3D printing. 3D printers enable the manufacturing of products and components anywhere; such a printer is deployed and accessible via a network. Such technologies are often referred to as additive manufacturing. The ability to print spare parts on demand for industrial machines can have a profound positive impact on the supply chain ecosystem, as the cost of such additive manufacturing continues to decrease.

**Artificial intelligence** (**AI**) and machine learning are also enabling more intelligent devices. As devices become self-learning, they can react to changing situations in real time. We'll discuss these topics and other emerging technologies when we explore what is likely to occur in the near and more distant future in the last chapter of this book.

These new capabilities are causing companies to rethink the value of their data and the kinds of businesses they are competing in. Many are facing new and non-traditional competition from other industries and are evaluating *digital transformation* strategies that sometimes include new strategies for monetizing their data assets. Some are becoming data aggregators, selling data to other companies and subscribers that find it useful.

The following diagram summarizes the four generations of the Industrial Revolution we described:

![](/api/v2/epubs/urn:orm:book:9781787282759/files/assets/03981c4d-66fb-462c-aaff-ff3a6635dc3a.png)
