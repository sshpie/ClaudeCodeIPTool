# Chapter 24. Mail Protocols

**IN THIS CHAPTER**

- How Internet e-mail is sent and delivered
- SMTP, POP3, and IMAP protocol server features
- Message formats, parts, and encodings
- A survey of various servers and clients

This chapter discusses the various technologies required to send e-mail over the Internet. Three important IP protocols form the core of these services: the Simple Mail Transfer Protocol (SMTP), Post Office Protocol (POP3), and Internet Message Access Protocol (IMAP). Together they form a system that is used to send mail from one e-mail client to another through two intervening e-mail application servers. The mechanism for polled e-mail is described.

E-mail messages consist of a header and a body. Different fields in the header are used for addresses. The SMTP protocol is used to format e-mail messages. This application protocol adds an envelope that is used by the SMTP server for routing. The Multipurpose Internet Mail Extensions, or MIME (which is an extension to SMTP), is used to segment and format e-mail messages as well as to include rich media content. The method by which MIME encodes non-ASCII or binary data is described.

A variety of e-mail clients are described. E-mail clients can support either POP3 or IMAP and offer a range of features that make getting e-mail from an incoming mail server more convenient and more secure. Other e-mail clients exist in the form of Web mail and terminal or telnet clients.

POP3 is used by clients to get e-mail from a POP3 server where the e-mail is eventually deleted at the server and retained by the client. IMAP is used by clients for server-based e-mail, where the data is stored at the server and can be stored on the client as well. IMAP is better suited for enterprise clients and for multi-user e-mail client access.

E-mail over the Internet is a client-server technology. The servers or Mail Transfer Agents (MTAs) provide router and transport functions. Some are messaging platforms. E-mail clients are the client applications. There are a very large number of e-mail clients, but they tend to offer a common set of features.

# The Three Main Protocols

E-mail is one of the oldest computer network services that exist. It existed before the Internet was developed and was adapted for its use. On the Internet, the core mail protocols —SMTP, POP3, and IMAP — are prevalent and comprise a significant percentage of all messages travelling on the Internet.

### Note

E-mail is defined by a set of IETF standards. The format of messages is described in RFCs 822, 1123, and 2822. RFC 822 replaced RFC 733. MIME e-mail formatting, described later in this chapter, is a draft standard contained in RFCs 2045 to 2049. For SMTP, refer to RFCs 2821 and 2822. Mail routing and DNS are contained in RFC 974.

## Polled e-mail

