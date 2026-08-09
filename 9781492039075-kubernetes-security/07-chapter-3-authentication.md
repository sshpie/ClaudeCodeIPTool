# Chapter 3. Authentication

If you’ve been using public cloud offerings such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform, you might have come across the term *identity and access management* (IAM), which allows you to define access to resources for users and services. In this chapter and in [Chapter 4](ch04.html#ch_authz), we discuss how this is realized in Kubernetes.

All components, such as a kubelet running on a node, as well as users issuing `kubectl` commands, need to communicate with the API server. To process the request, the API server first has to verify who (or what, in the case of machines) is issuing the request; the server has to establish the identity of the caller, or in other words, to authenticate the caller. This chapter covers how [authentication](http://bit.ly/2RQXE5J) in Kubernetes works and the options you have at hand as a cluster operator.

# Identity

For the API server to authenticate a request, the request issuer needs to possess an identity. At the time of writing, Kubernetes doesn’t have a first-class notion of a human user, but rather assumes that users are managed outside Kubernetes via a directory service such as Lightweight Directory Access Protocol (LDAP) or single sign-on (SSO) login standards like Security Assertion Markup Language (SAML) or Kerberos. This is the standard approach in production, but if you’re not using such a system, other [authentication strategies](http://bit.ly/2xECZdF) are available.

User accounts are considered cluster-wide, so make sure that the usernames are unique across namespaces.

###### Note

A *namespace* in Kubernetes is a way to logically divide the cluster into smaller units of management. You can have any number of namespaces; for example, you might have one per application, or one per client, or one per project. Resources in Kubernetes are either namespaced (services, deployments, etc.) or cluster-wide (nodes, persistent volumes, etc.) and you can consider a namespace as one of the built-in security boundaries. [“Security Boundaries”](ch06.html#running_boundaries) provides more information on this topic.

It’s not just humans who interact with Kubernetes. We often want a programmatic way for applications to communicate with the Kubernetes API; for example, to query, create, or update resources such as pods, services, or deployments. To that end, Kubernetes has a top-level resource to represent the identity of an application: the [service account](http://bit.ly/2xEDfcD). A *service account* is a namespaced resource that you can use if your application needs to communicate with the API server. Many business applications don’t need to manipulate Kubernetes resources in this way, so (following the principle of least privilege) they can have service accounts with limited permissions.

By default, Kubernetes makes the credentials of the service account available via a secret that is mounted into the pod (note that all files shown here are owned by `root`):

```
$ kubectl run -it --rm jumpod \
              --restart=Never \
              --image=alpine -- sh
~ $ ls /var/run/secrets/kubernetes.io/serviceaccount/
ca.crt          namespace       service-ca.crt  token
```

Most important here is the `token` file provided, which is a JSON Web Token as per [RFC7519](https://tools.ietf.org/html/rfc7519):

```
~ $ cat /var/run/secrets/kubernetes.io/serviceaccount/token
eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3Nl...
```

You can use the debugger provided by [*jwt.io*](https://jwt.io/) to see what exactly the payload of that token is; so, for example, copying content from the preceding `token` file gives the output shown in [Figure 3-1](#sa-jwt-token-fig).

![Example of a JSON Web Token provided by a service account](/api/v2/epubs/urn:orm:book:9781492039075/files/assets/kuse_0301.png)

###### Figure 3-1. A JSON Web Token provided by a service account

If you don’t explicitly specify a service account in the pod spec, the default service account for the namespace is used.

The general form of a service account is as follows:

```
system:serviceaccount:$NAMESPACE:$NAME
```

In [Figure 3-2](#serviceaccount-fig), you can see a more complex example setup.

![Service accounts](/api/v2/epubs/urn:orm:book:9781492039075/files/assets/kuse_0302.png)

###### Figure 3-2. Service accounts

Here we have two pods, `simplepod` and `podwithsa`. The former doesn’t specify the service account and hence ends up using the default service account of the namespace. On the other hand, `podwithsa` uses a dedicated service account called `mysa` that you can create, for example, using the following command:

```
$ kubectl create serviceaccount mysa
serviceaccount "mysa" created

$ kubectl describe serviceaccount mysa
Name:                mysa
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   mysa-token-prb4r
Tokens:              mysa-token-prb4r
Events:              <none>

$ kubectl get secrets
NAME                TYPE                                DATA AGE
default-token-dbcfn kubernetes.io/service-account-token 3    26m
mysa-token-prb4r    kubernetes.io/service-account-token 3    9m
```

What you can learn from the preceding output (also shown in [Figure 3-2](#serviceaccount-fig)) is that the creation of a service account triggers the creation of a secret, attached to and managed by the service account. This secret contains the JSON Web Token discussed earlier.

Now that we have created the service account, we want to use it in a pod. How can you do that? Simply by using the `serviceAccountName` field in the pod spec to select the service account, in our case, `mysa`. Let’s store a pod spec in a file called *podwithsa.yaml* with the following content:

```
apiVersion: v1
kind: Pod
metadata:
  name: podwithsa
spec:
  serviceAccountName: mysa
  containers:
  - name: shell
    image: alpine:3.7
    command:
      - "sh"
      - "-c"
      - "sleep 10000"
```

You can launch the pod and inspect its properties as follows (the output has been edited for better readability):

```
$ kubectl apply -f podwithsa.yaml
pod "podwithsa" created

$ kubectl describe po/podwithsa
Name:         podwithsa
Namespace:    default
...
Volumes:
  mysa-token-prb4r:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  mysa-token-prb4r
    Optional:    false
...
```

And indeed, here you see that our `podwithsa` pod uses its own service account with the token `mysa-token-prb4r` (allowing it to communicate with the API server) available at the usual file location */var/run/secrets/kubernetes.io/serviceaccount/token* mounted into the pod.

At this point, you might be wondering why you would bother at all messing around with service accounts and not always use the default service account. This will make more sense when you learn how service accounts are used with RBAC to define permissions for users and applications in [Chapter 4](ch04.html#ch_authz). For now, just remember that service accounts allow applications to communicate with the API servers (if they have to at all).

Now that we’ve covered the basics of identity in Kubernetes, let’s move on to how authentication works.

# Authentication Concepts

In [Figure 3-3](#authn-concept), you can see how the API server conceptually performs authentication by using one of the available strategies represented by the authentication plug-ins (learn more about the supported strategies in the next section).

![Authentication concepts](/api/v2/epubs/urn:orm:book:9781492039075/files/assets/kuse_0303.png)

###### Figure 3-3. Authentication concepts

The flow Kubernetes uses to authenticate a client’s request is as follows:

1. The client presents its credentials to the API server.
2. The API server uses one of the configured authentication plug-ins (you can enable multiple) to establish the identity with an identity provider.
3. The identity provider verifies the request information, including username and group membership.
4. If the credentials are in order, the API server moves on to check permissions as described in [Chapter 4](ch04.html#ch_authz). Otherwise, it returns an HTTP `401 Unauthorized` client error status response code, and with that the request fails.

###### Note

The identity provider and its behavior depend on the authentication plug-in used. For example, it could simply be a file with usernames and passwords that you provide to the API server or an external system like Active Directory. Kubernetes is not opinionated concerning how you verify the credentials; it just provides the interface and enforces a certain flow to make sure requests come from well-known clients.

Kubernetes also supports [user impersonation](http://bit.ly/2xEzaW1); that is, a user can act as another user. For example, as a cluster admin, you could use impersonation to debug any authorization issues.

# Authentication Strategies

A couple of authentication strategies are available in Kubernetes, represented by authentication plug-ins. Depending on the size of the deployment, the target users (human versus processes), and organizational policies, you as a cluster admin can choose one or more of the following:

Static password or token fileThis strategy uses the Basic HTTP authentication scheme as per [RFC7617](https://tools.ietf.org/html/rfc7617). Essentially, the API server requires the client to provide the identify via an HTTP header named `Authorization` and the value of `Basic base64($USER:$PASSWORD)` in case of a static password file or `Bearer $TOKEN` in case of a static token file. Since it’s inflexible to maintain a static file with the users and their passwords and requires direct access to the API server, this method is not recommended in production.

X.509 certificatesWith this strategy, every user has their own X.509 client certificate. The API server then validates the [client certificate](http://bit.ly/2Q6cTXJ) via a configured certificate authority (CA). If the client certificate is verified successfully, the common name of the subject is used as the username for the request, and any organizations defined for the subject are used as groups. As an admin, you need to manage access to the CA as well as issue the client certificates, and reissue them as they approach expiry. Kubernetes does not, at the time of writing, support [certificate revocation](http://bit.ly/2IfCNFK), and this is considered a good reason to use an SSO approach where possible.

OpenID Connect (OIDC)OIDC is an identity layer on top of the OAuth 2.0. With this strategy, you use OIDC to provide the API server with an `id-token` in the form of a [JSON Web Token](https://jwt.io/) after using your provider’s login page, such as Google or Azure Active Directory.

Bootstrap tokensThese are an experimental feature targeting the cluster setup phase and can be used with installers such as [`kubeadm`](http://bit.ly/2MZNPQg).

If you want to integrate with other authentication protocols such as LDAP, SAML, and Kerberos, you can use one of the following methods:

Authenticating proxyThe API server can be configured to identify users from request header values, such as `X-Remote-User`. You need to take care of setting up and running the proxy; see, for example, [Haoran Wang’s post of an authentication example](http://bit.ly/2ztRMt7).

Webhook token authenticationEssentially, a [hook](http://bit.ly/2OeczsH) for verifying bearer tokens.

With that, we move on to some good practices and tooling around authentication.

# Tooling and Good Practices

The majority of the effort in the context of authentication is with the Kubernetes cluster administrator. You would start off with existing infrastructure that you need to integrate with, such as an LDAP server your organization already uses to capture team members and group-related information. You also want to take into account the environment the cluster is running in, like a public cloud provider, a managed service (Amazon Elastic Container Service for Kubernetes, Azure Kubernetes Service, Google Kubernetes Engine, OpenShift Online, etc.), or an on-premises deployment. The latter is important, as you may have different options depending on the environment and may end up having more or less work with the authentication bits, based on what authentication strategy you go for.

Several tools are available to help with this (you may wish to check the [latest list](https://kubernetes-security.info/#authentication) on the website accompanying this book):

KeycloakAn open source IAM solution with built-in support to connect to existing LDAP servers. Keycloak can authenticate users with existing OIDC or SAML 2.0 identity providers. A [Helm chart](http://bit.ly/2OS6NKf) is also available to deploy it in Kubernetes.

DexAn identity service that uses OIDC to drive authentication for other applications. Dex acts as a portal to other identity providers, allowing you to defer authentication to LDAP servers, SAML providers, or established identity providers like GitHub, Google, and Active Directory.

AWS IAM Authenticator for KubernetesA tool to use AWS IAM credentials to authenticate to a Kubernetes cluster maintained by Heptio and Amazon.

GuardA Kubernetes webhook authentication server by AppsCode, allowing you to log into your Kubernetes cluster by using various identity providers, from GitHub to Google to LDAP.

In the last section of this chapter, we look at good practices in the context of authentication. Note that because a new Kubernetes release comes out every couple of months, some tips might be more relevant than others (as defaults change or new features are introduced):

Use third-party providersUnless you have to roll your own thing, integrate Kubernetes with third-party identity providers such as Azure, Google, or GitHub.

Don’t use static filesIf you can’t use third-party providers, prefer X.509 certificates over static password or token files.

Life cycleEnsure that when people leave the organization, their credentials are invalidated. With third-party providers, this task is typically easier compared to when you roll your own solution. In any case, regular audits help here as well to uncover holes.

To learn more about authentication options and gotchas, check out the resources on the accompanying website, in the [“Authentication”](https://kubernetes-security.info/#authentication) section.

With this, we have reached the end of the discussion of authentication in Kubernetes, and you are ready to learn where and how the authentication information eventually is used: giving users and applications permissions and enforcing those, through a process known as *authorization*.
