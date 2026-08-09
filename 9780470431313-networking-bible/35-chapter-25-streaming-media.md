# Chapter 25. Streaming Media

**IN THIS CHAPTER**

- How streaming supplies media content to users
- Streaming versus progressive downloads
- Streaming network architecture and protocols
- Unicasting versus multicasting
- Players, encoders, and streaming server software

Streaming media is a network technology that sends content to a user that can be played as it arrives. Streaming is associated with a special server called a *streaming server*. A related technology called *progressive download* can use Web servers to distribute media files.

Streaming content makes heavy use of network resources. A network architecture needs to be established to create the content, stage it to servers, and route the content to clients. All streaming solutions use a set of protocols to help package, control, and manage media traffic. The four IETF standard protocols — the Real-Time Streaming Protocol, the Real-Time Control Protocol, the Real-Time Transfer Protocol, and the SMIL markup language — are described in this chapter. The difference between unicasting and multicasting is described, and delineates different media delivery systems.

To prepare content for streaming or progressive downloads, media files need to be encoded. The process takes raw files and then compresses, segments, and packages them appropriately. Encoding can create content that has either constant or variable bit rates, as well as create a package of streams in multiple bit rates.

There are four main streaming media platforms in use today: Windows Media Services, RealNetworks Helix Server, Apple QuickTime Streaming Server, and Adobe Flash Media Streaming Server. All of these servers have their own formats, but with the exception of Flash, they work with a variety of other formats.

Adobe Flash is animation software that is served as content on Web pages. Flash can contain a variety of rich media content. Flash has a nearly universal penetration on the Web and is responsible for much of the inline media player content. Microsoft has an alternative technology called Silverlight that offers many of the same capabilities but is based on the Windows Presentation Foundation and the .NET Framework.

# How Streaming Works

Streaming media is the real-time delivery of content, one piece at a time, and it is pervasive and transformational technology. When you play a video from Google's `YouTube.com` or a TV episode from `ABC.com`, you are viewing video streamed over the Web. Streaming includes listening to audio on Internet radio stations such as Last. FM in media players like iTunes (see [Figure 25.1](ch25.html#internet_radio_played_within_apple_itune)), and viewing class lectures that you might download from the University of California at Berkeley or MIT. Long-distance learning is a revolution in education, and the technology described in this chapter makes it all possible.

![Internet radio played within Apple iTunes is streamed content, unlike podcasts.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2501.png)

**Figure 25.1. Internet radio played within Apple iTunes is streamed content, unlike podcasts.**

## Streaming versus progressive downloads

Streaming is used to transfer content over a network so that it can be played back in parts as it arrives. Streaming refers to the manner in which the content is transported and arrives as a stream of packets. Even the verb "to stream" has entered the vernacular to describe the process. To be a little more precise, streaming occurs when media is sent from a streaming server to a client and played by a player from the memory buffer it is stored in. As you play streamed content, the player discards the content after it is played; that is, streamed content never exists as a complete file that you can save to your disk and play at a later time. This is valuable from the viewpoint of the content creator or provider as it preserves the copyrights of these parties by making it hard to duplicate the material.

### Note

There are methods for using third-party tools to save streamed content such as FLV files, which are described later in this chapter.

Try as they might, there is no way that Digital Rights Management (DRM) software can protect content from those who want to copy it. At some point, the content must be displayed as output to an analog device: a speaker or a screen. If the person copying the content is willing to live with a certain loss of quality, the content can be rerecorded with a camera, microphone, or input to a second computer. This is as true of streamed content as it is of any other replay method. The problem is called the "analog hole." It is possible to tag content in ways that make the copies obvious upon closer scrutiny, but it is impossible to prevent the creation of a copy that will look to the average consumer as if it were an original.

