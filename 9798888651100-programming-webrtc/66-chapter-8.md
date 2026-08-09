# Chapter 8  
Deploying WebRTC Apps to Production

Deploying a WebRTC application requires two infrastructural components:

1. As with any web application, you need server space behind a domain you control. That’s where you’ll host the application’s static files: HTML, CSS, and JavaScript. The server must also run whatever server-side scripts are powering your signaling channel.
2. You will also need a STUN server optionally paired with a TURN server for relaying peer media streams and data when a direct, peer-to-peer connection is not possible. You can configure your app to use a public STUN server, or you can run your own. You’ll learn how to do both in this chapter. You’ll also learn what the heck STUN and TURN even mean.

You can, of course, avoid much of the server setup outlined in this chapter and deploy your app to a cloud service capable of running your server-side scripts. The deployable app in this chapter, for example, uses Node.js. But because WebRTC needs only limited server-side capability to serve your app and power your signaling channel, you’ll likely find you can do much of the setup yourself. So we’ll keep things minimal and homespun in this chapter.

To make the advice here applicable to as many server setups as possible, this chapter assumes only that you’re running your own server, on some flavor of Linux where you have root or sudo privileges. The server-side commands and configuration examples here use a stock LTS Debian Linux, but there’s enough detail to help you locate documentation specific to whatever flavor of Linux you’re running: Ubuntu, Arch, and so on. We’ll take a very brief run through a checklist covering a few essential bits of preliminary server setup in [​*Preparing a World-Ready Server: A Checklist*​](f_0066.xhtml#sb.serverChecklist).

Prior to deployment, you’ll need to make a few adjustments to your WebRTC app. You’ll then need to somehow get the app’s files onto your server. Although you can use plain old FTP or SFTP, you’ll set up Git on your server and configure a post-receive Git hook that runs all the necessary tasks your app requires each time you deploy. And you’ll deploy by running the git push command on your development machine.

You’ll learn how to set up the Nginx web server (pronounced “engine ex”) to serve your apps files, with an HTTPS assist from Let’s Encrypt. Nginx shines at reverse proxying, which you’ll configure to pass incoming requests—both for files and signaling—to the server-side scripts that power your WebRTC app. Tying all the server-side setup together, you’ll install and set up pm2 so that you can start, monitor, and even automatically restart your WebRTC app on the server with each fresh deployment.

You’ll finish off your deployment work by installing and configuring Coturn to power your own personal STUN/TURN server.[[100]](f_0070.xhtml#FOOTNOTE-100) You’ll then update your app to use your Coturn installation, deploy with another git push to your server, and ensure that everything is working correctly.

So let’s get to it! We’ll take all of this in manageable steps, and test things out as we go. To kick things off, you’ll ready your WebRTC app for production. You’re welcome to use any of the apps you’ve built so far, or follow along with the demo app in the /deploy/ directory in the book’s companion source code.
