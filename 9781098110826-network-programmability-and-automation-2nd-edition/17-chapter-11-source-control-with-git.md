# Chapter 11. Source Control with Git

So far in this book, we’ve shown you lots of ways to add automation to your toolbox, whether via scripting languages like Python (see [Chapter 6](ch06.html#python)) or via templating languages like Jinja (see [Chapter 9](ch09.html#templating)). The increased use of Python-based scripts or Jinja templates means that managing these artifacts is important (and by *artifacts* we mean the files that make up these scripts, templates, and other automation tools you’re employing). In particular, managing the *changes* to these artifacts has significant value (we’ll explain why shortly).

In this chapter, we’re going to show you how to use a *source control* tool—that is, a tool designed to manage the artifacts you’re creating and using in your network automation processes. The use of a source control tool lets you avoid messy and error-prone approaches like appending date- and timestamps to the end of filenames, and keeps you from running into accidentally deleted or overwritten files.

To start, let’s take a closer look at the idea of source control. We’ll keep the discussion fairly generic for now and delve into a specific source control tool known as Git later in the chapter. The generic qualities discussed in the next section are not specific to any particular source control tool.

# Use Cases for Source Control

Simply put, *source control* is a way of tracking files and the changes made to those files over time (source control is also known as *version control* or *revision control*). We know that’s a really generic description, so let’s look at some specific use cases:

- If you’re a developer writing code as part of a larger software development project, you could track the code you’re writing by using source control tools. This is probably the most well-known use case, and the one most people immediately think about when we mention source control.
- Let’s say you’re part of a team of administrators managing network devices. You could take the device configuration files and track them by using source control tools.
- Suppose you’re responsible for maintaining documentation for portions of your organization’s IT infrastructure. You could use source control tools to track the documentation.

In each of these cases, source control is tracking files (network configurations, documentation, software source code). By *tracking* these files, we mean that the source control tool is keeping a record of the files, the changes made to the files over time, and who made each set of changes. If a change to one of the files being tracked breaks something, you can revert, or roll back, to a previous version of the file, undoing the changes and getting back to a known good state. In some cases (depending on the tool being used), source control tools might enable you to more easily collaborate with coworkers in a distributed fashion.

# Benefits of Source Control

The previous section indirectly outlined some of the benefits of using a source control tool, but let’s pull out a few specific benefits that come from the use of source control.

## Change Tracking

First, you’re able to track the changes to the files stored in the source control tool over time. You can see the state of the files at any given point, and therefore you’re able to relatively easily see exactly *what* changed. This is an often overlooked benefit. When you’re working with lengthy network configuration files, wouldn’t it be helpful to be able to see *exactly* what changed from one version to the next?

Further, most source control tools also have the ability to add metadata about the change, such as why a change was made or a reference back to an issue or trouble ticket. This additional metadata can also prove quite useful in troubleshooting.

## Accountability

Not only do source control tools track changes over time, but they also track *who* made the changes. Every change is logged with who made that particular change. In a team environment, where multiple team members might be working together to manage network configurations or server configuration files, this is extraordinarily useful. Never again will you have to ask, “Who made this change?” The source control tool will already have that information.

## Process and Workflow

Using source control tools also helps you and your organization enforce a healthy process and workflow. We’ll get into this more in [Chapter 13](ch13.html#cicd), but for now think about the requirement that all changes must be logged in source control *before* being pushed to production. This gives you a linear history of changes, along with a log of the individual responsible for each set of changes, and enables you to enforce things like review (having someone else review your changes before they get put into production) or testing (having automated tests performed against the files in the source control system).

# Benefits of Source Control for Networking

Although source control is most typically associated with software development, it has clear benefits for networking professionals. Here are just a few examples:

- Python scripts (such as the ones you will be able to write after reading this book!) that interact with network devices can be placed in source control, so that versions of the script can be more easily managed.
- Network device configurations can be placed in source control, enabling you to see the state of a network device configuration at any point in time. A really well-known tool called RANCID uses this approach for storing network device configuration backups.
- It’s easy to highlight the changes between versions of network device configurations, allowing you and your team to easily verify that only the desired changes are in place (e.g., that you didn’t accidentally prune a VLAN from the wrong 802.1Q trunk).
- Configuration templates can be placed in source control, ensuring that you and your team can track changes to these templates *before* they are used to generate network device configurations or reports.
- You can use source control with network documentation.
- All changes to any of these types of files are captured along with the person responsible for the changes—no more “playing the blame game.”

Now that you have an idea of the benefits that source control can bring to you, your organization, and your workflow, let’s take a look at a specific source control tool that is widely used: [Git](https://git-scm.com).

# Enter Git

*Git*, the latest in a long series of source control tools, has emerged as the de facto source control tool for most open source projects. (It doesn’t hurt that Git manages the source code for the Linux kernel.) For that reason, we’ll focus our discussion of source control tools on Git, but keep in mind that other tools do exist. They are, unfortunately, beyond the scope of this book.

Let’s start with a brief history of how and why Git appeared.

## Brief History of Git

As we’ve mentioned, Git is the source control tool used to manage the source code for the Linux kernel. Git was launched by Linus Torvalds, the creator of the Linux kernel, in early April 2005 in response to a disagreement between the Linux kernel developer community and the proprietary system they were using at the time (a system called BitKeeper).

Torvalds had a few key design goals when he set out to create Git:

SpeedTorvalds needed Git to be able to rapidly apply patches to the Linux source code.

SimplicityThe design for Git needed to be as simple as possible.

Strong support for nonlinear developmentThe Linux kernel developers needed a system that could handle lots of parallel branches. Thus, this new system (Git) needed to support rapid branching and merging, and branches needed to be as lightweight as possible.

Support for fully distributed operationEvery developer needed a full copy of the entire source code and its history.

ScalabilityGit needed to be scalable enough to handle large projects, like the Linux kernel.

Development of Git was fast. Within a few days of its launch, Git was self-hosted (meaning that the source code for Git was being managed by Git). The first merge of multiple branches occurred just a couple of weeks later. At the end of April—just a few weeks after its launch—Git was benchmarked at applying patches to the Linux kernel tree at 6.7 patches per second. In June 2005, Git managed the 2.6.12 release of the Linux kernel, and the 1.0 release of Git occurred in late December 2005.

As of this writing, the most recent release of Git is version 2.41.0, and versions of Git are available for all major desktop operating systems (Linux, Windows, and macOS). Notable open source projects using Git include the Linux kernel (as we’ve already mentioned), Perl, the GNOME desktop environment, Android, KDE, and the X.Org implementation of the X Window System. Additionally, some very popular online source control services are based on Git, including [GitHub](https://github.com), [Bitbucket](https://bitbucket.org), and [GitLab](https://about.gitlab.com). Some of these services also offer on-premises implementations. You’ll get the opportunity to look more closely at GitLab in [Chapter 13](ch13.html#cicd), when we discuss continuous integration.

## Git Terminology

Before we progress any further, let’s be sure that we’ve properly defined the terminology. Some of these terms we may have used before, but we include them here for the sake of completeness:

RepositoryIn Git, a repository is a database that contains all of a project’s information (files and metadata) and history. (We’re using the term *project* here to refer to an arbitrary grouping of files for a particular purpose or effort.) A repository is a complete copy of all the files and information associated with a project throughout its lifetime. After data is added to a repository, it is immutable; that is, it can’t be changed once added. This *isn’t* to say that you can’t make changes to files stored in a repository, just that the repository stores and tracks these files in such a way that changes to a file create a new entry in the repository (specifically, Git uses SHA-1 hashes to create content-addressable objects in the repository).

Working directoryThis is the directory where you, as the user of Git, will modify the files contained in the repository. The working directory is *not* the same as the repository. Note that the term *working directory* is also used for other purposes on Linux/Unix/macOS systems (to refer to the current directory, as output by the `pwd` command). Git’s working directory is *not* the same as the current directory, and specifically refers to the directory where the *.git* repository is stored.

IndexThe index describes the repository’s directory structure and content at a point in time. The index is a dynamic binary file maintained by Git and modified as you stage changes and commit them to the repository.

CommitA commit is an entry in the Git repository, recording metadata for each change introduced to the repository. This metadata includes the author, the date of the commit, and a commit message (a description of the change introduced to the repository). Additionally, a commit captures the state of the entire repository at the time the commit was performed. Keep in mind that when we say “a change to the repository,” this might mean multiple changes to multiple files; Git allows you to lump changes to multiple files together as a single commit. (We discuss this in a bit more detail later in this chapter.)

## Overview of Git’s Architecture

With the terminology from the previous section in mind, we can now provide an overview of Git’s architecture. We’ll limit our discussion of Git’s architecture to keep it relatively high-level but detailed enough to help with your understanding of how Git operates.

###### Note

For a more in-depth discussion of Git’s architecture, we recommend [*Version Control with Git*, 3rd Edition](https://shop.oreilly.com/product/0636920022862.do), by Prem Kumar Ponuthorai and Jon Loeliger (O’Reilly).

As we described earlier, a Git *repository* is a database that contains all the information about a project: the files contained in the project, the changes made to the project over time, and the metadata about those changes (who made the change, when the change was made, etc.). By default, this information is stored in a directory named *.git* in the root of your working directory (this behavior can be changed). For example, here’s a file listing of a newly initialized Git repository’s working directory, showing the *.git* directory where the actual repository data is found:

```
macbookpro:npab-examples slowe (main)$ ls -la
total 0
drwxr-xr-x   3 slowe  staff  102 May 11 15:37 .
drwxr-xr-x  16 slowe  staff  544 May 11 15:37 ..
drwxr-xr-x  10 slowe  staff  340 May 11 15:37 .git
macbookpro:npab-examples slowe (main)$
```

###### Note

Although the preceding directory listing came from a MacBook Pro laptop, throughout this chapter we’ll primarily be using three different Linux distributions to show the output of various `git` commands and subcommands: Debian 11, Ubuntu 20.04, and Amazon Linux 2. We’ve customized the prompts shown here to clearly show the name of each distribution in the prompt; your prompt will quite likely look different.

As you can tell from this prompt, this directory listing is from the directory *npab-examples*. In this example, the *working directory* is the *npab-examples* directory, and the Git *repository* is in *npab-examples/.git*. This is why we said earlier that the working directory and the repository aren’t the same. It’s common for new users to refer to the working directory as the repository, but keep in mind that the actual repository is in the *.git* subdirectory.

Within the *.git* directory you’ll find all the various components that make up a Git repository:

- The index—which we defined earlier as representing the repository’s directory structure and content at a given point in time—is found at *.git/index*.
- The files contained within a Git repository are treated as content-addressable objects and stored in subdirectories in *.git/objects*.
- Any repository-specific configuration details are found in *.git/config*.
- Metadata about the repository, the changes stored in the repository, and the objects in the repository can be found in *.git/logs*.

All the information stored in the *.git* directory is maintained by Git—you should never need to directly interact with the contents of this directory. Over the course of this chapter, we’ll share with you the various commands for interacting with the repository to add files, commit changes, revert changes, and more. In fact, that leads us directly into our next section, which will show you how to work with Git.

# Working with Git

Now that you have an idea of what Git’s architecture looks like, let’s shift our focus to something a bit more practical: actually *working* with Git.

Throughout this discussion, we’re going to use a (hopefully) practical example. Let’s assume that you are a network engineer responsible for rolling out some network automation tools in your environment. During this process, you’re going to end up creating Python scripts, Jinja templates, and other files. You’d like to use Git to manage these files so that you can take advantage of all the benefits of source control.

The following sections walk you through each of the major steps in getting started using Git to manage the files created as part of your network automation effort.

## Installing Git

The steps for installing Git are extremely well documented, so we won’t go through them here. Git is often preinstalled in various distributions of Linux; if not, Git is almost always available to install via the Linux distribution’s package manager (such as `dnf` for RHEL/CentOS/Fedora or `apt` for Debian/Ubuntu). Installers are available for macOS and Windows that make it easy to install Git. Detailed instructions and options for installing Git are also available on [the Git website](https://oreil.ly/1IxBe).

## Creating a Repository

Once Git is installed, the first step is to create a directory where the repository will be stored. Assuming you’re using a Debian GNU/Linux system, the command might look something like this (and would be similar, if not identical, on other Linux distributions or on macOS):

```
admin@debian11:~$ mkdir ~/net-auto
```

Then you can change into this directory and create the empty repository by using the `git init` command:

```
admin@debian11:~$ cd net-auto
admin@debian11:~/net-auto$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Initialized empty Git repository in /home/admin/net-auto/.git
```

The `git init` command is responsible for *initializing*, or creating, a new Git repository. This involves creating the *.git* directory and all the subdirectories and contents found within them as well as setting up the initial branch (you’ll learn more on branches in [“Branching in Git”](#branching_in_git)).

The preceding message regarding the name of the initial branch was added in Git 2.28, released on July 27, 2020. Linux distributions and operating systems released after this time will most likely ship with or make available a version of Git that is at least 2.28 or higher. The preceding output was taken from a Debian 11 system, which provides Git 2.30.2. Ubuntu 20.04.3, which ships with Git 2.25.1, does not display the same output.

###### Note

The `git` commands described throughout this chapter should be nearly identical across all systems on which Git runs. We’ll use various Linux distributions (as reflected in the shell prompts in the examples), but using Git on macOS should be the same as on Linux. Using Git on Windows should be similar, but syntactical differences may exist here and there because of the differences in the underlying operating systems.

If you were now to run `ls -la` in the *net-auto* directory, you’d see the *.git* directory that stores the empty Git repository created by the `git init` command. The repository is now ready for you to start adding content. You add content to a repository by adding files.

## Adding Files to a Repository

Adding files to a repository is a multistage process:

1. Add the files to the repository’s working directory.
2. Stage the files to the repository’s index.
3. Commit the staged files to the repository.

Let’s go back to our example. You’ve created your new Git repository to store files created as part of your network automation project, and some of the first files you’d like to add to the repository are the current configuration files from your network devices. You already have three configuration files: *sw1.txt*, *sw2.txt*, and *sw3.txt*, that contain the current configurations for three switches.

First, copy the files into the working directory (in our example, */home/admin/net-auto*). More generically, remember that the working directory is the parent directory of the *.git* directory (which holds the actual Git repository). On a Linux or macOS system, copying files into the working directory would involve the `cp` command; on a Windows-based machine, you’d use the `copy` command.

The files are now in the working directory but are *not* in the repository itself. This means that Git is not tracking the files or their content, and therefore you can’t track changes, know who made the changes, or roll back to an earlier version.

You can verify this by running the `git status` command, which in this example produces output that looks like this:

```
admin@debian11:~/net-auto$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    sw1.txt
    sw2.txt
    sw3.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The output of the `git status` command tells you that untracked files are present in the working directory and that nothing has been added to the repository. As the output indicates, you need to use the `git add` command to add these untracked files to the repository, like this:

```
admin@debian11:~/net-auto$ git add sw1.txt
admin@debian11:~/net-auto$ git add sw2.txt
admin@debian11:~/net-auto$ git add sw3.txt
```

You could also use shell globbing to add multiple files at the same time. For example, you could use `git add sw*.txt` to add all three switch configurations with a single command. On systems running bash, you could also use brace expansion, as in `git add sw{1,2,3}.txt`, to stage multiple files.

After you’ve used `git add` to add the files to the staging area, you can run `git status` again to see the current status:

```
admin@debian11:~/net-auto$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   sw1.txt
    new file:   sw2.txt
    new file:   sw3.txt
```

At this point, the files have been *staged* into Git’s index; Git’s index and the working directory are in sync. Technically speaking, the files have been added as objects to Git’s object store as well, but there is no point-in-time reference to these objects. To create that point-in-time reference, you must first *commit* the staged changes.

## Committing Changes to a Repository

Before you’re ready to commit changes to a repository, you need to be sure that you’ve done a couple of things. Recall that one of the benefits of using Git as a source control tool is that you’re able to not only track the changes made to the files stored in the repository, but also know who made each set of changes. To obtain that information, you first need to provide it to Git. (You could also do this right after installing Git; it’s not necessary to create a repository first.) This configuration is also important when it comes to collaborating with others using Git, as you’ll see in [“Collaborating with Git”](#collaborating_with_git).

### Providing user information to Git

Git has a series of configuration options; some are repository-specific, some are user-specific, and some are system-wide. Recall from earlier that Git stores repository-specific configuration information in *.git/config*. In this particular case—​where we need to provide the user’s name and email address so Git can track who made each set of changes—​it’s the user-specific configuration we need to modify, not the repository-specific configuration.

So where are these values stored? These settings are found in the *.gitconfig* file in your home directory. This file is an INI-style file, and you can edit it by using either your favorite text editor or the `git config` command. In this case, we’ll show you how to use `git config` to set this information.

To set your name and email address, use the following commands:

```
ubuntu@ubuntu2004:~/net-auto$ git config --global user.name "John Smith"
ubuntu@ubuntu2004:~/net-auto$ git config --global user.email
"john.smith@networktocode.com"
```

You use the `--global` option here to set it as a user-specific value; if you want to set a different username and/or email address as a repository-specific value, just omit the `--global` flag (but be sure you’re in the working directory of an active repository first; Git will report an error otherwise). With the `--global` flag, `git config` modifies the *.gitconfig* file in your home directory; without it, `git config` modifies the *.git/config* file of the current repository.

### Committing changes

When Git has been configured with your identity, you’re ready to *commit* the changes you’ve made to the files into the repository. Remember that before you can commit changes into the repository, you must first *stage* the files by using the `git add` command; this is true both for newly created files as well as modified files that were already in the repository (we’ll review that scenario shortly). Since you’ve already staged the changes (via the `git add` command earlier) and verified that (via the `git status` command, which shows the files are staged), then you’re ready to commit.

Committing changes to a repository is as simple as using the `git commit` command:

```
ubuntu@ubuntu2004:~/net-auto$ git commit -m "First commit to new repository"
[main (root-commit) 9547063] First commit to new repository
 3 files changed, 24 insertions(+)
 create mode 100644 sw1.txt
 create mode 100644 sw2.txt
 create mode 100644 sw3.txt
```

###### Note

If you omit the `-m` parameter to `git commit`, Git will launch the default text editor so you can provide a commit message. The text editor that Git launches is configurable (via `git config` or editing *.gitconfig* in your home directory). You could, for example, configure Git to use [Visual Studio Code](https://code.visualstudio.com), [Sublime Text](https://www.sublimetext.com), or another graphical text editor.

So what’s happening when you commit the changes to the repository? When you add the files via `git add`, objects representing the files (and the files’ content) are added to Git’s object database. Specifically, Git creates *blobs* (binary large objects) to represent the files’ content, and *tree objects* to represent the files and their directory structure. When you commit the changes via `git commit`, you’re adding another type of object to the Git database (a *commit object*) that references the tree objects, which in turn reference the blobs. With a commit object, you now have a point-in-time reference to the entire state of the repository.

At this point, your repository has a single commit, and you can see that commit by using the `git log` command:

```
[ec2-user@amazonlinux2 net-auto]$ git log
commit 8d18465d697de11ebe34494f33d0cad42e01e076 (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:24:24 2022 +0000

    First commit to new repository
[ec2-user@amazonlinux2 net-auto]$
```

The `git log` command shows the various commits—or checkpoints, if you will—you created over the lifetime of the repository. Every time you commit changes, you create a commit object, and that commit object references the state of the repository at the time it was created. This means you can view the state of the repository and its contents only at the time of a commit. Commits, therefore, become the checkpoints by which you can move backward (or forward) through the history of the repository.

### Recommendations for committing changes

Understanding how commits work leads to a few recommendations around committing your changes to a repository:

Commit frequentlyYou can view the state of the repository only at the time when changes are committed (via a commit object). If you make changes, save the files, make more changes, and then save and commit, you won’t be able to view the state of the repository at the first set of changes (because you didn’t commit).

Commit at logical pointsDon’t commit every time you save changes to a file in the repository. We know this sounds like a contradiction to the previous bullet, but it makes sense to commit changes only when they are complete. For example, committing changes when you’re only halfway through updating a switch’s configuration doesn’t make sense; you wouldn’t want to roll back to a half-completed switch configuration. Instead, commit when you’ve finished the switch configuration.

Use helpful commit messagesAs you can see from the previous `git log` output, commit messages help you understand the changes contained in that commit. Try to make your commit messages helpful and straightforward—in six months, the commit message will likely be the only clue to help you decipher what you were doing at that time.

Before we move on to the next section, we need to discuss one more topic. We’ve explained that objects in a Git repository are immutable, and that changes to an object (like a file) result in the creation of a new object (addressed by the SHA-1 hash of the object’s content). This is true for all objects in the Git repository, including blobs (file content), tree objects, and commit objects.

What if, though, you make a commit and realize the commit contains errors? Maybe you have some typos in your network configuration, or the commit message is wrong. In this case, Git allows you to modify (or *amend*) the last commit.

### Amending commits

If the last commit is incorrect for some reason, it is possible to *amend* the commit via the `--amend` flag to `git commit`. Note that you could just make another commit instead of amending the previous commit; both approaches are valid, and each approach has its advantages and disadvantages, which we’ll discuss shortly. First, though, let’s show you how to amend a commit.

To amend a commit, you follow the same set of steps as with a “normal” commit:

1. Make whatever changes you need to make.
2. Stage the changes.
3. Run `git commit --amend` to commit the changes, marking it as an amendment.

Under the hood, Git is actually creating new objects—which is in line with Git’s philosophy and approach of content-addressable immutable objects—but in the history of the repository, you’ll see *only* the amended commit, not the original commit. This results in a “cleaner” history, although some purists may argue that simply making another commit (instead of using `--amend`) is a better approach.

Which approach is best? That is mostly decided by you, the user, but there are a couple of considerations. If you’re collaborating with others via Git and a shared repository, using `--amend` to amend commits already sent to the shared repository is generally a bad idea. The one exception is in an environment using Gerrit, where amended commits are used extensively. We talk more about Gerrit in [Chapter 13](ch13.html#cicd), and we cover collaborating with Git in [“Collaborating with Git”](#collaborating_with_git).

## Changing and Committing Tracked Files

You’ve created a repository, added new files, and committed changes to the repository. Now, though, you need to make some changes to the files that are already in the repository. How does that work?

Fortunately, the process for committing modified versions of files into a repository looks pretty much identical to what we’ve shown you already:

1. Modify the file(s) in the working directory.
2. Stage the change(s) to the index by using `git add`. This puts the index in sync with the working directory.
3. Commit the changes by using `git commit`. This puts the repository in sync with the index, and creates a point-in-time reference to the state of the repository.

Let’s review this in a bit more detail. Suppose you need to modify one of the files, *sw1.txt*, because the switch’s configuration has changed (or perhaps because you’re enforcing that configurations can be deployed only *after* they’ve been checked into source control). After a tracked file (a file about which Git already knows and is tracking) is modified, `git status` will show that changes are present:

```
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

    modified:   sw1.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Note the difference between this status message and the status message we showed you earlier. In this case, Git knows about the *sw1.txt* file (it’s already been added to the repository), so the status message is different. The status message changes if you add another switch configuration file, *sw4.txt*, to the working directory:

```
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

    modified:   sw1.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    sw4.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Again, Git provides a clear distinction between tracking changes to an already known file and detecting untracked (not previously added) files to the working directory. Either way, though, the process for getting these changes (modified file and new file) into the repository is exactly the same, as you can see in the output of the `git status` command: just use the `git add` command and then the `git commit` command:

```
admin@debian11:~/net-auto$ git add sw1.txt
admin@debian11:~/net-auto$ git add sw4.txt
admin@debian11:~/net-auto$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

    modified:   sw1.txt
    new file:   sw4.txt

admin@debian11:~/net-auto$ git commit -m "Update sw1, add sw4"
[main 679c41c] Update sw1, add sw4
 2 files changed, 9 insertions(+)
 create mode 100644 sw4.txt
```

In the output of the `git status` commands, you may have noticed a reference to `git commit -a`. The `-a` option simply tells Git to add all changes from all known files. If you’re only committing changes to known files *and* you are OK with committing all the changes together in a single commit, then using `git commit -a` allows you to avoid using the `git add` command first.

If, however, you want to break up changes to multiple files into separate commits, you need to use `git add` followed by `git commit` instead. Why might you want to do this?

- You might want to limit the scope of changes in a single commit so that it’s less impactful to revert to an earlier version.
- You may want to limit the scope of changes in a single commit so that others can review your changes more easily. (We’ll discuss this in more detail in [Chapter 13](ch13.html#cicd).)
- When collaborating with others, it’s often considered a best practice to limit commits to a single logical change, which means you may include some changes in a commit but not others. We discuss general guidelines for collaborating with Git in [“Collaborating with Git”](#collaborating_with_git).

You’ll also notice that we’ve been using `git commit -m` in our examples. The `-m` option allows the user to include a commit message on the command line. If you don’t include the `-m`, Git will open your default editor so that you can supply a commit message. Commit messages are required, and as we mentioned earlier, we recommend that you make your commit messages as informative as possible. (You’ll be thankful for informative commit messages when reviewing the output of `git log` in the future.) You can also combine both the `-a` and `-m` options, as in `git commit -am "Committing all changes to tracked files"`.

###### Tip

For more information on the various options to any of the `git` commands, just type **`git help command`**, like `git help commit` or `git help add`. This opens the man page for that part of Git’s documentation. If you like to use the `man` command instead, you can do that; just put a dash into the `git` command. Thus, to see the man page for `git commit`, you’d enter **`man git-commit`**.

Now that you’ve committed another set of changes to the repository, let’s look at the output of `git log`:

```
[ec2-user@amazonlinux2 net-auto]$ git log
commit f3a00e6596878faffbfb169063cafba67833323c (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:34:26 2022 +0000

    Update sw1, add sw4

commit 8d18465d697de11ebe34494f33d0cad42e01e076
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:24:24 2022 +0000

    First commit to new repository
[ec2-user@amazonlinux2 net-auto]$
```

Your repository now has two commits. Before we explore how to view a repository at a particular point in time (at a particular commit), let’s first review a few other commands and make some additional commits to the repository.

## Unstaging Files

If you’ve been following along, your repository now has four switch configuration files (*sw1.txt* through *sw4.txt*) and two commits. Let’s say you need to add a fifth switch configuration file (named *sw5.txt*, of course). You already know the process:

1. Copy the file *sw5.txt* into the working directory.
2. Use `git add` to stage the file from the working directory into the index.

At this point, running `git status` will report that *sw5.txt* has been staged and is ready to commit to the repository:

```
[ec2-user@amazonlinux2 net-auto]$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

    new file:   sw5.txt

[ec2-user@amazonlinux2 net-auto]$
```

However, you realize after staging the file that you aren’t ready to commit it in its current state. Maybe the file isn’t complete, or perhaps it doesn’t accurately reflect the actual configuration of `sw5` on the network. In such a situation, the best approach is to *unstage* the file.

The command to unstage the file—that is, to remove it from the index so the working directory and the index are no longer synchronized—has already been given to you by Git. If you refer to the output of `git status` shared just a couple paragraphs ago, you’ll see Git telling you how to unstage the file. The command looks like this:

```
git restore --staged file
```

In earlier versions of Git, the command was `git reset HEAD file`. Newer versions of Git added the `git restore` command you see here. The older version actually gives a clue as to what’s happening when you run this command, but to explain what’s happening, we first need to explain what *HEAD* is.

HEAD is a pointer referencing the last commit you made (or the last commit you checked out into the working directory, but we haven’t gotten to that point yet). Recall that when you stage a file (using `git add`), you are taking content from the working directory into the index. When you commit (using `git commit`), you are creating a point-in-time reference—a commit—to the content. Every time you commit, Git updates HEAD to point to the latest commit.

###### Note

HEAD also plays a strong role when you start working with multiple Git branches. You’ll learn more when we discuss branches in [“Branching in Git”](#branching_in_git).

Here’s a quick way to help illustrate updating HEAD. If you’ve been following along with this chapter’s examples, you can use these commands as well (just keep in mind that the SHA-1 checksums shown here will differ from your own SHA-1 checksums).

First, use `cat` to show the contents of *.git/HEAD*:

```
[ec2-user@amazonlinux2 net-auto]$ cat .git/HEAD
ref: refs/heads/main
[ec2-user@amazonlinux2 net-auto]$
```

You’ll see that HEAD is a pointer to the file *refs/heads/main*. If you `cat` that file, you’ll see this:

```
[ec2-user@amazonlinux2 net-auto]$ cat .git/refs/heads/main
f3a00e6596878faffbfb169063cafba67833323c
[ec2-user@amazonlinux2 net-auto]$
```

The content of *.git/refs/heads/main* is a SHA-1 checksum. Now run `git log`, and compare the SHA-1 checksum of the latest commit against that value:

```
[ec2-user@amazonlinux2 net-auto]$ git log
commit f3a00e6596878faffbfb169063cafba67833323c (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:34:26 2022 +0000

    Update sw1, add sw4

commit 8d18465d697de11ebe34494f33d0cad42e01e076
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:24:24 2022 +0000

    First commit to new repository
[ec2-user@amazonlinux2 net-auto]$
```

You’ll note that the SHA-1 checksum of the last commit matches the value of HEAD (which points to *refs/heads/main*), illustrating that HEAD is a pointer to the latest commit. Later in this chapter, we’ll show how HEAD also incorporates branches and how it changes when you check out content to your working directory.

For now, though, let’s get back to `git reset` as way of unstaging a file. This command is powerful, but fortunately it has some sane defaults. When used in this way—that is, without any flags and when given a filename or path—the only thing `git reset` will do is make the index look like the content referenced by HEAD (which you now know references a particular commit—by default, the latest commit).

Recall that `git add` makes the index look like the working directory, which is how you stage a file. The `git reset HEAD file` command is the exact opposite, making the index look like the content referenced by HEAD. It *undoes* changes to the index made by `git add`, thus *unstaging* files.

The `git restore` command works in the same fashion: it restores the specified paths with the content from a restore source. When used with the `--staged` parameter, it will (by default) restore from HEAD, just exactly as `git reset HEAD file` does. You can find out more about the `git restore` command by running `man git-restore`.

Let’s see this command in action. You’ve already staged *sw5.txt* in preparation for committing it to the repository, so `git status` shows the file listed in the `Changes to be committed:` section. Now run `git restore`:

```
[ec2-user@amazonlinux2 net-auto]$ git restore --staged sw5.txt
[ec2-user@amazonlinux2 net-auto]$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    sw5.txt

nothing added to commit but untracked files present (use "git add" to track)
[ec2-user@amazonlinux2 net-auto]$
```

You can see that *sw5.txt* is no longer listed as a change to be committed and is instead shown as an untracked file (it’s no longer in the index). Now you can continue working on the content of *sw5.txt* and committing a version of it to the repository when you’re ready.

We’ve shown you how to create a repository, add files (both new and existing), commit changes, and unstage files. What if you have files that need to be colocated with other files in the repository but shouldn’t be tracked by Git? This is where file exclusions come into play.

## Excluding Files from a Repository

Sometimes you might need to store files in the working directory—the “scratch space” for a Git repository—that you don’t want included in the repository. Fortunately, Git provides a way to exclude certain files or filename patterns from inclusion in the repository.

Going back to our example, you’ve created a repository in which to store network automation artifacts. Let’s suppose you have a Python script that connects to your network switches in order to gather information from them. An example of one such Python script—in this case, one written to connect to an Arista switch and gather information—might look like this:

```
#!/usr/bin/env python

from pyeapi.client import Node as EOS
from pyeapi import connect
import yaml

def main():

    creds = yaml.load(open('credentials.yml'))

    un = creds['username']
    pwd = creds['password']

    conn = connect(host='eos-npab', username=un, password=pwd)
    device = EOS(conn)

    output = device.enable('show version')
    result = output[0]['result']

    print('Arista Switch Summary:')
    print('---------------------')
    print('OS Version:' + result['version'])
    print('Model:' + result['modelName'])
    print('System MAC:' + result['systemMacAddress'])

if __name__ == "__main__":
    main()
```

Part of the way this script operates is via the use of authentication credentials stored in a separate file (in this case, a YAML file named *credentials.yml*). Now, you need these credentials to be stored with the Python script, but you don’t necessarily want the credentials to be tracked and managed by the repository.

###### Warning

Whether to include secrets—information like passwords, SSH keys, or the like—into a Git repository depends greatly on the way the repository is being used. For a strictly private repository where per-user secrets are not needed, including secrets in the repository is probably fine. For repositories where per-user secrets should be used or for repositories that may at some point be shared publicly, you’ll likely want to exclude secrets from the repository by using the mechanisms outlined in this section.

Fortunately, Git provides a couple of ways to exclude files from being tracked as part of a repository. In [“Committing Changes to a Repository”](#committing_changes_to_the_repository), we noted that Git configuration can be handled on a repository-specific, user-specific, or system-wide basis. Excluding files from Git repositories is similar in that there are ways to exclude files per repository or per user.

### Excluding files per repository

Let’s start with the per-repository method. The most common way of excluding (or ignoring) files is to use a *.gitignore* file stored in the repository itself. Like any other content in the repository, the *.gitignore* file must be staged into the index and committed to the repository anytime changes are made. The advantage of this approach is that the *.gitignore* file is then distributed as part of the repository, which is useful when you are part of a team whose members are all using Git as a distributed version control system (DVCS).

The content of the *.gitignore* file is simply a list of filenames or filename patterns, one on each line. To create your own list of files for Git to ignore, you simply create the file named *.gitignore* in the working directory, edit it to add the filenames or filename patterns you want ignored, and then add/commit it to the repository.

Looking at our Python script from earlier, you can see that it looks for its credentials in the file named *credentials.yml*. Let’s create *.gitignore* (if you don’t already have one) to ignore this file:

1. Create an empty file by using `touch .gitignore`.
2. Edit *.gitignore*, using the text editor of your choice, to add *credentials.yml* on a single line in the file.

At this point, if you run `git status`, you’ll see that Git has noticed the addition of the *.gitignore* file, but the *credentials.yml* file is *not* listed:

```
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

You can now stage and commit the *.gitignore* file into the repository by using `git add .` and `git commit -m "Adding .gitignore file"`.

Now, if you create the *credentials.yml* file for the Python script, Git will politely ignore the file. For example, here you can see the file exists in the working directory, but `git status` reports no changes or untracked files:

```
ubuntu@ubuntu2004:~/net-auto$ ls -la
total 40
drwxrwxr-x 3 ubuntu ubuntu 4096 May 31 16:32 .
drwxr-xr-x 5 ubuntu ubuntu 4096 May 12 17:18 ..
drwxrwxr-x 8 ubuntu ubuntu 4096 May 31 16:34 .git
-rw-rw-r-- 1 ubuntu ubuntu    8 May 31 16:27 .gitignore
-rw-rw-r-- 1 ubuntu ubuntu   15 May 31 16:32 credentials.yml
-rwxrwxr-x 1 ubuntu ubuntu    0 May 31 16:32 script.py
-rw-rw-r-- 1 ubuntu ubuntu   98 May 12 20:22 sw1.txt
-rw-rw-r-- 1 ubuntu ubuntu   84 May 12 17:17 sw2.txt
-rw-rw-r-- 1 ubuntu ubuntu   84 May 12 17:17 sw3.txt
-rw-rw-r-- 1 ubuntu ubuntu   84 May 12 20:33 sw4.txt
-rw-rw-r-- 1 ubuntu ubuntu  135 May 31 14:56 sw5.txt
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main
nothing to commit, working directory clean
```

If you’re really paying attention, you might note that the fact Git reports nothing to commit isn’t necessarily a guarantee that the file has been ignored. Let’s use a few more `git` commands to verify it. First, we’ll use `git log` to show the history of commits:

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
554b084 (HEAD -> main) Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
```

Next, let’s interrogate Git to see the contents of the repository at these various points in time. You’ll use the `git ls-tree` command along with the SHA-1 hash of the commit you want to inspect. You’ve probably noticed by now that Git often uses just the first seven characters of a SHA-1 hash, as in the preceding output of the `git log --oneline` command (Git will automatically use more characters to keep the hashes unique as needed). In almost every case (an exception may be out there somewhere!), that’s true for commands you enter that require a SHA-1 hash. For example, to see what was in the repository at the time of the next-to-last commit (whose SHA-1 hash starts with `ee7e7bf`), you could do this:

```
ubuntu@ubuntu2004:~/net-auto$ git ls-tree ee7e7bf
100755 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    script.py
100644 blob 2567e072ca607963292d73e3acd49a5388305c53    sw1.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw2.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw3.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw4.txt
100644 blob 88b23c7f60dc91f7d5bfeb094df9ed28996daeeb    sw5.txt
```

You can see that *credentials.yml* does not exist in the repository as of this commit. What about the latest commit?

```
ubuntu@ubuntu2004:~/net-auto$ git ls-tree 554b084
100644 blob 2c1817fdecc27ccb3f7bce3f6bbad1896c9737fc    .gitignore
100755 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391    script.py
100644 blob 2567e072ca607963292d73e3acd49a5388305c53    sw1.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw2.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw3.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw4.txt
100644 blob 88b23c7f60dc91f7d5bfeb094df9ed28996daeeb    sw5.txt
```

(We’ll leave it as an exercise for you to review the rest of the commits in order to verify that the *credentials.yml* file is *not* present in any commit.)

### Excluding files globally

In addition to excluding files per repository by using a *.gitignore* file in the repository’s working directory, you can also create a global file for excluding files for all repositories on your computer. Just create a *.gitignore_global* file in your home directory and add exclusions to that file. You may also want to run this command to ensure that Git is configured to use this new *.gitignore_global* file in your home directory:

```
git config --global core.excludesfile /path/to/.gitignore_global
```

If you placed *.gitignore_global* in your home directory, the path to the file would typically be noted as *~/.gitignore_global*.

The use of `git log` and `git ls-tree` naturally leads us into a discussion of how to view more information about a repository, its history, and its content.

## Viewing More Information About a Repository

When it comes to viewing more information about a repository, we’ve already shown you one command that you’ll use quite a bit: `git log`. The `git log` command has already been used on numerous occasions, which should give you some indicator of just how useful it is.

### Viewing basic log information

The most basic form of `git log` shows the history of commits up to HEAD, so just running `git log` shows you all the commits over the history of the repository. Here’s the output of `git log` for this chapter’s example repository:

```
admin@debian11:~/net-auto$ git log
commit 045c1aa80b2a75f304eff4f001c77dfba23935e7 (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 03:02:43 2022 +0000

    Adding .gitignore file

commit dcddb60add227e99c7ece91d22aa7f9e2001c268
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:58:42 2022 +0000

    Add Python script to talk to network switches

commit 097bbd348c5148d2f788ee00a8d59c7462e7e836
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:54:14 2022 +0000

    Add configuration for sw5

commit 0bc86eb847083a38e5cffedd780fd0a5217a90db
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:34:24 2022 +0000

    Update sw1, add sw4

commit 3121e674be42b59e0af4bcfbb30ad5d61dd45fdd
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:24:11 2022 +0000

    First commit to new repository
```

### Viewing brief log information

The `git log` command has multiple options—too many to cover here. One of the more useful options that we’ve already shown you, the `--oneline` option, would produce the following output for the same example repository:

```
admin@debian11:~/net-auto$ git log --oneline
045c1aa (HEAD -> main) Adding .gitignore file
dcddb60 Add Python script to talk to network switches
097bbd3 Add configuration for sw5
0bc86eb Update sw1, add sw4
3121e67 First commit to new repository
```

As you can see from this output, `--oneline` abbreviates the SHA-1 hash and lists only the commit message. For repositories with a lengthy history, it may be most helpful to start with `git log --oneline` and then drill into the details of a specific commit.

###### Tip

Disabling Git’s default behavior to pipe output through a pager can make finding things via the use of `grep` possible. To disable Git’s pager functionality, use the `--no-pager` option, as in `git --no-pager log --oneline`.

To drill into the details of a specific commit, you have a few options. First, you can use the `git log` command and supply a range of commits to show. The syntax is `git log start SHA..end SHA`. So, if you want to show more details on the last couple of commits in our example repository, you run a command that looks like this (if you’re wondering where the SHA-1 values came from, refer to the output of `git log --oneline` from earlier in this section, and recall that you need to supply only the first seven characters of the SHA-1 hash):

```
admin@debian11:~/net-auto$ git log dcddb60..045c1aa
commit 045c1aa80b2a75f304eff4f001c77dfba23935e7 (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 03:02:43 2022 +0000

    Adding .gitignore file
```

Git also has symbolic names that you can use in commands like `git log` (and others). We’ve already reviewed HEAD. If you want to use the commit just before HEAD, you reference that symbolically as `HEAD~1`. If you want to refer to the commit two places back from HEAD, you use `HEAD~2`; for three commits back, it’s `HEAD~3`. (You can probably spot the pattern.) In this case, with this particular repository, this command produces the same results as the previous command we showed you:

```
admin@debian11:~/net-auto$ git log HEAD~1..HEAD
commit 045c1aa80b2a75f304eff4f001c77dfba23935e7 (HEAD -> main)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 03:02:43 2022 +0000

    Adding .gitignore file
```

When we expand our discussion of HEAD later in this chapter, you’ll understand why we said “in this case, with this particular repository” that the two `git log` commands would produce the same output.

### Drilling into information on specific commits

Another way to drill into the details of a particular commit is to use the `git cat-file` command. Git, like so many other Unix/Linux tools, treats everything as a file. Thus, commits can be treated as a file and their “contents” shown on screen. This is what the `git cat-file` command does. So, taking the abbreviated SHA-1 from a particular commit, you can look at more details about that commit with a command like this:

```
admin@debian11:~/net-auto$ git cat-file -p 097bbd3
tree b289b034cab1ca9a95de8604d8576c5a752ae601
parent 0bc86eb847083a38e5cffedd780fd0a5217a90db
author John Smith <john.smith@networktocode.com> 1644375254 +0000
committer John Smith <john.smith@networktocode.com> 1644375254 +0000

Add configuration for sw5
```

(The `-p` option to `git cat-file`, by the way, just does some formatting of the output based on the type of file. The man page for `git cat-file` will provide more details on this and other switches.)

You’ll note this output contains a couple of pieces of information that the default `git log` output doesn’t show: the parent commit SHA-1 and the tree object SHA-1. You can use the parent commit SHA-1 to see this commit’s parent commit. Every commit has a parent commit that lets you follow the chain of commits all the way back to the initial one, which is the only commit in a repository without a parent. The tree object SHA-1 captures the files that are in the repository at the time of a given commit; we used this earlier with the `git ls-tree` command, like this:

```
[ec2-user@amazonlinux2 net-auto]$ git ls-tree c703cdf
100644 blob 0835e4f9714005ed591f68d306eea0d6d2ae8fd7	sw1.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw2.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw3.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw4.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw5.txt
[ec2-user@amazonlinux2 net-auto]$
```

Using the SHA-1 checksums listed here, you could then use the `git cat-file` command to view the content of one of these files at that particular time (as of that particular commit).

Let’s see how that works. In the following set of commands, you first use `git log ​--⁠oneline` to show the history of commits to a repository. Then you use `git cat-file` and `git ls-tree` with the appropriate seven-character SHA-1 hashes to display the contents of a particular file at two different points in time (as of two commits):

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
554b084 (HEAD -> main) Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
ubuntu@ubuntu2004:~/net-auto$ git cat-file -p 6b9b6cd
tree cdba8229f6ffb6fec5364ea3ec083e513b029d8a
author John Smith <john.smith@networktocode.com> 1644373442 +0000
committer John Smith <john.smith@networktocode.com> 1644373442 +0000

First commit to new repository
ubuntu@ubuntu2004:~/net-auto$ git ls-tree 6b9b6cd
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw1.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw2.txt
100644 blob 02df3d404d59d72c98439f44df673c6038352a27    sw3.txt
ubuntu@ubuntu2004:~/net-auto$ git cat-file -p 02df3d
interface ethernet0

interface ethernet1

interface ethernet2

interface ethernet3
```

This shows you the contents of *sw1.txt* as of the initial commit. Now, let’s repeat the same process for the second commit:

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
554b084 (HEAD -> main) Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
ubuntu@ubuntu2004:~/net-auto$ git cat-file -p dd61e7b
tree a0b53a7d568b0d46d87edd50fd3b553b5b414258
parent 6b9b6cd6a05ae85c22f870c6319b3158808d379c
author John Smith <john.smith@networktocode.com> 1644374061 +0000
committer John Smith <john.smith@networktocode.com> 1644374061 +0000

Update sw1, add sw4
ubuntu@ubuntu2004:~/net-auto$ git ls-tree dd61e7b
100644 blob 0835e4f9714005ed591f68d306eea0d6d2ae8fd7	sw1.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw2.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw3.txt
100644 blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391	sw4.txt
ubuntu@ubuntu2004:~/net-auto$ git cat-file -p 0835e4f
interface ethernet0
  duplex auto

interface ethernet1

interface ethernet2

interface ethernet3
```

Ah, note that the contents of the *sw1.txt* file have changed! However, this is a bit laborious—wouldn’t it be nice if there were an easier way to show the differences between two versions of a file within a repository? This is where the `git diff` command comes in handy.

## Distilling Differences Between Versions of Files

We mentioned at the start of this chapter that one of the benefits of using version control for network automation artifacts (switch configurations, Python scripts, Jinja templates, etc.) is being able to see the differences between versions of files over time. In the previous section, we showed you a manual method of doing so; now we’re going to show you the easy way: the `git diff` command.

###### Note

Git also supports integration with third-party diff tools, including graphical diff tools. In such cases, you would use `git difftool` instead of `git diff`.

### Examining differences between commits

The `git diff` command shows the differences between versions of a file (the differences between a file at two points in time). You just need to supply the two commits and the file to be compared. Here’s an example. First, you list the history by using `git log`, and then you use `git diff` to compare two versions of a file:

```
[ec2-user@amazonlinux2 net-auto]$ git log --oneline
9c66592 (HEAD -> main) Adding .gitignore file
b67c1dd Add Python script to talk to network switches
c703cdf Add configuration for sw5
f3a00e6 Update sw1, add sw4
8d18465 First commit to new repository
[ec2-user@amazonlinux2 net-auto]$ git diff 8d18465..f3a00e6 sw1.txt
diff --git a/sw1.txt b/sw1.txt
index 02df3d4..2567e07 100644
--- a/sw1.txt
+++ b/sw1.txt
@@ -1,4 +1,5 @@
 interface ethernet0
+  duplex auto

 interface ethernet1

[ec2-user@amazonlinux2 net-auto]$
```

The format in which `git diff` shows the differences between the files can be a bit confusing at first. The key in deciphering the output lies in the lines just after the `index...` line. There, `git diff` tells you that dashes will be used to represent file *a* (`--- a/sw1.txt`), and pluses will be used to represent file *b* (`+++ b/sw1.txt`). Following that is the representation of the differences in the files—lines that exist in file *a* are preceded by a dash, while lines that exist in file *b* are preceded by a plus. Lines that are the same in both files are preceded by a space.

Thus, in this example, you can see that in the later commit, represented by the hash `f3a00e6`, the line `duplex auto` was added. Obviously, this is a simple example, but hopefully you can begin to see just how useful this is.

###### Tip

If you omit the filename with the `git diff` command (for example, if you enter `git diff` *`start SHA..end SHA`*), then Git will show a diff for *all* the files changed in that commit, rather than just a specific file referenced on the command line. Adding the filename to the `git diff` command allows you to focus on the changes in a specific file.

### Viewing other types of differences

Let’s change the configuration file for *sw1.txt* so that the diff is a bit more complex, and then we’ll also show how you can use `git diff` in other ways.

First, you’ll make some changes to *sw1.txt* by using the text editor of your choice. It doesn’t really matter what the changes are; you’ll run `git status` to confirm that changes exist in the working directory. However, *before* you stage the changes, let’s see if you can use `git diff` again:

```
admin@debian11:~/net-auto$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

    modified:   sw1.txt

no changes added to commit (use "git add" and/or "git commit -a")
admin@debian11:~/net-auto$ git diff
diff --git a/sw1.txt b/sw1.txt
index 2567e07..7005dc6 100644
--- a/sw1.txt
+++ b/sw1.txt
@@ -1,9 +1,11 @@
 interface ethernet0
-  duplex auto
+  switchport mode access vlan 101

 interface ethernet1
+  switchport mode trunk

 interface ethernet2
+  switchport mode access vlan 102

 interface ethernet3
-
+  switchport mode trunk
```

Running `git diff` like this—without any parameters or options—shows you the differences between your working tree and the index. That is, it shows you the changes that have not yet been staged for the next commit.

Now, let’s stage the changes in preparation for the next commit and then see if there’s another way to use `git diff`:

```
admin@debian11:~/net-auto$ git add sw1.txt
admin@debian11:~/net-auto$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

    modified:   sw1.txt

admin@debian11:~/net-auto$ git diff
admin@debian11:~/net-auto$ git diff --cached
diff --git a/sw1.txt b/sw1.txt
index 2567e07..f3b5ad5 100644
--- a/sw1.txt
+++ b/sw1.txt
@@ -1,9 +1,11 @@
 interface ethernet0
-  duplex auto
+  switchport mode access vlan 101

 interface ethernet1
+  switchport mode trunk

 interface ethernet2
+  switchport mode access vlan 102

 interface ethernet3
-
+  switchport mode trunk
```

You can see that the first `git diff` command returns no results, which makes sense—there are no changes that *aren’t* staged for the next commit. However, when you add the `--cached` parameter, it tells `git diff` to show the differences between the index and HEAD. In other words, this form of `git diff` shows the differences between the index and the last commit.

Once you finally commit this last set of changes, you can circle back around to your original use of `git diff`, which allows you to see the changes between two arbitrary commits:

```
admin@debian11:~/net-auto$ git commit -m "Defined VLANs on sw1"
[main 3588c31] Defined VLANs on sw1
 1 file changed, 4 insertions(+), 2 deletions(-)
admin@debian11:~/net-auto$ git status
On branch main
nothing to commit, working directory clean
admin@debian11:~/net-auto$ git log --oneline
ead6f37 (HEAD -> main) Defined VLANs on sw1
045c1aa Adding .gitignore file
dcddb60 Add Python script to talk to network switches
097bbd3 Add configuration for sw5
0bc86eb Update sw1, add sw4
3121e67 First commit to new repository
admin@debian11:~/net-auto$ git diff 0bc86eb..ead6f37 sw1.txt
diff --git a/sw1.txt b/sw1.txt
index 2567e07..f3b5ad5 100644
--- a/sw1.txt
+++ b/sw1.txt
@@ -1,9 +1,11 @@
 interface ethernet0
-  duplex auto
+  switchport mode access vlan 101

 interface ethernet1
+  switchport mode trunk

 interface ethernet2
+  switchport mode access vlan 102

 interface ethernet3
-
+  switchport mode trunk
```

In several of the commands we’ve shown you thus far, you’ve had to reference a specific commit’s SHA-1 hash (at least, the first seven characters of it). That’s not a significant problem when your repository has a relatively small number of commits; you can fairly easily use `git log --oneline` to see the list of commits and find the one you want.

What if your repository has thousands of commits? What if you’re collaborating with others on a repository, so you’re not familiar with the commits listed by `git log`? Is there an easier way to find an important commit you might need later? In fact, there is. The next section discusses Git’s tagging functionality, which makes it easy to mark and refer back to important commits in your repository’s commit history.

## Tagging Commits in Git

*Tags* are essentially pointers to a specific commit. As such, they can be used in place of a commit hash. At first glance, this may not seem enormously useful, but let’s consider the current state of our repository as viewed using `git log --oneline`:

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
d268c37 (HEAD -> main) Defined VLANs on sw1
554b084 Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
```

Now, let’s say that commit `d40fe74` represents some sort of significant milestone in the development of the repository, like the state of the repository when the network initially went live. You can *tag* this commit with a user-friendly name—perhaps something like `golive` or `v1.0`—and then refer to this user-friendly name instead of having to remember the SHA-1 hash. So, if you want to compare the state of a file now versus at the time of initial roll-out using `git diff`, the command would be something like `git diff HEAD..golive sw1.txt` instead of the more esoteric `git diff HEAD..d40fe74`.

The process for tagging a commit involves the use of the `git tag name commit-hash`. If you omit the commit hash, the tag will be added to the latest commit, aka HEAD. This means that it is easy to tag commits after the fact, if necessary, so let’s add a couple of tags to our repository by using `git tag`:

```
ubuntu@ubuntu2004:~/net-auto$ git tag golive d40fe74
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
d268c37 (HEAD -> main) Defined VLANs on sw1
554b084 Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 (tag: golive) Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
```

Note the addition of the tag to the specific commit in the output of `git log`. You can verify that the tag refers to the commit fairly easily by using `git show`, once referencing the tag and once referencing the specific commit hash:

```
ubuntu@ubuntu2004:~/net-auto$ git show golive
commit d40fe743568a82b89c93ca58279855762f091305 (tag: golive)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:54:18 2022 +0000

    Add configuration for sw5

diff --git a/sw5.txt b/sw5.txt
new file mode 100644
index 0000000..e69de29
ubuntu@ubuntu2004:~/net-auto$ git show d40fe74
commit d40fe743568a82b89c93ca58279855762f091305 (tag: golive)
Author: John Smith <john.smith@networktocode.com>
Date:   Wed Feb 9 02:54:18 2022 +0000

    Add configuration for sw5

diff --git a/sw5.txt b/sw5.txt
new file mode 100644
index 0000000..e69de29
```

This is an example of what Git calls a *lightweight tag.* It is only a pointer to the commit. Git also supports *annotated tags*, which are full objects in the repository and have their own metadata. To create an annotated tag, you’ll add the `-a` flag to the `git tag` command. Let’s create an annotated tag in our repository:

```
ubuntu@ubuntu2004:~/net-auto$ git tag -a v1.0 d268c37 -m "Version 1.0 release"
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
d268c37 (HEAD -> main, tag: v1.0) Defined VLANs on sw1
554b084 Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 (tag: golive) Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
```

Like the `git commit` command, using `git tag` to create an annotated tag supports the use of `-m` to add a tag message (lightweight tags don’t require tag messages). If you don’t specify one, Git will open your default editor so you can supply a tag message. That tag message is then displayed when users run `git show` against the tag name, like this:

```
ubuntu@ubuntu2004:~/net-auto$ git show v1.0
tag v1.0
Tagger: John Smith <john.smith@networktocode.com>
Date:   Sat Mar 5 21:35:53 2022 +0000

Version 1.0 of network automation tools

commit d268c37b57c01962b0829df946fe19c67e4da448 (tag: v1.0)
Author: John Smith <john.smith@networktocode.com>
Date:   Thu Feb 10 05:04:47 2022 +0000

    Defined VLANs on sw1

diff --git a/sw1.txt b/sw1.txt
index 0835e4f..58d8b7d 100644
--- a/sw1.txt
+++ b/sw1.txt
@@ -1 +1,12 @@
-change
+interface ethernet0
+  duplex auto
+  switchport mode access vlan 101
+
+interface ethernet1
+  switchport mode trunk
+
+interface ethernet2
+  switchport mode access vlan 102
+
+interface ethernet3
+  switchport mode trunk
```

To list all the tags found in a Git repository, just use `git tag` or `git tag --list`. Any tag listed in the output can be used in place of a commit hash in commands like `git diff` or others. To delete a tag, use `git tag -d tag-name`.

###### Tip

When should you use annotated tags versus lightweight tags? The generally accepted practice is that annotated tags should be used for any long-term purposes, such as for version/release management. In such instances, you will want the ability to store additional metadata about the tag, and possibly even cryptographically sign the tag using GNU Privacy Guard (GnuPG). Lightweight tags, on the other hand, are primarily intended for temporary object labels.

Before we move on to our next topic—branches in Git—let’s take a moment to review what you’ve done so far:

- Staged changes (using `git add`) and committed them to the repository (using `git commit`)
- Modified the configuration of Git (using `git config`)
- Unstaged changes that weren’t yet ready to be committed (using `git restore` or the previous `git reset` method)
- Excluded files from inclusion in the repository (using `.gitignore`)
- Reviewed the history of the repository (using `git log`)
- Compared different versions of files within the repository to see the changes in each version (using `git diff`)
- Bookmarked specific commits in a repository (using `git tag`)

In the next section, we expand our discussion of Git to cover what is, arguably, one of Git’s most powerful features: branching.

# Branching in Git

As we’ve stated previously, one of the primary design goals for Git was strong support for nonlinear development. That’s a fancy way of saying that Git needed to support multiple developers working on the same thing at the same time. So how is this accomplished? Git does it through the use of branches.

A *branch* in Git is a pointer to a commit. Now, that might not sound too powerful, so let’s use some illustrations to help better explain the concept of a branch and why nonlinear development in Git can be powerful.

First, recall from [“Overview of Git’s Architecture”](#overview_of_gits_architecture) that Git uses a series of objects: blobs (representing the content of files in the repository), trees (representing the file and directory structure of the repository), and commits (representing a point-in-time snapshot of the repository, its structure, and its content). You can visualize this as shown in [Figure 11-1](#gitobjects).

![npa2 1101](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1101.png)

###### Figure 11-1. Objects in a Git repository

Each of these objects is identified by the SHA-1 hash of its contents. You’ve seen how commits are referenced via their SHA-1 hash, and you’ve seen how to use the `git ls-tree` or `git cat-file` commands to see the contents of tree and blob objects, respectively, by referencing their SHA-1 hash.

As you make changes and commit them to the repository, you create more commit objects (more snapshots), each of which points back at the previous commit (referred to as its *parent* commit; you saw this in [“Viewing More Information About a Repository”](#viewing_more_information_about_a_repository)). After a few commits, you can visualize it like [Figure 11-2](#commitchain) (we’ve omitted the blobs to simplify the diagram).

![npa2 1102](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1102.png)

###### Figure 11-2. A chain of commits in a Git repository

Each commit points to a tree object, and each tree object points to blobs that represent the contents of the repository at the time of the commit. Using the reference to the tree object and the associated blobs, you can re-create the state of the repository at any given commit—hence why we refer to commits as point-in-time snapshots of the repository.

This is all well and good—and helps to explain Git’s architecture a bit more fully—but what does it have to do with branching in Git? To answer that question (and we *will* answer it, we promise!), we need to revisit the concept of HEAD. Previously, we defined HEAD as a pointer to the latest commit, or to the commit we’ve checked out into the working directory. You visualize HEAD as something like [Figure 11-3](#headpointer).

![npa2 1103](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1103.png)

###### Figure 11-3. HEAD pointing to the latest commit

You can verify this using a procedure outlined earlier in this chapter (this assumes you haven’t checked out a different branch or different commit, something we’ll discuss shortly):

1. From the repository’s working directory, run **`cat .git/refs/heads/main`**. Note the value displayed.
2. Compare the value of the previous command to the value of the last commit from the output of `git log --oneline`. You should see the same value in both places, indicating that HEAD points to the latest commit.

By default, *every* Git repository starts out with a single branch, named *master* (by default; this is configurable). As a branch is just a reference to a commit, this is illustrated graphically in [Figure 11-4](#defaultbranch).

![npa2 1104](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1104.png)

###### Figure 11-4. HEAD pointing to the latest commit in the default branch

You can see that the branch reference points to a commit, and that HEAD points to the branch reference.

###### Note

To avoid cultural insensitivity, numerous Git-based online services have moved away from the use of *master* to denote the default branch and have started using *main* instead (GitHub is one example). Users can use `git config --global init.defaultBranch <name>` to tell Git to use a different name, like *main*, for the initial default branch. See [“Creating a Repository”](#creating_a_repository) for more information on creating a Git repository. We are using *main* as the name for the default branch in this chapter.

However, you’re not limited to only a single branch in a Git repository. In fact, because branches are so lightweight (a reference to a commit), you’re strongly encouraged to use multiple branches. So, when you create a new branch—let’s call this new branch *testing*, though the name doesn’t really matter—the organization of the Git objects now looks something like [Figure 11-5](#testingbranch).

![npa2 1105](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1105.png)

###### Figure 11-5. New branch created in a Git repository

So, you’ve created the new branch—we’ll show you the commands to do that shortly—and the new branch now references a particular commit. However, HEAD hasn’t moved. HEAD gets moved when you check out content in the repository, so to move HEAD to the new branch, you first have to *check out* the new branch. Similarly, if you want to work with the repository at an earlier point in time (at an earlier commit) you need to check out that particular commit. Once you check out a branch, HEAD now points to the new branch, as in [Figure 11-6](#testingcheckedout).

![npa2 1106](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1106.png)

###### Figure 11-6. HEAD pointing to a checked-out branch

At this point, you can start making changes and committing them to the repository. This is where branches start to really show their power: they *isolate new changes from other branches*. Let’s assume you’ve made some changes to the testing branch and have committed those changes to the repository. The graphical view of the objects and relationships inside the repository now looks like [Figure 11-7](#branchcommits).

![npa2 1107](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1107.png)

###### Figure 11-7. Adding a commit to a branch

You’ll note that the testing branch—and HEAD—move forward to represent the latest commit, but the default branch remains *untouched*. At any point, you can check out the default branch and be right back where you were before you created the new branch and made the changes. This diagram shows how multiple branches can evolve over time and allow for the development of hotfixes, new features, and new releases without affecting other branches.

[Figure 11-8](#multibranch) is a complicated example of branches, but it gives an idea of how branches *might* be used in a typical software development environment.

![npa2 1108](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1108.png)

###### Figure 11-8. Multiple branches in a development cycle

Hopefully, the wheels in your head are turning, and you’re starting to think about the possibilities that branches create:

- You can create a new branch when you want to try something new or different, without affecting what’s in the default (or main) branch. If it doesn’t work out, no big deal—the content in other branches, including the default branch, remains untouched.
- Branches form the basis for collaborating with other authors on the same repository. If you’re working in branch A and your coworker is working in branch B, then you’re assured that you won’t affect each other’s changes. (Now, you might have some issues when it comes time to bring the changes from the two branches together in a *merge*, but that’s a different story—one we tackle in [“Merging and Deleting Branches”](#mergin_and_deleting_branches).)

We’ve mentioned the default branch several times in this section. While, strictly speaking, Git has no concept of a default branch, there must always be at least one branch, and if you haven’t explicitly created one, Git will create one for you. We think of this as the *default branch*. We also mentioned that most open source communities and many Git-based online services are moving away from the use of *master* as the name for the default branch, and switching to something like *main* or *default* instead. Before we turn our attention to actually working with Git branches, we’d like to first show you how to rename the default branch.

## Renaming the Default Branch

For now, before we get into collaborating with Git (in [“Collaborating with Git”](#collaborating_with_git)), you can rename the default branch on your Git repository with one simple command: `git branch -m old_name new_name`. In fact, you can use this command to rename *any* branch.

If you didn’t set the `init.defaultBranch` configuration setting with `git config` and end up with a *master* branch after running `git init`, you can use this command to easily change the name of the branch to *main* or *default* or whatever you’d like.

The process for renaming branches gets a little more complicated once you start adding Git remotes—which we cover in the collaboration section—but until then it’s pretty straightforward to rename a branch.

Now let’s turn our attention to the practical side of working with Git branches, where you can see the theory we’ve been describing in practice.

## Creating a Branch

To create a Git branch—which, again, is just a reference to a commit—you use the `git branch` command. So, to create the testing branch we discussed in the previous section, you’d simply run `git branch testing`. The command doesn’t produce any output, but there *is* a way you can verify that it actually did something.

First, look in the *.git/refs/heads* directory, and you’ll see a new entry named after your newly created branch. If you run `cat` on that new file, you’ll see that it points to the commit referenced by HEAD when you created the branch. Let’s see that in action:

```
ubuntu@ubuntu2004:~/net-auto$ git branch testing
ubuntu@ubuntu2004:~/net-auto$ ls -la .git/refs/heads
total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb 10 05:19 .
drwxrwxr-x 4 ubuntu ubuntu 4096 Feb  9 02:20 ..
-rw-rw-r-- 1 ubuntu ubuntu   41 Feb 10 05:18 main
-rw-rw-r-- 1 ubuntu ubuntu   41 Feb 10 05:19 testing
ubuntu@ubuntu2004:~/net-auto$ cat .git/refs/heads/testing
d268c37b57c01962b0829df946fe19c67e4da448
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
d268c37 (HEAD -> main, testing) Defined VLANs on sw1
554b084 Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
```

The presence of the *testing* file in *.git/refs/heads*, along with the content of the file referencing the latest commit as of the time of creation, shows that the branch has been created. You can also verify this by simply running `git branch`, which will output the list of branches. The active branch—the branch that is *checked out* for use in the working directory—will have an asterisk before it (and, if colors are enabled in your terminal, may be listed in a different color). This shows you that your testing branch has been created, but not checked out—the main branch is still active.

To switch the active branch, you must first check out the branch.

## Checking Out a Branch

To *check out* a branch means to make it the active branch, the branch that will be available in the working directory for you to edit/modify. To check out a branch, use `git checkout`, supplying the name of the branch you’d like to check out:

```
admin@debian11:~/net-auto$ git branch
* main
  testing
admin@debian11:~/net-auto$ git checkout testing
Switched to branch 'testing'
```

###### Tip

You can create a branch and check it out at the same time by using `git checkout -b branch name`.

Let’s make a simple change to the repository—say, let’s add a file—and then switch back to the main branch to see how Git handles this. First, we’ll stage *sw6.txt* to the repository and commit it to the testing branch:

```
[ec2-user@amazonlinux2 net-auto]$ git add sw6.txt
[ec2-user@amazonlinux2 net-auto]$ git commit -m "Add sw6 configuration"
[testing 3a6f8cb] Add sw6 configuration
 1 file changed, 7 insertions(+)
 create mode 100644 sw6.txt
[ec2-user@amazonlinux2 net-auto]$
```

Note that the response from Git when you commit the change includes the branch name and the SHA-1 hash of the commit (`[testing 3a6f8cb]`). A quick `git log --oneline` will verify that the latest commit has the same hash as reported by the `git commit` command. Likewise, a quick `cat .git/HEAD` will show that you’re on the testing branch (because it points to *.git/refs/heads/testing*), and `cat .git/refs/heads/testing` will also show the latest commit SHA-1 hash. This shows that HEAD points to the latest commit in the checked-out branch.

# Viewing Git Branch Information in the Prompt

When you’re working with multiple branches in a Git repository, it can sometimes be challenging to know *which* branch is currently active (checked out). To help address this, most distributions of Git since version 1.8 have included support to allow bash—the shell most Linux distributions use by default—to display the currently active Git branch in the bash prompt.

On Debian and Debian derivatives like Ubuntu, this file is named *git-sh-prompt* and is found in the */usr/lib/git-core* directory. On RHEL-like distributions like Fedora and Amazon Linux 2, the file is named *git-prompt.sh* and is found in the */usr/share/git-core/contrib/completion* directory. On macOS, the file is installed as part of the Xcode command-line tools, is named *git-prompt.sh*, and is found in the */Library/Developer/CommandLineTools/usr/share/git-core* directory. The instructions for using this functionality are found at the top of the appropriate file for your OS.

Now, let’s switch back to the main branch and see the working directory:

```
[ec2-user@amazonlinux2 net-auto]$ git checkout main
Switched to branch 'main'
[ec2-user@amazonlinux2 net-auto]$ ls -la
total 12
drwxrwxr-x 3 ec2-user ec2-user 151 Feb 11 05:04 .
drwx------ 4 ec2-user ec2-user 145 Feb 11 04:56 ..
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 03:00 credentials.yml
drwxrwxr-x 8 ec2-user ec2-user 166 Feb 11 05:04 .git
-rw-rw-r-- 1 ec2-user ec2-user  16 Feb  9 03:00 .gitignore
-rw-rw-r-- 1 ec2-user ec2-user 634 Feb  9 02:56 script.py
-rw-rw-r-- 1 ec2-user ec2-user 213 Feb 10 05:04 sw1.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:22 sw2.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:22 sw3.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:32 sw4.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:37 sw5.txt
[ec2-user@amazonlinux2 net-auto]$
```

Wait—​the *sw6.txt* file is *gone!* What happened? Not to worry, you haven’t lost anything. Recall that checking out a branch makes it the active branch, and therefore the branch that will be present in the working directory for you to modify. The *sw6.txt* file isn’t in the main branch, it’s in the testing branch, so when you switched to main by using `git checkout main`, that file was removed from the working directory. Recall also that the working directory *isn’t* the same as the repository—​even though the file has been removed from the working directory, it’s *still* in the repository, as you can easily verify:

```
[ec2-user@amazonlinux2 net-auto]$ git checkout testing
Switched to branch 'testing'
[ec2-user@amazonlinux2 net-auto]$ ls -la
total 16
drwxrwxr-x 3 ec2-user ec2-user 166 Feb 11 05:05 .
drwx------ 4 ec2-user ec2-user 145 Feb 11 04:56 ..
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 03:00 credentials.yml
drwxrwxr-x 8 ec2-user ec2-user 166 Feb 11 05:05 .git
-rw-rw-r-- 1 ec2-user ec2-user  16 Feb  9 03:00 .gitignore
-rw-rw-r-- 1 ec2-user ec2-user 634 Feb  9 02:56 script.py
-rw-rw-r-- 1 ec2-user ec2-user 213 Feb 10 05:04 sw1.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:22 sw2.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:22 sw3.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:32 sw4.txt
-rw-rw-r-- 1 ec2-user ec2-user   0 Feb  9 02:37 sw5.txt
-rw-rw-r-- 1 ec2-user ec2-user  83 Feb 11 05:05 sw6.txt
[ec2-user@amazonlinux2 net-auto]$
```

This illustrates how branches help isolate changes from the main branch, a key benefit of using branches. Using a branch, you can make some changes, test those changes, and then discard them if necessary—​all while knowing that your main branch remains safe and untouched.

The preceding example shows what happens to committed changes and how the working directory changes when you switch branches, but what happens to uncommitted changes when you switch branches?

- For untracked files (files that don’t already exist in the repository), changes are left in the working directory. This is easy to demonstrate: create a new, untracked file in the working directory and then switch to a new branch. You’ll still see the untracked file in the working directory, and `git status` will report the file as an untracked file in either branch. The contents of the untracked file won’t change as you switch branches.
- For tracked files, uncommitted changes are saved into a temporary area called a *stash*, and the contents of the tracked file are restored to what’s stored in the commit referenced by the branch to which you switched.

Before looking at merging branches, we’d like to first review stashing in a bit more detail. Knowing how to stash uncommitted changes is useful when working with multiple branches.

## Stashing Uncommitted Changes

*Stashing* changes places those changes into a temporary storage area so that you can recall them later. There are numerous use cases for stashing; the one you’ve seen so far is capturing uncommitted changes so you can switch branches, but we’ll mention others as we progress through the chapter.

Here’s one example: say you need to add switch configuration changes to your network automation repository, so you start hacking away on the updated configuration only to realize at some point later than you forgot to create a branch in which to store these changes. Now what? The easiest thing for you to do is stash your changes, create a branch for your changes, and then apply the stash to the branch. Effectively, this allows you to move uncommitted changes from one branch to another.

Stashing in Git is handled via the `git stash` command, which has subcommands to add changes to the stash (`git stash push`), to list the stashed changes (`git stash list`), to examine the stashed changes (`git stash show`), and to take the changes from the stash and put them back into the working directory (`git stash pop`).

Using the preceding situation as our example—​you’ve made changes with the wrong branch checked out, and you realized your mistake before committing the changes—​we’ll walk through using the various `git stash` commands.

First, let’s make sure that the main branch is checked out:

```
ubuntu@ubuntu2004:~/net-auto$ git branch
* main
```

Great. Now we’re going to make some changes on the main branch, which—​especially when working with others in a single repository—​is generally not recommended (the changes should be isolated on their own branch). For example, let’s make some changes to *sw5.txt*, and then run `git status`:

```
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sw5.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

When you review the output of `git status`, you realize that you’re on the main branch instead of in a feature branch. This is where using `git stash` comes into play. The first step is to push the changes onto the stash:

```
ubuntu@ubuntu2004:~/net-auto$ git stash push -m "Updated changes for sw5"
Saved working directory and index state On main: Updated changes for sw5
ubuntu@ubuntu2004:~/net-auto$ git status
On branch main
nothing to commit, working tree clean
ubuntu@ubuntu2004:~/net-auto$ git stash list
stash@{0}: On main: Updated changes for sw5
```

The `git stash push` command pushes changes into (or onto) the stash. It supports the `-m` parameter to add a message; if you omit a message, the command will use the commit message from the last commit as the description. In our experience, this often isn’t very helpful, so we recommend using `-m` to add a stash-specific message to help you understand the contents of the stash. Once the changes are pushed into the stash, Git restores the working directory to match HEAD, as illustrated by the output of `git status`.

The `git stash list` command shows that the stash was created and shows the syntax for how Git refers to stashes (`stash@{0}` in this case).

To see what’s in this stash, you can use the `git stash show` command:

```
ubuntu@ubuntu2004:~/net-auto$ git stash show stash@{0}
 sw5.txt | 9 +++++++++
 1 file changed, 9 insertions(+)
```

The output of `git stash show` shows the changes in the stash as a diff (similar to how `git diff` works). The diff is between the stashed contents and the commit when the stash entry was first created.

Next, create a new branch, and then use the `git stash pop` command to apply the changes from the stash to the new branch:

```
ubuntu@ubuntu2004:~/net-auto$ git checkout -b sw5-updates
Switched to a new branch 'sw5-updates'
ubuntu@ubuntu2004:~/net-auto$ git status
On branch sw5-updates
nothing to commit, working tree clean
ubuntu@ubuntu2004:~/net-auto$ git stash pop stash@{0}
On branch sw5-updates
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sw5.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped stash@{0} (cf8fab0f7083feb5a817ab5933e9028bd64407d1)
ubuntu@ubuntu2004:~/net-auto$ git stash list
```

The `git stash pop` command takes the changes from a stash, applies them to the checked-out branch, and then drops the stash. As a result of dropping the stash, `git stash list` no longer shows it in the list of stashes. After the changes in the stash are applied to the checked-out branch, `git status` shows there are now unstaged changes in the working directory, and in the correct branch this time!

###### Tip

The `git stash` command has a `pop` as well as an `apply` subcommand. Both take changes from the specified stash and apply them against the working directory of the checked-out branch, but they aren’t the same! The `git stash pop` command drops the stash afterward, assuming no conflicts were encountered. However, `git stash apply` does not drop the stash afterward; you have to use `git stash drop` manually to drop the stash.

To summarize:

- Use `git stash push` to take uncommitted changes and stash them away, restoring the working directory to HEAD.
- Use `git stash list` to see the list of stashed changes.
- The `git stash show` command shows the stashed changes as a diff against the commit when the stash was created.
- Changes in a stash can be used with the `git stash pop` command.

Although our example scenario leveraged only a single stash entry, it is possible to have multiple stash entries. When you have multiple stash entries, be sure to append the appropriate stash name when using `git stash show` or `git stash pop`.

It’s now time to circle back to our discussion of Git branches. Stashes are useful in preserving uncommitted changes when switching between branches, or perhaps even to move uncommitted changes from one branch to another. Branches themselves are useful for isolating committed changes away from other branches. What about when you’re ready to make committed changes a permanent part of your repository? Perhaps you create a branch to try out a new Jinja template, and it works perfectly so you want to keep it. What’s the next step? This is where *merging* branches comes into play.

## Merging and Deleting Branches

Before we get into merging branches, let’s revisit the contents of a commit object in Git. In our example repository, you’ll examine the contents of the latest commit object for the testing branch:

```
admin@debian11:~/net-auto$ git checkout testing
Switched to branch 'testing'
admin@debian11:~/net-auto$ git cat-file -p 2e6fced
tree e895cac9760eba8d16b85a57ee8fff6fe9c590db
parent ead6f372effce74de8d96deade198a09558a5432
author John Smith <john.smith@networktocode.com> 1644556039 +0000
committer John Smith <john.smith@networktocode.com> 1644556039 +0000

Add sw6 configuration
```

What does this tell you?

1. This particular commit references the tree object with the hash `2e6fced`.
2. The author and committer of this commit is John Smith.
3. The commit message indicates that this commit captures the addition of the configuration for sw6.
4. This commit has a parent commit with a hash of `ead6f37`.

We’ve mentioned before that every commit (except the very first commit) has a pointer to a parent commit. This is illustrated in Figures [11-2](#commitchain) through [11-7](#branchcommits), where the commit objects point “backward in time” to the previous commit.

When you merge branches, Git is going to create a new commit object—​called a *merge commit* object—​that will actually have *two* parents. Each parent represents the two branches that were brought together as part of the merge process. In so doing, Git maintains the link back to previous commits so that you can always roll back to previous versions.

At a high level, the merge process looks like this:

1. Switch to the branch into which the other branch should be merged. If you’re merging back into main, check out (switch to) main.
2. Run the `git merge` command, specifying the name of the branch to be merged into main.
3. Supply a message (a commit message for the merge commit) describing the changes being merged.

### Reviewing fast-forward merges

Let’s see this in action. Let’s take the testing branch, which has a new switch configuration (*sw6.txt*) that isn’t present in the main branch, and merge it back into main.

First, let’s ensure you are on the main branch:

```
ubuntu@ubuntu2004:~/net-auto$ git branch
  main
* testing
ubuntu@ubuntu2004:~/net-auto$ git checkout main
Switched to branch 'main'
```

Next, let’s actually merge the testing branch into the main branch:

```
ubuntu@ubuntu2004:~/net-auto$ git merge testing
Updating d268c37..e70f353
Fast-forward
 sw6.txt | 7 +++++++
 1 file changed, 7 insertions(+)
 create mode 100644 sw6.txt
```

Note the `Fast-forward` in the response from Git; this indicates that it was possible to merge the branches by simply replaying the same set of changes to the main branch as was performed on the branch being merged. In situations like this—​a simple merge—​you won’t see an additional merge commit:

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline
e70f353 (HEAD -> main, testing) Add sw6 configuration
d268c37 Defined VLANs on sw1
554b084 Adding .gitignore file
ee7e7bf Add Python script to talk to network switches
d40fe74 Add configuration for sw5
dd61e7b Update sw1, add sw4
6b9b6cd First commit to new repository
ubuntu@ubuntu2004:~/net-auto$ ls -la sw6.txt
-rw-rw-r-- 1 ubuntu ubuntu 221 Jun  7 20:53 sw6.txt
```

### Deleting a branch

Once a branch (and its changes) have been merged, you can delete the branch by using `git branch -d+ branch-name`. You generally shouldn’t delete a branch before it’s been merged; otherwise, you’ll lose the changes stored in that branch (Git will prompt you if you try to delete a branch that hasn’t been merged). Once a branch has been merged, though, its changes are safely stored in another branch (typically the main branch, but not always), and it’s therefore now safe to delete.

### Reviewing merges with a merge commit

Now, let’s look at a more complex example. First, let’s create a new branch to store some changes you’ll make relative to the configuration for sw4. To do that, you’ll simply run `git checkout -b sw4`. This creates the new branch *and* checks it out so it’s the active branch. Once you’ve made some changes to *sw4.txt*, use `git add` and `git commit` to stage and commit the changes.

Next, let’s switch back to main (using `git checkout main`) and make changes to a *different* switch configuration. Stage and commit the changes to the main branch. Now what happens when you try to merge the sw4 branch into main?

Before we answer that question, let’s explore the commit objects a bit. Here are the contents of the last commit object in the sw4 branch:

```
admin@debian11:~/net-auto$ git checkout sw4
Switched to branch 'sw4'
admin@debian11:~/net-auto$ git log --oneline HEAD~2..HEAD
1bae927 (HEAD -> sw4) Update sw4 configuration
2e6fced (main) Add sw6 configuration
admin@debian11:~/net-auto$ git cat-file -p 1bae927
tree 72f0533c16734939d15624fbc41d47f33b54f7f9
parent 2e6fced00c8aad171d54a279232a569dec392f69
author John Smith <john.smith@networktocode.com> 1644556917 +0000
committer John Smith <john.smith@networktocode.com> 1644556917 +0000

Update sw4 configuration
```

The `git log --oneline HEAD~2..HEAD` command shows just the last two commits leading up to HEAD (which points to the last commit on the active branch). As you can see, this commit object points to a parent commit of `2e6fced`.

Here’s the last commit on the main branch:

```
admin@debian11:~/net-auto$ git checkout main
Switched to branch 'main'
admin@debian11:~/net-auto$ git log --oneline HEAD~2..HEAD
e222171 (HEAD -> main) Fix sw3 configuration for hypervisor
2e6fced Add sw6 configuration
admin@debian11:~/net-auto$ git cat-file -p e222171
tree c0c8034ab09379d350d718d8f1a63f1dbd033706
parent 2e6fced00c8aad171d54a279232a569dec392f69
author John Smith <john.smith@networktocode.com> 1644557833 +0000
committer John Smith <john.smith@networktocode.com> 1644557833 +0000

Fix sw3 configuration for hypervisor
```

This commit, the latest in the main branch, *also* points to the same parent commit—​showing that the two branches diverge.

Now let’s run the merge. First, you’ll verify you have the main branch checked out; then you’ll use `git merge` to actually perform the merge:

```
admin@debian11:~/net-auto$ git branch
* main
  sw4
admin@debian11:~/net-auto$ git merge sw4
(default Git editor opens to allow user to provide commit message)
Merge made by the 'recursive' strategy.
 sw4.txt | 9 +++++++++
 1 file changed, 9 insertions(+)
admin@debian11:~/net-auto$ git log --oneline HEAD~3..HEAD
8c34005 (HEAD -> main) Merge branch 'sw4'
e222171 Fix sw3 configuration for hypervisor
1bae927 (sw4) Update sw4 configuration
2e6fced Add sw6 configuration
```

In this instance, changes on *both* branches need to be reconciled when merging the branches. It isn’t possible to just “replay” the changes from the sw4 branch to main, because main has some changes of its own. Thus, Git creates a *merge commit*. Let’s look at that file real quick:

```
admin@debian11:~/net-auto$ git cat-file -p 8c34005
tree bff23ea7763a583586c0cf82e7651e35a7aa58fd
parent e2221715da5229e33ffd981c81d5874bb12957b7
parent 1bae92734368fc68a570539696aa4435c5ab5517
author John Smith <john.smith@networktocode.com> 1644558317 +0000
committer John Smith <john.smith@networktocode.com> 1644558317 +0000

Merge branch 'sw4'
```

Note the presence of *two* parent commits, which—​if you look—​represent the commits you made to each branch before merging the sw4 branch into main. This is how Git knows that the branches have converged and how Git maintains the relationship between commits over time.

Now that the commits in the sw4 branch have been merged into the main branch, you can just delete the sw4 branch by using `git branch -d sw4`:

```
admin@debian11:~/net-auto$ git branch -d sw4
Deleted branch sw4 (was 1bae927).
admin@debian11:~/net-auto$ git branch
* main
```

###### Warning

It’s possible to delete an unmerged branch by using `git branch -D` *`branch`*. However, in such situations, you will *lose* the changes in that branch, so tread carefully.

### Rebasing to avoid merge commits

In the previous section, we showed how to use `git merge` to merge two branches that had diverged (in other words, changes on both branches needed to be reconciled). In such cases, Git uses a merge commit to show that the two branches were brought together. However, merge commits are sometimes frowned upon; in 2021, Linus Torvalds took a Linux kernel contributor to task for what he called “useless merge commits.” Is there a way to avoid merge commits? Often, yes, and it involves something known as rebasing.

*Rebasing* is taking changes committed on one branch and replaying (applying) them to another branch. Let’s go back to the example from the previous section, where you made changes to both the sw4 and main branches. This could be illustrated as shown in [Figure 11-9](#beforerebasing).

![npa2 1109](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1109.png)

###### Figure 11-9. Divergent branches requiring a merge commit

However, rebasing the sw4 branch to include the changes from the main branch would change it to look like [Figure 11-10](#afterrebasing).

This sort of situation would allow you to use a fast-forward merge and avoid a merge commit, keeping a “cleaner” commit history.

![npa2 1110](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1110.png)

###### Figure 11-10. Divergent branches after rebasing can use a fast-forward merge

You can rebase a branch by using the `git rebase` command, which has the syntax `git rebase upstream`, where `upstream` is the name of the branch onto which the changes in the current branch should be replayed. In our example, if you wanted to avoid using a merge commit to merge the changes in the sw4 and main branches together, you’d first need to rebase sw4 on main:

```
ubuntu@ubuntu2004:~/net-auto$ git checkout sw4
Switched to branch 'sw4'
ubuntu@ubuntu2004:~/net-auto$ git branch
  main
* sw4
ubuntu@ubuntu2004:~/net-auto$ git rebase main
First, rewinding head to replay your work on top of it...
Applying: Update sw4 configuration
```

At this point, you could now merge sw4 into main with a fast-forward merge. We’ll leave that as an exercise for you. So, to recap:

- To create a branch, use `git branch` *`new branch name`*.
- To check out a branch, use `git checkout` *`branch`*.
- To create a new branch and check it out in one step, use `git checkout -b` *`new branch name`*.
- To merge a branch into main, run `git merge` *`branch`* while the main branch is checked out.
- To delete a branch after its changes have been merged, use `git branch -d` *`branch name`*.
- To rebase a branch, use `git rebase` *`upstream branch`*.

Let’s now turn our attention to using Git’s distributed nature to collaborate with others via Git.

# Collaborating with Git

As we discussed in [“Brief History of Git”](#brief-history-of-git), one of the key design goals for Git was that it was a fully distributed system. Thus, every developer needed to be able to work from a full copy of the source code stored in the repository as well as the repository’s full history. When you combine this fully distributed nature with Git’s other key design goals—​speed, simplicity, scalability, and strong support for nonlinear development via lightweight branches—​you can see why Git has become a leading option for users needing a collaborative version control system.

On its own, Git can act as a “server” and provides mechanisms for communications between systems running Git. Git supports a variety of transport protocols, including SSH, HTTPS, and Git’s own protocol (using TCP port 9418). If you’re simply using Git on a couple of systems and need to keep repositories in sync, you can do this with no additional software.

Further, Git’s distributed nature has enabled online services based on Git to appear. Many Git users take advantage of online Git-based services such as [GitHub](https://github.com) and [Bitbucket](https://bitbucket.org). A wide variety of open source projects facilitate collaboration via Git, such as [GitLab](https://about.gitlab.com), [Gitblit](https://gitblit.com), and [Djacket](https://djacket.github.io), which, somewhat ironically, is hosted on GitHub. As you can see, there’s no shortage of ways to collaborate with others by using Git and Git-based tools.

In this section, we explore how to collaborate using Git. That collaboration might be as simple as keeping repositories in sync on multiple systems, but we also cover using public Git-based services (focusing on GitHub). Along the way, you’ll learn about cloning repositories; Git remotes; pushing, fetching, and pulling changes from other repositories; and using branches when collaborating.

Let’s start with exploring a simple scenario involving multiple systems running Git, where you need to share/sync one or more repositories between these systems.

## Collaborating Between Multiple Systems Running Git

So far in this chapter, you’ve been building your collection of network configurations, scripts, and templates in a Git repository on a single system. What happens when you need or want to be able to access this repository from a separate system? Maybe you have a desktop system at work and a laptop that you use for travel and at home. How do you use your network automation repository from both systems? Fortunately, because of Git’s fully distributed design, this is pretty straightforward.

Can it be as simple as copying files? Let’s see what happens when you copy a repository and its working directory to a new location on the same system. First, run `git log --oneline HEAD~2..HEAD` in the existing repository:

```
ubuntu@ubuntu2004:~/net-auto$ git log --oneline HEAD~2..HEAD
829764b (HEAD -> main) Merge branch 'sw4' into main
53e3c45 Fix sw3 configuration for hypervisor
3ab27f8 Update sw4 configuration
```

Now, let’s copy the repository and working directory to a new location on the same system, run the same `git log` command, and see what you get:

```
ubuntu@ubuntu2004:~$ cp -ar net-auto netauto2
ubuntu@ubuntu2004:~$ cd netauto2
ubuntu@ubuntu2004:~/netauto2$ git log --oneline HEAD~2..HEAD
829764b (HEAD -> main) Merge branch 'sw4' into main
53e3c45 Fix sw3 configuration for hypervisor
3ab27f8 Update sw4 configuration
```

Looks like the contents are identical! If you were to continue to explore the contents of the repository at *~/netauto2* by using `git ls-tree`, `git cat-file`, or other commands, you’d find that the two repositories are, in fact, identical. Why is this? Recall that Git uses SHA-1 hashes to identify all content: blobs, tree objects, and commit objects. A key property of SHA-1 hashes is that *identical content produces identical hashes.* Recall also that the contents of the Git repository are immutable (once created, they can’t be modified). The combination of these attributes and Git’s architecture means that it’s possible to copy a repository by using simple tools like `cp` and end up with an intact version of the repository. It’s this ability to copy repositories—​with all data and metadata intact—​that is a key factor in Git’s fully distributed nature.

Note there’s no link between the copies, so changes made in one copy *won’t* be automatically reflected in the other copy, or vice versa. (You can verify this, if you’d like, by making a commit in either copy and then using `git log` in both repositories.) To create a link between copies, you need something known as a *remote*.

### Linking repositories with remotes

A Git *remote* is really nothing more than a reference to another repository. Git uses lightweight references pretty extensively—​you’ve seen this already in the use of branches and HEAD—​and in this case, remotes are similar. A remote is a lightweight reference to another repository, specified by a location.

Let’s add a remote to the *netauto2* repository that refers back to the original repository in *net-auto*. To do this, you use the `git remote` command:

```
admin@debian11:~/netauto2$ git remote
admin@debian11:~/netauto2$ git remote add first ~/net-auto
admin@debian11:~/netauto2$ git remote
first
```

When you use `git remote` with no parameters, it simply lists any existing remotes. In this case, there are none (yet). So you next run the `git remote add` command, which takes two parameters:

- The name of the remote repository. This name is purely symbolic—​it can be whatever makes sense to you. In this case, you use `first` as the name for the remote.
- The location of the remote repository. In this case, the remote repository is on the same system (for now), so the location is simply a filesystem path.

Finally, running `git remote` again shows that the new remote has been added.

With the remote in place, you now have an asymmetric link between the two remotes: *netauto2* has a reference to *net-auto*, but the reverse is *not* true. Via this asymmetric link, you can exchange information between Git repositories. Let’s see how this works.

First, let’s list the branches available in our *netauto2* repository. You’ll add the `-a` parameter here, which we’ll explain in more detail shortly:

```
vagrant@trusty:~/netauto2$ git branch -a
* main
```

Now, let’s fetch—​and we’re using the term *fetch* here intentionally, for reasons that will be evident later in this section—​information from the remote repository, which you configured earlier. You’ll update the information by using the `git remote update` command and then run `git branch -a` again:

```
admin@debian11:~/netauto2$ git remote update first
Fetching first
From /home/admin/net-auto
 * [new branch]      main     -> first/main
admin@debian11:~/netauto2$ git branch -a
* main
  remotes/first/main
```

Now a new branch is listed here. This is a special kind of branch known as a *remote tracking branch*. You won’t make changes or commits to this branch, as it is only a reference to the branch that exists in the remote repository. You’ll notice the `first` in the name of the branch; this refers to the symbolic name you gave the Git remote when you added it. You have to use the `-a` parameter to `git branch` in order to show remote tracking branches, which aren’t listed by default.

###### Tip

Instead of the two-step `git remote add` followed by `git remote update`, you can fetch information from a remote repository when you add the remote by using the syntax `git remote add -f name location`.

So what does this new remote tracking branch allow us to do? It allows us to *transfer* information between repositories in order to keep two repositories up-to-date. We’ll show you how this works in the next section.

### Fetching and merging information from remote repositories

Once a remote has been configured for a repository, information has been retrieved from the configured remote, and remote tracking branches have been created, it’s possible to start to transfer information between remotes by using various `git` commands. You could use these commands to keep branches of repositories or entire repositories in sync.

To see this in action, you’ll want to change one of the two repositories on your system (the *net-auto* repository) and see how to get that information into the *netauto2* repository.

First, in the *net-auto* repository, let’s make a change to the *sw2.txt* configuration file and commit that change to the repository. (We won’t go through all the steps here, as we’ve covered them previously. Need a hint? Edit the file, use `git add`, then `git commit`.)

Verify that you can see the new commit in the *net-auto* directory by using `git log --oneline HEAD~1..HEAD`; then switch to the *netauto2* repository and run the same `git log` command. The commit(s) listed will be different.

To get the updated information from *net-auto* over to *netauto2*, you have a few options:

- You can run `git remote update name`, which updates *only* the specified remote.
- You can run `git remote update` (without a remote’s name), which updates *all* remotes for this repository.
- You can run `git fetch name`, which will update (or *fetch*) information from the specified remote repository. In this respect, `git fetch` is a lot like `git remote update`, although the syntax is slightly different (again, we refer you to the man pages or the help screens for specific details). Note that `git fetch` is considered the conventional way of retrieving information from a remote, as opposed to using `git remote update` as we did earlier.

So, let’s run `git fetch first`, which will pull information from the repository named *first*. You’ll see output that looks something like this (the SHA-1 hashes will differ, of course):

```
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (2/2), 245 bytes | 245.00 KiB/s, done.
From /home/ubuntu/net-auto
   829764b..3267a4a  main       -> first/main
```

OK, so you’ve retrieved information from *first/main* (the main branch of the remote named *first*). Why, then, does `git log` in `netauto2` not show this? This is because you’ve only *fetched* (updated) the information from the remote repository; you haven’t actually made it part of the current repository.

###### Caution

We caution you against using the word “pull” when referring to simply retrieving information from a remote repository. In Git, the idea of “pulling” from a remote repository has a specific meaning and its own command (both of which we’ll discuss shortly). Try to train yourself to use “fetching” or “retrieving” when referring to the act of getting information from a remote repository.

So if you’ve only fetched the changes across but not made them a part of the current repository, how do you do that? The changes in the remote repository are stored in their own branch, which means they are kept separate from other branches of the current repository. How do you get changes from one branch to another branch? That’s right—​you *merge* the changes:

```
ubuntu@ubuntu2004:~/netauto2$ git checkout main
Already on 'main'
ubuntu@ubuntu2004:~/netauto2$ git merge first/main
Updating 829764b..3267a4a
Fast-forward
 sw2.txt | 7 +++++++
 1 file changed, 7 insertions(+)
```

As you can see from Git’s output, it has taken the changes applied to *first/main* (the main branch of the remote repository named *first*) and merged them—​via a fast-forward—​into the main branch of the current repository. Because this is a fast-forward, there will not be a merge commit, and now both repositories are in sync.

###### Note

If you noted that the use of `git fetch` and `git merge` on the main branch of two repositories doesn’t necessarily keep the repositories in sync, then you are *really* paying attention! In fact, only the main branches of the two repositories are in sync. To keep the entire repositories in sync, you’d need to perform this operation on all branches.

### Pulling information from remote repositories

Why the two-step process of first `git fetch` and then `git merge`? The primary reason is you might want to be able to review the changes from the remote repository *before* you merge them, in the event that you aren’t ready for those changes to be applied to the current repository.

As with so many things in Git, though, there is a shortcut. If you’d like to fetch changes and merge them in a single operation, you can use `git pull name`, where *`name`* is the name of the remote from which you’d like to get and merge changes into the current branch. The `git pull` command is simply combining the `git fetch` and `git merge` operations.

So you’ve seen how to get changes from *net-auto* to *netauto2*, but what about the reverse? We mentioned that adding a remote to *netauto2* is an asymmetric relationship in that *netauto2* now knows about *net-auto*, but the reverse is not true. In a situation such as we’ve described here—where you, as a single user, want to keep repositories in sync on separate systems—the best approach is to add a remote from *net-auto* to *netauto2*, and then use `git fetch` and `git merge` to move changes in either direction. Graphically, this looks something like [Figure 11-11](#twowayrepos).

![npa2 1111](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1111.png)

###### Figure 11-11. Using `git fetch` and `git merge` between repositories

###### Note

Git almost always offers multiple ways to do something, which can be both useful (in that it is very flexible) and frustrating (in that there’s no “one way” to do something). Two-way transfer of information between Git repositories as we’ve described in this section is one of these areas where there’s more than one way to get the job done. For new users of Git, this is probably the easiest way to handle it.

We started this section asking the question, “How do I use my network automation repository from multiple systems?” We’ve shown you how to make a copy of a repository, how to use Git remotes to link repositories, and how to use various Git commands to transfer data between repositories. In the next two sections, we’re going to show you a simpler, easier way of copying and linking repositories, and we’ll extend our working model across multiple systems, respectively.

### Cloning repositories

In the previous sections, we showed that you could simply copy a repository from one location to another and then use `git remote` to create a remote that would allow you to transfer information between repositories.

This process isn’t difficult, but what if there were an even easier way? There is, and it’s called *cloning* a repository via the `git clone` command. Let’s see how this works.

The general syntax of this command is `git clone repository directory`. In this command, *`repository`* is the location of the repository you’re cloning and *`directory`* is the (optional) directory where you’d like to place the cloned repository. If you omit *`directory`*, Git will place the cloned repository into a directory with the same name as the repository. Adding the *`directory`* parameter to the `git clone` command gives you some flexibility in where you’d like to place the cloned repository.

To illustrate how `git clone` works, let’s kill the *netauto2* repository. It shouldn’t have any changes in it, but if it does, you should know how to get those changes back into the original *net-auto* repository. Need a hint? Add a remote, fetch changes, and merge the changes:

```
ubuntu@ubuntu2004:~$ rm -rf netauto2
ubuntu@ubuntu2004:~$ git clone ~/net-auto na-clone
Cloning into 'na-clone'...
done.
ubuntu@ubuntu2004:~$ cd na-clone
ubuntu@ubuntu2004:~/na-clone$ git log --oneline HEAD~2..HEAD
3267a4a (HEAD -> main, origin/main, origin/HEAD) Update sw2 configuration
829764b Merge branch 'sw4' into main
3ab27f8 Update sw4 configuration
```

This example illustrates how `git clone` makes a copy of the repository, just as you did manually in the previous section. There’s more, though—​now run `git remote` in this new cloned repository:

```
ubuntu@ubuntu2004:~/na-clone$ git remote
origin
```

Here’s the advantage of using `git clone` over the manual steps we showed you earlier—it *automatically* creates a remote pointing back to the original repository from which this repository was cloned. Further, it *automatically* creates remote tracking branches for you (you can verify this by using `git branch -a` or `git branch -r`). Because it handles these extra steps for you, `git clone` should be your preferred mechanism for cloning a repository.

Before we move on, let’s talk a bit about the `origin` remote that was automatically created by `git clone`. While the name of a remote is strictly symbolic, origin does have special significance for Git. You can think of it as a default remote name. When you have multiple remotes (yes, this is definitely possible!) and you run a `git fetch` without specifying a remote, Git will default to origin. Aside from this behavior, though, no special attributes are given to the remote named origin.

As an example of using multiple remotes, this book was written using Git and multiple Git remotes. One Git remote was GitHub; the other was O’Reilly’s repository. Here’s the output of `git remote -v` from one author’s repository:

```
oreilly     git@git.atlas.oreilly.com:oreillymedia/network-automation.git (fetch)
oreilly     git@git.atlas.oreilly.com:oreillymedia/network-automation.git (push)
origin      https://github.com/jedelman8/network-automation-book.git (fetch)
origin      https://github.com/jedelman8/network-automation-book.git (fetch)
```

Now we’re finally ready to tackle the last step, which is taking everything you’ve learned so far and applying it to extend our Git working model with repositories across multiple systems.

### Extending our working model across multiple systems

When we discussed the idea of creating a Git remote (see [“Linking repositories with remotes”](#linking_repositories_with_remotes)), we said that a remote has two attributes: the name (symbolic in nature) and the location. So far, you’ve seen only remotes on the same system, but Git natively supports remotes on *different* systems across a variety of protocols.

For example, a remote on the same system uses a location like this:

```
/path/to/git/repository
file:///path/to/git/repository
```

However, a remote could also use various network protocols to reach a repository on a separate system:

```
git://host.domain.com/path/to/git/repository
ssh:/[user@]host.domain.com/path/to/git/repository
http://host.domain.com/path/to/git/repository
https://host.domain.com/path/to/git/repository
```

The `git://` syntax references Git’s native protocol, which is unauthenticated and therefore used for anonymous access (generally read-only access). The `ssh://` syntax refers to Secure Shell; this is actually Git’s protocol tunneled over SSH for authenticated access. Finally, you have HTTP and HTTPS variants as well.

This means that you could take the working model we’ve described throughout this section and *easily* extend it to multiple systems, using whatever network protocol best suits your needs. In this section, we focus on the use of SSH, and later in this chapter we’ll show you examples of using HTTPS with public Git hosting services.

Going back to our example, let’s say you need to be able to work on your network automation repository from both your desktop system and a laptop that you take with you. Let’s assume that both systems support SSH (i.e., they are running Linux, macOS, or some other Unix variant). The first step is to configure passwordless authentication for SSH, generally using SSH keys. This will allow the various `git` commands to work without prompting for a password. Configuring SSH falls outside the scope of this book, but it’s well documented online.

The next step is then to create the necessary Git remotes. The repository already exists on your desktop (for the purposes of this example, we’ll use our Ubuntu 20.04.3 Focal Fossa system to represent your desktop), but it doesn’t exist on your laptop (which we’ll represent with our Debian 11 Bullseye system). So, you need to clone the repository over to the laptop:

```
admin@debian11:~$ git clone ssh://ubuntu/~/net-auto net-auto
Cloning into 'net-auto'...
remote: Counting objects: 32, done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 32 (delta 12), reused 0 (delta 0)
Receiving objects: 100% (32/32), 2.99 KiB | 0 bytes/s, done.
Resolving deltas: 100% (12/12), done.
Checking connectivity... done.
```

This copies the repository from your desktop (*ubuntu*, defined using an SSH configuration file) to your laptop (placing it in the directory specified; in this case, *net-auto*), creates a Git remote named origin pointing back to the original, and creates remote tracking branches. You can verify all this by using `git remote` to see the remote and `git branch -r` to see remote tracking branches.

If you prefer to have a remote name that more clearly identifies where the remote is found, you can rename the remote from the default name, origin. Let’s rename the remote to reflect that it’s coming from our desktop system:

```
admin@debian11:~/net-auto$ git remote
origin
admin@debian11:~/net-auto$ git remote rename origin desktop
admin@debian11:~/net-auto$ git remote
desktop
```

Now, back on the Ubuntu system, you need to create a remote to the repository on the Debian laptop. The repository already exists here, so you can’t use `git clone`; instead, you need to add the remote manually and then fetch information from the remote to create the remote tracking branches:

```
ubuntu@ubuntu2004:~/net-auto$ git remote add laptop ssh://debian11/~/net-auto
ubuntu@ubuntu2004:~/net-auto$ git remote
laptop
ubuntu@ubuntu2004:~$ git fetch laptop
From ssh://debian11/~/net-auto
 * [new branch]      main     -> laptop/main
ubuntu@ubuntu2004:~/net-auto$ git branch -r
  laptop/main
```

Great—​now you have the repository on both systems, a remote on each system pointing back to the other, and remote tracking branches created on each side. From here, the workflow is exactly as we described in earlier sections:

1. Make changes on either system (not both at the same time!) and commit those changes to the repository. Ideally, you should work *exclusively* in branches other than the main branch.
2. When you get back to the other system, run a `git fetch` and `git merge` to fetch and merge changes from remote branches into local branches. (If you don’t care to review the changes before merging, you can use `git pull`.) Be sure to do this *before* you get started working!
3. Repeat as needed to keep branches on both systems up-to-date with each other.

With regard to using `git pull` to fetch and merge from a remote repository in a single step, there may be a configuration setting you need to turn on. Newer versions of Git ask the user to reconcile divergent branches, as shown in this output in response to running `git pull`:

```
admin@debian11:~/na-shared$ git pull origin main
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint:
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
```

We touched on rebasing briefly earlier in [“Rebasing to avoid merge commits”](#rebasing), but there is a lot more to rebasing. However, it is well documented online. For now, it’s probably safe to go ahead and run `git config pull.rebase false`, which is noted in the preceding hint as the default strategy.

The approach we’ve shown you so far works fairly well for a single developer on two systems, but what about more than one developer? While it’s possible to build a full mesh of Git remotes and remote tracking branches, this can quickly become unwieldy. Using a shared repository in cases like this greatly simplifies using Git across multiple systems.

### Using a shared repository

If you’ve been poking around Git remotes with the `git remote` command, you may have discovered the `-v` switch, which enables more verbose output. For example, running `git remote -v` from one of the two systems configured in the previous section shows this:

```
admin@debian11:~/na-shared$ git remote -v
desktop  ssh://ubuntu/~/net-auto (fetch)
desktop  ssh://ubuntu/~/net-auto (push)
```

This is useful, as it shows the full location of the remote repository. We’ve discussed the use of `git fetch` to retrieve information from the remote repository, but what’s this `push`?

So far we’ve discussed only retrieving information from a remote repository to your local repository through the use of commands like `git remote update`, `git fetch`, and `git pull`. It is possible, though, to send (Git uses the term *push*) changes to a remote repository from your local repository. However, in such cases, it is strongly recommended that the remote repository should be a bare repository.

What is a bare repository? Put simply, a *bare repository* is a Git repository without a working directory. (Recall that *working directory* has a specific definition in Git and shouldn’t be taken to mean the same as the *current directory*.) All the discussions of Git repositories so far have assumed the presence of a working directory, because someone—​a user like you—​was going to be working on the repository. You, as the user of the repository, needed a way of interacting with the content in the repository, and the working directory was the way Git provided that method of interaction.

The reason you are strongly recommended against pushing to a nonbare repository (a repository with a working directory) is that a push doesn’t reset the working directory. Let’s go back to our previous example—​two systems configured with remotes and remote tracking branches pointing to the other system—​and see how this might cause problems:

1. Let’s say you’re being a really good Git citizen and working from a branch. We’ll call this branch *new-feature*. You’ve got new-feature checked out on your first system, so it’s the contents of the new-feature branch that are in the working directory. As the day ends, you still have a few unfinished changes left in the working directory, but you commit a few other changes.
2. From your second system, you fetch the changes, review them, merge them into the local new-feature branch, and continue working. You know that you can’t see the uncommitted changes in the working directory on your first system, but that’s no problem. All is well so far.
3. It’s the end of the evening now, and you’ve just completed some work. You decide to push your changes to your work system’s new-feature branch.
4. The next day, you come into work and decide to get started. Your uncommitted changes are still in the working directory, but you don’t see the changes you pushed last night. What’s going on here?

This is the issue with pushing to a nonbare repository: the changes were pushed to the remote repository, but the working directory was not updated. That’s why you can’t see the changes. To be able to see the changes, you’ll have to run `git reset --hard HEAD`, which will *throw away* the changes in the working directory in order to show the pushed changes. Not a good situation, right?

Using a bare repository eliminates these problems but also eliminates the possibility of being able to interactively work with the repository. This is probably perfectly fine for a shared repository being used by multiple developers, though.

To create a new, bare repository, simply add the `--bare` option to `git init`:

```
[ec2-user@amazonlinux2 ~]$ git init --bare shared-repo.git
Initialized empty Git repository in /home/ec2-user/shared-repo.git/
[ec2-user@amazonlinux2 ~]$ git init non-bare-repo
Initialized empty Git repository in /home/ec2-user/non-bare-repo/.git/
```

Note the difference in the output of Git when `--bare` is used and when it is not used. In a non-bare repository, the actual Git repository is in the *.git* subdirectory, and Git’s response indicates this. In a bare repository, though, there’s no working directory, so the Git repository sits *directly* at the root of the directory specified.

###### Note

Although not required, it is accepted convention to end the name of a bare repository in *.git*.

In this case, you have an *existing* repository, and you need to somehow transition that into a bare repository that you can now share among multiple users. Git is prepared for such a scenario: you can use `git clone` to clone an existing repository into a new bare repository:

```
ubuntu@ubuntu2004:~$ git clone --bare net-auto na-shared.git
Cloning into bare repository 'na-shared.git'...
done.
```

When you use `git clone --bare`, Git does not add any remotes or remote tracking branches. This makes sense if you think about it; generally, remotes and remote tracking branches are useful only when you are directly interacting with the repository. With a bare repository, you aren’t interacting directly; you’ll use a clone on another system, which will have remotes and remote tracking branches.

Let’s take our two-system setup (with the repository on the Ubuntu desktop system and the Debian laptop system and remotes pointing back to each other) and transition it into a shared, bare repository on a third system. We’ll introduce our third system, a system running Amazon Linux 2 (AL2), to serve as the shared repository.

First, you need to get the repository onto the AL2 system. Here’s where `git clone --bare` comes into play:

```
[ec2-user@amazonlinux2 ~]$ git clone --bare ssh://ubuntu/~/net-auto
na-shared.git
Cloning into bare repository 'na-shared.git'...
remote: Counting objects: 32, done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (32/32), done.
remote: Total 32 (delta 12), reused 0 (delta 0)
Resolving deltas: 100% (12/12), done.
```

Now you can clone this bare repository onto your two work systems. First, the Ubuntu desktop system:

```
ubuntu@ubuntu2004:~$ git clone ssh://amzn2/~/na-shared.git
na-shared
Cloning into 'na-shared'...
remote: Counting objects: 32, done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 32 (delta 12), reused 32 (delta 12)
Receiving objects: 100% (32/32), done.
Resolving deltas: 100% (12/12), done.
Checking connectivity... done.
ubuntu@ubuntu2004:~$ cd na-shared
ubuntu@ubuntu2004:~/na-shared$ git remote -v
origin  ssh://amzn2/~/na-shared.git (fetch)
origin  ssh://amzn2/~/na-shared.git (push)
ubuntu@ubuntu2004:~/na-shared$ git branch -r
  origin/HEAD -> origin/main
  origin/main
ubuntu@ubuntu2004:~/na-shared$ git log --oneline HEAD~2..HEAD
3267a4a (HEAD -> main, origin/main, origin/HEAD) Update sw2 configuration
829764b Merge branch 'sw4' into main
3ab27f8 Update sw4 configuration
```

You can see that the `git clone` into the bare repository and subsequently back down to your Ubuntu system preserves all the data and metadata in the repository, and automatically creates Git remotes and remote tracking branches. (You can verify the Git history, if you’d like, by running `git log` in the new `na-shared` repository as well as in the old `net-auto` repository still on your system.)

Next, you perform the same steps on the Debian laptop system:

```
admin@debian11:~$ git clone ssh://amzn2/~/na-shared.git
na-shared
Cloning into 'na-shared'...
remote: Counting objects: 32, done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 32 (delta 12), reused 32 (delta 12)
Receiving objects: 100% (32/32), done.
Resolving deltas: 100% (12/12), done.
Checking connectivity... done.
admin@debian11:~$ cd na-shared
admin@debian11:~/na-shared$ git remote -v
origin  ssh://amzn2/~/na-shared.git (fetch)
origin  ssh://amzn2/~/na-shared.git (push)
admin@debian11:~/na-shared$ git branch -r
  origin/HEAD -> origin/main
  origin/main
```

Now that you have the new *na-shared* repository on all your systems, you can simply remove the old *net-auto* repository with `rm -rf net-auto`.

What does the workflow look like now?

1. You’ll still want to work almost exclusively in branches other than the main branch. This becomes particularly important when working with other users in the same shared repository.
2. Before starting work on the local clone on any system, run `git fetch` to retrieve any changes present on the shared repository but not in your local clone. Merge the changes into local branches as needed with `git merge`.
3. Make changes in the local repository and commit them to your local clone.
4. Push the changes up to the shared repository by using `git push`.

We’ve mentioned pushing changes a few times in this chapter, but this probably warrants additional explanation. To that end, let’s dive into the `git push` command to see this concept in action.

### Pushing changes to a shared repository

Now that you have a bare repository, you can push changes to the remote by using `git push`. The general syntax is `git push remote branch`, where *`remote`* is the name of the Git remote, and *`branch`* is the name of the branch to which these changes should be pushed.

To illustrate this in action, let’s make changes to the network automation repository on our Debian system. You’ll add a Jinja template, *hv-tor-config.j2*, that represents the base configuration for a ToR switch to which hypervisors are connected.

First, because you don’t want to work off the main branch, you create a new branch to hold your changes:

```
admin@debian11:~/na-shared$ git checkout -b add-sw-tmpl
Switched to a new branch 'add-sw-tmpl'
```

After you add the file to the working directory (by creating it from scratch or by copying it from elsewhere), you stage and commit the changes:

```
admin@debian11:~/na-shared$ git add hv-tor-config.j2
admin@debian11:~/na-shared$ git commit -m "Add Jinja template for TOR config"
[add-sw-tmpl 8cbbe6f] Add Jinja template for TOR config
 1 file changed, 15 insertions(+)
 create mode 100644 hv-tor-config.j2
```

Now, you push the changes to the origin remote, which points to our shared (bare) repository on the AL2 system:

```
admin@debian11:~/na-shared$ git push origin add-sw-tmpl
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 426 bytes | 426.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
To ssh://amzn2/~/na-shared.git
 * [new branch]      add-sw-tmpl -> add-sw-tmpl
```

This allows coworkers and others with whom you are collaborating to then fetch the changes on their systems. They would just use `git fetch` to retrieve the changes, make a local branch corresponding to the remote tracking branch, and then review the changes by using whatever methods they wanted. Here, we’ll show `git diff`, which isn’t terribly useful considering the only change is adding a single new file:

```
ubuntu@ubuntu2004:~/na-shared$ git fetch origin
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 406 bytes | 406.00 KiB/s, done.
From ssh://amzn2/~/na-shared
 * [new branch]      add-sw-tmpl -> origin/add-sw-tmpl
ubuntu@ubuntu2004:~/na-shared$ git checkout --track -b add-sw-tmpl origin/add-sw-tmpl
Branch add-sw-tmpl set up to track remote branch add-sw-tmpl from origin.
Switched to a new branch 'add-sw-tmpl'
ubuntu@ubuntu2004:~/na-shared$ git diff main..HEAD
diff --git a/hv-tor-config.j2 b/hv-tor-config.j2
new file mode 100644
index 0000000..8de9181
--- /dev/null
+++ b/hv-tor-config.j2
@@ -0,0 +1,13 @@
+interface ethernet0
+  description Mgmt interface for hypervisor
+  switchport mode access
+  switchport mode access vlan {{ mgmt_vlan_id }}
+
+interface ethernet1
+  switchport mode {{ modeSelection }}
+
+interface ethernet2
+  switchport mode {{ modeSelection }}
+
+interface ethernet3
+  switchport mode {{ modeSelection }}
+
```

Once everyone agrees that the changes are OK, you can merge the changes into the main branch. First, perform the merge locally:

```
admin@debian11:~/na-shared$ git checkout main
Switched to branch 'main'
Your branch is up-to-date with 'origin/main'
admin@debian11:~/na-shared$ git merge add-sw-tmpl
Updating 3267a4a..01616d1
Fast-forward
 hv-tor-config.j2 | 13 +++++++++++++
 1 file changed, 13 insertions(+)
 create mode 100644 hv-tor-config.j2
```

This a fast-forward, so there’s no commit merge. Now push the changes to the shared repository:

```
admin@debian11:~/na-shared$ git push origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To ssh://amzn2/~/na-shared.git
   3267a4a..01616d1  main -> main
```

Finally, delete your branch (also frequently referred to as a *feature branch* or a *topic branch*) and push that change to the shared repository:

```
admin@debian11:~/na-shared$ git branch -d add-sw-tmpl
Deleted branch add-sw-tmpl (was 01616d1).
admin@debian11:~/na-shared$ git push origin --delete add-sw-tmpl
To ssh://amzn2/~/na-shared.git
 - [deleted]         add-sw-tmpl
```

Your collaborators can then get the changes that were merged into the main branch, delete the local branch they created, and then delete the remote tracking branch that is no longer needed by using the `git fetch --prune` command:

```
ubuntu@ubuntu2004:~/na-shared$ git pull origin main
From ssh://amzn2/~/na-shared
 * branch            main       -> FETCH_HEAD
   3267a4a..01616d1  main       -> origin/main
Updating 3267a4a..01616d1
Fast-forward
 hv-tor-config.j2 | 13 +++++++++++++
 1 file changed, 13 insertions(+)
 create mode 100644 hv-tor-config.j2
ubuntu@ubuntu2004:~/na-shared$ git fetch --prune origin
From ssh://amzn2/~/na-shared
 - [deleted]         (none)     -> origin/add-sw-tmpl
ubuntu@ubuntu2004:~/na-shared$ git branch -d add-sw-tmpl
Deleted branch add-sw-tmpl (was 01616d1).
```

The `git fetch --prune` command is new; it’s used to delete a remote tracking branch when the branch no longer exists on the remote. In this particular case, you’re removing the remote tracking branch for *origin/add-sw-tmpl*, as noted in the output of the command.

###### Note

We know that all this may sound complicated if you’re new to Git. It’s OK—​everyone was new to Git at some point (except maybe Linus). Take it slow and be patient with yourself. After a little while of using Git, the commands will start to feel more natural. Until then, you might find it handy to have a Git cheat sheet nearby to remind you of some of the commands and their syntax.

Before we move on to our final topic—​collaborating using Git-based online services—​let’s recap what we’ve discussed in this section:

- Git uses *remotes* to create links between repositories. You’ll use the `git remote` command to manipulate remotes. A remote can point to a filesystem location as well as to a location across the network, such as another system via SSH.
- To retrieve changes from a remote repository into your local repository, use `git fetch` *`remote`*.
- Git relies heavily on branches when working with remote repositories. Special branches known as *remote tracking branches* are automatically created when you use `git fetch` to retrieve changes.
- Changes retrieved from a remote repository can be merged into your local repository just like any other branch merge by using `git merge`.
- If you don’t want to follow the two-step `git fetch` followed by `git merge`, you can use `git pull`.
- You’ll use `git push` to push changes to a remote repository, but this remote repository should be a bare repository.
- Using a bare repository as a central, shared repository can enable multiple users to collaborate on a single repository. Changes are exchanged via branches and through the use of `git push`, `git fetch`, `git merge`, and `git pull`.

Our last section in this chapter builds on everything we’ve shown you so far and focuses on using Git-based online services to collaborate with other users.

## Collaborating via Git-Based Online Services

Fundamentally, collaborating with other users by using a Git-based online service will look and feel much like what we described in the previous section. All the same concepts apply—​using clones to make copies of repositories, using remotes and remote tracking branches, and working in branches to exchange changes with other users in the same repository. You’ll even continue to use the same commands: `git fetch`, `git push`, `git merge`, and `git pull`.

All that being said, we’d like to cover a few differences. For the sake of brevity, we focus on the use of GitHub as our Git-based online service for collaborating. The topics covered in this section are as follows:

- Forking repositories
- Pull requests

Ready? Let’s start with forking repositories.

### Forking repositories

*Forking* a GitHub project is essentially the same as *cloning* a Git repository. (We use the terms *project* and *repository* somewhat interchangeably in this section.) When you fork a GitHub repository, you are issuing a command to GitHub’s servers to clone the repository into your user account. At the time of creation, your fork will be a full and complete copy of the original repository, including all the content and the commit history. Once the repository has been forked into your account, it’s just as if you’d issued a `git clone` from the command line—​links are maintained back to the original project, much like a Git remote. (These remotes are not exposed to the user, though.) The key difference here is that forking a repository on GitHub does *not* create a local copy of the repository; you’ll still need to use `git clone` to clone the forked copy down to your local system, as we’ll show you shortly.

So why fork a repository? In the case of a large online service such as GitHub, hundreds of thousands of repositories are hosted there. Each repository is associated with a GitHub user ID, and that user ID is allowed to control who may or may not contribute to the repository.

What if you find a repository to which you want to contribute? The owner of that repository may not know you (a likely situation) and may not trust your ability to contribute to their repository. However, if you had your own copy of the repository, you could make the contributions you wanted to make and then let the owner of the original decide if such contributions were worthwhile.

So, instead of trying to get approval to contribute directly to a repository, you instead *fork* (clone) the repository to your own account, where you can work with it. At some point later, you can (optionally) see if the original repository wants to include your changes moving forward (we discuss this in [“Creating pull requests”](#pull_requests)).

To fork a GitHub repository, just follow these steps:

1. Log into GitHub, using your security credentials.
2. Locate the repository you’d like to fork into your own account and then click the Fork button in the upper-right corner of the screen.
3. If you are a member of any GitHub organizations, you may be prompted for the user account or organization where you’d like this repository to be forked. Choose your own user account unless you know you need a different option.

That’s it! GitHub will fork (clone) the repository into your user account.

Because GitHub repositories are bare repositories, you generally need to then clone this bare repository down to your local system to work with it. (GitHub provides web-based tools to create files, edit files, make commits, and similar.) To clone a GitHub repository out of your account, you just use the `git clone` command, followed by the URL of the GitHub repository. For example, here’s the URL of one of the author’s GitHub repositories: [*https://github.com/scottslowe/learning-tools.git*](https://github.com/scottslowe/learning-tools.git).

Let’s say your GitHub username is npabook (this user did not exist at the time of this writing). If you were to fork the preceding repository, it would make a full and complete copy of the repository into your user account, just as if you’d used `git clone`. At this point, the URL for your forked repository would be [*https://github.com/npabook/learning-tools.git*](https://github.com/npabook/learning-tools.git).

If you ran `git clone https://github.com/npabook/learning-tools.git` from your local system, Git would clone the repository down to your local system, create a remote named origin that points back to your forked repository on GitHub, and create remote tracking branches—​just as `git clone` worked in our earlier examples.

Once you have a clone of the repository on your local system, working with your forked GitHub repository is *exactly* as we described in the previous section:

1. Create new feature/topic branches locally to isolate changes away from the main branch.
2. Use `git push` to push those changes to the remote GitHub repository.
3. Merge the changes into the main branch via `git merge` whenever you’re ready.
4. Use `git fetch` followed by `git merge` to pull down the changes to the main branch, or combine those steps by using `git pull`.
5. Delete the local feature/topic branch and the remote branch on the GitHub repository.

So far, this should all seem pretty straightforward—​we haven’t really shown anything different from what we described earlier. One situation, though, requires some discussion: how do you keep your fork in sync with the original?

### Keeping forked repositories in sync

Although GitHub maintains links back to the original repository when you fork it into your user account, GitHub does not provide a way to keep the two repositories synchronized. Why is it important to keep your fork synchronized with the original? Suppose you want to contribute to an ongoing project. Over time, your forked copy will fall hopelessly behind the original as development continues, branches are merged, and changes committed to the original. To be able to contribute useful changes, you need your fork to be up-to-date with the original.

To keep your forked repository up-to-date, you use multiple remotes. (We did say earlier that multiple remotes are definitely something you might need to use with Git.) Let’s walk through how this works. We’ll assume you’ve already forked the repository in GitHub.

First, clone the forked repository down to your system by using `git clone`. The command looks something like this:

```
git clone https://username@github.com/username/repository-name.git
```

This clones the repository down to your local system, creates a remote named origin that points back to the URL specified before, and creates remote tracking branches. At this point, if you run `git remote` in this repository, you’ll see a single remote named origin (remember that `git remote -v` will also show the location of the remote—​in this case, the HTTPS URL).

Next, add a *second* remote that points to the original repository. The command looks something like this:

```
git remote upstream add https://github.com/original-user/repository-name.git
```

The name `upstream` here is strictly symbolic, but we like to use it as this reminds us that the remote points to the upstream (or original) project. (We’ve also found that `upstream` is commonly used, so it may make sense to use the same remote name that others use for consistency.) Your local repository now has two remotes: origin, which points to your forked repository, and upstream, which points to the original repository.

Now, follow these steps to keep your repository up-to-date with the original (all these steps are taken from within the cloned Git repository on your local system):

1. Check out the main branch via `git checkout main`.
2. Get the changes from the original repository. You can use a combination of `git fetch upstream main` followed by `git merge upstream/main`, or you can use `git pull upstream main` (which combines the steps). Your local, cloned repository is now in sync with the original repository.
3. Push the changes from your local repository to the forked repository, using `git push origin main`. Now your forked repository is up-to-date with the original.

This process doesn’t keep any feature/topic branches up-to-date, but that’s generally not a problem—most of the time, you’ll want to keep main synchronized only between the original and the forked repository. If you do want to keep a different branch up-to-date between the original repository and your fork, substitute the correct branch name for the commands in the preceding list. The process is the same.

In the next section, you’ll learn how to let the owner of a repository know that you have changes you’d like them to consider including in their repository.

### Creating pull requests

Let’s quickly recap the recommended process for working with a shared repository such as that offered by GitHub:

1. Create a local branch—called a *feature* or *topic* branch—in which to store the changes you’re going to make.
2. Stage and commit the changes to the new local branch.
3. Push the local branch to the remote repository via `git push` *`remote branch`*.

That gets the changes into your forked repository, but how does the owner of the original repository know that you’ve pushed changes up to your forked copy? In short: they *don’t.* Why? Well, for one, it’s entirely possible that you are truly forking—creating a divergent codebase—and don’t want or need the original author(s) to know about your changes. Second, what if the changes you commit don’t include *all* the changes you want the original authors to consider? How would Git or GitHub know when you are ready? In short: it *can’t*. Only you can know when your code is ready for the original authors to review for inclusion, and that’s the purpose of a pull request.

A *pull request* is a notification to the authors of the original repository that you have changes you’d like them to consider including in their repository. Creating a pull request comes after step 3 in the preceding list. Once you’ve pushed your changes into a branch in your forked repository, you can create a pull request against the original repository. (Note that other Git-based platforms, such as GitLab, may use terms like *merge request* instead of pull request. The basic idea and workflow are much the same.)

To create a pull request after pushing a branch up to GitHub, go to the original repository. Just under the line listing the commits, branches, releases, and contributors, a new line will appear with a button labeled “Compare & pull request.” This is illustrated in [Figure 11-12](#githubpr).

![npa2 1112](/api/v2/epubs/urn:orm:book:9781098110826/files/assets/npa2_1112.png)

###### Figure 11-12. Creating a new pull request in GitHub

Click that button, and GitHub will open a screen to create the pull request. The base fork, base branch, head fork, and comparison branch will all be automatically filled in for you, and the notes in the pull request will be taken from the last commit message. Make any changes as needed; then click the green “Create pull request” button.

The owners of the original repository then have to decide if the changes found in your branch can and should be merged into their repository. If they agree—or if you are the one receiving the pull request—then you can merge the changes in GitHub’s web interface.

Once the changes have been merged into the original repository, you can update your fork’s main branch from the original (using `git fetch` and `git merge`, or the one-step `git pull`). Since the changes from your feature/topic branch are now found in the main branch, you can then delete the branch (as well as any remote tracking branches for your forked repository), as it is no longer needed.

As you can see, aside from a few minor differences, the general workflow for collaborating via GitHub is very similar to the workflow for collaborating using only a shared (bare) repository. By and large, the same terms, concepts, and commands are used in both cases, which makes it easier for you to collaborate with others using Git.

# Summary

In this chapter, we’ve provided an introduction to Git, a widely used version control system. Git is a fully distributed version control system that provides strong support for nonlinear development with branches. Like other version control systems, Git offers accountability (who made what changes) and change tracking (knowing the changes that were made). These attributes are just as applicable in networking-centric use cases as they are in developer-centric use cases. Branches are a key part of collaborating with Git. To help with Git collaboration, online services (such as GitHub and Bitbucket) have appeared, allowing users across organizations to collaborate on repositories with relative ease.
