# Chapter 3. Bidirectional Chat

Your first full-fledged example is to build a bidirectional chat using WebSocket. The end result will be a server that accepts WebSocket connections and messages for your “chat room” and fans the messages out to connected clients. The WebSocket protocol itself is simple, so to write your chat application, you will manage the collection of message data in an array and hold the socket and unique UUID for the client in locally scoped variables.

# Long Polling

Long polling is a process that keeps a connection to the server alive without having data immediately sent back to the client. Long polling (or a long-held HTTP request) sends a server request that is kept open until it has data, and the client will receive it and reopen a connection soon after receiving data from the server. This, in effect, allows for a persistent connection with the server to send data back and forth.

In practice, two common techniques are available for achieving this. In the first technique, `XMLHttpRequest` is initiated and then held open, waiting for a response from the server. Once this is received, another request is made to the server and held open, awaiting more data. The other technique involves writing out custom script tags possibly pointing to a different domain (cross-domain requests are not allowed with the first method). Requests are then handled in a similar manner and reopened in the typical long-polling fashion.

Long polling is the most common way of implementing this type of application on the Web today. What you will see in this chapter is a much simpler and more efficient method of implementation. In subsequent chapters you will tackle the compatibility issue of older browsers that may not yet support WebSocket.

# Writing a Basic Chat Application

