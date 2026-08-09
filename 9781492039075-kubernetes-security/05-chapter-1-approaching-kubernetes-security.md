# Chapter 1. Approaching Kubernetes Security

Security is a funny, elusive thing. You will rarely hear a security professional describe something as “secure.” You’ll hear that something may be more or less secure than an alternative, but security is dependent on context.

In this book, we will show you ways to make your Kubernetes cluster more secure. Whether you need to apply a particular measure to make your deployment secure enough for your particular use case is something for you to assess, depending on the risks you are running. We hope that if your Kubernetes cluster holds our bank account details or our medical records, you will take all the precautions described herein, at the very least!

We will cover ways that you can configure your Kubernetes cluster to improve security. Your cluster runs containerized workloads, and we will discuss ways to make it more likely that you are running the workloads you expect (and nothing more). We present precautions you can take to limit the likelihood of a breach by an attacker, and to limit the likelihood of that breach resulting in data loss.

In addition, you can use plenty of non-Kubernetes-specific security tools and approaches that are outside the scope of this book. You can layer traditional network firewalls and intrusion-detection systems, in addition to everything that is described here. You may have an air-gapped deployment. And wherever humans interact with your system, they may constitute a risk to security, either maliciously or just due to human error. We don’t pretend to address those issues in this book. As shown in [Figure 1-1](#attack-vectors), there are various ways that an attacker could attempt to compromise your Kubernetes cluster and the applications running on it.

![Kubernetes Attack Vectors](/api/v2/epubs/urn:orm:book:9781492039075/files/assets/kuse_0101.png)

###### Figure 1-1. Kubernetes attack vectors

In this book, we explain controls, configurations, and best practices that you can apply to mitigate all these potential modes of attack. We present several aspects of Kubernetes security:

Configuring Kubernetes for security[Chapter 2](ch02.html#ch_k8s_ctrl) considers the configuration of Kubernetes components, and [Chapter 3](ch03.html#ch_authn) and [Chapter 4](ch04.html#ch_authz) discuss how to limit access to Kubernetes resources so that they are accessible to only the people and applications that need them.

Preventing your application workloads from being exploited[Chapter 5](ch05.html#ch_images) explains approaches that ensure you are not running code with known vulnerabilities on your Kubernetes cluster. [Chapter 6](ch06.html#ch_running) presents additional ways you can limit the behavior of containers at runtime, making it harder for an attacker to abuse those containers.

Protecting credentials[Chapter 7](ch07.html#ch_secrets) discusses how to store credentials and pass them safely into applications.

We finish in [Chapter 8](ch08.html#ch_advanced) with some advanced ideas for securing your Kubernetes cluster.

But before we get started on Kubernetes-specific information, let’s introduce a few important general security concepts that we’ll use in the rest of the book.

# Security Principles

In this section, we’ll discuss three important principles that can be used to increase security: defense in depth, least privilege, and limiting the attack surface.

## Defense in Depth

Picture a medieval castle under siege. It has strong, high walls to keep undesirables out. The wall is surrounded by a moat, with access via a drawbridge that is lowered only occasionally to let people in and out. The castle has thick doors, and bars across any windows. Archers patrol the castle walls, ready to fire at any attacker.

The castle has several layers of defense. Attackers who can swim might be prepared to cross the moat, but then they have the walls to scale, and the likelihood of being picked off by an archer. It might be possible to compromise any given layer in the defensive structure, but by having several layers, it’s hard for an attacker to successfully enter the castle.

In the same way, it’s preferable to have several layers of defense against attacks on your Kubernetes cluster. If you’re relying on a single defensive measure, attackers might find their way around it.

## Least Privilege

The [*principle of least privilege*](http://bit.ly/2xSoQIW) tells us to restrict access so that different components can access only the information and resources they need to operate correctly. In the event of a component being compromised, an attacker can reach only the subset of information and resources available to that component. This limits the “blast radius” of the attack.

Consider an example of an e-commerce store. Let’s assume it is built using a “microservice” architecture with functionality broken into small, discrete components. Even if product and user information is held in the same database, different microservices might each be granted access to only the appropriate parts of that database. A product-search microservice needs read-only access to the product tables, but nothing more. If this microservice somehow gets compromised, or simply has a bug, the broken service can’t overwrite product information (because it has only read access) or extract user information (because it has no access to that data at all). Applying the principle of least privilege means that we make it more difficult for an attacker to cause damage.

###### Note

Microservices, as [defined by Martin Fowler](https://martinfowler.com/articles/microservices.html), are a particular design of software apps, essentially a collection of independently deployable services.

The same principle can apply to humans too. In some organizations, sharing production credentials with all staff may make sense. In others, it’s critical that only a small set of people have access, especially if that access is to sensitive information such as medical or financial records.

## Limiting the Attack Surface

The [*attack surface*](https://en.wikipedia.org/wiki/Attack_surface) is the set of all possible ways a system can be attacked. The more complex the system, the bigger the attack surface, and therefore the more likely it is that an attacker will find a way in.

Consider our castle metaphor again: the longer the length of the castle walls, the more archers we would need to patrol them effectively. A circular castle will be most efficient from this point of view; a complicated shape with lots of nooks and crannies would need more archers for the same interior volume.

In software systems, the fundamental way to reduce the attack surface is to minimize the amount of code. The more code that’s present in the system, the more likely it is that it has vulnerabilities. The greater the complexity, the more likely that latent vulnerabilities exist, even in well-tested code.

Now that we have established some security concepts, let’s see how we apply them to the configuration of a Kubernetes cluster.
