# Chapter 24. Digital Forensics

**IN THIS CHAPTER**

- **Understanding what digital forensics is**
- **Methods and types of forensics**
- **Proper handling of evidence**
- **Analysis of digital evidence**
- **Legal issues involving forensics**

Computers and networks are being used in almost every area of our business and life. Therefore more and more crimes are computer-based. In order to understand what has happened during a computer crime, fix the vulnerability, and possibly prosecute, it's critical to understand how to find and deal with evidence. The process of understanding and finding evidence is at the core of digital forensics and will be examined in this chapter.

Society today is more reliant on electronic information than ever before, but with this reliance comes the possibility of disaster. Most people think of a disaster as something in nature — a hurricane, earthquake, or tornado. But ask any CEO about the ramifications of a data loss or the inability to access data and you'll find they consider those to be disasters as well.

Most enterprises can't afford to have a disaster related to their data. The bottom line and customer confidence are real concerns and must be planned for in the case of a disaster. Most businesses plan for ordinary hack attacks and true natural disasters, but few are prepared for the meltdown of a critical system that's not backed up in real time. Nor are they prepared for that visit from the local FBI agent as a result of criminal activity being conducted on their networks.

*Computer forensics* is a term not widely understood in the enterprise community. Most enterprise managers feel that the only use for forensics is to recover data after an incident, a totally reactive role. Forensics by law enforcement organizations is viewed as the collection of evidence to be used in criminal prosecutions—again, a totally reactive role.

"Computer forensics," also referred to as "digital forensics" or "enterprise forensics," has always been divided into two distinct categories: enterprise forensics and law enforcement forensics. There is a clear dividing line between the two and the end result may vary, but the methods by which practitioners get to their goals are similar.

# Computer Forensics Defined

Most companies write contingency plans and data recovery plans. They also develop forensic responses using the term "computer forensics," but computer forensics actually is defined as "the application of computer investigation and analysis in the interests of determining potential legal evidence." As you can see, this definition is very specific to the law enforcement community. Computer forensics when discussed in the context of an enterprise is primarily concerned with incident response and recovery with little concern about evidence or sound methodology. Such methodology has recently acquired the name "enterprise forensics." It resembles but is different in some respects from the methodology used by law enforcement.

This chapter will cover the root methodology of computer forensics from start to finish. Computer forensics in the true sense of security and prosecution began, and the working model was developed, in the law enforcement community. This is the model accepted in most judicial districts. A similar methodology has been adopted in part by most enterprises as an incident-response component.

# Traditional Computer Forensics

Traditional computer forensics in the sphere of law enforcement is well-designed but almost exclusively reactive. It has four distinct phases: processing of the incident scene, acquisition of evidence, analysis of evidence, and finally storage of the evidence. The process is usually triggered by a call about a crime or incident in which there is a possibility for the retrieval of evidence from an electronic data source. The digital data source is collected and the chain of evidence begins.

## Evidence collection

Electronic evidence can be many things and in many forms, but the basic response and collection process remains the same. A methodology should be followed to properly process the scene. The first and most important thing to determine is the location of the incident. Unlike a traditional crime scene, an electronic crime scene is often hard to pinpoint and there may be multiple locations across several judicial boundaries.

As the incident scene is being processed, it must be documented every step of the way. There are many different methods of documentation and the use of more than one method is recommended. Some of the common documentation items are:

- Photographs
- Video tapes
- Written notes
- Voice dictations
- Electronic records

As the scene is processed, evidence will be identified for collection. The steps in this process must be clear and must be followed in order to provide an adequate chain of evidence or chain of custody.

## Chain of evidence/custody

The chain of evidence/custody is a key component of the forensic process. Without such a chain to track and categorize the evidence collected, that evidence can later be found to be tainted and not admissible in court. Chain of evidence is from collection to presentation in court, who had access, and how evidence was preserved. Custody is who has control or management of the evidence.