In contrast, progressive download takes content on a Web server and delivers it to a client where it may be played as it downloads or when the download is completed. Typically, RealNetworks and Windows Media use streaming content, while QuickTime and Flash players use progressive downloads. Most players can use content supplied by both kinds of delivery methods. [Figure 25.2](ch25.html#the_different_components_of_streaming_an) shows a schematic that represents the different components of streaming and progressive download using the Real-Time Streaming Protocol (RTSP) for network control of steaming media. RTSP use a messaging system called Real-Time Control Protocol (RTCP) and breaks apart files into Real Control Packets (RCP). RTSP is an Internet Engineering Task Force (IETF) standard (RFC 2326) that is described in detail later in this chapter.

In [Figure 25.2](ch25.html#the_different_components_of_streaming_an), captured content is transferred to an encoding station where the media file is transformed. Encoding translates the video file into a particular format that is convenient to send. An example of an encoding format is the popular H.264. The encoded file can be sent to a Web server (shown in [Figure 25.2](ch25.html#the_different_components_of_streaming_an)) and transferred to a client by a unicast (1:1) transfer over the Web. This type of file transfer can be controlled by a client system (lower right) called RTCP (Real-Time Control Protocol) that is used by the client to control the flow of packets sent to it.

An alternative pathway is shown at the top of [Figure 25.2](ch25.html#the_different_components_of_streaming_an). The encoded file is sent to a streaming media server where the file is packetized as an RCP data stream. The pieces of the video file are sent to a multicast router where it can be sent to multiple client systems at the same time. Multicasting can also be controlled by RTCP flow control messages. Clients decode the media file to return it to its native format for replay.

![The different components of streaming and progressive download](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2502.png)

**Figure 25.2. The different components of streaming and progressive download**

Most consumers can barely tell the difference between streaming and progressive download because they both supply playable content. Indeed, progressive downloads are sometimes referred to as pseudo-streaming, or in Apple QuickTime as fast-start streaming. The main difference between the two is found in the behavior of the fast forward, rewind, and navigation controls, and in the fact that progressive download stores a copy of the file to disk. Progressive downloads can only be played in the order from beginning to end, although you can move backwards and forwards in the part of the file that has already been downloaded and buffered. Streamed content can be played out of order, provided that the part of the content you want to view has already been downloaded.

You may encounter the terms HTTP streaming or Web server streaming; both simply represent another version of progressive downloading because they create a copy of the media file in a local cache that can be copied if the user understands the system being used. One difference, though, between progressive downloads and HTTP streaming is that the use of HTTP over port 80 makes it much easier to penetrate firewalls than other streaming transport methods.

Events can be streamed in real time or supplied as video on demand (VOD). When events are in near real time over an IP network, they are sometimes referred to as "Live-Live" or more frequently as Webcasts. On-demand implies that the media has been prerecorded and stored, and suggests but does not require that the content has also been edited or altered in some way.

[Table 25.1](ch25.html#streaming_versus_progressive_download) summarizes the two technologies of streaming versus progressive download.

**Table 25.1. Streaming versus Progressive Download**

| Feature | Progressive Download | Streaming |
| --- | --- | --- |
| **Staging** | Web server | Streaming server |
| **Best for** | Stored content replay | Video on demand (VOD), Live |
| **Bandwidth** | Insensitive to network conditions Retransmits lost packets | Sensitive to network conditions Lost packets are dropped in playback |
| **Firewalls** | Firewall friendly | Requires opening a special port most of the time |
| **Player control** | Must play in sequence | Can skip ahead if content is in buffer |
| **Copies** | Copy left on drive | No copy retained |
| **Content protection** | No | Yes |
| **Casting** | Unicast only | Broadcasts and multicasts supported |

The ability to sequence a group of files can be scripted in some products like Adobe Flash. Special files that specify sequences, called Synchronized Markup Integration Language (SMIL) files, also allow you to coordinate replays. (SMIL files are discussed later in this chapter.) One of the techniques people use with streamed content is called a pre-roll or gateway file. A pre-roll/gateway file can be used to advertise content, inform the viewer about the stream that they are about to view (in case they might want to bail out), and for many other purposes.

## Unicasting versus multicasting

Streaming is a point-to-point technology. A server defines one endpoint of the connection providing content and a client player or browser defines the other endpoint. When a media server maps a single stream between the two endpoints, it is called *unicasting*. You can think of unicasting as being equivalent to a private message. Unicasting is *narrowcasting*; the sender can customize the message for the audience with unique control over the message, but at an attendant cost. When a content provider uses multiple streams to broadcast a message to multiple consumers, the technology is called *multicasting*. Multicasting allows the sender to create one consistent message that has an economy of scale.

### Note

RSS feeds would not be considered a streamed media application, as the entire file must be delivered to be used. RSS is a subscription service based on specifications contained in either XML or RSS text files.

[Table 25.2](ch25.html#unicasting_versus_multicasting-043) lists some of the important differences between unicast and multicast streaming.

**Table 25.2. Unicasting versus Multicasting**

| Feature | Unicasting | Multicasting |
| --- | --- | --- |
| **Best used for** | On demand | Live or scheduled |
| **Bandwidth requirements** | Large capacity for multiple streams | Small capacity for one stream |
| **CPU requirements** | Heavy CPU load to manage individual streams | Low CPU load to manage one stream |
| **Client playback** | Players can have individual control over playback | Players get the same content and have the same capability and timing |
| **Infrastructure requirements** | Bandwidth that scales | Multicast router(s) |
| **Message control** | High | Low |

Streaming plays an important role in many enterprise deployment technologies. Products like Altiris Software Virtualization Solution (SVS), the Citrix XenApp application streaming server, and Microsoft SoftGrid (along with their Zero Touch technology) are examples of technology that relies on streamed content from distributed deployment servers. All these systems allow developers to deploy software and content in a multicast topology.

In the case of SoftGrid, applications are delivered in a way that allows them to begin operating on client systems before the entire application has been streamed to the client, a form of application virtualization. An application is prepared by the SoftGrid Sequencer, which deconstructs the application by determining its system settings, which DLLs or INI files it uses, and other parts, and then sending the parts required for startup in the first part of the stream. Because the client requests the application first, the technology is a pull technology. [Figure 25.3](ch25.html#softgrid_application_streaming) shows the SoftGrid implementation using the Microsoft System Center Virtual Application Server.

![SoftGrid application streaming](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2503.png)

**Figure 25.3. SoftGrid application streaming**

In streaming systems such as Citrix XenApp, Altiris SVS, and related deployment technologies, the systems use a push technology. When the system becomes available, it is inventoried by an agent or some other method and the software is then deployed as needed. While these systems all operate on IP networks, as a general rule, they do not use the open standards for media streaming that are described in this chapter. They tend to use XML files for coordination, response, or answer files, and proprietary methods for sending their streams down the wire.

# Streaming Protocols

Streaming media content involves the delivery and control of files that have been segmented for smoother delivery. On IP networks, the IETF has a number of standard protocols used to stream content. In the sections that follow, the four most important of these standards are described. These include RTSP, RTP, RTCP, and the SMIL markup language.

These protocols control the delivery of content, network factors such as Quality of Service and congestion control, and other variables. These streaming protocols work over TCP/IP networks. Most of the time, they use UDP (User Datagram Protocol) for their transport, but in some instances TCP (Transport Control Protocol) is used.

## Real-Time Streaming Protocol

The Real-Time Streaming Protocol (RTSP) is an Application layer protocol that is used to control how a media player can control a stream from a media server. It is based on IETF RFC 2326. RTSP is configured to use the well-known port 554. RTSP keeps track of the state of the session using a session ID. Any messages sent from client to server and vice versa reference this ID.

The best way to think about RTSP is that it provides a command set to a player that can issue navigation commands such as play and pause to a streaming media server. RTSP plays no role in how streaming content is segmented, encoded, or transported. Other protocols serve those functions and work hand in hand with RTSP. One common transport protocol for streaming media used with RTSP is the Real-Time Transport Protocol (RTP) that is described in the next section.

The more important RTSP commands include:

- `PLAY`. The `PLAY` message tells the player to play a stream. `PLAY`s can be queued and can specify a starting point in the stream. A `PLAY` issued for a `PAUSE`d stream will restart. Multiple `PLAY`s in a URL cause the player to play all of the media streams that the requests specify.
- `PAUSE`. The `PAUSE` message stops a media stream from playing. A `PLAY` command resumes playback from the point of the pause.
- `SETUP`. The `SETUP` message creates a stream connection and must be given before the stream can play. `SETUP` contains the URL and transport protocol, as well as the port used to receive RTP audio or video, and other RTCP transport metadata.
- `TEARDOWN`. The `TEARDOWN` message terminates the session. It ends all media stream transmission and releases all session data from the server buffer.
- `DESCRIBE`. The `DESCRIBE` message includes an RTSP URL (`rtsp://`...) and the streaming media file type that can be replayed.
- `RECORD`. A `RECORD` message specifies sending a stream to a server for storage.

The following streaming media servers use RTSP: Apple QuickTime Streaming Server, Darwin Streaming Server (open source QuickTime Streaming Server), Alcatel-Lucent pvServer (a.k.a. PacketVideo Streaming Server), RealNetworks Helix DNA Server, Live555 (open source), VideoLAN, Windows Media Services, and Maui X-Stream VX30.

## Real-Time Transport Protocol

The Real-Time Transport Protocol, or RTP, is a method for sending packets containing rich media over the Internet. The IETF standard is described in RFCs 1889 and 3550. RTP is usually combined with RTSP (as described in the previous section), and this is the same pair of protocols used to transport VoIP as described briefly in the next chapter. RTP is used in both unicast and multicast applications. Compressed RTP (CRTP), as defined in RFC 2509, and Enhanced RTP (ERTP) are also used.

### Note

RealNetworks has a version of RTP called Real Data Transport (RDT), which works with the RealNetworks RTSP server.

RTP transport on IP networks can occur with either TCP or UDP. TCP is used when a guaranteed delivery is required, while UDP is used when a certain amount of data loss can be tolerated. RTP transport of streaming media uses UDP and can be assigned to any even port in the dynamic range of 16384 to 32767. By convention, the next-higher odd port is assigned to RTSP messaging.

The use of dynamic ports often causes difficulty when trying to penetrate firewalls. To work around this problem, you can employ a STUN server to provide a mechanism for traversing firewalls. STUN stands for Simple Traversal of User Datagram Protocol through Network Address Translators. STUN works by using servers on both sides of the firewall to listen for open ports. If it is unable to penetrate the firewall from the outside, it can issue a request to a system on the inside to request the packets from the outside.

### Note

STUN is described in more detail in [Chapter 26](ch26.html).

RTP does the following things:

- Identifies content.
- Uses a sequence identification at the packet level, called a Protocol Data Unit (PDU).
- Manages streams using a Contributing Source ID (CSRC) to match a stream to one or more sources. The ability to manage separate streams allows video and audio to be handled individually, which can be helpful in a variety of circumstances.
- Time synchronization using a Synchronization Source ID (SSRC).
- Packet delivery checking. The RTSP protocol is used to monitor Quality of Service parameters.

Protocol Data Units, or PDUs, are ID numbers assigned to the following features: for OSI Layer 1, a PDU is assigned to a bit; for Layer 2, it is assigned to the frame; for Layer 3, it is assigned to the packet; for Layer 4, it is assigned to the segment; and for Layers 5 to 7, it is assigned to data. A related concept called the Service Data Unit, or SDU, is assigned to the data that one system sends another at the Layer 1 level below. For a PDU of *n*, the SDU would be *n-1*.

In [Figure 25.4](ch25.html#the_rtp_packet_structure), the structure of an RTP packet is shown. The packet contains a number of flags in the header (the expanded portion of the packet) to indicate the extension type, the packet ID, source, and payload type. The different fields in the RTP packet header are as follows:

- **Version**. The current version of the protocol (version2).
- **Padding**. A single bit flag that indicates that there are extra bytes at the end of the packet.
- **Extension header**. An options 32-bit word that contains both the specific profile identifier and the length of the extension.
- **CSRC**. The contributing source ID lists the sources of the stream when that stream is coming from two or more sources.
- **Payload Type**. A 7-bit field that contains the format of the payload.
- **Sequence Number**. This 16-bit field is the sequence number for each of the RTP data packets. The receiving system uses the sequence number to order playback.
- **Extension**. This 1-bit flap indicates that there is an application-specific Extension header between the header and payload data.
- **CSRC Count**. This 4-bit field indicates the number of CSRC identifiers that are appended after the fixed header.
- **Marker**. A 1-bit flag used by an application to indicate that the data is important in some way to the application.
- **Timestamp**. A 32-bit field that is used to synchronize playback on the receiver.
- **SSRC**. The synchronization source identifier is a means of uniquely determining the source of the stream.

The Secure Real-Time Transport Protocol (SRTP) is a variation of the RTP protocol that defines a method for encrypting, authenticating, and error checking RTP data for both unicast and multicast streams. It is used with Secure RTCP, a version of RTCP that applies these safeguards to the messages that are used to control SRTP traffic. Message authentication is required in SRTP, but all of the other features in SRTP are optional and up to applications to implement on an individual basis. These protocols can be used in VoIP as well as streaming media applications.

![The RTP packet structure](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2504.png)

**Figure 25.4. The RTP packet structure**

## Real-Time Control Protocol

The last of the real-time streaming protocols in common use is the Real-Time Control Protocol (RTCP), as defined in RFC 1889. This Session layer protocol is a messaging system that provides feedback on the performance of RTP data flow. As such, RTCP is a means of enforcing Quality of Service (QoS) functionality. RTCP monitors the arrival of bytes and packets, the amount of packets, network delays, and other statistics. Applications that are RTCP-enabled can take these statistics and alter their behavior to change the performance of the stream in order to match the QoS desired.

RTCP packets are small message packets. The following types of packets are transmitted:

- **Sender Reports**. Data is transmitted that includes the quantity of data sent and received, along with the timestamps needed to synchronize RTP packets.
- **Receiver Reports**. This message goes to clients that don't send RTP packets. It contains QoS statistics.
- **Application Specific**. This message type can be used by applications to define messages for their use.
- **Source Description**. This message type identifies the stream source and provides details on the owner of the source system.
- **Goodbye**. This message is sent when the source is shutting down a stream.

At the moment, RTCP isn't easily applied to large video broadcast systems such as IPTV (Internet Protocol-based Television). The large amount of collected data leads to long delays in sending RTCP statistics and long delays in the receiver analyzing the data.

## Synchronized Markup Integration Language

The Synchronized Markup Integration Language, or SMIL (pronounced 'smile'), is an open standard that defines a markup language based on XML to support coordinated media playback. SMIL serves as input to RTSP transport, just as HTML content serves as input to HTTP transport. SMIL takes encoded files and specifies a sequence for their playback. There are SMIL editors you can use to create the files. In order to play back a SMIL sequence, a player must be SMIL-compliant. Two examples of SMIL editors are Adobe GoLive and SMOX Editor/SMOX Pad.

A SMIL file (.SMIL or .SMI file extension) is a metafile that instructs a client on how to handle a selected stream. It defines a number of session-level characteristics for a connection. SMIL can negotiate which bit rate file is streamed when multiple bit rates have been stored. Another tag can point to localized content, picking a language based on system settings, or using a different video clip or soundtrack for different users based on other criteria. SMIL can be attached to buttons, which allow the format to direct content based on a user's interaction, which could enable playlists or jukebox features. Because SMIL is a set of instructions that is external to the content it controls, it is possible to use SMIL to alter the sequence of content playback, change the entry points of playback within a specific clip, or point to any number of different streaming media or Web servers.

### Note

Microsoft Synchronized Accessible Media Interchange, or SAMI, markup language files have an .SMI extension. This technology is used to place captions in PC media playback.

If you open a SMIL file in a text editor, you will find that it is similar to any other HTML file. A SMIL file must start and end with the `<SMIL>...</SMIL>` tags. There is a `<HEAD>` section that includes metadata and presentation layout information, a `<BODY>` section containing timing data and media elements, and both `<PAR>` and `<SEQ>` sections (for parallel and sequential) that are used to specify the media content by referencing their URLs. SMIL can also be tagged so that a media object is associated with a certain level of available bandwidth.

## Encoding

Most media files are recorded in high-quality formats that are called raw files, which are impractical to stream across most WAN connections such as the Internet. To prepare file formats more suitable for streaming, the raw files are usually cropped to a smaller picture size, the frame rate of the video and/or the bit rate of the audio are reduced in speed and quality, and the file is then encoded, which usually involves a significant amount of compression.

### Note

The input of a file to a streaming server is called ingest.

Encoding is a process by which a file is altered by an algorithm that compresses the file; unencoding is the process by which the encoded file is extracted. The software that performs the encoding is called a codec (literally, code/decode software); codecs can also be implemented in hardware in ASICs on audio/video capture boards. It is also possible to transcode an encoded file from one format to another. Encoding/decoding is often quite processor intensive and can take a long time to perform.

[Table 25.3](ch25.html#single_versus_multiple_bit_rate_encoding) compares single versus multiple bit rate encoding.

Although most encoding techniques use a constant bit rate input and output for their content, one technique that is helpful in terms of improving transmission over lower-bandwidth connections is to use what is called Multiple Bit Rate, or MBR, encoding. In MBR, multiple streams are encoded at different bit rates and then combined into a single file. A client that supports MBR will negotiate with the server the best bit stream based on available bandwidth. Should that bandwidth change during transmission, the client can request that a different-quality bit rate be sent.

**Table 25.3. Single versus Multiple Bit Rate Encoding**

| Feature | Unicasting | Multicasting |
| --- | --- | --- |
| **Staging** | On either a streaming or Web server | On a streaming server with software that supports it |
| **Size** | One file | Many files |
| **Bandwidth** | May pause or stop when network is congested | Slight pauses as a different bit rate stream fills the buffer |
| **Frame sizes** | Selected based on bandwidth | Frame sizes are the same for every bit rate |
| **Audio** | Selected based on bandwidth | Audio settings must be the same for every bit rate |
| **Web integration** | Must have individual controls or links for different streams | One control or link for all streams |

This intelligent or adaptive streaming goes by different names in the different streaming technologies. RealMedia calls this technology SureStream, Microsoft uses the term Intelligent Streaming for Windows Media, and Apple refers to these different bit rates as alternative data rate movies. Apple stores the different bit rates as individual files in a folder on the Macintosh.

In [Figure 25.5](ch25.html#windows_media_encoder_9_converts_audio_a) the Windows Media Encoder 9 is shown encoding a movie file into streaming content. Microsoft makes versions of this encoder available on the their Web site for use on Windows Media Player. The Media Encoder can capture live content for playback or streaming, convert a file to video, broadcast live events, and capture screen sessions. It can output multichannel audio, interlaced video, and Multiple Bit Rate (MBR) content, insert Digital Rights Management (DRM) information, and Constant Bit Rate (CBR) and Variable Bit Rate (VBR) encoding.

![Windows Media Encoder 9 converts audio and video files and input into streaming content.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2505.png)

**Figure 25.5. Windows Media Encoder 9 converts audio and video files and input into streaming content.**

CBR encoding is best used in streaming sessions. The bit rate is set to be a constant rate within a small variance allowed by the buffer size. The quality of CBR-encoded content varies over time because the amount of compression you apply is constant. Some frames are more complex and compress more poorly than the simpler frames. Because the variation of the delivery of one stream versus another stream varies, users find that the playback of CBR streams is inconsistent from session to session. Lower bit rate streams dramatically reduce the quality of playback.

VBR encoding is used when the content will be either progressively downloaded or played locally. This type of encoding can better accommodate content that varies in complexity, and results in smaller file sizes than a CBR recording, often as little as 50 percent of the size.

Here is a list of the most commonly used encoders:

- **Barix Instreamer**. This all-in-one hardware solution is an appliance that takes analog and digital audio and converts it into MP3 streams. The Instreamer can send the streams to the streaming server, such as an Icecast or SHOUTcast server, where the content can be served to networked devices. Information on this device can be obtained from `www.barix.com`.
- **EdCast**. This program creates SHOUTcast and Icecast streams, as well as MP3, Ogg, and aacPlus files. The program or its plug-in for Winamp can be obtained at `www.oddsock.org/tools/edcast`. EdCast was previously available as Oddcast.
- **Nicecast**. Nicecast is used to create streaming audio content. It is available for Mac OS X at the Rogue Amoeba Web site at `www.rogueamoeba.com/nicecast`.
- **QuickTime Broadcaster**. The Apple live encoding solution creates MPEG-4 or H.264 video, or the 3GP mobile version of the MPEG-4 Part 14 container format on the Macintosh. It is available from the Broadcaster site at `www.apple.com/quicktime/broadcaster`, as is the QuickTime Streaming Server.
- **RealProducer**. RealProducer is RealMedia's encoder and creates the RealAudio and RealVideo formats. It can create live and downloadable content that is used on the RealNetworks Helix Server. You can download the free version and the professional version of the encoder from `www.realnetworks.com/products/producer/index.html`.
- **SAM**. This DSP plug-in for Winamp encodes audio into MP3, Ogg, and Windows Media files. To download the SAM plug-in, go to `www.spacialaudio.com/products/winamp`.
- **Windows Media Encoder**. As described earlier, you can download this program from `www.microsoft.com/windows/windowsmedia/forpros/encoder/default.mspx`.
- **Wirecast**. The Wirecast encoder is available for both Mac and PC and creates files compatible with the QuickTime Streaming architecture to be played back on either the QuickTime Streaming Server or on the Darwin server. Wirecast is available from `www.flip4mac.com/wirecast.htm`.

# Streaming Servers

Streaming servers are available from a number of vendors and support a variety of streaming technologies. Most of these servers run on a single platform and offer a single streaming solution. Some are cross platform and a few are also cross technology. The most widely used streaming media servers include the following:

- **Windows Media Services**. This server is an installable service on Windows Server 2008; a prior version ran on Windows Server 2003. The 2008 edition serves up content that plays on Windows Media Player. Additional features are Fast Start, Fast Cache (caching and proxy services), Fast Recover and Fast Reconnect, authentication, multicast and unicast streaming, and broadcasting. To learn more about this server, go to `www.microsoft.com/windows/windowsmedia/forpros/server/server.aspx`.
- **Helix Server**. Currently in version 12, the Helix Server is a multi-format cross-platform streaming server from RealNetworks. It supports RealAudio and RealVideo, Windows Media, QuickTime, MPEG-4, 3GPP (H.263/H.264), and MP3, and can run on Windows Server 2003, Red Hat Linux Enterprise Level, and Solaris (on SPARC). Information on Helix may be found at `www.realnetworks.com/products/media_delivery.html`.RealNetworks sells the Helix Proxy server to provide caching, proxy, and gateway services for Helix content.
- **Apple QuickTime Streaming Server (QTSS)**. The Apple streaming server runs on Mac OS X server, and along with the sequencer QTSS Publisher, it delivers QuickTime content over RTP/RTSP protocols. QuickTime can deliver H.264, MPEG-4, 3GPP, MP3, and AAC content, as well as MP3 files using the Icecast protocols. Version 6 integrates into Open Directory services. The QTSS home page is found at `www.apple.com/quicktime/streamingserver`.
- **Adobe Flash Media Streaming Server 3 (FMSS)**. FMSS serves Flash content encoded in H.264 video or HE-ACC audio, and sent either as a stream or progressive download. To learn more about Flash Media Streaming Server, go to `www.adobe.com/products/flashmediastreaming`.
- **Wowza Media Server Pro**. This server is a much cheaper alternative to the Adobe Flash Streaming Server, and streams Flash content created by non-Flash RTSP/RTP encoders. To learn more about Wowza, go to `www.wowzamedia.com/products.html`.
- **Darwin Streaming Server**. Darwin is the Apple open source version of QTSS. It uses the same code base as QTSS, but runs on platforms other than the Macintosh, including Linux, Windows, and Solaris. Darwin's home page is located at `http://dss.macosforge.org`.
- **Icecast Streaming Media Server**. The Icecast server is an open source project that streams audio to listeners. It is very popular software for serving Internet radio content. The project publishes their libshout library to access Icecast servers, and Ices, which is a content management program that can post audio to the Icecast server. Icecast streams are compatible with SHOUTcast, another popular platform for streaming audio content. Icecast is found at `www.icecast.org/index.php`.Icecast is an open source streaming multimedia server solution from the `Xiph.Org` foundation. It uses Vorbis encoded content streamed over HTTP, or alternatively MP3 encoded content streamed over the SHOUTcast protocol. To download the software, go to `www.icecast.org`.
- **Nullsoft SHOUTcast**. This audio server is used for many of the Internet radio stations that are currently deployed. The home page is located at `www.shoutcast.com/download`.
- **SHOUTcast**. The SHOUTcast streaming media server is used to create digital audio files in either MP3 or HE-AAC format. Icecast is an open systems version of this software. SHOUTcast is available for both Mac and PC and is freeware. You can download this software from the developer, Nullsoft, at `www.shoutcast.com`.
- **Anysoft Agility**. This server is a complete video production and streaming server solution that works with a broad variety of content. It tends to be used by large media companies and includes features such as accounting, reporting, and production. The Agility home page is found at `www.anystream.com/agility.aspx`.
- **Unreal Media Server**. Unreal is a proprietary server that runs on Windows. It streams Windows Media and QuickTime-compatible content to browsers that have a Streaming Media Player application, ActiveX, or a Mozilla plug-in. The server is free for 15 connections, and can be obtained from `www.umediaserver.net`.

It can be difficult to run some of these servers, and so many of them are made available by a variety of vendors in the form of hosted services.

One of the key calculations that you need to make when considering server solutions is the amount of bandwidth that is required to support your client load. Minimum bandwidth requirements for individual connections are listed in [Table 25.4](ch25.html#server_bandwidth_requirements_open_paren), and must be *multiplied by the number of clients* that are directly supported. To support a client load beyond any single connection, solutions such as remote caches, proxy servers, and points of presence are established as part of a streaming solution.

**Table 25.4. Server Bandwidth Requirements (Minimum)**

| Stream Type | Rate | Quality | Minimum Connection |
| --- | --- | --- | --- |
| **Speech** | 800 bps | Minimum for speech | Dial up |
| **Speech** | 8 Kbits/s | Telephone | Dial up |
| **Video** | 16 Kbits/s | Videophone | Dial up |
| **Audio** | 32 Kbits/s | AM radio (Medium Wave, or MW) | Dial up |
| **Audio** | 96 Kbits/s | FM radio | DSL/ISDN |
| **Audio** | 128 – 160 Kbits/s | Standard listening | DSL/ISDN |
| **Video** | 128 – 384 Kbits/s | Videoconferencing | DSL/Cable modem |
| **Audio** | 192 Kbits/s | Digital audio broadcast | DSL/Cable modem |
| **Audio** | 320 Kbits/s | CD | DSL/Cable modem |
| **Audio** | 500 Kbps – 1 Mbits/s | Lossless audio (FLAC, for example) | DSL/Cable modem |
| **Video** | 1.25 Mbits/s | VCD (Video CD) | DSL/Cable modem |
| **Audio** | 1.41 Mbits/s | PCM sound for Compact Disk Digital Audio | DSL/Cable modem |
| **Video** | 5 Mbits/s | DVD | T1 |
| **Video** | 15 Mbits/s | HDTV | T2 |
| **Video** | 54 Mbits/s | Blu-ray | T2 |

In the sections that follow, I describe several of the different players and formats used for streaming media. You may be very familiar with some of these streaming file formats, such as Adobe's Flash files, which `YouTube.com` uses. This area of technology is very dynamic, with new products being introduced often. Microsoft's Silverlight is an example of a new streaming multimedia format that is being introduced to the market.

## Streaming file formats

Streaming media files use one or more extensions for the files that each player can play, and one or more file extensions for the metafiles that are referenced in a link on a Web page that initiates the stream. If the content file is referenced in an HTML `<a href>` tag, then that file is downloaded and not streamed when the link is selected. To initiate a stream, a metafile is used as the link reference. Metafiles are usually text files (XML or SMIL, for example) that describe the media player to use, initiate the stream, and then point the stream to the player on the client system.

### Tip

To search for detailed information on various file formats, go to `http://Filext.com`.

Sometimes the metafile and the streamed media file use the same extension, as in the case of the QuickTime .MOV extension. More often, they are different. RealMedia uses the .RM file extension for its streamed content, and the .RPM or .RAM extension for its metafile extensions. Windows Media uses .ASF and .WMV for content, and .ASX, .WAX, and .WVX for metafiles.

The reason that the Apple MOV files don't require a metafile is that the instructions for streaming are encoded into the MOV file in a hint track. Those instructions point directly to the streaming server. Sometimes this system doesn't work properly when the default player isn't QuickTime. This is more often the case on Windows systems than on the Macintosh. To address browser redirection when an RTSP link (URL) is selected, Apple uses a Reference Movie file, to which Apple also assigns the .MOV file extension. The Reference Movie is also used when the QuickTime version of MBR or alternate bit rates are used. The hints in the Reference MOV file support the negotiation required by the variable bit rate scheme from Apple.

When QuickTime is calling for a live feed to be streamed, there is no MOV file to work from. In that case, Apple uses a Session Description Protocol (SDP) file as its text metafile format to direct the player to the broadcasting server.

## Players

QuickTime, Windows Media Player, and RealMedia are available as both stand-alone players and as browser plug-ins. Because these three players work with files created to work on three different and non-interoperable streaming media architectures, content providers are forced to either support these three or make compromises.

The four most popular streaming media players are:

- **Adobe Flash**. The Flash player is currently at version 10.0x. It plays Flash Video Files (.FLV extension). Adobe Flash uses an applet that installs into a browser and that decodes and plays FLV files. You can find it at `http://get.adobe.com/flashplayer`.
- **Apple QuickTime**. The QuickTime player is at version 7.5.5 and can be downloaded either alone or with iTunes. The standard player is free; Apple sells an in-place upgrade to its Pro version, which can perform file transcoding and conversions. QuickTime is the preferred format on the Macintosh. QuickTime plays Movie (MOV) files, or less frequently, QT or QTI files. It can be obtained from `www.apple.com/quicktime/download`.
- **Microsoft Windows Media player**. Currently at version 11, this player ships with Microsoft Windows and plays Windows Media Audio (WMA), Windows Media Video (WMV), and Advanced Streaming Format (ASF) files. Windows Media Player's home page is at `www.microsoft.com/windows/windowsmedia/default.mspx`.
- **RealPlayer**. Currently at version 11.0, RealPlayer is the RealNetworks cross-platform player for MP3, MPEG-4, QuickTime, and Windows Media files. It is also the player of choice for the proprietary RM files that RealMedia produces. There are versions of RealPlayer for Windows, Mac OS X, Linux, UNIX, Windows Mobile, and the Symbian OS. You can obtain RealPlayer from its Web page at `www.real.com/player`.RealNetworks released the Helix engine as an open source project for developers of media creation solutions. The Helix DNA client is a playback engine, and the Helix Player is the media player based on the client that runs on Linux, Solaris, FreeBSD, and Symbian. The Helix Producer can be used to add content to the Helix DNA Server for streaming content. The Helix Web site is found at `https://helix-client.helixcommunity.org`.

Among the many other media players available, the best known are the following: BearShare, FLV-Media Player, Musicmatch Jukebox, Napster, PowerDVD, VLC Media Player, WinDVD, xine, Yahoo! Music Jukebox, and Zinf.

### Tip

Wikipedia maintains an extensive page listing of media players at `http://en.wikipedia.org/wiki/Media_player_application_software`.

All of these different technologies ensure that most Web sites providing streaming media do so in two or more formats and often in different data rates and screen sizes in order to accommodate the different player applications and connection bandwidths.

## Flash

Adobe Flash is animation software for serving content in Web pages. It, along with Adobe Shockwave, has nearly universal penetration in Web-based video playback. Flash was developed by FutureWave and acquired by first Macromedia and then Adobe. The name Flash is a contraction of the words Future and Splash, a takeoff on the FutureWave name. Flash Video is both the file format and the technology for delivery of streamed video content from a Web page. Perhaps the best-known Web site using Flash Video is `YouTube.com`.

Shown in [Figure 25.6](ch25.html#flash_video_is_ubiquitous_on_the_web_for) is the adorable spider that appeared as a Flash Video on the Science Friday Web site. Flash Video plays inside the Flash Player, which is a plug-in that is embedded inside Web pages. The current version of the player is 10.0x, and can be downloaded from `http://get.adobe.com/flashplayer`. Other players that play Flash Video include VLC media player (Mac, PC, Linux), FLV Player, QuickTime (requires the Perian video plug-in), RealPlayer, Windows Media Player, MPlayer, and xine and totem on Linux. Microsoft DirectShow is required for Media Player and Media Center Flash playback.

![Flash Video is ubiquitous on the Web for streamed video content; nearly all players look similar to this one in FLV Media Player.](/api/v2/epubs/urn:orm:book:9780470431313/files/figs/2506.png)

**Figure 25.6. Flash Video is ubiquitous on the Web for streamed video content; nearly all players look similar to this one in FLV Media Player.**

The Flash Video file format is FLV and supports Sorenson Spark H.263, H.264, MPEG-4 ASP, and On2 Technologies TrueMotion VP6 video codecs, as well as HE-ACC audio content. It is also possible to embed Flash Video into Shockwave Flash (SWF) files. Flash Video files themselves are defined by an open container format, but the encoding is done by a proprietary codec inside the Adobe Flash authoring program, called Adobe Flex, and other Adobe products. An FLV stream contains one video and one audio stream.

Among the file formats that Flash uses are the following:

- **F4A**. An audio format for the Flash Player with the audio/mp4 MIME type.
- **F4B**. An audio book format for the Flash Player with the audio/mp4 MIME type.
- **F4P**. The protected video format for the Flash Player with a video/mp4 MIME type.
- **F4V**. The video format for the Flash Player with a video/mp4 MIME type.

Flash Video is noted for being very compact. Flash Video can be delivered as FLV files, embedded in SWF files, sent from a Web server as a progressive download over HTTP, and streamed from the Web server to clients. For progressive download and streaming, Adobe uses the proprietary Real-Time Messaging Protocol (RTMP). The Real-Time Media Flow Protocol (RTMFP) is the technology that Adobe uses to communicate between Flash Players and the application server over the Adobe AIR framework and can be used to distribute Flash Video content. RTMP server software includes the Adobe Flash Media Server, the Wowza Media Server, and the WebORB Integration Server for .NET, Java, and ColdFusion.

As previously mentioned, streaming media doesn't leave a permanent copy of the file on your system. That means that any FLV file that you might want to view at a later time won't be available to you unless you take some extra steps to capture it. There are three methods that you can use to save FLV files: use some special-purpose Web sites that capture the video and send it to you, use a browser extension or plug-in, or purchase a commercial program that offers this functionality.

Sites that offer the ability to save online video include KeepVid (`www.keepvid.com`), or for YouTube, the YouTube Downloader site (`http://video.qooqle.jp`). The Firefox extension, called Video Downloader, can also save streamed FLV files. To save video captured off your screen, you can use programs like Snagit (from TechSmith) or Snapz Pro X 2 (from Ambrosia Software).

## Silverlight

Microsoft Silverlight is a programming environment for delivering rich content to browsers with the Silverlight plug-in. Silverlight offers many of the same capabilities of Adobe Flash and Shockwave, along with animation and vector graphics. It leverages the .NET Framework and development tools and is part of the Windows Presentation Framework. Plug-ins for Silverlight exist on Windows, Mac OS X, Linux (as Moonlight), Windows Mobile 6, and Symbian.

Silverlight 2.0 includes the Media Stream Source API that allows developers to create media streams with a variable streaming technology that Microsoft calls "adaptive streaming." This technology allows the player to select a bit rate that is allocated based on the available bandwidth and CPU capacity. The API is extensible, requiring only that the streams be in a Silverlight runtime in a decodable format, such as MP3 or WMA. Media Stream Source was the technology used to run the NBC Beijing Olympics Web site.

Windows Live offers the Silverlight Streaming Service as a hosting solution for Silverlight applications. The service provides Silverlight content to Windows and Macintosh clients, and can provide the content to Microsoft Expression Web sites. Silverlight content can be created in the Microsoft Expression Encoder that is part of Expression Studio 2 and other third-party tools. Silverlight Streaming by Windows Live also integrates with the Microsoft adCenter platform. You can find more information about this streaming service at `http://streaming.live.com`.

# Summary

In this chapter, you learned about streaming media solutions and progressive downloading. Streaming content makes heavy use of network resources. The network architecture needed was described.

Streaming solutions use a special set of protocols. The Real-Time Streaming Protocol, the Real-Time Control Protocol, the Real-Time Transfer Protocol, and the SMIL markup language were described in this chapter.

The encoding process can create content that has either constant or variable bit rates, as well as create a package of streams in multiple bit rates.

The four main streaming media platforms — Windows Media Services, RealNetworks Helix Server, Apple QuickTime Streaming Server, and Adobe Flash Media Streaming Server — were described. Flash and Silverlight streaming were also briefly considered.

In the next chapter, a related streaming technology for telephone is considered. Voice over IP is revolutionizing the telecommunications industry.
