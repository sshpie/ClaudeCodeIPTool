# Introduction

This book will teach you practices to make your Kubernetes deployments more secure. It will introduce you to security features in Kubernetes and tell you about other things you should be aware of in the context of containerized applications running on Kubernetes; for example, container image best practices from a security point of view.

We describe practical techniques and provide an [accompanying website](https://kubernetes-security.info/) with references and recipes, so if you want to follow along, check it out!

# Why We Wrote This Book

Kubernetes has rapidly become a popular choice for deploying code “in the cloud” and is now used by enterprises of all sizes to deploy mission-critical applications. However, information about securing Kubernetes is distributed across the internet and in the code itself. We want to make it easier for anyone who is using Kubernetes to think about and address the security of their deployments by gathering information into one resource.

# Who Is This Book For?

This book is written for developers, operation folks, and security professionals who are using Kubernetes. Please note that we assume familiarity with basic Kubernetes concepts. If you don’t have that familiarity yet, a great book to get started is [*Kubernetes: Up and Running*](https://bit.ly/kubernetes-up-and-running) by Kelsey Hightower et al. (O’Reilly). In addition, [*Kubernetes Cookbook*](https://bit.ly/kubernetes-cookbook) by Michael Hausenblas (one of the authors of this book) and Sébastien Goasguen (O’Reilly) provides recipes for common tasks.

In this book, we tackle the technical aspects of Kubernetes security, but sidestep cultural and organizational issues, such as who should be responsible for implementing and ensuring the advice we offer. We do suggest that this is something you pay attention to, as [no amount of technology will fix a broken culture](http://bit.ly/2xOVcEy).

# Which Version of Kubernetes?

Kubernetes is an evolving project with improvements being made all the time. At the time of writing, the latest release of Kubernetes is v1.11. Several security-related features have been added and stabilized over the last few releases, with the general availability of role-based access control (RBAC) in v1.8 particularly worthy of note. With that in mind, we strongly recommend upgrading to v1.8 or newer if you haven’t already.

We expect the advice in this book to be generally applicable to whatever version you are running from v1.8 onward. We point out when a particular version newer than 1.8 is required in order for a recommendation to work.

Via the accompanying website [*kubernetes-security.info*](https://kubernetes-security.info/), we plan to keep you up-to-date as new tooling and best practices become available and as Kubernetes evolves, so keep an eye on this site!

# A Note on Federation

*Federation* is the concept of operating multiple Kubernetes clusters together, with the ability to synchronize and discover resources across them. At the time of writing, the Kubernetes Federation API has no clear path to general availability, so we have left the security of federated clusters out of the scope of this book.

# Acknowledgments

A big thank you to the O’Reilly team, especially Virginia Wilson, for shepherding us through the process of writing this book.

We’re super grateful to our technical reviewers Alban Crequy, Amir Jerbi, Andrew Martin, Ian Lewis, Jordan Liggitt, Michael Kehoe, Seth Vargo, and Tim Mackey, who provided valuable, actionable feedback and advice.