The chain of evidence/custody can also be defined as the process in which documentation is used to track every movement of evidence collected during the course of an investigation.

The chain starts when an item is identified as something that might contain information that could be used later in some type of formal proceeding. The beginning of the chain is shown in [Figure 24-1](ch24.html#high-level_steps_in_handling_an_incident).

![High-level steps in handling an incident and evidence](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2401.png)

**Figure 24.1. High-level steps in handling an incident and evidence**

Traditionally, the "chain of evidence" is defined as having the following elements:

- Location of evidence when obtained
- Time evidence was obtained
- Identification of individual(s) who discovered evidence
- Identification of individual(s) who secured evidence
- Identification of individual(s) who controlled evidence and/or who maintained possession of that evidence

On the other hand, the "evidence life cycle" usually comprises:

- Discovery and recognition
- Protection
- Recording
- CollectionCollect all relevant storage mediaMake an image of the hard disk before removing power.Print out the screen.Avoid degaussing equipment.Identification (tagging and marking)
- PreservationProtection of magnetic media from erasureStorage in a proper environment
- Transportation
- Presentation in a court of law
- Return of evidence to owner

The former group of points is concerned with tracking who handled the evidence and the latter is concerned with what happens to the evidence from beginning to end.

The chain is by design a very rigid process with little room for deviation. [Figure 24-2](ch24.html#additional_steps_used_in_maintaining_a_c) shows the addition of two more steps.

![Additional steps used in maintaining a chain of evidence/custody](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2402.png)

**Figure 24.2. Additional steps used in maintaining a chain of evidence/custody**

Each step has to be documented and tracked by the person in control of the evidence. The most common forms used are log sheets and the tags shown in [Figures 24-3](ch24.html#chain_of_custody_tag) and [24-4](ch24.html#evidence_tag_used_during_incident_invest).

![Chain of custody tag](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2403.png)

**Figure 24.3. Chain of custody tag**

If the examiner did not properly check in the evidence to the property section, the evidence is unaccounted for during the several days while it is being processed by the examiner. When the evidence is then given to the property section and logged as being submitted, there will be a gap in the chain of custody due to the lapse in time from when the scene was processed until the time of evidence submission. A defense attorney can attempt to use this little oversight to have the evidence suppressed, and such an oversight can cause all evidence found on a particular medium to be suppressed. This commonly occurs when the examiner is the one collecting the evidence. Instead of checking the evidence in, and then checking it out, the examiner just takes the evidence from the scene of the incident to the examination location.

Well-defined policies and training in handling evidence handling will eliminate many problems.

![Evidence tag used during incident investigation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2404.png)

**Figure 24.4. Evidence tag used during incident investigation**

When there is a break in the chain of evidence or the proper method is not used, then the evidence can no longer be considered good and may be suppressed (or inadmissible) in a court of law. For example, [Figure 24-5](ch24.html#stages_where_mistakes_are_commonly_made) illustrates some stages where mistakes commonly are made and the chain broken.

![Stages where mistakes are commonly made in handling the chain of evidence](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2405.png)

**Figure 24.5. Stages where mistakes are commonly made in handling the chain of evidence**

## Acquisitions

Data acquisition can be defined as the method of copying data from one media to another on a bit level, ensuring the transfer of every bit from the original media is copied in an exact representation on the storage media being used without altering the original data. Acquisitions must be done in a way that protects the data and this can be done using two different methods. The first, commonly referred to as a "software write block," uses a method of software change that does not allow write commands to reach the original device. The blocking of the write commands is done using the operating system and modifications of that system to allow only one-way communication. The second and more commonly used method of acquisition is to use a hardware device called a "write blocker" placed between the source and target devices. This hardware block is capable of blocking all write commands to the source device. As shown in [Figure 24-6](ch24.html#write_blocker_open_parenthesis_left_clos), this device is placed between the digital media and the computer to protect the data on the hard drive and allow only read commands to reach the hard drive controller.

![Write blocker (left) connected to a hard drive](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2406.png)

**Figure 24.6. Write blocker (left) connected to a hard drive**

The ultimate goal of the forensic acquisition is to ensure that you have an identical image of the original evidence to work from. The primary reason for working from the copy of the original images is that you will never be able to reproduce that information if the original is altered or changed. This can have a significant impact if the information is requested by the defense attorney in a legal proceeding.

Three types of forensic acquisitions are commonly accepted and used in the law enforcement community.

### Mirror image

A *mirror image* is created from hardware that does a bit-for-bit copy from one hard drive to another. This allows the hard drive to be available if the original system needs to be restarted for additional examination or analysis.

The limitation of this type of methodology is the need to have a drive that is identical or that has a larger capacity than that of the source drive. This presents problems from a financial standpoint when it's necessary to obtain a new hard drive for each piece of evidence. The storage of multiple hard drives for multiple cases also has an impact on the resources of the entity conducting the forensic examinations.

The advantages are that acquisition is generally faster, there are more options for the use of the device, and the shelf life of the evidence is long.

### Forensic duplication

A *forensic duplicate* is a file that contains every bit of information from the source, in a raw bit-stream format. This can be one large file, or it can be broken into file sizes defined by the examiner. This is the most common type of acquisition. The ability to store multiple cases in one centralized storage facility allows for an overall cost savings as well as the ability to duplicate that file over and over without the need for additional drives or equipment. There is also the ability to restore the file image to its original state on a physical hard drive. The forensic duplication process is generally completed by a specialized program such as the following:

- The UNIX `dd` command
- Safeback
- EnCase
- FTK Imager

No matter which tool is used, the outcome must always be the same. The file must be an exact representation of the original drive at the bit level. The digital fingerprint, also known as a hash, must match.

### Live acquisition

A *live acquisition* is the retrieval of information from a system that is currently running. It is performed in lieu of traditional forensic duplications:

- To retrieve volatile information
- When circumstances merit the live collection of data

Live acquisitions are becoming more common and with this also comes additional concerns. While doing an acquisition, the examiner must maintain very detailed and exact notes. This is to ensure that all procedures were followed and that every precaution was taken to guarantee that the information was collected according to a standard. With this type of collection, the data is continually changing, and this must be taken into consideration during the examination portion of the investigation. As data changes, evidence has the potential of being lost or overlooked. The last major concern is the possibility of system corruption caused by the acquisition.

If the examiner is not using strong methodologies that have been tested and documented, and failure occurs as a result of actions not consistent with common practice, then the examiner could face legal action.

This type of acquisition requires additional technical support because of the use of more sophisticated data systems and equipment. For example, the newest SCSI technology is a SAS drive. These drives use a specific type of SATA connection and no hardware write block is currently available to conduct acquisitions. Therefore, a live acquisition is a viable option.

### Acquisition storage media

When considering an acquisition of any kind, an important step in the process is to use media already prepared to receive the evidence. This step is crucial and often overlooked. The process of forensically sterilizing the media is a fairly simple yet time-consuming process. There are several accepted methods of live acquisition and all should be tested by the examiner in a test environment before implementation.

After the receiving media is purchased or acquired in some manner, it needs to be processed to ensure it is completely cleaned and sterilized. The digital storage media should be connected to a computer or device designated to sterilize media. The sterilization process is nothing more than writing zeros, ones, or random characters on the device from the starting block of data to the end. If necessary the media can then be formatted to collect, store, or mirror data. Some examples of digital storage media are:

- Hard drive
- Flash drive
- SIM card
- Floppy drive
- iPod
- iPhone
- iTouch
- Cellular phone

The storage media can be reused but must be sterilized to ensure there are no remnants of data from any previous uses.

### Volatile information

*Volatile information* is information stored in RAM that is lost when a system is powered down after the decision has been made to perform the live acquisition. This volatile evidence cannot be collected after the system has been powered down, so it's necessary to collect such information as the following:

- System date and time
- A list of currently running processes
- A list of currently open sockets
- The applications listening on open sockets
- A list of the users who are currently logged on
- A list of the systems that have current or have had recent connections to the system

These types of evidence are used in many different circumstances and must be collected using tools tested and validated by the examiner. This ensures consistent and reliable results with the greatest chance of successfully retrieving the desired information. An outline of the process is shown in [Figure 24-7](ch24.html#evidence_collection_process).

![Evidence collection process](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2407.png)

**Figure 24.7. Evidence collection process**

### Analysis

The analysis phase is the most important and time-consuming part of the entire process. It can take weeks or months, depending on the type of case and the amount of data that must be examined. Different levels of examination have been defined over the years, including limited, partial, or full exams.

The exam process, regardless of which method used, is intended to produce the same end result. The information obtained should provide evidence of the crime or incident during which the initial response was initiated. Depending on the type of case, this information could also clear an individual or company of wrongdoing.

Examiners tend to have their own ways of processing the data, based on their training, experience, and the tools used during the process. A number of good forensic tools are available to law enforcement and businesses, and each has strong and weak points. Three of the most commonly used tools are Access Data's "Forensic Tool Kit (FTK)," Guidance's "EnCase" software, and Paraben's suite of forensic tools.

EnCase, shown in [Figure 24-8](ch24.html#example_of_encase_examining_forensic_evi), is a very powerful forensic tool that allows the user to use predefined scripts to pull information from the data being processed. The tool also allows users to develop their own scripts and thus personalize the process.

![Example of EnCase examining forensic evidence from an incident](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2408.png)

**Figure 24.8. Example of EnCase examining forensic evidence from an incident**

EnCase also has the ability to process larger amounts of data more efficiently than other software suites currently available.

Forensic Tools Kit (FTK) is a suite offered to both law enforcement and businesses; it contains a variety of separate tools to assist in the examination. FTK has the ability to examine the Windows Registry separately and is very efficient with e-mail and image processing.

P2 Enterprise Edition from Paraben is the next evolution in digital forensics, moving the examination from a reactive crisis mode to a proactive protection of digital evidence. Whether there are risks of intellectual property infringement, theft, embezzlement, or general insider threat, P2 Enterprise can perform the analysis; however, a tool is only as good as the person using it.

During the initial exam process, the examiner must ensure that the data to be processed has followed the chain of custody properly and that all proper documentation has been completed to begin the analysis phase. When everything has been checked and validated, the examiner must then determine what the data may contain, what method of examination may be used, and finally how the data will be extracted and stored. As stated previously, the type of incident will dictate the amount of data that must be examined as well as the method used to examine it. The analysis covers all the information provided to the examiner during the process of identifying the incident, evidence collection, and scene processing. But other factors, such as legal issues, also affect the overall scope of the investigation. There are many schools of thought on the exact methodology that must be followed when conducting a forensic analysis. The key point is to document your methodology and stick to that plan. Deviation from that plan without a reason is the main thing that will cause doubt on the part of a court.

### Limited examination

A *limited examination* is limited to data areas either specified by legal documents or based on interviews and/or examiner experience as to where the data will most likely be located. Sample information collected is shown in [Figure 24-9](ch24.html#using_encase_during_a_limited_exam). These types of examinations are the most common as they are the least time- and resource-intensive. The primary areas of focus are directories inside a specific user's profile. It is not uncommon to begin a limited exam and have to expand the scope based on evidence recovered. Some of the most common areas of data can include:

- Specific user areas of forensic interest on Windows systems
- Desktop folders (link files)
- Favorites folders (see "screen capture" in the text that follows)
- Local settings
- My Documents file
- Recent and link files
- Send To Folder file
- Start menu

A limited exam can also include the volatile information collected from a system that is still in operation.

### Partial examination

A *partial examination* is based on general search criteria developed through experience and training. An example is shown in [Figure 24-10](ch24.html#using_encase_during_a_partial_exam_comma). The examiner receives the request for an examination and pulls information from key areas for further study. Some of the common areas are the registry, log files, and user directories. These key areas are then examined in greater detail to find data that may be relevant to the case. Other areas are generally identified and examined during the process. Besides the files identified in the limited exam, the following list offers additional files that may be examined. A partial examination is becoming the most frequent type of exam.

- Specific user areas of forensic interest on Windows systems
- User personal files (see [Figure 24-10](ch24.html#using_encase_during_a_partial_exam_comma))
- Root files
- Application data
- Address book
- E-mail folders
- Cookies

![Using EnCase during a limited exam](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2409.png)

**Figure 24.9. Using EnCase during a limited exam**

### Full examination

A *full examination* is the most time- and resource-intensive and can take weeks if not months. It requires the examiner to look at every possible bit of data to determine the root factors of the incident. For example, in [Figure 24-11](ch24.html#using_encase_during_a_full_examination) the examiner is examining slack space on a drive. Slack space is a portion of a block of data that was not totally overwritten and may contain data from the previous file that resided at this location. This type of analysis will provide additional and otherwise unobtainable information.

This type of examination is becoming less frequent due to the large amounts of data being used; some agencies and examiners still feel that only the full exams should be conducted; they believe the time saved by shorter exams doesn't balance out the possibility of missing additional evidence. But the general school of thought is to obtain enough evidence to prove the case and then move on.

![Using EnCase during a partial exam, and showing a generic example of how the tool can be used.](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2410.png)

**Figure 24.10. Using EnCase during a partial exam, and showing a generic example of how the tool can be used.**

![Using EnCase during a full examination](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2411.png)

**Figure 24.11. Using EnCase during a full examination**

Regardless of which examination method is used, the underlying process is the same. The process must be documented at every step. Accurate logs, documented and tested methodologies, and validated equipment must be used. All equipment used by the examiner must be validated by the user before any analysis can be done. This ensures the validity of the tools as well as the examiner's ability to use the tool in the correct way. [Figure 24-12](ch24.html#process_followed_during_data_analysis) outlines briefly the process of this data analysis.

![Process followed during data analysis](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2412.png)

**Figure 24.12. Process followed during data analysis**

### Documentation

The examiner's report is a direct reflection of the amount done. The greater the detail in the report, the less there is left to question about the incident. The report should be written as concisely as possible but still do the following things:

- Accurately describe all the details
- Be understandable to decision makers
- Be able to withstand a barrage of legal scrutiny
- Be unambiguous and not open to misinterpretation
- Give an unbiased presentation of facts
- Be easily referenced
- Include all information required to substantiate the examiner's conclusions, if these are presented
- Be created in a timely manner

Most automated tools will generate a report. These should be used as a supplement to the examiner's report. An examiner developing a final report should use screen captures, images from the evidence (if appropriate), and any other key items that will assist in the completeness of the report. [Figure 24-13](ch24.html#process_from_evidence_collection_to_repo) shows the entire process in brief.

![Process from evidence collection to report generation](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2413.png)

**Figure 24.13. Process from evidence collection to report generation**

### Evidence retention

When the investigation is complete, the information must be stored in a way that meets the standards of evidence. The evidence may be needed in the future for either trial or follow-up. Retention policies vary based on the type of incident and the current policies of the judicial district and law enforcement agency.

The form of retention can vary greatly and will be affected by the amount of digital evidence collected during the investigation.

Retention of digital evidence is typically done in the following manner. The original digital device, which should have been stored after completion of the imaging, is stored until investigation of the incident has come to a conclusion. The forensic image, if copied to a physical device, will also be stored until the incident has been resolved. The final thing is the forensic image file, which is generally stored on a server or other type of storage device and retained until the incident has been resolved.

Disposal of the media is also dependent on the type of evidence contained on the media. [Figure 24-14](ch24.html#process_for_disposing_of_media) illustrates a general guideline for disposing of media.

Media is often stored in a controlled environment, but a few precautions should be taken to ensure it is not damaged or allowed to degrade. Media should not be stored near any type of magnetic devices such as active radio transmitters, magnets, or magnetic fields as this can cause data corruption or loss. Media should not be stored in plastic bags for extended periods of times.

### Legal closure

The final step in the process is the closure of the legal issues surrounding the incident. The examiner's ultimate goal throughout the forensic process has been to identify evidence that can be used to identify:

- Location where the incident originated
- Methodology used
- Suspects
- Victims

![Process for disposing of media](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2414.png)

**Figure 24.14. Process for disposing of media**

When the information has been collected and analyzed in written form, the next step is to determine if some type of legal action can be taken. A number of actions might be taken, including the following:

- Civil action
- Criminal action
- Interoffice action
- Termination
- Suspension
- Fines
- Combination of actions

### Civil

Some cases may be heard in a civil court of law. These types of cases fall outside the criminal arena and generally involve harassment, slander, or business-related activities that do not fit within the criminal justice system. The civil process does not allow for the incarceration of the person behind the incident, but instead may impose financial penalties.

Litigation in the civil court system involving businesses commonly revolves about the lack of safeguards to protect customer data. The evidence collected during the incident is designed not only to identify the person responsible, but also to show that the incident could have been prevented if the business had used "best practices."

### Criminal

The most common arena for the forensic analyst is criminal court. These proceedings are becoming more common in the United States and throughout the world. The analyst's role is to collect the evidence that will prove the defendant was either the sole person or one of several people who committed the crime. Documentation, chain of evidence, and the ability to convey the meaning of the report to the judge and/or jury is what will ultimately prove or disprove the defendant's involvement in the incident.

Criminal courts can impose various penalties on a convicted defendant, including jail, fines, restrictions, or a combination of all three. The examiner's role is critical in obtaining a conviction and any deviation from common practices could result in failure of the prosecution's case. (In some cases the defense can insist on having its own examiner.)

# Proactive Forensics

Traditional forensics is generally reactive and applied after an incident has occurred. Typically, traditional digital forensics is used after an attack to find out what damage was done and to catch the intruder. When suspicious activity is detected, computer forensics is applied to discover and document an electronic evidence trail. It generally relies on static disk dumps or portable probes deployed as the result of an incident.

In short, traditional digital forensics uses a law enforcement approach, in which the forensics investigation begins when a crime has been committed or discovered and after investigators visit a crime scene to seize evidence. However, in a proactive sense, there is an opportunity to actively and regularly collect potential evidence in the form of log files, e-mails, backups, network traffic logs, telephone logs, and the like. This evidence can be collected on an ongoing basis even in the absence of a crime or incident, and hence can be available should there be a forensics investigation.

The term *proactive computer forensics* is being used to describe new technologies and to market products. New proactive forensics tools are emerging and traditional forensics tools can also be used in a proactive way, to detect suspicious activity before it results in damage.

## Methods of proactive forensics

Proactive, ongoing forensics is the ability to catch a crime as it occurs. It involves taking steps to preempt the need to perform traditional reactive forensics. In terms of accountability, proactive computer forensics is being used to exonerate a company before an incident is made public. It has also been used in employee disputes and sexual harassment cases. An example of proactive computer forensics is the use of active monitoring systems that audit the use of a computer and notify the system administrators of any offensive material. Traditional computer forensics are then used to locate and secure the information on the computer for use in potential court proceedings. Another aspect of proactive computer forensics is the design, construction, and configuring of systems to facilitate future forensics analysis. This includes system structuring and augmentation for automated data discovery, lead formation, and efficient data preservation. This method promotes proactively preparing for forensics investigations. In this case, proactive forensics is about changes in user behavior over time and gathering evidence to document potential incidents. One technique includes online preemptive system restructuring that adjusts security resources based on partial or circumstantial evidence. This technique focuses on event-driven system functions. It looks for changes in the behavior of the user. These changes are recorded by system logs, network events, and other monitoring utilities. Computer security focuses on preventive measures, whereas proactive system forensics tries to generate appropriate data to provide good investigation leads and focus the search appropriately. This leads to more efficient data mining and the ability to automatically initiate data mining.

Intrusion detection is closely related to proactive forensics. However, the main focus of intrusion detection is quick detection and understanding of intrusions and attacks. Proactive forensics operates over a longer period of time by setting alerts and adjusting system parameters as necessary. Event-driven data can indicate suspected malicious behavior by a user. This user would then become the focus of data mining efforts to find related security events. This data mining can be performed during a system's idle time. Honeypots and honeynets play a role in both proactive forensics and intrusion detection. They can provide proactive forensics with evidence trails.

Another method of proactive forensics is the use of digital fingerprinting for proprietary data. Digital fingerprints are unique labels inserted into content before distribution. Each digital fingerprint is assigned to a person and can be used to trace who is using the data for unauthorized purposes. This provides a proactive method of evidence gathering and tracing the culprits in cases of unauthorized information dissemination. It is essential that the fingerprints be difficult to remove or modify. Digital fingerprinting is different from digital watermarking because watermarking can be defeated with collusion attacks—two or more people working together to commit a crime. Digital fingerprinting can resist collusion and identify users who attempt to use the data for unintended purposes.

Another example of digital fingerprinting is a technique that calculates the fingerprints of sensitive data on the network. In this case, however, just the data is fingerprinted, it is not assigned to a person. This technique then watches the network traffic and matches the fingerprints of sensitive information that is attempting to leave the network. The technique monitors data in motion and does not require large storage capacities. Violations are detected immediately and the appropriate administrators are notified. Because the system monitors for matches to fingerprinted data, the amount of data that needs to be stored and analyzed is significantly less. Most important, the system is proactive, not reactive.

Process forensics is closely related to proactive forensics in that it merges intrusion detection and checkpointing technology. Checkpoints are periodic snapshots of a running computer program or process. These checkpoints are then used later for forensics and investigations. With process forensics, digital forensics tools can be activated by an automatic intrusion detection system. This allows the collection of forensics information as the incident is occurring.

Forensic readiness employs many proactive forensic techniques. Forensic readiness is maximizing the collection and use of digital evidence while minimizing investigation costs. Forensic readiness includes enhanced system and staff monitoring; technical, physical, and procedural means to secure data that meets evidential standards of admissibility; processes and procedures to ensure that staff recognize the importance and legal sensitivities of evidence; and appropriate legal advice and interfacing with law enforcement.

## An ideal proactive forensics system

The products currently on the market tend to address specific issues in regards to forensics. At a high level, an ideal product would include three main components:

- **Knowledge of the network and systems**—The product can gain this knowledge in multiple ways, including firewall rulesets (knowing what traffic is allowed or denied), systems scans (knowing what ports and services are open on a system), and network traffic analysis (knowing the types and quantities of traffic flowing over the network).
- **Methods of detecting changes, malicious activity, and potential incidents**—This can be accomplished with many of today's existing devices such as intrusion detection systems, intrusion prevention systems, anomaly-based detection, event and log analysis, and behavioral analysis.
- **The forensic analysis method**—This component takes over when a potential incident is discovered. It can be implemented in many ways, but the main goal is to gather sufficient and reliable forensic evidence. This component uses a proactive approach by gathering and preparing the evidence before the potential incident results in any damage. It provides a method to easily gather evidence from various sources including network devices and systems. The forensic analysis component includes the majority of the intelligence of the proactive forensic system. On the low end, it can focus on rules and pattern matching. On the high end, however, it can make extensive use of machine learning and data mining.

There may never be an ideal system that can stop all attacks and security incidents from occurring, but there are ways of getting close to that goal. As technology evolves, more time and effort are invested in analyzing problems and researching solutions. Unfortunately, computer crime will always exist; therefore, a system is needed that takes a proactive approach and collects and preserves data in a manner that is sufficient and reliable for prosecution of the criminal. This system must provide fast and effective data analysis and presentation to provide the forensic analyst with appropriate and timely information.

# Future Research Areas

There are several areas of future research for forensics. First and foremost, new data mining methods are needed to analyze large amounts of stored data. These methods must be forensic-focused and must contain proactive detection techniques. Log aggregation, correlation, and efficient log storage and processing are among the critical areas. Forensic methods must generate appropriate data to provide good investigation leads and focus the search appropriately.

In addition, new proactive measures should be addressed that focus on user behavior and insider threat. Methods must be developed and streamlined that monitor changes in user behavior over time while gathering evidence to document potential incidents. This can include active monitoring systems that audit systems for forensic-specific events. This research area also includes the design, construction, and configuring of systems that facilitate future forensic analysis.

Another research area for proactive forensic monitoring is the tracking of data in motion. This expands upon the research that uses digital fingerprints to trace who is using data for unauthorized purposes. Future research should expand this idea to trace important data in terms of where it has been, who has had access to it, and who has passed it to whom.

Future research needs to identify methods of handling digital evidence collection and proactive forensics in the face of techniques such as steganography, covert communications, and information hiding. In addition, encryption and security protocols pose a challenge to forensic analysis. Methods are needed to assist analysts in dealing with these challenges.

Research also should adapt the design of current products such as intrusion detection systems and honeypots/honeynets so that they provide suitable data sets for forensic evidence. This could be accomplished by plug-ins or modification, but the best approach is to create a new standard that will allow current and future detection and prevention products to produce the appropriate digital evidence output. This also involves the design, construction, and configuring of systems to facilitate forensic analysis.

Lastly, if the appropriate best practices are used and the right methods deployed, digital forensics could become a proactive approach as a whole, instead of still relying in part on reactive measures. This will require more focus on the emergence of computer security and digital forensics and how they can work together in real time. This may involve the automatic activation of forensic evidence collection when certain events occur, or forensic evidence collection could become more of a continuously occurring activity.

Many organizations log all or some of their system information and network traffic. However, these logs can become extremely large, in a short amount of time. Therefore the logs are not analyzed regularly, but are analyzed only after an incident has occurred. Traditionally this reactive analysis is performed with tools like tcpdump.

There are several obstacles to proactive forensics. First, network forensic analysis tools require large storage systems. Second, additional personnel are often required to analyze the large amounts of data being monitored and stored. Also, storing network data can present some liability issues because the data often contains confidential, personal, and sensitive information. Last, searching through vast amounts of logged data is time-consuming and exhaustive. New proactive forensics tools are utilizing techniques that overcome these obstacles.

Taking a proactive stance on gathering and using evidence can also be of benefit as a deterrent. Many incidents are the result of insider attacks. With proactive forensics in place, employees know what the organization's attitude is toward the policing of corporate systems and what actions may have been taken as the result of incidents. A company showing that it has the ability to catch and prosecute this type of inside attacker will dissuade future offenders.

# The Forensic Life Cycle

The life cycle of the forensic process is long and can take several months to several years to complete. The overall ability to complete the process takes skilled dedicated personnel. This life cycle is shown in [Figure 24-15](ch24.html#entire_forensic_life_cycle).

![Entire forensic life cycle](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2415.png)

**Figure 24.15. Entire forensic life cycle**

The overall process is designed and implemented with law enforcement in mind. It is understood that the enterprise incident response strays from this life cycle in several of the areas. The mission and overall goal can be different in the two areas but the ultimate outcome should still remain the same.

# Summary

It is not a matter of whether an organization is going to have an incident but when. Therefore, it is critical that organizations understand forensics so they can properly protect and control access to the evidence. If there is no evidence then it makes it very difficult to figure out what happened and take appropriate legal action.
