# Chapter 7. Secrets Management

Your application code often needs access to secret information, like credentials, in order to do its job. For example, if you run an e-commerce site, some components will need access to a product database, and other components likely will need to be able to manage user or payment information. These components will need the right access tokens or username/password combinations so they can access the data they need to view or manipulate.

In this chapter, we consider the options for passing secret information into your code running under Kubernetes. Kubernetes provides a “secret” resource for this purpose, but there are different ways of using these secrets that you will want to weigh. In addition, you also need to be aware of some aspects of the Kubernetes secrets implementation from a security perspective.

# Applying the Principle of Least Privilege

The principle of least privilege has two consequences on secrets management in Kubernetes:

- We want to ensure that containerized code can read only the secrets that it needs.
- It’s a good idea to have a different set of secrets for different environments (like production, development, and testing). The development and test credentials can be shared with a wider set of team members without necessarily giving them full access to the production credentials.

# Secret Encryption

Since secret values protect sensitive data, we want them to be hard to access. Ideally, they should by protected at rest and in transit:

At restSecrets should always be stored on disk in encrypted form, so that an attacker with access to the filesystem cannot simply read them from the file. In this chapter, you will see how secrets are stored in Kubernetes, and our options for encrypting at rest.

In transitSecrets should be encrypted whenever they are sent as network traffic, so that an attacker snooping on the network cannot read them as they pass.

