# Chapter 2. Introduction to TCPdump and TCP

![Introduction to TCPdump and TCP](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

Now that you have learned a bit about Internet Protocol (IP), you can take a closer look at how it works by using a practical analysis tool known as *TCPdump*. Just as you cannot do any kind of intrusion detection or traffic analysis without knowledge of TCP/IP, you cannot do analysis without a tool of some sort. TCPdump, or its Windows cousin Windump, is a popular and widely used piece of software that can give you some insight into the traffic activity that occurs on a given network. This chapter teaches you how to manipulate the tool for your own purposes and explains the output that it displays. The discussion then turns to one of the most important and common protocols, TCP. You are introduced to some theory, but the real goal is to enable you to catch a visual clue about TCP’s behavior by examining it using TCPdump.

An excellent free tool for packet sniffing and interpretation is known as Ethereal, which is available for both Windows and UNIX. It provides a GUI interface to interpret all layers of the packet and many times the payload. It is even protocol aware, meaning that it knows how to interpret the payload of many common protocols. For instance, it would know how to decipher a normally coded DNS query. You are probably wondering why Ethereal is not being used as the tool of choice in this book. First, it is more difficult to translate the Ethereal output to readable book format. TCPdump is more succinct and more easily viewed. Second, TCPdump is more primitive because it requires the user to do much of the interpretation of the output. The challenge is to make you think rather than hand you all the answers, as Ethereal does.

The second part of this chapter begins the discussion of network protocols with a discussion of TCP. All the chapters in this book that discuss network protocols follow a similar format. To give you insight into “normal” activity, the protocol is first presented as you would expect to see it under normal circumstances. However, because the Internet has become a wild and unpredictable arena, you are quite likely to see aberrant kinds of activity too. Each protocol chapter discusses some of the deviant departures you might encounter. This chapter follows that basic format.

# TCPdump

TCPdump is a UNIX tool used to gather data from the network, decipher the bits, and display the output in a semi coherent fashion. The semi coherent output becomes fully coherent output with a little explanation and exposure to the tool. When I first came to work at the Dahlgren Navy Laboratory, for example, I spent the first week watching a network analyzer. My boss, Bob Hott, came by every couple of hours to ask questions or have me give him a small assignment. At the end of the week, he had learned something about the behavior of IP and the character of his network. I strongly encourage you to spend some time watching your network traffic; your investment will pay off for you many times over in your journey as an analyst.

Although output from commercial tools might differ slightly or be more fashionable than TCPdump, TCPdump runs close to the metal and can help you understand other tools as well. This section demonstrates the use and demystifies the output of TCPdump.

**Where Do You Get TCPdump and Its Variants?**

You can download TCPdump from [ftp://ftp.ee.lbl.gov/tcpdump.tar.Z](ftp://ftp.ee.lbl.gov/tcpdump.tar.Z)

You need to download software known as libpcap, which implements a portable framework for capturing low-level network traffic. You can find it at [ftp://ftp.ee.lbl.gov/libpcap.tar.Z](ftp://ftp.ee.lbl.gov/libpcap.tar.Z)

This is the “official” version of TCPdump; Lawrence Berkeley Labs authored it. Yet, more recently, a collective effort has arisen to maintain and improve the code. More feature-rich versions are being developed and can be found at [www.tcpdump.org](http://www.tcpdump.org)

Windump is a Windows variant of TCPdump. You can download it from [http://netgroupserv.polito.it/windump](http://netgroupserv.polito.it/windump)

It also requires winpcap software to function. You can obtain winpcap from this same site.

## TCPdump Behavior

After TCPdump has been installed, most operating systems require root access to run it. This is because reading packets requires access to devices accessible to root-only. TCPdump is run by issuing the command **tcpdump**. By default, this reads all the traffic from the default network interface and spews all the output to the console. This is not always the behavior the user wants; in fact, this is pretty irritating because records are likely to fly by uncontrollably on a busy network. Therefore, many different command-line options are available to alter the default behavior.

### Filters

Suppose, for instance, that you don’t want to collect all the traffic from the default network interface. Maybe you are interested only in TCP records. TCPdump has a filter that enables you to specify the records that you are interested in collecting. TCPdump comes complete with a filter “language” to denote the field(s) in an IP datagram that should be examined and retained if the specified conditions are met. To collect only TCP records, issue the command **tcpdump ‘tcp’**. The filter in this example is **‘tcp’**.

Filters get much more complicated and restrictive than this simple one when you use combinations of fields and traits. Just about any field in an IP datagram, including the actual data payload, can be used to limit the purview of collected records. It seems logical that TCPdump should include a way to indicate that the filter is stored in a file so that users don’t have to type a long filter complete with ham-handed keystrokes on the command line itself. And true to logic, TCPdump has an **–F** filename option to indicate that the filter is located in the file filename.

### Binary Collection

As mentioned earlier, TCPdump dumps all the collected output to the screen. This is tolerable behavior if you are looking for a specific record. Most times, however, TCPdump is running in unattended mode, gathering records for retrospective analysis. To gather data for retrospective analysis, you want TCPdump to collect the records in a binary format, also known as raw output. When TCPdump displays records on the console, they have been translated from the native raw output format to a human-readable format. For retrospective analysis, the desired format for storage is the binary mode, in which all captured data is stored, not just the data translated for output. To collect in raw output mode, use the command **tcpdump –w** filename, in which filename is the name of the file to which the records will be written in binary format.

To read this raw output file, another command-line option is necessary: **tcpdump –r** filename. This option reads input to TCPdump from filename rather than from the default network interface. You can read a file that has been written using the –w option only by using TCPdump with the –r option. If you have ever used the UNIX tar utility, you know that when you create a tar file, often referred to as a tarball, you must read that same tar file using tar. The same principle applies with TCPdump.

### Altering the Amount of Data Collected

One final option is discussed before proceeding because it determines the amount of data that TCPdump collects. TCPdump does not attempt to collect the entire datagram sent. The reason for this is due to volume concerns and many times the user’s interest is in the header portions of the datagram that are usually collected with the default length. The snapshot length, sometimes known as snaplen, determines the exact number of bytes collected. One of the most common lengths of collected data is 68 bytes.

What exactly do you get with these 68 bytes of data? [Figure 2.1](ch02.html#ch02fig01) shows a sample breakdown of a packet. The header fields can be different lengths than depicted, based on the protocol and header options. First you have an encapsulating link layer header—if this were Ethernet, it would represent 14 bytes of Ethernet frame header with fields such as source and destination MAC addresses. Next, you have an IP datagram header, which is minimally 20 bytes if there are no IP options. The encapsulated protocol header (TCP, UDP, ICMP, and so on) follows that and can range from 8 bytes to more than 20 bytes for TCP headers with options. The data, or payload in the datagram, is collected after all the headers. As you can see, there might not be much, if any, payload collected because of the default snaplen. To alter the default snaplen, use the **tcpdump –s** length command, in which length is the desired number of bytes to be collected. If you want to capture an entire Ethernet frame (not including 4 bytes of trailer), use **tcpdump –s 1514**. This captures the 14-byte Ethernet frame header and the maximum transmission unit length for Ethernet of 1500 bytes.

![Sample packet.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/02fig01.gif)

**Figure 2.1. Sample packet.**

You can use many more command-line options with TCPdump. To learn about them, issue the command **man tcpdump command**. Be warned, however, that the output is copious (change the printer cartridge and restock the paper), but very informative if you have the patience and curiosity to wade through it.

## TCPdump Output

Because you will be seeing many TCPdump traces in this book, it is important for you to understand the format. One of the hardest tasks for the novice analyst to master is decrypting TCPdump output. TCPdump output is fairly standard for the different protocols (TCP, UDP, ICMP, for example), but does have some nuances. The first step is to identify the protocol that you are examining. TCP output will be used to explain the general TCPdump format. Here is a TCP record displayed by TCPdump:

```
09:32:43:910000 nmap.edu.1173 > dns.net.21: S 62697789:62697789(0) win 512 
```

- **`09:32:43:9147882`.**This is the time stamp in the format of two digits for hours, two digits for minutes, two digits for seconds, and six digits for fractional parts of a second.
- **`nmap.edu`.**This is the source host name. If there is no resolution for the IP number or the default behavior of host name resolution is not requested (TCPdump -n option), the IP number appears and not the host name.
- **`1173`.**This is the source port number, or port service.
- **`>`.**This is the marker to indicate a directional flow going from source to destination.
- **`dns.net`.**This is the destination host name.
- **`21`.**This is the destination port number (for example, `21` might be translated as FTP).
- **`S`.**This is the TCP flag. The *S* represents the SYN flag, which indicates a request to start a TCP connection.
- **`62697789:62697789(0)`.**This is the *beginning TCP sequence number*:*ending TCP sequence number* (data bytes). Sequence numbers are used by TCP to order the data received. For a session establishment such as this, the beginning sequence number represents the *initial sequence number* (ISN), selected as a unique number to mark the first byte of data. The ending sequence number is the beginning sequence number plus the number of data bytes sent within this TCP segment. As you see, the number of data bytes sent for a session establishment request is usually 0. That is why the beginning and ending sequence numbers are the same. Normal session establishments do not send data.
- **`win 512`.**This is the receiving buffer size (in bytes) of nmap.edu for this connection.

**TCP Flags**

Normal TCP connections have one or more flags set. Flags are used to indicate the function of the connection. [Table 2.1](ch02.html#ch02table01) shows the TCP flags, their representation in TCPdump, and their meanings.

**Table 2.1. TCPdump Flags**

| **TCP Flag** | **Flag Representation** | **Flag Meaning** |
| --- | --- | --- |
| SYN | `S` | This is a session establishment request, which is the first part of any TCP connection. |
| ACK | `ack` | This flag is used generally to acknowledge the receipt of data from the sender. This might be seen in conjunction with or “piggybacked” with other flags. |
| FIN | `F` | This flag indicates the sender’s intention to gracefully terminate the sending host’s connection to the receiving host. |
| RESET | `R` | This flag indicates the sender’s intention to immediately abort the existing connection with the receiving host. |
| PUSH | `P` | This flag immediately “pushes” data from the sending host to the receiving host’s application software. There is no waiting for the buffer to fill up. In this case, responsiveness, not bandwidth efficiency, is the focus. For many interactive applications such as telnet, the primary concern is the quickest response time, which the PUSH flag attempts to signal. |
| URGENT | `urg` | This flag indicates that there is “urgent” data that should take precedence over other data. An example of this is pressing Ctrl+C to abort an FTP download. |
| Placeholder | . | If the connection does not have a SYN, FIN, RESET, or PUSH flag set, a placeholder (a period) will be found after the destination port. |

TCPdump output for TCP is unique; the flag field and the sequence numbers are distinguishing characteristics. When you see these telltale signs in the TCPdump output, you know the record is TCP. UDP records are likely to have the word *udp* in the TCPdump output. Although true most of the time, just when you think you can rely on this as a steadfast way to identify UDP output, TCPdump throws you a curve ball. TCPdump analyzes some UDP services, such as *Domain Name Service* (DNS) and *Simple Network Management Protocol* (SNMP), at the application level in addition to the protocol level as UDP. Like Ethereal, it is protocol aware and can interpret normally coded payloads of certain protocols. The output might look foreign to you the first few times you see it because it does not have the word *udp* and because there are no TCP trademarks such as flags or sequence numbers. Typically, this is UDP output with more detail. Finally, ICMP is easily identified because the word *icmp* appears, without exception, in the TCPdump output.

## Absolute and Relative Sequence Numbers

Not to belabor the discussion of TCPdump output any more than is necessary, but TCP sequence numbers need to be addressed in a little more detail. Sequence numbers are associated only with TCP output, as just discussed. TCP sequence numbers are used by the destination host to reassemble TCP traffic that arrives. Remember that TCP guarantees order, whereas UDP does not. The sequence numbers are decimal number representations of a 32-bit field, so they can be pretty monstrous in size and intimidating to read. TCPdump helps make the output more coherent by changing from the absolute ISNs to relative sequence numbers after the two hosts exchange their ISNs. Look at the following TCPdump output. The time stamp has been omitted for the clarity and space-saving considerations:

```
client.com.38060 > telnet.com.telnet: S 3774957990:3774957990(0) win 8760 
<mss 1460> (DF) 
telnet.com.telnet > client.com.38060: S 2009600000:2009600000(0) ack 
3774957991 win 1024 <mss 1460> 
client.com.38060 > telnet.com.telnet: .ack 1 win 8760 (DF) 
client.com.38060 > telnet.com.telnet: P 1:28(27) ack 1 win 8760 (DF) 
```

The section, “[Establishing a TCP Connection](ch02.html#ch02lev2sec5),” discusses the actual theory of this output. For now, however, look at the numbers in bold. The first two numbers in the first two lines in bold represent the very large ISNs in absolute format that are exchanged from client.com and telnet.com, respectively. The third line has a number in bold that represents a relative sequence number—1. This means that client.com has acknowledged receiving the previous SYN by telnet.com with an ISN of 2009600000. The 1 as the acknowledgement value means that the next expected relative byte to be received by client.com is byte 1. That would have an absolute sequence number of 2009600001, if it were not displayed as a relative sequence number. If this seems confusing, the theory of acknowledgement numbers will be discussed in more detail in the upcoming section “[Introduction to TCP](ch02.html#ch02lev1sec2).”

The final line has the numbers 1 and 28 in bold to indicate that relative to the absolute sequence number of 3774957990, the 1st byte through (but not including) the 28th byte are sent from client.com to telnet.com. The final line also has `ack 1.`. This acknowledgement number will not change until telnet.com sends more data.

If you ever need to leave the sequence numbers in their absolute form, the TCPdump –S option will alter the default behavior of expressing TCP sequence numbers in relative terms after the exchange of the ISNs.

**Changing the TCPdump Collection Interface**

You might find that you want to read TCPdump traffic from a different interface than the default one. The default interface is the lowest number active one, not including the loopback interface. For instance, if you were on a Linux box and had two NIC cards, one might be known as eth0 and the next eth1. To change the default interface, the –i option of TCPdump is used. The following command will select ppp0 as the listening interface:

```
tcpdump –i ppp0 
```

## Dumping in Hexadecimal

TCPdump does not display all the fields of the captured data. For example, the IP header has a field that stores the length of the IP header. How do you display this field if it is not available from the standard TCPdump output? There is a TCPdump command-line option (–x) that dumps the entire datagram captured with the default snaplen in hexadecimal. Hexadecimal output is far more difficult to read and interpret, but it is necessary to display the entire captured datagram.

To interpret TPCdump hexadecimal output, you need some reference material that discusses the format of the IP datagram headers and describes what each of the fields represents. (One such reference title is *TCP/IP Illustrated, Volume 1*, by W. Richard Stevens.) You then must translate hexadecimal to decimal for numeric fields and numeric to ASCII for character fields. Ethereal is probably the best tool to use for translation of TCPdump records that are stored in binary form with the –w tcpdump command line option; it can read TCPdump binary data as input.

# Introduction to TCP

TCP is a reliable connection-oriented protocol used with well-known applications such as telnet or smtp. An application such as telnet cannot tolerate the uncertainty of the Internet Protocol that can lose datagrams or deliver them in a different order from which they were sent. TCP is the protocol that orchestrates and ensures reliability. It does so using the following mechanisms:

- ****Exclusive TCP connection.****When a TCP session is established, the connection is exclusive and unique between the two hosts. This kind of connection is called a unicast connection. The negotiation of the unique session allows both sides to track the traffic exchanged between the two hosts.
- ****TCP sequence numbers.****These provide a sense of chronology to the TCP data sent and received. A telnet command or exchange might take several packets known as TCP segments to transmit all the data. Data is assigned a TCP sequence number to uniquely identify the data in each segment being sent. Because the data might arrive in a different order from which it was sent, TCP sequence numbers are also used to reassemble the data in the correct order.
- ****Acknowledgements.****Acknowledgements are used to inform the sender that data has been received. Acknowledgements are made to sequence numbers to identify the exact data received. If the sender does not receive an acknowledgement for specific data in a given time, it assumes that the data has been lost. The sender will retransmit what it believes was lost.

## Establishing a TCP Connection

[Figure 2.2](ch02.html#ch02fig02) shows establishing a TCP connection is almost ceremonial in nature, involving what is commonly known as the three-way handshake. This is normally completed before any data is passed between two hosts. What is depicted is the client or source host initiating a connection to the server or destination host. The term *client* is used to mean the host requesting some kind of service from another host. A server is a host that listens on a well-known port number for requests of a particular service. TCP requires a destination port or service to be specified. Examples of destination ports are 23 (telnet), 25 (smtp), or port 80 (also known as the HTTP or the web server port).

![The three-way handshake.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/02fig02.gif)

**Figure 2.2. The three-way handshake.**

The three-way handshake proceeds as follows:

1. The client sends a SYN (SYNC) to signal a request for a TCP connection to the server.
2. If the server is up and offers the desired service, and can accept the incoming connection, it sends a connection request of its own signaled by a new SYN (SYNS) to the client and acknowledges the client’s connection request with an ACK (ACKC). This is all accomplished in a single packet.
3. Finally, if the client receives the server’s SYN and ACK of the SYN that the client sent and still wants to continue the connection, it sends a final lone ACK (ACKS) to the server. This acknowledges that the client received the server’s request for a connection.

After the three-way handshake has been executed in this manner, the connection has been established. Data can now be exchanged between the two hosts. If you examine the three-way handshake with a little more scrutiny, you will discover that two connections have really been established. The first is between the client and server and the second between the server and the client. This is because TCP is *full duplex*, which means that data exchanges can travel in either direction independently.

The following example shows the three-way handshake, using TCPdump to display the exchange:

```
tclient.net.39904 > telnet.com.23: S 733381829:733381829(0) win 8760 <mss 
1460> (DF) 
telnet.com.23 > tclient.net.39904: S 1192930639:1192930639(0) ack 733381830 
win 1024 <mss 1460> (DF) 
tclient.net.39904 > telnet.com.23: . ack 1 win 8760 (DF) 
```

In the first record, you see the client, tclient.net, attempt a connection to the telnet server, port 23, of telnet.com. You see the SYN flag set followed by the ISN, 733381829, and the same ending sequence number, 0 payload bytes in the parentheses. After that, you see a window size of 8760 and a *maximum segment size* (mss) that it advertises to the server. The window size of 8760 says that the client has an 8760-byte buffer for aggregated incoming data to this connection. The mss informs the destination host that the physical network on which tclient.net resides should not receive more than 1460 bytes of TCP payload (20-byte IP header + 20-byte TCP header + 1460-byte payload = 1500 bytes, which is the maximum transmission unit, or MTU, for Ethernet) at a time. In this case, even though the client, (tclient.net) can accept 8760 bytes of data, the physical medium on which it resides, most likely Ethernet, cannot accept more than 1460 bytes for a TCP payload size.

In the second record, you see telnet.com send a SYN and an ACK to tclient.net informing it that it is an available and willing participant in this connection and is willing to establish one of its own as well. telnet.com informs tclient.net of its ISN, 1192930639. This is also the ending sequence number because no data is sent; this is normal for the SYN/ACK records. The number following the ACK is the acknowledgement number, in this case, 733381830. Note that this value is the ISN advertised by tclient.net in the first record 733381829 plus 1. telnet.com has just acknowledged that it expects absolute byte number 733381830 as the next sequence number from tclient.net. telnet.com advertises a window size of 1024 and a maximum segment size of 1460.

In the final line, tclient.net sends the final lone ACK to telnet.com and acknowledges receiving the SYN/ACK flags from telnet.com. The value of 1 as the relative acknowledgement number indicates that it next expects the first byte from telnet.com. Also, notice that the sequence numbers have changed from absolute to relative values beginning with this record. Right after the destination part, following the colon, you see a period. Remember this is the placeholder value when none of the PUSH, RESET, SYN, or FIN bits is set.

## Server and Client Ports

In the past, more so than today, well-known server ports generally fell in the range of 1–1023. Historically under UNIX, only processes running with root privilege could open a port below 1024. These ports should remain constant on the host for which they are offered. In other words, if you find telnet at port 23 on a particular host one day, you should find it there the next day. You will find many of the older well-established services in this range of 1–1023 (such as telnet on port 23 and smtp on port 25). Today, some of the newer services, such as AOL Instant Messenger, usually associated with TCP port 5190, don’t tend to conform to this original convention. This is partially because there are more services than numbers in this range today.

Client ports, often known as *ephemeral ports*, are selected only for a particular connection and are reused after the connection is freed. These are generally numbered greater than 1023. When a client initiates a connection to a server, an unused ephemeral port is selected. For most services, the client and server continue to exchange data on these two ports for the entirety of the session. This connection is known as a *socket pair* and it will be unique. There will be only one connection on the Internet that has this combination of source IP and source port connected to this destination IP and destination port.

Someone from the same source IP might even be connected to the same destination IP and port. This user will be given a different ephemeral port, however, thus distinguishing it from the other connection to the same server and destination port. Two users on the same host might connect to the same web server. Although this is the same source IP, destination IP, and port (80), the web server can maintain who gets what by the ephemeral source ports involved.

Examine the three-way handshake exchange again, but this time in the context of client and server ports:

```
tclient.net.39904 > telnet.com.23: S 733381829:733381829(0) win 8760 <mss 
1460> (DF) 
telnet.com.23 > tclient.net.39904: S 1192930639:1192930639(0) ack 733381830 
win 1024 <mss 1460> (DF) 
tclient.net.39904 > telnet.com.23: . ack 1 win 8760 (DF) 
```

You see that tclient.net has selected ephemeral port 39904 on which to communicate and to connect to well-known port 23 of telnet.com. Any further exchanges after the three-way handshake are done using these two negotiated ports. After the connection is closed and some time has passed, tclient.net releases port 39904 for use by another connection. Port 23 of telnet.com remains bound to the telnet service for additional telnet requests.

## Connection Termination

You can terminate a session in two ways: the graceful method or an abrupt method. The graceful method is the phone conversation equivalent of you saying, “Thanks, but we’re not interested,” and hanging up on the telemarketer. This informs the telemarketer that the conversation is over and that he should now hang up and place another intrusive dinnertime call to some other hapless victim. The abrupt equivalent of this is just hanging up after you determine someone isn’t worth your valuable time.

### The Graceful Method

When the graceful TCP session termination method is conducted, one of the hosts, either the client or server, signals with a FIN to the other that it wants to terminate the session. The receiving host signals back with an ACK (to acknowledge the request). This terminates only half the connection. Then, the other host must initiate a FIN as well, and the receiving host needs to acknowledge this. Both sides need to initiate a FIN and acknowledge the other’s FIN because TCP is full duplex. Both the client and server send data in an asynchronous manner, so both sides of the connection have to be individually terminated. Look at the following two TCPdump exchanges:

1. Client initiates a close with a FIN, and server does an ACK, as follows: tclient.net.39904 >telnet.com.23: **F** 14:14(0) ack 186 win 8760 (DF) telnet.com.23 > tclient.net.39904: . **ack** 15 win 1024 (DF)
2. Server initiates close with a FIN, and client does an ACK, as follows: telnet.com.23 > tclient.net.39904: **F** 186:186(0) ack 15 win 1024 (DF) tclient.net.39904 > telnet.com.23: . **ack** 187 win 8760 (DF)

The connection between tclient.net and telnet.com is now closed.

### The Abrupt Method

> `The second termination method is an abrupt halting of the connection. This is done with one host sending the other a RESET. This signals the desire to abruptly terminate the connection.tclient.net.39904 > telnet.com.23: R 28:28(0) ack 1 win 8760 (DF)`

This output shows tclient.com as it aborts the connection to telnet.com. It sends a RESET to telnet.net to signal the intent to terminate immediately. There should be no further communication between the two hosts using the negotiated session after the abort.

## Data Transfer

Now that you know how TCP establishes and terminates a connection, it is time to take a look at what happens in between. Normally, the whole reason for establishing a session is so data can be exchanged between two hosts. The following data excerpt might be transferred between tclient.net and telnet.com after the three-way handshake and before the termination:

```
tclient.net.39904 > telnet.com.23: P 1:28(27) ack 1 win 8760 (DF) 
telnet.com.23 > tclient.net.39904: P 1:14(13) ack 1 win 1024 
telnet.com.23 > tclient.net.39904: P 14:23(9) ack 28 win 1024 
```

The first line shows tclient.net sending 27 bytes of data (a relative range of 1 to 28 bytes as seen in the parentheses) to telnet.com. This is the first time the new P flag has appeared; it represents PUSH. Because telnet is an interactive application that demands the fastest response time available, the PUSH flag signals to the receiver of the data, in this case telnet.com, to push the data immediately to the telnet application upon receipt of data in the incoming buffer. This line also acknowledges that the next relative sequence number expected by tclient.com from telnet.com is byte 1.

The second line shows telnet.com sending 13 bytes of data to tclient.com and acknowledging receipt of 1 byte of data from tclient.com. It has yet to acknowledge receipt of the 27 new bytes just sent by tclient.net. The final line shows telnet.com sending an additional 9 bytes to client.com. See how the relative bytes begin at 14 (`14:23`) bytes after the 13 (`1:14`) preceding bytes sent from telnet.com to tclient.net.

This exchange also acknowledges receipt of 27 bytes of data from tclient.net to telnet.com. You see `ack 28` because this is known as an *expectational acknowledgement*: Byte 28 is the next anticipated byte to be received. All traffic exchanges between the two hosts will have the ACK flag set after the three-way handshake has been completed. This is sometimes used as an indication of an established session.

## What’s the Bottom Line?

What if you need to analyze some traffic for malicious intent? Is it really necessary for you to absorb all the detailed theory about TCP to do any kind of analysis of TCP traffic of normal or anomalous behavior? The bottom line is that you can do elementary analysis without flipping bits. Here are some of the more general behaviors that you might examine:

- ****Was the three-way handshake completed between two hosts?****If it was, this means that the server listens at the port at which the client requested and the server accepted the connection. This is fine if the expected behavior is that the server listens at the requested port. However, what if the server port is not one that you expect to listen? This might indicate some service, known to the system administrator and not to you, is running. It might also mean, however, that someone maliciously installed some backdoor application on the server without your knowledge.
- ****Was data transmitted?****In TCPdump output, after the TCP sequence numbers, you find the number of data bytes in parentheses that were sent. If you see data transmitted, that means that the two hosts are speaking to each other. When you are doing some kind of retrospective analysis of unexpected activity between two hosts, looking at the number of bytes exchanged can come in handy in assessing the severity of what might have transpired. You might not be able to see the actual data bytes or payload, but numbers can be telling. Lengthy individual exchanges and the number of exchanges in aggregate can readily indicate potential damage by an intruder.
- ****Who began and/or ended the connection?****By determining which host initiated and terminated the connection, you get an idea of who is in control. Typically, the client requests the connection and the server responds (as you have already seen). Either host can end the conversation, so observe which one initiates the termination with a RESET or FIN.

**Damage Assessment**

Using TCPdump as a detective tool to analyze an attempted computer break-in is like investigating a burglary attempt or actual burglary. The first step in damage assessment is determining whether the perpetrator actually got into the computer system (or in the case of a burglary, into the house). Repeated SYN attempts to a system without a reply might be the equivalent of jimmying a door without successful entry. The completion of the three-way handshake is the equivalent of entry; it might just be through the garage door, which also requires a key to get into the house, but it is indicative of some kind of entry. The three-way handshake is the evidence equivalent of finding a previous locked door now unlocked or finding strange fingerprints inside the locked door.

The server port number can indicate the intruder’s interest. The use of a conventional port, such as telnet, means that perhaps the burglar might be doing a serious raid of goods (password files, trusted host relationships, and so on), the equivalent of a thief’s interest in jewelry and appliances. What about the unconventional port numbers that don’t support a known service? Is that the sign of some kind of a joyride through your system just to prove it can be done—kind of like coming home to find that someone drank all the milk in the refrigerator, threw the empty carton on the floor, and did or took nothing else?

Whereas the house burglary damage might be assessed by determining what is blatantly gone (the big-screen TV, for example), what about a burglar who broke into a big, fully stocked warehouse that didn’t keep good inventory records? How would you make an assessment of stolen goods? Perhaps a neighbor saw a strange vehicle in the driveway. Was it a moving van or was it a motorcycle? When you examine the number of bytes exchanged in the TCPdump output, you are in effect determining what kind of haul the burglar made off with. You are making best-guess efforts based on the little evidence that you have.

# TCP Gone Awry

In subsequent chapters, you will read many examples of the malicious attacks that employ TCP. [Appendix A](apa.html), “Exploits and Scans to Apply Exploits,” and [Appendix C](apc.html), “Detection of Intelligence Gathering,” discuss scanning methods that use different and sometimes unexpected combinations of TCP flags to perform reconnaissance on networks and circumvent detection or bypass filtering attempts. The following sections introduce some other anomalous TCP activity, such as an ACK scan, a telnet scan, and TCP session hijacking.

## An ACK Scan

Scans of ports are done for a variety of reasons, but they usually are used to discover whether a host or hosts are offering a particular service. If a host is found to be offering a service that might be exploitable, the hacker might try to break in using some vulnerability. Often, scans are blatant; the hacker makes no attempt to hide his reconnaissance of your network, except that the computer from which the scans originate might be compromised. The hacker assumes that either no one is monitoring the scanning activity or that by using the compromised host, no one can identify the hacker with the scan. Most likely there will be no attribution because no one can associate the hacker with the scan.

At times, however, the scanner attempts to be more furtive about the reconnaissance efforts in an attempt to evade notice. Examine the following activity, which is TCPdump output of many related connections. The prober can identify live hosts by those responding to the ACK scan. The deletion of time stamps makes it more readable:

```
ack.com.23 > 192.168.2.112.23: . ack 778483003 win 1028 
ack.com.23 > 192.168.31.4.23: . ack 778483003 win 1028 
ack.com.143 > 192.168.2.112.143: . ack 778483003 win 1028 
ack.com.143 > 192.168.31.4.143: . ack 778483003 win 1028 
ack.com.110 > 192.168.2.112.110: . ack 778483003 win 1028 
ack.com.110 > 192.168.31.4.110: . ack 778483003 win 1028 
ack.com.23 > 192.168.14.19.23: . ack 778483003 win 1028 
ack.com.143 > 192.168.14.19.143: . ack 778483003 win 1028 
ack.com.110 > 192.168.14.19.110: . ack 778483003 win 1028 
ack.com.23 > 192.168.33.53.23: . ack 778483003 win 1028 
ack.com.23 > 192.168.37.3.23: . ack 914633252 win 1028 
ack.com.23 > 192.168.14.49.23: . ack 3631132968 win 1028 
```

The preceding scan from ack.com sends an ACK flag to various different hosts on the internal 192.168 network. A lone ACK should be found only as the final transmission of the three-way handshake, an acknowledgement of received data, an acknowledgement of a received FIN, or data that is transmitted where the entire sending buffer has not been emptied. This is not the case in this scan because no other traffic is found from ack.com to indicate that this is a reaction to some natural catalyst.

This might be an attempt to find live hosts, somewhat akin to the function of ping. If a live host receives an ACK for either an open or closed port, it should respond with a RESET. Also, filtering routers that allow only “established” connections into the network (in other words, the ACK bit is set) will not filter this kind of scan. As sites become more security conscious and begin to block more traffic into the network, those who want to do reconnaissance have to become more clever and stealthy in the manner in which they scan, as shown in this example.

Note that the source ports are the same as the destination ports. This is not the expected behavior of the client selecting an ephemeral port with a value greater than 1023. This is another signature that helps to identify this scan. With the lone ACK flag set and identical source and destination ports, we can assume that this traffic has been “crafted.” Someone has written a program to execute this particular scan; it is not the result of normal TCP/IP stack traffic generation.

**Reserved Private Networks**

Throughout the text, you will see references of networks 192.168 and 172.16 as examples. These particular address spaces are part of what the governing body of the Internet, the Internet Address Numbers Authority (IANA), has deemed to be reserved private networks per RFC 1918. In other words, these are address spaces that should be used for internal networks and traffic should not be sent to or from these networks. These address spaces are often used so that a site will not exhaust its actual assigned addresses.

Traffic to these networks is not routable because these are private address spaces. When you see these address spaces used in examples, understand that they are being used to disguise the real address spaces that were scanned or probed. The intent is not to imply that traffic can be routed to theses networks via the Internet.

## A Telnet Scan?

Look carefully at the next scan. Short of finding Waldo in the output, do you see anything amiss?

```
scanner.se.45820 > 192.168.209.5.23: S 4195942931:4195942935(4) win 4096 
scanner.se.45820 > 192.168.216.5.23: S 4195944723:4195944727(4) win 4096 
scanner.se.52526 > 172.16.68.5.23: S 357331986:357331990(4) win 4096 
scanner.se.45820 > 192.168.183.5.23: S 4196001810:4196001814(4) win 4096 
scanner.se.52526 > 172.16.248.5.23: S 357312531:357312535(4) win 4096 
scanner.se.45820 > 192.168.205.5.23: S 4196007442:4196007446(4) win 4096 
scanner.se.52526 > 172.16.250.5.23: S 357313043:357313047(4) win 4096 
scanner.se.52526 > 172.16.198.5.23: S 357365266:357365270(4) win 4096 
scanner.se.52526 > 172.16.161.5.23: S 357355794:357355798(4) win 4096 
```

To the naked eye, it is a scan from scanner.se of destination hosts on the 192.168 and 172.16 subnets—specifically to destination port 23, or telnet. You might conclude that this is an attempt to find all hosts on the destination subnets that offer telnet, and that would be mostly correct. A subtle signature might indicate potentially evasive behavior, however. A SYN request usually sends no data bytes, but this scan sends 4 bytes, as you can tell by looking at the number in the parentheses.

You might imagine that the 4 bytes of data sent before the completion of the three-way handshake would be discarded. However, this is not the case. The 4 bytes should be included in the data after the handshake has been completed as noted by RFC 793. Any payload bytes that are sent during the handshake become part of the data stream after the completion of the handshake according to the RFC. This could be a good way to circumvent detection by an *intrusion-detection system* (IDS) that examines data sent only after the three-way handshake.

If you see 64 data bytes sent on a SYN connection to your DNS server to the DNS port 53, this might indicate a different issue altogether. Software known as 3DNS attempts to give users the quickest response time to web requests. One way that this is done is by attempting to measure the response time to your DNS server from one or more web servers that might be used to respond to the user’s request. As a representative size of a typical web request, 64 bytes are used. If you see this activity, it should not be considered stealthy; perhaps you might deem it invasive or annoying, or even ineffective because many sites block inbound activity to TCP port 53, but the intent is not malicious.

## TCP Session Hijacking

Although TCP appears to be a fairly safe protocol because of all the negotiation involved in session establishment and all the protocol and precision involved in data exchange, don’t get complacent. Evil sniffers can be set up on an unsuspecting host to capture TCP or other data that crosses the sniffers’ path. Sniffers that are placed on networks that are not switched can snoop clear-text data such as user IDs and passwords that are not encrypted in any way.

Session hijacking software, such as Hunt, uses another approach to exploit an existing TCP session. These attempt to intercept an established TCP session and hijack one end of the connection from the session to an evil host. The problem is that conventional TCP exchanges do not require any authentication or confirmation that they are the actual hosts involved in a previously established connection. After a session has been established between two hosts, those hosts use the following to reconfirm the corresponding host:

- ****IP number.****The established IP numbers of the hosts must not change.
- ****Port numbers.****Most protocols communicate between established ports only; ports do not change.
- ****Sequence numbers.****Sequence numbers must change predictably in respect to the ISN and the aggregate number of bytes sent from one host to another.
- ****Acknowledgement numbers.****Acknowledgement numbers must change in respect to delivered sequence numbers and aggregate bytes acknowledged from one host to another.

If a hostile user can observe data exchanges and successfully intercept an ongoing connection with all the authentication parameters properly set, he can hijack a session. Imagine the damage that can be done if this hijacked session is one that has root authority. Many complications and considerations are involved in session hijacking. It is not a trivial endeavor, but it is made simpler using the Hunt software.

# Summary

A vast and growing number of security tools are at your disposal.You have many tool choices when it comes to monitoring your network. When you decide which tool to use, make sure that the tool provides at least the level of detail that TCPdump offers. Admittedly, TCPdump does not provide especially aesthetic output, but it does give the required amount of detail to make intelligent assessments about traffic activity. If you select a tool that is easier on the eye, but lighter on content, you might not get the whole story.

TCP is the protocol used for applications that require reliable delivery. TCP exchanges follow a prescribed architecture of session establishment, possible data transfer, and session termination, replete with all the mechanisms to ensure delivery and receipt of data. When you observe TCP activity with TCPdump, you can delve into the details, if desired or necessary, or you can observe broader patterns and make more general assessments of the type of activity that has transpired.

TCP is a very robust protocol, and it has been robustly mutated for malicious uses. Carefully analyze it for the unexpected when monitoring TCP activity. As Intrusion Detection Systems (IDSs) and firewalls become more sophisticated in function, so do the hackers’ efforts to circumvent detection and shunning. It is important for an intrusion analyst to have a good understanding of TCP, and TCPdump is an excellent instructional tool.
