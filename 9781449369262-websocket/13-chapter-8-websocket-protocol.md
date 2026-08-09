# Chapter 8. WebSocket Protocol

No discussion about protocols, especially ones that are initiated via an HTTP call, would be complete without talking a bit about the history of HTTP. The inception of WebSocket came about because of the massive popularity of Ajax and real-time updates. With HTTP, a protocol where a client requests a resource, and the server responds with the resource or possibly an error code if something went wrong. This unidirectional nature has been worked around by using technologies like Comet and long polling, but comes at a cost of computing resources on the server side. WebSocket seeks to be one of the techniques that solves this problem and allows web developers to implement bidirectional communication over the same HTTP request.

# HTTP 0.9—The Web Is Born

The birth of the World Wide Web brought rise to the first versions of the Hypertext Transfer Protocol (HTTP). The first version of HTTP was conjured up by Tim Berners-Lee in conjunction with the Hypertext Markup Language (HTML). HTTP 0.9 was incredibly simple. A client requests content via the `GET` method:

```
GET /index.html
```

The simplicity of HTTP 0.9 meant that you could request only two things: plain text or HTML. This initial version of HTTP didn’t have headers, so there was no ability to serve any media. In essence, as a client you requested a resource from the server using TCP, and after the server was done sending it, the connection was closed.

# HTTP 1.0 and 1.1

The simplicity in 0.9 was not going to last long. With the next version of HTTP, the complexity involved in an HTTP request/response pair grew. The later versions of HTTP added the ability to send HTTP headers with every request. With that growing number of headers to support, things such as POST (form) requests, media types, caching, and authentication were added in HTTP 1.0. In the latest version, multihomed servers with the Host header, content negotiation, persistent connections, and chunked responses were added and are used in production servers today. The point of all this is that as HTTP has grown in complexity, the size of headers has grown.

