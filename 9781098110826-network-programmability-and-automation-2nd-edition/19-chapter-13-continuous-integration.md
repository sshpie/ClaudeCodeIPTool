# Chapter 13. Continuous Integration

In this chapter, we’re going to change direction a little bit. Until now, this book has provided details on specific tools and technologies that you can learn, all for the purpose of applying them toward network automation. However, it would be improper to assume that network automation is all about shiny new tools—in fact, that’s only one piece of the bigger picture.

This chapter instead focuses much more on optimizing the processes around network management and operations. Armed with knowledge of the specific tools and technologies mentioned in previous chapters, you can use this chapter as a guide for using those tools to solve the *real*, challenging problems that network operators at any scale are facing. This chapter answers questions like these:

- How can I use network automation to produce a more stable, more available network?
- How can I help the network move as quickly as the rest of the business demands, without compromising on availability?
- What kind of software or tools can I use to help me implement better processes around my network?

Networking touches *every* other area of IT, and any outages, policy changes, or impediments to efficient process will impact any technology connected to the network. In modern times, these impacts are felt by every other technology discipline. This has caused the rest of IT and the business at large to view the network as something that should “get out of the way” and “just work.” These days, the network is called upon to be always accessible and be more flexible at a more rapid pace than ever before, ensuring that it supports any service or application the business requires.

The reality is there is no magic bullet here; accomplishing these goals requires discipline as well as a disruption of your existing processes and communication silos. It also takes a significant amount of work, learning, and new tools. That work may seem like you’re just adding more complexity, but it will pay off in the long run by adding both stability and speed to your network operations processes.

