# Chapter 5. Network Developer Environments

As a network engineer, you probably know how important it is to have an optimized working environment. In the physical sense, this might include things like having the right keyboard, sometimes using multiple monitors, and maybe even a standing desk to give you room for stretching out during those long troubleshooting sessions. You may have a bookshelf close at hand so your platform or protocol references are never too far away. This extends to the digital world too: you might have bookmarks to online references, or your network controller’s UI. Maybe you have your favorite terminal emulation tool, set up with scripts and shortcuts to get CLI access to all your network devices quickly.

In the same way, software developers often rely on a series of tools to not only stay productive, but also facilitate the development and eventual deployment of the code they write. Many of these tools are just as useful in a network automation context, and we discuss a few of them in this chapter.

Before we get started, it’s important to talk about some of the benefits you can expect by investing time in building a proper development environment:

Functional validationOne of the main reasons it’s important to build a development environment is so that we know the code we’re writing *actually works*. Professional developers don’t simply write code in Notepad and hope it works. They build using a variety of tools that not only provide feedback on their code while they’re writing it, but also allow them to *run* their code so they can see it working the way they expect.

ConsistencyWhen a developer environment is more formalized and shared among developers on a team, onboarding new team members becomes much easier. While room can be allowed for customization, having all team members use a common set of tools creates a lot less friction when new members are coming up to speed.

