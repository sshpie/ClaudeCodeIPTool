# Chapter 5  
Streaming Complex Data

Sending simple messages is pretty great: it’s a small but satisfying taste of what WebRTC data channels enable us to build. Bask in your success for a moment, and think about all that is happening in your browser at this point: you’ve built an app that streams video and allows two connected peers to set and share filters on their videos. You’ve enhanced the app further by providing the interface and logic for those peers to exchange text messages with each other, including outside of a connected call, thanks to the message queue you wrote.

In short, you’re now able to do some pretty fancy things with WebRTC. And they’re only going to get fancier: in this chapter alone, you will be pushing the capabilities of data channels even further to exchange more complex data, including JSON strings and binary data. You’re also going to learn how to add audio to the video you’ve been streaming. To keep your users happy, you’ll also be adding buttons to toggle their mics and cameras on and off. You’ll use your knowledge of JSON and data channels to share mic and camera state with the other peer on a call.

To prepare the way for all of those tasks, let’s begin by taking a look at sending and receiving JSON as a way to enrich the chat messages you learned to send last chapter.
