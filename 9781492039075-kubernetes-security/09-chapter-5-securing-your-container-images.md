# Chapter 5. Securing Your Container Images

Until now, we’ve been discussing things mainly from the point of view of a Kubernetes cluster administrator. Going forward, we’ll switch gears and focus more on developers, operators, or even DevOps teams who want to deploy code to run on the cluster.

The software that you run in your Kubernetes cluster gets there in the form of container images. In this chapter, we’ll discuss how to check that your images:

- Don’t include known critical vulnerabilities
- Are the images you intended to use, and haven’t been manipulated or replaced by a third party
- Meet other image policy requirements your organization might have in place

##### Vulnerabilities

In this context, a *vulnerability* is a flaw in a piece of code that an attacker can exploit to cause undesirable consequences, and that has been publicly disclosed (typically, through the [National Vulnerability Database](https://nvd.nist.gov/)). For example, the renowned [Heartbleed](http://heartbleed.com/) vulnerability was a flaw in the OpenSSL library that allowed attackers to access system memory, and hence steal encrypted information.

# Scanning Container Images

To detect vulnerabilities, you need to use a container image scanner. The basic function of a container image scanner is to inspect the packages included in an image, and report on any known vulnerabilities included in those packages. At a minimum, this looks at the packages installed through a package manager (like `yum` or `apt`, depending on the OS distribution). Some scanners may also examine files installed at image build time; for example, through ADD, COPY, or RUN operations in a Dockerfile. Some scanners also report on known malware (e.g., viruses) or the presence of sensitive data (like passwords and tokens).

To ensure that you’re not running vulnerable code in your deployment, you should scan any third-party container images as well as the ones built by your own organization.

New vulnerabilities continue to be found in existing software, so it’s important to rescan your images on a regular basis. In our experience, it’s typical for enterprise customers to rescan the images in use on their production systems every 24 hours, but you should consider your own risk profile. Depending on the scanning tool you use, this may be a simple configuration setting, or you may need to write automation scripting to put this in place.

Several commercial [image-scanning tools](http://bit.ly/2R0zNkP) are available as well as some open source and/or free-to-use options.

Some registries provide metrics on the health of the container images they store. For example, the [Red Hat Container Catalog](https://access.redhat.com/containers/#/) grades images from A–F, and the [Google Container Registry](https://cloud.google.com/container-registry/) and [Docker Trusted Registry](https://dockr.ly/2QY9onp) also include image scan results.

# Patching Container Images

Once you have identified that you have a container image that includes a package with a vulnerability, you need to update the container to use a fixed version of the package. Please don’t be tempted to SSH into your running containers and run something like `yum update` or `apt-get update`, as this is an antipattern for containers! It quickly becomes unfeasible to manually patch like this when running hundreds or thousands of instances across a cluster. Factor in the self-healing nature of Kubernetes, which ensures that a failed container will be replaced with a new one, and autoscaling, which can create and destroy containers automatically, and it becomes clear that it’s really not possible to keep up with the patching process manually.

The key to “patching” in a container deployment is to rebuild a new container image, and then redeploy the containers based on that new image. The build part is typically automated through a continuous integration (CI) pipeline, and this may be extended to cover continuous deployment (CD) as well. While CI/CD and its bright new cousin, GitOps, are out of scope for this book, it is worth examining how security tooling fits into the CI/CD pipeline.

# CI/CD Best Practices

Image scanning can be integrated into the CI/CD pipeline to automate the process of rejecting images, as shown in [Figure 5-1](#cicd). Many scanners can report a pass or fail for each image, either on basic criteria (“fail all images with high-severity vulnerabilities”) or more-complex, custom policies (“fail if the image has any high-severity vulnerabilities, ignoring this set of whitelisted vulnerabilities, and also fail if the image has this particular blacklisted medium-severity vulnerability, or includes sensitive data”).

You can use this pass/fail in several places in your CI/CD pipeline:

- A failed scan can result in a failed build.
- A failed scan before deployment can prevent the image from being deployed.
- A failed scan on an image that’s already in production can result in an alert so that operators can take remedial action.

![The CI/CD Pipeline](/api/v2/epubs/urn:orm:book:9781492039075/files/assets/kuse_0501.png)

###### Figure 5-1. The CI/CD pipeline

In [Figure 5-1](#cicd), we also see an admission control step. Advanced solutions may also use some form of dynamic admission control (see [“Dynamic Admission Control”](ch08.html#advanced_dynaadmission)) to ensure that images are deployed only if they have been scanned, and the scan was successful. This step can also automatically check whether the image can be trusted, as we’ll come to in [“Image Trust and Supply Chain”](#images_trust).

A good best practice is to use automation to scan all images before they are stored in a container registry, rejecting any images that fail the scan. The next question to consider, then, is the use of a secure container registry.

# Image Storage

Container images can be stored in public or private registries. Many security-conscious organizations use one or more private registries and require that only images from these registries can be deployed.

Running a private registry means that you have greater control over who has permissions to read and write images. You can also deploy the registry with limited network access, perhaps using a firewall so that only known IP addresses can access it.

Several offerings are available for running your own registry, including [Docker’s own implementation](https://docs.docker.com/registry/deploying/), [GitLab’s Container Registry](http://bit.ly/2ztfy8p), and [Quay](https://www.openshift.com/products/quay) from Red Hat.

The major hosted Kubernetes solutions all offer a container registry solution, which can have the advantage of tight integrations with the cloud platform that you are already familiar with. For example, if you are using AWS, the [Elastic Container Registry](https://aws.amazon.com/ecr/) uses IAM for access control.

Whichever registry solution you are using, unless you are pulling public images, you will need to [grant access](http://bit.ly/2xOPIcY) to your Kubernetes cluster so that it can pull images from the registry. It’s a good idea to use *read-only accounts* for this purpose; with the exception of, say, a CI/CD system deployed on Kubernetes, it’s highly unusual that your Kubernetes nodes would need to push images into the registry. By using read-only credentials, you mitigate the possibility that an attacker who gains access to the cluster can push modified images into your registry, which then get pulled and run.

# Correct Image Versions

When we define the containers that will run in pods, the PodSpec refers to the container image by using a fully qualified image name that includes the registry, the owner, the repository, and a reference to a particular image version—for example, *gcr.io/myname/myimage:1.0*.

Typically, the version reference is in the form of a tag (`1.0` in this example). However, tags are [mutable](http://bit.ly/2xysDfp) (the same tag can be moved to refer to a different image), and an image can have multiple tags, so you need to handle your tags with care.

The [Container Solutions](http://bit.ly/2O9U88w) blog provides a good demonstration of the confusion that can be created with image tags.

To be certain that you are deploying a particular version of an image, it’s possible to refer to it by its [unique digest](http://bit.ly/2QYOogh) instead of the tag. Here’s an example of YAML specifying a container in this way (digest truncated for clarity):

```
spec:
  containers:
  - name: myimage
    image: gcr.io/myname/myimage@sha256:4a5573037f358b6cdfa2...
```

While this ensures that you pick up a particular version of a container image, it means updating YAML whenever there is a new revision. In our experience, it’s much more common to refer to images by using a [semantic version](http://semver.org) tag.

If you supply neither a tag nor a digest, the image version tagged `latest` will be used. It’s [recommended](http://bit.ly/2QYOogh) to avoid using the `latest` version, at least in production, because it’s hard to keep track of exactly what code is running, and worse, what version to use should you want to roll back to a previous version.

## Running the Correct Version of Container Images

Make sure to always run the correct version of your container image by doing the following:

- Using semantic versioning when tagging your images. That way, it’s easy to identify the version you expect to be running. An alternative approach is to always refer to an image by its unique [SHA](http://bit.ly/2xXKdc3) digest.
- Using the `AlwaysPullImages` [admission controller](http://bit.ly/2DuQUsc) to ensure that the most recent version that matches the specified tag is obtained. Without this, a node may run a stale version of the image that it pulled some time in the past. You don’t need this if you are confident that all your images have immutable tags, or your YAML refers to all images by SHA. Using `AlwaysPullImages` also ensures that the pod doesn’t bypass the credentials check that it is entitled to access that image, by using a locally cached version.

# Image Trust and Supply Chain

We have discussed how to specify the correct version of an image in your YAML files, but a potential problem still remains: ensuring that the version pulled from the image registry is the genuine, intended code. Several projects aim to help with the problem of ensuring the provenance of the application software running in a deployment:

- The [TUF](https://theupdateframework.github.io/) project, and its implementation [Notary](http://bit.ly/2IpFN2i), use signing to ensure the integrity of an image—that is, to make sure that the image retrieved from a registry at deployment time is the correct version as signed by a trusted authority. The [Portieris admission controller](https://github.com/IBM/portieris) can prevent images from being deployed if they don’t have a valid Notary signature.
- [Grafeas](https://grafeas.io/) is another approach to storing and assuring image metadata, including signatures to validate image integrity.
- The [in-toto project](https://in-toto.github.io/) provides a framework to protect the integrity of the components installed into an image, and the tests they have passed.
- Commercial security solutions can also add validation that the image being deployed is a precisely approved version that matches your policies.

In a high-risk environment, you will want to explore tools like these for validating image provenance.

# Minimizing Images to Reduce the Attack Surface

Following the principle of [“Limiting the Attack Surface”](ch01.html#principle_attack_surface), you can take it as a general rule that the smaller the image, the smaller the attack surface:

- By minimizing the amount of code you include in the image, you can reduce the likelihood of a vulnerability.
- There is rarely a good reason to include an SSH daemon, as [explained by Jérôme Petazzoni](http://bit.ly/2OULB6I).
- Along similar lines, other utilities in your images may not be required by the application code. Excluding them will make the running container less useful to an attacker who manages to compromise it. For example, suppose that a container has access to database credentials that it accesses by reading from a secrets file (see [Chapter 7](ch07.html#ch_secrets)). If the container image doesn’t include utilities like `cat` or `more`, it will be that much harder for attackers to read the credentials even if they gain access to the running container. If the image doesn’t even have a shell (like `sh` or `bash`) included in the image, this will make an attack even harder.
- Taking this idea even further, if your application code can be built as a static binary, you can build an image that contains nothing but that binary. This image will have no utilities that an attacker can take advantage of.

As a counterpoint, however, consider that by excluding core tooling such as `cat`, troubleshooting will also be hard for you, so you want to aim for a sensible trade-off here.

To learn more about reducing image sizes, see [Abby Fuller’s talk on reducing image sizes](http://bit.ly/2xECjVF). For more information on building secure container images, check out the resources on the accompanying website, in the [“Securing Your Container Images”](http://bit.ly/2R0zNkP) section.

As you’ve seen in this chapter, a lot can be done at the image build stage to ensure that the application code is safe to deploy. Next, we turn our attention to Kubernetes security features that apply while code is running.
