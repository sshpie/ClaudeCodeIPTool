# Chapter 3  
Establishing a Peer-to-Peer Connection

In the previous chapter, you constructed the basic interface for a video-call app. You also explored and wrote a number of placeholder callback functions to prepare the way for triggering and responding to the signaling channel’s events.

In this chapter, you’ll build on that work to enable two peers to set up a WebRTC connection and stream video directly to each other. At first, of course, the two peers will just be you and yourself with two different browser windows opened to the same namespace. To prevent skull-shattering feedback while you test things out, you’ll start off with the audio disabled.

The goal is to to work systematically and get some foundational WebRTC code working as quickly as possible, which you’ll further refine and make backward-compatible over the next few chapters. To get started, you’ll learn how to request access to a user’s camera and microphone. You’ll then dive in to do meaningful work with the core pieces of a peer-to-peer app, including media streams and the WebRTC RTCPeerConnection interface. You’ll also set up your peer-connection logic by writing a real-world implementation of the “perfect negotiation” pattern found in the WebRTC specification.