TestabilityA formalized developer environment also lends itself to being more conducive to automated testing. For example, if your test suite can be executed with a simple `make test` command, each developer can validate that their own code works locally with ease—and more importantly, so can your CI system. We cover more about this in [Chapter 13](ch13.html#cicd).

This chapter is not meant to specify the “correct” environment, as everyone has their own way of working. Rather, we want to make you aware of some of the key attributes that a productive developer environment might have, as well as dive into a few popular examples that facilitate each of these attributes. From this, you can decide which tools and techniques work best for you or your team.

To that end, we cover a few topics in this chapter:

- Text editors
- Development tools
- Emulation/simulation tools

# Text Editors

Whether you’re developing automation solutions using a full-blown programming language like Python or Go (which we cover in Chapters [6](ch06.html#python) and [7](ch07.html#go)), or with more opinionated tools like Ansible or Terraform (which we cover in [Chapter 12](ch12.html#automationtools)), at the end of the day, you’ll have to do some typing. Even the most opinionated automation tools typically require complex workflows to be defined in some kind of text format like YAML (which we discuss in [Chapter 8](ch08.html#dataformats)), which has its own rules to follow.

The notepad-type of application that may come with your operating system is *technically* capable of allowing you to read and write basic code in a text file, but you’ll quickly find it is woefully inadequate for any practical network automation purposes. To understand this, it’s first necessary to cover some basic requirements you’re certain to have when using a text editor for building out a network automation solution.

No text editor is perfect, and everyone has their own peculiar workflows and preferences. However, any worthwhile text editor should support a core set of requirements, and we discuss these and more in the sections to follow.

Some popular text editors include the following:

Visual Studio CodeColloquially referred to as *VS Code*, this is a free, lightweight graphical editor that is well supported and actively developed by Microsoft. It boasts a large ecosystem of plug-ins. Because of its accessibility and the support available through plug-ins, VS Code has become a popular first choice.

VimThis lightweight and totally customizable text editor has an extremely large ecosystem (it’s been around for a while). Really, it’s the gold standard for text editors (you might notice that other text editors sometimes advertise support for “Vim key bindings/shortcuts”). Using Vim can be intimidating for those not used to relying so heavily on the keyboard to get around, but you’d be hard-pressed to find a more customizable editor.

Sublime TextThis minimalist graphical editor is similar to Visual Studio Code but has been around longer. It includes a free evaluation version, but individual licenses are available for purchase. It also has a healthy plug-in ecosystem.

This is just an abbreviated list. Many other text editors are available to choose from, each with its own pros and cons. There’s really no “best” editor. Each editor comes with its own workflow, features, and ecosystem, which fit everyone differently. Play around with a few options and get started with the one that seems best for you. For the purposes of illustration, many screenshots used in this chapter use Visual Studio Code.

Next, we highlight some specific features that you should consider when evaluating which text editor is right for you.

## Syntax Highlighting

*Syntax highlighting* allows your editor to highlight certain keywords in a given file to make it easier to read, instead of having a bunch of monochrome text on a monochrome background. [Figure 5-1](#developmentenvironments-syntax-highlighting) shows how syntax highlighting can color-code certain keywords and symbols to facilitate reading and writing code.

###### Note

If you’re reading the print edition of this book, the screenshot in [Figure 5-1](#developmentenvironments-syntax-highlighting) is in black-and-white, and therefore the colors used for syntax highlighting aren’t apparent. You’re encouraged to explore this feature for yourself by using one of the editors mentioned.

![npa2 0501](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0501.png)

###### Figure 5-1. Syntax highlighting in a text editor

Syntax highlighting can make it easier to read code, as it allows us to make use of our brain’s powerful pattern-matching capabilities to quickly recognize well-understood code without having to read every character individually and carefully.

Syntax highlighting is obviously context dependent—for instance, what’s considered a keyword in Python will be different from keywords in Go. A good text editor will either include support for syntax highlighting out of the box or, at a minimum, support an ecosystem of plug-ins that can add this kind of functionality.

## Customization

Text editors, by design, are minimalistic. You likely can’t just download one and have it do everything you need out of the box. However, most text editors allow you to find ways to add or change the functionality you need. This can be done via a combination of settings/preferences or third-party plug-ins that add features and integrations that don’t come natively with the editor, as shown in [Figure 5-2](#developmentenvironments-editor-plugin).

For instance, you might want to be able to interact with Git, for tasks like viewing your local repository’s status and making commits, all from within the editor itself. One of the most useful aspects of such an integration is seeing which changes you have made to your local repository at a glance, as shown in [Figure 5-3](#developmentenvironments-gitgutter).

![npa2 0502](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0502.png)

###### Figure 5-2. Customizing text-editor options via plug-ins

![npa2 0503](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0503.png)

###### Figure 5-3. Integrating Git

We dive much deeper into the CLI for Git in [Chapter 11](ch11.html#sourcecontrol); for now, know that little visual hints like this can help reduce friction when working on a complex project. Some editors like Visual Studio Code have this functionality built in; others may support this only via a third-party plug-in.

Plug-ins can also extend an editor’s functionality by adding support for intelligent code analysis, which can detect errors, add auto-completion drop-down menus, and provide advanced code navigation. We explore features like these in the following section.

## Intelligent Code Analysis

Several features that go well beyond simple syntax highlighting are required and expected for nearly all modern development workflows. They aren’t typically referred to by a single cohesive umbrella term, but for the sake of this section, we refer to them as *intelligent code analysis*—as they all enable you, as the developer, to work more productively in a particular language.

###### Note

Developers of text editors have historically had to add the necessary functionality to provide intelligent code analysis features for a particular language. This nontrivial task may require a lot of time and effort, made worse by the fact that the developers behind each editor had to spend this time and effort independently. This means that support for the language you wanted to work with might not be complete, or available at all, depending on your editor.

To make it much easier for editors to integrate with new languages, the [Language Server Protocol, or LSP](https://oreil.ly/Xh3LP) allows this integration to be centralized in a *language server*. Editors that support LSP can much more easily integrate with any language server, which is typically developed and maintained by that language’s community. Languages including Python, Go, and Rust all have their own language servers.

The first of these intelligent code analysis features is *integrated error checking*. If there’s a problem with our code, it’s useful to know right away, instead of having to find out only after we’ve compiled or run the code—especially in production. [Figure 5-4](#developmentenvironments-go-error) shows how a properly configured editor can provide this feedback as we write our code.

In addition to “hard errors,” we also want to know about less critical “stylistic” problems as early as possible. These kinds of problems can be found in code that, for instance, might be functional (it runs or compiles properly) but otherwise violates established idioms of the language you’re working in. For instance, Python has [PEP 8](https://oreil.ly/24O9f), a guide detailing conventions to follow to help make your Python code more readable. Violations of these guidelines can be brought to your attention, as shown in [Figure 5-5](#developmentenvironments-linting), and in some cases, even automatically corrected.

![npa2 0504](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0504.png)

###### Figure 5-4. Error detection in a text editor

![npa2 0505](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0505.png)

###### Figure 5-5. Using a text editor for linting

*Autocompletion* is another extremely common and valuable feature, especially when working with a programming language. This feature enables your editor to detect when you are beginning to type a recognized variable, function, method, or type, and then to provide a drop-down list from which you can quickly locate and choose the correct option, instead of typing the rest. Autocompletion is particularly useful in enumerating the available methods for a given type when relevant, including those methods, parameters, and return types. [Figure 5-6](#developmentenvironments-autocomplete) shows an example.

![npa2 0506](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0506.png)

###### Figure 5-6. A text editor with autocompletion

In many text editors, you can also view the documentation for a given type, method, or function, simply by hovering over it in code. It’s easy to forget the right order or type for the function you’re trying to use, and being able to refresh your memory quickly is incredibly useful. In [Figure 5-7](#developmentenvironments-hover-docs), the documentation for Go’s `strings.Split()` function is shown when hovering over a reference to it in source code.

![npa2 0507](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0507.png)

###### Figure 5-7. Viewing code documentation in a text editor

Options like Go to Definition, Find References, and Refactor within a text editor that includes this kind of integration can be much better than using simple text-searching tools like `grep` or `sed` because they use the deeper understanding of language semantics to avoid finding or updating the wrong thing (for example, partial matches). Code is often not read top to bottom, but rather as a hierarchy of types and function calls, and navigating through a codebase by following references in this way can be useful. While such functionality can vary by editor, Visual Studio Code features these options prominently when right-clicking a variable, function, or method, as shown in [Figure 5-8](#developmentenvironments-go-to-definition-references).

![npa2 0508](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0508.png)

###### Figure 5-8. Displaying the Go to Definition/References options

Editors that are built and configured to have a deeper understanding of the languages we’re working on can provide us with features like these and more, greatly enhancing our productivity when building network automation solutions.

## Text Editors Versus Integrated Development Environments

You may have heard the term *integrated development environment*, or *IDE*. Within the world of software development, this term is at times used somewhat loosely to refer to any general text editor. However, it actually means something much more specific. IDEs are similar to text editors in that they are tools for writing code, but they tend to have a lot of features aimed at helping developers work within a particular framework or language. They aim to be a holistic, “one-stop shop” for subspecialties of software development.

For instance, when writing Python code, you might choose something like [PyCharm](https://oreil.ly/R2t8q), made by JetBrains (shown in [Figure 5-9](#developmentenvironments-pycharm)). However, you likely wouldn’t want to use this for Go development.

![npa2 0509](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0509.png)

###### Figure 5-9. PyCharm

An IDE is a popular choice for some, especially for those who want a fully and vertically integrated solution for their development environment. Others may prefer a simpler editor, opting instead for generalized features that work for any programming environment. A popular reason developers might choose a simpler text editor over an IDE is that they tend to be much more lightweight and more broadly customizable. The downside, historically, has been that this lightweight nature came at the cost of maybe not having as many features as a full-blown IDE.

However, as mentioned in the previous section, the advent of language servers has democratized the in-depth language tooling that used to be reserved for these more focused IDEs. Previously, text editor developers had difficulty justifying the time and effort cost associated with adding these smarts natively. Now that these features are standardized and centralized, simple text editors can compete much more easily with IDEs on these features.

There’s no wrong answer here. Most modern text editors now have support for all kinds of languages, so their advantage is that you can work in a variety of languages while using the same general UI. Then again, companies like JetBrains are developing IDEs for a wide variety of languages and are making an effort to streamline the experience across the various IDEs they offer. So your choice really does come down to personal preference.

In the next section, we dive into more development tools that you can use directly in your editor or at the command line, and are invaluable for working on network automation solutions.

# Development Tools

Aside from the tools you may find integrated with your text editor (natively or through plug-ins) or IDE, a nearly endless list of other tools and frameworks are available to develop, deploy, or debug network automation solutions. Covering them all is impossible, but we can touch on a few you’re most likely to run into during your network automation journey.

Even the term *development tools* is quite broad, so it can be useful to break this discussion into a few use cases you’re bound to encounter:

Dependency managementAs covered in future chapters, the network automation solutions we’ll build are unlikely to be constructed from scratch; typically, they’ll be built on top of existing tools and libraries. Tools that help us manage these dependencies will pay dividends from development to deployment.

Packaging and deployment automationAt some point, you’ll want to take that script or workflow you’ve been developing on your laptop and deploy it to production. Tools that can help you automate the various tasks related to deployment will help you do so safely and predictably.

Working with text-based formatsMuch of the work involved with not only building automation solutions, but also updating and deploying them, often requires working with text-based data formats like YAML. We cover these formats in more detail in [Chapter 8](ch08.html#dataformats), but in this chapter we’ll first arm you with some tools you’ll want in your repertoire for helping you mutate, search, and manage changes to configurations found in these formats.

While these use cases are quite distinct from one another, you should keep in mind these important traits when looking for tooling in each area:

- Where relevant, inputs and configurations for these tools should be stored and managed as code: meaning that you should manage this data alongside the rest of your automation solution in a version-controlled repository like Git. We cover concepts like these a bit more in Chapters [11](ch11.html#sourcecontrol) and [13](ch13.html#cicd).
- Look for tools that align well with the Unix philosophy. Tools like these are often used as part of a shell script, so they should be simple and designed in such a way that they can be stitched together as part of a cohesive solution.

The following sections include specific examples of tools, but many more are out there, each with its own specialized focus.

## Virtualenv

In this book, we discuss a few options for creating automation solutions. Sometimes a full-blown programming language is required. In [Chapter 6](ch06.html#python), we explore the use of Python as part of our automation solutions. Most of the time, the solutions you build in Python should use its huge ecosystem of existing third-party libraries instead of trying to reinvent the wheel.

However, managing these software dependencies can be challenging. For instance, you might be working on two different solutions requiring different versions of a particular Python package to be installed. You might be working on a machine where you don’t even have the necessary permissions to install packages in Python’s system-wide packages directory. You might want to run your solution with a different version of Python than your system’s default.

For these and other reasons, [*Virtualenv*](https://oreil.ly/XuLvC) exists to make managing Python-based dependencies much easier. It works by creating a virtual environment in a directory of your choice, including a full-blown Python environment plus any dependencies you wish to install. This allows you to not only install these dependencies without elevated permissions, but also manage all of this alongside the program or script you’re writing. You’ll see more of Virtualenv in action in [Chapter 6](ch06.html#python).

## Make

Arguably the original build automation tool is [GNU Make](https://oreil.ly/ahm18). Historically, this has been extremely popular for compiling and installing software from source code. If you’ve ever tried to compile a software package from source on Linux, you’ve almost certainly used this tool.

With Make, you define a set of *targets* in a text file called a *Makefile*. You can run one of these targets on the command line, and the instructions in that target will be executed. However, you’re not limited to tasks like compiling source code; you can do just about anything you would normally do using a bash shell script. [Example 5-1](#developmentenvironments-example-makefile) shows a Makefile that includes some common tasks you might see in a Go project.

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch05-netdevenv*](https://github.com/oreilly-npa-book/examples/tree/v2/ch05-netdevenv).

##### Example 5-1. Makefile

```
SHELL=/bin/bash

all: build                   

build:
        go install ./cmd/... 

fmt:
        go fmt ./...         

test:
        go test ./... -cover 
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The `all` target is a special one that allows us to control what happens if the `make` command is run against this file without specifying a target. In this case, we just run the `build` target.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

`make build` installs the binaries in the *./cmd* directory.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

`make fmt` runs a formatting check against our code.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

`make test` executes all testing code found in our project and produces a coverage report.

Makefiles can be especially useful for creating a central place to execute the most common tasks in your project, whatever they are, including building, running, testing, and linting. Instead of having to remember which script to run, with which parameters, in which order, you can just run `make test`, `make lint`, etc.

You can also add dependencies between targets, which allows you to automatically execute other targets first. This allows you to define somewhat complex workflows in the Makefile while keeping the actual user interaction quite simple.

## Docker

As we’ve mentioned, managing software dependencies can be challenging, even for the simplest programs or scripts. This is true during development but also in production. For instance, if your script requires the Requests library, you need to make sure this is installed on every server your script might run on. What if we’re writing an Ansible playbook and requiring a particular module to be available? What about other programming languages, where we might compile a program that requires certain libraries to be available on the system?

Historically, the most comprehensive way to solve dependency issues was with VMs. With the advent of virtualization technology, it became possible to build a VM image that had all of these dependencies set up, without having to dedicate an entire hardware platform to running it. However, this approach isn’t without its problems. For one thing, building an image to house an entire operating system and then installing your application and dependencies on top can be time- and resource-consuming. Additionally, a VM image with a full operating system requires a lot of overhead to run just a single application—but if we try to run multiple applications within the same operating system, how do we manage conflicting dependencies?

In recent years, another option has emerged to solve this problem: application containers. This approach uses isolation techniques offered by the operating system (e.g., Linux) to allow applications to run—with all their dependencies—in an isolated environment on the same operating system. There are a few ways to build and run container images, but overwhelmingly the most popular choice these days is [Docker](https://www.docker.com). With Docker, you can create a manifest known as a (*Dockerfile*) that specifies the steps required to build a complete container image optimized to run a particular application, such as installing dependencies, adding configuration files, and setting environment variables. [Example 5-2](#developmentenvironments-example-dockerfile) shows a Dockerfile.

##### Example 5-2. Dockerfile

```
FROM python:3.8-slim-buster            

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt   

COPY ./getip.py /getip.py              

CMD [ "python3", "/getip.py"]          
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Specifies the base image we want to build from. This particular image comes with Python 3.8 already installed for us.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Copies our *requirements.txt* file from our outside filesystem, into the image itself.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

The `RUN` instruction executes a shell command to run inside the container image; in this case, we’re installing the Python requirements listed in the file we copied in the prior step.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Copies our Python program into the container image as well.

![5](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/5.png)

`CMD` specifies the command that should be run when the container starts; in this case, we’re calling Python to execute our program.

Building and running an instance of a container image from this specification is only a few commands away, as shown in [Example 5-3](#developmentenvironments-docker-build-run).

##### Example 5-3. Building an image from a Dockerfile

```
~$ docker build . -t getip:v1.0 
<...build output omitted for brevity...>

~$ docker run --rm getip:v1.0   
Hello from Docker! Your IP address is 104.28.253.219
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Instructs Docker to build a container image using a Dockerfile found in the current directory, and name it `getip`. It also specifies a tag `v1.0`, so that it can be uniquely identified, should we choose to build multiple versions of the same Docker image.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Instructs Docker to run an instance of the image we just built (and clean it up once it exits).

One of the great advantages of a simple container build system like Docker is that these container images can be run on a production server just as we ran them in the preceding example, without having to worry about installing application dependencies there—they’re all bundled in the container image! This makes it much easier to deploy our code to production.

This also makes it easier for other developers to use these images. For instance, you may publish your image to a registry, which is a centralized repository for images that others can download from using the `docker pull` command, shown in [Example 5-4](#developmentenvironments-docker-pull).

##### Example 5-4. Pulling a Docker image from a registry

```
~$ docker pull ghcr.io/nokia/srlinux
Using default tag: latest
latest: Pulling from nokia/srlinux
5021ece2e12c: Pull complete
Digest: sha256:39671cbffaa2e42d584ecacac2070c9fbef0cf5f0295abe13135506375d0e51e
Status: Downloaded newer image for ghcr.io/nokia/srlinux:latest
ghcr.io/nokia/srlinux:latest
```

When an image is published to a registry in this way, other people can simply download it instead of having to build it themselves.

###### Note

The image used in [Example 5-4](#developmentenvironments-docker-pull) is just an example, and you’ll see this image in action in an upcoming section. The path to your image depends on the type of registry being used.

Publishing images is a bit more complex than we have time to cover in this chapter, but the `docker push` command can be helpful here. You’ll also likely need to set up authentication to your image registry in order to push images. Consult your registry documentation—e.g., [Docker Hub](https://hub.docker.com)—for more information on how to publish container images.

Sometimes a single container image isn’t enough; even the simplest applications can comprise multiple components, each with unique configurations, dependencies, and scalability requirements. Running a single application might require that we instantiate multiple containers and allow them to communicate with one another, but still treat them as a single stack. You can do this by using a [Docker Compose file](https://oreil.ly/L_hiT). With this, Docker allows you to define a set of services that run together, with particular instructions such as what ports should be opened, and in what order they should be run. This can include a combination of images built using a local Dockerfile you’ve also defined or a prebuilt container image like `redis`. [Example 5-5](#developmentenvironments-docker-compose-file) shows a Compose file.

##### Example 5-5. Docker Compose file

```
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```

This is a *very* light introduction to the world of containers and Docker. We explored a bit more of the networking-specific details for container systems like Docker back in [Chapter 4](ch04.html#cloud), but for a more holistic exploration into Docker, we recommend [*Docker: Up & Running*](https://learning.oreilly.com/library/view/docker-up/9781098131814/), 3rd Edition, by Sean P. Kane with Karl Matthias (O’Reilly).

## dyff

Throughout this book (and indeed, later in this chapter), we use a data format called YAML that allows us to work with structured data in a human-readable way. Although YAML was designed to be human readable, technologies like Kubernetes and Ansible that make heavy use of YAML can result in some pretty unwieldy YAML files.

One common problem when working with large amounts of YAML is understanding changes. Generally, when looking at the difference between two versions of a file, we have to use something like `diff`. Let’s say we have a YAML file that defines a series of switches, each of which has a series of interfaces, each of which includes some configured VLANs. If we add a VLAN to one of these interfaces and view the change in a tool like `diff`, the output doesn’t tell us much about where this change took place ([Example 5-6](#developmentenvironments-diff-output)).

##### Example 5-6. `diff` output

```
~$ diff before.yaml after.yaml
30c30
<         vlans: [1, 100]
---
>         vlans: [1, 50, 100]
```

This might be OK for some formats, but with YAML, context is important. Knowing where that change is located within the greater YAML data structure is crucial for understanding the impact of the change. Because of YAML’s popularity within infrastructure automation circles, tools like [`dyff`](https://oreil.ly/5Qskd) have emerged to show changes to a file in a way that preserves the understanding of how YAML works. [Example 5-7](#developmentenvironments-dyff-output) illustrates how this tool can show us not only the change in data, but also a path describing where in the data structure that change took place.

##### Example 5-7. `dyff` output

```
~$ dyff between -b before.yaml after.yaml

switches.sw02.interfaces.eth3.vlans
  + one list entry added:
    - 50
```

This was only a brief exploration of some of the more relevant development tools you might encounter for network automation. You’re likely to encounter far more than we can cover in this section, and new use cases (and tools to solve them) are being discovered all the time. Remain open to incorporating new tools into your repertoire and retiring those that have outlived their usefulness.

In the next section, we explore another important part of building your development environment: tools for simulating network devices and topologies.

# Emulation/Simulation Tools

For a long time, if you wanted to build a network lab, you had to buy hardware. Even after the advent of x86 virtualization in the early 2000s, it wasn’t until around 2015 that network vendors published VM images for even a portion of their portfolios.

These days, many form factors are available as VMs. While running an NOS as a VM usually involves a few caveats (for instance, certain hardware features are difficult to emulate in software), the majority of use cases related to network automation are a perfect fit for this model. Most of the time when we’re looking to develop or test our network automation solutions, we need only a virtual network topology that has the same management interfaces we can expect from “real” equipment. Management APIs and telemetry interfaces like those we discuss in [Chapter 10](ch10.html#apis) are typically present in the virtual editions of our favorite NOS, and that’s usually all we need.

Now that most vendors have at least one VM image, the need has arisen for tools to help build topologies using these images so that we can (as much as possible) faithfully replicate our “real” production networks in a virtual form-factor by interconnecting multiple devices, establishing routing adjacencies, etc. Doing so makes it easier for us to ensure that the solutions we’re building are suitable for production.

For the purposes of integrating tools like these into your development environment, you should look out for the following features:

Configuration as codeAs with other tools in this chapter, it’s highly beneficial to use tools that allow their configuration to be represented simply using text files that are easy to read and edit. This allows you to manage these configurations in a version-controlled repository, alongside the rest of your code, scripts, and workflows. Putting a set of config files in a shared repo somewhere is a lot easier than passing around multigigabyte virtual image files. It also allows you to reuse many of the tools covered in this chapter in a continuous integration/continuous delivery (CI/CD) pipeline to automatically validate existing and proposed network changes, which we cover in [Chapter 13](ch13.html#cicd).

Supports connected topologiesBeing able to run a single instance of an NOS as a VM has some utiliity, but the real power comes from the ability to connect VMs using some of the virtual networking technologies we discussed in [Chapter 3](ch03.html#linux), such as bridging. Doing so allows you to not only validate that your solution performs the necessary configuration changes you intend, but also validate the desired operational state and overall connectivity of the topology as a whole.

Supported and accessibleThis part of your development environment can be complex, and you don’t want to waste time thinking too much about your tools. You want something that works well and is accessible to everyone. It doesn’t have to be open source, but you don’t want to be spending too many cycles fussing around with flaky tools. You need to use tools that are rock-solid and allow you to get a topology up simply and get on with your work.

Next, we explore some examples of emulation and simulation tools that you’re likely to want to add to your repertoire for your network automation journey.

## VirtualBox

If you’re looking to run VMs of any kind on your laptop, one of your best choices is [VirtualBox](https://www.virtualbox.org). This open source virtualization platform has been around for a long time. It can run on a variety of operating systems (including Windows, Linux, and macOS) and is free to download. You are, of course, free to use VirtualBox on its own by using the GUI shown in [Figure 5-10](#developmentenvironments-virtualbox).

![npa2 0510](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0510.png)

###### Figure 5-10. VirtualBox

You can download virtual images from just about any network vendor’s website and import them into VirtualBox, often with just a few clicks. However, as you’ll see in the following section, you can use tools like Vagrant to automate the instantiation and configuration of these VMs.

## Vagrant

As we’ve mentioned, using a platform like VirtualBox directly is certainly possible if you want to emulate your favorite NOS, but this particular workflow has a couple of shortcomings within the context of a proper network development environment:

- Collaborating over changes you might make to your VMs can be difficult. Even “small” VM images can be multiple gigabytes, making them somewhat impractical to share with other developers.
- Even simple configuration changes through the VirtualBox GUI can be tedious. Using this approach to create complex topologies of VMs is quite time-consuming and error prone.

Instead of doing this, you can use a tool like [Vagrant](https://www.vagrantup.com) to define a full topology in a text file, complete with not only the individual configuration of each VM, but also how they should be connected together. Vagrant integrates with *providers* like VirtualBox to orchestrate the creation and configuration of VMs, following the instructions defined in the configuration file. This *Vagrantfile* uses a Ruby-like syntax for defining VM configurations. [Example 5-8](#developmentenvironments-vagrantfile) shows a topology containing three interconnected virtual [VyOS routers](https://vyos.io).

##### Example 5-8. Vagrantfile describing three-node virtual router topology

```
Vagrant.configure(2) do |config|
    config.vm.box = "vyos/current"       

    config.vm.define "r1" do |r1|        
        r1.vm.host_name = "r1"
        r1.vm.network "private_network", 
                        ip: "192.168.12.11",
                        virtualbox__intnet: "01-to-02"
        r1.vm.network "private_network",
                        ip: "192.168.31.11",
                        virtualbox__intnet: "03-to-01"
    end

    config.vm.define "r2" do |r2|
        r2.vm.host_name = "r2"
        r2.vm.network "private_network",
                        ip: "192.168.23.12",
                        virtualbox__intnet: "02-to-03"
        r2.vm.network "private_network",
                        ip: "192.168.12.12",
                        virtualbox__intnet: "01-to-02"
    end

    config.vm.define "r3" do |r3|
        r3.vm.host_name = "r3"
        r3.vm.network "private_network",
                        ip: "192.168.31.13",
                        virtualbox__intnet: "03-to-01"
        r3.vm.network "private_network",
                        ip: "192.168.23.13",
                        virtualbox__intnet: "02-to-03"
    end
end
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Specifies the image that should be used for all three of the VMs defined in this Vagrantfile.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Defines the VMs. This `config.vm.define` statement and the block contained within are repeated for each VM in our topology.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Optionally, we can attach networks to each VM. In this case, the network names are chosen in such a way that the three virtual machines are connected in a “triangle” topology.

Vagrant images are distributed in a special format called [`boxes`](https://oreil.ly/JqfYP). This is similar to the virtual images you might download to run in VirtualBox natively, but also includes the necessary modifications to use that virtual image in Vagrant. The image in [Example 5-8](#developmentenvironments-vagrantfile) (`vyos/current`) is already packaged in this format and is also hosted on Vagrant Cloud—Vagrant’s official image repository. Vagrant can automatically download and use this image without any modifications, and it should just work.

Unfortunately, most network vendors don’t upload their Vagrant boxes to Vagrant Cloud, so you may need to download the Vagrant *.box* file yourself. Worse still, many vendors provide simple VirtualBox-compatible images, which means you may have to do a bit of packaging yourself to get them to work with Vagrant. Fortunately, plenty of guides and tools out there can help in this regard; for instance, the [netlab project](https://oreil.ly/JilA8) has guides for creating Vagrant boxes from these more general-purpose VM images.

###### Note

Some Vagrant boxes also require a Vagrant plug-in to be installed on the VM host, to allow Vagrant to detect and interact properly with the guest operating system. For example, you may need to install the VyOS plug-in via `vagrant plugin install vagrant-vyos` in [Example 5-8](#developmentenvironments-vagrantfile) to work.

In the directory where this Vagrantfile is located, you need only run `vagrant up`. Once you do this, the relevant image(s) will be downloaded, and three virtual routers will be started and connected to each other as described in the Vagrantfile. [Example 5-9](#developmentenvironments-vagrant-output) shows the output provided by Vagrant during the instantiation of this virtual topology.

##### Example 5-9. Starting a virtual topology

```
~$ vagrant up
Bringing machine 'r1' up with 'virtualbox' provider...
Bringing machine 'r2' up with 'virtualbox' provider...
Bringing machine 'r3' up with 'virtualbox' provider...
==> r1: Importing base box 'vyos/current'...
==> r1: Matching MAC address for NAT networking...
==> r1: Checking if box 'vyos/current' version '20230215.03.17' is up to date...
==> r1: Setting the name of the VM: vagrant_r1_1677336581429_25005
==> r1: Clearing any previously set network interfaces...
==> r1: Preparing network interfaces based on configuration...
    r1: Adapter 1: nat
    r1: Adapter 2: intnet
    r1: Adapter 3: intnet
==> r1: Forwarding ports...
    r1: 22 (guest) => 2222 (host) (adapter 1)
==> r1: Booting VM...
==> r1: Waiting for machine to boot. This may take a few minutes...
    r1: SSH address: 127.0.0.1:2222
    r1: SSH username: vyos
    r1: SSH auth method: private key
    r1:
    r1: Vagrant insecure key detected. Vagrant will automatically replace
    r1: this with a newly generated keypair for better security.
    r1:
    r1: Inserting generated public key within guest...
    r1: Removing insecure key from the guest if it's present...
    r1: Key inserted! Disconnecting and reconnecting using new SSH key...
==> r1: Machine booted and ready!
==> r1: Checking for guest additions in VM...
    r1: No guest additions were detected on the base box for this VM! Guest
    r1: additions are required for forwarded ports, shared folders, host only
    r1: networking, and more. If SSH fails on this machine, please install
    r1: the guest additions and repackage the box to continue.
    r1:
    r1: This is not an error message; everything may continue to work properly,
    r1: in which case you may ignore this message.
==> r1: Setting hostname...
==> r1: Configuring and enabling network interfaces...
==> r1: Rsyncing folder: ~/examples/ch05-netdevenv/vagrant/ => /vagrant

[output omitted for similar output from r2 and r3...]
```

You can connect via SSH to any of the VMs in this topology, and even ping between them (thanks to the networking configuration in our Vagrantfile), as shown in [Example 5-10](#developmentenvironments-vagrant-ssh).

##### Example 5-10. Connecting to a virtual topology

```
~$ vagrant ssh r1
Welcome to VyOS!

vyos@r1:~$ ping 192.168.12.12 count 1
PING 192.168.12.12 (192.168.12.12) 56(84) bytes of data.
64 bytes from 192.168.12.12: icmp_seq=1 ttl=64 time=0.431 ms

--- 192.168.12.12 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.431/0.431/0.431/0.000 ms
```

Vagrant also includes a feature called *provisioners* that allows you to perform additional configuration steps after the VMs have been provisioned and booted up. One relevant provisioner for our purposes is `ansible`, which allows you to run an Ansible playbook on your VMs. This can be used to bootstrap your topology with a more real-world configuration, including routing adjacencies and ACLs. You can do this by adding a stanza to the VM configuration in the Vagrantfile, like the one shown in [Example 5-11](#developmentenvironments-vagrant-provision).

##### Example 5-11. Adding a provisioner to a Vagrant topology

```
config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
end
```

The benefit, of course, is that you can store both the Ansible playbook and the Vagrantfile in the same version-controlled repository, making it easier for anyone to stand up the same topology, with all of the relevant configurations in place. We explore Ansible in greater detail in [Chapter 12](ch12.html#automationtools). Once you’ve learned more about Ansible, consider circling back here and adding a playbook to your Vagrant topology!

When you’re all done with your Vagrant topology, you can clean it up as simply as you created it, using the single command `vagrant destroy`, as shown in [Example 5-12](#developmentenvironments-vagrant-destroy).

##### Example 5-12. Destroying the vagrant topology

```
~$ vagrant destroy -f
==> r3: Forcing shutdown of VM...
==> r3: Destroying VM and associated drives...
==> r2: Forcing shutdown of VM...
==> r2: Destroying VM and associated drives...
==> r1: Forcing shutdown of VM...
==> r1: Destroying VM and associated drives...
```

Vagrant and VirtualBox represent a powerful combination for creating simulated network topologies from the comfort of your laptop, but sometimes you need something a bit more modern and lightweight. In the next section, we explore a fairly new tool for creating simulated network topologies, using containers instead of VMs.

## Containerlab

A great advantage of Vagrant is that it allows VM topologies to be easily orchestrated via text files that can be shared. However, VMs can often consume a lot of system resources. It would be great if you could use container images instead, while retaining many of these benefits.

Fortunately, a relatively new tool called [*Containerlab*](https://oreil.ly/kcahb) allows you to do this. With Containerlab, you can create lab topologies using a simple text-based format, and then instantiate these topologies using container images. Whereas Vagrant used a Ruby-like syntax for defining the topology configuration, Containerlab uses a simpler YAML-based language in *clab* files, as shown in [Example 5-13](#developmentenvironments-containerlab-clab).

##### Example 5-13. Containerlab topology clab file

```
name: example-lab               
topology:
  nodes:                        
    srl01:
      kind: srl
      image: ghcr.io/nokia/srlinux
      startup-config: srl1.cfg  

    srl02:
      kind: srl
      image: ghcr.io/nokia/srlinux
      startup-config: srl2.cfg

links:                          
    - endpoints: ["srl01:e1-1", "srl02:e1-1"]
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

The name of the topology as a whole. This allows Containerlab to understand which nodes are in which topology—especially useful for running multiple topologies at once.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

The nodes in the topology. We can specify which image the nodes use as well as what they should be named.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

An optional parameter specifying a configuration that should be applied to the node once instantiated.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Creates connectivity between the nodes in our topology.

###### Note

We explore YAML in much greater detail in [Chapter 8](ch08.html#dataformats), so don’t worry about the details of this syntax for now. This is just an example to get you started.

You can deploy this topology by using the single command `containerlab deploy`, shown in [Example 5-14](#developmentenvironments-containerlab-deploy).

##### Example 5-14. Containerlab deployment

```
~$ containerlab deploy
INFO[0000] Containerlab v0.36.1 started
INFO[0000] Parsing & checking topology file: topology1.clab.yaml
INFO[0000] Creating lab directory: /examples/ch05-netdevenv/containerlab/clab-srl02
INFO[0000] Creating docker network: Name="clab", IPv4Subnet="172.20.20.0/24", IPv6Subnet="2001:172:20:20::/64"
INFO[0000] Creating container: "srl1"
INFO[0000] Creating container: "srl2"
INFO[0001] Creating virtual wire: srl1:e1-1 <--> srl2:e1-1
INFO[0001] Running postdeploy actions for Nokia SR Linux 'srl2' node
INFO[0001] Running postdeploy actions for Nokia SR Linux 'srl1' node
INFO[0010] Adding containerlab host entries to /etc/hosts file
+---+-----------------+--------------+-----------------------+------+---------+----------------+----------------------+
| # |      Name       | Container ID |         Image         | Kind |  State  |  IPv4 Address  |     IPv6 Address     |
+---+-----------------+--------------+-----------------------+------+---------+----------------+----------------------+
| 1 | clab-srl02-srl1 | ea5012df1061 | ghcr.io/nokia/srlinux | srl  | running | 172.20.20.2/24 | 2001:172:20:20::2/64 |
| 2 | clab-srl02-srl2 | 08b9f9ec660a | ghcr.io/nokia/srlinux | srl  | running | 172.20.20.3/24 | 2001:172:20:20::3/64 |
+---+-----------------+--------------+-----------------------+------+---------+----------------+----------------------+
```

You can connect via SSH (or other available methods) by using the management address in the preceding table, as shown in [Example 5-15](#developmentenvironments-containerlab-ssh).

##### Example 5-15. Connecting to Containerlab topology via SSH

```
~$ ssh admin@172.20.20.2

A:srl1# ping network-instance default 192.168.0.1 -c 1
Using network instance default
PING 192.168.0.1 (192.168.0.1) 56(84) bytes of data.
64 bytes from 192.168.0.1: icmp_seq=1 ttl=64 time=10.5 ms

--- 192.168.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 10.518/10.518/10.518/0.000 ms
```

However, Containerlab is just orchestrating Docker containers behind the scenes, so you can use `docker exec` to access the CLI of these nodes as well, as shown in [Example 5-16](#developmentenvironments-containerlab-docker-exec).

##### Example 5-16. Connecting to Containerlab topology via `docker exec`

```
~$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS ...
08b9f9ec660a   ghcr.io/nokia/srlinux   "/tini -- fixuid -q …"   7 minutes ago   Up 7   ...
ea5012df1061   ghcr.io/nokia/srlinux   "/tini -- fixuid -q …"   7 minutes ago   Up 7  ...

~$ docker exec -it clab-srl02-srl1 sr_cli
Using configuration file(s): []
Welcome to the srlinux CLI.
A:srl1#
```

You can also use the `containerlab graph` subcommand to start a local web server that allows you to inspect your running topology in the browser ([Figure 5-11](#developmentenvironments-containerlab-graph)).

![npa2 0511](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0511.png)

###### Figure 5-11. Containerlab graph

While the idea of running a network topology by using containers is still fairly new, many vendors provide container images for learning purposes. Such a form factor for learning, or validating that automation solutions work as we expect, is proving to be an invaluable recent addition to our repertoire.

## Other Tools

This section lists a few other popular tools for simulating network topologies that we can’t cover in detail here. They all have varying capabilities and design goals but may be worth knowing about:

GNS3A popular network emulation platform that includes a great interface for drag-and-drop building of virtual topologies. Historically, it relied on emulation software called *dynamips*, which was specifically created to emulate Cisco hardware. However, it has since expanded greatly with many new features, including the ability to run non-Cisco images.

EVE-NGAnother great network emulation platform with a web-based UI. Includes free and paid versions.

TerraformA popular tool for IaC automation. Particularly useful for building cloud-based labs. We explore Terraform in much greater detail in [Chapter 12](ch12.html#automationtools).

Hopefully, this chapter has provided insight into the kinds of tools and techniques you can use in your own network automation development environment. Again, this is an ever-changing space, so take this chapter not as an exhaustive checklist, but as a source of inspiration for building out an environment that works for you and your team.

# Summary

The best network development environment is the one that works for you. The tools and techniques discussed here are just some popular examples, and the environment you construct for yourself will be influenced heavily by your own background, the programming and automation technologies you work with, and the organization and team you’re a part of. Play around with different options, and be open to adapting when new tools become available.

In the chapters to follow, we’re going to make heavy use of this environment, diving into concepts like Python, Go, data formats, and templates.