According to a Google whitepaper talking about [SPDY](http://bit.ly/chromium-spdy), the average HTTP header is now 800 bytes and often as large as 2 KB. Compression and other techniques are readily available to simplify this situation. The following shows a typical HTTP header from the popular search engine Google:

```
% curl -I http://www.google.com
HTTP/1.1 200 OK
Date: Wed, 20 May 2015 22:50:00 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Set-Cookie: PREF=ID=68769f4bb498a69f:FF=0:T...
Set-Cookie: NID=67=D26hM_BKWVnngC-7_1-XGmBR...
P3P: CP="This is not a P3P policy! See http..."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic,p=0
Transfer-Encoding: chunked
Accept-Ranges: none
Vary: Accept-Encoding
```

I took the liberty of removing the contents of the `cookie` header, and left how many characters it took up in the header. All told, the header was 850 characters long, or just under 1KB. When you’re looking to send data back and forth between server and client and vice versa, having to send a 1KB header on top of that is unnecessary and wasteful. As you’ll see, after the initial handshake, a WebSocket frame header is miniscule in comparison and akin to opening up a TCP connection over HTTP.

The following sections contain code samples showing how to build out portions of the server protocol. Taken together and you can build your own implementation of an RFC-compliant WebSocket server.

# WebSocket Open Handshake

One of the many benefits of the WebSocket protocol is that it begins its connection to the server as a simple HTTP request. Browsers and clients that support WebSocket send the server a request with specific headers that ask for a `Connection: Upgrade` to use WebSocket. The `Connection: Upgrade` header was introduced in HTTP/1.1 to allow the client to notify the server of alternate means of communication. It is primarily used at this point as a means of upgrading HTTP to use WebSocket and can be used to upgrade to HTTP/2.

According to the WebSocket spec, the only indication that a connection to the WebSocket server has been accepted is the header field `Sec-WebSocket-Accept`. The value is a hash of a predefined GUID and the client HTTP header `Sec-WebSocket-Key`.

# From RFC 6455

The `Sec-WebSocket-Accept` header field indicates whether the server is willing to accept the connection. If present, this header field must include a hash of the client’s nonce sent in `Sec-WebSocket-Key` along with a predefined GUID. Any other value must not be interpreted as an acceptance of the connection by the server.

## Sec-WebSocket-Key and Sec-WebSocket-Accept

The first thing the spec asks for on the client side for generating the `Sec-WebSocket-Key` is a nonce, or one-time random value. If you are using a browser that supports WebSocket, generating the `Sec-WebSocket-Key` will be done for you automatically by using the JavaScript API. One of the security restrictions is that an `XMLHttpRequest` will not be allowed to modify that header. As we discussed in [Chapter 6](ch06.html#chapter_6), this ensures that even if the website is compromised, you can trust that the browser will not allow any headers to be modified.

### Generating the Sec-WebSocket-Key

The following code will assume running under Node.js and possibly using WebSocket to communicate with another service acting as the WebSocket server. You’ll use a GUID generated using the `node-uuid` module, which should prove to be random enough for your needs.

The only thing you’re required to do at this point is base64 your nonce and include it in the HTTP headers for your WebSocket connection request. You will use the `node-uuid` module required earlier to create your random string:

```
var uuid = require('node-uuid');

var webSocketKey = function() {
    var wsUUID = uuid.v1();
    return new Buffer(wsUUID).toString('base64');
}
```

### Responding with the Sec-WebSocket-Accept

On the server side, the first thing you’ll do is include the `crypto` module so you can send back your `SHA1` hash of the combined value:

```
var crypto = require('crypto');
```

[RFC 6455](http://bit.ly/rfc-6455) defines a predefined GUID, which you’ll define as a constant in your code:

```
var SPEC_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";
```

Your next task is to define a function in your JavaScript code that accepts the `Sec-WebSocket-Key` as a parameter, and creates a crypto SHA1 hash object:

```
var webSocketAccept = function(secWebsocketKey) {
   var sha1 = crypto.createHash("sha1");
```

Finally, you’ll append the `Sec-WebSocket-Key` together with the predefined GUID, passing that into your SHA1 hash object. The `update` function will update the hash content with your combined data. You pass in `ascii` to identify the input encoding for the SHA1 update:

```
   sha1.update(secWebsocketKey + SPEC_GUID, "ascii");
   return sha1.digest("base64");
```

Generating the `Sec-WebSocket-Accept` header is usually be the job of a server library. It is a good idea to understand the inner workings and have a way of testing if something should go awry.

## WebSocket HTTP Headers

The WebSocket connection must be an HTTP/1.1 `GET` request, and include the following headers:

- `Host`
- `Upgrade: websocket`
- `Connection: Upgrade`
- `Sec-WebSocket-Key`
- `Sec-WebSocket-Version`

If any of these are not included in the HTTP headers, the server should respond with an HTTP error code `400 Bad Request`. Here’s an example of a simple HTTP request to upgrade for WebSocket. The arrangement of the headers is not as important as their existence:

```
GET ws://localhost:8181/ HTTP/1.1
Origin: http://localhost:8181
Host: localhost:8181
Sec-WebSocket-Key: zy6Dy9mSAIM7GJZNf9rI1A==
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Version: 13
```

[Table 8-1](#opening_handshake_headers) shows the possible headers in the opening handshake.

| Header | Required | Value |
| --- | --- | --- |
| `Host` | Yes | Header field containing the server’s authority. |
| `Upgrade` | Yes | websocket |
| `Connection` | Yes | Upgrade |
| `Sec-WebSocket-Key` | Yes | Header field with a base64-encoded value that, when decoded, is 16 bytes in length. |
| `Sec-WebSocket-Version` | Yes | 13 |
| `Origin` | No | Optionally, an `Origin` header field. This header field is sent by all browser clients. A connection attempt lacking this header field *should not* be interpreted as coming from a browser client. Sending the origin domain in the upgrade is so connections can be restricted to prevent CSRF attacks similar to CORS for `XMLHttpRequest`. |
| `Sec-WebSocket-Accept` | Yes (server) | Server sends back an acknowledgment that is described after the table and must be present for the connection to be valid. |
| `Sec-WebSocket-Protocol` | No | Optionally, a `Sec-WebSocket-Protocol` header field, with a list of values indicating which protocols the client would like to speak, ordered by preference. |
| `Sec-WebSocket-Extensions` | No | Optionally, a `Sec-WebSocket-Extensions` header field, with a list of values indicating which extensions the client would like to speak. The interpretation of this header field is discussed in RFC 6455 Section 9.1. |

Upon receiving a valid upgrade request with all required fields, the server will decide on the accepted protocol, and any extensions, and send back an HTTP response with status code 101 along with the `Sec-WebSocket-Accept` handshake acknowledgment. The following code shows a simple response from the server accepting the WebSocket request and opening the channel to communicate using WebSocket:

```
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Sec-WebSocket-Accept: EDJa7WCAQQzMCYNJM42Syuo9SqQ=
Upgrade: websocket
```

Next we’ll go over the WebSocket frame header in detail, at the bit level because the protocol is binary and not text.

# WebSocket Frame

A WebSocket message is composed of one or more frames. The frame is a binary syntax that contains the following pieces of information, each of which I will describe in greater detail. As you may remember from [Chapter 2](ch02.html#chapter_2), the specifics of the frame, fragmentation, and masking are all shielded and kept in the low-level implementation detail of the server and client side. It is definitely good to understand, though, because debugging WebSocket with this information makes things a lot more powerful than without it.

Fin bitIs this the final frame, or is there a continuation?

OpcodeIs this a command frame or data frame?

LengthHow long is the payload?

Extended lengthIf payload is larger than 125, we’ll use the next 2 to 8 bytes.

MaskIs this frame masked?

Masking key4 bytes for the masking key.

Payload dataThe data to send whether binary or UTF-8 string, could be a combination of extension data + payload data.

A WebSocket message may make up multiple frames depending on how the server and client decide to send data back and forth. And because the communication between client and server is bidirectional, at any time either side decides, data can be sent back and forth as long as no close frame was previously sent by either side. The following is a text representation of a WebSocket frame:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
:                     Payload Data continued ...                :
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                     Payload Data continued ...                |
+---------------------------------------------------------------+
```

Let’s talk about each of the header elements in greater detail.

## Fin Bit

The first bit of the WebSocket header is the Fin bit. If the bit is set, this fragment is the final bit in a message. If the bit is clear, the message is not complete with the following fragment. As you’ll see in the next section, the opcode to pass is `0x00`.

## Frame Opcodes

Every frame has an opcode that identifies what the frame represents. These opcodes are defined in [RFC 6455](http://bit.ly/rfc-6455). The initial values are as defined by the IANA in the [WebSocket registry](http://bit.ly/ws-registries) and are currently in use; additions to this are possible with WebSocket Extensions. The opcode is placed within the second 4-bits of the first byte of the frame header. [Table 8-2](#opcode-def) lists the opcode definitions.

| Opcode value | Description |
| --- | --- |
| `0x00` | Continuation frame; this frame continues the payload from the previous. |
| `0x01` | Text frame; this frame includes UTF-8 text data. |
| `0x02` | Binary frame; this frame includes binary data. |
| `0x08` | Connection Close frame; this frame terminates the connection. |
| `0x09` | Ping frame; this frame is a ping. |
| `0x0a` | Pong frame; this frame is a pong. |
| `0x0b-0x0f` | Reserved for future control frames. |

## Masking

By default, all WebSocket frames are to be masked from the client end, and the server is supposed to close the connection if it receives a frame indicating otherwise. As you discovered in [“Frame Masking”](ch06.html#security_frame_masking), the masking introduces variation into the frame to prevent cache poisoning. The second byte of the frame is taken up by the length in the last 7 bits, and the first bit indicates whether the frame is masked. The mask to apply will be the 4 bytes following the extended length of the WebSocket frame header. All messages received by a WebSocket server must be unmasked before further processing:

```
var unmask = function(mask, buffer) {
    var payload = new Buffer(buffer.length);
    for (var i=0; i<buffer.length; i++) {
        payload[i] = mask[i % 4] ^ buffer[i];
    }
    return payload;
}
```

Following unmasking, the server can decode UTF-8 for text-based messages (opcode `0x01`) and deliver unchanged for binary messages (opcode `0x02`).

## Length

The payload length is defined by the last 7 bits of the second byte of the frame header. The first byte is the opcode defined earlier. Depending on how long the payload ends up being, it may or may not use the extended length bytes that follow the first 2 header bytes:

- For messages under 126 bytes (0–125), the length is packed in the last 7 bits of the second byte of the frame header.
- For messages between 126 and 216, two additional bytes are used in the extended length following the initial length. A value of 126 will be placed within the first 7 bits of the length section to indicate usage of the following 2 bytes for length.
- For messages larger than 216, it will end up using the entire 8 bytes following the length. A value of 127 will be placed within the first 7 bits of the length section to indicate usage of the following 8 bytes for length.

## Fragmentation

In two cases, splitting a message into multiple frames could make sense.

One case is that without the ability to fragment messages, the endpoint would have to buffer the entire message before sending so it could send back an accurate count. With the ability to fragment, the endpoint can choose a reasonably sized buffer, and when that is full, send another frame as a continuation until everything is complete.

The second case is multiplexing, in which it isn’t desirable to fill the pipe with data that is being shared, and instead split up into several chunks before sending. Multiplexing isn’t directly supported in the WebSocket protocol but the extension `x-google-mux` can offer support. To learn more about extensions and how they relate to the WebSocket protocol, check out [“WebSocket Extensions”](#websocket_extensions).

If a frame is unfragmented, the Fin bit is set and it contains an opcode other than `0x00`. If fragmented, the same opcode must be used when sending each frame until the message has been completed. In addition, the Fin bit would be `0x00` until the final frame, which would be empty other than the Fin bit set and an opcode of `0x00` used.

If sending a fragmented message, there must be the ability to interleave control frames when either side is accepting communication (if a large message was sent and a control frame wasn’t able to be sent until the end, it would be fairly inefficient). The last necessary thing to remember is that the fragmented message must be all of the same type—no mixing and matching of binary and UTF-8 string data within a single message.

# WebSocket Close Handshake

The closing handshake for a WebSocket connection requires a frame to be sent with the opcode of `0x08`. If the client sends the close frame, it must be masked as is done in all other cases from the client, and not masked coming back from the server. In addition to the opcode, the close frame may contain a body that indicates a reason for closing, in the form of a code and a message. The status code is passed in the body of the message and is a 2-byte unsigned integer. The remainder reason string would follow, and as with WebSocket messages, would be a UTF-8 encoded string.

[Table 8-3](#websocket_registered_status_codes) shows the status codes available for a WebSocket `close` event. Each of the registered status codes in the RFC are identified and described in the next section.

| Status code | Meaning | Description |
| --- | --- | --- |
| `1000` | Normal closure | Send this code when your application has successfully completed. |
| `1001` | Going away | Send this code when either the server or client application is shutting down or closing without expectation of continuing. |
| `1002` | Protocol error | Send this code when connection is closing with a protocol error. |
| `1003` | Unsupported data | Send this code when your application has received a message of an unexpected type that it cannot handle. |
| `1004` | Reserved | Do not use; this is reserved as per RFC 6455. |
| `1005` | No status rcvd | Do not use; the API will use this to indicate when no valid code was received. |
| `1006` | Abnormal closure | Do not use; the API will use this to indicate the connection has closed abnormally. |
| `1007` | Invalid frame payload data | Send this code if the data in the message received was not consistent with the type of the message (e.g., non-UTF-8). |
| `1008` | Policy violation | Send this code when the message received has violated a policy. This is a generic status code that can be returned when there are no more suitable status codes. |
| `1009` | Message too big | Send this code when the message received was too large to process. |
| `1010` | Mandatory ext. | Send this code if you are expecting an extension from the server but it wasn’t returned in the WebSocket handshake. |
| `1011` | Internal error | Send this code when the connection is terminated due to an unexpected condition. |
| `1012` | Service restart | Send this code indicating that the service is restarted, and a client that reconnects should do so with a randomized delay of 5–30s. |
| `1013` | Try again later | Send this code when the server is overloaded and the client should either connect to a different IP (given multiple targets), or reconnect to the same IP when user has performed an action. |
| `1014` | Unassigned | Do not use; this is unassigned but might be changed in future revisions. |
| `1015` | TLS handshake | Do not use; this is sent when the TLS handshake has failed. |

Unlike TCP where connections can be closed at any time without notice, the WebSocket close is a handshake on both sides. The RFC also identifies the ranges and what they mean categorically for your application. In general, you’ll be using the defined range for the current version (`1000` through `1013`), and given any custom codes necessary in your application, the unregistered range `4000`–`4999` is available.

If an endpoint receives a Close frame without sending one, it has to send a Close frame as its response (echoing the status code received). In addition, no more data can pass over a WebSocket connection that has been sent a Close frame previously. There are certainly cases where an endpoint delays sending a Close frame until all of its current message is sent (in the case of fragmented messages), but the likelihood the other end would process that message is not guaranteed.

When an endpoint (client or server) has sent and received a Close frame, the WebSocket connection is closed and the TCP connection must be closed. A server will always close the connection after receiving and sending immediately, while the client should wait for a server to close, or set up a timeout to close the underlying TCP connection in a reasonable amount of time following a Close frame.

The IANA has a registry of the WebSocket status codes to use during the closing handshake.

[Table 8-4](#websocket_close_code_ranges) shows the complete range of status codes for a WebSocket `close` event.

| Status range | Description |
| --- | --- |
| `0–999` | This range is not used for status codes. |
| `1000–2999` | Status codes in this range are either defined by RFC 6455 or will be in future revisions. |
| `3000–3999` | This range is reserved for libraries, frameworks, and applications. |
| `4000–4999` | This range is reserved for private use, and is not registered with the IANA. Feel free to use these values in your code between client and server with prior agreement. |

# WebSocket Subprotocols

The RFC for WebSocket defines subprotocols and protocol negotiation between client and server. In [Chapter 2](ch02.html#chapter_2), you saw how to pass in one or more protocols via the JavaScript WebSocket API. Now that we’re in the chapter dedicated to the innards of WebSocket, you can look at how that negotiation actually happens, or doesn’t. At the lowest level, the negotiation of which protocol to use for a WebSocket connection happens via the HTTP header `Sec-WebSocket-Protocol`. This header is passed in with the initial upgrade request sent by the client:

```
Sec-WebSocket-Protocol: com.acme.chat, com.acme.anotherchat
```

In this instance, the client is telling the server that the two protocols it would like to speak are `chat` or `anotherchat`. At this point, it is up to the server to decide which protocol it will choose. If the server agrees with none of the protocols, it will return null or won’t return that header. If the server agrees with a subprotocol, it will respond with a header such as this:

```
Sec-WebSocket-Protocol: com.acme.anotherchat
```

As you may remember from [Chapter 2](ch02.html#chapter_2), your JavaScript WebSocket object will have the property `protocol` populated with the value chosen by the server, or none if nothing was chosen. In this instance, the API will have the value *com.acme.anotherchat* because the handshake response from the server indicates this as an acceptable protocol to communicate with. A subprotocol doesn’t change the underlying WebSocket protocol, but merely layers on top of it, providing a higher-level communication channel on top of the existing protocol. The ability to change the definition of a WebSocket frame is available to you, however, in the form of [“WebSocket Extensions”](#websocket_extensions).

Remember from [Chapter 2](ch02.html#chapter_2) that three types of subprotocols can be used with the subprotocol handshake. The first are the registered protocols, identified in WebSocket RFC 6455, section 11.5. It defines a registry with the [IANA](http://bit.ly/websocket-protocol-reg). The second are open protocols such as XMPP or STOMP, although you can see registered protocols for these as well. And the third, which you’ll likely use in your application, are the custom protocols, which usually take the form of the domain name with an identifier for the subprotocol name.

# WebSocket Extensions

The WebSocket RFC defines `Sec-WebSocket-Extensions` as an optional HTTP header to be sent by the connecting client asking if the server can support any of the listed extensions. The client will pass one or more extensions with possible parameters via the HTTP header, and the server will respond with one or more accepted extensions. The server can choose only from the client-passed in list.

Extensions have control to add new opcodes and data fields to the framing format. In essence, you can completely change the entire format of a WebSocket frame with a WebSocket extension. One of the earlier specs, `draft-ietf-hybi-thewebsocketprotocol-10`, even mentioned a `deflate-stream` extension, which would compress the entire WebSocket stream. The effectiveness of this is probably the reason it no longer shows up in later specs, because WebSocket has client-to-server frame masking, whereby the mask changes per frame, and with that, deflate would be wholly ineffective.

Here are two examples of extensions that are available in clients today:

- [`deflate-frame`](http://bit.ly/deflate-frame), a better method of deflate (available with Chrome, which uses x-webkit-deflate-frame as its name) where frames are compressed at source and extracted at destination
- [`x-google-mux`](http://bit.ly/x-google-mux), an early-stage extension supporting multiplexing

The one caveat, and it’s been an issue with adoption of any new technology attached to browsers as clients, is that support must be baked into the browsers used by your clients. The server will parse the extensions passed in by the client, and pass back the list it will support. The order of extensions passed back must coincide with what was passed in by the client. It must pass back only extensions that the client has indicated that it also supports.

# Alternate Server Implementations

I have chosen in this book to focus exclusively on using Node.js on the server side. Implementations of the WebSocket protocol on the server side are widespread and covered in nearly every language imaginable. Covering any of these other server-side options is certainly outside the scope of this book. The following is a nonexhaustive list of some of the RFC-compliant implementations of WebSocket in the wild today for some of the most popular languages:

- Java API for WebSocket (JSR-356), which is included in any Java EE 7–compatible server such as Glassfish or Jetty.
- Python has several options, two of which are available at [pywebsocket](http://bit.ly/py-ws) and at [ws4py](http://bit.ly/ws-4py).
- [PHP](http://socketo.me) has a compatible implementation with Ratchet
- Ruby has an EventMachine-based implementation, [em-websocket](http://bit.ly/em-ws).

These are just a few of the more popular implementations in each language. As with any technical decision on the backend, evaluate the options for your chosen platform and use these and the information within this book as a guidepost along the way.

# Summary

This chapter has gone into a lot of detail about the WebSocket protocol—hopefully enough for you to either use it as is, or extend it in the form of subprotocols layered on top of the underlying WebSocket protocol. The WebSocket protocol has taken a long road to get to where it is today, and while changes may occur in the future, it appears to be a solid way to communicate in a more efficient and powerful manner. It is time to do away with the historically necessary hacks of the past, and embrace the power provided by the WebSocket protocol and its API.
