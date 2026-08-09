# Chapter 8. Data Formats and Models

If you’ve done any amount of exploration into the world of APIs, you’ve likely heard about data formats like JSON, XML, or YAML. You may have heard about concepts like data modeling, or model-driven APIs. Terms like *data serialization* and *markup language* may have popped into the foreground. You’d be right to wonder what all of this means and how it all applies to network automation.

It turns out that these concepts are at the heart of any reasonably complex modern software system, including those built and operated for the purpose of network automation. Even if you’re writing a simple script to change the hostname on a switch, at some point, your script will need to transmit some kind of information over the network that the switch will successfully receive and correctly interpret. How can you get your script and that switch to speak the same language?

Data formats like the aforementioned are those shared languages. They are broadly supported in all popular programming languages and are under the covers of nearly all the libraries and tools that you’ll use in your network automation journey. They are used by your network device’s built-in software for the purpose of being able to reliably and programmatically communicate with external entities, whether a full-blown fabric manager or a simple script on your laptop.

Understanding these formats, and how to work with the data they represent, is therefore crucial for you to be able to work effectively as a network automation professional. This chapter covers a variety of technologies and tools used to represent, transmit, store, and model data formats, with a specific focus on those that you’re most likely to run into in your network automation work.

# Benefits and Fundamentals of Structured Data Formats

A programmer typically uses a wide variety of tools to store and work with data. You could use simple scalar values (single values), collections (arrays, hashmaps), or even custom types built in the syntax of the language you’re using. While the specifics often differ, all languages offer primitives like this to give the programmer multiple ways to solve problems. When passing data within the context of a single program, this is often sufficient. A compiler knows exactly how much memory to allocate for a given type, so all you have to do as the programmer is reference that type when you need it, and the compiler will handle everything.

However, sometimes a more abstract, portable format is required. For instance, a non-programmer may need to be able to feed data into, or retrieve data from, a running program. Multiple programs may need to communicate with one another somehow—and the programs may not even be written in the same language; this is often the case with traditional client-server applications using a script you’ve written to automate a task on a network device, for example.

The data formats discussed in this chapter were designed to enable these kinds of use cases. They are well-established standards for communicating between generic software systems, and as a result, they’re well supported in any language or tool you choose to use. They give you the ability to describe data that would otherwise be represented as a series of bytes in memory.

###### Note

Without standardization of data formats, our networks wouldn’t even function! Protocols like BGP, OSPF, and TCP/IP were standardized out of a necessity for network elements to have a predictable, shared language in order to effectively communicate across a globally distributed system—​the internet!

The formats discussed in this chapter have three key traits that make them extremely useful and preferable, especially within the context of network automation:

StructuredThese data formats, based on an agreed-upon set of rules, were designed to be easier for machines to understand. Computers are much more literal than humans and can’t intuitively understand data without a strict, predictable structure. For instance, the unstructured data you might see in the output of a `show` command on your router or switch may be formatted well for human consumption, but is not ideal for a computer to readily parse and understand.

SupportedSince these formats are standardized and widely adopted, you’ll almost never have to write your own code to understand them directly. You can reuse existing (and often extremely mature) software and tools for this. Many programming languages like Python and Go have built-in mechanisms that make it easy to import and export data to these formats, either on the filesystem or on the network.

PortableWhile some languages have their own intermediate representations (i.e., *pickle* in Python or *gobs* in Go), the formats we discuss here are language agnostic, meaning they work with a wide variety of software ecosystems.

These are all important to consider, but let’s ponder the first point a little longer through some examples. Why are structured data formats easier for computers to understand, as opposed to the output you might see as a result of a simple `show` command?

Whenever you run a command like this, the software on your network device first gathers any data it needs from its subsystems or other network devices. At this stage, the information is little more than bytes in memory. To meaningfully display the results, the software then represents that information in a format that a human being can easily and quickly understand:

```
root@vqfx1> show interfaces em0
Physical interface: em0    , Enabled, Physical link is Up
  Interface index: 8, SNMP ifIndex: 17
  Type: Ethernet, Link-level type: Ethernet, MTU: 1514, Speed: 1000mbps
  Device flags   : Present Running
  Interface flags: SNMP-Traps
  Link type      : Full-Duplex
  Current address: 52:54:00:b1:f5:8d, Hardware address: 52:54:00:b1:f5:8d
  Last flapped   : 2019-01-10 17:49:55 UTC (00:17:33 ago)
    Input packets : 1039
    Output packets: 778
```

The nice thing about output like this is that it requires little effort (or even expertise) to see that the name of this interface is `em0`. Our brains have the tools to flexibly identify data by using helpful phrases like `Physical interface`. Even if what we have in mind isn’t exactly this, we know that it will get us what we need.

However, it’s actually not obvious to a computer where the interface name is located in this output. To us, the term `Physical interface` is a useful indicator to describe the nature of the text that follows. To a computer, it’s all just undifferentiated text. If you were to write a program to pull out the bits of valuable data from this output, you’d have to answer some important questions:

- How do you know which portion of the text represents the value you want to access? Is it before or after the colon? What about commas? Why do some values share a line, whereas others get their own dedicated line?
- What happens if the output doesn’t follow a consistent set of formatting rules?
- What happens when another command (e.g., `show bgp neighbor`) formats things differently? Do you have to write a separate program or function for each command?
- Since the primary use case for this output is human readability, what happens when the network vendor hires a UX expert to review and make changes to the format of this output?

When writing your parsing program or function, you’ll have to answer these questions, and more often than not, that will require a lot of extra time and energy that you may not be able to afford. In contrast, structured formats like JSON and XML were built to handle these concerns well.

