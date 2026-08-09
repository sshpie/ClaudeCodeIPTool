# Chapter 10. Working with Network APIs

From Python, Go, and data formats to configuration templating with Jinja, we’ve explored key foundational technologies and skills that will make you a better network engineer. In this chapter, you’re going to put these skills to practical use and start to consume and communicate with various types of network device APIs to start automating your network.

As we introduced in [Chapter 2](ch02.html#netautomation), nowadays there are multiple options to interact with network platforms. Along with the traditional CLI and SNMP, we have new alternatives—from network-specific APIs (such as NETCONF, RESTCONF, and gNMI) to multipurpose APIs (such as HTTP-based ones or the Linux shell). Not every device supports all of these options, so understanding their capabilities will determine your automation options.

All interfaces are viable for automation, each one with its own pros and cons. The goal of this chapter is to introduce these APIs, showcasing how you can use them programmatically in Python and Go.

To best help you understand how to start interacting with networks programmatically, this chapter is organized into two sections:

Understanding network APIsWe examine the architecture and foundation of APIs, including RESTful and non-RESTful HTTP-based APIs, NETCONF, RESTCONF, and gRPC/gNMI. In each case, we introduce common tools used for testing and show how to use each one.

Automating using network APIsWe introduce some popular Python and Go libraries that allow you to start creating applications to interact with your network. We’ll look at the Python Requests and Go HTTP libraries for consuming HTTP-based APIs (including RESTCONF), the Python ncclient for interacting with NETCONF devices, the Go gNMIc for interacting with the gNMI interface, and the Python Netmiko library for automating devices over SSH.

As you read this chapter, keep in mind one thing: this chapter is *not* a comprehensive guide on any particular API and should not serve as API documentation. We provide examples using different vendor implementations of a given API, as it’s common to be working in a multivendor environment. It’s also important to see the common patterns and unique contrasts among APIs.

# Understanding Network APIs

Our focus is on four of the most common types of APIs you’ll find on network devices: HTTP-based APIs, NETCONF, RESTCONF, and gRPC/gNMI. We’re going to start by looking at foundational concepts for each type of API; once we review them, we’ll explore the consumption of these APIs with hands-on examples using multiple vendors.

###### Note

For each network API type, we have used one or two network platforms. This doesn’t imply that each API is the only interface a platform supports. Actually, each platform usually supports multiple interfaces, but for illustrating multiple vendors and interfaces, we have used an arbitrary mapping to show diversity, without extra considerations.

As we start our journey of *consuming* and interacting with network APIs, in each API subsection, our focus is just like the focus we’ve had thus far throughout the book—​on vendor-neutral tools and libraries. More specifically, we are going to look at tools such as cURL for working with HTTP-based APIs (RESTCONF included), NETCONF over SSH for working with NETCONF APIs, and gNMIc to interact with the gNMI interface.

It’s important to note that this section is about *exploring* network APIs in that we showcase how to get started using and testing network APIs without writing any code. We want you to understand the concepts from each particular API type before putting them to use in the next section. This section is *not* about the tools and techniques you would use for automating production networks. Those types of tools and libraries are covered in [“Using Network APIs for Automation”](#apis-aut_us_net_APIs).

Let’s get started by diving into HTTP-based APIs.

## Getting Familiar with HTTP-Based APIs

HTTP-based APIs are not exclusively used for network management. They are one of the most common interprocess connection types; thus most of the concepts introduced in this section apply to general use cases. Within the context of network automation, you will learn how to use APIs to manage network services using HTTP APIs as the management interface. For instance, HTTP APIs are used in [Chapter 12](ch12.html#automationtools) to provision dynamic network infrastructure via Terraform providers. In the same chapter, HTTP APIs are used to fetch data from a source of truth (SoT) containing the network device inventory and to create a dynamic inventory for Nornir.

You should understand two types of HTTP-based APIs in the context of network APIs: RESTful HTTP-based APIs and non-RESTful HTTP-based APIs. To better understand them and what the term *RESTful* means, we are going to start by examining RESTful APIs. Once you understand RESTful architecture and principles, we’ll move on and compare them with non-RESTful HTTP-based APIs.

### Understanding RESTful APIs

*RESTful APIs* are becoming more popular and more commonly used in the networking industry, although they’ve been around since the early 2000s. Most of the APIs that exist today within network infrastructure are HTTP-based RESTful APIs. Therefore, when you hear about a RESTful API on a network device or SDN controller, it is an API that will be communicating between a client and a server.

The client is an application such as a Python script or web UI application, and the server is the network device or controller. Moreover, since HTTP is being used as transport, you’ll perform some operations using URLs just as you do already as you browse the internet. Thus, if you understand that when you’re browsing a website, HTTP GETs are performed, and when you’re filling out a web form and clicking Submit, an HTTP POST is performed, you already understand the basics of working with RESTful APIs.

Let’s look at examples of retrieving data from a website and retrieving data from a network device via a RESTful API. In both instances, an HTTP GET request is sent to the web server (see [Figure 10-1](#apis-figure-rest)).

In [Figure 10-1](#apis-figure-rest), one of the primary differences is the data that is sent to and from the web server. When browsing the internet, you receive HTML data that your browser will interpret so that it can properly display the website. On the other hand, when issuing an HTTP GET request to a web server that is exposing a RESTful API (remember, it’s exposing it via a URL), you receive data back that is mostly encoded using JSON or XML. This is where you’ll use what we reviewed in [Chapter 8](ch08.html#dataformats). Since you receive data back in JSON/XML, the client application must understand how to interpret JSON and/or XML. Let’s continue with the overview, so you have a more complete picture before we start to explore the use of RESTful HTTP APIs.

![npa2 1001](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1001.png)

###### Figure 10-1. Understanding REST by looking at HTTP GET responses

Let’s take our high-level overview one step further and look at the origins of RESTful APIs. The birth and structure of modern web-based RESTful APIs came from a PhD [dissertation](https://oreil.ly/1a9lz) by Roy Fielding in 2000. In “Architectural Styles and the Design of Network-based Software Architectures,” he defined the intricate detail of working with networked systems on the internet that use the architecture defined as REST.

An interface must conform to six architectural constraints in order to be considered RESTful. For the purposes of this chapter, we’ll look at three:

Client-serverThis is a requirement to improve the usability of systems while simplifying the server requirements. Having a client-server architecture allows for the portability and changeability of client applications without the server components being changed. This means you could have different API clients (web UI, CLI) that consume the same server resources (backend API).

StatelessThe communication between the client and server must be stateless. Clients that use stateless forms of communication must send all data required for the server to understand and perform the requested operation in a single request. This is in contrast to interfaces such as SSH, which have a persistent connection between a client and a server.

Uniform interfaceIndividual resources in scope within an API call are identified in HTTP request messages. For example, in RESTful HTTP-based systems, the URL used references a particular resource. In the context of networking, the resource maps to a network device construct such as a hostname, interface, routing protocol configuration, or any other *resource* that exists on the device. The uniform interface also states that the client should have enough information about a resource to create, modify, or delete a resource.

These are just three of the six core constraints of the REST architecture, but you likely can already see the similarity between RESTful systems and how you consume the internet through web browsing on a daily basis. Keep in mind that HTTP is the primary means of implementing RESTful APIs, although the transport type could, in theory, be something else. To really understand RESTful APIs, then, you must also understand the basics of HTTP.

#### Understanding HTTP request types

While every RESTful API you look at is an HTTP-based API, you will eventually look at HTTP-based APIs that do not adhere to the principles of REST and therefore are not RESTful. In either case, the APIs require an understanding of HTTP. Because these APIs are using HTTP as transport, you’re going to be working with the same HTTP request types and response codes that are used on the internet already.

Common HTTP request types include GET, POST, PATCH, PUT, and DELETE. As you can imagine, GET requests are used to request data from the server, DELETE requests are used to delete a resource on the server, and the three Ps (POST, PATCH, PUT) are used to make a change on the server. In [Table 10-1](#apis-table-http-request-types), we list each method’s definition along with its meaning in the context of networking.

| Request type | Description | In networking context |
| --- | --- | --- |
| GET | Retrieves a specified resource | Obtaining configuration or operational data |
| PUT | Creates or replaces a resource | Making a configuration change |
| PATCH | Creates or updates a resource object | Making a configuration change |
| POST | Creates a resource object | Making a configuration change |
| DELETE | Deletes a specified resource | Removing a particular configuration |

#### Understanding HTTP response codes

Just as the request types are the same if you’re using a web browser on the internet or using a RESTful API, the same is true for response codes.

Ever see a `401 Unauthorized` message when you were trying to log in to a website and used invalid credentials? Well, you would receive the same response code if you were trying to log in to a system using a RESTful API and you sent the wrong credentials. The same is true for successful messages or if the server has an error of its own. [Table 10-2](#apis-table-http-response-codes) lists the common types of response codes you see when working with HTTP-based APIs. This list is not exclusive; others exist too.

| Response code | Description |
| --- | --- |
| 1*XX* | Informational |
| 2*XX* | Successful |
| 3*XX* | Redirect |
| 4*XX* | Client error |
| 5*XX* | Server error |

Remember, the response code types for HTTP-based APIs are no different from standard HTTP response codes. We are merely providing a list of the types and will leave it as an exercise for you to learn about individual responses.

### Exploring HTTP-based APIs with cURL

*cURL* is a command-line tool for working with URLs. From the Linux command line, you can send HTTP requests by using the cURL program. While cURL uses URLs, it can communicate to servers using protocols besides HTTP, including FTP, SFTP, TFTP, Telnet, and many more. You can use the command `man curl` from the Linux command line to get an in-depth look at all the various options cURL supports.

###### Note

cURL isn’t limited to Linux. It’s available in multiple OSs such as macOS and Windows. For installation instructions, check [*https://curl.se/docs/install.html*](https://curl.se/docs/install.html).

Multiple alternatives to cURL are available, either as command-line tools or GUIs, but all share the same concepts. Once you understand the basic ideas, you can apply them to the other tools. However, using a user-intuitive web GUI frontend, such as [Postman](https://www.postman.com), could make it much easier to learn and test HTTP APIs. These GUI tools put the focus on using the API without worrying about writing code. You’ll see an example shortly in [Figure 10-2](#apis-postman-example) to help you understand the look and feel.

We start our exploration of HTTP APIs by using cURL with the [Cisco Meraki](https://meraki.cisco.com) RESTful API (Meraki’s API documentation is available at [*https://oreil.ly/zHOWy*](https://oreil.ly/zHOWy)). *Cisco Meraki* is a cloud networking controller that helps to illustrate how to interact with this type of network infrastructure. Many modern NOSs also offer REST APIs, usually (but not limited to) implementing the RESTCONF interfaces, covered in [“Using RESTCONF”](#apis-restconf).

#### Using the HTTP GET method to retrieve information

As we’re just getting started with RESTful APIs, we’ll begin with a simple HTTP GET request to retrieve all *organizations* from the API, targeting the URL *[*https://api.meraki.com/api/v1/organizations*](https://api.meraki.com/api/v1/organizations)*.

###### Note

*Organization* is an abstract concept from Cisco Meraki created to support multiple tenants for the same account. Each will contain different network resources.

In [Example 10-1](#apis-curl-meraki-orgs), we use a cURL statement to call the Cisco Meraki URL and retrieve a list of all the organizations.

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis*](https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis).

##### Example 10-1. Retrieving Meraki organizations with cURL

```
$ curl 'https://api.meraki.com/api/v1/organizations' \                     
  -H 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' \ 
  -L                                                                      

# response omitted
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The URL is generic; it is shared by all Cisco Meraki customers. It’s offered as IaaS, covered in [Chapter 4](ch04.html#cloud).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

We have not defined any HTTP operation. Nevertheless, by default, cURL performs a GET operation. This behavior can be modified using the `-X` flag, as in next examples. You can see all the available cURL customizations via the command documentation: `man cURL`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `-H` argument, or `--header`, is used to include HTTP headers in the HTTP request. HTTP headers are key-value pairs used to pass metadata to the server, useful for things like authentication.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The `-L` flag, or `--location`, allows the client to follow any redirects issued by the server.

###### Note

The Cisco Meraki API token used in [Example 10-1](#apis-curl-meraki-orgs) has been taken from [Cisco Developer Hub](https://oreil.ly/XVQfU). You can use the same one if it is still active. If not, a new one will likely be available on this website, for API exploration.

Also, note that in the previous URL, the base URL path contains `/v1/`. This is an arbitrary way to indicate the targeted version of this API. As with any other application, the API can evolve over time, adding, changing, and removing resources. Using API versioning is a common pattern to offer a predictable behavior to consumer applications, without facing breaking changes (i.e., accessing a path that has been removed). In other APIs, the version may be specified via the `api_version` query parameter. This way, the URL path is not modified, and only the query parameter is appended; here’s an example:

```
$ curl https://my_application.com/api/my_path?api_version=1.3
```

The omitted output from the cURL statement in [Example 10-1](#apis-curl-meraki-orgs) is an output word wrapped on the terminal, which is hard to read. Alternatively, as shown in [Example 10-2](#apis-curl-meraki-orgs-python), you can *pipe* the response to `python3 -m json.tool` to pretty-print the response object, making it much more human-readable.

##### Example 10-2. Using the Python json.tool to render a JSON response

```
$ curl 'https://api.meraki.com/api/v1/organizations' \
  -H 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' \
  -L \
  | python3 -m json.tool

[
  {
    "id": "573083052582915028",
    "name": "Next Meraki Org",
    "url": "https://n18.meraki.com/o/PoiDucs/manage/organization/overview",
    "api": {
      "enabled": true
    },
    "licensing": {
      "model": "co-term"
    },
    "cloud": {
      "region": {
          "name": "North America"
      }
    }
  },
  # other organizations omitted for brevity
]
```

The object retrieved is a JSON object, which converts to a list in Python because it begins and ends with square brackets. Each item in the list is a dictionary, representing an organization and all its attributes. The response media type (in this case, JSON), can be influenced by the `Accept` header (expressing the client wish), but in this case, it has no impact because JSON is the only media type supported by this API.

To compare the user experience from cURL to Postman, [Figure 10-2](#apis-postman-example) shows an equivalent HTTP GET request done via the Postman GUI.

![npa2 1002](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1002.png)

###### Figure 10-2. Postman GET request

###### Warning

The UI you get from Postman may differ from the one in this book. UIs are evolving with the product, so it’s likely to change over time. However, the concepts remain the same.

In [Figure 10-2](#apis-postman-example), you can appreciate the same request and output from [Example 10-1](#apis-curl-meraki-orgs), but in a better visual presentation. Following the same pattern, you could reproduce all the examples in this section in Postman.

###### Tip

Postman allows you to create and publish Postman Collections as common API examples to be reused (using variables for customization). These collections can serve as a good reference for common operations on APIs. As an example, Nick Russo maintains an interesting collection for several network APIs at [*https://oreil.ly/QBJmd*](https://oreil.ly/QBJmd).

Commonly, behind a REST API, different resources are *related*. From Cisco Meraki documentation, we know that each organization can contain *networks*. So, similar to the previous API endpoint for organizations, there is one for networks: `/api/v1/organizations/{organizationId}/networks`. Between the curly braces, the `organizationID` must be replaced by the actual organization identifier.

This identifier is the most relevant attribute for each organization that you retrieved in [Example 10-2](#apis-curl-meraki-orgs-python). It is represented by the `id` key in each dictionary. Taking this ID, you can continue exploring the nested networks that belong to each organization. It’s interesting to notice the nested nature of this API, so you can’t list all the networks directly, but use the organizations they belong to as a reference. In [Example 10-3](#apis-curl-meraki-networks-python), the organization ID is used to retrieve the networks that belong to it.

##### Example 10-3. Retrieving Meraki networks with cURL

```
$ curl 'https://api.meraki.com/api/v1/organizations/573083052582915028/networks' \ 
  -H 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' \
  -L \
  | python3 -m json.tool

[
  {                                                                                
    "id": "L_573083052582989052",                                                  
    "organizationId": "573083052582915028",
    "name": "Long Island Office",
    "productTypes": [
      "appliance",
      "camera",
      "switch"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [
      "tag1",
      "tag2"
    ],
    "enrollmentString": null,
    "url": "https://n18.meraki.com/Long-Island-Offi/n/kWaHAbs/manage/usage/list",
    "notes": "Combined network for Long Island Office",
    "isBoundToConfigTemplate": false
  },
  # other networks removed for brevity
]
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The URL path contains the organization ID that limits the scope of the request to the networks belonging to that organization.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The response is a list of dictionaries, each representing a network. And in each dictionary, we can find each network’s attributes.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Similar to the previous organization’s example, the `id` key is used to uniquely identify the network.

Next, we continue exploring HTTP methods introduced in [“Understanding HTTP request types”](#apis-http-types). In particular, we’ll start with a method you can use to modify resources on the API: the POST.

#### Using the HTTP POST method to create a new resource

In [Example 10-3](#apis-curl-meraki-networks-python), you retrieved the networks belonging to a specific organization. Now, for the same organization, you want to create a new network ([Example 10-4](#apis-curl-meraki-create-network-python)).

##### Example 10-4. Creating a Meraki network with cURL

```
curl -X POST 'https://api.meraki.com/api/v1/organizations/573083052582915028/networks' \ 
  -H 'X-Cisco-Meraki-API-Key: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0' \
  -L \
  -d '{"name": "my new automated network", "productTypes": ["switch"]}' \                
  -H 'Content-Type: application/json' \                                                  
  | python3 -m json.tool

{
    "id": "N_573083052583237701",
    "organizationId": "573083052582915028",
    "productTypes": [
        "switch"
    ],
    "url": "https://n18.meraki.com/my-new-automated/n/mQ9KWds/manage/usage/list",
    "name": "my new automated network",
    "timeZone": "America/Los_Angeles",
    "enrollmentString": null,
    "tags": [],
    "notes": null,
    "isBoundToConfigTemplate": false
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The HTTP method to create new objects is `POST`, and it is specified with the `-X` flag. The POST method requires *data*.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

With the `-d` flag, or `--data`, we pass a JSON object with the attributes of the new network in the form of a key-value pair (`name` and `productTypes`).

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `Content-Type` header is used to specify the data format. In this case, we are using JSON, but other formats are also supported (e.g., XML).

###### Tip

Learning how to construct a proper API request requires becoming familiar with API documentation. The API documentation (the API definition and specs) defines what a given URL must be, the HTTP request type, headers, and what the body needs to be for a successful API call. For instance, in the previous example, we passed the required attributes for the POST request, but we could have also passed optional attributes, such as `timeZone` or `tags`. All these attributes are defined in the *API documentation*. Additionally, performing GET requests offers some hints of the required attributes, as you can see in the output of the `networks` `GET` (in [Example 10-3](#apis-curl-meraki-networks-python)) and the data used for the `POST`.

Now that you understand the principles of REST and HTTP, it’s important to also take note of non-RESTFul HTTP-based APIs.

### Understanding non-RESTful HTTP-based APIs

RESTful APIs are the most popular HTTP-based APIs, and other HTTP-based APIs are not compliant with REST principles. In the network industry, during the adoption of newer interfaces, such as RESTful ones, some APIs were built on top of CLIs, meaning that the API call actually sends a command to the device versus sending native structured data. Obviously, the preferred approach is to have any modern network platform’s CLI or web UI use the underlying API, but for legacy or preexisting systems that were built using commands, it is common to see the use of non-RESTful APIs, as it was easier to add an API this way rather than rearchitect the underlying system.

RESTful HTTP-based APIs and non-RESTful HTTP-based APIs have two major differences. RESTful APIs use particular verbs (e.g., GET, POST, PATCH, etc.) to dictate the type of change being requested of the target server. For example, in the context of networking, a configuration change would never occur if you’re doing an HTTP GET, since you’re simply retrieving data. However, systems that are HTTP based but do not follow RESTful principles could use the same HTTP verb for every API call. This means if you’re retrieving data or making a configuration change, all API calls could be using a POST request. Another common difference is that non-RESTful HTTP-based APIs always use the same URL and do not allow you to access a specific resource via a URL change. You can see both characteristics in [Example 10-5](#apis-curl-arista-run-command).

Within the non-REST HTTP-based APIs, there is one popular methodology, the RPC, which was available before the REST APIs become popular. An RPC is a simple calling to a function in a remote system, with a data payload containing a method, and some other attributes. Depending on how the data is codified, we could talk about XML-RPC or JSON-RPC. This command-and-action approach makes it more performant, but also more obscure in terms of predictability.

###### Note

Both types, REST and RPC, can coexist on the same API server, in different parts of the API, leveraging their benefits for different use cases. We will present more RPC use cases in [“Using NETCONF”](#apis-netconf) and [“Understanding gRPC”](#apis-grpc).

One example of a JSON-RPC API is the Arista eAPI. It offers an RPC endpoint (`/command-api`) to run CLI commands via the HTTP API. [Example 10-5](#apis-curl-arista-run-command) uses cURL again to request the execution of the CLI commands providing the proper JSON payload.

##### Example 10-5. Running CLI commands via the Arista eAPI

```
$ curl --insecure \
  -H "Content-Type: application/json" \
  -X POST \                                              
  -d '{"jsonrpc":"2.0", "method":"runCmds", "params":{ "version":1,
  "cmds":["show version"], "format":"text"}, "id":""}' \ 
  https://ntc:ntc123@eos-spine1/command-api \            
  | python3 -m json.tool

{
    "jsonrpc": "2.0",
    "id": "",
    "result": [
        {                                                
            "output": " vEOS\nHardware version:    \nSerial number:       \n
            System MAC address:  5254. 0097.1b5e\n\nSoftware image version:
            4.22.4M\nArchitecture:           i686\nInternal build version:
            4.22.4M-15583082.4224M\nInternal build ID:
            08527907-ec51-458e-99dd-e3ad9c80cbbd\n\nUptime:
            15 weeks, 4 days, 13 hours and 22 minutes\nTotal memory:
            2014520 kB\nFree memory:            1335580 kB\n\n"
        }
    ]
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We are using the POST method to retrieve data. As we’ve commented, in non-REST APIs, the method is not meaningful. Actually, with the same method, depending on the CLI commands passed, we could be retrieving the state or changing it.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

We define the *operation* to be executed remotely with the `method` (`runCmds`), and the `cmds` parameter, which contains a list of all the commands to be executed.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The authentication parameters (`ntc:ntc123@`) are passed in the URL that is equivalent to the standard HTTP `Authorization` header.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The `result` key contains the output of the command executed—in this case, the output of the `show version` command without any formatting, simply the raw text (i.e., what we get via an SSH CLI access).

###### Note

Alternatives to RESTful APIs other than RPC have appeared. For instance, GraphQL was published in 2015 by Facebook. It defines a data query language that simplifies the way data is consumed, allowing clients to define the structure/filtering of the data required, which will be served by the server. This approach reduces the amount of data transferred but can impede caching of the results. GraphQL is especially useful for retrieving data from an SoT, collecting the relevant data from one object (including nested resources). We dig into this in more detail in [Chapter 14](ch14.html#architecture).

As you start to use various types of HTTP-based APIs on network devices, keep in mind the following points:

- HTTP APIs can use XML or JSON for data encoding, but the device may implement only one or the other. The API’s author determines what gets supported.
- Tools such as cURL and Postman are helpful as you get started with APIs, but to write code to interact with HTTP APIs, you need a library that *speaks* HTTP, such as the Python Requests library or Go net/http package (covered in [“Using Network APIs for Automation”](#apis-aut_us_net_APIs)).
- Pay close attention to the HTTP verbs used when making configuration changes—using the wrong verb can have unintended consequences.
- You need to use API documentation to understand how to construct a proper API request. You’ll need the URL, headers, HTTP method, and body.

Now that we’ve introduced HTTP-based APIs, let’s shift our focus and introduce the NETCONF API.

## Using NETCONF

*NETCONF* is a network configuration management protocol, defined in [RFC 6241](https://oreil.ly/Bf8G4) and designed from the ground up for configuration management and for retrieving configuration and operational state data from network devices. In this respect, NETCONF has a clear delineation between configuration and operational state; API requests are used to perform operations such as retrieving the configuration state, retrieving the operational state, and making configuration changes.

###### Note

We stated in the previous section that RESTful APIs aren’t new; they are merely new for network devices and SDN controllers. As we transition to looking at the NETCONF API, it’s worth noting that NETCONF is also not new. NETCONF has been around for nearly two decades. In fact, it’s an industry-standard protocol with its original RFC published in 2006. It’s even been on various network devices for years, although often as a limited API rarely being used.

One of the core attributes of NETCONF is its ability to utilize various configuration data stores. Most network engineers are familiar with running configurations and startup configurations. These are thought of as two configuration files, but they are two configuration data stores in the context of NETCONF.

NETCONF implementations often tend to use a third data store called a *candidate configuration*. The candidate configuration data store holds configuration objects (CLI commands if you’re using CLI for configuration) that are not yet applied to the device. As an example, if you enter a configuration on a device that supports candidate configurations, they do not take action immediately. Instead, they are held in the candidate configuration and applied to the device only when a *commit* operation is performed. When the commit is executed, the candidate configuration is written to the running configuration.

Candidate configuration data stores have been around for years as originally defined in the NETCONF RFC almost two decades ago. One of the issues the industry has faced is having usable implementations of NETCONF that offered this functionality. However, not all implementations have been unused—​there have, in fact, been successful implementations. Juniper’s Junos OS has had a robust NETCONF implementation for years, along with the capability of a candidate configuration; more recently, other products from vendors such as Cisco, Huawei, and Nokia have adopted support for the candidate configuration data store.

###### Tip

Always check your hardware and software platforms, even if they are from the same vendor. The capabilities they support likely differ. The support of a candidate configuration is just one example.

We stated that with a candidate configuration, you enter various configurations, and they aren’t yet applied until a commit operation is performed. This leads us to another core attribute of NETCONF-enabled devices: configuration changes as a *transaction*. In our example, it means that all configuration objects (commands) are committed as a transaction. All commands succeed or are *not* applied. This is in contrast to the more common scenario of entering a series of commands and having a command somewhere in the middle fail, yielding a partial configuration.

Moreover, a unique feature of NETCONF (not available in any of the other interfaces) is the *network-wide* transaction. If a configuration change affects multiple devices—for example, provisioning a Layer 3 VPN (L3VPN) service end to end, updating the configuration of several network devices—all the changes need to succeed, or the whole operation is rolled back (which is called an *abort* phase).

The support of a candidate configuration and atomic transactions are just two features of NETCONF. Let’s take a deeper dive into the underlying NETCONF protocol stack.

### Learning the NETCONF protocol stack

Now we’ll tackle the four basic layers in NETCONF: the content representation, the operation types, the messages, and the supported transport protocols, as outlined in [Table 10-3](#apis-table-netconf-protocol-stack). We are going to review each and show concrete examples of what they mean for the XML object being sent between the client and server.

| Layer | Example |
| --- | --- |
| Content | XML representation of data models (YANG, XSD) |
| Operations | `get-config`, `get`, `copy-config`, `lock`, `unlock`, `edit-config`, `delete-config`, `kill-session`, `close-session`, `commit`, `validate`, `...` |
| Messages | rpc, rpc-reply, hello |
| Transport | SSHv2, SOAP, TLS, BEEP |

###### Note

NETCONF supports only XML for data encoding. On the other hand, remember that RESTful APIs *have the ability* to support JSON and/or XML.

#### Transport

NETCONF is commonly implemented using SSH as transport; it is its own SSH subsystem. While all of our examples use NETCONF over SSH, it is technically possible to implement NETCONF over SOAP, TLS, or any other protocol that meets the requirements of NETCONF.

A few of these requirements are as follows:

- It must be a connection-oriented session, and thus there must be a consistent connection between a client and a server.
- NETCONF sessions must provide a means for authentication, data integrity, confidentiality, and replay protection.
- Although NETCONF can be implemented with other transport protocols, each implementation *must* support SSH at a minimum.

###### Note

With the popularity of RESTful APIs, instead of further developing NETCONF over other protocols, the brand-new RESTCONF interface was created to implement NETCONF functionalities using REST principles. We cover this approach in [“Using RESTCONF”](#apis-restconf).

#### Messages

NETCONF messages are based on an RPC–based communication model, and each message is encoded in XML. Using an RPC-based model allows the XML messages to be used independent of the transport type. NETCONF supports three message types: `<hello>`, `<rpc>`, and `<rpc-reply>`. Viewing the actual XML-encoded object helps elucidate NETCONF, so let’s take a look at a NETCONF RPC request.

The `<hello>` message is sent by the NETCONF server when the connection is established, exposing its *capabilities*—the data models and the actions supported:

```
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.1</capability>
    <!-- rest of request as XML... -->
  </capabilities>
</hello>
```

###### Note

For a refresher on XML concepts, such as the XML namespace `xmlns`, see [Chapter 8](ch08.html#dataformats).

After the initial `<hello>`, the message types are always going to be `<rpc>` and `<rpc-reply>` and will always be the outermost XML tag in the encoded object:

```
<rpc message-id="101">
    <!-- rest of request as XML... -->
</rpc>
```

Every NETCONF `<rpc>` includes a required attribute called `message-id`. You can see this in the preceding example. It’s an arbitrary string the client sends to the server. The server reuses this ID in the response header so the client knows which message the server is responding to.

The other message type is `<rpc-reply>`. The NETCONF server responds with the `message-id` and any other attributes received from the client (e.g., XML namespaces):

```
<rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <data>
      <!-- XML content/response... -->
  </data>
</rpc-reply>
```

This `<rpc-reply>` example assumes that the XML namespace is in the `<rpc>` sent by the client. Note that the actual data response coming from the NETCONF server is embedded within the `<data>` tag.

Next, we’ll show how the NETCONF request dictates which particular NETCONF operation (RPC) it’s requesting of the server.

#### Operations

The outermost XML element is always the type of message being sent (e.g., `<rpc>` or `<rpc-reply>`). When you are sending a NETCONF request from the client to the server, the next element, or the child of the message type, is the requested NETCONF (RPC) operation. You saw a list of NETCONF operations in [Table 10-3](#apis-table-netconf-protocol-stack), and now we’ll take a look at some of them.

The two primary operations we review in this chapter are `<get>` and `<edit-config>`. The `<get>` operation retrieves running configuration and device state information:

```
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <!-- XML content/response... -->
  </get>
</rpc>
```

Since `<get>` is the child element within the `<rpc>` message, this means the client is requesting a NETCONF `<get>` operation.

Within the `<get>` hierarchy, optional filter types allow you to selectively retrieve a portion of the running configuration—namely, subtree and XPath filters. Our initial focus is on *subtree* filters, which allow you to provide an XML document, which is a subtree of the complete XML tree hierarchy that you wish to retrieve in a given request. Later, in [“Using ncclient with Cisco IOS XE”](#apis-ncclient-ios), we will use the *XPath* filter to inject the filter into the query path.

[Example 10-6](#apis-netconf-get-all-interfaces) references a specific XML data object by using the `<native>` element and the *http://cisco.com/ns/yang/cisco-ios-xe-native* URL. This data object is the XML representation of a specific data model that exists on the target device. This data model represents a full running configuration as XML, but in the example, we are requesting only the `<interface>` configuration hierarchy.

###### Note

As shown throughout this chapter, the actual JSON and XML objects sent can be based on either standard or vendor-specific models (often under the “native” tag).

The next two examples, for the `<get>` operation, are XML requests from a Cisco IOS XE device.

##### Example 10-6. NETCONF GET interfaces config

```
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
        <interface></interface>
      </native>
    </filter>
  </get>
</rpc>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The custom `xmlns`, under the Cisco custom domain, represents a vendor-specific data model.

###### Warning

In this edition of the book, we’ve updated the vendor model reference because the custom vendor data model changed. This may happen again in the future, so it’s necessary to always be aware of the supported capabilities.

You could add more elements to the filter’s XML tree to narrow the response that comes back from the NETCONF server. You will now add two elements to the filter—​so instead of receiving the configuration objects for all interfaces, you’ll receive the configuration of only `GigabitEthernet1`:

```
<filter type="subtree">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>1</name>
      </GigabitEthernet>
    </interface>
  </native>
</filter>
```

The next most common NETCONF operation is `<edit-config>`. This operation is used to make a configuration change. Specifically, this operation loads a configuration into the specified configuration data store: running, startup, or candidate. In [Example 10-7](#apis-netconf-edit-config-static-route), you add a static route to the running configuration.

##### Example 10-7. NETCONF `edit-config` to add a static route

```
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config> 
    <target>
      <running/>
    </target>
    <config>    
      <configuration>
        <routing-options>
          <static>
            <route>
              <name>0.0.0.0/0</name>
              <next-hop>10.1.0.1</next-hop>
            </route>
          </static>
        </routing-options>
      </configuration>
    </config>
  </edit-config>
</rpc>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `<edit-config>` operation is used, setting the target configuration data store with the `<target>` tag. If not specified, it’ll default to the *running* configuration.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Within the `<config>` element, we define the data-model hierarchy that we want to load onto the target data store. This structure is based on the NETCONF capabilities that are supported on a given platform.

###### Note

Vendors can implement platform-specific options. Juniper Junos OS, for example, offers options for `<edit-config>`. [Example 10-7](#apis-netconf-edit-config-static-route) uses `<config>`, and requires XML configuration objects for adding a static route to a Junos OS device. Junos OS also supports `<config-text>` within `<edit-config>`, which allows you to include configuration elements using text format (curly brace or set syntax).

The `<edit-config>` operation also supports an attribute called `operation` that provides more flexibility in the way a device applies the configuration object. When the `operation` attribute is used, it can be set to one of five values: `merge`, `replace`, `create`, `delete`, or `remove`. The default value is `merge`. If you wanted to delete the route from the previous example, you could use `delete` or `remove`; the difference is that an error occurs if you use `delete` when the object doesn’t exist. You could optionally use `create`, but an error is raised if the object already exists. Often `merge` is used for making configuration changes for this reason.

Finally, you could use the `replace` operation if you wanted to replace a given XML hierarchy in the configuration data object. In the static route example, you would use `replace` if you wanted to end up with *just* the default static route on the device; it would automatically remove all other configured static routes.

###### Note

If the `operation` options still seem a little confusing, don’t worry. Once we start exploring and automating devices using NETCONF later in this section, you’ll see even more examples that use various XML objects across device types for operations such as the NETCONF `merge` and `replace`.

We’ve shown what XML documents look like when using `<get>` and `<edit-config>`. The following list describes the other base NETCONF operations:

<get-config>Retrieves all or part of a specified configuration (e.g., running, candidate, or startup).

<copy-config>Creates or replaces a configuration data store with the contents of another configuration data store. Using this operation requires the use of a full configuration.

<delete-config>Deletes a configuration data store (note that the running configuration data store can’t be deleted).

<lock>Locks the configuration data-store system of a device being updated to ensure that no other systems (NETCONF clients) can make a change at the same time.

<unlock>Unlocks a previously issued lock on a configuration data store.

<close-session>Requests a graceful termination of a NETCONF session.

<kill-session>Forcefully and immediately terminates a NETCONF session.

This is not an exhaustive list of NETCONF operations, but rather the core operations that each device must support in a NETCONF implementation. NETCONF servers can also support extended operations such as `<commit>` and `<validate>`. To support extended operations like these, the device must support required dependencies called *NETCONF capabilities*.

The `<commit>` operation commits the candidate configuration as the device’s new running configuration. To support the `<commit>` operation, the device must support the `candidate` capability.

The `<validate>` operation validates the contents of the specified configuration (running, candidate, startup). Validation consists of checking a configuration for both syntax and semantics before applying the configuration to the device.

###### Tip

We’ve mentioned NETCONF capabilities twice already, so let’s give a bit more context. As you know now, NETCONF supports a base set of NETCONF RPC operations. These are defined by the device as NETCONF *capabilities*. NETCONF capabilities are exchanged between the client and the server during connection setup, and the capabilities supported are denoted by a URL/URI. For example, every device that supports NETCONF should support the base operation from the namespace: `urn:ietf:params:xml:ns:netconf:base:1.0`. Additional capabilities use the form `urn:ietf:params:netconf:capability:{name}:1.x`, where *`name`* is the name of the capability and the way it is usually identified (without the full namespace). When we start exploring the use of NETCONF from a hands-on perspective (in [Example 10-8](#apis-netconf-capabilities)), you’ll get to see all capabilities a given device supports.

#### Content

The last layer of the NETCONF protocol stack to understand is the *content*. This is the actual XML document that gets embedded within the RPC operation tag elements. We already showed examples of what the content could be for particular NETCONF operations.

In [Example 10-6](#apis-netconf-get-all-interfaces), you looked at the content that selectively requested configuration elements for the interfaces on a Cisco IOS XE device:

```
<native xmlns="http://cisco.com/ns/yang/cisco-ios-xe-native">
  <interface>
  </interface>
</native>
```

The most important point to understand about content is that it is the XML representation of a particular schema, or data model, that the device supports. We introduced schemas and data models in [Chapter 8](ch08.html#dataformats).

After this short introduction to the basic NETCONF concepts, you’re ready to start exploring what a real NETCONF API interaction looks like.

### Exploring NETCONF

As you learn new APIs, it’s advantageous to learn about associated tooling that allows you to learn the API without writing any code. You saw this with cURL when learning how to use HTTP-based APIs. For NETCONF, we are going to cover how to use an SSH client that creates an interactive NETCONF session. You’ll learn how to construct a proper NETCONF request while also seeing how the device responds to a given request, without writing any code.

###### Warning

Using an interactive NETCONF over SSH session as we do here is useful for *learning* and *exploring* the use of NETCONF, but it is also unintuitive, unfriendly, and fragile. For any use case outside of learning and experimentation (*especially* for those dealing with production infrastructure), you should instead use higher-level libraries and tools that we’ll explore later. These higher-level resources manage the minutiae of NETCONF operations and syntax much more effectively and predictably.

In the next two examples, we show you how NETCONF works on two platforms: Junos and Cisco IOS XE.

#### NETCONF with Junos

Let’s start with Juniper vMX running Junos as an example. You connect to the device via SSH on port 830, the default port number for NETCONF. To connect to the device, you’ll use a standard Linux `ssh` command:

```
$ ssh -p 830 ntc@vmx1 -s netconf
```

###### Note

Based on the vendor implementation, you may need to supply `-s netconf` as you SSH to the device. The `-s` denotes the SSH subsystem being used.

In [Example 10-8](#apis-netconf-capabilities), as soon as you connect and authenticate, the NETCONF server (the router) responds with a hello message that includes all of its supported NETCONF operations, capabilities, models/schemas, and a session ID.

##### Example 10-8. NETCONF `hello` response from server

```
<nc:hello xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <nc:capabilities>
    <nc:capability>urn:ietf:params:netconf:base:1.0</nc:capability>
    <nc:capability>urn:ietf:params:netconf:capability:candidate:1.0</nc:capability>
    <nc:capability>urn:ietf:params:netconf:capability:confirmed-commit:1.0</nc:capability>
    <--- output omitted for brevity --->
    <nc:capability>http://xml.juniper.net/netconf/junos/1.0</nc:capability>
    <nc:capability>http://xml.juniper.net/dmi/system/1.0</nc:capability>
  </nc:capabilities>
  <nc:session-id>77470</nc:session-id>
</nc:hello>
]]>]]>
```

All these capabilities announce what you could do with the device via the NETCONF interface.

Once you receive the server’s capabilities, the NETCONF connection setup process starts. The next step is to send our (client) capabilities. A capabilities exchange is required to be able to send any NETCONF requests to the server.

The `hello` object you’re going to send to the device to complete the capabilities exchange is the following:

```
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>http://xml.juniper.net/netconf/junos/1.0</capability>
  </capabilities>
</hello>
]]>]]>
```

Note the last six characters in the preceding XML documents: `]]>]]>`. These characters denote that the request is complete and can be processed. NETCONF supports two types of message separators, depending on the supported capabilities:

urn:ietf:params:netconf:base:1.0Structured as `]]>]]>` plus a newline. We use this separator in all the NETCONF examples with Junos, such as in [Example 10-8](#apis-netconf-capabilities).

urn:ietf:params:netconf:base:1.1This [chunked framing](https://oreil.ly/pwhqB) uses `<number>` and `#`. We use this separator in the examples in [“NETCONF with Cisco IOS XE”](#apis-netconf-iosxe).

However, the hello message always uses the `]]>]]>`, for backward compatibility.

###### Note

In an interactive NETCONF session, you need to explicitly use the separators; when you use a library, this low-level action is abstracted (and implicit).

As you start working with the SSH client, you’ll realize it’s not like a familiar interactive CLI, although it is an interactive session. No help menu or question mark help is available. There is no man page. It’s common to think something is broken or the terminal is frozen. It’s not. If you don’t get any errors after you copy and paste XML documents into the session terminal, things are likely going well. To break out of the interactive session, you need to press Ctrl-C on your keyboard—​there is no way to safely exit the interactive NETCONF session.

Once the client responds with its capabilities, you’re ready to start sending NETCONF requests. You can use a text editor to preconstruct your XML documents.

At this point, we’ve successfully connected to the device and exchanged capabilities, and we can now issue an actual NETCONF request. Our first example will query the device for the `fxp0` interface configuration. In [Example 10-9](#apis-netconf-get), we construct the XML document in a text editor and then copy and paste it into the interactive session.

##### Example 10-9. NETCONF GET operation in Junos

```
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <configuration>
        <interfaces>
          <interface>
            <name>fxp0</name>
          </interface>
        </interfaces>
      </configuration>
    </filter>
  </get>
</rpc>
]]>]]>
```

As soon as you hit Enter, the request is sent to the device. As presented in [Example 10-10](#apis-netconf-get-reply), you’d see the XML RPC reply from the device in near real time.

##### Example 10-10. NETCONF GET reply

```
<nc:rpc-reply xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"
  xmlns:junos="http://xml.juniper.net/junos/18.2R1/junos"
  message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <nc:data>
    <configuration xmlns="http://yang.juniper.net/junos/conf/root"
      junos:commit-seconds="1653021086"
      junos:commit-localtime="2022-05-20 04:31:26 UTC" junos:commit-user="ntc">
      <interfaces xmlns="http://yang.juniper.net/junos/conf/interfaces">
        <interface>
          <name>fxp0</name>
          <unit>
            <name>0</name>
            <description>MANAGEMENT_INTERFACE__DO_NOT_CHANGE</description>
            <family>
              <inet>
                <address>
                  <name>10.0.0.15/24</name>
                </address>
              </inet>
            </family>
          </unit>
        </interface>
      </interfaces>
    </configuration>
    <database-status-information></database-status-information>
  </nc:data>
</nc:rpc-reply>
]]>]]>
```

At this point, you may have successfully performed your first request to a network device via NETCONF and received a response. The point here isn’t to do anything with it, just as you didn’t do anything with data returned with cURL. The value is that you’ve tested and validated an XML request to retrieve the configuration for interface `fxp0`, and now know what the response looks like, to ease you into automating devices with Python or Go.

You’ve seen one example using NETCONF `<get>` operations to the device. Let’s take a look at one example introducing how to use the `<edit-config>` operation, which is used to make a configuration change.

To see the proper way to construct an XML request for a configuration change, you are going to first issue a `get` request, since that will show you the structure of the complete object that needs to get sent back to the device. This is similar to knowing different CLI commands in an operating system.

###### Note

This example uses a vendor-specific data model for the interfaces instead of the standard `urn:ietf:params:xml:ns:yang:ietf-interfaces` because the standard one is not available. It is not present in the output of [Example 10-8](#apis-netconf-capabilities).

In [Example 10-10](#apis-netconf-get-reply), you can notice how an interface (`fxp0`) is configured. If you remove the inner filter part, you could get the rest of the interfaces’ configurations. You can use the data structure used for the `fxp0` interface as the foundation to modify the configurations on other interfaces, to simplify the process.

Let’s make our first NETCONF configuration change by configuring the IP address of `192.0.2.1/24` on interface `ge-0/0/0`. To construct the object, you’ll extract the required data from your `get` request in [Example 10-10](#apis-netconf-get-reply). The two items you need to update are as follows:

- Your returned object in the `<data>` tag will get enclosed in a `<config>` tag when you want to make a configuration change using the NETCONF `<edit-config>` operation.
- The constructed object needs to specify a *target* data store (i.e., running, startup, or candidate) based on what the target node supports.

These changes result in the XML message in [Example 10-11](#apis-netconf-edit-config-interface).

##### Example 10-11. NETCONF `edit-config` to change IP and interface description

```
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <configuration xmlns="http://yang.juniper.net/junos/conf/root">
        <interfaces xmlns="http://yang.juniper.net/junos/conf/interfaces">
          <interface>
            <name>ge-0/0/0</name>
            <unit>
              <name>0</name>
              <description>Interface with changed IP</description>
              <family>
                <inet>
                  <address>
                    <name>192.0.2.1/24</name>
                  </address>
                </inet>
              </family>
            </unit>
          </interface>
        </interfaces>
      </configuration>
    </config>
  </edit-config>
</rpc>
]]>]]>
```

Once this XML document is built in a text editor, it can easily be copied and pasted into an active NETCONF session.

All the examples have been successful NETCONF operations so far, but the reality is that it could take a bit to get used to the XML syntax and the data models used in each platform. Luckily, NETCONF provides a useful error message to help you fix the problem. For instance, in [Example 10-11](#apis-netconf-edit-config-interface), you have targeted the *candidate* configuration data store to change. However, if you use another data store, such as *running*, the NETCONF operation will complain because it’s not expected to change it directly on this platform. It requires the use of the *commit* operation.

#### NETCONF with Cisco IOS XE

To complement the Junos NETCONF example, it’s interesting to see another NETCONF implementation—in this case, for Cisco IOS XE.

You establish the SSH NETCONF session, and receive the hello from the device, as in [Example 10-8](#apis-netconf-capabilities):

```
$ ssh -p 830 ntc@csr1 -s netconf
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
<capability>urn:ietf:params:netconf:base:1.1</capability>
<capability>http://tail-f.com/ns/netconf/actions/1.0</capability>
<capability>http://cisco.com/ns/cisco-xe-ietf-ip-deviation?...
  revision=2016-08-10</capability>
<capability>http://openconfig.net/yang/policy-types?...
  revision=2016-05-12</capability>
<capability>urn:ietf:params:xml:ns:yang:smiv2:RFC-1212?module=RFC-1212</capability>
<--- output omitted for brevity --->
```

All these capabilities announce what you could do with each device via the NETCONF interface. The first big difference, among platforms, is in the number of supported capabilities—there are many more in this case. This doesn’t mean that the first is less *capable* than the second. It means only that both support different data models and features.

It’s interesting to notice the different *organizations* being referenced in each output. As expected, both support the base IETF definitions for NETCONF operations, but each vendor has its own extensions. The Juniper one uses its own data models (`xml.juniper.net`), as does Cisco (`cisco.com` and `tail-f.com`). In this output, you can see that it also supports OpenConfig models (`openconfig.net`). And last, but not least, you can observe a lot of translated data models, from SMIv2 to YANG (defined in RFC 6643), to make available the same structure data used in SNMP, via NETCONF. We talk about the data models’ definitions in [“Comparing NETCONF, RESTCONF, and gNMI”](#apis-comparing-data-model-interfaces).

In this case, you will send a hello message announcing your intention to use `base:1.1` (which you did not use in the previous NETCONF examples with Junos) because it allows the chunked framing delineator that is the only one supported in this platform:

```
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
        <capability>urn:ietf:params:netconf:base:1.0</capability>
        <capability>urn:ietf:params:netconf:base:1.1</capability>
    </capabilities>
</hello>
]]>]]>
```

To run a `get-config` operation, you target the *source* data store and use the chunked framing delineator before and after the message (the number is arbitrary):

```
#200
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <get-config>
    <source>
      <running/>
    </source>
  </get-config>
</rpc>
##
```

This code outputs the full *running* configuration in XML format. You could apply filters to narrow the desired data.

###### Tip

We’ve stated this a few times already, but we’re going to restate it because it’s extremely important. As you get started using APIs, you need to know how to construct the proper request object. This is often challenging as you get started, but the hope is you can find *easy* ways to help figure out how to build these objects. This help could come from API documentation, tooling built to interface with the underlying schema definitions files such as XSDs or YANG modules, or even CLI commands on the device. For example, Cisco Nexus and Juniper Junos OS have CLI commands that show you exactly what the XML document needs to be for a given request.

As we wrap up the NETCONF section to move to other network management interfaces, keep in mind that NETCONF uses only XML encoding and SSH transport (you’re going to find different options next), and it supports data-model-based operations like the other interfaces.

After this deep dive into NETCONF, let’s continue with its *cousin*, RESTCONF.

## Using RESTCONF

In [“Getting Familiar with HTTP-Based APIs”](#apis-http-apis), we explained how popular REST APIs work, and afterward, in [“Using NETCONF”](#apis-netconf), we presented the benefits of exposing network management operations based on data models. The network automation community’s demand to bring both together should not come as a surprise. The answer was RESTCONF, defined in [RFC 8040](https://oreil.ly/Lnv9Y), which has been adopted by many NOSs.

Adhering to REST principles implies some limitations and simplifications compared to NETCONF:

- RESTCONF doesn’t support network-wide transactions because it requires stateful communications. So, the clients should manage failure scenarios in the system-by-system interactions.
- RESTCONF drops the data-store concept; only a single data store exists, equivalent to the *running* one.
- No locking operation is supported.

###### Warning

Don’t consider NETCONF and RESTCONF as mutually exclusive; the truth is almost the opposite. Devices can provide both interfaces relying on the same backend functionalities, so it’s up to the client to choose the most convenient one for particular use cases. However, dual interaction could lead to compatibility issues. For instance, locking a data store via NETCONF and accessing it via RESTCONF will raise an error.

As it’s a combination of REST APIs and NETCONF concepts, RESTCONF assembles characteristics from both. RESTCONF uses HTTP with the standard requests: GET, PUT, PATCH, POST, and DELETE, corresponding to some NETCONF operations, as you can see in [Table 10-4](#apis-restconf-to-netconf).

| `RESTCONF` | `NETCONF` |
| --- | --- |
| `GET` | `<get>/<get-config>` |
| `POST` | `<edit-config>>` (`nc:operation="create"`) |
| `PUT` | `<edit-config>>` (`nc:operation="create/replace"`) |
| `PATCH` | `<edit-config>>` (`nc:operation`, depends on the content) |
| `DELETE` | `<edit-config>>` (`nc:operation="delete"`) |

RESTCONF supports JSON *and* XML encoding. As the network developer, you have the choice to work with whichever data format you prefer. The structure of the content data is defined using YANG models, like NETCONF.

### Exploring RESTCONF in Cisco IOS XE

As in [“Exploring HTTP-based APIs with cURL”](#apis-explore-http-api), you’ll continue using cURL to explore RESTCONF because it’s just another REST API. In this section, we use the Cisco IOS XE platform to demonstrate basic RESTCONF interaction. Similar to NETCONF, you may need to activate the RESTCONF interface in your network device, if it’s supported.

###### Tip

A great resource to extend your knowledge about RESTCONF is the [Cisco DevNet learning tracks](https://oreil.ly/mXCrl). You will also find content about the other interfaces covered in this chapter.

Before getting started, you can use a well-known path (`/.well-known/host-meta`) to discover the RESTCONF path within the API:

```
$ curl https://csr1/.well-known/host-meta -k -u 'ntc:ntc123' 

<XRD xmlns='http://docs.oasis-open.org/ns/xri/xrd-1.0'>      
    <Link rel='restconf' href='/restconf'/>
</XRD>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `-u` (or `user`) cURL argument provides the user and password for Basic authentication. In Basic authentication, the user and password are sent in clear text over the network (Base64 encoded), so it’s not a recommended method for production.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

By default, the API returns the response in XML. Remember, you could change this behavior by using the HTTP `Accept` header.

###### Warning

A Base64-encoded string does *not* mean it has been encrypted. You can easily encode and decode Base64-encoded strings with Python using the `base64` BY Python module:

```
>>> import base64
>>>
>>> encoded = base64.b64encode('ntc:ntc123')
>>> encoded
'bnRjOm50YzEyMw=='
>>>
>>> text = base64.b64decode(encoded)
>>> text
'ntc:ntc123'
>>>
```

Now, knowing that the RESTCONF API is located at `/restconf`, you are ready to start exploring it:

```
$ curl -k -X GET https://csr1/restconf \
    -H 'Accept: application/yang-data+json' \ 
    -u 'ntc:ntc123'

{
  "ietf-restconf:restconf": {
      "data":{},                              
      "operations":{},                        
      "yang-library-version":"2016-06-21"
  }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Using the `Accept` header with `application/yang-data+json`, the response comes in JSON format instead of the default XML.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `data` path will contain all data resources.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `operations` path will include the data-model-specific operations.

Then, similar to NETCONF, you can discover the *capabilities* offered via the RESTCONF interface. In [Example 10-8](#apis-netconf-capabilities), you can target the path `/restconf/data/netconf-state/capabilities` to obtain the very same list you got in [“NETCONF with Cisco IOS XE”](#apis-netconf-iosxe):

```
$ curl -k -X GET https://csr1/restconf/data/netconf-state/capabilities \
    -H 'Accept: application/yang-data+json' \
    -u 'ntc:ntc123'

{
  "ietf-netconf-monitoring:capabilities": {
    "capability": [
      "urn:ietf:params:netconf:base:1.0",
      "urn:ietf:params:netconf:base:1.1",
      "http://cisco.com/ns/yang/Cisco-IOS-XE-native?module=Cisco-IOS-XE-native&
        revision=2019-11-01", 
      # output omitted for brevity
    ]
  }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This model contains all the Cisco IOS XE native configuration models.

In [Example 10-12](#apis-restconf-get-config), we explore `Cisco-IOS-XE-native:native` under the `/restconf/data/` path.

##### Example 10-12. GET configuration with RESTCONF

```
$ curl -k -X GET https://csr1/restconf/data/Cisco-IOS-XE-native:native \
    -H 'Accept: application/yang-data+json' \
    -u 'ntc:ntc123'

{
  "Cisco-IOS-XE-native:native": {
    "version": "17.1",
    "memory": {
      "free": {
        "low-watermark": {
          "processor": 72107
        }
      }
    },
    # output omitted for brevity
  }
}
```

The next subsections explore the RESTCONF API in more detail, including updating the configuration (with PATCH and PUT operations) and executing operations.

#### Updating configuration via RESTCONF

As in any other REST API, you can change the content of the API via POST, PATCH, PUT, and DELETE operations. In this case, you want to add two OSPF network statements to an existing OSPF configuration, so the PATCH operation will allow updating it starting from the current state.

As we’ve already said, when dealing with APIs, you need to know the expected data model structure that the API can understand. You can check the data model specification from the announced capabilities, but it’s quicker to explore the data model with a GET operation (as in [Example 10-12](#apis-restconf-get-config)). In the previous output, you got the full configuration, but to check a specific section, you can append it to the previous path. For instance, by adding `router/` to the previous path, you get *only* the `router` section that contains the OSPF current configuration:

```
"router": {
  "Cisco-IOS-XE-ospf:router-ospf": {
    "ospf": {
      "process-id": [
        {
          "id": 10,
          "network": [
            {
              "ip": "192.0.2.0",
              "wildcard": "0.0.0.7",
              "area": 0
            },
            {
              "ip": "192.0.2.64",
              "wildcard": "0.0.0.7",
              "area": 0
            }
          ],
          "router-id": "192.0.2.1"
        }
      ]
    }
  }
}
```

Now, in [Example 10-13](#apis-restconf-patch), we request a PATCH operation with the data payload containing two new networks to update the OSPF configuration.

##### Example 10-13. RESTCONF PATCH to add OSFP statements

```
$ curl -k
    -X PATCH "https://csr1/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf" \ 
    -H 'Content-Type: application/yang-data+json' \
    -H 'Accept: application/yang-data+json' \
    -u 'ntc:ntc123' \
    -d $'{
  "router-ospf": {
    "ospf": {
      "process-id": [
        {
          "id": 10,                                                                       
          "network": [
            {
              "ip": "192.0.2.128",
              "wildcard": "0.0.0.7",
              "area": 0
            },
            {
              "ip": "192.0.2.192",
              "wildcard": "0.0.0.7",
              "area": 0
            }
          ]
        }
      ]
    }
  }
}'
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We target the `router-ospf` leaf in the URL path.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `process-id` is the same as the previous one (`10`), so it will append the new networks to the existing ones. We can check it by repeating the previous GET operation, and it would show the four OSPF networks.

If instead of PATCH you use the PUT method, the whole `router-ospf` will be replaced by the new one. This method allows much more efficient configuration management than traditional CLI configuration. In the CLI, adding configurations is trivial. However, removing or negating commands is complex. For example, what if you have a single instance of OSPF running with 50 network statements, but because of a change in design, you need only 2 network statements? You will have to know which 48 statements need to be negated with a `no` command. This process is arduous and mundane as you extrapolate the effort for all types of configurations on a network device. For our example, wouldn’t it be easier to take the opposite approach—focus on the configuration that *should* exist on the network device? This is a growing trend, becoming more possible thanks to newer APIs and ways of thinking. This is called *declarative configuration*.

###### Note

In [“Updating configuration via RESTCONF with net/http”](#apis-go-http-put), you can see an example of using the HTTP PUT method to update the configuration.

#### Understanding the YANG PATCH HTTP operation

Following REST principles, RESTCONF comes with two limitations when compared to NETCONF. First, HTTP calls should not carry the state in between, so a transaction is limited to one HTTP call. Second, an HTTP request implements one type of create, read, update, and delete (CRUD) operation specified by the HTTP method (e.g., GET or POST). The second limitation can be overcome by a new `YANG PATCH` HTTP media type that allows combining various operation types on the same HTTP request.

Before you start using it, you need to validate that the feature (i.e., `urn:ietf:params:restconf:capability:yang-patch:1.0`) is supported in the target platform. You can look for this capability in the `restconf-state/capabilities` endpoint:

```
$ curl -k -X GET \
    https://csr1/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities \
    -H 'Accept: application/yang-data+json' \
    -u 'ntc:ntc123'

{
  "ietf-restconf-monitoring:capabilities": {
    "capability": [
      # output omitted for brevity
      "urn:ietf:params:restconf:capability:yang-patch:1.0", 
    ]
  }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Notice the `yang-patch` capability listed under the `restconf-state/capabilities` endpoint.

To illustrate how YANG PATCH works, you will manage loopback interfaces, adding and removing them. With YANG PATCH, you will first create a `Loopback0`, and in a second request, you will remove it and add a new `Loopback1`.

In [Example 10-14](#apis-restconf-yang-patch-xml-1), you have the YANG PATCH payload necessary to create a new `Loopback0` interface. Remember, you need to know the expected data structure for the `value` before.

##### Example 10-14. YANG PATCH with one operation

```
<yang-patch xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-patch">
  <patch-id>add-Loopback0-patch</patch-id> 
  <edit>                                   
    <edit-id>edit1</edit-id>
    <operation>create</operation>          
    <target>/Loopback=0</target>           
    <value>                                
        <Loopback xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <name>0</name>
        </Loopback>
    </value>
  </edit>
</yang-patch>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Unique ID to identify the YANG PATCH request.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

A YANG PATCH is an *ordered* list of edits, each one with an identifier (`edit-id`).

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The type of operation: `create`, `delete`, `insert`, `merge`, `move`, `replace`, or `remove`.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Specifies the target node the operation targets.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

This is optional (for example, a `move` operation doesn’t need it), but for a `create` operation, it is the content to be *created* in the target.

Then, you can use this data payload with an HTTP PATCH operation with a special `Content-Type`, `application/yang-patch+xml`. The `@` specifies using a file instead of a data payload directly:

```
$ curl -k -X PATCH "https://csr1/restconf/data/Cisco-IOS-XE-native:native/interface" \
    -H 'Content-Type: application/yang-patch+xml' \
    -H 'Accept: application/yang-data+xml' \
    -u 'ntc:ntc123' \
    -d '@create-loopback-0.xml'

<yang-patch-status xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-patch">
  <patch-id>add-Loopback0-patch</patch-id>
  <ok/>
</yang-patch-status>
```

###### Note

Remember that YANG PATCH is not an HTTP method but a media type.

[Example 10-14](#apis-restconf-yang-patch-xml-1) helps you understand the key parts of the YANG PATCH media type, but a single operation can be done without this special type. In [Example 10-15](#apis-restconf-yang-patch-xml-2), we add a new interface, `Loopback1`, and remove the previous one, `Loopback0`, in the same HTTP request.

##### Example 10-15. YANG PATCH with two operations

```
<yang-patch xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-patch">
  <patch-id>add-remove-loopback-patch</patch-id>
  <edit>
    <edit-id>edit1</edit-id>
    <operation>create</operation>
    <target>/Loopback=1</target>
    <value>
        <Loopback xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <name>1</name>
        </Loopback>
    </value>
  </edit>
  <edit>
    <edit-id>edit2</edit-id>
    <operation>remove</operation>
    <target>/Loopback=0</target>
  </edit>
</yang-patch>
```

###### Tip

The order of the operations within a YANG PATCH payload is not relevant. What is important is the final configuration outcome state and its behavior as an atomic transaction, for one single device. Either *all* the operations work well or the whole set of changes is rejected.

The YANG PATCH media supersedes all HTTP methods. This means that you could concentrate all your CRUD operations via YANG PATCH if you wish.

#### Discovering RESTCONF operations

RESTCONF, like NETCONF, supports managing modeled *data* but also running *operations*. You can list the supported operations in the `/restconf/operations` path:

```
$ curl -k -X GET https://csr1/restconf/operations \
    -u 'ntc:ntc123'  \
    -H 'Accept: application/yang-data+json' \
    | python3 -m json.tool

{
    "ietf-restconf:operations": {
        "Cisco-IOS-XE-rpc:factory-reset":                  
          "/restconf/operations/Cisco-IOS-XE-rpc:factory-reset",
        "ietf-event-notifications:establish-subscription": 
          "/restconf/operations/ietf-event-notifications:establish-subscription",
        "ietf-event-notifications:create-subscription":    
          "/restconf/operations/ietf-event-notifications:create-subscription",
        # output omitted for brevity
    }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Notice the various *sources*. Some are vendor specific, defined by Cisco in this case.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Other operations are defined by the IETF.

With this, we conclude the exploration of the RESTCONF interface. In [“The Go net/http Package”](#apis-go-http), we will come back to RESTCONF, but will use the Go net/http package to automate it. After NETCONF and RESTCONF, it’s time to explore another network management interface: gNMI.

## Using gRPC and gNMI

The gRPC Network Management Interface (gNMI) is, as its name indicates, a network management interface built on top of gRPC. It tries to overcome some limitations seen in the network management space, from SNMP to NETCONF, solving the two network management goals—configuration management and state retrieval—in a data-model-oriented way. Like NETCONF or RESTCONF, gNMI is a data model interface. However, it has characteristics that make it different:

- It uses gRPC as the transport protocol, instead of SSH or HTTP, and protobuf for encoding.
- It is defined and maintained by the OpenConfig consortium, led by Google. In contrast, NETCONF and RESTCONF are IETF standards.

gNMI is an alternative to other network management protocols that has gained popularity because of a fast initial development, and a capable and simple feature set. Most popular NOSs support it: Nokia Service Router Operating System (SROS) and SR Linux; Cisco IOS XR, IOS XE, and NX-OS; Arista EOS; Junos OS; and SONiC. We compare gNMI and the other data model interfaces in more detail in [“Comparing NETCONF, RESTCONF, and gNMI”](#apis-comparing-data-model-interfaces).

Complementary to gNMI, the [gRPC Network Operations Interface (gNOI)](https://oreil.ly/tzy4x), defines operational commands on network devices (e.g., ping or reboot). We don’t cover gNOI in this book, but it follows the same principles as gNMI.

But before getting into the gNMI capabilities, we need to introduce the framework that makes it possible: gRPC.

### Understanding gRPC

*gRPC* (initially called *Stubby*) was created by Google and evolved into a public project within the [CNCF](https://www.cncf.io). Before getting into the characteristics of gRPC, let’s understand the motivations behind its creation.

Google’s application stack is built around distributed microservices. Each application can be implemented in a different programming language and requires high performing communications to execute RPC operations. gRPC was designed to support these requirements by being useful in multiple environments, including intra-data-center and end-user applications. gRPC offers low latency and extensibility to add extra features, such as load balancing or tracing.

gRPC design embraces [several principles](https://oreil.ly/q_lBT), and the following are a few of the most significant ones:

High performanceFast and efficient communication between services is one core principle of gRPC design. For example, one significant change versus REST APIs is the use of static paths instead of dynamic ones. Dynamic paths include query parameters that need to be parsed before processing the call, which makes it slower and more complex. In gRPC, everything is part of the message body.

Payload agnosticThe framework supports multiple content types for data serialization and encoding, such as Protocol Buffers, JSON, and XML. Because of the high-performance requirement, the most common one is Protocol Buffers. In this section, we will use this data format, introduced in [Chapter 8](ch08.html#dataformats).

Several communication patternsgRPC allows various communication patterns, from traditional request/response (*unary*) to unidirectional and bidirectional streaming. Also, it can work in asynchronous or synchronous mode to enable scalability and streaming processing.

Language independentgRPC clients and servers can be built in multiple popular languages, such as Python and Go, and also in cross-platform environments. In [“A gRPC example”](#apis-grpc-example), we demonstrate this by implementing the client in Python, and the server in Go.

You can extend your gRPC knowledge at [*https://grpc.io*](https://grpc.io).

Using gRPC as a transport protocol brings a lot of flexibility. It works over TCP without a predefined port—the port is defined by each application. Also, it comes without any predefined calls and messages. It’s up to each application to define them. You will see a specific implementation for network management in [“Understanding the gNMI interface”](#apis-gnmi).

The best way to understand a protocol like gRPC is via an example, so let’s dig in.

### A gRPC example

[Figure 10-3](#apis-figure-grpc-example) shows a gRPC service example using a Python client and a Go server. The gRPC service is defined by the protobuf file from [Example 8-12](ch08.html#dataformats-protobuf-full-definition). All the files for these examples are located at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis/grpc*](https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis/grpc).

![npa2 1003](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1003.png)

###### Figure 10-3. gRPC communication

The protobuf file (*networkstuff.proto*, defined in [Chapter 8](ch08.html#dataformats)) contains the definition of the `messages` (the data types) and the `service` (the RPC operation). The only addition in comparison to [Example 8-12](ch08.html#dataformats-protobuf-full-definition) is the `option go_package = "./networkstuff";` to enable auto-generation of code for Go.

#### Running a gRPC server in Go

One key feature of gRPC is its ability to create code bindings from the protobuf definition. This means that the messages and services will be transformed into type structures and functions, respectively. In the directory, the files have been autogenerated, so you don’t need to do it. The only Go file manually defined is *server.go*; the rest of Go files in the folder are autogenerated by the protobuf compiler.

###### Note

To autogenerate gRPC bindings, you need to install the protocol buffer compiler. The installation for various platforms is described at [*https://oreil.ly/1NtLG*](https://oreil.ly/1NtLG).

We define and initialize a new Go module, `grpc_example`, that uses the autogenerated module `networkstuff`. The *server.go* file (part of the `grpc_example` module) uses the generated bindings to expose the gRPC service, which we analyze here in three parts.

[Example 10-16](#apis-grpc-go-1) contains the beginning of the *server.go* file that will perform as the gRPC server.

##### Example 10-16. gRPC Go *server.go*, part 1

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "net"

    // implementation of gRPC for Go maintained by Google
    "google.golang.org/grpc"

    // our own package that was built before, and updated to point
    // to ./networkstuff via a replacement in the go.mod file
    pb "github.com/pkg/networkstuff"
)

// custom struct extending the pb.RouterServiceServer plus a
// local cache of Routers
type routerServiceServer struct {
    pb.UnimplementedRouterServiceServer
    localRouters []*pb.Router
}

// method necessary to match the interface definition for
// pb.RouterServiceServer, with the same signature
func (s *routerServiceServer) GetRouter(ctx context.Context,
    router_request *pb.RouterRequest) (*pb.Router, error) {
    // Use the local cache of Routers to match by the
    // router identifier
    for _, router := range s.localRouters {
        if router.Id == router_request.Id {
            return router, nil
        }
    }
    // No router was found, return a nameless router
    return &pb.Router{}, nil
}

// -> continues to part 2
```

The first part of the file contains the necessary imports, with special attention given to `grpc` and `networkstuff`. Then, the file defines the `routerServiceServer` struct, which is implementing the `RouterServiceServer` interface (from *networkstuff_grpc.pb.go*), plus a list of `Routers` objects to serve as a poor-man data store. The `GetRouter` method is required by the `interface` ([Chapter 7](ch07.html#go) provides more details about implementing struct interfaces), and it returns the corresponding element from the `localRouters` list.

###### Note

The gRPC package is part of Go included packages at [*https://oreil.ly/7LeGx*](https://oreil.ly/7LeGx), but it can also be found at [*https://oreil.ly/WTNma*](https://oreil.ly/WTNma).

Continuing with the *server.go* file, [Example 10-17](#apis-grpc-go-2) includes a `server` variable with all the data that the gRPC server will serve. The data could have been loaded from an external database or a JSON file, but we decided to directly initialize the objects.

##### Example 10-17. gRPC Go *server.go*, part 2

```
// -> comes from part 1
// server contains the data to expose via grpc
var server = &routerServiceServer{
    localRouters: []*pb.Router{
        &pb.Router{
            Id:       1,
            Hostname: "Router A",
            Interfaces: []*pb.Interface{
                &pb.Interface{
                    Id:          1000,
                    Description: "Gi 0/0/0",
                },
                &pb.Interface{
                    Id:          1001,
                    Description: "Gi 0/0/1",
                },
            },
        },
  // omitted for brevity
  },
}
// -> continues to part 3
```

Finally, in [Example 10-18](#apis-grpc-go-3), a new TCP socket is defined and initialized to start serving TCP connections.

##### Example 10-18. gRPC Go *server.go*, part 3

```
// -> comes from part 2

func main() {
    // Create a TCP server listener in 50051 port
    lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", 50051))
    // This is the common Go Pattern to handle errors
    if err != nil {
        log.Fatalf("failed to listen: %v", err)
    }
    // Bootstrap a gRPC server with defaults
    var opts []grpc.ServerOption
    grpcServer := grpc.NewServer(opts...)

    // Register the custom RouterServiceServer implementation to
    // the gRPC server
    pb.RegisterRouterServiceServer(grpcServer, server)
    // Attach the gRPC server to the TCP port 50051 opened before
    // to start serving requests.
    grpcServer.Serve(lis)
}
```

With the *server.go* file ready, you can start the gRPC server and move to another terminal while the server is listening for gRPC connections:

```
ch10-apis/grpc$ go run server.go
```

#### Running a gRPC client in Python

gRPC can generate code bindings in multiple languages, so to complete the gRPC example, you will use Python to run the client gRPC requests. First, as we did for Go, it’s necessary to autogenerate the Python bindings with the libraries `grpcio` and `grpcio-tools`. Using these libraries, we already generated the Python files that are available in the examples located at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis/grpc*](https://github.com/oreilly-npa-book/examples/tree/v2/ch10-apis/grpc).

In [Example 10-19](#apis-grpc-python-client), we demonstrate in the Python interpreter how to use the generated gRPC code to establish a client request toward the gRPC server (running in the other terminal).

##### Example 10-19. Python gRPC client usage

```
>>> import grpc                                        
>>> import networkstuff_pb2_grpc as pb2_grpc           
>>> import networkstuff_pb2 as pb2                     
>>> channel = grpc.insecure_channel("localhost:50051") 
>>> stub = pb2_grpc.RouterServiceStub(channel)         
>>> router_request = pb2.RouterRequest(id=1)           
>>> result = stub.GetRouter(router_request)            
>>> type(result)
<class 'networkstuff_pb2.Router'>
>>> result                                             
id: 1
hostname: "Router A"
interfaces {
  id: 1000
  description: "Gi 0/0/0"
}
interfaces {
  id: 1001
  description: "Gi 0/0/1"
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Imports the `grpc` library and the autogenerated bindings from the protobuf.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Establishes a `grpc` *insecure* channel (a TCP connection) without certificate validation.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Defines a `stub` (a single gRPC client on top of the TCP connection) by using the protobuf specification.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Creates a proper request by using the protobuf specs embedded in a Python class and the `id` of the router to check.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

Using the `stub` and the `router_request`, we can call the predefined `GetRouter` method.

![6](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/6.png)

Finally, we check that the response serialized with the protobuf specs and is of type `Router`.

We leave to you the exercise to create other gRPC requests, with existing IDs (`id=2`) or with nonexistent ones, to see how the client behaves. The expectations are to get Router B, or an empty router for another ID.

After this quick overview of gRPC, we start digging into the gNMI interface, which uses gRPC for network management.

### Understanding the gNMI interface

*gNMI* defines a small set of gRPC operations: `CapabilityRequest`, `GetRequest`, `SetRequest`, and `SubscribeRequest`. These operations are defined in the *gnmi.proto* file, which is part of the OpenConfig project and can be found at [*https://oreil.ly/pul-l*](https://oreil.ly/pul-l).

In [“Comparing NETCONF, RESTCONF, and gNMI”](#apis-comparing-data-model-interfaces), we dive into the differences between gNMI versus NETCONF and RESTCONF, but all these data-model-oriented interfaces share a lot of similarities, as you can see in [Table 10-5](#apis-gnmi-netconf-operations), which compares the NETCONF and gNMI basic operations. More details about available gNMI operations can be found at the [gNMI specification documentation](https://oreil.ly/nc9Tm).

| `gNMI` | NETCONF |
| --- | --- |
| `CapabilityRequest` | `hello` |
| `GetRequest` | `get/get-config` |
| `SetRequest` | `edit-config` |
| `SubscribeRequest` | `establish-subscription` |

gNMI has gained a lot of popularity in the industry because of the open source contributions by the OpenConfig consortium (mostly by Google), and in the observability realm because it provided the first implementation of dial-in streaming telemetry. You’ll learn more about this in [“Understanding model-driven telemetry”](#apis-model-driven-telemetry).

After this short introduction to gNMI, let’s get hands-on and explore it.

### Exploring gNMI with gNMIc

To explore gNMI, you will use the gNMIc CLI client. This open source client has been adopted under the OpenConfig umbrella and can be found at [*https://oreil.ly/d343N*](https://oreil.ly/d343N).

###### Note

In this section, you use the gNMIc CLI version, but in [“The OpenConfig gNMIc Go Package”](#apis-gnmic-go), you will use the base Go package to create network automation scripts for interacting with gNMI.

First, you need to install `gNMIc`. You can use a downloaded bash script for macOS or Linux (or you could use gNMIc as a Docker container). For more information, check [*https://gnmic.openconfig.net/install*](https://gnmic.openconfig.net/install); here’s the command:

```
$ bash -c "$(curl -sL https://get-gnmic.openconfig.net)"
```

We use an Arista switch to explore gNMI. Because there is no standard TCP port for gNMI, the first thing to double-check is the TCP port being used (you can check it in the platform documentation or directly on the platform settings). The default port for Arista is TCP/6030, but you can change it if necessary.

Then, in [Example 10-20](#apis-gnmi-capabilities), you can check which data models are supported behind the gNMI interface, using the `CapabilityRequest` operation (`capabilities`), equivalent to the NETCONF `hello`.

##### Example 10-20. gNMI capabilities

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123 --insecure capabilities
gNMI version: 0.7.0
supported models:
  - openconfig-network-instance-types, OpenConfig working group, 0.9.3
  - iana-if-type, IANA,
  - openconfig-vlan, OpenConfig working group, 3.2.1
  - arista-vlan-deviations, Arista Networks <http://arista.com/>, 1.0.2
  - ietf-yang-types, IETF NETMOD (NETCONF Data Modeling Language) Working Group,
  // omitted models for brevity
supported encodings:
  - JSON
  - JSON_IETF
  - ASCII
```

[Example 10-20](#apis-gnmi-capabilities) introduces two important topics to discuss:

Supported data modelsThe supported data models define what can be changed/retrieved from the network device. In the output, you can notice data models coming from standards bodies (IANA and IETF), the OpenConfig consortium, and the vendor itself. Also, notice the versioning, relevant to understand the status of its definition.

Supported encodingThis is the encoding of the payload (not the transport encoding, which is protobuf). It supports JSON and JSON_IETF (to support some serialization of YANG models), which allow structured data. It also supports ASCII encoding, used for semistructured CLI configuration, depending on the gNMI backend implementation.

You can find more information about these two topics at the [gNMI specification on GitHub](https://oreil.ly/YxUnw).

#### gNMI GetRequest

Once you know the interface capabilities, you can do your first gNMI `Get` operation. You can retrieve the actual configuration state from the running configuration, targeting the `config` container in an OpenConfig data model: `/interfaces/interface/config`. gNMI paths are a simplified variant of the XPath syntax. These paths can be obtained by observing the YANG data models or by using tools to extract paths from them—e.g., [Cisco YANG Suite](https://oreil.ly/WlojA).

###### Note

OpenConfig and IETF advocated for different styles of data model organization. In OpenConfig, a model node has two containers, *config* and *state*, to represent the intended and the operational state, respectively. In contrast, The IETF proposed to split both configurations into different data stores. There is more information in Rob Shakir’s blog post [“OpenConfig and IETF YANG Models: Can they converge?”](https://rob.sh/post/215/).

In [Example 10-21](#apis-gnmic-get-interfaces-config), the configuration contains only a few *leaves* (`mtu`, `name`, and `type`), because only a few items are configured (the defaults are not shown). This is something that depends on each data-model specification.

##### Example 10-21. Get config interface with gNMIc

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123 --insecure  --gzip \
    get \
    --path '/interfaces/interface/config'

[
  {
    "source": "eos-spine1:6030",
    "timestamp": 1664428366933949209,
    "time": "2022-09-29T05:12:46.933949209Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Management0]/config",
        "values": {
          "interfaces/interface/config": {
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Management0",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      }
    ]
  }
]
```

###### Tip

In this example, you see only one interface, `Management0`. If more were present, you could get the same behavior using XPath (filtering by the interface name) and target this specific interface with the path `interfaces/interface[name=Management0]/config`.

Now, instead of targeting the *config* container, we target the *state* one. Besides the interface configuration (with default values), the interface stats will be returned:

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123 --insecure --gzip \
    get \
    --path '/interfaces/interface/state'
[
  {
    "source": "eos-spine1:6030",
    "timestamp": 1664428346403170400,
    "time": "2022-09-29T05:12:26.4031704Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Management0]/state",
        "values": {
          "interfaces/interface/state": {
            "arista-intf-augments:inactive": false,
            "openconfig-interfaces:admin-status": "UP",
            "openconfig-interfaces:counters": {
              "in-unicast-pkts": "1694",
              "out-unicast-pkts": "4410"
              // omitted output for brevity
            },
            "openconfig-interfaces:ifindex": 999999,
            "openconfig-interfaces:last-change": "1664343413005553920",
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Management0",
            "openconfig-interfaces:oper-status": "UP",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      }
    ]
  }
]
```

#### gNMI SetRequest

Next, use the `SetRequest` operation to change the configuration of the interface. As you did in NETCONF and RESTCONF, when updating data-model-based configurations, you need to understand the data model. You can check the OpenConfig interfaces [data model](https://oreil.ly/ibP6F), and you will discover that it supports a `description` attribute that was not retrieved in the previous Get examples because it was not set yet, and there is no default value. Our goal is to define the interface description to `New Description`:

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123 --insecure --gzip \
    set \
    --update-path '/interfaces/interface[name=Management0]/config/description' \
    --update-value 'New Description'
```

Notice the use of `set` instead of `get` and the new parameters: `update-path` and `update-value`. In this case, we use XPath filtering to target a specific interface (if not, you would be updating *all* the interfaces with the same description) and the corresponding value. When the `SetRequest` is executed successfully, you receive a response confirming the operation.

Now, if you retrieve the configuration as you did in [Example 10-21](#apis-gnmic-get-interfaces-config), the new attribute will show up:

```
[
  {
    "source": "eos-spine1:6030",
    "timestamp": 1664428969195249733,
    "time": "2022-09-29T05:22:49.195249733Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Management0]/config",
        "values": {
          "interfaces/interface/config": {
            "openconfig-interfaces:description": "New Description",
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Management0",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      }
    ]
  }
]
```

However, not all the attributes are configurable because of dependencies on the platform. For instance, the `mtu` attribute is not configurable in this Arista platform, and if you try to update it, you will receive an error, as you can see next:

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123 --insecure --gzip \
  set \
  --update-path '/interfaces/interface[name=Management0]/config/mtu' \
  --update-value '1400'

target "eos-spine1:6030" set request failed: target "eos-spine1:6030" SetRequest failed:
  rpc error: code = Aborted desc = failed to apply: Unavailable command (not supported
  on this hardware platform) (at token 1: 'mtu'): CLI command 3 of 5 'l2 mtu 1400'
  failed: invalid command
CLI Commands:
1 interface Management0
2 l2 mtu 1400
3 exit

Error: one or more requests failed
```

###### Note

This error message also shows something interesting—what is happening behind the scenes. Every platform implements the RPC operations differently. In this case, you see from the CLI commands executed that the device is translating the YANG data model changes into CLI commands.

#### gNMI Subscribe

gNMI was the first data-model interface to support data-model-driven telemetry (dial-in) with the `subscribe` operation. We go deep on telemetry in [“Understanding model-driven telemetry”](#apis-model-driven-telemetry), but here you have an example of subscribing to the interface counters, targeting the counters’ *path* in the prefix:

```
$ gnmic -a eos-spine1:6030 -u ntc -p ntc123  --insecure \
  subscribe \
  --path "/interfaces/interface/state/counters"

{
  "source": "eos-spine1:6030",
  "subscription-name": "default-1664428777",
  "timestamp": 1664428707256105665,
  "time": "2022-09-29T05:18:27.256105665Z",
  "prefix": "interfaces/interface[name=Management0]/state/counters",
  "updates": [
    {
      "Path": "in-octets",
      "values": {
        "in-octets": 141271
      }
    },
    {
      "Path": "in-unicast-pkts",
      "values": {
        "in-unicast-pkts": 1779
      }
    }
  ]
}
# other outputs omitted for brevity
```

The `subscribe` operation keeps a session established, from the client, to get updates on the data model. In this case, we are subscribed to updates on the interface counters, but you could also subscribe to the interface operational status or the BGP session establishment, and so on. The updates can be sampled periodically or triggered when the value changes, so you get notified only when something happens.

As you may have already concluded after reviewing NETCONF, RESTCONF, and gNMI, these protocols and interfaces share common concepts but also have differences. To make this content easier to digest, we spell out the differences next.

## Comparing NETCONF, RESTCONF, and gNMI

At this point, you likely have questions about the differences between the three interfaces using a data-model-driven approach (NETCONF, RESTCONF, and gNMI). In this section, we want to give you more insight into how they are related.

Everything started with NETCONF (the first RFC published in 2006) trying to address the limitations of SNMP to manage network configurations. At that moment, SNMP was widely used to monitor network’s operational state, but it was not adopted for network management. Because of this, as we explained in [“Using NETCONF”](#apis-netconf), new ideas were introduced: multiple data stores, RPC operations, effective config management in transactions, and the use of data models to update/retrieve configuration data and retrieve operational data.

Notice that we stress configuration management as the primary use case for NETCONF. Implicitly, it was acknowledging that the SNMP monitoring approach, ported to NETCONF, was good enough. However, later, new concerns about a better way to retrieve operational data appeared, and the IETF started (around 2014–2015) to get requirements to implement streaming telemetry (a continuous and customized stream of data from a YANG data store), which we present in [“Understanding model-driven telemetry”](#apis-model-driven-telemetry).

Around the same time (2014), the OpenConfig consortium was founded and led by Google, focused on implementing streaming telemetry as one of the main drivers of gNMI, a new network management interface defined as an open source project (with the first commit in 2017), instead of an internet standard. For the rest of the functionalities, it used NETCONF ideas as a reference with a simpler implementation.

More or less in parallel (2017), the IETF created the RESTCONF interface that brought together the NETCONF approach and the simpler, well-known RESTful API paradigm to promote more adoption of data-model-driven management when not all the NETCONF requirements are needed.

[Table 10-6](#apis-comparing-data-model-interfaces-table) compares the three interfaces by focusing on their main differences.

|  | NETCONF | RESTCONF | gNMI |
| --- | --- | --- | --- |
| Encoding | XML | JSON or XML | protobuf or JSON |
| Transport | SSH | HTTP/TLS | gRPC over HTTP/2 |
| Transaction scope | Network-wide | Single-target, single-shot | Single-target, single-shot, sequenced |

Let’s take a closer look at these three main differences:

EncodingNETCONF used the most popular encoding when it was defined (XML), and RESTCONF, even though still supporting XML (likely for reusability from NETCONF scripts), promoted JSON as a more popular encoding (and easier to read). However, gNMI chose protobuf because this binary encoding reduced the payload when compared to XML. Streaming operational data was an important use case for this interface, and this creates a lot of network traffic.

TransportNETCONF can support multiple transport protocols, but the most common one when it was defined was SSH, and it became the de facto one. RESTCONF leveraged HTTP to become yet another REST API, and gNMI adopted the Google internal protocol gRPC to support protobuf encoding.

Transaction scopeNETCONF came from operator best practices whereby the network itself is used to test and deploy configurations that can affect multiple devices, so the network-wide transaction scope was implemented. RESTCONF, to adhere to REST principles, doesn’t support state and can deal with only one target at a time, without any relevant operation sequence. gNMI is the simplest of all, assuming a specific order of all the operations. This simple approach comes from software-oriented teams managing infrastructure, where the configuration validation is most likely done out of the box, in a development environment.

Next, so you can better understand the interfaces, we compare the development lifecycle of the organizations behind them, which are also developing vendor-neutral data models.

### Network interfaces development lifecycle

NETCONF and RESTCONF are defined and promoted by the [IETF](https://www.ietf.org). On the other side, gNMI is developed under the umbrella of the [OpenConfig community](https://www.openconfig.net). Each group has a completely different way of working, which affects how these protocols and interfaces are defined, developed, and adopted:

IETFIts mission—defined in [RFC 3936](https://oreil.ly/XtEg7)—is to develop technical recommendations to design, use, and manage the internet. This is done via an open process, with volunteers, and rough consensus from multiple parts.

OpenConfigThis working group of network operators and vendors is focused on building a vendor-independent software layer for managing network devices. It operates as an open source project, with direct contributions.

Both have the common goal to create better ways to manage networks. However, the difference is in the way they achieve it. IETF’s process of proposal, approval, and implementation usually takes longer than the same process under OpenConfig. In open source projects with strong leadership, the proposal, review, and adoption process leads to a faster release cycle. A standard addresses diverse use cases and will be stable for a while, but when you work on an open source project, you can move quickly to solve more concrete use cases and leave the door open for future changes. This capacity to deliver, especially for streaming telemetry, was one of the key factors for the adoption and popularity of the gNMI interface.

Having multiple options to solve a problem is nothing new in the networking world. Successful nonstandard solutions have been adopted multiple times, and afterward, these solutions (with small differences) were adopted by IETF (e.g., NetFlow and Internet Protocol Flow Information Export, or IPFIX). The experience says that both could likely coexist, solving different usage approaches.

OpenConfig and IETF are working on more than network management interfaces. A main focus of both organizations is to implement the right data models to describe the network information needed for configuration and operational validation. These models should work well under any of the interfaces—for instance, using an OpenConfig data model under the NETCONF interface, as you saw in [“NETCONF with Cisco IOS XE”](#apis-netconf-iosxe). However, as we mentioned, the structure of the data models differ in how the intended and operational data is organized.

Last, we will delve into streaming telemetry.

### Understanding model-driven telemetry

Current large-scale network architectures have uncovered the operational limitations of SNMP for network monitoring. Even though SNMP is still in use, its model to retrieve data via a *poll* method, with the management server *asking* for data every time, was adding delay and extra processing to get data continuously.

These performance limitations, together with the adoption of data-model management (e.g., NETCONF or gNMI), led to the definition of *model-driven telemetry*. It adopts a *push* model to stream data from network devices continuously, providing near real-time access to operational data. Now, instead of *asking* for data, the management applications can *subscribe* to specific data from the supported data models defined with YANG. The retrieved data is structured and can be published at a defined cadence or as it changes.

With model-driven telemetry, you decide which data you need, when you need it, and where to send (or receive) it. You can subscribe to telemetry streams in two ways: dial-in and dial-out (represented in [Figure 10-4](#apis-figure-telemetry)).

Dial-inThis is a dynamic model: an external application opens a session to the network device and establishes one or more subscriptions (to different parts of the data store) over the same session. The network devices send operation data for as long as the session stays up.

Dial-outThis is a configured model: the subscriptions are configured on the network device in advance using any of the available interfaces, and it’s up to the device to open a telemetry session to the receiver. If this session goes down, the network device will open a new one.

![npa2 1004](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1004.png)

###### Figure 10-4. Model-driven telemetry

gNMI implemented the first streaming telemetry via the dial-in model, and it’s still the most widely adopted one. However, the dial-out model adds some benefits:

- Reduces a network device’s exposure to external threats as the connection is initiated from the device itself and avoids firewall configurations to let access in.
- Collectors can be stateless; they need to only listen and store the collected data. The control is on the configuration management system that created the subscription on the network device.

Nowadays, both NETCONF and gNMI support the dial-in model. Dial-out mode is simply a configuration setting, which can be done via any configuration interface (including CLI), and the data is exported over a transport protocol (TCP or UDP).

The first model-driven telemetry implementation was the gNMI `SubscribeRequest` operation, a dial-in mode. This has been, for a long time, one of the key benefits of gNMI versus NETCONF, which took more time to come up with its implementation definition. At the time of this writing, the adoption of streaming telemetry is much more mature in gNMI, which is widely adopted by most vendors. NETCONF dial-in and dial-out are still in their early stages.

Dial-out telemetry has some incipient implementations—for instance, by Cisco and Juniper, using gRPC as the transport protocol. In parallel, the IETF is working on standards grouped as YANG Push, UDP and HTTPS/TCP transport options, and support for JSON and CBOR encoding.

###### Note

[Concise Binary Object Representation or CBOR](https://cbor.io) standardized in [RFC 8949](https://oreil.ly/UFjnD), is a binary data format based on JSON that supports schema definition directly with the YANG language.

Model-driven telemetry has prioritized TCP as a transport protocol over UDP (used by SNMP) for providing more reliable data transfer, and with nonrepudiation. However, UDP support provides some benefits in highly intense event traffic, such as in sampling mode when TCP benefits are not mandatory.

As we will explore in [Chapter 14](ch14.html#architecture) when discussing the role of model-driven telemetry in a network automation strategy, telemetry is usually combined with message brokers to distribute data from the collectors, adding some features such as data schema validation, versioning, or routing.

Which solution will prevail is hard to predict. gNMI is well established and supported by a lot of vendors. On the other side, YANG Push supports more use cases (e.g., more encoding options) and comes from a standardization body (IETF) that is important for some network industry actors (e.g., service providers).

Now that we’ve explained the API interfaces available to manage network devices and controllers, you must understand how to automate them via these APIs. We’ll now take a look at using Python and Go to automate these interfaces, and also SSH.

# Using Network APIs for Automation

As we’ve stated, the tools for *exploring* and *learning* to use an API differ from the tools used to *consume* an API within a programmatic solution. Thus far, we’ve looked at cURL for exploring HTTP-based APIs, an interactive NETCONF over SSH session for exploring the use of NETCONF, and gNMIc for exploring gNMI. In this part of the chapter, we’ll look at how to use Python and Go to automate network devices, using some popular libraries:

Python RequestsAn intuitive and popular HTTP library for Python. This is the library we will use for automating devices and controllers with both RESTful HTTP-based APIs and non-RESTful HTTP-based APIs.

Go net/httpA built-in package to serve as an HTTP client or server. Introduced in [Chapter 7](ch07.html#go), it’s similar to Python Requests, and we will use it to demonstrate how to interact with RESTCONF.

Python ncclientThis is a NETCONF client for Python, so we will use it for automating devices using NETCONF.

Go OpenConfig gNMIcWe used this gNMI client as a CLI in the previous section. Here, we will use the package directly in Go applications to interact via the gNMI interface.

Python NetmikoThis is a network-first SSH client for Python. This is the library we will use for automating devices via native SSH for devices without programmatic APIs.

###### Warning

Even though we cover multiple APIs in this chapter, it is meant to be read from start to finish and not as API documentation for any given API. All the scripts created in this chapter have loose error handling because we are prioritizing simplicity to show the ideas instead of creating production-ready code. Be aware that the examples shown depend on the library’s version. The syntax and signature can change from one version to another.

Let’s start by looking at the Requests library and communicating with HTTP-based APIs.

## The Python Requests Library

You’ve seen how to make HTTP-based API calls from the command line with cURL, or maybe you used the Postman GUI. These are great mechanisms for learning how to use a given API—but realistically, to write a script or a program that helps automate network devices, you need to be able to make API calls from within a script or program. In this section, we introduce the Python Requests library, which simplifies working with web-based APIs.

To enable an easy mapping between the previous section and this one, we reuse the same examples from [“Exploring HTTP-based APIs with cURL”](#apis-explore-http-api), the Cisco Meraki API, and the Arista eAPI. This section is meant to be read from start to finish, as the core focus is getting started with using the Requests library.

###### Tip

To install Requests, you can use `pip3` within your virtual environment. Remember that you can review basic Python concepts in [Chapter 6](ch06.html#python). Here’s the installation command:

```
$ pip3 install requests
$ pip3 list | grep requests
requests                          2.26.0
```

### Automating the Meraki API with Requests

Let’s dive in and take a look at our first example using Requests. We’re going to create a complete Python script to retrieve the first network, from the first organization, from a Cisco Meraki account. We’ve already executed this same GET request with cURL in Examples [10-2](#apis-curl-meraki-orgs-python) and [10-3](#apis-curl-meraki-networks-python). Remember to check the [Meraki API documentation](https://oreil.ly/rzR5F) if needed.

Now, in [Example 10-22](#apis-requests-get-organizations), we focus on the first part of a script to retrieve the organizations available in Cisco Meraki.

##### Example 10-22. Using Requests to get Meraki organizations

```
#!/usr/bin/env python3

# The Python Requests library is used to issue and work HTTP-based systems.
import requests

# This executes if our script is being run directly.
if __name__ == "__main__":
    # This token is taken from Cisco Developer Hub to experiment with the API
    my_token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

    # This statement creates a Python dictionary for the HTTP request
    # headers that are going to use in the API calls.  The first two
    # headers we are setting are Content-Type and Accept.
    # The last one uses a custom Meraki header for authentication
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": my_token,
    }

    # The URL is saved as a variable called base_url to modularize our
    # code and simplify the next statement.
    base_url = "https://api.meraki.com/api/v1"

    # In the Requests library, there is a function per HTTP verb, and in
    # this example we are issuing a GET request, so we are therefore
    # using the get function. We pass two objects into the get function.
    # The first  object passed in must be the URL, and the others should be
    # keyword arguments (key=value pairs). Then, we pass the proper headers.
    response = requests.get(f"{base_url}/organizations", headers=headers)
```

At the end of this Python script, the `response` variable contains the response from the Meraki API. You could reproduce the same steps in an interactive Python session, as noted in [Chapter 6](ch06.html#python). Actually, it’s a great idea to try this to better understand the content of the `response` variable. So, let’s run the previous script in the interactive interpreter, using the `-i` flag. It is a great way to test and troubleshoot:

```
ch10-apis/python_requests$ python3 -i get_networks.py
# The interactive execution leave us at the end of our script, after the
# response = requests.get(f"{base_url}/organizations", headers=headers)
>>> response
<Response [200]>
```

The `response` variable contains a 200 HTTP response, so you should assume everything worked as expected. Indeed, one important piece of data is missing: where is the content of the response, containing the *organizations*?

Being in the Python interactive interpreter session, you can inspect the `response` with `dir()`, displaying all attributes and methods of a given object:

```
>>> dir(response)
[ # output omitted for brevity
 'apparent_encoding', 'close', 'connection', 'content',
 'cookies', 'elapsed', 'encoding', 'headers', 'history',
 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason',
 'request', 'status_code', 'text', 'url']
```

From all the attributes and methods available in the `response`, we will review two: `status_code` and `json`.

The `status_code` attribute gives us access to the HTTP response code as an integer:

```
>>> print(response.status_code)
200
```

The `json()` method returns the response content as a `dict`, decoding the JSON contained in the `text` attribute (which stores the actual response):

```
>>> response.json()
[
  {
    'id': '573083052582915028',
    'name': 'Next Meraki Org',
    'url': 'https://n18.meraki.com/o/PoiDucs/manage/organization/overview',
    'api': {
      'enabled': True
    },
    'licensing': {
      'model': 'co-term'
    },
    'cloud': {
      'region': {
        'name': 'North America'
      }
    }
  },
  # other entries omitted for brevity
]
>>>
```

You can start using this output by saving it as a variable and extracting the value of the `name` key from the first organization:

```
>>> organizations = response.json()
>>> type(organizations)
<type 'list'>
>>> organizations[0]["name"]
'Next Meraki Org'
```

In our script, we also store the response data in an `organizations` variable, and you can resume the script that will get the *networks* from a given organization, as shown in [Example 10-23](#apis-requests-get-networks).

##### Example 10-23. Using Requests to get Meraki networks

```
    # Continues from the previous code snippet

    # We pick the id from the first organization to later gather the related networks
    first_organization_id = organizations[0]["id"] 

    # Similar get request, composing the URL with the organization id
    response = requests.get(
        f"{base_url}/organizations/{first_organization_id}/networks", headers=headers
    )

    networks = response.json()                     
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We pick the identifier from the first available organization, accessing the `0` index in the list of organizations.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

If we explore the content of `networks`, we will see another dictionary—this time containing the network data from the Meraki API.

Let’s continue to build on this; you are now going to create a new network (within an organization) by using Requests, as in [Example 10-4](#apis-curl-meraki-create-network-python). As you may guess, you need to only extend the previous script, adding the same content used in the cURL example: update the URL, update the HTTP request type, and send data in the body of the request, as we do in [Example 10-24](#apis-requests-post-networks).

##### Example 10-24. Using Requests to create a Meraki network

```
    # Continues from the previous code snippet
    # first_organization_id comes from the previous script

    # json library is used to encode a dictionary object as a JSON string
    import json

    # Payload contains the data necessary to define the expected
    # data to create a new network in the API
    payload = {
        "name": "my brand new automated network",
        "productTypes": ["switch"],
    }

    # Using the post method instead of get to create an object
    response = requests.post( 
        f"{base_url}/organizations/{first_organization_id}/networks",
        headers=headers,
        data=json.dumps(payload)
    )

    print(response.json())
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Pay attention to the HTTP verb being used. This particular request uses the `post()` function as a resource is being created. To update a resource, you’d use the `patch()` function, and to replace a resource, you’d use `put()`. You’ll see these functions in more examples later in the chapter.

Let’s focus on how to send data in the body of the HTTP request. This is where you need to differentiate between a Python dictionary and a JSON string. While you work with dictionaries in Python to construct the required body, this is sent over the wire as a JSON string. To convert the dictionary to a well-formed JSON string, you use the `dumps()` function from the `json` module. This function takes a dictionary and converts it to a JSON string. You finally take the string object and pass it over the wire by assigning it to the `data` key being passed to the `post()` function.

###### Tip

We typically know which payload data is required to create/update an API resource by checking the API documentation. Some of the attributes will use some defaults, but for the rest, we need to provide some data. In the example, `name` looks like an obvious mandatory piece of data. But `productTypes` could be missed, assuming that it could be a default product type. In these cases, the API response should provide a useful error message to guide you, pointing out what is missing in the request payload.

Finally, when running the script, you get a response (from the POST). It provides a new network with the `name` and the `productTypes` defined before, plus the rest of the parameters automatically assigned in creation:

```
ch10-apis/python_requests$ python3 create_network.py
{
  'id': 'N_573083052583238204',
  'organizationId': '573083052582915028',
  'productTypes': ['switch'],
  'url': 'https://n18.meraki.com/my-brand-new-aut/n/vAQKbcs/manage/usage/list',
  'name': 'my brand new automated network',
  'timeZone': 'America/Los_Angeles',
  'enrollmentString': None,
  'tags': [],
  'notes': None,
  'isBoundToConfigTemplate': False
}
```

You have learned about using the Python Requests library for the Cisco Meraki API. Next, we continue exploring Requests but for the Arista eAPI (as in the cURL examples).

### Consuming eAPI in a Python script

We’re now going to look at Arista’s eAPI. As you learned in [“Understanding non-RESTful HTTP-based APIs”](#apis-curl-non-restful), as you go through the next examples with eAPI, keep the following points in mind:

- eAPI is a non-RESTful HTTP-based API. In other words, it’s an HTTP-based API that doesn’t follow all the principles of REST. An HTTP POST is used no matter which operation is being performed—​even if `show` commands are used, a POST is still used. Specifically, it uses the JSON-RPC protocol to communicate between you (the client) and the switch (the server).
- Remember POST requests require data to be sent in the data payload of the request. This is where solid API tools and documentation come into play.
- The URL format for eAPI API calls is always *http(s)://<ip-address-eos>/command-api*.

###### Tip

Arista switches have a built-in tool called the *Command Explorer* that you could leverage to learn the required structure of the payload object. The API documentation provides details about this tool.

We start with a basic Python script in [Example 10-25](#apis-requests-eapi). This code uses the Requests library to communicate to the Arista API (eAPI), executing the `show vlan brief` CLI command. This command should return the VLAN information with the device. At the end of the script, the code will output the response and the HTTP status code.

##### Example 10-25. Using Python Requests with Arista eAPI

```
import json
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    # requests class to create the basic authentication header
    auth = HTTPBasicAuth('ntc', 'ntc123') 

    url = 'http://eos-spine1/command-api' 

    # payload expected by the API
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": [
                "show vlan brief"
            ],
            "version": 1
        },
        "id": "EapiExplorer-1"
    }

    # Even though we retrieve data with the "show vlan brief",
    # the API uses the POST method
    response = requests.post(url, data=json.dumps(payload), auth=auth) 

    # Helper output onscreen to show the status code, and the response
    print(f'STATUS CODE: {response.status_code}')
    print(f'RESPONSE: {json.dumps(response.json(), indent=4)}')
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`HTTPBasicAuth` class, from the Requests library, to create the basic authentication format (using a Base64 encoding).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Using an *http* endpoint is not recommended for production. If we use a self-signed certificate or unverified HTTPS connection (adding `verify=False` to the requests method), we will receive a warning, which can be disabled with `requests.packages.urllib3.disable_warnings()`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Even though we are *retrieving* data, the HTTP method used is POST. So, it requires a *payload*, which defines several parameters required by the API.

When you execute the script, it should give a similar output:

```
ch10-apis/python_requests$ python3 eapi-requests.py
STATUS CODE: 200
RESPONSE:
{               
    "jsonrpc": "2.0",
    "id": "EapiExplorer-1",
    "result": [ 
        {
            "sourceDetail": "",
            "vlans": {
                "1": {
                    "status": "active",
                    "name": "default",
                    "interfaces": {
                        "Ethernet1": {
                            "privatePromoted": false
                        },
                        # Omitted other interfaces for brevity
                    },
                    "dynamic": false
                },
                "20": {
                    "status": "active",
                    "name": "VLAN0020",
                    "interfaces": {},
                    "dynamic": false
                },
                "30": {
                    "status": "active",
                    "name": "VLAN0030",
                    "interfaces": {},
                    "dynamic": false
                }
            }
        }
    ]
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The response is a nested JSON object, as expected.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The output of the commands (only one in this example) is a list of dictionaries. There would be a list element for each command executed.

It’s noticeable that, even though you send a CLI command (`show vlan brief`), the format of the response content is JSON. This makes it much easier to interact with the API programmatically. However, if you are interested in the traditional text CLI output, you can specify it with `"format": "text"` in the payload, and the response would contain an `output` key with a string:

```
RESPONSE: {
    "jsonrpc": "2.0",
    "id": "EapiExplorer-1",
    "result": [
        {
            "output": "VLAN  Name                             Status    Ports\n
            ---- -------------------------------- --------- -------------------"
            # output omitted for brevity
        }
    ]
}
```

Next, we go a bit further with a more elaborate example to show the potential of automating the network via API-based scripts.

#### Using eAPI to autoconfigure interface descriptions based on LLDP data

Let’s continue to use eAPI to build something a little more useful. How about a Python script that autoconfigures interface descriptions for Ethernet interfaces based on LLDP neighbors for two Arista spine switches?

To do this, you *should* modularize the script to support multiple devices as well as have a simple way to send multiple API calls without requiring multiple payload objects in the script. Our goal is to autoconfigure interface descriptions such that they will look like the following (this is an example, and you will see the actual LLDP data and the final description later):

```
interface Ethernet2
  description Connects to interface Ethernet2 on neighbor eos-leaf1.ntc.com
  no switchport
!
interface Ethernet3
  description Connects to interface Ethernet2 on neighbor eos-leaf2.ntc.com
  no switchport
!
```

To easily digest the code, we split it into three parts so you can progressively understand the complete example.

First, in [Example 10-26](#apis-eapi-lldp-1), you create the `issue_request()` function, which takes two arguments: the target device and the commands. The data is the only data in the requests’ operation. So, with this helper function, you could later pass different target devices and different commands to obtain the response (already converted from JSON to a Python object). This is a good example of the Don’t Repeat Yourself (DRY) software development principle.

##### Example 10-26. Wrapping requests in a helper function

```
import json
import sys
import requests
from requests.auth import HTTPBasicAuth

# Helper method to issue "commands" to a "device", and return the result
def issue_request(device, commands): 
    """Make API request to EOS device returning JSON response."""
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": commands,
            "version": 1
        },
        "id": "EapiExplorer-1"
    }

    response = requests.post(
      'http://{}/command-api'.format(device),
      data=json.dumps(payload),
      auth=HTTPBasicAuth('ntc', 'ntc123')
    )

    return response.json()

# continues in the next example
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The code of this function is exactly the same as [Example 10-25](#apis-requests-eapi), but has been modularized for reusability.

Next, in [Example 10-27](#apis-eapi-lldp-2), we leverage the `issue_request()` function to get the specific information we want from the API response (in this case, `lldpNeighbors`). This implies knowledge of the data structure from the response, which you can get by experience or from the documentation.

##### Example 10-27. Extracting LLDP neighbors from the response

```
# continues from the previous example

def get_lldp_neighbors(device):
    """Get list of neighbors

    Sample response for a single neighbor:
        {
          "ttl": 120,
          "neighborDevice": "eos-spine2.ntc.com",
          "neighborPort": "Ethernet2",
          "port": "Ethernet2"
        }
    """
    # Define the target methods
    commands = ['show lldp neighbors']
    response = issue_request(device, commands)
    # Extract the neighbors' data from the result of the first and only command
    # and return it as a list of dictionaries
    return response['result'][0]['lldpNeighbors']

# continues in the next example
```

###### Tip

Creating readable code takes practice, but in [Example 10-27](#apis-eapi-lldp-2) you can observe two useful approaches:

- Using self-descriptive naming: `get_lldp_neighbors` clearly defines its intent
- Leveraging function docstrings to explain the function’s purpose—in this case, the format of the response

Finally, in [Example 10-28](#apis-eapi-lldp-3), we add another helper function, `configure_interfaces()`, and the `main` function to run the script. The `configure_interfaces()` function does exactly what it describes: takes the list of neighbors, and with *configuration* commands, updates the description of the interfaces. In the `main` function, you define all the target devices to iterate on and perform two operations: get the LLDP information, and configure the interfaces description accordingly.

##### Example 10-28. Configuring the interfaces description with LLDP information

```
# continues from the previous example

def configure_interfaces(device, neighbors):
    """Configure interfaces in a single API call per device."""
    command_list = ['enable', 'configure']
    for neighbor in neighbors:
        local_interface = neighbor['port']
        if local_interface.startswith('Eth'):
            # Excluding Management as it has multiple neighbors
            description = (
              f"Connects to interface {neighbor['neighborPort']} on neighbor "
              f"{neighbor['neighborDevice']}"
            )
            description = 'description ' + description
            interface = f'interface {local_interface}'
            # Extending the list of commands, in the proper order
            command_list.extend([interface, description])
    # Retrieve the output from the commands created from the neighbors
    response = issue_request(device, command_list)

if __name__ == "__main__":
    # device names are FQDNs
    devices = ['eos-spine1', 'eos-spine2']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('Auto-configured Interfaces for {}'.format(device))
```

###### Note

Going through this example, you may be wondering if you could have organized the code differently. Maybe you could combine `get_lldp_neighbors` with the `configure_interfaces()` function, to get a bigger one. Or you could call `issue_request` out of the other functions, in the main code. The point here is that you have a myriad of options to create valid code. Choose one, experiment with it, and look for better patterns toward reusability and readability, while keeping it simple.

Let’s run the script that will update the interfaces’ descriptions according to the LLDP neighbor:

```
ch10-apis/python_requests$ python3 eapi-autoconfigure-lldp.py
Auto-configured Interfaces for eos-spine1
Auto-configured Interfaces for eos-spine2
```

Using the Requests Python library is an easy way to interact with APIs in your Python applications. However, to make it even simpler, some APIs provide their own libraries, the SDKs. We will give a quick glance at SDKs next.

### Using API SDKs

An *API SDK* is a software package that abstracts access to an API by using functions, methods, and/or classes. It allows faster development because it comes with all the common conventions implemented. Therefore, you don’t need to reinvent the wheel every time, reducing development time. The SDK makes the code simpler and more readable. On the other hand, it could introduce some constraints due to non-implemented features available in the API or introduce library dependencies, increasing the footprint of your application.

Most API platforms offer SDKs in the most popular languages in their user community. Both APIs explored in the previous section offer Python SDKs:

- [Cisco Meraki](https://oreil.ly/YCfkp)
- [Arista eAPI](https://oreil.ly/retLy)

It’s not the purpose of this book to document using any specific SDK, but showing how an SDK is used enables you to see what one looks like. For detailed information about an SDK, check its reference docs page.

#### Exploring the Meraki API SDK

Using the Meraki API SDK instead of the Requests library, you will get the same output as in [Example 10-22](#apis-requests-get-organizations) without having to know about some API conventions. For instance, you don’t need to know about the custom authentication header the API expects. This is also useful for maintainability because if this header key changes, you don’t need to update your code.

###### Note

Use `pip3` to install the Meraki API SDK:

```
$ pip3 install meraki
$ pip3 list | grep meraki
meraki                            1.25.0
```

After importing the library, you have to instantiate the class `meraki.DashboardAPI`, which contains all the methods to interact with the API. This initialization requires only the API key used before, but not the URL or the authentication header key, as these are implicitly defined by the library:

```
>>> import meraki
>>>
>>> meraki_client = meraki.DashboardAPI(
...   api_key="6bec40cf957de430a6f1f2baa056b99a4fac9ea0")
2022-10-01 16:18:28 meraki: INFO > Meraki dashboard API session initialized with ...
# output omitted for brevity
>>>
```

Then you can retrieve the organization, as you did in [Example 10-22](#apis-requests-get-organizations). Instead of crafting the HTTP request, you use the `getOrganizations()` method in `meraki_​cli⁠ent.organizations`:

```
>>> my_orgs = meraki_client.organizations.getOrganizations()
2022-10-01 16:18:49 meraki: INFO > GET https://api.meraki.com/api/v1/organizations
2022-10-01 16:18:50 meraki: INFO > GET https://n392.meraki.com/api/v1/organizations
2022-10-01 16:18:50 meraki: INFO > organizations, getOrganizations - 200 OK
>>>
>>> my_orgs[0]
{
  'id': '573083052582915028',
  'name': 'Next Meraki Org',
  'url': 'https://n18.meraki.com/o/PoiDucs/manage/organization/overview',
  'api': {'enabled': True},
  'licensing': {'model': 'co-term'},
  'cloud': {'region': {'name': 'North America'}}
}
>>>
```

By now, you’re likely feeling comfortable interacting with HTTP APIs with Python.  You’ve interacted with a native RESTful HTTP API, Cisco Meraki, and a non-RESTful one, Arista eAPI. As a reminder, every request to eAPI is an HTTP POST, and the URL is the same for every request, whereas a truly RESTful API using HTTP as its transport has a different URL based on the resource in question (e.g., organization, network, or routes in Cisco Meraki API).

Next, we will use the other programming language covered in the book, Go, to explore a specific HTTP API, the RESTCONF interface.

## The Go net/http Package

In the previous section, you learned how to use the Python Requests library to interact with HTTP APIs. Here, we will use the Go net/http package to interact with HTTP APIs (focusing specifically on the RESTCONF interface—in this case, exposed by a Cisco IOS XE). [Chapter 7](ch07.html#go) introduced the net/http package, and here we’ll show a few examples of interacting with the RESTCONF interface.

### Using net/http with RESTCONF

First, let’s start with the same operation as in [“Exploring RESTCONF in Cisco IOS XE”](#apis-exploring-restconf) to obtain the full native configuration. In [Example 10-29](#apis-go-http-config), the main differences from the net/http example in [Chapter 7](ch07.html#go) are the use of the basic `http.NewRequest` to create a GET request and the `Authorization` header.

##### Example 10-29. Using Go net/http to retrieve the configuration

```
package main

import (
    "crypto/tls"
    "encoding/base64"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
)

// helper method to construct the expected format of
// the basic authentication string, encoded in base64
func basicAuth(username, password string) string {
    auth := username + ":" + password
    return base64.StdEncoding.EncodeToString([]byte(auth))
}

// helper method to implement the error-checking pattern
func checkError(err error) {
    if err != nil {
        log.Fatal(err)
    }
}

func main() {
    transCfg := &http.Transport{
        // ignore expired SSL certificates
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    // create a new HTTP client, with the previously defined transport config
    client := &http.Client{Transport: transCfg}

    // create a new HTTP request, with the method, url, and headers
    request, err := http.NewRequest("GET",
        "https://csr1/restconf/data/Cisco-IOS-XE-native:native", nil)
    checkError(err)
    request.Header.Set("Accept", "application/yang-data+json")
    request.Header.Add("Authorization", "Basic "+basicAuth("ntc", "ntc123"))

    // perform the HTTP request, defined before, and store it in result
    result, err := client.Do(request)
    checkError(err)
    // read the body content from the response
    body, err := ioutil.ReadAll(result.Body)
    checkError(err)
    result.Body.Close()
    fmt.Printf("%s", body)
}
```

Running the code (`go run get_config.go`) will return the very same output obtained in [“Exploring RESTCONF in Cisco IOS XE”](#apis-exploring-restconf). However, you could narrow the output by extending the path in the `NewRequest` with a specific data model and including filtering.

For instance, you can retrieve a specific interface configuration by using URI-encoded path expressions. In `get_config_interface_g1.go`, we use the URI-encoded path expression `interface=GigabitEthernet1` to retrieve the configuration of the `GigabitEthernet1` interface: `restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1`. This matches the identifier field (`name`) of the interface in the YANG model and gets you only the configuration of the specified interface:

```
ch10-apis/go_http$ go run get_config_interface_g1.go
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet1",
    "description": "MANAGEMENT_DO_NOT_CHANGE",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.0.0.15",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {
    }
  }
}
```

### Updating configuration via RESTCONF with net/http

You can also use net/http to run HTTP requests to change the configuration state. In [“Exploring RESTCONF in Cisco IOS XE”](#apis-exploring-restconf), we used a PATCH request to update the existing OSPF configuration, and we mentioned that with a PUT request, you could apply the *declarative configuration* approach that defines the final state without considering the current one.

In [Example 10-30](#apis-go-http-update), you can see the most relevant code from `update_ospf_config.go` that *replaces* the OSPF configuration with a new one. The HTTP request takes a JSON payload with the expected data structure and uses it in the PUT request.

##### Example 10-30. Using Go net/http to update the OSPF config

```
// Omitted code

func main() {
  // Omitted code

  // JSON payload for HTTP request
  var jsonStr = []byte(`{
  "router-ospf": {
    "ospf": {
      "process-id": [
        {
          "id": 10,
          "network": [
            {
              "ip": "203.0.113.0",
              "wildcard": "0.0.0.7",
              "area": 0
            },
            {
              "ip": "203.0.113.64",
              "wildcard": "0.0.0.7",
              "area": 0
            }
          ],
          "router-id": "203.0.113.1"
        }
      ]
    }
  }
}'`)

  // create a new HTTP request, with PUT method, new URL,
  // the payload, and new headers
  request, err := http.NewRequest("PUT",
    "https://csr1/restconf/data/Cisco-IOS-XE-native:native/router/
    Cisco-IOS-XE-ospf:router-ospf", bytes.NewBuffer(jsonStr))
  checkError(err)
  request.Header.Set("Accept", "application/yang-data+json")
  request.Header.Set("Authorization","Basic " + basicAuth("ntc","ntc123"))
  request.Header.Set("Content-Type", "application/yang-data+json")

  // Omitted code
}
```

###### Note

In a real example, you would get the payload from an external file or a database, but we used a JSON object directly to simplify the script.

After these changes, you run the script, and voilà! The new OSPF configuration is in place. You can check it by repeating the GET request to the OSPF configuration node in the router.

With RESTful APIs that offer this type of power and control, you need to ensure you have a good process for making changes. As you can see, if you are trying to make only a small change or addition and happen to send a PUT request, catastrophic consequences can result. From an overall adoption perspective of this particular API, you may want to start using PATCH requests and gradually migrate to the point where you can indeed use PUT to declaratively manage specific sections of the configuration.

###### Warning

[Example 10-30](#apis-go-http-update), using the PUT declaratively, configures everything under the `ospf` key. But if you targeted the `router` key, this key change would technically eliminate all other routing protocol configurations too. That’s not a good thing. However, we chose to show the power and potential danger if it’s not used and understood properly.

Now that we’ve shown how to start automating devices that have HTTP-based APIs by using Python and Go, let’s look at the same approach by using the Python ncclient for automating devices with the NETCONF interface.

## The Python ncclient Library

The Python ncclient is a popular NETCONF client for Python. It is client software that is built to communicate programmatically with NETCONF servers. Remember, in our case, a NETCONF server is going to be a network device. We’ll walk through a vMX Juniper example, but the same approach will work for other platforms.

###### Note

To install ncclient, you can use `pip3`:

```
$ pip3 install ncclient
$ pip3 list | grep ncclient
ncclient                          0.6.13
```

Once ncclient is installed, you can start to issue NETCONF API calls to network devices. Let’s walk through this while in the Python interactive interpreter.

###### Note

ncclient is not the only Python library offering NETCONF capabilities. Vendor-specific ones exist, such as [PyEZ](https://oreil.ly/8Cz23) for Junos, as well as other generalist ones such as [scrapli-netconf](https://oreil.ly/sdPcl) and [netconf-client](https://oreil.ly/XG6pK).

When you enter the Python interpreter, your first step is to import the `manager` module within the ncclient Python package:

```
>>> from ncclient import manager
```

The basic function we are going to use within the `manager` module is responsible for establishing a persistent connection to the device. Keep in mind that since NETCONF runs over SSH, this connection is stateful and persistent (as compared to RESTful APIs being stateless). This function is called `connect()` and accepts several parameters such as hostname/IP address, port number, and credentials. You’ll see in the following example that other parameters will remain unchanged that map back to the underlying SSH configuration and properties:

```
>>> device = manager.connect(
...   host='vmx1', port=830, username='ntc',
...   password='ntc123', hostkey_verify=False,
... )
```

As soon as the `connect()` function is called, a NETCONF session is established to the network device, and an object is returned and saved as `device`, an instance of a ncclient `Manager` object. This object exposes the methods to interact with NETCONF RPC operations.

### Understanding the Manager object

First, let’s look at the `device` capabilities, as in [Example 10-8](#apis-netconf-capabilities), and get exactly the same output, but in a different format (a Python list):

```
>>> list(device.client_capabilities)
[
  'urn:ietf:params:netconf:base:1.0',
  'urn:ietf:params:netconf:base:1.1',
  'urn:ietf:params:netconf:capability:writable-running:1.0',
  'urn:ietf:params:netconf:capability:candidate:1.0',
  'urn:ietf:params:netconf:capability:confirmed-commit:1.0',
  # output omitted for brevity
]
```

### Retrieving Juniper vMX device configurations with ncclient

In [Example 10-9](#apis-netconf-get), when exploring the use of NETCONF over an SSH session, you used the complete `<get>` XML RPC operation to query the vMX router for the `fxp0` interface configuration. Now, you reuse the subtree filtering, defined as a string:

```
>>> get_filter = """
...   <configuration xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
...     <interfaces>
...       <interface>
...         <name>fxp0</name>
...       </interface>
...     </interfaces>
...   </configuration>
... """
```

###### Note

Remember that triple quotes in Python denote a multiline comment and can be used to create a multiline string that can be used as a value of a variable.

Once the filter is defined, you pass that as a parameter to the `get()` method, specifying the subfilter `subtree` type. Without the filter, you would get the full configuration:

```
>>> nc_get_reply = device.get(('subtree', get_filter))
```

At this point, after the NETCONF GET request to the device, the result is stored in `nc_get_reply` and matches the result in [Example 10-10](#apis-netconf-get-reply).

###### Note

The ncclient supports *XPath* filters. But, this support depends on the NETCONF capabilities of the platform. All filters used with Junos vMX examples are *subtree* filters because this platform doesn’t support XPath for `get` operations. You can see how to use XPath filters in [“Using ncclient with Cisco IOS XE”](#apis-ncclient-ios).

While our examples use XML strings as the filters, it is also possible to use native XML objects (etree objects). We are using string objects because they are much more human-readable and easier to use when getting started. You may want to use native etree objects if you need to dynamically build a filter object.

The `data` attribute in `nc_get_reply` contains the native XML object from the `lxml` Python library (lxml is covered in more detail in [Chapter 8](ch08.html#dataformats)). For instance, the `etree.tostring()` method converts a native XML object to a string:

```
>>> from lxml import etree
>>>
>>> as_string = etree.tostring(nc_get_reply.data)
>>> print(as_string)
b'<rpc-reply message-id="urn:uuid:e2c1daa0-8556-4e6b-84dc-e72e90809f73"><data>
<configuration commit-seconds="1653021086" commit-localtime="2022-05-20 04:31:26
UTC" commit-user="ntc"><interfaces><interface><name>fxp0</name><unit><name>0
</name><description>MANAGEMENT_INTERFACE__DO_NOT_CHANGE</description><family>
<inet><address><name>10.0.0.15/24</name></address></inet></family></unit>
</interface></interfaces></configuration><database-status-information>\n
</database-status-information></data></rpc-reply>'
```

In the output of `nc_get_reply`, you can observe the IP address and mask for the `fxp0` interface (`10.0.0.15/24`). If this is the information you are interested in, you should parse the XML tags that contain this information: `<address>` and `<name>`.

To *find* a specific tag in an `lxml.etree` object, you can use the `find()` method. It provides a simple way to search a full XML object for a given XML tag when using the expression denoted by `.//`. Since you want to extract the `<address>` object and its children, you could try the following example:

```
>>> address = nc_get_reply.data.find('.//address')
```

Unfortunately, it doesn’t work. What’s wrong here? The statement tries to extract the XML element with the `<address>` tag. However, when XML namespaces are used, the tag name must include the namespace concatenated—in other words, {`namespace`}`tag`. In this case, `{http://yang.juniper.net/junos/conf/interfaces}address`. Alternatively, if an XML namespace *alias* is defined, it can be used as *`alias`* : *`tag`*.

###### Note

Our example has multiple namespaces. You can gradually print one child object at a time to see which namespace is used. In the example, the default namespace is `urn:ietf:params:xml:ns:netconf:base:1.0`, but when you print a single object, you see only one. The next namespace in the hierarchy is overriding the default namespace for all children of the `<configuration>` element.

To properly extract the IP address and mask, we’ll follow three steps. First, we extract the `<address>` object that contains an inner `<name>` XML tag, then we extract the content of the `<name>` tag with the prefix and mask combined, and finally, we save it as a string by using `text`:

```
>>> address = nc_get_reply.data.find(
>>>   './/{http://yang.juniper.net/junos/conf/interfaces}address'
>>> )
>>> ip_address = address.find(
>>>   './/{http://yang.juniper.net/junos/conf/interfaces}name' 
>>> )
>>> ip_address.text
'10.0.0.15/24'
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We can’t look for `<name>` directly because we would hit the *interface* name, which is first in the hierarchy.

You may be thinking, “Extracting values based on the namespaces is tedious.” You are absolutely right. Parsing XML is not easy, and it is even more difficult when namespaces are involved. But, in the end, once you know the namespace, you just need to concatenate two strings. Also, it’s possible to strip namespaces from an XML object before doing XML parsing, further simplifying the process.

By now, you should be getting the hang of issuing NETCONF `<get>` requests. Let’s look at one more, but this time, working with the SNMP configuration to use the `findall()` method.

#### Using findall() to retrieve multiple XML objects

On our Juniper vMX, we currently have two SNMP read-only community strings configured. For verification, this is the output after we issue the `show snmp` command while in configuration mode:

```
ntc@vmx1# show snmp
location EMEA-IE;
contact Scott_Grady;
community public123 {
    authorization read-only;
}
community supersecure {
    authorization read-write;
}
[edit]
```

###### Tip

Our goal is to extract the name of each community string and the authorization level for each. Juniper has functionality in its CLI such that you can see the expected XML response as well when you pipe the command to `display xml` (for instance, `show snmp | display xml`).

When you know the data returned from the NETCONF request, you can more easily write the associated Python code. Whenever you are issuing a NETCONF `get` request to a Junos device, `<configuration>` needs to be the outermost XML tag when you’re collecting configuration state information. Within that element, you can build the appropriate filter, which can be gleaned from the XML text found while on the CLI. The filter string to request SNMP configuration looks like this:

```
get_filter = """
... <configuration>
...   <snmp>
...   </snmp>
... </configuration>
... """
```

The next step, in [Example 10-31](#apis-ncclient-get-snmp), is to make the request, just as we’ve done already. After the request is made, we’ll verify the output, printing the XML string to the terminal.

##### Example 10-31. ncclient `get` SNMP configuration

```
>>> nc_get_reply = device.get(('subtree', get_filter))
>>> print(nc_get_reply)
<rpc-reply message-id="urn:uuid:c3170685-e275-4db1-855d-bb1a56404d55">
  <data>
    <configuration commit-seconds="1653021086"
    commit-localtime="2022-05-20 04:31:26 UTC" commit-user="ntc">
      <snmp>
        <location>EMEA-IE</location>
        <contact>Scott_Grady</contact>
        <community>
          <name>public123</name>
          <authorization>read-only</authorization>
        </community>
        # output omitted for brevity
  </data>
</rpc-reply>
```

As we stated, our goal is to parse the response, saving the community string and authorization type for each community. Rather than just print these to the terminal, let’s save them as a list of Python dictionaries. To do this, you’ll follow the same steps used earlier in [Example 10-32](#xml-findall).

##### Example 10-32. Using `findall()` to iterate over multiple XML objects

```
>>> snmp_list = []
>>> xmlns = "http://yang.juniper.net/junos/conf/snmp"
>>> communities = nc_get_reply.data.findall(f'.//{{{xmlns}}}community')    
>>> for community in communities:                                          
...     temp = {}
...     temp['name'] = community.find(f'.//{{{xmlns}}}name').text          
...     temp['auth'] = community.find(f'.//{{{xmlns}}}authorization').text 
...     snmp_list.append(temp)
...
>>>
>>> print(snmp_list)
[
  {'auth': 'read-only', 'name': 'public123'},
  {'auth': 'read-write', 'name': 'supersecure'}
]
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Instead of using `find()`, youwe use the `findall()` method, which allows extracting multiple elements of the same type instead of only the first match. Using a string formation option, such as f-strings, simplifies xmlns management.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

`communities` contains a list of objects, not only the first match.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Because we need to output the curly brackets in the output within the f-string, we need to escape them via doubling: `{{{`.

You’ve seen how to issue NETCONF requests to obtain configuration data, but now we are going to transition a bit and show how to make configuration changes via NETCONF by using the `<edit-config>` operation.

### Making Junos vMX configuration changes with ncclient

To illustrate how to use ncclient to change the configuration via NETCONF, we will use the `edit_config()` method of the `device` object, which maps directly to the `<edit-config>` NETCONF operation. Following the previous example, now we’re going to configure a new SNMP community string.

The ncclient `edit_config()` method takes two mandatory arguments. The first one, called `<target>`, defines which configuration data store is going to get modified in the request. Valid data stores are running, startup, and candidate. The second parameter, called `<config>`, needs to be an XML string or object that defines the requested configuration changes.

Therefore, we need to construct the `<config>` that matches the expected format. The easiest way to get an understanding of the expected data structure is to use it from the `get` request, as shown in [Example 10-31](#apis-ncclient-get-snmp). Then, with this reference, we can construct a new XML configuration object. Let’s add a new community string called `myNewCommunity` that has `read-only` privileges:

```
>>> config_filter = """
... <config>
...   <configuration>
...     <snmp>
...       <community>
...         <name>myNewCommunity</name>
...         <authorization>read-only</authorization>
...       </community>
...     </snmp>
...   </configuration>
... </config>
... """
```

###### Note

You need to encapsulate this document in one final tag: `<config>`. This is often required when you’re using the `<edit-config>` operation, as covered in [“Using NETCONF”](#apis-netconf).

To change the candidate data store with the new SNMP community, you call the `edit_config()` method:

```
>>> response = device.edit_config(target='candidate', config=config_filter)
>>> print(response)
<rpc-reply message-id="urn:uuid:56584f09-24d2-4e28-aa55-e583bf9d2ff2">
  <ok/>
</rpc-reply>
```

If you check the configuration via the CLI or make a `get` request, you’ll see a new community string on the device.

#### Performing NETCONF delete/replace operations with the ncclient

You’ve seen how to make a configuration change on the device by using the `<edit-config>` operation. The default edit operation is `merge`. However, more operations are available via the XML `operation` attribute.

After adding the SNMP community `myNewCommunity`, we are going to remove it by using the `delete` operation. In this case, we need to construct the new `<config>` with `operation="delete"` in the `<community>` tag. Notice that only the `<name>` tag is required to identify the object:

```
>>> config_filter = """
... <config>
...   <configuration>
...     <snmp>
...       <community operation="delete">
...         <name>myNewCommunity</name>
...       </community>
...     </snmp>
...   </configuration>
... </config>
... """
>>> response = device.edit_config(target='candidate', config=config_filter)
```

The `merge` and `delete` operations allow managing the configuration from its current state. But what if you want to implement a declarative approach, in which you don’t need to care about the current state, but only the final one?

There are a few ways to go about *replacing* a given hierarchy of XML configuration. One option is to make an API call to configure all desired SNMP community strings, and then retrieve all currently configured SNMP communities in another API call, loop over the response, and issue a `delete` operation per community for any not desired. While this approach is not terrible, NETCONF offers a better way—as you already know, of course.

With NETCONF, you can use the `replace` operation instead of `merge` or `delete`. This is the same as doing a PUT with RESTCONF. You define the `replace` operation (`<snmp operation="replace">`) and then define the desired SNMP community name and privilege.

When you start experimenting with the `delete` and `replace` operations, you need to be extremely careful. The `merge` operation is the default for a very good reason—​it enables you to only add or update a configuration. More importantly, if you put the `operation="delete"` line at the wrong place in the XML hierarchy, it could have a catastrophic effect on the network. For instance, placing the `replace` operation as an attribute in the `<snmp>` tag replaces the *full* configuration of SNMP. As we said with RESTCONF PUT, the same is true with NETCONF `replace` operations; be aware of their power.

###### Warning

Always make sure to test in a lab or sandbox environment first. Do *not* test full `replace` operations in production!

Now, after exploring NETCONF automation with Juniper vMX, we want to give a glimpse into using it for Cisco IOS XE to show another implementation.

### Using ncclient with Cisco IOS XE

To illustrate the usage of the XPath filter instead of the subfilter one, we will use Cisco IOS XE, which implements this *capability*. In this example, we want to extract the configuration for a specific interface (`GigabitEthernet1`).

```
>>> from ncclient import manager
>>> device = manager.connect(
>>>     host='csr1', port=830, username='ntc',
>>>     password='ntc123', hostkey_verify=False,
>>> )
>>> nc_get_reply = device.get(
...   ('xpath', '/interfaces/interface[name="GigabitEthernet1"]/config') 
... )
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The XPath filter injects `[name="GigabitEthernet1"]` in the path.

Now, as in [Example 10-32](#xml-findall), you use `find()` to traverse the XML structure to locate the data you are interested in. In this case, let’s extract the `description` of the interface `GigabitEthernet1`:

```
>>> description = nc_get_reply.data.find(
...   './/{http://openconfig.net/yang/interfaces}description')
>>> interface.text
'MANAGEMENT_DO_NOT_CHANGE'
```

As more vendors and operating systems support vendor-neutral data models, you’ll be able to issue the same exact API call against those devices, simplifying working with various device types. Until that point comes, you’ll need to understand the XML objects supported per NOS.

### Understanding vendor-specific NETCONF operations

We have been focusing on the two most commonly used methods in ncclient—namely, `<edit-config>` and `<get>`. However, as you may have noticed earlier in this chapter, many more methods are available when working with NETCONF and ncclient. Here are a few of those:

commit()Commits a candidate configuration to the active running configuration.

copy_config() and delete_config()Creates or replaces, and deletes, respectively, an entire configuration data store with the contents of another complete configuration data store.

lock() and unlock()For a production environment, you may want to lock the configuration data store before changes are made so that no other person or system can make changes during your NETCONF session. When it’s complete, you can unlock the configuration.

Everything we focused on with the Python-based ncclient was vendor neutral and would work across vendors, assuming you understand how to build the proper XML objects. However, you should understand that not every vendor implements NETCONF the same way even though it is an industry-standard protocol. For example, particular vendors have created their own platform-specific NETCONF operations or created their own methods for ncclient to simplify performing common operations. This is in contrast to NETCONF standard operations such as `<edit-config>`, `<get>`, `<lock>`, `<unlock>`, and `<commit>`.

To use these vendor-specific options when using ncclient, you need to specify the correct platform in the `device_params` parameter when instantiating a device object.

Every example we showed used `device_params={}` because we used industry-standard operations within ncclient. If you choose the vendor-specific methods and operations, you would set the `device_params` parameter to its required value. If you append `device_params={"name": "junos"}` in the `connect()` method, you will find out some custom Juniper RPC operations:

```
>>> device = manager.connect(
...  host='vmx1', port=830, username='ntc',password='ntc123',
...  hostkey_verify=False,device_params={"name": "junos"}
... )
>>> device._vendor_operations.keys()
dict_keys(['rpc', 'get_configuration', 'load_configuration', 'compare_configuration',
'command', 'reboot', 'halt', 'commit', 'rollback'])
```

###### Note

Juniper has developed custom methods within ncclient such as `load_configuration()`, `get_configuration()`, `compare_configuration()`, and `command()`, just to name a few. Several of Juniper’s methods are wrappers to simplify performing common tasks with standard NETCONF operations, and others use Juniper-specific NETCONF RPC operations.

For instance, using the `commit()` method, the `candidate` configuration can be moved to the `running` one, making the changes active:

```
>>> response = device.commit()
>>> print(response)
<rpc-reply message-id="urn:uuid:12a2bea3-7aa3-48dd-bfe8-569ccd84d61d">
  <ok/>
</rpc-reply>
```

After this complete overview of NETCONF (using the ncclient library), we will use the gNMIc Go package, the same we used in its CLI form before, to interact via the gNMI interface programmatically.

## The OpenConfig gNMIc Go Package

In [“Exploring gNMI with gNMIc”](#apis-gnmic), you already used OpenConfig gNMIc to explore gNMI, but via CLI. Here, you will use the inner Go package to build Go scripts, emulating the same operations as before with an Arista EOS switch.

###### Note

In the Python world, the most popular library for gNMI management is [pyGNMI](https://oreil.ly/VKcTa), which offers a similar interaction with gNMI methods as ncclient offers for NETCONF. This is an example of performing a `GetRequest` to a specific path with the pyGNMI library:

```
from pygnmi.client import gNMIclient

with gNMIclient(
    target=('eos-spine1', '6030'), username='ntc',
    password='ntc123', insecure=True
  ) as gnmi_client:
    result = gnmi_client.get(path=[
      'openconfig-interfaces:interfaces', 'openconfig-acl:acl'])
```

As we did in [“gNMI GetRequest”](#apis-gnmi-get), we will start first with a GetRequest operation.

### Using OpenConfig gNMIc to perform a gNMI Get operation

In this example, we create a basic programmatic script with gNMI. It contains the base program structure to interact with the gNMI interface that we will reuse in later examples. To extend your understanding of the gNMIc package, see the online [documentation](https://oreil.ly/Wtarm).

###### Note

To use the OpenConfig gNMIc package, you need to get and install the package first, or manage the Go module dependencies with `go mod`:

```
$ go get github.com/openconfig/gnmic/api
go: downloading github.com/openconfig/gnmic v0.27.1
go: added github.com/openconfig/gnmic v0.27.1
```

[Example 10-33](#apis-gnmic-go-get-config-1) defines the necessary imports. The most important ones are the `openconfig/gnmic` that offers access to the gNMI interface, and the protobuf that is used to manage the data serialization.

##### Example 10-33. gNMIc script, part 1

```
package main

import (
  "context"
  "fmt"
  "log"

  // gnmic package
  "github.com/openconfig/gnmic/api"

  // prototext marshals and unmarshals protocol buffer messages
  // as the textproto format, which offers generic support for text-based
  // request/response protocols
  "google.golang.org/protobuf/encoding/prototext"
)

// helper method to implement the error-checking pattern
func checkError(err error) {
  if err != nil {
    log.Fatal(err)
  }
}

// continues to part 2
```

Continuing the script, in [Example 10-34](#apis-gnmic-go-get-config-2), the five steps to retrieve the device configuration are defined.

##### Example 10-34. gNMIc script, part 2

```
// -> comes from previous

func main() {
  // create a gnmic target
  tg, err := api.NewTarget(
      api.Name("gnmi example"),
      api.Address("eos-spine1:6030"),
      api.Username("admin"),
      api.Password("admin"),
      api.Insecure(true),
  )
  checkError(err)

  // cancelable context releases the associated resources, as soon as the
  // operation is completed or canceled.
  ctx, cancel := context.WithCancel(context.Background())
  defer cancel()

  // create a new gNMI client within the base target, using the previous context
  err = tg.CreateGNMIClient(ctx)
  checkError(err)
  defer tg.Close()

  // create a GetRequest
  getReq, err := api.NewGetRequest(
      // Retrieve the full path, all the configuration
      api.Path("/"),
      // Define the expected payload encoding
      api.Encoding("json_ietf"))
  checkError(err)
  fmt.Println(prototext.Format(getReq))

  // send the created gNMI GetRequest to the gnmic target
  getResp, err := tg.Get(ctx, getReq)
  checkError(err)
  fmt.Println(prototext.Format(getResp))
}
```

###### Note

Notice the common Go pattern for error checking after each operation, wrapped in the `checkError()` function.

Then, it’s time to run the script and check its output:

```
ch10-apis/go_gnmic$ go run get_config.go
path: {}
encoding: JSON_IETF

notification:  {
  timestamp:  1664733418878706841
  update:  {
    path:  {}
    val:  {
      json_ietf_val:  "{\"openconfig-acl:acl\":{\"state\":
      {\"counter-capability\":\"AGGREGATE_ONLY\"}},
      \"arista-exp-eos:arista\":{\"eos\":
      {\"arista-exp-eos-igmpsnooping:bridging\":
      {\"igmpsnooping\":{\"config\":{}}},\"arista-exp-eos-mlag:mlag\":
      {\"config\":{\"dual-primary-action\":\"action-none\"
      "
      # omitted a VERY LONG output
    }
  }
}
```

In this initial example, we targeted the full data set with the `/` path. Now, as in [Example 10-21](#apis-gnmic-get-interfaces-config), we narrow the scope to get the only interfaces’ data section—in particular, its configuration.

The only change from the previous script is changing the `Path` to filter the section `/interfaces/interface/config`, as defined in `go_gnmic/get_interface_​con⁠fig.go`:

```
  getReq, err := api.NewGetRequest(
    // Narrow the scope to the interfaces config
    api.Path("/interfaces/interface/config"),
    api.Encoding("json_ietf")
  )
```

If you run the script with the path change, you get a filtered output:

```
ch10-apis/go_gnmic$ go run get_interfaces_config.go
path:  # omitted path
encoding:  JSON_IETF

notification: {
  timestamp: 1664771809792522887
  update: {
    path: {
      # omitted path
    }
    val: {
      json_ietf_val: "{ 
        \"openconfig-interfaces:description\":\"New Description\",
        \"openconfig-interfaces:mtu\":0,
        \"openconfig-interfaces:name\":\"Management0\",
        \"openconfig-interfaces:type\":\"iana-if-type:ethernetCsmacd\"}"
    }
  }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The interface’s configuration values, with the JSON_IETF encoding

The next step is to interact with the output of the `Get` operation, which we saved in the `getResp` variable.

Evolving from the previous script, in [Example 10-35](#get_interfaces_ex_go) (part of the example script *get_interfaces_description.go*), you narrow the path to the description leaf with `/interfaces/interface/config/description`. Then, you need only to extract its value and start using it.

##### Example 10-35. Using value from the gNMI response

```
  descriptionGnmiValue := getResp.GetNotification()[0].GetUpdate()[0].GetVal() 
  myCurrentDescriptionValue, err := value.ToScalar(descriptionGnmiValue)       
  checkError(err)

  myCurrentDescriptionStr := myCurrentDescriptionValue.(string)                
  fmt.Println("This is my current description: " + myCurrentDescriptionStr)
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Extracts `json_ietf_val` into the `descriptionGnmiValue` variable

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Converts the variable value into a scalar value

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Casts it into a string, and we are ready to use it

If you run the script, you can see how the interface description is retrieved and printed in the screen output:

```
ch10-apis/go_gnmic$ go run get_interfaces_description.go
# omitted previous output

This is my current description: New Description
```

With the current description, we will reuse part of the previous code to update the interface’s description with a new value.

### Using OpenConfig gNMIc to perform a gNMI Set operation

As in [“gNMI SetRequest”](#apis-gnmic-set-interface) via CLI, in [Example 10-36](#apis-gnmic-set-intf-description), you will update the interface description for the `Management0` interface, but programmatically.

##### Example 10-36. gNMIc script to update configuration

```
  myNewDescription := myCurrentDescriptionStr + "_something_else" 

  // create a gNMI SetRequest
  setReq, err := api.NewSetRequest(
      api.Update(                                                 
          // Use XPath to target the description for Management0 interface
          api.Path("interfaces/interface[name=Management0]/config/description"),
          // Define the value to update
          api.Value(myNewDescription, "json_ietf")
      ),
  )
  checkError(err)

  // send the created gNMI SetRequest to the created target
  setResp, err := tg.Set(ctx, setReq)                             
  checkError(err)
  fmt.Println(prototext.Format(setResp))
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We use the previous description value, stored in `myCurrentDescriptionStr`, to create a new description.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `SetRequest` type contains an `Update` object with the path and the value. gNMI supports two `Set` operation modes: update and replace (similar to a PUT versus PATCH in REST APIs).

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

We perform a `Set` operation in the gNMIc target, instead of a `Get`.

We run the script and receive confirmation that the update operation has been performed successfully:

```
ch10-apis/go_gnmic$ go run set_interfaces_description.go
# omitted previous output
response: {
  path: {
    # path omitted
  }
  op: UPDATE
}
timestamp: 1664863404149182568
```

If you retrieve the interface description configuration again, as before, you will see the new description updated.

### Using OpenConfig gNMIc to subscribe to events

As we explained in [“Understanding model-driven telemetry”](#apis-model-driven-telemetry), gNMI’s support for streaming telemetry via the `subscribe` operation was, and still is, one of the main drivers for its adoption. In [Example 10-37](#apis-gnmic-subscription), the goal is to subscribe to interface counters as you did in [“gNMI Subscribe”](#apis-gnmi-subscribe) via the CLI.

##### Example 10-37. gNMIc subscription to interface counters

```
  // create a gNMI subscribeRequest
  subReq, err := api.NewSubscribeRequest(
    api.Encoding("json_ietf"),
    // Select the stream mode, instead of poll
    api.SubscriptionListMode("stream"),
    // Define the subscription scope
    api.Subscription(                  
      // Data container to retrieve
      api.Path("/interfaces/interface/state/counters"),
      // Define the subscription method. Others are on_change and target_defined
      api.SubscriptionMode("sample"),
      // For the sample mode, the sample interval is defined
      api.SampleInterval(10*time.Second),
    ))
  checkError(err)
  fmt.Println(prototext.Format(subReq))

  // start the subscription, identified as sub1, in a new goroutine
  go tg.Subscribe(ctx, subReq, "sub1") 

  // start a goroutine that will stop the subscription after 30 seconds
  go func() {                          
    select {
    case <-ctx.Done():
      return
    case <-time.After(30 * time.Second):
      // If the context is not stopped before, after 30 seconds
      // in this goroutine, it will stop the subscription defined
      // as sub1
      tg.StopSubscription("sub1")
    }
  }()

  // In the main process, starts creating two subscriptions, creating two channels
  // that are read in an infinite loop, until the subscriptions are closed
  // by the other goroutines
  subRspChan, subErrChan := tg.ReadSubscriptions()
  for {                                
    select {
    case rsp := <-subRspChan:
      fmt.Println(prototext.Format(rsp.Response))
    case tgErr := <-subErrChan:
      log.Fatalf("subscription %q stopped: %v", tgErr.SubscriptionName, tgErr.Err)
    }
  }
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`SubscribeRequest` is a *sampling* type, and it targets the `state`, not the `config` container.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `Subscribe()` method is run in a different goroutine (notice the `go` before). This will keep it running while you progress in the script.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This goroutine is in charge to stop the subscription after 30 seconds. The identifier (`sub1`) connects the dots.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The main process will keep reading the subscription responses and errors (via two Go channels) until the subscription is stopped.

###### Note

[Example 10-37](#apis-gnmic-subscription) shows how three flows are executed and communicated to Go. The main one (initializing and printing the output received via channels) is the one managing the subscription, and the one to stop the subscription after a specified number of seconds.

When running the script, you will see the operation summary at the top, with the mode (`SAMPLE`), its interval (10 seconds), and the encoding. Remember that there is another mode type, `on-change`, which only sends data when there is a change in the data source. You can see the output here:

```
ch10-apis/go_gnmic$ go run subscribe_int_counters.go
subscribe:  {
  subscription:  {
    path:  {
      # path omitted
    }
    mode:  SAMPLE
    sample_interval:  10000000000
  }
  encoding:  JSON_IETF
}

update:  {
  timestamp:  1664944947620748134
  prefix:  {
    # prefix omitted
  }
  update:  {
    path:  {
      elem:  {
        name:  "out-octets"
      }
    }
    val:  {
      uint_val:  6243543
    }
  }
  update:  {
    path:  {
      elem:  {
        name:  "out-unicast-pkts"
      }
    }
    val:  {
      uint_val:  31339
    }
  }
  # output omitted for brevity
}
```

We’ve now provided an introduction to using the Python and Go libraries to communicate with modern programmatic network APIs. Now, we are going to shift gears and talk about using SSH in Python, as SSH is still the most widely deployed interface on network devices.

## The Netmiko Python Library

Using CLI commands, SSH has been the de facto way network engineers and operators manage their infrastructure. Commands are passed over a persistent SSH connection to a network device, the device interprets them, and it responds with text that is viewable by a human on a terminal window. SSH does not use structured encoded data such as XML or JSON over the wire. While SSH is not a modern or a programmatic API, it is important to have an understanding of how to use Python to automate network operations with SSH for three reasons:

- Not all devices support a programmatic API.
- You may want to automate the turning on of the API.
- Even if you’re automating a device with an API:
  - It’s good to have a backup plan.
  - Not all operations of a device may be supported with the API. This is not ideal, as it shows immaturity in the underlying API.

In this section, we show how to get started with a popular open source SSH client for Python called *Netmiko*. Netmiko’s purpose is to simplify SSH device management specifically for network devices.

###### Note

Do not underestimate the utility of the SSH Netmiko library, as it’s proven useful in providing a smooth transition from traditional network CLI management to network automation, and it’s heavily used and developed, as you can see in the [Netmiko GitHub Contributors page](https://oreil.ly/xmpee).

We’re focused on Netmiko, as it provides a lower barrier to entry and already understands how to communicate with many network device types. Netmiko has varied support for dozens of device types, including those from Arista, Brocade, Cisco, Dell, HPE, Juniper, Palo Alto Networks, Linux, and many more; check the [documentation](https://oreil.ly/PI_q1) for updated information. The great thing about Netmiko is that the overall usage is common across vendors. Only the commands used are specific to each platform.

###### Note

To install Netmiko, you can use `pip3`:

```
$ pip3 install netmiko
$ pip3 list | grep netmiko
netmiko                           3.4.0
```

The first thing you need to do is import the proper Netmiko device object. This object handles the SSH connection setup, teardown, and the sending of commands to the device. You used a similar approach with ncclient:

```
>>> from netmiko import ConnectHandler
```

You’re now ready to establish an SSH connection to the network device and create a Netmiko device object. The `ConnectHandler` object handles the SSH connection to the network device:

```
>>> device = ConnectHandler(
...   host='nxos-spine1',
...   username='admin',
...   password='admin',
...   device_type='cisco_nxos'
... )
```

At this point, there is an active SSH connection from Python using Netmiko with a Cisco NX-OS switch. Because each platform supports different commands and handles SSH differently, you must provide the `device_type` parameter when instantiating an instance of the `ConnectHandler` object.

Let’s check the available methods for our new device object called `device` by using the `dir()` function:

```
>>> dir(device)
[
  # methods removed for brevity
  'cleanup', 'clear_buffer', 'close_session_log', 'commit', 'config_mode',
  'conn_timeout', 'device_type', 'disable_paging', 'disconnect', 'enable',
  'encoding', 'establish_connection', 'exit_config_mode', 'exit_enable_mode',
  'select_delay_factor', 'send_command', 'send_command_expect',
  'send_command_timing', 'send_config_from_file', 'send_config_set',
]
```

As a network engineer, you should feel pretty comfortable with many of the attributes shown from the `dir()` function, as they are very network centric. We’ll walk through a few of them now.

### Verifying the device prompt

Use the `find_prompt()` method to check the prompt string of the device:

```
>>> device.find_prompt()
'nxos-spine1#'
```

### Entering configuration mode

Because Netmiko understands multiple vendors and what configuration mode means, it has a method to go into configuration mode that works across vendors; of course, the commands Netmiko uses under the covers may be different per OS:

```
>>> device.config_mode()
>>>
>>> device.find_prompt()
'nxos-spine1(config)#'
```

###### Warning

Some NOSs could fail to enter `config_mode()` if there is already a CLI session in this mode.

### Sending commands

The most common operation you’re going to perform with Netmiko is sending commands to a device. Let’s look at a few methods to do this.

To simply send a single command to a device, you can use one of three methods:

send_command_expect()This method is used for long-running commands that may take a while for the device to process (`show run` on a larger chassis, `show tech`, etc.). By default, this method waits for the same prompt string to return before completing. Optionally, you can pass what the new prompt string is going to be should it change based on the commands being sent.

send_command_timing()This method is for short-running commands; it is timing based and does not check the prompt string.

send_command()This is an older method in Netmiko, which now acts as a wrapper for calling `send_command_expect()`. Thus, `send_command()` and `send_command_expect()` perform the same operation.

Let’s look at a few examples. Here you’re gathering a `show run` and printing out the first 176 characters for verification:

```
>>> show_run_output = device.send_command('show run')
>>>
>>> print(show_run_output[:176])

!Command: show running-config
!Running configuration last done at: Wed Oct  5 04:18:12 2022
!Time: Wed Oct  5 04:23:22 2022

version 9.3(3) Bios:version
hostname nxos-spine1
```

Send a command that changes the prompt string—remember you’re still in configuration mode when you enter `device.config_mode()`—as follows:

```
>>> output = device.send_command_expect('end')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.8/site-packages/netmiko/base_connection.py",
  line 1582, in send_command_expect
    return self.send_command(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/netmiko/utilities.py", line 500,
   in wrapper_decorator
    return func(self, *args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/netmiko/base_connection.py",
   line 1535, in send_command
    raise IOError()
OSError: Search pattern never detected in send_command: nxos\-spine1\(config\)\#
>>>
```

The stack trace shown is expected, as `send_command_expect()` expects to see the same prompt string by default. Since you are in config mode with the current prompt string of `nxos-spine1(config)#`, when you type the command `end`, the new prompt string is going to be `nxos-spine1#`.

To execute a command that changes the prompt string, you have two options. First, you can use the `expect_string` parameter that defines the new and expected prompt string:

```
>>> output = device.send_command_expect('end', expect_string='nxos-spine1#')
>>>
```

Second, you can use the `send_command_timing()` method, which is timing based and doesn’t expect a particular prompt string to be found again:

```
>>> output = device.send_command_timing('end')
>>>
```

You’ve shown three methods thus far on how to send commands with Netmiko. Let’s look at two more useful ones, as you may want to send several commands at once instead of one at a time.

Netmiko also supports a method called `send_config_set()` that takes a parameter that must be iterable. We’ll show this using a Python list, but you can also use a Python set:

```
>>> commands = [
  'interface Ethernet1/1',
  'description configured by netmiko',
  'shutdown'
]
>>>
>>> output = device.send_config_set(config_commands=commands)
>>>
>>> print(output)
nxos-spine1(config)# interface Ethernet1/1
nxos-spine1(config-if)# description configured by netmiko
nxos-spine1(config-if)# shutdown
nxos-spine1(config-if)# end
nxos-spine1#
```

This method checks whether you’re already in configuration mode. If you aren’t, it goes into config mode, executes the commands, and by default, exits configuration mode. You can verify this by viewing the returned output, as shown in the previous example.

Finally, Netmiko has a method that can execute commands from a file. This allows you to do something like create a Jinja template, render it with variable data, write the data to a file, and then execute those commands from the file with the Netmiko method `send_config_from_file()`. Building on what we covered in Chapters [6](ch06.html#python) and [9](ch09.html#templating), let’s see how to perform this workflow in [Example 10-38](#apis-netmiko-commands-file).

##### Example 10-38. Sending commands from a file with Netmiko

```
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

device = ConnectHandler(
  ...
)

interface_dict = {
    "name": "Ethernet1/2",
    "description": "Server Port",
    "vlan": 10,
    "uplink": False
}

# Create the custom commands, combining the Jinja config.j2 template
# with the data defined in interface_dict
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("config.j2")
commands = template.render(interface=interface_dict)

# Store the CLI commands in a local file
filename = 'nxos.conf'
with open(filename, 'w') as config_file:
    config_file.writelines(commands)

# Send CLI commands directly from the file
output = device.send_config_from_file(filename)

# Use show commands to verify that the change succeeded
verification = device.send_command(f'show run interface {interface_dict["name"]}')
print(verification)

device.disconnect()
```

Everything shown in this example was covered in prior chapters. Note that *config.j2* must be created for this to work, and for this example, that the Jinja template is stored in the same directory from where we entered the Python interpreter. The content of the template is from [Example 9-3](ch09.html#templates-switchport-configuration-3), and is as follows:

```
interface {{ interface.name }}
 description {{ interface.description }}
 switchport access vlan {{ interface.vlan }}
 switchport mode access
```

Finally, when you’re done working with Netmiko, you can gracefully disconnect from the device by using the `disconnect()` method. If we run the script, we will see the verification of the new interface configuration according to the template:

```
ch10-apis/python_netmiko$ python3 send_commands_from_file.py

!Command: show running-config interface Ethernet1/2
!Running configuration last done at: Wed Oct  5 04:38:54 2022
!Time: Wed Oct  5 04:38:55 2022

version 9.3(3) Bios:version

interface Ethernet1/2
  description Server Port
  switchport access vlan 10
```

###### Tip

Context managers in Python help manage setup and teardown operations. For an SSH library such as Netmiko, a context manager seems ideal. Thus, Netmiko provides one, `netmiko.ConnectHandler`, that will take care of establishing the SSH session at the beginning, and tearing it down when exiting it (so you don’t leave open SSH connections):

```
with netmiko.ConnectHandler(**device_config) as device:
    device.send_command("show run")
```

So far, you have shown the benefits of Netmiko, allowing interaction with a traditional CLI interface programmatically. Unfortunately, the unstructured data used in the CLI output is a big drawback in the automation journey. Hopefully, we have some helpers available.

### Empowering Netmiko with TextFSM and NTC Templates

[TextFSM](https://oreil.ly/cVuCh) is an open source project built by Google that converts semiformatted text (the CLI output) to structured data, using templates. So, for each CLI output, you need to provide a specific template that NTC Templates solves.

[NTC Templates](https://oreil.ly/A1svX) is an open source project sponsored by Network to Code that provides a large collection of TextFSM templates for a lot of [network vendors](https://oreil.ly/IhLYy).

###### Note

You don’t need to install TextFSM or NTC Templates because they are dependencies of Netmiko, so they are already installed.

In [Example 10-39](#apis-ntc-templates-output), we demonstrate how to use NTC Templates in two steps:

1. Get raw CLI output from Netmiko and store it as a string.
2. Use the NTC Templates parser to transform the raw output into structured data.

##### Example 10-39. Using NTC Templates to get structured data from Netmiko output

```
>>> from netmiko import ConnectHandler
>>> device = ConnectHandler(
...     host='nxos-spine1',
...     username='admin',
...     password='admin',
...     device_type='cisco_nxos'
... )
>>> show_interfaces_raw = device.send_command('show int brief')
>>> show_interfaces_raw[:150]
'\n-------------------------------------------------------------------------------\n
Port   VRF          Status IP Address                              S'
>>>
>>> from ntc_templates.parse import parse_output
>>> show_interfaces_parsed =  parse_output(
...     platform="cisco_nxos",    
...     command="show int brief", 
...     data=show_interfaces_raw, 
... )
>>> show_interfaces_parsed[0]
{
  'interface': 'mgmt0', 'vrf': '--', 'status': 'up', 'ip': '10.0.0.15',
  'speed': '1000', 'mtu': '1500', 'vlan': '', 'type': '', 'mode': '',
  'reason': '', 'portch': '', 'description': ''
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Indicates the reference platform. Each will have different parsers.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Identifies the specific template within a platform because each CLI command may have different data.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The raw input data to be parsed.

Luckily, since its 2.0.0 release, Netmiko has the implicit support of NTC Templates, simply using the `use_textfsm` argument:

```
>>> show_interfaces_parsed_directly = device.send_command(
...  'show int brief',
...   use_textfsm=True,
... )
>>> show_interfaces_parsed == show_interfaces_parsed_directly
True
```

This functionality is just combining the two steps presented in [Example 10-39](#apis-ntc-templates-output).

###### Note

Netmiko is also used as the primary SSH driver for devices within NAPALM, a robust and multivendor network Python library for configuring devices and retrieving data. We cover NAPALM in [Chapter 12](ch12.html#automationtools).

This concludes using Netmiko to automate SSH-based network devices. You’ve now seen how to automate various types of network devices across a range of API types, no matter the device or API type you need to work with.

# Summary

This chapter introduced the available types of APIs in the context of networking: HTTP-based APIs (both RESTful and non-RESTful), NETCONF, RESTCONF, and gNMI. After an introduction using command-line tools, we went through how these interfaces can be leveraged with the Go and Python programming languages. All these programmatic interfaces allow a much more efficient automation pattern than the traditional CLI with unstructured data. However, even nowadays, a lot of network devices are still out there where the main interface is still an SSH connection. Because of this, we also covered the Netmiko Python library.

At this point, you may be wondering, “Which network interface should I use?” The answer is, it depends. It depends on the device you are trying to automate—including the interfaces it supports and the capabilities you need to use. Another important factor is the tooling you prefer. Having tools that allow effective and efficient automation is key to success. One way or another, all the data-model interfaces share one big challenge that slows their adoption: the translation between standard or community data models to the device models does not always cover all the features or may not be fully supported. In the end, the goal is to change the data in the device’s data store, and these data models come with inertia. This is the reason text-based configurations are still the main interface for many network devices.

As you continue your journey automating network devices with various types of APIs, remember that there is no magic here—​you need to perform due diligence to understand how to use any given API and to know which options each platform offers over each interface.

In the next chapter, we shift gears and introduce the importance of using source code control to support network automation and programmability.
