# Chapter 13. Domain Name System

**IN THIS CHAPTER**

- **Understanding the role of DNS**
- **Identifying common DNS security weaknesses and attacks**
- **Explaining single-server, split, and split-split DNS designs**
- **Building a DNS architecture**
- **Implementing DNS**
- **Knowing how DNS SEC can be used**

When the Internet first began and was known as ARPANET, it was a small community of universally known IP addresses. As it grew to the bustling size of a few hundred hosts, memorizing and identifying servers by numbers was difficult and inefficient. Because numbers are more difficult for humans to remember, names were developed for servers. So instead of `15.5.5.5` you could say `http://wiley.com`. However, there needed to be a way to link the IP address to a domain name.

To diminish this burden, a flat text file, `hosts.txt`, was created, which contained a listing of server IP addresses and descriptive hostnames. The following is a sample of what this would look like:

```
15.5.5.1     Eric

15.5.5.2     Server
```

Now if someone wanted to use SSH to connect to the system, they could type either SSH 15.5.5.1 or SSH Eric and it would work.

This file was maintained on a single server by the Network Information Center (NIC) of Stanford Research Institute (SRI). Each administrator was responsible for maintaining an up-to-date copy from the central server on their own host.

This system posed many limitations, including restrictions on domain name selection, inaccuracy, and inefficiency for participating administrators.

As a result, in 1984 Paul Mockapetris of the University of Southern California's Information Sciences Institute developed a design for a more efficient distributed translation method. His suggested architecture was released in RFCs 882 and 883 and became the foundation for the domain name system (DNS) used today.

# DNS Basics

