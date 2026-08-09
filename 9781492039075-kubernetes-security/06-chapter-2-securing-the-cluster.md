# Chapter 2. Securing the Cluster

Perhaps it goes without saying, but you don’t want to allow unauthorized folks (or machines!) to have the ability to control what’s happening in your Kubernetes cluster. Anyone who can run software on your deployment can, at the very least, use your compute resources (as in the well-publicized case of “cryptojacking” at [Tesla](https://blog.redlock.io/cryptojacking-tesla)); they could choose to play havoc with your existing services and even get access to your data.

Unfortunately, in the early days of Kubernetes, the default settings left the control plane insecure in important ways. The situation is further complicated by the fact that different installation tools may configure your deployment in different ways. The default settings have been improving from a security point of view, but it is well worth checking the configuration you’re using.

In this chapter, we cover the configuration settings that are important to get right for the Kubernetes control-plane components, concluding with some advice on tools that can be used to verify the deployed configuration.

# API Server

As its name suggests, the main function of the Kubernetes API server is to offer a REST API for controlling Kubernetes. This is powerful—a user who has full permissions on this API has the equivalent of root access on every machine in the cluster.

The command-line tool `kubectl` is a client for this API, making requests of the API server to manage resources and workloads. Anyone who has write access to this Kubernetes API can control the cluster in the same way.

By default, the API server will listen on what is rightfully called the [*insecure port*](http://bit.ly/2O8SHas), port 8080. Any requests to this port *bypass authentication and authorization checks*. If you leave this port open, *anyone who gains access to the host your master is running on has full control over your entire cluster*.

*Close the insecure port* by setting the API server’s `--insecure-port` flag to 0, and ensuring that the `--insecure-bind-address` is not set.

###### Note

The `--insecure-port` flag was deprecated in Kubernetes v1.10 and is a target for removal altogether in the future.

You can check whether the insecure port is open on the default port with a simple `curl` command like the following, where `<IP address>` is the host where the API server is running (or `localhost` if you can SSH directly to that machine):

```
$ curl <IP address>:8080
{
  "paths": [
    "/api",
    "/api/v1",
    "/apis",
...
```

If the response lists API endpoints, as in the preceding example, then the insecure port is open. However, if you see an error message of *Connection refused*, it’s good news, as the port is not open.

With the insecure port closed, the API can be accessed only over a secure, encrypted TLS connection via the *secure port*. You may want to further restrict API access to known, authenticated users by setting `--anonymous-auth=false` for the API server. However, it is not reckless to allow anonymous access to the API so long as you are using RBAC, which we strongly recommend. We discuss this in more detail in [“Access Control with RBAC”](ch04.html#authz_rbac).

The [default RBAC settings](http://bit.ly/2zttgZ0) permit only limited API access for anonymous users. This allows for health and discovery checks to be made, for example, by components like load balancers.

One thing to be aware of, however, is that enabling anonymous access to discovery endpoints could also increase the likelihood of leaking information about the software that’s running on the system to an attacker. This read-only information is unlikely to compromise anything important by itself, but it can signpost an attacker toward other weaknesses. For example, if attackers can use health-check information to learn that a particular database is in use, they could use that information to choose which types of attack are more likely to work against that database.

For this reason, you may want to protect network access to the API server by using other mechanisms—perhaps a traditional firewall or a virtual private network (VPN).

Although we cover RBAC in more detail later, for now let’s cover how to enable it in the control plane:

- Set `--authorization-mode` on the API server to enable the `RBAC` authorization module.
- Include the `Node` authorizer in the `--authorization-mode` list, which (in conjunction with the `NodeRestriction` admission controller described in the next section) enables RBAC for kubelets.

# Kubelet

The [kubelet](http://bit.ly/2MZT8iN) is the agent on each node that is responsible for interacting with the container runtime to launch pods, and report node and pod status and metrics. Each kubelet in the cluster also operates an API, through which other components ask it to do things like starting and stopping pods. If unauthorized users can access this API (on any node) to execute code on the cluster, it’s possible to [gain control of the entire cluster](http://bit.ly/2Q0ECZY).

Fortunately, layers of defense are now available in Kubernetes that make it easy to prevent this kind of attack:

- You can limit the API access to authenticated requests; that is, anonymous requests are ignored.
- You can leverage access control to stop unauthorized actions from being performed (see [“Access Control with RBAC”](ch04.html#authz_rbac)).

More specifically, here are some configuration options to lock down the kubelets and hence help minimize the attack surface:

- *Disable anonymous access* with `--anonymous-auth=false`, so that unauthenticated requests will receive *Unauthorized Access* error responses. This requires the [API server to identify itself to the kubelet](http://bit.ly/2ONLU2T), which you can set up with the `--kubelet-client-certificate` and `--kubelet-client-key` flags.
- *Ensure that requests are authorized* by setting [`--authorization-mode` to something other than `AlwaysAllow`](http://bit.ly/2NEKPxZ). The [`kubeadm`](http://bit.ly/2xORevG) installation tool defaults this setting to `Webhook` so that the [kubelet calls `SubjectAccessReview` on the API server for authorization](http://bit.ly/2Od4XGR).
- *Limit the permissions of kubelets* by including `NodeRestriction` in the [`--admission-control` settings](http://bit.ly/2IgwP7G) on the API server. This restricts a kubelet so that it can modify only pods that are bound to it and its own `Node` object.
- Set `--read-only-port=0` to *turn off the read-only port*. This port allows an anonymous user to access information about running workloads. While access to this port doesn’t allow a hacker to control the cluster, exposing information about what’s running could make it easier to attack.
- Older Kubernetes deployments used cAdvisor to provide metrics, but this has largely been superseded by stats on the Kubelet API. Unless you know you are using the kubelet cAdvisor port, you should turn it off to stop it from exposing information about your running workloads, by setting `--cadvisor-port=0`. This is the default setting in Kubernetes v1.11, and it is expected that the flag will be removed altogether in the future. If you want to run cAdvisor on your cluster, it is now [recommended](https://github.com/kubernetes/kubernetes/issues/56523) that you do this with a `DaemonSet`.

You can check what access is available on a kubelet by attempting an API request to the node as follows:

```
$ curl -sk https://<IP address>:10250/pods/
```

- If `--anonymous-auth` is `false`, you will see a `401 Unauthorized` response.
- If `--anonymous-auth` is `true` and `--authorization-mode` is `Webhook`, you’ll see a `403 Forbidden` response with the message `Forbidden (user=system:anonymous, verb=get,` `resource=nodes, subresource=proxy)`.
- If `--anonymous-auth` is `true` and `--authorization-mode` is `AlwaysAllow`, you’ll see a list of pods.

## Kubelet Certificate Rotation

Each kubelet needs a client certificate so that it can communicate with the API server. From 1.8 onward, the kubelet supports [rotating these certificates automatically](http://bit.ly/2IjCr12) with use of the `--rotate-certificates` flag, so that a new certificate will be requested and issued automatically as the expiry deadline approaches. Unless you have a good reason not to do so, we recommend enabling this feature.

# Running etcd Safely

Kubernetes stores configuration and state information in a distributed key-value store called etcd. Anyone who can write to etcd can effectively control your Kubernetes cluster. Even just reading the contents of etcd could easily provide helpful hints to a would-be attacker. Therefore, you need to ensure that only authenticated access is permitted:

- Set `--cert-file` and `--key-file` to enable HTTPS connections to etcd.
- Set `--client-cert-auth=true` to ensure that access to etcd requires authentication. Set `--trusted-ca-file` to specify the certificate authority that has signed the client certificates.
- Set `--auto-tls=false` to disallow the generation and use of self-signed certificates.
- Require etcd nodes to communicate with each other securely by using `--peer-client-cert-auth=true`. Also set `--peer-auto-tls=false` and specify `--peer-cert-file`, `--peer-key-file` and `--peer-trusted-ca-file`. You will need corresponding configuration on the Kubernetes API server so that it can communicate with etcd.
- Set `--etcd-cafile` on the API server to the certificate authority that signed etcd’s certificate.
- Specify `--etcd-certfile` and `--etcd-keyfile` so that the API server can identify itself to etcd.

See the [etcd documentation](http://bit.ly/2NF22av) for more information.

You should take additional measures to [encrypt etcd’s data stored on disk](http://bit.ly/2ORsavt). This is especially important if you are storing Kubernetes secrets in etcd rather than an external secrets store. See [Chapter 7](ch07.html#ch_secrets) for more details on this topic.

Because only the Kubernetes control-plane components have any business communicating with etcd, you can additionally use network firewalling to prevent traffic from other sources from reaching the etcd cluster.

# Kubernetes Dashboard

The *Dashboard* has historically been used by attackers to gain control of Kubernetes clusters. It’s a powerful tool, and in older versions of Kubernetes, the default settings made it easy to abuse; for example, prior to 1.7, the Dashboard had full admin privileges by default.

You might want to take several steps to ensure that your Kubernetes Dashboard is not an easy entry point for attackers, including but not limited to the following:

Allow only authenticated accessOnly known users should be able to access the Dashboard.

Use RBACLimit the privileges that users have so they can administer only the resources they need to.

Make sure the Dashboard service account has limited accessAfter reaching the Dashboard login screen, users have the option to Skip. Taking this path means that rather than authenticating as their own user identity (as discussed in [“Identity”](ch03.html#authn_identity)), they access the Dashboard with the service account associated with the Dashboard application itself. This service account should have [minimal permissions](http://bit.ly/2Q6es7X).

Don’t expose your Dashboard to the public internetUnless you really know what you’re doing.

We recommend checking the latest [Kubernetes Dashboard installation recommendations](http://bit.ly/2xCZYps).

You can use `kubectl proxy` to access the Dashboard securely from a local machine. If you want to give users access directly via their browser, the [Heptio blog](http://bit.ly/2O50ENZ) has a good discussion of the options.

Applying different security measures to the Dashboard gives you defense in depth to mitigate potential attacks. For example, suppose you use `NodePort` as the type for the `kubernetes-dashboard` service so that it is available only from cluster nodes. A compromised pod running within the cluster can still access the Dashboard service, but well-crafted RBAC rules will limit the damage that it could do through that service.

# Validating the Configuration

Once you have set up your Kubernetes cluster, there are two main options for validating whether it is configured safely. These options are configuration testing, where tests validate the deployment against a recommended set of settings, and penetration testing, where tests explore the cluster from the perspective of an attacker.

## CIS Security Benchmark

The Center for Internet Security (CIS) publishes a [Benchmark for Kubernetes](http://bit.ly/2Ie7z1O) giving best practices for configuring a deployment to use secure settings. If you’re using Docker as your underlying run-time, you may also want to follow the [CIS Benchmark for Docker](http://bit.ly/2T87HVt).

It’s a good idea to check your deployment against this benchmark. You might decide that not all the recommendations apply for you, but checking against the benchmark may alert you to insecure settings that you were unaware of. As a simple example, the Kubernetes tests will let you know whether your cluster is configured to allow anonymous access to the Kubernetes API.

###### Tip

Running the benchmark tests on all your nodes on a regular basis will help you spot any configuration drift that might affect your security posture.

Manually running the benchmark tests would be time-consuming. Fortunately, tools exist to automate the process, such as the [Kubernetes Benchmark](https://github.com/aquasecurity/kube-bench) tool (for which Liz is a maintainer).

## Penetration Testing

Enterprises commonly recruit the services of a “pen-tester,” or penetration testing company, to probe their deployed software, searching for ways that an attacker could exploit the software or the platform on which it runs. A penetration-testing specialist will use creative approaches to find weak points in your cluster configuration and in the software running on it.

Additionally, you may like to consider testing with [kube-hunter](http://github.com/aquasecurity/kube-hunter). This project (also one that Liz maintains) is an open source penetration testing tool specifically for Kubernetes.

To learn more about how to secure the Kubernetes control plane, check out the resources on the accompanying website, in the [“Securing the Cluster”](http://bit.ly/2Q6Wfr0) section.

Now that we have covered configuring the Kubernetes control-plane components, let’s move on to discussing how to enable access to the cluster by known users and software entities.