For example, some configuration models are friendly to automated methods, by representing the configuration model in these data formats like XML or JSON. It is easy in Junos OS to see the XML representation of the `show` command we ran earlier, as shown in [Example 8-1](#dataformats-show-output-xml).

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch08-dataformats*](https://github.com/oreilly-npa-book/examples/tree/v2/ch08-dataformats).

##### Example 8-1. Displaying the XML-RPC equivalent for Junos commands

```
root@vqfx1> show interfaces em0 | display xml
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/15.1X53/junos">
    <interface-information>
        <physical-interface>
            <name>em0</name>
            <admin-status junos:format="Enabled">up</admin-status>
            <oper-status>up</oper-status>
            <local-index>8</local-index>
            <snmp-index>17</snmp-index>
            <if-type>Ethernet</if-type>
            <link-level-type>Ethernet</link-level-type>
            <mtu>1514</mtu>
            <speed>1000mbps</speed>

 ... output truncated for brevity ...
```

Comparing this output to the preceding example, you might point out that this is quite a bit harder to read, and you’d be right. You’d even be right to argue that the latter is potentially a little less efficient; in some cases, more raw text would be needed to represent the same data.

From a programmatic perspective however, this is ideal. [Example 8-1](#dataformats-show-output-xml) provides key advantages over the previous, human-readable code when it comes to being able to programmatically parse the data contained within:

- XML follows a stable set of rules, so there’s no need to constantly rewrite low-level text-parsing logic. You need to care about only the data being represented.
- There is consistent use of delimiting structures. It’s clear that any tag starts with `<` and ends with `>`, and an opening tag should eventually be closed with a corresponding closing tag, such as `</tag>`.
- Each piece of data is given its own easily parsable field. You know that the space inside the tags represents the entirety of the actual value, and everything else is just structure.
- This format is inherently hierarchical. You know based on the order of opening and closing tags which values have parent/child relationships.
- There is an established convention for metadata—that is, data about data (e.g., the `xmlns` tag).

While some of the particulars here are specific to XML, all structured data formats provide the same advantages in their own way.

So, in short, structured data formats like those discussed here are designed to allow software systems to communicate reliably and predictably with one another, no matter what language they’re written in.

## When Structured Data Isn’t Available: Screen Scraping

When the first version of this book was written, numerous platforms offered only human-readable text as output to be consumed by automation tools and scripts, as opposed to structured formats like JSON or XML. In cases like these, *screen scraping* can be used to retrieve data from a network device. This technique uses a protocol like SSH to emulate user behavior by sending a series of terminal commands, retrieving the raw text output, and attempting to format this output into a more structured representation. Whether done using a language like Python, or other tools that may provide a slightly more abstract framework, this approach requires you to provide your own set of low-level rules for parsing raw text, or depend on those created/maintained by others. However, these days, platforms that require this approach are becoming more and more rare.

Screen scraping not only makes your automation software extremely fragile, but is also enormously wasteful to your time, and by extension, that of the organization you’re working in. The lesson to learn here isn’t that it is *impossible* to write a program to parse some kind of text blob that follows from a `show` command. Instead, remember that the unstructured output you see in your terminal—and the subsystems required to produce it—simply weren’t designed to be accessed programmatically. Even those who have successfully created screen-scraping scripts will tell you that this approach is fraught with danger. Some network platforms will literally crash if too many commands are sent at once—not exactly a solid foundation for automation.

In contrast, choosing an architecture that aligns best with your own use case means you can achieve a valuable outcome more quickly and avoid having to deal with problems that were solved decades ago. Your job as network automation professionals is to provide value to your organization as quickly and effectively as possible, and if you are able to choose an approach that doesn’t require you to constantly reinvent parsing logic, you should.

Platforms that don’t offer any form of support for structured data formats are being phased out, and any serious automation initiative should include a requirement for platforms that do support these options. This not only saves you the time from having to do screen scraping yourself, but also frees you from having to use tools built on this fragile foundation.

## Types of Data

As discussed in Chapters [6](ch06.html#python) and [7](ch07.html#go), you can use a variety of built-in data types in any modern programming language. We refer to these throughout the text, so if you’re not familiar with them, we recommend you start there. We might use terms like *string*, *integer*, and *boolean* for representing different types of scalar (singular) values, *list* or *array* to describe a collection of values, or *dictionary* for key-value pairs.

However, all of these may be known by slightly different names in the various data formats and programming languages we reference, and within those contexts we may use different terms. This is OK and expected; it’s more important that you understand the basic concepts behind all of these, rather than trying to be unified and precise in the terminology across the board.

## Documents Versus Data

You may have heard the term *markup language* within the context of some of these formats. This is an important term to understand because it is a big part of the history of some of the formats we discuss, and we should be clear about the primary reasons we’re even talking about these formats in the first place.

Markup languages can also be referred to as *document-oriented languages*. The canonical example for this is HTML, which includes tags for things like headers, images, and links to external dependencies like JavaScript and CSS files:

```
<html>
    <body>
        <div>
            <p>Hello, World!</p>
        </div>
    </body>
</html>
```

Markup languages like HTML are ultimately used to *describe/annotate a document*, which is then rendered together to form a web page that shows up in your browser.

However, this chapter is not focused on this use case. While some formats (in particular XML) can be used for this purpose, the data formats we’re looking at are designed for the task of *data serialization*—that is, representing data (not documents) in a structured way. Remember that the primary reason we’re looking at these formats is so that you can understand how software systems exchange data with one another.

So in short, you can think of markup languages as describing *documents* and data serialization formats as describing *data*. It is this second use case that we’re focusing on in this chapter.

## Categories of Data Formats

The data formats we explore in this chapter fall into two broad categories:

Text-basedData is first serialized into an intermediate format like UTF-8 and then encoded into bytes for storage or transmission.

BinaryData is encoded directly into an efficient, binary format.

We’ll start by looking at text-based data formats.

# Text-Based Data Formats

We’ve already teased a few text-based formats so far in this chapter, but now it’s time to look at them more closely. Text-based formats have some key advantages:

- You can easily edit them using a standard text editor or view them plainly using inspection tools in your browser.
- They are well-established standards, and it’s extremely easy to find support for them in libraries and tools.
- They’re abstract enough to map into just about any common data structure in a variety of programming languages.

###### Note

The main disadvantage to these formats is that they can be inefficient. One reason is because text-based formats include not only the raw data you want to transmit (strings, integers, arrays, key-value pairs) but also the various characters used to represent that data, such as curly braces and square brackets in JSON or `<>` tags in XML.

Text-based formats generally have to use more raw storage or bandwidth capacity to accommodate this extra information. These formats also require more processing to both send and receive data. This can become a problem when sending large amounts of data, as this inefficiency can compound. Fortunately, for the vast majority of network automation use cases and workflows, this is rarely a problem.

Whether at rest or in transit, any data you bring into an automation tool or script is ultimately represented as 0s and 1s: *bits*. Most of the time, you deal with these in multiples of 8: *bytes*. We loosely refer to this as *raw binary data*. However, before you can do something practical with this data, it needs to be processed and converted into a form you can work with. For example, computers don’t implicitly know that a series of bytes you’re receiving from an API request is ultimately meant to be interpreted as a Python list.

To get data from this raw binary format to something you can use (or vice versa), two distinct phases must take place:

1. Decoding and deserializing
2. Serializing and encoding

[Figure 8-1](#dataformats-decoding-text-formats) shows that to make sense of data using one of these formats—say, as a payload in an API response that you’re receiving—your computer must first decode the raw bits that come off the wire and into a text-encoding standard like UTF-8. This is the *decoding* step.

![npa2 0801](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0801.png)

###### Figure 8-1. Decoding and deserializing text-based data formats

However, at this point you effectively have the equivalent of one big string. A JSON payload, for example, might look something like [Example 8-2](#dataformats-decoded-json-payload).

##### Example 8-2. Decoded JSON string

```
"{\"vendors\":[\"Cisco\",\"Juniper\",\"Arista\"]}"
```

Data that’s been transmitted using these formats is most useful when it’s been *deserialized* into types and structures within the programming language or tool you’re using. For instance, this JSON document would map nicely into a Python dictionary, with a single key, `vendors`. This key’s value would map into a Python list for the three elements in the JSON array. Only after the data is decoded and then deserialized can you do something useful with the data contained within the response payload.

The same process must be followed in reverse to store or transmit data from these types. First, the data must be *serialized* into one of these formats and then *encoded* into bytes, as in [Figure 8-2](#dataformats-encoding-text-formats).

![npa2 0802](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0802.png)

###### Figure 8-2. Serializing and encoding of text-based data formats

This approach sacrifices a bit of efficiency for enhanced portability, and the potential for humans to more easily understand and even make changes to data found in one of these intermediate formats. Next, we’ll explore some of these specific formats in greater detail.

## YAML

If you’re reading this book because you’ve seen compelling examples of network automation online or in a presentation and you want to learn more, you may have heard of YAML. This is because YAML is a particularly human-friendly data format, and for this reason, it is used in many network automation tools and initiatives. For instance, YAML is used by Ansible to describe playbooks, variable files, inventory files, and more, as you’ll see in [Chapter 12](ch12.html#automationtools).

###### Note

Previously, we explored the difference between markup and data serialization formats, and you may be wondering which category best describes YAML. Fortunately, the website that hosts the YAML specification ([*https://www.yaml.org*](https://www.yaml.org)) explicitly states that *YAML* stands for *YAML Ain’t Markup Language* and that “YAML is a human-friendly data serialization language for all programming languages.” So, YAML is primarily intended as a data serialization language, with the added goal of being as human-friendly as possible.

If you compare YAML to the other data formats like XML or JSON, it seems to do much the same thing: it represents constructs like lists, key-value pairs, strings, and integers. However, as you’ll soon see, YAML does this is a uniquely human-readable way. YAML is very easy to read and write once you understand how its syntax maps to these basic data structures.

This is a big reason that many automation tools use YAML as a method of defining an automation workflow or providing a data set to work with (like a list of VLANs). YAML also has the added benefit of helping to enable IaC approaches, covered in [Chapter 13](ch13.html#cicd).

At the time of this writing, the latest YAML specification is YAML 1.2.2, published at [*https://www.yaml.org*](https://www.yaml.org). Also provided on that site is a list of software projects that implement YAML, typically for the purpose of being read into language-specific data structures and doing something with them. If you have a favorite language, it might be helpful to follow along with the YAML examples in this chapter and try to implement them using one of these libraries.

Let’s take a look at some examples. Let’s say you want to use YAML to represent a list of network vendors. If you paid attention in the preceding section, you’re probably thinking that you want to use a `string` to represent each vendor name—​and you’d be correct! This example is simple:

```
- Cisco
- Juniper
- Brocade
- VMware
```

This YAML document contains four items. You know that each item is a `string`. One of the nice features of YAML is that you usually don’t need quotes or double quotes to indicate a string; a string is usually automatically discovered by the YAML parser (e.g., PyYAML). Each of these items has a hyphen in front of it. Since all four of these strings are shown at the same level (no indentation), you can say that these strings compose a list with a length of 4.

YAML closely mimics the flexibility of Python’s type system. A good example of this flexibility is shown by mixing data types in a list:

```
- Core Switch
- 7700
- false
- ['switchport', 'mode', 'access']
```

This is another list, again with a length of 4. However, each item is a totally unique type. The first item, `Core Switch`, is a `string` type. The second, `7700`, is interpreted as an `integer`. The third is interpreted as a `boolean`. This interpretation is performed by a YAML interpreter, such as PyYAML. PyYAML, specifically, does a pretty good job of inferring the kind of data the user is trying to communicate.

The fourth item in this example is itself a list, containing three `string` items. This is an example of a nested data structure in YAML. You’ve also seen the various ways that some data can be represented. Our “outer” list is shown on separate lines, with each item prepended by a hyphen. The “inner” list is shown on one line, using brackets and commas. These are two ways of writing the same thing: a list.

###### Tip

Sometimes it’s possible to help the parser figure out the type of data you wish to communicate. For instance, if you want the second item to be recognized as a `string` instead of an `integer`, you can enclose it in quotes (`"7700"`). You also enclose data in quotes if a `string` contains a character that is part of the YAML syntax itself, such as a colon (:). Refer to the documentation for the specific YAML parser you’re using for more information.

Early on in this chapter, we briefly talked about key-value pairs (or dictionaries, as they’re called in Python). YAML supports this structure quite simply. Let’s see how you might represent a dictionary with four key-value pairs ([Example 8-3](#dataformats-example-yaml-dict-mixed)).

##### Example 8-3. YAML dictionary with mixed types

```
Juniper: Also a plant
Cisco: 6500
Brocade: True
VMware:
  - esxi
  - vcenter
  - nsx
```

Here, your keys are shown as `strings` to the left of the colon, and the corresponding values for those keys are shown to the right. If you want to look up one of these values in a Python dictionary, for instance, you reference the corresponding key for the value you are looking for.

Similar to lists, dictionaries are flexible with respect to the data types stored as values. In [Example 8-3](#dataformats-example-yaml-dict-mixed), you are storing a myriad of data types as the values for each key-value pair.

YAML dictionaries—​like lists—​can be written in multiple ways. From a data representation standpoint, the previous example is identical to this:

```
{Juniper: Also a plant, Cisco: 6500, Brocade: true,
VMware: ['esxi', 'vcenter', 'nsx']}
```

Most parsers will interpret these two YAML documents precisely the same, but the first is obviously far more readable. The latter is a good illustration of the close relationship between YAML and JSON, but from a practical perspective, you’ll rarely need to use the latter format. Again, the primary use case for YAML is to be human readable, so stick with the conventions that most closely align with this.

Finally, you can use a hash sign (`#`) to indicate a comment. This can be on its own line or after existing data:

```
- Cisco    # ocsiC
- Juniper  # repinuJ
- Brocade  # edacorB
- VMware   # erawMV
```

Anything after the hash sign is ignored by the YAML parser.

As you can see, YAML offers a friendly way for human beings to provide structured data to software systems. However, YAML is fairly new as far as data formats go. When it comes to data formats used for communication directly between software elements (i.e., no human interaction), other formats like XML and JSON are much more popular and have much more mature tooling that is conducive to that use case.

### Working with YAML in Python

Let’s narrow in on a single example to see exactly how a YAML interpreter will read in the data you’ve written in a YAML document. Let’s reuse one of the previous examples to illustrate the various ways to represent certain data types:

```
Juniper: Also a plant
Cisco: 6500
Brocade: true
VMware:
  - esxi
  - vcenter
  - nsx
```

Let’s say this YAML document is saved to your local filesystem as *example.yml*. Your objective is to use Python to read this YAML file, parse it, and represent the contained data as some kind of variable.

Fortunately, the combination of native Python syntax and the aforementioned third-party YAML parser, PyYAML, makes this easy:

```
import yaml
with open("example.yml") as f:
    result = yaml.load(f)
    print(result)
    type(result)

{'Brocade': True, 'Cisco': 6500, 'Juniper': 'Also a plant',
'VMware': ['esxi', 'vcenter', 'nsx']}
<type 'dict'>
```

###### Tip

The Python snippet in the preceding example uses the `yaml` module that is installed with the PyYAML Python package. This is easily installed using pip as discussed in [Chapter 6](ch06.html#python).

This example shows how easy it is to load a YAML file into a Python dictionary. First, a context manager is used to open the file for reading (a common method for reading any kind of text file in Python), and the `load()` function in the `yaml` module allows us to load this directly into a dictionary called `result`. The lines that follow this code show that this has been done successfully.

## XML

As mentioned in the previous section, while YAML is a suitable choice for human-to-machine interaction, other text-based formats like XML and JSON tend to be favored when software elements need to communicate with one another. This section covers Extensible Markup Language (XML), why it is suitable for this use case, and some of the ecosystem tools that exist for working with it.

The XML specification is defined and maintained by the World Wide Web Consortium, or [W3C](https://oreil.ly/47r0N). XML was derived from a similar but older format called Standard Generalized Markup Language (SGML). XML is considered a subset of SGML, and as a result, any existing SGML parsers should be able to parse XML.

XML was originally created in the late 1990s, when the World Wide Web was moving from static HTML pages to more dynamic content that required lightweight update mechanisms. During this time, the limitations of HTML on its own in this respect were becoming obvious. HTML was designed for the sole purpose of describing the format and structure of a web page, and as a result was quite static and not very extensible. XML was created so that arbitrary data—not just web-focused markup—could easily be transmitted over the network. Some of the earliest use cases for XML were applied toward creating a more dynamic web, but XML itself is a generic format for representing just about anything.

An early popular use case for XML was in the implementation of Asynchronous JavaScript and XML, or Ajax. This was one of the first web development techniques for making web content more dynamic. It accomplished this by having web applications send and receive data in the background, and use this data to dynamically refresh components within the application, without requiring a full page refresh. Another popular use case was SOAP, which was an RPC technique based on XML. At the time of this writing, both use cases have been supplanted by more modern, lightweight alternatives.

In the world of modern network automation, the most popular use case for XML is within the NETCONF protocol. In addition, while JSON is generally a more popular option, XML can be used as the data format for REST APIs as well. We talk about both of these in [Chapter 10](ch10.html#apis).

XML shares some similarities with YAML. For instance, it is inherently hierarchical. We can easily embed data within a parent construct, as shown in [Example 8-4](#dataformats-xml-basic-1).

##### Example 8-4. Basic XML document

```
<device>
  <vendor>Cisco</vendor>
  <model>Nexus 7700</model>
  <osver>NXOS 6.1</osver>
</device>
```

In this example, the `<device>` element is said to be the *root*. While spacing and indentation don’t matter for the validity of XML, you can easily see the root, as it is the first and outermost XML tag in the document. It is also the parent of the elements nested within it: `<vendor>`, `<model>`, and `<osver>`. These are referred to as the *children* of the `<device>` element, and they are considered siblings of one another. This structure is conducive to storing metadata about network devices, as you can see in this particular example. An XML document may contain multiple instances of the `<device>` tag (or multiple `<device>` elements), perhaps nested within a broader `<devices>` tag.

You’ll also notice that each child element contains data within. Whereas the root element contains XML children, these tags contain text data. Thinking back to the section on data types, it is likely these would be represented by `string` values in a Python program, for instance.

XML elements can also have attributes:

```
<device type="datacenter-switch" />
```

When a piece of information has associated metadata, it may not be appropriate to use a child element to describe that metadata, but rather an attribute. Of course, you can do both if needed. The key is to understand the difference between data and metadata (data about data) and use the appropriate tool to describe it.

An XML document can contain tags with just about any kind of name, depending on the use case. You could, therefore, encounter a naming conflict when creating tags for your own XML data structure. For instance, you might choose to use the tag `<device>` to describe one of those fancy new “smartphones”:

```
<device>Palm Pilot</device>
```

However, what if you also want to use the tag `<device>` to describe a ToR switch? Fortunately, the XML specification has implemented a namespace system, which helps disambiguate collisions like this. XML allows you to define these namespaces, and refer to them using the `xmlns` attribute ([Example 8-5](#dataformats-xml-namespaces)).

##### Example 8-5. XML namespaces

```
<root>
  <e:device xmlns:c="https://example.org/enduserdevices">Palm Pilot</e:device>
  <n:device xmlns:m="https://example.org/networkdevices">
    <n:vendor>Cisco</n:vendor>
    <n:model>Nexus 7700</n:model>
    <n:osver>NXOS 6.1</n:osver>XML Schema Definition
  </n:device>
</root>
```

The basic primitives of XML are quite simple. However, to do something meaningful with XML, you should look at the tools available for working with XML in a programming language like Python.

### Working with XML in Python

Python includes native support for searching and creating XML documents in its standard library, under the `xml` module. Popular third-party libraries, such as [lxml](https://lxml.de), offer a similar API but different underlying implementation. For the sake of simplicity, we stick with what’s available natively in Python for these examples.

XML is inherently hierarchical, which makes it a good fit for a tree structure. This is made a bit more apparent in [Figure 8-3](#dataformats-xml-tree-visualized), which provides a visual representation of the basic XML document in [Example 8-4](#dataformats-xml-basic-1).

![npa2 0803](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0803.png)

###### Figure 8-3. Visualization of an XML tree structure

Visualizations like these can be helpful when navigating XML documents by using a programming language like Python.

There are a few ways to search a tree for a particular piece of information, each with its own pros and cons. In this section, we stick with whatever’s most pragmatic and straightforward to understand for a given example.

###### Note

This section is an extremely condensed explanation of tree structures and how to iterate through them. Courses and other learning resources focused on data structures and algorithms will give you a deeper understanding of the various kinds of tree structures and what they’re used for.

The API for working with XML in Python is based on the concept of an element tree: literally, a tree of XML elements. This is in fairly stark contrast to the way you work with data from YAML or JSON, which maps directly into data structures like dictionaries and lists, which can be easier to understand at first glance. However, if you’re able to understand the very basics of tree structures, the ElementTree API should be fairly straightforward.

You can import the `ElementTree` class directly from the standard library. You’re also creating the simpler alias `ET` so you can easily refer to it in the following examples:

```
>>> import xml.etree.ElementTree as ET
```

There are a few ways to import an XML document, such as with `ET.parse()`, which loads from a file on the filesystem. However, you can also load XML from a string variable, which you might have if you’re looking at a response to an API request. In the next example, you’re declaring your own variable `data` and then using the `ET.fromstring()` method to read this string and create a new element tree from it:

```
data = """
<devices>
    <device name="sw01">
        <vendor>Cisco</vendor>
        <model>Nexus 7700</model>
        <osver>NXOS 6.1</osver>
    </device>
    <device name="sw02">
        <vendor>Arista</vendor>
        <model>Arista 7800</model>
        <osver>EOS 4.27</osver>
    </device>
    <device name="sw03">
        <vendor>Juniper</vendor>
        <model>QFX 10008</model>
        <osver>Junos 21.3</osver>
    </device>
</devices>
"""

tree = ET.fromstring(data)
```

You can simply print the value of your new `tree` variable to see what has been created for you:

```
>>> print(tree)
<Element 'devices' at 0x7f953cc8e1d0>
```

You’ll notice that the type for this variable is `Element`. This doesn’t fully represent the whole tree, but only the root element, which is the outermost tag in your XML document: `<devices>`. This element will have references to its children that you can access, and those will have their own children, and so on.

The main way to access the children for a given `Element` is through iteration. You can create a `for` loop to iterate over this element, and the items provided at each iteration will be one of that element’s children:

```
>>> for device in tree:
...     print(f"Device {device} found!")
...
Device <Element 'device' at 0x7f953cc3c590> found!
Device <Element 'device' at 0x7f953cbeb6d0> found!
Device <Element 'device' at 0x7f953cbeb860> found!
```

Of course, this doesn’t tell you much about each device, only that there are three of them. To access more information, you must go a bit deeper, since the elements like `model` and `vendor` are child elements of the `device` elements. You can use the `find()` method to search within the children of a given node and find the first one that matches a given tag:

```
>>> for device in tree:
...     model = device.find('model').text
...     print(f"Device model is {model}")
...
Device model is Nexus 7700
Device model is Arista 7800
Device model is QFX 10008
```

Since you were already iterating through the children of `tree` to get the `device` elements, the `find()` method can be used directly on a `device` element to search its children.

In some cases, especially when you have a deeply nested structure and are trying to get to a particular element, the `iter()` method can be useful. It allows you to iterate over all tree elements with a certain tag:

```
>>> for vendor in tree.iter('vendor'):
...     print(vendor.text)
...
Cisco
Arista
Juniper
```

This saves you from having to use things like nested `for` loops, or chained `find()` or `findall()` calls. In this case, you can just ask for all `vendor` elements in the entire tree and iterate over them.

As you might imagine, searching large trees can get a little complicated. Fortunately, Python includes limited support for XPath, an expression language that helps simplify searching through an XML document. You can provide a simple XPath expression as a parameter to the `findall()` method, which will then return all elements in the tree that match that expression:

```
>>> for model in tree.findall("./device/model"):
...     print(model.text)
Nexus 7700
Arista 7800
QFX 10008
```

You can also locate nodes based on a combination of their metadata attributes (e.g., the `name` attributes) as well as their element name. This is where things can get *really* powerful. Let’s say you want to look up the model for the device named `sw01`:

```
>>> tree.find("./device[@name='sw01']/model").text
'Nexus 7700'
```

You built on the previous expression by specifying the attribute and the desired value alongside `device` in the path. However, you are still able to get a handle on the `model` element, because of the remaining `/model` portion of the expression.

A lot more remains to dig into here, but a detailed explanation of XPath is a bit outside the scope of this section. That said, if you’re planning to work with XML frequently, especially large XML documents, XPath is an important tool to have in your toolbox. The official Python documentation on the `xml` module contains a lot of helpful examples.

###### Tip

Another tool for working with XML data is [XQuery](https://oreil.ly/gJX12). XQuery is a full-blown query language, similar to what SQL is for relational databases, whereas XPath is a way of providing simple expressions—typically, one-liners for locating data within an XML document. Because of their similarities, you may wonder whether you should learn both. XQuery is rarely needed in the context of network automation. Most of the time, a little bit of Python and XPath can get you just about anything you might need.

While XML is well represented throughout the history of network automation, you should be aware of at least one other text-based format, as we’ll explore next.

## JSON

JavaScript Object Notation (JSON) is the final text-based data format we’ll look at, and arguably the most widely used. XML has seniority, and YAML fills a need for a human-readable format, but when it comes to the format chosen for transporting structured data within networked applications, especially those that use HTTP, JSON is the undisputed champion. Many of the tools and libraries that communicate with network APIs, such as those in Chapters [10](ch10.html#apis) and [12](ch12.html#automationtools), use JSON to send/receive structured data over the network.

The origin story of JSON is similar to that of XML, albeit slightly more recent. It too was created as a lightweight mechanism for exchanging data over the web, to enable more dynamic content. It was based on a subset of the JavaScript programming language (thus the name), and the types used within the JSON specification closely reflect those within JavaScript. However, JSON is a language-independent format that’s well supported by a multitude of programming languages and automation tools. Languages like Go and Python have native JSON support in their standard libraries.

JSON has gone through a few iterations when it comes to standardization but remains largely consistent with the original ECMA-404 standard even to this day. The current version of the Internet Standard for JSON is described in [RFC 8259](https://oreil.ly/wlcYk). As you can see from this, JSON is a remarkably simple format; RFC 8259 is only 16 pages long!

JSON can also be used for configuration-related use cases. Node Package Manager (npm) uses JSON to describe the configuration of an npm package. Cloud providers like AWS and GCP use JSON files to configure a variety of their command-line utilities. JSON does have subjective advantages over YAML in this regard. Unlike YAML, JSON does not use indentation to indicate the scope of a given block of data, but rather the more explicit curly brace (`{}`) and square bracket (`[]`) syntax. This can make it easier to read and edit JSON documents for those unaccustomed to using indentation for scoping, as is done in programming languages like Python. However, this is almost entirely a matter of preference.

###### Note

JSON is widely considered a subset of YAML. In fact, many popular YAML parsers can also parse JSON data as if it were YAML (you may recall some of the “alternative” syntax we used in that section, which is remarkably similar to JSON). However, some of the details of this relationship are a bit more nuanced. See the [YAML specification](https://oreil.ly/RTKLL) for more information.

When compared directly against XML, it’s easy to see that JSON is more lightweight; it is generally able to describe the same underlying data with less overall text structure. Let’s say you want to represent a list of book authors in XML. You might do it like this:

```
<authors>
    <author>
        <firstName>Christian</firstName>
        <lastName>Adell</lastName>
    </author>
    <author>
        <firstName>Scott</firstName>
        <lastName>Lowe</lastName>
    </author>
    <author>
        <firstName>Matt</firstName>
        <lastName>Oswalt</lastName>
    </author>
</authors>
```

[Example 8-6](#dataformats-json-json-example) shows the equivalent data structure in JSON.

##### Example 8-6. Equivalent JSON

```
{
    "authors":[
        {
            "firstName": "Christian",
            "lastName": "Adell"
        },
        {
            "firstName": "Scott",
            "lastName": "Lowe"
        },
        {
            "firstName": "Matt",
            "lastName": "Oswalt"
        }
    ]
}
```

You can see that JSON is clearly a more lightweight way of representing data. This results in a more efficient way of transmitting the same underlying data. Especially in the early 2000s, this had a meaningful impact on web performance.

JSON has a fairly straightforward set of built-in types that are similar to those you might find in most programming languages, with some minor terminology differences. You’ll find they map to our YAML experience quite nicely:

NumberA signed decimal number.

StringA collection of characters, such as a word or a sentence.

Boolean`True` or `False`.

ArrayAn ordered list of values enclosed in square brackets, `[]`; items do not have to be the same type.

ObjectAn unordered collection of key-value pairs; keys must be `strings` (enclosed in curly braces, `{}`).

NullEmpty value. Uses the word `null`.

In [Example 8-6](#dataformats-json-json-example), you can see several of these types in use. You’ll notice that the whole document is wrapped in curly braces. This means that the outermost (or root) type is an object, which contains key-value pairs.

###### Note

A JSON document that uses an object as its root, or outermost, type isn’t uncommon, but also isn’t the only option. The outermost type could also be an array, containing elements of any type.

In this example, the object being described contains only a single key-value pair (note that the keys within a JSON object are always strings). The key is `authors`, and the value for that key is an array. This is also equivalent to the list format we discussed in YAML—an ordered list of zero or more values. This is indicated by the square brackets `[]`.

Contained within this list are three objects (separated by commas and a newline), each with two key-value pairs. The first pair describes the author’s first name (key of `firstName`) and the second, the author’s last name (key of `lastName`).

### Working with JSON in Python

JSON enjoys wide support across a myriad of languages. A JSON document can often be mapped directly into native data structures in languages like Python (dictionaries, lists) and Go (slices, maps, structs). We’ll now look more specifically at how to work with JSON in Python.

Our JSON data is stored in a simple text file:

```
{
  "hostname": "CORESW01",
  "vendor": "Cisco",
  "isAlive": true,
  "uptime": 123456,
  "users": {
    "admin": 15,
    "storage": 10,
  },
  "vlans": [
    {
      "vlan_name": "VLAN30",
      "vlan_id": 30
    },
    {
      "vlan_name": "VLAN20",
      "vlan_id": 20
    }
  ]
}
```

Python has tools for working with JSON built right into its standard library, aptly called the `json` package. In [Example 8-7](#dataformats-json-import-python), you can read this JSON file, convert it (load) into a Python dictionary, and print out some useful information about it (the inline comments can help explain each step in a bit more detail):

##### Example 8-7. Importing JSON to a Python dictionary

```
# Python contains very useful tools for working with JSON, and they're
# part of the standard library, meaning they're built into Python itself.
import json

# We can load our JSON file into a variable called "data"
with open("json-example.json") as f:
    data = f.read()

# Since our JSON document is an Object, json.loads() returns a dictionary.
# If our document was an Array, this would result in a list.
json_dict = json.loads(data)

# Printing information about the resulting Python data structure
print("The JSON document is loaded as type {0}\n".format(type(json_dict)))
print("Now printing each item in this document and the type it contains")
for k, v in json_dict.items():
    print(
        "-- The key {0} contains a {1} value.".format(str(k), str(type(v)))
    )
```

Those last few lines show exactly how Python views this data once it’s imported. The output that results from running this Python program is shown in [Example 8-8](#dataformats-json-import-python-results).

##### Example 8-8. Results of importing JSON to a Python dictionary

```
~ $ python json-example.py

The JSON document is loaded as type <type 'dict'>

Now printing each item in this document and the type it contains
-- The key uptime contains a <type 'int'> value.
-- The key isAlive contains a <type 'bool'> value.
-- The key users contains a <type 'dict'> value.
-- The key hostname contains a <type 'unicode'> value.
-- The key vendor contains a <type 'unicode'> value.
-- The key vlans contains a <type 'list'> value.
```

###### Note

You might be seeing the `unicode` data type for the first time. In Python, the `str` type is just a sequence of bytes, whereas `unicode` specifies an actual encoding. The reason you’re seeing it here is that the JSON specification requires text to be encoded in Unicode. So, if you’re new to text encoding, you can conceptually think of `unicode` as a specific type of string and useful for the same kind of things as the `str` (string) type, discussed in [Chapter 6](ch06.html#python).

Now that you’ve imported your JSON document into a native Python data structure, all the tools and techniques you learned in [Chapter 6](ch06.html#python) can be used to find whatever information you’re looking for.

You can also perform the reverse action—that is, taking a Python data structure and creating a JSON document from it. [Example 8-9](#dataformats-json-list-to-json-array) creates a Python list `vendors` and uses the method `json.dumps()` to create a JSON document containing an array.

##### Example 8-9. Dumping a Python list as a JSON array

```
>>> import json
>>> vendors = []
>>> vendors.append("Cisco")
>>> vendors.append("Arista")
>>> vendors.append("Juniper")
>>> print(json.dumps(vendors, indent=2))
[
  "Cisco",
  "Arista",
  "Juniper"
]
```

# Binary Data Formats

So far in this chapter, we’ve been discussing text-based data formats. These data formats leverage an intermediate representation for enhanced portability. The vast majority of languages and tools can easily understand formats like JSON. Therefore, when you’re sending data over the network, you can use this format and know that the other end can understand it, even if it’s written in another language, by another team, on another continent.

Hopefully, it has also been clear that while this intermediate step sacrifices a bit of efficiency to achieve this portability, the vast majority of use cases in network automation simply do not have the performance requirements for this inefficiency to become a problem. That said, in a few situations, the extra time and storage/bandwidth required to serialize and deserialize into these formats is considered prohibitively inefficient. For these, a more efficient type of format is called for: a *binary data format*. To understand this format, we first have to explore data types a bit more and how they actually work under the hood.

The type system in any statically typed programming language can usually be thought of as a set of aliases that the compiler uses to represent various lengths of bytes. For example, an `int` in Go, which defaults to a 32-bit integer, is just a way of allocating 4 bytes of memory. It follows, then, that if we were to define our own type composed of fields like these, that type would occupy as much memory as the sum of its constituent parts; see [Example 8-10](#dataformats-go-struct).

##### Example 8-10. A simple Go struct

```
type Coords struct {
    X int32
    Y int32
}
```

This type is another way of saying “a 64 bit chunk of memory.” The fields used within this type are a way of telling the compiler that the first 32 bits are used for one purpose and the second 32 bits for another.

As you might imagine, this mapping is language-specific. The way Go maps its own type system into memory is very different from the way Python, Rust, or C does it. However, applications written in these languages still need to communicate somehow. We’ve established that applications can serialize into one of the aforementioned text-based formats to solve this problem, but as we’ve also shown, this comes at a computational and storage cost that can be unacceptable for some use cases. This is where binary data formats come in.

The primary difference between binary data formats and the text-based formats you’ve seen thus far is that text-based formats require two separate steps to store or transmit information (encoding/decoding and serialization/deserialization), whereas binary data formats do it all in a single step. This is because applications using binary data formats do not have to first serialize data to an intermediate format like JSON or XML, but rather, they are able to read the raw bytes off of a network request or file on the filesystem, and map those bytes directly into a data structure, as shown in [Figure 8-4](#dataformats-decoding-encoding-binary-formats).

![npa2 0804](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0804.png)

###### Figure 8-4. Decoding/deserialization and serialization/encoding binary data formats

###### Note

Of course, even JSON messages must eventually be translated into binary in order to be transmitted or stored; everything your computer does is eventually a bunch of 0s and 1s, after all. However, because binary data formats do not require a text-based serialization step, they require much less work to get to that stage, and ultimately require a smaller number of bits in which to do it. You can think of binary data formats as being “closer” to that low-level representation.

For a more networking-centric example of binary data formats, you need look no further than your earliest Cisco Certified Network Associate (CCNA) or CompTIA Network+ studies. Packet headers are laid out as raw bits and bytes. You are taught to understand that bits 64–72 of an IPv4 packet are for that packet’s time to live (TTL), and that the source and destination address are both 32 bits long. You know this because you spend time understanding the concepts that each field represents, and then you understand how many bits are required to represent them. Most importantly, this layout of bits is standardized and must be strictly adhered to; otherwise, two network endpoints wouldn’t be able to communicate effectively.

The binary data formats we’re talking about here are really no different: they’re intended to represent a variety of data structures in such a way that it can be transmitted/stored and encoded/decoded as efficiently as possible. Imagine for a second if this wasn’t the case—that the IPv4 packet header was some agreed-upon JSON object that first needed to be deserialized before it could be read by your router. What a preposterously inefficient design that would be! Why, then, is such an idea so patently absurd, yet it’s totally acceptable to use formats like JSON for our automation-related APIs? Why wouldn’t we just use binary data formats everywhere? Well, the reality is that some APIs have gone in this direction. As we discuss in [Chapter 10](ch10.html#apis), binary data formats are quite popular in newer technologies like gRPC. However, JSON-based APIs are hardly going away. And don’t forget, text-based data formats still have their unique advantages: they’re more readable, easier to debug, and enjoy broader application support.

Application developers have a slew of considerations when deciding between binary data formats and text-based data formats. However, given that this book is focused specifically on network automation, we can boil this down a bit. The first thing you should know is that not many use cases really *require* the efficiencies gained by using binary data formats. Most of the time when you’re running network automation workflows, the *vast* majority of your computer’s time is spent idle. Typically, your script or tool will send a few API requests and wait for a response. Using text-based data formats for use cases like this is perfectly fine.

Binary data formats are preferred by a network automation professional for two main reasons:

Developer preferenceAs you’ve seen, all data formats come with their own set of tools and techniques for working with them. Developers become accustomed to using certain tools, and barring a compelling reason to do otherwise, sticking with what you know is sometimes useful. In some cases, this manifests in the form of a vendor building an API that uses only a certain format; if you’re writing a script to work with this API, you too will have to understand how to work with this format.

PerformanceThis is a nuanced point that shouldn’t be taken for granted. Again, most of what is done in network automation is trivial for a computer to handle, However, some use cases, such as streaming network telemetry, do benefit from these kinds of efficiencies. The key questions to ask here are, “How much information is being transmitted, and how often is it being transmitted?” One of the reasons streaming telemetry often uses binary data formats is that it’s sending *very* frequent updates, each of which could contain a significant amount of data.

###### Caution

Binary formats aren’t *always* faster or more efficient than text-based formats. A lot of nuance can be found in the implementations behind each technology, and in how well the data itself is laid out in each format. It’s totally possible that a text-based format could outperform a binary format. While the scales are definitely tipped in favor of binary formats when it comes to performance, this outcome is not guaranteed by any means.

Because most of the specific benefits and drawbacks of binary data formats tend to vary based on the format in question, it’s time to dive into some examples. We have quite a few options when it comes to binary data formats, and we’ll start with Protocol Buffers.

## Protocol Buffers

By far, the most likely binary data format you’ll run into in your network automation journey is that provided by [Protocol Buffers](https://protobuf.dev), also known as *protobuf*. As described on its website, protobuf was originally developed by Google for internal use, as a smaller and faster alternative to XML.

Since then, the specification and tooling for protobuf have become open source, so that anyone can use them. Previously, if you wanted to store or transmit information between applications, you had to either pick one of the well-known text-based formats like XML (which can be very slow when you’re operating at Google scale), or use a binary format specific to a programming language like Python or Go, which solves the performance problem to some extent but then locks you into that format’s language and ecosystem.

Protobuf, in contrast, is language agnostic, with nine languages supported by the latest version of the specification, and more being added all the time. This is the result of two important and distinct components:

- A schema definition language that allows you to specify services and messages in a way that’s not specific to any one application language (e.g., Python or Go)
- Tools for automatically generating source code in any of the supported languages based on these definitions

We’ll explore both of these aspects in the following sections.

### Protobuf definitions

Many text-based formats like JSON and XML are self-describing, in that they have formally defined textual conventions for indicating the type of data that they contain. Most binary data formats, on the other hand, are not self-describing. Because they’re just an opaque blob of bytes, you need some kind of external type definition so these bytes can be translated into types that both ends of a communication stream can make sense of.

Protobuf is no exception to this. To use protobuf to communicate, developers must first define their message format in the *protobuf interface definition language*, usually stored as *.proto* files. This language allows you to define the complex types that will eventually be serialized into binary data and transmitted to another application. Protobuf is a language-agnostic, human-editable way of representing otherwise opaque, binary data. It’s like a Rosetta Stone for binary data—and both sides of a protobuf-based communication channel must have the same copy of it in order to communicate.

A *type* in this language is referred to as a *message*. With this, you can define a custom type that you would like to be serialized via protobuf ([Example 8-11](#dataformats-protobuf-message)).

##### Example 8-11. A protobuf message

```
message Router {
    int32 id = 1;
    string hostname = 2;
}
```

Before we go much further, a closer examination of the protobuf message in [Example 8-11](#dataformats-protobuf-message) is warranted:

- `message Router` is a top-level declaration of the message named `Router`. You can use this message definition within other messages or as a parameter or return value for services, which we cover later.
- There are two *singular* fields: `id`, which is of type `int32`, and `hostname`, which is of type `string`.
- Each field has a number to the right that’s known as the *field identifier*. Since the order of serialized protobuf data is an implementation detail (and therefore can vary), this helps ensure that the raw binary is deserialized into the right fields.

At no point is the textual data in [Example 8-11](#dataformats-protobuf-message) transmitted on the wire (this is a key distinction between this and other text-based formats presented thus far, like XML or JSON). It is merely a human-editable specification that the protobuf tooling can read, and “compile” into a more efficient format. For the same reason you would define a class or a struct (as in [Example 8-10](#dataformats-go-struct)) so your program knows how to allocate and read a chunk of memory on your computer, you can define a protobuf message in a *.proto* file so that your software knows how make sense of the raw binary data you’re retrieving or sending.

Protobuf messages can also reference other messages when the built-in types like `int32` and `string` aren’t enough on their own. Let’s add a second message type called `Interface`, and then add a field to the `Router` message that uses it:

```
message Router {
    int32 id = 1;
    string hostname = 2;
    repeated Interface interfaces = 3;
}

message Interface {
    int32 id = 1;
    string description = 2;
}
```

The `repeated` keyword is the protobuf equivalent of a list or array. It indicates that the field `interfaces` is not just a single instance of the `Interface` message type, but multiple instances.

Protobuf also allows you to define a `Service`, which describes a set of RPC functions that can use either the built-in types, or the messages you’ve defined as parameters or return types:

```
service RouterService {
    rpc GetRouter(RouterRequest) returns (Router);
}
```

###### Tip

Service declarations can be used to define service endpoints for frameworks like gRPC and gNMI. For these, protobuf is one of the most popular data representation technologies, and [Chapter 10](ch10.html#apis) covers this in more detail.

This is an *extremely* light introduction to protobuf definitions. There are several more built-in types and important keywords to know if you want to write your own definitions or even read an existing definition. The Protocol Buffers [Language Guide](https://oreil.ly/Wnsdb) is a great next step if you want to dig in further.

### Protobuf tooling and code generation

The second important component that makes protobuf work is the tooling that can automatically generate code in the language of your choice, from these message and service definitions. This automatically generated code makes it much easier to send and receive binary-encoded protobuf data that follows those definitions in your applications.

You looked at individual pieces of our protobuf definition in the preceding section, and a full working example is shown in [Example 8-12](#dataformats-protobuf-full-definition).

##### Example 8-12. Full protobuf definition

```
syntax = "proto3";
package networkstuff;

service RouterService {
    rpc GetRouter(RouterRequest) returns (Router);
}

message RouterRequest {
    int32 id = 1;
}

message Router {
    int32 id = 1;
    string hostname = 2;
    repeated Interface interfaces = 3;
}

message Interface {
    int32 id = 1;
    string description = 2;
}
```

The number one tool you’ll want to familiarize yourself with, and make sure you have installed anywhere you want to write code that uses protobuf, is `protoc`. This is the *protobuf compiler*, and it allows you to go from the generic message definitions you’ve been working with thus far to “real” code that you can use in languages like Python or Go. Instructions for downloading and installing `protoc` can be found on the main [Protocol Buffers website](https://oreil.ly/ak-_A).

Once installed, `protoc` can be used to generate code for a variety of languages, even simultaneously. This can be executed on the bash command line. The following example instructs `protoc` to generate Go and Python code in the local directory, from the protobuf definition (as shown in [Example 8-12](#dataformats-protobuf-full-definition)) in the file *networkstuff.proto*:

```
protoc --go_out=. --python_out=. networkstuff.proto
```

This creates two files, one for Python (*networkstuff_pb2.py*), and one for Go (*networkstuff.pb.go*). These contain automatically generated type definitions and constructors for working with the language-specific implementation of the messages and services defined in our protobuf source file. You can then refer to these in your own code in order to use those types.

Let’s take a closer look at how to work with the generated Python code. You can open an interactive Python shell in the current directory and import the new module by name:

```
>>> import networkstuff_pb2
```

Within this module, each of your protobuf messages is given its own class, which you can instantiate:

```
>>> router = networkstuff_pb2.Router()
>>> router.id = 1337
>>> router.hostname = "r1"
```

It turns out the Python implementation is pretty smart. Normally, instances of Python classes permit the addition of attributes on the fly, but if you try to do that with your protobuf-generated class, you get an exception:

```
>>> router.foo = "bar"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed (no field "foobar" in message object).
```

This adds a little bit of safety against things like “fat fingering” attribute names. It’s still Python, so this check doesn’t happen until runtime (with languages like Go, this would be caught at compile time), but it’s better than nothing.

You can also use the `add()` method on the `router.interfaces` attribute to instantiate a new `Interface` object:

```
>>> if1 = router.interfaces.add()
>>> if1.id = 1
>>> if1.description = "outside interface"
>>> if2 = router.interfaces.add()
>>> if2.id = 2
>>> if2.description = "inside interface"
```

Now that you have instantiated your protobuf-defined `Router` object in Python and populated it with sample data, you can use the `SerializeToString()` method to see the byte-level representation of this instance, printed as a Python byte string:

```
>>> router.SerializeToString()
b'\x08\xb9\n\x12\x02r1\x1a\x15\x08\x01\x12\x11outside interface\x1a\x14...'
```

You can write this binary data to the filesystem:

```
>>> f = open('serialized.bin', 'w+b')
>>> f.write(router.SerializeToString())
>>> f.close()
```

Back at the bash shell, you can then use a tool like `hexdump` to inspect the raw bytes in the file:

```
~$ hexdump serialized.bin
0000000 b908 120a 7202 1a31 0815 1201 6f11 7475
0000010 6973 6564 6920 746e 7265 6166 6563 141a
0000020 0208 1012 6e69 6973 6564 6920 746e 7265
0000030 6166 6563
0000034
```

Finally, to go full circle with this example, you can use `protoc` to decode these raw bytes back into a readable format. This decoding requires the original *.proto* file, as well as the name of the message you intend to decode and, of course, the binary file itself (passed via `stdin`):

```
~$ protoc --decode networkstuff.Router networkstuff.proto < serialized.bin

id: 1337
hostname: "r1"
interfaces {
  id: 1
  description: "outside interface"
}
interfaces {
  id: 2
  description: "inside interface"
}
```

The latest protobuf specification supports a [canonical encoding in JSON](https://oreil.ly/3LmDI), which can be *really* useful for working with systems that require a more traditional format. This way, you can primarily define your message types in protobuf, and serialize to binary data when you can, but still have the option to generate JSON from a given message when needed.

The method for producing this will vary based on the language, but the protobuf Python library contains a package for working with JSON from protobuf types:

```
>>> from google.protobuf.json_format import MessageToJson
>>> print(MessageToJson(router))
{
  "id": 1337,
  "hostname": "r1",
  "interfaces": [
    {
      "id": 1,
      "description": "outside interface"
    },
    {
      "id": 2,
      "description": "inside interface"
    }
  ]
}
```

Truthfully, as a network automation professional, you’re unlikely to use protobuf to write serialized binary data to the filesystem. Things get *really* exciting when you are able to build on what we’ve only started to explore here and leverage protobuf in modern RPC frameworks like gRPC. Technologies like this will also leverage the code generated by `protoc` not only for the message definitions, but also to generate functions that represent the services we defined. It doesn’t matter if you have an API client written in Python and an API server written in Go (or many other combinations); as long as both sides are working from the same protobuf definitions, they can communicate. [Chapter 10](ch10.html#apis) covers this in much more detail.

Protobuf is a modern, lightweight binary data format that in the world of network automation has already been widely adopted. However, before we move on, we should touch on a few other binary data formats that you may come across.

## Other Binary Data Formats

Within the scope of network automation, protobuf is really the only binary data format you *need* to know about, since it is a key component in many modern network programmability options. However, a few other binary data formats are potentially relevant. It’s useful to be aware of some of these alternatives, so we’ll spend a few sentences discussing a few of them and their pros and cons:

Pickle[Pickle](https://oreil.ly/bb0p7) is a binary format for serializing Python objects. It is specific to Python and therefore will not work in other languages, but offers support for serializing just about any kind of object structure you have in your Python programs. It has advantages like built-in de-duplication (will not serialize the same object twice) and backward compatibility.

Gob[Gob](https://go.dev/blog/gob) is a binary format for serializing Go types. It aims to have the same speed advantages as Protocol Buffers, but presented in a way that’s much easier to use and doesn’t require a separate interface definition language, as you would have in *.proto* files. You need only define your types in code, and the `gobs` package will be able to determine how best to serialize those types by using reflection techniques.

BSON[BSON](https://bsonspec.org) is a “binary-encoded serialization of JSON-like documents.” It was originally invented as an internal representation of data for the MongoDB database. It’s more efficient than its textual counterpart JSON, but still somewhat less efficient than other binary formats, since it includes things like field names within the serialized data. It does include some additional types that are not supported in the JSON specification.

FlatBuffers[FlatBuffers](https://flatbuffers.dev) is similar to protobuf, including the fact that both were originally developed at Google. However, unlike protobuf, FlatBuffers allows you to directly access the serialized data in the form of a flat binary buffer, without having to unpack or deserialize it first. You can also deserialize a portion of the buffer, as opposed to having to deserialize the entire buffer all at once. This is highly desirable for extremely performance-sensitive applications, such as video games.

Apache Thrift[Apache Thrift](https://thrift.apache.org) is also similar to protobuf, in that it is a binary data format that includes an RPC framework, an interface definition language, and code generation tooling. However, while it was originally created at Facebook, it has since become an Apache project. Thrift and protobuf are typically seen as roughly equivalent in terms of performance (most comparisons have these two tied at first place). Thrift does offer a full RPC implementation, whereas protobuf generates only RPC stub functions that need to be implemented to be useful.

It’s useful to be aware of these other formats, and each has its own benefits and drawbacks. However, as a network automation professional, the choice of which binary data format to use will almost always be made for you. A network platform will typically determine one of these and provide either message definitions for you to create your own code or a prebuilt library that you can simply consume.

Next, we’ll cover data modeling, which allows us to place additional constraints on the data sent using one of these formats.

# Data Modeling

So far in this chapter, we’ve discussed a variety of data formats. Text-based formats like YAML, XML, and JSON are great for representing data in a human-readable and portable way. Binary data formats like protobuf are useful when performance is a bit more important. All these formats have basic type systems so your program is able to understand that a given series of characters or bytes is a string, integer, or boolean. At the end of the day, all these formats are aimed at representing data in a way that can be serialized and deserialized, to facilitate things like API-based communication.

However, sometimes we need more than just simple serialization. Let’s imagine that we are interacting with an API endpoint to update the hostname for a network device. The JSON payload for a request to this endpoint might look something like [Example 8-13](#dataformats-modeling-json-object).

##### Example 8-13. Example JSON payload

```
{
  "hostname": ""
}
```

This JSON object has a single key, `hostname`, whose value is also a string—presumably representing the new hostname we want to use for this device. However, while it is a valid string, it is also empty. From a JSON formatting perspective, this is a perfectly valid syntax; any mature JSON parser will have no problem deserializing this document.

However, if we were to send this payload to the API endpoint in question, it could still cause problems. These problems would have nothing to do with the validity of the JSON document itself, but rather the downstream effects of sending an empty string as a parameter to the hostname update functionality that this API endpoint represents. Now, of course, the API server could include a check to ensure that this field is not empty; this might take the form of a conditional, as in [Example 8-14](#dataformats-modeling-explicit-check).

##### Example 8-14. Explicit check for an empty string

```
req = json.loads(json_str)
if req["hostname"] == "":
    raise Exception("Hostname field must not be empty")
```

However, what about hostnames that are too long? What about special characters that might be supported in JSON but aren’t supported by the actual network device? By the way, all these considerations apply only to this one `hostname` field; what about even moderately more complex JSON payloads? We may have many more types in this payload to think about like integers, arrays, or nested objects, each with its own specific validity concerns. We might want to ensure that a given JSON array is not empty, or contains no more than five elements, or doesn’t contain any duplicates.

Writing server-side code to check for *all* these cases can quickly become unsustainable. Even if we could stay on top of all of them, such an approach would create an ugly experience for anyone writing code to consume such an API. If all these checks were built into the API server itself, clients would have great difficulty knowing how to send valid data to this API. The maintainers of the API would have to maintain detailed documentation about all of these checks and ensure that it was kept up-to-date manually (you can probably imagine how rarely this approach ends in success).

*Data modeling* is a set of tools and techniques for solving this problem. Whereas data formats allow you to serialize structured data generically, data modeling allows us to take this a step further and provide constraints that this structured data must adhere to. It gives us the opportunity to describe more specific rules and relationships that bring data into alignment with a specific use case or business process.

Typically, this is accomplished using some kind of data modeling language, which specializes in describing these constraints and relationships between data. These are often developed in conjunction with applications (i.e., an API server) designed to leverage that data model. Such an approach gives us key advantages and capabilities, especially within the network automation domain:

- Data models can often be language agnostic. Multiple applications can use the same model (e.g., a Python API client and a Go API server). In addition, you have only one place to see or update the data model.
- This approach focuses on the data, not the application. This makes it easier for nondevelopers (or developers who specialize in various languages) to understand the data model, without having to worry about language-specific syntax.
- Many data-modeling techniques provide a way to generate application code that enforces these constraints. This can be extremely useful for working with APIs; if you have the data model, you can automatically generate code to reliably produce a correct payload for an API call.

The canonical example of data modeling in practice is the *database schema*, which is used to describe the organization and structure of data within a database. These schemas allow you to describe tables of data, which include columns of a particular data type, but also allow you to specify relationships between data, and constraints like the uniqueness of a particular value. For example, in relational database systems the *primary key* is a special designation describing a column of values that can be used to uniquely identify the row to which those values belong. Primary keys often enforce such a uniqueness constraint; an attempt to insert a new row with a primary-key value that already exists for another row will be rejected.

###### Caution

It may seem like we’re straying into software developer territory here. While it’s true that some of these concepts may be more aligned with the day-to-day work of professional developers, it doesn’t mean you’ll never need to create your own data models (even simple ones), and it certainly doesn’t mean that understanding the concepts behind data modeling, the technologies involved, or an existing data model aren’t profoundly useful skills to have as a network automation professional.

That said, more goes into creating a solid data model than throwing a few fields together. It can often require a more in-depth understanding of relationships between data, cardinality, and data normalization (or in some cases, denormalization), which can be tough for even seasoned software developers to get right.

As a result, this section doesn’t cover every aspect of data modeling, for every possible use case. Rather, we give you just enough insight into the important concepts involved with data models, some of the specific tools and techniques for creating and evolving them, and the most likely ways you’ll need to use this knowledge in your work as a network automation engineer.

While we won’t be diving into database schemas in this chapter, the idea of a schema as applied to the data formats we’ve discussed thus far is very much applicable. In its most general definition, a *schema* is just a way to describe the structure of data. As a result, we use the terms *data model* and *schema* somewhat interchangeably in this section, since they’re both close enough approximations for accomplishing our goals.

Before getting started, here are a few key points to keep in mind as you read the remaining sections of this chapter:

- Data modeling involves the creation of a schema to which data must conform. This allows us to go beyond simple serialization and provide a more opinionated structure of the data that is relevant to our business logic or use case.
- Data-modeling languages and tools are not serialization formats. They are not used to carry information, but only to describe it. You won’t see any of these modeling technologies in a packet capture or browser network trace.
- Some data-modeling technologies are specific to a corresponding serialization format (e.g., JSON and XML), and others are a bit more broadly applicable.
- We don’t cover every data modeling tool in existence—only those that you’re most likely to run into in your network automation journey.

Within the context of network automation, you can consider data models as analogous to a grammar textbook. It doesn’t tell you the specific words to say to a friend during a conversation, only the rules you should follow to ensure that the two of you can have a conversation of any kind. When you speak, you don’t regurgitate the textbook itself; rather, you use your own words that follow the rules from that textbook. In the same way, data models provide the specific rules and constraints that a particular communication mechanism must follow. Given that both sides are following the same “grammar textbook,” they can communicate.

## YANG

Without a doubt, the data-modeling technology you’re most likely to run into during your network automation journey is YANG. Originally published as IETF [RFC 6020](https://oreil.ly/bYaZ4), YANG was created as a data-modeling language specific to the NETCONF protocol, which we cover in greater detail in [Chapter 10](ch10.html#apis). However, in the most recent version, which is defined in [RFC 7950](https://oreil.ly/nXq81), YANG has begun to decouple itself from NETCONF and XML so that other serialization formats like JSON, defined in [RFC 7951](https://oreil.ly/T3enl), can be used, as well as other APIs like RESTCONF (NETCONF over an HTTP transport). Regardless, the main purpose of YANG is to model configuration and operational state data such as that transmitted during NETCONF RPCs.

You may have heard that a given NOS or API is YANG-based, or model driven using YANG. This is a way of summarizing an architectural approach to building programmable network systems that places the data model at the center. This is usually a good thing; starting with the data model allows a vendor to automatically generate code from that model to implement API servers, clients, and internal systems. It’s a much less fragile, less burdensome approach than building API bindings by hand.

###### Caution

One unfortunate by-product of condensing the YANG approach into such simple terms is that it almost sounds like YANG is used as a serialization format for APIs like RESTCONF or NETCONF. This is a popular misconception about YANG. YANG is not a serialization format like JSON or XML, and you won’t see YANG syntax in a packet capture of an API request or response. In fact, APIs that leverage YANG for data modeling *usually* use XML as the serialization format when sending data between a server and a client. For this reason, many of the examples in this section use XML to show how data that is modeled in YANG can be serialized in an API request.

YANG enjoys broad adoption by many companies and organizations. Many network vendors use YANG to build their systems with a model-driven approach. End-user-led organizations like OpenConfig aim to create a common set of vendor-neutral data models. The IETF also has working groups for building its own set of vendor-neutral models.

Like other data-modeling technologies, YANG enables you to define the constraints of that data—such as those found in a network configuration or state table. You can specify, for instance, that VLAN IDs must be between 1 and 4094. You can enforce the operational state of an interface, in that it must be “up” or “down.” Through these models, the behavior of data within and between network systems can be defined.

Various types of YANG models exist. Some of these YANG models were created by end users; others were created by vendors or open working groups:

- Industry standard models include those from groups like the IETF and the OpenConfig Working Group. These models are vendor and platform neutral. Each model produced by an open standards group is meant to provide a base set of options for a given feature.
- Of course, vendor-specific models also exist. Almost every vendor has its own solution for multichassis link aggregation groups (MC-LAGs), for example, each with its own variances in configuration and state data. As a result, each vendor would need to build a data model specific to these implementations.
- Even within a single vendor, variances arise in the way a given feature is implemented across product platforms and would similarly require unique models.

As you may recall from earlier in this chapter, XML closely resembles a tree structure. Since YANG was originally intended to model data serialized in XML, it makes sense that the primitives it offers also follow this pattern. In fact, one of the core concepts in YANG is `leaf`, which allows you to define a singular piece of data that contains a single value and has no children. Note also the `type` statement, which allows you to specify that this element is a `string`, but other types are supported:

```
leaf hostname {
    type string;
    mandatory true;
    config true;
    description "Hostname for the network device";
}
```

This maps neatly to the XML document in [Example 8-15](#dataformats-yang-xml-equivalent).

##### Example 8-15. XML document satisfying the YANG model

```
<hostname>sw01</hostname>
```

This `leaf` statement is fairly flexible but still enforces some constraints on the data being described. For example, the `mandatory true;` statement means this field cannot be empty or blank. If you had omitted the `sw01` text from [Example 8-15](#dataformats-yang-xml-equivalent), it would not validate against your YANG data model.

You may also remember that XML can contain multiple instances of the same element. A good example of this in practice is the list of configured DNS servers on a device. The `leaf-list` statement allows you to model this kind of data:

```
leaf-list name-server {
    type string;
    ordered-by user;
    description "List of DNS servers to query";
}
```

The `ordered-by` statement controls whether the order of elements within this data structure should be respected and maintained, or whether the implementation of the system can order the elements in the way it sees fit. The latter can be useful for things like VLAN definitions, as the order in which VLANs are defined doesn’t really matter. However, for other things like DNS name servers or access-list entries, order is *extremely* important. As a result, the statement `ordered-by user;` is used.

Again, here’s an example of XML data that adheres to this model:

```
<name-server>1.1.1.1</name-server>
<name-server>8.8.8.8</name-server>
```

Until now, we’ve been looking only at elements that don’t include any nested data. In YANG parlance, these are leaves in the tree. However, as we’ve shown, a nested structure is usually a more practical way of representing data like this. For instance, a specific VLAN may have several fields to describe it: minimally, a VLAN ID and a human-readable name. These could be represented as children of a generic `vlan` element:

```
<vlan>
    <id>100</id>
    <name>web_vlan></name>
</vlan>
<vlan>
    <id>200</id>
    <name>app_vlan></name>
</vlan>
```

YANG provides another way of defining lists, but unlike the `leaf-list` statement, the `list` statement is used when the elements of that list are themselves parent elements—that is, they contain nested elements, as shown in [Example 8-16](#dataformats-yang-list).

##### Example 8-16. List statement in YANG

```
list vlan {
    key "id";
    unique "name";
    leaf id {
        type int16;
    }
    leaf name {
        type string;
    }
}
```

This is also where you get to see some useful constraints in action. This `key` statement indicates that the `id` field should be used as a unique identifier for elements in this list. This is roughly analogous to a primary key in database terms. The `unique` statement specifies that the `name` value within these list elements should also be unique. This is useful for values that may not be used as a key, but should still be unique; in this case, it’s useful to ensure that the VLAN names are not duplicated.

However, you’re missing an important constraint here. The type for the VLAN ID is `int16`—which is quite broad when you consider that VLAN IDs are only positive and can go up to only a value of 4094 (16-bit signed integers can represent values from −32,768 to 32,767). Unfortunately, an 8-bit integer would be too small for this purpose. So, what do you do?

You can define your own custom data type that helps enforce these kinds of constraints. Using the `typedef` statement, you can define a new type by name—say, `vlanid`:

```
typedef vlanid {
    type int16 {
      range "1 .. 4094";
    }
}
```

Within this block, you can specify that this new type definition inherits from the built-in type `int16`, but then also enforces a constraint that the value must be within the `range` 1 to 4094. As a result, any element that references this type must not only be a 16-bit integer, but also fit within this more specific range.

You can then amend the leaf node from [Example 8-16](#dataformats-yang-list) to use this new type definition:

```
list vlan {
    key "id";
    unique "name";
    leaf id {
        type vlanid;
    }
    leaf name {
        type string;
    }
}
```

Of course, seeing a series of `vlan` elements at the root of an XML document would be strange. It’s more likely that these would be nested within a parent element like `vlans`:

```
<vlans>
    <vlan>
        <id>100</id>
        <name>web_vlan></name>
    </vlan>
    <vlan>
        <id>200</id>
        <name>app_vlan></name>
    </vlan>
</vlans>
```

This can be specified in YANG by using the `container` statement:

```
    container vlans {
        list vlan {
            key "id";
            unique "name";
            leaf id {
                type vlanid;
            }
            leaf name {
                type string;
            }
        }
    }
```

This was just a taste of some of the more common primitives within YANG syntax. YANG has plenty of other terms and concepts that we don’t have time to get into. The YANG RFCs are surprisingly readable and quite thorough, so these can be a reliable reference if you want to dive deeper. Numerous online resources are also available for YANG fundamentals and practical applications.

Before we end this section, however, it’s useful to take a look at ways you can do something practical with a YANG model by using some of the tools in its ecosystem. One of the most popular of these is `pyang`, which is a Python-based library as well as command-line tool for working with YANG. With `pyang` and some plug-ins built for it, you can do things like validate that a given model is compliant with YANG RFCs, check whether a given XML document is valid against a given model, and even generate a Python class hierarchy from a model.

Once `pyang` is installed, you can use it from the bash command line to check that a given YANG model is valid:

```
~$ pyang config.yang
```

If any validation errors result from parsing this YANG model, this command would list them in the resulting output.

`pyang` also allows you to convert a YANG model to several supported output formats. One useful output is `tree`, which provides a nice tree-like map of the module and its statements and types:

```
~$ pyang config.yang -f tree
module: config
  +--rw hostname        string
  +--rw vlans
  |  +--rw vlan* [id]
  |     +--rw id      vlanid
  |     +--rw name?   string
  +--rw name-servers
     +--rw name-server*   string
```

Another useful output format is a sample XML skeleton:

```
~$ pyang config.yang -f sample-xml-skeleton
<?xml version='1.0' encoding='UTF-8'?>
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <hostname xmlns="https://example.org/config"/>
  <vlans xmlns="https://example.org/config">
    <vlan>
      <id/>
      <name/>
    </vlan>
  </vlans>
  <name-servers xmlns="https://example.org/config">
    <name-server>
      <!-- # entries: 0.. -->
    </name-server>
  </name-servers>
</data>
```

`pyangbind` is a plug-in for `pyang` that allows you to automatically generate a Python module from a YANG model. This can then be used to serialize out to XML, JSON, etc. You reference the plug-in directory where `pyangbind` can be located, and then refer to this location with the `--plugindir` flag. This makes a new output format available, `pybind`:

```
~$ PYANG_PLUGIN_DIR=$(pwd)/venv/lib/python3.8/site-packages/pyangbind/plugin
~$ pyang --plugindir $PYANG_PLUGIN_DIR -f pybind -o yangconfig.py config.yang
```

These commands generate a Python file, *yangconfig.py*, which you can then import from a Python prompt at the same location. Within this module is a class called `config`, which you can instantiate into `cfg`:

```
from yangconfig import config
cfg = config()
```

As of now, `cfg` is basically the Python equivalent of our YANG data model but is also empty. You can start populating it with information that is compliant with the model—for instance, a hostname:

```
cfg.hostname = "sw01"
```

Since the name servers are stored as a leaf list, these must be appended:

```
cfg.name_servers.name_server.append("1.1.1.1")
cfg.name_servers.name_server.append("8.8.8.8")
```

The VLANs are a bit more complicated, since these are modeled as a plain `leaf`. This means you need to `add()` a new VLAN by specifying its key as a parameter (this is the VLAN ID in our model). Then you can refer to it via that same key to set the other attributes, like `name`:

```
cfg.vlans.vlan.add(100)
cfg.vlans.vlan[100].name = "VLAN_100"
```

Note that you use a custom type to describe the VLAN ID, which specifies that it must be an integer between 1 and 4094. If you try to add a VLAN with an ID outside this range, an exception is raised:

```
>>> cfg.vlans.vlan.add(5000)

 (traceback omitted for brevity)

ValueError: 5000 does not match a restricted type
```

From here, you can serialize this into either XML or JSON. You can also use `pyangbind` to deserialize an existing XML or JSON document into this same class structure, and more. The `pyangbind` README file contains examples for these and other use cases.

As with most topics in this chapter, the preceding examples are really just a taste of what you can do with YANG. If you’re interested in providing a more structured, model-based approach to thinking about network data, you could do worse than to start off with YANG. However, you also should be aware of other modeling languages, which we’ll explore next.

## JSON Schema

JSON is an incredibly popular data format, especially in the frontend (web) developer world. As a result, it also enjoys a healthy ecosystem of tools and related specifications. *JSON Schema* is a data-modeling technology that allows you to easily document and validate JSON documents. If you know you want to use JSON as a data format, JSON Schema is a safe choice for creating a model or schema for validating the data you’re working with.

Like other data modeling technologies, JSON Schema includes a series of primitives and constraints for describing the layout of a set of data. As you might expect, its type system closely aligns with that of JSON itself; types like string, number, array, and object are all built right in. However, JSON Schema also provides a wide variety of other tools for describing the constraints within which those types should operate.

Let’s start with an example similar to the one you worked with for YANG, but instead of XML, you’ll use JSON; see [Example 8-17](#dataformats-jsonschema-list).

##### Example 8-17. JSON document to model

```
{
    "hostname": "sw01",
    "vlans": [
        {
            "id": 100,
            "name": "VLAN_100"
        },
        {
            "id": 200,
            "name": "VLAN_200"
        }
    ],
    "nameservers": [
        "1.1.1.1",
        "8.8.8.8"
    ]
}
```

This JSON document contains an object type, which includes three fields:

hostnameThis has a simple string value containing the device hostname.

nameserversAn array of strings containing our name servers.

vlansAn array of objects, which contain two fields, `id` and `name`. Each object represents a different VLAN.

As discussed in the previous section, you might want to make sure that the data shown in this example conforms to a few additional constraints beyond those imposed by the basic type system:

- The `vlans` and `nameservers` arrays must not be empty, and they must not contain duplicate entries.
- VLAN IDs must be between 1 and 4094.
- All three fields—`hostname`, `vlans`, and `nameservers`—must be present; they cannot be omitted from the document.

A JSON Schema document is actually written in JSON, using a set of predefined terms and fields. Creating a new JSON Schema document starts by defining the outer type. Since our configuration data is a JSON object, you can specify this by using the `type` property. You can also provide useful metadata like `title` and `description` for our schema. The `$schema` property specifies the version of JSON Schema you’re using. This allows tools that use this schema to know which rules to use when parsing this schema and validating data with it. [Example 8-18](#dataformats-jsonschema-example) shows a definition for a JSON schema.

##### Example 8-18. JSON Schema definition

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Config",
    "description": "A bit of configuration data for a network device",
    "type": "object",
    "properties": {
       ......omitted for brevity......
    },
    "required": ["hostname", "vlans", "nameservers"]
}
```

This definition includes two fields that you’ll see a lot more of in the following examples. The `required` key references keys within the JSON document that are mandatory; they should be present for a JSON document to be considered valid. The `properties` property allows you to specify further constraints that should be applied to these keys. Let’s now explore each property with specific examples (the following three examples are contained within `properties`).

The `hostname` key is fairly simple. You know it needs to be a string, but you also probably want to enforce a minimum and maximum length:

```
"hostname": {
    "type": "string",
    "minLength": 1,
    "maxLength": 20
}
```

The `nameservers` property is a bit more complex because it represents an array of values:

```
"nameservers": {
    "type": "array",
    "items": {
        "type": "string"
    },
    "minItems": 1,
    "uniqueItems": true
}
```

You need to not only specify the type `array` for this property but also use the `items` field to describe the type of the elements of that array—in this case, `string`. You can also specify that the array must have at least one item with the `minItems` field, and that the array shouldn’t contain duplicates by setting `uniqueItems` to `true`.

Finally, `vlans` is quite a bit more complicated since it is an array of objects:

```
"vlans": {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer",
                "minimum": 1,
                "maximum": 4094
            },
            "name": {
                "type": "string"
            }
        },
        "required": ["id", "name"]
    },
    "minItems": 1,
    "uniqueItems": true
},
```

Fortunately, this part of the JSON document mostly uses terms you’ve already seen. The type of `vlans` is `array`, but its elements are of type `object`. Therefore, you also need to use the `properties` field to describe the properties of each object in the array. This is where you can use the `required` field again to specify that `id` and `name` are mandatory keys in each element. You can specify that `id` must not only be an integer, but also be between 1 and 4094.

Altogether, our JSON schema looks like this:

```
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Config",
    "description": "A bit of configuration data for a network device",
    "type": "object",
    "properties": {
        "hostname": {
            "type": "string",
            "minLength": 1,
            "maxLength": 20
        },
        "vlans": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 4094
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "required": ["id", "name"]
            },
            "minItems": 1,
            "uniqueItems": true
        },
        "nameservers": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": true
        }
    },
    "required": ["hostname", "vlans", "nameservers"]
}
```

You can store this schema as a JSON file, just as you can store the JSON document described in [Example 8-18](#dataformats-jsonschema-example).

A plethora of tools exist for working with JSON Schema, in a variety of languages, for all kinds of use cases. One common use case is to simply validate that a JSON document adheres to a given schema. For instance, [jsonschema](https://oreil.ly/tsaCI) is a popular Python-based tool for doing this. You can write Python scripts to use this library to perform validation, or you can use the command-line tool that comes with it to validate documents right on the bash command line:

```
~$ jsonschema --instance data.json schema.json
```

If there’s no output, you have a valid JSON document. However, you can easily tweak your JSON document to include invalid data to ensure that you’ve written a well-thought-out schema. For instance, say your document includes an invalid VLAN ID:

```
~$ jsonschema --instance data.json schema.json
50000: 50000 is greater than the maximum of 4094
```

Or say you’ve omitted the `nameservers` property:

```
~$ jsonschema --instance data.json schema.json
{
    'hostname': 'sw01',
    'vlans': [
        {'id': 100, 'name': 'VLAN_100'},
        {'id': 200, 'name': 'VLAN_200'}
    ]
}: 'nameservers' is a required property
```

As you’ve seen, JSON Schema can be a powerful tool for validating JSON data, and is probably a good choice if you know you’ll be working with JSON as a data format.

###### Tip

Since YAML and JSON are close relatives, some tools allow you to seamlessly validate YAML data as if it were JSON. In addition, it’s usually possible to convert a YAML document to JSON so that existing JSON-only tools can be used.

Next, we’ll explore how to validate data formatted in XML.

## XML Schema Definition

XML also has its own dedicated modeling language, known as [*XML Schema Definition*, or *XSD*](https://oreil.ly/ziWqv). One popular use case for XSD (as with most modeling languages) is to generate source code data structures that match and enforce the schema described by that data model. You can then use that source code to automatically generate XML that is compliant with that schema, as opposed to writing out the XML by hand.

For a concrete example of how this is done in Python, let’s look once more at our XML example:

```
<device>
  <vendor>Cisco</vendor>
  <model>Nexus 7700</model>
  <osver>NXOS 6.1</osver>
</device>
```

Your goal is to print this XML to the console by using some automatically generated code. You can do this by first creating an XSD document, and then using a third-party tool to generate Python code from that document. Then, that code can be used to print the XML you need.

Let’s write an XSD schema file that describes the data you intend to write out:

```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/
XMLSchema">
  <xs:element name="device">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="vendor" type="xs:string"/>
      <xs:element name="model" type="xs:string"/>
      <xs:element name="osver" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
</xs:schema>
```

In this schema document, you are describing that each `<device>` element can have three children and that the data in each child element must be a `string`. Not shown here but supported in the XSD specification is the ability to specify that child elements are required; in other words, you could specify that a `<device>` element *must* have a `<vendor>` child element present.

You can use a tool called [PyXB](https://oreil.ly/ko-4l) at the bash command line to create a Python file that contains class object representations of this schema:

```
~$ pyxbgen -u schema.xsd -m schema
```

This creates *schema.py* in this directory. So, if you open a Python prompt at this point, you can import this schema file and work with it. In [Example 8-19](#dataformats-generate-object-from-xsd), you’re creating an instance of the generated object, setting some properties on it, and then serializing it into XML by using the `toxml()` function.

##### Example 8-19. Generating XML from an XSD schema in Python

```
>>> import schema
>>> dev = schema.device()
>>> dev.vendor = "Cisco"
>>> dev.model = "Nexus"
>>> dev.osver = "6.1"
>>> dev.toxml("utf-8")
'<?xml version="1.0" encoding="utf-8"?><device><vendor>Cisco</vendor><model>Nexus
</model><osver>6.1</osver></device>'
```

Next, we’ll explore how to validate data that uses protobuf.

## Modeling and Validating Protocol Buffers

Protocol Buffers don’t include any built-in data modeling or validation beyond their basic type system. If you want to do this, you need to look at third-party options. One popular choice is [`protoc-gen-validate`](https://oreil.ly/VyKz_), which is a plug-in to the protobuf compiler `protoc` that is maintained as part of the Envoy Proxy project.

This plug-in allows you to specify validation rules within the protobuf definitions we explored earlier. Let’s say you have a message `Vlan` with fields `id` and `name`:

```
message Vlan {
    int32 id = 1;
    string name = 2;
}
```

You can provide validation rules for this plug-in within brackets after the field number:

```
message Vlan {
    int32 id = 1 [(validate.rules).int32 = { gte: 1,  lte: 4094 }];
    string name = 2 [(validate.rules).message.required = true];
}
```

When compiled with this plug-in, the generated code will include validation methods on these types, such as `Vlan.Validate()`. This method can be used to determine whether a given class instance or struct adheres to the constraints described in these validation rules.

# Summary

Data formats and data models are at the core of everything we do in network automation. Whether we’re talking about configuration management, troubleshooting, or even just generating quick reports, a firm grasp on these fundamentals is essential to being successful on your automation journey. As you’ve seen, specific technologies come and go, but the need for structured data, and the ability to describe the layout of that data and the constraints to which it must adhere, will never change.

Here are some parting thoughts:

- Structured data is essential to a successful automation initiative. Unstructured data formats, while often ideal for humans to consume, are not designed to be easily parsed or understood by our automation systems and scripts.
- None of the languages or formats discussed in this chapter are perfect. They’re all designed with specific trade-offs in mind; your job is to identify which trade-offs align best with your situation.
- New data-modeling methods and languages are emerging all the time. For instance, [CUE](https://oreil.ly/GPwfB) has recently grown in popularity as a bit of a hybrid between a schema definition language and a templating system. Some technologies discussed in this chapter have also decreased in popularity over time. This is a natural and expected evolution; keep your head on a swivel and assess each new tool on its own merits and trade-offs and how they align with your goals.

In the next chapter, we’ll use data from formats like those we’ve discussed here to drive the automatic creation of consistent, templated configurations.
