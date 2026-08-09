# Chapter 8. Windows Security

**IN THIS CHAPTER**

- **Out-of-the-box operating system hardening**
- **Installing applications**
- **Putting the workstation on the network**
- **Operating Windows safely**
- **The importance of upgrades and patches**
- **Maintaining and testing security**
- **Known attacks against Windows workstations**

Windows security is an important component of the overall security of a network or enterprise. The Windows workstation holds a critical position in a defense-in-depth strategy. [Figure 8-1](ch08.html#defense-in-depth_methodology) illustrates the defense-in-depth strategy.

Defense-in-depth is a general methodology to slow down and obstruct an attacker. Defense-in-depth can also reduce the damage that occurs from an attack or other security incident. Should any one security control (defense) fail, defense-in-depth slows an attacker down by ensuring that there are still more obstacles in the way. This approach might give administrators time to discover and react to the threat. The "onion" shown in [Figure 8-1](ch08.html#defense-in-depth_methodology) has the following layers of protection:

- **Managing users**—The vigilance and security awareness of users can be crucial to all the other security controls being effective.
- **Harden hosts**—Default features are prime targets for attackers and always make the Top 10 on vulnerability lists.
- **Virtual local area network (VLAN) separation**—Trusted but separate; no one aside from payroll personnel and administrators has a need to be able to reach payroll workstations.
- **Server separation**—Provide a place of enhanced security for high-value targets.
- **Wide area network (WAN) separation**—Establish need-to-know or need-to-access criteria between hosts and servers.
- **Customer separation**—Assume that any users and hosts outside of an organization's control are insecure.
- **Internet perimeter**—The Internet contains many threats, but law enforcement finds that most attacks come from the inside.

![Defense-in-depth methodology](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0801.png)

**Figure 8.1. Defense-in-depth methodology**

Defense-in-depth can also serve to discourage an attacker. Attackers will take the path of least resistance. Many attacks are opportunistic. The attacker sees a vulnerability and explores it. In such cases, the attacker will pursue the attack until resistance is met. If the attacker then senses that there will be little resistance (no defense-in-depth), this provides motivation to continue. If, on the other hand, resistance and difficulty are met, the attacker may abandon the attack and seek easier prey.

Defense-in-depth also reduces the number of successful attackers. With defense-in-depth, the attacker must be knowledgeable and able to execute several attacks. This requirement eliminates the threat from the largest group of attackers, *script kiddies*. Script kiddies are generally recognized as immature, anarchist hackers who acquire tools developed by knowledgeable hackers. The script kiddies could not develop these tools or even execute the attack manually. However, they are capable of running the tools and causing damage. Most of these tools target a single vulnerability or flaw. Script kiddies are not proficient at stringing tools together, so they are often thwarted by defense-in-depth.

# Windows Security at the Heart of the Defense

All attacks will require that the perpetrator must affect a networked device. In most cases, this device is a host or server. Securing the Windows operating system should be considered as important as any other security control, such as a firewall. Most attackers are after data, which resides on a computer with an operating system. Thus, the operating system is ultimately what is going to be exploited to cause harm to an organization.

Because most work is typically done on the Windows workstation, it is often configured for ease-of-use. There is a natural trade-off between ease-of-use and security. The easier a system or application is to use, the less secure it will be. This trade-off is illustrated in [Figure 8-2](ch08.html#the_trade-off_between_convenience_and_se). If an attacker has made it as far as a user's Windows machine, there is a good chance the attack will be successful.

![The trade-off between convenience and security](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0802.png)

**Figure 8.2. The trade-off between convenience and security**

## Who would target an organization?

If you have chosen to make Windows your dominant platform, you can count yourself among the vast majority of computer users. According to some reports over 90 percent of all systems run some variant of Windows. That in itself means you may be a target because attackers know if they can find a way to compromise a Windows system, there are a large number of targets to go after.

When you purchase your Windows product, it will most likely do what you want it to do. Overall, the purchase will be a pleasant experience, and this is a great business approach for Microsoft.

Another good business move by Microsoft is to make the product very easy to install. Windows requires very little information for the initial installation. Older versions of Windows 95 and Windows NT required some technical knowledge for selecting options, but the newer versions of Windows require less knowledge about how computers work while installing. In addition, most laptops and desktop systems come with the operating system already installed, meaning it is configured in a default mode. As a result, it has many features turned on to make it easy to use. However, these same features could be used as points of compromise.

Windows features that the user does not use and that don't impact system performance do not, at first, appear to be a problem. In fact, in the vast majority of cases, no thought is given to configuring the operating system after the initial installation. Most users are obliviously happy, having just experienced an easy installation and seeing that the system does everything that they expected.

The security problem is that these circumstances, a very large installation base and a feature-rich default installation, feed right into the hands of the hackers. The hackers purchase and install the very same Windows as their future victims. They know that if they find a vulnerability, they will have potentially millions of workstations to try to exploit. The hackers also know that most users will settle for the default installation of Windows, leaving most features enabled.

This situation all leads up to Windows being the most targeted operating system for hackers. It is a debate in the security community as to which operating systems have the most published vulnerabilities. However, it is agreed that an out-of-the-box installation of Windows will be attacked and compromised in short order, depending, of course, on the network to which it is attached.

## Be afraid...

It is a dangerous and cruel world out there. Most of us seek out safe havens in our communities, at home, and at work. However, we still lock our cars and our front doors.

Consider your Windows workstation an entry point for the outside world to get into your safe haven. Consider some of the ramifications of having such easy access to the outside world:

- Credit card data could be stolen and used.
- Private data could be stolen and used for identity theft.
- Private e-mail could be read by strangers or by colleagues at work.
- Pornographic and undesirable material, which would never be allowed in the home or workplace, could be put on the workstation.
- Complete strangers could learn information about your family and children. Such information could lure your children into a "trust" situation.
- Viruses and worms may annoy your friends and colleagues, damaging your personal and professional reputation.
- The Windows system could be used to attack and damage others, perhaps leaving you liable.

You would never let a criminal or con artist into your home to look through private papers. The same level of concern and protection should be extended to a Windows workstation. However on the Internet it is harder to identify attackers, and they often operate in a stealthy manner.

It is common to hear potential victims say, "I have nothing important to lose on that system." That is a false sense of security. Be paranoid and avoid the risk. In addition, even if that statement were true (which is very unlikely — you may not appreciate the value of your information), talk to an attorney about downstream liability and gross negligence. If your system is attacked and used to break into other systems, you could be held liable for the damage because you did not take reasonable measures to protect your system — and due to your negligence, someone else was harmed.

## Microsoft recommendations

Microsoft, on its official Web site at `www.microsoft.com/security/protect`, recommends the following three steps to improving a computer's security:

1. Use an Internet firewall.
2. Get computer updates (run the latest version of the software, including all service packs and patches).
3. Use up-to-date antivirus software.

Microsoft recommends either a hardware or software firewall to "prevent hackers, and many types of viruses and worms, from accessing your computer." Host based intrusion prevention systems (HIPS) can also be used to detect and prevent advanced attacks. This chapter discusses additional ways to protect against these threats.

Microsoft also recommends a daily update using the automatic update feature available in Windows 2003 or later. This chapter will discuss the need to keep all applications updated, as well as some associated steps such as testing and backups.

Microsoft suggests getting antivirus software from Computer Associate, McAfee Security, or Symantec, keeping it up-to-date, and configuring it properly. This chapter further expands on these recommendations.

These are important steps to maintaining the security of a Windows workstation. This chapter will discuss many more steps that can be taken to secure a Windows workstation.

The following recommendations are in support of hardening systems on the network:

- Establish a plan to harden any host that will interact with the outside world, including placing the Windows workstation on a local area network (LAN) or sharing files with other computers. It is most important to develop a procedure that is kept up-to-date. Many points will be learned along the way and it is important that these be noted and incorporated into the procedures. Each time you harden a system, it will not go quickly and smoothly. The task is assumed to take 50 hours. Through the use of security template and group policy objects (GPOs), this process can be scaled.
- Never put an out-of-the-box operating system on a LAN other than a very secure test LAN. Original equipment manufacturers (OEMs) prepare Windows workstations for a wide audience. An organization needs to have systems stripped down to the minimum needed for the business to be done.
- Never put a Windows workstation that has previously been on the Internet on a trusted LAN. Any host that has been unprotected on the Internet for more than an hour should be considered suspect and corrupted. If placed on a trusted LAN, it will pose a risk to all the other workstations. Any Windows system that has been on the Internet, unprotected, should be completely rebuilt before being put into a trusted environment.
- Turn off unneeded ports and corresponding services on the Windows workstation. Numerous tools, such as nmap, are available to check the open ports by scanning from the network. On the Windows workstation, run `netstat -ano` from a command prompt, which will list the open ports.
- Turn off unneeded services on the Windows workstation, even if these services do not open ports onto the network.
- Use the Microsoft update site to determine the recommended patches and upgrades to the Windows operating system.
- Install and maintain a good antivirus application.
- Put personal firewalls on the Windows workstations. This is a good defense-in-depth deterrent for attackers.
- Do not run high-visibility services (Web, mail, file sharing, information sharing— LDAP, FTP) on the Windows workstation without a business case. A review of all such services running should be done to determine their need. Any that are not needed should be shut down or disabled.
- Do not use services that also have reliable secure versions. For example, use SSH for Telnet, IMAP instead of POP3, and secure FTP for FTP.
- Identify mission-critical applications and maintain the security patches and upgrades for these applications.
- Establish a program to scan the Windows workstation periodically to determine what ports are open and why. Optimally, the workstation should be checked quarterly.
- Use strong passwords. Change the password frequently—every 60 days or sooner is recommended.
- Operate safely. Don't open or launch any application that you are not 100 percent sure about. Don't open e-mails from strangers. Don't open any e-mail attachment you do not expect ahead of time. Remove unneeded data and history files from the workstation. Use encryption.
- Watch for performance issues. If metrics are not in place to notice performance, put them in place.
- Run a host-based intrusion detection or prevention system (HIDS or HIPS) on critical Windows workstations. The HIDS will detect unauthorized activity on the host as well as raise the alarm if certain files are changed. The costly part of running an HIDS is the learning curve. Because each site's administrators will manage the site's own HIDS systems, this learning curve is repeated several times. The learning curve continues because the HIDS must be monitored and adjusted on the installed servers. It is expected that the administrators will spend a couple of hours a week working with the HIDS.

# Out-of-the-Box Operating System Hardening

This section examines steps to improve the security of a Windows system, prior to putting the workstation on the network.

## Prior to system hardening

Physically disconnect the workstation from any network. Out-of-the-box installations of Windows are so prominently targeted that a new system can be compromised in a matter of minutes, or even seconds — far too fast for an administrator to harden the system.

If reinstalling Windows on an existing workstation, be certain to back up your data. Back up to external media or to a different hard drive or partition. Most people back up their data files, such as letters and photos. It is also important to capture some other information while the system is still functioning. Consider the following, for example:

- Write down the type of video card and how much memory it has.
- Record the network interface card (NIC) type and any TCP/IP settings. If using wireless, record the service set identifier (SSID) and any encryption keys.
- Check dialup connections for phone numbers.
- Go into the Web browser and save the bookmarked pages.
- Record printer configuration settings.
- Record any types and configurations for other hardware such as sound cards, Web cameras, or scanners.

## The general process of system hardening

No matter which Windows version you are dealing with, the general process for hardening the operating system and workstation is the same. The process is as follows:

1. Assess and understand the role of the Windows workstation to be hardened. This entails understanding the users and their responsibilities. It also involves knowing where on the network the workstation will be placed.
2. Acquire hardening procedures for other Windows workstations that have a similar role. If prior procedures are not available, get a listing of applications and settings on a similar workstation (`winmsd.exe` provides a good starting point). There are many hardening guides available to assist an administrator in the hardening of their operating system. These guides offer an administrator a step-by-step procedure for securing the workstation. They also assist network administrators by offering a repeatable process so that steps are not missed.
3. Install a clean version of the operating system; then document the changes and burn a ghost image.
4. Remove some services that are not required; then document the changes and burn another ghost image.
5. If at any point, the system becomes unusable, which should be expected, drop back to the most recent ghost image and try again. However, this time, do not remove the service the removal of which in step 4 caused the problem.
6. Remove any extra applications that may have been loaded with the Windows operating system, and then document the changes and burn another ghost image.
7. Check and close any ports that are not explicitly required for performing the mission of this workstation. Open ports can be detected by opening a command prompt window and running `netstat -ano`. Any protocol listed in the results that shows a status of "LISTENING" has an open port.
8. Locate and close any shares that are not explicitly required by the role that this workstation will have. Open shares can be listed by opening a command prompt window and running net share. This will list the share name and the resource (folder) being shared. You can disable sharing through the Windows Explorer by clicking on the properties of the folder.
9. Install only the needed applications, document the changes, and burn a final ghost image.
10. Install a personal firewall on the Windows workstation.
11. Thoroughly test the system.

It is important to document every step of the system hardening for both successes and failures. If failures occur, usually in the form of the system crashing or hanging, it is important to know exactly what was done so the procedure can be altered. The most common failure will be a result of a needed service having been disabled or removed.

It is also important to document the case when the system hardening goes successfully. A detailed procedure for how to harden a system for a particular organization or user will be very useful when adding future systems to the inventory. A Web search will produce a number of sets of procedures for hardening various Windows operating systems. Many colleges and universities provide this information, primarily trying to reach their student population, but they make the information available to the public in the process.

By now, you should see the need to have frequent ghost or binary images. The relatively short delay taken to burn a ghost image will be more than recouped the first time the system crashes and needs to be rebuilt. The ghosting application makes a compressed snapshot of the partition on the hard drive. This snapshot or image can either be burned to a CD-RW disk, or put on another hard drive partition.

It is important to thoroughly test the system once it has been hardened. The final configuration is, in all likelihood, not one that has been tested by Microsoft. In fact, the combination of services and applications needed might be unique to your organization.

You can obtain a list of Windows services using the `net` command. The following results from opening a command prompt and running `net start`:

```
Alerter
   Automatic Updates
   COM+ Event System
   Computer Browser
   DHCP Client
   Distributed Link Tracking Client
   DNS Client
   Event Log
   IPSEC Policy Agent
   Logical Disk Manager
   Messenger
   Network Connections
   PGPsdkService
   PGPService
   Plug and Play
   Print Spooler
   Protected Storage
   Remote Access Connection Manager
   Remote Procedure Call (RPC)
   Remote Registry Service
   Removable Storage
   RunAs Service
   Security Accounts Manager
   Server
   System Event Notification
   Task Scheduler
   TCP/IP NetBIOS Helper Service
   Telephony
   VMware Tools Service
   Windows Management Instrumentation
   Windows Management Instrumentation Driver Extensions
   Workstation
The command completed successfully.
```

WMIC is also a great tool to find out this information.

## Windows vulnerability protection

This section serves as an overview of the technologies that are provided by the security industry to protect a Windows machine against as-yet-unknown vulnerabilities. These technologies do not include automated system patching or firewall protection. The main focus of this overview is on technologies that can prevent vulnerabilities, in either the operating system or software running on the system, that are as yet unknown. These are technologies built to monitor a system for certain "symptoms" that might alert the user to a vulnerability in progress or prevent a vulnerability from being exploited.

### Off-the-shelf Products

Some of the most common off-the-shelf protection products are as follows:

- **Symantec-Norton Internet Security**—This software has five pieces —antivirus, firewall, "privacy control," anti-spam, and parental controls. The software will scan your computer and report back all the software installed on the machine that has the ability to access the Internet. You then have the option to allow or disallow certain pieces of software. An intrusion detection system is also linked to the firewall. This system will alert you to an attack on your machine. The privacy control option says it will "prevent inadvertent sending of confidential data, such as credit card numbers, onto the Internet." It focuses much more on Internet security, rather than vulnerabilities being exploited. However, this is somewhat expected for a home user, and a product targeted for a home computer.
- **Symantec Client Security**—This software is another off-the-shelf product that is targeted more toward enterprises than home offices or small businesses. Again, this software is made for the client machine, and includes most of the features in the "Internet Security" software for the home with one major addition: Generic Exploit Blocking. This technology is used to create "fingerprints" of vulnerability attacks. Generic exploit blocking analyzes the targeted vulnerable software rather than the attacking viruses. The key is that a signature or fingerprint is created, not for the virus of attacking software, but rather for actions taken by that virus to exploit the vulnerability. In the Symantec example, the vulnerability discussed is MS SQL server:*The need for this technology was established when Microsoft announced a vulnerability in Microsoft SQL Server database. To exploit the vulnerability, an attacker simply had to send a packet that was 61 bytes or longer, and whose first byte had a value of 4, to network Port 1434 on an unpatched machine running SQL Server. A generic exploit-blocking signature for this vulnerability would have blocked the threat*.

While this analysis is becoming faster every day, it still requires human interaction and the updating of the firewall to protect against this signature of an attack.

- **McAfee-Internet Security Suite**—This is designed to go on the home user's computer and protect it from Internet threats. It includes standard things such as antivirus and anti-spam. These capabilities are almost the same as for the Symantec software. The only proactive technology to detect and prevent vulnerability exploitation is one called WormStopper. This technology monitors mass e-mailings looking for viruses.
- **McAfee System Protection-McAfee Entercept Server and Desktop Agents**—This product has a key technology, Zero-day attack prevention and buffer overflow exploit prevention. The technology to prevent buffer overflow exploits is patented (patent number *6,301,699* at `http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=/netahtml/srchnum.htm&r=1&f=G&l=50&s1=6301699.WKU.&OS=PN/6301699&RS=PN/6301699`). The patent, like most, is a bit confusing but basically the strategy applies a threshold value to each buffer and then analyzes what is placed in that buffer looking for jump instructions. This type of a technology would prevent buffer overflow exploits before they are even known. Quoting from the patent:

> *In accordance with the present invention, there is thus provided a method for detecting buffer overflow weakness exploitation, including the steps of determining at least one threshold parameter, where each of the threshold parameters is respective to a buffer overflow weakness exploitation event, analyzing a code to be executed, thereby producing at least one validation value, comparing the validation values to the respective ones of the threshold parameters, and determining a buffer overflow weakness exploitation attempt, when at least one of the validation values exceeds the respective one of the at least one threshold parameters*.

### Academic technologies/ideas

There are a few main approaches in academia to buffer overflow prevention/detection. They range from relocating information, to using canary values, to adding system calls to the operating system. Most of these ideas are purely theoretical and not usually implemented for a number of reasons. The biggest reason is that of performance, both in actual run time, and in setup. For example, any prevention mechanism that makes use of a compiler modification will require all code running on the machine to be recompiled. This is a long and tedious process, and usually not available to people using Windows because the source code is often not released to the general public. Listed next are the main areas of buffer overflow prevention.

#### Rearranging stack data locations

This focuses on rearranging information in memory so that when the overflow occurs no damage can be done to the system. There are a number of tools and compiler modifications that accomplish this task. The basic idea is to rearrange the information on the stack so that overflowing a buffer will not allow the attacker the ability to overwrite the return address.

This same basic idea can be adapted to work with the heap as well. It should be noted that a lot of the solutions posted later in this section do not even address the heap because heap-based attacks are less common and much harder to launch.

One method for prevention using this approach can be found in a paper titled, "A Methodology for Designing Countermeasures Against Current and Future Code Injection Attacks," by Younan, Joosen, and Piessens. Their countermeasures work by rearranging the stack, heap, and data segments of memory. From the paper, here is a brief description of how this is accomplished:

> *Firstly, we must modify the way the stack is organized: The control data must be separated from the regular data. To do this we suggest making three stacks: one stack which contains the return addresses (this is the regular stack and can still take advantage of the call and ret instructions). A second stack contains the frame pointers, local pointers and arrays of points. Finally, a third stack contains the other data*.
> 
> *Secondly, dynamically allocated memory must have its memory management information stored out-band. To accomplish this its management information is stored at the beginning of the heap-section in a hash table. The actual dynamically allocated memory simply contains the user-allocated memory*.
> 
> *Finally, the memory in the data segment must be organized in a different order. The ctors and dtors sections would be stored first, followed by the Global Offset Table and the exception handling frame, which are followed by pointers, regular data, arrays of pointers and finally normal arrays*

There have been other approaches to modifying the layout of the data in the stack, heap, and data segments to prevent buffer overflows from doing any damage. However, the key is that none of these approaches actually prevents buffer overflows from occurring. An attacker can still write too much data to a segment of memory corrupting the memory next to it. The only difference now is that the memory next to it will not have control flow information in it. However, what if the memory next to it contained the file name, or worse yet the permissions of the file to be written to? Damage can still be done.

Also these methods are impossible to implement on a Windows system without the consent of Microsoft. While you could possibly create a compiler for Windows from scratch and implement these ideas, software that wasn't compiled with the new compiler would still be susceptible to attacks.

#### Adding System Calls to the Operating System

The idea for adding a system call to the operating system is simple: allow the program to query the operating system as to how much memory there is at a certain address.

This idea was first published in a paper titled, "Making the Kernel Responsible: A New Approach to Detecting & Preventing Buffer Overflows." The idea is summed up in the abstract of the paper, as follows:

> *This paper takes the stance that the kernel is responsible for preventing user processes from interfering with each other, and the overall secure operation of the system. Part of ensuring overall secure operation of the computer is preventing buffers in memory from having too much data* *written to them, overflowing them. This paper presents a technique for obtaining the writable bounds of any memory address. A new system call for obtaining these bounds*, *`ptrbounds`*, *is described that implements this technique. The system call can be used to detect most buffer overflow situations. Once an overflow has been detected it can be dealt with in a number of ways, including to limit the amount of information written to the buffer. Also, a method for accurately tracking the allocation of memory on the stack is proposed to enhance the accuracy of the technique. The intended use of* *`ptrbounds`* *is to provide programmers with a method for checking the bounds of pointers before writing data, and to automatically check the bounds of pointers passed to the kernel*.

While this idea is novel and inventive, it has some very large practical problems for actually implementing it. The biggest is, again, that it cannot be implemented in the Windows operating system because it would require adding a system call to the OS and other extreme modifications. Because Windows is a closed source, these modifications would be impossible to implement. However, it should be noted that this solution also provides protection to the stack, heap, and data segments.

#### Use of Canary Values to Indicate Changes

The use of a canary value to monitor the size of buffers is a classic solution to the problem. The idea is simply to place a particular value at the end of each buffer, or in the case of the stack, just before the return address. This way if a buffer were to overflow, the canary value would be overwritten and indicate that a buffer overflow has occurred.

The obvious problem with this is that the canary value must be kept secret or else the buffer that is overflowing can simply replace this value as it overflows. To prevent this from occurring a random number generator is usually used. This will prevent the most straightforward attack, but implementation attempts in Windows have failed. The Windows canary value protection scheme is defeated by leveraging the exception handling mechanisms built into the code. The following excerpt from the paper entitled, "Defeating the Stack Based Buffer Overflow Prevention Mechanism of Microsoft Windows 2003 Server," by Litchfield gives a brief overview of the situation:

> *Currently the stack protection built into Windows 2003 can be defeated. I have engineered two similar methods that rely on structured exception handling that can be used generically to defeat stack protection. Other methods of defeating stack protection are available, but these are dependent upon the code of the vulnerable function and involve overwriting the parameters passed to the function*.

While this type of an approach has merit, there are some shortcomings. The first is that this new canary checking code must be inserted into all the code running on the system. This requires recompiling the source code, which, as explained before, is a huge hurdle in the Windows world. Finally, this method only protects the stack, and does not prevent an overflow from occurring, but rather just notices when one has occurred.

#### Use of safer library calls

This is one of the more promising and easier-to-implement ideas. It is simply a re-engineering of the library calls that most people use improperly. These are usually string manipulation calls such as `sprintf` and `strcpy`. Some of the methods walk back through the stack, to see how much space is left in the activation record for local variables. The function then will copy characters until a null character `'\0'` has been reached, or until the amount of memory left on the stack for this function has been used up. This method is very good; however, it does not prevent a buffer overflow from occurring. One buffer can still write data into another buffer. This method just prevents the overwriting of one buffer to have negative consequences on the system — it stops it from overwriting the return address.

Other library call replacements just dynamically allocate the memory that is needed for the amount of data. These replacement calls cannot be exact replacements because it is impossible to reallocate memory on the stack. So, for example, if the `strcpy` function were passed the address of a buffer on the stack, and a new library version attempted to free that memory and then create new memory on the heap, changing the pointer, the program would crash when it attempted to free the pointer to the stack. Instead, a whole new string library, or string class in the case of C++, is created that will do all the dynamic allocation of memory for you, without the user ever knowing. One such library is already part of the C++ standard, STL's string class.

## Windows 2003 New Installation Example

Here is an example of a typical out-of-the-box installation of Windows 2003 Enterprise Edition. No special features were installed. This was the baseline installation, and the workstation might be used for anything from simply a word processing station to an Internet gaming workstation. Six ports were found open on the newly installed system using nmap and nessus. Scanners found the following information:

```
The 65530 ports scanned but not shown below are in state: closed
Port       Service
135/tcp    loc-srv
137/udp    netbios-ns
139/tcp    netbios-ssn
445/tcp    microsoft-ds
1025/tcp   NFS-or-IIS
1026/tcp   LSA-or-nterm
```

The following list breaks down the port information discovered during the scan in detail:

- **Port 135 - loc-srv/epmap**—Microsoft Data Circuit-Terminating Equipment (DCE) Locator service aka end-point mapper. It works like Sun Remote Procedure Call (RPC) portmapper, except that end points can also be named pipes. Microsoft relies upon DCE RPC to manage services remotely. Some services that use port 135 of end-point mapping are Dynamic Host Configuration Protocol (DHCP), Domain Name System (DNS), and Windows Internet Name Service (WINS) servers. The remote host is running a version of Windows that has a flaw in its RPC interface, which may allow an attacker to execute arbitrary code and gain SYSTEM privileges. An attacker or a worm could use it to gain the control of this host. Note that this may not be the same bug as the one described in MS03-026, which fixes the flaw exploited by the MSBlast (or LoveSan) worm. DCE services running remotely can be enumerated by connecting on port 135 and doing the appropriate queries. An attacker may use this fact to gain more knowledge about the remote host. The scanners provide the following additional information:Solution: see `www.microsoft.com/technet/security/bulletin/MS03-039.asp`Solution: see `www.microsoft.com/technet/security/bulletin/MS03-026.asp`
- **Port 139 - NetBIOS Session (TCP)**—Windows File and Printer Sharing. A Server Message Block (SMB) server is running on this port. This is the single most dangerous port on the Internet. All File and Printer Sharing on a Windows machine runs over this port. About 10 percent of all users on the Internet leave their hard disks exposed on this port. This is the first port hackers want to connect to, and the port that firewalls block.
- **Port 139 - NetBIOS Session (UDP)**—The remote host is running a version of the NetBT name service that suffers from a memory disclosure problem. An attacker may send a special packet to the remote NetBT name service, and the reply will contain random arbitrary data from the remote host memory. This arbitrary data may be a fragment from the Web page the remote user is viewing, or something more serious, such as a POP password or anything else. An attacker may use this flaw to continuously poll the content of the remote host's memory and might be able to obtain sensitive information.
- **Port 445**—SMB in Windows 2003. Microsoft has created a new transport for SMB over TCP and UDP on port 445. This replaces the older implementation that was over ports 137, 138, and 139. However, port 139 is still left open on a new installation. A Common Internet File Systems (CIFS) server is running on this port. It was possible to log into the remote host using a NULL session. The concept of a NULL session is to provide a null username and a null password, which grants the user the guest access. The computer name of the Windows 2003 host was determined through the null session running on this port. This is potentially dangerous as it may facilitate the attack of a potential hacker by giving him extra targets to check for. The scanners provide the following additional information.To prevent null sessions, see MS KB Article Q143474 (NT 4.0) and Q246261 (Windows 2000). Note that this won't completely disable null sessions, but it will prevent them from connecting to IPC$.
- **Port 1025**—This is the first dynamically assigned port. Therefore, virtually any program that requests a port can be assigned one at this address. A DCE service is listening on this port. Here is the list of DCE services running on this port:UUID: 12345678-1234-abcd-ef00-0123456789ab, version 1, Endpoint: ncacn_ip_tcp:192.168.1.12[1025] Annotation: IPSec Policy agent endpointUUID: 12345778-1234-abcd-ef00-0123456789ac, version 1, Endpoint: ncacn_ip_tcp:192.168.1.12[1025]
- **Port 1026**—This is a dynamically assigned port. Therefore, virtually any program that requests a port can be assigned one at this address. Nmap reports that either a Local Security Authority (LSA) server or the nterm application is running. Here is the list of DCE services running on this port:UUID: 1ff70682-0a51-30e8-076d-740be8cee98b, version 1, Endpoint: ncacn_ip_tcp:192.168.1.12[1026]UUID: 378e52b0-c0a9-11cf-822d-00aa0051e40f, version 1, Endpoint: ncacn_ip_tcp:192.168.1.12[1026]UUID: 0a74ef1c-41a4-4e06-83ae-dc74fb1cdd53, version 1, Endpoint: ncacn_ip_tcp:192.168.1.12[1026]

This example illustrates the inherent problem with out-of-the-box installations of Windows systems. This system was not intended to be used for file sharing or serving up DHCP, NFS, IIS, LSA, or nterm. Yet, apparently, ports are open for these or similar applications.

## Windows Quick-start Hardening Tips

This section will cover a list of security vulnerabilities that organizations can start fixing today. It is not meant as a replacement for full hardening but focuses on the first things an organization can do to fix a majority of the vulnerabilities that are often compromised. Following are several things to note:

- Every change should be thoroughly tested and validated before it is made to a system.
- A prioritized list of all servers should be created in order to ensure the security vulnerabilities are fixed in a timely manner.
- A notebook should be kept for each server and any change that is made to a server should be clearly documented and recorded in the book. All servers should be kept at a common revision level.
- All changes should be done through the change control board.

The following is a partial list of some of the vulnerabilities that organizations can start to fix across all of their key servers:

- All appropriate patches and service packs should be applied to each server.
- Remove file and print sharing from network settings.
- Perform port blocking at the network setting level.
- Change all administrative and system passwords to be strong passwords.
- Disable unneeded services.
- Remove unneeded Windows components.
- Create, test, and run a security template against key systems.

### Apply patches and service packs

Many servers typically do not have the latest patches applied at both the operating system and application level. Security patches resolve known vulnerabilities that attackers can exploit to compromise a system. Whenever a patch is released, it should be analyzed, tested, and applied in a timely manner.

Checks and balances should be put in place so that when a new patch is released it is applied across all servers in a consistent and timely manner. It is recommended that a weekly report be produced stating which patches were released and when they are going to be applied to each server. Also, any patches that are older than 30 days and have not been applied should be highlighted with an explanation.

### Remove file and print sharing

File and print sharing could allow anyone to connect to a server and access critical data without requiring a user ID or password. It is critical that any unnecessary network drivers are removed from the system. [Figure 8-3](ch08.html#a_vulnerable_configuration) shows how a system is typically configured and is vulnerable. [Figure 8-4](ch08.html#as_configured_from_a_security_standpoint) shows how it should be configured from a security standpoint.

![A vulnerable configuration](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0803.png)

**Figure 8.3. A vulnerable configuration**

![As configured from a security standpoint](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0804.png)

**Figure 8.4. As configured from a security standpoint**

Secure configuration should be performed on all stand-alone servers and domain servers, after which critical functionality should be validated.

### Port Blocking

Defense-in-depth is a critical principle of network security. It is important that multiple levels of protection be implemented across an organization's systems. Additional ports can be open on a server that provides an avenue for someone to compromise a system. While port filtering is typically performed, it is critical that port blocking be applied to all critical servers. For each server, an analysis should be performed on which ports need to be open and access to all other ports should be restricted.

[Figure 8-5](ch08.html#no_port_blocking_performed) shows an example of no port blocking being performed, which creates a security vulnerability across the system. [Figure 8-6](ch08.html#configuration_with_port_blocking) shows configuration to allow only the critical ports that are needed for the server to function properly.

The UDP and IP protocols setting can probably be applied to most servers, but the TCP settings need to be adjusted on a server-by-server basis. Third-party software such as McAfee can also be used to provide port blocking across key servers.

![No port blocking performed](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0805.png)

**Figure 8.5. No port blocking performed**

![Configuration with port blocking](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0806.png)

**Figure 8.6. Configuration with port blocking**

### Implement strong passwords

For every privileged account that is needed on the system, the password should be changed to a 15-character password that is not based on a dictionary word and that has letters, numbers, special characters, and invisible (CTRL^) characters interspersed throughout the password. Tracking should be performed so that all passwords are changed every 90 days.

### Disable unneeded services

Most servers typically contain default installs of the operating systems. A default install contains extraneous services that are not needed for the system to function and represents a security vulnerability across the system. Therefore, it is critical that all unnecessary services be removed from the system.

### Remove Unneeded Windows Components

In addition to installing additional services, Windows also installs additional windows components. Any unnecessary Windows components should be removed from critical systems to keep the servers in a secure state.

[Figure 8-7](ch08.html#component_installation_options_for_windo) shows an example of what components should be installed for a Web server. [Figure 8-8](ch08.html#configuration_options_for_accessories_an) shows the options for accessories and utilities. [Figure 8-9](ch08.html#configuration_options_for_internet_infor) shows configuration options for Microsoft Web server IIS.

![Component installation options for Windows](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0807.png)

**Figure 8.7. Component installation options for Windows**

![Configuration options for Accessories and Utilities](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0808.png)

**Figure 8.8. Configuration options for Accessories and Utilities**

![Configuration options for Internet Information Services (IIS)](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0809.png)

**Figure 8.9. Configuration options for Internet Information Services (IIS)**

### Run Security Template

A security template allows a consistent configuration to be used to test the security of a server and/or to directly make those changes to the server. It is recommended that the template be used just to analyze the server and that any settings not compliant be manually changed on the system. While the template can be automatically applied, it is not recommended because this could cause the system to operate incorrectly. Templates can be downloaded from the Internet. A good resource for securing Windows systems is the Center for Internet Security, which can be found at `www.cisecurity.com`.

It is critical that servers are not only properly secure, but that they are kept consistent from a configuration management standpoint. However, it is recommended that a table be created and that all changes be performed in a consistent, documented manner across the systems. There can be a problem if changes are made to servers in an inconsistent manner. While the initial intent may be to secure the server, if every server stays in a different state it will be impossible to manage a large number of servers, all of which are configured differently. Therefore, it is recommended that in the future all changes be clearly documented, tracked, and implemented across all servers.

## Specifics of system hardening

The following list itemizes more specific recommendations that can improve the security of a Windows workstation:

- Enable the built-in Encrypting File System (EFS) with NTFS or BitLocker on the appropriate version of Vista and 2008.
- Remove Enable LMhosts lookup.
- Disable NetBIOS over TCP/IP.
- Remove ncacn_ip_tcp.
- Set MaxCachedSockets (REG_DWORD) to 0.
- Set SmbDeviceEnabled (REG_DWORD) to 0.
- Set AutoShareServer to 0.
- Set AutoShareWks to 0.
- For NullSessionPipes delete all value data INSIDE this key.
- For NullSessionShares delete all value data INSIDE this key.
- If the workstation has significant random access memory (RAM), disable the Windows swapfile. This will increase performance and security because no sensitive data can be written to the hard drive.
- Set specific users to have access to shared folders. This will prevent other users (except administrator) from accessing the shared folder.
- Set the number of users allowed to access the shared folder to a reasonable number. If the folder is intended to be accessed by only one user, set the number of users to 1.
- If encryption of folders content is available (as in XP Professional version), use it.
- Apply appropriate Registry and file system ACLs.
- Protect the registry from anonymous access.
- Display legal notice before the user logs in.
- Set the paging file to be cleared at system shutdown.
- Set strong password policies.
- Set account lockout policy.
- Enable auditing of failed logon attempts and privilege requests.
- Secure LDAP features.
- Remove exploitable sample data from IIS.

### Do not use AUTORUN

Untrusted code can be run without the direct knowledge of the user. In some circumstances an attacker can put a CD into the machine and cause his own script to run.

### File permissions

Another important, and often overlooked, security procedure is to lock down the file-level permissions for the server. By default, Windows does not apply specific restrictions on any of the local files or folders. The Everyone group is given full permissions to most of the machine. To harden the operating system, this group must be removed and only the proper groups and users be given specific access to every file and folder in the operating system.

### The Registry

Although changes to Windows are done with the Graphical User Interface (GUI), the changes are really just made in the Registry. Many functions that the Registry performs cannot be manipulated through the Windows GUI. It is essential that the administrator take the time to thoroughly understand how the Registry functions and what functions the different hives and keys perform. Many of the vulnerabilities found in the Windows operating system can be fixed by making changes to specific keys.

### File allocation table security

Microsoft Windows has many of its security features enabled out-of-box, but because of the variety of network scenarios, most of its security features are inactive at the time of install. One of the primary security features that Windows offers, unique in Microsoft environments, is its file allocation table, New Technology File System (NTFS), which allows for file-level permissions. Many administrators do not implement this format on their servers; it is inaccessible from DOS, making certain recoveries more difficult and time consuming. An administrator's first line of defense is to verify that every Windows server is formatted with NTFS and that the proper permissions have been applied.

### User groups rights

After the files have been locked down, user rights need to be established for the different groups in the organization. Windows has a built-in logic on what rights each group should have. Standard groups include the following:

- Users
- Domain Administrators
- Power Users
- Backup Operators

Users should be strategically placed in specific groups depending on their job needs. However, it is recommended that users not be placed in any pre-made group. New groups with specific rights should be created for users based on their specific job needs. Administrators can keep tighter controls on their networks' user permissions infrastructure if it is created specifically for the organization. A common way of designing groups is by department. Users in specific departments tend to perform the same job duties, requiring that they all have the same rights. For example, by placing everyone in the marketing department into the marketing group, it will be easier for the administrator to keep the current employee list accurate in the system. Also, verify that only domain administrators have the right to log on locally to any machine in the server environment. This will ensure that even if users obtain physical access to the machine, they will not be able to locally log on to the machine.

### Create or edit user level accounts

Caution must be taken to avoid users having passwords that never expire. This setting will lower the security level, giving an attacker unlimited time to guess the password, and an unlimited amount of time to use the password once it is uncovered. Also, accounts where the user has established an account but never logged on should be eliminated. These accounts are frequently created with standard passwords and may give unauthorized access opportunities to an attacker. All user accounts should be checked regularly to ensure that some have not expired.

If not done during installation, create user accounts so that the administrator account does not need to be used for normal work. If an account other than Administrator was set up during the installation, check that it is not an administrator account. If needed, reset the account to Restricted User. Do not use the same password for restricted accounts as for the administrator account.

For each user, set the following:

- Users must enter a username and password to use this computer
- Maximum password age — 90 days
- Minimum password age — 2 days
- Minimum password length — 15 characters
- Password must meet complexity requirements — Enable
- Store passwords using reversible encryption for all users in the domain — Disable
- Account lockout threshold —3 invalid logon attempts
- Account lockout duration — 90 minutes
- Reset account lockout counter after — 45 minutes
- Audit account logon events — Success, failure
- Audit account management — Success, failure
- Audit logon events — Success, failure
- Audit object access — Success, failure
- Audit policy change — Success, failure
- Audit system events — Success, failure

Using the net command, the administrator can check the values of some key parameters. The following information is available by opening a command prompt and running `net account`:

```
Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          42
Minimum password length:                              0
Length of password history maintained:                None
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
Computer role:                                        WORKSTATION
The command completed successfully.
```

The following information is available by opening a command prompt and running `net localgroup`:

```
Aliases for \\RISKY_SYSTEM
--------------------------------------------------------------------------
*Administrators           *Backup Operators         *Guests
*Power Users              *Replicator               *Users
The command completed successfully.
```

### Use good passwords

Good passwords are key to protecting a Windows workstation. Passwords will initially be set when installing the operating system. However, passwords should be changed frequently as the Windows system is operated. Some key features of good passwords are as follows.

- The password should be at least 15 characters long, containing letters (upper and lower), numbers, and special marks (such as !"# %&/()).
- Never use the same password in two places or systems.
- Do not use simple or obvious passwords that may be easy for an attacker to guess.

### Note

A detailed discussion of password security for Windows is presented in the section "[Operating Windows Safely](ch08.html#operating_windows_safely)," later in this chapter.

## Securing the Typical Windows Business Workstation

As discussed earlier, Windows is a general operating system. However, the typical workstation user does not need a general computing device.

The typical business Windows workstation user needs a computer to do the following:

- **Word processing and office productivity** — This is a key use of computers on the typical workstation. Word processors or text editors, presentation applications, spreadsheets, and simple database tools are the common office suite. To harden Windows for using these applications, be sure to disable macros.
- **E-mail** — Only the e-mail client is generally needed. The Windows workstation is at risk for a number of additional vulnerabilities if the user decides to run a mail server, as well. When hardening the workstation, be sure to use a virus protection application. If possible, the workstation should be set up to use Secure Shell (SSH) and port forwarding when getting and sending e-mail. In this way, the traffic will be encrypted and not subject to being sniffed on the LAN.
- **Web browsing** — Users should be instructed not to download questionable applications.
- **Occasional file transfer** — If downloading a file, only turn on the transfer capability for the short period of time it is needed. Train the user not to pull questionable files.
- **File sharing** — Use a file server to share files. Use antivirus and pest control tools on the file server. (Pest software is generally something that alters the user's workstation in a manner that is unwanted and annoying. The typical example is when irritating pop-up ads persist despite all efforts by the user to close them.)

Word processing, e-mail, Web browsing, and file transfer do not require outsiders to gain access to the Windows workstation. Therefore, the personal firewall on the Windows workstation could be set to block all outside access.

File sharing does require that outsiders have access to the workstation. This would require access through the personal firewall on the Windows workstation. To avoid having to open up access to the Windows workstation, file sharing should not be done directly to a file server.

## Securing the Typical Windows Home System

The typical home Windows workstation is similar to the business workstation, but introduces an added risk. Home users run applications such as games that can be an uncontrolled means of introducing malcode onto the workstation. *Malcode* (also known as malicious logic) consists of hardware, software, or firmware that is intentionally included or inserted in a system for a harmful purpose. Some forms of malcode include logic bombs, Trojan horses, viruses, and worms. Three cases exist for a home workstation:

- The games are all purchased from trusted sources (such as shrink wrapped in a major computer chain). The software can be considered safe to put on a workstation that is exposed to a trusted LAN. It is safe to have this gaming workstation. When no longer used for gaming, it is recommended that this workstation be rebuilt with a new operating system. Games are notorious for interfering with an operating system. This interference is manifested in applications not working together smoothly. The security concern is that any abnormal operating system configuration is a security risk. The security controls put in place to protect a system may not be valid if the operating system has been subtly altered due to a game installation.
- The gaming software is acquired from sources that cannot be verified. Such software should be considered questionable and risky. This gaming workstation needs to be isolated. Ultimately, this workstation should be considered compromised and not trusted to interact with any trusted LANs. The workstation should be disconnected from any untrusted LAN. Because most homes have only one connection to the Internet, this usually means that the gaming workstation should not be connected to the Internet. It would be safe to connect this workstation to the Internet on a LAN of its own. Again, caution should be taken not to permit any personal or private data on this workstation. When no longer used for gaming, this workstation should not be connected to a trusted network, without the operating system being completely re-installed.
- If the gaming workstation must be connected to the Internet (due to the nature of the games), the workstation should be used *only* for gaming. No private data should be put on the workstation. The workstation's operating system should be rebuilt frequently (approximately every three months or when switching to new games). Under *no* circumstances should this workstation be later connected to a trusted network, without the operating system being completely re-installed.

# Installing Applications

After the operating system has been hardened, it is time to install the applications needed for the particular mission intended for this workstation. For security reasons, the applications on the Windows workstation are limited to the minimum needed to perform the user's mission. This is a simple matter of reducing the exposure or risk by removing a potential avenue of attack.

## Antivirus protection

A virus is a computer program embedded in another program or data file. The virus is designed to copy itself into other files whenever the infected file is opened or executed. In addition to propagating itself, a virus may perform other tasks, which can be as benign as changing colors on the computer screen, or as malicious as deleting all files on a hard drive. Once a user's computer has been infected with a virus, it can be very difficult to isolate the virus and eradicate it. Often a user's eradication efforts are focused on the symptoms caused by the virus and miss the virus code itself.

Viruses and worms spread using means normally available on a workspace or home LAN. Some examples of how a virus spreads are as follows:

- **On bootable CDs and USB drives as they are transported from machine to machine** — Users constantly share and move information between systems.
- **Through file shares** — An example of this is the W32NetSky virus that duplicates itself in numerous files on every open share.
- **Through e-mail attachments** — If a user opens or launches an attachment containing a virus, it can spread by sending out more e-mails, or by using any of the other methods in this list.
- **By downloading files from the Internet** — Files downloaded from the Internet and opened may contain macros or code that starts the spread of a virus or worm.
- **By exploiting a vulnerability in an application** — Once running, the virus or worm can connect to applications running on other Windows workstations. It is then free to exploit a vulnerability. An example of this is SLAMMER, which jumps from host to host, exploiting a SQL database vulnerability.

Virus protection controls should focus on the following:

- **The use of antivirus applications** — Protection against new viruses can be provided by antivirus applications that provide frequent upgrades for virus signatures.
- **Windows configuration** — Virus spread can be stopped by disabling workstation vulnerabilities, such as NetBIOS shares. NetBIOS is discussed in more detail in the "Operating Issues" section of this chapter. A virus can exploit the trust established between two users when a NetBIOS share is set up between workstations.
- **User training and awareness** — Most viruses (as well as worms and Trojan horses) can be stopped in their tracks by an aware user.

This multilevel defense against viruses and worms is shown in [Figure 8-10](ch08.html#protecting_against_viruses_comma_worms_c). Because new viruses and worms are constantly being created, the best protection is to run antivirus software, properly configure Windows, and educate users on safe practices.

With today's threat environment, it is important to have virus protection applications running on all Window systems. Additionally, it is important to have the current version of the antivirus software as well as the current signatures of any viruses. The virus signatures are patterns of bits inside a virus that let the antivirus software detect the virus. The antivirus software relies on periodic updated virus signature files to provide protection against the latest threats. A number of good antivirus products are available today for the Windows workstation.

![Protecting against viruses, worms, and Trojan horses](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0810.png)

**Figure 8.10. Protecting against viruses, worms, and Trojan horses**

With virus protection software, Windows workstations can trap and block viruses before they can spread further. An organization should have protection on every server where people are saving files or storing e-mail messages. The antivirus software should be configured to provide real-time protection as well as routinely scheduled scanning. Without continuous protection, a virus can spread throughout an organization before the next routine scan is scheduled.

By providing users with training on safe Internet practices, many attacks can be stopped even before the antivirus manufacturers have released a new virus signature. Even though a virus attacks an individual workstation, it is a community problem. It is important to have organization-wide antivirus policies, procedures, and standards. If such policies are not effective, valuable data may be destroyed or disclosed without authorization. In addition, unnecessary costs are likely to go unsecured, such as wasted processing resources, the cost to isolate and eradicate the virus, and the cost to restore or recreate the lost data. It is important that all servers and workstations be checked periodically to verify that the latest virus protection software is in place, and that all file servers and e-mail servers are scanned constantly.

## Personal firewalls

A personal firewall is software that runs on the user's workstation and blocks incoming and outgoing LAN traffic.

When used properly, a personal firewall can be much more effective than a perimeter firewall in protecting the user's workstation. With regard to traffic in and out of a user's workstation, the perimeter firewall configuration is usually very general. A properly configured personal firewall can be very specific to a user's need for LAN traffic.

The proper way to configure a personal firewall is to block everything in and out of the workstation. As the user encounters warnings of attempted activity that has been blocked, the user can choose to permit that traffic. In a short period of time, the user will have unblocked the majority of the needed traffic to and from the LAN. The configuration of the personal firewall now represents the user's very specific needs.

## Secure Shell

*Secure Shell (SSH)* secures connections over the network by encrypting passwords and other data. SSH is a program for logging into and executing commands on a remote machine. It is intended to replace rlogin and rsh, and provide secure encrypted communications between two untrusted hosts over an insecure network. X11 connections and arbitrary TCP/IP ports can also be forwarded over the secure channel.

As an authentication method, SSH supports RSA-based authentication. In this method encryption and decryption are done using separate keys, and it is not possible to derive the decryption key from the encryption key. Each user creates a public/private key pair for authentication purposes. The server knows the public key, and only the user knows the private key.

When launched, SSH opens a command prompt window (terminal session) to the other server or host. All traffic generated within that terminal session is encrypted. SSH was first used as a substitute for remote server management via telnet. SSH essentially opens an encrypted telnet session. But the capability to forward ports in SSH has greatly expanded its uses. The use of port forwarding to secure e-mail is described in the section "[Operating Windows Safely](ch08.html#operating_windows_safely)" in this chapter.

One of the most powerful aspects of SSH is that it can be used to improve the use of less secure protocols. A common use of SSH port forwarding is for encrypting e-mail traffic. This is useful because certain e-mail protocols, such as POP3, FTP, and telnet send the e-mail messages in the clear, meaning they are easily read and not encrypted. Without the use of SSH, the Windows client will receive e-mail from the mail server by connecting to port 110 (POP3 e-mail) on the server. The server responds by sending the client's e-mail back in the clear (unencrypted). This puts potentially sensitive traffic on at least two local segments (LANs) and the Internet. However, an SSH session can be established with a mail server using the port forwarding options to secure this traffic. For example, when establishing the SSH connection the option can be given to forward the Windows client's port 65110 to the mail server's port 110 (POP3 e-mail). Now, if e-mail is retrieved by POPing the local port of 65110, the e-mail will be retrieved from the mail server. The e-mail will be encrypted because it will have traveled over the SSH port forwarding. Mail can be sent in a similar fashion by forwarding a local Windows port to port 25, Simple Mail Transfer Protocol (SMTP), on the mail server.

## Secure FTP

Secure FTP (sFTP) is a file transfer client program, which enables file transfer between the Windows workstation and an FTP server. It uses the same encryption and authentication methods as SSH. Because sFTP is an implementation of FTP over SSH, it provides all the security of SSH and all the features of FTP. In addition to transferring files, sFTP can delete files, change file names, create and delete directories, and change file access rights.

Using sFTP is the recommended alternative to NetBIOS file shares. However, with the added security comes some inconvenience. An sFTP solution to file sharing requires either a separate file server, or the need to run an sFTP server daemon on each Windows workstation. The first option, a separate file server, is recommended.

## Pretty Good Privacy

Pretty Good Privacy (PGP) is a public key encryption package to protect e-mail and data files. It lets you communicate securely with anyone who has a public key. Because public keys do not require a secure channel to exchange keys, the key exchange is not difficult. Public keys can be e-mailed, put on public key servers, or put on public Web sites.

PGP integrates nicely with most e-mail clients. So, once you have someone's public key, you can send e-mail with attachments that only they can open.

# Putting the Workstation on the Network

The Windows workstation should not be put on a network without some prior considerations as to the risk that exists. Because it takes only seconds for a local attack on a new workstation, care must be taken to prepare the system before putting it on any network.

## Test the hardened workstation

Prior to putting a newly hardened Windows workstation on a risky network, the system should be tested at its network interface. The test should consist of running a port and vulnerability scan against the Windows system. Any open ports should be accounted for, meaning that the application using that port should be required for the workstation's mission.

Once this initial testing is done, it should be archived for comparisons to future scans. By comparing new and old scans, the Windows workstation can be quickly checked for the addition of security vulnerabilities.

## Physical security

The physical security of the Windows workstation is important because lack of physical security can quickly nullify all the work done to harden the operating system. Attackers can take over control of any Windows workstations to which they have physical access.

The Windows workstation should have a reliable supply of power. If possible, this should consist of an uninterruptible power supply (UPS). It is considered a security problem if a system is unable to perform its functions due to a loss of power. Additionally, sudden losses of power can cause loss of data and possibly hard drive failures.

## Architecture

To keep your newly hardened Windows workstation secure, it is important to place it within a secure architecture. Architecture, in this case, refers to how the total network is designed and constructed. Certain portions of the network are more secure than others. The newly hardened workstation should be placed on the most secure LAN that still permits the user and the workstation to complete its mission and functions.

The security of the LAN on which the workstation is to be located should dictate the system's configuration. [Figure 8-11](ch08.html#the_configuration_of_the_workstation_dep) shows three segments with different levels of security. The least secure segment is labeled DMZ, the next most secure segment is labeled Company Intranet, and the most secure segment is labeled Personal/Private Segment.

![The configuration of the workstation depends, in part, on its network segment.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/0811.png)

**Figure 8.11. The configuration of the workstation depends, in part, on its network segment.**

Any system placed in the DMZ should be locked down and very hardened. It should contain no personal or sensitive data. It should contain a bare minimum of applications. In fact, it should not have any of the normal applications that a workstation might have. It should only have the single application that requires it to be in the DMZ.

If the workstation in the DMZ does need to handle sensitive data, that data should be acquired just in time to support the transaction needing it. For example, suppose the workstation is running a Web server to provide meeting schedules for traveling salespersons. The names and meeting times of the salespersons are too sensitive to leave on a system that sits on the DMZ. If a salesperson enters the Web site and needs to know his or her meeting details, the workstation must query the information from the workstation on the intranet. This sensitive data is not stored on the DMZ workstation but rather is immediately provided to the salesperson and then deleted.

No sensitive or private data should be stored on the DMZ workstation because of the elevated risk of being compromised or attacked.

The workstation sitting on the intranet should not contain any personal or private data. Because this is a company intranet, it is safe to have company-sensitive data on the workstation. This workstation should strictly conform to company policies regarding software use. It should not be running any personal software without the knowledge of the company network administrators.

The workstation on the private network segment can have any private or personal data that is needed for the user's mission.

## Firewall

The network that the Windows workstation is to be placed on should be protected from other unsecured networks (such as the Internet) by a firewall. While you may have hardened the operating system and workstation in general, it is still vulnerable to misuse of the workstation's capabilities as well as relay, spoofing, and man-in-the-middle attacks. One of the best ways to protect against these attacks and misuse of the workstation is to keep malicious users off the local segment on which the workstation is connected, and a network firewall is a good way to do that.

## Intrusion detection systems

For purposes of protecting the Windows workstation, an intrusion detection system (IDS) will serve much the same purpose as the firewall, that is, to keep malicious users off the same segment or LAN as the workstation. In the case of an IDS, the attacker or attacking code is detected if it has gotten around the firewall. The IDS can also detect an attack that originates on the LAN, a case in which the network firewall would not be useful.

# Operating Windows Safely

It is not sufficient merely to harden a Windows workstation against an attack; the workstation must also be operated safely. After hardening, the workstation must still be able to assist the user in performing some mission. If the user instead chooses to operate the workstation in a risky manner, the system may be left open to attack.

## Separate risky behavior

Ultimately, the security posture of a Windows workstation depends on the activity in which the user engages. To not put at risk an otherwise secure Windows workstation, risky user behavior should be separated from other activities whenever possible, either with a separate Windows workstation, or within the multiboot capability provided in Windows NT and more recent versions of Windows.

When it comes to use of a Windows workstation, users fall into one of two personality categories (and sometimes both): risky or stable.

The stable personality uses the Windows workstation as a tool for the following types of tasks:

- **E-mail** — Limited to family, friends, and co-workers
- **Web browsing** — Shopping, entertainment, information searching (within reason)
- **Multimedia** — Watching DVDs or listening to audio files
- **Document writing** — Letters, articles, diaries, presentations, recipes, and inventories
- **Photo processing** — Downloading images from digital cameras, some minor photo editing, printing photos
- **Web site maintenance** — Minor editing of HTML files for a personal or small business Web site
- **Finances** — Small payrolls, taxes, banking online, and checkbook balancing
- **Simple gaming** — Minesweeper, solitaire, time-tested, shrink-wrapped products such as flight simulator and card games

In many cases, this is the only personality that users will have. In addition to the general requirements for securing their workstation, they need to be sure to have up-to-date antivirus protection and surf the Internet safely.

The risky personality does some or all of the following:

- **Web browsing** — With frequent downloads to try things out, such as 30-day trials and free software
- **IRC chat** — Spends significant time in chat rooms and exchanges interesting downloads
- **Multimedia** — Experiments with screen savers, movies, and short clips; shares files on peer-to-peer forums, such as Kazaa
- **Tools** — Likes to get "toys" such as macros for Microsoft Word and Excel
- **Screensavers** — Experiments with applications such as screensavers
- **Games** — Downloads from untrusted sources and plays risky games
- **Pirated software** — Exchanges software while intentionally hiding its origins so the receiver cannot trust the software's pedigree

The risky games are of unknown origin and might have some of these characteristics:

- **Stresses computer resources** — Some of these games recommend changing computer chip speeds to increase performance.
- **Latest and greatest releases** — Often new versions are released before being fully tested, so the gaming community becomes the testing environment.
- **Distributed over the Internet** — While making distribution easy, it is very hard to know the origin of the software. If control of the software is lost, viruses and Trojan horses can be inserted.

## Physical security issues

Physical security is a company's first line of defense against an attack. In most cases, it is much easier, given proximity access, to pick up a file folder and walk off with it, or copy it and put it back, than it is to penetrate a network undetected. The most common cause of malicious information loss is physical theft. Providing lockable secure storage space is a vital part of ensuring physical security.

Physical protection of critical application servers is a key part of network security. If people can gain physical access to a machine they can do a lot of damage. In the simplest sense, they can unplug the machine and take down the network. All servers should be locked in racks and consistently labeled. Also, cabling to major data closets should be clearly labeled so it is evident to an administrator if patch cables have been moved and a workaround has been created.

### Secure the workstation when not in use

Unless there is a specific need to have the Windows system up and running all the time, it is recommended that the system be shut down when not in use. This will reduce the exposure time of the Windows system. Because attackers are active day and night, this can significantly reduce the risk to the workstation.

If the Windows system cannot be shut down, the next best thing is to disconnect from the Internet. This can be done in a number of ways, including the following:

- Disconnect at the firewall by removing the network connection.
- Add rules to the firewall that will not allow traffic through after normal working hours.
- Disconnect the workstation from the LAN by unplugging the cable (or wireless card) or by disabling the network interface card (NIC).

When possible, sensitive data and critical components should be locked up when not in use. This is a good reason for using removable hard drives. Remember as well to lock up media and backups. Most casual backups (such as writing critical data to a CD-RW) are not password protected, so they should be locked up.

When users step away from their workstations, they should use a screen lock. This can protect the users' privacy but can also prevent the introduction of a Trojan horse by someone walking by at the right time.

### Keep strangers off your systems

A Windows workstation, particularly one that is already logged into, should be considered very vulnerable, because given the opportunity, an attacker could sit down with the system. In just a few seconds, a stranger could alter settings, open a back door, tunnel through the firewall, or install a Trojan horse. This would be a severe security compromise to the system.

The Windows system should be protected against the wandering eyes of strangers. By "over-the-shoulder surfing" an attacker may pick up password keystrokes and private data that can be used in social engineering attacks.

## Configuration issues

A number of configuration issues should be considered when securing a Windows workstation. These range from properly using antivirus protection to limiting and managing users.

### Use antivirus protection

Antivirus software has been engineered to provide rapid protection against the latest virus or worm threats. However, in addition to having antivirus software installed, it must be configured and maintained properly, as follows:

- Manually run full scans periodically
- Configure antivirus software to check all new files
- Configure antivirus software to check all executables that are run
- Regularly obtain antivirus signatures and updates

### Limit user rights

It is recommended that administrators limit user permissions to the minimum needed to perform their functions. Recall that a Windows workstation is a general-purpose computer. The more that it can be made a specific-purpose computer, the more secure it will be. Limiting the scope of the user's capability will make the workstation more specific and, therefore, more secure.

If possible, the ideal situation would be to create specific user groups that have similar needs and, therefore, should have similar rights. Users can then be put into the group that best applies to them. For example, the following groups could be made:

- **Word processing** — Applications such as Microsoft Word, Excel, and PowerPoint
- **Internet** — E-mail clients, Web browsers
- **Gamers** — Various game-playing applications

A user can then be assigned to the word processing group but not the Internet group. In this way, the security risk to the Windows workstation is reduced due to less exposure to e-mail and browser-transmitted viruses and worms.

Some other restrictions that could be placed on a user are as follows:

- Access to ports
- Access to media
- Permission to shut down the Windows workstation

When considering the rights and permissions of users, it is important not to allow users to alter their own rights and permissions. This would defeat the purpose of limiting user access.

### Manage user accounts

The most secure Windows workstation is still very vulnerable to abuse or misuse by a user. The overall security of the workstation depends on the user being responsible. Normally users are conscientious and responsible and trusted enough to have access to critical applications and data. This trust is granted because a user is working with the data on a particular project and there is an expectation that, while on that project, the user will be a good steward of the data. When the user changes roles and responsibilities, his or her integrity does not change, but the trust relationship does. It is appropriate to review the user's permissions and access when the user has a change in status. The following are some circumstances under which user accounts need to be managed:

- A user's role and responsibility changes.
- User moves from one project to another.
- User permanently changes worksites.
- User leaves or is terminated from the organization.

If users change their roles and responsibilities, their permissions and access should be reviewed and adjusted accordingly. If users are promoted, they will probably need more privileges on the system. They may require access to directories and applications that they previously did not need and therefore were restricted from accessing or using.

If a user migrates from one project to another, he or she will probably use the same application. However, the administrator should limit the user's access to the old projects data while opening up access to the new project.

If the user is permanently changing work locations, he or she may have to access different data and servers. Because the user will probably have a new administrator handling their account, this would be a good time to review all the user's permissions and accesses.

It is very important to deal with a user's account when the person is terminated from or leaves an organization. The optimal procedure would be as follows:

1. Identify all data owned by the user.
2. Back up the data in case an issue regarding the user comes up in the future. If possible, make a ghost image of the user's hard drive. The length of time needed to retain this backup will vary with the user's responsibilities and the organization's policy, but a six-month time period is reasonable.
3. Transfer ownership of the data to the user's replacement or supervisor.
4. Remove the user from any groups. The user can be placed in a terminated group or a permit_no_access group.
5. Logs and other monitoring that user account names should be reviewed and archived if they contain activity about the user that may be needed at a later date. The length of time these logs are retained depends on the organization, but six months is a reasonable length of time.

The administrator can now delete the user account if the circumstances permit. There may be reasons why an account (username) might not be completely purged from a Windows system. For example, some timesheet and accounting packages use the userid as a key into their database. In situations such as this, the user account cannot be completely purged from the system. Because the account cannot be deleted, the administrator needs to ensure that the account will not be used or abused in the future by an attacker. Following the preceding steps should ensure this.

All this management of the user's account is predicated on the appropriate administrators knowing when the status of a user has changed, such as a user being terminated, being added or removed from a project, and so on. All of these activities are enacted by someone other than the administrator. Normally, HR or a project manager determines a user's change of status. However, in many organizations, there is no formal process established for the system administrators to be informed about such a change of status. A formal system, which ensures that administrators are informed of the change in status of users, is important for the overall security of the Windows system.

## Configuration Control

Configuration control is very much a security issue. Attackers can be expected to take the path of least resistance. They will scan thousands of machines to find the one that most suits their purpose or has a vulnerability that other systems do not have. System administrators must not only have secure configurations, but they must also have good configuration control. No system can be allowed to slip through the cracks. Configuration control should be used in concert with a test LAN, recommended later in this chapter. New systems should be configured and hardened prior to being put on the Internet or intranet.

Very subtle changes in a system and the infrastructure can severely impact security. The process of maintaining and administering systems should be formal and well documented. Procedures and hardening guides should be developed and used religiously.

### Control users on the system

Control of user accounts is a key component for the overall security of the Windows workstation. A number of problems can arise when personnel leave an organization or change positions and their accounts are not terminated. The account holder is no longer bound by any rules or policies of the organization and may no longer have any loyalty to the organization to safeguard and protect what was once trusted. Old accounts are often the targets of attackers. They have the advantage of being alterable without anyone raising concern.

A system for reporting the status change of an account is important so that the Windows workstations can be kept current. Whenever a person changes positions, responsibilities, or leaves the organization, all affected Windows systems should be updated to reflect the change in personnel.

The following are additional steps that can be taken to control users on a Windows system:

- Limit creation of accounts.
- Delete accounts no longer needed.
- Monitor for accounts that are no longer used.
- Periodically review a person's account and access as they change job responsibilities.
- Limit account (user) rights to the minimum needed for the user.
- Limit the use of Administrator privileges.

### Use digital certificate technology

Using encryption and digital technology on a Windows workstation can provide a significant improvement in security. Encryption can improve security in two general ways:

- If a protocol that transmits data in the clear is used
- As an added defense if a security control fails or is compromised

A number of protocols commonly in use today do not provide for data encryption. Some examples are FTP for file transfer, SMTP for sending e-mail, and POP for receiving e-mail. These protocols all authenticate and transfer data in the clear (unencrypted ASCII text). Encryption can be added to the use of these protocols to make the entire transaction unexploitable if someone is sniffing the line. For example, FTP, SMTP, and POP can all be done over an SSH session. In the case of FTP, a secure FTP client is used. In the case of STMP and POP, the SSH session is established and the two needed ports are forwarded over the SSH connection.

A defense-in-depth strategy calls for backup protection if the security on a Windows workstation breaks down. If the workstation were compromised and taken over by an attacker, the data on the workstation could still be protected if it were encrypted.

### Know the software running on the workstation

The Windows workstation is likely to be its most secure just after installation and hardening. As time goes by, most activity on the workstation will threaten the security, however slightly. One aspect of the security of the workstation deals with the software that is running. There are several reasons that the applications running on the Windows workstation might need to be reviewed. Some examples are as follows:

- The user roles and responsibilities will change over time. In this case, the user may no longer need one or more of the applications originally installed on the Windows workstation.
- New responsibilities may have lead to the user loading additional applications onto the workstation.
- An application may no longer be needed because the project requiring it has ended.
- Users may have installed applications and games from the Internet.

There are likely to be many changes to the software running on a Windows workstation over time. To maintain the highest level of security, an administrator should be aware of the software running on the Windows workstation. Particular attention should be paid to software that interacts with the network. This software can be detected when the network administrator does a scan of open ports on the Windows workstation.

If the user has loaded software onto the Windows workstation, the administrator should consider taking the following actions:

- **Remove the software**. If the application the user has installed is too risky to the security of the Windows system, the administrator may have to remove the software.
- **Apply patches**. If the application is needed, it will have to be maintained and kept up-to-date with patches and upgrades.
- **Use less vulnerable versions of the software**. In some cases, the user will have a legitimate need for the software but may not have chosen the most secure application. If a more secure version is available, the Windows administrator should remove the old application and install a more secure version. An example of this would be when the user has installed an FTP client for file transfer when a secure file transfer application, such as sFTP, would work just as well.

## Operating issues

Users and system administrators should adhere to a number of good operating techniques. These techniques or procedures reinforce the security configuration and hardening that has already been put into the Windows workstation.

### Adhere to policies

It is important that users adhere to security policies within an organization. Often these policies will be established to coordinate the various security measures across an organization. A risk in one area may be mitigated by establishing a security control on the Windows workstation. For example, there may be a subnet on the corporate LAN that routinely has untrusted users on it (perhaps for training non-employees). The company security policy may require an added rule in the personal firewalls on all Windows workstations to block access from that subnet. If the Windows workstation administrator were to remove this rule, the workstation would be at greater risk.

### Minimize use of administrator account

It is often the case that normal users on a Windows workstation will also have access to the administrator account. The user will occasionally have to log in as administrator to install software or to do a number of other administrative-level tasks. If possible, the user should resist the temptation to stay in the administrator account. Best security practices would dictate that the user use the administrator account only when absolutely necessary. Any protection afforded the Windows workstation due to the limitation of privileges or the protection of files will be bypassed if the user always uses the administrator account out of convenience.

### Enforce good data handling

The Windows security risk can be significantly reduced by practicing good data handling. The proper handling required for the data depends on the environment in which the Windows workstation is placed. If the workstation is on the Internet or in a DMZ, it should have no critical or sensitive data. If the workstation is on an intranet, it can have company-sensitive data, but should not have personal data. If the workstation is on a personal or private network, it can have any level of sensitive and private data.

As a general rule, for the best security, the user should minimize the storage of private or sensitive data. Special care must be taken to remove information that is stored but not obvious to the user. Data can be stored by the Web browser, in Microsoft Word documents, or in deleted files.

Web browsers store information about the sites visited. In addition to the URLs visited, data about Web transactions can be stored in cookies. Some cookie data is *persistent*, meaning that it will be stored on the hard drive.

Microsoft Word documents also contain hidden metadata, such as who has created the document, when it has been created, what has been changed, and by whom. Information that was thought to have been deleted from a Word document might still reside in the metadata of the document. Any of the following techniques should clear the metadata out of the Word documents:

- Save the document to a format that does not hold metadata, such as Rich Text Format (RTF). The RTF file can then be immediately opened as a Word document and will not contain the metadata. Unfortunately, some information may be lost, such as styles unique to the original document.
- Select and copy the entire document, open a new document, and paste. Only the selected text will be in the new document without any of the metadata.
- Save the document using Save As. The new document will not contain any clipboard data or metadata.

Users should be aware that deleting a file doesn't erase the file's content. When a file is deleted, the first character in the name is lost and the file system loses its pointer to the storage location of the file on the hard drive. A number of tools are available to recover deleted files.

Best security practices require that data and files should be properly marked. The classification is used to determine the distribution of the data, how it should be stored, and when it should be deleted. The following provides some common examples of data classification:

- **Company Sensitive** — This information should not be divulged to the public without a nondisclosure agreement (NDA). The NDA prevents someone outside the company from disclosing the information further. Normally, this is information that would be damaging for business if the company's competitors acquired it.
- **Departmental Restricted** — This information should stay within the department that has generated the data. For example, Payroll Restricted information should not be disseminated outside the payroll department.
- **Personal or Private** — This information should not be available to anyone beyond the individual and the few people who need to process the data, such as a payroll or human resources person.
- **Eyes Only** — This information is to be seen and used by only one individual.

Care must be taken to ensure that files are stored properly on the Windows workstation. The data should be stored in an easy-to-understand hierarchy. It is not a good security practice to try to hide the data on the Windows workstation. It is more likely that the user will lose track of the data and not delete it when the time comes.

If possible, sensitive data should be encrypted or put under password protection. PGP allows for the encryption of files. If the data is zipped, a password can be applied, but this should be considered a weak security control.

Files should be stored and handled properly when removed from the workstation. Media should be properly locked up and handled commensurate with the classification of the data. The same persons or department authorized to read the data should be responsible for the off-line media. Checks should be made daily that media is properly stored and secure. In most cases, this means that storage cabinets are checked to make sure they are locked before closing down the department for the day.

Obsolete data or information should be destroyed immediately or stored in a long-term manner that allows for tight control of its access. Long-term stored data should undergo regular destruction after a prescribed period of time. Depending on the particular business, destruction after 3 months, 6 months, 18 months, or longer may be appropriate. When determining how long to retain media, consider the need to put out monthly reports, quarterly reports, and annual reports, such as taxes.

### Avoid Viruses, Worms, and Trojan Horses

Windows users can take steps to minimize the spread of viruses, worms, and Trojan horses on their systems. The following steps require a judgment call by the user, but can provide significant protection against the spread of malcode:

- Turn off any Preview feature that the mail client may have. When an e-mail is previewed, it must be opened by the mail client, first. With some e-mail clients, this will cause scripts embedded in the message to execute.
- Don't open any e-mail from strangers that contain attachments.
- Only accept or open expected attachments. The user should have prior knowledge that the attachment was going to be sent. Many viruses today will, at first, appear to be legitimate messages. However, upon scrutiny, a user will be able to catch unexpected messages.
- Do not open attachments in e-mail that seems vague or out of character. Watch out for nondescript messages such as "Check this out." The sender should include information in the message that helps the recipient trust the attachment. If questionable e-mail must be received and read, use a separate e-mail client that is less susceptible to viruses. There are circumstances when a user is part of a public mailing list in which the members routinely share files. If attachments from this mailing list are routinely opened, an e-mail client that does not run Visual Basic scripts should be used.
- Turn off the "use macros" features in spreadsheet applications and word processors. Macros in word processing files are rare. Macros are more common in spreadsheets, but still infrequent enough that they can be enabled on a case-by-case basis.

In many cases, the preceding procedures require a judgment call on the part of the user. This judgment must be sharpened over time as the user becomes more aware of the risk of viruses.

### Use Good Passwords

It is important to remember that the length of the password determines how long it will take someone to crack it. For example, a six-character alphanumeric password (a–z, 0–9) can be cracked in a mean time of less than 1 hour (depending on the computer used). If these passwords were used on a Windows workstation, the user would be required to change the password every day.

However, a password containing 15 alphanumeric characters and symbols (such as !@#$%^&*+<>?|{}) has a mean time to crack of over 60 days. Therefore, the password policy can allow these passwords for 30 to 60 days.

As a general rule, passwords should be changed on a regular basis for Windows workstations, depending on the threat and criticality of information that is being protected.

Each system should have an identification mechanism built into the access path. Each user, or the user's supervisor, should respond to system administrators or the security organization as part of a periodic re-identification of system users. Access to a system should be disabled or suspended if the user has not used the system's capability within a 30-day period or the user does not respond to a periodic re-identification request.

The following password requirements are recommended:

- A password should be known only to the owner of an account (no shared passwords).
- When a password is assigned to initiate or reset access to an account, the Windows system should require the password to be changed upon initial use.
- Default passwords should be changed or removed prior to the system being placed on a network.
- Default passwords should not be allowed on a system except during the installation process, initial setup of a user, or re-initialization of a user.
- The system should not allow the password to be null or bypassed at any time.
- Passwords should not be displayed on an entry screen or any attached or associated device such as a printer.
- The Windows system should provide a mechanism to allow passwords to be changed by the user. The mechanism should require re-authentication of the user's identity prior to allowing a password change.
- Passwords should remain confidential.
- Users are not to write down their passwords.
- Users are not to save passwords electronically in unencrypted form.
- Users are not to reveal their passwords to anyone else under any circumstances, except in a temporary emergency situation.
- If a situation requires a password to be revealed to a second person, the owner of the password should change the password as soon as possible after the emergency situation has passed. During the time in which the password is shared, everyone with knowledge of the password is accountable for its use.

Systems should require the construction of access passwords, as follows:

- Passwords should be a minimum of 15 characters in length.
- Passwords should contain at least one alphabetic character and at least one numeric character.
- Passwords should contain at least one special or punctuation character.
- Passwords are not to be constructed using all or any part of the following:User idProper nameTelephone numberSocial security numberStreet addressDate of birthDictionary wordCommon company acronym or work group name
- Passwords are not to be constructed using common or proper names or words from the English language or other locally prevalent languages.
- Passwords are not to contain four or more characters of the same type (for example, four letters or four numbers) in succession.
- Passwords are not to contain three or more of the same character (for example, AAA or 777) in succession.
- Passwords should not be used for longer than 90 days.
- Passwords should be changed at least every 45 days on a system with critical functions or data.
- Passwords should be changed at least every 45 days, if they belong to administrative or other special privileged accounts.
- Passwords should not be reused.

### Limit the use of NetBIOS

NetBIOS is used for the convenient sharing of files in an interoffice or home setting. NetBIOS also supports print sharing. NetBIOS session vulnerabilities make Windows an easy target.

If possible, remove NetBIOS from the Windows system. For Windows2000/XP/Vista, disable NetBIOS in the network preferences.

If the use of NetBIOS cannot be avoided, strong passwords should be used to protect the Windows workstation. Limit the shared folders to the minimum needed to accomplish the task and avoid one huge share. A group of smaller shares with fewer files in each and different access lists will reduce the risk by limiting the damage should any one share be compromised.

The existence of available shares can be determined using the net command. The following information is available by opening a command prompt and running `net share`:

```
Share name   Resource                        Remark
--------------------------------------------------------------------------
C$           C:\                             Default share
ADMIN$       C:\WINNT                        Remote Admin
IPC$                                         Remote IPC
tmp          C:\tmp
The command completed successfully.
```

Current connections to any shares can be detected using the net command. The following information is available by opening a command prompt and running `net use`:

```
New connections will be remembered.
Status       Local     Remote                    Network
--------------------------------------------------------------------------
Unavailable  Z:      \\.host\Shared Folders   VMware Shared Folders
                     \\.host                  VMware Shared Folders
The command completed successfully.
```

### Avoid NULL sessions

A null session is a session established with a server in which no user authentication is performed. A null session does not require a username and password. Because there is no authentication, the access can be done anonymously.

To establish a null session, a user simply issues the following command:

```
net use <mount point> \\<host>\<path>  /user:" "
```

The net command is a powerful command line application that configures and reports on most aspects of Windows. Here is the help menu provided by the net command; the many uses of net can clearly be seen:

```
NET command /HELP
   Commands available are:
   NET ACCOUNTS             NET HELP              NET SHARE
   NET COMPUTER             NET HELPMSG           NET START
   NET CONFIG               NET LOCALGROUP        NET STATISTICS
   NET CONFIG SERVER        NET NAME              NET STOP
   NET CONFIG WORKSTATION   NET PAUSE             NET TIME
   NET CONTINUE             NET PRINT             NET USE
   NET FILE                 NET SEND              NET USER
   NET GROUP                NET SESSION           NET VIEW

   NET HELP SERVICES lists the network services you can start.
   NET HELP SYNTAX explains how to read NET HELP syntax lines.
   NET HELP command | MORE displays Help one screen at a
time.
```

In the net use command, the `<mount point>` is the drive letter that will be used to access the null share. The `<host>` value is the system name. The `<path>` value is the directory or folder to be accessed. The `/user:" "` is a keyword. Notice that the double quoted username is left blank. If a username were supplied, the user would be prompted for a password.

Null sessions allow easy inter-host communications, usually at the service level. The use of null sessions can expose information to an attacker that could compromise security on a system. For example, null sessions can list the usernames that allow an attacker to greatly reduce the amount of time it would take to carry out a brute force attack on a user's account.

The null session can also provide an attacker with the enumeration of machines and resources in a domain. This can make it easier for someone to break in. If an attacker can anonymously obtain the names of all the machines in a domain and then list the resource shares on those machines, it becomes a simple matter to try all of them until one is found that is open to everyone. Now the attacker has a foothold from which to launch an attack. One possibility is that a Trojan horse is put on the hard drive for an unsuspecting user to launch.

Null sessions can provide a convenient entry point into the Windows workstation and lead to a security compromise.

Null sessions should be eliminated entirely on the Windows workstation. If business practices make the elimination of null sessions impossible, take precautions to ensure that the only information exposed is the information you want exposed.

Null sessions can also be used to establish connections to shares, including such system shares as \\servername\IPC$. IPC stands for inter-process communication. The IPC$ is a special hidden share that allows communication between two processes on the same system. The IPC$ share is an interface to the server process on the machine. It is also associated with a pipe so it can be accessed remotely.

Null sessions were originally created to facilitate the communications between hosts and servers and between domains. All of these arcane reasons have modern workarounds that do not require a Windows workstation to leave open access via a null session.

### Conduct frequent backups

One of the security tasks that every user can practice is to conduct frequent backups of critical data. Of the security triad (confidentiality, integrity, availability), availability is often underrated as an important security tenet. A hardware failure can occur at any moment causing the loss of data back to the last good backup. If you can't afford to lose the last hour's work, back it up.

Backups need to occur a number of times to ensure the security (availability) of a Windows workstation. Consider backing up at the following times:

- Immediately after installation and hardening, burn a ghost image.
- Prior to applying patches and upgrades, back up all data.
- Prior to transporting the workstation, back up all data. In the case of a laptop, this could be very frequently.
- Periodically, back up all data. The time period depends on the business impact for losing the data. In most cases, this should be weekly or oftener.
- More frequently than periodically, back up critical data. In most cases, this should be no less frequently than daily.
- When making frequent changes to critical data, back up the data.

A good backup application will archive the operating system changes, changed data files, the Security Accounts Manager (SAM), and the Registry.

No backup should be considered complete until the backup has been verified. Remember that a backup contains very sensitive information and, therefore, needs to be properly protected.

# Upgrades and Patches

Security is an ever-changing arena. Hackers are constantly adapting and exploring new avenues of attack. The technology is constantly changing with new versions of operating systems and applications coming out every year. The result of all this change is an increased risk to the typical Windows workstation.

One favorable trend in the security community is that vendors are starting to become more security aware. Increased upgrades and patches are a result of the need to propagate fixes to security vulnerabilities. Therefore, it is important that users and system administrators keep current with the various upgrades and patches.

## Keep current with microsoft upgrades and patches

Windows security is absolutely dependent on users and administrators keeping current with Microsoft patches and upgrades. Ironically, this method of protecting applications may make systems more vulnerable to attack. Consider the problem from the attacker's perspective. Many attackers go after targets of opportunity. This means that if a vulnerable system is found, the attacker will apply the scripts to exploit the system. With the advent of patches and upgrades for a particular application, the attacker's mode of operation changes somewhat. The attacker can now search for systems that have not been patched or upgraded. Determining if a system has been patched or upgraded is generally simpler than attempting a full-blown exploit. So the ready availability of patches and upgrades for applications in your organization may in the end make you more vulnerable if you do not apply the patches and upgrades.

The market forces in today's fast-paced economy tend to lead to the development of software that is more risky from a security perspective. Software is rushed to meet deadlines without adequate and rigorous security testing. It is often left up to users to find problems and report them. This leads to an environment in which patches and upgrades are more frequent and more important to the network administrator.

Microsoft security bulletins include a rating system to indicate the severity of the problem addressed by the security updates. The Microsoft ratings are as follows:

- **Critical** — A vulnerability whose exploitation can allow the propagation of an Internet worm without user action
- **Important** — A vulnerability whose exploitation can result in compromise of the confidentiality, integrity, or availability of users' data or of the integrity or availability of processing resources
- **Moderate** — A vulnerability whose exploitation is mitigated to a significant degree by factors such as default configuration, auditing, or difficulty of exploitation
- **Low** — A vulnerability whose exploitation is extremely difficult or whose impact is minimal

It is recommended that all Windows patches, no matter their rating, be applied.

## Keep Current with Application Upgrades and Patches

High-visibility applications are well-known targets of hackers in search of vulnerabilities. An application should be considered high visibility if it has a large market share or large user base. There is a constant back and forth battle to keep these high-visibility applications protected against attack. As hackers discover vulnerabilities, developers quickly make patches to secure the application. This leads to a series of patches and upgrades for most high-visibility software.

It is easy to make a policy that states, "All applications will be kept current with patches and upgrades." In practice, however, this is very resource-intensive. Accurate inventories need to be maintained. Application and system baselines also need to be known and verified. Backups should be done before every patch and upgrade. Patches and upgrades should be loaded on a test platform to verify the stability of the resulting application and system. If unanticipated, these testing and backup requirements can tax an already overworked IT department.

Patches and upgrades should be tested prior to installing them. The testing should be done by someone in the organization who has a vested interest in the work or business that will be performed on the workstation. The software vendor does not have the concern and appreciation for your organization's business needs. There is always a possibility that a patch or upgrade will cause your business to lose time, efficiency, or data. Backups should be done prior to patching and upgrading. Whenever possible, patches and upgrades should be put onto mirror systems to assess their impact on the business operations.

## Keep current with antivirus signatures

It is not enough that an antivirus application is installed on a Windows workstation. For more protection against new and emerging viruses and worms, the administrator or user must ensure that the Windows workstation is kept current with antivirus signatures. There are four key steps to getting updated signatures:

1. Download new signatures.
2. Test new antivirus downloads.
3. Deploy new signatures.
4. Continue to monitor.

Most signature updates are obtained by accessing the antivirus vendor's site and pulling down the latest update. Most antivirus packages will allow the administrator to choose to have the new signatures downloaded automatically on a regular schedule. Automating the process may ensure that critical updates are not missed.

If the new antivirus signature is downloaded to be redistributed throughout a large organization, it should be tested first. In certain circumstances, it is advisable to eliminate the testing in favor of a more rapid deployment of the signature files.

In large organizations, it is prudent to have an internal deployment of the tested antivirus signatures. In such a case, it is expected that the clients will get their updates from a server that is local to them. The local server, in turn, gets its files from a master server that distributes the tested update.

Finally, it is important that the Windows systems be monitored periodically to ensure that the new antivirus signatures are being automatically downloaded and (if applicable) distributed properly. It is not the time to find a flaw in the system when the next big virus or worm hits.

## Use the Most Modern Windows Version

Older Windows systems have security issues that are not easily corrected or protected against. The typical example is the poor security built into LANMAN passwords. If a user's password is captured on an older version of Windows, it will be easy for a hacker to crack the password. LANMAN shortcomings can be mitigated to some degree by using longer passwords (if a password is greater than 15 characters, LANMAN will not be able to compute the password). Also, try using Unicode in the password by holding down the Alt key while entering a four-digit number on the keypad. There is a chance that the brute force password cracker may not try Unicode examples.

The newer the Windows system, the more security that is built into the operating system. For example, Vista does not have the LANMAN vulnerability.

Certain applications may require older versions of Windows operating systems. Consider running these applications in a virtual session, such as provided by VMWARE. In this way, the newest operating system can be used as the base system on the workstation, while still allowing the ability to run the legacy applications.

# Maintain and Test the Security

The threat against a Windows workstation is constantly changing and improving. More and more hackers are experimenting with attack tools. The propagation of tools for hacking is greater now than it has ever been. This means that the administrator of a Windows system must be diligent in maintaining and testing the security of the workstation.

## Scan for vulnerabilities

A Windows system should be periodically checked for vulnerabilities and open ports. A number of good scanners can do this, such as nmap, nessus, and several commercial versions. Each vulnerability and open port should be justified for its business requirement.

## Test questionable applications

Whenever there is a need to put a new but questionable application on a Windows workstation, it should be tested first. If the application is of unknown origin or pedigree, it should be considered questionable. Shrink-wrapped products purchased in retail stores are generally safe. However, Internet downloads or free software should be considered risky or questionable.

A Windows administrator should have access to a second computer that is considered risky from a security perspective. Any new or questionable applications can be loaded on the risky system to test the application and system for viruses and other problems.

One way for home users to test questionable applications is to take a ghost image of their Windows system before uploading the questionable software. If the software turns out to be unsafe, the Windows system can be reloaded from the ghost image.

## Be sensitive to the performance of the system

By far, most security issues with a Windows system are found while investigating performance issues. Attacks and exploits often work outside the bounds of what is normal for a protocol or procedure. In many cases, side effects of exploits can be detected in system performance. Some typical performance issues that can alert a system administrator to a problem are as follows:

- Excessive hard disk activity
- Excessive or unexplained network activity
- Frequent system crashes
- Unusual application behavior

Attackers are aware that any change in the performance of the Windows system can attract a system administrator's attention. Therefore, attackers take steps to keep their activities and attacks below an administrator's radar. This means that administrators need to be even more sensitive to changes in a system's performance.

Because most Windows administrators and users do not spend a lot of time reviewing system, security, and application logs, most attacks on a system are not detected until there is a performance impact.

## Replace old Windows systems

As expected, Windows is constantly improving its security. Each new Windows version has improved security features. The single biggest security problem to be corrected is the weak password protection provided by the LANMAN technology and vulnerability issues associated with NetBIOS.

The threat environment today is much more severe than when Windows 95 and Windows 98 first came out. Out-of-the-box installations of these systems can be completely taken over in seconds by readily available attacker scripts. Some of the security problems with these systems cannot be corrected, including their weak password protection.

Windows 2000 is a much improved system from a security perspective. A lot of information is available on how to secure Windows 2000. While Windows 2000 can be made secure, the system will require a significant amount of monitoring and maintenance to keep the security posture strong. Vista/XP on the client and 2008/2003 on the server are currently recommended operating systems.

It is recommended that you replace old Windows systems with newer, more secure systems. Note that a new Windows version should be out for six months to a year before it can be considered vetted. After that time, the new Windows version should have its security concerns identified.

## Periodically re-evaluate and rebuild

A Windows workstation will be at its peak performance and highest security level just after being built and hardened. The security of the system will degrade over time. The system will undergo many changes over time; some will be obvious, such as adding applications, and others will be subtle and hidden in the Registry.

It is recommended that a user or administrator re-evaluate the security posture of the Windows system periodically. If done religiously at specific times, it can become part of the information technology (IT) culture. Some good times to re-evaluate the security of a Windows system are as follows:

- When a user is added or deleted from a system
- When major updates or patches are added
- When the clocks are changed for Daylight Savings Time and smoke detector batteries are replaced
- During the usually quiet weeks over the 4th of July and the last week of December

It is also recommended that you back up and rebuild your operating system periodically. The frequency depends on a number of factors, including the following:

- The amount of experimenting that you do on a system
- The amount of different risky software you run
- Whether the system is used for software development
- If the system is operating strangely or crashing more frequently

With low or moderate use, such as a home system, Windows should probably be rebuilt once a year. With a system that experiences heavy use, such as software development and experimentation, the system should be rebuilt as frequently as every three months.

## Monitoring

Hardening Windows and protecting the network tend to address known security issues. However, a Windows system administrator needs to have a constant vigilance to be able to catch emerging security threats. Monitoring can detect attacks on the system as well as poor operations by the users.

Systems should be checked commensurate with the risk of lost data and lost productivity. If any loss of data or productivity cannot be tolerated, monitoring must be continuously done. If good backup and recovery mechanisms are in place, monitoring can be done less frequently, such as on a weekly basis.

The administrator can monitor for risky behavior. The following should be monitored:

- System logs
- Mail logs
- Failed access attempts
- Application errors
- Changing of critical files
- Permissions on critical files
- Performance tests
- Disk usage

The Windows system should also be checked for the installation of questionable applications and the careless use of data management.

## Logging and auditing

The Windows administrator should turn on as much logging as can be supported without adversely affecting the system performance and logging resources. Be mindful that too much logging may reduce the effectiveness of monitoring the system.

Be sure to log system restarts. Being able to match up the start of a system with other observed problems is very useful when tracking down security problems.

The logs should be reviewed and audited periodically. The frequency depends on the environment in which the workstation is located. If the workstation is directly connected to the Internet, such as in a DMZ, the system, security, and application logs and events should be audited daily or more frequently. If the workstation is behind a firewall and on a company LAN, the auditing should be done weekly. If the workstation is well protected with firewalls and is on a private and very secure network, the auditing can be done monthly.

## Clean up the system

It is a good practice to periodically clean up the Windows system. The workstation can collect various items that are best purged. The following is a sample of items that, if removed, could lower the risk of a security problem on a Windows workstation:

- Go through Add/Remove Programs and remove any programs that were installed but are no longer used.
- Archive and remove old work projects that are no longer active. In the event that the workstation is compromised or lost (due to some physical disaster), the risk of losing this data will be minimized.
- Check to make sure that any company-sensitive data that was not removed in the previous step is properly marked. The organization needs to set policies regarding marking data, but in essence, the data should not be viewable without the person clearly knowing the sensitivity level of the data. For printouts, this means labels on the top, bottom, front, and back. In the case of e-mail, it is usually a statement at the bottom of the e-mail. And in the case of data on a screen, the sensitivity must also be viewable on the screen.
- Run built-in Windows tools for cleaning up a disk drive. This will delete temporary files that are no longer needed. This will also delete cached Internet information. It is important to remove cached Internet information because an attacker may use it to conduct social engineering (human manipulation, which is described later in the chapter) against the workstation's user.
- Review and remove any private data that has been put on the workstation inadvertently.

## Prepare for the eventual attack

Despite your best efforts to harden your Windows system and protect the network, security incidents will happen. There are some things that the Windows system administrator can do to prepare for the eventual attack.

Preparation for an attack starts with the knowledge of what to do. Administrators of large networks may need more formal training such as that available with SANS (`www.sans.org`).

Learning what to do in the event of an attack will lead to the development of a plan. This plan may be formal and written or just in the administrator's head. Items in the plan should have a lead-time, such as the following:

- Buy that inexpensive backup system now, when you can shop for the bargains. After the attack occurs, there will be a rush to get a backup system and it is likely to be more expensive.
- Install backup hard drives into existing systems.
- Have a backup Internet service provider (ISP); a phone connection will work nicely.
- Test your backup ISP connection monthly.

As long as Windows remains a popular operating system, it will be a major target for attack. The best that a system administrator can do is prepare the Windows workstation, place it on a safe network, operate safely, keep current with patches and upgrades, and be diligent in monitoring and testing.

# Attacks Against the Windows Workstation

The Windows operating system has many vulnerabilities. A visit to Web sites such as NTBugTraq and SecurityFocus will show that the list of vulnerabilities is growing every day.

## Viruses

A virus is a piece of code that inserts itself into other legitimate software. As with a biological virus, the computer virus is not viable if found on its own. The virus needs the host software or file to propagate and carry out its mission. A virus is able to replicate itself and propagate with the host software or file.

Early viruses infected boot sectors of floppies and were spread by the sharing of applications on floppies. Today, floppies are too small to be practical for the sharing of applications, so boot sector viruses are not common anymore. But with bootable USB drives you might see this attack make a comeback.

Certain viruses are able to attach to data files such as spreadsheets and word processor files. These viruses are able to take advantage of the scripts that can be put into such files. These scripts are Visual Basic code that can execute when the file is loaded.

One of the first widespread viruses was Melissa, which spread by infecting Microsoft Word files. When the Word files were opened, the virus code would run and infect the `Normal.DOT` template file used by the word processor. Now any Word document saved would have the Melissa virus. Melissa used the autorun macros in a Word document to run a Visual Basic script when an infected Word document was first opened. Microsoft now has a feature called Macro Virus Protection that can stop macros from running. This protection should not be disabled.

If the virus has attached itself to an application, the code in the virus is run every time the application runs. The virus code will have the same privileges as the host application. A typical example of a host for this kind of virus is a self-extracting video clip. When the unsuspecting user launches the file to extract the video, the virus code runs. This virus spreads by persons sending the self-extracting video clip to their friends.

E-mail viruses move from PC to PC as part of the body of a message. When the virus code is executed, a message with the virus embedded is sent to other mail clients. The virus can either be an attachment that must be opened or an embedded script. Scripts can have access to the user's address book, and can use those addresses to propagate the virus-infected message.

Another common variant is the virus's Visual Basic script sending out an infected message to everyone in the user's address book.

Disabling the Windows ability to run Visual Basic will stop the scripting attacks these viruses contain. It is rare that a user needs to run a Visual Basic scripting program. The running of Visual Basic scripts can be disabled by deleting the association of VBS and VBE files with the Windows Scripting Host. The association is changed in the Windows Explorer tools options.

## Worms

A worm is code that is able to replicate itself while propagating to other hosts. In addition to replicating and propagating, worms can have code that might be destructive.

The difficult task for a worm is its need to get code to run on a remote host. To do this, the worm must exploit a vulnerability on the remote host.

The best protection against worms is to stay current with patches and upgrades for Windows as well as for the major applications. Most worms exploit previously identified vulnerabilities that are correctable with patches or upgrades.

The other protection against worms is to minimize the services and applications running on the workstation. For example, worms often target common, high-visibility applications, such as the Microsoft Web server which is called Internet Information Server (IIS). If a workstation does not need to serve up Web pages, this product should be removed from the workstation. If a worm does attack the Internet searching for IIS servers, it will not affect those workstations from which the Web server has been removed.

Worms differ from viruses in that they are much more complex routines tailored to the target company, designed to embed themselves in binary executable files, and able to alter or destroy data. Lack of a version control system places a company's data in jeopardy. Software systems that detect these types of attacks allow a quick response to the corruption of data. Important and critical systems files need to be identified and strictly controlled.

## Trojan horses

A Trojan horse is a program that masquerades as a legitimate application, while also performing a covert function. Users believe they are launching a legitimate application, such as a screen saver. When the Trojan horse runs, the user has every indication that the expected application is running. However, the Trojan horse also runs additional code that performs some covert activity. The possibilities for covert activity are almost limitless.

The best way to detect a Trojan horse is to identify executable files that have been altered. This is most easily done by baselining the hash values for all executable files on a workstation. If an executable file is later altered to include a Trojan horse, it can be detected by comparing the current hash value with the baselined value. This is typically done with file integrity checking programs such as TripWire.

Trojan horses have a distribution problem. They do not propagate on their own. They rely on users accepting questionable executables from untrusted sources. This becomes much more of a social engineering problem. As with social engineering, it is not difficult to target a particular user and to eventually get them to execute an untested piece of code.

Trojan horses are very powerful threats to the security of a workstation, network, and organization. They bypass most security controls put in place to stop attacks. Trojan horses are not stopped by firewalls, intrusion detection systems (IDS), or access control lists (ACLs).

The key feature of a Trojan horse is that it has all the capabilities and permissions of a user — a malicious user. Most organizations put a certain amount of trust in users not to abuse the resources they have access to. All this trust works against the organization in the case of Trojan horses. This can make them very difficult to defend against. As more and more improvements are made to secure networks, attackers may move to Trojan horses as a means of circumventing the security controls.

## Spyware and ad support

Spyware is a group of software applications that gathers information about the workstation and users. This information is then sent back to the developer or distributor of the spyware to prepare ads or revise marketing campaigns.

Targeted marketing has long been a tenet of a good sales program. The classic example is when marketers use census data to direct more effective mass-mailing campaigns. Census data is used to find certain zip codes that have the ideal average income and number of children for the particular product being advertised. The use of census data, provided for this purpose by the Census Bureau, is inherently safe because specific names and addresses have been removed and the data is a summary of statistics for the zip code.

Spyware software, however, poses a much greater risk, because the data has a lot of specifics on a named individual. The information can be used in any number of ways, unbeknownst to the user. For example, you may be a target for intense mailing or phone marketing efforts. In the case of spyware, the user also does not know who might get hold of the data. For example, certain private data can make identity theft easier.

The Windows workstation stores personal information in a number of places accessible to applications running on the machine. The most common example is accessing the information put into Web browsing cookies.

Cookies can potentially contain a wide range of personal and sensitive data. Essentially, anything that you have entered in a Web page could have been stored into a cookie by the Web server. The Web server also decides whether the cookie is persistent or not. Consider some of the information that you may have put into a Web page in the past:

- Your name and address
- Phone numbers, e-mail addresses, instant messaging (IM) handles
- Social security numbers, bank account numbers, banking PINs
- Children's names, mother's maiden name, favorite pet name
- Employer and salary
- Car tags and vehicle make and model

It is possible to disable cookies on most Web browsers. However, this turns out not to be a practical solution in many cases. Many sites depend on cookies to implement legitimate stateful processes by the Web server. Many people start out by selecting the option to "Ask Me Before Accepting Cookies." However, the constant pop-ups requesting permission to accept the cookies tend to be such an aggravation that they give in and accept all cookies.

## Spyware and 'Big Brother'

The term spyware also refers to the set of applications that intentionally snoop and monitor user activities in a covert manner. This is reminiscent of Big Brother in George Orwell's *1984*. These PC surveillance tools report detailed information back to the person installing the spyware. Typical information that can be reported includes the following:

- **User keystrokes** — This can be used to capture passwords and other very sensitive data.
- **Copies of e-mails** — E-mails sent or received can be forwarded, unbeknownst to the user, to the person wanting to monitor the user.
- **Copies of instant messages** — Essentially, any communications to and from the PC can be copied and sent to the spyware's owner.
- **Screen snapshots** — Even encrypted communications will at some point be displayed in the clear to the screen. At this point, the spyware can take a screen shot and send the image to whoever has developed or distributed the spyware.
- **Other usage information** — Login times, applications used, and Web sites visited are examples of other data that can be captured and reported back.

Spyware that reports to its owner relies on stealth to accomplish its mission. If users know that the spyware is present, they will remove the spyware, change their behavior, or otherwise avoid the use of the particular applications being monitored.

A number of commercial products claim to detect spyware. These products maintain a database of known spyware applications. While these products may be useful for finding the most common and blatant examples of spyware, it should not be assumed that they will find all spyware.

## Physical attacks

There are numerous physical attacks to which Windows workstations are vulnerable. Most security professionals assume that if an attacker has unlimited physical access to a system, the system can be successfully attacked. Some examples of physical attacks are as follows:

- If the attacker can boot a system with a USB or CD, they can get the SAM and other key information to crack passwords, or they can just delete the passwords and set up their own.
- If the attacker can boot a system with a USB or CD, they can have the workstation boot into a Windows system that is configured to give them access.
- Keystroke capture devices can be placed on the workstation to steal critical data that is typed into the system, such as passwords and e-mails.
- Network traffic to and from the workstation can easily be captured or sniffed if an attacker can insert a hub or modify a switch.

Physical security addresses the threats, vulnerabilities, and countermeasures that can be used to physically attack a Windows workstation. Most organizations put too little reliance on their physical security when considering the various tools to protect a Windows system. Physical security for a Windows system should work from the premise that any system can be compromised if the attacker gains physical access.

## TEMPEST attacks

Transient electromagnetic pulse emanation standard (TEMPEST) attacks consist of capturing the electromagnetic radiation leaking from electronic equipment. TEMPEST attacks are usually done by analyzing the electromagnetic radiation from the monitor. Because TEMPEST attacks can be carried out at a distance of tens of yards, this can be a concern when dealing with very sensitive data.

The best protection against TEMPEST attacks is to do the following:

- Don't operate with systems opened or in a manner inconsistent with FCC guidelines. The FCC regulates the emissions from PCs to keep down the broadcast interference.
- Limit the processing of very sensitive data to TEMPEST-certified systems.
- Be aware of the surrounding environment.
- If a problem is suspected, have the environment checked for TEMPEST emissions.

## Back Doors

A back door is a means for an attacker to easily get into Windows workstations. Often, the initial attack on a workstation is difficult and potentially detectable by a firewall or IDS device. So the attacker will install an application that will allow him to get back into the workstation quickly and easily. These back doors are often stealthy and difficult to detect.

If a Windows workstation has been on the Internet unprotected and unhardened for more than a day, it most likely has been "rooted" and has a back door installed. In such a case, the best thing to do is wipe the system clean and re-install the Windows operating system. Although the back door might be detectable using host scanners, the administrator can never be sure that other changes have not been made on the workstation. Some kernel and driver modifications are difficult to detect. Some Trojan horses would be very difficult to find without a clean identical system to compare files against.

## Denial-of-service attacks

Remember that security is concerned with confidentiality, integrity, and availability. It is considered a security loss if you are denied access to your data or are denied the capability to use your resources. When an attacker prevents a system from functioning normally, this is considered a denial-of-service (DoS) attack.

DoS attacks are difficult to prevent. Every computer device will have limits to its capabilities. Many DoS attacks push the device to its limits and cause it to fail. DoS attacks will often access the device in a normal manner, but so frequently that no other user can access the same device. The device does not fail, but because legitimate users cannot access the device, a DoS situation exists.

Windows workstations can best prevent DoS attacks by taking the following actions:

- Install a personal firewall.
- Use a firewall on the network.
- Limit unnecessary applications on the workstation. If the following, in particular, are not needed, they should not be loaded and run on the workstation:Web serverMail serverFTP serverFile server

## File extensions

Windows has a feature that allows the file extensions to be hidden to the user. This supposedly makes the system more convenient and user friendly. This convenience comes at a security price, however. By hiding the extensions, malicious code is able to masquerade as something benign. For example, a user might be tempted to open a file named `readme.txt`, knowing that simple ASCII text files cannot contain malicious code. However, the user will be at risk if the real file name is `readme.txt.bat` because the true extension, `.bat`, is hidden by Windows. Now if the user opens the file by double clicking on it, the malicious code in the BAT file will run with the same permissions as the user.

File extension hiding should be disabled on the Windows systems.

## Packet sniffing

A Windows workstation is vulnerable to having its network traffic intercepted and read by another workstation on the same LAN segment. At one time, this threat was restricted to when the two workstations were on the same hub. Now, tools such as ettercap are available to attackers that will allow them to read the traffic in a switched environment. In a hub environment, the traffic can be read passively without the Windows user being affected. In the switched environment, the tools set up a man-in-the-middle attack, in which the traffic is intercepted, copied, and then sent on to the intended destination.

Using packet sniffing, an attacker can read all the user's Internet traffic, including e-mail, instant messages, and Web traffic. With regard to Web traffic, the attacker sees every screen just as the user does.

The best Windows protection against packet sniffing is to use encryption whenever possible. The attacker can still intercept the traffic, but it will be encrypted and of no use.

## Hijacking and session replay

Session hijacking occurs when a TCP/IP session is observed and captured by a network sniffer. The session has an originator and a target host. The attacker captures the traffic sent out by the originator. The attacker can then modify the captured traffic to allow the attacker to appear to be the target host. The traffic is now sent to the attacker instead of the original target host. All future traffic in the session is now between the originator and the attacker.

Session replay occurs when a TCP/IP session is captured by a network sniffer. Some aspect of the session is then modified (certain replays, such as transferring bank funds, may not require modifications). The modified session is then fed back onto the network and the transaction is replayed.

## Social engineering

Social engineering is a method to gain valuable information about a system from personnel. Generally, the attacker uses a little bit of inside information to gain the trust of the victim. With this trust, the victim ends up providing sensitive data that the attacker can use to exploit the system further. For example, pretending to be an authority figure, an attacker may call a help desk and tell them that they forgot their password and need immediate access to a system in order not to lose a very important client. Many situations can be invented, depending on what information has already been gained about the enterprise and the particular application. In some cases, the attacker will construct a situation that creates a lot of pressure on the personnel to get information fast.

It should be assumed that serious and malicious attackers will always want to use social engineering to make their work easier.

Information should not be provided in a public forum that does not contribute to the mission of the Windows workstation. This information might make the social engineering task easier. For example, usernames and IDs should not be displayed in a manner that is visible to a stranger.

Social engineering is the hardest attack to defend against and is potentially the most damaging. Despite the best training, people will share critical and sensitive information in an effort to "get the job done." The attacker can then do some very damaging things with this information. If the information obtained contains user IDs and passwords, the attacker can essentially do anything that a legitimate user can do.

# Summary

The Windows workstation may very well be the most insecure part of an organization and a network. This is due in part to the following:

- The typical user is not well trained in security but has a great deal of influence on the security of the Windows workstation.
- The PC has been designed as a general computing platform. This leaves a lot of the design open to hacking and finding vulnerabilities.
- Most of the work performed on an organization's network is done on the Windows workstation. Because there is a trade-off between security and ease of doing work, it is expected that the workstation will be the most vulnerable part of a network.

The Windows workstation can be made secure. The major components to a secure workstation are as follows:

- Harden the operating system.
- Install secure applications such as antivirus protection.
- Prepare the network that will contain the workstation.
- Operate the workstation safely.
- Maintain patches and upgrades for both the operating system and key applications.
- Test and monitor the security of the workstation frequently.
