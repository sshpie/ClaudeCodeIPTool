# Chapter 6  
Managing Multipeer Connections

If you’re like me and have a habit of opening way too many browser windows and tabs while you’re working, you might have encountered mysterious problems and errors at some point during your peer-to-peer WebRTC work. Perhaps you thought your app had stopped working, only to discover two browser windows connected on your app’s namespace already—before you accidentally connected a third.

But even if you’ve been more careful than that, let’s prove the connection limits on a peer-to-peer app. Fire up the starter app for this chapter—which contains peer-to-peer logic and the audio features you built in the last chapter—by running npm run start and pointing to the same namespace off of https://localhost:3000/multipeer/ in three browser windows. Join the call in the first two windows, and ensure that the peer-to-peer connection is successful:

![images/MultiPeer/two-way-okay.jpg](/api/v2/epubs/urn:orm:book:9798888651100/files/images/MultiPeer/two-way-okay.jpg)

Then let that evil, interloping third peer join.

What you’d hope would happen, of course, is that suddenly the call will show all three peers, in all three windows. Magic.

But what really happens is probably even worse than you could’ve imagined: not only can’t the third peer join the call (that truly would be magical, given the logic we’ve written so far), but the first two peers have their connection severed, and the consoles of all three browser windows fill up with new and exotic errors. What a mess. From two connected peers to no connected peers, thanks to an unwelcome, evil third peer’s attempt to connect:

![images/MultiPeer/three-way-not-okay.jpg](/api/v2/epubs/urn:orm:book:9798888651100/files/images/MultiPeer/three-way-not-okay.jpg)

However multipeer connections are created and maintained, hoping for code to suddenly turn magical ain’t it.
