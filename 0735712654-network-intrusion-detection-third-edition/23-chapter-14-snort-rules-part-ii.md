# Chapter 14. Snort Rules—Part II

![Snort Rules—Part II](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/01icon01.jpg)

The previous chapter provided an introduction to Snort, in general, and Snort rules. As you will recall, a Snort rule is composed of a rule header, which was examined in detail in the previous chapter, and a rule option, which will be covered thoroughly in this chapter.

The rule header supplies the action that will be applied if the rule is triggered. It details the source and destination IP addresses and ports, the protocol, and the direction of the traffic flow. The rule header can be used alone to form a rule, but it is usually followed by a rule option to provide more detail about the packet attributes. Ironically, there are some commercial NIDS that only allow the same level of detail as a Snort rule header when specifying a signature. In other words, they don’t allow the user to configure much more than the IP addresses, protocol, and TCP or UDP ports to define a signature. Obviously, this cannot be considered very robust in terms of rule or packet granularity. The rule options form the core of Snort’s intrusion-detection capabilities.

# Format of Snort Options

The rule options are separated from the rule header via required parentheses ( ). Look at the following rule:

```
alert tcp !$HOME_NET any -> $HOME_NET any (flags: SF; \ 
msg: "SYN-FIN scan";) 
```

The options portion is as follows:

```
(flags: SF; msg: "SYN-FIN scan";) 
```

Each option is made up of an option keyword, and possibly a value for the particular option keyword. In the preceding example, you find the option keyword flags paired with a value of SF and an option keyword of msg paired with a value of SYN-FIN scan. The value that is associated with a given option keyword depends on the option. Some options require numeric values and others require text. Option keywords are separated from the associated value via the colon (:), and individual options are delimited by a semi-colon (;). A semi-colon must follow the final option as well or an error will be generated. Although most option keywords are usually followed by a value, there are some options that require no value. One such example is the option nocase that indicates a search for content in the packet’s payload is to be case insensitive.

Snort is pretty unconcerned and forgiving about the lack or abundance of whitespace between delimiters such as ; and :. You don’t have to supply spaces, or you can supply multiple spaces between options, values, and delimiters. For instance, the two following options should both work:

```
(flags:SF;msg:"SYN-FIN scan";) 
(flags:  SF    ; msg  : "SYN-FIN scan"  ;) 
```

