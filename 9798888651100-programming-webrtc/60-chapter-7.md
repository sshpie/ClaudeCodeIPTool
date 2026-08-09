# Chapter 7  
Managing User Media

When it comes to requesting access to user media—cameras and mics—the code we’ve written so far has made some optimistic but naive assumptions: not only have we generally expected that users will grant our apps permission to access their media devices, but also that there will even be media devices available for users to grant access to in the first place.

Those assumptions suit us just fine in development. But the challenge in this chapter is to think about a wide range of far less ideal circumstances that any WebRTC app will face in the hands of real users. Much of your work along those lines will focus on the getUserMedia() method, which you haven’t really touched since [​*Adding Mic and Camera Toggles*​](f_0042.xhtml#sec.avtoggles). And even that was just to make a minor adjustment for requesting microphone access.

In this chapter, we’ll look at how getUserMedia() and related MediaDevices methods behave under different conditions, including:

- When media devices aren’t available, because there simply is no mic or camera attached—or because an overzealous system administrator has blocked access to them at the operating-system level
- When users deny access to media devices, either intentionally or accidentally, in the browser’s media-permissions dialog box that appears after getUserMedia() has been called

Working in such close proximity to the MediaDevices interface on the Media Capture and Streams API,[[83]](f_0063.xhtml#FOOTNOTE-83) you’ll discover subtle differences in error states and messages and media-permissions models in different browsers. Those differences include how and even whether permissions persist for users returning to a WebRTC app that they’ve used previously.

With logic in hand that addresses those types of conditions and browser differences, we’ll then turn our attention to optimizing the media tracks returning data from user cameras and mics. You’ll develop skills with specifying and applying media constraints objects. Those can be applied either to an initial call to getUserMedia(), or later, through the applyConstraints() method on a media track that’s already been returned from getUserMedia().

Adjusting Low-Level WebRTC ObjectsBeyond media constraints, it’s possible to reach down to lower-level APIs like the RTCRtpTransceiver,[[84]](f_0063.xhtml#FOOTNOTE-84) RTCRtpSender,[[85]](f_0063.xhtml#FOOTNOTE-85) and RTCRtpReceiver[[86]](f_0063.xhtml#FOOTNOTE-86) objects to do everything from try to force the use of a particular CODEC to scale video resolutions or bit rates up and down manually.

My advice is to avoid the temptation to do this. Your users’ browsers already have highly tuned, well tested algorithms to respond to shifting network conditions and overtaxed CPUs. Any custom logic of your own won’t be as good, and might well overlook certain conditions that will make for a degraded user experience with your apps.

The thing to remember throughout this chapter is that there’s only so much you, as a developer, can do about suboptimal media availability or permissions, let alone limited bandwidth and computing power. Whether a user is missing a media device, or either can’t or won’t let your app access it, the result is the same: there’ll be no video or audio (or both) streaming from that user. Your job is to develop an app that performs the best it can, given a wide and sometimes regrettable range of circumstances. But hey—that’s the case for all forms of web development, not just WebRTC.
