# Preface

The Web has grown up.

In the old days, we used to code design-rich websites using an endless mess of nested tables. Today we can use a standards-based approach with Cascading Style Sheets (CSS) to achieve designs not possible in the Web’s infancy. Just as CSS ushered in a new era of ability and readability to the design aspects of a site, WebSocket can do that for bidirectional communication with the backend.

WebSocket provides a standards-based approach to coding for full-duplex bidirectional communication that replaces the age-old hacks like Comet and long polling. Today we have the ability to create desktop-like applications in a browser without resorting to methods that exhaust server-side resources.

In this book, you’ll learn the simple ways to deliver on bidirectional communication between server and client, and do so without making the IT guy cry.

# Who Should Read This Book

This book is for programmers who want to create web applications that can communicate bidirectionally between server and client and who are looking to avoid using hacks that are prevalent on the Web today. The promise of WebSocket is a better way, based on standards and supported by all modern browsers, with sensible fallback options for those who need to support it. For those who haven’t considered WebSocket, put down the Comet tutorial you have been reading.

This book is appropriate for novices and experienced users. I assume that you have a programming background and are familiar with JavaScript. Experience with Node.js is helpful, but not required. This book will also benefit those who are charged with maintaining servers that run WebSocket code, and are responsible for ensuring the security of the infrastructure. You need to know the potential pitfalls of integrating WebSocket and what that means for you. The earlier chapters may be of less use to you, but the last three chapters will give you enough knowledge to know what is coming across your network.

# Goals of This Book

I’ve been in the trenches, and have had to implement acceptable hacks to achieve bidirectional communication for clients who needed the functionality. It is my hope that I can show you a better way, one that is based on standards and proves simple to implement. For several clients over the years, I have successfully deployed this book’s approach to communicating with the backend by using WebSocket rather than long polling and have achieved the goals I was after.

# Navigating This Book

I often read a book by skimming and pulling out the relevant pieces to use as a reference while coding. If you’re actually reading this preface, the following list will give you a rough idea of each chapters’ goals:

- Chapters [1](ch01.html#chapter_1) and [2](ch02.html#chapter_2) provide a quick-start guide with instructions on dependencies needed throughout the book, and introduces you to the JavaScript API.
- [Chapter 3](ch03.html#chapter_3) presents a full example with client and server code using chat.
- In [Chapter 4](ch04.html#chapter_4) you write your own implementation of a standard protocol and layer it on top of WebSocket.
- [Chapter 5](ch05.html#chapter_5) is essential for those who need to support older browsers.
- Finally, Chapters [6](ch06.html#chapter_6) through [8](ch08.html#chapter_8) dive into aspects of security, debugging, and an overview of the protocol.

# Conventions Used in This Book

The following typographical conventions are used in this book:

ItalicIndicates new terms, URLs, email addresses, filenames, and file extensions.

Constant widthUsed for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

Constant width boldShows commands or other text that should be typed literally by the user.

Constant width italicShows text that should be replaced with user-supplied values or by values determined by context.

###### Note

This element signifies a general note.

# Using Code Examples

Supplemental material (code examples, exercises, etc.) is available for download at [*https://github.com/kinabalu/websocketsbook*](https://github.com/kinabalu/websocketsbook).

This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you’re reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing a CD-ROM of examples from O’Reilly books does require permission. Answering a question by citing this book and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product’s documentation does require permission.

We appreciate, but do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: “*WebSocket* by Andrew Lombardi (O’Reilly). Copyright 2015 Mystic Coders, LLC, 978-1-4493-6927-9.”

If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at [*permissions@oreilly.com*](mailto:permissions@oreilly.com).

# Safari® Books Online

###### Note

[*Safari Books Online*](http://safaribooksonline.com) is an on-demand digital library that delivers expert [content](https://www.safaribooksonline.com/explore/) in both book and video form from the world’s leading authors in technology and business.

Technology professionals, software developers, web designers, and business and creative professionals use Safari Books Online as their primary resource for research, problem solving, learning, and certification training.

Safari Books Online offers a range of [plans and pricing](https://www.safaribooksonline.com/pricing/) for [enterprise](https://www.safaribooksonline.com/enterprise/), [government](https://www.safaribooksonline.com/government/), [education](https://www.safaribooksonline.com/academic-public-library/), and individuals.

Members have access to thousands of books, training videos, and prepublication manuscripts in one fully searchable database from publishers like O’Reilly Media, Prentice Hall Professional, Addison-Wesley Professional, Microsoft Press, Sams, Que, Peachpit Press, Focal Press, Cisco Press, John Wiley & Sons, Syngress, Morgan Kaufmann, IBM Redbooks, Packt, Adobe Press, FT Press, Apress, Manning, New Riders, McGraw-Hill, Jones & Bartlett, Course Technology, and hundreds [more](https://www.safaribooksonline.com/our-library/). For more information about Safari Books Online, please visit us [online](http://safaribooksonline.com).

# How to Contact Us

Please address comments and questions concerning this book to the publisher:

- O’Reilly Media, Inc.
- 1005 Gravenstein Highway North
- Sebastopol, CA 95472
- 800-998-9938 (in the United States or Canada)
- 707-829-0515 (international or local)
- 707-829-0104 (fax)

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at [*http://bit.ly/orm-websocket*](http://bit.ly/orm-websocket).

To comment or ask technical questions about this book, send email to [*bookquestions@oreilly.com*](mailto:bookquestions@oreilly.com).

For more information about our books, courses, conferences, and news, see our website at [*http://www.oreilly.com*](http://www.oreilly.com).

Find us on Facebook: [*http://facebook.com/oreilly*](http://facebook.com/oreilly)

Follow us on Twitter: [*http://twitter.com/oreillymedia*](http://twitter.com/oreillymedia)

Watch us on YouTube: [*http://www.youtube.com/oreillymedia*](http://www.youtube.com/oreillymedia)

# Acknowledgments

A lot of people made this book possible, including my wonderful and patient editor Brian MacDonald. To everyone at O’Reilly who helped make this book happen, a deep and profound thanks.

I would also like to thank my technical reviewers for their invaluable input and advice: Joe Ottinger and Arun Gupta. And thanks to those of you who sent in errata on the preview of the book so we could get them solved before going to production.

Thanks to Mom and Dad, for putting a computer in front of me and opening up an ever-expanding universe of creativity and wonder.
