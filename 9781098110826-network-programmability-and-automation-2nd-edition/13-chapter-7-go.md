# Chapter 7. Go

Earlier editions of this book covered a wide variety of tools and techniques within the world of network automation. Even at that time (when automation was still largely considered to be a nascent discipline), a multitude of tools existed to address the most common use cases. However, an alternative approach has always existed for use cases where those tools aren’t sufficient on their own. Given Python’s popularity and approachability, including a chapter focusing on that language makes sense. With this knowledge, network automation professionals always have the option of writing custom Python scripts to fill in any gaps in the existing ecosystem, should the existing tools prove insufficient on their own.

However, Python is no longer the only kid on the block. These days, another programming language can often be found in network automation initiatives of any scale: Go. Initially designed by Google in 2007, Go is used today by thousands of companies around the world. According to the [2021 Go Developer Survey](https://oreil.ly/-Y_PE), 76% of respondents use Go at work. As might be expected, this includes a healthy percentage of technology-focused companies, but also includes industries like healthcare, retail, and manufacturing. Among many others, nearly 40% of respondents said they use Go for automation or scripting use cases. Clearly, something powerful in this relatively young language warrants a closer look for our purposes in the world of network automation.

Before we dig into Go, you should be aware of three significant industry trends, which will help place this chapter in the appropriate context:

Maturity of discipline and demand for specialized skillsDespite the explosion of additional tools, demand for programming skills in network automation has *increased*, not decreased. This is not entirely unexpected: as the discipline matures, and the common, shared problems are solved by canned tooling, we move up the stack and require more specialized tools that are unique to our individual organizations/environments. Because of this, we also have a much more well-understood set of requirements for what we need our languages and tools to be able to provide.

Cloud nativeGo has an incredibly strong foothold in the area of cloud native technologies. Just as the server virtualization movement in the early 2010s had an immense influence and demand on increasing network agility (which eventually led to SDN), so too is the cloud native movement now having a profound impact on the techniques and technologies that network engineers must use to keep up. More than any other language, Go is the number one choice for integrating modern application infrastructure with the network automation discipline.

Growing communityJust as the proliferation of libraries and general support for Go has exploded because of the cloud native movement, the last few years in particular have seen a surge of tools, libraries, and training materials focused on using Go for network automation. While Python is still the undisputed leader here because of its extensive, mature network automation ecosystem, the network automation community around Go has grown substantially and has made significant strides toward closing that gap.

These factors have led us to add this chapter to the book. We’ll introduce you to Go and its application to network automation. We will, of course, explore each of these factors in the sections to follow. This will provide you with a potentially complementary alternative to Python, for those times when a custom solution is required.

As with the Python chapter, it’s impossible to cover everything you need to know about Go in a single chapter. There’s a reason programming languages dedicate entire books to even the most introductory concepts. We cover the basics using a few relevant examples so that by the end of this chapter you’ll have a solid foundation, but consider this a starting point of your journey; in fact, we cover a few great next-steps at the end of this chapter. Along the way, we highlight some of Go’s unique strengths so that you’ll have a better understanding of when it might suit your purposes.

# Why Go?

With Python dominating the network automation space, you might be wondering, why learn another programming language? Why specifically Go? To answer either question, we should first answer a more fundamental one: what requirements does the typical network automation professional have for any programming language? This is a question we as an industry haven’t had to contend with often, given that for many years, Python was our only practical choice. However, it’s an important one to consider these days; understanding these requirements will help us understand why the industry gravitated toward Python so strongly, and will enable us to identify other languages that may do the job as well, taking into account the unique strengths they may bring to the table.

We propose the following requirements:

Speed of developmentMost network engineers are not seasoned developers and don’t necessarily want to be (nor do their employers). The language must be simple enough that it’s easy to get to value and iterate quickly. This requirement has two subrequirements. First, the language should be easy to adopt; a newcomer must be able to adopt this new language and its patterns and become moderately productive with it within a week or two. Second, the language should have low maintenance overhead: the language has to be easy enough to work with and maintain so that when problems arise, we can solve them quickly and simply.

EcosystemAgain, we as network automators don’t have the time to write everything from scratch. We must rely on an established ecosystem of libraries and tools to build upon. The language we choose must have at least a growing community of others working with this language, publishing these kind of integrations and collaborating to improve the developer experience for everyone.

Operational stabilityThe code we write controls the network, which powers everything else in our organization—so our code has to be rock-solid. For example, some modern languages do quite a bit of heavy lifting here, through static type checking, race condition detection, and memory safety guarantees. The language we choose must have the necessary tools to create a stable service, while not violating the other requirements.

###### Note

No language is perfectly suited nor perfectly flawed when it comes to any of these requirements for network automation. Too much nuance exists to have an absolutist’s view. For instance, Python has multiple implementations, each with its own trade-offs. In addition, Python and Go have many design patterns with their own strengths and weaknesses. In light of this, we will view the satisfaction of these requirements through a more subjective lens, from the perspective of the typical network automation professional. Our aim is to help guide you to making your own decision about which of these languages to pursue.

How do Python and Go compare when it comes to satisfying these requirements? Arguably, both do pretty well—each covering all three, with perhaps one slight weakness versus the other. For instance:

- Both Python and Go satisfy our speed-of-development requirement quite well. Both are extremely easy to adopt and require little maintenance overhead over the long-term. One of Go’s strengths is that it was built for simplicity from the beginning; it typically provides only one or two ways to do something. This means that once you can understand Go code generally, reading others’ code is not too difficult.
- When it comes to the network automation ecosystem, Python has the lead, without question. While Go’s community is still growing rapidly, the early lead established by Python in the network automation community will be hard to beat. However, other, somewhat related communities may prefer Go in certain circumstances. For instance, the cloud native community rallied early around Go, and technologies from that ecosystem (e.g., gRPC and gNMI, both discussed in [Chapter 10](ch10.html#apis)) are often biased toward Go support, or at least have supported Go for a longer period of time.
- For stability and reliability, Go is a much more modern systems-focused language, with a lot of safety-related features built right into the compiler. While creating a stable, reliable service in Python is certainly possible, it can take a considerable amount of extra work because of Python’s runtime-focused nature. Additionally, Go programs can be compiled to a single, statically linked binary. Once a Go program is compiled, you don’t need to install Go on every machine that will run the program or any third-party libraries you want to include in your program. This tends to result in a lower operational burden.

As you can see, both languages cover these requirements handily. Python isn’t going anywhere anytime soon, but Go provides an attractive alternative that may be more suitable in certain cases.

###### Tip

You may also be asking, as many do when they first encounter these subjects, “Which do I learn first?” Take comfort in knowing that there’s probably no wrong answer to this question, especially very early in your learning journey. There are definitely reasons to pick one language over the other, but these reasons are typically self-evident: for instance, if your organization is primarily a Python shop, it might be best to stick with that for now. On the other hand, if no precedent has been established, picking a more modern language like Go has advantages. In the absence of these kinds of external factors, the choice is mostly up to you. Explore both languages at a high level, and maybe write a little in each, before making your own decision.

This chapter is not promoting Go over Python, and this book as a whole does not suggest that you *have* to learn both, or even either. We do our best to highlight the strengths and weaknesses of all approaches, so that you can decide what works best in your particular case.

## Is Go Faster Than Python?

Inevitably, when comparing these two languages, the question of speed comes up. Python does have a reputation for being slower than other languages, and while you can certainly apply optimizations to improve this, such as choosing different runtimes, this is a generally accepted fact of life for most Python developers. In any objective test, Go will be many times faster than Python, without a doubt.

How important, though, is the speed of our language in the world of network automation? You’ll notice we didn’t add this to our list of requirements. For most network automation use cases, seeking out Go solely for the purpose of addressing performance-related concerns is likely to be a red herring. *Most* use cases in network automation involve a lot of waiting for I/O, so any performance gains simply by language choice are usually moot. That said, speed is not something to disregard entirely, and performance is definitely a more significant factor in some use cases. Until those use cases present themselves, however, prioritize the other requirements listed in the preceding section.

## Is Go Harder than Python?

It’s not uncommon for those learning Go for the first time (especially those with primary experience in a language like Python) to develop the perception that Go is relatively difficult to adopt. This perception takes a few forms:

- Go is a statically typed language, whereas Python is dynamically typed (we cover this in more detail in an upcoming section). Python tends to be much more forgiving about which types are used in function parameters, for example.
- Go is a compiled language, which means a seemingly obstructive “extra step” must be performed before a working program is produced.
- Go often complains about things like invalid types and unused variables, preventing a program from even compiling until they’re resolved.

Because of perceptions like these, it’s not hard to understand why, to an outside observer, languages like Go can be viewed as more difficult compared to Python. Python is far more permissive in comparison.

Modern systems languages like Go have been moving in the direction of having the compiler do more work, and for good reason: the more errors we catch at compile time, the fewer we have to deal with at runtime. A junior engineer may view this extra compilation step (and any errors that surface here) as a hurdle or an impediment; a senior engineer will be thankful for the compiler’s brief pause and will try to solve as many problems as possible *before* runtime, when it costs us and our organization much more severely.

Go—like Python—is also known as a *garbage-collected language*. This means it comes with a runtime that takes care of cleaning up unused memory references in the background, allowing you to focus just on the code you want to write. In contrast, languages like C and C++ require you to allocate and free memory yourself, which can not only be arduous but also vulnerable to memory management bugs. So, while it might be easy to write Go off as difficult because of the previous points we’ve discussed, it should be remembered that Go is much more like Python in this respect, and as a result, has a far lower barrier to entry than its compiled counterparts.

It’s important to not overfocus solely on this requirement (speed of adoption is, after all, only one of our requirements). We want a language that’s easy to adopt, stable, *and* resilient to operate in production. Fortunately, Go hits a bit of a sweet spot here: the learning curve is not that much steeper than for Python, but we get a tremendous amount of built-in value in the form of compile-time checks that provide a lot of stability and maintainability advantages for free.

Now that we’ve spent time setting the context for learning Go, let’s dive into the fundamental concepts you’ll need to know to understand this powerful language.

###### Note

Just as we mentioned in [Chapter 6](ch06.html#python), we need to cover a lot of fundamental Go concepts before we can use these concepts to tackle real-world, complex network automation workflows. While the concepts discussed here are certainly relevant to network automation, this chapter is focused purely on these fundamentals, so that you have a solid foundation. [Chapter 10](ch10.html#apis) builds on this foundation by using some popular Go libraries and other APIs for performing common network automation tasks.

# Fundamental Go Concepts

When first learning any programming language, it’s helpful to start with a “Hello, world” example—that is, a minimal example of a working program that prints a short message to the terminal. You can run this program, see its output, and know that you’re starting with a working example you can build on. Let’s start with [Example 7-1](#go-first-program).

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go*](https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go).

##### Example 7-1. Your first Go program

```
package main                                  

import "fmt"                                  

func main() {                                 
    fmt.Println("Hello, network automators!") 
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Packages allow us to organize the code into a logical hierarchy. We are specifying the `main` package here because we want to create an executable program. We’ll explore packages in greater detail in later examples.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `import` keyword allows us to use other packages in the code. In this case, the `fmt` package is part of the standard library and is used for formatted I/O.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `main()` function is the primary entry point when creating an executable program. When we run a compiled Go program, this code represents the beginning of that program’s logical flow. While indentation isn’t as crucial in Go as it is in Python (in Go, scope is formally indicated using curly braces), automated formatting tools like `gofmt` will automatically indent scopes, such as this function.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The `Println()` function is part of the `fmt` package we imported previously and allows us to print a simple string to the terminal as a line of output. You’ll see this quite a few times in the examples to follow—if you’re trying to follow along, don’t forget to import `fmt`!

###### Note

Future examples in this chapter are shortened for brevity. Unless otherwise noted, you can assume they can be found within a similar structure: a `main` package and a `main()` function. You can view the full, working version of any example at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go*](https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go).

You can use `go run` to quickly compile and execute this program with a single command in your bash terminal, as shown in [Example 7-2](#go-running-first-program). This is extremely useful and gives you the same “scripting” experience you’ve come to love from Python, but with all of Go’s unique benefits.

##### Example 7-2. Running your first Go program

```
~$ go run 1-first-program.go
Hello, network automators!
```

###### Tip

The `go run` command is a great way to quickly get started running Go code, but it has its limitations. You should also be aware of the `go build` and `go install` commands, especially if you want to build a reusable binary that you can distribute to other machines that don’t have Go installed.

Now that we have a solid foundation to build on, let’s get into some concepts. Next, we explore variables, common types, and how they compare with those found in Python.

## Types and Variables

As with nearly any programming language, Go comes with a set of basic types. For the most part, they are comparable to the equivalent types in Python, so if you’re familiar with those, these work much the same way. [Table 7-1](#go-built-in-types) shows the most commonly used types in Go.

| Type | Example | Description |
| --- | --- | --- |
| `bool` | `false` | Boolean value; true or false |
| `int` | `3` | Commonly used numeric type; used for integers |
| `float` | `3.0` | Numeric value for nonwhole numbers |
| `string` | `"hello"` | A series of textual characters |

However, Go has some additional variations that you’ll want to be aware of. For instance, `int` is short for a *signed integer*, which can be used to represent either negative or positive values. On the other hand, `uint`, which represents unsigned integers, can represent only positive integers.

Additionally, both `uint` and `int`, as well as `float`, may optionally include a number at the end, such as `uint8` or `float64`. This is a way of statically specifying the size for that type: a `uint8` is an 8-bit unsigned integer (also called a `byte`), and a `float64` is a 64-bit floating-point number.

For types like `uint` and `int` that omit this size, the target system determines the size; for example, `int` is 32 bits long on 32-bit systems, and 64 bits long on 64-bit systems. It is overwhelmingly common (and indeed a Go best practice) to use these more flexible types when possible.

We later get into a few other built-in types, not to mention the multitude of externally defined types (or structs), but this simple set of types suffices for now. Next, we explore the use of variables in Go and make use of these types.

### Variables in Go

In Go, variables are one of the fundamental building blocks of the language, as they are in many other programming languages. Variables allow you to create unique, ideally self-describing references to a value of a given type. Instead of passing around the string `"Hello, network gophers!"`, you can assign this value to a variable—say, `myString1`—and then use the variable to reference that value. Variables, as the name implies, also allow you to reassign new values to that same reference, so you have to change this value in only one place.

You can create a variable in Go in a few ways. In general, the approach you choose depends on whether you want to initialize the variable with a value or leave to a default, or zero value. You may also want to explicitly specify the type, or let the compiler infer the type based on the value you initialize the variable with.

[Example 7-3](#go-initializing-variables) explains these options:

##### Example 7-3. Initializing variables in Go

```
var myString1 string = "Hello, network gophers!" 

var myString2 string                             

var myString3 = "Hello, network gophers!"        

myString4 := "Hello!"                            

var (                                            
    myString5 string
    myString6 = "Hello, network gophers!"
)

// This is invalid, as there is no explicit type declaration
// or a value from which the type can be inferred.
// So, this will fail to compile.
var whatIsThis
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This is the most explicit form; it initializes the variable with a value, while also explicitly stating its type.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Omitting the value defaults to the *zero value* for that type—in this case, a zero-length string (`""`). Other types have different zero values; for instance, a `bool` will default to `false`, and an `int` type will default to `0`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The Go compiler can also infer the type based on the value passed in.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The `:=` operator is shorthand for the previous example, which infers the type based on the provided value.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

The `var` keyword allows you to group variable declarations together, to improve readability.

If you were to copy this code into your own project as is, it would fail to compile, with the message `variable name declared but not used`. This is one major difference between Python and Go: Python has no problem running a program with unused variables (though it’s common to use external linting tools to help catch such occurrences), whereas Go won’t even compile a program successfully if unused variables are present. To fix this, we must *use* the variable—for instance as a parameter to a function call.

###### Note

This is another instance where “stricter” languages like Go seem to be looked at unfavorably in the network industry. After all, Python doesn’t care if variables are unused or not, so why can’t Go just let us do what we want so we can get this script written? Think of it this way: within a network device’s configuration, ACLs often get unwieldy and hard to manage because we fear that removing an entry might break something, so they inevitably grow over time. To prevent this kind of thing from happening in our Go programs, the compiler is doing us a favor by letting us know upfront if a variable is unused. This helps improve readability and maintainability.

You can represent values in Go by using another approach that’s particularly well suited for values that do not change. These are known as *constants*. Whereas variables allow you to reassign new values to them, constants do not; instead, they always retain the value they were initialized with.

Using constants has advantages: since they are unchanging by design, the compiler can safely make optimizations that aren’t always possible with variables. Constants can also be used for potentially larger values—for instance, a floating-point number defined as a constant can have much higher precision than even the `float64` type.

Their usage is similar to variables, but with a few nuances—particularly, the use of the `const` keyword. Also, unlike variables, unused constants are permitted at compile time. [Example 7-4](#go-initializing-constants) shows a few ways to declare constants in your code.

##### Example 7-4. Initializing constants in Go

```
const myString string = "Hello, network gophers!"                           

// myString = "new value"                                                   

const Pi = 3.14159265358979323846264338327950288419716939937510582097494459 

const (                                                                     
    myString2 = "Hello, network gophers!"
    retries   = 3
)
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This is the most explicit form of constant declaration.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This will fail to compile; `myString` is declared above as a `const`, so a re-assignment like this is not permitted (thus this line is commented out).

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

As with variables, the compiler will infer the type from the assigned value if not explicitly stated.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Multiple assignment blocks work the same as variables as well.

Practically speaking, constants should be used when a particular value is known ahead of time and is guaranteed to not change. The maximum value for a VLAN or VXLAN identifier, or the speed for a Gigabit Ethernet interface, are good examples.

### Static versus dynamic type systems

Especially if you have experience with Python, much of what’s been discussed thus far may not be that new to you. Other than the obvious syntax differences, these concepts translate across language boundaries fairly well. Python also has variables and simple types like strings and integers. However, the two languages differ greatly in the way these types are verified and enforced.

Python uses a *dynamic type system*: the types used within a Python program are not checked for validity until runtime. If you write a program that uses an inappropriate type (say, as a parameter for a function), the program will run just fine until it encounters the line of code that makes this mistake. Trying to do math using strings and integers is a classic example, as shown in [Example 7-5](#go-python-typeerror).

##### Example 7-5. `TypeError` in Python

```
>>> x = 1
>>> y = "2"
>>> x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

If you had a program with this code, the error wouldn’t occur until those lines executed. Imagine if your network automation system failed to handle this kind of error at 2:00 a.m. while you were fast asleep!

In contrast, Go uses a *static type system*: types are checked at compile time. You are unable to compile/build your program until these errors are addressed. [Example 7-6](#go-type-mismatch), which is similar to the Python program shown in [Example 7-5](#go-python-typeerror), will fail to compile, with the message `invalid operation: x + y (mismatched types int and string)`.

##### Example 7-6. Type mismatch in Go

```
x := 1
y := "2"
z := x + y
```

You are also not permitted to change the type of a variable once initialized. [Example 7-7](#go-type-change) will fail to compile because you’ve tried to assign a string value to `x`, which was first initialized as an `int`.

##### Example 7-7. Trying to change type in Go

```
var x = 1
x = "foo"
```

Another important point to understand is that even though in this example, `x` is initialized as an `int` implicitly because of the value it is initialized with, this still follows the rules of a static type system. The `x` variable is still just as much an `int` as if we’d explicitly stated so; this kind of type inference is purely for convenience.

This strict enforcement of types extends well beyond these simple examples, and you’ll see their influence in many of the sections to follow.

###### Note

Again, on the surface this all seems rather obstructive, doesn’t it? After all, we’re busy network engineers who just want to get on with our day job, much of which doesn’t involve writing code.

However, most programmers (especially those also operating the software they write, as most network engineers do) would choose to encounter these kinds of errors on our terms, rather than encountering them later on, in the middle of the night.

While no compiler will ever completely prevent all runtime errors, modern systems languages like Go have made great strides to make the compiler as smart as possible—resulting in a program that’s simpler and stabler—while still trying to make the development process as smooth as possible.

You may have also heard languages described as either *strongly* or *weakly* typed. This concept is tangentially related to the dynamic versus static spectrum we’ve discussed in this section, but ultimately describes a different way of looking at type systems. Recall that a static or dynamic type system is defined by *when* types are checked for validity (compile time versus run time). While there is no official definition, *strict versus weak* is generally used to describe how *lenient* the language is when a type mismatch occurs.

Recall Examples [7-5](#go-python-typeerror) and [7-6](#go-type-mismatch), from earlier in this section where we tried to perform a mathematical addition of the integer `1` and the string `"2"`. Even though Python and Go differ in *when* they produce an error (Python does this at runtime, whereas Go won’t even compile the program), neither will allow such an operation without an explicit conversion of some kind. These are both strongly typed systems.

In contrast, a language like JavaScript—which is considered weakly typed—will make an attempt to implicitly convert types whenever possible. Attempting to perform the operation `1 + "2"` will automatically convert `1` to a string and *concatenate* the two operands, resulting in the string `"12"`. While this does avoid a runtime error, this behavior could be entirely against the programmer’s actual intent and could result in serious problems.

Now that you understand the basics of types and variables in Go, it’s time to move on to the backbone of any real-world application of programming: flow control.

## Flow Control

*Flow control* is a language-agnostic term used to describe logical constructs that allow you to specify the decisions your program should make, and the order in which certain tasks are carried out. If you’ve already read [Chapter 6](ch06.html#python), this should sound familiar.

In Python, flow control is accomplished with loops, conditionals, and match statements. In fact, primitives like these are common across a wide variety of programming languages, which is why learning a second or third programming language is usually easier than learning programming for the first time in any language.

Let’s start with conditionals. Like many programming languages (including Python), this is accomplished with an `if` statement. In Go, these work by testing whether an expression evaluates to a boolean `true` or `false`. This can be a simple expression (even a single boolean variable), or a more complex one, with chained logical or arithmetic operators, but ultimately it must evaluate to either `true` or `false`. [Example 7-8](#go-conditionals) shows a simple Go conditional statement.

##### Example 7-8. Conditionals in Go

```
var snmpConfigured bool = true         
if snmpConfigured {                    
    fmt.Println("SNMP is configured!") 
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This is a boolean variable that we’re setting explicitly here, but this could be set any number of ways, such as in response to parsing a config file.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Because `snmpConfigured` is itself a boolean type, it can be used as an expression.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Code within the braces will execute if the preceding expression is true.

The `!` operator is used for negation. It can negate all or part of an expression, as in [Example 7-9](#go-negate-expression).

##### Example 7-9. Negating conditional expressions in Go

```
// In this case, the "!" negates the value of snmpConfigured,
// so the inner statement will execute only if snmpConfigured
// is false.
if !snmpConfigured {
    fmt.Println("SNMP is not configured.")
}
```

Sometimes you want to handle multiple outcomes within the same statement. The `else` keyword serves this purpose in [Example 7-10](#go-else-statement).

##### Example 7-10. Else statement in Go

```
// Both conditions can be handled by using the else
// keyword.
if snmpConfigured {
    fmt.Println("SNMP is configured!")
} else {
    fmt.Println("SNMP is not configured.")
}
```

Boolean values can be only true or false. Other types, like integers, can have a wider variety of possibilities. For these, we must employ a few additional tricks:

- Relational operators such as greater-than (>) and less-than (<) can capture a range of numeric values.
- The else if phrase is used to capture another expression, should an earlier one fail to evaluate to true.
- Logical operators such `&&` (AND) and `||` (OR) can be used to create more complex expressions.

[Example 7-11](#go-complex-conditionals) illustrates a few of these more complex expressions.

##### Example 7-11. More complex conditionals in Go

```
var vlanID int = 1024
if vlanID < 100 {
    fmt.Println("VLAN ID is less than 100")
} else if vlanID > 100 && vlanID < 1000 {
    fmt.Println("VLAN ID is between 100 and 1000")
} else {
    fmt.Println("VLAN ID is greater than 1000")
}
```

Sometimes you want to run a bit of code multiple times. In these cases, loops are a common choice.

Go has only a single type of loop, the `for` loop. As in Python, this can be used to loop, or iterate, over a set of values. However, it also can be used to simply execute a set of instructions until a specified condition is met.

The number of times a loop repeats is determined by the same logic that governs conditionals. In general, while a given statement evaluates to true, the loop continues to repeat itself. Once that expression evaluates to false, the loop exits. In many programming languages, this expression is often referred to as the *exit condition*.

[Example 7-12](#go-simple-loop) is a simple loop that initializes a counter variable `i`, and repeatedly prints its value and increments it by 1 while its value is less than or equal to 5.

##### Example 7-12. Simple loop with counter

```
// Simple loop that prints VLAN IDs in order from 1-5. It
// accomplishes this by incrementing a counter
// and exits once it's greater than 5
i := 1
for i <= 5 {
    fmt.Printf("VLAN %d\n", i)
    i = i + 1
}
```

###### Tip

`Printf()`, another function from the `fmt` package that is similar to `Println()`, also allows you to create formatted strings where you can dynamically inject the VLAN ID into the output. You can read more about the formatting syntax in the [the `fmt` package documentation](https://pkg.go.dev/fmt).

When the value of `i` is greater than 5, the loop’s condition no longer evaluates to `true`, and the loop exits. The output produced by this code confirms this:

```
VLAN 1
VLAN 2
VLAN 3
VLAN 4
VLAN 5
```

[Example 7-13](#go-simple-loop-one-line) shows a more common way to write a simple loop like this. You place the initialization of `i`, the loop’s exit condition, and the increment of `i` all on one line. While the syntax is different, the behavior of this loop is identical to the one in [Example 7-12](#go-simple-loop).

##### Example 7-13. Simple loop (classic notation)

```
for i := 1; i <= 5; i++ {
    fmt.Printf("VLAN %d\n", i)
}
```

Sometimes you need more fine-grained control over the behavior of these loops. For instance, in these examples, any instructions you place within the loop will be executed every time the loop repeats. What if you want the loop to repeat—or even exit—before the end of these instructions is reached?

For cases such as these, the `continue` and `break` keywords are essential. In Go, these keywords work almost exactly as they do in Python.

The `continue` keyword allows you to effectively skip over any remaining instructions. In [Example 7-14](#go-loops-continue), `continue` is used with a conditional that causes the loop to repeat before printing the value of `i`, only when that value is equal to 3.

##### Example 7-14. Using `continue` in Loops

```
// We can use the continue keyword to cause the loop to repeat
// earlier than it normally would
for i := 1; i <= 5; i++ {
    if i == 3 {
        continue
    }

    // Because of the continue statement above,
    // this line will not run when i == 3
    fmt.Printf("VLAN %d\n", i)
}
```

The `break` keyword is used to exit from a loop entirely, even if the exit condition hasn’t yet been reached. [Example 7-15](#go-loops-break) uses the `break` keyword in a loop that doesn’t even have an exit condition. This allows you to control exactly when and how this loop ends.

##### Example 7-15. Using `break` in loops

```
vlanID = 1

for {                                          
    fmt.Printf("Looking at VLAN %d\n", vlanID) 

    if vlanID > 5 {
        break                                  
    }

    vlanID++
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Loops with no exit condition (like this one) will loop indefinitely unless a `break` or `return` statement is used.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This line will always execute as long as the loop is running.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Because the loop doesn’t have an exit condition, this break statement is the only way this loop will end.

In this example, the `break` statement is called when the value of `vlanID` is greater than 5. Since this takes place near the end of the loop, any preceding instructions will still be executed, even if `vlanID` is greater than 5 (a traditional loop with an exit condition would not have this behavior). Therefore, you see six lines of output:

```
Looking at VLAN 1
Looking at VLAN 2
Looking at VLAN 3
Looking at VLAN 4
Looking at VLAN 5
Looking at VLAN 6
```

One important point to keep in mind is that the `continue` and `break` statements by default apply only to the loop in which they appear. In the preceding examples, this is simple because you have only one loop—but if they appeared within nested loops, for example, it would be hard for the compiler to know which loop we are referring to when using these keywords.

The next section illustrates a method for solving this problem and presents other use cases for loops as we explore collection types in Go.

## Collection Types

We’ve covered the basic types in Go, including `string`, `int`, and `bool`. However, sometimes a single instance of one of these types is not enough, and you may want to be able to work with a series of them.

This is a common use case for just about any practical programming task, and while the terminology may differ, you’ll find tools to support this in any modern programming language.

Different languages have their own specific ways of storing series of values, which may have some language-specific behavior. For instance, in dynamic languages like Python we have the *list*, which is similar to an array but offers more flexibility, like being able to grow or shrink the series at will, as well as store a variety of types.

The generalized version you might learn about in a computer science course is the *array*, which is simply a fixed-length series of values of a given type. Go has the concept of an array, as shown in [Example 7-16](#go-collections-array).

##### Example 7-16. Arrays in Go

```
// This declares "vlans" as an array of type "int"
// and a size of 3.
var vlans [3]int

// Once initialized, we can set values in the array
// by their index. Since arrays have a fixed size,
// the compiler can warn us if we use an invalid index
//
// Don't forget, slices and arrays start with index 0!
vlans[0] = 1

// You can also initialize arrays with values at
// the same time
vlans2 := [3]int{1, 2, 3}
```

###### Note

Arrays are a commonly supported collection type, especially in compiled, statically typed languages like Go, because the compiler can easily calculate how much memory is required to store an array. On a 64-bit machine, `int` is 64 bits, and the arrays in [Example 7-16](#go-collections-array) have a fixed size of 3, so a minimum of 192 bits of memory is needed to store each of them (though in practice this ends up being slightly higher because of padding).

From a practical standpoint, however, you’ll almost never see arrays used in Go code. This is because arrays are inflexible—for instance, arrays have a fixed size. If you want to add an element to an array, you have to create a new one with the size you want and then copy the values from the smaller one yourself.

Fortunately, Go offers another option: the slice. *Slices* are similar to arrays in that they store a sequence of values, but they’re more flexible. For instance, slices don’t have a fixed size; you can grow them as needed. For this reason, slices are an overwhelmingly more popular choice than arrays in Go.

However, slices and arrays in Go aren’t totally unrelated concepts. In fact, slices are really just a thin abstraction on top of arrays, and it is in this abstraction where slices gain their flexibility advantage. You can think of slices as simply a *view* into an array—or [as the Go blog puts it](https://oreil.ly/mTBVn), a “descriptor of an array segment.” The advantage of using slices, and the built-in functions for working with them (as we’ll explore in the following examples), is that the management of this *backing* array (the array to which the slice is providing a view) is done for you.

The syntax for initializing a slice is similar to that in [Example 7-16](#go-collections-array), but with slices, we can omit the size parameter. [Example 7-17](#go-collections-initializing-slice) shows a few ways you can initialize slices in Go.

##### Example 7-17. Initializing a slice

```
var intSlice []int                        

var stringSlice []string                  

var vlanSlice = []int{11, 22, 33, 44, 55} 

vlanSlice2 := []int{11, 22, 33, 44, 55}   
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Initializing a slice is similar to initializing an array—just leave out the size! Note, though, that this slice is empty; we need to append values to it before we can do much with it.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

We can create slices of just about any type; here’s a slice of strings!

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The literal method using curly braces also allows us to initialize the slice with values at the same time.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

This is identical to ![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png).

As mentioned previously, slices are more flexible than arrays, and one of the most obvious benefits of this flexibility is that they don’t have a fixed size; you can add elements as needed. This is done with the `append()` built-in function, as illustrated in [Example 7-18](#go-collections-appending-elements-slice).

##### Example 7-18. Appending elements to a slice

```
// append() takes the original slice from the previous example, adds
// a new element, and returns the resulting new slice.
// That's why we're passing "vlanSlice" as the first parameter but then
// overwriting it with the result.
vlanSlice = append(vlanSlice, 66)

fmt.Println(vlanSlice) // output: [11 22 33 44 55 66]
```

As mentioned previously, slices are really just a view into a backing array that is managed for you. This view is defined by two properties:

LengthThe current size of the segment of the backing array that the slice represents.

CapacityThe maximum size of the slice, which is another way of saying “the size of the backing array.”

You can use the `cap()` and `len()` functions to find out the capacity and length of a given slice, as shown in [Example 7-19](#go-collections-slice-capacity-length).

##### Example 7-19. Slice capacity and length

```
// Let's redefine vlanSlice back to a length of 5 elements
vlanSlice = []int{11, 22, 33, 44, 55}

// output: vlanSlice cap is 5, len is 5
//
// The "cap()" function returns an integer containing the slice's capacity,
// len() returns the slice's length. We can see that after initialization,
// both are set to 5, meaning that the backing array has a capacity of 5,
// and the "segment" of that backing array that the slice provides a view
// to is also 5.
fmt.Printf("vlanSlice cap is %d, len is %d\n", cap(vlanSlice), len(vlanSlice))
```

The difference between these two properties can be seen by repeating this print statement after appending some additional values to the slice that we defined in [Example 7-19](#go-collections-slice-capacity-length). See [Example 7-20](#go-collections-slice-capacity-length-appending).

##### Example 7-20. Slice capacity and length after appending

```
vlanSlice = append(vlanSlice, 66)

// output: vlanSlice cap is 10, len is 6
//
// After appending a value, the slice length increased to 6
// as expected, but the capacity is now 10! This is because we reached
// the maximum capacity of the backing array, so append() had to allocate
// a new one.
fmt.Printf("vlanSlice cap is %d, len is %d\n", cap(vlanSlice), len(vlanSlice))

// Append one more time
vlanSlice = append(vlanSlice, 77)

// output: vlanSlice cap is 10, len is 7
//
// After another append, the length has yet again increased to 7, but the
// capacity remains unchanged, because it is greater than the length.
// This means that append() did not have to allocate a new backing array;
// it had enough room to spare to accommodate the additional element.
fmt.Printf("vlanSlice cap is %d, len is %d\n", cap(vlanSlice), len(vlanSlice))
```

###### Note

You may see different allocations after calling `append()` as the behavior of this reallocation may vary based on the types used and the platform your code is running on, etc. The important point to remember is that this reallocation is done for you, so you don’t need to do it yourself.

The lesson to learn here is that being able to dynamically append elements to a slice does come with potential drawbacks to consider. Repeatedly appending elements to a slice may cause its length to outgrow its capacity. When this happens, a new backing array will have to be allocated, and then on top of that, the elements from the old backing array will have to be copied over to the new.

The good news is that `append()` does all that for you, so you don’t have to do it yourself. However, these operations can have a significant negative impact on performance, especially for large slices. Imagine appending elements to a slice with millions of elements!

One way to deal with this is to use `make()` to initialize a slice. When using this function, you must specify the type and length of the slice you wish to create, but you can also optionally specify the capacity for the slice, as shown in [Example 7-21](#go-collections-slice-make).

##### Example 7-21. Using `make()` to set slice capacity

```
preallocatedVlanSlice := make([]int, 2, 50)  

// output: preallocatedVlanSlice cap is 50, len is 2
fmt.Printf("preallocatedVlanSlice cap is %d, len is %d\n",
    cap(preallocatedVlanSlice), len(preallocatedVlanSlice))

preallocatedVlanSlice[0] = 1                 
preallocatedVlanSlice[1] = 2                 

for i := 3; i <= 50; i++ {                   
    preallocatedVlanSlice = append(preallocatedVlanSlice, i)
}

// output: preallocatedVlanSlice cap is 50, len is 50
fmt.Printf("preallocatedVlanSlice cap is %d, len is %d\n",
    cap(preallocatedVlanSlice), len(preallocatedVlanSlice))
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We can get the flexibility benefits of slices and the predictability/performance of arrays by using `make()` to declare slices with a length (and capacity) ahead of time.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Because our slice’s length is 2, we can set the first two elements to indices 0 and 1.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

If we go beyond this length, we must use `append()`—but since the slice has a capacity of 50, we can add 48 more elements before `append()` must allocate a new backing array. Until then, this will simply grow the length and set values at the referenced index. Efficient!

If you know in advance how large a slice might become, you can use `make()` to avoid the costly reallocation that can happen when using `append()`.

You can use what you learned earlier about loops to iterate over a slice. This is useful when you want to perform an operation over the elements of a slice individually. [Example 7-22](#go-collections-slice-iterating) does this while printing each element of the slice.

##### Example 7-22. Iterating over slices with `for` loops

```
var vlanSliceIter = []int{11, 22, 33, 44, 55}

for i := 0; i < len(vlanSliceIter); i++ { 
    fmt.Printf("vlanSliceIter index %d has a value of %d\n", i, vlanSliceIter[i])
}

for i := range vlanSliceIter {            
    fmt.Printf("vlanSliceIter index %d has a value of %d\n", i, vlanSliceIter[i])
}

for i, val := range vlanSliceIter {       
    fmt.Printf("vlanSliceIter index %d has a value of %d\n", i, val)
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We can use a `for` loop with a counter variable to iterate over the slice. Starting at 0 and ending before we reach the end of the slice allows us to iterate over each element one at a time.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Alternatively, we can use the `range` keyword to do the same thing. At each iteration, the variable `i` will be set to the next index of the slice.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `range` keyword can also provide the value at each index.

Combining `range` with some of the other keywords you learned like `break` or `continue` can be useful for controlling when to act on a particular element in a slice, or when to stop iterating entirely, as shown in [Example 7-23](#go-collections-slice-iteration-break).

##### Example 7-23. Breaking out of slice iteration

```
// When searching an array or slice for a particular value, you can use
// the break statement to stop iterating once you've found it.
toFind := 33
for i, val := range vlanSliceIter {
    if val == toFind {
        fmt.Printf("Found! Index is %d\n", i)

        // Since we've found our value, there's no point in looping any further.
        // We can use break to stop iterating over the slice.
        break
    }
}
```

As we stated previously, `continue` and `break` statements by default apply only to the loop in which they appear. As in [Example 7-23](#go-collections-slice-iteration-break), this can be quite simple when you have only one loop. However, for multiple loops nested within one another, these keywords may not be sufficient on their own, as the compiler will assume you’re referring to the innermost loop. To solve this problem, you can use *labels*, which allow you to refer to a loop scope other than the immediately local scope. If you have a set of deeply nested loops, this allows you to break out of a loop scope of your choosing.

Let’s say you have a data structure made of nested slices of varying types, which represents a series of network devices. Each device has a series of interfaces, and each interface has a series of VLANs configured on them. If you want to find the first device and interface that was configured with VLAN 400, you’d need to use a series of nested loops to search for this. Once found, it’s not very useful to continue iterating, so you want a way to stop all loops from iterating.

[Example 7-24](#go-loops-labels) uses a label on the outermost scope of a nested loop so that you can break out of it even if you use the `break` keyword on the innermost loop.

###### Note

[Example 7-24](#go-loops-labels) uses structs so you can more easily refer to the slices you’re iterating over by name (e.g., `.interfaces`, `.vlans`, etc.), which are defined outside this particular example. We cover this concept in [“Structs”](#structs), and you can always see the full example in the repository at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go*](https://github.com/oreilly-npa-book/examples/tree/v2/ch07-go).

##### Example 7-24. Using labels on loops

```
deviceloop:                                        
    for _, device := range devices {               
        for i, iface := range device.interfaces {  
            for _, vlanID := range iface.vlans {   

                if vlanID == 400 {
                    fmt.Printf("Device %s has vlan 400 configured on interface %d\n",
                      device.hostname, i)
                    break deviceloop               
                }
            }
        }
    }
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This label `deviceloop` applies to the outer loop, which is declared immediately in line ![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png). We can use `continue` or `break` statements at any level of nested loop to refer explicitly to this outer loop scope by name.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This outer loop iterates through a slice of devices.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This middle loop iterates through a slice of that device’s interfaces.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

This inner loop iterates through a slice of that interface’s VLAN IDs.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

A typical `break` statement would break out of only the inner loop. By referring to the `deviceloop` label we declared earlier, we can specify that we want to break out of the outermost loop. This means that all three loops stop iterating.

Note that `continue` statements work the same way; if you want to skip other interfaces on a particular device but still look at the interfaces of the next device in the slice, you could use `continue` in this example to print all devices that have an interface configured with VLAN 400, while skipping any unnecessary iterations in the process.

###### Warning

While labels have their place, using them to solve challenges with nested loops can have a negative impact on the maintainability of your code. Even the simple code in [Example 7-24](#go-loops-labels) can be difficult to follow, and this will only increase as the complexity of your program grows. In many cases, the use of labels can be taken as a hint that it may be time to break up your code a little more. In an upcoming section, you’ll learn about using functions to build reusable blocks of code, and how you can use them to solve this problem in a more maintainable way.

As you can see, slices are a powerful tool for storing a sequence of values. However, they’re not the only collection type in Go. In some use cases, a slice might not be the best choice; for instance, as you saw in the previous example, in order to find a value in a slice, you don’t implicitly know its index up front. Rather, to find it, you must iterate over the slice until the element is found. For large slices, this can take a long time.

Sometimes, a key-value data structure could be a more appropriate choice. These work by storing a particular value using a corresponding *key*, forming a key-value pair. Once stored, the value can be looked up simply using this key, regardless of where that value is stored in memory. Unlike with slices or arrays, this operation is extremely fast, as it doesn’t require iteration.

This kind of data structure is also common in many programming languages, but may be known by different names. You saw this in [Chapter 6](ch06.html#python) in the form of dictionaries. Go’s key-value data structure is called the *map*. The methods for initializing maps are somewhat similar to slices, but have a few minor differences and some important considerations. [Example 7-25](#go-collections-map-initialize) shows a few of these.

##### Example 7-25. Initializing maps

```
// CAREFUL - this syntax will only declare the map but will not
// initialize it.
var nilMap map[string]int
// Trying to write to this map will cause a runtime panic!
nilMap["foo"] = 80

// It's much safer to declare and initialize the map at the same time.
// Each of these examples is equivalent - they each declare and initialize
// a map with a "string" type for the keys, and an "int" type for the values.
var myMap = make(map[string]int)
var myMap2 = map[string]int{}
myMap3 := map[string]int{}

// The "literal" method using curly braces also allows us to initialize
// the map with some values at the same time.
vlanMap := map[string]int{
    "VLAN_100": 100,
    "VLAN_200": 200,
    "VLAN_300": 300,
}
```

If you’ve already gone through [Chapter 6](ch06.html#python), some of the syntax for reading from or writing to this map should be somewhat familiar, perhaps with some minor differences. [Example 7-26](#go-collections-map-read-write-keys) illustrates reading a value from a map, writing new keys (or overwriting existing ones) to the map, and deleting existing keys.

##### Example 7-26. Reading, writing, and deleting keys from maps

```
vlan := vlanMap["VLAN_300"]      
fmt.Printf("vlan is %d\n", vlan)

vlanMap["VLAN_400"] = 401        
vlanMap["VLAN_400"] = 400        

delete(vlanMap, "VLAN_300")      
fmt.Println(vlanMap)

fmt.Println(vlanMap["VLAN_999"]) 
// output: 0
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This reads a value from the map using the expected key and creates a new variable `vlan` with this value.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This syntax adds a single key-value pair to the map. Note that the key is a string, and the value is an int, which matches the types declared when the map was created.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

We can overwrite an existing key.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

We can delete a key-value pair from a map by using the `delete()` function. This requires two parameters: first the map itself, and then the key to delete.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

Reading a key that doesn’t exist will return the zero value for the value’s type—in this case, `0`.

One important point to take away from [Example 7-26](#go-collections-map-read-write-keys) is that looking up a key that doesn’t exist in a map will not produce an error, as it does in other languages like Python. Rather, if you attempt to read a key from a map that doesn’t exist, you’ll get back the zero value for the type used as that map’s value.

###### Tip

The *zero value* for a type is another way of saying the *default* value for a type. If you create a string variable but don’t initialize it with a value, the value will be an empty string (`""`). Boolean variables default to `false`, and `int` variables default to `0`. Since your map uses `int` for its value type, this is what you’ll get back if you try to read a key that doesn’t exist.

Because you’ll get a zero value instead of an error, knowing whether a given key exists in the map can be important. Imagine reading a key that *does* exist in the map, but the value for that key just happens to be that type’s zero value. It’s a totally reasonable scenario—and in this case, it would be impossible to rely solely on the value retrieved to determine whether the key actually exists in the map, since you’d get the zero-value back either way.

Another problem is the behavior around writing keys to the map. If the key doesn’t already exist, writing a new key is no problem. However, if the key does already exist, writing to this key will silently replace its old value, which may not be desired. In some cases, knowing first whether the key already exists can be useful, so you can then decide whether to replace the existing value.

Fortunately, Go offers precisely what you need for both of these use cases: a way to test whether a key exists in a map. You can use this within a conditional (`if`) statement to perform instructions depending on whether the key is found in the map. [Example 7-27](#go-collections-map-testing-exists) shows this idea in action.

##### Example 7-27. Testing whether a key exists in a map

```
if val, found := vlanMap["VLAN_999"]; found {       
    fmt.Printf("Found vlan %d\n", val)              
}

if _, found := vlanMap["VLAN_999"]; !found {        
    fmt.Println("Did not find VLAN_999 in the map") 
}

if val, found := vlanMap["VLAN_400"]; found {
    fmt.Printf("Found vlan %d\n", val)              
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The same syntax used for reading a key from a map can optionally return a second boolean value, which is set to `found`. We can then test whether `found` is `true` (which indicates the key already exists) on the same line by adding a semicolon and then the variable `found` on its own (remember, booleans can be used as entire expressions in conditionals).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The key doesn’t exist, but the conditional in ![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png) evaluates to `true` only if it is found—so this line will *not* execute.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

We can test the reverse by simply negating `found`; this is an easy way to test that a key is *not* found in a map. In this case, we don’t expect the retrieved value to be useful, so we can ignore it by replacing `val` with an underscore. This tells the compiler to discard the retrieved value.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

This key still doesn’t exist, but unlike the preceding conditional, this one evaluates to `true` if the key is *not* found, so this line *will* execute.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

This conditional specifies a key that *does* exist, and evaluates to `true` if it’s found in the map—so this print statement *will* execute.

You can, of course, include much more than print statements within these conditionals. You may choose to delete a key if it exists, or perhaps write a key to a map *only* if it doesn’t already exist, for example. Having the ability to first understand whether a key exists in a map enables you to decide about the behavior of your program based on a map’s state.

As with slices, you may want to be able to iterate over the key-value pairs in a map, as shown in [Example 7-28](#go-collections-map-iterating). You might notice the syntax is similar to iterating over a slice (using the `range` keyword).

##### Example 7-28. Iterating over key-value pairs in a map

```
// As with slices, the range keyword allows us to easily
// iterate over the key-value pairs in the map.
// Note that unlike slices, maps are not ordered.
for key, value := range vlanMap {
    fmt.Printf("%s has a value of %d\n", key, value)
}

// If we don't need the values, we can omit the second variable to retrieve only the
// keys out of the map.
for key := range vlanMap {
    fmt.Printf("Found key %s\n", key)
}
```

Thus far in this chapter, we’ve explored quite a few of Go’s built-in types: singular types like `int`, `string`, and `bool`, as well as collection types like maps and slices. We’ve also explored flow-control tools like conditionals and loops. Even the simplest program or script will use most or all of these concepts. However, inevitably, those small scripts grow to a point where it may be necessary to break up the code and create reusable chunks. The next section explores how to do this in Go with functions.

## Functions

The vast majority of programming languages you might run into offer the ability to create blocks of code that are somewhat self-contained and can be used to accomplish a specific task. These are often called *functions*. They have a few benefits that apply in just about any programming language:

Reusable codeFunctions can make it possible for you to create chunks of code that can be reused by you or even other programmers. For instance, the `fmt` package in the standard library has the `Println()` function, which we’ve made liberal use of in this chapter thus far. You didn’t have to worry about the details of how to actually write text to standard output; you just called the function, and it did the rest. Creating functions that perform even moderately complex tasks on their own can make future programming more productive.

Improved readability and maintainabilityFocusing on accomplishing a specific task in a function makes that task much easier to reason about. Code within the function is there only to facilitate that single task, and the rest of your program can simply call this function without worrying about what’s happening inside.

You’ve already seen functions in use in this chapter; recall that all the examples thus far are designed to be executed within a `main()` function. This function, defined within a package named `main`, will be automatically called when the resulting binary is executed. [Example 7-29](#go-functions-main) shows a simple program that illustrates this.

##### Example 7-29. The `main` function

```
// This is a function like any other - but because it
// has the special name main and is located within a
// package also called main, it will be automatically
// called when this program is executed.
func main() {
    fmt.Println("Hello, network automators!")
}
```

However, you can also define your own functions. For instance, [Example 7-30](#go-functions-minimal) shows that the call to `fmt.Println()` can be wrapped in a custom function `doPrint()`, which can then be called from `main()`.

##### Example 7-30. A minimal function

```
func main() {
    doPrint()
}

func doPrint() {
    fmt.Println("Hello network automators!")
    fmt.Println("Welcome to Network Programmability and Automation!")
    fmt.Println("Enjoy this chapter on the Go programming language.")
}
```

This can be useful if you simply want to make a set of tasks more repeatable. Calling a single function to perform many tasks can keep the code in `main()` much simpler and easier to understand.

However, while certainly permissible, it’s not always practical for functions like this to be truly self-contained. Functions often require *input* to be able to do their tasks; the tasks themselves may be defined in the function, but they often need some kind of data from elsewhere in the program to do their work. For instance, the call to `fmt.Println()` isn’t that useful unless you provide it with the string you want to print to standard output.

For this reason, many functions have one or more *parameters*. These work like variables that are initialized and usable within the scope of the function, but are populated with values passed when the function is called. These follow the same strict typing rules as normal variables, and their type has to be explicitly declared within the function definition. [Example 7-31](#go-functions-parameter) shows a function `printMessage()` with a parameter `msg`, which is a `string` type. You can then refer to `msg` as if it were any other string variable.

##### Example 7-31. Function with a parameter

```
func printMessage(msg string) {
    fmt.Printf("Hello network automators, today we're learning %s!\n", msg)
}
```

###### Note

To reiterate a point made earlier, this strict type system behavior is often one of the arguments made in favor of languages like Python. Because these languages don’t require function parameters to have an explicit type like this, they are perceived as easier to learn. However, this kind of flexibility adds a nontrivial amount of complexity for the programmer, who will inevitably have to add type checks to ensure that the function won’t fail at runtime if the wrong type is used.

Strict type systems like this may seem overly cumbersome on the surface, but don’t take for granted the time and mental energy saved in avoiding the kind of runtime checks necessary in dynamic languages. These systems also make your code easier to understand. Remember, the smarter your compiler is, the more maintainable and stable your program will be!

Functions not only accept input in the form of parameters, but can also return values to be consumed by the caller (perhaps to initialize a new variable). Like parameters, the return type must be explicitly declared. [Example 7-32](#go-functions-parameter-return-type) shows a function that calculates the total number of addresses in an IPv4 prefix. The caller must only provide the length of the prefix as an `int` parameter, and the function will return an `int` value representing the number of addresses.

##### Example 7-32. Function with parameter and return type

```
func totalIPv4Addresses(prefixLen int) int { 
    x := 32 - prefixLen                      

    addrCount := math.Pow(2.0, float64(x))   

    return int(addrCount)                    
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`totalIPv4Addresses()` is a function for calculating the number of addresses in an IPv4 prefix of a provided length. `prefixLen` is a parameter of type `int`. The return type for this function is also `int`, which is declared after the set of parentheses containing the function parameter(s).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

To calculate the number of addresses in an IPv4 address, we must calculate `2x`, where `x` is `prefixLen` subtracted from 32. So let’s first get `x`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Go doesn’t have an exponent operator, but we can use the `Pow()` function in the `math` package. This function has two parameters, and each has a type of `float64`, which is why we’re converting the latter using the `float64` built-in function (`2.0` is already a `float64`).

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`math.Pow()` also has a return type of `float64`, so we must convert it to an `int` before returning it, to satisfy the function’s return type. The `return` keyword allows us to exit a function immediately and return the value provided.

Because this function returns a value, you can capture it in a new variable to be used later, as illustrated in [Example 7-33](#go-functions-parameter-return-type-call).

##### Example 7-33. Calling a function with a parameter and return type

```
func main() {
    // Create a variable to hold the prefix length we'll pass in to
    // totalIPv4Addresses()
    prefixLen := 22

    // Call totalIPv4Addresses and provide the variable prefixLen as the
    // required parameter. (We could provide a value of 22 directly as well,
    // but this way we can reuse this variable in the log message below.)
    //
    // Note also that we're assigning the return value to a new variable
    // called "addrs"
    addrs := totalIPv4Addresses(prefixLen)

    fmt.Printf("There are %d addresses in a /%d prefix\n", addrs, prefixLen)
    // output: There are 1024 addresses in a /22 prefix
}
```

[Example 7-34](#go-functions-multiple-parameters-return-values) shows that functions can have multiple parameters or multiple return types.

##### Example 7-34. Function with multiple parameters and return values

```
func main() {
    // both input parameters and return values are separated by commas
    sum, product := sumAndProduct(2, 6)
    fmt.Printf("Sum is %d, product is %d\n", sum, product)
}

// sumAndProduct takes in two integers x and y, and returns their sum and product,
// respectively.
//
// Note that the input parameters x and y are separated only by a comma - since
// they're both integers, we can just specify int once after them.
//
// Also, note that the return types are also separated by a comma and also wrapped
// in parentheses.
func sumAndProduct(x, y int) (int, int) {
    sum := x + y
    product := x * y
    return sum, product
}
```

The examples thus far are fairly simple functions performing basic mathematic tasks that have a predictable outcome. However, some functions include operations that can fail, such as those that rely on I/O from the network or filesystem. It’s important to know when a particular operation has succeeded or failed, so we can decide what to do next; we could perhaps log a message to our user and/or try the operation again.

Go handles errors like these with a special `error` type. You can see this type in the declaration of the function `createVLAN()` in [Example 7-35](#go-functions-error-value).

##### Example 7-35. Function that returns an error value

```
func createVLAN(id uint) error {                     

    if id > 4096 {                                   
        return errors.New("VLAN ID must be <= 4096") 
    }

    fmt.Printf("Creating VLAN with ID of %d\n", id)  
    return nil
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`createVLAN()` takes in an unsigned integer parameter for the VLAN ID and returns an error type if a problem is encountered.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Even though the `uint` type (used for the `id` parameter) can support billions of values, you know that 4096 is the maximum VLAN ID. So we can add a conditional that checks for this and returns a new error if the ID is over this value.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`New()` is a function in the `errors` package that allows us to initialize a new error value from a string containing your custom error message.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

This will execute only if `id` is a valid VLAN ID, so to simulate the creation of a VLAN, we’ll print a log message and return `nil` as the error value, which indicates that no error occurred.

In Go, after calling a function that returns an error, it’s necessary to explicitly check this error value. In the vast majority of cases, you’ll want to do this immediately after the function returns. Unlike languages like Python, which work by throwing exceptions that could stop your program if you don’t handle them properly, Go requires that you explicitly check the returned error for a non-nil value to determine whether an error took place. [Example 7-36](#go-functions-handling-errors) illustrates a common pattern that occurs after most function calls.

##### Example 7-36. Handling errors

```
// It is conventional to assign error return types to a variable err.
err := createVLAN(50)

// If err is not a nil value, it means an error occurred, so we should
// check for that immediately after calling the function above.
if err != nil {
    // This is where you could take steps to recover from the error
    // if possible.
    fmt.Println(err)
}
```

###### Tip

Not every function returns an `error` type. Some functions return only concrete types like `int` or `bool`, and others return nothing at all. When calling a function, especially one that you didn’t write, take the time to understand the function’s documentation if it’s available so you can properly interpret any values it returns.

Previously, you used the `continue` and `break` keywords to more carefully control the operation of loops in Go. In [Example 7-24](#go-loops-labels), you also used labels to disambiguate which loop scope is being targeted by these keywords, in the event of nested loops. However, you can use what you just learned about functions as a potentially more maintainable alternative to using labels.

Anywhere within the scope of a function, you can use the `return` keyword to exit from that function, regardless of any additional level of scope (i.e., from conditionals, loops, etc.) in which it is called. [Example 7-37](#go-functions-return-break) makes a nested loop more readable by putting it in its own function and relying on the `return` keyword to break execution when desired.

##### Example 7-37. Returning from a function to break out of nested loops

```
func returnFromNestedLoops() {
    for _, device := range devices { 
        for i, iface := range device.interfaces {
            for _, vlanID := range iface.vlans {
                if vlanID == 400 {
                    fmt.Printf("Device %s has vlan 400 configured on interface %d\n",
                        device.hostname, i)
                    return           
                }
            }
        }
    }
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

No label is needed here!

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The `return` keyword immediately exits from the entire function, so this effectively breaks out of all three loops.

In some cases, using `return` can provide a more readable alternative than the label-based approach. In this example, you are not only avoiding the use of labels (which can be difficult to keep track of), but also enclosing the entire nested loop structure within the function, making it easier to reason about.

Next, we move beyond the built-in types like `int` and `string` we’ve been using thus far to work with custom-defined types and the variety of tools Go offers to work with them.

## Structs

Sometimes the built-in types like integer, boolean, and string are not sufficient to create representations of complex logical or even physical constructs that you want to be able to represent in your programs. For instance, using one of these built-in types, how might you represent a network device such as a switch or a router? Would you use a string to represent this? A string type might capture the hostname of this device, but that’s it—what about that device’s port layout, its configuration, or its operational status? Even a far simpler example—the humble VLAN—still has two properties that are typically described together: an ID and a name.

It’s important to be able to model constructs like this in your code; doing so makes your code far easier to understand and maintain. In Go, the *struct* allows you to create your own type definitions, which are composed of properties, or fields, which have their own types (which can themselves be built-in types or other struct types). In [Example 7-38](#go-structs-definition), you define a struct type `vlan` with two fields, `id` and `name`.

##### Example 7-38. Struct definition

```
// This is where we define our custom struct vlan
// Note that this is just a definition - we'll actually create
// an instance of this later.
type vlan struct {

    // id and name are fields of our vlan struct.
    // They each have their own type definition (in this
    // case, uint and string)
    id   uint
    name string
}
```

###### Note

Go is far less of an object-oriented language when compared to Python (Go doesn’t include traditional object-oriented features you might know from Python, such as inheritance). But thinking of structs as Go’s analog to Python’s classes (covered in [Chapter 6](ch06.html#python)) is a reasonably close approximation for learning purposes. Like Python’s classes, structs are a way to model real-world objects with properties (fields) and behaviors (methods).

As shown in [Example 7-39](#go-struct-instantiation), you can then create an instance of this struct and store this value as a single variable—the type of which is `vlan`. That variable will hold both the ID and name of this VLAN together as fields of the same object.

##### Example 7-39. Instantiating a struct

```
// instantiate a vlan type using the literal syntax.
//
// You can populate every field with a value, or you can leave it out, and the
// field will be set to the zero value for that field's type.
myVlan := vlan{
    id:   5,
    name: "VLAN_5",
}

// We can also set these fields after instantiation
myVlan.id = 6
myVlan.name = "VLAN_6"
```

As we mentioned previously, a valid VLAN ID must be less than or equal to 4096. However, when instantiating structs directly in this fashion, you could set the `id` field to any valid `uint` value, which can contain many more values than this.

To provide a more opinionated way of instantiating structs so that you can check for constraints like this, it’s not uncommon to create a constructor function, as shown in [Example 7-40](#go-struct-constructor). This function takes in a set of parameters needed to instantiate the struct type but is also able to perform checks that ensure that the values are valid.

##### Example 7-40. Instantiating a struct within a constructor function

```
func NewVLAN(id uint, name string) (vlan, error) {            
    if id > 4096 {
        return vlan{}, errors.New("VLAN ID must be <= 4096") 
    }

    return vlan{                                             
        id,
        name,
    }, nil
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`NewVLAN()` is a constructor function, which returns an instantiated `vlan` instance but also ensures that the `id` field is populated with a valid VLAN ID. The first letter in this function is capitalized, indicating it is *exported* (accessible from outside the current package).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This function has two return types: the first is `vlan`, and the second is `error`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

When returning a non-nil error alongside a struct type, it’s conventional to return the zero value for those struct types. We did this with the empty braces as in ![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png).

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

We already determined that the `id` parameter satisfies your requirements, so we can instantiate and return a `vlan` right here in the `return` statement, passing in the `id` and `name` variables as fields.

In a practical setting, instantiating a struct often requires more than simply populating its fields with static values. It’s not out of the ordinary for more complex setup tasks to be required in order to populate the struct with the information needed. Constructor functions like these allow all this logic to be contained in a single function, which enables consumers to easily create a working instance of the struct.

###### Note

[Example 7-40](#go-struct-constructor) mentions that the constructor function is exported, which means it is accessible outside the current package. This is common for constructor functions such as this. Constructor functions provide a more stable API for instantiating structs, while also performing checks like the ID range check you saw in the example. We cover the differences between exported and unexported in [“Packages and Modules”](#packages_and_modules); for the time being, we’ll continue to operate in the `main` package as we have thus far.

Structs can use other structs in their field definitions. Given the definition `vlan` in [Example 7-38](#go-structs-definition), you can include this type in the fields of a new struct, such as `device`, as defined in [Example 7-41](#go-struct-other-structs).

##### Example 7-41. Using struct types in other struct definitions

```
type device struct {
    hostname string

    // Here, vlans is a field on the device struct. Its type
    // is a slice of vlan instances.
    vlans []vlan
}
```

However, the physical or logical constructs we’re trying to model with structs are usually more than just a set of properties we want to store in memory. If structs represent what something *is*, we need something to also describe what something *does*. We need a way to represent *behavior*. For this, structs can have methods.

## Methods

*Methods* are similar to functions in that they can have parameters, return types, and keywords that are specific to functions, like `return`. However, one significant difference is that methods include a receiver. A *receiver* is like a function parameter: it is made available to the function body in the same way, but always represents the instance of the struct it’s defined on. You’ll also see receivers declared prior to the method name, rather than in the usual place function parameters are declared.

For a practical demonstration, [Example 7-42](#go-struct-method-defining) builds on [Example 7-41](#go-struct-other-structs) by defining a new method on the `device` type that prints the hostname of the device to the terminal.

##### Example 7-42. Defining a method on a struct

```
type device struct {
    hostname string
    vlans []vlan
}

// printHostname has no explicit parameters, but does have a receiver of type
// device named d.
func (d device) printHostname() {
    // We can refer to d in the body of the method
    // to access the fields of the instantiated struct object.
    fmt.Println(d.hostname)
}
```

Since methods are, by definition, functions declared on an *instance* of a struct, in [Example 7-43](#go-struct-method-invoking), you must first instantiate your `device` struct in order to be able to call the `printHostname()` method on it.

##### Example 7-43. Invoking a method

```
// Methods are defined on a struct instance, so we must first instantiate device
// as a new variable myDevice.
myDevice := device{hostname: "r1"}

// While functions are called from a package (i.e., fmt), methods are called
// from an instance of a struct, which we created above.
//
// Note that there's no need for this method to have a hostname parameter;
// since the receiver is passed implicitly, the method already has access to
// this receiver's hostname field.
myDevice.printHostname() // output: "r1"
```

What if you want to create a method that *sets* the hostname? This could be useful; perhaps you could enforce some kind of length limit here. [Example 7-44](#go-struct-method-value-receiver) shows that you can assign a new value to the fields of the receiver the same way you might do this for a struct instance outside a method.

##### Example 7-44. Defining the `setHostname()` method

```
func (d device) setHostname(hostname string) {
    // If the length of the hostname parameter is greater than 10,
    // use slicing syntax to shorten to 10 characters.
    if len(hostname) > 10 {
        hostname = hostname[:10]
    }

    // Assign the result to the hostname field of receiver d
    d.hostname = hostname
}
```

However, when you execute this method and call `printHostname()` once more, you see some strange behavior, shown in [Example 7-45](#go-struct-method-value-receiver-print).

##### Example 7-45. `setHostname()` not updating the hostname as expected

```
myDevice.printHostname() // output: "r1"
myDevice.setHostname("r2")
myDevice.printHostname() // output: "r1" ??
```

Interestingly, even though you call `setHostname()` with a parameter of `r2`, if you call `printHostname()` once more afterward, it still produces an output of `r1`, which is the original hostname you used to initialize the struct in previous examples.

To explain this, you need to dive into a concept that you may not have had much exposure to if you’re new to programming or if your primary experience comes from Python: the concept of pointers. For those who don’t write low-level code every day, this may come off as a bit of an advanced topic, but have no fear. Go makes this much easier to deal with than most languages that include this concept.

When you call a function (or method) in most programming languages, your program (under the hood) will allocate additional memory for that function on a region of memory known as the *stack*. The portion of the stack allocated for a particular function, known as a *stack frame*, is used to store values that are needed by that function while it’s running. It’s also generally pretty fast.

Go is typically referred to as a *pass-by-value* language. One way this behavior is observed is that whenever you invoke a function or method, stack memory is allocated, and any parameters for that function are *copied* into that memory space. For methods, this includes the receiver; the values that make up that receiver’s fields are also copied into this region of memory, as illustrated in [Figure 7-1](#go-mutating-value-receiver).

![npa2 0701](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0701.png)

###### Figure 7-1. Mutating a value receiver

When you changed the `hostname` field on your receiver `d` in [Example 7-44](#go-struct-method-value-receiver), you did this on the *copied value* of this receiver within the method. Outside the method, in your `main()` function, `myDevice`—which is what your method copied *from*—still has the hostname `r1` because you modified only its copy, which was then discarded when the function exited. The original `myDevice` remains unaffected.

So, you need a way to mutate the original value. But how can you do this if everything in Go is passed by value and is therefore copied into contexts like functions or methods? In Go, you can use *pointers*—and in this particular case, *pointer receivers*. A pointer is exactly what it sounds like: it “points” to a specific memory address where a value is stored. In this case, rather than copying a struct’s value (all of its constituent fields) into the stack, only the value of the pointer—the address in memory it refers to—is copied. This allows the code in `setHostname()` to mutate the original value, as illustrated in [Figure 7-2](#go-mutating-pointer-receiver).

![npa2 0702](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0702.png)

###### Figure 7-2. Mutating a pointer receiver

When we manipulate the fields of a pointer to our struct within the method, those changes will outlast the stack frame and be made on the original copy of that struct instance. In some cases, this is made possible because the language’s runtime will store the original value not on the stack, but on a different region of memory known as the *heap*. Allocating memory on the heap is more computationally expensive than using stack memory, but when you need to mutate the original value, the trade-off can be worthwhile.

In our example, you need to convert the `setHostname()` method to use a pointer receiver rather than a value receiver. Thankfully, this change is remarkably simple: you add an asterisk (`*`) just before the receiver’s type. This indicates the receiver is a *pointer* to a `device` value rather than a copy of that value. Any changes you make to the fields of your receiver `d` will be applied to the original `myDevice` instance you created in the `main()` function. [Example 7-46](#go-struct-method-pointer-receiver) shows the use of a pointer receiver to update the `hostname` field of the `device` struct.

##### Example 7-46. Defining the `setHostname()` method with a pointer receiver

```
// This has a pointer receiver, denoted by the asterisk before the device
// receiver type. This means that setting the hostname field here will apply
// to the original copy of this struct instance.
func (d *device) setHostname(hostname string) {
    // If the length of the hostname parameter is greater than 10,
    // use slicing syntax to shorten to 10 characters.
    if len(hostname) > 10 {
        hostname = hostname[:10]
    }

    // Assign the result to the hostname field of receiver d
    d.hostname = hostname
}

func main() {

    myDevice := device{hostname: "r1"}

    // Since the setHostname() method is declared with a pointer receiver,
    // it will mutate the hostname field in the original instance,
    // represented here by the variable myDevice.
    myDevice.setHostname("r2")
    myDevice.printHostname() // output: r2
}
```

###### Note

Most of the time, if you’re simply using an existing struct or its methods, you don’t have to care about whether they’re using a value or pointer receiver, because Go handles this for you (you’ll notice that no change to how you *called* this function was needed). This isn’t always true, though, as you’ll see in the next section.

You might be asking yourself, “Why not just use pointer receivers everywhere?” Often it does seem more convenient to always use pointer receivers so you never have to run into this problem. For programs that aren’t particularly performance-sensitive, this may be a sensible approach. For others, more consideration may be necessary.

For example, copying values onto the stack sounds bad, but it’s usually quite fast, since stack memory is calculated at compile time and allocated for your program when it starts. In contrast, the use of a pointer receiver often implies an allocation on the heap, which can be computationally expensive since this must be requested via the operating system at runtime. So, for small receiver values, it may be best to avoid pointer receivers if you don’t need to mutate the receiver. However, for large receiver values, and especially if you’re repeatedly calling a method, the opposite may be true: copying onto the stack may be tremendously costly, whereas passing a pointer around is pretty cheap after the memory it points to has been allocated. So in some cases, using a pointer receiver, even if you’re not mutating it, can be a better choice.

###### Caution

In many programming languages (including Go), it’s not always possible to determine whether something is allocated on the stack or heap just by reading the code. A lot of other factors and optimizations (many of which are implementation-specific) influence this decision but are well beyond the scope of this chapter.

Unfortunately, it’s not possible to give a one-size-fits-all answer when it comes to performance analysis. If performance is important to you, explore the use of profilers to identify areas in your program that can be optimized. For most use cases, especially those that pertain to emerging network automation programmers, this is not something you need to worry about too much. Instead, use this general guideline when you define your own methods: use pointer receivers if you need to mutate the original value, and use value receivers if you don’t.

Next, we’ll explore a powerful feature of Go that allows us to create far more flexible APIs while retaining the benefits of a strict type system: interfaces.

## Interfaces

As you saw in previous examples, functions can use structs as parameter types, allowing callers to pass more complex types into functions instead of the simpler built-in types like `int` or `string`. However, using strictly defined types like this (also known as *concrete types*) can be inflexible.

Imagine you’re designing a function to print the hostname of a network device. You may already have a custom type defined (say, `Router`), which includes the `hostname` field, as well as some fields that might be relevant to routers in particular (say, a list of VRFs). [Example 7-47](#go-function-concrete-type) shows this idea in action.

##### Example 7-47. Using a concrete type as a function parameter

```
type Router struct {
    hostname string
    vrfs     []string
}

// This function takes a concrete type (the "Router" struct)
// and therefore, no other type can be used when calling this
// function.
func printHostname(device Router) {
    fmt.Printf("The hostname is %s\n", device.hostname)
}
```

This approach has one major drawback: you can use the `Router` type only when passing in the `device` parameter. If you had other types (say, `Firewall` or `Switch`), even if they had a `hostname` field, you could not use them in this case. You’d end up having to create different functions for each parameter type you wanted to be able to use, which can get messy. Is there a better way?

There is! In cases like these, you often don’t actually require a specific type, but only a particular behavior that you expect that type to have. In this example, you don’t care about the parameter’s type, but only that it has a hostname. While today there’s no way in Go to allow any type with a particular field (this is somewhat nuanced situation we explore in [“Generics”](#generics)), there *is* a way to allow any type that implements a particular set of *methods*. This is where interfaces come in.

*Interfaces* allow you to describe the behavior you want a particular type to have. They mandate a set of one or more methods (with their parameter and return types as applicable), and instead of using this concrete type when declaring your function parameter, you can use this interface type. Any concrete type can be used as long as it implements the method requirements described by that interface. A concrete type that implements all the methods required by an interface is said to have “satisfied” or “implemented” that interface. [Example 7-48](#go-function-interface-type) shows the use of interfaces to capture any concrete type that implements the `GetHostname()` method.

##### Example 7-48. Interface type as a function parameter

```
type Hostnamer interface {             
    GetHostname() string
}

type Router struct {
    hostname string
    vrfs     []string
}

func (r Router) GetHostname() string { 
    return r.hostname
}

func printHostname(device Hostnamer) { 
    fmt.Printf("The hostname is %s\n", device.GetHostname())
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This interface type describes any concrete type that implements a `GetHostname()` method that has no parameters, and a single `string` return type.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This method allows the `Router` type to satisfy the `Hostnamer` interface.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This function uses the `Hostnamer` interface for the `device` parameter, so any type that implements that interface can be used.

The reason this is useful is that you are now no longer required to use only the concrete type `Router`. You can use any type that satisfies the `Hostnamer` interface. For instance, the `Firewall` and `Switch` types in [Example 7-49](#go-interface-additional-concrete-types) also implement the `Hostnamer` interface.

##### Example 7-49. Additional concrete types for the `Hostnamer` interface

```
type Switch struct {
    hostname string
    vlans    []int
}

func (s Switch) GetHostname() string {

    // There's no rule that says we **have** to return r.hostname directly.
    // What we do inside the method doesn't affect whether it implements
    // the Hostnamer interface. We can give the hostname a prefix of "switch-"!
    return fmt.Sprintf("switch-%s", s.hostname)
}

type Firewall struct {
    hostname string
    zones    []string
}

func (f Firewall) GetHostname() string {
    return fmt.Sprintf("firewall-%s", f.hostname)
}
```

Each of these concrete types satisfies the `Hostnamer` interface so they can all be used as a parameter for `printHostname()`.

The *contents* of the methods required by this interface don’t matter; what matters is the method signature. This is why each of the `GetHostname()` methods shown in [Example 7-49](#go-interface-additional-concrete-types) can do things like prepend a prefix of `switch-` or `firewall-` if desired before returning a value. This means you have great flexibility in the kind of behavior that each of these types exhibits.

###### Note

In Go, satisfaction of an interface is checked at compile time. Therefore, if you try to use a concrete type for an interface parameter, but that type doesn’t satisfy that interface, your program will fail to compile. However, this check is done implicitly. The only way the Go compiler will know to even bother checking for whether a type satisfies a given interface is if your program tries to actually use that type to satisfy an interface parameter, as you saw in `printHostname()`. This is in contrast to other languages like Rust or Java, which require you to explicitly declare that a given type satisfies an interface or trait, even if it’s never used in such a context.

Now, let’s backtrack a little bit to our discussion on method receivers. Recall that these are implicitly passed parameters that provide a handle to the instance of an object on which that method is defined. You should also remember that you can have value and pointer receivers, and that each has pros and cons.

Generally speaking, when you’re *calling* a method, you don’t have to care about whether it’s defined using a value or pointer receiver. This is an implementation detail that doesn’t change the way methods are called. However, in one important exception, you still might need to do something a bit different, and it comes into play when you’re using interfaces, which we’ll explore next.

Let’s build on the previous examples and define a new interface `Trimmable`, which includes the same method from your `Hostnamer` interface but adds a second method `TrimHostname()`. You’ll then implement the `TrimHostname()` method on your `Router` type so that it is able to satisfy the `Trimmable` interface. Finally, you’ll create a new `printHostnameTrimmed()` function that accepts a parameter of this interface type `Trimmable`, as well as an integer to specify the maximum length for your hostname—anything over this will be trimmed. This is shown in [Example 7-50](#go-interface-pointer-receiver).

##### Example 7-50. Implementing the `Trimmable` interface with a pointer receiver method

```
type Trimmable interface {                                             
    TrimHostname(int)
    GetHostname() string
}

func (r *Router) TrimHostname(length int) {                            
    if len(r.hostname) > length {                                      
        r.hostname = r.hostname[:length]
    }
}

func printHostnameTrimmed(device Trimmable, trimLength int) {
    device.TrimHostname(trimLength)                                    

    fmt.Printf("The device hostname trimmed to %d characters is %s\n", 
        trimLength, device.GetHostname())
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

As we can see, interfaces can specify more than one method.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Remember, when mutating the fields of the receiver, we usually want to use a pointer receiver. Otherwise, we’ll just mutate a copy of the receiver value.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This syntax trims the string so that it’s no longer than the `length` parameter. Of course, if it’s already shorter, we don’t need to do anything.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`Trimmable` requires the `TrimHostname()` method to be defined, so we know we can use it here.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

`Trimmable` also uses the `GetHostname()` method so we can use this to retrieve the result after we’ve trimmed it.

What happens if we create an instance of `Router` and try to pass it to `printHostnameTrimmed()`? This is exactly what we do in [Example 7-51](#go-interface-value-method-set).

##### Example 7-51. Compilation error—`Router` does not implement `Trimmable`

```
rtr := Router{hostname: "rtr1-dc1"}

// Fails to compile!
//
// ./10-interfaces.go:23:23: cannot use rtr (variable of type Router) as
//      type Trimmable in argument to printHostnameTrimmed:
// Router does not implement Trimmable (TrimHostname method has pointer receiver)
printHostnameTrimmed(rtr, 4)
```

This code fails to compile! The error message you get from the compiler is also somewhat cryptic, indicating that `Router` does not implement the `Trimmable` interface.

This is a bit misleading because there’s nothing actually wrong with the way you defined the `TrimHostname()` method on `Router`. On paper, this method should allow the `Router` type to satisfy the `Trimmable` interface. Rather, the problem is with what you passed in to `printHostnameTrimmed()`.

In Go, the *method set* of a type determines which methods can be called on that type. A we’ve discussed in earlier examples, types can be represented in more than one form—values, pointers, and now interfaces. The method set available depends on which of these you’re dealing with. In [Example 7-51](#go-interface-value-method-set), you’re passing a *value* to `printHostnameTrimmed()`. However, the method set for such a value does not include methods defined with a pointer receiver; it’s as if your `TrimHostname()` method doesn’t exist! This is why the compiler believes you haven’t satisfied the `Trimmable` interface.

In constrast, the method set of a *pointer* to a type includes not only all the methods with a value receiver type, but also the methods with a *pointer* receiver type, such as `TrimHostname()`. To use `Router` to satisfy `Trimmable`, you must pass a pointer, rather than a value, to `printHostnameTrimmed()`. Fortunately, this is easy to do, as shown in [Example 7-52](#go-interface-method-method-set).

##### Example 7-52. Passing a pointer to `Router` as `Trimmable`

```
// We can create a pointer to a value by using the ampersand symbol. Whereas rtr was
// type Router, rtrPointer is type *Router (pointer of type Router)
rtrPointer := &rtr

// This works, because we're passing a pointer (*Router) to printHostnameTrimmed()
// rather than a value. This means the method set now includes the method required
// to satisfy Trimmable
printHostnameTrimmed(rtrPointer, 4)

// We could also skip defining a separate variable and do this all in one step
printHostnameTrimmed(&rtr, 4)
```

You’ve learned that, with interfaces, you can still benefit from the compile-time safety of a static type system while also creating the flexibility needed to create reusable and ergonomic APIs. Interfaces are in use in all kinds of Go programs and libraries. Many of the functions you use from Go’s standard library accept interface parameters.

This wraps up the more fundamental concepts in Go. With the concepts we’ve covered thus far, you’ll be well equipped to start your Go journey. The next section covers a few concepts that are a little more advanced but crucial for understanding how to use Go most effectively.

# Advanced Concepts

The previous sections have mostly focused on fairly basic Go concepts; these are things you need to know if you’re going to be productive with Go. Some of these concepts are easier to understand than others, to be sure; while loops and conditionals are second nature if you come from Python, for example, interfaces and strict type systems can be difficult if you’ve never been exposed to them before. In either case, you’ll likely need to build a solid understanding of all these concepts to be productive with Go in just about any capacity.

This section dives into some slightly more advanced topics. This isn’t to say you don’t need to know these topics, or that you’ll never run into them, but they do require a bit more effort to truly master than can be covered in a single subsection in this book. As a result, the coverage of these topics and the examples provided are not comprehensive, but rather a brief introduction.

The goal of this section is to introduce these concepts and explain as simply as possible why they’re important—especially within the context of network automation. With this foundation, you can build a more detailed understanding by using the numerous fantastic resources out there. We cover a few of these resources at the end of this chapter.

## Concurrency

If you’ve heard about Go, you’ve probably also heard that one of its strengths is concurrency. But what does this mean?

When you write scripts or programs to perform some kind of automation workflow, you typically start out writing a series of tasks to be executed serially; in other words, do task A, then task B, then task C, as shown in [Figure 7-3](#go-serial-tasks).

![npa2 0703](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0703.png)

###### Figure 7-3. Executing tasks serially

*Concurrency* is a program’s capability to handle multiple tasks at the same time. This allows us to do things like execute tasks A and B simultaneously, wait for them to finish, and only then execute task C, as illustrated in [Figure 7-4](#go-concurrency-visualized).

![npa2 0704](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0704.png)

###### Figure 7-4. Executing tasks concurrently

Concurrency is frequently brought up when discussing Go’s strengths for two reasons. First, Go includes native support for concurrency (it’s built into the language itself, as opposed to being available only via third-party libraries). Second, the way Go exposes concurrency primitives is remarkably simple, compared to how it’s done in other languages.

Given that concurrency is one of Go’s most popular features, do you *have* to learn concurrency to learn Go? Certainly not, in the same way that it’s possible to become quite proficient in Python without learning one of the concurrency frameworks in that language (though [Chapter 6](ch06.html#python) covers these topics, if you’re interested). Perfectly stable and efficient programs are deployed to production all the time that do not make use of concurrency.

Like most concepts we discuss in this book, concurrency is simply a tool to solve a particular set of problems. While Go aims to make concurrency as simple as possible, there’s still something to be said for avoiding the added complexity that it will inevitably bring. However, as with any tool, sometimes it’s the right one for the job, and it’s important to be aware of it as well as the context in which it shines.

The primary building block of concurrency in Go is the goroutine. A play on the established term coroutine, goroutines are lightweight threads that allow you to execute a function or method in parallel to the rest of your code. Creating a goroutine is incredibly easy, as you’re able to start one by simply prepending the word go before invoking a function or method; see [Example 7-53](#go-concurrency-goroutine).

##### Example 7-53. A simple goroutine

```
// This call to time.Sleep() will "block", meaning it will halt execution
// of the rest of this program until the timer expires.
time.Sleep(1 * time.Second)

// This call to time.Sleep() will not block execution of this program,
// because it is launched as a goroutine. The timer will still count down,
// but this will happen in a separate lightweight thread, so the following
// instruction(s) will execute immediately.
go time.Sleep(10 * time.Second)

// We will see this immediately - not after 10 seconds.
fmt.Println("Program finished!")
```

However, this code isn’t very useful because the program will end before the goroutine is able to finish. Typically, after launching a concurrent task using a goroutine, you should wait for that goroutine to complete before moving forward. This approach is common when launching many goroutines at once, which you might do when you want to perform a certain number of similar tasks, all in parallel. A common tool for this situation is the `WaitGroup`, found in the `sync` package. This is essentially a counter that keeps track of the number of goroutines and then blocks execution until they all finish, as shown in [Example 7-54](#go-concurrency-waitgroup).

##### Example 7-54. Waiting for goroutines to finish

```
var wg sync.WaitGroup
var numGoroutines = 5

wg.Add(numGoroutines)                 

for i := 1; i <= numGoroutines; i++ { 
    go func(i int) {
        defer wg.Done()               

        fmt.Printf("Goroutine started with duration of %d seconds\n", i)
        time.Sleep(time.Duration(i) * time.Second)
        fmt.Printf("%d second goroutine finished!\n", i)
    }(i)
}

wg.Wait()                             

fmt.Println("Program finished!")
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `Add()` method allows us to configure the wait group with the number of goroutines to wait for.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This loop allows us to launch all the goroutines in quick succession.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This will decrement (subtract) the wait group by a value of 1. Remember, `defer` statements run at the *end* of a function.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The `Wait()` method will block execution until all of the goroutines complete. Remember, we set the number of goroutines to wait for via the `Add()` method.

[Example 7-55](#go-concurrency-waitgroup-output) shows the output from this program. Although the goroutines are started in no particular order (the wait duration printed for each appears random), they finish in chronological order because each has a different sleep value. What’s more is that because of your wait group, your program doesn’t exit until all the goroutines have finished.

##### Example 7-55. The output after waiting for goroutines to finish

```
~$ ~go run 11-concurrency.go
Goroutine started with duration of 5 seconds
Goroutine started with duration of 3 seconds
Goroutine started with duration of 4 seconds
Goroutine started with duration of 1 seconds
Goroutine started with duration of 2 seconds
1 second goroutine finished!
2 second goroutine finished!
3 second goroutine finished!
4 second goroutine finished!
5 second goroutine finished!
Program finished!
```

Another common method of synchronizing goroutines is accomplished through the use of *channels*. Channels are commonly used to communicate values between goroutines. In addition, channels block execution until the value you’re sending is received by the other goroutine. This gives you the same synchronization power as with wait groups, but in more than one place, while also communicating an actual value across the goroutine boundary. Quite powerful! [Example 7-56](#go-concurrency-channels) shows channels in action.

##### Example 7-56. Synchronizing goroutines with channels

```
fChan := make(chan float32)      

getDeviceCPU := func() float32 { 
    time.Sleep(250 * time.Millisecond)
    return rand.Float32()
}

go func(iChan chan float32) {    
    for {
        cpu := getDeviceCPU()

        if cpu >= 0.8 {          
            iChan <- cpu         
        }
    }
}(fChan)

for {                            
    fmt.Println(<-fChan)          
}
// Output:
// 0.9405091
// 0.81363994
// 0.8624914
// 0.865335
// 0.975241
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Channels have a type (in this case, `float32`) as well as a length. By omitting the length parameter to `make()`, we’re creating an unbuffered channel, which has a length of 0.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

`getDeviceCPU()` simulates an API call to a network device to get the current CPU utilization.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Here, we’re doing a fairly common task of retrieving a device’s CPU via an API call. We want to do ongoing monitoring (and keep sending values into the channel), so we’ll do this in an infinite loop.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

We don’t really care about values less than 0.8. But for any higher values, let’s notify the main goroutine by sending those values on the channel.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

The send syntax places the channel on the *left* side of the `<-` operator. Remember, this will block execution of the goroutine until you receive a value from this channel in the main goroutine.

![6](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/6.png)

This is an infinite loop so that the program continually receives values from the channel.

![7](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/7.png)

Remember, channels allow for synchronization of goroutines, as well as conveying values. When receiving a value here, we know that the goroutine is sending a value at the same time. This will block execution of this main goroutine until the goroutine we launched earlier sends a value into the channel.

![8](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/8.png)

The receive syntax places the channel on the *right* side of the `<-` operator.

###### Caution

Channels can be created with a length greater than 0. These are known as *buffered channels*, and unlike unbuffered channels, they block execution on send operations only if their buffer is full. Unbuffered channels, effectively having no buffer, always block on a send operation until that value is received from the channel. While buffered channels have their use cases, they do dull the synchronization benefits of channels a bit, and as a result, they are not as popular of a choice in the broader Go community. A common convention is to default to using unbuffered channels and to use buffered channels only if you know you require them.

In [Chapter 10](ch10.html#apis), you will see additional, practical examples of goroutines and channels in action, as these are helpful when working with modern network automation RPC frameworks like gNMI.

Goroutines may require access to shared resources. Often the most practical solution is to allow goroutines direct access to resources managed in other goroutines, rather than through channels or a similar mechanism. This is often done by passing a pointer (rather than a value) into a goroutine or into popular reference types like maps or slices. As you saw with methods during our exploration of pointer and value receivers, pointers allow you to pass around a handle to the same region in memory.

However, when writing concurrent code as you have been with goroutines, you must be careful. Concurrent access to shared resources should be done with care. For instance, if Go detects that multiple goroutines are trying to write to a map at the same time, it will trigger a `panic`, and your program will crash.

To avoid this, you must ensure that only one goroutine is actually accessing a shared resource at a time. A popular choice for accomplishing this is the *mutex*, which works in the same way you might check out a book from the library. When you want to read a book, you check it out. Then, you read it; and while you’re reading it, others are waiting for it to become available. When you check the book back in, other people are able to repeat the same process in order to read it for themselves.

A mutex works much the same way: when you want to access a shared resource, you `Lock` the corresponding mutex (check out the book). When you’re finished, you `Unlock` the mutex (check the book back in). In [Example 7-57](#go-concurrency-mutex), we are monitoring the CPU utilization of several network devices concurrently, and updating a shared map where these values are stored and in turn printed to the console.

##### Example 7-57. Protecting shared resources with a mutex

```
var cpuMap = make(map[string]float32)  
var cpuMapMut = sync.Mutex{}

getDeviceCPU := func() float32 {       
    return rand.Float32()
}

monitorFunc := func(hostname string) { 
    for {
        cpu := getDeviceCPU()
        cpuMapMut.Lock()               
        cpuMap[hostname] = cpu         
        cpuMapMut.Unlock()             
    }
}

go monitorFunc("sw01")                 
go monitorFunc("sw02")
go monitorFunc("sw03")

for {                                  
    time.Sleep(1 * time.Second)
    fmt.Printf("cpuMap: %v\n", cpuMap)
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We’re declaring the map and the mutex. Because they are contained in the outer scope, they can be referenced directly by the goroutines we’ll launch later.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

`getDeviceCPU` simulates an API call to a network device to get the current CPU utilization.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`monitorFunc` is the function that we’ll eventually launch as a goroutine, and it contains the infinite `for` loop as well as the updates to `cpuMap`, including the mutex `Lock` and `Unlock` operations.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

This call will block execution if another goroutine already has a lock. Only when we’re able to successfully acquire a lock in *this* goroutine will execution continue. This is how we can safely write to a map from multiple concurrent goroutines.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

Now that we have a lock on the mutex, we can write to the map safely. Without the mutex (or another similar tool offering the same kind of synchronization), the program might crash when multiple goroutines try to access the map at the same time.

![6](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/6.png)

Don’t forget to unlock the mutex when you’re done so that other goroutines can use it! Sometimes you’ll see `defer` used to call `Unlock()` automatically at the end of the function.

![7](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/7.png)

Launch three goroutines—one for each device.

![8](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/8.png)

Repeatedly print the contents of the map to the terminal.

In Go, mutexes are not tied directly to the shared resource itself; it’s up to you to ensure that you’re accessing the resource only after you’ve acquired a lock (other languages might force you to take a lock before you can even access the resource). It’s common for library authors to wrap all of this lock/unlock logic in functions so that you don’t have to worry about it, but in the event you’re working with your own goroutines and shared resources, the mutex is an important concept to understand.

Goroutines (and concurrency in general) are a powerful, and sometimes necessary, tool when performing the same task on multiple network devices. However, as you can see even in the few preceding examples, using goroutines can get complex, fast. Writing concurrent code—even in a language like Go, which makes it as easy as possible—is about much more than simply prepending a function call with `go`. Creating concurrent code opens you up to a new class of problems that require their own solutions.

In other words, be careful not to introduce concurrency into your program for the wrong reasons. It is not a panacea that will automatically make your program faster. Modern languages like Go are quite fast without concurrency, and you may find that the perceived inefficiency of performing tasks serially (without concurrency) isn’t as problematic for your particular use case as it seemed on paper. That said, sometimes it’s the right tool for the job, and in those cases, you’ll be glad you’re armed with a language like Go, which makes it as approachable as possible, and comes with the tools we’ve discussed in this section.

## Generics

In an earlier section, we talked about interfaces. These enable you to inject a little flexibility into your APIs by requiring a given type to exhibit a certain kind of *behavior*, rather than working only with concrete types like integers, strings, or specific structs. However, this comes with important caveats. For example, interfaces work by requiring a method set—which means that any type used as an interface parameter *must* implement that interface’s methods. If you want your function parameters to flexibly handle a variety of types, but those types don’t implement any methods, interfaces won’t be a good solution.

For quite a long time, this situation was the status quo in Go. However, Go 1.18 introduced *generics*, which is a well-established concept in other programming languages. Just as interfaces did before Go 1.18, generics allow you to have much more flexibility over concrete types—but rather than requiring that a type adhere to a particular method set, they work by specifying a *type set*. This is a broader categorization than method sets, in that they can capture a set of just about any type, not just types that implement a particular method. [Example 7-58](#go-generics) shows generics in actions.

##### Example 7-58. Type flexibility with generics

```
func main() {
    fmt.Println(Min(3, 5))         
    fmt.Println(Min(2.5, 6.3))
    fmt.Println(Min("foo", "fooooo"))
}

type comparable interface {        
    int | float64 | string
}

func Min[T comparable](x, y T) T { 
    if x < y {
        return x
    }
    return y
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Because `Min` uses generic parameters, you can pass a variety of types as parameters to `x` and `y`; in these examples, you’re passing integers, then floats, then strings. Because all of these are listed in the type set declared in the `comparable` interface, this approach works.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Rather than declaring methods in your `comparable` interface, you can specify types that you know can be compared using the `<` operator. This allows you to pass any of these types into `Min()`. This is the upgrade that interfaces received in Go 1.18: they can be used to define method sets and/or type sets.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This declares a generic type `T` that must implement the `comparable` interface. Then, when declaring parameters `x` and `y`, you can reference this type `T`. This means that both `x` and `y` must in turn implement `comparable`. Also, because they’re both generic type `T`, they cannot be different types from each other when the function is invoked. Without generics, you’d either have to use interfaces (and therefore each of these types would have to have methods the interface would match on) or you’d have to create a copy of this `Min()` function for each type we want to be able to pass in (`MinInt`, `MinFloat64`, etc.).

In addition to working on type sets and not just on method sets, generics differ from the traditional use of interfaces in Go in their implementation. Before the introduction of generics in Go, each type in [Example 7-58](#go-generics) would need its own `Min()` function that used concrete types for this comparison (i.e., `MinInt`, `MinFloat64`, etc.). This is actually what the compiler does on your behalf when you compile a program using generics: the compiler creates a copy of that generic function for every concrete type passed in to it. You never see these copies; they’re present only in the resulting binary.

As programmers, we can keep our code simple by dealing only with generic types; this is known as *monomorphization*. This technique retains the benefits of a static type system, but with the flexibility that previously required the use of interfaces with method sets.

###### Caution

In some cases, using generics can be more efficient than the equivalent traditional approach with interfaces and method sets. For instance, when using a traditional interface, your program will have to do a runtime lookup to find the actual concrete type being referenced. With generics, this is unnecessary because the mapping of type to function is done at compile time. Naturally, the size of your program’s resulting binary after compilation will be larger.

However, whether generics *actually* speed up your program in a meaningful way is extremely use-case dependent. The decision of whether to use generics should be first and foremost driven by readability and maintainability concerns, and any perceived performance gains should be backed up with data from profiling your program.

While generics are a useful tool for a certain class of problems, you will almost certainly be able to address any automation use case in Go without them. At the time of this writing, generics are still an incredibly new concept in the Go programming language, and it will take years for the ecosystem and best practices around them to be established. As with any other advanced topic in this section, reach for generics only when you’ve gone through the work of proving you really need them.

Next, we explore how Go code is organized and shared via packages and modules.

# Packages and Modules

As with any programming language, the more code you write in Go, the more you’ll want to organize your code into logical groups. For instance, you may have a set of *.go* files that pertain to interacting with network devices. Then, you may have another set of files for generating config files, and another still for retrieving intended state from your single-source-of-truth platform, and on and on. Eventually, it will become difficult to manage a growing codebase that blurs the lines between these logical groupings.

Packages are one way to solve this problem in Go. Using *packages*, you can create logical groupings to organize your code better. For instance, you might have three packages, given the previous examples: `devices`, `generator`, and `ssot`. [Example 7-59](#go-packages) shows what the filesystem structure of such a package might look like.

##### Example 7-59. Go packages

```
myprogram
├── devices
│   ├── arista.go
│   ├── cisco.go
│   ├── devices.go
│   └── juniper.go
├── generator
│   └── generator.go
├── main
│   └── main.go
└── ssot
    ├── ssot.go
    └── state.go
```

Remember that when you execute a Go program, the `main()` function is invoked automatically. This function must exist within a package called `main` (recall, all the way back to [Example 7-1](#go-first-program), that you declared this by using the `package` keyword). In [Example 7-59](#go-packages), you have a package `main` in addition to the other three. From our code in this package, you can refer to the other three packages when calling their functions or using their types.

You’ve already done this several times throughout this chapter. As mentioned before, functions like `Println()` and `Printf()` are from the `fmt` package, which is part of Go’s standard library (we’ll explain what that means in the next section). Similarly, if the `generator` package included a function `Generate()`, and you wanted to call it from your `main` package, you’d probably call it with `generator.Generate()`.

You may have also noticed that anytime you call a function or use a type from a different package, that function or type always starts with a capital letter. This is because Go uses the capitalization (or lack thereof) to indicate whether the thing being identified should be available outside its package. This applies to a lot of constructs in Go, including functions, methods, structs, interfaces, and even field names. If a given identifier starts with a capital letter, it is known to be *exported* and is usable by code both inside and outside the package in which it’s declared. A lowercase letter means that identifier can be used only from within that package (*unexported*). This is comparable to concepts like *public* and *private* (respectively) in other languages. This syntax allows you to be more precise when defining your package’s API surface—the more stable points of interaction between your package and other programmers who wish to use it.

Packages, however, are just part of the picture. In Go, *modules* describe a collection of packages and are useful for a few things. First, they provide a way to unify a set of related packages into one easily distributable repository. In fact, it’s common to see a Go module located at the root of a corresponding Git repository. This can be particularly useful if you’re developing a Go library for other developers to consume.

Modules play another role, though: they are the mechanism by which Go *manages dependencies*, such as third-party libraries you want to use in your own code. We haven’t talked too much about this yet because all of the prior examples exclusively use the standard library. However, if you want to go beyond the standard library (which you almost certainly will at some point), you’ll need to configure your own module to properly handle the dependencies your code has on other modules. In [“Third-Party Modules and Packages”](#modules_and_pkgs), you’ll learn more about how to work with modules in order to bring third-party code into your project.

At the beginning of this chapter, we make the assertion that Go is an important language to know in the world of network automation, and that a big reason for that is the growing ecosystem of tools and packages that are particularly useful for network automation use cases. Now that you understand the basics of packages and modules, it’s time to explore this a bit further. Let’s look a bit more deeply at some popular packages—those in Go’s standard library as well as those maintained by third parties—that you’ll want to be aware of as you move forward in your journey.

###### Note

Though we do our best in these sections to explore some of the more popular packages you might run into, it’s impossible to cover them all and equally difficult to cover any one of them exhaustively. In addition, the network automation ecosystem in Go is constantly growing and changing, so a large portion of these specific examples will almost certainly change dramatically within the next few years. The goal of this section is to provide you with a repertoire for common network automation use cases. At the end of this section, you will have a solid base upon which you can continue to build as you progress in your journey.

## Standard Library Packages

Programming languages are rarely just a spec and a compiler that converts that spec into machine code. They often come with a set of types and functions used for common tasks. Some of these are provided as *built-ins*, meaning they are baked into the language specification so you don’t need to do anything special to use them.

Go built-ins include types like `int` and `string` but also functions like `make()` and `new()`. Other Go built-ins do require you to import a package in your code, but otherwise don’t require any special installation to be usable. The `fmt` package is a good example; we’ve made liberal use of functions like `Println()` and `Printf()` throughout this chapter, both of which are from the `fmt` package.

###### Tip

This paradigm of built-ins versus standard library is true of many programming languages. As you saw in [Chapter 6](ch06.html#python), for instance, Python has built-ins like `str` and `print()` but also a diverse standard library including packages like `time` and `sys`.

The `fmt` package is one of many considered part of Go’s *standard library* (sometimes abbreviated `stdlib` or `std`). This is a collection of packages that are useful for common tasks you’d need in just about any program you’re writing in Go. These packages also have an extremely stable API, which is required as part of the Go version 1 compatibility guarantee. You don’t have to worry about Go version upgrades breaking code that uses standard library types or functions.

Go has a robust standard library, including several packages that are particularly useful for network automation use cases. We’ve covered a few of these already in this chapter. Again, [`fmt`](https://pkg.go.dev/fmt) is where we find functions like `Println()` and `Printf()`, but is broadly useful for formatted I/O in general. We also used [`sync`](https://pkg.go.dev/sync), which is definitely a package you’ll want to be familiar with if you use concurrency in your programs.

### strings

To start, we’ll explore a few packages that specifically relate to working with string data. If you want to perform tasks like find a substring (such as a prefix or suffix), trim off parts of a string, or otherwise parse string data, your first stop should absolutely be the `strings` package. This package includes many functions that are useful for doing all kinds of common things to parse, edit, and search within strings, and you will almost certainly run into a handful of them in your network automation. [Example 7-60](#go-stdlib-strings) shows some of the more commonly used functions in this package.

##### Example 7-60. Using `strings` to work with…​strings!

```
exampleString := `
Hello network automators! Welcome to Network Programmability and Automation.
`

doesContain := strings.Contains(exampleString, "Automation")          
fmt.Println(doesContain) // output: true

substringIndex := strings.Index(exampleString, "Welcome")             
fmt.Println(substringIndex) // output: 27

strSplit := strings.Split(exampleString, " ")                         
fmt.Println(strSplit[4]) // output: "Welcome"

strTrimmed := strings.TrimSpace("    Automation!    ")                
fmt.Println(strTrimmed)      // output: "Automation!"
fmt.Println(len(strTrimmed)) // output: "11"

strReplaced := strings.ReplaceAll(exampleString, "network", "gopher") 
fmt.Println(strReplaced)
// output:
// "Hello gopher automators! Welcome to Network Programmability and Automation."
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`Contains()` returns `true` or `false`, depending on whether the string (first parameter) contains the indicated substring (second parameter).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

`strings.Index()` returns the index (location within the string) of the first instance of the substring.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`strings.Split()` creates a slice of strings (`[]string`) from the input string based on a provided delimiter. The following example uses a space as a delimiter, which will result in each word of the input string being placed in its own slice element. We can perform the reverse of this operation by using `strings.Join()`, which creates a single string from a `[]string`, joined with a delimiter of your choice.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`strings.TrimSpace()` is a super handy function for easily removing extra spaces at the beginning or end of a string. Plenty of other trim functions are in `strings`, each with its own specialized use cases, including `Trim()`, `TrimPrefix()`/`Trim​Suf⁠fix()`, and `TrimLeft()`/`TrimRight()`.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

`strings.ReplaceAll()` can replace all instances of a given substring with another string of our choice. If we want to replace only a limited number of instances, we can use `strings.Replace()`.

### strconv

[Example 7-61](#go-stdlib-strconv) shows another strings-related (but much more narrowly focused) package: `strconv`. This contains functions for parsing and converting between strings and other built-in types like integers.

##### Example 7-61. Converting to and from strings by using `strconv`

```
// strconv.Atoi converts a string to an integer. It returns the integer
// value but also an err, as the parse might fail because of integer overflow,
// non-integers, etc.
i, err := strconv.Atoi("-42")
if err != nil {
    fmt.Printf("Unable to convert string to integer: %s\n", err)
} else {
    fmt.Printf("Parsed integer is %d\n", i)
}

// strconv.ItoA performs the reverse, converting an integer to a string.
// This cannot fail, so we see only one return type from this function.
i42 := strconv.Itoa(42)
fmt.Printf("i42 as a string is %s\n", i42)
```

`strconv` has several other functions, including those that work with other types like booleans and floating-point numbers.

### regexp

Inevitably, especially in the world of network automation, the somewhat basic string-searching functions in `strings` just aren’t sufficient, and we need something a bit more advanced. In any language or tool, this generally means the introduction of *regular expressions* (*regexes*) for more advanced string-search or even-replacement tasks. Fortunately, Go’s standard library has the `regexp` package, which includes robust regex support. [Example 7-62](#go-stdlib-regexp) contains practical examples of using this package to perform common parsing tasks in network automation.

##### Example 7-62. Using regular expressions in Go with the `regexp` package

```
outputStr := `
eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
    inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
    ether 02:12:2a:24:5b:98  txqueuelen 0  (Ethernet)
`                                                                

re, err := regexp.Compile(`([0-9a-f]{2}:){5}[0-9a-f]{2}`)        
if err != nil {
    panic(err)
}

fmt.Println(re.MatchString(outputStr))                           
// output: true

fmt.Println(re.FindString(outputStr))                            
// output: 02:12:2a:24:5b:98

fmt.Println(re.ReplaceAllString(outputStr, "00:00:00:00:00:00")) 
// output:
//
// eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
//     inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
//     ether 00:00:00:00:00:00  txqueuelen 0  (Ethernet)
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

`outputStr` is a large multiline string you can parse with the `regexp` package. A variable containing contents retrieved from a file or from an API call would work just as well.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

This regex matches MAC addresses. `regexp.Compile()` returns a `*regexp.Regexp`, which we can use for later tasks. All following tasks are done using methods of this returned instance `re`. This is a common step in many implementations of regexes, including in languages other than Go. This helps ensure that you have a valid expression before continuing.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

We can use the `MatchString()` method of the returned instance `re` to get a basic boolean `true`/`false` to indicate whether any substring in `outputStr` matches your regular expression.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`FindString()` goes a step further and returns the first specific substring that matches our expression. Other methods like `FindAllString()` and `FindAllStringIndex()` can be used to find all instances that match, returning a slice of strings (`[]string`) that can be inspected afterward or perhaps even iterated over.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

`ReplaceAllString()` allows us to replace all instances that match the expression with a given string literal. In this case, we’re overwriting the MAC address with all 0s, leaving the rest untouched.

### encoding

A common task in Go, especially in network automation, is the serialization and deserialization of data structures to and from formats like JSON and XML. This is often necessary to send/receive data between disparate systems—for instance, the HTTP API on your favorite network device. For this, as shown in [Example 7-63](#go-stdlib-encoding), the `encoding` package is invaluable—and in particular, `encoding/json` and `encoding/xml` for working with JSON and XML, respectively.

##### Example 7-63. JSON/XML serialization with the `encoding` package

```
type NetworkInterface struct {            
    Name  string `xml:"name" json:"name"` 
    Speed int
}

type Device struct {
    Hostname   string
    Interfaces []NetworkInterface
}

r1 := Device{
    Hostname: "r1",
    Interfaces: []NetworkInterface{
        {
            Name:  "eth0",
            Speed: 1000,
        },
    },
}

jsonOut, err := json.Marshal(&r1)
if err != nil {
    panic(err)
}
fmt.Println(string(jsonOut))
// output:  {"Hostname":"r1","Interfaces":[{"name":"eth0","Speed":1000}]}

xmlOut, err := xml.Marshal(&r1)
if err != nil {
    panic(err)
}
fmt.Println(string(xmlOut))
// output:  <Device><Hostname>r1</Hostname><Interfaces>
//             <name>eth0</name><Speed>1000</Speed></Interfaces></Device>
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `encoding` package (and generally any package that performs serialization/deserialization) will work with only exported types and fields (which start with a capital letter).

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

You may wonder about this strange string after this field. This is called a *struct tag*, and while not required, it is extremely common to see these for structs that will be used for serialization/deserialization purposes, such as to/from JSON or XML. Generally, struct tags are just metadata; they have no implicit purpose on their own. However, both the `xml` and `json` package can use these if present to specify a field name that is different from the actual struct field’s name.

[Chapter 8](ch08.html#dataformats) covers JSON and XML in much more detail, but [Example 7-63](#go-stdlib-encoding) will help you get started working with these extremely popular data formats.

### net

The Go standard library includes a robust networking package known as `net`. Here, you can find all kinds of useful types and functions for working with the network stack, from setting up an arbitrary TCP connection to full-blown application-level network interactions.

As you’ll see in [Chapter 10](ch10.html#apis), it’s common for a REST API to have a companion client-side library that you can integrate with easily. However, this isn’t always the case, and sometimes you have to query an HTTP API directly. A specific subset of Go’s `net` package known as `net/http` has an easy-to-use HTTP client, which you use in [Example 7-64](#go-stdlib-net-http) to query a public HTTP API.

##### Example 7-64. Querying an HTTP API with the `net/http` package

```
resp, err := http.Get("https://api.ipify.org?format=json")                   
if err != nil {
    panic(err)
}
defer resp.Body.Close()
body, err := io.ReadAll(resp.Body)
if err != nil {
    panic(err)
}

ipifyResponse := struct {                                                    
    IP string `json:"Ip"`
}{}
err = json.Unmarshal(body, &ipifyResponse)
if err != nil {
    panic(err)
}
fmt.Println(ipifyResponse.IP)

client := &http.Client{}                                                     
req, err := http.NewRequest("GET", "https://api.ipify.org?format=json", nil) 
if err != nil {
    panic(err)
}
req.Header.Add("My-Header", `foo`)                                           
resp, err = client.Do(req)                                                   
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `net/http` package includes high-level functions like `Get()` for performing requests easily with some sensible defaults.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

We can use what you learned in [Example 7-63](#go-stdlib-encoding) to unmarshal the raw JSON string into a struct type.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Sometimes we need a bit more control than these high-level functions offer. For instance, we may need to send specific HTTP headers with our request. This requires that we create our own `Client` and `Request`.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

The method (`GET`) is defined here as a parameter to `http.NewRequest`, as is the URL.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

Headers are defined on the request object after they’re created.

![6](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/6.png)

Once prepared, the request is passed as a parameter to `Do()`, which is a method on `client` that we created earlier.

This is a brief example of one of the more common tasks you’ll run into, but the `net/http` package has far more utility than this demonstration. For instance, we explored the use of this package to query an HTTP API, but you can also use this package to make your own HTTP API server! You’ll also use this package in [Chapter 10](ch10.html#apis) to query a RESTCONF server on a network device.

Zooming out a bit, the `net` package itself also has a few useful things to know about. You can spin up your own raw TCP client or server, perform DNS resolution, and query the local system’s network interfaces. However, one of the most likely use cases you’ll have for this package is the ability to work with IP addresses and networks. [Example 7-65](#go-stdlib-net) shows a few helpful examples of these types and functions in action.

##### Example 7-65. Working with IP addresses and networks via the `net` package

```
var ipFromByteSlice net.IP = []byte{192, 168, 0, 1} 
fmt.Println(ipFromByteSlice)

addrOne := net.ParseIP("192.168.0.1")               
addrTwo := net.ParseIP("2001:db8::1")
fmt.Println(addrOne)
fmt.Println(addrTwo)

network := net.IPNet{                               
    IP: net.ParseIP("192.168.0.0"),
    Mask: net.CIDRMask(24, 32),                     
}

fmt.Println(network.Contains(addrOne))              
 // output: true
fmt.Println(network.Contains(addrTwo))
 // output: false
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `net.IP` type is used to represent IP addresses. While it includes many helpful methods, at its core it is really just a slice of bytes, so we can initialize a `net.IP` instance by constructing this byte slice ourselves.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

For convenience, `net.ParseIP()` allows us to construct IP instances with a string as input. This is a much more common way of constructing `net.IP` instances. You’ll notice that either IPv4 or IPv6 addresses can be passed here. This is because of the flexibility of the byte slice representation, with a length suited to the address being represented.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`net.IPNet` is used to represent a network/subnet. It is defined by two fields: an IP (`net.IP`) and a mask (`net.CIDRMask`). Like `net.IP`, `net.IPNet` is v4/v6 agnostic.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

We’re defining a bitmask that’s 24 bits long, with a total size of 32 bits. In other words, this is the v4 subnet mask `255.255.255.0`.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

We can then use the `Contains()` method on `network` to easily determine if a given IP address is a member of this network.

The `net/netip` package is a relatively recent addition to the standard library. Initially developed as a [third-party module by Tailscale](https://oreil.ly/b7IW9), this package was moved into the standard library in Go 1.18. The package contains alternatives to the `net.IP` type and related functions we explored in [Example 7-65](#go-stdlib-net). [Example 7-66](#go-stdlib-netip) shows the use of this new `netip.Addr` type and its associated functions.

##### Example 7-66. The `net/netip` package

```
// ParseAddr allows us to parse an IP address (v4 or v6) from a string. Once we
// have the resulting netip.Addr type, we can call helpful methods like
// IsGlobalUnicast() or IsLoopback() to quickly identify properties of the
// address we parsed.
ipv6, err := netip.ParseAddr("2001:db8::1")
if err != nil {
    panic(err)
}
fmt.Println(ipv6.IsGlobalUnicast()) // output: true

// ParseAddr does work for IPv4 addresses as well, but an alternative is the
// AddrFrom4() function, which allows us to pass the address as a 4-length byte
// array, removing the need for error handling (no parsing is being done here).
fmt.Println(netip.AddrFrom4([4]byte{127, 0, 0, 1}).IsLoopback()) // output: true

// We can parse entire prefixes from a string using ParsePrefix()
prefixString := "192.168.0.0/24"
prefix, err := netip.ParsePrefix(prefixString)
if err != nil {
    panic(err)
}
```

###### Note

At the time of this writing, the remainder of the original third-party `netaddr` module that didn’t make it into Go’s standard library in 1.18 is available as [`netipx`](https://oreil.ly/QSzjF). This includes functions and types for working with ranges of IP addresses, which can be helpful if you want to iterate over all addresses in a given prefix. This might also be made available in Go’s standard library in the future.

### time

You’d be hard-pressed to find a use case that doesn’t require the `time` package, as working with time is an extremely common element of just about any network automation workflow. [Example 7-67](#go-stdlib-time) illustrates uses frequently found in network automation projects. For instance, pausing execution for a certain period of time (for instance, to wait for another task to complete) is, of course, something we must rely on frequently. Other tasks like comparing date/times, or triggering events based on a period of elapsed time are also invaluable tools to add to any network automation-related Go program.

##### Example 7-67. Working with the `time` package

```
now := time.Now()                                                      
fmt.Println(now)

moonLanding := time.Date(1969, time.July, 20, 20, 17, 45, 0, time.UTC) 

var oneSecond time.Duration = 1000000000                               

tenSeconds := 10 * time.Second                                         

fmt.Println(time.Since(moonLanding))                                   

time.Sleep(tenSeconds)                                                 
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `time.Time` type is a singular point in time. One of the most common ways of getting this is via the `Now()` function, which returns the current time.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

However, we can create an instance of `time.Time` representing any arbitrary date/time.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`time.Duration` is a type alias for `int64`, and it’s used to represent a time duration in nanoseconds. The following example is equivalent to 1 second of duration.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

However, the `time` package also includes convenient constants such as `time​.Sec⁠ond`, which make it easier to represent durations in a more readable way.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

`time.Since()` is a common way to derive a `Duration` between an event in the past and the current time.

![6](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/6.png)

Finally, the ever-useful `Sleep()` function—you guessed it—sleeps the current goroutine for the specified `Duration`.

In addition to these fairly common tasks, you can expand on what you learned in [“Concurrency”](#concurrency), and use functions like `time.After()` in conjunction perhaps with other channels to build more complex event-handling systems.

### os

The `os` package is extremely useful for working with underlying operating system concepts, like working with reading and writing files, as shown in [Example 7-68](#go-stdlib-os-files).

##### Example 7-68. Reading and writing files with the `os` package

```
// Reading a text file is easy with os.ReadFile
dat, err := os.ReadFile("sampleconfig.yaml")
if err != nil {
    panic(err)
}
fmt.Println(string(dat))

// Next, let's write a file. Here we're first marshaling a struct into JSON
// so we can write the result to the file.
jsonOut, err := json.Marshal(struct {
    Hostname   string
    Interfaces []string
}{
    "sw01",
    []string{"eth0", "eth1", "eth2"},
})
if err != nil {
    panic(err)
}
// Just like ReadFile returns a []byte value, so does WriteFile require
// this type as an argument. Fortunately that's exactly what json.Marshal returns
err = os.WriteFile("sampleconfig.json", jsonOut, 0644)
if err != nil {
    // Here, instead of calling panic(), we can use os.Exit to more gracefully exit
    // our program, while returning an error code to the operating system.
    fmt.Printf("Unable to write file: %s\n", err)
    os.Exit(1)
}
```

It can also be handy for returning exit codes as we exit our program and handling incoming signals, illustrated in [Example 7-69](#go-stdlib-os-signals).

##### Example 7-69. Handling signals with the `os` package

```
sigs := make(chan os.Signal, 1)                      

signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM) 
go func() {                                          
    for {
        fmt.Println("Doing some work...")
        time.Sleep(1 * time.Second)
    }
}()

<-sigs                                               

fmt.Println("exiting")                               
os.Exit(0)
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

We can use a combination of packages like `os`, `os/signal`, and `syscall` to handle incoming signals from the operating system. This allows us to more gracefully handle these signals. Here, we’re creating a channel of type `os.Signal`.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

We then pass this channel into `signal.Notify()`, along with a list of signals we wish to handle.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

This line launches a goroutine to simulate doing some actual work.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

If the operating system sends any of the prevously listed signals to our application, this channel will receive this, and the following code will execute. However, until then, it will block, as it is an unbuffered channel.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

Here, we add a simple print statement, but we could add any logic we want, to make sure we take care of any cleanup tasks before the program shuts down.

A few other packages are worth a brief mention:

ioThis is one of those packages that shows up everywhere. We already used this in our exploration of `net/http` in [Example 7-64](#go-stdlib-net-http), as `resp.Body` implements the `io.Reader` interface.

encoding/binaryUsed for encoding to/from binary formats. While we don’t cover this package explicitly, we do cover other binary formats in [Chapter 8](ch08.html#dataformats).

text/templateUsed for Go’s templating functionality, which is powerful. You’ll learn more in [Chapter 9](ch09.html#templating).

Despite the varied and robust examples presented thus far, we’re still only scratching the surface. There’s a lot more to Go’s standard library, and you would be well served to peruse the [full package list](https://pkg.go.dev/std) to see what else comes with Go. For now, let’s turn our attention to the ecosystem of third-party libraries that has emerged to support network automation.

## Third-Party Modules and Packages

While Go does enjoy a robust standard library, it cannot address every use case. Inevitably, you’ll encounter a situation that may be addressed more comprehensively by code that someone else wrote and published to a platform like GitHub. Remember that Go code is distributed via modules, and to use them, you must first explore how to initialize your own code as its own module.

Fortunately, the vast majority of the tooling you’ll need for common development tasks in Go are built right into the same tooling we’ve used this far to run and build our code—and working with modules and third-party dependencies are no exception. [Example 7-70](#go-modules-init) shows how to initialize a new Go module (these commands should be executed within the bash terminal).

##### Example 7-70. Initializing a Go module

```
mkdir myfirstmodule && cd myfirstmodule               
go mod init github.com/oreilly-npa-book/myfirstmodule 
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

This command creates the new directory *myfirstmodule* and then enters into it.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The argument after `go mod init` is the *module path*. It’s really a prefix for the packages that the module contains. You’ll notice that a popular convention is to use the location of the Git repository containing this module; while this isn’t required, it does make it easier for other commands like `go get` to find and download the source for this module.

As a result of running the `go mod init` command, you have a new file *go.mod* in your directory, with some fairly simple contents, showing the module path as well as the version of Go it was initialized with. A newly initialized *go.mod* file will look very similar to [Example 7-71](#go-modules-barebones-go-module).

##### Example 7-71. Bare-bones go.mod file

```
~$ cat go.mod
module github.com/oreilly-npa-book/myfirstmodule

go 1.18
```

Now that you have an initialized module, you can explore the use of third-party libraries in your code. One extremely popular package for structured logging is Logrus. You’ll create a new file *main.go* with the contents shown in [Example 7-72](#go-modules-myfirstmodule-main).

##### Example 7-72. Source of `myfirstmodule` program

```
package main

import (
    "fmt"

    // It's conventional to place third-party dependencies in a separate section,
    // to help distinguish them from standard-library and intra-module imports.
    //
    // You can also optionally specify an alias prior to the package path,
    // which may or may not be different from the original package name. In this
    // case, the logrus package is being aliased to log.
    log "github.com/sirupsen/logrus"
)

func main() {
    vlanIDs := []int{
        100, 200, 300,
    }

    log.Infof("Hello from logrus! There are %d VLANs in the vlanIDs slice.",
        len(vlanIDs))

    fmt.Println("End of program.")
}
```

As you can see, you referred to the `logrus` package within the `import` block of [Example 7-72](#go-modules-myfirstmodule-main). However, you need to do one more thing before your program can compile and run: actually download the `logrus` source code so it can be compiled alongside your program. For this, you can use two particularly helpful `go mod` subcommands, shown in [Example 7-73](#go-modules-tidy-vendor).

##### Example 7-73. Downloading module dependencies

```
# This useful command makes sure that the go.mod file matches what your program
# needs. It will download/add any missing modules, but also remove any unused
# modules as well.
~$ go mod tidy

# By default, modules are downloaded to the system's module cache. However,
# if you want the source for the modules you depend on to be stored alongside
# your code, you can "vendor" them - in this case, these modules will literally
# be stored in a vendor/ subdirectory within your module's directory.
~$ go mod vendor
```

At this point, the *go.mod* file is now much more interesting. Of particular note is the addition of the third-party module you’re depending on, including the module’s version at the time it was added. You can see this updated file in [Example 7-74](#go-modules-updated-go-mod).

##### Example 7-74. Updated go.mod contents

```
module github.com/oreilly-npa-book/myfirstmodule

go 1.18

require github.com/sirupsen/logrus v1.9.0

require golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8 // indirect
```

###### Tip

You will usually notice other modules listed in *go.mod* that aren’t directly referenced in your code—such as those in [Example 7-74](#go-modules-updated-go-mod) that are followed by `// indirect`. These are modules that your *dependencies* rely on. When managing your program’s dependencies, the Go tooling navigates the full tree of dependencies and makes sure they’re all available on the system so that your program can compile.

While you’ll definitely run into other subcommands and tools while working with Go modules, this covers the basics of initializing your own module and importing other third-party modules. However, knowing how to import other modules is just the first step. You now need to learn where to find third-party modules and how to vet them for quality. We’ll also briefly explore a handful of existing third-party modules that you may find useful for network automation in particular.

A great starting point for locating a new module is [*https://pkg.go.dev*](https://pkg.go.dev), which offers a search engine for Go packages and modules. Search for anything you want—maybe “network automation”—and you’ll immediately get a bunch of results for Go packages. From here, you can view the README file for a given module and follow the provided links to the code repository (e.g., GitHub), so you can vet the module more thoroughly for your use cases.

This leads to an interesting question; how to know if a module is “good”? We are often looking to bring in third-party modules so that we can complete an automation project and put it into production, so we have to be somewhat rigorous about the code we add to our services. What does this entail?

Unfortunately, there’s no silver-bullet answer here. You’ll find that most programmers have varying standards for vetting third-party libraries in any language, and this is also true for organizations as a whole. If you’re a solo developer working on a network team for a traditional enterprise, your company might have no established standards. Others with more well-established software practices may have more explicit requirements for qualifying third-party code. As this can be a bit of a rabbit hole, we’ll focus instead on a few common sense guidelines that make sense for most situations:

Code auditabilityWhen you’re bringing a third-party module into your project, it becomes just as much a part of your program as the code you wrote yourself. So, make it a practice to become comfortable with reading others’ code, especially for the modules you’re evaluating. The code, or at the very least, its intent, must be clear; if after an hour or two of reading you still have no idea how the code does what it’s supposed to do, bringing it into your project may not be a good idea.

SuitabilityDoes the module actually do what you want it to? Even for a single use case, there could be several potential options to choose from, each with their own design constraints and trade-offs. Become familiar with these and choose the module that best aligns with your goals.

TestsDoes the module come with tests, (e.g., unit tests)? Are the tests reasonably comprehensive; do they provide suitable validation that the code does what it claims to do? Is there a CI/CD infrastructure in place that ensures these tests are run against the existing code, as well as any new contributions?

API stabilityWhat guarantees does the module offer (if any) around breaking API changes? Particularly new modules that are under active development may be changing frequently, which could cause you to have to update your code when updating the module to a new version. This is not always a bad thing, but it’s something to consider and be aware of before relying on a module.

Active developmentYou may find problems with a module after bringing it into your project, so knowing whether the developers of that module are still active and working on improvements can be helpful. Red flags include things like a backlog of unanswered pull requests or issues/bug reports, or the most recent commits being months or years old. Keep in mind that active development is not a panacea; many high-quality libraries are *feature complete*, meaning they reached their original design goal, and nothing is left to work on.

Again, remember that when you bring a third-party library into your program, it becomes just as much a part of your program as the code you wrote yourself, so it’s important to take this part seriously. Just because a Go module is published on GitHub doesn’t mean it is “good” (or that it even works at all), so don’t skip the due diligence here. Even though the preceding guidelines work particularly well for evaluating Go libraries, they contain good advice for working in just about any language.

Obviously, the types of libraries you need depends greatly on what you’re trying to accomplish. However, to help get you started, the following is a diverse list of popular libraries that can be used to solve some of the more common network automation use cases:

ygotGenerates Go code from YANG models and validates/generates data against these models.

goSNMPWorks with SNMP in Go.

ProtobufWorks with protobuf, a binary serialization format. We cover this must-have library in more detail in [Chapter 8](ch08.html#dataformats) and build on this knowledge when exploring gRPC in [Chapter 10](ch10.html#apis).

goBGPAn open source BGP implementation in Go. Can be used as a standalone routing stack or integrated as a library into your own application.

netlinkInteracts with the Linux networking stack via netlink.

gotextfsmWorks with TextFSM (a text-parsing language).

goeapiWorks with Arista’s eAPI, the programmability option offered on most Arista products.

A few other third-party libraries are extremely common when working with APIs in Go ([Chapter 10](ch10.html#apis) covers these in more detail):

gRPCThis library is a must-have for working with gRPC, a lightweight, modern RPC framework.

gNMIThe official OpenConfig library for working with gNMI, a protocol for config manipulation and state retrieval built on gRPC.

gNMIcA CLI client and collector application for gNMI.

This is by no means an exhaustive list, but it should be enough to get you started. Be sure to begin any exploration or search for libraries with a solid understanding of your core requirements. This will help you find the library that best matches the trade-offs you’re willing to make.

# Summary

We wrote this chapter for the same reason that drives all chapters in this book: to provide you with a properly constrained but still diverse set of tools for solving problems in your network automation journey. You’ll inevitably run into a use case that’s better suited for Python, even after reading this chapter or getting more hands-on experience with Go. This is expected; in practice, there is no room for absolutism in the ever-changing world of network automation or software development as a whole. As they say, “the right tool for the right job.”

That said, Go does strike the sweet spot for today’s network automator: it combines the ease of adoption of a language like Python, with the safety and performance typically associated with much less accessible languages. Even if you don’t consider yourself a programmer, giving Go a chance is worthwhile. You might find it a useful tool to have in your toolchest.

A subject as vast as a programming language is impossible to cover exhaustively in a single chapter. For next steps, we encourage you to get your hands dirty and consider building something in Go as a prototype. For many of us, learning by doing can be a powerful strategy. Additionally, a great new book has been published called *Network Automation with Go* by Nicolas Leiva and Michael Kashin (Packt Publishing). If you want to go deeper with your knowledge of Go, this book would be a great next step. In addition, the [Go Tour](https://oreil.ly/14k2w) is a fantastic way to get your hands dirty with Go right away, all in the browser (no need to install anything).

In [Chapter 8](ch08.html#dataformats), you’ll see a little bit of both Python and Go in action, as we explore the various data formats that you’ll run into in your network automation journey.
