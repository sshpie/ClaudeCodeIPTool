# Chapter 12. Electronic mail (E-mail) Security

**IN THIS CHAPTER**

- **Overall security issues and concerns with e-mail**
- **E-mail risks**
- **E-mail protocols**
- **E-mail authentication**
- **Operating safely when using e-mail**

Along with Web browsing, e-mail has made the Internet popular, widespread, and indispensable for most users. Despite its critical role in the typical Internet user's life, e-mail is comparatively insecure. Many people rely on e-mail and use it as an integral part of their job. However, most users forget that the content and the sender are not authenticated or validated, so it can easily be spoofed. This is one of the reasons that phishing attacks are so prevalent and successful.

# The E-mail Risk

E-mail is widely used and has a well-defined and universally implemented protocol, which is SMTP (simple mail transfer protocol). Therefore, it is a prime target for hackers developing attacks. Attacks on e-mail focus on two areas: the delivery and execution of malicious code (malcode) and the disclosure of sensitive information. The latter gets little publicity because it is easily done and does not require a sophisticated attack.

The two main attack vectors that are used are:

- **Auto-processing**—Many mail clients automatically open and preview content when it is received, even if the user is not at the system. Therefore, a carefully crafted attack could automatically run on a system with no action required from the user.
- **Social engineering**—Many e-mail attacks are meant to manipulate a person into clicking on a link or opening an attachment that looks legitimate (phishing attacks), allowing an attacker to run malicious content on a system.

## Data vulnerabilities

E-mail has great potential risk due to the very sensitive nature of the data or information that is transmitted and the false assumption people make that it is secure by default. E-mail can reveal a huge amount of company and personally sensitive data. For example, consider only a few common items in e-mail traffic:

- **Whom you correspond with**—Can be used in expanded attacks.
- **What you think about other people**—Few people would want their personal opinions made public.
- **Business strategies**—How to win a contact.
- **Informal policies**—Many a whistle-blower has used e-mail to establish the existence of a company policy that was not written down or recorded in any place other than e-mail.
- **Who are allies or enemies**—People tend to be brutally honest in e-mails, more so than in a memo or other written policy.
- **Who is being deceived and misled**—Persons tend to set the record straight in e-mail. Explanations of ambiguous policies are clearly explained.

## Simple e-mail vs. collaboration

The security risks associated with e-mail are often confused with the risks associated with collaboration tools that also serve as e-mail clients. Microsoft Outlook is one such tool. In the Outlook E-Mail Security Update, Microsoft states the following:

> *In addition to providing industry-leading e-mail and group scheduling—the most popular collaboration applications today—the Microsoft® Outlook® messaging and collaboration client allows users to connect to, communicate with, and collaborate with other users*.

Microsoft Outlook is definitely a collaboration tool, not merely an e-mail client. Some of the many features and functions within the application are as follows:

- **E-mail folders**—The e-mail capability in Outlook
- **Contacts**—A personal database of people and their related information
- **Calendar**—A database storing appointments and meetings
- **Journal**—A simple editor with text storage
- **Notes**—A simple editor with text storage
- **Tasks**—A simple database of short text with date, priority, and so on
- **Net, Public, and Personal folders**—File-sharing capability
- **Newsgroups**—Access to public postings to news groups

If Outlook were marketed as a collaboration tool, as opposed to an e-mail client, the public would be more wary of the security that is built into the application. However, when the masses think of Outlook only as an e-mail client, it avoids the security scrutiny that would accompany a collaboration tool. E-mail is more inherently secure than collaboration. Plus this illustrates a common problem, where many of the tools we utilize today have extra capabilities that the end users are not aware of but that the attacker uses to exploit a system.

The following are two issues to consider when comparing e-mail and collaboration tools:

- The acquisition and propagation of malcode
- The loss of privacy data

### Attacks involving malcode

E-mail, as defined by the Network Working Group's RFCs, is implemented in simple ASCII text. ASCII text cannot be executed directly. This can be a serious impairment for malcode, which needs to be executed, be propagated, or do damage. Therefore, e-mail at its very basic core is safe because it does not transmit directly executable (binary) code.

The following is some sample plain text script that might be embedded in an e-mail message:

```
/**
 *  Browser specific detection
 *  and printing of Style Sheets
*/
bName = navigator.appName;
bVer = parseInt(navigator.appVersion);
if (bName == "Netscape" && bVer >=3) {
   window.location=error;
} else if (bName == "Netscape" && bVer >=1) {
   window.location=error;
}

function isUnix() {
    var Unixes = new Array("SunOS", "HP", "Linux");
    var $flag = false;
    for (var i=0; i < Unixes.length; i++) {
        if (navigator.appVersion.indexOf(Unixes[i]) != −1) {
            $flag = true;
            break;
        }
    }
    return $flag;
}
```

This text, when transmitted in e-mail, does not in itself cause any execution to take place. To the network, this script is just an ASCII e-mail. The mere fact that the words put together make a script does not inherently make it dangerous. A user would not expect that simply putting the word *shutdown* in the middle of an e-mail message would actually shut down a device that handles the e-mail as it is transmitted across the country.

Malcode can (and usually does) spend part of its life in ASCII form. When in this form, the malcode will either be a plain text script or an encoded block. The following shows an e-mail received with an encoded binary embedded as an attachment:

```
Subject: access
From: tmp@atrc.sytexinc.com>
To: Jim - ATRC <example@atrc.sytexinc.com>
Content-Type: multipart/mixed; boundary="=-Hn2QCdYjnPZf/KrrgRe0"
Mime-Version: 1.0

--=-Hn2QCdYjnPZf/KrrgRe0
Content-Type: text/plain
Content-Transfer-Encoding: 8bit

This is a binary file 'access'....

--=-Hn2QCdYjnPZf/KrrgRe0
Content-Disposition: attachment; filename=access
Content-Type: application/x-executable-binary; name=access
Content-Transfer-Encoding: base64

f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAkIMECDQAAAAYCwAAAAAAADQAIAAGACgAGAAXAAYAAAA0
AAAANIAECDSABAjAAAAAwAAAAAUAAAAEAAAAAwAAAPQAAAD0gAQI9IAECBMAAAATAAAABAAAAAEA
AAABAAAAAAAAAACABAgAgAQIUAkAAFAJAAAFAAAAABAAAAEAAABQCQAAUJkECFCZBAgQAQAAHAEA
     <similar lines deleted>
AwAAADSaBAg0CgAABAAAAAAAAAAAAAAABAAAAAAAAACrAAAAAQAAAAMAAAA4mgQIOAoAACgAAAAA
AAAAAAAAAAQAAAAEAAAAsAAAAAgAAAADAAAAYJoECGAKAAAMAAAAAAAAAAAAAAAEAAAAAAAAAAEA
AAADAAAAAAAAAAAAAABgCgAAtQAAAAAAAAAAAAAAAQAAAAAAAAA=

--=-Hn2QCdYjnPZf/KrrgRe0--
```

