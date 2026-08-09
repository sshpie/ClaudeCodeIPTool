# Chapter 11. Web Security

**IN THIS CHAPTER**

- **Understanding HTTP**
- **Identifying common Web security weaknesses and attacks**
- **Developing secure Web sites**
- **Understanding tracking mechanisms**

Around the year 2000, the language of the Internet transitioned from File Transfer Protocol (FTP) to Hypertext Transfer Protocol (HTTP). This marked the broad acceptance of the World Wide Web. Engineers, businessmen, clerks, teachers, students, parents, grandparents, children, and everyone in between access Web sites, and security is a significant element of every one of these transactions. Even activities as simple as checking the local weather or shopping online for a gift can be the target of a malicious attack.

This chapter discusses network security as it is applied to the World Wide Web, in particular, communication that takes place over HTTP. Details of not only how the protocol works but why and the associated security issues are described. In conclusion, it describes a method for implementing a secure e-commerce site.

# What Is HTTP?

HTTP is a generic communication protocol used to transfer requests, responses, and data between Web clients and servers. Data transfer can be in the form of plain text, formatted text, or encoded binary.

Although not as common, this extensible protocol is occasionally used by clients accessing proxies and gateways that communicate to servers in other protocols. These gateways provide the ability for HTTP to communicate with the following:

- Simple Mail Transfer Protocol (SMTP)
- Network News Transfer Protocol (NNTP)
- File Transfer Protocol (FTP)
- Post Office Protocol (POP)
- Wide Area Information Servers (WAIS)
- Gopher servers

HTTP rests on top of the layer 4 Transmission Control Protocol (TCP) transport protocol. Each HTTP session initiates with the TCP three-way handshake and is terminated with an acknowledged FIN packet. Most HTTP traffic takes place across TCP port 80.

HTTP has a range of commands, or methods, it can use. Although by design it is capable of much more, security concerns and lack of necessity have reduced HTTP to a small handful of common methods. These methods, their purpose, and syntax are described in the following list:

- **GET** — A request from the client to retrieve an object from the server. It has the following syntax:GET Request-URI VersionAn example follows:GET / HTTP/1.1`Request-URI` is the object of interest on the Web server. When viewing a Web site's root directory (for example, `www.yahoo.com` versus `www.yahoo.com/travel`), the URI is simply `/`. Although not a requirement, Web clients generally include the maximum version of HTTP that they support. This ensures that both the client and server communicate using the same feature set. The option not to include the version is referred to as a *simple request* and is provided for backward compatibility with HTTP/0.9. The response to this request from a Web server is in the form of a status number (200, if successful), and the content of the requested object.
- **HEAD** — A request from the client to retrieve meta-information about an object from the server. It has the following syntax:HEAD Request-URI VersionAn example follows:xsHEAD / HTTP/1.1The only difference between a `GET` and a `HEAD` response is that the `HEAD` does not actually return the body of the `Request-URI`. It is used to find out meta-information about the server and verify the status and existence of an object prior to receiving it. For example, it can be particularly useful to determine if a site has changed from its last viewing without retrieving it. All other header fields within the response exist and are identical.
- **POST** — A request from the client to send an object to a handler on the server. It has the following syntax:POST Request-URI VersionAn example follows:POST /cgi-bin/message.cgi HTTP/1.1`Request-URI` is the Web page intended to receive the posted data. `POST` is commonly used in forms to submit a message to a bulletin board, newsgroup, Web-based e-mail, or to send data for handling by a database or active content script.
- **PUT** — A request from a client to send an object and place it directly on the server. It has the following syntax:PUT Request-URI VersionAn example follows:PUT /home/mypage.html HTTP/1.1`Request-URI` is the location that the client would like the data placed at on the server. `PUT` is occasionally used to provide authorized users with a means of uploading content directly to a Web site. Additional security precautions must be taken with servers that are configured to accept this method.
- **DELETE** — A request from a client to delete an object from the server. It has the following syntax:DELETE Request-URI VersionAn example follows:DELETE /home/invitation.html HTTP/1.1`Request-URI` is the location of the object that the client would like to delete from the server. Similar to `PUT`, `DELETE` is generally not supported by most Web servers. It is dangerous to provide outside users with the ability to modify content on a Web site.

# How Does HTTP Work?

HTTP operates through a simple request and response model. The client, or Web browser, initiates a session by issuing a request method and a request object (that is, `Request-URI`). The Web server processes and handles this request and the appropriate response is returned to the client.

