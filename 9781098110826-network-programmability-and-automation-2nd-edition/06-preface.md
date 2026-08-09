# Preface

Welcome to *Network Programmability and Automation*!

The networking industry is changing dramatically. The drive for organizations and networking professionals to embrace the ideas and concepts of network programmability and automation is greater now than perhaps it has ever been, fueled by a revolution in new protocols, new technologies, new delivery models, and a need for businesses to be more agile and more flexible in order to compete. But what *is* network programmability and automation? Let’s start this book by answering that question.

# What This Book Covers

As its title indicates, this book is focused on network programmability and automation. At its core, network programmability and automation is about simplifying the tasks involved in configuring, managing, and operating network equipment, network topologies, network services, and network connectivity.

Many, many components are involved—including operating systems that are now seeing far broader use in networking than in the past, new methodologies like continuous integration, and tools that formerly might have fallen only in the realm of the system administrator (tools like source code control and configuration management systems). Because all of these play a part in the core definition of network programmability and automation, we cover all these topics. Our goal for this book is to enable you to establish a foundation of knowledge around network programmability and automation.

## What’s New in This Edition

This edition of the book has been updated from the original to include four totally new chapters:

- [Chapter 4, “Cloud”](ch04.html#cloud)
- [Chapter 5, “Network Developer Environments”](ch05.html#developmentenvironments)
- [Chapter 7, “Go”](ch07.html#go)
- [Chapter 14, “Network Automation Architecture”](ch14.html#architecture)

We’ve also updated the existing chapters to include newer concepts such as these:

- Google Protocol Buffers
- gRPC/gNMI
- Terraform
- Nornir

On top of all these new additions, we’ve refreshed and extended every chapter to reflect the advances and industry changes that have taken place since the first edition was published.

We’re thrilled to have the opportunity to add these new, exciting topics to the book. Because of size constraints, some content from the first edition was not carried over into this one. However, rather than simply removing this content, we’ve made it freely available at [*https://oreilly-npa-book.github.io*](https://oreilly-npa-book.github.io).

# How This Book Is Organized

This book isn’t necessarily intended to be read from start to end; instead, we’ve broken up the topics so that you can easily find the content that most interests you. You may find it useful to start out sequentially reading the first three chapters, as they provide background information and set the stage for the rest of the book. From there, you’re welcome to jump to whatever topics are most useful or interesting to you.

We’ve tried to keep the chapters relatively standalone, but—as with any technology—that’s not always possible. Wherever we can, we provide cross-references to help you find the information you need.

Here’s a quick look at how we’ve organized the topics:

Chapter 1, “Network Industry Trends”Provides an overview of the major events and trends that launched software-defined networking (SDN). As you’ll see, SDN was the genesis for an increased focus on network programmability and automation.

Chapter 2, “Network Automation”Takes the SDN discussion from [Chapter 1](ch01.html#trends) and focuses specifically on network automation—the history of network automation, types of automation, tools and technologies involved in automation, and how automation affects operational models (and how operational models affect automation).

Chapter 3, “Linux”Provides an overview of the Linux operating system. By no means a comprehensive discussion of Linux, this chapter aims to get networking professionals up to speed on Linux, basic Linux commands, and Linux networking concepts.

Chapter 4, “Cloud”Introduces cloud computing from a networking perspective, and provides a jumping-off point for many relevant topics like containers and Kubernetes networking. We also discuss how network engineers’ existing skills translate to a cloud-based environment.

Chapter 5, “Network Developer Environments”Explores the tools and techniques for maintaining a network developer environment. This is a crucial part of any network automation project, and it allows teams to collaborate on solutions more effectively, as well as efficiently move from development to testing, all the way to production.

Chapter 6, “Python”Introduces networking professionals to [Python](https://python.org). This programming language is frequently used in network programmability and automation contexts, and this chapter covers many of the basics of programming with Python: data types, conditionals, loops, working with files, functions, classes, and modules.

Chapter 7, “Go”Adds a second option to the network automation professional’s programming language repertoire, by exploring Go. Having recently grown in popularity—in large part because of the cloud native ecosystem—Go is a valuable asset even for those just starting on their automation journey.

Chapter 8, “Data Formats and Models”Digs into the formats and methods for transmitting, storing, and modeling network automation data. The ability to understand and work with data is a fundamental skill for any network automation professional, and in this chapter, we build a solid foundation for the chapters to follow.

Chapter 9, “Templates”Looks at the use of templating languages to create network device configurations. While the primary focus of this chapter is on the Jinja templating language, as it integrates natively with Python, we also explore Go templates and Extensible Stylesheet Language Transformations (XSLT).

Chapter 10, “Working with Network APIs”Covers the role of APIs in network programmability and automation. We explore key terms and technologies pertaining to APIs including HTTP, NETCONF, RESTCONF, and gNMI as examples to show how they can be used for network programmability and automation. We use both Python and Go libraries to automate network devices using these APIs.

Chapter 11, “Source Control with Git”Introduces [Git](https://git-scm.com), a popular and widely used tool for source code control. We talk about why source code control is important, how it is used in a network programmability and automation context, and how to work with popular online services such as [GitHub](https://github.com).

Chapter 12, “Automation Tools”Explores the use of open source automation tools such as [Ansible](https://www.ansible.com), [Nornir](https://oreil.ly/L7rFo) with [NAPALM](https://oreil.ly/MngGc), and [Terraform](https://www.terraform.io). You’ll learn how these tools can be used specifically for network programmability and automation, using the imperative and declarative approaches.

Chapter 13, “Continuous Integration”Examines continuous integration (CI) and the key tools and technologies that are involved. We discuss the use of test-driven development (TDD), explore tools and frameworks like GitLab and Jenkins, and take a look at a sample network automation workflow that incorporates all these CI elements.

Chapter 14, “Network Automation Architecture”Unifies all the concepts covered in prior chapters by proposing a reference architecture for a holistic network automation solution. Brings together automation and orchestration, explores the idea of a source of truth, and shows how user interactions might work in such a system.

# Who Should Read This Book

As we mentioned previously, the goal of this book is to equip you with foundational knowledge and a set of baseline skills in the areas of network programmability and automation. We believe that members of several IT disciplines will benefit from reading this book.

## Network Engineers

Given the focus on network programmability and automation, it’s natural that one audience for this book is the “traditional” network engineer, someone who is reasonably fluent in network protocols, configuring network devices, and operating and managing a network. You’ll learn how to use automation for configuration management, troubleshooting, observability, and more. This book will enable network engineers to be more efficient and to build more reliable infrastructure through automation and programmability.

### Prerequisites

Network engineers interested in learning more about network programmability and automation don’t need any previous knowledge in software development, programming, automation, or DevOps-related tools. The only prerequisite is an open mind and a willingness to learn about new technologies and how they will affect you—the networking professional—and the greater networking industry as a whole.

## Systems Administrators

Systems administrators, who are primarily responsible for managing the systems that connect to the network, may already have previous experience with some of the tools discussed in this book (notably, Linux, source code control, and configuration management systems). This book, then, could serve as a mechanism to help systems administrators expand their knowledge and understanding of such tools by presenting them in a different context (for example, using Ansible to configure a network switch as opposed to using Ansible to configure a server running a distribution of Linux).

### Prerequisites

This book *doesn’t* provide any coverage or explanation of core networking protocols or concepts. However, as a result of managing network-connected systems, we anticipate that many systems administrators also have a basic knowledge of core networking protocols. So most experienced systems administrators should be fine. If you’re a bit weak on your networking knowledge, we recommend supplementing this book with one that focuses on core networking concepts and ideas. For example, [*Packet Guide to Core Network Protocols*](https://learning.oreilly.com/library/view/packet-guide-to/9781449308094/) by Bruce Hartpence (O’Reilly) may be a good choice.

## Software Developers

Software developers may also benefit from reading this book. Many developers will have prior experience with some of the programming languages and developer tools we discuss (such as Python and/or Git). Like systems administrators, developers may find it useful to see developer tools and languages used in a networking-centric context (for example, seeing how Python could be used to retrieve and store networking-specific data).

### Prerequisites

We do assume that you have a basic understanding of core network protocols and concepts, and all the examples we provide are networking-centric examples. As with systems administrators, software developers who are new to networking will probably find it necessary to supplement the material in this book with a book that focuses on core networking concepts.

# Tools Used in This Book

As with any field of technology, the technologies and tools found in the network programmability and automation space have many versions and variations. Therefore, we standardized on a set of tools in this book that we feel best represents those you will find in the field. For example, Linux has many distributions, but we focus on only Debian, Ubuntu (which is itself a derivative of Debian), and CentOS (a derivative of Red Hat Enterprise Linux or RHEL). To help make it easy for you, we call out the specific version of the various tools in each tool’s specific chapter.

# Online Resources

We can’t possibly cover *all* the material we’d like to regarding network automation and network programmability. Therefore, throughout the book we reference additional online resources that you may find helpful in understanding the concepts and skills being presented.

# Conventions Used in This Book

The following typographical conventions are used in this book:

ItalicIndicates new terms, URLs, email addresses, filenames, and file extensions.

Constant widthUsed for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

Constant width boldShows commands or other text that should be typed literally by the user.

Constant width italicShows text that should be replaced with user-supplied values or by values determined by context.

###### Tip

This element signifies a tip or suggestion.

###### Note

This element signifies a general note.

###### Warning

This element indicates a warning or caution.

# Using Code Examples

Supplemental material (code examples, exercises, etc.) is available for download at [*https://github.com/oreilly-npa-book/examples/tree/v2*](https://github.com/oreilly-npa-book/examples/tree/v2).

If you have a technical question or a problem using the code examples, please send email to [*support@oreilly.com*](mailto:support@oreilly.com).

This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you’re reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing examples from O’Reilly books does require permission. Answering a question by citing this book and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product’s documentation does require permission.

We appreciate, but do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: “*Network Programmability and Automation*, 2nd Edition, by Matt Oswalt, Christian Adell, Scott S. Lowe, and Jason Edelman (O’Reilly). Copyright 2023 Matt Oswalt, Scott S. Lowe, and Christian Adell, 978-1-098-11083-3.”

If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at [*permissions@oreilly.com*](mailto:permissions@oreilly.com).

# O’Reilly Online Learning

###### Note

For more than 40 years, [*O’Reilly Media*](https://oreilly.com) has provided technology and business training, knowledge, and insight to help companies succeed.

Our unique network of experts and innovators share their knowledge and expertise through books, articles, and our online learning platform. O’Reilly’s online learning platform gives you on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video from O’Reilly and 200+ other publishers. For more information, visit [*https://oreilly.com*](https://oreilly.com).

# How to Contact Us

Please address comments and questions concerning this book to the publisher:

- O’Reilly Media, Inc.
- 1005 Gravenstein Highway North
- Sebastopol, CA 95472
- 800-889-8969 (in the United States or Canada)
- 707-829-7019 (international or local)
- 707-829-0104 (fax)
- [*support@oreilly.com*](mailto:support@oreilly.com)
- [*https://www.oreilly.com/about/contact.html*](https://www.oreilly.com/about/contact.html)

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at [*https://oreil.ly/NPA_2e*](https://oreil.ly/NPA_2e).

For news and information about our books and courses, visit [*https://oreilly.com*](https://oreilly.com).

Find us on LinkedIn: [*https://linkedin.com/company/oreilly-media*](https://linkedin.com/company/oreilly-media)

Follow us on Twitter: [*https://twitter.com/oreillymedia*](https://twitter.com/oreillymedia)

Watch us on YouTube: [*https://youtube.com/oreillymedia*](https://youtube.com/oreillymedia)

# Acknowledgments

This book would not have been possible without the help and support of a large community of people.

First, we’d like to extend our thanks to the vibrant network automation community. There are too many folks to name directly, but these are the people who have created open source projects like NAPALM, Netmiko, Nornir, and Containerlab, who have helped lead the charge in educating the industry about network automation, and who have tirelessly contributed their knowledge and experience for the benefit of others. Thank you all for your efforts and your contributions.

Our technical reviewers were critical in ensuring that the content is both technically accurate and easily consumable by readers. We’d like to extend our thanks to Patrick Ogenstad, Akhil Behl, Eric Chou, Sreenivas Makam, Michael Kehoe, and Arthur Chiao. Thanks for helping make sure this book is the best it could be!

Finally, our thanks would not be complete without including the staff of O’Reilly Media: our editors Simina Calin, Jennifer Pollock, and Melissa Potter; production editor Kristen Brown; copyeditor Sharon Wilkey; proofreader Stephanie English; and indexer Bill Morrison.