In this e-mail, the binary file "access" is encoded with a common method used for e-mail—base64. This encoding converts the 8-bit binary to the seven bits used in ASCII text (in the very early days of networking, some devices could only handle 7-bit data). Base64 encoding does this conversion by taking triplets of 8-bit octets and encoding them as groups of four characters, each representing 6 bits of the source 24 bits, as shown in [Figure 12-1](ch12.html#base64_encoding_converts_24_bits_of_bina).

If left in the base64 encoded form, the malcode is harmless. For the plain text version of the malcode (worms, viruses, and so on) to be executed, it requires a Web browser or collaboration tool. To do its damage, the malcode must be decoded and launched.

When an e-mail client starts adding features to be more of a collaboration tool, such as Outlook, the malcode has many avenues of being decoded and launched. The goal of these tools is to make life easy and convenient for the users. This ease and convenience leads to the tools providing features for the user that the malcode can use to its advantage. Some examples of such features follow:

- **The automatic population of databases**—E-mail messages may be parsed for special data that needs to be populated into a database. An example of this is when users sign their e-mail with their contact information. This information can be autopopulated to a recipient's contact list.
- **Other applications are automatically launched**—The e-mail may contain a document such as a spreadsheet. When the e-mail is parsed, the collaboration tool may launch the spreadsheet application and load the document. This is dangerous if the document contains macros or other scripted code.

![Base64 encoding converts 24 bits of binary data to 32 bits of ASCII data.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1201.png)

**Figure 12.1. Base64 encoding converts 24 bits of binary data to 32 bits of ASCII data.**

By some measures, collaboration tools such as Outlook are a huge success. They enjoy a big market share of the e-mail clients in use. But users should be aware that the more features and convenience the application offers, the more of a security risk it is likely to be.

As an ongoing security theme, the more features and functionality added to programs, the more attackers are likely to use these features and malicious code. If the feature is turned off, there's no impact to the user because the malicious code is prevented from causing harm.

A perfect example of this is HTML-embedded content. Allowing HTML-embedded content within e-mail is one of the top reasons that many malicious attacks are able to exploit e-mail. But turning off this feature has minimal impact on users and completely stops an attacker.

As you install and configure your mail clients, keep in mind that simplicity is best. In many cases, turning off executable content and HTML encoding stops many of the malicious attacks such as phishing and cross-site scripting.

### Privacy data

The basic protocols used in e-mail may not be inherently vulnerable to malicious code such as worms and viruses, but the same cannot be said for protecting personal and sensitive data. For many years, the popular e-mail protocol, Post Office Protocol (POP), was used in the clear (not encrypted). Even in today's security-conscious society, most e-mail is still transmitted in the clear.

[Figure 12-2](ch12.html#a_captured_ip_packet_clearly_shows_e-mai) shows a captured IP packet from a simple Simple Mail Transfer Protocol (SMTP) session. The text of the e-mail can be clearly seen in the raw packet.

![A captured IP packet clearly shows e-mail text.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1202.png)

**Figure 12.2. A captured IP packet clearly shows e-mail text.**

When the message in [Figure 12-2](ch12.html#a_captured_ip_packet_clearly_shows_e-mai) is sent, it can be spread over several packets. The received e-mail, with all the headers, is shown as follows:

```
Return-path: <tmp@the-isp.tmp>
Received: from dedicated199-bos.wh.sprintip.net ([10.228.166.89]) by
        cluster02-bos.wh.sprintip.net (iPlanet Messaging Server 5.2 HotFix 1.21
        (built Sep  8 2003)) with ESMTP id
        <0I1X008AF926WC@cluster02-bos.wh.sprintip.net> for
        tmp@the-isp.tmp; Wed, 04 Aug 2004 12:22:54 +0000 (GMT)
Received: from compaq ([12.28.183.11]) by boded0199snunx.wh.sprintip.net
        (iPlanet Messaging Server 5.2 HotFix 1.25 (built Mar  3 2004))
with SMTP id
        <0I1X001FI8Y93G@boded0199snunx.wh.sprintip.net> for
        tmp@the-isp.tmp; Wed, 04 Aug 2004 12:22:54 +0000 (GMT)
Date: Wed, 04 Aug 2004 12:21:55 +0000 (GMT)
Date-warning: Date header was inserted by boded0199snunx.wh.sprintip.net
From: tmp@the-isp.tmp
Subject: Send me money!
Message-id: <0I1X001GF8Z03G@boded0199snunx.wh.sprintip.net>
Content-transfer-encoding: 7BIT
Original-recipient:
        rfc822;@cluster02-bos.wh.sprintip.net:tmp@the-isp.tmp
```

```
X-Evolution-Source: pop://tmp@pop.the-isp.tmp
Mime-Version: 1.0

Hi,

Mom, please wire me $1000 to my bank account # 4567-9832.
My passcode is S0nnyB0y.

Love,  Your Son
```

When the mail was received, it was transmitted with the POP3 protocol. In this case, the entire e-mail fit into one packet. A portion of that packet follows:

```
0000  00 06 5b ec f8 35 00 0a  f4 5f 20 b6 08 00 45 00   ..[..5.. ._ ...E.
0010  04 89 77 0c 40 00 30 06  e1 9e 3f a7 72 11 c0 a8   ..w.@.0. ..?.r...
0020  7b 63 00 6e 80 02 11 05  74 d0 0c 8d 43 3e 80 18   {c.n.... t...C>..
    <similar lines deleted>
0420  0a 0d 0a 48 69 2c 0d 0a  0d 0a 4d 6f 6d 2c 20 70   ...Hi,.. ..Mom, p
0430  6c 65 61 73 65 20 77 69  72 65 20 6d 65 20 24 31   lease wi re me $1
0440  30 30 30 20 74 6f 20 6d  79 20 62 61 6e 6b 20 61   000 to m y bank a
0450  63 63 6f 75 6e 74 20 23  20 34 35 36 37 2d 39 38   ccount #  4567-98
0460  33 32 2e 20 20 4d 79 20  70 61 73 73 63 6f 64 65   32.  My  passcode
0470  20 69 73 20 53 30 6e 6e  79 42 30 79 2e 0d 0a 0d    is S0nn yB0y....
0480  0a 4c 6f 76 65 2c 20 20  59 6f 75 72 20 53 6f 6e   .Love,   Your Son
0490  0d 0a 0d 0a 2e 0d 0a                               .......
```

Because e-mail is transmitted in ASCII text, the words typed into an e-mail message are easily viewed and read, even at the IP packet level. In the preceding sample packet, the text "My passcode is S0nnyB0y" can clearly be read.

Processing IP packets is a core capability of any device on the network. Capturing and viewing the packets is easily done on a networked workstation; root or administrator access is required, but this is generally not much of a deterrent to a motivated attacker. Because of the way that Ethernet works, if a network interface card (NIC) on a workstation is put into promiscuous mode by the administrator, that workstation will be able to capture every packet on a hubbed network. The problem is slightly more difficult on a switched network, but easily available tools such as ettercap allow attackers to get any packets they need.

This opportunity to capture packets and read e-mail is not limited to a user's immediate network. The risk of packets being captured can occur anywhere in the transmission between the sender and the e-mail recipient. Most users would be surprised to discover the many connections, jumps, or hops that their e-mail must take to get to the final location. The following is a list of hops to get from the author's home to his work site, which is only a 10-minute commute (5 miles) away. The command used is `traceroute`, which reports every router or gateway that must be traversed to reach the destination:

```
# traceroute work
traceroute to work 112.128.1.8, 30 hops max, 38 byte packets
 1  68.38.76.1     89.721ms  19.895ms   19.704 ms
 2  68.100.0.1     47.083ms  21.924ms   16.975 ms
```

```
3  68.100.0.145   50.535ms  103.814ms  222.326 ms
 4  68.1.1.6       53.085ms  23.345ms   17.810 ms
 5  68.1.0.30      59.535ms  130.003ms  192.466 ms
 6  112.124.23.77  61.336ms  32.410ms   27.684 ms
 7  112.123.9.62   53.214ms  26.873ms   25.215 ms
 8  112.123.14.41  36.065ms  55.200ms   202.197 ms
 9  112.118.13.58  59.731ms  30.929ms   32.333 ms
10  112.128.1.8    59.731ms  30.929ms   32.333 ms
```

So how much of a risk is it to send this information over these 10 hops? If each network has an on-duty administrator (3 shifts), a supervisor (3 shifts), and a help desk of 3 people (3 shifts), that is 150 persons with access to the packets transversing this route. If people who have the technical capability to plug in a laptop on any of these segments and sniff the line are included, the risk probably increases to thousands or tens of thousands. Among tens of thousands of people, it is not unlikely to find someone willing to read unauthorized e-mail. [Figure 12-3](ch12.html#many_network_devices_and_people_have_acc) illustrates this route and the many network devices that may capture or read the e-mail IP packets.

![Many network devices and people have access to e-mail traffic.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1203.png)

**Figure 12.3. Many network devices and people have access to e-mail traffic.**

Few users consider how many people might read their e-mail before composing a personal message. Aside from the occasional postcard, would you send a letter in the postal mail without an envelope for privacy? Let's hope our postcards don't read as the one shown in [Figure 12-4](ch12.html#would_you_put_your_e-mail_on_a_postcard).

![Would you put your e-mail on a postcard?](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1204.png)

**Figure 12.4. Would you put your e-mail on a postcard?**

### Data integrity

As previously mentioned, the text put into an e-mail message is easily seen and read at the IP packet level. The packet can be read with readily available network administrator tools. It is only slightly more difficult to modify the text in the e-mail by modifying the packets. Some typical information contained in an e-mail message that may be altered is as follows:

- **Addressees**—The attacker can change or resend the e-mail to a different addressee. E-mail is often confidential and only intended for those listed on the To: line. It is easy to see that changing addressees can create havoc.
- **Financial amounts**—If the e-mail directs the handling of funds, the dollar amounts could easily be altered. For example, the unsuspecting sender of the e-mail may be authorizing a stockbroker to purchase stock at $10 per share, but the altered e-mail may read $50 per share.
- **Object of financial transactions**—Not only could attackers change the dollar amount of a transaction, but they could also make themselves the object of the money transfer. Consider an e-mail that instructs an agent to transfer $100 to Bob's account with the account number provided. Attackers could substitute their own names and account numbers.

The capturing and modifying of e-mail can be done either as a man-in-the-middle attack or as a replay attack. Both of these attacks permit the altering of critical data that can be costly and disruptive for the user. In addition, it is important to remember that there is no built-in authentication for e-mails, so the From address can easily be spoofed. Before you click on an attachment or read an e-mail, ask yourself: "How do I know the From address is really that person?"

#### E-mail man-in-the-middle attacks

In a typical man-in-the-middle attack, the attacker must have control of one of the many firewalls, routers, or gateways through which the e-mail traverses. You saw earlier that a simple e-mail from home to work can traverse 10 or more of these gateways. Other man-in-the-middle attacks do not require control of the gateway; rather, the attacker merely needs to reside on the same local area network (LAN) segment as the user sending or receiving the e-mail or compromise a host on a network. In this case, the attacker can use an Address Resolution Protocol (ARP) spoofing tool, such as ettercap, to intercept and potentially modify all e-mail packets going to and from the mail server or gateway. In an ARP spoof attack, the attacker gets between any two hosts in the e-mail transmission path. There are four possible locations to attack:

- **Between the e-mail client and server**—This situation assumes that the client and server are on the same LAN segment.
- **Between the e-mail client and the gateway**—The gateway must be in the path to the mail server.
- **Between two gateways**—The gateways must be in the path between the client and the server.
- **Between the gateway and the mail server**—This option assumes the client and the server are not on the same LAN segment and therefore the e-mail traffic must reach the server via a gateway.

[Figure 12-5](ch12.html#an_arp_spoofing_man-in-the-middle_attack) illustrates the network configuration for the ARP spoofing attack.

In the ARP spoofing man-in-the-middle attack, the e-mail's IP packets are intercepted on their way to or from the mail server. The packets are then read and possibly modified. As discussed earlier, reading the e-mail text in an IP packet is trivial — assuming the e-mail is not encrypted. The attacker has some minor limitations when modifying the packets. For example, the total length of the packet cannot grow to a size larger than the maximum allowable for transmission on the network. This is usually about 1500 bytes. This may require the attacker to be clever when modifying the e-mail text so that the meaning changes, but the length does not.

Man-in-the-middle attacks are best avoided by using encryption and digital signing of messages. If the encryption is sufficiently strong, the attacker will not be able to decrypt and alter the e-mail. Digital signatures ensure the integrity of the body of the e-mail message. To accomplish this, the e-mail message is passed through a one-way hashing algorithm. The resulting hash is encrypted with the sender's private key added to the bottom of the e-mail message. The recipient is able to decrypt the hash with the sender's public key and verify the e-mail to have been unaltered. An attacker could not alter the message or the hash (digital signature) without being detected. [Figure 12-6](ch12.html#attaching_a_digital_signature_to_an_e-ma) illustrates how a digital signature is created and attached to the e-mail.

#### E-mail replay attack

An e-mail replay attack occurs when an e-mail packet (or set of packets) is captured, the e-mail message extracted, and the message put back on the network at a later time (replayed). This causes a second, identical e-mail to be received. The danger or damage occurs when the second e-mail is accepted as legitimate and causes unforeseen consequences.

![An ARP spoofing man-in-the-middle attack](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1205.png)

**Figure 12.5. An ARP spoofing man-in-the-middle attack**

![Attaching a digital signature to an e-mail](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1206.png)

**Figure 12.6. Attaching a digital signature to an e-mail**

Replay may be used if an attacker discovers a business that sends financial transactions over e-mail. The attacker then arranges for a nominal transaction (perhaps a $100 refund). The attacker captures the e-mail authorizing the refund and replays it several times causing several refunds to occur.

In the case of a replay attack, shown in [Figure 12-7](ch12.html#replay_attack-028), the attacker does not have to use the gateway or ARP spoofing. The attacker merely needs to be on one of the many segments that the e-mail packets transverse on their way to or from the mail server.

### The bottom line

This chapter examines some ways to make e-mail more secure (preferred protocols), some ways to safeguard the transmitted data (encryption), and some ways to improve authentication. But, in the end, if a user allows a collaboration tool to do things such as launch executables, run scripts or macros, modify databases or files, change systems or register settings, and e-mail other users, these other security measures will be very limited in their success.

![Replay attack](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1207.png)

**Figure 12.7. Replay attack**

## Spam

Spam is the unwanted receiving of e-mail. Spam has become a serious problem in today's networking environment. It is a major irritant and consumer of resources. It has been estimated that for some of the large e-mail providers, over half of the e-mail they service is spam. In gross terms, this means that these providers could get by with half of the resources needed to handle their customers' e-mail. From a security perspective, spam is a potential denial-of-services (DoS) problem.

Spammers make money by getting their advertising message out to thousands or millions of people. Very few will respond positively to the message, but even a very small percentage of responses will produce enough activity to make the spamming profitable. Spamming is profitable because it is very cheap to send an e-mail, so it requires only one positive response to cover the cost.

Spammers put their advertising message into the body of the e-mail and view e-mail headers as a necessary encumbrance needed to get the body delivered. Spammers view e-mail headers as a possible Achilles heel that can hurt them. If users and Internet service providers are able to trace the spam back to the source, the spammers could be tied up in legal proceedings or other methods of limiting them. This severely increases the cost of sending out the e-mails and reduces the profit margin to the point that the spammer may not be able to continue to operate.

Spammers take steps to hide their originating (From:) address. This is easily done if spammers run their own e-mail servers. For example, sendmail configuration files can be modified to put in a particular originating address. This address may be either fake (such as yourfriend.spam) or a legitimate address that is not owned by the spammer.

### Spam DoS

Spam DoS attacks are a result of spammers using false domains in the e-mails they send. If a spammer does not use a valid domain, the spam can be blocked by testing that the e-mail was sent from a legitimate domain. In this case, a domain is legitimate if it returns a value when a Domain Name Server (DNS) lookup is done. The following `dig` command does a DNS lookup of an e-mail coming from [bob@sytexinc.com:](mailto:bob@sytexinc.com:)

```
; <<>> DiG 9.2.1 <<>> @198.6.1.2 sytexinc.com
;; global options:  printcmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 44457
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 4,
ADDITIONAL: 4

;; QUESTION SECTION:
;sytexinc.com.                  IN      A

;; ANSWER SECTION:
sytexinc.com.           604800  IN      A       64.124.137.66

;; AUTHORITY SECTION:
sytexinc.com.           84575   IN      NS      ns1.i-n-s.com.
sytexinc.com.           84575   IN      NS      ns2.i-n-s.com.
sytexinc.com.           84575   IN      NS      ns3.i-n-s.com.
sytexinc.com.           84575   IN      NS      ns4.sytexinc.com.

;; ADDITIONAL SECTION:
ns1.i-n-s.com.          84575   IN      A       146.145.146.18
ns2.i-n-s.com.          84575   IN      A       146.145.6.85
ns3.i-n-s.com.          84575   IN      A       146.145.146.19
ns4.sytexinc.com.       84575   IN      A       64.124.137.67

;; Query time: 1263 msec
;; SERVER: 198.6.1.2#53(198.6.1.2)
;; WHEN: Wed Aug 18 15:15:32 2003
;; MSG SIZE  rcvd: 200
```

The most prevalent DoS attack that occurs due to spam is when a spammer forges an address on thousands or millions of mail messages. The result is tens of thousands of bounces, complaints, and a few responses. This results in a flood of e-mail traffic to the forged address, essentially shutting down the address for legitimate use.

Another DoS situation occurs when the spammer forges a valid e-mail address and this address then gets blacklisted. When this occurs, the user of the valid e-mail can experience obstacles to sending legitimate e-mail to users whose Internet service provider uses blacklists.

### Blacklisting

A *blacklist* is a database of known Internet addresses (by domain names or IP addresses) used by spammers. Often, Internet service providers and bandwidth providers subscribe to these blacklist databases to filter out spam sent across their network or to their subscribers.

Lists of IP addresses to be added to the blacklist are collected in different ways, including the following:

- The e-mail user community (all of us) sends samples of spam to the blacklist site. The site parses out the offending originating e-mail IP addresses and adds them to the blacklist.
- The blacklist provider runs its own mail server and fake e-mail user. Any e-mail received is automatically unsolicited and therefore spam.
- Blacklist providers exchange lists.

Some blacklists are implemented by placing offending IP addresses in a nameserver database. When a spammer's e-mail arrives, a DNS lookup is conducted to verify that the sender's e-mail address is legitimate. However, blacklisted addresses return invalid responses so the server rejects the e-mail.

### Spam filters

Spam filters attempt to identify spam from the content of the message body and not the message headers. If spam filtering can be done, it will strike at the heart of the problem and hit spammers in an area that they may not be able to circumvent. Spammers may be unwilling to change the content of an e-mail, which is in essence their advertisement message. If spammers are not able to present the advertisement, they may as well not send the e-mail at all.

**Defining Bayesian Logic**

According to Bayesian logic, the only way to quantify a situation with an uncertain outcome is through determining its probability. Bayes' Theorem is used to quantify uncertainty based on probability theory. The Bayes' Theorem defines a rule for refining a hypothesis by factoring in additional evidence and background information. This leads to a number that is the degree of probability that the hypothesis is true.

For example, suppose that you have a bag that contains three marbles, each of which may be blue or red. In a blind test, you reach in and pull out a red ball. You return the ball to the basket and try again and again, pulling out a red ball each time. Once more you return the ball to the basket and pull a ball out, red again. You form a hypothesis that all the balls are, in fact, red. Bayes' Theorem can be used to calculate the probability (p) that all the balls are red (an event labeled as A) given (symbolized as |) that all the selections have been red (an event labeled as B):

> p(A|B) = p{A + B}/p{B}

The possible combinations are RRR, RRB, RBB, and BBB. The possible outcomes are RRR, RRB, RBR, RBB, BRR, BRB, BBR, and BBB. The chance that all the balls are red is 1/4 (possible combinations) in 1/8 of all possible outcomes. Therefore, the probability that all the balls in the bag are red, given that all the selections so far have been red, is 0.5 where 0 is no probability and 1 is 100 percent probability.

A spam filter builds on the fact that the e-mail recipient can easily recognize spam. Partially, this is because the recipient has not requested the e-mail, but also because the information contained in the e-mail is not of interest to the user. It is also assumed that a third party would also be able to identify spam. Terms of familiarity such as *Hi*, *re:*, and *your account*, are not likely to fool a third party into thinking the e-mail is legitimate and not spam. The task for a spam filter is to automate the process that is done so easily by the user (or third party). In most cases, spam filtering can be done with statistical analysis and Bayesian logic.

Statistical analysis is done by comparing large sets of normal e-mail and sets of spam. Statistics are then derived that look for combination of words that do not normally occur in legitimate e-mail.

*Whitelisting*, combined with the above techniques, is also becoming more popular. The idea of a whitelist is to create a list of known, trusted sites, which allows e-mail from those sites. This tends to be more effective than blacklisting, where known bad sites are blocked. The reason why blacklisting is less effective is because the relay sites used by attackers are constantly changing.

## Maintaining e-mail confidentiality

Confidentiality is achieved when a third party cannot read the e-mail sent between the sender and the receiver.

The e-mail traffic itself can be protected against a third party reading the e-mail with the use of encryption. If the third party can (somehow) defeat the protections previously listed and get a copy of the e-mail, he or she would still have to decrypt the e-mail. The following are some factors to consider when determining how effective encryption will be in maintaining the e-mail's confidentiality:

- If a symmetric key is used, the key is passed securely between the sender and receiver. Hopefully, the key is transmitted in a different manner than the e-mail itself. It would be foolish to e-mail the encryption key and then e-mail an encrypted message. If an attacker can capture the e-mail, they are just as likely to be able to grab the key.
- If a public-private key encryption method is used, the receiver's private key must be protected and kept secret. With public-private key encryption, only the recipient's private key will be able to open and read the message.
- Strong encryption methods should be used. If a weak method is used to encrypt the message, the attacker may grab the e-mail and spend a few weeks decrypting the message. Strong encryption methods are Secure Sockets Layer (SSL) using 256 (or more) bits symmetric keys and Pretty Good Privacy (PGP) using 2048 (or more) bit asymmetric keys.

## Maintaining e-mail integrity

Integrity is the assurance that an e-mail has not been altered in transmission between the sender and the receiver. In familiar terms, integrity ensures that the receiver gets the message that the sender has sent.

E-mail integrity is ensured with the use of digital signatures. (Digital signatures are described earlier in this chapter in the "Data integrity" section.) E-mail integrity can also be maintained by encrypting the e-mail because any alteration to the encrypted e-mail will cause the decryption to fail.

Digitally signing e-mails also allows for nonrepudiation. Repudiation occurs when the sender of the e-mail denies having sent the e-mail at a later date. The sender may attempt to claim that the e-mail is a hoax or a forgery. Because only the holder of the private key (the sender) can create the digital signature, the sender of the e-mail will have to accept responsibility for sending the e-mail or claim that their private key was stolen.

E-mail encryption does not allow for nonrepudiation. Because the encryption is done with the receiver's public key, anyone who has access to this key can encrypt the e-mail.

## E-mail availability issues

A user's ability to send and receive e-mails determines his availability, which is considered a security issue. If an attacker is able to prevent the use of e-mail, this condition would be considered a DoS attack.

E-mail availability is provided by means that are usually considered outside the scope of the e-mail system (with the possible exception of spam filters). The following are some measures that system and network administrators can generally take to ensure e-mail availability:

- The use of a spam filter (discussed earlier in this chapter)
- The use of border protection devices such as firewalls and proxies
- The use of internal network protection devices such as intrusion detection systems (IDS)
- The use of host-based intrusion detection systems (HIDS) to protect individual servers and workstations
- The use of frequent backups, strong passwords, and other good operating procedures

# The E-mail Protocols

Several protocols are associated with e-mail, such as SMTP, POP, and Internet Message Access Protocol (IMAP). These are discussed briefly in the following sections.

## SMTP

The Simple Mail Transfer Protocol (SMTP) is used for sending e-mail messages between servers. Most systems that send mail over the Internet use SMTP to send messages from one server to another; the messages can then be retrieved with an e-mail client using either POP or IMAP. [Figure 12-8](ch12.html#various_protocols_are_used_to_send_and_r) illustrates how e-mail is sent with SMTP and received with POP or IMAP.

![Various protocols are used to send and receive e-mail.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1208.png)

**Figure 12.8. Various protocols are used to send and receive e-mail.**

The SMTP protocol looks very much like a conversation between the sender and receiver. [Figure 12-9](ch12.html#a_typical_smtp_conversation) illustrates this conversation. Initially, the client connects on port 25. This is a well-known port that most SMTP servers listen to; however, the server can be configured to use any other port. Changing the port may make the server more secure through obscurity, but it would then not be accessible to receive mail from the general public. This configuration would only be practical on an isolated corporate wide area network (WAN).

After connecting to port 25, the client waits for the server's greeting. In the following example, the commands issued by the client are shown in bold:

```
telnet the-isp.tmp 25
Trying 169.112.72.30...
Connected to the-isp.tmp.
Escape character is ' ^]'.
220 smtp.the-isp.tmp ESMTP Sendmail 8.12.8/8.12.8;
Wed, 20 May 2009 14:50:41 −0400
```

![A typical SMTP conversation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1209.png)

**Figure 12.9. A typical SMTP conversation**

The client then sends a HELO command with its domain name and waits for the response, as follows. The commands are shown in all-caps here, although the protocol is not case sensitive. Some servers also support the EHLO command, which requests that the server send more information about commands that are available at each step in the conversation. Some mail servers require that the client accurately report their domain; other servers accept any domain name. Reporting a fabricated domain name may be a means for spammers and attackers to hide their tracks.

```
HELO johnbrown
```

The SMTP server responds with the domain name of the client as the server recognizes the client. This need not be the same domain name as the client has sent in the HELO command.

```
250 smtp.the-isp.tmp Hello [112.218.183.8], pleased to meet you
```

The client then sends a MAIL FROM: command providing the sender's address, and waits for the response:

```
MAIL FROM: billy-joe@research.tmp
250 2.1.0 billy-joe@research.tmp... Sender ok
```

The client now sends one RCPT TO: command for each recipient address. The server must acknowledge each command before the client can continue.

```
RCPT TO: mom@research.tmp
250 2.1.5 mom@research.tmp... Recipient ok
```

The e-mail message can now be transmitted. Both message headers and body are part of the data command in the SMTP protocol. The data entry continues until a period (.) followed by a carriage return is entered on a newline, as follows:

```
DATA
354 Enter mail, end with "." on a line by itself
Subject: Hi Mom!
How are you?
Please send money!

Love,
your son - jb
.
250 2.0.0 i7IIofMO001724 Message accepted for delivery
```

Note that all of the header data need not be true. The SMTP protocol treats the Date, From, and To header lines as user-defined data. There is no requirement that these be valid. Spammers will usually put in false header data to avoid detection.

The telnet and SMTP session is now closed with the quit command. If the client has more than one message to transmit, rset command is sent and then followed with a new MAIL, RCPT, and so on. After all messages have been transmitted, the quit command is sent:

```
QUIT
221 2.0.0 smtp.research.tmp closing connection
Connection closed by foreign host.
```

## POP/POP3

The Post Office Protocol (POP) is used to retrieve e-mail from a mail server. POP3 is the most recent version of the protocol and is available in all popular mail clients. POP3 is intended for users to download their e-mail from a mail server on which they have an account or mailbox. Most e-mail clients have a default behavior of deleting the mail on the server after it is downloaded. POP3 does not support sending e-mail.

POP3 is by far the most common protocol used by nontechnical Internet users. It should, therefore, be closely watched for the security concerns that it raises. POP3 uses a client-server model in which the client connects to the server and issues simple text commands, and the server responds. Basic POP3 does not support encryption, so both passwords and the e-mail content are transmitted in the clear (unencrypted). Clients and servers may offer enhanced authentication and encryption that can be used with POP3 to alleviate the security concerns.

To authenticate using the USER and PASS command combination, the client must first issue the USER command. If the POP3 server responds with a positive status indicator (+OK), the client may issue either the PASS command to complete the authentication, or the QUIT command to terminate the POP3 session. If the POP3 server responds with a negative status indicator (-ERR) to the USER command, the client may either issue a new authentication command or the QUIT command. The following is a POP3 session that was initiated with telnet from a command prompt. The commands issued by the client are in bold and the passing of user names and passwords in the clear is transparent:

```
telnet pop.the-isp.tmp 110
Trying 163.67.114.17...
Connected to pop.the-isp.tmp.
Escape character is ' ^]'.
+OK Messaging Multiplexor (iPlanet Messaging Server 5.2 HotFix 1.21
(built Sep  8 2003))
USER jim-bob
+OK password required for user jim-bob
PASS sad2say
+OK Maildrop ready
LIST
+OK scan listing follows
1 2059
.
RETR 1
+OK 2059 octets
Return-path: < jim-bob@sytexinc.com>
Received: from dedicated199-bos.wh.ip.net ([10.228.166.89])
 by cluster02-bos.wh.ip.net
 (iPlanet Messaging Server 5.2 HotFix 1.21 (built Sep  8 2003))
 with ESMTP id <0I2N00LHYMLUAL@cluster02-bos.wh.sprintip.net> for
 jim-bob@the-isp.tmp; Wed, 18 Aug 2004 18:13:06 +0000 (GMT)
      <multiple Received: lines deleted>
Date: Wed, 18 Aug 2003 14:14:20 −0400
```

```
From: Jim Bob < jim-bob@atrc.sytexinc.com>
Subject: Hi mom
To: jim-bob@the-isp.tmp
Reply-to: jim-bob@atrc.sytexinc.com
Message-id: <1092852860.10112.4.camel@compaq.research.tmp>
MIME-version: 1.0
Content-type: text/plain
Content-transfer-encoding: 7BIT
Original-recipient: rfc822; jim-bob@the-isp.tmp

Please send money!

love jim-bob

.
DELE 1
+OK message deleted
QUIT
+OK
Connection closed by foreign host.
```

## IMAP

The Internet Message Access Protocol (IMAP) is a method of accessing e-mail on a remote server. It was designed for use where the e-mail will stay on the remote server, and the user may access the e-mail from more than one client. In this way, the user can be mobile and still have access to all the new and old e-mails. IMAP supports capabilities for retaining e-mail and organizing it in folders on the server. IMAP is often used as a remote file server.

IMAP offers features similar to POP3 with some additions that improve the efficiency for the user and improve their performance over low-bandwidth lines. IMAP has some search capabilities so users do not have to download all their messages to find the critical ones. The structure or outline of a message can also be read without the need for the client to download the entire message. If the user chooses to read the message, the entire e-mail (or just part of it) can be downloaded. Some of the features of IMAP offered by the standards are as follows:

- Access to multiple mailboxes on multiple servers
- Support for folder hierarchies
- Standard and user-defined message flags
- Shared access to folders by multiple users
- Message searching and selection
- Selective access to MIME body parts
- Provision for protocol extensibility through annotations

These features clearly support users who need to access their e-mails from multiple locations and clients and have a need to store the messages for later recall and manipulation.

# E-mail Authentication

Proper authentication is also a security concern. Sometimes authentication is considered a confidentiality issue (for the e-mail receiver) or an integrity issue (for the e-mail sender). E-mail authentication is generally part of the e-mail protocol used. This section discusses several methods for authenticating e-mail.

## Plain login

In the plain authentication method, the user name and password are converted into a base64 encoded string. Base64 encoding was described earlier in [Figure 12-1](ch12.html#base64_encoding_converts_24_bits_of_bina) and in the "Attacks involving malcode" section. In the following example, the application `mimencode` is used to convert the three NULL-terminated strings of `user`, `myUserName`, and `mySecretPassord` into one base64 string. This results in a string of

```
dXNlclwwbXlVc2VyTmFtZVwwbXlTZWNyZXRQYXNzd29yZAo=.

echo "user\0myUserName\0mySecretPassword"  |  mimencode

dXNlclwwbXlVc2VyTmFtZVwwbXlTZWNyZXRQYXNzd29yZAo=
```

Manually telneting into a server and issuing the following commands demonstrates the plain authentication process.

```
telnet email.sytexinc.com 25
Trying 192.168.1.25
Connected to 192.168.1.25
Escape character is ' ^ ]'.
HELO test
auth plain dXNlclwwbXlVc2VyTmFtZVwwbXlTZWNyZXRQYXNzd29yZAo=
235 Authentication successful
```

Note that the mail server responded with "Authentication Successful," indicating that the user name and password were accepted as proper authentication.

Although the user name and password are not human readable during the telnet transaction, this is not a secure way to transmit a password. Anyone sniffing the packets would have no difficulty in identifying the protocol and authentication method. They could then easily extract and decode the password.

## Login authentication

Login authentication is similar to plain authentication, with the user name and password being passed separately. The following example shows the user name and password being encoded with base64. The user name and password are then used to authenticate to the mail server. The lines in bold are entered on the command line.

```
# echo "myUserName"  |  mimencode
bXlVc2VyTmFtZQo=
# echo "mySecretPassword"  |  mimencode
bXlTZWNyZXRQYXNzd29yZAo=
```

The following manual telnet session demonstrates the login authentication. The lines in bold are entered by the e-mail client.

```
# telnet email.sytexinc.com 25
Trying 192.168.1.25
Connected to 192.168.1.25
Escape character is ' ^ ]'.
HELO test
auth login
334 VXNlcm5hbWUC6
bXlVc2VyTmFtZQo=
334 UGFzc3dvcmQ6
bXlTZWNyZXRQYXNzd29yZAo=
235 Authentication successful
```

Note that the mail server provided prompts of "Username:" and "Password:" that are base64-encoded as `VXNlcm5hbWU6Cg` and `UGFzc3dvcmQ6`, respectively.

As with plain text authentication, this is not a secure method of transmitting the user's password. The protocol and authentication method are easily identified and the password extracted and decoded.

## APOP

Authenticated Post Office Protocol (APOP) encrypts the user's password during a POP session. The password is encrypted by using a secret that the user provides to the server long before the APOP session.

The strength of this encryption depends on a number of factors, including the following:

- **The complexity of the secret**—The more complex the secret, the better the encryption.
- **How often the same secret is used**—Over time, the encryption can be broken if the secret is not changed.

To assign the secret on the mail server, the user logs in to the server and issues the popauth command. The user is then prompted for the secret key. Later, when the user attempts to retrieve e-mail with an e-mail client, the same secret key is provided to the client so that the user's password can be encrypted.

There are three security concerns when using APOP:

- The password used is not the same as the user login; therefore, a separate file must be used to keep this password. This becomes another point of failure and possible way to exploit.
- Not all clients support APOP. This may lead organizations to settle for a more universal, although less safe method of authentication, such as the basic user name and password used by POP3.
- APOP is concerned only with encrypting the user name and password and does not encrypt the e-mail messages itself.

## NTLM/SPA

The NT LanManager (NTLM) protocol, also known as Secure Password Authentication (SPA), is a Microsoft-proprietary protocol that operates via the SMTP AUTH interface defined by RFC 2554. This authentication is provided by Microsoft mail for its mail servers and clients as a secure means of authenticating POP3, SMTP, and IMAP traffic.

The NTLM/SPA authentication exchange consists of three messages, as described in the following scenario:

1. The client (either Outlook or Outlook Express) sends the authentication method to be used and the server responds.AUTH NTLM +OK NTLM
2. Now the first authentication message is sent by the client to identify itself to the server. This is message type 1; it indicates the version of Outlook.TlRMTVNTUAABAAAABoI<message 1>
3. The second authentication message is the server's challenge. This message contains a string of 8 bytes called the *nonce*. The client will encrypt the nonce with the user's password and send it back to the server.+ TlRMTVNTUAABAAAAA4I<message 2>
4. Finally, the client responds with the third authentication message. This identifies the user, domain, and host name. The nonce sent in the server's challenge is encrypted with the user's password and returned in this message. The server repeats the encryption process with the stored password for the user and, if the response strings match, authentication is complete. The server then acknowledges that the user has authenticated.TlRMTVNTUAADAAAAGAA<message 3>

## +OK logged onPOP before SMTP

The POP before SMTP authentication method provides a means for preventing spammers from using a mail server for relaying, while providing plenty of flexibility for users that change locations frequently.

Mail relaying occurs whenever a mail server in domain A is used to send mail between domains B and C. Mail servers that permit relaying are abused by spammers who want to cover their tracks by not using their own mail servers to send mail. If a spammer were to use his or her own mail server, the Internet community would quickly block and isolate the spammer's domain.

Many organizations need to provide mail-sending capability for users that access the mail server from different (and changing) domains. Consider a mobile sales force that must send frequent e-mail but is constantly on the road connecting from different service providers. In such a case, the mail server must permit the relaying of mail for the authorized users, while at the same time preventing spammers from relaying mail. The POP before SMTP authentication method provides a solution for this problem.

In a nutshell, SMTP relaying is permitted by an IP address if that IP address has participated in a valid POP session in the prior *x* minutes. (The value of *x* varies for each server but is typically 15 minutes to one day.) The POP protocol requires a valid password so spammers will not be able to use POP prior to using the mail server for relaying. Therefore, only authorized users will be able to use the mail server for mail relaying.

## Kerberos and GSSAPI

Kerberos is a network authentication protocol designed to provide strong authentication for client/server applications by using secret-key cryptography. Kerberos authenticates the client application to the server application. A token is used to authenticate the client. The client first obtains the token from a third-party server (the token server). For the client to get the token, it must pass a strong authentication process.

The Generic Security Services Application Progamming Interface (GSSAPI) is an attempt to establish a generic Application Programming Interface (API) for client-server authentication. Typically, each application has its own authentication methods. By developing and using a common API, the overall security can be improved by the increased attention paid to its implementation and testing. GSSAPI is similar to Kerberos in that a token is passed between the mail client and server. The underlying mechanism is based on public-private key encryption technology.

# Operating Safely When Using E-mail

In addition to the protections provided by the various protocols and encryption methods, a user must also operate safely when using e-mail to avoid security problems. The following sections provide recommended safe operating procedures.

## Be paranoid

You can avoid most e-mail–propagated malcode attacks by properly using your e-mail. The following list outlines some steps that a paranoid user will use to keep safe and secure:

- **Keep your e-mail address private**. Avoid providing it whenever possible on Web sites and other interactive forums such as chat rooms.
- **Set up one or more sacrificial e-mail addresses**. When an e-mail address must be provided to a Web site, the user should have a sacrificial e-mail address to use. When an e-mail is received on this account the user knows that there is a high likelihood that it will be spam or malicious in nature. The user must resist the temptation to browse through the e-mails received on this account.
- **Keep e-mail for different organizations separate**. In most cases, this will mean one account for work and a separate account for home. The ramifications of receiving and propagating malicious code in a work environment may be more damaging than at home.
- **Do not open any e-mail that is not expected**. Common sense can be a strong deterrent to the spread of malicious code. An unexpected "Read This" or "Try This Game" should be ignored until the user can verify what the sender has in mind. The verification can be in person, by phone, or by a second e-mail (initiated from the user).
- **Never save or open attachments from strangers**. All curiosity must be resisted.
- **Never save or open attachments that are not absolutely needed**. The fact that a friend wants to send a user an attachment does not obligate the user to open it. Some users would be surprised to find how easily life proceeds without opening risky e-mails and attachments. If it is really important or of special interest, the friend will follow up and explain what is in the attachment.

## Mail client configurations

Microsoft Outlook uses security zones to allow users to customize whether scripts and active content can be run in HTML messages. Outlook provides two choices for the security zone setting: Internet or Restricted.

Scripting capabilities of the e-mail clients should be disabled whenever possible. As discussed earlier, if the e-mail client executes scripts, the user will be vulnerable to worms and viruses. If scripts must be passed around, they should be saved to a file and examined before being executed.

Mail clients should not use the Preview feature when viewing e-mail. Many e-mail clients will provide a feature to preview the currently selected (highlighted) e-mail on the list of e-mails. This is usually done in a split window, which simultaneously shows the list of received e-mails in one half of the window while the currently selected e-mail can be read in the other half of the window. The Preview feature can be a risk for two reasons. First, depending on the client settings, when an e-mail is opened for display, scripts may be run. Even if the user is aware that a virus is propagating and the user would avoid opening the e-mail, the Preview feature might inadvertently open it.

Another reason for not using the preview feature is that an e-mail may have a flaw in the mime encoding. Some flaws can cause the client to hang or crash the mail client when the e-mail is opened for reading. If it happens that such a malformed e-mail is at the top of the list of e-mails, the Preview feature will attempt to open this e-mail. As a result, the e-mail client will become unusable because each time the client is launched, the Preview feature opens the malformed e-mail and the client crashes immediately.

## Application versions

It is important to stay current with revisions and updates to mail client-server software. SMTP mail servers are high-visibility targets of hackers. This susceptibility is demonstrated in the history of vulnerabilities and subsequent fixes that have evolved over the years for the most popular mail server, sendmail. It was not uncommon to see a new version of sendmail every three months. The pace has slowed in recent years, but new versions are still released every 12 months or so.

You should stay current with the new releases of a mail server. When a new vulnerability or exploit is discovered, a corresponding mail server fix will quickly follow. It is important that all mail servers be upgraded to the new release. Attackers of mail servers will seek the path of least resistance. They will seek out old versions of the mail server application and focus their attacks on these servers.

Network administrators should check the CERT Coordination Center (CERT/CC) at `www.cert.org` for alerts and summaries to ensure that they are running the latest recommended version of their mail server. If the mail server that is being used is not listed by CERT/CC, the network administrators should check with the mail server vendor for the latest recommended release.

When downloading a new version of an SMTP application, it is important to verify the download site (download only from sites with valid certificates) and verify the PGP or MD5 signature of the download. There have been attacks in the past where bad (vulnerable) versions of sendmail have been circulated over the Internet. Network administrators, believing they were protecting themselves, inadvertently downloaded and installed vulnerable versions of sendmail.

## Architectural considerations

A number of system and network-related architectural considerations ensure safe use of e-mail:

- **Check for viruses**. Every workstation or server should run virus protection.
- **Use a mail relay or mail proxy**. Medium- to large-size organizations benefit from having all their mail received first by a mail relay or mail proxy. The mail relay will usually sit in the DMZ outside the perimeter firewall. If configured properly, the relay can check for unwanted scripts, viruses, and questionable attachments. Mail relays are also a good place to put spam protection, such as blacklist monitoring and spam filtering.
- **Buffer against attacks**. If possible, risky activity should be undertaken on workstations that can better afford to be attacked. Generally, this would be a workstation that has little or no personal and sensitive data. This workstation should also not contain critical applications that can't be lost or re-installed. It should be expected that a workstation that is buffering this way may have to be rebuilt every three to six months.
- **Back up frequently**. Even the best security measures will occasionally fail to stop a new and emerging threat. To minimize the impact, when that happens, backups should be done frequently. The frequency of backups depends on the level of critical data involved. A book author will back up a few times a day, while the typical home user may get by with backing up once a week or once a month.
- **Control scripting capabilities**. Some mail clients will provide collaboration capability and run scripts automatically. Usually, this feature can be disabled to reduce the risk of worm and virus attacks.
- **Limit attachments**. Attachments can contain scripts and executable code. When the user runs these scripts or executables, they will have all the privileges and access that the user enjoys. Unless the user is diligent and fully appreciates the risk, it is not safe to allow attachments on e-mail.
- **Quarantine attachments**. In many cases, an organization can benefit from quarantining attachments. To quarantine an attachment, a mail relay or mail proxy strips attachments off of e-mails before they are delivered to users. If the users can assert the need for the attachment and verify that a legitimate sender has sent it, they can recover the attachments.

## SSH tunnel

Creating a secure tunnel for using less secure e-mail protocols can be a strong method of protecting the privacy and integrity of the e-mail. Secure Shell (SSH) is a program for logging into a remote machine. SSH allows for executing commands on a remote machine and is intended to replace rlogin and rsh. SSH provides secure, encrypted communications between two untrusted hosts over an insecure network.

With SSH, TCP/IP ports can be forwarded over the secure channel (through the tunnel). Normally, the SSH client connects to the server over port 22. Consider the following commands (client commands are in bold):

```
ssh   192.168.1.2
jim-bob@192.168.1.2's  password:shh!secret
Last login: Sat Aug 21 11:58:33 2003 from 172.16.1.3
[jim-bob@192.168.1.2]#
```

The SSH client (ssh) attempts to connect to the server `192.168.1.2` on port 22. The client and server exchange encryption keys. Then the client is prompted for a password on the server. It is important to note that the password exchange is done under the umbrella of the encryption; therefore, the password is not vulnerable to sniffing. Once the client has been authenticated, the user gets a window with a command line prompt for entering commands on the server. Everything that the user types and receives in this window is encrypted.

Within this command-line prompt window, the user can read and send mail on the mail server. For reading e-mail, the user can use a text-based client, such as elm or pine. The user can also read the e-mail directly from the mailbox, as follows:

```
[jim-bob@192.168.1.2]# cat /var/spool/mail/jim-bob
Return-path: <tmp@the-isp.tmp>
Received: from my.ip.net ([10.228.166.89]) by
        cl.ip.net (Server 5.2 HotFix 1.21
        (built Sep  8 2003)) with ESMTP id
        <0I1X008AF926WC@cluster02.ip.net> for
        tmp@the-isp.tmp; Wed, 04 Aug 2004 12:22:54 +0000
Date: Wed, 04 Aug 2003 12:21:55 +0000 (GMT)
From: tmp@the-isp.tmp
Subject: Send you money!
Message-id: <0I1X001GF8Z03G@boded0199s.ip.net>
Content-transfer-encoding: 7BIT
Mime-Version: 1.0

Hi,

Jim-bob, I sent your money

Love,  Your Mom
```

Mail can be sent in the command line prompt window using the `mail` command, which invokes sendmail directly, as follows:

```
[jim-bob@192.168.1.2]# mail –s "Thanks Mom" momma@my-isp.tmp
Thanks again, Mom!
Love,
  Your son
.
cc:

[jim-bob@192.168.1.2]#
```

While a user can accomplish the sending and receiving of e-mail in a command line prompt window during an SSH connection, it is less than optimal. Most users will want to use their favorite e-mail clients. With an SSH tunnel, the user can still have the protection of the SSH encryption, while using their favorite client applications. [Figure 12-10](ch12.html#an_ssh_tunnel_to_secure_e-mail) illustrates an SSH tunnel. The following steps are involved in setting up an SSH Tunnel:

1. Establish the SSH session.
2. Configure the e-mail client.

![An SSH tunnel to secure e-mail](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1210.png)

**Figure 12.10. An SSH tunnel to secure e-mail**

### Establish SSH session

An SSH connection to the mail server is established in a similar manner to that described earlier. This will, again, result in a command line prompt window, which will not be used in this case. This can be done with a Windows application, such as putty or on a command line, as follows:

```
ssh mail.sytexinc.com
```

When establishing the SSH session, forward ports from the client to the server. In this case, the client's port 110 (POP3) is forwarded to the server's port 110 for receiving e-mail. Also, the client's port 25 (SMTP) is forwarded to the server's port 25 for sending e-mail. The syntax for designating this port forwarding is as follows:

```
ssh -L 110:mail.iwc.sytexinc.com:110 \
    -L 25:mail.iwc.sytexinc.com:25   \
    mail.iwc.sytexinc.com
```

The syntax tells the SSH application to forward the local port (-L) of 110 to `mail.iwc.sytexinc.com`:110.

### Configure e-mail clients

Once the SSH session is established, the user's e-mail client can be configured to send and receive e-mail to use the SSH tunnel. To do this, the e-mail client should use the POP protocol to acquire e-mail from the user's local port 110, instead of the mail server's port 110. In the same manner, the user's e-mail client should be configured to send mail to the local port 25, instead of the mail server's port 25. Note that on e-mail clients, it is often the case that the user does not set the port numbers, rather they choose the protocol of POP and SMTP and the ports are defaulted to 110 and 25, respectively.

Once the e-mail client is configured, the user can receive from (POP) and send to (SMTP) the mail server. The processes are secure because the traffic passes through the SSH tunnel.

### SSH advantages and disadvantages

The advantage of the SSH tunnel is having a secure, end-to-end connection to the mail server over which all mail traffic is sent and received. This compensates for the use of insecure protocols, such as POP3 and SMTP, both of which are easily intercepted (sniffed) and passwords read.

Another advantage of SSH tunneling is the ability to use the two most supported protocols for e-mail (POP3 and SMTP). All e-mail clients and servers support these protocols. Because SSH has been ported to all platforms, there should be no barrier to an organization setting up an SSH tunnel as the means for remote users to access sensitive e-mail.

Following are some of the disadvantages or considerations when using an SSH tunnel:

- **The SSH session must be established prior to receiving or sending mail**. Most users are accustomed to having instant access to e-mail, without the need to establish a prior connection. Most users will probably bring up the SSH session and leave it up as long as they are on the workstation.
- **SSH sessions may time out and close, causing the user to fail to send or receive e-mail**. Depending on the sophistication of the user, this could require some user training to check and re-establish the SSH session.
- **While SSH is ported to all platforms, the SSH application does not come installed out of the box on many systems**. Therefore, the system administrators or users have the extra task of finding and installing an SSH client.
- **The SSH daemon may not be part of the default mail server installation**. Network or system administrators may have to install and configure the SSH server-side daemon on the mail server.
- **SSH tunneling provides a secure send and receive method between the client and server**. However, this may not extend all the way to the other end of the total e-mail path—the other e-mail user (see [Figure 12-11](ch12.html#an_ssh_tunnel_secures_one-half_of_the_e-)).

## PGP and GPG

Pretty Good Privacy (PGP) and GNU Privacy Guard (GPG) are public-private key encryption technologies that can enhance the security of many applications, including e-mail. GPG and PGP are compatible because new releases will be implemented on the OpenPGP standard.

PGP is probably the most popular cryptographic application in the computer community. PGP is an application developed by Phil R. Zimmermann that allows you to communicate in a secure way over an insecure channel. Using PGP, the privacy of data can be protected with encryption so that only intended individuals can read it. PGP is based on public key cryptography: two complementary keys, called a key pair, are used to maintain secure communications. One of the keys is designated as a private key to which only you have access, and the other is a public key, which you freely exchange with other PGP users. Both your private and your public keys are stored in keyring files.

![An SSH tunnel secures one-half of the e-mail transmission.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1211.png)

**Figure 12.11. An SSH tunnel secures one-half of the e-mail transmission.**

GPG is the open-source equivalent of PGP and is compliant with the proposed OpenPGP Internet standard, as described in RFC 2440. Some of the uses of PGP/GPG are as follows:

- **Encrypt files for transmission or storage on a hard drive**. The e-mail message can be put into a file, encrypted, and then attached to an e-mail.
- **Encrypt data for transmission with other protocols such as POP3**. PGP and GPG integrate with the mail clients to encrypt the data.
- **Create digital signatures of e-mail messages**. PGP and GPG integrate with the mail clients to sign the e-mail message.

# Summary

E-mail (along with Web browsing) is one of the most popular uses of the Internet. But for all of its widespread use, e-mail is very insecure. This insecurity comes about mostly because of two factors:

- A lot of sensitive and private data is sent via e-mail. The potential loss or damage due to a security incident can be considerable in terms of dollars (lost work) or prestige (embarrassment).
- E-mail started out and is still mostly today sent in the clear (unencrypted). This is of particular concern because it is relatively simple for a technical person to sniff (intercept) e-mail traffic on a network.

There are a number of methods to improve the security of e-mail, such as using the more secure protocols that will encrypt the mail traffic.
