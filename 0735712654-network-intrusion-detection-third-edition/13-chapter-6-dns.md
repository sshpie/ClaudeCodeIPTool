# Chapter 6. DNS

![DNS](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

Why devote an entire chapter to DNS? Isn’t DNS used to translate a host name to an IP address and that’s about it? Sure, that is a big and important part of DNS, but DNS is much more.

DNS servers are probably one of the most common targets of reconnaissance and exploit efforts. Your DNS server is a cherished prize for a hacker to compromise, so hackers are going to see how vulnerable it is by pounding on it for weaknesses. DNS servers are targeted for the following reasons:

- DNS servers can provide a lot of reconnaissance information about hosts in preparation for launching an attack of a targeted network.
- DNS is used to resolve host names and IP addresses; so if a hacker can dupe a DNS server or actually seize control of a DNS server, she can manipulate name or address translations for malicious purposes. Often, weak methods of authentication rely on a host having a particular host name or IP address. If normal translations can be subverted, authentications can be corrupted.
- DNS servers are accessible and information sharing entities. The port commonly associated with DNS traffic, UDP port 53, is often left open on packet-filtering devices so that internal name servers can function.

This chapter covers these topics along with DNS theory and practical applications. You learn how DNS queries are answered, how DNS servers interact with other DNS servers, how DNS can be used to discover information about a site, and ways that DNS can be used for exploit purposes. In short, this information will aid you in applying network security and analyzing the nature of DNS traffic seen on the network.

# Back to Basics: DNS Theory

Again, TCPdump is enlisted to help explain and visualize what occurs with different types of DNS transactions. Specifically, this section examines how a DNS query is issued and answered. DNS differs from a normal client/server application, such as telnet, where the client requests a connection to a desired server and the interaction is between those two hosts. For DNS, however, when a client issues a DNS query, a DNS server accepts the query, perhaps interacts with one or more additional DNS servers, and then returns the response to the client.

This section looks at the structure of DNS as a distributed system, and it examines host name to IP address resolution. It also discusses the role of master (formerly known as primary) and slave (formerly known as secondary) name servers and discusses the interaction between them. You learn that unlike other services, DNS can switch between UDP and TCP protocols, depending on the kind of DNS activity.

## The Structure of DNS

DNS is a globally distributed system that depends on the cooperative interaction of many DNS servers to store records about “domains” and to communicate with each other. A domain is a subset of DNS records associated with a logical grouping. For instance, sans.org is a collection of records containing IP addresses, host names, name servers, and more associated with the sans.org domain. [Figure 6.1](ch06.html#ch06fig01) depicts the hierarchical nature of DNS.

![DNS, the pyramid scheme.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig01.gif)

**Figure 6.1. DNS, the pyramid scheme.**

Logically, the top node of the DNS tree is known as root—designated by the period (.). Functionally, this is represented by root servers that can act as the starting point for DNS resolutions. These servers just point to other DNS servers that might have dominion over the DNS records being sought. You are probably familiar with the top-level domains, those falling directly under the root servers (the long-established .edu, .org, .com, .net, .mil, and .gov; and the recently established .aero, .biz, .coop, .info, .museum, .name, and .pro, to name the domestic domains). There are additional top-level domains for foreign countries, such as .jp for Japan.

## Steppin’ Out on the Internet

Suppose that you want to visit www.sans.org, which is the home page for the System Administration, Networking, and Security (SANS) Institute. You enter www.sans.org in your browser, and seconds later you see the www.sans.org page.

Now, remember that IP datagrams use IP addresses for all source and destination addresses. IP knows nothing about host names. The human mind is more likely to remember that the capital of Florida is Tallahassee, than it is to remember the value of pi to 10 fractional digits is 3.1415926536, even though both take 11 characters (excluding the decimal) to represent. Names have more order and less randomness than numbers, so you tend to remember them better. This is why you speak in host names rather than IP addresses. It is apparent that some kind of translation mechanism is required between the way you reference hosts (via host names) and the way TCP/IP must reference hosts (via IP addresses).

So, how did this translation from www.sans.org to an IP address mysteriously occur behind the scenes? Before you could even send out a request to www.sans.org, your host had to know an IP address. Your host needs this IP address to insert into the datagram when it sends the connection request to www.sans.org out on the network. The following section unveils this somewhat transparent process.

**Recursive Versus Iterative Queries**

DNS queries come in two different varieties: recursive and iterative. A recursive query requires a name server to find the answer to the query itself. In other words, it might query name servers, such as root name servers that do not know the answer to the query but know references of name servers that possibly have the answer to the query. The name server must follow all the references until it finds a name server that has the answer. The bottom line is that a recursive query asks the queried DNS server to be the workhorse and finds an answer while the querying DNS server waits for the answer or performs unrelated queries.

An iterative query asks a name server to fetch the answer to a query. If the name server doesn’t have the answer, it returns to the querying name server a reference of another name server that possibly has the answer to the query. The queried name server does not pursue finding the answer; the querying name server must pursue finding the answer to the query itself.

### DNS Resolution Process

[Figure 6.2](ch06.html#ch06fig02) shows the beginning of the process of resolution from host name www.sans.org to IP address.

![Client resolver, the handoff.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig02.gif)

**Figure 6.2. Client resolver, the handoff.**

You see your browser is on host.my.com and it attempts resolution of www.sans.org. Assuming that your host is not a name server, it is mostly passive throughout the resolution process. It just fires off the request for the translation and resumes the process of connecting to the www.sans.org page after it receives a resolution of the IP address. The workhorse behind the resolution process is the DNS server that is queried (in this case, dns.my.com). Generally, a default name server is chosen at the time the operating system is installed on a given client machine. On UNIX machines, the information is stored in the file /etc/resolv.conf. The DNS server is set as a TCP/IP property in the Network portion of the Control Panel for Windows hosts. This default DNS server typically is managed locally and is located somewhere on your organization’s intranet. dns.my.com is this site’s DNS server.

On the client host, the TCP/IP applications, such as telnet, FTP, Netscape, or Internet Explorer, call “resolver” library routines to obtain DNS resolution. When you requested www.sans.org, application software issued a call to resolve the host name to an IP address. In this case, a gethostbyname call is sent from host.my.com to the DNS server. This requests host name translation of www.sans.org to an IP address. The DNS server receives this request, processes it, and returns it to host.my.com.

[Figure 6.3](ch06.html#ch06fig03) shows the second part of the resolution journey after leaving host.my.com. You see dns.my.com assumes the actual task of finding the answer of the IP of www.sans.org. For simplicity of theory (although this might be perceived as adding complexity to the actual resolution process), assume that dns.my.com knows nothing about www.sans.org or any other host in the .org domain. dns.my.com begins its search with a DNS root server to find the resolution.

![DNS server resolution, the cry for help.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig03.gif)

**Figure 6.3. DNS server resolution, the cry for help.**

If a DNS server has to resolve an unknown external host name and it has no knowledge of the host’s associated domains, it must contact a root name server. Root name servers are more than just a starting point—they maintain a mapping between domain names (sans.org) and the authoritative name servers—DNS servers that maintain DNS records for those domains. When the local name server, dns.my.com, asks a root name server for the IP address of www.sans.org, it gets back a referral to the name servers for sans.org. You might ask how dns.my.com knows the names and IP addresses of the root servers to contact. Obviously, the local name server must be preconfigured with a list of known root name servers. This information is maintained by the InterNIC and may be downloaded from [ftp://ftp.rs.internic.net/domain/named.ca](ftp://ftp.rs.internic.net/domain/named.ca).

Continuing the resolution adventure, the root server lets dns.my.com know where to continue its search. The root server has returned a referral to the name server server1.sans.org as an authoritative name server for www.sans.org. [Figure 6.4](ch06.html#ch06fig04) depicts dns.my.com querying server1.sans.org and receiving an authoritative answer, the IP address of 12.33.247.6.

![DNS server resolution, from the horse’s mouth](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig04.gif)

**Figure 6.4. DNS server resolution, from the horse’s mouth**

### TCPdump Output of Resolution

You can examine the traffic that this DNS request generated by observing the TCPdump output that follows:

```
host.my.com.1716 > dns.my.com.53: 1+ (35) 
dns.my.com.53 > h.root-servers.net.53: 12420 (30) (DF) 
h.root-servers.net.53 > dns.my.com.53: 12420- 0/3/3 (153) (DF) 
dns.my.com.53 > server1.sans.org.53: 12421+ (30) (DF) 
server1.sans.org.53 > dns.my.com.53: 12421* 1/3/3 (172) 
dns.my.com.53 > host.my.com.1716: 1* 1/3/3 
(197) (DF) 
```

First, host.my.com (the client exchanges from host.my.com are in bold) issues the request to resolve www.sans.org to dns.my.com. TCPdump analyzes DNS at the application level, which is why you don’t see the word `udp` embedded in the output even though this is UDP. UDP is the protocol selected for the transmission of the majority of DNS traffic because the queries and responses are often short and the application itself can tolerate lost data. When anticipated data is not received, the DNS query is reissued.

Next, dns.my.com attempts a connection to h.root-servers.net on port 53. Notice that both source and destination ports are 53. h.root-servers.net responds back to dns.my.com using source and destination ports 53 as well. A discussion of the numbers and notations found at the end of each TCPdump record is found in the next section, “[Strange TCPdump Notation](ch06.html#ch06lev3sec3).” h.root-servers.net does not have the answer to the query. It has a reference of another DNS server that either has the answer or has a reference of who might have the answer. Querying name servers for the IP of www.sans.org is an iterative process that yields a reference of another DNS server that might have the answer. This process repeats until contacting a name server that has the IP address answer.

Because h.root-servers referred dns.my.com to another DNS server, in the third line of the preceding output, you see dns.my.com query this server, server1.sans.org, for the IP for www.sans.org. server1.sans.org happens to “own” the DNS record for www.sans.org and can return the IP address associated with www.sans.org to dns.my.com. At long last, dns.my.com delivers the response to host.my.com.

TCPdump has a unique format that contains necessary insight into what is happening between DNS connections. Look at the next section to help you decipher the TCPdump output.

### Strange TCPdump Notation

Look at the exchange between dns.my.com and h.root-servers.net that follows:

```
dns.my.com.53 > h.root-servers.net.53: 12420 (30) (DF) 
h.root-servers.net.53 > dns.my.com.53: 12420- 0/3/3 (153) (DF) 
```

The first line of TCPdump output is the query from dns.my.com to the root server. The first field that you have not seen before in conventional TCPdump output is the number 12420, following the colon after destination port 53. This is the DNS identification number. It is a unique identifying number that a DNS server or client uses to match a query and response. dns.my.com issues the request to the root server with the number 12420, and when it receives a response, it can pair it to the request. You have to be aware that a busy dns.my.com is probably doing a lot of other queries while it is doing yours, so it has to be able to match multiple queries with responses. The length of the UDP payload (not including the IP or UDP headers) is 30 bytes. And, the Don’t Fragment (DF) flag is set so that this datagram won’t be fragmented.

The response to query 12420 follows. A dash after 12420 signifies that recursion was not desired. This means that dns.my.com told the root server that it wanted a response that referenced where the next DNS server is—it did not want the root server to pursue finding the response itself.

Root servers are very busy computers, processing many initial DNS requests, and they cannot process queries in a recursive fashion like dns.my.com can. Root servers are only expected to give whatever knowledge they have about a good reference in pursuit of the answer. If you were hopelessly lost in a city somewhere and came across a policeman directing traffic at a busy intersection, you would know better than to ask him directions to Aunt Sadie’s place. If you had the poor sense to ask, the best you could hope for is a general hasty reference to a gas station that could give you better directions.

In the response from the root server, you see some strange output in the format of 0/3/3. This says that there were zero answer records, meaning no IP address was found, but three authority records were found and three additional records were found. An authoritative server is one that “owns” and maintains records for a given domain. You don’t see this in the TCPdump output, but the three authoritative servers (server1.sans.org, ns.BSDI.COM, and ns.DELOS.com) and the three additional records are shown with the pairing of the authoritative DNS servers with their IP addresses.

AUTHORITY RECORDS

|  |  |
| --- | --- |
| sans.org | nameserver = server1.sans.org |
| sans.org | nameserver = ns.BSDI.COM |
| sans.org | nameserver = ns.DELOS.COM |

ADDITIONAL RECORDS

|  |  |
| --- | --- |
| server1.sans.org | Internet address = 167.216.198.40 |
| ns.BSDI.COM | Internet address = 206.196.44.241 |
| ns.DELOS.COM | Internet address = 65.102.83.117 |

The section, “[Using DNS for Reconnaissance](ch06.html#ch06lev1sec2),” shows you how to use the **nslookup** command to discover this information. By sending the IP addresses in additional records, when using the returned authoritative name servers, subsequent resolutions are unnecessary to translate those returned host names to IP addresses. Any one of those DNS servers has authority for the sans.org domain and can answer the query. As you saw, dns.my.com selects the first one, server1.sans.org, to use for the final resolution.

Finally, examine the remainder of the TCPdump output from the resolution process:

```
dns.my.com.53 > server1.sans.org.53: 12421+ (30) (DF) 
server1.sans.org.53 > dns.my.com.53: 12421* 1/3/3 (172) 
dns.my.com.53 > host.my.com.1716: 1* 1/3/3 
(197) (DF) 
```

dns.my.com has been informed that there are several authoritative servers, and it selects the first one, server1.sans.org, for resolution. It issues a new query 12421 and asks for recursion, noted by the plus sign. Essentially, dns.my.com has tasked server1.sans.org to find the IP address. In this case, server1.sans.org is an authoritative name server for www.sans.org, so it can answer the query itself. If it were not the authoritative name server, however, it would be asked to find the IP address by recursively issuing queries to other name servers until an IP address was found. Not all DNS servers are configured to perform recursive queries; so even though recursion might be desired, it is not necessarily done.

server1.sans.org responds to the query. The asterisk means that this is an authoritative response. This says that the record for www.sans.org is in the DNS database that server1.sans.org maintains. One answer is returned—in this case, the IP address of www.sans.org, 12.33.247.6. You do not see the IP in the TCPdump output, but that is what is in the payload of the UDP datagram. The three authority records and three additional records that were previously discussed are returned here too. Lastly, after dns.my.com has the IP address, it returns it to host.my.com, the original querier.

## Caching: Been There, Done That

This section briefly explains what happens to received responses. DNS servers cache or save responses that they receive. This makes the resolution process more efficient if the same DNS queries do not have to be repeated over and over again. This also potentially reduces the number of hits that other DNS servers take responding to queries. Chances are pretty good that the same host name to IP resolution that was requested once may be requested again soon thereafter. But, as you will soon see in the section, “[Cache Poisoning](ch06.html#ch06lev2sec14),” these savings, gained by caching responses, will open up some security risks if cached responses are not authentic and valid.

If you were to ask for the www.sans.org web page again soon after the first request, the resolution process would differ a little. Your host still issues a gethostbyname call to resolve the IP address for www.sans.org. When dns.my.com receives this request, however, it checks its cache as usual before trying to resolve it. If everything is working correctly, dns.my.com finds the record residing in cache and returns the IP address to host.my.com.

How long do cached records stay around on the DNS server? Well, it depends. Each cached record might have a different life span. It turns out that each response of a DNS resource record has a DNS time-to-live (TTL) value. Don’t confuse this TTL value with the IP header TTL. They represent two very different and distinct functions. The DNS TTL value is set by the responding DNS server and cached by the receiving name server for the TTL time value. DNS servers that update records often are more likely to have lower TTL values than relatively static servers have.

**Berkeley Internet Name Daemon**

Berkeley Internet Name Daemon (BIND) is the *de facto* standard DNS implementation in use on the Internet today. Older versions of BIND are 4.x.x, whereas the more current versions are 8.x.x and 9.x.x. When you observe DNS servers that communicate with both source and destination ports of 53, it is usually indicative of the default behavior of BIND 4.x.x. By default, BIND versions 8 and later assign an ephemeral source port greater than 1023 in a querying DNS server datagram, similar to the behavior that you witnessed with other client applications, such as telnet.

However, BIND versions 8 and later can be configured to mimic version 4 behavior by using a default source port of 53. This is done using the **query-source address * port 53** configuration file substatement. Some sites find that this configuration better suits existing firewall/router access rules.

## Reverse Lookups

Occasionally, you will be given an IP address and want to see whether it resolves to a host name. This is done via a gethostbyaddr call by the client resolver.

Remember, DNS is a distributed hierarchy of responsibility, and resolution begins at the root node and continues down in the DNS tree.You saw top-level domain nodes, such as .org, .mil, .edu, and so forth. A special domain has been reserved for resolution of IP addresses to host names. At the top-level domain, this is the arpa suffix. A second-level domain follows, known as in-addr. The tree expands outward beneath this for the legal first octets in the IP address, as you see in [Figure 6.5](ch06.html#ch06fig05). In the case of the IP for www.sans.org, for instance, the first octet is 12. Beneath this follows a subtree with the next node of 33, the second octet of the www.sans.org IP address. Continuing with this logic, the 247 and 6 nodes for the final two octets fall below. Only this subtree is examined in this example, but this subtree spans all the possible IP addresses just as the other top-level domains begin the expansion of all the host names.

![Reverse lookups, IP address to host name.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig05.gif)

**Figure 6.5. Reverse lookups, IP address to host name.**

Resolutions of IP to host name are known as reverse lookups. When DNS attempts a reverse lookup for 12.33.247.6, the application software reformats this as a query to 6.247.33.12.in-addr.arpa. The order of the octets is reversed to conform to the host name notation. For name www.sans.org, the name is formulated by starting at the bottom of the DNS tree with node www, moving up to node sans, and topping out at node org. Similarly, with the IP address, you must move from the most specific to the most general.

## Master and Slave Name Servers

Each domain must have a master server, upon which database records of names and IP addresses are maintained. Then, for redundancy sake, one or more slave servers are often created in case the master server ever goes down. If there is no redundancy built in and the only DNS server for a particular domain were to go down, no queries could be answered for hosts in that domain. Unless entries were cached at other DNS sites, resolution of hosts in the domain whose DNS server was down could not be accomplished. Slave servers can share the load of responding to queries with a fully functioning master name server.

DNS information is maintained on the master server in flat text files. The slave name servers periodically contact the master name server to see whether any updates have been made for a particular domain. If so, the slave servers with older versions of BIND download all information for that domain, even if only one record has been modified. Newer versions of BIND will allow incremental updates that will download only changed records.

## Zone Transfers

This section examines how changes are propagated from the master to the slave name server. When the slave server restarts, or when it periodically queries the master server and finds updated records, a zone transfer is performed between the master and slave servers.

This is just a transfer of the zone maps or DNS records from the master server to the slave server. Unlike most DNS transactions, this is done using TCP because there is potentially a lot of data and reliable delivery is important. The zone transfer seems like an innocuous process. It usually is between the same domain master and slave servers. Yet, what if a hacker could do a zone transfer of your domain data for your internal hosts? This would give him all the IP addresses and hosts in your domain. This is very valuable data that should not be readily available to anyone.

Obviously, you would like to try to prevent this kind of misuse. You can do this in a couple of ways. In versions of BIND 4.9.3 and later, configuration parameters enable the DNS administrator to specify IP addresses or subnets authorized to do zone transfers. BIND 4.9.x has an xfernets directive, and BIND 8 and 9 have an allow-transfer substatement to control zone transfers.

If your version of BIND does not support this feature, another option is to block inbound traffic to TCP port 53. This block prevents transfers, but might block other legitimate data as well (as discussed in the very next section). If this is your only option, however, it is preferable to prevent the zone transfer, even at the expense of blocking other legitimate data.

## UDP or TCP

As discussed earlier, typically, DNS traffic is sent using UDP because answers are often succinct, and a best-delivery effort can be tolerated because responses to DNS queries not received can be reissued. Because there is more data for zone transfers, and reliable exchange is required, they are an exception to the UDP protocol and are done using TCP.

The maximum allowable size for a UDP DNS payload response is 512 bytes. What happens if the data contained in the DNS message exceeds 512 bytes? First, the response is returned with the truncated bit turned on. This bit is found in the flags field spanning offset bytes 2 and 3 of the DNS message:

```
dns.my.com.53 > dns.verbose.com.53: 18033 (43) (DF) 
dns.verbose.com.53 > dns.my.com.53: 18033| 7/0/0 (494) 
dns.my.com.37404 > dns.verbose.com.53: S 518696698:518696698(0) win 8760 <mss 
1460> (DF) 
dns.verbose.com.53 > dns.my.com.37404: S 199578733:199578733(0) ack 518696699 
win 8760 <mss 1460> (DF) 
```

In the preceding output, look carefully at the second line of TCPdump output. The response is from dns.verbose.com to dns.my.com. After the DNS identification number, 18033, you see a vertical line, or UNIX pipe symbol. This is the notation that TCPdump uses to alert you that the DNS record has been truncated. The response of seven resource records would have exceeded the 512-byte payload limit. You see that 494 bytes of payload are returned, consisting of complete answers that do not exceed the limit.

Therefore, dns.my. com reissues the DNS query using TCP. You see the attempted SYN connection from dns.my.com to dns.verbose.com. dns.verbose.com responds with a SYN/ACK, indicating that it is listening on port 53. The information is then transferred using TCP as the protocol.

Some sites will block all inbound TCP traffic with either a source or destination port of 53 to prevent unauthorized zone transfers. But, this will also block any queried external DNS server from resolving large responses. That is what happens in the preceding output. The fourth line in the previous output shows the packet with the SYN/ACK from dns.verbose.com that got blocked. Our packet-filtering device in front of dns.my.com blocks a TCP connection from dns.verbose.com source port domain (53). That is why the three-way handshake is never completed and the large DNS response is never delivered. To avoid this problem, block traffic to TCP destination port 53 only and allow traffic from TCP source port 53 that has an already established connection.

## Summary of DNS Theory

DNS relies on a complex interweaving of many DNS servers.You must be able to examine traffic to and from your DNS server to understand the nature of the activity. TCPdump is an adequate tool to use; but at times, you have to use other tools to examine the content of the datagrams to see whether problems exist. Typical DNS servers on active networks receive a lot of traffic, and hackers can use the volume of normal activity as a smoke screen for malicious activity.

# Using DNS for Reconnaissance

Given the notion that DNS is a global database, it is an excellent source for reconnaissance. DNS information is intended to be freely shared and freely available in the spirit of cooperation. At one time in the evolution of the Internet, this was a relatively innocuous philosophy. In today’s climate of hungry pirates, however, it seems quite naive. Here are some ways in which reconnaissance can be done using DNS.

## The nslookup Command

nslookup acts much like a DNS client would, but displays the information so that you can see it. In fact, that is how the authoritative name server host names and IP addresses for the sans.org domain were obtained. This is a very helpful interactive tool that can be used on a UNIX or Windows NT (and beyond) host. Some UNIX operating systems are beginning to replace the **nslookup** command with the **dig** (Domain Internet Groper) command.

You can ask many more questions of a DNS server than just the host name. Using nslookup, you can formulate queries and see the kinds of responses you get. There is also a debug setting that enables you to see more of the data in the DNS message that is sent and returned than just the query and response values.

Look at the following output to get an idea of the capabilities of the nslookup tool. You see host.my.com issue the **nslookup** command. You then enter into the nslookup interactive process and receive notification of the default DNS server, dns.my.com and its associated IP address (192.168.4.4) used to resolve your queries. The output follows:

```
host.my.com% nslookup 
Default Server:  dns.my.com 
Address:  192.168.4.4 

> www.sans.org 
Server:  dns.my.com 
Address:  192.168.4.4 

Name:    www.sans.org 
Address:  12.33.247.6 
```

At the greater than (`>`) prompt, `www.sans.org` is entered to find its IP address. Again, you get confirmation of the DNS server and IP address being used to resolve the query. You see the answer below that of 12.33.247.6.

### Name That Name Server

How does someone discover what your DNS server is? Given the number of reconnaissance attempts targeting DNS servers only, there must be a way to find out. Actually, it is rather easy to find this out using nslookup:

```
> set type=ns 
> sans.org 
Server:  dns.my.com 
Address: 192.168.4.4 
```

NON-AUTHORITATIVE ANSWER

sans.org nameserver = NS.DELOS.COM

sans.org nameserver = server1.sans.org

sans.org nameserver = NS.BSDI.COM

AUTHORITATIVE ANSWERS CAN BE FOUND FROM

NS.DELOS.COM Internet address = 65.102.83.117

server1.sans.org Internet address = 167.216.198.40

NS.BSDI.COM Internet address = 206.196.44.241

Assuming that you are at a subcommand prompt of the **nslookup** command, enter the subcommand **set type=ns**. You have just set the option to return an answer of a name server(s) to subsequent queries issued. Bump up one node on the DNS tree and query for sans.org to see the name servers for this domain. You discover all the name servers for sans.org, both host names and IP addresses. This appears to be a pretty good place to start the reconnaissance effort for a site. After discovering the name servers, one might scan those name servers for potential security deficiencies or to see what kind of Internet services or daemons are being run on the DNS server.

## HINFO: Snooping for Details

HINFO records are yet another record type stored by DNS. These are information records and another potential source for reconnaissance. A DNS server administrator has the option of entering host information, specifically the CPU type and operating system, when creating a new or maintaining an existing DNS record. If trusted intranet hosts use the DNS server, this is a way to maintain an inventory of the hosts without too much risk.

Because this provides too much information to unknown Internet users, many administrators do not enter these parameters. Obviously, if this type of information can be harvested from a DNS server, a hacker can get some serious intelligence about the site.

```
> set type=hinfo 
> host49 
Server:  dns.my.com 
Address:  192.68.4.4 

host49.my.com CPU = SunSparc          OS = Solaris 
my.com nameserver =dns.my.com 
dns.my.com     Internet address = 192.68.4.4 
```

Set the type to **hinfo** as a subcommand in nslookup. Information is queried for host49, which is a fictional renaming of a real host. host49.my.com is a Sun SPARC running a version of the Solaris operating system. It is possible that a hacker’s efforts might be foiled by outdated data kept in the HINFO records. This is probably one of the few times that less-than diligent maintenance is a desirable thing.

## List Zone Map Information

One of the easiest ways to discover a lot of information about a domain is to try to list all the zone map information. Assume that there is a domain with the lackluster name of fakeplace.com. You can attempt to dump the records associated with the domain using the following subcommand in the nslookup utility:

```
> ls –d fakeplace.com 
```

If the site has not disabled the dissemination or transfer of the data, the DNS server lists all records for the domain fakeplace.com. As a bonus to the information collector, this site also maintains HINFO records.

```
whish       1D IN HINFO       "SGI" "Irix" 
1D IN A                 192.168.1.239 
susie       1D IN HINFO       "IBM-RS/560F" "unix" 
1D IN A                 172.16.16.13 
pixie       1D IN HINFO       "IBM-RS/560F" "unix" 
1D IN A                 172.12.16.14 
bandit      1D IN HINFO       "PC" "Win98" 
1D IN A                 192.168.3.107 
adder       1D IN HINFO       "IBM-RS/530" "unix" 
1D IN A                 172.16.133.4 
hub21       1D IN HINFO       "Cabletron-MMAC3" "SNMP" 
1D IN A                 192.168.26.80 
switch3     1D IN HINFO        "Switch" "3COM" 
1D IN A                 192.168.7.130 
```

This information harvesting can occur only if the site allows indiscrimate access to TCP destination port 53, because TCP is the transport protocol used to deliver this information.

## Dig

Another information gathering technique is to query a DNS server for its BIND version number:

```
dns.my.com% dig @MYDNS.COM version.bind txt chaos 

; <<>> dig 8.1 <<>> @MYDNS.COM version.bind txt chaos 
; (1 server found) 
;; res options: init recurs defnam dnsrch 
;; got answer: 
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10 
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0 
;; QUERY SECTION: 
;;      version.bind, type = TXT, class = CHAOS 

;; ANSWER SECTION: 
VERSION.BIND           0S CHAOS TXT    "4.9.7-REL" 
```

A tool called **dig** (which stands for Domain Internet Groper) comes with many implementations of BIND. It has many of the same capabilities as nslookup. You have an option to display the version number of BIND running on a DNS server. The format of the command is as follows: **dig** followed by the at sign (**@**), followed by the name of the DNS server you want to examine, followed by the option **version.bind**, followed by the word **TXT** and the word **CHAOS**. The word **TXT** tells DNS that the type of entry you are searching for is a TXT record found in the DNS database. This is just a different record type, much as HINFO records and NS records are different types. Finally, you see the word **CHAOS**, which is a query class that is mostly obsolete.

This **dig** command has queried for the version number of MYDNS.com. You see that it is running an older version 4.9.7 of BIND. For someone conducting reconnaissance, this is valuable information. If a hacker can pair a BIND vulnerability with the version discovered, she is better able to target the name server for attack. BIND versions 8.2 and later have an options statement in the configuration file /etc/named.conf that will return a message instead of the version number. You select the contents of the message, perhaps something like “unknown version of BIND.” But, if you feel mischievous, your message can return the wrong version of BIND just to confuse the information gatherer.

# Tainting DNS Responses

As discussed earlier, DNS requires the cooperation of many unknown or untrusted hosts to function properly. You have to blindly trust that the response received to a DNS query is genuine. Unfortunately, this is not always the case. This section presents a sampling of DNS problems and perversions related to DNS record authentication.

## A Weak Link

One of the weaknesses in using host names to allow or deny access to a given service is that if a host can assume a bogus identity of a trusted host, all authentication can be subverted. Think of the types of access allowed based on host name or perhaps on an entire domain name. Do you allow access to an intranet web server for all internal hosts because they are part of your domain? Or, do you use UNIX hosts that allow access without user ID and password authentication based on a trusted host name? That can be very risky behavior if true identities are altered to masquerade as trusted hosts. A host name can be changed on a host itself, on a DNS server that has been compromised and altered until discovered, or on a DNS server temporarily by corrupting a cached DNS record.

Versions of BIND, beginning with BIND 8.3, include DNS Security Extensions (DNSSEC) to provide better authentication mechanisms based on cryptographic signatures to validate the integrity and origin of DNS data. To authenticate a set of responses, a responding DNS server will “sign” them by encrypting a hashed incarnation of the set of responses with the DNS zone’s private key. This signature will be returned to the resolver via a new resource record known as SIG. The resolver needs to get the DNS server’s public key for the appropriate zone, which is done using another new resource record known as KEY. After it is obtained, the recipient decrypts the signature using the public key to obtain the original hash of the data. The recipient then computes its own hash of the received set of responses, using the same algorithm the DNS server used. It compares the response it receives, and if it matches the decrypted one from the server, it means that the data has not been altered and it is from the professed source.

## Cache Poisoning

A Computer Emergency Response Team (CERT) advisory (CA-97.22, issued in August 1997) warns of a vulnerability in versions of BIND.Versions before release 8.1.1 were vulnerable to caching malicious or misleading data from a remote server. A hostile user could use a remote DNS server to put incorrect DNS records in the cache of a victim DNS server.

For this to happen, first, an evil user must force your vulnerable local name server to query the evil user’s hacked DNS server. The query is for some innocent piece of information, but the response contains corrupted resource records that your vulnerable DNS server caches.

This “poisoned” data is then returned in any responses for the poisoned record asked of the tainted DNS server. The cache-poisoning techniques are used to corrupt the mapping between host names and IP addresses.

Another of the cache-poisoning exploits is successful because it sends answers with a query record. When any type of DNS traffic is sent, a DNS message is contained in the datagram. The same DNS message format is used for both queries and responses. It appears that some errant versions of BIND cache whatever they find in the response section of the DNS message. They don’t check to make sure that the record is a response and not a query. The evil user sends a query to your vulnerable DNS server with poisoned answers in the query, and the DNS server caches these tainted responses.

[Figure 6.6](ch06.html#ch06fig06) shows an example of how cache poisoning can work. Suppose there is a wicked user who crafts a DNS message with a response in the request. This same user can then send a query using the source host evil.dns.net and the destination DNS server of ns04.baweb.com, the authoritative name server for www.hillary2000.org.

![DNS cache poisoning.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/06fig06.gif)

**Figure 6.6. DNS cache poisoning.**

This crafted packet has a query for the IP address of www.hillary2000.org, but it includes an IP address in the response part of the DNS message, which gives the IP address of 206.245.150.74. This is not the real IP address associated with www.hillary2000.org, as you will soon see.

ns04.baweb.com suffers from the inability to tell query from response, and therefore caches the answer it received in the query. Its cache has just been poisoned with a bogus host name and IP pairing. Now, to complete the ruse, there must be a DNS server on behalf of a user or process that consults ns04.baweb.com for the IP address for www.hillary2000.org. In response, the cached answer of 206.245.150.74 is returned.

This is a real-world example in alleged political cyber-warfare. In July 1999, Hillary Clinton launched a web site, www.hillary2000.org, which promoted her to-be-declared run for the U.S. Senate from New York.

When some users attempted to contact this site, however, they were redirected to a rival site, www.hillaryno.com (IP address 206.245.150.74). The supporters of then New York City mayor Rudolph Giuliani maintained this site. (Mayor Giuliani, at the time of these mysterious occurrences, was an undecided contender for the same seat; he subsequently decided not to run.)

The speculation is that this might have been a cache-poisoning hack that successfully diverted Hillary supporters to the Giuliani page. In other words, www.hillary2000.org was paired with the IP address for www.hillaryno.com. Of course the people who maintained the www.hillaryno.com site, disavowed all knowledge of any wrongdoing.

So, you see that the arsenal of political dirty tricks has now entered the realm of cyberspace. This would be a very hard kind of hack to trace or prove if the cache were poisoned to reroute users.

# Summary

DNS is a distributed hierarchy of name servers that provides different types of resolutions, such as IP addresses and host names. Unlike typical client/server interactions, the resolution of a DNS query might involve multiple DNS servers and multiple connections. And, unlike other client/server interactions, DNS might use UDP, or TCP, or both as the transport protocol to do resolutions.

DNS servers can provide a wealth of reconnaissance information because historically, DNS servers have been the purveyors of host name to IP address pairing information. Sadly, as the Internet has become less safe and less trusted, it is best to silence DNS servers by offering only limited information.

BIND software has a notorious history of security problems. Several exploits have been discovered in recent years that have allowed root level access from buffer overflow attacks. But, it is pretty much impossible to use the Internet today without some kind of interaction with DNS. This doesn’t mean that you should innocently trust answers received from other DNS servers, but you should certainly safeguard your own DNS server as much as possible. Upgrade your DNS server to the newest versions, take advantage of the latest security features, and configure your site’s DNS servers to restrict the information shared.