[Chapter 1](ch01.html#chapter_1) showed a basic server that accepted a WebSocket connection and sent any received message from a connected client to the console. Let’s take another look at that code, and add features required for implementing your bidirectional chat:

```
var WebSocketServer = require('ws').Server,
    wss = new WebSocketServer({port: 8181});

wss.on('connection', function(socket) {
    console.log('client connected');
    socket.on('message', function(message) {
        console.log(message);
    });
});
```

The `WebSocketServer` provided by the popular `ws` Node module gets initialized and starts listening on port 8181. You can follow this by listening for a client `connection` event and the subsequent `message` events that follow. The `connection` event accepts a callback function where you pass a `socket` object to be used for listening to messages after a successful connection has occurred. This works well to show off a simple connection for our purposes, and now you’re going to build on top of that by tracking the clients that connect, and sending those messages out to all other connected clients.

The WebSocket protocol does not provide any of this functionality by default; the responsibility for creation and tracking is yours. In later chapters, you will dive into libraries such as Socket.IO that extend the functionality of WebSocket and provide a richer API and backward compatibility with older browsers.

[Figure 3-1](#FIG3.1) shows what the chat application looks like currently.

Building on the code from [Chapter 1](ch01.html#chapter_1), import a Node module for generating a UUID. First things first, you’ll use npm to install `node-uuid`:

```
% npm install node-uuid
```

```
var uuid = require('node-uuid');
```

A UUID is used to identify each client that has connected to the server and add them to a collection. A UUID allows you to target messages from specific users, operate on those users, and provide data targeted for those users as needed.

##### Universally Unique IDentifier

A UUID is a standardized identifier commonly used in building distributed systems and can be assumed “practically unique.” Generally speaking, you won’t run into collisions, but it isn’t guaranteed. Therefore, you should be fine using this as your identifier for your simple chat application.

![webs 0301](/api/v2/epubs/urn:orm:book:9781449369262/files/assets/webs_0301.png)

###### Figure 3-1. Your first WebSocket chat application

Next, you’ll enhance the connection to the server with identification and logging:

```
var clients = [];

wss.on('connection', function(ws) {
  var client_uuid = uuid.v4();
  clients.push({"id": client_uuid, "ws": ws});
  console.log('client [%s] connected', client_uuid);
```

Assigning the result of the `uuid.v4` function to the `client_uuid` variable allows you to reference it later when identifying message sends and any `close` event. A simple metadata object in the form of JSON contains the client UUID along with the WebSocket object.

When the server receives a message from the client, it iterates over all known connected clients using the `clients` collection, and send back a JSON object containing the `message` and `id` of the message sender. You may notice that this also sends back the message to the client that initiated, and this simplicity is by design. On the frontend client you don’t update the list of messages unless it is returned by the server:

```
ws.on('message', function(message) {
  for(var i=0; i<clients.length; i++) {
      var clientSocket = clients[i].ws;
      console.log('client [%s]: %s', clients[i].id, message);
      clientSocket.send(JSON.stringify({
          "id": client_uuid,
          "message": message
      }));
  }
});
```

The WebSocket server now receives `message` events from any of the connected clients. After receiving the message, it iterates through the connected clients and sends a JSON string that includes the unique identifier for the client who sent the message, and the message itself. Every connected client will receive this JSON string and can show this to the end user.

A server must handle error states gracefully and still continue to work. You haven’t yet defined what to do in the case of a WebSocket `close` event, but there is something missing that needs to be addressed in the `message` event code. The collection of connected clients needs to account for the possibility that the client has gone away, and ensure that before you send a `message`, there is still an open WebSocket connection.

The new code is as follows:

```
ws.on('message', function(message) {
  for(var i=0; i<clients.length; i++) {
      var clientSocket = clients[i].ws;
      if(clientSocket.readyState === WebSocket.OPEN) {
        console.log('client [%s]: %s', clients[i].id, message);
        clientSocket.send(JSON.stringify({
            "id": client_uuid,
            "message": message
        }));
      }
  }
});
```

You now have a server that will accept connections from WebSocket clients, and will rebroadcast received messages to all connected clients. The final thing to handle is the `close` event:

```
ws.on('close', function() {
  for(var i=0; i<clients.length; i++) {
      if(clients[i].id == client_uuid) {
          console.log('client [%s] disconnected', client_uuid);
          clients.splice(i, 1);
      }
  }
});
```

The server listens for a `close` event, and upon receiving it for this client, iterates through the collection and removes the client. Couple this with the check of the `readyState` flag for your WebSocket object and you’ve got a server that will work with your new client.

Later in this chapter you will broadcast the state of disconnected and connected clients along with your chat messages.

# WebSocket Client

The simple `echo` client from [Chapter 1](ch01.html#chapter_1) can be used as a jumping off point for your chat web app. All the connection handling will work as specified, and you’ll need to listen for the `onmessage` event that was being ignored previously:

```
ws.onmessage = function(e) {
  var data = JSON.parse(e.data);
  var messages = document.getElementById('messages');
  var message = document.createElement("li");
  message.innerHTML = data.message;
  messages.appendChild(message);
}
```

The client receives a message from the server in the form of a JSON object. Using JavaScript’s built-in parsing function returns an object that can be used to extract the message field. Let’s add a simple unordered list above the form so messages can be appended using the DOM methods shown in the function. Add the following above the form element:

```
<ul id="messages"></ul>
```

Messages will be appended to the list using the DOM method `appendChild`, and shown in every connected client. So far you have only scratched the surface of functionality that shows off the seamless messaging provided by the WebSocket protocol. In the next section you will implement a method of identifying clients by a nickname.

# Client Identity

The WebSocket specification has been left relatively simplistic in terms of implementation and lacks some of the features seen in alternatives. In your code so far, you have already gone a long way toward identifying each client individually. Now you can add nickname identities to the client and server code:

```
var nickname = client_uuid.substr(0, 8);
clients.push({"id": client_uuid, "ws": ws, "nickname": nickname});
```

The server gets modified to add the field `nickname` to a locally stored JSON object for this client. To uniquely identify a connected client who hasn’t identified a nickname choice, you can use the first eight characters of the UUID and assign that to the `nickname` variable. All of this will be sent back over an open WebSocket connection between the server and all of its connected clients.

You will use a convention used with Internet Relay Chat clients (IRC) and accept `/nick` `new_nick` as the command for changing the client nickname from the random string:

```
if(message.indexOf('/nick') == 0) {
  var nickname_array = message.split(' ')
  if(nickname_array.length >= 2) {
    var old_nickname = nickname;
    nickname = nickname_array[1];
    for(var i=0; i<clients.length; i++) {
      var clientSocket = clients[i].ws;
      var nickname_message = "Client " + old_nickname +
      " changed to " + nickname;
      clientSocket.send(JSON.stringify({
        "id": client_uuid,
        "nickname": nickname,
        "message": nickname_message
      }));
    }
  }
}
```

This code checks for the existence of the `/nick` command followed by a string of characters representing a nickname. Update your `nickname` variable, and you can build a notification string to send to all connected clients over the existing open connection.

The clients don’t yet know about this new field, because the JSON you originally sent included only `id` and `message`. Add the field with the following code:

```
clientSocket.send(JSON.stringify({
    "id": client_uuid,
    "nickname": nickname,
    "message": message
}));
```

The `appendLog` function within the client frontend needs to be modified to support the addition of the `nickname` variable:

```
function appendLog(nickname, message) {
  var messages = document.getElementById('messages');
  var messageElem = document.createElement("li");
  var message_text = "[" + nickname + "] - " + message;
  messageElem.innerHTML = message_text;
  messages.appendChild(messageElem);
}
```

[Figure 3-2](#FIG3.2) shows your chat application with the addition of identity.

![webs 0302](/api/v2/epubs/urn:orm:book:9781449369262/files/assets/webs_0302.png)

###### Figure 3-2. Identity-enabled chat

Your new function signature includes `nickname` along with `message`, and you can preface every message now with the client nickname. At the client’s request, you can see a nickname preceding messages rather than a random string of characters before each message.

# Events and Notifications

If you were in the middle of a conversation and another person magically appeared in front of you and started talking, that would be odd. To alleviate this, you can add notification of connection or disconnection and send that back to all connected clients.

Your code has several instances where you’ve gone through the trouble of iterating over all connected clients, checking the `readyState` of the socket, and sending a similar JSON-encoded string with varying values. For good measure, you’ll extract this into a generic function, and call it from several places in your code instead:

```
function wsSend(type, client_uuid, nickname, message) {
  for(var i=0; i<clients.length; i++) {
    var clientSocket = clients[i].ws;
    if(clientSocket.readyState === WebSocket.OPEN) {
      clientSocket.send(JSON.stringify({
        "type": type,
        "id": client_uuid,
        "nickname": nickname,
        "message": message
      }));
    }
  }
}
```

With this generic function, you can send notifications to all connected clients, handle the connection state, and encode the string as the client expects, like so:

```
wss.on('connection', function(ws) {
    ...
      wsSend("message", client_uuid, nickname, message);
    ...
});
```

Sending messages to all clients post connection is now simple. Connection messages, disconnection messages, and any notification you need are now handled with your new function.

# The Server

Here is the complete code for the server:

```
var WebSocket = require('ws');
var WebSocketServer = WebSocket.Server,
    wss = new WebSocketServer({port: 8181});
var uuid = require('node-uuid');

var clients = [];

function wsSend(type, client_uuid, nickname, message) {
  for(var i=0; i<clients.length; i++) {
    var clientSocket = clients[i].ws;
    if(clientSocket.readyState === WebSocket.OPEN) {
      clientSocket.send(JSON.stringify({
        "type": type,
        "id": client_uuid,
        "nickname": nickname,
        "message": message
      }));
    }
  }
}

var clientIndex = 1;

wss.on('connection', function(ws) {
  var client_uuid = uuid.v4();
  var nickname = "AnonymousUser"+clientIndex;
  clientIndex+=1;
  clients.push({"id": client_uuid, "ws": ws, "nickname": nickname});
  console.log('client [%s] connected', client_uuid);

  var connect_message = nickname + " has connected";
  wsSend("notification", client_uuid, nickname, connect_message);

  ws.on('message', function(message) {
    if(message.indexOf('/nick') === 0) {
      var nickname_array = message.split(' ');
      if(nickname_array.length >= 2) {
        var old_nickname = nickname;
        nickname = nickname_array[1];
        var nickname_message = "Client "+old_nickname+" changed to "+nickname;
        wsSend("nick_update", client_uuid, nickname, nickname_message);
      }
    } else {
      wsSend("message", client_uuid, nickname, message);
    }
  });

  var closeSocket = function(customMessage) {
    for(var i=0; i<clients.length; i++) {
        if(clients[i].id == client_uuid) {
            var disconnect_message;
            if(customMessage) {
                disconnect_message = customMessage;
            } else {
                disconnect_message = nickname + " has disconnected";
            }
          wsSend("notification", client_uuid, nickname, disconnect_message);
          clients.splice(i, 1);
        }
    }
  }
  ws.on('close', function() {
      closeSocket();
  });

  process.on('SIGINT', function() {
      console.log("Closing things");
      closeSocket('Server has disconnected');
      process.exit();
  });
});
```

# The Client

Here is the complete code for the client:

```
<!DOCTYPE html>
<html lang="en">
<head>
<title>Bi-directional WebSocket Chat Demo</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://bit.ly/cdn-bootstrap-css">
<link rel="stylesheet" href="http://bit.ly/cdn-bootstrap-theme">
<script src="http://bit.ly/cdn-bootstrap-jq"></script>

    <script>
            var ws = new WebSocket("ws://localhost:8181");
            var nickname = "";
            ws.onopen = function(e) {
              console.log('Connection to server opened');
            }
            function appendLog(type, nickname, message) {
              var messages = document.getElementById('messages');
              var messageElem = document.createElement("li");
              var preface_label;
              if(type==='notification') {
                  preface_label = "<span class=\"label label-info\">*</span>";
              } else if(type=='nick_update') {
                  preface_label = "<span class=\"label label-warning\">*</span>";
              } else {
                  preface_label = "<span class=\"label label-success\">"
                  + nickname + "</span>";
              }
              var message_text = "<h2>" + preface_label + "&nbsp;&nbsp;"
              + message + "</h2>";
              messageElem.innerHTML = message_text;
              messages.appendChild(messageElem);
            }

            ws.onmessage = function(e) {
              var data = JSON.parse(e.data);
              nickname = data.nickname;
              appendLog(data.type, data.nickname, data.message);
              console.log("ID: [%s] = %s", data.id, data.message);
            }
            ws.onclose = function(e) {
              appendLog("Connection closed");
              console.log("Connection closed");
            }
            function sendMessage() {
               var messageField = document.getElementById('message');
               if(ws.readyState === WebSocket.OPEN) {
                   ws.send(messageField.value);
               }
               messageField.value = '';
               messageField.focus();
            }
            function disconnect() {
              ws.close();
            }
    </script>

</head>
<body lang="en">
    <div class="vertical-center">
    <div class="container">
    <ul id="messages" class="list-unstyled">

    </ul>
    <hr />
    <form role="form" id="chat_form" onsubmit="sendMessage(); return false;">
        <div class="form-group">
        <input class="form-control" type="text" id="message" name="message"
          placeholder="Type text to echo in here" value="" autofocus/>
        </div>
<button type="button" id="send" class="btn btn-primary"
  onclick="sendMessage();">Send Message</button>
  </form>
  </div>
  </div>
<script src="http://bit.ly/cdn-bootstrap-minjs"></script>
</body>
</html>
```

[Figure 3-3](#FIG3.3) shows the chat application with the addition of notifications.

![webs 0303](/api/v2/epubs/urn:orm:book:9781449369262/files/assets/webs_0303.png)

###### Figure 3-3. Notification-enabled chatbsoc

# Summary

In this chapter you built out a complete chat client and server using the WebSocket protocol. You steadily built a simplistic chat application into something more robust with only the WebSocket API as your technology of choice. Effective and optimized experiences between internal applications, live chat, and layering other protocols over HTTP are all possibilities that are native to WebSocket.

All of this is possible with other technology, and as you’ve probably learned before, there’s more than one way to solve a problem. Comet and Ajax are both battle tested to deliver similar experiences to the end user as provided by WebSocket. Using them, however, is rife with inefficiency, latency, unnecessary requests, and unneeded connections to the server. Only WebSocket removes that overhead and gives you a socket that is full-duplex, bidirectional, and ready to rock ‘n’ roll.

In the next chapter you’ll take a look at a popular protocol for layering on top of WebSocket, to provide transport without the overhead of HTTP.
