# Chapter 6. Python

As a network engineer, there has never been a better time for you to learn to automate and write code. As we noted in [Chapter 1](ch01.html#trends), the network industry is fundamentally changing. It is a fact that networking had not changed much from the late 1990s to about 2010, both architecturally and operationally. In that span of time, network engineers undoubtedly typed in the same CLI commands hundreds, if not thousands, of times to configure and troubleshoot network devices. Why the madness?

It is specifically around the operations of a network that learning to read and write some code starts to make sense. In fact, scripting or writing a few lines of code to gather information on the network, or to make changes, isn’t new at all. It’s been done for years. Some engineers took on this feat—​programming in their language of choice, learning to work with raw text using complex parsing and regular expressions, and querying SNMP MIBs in a script. If you’ve ever attempted this yourself, you know firsthand that it’s possible, but working with regular expressions and parsing text is time-consuming and tedious.

Luckily, things are starting to move in the right direction, and the barrier to entry for network automation is more accessible than ever. We are seeing advances from network vendors, but also in the open source tooling available for automating the network, both of which we cover in this book. For example, there are now network device APIs, vendor- and community-supported Python libraries, and freely available open source tools that give you and every other network engineer access to a growing ecosystem to jump-start your network automation journey. This ultimately means that you have to write less code than you would have in the past, and less code means faster development and fewer bugs.

Before we dive into the basics of Python, we’ll consider one more important question because it always comes up in conversations among network engineers: *should network engineers learn to code?*

# Should Network Engineers Learn to Code?

Unfortunately, you aren’t getting a definitive *yes* or *no* from us. Clearly, we have a full chapter on Python and another on Go, and plenty of examples throughout the book on how to use Python or Go to communicate to network devices via network APIs and extend DevOps tools like Ansible and Terraform, so we definitely think learning the basics of any programming language is valuable. We also think it’ll become an even more valuable skill as the network and IT industries continue to transform at such a rapid pace, and we happen to think Python is a pretty great first choice.

###### Note

We consider Python a great first choice when it comes to network automation for several reasons. First, Python is a dynamically typed language that allows you to create and use Python objects (such as variables and functions) where and when needed, meaning they don’t need to be defined before you start using them. This simplifies getting started. Second, Python is also super readable. It’s common to see conditional statements like `if device in device_list:`, and in that statement, you can easily decipher that we are simply checking to see if a device is *in* a particular list of devices. Another reason is that network vendors and open source projects are building a great set of libraries and tools using Python. This just adds to the benefit of learning to program with Python.

The real question, though, is *should every network engineer know how to read and write a basic script*? The answer is a definite *yes*. Now *should every network engineer become a software developer*? Absolutely not. Many engineers will gravitate more toward one discipline than the next, and maybe some network engineers do transition to become developers, but all types of engineers, not just network engineers, *should not* fear trying to read through some Python or Ruby, or even more advanced languages like C, Go, or Rust. System administrators have done fairly well already with using scripting as a tool to allow them to do their jobs more efficiently by using bash scripts, Python, Ruby, and PowerShell.

On the other hand, this hasn’t been the case for network administrators (which is a major reason for this book!). As the industry progresses and engineers evolve, it’s realistic for you, as a network engineer, to be more *DevOps oriented*, in that you end up somewhere in the middle—​not as a developer, but also not as a traditional CLI-only network engineer. You could end up using open source configuration management and automation tools and then add a little code as necessary (and if needed) to accomplish and automate the workflows and tasks in your specific environment.

###### Warning

Unless your organization warrants it based on size, scale, compliance, or control, it’s not common or recommended to write custom software *for everything* and build a home-grown automation platform. It’s not an efficient use of time. We do recommend that you understand the components involved in programming, software development, and especially fundamentals such as core data types that are common to all tools and languages, as we cover in this chapter focused on Python.

So we know the industry is changing, devices have APIs, and it makes sense to start the journey to learn to write some code. This chapter provides you with the building blocks to go from 0 to 70 as you start your Python journey. Throughout the rest of this chapter, we start with the basics of Python (e.g., data types and flow logic), and then explore more advanced topics such as functions, classes, modules, and other patterns.

Get ready—​you are about to jump in and learn some Python!

###### Note

This chapter’s sole focus is to introduce foundational Python concepts to network engineers looking to learn Python to augment their existing skill sets. It is not intended to provide an exhaustive education for full-time developers to write production-quality Python software. A useful book to go deeper on Python is [*Fluent Python*](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/) by Luciano Ramalho (O’Reilly).

Additionally, the concepts covered in this chapter are heavily relevant outside the scope of Python. For example, you *must* understand concepts like loops and data types—which we explore here—to work with tools like Ansible, Nornir, and Terraform.

Finally, once you finish this chapter, you might realize that we didn’t explore many real-world network automation use cases. This is intentional; as with any programming language, sometimes entire books are often not enough to cover even the basics, and we aim to give a sufficient foundation for our purposes in a single chapter. So, in this chapter we focus solely on this foundation. [Chapter 10](ch10.html#apis) then revisits many of these concepts to tackle some real-world network automation tasks.

# Using the Python Interactive Interpreter

The *Python interactive interpreter* isn’t always known by those just starting out to learn to program or even those who have been developing in other languages, but it is a tool that everyone should know and learn before trying to create standalone executable scripts.

The interpreter is instrumental to developers of all experience levels. This tool, also commonly known as the Python *shell*, is used as a learning platform for beginners, but it’s also used by the most experienced developers to test and get real-time feedback without having to write a full program or script.

The Python shell, or interpreter, is found on nearly all native Linux distributions as well as many of the more modern network OSs from vendors including, but not limited to, Cisco, HPE, Juniper, Cumulus, and Arista. To access the Python interactive interpreter, you simply open a Linux terminal window, or SSH to a modern network device, type in the command `python3`, and hit Enter.

###### Note

All examples throughout this chapter that denote a Linux terminal command start with `$`. While you’re at the Python shell, all lines and commands start with `>>>`. Additionally, all the examples are from a system running Ubuntu 20.04 LTS and Python 3.8.12.

Since the first version of this book was published, Python 2.7 has reached End of Life. As a result, this chapter now exclusively uses Python 3 syntax and libraries.

For an explicit usage of Python 3 across the book, we use `python3` to run Python scripts and launch the interactive interpreter, disambiguating with the `python` alias, which could still be pointing to Python 2.

After entering the `python3` command and hitting Enter, you are taken directly into the shell. While in the shell, you start writing Python code immediately! There is no text editor, no IDE, and no prerequisites to getting started:

```
$ python3
Python 3.8.12 (default, Feb 26 2022, 00:05:23)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Although we jump into much more detail on Python throughout this chapter, we’ll take a quick look at a few examples right now to see the power of the Python interpreter. Let’s start by simply creating a variable called `hostname` and assigning it the value of `ROUTER_1`:

```
>>> hostname = 'ROUTER_1'
```

Notice that you do not need to declare the variable first or define that `hostname` is going to be of type `string`. This is a departure from some programming languages such as C and Java, and a reason Python is called a dynamic language.

Now, you can print the variable `hostname`:

```
>>> print(hostname)
ROUTER_1
>>>
>>> hostname
'ROUTER_1'
```

Once you’ve created the variable, you can easily print it using the `print` command, but while in the shell, you can also display the value of `hostname` or any variable by just typing in the name of the variable and pressing Enter. One difference between these two methods is that when you use the `print` statement, characters such as the end of line, or EOL (`\n`), are interpreted, but are not when you’re not using the `print` statement.

For example, using `print` interprets the `\n` and a new line is printed, but when you’re just typing the variable name into the shell and hitting Enter, the `\n` is not interpreted and is just displayed to the terminal:

```
>>> banner = "\n  WELCOME TO ROUTER_1  \n"
>>>
>>> print(banner)

  WELCOME TO ROUTER_1

>>>
>>> banner
'\n  WELCOME TO ROUTER_1  \n'
```

Can you see the difference?

When you are validating or testing, the Python shell is a great tool to use. In the preceding examples, you may have noticed that single quotes and double quotes are both used. Now you may be thinking, could they be used together on the same line? Let’s not speculate about it; let’s use the Python shell to test it out:

```
>>> hostname = 'ROUTER_1"
  File "<stdin>", line 1
    hostname = 'ROUTER_1"
                        ^
SyntaxError: EOL while scanning string literal
```

And just like that, you verify that Python supports both single and double quotes, and learn that they cannot be used together.

Most examples throughout this chapter continue to use the Python interpreter—​feel free to follow along and test them out as they’re covered. We’ll continue to use the Python interpreter as we review Python data types, with a specific focus on networking.

# Understanding Python Data Types

This section provides an overview of various Python data types, including strings, numbers (integers and floats), booleans, lists, and dictionaries. This section also touches upon tuples and sets.

The content on strings, lists, and dictionaries is broken into two parts. The first is an introduction to the data type and the second covers some of its built-in methods. As you’ll see, *methods* are natively part of Python, making it extremely easy for developers to manipulate and work with each respective data type.

For example, a method called `upper` that takes a string and converts it to all uppercase letters can be executed with the statement, `"router1".upper()`, which returns `ROUTER1`. We show many more examples of using methods throughout this chapter.

The sections on integers and booleans provide an overview to show you how to use mathematical operators and boolean expressions while writing code in Python.

Finally, we close the section on data types by providing a brief introduction to tuples and sets. They are more advanced data types, but we feel they were still worth covering in an introduction to Python.

[Table 6-1](#table-python-data-types) describes and highlights each data type covered in this chapter. You can use this as a reference throughout the chapter.

| Data type | Description | Short name (type) | Characters | Example |
| --- | --- | --- | --- | --- |
| **String** | Series of any characters surrounded by quotes. | `str` | `""` | `hostname="nycr01"` |
| **Integer** | Whole numbers represented without quotes. | `int` | n/a | `eos_qty=5` |
| **Float** | Floating-point number (decimals). | `float` | n/a | `cpu_util=52.33` |
| **Boolean** | Either `True` or `False` (no quotes). | `bool` | n/a | `is_switchport=True` |
| **List** | Ordered sequence of values. Values can be any data type. | `list` | `[]` | `vendors=['cisco', 'juniper', 'arista', ​'cisco']` |
| **Dictionary** | Ordered collection of key-value pairs. | `dict` | `{}` | `facts={"vendor":"cisco", "platform":"catalyst", ​"os":"ios"}` |
| **Set** | Unordered collection of unique elements. | `set` | `set()` | `set(vendors) returns {'arista', 'cisco', ​'juniper'}` |
| **Tuple** | Ordered and unchangeable sequence of values. | `tuple` | `()` | `ipaddr=('10.1.1.1', 24)` |

Let’s get started and take a look at Python strings.

## Strings

*Strings*—a sequence of characters enclosed by quotes—are arguably the most well-known data type in all programming languages.

###### Warning

Although strings look like a simple data type, they are slightly more complex. A string can represent two kinds of data: *text* and *bytes*. In Python 2, both types were represented as a `str`, but in Python 3, each is a separate and incompatible type.

You can [go deeper on the differences](https://oreil.ly/RuNfW), but in short, in Python 2 strings are ASCII characters and in Python 3 strings are Unicode characters (by default UTF-8), so if you receive *bytes* you will need to *encode* them to use string methods, using one of the available encode types, such as UTF-8, UTF-16, ASCII, or others.

Earlier in the chapter, we presented a few basic examples for creating variables that were of type `str`. Let’s examine what else you need to know when starting to use strings.

First, you’ll define two new variables that are both strings, `final` and `ipaddr`:

```
>>> final = 'The IP address of router1 is: '
>>>
>>> ipaddr = '192.0.2.1'
```

###### Tip

You can use the built-in function called `type` to verify the data type of any given object in Python:

```
>>> type(final)
<class 'str'>
```

This is how you can easily check the type of one object, which is often helpful in troubleshooting code, especially if it’s code you didn’t write.

Next, let’s look at how to combine, add, or *concatenate* strings:

```
>>> final + ipaddr
'The IP address of router1 is: 192.0.2.1'
```

So far, you’ve created two new variables: `final` and `ipaddr`. Each is a string. After both are created, you *concatenate* them using the `+` operator, and finally print them out. Fairly easy, right?

The same could be done even if `final` is not a predefined object:

```
>>> print('The IP address of router1 is: ' + ipaddr)
The IP address of router1 is: 192.0.2.1
```

### Using built-in methods of strings

To view the available built-in methods for strings, you use the built-in `dir()` function while in the Python shell. You first create any variable that is a string or use the formal data type name of `str` and pass it as an argument to `dir()` to view the available methods. You can always find more detailed information in the [Python official docs](https://oreil.ly/ICC4d).

###### Tip

`dir()` can be used on any Python object, not just strings, as we show throughout this chapter.

```
>>> dir(str)
# output has been omitted
['__add__', '__class__', '__contains__', '__delattr__', '__doc__',
'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha',
'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'lower',
'lstrip', 'replace', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'upper']
```

###### Note

To keep the output clean and simplify examples throughout the chapter, we add an *omitted* comment in some outputs. In this example, we’ve removed some objects that start and end with double underscores (`__`), also known as *dunders*. These internal methods are used to implement some *magic* operations without explicitly calling them.

For instance, as you will see in [“Understanding Python Classes”](#python-classes), when an object is created from a class, there is an implicit call to the `__init__()` method (the *constructor*) and it returns an object. By overwriting this dunder, you can customize how your objects will be created.

To reiterate what we said earlier, it’s possible to also pass any string to the `dir()` function to produce the same output as previously. For example, if you define a variable such as `hostname = 'ROUTER'`, `hostname` can be passed to `dir()`—that is, `dir(hostname)`—producing the same output as `dir(str)` to determine what methods are available for strings.

# Navigate the Code with type(), dir(), and help()

To learn how to use a given method that you see in the output of `dir()`, you can use the built-in function `help()`. To use this built-in help feature, you pass in the object (or variable) and the given method. The following example shows how you can use `help()` to learn how to use the `upper` method:

```
>>> help(hostname.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
(END)
```

When you’re finished, press **`Q`** to *quit* viewing the built-in help.

At this point, we have already introduced the three functions that will help you gain more understanding of your code. Here is our recommended flow:

1. Check your data type by using `type()`.
2. Check the available methods for your object by using `dir()`.
3. After knowing which method you want to use, learn how to use it by using `help().`

Let’s take a look at several of the string methods, including `count()`, `endswith()`, `startswith()`, `format()`, `isdigit()`, `join()`, `lower()`, `upper()`, and `strip()`.

As we review each method, you should be asking yourself two key questions. What value is returned from the method? And what action is the method performing on the original object?

#### Using the upper() and lower() methods

Using the `upper()` and `lower()` methods is helpful when you need to compare strings that do not need to be case-sensitive. For example, maybe you need to accept a variable that is the name of an interface such as `Ethernet1/1`, but want to also allow the user to enter `ethernet1/1`. The best way to compare these is to use `upper()` or `lower()`:

```
>>> interface = 'Ethernet1/1'
>>>
>>> interface.lower()
'ethernet1/1'
>>>
>>> interface.upper()
'ETHERNET1/1'
```

You can see that when you’re using a method, the format is to enter the object name, or string in this case, and then append *`.methodname()`*:

- The period (`.`) indicates accessing a method (or an attribute) of an object.
- `methodname` is the name of the method.
- The parentheses, `()`, indicate calling the method. As you will see soon, it could take arguments.

Next, after executing `interface.lower()`, notice that `ethernet1/1` is printed to the terminal. This is telling you that `ethernet1/1` was *returned* when `lower()` was executed. The same holds true for `upper()`. When something is returned, you also have the ability to assign it as the value to a new or existing variable:

```
>>> intf_lower = interface.lower()
>>>
>>> print(intf_lower)
ethernet1/1
```

In this example, you can see how to use the method, but also assign the data being returned to a variable.

What about the original variable called `interface`? Let’s see what, if anything, changed with `interface`:

```
>>> print(interface)
Ethernet1/1
```

Since you are exploring the first examples, it still may not be clear what you’re looking for to see if something changed in the original variable `interface`, but you do know that it still holds the value of `Ethernet1/1`, which hasn’t changed. Don’t worry, you’ll see plenty of examples of when the original object is modified throughout this chapter.

#### Using the startswith() and endswith() methods

As you can probably guess, `startswith()` is used to verify whether a string starts with a certain sequence of characters, and `endswith()` is used to verify whether a string ends with a certain sequence of characters:

```
>>> ipaddr = '10.100.20.5'
>>>
>>> ipaddr.startswith('10')
True
>>>
>>> ipaddr.startswith('100')
False
>>>
>>> ipaddr.endswith('.5')
True
```

The `lower()` and `upper()` methods return a string, which is a modified string with all lowercase or uppercase letters. However, `startswith()` and `endswith()` do not return a string, but rather a boolean (`bool`) object. As you’ll learn later in this chapter, boolean values are `True` and `False`. The `startswith()` method returns `True` if the sequence of characters being passed in matches the respective starting or ending sequence of the object. Otherwise, it returns `False`.

###### Note

For the boolean values `True` and `False`, no quotes are used, and the first letter must be capitalized. Booleans are covered in more detail later in the chapter.

Using these methods proves to be valuable when you’re looking to verify the start or end of a string. Maybe you want to verify the first or fourth octet of an IPv4 address or verify an interface name, as you did in the previous example using `lower()`. Rather than assume that a user of a script is going to enter the full name, it’s advantageous to do a check on the first two characters to allow the user to input `ethernet1/1`, `eth1/1`, or `et1/1`.

For this check you’ll combine methods, or use the return value of one method as the base string object for the second method:

```
>>> interface = 'Eth1/1'
>>>
>>> interface.lower().startswith('et')
True
```

You verify that it is an Ethernet interface by first executing `lower()`, which returns `eth1/1`, and then the boolean check is performed to see whether `eth1/1` starts with `et`. And, clearly, it does.

Of course, other parts could be invalid beyond the `eth` in an interface string object, but the point is that methods can be easily used together.

#### Using the strip() method

Some legacy network devices still don’t have APIs. If you want to write a script, it’s plausible that at some point you’ll try it out on an older CLI-based device. If you do this, you’ll be sure to encounter globs of raw text coming back from the device—​this could be the result of any `show` command from the output of `show interfaces` to a full `show running-config`.

When you need to store or simply print something, you may not want any whitespace wrapping the object you want to use or see. To be consistent with previous examples, let’s say this is an IP address.

What if the object you’re working with has the value of `"    10.1.50.1    "` including the whitespace. The methods `startswith()` or `endswith()` don’t work because of the spaces. For these situations, you use `strip()` to remove the whitespace:

```
>>> ipaddr = '   10.1.50.1   '
>>>
>>> ipaddr.strip()
'10.1.50.1'
```

Using `strip()` returns the object without any spaces on both sides. Examples aren’t shown for `lstrip()` or `rstrip()`, but they are two other built-in methods for strings that remove whitespace specifically on the left or right side of a string object, respectively.

#### Using the isdigit() method

While working with strings, you’ll need to verify that the string object is a number at times. Technically, integers are a different data type (covered in the next section), but numbers can still be values in strings.

Using `isdigit()` makes it extremely straightforward to see whether the character or string is actually a *digit*:

```
>>> ten = '10'
>>>
>>> ten.isdigit()
True
>>>
>>> bogus = '10a'
>>>
>>> bogus.isdigit()
False
```

Just as with `startswith()`, `isdigit()` also returns a boolean. It returns `True` if the value is an integer; otherwise, it returns `False`.

#### Using the count() method

Imagine working with a binary number—​maybe it’s to calculate an IP address or subnet mask. Although some built-in libraries can do binary-to-decimal conversion, what if you just want to *count* how many 1s or 0s are in a given string? You can use `count()` to do this for you:

```
>>> octet = '11111000'
>>>
>>> octet.count('1')
5
```

This example shows how easy it is to use `count()`. This method, however, returns an `int` (integer), unlike any of the previous examples.

When using `count()`, you are not limited to sending a single character as a parameter either:

```
>>> octet.count('111')
1
>>>
>>> test_string = "Don't you wish you started programming a little earlier?"
>>>
>>> test_string.count('you')
2
```

#### Using the format() method

You saw earlier how to concatenate strings. Imagine needing to create a sentence, or better yet, a command to send to a network device that is built from several strings or variables. How would you *format* the string, or CLI command?

Let’s use `ping` as an example and assume that the command you need to create is the following:

```
ping 8.8.8.8 vrf management
```

###### Note

The examples in this chapter use generic network CLI commands, as no actual device connections are being made. Thus, they map to no specific vendor and are the de facto “industry standard” examples that work on various systems including Cisco IOS, Cisco NXOS, Arista EOS, and many others.

If you were writing a script from the preceding command, you could identify two variables: `'8.8.8.8'` (the IP address) and `management` (the VRF name). These variables can become user-input parameters that change at every execution.

One way to build the string is to start with the following:

```
>>> ipaddr = '8.8.8.8'
>>> vrf = 'management'
>>>
>>> ping = 'ping' + ipaddr + 'vrf' + vrf
>>>
>>> print(ping)
ping8.8.8.8vrfmanagement
```

You see the spacing is incorrect, so you have two options: add spaces to your input objects or within the `ping` object. Let’s try adding them within `ping`:

```
>>> ping = 'ping' + ' ' + ipaddr + ' ' + 'vrf ' + vrf
>>>
>>> print(ping)
ping 8.8.8.8 vrf management
```

As you can see, this works quite well and is not too complicated, but as the strings or commands get longer, dealing with all the quotes and spaces can get messy. Using the `format()` method can simplify this:

```
>>> ping = 'ping {} vrf {}'.format(ipaddr, vrf)
>>>
>>> print(ping)
ping 8.8.8.8 vrf management
```

The `format()` method takes multiple arguments, which are inserted between the curly braces (`{}`) found within the string. Notice that `format()` is being used on a raw string, unlike in the previous examples.

###### Note

It’s possible to use any of the string methods on both variables or raw strings. This is true for any other data type and its built-in methods as well.

The next example shows using the `format()` method with a pre-created string object (variable), in contrast to the previous example:

```
>>> ping = 'ping {} vrf {}'
>>>
>>> command = ping.format(ipaddr, vrf)
>>>
>>> print(command)
ping 8.8.8.8 vrf management
```

This scenario is more likely, in that you would have a predefined command in a Python script with users inputting two arguments, and the output is the final command string that gets pushed to a network device.

###### Note

Another option to concatenate strings is to use the `%` operator. One example for inserting strings (`s`) is provided here:

```
>>> hostname = 'r5'
>>> interface = 'Eth1/1'
>>>
>>> test = 'Device %s has one interface: %s' % (hostname,
   interface)
>>> print(test)
Device r5 has one interface: Eth1/1
```

Since Python 3.6, a new formatting option for strings is available: *f-strings*, which has an `f` at the beginning of the string and uses `{}` to contain the expressions that will be *rendered* to strings. This formatting option has gained a lot of popularity within the Python community because it helps visualize where the variables are used:

```
>>> f'ping {ipaddr} vrf {vrf}'
'ping 8.8.8.8 vrf management'
```

###### Tip

When using *f-strings* for debugging, you can use `=` after the object name to populate the name of the object rendered:

```
>>> f'Rendering command with: {ipaddr=} {vrf=}'
"Rendering command with: ipaddr='8.8.8.8' vrf='management'"
```

#### Using the join() and split() methods

We saved `join()` and `split()` for last since they include working with another data type called `list`.

###### Note

Although lists are formally covered later in this chapter, we include a brief introduction here to show the `join()` and `split()` methods for string objects.

Lists are exactly what they sound like. They are a *list* of objects, and each object is called an *element*. The elements in a list don’t have to be of the same data type.

In an environment with five routers, you might have a list of hostnames:

```
>>> hostnames = ['r1', 'r2', 'r3', 'r4', 'r5']
```

You can also build a list of commands to send to a network device to make a configuration change. The next example is a list of commands to shut down an Ethernet interface on a switch:

```
>>> commands = ['config t', 'interface Ethernet1/1', 'shutdown']
```

Building a list like this is common, but if you’re using a traditional CLI-based network device, you might not be able to send a `list` object directly to the device. The device may require strings to be sent (or individual commands).

`join()` is one such method that can take a list and create a string, but insert required characters, if needed, between them.

Remember that `\n` is the EOL character. When sending commands to a device, you may need to insert `\n` between commands to allow the device to render a new line for the next command.

If you take `commands` from the previous example, you can see how to leverage `join()` to create a single string with a `\n` inserted between each command:

```
>>> '\n'.join(commands)
'config t\ninterface Ethernet1/1\nshutdown'
```

Another practical example is when using an API such as NX-API that exists on Cisco Nexus switches. Cisco gives the option to send a string of commands, but they need to be separated by a semicolon (`;`). To do this, you use the same approach:

```
>>> ' ; '.join(commands)
'config t ; interface Ethernet1/1 ; shutdown'
```

In this example, you add a space before and after the semicolon, but it’s the same overall approach.

###### Tip

In these examples, a semicolon and an EOL character are used as the separator, but you don’t need to use any characters at all. It’s possible to concatenate the elements in the list without inserting any characters, like this: `''.join(list_name)`.

You’ve learned how to use `join()` to create a string out of a list, but what if you need to do the exact opposite and create a list from a string? One option is to use the `split()` method.

Let’s start with the previously generated string and convert it back to a list:

```
>>> commands = 'config t ; interface Ethernet1/1 ; shutdown'
>>>
>>> cmds_list = commands.split(' ; ')
>>>
>>> print(cmds_list)
['config t', 'interface Ethernet1/1', 'shutdown']
```

This shows how simple it is to take a string object and create a list from it. Another common example for networking is to take an IP address (string) and convert it to a list by using `split()`, creating a list of four elements—​one element per octet:

```
>>> ipaddr = '10.1.20.30'
>>>
>>> ipaddr.split('.')
['10', '1', '20', '30']
```

That covers the basics of working with Python strings. Let’s move on to the next data type, which is numbers.

## Numbers

In this section, we don’t spend much time on different types of numbers such as floats (decimal numbers) or imaginary numbers (complex numbers with a zero real part), but we do briefly look at the data type denoted as `int`, better known as an *integer*. Frankly, this is because most people understand numbers, and there aren’t built-in methods that make sense to cover at this point. Rather than cover built-in methods for integers, we take a look at using mathematical operators while in the Python shell.

###### Note

Decimal numbers in Python are referred to as *floats*. Remember, you can always verify the data type by using the built-in function `type()`:

```
>>> cpu = 41.3
>>>
>>> type(cpu)
<class 'float'>
```

To add numbers, nothing fancy is needed; just add them:

```
>>> 5 + 3
8
>>> a = 1
>>> b = 2
>>> a + b
3
```

A counter might be needed as you are looping through a sequence of objects. You may want to say `counter = 1`, perform some type of operation, and then do `counter = counter + 1`. While this is perfectly functional and works, it is more idiomatic in Python to perform the operation as `counter += 1`, as shown here:

```
>>> counter = 1
>>> counter = counter + 1
>>> counter
2
>>>
>>> counter = 5
>>> counter += 5
>>> counter
10
```

Like addition, subtraction requires nothing special. Let’s dive right into an example:

```
>>> 100 - 90
10
>>> count = 50
>>> count - 20
30
```

When multiplying, yet again, there is no difference:

```
>>> 100 * 50
5000
>>>
>>> print(2 * 25)
50
```

The nice thing about the multiplication operator (`*`) is that you can also use it on strings. You may want to format something and make it nice and pretty:

```
>>> print('=' * 50)
==================================================
```

The preceding example is basic but powerful. Not knowing this is possible, you may be tempted to print one line a time and print a string with the command `print(================)`, but in reality after learning this and a few other tips covered later in the chapter, pretty-printing text data becomes much simpler.

If you haven’t performed any math by hand in recent years, division may seem like a nightmare. As expected, though, it is no different from the previous three mathematical operations reviewed—well, sort of.

To perform a division operation, you still begin by entering `10 / 2`, or `100 / 50`, and so on, like so:

```
>>> 100 / 50
2
```

These examples are probably what you expected to see.

However, you might see a difference in the result, as compared to manual division:

```
>>> 12 / 10
1
```

As you know, the number 10 goes into 12 *one* time. This is called the *quotient*, so here the quotient is equal to 1. What is not displayed or returned is the *remainder*. To see the remainder in Python, you must use the `%`, or modulus, operation.

```
>>> 12 % 10
2
```

This means to fully calculate the result of a division problem, you use both the `/` and `%` operators.

###### Tip

You can convert (or cast) an integer to a string by using `str(10)`, and also do the opposite, converting a string to an integer by using `int('10')`:

```
>>> str(10)
'10'
>>> int('10')
10
```

That was a brief look at how to work with numbers in Python. We’ll now move on to booleans.

## Booleans

*Boolean objects*, otherwise known as objects that are of type `bool` in Python, are fairly straightforward. Let’s first review the basics of general boolean logic by looking at a *truth table* ([Table 6-2](#table-boolean-truth)).

| A | B | A and B | A or B | Not A |
| --- | --- | --- | --- | --- |
| False | False | False | False | True |
| False | True | False | True | True |
| True | False | False | True | False |
| True | True | True | True | False |

Notice that all values in the table are either `True` or `False`. This is because with boolean logic, all values are reduced to either `True` or `False`. This makes booleans easy to understand.

Since boolean values can be only `True` or `False`, all expressions also evaluate to either `True` or `False`. You can see in the table that *both* values, for A and B, need to be `True`, for “A and B” to evaluate to `True`. And “A or B” evaluates to `True` when *any* value (A or B) is `True`. You can also see that when you take the *NOT* of a boolean value, it calculates the inverse of that value. This is seen clearly as `NOT False` yields `True` and `NOT True` yields `False`.

From a Python perspective, nothing is different. We still have only two boolean values: `True` and `False`. To assign one of these values to a variable within Python, you must enter it just as you see it (with a capitalized first letter, and without quotes):

```
>>> exists = True
>>>
>>> exists
True
>>>
>>> exists = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

As you can see, using booleans is quite simple. Based on the real-time feedback of the Python interpreter, you can see that using a lowercase *t* doesn’t work when you’re trying to assign the value of `True` to a variable.

Here are a few more examples of using boolean expressions while in the Python interpreter:

```
>>> True and True
True
>>>
>>> True or False
True
>>>
>>> False or False
False
```

In the next example, these same conditions are evaluated, assigning boolean values to variables:

```
>>> value1 = True
>>> value2 = False
>>>
>>> value1 and value2
False
>>>
>>> value1 or value2
True
```

Notice that boolean expressions are also not limited to two objects:

```
>>> value3 = True
>>> value4 = True
>>>
>>> value1 and value2 and value3 and value4
False
>>>
>>> value1 and value3 and value4
True
```

When extracting information from a network device, using booleans for a quick check is common. Is the interface a routed port? Is the management interface configured? Is the device reachable? While a complex operation may be required to answer each of those questions, the result is stored as `True` or `False`.

The opposite of those questions would be, is the interface a switched port or is the device not reachable? Having variables or objects for each question wouldn’t make sense, but we could use the `not` operator, since we know the `not` operation returns the inverse of a boolean value.

Let’s take a look at using `not` in an example:

```
>>> not False
>>> True
>>>
>>> is_layer3 = True
>>> not is_layer3
False
```

This example uses a variable called `is_layer3`. It is set to `True`, indicating that an interface is a Layer 3 port. If you take the `not` of `is_layer3`, you would then know if it is a Layer 2 port.

We introduce conditionals (`if-else` statements) later in the chapter, but based on the logic needed, you may need to know whether an interface is in fact Layer 3. If so, you would have something like `if is_layer3:`, but if you needed to perform an action if the interface was Layer 2, then you would use `if not is_layer3:`.

In addition to using the `and` and `or` operands, the *equal to* (`==`) and *does not equal to* (`!=`) expressions are used to generate a boolean object. With these expressions, you can do a comparison, or check, to see whether two or more objects are (or not) equal to one another:

```
>>> True == True
True
>>> True != False
True
>>> 'network' == 'network'
True
>>> 'network' == 'no_network'
False
```

# Empty Objects

Python offers a simple and readable way to *evaluate* whether an object is empty. If the object is not empty, the evaluation will return `True`, and if empty, will return `False`. In the following example, you can notice how easy it is to read the code `if not devices:`. It’s almost literal: if there are no `devices`, the assessment will match the `if` statement:

```
>>> devices = []
>>> if not devices:
...     print('devices is empty')
...
devices is empty
>>>
>>> hostname = 'something'
>>>
>>> if hostname:
...    print('hostname is not empty')
...
hostname is not empty
```

However, even though this *evaluation* usually matches what we understand as *emptiness*, the actual logic applied is the boolean evaluation of the object, implemented via the `__bool__` dunder method, and could be customized for our own class, as we will explore in [“Understanding Python Classes”](#python-classes).

After a quick look at working with boolean objects, operands, and expressions, we are ready to cover working with Python lists.

## Lists

You had a brief introduction to lists when we covered the string built-in methods called `join()` and `split()`. This section covers lists in a bit more detail.

*Lists* are the object type called `list`, and at their most basic level are an ordered sequence of objects. The examples from earlier in the chapter when we looked at the `join()` method with strings are provided again next to provide a quick refresher on how to create a list. Those examples were lists of strings, but it’s also possible to have lists of any other data type as well, which you’ll see shortly.

```
>>> hostnames = ['r1', 'r2', 'r3', 'r4', 'r5']
>>> commands = ['config t', 'interface Ethernet1/1', 'shutdown']
```

Here is a list of objects in which each object is a different data type:

```
>>> new_list = ['router1', False, 5]
>>>
>>> print(new_list)
['router1', False, 5]
```

Now you understand that lists are an ordered sequence of objects and are enclosed by brackets. One of the most common tasks when you’re working with lists is to access an individual element of the list.

Let’s create a new list of interfaces and show how to print a single element of a list:

```
>>> interfaces = ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4']
```

The list is created, and now three elements of the list are printed one at a time:

```
>>> print(interfaces[0])
Eth1/1
>>>
>>> print(interfaces[1])
Eth1/2
>>>
>>> print(interfaces[3])
Eth1/4
```

To access the individual elements within a list, you use the element’s *index* value enclosed within brackets. It’s important to see that the index begins at 0 and ends at the “length of the list minus 1.” This means in our example, to access the first element, you use `interfaces[0]` and to access the last element, you use `interfaces[3]`.

You can easily see that the length of the preceding list is 4, but what if you didn’t know the length of the list?

Luckily, Python provides a built-in function called `len()` to help with this:

```
>>> len(interfaces)
4
```

So, you can access the last element of the list by subtracting 1 from its length: `list_name[len(list_name) - 1]`:

```
>>> interfaces[len(interfaces) - 1]
'Eth1/4'
```

Another way, more Pythonic, to access the last element in any list is: `list_name[-1]`. So, with the minus we are indexing the list from the end, instead of the beginning:

```
>>> interfaces[-1]
'Eth1/4'
```

###### Note

Often, the terms *function* and *method* are used interchangeably, but until now we’ve mainly shown methods, not functions. The slight difference is that a function is called without referencing a parent object. As you saw, when you use a built-in method of an object, it is called using the syntax `object.method()`, and when you use a function like `len()`, you call it directly. That said, it is common to call a method a function.

The same *indexing* access used for *lists* also works for *strings*. If a variable called `router` is assigned the value of `"DEVICE"`, then `router[0]` returns `"D"`.

However, a string is not a list, so you can’t assign a new value to the indexed position. String is an *immutable* type; it cannot be modified. Notice that if you assign a different value, `hostname = 'something else'`, you are not modifying the string; you are creating a new one. If you try to modify an element of a string, you will observe an error raised:

```
>>> hostname[1] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

A useful technique, to produce a subset of a sequence (such as lists or strings), is *slicing*. Using a colon (`:`) before or after the index, you can indicate that you want to retrieve all the elements before or after the index, respectively. This can become pretty powerful when you need to parse through different types of objects:

```
>>> hostname = 'DEVICE_12345'
>>>
>>> hostname[4:]
'CE_12345'
>>>
>>> hostname[:-2]
'DEVICE_123'
```

### Using built-in methods of Python lists

To view the available built-in methods for lists, the `dir()` function is used just as we showed previously when working with string objects. You can create any variable that is a list or use the formal data type name of `list` and pass it as an argument to `dir()`. You’ll use the `interfaces` list for this:

```
>>> dir(interfaces)
[... omitted dunders ..., 'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
```

Let’s take a look at a few of these built-in methods.

#### Using the append() method

The great thing about these method names, as you’ll continue to see, is that they are human-readable, and for the most part, intuitive. The `append()` method is used to *append*, or add, an element to an existing list.

This is shown in the next example, but let’s start with creating an empty list. You do so by assigning empty brackets to an object:

```
>>> vendors = []
```

Let’s append `vendors` to this list:

```
>>> vendors.append('arista')
>>>
>>> print(vendors)
['arista']
>>>
>>> vendors.append('cisco')
>>>
>>> print(vendors)
['arista', 'cisco']
```

You can see that using `append()` adds the element to the *last* position in the list. In contrast to many of the methods reviewed for strings, this method is *not* returning anything, but modifying the original variable, or object.

#### Using the insert() method

Rather than just append an element to a list, you may need to *insert* an element at a specific location. This is done with the `insert()` method.

To use `insert()`, you need to pass it two arguments. The first argument is the position, or index, where the new element gets stored, and the second argument is the object getting inserted into the list:

```
>>> commands = ['interface Eth1/1', 'ip address 192.0.2.1/32']
```

###### Note

As a reminder, the commands in these examples are generic and do not map back to a specific vendor or platform.

Let’s now assume you need to add two more commands to the previous `commands` list. The command that needs to be added as the first element is `config t`, and the one that needs to be added just before the IP address is `no switchport`:

```
>>> commands = ['interface Eth1/1', 'ip address 192.0.2.1/32']
>>>
>>> commands.insert(0, 'config t')
>>>
>>> print(commands)
['config t', 'interface Eth1/1', 'ip address 192.0.2.1/32']
>>>
>>> commands.insert(2, 'no switchport')
>>>
>>> print(commands)
['config t', 'interface Eth1/1', 'no switchport', 'ip address 192.0.2.1/32']
```

###### Tip

Using indexes bigger than the actual length of the list will not raise an error. It will simply insert the objects at the end of the list:

```
>>> commands.insert(9999, "shutdown")
>>> commands
['config t', 'interface Eth1/1', 'no switchport',
'ip address 192.0.2.1/32', 'shutdown']
```

#### Using the count() method

If you are doing an inventory of types of devices throughout the network, you may build a list that has more than one of the same object within a list. To expand on the earlier example, you may have a list that looks like this:

```
>>> vendors = ['cisco', 'cisco', 'juniper', 'arista', 'cisco', 'hp', 'cumulus',
'arista', 'cisco']
```

You can *count* how many instances of a given object are found by using the `count()` method. In our example, this can help determine how many Cisco or Arista devices are in the environment:

```
>>> vendors.count('cisco')
4
>>>
>>> vendors.count('arista')
2
```

Note that `count()` returns an `int`, or integer, and does not modify the existing object—unlike `insert()`, `append()`, and a few others reviewed in the upcoming examples.

#### Using the pop() and index() methods

Most of the methods thus far have either modified the original object or returned something. The `pop()` method does both:

```
>>> hostnames = ['r1', 'r2', 'r3', 'r4', 'r5']
```

The preceding example has a list of hostnames. Let’s pop (remove) `r5` because that device was just decommissioned from the network:

```
>>> hostnames.pop()
'r5'
>>>
>>> print(hostnames)
['r1', 'r2', 'r3', 'r4']
```

As you can see, the element being popped is returned, *and* the original list is modified as well. You should also notice that no element or index value was passed in, so you can see by default, `pop()` pops the last element in the list.

What if you need to pop `r2`? It turns out that to *pop* an element that is not the last one, you need to pass in an index value of the element that you wish to pop. But how do you find the index value of a given element? This is where the `index()` method comes into play.

To find the index value of a certain element, use `index()`:

```
>>> hostnames.index('r2')
1
```

Here you see that the index of the value `r2` is `1`.

So, to pop `r2`, you would perform the following:

```
>>> hostnames.pop(1)
'r2'
>>>
>>> print(hostnames)
['r1', 'r3', 'r4']
```

You could also do this in a single step:

```
>>> hostnames.pop(hostnames.index('r2'))
```

#### Using the sort() method

The last built-in method to take a look at for lists is `sort()`. As you may have guessed, `sort()` is used to *sort* a list.

In the next example, you have a list of IP addresses in nonsequential order, and you use `sort()` to update the original object. Notice that nothing is returned:

```
>>> available_ips = ['10.1.1.1', '10.1.1.9', '10.1.1.8', '10.1.1.7', '10.1.1.4']
>>>
>>> available_ips.sort()
>>>
>>> available_ips
['10.1.1.1', '10.1.1.4', '10.1.1.7', '10.1.1.8', '10.1.1.9']
```

###### Note

The sort from the previous example sorts IP addresses as strings instead of as IP addresses. So, if in `available_ips` you had `2.2.2.2`, this “smaller” IP address will be sorted to be the last, because, as characters, `10 < 2`.

A useful practice when working with methods is to check the available *customization* options. Usually, a method behavior has already implemented some tuning options to cover the common use cases. The `help()` method will show you all the detail:

```
>>> help(list.sort)
Help on method_descriptor:

sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.
    ...

    The reverse flag can be set to sort in descending order.
(END)
```

The `sort()` method supports a named boolean argument, `reverse`, that can sort the list in *descending* order:

```
>>> available_ips.sort(reverse=True)
>>>
>>> available_ips
['10.1.1.9', '10.1.1.8', '10.1.1.7', '10.1.1.4', '10.1.1.1']
```

In nearly all our list examples, the elements of the list are the same type of object; that is, they are all strings: commands, IP addresses, vendors, or hostnames. However, Python allows you to create lists that store different types of objects.

A prime example of storing different objects arises when storing information about a particular device. Maybe you want to store the hostname, vendor, and OS. A list to store these device attributes would look something like this:

```
>>> device = ['router1', 'juniper', '12.2']
```

Since elements of a list are indexed by an integer, you need to keep track of which index is mapped to which particular attribute. While it may not seem hard for this example, what if 10, 20, or 100 attributes need to be accessed? Even if mappings were available, it could get extremely difficult since lists are *ordered*. Replacing or updating any element in a list would need to be done carefully.

Wouldn’t it be nice if you could reference the individual elements of a list by *name* and not worry so much about the *order* of elements? So, rather than access the hostname by using `device[0]`, you could access it like `device['hostname']`. As luck would have it, this is exactly where Python dictionaries come into action, and they are the next data type we cover in this chapter.

## Python Dictionaries

We’ve now reviewed some of the most common data types, including strings, integers, booleans, and lists, which exist across all programming languages. In this section, we introduce the *dictionary*, which is a Python-specific data type. In other languages, they are known as *associative arrays*, *maps*, or *hash maps*.

Dictionaries are ordered lists by *insertion*, and their *values* are accessed by names, otherwise known as *keys*, instead of by index (integer). Dictionaries are simply a collection of *key-value* pairs called *items*.

###### Note

In earlier versions of Python, dictionaries were an *unordered* data structure. You were not able to warrant the order of the items. However, as of Python 3.7, dictionaries are guaranteed to preserve the order in which key-value pairs are inserted.

We finished the previous section on lists with this example:

```
>>> device = ['router1', 'juniper', '12.2']
```

If you build on this example and convert the list `device` to a dictionary, it would look like this:

```
>>> device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
```

The notation for a dictionary is a curly brace (`{`), then key, colon, and value, for each key-value pair, separated by a comma (`,`), and then it closes with another curly brace (`}`).

Once the `dict` object is created, you access the desired value by using *`dict`*[*`key`*]:

```
>>> print(device['hostname'])
router1
>>>
>>> print(device['os'])
12.1
>>>
>>> print(device['vendor'])
juniper
```

You can create the same dictionary from the previous example in a few ways. Two are shown here:

```
>>> device = {}
>>> device['hostname'] = 'router1'
>>> device['vendor'] = 'juniper'
>>> device['os'] = '12.1'
>>>
>>> print(device)
{'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
```

```
>>> device = dict(hostname='router1', vendor='juniper', os='12.1')
>>>
>>> print(device)
{'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
```

### Using built-in methods of Python dictionaries

Python dictionaries have a few built-in methods worth covering, so as usual, we’ll dive right into them. Just as with the other data types, we first present all available methods minus those that start and end with underscores:

```
>>> dir(dict)
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
'setdefault', 'update', 'values']
```

#### Using the get() method

You saw earlier how to access a key-value pair of a dictionary by using the notation of *`dict`*[*`key`*]. That is a popular approach, but with one caveat. If the key does not exist, Python raises a `KeyError` (similarly, a `list` would raise an `IndexError` when accessing a nonexistent position):

```
>>> device
{'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
>>>
>>> print(device['model'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'model'
```

Using the `get()` method provides another approach that is arguably safer, unless you *want* to raise an exception. We explore more about exceptions in [“Embracing Failure with try/except”](#python-exceptions).

Let’s first look at an example using `get()` when the key exists:

```
>>> device.get('hostname')
'router1'
```

And now an example of when a key doesn’t exist:

```
>>> device.get('model')
>>>
```

As you can see, absolutely nothing is returned when the key isn’t in the dictionary, but it gets better than that. The `get()` method also allows the user to define a value to return when the key does not exist! Let’s take a look:

```
>>> device.get('model', False)
False
>>>
>>> device.get('model', 'DOES NOT EXIST')
'DOES NOT EXIST'
>>>
>>> device.get('hostname', 'DOES NOT EXIST')
'router1'
```

Pretty simple, right? You can see that the value to the right of the key is returned only if the key does not exist within the dictionary.

#### Using the keys() and values() methods

Dictionaries are a list of key-value pairs. Using the built-in methods `keys()` and `values()`, you can access each object individually.

In Python 3, these methods do not return a simple list but dictionary *view objects* that can be iterated to yield the data, as you will see in [“Using Loops in Python”](#python-loops). Notice that the order of the items is preserved:

```
>>> device.keys()
dict_keys(['hostname', 'vendor', 'os'])
>>>
>>> device.values()
dict_values(['router1', 'juniper', '12.1'])
```

However, these view objects can’t be accessed directly:

```
>>> device.keys()[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_keys' object is not subscriptable
```

To access a specific object, you need to first convert the data to a list with `list()`:

```
>>> list(device.keys())[0]
'hostname'
```

#### Using the pop() method

We introduced the built-in method `pop()` earlier in the chapter when we were reviewing lists. It just so happens dictionaries also have a `pop()` method, and it’s used similarly. Instead of passing the method an index value as you did with lists, you pass it a key:

```
>>> device
{'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
>>>
>>> device.pop('vendor')
'juniper'
>>>
>>> device
{'hostname': 'router1', 'os': '12.1'}
```

You can see that `pop()` modifies the original object *and* returns the value being popped.

#### Using the update() method

There may come a time when you are extracting device information such as hostname, vendor, and OS from a network device and storing it in a Python dictionary. And down the road you need to add to or *update* it with another dictionary that has other attributes about a device.

The following shows two dictionaries:

```
>>> device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
>>>
>>> oper = dict(cpu='5%', memory='10%')
>>>
>>> oper
{'cpu': '5%', 'memory': '10%'}
```

You can use the `update()` method to update one of the dictionaries, basically adding one dictionary to the other. Let’s add `oper` to `device`:

```
>>> device.update(oper)
>>>
>>> print(device)
{'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1', 'cpu': '5%',
'memory': '10%'}
```

If a *match* occurs with a dictionary key, the `update()` method will *update* the old value with the new value from the new dictionary. In the next example, the `vendor` key from `device` is changed from the original `juniper` to `arista` because the data from `new_vendor` is updated on the reference dictionary:

```
>>> new_vendor = {'vendor': 'arista'}
>>>
>>> device.update(new_vendor)
>>>
>>> print(device)
{'hostname': 'router1', 'vendor': 'arista', 'os': '12.1', 'cpu': '5%',
'memory': '10%'}
```

Notice that nothing is returned with `update()`. Only the object being updated, or `device` in this case, is modified.

#### Using the items() method

When working with dictionaries, you’ll see `items()` used *a lot*, so it is extremely important to understand—​not to discount the other methods, of course!

You saw how to access individual values via `get()` and how to get a list of all the keys and values via the `keys()` and `values()` methods, respectively. What about accessing a particular key-value pair of a given item at the same time, or iterating over all items? If you need to iterate (or loop) through a dictionary and simultaneously access keys and values, `items()` is a great tool for your tool belt.

###### Note

We formally introduce loops later in this chapter, but because `items()` is commonly used with a `for` loop, we are showing an example with a `for` loop here. The important takeaway is that when using the `for` loop with `items()`, you can access a key and value of a given item at the same time.

The most basic example is looping through a dictionary with a `for` loop and printing the key *and* value for each item. Again, loops are covered later in the chapter, but this is meant just to give a basic introduction to `items()`:

```
>>> for key, value in device.items():
...     print(f'{key}: {value}')
...
hostname: router1
vendor: arista
os: 12.1
cpu: 5%
memory: 10%
```

In the `for` loop, `key` and `value` are user-defined and could have been anything, as you can see in this example:

```
>>> for my_attribute, my_value, in device.items():
...     print(f'{my_attribute}: {my_value}')
...
hostname: router1
vendor: arista
os: 12.1
cpu: 5%
memory: 10%
```

Now that we’ve covered the major data types in Python, you should have a good understanding of how to work with strings, numbers, booleans, lists, and dictionaries.  Next we introduce two more data types—sets and tuples—that are a bit more advanced than the previous data types covered.

## Sets and Tuples

The next two data types don’t necessarily need to be covered in an introduction to Python, but as we said at the beginning of the chapter, we want to include a quick summary of them for completeness. These data types are `set` and `tuple`.

If you understand lists, you’ll understand sets. *Sets* are a list of elements, but there can be only one of a given element in a set, and additionally, elements cannot be indexed (or accessed by an index value, like a list).

You can see that a set looks like a list, but is surrounded by `set()`:

```
>>> vendors = set(['arista', 'cisco', 'arista', 'cisco', 'juniper', 'cisco'])
```

This set is being created with multiple elements that are the same. We used a similar example when using the `count()` method with lists to count the number of devices from a given vendor. But what if you want to know only how many, and which, vendors exist in an environment? You can use a set:

```
>>> vendors = set(['arista', 'cisco', 'arista', 'cisco', 'juniper', 'cisco'])
>>>
>>> vendors
set(['cisco', 'juniper', 'arista'])
>>>
>>> len(vendors)
3
```

Notice that `vendors` contains only three elements.

The next example shows what happens when you try to access an element within a set. You must iterate through the elements, using a `for` loop as an example:

```
>>> vendors[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

We leave as an exercise for you to explore the built-in methods for `sets`.

The tuple is an interesting data type and also best understood when compared to a list. It is like a list but cannot be modified. You saw that lists are *mutable*, meaning that you can update, extend, and modify them. Tuples, on the other hand, are *immutable*, and you can’t modify them after they’re created. Also, as with lists, it’s possible to access individual elements of tuples:

```
>>> description = ('ROUTER1', 'PORTLAND')
>>>
>>> description
('ROUTER1', 'PORTLAND')
>>>
>>> print(description[0])
ROUTER1
```

After the variable object `description` is created, there is no way to modify it. You cannot modify any of the elements or add new elements. This could help if you need to create an object and want to ensure that no other function or user can modify it. The next example shows that you cannot modify a tuple and that a tuple has no methods such as `update()` or `append()`:

```
>>> description[1] = 'trying to modify one'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> dir(tuple)
[... omitted dunders ..., 'count', 'index']
```

To help compare and contrast lists, tuples, and sets, we have put this high-level summary together:

ListsAre mutable, can be modified, contain individual elements they can be accessed directly, and can have duplicate values

SetsAre mutable, can be modified, contain individual elements that cannot be accessed directly, and cannot have duplicate values

TuplesAre immutable, cannot be updated or modified after they’re created, contain individual elements that can be accessed directly, and can have duplicate values

You have learned about various Python types, each with its own behavior and methods. So, in your programs you might like to validate the variable’s type before using it. The `isinstance()` built-in function can identify a type, not only for built-in types but also custom-class types:

```
>>> hostname = ''
>>> devices = []

>>> if isinstance(devices, list):
...     print('devices is a list')
...
devices is a list
>>>
>>> if isinstance(hostname, str):
...     print('hostname is a string')
...
hostname is a string
```

This concludes the section on data types. We’ll now shift gears a bit and jump into using conditionals (*if then* logic) in Python.

# Adding Conditional Logic to Your Code

By now you should have a solid understanding of working with various types of objects. The beauty of programming comes into play when you start to use those objects by applying logic within your code, such as executing a task or creating an object when a particular condition is true (or not true!).

*Conditionals* are a key part of applying logic within your code, and understanding conditionals starts with understanding the `if` statement. Let’s start with a basic example that checks the value of a string:

```
>>> hostname = 'NYC'
>>>
>>> if hostname == 'NYC':
...     print('The hostname is NYC')
...
The hostname is NYC
```

Even if you did not understand Python before starting this chapter, odds are you know what is being done in this example. This is part of the value of working in Python—​it tries to be as human-readable as possible.

When you’re working with an `if` statement, note two parts of the syntax. First, *all* `if` statements end with a colon (`:`). Second, the code that gets executed *if* your condition is true is part of an indented block—​this indentation *should be* four spaces, but the number of spaces technically does not matter. All that *technically* matters is that you are consistent.

###### Tip

Generally speaking, it is good practice to use a four-space indent when writing Python code. This is widely accepted by the Python community as the norm for writing idiomatic Python code. This makes code sharing and collaboration much easier.

The following shows a full indented code block:

```
>>> if hostname == 'NYC':
...     print('This hostname is NYC')
...     print(len(hostname))
...     print('The End.')
...
This hostname is NYC
3
The End.
```

Now that you understand how to construct a basic `if` statement, let’s add to it.

What if you need to do a check to see if the hostname is `NJ` in addition to `NYC`? To accomplish this, you use the *else if* statement, or `elif`:

```
>>> hostname = 'NJ'
>>>
>>> if hostname == 'NYC':
...     print('This hostname is NYC')
... elif hostname == 'NJ':
...     print('This hostname is NJ')
...
This hostname is NJ
```

Similar to the `if` statement, the `elif` statement needs to end with a colon, and the associated code block to be executed must be indented. The `elif` statement also must be aligned to the `if` statement.

What if `NYC` and `NJ` are the only valid hostnames, but now you need to execute a block of code if another hostname is being used? This is where you use the `else` statement:

```
>>> hostname = 'DEN_CO'
>>>
>>> if hostname == 'NYC':
...     print('This hostname is NYC')
... elif hostname == 'NJ':
...     print('This hostname is NJ')
... else:
...     print('UNKNOWN HOSTNAME')
...
UNKNOWN HOSTNAME
```

Using `else` isn’t any different from using `if` and `elif`. It needs a colon (`:`) and an indented code block underneath it to execute.

When Python executes conditional statements, the conditional block is exited as soon as a match occurs. For example, if `hostname` is equal to `NYC`, there would be a match on the first line of the conditional block, the `print` statement `print('This hostname is NYC')` would be executed, and then the block would be exited (no other `elif` or `else` would be executed).

The following is an example of an error produced because of incorrect indentation. The example has extra spaces in front of `elif` that should not be there:

```
>>> if hostname == 'NYC':
...     print('This hostname is NYC')
...   elif hostname == 'NJ':
  File "<stdin>", line 3
    elif hostname == 'NJ':
                         ^
IndentationError: unindent does not match any outer indentation level
```

And the following shows an error produced by a missing colon:

```
>>> if hostname == 'NYC'
  File "<stdin>", line 1
    if hostname == 'NYC'
                       ^
SyntaxError: invalid syntax
```

The point is, even if you have a typo in your code when you’re just getting started, don’t worry; you’ll see pretty intuitive error messages.

You will continue to see conditionals in upcoming examples, including the next one, which introduces the concept of containment.

# Understanding Containment

When we say *containment*, we are referring to the ability to check whether an object *contains* a specific element or object. Specifically, let’s look at the usage of `in`, building on what you just learned with conditionals. Although this section covers only `in`, don’t underestimate this powerful containment feature of Python.

If you use the `vendors` variable that has been used in previous examples, how would you check to see if a particular vendor exists? One option is to loop through the entire list and compare the vendor you’re looking for with each object. That’s definitely possible, but why not just use `in`?

Using containment is not only readable, but also simplifies the process for checking whether an object has what you are looking for:

```
>>> vendors = ['arista', 'juniper', 'cumulus', 'cisco']
>>>
>>> 'arista' in vendors
True
```

This syntax is straightforward, and a `bool` is returned. It’s worth mentioning that this syntax is another one of those expressions that is considered writing idiomatic Python code.

This can now be taken a step further and added into a conditional statement:

```
>>> if 'arista' in vendors:
...     print('Arista is deployed.')
...
'Arista is deployed.'
```

Just as in previous examples, where you checked whether an element was in a list, in this next example, check to see if part of a string is *in* another string. You use a basic boolean expression and then use the expression in a conditional statement:

```
>>> version = "CSR1000V (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.1"
>>>
>>> "16.3.1" in version
True
>>>
>>> if "16.3.1" in version:
...   print("Version is 16.3.1!!")
...
Version is 16.3.1!!
```

###### Note

The `in` operator is implemented by the `__contains__` dunder method. So, any object that implements this method can be used with the `in` operator.

As we previously stated, containment when combined with conditionals is a simple yet powerful way to check whether an object or value exists within another object. In fact, when you’re just starting out, it is quite common to build really long and complex conditional statements, but what you really need is a more efficient way to evaluate the elements of a given object.

One such way is to use loops while working with objects such as lists and dictionaries. Using loops simplifies the process of working with these types of objects. This will become much clearer soon, as our next section formally introduces loops.

# Using Loops in Python

We’ve finally made it to loops. As objects continue to grow, especially those that are much larger than our examples thus far, loops are absolutely required. Start to think about lists of devices, IP addresses, VLANs, and interfaces. We’ll need efficient ways to search data or perform the same operation on each element in a set of data (as examples). This is where loops begin to show their value.

In this section, we cover two main types of loops: the `for` loop and `while` loop. From the perspective of a network engineer who is looking at automating network devices and general infrastructure, you can get away with almost always using a `for` loop. Of course, it depends on exactly what you are doing, but generally speaking, `for` loops in Python are pretty awesome, so we’ll save them for last.

## The while Loop

The general premise behind a `while` loop is that a set of code is executed *while* a certain condition is true. In the example that follows, the variable `counter` is set to `1` and then for as long as, or *while*, it is less than `5`, the variable is printed, and then increased by 1.

The syntax required is similar to what we used when creating `if-elif-else` statements. The `while` statement is completed with a colon (`:`), and the code to be executed is indented four spaces:

```
>>> counter = 1
>>>
>>> while counter < 5:
...     print(counter)
...     counter += 1
...
1
2
3
4
```

This introduction is all we are going to cover on the `while` loop, as we’ll be using the `for` loop in the majority of examples going forward.

## The for Loop

The `for` loop in Python is awesome because when you use it, you are usually looping, or *iterating*, over a set of objects, like those found in a list, string, or dictionary. In other programming languages, `for` loops require an index and increment value to always be specified, which is not the case in Python.

Let’s start by reviewing a *for-in*, or *for-each* loop, which is the most common type of `for` loop in Python. As in the previous sections, we start by reviewing a few basic examples.

The first prints each object within a list. You can see in the following example that the syntax is simple, and again, much like what you learned when using conditionals and the `while` loop. The first statement, or the beginning of the `for` loop, needs to end with a colon (`:`), and the code to be executed must be indented:

```
>>> vendors = ['arista', 'juniper', 'cisco']
>>>
>>> for vendor in vendors:
...     print(f'VENDOR: {vendor}')
...
VENDOR:  arista
VENDOR:  juniper
VENDOR:  cisco
```

As mentioned earlier, this type of `for` loop is often called a *for-in* or *for-each* loop because you are iterating over *each* element *in* a given object.

In the example, the name of the object `vendor` is totally arbitrary and up to the user to define, and for each iteration, `vendor` is equal to that specific element. For example, in this example `vendor` equals `arista` during the first iteration, `juniper` in the second iteration, and so on.

To show that `vendor` can be named anything, let’s rename it `network_vendor`:

```
>>> for network_vendor in vendors:
...     print(f'VENDOR: {network_vendor}')
...
VENDOR:  arista
VENDOR:  juniper
VENDOR:  cisco
```

Let’s now combine a few of the things you’ve learned so far with containment, conditionals, and loops.

In the next example, you have a new list of `vendors`. One of them is a *great* company, but just not cut out to be a network vendor! Then, you define `approved_vendors`, which is basically the approved vendors for a given customer. This example loops through the vendors to ensure that they are all approved, and if not, prints a statement saying so to the terminal:

```
>>> vendors = ['arista', 'juniper', 'cisco', 'oreilly']
>>>
>>> approved_vendors = ['arista', 'juniper', 'cisco']
>>>
>>> for vendor in vendors:
...     if vendor not in approved_vendors:
...         print(f'NETWORK VENDOR NOT APPROVED: {vendor}')
...
NETWORK VENDOR NOT APPROVED:  oreilly
```

You can see that `not` can be used in conjunction with `in`, making the code powerful and easy to read.

[Example 6-1](#python-for-loop) is a more challenging example: you loop through a dictionary, while extracting data from another dictionary, and even get to use some built-in methods you learned earlier in this chapter.

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch06-python*](https://github.com/oreilly-npa-book/examples/tree/v2/ch06-python).

##### Example 6-1. Using a `for` loop with `items()`

```
>>> COMMANDS = {
...     'description': 'description {}',
...     'speed': 'speed {}',
...     'duplex': 'duplex {}',
... }
>>> CONFIG_PARAMS = {
...     'description': 'auto description by Python',
...     'speed': '10000',
...     'duplex': 'auto'
... }
>>> commands_list = []
>>>
>>> for feature, value in CONFIG_PARAMS.items():
...     command = COMMANDS.get(feature).format(value)
...     commands_list.append(command)
...
>>> commands_list.insert(0, 'interface Eth1/1')
>>>
>>> print(commands_list)
['interface Eth1/1', 'description auto description by Python',
'speed 10000', 'duplex auto']
```

###### Note

Using uppercase variables (e.g., `COMMANDS` or `CONFIG_PARAMS`) is a Python convention to refer to variables containing constant values, which do not change during execution.

In this example, you start building a dictionary that stores CLI commands to configure certain features on a network device into the `COMMANDS` variable.

You have a dictionary of three items (key-value pairs). Each item’s key is a network feature to configure, and each item’s value is the start of a command string that’ll configure that respective feature. These features include speed, duplex, and description. Each value of the dictionary is followed by curly braces (`{}`) because you’ll be using the `format()` method of strings to insert variables.

After the `COMMANDS` dictionary is created, you create a second dictionary called `CONFIG_PARAMS` that will be used to dictate which commands will be executed and which value will be used for each command string defined in `COMMANDS`.

Then you use a `for` loop to iterate through `CONFIG_PARAMS()` using the `items` built-in method for dictionaries. As you iterate through, you’ll use the key from `CONFIG_​PAR⁠AMS` to `get` the proper value, or command string, from `COMMANDS`. This is possible because they were prebuilt using the same key structure. The command string is returned with curly braces, but as soon as it’s returned, you use the `format()` method to insert the proper value, which happens to be the value in `CONFIG_PARAMS`.

Now we’ll walk through this in even more detail. Please take your time and even test this out yourself while on the Python interactive interpreter.

In the first line, `commands_list` is creating an empty list `[]`. This is required in order to `append()` to this list later.

You then use the `items()` built-in method as you loop through `CONFIG_PARAMS`. This was covered briefly earlier in the chapter, but `items()` is giving you, the network developer, access to both the key *and* value of a given key-value pair at the same time. This example iterates more than three key-value pairs: `description`/`auto description` by Python, `speed`/`10000`, and `duplex`/`auto`.

During each iteration—​that is, for each key-value pair that is being referred to as the variables `feature` and `value`—a command is being pulled from the `COMMANDS` dictionary. As you may recall, the `get()` method is used to get the value of a key-value pair when you specify the key. In the example, this key is the `feature` object. The value being returned is `description {}` for `description`, `speed {}` for `speed`, and `duplex {}` for `duplex`. As you can see, all of these objects being returned are strings, so then you are able to use the `format()` method to insert the `value` from `CONFIG_PARAMS` because you also saw earlier that multiple methods can be used together on the same line. Once the value is inserted, the command is appended to `commands_list`.

Finally, after the commands are built, you insert interface `Eth1/1` as the first item of the list. This could have also been done first, with `commands_list = ['interface Eth1/1']`. If you understand this example, you’re at a really good point already with getting a grasp on Python!

You’ve now seen some of the most common types of `for` loops that allow you to iterate over lists and dictionaries. We’ll now take a look at another way to construct and use a `for` loop.

### Using the enumerate() function

Occasionally, you may need to keep track of an index value as you loop through an object. We show this fairly briefly, since most of these examples are like the previous examples already covered.

The `enumerate()` function is used to enumerate the list and give an index value, and is often handy to determine the exact position of a given element.

The next example shows how to use `enumerate()` within a `for` loop. You’ll notice that the beginning part of the `for` loop looks like the dictionary examples, only unlike `items()`, which returns a key and value, `enumerate()` returns an index, starting at 0, and the object from the list that you are enumerating.

The example prints both the index and value to help you understand what it is doing:

```
>>> vendors = ['arista', 'juniper', 'cisco']
>>>
>>> for index, each in enumerate(vendors):
...     print(f'{index} {each}')
...
0 arista
1 juniper
2 cisco
```

Maybe you don’t need to print all indices and values. Maybe you need only the index for a given vendor. This is shown in this example:

```
>>> for index, each in enumerate(vendors):
...     if each == 'arista':
...         print(f'arista index is: {index}')
...
arista index is:  0
```

### Flow control within loops

Loops can become a trap. In the *enumerate* example, you started and completed a full iteration over the objects in `vendors`, even though you were interested in only the ones matching `arista`. In that case, this was not a big issue because the list had three items. But, what if `vendors` had thousands of elements? Should you continue iterating over the list when you have already found the item you were looking for?

Luckily, Python has a `break` statement to stop a loop iteration at any point—for example, when the purpose of the loop is fulfilled. In the following variation, you add a `print()` for each iteration and a `break` to stop the loop once you find `arista`, so you can see how the loop is stopped when a condition is met:

```
>>> vendors = ['arista', 'juniper', 'cisco']
>>>
>>> for index, each in enumerate(vendors):
...     print(index)
...     if each == 'arista':
...         print(f'arista index is: {index}')
...         break
...
0
arista index is: 0
```

Another useful statement is `continue`, to jump to the next iteration of the loop and skip any pending logic for the present iteration. In the next example, you use `continue` to achieve the same goal, printing the `arista` index:

```
>>> for index, each in enumerate(vendors):
...     print(index)
...     if each != 'arista':
...         continue
...     print(f'arista index is: {index}')
...
0
arista index is: 0
1
2
```

Obviously, in this case you are not *breaking* the loop (you are not using `break`), and you print all the *indexes* but not the strings. Using `continue` makes the code easy to read: adding a condition at the beginning of the iteration helps you understand whether it makes sense to continue with the iteration or to move to the next one.

We’ve covered quite a bit of Python so far, from data types to conditionals to loops. However, we still haven’t discussed how to efficiently reuse code via functions. This is what we cover next.

# Using Python Functions

Because you are reading this book, you probably at some point have heard of functions, but if not, don’t worry—​we have you covered! Functions are all about eliminating redundant and duplicate code and easily allowing for the reuse of code.

On a daily basis, network engineers are configuring VLANs over and over again. And they are likely proud of how fast they can enter the same CLI commands into a network device or switch over and over. Writing a script with functions eliminates writing the same code *over and over*.

Let’s assume you need to create a few VLANs across a set of switches. Based on a device from Cisco or Arista, the commands required may look something this:

```
vlan 10
  name USERS
vlan 20
  name VOICE
vlan 30
  name WLAN
```

Imagine you need to configure 10, 20, or 50 devices with the same VLANs! You likely would type in those six commands for as many devices as you have in your environment.

This is actually a perfect opportunity to create a function and write a small script. Since we haven’t covered scripts yet, we’ll still be working in the Python shell.

For our first example, you’ll start with a basic `print()` function and then come right back to the VLAN example:

```
>>> def print_vendor(net_vendor):
...     print(net_vendor)
...
>>>
>>> vendors = ['arista', 'juniper', 'cisco']
>>>
>>> for vendor in vendors:
...     print_vendor(vendor)
...
arista
juniper
cisco
```

Here, `print_vendor()` is a function that is created and *defined* using `def`. If you want to pass variables (parameters) into your function, you enclose them within parentheses next to the function name. This example is receiving one parameter and is referenced as `net_vendor` while in the function called `print_vendor()`. Like conditionals and loops, function declarations also end with a colon (`:`). Within the function, an indented code block has a single statement—​it simply prints the parameter being received.

Once the function is created, it is ready to be immediately used, even while in the Python interpreter.

For this first example, we looped through `vendors`. During each iteration of the loop, we passed the object, which is a string of the vendor’s name, to `print_vendor()`.

Notice that the variables have different names based on where they are being used, meaning that you are passing `vendor`, but it’s received and referenced as `net_vendor` from within the function. There is no requirement to have the variables use the same name within the function, although it’ll work just fine if you choose to do it that way.

Since you now understand how to create a basic function, let’s return to the VLAN example and create two functions to help automate VLAN provisioning; see Examples [6-2](#function-get-commands) and [6-3](#function-push-commands).

##### Example 6-2. `get_commands()` function

```
>>> def get_commands(vlan, name): 
...     commands = []
...     commands.append(f'vlan {vlan}')
...     commands.append(f'name {name}')
...     return commands           
...
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `get_commands()` function accepts two parameters: `vlan` indicates the VLAN ID, and `name` indicates the name.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Returns a list of commands crafted from the input arguments.

##### Example 6-3. `push_commands()` function

```
>>> def push_commands(device, commands):     
...     print(f'Connecting to device: {device}')
...     for cmd in commands:
...         print(f'Sending command: {cmd}') 
...
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This function also accepts two parameters: `device`, which is the device to send the commands to, and `commands`, which is the list of commands to send.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

In reality, the actual configuration push isn’t happening in this function, but rather it is printing commands to the terminal to simulate the command execution.

To use these functions, you need two things: a list of devices to configure and the list of VLANs to send. The list of devices to be configured is as follows:

```
>>> devices = ['switch1', 'switch2', 'switch3']
```

To create a single object to represent the VLANs, we have created a list of dictionaries. Each dictionary has two key-value pairs, one pair for the VLAN ID and one for the VLAN name:

```
>>> vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}]
```

As you may recall, Python provides more than one way to create a dictionary. Any of those options could have been used here.

In [Example 6-4](#using-get-push-commands), we use these functions. The following code loops through the `vlans` list. Remember that each element in `vlans` is a dictionary. For each element, or dictionary, the `id` and `name` are obtained by way of the `get()` method. There are two `print` statements, and then the first function, `get_commands()`, is called—`id` and `name` are parameters that get sent to the function, and then a list of commands is returned and assigned to `commands`.

##### Example 6-4. Using defined functions

```
>>> for vlan in vlans:                       
...     vid = vlan.get('id')
...     name = vlan.get('name')
...     print(f'CONFIGURING VLAN: {vid}')
...     commands = get_commands(vid, name)   
...     for device in devices:               
...         push_commands(device, commands)  
...         print()
...
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Combining two `for` loops, for `vlans` and `devices`, will provide full coverage of VLAN configuration per device.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Using the `get_commands()` function from before, we can obtain all the necessary commands per VLAN.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Once we have the commands for a given VLAN, they are executed on each device by looping through `devices`.

And this is the output generated:

```
CONFIGURING VLAN: 10
Connecting to device: switch1
Sending command: vlan 10
Sending command: name USERS

Connecting to device: switch2
Sending command: vlan 10
Sending command: name USERS

Connecting to device: switch3
Sending command: vlan 10
Sending command: name USERS

CONFIGURING VLAN: 20
Connecting to device: switch1
Sending command: vlan 20
Sending command: name VOICE

Connecting to device: switch2
Sending command: vlan 20
Sending command: name VOICE

Connecting to device: switch3
Sending command: vlan 20
Sending command: name VOICE

CONFIGURING VLAN: 30
Connecting to device: switch1
Sending command: vlan 30
Sending command: name WLAN

Connecting to device: switch2
Sending command: vlan 30
Sending command: name WLAN

Connecting to device: switch3
Sending command: vlan 30
Sending command: name WLAN
```

###### Tip

Remember, not all functions require parameters, and not all functions return a value.

In this output, you may notice that we pivoted on the VLANs instead of the devices, which resulted in tearing up and down several connections to the devices (one per VLAN). Swapping the `for` loops and pivoting on the devices could have reduced the number of necessary device connections by consolidating all the VLAN changes.

You should now have a basic understanding of creating and using functions, understanding how they are called and defined with and without parameters, and how it’s possible to call functions from within loops. Next, we cover how to read and write data from files in Python.

# Working with Files

This section shows you how to read and write data from files. Our focus is on presenting the basics so you’ll then be able to easily pick up other sources to continue learning about working with files.

## Reading from a File

For our example, a configuration snippet is located in the same directory from where you entered the Python interpreter. The file, named *vlans.cfg*, looks like this:

```
vlan 10
  name USERS
vlan 20
  name VOICE
vlan 30
  name WLAN
vlan 40
  name APP
vlan 50
  name WEB
vlan 60
  name DB
```

With just two lines in Python, you can *open* and *read* the file:

```
>>> vlans_file = open('vlans.cfg', 'r')
>>>
>>> vlans_file.read()
'vlan 10\n  name USERS\nvlan 20\n  name VOICE\nvlan 30\n
name WLAN\nvlan 40\n  name APP\nvlan 50\n  name WEB\nvlan 60\n
  name DB'
>>>
>>> vlans_file.close()
```

You read the full file as a complete `str` object by using the `read()` method for file objects.

The next example reads the file and stores each line as an element in a list by using the `readlines()` method for file objects:

```
>>> vlans_file = open('vlans.cfg', 'r')
>>>
>>> vlans_file.readlines()
['vlan 10\n', '  name USERS\n', 'vlan 20\n', '  name VOICE\n', 'vlan 30\n',
'  name WLAN\n', 'vlan 40\n', '  name APP\n', 'vlan 50\n', '  name WEB\n',
'vlan 60\n', '  name DB']
>>>
>>> vlans_file.close()
```

Let’s reopen the file, save the contents as a string, but then manipulate it in order to store the VLANs as a dictionary (similar to the way you used the `vlans` object in [Example 6-4](#using-get-push-commands)):

```
>>> vlans_file = open('vlans.cfg', 'r')
>>>
>>> vlans_text = vlans_file.read()
>>>
>>> vlans_list = vlans_text.splitlines()
>>>
>>> vlans_list
['vlan 10', '  name USERS', 'vlan 20', '  name VOICE', 'vlan 30',
'  name WLAN', 'vlan 40', '  name APP', 'vlan 50', '  name WEB',
'vlan 60', '  name DB']
```

The file is read, and the contents are stored as a string in `vlans_text`. A built-in method for strings called `splitlines()` is used to create a list; each element in the list is each line within the file. This new list is called `vlans_list` and has a length equal to the number of commands that were in the file.

Next, in [Example 6-5](#python-normalize), we normalize the raw text content into a list of dictionaries.

##### Example 6-5. Normalizing raw text into a list of dictionaries

```
>>> vlans = []
>>> for item in vlans_list:                         
...     if 'vlan' in item:
...         temp = {}                               
...         id = item.strip().strip('vlan').strip() 
...         temp['id'] = id
...     elif 'name' in item:
...         name = item.strip().strip('name').strip()
...         temp['name'] = name
...         vlans.append(temp)
...
>>>
>>> vlans
[{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}, {'id': '40', 'name': 'APP'},
{'id': '50', 'name': 'WEB'}, {'id': '60', 'name': 'DB'}]
>>>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Once the list is created, it is iterated over within a `for` loop. The variable `item` is used to represent each element in the list as it’s being iterated over. In the first iteration, `item` is `'vlan 10'`; in the second iteration, `item` is `'  name USERS'`; and so on.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Within the `for` loop, a list of dictionaries is ultimately created; each element in the list is a dictionary with two key-value pairs: `id` and `name`. We accomplish this by using a temporary dictionary called `temp`, adding both key-value pairs to it, and then appending it to the final list only after appending the VLAN name. Per the following note, `temp` is reinitialized *only* when it finds the next VLAN, so it’s assuming a certain order of the input data.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Notice how `strip()` is being used. We can use `strip()` to strip not only whitespace but also particular substrings within a string object. Additionally, we *chain* multiple methods together in a single Python statement. For example, with the value `'  name WEB'`, when `strip()` is first used, it returns `'name WEB'`. Then, we use `strip('name')`, which returns `' WEB'`, and then finally `strip()` to remove any whitespace that still remains to produce the final name of `'WEB'`.

###### Note

The previous example is not the only way to perform an operation for reading in VLANs. That example *assumes* a VLAN ID and name for every VLAN, which is usually not the case, but is done this way for conveying certain concepts. It initializes `temp` only when `VLAN` is found, and appends `temp` only after the “name” is added (this would not work if a name did not exist for every VLAN and is a good use case for using Python error handling using `try/except` statements, as we cover in [“Embracing Failure with try/except”](#python-exceptions)).

## Writing to a File

The next example shows how to write data to a file. The `vlans` object created in the previous example is used here too:

```
>>> vlans
[{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}, {'id': '40', 'name': 'APP'},
{'id': '50', 'name': 'WEB'}, {'id': '60', 'name': 'DB'}]
```

A few more VLANs are created before you try to write the VLANs to a new file:

```
>>> add_vlan = {'id': '70', 'name': 'MISC'}
>>> vlans.append(add_vlan)
>>>
>>> add_vlan = {'id': '80', 'name': 'HQ'}
>>> vlans.append(add_vlan)
>>>
>>> print(vlans)
[{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}, {'id': '40', 'name': 'APP'},
{'id': '50', 'name': 'WEB'}, {'id': '60', 'name': 'DB'},
{'id': '70', 'name': 'MISC'}, {'id': '80', 'name': 'HQ'}]
```

Eight VLANS are now in the `vlans` list. Let’s write them to a new file but keep the formatting the way it should be with proper spacing.

The first step is to open the new file. If the file doesn’t exist, which it doesn’t in our case, it’ll be created:

```
>>> write_file = open('vlans_new.cfg', 'w')
```

Once the file is open, you use the `get()` method again to extract the required VLAN values from each dictionary and then use the file method called `write()` to write the data to the file. Finally, you close the file:

```
>>> for vlan in vlans:
...     id = vlan.get('id')
...     name = vlan.get('name')
...     write_file.write(f'vlan {id}\n')
...     write_file.write(f'  name {name}\n')
...
>>>
>>> write_file.close()
```

You’ve created the *vlans_new.cfg* file and generated the following contents in the file:

```
$ cat vlans_new.cfg
vlan 10
  name USERS
vlan 20
  name VOICE
vlan 30
  name WLAN
vlan 40
  name APP
vlan 50
  name WEB
vlan 60
  name DB
vlan 70
  name MISC
vlan 80
  name HQ
```

As you start to use file objects more, you may see some interesting things happen. For example, you may forget to close a file, and wonder why there is no data in the file that you know should have data!

###### Note

By default, what you are writing with the `write()` method is held in a buffer and is written to the file only when the file is closed. This setting is configurable.

You can also use the `with` statement, a context manager, to help manage this process. A context manager is a Python object that defines a runtime context: what to do when entering it and what to do when exiting it. In this example, you see how the return object of the `open()` method is used as a context manager, so it closes the file when exiting the context *automatically*:

```
>>> with open('vlans_new.cfg', 'w') as write_file:
...     write_file.write('vlan 10\n')
...     write_file.write('  name TEST_VLAN\n')
...
```

###### Note

When you open a file with `open('vlans.cfg', 'r')`, two parameters are passed. The first is the name of the file, including the relative or absolute path of the file. The second is the *mode*, which is an optional argument, but if not included, defaults to read-only, which is the `r` mode. Other modes include `w`, which opens a file only for writing (if you’re using the name of a file that already exists, the contents are erased), `a` opens a file for appending, and `r+` opens a file for reading and writing. You can find more details in the [official Python docs](https://oreil.ly/_Zx55).

Since Python 3, the file’s content is handled as `bytes` and *encoded* to text with an implicit UTF-8 encoding. If you want to change the encoding type, you can use the named argument `encoding`:

```
>>> vlans_file = open('vlans.cfg', 'r', encoding='ascii')
```

Everything in this chapter thus far has been using the dynamic Python interpreter. This showed how powerful the interpreter is for writing and testing new methods, functions, or particular sections of your code. No matter how great the interpreter is, you still need to be able to write programs and scripts that can run as a standalone entity. This is exactly what we cover next.

# Creating Python Programs

Let’s take a look at how to build on what you’ve been doing in the Python shell and learn how to create and run a standalone Python script, or program. This section shows how to easily take what you’ve learned so far and create a script within just a few minutes.

###### Note

If you’re following along, feel free to use any text editor you are comfortable with, including, but not limited to vi, Vim, Sublime Text, Notepad++, or even a full-blown IDE, such as PyCharm or VS Code, as introduced in [Chapter 5](ch05.html#developmentenvironments).

Let’s look at a few examples.

## Creating a Basic Python Script

The first step is to create a new Python file that ends with the *.py* extension. From the Linux terminal, you can create a new file by typing **`touch net_script.py`** and opening it in your text editor. As expected, the file is completely empty.

The first script you’ll write simply prints text to the terminal. Add the following five lines of text to *net_script.py* to create a basic Python script:

```
#!/usr/bin/env python3

if __name__ == "__main__":
    print('^' * 30)
    print('HELLO NETWORK AUTOMATION!!!!!')
    print('^' * 30)
```

Now that the script is created, let’s execute it. To execute a Python script from the Linux terminal, you use the `python3` command. All you need to do is append the script name to the command as shown here:

```
$ python3 net_script.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
HELLO NETWORK AUTOMATION!!!!!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

And that’s it! If you were following along, you just created a Python script. You might have noticed that everything under the `if __name__ == "__main__":` statement is the same as if you were on the Python interpreter.

Now we’ll take a look at the two unique statements that are optional, but recommended, when you are writing Python scripts.

## Using Comments in Python

Python code is usually easy to read, even without adding extra *comments*. However, adding comments in your programs can sometimes help new developers jumping into the code (reviewing, fixing or extending it), or even you, when you’re coming back to your code after a while and don’t fully remember the original context.

This book isn’t about *clean code* best practices, but an accepted rule of thumb is that comments should be used to explain or clarify your intent when it is not obvious enough.

In Python you can use the # (known as a hashtag, number sign, or pound sign) for inline comments:

```
commands = []
# The order of the commands is relevant, do not change it
commands.append(f'vlan {vlan}')
# Due to the naming convention, the name of a vlan includes the vlan ID
commands.append(f'name {name}_{vlan}')
```

Python linters used to perform checks on the code can also act upon the text that comes after comments starting with `#`.

Now we’ll take a look at a special comment type, optional but recommended, when you are writing Python scripts, the shebang. We introduced the shebang in [Chapter 3](ch03.html#linux).

### Understanding the shebang

The *shebang* is the first line in the script: `#!/usr/bin/env python3`. This is a special and unique line for Python programs.

It is the only line of code, other than comments, that uses the `#` as the first character. The shebang needs to be the first line in a Python program when used.

The shebang instructs the system which Python interpreter to use to execute the program. Of course, this also assumes file permissions are correct for your program file (i.e., that the file is executable). If the shebang is not included, you must use the `python` keyword to execute the script, which you have in all our examples anyway.

For example, say you have the following script in *hello.py*:

```
if __name__ == "__main__":
    print('Hello Network Automation!')
```

You could execute the code by using the statement `$ python3 hello.py`, assuming the file was saved as *hello.py*. But you could not execute it using the statement `$ ./hello.py`. In order for the statement `$ ./hello.py` to be executed, you need to add the shebang to the program file because that’s how the system knows how to execute the script. Also, remember to add execute permissions to the file with `chmod +x hello.py`!

```
#!python3

if __name__ == "__main__":
    print('Hello Network Automation!')
```

The shebang as we have it, `python3`, defaults to using Python 3.8.12 on the system we’re using to write this book. We can check the exact Python version with `which python3`:

```
$ which python3
/usr/bin/python3
```

If your machine has different installations of Python, you can refer directly to the desired one in your shebang. For instance, using `#!/usr/bin/python3.9` will use the Python 3.9 executable. However, this approach has the drawback of being inflexible (for instance, this will cause problems in Virtualenv, covered in [“Isolating Your Dependencies with Virtualenv”](#virtualenv)).

A better approach is to use `/usr/bin/env python3`, which allows the external environment to influence the specific installation your script uses.

Now that you understand the shebang, we can continue to present another optional statement that will open the door to start creating your first Python scripts.

## Migrating Code from the Python Interpreter to a Python Script

A common component of a Python script is the `if __name__ == "__main__":` statement. Based on the quotes, or lack thereof, you can see that `__name__` is a variable, and `"__main__"` is a string. When a Python file is executed as a standalone script, the variable name `__name__` is automatically set to `"__main__"`. Thus, whenever you use `python3 script.py`, everything underneath the `if __name__ == "__main__":` statement is executed.

At this point, you are probably thinking, when wouldn’t `__name__` be equal to `"__main__"`? That is discussed in [“Working with Python Modules”](#working-with-python-modules), but here’s the short answer: when you are importing particular objects from Python files, but not necessarily using those files as a standalone program.

In [Example 6-6](#push-script), we use the same Python script as in [“Using Python Functions”](#using-python-functions). The reason is to show you firsthand how easy it is to migrate from using the Python interpreter to writing a standalone Python script.

##### Example 6-6. Script to render push commands

```
#!/usr/bin/env python3               

def get_commands(vlan, name):        
    commands = []
    commands.append(f'vlan {vlan}')
    commands.append(f'name {name}')
    return commands

def push_commands(device, commands): 
    print(f'Connecting to device: {device}')
    for cmd in commands:
        print(f'Sending command: {cmd}')

if __name__ == "__main__":           

    devices = ['switch1', 'switch2', 'switch3']

    vlans = [
        {'id': '10', 'name': 'USERS'},
        {'id': '20', 'name': 'VOICE'},
        {'id': '30', 'name': 'WLAN'}
    ]

    for vlan in vlans:               
        vid = vlan.get('id')
        name = vlan.get('name')
        print(f'CONFIGURING VLAN: {vid}')
        commands = get_commands(vid, name)
        for device in devices:
            push_commands(device, commands)
            print()
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The shebang instructs the system about the Python interpreter to use.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The functions are defined before using them.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `if` statement indicates to run this code when it’s executed as a script instead of being imported.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The same nested `for` loop defined in [Example 6-4](#using-get-push-commands) is executed.

You can execute this script with the commands `python3 push.py` or `./push.py`. The output you see is exactly the same output you saw when it was executed on the Python interpreter in [Example 6-4](#using-get-push-commands).

###### Tip

Python offers the `-i` flag to be used when executing a script, but instead of exiting the script, it enters the interpreter, giving you access to all the objects built in the script. This is *great* for testing.

Let’s see what happens when you run the script with the `-i` flag set:

```
$ python3 -i push.py
>>>
>>> print(devices)
['switch1', 'switch2', 'switch3']
>>>
>>> print(commands)
['vlan 30', 'name WLAN']
```

Notice that it executes, but then drops you right into the Python shells and you have access to those objects at the end of the execution. Pretty cool, right?

If you are creating several scripts that perform various configuration changes on the network, you can intelligently assume that the `push_commands()` function will be needed in almost all scripts. One option is to copy and paste the function into all the scripts. Clearly, that would not be optimal because if you need to fix a bug in that function, you would need to make that change in *all* the scripts.

Just as functions allow you to reuse code within a single script, Python provides a way to reuse and share code among scripts/programs. You do so by creating a Python module, which is what we cover next as we continue to build on the previous example.

# Working with Python Modules

We are going to continue to leverage the *push.py* file we just created in the previous section to better articulate how to work with a Python module. You can think of a *module* as a type of Python file that holds information, (e.g., Python objects), that can be used by other Python programs but is not a standalone script or program itself.

For this example, you are going to enter back into the Python interpreter while in the same directory where the *push.py* file exists.

Let’s assume you need to generate a new list of commands to send to a new list of devices. Remember that you have this function called `push_commands()` in another file that already has the logic to push a list of commands to a given device. Rather than re-create the same function in your new program (or in the interpreter), you can reuse `push_commands()` from within *push.py*. Let’s see how to do it.

While at the Python shell, you type in `import push` and hit Enter. This imports all the objects within the *push.py* file:

```
>>> import push
```

Take a look at the imported objects by using `dir(push)`:

```
>>> dir(push)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'get_commands', 'push_commands']
```

Just as with the standard Python data types, `push` has methods that start and end with underscores (dunders), but you should also notice the two objects called `get_ ​com⁠mands` and `push_commands`, which are the functions from the *push.py* file!

As you may recall, `push_commands()` requires two parameters. The first is a device, and the second is a list of commands. Let’s now use `push_commands()` from the interpreter:

```
>>> device = 'router1'
>>> commands = ['interface Eth1/1', 'shutdown']
>>>
>>> push.push_commands(device, commands)
Connecting to device: router1
Sending command: interface Eth1/1
Sending command: shutdown
```

If you import multiple modules, there could be objects with duplicated names. Using `import push` is definitely a good option because it enables you to specify the module where the object exists (i.e., `push.push_commands`). On the other hand, there are other options for importing objects.

One other option is to use `from import`. In our example, it would look like this: `from push import push_commands`. Notice in the following code, you can directly use `push_commands()` without referencing `push`:

```
>>> from push import push_commands
>>>
>>> push_commands(device, commands)
Connecting to device: router1
Sending command: interface Eth1/1
Sending command: shutdown
```

###### Tip

We recommend making `import` statements as specific as possible and to import only what’s used in your code. You should *not* use wildcard imports, such as `from push import *`. Statements like this load all objects from the module, potentially overloading and causing namespace conflicts with objects you’ve defined. And it also complicates troubleshooting, as it makes it difficult to decipher where an object was defined or came from.

Another option is to rename the object as you are importing it, using `from import as`. If you happen to not like the name of the object or think it is too long, you can rename it on import. The code looks like this for our example:

```
>>> from push import push_commands as pc
>>>
>>> pc(device, commands)
Connecting to device: router1
Sending command: interface Eth1/1
Sending command: shutdown
```

Notice how easy it is to rename the object and make it something shorter and/or more intuitive.

Reusing functions is great, but it implies that the consumer of the code may not know the concrete purpose, or usage, of the imported function. To make reusability easier, the next step is to learn how to document your functions.

## Documenting Functions

When you create functions that will be used by others, it’s helpful to document how your function should be used. In Python, you can add *docstrings* to describe functions, methods, and classes; you use triple quotes (`"""`) to define a docstring, and you can document the expected arguments and what the function returns:

```
def get_commands(vlan, name):
    """Get commands to configure a VLAN.

    Args:
        vlan (int): vlan id
        name (str): name of the vlan

    Returns:
        List of commands is returned.
    """

    commands = []
    commands.append(f'vlan {vlan}')
    commands.append(f'name {name}')
    return commands
```

You learned how to import a module—namely, *push.py*. Let’s import it again now to see what happens when you use `help` on `get_commands()` since you now have a docstring configured. You see the whole function’s *docstring* when you use `help()`. Additionally, you see information about the parameters and what data is returned, if properly documented:

```
>>> import push
>>>
>>> help(push.get_commands)

Help on function get_commands in module push:

get_commands(vlan, name)
    Get commands to configure a VLAN.

    Args:
        vlan (int): vlan id
        name (str): name of the vlan

    Returns:
        List of commands is returned.
(END)
```

###### Tip

Some code editors provide contextual help to automatically render the docstring information when you are typing a function name.

By now you should understand how to create not only a script, but also a Python module with functions (and other objects), and how to use those reusable objects in other scripts and programs.

# Passing Arguments into a Python Script

The preceding two sections covered writing Python scripts and using Python modules. The `sys` module is part of the Python standard library (i.e., comes with Python by default), and now you will see how it allows you to easily pass in arguments from the command line into a Python script. Specifically, you’re going to use an attribute (or variable) within the module called `argv`.

Let’s take a look at a basic script called *send_command.py* that has only a single `print` statement:

```
#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print(sys.argv)
```

###### Warning

`sys.args` is available only when running a Python script. It doesn’t exist in the Python interpreter.

Now you’ll execute the script, passing in a few arguments simulating data required to log in to a device and issue a `show` command:

```
ubuntu2004:~$ python3 send_command.py username password 10.1.10.10 "show version"
['send_command.py', 'username', 'password', '10.1.10.10', 'show version']
```

You can see that `sys.argv` is a list. In fact, it’s simply a list of the strings that you passed in from the Linux command line. You can also infer what really happened: Python did a split (`str.split(" ")`) on `send-command.py username password 10.1.10.10 "show version"`, which created the list of five elements!

Finally, note that when you’re using `sys.argv`, the first element is always the script name.

If you’d like, you can assign the value of `sys.argv` to an arbitrary variable to simplify working with the parameters passed in. In either case, you can extract values by using the appropriate index values as shown:

```
#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    args = sys.argv
    print(f"Username:  {args[1]}")
    print(f"Password:  {args[2]}")
    print(f"Device IP: {args[3]}")
    print(f"Command:   {args[4]}")
```

If you execute this script, you get the following output:

```
$ python3 send_command.py username password 10.1.10.10 "show version"
Username:  username
Password:  password
Device IP: 10.1.10.10
Command:   show version
```

###### Warning

When using `sys.argv`, you still need to account for input error handling (at a minimum, check the length of the list). Additionally, the user of the script must know the precise order of the elements that need to be passed in.

In our example, if you call the script with fewer than the four expected arguments, you will hit an `IndexError` because you are accessing an index in a list that doesn’t exist:

```
$ python3 send_command.py
Traceback (most recent call last):
  File "/your/path/examples/ch06-python/send_command.py",
   line 8, in <module> print(f"Username:  {args[1]}")
IndexError: list index out of range
```

For more advanced argument handling, you should look at the Python module `argparse`, which offers a user-intuitive way of passing in arguments with flags and a built-in help menu. This is beyond the scope of this book.

You can build on this to perform more meaningful network tasks as you continue reading this book. For example, after reading [Chapter 10](ch10.html#apis), you’ll be able to pass parameters like this into a script that actually connects to a device and issues a `show` command (or equivalent).

# Using pip and Installing Python Packages

As you get started with Python, you’ll likely need to install third-party software. For example, you may want to automate network devices with Netmiko, a popular SSH client for Python that we cover in [Chapter 10](ch10.html#apis). The most common way to distribute Python software, including Netmiko, is the Python Package Index (PyPI), pronounced “pie-pie.” You can also browse and search the PyPI repository directly at [*https://pypi.python.org/pypi*](https://pypi.python.org/pypi).

###### Warning

`pip`, by default, installs the packages in the system. We strongly recommend using virtual environments to isolate your Python package installations. This topic is introduced next in [“Isolating Your Dependencies with Virtualenv”](#virtualenv).

You can use the `pip` program to install any software that’s hosted on PyPI (such as Netmiko) to your machine directly from PyPI. The `pip` installer by default goes to PyPI, downloads the software, and installs it on your machine.

###### Note

`pip3`, an updated version of the original `pip` from Python 2, installs packages for Python 3+. Even though `pip` as a soft link could be also pointing to `pip3`, to avoid ambiguity, we use `pip3` consistently in this book.

Using `pip3` to install Netmiko can be done with a single line on your Linux machine:

```
ubuntu2004:~$ pip3 install netmiko
# output has been omitted
```

By default, this command will install the latest (stable release) of a given Python package in a system path (the path will vary based on the OS). However, you may want to ensure that you install a specific version—​this is helpful so you don’t automatically install the next release without testing. This is referred to as *pinning*: you can *pin* your install to a specific release. In the next example, we show how you can pin the installation of Netmiko to version 3.4.0:

```
ubuntu2004:~$ pip3 install netmiko==3.4.0
# output has been omitted
```

You can use `pip3` to upgrade versions of the software too. For example, you may have installed version 3.4.0 of Netmiko and when a new release is available, you can upgrade to the latest release by using the `--upgrade` or `-U` flag on the command line:

```
ubuntu2004:~$ pip3 install netmiko --upgrade
# output has been omitted
```

It’s also common to install Python packages from *source*. That means getting a specific version from the source code (not released to PyPI)—for example, from GitHub, a version control system that we cover in [Chapter 11](ch11.html#sourcecontrol). Perhaps the code under development in GitHub has a bug fix you need, but it hasn’t been published.

When you get the source code of a Python project, there is a good chance you’ll see two files in the root of the project: *requirements.txt* and *setup.py*. You can use these to install the Python package from source. The requirements file lists the requirements needed for the application to run. For example, here is the current *requirements.txt* for Netmiko:

```
paramiko>=2.0.0
scp>=0.10.0
pyyaml
pyserial
textfsm
```

You can see that Netmiko has five dependencies, commonly referred to as *deps*. You can also install these deps directly from PyPI by using a single statement:

```
ubuntu2004:~$ pip3 install -r requirements.txt
# output has been omitted
```

To completely install Netmiko (from source) including the requirements, you can also execute the *setup.py* file that you’d see in the same source code directory:

```
ubuntu2004:~$ python3 setup.py install
# output has been omitted
```

By default, installing the software with *setup.py* will also install directly into a system path. If you want to contribute back to a given project and actively develop the project, you can also install the application directly from where the files exist and are being developed:

```
ubuntu2004:~$ python3 setup.py develop
# output has been omitted
```

This makes it such that the files in your local directory are the ones running Netmiko. Otherwise, with the `install` option, you’ll need to modify the files in your system path to affect the Netmiko install (for example, when troubleshooting an external library).

###### Tip

There is an even easier way to install a Python project from the source code without cloning the repository locally. This approach is especially useful when you don’t need to develop code but just use a specific version, from a branch or a commit (see [Chapter 11](ch11.html#sourcecontrol) for details). To target a specific branch, you can append `@develop` after the repository URL. The name of the branch is `develop`, but you could point to a specific commit or tag. This is particularly useful when the library is still not released to PyPI or when you want to use a feature that hasn’t been released yet:

```
ubuntu2004:~$ pip3 install \
    git+https://github.com/ktbyers/netmiko.git@develop
# output has been omitted
```

## Isolating Your Dependencies with Virtualenv

By default, `pip3` installs the packages into your global Python environment. This works well for single-purpose applications (such as a container running one process), but your local development environment is going to become a nightmare sooner rather than later.

For example, when you work on your first Python project, say you install a specific version of an external library. Then a new project comes up, and one of its dependencies depends on exactly the same library you already have, but on a different version. Because `pip3` installs the libraries globally, you have a problem.

But don’t worry; Python offers you a solution by creating *virtual environments*, or *virtualenvs*. These isolated Python environments live inside a folder, with all the dependencies of a specific project. This *folder* could be placed wherever you prefer, and one common option is to put it directly in each project folder with the name *.venv*.

To create a new Python virtualenv, you use `python3 -m venv`, followed by the folder name. This command creates a brand-new Python environment in this folder, where the packages will be installed:

```
ubuntu2004:~$ python3 -m venv .venv
ubuntu2004:~$ ls .venv
bin  include  lib  lib64  pyvenv.cfg
```

But so far, you have created only the virtualenv, and you are still not using it because it’s not *active*. The next step is to activate it. Run `source` on `bin/activate` within the virtualenv, and you will see how the *path* changes to `(.venv)`, the name of your virtualenv, indicating that now the Python environment is not the global one but the one that has been activated. Now, if you check your Python binary path, it points to the one within the *.venv* folder:

```
ubuntu2004:~$ source .venv/bin/activate
(.venv) ubuntu2004:~$
(.venv) ubuntu2004:~$ which python
/home/ntc/.venv/bin/python
```

Do you remember installing Netmiko before? If you check the installed packages within the virtualenv, you won’t find it! Similarly, anything you install while the virtualenv is activated is kept only on this virtualenv and won’t affect the global environment or other virtualenvs:

```
(.venv) ubuntu2004:~$ pip3 list
Package    Version
---------- -------
pip        21.2.4
setuptools 57.5.0
wheel      0.37.1
```

Finally, you can go back to the global mode simply by *deactivating* the virtualenv:

```
(.venv) ubuntu2004:~$ deactivate
ubuntu2004:~$ which python
/usr/bin/python
```

###### Tip

Python has several packages (Pipenv, Poetry, and others) that can help you with dependency management, installation, and packaging. We strongly recommend you give them a try; they are really helpful!

As a best practice, keep every Python project in a different virtual environment. This approach will make your life much easier because you will avoid the pain of inconsistent package versions, inherited from each project’s direct package dependencies.

Now that you have learned about installing and importing others’ code, and have explored the Python built-in data types in [“Understanding Python Data Types”](#python-data-types), the next stop is to understand how to define your own data types: *classes*.

# Understanding Python Classes

A *class*, in a programming language, contains *data* (attributes) and *procedures* (methods) that are related to its data. A class is one of the key abstractions that enable object-oriented programming (OOP) in Python (and similarly in other programming languages). OOP is about modeling real-world entities and how they interact; used correctly, OOP can make your code more readable, maintainable, and even more testable.

But, before going into defining your classes, you need to understand how to use others’ defined classes.

## Using Classes

To get access to classes from other modules, you use the same `import` statement you used to import functions in [“Working with Python Modules”](#working-with-python-modules). Here, you import the class `Device` from your package `vendors.cisco.device` (from within the *ch6-python* directory):

```
>>> from vendors.cisco.device import Device
```

Classes are just abstract representations of an object. However, to create a specific instance of an object, you must *instantiate* the class. This looks similar to the way you call functions, and you can think of this syntax as calling a function that returns an instance of the class.

Then you can instantiate an instance of the `Device` class and get a `Device` object. As with functions, you pass some arguments, which are used to *construct* the instance. When you instantiate a class, you are actually calling the `__init__()` method, known as the *constructor*. The following snippet describes how to create three objects from the `Device` class and save them in different variables:

```
>>> switch1 = Device(ip='10.1.1.1', username='cisco', password='cisco')
>>> switch2 = Device(ip='10.1.1.2', username='cisco', password='cisco')
>>> switch3 = Device(ip='10.1.1.3', username='cisco', password='cisco')
```

Notice that each variable is a separate instance of `Device`:

```
>>> type(switch1)
<class 'vendors.cisco.device.Device'>
```

Once the class object is initialized, you can start using its *methods*. This is just like using the built-in methods for the data types you learned about earlier in the chapter. The syntax is *`class_object.method`*:

```
>>> switch1.show('show version')
```

###### Tip

As a reminder, using method objects of a class is just like using the methods of the data types such as strings, lists, and dictionaries.

If you execute `show` for `switch2` and `switch3`, you would get the proper return data back from each device as expected, since each object is a different instance of `Device`, and the `show()` method will use the connection data from each instance.

Now that you understand how to use classes, let’s create your first class!

## Building Your Own Classes

In the previous section, we introduced two main elements you need to define when building your own class:

- The *constructor* method (`__init__()`) to initialize the instance data (attributes)
- The methods that the objects of this class will expose

Taking as a reference the example from [“Using Classes”](#using-classes), [Example 6-7](#build-class) implements the `Device` class, starting with the `__init__()` method.

##### Example 6-7. Building a class

```
>>> class Device:
...     def __init__(self, ip, username, password):
...         self.host_ip = ip
...         self.user = username
...         self.pswd = password
...
>>> router = Device(ip='192.0.2.1', username='abc', password='123')
>>>
>>> router.host_ip
'192.0.2.1'
>>>
>>> router.__dict__
{'host_ip': '192.0.2.1', 'user': 'abc', 'pswd': '123'}
```

With the `class` statement, you start the class definition (by convention, starting with a capital letter, but that’s not mandatory).

And right after it, you define the `__init__()` constructor method (with `def`). Remember that this method is a dunder that will be called, magically, when the class is instantiated via `Device()`, returning an actual instance object. This newly created object is referenced, within the method definition, by `self`. As you build more class methods, you will use `self` to represent the instance of the class. However, `self` is a convention, not an actual Python keyword. It is simply the first argument a class method takes. In [Example 6-7](#build-class), the `__init__()` method stores only input arguments into object attributes, but this method could contain a more complex logic.

After the class definition, you instantiate it and assign it to the `router` variable, and then you access the data from one of its attributes with `router.host_ip`, similar to the way you would call the methods that will expose later, but without the parentheses.

Last, you access a hidden attribute, `__dict__`, that returns a default conversion of all attributes as a dictionary. This could look like magic now because you have not explicitly defined it, but you will understand when we explain *inheritance* in [Example 6-9](#extend-class).

Defining class methods is pretty similar to defining functions, but with the context reference to `self` that points to the instance object created when the class is instantiated. See [Example 6-8](#adding-method-class).

##### Example 6-8. Adding a method to a class

```
>>> class Device:
...     def __init__(self, ip, username, password):
...         # omitted for brevity
...
...     def show(self, command):                           
...         return f'{command} output from {self.host_ip}' 
...
>>> router = Device(ip='192.0.2.1', username='abc', password='123')
>>>
>>> router.show('show version')
'show version output from 192.0.2.1'
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `show()` method, in the `Device` class, returns a string, combining an internal class attribute, `self.host_ip`, and a method argument, `command`.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Class methods have access to the class instance object, via the first argument (usually named `self`).

Sometimes you don’t need to completely create a brand-new class only to add a new attribute or a new method. In these cases, it’s wiser to *extend* a class via *inheritance*. We will not go deep on this topic, but [Example 6-9](#extend-class) shows how simple is to extend a class for your convenience while keeping the definition (attributes and methods) from the *parent* class.

##### Example 6-9. Extending a class

```
>>> class Router(Device):                                           
...     def disable_routing(self):                                  
...         return f'Routing is disabled for {self.host_ip}'
...
>>>
>>> router = Router(ip='192.0.2.1', username='abc', password='123') 
>>>
>>> router.show('show version')                                     
'show version output from 192.0.2.1'
>>>
>>> router.disable_routing()
'Routing is disabled for 192.0.2.1'
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We define the new class `Router` as in [Example 6-7](#build-class), but taking the argument `Device`. At this point, `Router` is a copy of the original `Device` class, with a different name.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

After inheriting from a parent class, we can add new methods, as we do with `def disable_routing(self)`, or we can add other class attributes. Similarly as we add a new method, we can overwrite a previously existing one by redefining it in the child class.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The initialization of the `router` object (`router = Router(...)`) is exactly the same as in [Example 6-8](#adding-method-class), even though we have not defined a new `__init__()` method.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The methods from the parent class are still available for the child objects.

Moreover, when an object is created from a class that inherits from another class, the object *belongs* to all the classes. In our example, `router` is, at the same time, a `Device` and a `Router`, as you can check with the `isinstance()` function:

```
>>> isinstance(router, Router)
True
>>> isinstance(router, Device)
True
```

We have barely touched the surface of Python classes, giving you the basics to start using OOP in your programs. Next, you will learn how to make your code execution more robust.

# Embracing Failure with try/except

When you write code, you try to build it to provide a seamless execution, without flow execution crashes. However, as the code grows in complexity, guaranteeing an execution without errors becomes a big challenge because of the multiple cases to cover.

Every programming language provides a pattern or mechanism to facilitate error handling. In Python, error handling is built around exceptions (you’ve already seen some of them, such as `KeyError`, in previous code examples) and the try/except block.

Functions and methods communicate that something special has happened via *raising* an *exception*. Python has a `raise` statement to enable your code to signal to the caller of the function that a specific event has happened. Usually, this event is something wrong and must be handled by the caller, but its meaning is not necessarily negative.

From the caller’s perspective, you can use the try/except block to handle exceptions. The *try* block is where the code is executed and exceptions may be raised, and the *except* captures specific exceptions, in order to handle them appropriately.

When exploring the dictionaries access, you saw that a `KeyError` exception is raised when you access a *key* that doesn’t exist. Now let’s try to not break the execution using the try/except block:

```
>>> device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
>>>
>>> device["random_key"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'random_key'
```

Here, when you access `random_key` without the try/except block, a `Traceback` is printed. This report contains *where* and *how* your code failed and broke the execution, and is useful to diagnose the issue and debug your code. To better understand the `Traceback` content, we should read it from the bottom up:

KeyErrorException name raised.

'random_key'The error message—in this case, the key that you are accessing.

File "<stdin>", line 1, in <module>Calls involved, pointing out to the file and the line of code. In this case, because we are using interactive mode, `stdin` is shown.

Now, using the try/except block, you make your code ready to handle the `KeyError` exception gracefully, simply printing a message and resuming the code execution:

```
>>> try:
...     device["random_key"]
... except KeyError:
...     print('The key is not present')
...
The key is not present
```

Python has a built-in class `Exception` that is the parent of all the other exceptions. Indeed, the `KeyError` exception inherits from `Exception`. Thus, you can use `Exception` as a wildcard to catch *all* Python exceptions and protect your code execution against any unexpected failure. However, use this with caution because it could mask real programming errors.

`Exception` is yet another class, with certain dunders that make it *special*. All you learned about classes still applies here, so you can create your own *exceptions* from the base `Exception` class, overwriting methods or adding extra attributes, and catch them in *try/except* blocks. When you build a Python library, the exception classes have a relevant role too, besides the other functions and classes you expose.

Before closing this chapter, we want to explain a slightly more advanced concept to introduce you to a new programming paradigm: parallel code execution.

# Parallelizing Your Python Programs

By default, Python programs follow a *serial* execution pattern. Starting from an entry point, your code is executed one task after another, so the second task doesn’t start until the previous task is completed. This is not a problem when you have a small program or when the time spent on each task is not significant. But what if one task takes too long, simply waiting for an external process to complete? Should your precious CPU stay empty until you get the response? Or, having multiple CPU cores, why not distribute processing load across them, instead of leaving them on the bench?

The solution to this challenge is performing multiple operations at the same time. [Figure 6-1](#serial-parallel-execution) illustrates the difference between running your code tasks in serial or running them in parallel.

![npa2 0601](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0601.png)

###### Figure 6-1. Serial versus parallel execution

The most common network automation use cases, interacting with APIs or remote network devices, are *I/O-bound* operations (entering a *blocking* state when waiting for the input/output data). To parallelize these operations, you can use threads. A *thread* is a separate flow of execution that runs at *the same time*.

Python supports multiple implementation options for parallelization. We don’t cover all of them, but use the `ThreadPoolExecutor` utility to exemplify the idea.

###### Note

For *CPU-bound* operations, where it’s necessary to spread the load over multiple processes (instead of multiple threads on the same process), you can use `ProcessPoolExecutor`, similarly to using `ThreadPoolExecutor` here.

First, you *simulate* a long-standing I/O task adding a *blocking* call, `time.sleep(5)`, in the `get_commands()` function, the same function defined in [Example 6-2](#function-get-commands):

```
>>> import time
>>>
>>> def get_commands(vlan, name):
...     time.sleep(5)
...     commands = []
...     commands.append(f'vlan {vlan}')
...     commands.append(f'name {name}')
...     return commands
...
```

As expected, in [Example 6-10](#serial-execution), if we execute the `get_commands()` function in a three-iteration loop, the total execution time is 15 seconds, because each function is called when the previous ends in a serial way.

##### Example 6-10. Serial execution

```
>>> def run_task(vlans):                                         
...     start_time = time.time()
...     for vlan in vlans:
...         result = get_commands(vlan=vlan['id'], name=vlan['name'])
...         print(result)
...     print(f'Time spent: {time.time() - start_time} seconds') 
...
>>> vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}]
>>>
>>> run_task(vlans)
['vlan 10', 'name USERS']
['vlan 20', 'name VOICE']
['vlan 30', 'name WLAN']
Time spent: 15.008316278457642 seconds
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Wraps the loop into a `run_task()` function.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Prints the time spent subtracting the initial and final time, using the `time.time()` function, which returns the time in seconds since the epoch.

Now, in [Example 6-11](#parallel-threadpoolexecutor), using `ThreadPoolExecutor`, the overall time spent is only 5 seconds instead of 15 seconds because the three tasks are executed concurrently. Imagine what this means when you have to execute a 30-second operation for hundreds of devices. Even though the code may look a bit overwhelming in the beginning, we hope this sounds appealing to you.

##### Example 6-11. Parallel execution

```
>>> import concurrent.futures
>>>
>>> with concurrent.futures.ThreadPoolExecutor() as executor: 
...     start_time = time.time()
...     tasks = []
...     for vlan in vlans:                                    
...         tasks.append(
...             executor.submit(
...                 get_commands, vlan=vlan['id'], name=vlan['name']
...             )
...         )
...     for task in concurrent.futures.as_completed(tasks):   
...         print(task.result())
...     print(f'Time spent: {time.time() - start_time} seconds')
...
['vlan 10', 'name USERS']
['vlan 20', 'name VOICE']
['vlan 30', 'name WLAN']
Time spent: 5.001068830490112 seconds
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We introduce the `ThreadPoolExecutor` class, imported from `concur⁠rent​.futures`, to implement concurrency running the same `get_commands()` function. We use it as a context manager with the `executor` variable, automatically cleaning up threads upon completion.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The first loop appends *future* tasks (using the `executor`).

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The second iterates over these tasks, getting the results when completed.

This example helps illustrate the potential of using parallelization in Python. Getting into the details of this code, or exploring other options, such as asyncio, are beyond the scope of this book.

However, this paradigm introduces some collateral effects that must be taken into account when building your code:

- When running code in parallel, by default, you don’t control the ending order of the tasks. If your task’s execution has dependencies, some kind of coordination will be needed (for instance, using *semaphores*).
- Depending on the parallelization approach, your functions may need to be rewritten, slightly. For instance, you might need to adopt asynchronous behavior when using the `async/await` pattern.
- Multiple tasks accessing the same memory object could cause data inconsistency. For instance, two tasks could update the value of the same variable at the exact same time. This can be solved using a *locking* mechanism, preventing concurrent access.
- Increasing the number of parallel tasks, and running concurrent connections, could overload the target endpoint if it’s not ready to handle so many sessions. A good approach is to check the concurrency impact in the target endpoint, progressively, so as to not completely knock it down.

Despite the previous considerations, running code in parallel, with the appropriate design, can save a lot of time. With this last superpower, we end the Python chapter, where you have hopefully gained the basic knowledge to start building your Python applications.

Now, you are ready to start programming your first Python program, and as a bonus point, we give you a simple trick to learn more about Python’s design philosophy. Try `import this` and see what happens!

# Summary

This chapter provided a grassroots introduction to Python for network engineers. We covered foundational concepts such as working with data types, conditionals, loops, functions, and files, and even how to create a Python module that allows you to reuse the same code in different Python programs/scripts. We also got into more advanced topics such as classes and error handling, ending with a quick glance at parallel execution. All these topics should help you as a reference as you continue on with your Python and network automation journey.

In [Chapter 8](ch08.html#dataformats), we introduce you to data formats such as YAML, JSON, and XML, and in that process, we also build on the content in this chapter. For example, you’ll take what you learned and start to use Python modules to simplify the process of working with these data types, and also see the direct correlation among YAML, JSON, and Python dictionaries.

But Python is not the only programming language used in network automation. Next, in [Chapter 7](ch07.html#go), you will learn about another popular programming language for automation (Go), and you will start noticing commonalities and differences.