One common underlying theme is the removal of humans from the direct control path of the network. You would be right to be skeptical of this idea, since we’ve talked about automating humans out of a job for a long time. However, removal of humans from direct control is not the same thing as removing humans entirely. Today, humans maintain direct control over the network by forming a manual, human pipeline for making changes to the network, as illustrated in [Figure 13-1](#cicd-humans-direct).

![npa2 1301](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1301.png)

###### Figure 13-1. Humans in the direct path of a network

This technique has proven to be slow and arduous, while also not providing much, if any, additional reliability to making changes on the network. This method mostly just gets in the way, while providing the illusion of safety around making changes.

When we talk about removing humans from the direct path, we’re talking about *continuous integration* (*CI*)—that is, automating the discrete tasks that should be taking place when we are managing infrastructure change, and freeing technical resources to sit above that pipeline, improving it and making it more efficient ([Figure 13-2](#cicd-automated-change)).

As a result of this fundamental shift toward CI, we can introduce real protections against human error in network operations instead of the “Change Management Theater” that we’ve relied on historically.

![npa2 1302](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1302.png)

###### Figure 13-2. Automated change with continuous integration

###### Note

As shown in [Figure 13-2](#cicd-automated-change), some organizations hire specialists called *release engineers* to manage the CI pipeline. They’re skilled with tools like Git, testing tools, build servers, and peer review systems. They maintain the pipeline’s integrity so the developers don’t have to. Ultimately, their goal is to automate the process, from laptop to production (thus, *release* engineer).

These days, developers are expected to take more responsibility for the code they write, including deployment and ongoing operations (such as participating in an on-call rotation). An engineer or team may still be responsible for managing the CI/CD pipeline infrastructure, but the role of building a pipeline that produces well-tested, well-vetted code is being distributed to the developers themselves. For this reason, your organization may not have dedicated release engineers, particularly those focused on one team’s development processes.

# Important Prerequisites

To maximize your success in using the concepts in this chapter, you need to keep a few things in mind, as outlined in this section.

## Simple Is Better

One of the best things you can do to enable your network automation has nothing to do with learning to code or using a hot new automation tool—it’s all about your network design. Stay away from snowflakes and strive to deploy network services in a cookie-cutter fashion.

In other words, you may decide you want to deploy network configurations driven by templates, such as those we discussed at length in [Chapter 9](ch09.html#templating). If each of your network devices has a unique configuration with a wide variety of features, it’s going to be fairly difficult to build templates for a large group of devices.

The more thought you put into making your network design simpler and more consistent, the less work you’ll have to do when it comes time to automate network tasks. Often this means staying away from vendor-specific features, or bypassing embedded features entirely and implementing network services right at the compute layer.

## People, Process, and Technology

In the previous chapters, we’ve discussed several great technologies and tools, but a lot more serious challenges face the network industry today—challenges of process and of working with other IT teams that may not share your primary skill set.

We’ve addressed specific technologies and tools that you can use to build efficient systems for network automation. A multitude of technologies can be used for automation—many of which may be new to many network engineers—and it’s important to be aware of them. It’s also important to improve and change the ways that we communicate with other areas of IT and the business at large.

In this chapter, however, we’re going to discuss process enhancements that software developers have used for quite some time to improve the way they make changes to applications. The ultimate goal is to make such changes quickly and push them into production while minimizing the risk of negative impact. There are many important lessons here that can be learned by the network engineering community, especially when considering network automation.

## Learn to Code

First, you don’t have to be a software developer to leverage the concepts in this chapter. In fact, this chapter primarily exists to convey that message. However, you will likely find that no one tool (or even set of tools) will solve all your problems.

You’ll likely have to fill some gaps in your CI journey by writing a custom solution, like a script. Use this as an opportunity to broaden your skill set. As discussed in previous chapters, both Python ([Chapter 6](ch06.html#python)) and Go ([Chapter 7](ch07.html#go)) are easy to start with and powerful enough to suit the vast majority of network automation use cases.

# Introduction to Continuous Integration

Before we dive into how CI is useful within a network automation context, let’s talk about its origins and its value to software development teams.

When we talk about implementing CI, we’re looking to accomplish two primary objectives:

Improve reliabilityLearn from old lessons, and improve quality and stability of the overall system.

Move fasterBe able to respond to the changing needs of the business more quickly.

Before CI, changes to software were often made in large batches, and sometimes it took months for developers to see their features make it into production. This made for incredibly long feedback loops, and if there were any serious issues or new features/requirements, it took a very long time for issues to be addressed. This inefficiency meant not only that new features took much longer to get developed but also that software quality suffered.

Naturally, it would be great if developers could simply make changes and push them directly to production, right? It would certainly solve the speed problem—and developers would be able to see the results of their changes more quickly. However, as you might expect, this is incredibly risky. In this model, it’s easy to introduce bugs into production, which could seriously impact the bottom line for many businesses.

CI (when combined with continuous delivery, which we explore later in this chapter) is the best of both worlds. In this model, we’re quickly pushing changes to production—but we’re doing so within a context that tests and validates these changes, to be more confident that they’re not going to cause problems when they’re manifested in production.

In the sections to come, we discuss some of the components of and concepts related to CI, and then look at how we can apply these concepts to our network automation journey.

## Basics of Continuous Integration

You’ve probably heard horror stories about software teams with insufficient processes deploying code to production directly from their laptops ([Figure 13-3](#cicd-deploy-directly))—or even editing code live on a server. Such changes *may* be peer reviewed, but even in this case, there’s little to no formal guarantee that the change will even work. Nevertheless, we hear about deployments like this being made, usually in the name of “it just needs to get done quickly” or “it’s not a very risky change.”

![npa2 1303](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1303.png)

###### Figure 13-3. Deploying software directly to production

Stories like this are thankfully becoming increasingly rare. The expectations on any online service to maintain a high uptime have never been higher, and the processes for reliably shipping code to production have now been around for decades. In the world of software, there’s really no legitimate excuse for deploying code directly to production without a formal testing and peer-review process.

In contrast, network engineers do this kind of thing all the time. Yet, logging in to an SSH session to a router to make config changes is no less risky than editing the source code of an application live in production. In many ways, it’s even more risky: a developer who screws up a deployment might bring down that application, but a network engineer who screws up a configuration change can cause reverberating effects throughout not only the entire organization’s network, but even the entire internet—e.g., via [BGP route leaking](https://oreil.ly/HVqgR).

Software teams have moved toward a much more rigorous process for deploying code to production. While there is more than one name for this process, one extremely common and important component used in many organizations goes by the name of *continuous integration*. In short, CI is all about being able to merge changes to a source code repository at any time. A team of developers, no matter when they’re working, can integrate changes to a shared repository at any time because tools are in place that allow the team to know—in an automated fashion—that those changes are not going to break the functionality of the overall system.

You might have heard the term *pipeline* used when discussing CI. This is because CI is not one particular technology, but usually a suite of tools and technologies used together to accomplish the goal. Changes to a codebase flow through these tools in a predetermined way, which forms a *CI pipeline*. All changes must go through this pipeline in its entirety before moving on to deployment, as shown in [Figure 13-4](#cicd-deploy-pipeline).

![npa2 1304](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1304.png)

###### Figure 13-4. Deploying software to a CI pipeline

This process may seem like it makes deploying harder and slower. In contrast, it provides a foundation for continuously learning from (and ideally preventing) mistakes, so the deployments that do make it through are much more likely to succeed, which means far less wasted time on rollbacks and troubleshooting. This model has worked well to not slow, but actually accelerate, velocity for software teams to become more agile and provide value more quickly for their organizations. Many of these same benefits can be realized within the network infrastructure domain.

We’ve talked about the basics of CI, so now let’s dive into some of the components and related concepts and technologies you might encounter along the way.

## Continuous Delivery

*Continuous delivery* (CD) is another term closely related to CI that you may have heard. In a CD approach, the software team is continuously providing software that could be deployed into production; they are *delivering* working software in the form of an always-deployable codebase.

###### Note

*Continuous deployment* tends to imply that you’re always pushing new code to production immediately. The industry has lately been using the term *continuous delivery* instead. This term generally means that your code is always in a condition where it *could* be deployed at any time, but doesn’t have to be. Your organization may still wish to keep deployments on a set schedule, such as on a nightly or weekly basis.

CI is fairly easy to apply to network automation (as you’ll see in upcoming sections), but CD requires a bit more thought. The rest of this chapter may blur the lines between CI and CD with respect to network automation, so keep in mind these two questions:

- *What* am I deploying?
- *To what/whom* am I deploying it?

These are important questions to address because they determine your delivery model. For instance, some network teams may perform all their automation with in-house Python applications. This is fairly simple since they are essentially a software development shop within the infrastructure team.

On the other hand is the canonical network automation example: provide some kind of configuration artifact (say, a YAML file) into a Git repository, and have the CI/CD pipeline take it through basic sanity checks before finally calling it with a tool like Ansible, resulting in actual and immediate changes to network devices in production. This may work for some organizations, but this is analogous to a software development team deploying each and every software patch to production immediately—and this is not always desired.

Consider, perhaps, a staging environment to which these changes can be continuously delivered, and whenever the business requires that those changes are finally deployed to production, they can be moved from staging, where (hopefully) they’ve been tested. At the time of this writing, many network vendors have heard our demands for providing virtual images of their platforms, so this is much easier to do than it used to be.

###### Caution

While virtual appliances work great for testing automation, not all are meant to carry production network traffic. Refer to your vendor’s documentation for clarity on this.

You also need to think about rollback procedures. Are you periodically taking the configurations that are in your production Git repository and using them to overwrite the current production configurations, or at least comparing the two? If you’re not, even if you roll back the repository, the production deployment of those configurations may not get rolled back. What will be the impact, based on whether you’re using Ansible or Puppet, or maybe custom Python programs, if you roll back the Git repository? You need to own that layer of your software stack and understand how your tools and software will react (if at all) when your production configurations get rolled back.

The truth is, you’ll likely have to address the CD question on your own. What works for one organization probably won’t work for yours, because of the many tools and languages available for solving network automation problems. However, this chapter should at least provide a starting point and ideas for properly delivering changes to your network in an automated fashion.

## Test-Driven Development

It’s also important to discuss yet another software development paradigm that has seen a growing amount of adoption: *test-driven development* (*TDD*).

Let’s say you’re working as a software developer tasked with creating a new feature in your project. Naturally, you might first gather basic requirements, put together a minimal design, and then move forward with building the feature ([Figure 13-5](#cicd-tdd-before)). We’ll even say that you’re on board with CI, so you will then build unit tests to validate the functionality you’ve built.

Unfortunately, it doesn’t always happen this way. In reality, building tests after the feature has been built is often difficult to justify, or at the very least, deemed less important than the feature itself.

![npa2 1305](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1305.png)

###### Figure 13-5. Software development lifecycle before test-driven development

In practice, this can easily lead to the accumulation of *technical debt*: if you don’t build your tests first, there’s always a temptation to not build them immediately after you develop the desired feature, or to not build them at all. This inevitably leads to gaps in test coverage, and on large projects, this gap only increases over time.

TDD turns this idea on its head. When using TDD, after going through requirements gathering and putting together a basic design, you write a test for that feature *before* the feature is even implemented ([Figure 13-6](#cicd-tdd-after)). Naturally, this means the test will fail, since there’s no code to test against. So, the final validation of this feature is to write code that passes that test (or tests).

![npa2 1306](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1306.png)

###### Figure 13-6. Software development lifecycle after test-driven development

Why use a test-driven approach? The most immediate benefit is the reduction of technical debt; if the tests are built before the feature, there’s no temptation to let test coverage fall behind while the shiny new feature takes priority. However, a bit of a conceptual difference also exists. By writing tests first, the developer must have a strong grasp of how their software is being used—since they’re writing tests to do just that. This is widely believed to improve software quality.

When you apply these concepts to network automation, you begin to realize numerous parallels. The network is as much of a business resource as the applications that flow on top of it. Therefore, it’s important to have adequate testing in place that not only validates any changes made on the network, but also helps warn of any problems ahead of time (capacity planning). Are you gathering detailed statistics about the applications flowing on your network—not just what the SNMP service on your network devices is telling you—but from the perspective of the applications themselves? It’s important as network engineers to learn the lesson that TDD is teaching software developers: understanding how our network is used, and further codifying this understanding into automated testing, is crucial.

Regardless of whether this testing takes the form of an existing off-the-shelf tool, a custom set of tests written in a programming language like Python or Go, or a mixture of the two, the two reasons we care about doing testing apply equally and are the same reasons software developers test their systems:

- We care enough about the quality of our network automation system, our network’s uptime, and the positive experience of our users and applications to ensure that our system is properly tested.
- Enforcing a test-first methodology ensures we maintain a firm understanding of the key metrics and behaviors of our network. This allows us to continue to add new functionality quickly, without compromising on our existing obligations.

By adopting a methodology similar to TDD, we are not only helping to put the applications first, but also building a repeatable process by which we can constantly be *sure* that our network is serving the needs of the application, despite changes to configuration or environment. Later in this chapter, we discuss specific tools and technologies that we can use to accomplish these goals.

## Why Continuous Integration for Networking?

So far, we’ve discussed CI and TDD, and how they provide value to software development teams. From now on, however, we’ll be applying concepts like these exclusively to our network automation journey.

Why are we doing this? What value could CI or TDD have to network engineers? Remember the goals of CI:

Improve reliabilityLearn from old lessons, and improve quality and stability of the overall system.

Move fasterBe able to respond to the changing needs of the business more quickly.

These goals, which have driven results for more stable software and more agile development teams, can also help us create a *more* reliable network—not less. Automation that compromises on either of these two goals is pointless.

For a long time, we’ve thought about and administered our networks as black boxes that happen to be connected to one another, and this mindset isn’t conducive to the practices and concepts implemented in CI. So the first thing to do is start to think about your network as a pool of resources and fluid configurations—a system with ever-changing environments and requirements. Such a mindset requires a change in the way we deploy changes to production.

*CI for networking* means a lot of the same things as the canonical software example—creating a single point where changes to network infrastructure are performed, and testing and reviewing those changes is automated and nonoptional.

# A Continuous Integration Pipeline for Networking

At this point, it’s time to put the high-level CI concepts we’ve discussed into practice. In this section, we’ll go through a few practical examples and tools for helping us achieve the goals we’ve outlined within the context of network automation.

While reading the following examples, keep these tips in mind:

- The tools used in this section are just examples. In every category, you have choices beyond what’s presented here. We encourage you to evaluate the tools available in each category and determine whether they fit your needs.
- This section comes after the previous section for a reason. Implementing these tools without fixing the bad process that has plagued many organizations for years will accomplish nothing.

###### Note

The tools in this section also can be configured in a variety of ways. Only one approach is presented in this section, so remember the fundamental concepts here and adopt the right configuration to realize the same benefits within your organization.

Our CI pipeline for networking has five main components:

- Peer review
- Build automation
- Deployment validation and testing
- Test/dev/staging environment
- Deployment tools and strategies

To illustrate the concepts in this chapter, we’ll use a project called Templatizer, which renders Jinja templates into network device configurations based on data found in YAML data files. Many of the examples center on the Templatizer Git repository hosted on our private Git server.

[Figure 13-7](#cicd-templatizer) serves as a useful illustrative example for our CI journey.

![npa2 1307](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1307.png)

###### Figure 13-7. Templatizer project

###### Note

The concepts in this chapter are generic and apply well beyond the Templatizer project we’re using as a contrived, illustrative example. That said, if you want to obtain a copy of the files that make up this project, you can find them at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch13-cicd*](https://github.com/oreilly-npa-book/examples/tree/v2/ch13-cicd).

## Peer Review

When we talk about peer review in a traditional software sense, we’re typically talking about source code for an application. A developer submits a patch containing diffs to source code files, that patch is posted to the code review system in some way, and a reviewer (or reviewers) looks at the patch and provides comments or approval.

When adapting this portion of the pipeline for network automation, we’re not that far off from this example. Chapters [8](ch08.html#dataformats) and [9](ch09.html#templating) have advocated an IaC approach with network automation, whereby any and all relevant configuration information is treated in the same way a developer would treat source code. In our case, instead of Java code, we might have YAML files or Jinja templates. They’re all just text files, and we can run automated tests on them just the same.

###### Note

Another related term you may have heard in recent years is *GitOps*. GitOps shares a lot of similar ideas with IaC. Both emphasize the use of a version control system like Git to store configuration files and scripts used to manage infrastructure. Whereas IaC can in some circles be thought of as applying to only the infrastructure domain (servers, networking, storage, cloud, etc.), GitOps takes a more holistic approach, using Git as the interface through which all operations professionals manage their platforms, including the application stack.

We’re going to be building on the knowledge you gained about version control in [Chapter 11](ch11.html#sourcecontrol) by using Git to not only control the versions of our various configuration artifacts like YAML files, but also leverage the first stage of this pipeline—peer review—to get an additional pair of eyes on our change to make sure we’re doing the right thing.

If you’ve maintained any form of production IT infrastructure, you’ve likely taken part in change advisory board (CAB) meetings. Perhaps you were responsible for filling out a form describing the configuration change you want to make, and then attending long conference calls to say a few quick words that were carefully constructed to appease the approvers and get them out of your way. This process has deep roots in modern IT, but it doesn’t do much to *actually* minimize risk or provide transparency among related technical teams. This is the old way of doing things.

When we talk about using CI for networking, we start with the idea of peer review, and although it might seem similar to what was just described, fundamental differences exist. In CI, if you want to make the change, you simply cut a new branch in Git and *make the change*. By having our configurations performed in a Git repository that is part of a CI pipeline, we don’t have to ask for permission before doing the work in a branch, because that work is not actually pushed through production until it has been reviewed and merged to main.

This new model has some attractive benefits. With respect to peer review, you no longer need to describe the change you want to make and then hope you get it right when it comes time to implement—now, the description of the change is the same as the change itself. There is no ambiguity about what you’re going to do because it’s displayed right in the peer review system being used. To put your change into production, the approver(s) will simply merge your working branch into main.

When it comes to code review platforms, you have a few options. Here is a non-exhaustive list:

GitHubPopular SaaS offering for reviewing and displaying source code (enterprise edition also available for a cost).

GitLabCommunity edition is open source and free to download and run behind your firewall. There is also a tiered SaaS offering, as well as a closed-source enterprise edition.

GerritOpen source, complicated, but lots of integrations available, and a popular choice for some very large open source projects.

BitbucketAtlassian’s code review and CI/CD platform. Useful if your organization already uses other Atlassian products like Jira or Confluence.

All these options leverage Git for the actual version control portion (and Git is therefore the way that you will interface with them when submitting code), but on top of Git, they all have subtle differences when it comes to their workflow. For instance, with GitHub, you can submit additional changes by simply pushing more commits to the same branch, but with Gerrit, the submitter must always work with the same commit (meaning additional changes require the `--amend` flag).

We’ll be using GitLab throughout this chapter, primarily because it offers a lot for free, and we don’t have to fuss around with setup too much. Know, however, that the other systems may work out better for you.

###### Note

At this point in the book, you should be familiar with not only Jinja templates ([Chapter 11](ch11.html#sourcecontrol)) and YAML ([Chapter 8](ch08.html#dataformats)), but also how to work with a Git repository ([Chapter 11](ch11.html#sourcecontrol)). All three are extremely common components of any CI pipeline for network automation. Additionally, the tools discussed in [Chapter 5](ch05.html#developmentenvironments) will make a reappearance later in this chapter, so it’s a good idea to at least be aware of these. If you skipped over these chapters, you’re encouraged to revisit these concepts, as the remainder of this chapter won’t make much sense otherwise.

As an example, we’ll add some Jinja templates and YAML files so the Templatizer project is able to create configurations for network device interfaces. These examples assume that the Templatizer Git repository has already been cloned to the local filesystem. We’ll start by creating a new Git branch for committing our changes in [Example 13-1](#cicd-new-branch).

###### Note

Full versions of the code examples in this chapter can be found in the book’s GitHub repo at [*https://github.com/oreilly-npa-book/examples/tree/v2/ch13-cicd/templatizer*](https://github.com/oreilly-npa-book/examples/tree/v2/ch13-cicd/templatizer).

##### Example 13-1. Cutting a new branch

```
~$ git checkout -b "add-interface-template"

Switched to a new branch 'add-interface-template'
```

We’re on a branch that is only on your machine (we haven’t run `git push` yet) and it’s on a nonmain branch. So we simply make the change. No waiting for approval before we get started—​we do the work first, and let the work speak for itself when the time comes for approval.

After we’ve added the template and YAML file, Git should notify us that two new files are present but untracked, as shown in [Example 13-2](#cicd-new-untracked).

##### Example 13-2. Making a change to the Templatizer project

```
~$ git status

On branch add-interface-template
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    datafiles/interfaces.yml
    templatizer/templates/interfaces.j2

nothing added to commit but untracked files present (use "git add" to track)
```

We need only make a commit and push to our origin remote (as shown in [Example 13-3](#cicd-commit-push)), which in this case is the GitLab repository shown earlier.

##### Example 13-3. Committing and pushing the change to Templatizer

```
 ~$ git add datafiles/ templatizer/

 ~$ git commit -s -m "Added template and datafile for device interfaces"
 [add-interface-template 4121bfa] Added template and datafile for device interfaces
  2 files changed, 10 insertions(+)
  create mode 100644 datafiles/interfaces.yml
  create mode 100644 templatizer/templates/interfaces.j2

 ~$ git push origin add-interface-template
 Counting objects: 7, done.
 Delta compression using up to 8 threads.
 Compressing objects: 100% (7/7), done.
 Writing objects: 100% (7/7), 718 bytes | 0 bytes/s, done.
 Total 7 (delta 2), reused 0 (delta 0)
 To http://gitlab/Matt/templatizer.git
  * [new branch]      add-interface-template -> add-interface-template
```

The next step is to log in to our code review system (GitLab) and initiate the step that would kick off a peer review. Every code review system has its own workflow, but ultimately they all accomplish the same thing. For instance, Gerrit uses terminology like *change* and *patchset*, and GitHub uses *pull requests*. In short, these tools are a way of saying, “I have a change, and I’d like it to be merged into the main branch” (usually main).

GitLab uses a concept similar to GitHub pull requests called *merge requests*. Now that we’ve pushed our changes to a branch, we can specify in the merge request creation wizard that we’d like to merge the commit we made on `add-interface-template` to the main branch, which is considered stable for this project ([Figure 13-8](#cicd-merge-request)).

After we click through to the follow-up confirmation screen, our merge request is created. Keep in mind that this is still just that—a request. There has still been zero impact to the main branch, and as a result, the current stable version of the Templatizer project. This is just a proposal we’ve made, and will serve as a point of reference for the upcoming peer review.

![npa2 1308](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1308.png)

###### Figure 13-8. Creating a merge request

So the next step is to get our merge request reviewed by someone in authority. This part of the workflow can differ based on the culture of the team, as well as the review platform. Some teams restrict access to the main branch so that only certain senior members can accept merge requests, while other teams use the honor system and ask that each merge request is reviewed by at least one other team member. A common convention is to refrain from merging any changes until someone gives a +1, which is a way of saying, “From my perspective, this change is ready to be merged.” This may happen right away, or a reviewer may have some comments or pointers before they’re ready to give their +1.

Our imaginary teammate Fred is on hand to review our Templatizer change, and we can engage him in any number of ways. Most code review tools have a way of adding a reviewer, which should notify them by email, or you can message them directly. Either way, [Figure 13-9](#cicd-merge-request-comments) shows what Fred will see when reviewing our change in GitLab.

![npa2 1309](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1309.png)

###### Figure 13-9. Fred providing comments to the merge request

As you can see, Fred leaves a message indicating he feels we should add a comment to our template, explaining how it works. It’s not uncommon for a change to go through multiple iterations before being merged, and most platforms have facilities for this. With GitLab, we need to only add another commit to this branch and push to GitLab, and the new commit will be added to this merge request. Fred can easily see these additional changes, and once he is satisfied that this change is ready to be merged, he can do so.

[Figure 13-10](#cicd-merge-request-merge) shows us how GitLab can track this entire event stream for anyone who may want to see the status of this change.

![npa2 1310](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1310.png)

###### Figure 13-10. Change accepted and merged

## Build Automation

Next up is an extremely important topic: *build automation*. This term largely stems from the use of CI tooling as a way of automatically compiling or installing software in order to test it. For instance, a program written in C must be compiled before it can be run in a test environment.

We may not necessarily be compiling software in our pipeline, but we can reuse many of the tasks that software developers will want to automatically perform on every proposed change to the repository. For instance, a pipeline for a Python project may perform static code analysis to ensure that the code conforms to Python’s style guide, PEP 8. In a network automation context, we may only be making changes to YAML files, but we can perform similar checks to automate some of the simple stuff that we don’t want human reviewers to deal with, including verifying that the file is in fact valid YAML (ensuring indentation is correct)!

This is the crux of what makes build automation so valuable. Before even bothering a human reviewer, we can automatically do numerous things to ensure that the reviewer is providing useful comments:

- Static code analysis (checking for proper syntax and adherence to any style guides)
- Unit testing (unit tests, parsing of data files or templates, etc.)
- Integration testing (checking whether a change breaks any existing functionality in the whole system)

With these out of the way, the reviewer can leave comments like “this needs to be more readable,” instead of “add a space here.” For this reason, these automated steps usually take place immediately when a change is submitted (our merge request from the previous example), and a reviewer is engaged only when these checks pass.

This process saves time for both the submitter and the reviewer, since the submitter gets close to immediate feedback if their change breaks something, and the reviewer knows that if a change passes these basic tests, they won’t be wasting their time with simple comments. This approach also produces repeatable, more stable changes to network automation efforts—when a bug is discovered, it can be added to these automated tests to ensure that it doesn’t happen again.

Numerous solutions are available for build automation, which we discuss later in this section. Fortunately, GitLab includes some build automation features natively, so the next few examples stick with that. In addition, much of the automation can be done by scripts in the repository itself, keeping the dependence on the build server to a minimum, and providing a lot of transparency for anyone working with the repository. This is yet another example where IaC is a powerful ally.

Let’s say we make a minor change to our new *interfaces.yml* file, and Fred reviews it. Everything looks good to him, so he gives a +1 and merges the change to the main branch ([Figure 13-11](#cicd-yaml-change)).

![npa2 1311](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1311.png)

###### Figure 13-11. Minor change to YAML

However, we have a problem. This change produces invalid YAML, which shows when we try to run our Templatizer program ([Example 13-4](#cicd-yaml-change-error)).

##### Example 13-4. Error parsing YAML

```
File "/Users/mierdin/Code/Python/templatizer/lib/python3.8/.../scanner.py", line 289,
  in stale_possible_simple_keys "could not found expected ':'", self.get_mark())
yaml.scanner.ScannerError: while scanning a simple key
  in "datafiles/interfaces.yml", line 7, column 1
could not found expected ':'
  in "datafiles/interfaces.yml", line 8, column 14
```

This was a minor change, but Fred is still a human being and overlooks typos like this, just as Matt did. When multiple files undergo multiple changes, this kind of mistake can be an even more common occurrence.

On the other hand, it should be trivial to write a script that checks for this error and provides feedback to our build system ([Example 13-5](#cicd-yaml-change-script)). If we can do this, and configure our automated build system to check for this on all future patches, we should avoid this problem in the future.

##### Example 13-5. Python script to check valid YAML

```
#!/usr/bin/env python3

import os
import sys
import yaml

# YAML_DIR is the location of the directory where the YAML files are kept
YAML_DIR = "%s/../datafiles/" % os.path.dirname(os.path.abspath(__file__))

# Let's loop over the YAML files and try to load them
for filename in os.listdir(YAML_DIR):
    yaml_file = "%s%s" % (YAML_DIR, filename)

    if os.path.isfile(yaml_file) and ".yml" in yaml_file:
        try:
            with open(yaml_file) as yamlfile:
                configdata = yaml.load(yamlfile)

        # If there was a problem importing the YAML, we can print
        # an error message, and quit with a nonzero error code
        # (which will trigger our CI system to indicate failure)
        except Exception:
            print("%s failed YAML import" % yaml_file)
            sys.exit(1)

sys.exit(0)
```

###### Note

[Example 13-5](#cicd-yaml-change-script) shows a simple script that only checks for valid YAML. [Chapter 8](ch08.html#dataformats) introduced a few tools that can perform much more comprehensive validation for a variety of data formats. Including tools like these in your CI/CD pipeline is strongly encouraged.

Once we’ve committed that script to our *tools* directory in the repo, we also need to modify the CI configuration file *.gitlab-ci.yml* since we’re running GitLab (as shown in [Example 13-6](#cicd-run-yaml-script)).

##### Example 13-6. Configuring the CI environment to run the YAML validation script

```
test:
  script:
  - cd tools/ && python validate_yaml.py
```

GitLab will run this script every time a change is proposed. Now that this validator script is in place, let’s take a look at what Fred sees when Matt proposes another change with invalid YAML ([Figure 13-12](#cicd-yaml-build-fail)).

![npa2 1312](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1312.png)

###### Figure 13-12. CI build fails because of invalid YAML

Both Matt and Fred can plainly see that a problem occurred during automated testing. They can also click through to see the details, including a full console log that shows the output of the script, indicating which file had the issue ([Figure 13-13](#cicd-yaml-build-output)).

![npa2 1313](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1313.png)

###### Figure 13-13. YAML validation script output

This is just one example in a multitude of possibilities with respect to automated validation and testing. Templatizer is also a Python project, so we can explore some of the tooling present in that ecosystem to run Python-specific validation and testing as part of this CI pipeline. For instance, Tox is a popular tool for doing all kinds of automated testing within a Python project. The OpenStack community uses Tox to simplify the CI process by summarizing a slew of tasks within a small list of commands; see [Example 13-7](#cicd-tox).

##### Example 13-7. Adding Tox to the CI configuration

```
test:
  script:
  - cd tools/ && python validate_yaml.py
  - tox -epep8  # Checks for PEP8 compliance with Python files
  - tox -epy38  # Runs unit tests
  - tox -ecover # Checks for unit test coverage
```

Again, all these commands must pass without error in order to “pass” the build process. When a reviewer receives a merge request that shows that these checks were passed, they know it’s ready for a real review.

The build automation component of the CI pipeline is crucial and is a great way to keep the workflow efficient, while also helping ensure that past mistakes are not repeated. Here are some additional ideas that may be useful at this stage in the pipeline—explore each in your own journey toward network automation:

- Unit testing any code (e.g., Python)
- Integration testing to ensure that any code can interoperate with other projects and APIs
- Syntax and style validation (both source code as well as data formats like YAML)

In the preceding examples, we used GitLab’s included build automation features. However, you may not be using GitLab, and even if you are, you might wonder if other solutions exist for build automation. There are, in fact, quite a few, and each comes with its own pros and cons. These are some popular general-purpose solutions:

JenkinsThis open source build server has been around for long enough that just about anyone who is a true expert in CI will have experience with it.

GitLabWe covered GitLab while talking about code review options. GitLab is open source (but has a hosted option) and is one of few options containing both code review/repository functionality and build server functionality in one platform.

GitHub ActionsA more recent entrant into the build automation space, this extremely powerful, highly customizable workflow engine is cloud based and obviously tied to GitHub.

CircleCIAlso cloud-based, and able to work with a wide variety of version control systems and platforms.

You’ll also find niche players focused on particular aspects of CI. For instance, Codecov is a cloud-based platform for reporting on test coverage in your projects. You can set up rules in your pipeline that reject any new contributions that don’t at least maintain the current percentage of test coverage, for example. You can use a multitude of more focused platforms and tools like this, so you don’t have to reinvent the wheel.

The good news is, you don’t have to spend months researching all possible options before selecting “the one” that will meet your needs. You can start with a handful and evaluate them over time. And you should not expect to have all your needs met by a single solution, but likely a combination of them, including both off-the-shelf and custom build steps. The reason we refer to the collection of these tools as a *pipeline* is that there’s really no one-size-fits-all approach, and the needs of your team will differ from the needs of another.

## Deployment Validation and Testing

Earlier in this chapter, we talked a lot about the influence that TDD can have on network automation. CI is one place where such an approach can have tremendous benefits on our ability to deploy new changes in an automated way, but with heightened confidence that this change will not negatively impact our production systems.

When we have rigorous, automated tests defined for not only asserting the validity of the configurations that make up our network elements (roughly analogous to unit tests in the software development world), but also the end-to-end UX over our network (validating things like base-level connectivity, expected link/flow performance, etc.), it gives us an incredible safety net that we can use to test changes both before and after we hit production. This forms a feedback loop that we can use to quickly drive further iteration ([Figure 13-14](#cicd-continuous-testing)).

![npa2 1314](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1314.png)

###### Figure 13-14. Continuously testing automated changes

Traditionally, such an approach is rare. We’ve all been in the situation where the best thing we can do to validate that our change didn’t break production is a long-running ping that we watch very carefully while we wait for our `commit` operation to succeed. Fortunately, modern tools have evolved to provide other options.

The methods and tools for validating changes—automated or otherwise—depend on the type and scope of validation you’re pursuing. For instance, if all you’re after is some basic checks that your configuration is valid, maybe a simple Python script that loads a YAML file and renders a template is good enough. As we’ll explore in the next section, you could extend this by uploading this configuration to a virtual topology and verify that at least a virtual instance of your intended network device accepts the configuration as valid.

However, static validation of configuration—especially within the context of a single network device—is often insufficient on its own. After all, the operational state of a device doesn’t always match the configuration. Beyond this, our networks are much more than a collection of isolated boxes; they must all work together as part of a cohesive distributed system to provide a reliable service. To that end, a few other aspects are important to consider as part of your deployment validation strategy:

Operational stateDo your network devices have the operational state (e.g., number of active BGP peers) you would expect, given their configuration?

Basic connectivityCan the users on your network access the applications they need?

End-to-end performanceDoes the network have the bandwidth and latency characteristics you would expect? Has a recent change impacted these characteristics?

As we’ve discussed in the previous sections, not every tool in your pipeline needs to solve all your problems. Using a combination of tools is usually necessary to ensure that you’re able to hit all the layers of validation we’ve just described. Open source tools like [NAPALM](https://oreil.ly/aBhv1) and [Batfish](https://www.batfish.org) as well as commercial tools like [Forward Networks](https://www.forwardnetworks.com) enable you to not only check, but provide ongoing assurance on, operational state and basic connectivity of your network. Other commercial solutions like [NetBeez](https://netbeez.net) and [ThousandEyes](https://www.thousandeyes.com), which is part of Cisco, can give you visibility into the end-to-end performance characteristics of your network. These are just examples; tools are falling in and out of favor all the time.

The important point to consider is how well solutions like these can be integrated with your CI/CD pipeline. Here are good questions to ask of these projects or products:

- How programmable is this solution? Is it designed to fit into a pipeline or only for human interaction (e.g., through the GUI)?
- Are there existing integrations with build systems like Jenkins or GitHub Actions that can be used off the shelf, or do I need to build my own?

Tools like these can provide additional value during failover testing, such as the simulation of a data center failure. Failover testing is an underappreciated activity when it comes to network infrastructure. Often, it’s hard to get the approval to run such a test, and in the rare cases when such approval is obtained, it’s even more difficult to determine how the network and the connected applications are performing. Using these and other tools, we can gather a baseline of what “normal” connectivity and performance looks like, and by running the same tests after a failover, we can have greater confidence that we have sufficient capacity to keep the business running.

###### Tip

As discussed in [Chapter 10](ch10.html#apis), the rise of model-driven telemetry, especially streaming/push-style telemetry, has made it easier than ever before to maintain constant awareness of how well the network is fulfilling its obligations. Using conventionally standardized data models allows us to do this with multiple vendors. Integrating tools that take advantage of these new technologies is something you should consider as part of your pipeline’s validation steps.

The importance of validation as part of not only your pre-deployment checks but also your post-deployment and continuous assurance cannot be overstated. Downloading or buying a solution in isolation is not enough, though; integrating it into your pipeline raises the quality of every change that makes it into production.

## Test/Dev/Staging Environment

In addition to the validation/testing methodologies we’ve discussed thus far, it’s usually desirable to run more real-world testing on the changes we make to our automation solution, before pushing the change to our production systems. For Templatizer, we might want to render real configurations using the Jinja templates and YAML files against virtual devices that mimic the real production devices we’d like to eventually target.

In this case, some of the tools we discussed in [Chapter 5](ch05.html#developmentenvironments) for developing automation solutions against a virtual topology of network devices can be particularly helpful. For instance, tools for creating simulated network topologies give us the ability to develop and quickly iterate on our workflows in as close to a production context as possible, but without the inherent risk that would come from developing these workflows against real, production infrastructure.

It’s common for a virtual reference topology to be reused for both development and testing purposes, as shown in [Figure 13-15](#cicd-reference-topology-reuse).

![npa2 1315](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1315.png)

###### Figure 13-15. Reusing the same virtual topology for development and testing

This reuse allows automation solutions to be vetted much earlier in the development lifecycle. While this can be a valuable approach to creating more reliability in your automation journey, virtual topologies are not a panacea. Here are some factors to be aware of:

- Virtual testing can get you only so far. Some features are simply not possible to test in a virtual NOS, and even those that are often have vastly different performance characteristics than their hardware counterparts.
- As with any test suite or fixture, a virtual topology meant to mimic production is in a perpetual state of entropy. It will take work to ensure that this topology continues to appropriately mirror production and remain a useful ally against deploying bad changes.

In Chapters [5](ch05.html#developmentenvironments) and [12](ch12.html#automationtools), we discussed several tools that are essential for developing network automation solutions. Three tools we explored in those chapters have additional utility in this regard:

VagrantSets up an automated topology of connected VMs, with support for a wide variety of hypervisors.

ContainerlabCreates container-based networking labs using a simple, YAML-based configuration model.

TerraformThis embodiment of IaC allows you to declare resources (both cloud and on-premises) that are then programmatically managed.

All three of these tools have strong support for the IaC methodology we’ve been discussing in this chapter, and are therefore ideal to be used within a CI/CD pipeline for network automation. The same commands used to instantiate a virtual topology on your laptop can be embedded into a workflow within one of the build systems we’ve discussed. With this, you can run a series of automated tests against that topology, in conjunction with your Ansible playbook or Python script. If everything works out, the build passes, and your change is permitted to continue in the pipeline.

Having a reliable, accurate test environment isn’t something you should overlook in your pipeline. Piecemeal testing of individual configs or state tables can get you only so far. Networks are complicated distributed systems, and some failure scenarios can happen only in such a system. Replicating this environment virtually may be your only safety net against causing production outages, and putting it in the pipeline means every change is vetted equally.

## Deployment Tools and Strategies

Earlier in the chapter, we discussed the importance of understanding *what* you’re deploying in a CI/CD pipeline. This knowledge has a big impact on the tools you use to actually deploy the changes you make.

For instance, if you’re writing Python code to automate tasks around your network, you should consider treating it like a full-fledged software project. Regardless of the size, production code is production code. Even a bug in a small script can cripple your infrastructure, so you apply the same rigorous process to it as any large-scale web project.

In addition to the important testing and peer review discussed earlier, you may find it useful to explore the delivery mechanisms that software developers are starting to use. You may be able to learn from (and even copy) the cloud deployment processes and tools that other teams in your organization use to deploy their changes.

It’s also becoming increasingly popular to deploy software in Docker containers. You could instruct your CI pipeline to automatically build a Docker image after a new change is reviewed and merged. This image can be deployed to a Docker Swarm or Kubernetes cluster in production.

On the other hand, sometimes we’re not deploying custom software; sometimes our Git repositories are used simply to store configuration artifacts like YAML or Jinja templates. This is common for network automation efforts that use configuration management tools like Ansible to push network device configurations onto the infrastructure. However, while the method of deployment may differ between network engineers and software developers, CI plays a vital role ([Figure 13-16](#cicd-pipeline-comparison)).

![npa2 1316](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1316.png)

###### Figure 13-16. A comparison of development and networking CI pipelines

In this case, it’s important to understand how these configurations are going to be used in production, as well as how rollbacks will be handled. This is important for deciding not only how Ansible will run in production but also how the configuration templates themselves are constructed. For instance, you might consider running an Ansible playbook to deploy configuration templates onto a set of network devices every time a new change is merged to the main branch—but what impact will that have on the configuration? Will the configuration always be overwritten? If so, will that overwrite a crucial part of the configuration that you didn’t intend?

Some vendors provide options to help solve this problem; for example, when pushing an XML-based configuration to a Junos device, you can use the `operation` flag with a value of `replace` to specify that you want to replace an entire section of configuration. The following example shows a Jinja template for a Junos configuration that uses this option:

```
<configuration>
  <protocols>
      <bgp operation="replace">
          {% for groupname, grouplist in bgp.groups.iteritems() %}
          <group>
              <name>{{ groupname }}</name>
              <type>external</type>
              {% for neighbor in grouplist %}
              <neighbor>
                  <name>{{ neighbor.addr }}</name>
                  <peer-as>{{ neighbor.as }}</peer-as>
              </neighbor>
              {% endfor %}
          </group>
          {% endfor %}
      </bgp>
  </protocols>
</configuration>
```

Unfortunately, not all vendors allow for this, but in this particular case, you could simply overwrite entire sections of configuration for each new patch in the CI pipeline to ensure that *what it should be* (WISB) always equals *what it really is* (WIRI).

This is another area with no silver bullet. The answer to the deployment question depends largely on what you are deploying and how often. It’s best to first settle on a strategy for network automation; decide if you want to invest in some developers and write more formalized software, or if you want to leverage existing open source or commercial tools to deploy simple scripts and templates. This will guide you toward the appropriate deployment model.

However, deployment should *never* take place until the aforementioned concepts like peer review and automated testing have taken place. A network automation effort that does not prioritize quality and stability above all is doomed to failure.

Thinking a bit more broadly, how might we approach deploying a change to our entire network from a CI/CD context—not just to a single device at a time? A few deployment strategies have become popular for deploying applications, particularly in the cloud era, and it’s important to consider what we can learn from them:

Deploy in placeJust make the change blindly to all infrastructure nodes at once.

RollingSlowly roll a change to one infrastructure element at a time, until complete.

CanaryRoll a change out to a relatively small percentage of production infrastructure, pausing to evaluate success/failure.

Blue/greenCreate a new environment to contain the change—in parallel to the old—and migrate traffic from old to new using routing or load balancing.

While these work well for the application domain, especially in environments where the application infrastructure is relatively homogenous, it may not be obvious how these map to the network domain. After all, networks are a series of interconnected and interrelated infrastructure elements; often it’s not possible to simply make a change on one network device at a time.

However, there are still lessons we can learn. Here’s some food for thought:

- Blue/green deployments may not seem possible at first; we can’t necessarily spin up a parallel network for every change we want to make. But often we can create parallel virtual resources like VRFs or routing adjacencies. Although this causes a bit more complication in the moment (making a change in place rather than duplicating configuration is always going to be “easier”), it not only can make the change itself easier, but also has a much simpler rollback model.
- Canary deployments work best when production infrastructure is well modularized and homogenous. You have to be able to make a change in a way that’s well contained (perhaps a single data-center row) but that is also a valid production environment (deploying to a network that’s used only for testing is not a valid canary deployment). This is why simple, repeatable network design is so critical for network automation success.

# Summary

Your organization, especially if it’s a large enterprise, might have some kind of in-house software development shop, or at least interact with third-party contractors for projects that require some custom software to be built. Reach out to those teams and ask about their processes. If they’re using CI, there’s a chance they’d be willing to let you use some of their existing tooling to accomplish similar goals with network automation.

In this chapter, we talked about a lot of process improvements (as well as tooling to help enforce these processes), but the real linchpin to all of this is a culture that understands the costs and benefits of this approach. If you don’t have buy-in from the business to make these improvements, they will not last.

It’s also important to remember that a big part of CI/CD is continuously learning. Continuously challenge the status quo, and ask yourself if the current model of managing and monitoring your network is *really* sufficient. Application requirements change often, so the answer to this question is often “no.” Try to stay plugged in to the application and software development communities so you can get ahead of these requirements and build a pipeline that can respond to these changes quickly.
