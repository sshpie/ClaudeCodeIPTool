# Chapter 23. Web Services

**IN THIS CHAPTER**

- Hypertext Transfer Protocol
- HTTP request/response mechanism
- Different technologies used to create Web services
- Service Oriented Architecture

In this chapter, I introduce the basis for creating and developing Web services. As more applications begin to migrate to the Internet, Web services will become increasingly important.

The Hypertext Transfer Protocol (HTTP) is the Application layer protocol that browsers use to transfer information. HTTP uses plain-text requests from a user agent or client to the server to request a resource, and the server responds with the appropriate resource in the appropriate format, provided that the request is valid. A set of status codes is defined to aid in negotiation and execution. In this chapter, you learn how HTTP messages are composed and executed.

HTTP can transfer information using HTML or XHTML, which, when processed by a browser, describes how to create and format a Web page. Web pages can contain either static or dynamic content. Some of the different ways in which dynamic content is controlled across a network are considered — server-side and client-side scripting, and CGI in particular.

A Web service is a mediated client-server application. An example of how a Web service can be implemented using SOAP as the communication or messaging protocol between service requestor and service provider will be presented. In a Web service, transactions are mediated by a service broker that runs on a third system. The purpose of the service broker is to make services discoverable and to list the capabilities of a service, as well as to pass information between the client and server.

A Service Oriented Architecture (SOA) is a framework that can be used to build distributed applications. The goal of an SOA is to allow a client to create and manage applications using services running on other systems. A number of technologies and standards have been applied to creating SOAs and are presented to you in this chapter.

# The Hypertext Transfer Protocol

The Hypertext Transfer Protocol (HTTP) is the native Application layer protocol used by Web servers and client Web browsers to transfer information between each other. HTTP uses a request/response mechanism, the request being composed of ASCII text containing one or more action verbs, and the response formulated as text formatted in a manner similar to the use of MIME in e-mail. MIME or Multipurpose Internet Mail Extensions is a text formatting standard that allows e-mail sent over the Internet to use characters in addition to ASCII, attach files to e-mails, divide messages into sections, and have headers that contain non-ASCII characters. Virtually all e-mail currently sent over the Internet is in MIME sent over SMTP.

HTTP is a stateless protocol; the information necessary to act on requests and responses is contained within the messages themselves. This frees the client and the server from the overhead of storing and managing user information. However, because HTTP is stateless, if a Web site needs to manage user data to customize a user's experience, it is forced to use other methods. The commonly used methods are writing and modifying cookies, authenticated logins for sessions, and server-side sessions.

HTTP is a standard of the IETF (Internet Engineering Task Force), and the latest version of the standard is HTTP 1.1, as defined in RFC 2616 (`tools.ietf.org/html/rfc2616`); its development was overseen by the World Wide Web Consortium (`www.w3.org`), which is responsible for the development of the Internet protocol suite (including HTTP). Although HTTP is almost always used on a TCP/IP network, the protocol's specification does not require TCP as a transport, only that the data that arrives be validated for its integrity.

In a typical HTTP exchange, a client or user agent sends a request out of outgoing port 80 to a destination server on the internetwork, which is listening on incoming port 80. The destination is formatted in the familiar Uniform Resource Locator (URL) format:

```
http://URL
```

Examples of this format include `http://www.w3.org/2002/03/tutorials` and http://192.168.1.1/index, both of which are pointers to a particular resource. In the former case, the URL points to a folder called *tutorials*, while in the latter case, the URL points to a file called index.html. The reason that the latter private network address doesn't need an HTML extension on the filename is that browsers automatically assume that it is an HTML file. The resource is uniquely identified because the server must have a unique entry in the TCP/IP namespace, and because the resource must also be uniquely identified in the file system of the server. When you press the Enter key or click the Refresh button in a browser, you are requesting that the server return the resource, which is then displayed in the browser.

### Note

The term Uniform Resource Name (URN) is a related concept where a resource is identified by its location in a namespace — for example, a book's Dewey Decimal number in a library catalog. URLs and URNs are both resource identifiers and belong to a general category of identification systems called Uniform Resource Identifiers (URIs).

## HTTP requests

An HTTP request consists of the following parts:

1. **Header**. The header lines can contain a request for information or establish a condition. Header lines are optional, but in HTTP 1, the Host header is required.Examples would be: Accept: text/plain, Host: `www.whitehouse.gov`, or Range: bytes=200-500. The first line sets the content type to plain text, the second line gives the domain name of the server or virtual host, and the third line requests only a range of the resource's data that is being requested.
2. **Request line**. A request line contains a method (see below) or verb and the resource upon which the action is processed.For example, `GET` `www.hulu.com` would return the default page (often `index.html`) for that domain, unless the Web site has dropped a cookie on your system that returns a different page.
3. **Empty line(s)**, defined as a Carriage Return (CR) followed by a Line Feed (LF), are required to separate the header and the request line from any other parts.In ASCII, the CR symbol is the 13th character (015 octal, 0D hex), and the LR or newline character is the 10th character (012 octal, 0A hex) of the lower 127-character ASCII set. You enter these characters in most editors using the Enter key for CR and the Shift+Enter keystroke for LR.
4. **Body (optional)** is the information returned by the server. If you requested a Web page, the HTML portion of the reply is sent back to your browser as the body part.

However, an HTTP message can be as simple as a one-line command, such as:

```
GET <URL>
```

[Figure 23.1](ch23.html#the_request_for_the_google_home_page_sho) shows the HTTP request `GET` `www.google.com` as displayed by the Live HTTP Headers extension of Mozilla Firefox. The `GET` command is followed by the optional fields, and the server responds with a 304 Not Modified status message. The first of the needed Web resources (the Google logo) then begins to be transferred. Another tool that is recommended for viewing HTTP requests is Fiddler, a browser independent tool that you can find at `www.fiddler2.com/fiddler2/`.

Notice the line Keep-Alive with a value of 300 seconds. This parameter was added in HTTP 1.1 in order to maintain persistent connections. In prior versions of HTTP, a connection closed when the request was satisfied. Because HTTP 1.1 can rely on a persistent connection, it can transfer information using the chunked transfer encoding method. Normally, data sent as an HTTP response is sent in one block with its length indicated in the Content-Length header field. However, with chunked transfer, encoding the data can be broken up and set into compressed pieces. Chunking allows the compression to be done on the fly instead of before transfer, which speeds up the process.

The second improvement that Keep-Alive allows is called HTTP pipelining. In HTTP pipelining, several HTTP requests are sent through a single socket without requiring a response from the server. Pipelining can result in significant improvements in the time it takes for your browser to display a Web page, particularly over low-bandwidth connections.

Other methods and verbs that HTTP 1.1 uses are shown in [Table 23.1](ch23.html#http_methods_or_verbs). The HTTP standard prescribes that some methods such as `GET`s request information without changing the server's contents or states. Methods of this type are deemed safe. However, there is no mechanism that enforces this requirement. An automated retrieval system such as a Web crawler or robot can therefore index a site using successive `GETs` without expecting any changes to be made. A safe request will still be logged, cached, and can alter a Web page's counter.

![The request for the Google home page showing HTTP message composition in the Live HTTP Headers extension of Firefox](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2301.png)

**Figure 23.1. The request for the Google home page showing HTTP message composition in the Live HTTP Headers extension of Firefox**

Some methods act on a resource once, no matter how many times you send the request. `DELETE` can only delete a resource once; any subsequent `DELETE`s will not find the resource on the server and will be ignored. A method such as `DELETE`, which works only once no matter how many times you request it, is called idempotent. An example of a method that is not idempotent is the `POST` method. On a Web form, the Submit button is usually a trigger for a `POST` request. That's why many Web forms ask you not to press the Submit button more than once for the transaction. Again, although HTTP 1.1 prescribes that a method be idempotent or not, there is no enforcement mechanism that ensures that this behavior is followed by a particular Web server.

**Table 23.1. HTTP Methods or Verbs**

| Method | Action | Safe | Idempotent |
| --- | --- | --- | --- |
| `CONNECT` | Creates a tunnel using an established network connection. `CONNECT` is most often used to send encrypted data over secure transport (for example, HTTPS). | No | No |
| `DELETE` | Deletes the specified resource. | No | Yes |
| `GET` | Requests a resource. This is used by the Refresh button of a browser. | Yes | No |
| `HEAD` | Requests a resource, but without requiring a body section in the reply. This is used for retrieving metadata. | Yes | No |
| `OPTIONS` | Requests that the server return a list of methods that the server supports for the resource that is specified. | Yes | No |
| `POST` | Sends data to a resource for further action. This is used in the Submit button of a browser where the page has data to be acted on: forms, password validation, and so on. | No | No (mostly) |
| `PUT` | Uploads a resource. | No | Yes |
| `TRACE` | Requires an echo response for a request. `TRACE` allows the action of any intermediaries to be examined. | Yes | No |

## HTTP status codes

A response to an HTTP request returns the resource requested. However, if there is a problem, the Web server will return a one-line status code, along with explanatory text, to the client (user agent), which interprets the response and either displays it in the browser or acts upon it. The classic "404 – Not Found" error message is displayed when a server cannot respond to the request for some reason. Each browser can display different messages, but the explanations for each status code, shown in [Table 23.2](ch23.html#http_status_codes-039), are the HTTP 1.1 recommendations.

**Table 23.2. HTTP Status Codes**

| Class | Status Code | Description | Notes |
| --- | --- | --- | --- |
| Source: `www.w3.org/Protocols/rfc2616/rfc2616-sec10.html`. |  |  |  |
| 1xx |  | Informational | A provisional response that is a status line and optional headers terminated by an empty line. This only applies to HTTP 1.1. |
|  | 100 | Continue | The client should continue with the request. |
|  | 101 | Switching Protocols | The server will act on the client request for a change in the application protocol as indicated in the Upgrade message header field. |
| 2xx |  | Successful | The request was received, understood, and accepted by the server. |
|  | 200 | OK | The request succeeded. |
|  | 201 | Created | The request has been fulfilled and the new resource has been created. |
|  | 202 | Accepted | The request has been accepted, but the processing is not complete. |
|  | 203 | Non-Authoritative Information | The data returned by the server in the header is not the definitive information from the origin server, but is obtained from a local or third-party copy. The information may be either a subset or superset of the original version. |
|  | 204 | No Content | The server has fulfilled the request, but does not need to return a resource. Additional metadata may be returned by the server if the request is altered. |
|  | 205 | Reset Content | The server has fulfilled the request and the client should refresh the document view. |
|  | 206 | Partial Content | The server has fulfilled part of the `GET` request for the resource. The request must have a Range header field, and may include an If-Range header field if the request is conditional. |
| 3xx |  | Redirection | Further action needs to be taken by the client to fulfill the request. |
|  | 300 | Multiple Choices | The requested resource corresponds to a set of possible replies requiring that the client specify their choice. |
|  | 301 | Moved Permanently | The requested resource has been moved to a different URI and any future references should use the returned URIs. |
|  | 302 | Found | The requested resource resides temporarily under a different URI. |
|  | 303 | See Other | The response to the request can be found under a different URI and should be retrieved using a `GET` method for that resource. |
|  | 304 | Not Modified | If the client has performed a conditional `GET` request and access is allowed, but the document has not been modified, the server should respond with this status code. |
|  | 305 | Use Proxy | The requested resource must be accessed through a proxy indicated in the URI contained in the Location field. |
|  | 306 | Unused | This status code is no longer used, but the number is held in reserve. |
|  | 307 | Temporary Redirect | The requested resource resides temporarily at a different URI. |
| 4xx |  | Client Error | A client error is detected by the server. Clients are directed to display the error to the user. |
|  | 400 | Bad Request | The request could not be processed because the syntax is malformed. |
|  | 401 | Unauthorized | The request requires user authentication. The response must contain a WWW-Authenticate header field with a challenge applicable for the requested response. |
|  | 402 | Payment Required | This code is reserved for future use. |
|  | 403 | Forbidden | The server understood the request but will not honor it. Authorization will not help and the request should not be repeated. |
|  | 404 | Not Found | The server cannot find a matching URI for the request. The condition may be permanent or temporary. |
|  | 405 | Method Not Allowed | The method in the request is not allowed for the type of resource that is indicated in the URI. The server response must indicate in an Allow header which methods are valid for the requested resource. |
|  | 406 | Not Acceptable | The resource identified by the request is not capable of a response that has appropriate content characteristics, as specified by the request Content –Type header field. |
|  | 407 | Proxy Authentication Required | The client must first authenticate itself with the proxy. The proxy must return a Proxy-Authenticate header field with the appropriate challenge for the proxy to obtain access to the requested resource. This is similar to the 401 message. |
|  | 408 | Request Timeout | The client did not produce a request within the time that the server dedicated to servicing the request. The request should be repeated if necessary. |
|  | 409 | Conflict | The request cannot be completed due to a conflict relating to the current state of the resource. For example, the resource may be locked. The response body should identify the source of the conflict. |
|  | 410 | Gone | The requested resource is no longer available at the server and cannot be located. |
|  | 411 | Length Required | The server refuses to accept the request without a Content-Length header field defining the length of the message body to be returned. |
|  | 412 | Preconditioned Failed | The Preconditioned in the request header field evaluates to false at the server. |
|  | 413 | Request Entity Too Large | The server denies the request because the request would result in an unacceptably long response. |
|  | 414 | URI Too Long | The server is refusing service because the URI is longer than the server is willing to interpret. |
|  | 415 | Unsupported Media Type | The server is refusing the request because the format of the requested resource does not conform to the requested method. |
|  | 416 | Requested Range Not Satisfied | This response indicates that the request contains a range in the Range header field that is not valid for the current resource. |
|  | 417 | Expectation Failed | The expectation in the Expect header could not be met. |
| 5xx |  | Server Error | The server detects an error that is interfering with a response. |
|  | 500 | Internal Server Error | The server encountered an unexpected error. |
|  | 501 | Not Implemented | The server does not have the necessary capabilities to process the request. This can also indicate that the server does not recognize the request. |
|  | 502 | Bad Gateway | The server as a gateway or proxy gets an invalid response from an upstream server needed to process the request. |
|  | 503 | Service Unavailable | The server is temporarily unable to process the request. Most often, this error occurs due to a loading problem or when the server is down for maintenance. |
|  | 504 | Gateway Timeout | The server as a gateway or proxy did not receive a response from an upstream server in the time allotted. |
|  | 505 | HTTP Version Not Supported | The server does not support the HTTP protocol version required. |

HTTP has been enhanced in order to create secure connections. The first of these methods appeared in early versions of HTTP and is the HTTPS protocol that is described in more detail in the following section. When you request a resource using `https://` the browser encrypts the message using SSL/TLS. In HTTP 1.1, an Upgrade header was added to the HTTP protocol. In a typical exchange between client and server, the client requests an encrypted resource:

- `GET /encrypted-area HTTP 1.1`
- `Host: www.domain.ext`

to which the server would reply:

- `HTTP/1.1 426 Upgrade Required`(status message)
- `Upgrade: TLS/1.0, HTTP/1.1` (these are the required protocols)
- `Connection: Upgrade`

The response from the server indicates a client error relating to the use of legacy HTTP (1.0 and earlier).

## Static versus dynamic pages

HTTP provides the Application level control that allows Web resources to be transferred from a Web server to a browser. These resources are described using the HTML, XHTML, or a related markup language, and from the content, a Web page is built by the browser. When a Web page is built using a set of stored files from the server, it is referred to as a static Web page.

When the Web page is built based on variable criteria and the page is constructed individually for a client, it is referred to as a dynamic Web page. Often dynamic Web pages are displaying information stored in a database. Web pages can be constructed and modified by scripts, either client-side or server-side. JavaScript is an example of client-side code and is an executable file bearing a `.js` extension. The advantage of client-side code is that it distributes the computing load, making it easier for Web services to scale. The downside, as you well know, is that executing code on client systems is a potent vector for security threats.

Server-side scripts impact a Web server's performance and often require that supporting software be installed on the server. Some scripting capabilities are almost always available on Web servers, with Common Gateway Interface (CGI) being a prime example. The tendency these days is to run Web servers as spare as possible in order to lower their attack surface, which means that it is not a given anymore that Web servers support the dynamic methods of your choice. When a CGI script is called, data in the form of environmental variables are passed to the CGI script. After the script runs, the results are returned by the script as standard HTTP headers and a MIME type, and forwarded to the requesting client (user agent).

The problem with server-side scripts in general, and with CGI in particular, is that for every request, an executable program must be loaded into system memory to process data. This approach is one that doesn't scale well. Alternatives to CGI have been developed that extend different Web servers so that the script runs in the Web server itself and does not have to be instantiated. Different Web servers use different add-ons or extensions — Apache modules, Netscape NSAPI, and IIS ISAPI — and these APIs are published and available for public use. Other versions of CGI, notably FastCGI and Simple Common Gateway Interface (SCGI), have been developed to enable CGI applications to run multiple scripts at once and thus eliminate the need to instantiate these scripts more times than necessary.

# Web Services

A classic Web service has the elements shown in [Figure 23.2](ch23.html#a_web_service_application_implemented_wi): both a service provider (server) and service requester (client), as well as a service broker. Information is sent between the service requester and the service provider in a form that allows the requestor to use the service to obtain a result. As shown in [Figure 23.2](ch23.html#a_web_service_application_implemented_wi) the message passing protocol is SOAP, and the data is formatted in the WSDL or Web Services Description Language.

![A Web service application implemented with SOAP](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2302.png)

**Figure 23.2. A Web service application implemented with SOAP**

Many implementations of Web services use the SOAP Application layer protocol for their message to pass between requester and service provider. SOAP, which originally stood for Simple Object Access Protocol (but now stands for SOAP) formats data in XML and uses Remote Procedure Calls (RPCs) as its inter-application communication (IAC) mechanism. SOAP is now a W3C recommendation, currently at version 1.2.

SOAP messages can be transported using HTTP, HTTPS, and SMTP. It is an open industry standard. The fact that SOAP uses XML is both an advantage and a disadvantage. XML makes the messages both readable and editable with tools as simple as a text editor. The use of XML results in slower speeds than a binary data representation in situations of high Web service loading.

Other IAC standards — such as CORBA (`www.omg.org/technology/documents/formal/components.htm`), General Inter-ORB Protocol (GIOP; `www.omg.org/spec/CORBA/3.1`), ZeroC's Internet Communications Engine (ICE; `http://zeroc.com/ice.html`), and Microsoft's Distributed Component Object Model (DCOM; `http://msdn.microsoft.com/library/cc201989.aspx`) — are message-passing methods for distributed application development, but they use binary data for their message format. Binary XML is under development at a number of companies and may eventually be standardized and adopted.

The important characteristics in SOAP or any other IAC message-passing protocol is that it:

- Allow for transport on existing networks and be firewall friendly
- Be platform and language independent
- Run over HTTP, and preferably other protocols
- Be extensible for use by different vendors

Web services are not a classic client-server architecture. They use a service broker to mediate interaction between requestor and provider. In a Web service, information about the different services available on the server is sent in a special version of XML called Web Services Description Language (WSDL) to the service broker, where that data is then passed to the client. GoToMyPC is an example of a Web service, and its architectural diagram, shown in [Chapter 32](ch32.html), is an example of this type of construction.

The service broker, while not required by SOAP, makes it easier to generate the client-side code that different service architectures, such as Java and .NET, require. Many service brokers use the Universal Description, Discovery, and Integration (UDDI) XML registry standard. UDDI is an open standard of OASIS (the Organization for the Advancement of Structured Information Standards; `www.oasis-open.org/home/index.php`), as are the WDSL markup format and many others. UDDI was meant to be a core Web service standard implemented in the form that you see in [Figure 23.2](ch23.html#a_web_service_application_implemented_wi), and formed the basis for storing what are referred to as white pages, yellow pages, and green pages. White pages store user ID and associated data; yellow pages store categories used in different industries to classify different systems; and green pages store technical information about services used by businesses.

The Web Services Interoperability Organization (WS-I) is an industry group that promotes interoperability between different Web services. Its work involves testing and recommending interoperability guidelines. WS-I publishes three specifications: WS-Security based on SOAP, WS-Reliability based on an OASIS standard, and WS-Transactions.

An alternative set of specifications called the Web Services Resource Framework (WSRF) is published by OASIS for use by Web services. WSRF defines different methods for maintaining session data during a distributed transaction. When a client communicates with the Web service, the message contains a resource identifier within the request. This information may be encapsulated within the WS-Addressing header as a URI, as XML data, or with a description of a particular target resource. The WSRF operations standardize `READ` and `WRITE` methods (actually `GET`/`SET`) that can work with the resource's state without the client having to be aware of the details of the individual Web service.

The overall OASIS Web service standard that is used to manage and monitor services is called Web Services Distributed Management (WSDM). WSDM plays the same role in Web service management that SNMP does in network management. Vendors use WSDM to create applications that display current status, provide Web management services, and can diagnose and repair systems remotely.

While RPC provides an architecture based on WSDL message passing, a different model called Representational State Transfer (REST) is applied to distributed architectures where standard methods for HTTP are used. A RESTful Web service can still use WSDL to convey a SOAP message over an HTTP request/reply, but it can be implemented by other methods without using SOAP.

# Service Oriented Architectures

A Service Oriented Architecture (SOA) is a framework for building distributed networked applications from a set of interoperable services. SOA abstracts the service requestor from the different locations of the service providers. Indeed, a well-implemented SOA abstracts the service from the service provider. A service requestor seeking a particular service is required only to know the input to the service and to be able to use the SOA messaging format to communicate with the service. If the service provider is upgraded, or moved, or even replaced, but the architecture is maintained, then the service will continue to supply the result that is needed. This makes components in an SOA highly modular, and portable to different NOS and languages, and the whole system very flexible. Many services that are provided over the Internet are built using an SOA.

### Note

Many people confuse SOA with SOAP, although they refer to entirely different technologies. SOA is an architecture, while SOAP is a messaging protocol.

In an SOA, the client or service requestor is typically a lightweight "application," and can often be running inside a browser interface. The word "application" is in quotes because the client is essentially orchestrating services running on one or more networked systems, and so the application is a name given to the particular set of services that the service requester is using at the moment. [Figure 23.3](ch23.html#a_conceptual_diagram_of_a_service_orient) shows a conceptual diagram of an SOA. The Orchestration layer is used to describe a layer containing large capable software modules that can act in concert with other orchestration modules to perform a variety of tasks.

![A conceptual diagram of a Service Oriented Architecture](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2303.png)

**Figure 23.3. A conceptual diagram of a Service Oriented Architecture**

The modularity of SOA components and the independent nature of each service provider lends SOA to development in object-oriented languages such as C#, C++, C, Java, and others. Unlike many of the objects that are supported in these programming languages, SOA provider modules are very large objects combined to create executable programs. Many different technologies are used to create SOAs, including SOAP, RPC, DCOM, CORBA, REST, Jini, and Microsoft Windows Communication Foundation (WCF).

There is an industry effort under way to devise what is called a Service Component Architecture (SCA), which will provide a set of standards that different languages can all use to communicate with service providers, abstracting the language from the invoked service calls to the service providers. In the SCA, data may be represented as a set of Service Data Objects (SDOs). The transition of SCA from an industry working group to a standard is being overseen by the OASIS Open Composite Services Architecture (CSA) project (`www.oasis-opencsa.org/`).

Some of the important SOA frameworks, including the Microsoft .NET Framework and Java EE (Enterprise Edition), not only specify how to communicate between service requestor and service provider but also provide isolation of the service module from the operating system and other applications running on the server that they are on. Different service providers are independent of one another in an SOA. These features have allowed many legacy applications to act as service providers, which preserves the tremendous resources that have often gone into developing them.

As you can imagine, a fully implemented SOA can grow to be quite large with many components. To the user viewing a management GUI (in their browser perhaps), they might see a set of controls, data display, and other features, but each individual item or group of items could be running on individual service providers and take the form of a .NET Control or an Enterprise Java Bean (EJB). In order to understand complex environments and to be able to determine the impact of different changes as well as troubleshoot the system, a system map must be constructed that shows the different relationships. The situation is similar to modeling a database using a Computer Aided Software Engineering (CASE) tool such as ERWin, which uses entity relationship diagrams to normalize a database. The tools used to model SOAs are based on what is called the Software Oriented Modeling Framework (SOMF).

### Note

Wikipedia has an introduction to service-oriented modeling that you can read at `http://en.wikipedia.org/wiki/Service-oriented_modeling`. For a more detailed treatise on SOMF, you can read Service-Oriented Modeling (SOA): Service Analysis, Design, and Architecture, by Michael Bell (Wiley Publishing, Inc., 2008).

SOA is a highly attractive technology to many companies because it allows them to port their applications into services and charge for these services on an ongoing basis. In the past, if a user owned an office suite and an upgrade was created for some particular component or set of components, the vendor needed to either patch the software or provide a new version of the software for each of the users. In this new architecture, if the software is changed or upgraded, it can be upgraded at the servers without requiring all of that additional overhead and infrastructure to provide the benefits to user and vendor.

# Summary

In this chapter, you learned how Web browsers communicate with a Web server to obtain resources over a network. The Hypertext Transfer Protocol (HTTP) is the Application layer protocol that browsers use to transfer information. HTTP uses a request/response mechanism to send commands, requests, and responses between the browser and server.

A Web service is a mediated client-server application. Web services can be implemented with SOAP or another messaging protocol to transfer information between a service requester and service provider. Web services are mediated by a service broker, which makes services discoverable.

You also learned about Service Oriented Architectures (SOAs) in this chapter. An SOA is a framework used to build distributed applications. SOAs have been used to create a number of well-known Web-based applications, and they serve as the future method by which applications can be delivered as services on demand.

In the next chapter, you learn about the mail protocols used on the Internet.
