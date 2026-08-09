# Chapter 6. WebSocket Security

This chapter details the WebSocket security apparatus and the various ways you can use it to secure the data being passed over the underlying protocol. You’ll learn why it is always a good idea to communicate over TLS (Transport Layer Security) to avoid ineffective proxies and man-in-the-middle attacks, and ensure frame delivery. Discussion focuses on setup of the WebSocket connection over TLS with `wss://` (WebSocket Secure), origin-based security, frame masking, and specific limits imposed by browsers to ensure messages don’t get hijacked.

As with any discussion about security, the content of this chapter presents today’s best-known data about properly securing your WebSocket communication. Security is fickle, though, and the cat-and-mouse game played with those who seek to exploit and those who work to block is constant and unending. Data validation and multiple checks are even more important while using WebSocket. You’ll begin by setting up WebSocket over TLS.

# TLS and WebSocket

All of the demos so far have used the unencrypted version of WebSocket communication with the `ws://` connection string. In practice, this should happen only in the simplest hierarchies, and all communication via WebSocket should happen over TLS.

## Generating a Self-Signed Certificate

A valid TLS-based connection over WebSocket can’t be done without a valid certificate. What I’ll go over fairly quickly here is a way to generate a self-signed certificate using OpenSSL. The first thing you’ll need to do is ensure that if you don’t already have [OpenSSL](https://www.openssl.org/) installed, you follow the set of instructions presented next that is specific to your platform.

## Installing on Windows

This section covers only downloading and installing the precompiled binary available on Windows. As we discussed in [Chapter 1](ch01.html#chapter_1), for the masochistic among us, you can [download the source](http://openssl.org/source/) and compile it yourself.

For the rest of us, [download the standalone Windows executable](http://bit.ly/openssl-win). You should be able to run OpenSSL after this via the examples following the instructions on OS X and Linux installs.

## Installing on OS X

The easiest method of installing OpenSSL on OS X is via a package manager like [Homebrew](http://bit.ly/homebrew-osx). This allows for quick and easy updating without having to redownload a package from the Web. Assuming you have Homebrew installed:

```
brew install openssl
```

## Installing on Linux

There are so many flavors of Linux that it would be impossible to illustrate how to install on all of them. I will reiterate how to install it via apt on [Ubuntu](http://www.ubuntu.com). If you’re running another distro, you can read through the [Compilation and Installation](http://bit.ly/openssl-linux) instructions from OpenSSL.

Using apt for installation requires a few simple steps:

```
sudo apt-get update
sudo apt-get install openssl
```

## Setting up WebSocket over TLS

Now that you have [OpenSSL](https://www.openssl.org/) installed, you can use it for the purposes of generating a certificate to be used for testing, or to submit to a certificate authority.

###### Note

A certificate authority (CA) issues digital certificates in a public key infrastructure (PKI). The CA is a trusted entity that certifies the ownership of a public key as the named subject of the certificate. The certificate can be used to validate that ownership, and encrypt all information going over the wire.

Here’s what you’re going to do in the following block of code:

- Generate a 2048-bit key with a passphrase
- Rewrite that key removing the passphrase
- Create a certificate signing request (CSR) from that key
- Generate a self-signed certificate from the key and CSR

The first thing to do is generate a 2048-bit key. Do this by using the `openssl` command to generate the RSA key pair:

```
% openssl genrsa -des3 -passout pass:x -out server.pass.key 2048

Generating RSA private key, 2048 bit long modulus
...............................................................................
+++........+++
e is 65537 (0x10001)
```

Next, you generate a private key sans passphrase for eventual creation of a CSR, which can be used for a self-signed certificate, or to receive a certificate authorized by a certificate authority. After generating the key, you can remove the key with the passphrase as well:

```
% openssl rsa -passin pass:x -in server.pass.key -out server.key
writing RSA key
% rm server.pass.key
```

Now that you have your private key, you can use that to create a CSR that will be used to generate the self-signed certificate for sending secure WebSocket communication:

```
% openssl req -new -key server.key -out server.csr
      -subj '/C=US/ST=California/L=Los Angeles/O=Mystic Coders, LLC/
             OU=Information Technology/CN=ws.mysticcoders.com/
             emailAddress=fakeemail AT gmail DOT com/
             subjectAltName=DNS.1=endpoint.com' > server.csr
```

If you’re looking to get set up with a proper server certificate, the CSR file is all you need. You will receive a certificate file from the Certificate Authority, which you can then use. While you wait, though, let’s get the self-signed certificate for testing and replace it later.

Use the following code to generate your certificate for use in the server code:

```
% openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
Signature ok
subject=/C=US/ST=California/L=Los Angeles/...
Getting Private key
```

In the directory you’ve chosen to run everything in, you should now have three files:

- *server.key*
- *server.csr*
- *server.crt*

If you decide to send things to a Certificate Authority for a validated certificate, you’ll send the *server.csr* file along with the setup procedure to receive a key. Because you’re just going to use a self-signed certificate here for testing purposes, you’ll continue with your generated certificate *server.crt*. Decide where you’ll keep the private key and certificate files (in this instance you’ll place them in */etc/ssl/certs*).

## WebSocket Server over TLS Example

In the following code you’ll see an example of using the `https` module to allow the bidirectional WebSocket communication to happen over TLS and listen on port 8080:

```
var fs = require('fs');

// you'll probably load configuration from config
var cfg = {
    ssl: true,
    port: 8080,
    ssl_key: '/etc/ssl/certs/server.key',
    ssl_cert: '/etc/ssl/certs/server.crt'
};

var httpsServ = require('https');
var WebSocket = require('ws');
var WebSocketServer = WebSocket.Server;

var app = null;

// dummy request processing
var processRequest = function( req, res ) {
    res.writeHead(200);
    res.end("Hi!\n");
};

app = httpsServ.createServer({
    key: fs.readFileSync( cfg.ssl_key ),
    cert: fs.readFileSync( cfg.ssl_cert )

}, processRequest ).listen( cfg.port );

var wss = new WebSocketServer( { server: app } );

wss.on( 'connection', function ( wsConnect ) {

    wsConnect.on( 'message', function ( message ) {
        console.log( message );
    });

});
```

Changing client code to use a WebSocket connection over TLS is trivial:

```
var ws = new WebSocket("wss://localhost:8080");
```

When making this connection, the web page being used to load it must also connect over TLS. In fact, if you attempt to load an insecure WebSocket connection from a website using the `https` protocol, it will throw a security error in most modern browsers for attempting to load insecure content. Mixed content is a common attack vector and is rightfully discouraged from being allowed. In most modern browsers, the use of mixed content is not only actively discouraged, it is forbidden. Chrome, Firefox, and Internet Explorer all throw security errors and will refuse to communicate over anything other than WebSocket Secure in the event the page being loaded is also served over TLS. Safari, unfortunately, does not do the proper thing. [Figure 6-1](#FIG6.1) is an example from Chrome showing the errors in console upon attempting to connect to an insecure WebSocket server.

![webs 0601](/api/v2/epubs/urn:orm:book:9781449369262/files/assets/webs_0601.png)

###### Figure 6-1. Mixed content security error with Chrome

[Qualys Labs has a nice chart](http://bit.ly/qualys-mixed) identifying the browsers that handle mixed content properly, and those that do not.

Now that your connection is encrypted, we’ll dive into other methods of securing the communications channel in the next section.

# Origin-Based Security Model

There has always been a race between those who seek to exploit vulnerabilities in a transport mechanism and those who seek to protect it. The WebSocket protocol is no exception. When `XMLHttpRequest` (XHR) first appeared with Internet Explorer, it was limited to the same-origin policy (SOP) for all requests to the server. There are innumerable ways that this can be exploited, but it worked well enough. As the use of XHR evolved, though, allowing access to other domains became necessary. Cross Origin Resource Sharing (CORS) was the result of this effort; if used properly, CORS can minimize cross-site scripting attacks while still allowing flexibility.

###### Note

CORS, or Cross-Origin Resource Sharing, is a method of access control employed by the browser, usually for Ajax requests from a domain outside the originating domain. For further information about CORS, see the [Mozilla docs](http://bit.ly/mdn-cors).

WebSocket doesn’t place any same-origin policy restriction on accessing WebSocket servers. It also doesn’t employ CORS. What you’re left with in regards to `Origin` validation is server-side verification. All of the previous examples used the simple and fast [`ws` library with Node.js](https://github.com/einaros/ws). You’ll continue to do so and see in the initialization how simple it is to employ an origin check to ensure connection from the browser is only the expected `Origin`:

```
var WebSocketServer = require('ws').Server,
    wss = new WebSocketServer({
      port: 8181,
      origin: 'http://mydomain.com',
        verifyClient: function(info, callback) {
            if(info.origin === 'http://mydomain.com') {
                callback(true);
                return;
            }
            callback(false);
        }
    }),
```

If you write a `verifyClient` function for the library you’re using, you can send a callback with either `true` or `false` indicating a successful validation of any information, including the `Origin` header. Upon success, you will see a valid upgraded HTTP exchange for the `Origin` `http://mydomain.com`.

The HTTP exchange that happens as a result is as follows:

```
GET ws://mydomain.com/ HTTP/1.1
Origin: http://mydomain.com
Host: http://mydomain.com
Sec-WebSocket-Key: zy6Dy9mSAIM7GJZNf9rI1A==
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Version: 13
```

```
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Sec-WebSocket-Accept: EDJa7WCAQQzMCYNJM42Syuo9SqQ=
Upgrade: websocket
```

If the `Origin` header doesn’t match up, the `ws` library will send back a 401 Unauthorized header. The connection will never complete the handshake, and no data can be sent back and forth. If this happens, you’ll receive a response similar to the following:

```
HTTP/1.1 401 Unauthorized
Content-type: text/html
```

It should also be noted that verifying the `Origin` header does not constitute a secure and authorized connection by a valid client. You could just as easily pass the proper `Origin` header from a script run outside the browser. The `Origin` header can be spoofed with close to no effort at all outside the browser. Therefore, additional strategies must be employed to ensure your connection is authorized.

The major benefit of requiring the `Origin` header is to combat WebSocket-like Cross-Site Request Forgery (CSRF) attacks, also called [Cross-Site WebSocket Hijacking (CSWSH)](http://bit.ly/cswsh-vulnerability), from being possible as the `Origin` header is passed by the user agent, and cannot be modified by JavaScript code. Implicit trust, therefore, goes to the client browser in this instance, and the restrictions it places on web-based code.

## Clickjacking

One other area of concern with WebSocket and the Web at large is termed [*clickjacking*](http://bit.ly/clickjack-wiki). The process involves framing the client-requested website and executing code in the hidden frame without the user’s awareness.

To combat this, web developers have devised methods called [*framebusting*](http://bit.ly/framebuster-wiki) to ensure that the website their users are visiting is not being framed in any way.

A simple and naive way to bust out of a frame is as follows:

```
if (top.location != location) {
    top.location = self.location;
}
```

This tends to fail, however, due to inconsistencies in how browsers have handled these properties with JavaScript in the past. Other problems that creep up are availability of JavaScript on the system, or possibly in the iframe, which can be restricted in certain browsers.

The most thorough JavaScript-based framebusting technique available, which comes from a study by the [Stanford Web Security Research on framebusting](http://bit.ly/stanford-framebusting), is outlined in the following snippet:

```
<style>
body { display: none; }
</style>

<script>
if(self===top) {
  documents.getElementsByTagName("body")[0].style.display = 'block';
} else {
  top.location = self.location;
}
</script>
```

Of all the JavaScript-based solutions, this allows you to stop the user from viewing your page if it is being framed. The page will also remain blank if JavaScript is turned off or any other way of exploiting the framebusting code is attempted. Because WebSocket is JavaScript based, busting any frames will remove any ability for an attacker to hijack the browser and execute code without the users’ knowledge. Next you’ll look at a header-based approach that can be used in conjunction with the preceding script, and a proof of concept called Waldo, which takes advantage of this attack vector. Using the techniques mentioned here will render the Waldo code moot.

## X-Frame-Options for Framebusting

The safest method of getting around clickjacking was introduced by Microsoft with Internet Explorer 8 and involves an HTTP header option called `X-Frame-Options`. The solution caught on and has become popular among all major browsers including Safari, Firefox, Chrome, and Opera, and has been officially standardized as [RFC 7034](http://bit.ly/rfc-7034). It remains the most effective way of busting out of frames. [Table 6-1](#xframe_options_acceptable) shows the acceptable values that can be passed by the server to ensure that only acceptable policies are being used for framing the website.

| Header value | Description of behavior |
| --- | --- |
| `DENY` | Prevents framing code at all |
| `SAMEORIGIN` | Prevents framing by external sites |
| `ALLOW-FROM` *`origin`* | Allows framing only by the specified site |

Why does all this matter in regards to WebSocket communication? A proof of concept called [Waldo](http://bit.ly/waldo-websockets) shows how simple it can be for a compromised bit of JavaScript to control and report data back to a WebSocket server. These are a few of the things Waldo is able to achieve:

- Send back cookies or DOM
- Install and retrieve results of keylogger
- Execute custom JavaScript
- Use in a denial-of-service attack

Modern browsers all support WebSocket, and the only real defense against this attack vector is anti-framing countermeasures such as `X-Frame-Options` and, to a lesser extent, the other JavaScript-based frame-buster code reviewed previously.

If you’d like to test Waldo, you can find installation instructions on the website. Please be aware that versions of supporting libraries that Waldo uses have advanced.

Here are the supported versions for compiling Waldo:

- [websocketpp](http://bit.ly/websocketpp) WebSocket library (version 0.2.x)
- [Boost](http://www.boost.org/) with version 1.47.0 (can use package manager)

After installing `websocketpp` and downloading [*waldo.zip*](http://bit.ly/waldo-source-code), modify the *common.mk* file with correct paths for `boost` and `websocketpp` and build. Create a simple HTML page that includes the compromised JavaScript in a hidden frame and load the regular website in another frame. Ensure you have the Waldo C++ app running, and control at will. Waldo is completely relevant, as it was released based on RFC 6455 and still works fine on the latest browsers.

For more in-depth tools that allow you to use the browser as an attack vector, including using WebSocket to perform these tests, check out [BeEF](http://beefproject.com/), which comes with a RESTful and GUI interface, and [XSSChef](http://bit.ly/xsschef), which installs as a compromised Google Chrome extension.

# Denial of Service

WebSocket by its very nature opens connections and keeps them open. An attack vector that has been commonly used with HTTP-based web servers is to open hundreds of connections and keep them open indefinitely by slowly trickling valid data back to the web server to keep a timeout from occurring and exhausting the available threads used on the server. The term given to the attack is [Slowloris](http://bit.ly/slowloris-wiki), and while more asynchronous servers such as [nginx](http://nginx.org) can mitigate the effect, it is not always completely effective. Some best practices to look at to lessen this attack include the following:

- Add IP-based limitation to ensure that connections coming from a single source are not overwhelming the number of available connections.
- Ensure that any actions being requested by a user are spawned asynchronously on the server end to lessen the impact of connected clients.

# Frame Masking

The WebSocket protocol (RFC 6455), discussed in a lot more detail in [Chapter 8](ch08.html#chapter_8), defines a 32-bit masking key that is set using the `MASK` bit in the WebSocket frame. The mask is a random key chosen by the client, and it is a best practice that all clients set the `MASK` bit along with passing the obligatory masking key. Each frame must include a random masking key from the client side to be considered valid. The masking key is then used to XOR the payload data before sending to the server, and the payload data length will be unchanged.

You may be saying to yourself, “That’s great, but why should I care about this when we’re talking about security?” Two words: cache poisoning. The reality of an app in the wild is that you cannot control misbehaving proxy servers, and the relative newness of WebSocket unfortunately means that it can be an attack vector for the malicious.

A paper in 2011 titled [“Talking to Yourself for Fun and Profit”](http://bit.ly/cmu-talking) outlined multiple methods for fooling a proxy into serving up the attacker’s JavaScript file. Masking in effect introduces a bit of variability that is injected into every client message, which cannot be exploited by an attacker’s malicious JavaScript code. Data masking ensures that cache poisoning is less likely to happen due to variability in the data packets.

The downside of masking is that it also prevents security tools from identifying patterns in the traffic. Unfortunately, because WebSocket is still a rather new protocol, a good number of proxies, firewalls, and network and endpoint DLP (data loss prevention) software are unable to properly inspect the packets being sent across the wire. In addition, because many tools don’t know how to properly inspect WebSocket frames, dData can be hidden in reserved flags, buffer overflows or underflows are possible, and malicious JavaScript code can be hidden in the mask frame as well.

Trust no one.

# Validating Clients

There are many ways to validate clients attempting to connect to your WebSocket server. Due to restrictions on the browser for connection over WebSocket, there is no ability to pass any custom HTTP headers during the handshake. Therefore, the two most common methods of implementing auth are using the Basic header and using form-based auth with a set cookie. This example employs the latter method and uses a simple username/password form, setting and reading the cookie in your WebSocket server.

## Setting Up Dependencies and Inits

Because the solution uses shared keys via a cookie, you’ll need to get some dependencies in place. The libraries you’ll use are all listed here with the `npm` commands:

```
% npm install ws
% npm install express
% npm install body-parser
% npm install cookie
```

You likely have the `ws` library installed in your environment from previous examples. You will be using `express` and plug-ins for parsing form and cookie data: `body-parser` and `cookie`. The remaining dependency is `fs`, which you’ll use to read your TLS certificate files.

Back to your server code—the first thing to do is set up your imports with `require`:

```
var fs = require('fs');
var https = require('https');
var cookie = require('cookie');
var bodyParser = require('body-parser');
var express = require('express');
var WebSocket = require('ws');
```

Now that you have all the necessary dependencies in place, set up the self-signed certificate and initialize `express` and the HTTPS server backing it. You can use the same self-signed cert that you set up earlier in this chapter:

```
var WebSocketServer = WebSocket.Server;

var credentials = {
    key: fs.readFileSync('server.key', 'utf8'),
    cert: fs.readFileSync('server.crt', 'utf8')};

var app = express();

app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true }));

var httpsServer = https.createServer(credentials, app);
httpsServer.listen(8443);
```

## Listening for Web Requests

In order for your form-based auth to work, you will be serving up a login page and a secured page, which will require that a cookie named `credentials` is found and has the proper key within. For brevity, you will use the username/password combination of `test`/`test` and use a predefined key that never changes. In your own code, however, this data should be saved to a data source of your choosing that can also be retrieved by the WebSocket server. Stub methods will be used to show where you would insert the retrieval and storage code in whatever data source you decide to use in your own application.

Following is the HTML for the login example, which you’ll serve from your `express` server. Save this in your project directory and name it *login.html*:

```
<html>
<head>
<title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" action="/login" name="login">
        Username: <input type="text" name="username" />
        Password: <input type="password" name="password" />
        <input type="submit" value="Login" />
    </form>
</body>
</html>
```

You will listen for `GET` and `POST` requests at the URL `/login`, and a `GET` request for `/secured`, which does a check on the cookie to ensure existence and redirects if not found:

```
app.get('/login', function (req, res) {
    fs.readFile('./login.html', function(err, html) {
        if(err) {
            throw err;
        }
        res.writeHeader(200, {"Content-Type": "text/html"});
        res.write(html);
        res.end();
    });
});

app.post("/login", function(req, res) {
    if(req.body !== 'undefined') {
        key = validateLogin(req.body['username'], req.body['password']);
        if(key) {
            res.cookie('credentials', key);
            res.redirect('/secured');
            return;
        }
    }
    res.sendStatus(401);
});

var validateLogin = function(username, password) {
    if(username == 'test' && password == 'test') {
        return '591a86e4-5d9d-4bc6-8b3e-6447cd671190';
    } else {
        return null;
    }
}

app.get('/secured', function(req, res) {
    cookies = cookie.parse(req.headers['cookie']);
    if(!cookies.hasOwnProperty('credentials')
         && cookies['credentials'] !== '591a86e4-5d9d-4bc6-8b3e-6447cd671190') {
        res.redirect('/login');
    } else {
        fs.readFile('./secured.html', function(err, html) {
            if(err) {
                throw err;
            }
            res.writeHeader(200, {"Content-Type": "text/html"});
            res.write(html);
            res.end();
        });
    }
});
```

As you can see, you’ve stubbed out a `validateLogin` method, which in this simple implementation just checks to ensure that the username and password are both `test`. After a successful validation, it passes back the `key`. In a production implementation, I would opt for storing this key in a data store, which can then be retrieved and validated with the WebSocket server end. We’re cheating a bit to not add any unnecessary dependencies to this example. The HTML served up by the `/secured` endpoint as follows:

```
<html>
<head>
<title>WebSocket Auth Example</title>
<script
src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script type="text/javascript">

$(function() {
  var ws = new WebSocket("wss://localhost:8443");

  ws.onopen = function(e) {
    console.log('Connection to server opened');
  }
});
</script>
</head>
<body>
Hello, WebSocket.
</body>
</html>
```

Now you have all the web endpoints being served to the user, and a WebSocket client that is connecting securely over TLS to port 8443.

## WebSocket Server

You’ve handled the web end of the spectrum, and you have a WebSocket client all loaded up and ready to send messages to your WebSocket endpoint. In the same source file, you’ll include code to spin up a secure WebSocket server and use `verifyClient` to check for your `credentials` cookie. The first thing you do is ensure you are talking over a secure channel and if not, return `false` to the callback failing the connection. Then, check the cookie header and call the `checkAuth` function, which in production code would look up the key in a data source and validate that the client indeed can access this service. If all goes well, return `true` to the callback and allow the connection to proceed:

```
var checkAuth = function(key) {
    return key === '591a86e4-5d9d-4bc6-8b3e-6447cd671190';
}

var wss = new WebSocketServer({
    server: httpsServer,
    verifyClient: function(info, callback) {
        if(info.secure !== true) {
            callback(false);
            return;
        }
        var parsed_cookie = cookie.parse(info.req.headers['cookie']);

        if('credentials' in parsed_cookie) {
            if(checkAuth(parsed_cookie['credentials'])) {
                callback(true);
                return;
            }
        }
        callback(false);
    }

});
wss.on('connection', function( wsConnect ) {
    wsConnect.on('message', function(message) {
        console.log(message);
    });
});
```

As you can see, this is an end-to-end solution for validating that a WebSocket connection is authorized to continue. You can add other checks as needed, depending on the application being built. Just remember that the client browser cannot set any headers, so cookies and the `Basic` header are all you are afforded. This should give you the structure to enable you to build this out into your own applications in a secure manner, away from prying eyes.

# Summary

This chapter looked at various attack vectors and ways of securing your WebSocket application. The primary takeaway should be to assume that the client is not a browser, and so do not trust it.

Three things to remember:

- Always use TLS.
- Server code should always verify the `Origin` header.
- Verify the request by using a random token similar to a CSRF token for Ajax requests.

It is even more important to use the items discussed in this chapter so the possibility of someone hijacking the WebSocket connection for other nefarious purposes is heavily minimized. In the next chapter we’ll review several ways of debugging WebSocket and actively measuring the performance benefits over a regular Ajax-based request.