Finding a single server out of all the servers on the Internet is like trying to find a single file on a drive with thousands of files. In both cases it helps to have some hierarchy built into the directory to logically group things (see [Figure 13-1](ch13.html#the_domain_hierarchy)). The DNS "namespace" is hierarchical in the same type of upside-down tree structure seen with file systems. Just as you have the root of a partition or drive, the DNS namespace has a root that is signified by a period.

![The domain hierarchy](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1301.png)

**Figure 13.1. The domain hierarchy**

When specifying the absolute path to a file in a file system you start at the root and go to the file:

**/etc/bind/named.conf**

When specifying the absolute path to a server in the DNS namespace you start at the server and go to the root:

`http://www.aboutdebian.com`.

Note the period after the "com" as it's important. It's how you specify the root of the namespace. An absolute path in the DNS namespace is called a *FQDN (Fully Qualified Domain Name)*. FQDNs are prevalent in DNS configuration files and it's important that you always use that trailing period.

Internet resources are usually specified by a domain name *and* a server hostname. The .www part of a URL is often the hostname of the Web server (or it could be an alias to a server with a different hostname). DNS is basically just a database with records for these hostnames. The directory for the entire telephone system is not stored in one huge phone book. Rather, it is broken up into many pieces with each city having, and maintaining, its piece of the entire directory in its phone book. By the same token, pieces of the DNS directory database (the "zones") are stored, and maintained, on many different DNS servers located around the Internet. If you want to find the telephone number for a person in Poughkeepsie, you'd have to look in the Poughkeepsie telephone book. If you want to find the IP address of the .www server in the `some-domain.com` domain, you'd have to query the DNS server that stores the DNS records for that domain.

The entries in the database map a host/domain name to an IP address. [Table 13-1](ch13.html#types_of_information_stored) is a simplistic logical view of the type of information that is stored (we'll get to the A, CNAME, and MX designations in a bit).

**Table 13.1. Types of Information Stored**

|  |  |  |
| --- | --- | --- |
| A | `www.their-domain.com` | 172.29.183.103 |
| MX | `mail.their-domain.com` | 172.29.183.217 |
| A | `debian.your-domain.com` | 10.177.8.3 |
| CNAME | `www.your-domain.com` | 10.177.8.3 |
| MX | `debian.your-domain.com` | 10.177.8.3 |

This is why a real Internet server needs a *static* (unchanging) IP address. The IP address of the server's NIC connected to the Internet has to match whatever address is in the DNS database. However, dynamic DNS does provide a way around this for home servers, which we'll see later.

When you want to browse to `www.their-domain.com` your DNS server (the one you specify in the TCP/IP configuration on your desktop computer) most likely won't have a DNS record for `their-domain.com` domain so it has to contact the DNS server that does. When your DNS server contacts the DNS server that has the DNS records (referred to as "resource records" or "zone records") for `their-domain.com` your DNS server gets the IP address of the Web server and relays that address back to your desktop computer. So which DNS server has the DNS records for a particular domain?

When you register a domain name with someone such as Network Solutions, among the things you're asked for are the server names and addresses of two or three "name servers" (DNS servers). These are the servers where the DNS records for your domain will be stored (and queried by the DNS servers of those browsing to your site). So where do you get the "name servers" information for your domain? Typically, when you host your Web site using a Web hosting service, they not only provide a Web server for your domain's Web site files but they will also provide a DNS server to store your domain's DNS records. In other words, you'll want to know who your Web hosting provider is going to be before you register a domain name (so you can enter the provider's DNS server information in the name servers section of the domain name registration application).

### Note

You'll see the term "zone" used in DNS references. Most of the time a zone just equates to a domain. However, this wouldn't be true if you set up subdomains *and* set up separate DNS servers to handle just those subdomains. For example, a company would set up the subdomains `us.their-domain.com` and `europe.their-domain.com` and would "delegate" a separate DNS server to each one of them. In the case of these two DNS servers their zone would be just the subdomains. The zone of the DNS server for the parent `their-domain.com` (which would contain the servers `www.their-domain.com` and `mail.their-domain.com`) would only contain records for those few machines in the parent domain. Note that in the preceding example "us" and "europe" are subdomains while "www" and "mail" are hostnames of servers in the parent domain.

Once you've got your Web site up and running on your Web hosting provider's servers and someone surfs to your site, the DNS server specified in this person's local TCP/IP configuration will query your hosting provider's DNS servers to get the IP address for your Web site. The DNS servers that host the DNS records for your domain, i.e. the DNS servers you specify in your domain name registration application, are the authoritative DNS servers for your domain. The surfer's DNS server queries one of your site's authoritative DNS servers to get an address and gets an authoritative response. When the surfer's DNS server relays the address information back to the surfer's local PC it is a non-authoritative response because the surfer's DNS server is not an authoritative DNS server for your domain.

Example: If you surf to MIT's Web site the DNS server you have specified in your TCP/IP configuration queries one of MIT's authoritative DNS servers and gets an authoritative response with the IP address for the www server. Your DNS server then sends a non-authoritative response back to your PC. You can easily see this for yourself. At a shell prompt, or a DOS window on a newer Windows system, type in

```
nslookup www.mit.edu
```

First you'll see the name and IP address of your locally specified DNS server. Then you'll see the non-authoritative response your DNS server sent back containing the name and IP address of the MIT Web server. (You'll also see that "www" is actually an alias for a different server with the hostname DANDELION-PATCH.)

If you're on a Linux system you can also see which name server(s) your DNS server contacted to get the IP address. At a shell prompt type in

```
whois mit.edu
```

and you'll see three authoritative name servers listed with the hostnames STRAWB, W20NS, and BITSY. The `whois` command simply returns the contents of a site's domain record.

**Records and Records**

Don't confuse DNS zone records with domain records. Your **domain record** is created when you fill out a domain name registration application and is maintained by the domain registration service (such as Network Solutions) that you used to register the domain name. A domain has only one domain record and it contains administrative and technical contact information as well as entries for the authoritative DNS servers (aka "name servers") that are hosting the DNS records for the domain. You have to enter the hostnames and addresses for multiple DNS servers in your domain record for redundancy (fail-over) purposes.

**DNS records** (aka **zone records**) for a domain are stored in the domain's zone file on the authoritative DNS servers. Typically, it is stored on the DNS servers of whatever Web hosting service is hosting your domain's Web site. However, if you have your own Web server (rather than using a Web hosting service) the DNS records could be hosted by you, using your own authoritative DNS servers (as in MIT's case), or by a third party like EasyDNS.

In short, the name servers you specified in your domain record host the domain's zone file containing the zone records. The name servers, which host the domain's zone file, whether they be your Web hosting provider's, those of a third party like EasyDNS, or your own, are authoritative DNS servers for the domain.

Because DNS is so important to the operation of the Internet, when you register a domain name you must specify a minimum of two name servers. If you set up your own authoritative DNS servers for your domain you must set up a minimum of two (for redundancy) and these would be the servers you specify in your domain record. While the multiple servers you specify in your domain record are authoritative for your domain, only one DNS server can be the primary DNS server for a domain. Any others are "secondary" servers. The zone file on the primary DNS server is "replicated" (transferred) to all secondary servers. As a result, any changes made to DNS records must be made on the primary DNS server. The zone files on secondary servers are read-only. If you made changes to the records in a zone file on a secondary DNS server they would simply be overwritten at the next replication. As you will see further on, the primary server for a domain and the replication frequency are specified in a special type of zone record.

Early on in this page we said that the DNS zone records are stored in a DNS database, which we now know is called a zone file. The term "database" is used quite loosely. The zone file is actually just a text file, which you can edit with any text editor. A zone file is domain-specific. That is, each domain has its own zone file. Actually, there are two zone files for each domain but we're only concerned with one right now. The DNS servers for a Web hosting provider will have many zone files, two for each domain it's hosting zone records for. A zone "record" is, in most cases, nothing more than a single line in the text zone file.

There are different types of DNS zone records. These numerous record types give you flexibility in setting up the servers in your domain. The most common types of zone records are:

- An **A** (Address) record is a "host record" and it is the most common type. It is simply a static mapping of a hostname to an IP address. A common hostname for a Web server is **`www`** so the A record for this server gives the IP address for this server in the domain.
- An **MX** (Mail eXchanger) record is specifically for mail servers. It's a special type of service-specifier record. It identifies a mail server for the domain. That's why you don't have to enter a hostname like **`www`** in an e-mail address. If you're running Sendmail (mail server) and Apache (Web server) on the same system (i.e. the same system is acting as both your Web server and e-mail server), both the A record for the system and the MX record would refer to the same server.To offer some fail-over protection for e-mail, MX records also have a **Priority** field (numeric). You can enter two or three MX records, each pointing to a different mail server, but the server specified in the record with the highest priority (lowest number) will be chosen first. A mail server with a priority of 10 in the MX record will receive e-mail before a server with a priority of 20 in its MX record. Note that we are only talking about receiving mail from other Internet mail servers here. When a mail server is sending mail, it acts like a desktop PC when it comes to DNS. The mail server looks at the domain name in the recipient's e-mail address and the mail server then contacts its local DNS server (specified in the `resolv.conf` file) to get the IP address for the mail server in the recipient's domain. When an authoritative DNS server for the recipient's domain receives the query from the sender's DNS server it sends back the IP addresses from the MX records it has in that domain's zone file.
- A *CNAME (Canonical Name)* record is an alias record. It's a way to have the same physical server respond to two different hostnames. Let's say you're not only running Sendmail and Apache on your server, but you're also running WU-FTPD so it also acts as an FTP server. You could create a CNAME record with the alias name `ftp` so people would use `ftp.your-domain.com` and `www.your-domain.com` to access different services on the same server.Another use for a CNAME record was illustrated in the example near the top of the page. Suppose you name your Web server "debian" instead of "www". You could simply create a CNAME record with the alias name "www" but with the hostname "debian" and debian's IP address.
- **NS** (Name Server) records specify the authoritative DNS servers for a domain.

There can be multiples of all the record types mentioned. There is one special record type of which there is only one record in the zone file. That's the **SOA** (Start Of Authority) record and it's the first record in the zone file. An SOA record is only present in a zone file located on authoritative DNS servers (non-authoritative DNS servers can cache zone records). It specifies such things as:

- The primary authoritative DNS server for the zone (domain).
- The e-mail address of the zone's (domain's) administrator. In zone files, the "@" has a specific meaning so the e-mail address is written as `me.my-domain.com`.
- Timing information as to when secondary DNS servers should refresh or expire a zone file and a serial number to indicate the version of the zone file for the sake of comparison.

The SOA record is the one that takes up several lines.

Several important points to note about the records in a zone file:

Records can specify servers *in other domains*. This is most commonly used with MX and NS records when backup servers are located in a different domain but receive mail or resolve queries for your domain.

There must be an A record for systems specified in all MX, NS, and CNAME records.

A and CNAME records can specify workstations as well as servers (which you'll see when we set up a LAN DNS server).

Now let's look at a typical zone file. When a Debian system is set up as a DNS server the zone files are stored in the /etc/bind directory. In a zone file the two parentheses around the timer values act as line-continuation characters as does the backslash ( \ ) character at the end of second line. The semicolon ( ; ) is the comment character. The "IN" indicates an INternet-class record.

```
$TTL 86400
my-name.com.          IN     SOA    debns1.my-name.com. \
                                    joe.my-name.com. {
                   2004011522     ; Serial no., based on date
                        21600     ; Refresh after 6 hours
                         3600     ; Retry after 1 hour
                       604800     ; Expire after 7 days
                         3600     ; Minimum TTL of 1 hour
)
;Name servers
debns1                IN     A       192.168.1.41
debns2.joescuz.com.   IN     A       192.168.1.42

@                     IN     NS      debns1
my-name.com.          IN     NS      debns2.my-name.com.

;Mail servers
debmail1              IN     A       192.168.1.51
debmail2.my-name.com. IN     A       192.168.1.52

@                     IN     MX      10 debmail1
my-name.com.          IN     MX      20 debmail2.my-name.com.

;Aliased servers
debhp                 IN     A       192.168.1.61
debdell.my-name.com.  IN     A       192.168.1.62

www                   IN     CNAME   debhp
ftp.my-name.com.      IN     CNAME   debdell.my-name.com.
```

Several things to take note of when evaluating this example zone file:

- Records are grouped in fours and then subgrouped in twos. The lines are spaced apart only to aid in the readability of this example. You don't want any blank lines in a zone file.
- The first two records in the group of four use A records to specify the servers, and then the second two records are types which specify what those servers are used for. Optionally, you could list all A records together, all NS records together, all CNAME records together, etc.
- The first record in the subgroup of two is a shorthand way of entering the information (without the FQDN). The second record is the longhand way. The @ is a shorthand way of specifying "this zone" (domain).
- Whenever you specify a domain in a zone file it must have a trailing period to make it a FQDN.
- The `$TTL 86400` line at the very top of the file specifies the Time To Live value for the record (used by secondary DNS servers).
- Notice that this zone file specifies the required two DNS servers (with the primary specified in the SOA record) and two mail servers (also for redundancy).
- Also notice the priority numbers before the hostnames in the MX records.

If you had a simpler setup with only one server with the hostname `debian` that operated as a Web, e-mail, and FTP server and you had your DNS records hosted by someone like EasyDNS, your zone file would look a lot simpler:

```
$TTL 86400
my-name.com.          IN     SOA    ns1.easydns.com. \
                                    me.my-name.com. (
                   2004011522     ; Serial no., based on date
                        21600     ; Refresh after 6 hours
                         3600     ; Retry after 1 hour
                       604800     ; Expire after 7 days
                         3600     ; Minimum TTL of 1 hour
                      )
debian                IN     A       192.168.1.51
ns1.easydns.com.      IN     A       216.220.40.243
ns2.easydns.com.      IN     A       205.210.42.20
@                     IN     NS      ns1.easydns.com.
@                     IN     NS      ns2.easydns.com.
@                     IN     MX      10 debian
www                   IN     CNAME   debian
ftp                   IN     CNAME   debian
debian                IN     CNAME   @
```

Naturally, the 192.169.1.51 private address in this example would have to be an ISP-assigned public address for an Internet-accessible server. We just used a private address as an example.

Notice that the last CNAME record is a little different from the others. It specifies which server should handle requests when no hostname is specified, e.g., requests going to simply `my-name.com` in a URL. Notice also that you can specify other domains in your zone file, which is where the long-hand way of specifying a FQDN is useful.

# Purpose of DNS

A DNS is composed of name servers, resolvers, and their communications protocol. Together they create a distributed Internet directory service capable of translating between IP addresses and host domain names.

Nearly all Internet services today rely on DNS to function, and without this translation mechanism they cannot operate.

Without DNS, you would enter `http://216.239.39.99` into your Web browser instead of `http://www.google.com`, you would send e-mail to [sring@63.148.66.186](mailto:sring@63.148.66.186) instead of [ecole@testsystem.com](mailto:ecole@testsystem.com), and you would have to configure your instant message chat client to know that America Online is at `64.12.30.216`. Essentially, the Internet can still function without DNS, but it would mean you would have to remember numbers instead of names. If you know a company is called Wiley, you can make a good guess at what its domain name might be, but you would have no idea what its IP address is.

IP addresses alone are difficult to remember. DNS provides a means of translating addresses into names (and vice versa) that can be descriptive and representative of a site and its purpose/contents.

As shown in [Figure 13-2](ch13.html#fully_qualified_domain_name_structure), reading from left to right, a fully qualified domain name is composed of a server, optional subdomains, an organizational domain, and a top-level domain.

![Fully qualified domain name structure](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1302.png)

**Figure 13.2. Fully qualified domain name structure**

Top-level domains are shared across organizations and examples include `.com`, `.mil`, `.edu`, and `.org`. Domain names are registered by organizations through providers such as Network Solutions and `Register.com`. They are generally not shared across organizations and are descriptive of the information provided within the domain. When subdomains are used, fully qualified domain names are similar to the names in [Figure 13-3](ch13.html#fully_qualified_domain_names_including_s).

![Fully qualified domain names including subdomains](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1303.png)

**Figure 13.3. Fully qualified domain names including subdomains**

Subdomains provide the ability to further categorize a site. However, they require the user to remember and type additional information, and are therefore infrequently used.

### Note

On October 25, 2001, the United States Patent and Trademark office awarded patent application number 20010034657 titled "Method and apparatus for conducting domain name service" to Ideaflood, Inc. According to this application, Ideaflood has patented the idea of assigning users subdomains, such as `client.hostingcompany.com`.

Top-level domain names were initially broken down by organization type, such as `.gov` for government, `.edu` for education, and `.com` for commercial. However, as the Internet became a global network, people wanted to be able to distinguish by country. In addition, countries that came late to the game noticed all of the good names were used up. Now if you reside in Andoria and your company is named Wiley, because `wiley.com` is taken, you could register `wiley.an`. [Table 13-2](ch13.html#top-level_domains_from_around_the_world) lists the high-level domain names based on country.

## Forward lookups

Name-to-address resolution is referred to as a *forward DNS lookup*. This is the normal operation of DNS used by most applications. In this case, the user sends a DNS query to resolve the actual IP address that corresponds with a domain name. In addition to providing a convenience to the user, the mechanics of forward lookups enable a domain to implement load balancing (see [Figure 13-4](ch13.html#forward_lookups_translate_domain_names_i)).

![Forward lookups translate domain names into IP addresses.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1304.png)

**Figure 13.4. Forward lookups translate domain names into IP addresses.**

As the preceding figure depicts, the single server name `www.yahoo.com` can actually represent a cluster of hosts. Each of these hosts has a unique IP address.

Depending on current load, DNS may respond with a different IP address to the same user request, as depicted in the following code example:

```
blinky@site$ ping www.yahoo.com
PING www.yahoo.akadns.net (216.109.118.70) 56(84) bytes of data.
64 bytes from p7.www.dcn.yahoo.com (216.109.118.70):
icmp_seq=1 ttl=53 time=11.1 ms

blinky@site$ ping www.yahoo.com
PING www.yahoo.akadns.net (216.109.117.204) 56(84) bytes of data.
64 bytes from p17.www.dcn.yahoo.com (216.109.117.204):
icmp_seq=1 ttl=52 time=13.7 ms
```

Both of the preceding DNS requests are to the site `www.yahoo.com`, but each responds using different IP addresses.

**Table 13.2. Top-Level Domains from Around the World**

| Domain | Country | Domain | Country | Domain | Country |
| --- | --- | --- | --- | --- | --- |
| Ad | Andorra, Principality of | gm | Gambia | nr | Nauru |
| Ae | United Arab Emirates | gn | Guinea | nt | Neutral Zone |
| Af | Afghanistan, Islamic State of | gov | USA Government | nu | Niue |
| Ag | Antigua and Barbuda (French) | gp | Guadeloupe | nz | New Zealand |
| Ai | Anguilla | gq | Equatorial Guinea | om | Oman |
| al | Albania | gr | Greece | org | Non-Profit Making Organizations (sic) |
| Am | Armenia | gs | S. Georgia & S. Sandwich Isls. | pa | Panama |
| An | Netherlands Antilles | gt | Guatemala | pe | Peru |
| Ao | Angola | gu | Guam (USA) | pf | Polynesia (French) |
| Aq | Antarctica | gw | Guinea Bissau | pg | Papua New Guinea |
| Ar | Argentina | gy | Guyana | ph | Philippines |
| Arpa | Old style Arpanet | hk | Hong Kong | pk | Pakistan |
| As | American Samoa | hm | Heard and McDonald Islands | pl | Poland |
| At | Austria | hn | Honduras | pm | Saint Pierre and Miquelon |
| Au | Australia | hr | Croatia | pn | Pitcairn Island |
| Aw | Aruba | ht | Haiti | pr | Puerto Rico |
| Az | Azerbaidjan | hu | Hungary | pt | Portugal |
| Ba | Bosnia-Herzegovina | id | Indonesia | pw | Palau |
| Bb | Barbados | ie | Ireland | py | Paraguay |
| Bd | Bangladesh | il | Israel | qa | Qatar |
| Be | Belgium | in | India | re | Reunion (French) |
| Bf | Burkina Faso | int | International | ro | Romania |
| Bg | Bulgaria | io | British Indian Ocean Territory | ru | Russian Federation |
| Bh | Bahrain | iq | Iraq | rw | Rwanda |
| Bi | Burundi | ir | Iran | sa | Saudi Arabia |
| Bj | Benin | is | Iceland | sb | Solomon Islands |
| Bm | Bermuda | it | Italy | sc | Seychelles |
| Bn | Brunei Darussalam | jm | Jamaica | sd | Sudan |
| Bo | Bolivia | jo | Jordan | se | Sweden |
| Br | Brazil | jp | Japan | sg | Singapore |
| Bs | Bahamas | ke | Kenya | sh | Saint Helena |
| Bt | Bhutan | kg | Kyrgyz Republic (Kyrgyzstan) | si | Slovenia |
| Bv | Bouvet Island | kh | Cambodia, Kingdom of | sj | Svalbard and Jan Mayen Islands |
| Bw | Botswana | ki | Kiribati | sk | Slovak Republic |
| By | Belarus | km | Comoros | sl | Sierra Leone |
| Bz | Belize | kn | Saint Kitts & Nevis Anguilla | sm | San Marino |
| Ca | Canada | kp | North Korea | sn | Senegal |
| Cc | Cocos (Keeling) Islands | kr | South Korea | so | Somalia |
| Cd | Congo, The Democratic Republic of the | kw | Kuwait | sr | Suriname |
| Cf | Central African Republic | ky | Cayman Islands | st | Saint Tome (Sao Tome) and Principe |
| Cg | Congo | kz | Kazakhstan | su | Former USSR |
| Ch | Switzerland | la | Laos | sv | El Salvador |
| Ci | Ivory Coast (Cote D'Ivoire) | lb | Lebanon | sy | Syria |
| Ck | Cook Islands | lc | Saint Lucia | sz | Swaziland |
| Cl | Chile | li | Liechtenstein | tc | Turks and Caicos Islands |
| Cm | Cameroon | lk | Sri Lanka | td | Chad |
| Cn | China | lr | Liberia | tf | French Southern Territories |
| Co | Colombia | ls | Lesotho | tg | Togo |
| Com | Commercial | lt | Lithuania | th | Thailand |
| Cr | Costa Rica | lu | Luxembourg | tj | Tadjikistan |
| Cs | Former Czechoslovakia | Latvia | lv | Tokelau | tk |
| Cu | Cuba | ly | Libya | tm | Turkmenistan |
| Cv | Cape Verde | ma | Morocco | tn | Tunisia |
| Cx | Christmas Island | mc | Monaco | to | Tonga |
| Cy | Cyprus | md | Moldavia | tp | East Timor |
| Cz | Czech Republic | mg | Madagascar | tr | Turkey |
| De | Germany | mh | Marshall Islands | tt | Trinidad and Tobago |
| Dj | Djibouti | mil | USA Military | tv | Tuvalu |
| Dk | Denmark | mk | Macedonia | tw | Taiwan |
| Dm | Dominica | ml | Mali | tz | Tanzania |
| Do | Dominican Republic | mm | Myanmar | ua | Ukraine |
| Dz | Algeria | mn | Mongolia | ug | Uganda |
| Ec | Ecuador | mo | Macau | uk | United Kingdom |
| Edu | Educational | mp | Northern Mariana Islands | um | USA Minor Outlying Islands |
| Ee | Estonia | mq | Martinique (French) | us | United States |
| Eg | Egypt | mr | Mauritania | uy | Uruguay |
| Eh | Western Sahara | ms | Montserrat | uz | Uzbekistan |
| Er | Eritrea | mt | Malta | va | Holy See (Vatican City State) |
| Es | Spain | mu | Mauritius | vc | Saint Vincent & Grenadines |
| Et | Ethiopia | mv | Maldives | ve | Venezuela |
| Fi | Finland | mw | Malawi | vg | Virgin Islands (British) |
| Fj | Fiji | mx | Mexico | vi | Virgin Islands (USA) |
| Fk | Falkland Islands | my | Malaysia | vn | Vietnam |
| Fm | Micronesia | mz | Mozambique | vu | Vanuatu |
| Fo | Faroe Islands | na | Namibia | wf | Wallis and Futuna Islands |
| Fr | France | nato | NATO (this was purged in 1996—see hq.nato.int) | ws | Samoa |
| Fx | France (European Territory) | nc | New Caledonia (French) | ye | Yemen |
| Ga | Gabon | ne | Niger | yt | Mayotte |
| Gb | Great Britain | net | Network | yu | Yugoslavia |
| Gd | Grenada | nf | Norfolk Island | za | South Africa |
| Ge | Georgia | ng | Nigeria | zm | Zambia |
| Gf | French Guyana | ni | Nicaragua | zr | Zaire |
| Gh | Ghana | nl | Netherlands | zw | Zimbabwe |
| Gi | Gibraltar | no | Norway |  |  |
| Gl | Greenland | np | Nepal |  |  |

Address information within name servers is optimized to provide the fastest feedback to a forward query as possible. To do this, it is arranged categorically based on top-level domains, domains, and subdomains. An example of this type of representation is shown in [Figure 13-5](ch13.html#name_server_data_storage_for_fast_forwar).

![Name server data storage for fast forward lookup queries](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1305.png)

**Figure 13.5. Name server data storage for fast forward lookup queries**

## Reverse lookups

Address-to-name resolutions are called *reverse DNS lookups*. As the name suggests, they are the exact opposite of the forward lookups. In general, these queries are not made manually by users because users tend to remember host and domain names better than IP addresses. Instead, they are used frequently by computers, which prefer numbers.

Reverse lookups are commonly implemented in network-related applications such as server-logging programs and sniffers.

For example, take a look at how two different representations of the same exact line from a tcpdump sniffer log compare:

```
21:00:38.327998                         21:00:38.327998
10.1.1.100.50758 >                      10.1.1.100.50758 >
66.35.250.150.http: S                 Slashdot.org.http: S
3708138522:3708138522(0) win            3708138522:3708138522 (0) win
5840 <mss                               5840 <mss
1460,sackOK,timestamp                   1460,sackOK,timestamp
22373740 0,nop,wscale 0> (DF)           22373740 0,nop,wscale 0> (DF)
```

The entry on the left does not resolve the IP addresses, whereas the entry on the right does. The application itself processes the packet based on its address, but the address is converted into a human-readable domain name for convenience to the user.

Strangely enough, this means that the representation started as a domain name, was converted to an IP address for the application, and then reconverted into a domain name.

Reverse lookups are also occasionally used to determine the domain a user is originating from. This can be used as a method of authorization.

As an example, a user may only want to allow hosts from `company.com` to access a server. Entering all of the allowed IP addresses into an inclusive filter would be time consuming and require constant maintenance as new hosts are added or removed. Using domain names in the filter means the filter is able to do a reverse lookup to obtain all of the IPs tied to that filter and block anyone coming from a specific domain. This is much easier than trying to list every single IP address.

Conventional storage within a name server is optimized to provide fast results based on forward reverses. Because several ranges of IP addresses can be associated with single domain names, each and every domain must be searched until the requested IP address is located. This is inefficient and impractical.

The alternative is to provide a second organization of information within a name server that is specifically designed to quickly field reverse queries. This is done by storing the data in the reverse order (that is, by IP address instead of domain). Commonly referred to as the `in-addr.arpa` domain, data is organized hierarchically by IP addresses (see [Figure 13-6](ch13.html#name_server_data_storage_for_fast_revers)).

However, because domain names are read from leaf to root, it is actually written as `26.146.145.146.in-addr.arpa`, where `26` is the least significant of the address octets.

![Name server data storage for fast reverse lookup queries](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1306.png)

**Figure 13.6. Name server data storage for fast reverse lookup queries**

## Handling Reverse Lookups

To be able to resolve from an IP address back to a domain name, a reverse lookup entry has to be created. Back in the /etc/named.conf file, you need to add the following entry:

```
zone "1.0.10.in-addr.arpa" IN {    // This is the reverse
  lookup record type master;
  file "example.com.rr.zone";
  allow-update { none; };
};
```

Where `1.0.10.in-addr.arpa` is your IP address backwards, minus the final octet.

If your IP address is 1.2.3.4 then the example zone entry would be:

```
zone "3.2.1.in-addr.arpa" IN {    // This is the reverse
  lookup record type master;
  file "example.com.rr.zone";
  allow-update { none; };
};
```

You have to *keep* the `in-addr.arpa` appended to the end of the zone name.

`Example.com.rr.zone` is the filename as in the normal zone record.

The new zone file looks like this:

```
@     IN     SOA    dns1.example.com.     hostmaster.example.com. (
                    2001062501 ; serial
                    21600      ; refresh after 6 hours
                    3600       ; retry after 1 hour
                    604800     ; expire after 1 week
                    86400 )    ; minimum TTL of 1 day

      IN     NS     dns1.example.com.
      IN     NS     dns2.example.com.

20    IN     PTR    alice.example.com.
21    IN     PTR    betty.example.com.
22    IN     PTR    charlie.example.com.
23    IN     PTR    doug.example.com.
24    IN     PTR    ernest.example.com.
25    IN     PTR    fanny.example.com.
```

The SOA is identical to the one on a normal zone file.

The PTR records actually contain the IP address as the first field and the name to be resolved as the last. So if we assume that your file is

```
3.2.1.in-addr.arpa
```

then 1.2.3.20 would resolve to `alice.example.com`, and 1.2.3.25 would resolve to `fanny.example.com`.

## Alternative approaches to name resolution

Name resolution can also be implemented using the `/etc/hosts` file on UNIX operating systems. This is similar to the `hosts.txt` file that was used originally before distributed naming was implemented.

Following is an example of an entry that does this:

```
# Do not remove the following line, or various programs
# that require network functionality will fail.
127.0.0.1     localhost.localdomain     localhost
66.97.36.189     www.uberhaxor.com     hxr
```

The second line tells the operating system that requests for the fully qualified domain `www.uberhaxor.com`, or the nickname hxr, should be directed to the IP address `66.97.36.189`.

Following is an example of a ping that uses Internet domain name resolution (before the change to the `/etc/hosts` file is made):

```
blinky@site$ ping www.uberhaxor.com
PING www.uberhaxor.com (66.97.36.189) 56(84) bytes of data.
64 bytes from www.uberhaxor.com (66.97.36.189):
icmp_seq=1 ttl=49 time=31.7 ms
64 bytes from www.uberhaxor.com (66.97.36.189):
icmp_seq=2 ttl=49 time=23.0 ms

--- www.uberhaxor.com ping statistics ---

2 packets transmitted, 2 received, 0% packet loss, time 1009ms
rtt min/avg/max/mdev = 23.065/27.416/31.767/4.351 ms
```

After the file is saved, the ping functions seamlessly without any intervention from the user using `/etc/hosts` for resolution, as demonstrated in the following example:

```
blinky@site$ ping hxr
PING www.uberhaxor.com (66.97.36.189) 56(84) bytes of data.
64 bytes from www.uberhaxor.com (66.97.36.189):
icmp_seq=1 ttl=49 time=33.3 ms
```

```
64 bytes from www.uberhaxor.com (66.97.36.189):
icmp_seq=2 ttl=49 time=33.0 ms

--- www.uberhaxor.com ping statistics ---

2 packets transmitted, 2 received, 0% packet loss, time 1012ms
rtt min/avg/max/mdev = 33.089/33.209/33.329/0.120 ms
```

# Setting Up DNS

The BIND service is what will give you name resolution within your enterprise.

It is recommended that you run one master DNS server, and at least one slave DNS server as a backup.

The daemon to run BIND is located in /usr/sbin/named

BIND stores its configuration files in the following two places:

- `/etc/named.conf`—The configuration file for the named daemon
- `/var/named/` directory—The named working directory

Inside the `/etc/named.conf` you must configure each domain that you want to resolve. For each domain, you should have one of the following entries in your master DNS configuration file:

```
zone "example.com" IN {
  type master;
  file "example.com.zone";
  allow-update { none; };
};
```

The slave should be configured similarly, like this:

```
zone "example.com" {
  type slave;
  file "example.com.zone";
  masters { 192.168.0.1; };
};
```

The following is a list of valid comment tags used within `named.conf`:

- //—When placed at the beginning of a line, that line is ignored by named.
- #—When placed at the beginning of a line, that line is ignored by named.
- /* and */—When text is enclosed in these tags, the block of text is ignored by named.
- /etc/named/ files—Each file in the named directory should configure one domain.

Let's review an example zone file and discuss what each line means.

```
@     IN     SOA    dns1.example.com.     hostmaster.example.com. (
                    2001062501 ; serial number
```

```
21600      ; time to refresh = 6 hours
                    3600       ; time to retry = 1 hour
                    604800     ; time to expire = 1 week
                    86400 )    ; minimum TTL = 1 day

      IN     NS     dns1.example.com.
      IN     NS     dns2.example.com.

      IN     MX     10     mail.example.com.
      IN     MX     20     mail2.example.com.

             IN     A       10.0.1.5

server1      IN     A       10.0.1.5
server2      IN     A       10.0.1.7
dns1         IN     A       10.0.1.2
dns2         IN     A       10.0.1.3

ftp          IN     CNAME   server1
mail         IN     CNAME   server1
mail2        IN     CNAME   server2
www          IN     CNAME   server2
```

The First record is considered everything in the first six lines.

An SOA record is a Start of Authority record. It publishes critical information about a namespace to the name server. SOA always come before any of the resource file records.

For instance, in this case, the @ represents the ZONE NAME specified in the `named.conf` file—so in this case, `example.com`.

IN stands for Internet, and will be seen throughout this file.

SOA determines the type of record.

`dns1.example.com`. is the primary name server to use for this domain (and, as with all fully qualified domain names, it is followed by a trailing period).

The last entry on the first line is the e-mail address of the hostmaster. The normal @ in the e-mail address is replaced by a period in this record.

Remember that everything after a semicolon is a comment in this file.

The serial number is usually made up of the date and time. Whenever it is changed, the slave servers know to update information, so this should be updated whenever the file is changed.

The time to refresh tells any slave servers how long to wait before asking the master name server if any changes have been made to the zone using the serial number as a guide.

The time to retry tells the slave name server the interval to wait before issuing another refresh request, if the master name server is not answering. If the master has not replied to a refresh request before the time to expire elapses, the slave stops responding as an authority for requests concerning that namespace.

The minimum TTL requests that other name servers cache the zone's information for at least this amount of time.

All time fields are in seconds.

The next two records are Name Server Records. They announce the authoritative name servers for a particular domain. The order of these is not important. Both master and slaves should be listed.

The next two records in this case are MX or Mail Exchange records. They specify where mail sent to a particular domain should go. The number represents the preference. Lower servers are used first. When two servers have identical preferences, they are alternated—which is useful in load balance situations.

Next are five A records. A records are Address records; they assign an IP address to a hostname. In the first example it states that default traffic to `example.com` should go to one IP address. The other four records are specific hostnames and are actually resolved before the default. If someone requests `server2.example.com` then they will go to 10.0.1.5, but if they request `server1.example.com` or just `example.com` without a hostname, then they will both go to 10.0.1.3. dns1 and dns2 are just additional possible hostnames.

The next four records are CNAME records, or Canonical records. These set up aliases to other host or domain names. Having more CNAME records and fewer A name records pointing to the same IP Address is normally considered good form.

# Security Issues with DNS

Too often, DNS servers are installed on old servers that are not capable of servicing large central processing units (CPUs) and bandwidth-intensive applications. This hand-me-down approach lends itself to accidental utilization of outdated and vulnerable operating system releases.

In addition, DNS servers require little manual maintenance, so they are often neglected when it comes time to log monitoring and patch installation.

In contrast, maintaining authority for domain names and IP addresses is a tremendously important responsibility.

Together these factors mark DNS servers as a high target of interest among attackers. As demonstrated in the following sections, gaining access to a DNS server can provide broader access to clients that rely on and trust it.

Yet passwords and access to accounts capable of updating records with providers are often handled with little security. After administrators move on to other positions, passwords are changed for remote access accounts, but seldom is the account for domain registration changed, or the certificate key changed for DNS servers. Consequences of not doing so could be dire to a company.

**AOL DNS Update from a Spoofed E-mail**

Early on the morning of October 16, 1998, someone spoofed an e-mail from an AOL official to the InterNIC domain registration service. Because AOL had chosen the default registration and update method, this single e-mail was able to cause all external AOL traffic to be redirected to the Internet service provider autonet.net.

Transmission problems were discovered as early as 5 a.m. that morning, and lasted until the late afternoon. Autonet.net was overwhelmed with thousands of misrouted e-mails. In parallel to repairing the incorrect DNS record, AOL was forced to rent a server for autonet.net to redirect e-mail back to AOL servers. Following is a DNS registration snapshot for the domain that day:

```
blinky@site$ whois aol.com
[rs.internic.net]
 Registrant:
 America Online (AOL-DOM)
    12100 Sunrise Valley Drive
    Reston, VA 20191
    US

    Domain Name: AOL.COM

    Administrative Contact:
       O'Donnell, David B  (DBO3)  PMDAtropos@AOL.COM
       703/265-5666 (FAX) 703/265-4003
    Technical Contact, Zone Contact:
       America Online  (AOL-NOC)  trouble@AOL.NET
       703-265-4670
    Billing Contact:
       Barrett, Joe  (JB4302)  BarrettJG@AOL.COM
       703-453-4160 (FAX) 703-453-4001

    Record last updated on 15-Oct-98.
    Record created on 22-Jun-95.
    Database last updated on 16-Oct-98 04:27:25 EDT.
    Domain servers in listed order:

    DNS1.AUTONET.NET         206.88.0.34
    DNS2.AUTONET.NET         206.88.0.66

The InterNIC Registration Services database contains ONLY
non-military and non-US Government Domains and contacts.
```

```
Other associated whois servers:
   American Registry for Internet Numbers - whois.arin.net
   European IP Address Allocations        - whois.ripe.net
   Asia Pacific IP Address Allocations    - whois.apnic.net
   US Military                            - whois.nic.mil
   US Government                          - whois.nic.gov.
```

## Misconfigurations

DNS misconfiguration can lead to the following:

- **Service redirection**—The site `downloads.com` is a popular location to acquire free and shareware software applications. If DNS requests to this site were instead redirected to the IP address of a malicious attacker's site, a user might download tainted software without realizing it. If the user trusts the site and does not verify the authenticity through cryptographic signature hashes, the consequences could be monumental. Execution of the tainted software could silently install rootkits and other backdoors.Unscrupulous companies could also use the same approach to redirect traffic from a competitor's Web site to their own. Similarly, name servers with MX records can be modified to redirect e-mail from one domain to another.
- **Denial of service**—The same misconfiguration approaches previously listed can instead be used for simply denial of service. Instead of redirecting records elsewhere, they can be redirected to `10.1.1.1` or another address range that does not exist. Changing a record to a nonexistent IP address means every time someone tries to resolve a domain name they are sent to a server that does not exist and, therefore, cannot resolve the name. This results in a denial-of-service attack.
- **Information leakage for recognizance**—DNS servers maintain significant amounts of information about the architecture of a network. For example, many server naming conventions in companies are descriptive of the services provided by the server. For example, `ns1.company.com` is likely the primary name server while `ns2.company.com` is likely the backup. Similarly, `mail.company.com` is likely the mail server and `www.company.com` is the Web server. Obtaining DNS records can provide an attacker with a complete database of these names along with their associated IP addresses. This database can provide the attacker with recognizance information needed to target specific hosts without actively scanning the network itself.

## Zone transfers

For efficiency and accuracy automated methods have been introduced to ensure that information across primary and secondary name servers is kept up-to-date. Domain record exchanges such as this can reconfigure packet routing across a network.

Zone transfers are one method of doing this. Zone transfers operate as a service that periodically creates connections to primary services to update table information.

### Historical problems

Past versions of name servers had design and implementation issues associated with this service. Older versions included no security, and virtually anyone with access to programs like nslookup and dig were capable of issuing them.

Beyond the danger of modifying or exposing sensitive information, these events were also resource intensive. BIND version 4, for example, created a new named process using `fork()` for each zone transfer. In addition, zone transfers could each be up to 64K in size, which when performed on a large scale in a malicious manner, could take up precious bandwidth.

Today a large number of servers still allow zone transfers to be initiated by any host. Now, nearly all prevent all unauthorized transfers. This hides sensitive server and IP address information from those that do not have a legitimate need to know.

### Specifying transfer sites

The UNIX BIND name server uses the field `allow-transfer` in the zone statement for just this purpose:

```
zone "sytexinc.com"    {
     type master;
     file "data.sytexinc.com";
     allow-transfer { slave-1-IP-addr;  slave-2-IP-addr; };
     }
```

The preceding master statement specifies that it is allowed to transmit zone information to (and only to) the IP addresses of slave-1 and slave-2 DNS servers. Alternatively, a slave should not transmit to anyone in most configurations. An example of an appropriate configuration for a slave follows:

```
zone "sytexinc.com"    {
     type slave;
     file "copy.sytexinc.com";
     allow-transfer { none; };
     }
```

### TSIG for requiring certificates

Transaction Signatures (TSIGs) can provide additional security for conventional zone transfer services. Instead of limiting transfers purely based on IP address, sites can maintain cryptographic signatures that further warranty their authority.

Starting with BIND 8.2, this can be implemented using a shared secret key. This key is stored in a record for each allowed transfer site. Following is an example:

```
key "rndckey" {
  algorithm hmac-md5;
```

```
secret "k6ksRGqf23QfwrPPsdhbn==";
};

zone "sytexinc.com"    {
     type master;
     file "data.sytexinc.com";
     allow-transfer { key "rcdnkey"; };
     };
```

In this example, only DNS zone transfer requests that have been signed with the shared secret key `k6ksRGqf23QfwrPPsdhbn==` are processed.

The benefit of this approach verses the previous IP address restriction is that it allows for more flexibility. Name servers configured with dynamic addressing schemes (that is, DHCP) will not operate using the previous approach, but as long as they are knowledgeable of the shared key they will operate in this circumstance.

On the slave, the configuration file would include the following:

```
key "rndckey" {
  algorithm hmac-md5;
  secret "k6ksRGqf23QfwrPPsdhbn==";
};

zone "sytexinc.com"    {
     type slave;
     file "data.sytexinc.com";
     allow-transfer { none; };
};

server master-IP-addr {
  keys { "rndckey"; };
};
```

This identifies that all requests designed for the IP address of the master name server should be signed with the shared secret key `rndckey`.

The weakness of this design is that shared secret keys are used between the two severs, which means that if one server is compromised, the key has been exposed and all are vulnerable.

### DNS Security Extensions

Similar to TSIG, DNS security extensions (DNS SEC) are designed to provide an authorization method for name server queries. However, unlike TSIG, DNS SEC relies on public key cryptography. This model is described in more detail in RFC 2535. However, past experiments have shown that issues exist with this key handling in this design and the Internet Engineering Task Force (IETF) is currently reviewing revision drafts. Although no new RFC has been published yet, it is anticipated that 2535bis will become the standard. DNS SEC will be discussed in detail later in this chapter.

The benefit of using a public key infrastructure is that configurations can be transmitted without fear of compromise, and the exploitation of one server does not automatically expose the keys of all servers.

A key file in this scheme would resemble the following:

```
trusted-keys {
    "." 256 3 1 "AsfFGnuB5FGD87VdjwbyMQxuMs4DSVDSSsdcxr6xR
                 ffg67jmRdtisIskoAhw4tingujdyWCCXFFG455sd6
                 70K7FSlTARDIjr3hXfTLDS5HnP";
};
```

DNS SEC creates larger DNS messages and larger zones, which, in turn, requires additional bandwidth and processing resources.

### Zone transfer alternatives

Several popular alternatives exist to conventional zone transfers. The secure copy program, scp (which is part of the OpenSSH distribution), is one example. By default, this program is manual, but it can be combined with scripts and automated distributed file maintenance methods such as rsync and rdist.

**Enumerating Domain Names**

With the archives generated on the Internet, searching on `www.google.com` and other sites (particularly those that cache) is an effective approach to enumerate server and domain names.

For example, suppose you did a search on `www.google.com` for `senate.com` servers. Your search would result in the enumeration of hundreds of `senate.com` servers. Similar searches for non-Web–based servers can be done by searching for specific banners or characteristics, such as "@" to find mail servers.

## Predictable query Ids

Busy name servers have the potential of servicing many requests at the same time. Because all communication occurs across the same port, a query ID is included within a packet to uniquely identify sessions. These numbers start at a set number generated by the server and increment with each request. A predicable query ID within a request is a security issue that allows an attacker to poison domain name server caches with forged address resolution information.

For example, an attacker can send a forward lookup query to a high-level DNS server requesting an IP address. In response, the DNS server sends a query on behalf of the client down to a lower-level server.

Simultaneously, the attacker floods the high-level DNS server with malicious responses to mimic what was expected from the legitimate low-level server. If the high-level server has implemented predicable sequences of query IDs, the server trusts this illicit response and places it in its cache for future reference.

When a DNS issues many queries at once, this attack could be used to poison large spans of domain names and redirect innocent users to incorrect sites.

As a result, newer DNS servers have been modified to use random query IDs to reduce the breadth of this attack.

## Recursion and iterative queries

DNS servers are designed to respond to two different types of queries: recursive and iterative. Recursive queries are from local *users* and iterative queries are from remote name *servers*.

Recursive queries are the most difficult for a name server to handle because the server is ultimately responsible for providing a final answer to the question. Recursive queries respond with either the requested address or an error.

Iterative queries, on the other hand, respond with a refer-to answer if the address is not currently known. The difference between the two becomes important later with security issues related to query types.

The process of a DNS request on the Internet begins with a recursive query arriving at a local name server. This server must either respond with the answer or respond with an error that an answer does not exist.

If the query name is not in the name server's cache, the current name server in turn asks the same question to a name server it knows of that most closely fits the requested domain. This query generated on the local name server could potentially be recursive, but that is considered to be in bad taste because it causes undue work on other servers that are not owned by the provider.

As is the nature of iterative queries, this name server will either respond with an answer, or refer the original server to a closer match. The process repeats until the original server receives an answer to the original query. [Figure 13-7](ch13.html#dns_servers_processing_a_recursive_query) depicts this event.

Although it is possible for the local server to send recursive queries to the external servers, in practice it is seldom done. Most queries that originate from a recursive query at a local name server are instead iterative, as depicted in [Figure 13-6](ch13.html#name_server_data_storage_for_fast_revers).

![DNS servers processing a recursive query systematically ask servers that appear to be the most likely to be knowledgeable about the requested address.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1307.png)

**Figure 13.7. DNS servers processing a recursive query systematically ask servers that appear to be the most likely to be knowledgeable about the requested address.**

# DNS Attacks

Because DNS is responsible for translating a domain name (which users prefer) to an IP address (which computers like), it is often a target of attack. If an attacker can go in and modify a DNS record so that it resolves to an incorrect IP address, they can cause all traffic for that site to go to the wrong computer. This section looks at some of the common attacks on DNS.

**DNS Vulnerability Statistics**

A Domain Health Survey for .com sites by `www.menandmice.com` illustrates the high likelihood of attack success on DNS servers.

- 68.4 percent were misconfigured.
- 27.4 percent have all name servers on the same subnet.
- 18.4 percent maintain records that point to an incorrect host.
- 16.1 percent lack the correct match of delegation data and zone data.
- 16.4 percent have nonresponding authoritative name servers.
- 43.3 percent block zone transfer from all name servers.

## Simple DNS attacks

DNS spoofing on a local network is the most simple and easy-to-implement name service attack. As illustrated in [Figure 13-7](ch13.html#dns_servers_processing_a_recursive_query), the victim attempts to view the Web site `www.download.com`. Because the victim has not been to the Web site recently, a cached entry of the IP address does not exist in the client's Address Resolution Protocol (ARP) table. Therefore, the victim's computer issues a query for `www.download.com` to its local DNS server.

The malicious attacker observes this DNS query and instantaneously a spoofed response is returned to the victim. On local networks it is trivial to identify this traffic because name servers are widely advertised. In addition, all traffic related to the request travels on UDP port 53. As a result, the victim receives the response from the malicious attacker before the DNS server is able to issue and receive responses from a recursive query to the true authority for `www.download.com`.

The first response received by the requesting victim "wins" and the secondary response is simply discarded.

## Cache poisoning

Attackers that reside on the same local network as the victim are able to execute simple "race" condition response spoofs to redirect traffic. When attackers are not able to reach local servers directly the exploitation method becomes slightly more complex. The most common technique to attack victims in this case is to poison the cache of their DNS server ([Figure 13-8](ch13.html#illustration_of_a_simple_dns_attack_that)).

![Illustration of a simple DNS attack that redirects traffic destined to www.download.com to a malicious site because the DNS query response from the attacker is received before the legitimate response arrives](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1308.png)

**Figure 13.8. Illustration of a simple DNS attack that redirects traffic destined to `www.download.com` to a malicious site because the DNS query response from the attacker is received before the legitimate response arrives**

Cache poisoning means that entries in the server have been maliciously modified although the victim continues to trust the responses supplied by the server. There are several methods of doing this, the first of which became publicly available in 1993 (see "[Implementation flaws that allow cache poisoning](ch13.html#implementation_flaws_that_allow_cache_po)" for more details).

One of the more difficult attacks to prevent against is the birthday attack, illustrated in [Figure 13-9](ch13.html#the_birthday_attack_method_of_dns_cache). The birthday attack method of DNS cache poisoning launches spoofed DNS queries and requests instantaneously with a valid user request. Mathematically, as the number of queries reaches 700, the possibility of a collision reaches nearly 100 percent. A *collision* occurs when the real number that was generated by the server and the guess are the same, which means the attacker successfully guessed the query and can spoof the response.

![The birthday attack method of DNS cache poisoning](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1309.png)

**Figure 13.9. The birthday attack method of DNS cache poisoning**

# Designing DNS

Unfortunately, when most companies set up an infrastructure, functionality is all that matters, not security. If you successfully set up a system and everything is working, you assume you are done. However, just because it is working does not mean that it is secure. Securing DNS requires that the system be properly configured and properly designed.

## Split DNS

Simply put, a split DNS design splits the address range of your network into internally and externally reachable zones. An internal server receives query requests from users and forwards them to an outside server that makes recursive queries on its behalf. Although this design protects against most exploitation related to application vulnerabilities such as buffer overflows, it does not protect against cache poisoning. While better than a single external DNS server, this design is not the most optimal approach and should be replaced with a split-split design, if possible.

### Note

A bastion host is a dual-homed server that has routable interfaces in both sides of a split namespace. This host operates as a gateway between the two, and is designed to protect against attacks against internal resources.

## Split-split DNS

Split-split DNS is the most recommended DNS system design. Using physical separation, it is capable of disabling recursive queries from the Internet on name servers that service your users. This design prevents external attackers from poisoning the DNS cache seen by internal resources.

Designing a split-split architecture means that you have two name servers. As [Figure 13-10](ch13.html#a_split-split_dns_architecture_uses_comp) illustrates, the name server on the left resides on your internal IP address subnet and does nothing but issue recursive queries for your users. The name server on the right serves public domain information for external parties and does not issue recursive queries.

![A split-split DNS architecture uses complete physical separation of internal recursive queries and external public name service to prevent DNS cache poisoning.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1310.png)

**Figure 13.10. A split-split DNS architecture uses complete physical separation of internal recursive queries and external public name service to prevent DNS cache poisoning.**

**Implementation Flaws that Allow Cache Poisoning**

Following is a list of implementation flaws that can contribute to cache poisoning. Such poisoning can be prevented with split-split DNS architecture:

- Secunia released an advisory (SA11888) that applied to Symantec Firewall products. The DNS caching engine trusted any answer received from a DNS server.
- The Brazilian Research Network CSIRT and Vagner Sacramento released an advisory (VU#457875) that applied a birthday attack to Berkeley Internet Name Domain (BIND). They demonstrated that it was mathematically possible for BIND to send multiple simultaneous recursive queries for the same IP address.
- CERT released an advisory (CA-2001-09) based on the paper that Michael Zalewski wrote entitled "Strange Attractors and TCP/IP Sequence Number Analysis." This was based on the ability to predict transaction ID/UDP port pairs.
- CERT released an advisory (CA-1997-22), which described a vulnerability in the BIND software that was released. This vulnerability had to do with the query IDs being sequential, which led to predictability and mass poisoning.
- Christoph Schuba authored "Addressing Weaknesses in the Domain Name System Protocol." This paper introduced the concept of cache poisoning, with the most notable vulnerability being the inclusion of additional information in a DNS reply packet.

# Master Slave DNS

Redundancy and load balancing requires that networks house more than one DNS server. However, as the number of servers increases, so does the amount of time required to administer them.

One method to reduce administration responsibilities is to implement *master* and *slave* relationships among them. With this plan, only one server (the master) must be manually configured with changes to addresses and domain names. All remaining servers (the slaves) receive their information in an automated fashion from other servers. This transmission of information is commonly referred to as a *zone transfer*, and was discussed previously in this chapter.

When configured, changes to zone files cause the maintainer of the change (generally the master) to send a NOTIFY announcement to its slaves. To identify if a slave server should be updated with new information, zone files contain an incrementing serial number. Each change of the file raises this number, which indicates a more recent copy. Slave servers that determine that their serial number is lower will request an update.

In general, updates to slave servers are only acquired from the master server. However, it is possible for them to acquire the information from each other. Precautions in terms of carefully changing DNS must be taken to ensure that transfer loops are not created by this configuration. For example, if a change is made to slave-server-1, and slave-server-2 acquires it but is told to send changes to slave-server-1, this process could loop infinitely.

# Detailed DNS Architecture

When selecting the proper DNS architecture for your organization, it is important to keep in mind the critical role that name translation plays. Without it, although firewalls and routers are functioning properly, your users' Internet service will become virtually useless. Redundancy is critical.

The most secure of all designs is to implement a split-split architecture. This design should incorporate no less than two internal DNS servers for every 500 users. Organizations that require multiple servers due to network size should space them out in a load-balancing manner to produce the most efficient architecture.

For users that operate over WAN or other long-distance connections, it is most efficient to locate servers within close proximity so that each query does not have to traverse across the distance of the WAN.

Policy must be set in place and followed to ensure that the DNS server software and its underlying operating system is maintained and kept up-to-date with patches and new software releases. A host-based intrusion detection system (HIDS) should be installed on the server and frequently monitored. Undetected compromise of this machine could lead to a malicious user preventing access as a denial-of-service attack, or worse, redirecting traffic to sites containing misinformation and trojaned software.

# DNS SEC

DNS SEC is an operational method, through the use of security related extensions to DNS, which allows for the authentication of DNS data, data integrity, and authenticated denial of existence.

Present day Internet access requires that a name resolution solution exist to assist in the assignment of appropriate Internet Protocol (IP) addresses to our Internet queries for services. This current process requires that only the client side of communication provide a destination indication, be it IP address or Fully Qualified Domain Name (FQDN), within its request to communicate. Either response will spawn a process known as reverse domain name lookup and provide systems communicating both the IP and FQDN. This process utilizes DNS settings to inquire about programmed Name Servers (NS) for the rest of the equation. If an NS does not know the answer, the query is forwarded up the hierarchal tree to the next NS in the tree to resolve the query, and continues to do so until an answer is found or the top (root) of the tree is found and a negative answer is returned.

Outside the programmed NS mapping, no validation of requests, be it the data of the query or the responses to the query, is conducted. This leaves a critical aspect or trust in the responses open for interpretation and attack.

DNS SEC follows the same programming aspect of normal DNS configurations, and enhances it with the addition of new resource records (RRs) and record types. It also attempts to alleviate the issue of authentication of data within the query or the trust nature of the name servers responding through the use of digital signing of answers/queries to DNS lookups. This digital signing is based upon the public-key cryptography in use today in other protocols.

To understand how DNS SEC enhances present-day DNS, let's recap the original DNS record types:

- **TTL**—Time to live in seconds
- **Class**—Currently only IN (Internet) is in use
- **RRType**—Type of resource
- **RData**—Resource information
- **A**—Address, typically the IP address of a host
- **MX**—Mail exchange
- **NS**—Name server

Now to allow for the ability to identify and validate data within individual queries or to identify and validate domain queries, we utilize new resource record types. These DNS SEC resource record types are as follows:

- **RRSIG**—Resource Record Signature is a digital signature of a DNS answer to a query.
- **DNSKEY**—The DNS Public Key (DNSKEY) is used to sign queries and responses.
- **DS**—Delegation or Designated Signer.
- **NSEC**—Next Secure (NSEC) is used to identify the non-existence of DNS owner names and types.

Additionally, new DNS header flags are required to allow for the identification of data checking and authentication use:

- **Checking Disabled (CD)**—Requests the answering DNS server not to validate the data, be it a query or results.
- **Authenticated Data (AD)**—Identifies the results (query or answer) as having been validated using the sender's key.

TSIG is transaction protection through hash-based message authentication codes (HMAC). This process can be simplistically referred to as transaction signing or signatures and is attached to the end of a query.

The sender commonly computes the hash of a DNS message, using the secret key, and encodes the results in a TSIG RR, which is appended to the end of the message. It includes the following:

- Name of hash algorithm
- Key identifier or name
- Timestamp
- Time in seconds for clock skew allowance

The following requirements must be taken into account for all DNS SEC–formatted messages:

- EDNSO (RFC 2671) support for larger DNS message sizes resulting from the addition of the new RRs.
- DNSSEC OK (DO) EDNS header bit (RFC 3225) used to indicate the request for DNS SEC RRs in response messages.

## Trust anchors and authentication chains

A key aspect in the use and validation conducted in DNS SEC is the identification of *trust anchors*. These sites are usually starting points and maintain known good public keys used to verify designated signer (DS) records which in turn are used to verify DNSKEYs in subdomains.

*Authentication chains* are nothing more than a series of linked DS and DNSKEY records from the trust anchor down to the authoritative name server of the query. An incomplete authentication chain may indicate a man-in-the-middle attack due to stripped data or inclusion of non-validated identities.

## The DNS SEC lookup process

Now let's see how a configured DNS SEC lookup would occur:

- An address is requested.
- DNS SEC resolver sets the "DO" flag bit in the DNS query. NOTE: this bit is what requires DNS SEC servers to support EDNS due to the larger packet sizes expected.
- When the resolver receives an answer, it attempts to verify the answer by verifying the DS and DNSKEY records against those located at the DNS root.
- The DS records for the query are then used to verify the DNSKEY records in the queried zone.
- Next the RRSIG record in the response is verified in the queried zone.
- There are several exception cases with the preceding example.
- If the queried domain does not support DNS SEC, there will not be an RRSIG or DS record for the queried zone in the DNS root zone.
- If a DS record for the queried domain exists, but there is no RRSIG record in the reply, the following may be occurring:An active attack that is modifying the A records.A non–DNS SEC name server along the query path stripped the DO flag bit or RRSIG record from the query.A misconfigured DNS SEC server exists in the path of the query.

If the queried domain does not exist, an NSEC/NSEC3 record is returned which can be verified through RRSIG records. An "island of security" exists if the queried domain exists but is not contained or registered with the root DNS SEC zone.

## Advantages of DNS SEC

DNS SEC is not expected to be the whole answer to securing the Internet, but it does afford the ability to verify that data is trustworthy; as a matter of fact the main advantage to DNS SEC is the ability to verify data. Through the use of the validation ability we gain methods to prevent or reduce the effectiveness of some of the following types of attacks:

- *DNS cache poisoning* attacks using forgery methods or redirection.
- *DNS hijacking* through spoofing routes or erroneous data and spoofed updates. Ability to sign zone transfers and allow only DNS SEC trusted authentication servers previously authorized by said site to request complete transfers of a particular domain. This eliminates rogue network discovery techniques.

## Disadvantages or shortfalls

Data viewing is still possible because DNS SEC was not intended to encrypt the actual payload. Interception of packages during transmission is subject to capture and may be used to identify network components through passive monitoring.

Spoofed packages may be successful, if the validation process is not maintained and implemented fully. Disregarding the validation process anywhere within a chain will disrupt the process.

Attacks made from within a network with direct access to a server in an authentication chain may disrupt the entire key signing and validation process of that particular chain. The requirement for physical and validated access to DNS servers must be implemented as well.

New attack vectors targeting the "CD" flag, e.g., attempting to set this flag causing recursive DNS servers to disregard the validation process for particular queries, can be exploited by an attacker. Understand that this type of attack *should not* affect DNS SEC servers set to only trust-particular servers and disregard non-DNS SEC settings/queries.

The requirement to maintain time synchronization may still lead to inadvertent Denial of Service (DoS) attacks, or allow another vector (time protocol) for attackers.

## How do we implement DNS SEC?

The actual implementation of DNS SEC is not extremely difficult. In most instances, additional software isn't required, only the use and implementation of new configurations for DNS queries by the DNS Servers, and the creation of public/private keys, and time synchronization with the appropriate TLDs (top-level domains), and registering zones within the authentication chains. Sounds simple doesn't it? But let's view a few of the basic steps towards the enabling of DNS SEC.

1. Establish an authoritative server directory structure and zone file naming conventions.
2. Enable DNS SEC on identified authoritative servers.
3. Enable DNS SEC on recursive servers.
4. Enable DNS SEC on each zone to protect.
5. Generate keys:ZSK—Zone Signing Key, used to sign data in zonesKSK—Key Signing Key, used to sign zone keys
6. Place keys into a "zonefile."
7. Sign your respective zone.
8. Configure the "named.conf" file of the signed zonefile.
9. Reload the zone.
10. Populate the tree by providing your zone DS records to the parent zone. Should parent zone not be configured to respond to DNS SEC inquiries, provide DNS SEC lookaside Validation (DLV) registry and DLV records to unaware parents.

## Scalability of DNS SEC with current internet standards

Because DNS SEC does not require additional software, but rather additional maintenance methods, DNS SEC can be made to work with current Internet standards. It will require dedicated monitoring and maintenance upkeep, e.g., monitoring of key rotations, signing of zones, and registering of zones with root level domains, as well as managing the ability to handle non-authenticated zones. The addition of these maintenance issues will lead to reluctance by some institutions to implement DNS SEC. Even though the initial setup is not that intense and difficult, the potential for out-of-sync keys, receipt of non-signed or validated information, or the denial of a zone to accept requests will slow the implementation of DNS SEC within the global community.

# Summary

DNS plays a critical role in an organization's security posture. Of all servers, DNS is the one that every organization must have if it want to allow people to use domain names to access their company's resources. This chapter laid out the fundamentals of DNS and what needs to be done to secure it.
