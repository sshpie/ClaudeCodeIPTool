# Chapter 10. Web Browser and Client Security

**IN THIS CHAPTER**

- **Exploring client risk from a Web browser**
- **Understanding Web browser operation**
- **Reviewing known Web browser attacks**
- **Operating a Web browser safely**
- **Understanding Web browser configurations**

Web browsers provide the face—the convenience and productivity—of the Internet. The vast majority of Internet users spend all their time with two applications—the e-mail client and the Web browser. Web browsers provide everything that has made the Internet useful and productive for millions of people. With the new style of malicious code, attackers are using browsers to infect a system. Because browsers easily allow executable content to run on a local system, it is simple for malware to infect a local system.

# Web Browser and Client Risk

In many ways, Web browsers are the ultimate in computer convenience. The Internet started out as an academic information exchange enabler. Then Web browsers made the Internet easy to use and allowed noncomputer-savvy companies and individuals to harness the power of information exchange and remote processing. Ever since the inception of the easy-to-use and pleasant-to-view Web browser, the Internet has taken off. In a few short years, it has landed in nearly every business and most homes throughout the United States.

The convenience, productivity, and popularity of Web browsers make them a prime target for hackers and would be attackers. As the convenience of a product increases, so does the security risk, so Web browsers by their very nature should be expected to be risky. The productivity of the Web browser also makes it a prime target for attacks because the hacker can get the biggest bang for the effort put forth. Finally, the popularity of a product plays into the hacker's hands by increasing the scope of any attack or vulnerability discovered. The hacker who develops an attack for a common Web browser is sure to find many susceptible targets.

## Privacy vs. security

More so than most applications on the typical user's workstation, the Web browser highlights the two related areas of concern—privacy and security. Security is concerned with the confidentiality, integrity, and availability of data. Privacy is concerned with the inadvertent disclosure of information. In some cases, this disclosure is the result of a security breakdown in confidentiality. But in many cases, the privacy violation occurs when users unwittingly disclose personal information. The convenience and productivity of Web browsers can lull users into providing information that they would not normally give to total strangers.

## Web browser convenience

As previously mentioned, with convenience comes security risks. This is very evident in the case of Web browsers. The first Web browsers only rendered HTML code and downloaded image files. This simple capability had some security risks that were not manifest until later years. Because most of these risks are a result of input and buffering vulnerabilities on the Web server, they are addressed in [Chapter 11](ch11.html), "Web Server Security."

Web browsers today provide a lot more features than simply rendering images and HTML code. Their convenience is greatly enhanced by their capability to do the following:

- Run Common Gateway Interface (CGI) scripts on the Web server
- Run scripts written in JavaScript or Visual Basic Script (VBScript) on the Web browser
- Run executables such as Java and ActiveX on the Web browser host
- Launch various plugins such as an audio player or movie player

In most cases, these conveniences come from a very tight integration between the Web browser and the operating system (or other applications). By far, the most convenient and integrated Web browser is Microsoft Internet Explorer. As such, it should also be viewed as having security risks. Therefore, users should expect that out-of-the-box configurations of Internet Explorer will be configured for user convenience. A security-minded user will want to examine this configuration and perhaps improve the security of the application.

## Web browser productivity and popularity

Convenience may introduce security risks into Web browsers, but it is the productivity and popularity of the browser that makes us susceptible to these risks. It is a Web browser's productivity that keeps users coming back to this application.

The more an application is used for critical or sensitive work, the greater the potential security risk to the user. Some of the most sensitive work users do on their workstations is done through Web browsers. Often users will do banking, credit card purchases, shipping to a home address, and hobby pursuits. The data involved in any of these activities would be of interest to an attacker.

