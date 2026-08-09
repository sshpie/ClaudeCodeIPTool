# Introduction

![](/api/v2/epubs/urn:orm:book:9781098128876/files/image_fi/book_art/chapterart.png)

Our dependence on connected technology is growing faster than our ability to secure it. The same technologies we know to be vulnerable, exposed to accidents and adversaries in our computer systems and enterprises, are now driving us to work, delivering patient care, and monitoring our homes. How can we reconcile our trust in these devices with their inherent lack of trustworthiness?

Cybersecurity analyst Keren Elazari has said that hackers are “the immune system of the digital era.” We need technically minded individuals to identify, report, and protect society from the harms that the internet-connected world causes. This work has never been more important, yet too few people have the necessary mind-set, skills, and tools.

This book intends to strengthen society’s immune system to better protect us all.

## This Book’s Approach

The IoT hacking field has a large breadth, and this book takes a practical approach to the topic. We focus on concepts and techniques that will get you started quickly with testing actual IoT systems, protocols, and devices. We specifically chose to demonstrate tools and susceptible devices that are affordable and easy to obtain so you can practice on your own.

We also created custom code examples and proof-of-concept exploits that you can download from the book’s website at [https://nostarch.com/practical-iot-hacking/](https://nostarch.com/practical-iot-hacking/). Some exercises are accompanied by virtual machines to make setting up the targets straightforward. In some chapters, we reference popular open source examples that you can readily find online.

*Practical IoT Hacking* isn’t a guide to IoT hacking tools, nor does it cover every aspect of IoT security, because these topics would take an even bigger book to cover, one much too cumbersome to read. Instead, we explore the most basic hardware hacking techniques, including interfacing with UART, I2C, SPI, JTAG, and SWD. We analyze a variety of IoT network protocols, focusing on those that aren’t only important, but also haven’t been extensively covered in other publications. These include UPnP, WS-Discovery, mDNS, DNS-SD, RTSP/RTCP/RTP, LoRa/LoRaWAN, Wi-Fi and Wi-Fi Direct, RFID and NFC, BLE, MQTT, CDP, and DICOM. We also discuss real-world examples that we’ve encountered in past professional testing engagements.

## Who This Book Is For

No two people share identical backgrounds and experience. Yet analyzing IoT devices requires skills spanning nearly every domain of expertise, because these devices combine computing power and connectivity into every facet of our world. We can’t predict which parts of this book each person will find the most compelling. But we believe that making this knowledge available to a broad population gives them power to have greater control over their increasingly digitizing world.

We wrote the book for hackers (sometimes called security researchers), although we expect that it will be useful to others as well, such as the following individuals:

- A **security researcher** might use this book as a reference for experimenting with an IoT ecosystem’s unfamiliar protocols, data structures, components, and concepts.
- An **enterprise sysadmin** or network engineer might learn how to better protect their environment and their organization’s assets.
- A **product manager** for an IoT device might discover new requirements their customers will assume are already present and build them in, reducing cost and the time it takes the product to reach the market.
- A **security assessor** might discover a new set of skills to better serve their clients.
- A **curious student** might find knowledge that will catapult them into a rewarding career of protecting people.

This book was written assuming the reader already has some familiarity with Linux command line basics, TCP/IP networking concepts, and coding. Although not required to follow along in this book, you can also refer to supplementary hardware hacking material, such as the *The Hardware Hacking Handbook* by Colin O’Flynn and Jasper van Woudenberg (No Starch Press, forthcoming). We recommend additional books in certain chapters.

## Kali Linux

Most of the exercises in this book use Kali Linux, the most popular Linux distribution for penetration testing. Kali comes with a variety of command line tools, all of which we’ll explain in detail as we use them in the book. That said, if you don’t know your way around the operating system, we recommend reading *Linux Basics for Hackers* by OccupyTheWeb (No Starch Press, 2019) and exploring the material at [https://kali.org/](https://kali.org/), including its free course at [https://kali.training/](https://kali.training/).

To install Kali, follow the instructions at [https://www.kali.org/docs/installation/](https://www.kali.org/docs/installation/)*.* The version you use shouldn’t matter as long as it’s up to date, however, please keep in mind that we tested most of the exercises for rolling Kali versions between 2019 and 2020. You can try out older images of Kali at [http://old.kali.org/kali-images/](http://old.kali.org/kali-images/) if you have trouble installing any particular tool. Newer versions of Kali will by default not have all the tools installed, but you can add them through the `kali-linux-large` metapackage. Enter the following command in a terminal to install the metapackage:

```
$ sudo apt install kali-linux-large
```

We also recommend using Kali inside a virtual machine. Detailed instructions are on the Kali website, and various online resources describe how to do that using VMware, VirtualBox, or other virtualization technologies.

## How This Book Is Organized

The book has 15 chapters loosely split between five parts. For the most part, the chapters are independent from each other, but you might encounter references to tools or concepts in later chapters that we introduced in earlier ones. For that reason, although we wrote the book trying to keep most chapters self-contained, we recommend reading it in sequential order.

**Part I: The IoT Threat Landscape**

1. **Chapter 1: The IoT Security World** paves the way for the rest of the book by describing why IoT security is important and what makes IoT hacking special.
2. **Chapter 2: Threat Modeling** discusses how to apply threat modeling in IoT systems, as well as what common IoT threats you’ll find, by walking through an example threat model of a drug infusion pump and its components.
3. **Chapter 3: A Security Testing Methodology** lays out a robust framework for conducting holistic manual security assessments on all layers of IoT systems.

**Part II: Network Hacking**

1. **Chapter 4: Network Assessments** discusses how to perform VLAN hopping in IoT networks, identify IoT devices on the network, and attack MQTT authentication by creating a Ncrack module.
2. **Chapter 5: Analyzing Network Protocols** provides a methodology for working with unfamiliar network protocols and walks through the development process of a Wireshark dissector and Nmap Scripting Engine module for the DICOM protocol.
3. **Chapter 6: Exploiting Zero-Configuration Networking** explores network protocols used for automating the deployment and configuration of IoT systems, showcasing attacks against UPnP, mDNS, DNS-SD, and WS-Discovery.

**Part III: Hardware Hacking**

1. **Chapter 7: UART, JTAG, and SWD Exploitation** deals with the inner workings of UART and JTAG/SWD by explaining how to enumerate UART and JTAG pins and hacking an STM32F103 microcontroller using UART and SWD.
2. **Chapter 8: SPI and I2C** explores how to leverage the two bus protocols with various tools to attack embedded IoT devices.
3. **Chapter 9: Firmware Hacking** shows how to obtain, extract, and analyze backdoor firmware, and examine common vulnerabilities in the firmware update process.

**Part IV: Radio Hacking**

1. **Chapter 10: Short Range Radio: Abusing RFID** demonstrates a variety of attacks against RFID systems, such as how to read and clone access cards.
2. **Chapter 11: Bluetooth Low Energy** shows how to attack the Bluetooth Low Energy protocol by walking through simple exercises.
3. **Chapter 12: Medium Range Radio: Hacking Wi-Fi** discusses Wi-Fi association attacks against wireless clients, ways of abusing Wi-Fi Direct, and common Wi-Fi attacks against access points.
4. **Chapter 13: Long Range Radio: LPWAN** provides a basic introduction to the LoRa and LoRaWAN protocols by showing how to capture and decode these kinds of packets and discussing common attacks against them.

**Part V: Targeting the IoT Ecosystem**

1. **Chapter 14: Attacking Mobile Applications** reviews common threats, security issues, and techniques for testing mobile apps on Android and iOS platforms.
2. **Chapter 15: Hacking the Smart Home** animates many of the ideas covered throughout the book by describing techniques for circumventing smart door locks, jamming wireless alarm systems, and playing back IP camera feeds. The chapter culminates by walking through a real-world example of taking control of a smart treadmill.
3. **Tools for IoT Hacking** lists popular tools for practical IoT hacking, including those we discuss and others that, although not covered in the book, are still useful.

## Contact

We’re always interested in receiving feedback, and we’re willing to answer any questions you might have. You can use [errata@nostarch.com](http://mailto:errata@nostarch.com) to notify us about errors when you find them and [ithilgore@sock-raw.org](http://mailto:ithilgore@sock-raw.org) for general feedback.