The general sequence of sending an e-mail (see [Figure 24.1](ch24.html#a_general_e-mail_transfer_process)) is as follows:

1. The sender's e-mail client or Mail User Agent (MUA) sends the encoded message in SMTP format to the outgoing SMTP server, which is referred to as the Mail Transfer Agent (MTA) using a Mail Submission Agent (MSA).
2. The SMTP server parses the recipient e-mail address (in the SMTP header), looking for the @ symbol to obtain the domain name, and then contacts that domain's DNS server to obtain the Mail eXchange record.The DNS Server returns the MX record to the SMTP server with the location of the POP3 (or IMAP) server that is listed for the domain.
3. The SMTP message is sent by a Mail Delivery Agent (MDA) over the Internet to the POP3 (or IMAP) server.
4. The POP3 (or IMAP) server sends the encoded SMTP message to the recipient's e-mail reader or client (their MUA) where the e-mail is decoded and placed into the recipient's mailbox.When an IMAP server, such as Microsoft Exchange or Lotus Notes, sends and receives e-mails, it uses a proprietary format for the e-mail and relies on a translation from standard protocols using either a mail gateway or some other service. If mail is requested by the recipient using a Web mail service, then the MUA involved in the final transfer is the Web browser.

Mail routing and its relationship to DNS is an important part of the mechanism for polled Internet mail. Every domain name server is required to contain a Mail eXchange (MX) record that defines where mail to that domain must be sent. An MX record can point to a specific server or host, or it can use a wild card to define an MX record that points to the default of a domain. Without this information, mail would be undeliverable.

![A general e-mail transfer process](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2401.png)

**Figure 24.1. A general e-mail transfer process**

While POP3 and IMAP clients and servers use different mechanisms to transfer mail, most current e-mail servers and clients support both types of mail transfer protocols. If you open the configuration settings for an e-mail client such as Microsoft Outlook or the open source Mozilla Thunderbird client, both allow you to use either format.

The common port numbers used for these various services are shown in [Table 24.1](ch24.html#common_e-mail_port_numbers).

**Table 24.1. Common E-mail Port Numbers**

| Protocol | Purpose | Both Plain Text and Encrypted | Plain Text Only | Encrypted Only |
| --- | --- | --- | --- | --- |
| **HTTP** | Web mail |  | 80 | 443 |
| **IMAP4** | Inbound | 143 |  | 993 |
| **MSA** | outbound | 587 |  |  |
| **POP3** | inbound | 110 |  | 995 |
| **SMTP** | outbound | 25 |  | 465 (non-standard) |

## Push e-mail

Some e-mail systems are always on and provide a push service. As soon as the message arrives at the server, it is sent out to the phone without the phone having to poll the server for delivery. Push e-mail is different than e-mail clients that have a feature that checks for mail at regular periods, which is still a polling service.

Push e-mail is found in smart phones like the Research in Motion (RIM) Blackberry. Other examples include Google's new Android mobile operating system, Palm Treos, Windows Mobile (5.0 and later), the Apple iPhone, Sony Ericsson Smartphones, and others.

RIM uses a proprietary protocol; but the IDLE command of Push-IMAP and the SyncML protocols are both solutions. As long as the phone has its GPRS (roaming signal) on, the device can be located by their wireless service and the mail can be routed to their phone. Windows Mobile's push system is branded as Direct Push Technology and works with Microsoft Exchange to Pocket Outlook clients.

Push e-mail systems often employ a notification feature such as the "You've Got Mail!" alert that AOL uses. On UNIX, the `biff` program is used to send an alert to a terminal that performs the same function when mail arrives.

Another e-mail service that was developed in the 1980s and 1990s was the X.400 mail system. X.400 systems are an ITU-TS standard that is an alternative to the SMTP protocol run over TCP/IP networks according to RFC 1006. This messaging system did not achieve marketing success in the United States, but is used to some extent in Canada, and more frequently in Europe, Asia, and in South America, particularly for vendors transmitting Electronic Data Interaction, or EDI, messaging. Derivative standards exist for both the military and aviation industries. X.400's use is dwarfed by the e-mail Internet standards.

SMTP works with addresses in the form:

```
friendly.name@server.domain.ext
```

whereas an X.400 address takes the form:

```
C=no;ADMD= ;PRMD=mynetwork;O=domain;OU=server;S=Name;G=Friendly
```

# Message Parts

E-mail messages are separated into two or more parts. At a minimum, there is a header and a body, and there is always a blank line separating one from the other. Most people would refer to the message as the body, but for a mail server, the message is the entire data object, header included.

Each header is broken up into several fields, some of which are required and others that are optional. The required fields are:

- `From:` <*sender e-mail*>
- `To:` <*recipient e-mail*>
- `Subject:` <*content description*>
- `Date:` <*creation date*>

### Note

To view a list of header fields, go to `www.iana.org/assignments/message-headers/perm-headers.html`.

It is important to note that the header fields for `Reply`-`To:` and `From:` don't necessarily correspond to the sender or recipient's e-mail address. The address used for routing is obtained from the SMTP header, and unless the e-mail contains a digital signature that verifies the sender, any e-mail address can be used in the `From:` field.

Address fields can include mailing lists and aliases. A mailing list is a named object that is a delimited list of e-mail addresses, whereas an alias is a substitute name for one or more e-mail addresses. The technical difference between the two is that when an alias is applied to the envelope containing the message, it leaves the envelope intact. When the envelope sender is changed so that it is the owner of the list, this signifies that the address is a mailing list. The distinction is subtle, but important. Should the message not get to its destination, the owner is much more likely to care and act on a notification than the sender is.

Optional fields include:

- `Cc: Carbon copy to these e-mail addresses`
- `Bcc: Blind carbon copy to these e-mail addresses`
- `Reply-To: Reply to e-mail address`
- `Content-Type: Display instructions, usually in MIME`
- `In-Reply-To: The unique Message-ID that this message replies to`
- `Reference: The unique Message-ID of both the current message and the one being replied to`

A Blind Carbon Copy lists recipients who will get the e-mail, but whose names and addresses won't appear on the e-mail the recipient gets. Reply-To addresses do not have to be the same as the sender, nor must they be a single address. All of these fields can support mailing lists. MIME is described later in this chapter.

The body of a message consists of text in 7-bit ASCII. This includes all letter characters, and the "/" and "+" symbols. To use additional character sets and the upper characters of 8-bit ASCII, those additional characters must be converted into a representation in 7-bit ASCII. The process is called content encoding, or unencoding for the extraction of the original information. Several different encoding schemes are used, but the most widely used method is the one that MIME uses, called Base64. (The Base64 method is described later.) When 8-bit ASCII appears with only 7-bit ASCII characters, it is referred to as *8-bit clean*.

Many e-mail clients support not only plain text but HTML as well. HTML is plain text with embedded tags, but the formatting of HTML requires that the e-mail client have a rendering engine. The use of HTML in e-mail presents the same set of problems that HTML in browsers does; often e-mail clients render with the same browser engines your operating system uses. Links in e-mails and executable content can initiate malware or problematic actions.

# Simple Mail Transfer Protocol

The Simple Mail Transfer Protocol, or SMTP, is the protocol used to send electronic mail between servers on an IP network, including the Internet. Most e-mail clients send their mail to an SMTP server as SMTP, although they use either the Post Office Protocol (POP) or the Internet Mail Access Protocol (IMAP) to receive mail. (POP and IMAP are covered in the sections that follow.) The best-known SMTP mail servers are UNIX sendmail (which was the first one), Windows Microsoft Exchange, Lotus Notes, Novell GroupWise and NetMail, Sun Java System Messaging, Postfix, qmail, and over 40 others.

An e-mail message is sent from a client to the SMTP server in the following way:

1. The message is composed by the client and the Send button is clicked.
2. The e-mail client connects to the outgoing SMTP server stored in its configuration settings through port 25.NoteWhen an SMTP server sends mail to a relay SMTP server, the outgoing port is meant by the current standard to be set by a system administrator to port 587. An older SMTP port setting of 465 for secure SMTP is now deprecated.
3. The SMTP server parses the `sendto:` address into name and domain parts.
4. If the message is in the same domain as the sender, the message is passed to the POP3 server for delivery and the message is sent.
5. If the message is to a different domain, the SMTP server sends the message to a delivery agent.
6. The SMTP contacts a DNS server to obtain the Mail eXchange (MX) address of the SMTP server listed for the recipient's domain.
7. The outgoing SMTP server then sends the message through port 25 to the recipient's SMTP server where it is transferred into the POP3 or IMAP server.Some systems are set up with a smart host to transfer mail from the outgoing SMTP server over port 587 to an intermediate or relaying SMTP server, which then forwards it on. Any relay server that uses port 25 and forwards all traffic is referred to as an open relay server and may be blocked at their ISP. Many ISPs do not allow relay mail servers and only transfer mail on port 25.
8. The recipient's e-mail program, which is sometimes referred to as the Mail User Agent (MUA), or the intermediate SMTP server, which is sometimes called a Mail Transport Agent (MTA), sends the check mail request to initiate the mail transfer.

Not all messages can be delivered immediately, and so SMTP queues messages for a period of time and then retries periodically to resend the message. Many SMTP programs use the sendmail program as their delivery agent, and refer to the queue as a sendmail queue. The details on how long an SMTP server will try to send mail, how often it tries to resend a message in the queue, how often you are sent a message that the mail has not reached its destination, and if the mail is returned to the sender are configurable on the server.

An SMTP Envelope is the information that contains the addresses of the sender and recipient. The sender is required in case the mail is undeliverable, as it provides a means of notification. The SMTP Body is the combined header and body of the message, although the term SMTP Body is rarely used.

SMTP uses a very simple command set that is readable in the English language. Messages such as `HELO` for hello, `MAIL FROM:` for the sender's address, and so on are passed back and forth during an SMTP session. When an SMTP server responds to these commands, it does so using a set of numbers as responses. Common responses include: 220, ready; 221, closing the connection; 250, completed; 354, OK, transmit; 450, mailbox busy; 451, abort due to error; 452, aborted due to out of disk space error; 500, syntax error; 550, mailbox unavailable or does not exist; 552, aborted due to storage quota violation; and 554, transaction failed.

The Extended Simple Mail Transfer Protocol (ESMTP) is an extension of SMTP that can send multimedia files as e-mail messages. ESMTP begins when a client sends the `EHLO` or Extended HELLO command to initiate a connection, and an SMTP server would respond with an appropriate reply indicating a successful connection, a failure, or some other condition. A number of ESMTP commands support rich data transfer, including `SIZE, BDAT, CHUNKING, DSN, ETRN`, among others. ESMTP supports a pipelining feature where multiple commands can be sent at the same time.

SMTP has no built-in security mechanism. When a more secure version of SMTP is required, the SMTP-AUTH extension of the protocol can be used to force a user to log into the mail server before mail may be sent. The SMTP-AUTH extension allows a user access to the mail server, but provides no other checks on the validity or purpose of the e-mail that is sent. SMTP-AUTH can allow mail to be relayed, but requires that the relay server trust the sending SMTP server. For that reason, it is rare to find SMTP-AUTH used on the Internet.

## Multipurpose Internet Mail Extensions

SMTP manages messages in the form of text files, which POP3 and IMAP clients can download. Many messages contain additional content that isn't text; therefore, there needs to be a mechanism by which content can be included in text. The mechanism that is used by nearly everyone is the Multipurpose Internet Mail Extensions, or MIME. [Figure 24.2](ch24.html#the_message_and_mime_hierarchy) shows the message hierarchy and how MIME segments messages.

MIME formats text sent in messages using the metaphor of an envelope. In the formatting hierarchy Root represents all of the messages that are sent to anywhere by anybody. The message advertises certain Properties, namely the Domain it came from and the Content-Type that describes the Domain information. The rounded rectangles in the figure represent either information or metadata. Regular rectangles represent formatting or organizational structure. The Transport Headers contain the routing information contained in the header, fields such as From:, To:, Reply-To:, Re:, BCC:, and so forth.

The main part of the hierarchy is the MIME branch which formats the body of the message into parts. Each part contains content, a description of the content, and the MIME version used to format the part. Parts further subdivide into Subparts, with each Subpart containing the same data and metadata formatting. The Preamble and Epilogue parts can be added to explain what the different parts are for, but are an optional feature. At some point you get to the final (lowest) level part to which you can attach Data, shown as BLOB in the figure. A BLOB or Binary Large Object is a file of any size or structure that can be appended to the message. BLOB is a container object field and can contain word processor documents, picture files, PDF files, or whatever you attach to the message.

As defined by RFCs 822 and 2822, e-mail messages are plain 7-bit ASCII text. Any language that uses upper-level ASCII (8-bit) is not accommodated by the e-mail standard. If there are any files such as pictures, documents, or formatting information that might separate one part of an e-mail from another, those are also not part of the e-mail standard. MIME adds the ability to address all of these shortcomings by adding plain text commands to e-mail messages that specify these additional capabilities.

MIME is responsible for:

- **Showing non-ASCII text (symbols)**. SMTP uses the 7-bit ASCII character set. MIME extends that to the full 8-bit set that supports symbols used in other languages, such as é, á, â, æ, ç, ó, ý, and many others.
- **Specifying attachments such as pictures and documents**.
- **Separating a message into different parts**.
- **Symbols in message headers**.
- Encoding and decoding non-ASCII e-mail content.

A sample MIME header might start out looking similar to the following:

```
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Content-Description: This is my example MIME message
Content-ID: <part0090829@servername.domain>
Content-Location: http://servername.domain/filename.txt
Content-Disposition: inline
This is the body of the message.
```

![The Message and MIME hierarchy](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2402.png)

**Figure 24.2. The Message and MIME hierarchy**

### Base64 encoding

When you compose an e-mail in an e-mail client, MIME commands are added to the message which instruct the receiving e-mail client how to display the message. If your message is simple 7-bit ASCII text and nothing else, then MIME reports the content as plain text and the message is left as is. If there are attachments that accompany the message or if there is HTML content in the body portion of the message, then each part is given a MIME command that tells the client what content to expect and how to handle that part.

The encoding/decoding process deconstructs content on the sending end and restores it on the receiving end. Base64 encoding works by taking a file's data and separating it into 8-bit bytes in units 3 bytes long. These 24 sequential bits, now grouped into 3 sequential bytes, are assigned to four 6-bit characters. The 6-bit character set includes the 26 uppercase (A-Z) and 26 lowercase (a-z) ASCII letters, the 10 numbers (0-9), and the "+" and "/" symbols. The numbering sequence follows the order in the previous sentence from 0 to 63. Base64 refers to the fact that the character set is 26 or 64 characters in size. [Figure 24.3](ch24.html#encoding_can_take_non-ascii_data_and_rep) shows a representation of the encoding process.

![Encoding can take non-ASCII data and represent it in an ASCII form for e-mail transmission.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2403.png)

**Figure 24.3. Encoding can take non-ASCII data and represent it in an ASCII form for e-mail transmission.**

Let's consider an example of how this conversion works. Suppose that the three bytes are the numbers 124, 250, and 039 in that sequence. The bit stream that represents those three numbers is:

```
01111100
11111010
00100111
```

Encoding breaks this stream up into the following four 6-bit numbers:

```
011111
001111
101000
100111
```

The conversion of the four 6-bit binary number gives:

```
31
15
40
39
```

which is then translated into 7-bit ASCII as the following sequence:

```
f
P
o
n
```

Base64 encoding isn't the only method used to encode binary data in SMTP messages. Other techniques used are 7-bit and quoted-printable for normal SMTP, and 8-bit and binary when 8BITMIME is used as an SMTP extension. While Base64 is a common encoding scheme, Base32 and Base16 encoding schemes are also used. The difference between the three is that Base32 and Base16 (hexadecimal) use smaller character sets to encode the characters in messages. For hexadecimal encoding the symbols 0-9 are combined with the letters A-F (or f) to provide two character combinations such as A0, F2, and so forth.

### MIME rendering

Any MIME message announces its presence by inserting the following line in the header:

```
MIME-Version: 1.0
```

If the content is simply ASCII text and no more, then you see the following line:

```
Content-Type: text/plain
```

A type can consist of a Content-Type as well as subtypes. To indicate that there is other content, MIME specifies different parts. An attachment is indicated using the `multipart/mixed` message, and the type of attachment is indicated by a header message `Content-Disposition:` along with the filename and extension. A Content-Disposition header can indicate which program can use the enclosed content. An example might be:

```
Content-Disposition: attachment; filename="filename.jpg"
```

A `Content-Disposition` line allows the sender to embed a plain text description of the purpose of the MIME message.

MIME also applies to other Internet protocols. Many HTTP requests are accompanied by data that is described by MIME and displayed in your browser. If an e-mail client can render HTML, then the message `multipart/alternative` instructs the client to either read the `text/plain` or the `text/html` section, depending upon whether or not the client is rendering HTML. This is usually a setting that you can control in the e-mail client. Other content types are also indicated by content-type instructions, including `image/jpg, audio/mp3`, or `video/mp4`. An application document can be attached with the content-type `application/msexcel`. A complete list of MIME media types may be found on the IANA (Internet Assigned Numbers Authority) at `http://www.iana.org/assignments/media-types/`.

The method used by MIME to encode the upper ASCII character set (8-bit ASCII) is similar to what you've already seen for Base64 encoding. The upper ASCII character is transformed into a string of ASCII characters of the following format:

```
=?charset?encoding?encoded text?=
```

Any Internet Assigned Numbers Authority (IANA) character set may be used; the encoding used is Q-encoding (quoted-printable) or B-encoding (Base64), followed by the character string that is being translated. There are some minor differences between the two encodings, but they work similarly. Thus you might see a header line such as:

```
Subject: =?iso-8859-1?Q?=New Tax Tables Listed in A2?=
```

which becomes `Subject: New Tax Tables Listed in ¢`.

MIME uses what is called a `Content-ID` header to create a unique identifier for the message part of a multi-part message. An example of a `Content-ID` would be something like:

```
Content-ID: <11.3.23957.2098389882@servername.domain.ext>
```

The only requirement is that this be a unique identifier, and so convention has it that it is separated into the hostname on the right of the @ sign, and some unique number scheme. Usually a timestamp is incorporated into the left part of the `Content-ID` string. A very similar unique header called `Message-ID` is used to identify the entire message.

Uuencoding is an alternate method for encoding non-ASCII characters into ASCII characters, which was used mainly in UNIX mail programs. The name *uuencoding* comes from the term UNIX-to-UNIX encoding. This method is an alternative to MIME. `Uuencode` is the UNIX program that is responsible for the encoding operation, and `uudecode` is the program that decodes the encoded information. MIME has largely replaced uuencoding, with Base64 used as the encoding technique.

# Post Office Protocol

The Post Office Protocol, or POP, is one of the two common e-mail protocols used by client applications to retrieve mail from servers on IP networks. POP has gone through several versions, with POP3 being the most recent version. The Post Office Protocol is essentially a text file server. Messages are text that is appended to an e-mail address file.

The procedure that follows outlines a POP3 mail request:

1. A POP3 client initiates a check mail request and creates a connection to the POP3 server over port 110.
2. The POP3 server requests a name and password as authentication, which the client provides.
3. The e-mail account is given access to its message text file, and the client passes the last message received number to the server.
4. All messages numbered higher than the last received message are sent to the client, where they are appended to the end of that account's e-mail.
5. The POP3 server closes the connection and deletes the e-mail that it just sent from the account's text file on the POP3 server.

Step 5 defines a very important potential difference between the POP3 mail protocol and the IMAP protocol that is described in the next section. IMAP is server-based e-mail. When messages are sent to an IMAP client, they are retained on the server so that they may be accessed by another IMAP session at a later time or from a different location. When using a POP3 client, there is a setting in the client software that allows you to either delete all delivered mail from the server, or leave it on the server. Most people use the default setting of deleting the e-mail after it is received.

When a POP3 client elects to leave the mail on the server, it needs to be able to recognize new messages when it next connects. Should another POP3 client come along and download messages and then have the POP3 server delete them, the numbers attached to the messages that come in afterwards will no longer match what the original POP3 client expects. To solve this problem, POP3 uses a 32-bit Unique IDentification Listing (UIDL) number to identify messages. When the original POP3 client views the UIDL for a message, it can now map those messages to the current message ID. IMAP clients use a similar system, but their UIDLs are assigned as sequential numbers so that the IMAP client can retrieve the next number in the sequence.

POP3 servers use a very simple command and retrieval language. It isn't necessary to use a POP3 client to retrieve e-mail. If you have a telnet client, you can connect to the POP3 server over port 110 and send the POP3 server the session commands required to retrieve your mail. After login and sending the RETR command, the POP3 server sends your messages to the telnet client for you to read.

POP3 allows clients to log into a POP3 server using plain text or unencrypted text. A variety of authentication methods are added to POP3 to protect user logins. The most common method is called Authenticated POP (APOP), which employs an MD5 hash function to encrypt login. Many POP3 clients support APOP.

## Web mail clients

Web mail is a Web client that runs inside a browser. A number of e-mail clients offer a browser version, most prominently Microsoft Outlook Web Access. A variety of Web mail services exist, many of which are Internet based; they include Hotmail (now owned by Microsoft), AOL mail, Yahoo! Mail, and Gmail (Google), among others.

Web mail providers run the mail servers that store and send a user's mail and to which any browser can connect. The client software is embedded on the server and can provide nearly all of the functions that a stand-alone client application can; and the browser renders the user interface (UI) on the client. Google's Gmail uses an interface developed in JavaScript. Many of these services are free to use at some basic level, which is usually tied to the amount of storage that they allow on their servers. When you pay for the service, your storage is increased.

The success of Web mail has led enterprise mail servers to offer this capability. There are also several open source Web client applications that you can use to connect to mail servers. Most Web mail clients are written to access either IMAP or SMTP servers. However, there are a number of Web mail clients that can connect to both POP3 and IMAP servers.

Perhaps the best-known example of one of these Web mail sites is `Mail2Web.com`, which is owned by SoftCom Technology Consulting Inc., in Toronto. Mail2Web's service offers many of the features of a pure e-mail client within a browser. With Mail2Web, you only need to specify the e-mail account and login, and the service connects and retrieves your mail; you don't need a Mail2Web account to use the free service.

# Internet Message Access Protocol

The Internet Message Access Protocol, or IMAP, is a server-based mail program. Unlike POP3, which was described in the previous section, IMAP creates an e-mail data store on the server that you can access from an IMAP client. Microsoft Exchange and the Outlook client are the classic examples of an IMAP server and client. IMAP has some very powerful advantages over POP3, particularly for business applications. With IMAP there is a permanent record of e-mail, and your e-mail can follow you anywhere you can connect to it.

IMAP supports both online or connected sessions, and offline or disconnected sessions. To provide for situations where a system is disconnected from an IP network, most IMAP clients store their e-mail locally and synchronize the data when they connect to the IMAP server. Any changes you make locally are sent to the server the next time you connect, and any changes on the server that you might have made from another IMAP client are sent from the server to your current IMAP client.

If you have a desktop and a laptop, IMAP provides a way to have e-mail appear on both systems and an automated mechanism by which you can synchronize your work. You can synchronize POP3 e-mail between systems, but this is done manually and isn't part of the POP3 system, which makes synchronizing harder and more subject to errors.

IMAP uses a system of simple messages, just like SMTP and POP3 do, and communicates them over port 143.

# Mail Servers

A mail server or Mail Transfer Agent (MTA) is an application server dedicated to mail transport. Sometimes these systems are referred to as a mail router or mail transport agent, and very infrequently as an Internet mailer, but they mean the same thing as the commonly used MTA. There are a large number of different MTAs deployed throughout the world, and because they usually don't respond to automated queries to identify themselves, the market share of the servers is a little unclear. Some studies seem to indicate that the largest number of MTAs are shared by Microsoft Exchange on the Windows platform, and sendmail, qmail, and Exim on the Linux and UNIX platforms. Other studies indicate a much broader distribution among many more products.

Mail servers are not simply a transport application, although some are configured that way. Most mail servers manage message stores, which is a rich data object database containing messages and all of the other content that is carried along with modern e-mail. The messaging portion of the application can be very feature rich and include filtering, smart routing, identity management, security, and many other features. A key feature is the establishment of user accounts and the maintenance of mailboxes. In some systems, a mailbox can be a single file, and in others, it can be a directory of files where incoming messages are stored.

Products like Microsoft Exchange and IBM Lotus Domino are servers backed by the enterprise-class databases SQL Server and DB2, respectively. Domino was originally developed as the Lotus Notes message server, integrated into a groupware collaboration platform, and can function as an application server and/or a Web server. Microsoft Exchange was developed as a messaging platform to which collaboration was added. The most popular mail server in use is sendmail, which is an open source program that replaced an older program called delivermail. Estimates are that around 30 percent of all mail servers run sendmail.

Sendmail is configurable from the command line. One way to expose sendmail is to use the Web-based GUI called Webmin, shown in [Figure 24.4](ch24.html#sendmail_configuration_exposed_in_the_br). Webmin (`www.webmin.com`) is open source software that can expose operating system services for OpenSolaris, Linux, and other flavors of UNIX. Sendmail is only one of the applications that it works with. Others include the Apache HTTP Server, MySQL, and PHP. Each of the Webmin modules loads the appropriate configuration file, essentially creating a plug-in architecture.

![Sendmail configuration exposed in the browser GUI managed by Webmin](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2404.png)

**Figure 24.4. Sendmail configuration exposed in the browser GUI managed by Webmin**

# Setting Up a Mail Client

An e-mail client or Mail User Agent (MUA) is a program that can compose and send messages as well as retrieve and display them. In a client-server architecture, the e-mail client is the client portion and the mail server is the server portion. Other programs that can perform these functions are also referred to as e-mail programs, whether they run inside a browser such as Web mail or at a command prompt inside a telnet session.

Mail clients do not run as a service unless they are automatically started as a system preference. Most mail clients are configurable as either an SMTP/POP3 or IMAP client. This allows clients to download e-mail from nearly all of the Internet mail servers. Some e-mail clients such as Eudora have been largely single user, while others such as Microsoft Outlook are designed to be multiuser. The organizational structure of mailboxes is separated by accounts. So while Outlook uses a single mailbox file (PST), Eudora separates mailboxes (MBX) into different files.

To set up a mail client, you need to provide the following pieces of information:

- The account if you are using a multi-account client
- A display name or "real name"
- A valid e-mail address
- The incoming server address, either a POP3 or IMAP server
- The username used to log into the server
- The outgoing SMTP server

A typical settings dialog box is shown in [Figure 24.5](ch24.html#e-mail_client_settings), taken from Eudora 2.6. Eudora 2.7 was Qualcomm's last commercial version. Eudora is in the process of being converted to an open source client that will be called Penelope, and will adopt some of the features of perhaps the best-known open source e-mail client, Mozilla's Thunderbird.

Microsoft's mail clients include Outlook Express (XP and before), Outlook (all versions), and Windows Mail (Vista). These products place a user into setup with a wizard in which you create the e-mail account before entering the settings. Windows Mail supports not only POP3 and IMAP but also HTML servers.

### Note

For an extensive list of e-mail clients, their current versions, protocol support, and features, go to `http://en.wikipedia.org/wiki/Comparison_of_e-mail_clients`.

A list of the best-known e-mail clients would include the following programs: @mail, Eudora, Gnus, Novell GroupWise, IBM Lotus Notes, Kerio WebMail, Apple Mail, Microsoft Entourage (for the Macintosh), Microsoft Office Outlook, Outlook Express, Pine, Mozilla Mail & Newsgroups, Mozilla Thunderbird, Netscape Messenger, Novell Evolution, Opera Mail, SeaMonkey Mail & Newsgroups, and Squirrelmail.

![E-mail client settings](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2405.png)

**Figure 24.5. E-mail client settings**

Some of the more valuable features that you can find in e-mail clients include the following:

- **Encrypted database**. This secures the database file from inspection by outside parties.
- **Indexed searches**. An e-mail client that indexes the content in its database allows for very fast searches. Some of these programs index an IMAP data store as well as a local database.
- **HTML e-mail rendering**. This feature makes an e-mail look like a browser page. The same risks apply to working with embedded content in this type of display that exist for a browser page.
- **Image blocking**. This is the ability to display a placeholder in place of the downloaded image file. This is valuable for reducing load time and can help reduce unintended click-throughs.
- **Junk mail filtering**. Filtering in general is quite valuable. This redirects e-mail by criteria that you select to be placed into the mailbox of your choice. The junk e-mail filter is a proactive mechanism that evaluates mail based on a set of criteria and places the mail into the Junk folder. The best junk filters use a Bayesian filter that learns what you consider junk and adds similar e-mails to the junk list. Eudora's filtering mechanism is shown in [Figure 24.6](ch24.html#eudora_apostrophy_s_filter_creation_dial).
- **Phishing blocker**. This tool prevents sites from displaying links that take users to sites where their information is hijacked. Usually phishing filters work off of blacklists.
- **Message templates**. Templates are documents that you can use as models for your e-mails.![Eudora's filter creation dialog box](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2406.png)**Figure 24.6. Eudora's filter creation dialog box**
- **Encryption**. Many e-mail clients support encryption inline or through open standards such as Pretty Good Privacy (PGP) or OpenPGP or through the use of Secure MIME (S/MIME).
- **Scripting**. The ability to program actions in VBScript, JavaScript, Python, Java, PHP scripts, and others allows advanced users to add additional automation to the e-mail client. Automatic automation can do things such as add a signature, perform a search and replace, modify an address list, and so forth.

# Summary

Internet e-mail is one of the most important network services that the IP protocol offers to users. It relies on three important protocols that were described in this chapter: the Simple Mail Transfer Protocol, Post Office Protocol, and Internet Message Access Protocol. The method that is used to send mail from one e-mail client to another through these services was described.

E-mail messages have a specific form and are formatted using MIME when sent using SMTP. This chapter examined how MIME works, and how data is encoded for transfer.

A variety of e-mail servers and clients were examined and surveyed.

In the next chapter, I describe the use of streaming media, sound, video, and other rich media. Streaming services allow for real-time transfer of data that requires large file sizes. The special techniques used for these services are explored.