The backslash (\) is a rule continuation character; rules can be continued on separate lines if this character is supplied at the end of any unfinished line. Speaking of special characters, the pound sign (#) is used as the comment character for Snort rules.

# Rule Options

Some of the most important and commonly used options will be discussed now to convince you of the power of Snort rules. The entire list of burgeoning options will not be covered, but descriptions of all of them can be found at [www.snort.org](http://www.snort.org) by examining the online Snort Users Manual under the documentation link.

## Msg Option

The msg option allows the user or analyst to assign an appropriate message to the output of a triggered rule. When you examine an alert or logged entry for the triggered rule, you will see the offending packet. You will not see the actual rule that triggered the alert in the output itself, so you need some descriptive way of associating the alert with the rule. If you assign an msg option value, it will appear before the offending packet output to give you a better idea of why the rule triggered.

Look at the following format, rule, and an associated alert that triggered from the rule:

Format:

```
msg: "<message text>"; 
```

Sample rule:

```
alert udp any any -> 192.168.5.0/24 31337 \ 
(msg:"Back Orifice";) 
```

Sample output:

```
 [**] Back Orifice [**] 
04/24-08:49:21.318567 192.168.143.15:60256 -> 192.168.5.16:31337 
UDP TTL:41 TOS:0x0 ID:49951 
Len: 8 
```

The Snort rule says to alert (and log) when a UDP packet from any source IP address or port goes to subnet 192.168.5 destination port 31337 and to assign it a message of “Back Orifice”. When the rule is triggered, the alert is recorded with “[**] Back Orifice [**]” to describe the activity.

## Logto Option

The logto option allows you to specify a filename to which to log the activity. This applies to rules with the alert or log action in the rule header only. A rule that is triggered with the alert or log action will normally write to a default directory (either /var/log/snort for UNIX hosts or, on a Windows machine, a subdirectory named log from wherever Snort is launched) or a directory specified using the –l filename option on the command line. This assumes that the user hasn’t changed the default logging to binary output (-b command-line option), to send the output to the syslog daemon (-s command-line option), or disabled logging altogether (-N command-line option).

The logto option can be used to send the output for a specific rule or class of user-chosen rules to a given file. Why might you want to use this option? Well, this is an excellent way to separate the truly dangerous or harmful kinds of alerts from those that are the garden variety. In the case shown in the example, if you suspect that you have some kind of trinoo distributed denial-of-service (DDoS) infestation or any other DDoS activity on the network, you can look directly at the DDoS file for signs of this. This will also be logged to the default alert file as well because the following sample rule uses the action alert.

Format:

```
logto: "<filename>"; 
```

The supplied filename should not include a path, only a filename. Including a path causes Snort to display an error message. You should place the filename in quotes, otherwise an initial space is sometimes added before the name.

Sample rule:

```
alert udp any any -> 192.168.5.0/24 31335 \ 
(msg: "trinoo port"; logto: "DDoS";) 
```

Sample output:

If the rule is triggered, the output on this UNIX host will be found in /var/log/snort/DDoS:

```
 [**] trinoo port [**] 
04/24-09:07:41.320938 192.168.143.15:56881 -> 192.168.5.16:31335 
UDP TTL:42 TOS:0x0 ID:4011 
Len: 8 
```

## Ttl Option

The ttl option allows you to examine the arriving time-to-live field for a specific value. This option could be used for a variety of reasons. One reason to examine this field would be to look for a packet with a low arriving TTL value, which can be indicative of a UNIX host performing a traceroute or a Windows host performing a tracert. When the protocol is UDP and the port ranges are 33000 through 34000, it is most likely a UNIX traceroute. A Windows tracert is done via ICMP echo requests.

The following rule looks for UNIX traceroute traffic to the 192.168.5 network with a UDP port in the range 33000 through 34000 inclusive and an arriving TTL value of 1.

Format:

```
ttl: <number>; 
```

Sample rule:

```
alert udp any any -> 192.168.5.0/24 33000:34000 \ 
(msg: "Unix traceroute"; ttl: 1;) 
```

Sample output:

```
[**] Unix traceroute [**] 
04/24-09:29:37.971353 192.168.143.15:40920 -> 192.168.5.16:33437 
UDP TTL:1 TOS:0x0 ID:40923 
Len: 18 
```

## Id Option

As you recall, the IP identification value is a 16-bit value that is found in the IP header of each datagram. Each new datagram is assigned a unique IP ID number that is typically incremented by 1 for each packet. This number becomes the fragment ID, which assists the destination host in reassembling fragments. The sample rule looks for an unusual IP ID value of 0. It now appears that Linux 2.4 kernels set the IP ID value to 0 when the Don’t Fragment (DF) flag is set in the packet. The reasoning for this is that if the packet will never become fragmented, why bother to assign it a fragment ID?

Format:

```
id: <number>; 
```

Sample rule:

```
alert icmp any any -> 192.168.5.0/24 any \ 
(msg: "Suspect IP Identification #"; ID:0;) 
```

Sample output:

```
[**] Suspect IP Identification # [**] 
04/25-09:21:36.371005 192.168.143.15 -> 192.168.5.16 
ICMP TTL:64 TOS:0x0 ID:00 
```

## Dsize Option

The dsize option allows Snort to examine the size of the payload. You can inspect the payload size for an exact value, or a value less than or greater than a particular number. This can come in handy when you are creating a rule for buffer overflow attacks. These attacks might have a telltale signature of having a larger payload than expected. The following sample rule looks for ICMP packets with a payload size greater than 1,024 bytes.

Format:

```
dsize: [<|>] number 
```

Sample rule:

```
alert icmp any any -> 192.168.5.0/24 any \ 
(msg: "Large ICMP payload"; dsize: >1024;) 
```

Sample output:

```
[**] Large ICMP payload [**] 
04/24-11:10:24.110169 192.168.143.100 -> 192.168.5.16 
ICMP TTL:255 TOS:0x0 ID:5487  DF 
ID:7564   Seq:0  ECHO 
```

## Sequence Option

The sequence option checks the value of the TCP sequence number. The Shaft distributed denial-of-service software is known to assign a fixed sequence number—hexadecimal 28374839—when a TCP flood is directed to a victim site. No doubt, this is something that is configurable in the source code, so this is not a failsafe method of identifying Shaft. Of course, a benign packet could coincidentally be using the same sequence number, too.

Format:

```
seq: <number>; 
```

Sample rule:

```
alert tcp  any any -> any any \ 
(msg: "Possible Shaft DDoS"; seq: 0x28374839;) 
```

Sample output:

```
[**]Possible Shaft DDoS [**] 
04/25-07:19:58.582562 192.168.143.100:35680 -> 192.168.143.15:23 
TCP TTL:255 TOS:0x0 ID:7705  DF 
******S* Seq: 0x28374839  Ack: 0x0   Win: 0x2238 
TCP Options => MSS: 1460 
```

## Acknowledgement Option

The acknowledgement option examines the value of a TCP acknowledgement number. The primary use for this currently is to detect nmap pings. As you discovered in the previous chapter, nmap sends a unique signature when it tries to assess if a host is alive. It sets the ACK flag on, and it sets the acknowledgement value of 0. This would be a rare setting to find in normal traffic because it would be indicative of an already established connection acknowledging that the previous TCP sequence number received was 232 – 1, and now the acknowledgement number is wrapping back to 0.

Format:

```
ack: <number>; 
```

Sample rule:

```
alert tcp  any any -> any any \ 
(msg: "nmap TCP ping"; flags: A; ack: 0;) 
```

Sample output:

```
[**] nmap TCP ping [**] 
04/25-07:27:13.578488 192.168.143.15:63367 -> 192.168.143.16:80 
TCP TTL:42 TOS:0x0 ID:26253 
***A**** Seq: 0x16680003   Ack: 0x0   Win: 0xC00 
```

## Itype and Icode Options

The itype option is used to select a particular ICMP message type. The message type field is found in the zero byte offset of the ICMP message.Valid values for this and its partner option icode, which is used to represent the ICMP message code, can be found at [www.iana.org/assignments/icmp-parameters](http://www.iana.org/assignments/icmp-parameters). The icode option is often used in conjunction with the itype option. The ICMP message code is found in the first byte offset of the ICMP message. Many ICMP messages share the same type but are further delineated using the ICMP code field. For instance, an ICMP type of 3 has many different ICMP codes associated with it. If you are just interested in seeing ICMP port unreachable messages, you must qualify the rule with an itype value of 3 and an icode value of 3.

Format:

```
itype: <number>; 
icode: <number>; 
```

Sample rule:

```
alert icmp  1.1.1.0/24 any -> 192.168.5.0/24 any \ 
(msg: "port unreachable"; itype: 3; icode: 3;) 
```

Sample output:

```
[**] port unreachable [**] 
04/25-07:56:37.129338 1.1.1.16 -> 192.168.5.15 
ICMP TTL:255 TOS:0xC0 ID:33569 
DESTINATION UNREACHABLE: PORT UNREACHABLE 
```

## Flags Option

The flags option enables you to inspect TCP flag settings in many different ways. Starting from the least significant (rightmost) flag bit setting:

|  |  |
| --- | --- |
| F: | Finish flag set |
| S: | Synchronize flag set |
| R: | Reset flag set |
| P: | Push flag set |
| A: | Acknowledgement flag set |
| U: | Urgent flag set |
| 2: | ECN echo flag set (formerly a reserved bit) |
| 1: | ECN congestion window reduced set (formerly a reserved bit) |
| 0: | No flag bits set |

It’s also possible to use one of three modifiers (+,*,!) to assist in examining flag combinations or negating a flag setting. For instance, the A+ flag setting indicates that the Acknowledgement flag must be set. It can be set alone, or any other flag might be set along with it. This could include an acknowledgement on push flag (meaning new data is being sent at the same time received data is being acknowledged to combine transfers into one packet), which is a common and legitimate combination. The * modifier is used when you have a combination of flags and any of those flags might be set. For instance, SFP* says that any combination of the SYN, FIN, and PSH flags can be set—they can all be set; a lone SYN, FIN, or PSH can be set; or any pair in the trio can be set. Finally, the ! modifier specifies to negate the current flag setting. The flags option !S specifies that any TCP segment without the SYN flag set will be a candidate packet.

Format:

```
flags: <flag_settings> 
```

Flag Settings:

- F = FIN
- S = SYN
- R = RST
- P = PSH
- A = ACK
- U = URG
- 2 = ECE
- 1 = CWR
- 0 = No flags set

See [Figure 14.1](ch14.html#ch14fig01) for a pictorial representation of Snort’s TCP flag bits. Possible flag modifiers:

![Snort’s view of the TCP flag byte.](/api/v2/epubs/urn:orm:book:0735712654/files/graphics/14fig01.gif)

**Figure 14.1. Snort’s view of the TCP flag byte.**

|  |  |
| --- | --- |
| + | All, match if listed flag(s) set and any others set |
| * | Any, match if any combination of listed flag(s) set |
| ! | Not, match if listed flag(s) NOT set |

Sample rule:

```
alert tcp  any any -> any any (msg:"Null Scan"; flags:0;) 
```

Sample output:

```
[**] Null Scan [**] 
04/25-05:49:51.914748 192.168.143.15:54746 -> 192.168.143.16:21 
TCP TTL:51 TOS:0x0 ID:23446 
******** Seq: 0x1CED3E2E   Ack: 0x0   Win: 0x1000 
TCP Options => WS: 10 NOP MSS: 265 TS: 1061109567 0 EOL EOL 
```

In the previous sample output, you see a string of eight asterisks (********). Snort changes an asterisk to its respective flag bit letter association (12UAPRSF) if the flag is set in the packet that triggered the alert. Because this is a null scan, no flag bits are set; hence, you see all asterisks.

## Content Option

The content option is one of the most vital and potentially misused options. It provides a means of supplying payload content to search for in the packet. There are many ways to supply the content value and multiple different content values can be sought. This option is used liberally throughout the rules that are supplied in the Snort download, but the content option should also be used wisely. Seeking content in payload is considered to be computationally expensive—in other words, this can slow Snort down considerably if it is not done intelligently. Although the developers of Snort have maximized the efficiency of the algorithm applied to do content searches, it is a slow operation when compared with a more exact task such as a match of a header field value. This is because the header field value is, at most, four bytes long, yet payloads are often much longer, thus taking more time to search.

If at all possible, the content option should be qualified with other options as flags or those that will be discussed shortly, such as an offset into the payload where the content search begins, and depth into the payload where the content search ends. The content option is tested last even if it is listed first in the rule options. This is done to optimize the search by qualifying it with other options.

Content strings can be represented as text or a hexadecimal translation of binary data or a combination of text and hexadecimal. Text strings are enclosed in quotes (“”) and matches are case sensitive unless the nocase option is used. Hexadecimal code is delimited with the pipe (|) characters. Multiple content options and values can be specified in a rule and all values associated with the multiple content options must be found in the packet. The content values associated with the multiple content options can appear in any order in the payload; in other words, they do not have to match the order in which they are listed in the rule. There is another available content option that will not be covered known as the content-list. This allows multiple content strings to be specified and if any of them match, the rule triggers. The Snort Users Manual found on [www.snort.org](http://www.snort.org) discusses this option and gives an example.

Format:

```
content: <"value">; 
content: <"value">; content: <"value">; 
```

Sample rule:

```
alert udp $EXTERNAL_NET any -> $HOME_NET 53 \ 
(msg: "EXPLOIT BIND tsig Overflow Attempt"; \ 
content: "|00 FA 00 FF|"; content: "/bin/sh";); 
```

Sample output:

```
02/22-15:33:19.472301 ATTACKER:1024 -> VICTIM:53 
UDP TTL:64 TOS:0x0 ID:6755 IpLen:20 DgmLen:538 
Len: 518 

<lines omitted to condense output> 

00 3F 90 E8 72 FF FF FF 2F 62 69 6E 2F 73 68 00 .?..r.../bin/sh. 
0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D ................ 
1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D .. !"#$%&'()*+,-
2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C EB ./0123456789:;<. 
07 C0 00 00 00 00 00 3F 00 01 02 03 04 05 06 07 .......?........ 
08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 ................ 
18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 ........ !"#$%&' 
28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 ()*+,-./01234567 
38 39 3A 3B 3C EB 07 C0 00 00 00 00 00 3F 00 01 89:;<........?.. 
02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 ................ 
D8 FA FF BF D8 F7 FF BF D0 7C 0D 08 04 F7 10 40 .........|.....@ 
22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 "#$%&'()*+,-./01 
32 33 34 35 36 37 38 39 3A 3B 3C EB 07 C0 00 00 23456789:;<..... 
00 00 00 3F 00 01 02 03 04 05 06 07 08 09 0A 0B ...?............ 
0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B ................ 
1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B .... !"#$%&'()*+ 
2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B ,-./0123456789:; 
3C EB 07 C0 00 00 00 00 00 00 00 FA 00 FF <............. 
```

This output provides the hex characters in the payload on the left side of the output, followed by the ASCII interpretation of those characters on the right side. The rule that was created looks for UDP traffic from outside the trusted network to destination port 53 on a host on the trusted network. Specifically, it looks for the existence of two strings—the first expressed in hexadecimal 00 FA 00 FF, and the second, the text /bin/sh. Both strings must appear in the payload in any order. This rule will be refined more after some other options are discussed.

Some rule options are used only as modifiers to a content option—in other words, they are meaningless and will generate an error message unless the content option is used. These options are: offset, depth, nocase, and regex. They follow the content option that they qualify and if multiple content options are given, the offset, depth, nocase, and regex options modify only the content option that they immediately follow.

**To Push or Not to Push**

If you examine the TCP rules supplied with Snort, you will discover that many of those with a content option include a flag option of A+. This means for the rule to trigger, the acknowledgement flag must be set and other flags can be set as well. This might seem odd because logically, you might be thinking, “Why isn’t the flag setting P+?” After all, shouldn’t Snort examine content when payload bytes are pushed in the packet?

That is absolutely true; it makes the processing more efficient by qualifying the rule to look at content when actual payload data is transmitted. According to the noted author, Richard Stevens, in *TCP/IP Illustrated, Volume 1*, many BSD derived stacks set the push flag any time data is transmitted; but other operating system stacks set the push flag when data is sent only if the sender empties its write buffer. This means that if the receiver advertises a small TCP window size and the sender doesn’t empty its write buffer when transmitting data, only the acknowledgement flag is set. That is why the A+ flag setting is used, because it will match the condition regardless if the push flag is set or not. Although many packets with only the acknowledgement flag set do not have payload, they will be considered for examination.

Alternatively, an option of dsize > 0 could be used to make sure that there was payload in the packet before examining it. This would catch unusual traffic such as data on the SYN, which the A+ would not.

As an example of payload data sent in a packet with only the acknowledgement flag set, look at two TCPdump records from LaBrea version 2, as discussed in [Chapter 9](ch09.html), “Examining Embedded Protocol Header Fields,” that slowed the attacker by advertising an unusually small TCP window size and then effectively arrested data transfer by decreasing the TCP window size to 0. The first record shows the LaBrea host 10.10.10.155 pretending to be a web server and advertising an usually small TCP window size of 5. Host attacker.net sends 5 bytes of payload, yet you see there is no push flag set along with the acknowledgement flag because this amount of data was too small to empty attacker.net’s TCP write buffer:

```
10.10.10.155.www > attacker.net.2045: S 998514038:998514038(0)
 ack 882335287 
win 5 
attacker.net.2045 > 10.10.10.155.www: . 1:6(5) ack 1 win 8576 (DF) 
```

### Offset Option

As mentioned, the content search is computationally expensive, but it can be made more efficient by starting the search at an offset into the payload if the location of the content is known to begin somewhere other than the first byte in the payload. By default, the content search starts at the first byte, which is considered to be offset 0.

Format:

```
offset: <number>; 
```

Sample rule:

```
alert tcp any any -> 192.168.5.0/24 21   \ 
(msg: "Attempted anonymous ftp access";  \ 
content: "anonymous"; offset: 5;) 
```

Sample output:

```
 [**] Attempted anonymous ftp access [**] 
04/24-12:11:08.724441 192.168.143.15:3484 -> 192.168.5.16:21 
TCP TTL:64 TOS:0x10 ID:30124  DF 
***AP*** Seq: 0x93EE0AB7   Ack: 0xB8352E61   Win: 0x7D78 
TCP Options => NOP NOP TS: 112024246 27551686 
55 53 45 52 20 61 6E 6F 6E 79 6D 6F 75 73 0D 0A  USER anonymous.. 
```

The text “anonymous” is found at the 6th byte in the payload, but because we begin the offset count at 0, it is found in offset byte 5.

### Depth Option

The depth option is another useful option to help limit the amount of processing Snort must do on content searches. The depth specifies the number of bytes to search from the offset. If no offset is given, the offset is assumed to be 0. This option can drastically improve Snort’s performance if packets have large payloads and the content being sought appears in well-defined areas of the payload.

Format:

```
depth: <number> 
```

Sample rule:

```
alert udp !$HOME_NET any -> $HOME_NET 5632 \ 
(msg: "PCAnywhere Startup"; content: "ST"; depth: 2;) 
```

Sample output:

```
[**] PCAnywhere Startup [**] 
04/24-12:11:08.724441 192.168.143.15:3484 -> 192.168.143.16:5632 
UDP TTL:64 TOS:0x10 ID:30124  DF 
73 74 61 72 74 75 70   STARTUP 
```

This rule is triggered if the characters “ST” are discovered two bytes from the default offset of byte 0.

### Nocase Option

The nocase option makes the content search in the payload case insensitive. This means that Snort will match the content string being searched no matter what case is used. This is one of the few options that does not have an option value partnered with it.

Format:

```
nocase; 
```

Sample rule:

```
alert tcp  any any -> any 21  \ 
(msg: "FTP warez snooping"; content: "warez"; nocase;) 
```

Sample output:

```
[**] FTP warez snooping[**] 
04/25-05:28:28.146374 192.168.143.15:3487 -> 192.168.143.16:21 
TCP TTL:64 TOS:0x10 ID:30637  DF 
***AP*** Seq: 0xE1977C8D   Ack: 0x452F7F9   Win: 0x7D78 
TCP Options => NOP NOP TS: 118248207 33775174 
43 57 44 20 57 61 52 65 5A 0D 0A          CWD WaReZ.. 
```

### Regex Option

The regex option modifier of content allows wildcard characters to appear in the content string. Two wildcard characters are available: the ? specifies that a single character can be substituted in the position where the ? is found. The second wildcard character * indicates that any number of characters can be substituted where the * is found.

One excellent use of the regex option is looking for signs of buffer overflow characters. If a buffer overflow is successful on a UNIX host, the attacker might very well try to gain access to a shell such as the Bourne shell using /bin/sh. Yet, there are many other shells that can be used such as the C shell (csh), the Korn shell (ksh), and Bourne again shell (bash), to name a few. Therefore, specifying a proper string and wildcard character will find all of the various shells. Prior to the addition of the regex option, the only way to test for all different shells was to use different rules. Be warned that the regex option will not be fully functional until release 2.0 of Snort.

Format:

```
regex; 
```

Sample rule:

```
log tcp any any -> 192.168.5.0/24 515/ 
(msg: "Attempted shell on lpd"; content: "/bin/*sh"; regex;) 
```

Sample output:

```
[**] Attempted shell on lpd [**] 
03/23-07:41:11.282960 1.1.0.1:1892 -> 192.168.5.55:515 
TCP TTL:64 TOS:0x0 ID:63821 IpLen:20 DgmLen:60 
***AP*** Seq: 0x32A77D55  Ack: 0x0  Win: 0x200  TcpLen: 20 
2F 62 69 6E 2F 63 73 68 0A 00 00 00 00 00 00 00  /bin/csh........ 
00 00 00 00 
```

The previous rule looks for shell access to destination port 515 known as the line printer daemon. The regex qualifier to the content value of /bin/*sh is used to find all the different types of shell access.

## Session Option

The session option is used to capture user data from TCP sessions. It can provide a good forensics tool to see what a particular user is doing, especially if you suspect some kind of malicious behavior is taking place.

There are two available argument keywords for the session rule option: printable or all. The printable keyword only prints out data that the user would normally see or be able to type. The all keyword substitutes non-printable characters with their hexadecimal equivalents.

You should be aware that the use of the session option can degrade the performance of Snort, so it is best used retrospectively; capture the data in binary format (TCPdump files) and then run it through Snort. Also, note that typically when you use this option, you should use the direction operator that specifies both directions as shown in the example. Finally, it is best to use the –d command-line option to dump at the application level; otherwise, it doesn’t make much sense to specify the session option.

By default, the session is recorded in the default log directory. The subdirectory beneath that is the IP number of the host initiating the activity. A file named SESSION:sourceport-destport, where sourceport and destport are the actual source, destination ports for the connection will be located in that directory.

Format:

```
session: [printable|all] 
```

Sample rule:

```
log tcp any any <> 192.168.5.0/24 21 (session: printable;) 
```

Sample output:

Assuming the source host for the session is 1.2.3.4 on port 1025, the following output will be in the log directory in subdirectory 1.2.3.4 file SESSION: 1025-21:

```
220 linux2 FTP server (Version wu-2.5.0(1) Tue Sep 21 16:48:12 EDT 1999) 
ready. 
USER jsmith 
331 Password required for jsmith. 
PASS snorty-the-p1g 
230 User jsmith logged in. 
SYST 
215 UNIX Type: L8 
QUIT 
221-You have transferred 0 bytes in 0 files. 
221-Total traffic for this session was 239 bytes in 0 transfers. 
221-Thank you for using the FTP service on linux2. 
221 Goodbye 
```

## Resp Option

The resp option allows an automated active response when malicious activity is detected. An active response attempts to disable a connection. There are many different combinations of active responses and multiple resp options can be given in a single rule.

TCP connections can be aborted by sending a reset to the sending host socket connection, the receiving host socket connection, or both hosts’ socket connections. If the offending packet is UDP, different ICMP messages can be sent in an attempt to interrupt the UDP data flow. An ICMP network, host, or port unreachable message—or a combination of all three of these ICMP messages—can be sent.

The response option doesn’t come automatically enabled with the source distribution. To enable it, you must explicitly configure Snort via the following command:

```
./configure  --enable-flexresp 
```

This includes the necessary code for compilation. It is also possible that your configuration of UNIX doesn’t have a libnet.h include file required for this to compile. It is available from [www.packetfactory.net](http://www.packetfactory.net).

No discussion of active response is complete unless the requisite caveats are offered. First, think smoking-brain hard before you decide to indiscriminately use active response. It should be used for situations where you perceive that unauthorized harmful access could occur such as a buffer overflow. Keep in mind that attackers can spoof source IP addresses, and you might end up using active response against an IP address or addresses that never sent you traffic to begin with. Think about the consequences of active response if someone spoofs a legitimate partner’s IP addresses; it is possible for you to end up attacking a vital resource. Also, a false positive could cause a totally benign connection to be halted. This can cause a denial of service to legitimate users.

Another concern is timing issues. Many requests and responses are almost instantaneous, especially one such as a UDP DNS query-response pair. Attempting to actively respond to a perceived malicious DNS query might prove to be futile because by the time Snort reacts, the response has probably already been sent.

Format:

```
resp <resp_option[, resp_option…]>; 
```

Available choices for the response are:

|  |  |
| --- | --- |
| rst_snd | Send TCP RESET packets to sending socket |
| rst_rcv | Send TCP RESET packets to receiving socket |
| rst_all | Send TCP RESET packets to both sending and receiving sockets |
| icmp_net | Send an ICMP_NET_UNREACH to sender |
| icmp_host | Send an ICMP_HOST_UNREACH to sender |
| icmp_port | Send an ICMP_PORT_UNREACH to sender |
| icmp_all | Send all of the above ICMP_UNREACH packets to sender |

Sample rule:

```
alert tcp any any -> $HOME_NET 21        \ 
(msg: "FTP password file retrieval";      \ 
flags: A+; resp: rst_all; content: "passwd";) 
```

Sample session:

```
[root@verbo hping2-beta53]# ftp sparky 
Connected to sparky. 
220 sparky FTP server (SunOS 5.7) ready. 
Name (sparky:root): jsmith 
331 Password required for jsmith. 
Password: 
230 User jsmith logged in. 
Remote system type is UNIX. 
Using binary mode to transfer files. 
ftp> cd /etc 
250 CWD command successful. 
ftp> get passwd 
local: passwd remote: passwd 
200 PORT command successful. 
421 Service not available, remote server has closed connection 
```

The previous rule calls for an active response to a connection to an ftp server that references the password file passwd. Snort resets both ends of the connection to interrupt this attempt because the resp option of rst_all was selected.

Look at the last line of the ftp session. You see that right after the attacker entered the command **get passwd**, the connection was actually closed. It is possible that the password file had already been transferred before the reset occurred.

## Tag Option

The use of the tag option enables Snort to dynamically capture additional packets after a rule triggers. Without the tag option, only the packet that caused the rule to be triggered is recorded. This is an excellent way to see what transpires after the rule is triggered to get a better idea of the intent of the activity. This can also be useful for validating that some activity that triggered a rule is simply a false positive.

Format:

```
tag: <type>, <count>, <metric>, [direction] 
```

- ****type.****What traffic to record.session. Record the packets from both sides of the connectionhost. Record the packets from the host that caused the rule to trigger (must use direction modifier)
- ****count.****Number of units specified by metric.
- ****metric.****Number of packets/seconds to record.packets. Record host/session for <count> packets.seconds. Record host/session for <count> seconds.
- ****direction.****Used only with “host” type to indicate host to tag.src. Tag all traffic of source IP in triggered rule.dst. Tag all traffic of destination IP in triggered rule.

Sample rule:

```
alert tcp any any -> any 21 (msg: "FTP passwd access"; flags: A+; \ 
content: "passwd"; tag: session, 10, packets;) 
```

Sample output:

The alert file shows the abbreviated data from the miscreant connection to destination port 21:

```
[**] FTP passwd access [**] 
03/21-20:31:05.610035 10.10.10.101:1454 -> 10.10.10.100:21 
TCP TTL:128 TOS:0x0 ID:50697 IpLen:20 DgmLen:58 DF 
***AP*** Seq: 0x17806739  Ack: 0x121C07E5  Win: 0x1FD3  TcpLen: 20 
```

A directory named 10.10.10.101 was created with a file named TCP:1454-21 to record the session exchange of the attempted password file access and 10 subsequent records. Note that the command line used the –d option to capture and dump the data payload. This is an excerpt of the output:

```
03/21-20:31:05.610035 10.10.10.101:1454 -> 10.10.10.100:21 
TCP TTL:128 TOS:0x0 ID:50697 IpLen:20 DgmLen:58 DF 
***AP*** Seq: 0x17806739  Ack: 0x121C07E5  Win: 0x1FD3  TcpLen: 20 
52 45 54 52 20 2F 65 74 63 2F 70 61 73 73 77 64  RETR /etc/passwd 
0D 0A                                            .. 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= 

03/21-20:31:05.610731 10.10.10.100:21 -> 10.10.10.101:1454 
TCP TTL:64 TOS:0x10 ID:1752 IpLen:20 DgmLen:109 DF 
***AP*** Seq: 0x121C07E5  Ack: 0x1780674B  Win: 0x7D78  TcpLen: 20 
31 35 30 20 4F 70 65 6E 69 6E 67 20 41 53 43 49  150 Opening ASCI 
49 20 6D 6F 64 65 20 64 61 74 61 20 63 6F 6E 6E  I mode data conn 
65 63 74 69 6F 6E 20 66 6F 72 20 2F 65 74 63 2F  ection for /etc/ 
70 61 73 73 77 64 20 28 36 37 39 20 62 79 74 65  passwd (679 byte 
73 29 2E 0D 0A                                   s)... 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= 

<omitted boring records> 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= 

03/21-20:31:08.924038 10.10.10.101:1454 -> 10.10.10.100:21 
TCP TTL:128 TOS:0x0 ID:52489 IpLen:20 DgmLen:58 DF 
***AP*** Seq: 0x17806764  Ack: 0x121C0860  Win: 0x1F58  TcpLen: 20 
52 45 54 52 20 2F 65 74 63 2F 73 68 61 64 6F 77  RETR /etc/shadow 
0D 0A                                            .. 
```

# Putting It All Together

Now that you’ve endured the tedium to understand Snort rules, you might be wondering how you would write a rule for a new exploit that was released. Chances are that the user/developer population of Snort will have a new rule out for a current exploit very quickly. But, assume you have some code that professes to be an attack for which no Snort rule exists.

The first thing to do is to execute the exploit code in an isolated test network such as your home or a segregated lab environment at work. If the code works as advertised, record the packet exchange between the attacking and victim hosts. Then, look for unique and repeatable values in the packet that can be used to write a signature or rule. You might have to read some RFCs to become acquainted with the protocol used in the exploit to understand which are repeatable and which are modifiable values.

Suppose you downloaded some code that exploited a buffer overflow condition for DNS TSIG (transaction signature) records. This is an actual attack that was effective against unpatched versions of BIND from 4.x up to, but not including, 8.2.3. A TSIG record in DNS is another resource record type like an address or pointer record. It is used by resolvers and for dynamic updates to ensure the integrity of an exchanged DNS record using a cryptographic one-way hash and shared secret key.

Because the exploit attempts to get access to a shell at the privilege level that BIND (the “named” daemon) runs at, the captured traffic from the exploit should be examined for this signature. Here is the packet that contains the buffer overflow and subsequent attempt to get shell access:

```
02/22-15:33:19.472301 ATTACKER:1024 -> VICTIM:53 

UDP TTL:64 TOS:0x0 ID:6755 IpLen:20 DgmLen:538 
Len: 518 

DE AD 01 80 00 07 00 00 00 00 00 01 3F 00 01 02 ............?... 
03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 ................ 
13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 ............. !" 
23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 #$%&'()*+,-./012 
33 34 35 36 37 38 39 3A 3B 3C EB 0A 02 00 00 C0 3456789:;<...... 
00 00 00 00 00 3F 00 01 EB 44 5E 29 C0 89 46 10 .....?...D^)..F. 
40 89 C3 89 46 0C 40 89 46 08 8D 4E 08 B0 66 CD @...F.@.F..N..f. 
80 43 C6 46 10 10 66 89 5E 14 88 46 08 29 C0 89 .C.F..f.^..F.).. 
C2 89 46 18 B0 90 66 89 46 16 8D 4E 14 89 4E 0C ..F...f.F..N..N. 
8D 4E 08 EB 07 C0 00 00 00 00 00 3F EB 02 EB 43 .N.........?...C 
B0 66 CD 80 89 5E 0C 43 43 B0 66 CD 80 89 56 0C .f...^.CC.f...V. 
89 56 10 B0 66 43 CD 80 86 C3 B0 3F 29 C9 CD 80 .V..fC.....?)... 
B0 3F 41 CD 80 B0 3F 41 CD 80 88 56 07 89 76 0C .?A...?A...V..v. 
87 F3 8D 4B 0C B0 0B CD 80 EB 07 C0 00 00 00 00 ...K............ 
00 3F 90 E8 72 FF FF FF 2F 62 69 6E 2F 73 68 00 .?..r.../bin/sh. 
0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D ................ 
1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D .. !"#$%&'()*+,-
2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B 3C EB ./0123456789:;<. 
07 C0 00 00 00 00 00 3F 00 01 02 03 04 05 06 07 .......?........ 
08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 ................ 
18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 ........ !"#$%&' 
28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 36 37 ()*+,-./01234567 
38 39 3A 3B 3C EB 07 C0 00 00 00 00 00 3F 00 01 89:;<........?.. 
02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 ................ 
D8 FA FF BF D8 F7 FF BF D0 7C 0D 08 04 F7 10 40 .........|.....@ 
22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 "#$%&'()*+,-./01 
32 33 34 35 36 37 38 39 3A 3B 3C EB 07 C0 00 00 23456789:;<..... 
00 00 00 3F 00 01 02 03 04 05 06 07 08 09 0A 0B ...?............ 
0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B ................ 
1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B .... !"#$%&'()*+ 
2C 2D 2E 2F 30 31 32 33 34 35 36 37 38 39 3A 3B ,-./0123456789:; 
3C EB 07 C0 00 00 00 00 00 00 00 FA 00 FF <............. 
```

One obvious signature is the /bin/sh, which attempts to give shell access after a successful buffer overflow. Another signature of this output is that there must be some identification that a DNS TSIG record has been used.

The DNS type is a 2-byte field and a TSIG record will be assigned a value of 250 (0x00FA). There must also be a 2-byte DNS class associated with each different resource record type and the value assigned to a TSIG record is 255 (0x00FF)—to mean any class. Therefore, there must be an occurrence of 0x00FA00FF in the DNS payload for this to be a TSIG record. You would not find the occurrence of the string “/bin/sh” in a normal TSIG query, so looking for both of these values is likely to find malicious records without alerting on false positives. Although other values in this particular packet could be used for the rule, it is possible to alter the source code so that the exploit would still work, yet the DNS header or following TSIG records could change. Here is a rule that can detect the exploit:

```
alert udp $EXTERNAL_NET any -> $HOME_NET 53  \ 
(msg: "EXPLOIT BIND tsig Overflow Attempt";  \ 
content: "|00 FA 00 FF|"; offset: 12;        \ 
content: "/bin/*sh"; regex; offset: 12;) 
```

The observed traffic uses UDP, and you want to look for attackers coming into your network from an outside host on any port to destination port 53. Two separate content options are used to find the multiple occurrences of strings that are in the signature. The option of regex is used in case a shell other than the Bourne shell is used. The regex option is a work in progress and doesn’t always work as advertised in Snort version 1.8.3. In the previous example, it failed to work when included with the wildcard search of “/bin/*sh”, but it will be fixed and should work in the upcoming version 2.x releases.

Also, the content strings are qualified using an offset of 12 indicating that the search is to begin at the 12th byte offset from the beginning of the DNS message. This is done for efficiency and accuracy because the DNS header takes up the first 12 bytes and the search to be performed is on the DNS payload, not the DNS header.

**The TSIG Exploit**

If you would like more information about TSIG, look at RFC 2845 titled, “Secret Key Transaction Authentication for DNS (TSIG).” More information about the exploit can be found at the Carnegie Mellon CERT site, [www.cert.org](http://www.cert.org), advisory CA-2001-02. There is a wonderful write-up of the exploit done by Paul Asadoorian, which can be found at [www.sans.org/newlook/resources/IDFAQ/TSIG.htm](http://www.sans.org/newlook/resources/IDFAQ/TSIG.htm). Many thanks to Paul for his discussion of the Snort rule and the attack output.

# Summary

Snort rule options provide a wide range of attributes and ways to specify values to examine in a packet. The use of the options is quite intuitive and requires only some familiarization of the various options via experimentation or reading the Snort documentation. With virtually each new release of Snort, more options have been added, making Snort rules feature-rich and comparable or better than many of the commercial NIDS’ signature writing capabilities.

To create a Snort rule for some exploit, run the exploit in an isolated environment and record the traffic either using Snort or TCPdump in a mode where the entire packet is captured for examination. Use any available Snort rule header fields or options to precisely identify the unique values and attributes of the exploit packets. Be aware that some aspects of the exploit source code can be changed to alter the packet content; so, attempt to extract the values or fields that are not likely to change when creating your rule. Selecting and qualifying appropriate fields and values to be used is not an easy thing to do because good signature writing is truly a practiced art that requires knowledge about the signature language, the exploit, and the protocol involved in the exploit.
