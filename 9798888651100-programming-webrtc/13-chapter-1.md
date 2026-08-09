# Chapter 1  
Preparing a WebRTC Development Environment

Exciting new technologies often require developers to level up the sophistication of their development environments. WebRTC is no exception. Almost everything you’ll be doing with WebRTC happens in and between browsers. While you’ll be writing HTML, CSS, and JavaScript just as you would for any other web application, there are some important things to set up to smooth your way through the rest of the book and your work building real-time web applications.

In this chapter, you’ll install Node.js if you haven’t already. You’ll also learn where to get yourself a copy of the code that accompanies this book, and you’ll take a brief tour of the code’s organization so you can find what you need, when you need it. You’ll then generate and make use of your own self-signed certificates for serving HTTPS in development. HTTPS is necessary to fully and reliably access many newfangled, highfalutin Web APIs—including WebRTC, even in development.

You’ll choose a WebRTC-ready development browser (spoiler: Chrome or Firefox), fire up the server that’s packed in with the book’s code to serve your in-progress work or the completed examples, and heroically machete your way through the dire security warnings that your browser will throw at you over your self-signed certificates.

It’ll be a little bit of work, but once you’ve set this all up for yourself, you shouldn’t have to think about any of it again.

All of the setup here should work without much fuss or drama on Unix-like operating systems, including macOS.

| Install Windows Subsystem for Linux |  |
| --- | --- |
| ![images/aside-icons/warning.png](/api/v2/epubs/urn:orm:book:9798888651100/files/images/aside-icons/warning.png) | If you’re developing on Windows, you’ll need to install and use Windows Subsystem for Linux.[[5]](f_0016.xhtml#FOOTNOTE-5) |
