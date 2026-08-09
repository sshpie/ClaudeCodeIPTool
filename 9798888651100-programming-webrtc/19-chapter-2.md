# Chapter 2  
Working with a Signaling Channel

In this chapter, you’re going to build the foundations of a video-calling app that will use WebRTC for connecting two peers who can stream video—and eventually also audio—to each other, in real time.

You’ll start by building an interface using semantic HTML and CSS, including a little flexbox for layout. Some of that work will strike you as being very precise and detailed. But the goal is to build a lean, accessible interface that also displays responsively across all types of devices. With the interface built, you’ll then do the necessary work to wire it up with JavaScript for handling routine events, like clicks, that happen in the browser. Those will eventually hook into the signaling channel and other WebRTC logic. So it’s necessary to build the interface first.

With the interface built, we’ll take a look at the peer-to-peer architecture of WebRTC and how it differs from the more familiar client-server web architecture of HTTP and HTTPS.

From there, we’ll take a sightseeing tour of a crucial piece of technology for establishing peer connections over WebRTC: a signaling channel, which will take the form of a small server that you’ve already downloaded with the book’s companion code. With a better understanding of the signaling channel in hand, you’ll then write some skeletal, foundational code for simultaneously connecting multiple pairs of peers over your app.
