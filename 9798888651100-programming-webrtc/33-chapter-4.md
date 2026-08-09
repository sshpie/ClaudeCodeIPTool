# Chapter 4  
Handling Data Channels

Over the last two chapters, you built the essential core of all WebRTC applications: you connected to a signaling server and established a peer connection according to the perfect-negotiation pattern. You also successfully implemented WebRTC’s most famous feature, which is the ability to stream user media from one peer to another in real time.

But streaming media is only one facet of WebRTC’s capabilities. WebRTC connections can also stream any application data you like, directly from one peer to another, over the RTCDataChannel interface. This chapter picks up right where you left off and will have you adding a couple of features to your video-call app for streaming application data, too.

The first feature you’ll build will enable your users to set filters on their videos. For example, users will be able to set it so that their video streams display in black and white, instead of the normal color coming off of their cameras. We’ll use a data channel to tell the remote peer to set the same filter as the local peer selects. The video-filter feature will help you familiarize yourself with an asymmetric method for adding data channels to a call, and the events that data channels fire as they are added, opened, and closed.

We’ll follow that up with a second, more involved feature backed by data channels: a chat box that will give users the ability to send text messages to each other. In setting up the chat feature, we’ll employ a symmetric method for adding data channels to a call and look more closely at how data is sent and received over WebRTC data channels.

In this chapter, we’ll be sending data in the form of simple strings, which is enough to build these two features. You’ll extend your skills to stream more sophisticated forms of data in Chapter 5, [​*Streaming Complex Data*​](f_0040.xhtml#chp.complexdata).