Encryption in transit is achieved by encrypting the traffic between the Kubernetes control-plane components using TLS (see [Chapter 2](ch02.html#ch_k8s_ctrl)). In order to consider how we can store our secrets safely in encrypted form, let’s look at how Kubernetes manages secrets, and the options for where they can be stored.

# Kubernetes Secret Storage

The [Kubernetes secret resource type](http://bit.ly/2xCI7Pz) is a mechanism for passing secrets to your code without them appearing in plain text in the pod’s YAML. Instead, the pod specification refers to a secret by name, and the actual value of the secret is configured separately.

###### Warning

Take care with the storage and control of any YAML or JSON manifest files used to define secrets. If you check these manifests into source code control, the secret value is accessible to anyone with access to that repository. Note also that secret values encoded in base64 in secret manifest files are not encrypted!

The default storage for secret values is etcd, or you can use third-party secret storage solutions.

## Storing Secrets in etcd

By default, secret values are stored alongside other configuration information in the etcd database; they are simply base64 encoded.

###### Warning

Although base64 encoding makes content unreadable to the human eye, it does not encrypt it. If you come across base64-encoded information, you simply need to pass it through base64 decoding to retrieve the original information; no key is required. In other words, base64 is effectively plain text to an attacker.

Anyone who gains access to your etcd database will be able to read base64-encoded secrets from it. You can control access by configuring secure access only (see [Chapter 2](ch02.html#ch_k8s_ctrl)), but even then there is a risk: your data is written to disk unencrypted, and if an attacker gains access to the filesystem, your data may be compromised.

You can avoid this risk by ensuring that your [etcd cluster is also encrypted on disk](http://bit.ly/2ORsavt). (The API server has access to the encrypted data in etcd, so you will also want to limit API access as described in [Chapter 2](ch02.html#ch_k8s_ctrl) and [Chapter 4](ch04.html#ch_authz).)

###### Tip

The *EncryptionConfig* YAML file for etcd encryption includes a secret for unlocking the encrypted data. You should make sure that this file can be read only by the user account that runs the Kubernetes API server, which often is `root`.

It’s good practice to [rotate the encryption secret](http://bit.ly/2xEyUWW) from time to time. If you have multiple etcd nodes, you should also [encrypt the communication between them](http://bit.ly/2N1wIxq), to prevent the secret values from being passed in the clear.

## Storing Secrets in Third-Party Stores

Some third-party systems are specifically designed to store secret and sensitive values. Using these in conjunction with Kubernetes is considered by many to be a more secure option than storing the secrets alongside less-sensitive information in etcd.

The major cloud providers have key management systems that can be used in this way. Other third-party solutions include [HashiCorp Vault](https://www.vaultproject.io/) and [CyberArk Conjur](https://www.conjur.org/).

Commercial container security tools offer integration with multiple backend secret stores, and can also control access so that only specific containers have access to particular secrets.

# Passing Secrets into Containerized Code

There are three ways to get secrets (or any other kind of information) into a container so that they are accessible to the application:

- Building them into the image itself
- Passing them into the container as environment variables
- Mounting a volume into a container so that code can read the information out of a file on that volume

You might be thinking that the container application could query secrets through some kind of network activity, but then the question arises: how do you stop that information from being available to bad actor entities without requiring credentials of some kind? Then those credentials are a secret that needs to be passed into the container first, and we are back to the set of three options.

Kubernetes secrets support the last two of these approaches, although for reasons we will cover shortly, the third option of mounting a volume is generally considered the safest, so if you are short of time, skip ahead to [“Passing Secrets in Files”](#secrets_in_files). Before we come to that, let’s consider why building secrets into container images is really not a great idea.

## Don’t Build Secrets into Images

The first of these options is a bad idea for secrets, and here are a few reasons:

- Anyone who has access to the image can obtain the secrets it holds. Bear in mind that the set of people who can access the image may not be the same set of people who need your production credentials.
- If you want to change a secret value, you need to rebuild the image. This can imply downtime: for example, if you change database credentials, your application code can’t access the database until it is rebuilt and redeployed.
- Anything that is built into the image is likely under source code control, and unfortunately it’s all too common to see [secret information made publicly available through GitHub](http://bit.ly/2ztncQn) and similar tools. Even if your repos are private, consider the possibility that an authorized user forks your repo and makes it public.

## Passing Secrets as Environment Variables

The [Twelve-Factor App manifesto](https://12factor.net/config) taught us to pass configuration information into applications as environment variables. This allows us to separate configuration from code, which is helpful when you need to run the same code in different scenarios (production, test, your own laptop…).

You can pass environment variables into containers at runtime. This means you can take the container image (code) and configure it according to the scenario it is running in. In Kubernetes, “ordinary” environment variables can be specified directly in the pod YAML or via a [ConfigMap](http://bit.ly/2Q8Hlkb). But be careful: including secret values in YAML files that you check into code control means those secrets are accessible to the same people who can see the source code.

To mitigate this, Kubernetes also supports the [secret](http://bit.ly/2xCI7Pz) resource, which can be [passed into a pod as an environment variable](http://bit.ly/2xO0Syz). Your pod spec or ConfigMap YAML refers to the secret resource by name rather than directly to the secret value, so that it’s safe to put that YAML under code control.

However, it’s easy to “leak” information from environment variables to places you might not have considered. Let’s have a look at three cases:

### Case 1

It’s common for a process to log out its entire environment in the event of a crash. This may be written to file, or in many deployments it will make its way to a centralized log aggregation system. Should the people who have access to this system also have access to your production database credentials?

### Case 2

Take a look at the results from `kubectl describe pod <example>` and you will find the environment variables are available in plain text, such as shown in the following:

```
$ kubectl describe pod nginx-env-6c5b7b8ddd-dwpvk
Name:           nginx-env-6c5b7b8ddd-dwpvk
...
Containers:
  nginx-env:
  ...
    Environment:
      NOT_SO_SECRET:  some_value
  ...
```

You may have people who are allowed to inspect running pods in your cluster who again don’t need access to the most privileged of credentials in your system.

### Case 3

If you are using Docker as your container runtime, the environment is accessible using `docker inspect <container>`, running on the host as shown here:

```
$ sudo docker inspect b5ad78e251a3
[
  {
   "Id": "b5ad78e251a3f94c10b9336ccfe88e576548b4f387f5c7040...",
   ...
   "Config": {
      "Hostname": "nginx-env-6c5b7b8ddd-dwpvk",
     ...
     "Env": [
      "NOT_SO_SECRET=some_value",
      ...
    ]
   }
  }
]
```

The fact that environment variables are accessible via logs or via the command line to a broader set of people than might need access to secret credentials can be considered a security risk. You should contemplate whether this is an issue in your application and in your organization.

Some commercial solutions inject secrets into the environment by using a proprietary technique that means that the secret is not available through the command line via `kubectl describe` or `docker inspect`. However, this approach still doesn’t protect against leaks through dumping the environment to a file or to a log.

You can restrict access via `kubectl` by using RBAC (see [Chapter 4](ch04.html#ch_authz)) so that only a subset of users can access specific pods.

## Passing Secrets in Files

The last mechanism for passing information into a container is via a volume mounted into the container, where secret values are written into files on that volume. Kubernetes supports passing [secrets into pods through volume mounts](http://bit.ly/2xNOOxy). The containerized code needs to read values out of these files.

If the mounted volume is a temporary filesystem, so much the better. This means the files are not written to disk, but held in memory, thus helping our aim of never storing secrets in plain text at rest.

The values held in the file are not accessible via `docker inspect` or `kubectl describe`. It’s possible that the application code might write these secrets to somewhere undesirable, but this is much less likely than the inadvertent inclusion of secrets as part of a dump of environment variable values.

# Secret Rotation and Revocation

For humans, it is [no longer considered advisable to require frequent password changes](http://bit.ly/2xOFR6R), but this advice doesn’t apply to the secrets used by machines. The longer a given secret remains valid, the more likely that it has been compromised. By regularly changing, or “rotating,” secret values, we can ensure that a secret stops being of any use to an attacker.

For both the human- and machine-readable credentials related to your applications, you should have a mechanism in place that allows you to revoke a value if you discover it has been compromised. If you have a regular secret rotation process in place, you can have confidence that you can revoke or change a secret in the event of an emergency without harmful effects on the system.

Depending on how your application code is written, you may need to restart a pod in order for a new secret value to take effect. For example, an application might read a database password (from a file or from an environment variable) just once as part of its initialization; it would need to be restarted in order to read the new value when it changes.

A different approach in the application might be to reread the secret value, perhaps on a regular basis, or in response to a failure using the currently held value. If the application code can cope with a secret being updated, this leads us to a benefit of the file-based approach to passing secrets: Kubernetes can update the secret value written to file without having to restart the pod. If you’re using the environment variable mechanism in Kubernetes to pass secrets, they can’t be updated live without a pod restart (although commercial solutions provide this capability).

# Secret Access from Within the Container

If attackers gain execution access to a container, there is a high likelihood they will have access to the secrets within that container. This includes access via `kubectl exec` and `docker exec`.

In this situation, runtime protection can help (see [“Sandboxing and Runtime Protection”](ch08.html#advanced_runtimesandboxing)). The fewer tools that the attacker can run inside the container, the better. For example, if the secrets are held in a file, preventing the attacker from being able to run commands like `cat`, `more`, or `less` make it harder to reach the secrets.

You can also limit the attacker’s ability to access secrets by not building those commands into the container image in the first place. See [Chapter 5](ch05.html#ch_images) for more on reducing the attack surface in an image.

# Secret Access from a Kubelet

Prior to Kubernetes 1.7, any kubelet could access any secret, but nowadays [node authorization](http://bit.ly/2IfD2k1) ensures that a kubelet can access only the secrets related to those pods that are scheduled to its node. If a node is compromised, this limits the effect of secrets access. You can ensure that this is in use by confirming that `--enable-admission-plugins` includes `NodeRestriction`.

To learn more about secrets and how to use them, check out the resources on the accompanying website, in the [“Secrets”](https://kubernetes-security.info/#secrets) section.

So far, we have discussed how to set up your Kubernetes cluster with security in mind, and approaches for building and running application code safely. We now move on to discuss advanced security features that might apply, depending on your particular needs, and some new projects and capabilities that are under development at the time of writing.
