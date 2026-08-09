# Chapter 9. Templates

Much of a network engineer’s job involves the CLI, and much of this work requires syntax-specific keywords and phrases that are often repeated several times, depending on the change. This not only becomes inefficient over time but also is error prone. The way to configure a BGP neighbor relationship on Cisco IOS may be obvious, for instance, but what’s not obvious at times are the smaller, “gotcha” configurations, like remembering to append the right BGP community configuration. Often in networking, there are many different ways to do the same thing—and this may be totally dependent on your organization.

One of the key benefits of network automation is *consistency*—being able to predictably and repeatably make changes to production network infrastructure and achieve a desired result. One of the best ways to accomplish this is by creating templates for all automated interaction with the network.

Creating templates for your network configurations means that you can standardize those configurations for your organization, while also allowing network administrators and *consumers* (help desk, network operations center, IT engineers) to dynamically fill in some values when needed. You get the benefits of speed, requiring much less information to make a change, but also consistency (and through this, safety) because the template contains all the necessary configuration commands that your policies dictate.

This chapter starts with an introduction to template tools in general, and then presents specific implementations and shows how to leverage these tools to create network configuration templates.

# The Rise of Modern Template Languages

Template technologies have been around for a very, very long time. Just a basic web search for “template languages” shows a multitude of these, most often several options for every related programming language.

You may also notice that the majority of these languages have deep applications in the web development industry. This is because much of the web is based on templates! Instead of writing HTML files for every single user-profile page that a social media site may have, the developers will write one and insert dynamic values into that template, depending on the data being presented by the backend.

In short, template languages have a wide variety of relevant use cases. Their obvious roots are in web development, and of course we’ll be talking about using them for network configuration in this chapter, but they have applications in just about any text-based medium, including documentation and reports.