But to be a prime target, an application must be more than just convenient and productive—it must be popular, meaning widely distributed and used. Hackers will focus their efforts on applications that will provide them with the largest source of potential targets. [Figure 10-1](ch10.html#convenient_comma_productive_comma_and_po) illustrates the unique combination of convenience, productivity, and popularity that makes a Web browser a favorite target for security attacks.

![Convenient, productive, and popular applications become targets.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1001.png)

**Figure 10.1. Convenient, productive, and popular applications become targets.**

## Web browser evolution

Web browsers, like most Internet applications, respond to emerging security threats. In the early years, Web browsers were very vulnerable. They had features making them convenient and productive but had no means for the user to make them more secure. Web browsers have evolved (due to the security threat) to a customizable application. Users are now able to set various configuration items to improve the security of their Web browsers.

The problem with highly customizable Web browsers, as a security measure, is that most users are not sophisticated and savvy when it comes to securing a Web browser or even understanding the threat. Often users will not change any of the browser's security configuration items. The customization, for security purposes, is then left to the system or network administrator. However, as discussed earlier, browsing has become such an accepted norm for convenience and productivity that few users will tolerate less than total functionality. As a result, administrators that initially attempt to secure browsers are often beaten back by the onslaught of complaints and requests for help. In the end, the administrator must relax the Web-browsing security settings.

## Web browser risks

The security risks associated with using a Web browser can be grouped into several categories:

- **The Web server may not be secure**. All the data that users enter into their browsers is ultimately processed on the Web server. In most cases, this information is stored in a database of some sort. Most typical users assume that a professional organization that is providing the service is security conscious. The best defense a user can have against an insecure Web server is to limit the sensitive data that is transmitted to the server.
- **The browser runs malcode in the form of scripts or executables**. The Web browser is a convenient and powerful tool that makes the user's life easier by running scripts and (in some cases) executables for the user. However, this feature could be abused and malcode could be run instead of useful routines.
- **An attacker may eavesdrop on network traffic**. Users should be aware that the security of the data transmitted to and from the Web server is no more secure than the security of the network on which it travels. This risk can be reduced when the Web server uses Secure Sockets Layer (SSL) to encrypt the data transmitted and received.
- **An attacker may employ a man-in-the-middle attack**. Sessionless Web-based applications, such as a Web server, are potentially susceptible to man-in-the-middle attacks such as hijacking and replay.

Session hijacking and replay occurs when traffic between the browser and server is observed and captured by a network sniffer. In the case of hijacking, the attacker modifies the captured traffic to allow the man in the middle to take the place of the client. All future traffic in the session is now between the Web server and the attacker. For the replay attack, some aspect of the session may be modified. Certain replays, such as transferring bank funds, may not require modifications. The modified session is then fed back onto the network. As a result, the Web server is fooled into believing that the replayed transaction is a legitimate action by an authorized user, clearly a security problem.

## Issues working against the attacker

Almost every browser and operating system combination is vulnerable, but a couple of factors work in the browser's favor. The following are some factors that slightly reduce the risk to the user:

- **The attacker cannot choose the time and place**. The nature of a Web browser and server interaction requires the user to come to the server. In the vast majority of cases, the server does not know who or when a user will connect with the server. This makes the planning of an attack slightly more difficult. It is very difficult for an attacker to focus on one particular individual. Because attackers cannot specifically target their victims, they have to take a victim of opportunity.
- **The attacker probably does not know the victim**. Because the attacker does not know who the victim will be, they may attack a sophisticated user and get discovered very quickly.
- **Browsers can vary**. Although there are two major browsers (Netscape and Internet Explorer), there is a fair amount of variety in the versions of each that are commonly deployed. An attack for one particular browser version may not be a risk to users using a different browser.

# How a Web Browser Works

Understanding how the browser and server work together can be helpful in understanding the need for security.

## HTTP, the browser protocol

Hyper Text Transfer Protocol (HTTP) is the main protocol of Web browsers. HTTP is the application layer protocol that enables the Web browser to request Web pages and send information (usually in forms) to the Web server. The Web server responds to the request and typically returns the following:

- **Hypertext Markup Language (HTML) code** — This is the code that provides the basis for everything that a Web browser typically displays. The Web browser interprets this code to display text in various forms and orientations. This code also has placeholders for scripts and links to images and perhaps executables. When a page is downloaded, the Web browser interprets the HTML code for further requests to be made. For example, when an image is to be downloaded, it typically is embedded in the HTML code. The Web browser recognizes the embedded link to the image and automatically sends another request to the Web server to get the image. After the Web server returns the image, the Web browser renders the image in the same location as the link.
- **Images** — An image can be requested directly by the user, or the Web browser can interpret a link in a downloaded page and send a request to the Web server. The image is returned in a file format. The Web browser must know how to render the file type. Typical image file types are GIF, JPEG, BMP, and TIFF, but there are many possibilities.
- **Scripts** — Scripts are typically embedded in the HTML code. The Web browser extracts the script from the HTML and runs the script. There are a number of scripting languages and the Web browser must know how to interpret the scripts. Some typical scripting languages include JavaScript, PerlScript, and Visual Basic Script.
- **Executables** — The Web browser can download and launch executables. This obviously is a security risk, because most Web servers are managed by strangers to the Web-browsing user. It is ironic that users who would closely guard their workstations from strangers would also download and run executables written by strangers.

In theory, there is no limit to the type of information that can be passed between the Web browser and the Web server. All that is required is that the Web browser and Web server agree as to how a particular file type will be interpreted.

The most unusual feature of HTTP is that it is a "stateless" protocol. Essentially, each browser request and server return is a separate TCP connection. This is not at all intuitive to the user because the Web browser and server work in concert to give the user a "feel" of continuity during a session. *Session* in this chapter is a loosely defined term meaning a whole series of transactions (requests and responses) that are logically tied together in the user's mind. [Table 10-1](ch10.html#a_simple_http_session) shows the difference between what the user thinks is happing and what is really occurring between the browser and server.

From the session described in the table, you see that the Web server sends an initial Web page (`index.html`) and sends the subsequent images as the Web browser requests them. Note that the Web server does not control when the images are sent, the browser does. In fact, the Web server does not even anticipate the sending of the images because to the Web server, the request for the images is completely separate from the request for the initial page (`index.html`). The Web server does not maintain a state of what the Web browser (or user) is doing. It merely responds to requests in any order that the Web browser sees fit to request them. This is what is meant by the HTTP protocol being stateless. Each and every piece of a Web page is a separate connection or transaction (request and response).

## Cookies

A *cookie* is an information storage device created by a Web site to store information about the user visiting that site. This information is stored for the convenience of the Web site or for the convenience of the user. In any case, the retention of potentially sensitive or private information is a possible privacy concern.

A cookie is simply an ASCII file that the server passes to the client and the client stores on the local system. When a new request is made, the server can ask the browser to check if it has any cookies and, if it does, to pass those cookies back to the server. The browser can potentially pass *any* cookie to a Web server. This could include cookies from completely different Web sites.

The contents of the cookie are under the control of the Web server and may contain information about you or your past and present surfing habits. Originally, the information that the Web server has came from the Web browser. When a user fills out a form with a name and e-mail address, that information is sent to the Web server, which may store it in a cookie for future use.

There are two general types of cookies: persistent and nonpersistent. A persistent cookie is one that will survive reboots and last for a fairly long period of time. Persistent cookies are traditionally stored on the hard drive in a file such as `cookies.txt`. This file can be read and edited by the user or system administrator. This file may contain sensitive data unbeknownst to the user. If at some future date the workstation is compromised, an attacker can use this sensitive data in subsequent attacks. Because the cookies file can be modified, it is also susceptible to being used in a hijacking or replay attack.

**Table 10.1. A Simple HTTP Session**

| User Perception | Browser and Server Activity |
| --- | --- |
| User opens the Web browser, types `www.my-family.tmp` into the navigation window, and presses Enter. The Web page is displayed with some text and family photos. | The following steps are taken by the Web browser to ultimately display the Web page that the user expects: The browser contacts a domain name server to get the IP address of `www.my-family.tmp`. The browser uses IP addresses when communicating on the Internet, not the domain name itself.The Web browser opens a TCP connection to the IP address on port 80. This is similar to telneting to that IP address on port 80. The Web server is listening for the connection.The Web browser sends the initial request to the server, as follows: `http1.1 GET /`. The slash (/) is used in the initial request because no subdirectory was given by the user.The Web server looks in the document root directory (/) and most likely sends the ASCII file `index.html` back to the Web browser. |
| The user sees the Web page starting to display. Typically, this starts with a color change or the rendering of some initial text. | As the `index.html` file is downloaded, the Web browser interprets the HTML code for display parameters such as the following: The Web page size and color is set.The browser displays any text with appropriate formatting, such as bold or centered.Any scripts, such as JavaScript, are extracted from the HTML code and associated with a button or mouse movement.The Web browser parses through the HTML code looking for links to other files to download. In this example the browser finds links to images. |
| The user sees images being downloaded and displayed. The Web browser is interpreting the initial HTML downloaded and requesting the images. But from the user's perspective, the images seem to come down with the original response. | The Web browser parses all the links to images in the HTML code and submits a separate request to the Web server for each image. Note that the Web server has not sent the images down with the `index.html` page. It is the Web browser's responsibility to interpret the HTML code and request the images. |

Cookies originally were intended to track users during their sessions on a Web site, or to retain information about users between visits to the Web site. However, persistent cookies built up on a user's workstation over a long period of time can comprise a detailed history of the user's activities on the Internet. In the past, some marketing companies have attempted to exploit user behavior by trying to capture these persistent cookies.

As a result of concerns, more and more people are wary of cookies, especially those that can be used to track users over time. Therefore, many sites are starting to use nonpersistent cookies. A nonpersistent cookie is stored in memory, so when the computer is turned off or rebooted the cookie information is lost. There is no assurance that every browser will handle every instance of nonpersistent cookies correctly. The Web server has no control over how the browser stores or disposes of the cookies. The Web server can tag a cookie as nonpersistent, but then has to trust that the Web browser will honor the tag.

For maintaining state purposes, nonpersistent cookies would work just fine because you only need to track a user during a session, which will not span a reboot of the workstation.

Cookies generally contain information that allows the Web site to remember particulars about users visiting the site. A popular scheme is to include the following information in cookies:

- **Session ID** — This is typically used to maintain state or carry authorization information forward between browser requests.
- **Time and date the cookie was issued**.
- **Expiration time and date** — This can be used by the Web site to determine if this is an old cookie that should be ignored.
- **The IP address of the browser the cookie was issued to** — This can serve as an additional test of the authenticity of the request.

## Maintaining state

A Web-based application that deals with sensitive data has three major security issues to address in its design and development:

- **Initial authentication** — When needed, authentication is usually done with a username and password. As long as a strong password is used and the network data is encrypted, the initial authentication can be made secure.
- **Confidentiality of data** — This is usually done with encryption. With a sufficiently strong encryption technique, only the legitimate recipient of the data should be able to decrypt the traffic.
- **Continuing authentication of users over an extended session** — Also known as maintaining state, this is the biggest risk for a Web-based application such as a Web server. The reason the risk is high is that there is no normal or preferred method to provide continuing authentication of users over an extended session. Off the shelf, Web servers do not provide a secure means for a Web site developer to maintain state securely.

The continuing authentication of a user over an extended session is done as a matter of convenience for the user. Without the continuing authentication, the user would have to provide a user name and password for *every* request submitted to the Web server. In other words, as users navigate the various Web pages of the application, they would be constantly entering a user name and password. For a typical Web page, this could mean providing the user name and password hundreds of times an hour (recall from earlier discussions that every image is a separate request and response).

For a Web server to be useful and convenient to a user, it must interact with the user much as an intelligent clerk or sales person would. To act intelligently, the Web site should do the following:

- **Remember user-specific information**. The Web site should not ask for the same information twice. When provided a user's name and address, the Web site should remember this information from one page to the next.
- **Remember decisions the user has made**. If the user has set some preferences (such as sort by lowest price) the Web site should remember these preferences during the user's entire session.
- **Remember intermediate results**. The typical example of this is the shopping cart. As users select items to purchase, they can store these items in a shopping cart until they decide to check out and purchase the items. Clearly, the Web site needs to remember the items in the shopping cart while the user navigates around the site.
- **Remember where the Web site and the user are in a "conversation."** As users navigate a site, the Web server needs to know where they are and how they got to that location. For example, certain locations on the Web site may require password authentication. The server needs to know if a user has previously successfully authenticated during this session before allowing access to these pages.

Remembering all this state information means that data will have to be passed from Web page to Web page. There is no usual method of maintaining state. The burden of continuing authentication is left up to each Web site implementation. As a result, some sites will be secure, but many will not. Most Web site developers focus on performance and content, not security. Therefore, many schemes that are implemented for maintaining state are ideal for user convenience but might be susceptible to attacks.

Because HTTP is sessionless, the Web server does not carry an authentication forward from one page to the next. The Web site developer must use what is at hand to maintain state. The three common means of continuing authorization (carrying session data forward) are as follows:

- **GET lines** — The GET line holds the Universal Resource Locator (URL), which is the Web site requested by the user (such as `www.my-family.tmp`). In addition to the domain name and directory requested, other information can be passed on the GET line. This information is passed in the form of `? <variable>=<value>`. Consider the following GET line, which conducts a Yahoo search on the keyword of "linux": `http://search.yahoo.com/search?p=linux`In this case, Yahoo uses the variable `p` and the data passed is `linux`.
- **POST data** — In addition to the GET line, variable information can be passed from the browser to the server with a POST command. These variables and their data are not so easily seen by the user because they are transmitted behind the schemes. POST data is slightly more difficult to acquire and modify. However, you can easily write a tool to do so within a couple of hours. The SSL encryption would prevent the modification of POST data but would still leave open the possibility of session replay. The form used for POST data is in the HTML code as a hidden form element. Because the information is marked hidden, the browser never displays it. The values can be seen with a network sniffer, but if viewed through the browser, the information is not displayed.
- **Cookies** — Information is put into a cookie by the Web server and passed to the Web browser. The Web browser then returns the information to the Web server with subsequent requests. Cookies are easily acquired and modified, both on the user's workstation and on the network. You will see later in this chapter that cookies used for maintaining state are susceptible to hijacking and replay attacks.

## Caching

When you access a Web site, your browser may save pages and images in a cache. Web browsers do this for the convenience of the user by improving the speed at which Web pages are rendered. However, all these pages and images are stored on the workstation's hard drive as HTML files and image files. The user or system administrator can load and view these pages and images without the need to be on the network or to go back to the original site. This can be a privacy concern because if the workstation is compromised, the attacker can learn details of a user's browsing.

The Web browser also maintains a history of sites visited. If you do not clear the cache and history files, anyone can view the sites accessed simply by using the back button on the browser.

## Secure Socket Layer/ Transport Layer Security

The Secure Socket Layer (SSL) and Transport Layer Security (TLS) protocol provides for the encryption of the traffic between the Web browser and server. SSL uses public-key encryption to exchange a symmetrical key between the client and server; this symmetrical key is used to encrypt the HTTP transaction (both request and response). Each transaction uses a different key. If the encryption for one transaction is broken, the other transactions are still protected.

The following are the benefits of encrypting Web-based communications:

- **The communications can travel over nonsecure networks**. The traffic between a browser and a Web server may traverse many networks as it travels across the country or around the world. It would be cost prohibitive for each Web site provider to ensure the security of all networks between the Web server and the user's browser. With encryption, the risk of a man-in-the-middle attack is greatly reduced because the attacker cannot decrypt the traffic (in a reasonable timeframe). This benefit assumes that SSL is properly configured and used.
- **The integrity of the data transmitted is maintained**. Encrypted data ensures the integrity of the data because the decryption process requires that not even one bit is "flipped" or out of place. If the encrypted data has been altered in any way, it will not decrypt properly. This allows a user to be sure that when they send someone an electronic check for $100, it does not get altered to $100,000.
- **The confidentiality of the data being transmitted is ensured**. If a third party is listening to the traffic between the browser and the Web server, they will only see the encrypted data. Assuming the encryption cannot be broken in a reasonable time, this ensures the confidentiality of the data.
- **The Web site's authentication can be enhanced**. The process of exchanging encryption keys and certificates can provide assurance that the browser is communicating with the proper Web site. The degree of security depends on the method used to exchange the key or certificate.

Netscape introduced the SSLv2 protocol in 1995, and the protocol has provided consumers with a secure means for conducting Web commerce. Additionally, Web-based applications that deal with sensitive or private data could now be made available to the general public. The growth of the Internet in the late 1990s probably would not have been possible without a secure and reliable protocol such as SSL.

Encryption can go a long way in maintaining the integrity and confidentiality of the data in a Web-based transaction. The price for encryption is performance or the cost of additional hardware and software. Additional hardware may be needed to increase the bandwidth and improve the performance of the Web server or application.

### A typical SSL session

SSL is a low-level encryption scheme used to encrypt transactions in higher-level protocols such as HTTP, Network News Transfer Protocol (NNTP), and File Transfer Protocol (FTP). SSL is implemented commercially on all major browsers and servers.

To pass encrypted data, two parties must exchange a common key. The keys are exchanged using certificates and a handshaking process, shown in [Figure 10-2](ch10.html#the_ssl_handshake_process). The handshaking process is as follows:

1. The browser or client requests a certificate from the server. In essence, a certificate is a set of fields and values encrypted into a small block of ASCII text. The certificate is encrypted to avoid tampering, thus ensuring its integrity.
2. The server provides its certificate. The server's organization has acquired the certificate from a reliable and trusted certificate authority. The certificate authority verifies that the server's organization is who they say they are. In other words, only the Microsoft Corporation should be able to get a certificate for "Microsoft."
3. Having received the certificate, the browser checks that it is from a reliable certificate authority (CA). The certificate contains the Web server's public key. The Web browser now sends a challenge to the server to ensure that server has the private key to match the public key in the certificate. This is important because someone who has the certificate could be pretending to be that organization. This challenge contains the symmetrical key that will be used to encrypt the SSL traffic. Only the owner (possessor) of the private key would be able to decrypt the challenge.
4. The Web server responds to the challenge with a short message encrypted with the symmetrical key. The browser now is assured that it is communicating with the proper organization and that the Web server has the symmetrical key.
5. Both the browser and the Web server now share a common symmetrical key. No one other than these two parties knows what the key is, so the encrypted communications between them should be secure.
6. Now any GET or POST sent from the browser can be encrypted with the symmetrical key. The Web server uses the same symmetrical key to decrypt the traffic.
7. In the same manner, any response sent from the server is encrypted with the common symmetrical key and the browser can decrypt the traffic.

![The SSL handshake process](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1002.png)

**Figure 10.2. The SSL handshake process**

Note that the SSL handshake process authenticates the Web server to the browser, and not vice-versa. This makes SSL more susceptible to a man-in-the-middle attack. During such an attack, the server would have no indication that there is a man in the middle. The browser or user will, however, have to accept a bad certificate for the attack to work. The security of the overall process would be greatly enhanced, if the Web server authenticated the client. The Web server would be less likely to accept a bad certificate, whereas unsophisticated users may not appreciate the risk they are taking by doing so.

A properly configured Web browser will warn the user of a certificate problem if any of the following occur:

- **The certificate was not signed by a recognized certificate authority**. Software is available in the public domain to create a rogue CA and generate illegitimate certificates.
- **The certificate is currently invalid or has expired**. Legitimate Web sites will keep their certificates up to date. This may indicate that the certificate has been stolen and is being used by a third party.
- **The common name on the certificate does not match the domain name of the server**. The host name of the Web server is a fixed part of the site certificate. If the name of the Web server doesn't match the name on the certificate, the browser will report the problem.

If a problem has been identified with the certificate, the user is prompted whether or not to accept the certificate. If the user accepts a bad certificate, he or she is exposed to a possible man-in-the-middle attack by someone impersonating the Web server.

### SSL performance issues

The negative impact that SSL can have is on performance and cost. The following is from an SSL FAQ:

```
How will SSL affect my machine's performance?

The performance problems associated with most HTTP servers are CPU and
memory related (this contradicts the common assumption that it is always
the network which is the problem). The CPU has to process the HTTP
request, write out HTTP headers, log the request and put it all on the TCP
stack. Memory bandwidth is also a problem (the OS has to make a lot of
copies to put packets onto the network). SSL makes this bottleneck more
severe:
    Bandwidth: SSL adds on average 1K bytes to each transaction. This is
not noticeable in the case of large file transfers.
    Latency: SSL with client authentication requires two round trips
between the server and the client before the HTTP session can begin. This
typically means at least a 500 ms addition to the HTTP service time.
    Bulk Encryption: SSL was designed to have RC4 and MD5 in its cipher
suite. These run very efficiently on a 32-bit processor.
    Key Exchange: This is where most of the CPU bottleneck on SSL
servers occurs. SSL has been optimized to require a minimum amount of RSA
operations to set up a secure session. Avoid temporary RSA keys which can
cause a massive performance hit.
```

Netscape has published figures suggesting that the throughput (in hits per second) of an SSL-enabled server is as low as 20 percent of that of an unencrypted server. The greatest performance hit occurs when the server and client exchange handshake messages for authentication and key generation/exchange. These operations are performing computationally intensive public key operations. Subsequent hits use the session restart feature of SSL. This enables the server and client to simply use the previously negotiated secret key.

# Web Browser Attacks

Web browser attacks are pretty typical of Web-based applications in general. The attacks can be summarized as follows:

- **Hijacking** — This is a man-in-the-middle attack in which the attacker takes over the session.
- **Replay** — This is a man-in-the-middle attack in which sent data is repeated (replayed) leading to various results.
- **Spread of malcode (viruses, worms, and so on)** — The scripting nature of Web browsers makes them prime targets for the spread of malcode.
- **Running dangerous executables on the host** — In some cases, the browser may permit executables to run on the host workstation. This can be very risky.
- **Accessing host files** — Certain attacks allow the browser to send files to an attacker. These files may contain personal information, such as banking data, or system information, such as passwords.
- **Theft of private information** — Browsers are at risk of disclosing sensitive information to strangers on the Internet. This information may be used in identity theft or to conduct a social engineering attack.

## Hijacking attack

Session hijacking occurs when an HTTP session is observed and captured by a network sniffer. The attacker modifies the captured traffic to allow the attacker to take the place of the client. All future traffic in the session is now channeled between the Web server and the attacker.

The hijacking is usually done after the legitimate user has authenticated to the Web server. Therefore, the attacker does not have to re-authenticate (usually for the remainder of the session). In this way, the attacker bypasses one of the major security features of the Web-based session, the initial authentication.

The hijacking attack exploits a weak method of maintaining state. If the attacker can understand how state is maintained, they may be able to inject themselves into the middle of the session by presenting a valid state.

One typically weak method of maintaining state is using cookie data to maintain state. In this method, the user is initially authenticated (usually with a user ID and password). If the authentication is successful, the Web server sends a session cookie to the user's browser. Now every time the browser hits that same Web server (presumably during the same session), the user does not need to enter the password, rather the cookie re-authenticates for the user. [Figure 10-3](ch10.html#hijacking_when_cookies_maintain_state) illustrates a hijacking attempt to exploit this weak method of maintaining state.

![Hijacking when cookies maintain state](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1003.png)

**Figure 10.3. Hijacking when cookies maintain state**

## Replay attack

Session replay occurs when an HTTP session is captured by a network sniffer. Some aspect of the session is then modified (certain replays, such as transferring bank funds, may not require modifications). The modified session is then fed back onto the network. If the replay is successful, the Web server will believe the replayed traffic to be legitimate and respond accordingly. This could produce a number of undesirable results. [Figure 10-4](ch10.html#replay_attack-019) illustrates session replay.

The responsibility is on the Web server to prevent replay attacks. A good method for maintaining the session will also prevent a replay attack. The Web server should be able to recognize replayed traffic as no longer being valid.

## Browser parasites

A browser parasite is a program that changes some settings in your browser. The parasite can have many effects on the browser, such as the following:

- Browser plugin parasites may add a button or link add-on to the user's browser. When the user clicks the button or the link, information about the user is sent to the plugin's owner. This can be a privacy concern.
- Browser parasites may change a user's start page or search page. The new page may be a "pay-per-click site," where the owner of the browser parasite earns money for every click.
- Browser parasites may transmit the names of the sites the user visits to the owner of the parasites. This can be used to formulate a more directed attack on the user.

![Replay attack](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/1004.png)

**Figure 10.4. Replay attack**

A typical browser parasite is the W97M_SPY.A. Once installed, this parasite hides from the user and stays resident in the background. This spyware macro program originated in France. It steals e-mails and addresses from the user's contact list and then sends the information to a hacker's e-mail address. The W97M_SPY.A can be manually removed by editing the Registry for the key:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
```

Then delete the key value:

```
Spy='%winsysdir%\Spy.vbs'
```

Finally, the user needs to find and delete the files W97M_SPY.A and VBS_SPY.A.

# Operating Safely

Learning to operate a Web browser safely is a tall order with all the attacks that are possible today. Even if users manage to configure their browsers for the safest possible operation, they are still at risk in how they navigate the Internet and how they respond to certain circumstances.

For example, the most secure browser settings won't improve your security unless you respond appropriately to any prompt dialog boxes that come up. If the prompt asks if an ActiveX control should be run, the user must decide to completely trust the site and click OK. If the user chooses poorly, a dangerous ActiveX application can bypass all the security features and run on the user's host workstation.

If users do configure their browsers for strong security, they will experience the brunt of the security versus convenience dilemma. The user will be constantly barraged with requests to accept cookies, scripts, and other features such as ActiveX. Under this constant barrage, the typical user will give in and loosen the security settings.

Users can take a number of steps to increase the security of their Web browser. Users should evaluate the risks based on their own circumstances and decide which steps are appropriate for them. These steps include the following:

- Keeping current with patches
- Avoiding viruses
- Using secure sites for financial and sensitive transactions
- Using a secure proxy
- Securing the network environment
- Avoiding using private information
- Taking care when changing browser settings

## Keeping current with patches

The Web browser is one of the favorite targets for hackers trying to find security flaws. There is far too much activity regarding Web browser security for the typical user to keep on top of the issues. Users must, therefore, rely on vendors such as Netscape and Microsoft to keep up with the security vulnerabilities of their products. These vendors must then make updates and patches available to users in a timely manner.

Regular updates and patches are available for high visibility Web tools such as the Web browser. These updates will include patches to recently found security flaws. Users should check for updates and patches on a regular basis.

For example, the Internet Explorer High Encryption Pack provides 128-bit encryption, the highest level of protection Microsoft can offer for Internet communications, including credit card use and financial transactions.

## Avoiding viruses

Many of the worms and viruses today will attack the Web browser because of its ability to propagate malcode. To maintain the overall security of the Web browser, it is important for the user to maintain a virus-scanning program running on the workstation.

As with all security tools, it is important that the virus protection software be kept up to date with patches and updates.

## Using secure sites

SSL adds significant advantages to securing Web browser transactions and data (as discussed earlier in this chapter). These added benefits make SSL a must for any Web sites using sensitive, private, or financial data.

There should be no acceptable excuses for not using SSL. All major browsers support SSL. On the server side, SSL is more expensive and only slightly more difficult to implement and maintain. Any security-conscious software development organization will invest in the SSL capability to provide the added protection to the users of their product.

An alarm should go off in the head of any user asked to enter any of the following data in a Web site not running SSL:

- Social Security Number (SSN)
- Addresses, including home, business, and shipping addresses
- Phone numbers, including home, business, cell, and fax
- Credit card information
- Personal identification numbers (PINs)
- Financial data—this can include banking account numbers
- Secondary identification information, such as mother's maiden name, high school, favorite pet, and so on

Attackers can use the information listed in the preceding list to steal a person's identity. Identity theft is a far too common occurrence. As the world's economy moves more and more to doing business on the Internet, it is expected that identity theft will become more of a risk.

A user may have faith or trust in an organization when dealing with them face to face, such as a local branch office of a bank, but this trust should not be extended automatically to any online capability that the organization offers. A personal trust of the organization is not sufficient reason to provide them personal financial information if they don't handle it correctly. Following are some aspects of the security risk to keep in mind:

- As an individual, you may not be a target. But as an Internet-based organization, the site you are dealing with is a big target, particularly if it is gathering personal or financial data on you.
- The Web site can be attacked at an organization's database. This risk is only slightly reduced with the use of SSL, but if the organization cares enough to use SSL, they are probably taking steps to improve their database security.
- The Web site can be attacked as the data transits to (and from) the Web site. There are probably a few hops between the user and the Web site. At each hop along the way, there may be a dozen persons with administrator or root access to the routers and gateways. That all adds up to a large number of people to trust. SSL virtually protects the user's sensitive data from all these administrators.
- The Web site (or organization behind it) can be attacked in an organization's local network. Organizations often overlook the insider threat. The use of SSL will protect the data during transmission even against a local network administrator.
- The Web site (or organization behind it) can be attacked with social engineering. The social engineering attack could yield access to many resources in the organization. The use of SSL will protect against an attacker gaining access to the local network.

When using a Web site secured with SSL, the Web browser will provide a visual indicator that the site is secure. With Internet Explorer a little closed padlock will be displayed in the lower right-hand corner of the browser window. With Netscape, a padlock can be seen in the lower left-hand corner of the browser.

The level of encryption can be determined on Internet Explorer by clicking the Help menu and then selecting About Internet Explorer. This will show the version of the browser and the level of security. In Netscape, if the key has one large tooth, it means that you have 40-bit encryption software. If the key has two large teeth, it means you're using 128-bit encryption. If the browser is not using 128-bit encryption, it should be upgraded immediately.

## Securing the network environment

The most securely developed application is still vulnerable if placed in an insecure environment. Therefore, it is important to have the security of the environment match the sensitivity and criticality of the application.

By way of an example, the following are general requirements for an application or system that processes credit cards:

- Install and maintain a working firewall to protect data.
- Keep security patches up to date.
- Protect stored data.
- Encrypt data sent across public networks.
- Use and regularly update antivirus software.
- Restrict access on a need-to-know basis.
- Assign a unique ID to each person with computer access.
- Don't use vendor-supplied defaults for passwords and security parameters.
- Track all access to data by unique ID.
- Regularly test security systems and processes.
- Implement and maintain an information security policy.
- Restrict physical access to data.

## Using a secure proxy

A proxy server provides a secure gateway for one (or more) protocols. All Web-browsing traffic destined for the Internet must pass through the Web proxy. The use of a secure Web proxy provides a number of advantages, as follows:

- **Some of the security features may be moved from the browser to the Web proxy**. It is often easier for a network administrator to manage a proxy than to manage hundreds of individual browsers.
- **The security features of the proxy will work for all versions of browsers**. All browsers support the use of a Web proxy. Suppose the security administrator wants to implement a security control such as blocking all ActiveX. It is easier to do it on a single proxy as compared to determining how to implement this control on every different version of browsers on the network.
- **The proxy may improve Web-browsing performance by caching frequently used sites**. There is usually a sufficient increase in performance to make up for the extra processing needed to browse through the proxy.
- **Proxies can be particularly useful with children to restrict sites and prevent the leakage of private data**. This is a big concern when considering the welfare of children.

## Avoid using private data

Anytime sensitive or private information is put on a system that is outside the user's complete control, there is a risk of that data being compromised. A lot goes into having a secure Web site that can protect the user's personal information. For example, the Web site organization must do the following:

- Develop a safe Web-based application.
- Properly configure and maintain database security.
- Harden the Web server's host.
- Secure the network on which the Web server resides.
- Establish policies and procedures for handling sensitive data.
- Hire responsible people and provide them adequate training.

Obviously all of these steps are out of the control of Web browser users, who want to be assured that their private data is handled safely.

For example, the Web site may not protect the logs for the Web server, leaving the logs open for casual viewing by anyone with access to the network. The GET requests will appear in the server log files. Depending on the Web site, sensitive information may be passed on the GET line. It should be noted that POST requests do not get logged.

The best defense for the user is to avoid using sensitive and private data whenever possible.

## General recommendations

The following are recommendations to improve the Web browser security or reduce the security risk while browsing on the Internet.

- **Be careful when changing browser configurations**. Do not configure a command line shell, interpreter, macro processor, or scripting language processor as the "viewer" for a document. This shifts control to the creator of the file. The Web server determines the type of a document, not the browser. Do not declare an external viewer for any file that contains executable statements.
- **Don't configure to support scripts and macros**. Do not configure an external view to be any application that supports scripts and macros, such as Excel and Word.
- **Never blindly execute any program you download from the Internet**. When possible, download scripts as text and examine the code before running the script.
- **Browse to safe places**. A user's risk of getting malcode and parasites can be greatly reduced by avoiding hacker and underground sites.
- **Be conscious of the home page configuration**. Every time you bring up the browser, which for most people is every time they start their machine, some Web sites will know it. The tracking of users in this manner is low risk. Consider setting the home page to be blank.
- **Don't trust links**. Be suspicious of everything. Get into the habit of reading where the link is before you blindly click.
- **Don't follow links in e-mail**. E-mail is easily spoofed, meaning the mail may not be coming from the person on the From: line. A legitimate business, such as your bank, will not send an e-mail to its clients and ask them to click to log in.
- **Avoid browsing from systems with sensitive data**. If possible, use a less risky workstation to browse the Internet. This less risky workstation should not have sensitive and private data on it.
- **Guard your information**. If possible, don't use personal information on the Web.
- **Use stronger encryption**. Choose 128-bit encryption over 56 or 40 bit.
- **Use a less common browser**. Because most hackers are trying to exploit Netscape and Internet Explorer, some security can be gained by using another browser.
- **Minimize use of plugins**. JavaScript, Java, and ActiveX all have vulnerabilities and should be avoided, if possible.
- **Minimize use of cookies**. Private or sensitive data might be extracted from a Web browser through cookies.
- **Be conscious of where temporary files are stored and how they are handled**. These temporary files may hold private and sensitive information. Make sure the files are not on a shared directory. If possible, set the browser to clear the history of saved files and locations visited to zero or one day. Learning about a user's Web-browsing habits can be a valuable aid in conducting a social engineering attack.

# Web Browser Configurations

In addition to operating a Web browser safely, configuration items can make Web browsing more secure. The configuration items concern the use of cookies and plugins. Additionally, each vendor has some browser-specific configuration issues.

## Cookies

Cookies are small text files that are sent to Web browsers by Web servers. A cookie's main purpose is to identify users and to present customized information based on personal preferences. Cookie files typically contain information such as your user name, password information, or ad-tracking information.

Because cookies are simple text files, they cannot contain viruses or execute applications, and they cannot search your hard drive for information, or send it to Web servers. Most of the information in a cookie is simple tracking information designed to provide enhanced customer convenience.

Cookies are generally not a security threat. However, they can pose a privacy concern. Any information that a user has ever entered into a browser may be stored in a cookie. All of that information may then be shared with every Web site the user visits. Clearly, this is an exaggerated worst-case scenario. A good browser will provide some control over cookies to greatly mitigate this risk.

Cookies cannot be used to search the workstation for sensitive information. Rather, they can only store information that the user has previously provided to a Web site. One of the best ways to avoid the loss of privacy through cookies is to not put private and sensitive data into the browser in the first place.

Some configuration items that can be set on the Web browser to mitigate the risk of a loss of privacy due to cookies are as follows:

- **Turn off all cookies**. Some Web sites will fail if cookies are disabled completely. Some conveniences will be lost, such as keeping a shopping cart while the user continues to shop on the Web site. Also, some banking sites may not operate without cookies. If the user has disabled all cookies and encounters the need for them on certain sites, cookies can be enabled just for those sites. The difficulty is being able to recognize that the site is not functioning properly because cookies are disabled. In some cases, when a site is dependent on cookies to function, the site may attempt to send the cookie over and over again. In this circumstance the user must weigh the privacy risk with the convenience of using that particular site.
- **Limit the Web sites that can set cookies**. The browser can be set to ask the user if any particular cookie should be accepted. In this way, the user can decide in each case if the information put into the browser for that particular site poses a privacy risk. In most cases, when prompted to accept or reject a cookie, the user has an option to accept all future cookies from this Web site.
- **Only return cookies to the originating domain**. Cookies originate (are sent to the browser) from a Web server. The browser can refuse to send these cookies back to any Web site other than the one that created the cookie in the first place. This will mitigate the risk of a third-party site trying to get private data on a user.
- **Force all cookies to be nonpersistent**. Nonpersistent cookies are deleted after they are no longer needed. In some cases, this is when the browser is closed. It would be very unusual for a Web site to require a persistent cookie on the user's browser. Many Web sites do use persistent cookies as a matter of convenience for the user, but the sites perform just as well without the cookies being persistent.
- **Clean out persistent cookies**. Periodically, go into the browser settings and delete any persistent cookies.

## Plugins

Java, JavaScript, and ActiveX controls are used by many Web sites to make Web browsing convenient and powerful. However, with added convenience comes a greater security risk. Java and ActiveX are executable code that you download and run on your local computer. JavaScript is a scripting language that is downloaded and executed.

ActiveX is more dangerous than Java or JavaScript. ActiveX can make system calls that can affect the files on your hard drive. With ActiveX controls, new files can be created or existing files can be overwritten. There are many files that control the workstation that should not be alterable by some stranger on the Internet.

Many users are not aware of the differences between Java and JavaScript. Java is a language designed by Sun Microsystems which results in executable code. Java code is compiled into applications known as Java applets. Browsers that support Java applets will download the compiled Java applications and execute them.

JavaScript (or Jscript) is a series of extensions to the HTML language designed by the Netscape Corporation. JavaScript is an interpreted language that executes commands on behalf of the browser. The scripts have the ability to open and close windows, manipulate form elements, adjust browser settings, and download and execute Java applets.

### ActiveX

ActiveX is a technology developed by Microsoft Corporation for distributing software over the Internet. ActiveX controls are available for Internet Explorer.

ActiveX controls are distributed as executable binaries and are compiled for each target machine and operating system.

The use of ActiveX is a security risk because the browser places no restrictions on what an ActiveX control can do.

To mitigate the risk of using ActiveX plugins, each control can be digitally signed. The digital signatures can then be certified by a trusted certifying authority, such as VeriSign. The user does not know if the ActiveX code is safe to execute; rather, the user is assured of who is providing the code. In the end, the user is allowing the signing organization to do anything they want on the user's workstation and trusting that the organization will act responsibly.

If the browser encounters an ActiveX control that hasn't been signed (or that has been signed but certified by an unknown certifying authority), the browser presents a dialog box warning the user that this action may not be safe. At this point the user can elect to accept the control or cancel the download. If the user accepts the ActiveX control they are putting their entire workstation at risk. Few users that accept an unsigned control appreciate the risk involved. Digital signatures on ActiveX controls are of little protection to an unsophisticated user.

The following steps will disable ActiveX controls on Internet Explorer:

1. From the menu bar select View ![ActiveX](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)
2. In the pop-up window, select the Security tab.
3. In the pull-down list of options, select Internet Zone.
4. Select the Custom security level check box.
5. Click the Settings button.
6. Scroll down to the ActiveX and Plug-ins section. Select Disable.
7. Click OK to close out of the window.
8. Click OK to close out of the options window.

### Java

Java applets are programs written in the Java programming language that are run on the user's workstation. The Java applets are commonly used as a user interface to server-side programs.

Java has a large number of security safeguards intended to avoid attacks. However, any time code written by a stranger is run on the user's workstation, care should be taken. Disabling Java is a recommended option for a security-conscious user.

Several security features were built into Java to prevent it from compromising the remote user's machine. When running as applets, Java scripts are restricted with respect to what they are allowed to do by a security manager object. The following security features are part of the Java design:

- The security manager does not ordinarily allow applets to execute arbitrary system commands, to load system libraries, or to open up system device drivers such as disk drives.
- Scripts are generally limited to reading and writing to files in a user-designated directory.
- Applets are also limited in the network connections they can make: An applet is only allowed to make a network connection back to the server from which it was downloaded. This security hole involves Java's trusting use of the Domain Name System (DNS) to confirm that it is allowed to contact a particular host. A malfeasant using his own DNS server can create a bogus DNS entry to fool the Java system into thinking that a script is allowed to talk to a host that it is not authorized to contact.
- The security manager allows Java applets to read and write to the network and to read and write to the local disk but not to both. This limitation was created to reduce the risk of an applet spying on the user's private documents and transmitting the information back to the server.

To disable Java applets in Netscape, follow these steps:

1. From the menu bar select Edit ![Java](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)
2. Select the Advanced tab from the options at the left.
3. Clear the Enable Java checkbox.
4. Click OK at the bottom of the dialog window.

To disable Java Applets in Internet Explorer, follow these steps:

1. From the menu bar select Tools ![Java](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)
2. In the pop-up window, select the Security tab.
3. In the pull-down list of options, select Internet Zone.
4. Below, select the Custom security level checkbox.
5. Click the Settings button. A scrolling list will pop up.
6. Scroll down until you see the Java item. Select Disable Java.
7. Click OK at the bottom of the Settings.
8. Click OK at the bottom of the dialog window.

### JavaScript

The designers of JavaScript built security into the language itself. The basic approach was to eliminate the possibility of JavaScript code doing insecure activities by not providing commands or objects for those activities. Some examples of the security issues with JavaScript are as follows:

- **JavaScript cannot open, read, write, create, or delete files**. The language does not have any objects for managing files. A script cannot even list files and directories.
- **JavaScript cannot access the network or network resources**. The language does not have any objects for connecting or listening to the network interface.
- **JavaScript can access information available to the browser**. Information such as URLs, cookies, names of files downloaded, and so on.
- **JavaScript can only access the domain from which it was downloaded**. The script cannot access any other domain other than the one from which it originated.
- **JavaScript can make HTTP requests**. Scripts can request URLs and send other HTML information such as forms. This means the scripts could hit CGI programs that run on the Web server.

Over the years, JavaScript has produced quite a few security vulnerabilities for Web browsers. Patches and updated browsers have eliminated most of the security problems. However, the general concept that JavaScript is a potential avenue for the loss of private data still exists. Therefore, the general recommendation is to disable JavaScript unless it is explicitly needed for a trusted Web site.

The following steps are for disabling JavaScript on the Netscape browser:

1. From the menu bar select Edit ![JavaScript](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)
2. In the pop-up window, select the Advanced tab from the options on the left.
3. Clear the Enable JavaScript checkbox.
4. Clear the Enable JavaScript for Mail and News checkbox.
5. Click OK at the bottom of the dialog window.

The following steps are for disabling JavaScript on Internet Explorer:

1. From the menu bar, select Tools ![JavaScript](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)
2. In the pop-up window, select the Security tab from the top.
3. In the pull-down list of options, select Internet Zone.
4. Below, select the Custom security level checkbox.
5. Click the Settings button. A scrolling list will pop up.
6. Scroll down until you see the Scripting item. Under Active Scripting, select Disable and Disable Scripting of Java Applets.
7. Click OK at the bottom of the Settings.
8. Click OK at the bottom of the dialog window.

## Netscape-specific issues

Even though Netscape and Internet Explorer both manage the client end of the HTTP protocol, they do differ in how the features and configurations are handled.

### Encryption

Netscape browsers use either a 40-bit secret key or a 128-bit secret key for encryption. The 40-bit key was shown to be vulnerable to a brute force attack. The attack consisted of trying each of the 2 ^ 40 possible keys until the one that decrypts the message was found. This was done in 1995 when a French researcher used a network of workstations to crack a 40-bit encrypted message in a little over a week.

The 128-bit key eliminates the problem of a brute force attack because there are 2 ^ 128 possible keys instead of 2 ^ 40. To crack a message encrypted with such a key by brute force would take significantly longer than the age of the universe, using conventional technology.

### Netscape cookies

Setting up cookies in Netscape is different from doing so in Internet Explorer:

1. Select Edit from the Netscape menu and then choose Preferences.
2. In the Preferences window, select Advance.
3. In the section dedicated to cookies, choose the appropriate setting—your options are:Accept only those cookies originating from the same server as the page being viewed.Do not accept or send cookies.

### History and cache

The browser stores the URLs of the sites visited as a convenience for the users. Taken as a whole, this can represent a pattern of usage that many users would consider private and sensitive. It is recommended that the history settings be minimized. Also, the history data should be cleared periodically.

In Netscape, you can specify when the history list expires and manually clear the history list. This can be done with the following steps:

1. Select Preferences from the Edit menu.
2. Choose Navigator from the left frame.
3. Specify when pages in the history list expire by entering the number of days.
4. Clear the history list by clicking the Clear History button.

Browsers use two types of cache: memory cache and disk cache. Both caches should be cleared to ensure that no one can view information that you have accessed while using the browser.

In Netscape, the following steps will clear the cache:

1. Select Preferences from the Edit menu.
2. Choose Advance from the left frame and expand the list.
3. Click Cache.
4. Click to clear Memory Cache.
5. Click to clear Disk Cache.

## Internet Explorer-specific issues

Internet Explorer is a powerful and feature-rich tool for browsing the Internet. There are many configuration items available to make Internet Explorer more secure. The Internet Explorer configuration options are accessed by selecting the Tools

![Internet Explorer-specific issues](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/U001.png)

### General settings

The general settings control the home page, temporary Internet files, and the history list of visited Web sites.

Users should set their home page to Blank to prevent any Web site from tracking the behavior of the user. However, setting the home page to a favorite search engine, such as Google or Yahoo, should be considered low risk.

With regard to the history, cookies, and temporary Internet files, it is advisable to periodically delete this stored information. These files and cookies can profile a user and contain sensitive or private information.

### Security settings

Internet Explorer orients the Security settings around the Web content zone of the site to be accessed by the Web browser. In other words, the security settings the browser uses will depend on which zone the Web site being requested resides in. The zones are as follows:

- Internet
- Local intranet
- Trusted sites
- Restricted sites

#### Internet

This zone contains all Web sites the user hasn't placed in any other zone. In a sense, this is the default zone. Unless security is relaxed for a particular site, it will be put into the Internet zone and have default security settings.

This is one zone to which you cannot add sites. By default, all Web sites that are not added to the Local intranet zone, the Trusted Sites zone or the Restricted Sites zone, are placed into the Internet zone.

The default security setting for the Internet sites zone is Medium, which entails the following:

- ActiveX requires user acceptance before running.
- Unsigned ActiveX controls cannot be downloaded.
- Scripts and Java applets are enabled.
- Files can be downloaded, but prompt before downloading potentially unsafe content.
- The user is prompted before the installation of desktop items.

#### Local intranet

This zone is intended to contain all Web sites that are on the intranet of the user's organization. These sites are considered to be more trusted than those that default on the Internet zone.

The Local intranet zone contains local domain names, as well as the addresses of any proxy server exceptions you may have configured. To be effective, the Local intranet zone should be set up in conjunction with a local area network (LAN) proxy server or firewall. The intent is that all sites in the Local intranet zone are on the local network and inside the firewall.

The default setting for this zone is Medium-low, which provides the following security:

- Most content will be run without prompts.
- ActiveX requires user acceptance before running.
- Unsigned ActiveX controls cannot be downloaded.
- Scripts and Java are enabled.
- The user is prompted before the installation of desktop items. This controls whether or not the user can download and install Active Desktop content.

#### Trusted sites

This zone contains Web sites that the user trusts will not damage the workstation. The user should also trust this site with sensitive or personal data. The Security settings can require SSL for all the sites in this zone.

The Trusted sites zone includes sites that will not damage the workstation. It is very difficult to trust any site that is outside an individual's direct control. This trust may extend to organizational resources that are under the watchful eyes of network security engineers.

This zone should rarely be used. Few Web sites need the added features of this zone. Most Web sites that might be put in this zone will probably operate equally well in the Local intranet zone.

The default security level for the Trusted sites zone is Low and has the following settings:

- Minimal safeguards and prompts are provided.
- Most content is downloaded and run without prompts.
- All scripts, Java, and ActiveX content can run.

Clearly, given these settings, this zone is only appropriate for Web sites that are absolutely trusted.

#### Restricted sites

This zone contains Web sites that could potentially damage your computer or data.

The default security level for the Restricted sites zone is High and has the following settings:

- All scripting, Java, and ActiveX is disabled.
- Files cannot be downloaded.
- Prompting is required before downloading fonts.
- Data sources cannot be accessed across domains. This controls cross-domain data access, which can open the door to various spoofing attacks.
- Installation of desktop items is disabled.

### Privacy settings

Internet Explorer allows the user to set one of six levels of privacy. These settings, for the most part, adjust how the browser will deal with cookies. The six possible settings are as follows:

- **Accept All Cookies** — All cookies will be saved on the user's workstation and existing cookies can be read by the Web sites that created them.
- **Low** — Third-party cookies that contain sensitive or personal information will require the user's permission to be used. Also, third-party cookies that do not have a compact privacy policy are restricted.
- **Medium** — First-party cookies that contain sensitive or personal information will require the user's permission to be used. Third-party cookies that contain sensitive or personal information will be blocked completely. Also, third-party cookies that do not have a compact privacy policy are now blocked.
- **Medium High** — The settings are the same as Medium, except that now first-party cookies that contain sensitive or personal information will be blocked completely.
- **High** — All cookies containing personal data require the user's explicit permission to be used. Also, all cookies that do not have a compact privacy policy are completely blocked.
- **Block All Cookies** — All new cookies will be blocked and existing cookies cannot be used.

### Note

First-party cookies are returned to the Web site that created them in the first place. Third-party cookies are sent to a Web site that did not create the cookie.

The Privacy settings tab also allows the user to override cookie handling for individual Web sites. The user can specify which Web sites are always (or never) allowed to use cookies, regardless of the site's privacy policy. The user must enter the exact address of the Web site to allow or block cookies.

### Content settings

The Content settings deal with the Content Advisor, Certificates, and Personal information.

The Content Advisor uses a rating system to help the user control the Internet content that can be viewed on the browser. When enabled, the user can choose to control four categories, as follows. Each category has five settings from mild to strong.

- **Language** — controls slang and profanity
- **Nudity** — controls levels of attire and nudity
- **Sexual** — controls sexual activity (kissing and so on)
- **Violence** — controls aggressiveness of the violence

The Content Advisor allows the user to set Approved Sites that are always viewable (or never viewable), regardless of how they are rated. Also, the rating system can be changed. When the user leaves the Content Advisor enabling windows, they are prompted to enter a password for controlling further changes to the Content Advisor.

The Content settings allow users to view, add, and delete certificates. Additionally, the user can add or delete certificate authorities that will validate certificates received by the browser.

The Personal information settings allow the user to enter personal profile information in the Address Book, and thus create a new entry. Typical information in the profile would include name, e-mail, home and business addresses, spouse and children's names, birth date, and a digital ID. It is recommended that such personal information not be stored with the browser or be made browser accessible.

### Advanced settings

Internet Explorer has quite a few advanced settings. The following list shows some of the settings relevant to security. These settings are recommended, unless otherwise noted:

- Notification about script errors can be disabled. This is not recommended because script errors may be an indication of an attack.
- Java 2 to be used for Java applets.
- Enable or disable Java console, Java logging, and use of the JIT compiler for virtual machine.
- Check for publisher's certificate revocation.
- Check for server certificate revocation.
- Check for signatures on downloaded programs.
- Save encrypted pages to disk.
- Empty temporary Internet files when browser is closed.
- Enable integrated windows authentication.
- Enable profile assistant. This is not recommended because personal information may be disclosed.
- Use SSL 2.0, SSL 3.0, and TLS 1.0.
- Warn about invalid site certificates.
- Warn if changing between secure and not secure mode.
- Warn if forms submittal is being redirected.

### Encryption

It is recommended that 128-bit or 256-bit encryption be used in Internet Explorer. When using SSL, a solid padlock will appear on the bottom right of the screen. To determine whether 40-bit, 128-bit, or 256-bit encryption is in effect, select Properties from the File menu. This opens the document information page and will indicate whether weak (40-bit) or strong (128-bit or 256-bit) encryption is in use.

# Summary

For many nontechnical people, the power and usefulness of the Internet is personified in their Web browsers. Web browsing is by far the most popular use of the Internet. The combination of being very convenient and popular makes the Web browser a favorite target for viruses and other attacks. Some of the key steps that can be taken to allow for safe browsing on the Internet are as follows:

- Keep current with Web browser patches.
- Use antivirus software.
- Use secure sites for financial and sensitive transactions.
- Secure the network environment.
- Avoid using private information while browsing.
- Take care when changing browser settings.