[Figure 11-1](ch11.html#the_basic_request_and_response_model_use) shows the basic request and response model used in an HTTP session. [Figure 11-2](ch11.html#examples_of_various_successful_and_unsuc) provides examples of successful and unsuccessful HTTP requests from an Apache Web server log file.

![The basic request and response model used in an HTTP session](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1101.png)

**Figure 11.1. The basic request and response model used in an HTTP session**

![Examples of various successful and unsuccessful HTTP requests from an Apache (www.apache.org) Web server log file](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1102.png)

**Figure 11.2. Examples of various successful and unsuccessful HTTP requests from an Apache (`www.apache.org`) Web server log file**

Beyond the HTTP method and Request-URI, the HTTP header contains additional fields both on the request and response packets. A standard HTTP request header looks like this:

```
GET / HTTP/1.1
Host: www.wiley.com
User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv: 1.4)
Gecko/20030626 Netscape/7.1
```

```
Accept: text/xml, application/xml, application/xhtml+xml,
text/html; q=0.9, test/plain; q=0.8, video/x-mng, image/png,
image/jpg, image/gif; q=0.2, */*; q=0.1
Accept-Language: en-us, en; q=0.5
Accept-Encoding: gzip, deflate
Accept-Charset: ISO-8859-1, utf-8; q=0.7, *; q=0.7
Keep-Alive=300
Connection: keep-alive
```

The first line describes the method and `Request-URI`, which in this case is a request to retrieve a Web site's root directory (that is, `/`). `Host` identifies that the Web site requested is `www.wiley.com`.

Web content is not What-You-See-Is-What-You-Get (WYSIWYG, pronounced *WIZ-zee-wig*). Formatting and other content interpretation vary across Web browsers. Therefore, many Web sites tailor the appearance of a Web page to the specific browser. The `User-Agent` field identifies the type of the Web client used, and scripts can be implemented on the server to substitute the Web pages accordingly.

`Accept` describes each of the data formats that is supported by the browser. This is followed by language preferences. To reduce bandwidth and transfer binaries, many Web sites encode and compress data prior to sending it. Browsers that support this indicate it in the `Accept-Encoding` field.

`ISO-8859-1` is the character set that is the preference for this client. `US-ASCII` is also a common default for the `Accept-Charset` field.

`Keep-Alive` is a TCP timeout option that is associated with persistent connections, which are discussed in detail later in this chapter.

When this request is received, the Web server processes it and sends a response. The response in this case is as follows:

```
HTTP/1.1 301
Location: /WileyCDA/
```

The code 301 informs the Web client that the main page now permanently resides at `/WileyCDA/` instead of `/`. The browser then automatically reissues a request, but this time `Request-URI` is different.

```
GET /WileyCDA/ HTTP/1.1
Host: www.wiley.com
User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030626
     Netscape/7.1
Accept: text/xml, application/xml, application/xhtml+xml, text/html; q=0.9,
```

```
test/plain; q=0.8, video/x-mng, image/png, image/jpg, image/gif;
     q=0.2, */*; q=0.1
Accept-Language: en-us, en; q=0.5
Accept-Encoding: gzip, deflate
Accept-Charset: ISO-8859-1, utf-8; q=0.7, *; q=0.7
Keep-Alive=300
Connection: keep-alive
```

Following the correct request, the Web server issues the following response:

```
HTTP/1.1 200 OK
Date: Wed, 20 May 2009 16:06:44 GMT
Server: Apache/1.3.20 (Unix)
Set-Cookie: JSESSIONID=0000NB14CONYTVM4LW3KGM5VX4I:vpk0qcu;Path=/
Cache-Control: no-cache="set-cookie, set-cookie2"
Expires: Thu, 01 Dec 1994 16:00:00 GMT
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=ISO-8859-1
Content-Language: en
[ the body of the website ]
```

The response code 200 indicates that the request was processed correctly, and that the requested URI is in the body of the response. Just as the request identifies the type of client used, this response indicates that Apache version 1.3.20 is used for the Web server.

In addition, this response sets the nonpersistent cookie `JSESSIONID` for the entire site. Nonpersistent means that the expiration date is not set for a date in the future, and therefore the cookie will be removed from memory when the browser is terminated. Persistent cookies are written out to the hard drive and are referenced in subsequent browser sessions. Following the setting of this cookie, all subsequent requests to this site during this session contain the following additional field below `Connection`:

```
Cookie: JSESSIONID=0000NB14CONYTVM4LW3KGM5VX4I:vpk0qcu
```

This allows the Web server to track activity from this browser. Cookies and other tracking mechanisms are explored in further detail later in this chapter.

## HTTP implementation

There are two primary releases of HTTP: 1.0 and 1.1. Versions are defined with a "<major>.<minor>" notation and are meant to provide formatting and capability information by the sender for the receiver. Minor numbers are incremented when changes are made that do not affect the overall parsing algorithm, and major numbers are incremented otherwise.

HTTP/1.0 and previous releases are inefficient. Unless unofficially supported by the browser through a keep-alive mechanism, unnecessary overhead TCP chatter occurs with these versions.

As a demonstration, think of an HTTP session as a telephone call. The initial three-way TCP handshake is analogous to the receiver answering, "Hello," the caller asking, "Is Penny there?" and the receiver responding, "Yes, this is Penny."

The HTTP portion of the phone call comes after this handshake when the caller asks Penny a question and Penny answers. When the caller has multiple questions to ask, it is most efficient for the questions and responses to occur in a single telephone call.

HTTP/1.0 and older versions instead re-implement the 3-way handshake for each question. This would instead create a conversation that sounds something like the following:

|  |  |
| --- | --- |
| **Receiver:** | Hello? |
| **Caller:** | Is Penny there? |
| **Receiver:** | Yes, this is Penny. |
| **Caller:** | Great, how are you? |
| **Receiver:** | I am doing well, thank you. |
| **Caller:** | Bye. |
| **Receiver:** | Bye. <HANG UP> |

|  |  |
| --- | --- |
| **Receiver:** | Hello? |
| **Caller:** | Is Penny there? |
| **Receiver:** | Yes, this is Penny. |
| **Caller:** | Will you be attending Stan's party tomorrow? |
| **Receiver:** | Yes, I would not miss seeing him! |
| **Caller:** | Bye. |
| **Receiver:** | Bye. <HANG UP> |

|  |  |
| --- | --- |
| **Receiver:** | Hello? |
| **Caller:** | Is Penny there? |
| **Receiver:** | Yes, this is Penny. |
| **Caller:** | Would you like to ride together to the party? |
| **Receiver:** | Yes, you pick me up at 6:00 p.m. |
| **Caller:** | Bye. |
| **Receiver:** | Bye. <HANG UP> |

When Web pages were first created, bandwidth was restrictive and most pages contained only one or two objects at the most. Although inefficient, this duplication of TCP sessions was not prohibitive at the time. However, now it is not uncommon for a single site to have dozens of objects. Creating an entirely new TCP connection for each object (no matter how large or small) exponentially increases the network traffic, which is unacceptable.

[Figure 11-3](ch11.html#http_solidus_1.0_inefficiently_establish) illustrates how separate TCP sessions must be created for the transfer of both the Web page and the image located on it using HTTP/1.0.

![HTTP/1.0 inefficiently establishes a new TCP connection for each object received during a Web session. The main Web page is first retrieved, followed by separate connections for each image, and so on. HTTP communication (highlighted below) is minimal compared to the overhead associated with creating and terminating a new TCP connection for each object.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1103.png)

**Figure 11.3. HTTP/1.0 inefficiently establishes a new TCP connection for each object received during a Web session. The main Web page is first retrieved, followed by separate connections for each image, and so on. HTTP communication (highlighted below) is minimal compared to the overhead associated with creating and terminating a new TCP connection for each object.**

To compound the inefficiencies of HTTP/1.0 and previous versions, TCP was developed to be most efficient over long sessions.

For smaller sized objects, the slow-start algorithm used in TCP actually forces the transfer to operate at its smallest (and hence slowest) capacity. Transactions of this nature will often be completed before the window size can be ramped up to accommodate the true capacity of the network.

**What Does 'Slow Start' Mean?**

Slow start refers to an algorithm that has been built into modern implementations of TCP. It came about after older releases allowed the transmitter to send multiple packets blindly across a network that were up to the publicized window size of the receiver. This is highly efficient when both hosts reside on the same subnet, but when they are separated by a router this can be dangerous. Denial-of-service attacks can take advantage of this queuing and cause a router to run out of memory by sending large packets faster than the router can transmit them ([Figure 11-4](ch11.html#packets_that_are_too_large_for_routers_o)).

![Packets that are too large for routers or gateways are divided and the remaining packets are queued to be sent.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1104.png)

**Figure 11.4. Packets that are too large for routers or gateways are divided and the remaining packets are queued to be sent.**

If the intermediate router or network is sized to handle a smaller window it must queue up the packet, divide it into multiple packets of an allowable size, and retransmit. This queuing can slow throughput and, even worse, cause the router to run out of memory (a security concern).

To prevent this event from unintentionally taking place, the sender also establishes a size restriction. This restriction is referred to as the congestion window (cwnd) size in the TCP header. This value gets initialized upon the start of a connection as the size of one segment, typically 512 bytes. Every received ACK packet indicates that the size is allowable across the entire path between the two servers, and the value increases exponentially (that is, transmit 1: 1 segment, transmit 2: 2 segments, transmit 3: 4 segments, and so on). Eventually the transmission will be beyond the allowable size of the network, and the sender will not receive an ACK. This enables the sender to identify the maximum window size in an efficient manner. Slow start provides a graceful sanity check that the maximum allowed size by the receiver is an accepted value across the entire network.

You can read more about the slow start algorithm in RFC 2001, at `www.faqs.org/rfcs/rfc2001.html`.

## Persistent connections

In 1999 the IETF released the standard for HTTP/1.1 as an improvement to deal with these performance issues. This enhancement uses *persistent connections* so that multiple objects can be transferred over each TCP session. In addition to reducing the amount of overhead associated with creating or closing connections, persistent connections provide the ability to maximize window size by already knowing the negotiated maximum. Otherwise, each operation would itself be forced to start slow and negotiate up as was done previously.

The previous implementation of HTTP initially tried to accommodate this concept by issuing the keep-alive extension. However, this extension did not deal with the circumstance in which there was more than one proxy between the sender and receiver. In addition, keep-alive was only unofficially supported, which meant that not all browsers accommodated it.

Unless the request header field explicitly indicates the following, HTTP/1.1 will allow multiple requests to be sent across a single TCP session:

```
Connection:   close
```

As illustrated in [Figure 11-5](ch11.html#the_efficient_http_solidus_1.1_protocol), the HTTP/1.1 protocol establishes a new TCP connection only at the start of the session. All data for the Web site is passed using this existing connection, which also alleviates inefficient use of the slow start functionality.

Each TCP segment can actually contain multiple requests and responses, which *pipelines* the queue of operations. The second major improvement in HTTP/1.1 is that it enables compression of the data being transmitted.

### Note

This compression is generally implemented on UNIX-based Web servers using the GNU zip (gzip) algorithm, as defined in RFC 1952. This compression is based on the Lempel-Ziv coding (LZ77) with a 32-bit CRC. Alternatively, a Web site may use `compress`, which is an adaptive Lempel-Ziv-Welch (LZW) coding, or `deflate`, which uses the zlib format defined in RFC 1950.

![The efficient HTTP/1.1 protocol only establishes a new TCP connection at the start of the session.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1105.png)

**Figure 11.5. The efficient HTTP/1.1 protocol only establishes a new TCP connection at the start of the session.**

**Where Did Hypertext Originate?**

Although popularity of the World Wide Web only started in the early nineties, the concept of hypertext dates back to 1945. It was President Franklin D. Roosevelt's science advisor, Dr. Vannevar Bush, who first proposed the concept in his article "As We May Think" about the design of a future device that he named the memex. As the following caption from this article describes, this device was intended to provide the capability to efficiently store and search for information in a manner similar to that of the human mind:

> *It affords an immediate step, however, to associative indexing, the basic idea of which is a provision whereby any item may be caused at will to select immediately and automatically another. This is the essential feature of the memex. The process of typing two items together is the important thing ...[the human mind] operates by association. With one item in its grasp it snaps instantly to the next that is suggested by association of thoughts, in accordance with some intricate web of trails carried by the cells of the brain*.

Twenty years later, Ted Nelson coined the phrase hypertext in his paper "Complex information processing: a file structure for the complex, the changing, and the indeterminate," which was presented at the 1965 ACM 20th National Conference:

> *Let me introduce the word "hypertext" to mean a body of written or pictorial material interconnected in such a complex way that it could not conveniently be presented or represented on paper. It may contain summaries, or maps of its contents and their interrelations; it may contain annotations, additions and footnotes from scholars who have examined it. Let me suggest that such an object and system, properly designed and administered, could have great potential for education, increasing the student's range of choices, his sense of freedom, his motivation, and his intellectual grasp...Such a system could grow indefinitely, gradually including more and more of the world's written knowledge*.

Two years later, in 1967, a team of researchers led by Dr. Andries van Dam at Brown University developed the first hypertext system, Hypertext Editing System. This research was funded by IBM and later sold to the Houston Manned Spacecraft Center where it was used for the Apollo space program documentation. Around that same time, Doug Engelbart from Stanford University (who invented the mouse) introduced his oN Line System (NLS). This system debuted in 1968 as a "shared journal" that housed over 100,000 papers, reports, memos, and cross references.

Complications occur when a proxy or gateway forwards traffic that is a different version than its own capability. In this case, selection of the version is almost always chosen to reflect the capability of the most recent sender. For example, if the Web server was HTTP/1.1 but the proxy only supports HTTP/1.0, the message is downgraded to HTTP/1.0 because it reflects the highest possible value of its transmitter (which, in this case, is the proxy). Alternatively, the proxy can instead choose to send an error message or tunnel the traffic.

When the transmission is forwarded with a version higher than the originating server, there are several potential outcomes. In the case of caching proxies, gateways have the option of upgrading, and tunnels do not change the version number at all.

## The client/server model

The fundamental design for most network-based applications, particularly those on the Internet, is the client/server model. The names client and server are also commonly used to categorize computers on a network based on their functionality.

In this case, there are two categories—those that want something (the clients) and those that have something (the servers). Although popular, this terminology is *technically* incorrect because the servers are also clients of other applications. For our purposes, client refers to the application (Web browser) on the host that is interacting with the remote computer's server application (Web server).

The most prevalent example of a client when it comes to the Internet is a Web browser. A browser is responsible for managing communication between the user and a Web server (see [Figure 11-6](ch11.html#client_solidus_server_interaction_depict)).

![Client/Server interaction depicted in Web browsers and servers](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1106.png)

**Figure 11.6. Client/Server interaction depicted in Web browsers and servers**

Initiation occurs when the user enters a URL (for example, `www.google.com`) into the client browser. The client indicates what it wants from the server by sending a `GET` request. The server that maintains all of the information responds back to the client with a `PUT` method containing the requested data.

This client/server relationship can be seen in other common Internet activities such as e-mail. Just as the post office stores and processes physical mail, e-mail is first stored in an electronic mailbox managed by a mail server. E-mail clients, such as Eudora or Outlook Express, send requests to the mail server using a specified protocol (generally SMTP). The mail server processes this request and forwards e-mail to a client where it can be viewed and processed by the user.

## Put

In HTTP the well-known `POST` method is used to upload message board postings, credit card and address information for online purchases, and Web-based e-mail. Although not commonly implemented because of security issues, HTTP also provides the PUT method for uploading information.

The difference between the two is in the meaning of `Request-URI`. For `POST`, the URI refers to the program on the server that is responsible for receiving and processing the information that you upload (for example, `registration_form.cgi`). For a `PUT` request, the URI actually refers to the location on the server where you would like the information placed.

### Note

This is of significant concern from a security standpoint because users are able to actively modify the *actual* content of the Web server without intervention.

If absolutely required, servers should only support the `PUT` capability for users to administer their own files and directories. Authoring clients such as Dreamweaver (`www.macromedia.com`) and Amaya (`www.w3.org/amaya`) support this feature. Instead of saving the modified page and manually transferring it to the Web site, these clients enable you to save directly to the remote Web site.

Because of obvious security concerns, most servers do not support this functionality remotely by default. However, be warned that some do. For example, by default, some servers are configured to allow the admin user to put files on the server. This capability must be disabled or the password changed prior to allowing remote access to this server. Attackers prey on configuration errors such as this by scouring the Internet for potentially misconfigured domains that use this type of server.

In general, the concept of allowing a user to upload information without some sort of processing engine (as is the case with `POST`) is a security risk. Even when locations and size restrictions are placed on the `PUT` requests, a malicious user can still potentially use this mechanism to exploit the server. For example, the user could upload a Web page that is purposefully vulnerable. When exploited it could provide unrestricted access to the attacker.

## Get

The `GET` method is associated with retrieving content from a Web server rather than modifying it. As discussed previously, it is used to retrieve pages and other objects such as images from Web servers when a Web client requests them. Because of this, the `GET` method is itself not a security risk like `PUT`.

Security concerns associated with `GET` actions are instead focused on ensuring the integrity and functionality of the server application itself and any active content. `GET` is still an interface between a potentially malicious user and the server. Any inputable pages involved in this method should be closely analyzed and tested for faults.

## HTML

HTML is a formatting language used extensively in the World Wide Web. It is an application of the International Standard Organization (ISO 8879) for hypertext, the Standard Generalized Markup Language (SGML).

Instead of physically changing the appearance of the text, it is surrounded with markup symbols, referred to as *tags*, which indicate how it should be displayed. For example, the following formatting would bold a section of text:

```
<B>HTML is also used in many chat programs!</B>
```

The first tag, <B>, indicates that the browser should begin bolding text, and the second tag, </B>, indicates that it should end bolding. In addition to formatting such as background and foreground configuration, HTML provides symbols to indicate how a browser should display and interpret links and images.

A typical HTML page is composed of a head and body section. The head section contains information about the page such as its title and meta-information used by search engines, and the body contains the actual viewable content on the page. An example format of a typical HTML page follows:

```
<HTML>
<HEAD>
  <TITLE> An example of HTML </TITLE>
</HEAD>
<BODY>
<CENTER><FONT SIZE=25>HTML demonstration</FONT></CENTER>
<BR>
<BR>
HTML is merely a means of formatting.
<BR>
<BR>
Netscape's HTML Central is a good
<A HREF="http://devedge.netscape.com/central/html">guide</A>.
</BODY>
</HTML>
```

Because HTML does not possess any active content, it is a minimal security risk. Note, however, that additional content such as JavaScript and ActiveX objects can be embedded within Web pages, which could potentially be dangerous.

# Server Content

Active content on a Web site is composed of server-side executables and client-side executables. The host executing the content should be the most concerned with its security. This section focuses on the server side, which includes Common Gateway Interface (CGI) and PHP.

## CGI scripts

The Common Gateway Interface was the first interface designed to provide developers with the capability to produce dynamic content on their Web sites. With this introduction, suddenly pages began to transform from informative but stale HTML to active feedback environments. The first search engines, registration sites, Web-based chat forums, and online database queries were implemented using CGI.

The execution component of a CGI script can be written in any programming language that can execute on the host machine (Perl, Python, Shell, C, C++, and so on). Because of its ability to parse text easily, Perl tends to be the most popular of the choices. To be most effective, this language should be able to read from the standard input stream, output to the standard output stream, and read environment variables. Examples of commonly used environment variables used in active content are listed in [Table 11-1](ch11.html#commonly_used_environment_variables).

**Table 11.1. Commonly Used Environment Variables**

| Environment Variable | Purpose |
| --- | --- |
| REQUEST_METHOD | How the script was called, usually `POST`, `GET`, or `HEAD` |
| HTTP_REFERER | URL of the form |
| REMOTE_ADDR | IP address of the remote client |
| REMOTE_HOST | Name of the remote client |
| REMOTE_USER | Authenticated username (if supported) |
| CONTENT_TYPE | Content type of client-submitted data |
| CONTENT_LENGTH | Length of the client-submitted content |
| HTTP_USER_AGENT | Type of browser used by the client |

CGI scripts are located in a specified directory within a Web server (usually `/cgi-bin`). Although they are physically separated from sensitive system files, configuration errors can lead to access by malicious users.

## PHP pages

CGI is an interface, and PHP is a language. Just as CGI provides the ability to embed Perl and other languages directly into HTML, PHP is directly embedded.

The following example of a PHP page shows how they are commonly implemented. It randomly selects a URL for a book each time someone visits the page.

```
<?
$url = array(
  "http://www.wiley.com/WileyCDA/WileyTitle/
          productCd-0764519956.html",
  " http://www.wiley.com/WileyCDA/WileyTitle/
          productCd-0471493031.html",
  " http://www.wiley.com/WileyCDA/WileyTitle/
          productCd-0471486663.html",
  " http://www.wiley.com/WileyCDA/WileyTitle/
          productCd-047139470X.html ");

$subject = array(
        "HTML",
        "E-Commerce",
        "Java",
        "Testing");
```

```
$title = array(
  "- HTML 4 For Dummies, 4th Edition",
  "- E-Commerce: Fundamentals and Applications",
  "- Java Tools: Using XML, EJB, CORBA, Servlets and
     SOAP",
  "- Testing Applications on the Web: Test Planning
     for Internet-Based Systems");

srand(time());
$sizeof = count($url);
$random = (rand()%$sizeof);
print("<center><a href=\"
$url[$random]\">$subject[$random]</a>
$title[$random]</center>");
?>
```

As with CGI scripts, PHP is able to read and interpret environment variables. For example, the following line will display the type of Web client that the individual viewing the page is using:

```
<?php echo $HTTP_USER_AGENT; ?>
```

# Client Content

Client-side active content executes directly on the computer of the user that is browsing the Web site. Scripting languages such as JavaScript are either embedded directly into the HTML where they are interpreted by the browser, or executable content is downloaded and run separately. Popular examples of client-side active content include JavaScript, Java, and ActiveX.

## JavaScript

The HTML markup tag `<SCRIPT>` is used to identify a section of JavaScript within a Web page. Following is an example that causes the browser to execute an alert box with a message for the user.

```
<HTML>
<HEAD>
  <TITLE> An example of JavaScript </TITLE>
</HEAD>
<BODY>
<CENTER>This is a simple example of JavaScript</CENTER>
<SCRIPT>
  alert("This is an example of an alert!")
</SCRIPT>
</BODY>
</HTML>
```

The primary security issue related to JavaScript is that when viewed on a Web site it has the ability to open new browser windows without your permission. Just by adding the following lines to an HTML file, the Web site `www.google.com` will open in a separate window without any interaction by the user.

```
<SCRIPT>
window.open("http://www.google.com", '" + 0 + "', 'toolbar=0,
scrollbars=1,location=0,statusbar=0,menubar=0,resizable=0,
width=1152,height=864');
</SCRIPT>
```

This is one of the ways that Web sites create pop-up advertisements. While those ads can be annoying, they are generally not security threats. The danger comes when the opened Web site is operated by a malicious user. These types of attacks have been known to be capable of stealing passwords, PINs, credit card numbers, cause the computer to crash, and monitor all activity performed by the browser.

Although all current (known) vulnerabilities have been patched, JavaScript has the potential to access anything that the browser can if a new vulnerability is discovered. As with any client-side executable, JavaScript should be disabled if high security is a concern and sensitive information is present on the host computer.

## Java

Java is a language created by Sun Microsystems in 1991 to provide a method to execute programs without any platform dependence. Although originally intended for small consumer electronic devices such as VCRs, toasters, and television sets, its popularity soared in 1994 when it was used across the Internet.

### The sandbox and security

The Java security model is based on the notion of a sandbox. This environment resides on the host computer that is executing the Java application, and is designed to confine the program to a small play area. This play area is the sandbox, and it contains no critical resources. All access is explicitly granted by the user.

By default, the application only has access to the central processing unit (CPU), the display, the keyboard, the mouse, and its own memory. This provides the program with what it needs to run, but does not afford it what it needs to be dangerous.

Trusted applications can be provided larger boundaries and access to additional information. For example, applications that share files or documents may require additional access to the hard drive.

The Java sandbox is composed of the following:

- **Permissions** — Explicit statements of actions that applications are allowed to execute and resources that they are allowed to access.
- **Protection domains** — Collections of permissions that describe what actions applications from domains are allowed to execute and resources that they can access.
- **Policy files** — Contains protection domains.
- **Code stores** — The sites that the applications are physically stored on prior to execution on the host.
- **Certificates** — Used to sign code to convey trust to a user that you are the developer of the application.
- **Key stores** — Files that contain the certificates for Web sites. Key stores are queried to identify who signed the application code.

[Figure 11-7](ch11.html#the_java_security_model_involves_the_pol) depicts the Java security model.

![The Java security model involves the policy file, protection domain, code sources, key stores, and certificates.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1107.png)

**Figure 11.7. The Java security model involves the policy file, protection domain, code sources, key stores, and certificates.**

### Types of Java Permissions

[Table 11-2](ch11.html#java_permissions_summary) shows the different permissions that are allowed in Java and what the resulting actions are.

**Table 11.2. Java Permissions Summary**

| Type | Name | Actions |
| --- | --- | --- |
| java.io. FilePermission | File to perform action on | Read, write, delete, execute |
| java.net. SocketPermission | hostname:port | Accept, listen, connect, resolve |
| java.util. PropertyPermission | Java virtual machine that you want to perform action on | Read, write |
| java.lang. RuntimePermission | Specific to the class, examples within the core Java API include the following: *createClassLoader, readFileDescriptor, exitVM*, and *setIO* | Actions are not used; you either have permission to execute the specific runtime operation or you do not |
| Java.awt. AWTPermissions | accessClipboard, accessEventQueue, createRobot, listenToAllAWTEvents, readDisplayPixels, and showWindowWithoutWarningBanner | Not used |
| Java.net. NetPermission | specifyStreamHandler, setDefaultAuthenticator, requestPasswordAuthentication | Not used |
| Java.security. SecurityPermission | There are several; popular examples include the following: *addIdentityCertificate, getPolicy, setPolicy, setSystemScope* | Not used |
| Java.io. SerializablePermission | enableSubstitution, enableSubclassImplementation | Not used |
| Java.lang.reflect. ReflectPermission | suppressAccessChecks | Not used |
| Java.security. AllPermission | None | Not used |

## ActiveX

ActiveX is one of the most powerful technologies available today. Using it, software can be automatically downloaded, installed, and executed. ActiveX can be thought of as a self-installing plug-in. If configured by the browser, Web pages that contain an `OBJECT` tag are automatically acted upon simply by viewing.

The original Microsoft code name for ActiveX was *sweeper*. It was formally announced at a San Francisco conference in 1996. Although most consider it a browser-related technology, it is also a part of Microsoft Outlook, Outlook Express, and Office applications.

The ActiveX `OBJECT` tag requires the following attributes:

- **CODEBASE** — The URL of the program that is to be downloaded and executed on the host computer
- **CLASSID** — A unique value assigned to each ActiveX component that is used to specify what controls you are using
- **ID** — A value that can be arbitrarily set to any value that is used to identify the control for use within a Web site
- **TYPE** — An optional field that is almost always set to `application/x-oleobject` (the MIME type for ActiveX controls)
- **WIDTH** — The width of the ActiveX visual object on the page
- **HEIGHT** — The height of the ActiveX visual object on the page
- **ALIGN** — The alignment of the ActiveX visual object on the page

ActiveX pages also require the `PARAM` tag, which has a `NAME` and a `VALUE` attribute. `NAME` is used to specify a control that is to be set, and `VALUE` specifies what it should be set to.

Following is an example of an embedded Flash movie that downloads and runs Shockwave. Also demonstrated is that despite the common misconception, not all Web sites that implement ActiveX are malicious. This sample is actually used to execute a scrolling cartoon menu bar on `www.sesamestreet.com`.

```
<OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
codebase="http://download.macromedia.com/pub/shockwave/cabs/f
lash/swflash.cab#version=4,0,2,0"
ID=movie WIDTH=770 HEIGHT=310>
<PARAM NAME=movie
VALUE="/sesamestreet/scroller/swf/scroller_page.swf?server%5F
name=www%2Esesameworkshop%2Ecom&swf%5Fpath=%2Fsesamestreet%2F
scroller%2Fswf&name=games&filter=6&focus%5Fitem=&num%5Ffilter
s=6">
<PARAM NAME=quality VALUE=high>
<PARAM NAME=bgcolor VALUE=#3366CC>
<PARAM NAME=menu VALUE=false>
<EMBED
src="/sesamestreet/scroller/swf/scroller_page.swf?server%5Fna
me=www%2Esesameworkshop%2Ecom&swf%5Fpath=%2Fsesamestreet%2Fsc
roller%2Fswf&name=games&filter=6&focus%5Fitem=&num%5Ffilters=
```

```
6" quality=high bgcolor=#3366CC  WIDTH=770 HEIGHT=310
NAME=movie TYPE="application/x-shockwave-flash"
PLUGINSPAGE="http://www.macromedia.com/shockwave/download/ind
ex.cgi?P1_Prod_Version=ShockwaveFlash"></EMBED></OBJECT>
```

When it comes to security, ActiveX applications are digitally signed using the Authenticode system. The benefit of this is that it provides the user with a measure to verify the identity of the certificate's signer, but it does not prevent against malicious software in the application.

Without paying close attention, you may see only the name "Microsoft Corporation" and not realize that this message is actually indicating that the certificate has not been authenticated. Accidental consent of an unverified `OBJECT` can give a malicious user full access to your computer.

When valid authentication occurs, the Authenticode system allows you to determine who signed the object. Because the signature is actually applied to a cryptographic checksum of the object, you are also guaranteed that it has not been modified since the signing took place. However, if you chose to accept an object from a malicious Web site, this mechanism will not protect you against their attack.

Similarly, when you purchase a vehicle from a neighborhood car dealer and are provided a warranty, you are not protected against the car breaking down. However, you know exactly where to go and have it fixed if it does. Accepting an object from an unknown entity is similar to deciding to purchase a vehicle from someone that just happens to drive by your house. Even though this individual presents you with a paper copy of a warranty, you may be wary that their vehicle is not trustworthy. The warranty is useless without knowledge that it is supported by a trustworthy entity.

The example Web page is based on the Microsoft Internet Explorer "rotating e" developer's example. A sample section responsible for displaying and rotating the "X" in ActiveX is listed here:

```
<SCRIPT LANGUAGE="VBScript">
Sub Window_OnLoad()
    call SG7.Scale(0.50, 0.50, 0.50)
    call SG7.Rotate(90, 90, 90)
    RotateAll
end sub
Sub RotateAll
    Call SG7.Rotate(4,6,2)
    FILK = Window.SetTimeOut("Call RotateAll", 10,
"VBSCript")
End Sub
</SCRIPT>
<OBJECT id=SG7 STYLE="POSITION:ABSOLUTE; HEIGHT: 100%; LEFT:
600; TOP: 55; WIDTH: 100%; ZINDEX: 1" CLASSID =
"CLSID:369303C2-D7AC-11D0-89D5-00A0C90833E6">
```

```
<PARAM NAME="Line0001" VALUE="SetLineStyle(0)">
<PARAM NAME="Line0002" VALUE="SetFillColor(0, 0, 0)">
<PARAM NAME="Line0003" VALUE="SetFillStyle(1)">
<PARAM NAME="Line0004" VALUE="SetFont('Arial', 700, 700, 0,
0, 0)">
<PARAM NAME="Line0005" VALUE="Text('X', −95, 87)">
</OBJECT>
```

This particular example is noteworthy because it relies completely on VBScript and controls available within the browser itself. This means that no actual source code has to be downloaded from the Web server. Therefore, the user is not prompted to accept a certificate prior to execution.

# State

Web sites need to be able to keep track of users connecting to the site multiple times or accessing multiple pages. This is not built into HTTP and applications such as online banking and e-commerce need this functionality, which is called state. State is discussed in the following sections.

## What is state?

State is the current status of a specific instance of an application. Examples of state can be found every day in human interaction. Every action that you make or respond to is recorded and used to shape the way that you approach the future. For example, imagine that a telemarketer calls you and you dismiss the offer. If that telemarketer immediately calls back and asks the same question again, you get upset because your state indicates that you have already experienced this event and the telemarketer should remember that you are not interested.

Just as you maintain a memory for state in everyday life, an application must have dedicated memory to do the same. This can take place in the form of a file, entry in a database, or a buffer in memory. This memory can be expensive and, therefore, most applications do not maintain state.

## How does it relate to HTTP?

HTTP is a stateless, sessionless protocol that relies on the use of external authentication mechanisms, such as tokens, to identify clients and their current state. This means that each transaction is completely unique and that after the transaction occurs, neither the browser nor the server maintains a memory of where it left off. Each new Web page is processed without any memory of past history. You may ask yourself how this can be because your shopping cart on `www.amazon.com` is capable of maintaining its contents from one session to another, but this is accomplished through external mechanisms such as cookies and by the application developer, not within the protocol itself.

## What applications need state?

Any application that requires the association of multiple pages by a single user requires state. For example, it takes a specialized session tracking system to correlate your shopping cart with your billing information on a Web site. State tracking becomes increasingly complex when the Web site is a server farm composed of multiple coordinating Web servers instead of a single entity. Multiserver environments are especially challenging for applications such as Microsoft Internet Information Services (IIS), which are only capable of tracking session state across a single server. What happens if WebServer1 serves the shopping cart, but WebServer2 collects the billing information? Generally, a session manager database is implemented in SQL to maintain congruency across the servers.

## Tracking state

An important concept to remember when it comes to the Internet is that every transaction is logged somewhere. Because HTTP is stateless by design, this tracking must be done by external mechanisms. Web sites equate state with a session. Security issues associated with each session include creating a new session or security identifying a participant in a previous session, identification of a participant (or concurrent participants) in an ongoing session, and terminating a session.

## Cookies

A cookie is made of ASCII text (up to 80k per domain) that can be stored all in one file or stored in individual files, depending on the browser. They are used to maintain information on items such as the following:

- A shopping cart
- Advertising information
- User name/password to a site
- Preference information
- A tracking ID for your computer

Cookies can contain either the actual information to be passed (for example, your user name) or they can contain an index into a database on the server. Both are commonly used, and each has its benefits. By storing actual information in a cookie on the user's hard drive, the server does not need to retain it in a central location. Privacy advocates often prefer this method because of concerns about growing databases of personal information. However, the downside to this means the information must be openly passed each time the user accesses the Web site. By passing only an index to the server, any attacker intercepting the transmission will not gain any useful information.

### How do they work?

Web servers send cookies to your client browser either by embedding them directly into the response from an HTTP request, or through scripts executing on the Web site. After a request is made, the cookie portion of the response is set in the Set-Cookie header with the following fields:

- **expires=** — When the cookie should be removed from the hard drive
- **domain=** — The domain associated with the cookie (usually left blank and assumed to be the domain that sent it)
- **path=** — Indicates the pages that should trigger the sending of the cookie

Following is an example of a set of cookies that I received when I visited the Web site `www.1800flowers.com` for the first time:

```
HTTP/1.1 200 OK
Server: Microsoft-IIS/5.0
Date: Thu, 21, May 2009 12:35:39 GMT
P3P: policyref="http://www.1800flowers.com/w3c/p3p.xml",
CP="CAO DSP COR CURa ADMa DEVa PSAa PSDa IVAa IVDa CONo HISa
TELo OUR DELa SAMo UNRo OTRo IND UNI NAV"
Content-Length: 679
Content-Type: text/html
Expires: Thu, 19 Aug 2004 12:35:39 GMT
Set-Cookie: 800fBanner=+; expires=Sat, 21-Aug-2004 12:35:38
GMT; path=/
Set-Cookie:
ShopperManager%2Fenterprise=ShopperManager%2Fenterprise=U38Q1
8QHW7S69G0GPWBXMBRGB30M23J1; expires=Fri, 01-Jan-2010
05:00:00 GMT; path=/
Cache-control: private
```

To show you how cookies can be used as a convenience to the user, see the following example of a cookie passed when I visited `www.weather.com` to check my local forecast:

```
GET / HTTP/1.1
Host: www.weather.com
User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4)
Gecko/20030624 Netscape/7.1
Accept:
text/xml,application/xml,application/xhtml+xml,text/html;q=0.
9,text/plain;q=0.8,video/x-
mng,image/png,image/jpeg,image/gif;q=0.2,*/*;q=0.1
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive
Cookie: UserPreferences=3%7C%20%7C0%7Creal%7Cfast%7C-1%7C-
1%7C-1%7C-1%7C-1%7C+%7C%20%7C+%7C%20%7C%20%7C-
1%7CUndeclared%7C%20%7C%20%7C%20%7C; LocID=22305;
RMID=4453d3f04005fbb0
```

Because I had been to this site before, the cookie on my hard drive already contained an entry for this Web site. Therefore, when I went this time it automatically passed over my LocID, which happens to be the zip code that I checked the weather for previously. This provides a convenience to me so that I do not have to enter my zip code each time I want to check my local weather.

As you can see from the preceding example, cookies are passed within the HTTP protocol during Web site requests or responses.

### Cookie security

As the recipient of a cookie, the only security concern that you should have is the lack of privacy that you may experience. Cookies do not contain executable code and cannot be run by attackers. Also, they are not able to access any files on your hard drive. They are simply a means for Web servers to track your previous activity on their site. Because your hostname and IP address may change depending on your Internet service provider (ISP), they are a secondary means of identification.

One key to remember is that the cookies themselves are stored on the user's computer. Therefore, they can be removed, created, or edited at will by the user. This can be especially dangerous if the cookie contains an index into a database. For example, if user A has a cookie set with an ID of 500, that user can change that ID to be 501 instead. This means that when the user now accesses the Web site, his or her transaction is identified with the user associated with ID 501.

This is commonly referred to as *cookie poisoning*. It is a method of attacking Web servers by impersonating cookies for legitimate users. Attackers that do this can sometimes gain personal information about users and, even worse, execute new actions as if they were the impersonated user. An example of this type of attack was launched against the Verizon Wireless (`www.verizonwireless.com`) Web site when Marc Slemko, a Seattle-based software developer, posted this vulnerability to a security mailing: the "token" that the Web site used to track customers accessing their account information online was trusted and had no authentication checks.

```
http://www.app.airtouch.com/jstage/plsql/ec_navigator_wrapper
.nav_frame_display?p_session_id=223344556&p_host=ACTION
```

By merely changing this token and accessing the Web site, an attacker was able to browse sensitive customer billing and account information. To combat this, most cookies are now protected by a mathematical HASH that can identify any modifications, but they should still always be treated as suspect.

Some cookies also suffer from another weakness; they are based on timestamps, or improperly randomized data.

### Where are the cookies stored?

Each Web client has its own method for storing cookies. When a cookie does not have an expiration date set for it, it is only temporarily stored within a browser's memory. However, cookies that have expiration dates set remain on your hard drive long after you have visited the Web site. [Table 11-3](ch11.html#cookie_jar_locations) lists a collection of cookie locations for the most common browsers.

**Table 11.3. Cookie Jar Locations**

| Web Client | Cookie Jar Location |
| --- | --- |
| Netscape Navigator on Windows | In a single file called `cookies.txt` |
| Netscape Navigator on Mac OS | In a single file called MagicCookie |
| Netscape Navigator or Mozilla on UNIX | In a single file called `cookies.txt` |
| Internet Explorer | In individual files within a directory named Cookies |

## Web bugs

A *Web bug* is a euphemism for an invisible eavesdropping graphic embedded in a Web site, e-mail, or word processing document. Also called clear GIFs, invisible GIFs, beacon GIFs, and 1-by-1 GIFs, they are hypertext images that are generally 1-by-1 pixel in size. Web bugs can be used to track the following:

- The IP address of the computer that opens the image within the Web site, e-mail, or word processing document
- The time the computer opened the image
- The type of browser that the user opened the image with
- Any previous cookies for that site

In addition to the obvious tracking images displayed on the page, this HTML e-mail contains the following Web bug:

```
<BODY><B>From:</B> Orbitz
[Orbitz@email.orbitz.com]<BR><B>Sent:</B> Wednesday,
May 20, 2009 5:40 PM<BR><B>To:</B>
bugtraq@comcast.net<BR><B>Subject:</B>
FLIGHT DEALS: Vegas, LA, Orlando, and more!<BR><A
href="http://ad.doubleclick.net/jump/N2870.or/B914513.8;sz=1x
1;ord=[timestamp]?"><IMG
src="http://ad.doubleclick.net/ad/N2870.or/B914513.8;sz=1x1;o
rd=[timestamp]?"
border=0></A>
```

In this case, Doubleclick (the company responsible for most of the banners that appear on Web sites) has stored a 1-by-1 pixel image that is invisible to the naked eye. Nonetheless, by accessing this page, this pixel is retrieved from the Doubleclick ad server and a timestamp is stored. This information is used to tell Orbitz exactly when I viewed this e-mail. Web bugs such as this are also used to track where e-mails get forwarded. Because Microsoft Word also enables embedded HTML, Web bugs can also be used in documents to find out exactly when they are opened and who opens them.

## URL tracking

URL tracking is used to determine when, how often, and who is viewing a Web site. This tracking can be used to combine data from banner ads, newsgroup postings, and Web sites to determine how people are accessing your site. Data within the HTTP header is collected to associate the following:

- Browser types
- Operating systems
- Service providers
- Dates
- Referrers

When analyzed, this information can provide insight into improvements that can be made to increase advertising and response rates.

## Hidden frames

Another option to maintain state is through the use of hidden frames. The benefit of this approach is that it does not rely on any object left on the user's computer to operate. Data is simply passed from page to page as the user browses across the Web site. This method lends itself well to shopping cart instances, but does not provide the ability to track once the user exits the browser.

A hidden frame can be implemented in HTML by dividing the page into visible frames that require 100 percent of the browser space, and defining a second frame that requires 0 percent of the space. Because this frame is not allocated any room within the browser it is not visible, yet it maintains attributes as if it were. An example of this can be seen in the following HTML:

```
<HTML>
<FRAMESET ROWS="100%,*" FRAMESPACING="0">
<FRAME NAME="BROWSER" SRC="MAIN.HTM" SCROLLING="AUTO">
<FRAME NAME="HIDDEN" SRC="TRACKING.HTM">
</FRAMESET>
</HTML>
```

Both the "main" and the "tracking" pages are visited, but only the main page is visible. When the user clicks on links on the main page or progresses through the process of purchasing items, only the top frame is changed. The tracking frame remains active as an open session and is, therefore, able to maintain state for the duration of the activity.

## Hidden fields

Similar to hidden frames, hidden fields are commonly used to maintain the state of a Web session. Following is an example of how hidden fields are used by `www.google.com`:

```
<HTML><HEAD><meta http-equiv="content-type"
content="text/html; charset=UTF-8"><title>Google</title>
...
<input type=hidden name=hl value=en>
<input type=hidden name=ie value="UTF-8">
<input maxLength=256 size=55 name=q value=""><br>
<input type=submit value="Google Search" name=btnG>
...
</html>
```

When a query term is entered into the search form and the submit button is pressed, the Web site also submits tracking values for the variables named `hl` and `ie`. These values are used to indicate the language and character encoding with which subsequent pages should be displayed. Many browsers display information about hidden fields that can be obtained using the View menu.

# Attacking Web Servers

A Web server is a target for attack because of its high value and high probability of weakness. As it turns out, the Web servers that provide the highest value also provide the highest probability of weakness because they rely on multiple applications.

## Account harvesting

Harvesting information about legitimate accounts is the first step an attacker takes toward maliciously impersonating a user and gaining system access. This harvesting can be done by enumerating directory structures, investigative searching, and taking advantage of improper identity authentication.

### Enumerating directories

A common mistake made by Web site administrators is to allow directory listings. By default, any page named `index.html` or `index.htm` within a directory will be displayed. If this file does not exist and directory listings are allowed, the Web site may accidentally leak sensitive information.

Open directories such as this can be extremely dangerous because they may display files that an administrator does not intend to be available to users.

### Investigative searching

Pieces of information posted on the Internet are rarely forgotten (even years after being identified by a caching search engine). As a form of reconnaissance against a site, attackers will often harvest user names by using Web sites to search for e-mail addresses. Simple searching on the partial e-mail address [@someone.navy.mil](mailto:@someone.navy.mil) quickly turns up over a dozen e-mail newsgroup postings which each provide a unique user name that can be used in an attack. In addition, Web administrators often place e-mail addresses and sensitive information in the comments Web pages, which can provide an attacker with additional ammunition against a site.

### Faulty authorization

Mistakes in authorization can lead to account harvesting or, even worse, impersonation. As previously discussed in the "Cookie security" section, improperly implemented tokens can be used to gain or upgrade access to a Web site.

## SQL injection

Structured Query Language (SQL) is the American National Standards Institute (ANSI) standard for database query languages. Implemented in Access, Microsoft SQL Server, Oracle, Sybase, and Ingres, this standard has been accepted industry wide. Statements written in SQL are capable of adding, removing, editing, or retrieving information from a relational database.

For example, the sample database provided in [Table 11-4](ch11.html#sample_database_colon_attendeeinfo) is an example of a database.

**Table 11.4. Sample Database: attendeeinfo**

| First | Last | Location | Organization |
| --- | --- | --- | --- |
| Molly | Carroll | 22305 | University of Science |
| David | Michaels | 45334 | International Sales Corporation |
| Barbara | Richards | 35758 | Tungsten Tidal |
| Margaret | Carroll | 44506 | Association of Metallurgical Science |

The following SQL command will return the entries for customers Molly and Margaret Carroll:

```
select * from customerinfo where last='Carroll';
```

SQL injection occurs when a malicious user purposefully enters data into this table that will cause an error in its processing. For example, suppose that this information was collected through online registration for an International Metallurgical Convention.

If David Michaels had been a malicious user, he may have tried to *inject* SQL into his input by entering the following:

```
First Name:     David
Last Name:      Mi'chaels
```

Now the query string for this element has become the following:

```
select * from customerlist where last='Mi'chaels'
```

However, with the added single quote, this statement is syntactically incorrect and will result in an error:

```
Server: Msg X, Level X, State 1, Line 20
Line 20: Incorrect syntax near 'chaels'
```

This error would be even more serious if the malicious user were to add a semicolon and a command following the single quote that would be executed by the server:

```
First Name:     David
Last Name:      Mi'; shutdown–
```

Web sites that use SQL as a means of authentication are just as vulnerable. Take the following authentication query, for example:

```
Var login="select * from users where username = '" + username
+ "' and password = '" + password + "'";
```

The user can simply add another condition to the query string, which makes it always true to grant access:

```
First Name:     David
Last Name:      ' or 1=1–
```

# Web Services

A Web service is a collection of protocols and standards used for exchanging data between applications. Software applications written in various programming languages and running on various platforms can use Web services to exchange data over computer networks such as the Internet in a manner similar to interprocess communication on a single computer. This interoperability (e.g., between Java and Python, or Windows and Linux applications) is due to the use of open standards. OASIS and the W3C are the steering committees responsible for the architecture and standardization of Web services. To improve interoperability between Web service implementations, the WS-I organization has been developing a series of profiles to further define the standards involved.

The term Web services describes a standardized way of integrating Web-based applications using the XML, SOAP, WSDL, and UDDI open standards over an Internet protocol backbone. These will be explained in detail later in the chapter. XML is used to tag the data, SOAP is used to transfer the data, WSDL is used for describing the services available, and UDDI is used for listing what services are available. Used primarily as a means for businesses to communicate with each other and with clients, Web services allow organizations to communicate data without intimate knowledge of each other's IT systems behind the firewall.

Unlike traditional client/server models, such as a Web server/Web page system, Web services do not provide the user with a GUI. Web services instead share business logic, data and processes through a programmatic interface across a network. The applications interface, not the users. Developers can then add the Web service to a GUI (such as a Web page or an executable program) to offer specific functionality to users.

Web services allow different applications from different sources to communicate with each other without time-consuming custom coding. Because all communication is in XML, Web services are not tied to any one operating system or programming language. For example, Java can talk with Perl, and Windows applications can talk with UNIX applications. Web services do not require the use of browsers or HTML. Web services are sometimes called application services.

Web services are services (usually including some combination of programming and data, but possibly including human resources as well) that are made available from a business's Web server for Web users or other Web-connected programs. Providers of Web services are generally known as application service providers. Web services range from such major services as storage management and customer relationship management (CRM) down to much more limited services such as the furnishing of a stock quote and the checking of bids for an auction item. The accelerating creation and availability of these services is a major Web trend.

Users can access some Web services through a peer-to-peer arrangement rather than by going to a central server. Some services can communicate with other services. This exchange of procedures and data is generally enabled by a class of software known as middleware. Services previously possible only with the older standardized service known as Electronic Data Interchange (EDI) increasingly are likely to become Web services. Besides the standardization and wide availability to users and businesses of the Internet itself, Web services are also increasingly enabled by the use of the Extensible Markup Language (XML) as a means of standardizing data formats and exchanging data. XML is the foundation for the Web Services Description Language (WSDL).

The technology used to create a Web service is open source standards and protocols. These standards and protocols were not necessarily created for the sole purpose of creating and defining a Web service, but were, in some cases, adapted to be used for a Web service's needs. This includes the use of a protocol for transferring information in a platform and language independent manner, and a method for making remote function calls and procedure calls. With these requirements in mind, the definition for a Web service that will be used is as follows:

> *A Web service is a collection of standards and protocols that dictate the exchange of data between applications, and the execution of procedures remotely, independent of the programming language or platform the data or procedure is being executed upon. It is usually done over the Internet or World Wide Web*.

With this definition of a Web service, the next obvious question is, "What are the standards and protocols that are used?" Unfortunately, this question is almost as hard to answer as "What is a Web service?" There is much more common ground, however, simply because these Web services must interact with each other and therefore need to use the same standards and protocols.

## Web service standards and protocols

The Web service protocol stack is the collection of computer networking protocols that are used to define, locate, implement, and make Web services interact with one another. The Web service protocol stack consists mainly of four areas:

- **Service Transport** — This is responsible for transporting messages between network applications and includes protocols such as HTTP, SMTP, FTP, as well as the more recent Blocks Extensible Exchange Protocol (BEEP).
- **XML Messaging** — This is responsible for encoding messages in a common XML format so that messages can be understood at either end of the network connection. Currently, this area includes such protocols as XML-RPC, SOAP, and REST.
- **Service Description** — This is used for describing the public interface to a specific Web service. The WSDL protocol is typically used for this purpose.
- **Service Discovery** — This centralizes services into a common registry such that network Web services can publish their location and description, and makes it easy to discover what services are available on the network. At present, the UDDI protocol is normally used for service discovery.

## Service transport

These are the protocols and standards that dictate the transfer of information from process to process or service to service. These protocols and standards do not dictate how that information should be packaged, or what type of information it is (although sometimes headers contain information such as the MIME type in the case of HTTP). These protocols are application-level networking protocols. They are described and defined by RFCs (Request For Comments). These protocols were not developed necessarily for use by Web services. For example, HTTP and FTP were used well before Web services were even discussed, and simple text and binary files were being transferred between computers.

These protocols are platform independent, making data flow possible between any two machines. Also, these protocols are language independent because they are used simply to transfer data from one point to another. These protocols can be thought of as the analog of TCP/IP in the network stack. These protocols are usually the oldest and most well understood and implemented of the protocols surrounding a Web service.

## XML messaging

XML or **Extensible** Markup Language, according to Wikipedia, is "a W3C-recommended general-purpose markup language for creating special-purpose markup languages. It is a simplified subset of SGML, capable of describing many different kinds of data. Its primary purpose is to facilitate the sharing of data across different systems, particularly systems connected via the Internet."

In the context of a Web service, XML is used to encapsulate data in a platform and standard manner. XML is useful because the format of XML is well defined while allowing for personalized structures for specific applications. Some debate has surrounded XML because of its heavy use of ASCII characters to mark up a document. This makes XML data very large at times, and sometimes there is more meta information than actual data sent. However, XML has become the standard method for packaging information in Web services.

Other protocols such as SOAP have changed the way information is packaged and accessed in the context of a Web service.

There are several different types of messaging patterns in SOAP, but by far the most common is the Remote Procedure Call (RPC) pattern, where one network node (the client) sends a request message to another node (the server), and the server immediately sends a response message to the client.

SOAP originally was an acronym for Simple Object Access Protocol, but the acronym was dropped in Version 1.2 of the SOAP specification. Originally designed by Dave Winer, Don Box, Bob Atkinson, and Mohsen Al-Ghosein in 1998 with backing from Microsoft (where Atkinson and Al-Ghosein worked at the time), the SOAP specification is currently maintained by the XML Protocol Working Group of the World Wide Web Consortium.

HTTP was chosen as the primary transport protocol for SOAP because it works well with today's Internet infrastructure. Specifically, SOAP works well with network firewalls. This is a major advantage over other distributed protocols such as GIOP/IIOP or DCOM which are normally filtered by firewalls.

XML was chosen as the standard message format because of its widespread acceptance by major corporations and open source development efforts. Additionally, a wide variety of freely available tools significantly ease the transition to a SOAP-based implementation.

## Service description

This protocol describes what the Web service does. This description is used so the clients of a particular Web service can get information about what the Web service provides and how the information is provided. A language is created to make a succinct definition of the Web service. This language is again standardized so that it can work between different platforms and be interfaced by different languages.

The Web Services Description Language (WSDL) is an XML-based language used to describe the services a business offers and to provide a way for individuals and other businesses to access those services electronically. WSDL is the cornerstone of the Universal Description, Discovery, and Integration (UDDI) initiative spearheaded by Microsoft, IBM, and Ariba. UDDI is an XML-based registry for businesses worldwide, which enables businesses to list themselves and their services on the Internet. WSDL is the language used to do this.

WSDL is derived from Microsoft's Simple Object Access Protocol (SOAP) and IBM's Network Accessible Service Specification Language (). WSDL replaces both NASSL and SOAP as the means of expressing business services in the UDDI registry.

The W3C is responsible for the WSDL and has documentation that outlines and specifies exactly how the language/protocol operates. This document, as with most RFCs or other protocol standards documents, defines exactly how the protocol works and the notations that are used. The description is well over 100 pages long and very technical. The technical report is open, however, allowing all companies and research institutions the opportunity to comment and make suggestions or push technologies. The W3C defines WSDL as follows:

> *WSDL is an XML format for describing network services as a set of endpoints operating on messages containing either document-oriented or procedure-oriented information. The operations and messages are described abstractly, and then bound to a concrete network protocol and message format to define an endpoint. Related concrete endpoints are combined into abstract endpoints (services). WSDL is extensible to allow description of endpoints and their messages regardless of what message formats or network protocols are used to communicate. However, the only bindings described in this document describe how to use WSDL in conjunction with SOAP 1.1, HTTP GET/POST, and MIME*.

## Service discovery

With a protocol defined to describe the services provided by a Web service, the next logical step was to create a protocol that would discover the services provided by a Web service. The UDDI protocol is used for service discovery.

The Universal Description, Discovery and Integration (UDDI) protocol is one of the major building blocks required for successful Web services. UDDI creates a standard interoperable platform that enables companies and applications to quickly, easily, and dynamically find and use Web services over the Internet. UDDI also allows operational registries to be maintained for different purposes in different contexts. UDDI is a cross-industry effort driven by major platform and software providers, as well as marketplace operators and e-business leaders within the OASIS standards consortium (`www.uddi.org/`).

# Summary

Companies of every size use Web servers to provide information to the public. Because Web servers are so popular, they are also a common point of compromise for attackers to go after. Therefore, it is critical that Web sites be properly secured, and a key step in doing that is to understand how and why Web applications work. This chapter detailed the critical areas of Web security and what needs to be done to deploy a secure Web server.