So it’s important to remember that using templates requires three steps. First, the templates have to be written. Second, you need some form of data, which will ultimately get rendered into the template to produce something meaningful like a network configuration. This leads us to the third step: something has to drive data into the template. This could be an automation tool like Ansible, which we cover in [Chapter 12](ch12.html#automationtools), or you could be doing it yourself with a language like Python, which we show later in this chapter. Templates are not very useful on their own.

###### Tip

Most template languages aren’t full-on programming languages in the purest sense. Most often, a template language is closely tied to another language that will drive data into the templates that you’ve built. As a result, each template language and its “parent” language have several similarities. A good example is one that we heavily discuss in this chapter: Jinja is a template language that came out of a Python-centric community, so Jinja has distinct similarities with Python. So if you’re wondering which template language to use, it’s probably best to decide which “real” language you’re aligned with (either through writing your own code or by using an existing tool like Ansible) and go from there.

As mentioned previously, template languages aren’t necessarily a new concept, but we are seeing new ideas and even entire languages make it into the ecosystem all the time. If you look at the history of template languages, many were created to serve as a crucial part of the web: dynamic content. This is easily taken for granted these days, but back when the web was just getting started and most websites were built from fairly static content, dynamically loading pieces of data into a page was a big step forward.

## Using Templates for Web Development

[Django](https://www.djangoproject.com), a Python-based web framework, significantly leverages the concept of templated documents. Django has a template language that allows the web developer to create web content in much the same way they normally would, but also offers a way to make portions of the page dynamic. Using Django’s template language, the developer can designate portions of an otherwise static page to load dynamic data when the user requests a page.

Here’s a simple example—note that this looks much like an HTML document, but with certain portions replaced with variables (indicated with `{{ }}` notation):

```
<h1>{{ title }}</h1>

{% for article in article_list %}
<h2>
  <a href="{{ article.get_absolute_url }}">
    {{ article.headline }}
  </a>
</h2>
{% endfor %}
```

This template can be rendered by Django when a user loads the page. The Django framework will populate the `title` and `article_list` variables, and the user will receive a page that’s been fully populated with real data. The developer doesn’t have to write a static HTML page for every possible thing the user wants to retrieve; this is managed by logic on the backend of this web application.

###### Note

The Django templating language is similar (but not identical) to the templating language [Jinja](https://oreil.ly/FdzuH), which we discuss in depth in this chapter. Don’t worry about the syntax; we’ll get into that. For now, just focus on the concepts and the value that templates provide: consistency.

Detailing the multitude of other available template languages is outside the scope of this chapter, but you should be aware that they exist. Python alone has several options, such as the aforementioned Django and Jinja languages, but also [Mako](https://www.makotemplates.org) and [Genshi](https://genshi.edgewall.org). Other languages like [Go](https://oreil.ly/x0V40) and [Ruby](https://oreil.ly/lUVr9) have built-in template systems. Again, the point to remember is that the important work of populating a template with data is the role of one of these languages, like Python or Go, so this is the number-one factor in deciding which template language to use. More often than not, it’s best to go with a template system built for that language.

## Expanding On the Use of Templates

The concepts of templating, especially those discussed in this chapter, are not specific to any single use case and can be applied to nearly any text-based medium. At the end of the day, templates are just a way to transform data into a specific text format. [Figure 9-1](#templates-flow) illustrates this flow.

![npa2 0901](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0901.png)

###### Figure 9-1. How templates are produced

All template technologies discussed in this chapter generally work this way. This makes templates useful for anything text based, including reports, configuration files, and configurations. Perhaps you’re pulling data from a network device and want to be able to produce a nice report on this data and email it to coworkers. [Example 9-1](#templates-basic-report) shows a Jinja template for producing a report containing a list of VLANs.

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch09-templates*](https://github.com/oreilly-npa-book/examples/tree/v2/ch09-templates).

##### Example 9-1. Basic report with Jinja

```
| VLAN ID | NAME | STATUS |
| ------- |------| -------|
{% for vlan in vlans %}
| {{ vlan.get('vlan_id') }} | {{ vlan.get('name') }} | {{ vlan.get('status') }} |
{% endfor %}
```

Because you’re really just working with text, you can build a template for it. Keep the generic nature of templates in mind as you get into the details of specific use cases and particular template technologies like Jinja; templates have applications well beyond the narrow set of use cases presented in this chapter.

# The Value of Templates in Network Automation

At this point, you might be wondering why we’re talking about web development and how that could possibly help you on your network automation journey. It’s important to understand the value behind templates in general, whether they’re used for the web or not. Templates provide consistency—instead of handcrafting text files full of HTML tags or entering CLI commands, templates enable you to declare which parts of your files need to remain static and which parts should be dynamic.

Every network engineer who has worked on a network long enough has had to prepare a configuration file for a new piece of network gear, like a switch or router. Maybe this has to be done for many switches—perhaps for a new data center build. To make the best use of time, it’s useful to build these configurations ahead of time, so that when the switch is physically racked and cabled, the network engineer needs only to paste the configuration into a terminal.

Let’s say you’re in charge of a rollout like this—it’s your job to come up with configurations for all switches going into the new data center being built for your organization. Obviously, each switch will need its own unique configuration file, but a large portion of the configuration will be similar among devices. For instance, you might have the same SNMP community strings, the same admin password, and the same VLAN configuration (at least for similar device types like ToR switches).

Then again, some parts of the configuration are probably unique to a single device. Routers or Layer 3 switches typically require unique addresses, and probably some fairly unique routing protocol configurations, depending on where that device exists in the topology. Deciding what parameters go to which switches can be time-consuming and likely to result in errors. Templates allow you to standardize on a common base configuration and help ensure that the right values get filled in for each device. Separating the template from the data that populates it is one of the best ways to simplify this process.

The primary value of templates for network engineers is achieving configuration consistency. Appropriately implemented, templates can reduce the likelihood of human errors caused when changing network configurations. There seems to be a lot of fear that making complex changes in an automated way in production is a bad idea, but if you follow good discipline and properly test your templates, you really can improve network operations. Templates don’t automatically remove human error, but when used properly, they can greatly reduce it, resulting in fewer outages.

Using templates to aid the rollout of new network devices is a simple yet powerful way to demonstrate the value of templates, since it has the added benefit of saving a lot of time for the network engineer. However, don’t think that this is the only place where templates can be used. In many network automation projects, templates are not even used by humans but by automation software like Ansible to push configuration changes to network devices—live, in production.

The following sections cover some of the most popular options for building template-based configurations and documents that exist for network automation.

# Jinja

We mentioned Jinja in the introduction to this chapter, but it’s time to dive in a little deeper. While we’ll briefly explore a few other options in this chapter, you’ll notice that we spend a lot more pages on Jinja. Currently, Jinja is still by far the most popular template language in the world of network automation because of broad support by many automation tools and languages, including Python.

Let’s start with a basic example and write a template to configure a single switch interface. Here’s an example switchport configuration that you want to convert to a template (so you can configure the hundreds of other switchports in your environment):

```
interface GigabitEthernet0/1
 description Server Port
 switchport access vlan 10
 switchport mode access
```

This kind of snippet is easy to write a template for—you need only decide which parts of this configuration need to stay the same and which need to be dynamic. [Example 9-2](#templates-switchport-configuration-2) has removed the specific interface name and converted it into a variable that you’ll populate when you render the template into an actual configuration.

##### Example 9-2. Parameterized interface name in a switchport config template

```
interface {{ interface_name }}
 description Server Port
 switchport access vlan 10
 switchport mode access
```

You can pass in the variable `interface_name` when rendering this template, and that spot will get filled in with the value associated with `interface_name`.

However, this template assumes that each network interface has an identical configuration. What if you want a different VLAN or a different interface description on some of the interfaces? In that case, you should also convert some of the other parts of the configuration into their own variables, as shown in [Example 9-3](#templates-switchport-configuration-3).

##### Example 9-3. Several variables in the switchport config template

```
interface {{ interface_name }}
 description {{ interface_description }}
 switchport access vlan {{ interface_vlan }}
 switchport mode access
```

These are simple examples, but they’re not very namespace-friendly.

It’s common to leverage concepts like classes and dictionaries in a language like Python when rendering a template. This allows us to store multiple instances of data that we can loop over and write multiple times in our resulting configuration. We’ll look at loops in a future section, but for now, [Example 9-4](#templates-switchport-configuration-4) shows that same template rewritten to take advantage of something like a Python class or dictionary.

##### Example 9-4. Using a dictionary in a switchport config template

```
interface {{ interface.name }}
 description {{ interface.description }}
 switchport access vlan {{ interface.vlan }}
 switchport mode access
```

This is a minor change, but an important one. The `interface` object is passed to the template as a whole. If `interface` is a Python class, then `name`, `description`, and `vlan` are all properties of that class. The same is true if `interface` is a dictionary—the only difference is that they are all keys of this dictionary, and not properties, so the rendering engine would automatically place the corresponding values for those keys when rendering this template.

## Rendering a Jinja Template File in Python

In the previous example, you created a basic Jinja template for a switchport configuration, but you didn’t explore how that template is rendered or what drives data into the template to result in the final product. We’ll explore that now by using Python and the Jinja2 library.

###### Note

While the templating language itself is known as *Jinja*, the Python library for working with Jinja is called *Jinja2*.

Let’s use the same template snippet from [Example 9-4](#templates-switchport-configuration-4) and use Python to populate those fields with real data. We’ll use the Python interpreter this time so you can walk through the example on your own machine.

###### Tip

The Jinja2 rendering engine in Python is not part of the standard library, so it is not installed by default. However, Jinja2 can be installed with `pip3`, through the command `pip3 install jinja2`, the same as any other Python package found on PyPI, as we covered in [Chapter 6](ch06.html#python).

Once the Jinja2 library is installed, you should first import the required objects that you’ll need in order to render your templates:

```
>>> from jinja2 import Environment, FileSystemLoader
```

Next, you need to set up the environment, so the renderer knows where to find the template:

```
>>> ENV = Environment(loader=FileSystemLoader('.'))
>>> template = ENV.get_template("template.jinja")
```

The first line sets up the `Environment` object, specifying a single dot (`.`) to indicate that the templates exist in the same directory in which you started the Python interpreter. The second line derives a template object from that environment by statically specifying the template name, *template.jinja*. The contents of this file are identical to [Example 9-4](#templates-switchport-configuration-4).

Now that this is done, you need your data, which you’ll specify using a dictionary. The keys for this dictionary correspond to the field names referenced in your template:

```
>>> interface_dict = {
...     "name": "GigabitEthernet0/1",
...     "description": "Server Port",
...     "vlan": 10,
...     "uplink": False
... }
```

###### Caution

You probably won’t have to manually create data structures in Python to populate a template with data. This is being done for illustrative purposes in this book. Typically, you’ll want to pull data from an API or a file on disk, rather than declaring it statically in your program or script.

You now have everything you need to render your template. You’ll call the `render()` function of your template object to pass data into the template engine, and use the `print()` function to output your rendered output to the screen:

```
>>> print(template.render(interface=interface_dict))
interface GigabitEthernet0/1
 description Server Port
 switchport access vlan 10
 switchport mode access
```

Note that you pass an argument to the `render()` function of your template object. Pay close attention to the name—the keyword argument `interface` corresponds to the references to `interface` within your Jinja template. This is how you get your interface dictionary into the template engine—when the template engine sees references to `interface` or its keys, it will use the dictionary passed here to satisfy that reference.

As you can see, the rendered output is as you expect. However, you don’t have to use a Python dictionary. It’s common to drive data from other Python libraries into a Jinja template, and this may take the form of a Python class.

[Example 9-5](#templates-jinja-python-class) shows a Python program that’s similar to the code you just went through, but instead of using a dictionary, you use a Python class.

##### Example 9-5. Using a Python class to populate a Jinja template

```
from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.jinja")

class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
print(template.render(interface=interface_obj))
```

The output from this program is identical to the previous output. Therefore, there really isn’t one right way to populate a Jinja template with data—it depends on where that data comes from. Fortunately, the Python Jinja2 library allows for some flexibility here.

## Using Conditionals and Loops

It’s time to really make your templates work for you. The previous examples are useful for understanding how to insert dynamic data into a text file, but that’s just part of the battle of scaling network templates up to properly automate network configuration.

###### Caution

Jinja allows you to embed Python-esque logic into your template files in order to do things like make decisions or condense duplicate data into one chunk that is *unpacked* at render time via a `for` loop. While these tools are powerful, they can also be a slippery slope. Don’t get too carried away with putting all kinds of advanced logic into your templates. Jinja has some really useful features, but it was never meant to be a full-blown programming language, so it’s best to keep a healthy balance. Read the [Jinja FAQ](https://oreil.ly/kKA8O), specifically the section titled “Isn’t It a Bad Idea to Put Logic in Templates?” for some tips.

### Using conditional logic to create a switchport configuration

Let’s continue our example of configuring a single switchport—but in this case, you want to decide what to render by using a conditional in the template file itself.

Often some switchport interfaces will be VLAN trunks, and others will be in *mode access*. A good example is an access layer switch, where two or more interfaces are the uplink ports that need to be configured to permit all VLANs. Our previous examples showed an `uplink` boolean property, set to `True` if the interface is an uplink and `False` if it is just an access port. You can check against this value in your template by using a conditional:

```
interface {{ interface.name }}
 description {{ interface.description }}
{% if interface.uplink %}
 switchport mode trunk
{% else %}
 switchport access vlan {{ interface.vlan }}
 switchport mode access
{% endif %}
```

###### Tip

If you run some of the examples in this section, you may notice extra whitespace, especially extra newlines between lines of rendered text. This is due to the way Jinja removes the template syntax when rendering the final text. You can use opt-in methods to manage this whitespace, such as placing a hyphen immediately following or preceding the substitution syntax (e.g., `{% for item in seq -%}`). This gives you the option to trim extra whitespace either before or after a given bit of Jinja logic. We’ve omitted these options to keep the examples simpler, but in practice you can and probably should use them to keep your rendered text cleaner, especially when rendering to formats where whitespace has a significant impact on the data being represented.

In short, if the `uplink` property of `interface` is `True`, you want to make this interface a VLAN trunk. Otherwise, let’s make sure that it’s set up with the appropriate access mode.

In the previous example, you also see a new syntax: the `{% ... %}` braces are a special Jinja tag that indicates some kind of logic. This template is built to configure `GigabitEthernet0/1` as a VLAN trunk, and any other interface will be placed in access mode, in VLAN 10.

### Using a loop to create many switchport configurations

You’ve configured only a single interface at this point, so let’s see if you can use Jinja loops to create configurations for many switchports. For this, you use a `for` loop that’s extremely similar to the syntax you would normally have in Python:

```
{% for n in range(10) %}
interface GigabitEthernet0/{{ n+1 }}
 description {{ interface.description }}
 switchport access vlan {{ interface.vlan }}
 switchport mode access
{% endfor %}
```

Note that you’re again using the `{% ... %}` syntax to contain all logic statements. In this template, you’re calling the `range()` function to give a list of integers to iterate over, and for each iteration, you print the result of `n+1` because `range()` starts at 0, and normally, switchports start at 1.

### Using a loop and conditionals to create switchport configurations

This creates an identical configuration for 10 switchports—but what if you want a different configuration for some of them? Take the example about Jinja conditionals—perhaps the first port is a VLAN trunk. You can combine what you’ve learned about conditionals and loops to accomplish this:

```
{% for n in range(10) %}

interface GigabitEthernet0/{{ n+1 }}
 description {{ interface.description }}
{% if n+1 == 1 %}
 switchport mode trunk
{% else %}
 switchport access vlan {{ interface.vlan }}
 switchport mode access
{% endif %}

{% endfor %}
```

This results in `GigabitEthernet0/1` being configured as a VLAN trunk, but `Gigabi⁠t​Ethernet0/2–10` is in access mode. Here is an example using simulated data for the interface descriptions:

```
interface GigabitEthernet0/1
 description TRUNK INTERFACE
 switchport mode trunk
interface GigabitEthernet0/2
 description ACCESS INTERFACE
 switchport mode access
interface GigabitEthernet0/3
 description ACCESS INTERFACE
 switchport mode access
...
```

### Iterating over a dictionary to generate configurations

You were able to access keys in a dictionary in your Jinja template in the preceding section, but what if you want to iterate over dictionaries and lists by using a `for` loop? Let’s imagine that you’re passing the following list to your template as `interface_list`. Here’s the relevant Python:

```
intlist = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]
print(template.render(interface_list=intlist))
```

You then reference `interface_list` in your loop so that you can access its members and generate a switchport configuration for each one. Note that the nested conditional has also been modified, since your counter variable `n` no longer exists:

```
{% for iface in interface_list %}

interface {{ iface }}
{% if iface == "GigabitEthernet0/1" %}
 switchport mode trunk
{% else %}
 switchport access vlan 10
 switchport mode access
{% endif %}

{% endfor %}
```

You now simply refer to `iface` to retrieve the current item of that list for every iteration of the loop.

You can also do the same thing with dictionaries. Again, here’s a relevant Python snippet for constructing and passing in a dictionary to this Jinja template. Let’s keep it simple this time, and just pass a set of interface names as keys, with the corresponding port descriptions as values:

```
intdict = {
    "GigabitEthernet0/1": "Server port number one",
    "GigabitEthernet0/2": "Server port number two",
    "GigabitEthernet0/3": "Server port number three"
}
print(template.render(interface_dict=intdict))
```

You can modify your loop to iterate over this dictionary in much the same way you’d do in native Python:

```
{% for name, desc in interface_dict.items() %}
interface {{ name }}
  description {{ desc }}
{% endfor %}
```

The `for name, desc...` means that at each iteration of the loop, `name` will be a key in your dictionary, and `desc` will be the corresponding value for that key. Don’t forget to add the `.items()` notation as shown here, to properly unpack these values.

This allows you to simply refer to `name` and `desc` in the body of the template, and the result is shown here:

```
interface GigabitEthernet0/1
  description Server port number one

interface GigabitEthernet0/2
  description Server port number two

interface GigabitEthernet0/3
  description Server port number three
```

###### Note

In previous versions of Python, the order in which these interfaces appear would not be guaranteed, as dictionaries were by nature an unordered data structure. However, as of Python 3.7, dictionaries preserve insertion order for literals like these.

### Generating interface configurations from a list of dictionaries

In this section, you’re going to combine using lists and dictionaries to really put this template to work for you. Each interface will have its own dictionary, and the keys will be attributes of each network interface, like `name`, `description`, or `uplink`. Each dictionary will be stored inside a list, which is what your template will iterate over to produce configuration.

First, here’s the data structure in Python that we just described:

```
interfaces = [
    {
        "name": "GigabitEthernet0/1",
        "desc": "uplink port",
        "uplink": True
    },
    {
        "name": "GigabitEthernet0/2",
        "desc": "Server port number one",
        "vlan": 10
    },
    {
        "name": "GigabitEthernet0/3",
        "desc": "Server port number two",
        "vlan": 10
    }
]
print(template.render(interface_list=interfaces))
```

This allows you to write a powerful template that iterates over this list, and for each list item, simply refers to keys found within that particular dictionary. [Example 9-6](#templates-jinja-iterating-list-dicts) makes use of all the techniques you’ve learned about loops and conditionals.

##### Example 9-6. Iterating over a list of dictionaries in Jinja

```
{% for interface in interface_list %}
interface {{ interface.name }}
  description {{ interface.desc }}
  {% if interface.uplink %}
    switchport mode trunk
  {% else %}
    switchport access vlan {{ interface.vlan }}
    switchport mode access
  {% endif %}
{% endfor %}
```

###### Tip

When using Jinja to access data in a dictionary, you can use the traditional Python syntax `dict['key']` or the shorthand form `dict.key` (as we’ve been showing). These two are identical. If you’re trying to access a key that doesn’t exist, a key error will be raised. However, you can also use the `get()` method in Jinja if it’s an optional key or if you want to return another value if the key doesn’t exist—for example, `dict.get(key, 'UNKNOWN')`.

As mentioned previously, it’s bad form to embed data into your Python applications (see the `interfaces` list of dictionaries from the previous example). Instead, let’s place that data into its own YAML file and rewrite our application to import this data before using it to render the template. This is a good practice, because it allows someone with no Python experience to edit the network configuration by simply changing this simple YAML file.

[Example 9-7](#templates-jinja-yaml-file-switchport) shows a YAML file that is written to be identical to your `interfaces` list in [Example 9-6](#templates-jinja-iterating-list-dicts).

##### Example 9-7. YAML file for switchport configurations

```
---
- name: GigabitEthernet0/1
  desc: uplink port
  uplink: true
- name: GigabitEthernet0/2
  desc: Server port number one
  vlan: 10
- name: GigabitEthernet0/3
  desc: Server port number two
  vlan: 10
```

As we explored in [Chapter 8](ch08.html#dataformats), importing a YAML file in Python is easy. As a refresher, here’s our full Python application, but instead of the static, embedded list of dictionaries, you’re simply importing a YAML file to get that data:

```
from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("template.jinja")

with open("data.yml") as f:
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))
```

You can reuse the same template from [Example 9-6](#templates-jinja-iterating-list-dicts) and achieve the same result—but this time, the data that you’re using to populate your template comes from an external YAML file, which is a bit easier to maintain. The Python file now contains only the logic of pulling in data and rendering a template. This makes for a more maintainable template-rendering system.

This covers the basics of loops and conditionals. In this section, we’ve explored only a portion of what’s possible. Explore these concepts on your own and apply them to your own use cases.

## Using Jinja Filters

The data structures (like lists and dictionaries) and basic logical constructs (like loops and conditionals) presented so far are useful, but sometimes something a little more advanced is warranted. What if you want to convert a given bit of input to uppercase before it’s rendered out to the template? Or perhaps you want to reverse the characters in a string? Tasks like these can be prohibitively difficult or even impossible with what we’ve covered in this chapter up to this point.

Jinja filters provide an extremely powerful answer to these and many more problems. You can think of them like little modular functions you can call upon at any point in your templates. They generally work by taking in data or text as input (such as a variable you are passing in to the template environment), performing some kind of specialized task on that data, and then outputting the result.

The syntax for using filters in a Jinja template is simple. In the same way that you can pipe output from a command into another command in a terminal shell on a Linux distribution, you can take the result of a Jinja statement and pipe it into a filter. The resulting text will make it into the rendered output of your template.

[Example 9-8](#templates-jinja-filter-syntax) uses the familiar double-brace syntax to specify that you want to use a variable named `hostname`. However, before the contents of `hostname` are rendered into the final output for this template, they are first *piped* (using `|`) into the filter called `myfilter`. The output from that filter is then used to populate that portion of the template.

##### Example 9-8. Basic filter syntax in Jinja

```
{{ hostname|myfilter }}
```

This is a bit contrived, so let’s move on to practical examples of Jinja filters in action.

### Using the upper Jinja filter

Let’s take the preceding template and use a built-in filter called `upper` to capitalize the descriptions for each interface configuration:

```
{% for interface in interface_list %}
interface {{ interface.name }}
  description {{ interface.desc|upper }}
  {% if interface.uplink %}
    switchport mode trunk
  {% else %}
    switchport access vlan {{ interface.vlan }}
    switchport mode access
  {% endif %}
{% endfor %}
```

This filter, built into the Jinja2 library for Python, capitalizes the text piped to it.

### Chaining Jinja filters

You can also chain filters, in much the same way that you might pipe commands together in Linux. Let’s use the `reverse` filter to take your capitalized text and print it backward:

```
{% for interface in interface_list %}
interface {{ interface.name }}
  description {{ interface.desc|upper|reverse }}
  {% if interface.uplink %}
    switchport mode trunk
  {% else %}
    switchport access vlan {{ interface.vlan }}
    switchport mode access
  {% endif %}
{% endfor %}
```

This results in the following output:

```
interface GigabitEthernet0/1
  description TROP KNILPU
  switchport mode trunk

interface GigabitEthernet0/2
  description ENO REBMUN TROP REVRES
  switchport access vlan 10
  switchport mode access

interface GigabitEthernet0/3
  description OWT REBMUN TROP REVRES
  switchport access vlan 10
  switchport mode access
```

To recap, our original description for GigabitEthernet0/1 was first `uplink port`, and then it was `UPLINK PORT` because of the `upper` filter, and then the `reverse` filter changed it to `TROP KNILPU`, before the final result was printed into the template instance.

### Creating custom Jinja filters

This is all great, and tons of other great built-in filters are documented within the Jinja specification. But what if you want to create your own filter? Perhaps there’s something specific to network automation that you would like to perform in your own custom filter that doesn’t come with the Jinja2 library?

Fortunately, the library allows for this. [Example 9-9](#templates-jinja-custom-filter-python-full) shows a full Python script defining a new function, `get_interface_speed()`. This function is simple—it looks for certain keywords like `gigabit` or `fast` in a provided string argument and returns the current Mbps value. It also loads all your template data from a YAML file, as shown in previous examples.

##### Example 9-9. Full Python script with custom Jinja filter

```
from jinja2 import Environment, FileSystemLoader         
import yaml                                              

ENV = Environment(loader=FileSystemLoader('.'))          

def get_interface_speed(interface_name):
    """ get_interface_speed returns the default Mbps value for a given
        network interface by looking for certain keywords in the name
    """

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

ENV.filters['get_interface_speed'] = get_interface_speed 
template = ENV.get_template("template.jinja")

with open("data.yml") as f:                              
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Imports the Jinja2 and PyYAML libraries.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Declares the template environment.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Filters are added to the `ENV` object after declaration. We’re actually passing in the `get_interface_speed` function and not running it—the template engine will execute this function when we call `template.render()`.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

We load the YAML file and pass it in to the template when rendering it.

With a slight modification to our template, as shown in [Example 9-10](#templates-full-python-custom-filter), we can leverage this filter by passing `interface.name` into the `get_interface_speed` filter. The resulting output will be whatever integer the function decides to return. Since all interface names are Gigabit Ethernet, the speed is set to `1000`.

##### Example 9-10. Updated Jinja template leveraging the custom filter

```
{% for interface in interface_list %}
interface {{ interface.name }}
  description {{ interface.desc|upper|reverse }}
  {% if interface.uplink %}
  switchport mode trunk
  {% else %}
  switchport access vlan {{ interface.vlan }}
  switchport mode access
  {% endif %}
  speed {{ interface.name|get_interface_speed }}
{% endfor %}
```

###### Tip

You don’t always have to create your own function to pass in as a Jinja filter. Plenty of libraries provide helpful functions that you can import and simply pass right into the Jinja2 environment.

## Template Inheritance in Jinja

As you create bigger, more capable templates for your network configuration, you may want to be able to break templates into smaller, more specialized pieces. It’s common to have a template for VLAN configuration, one for interfaces, and maybe another for a routing protocol. This kind of organizational tool, while optional, can allow for much more flexibility. The question is, how do you link these templates together in a meaningful way to form a full configuration?

Jinja allows you to perform inheritance in a template file, which is a handy solution to this problem. For instance, you may have a *vlans.jinja* file that contains only the VLAN configuration, and you can inherit this file to produce a VLAN configuration in another template file. You might be writing a template for interface configuration, and you want to also produce a VLAN configuration from another template. [Example 9-11](#templates-jinja-inheritance) shows how this is done by using the `include` statement.

##### Example 9-11. Using `include` for Jinja template inheritance

```
{% include 'vlans.jinja' %}

{% for name, desc in interface_dict.items() %}
interface {{ name }}
  description {{ desc }}
{% endfor %}
```

This renders *vlans.jinja* and inserts the resulting text into the rendered output for the template that includes it. Using the `include` statement, template writers can compose switch configurations made up of modular parts. This is great for keeping multiple template files organized.

Another inheritance tool in Jinja is the `block` statement. This is a powerful but more complicated method of performing inheritance, as it mimics object inheritance in more formal languages like Python. Using blocks, you can specify portions of your template that may be overridden by a child template, if present. If a child template is not present, this portion of the rendered output will still contain some default text.

[Example 9-12](#templates-jinja-blocks) shows how blocks are declared within a parent template.

##### Example 9-12. Jinja block definition

```
{% for interface in interface_list %}
interface {{ interface.name }}
  description {{ interface.desc }}
{% endfor %}
!
{% block http %}
  no ip http server
  no ip http secure-server
{% endblock %}
```

Call this template *no-http.jinja*, indicating that you’d like to normally turn off the embedded HTTP server in your switch. However, you can use blocks to provide greater flexibility here. You can create a child template called *yes-http.jinja* that is designed to override this block and output the configuration that enables the HTTP server if that’s what you want; see [Example 9-13](#templates-jinja-blocks-child).

##### Example 9-13. Jinja block reference

```
{% extends "no-http.jinja" %}
{% block http %}
  ip http server
  ip http secure-server
{% endblock %}
```

This allows you to enable the HTTP server simply by rendering the child template. The first line in [Example 9-13](#templates-jinja-blocks-child) extends the parent template *no-http.jinja* so all of the interface configurations will still be present in the rendered output. However, because you’ve rendered the child template, the `http` block of the child overrides that of the parent. Using blocks in this way is useful for portions of the configuration that may need to change but aren’t properly served by traditional variable substitution.

The [Jinja documentation on template inheritance](https://oreil.ly/RqRua) goes into much more detail and is a great resource to keep bookmarked.

## Variable Creation in Jinja

Jinja allows you to create variables within a template by using the `set` statement. A common use case is variable shortening. Sometimes you have to go through several nested dictionaries or Python objects to get what you want, and you may want to reuse this value several times in your template. Rather than repeat a long string of properties or keys, use the `set` statement to represent a particular value with a much smaller name:

```
{% set int_desc = sw01.config.interfaces['ge0/1']['description'] %}
{{ int_desc }}
```

While Jinja is clearly the dominant templating tool in network automation, it isn’t the only one. At times another tool is more appropriate, and we cover a few of them in the following sections.

# Extensible Stylesheet Language Transformations

As discussed in [Chapter 8](ch08.html#dataformats), XML is an extremely popular data format that’s typically well supported by major NOSs for automation purposes and more. XML enjoys a rich ecosystem of tools surrounding it.

One of these is a fairly robust templating format called *Extensible Stylesheet Language Transformations* (*XSLT*). XSLT is typically used for applying transformations to XML data, such as to convert that data into XHTML or other XML documents. However, like Jinja, it can be used to create templates for any arbitrary document format, and given its affinity to the XML ecosystem, is an important option to have in your repertoire if you’re going to be working with XML frequently.

###### Note

As with XML itself, the XSLT specification is defined by [W3C](https://oreil.ly/vnjJl).

Let’s look at a practical example of populating an XSLT template with meaningful data in Python so that a resulting document can be achieved. The first thing you need is raw data to populate your template. This XML document will suffice:

```
<?xml version="1.0" encoding="UTF-8"?>
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

This amounts to a list of authors, each with `<firstName>` and `<lastName>` elements. The goal is to use this data to generate an HTML table that displays these authors, via an XSLT document. An XSLT template to perform this task might look like [Example 9-14](#templates-xslt-template).

##### Example 9-14. XSLT template

```
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output indent="yes"/>
<xsl:template match="/">
  <html>
  <body>
  <h2>Authors</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th style="text-align:left">First Name</th>
        <th style="text-align:left">Last Name</th>
      </tr>
      <xsl:for-each select="authors/author">
      <tr>
        <td><xsl:value-of select="firstName"/></td>
        <td><xsl:value-of select="lastName"/></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
```

A few notes on this:

- A basic `for-each` construct is embedded in what otherwise looks like valid HTML. This is a standard practice in template language—the static text remains static, and little bits of logic are placed where needed.
- The `for-each` statement uses a *coordinate argument* (listed as `authors/author`) to state exactly which part of your XML document contains the data you wish to use. This is called *XPath*, a syntax used within XML documents and tools to specify a location within an XML tree.
- You use the `value-of` statement to dynamically insert a value (like a variable in a Python program) as text from your XML data.

Assuming your XSLT template is saved as *template.xslt* and your data file as *data.xml*, you can return to your trusty Python interpreter to combine these two pieces and come up with the resulting HTML output:

```
from lxml import etree
xslRoot = etree.fromstring(bytes(open("template.xslt").read(), encoding='utf8'))
transform = etree.XSLT(xslRoot)

xmlRoot = etree.fromstring(bytes(open("data.xml").read(), encoding='utf8'))
transRoot = transform(xmlRoot)
```

This produces a valid HTML table, as shown in [Figure 9-2](#templates-xslt-table).

![npa2 0902](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_0902.png)

###### Figure 9-2. HTML table produced by XSLT

XSLT also provides additional logic statements:

<if>Output the given element(s) only if a certain condition is met.

<sort>Sort elements before writing them as output.

<choose>A more advanced version of the `if` statement (allows `else if` or `else` style of logic).

You can take this example even further and use this concept to create a network configuration template using configuration data defined in XML; see [Example 9-15](#templates-xslt-xml-interface-data).

##### Example 9-15. XML interface data

```
<?xml version="1.0" encoding="UTF-8"?>
<interfaces>
    <interface>
        <name>GigabitEthernet0/0</name>
        <ipv4addr>192.168.0.1 255.255.255.0</ipv4addr>
    </interface>
    <interface>
        <name>GigabitEthernet0/1</name>
        <ipv4addr>172.16.31.1 255.255.255.0</ipv4addr>
    </interface>
    <interface>
        <name>GigabitEthernet0/2</name>
        <ipv4addr>10.3.2.1 255.255.254.0</ipv4addr>
    </interface>
</interfaces>
```

Then, you can create an XSLT template to take this data and render it out into a new document that contains your valid network configuration, as shown in [Example 9-16](#templates-xslt-router-config).

##### Example 9-16. XSLT template for router config

```
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <xsl:for-each select="interfaces/interface">
interface <xsl:value-of select="name"/>
    ip address <xsl:value-of select="ipv4addr"/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
```

With these XML and XSLT documents, you can get a rudimentary router configuration in the same way you generated an HTML page:

```
interface GigabitEthernet0/0
    ip address 192.168.0.1 255.255.255.0
interface GigabitEthernet0/1
    ip address 172.16.31.1 255.255.255.0
interface GigabitEthernet0/2
    ip address 10.3.2.1 255.255.254.0
```

As you can see, it’s possible to produce a network configuration by using XSLT. However, it is admittedly a bit cumbersome. You will likely find Jinja a much more useful templating language for creating network configurations, as it has a lot of features that are conducive to network automation.

# Go Templates

The Go programming language has a [package for working with templates](https://oreil.ly/w1RS0) in the standard library, importable as `text/template`. This package implements a template language that is tightly integrated with the Go programming language. So, if you’re working with Go, this package is a strong choice for building and rendering templates.

While the template language implemented by this package is specific to Go, and therefore includes some familiar Go-esque keywords and syntax, it does share some familiar concepts with other template languages like Jinja. For instance, the actual text replacement syntax in Go templates also uses double braces: `{{ }}`.

To get started, you’ll create a simple template using a string literal defined in your Go program, and print the results to the terminal; see [Example 9-17](#templates-go-template-simple).

##### Example 9-17. Simple Go template

```
package main

import (
  "os"
  "text/template"
)

func main() {
  // We can create an inline template using the Parse() method of the
  // template.Template type
  //
  // Note that simpleTemplate is just an arbitrary name chosen for this example.
  tmpl, err := template.New("simpleTemplate").Parse(`{{ "foobar" | print }}`)
  if err != nil {
    panic(err)
  }

  // We can render the template with Execute, passing in os.Stdout
  // as the first parameter, so we can see the results in our terminal
  err = tmpl.Execute(os.Stdout, nil)
  if err != nil {
    panic(err)
  }
}
```

###### Note

[Example 9-17](#templates-go-template-simple) shows a full working Go template that can be run with `go run`, but the following examples are simplified to show only the most relevant code. Full working versions of the following examples can be found at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch09-templates*](https://github.com/oreilly-npa-book/examples/tree/v2/ch09-templates).

You’re not even doing any variable substitution here. Go templates allow you to define string literals within the template itself, thus the escaped double quotes. So, this example simply results in the text `foobar`.

Also note that you don’t have to send the results to `stdout`. Anything that satisfies `io.Writer` can be used as the first parameter to `Execute()`, including a file opened via `os.Create()`, as shown in [Example 9-18](#templates-go-template-simple-file).

##### Example 9-18. Rendering a template to a file

```
tmpl, err := template.New("simpleTemplate").Parse(`{{ "foobar" | print }}`) 
if err != nil {
  panic(err)
}

file, err := os.Create("./output.txt")                                      
if err != nil {
  panic(err)
}

err = tmpl.Execute(file, nil)                                               
if err != nil {
  panic(err)
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Creates an inline template by using the `Parse()` method of the `template​.Tem⁠plate` type.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Creates the file to contain the output.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Anything that satisfies `io.Writer` can be passed as the first parameter to `Execute()`, which includes the `file` returned by `os.Create`.

To keep the remaining examples simple, you’ll continue to write to `stdout`.

Now, on to some more practical examples. As with Jinja, the chief use case for Go templates in network automation is to inject some kind of structured data into a predefined output format. This allows you to define the text that should more or less remain consistent within the template, and pass data retrieved from a user parameter or API call to “fill in” the parts of the template that require it.

For instance, you may have a `Switch` struct with the fields `Hostname` and `InterfaceCount` that you wish to use to pass data into your template; see [Example 9-19](#templates-go-template-struct).

##### Example 9-19. Passing data into a template via a struct

```
type Switch struct {                
  Hostname       string
  InterfaceCount uint
}

sw01 := Switch{"sw01", 48}          

tmpl, err := template.New(
    "switchTemplate").Parse("Device {{.Hostname}} has {{.InterfaceCount}} interfaces\n"
)                                   
if err != nil {
  panic(err)
}

err = tmpl.Execute(os.Stdout, sw01) 
if err != nil {
  panic(err)
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

First, we must define the struct that represents a switch.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

Then we instantiate this struct into a variable `sw01`.

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

We can refer to the fields of the struct by using the `.field name` syntax.

![4](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/4.png)

Our input struct is passed in as the second parameter to `Execute()`.

You may have noticed you were able to refer to the `Hostname` field of your struct via a leading dot (`.`). In the package documentation, this is literally referred to as *dot* and is a reference to whatever type is passed in to your template context. In this case, dot is a simple struct with fields you could refer to by name, but this doesn’t have to always be the case, as you’ll see in the next few examples.

This prints the following:

```
Device sw01 has 48 interfaces
```

Instead of a single struct, you can pass in a slice of multiple `Switch` elements and iterate over them using the `range` keyword:

```
type Switch struct {
  Hostname       string
  InterfaceCount uint
}

// switches is a slice that represents all our Switch instances
switches := []Switch{
  {"sw01", 48},
  {"sw02", 24},
  {"sw03", 48},
}

// As with Jinja, it's often better to define templates in a multiline string
// like tmplStr below, or in a separate file that is read in before rendering.
tmplStr := `
{{range $i, $switch := .}}
Device {{$switch.Hostname}} has {{$switch.InterfaceCount}} interfaces
{{end}}
`
```

In this case, dot represents your slice, and iterating over this slice in the template is done via `range $i, $switch := .` This is similar to iterating over a slice natively in Go, as the slice is to the right of the short variable declaration operator `:=`, and `i` and `switch` represent the index value of each element and a copy of the element itself, respectively.

Go templates support conditionals as well. You can optionally print a line based on the value of the `Enabled` boolean field:

```
type Switch struct {
  Hostname       string
  InterfaceCount uint
  Enabled        bool
}

// switches is a slice that represents all our Switch instances
switches := []Switch{
  {"sw01", 48, true},
  {"sw02", 24, true},
  {"sw03", 48, false},
}

tmplStr := `
{{range $i, $switch := .}}
{{if $switch.Enabled}}
Device {{$switch.Hostname}} has {{$switch.InterfaceCount}} interfaces
{{end}}
{{end}}
`
```

Your struct thus far has been fairly simple, and you might wonder if you can simplify it to a `map` and iterate over that. You can!

```
switches := map[string]int{
  "sw01": 48,
  "sw02": 24,
  "sw03": 48,
}

// Since we're now iterating over a map, the two created variables after the
// range keyword represent each key/value pair
tmplStr := `
{{range $hostname, $ifCount := .}}
Device {{$hostname}} has {{$ifCount}} interfaces
{{end}}
`
```

When discussing Jinja, we explored the use of filters to further manipulate data within the template and even defined our own custom filter. You can do the same in Go templates, albeit with a slightly different terminology. Go templates include a feature called *pipelines*, which can be a sequence of commands delimited by the pipe operator (`|`). Go has several built-in commands, but you’ll see how to define your own. While the terms differ, the syntax is extremely similar to Jinja.

Let’s go back to passing a `Switch` struct as the `data` parameter for your template, but instead of an integer field representing the number of interfaces, this struct can contain a slice of strings, so you can actually have the names of each interface. This will allow you to iterate over the interface names if you want to, but at the same time, you can also still print the total number of interfaces by passing that field through a pipeline, using the `len` command, as shown in [Example 9-20](#templates-go-template-pipeline).

##### Example 9-20. Go template pipelines

```
// A fairly small switch, indeed
sw01 := Switch{"sw01", []string{
  "ge-0/0/1",
  "ge-0/0/2",
  "ge-0/0/3",
  "ge-0/0/4",
}}

tmplStr := "Device {{.Hostname}} has {{ .Interfaces | len }} interfaces\n"
```

The built-in `len` command prints the length of the value passed to it, rather than the value itself. This results in the following:

```
Device sw01 has 4 interfaces
```

Other commands are available, such as `slice` for subslicing an argument, `and` and `or` for comparing two arguments for emptiness, and `call` for calling a function. However, you can create your own function and make it available to the template context on creation. For instance, you can create a function called `IfParse()` for parsing the speed and location details out of a string interface name:

```
type Interface struct {
  Speed int
  FPC   int
  PIC   int
  Port  int
}

func IfParse(ifaceStr string) Interface {

  iface := Interface{}

  ifSplit := strings.Split(ifaceStr, "-")

  speeds := map[string]int{
    "ge": 1,
    "xe": 10,
    "et": 40,
  }
  iface.Speed = speeds[ifSplit[0]]

  locSplit := strings.Split(ifSplit[1], "/")

  fpc, _ := strconv.Atoi(locSplit[0])
  iface.FPC = fpc

  pic, _ := strconv.Atoi(locSplit[1])
  iface.PIC = pic

  port, _ := strconv.Atoi(locSplit[2])
  iface.Port = port

  return iface
}
```

To use this function, you must create a mapping between the function itself and a name you can refer to in your template. The `template` package has a function called `FuncMap()` you can use to create this. Then, you must remember to pass in this function map by using the `Funcs()` method of the template object, as shown in [Example 9-21](#templates-go-template-using-function).

##### Example 9-21. Using custom functions in Go templates

```
fmap := template.FuncMap{"ifparse": IfParse}                           

sw01 := Switch{"sw01", []string{
  "ge-0/0/1",
  "ge-0/0/2",
  "ge-0/0/3",
  "ge-0/0/4",
}}

tmplStr := `
{{range $i, $interface := .Interfaces}}
{{with $loc := $interface | ifparse}}
Interface {{$interface}}   port {{$loc.Port}}
{{end}}
{{end}}
`                                                                      

tmpl, err := template.New("switchTemplate").Funcs(fmap).Parse(tmplStr) 
if err != nil {
  panic(err)
}
```

![1](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/1.png)

Creates a mapping of functions to names we can refer to in the template.

![2](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/2.png)

In this template, we’re first creating a new variable `loc` by pipelining `$interface` into the custom function `ifparse`. Since `ifparse` returns an `Interface` type, we can then refer to the fields of that struct directly!

![3](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/3.png)

Don’t forget to pass in the `FuncMap` by using the `Funcs()` method, as shown here.

This prints the following:

```
Interface ge-0/0/1   port 1
Interface ge-0/0/2   port 2
Interface ge-0/0/3   port 3
Interface ge-0/0/4   port 4
```

There is much more to explore with Go templates, but we’ve covered the basics. Again, if you’re working with Go and already familiar with the basic concepts we previously discussed with Jinja, you could do worse than to skill up on Go templates.

# Summary

You don’t have to work directly with programming languages like Go and Python in order to use templates, as we’ve done in this chapter. As we discuss in [Chapter 12](ch12.html#automationtools), tools like Ansible and Nornir include native support for template languages like Jinja2, allowing you to populate your templates with data available within those platforms.

Here are a few parting thoughts on using templates for network automation:

- Keep the templates simple. Leveraging loops and conditionals to enhance your templates is fine, but don’t go overboard. Jinja isn’t as robust as a fully featured, general-purpose programming like Python, so keep the more advanced stuff out of the template.
- Leverage template inheritance to reuse portions of configurations that don’t need to be duplicated.
- Remember, syntax and data should be handled separately. For instance, keep VLAN IDs in their own data file (maybe YAML) and the CLI syntax to implement those VLANs in a dedicated template.
- Templates are just text files, so you can and should use version control (i.e., Git) to track changes and collaborate with others. We discuss this in [Chapter 11](ch11.html#sourcecontrol).
