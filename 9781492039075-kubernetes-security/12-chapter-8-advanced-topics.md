# Chapter 8. Advanced Topics

This chapter covers a collection of crosscutting topics related to making your Kubernetes cluster and its applications more secure. We’ll build on the topics discussed in the previous chapters and sometimes go beyond Kubernetes proper (for example, with monitoring or service meshes).

###### Tip

Many of the ideas in this chapter are evolving and under discussion within the Kubernetes community. We welcome involvement from end users as well as those contributing to the development of cloud native projects themselves. If you’re not already involved, there is a list of different ways to get involved; the [Community](https://kubernetes.io/community/) section of the Kubernetes website provides a list of ways to get involved, from mailing lists and Slack channels to in-person events.

# Monitoring, Alerting, and Auditing

The community seems to be standardizing on [Prometheus](https://prometheus.io) for monitoring Kubernetes clusters, so a good start is to familiarize yourself with it. Since there are so many moving parts (from nodes to pods to services), alerting on each event is not practical. What you can do, however, is think about who needs to be informed about what kind of event. For example, a policy could be that node-related or namespace-related events are handled by admins, and developers are paged for pod-level events. The same applies more or less for logs, but here you also should be aware of where and when your sensitive data lands on disk; see [Chapter 7](ch07.html#ch_secrets) for details.

Another useful feature Kubernetes offers via the API server is [auditing](http://bit.ly/2O4WBkL), effectively recording the sequence of activities affecting the cluster. Different strategies are available in the auditing policy (from no logging to logging event metadata, request and response bodies), and you can choose between a simple log backend as well as using a webhook for integrating with third-party systems.

# Host Security

Much discussion of Kubernetes security focuses on the setup of Kubernetes itself, or on securing the containerized applications that run within it. There is another layer to be secured: the host machines on which Kubernetes runs.

Whether they are bare-metal or VMs, there are many steps you can take to restrict access to your hosts that are essentially the same as you would take in a traditional cluster. For example, you should, of course, restrict access to the machines, and you might well configure them to use a dedicated VPN. These general machine security measures are outside the scope of this book, but there are some specific things you would do well to consider when you are running Kubernetes (or any container orchestrator). Resources such as [OpenSCAP](https://www.open-scap.org/tools/) and [OVAL](https://oval.mitre.org/index.html) can help with a broader security assessment.

## Host Operating System

The host machines need to be able to run only the Kubernetes code, its dependencies (a runtime system like Docker), and supporting features like logging or security tools. Following the principle of reducing the attack surface, a best-practice setup would have *only* the necessary code and no superfluous libraries or binaries. This is sometimes referred to as a *thin OS*.

Container-specific distributions like [Container Linux](https://coreos.com/os/docs/latest/) from CoreOS (now part of Red Hat), [RancherOS](https://rancher.com/rancher-os/), or Red Hat’s own [Atomic](https://red.ht/2MYylff) are one approach to minimizing the amount of code installed on your host machines. These can also include other security features like a read-only root filesystem. A general-purpose Linux distribution is also fine, but it’s worth checking that you’re not using a machine image with extra libraries and tools installed (particularly if, out of habit, you are using the same machine image you have used in a traditional deployment).

## Node Recycling

In a cloud-native deployment, we treat nodes as [“cattle not pets,”](http://bit.ly/2ztNLot) and it should be trivially easy to create a new node or replace a faulty one, as it should be automated through an [infrastructure as code](http://bit.ly/2zE2E7L) approach. This enables node recycling, where you tear down and replace your nodes on a regular (or random) schedule.

When you recycle a node, you know that it has been returned to the desired state, as determined by your infrastructure as code. If there has been any “drift”—for example, because an undetected attacker got a foothold into the system—that drift is removed.

Another benefit of recycling your nodes (especially for small or new deployments) is that it’s effectively a fire drill. If you are frequently replacing nodes as a matter of course, you can have more confidence in the system’s ability to cope through node failure. It’s a baby step toward [chaos engineering](https://principlesofchaos.org/)!

# Sandboxing and Runtime Protection

[*Sandboxing*](http://bit.ly/2NGLvTy) is the ability to isolate containers from each other and from the underlying host, so that code running within one container can’t effect change outside that container.

*Runtime protection* is the concept of limiting the set of code that can be executed within the container itself. If attackers can access a container, but can’t execute their own code within it, the potential damage is limited.

While the end goal of these two concepts is different, some overlap exists in the mechanisms used to achieve them. For example, seccomp or AppArmor profiles can limit a container to have access to a limited set of system calls. This restricts what the container can do (runtime protection) and increases its isolation by giving it less access to the kernel (sandboxing).

Containers share the host’s kernel, so vulnerabilities in the kernel could conceivably allow an exploit to escape one container and move to another or to the host.

At time of writing, several projects and vendors are aimed at improving sandboxing and/or runtime protection, all with their own strengths and characteristics:

- [seccomp](https://en.wikipedia.org/wiki/Seccomp) is a kernel mechanism for limiting the system calls that application code can make. A `securityContext` or `PodSecurityPolicy` can specify the seccomp profile.
- [AppArmor](https://en.wikipedia.org/wiki/Apparmor) and [SELinux](https://en.wikipedia.org/wiki/SELinux) are kernel security modules, also configurable through profiles attached to `securityContext` or `PodSecurityPolicy` in Kubernetes.
- [Kata Containers](https://katacontainers.io/) run each application inside a “lightweight” VM (so each has its own kernel).
- Google’s [gVisor](https://github.com/google/gvisor) project runs container code in a sandbox through a kernel API implemented in user space (if that’s not a contradiction in terms).
- [Nabla containers](https://nabla-containers.github.io/) use unikernel technology to provide isolation and limit access to the shared kernel.
- Enterprise container security solutions such as those from Aqua Security and Twistlock use regular containers, with proprietary runtime protection technology that includes whitelisting/blacklisting the set of executables that can run in a given container.

# Multitenancy

In some deployments, multiple “tenants” using the same cluster don’t fully trust each other or might not be trusted by the cluster operator. Tenants could be users, groups of users, or applications. The level of trust between users depends on the environment; for example, in a platform-as-a-service (PaaS) environment where users can upload and run their own applications, they should be treated as entirely untrusted, whereas in an enterprise, the tenants might map to different organizational teams, who do cooperate and trust each other to some extent, but who want to limit the risk of someone outside one team maliciously or inadvertently affecting another team’s application.

Multitenant isolation has two parts:

- The control plane, so that users can’t, for example, run `kubectl` commands that impact other tenants’ resources
- The runtime and networking environment, where container workloads should not be able to interfere with each other or steal resources

The Kubernetes [namespace](http://bit.ly/2r0wBc3) gives us the first building block for multitenancy in the control plane. Typically, there will be one namespace per tenant. Users are given RBAC permissions to create, update, and delete resources within the namespace that maps to their tenancy (see [Chapter 3](ch03.html#ch_authn) and [Chapter 4](ch04.html#ch_authz)). [Resource quotas](http://bit.ly/2r0eq6p) allow each namespace (and thereby, each tenant) to be restricted to a limit of compute and storage resources, and of Kubernetes objects (for example, upper bounds on the number of services, secrets, and persistent volume claims allowed within the namespace).

In an enterprise environment, this may be sufficient. Namespace-based RBAC controls mean that one team can’t update application code and associated Kubernetes resources that they are not responsible for. Quotas mean that one team’s application can’t use all available resources so that another is starved.

However, this is unlikely to be sufficient protection in a fully untrusted environment. Here, tenant workloads should be isolated from each other at a container level so that if there were to be an escape from one container (perhaps because a user deploys code with a serious vulnerability, perhaps even deliberately), they can’t affect or inspect other tenants’ applications or data. Container sandboxing, as described in [“Sandboxing and Runtime Protection”](#advanced_runtimesandboxing), is largely designed to solve this problem (for example, the gVisor approach is based on the way [Google isolates user workloads](http://bit.ly/2zsA3C5) from each other in Google App Engine).

Another approach to workload isolation is to assign one or more nodes to each tenant, and then schedule pods so that workloads are only ever colocated with other workloads from the same tenant. This is straightforward (using [taints and tolerations](http://bit.ly/2ztTIBI)), but potentially wasteful unless each tenant needs a node’s worth of compute resources.

In an untrusted multitenant environment, you would want strong network policies to isolate traffic so that it can’t flow between namespaces. See [“Network Policies”](ch06.html#running_networkpolicies) for more information.

# Dynamic Admission Control

From Kubernetes 1.9, [dynamic admission controllers](http://bit.ly/2DwR2Y3) allow for flexible, extensible mechanisms for making checks before allowing a resource to be deployed to a cluster. As an example, check out Kelsey Hightower’s [Grafeas tutorial](http://bit.ly/2OcTHub), which includes a validating webhook that ensures that only signed images are admitted.

# Network Protection

In a typical traditional deployment, a significant proportion of the security measures is network based: firewalling and the use of VPNs come immediately to mind. In the cloud-native world, similar approaches are dedicated to restricting traffic so that only approved flows can take place.

Security solutions for containers have for some years talked about network [micro-](http://bit.ly/2ONkASt) or [nano-segmentation](http://bit.ly/2DuISzk), and these approaches have been made fairly common practice in Kubernetes deployments through the use of network policies (as discussed in [“Network Policies”](ch06.html#running_networkpolicies)).

At the time of writing, service meshes are a popular topic—although, in our opinion, currently at the stage of “early adopter” rather than “early majority” market penetration.

## Service Meshes

The idea of a service mesh like [Istio](https://istio.io/) or [Linkerd](https://linkerd.io/) is to take on much of the burden of networking communication and control, so that application developers don’t need to concern themselves with these nonfunctional capabilities. While they offer several features like load balancing and routing that are outside the scope of this book, they offer two features that are of particular interest in relation to security: mutually authenticated TLS connections and service mesh network policies.

### Mutually authenticated TLS connections

The service mesh intercepts network traffic to and from a pod, and ensures that connections are all set up using TLS between authenticated components. This automatically ensures that all communications are encrypted. Even if attackers find their way into your cluster, they will struggle to intercept the network traffic within it.

### Service mesh network policy

The service mesh can control which services can communicate with each other, adding another layer of protection that makes it harder for an attacker to move within the cluster.

As discussed in [“Network Policies”](ch06.html#running_networkpolicies), Kubernetes [network policies](http://bit.ly/2vgq96P) define what traffic is allowed to and from a group of pods, so you may well be wondering how Kubernetes and service mesh network policies interact.

Kubernetes network policy acts at the networking level, based on IP addresses and ports as well as pods (identified by label), whereas service mesh policy acts at the service level. There is a good discussion of this in a [series of blog posts from Project Calico](http://bit.ly/2OOrpmF).

# Static Analysis of YAML

In many organizations, the YAML associated with an application could be written by a developer who may not have intimate knowledge of the security policies that the organization requires (or who may simply make a mistake). Static analysis tools such as [`kubetest`](https://github.com/garethr/kubetest) and [`kubesec`](http://kubesec.io) can be useful to look for issues in YAML configuration files (for example, checking for the use of the `privileged` flag for a pod), or to enforce a particular labeling policy. Just like image scanning (see [“Scanning Container Images”](ch05.html#images_scan)), this is an example of “shift-left,” where security practices are dealt with and enforced earlier in the development lifecycle.

# Fork Bombs and Resource-Based Attacks

A [*fork bomb*](https://en.wikipedia.org/wiki/Fork_bomb) is a process that continually launches copies of itself, with the intention of using all the available resources, effectively creating a denial-of-service attack. Kubernetes addresses this by allowing you to [configure a limit on the number of processes within a pod](http://bit.ly/2QXLicv). At the time of writing, this is an [Alpha feature](http://bit.ly/2OOhIEQ) that may be subject to significant changes in the future.

Other resource-based attacks might involve trying to consume excessive memory and CPU, denying those resources to legitimate workloads. You can [set resource limits](http://bit.ly/2Obcx4V) to limit exposure to this kind of attack.

# Cryptocurrency Mining

A [famous attack on Tesla](https://blog.redlock.io/cryptojacking-tesla) exploited control-plane insecurities to allow hackers to use the company’s resources to mine cryptocurrency. Following the advice in [Chapter 2](ch02.html#ch_k8s_ctrl) will go a long way to preventing this from happening in your cluster.

[Additional research](http://bit.ly/2QRUTSh) shows other approaches that would-be miners are attempting. Ensuring that only trusted images can run in your cluster would prevent, for example, a bad actor with approved access to the cluster from running an unexpected mining image. See [Chapter 5](ch05.html#ch_images) for advice on preventing untrusted or compromised images from running.

Runtime protection can add another layer of defense to ensure that even if an approved image has a vulnerability that allows code to be injected into a running container, that code can’t be executed.

Monitoring for unusual activity, such as unexpected CPU usage and unexpected resources being scaled out, can help spot when your resources are being used by an attacker. See [“Monitoring, Alerting, and Auditing”](#advanced_mon_auditing).

# Kubernetes Security Updates

From time to time, security issues in Kubernetes itself are unearthed, and the project has a [security process](http://bit.ly/2IdkSPX) for dealing with these. The project documentation includes instructions for [reporting a vulnerability in Kubernetes to the security team](http://bit.ly/2OdqoYk).

If you want to be alerted as soon as vulnerabilities in Kubernetes are announced, subscribe to the [kubernetes-announce](http://bit.ly/2Q6SzWe) mailing list.

To learn more about the topics discussed in this chapter, check out the resources on the accompanying website, in the [“Advanced Topics”](https://kubernetes-security.info/#advanced-topics) section.

We’ve reached the conclusion of the book and want to thank you for sticking with us until the very end. Enjoy Kubernetes in production—and stay safe!
