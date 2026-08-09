# Chapter 20. Secret Communication

**IN THIS CHAPTER**

- **Cryptography terminology**
- **Exploring symmetric cryptography**
- **Exploring asymmetric cryptography**
- **Learning hash**
- **Using and understanding common practices of encryption**

Many people think of cryptography as spies trading secret messages written with strange symbols that only the author and recipient of the message can understand. Some have even heard of terms such as *cipher text* or *public-key encryption*, but can't readily explain what they are. There are a lot of terms in cryptography, and even more mathematics, making cryptography often confusing. A lack of understanding can create a situation where both parties believe they are communicating securely when in actuality they are not. This is why even a basic level of understanding of cryptography can be helpful.

While cryptography is a vast and complex subject, a little knowledge about the field can be very helpful with respect to security. While a lot of security is the process of putting up walls to prevent an attack, or managing risk when an attack occurs, cryptography plays an important role in an overall security scheme. In security, where little can be proven secure, it is nice to know that at least one tool, cryptography, has mathematical proofs backing up the level of security. However, as with anything in math, these proofs only apply in specific situations, and it is often the case that people try to bend protocols or use cryptographic primitives in ways for which they were never intended; the result can be an insecure system.

While cryptography can be very secure when used properly, the human element of the process should always be considered. Sometimes, even if all the cryptographic algorithms used are secure and have been tested, a password left taped to a computer screen can void all security provided by cryptography. Although the human aspect of cryptography is not a focus in this chapter, it should always be kept in mind.

First, some general terms are introduced that are used throughout the chapter. Next, a short history of cryptography is provided to give some background as to who uses cryptography and classic ciphers. Then, the four basic cryptographic primitives are explained in detail with examples of real-life encryption algorithms and their uses. Finally, the differences between algorithms and implementations and between proprietary and open source are discussed.

### Note

While this chapter discusses these primitives and how they fit into the overall use of cryptography, it is beyond the scope of this book to discuss how these algorithms were created or why they are believed to be secure. Breaking these algorithms is not discussed either.

# What is Cryptography?

Many books have been written on the broad topic of cryptography (crypto) because it is very complex. In this chapter, we are going to cover some of the key concepts and principles that you need to understand so that you can apply them to secure and covert communication.

According to `www.dictionary.com`, cryptography is defined as "The process or skill of communicating in or deciphering secret writings or ciphers." In its most basic form crypto deals with keeping secrets secret. It deals with ways to transform information in such a manner that no one besides the intended recipients can read what was actually sent. More advanced crypto techniques deal with ensuring that the information being transmitted has not been modified in transit. Some argue that crypto also includes techniques used to crack current encryption schemes. All the various aspects will be examined in this chapter.

## Why is crypto important?

Crypto is critical for almost any society to exist. Any society, no matter how big or small, needs to convey information in a secure manner. In some situations this is both convenient and nice to have, but in others it can be critical for certain information to be sent in a secure manner. As discussed in the [Chapter 1](ch01.html), communication is critical to everything we do and ensuring the confidentiality of communications is a critical part of any communication scheme.

### When is crypto good?

Whether crypto is good or bad is really in the eye of the beholder. For instance, when criminals use cryptography to successfully commit a crime then it benefits the criminal, but it's a major problem for law enforcement. This section focuses on good, ethical law-abiding use of cryptography. However, if you weren't a law-abiding citizen you could just switch this heading with the next and the section would still be useful to you.

In an individual sense, crypto is good whenever it's used to help further a righteous cause for an individual. From society's standpoint, crypto is good whenever it's used to protect our freedoms and keep our citizens safe. Some specific examples of good crypto uses are the following:

- Protecting the launch codes of nuclear weapons
- Protecting the location of our troops
- Protecting the names of suspected criminals until they are actually charged
- Protecting the salaries of employees
- Protecting the formula for a new product
- Protecting a new research idea

You can see that all these cases start with protecting information to keep some unauthorized or hostile entity from seeing it. These areas encompass government, research, and commerce and show how critical cryptography is to protecting our way of life.

### When is crypto bad?

Deciding the line between the good and bad uses of cryptography can be a heated topic, and may be debated as passionately as gun control. On the one hand the use of crypto is every person's right and freedom — to be able to communicate without anyone eavesdropping. On the other hand, law enforcement officials need to be able to track criminal activity so that they can arrest and prosecute lawbreakers. At what point does the use of crypto become bad? For example, when two ethical scientists discuss a patent idea in private, that's clearly a good use. The scientists need to be sure that no one else will steal their idea. However, if the scientists were exchanging ideas on how to bomb a building, than that would definitely be a bad use. Society must decide when it's proper for authorities of some sort to read messages, and when it isn't. Crypto isn't bad in itself — it's simply a tool that can be used in good or bad ways.

## Goals of Cryptography

Whenever I examine security technologies and try to determine their strengths and weakness, I always like to map this analysis back to the three core areas of network security: confidentiality, integrity, and availability. These three areas have stood the test of time because they represent the critical concepts of network/computer security and because they emphasize what's important when you're trying to protect your networks.

### Confidentiality

Confidentiality deals with detecting and deterring the unauthorized disclosure of information — essentially, keeping secrets secret. I have information and I want no one else to find out about it unless I reveal it to them. Confidentiality is what most people think about when you say security. If you went out on the street and asked people to give you a short definition of security, many respondents probably would include confidentiality in their answer.

This is one reason why some people protect their homes with security alarms and safes. Besides not wanting to lose their belongings, they have information with monetary value, often their financial records, that they want to protect and keep from access by unauthorized persons. While safes may be used to protect money and valuables, most people choose banks for this purpose — a bank's protective resources usually are greater than those of the home.

Because confidentiality is a priority for many people, it's no surprise that this was one of the first security problems addressed when the Internet and its predecessors began. Remember that one of the first protective mechanisms built into Web browsers and servers was SSL, which stands for Secure Socket Layer. Some people believe they've taken care of security by using SSL. When a security specialist asks what else they're doing, they're at a loss. But in terms of securing the World Wide Web, the sort of confidentiality provided by SSL is just the starting point.

Cryptography directly addresses the problem of confidentiality. The main goal of cryptography is to take a plain text message and garble it in such a way that only the intended recipient, and no one else, can read it.

### Integrity

Integrity deals with detecting and preventing the unauthorized modification of information. This type of attack can potentially be more dangerous than a confidentiality attack. With a confidentiality attack someone reads something that he or she should not have had access to, but the impact to the organization depends on what is done with that information. If the attacker does nothing with it then the threat is minimal. However, with an integrity attack someone changes the value of a key field to a false value, which creates an immediate threat. You now have invalid information, which could have a detrimental impact on your organization.

People often think that if their data is protected and cannot be read, no one can modify it. That assumption is wrong; people can modify and use information without being able to read it directly. As an example, consider a spreadsheet that an HR department maintains to track people's positions and salaries across the company. The fields containing names and positions are kept in plain text because that information is not considered secure. But the salary field is encrypted. As an employee, I don't know what other people are making, but I do know my own salary, and can infer that someone else, say the vice president of engineering, makes more than I do. If I paste the vice president's encrypted figure into my salary field, I may be able to make some logical guesses about it. I have performed an integrity attack even though I did not, strictly speaking, violate confidentiality.

This type of attack was popular on UNIX systems a while back. Originally, the etc/passwd file contained both the user IDs and the encrypted passwords. If you wanted to gain root access (which is "god access" on the computer) you needed to find out the root password. To accomplish this, you create a new user account in which you know the password. You would then go into etc/passwd and take the encrypted value for the password for the account you created and copy it over the current value that lists the root. Usually, you would save the original value of the root in order to put the system back the way it was when you were done. By doing this you could change the password for the root without knowing the original value. Even though it might seem as if you need to breach confidentiality in order to breach integrity, these examples show this is not always true.

Cryptography also addresses integrity by performing verification and validation of data. In essence, it performs a digital signature across the information and if any bit of data changes the signature will be different. This allows sites to perform integrity checks against their information and ensure nothing has changed in transit.

A great example of this is a program called Tripwire. Tripwire performs cryptographic hashes or digital signatures of all your key files and informs you if any of these files have been modified.

A key thing to remember is that when you use cryptography only to strictly protect against integrity attacks, there is no assurance of confidentiality protection — an attacker couldn't modify the information, but might still read it. You'll see later how you can use different methods of cryptography to provide both integrity and confidentiality for key information.

### Availability

Availability deals with detecting or preventing the denial of access to critical information. Availability (or denial of service) attacks can be broken down into two general categories: incorrect data and resource exhaustion. Denial of service attacks through incorrect data deal with sending data that a service or process is not expecting and that causes the system to crash. Applying a vendor patch or reconfiguring the system can usually fix this type of attack. Most times, incorrect data attacks can be prevented. Resource exhaustion attacks are the most popular availability attack and are extremely difficult to prevent. Essentially an attacker will try to send more data than your network, router, or server can handle, which will overload the system as well as make it unable to respond to other attacks. Preventing this type of attack is difficult and usually involves acquiring additional resources. Cryptography is not a useful solution for preventing availability attacks.

Because there is no single answer for every security problem, you should remember one of the key principles of security — defense in depth. Cryptography plays a key role but must be combined with other defense measures to create a robust solution for your site.

## Sub-goals

When talking about network security solutions, it's useful to trace the goals of a particular technology back to the three core areas of security. However, as with cryptography, these technologies also have additional goals that are critical to look at. Two of the additional goals are authentication and non-repudiation.

### Authentication

In most transactions you must be able to validate that people are who they say they are. If I buy a car or an object off the Internet, the entity selling me the goods wants to be able to authenticate who I am. Identifying who an individual is at the other end of a transaction is critical for many reasons. For merchants, the most important reason usually is that they want to make sure they'll be paid for what they're selling. The information is also critical for follow-up business and warranties.

Authentication also plays a role when we talk about e-commerce and electronic transactions. Not only do merchants want to validate who a person is, but they also want to ensure that what they agreed to sell and the amount they agreed to sell it for does not get modified. In this sense they are authenticating the validity and accuracy of the information. This is similar in some ways to an integrity check but it provides a higher validity standard for the information. With an integrity check, you just want to make sure the information has not changed. With authentication it may be all right if the information has changed, as long as it is still accurate. This becomes very critical in Web transactions because at the end of the transaction a server will send the seller's client all the charges. During selection, the client can add or remove items, change quantities, and select a shipping method, before sending the information to the server. The server needs to be able to authenticate the accuracy of the information — is the seller in fact getting the information the buyer intended? Without a human in the loop, this is a big concern.

### Non-repudiation

One of the last bills that President Clinton signed before leaving office made digital signatures binding for contracts with the federal government. For a digital signature to be binding, you must prove that the person sent it. You must also ensure that no one else could spoof their signature. This is exactly the goal of non-repudiation, which aims to prove in a court of law that someone sent something or signed something digitally. Without non-repudiation digital signatures and contracts would be useless.

Let's suppose that you sent a company an order for 400 widgets at $100 apiece, but then 10 days later the price of widgets dropped to $40 apiece. If you could repudiate your contract by denying that you sent the order, digital contracts and signatures would be worthless. The seller's only recourse to prove that the transaction occurred would be to argue that there was a verbal contract. In order for e-commerce to proceed, there has to be some way to implement non-repudiation across digital transactions just as in written contracts. Although the term may be unfamiliar, non-repudiation exists whenever you sign your name to a contract. You are obligated to fulfill your side of the contract and if you do not, you can be sued, taken to court, and either forced to perform or to pay a penalty.

One of the big strengths of cryptography is that it can be used to provide non-repudiation for any type of digital information including digital contracts.

# General Terms

As with most subjects, understanding basic terms can help you understand the subject clearly, and cryptography is no exception. The terms defined in the following list pertain to cryptography and will be used throughout the rest of the chapter:

- **Brute-force attack**—This is the process of going through all the possible keys until the proper key is found that decrypts a given cipher text into correct plain text. Because all encryption is vulnerable to a brute-force attack, this type of attack is usually the upper bound of resistance the algorithm has. All encryption algorithms will eventually fall to brute-force attacks given enough time. It can be helpful, then, to see in the best case how long a piece of cipher text can remain cipher text, the idea being that if an algorithm's only attack vulnerability is through the use of brute force and there are enough possible keys to slow down such an attack, the algorithm can be considered secure. Algorithm strength is discussed in more detail later in the chapter.
- **Cipher text**—Data in its encrypted, unreadable form. Cipher text only refers to encrypted data and says nothing about the type of data before encryption, or the algorithm used to encrypt the data. Encrypted data is a synonym for cipher text.
- **Cryptanalysis**—The process of analyzing cipher text or the algorithms to find a weakness so that plain text can be extracted from the cipher text without the key. Cryptanalysis is done by cryptanalysts who use techniques such as frequency analysis, explained later, to find patterns in the cipher text.
- **Decryption**—Taking cipher text and using a key to convert it into plain text. In most cases, the algorithm or key used to encrypt the data is not the same as the one used to decrypt the data. Decrypting cipher text should not be computationally feasible without the proper key.
- **Encryption**—The process of taking plain text and using a key to convert it into cipher text. Ciphers, algorithms, or schemes are used to encrypt data. All encryption algorithms require the use of a key, and must be able, with the proper key, to be reversed, converting the cipher text back into the original plain text.
- **Key**—A random piece of data used with encryption and decryption. Encryption and decryption algorithms require a key and plain text or cipher text to produce cipher text or plain text, respectively. The key is usually shared only with those parties that should be allowed to encrypt and decrypt messages.
- **Plain text**—Refers to any type of data in its original, readable, unencrypted form. A text document, an image, and an executable are all examples of plain text. It is important to note that plain text refers only to unencrypted data.

# Principles of Cryptography

In order to understand how crypto works and why it works, you need to know some key principles of cryptography. By looking at the following principles in more detail, you'll get a better understanding of how the process works:

- You can't prove something is secure, only that it's not secure.
- There is a difference between algorithms and implementations.
- You should never trust proprietary algorithms.
- The strength of an algorithm is based on secrecy of the key, not the algorithm.
- Cryptography is more than SSL.
- Cryptography must be built-in—like electricity.
- All cryptography is crackable; it's just a matter of time.
- Secure today doesn't mean it will be secure tomorrow.

## You can't prove something is secure, only that it's not secure

The ideal situation is to secure and protect your information, without weakness that can be exploited, and to prove that your information is secure. Unfortunately, with crypto there is no easy way to prove that an algorithm is secure. The only way to test its security is to have a bunch of really smart people try to crack it — if after seven years or so they haven't, then you can assume it's secure. There could still be a vulnerability that they missed but the chances are slim. This is why new algorithms are not considered secure for five to eight years; you have to give people enough time to try to break them.

It's not possible to prove an algorithm is secure, but you can prove it is not secure by breaking it. If someone finds a vulnerability, then its insecurity is no longer in question. However in doing such code-breaking, there is no mathematical principle to guarantee that you've tested for every possible vulnerability. You can test for known vulnerabilities and for vulnerabilities that were found in other algorithms, but there's no way to determine that the new algorithm is not susceptible to some undiscovered vulnerability. New ways to break crypto are discovered all the time, which is why few new crypto algorithms actually make it beyond testing. Most algorithms that are released are broken so quickly, often with major holes found, that they're not worth pursuing or would entail fixes that would defeat the reason for the algorithm in the first place. A very fast algorithm might be found to have a major flaw, but fixing the flaw would make it too slow to be of use — no matter how secure it now was. Even if an algorithm is not broken, this doesn't mean it's totally secure, just that no one has found a way to break it.

A case in point could be the DES (Data Encryption Standard) algorithm. It's been rumored for years that the National Security Agency, which worked on the algorithm with IBM, planted a back door in the system, but this has never been proved. We simply don't know. (It could be argued, of course, that those who made the algorithm were so good that if they didn't want anyone to find their back door, no one ever would!)

## Algorithms and implementations aren't the same

When talking about the strength of various encryption schemes, it's important to remember the difference between an algorithm and an implementation of that algorithm. An algorithm is the blueprint or design for the encryption process to follow. An implementation is someone taking that design and putting it in a working piece of software. The problem when you take an algorithm and implement it in a piece of software is that the designer has to decide on or interpret certain properties.

Because the algorithm does not specify every single detail, an implementation is really a person's interpretation of how the algorithm should work. For example, the algorithm may require choosing a large prime number, but how that number is chosen may result in either a solid encryption scheme or one that is weak and easily broken.

Remembering this rule becomes very important when you hear about encryption being broken. The media usually cannot differentiate between whether a weakness was found in the algorithm, in the implementation, or in both. If a weakness was found in a specific implementation and not the algorithm itself, that generally means someone misunderstood the specifications and implemented them incorrectly. This is usually what has happened when you hear about a popular scheme being broken. It was reported at one time that triple DES had been broken. But it turned out that a small developer, without much understanding of crypto, had implemented his own version of Triple DES, which was easily broken. When a weakness is found in an implementation, the algorithm and all other implementations may be fine; it's just that particular software version that shouldn't be used.

But if a weakness is found in the algorithm, then there's a major problem, because all implementations are also broken. So it's critical that, when you hear an encryption technique has a weakness or has been broken, you clarify what happened. Weak implementation is not critical, but a weak algorithm is.

You'll find more later in this chapter about the difference between algorithms and implementations.

## Never trust proprietary algorithms

As noted earlier, the only way to prove that a given crypto algorithm is reasonably secure is to allow smart people try to break it. Another interesting point is that all the algorithms we use today such as Triple DES and RSA, were not perfect when first released. There are always problems, either major or minor, with a new algorithm, and they're only found by relentless code-breaking efforts.

Thus, you should never trust a proprietary algorithm, where all the information and details are concealed. No one has looked at it or validated it externally. If a vendor ever says, "We use proprietary encryption," then you should run for the hills.

Vendors sometime claim that proprietary algorithms are actually more secure because no one knows how they work and therefore they're harder to break. This is essentially a "security through obscurity" argument. But this doesn't work either for security or cryptography. Attackers are smart and will always be able to figure out what you did. Even if they can't figure out the inner workings, mostly likely they can still break it because a proprietary algorithm is almost certain to have weaknesses built in.

So you should never trust proprietary algorithms. The only way to have strong crypto is to share the inner workings of the algorithm. Good crypto is designed in such a way that even if people know how the algorithm works, the encryption is still secure. If the security of your crypto algorithm is compromised by the transparency of its inner workings, it should not be used.

## Strength of algorithm is based on secrecy of the key, not the algorithm

As explained in the previous section, the strength of crypto is never based on secrecy of the algorithm. The strength, rather, is in the secrecy of the key.

The fact that someone knows I am using RSA does not make it any easier for them to crack my cipher text. As long as they don't know the key I used to encrypt the information, they can't decrypt my cipher text. This is the same logic used in a padlock. Knowing the "algorithm" for the padlock — how it's constructed — doesn't help you open a lock. What keeps it safe is keeping the key safe. How silly would it be if I put a lock on my shed to protect my belongings, but taped the key to the back of the lock? The care you take to safeguard your padlock key must also be used in protecting your crypto key.

That might seem self-evident, but let's look at some examples. Wireless technology has a lot of issues with security and lots of problems trying to protect information as it flies through the air. WEP was developed to provide encryption of information flowing over the wireless network. The problem is that the key used to encrypt the information is embedded within the message. Therefore anyone who intercepts the encrypted message can also extract the key and read the information. The key is on the back of the lock.

## Cryptography is more than SSL

SSL, which stands for Secure Socket Layer, allows for point-to-point encryption between a client's browser and a server. It's mainly used to protect credit cards or any information in transit, but only while it is in transit. The information is unprotected before it leaves the client's system and once it gets to the server. SSL has nothing to do with end-point encryption yet end point encryption is critical to the overall security of the information. You can quickly see that while SSL helps, there is a lot more to crypto than just SSL, You also have to make sure your information is protected in any system it is stored on. Security must address all points of vulnerability, remembering that an attacker is always going to try to break the weakest link. Why try to break the SSL encryption when the end-client system is wide open and the information is unprotected? You must always look at the entire picture.

## Cryptography must be built in – like electricity

Crypto is more than just building a functional site and adding in crypto or SSL at the end. Crypto must be designed into a site from the beginning.

Designing crypto in from the beginning is like putting wiring in a new house. You wouldn't build the house and then tear up the walls to add the electric wiring. But some people still try to design the site, and then put crypto in as an afterthought. Maybe that explains why so many sites still get broken into.

## All cryptography is crackable; it's just a matter of time

Anyone who claims to have crypto that's uncrackable is lying to you. Crypto is based on a key, so in the worst case someone can try every possible combination of a key until the plain text is obtained. This type of attack is called a brute force attack. But how do attackers know if they're successful? They have to be able to recognize that what they've obtained is the original plain-text message. If you're using English text this is easy, but if you're encrypting machine code this could be much more difficult.

Still, all encryption is crackable from a brute force standpoint—it's just a matter of time. A brute force attack tries every possible combination of keys, and you have to assume the attacker has all day, all month, all year, all his lifetime.

## Secure today does not mean secure tomorrow

Computers are constantly getting quicker and quicker. A crypto algorithm that could be brute-forced in 40 years just 5 years ago might only take 10 years today, based on current computing power. Just because something was secure yesterday doesn't mean it will be secure today.

You can also see that this isn't linear. Let's say that in 1990 a given algorithm took 50 years to crack based on current computer speeds. If it took computers 10 years to get 10 years faster, then the same job in 2000 would take 40 years. But of course computers get faster at an accelerating rate—by 2000, a 50-year code-breaking job might be down to 10 years. So if you need to protect something for 25 years you should pick crypto that will take 500 years to crack based on today's standard; that way, it may not be cracked until 2035 or so.

An example of the problem is DES.

DES is no longer considered secure, not because the algorithm has been cracked but because of the key length. DES has an effective key length of 56 bits (it's really 64 but 8 of the bits are used for parity and don't count against the core key length). Triple DES is the *de facto* standard today and has an effective key length of either 112 or 168 bits depending on which mode is used. Triple DES can be used with two keys or three keys. With two-key 3DES you encrypt with the first key, decrypt with the second and then encrypt with the first key. With standard three-key 3DES you would encrypt with key 1, than key 2, followed by key 3.

# Historic Cryptography

This section takes a brief historic look at the various types and uses of cryptography.

## Substitution ciphers

Most people are unaware of the impact cryptography has had on the world and on their daily lives. As far back as Caesar, cryptography was used to protect messages. Caesar would encrypt his messages before giving them to messengers, protecting them from being read while in transit. Caesar used a simple method of encryption called a *substitution cipher*. A substitution cipher maps each letter in the alphabet to another letter. For example, the letter *a* might be mapped to *z*, *b* to *y*, and so on through the alphabet. Caesar used to replace each letter in the alphabet with the letter three letters to the left of it, wrapping around at the end of the alphabet. This mapping is shown in [Figure 20-1](ch20.html#caesar_apostrophy_s_encryption_scheme), where the letters in the top row are the plain text letters and the ones in the bottom row are the corresponding letters in cipher text.

![Caesar's encryption scheme](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2001.png)

**Figure 20.1. Caesar's encryption scheme**

Using this encryption scheme, or cipher, if you were to encode the word *cryptography*, you would look up the letter *c* in the top row and find the letter *z* corresponding to it in the bottom row. Applying this process to all the letters yields the following:

- **Plain text:** CRYPTOGRAPHY
- **Cipher text:** ZOVMQLDOXMEV

Without the table, decoding ZOVMQLDOXMEV into CRYPTOGRAPHY would seem like an impossible task. However, some cryptanalysts realized that breaking such a cipher was very easy; they needed only try 26 different substitutions or rotations of the alphabet before the cipher text would be converted into plain text, making sense of the words.

You may have noticed that this cipher does not have a key. In the definition previously given, an encryption algorithm requires both plain text and a key to create cipher text. It seems as though this algorithm requires only plain text to create the cipher text. However, this is not the case. The key in this algorithm is the table shown in [Figure 20-1](ch20.html#caesar_apostrophy_s_encryption_scheme). This table acts as the key for the algorithm, mapping plain text letters to cipher text letters.

### Vigenere cipher

To create a more secure encryption algorithm, Blaise de Vigenere, in the sixteenth century, proposed the Vigenere cipher. He created a cipher that works by using a keyword and substituting plain text letters for cipher text letters according to the keyword. However, instead of a simple rotation of the alphabet, Vigenere's cipher assigned a number to each of the letters in the alphabet and then used the value of each letter in the keyword to add to the value of each letter in the plain text, obtaining the cipher text. If the value of the two letters added together was larger than 26, 26 was subtracted from this value to obtain the cipher text character. This process was repeated for each letter in the plain text using the next letter in the keyword, and repeating the keyword as many times as needed to compensate for the length of the plain text.

The numbering for the alphabet was simple and always remained the same: a = 1, b = 2, and so on until reaching z = 26. A key was constructed for each message, unlike the Caesar cipher, which used the same key for each message, making it more secure. By creating a keyword with multiple letters instead of just a single letter rotation for the entire message, it had the effect of using as many different substitution ciphers as there were letters in the keyword. Using the same sample message, CRYPTOGRAPHY, and the keyword LUCK, the plain text is encrypted into NLAZEIIBLJJI, as shown:

- **Plain text:** CRYPTOGRAPHY
- **Key:** LUCKLUCKLUCK
- **Cipher text:** NLAZEIIBLJJI

Unfortunately, like the Caesar cipher, this cipher, too, was broken. To obtain the plain text from the cipher text by brute-force methods, trying all possible combinations, would take a very long time even with today's computers because the size of the key is not known. So, to attempt every possible keyword you would need to start with words that are of size 1, then words of size 2 (meaning begin with words that are one letter in length, then words of two letters in length), and so on. However, nothing specifies in the encryption algorithm that the keyword must be an English word. In fact, keys or keywords are often a random string of bits or letters, as you will see later. So attempting to crack this cipher would require going through all 26 letters in the alphabet with all different sizes of combinations up to the total size of the message (there is also nothing that states the keyword must be smaller than the plain text, only no larger). Assuming the keyword was no longer than 10 characters, and that only the 26 English letters were used, that would yield 146,813,779,479,510 possible combinations to try. Using a computer that could try a million keywords per second, it would still take four years to break the encryption.

However, using a technique called *frequency analysis*, Vigenere's cipher can be broken quite easily. One important property about the English language is that not all of the letters appear with the same level of regularity. For example, can you pick out what is very interesting about the following paragraph?

> *This is an unusual paragraph. I'm curious how quickly you can find out what is so unusual about it. It looks so plain you would think nothing was wrong with it. In fact, nothing is wrong with it! It is unusual though. Study it, and think about it, but you still may not find anything odd. But if you work at it a bit, you might find out! Try to do so without any coaching! You probably won't, at first, find anything particularly odd or unusual or in any way dissimilar to any ordinary composition. That is not at all surprising, for it is no strain to accomplish in so short a paragraph a stunt similar to that which an author did throughout all of his book, without spoiling a good writing job, and it was no small book at that. By studying this paragraph assiduously, you will shortly, I trust, know what is its distinguishing oddity. Upon locating that "mark of distinction," you will probably doubt my story of this author and his book of similar unusuality throughout. It is commonly known among book-conscious folk and proof of it is still around. If you must know, this sort of writing is known as a lipogram, but don't look up that word in any dictionary until you find out what this is all about. — Unknown*

The interesting or amazing thing about the preceding paragraph is that it does not contain the letter e; however, e is the most commonly used letter in the English language. It is the fact that some letters are found with such precise regularity that messages encrypted using the Vigenere cipher can be decrypted without the use of the keyword. This is done by computing the *index of coincidence*. The index of coincidence is the probability that a letter in a string and a letter in the shifted version of the string appear in the same place. This is sometimes referred to as *autocorrelation*. To calculate the index of coincidence, you use the formula shown in [Figure 20-2](ch20.html#formula_for_calculating_the_index_of_coi).

![Formula for calculating the index of coincidence](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2002.png)

**Figure 20.2. Formula for calculating the index of coincidence**

This formula sums up the probability of a reoccurring character squared, where the summation runs from zero to the amount of shift. To apply this formula to breaking the Vigenere cipher, or any other substitution cipher, the index of coincidence is calculated for various shifts, *s*, starting at 1 (1 being the value or position of *s*) and working up. When an index of coincidence is found that is equal or close to that of English text (0.066), the key length, or the shift, has been discovered. This works because the key is repeated throughout the encrypting of the plain text. It is this repeating of the key that causes multiple characters in the message to be substituted by the same shifted alphabet. This reuse of the key is sometimes called *depth*, and it is very dangerous, making any otherwise good encryption algorithm insecure.

### Note

If you take nothing else from this chapter, realize that the reuse of a key is the leading cause for encryption being broken (next to leaving the key or password taped to your monitor, of course).

Once the key length has been discovered, breaking the Vigenere cipher is done with frequency analysis and some brute force. English, like most human-created languages, has a precise repetition of letters. This fact allows us to compute the index of coincidence for English (0.066), allowing us to find the key length. It is this same frequency of letters appearing that enables the discovery of the key. [Table 20-1](ch20.html#frequency_of_letters) shows the frequency with which letters in the English language appear in text. This table was calculated by taking a large corpus of text and counting the occurrence of each letter.

**Table 20.1. Frequency of Letters**

| Letter | Frequency | Letter | Frequency | Letter | Frequency | Letter | Frequency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 8.50% | H | 3.00% | O | 7.16% | V | 1.01% |
| B | 2.07% | I | 7.54% | P | 3.17% | W | 1.29% |
| C | 4.54% | J | 0.20% | Q | 0.20% | X | 0.29% |
| D | 3.38% | K | 1.10% | R | 7.58% | Y | 1.78% |
| E | 11.16% | L | 5.49% | S | 5.74% | Z | 0.27% |
| F | 1.81% | M | 3.01% | T | 6.95% |  |  |
| G | 2.47% | N | 6.65% | U | 3.63% |  |  |

By setting the shift, *s*, to 25 and applying the formula for the index of coincidence, the index of coincidence for English text can be found—0.066. The value for random text is 0.038. With the key length known, all the letters of the cipher text are broken up into strings. Each string represents a letter of the key. For example, if the key is four characters long, the cipher text is broken into four strings where the first letter of the cipher text is the first letter of the first string, the second letter of the cipher text is the first letter of the second string, the third letter of the cipher text is the first letter of the third string, the fourth letter of the cipher text is the first letter of the fourth string, the fifth letter of the cipher text is the second letter of the first string, and so on through all of the letters of the cipher text. This way, all the letters in a string are encrypted with the same letter of the key. Then each string is analyzed and a table like [Table 20-1](ch20.html#frequency_of_letters) is constructed for each string. Because the substitutions for each string are only a shift of the real alphabet, matching the English frequencies with the created frequency table for each string is usually easy. Keep in mind that all of this can be done in seconds, rather than years, with a computer. If one of the strings does not yield a frequency table that matches some shifted version of the English frequency table, brute force can be used to determine that string's shift. For example, when you piece back together the strings after all but two have been decrypted, it is usually easy to figure out the remaining characters from context of the other characters, another nice property of the English language.

Again, the key concept to take away from the Vigenere cipher is that reuse of the key can be a costly mistake. This is true for any cryptography system, no matter how simple or complex. What would happen, however, if the key was never repeated? What if the length of the key matched exactly the length of the plain text? How could the index of coincidence be calculated? The answer is that it could not. Using the index of coincidence to find the key length relies completely on the fact that the key is repeated. This brings us to a proven, 100 percent secure cryptography cipher, the *one-time pad*. The one-time pad uses the same basic cipher as the Vigenere; however, instead of having a key that repeats over and over to match the length of the plain text, it never repeats. The letters of the key are picked at random and have no correlation to the plain text. These types of ciphers are 100 percent secure because there is no cryptanalysis that can be performed to find patterns in the cipher text that can then be leveraged to obtain the plain text.

The one-time pad was used by the military to communicate covertly between field agents. Each agent was given a pad of paper that contained randomly selected numbers between 0 and 25. Two copies of each pad were made. One was given to the agent and the other was kept at the headquarters they were to communicate with. To encrypt a message, the agent shifted the position of the first letter of the plain text by the first number in the pad. The second letter of the plain text was shifted by the second number in the pad. This continued until all of the letters in the plain text were encrypted and the resulting cipher text was left. Assuming the numbers were randomly created, the cipher text was completely secure and only the agent and headquarters could decrypt the message. While this idea was completely secure, it had logistical flaws. The numbers could not be generated randomly and they would repeat or have patterns that could be detected and reproduced by an agent who carelessly discarded part of the pad. Also, the pads were usually not long enough for more than a few messages. With the agents unable to obtain a new pad, they simply reused the pad starting from the beginning. This reuse of the pad, even across multiple messages, caused the same problem the Vigenere cipher had. This method, however, has been improved upon with the use of computers.

### XOR and random number generators

Because the one-time pad is 100 percent secure, a few logistical problems were overcome so that the method could still be used to securely communicate messages. Instead of simply rotating characters, a more modern approach was taken with the use of the *XOR function*. The XOR function is a binary operation performed on two strings of bits, and resulting in a third string of bits. This function is defined using [Table 20-2](ch20.html#the_xor_function). In general terms, whenever two bits are not the same the resulting bit is a 1, and when they are the same the resulting bit is a 0.

**Table 20.2. The XOR Function**

| A | B | A XOR B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Instead of using simple addition, which had the problem of the resulting number being larger than the character set, XOR can be used in the same way as shifting with the same level of security, but without the problem of the result not mapping to a character. XOR also has a very nice inverse property just like addition — for example, A XOR B = C, A XOR C = B, and B XOR C = A. If A represents a plain-text character and B represent a key character, then C is the resulting cipher text after encryption using the XOR function. To decrypt, you simply reapply the XOR function to C and B or the cipher text and the key. Without the key, it is impossible to know what the plain text was. All possible values can work for the key, but only one returns the proper results. If the key is just as long as the plain text, and the values generated for the key are done so randomly, this method of encrypting is perfectly secure.

However, there still remains one problem with using this method of encryption, the generation of perfectly random numbers or bit strings to be used as the key for XORing. This problem is not easily solved because computers are deterministic machines by design. The result of a computer operation is always the same, so generating random data is very hard. More important than the data being completely random is that the data cannot be predictable. If a few bits of the random stream are revealed to an attacker, a likely situation, the system still needs to be secure. This means that from knowing all previous random values the next value cannot be determined. The generation of random data is discussed further later in this chapter.

## Ciphers that shaped history

The idea of substituting one letter for another carried on to World War II, where the Germans created a machine called Enigma that worked on the same basic principle of substituting each letter for another. However, instead of the substitution being simple, it was a complex set of substitutions that changed while the message was being typed. Rotors in the machine tracked these substitutions. It was the different speeds at which these rotors advanced and the ability to change rotors that provided the machine's security. While the machine was very complex and did a good job of encryption, it was the Germans' belief that letters in plain text should not be substituted for the same letter in cipher text that proved to be its downfall. This poor assumption and design decision greatly reduced the number of possible combinations for substitution making the machine weak. The U.S. was able to exploit this weakness and decrypt messages without the key, essentially breaking Enigma.

Following the Germans' lead, the Japanese created a machine called Purple. This machine was modeled after Enigma but used telephone stepping switches instead of rotors to create the character mappings. This machine proved very important in the war because it was used to encrypt diplomatic communications that hinted at the Pearl Harbor attack. This machine was also broken by the U. S. Government during World War II.

# The Four Cryptographic Primitives

Cryptography is best understood by breaking it into four main areas or *primitives*. Using these primitives, or building blocks, all areas of cryptography are constructed. In fact, some of the primitives are used to build other primitives. For example, without the generation of random numbers it would be very hard to create secure keys for use in any of the symmetric or asymmetric encryption algorithms explained in this chapter.

All of cryptography is based on these four primitives, and the primitives are closely connected. With a full understanding of these primitives you should be able to read any standard that references them and understand protocols built using them. While the design and construction of cryptographic primitives should be left to the experts, it is important to know how they work and interact from a high-level perspective.

It is important to understand the goals of cryptography and these primitives. Cryptography provides three main properties using one or more of the following primitives. These properties are often discussed using the acronym CIA, which stands for *confidentiality*, *integrity*, and *authentication*.

The four basic cryptographic primitives are as follows:

- Random number generation
- Symmetric encryption
- Asymmetric encryption
- Hash functions

Sometimes it is enough to use a single primitive alone to obtain one of the CIA goals; however, most of the time these primitives are used in conjunction to obtain the CIA goal. For example, it requires all four of these primitives together to complete the task of using a credit card to purchase merchandise from a secure Internet site.

## Random number generation

The first cryptographic primitive is the generation of random numbers or, more accurately, random bit strings. While completely random numbers can never be generated from a computer algorithm alone, there are algorithms that create pseudorandom numbers, or numbers that appear to be random. It is the ability to generate pseudorandom numbers that provides keys for all of the encryption algorithms explained later. Even the simplest encryption algorithms, such as the one-time pad, require the generation of pseudorandom numbers.

The numbers created from cryptographic pseudorandom number generators do not have to be 100 percent random; they simply have to be unpredictable to an attacker. If an attacker can recreate the stream of bits used to create the keys for any encryption algorithm, it is as if you have given the attacker your key. By recreating the stream of bits used to create the key, an attacker can recreate the key using the same method because all good encryption algorithms are published (more on this later in the chapter).

Because creating truly random numbers is not possible on a computer, many interesting techniques have been used to get seemingly random numbers. There are two basic approaches to generating pseudorandom numbers on a computer. The first is to design an algorithm that will create what appears to be random numbers. The main problem with this approach is that at some point the algorithm will cycle and you will start seeing the same numbers in the same order. As previously mentioned, this is called *depth* and is very dangerous because the repeated bit stream makes it easy to break encryption.

### Algorithms for pseudorandom number generation

The most basic pseudorandom number generation algorithm is the linear congruent pseudorandom number generator (LCG). This algorithm is a simple function that has as parameters *a*, *b*, and *n*. These parameters characterize the output of the function and should be kept secret. There is also a seed value, which is the first value of the pseudorandom stream. It quickly becomes a chicken-and-egg problem because the seed should be a random number itself. So how do you generate a random seed without a random number generator? The answer is not a simple one, but elements such as time, hardware serial numbers, and so on are all combined to generate a pseudorandom seed. The function for an LCG is shown in [Figure 20-3](ch20.html#the_lcg_function).

![The LCG function](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2003.png)

**Figure 20.3. The LCG function**

Unfortunately, this pseudorandom number generator is not cryptographically secure. With only a few numbers, the parameters to the function (a, b, n) can be determined, leading to the creation of the same pseudorandom numbers in the same order. While this algorithm is not cryptographically secure, it was included because it is a frequently used pseudorandom number generator in simulations and is sometimes incorrectly used in cryptographic situations creating a weak or guessable key.

Two pseudorandom generators that are cryptographically secure are the Blum-Blum-Shub pseudorandom generator and the RSA (which stands for Rivest, Shamir, and Adleman, its inventors) pseudorandom generator. Both of these algorithms rely on a number of theoretical properties that are outside the scope of this book. However, these algorithms are believed to be secure because they require the factoring of large numbers to be broken, and this is believed to be computationally infeasible if the number is large enough.

While neither of these algorithms creates truly random bits, they do create unpredictable bits, making them good generators for use in key creation. However, like the LCG, keeping the parameters used for these generators private is very important. Giving away *p* and *q* for either generator will allow an attacker to recreate the stream of pseudorandom bits, enabling the attacker to recreate the key.

### Using user input to generate numbers

The second approach to creating random numbers on a computer is to track some sort of user input. One common method is to record input from the keyboard and the mouse. These types of programs will ask the user to push random keys on the keyboard and move the mouse around the screen in a random fashion. The idea is that a human mashing the keys of a keyboard or moving the mouse around the screen will be able to create random enough data for key generation. Remember the numbers do not need to be completely random, only nondeterministic, and wild movements of the mouse usually are nondeterministic. The recorded values are then fed into a *hash function* or *stream cipher* (both hash function and stream cipher are explained later) to create pseudorandom numbers. Computer device access times are also used to create pseudorandom numbers. The time at which your hard disk is accessed and the time at which packets are received by your network card are all fed into a mixing function and pseudorandom bits are computed. While these methods might not produce completely random bits, they are usually unpredictable enough to prevent an attacker from recreating your key.

### Whitening functions

Even with the seemingly random mashing of the keyboard and movement of the mouse, there is still some predictability to the values created. This is why these values are put through a mixing and whitening function. A mixing function's goal is to take somewhat random numbers or bits and map them into seemingly random bits. Whitening functions make sure that an even number of ones and zero bits are produced from the pseudorandom bit generator. While mixing functions are usually stream ciphers, block ciphers, or hash functions that are very complex, whitening functions can be very simple functions. Von Neumann created the most classic and simple whitening function. This function works by observing two bits at a time and generating one whitened bit half of the time. The function works as shown in [Table 20-3](ch20.html#the_whitening_function_operation).

Only when the bits are different is 1 the output. Then the first bit is used as the output bit, as shown in the preceding table, where *z* is the output bit. This function reduces the bit basis on a single bit level because only when there is a change in bits, from a stream of 1s to a stream of 0s, is a bit output. While this function helps to remove bias on a single-bit level, it does nothing to remove bias on a multiple-bit level. This function does not help to create random or pseudorandom bits; it creates only a uniform distribution of bits on the single bit level.

**Table 20.3. The Whitening Function Operation**

| X | Y | Output Bit |
| --- | --- | --- |
|  |  | *Z* |
| 0 | 0 | Nothing |
| 1 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 1 | Nothing |

Examples of this method of pseudorandom bit generation can be seen in both Windows and UNIX/Linux operating systems. In the Windows operating system, the function `CryptGenRandom` found in the Crypt application program interface (API) generates its random bits by tracking user interrupts and then feeding these values into RC4, a stream cipher. In UNIX/Linux operating systems, user interrupts are also monitored, and they are put through the SHA-1 hashing function to further mix the bits and help to whiten them. These values can then be found by reading from `/dev/random` or `/dev/urandom`. The only difference between the two is that `/dev/random` keeps an estimate of how much entropy or randomness is in the pool and allows reads only when the level is high enough, whereas `/dev/urandom` will continue to generate bits by simply rehashing the pool for more random bits. For this reason, `/dev/random` is considered a more secure source of random bits than `/dev/urandom`.

### Cast Introduction

Before explaining the next cryptographic primitive, symmetric encryption, it is a good idea to introduce some people that will be used throughout the rest of this chapter. The following are used to designate actual people or computers. The names chosen are not unique to this book; in fact, almost all cryptography explanations use these names. The reason for the names is no more complex than the first letter of their names. Instead of saying, "Computer A sends a message to computer B," you say "Alice sends a message to Bob." The cast of characters is as follows:

- **Alice**—She is an end user/computer without malicious intentions, one of the main users of cryptography.
- **Bob**—He is Alice's friend and is also a main user of cryptography, without malicious intentions.
- **Cathy**—Another user of cryptography; she does not usually have a large role nor malicious intentions.
- **Eve**—A malicious user who does not interfere with communications. She simply wants to eavesdrop on the conversation between two other characters, typically Alice and Bob, but does not actively try to attack the communication.
- **Mallory**—The malicious user. She's always trying to thwart attempts by other characters to communicate securely.
- **Trent**—He is a trusted third party. He communicates only with Alice, Bob, or Cathy when they ask for his help. He can always be trusted to do what he says he will do.

These characters are used throughout the rest of this chapter. Familiarize yourself with them because they will often be used to describe a cryptographic protocol without further definition. It is assumed you know that Trent is a trusted third party, for example.

## Symmetric Encryption

Symmetric encryption, or single-key encryption, is the most basic and well-understood cryptography primitive. It is where the whole field really started. Caesar and his cipher, the Germans and Enigma, and the Japanese and Purple are all examples of symmetric encryption. The idea behind symmetric encryption is that only a single key is used to encrypt and decrypt a message.

Symmetric encryption is used when Alice wants to provide confidentiality of a message sent to Bob. Alice wants the message, or data, to remain secret to everyone except herself and the recipient, Bob. This is the main property that symmetric encryption provides. Depending upon the mode of encryption used (modes are explained later in this chapter), symmetric encryption can also provide integrity when used correctly.

The best analogy for symmetric encryption is that of a safe. To unlock a safe you must have the right key. In the physical world this key is usually a metal object. In the world of cryptography, this key is a set of random bits. If you have the key, you can open the safe and put something inside of it. In the world of cryptography, the only thing you can put into the safe is data, and you do so by encrypting it. Now whatever is inside the safe is confidential and protected from anyone without the key. Without the key, Mallory is unable to read, modify, or do anything to the data except destroy it.

To unlock the safe you must have the proper key. The same is true with symmetric cryptography; Alice or Bob must have the correct key to decrypt the data. Much like a real safe, the key that was used to encrypt the data is the same key used decrypt. If you do not have the proper key, you cannot decrypt the message, or data. Just like a real safe, however, attempts by Mallory can be made to decrypt the message without the proper key. In our safe example, this can be done by going through all possible physical configurations for a key until the proper configuration is tried and the safe is opened. In cryptography the same is true. Mallory can try all possible key combinations until one works, and the resulting data or message is understandable. You might be asking yourself, how many combinations would she have to try? The answer to that question depends upon the encryption algorithm or cipher used.

### Note

The key used to encrypt and decrypt is sometimes not exactly the same, but you can always derive the decryption key from the encryption key without much work. Reversing the encryption key is a normal method for obtaining the decryption key.

This also brings up a term that might be unfamiliar but is often used to talk about an algorithm's security: *computationally secure*. Computationally secure means that the amount of time needed to compute all possible combinations is so large that it cannot be done in any reasonable amount of time. The definition, "in a reasonable amount of time," is deliberately vague because the definition of computationally secure is ever changing as the speed of a computer is ever increasing. For example, one popular symmetric encryption algorithm, Data Encryption Standard (DES), has a key of 56 bits. This means that for someone to break the algorithm it would require 256 = 72, 057, 594, 037, 927, 936 different keys to be tested to exhaust all possible keys. Assuming your computer could try a million keys a second, it would take 2284 years to try all of the keys. That sounds like it is a secure algorithm because we will all be dead by the time the key is discovered. However, a specially built machine was used to crack DES in a little over 36 hours. With unlimited funds and current technology, DES might be able to be broken in only a few hours. It is this change in computer speed that makes the definition of computationally secure ever changing. What is computationally secure now, at the time of this writing? This is a heavily debated question, but something that requires around 280 attempts (keys) is considered beyond the computational ability of any computer in existence today. However, remember that what is out of reach today might become very easy to compute tomorrow.

In the area of symmetric key cryptography, there are two main types of algorithms that use only a single key: stream ciphers and block ciphers. They differ only in the way that the data is processed.

### Stream ciphers

A stream cipher uses a single key to encrypt a message or stream of data. The message is considered to be a stream of data in that each byte is processed with the bytes preceding it, and that order is important. If you were to change the order of any of the bytes in the plain text, the cipher text, from that point forward, would look different. [Figure 20-4](ch20.html#a_stream_cipher) shows what a stream cipher does.

![A stream cipher](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2004.png)

**Figure 20.4. A stream cipher**

Stream ciphers normally do not require any padding of the message. Because messages are treated as a stream of data, they can be of any length and do not need to be padded in any way except to add randomness to common messages.

You have already seen one type of stream cipher, the one-time pad. Other stream ciphers include the following:

- RC4
- SEAL
- ISAAC
- PANAMA
- Helix

There are a lot of stream ciphers and most of them work by generating seemingly random data using the key as the seed for the generator. Then this stream of data is XORed with the message as with a one-time pad, and the cipher text is created.

When Alice wants to send a message to Bob using a stream cipher, they must both have the same key. This is true for any symmetric key encryption; however, the other caveat for using stream ciphers is that they must feed the plain text and cipher text into the algorithm in the same order as it was produced. Order is very important when using stream ciphers. Mallory can prevent Bob from decrypting most steam cipher-encrypted messages by changing the first few bits that Alice sends to Bob. This property of a stream cipher is not a bad thing, however; it provides integrity. If any of the cipher text bits are changed, it will be obvious to Bob when he decrypts the message. However, there are plenty of stream ciphers where errors do not propagate through the entire message. What this means is that if an error occurs while the message is being sent from Alice to Bob, it will only prevent that section of the message from being decrypted properly. This property is an important one to consider if the channel used to communicate is not reliable.

### Block ciphers

A block cipher is the other kind of symmetric encryption algorithm. Block ciphers also use a single key to encrypt a message, but it is done a block at a time. A block is considered a certain number of bits and is determined by the algorithm. Each block is processed independently of each other and there is no correlation between the encrypting of one message block and another. It is the ability of a block cipher to process a single message block at a time that makes it different from a stream cipher. [Figure 20-5](ch20.html#a_block_cipher) shows what a block cipher does.

![A block cipher](/api/v2/epubs/urn:orm:book:9780470502495/files/figs/2005.png)

**Figure 20.5. A block cipher**

While block ciphers have the ability to process a single block of the message independently, usually encryption modes are used to break this property to prevent someone from gaining information about the message by seeing repeated blocks. For example, if Alice sends the message "yes" to Bob in response to a question, the word "yes" will be encrypted to the same cipher text assuming the same key is used. Then every time the word "yes" was sent, Eve would know what message was being sent without needing to decrypt it. Worse yet, Mallory could pre-compute the message "yes" with all possible keys and then simply match the cipher text seen to the cipher text of a pre-computed message. This would allow Mallory to know the corresponding key and break all further encryptions, assuming the key size is small enough.

Another attack that Mallory can use is to change the order of blocks. This will not prevent decryption from occurring, as would happen with a stream cipher, because each block does not depend on any other block. For example, suppose Alice asks Bob what house number his house is and his response is "1234," encrypting "12" in one block and "34" in another. Without knowing what house number was actually sent, Mallory can still change the ordering of the blocks and send Alice to "3412," the wrong house. So while an error in one block of cipher text does not propagate to further blocks, Mallory can still change the ordering of the blocks without Bob or Alice knowing. This still implies that there is confidentiality; however, integrity is now lost using a block cipher this way.

To keep from having the same plain-text block always encrypting to the same cipher text block, modes of encryption were created. The first mode of encryption is the one already explained, simply encrypting block by block through the plain text. This mode of encryption is called electronic code book. Three other common modes are used: cipher block chaining, cipher feedback, and output feedback. While these three modes avoid encrypting the same plain text to the same cipher text, they come with the disadvantage that any error will propagate throughout the encrypting process much like a stream cipher. The level of error propagation is different for each mode. Differences by mode are outlined as follows:

- **Electronic code book (ECB)**—The message is encrypted one block at a time so that one plain text block maps to one cipher text block. An error in any block affects the decryption of only that block. If an entire block is lost during transmission, none of the other blocks are affected.
- **Cipher block chaining (CBC)**—The output block of the previous encryption is XORed with the next block of plain text before being encrypted. If an error occurs in one block, that error is propagated into the next two blocks that are deciphered. If an entire block is lost during transmission only the next block is affected during decryption.
- **Cipher feedback (CFB)**—The previous cipher text block is encrypted and the result is XORed with the plain text block. This differs from CBC mode in that the XOR occurs after the encryption of the previous cipher text block. If an error occurs in one block, that error is propagated into |*n*/*r*| blocks where *n* equals the output size of the block cipher and *r* equals the number of bits used in the XOR. If an entire block is lost during transmission, CFB mode will recover just like CBC; however, it requires |*n*/*r*| blocks before the error is removed.
- **Output feedback (OFB)**—The output of the encryption algorithm is continually fed into the algorithm while the plain text is XORed with this output. This differs from CFB because what is fed into the encryption algorithm does not include the cipher text. If an error occurs in one block, that error is only propagated to those bits that are changed. However, if any of the bits are lost, including a whole block, the error is propagated to all of the remaining blocks and cannot recover.

Of all the modes shown in the preceding list, ECB is almost never used because of the reasons stated. The most popular mode is CBC because errors do not propagate (as they do in OFB) throughout the entire message if bits are lost. CBC is used over CFB because the error propagation is usually smaller, only two blocks, and because the bit changes that do occur happen in a predictable manor to the later blocks. For example, when using CBC, if block 1 has bits flipped in it during transmission, block 1 will be seemingly random, and block 2 will have the exact bits flipped where they were in block 1 during transmission. This enables Mallory to cause predictable changes to the message. In CFB mode, bits flipped in block 1 are the exact bits that are flipped in block 1 of the decipherment. The later blocks then appear random. If an attacker is going to flip bits while the cipher text is being transmitted, it is always better to receive a random-looking block on decryption alerting you that this has occurred and to not trust anything that comes after it. This is not true for CFB, because you cannot necessarily tell where the error begins, only that one has occurred.

DES (mentioned already) is only one of many block ciphers. DES was the original block cipher backed by a National Institute of Standards and Technology (NIST) publication. However, because of the small key size, 56 bits, it was thought to last only for five years because computers today can quickly perform a brute-force attack against 56 bits. About 15 to 20 years later, talk of a new algorithm was brought up at NIST. They took submissions for the new algorithm to be called *Advanced Encryption Standard* (AES). The hundreds of submissions were whittled down to a final five, and then finally an algorithm called Rijndael was selected to become AES. AES has three key sizes: 128, 192, or 256 bits. Other block ciphers include the following:

- Desx
- Blowfish
- Cast
- Skipjack
- Twofish

There are many, many more.

### Sharing keys

With strong block ciphers created, the ability to use them is still hindered by the fact that the key must be known by both parties before the algorithm can be used. Often, the other party you are going to communicate with is known, so keys can be created and shared in a secure manner before communication begins. This type of key generation is called using a *pre-shared secret*. The key is shared between parties before communication begins. However, what if Alice wants to communicate with Bob and she has never met Bob before, so they do not have a pre-shared secret key? How then can Alice and Bob communicate securely? They could create keys and encrypt them so no one knows the keys, but how are they going to encrypt them without common keys? Again, we are back at the chicken-and-egg question.

One way to solve this problem is to have a trusted third party, Trent. Alice will create a key to be used to communicate with Bob. She will encrypt this key using a pre-shared key that she has with Trent and then send the key to Trent. Trent will then be able to decrypt the key he received from Alice using her key and then encrypt with the key he has pre-shared with Bob and send it to him. Now both Alice and Bob have a common shared key, and only Trent, Alice, and Bob know what the key is. However, this scheme has problems, starting with Trent. What if Trent is really not Trent at all but Mallory? Now she has the key and can decrypt any communication between the two parties. Also, this scheme requires that everyone have a pre-shared key with Trent. Implementing a system like this would be a huge logistical problem.

Another way to share a key between two parties is for the parties to create the key on-the-fly, in a secure manner. This idea is called *key agreement*. One classic key agreement protocol is the Diffie-Hellman key agreement protocol. This protocol has each user send the other a message. Once both parties have the other's message, a secret key has been established between the two, and any third party, Eve, cannot obtain the key even if she knows both messages. This protocol relies on a number theory called the *discrete logarithm problem*. Explaining this hard problem in detail, however, is beyond the scope of this text. The protocol is briefly outlined for you here:

1. A prime, *p*, and an integer, *a*, such that (2 ≤ *a* ≤ *p* − 2), are created and openly published.
2. Alice → Bob: *a*x mod *p* where *x* such that (1 ≤ *x* ≤ *p* − 2) and is kept secret by Alice.
3. Bob → Alice: *a*y mod *p* where *y* such that (1 ≤ *y* ≤ *p* − 2) and is kept secret by Bob.
4. Bob receives *a*x mod *p* and computes the secret key: *k* = (*a*x)y mod *p*.
5. Alice receives *a*y mod *p* and computes the secret key: *k* = (*a*y)x mod *p*.

It is easy to see that both of the keys will be the same. It is not so easy to see why a person cannot figure out *x* and *y* from the two messages. Essentially, you need to take the logarithm of the messages to obtain *x* and *y*; this is very hard to do with mod *p*. If the integers used are large enough, 512 bits or larger, it is computationally infeasible to compute this discrete logarithm and therefore computationally infeasible to break this key exchange.

However, a man-in-the-middle attack can be launched against this type of key agreement protocol. In this attack Mallory intercepts the message sent from Alice to Bob and those sent from Bob to Alice. In both cases she pretends to be Bob when Alice sends a message to Bob, and pretends to be Alice when Bob sends a message to Alice. With Mallory in the middle of this key exchange, she can create her own two secret keys and exchange communications with Alice and Bob forwarding the messages so Alice and Bob are none the wiser. When Alice sends a message to Bob using what she thinks is the key Bob has, she really uses the one Mallory set up with her. The message is sent; Mallory intercepts it, decrypts it, reads or changes it, and then re-encrypts it with the key set up between Mallory and Bob. Bob receives a message he believes to be from Alice when it is really from Mallory. Now Mallory has full control over the communication channel and both confidentiality and integrity are lost because authentication was never established.

This key agreement protocol is still in use today; however, things have been changed to make it more secure and so that the man-in-the-middle attack cannot be used.

ElGamal is another common key exchange protocol that also relies on hard number theoretical math problems for its security. However, the property of authentication has never been addressed properly in the use of symmetric key encryption. There is still a level of doubt that you are communicating with whom you say you are. To help alleviate this problem and provide authentication, asymmetric encryption was created.

## Asymmetric encryption (two-key encryption)

Let's get back to the safe example: in asymmetric encryption two keys are needed instead of just one. One of the keys is used to open the safe for putting things into it, and the other is used to take things out of the safe (the analogy falls apart a bit here, but stick with me). Now with one key, key A, you can place data into the safe or encrypt it. After key A has been used to encrypt the data, only key B can open the safe to remove the data, or decrypt it. It is important to note that asymmetric encryption has the property that figuring out one key from the other should be as hard as decrypting the message without any key. Stated another way, the computational power required to decrypt an asymmetrically encrypted message is approximately the same as deducing one asymmetric key from the other. When these algorithms are applied to the sharing of keys for symmetric encryption, it becomes very clear how useful they are and why these properties are important.

Alice creates the two keys required for asymmetric encryption and publishes one of them to the world. Now everyone in the world, including Bob, has access to this key (Alice's public key). This means Bob, or anyone else in the world, can encrypt data and send it to Alice for only Alice to read. Remember, the only person that can decrypt the cipher text is Alice, or the person with key B (Alice's private key, in this case). Now the problem of sharing a symmetric key is easy.

1. Bob creates a symmetric key.
2. He uses Alice's public key to encrypt the symmetric key so no one else can read it.
3. He sends the encrypted symmetric key to Alice.
4. Alice receives the encrypted symmetric key, decrypts it with her private key, and begins communicating with Bob using the symmetric key he created.

But why would I use the symmetric key encryption algorithms at all? If asymmetric algorithms are secure and I already have everyone's public key, why bother with creating a symmetric key and using symmetric algorithms? The answer to that question is simple — for speed. Using RSA, a standard asymmetric encryption algorithm on an average computer, you can encrypt 35,633 1024-bit messages in 10 seconds. Whereas using AES, the standard for symmetric encryption in CBC mode, you can encrypt 69,893 1024-bit messages in only 3 seconds. That is over 6.5 times faster using symmetric encryption instead of asymmetric encryption. Assuming both algorithms are secure, why would you use one that is 6.5 times slower than the other? Why is asymmetric encryption so slow? Asymmetric encryption uses properties of number theory to derive its strength. The addition and multiplication of these very large (1024-bit) numbers takes a very long time on computers compared to the binary operations performed in symmetric key encryption. Unfortunately, all of the asymmetric encryption algorithms today rely on number theory principles and require the use of very large numbers.

Even though asymmetric encryption is very slow, it does a very good job of solving the problem of sharing keys. Most symmetric algorithms have a key size somewhere around 128 to 256 bits. These keys can be encrypted in a single asymmetric message block, for most algorithms. This means only one message (the encrypted symmetric key) needs to be sent from Alice to Bob using an asymmetric algorithm before they can communicate using a symmetric algorithm. However, while asymmetric encryption does a good job of solving the key distribution problem, it has a few problems of its own besides slower speed.

### Using a certificate authority

The first problem with asymmetric cryptography is in publishing one of the two keys. How does Bob know that what he thinks is Alice's public key is really hers? Why couldn't this be our old friend Mallory launching another man-in-the-middle attack by changing the publication of Alice's public key to her own public key? The answer to this is that Bob does not know that it really is Alice's public key that is published. To solve this problem, we can enlist the help of our friend Trent. Trent can start a company to keep people's public keys. His company is called a *certificate authority* (CA). The idea behind a CA is that Trent's public keys are so well known, and distributed, that everyone believes them to be correct. This is where cryptography and money meet. It is money and company integrity that keep Trent from turning into a Mallory. If everyone believes that Trent is doing his job properly, he builds trust. However, if Trent were to cheat the system even once and get caught, all credit for him and his company is lost and people will go elsewhere.

So how do you register your public key with Trent, and why does everyone believe they really know his public key? CAs contact software developers and negotiate to have them hard-code the CA's public key into every piece of software they develop. With this public key in a lot of different software and published on the authority's site, anyone can check to make sure that they have the correct key. Now anyone who wants to use this system has to believe that this public key is correct. With this trusted third party, Trent, anyone who wants can create a public key and register it with the CA. To do this, you must create a certificate that includes, among other things, an expiration date, your name, and your public key.

### Note

The X509 standard documents exactly what is in a certificate and how to create one.

When Alice needs Bob's public key she goes to the CA Bob has registered with and asks for Bob's public key. This public key is then encrypted with Trent's private key and sent to Alice. Alice can decrypt this message from Trent because she knows Trent's public key. (Public and private keys are not connected to encrypting and decrypting in any way. They are just labeled public if it has been published and private if it has not). Now, for the first time, you have authentication. Alice knows for certain that Trent has sent her Bob's public key because only Trent could create a message that will decrypt with his public key. This is what is called a *digital signature*, and it provides the missing goal of authentication.

### Using a web of trust

While CAs work very well, they are expensive for the average user and are not the only method for sharing public keys. Another method for sharing public keys uses what is called a *web of trust*. A web of trust is when two people who trust each other, such as Alice and Bob, get together and share their public keys with each other. They have no reason to lie about their public keys, and in a face-to-face environment they can check for proper identification, if necessary, to confirm any information.

Now that these two people trust each other, they can go and find friends. Let's say that Alice finds Cathy, and Cathy wants to get into this web of trust so that she can send messages to Bob. Alice can verify Cathy's public key, sign it, and send it on to Bob. Now Bob is able to trust Cathy's public key because he trusts Alice. This web can extend to include any number of people at any level of security. If Cathy finds another friend and wants to give that key to Bob, he can work through the web of trust and end at Alice whom he implicitly trusts. The depth of trust can be set by the user's paranoia level, but in theory, if everyone is checking everyone's identification and key, it should be a secure system. A very popular piece of software called Pretty Good Privacy (PGP) implements this web of trust. There are also key servers that are set up so that after a key has been signed by someone it can be placed on the server so that Bob does not need to receive the message from Cathy directly; he can download Alice's signed version of Cathy's public key from the key server.

Before moving on to digital signatures, the following steps outline the RSA encryption algorithm. While the list doesn't cover the number theory behind the algorithm, it is important to see how it works from a high-level point of view.

1. Generate two RSA primes, *p* and *q*, and compute *n* = *pq* and Φ = (*p* − 1)(*q* − 1)
2. Select a random integer *e* from the interval (1,Φ) such that .gcd(e, Φ) = 1.
3. Select an integer *d* from the interval (1,Φ) such that ed = 1modΦ.
4. The public key is (n,e) and the private key is (n,d).

The following steps outline RSA encryption:

1. Let *m* be the message represented as a number in the interval [0, *n* − 1].
2. Compute c = me mod *n* where *c* is the cipher text.

You can decrypt RSA with the following: Compute m = ca mod *n* where *m* is the original message.

## Digital signatures

The process of encrypting a message with a private key so that anyone can read it, but knowing that it only came from the holder of the private key, is called *digitally signing*. The name refers to the fact that only the person who holds the private key can create cipher text that can be decrypted using the public key. The same idea is true with a real signature and a credit card, for example. In theory, only someone who can produce your signature is allowed to buy things with your credit card. With digital signatures it is true that if only your public key can decrypt a message, assuming you have not given away your private key to anyone, only you had the ability to create the cipher text in the first place. In reality, using digital signatures to purchase things with your credit card can be more secure than a real signature and your credit card. Digital signatures are founded on provable principles of mathematics, whereas, a real signature is only secure if no one can forge it.

Using asymmetric encryption is really, really slow. Does this mean digital signatures are really slow as well? The answer depends upon implementation. Imagine that Alice has an e-mail that she would like to send to Bob. Alice wants to be able to prove that the message came from her and not Mallory. Alice could create a symmetric key, encrypt the entire message with that key, and then send the symmetric key encrypted with her private key to Bob along with the message encrypted with the symmetric key. This process would work because only that symmetric key would decrypt the message, and Bob would know it must have come from Alice because only she could have created it using her private key. However, what if Alice does not care who reads the message, and only wants to provide authentication for those who might not trust it is truly coming from Alice? To alleviate this problem, the message is represented as a smaller message and that is signed by Alice and sent along with the unencrypted original message. This smaller message is so small that it takes only a tiny amount of time to sign. Now anyone can read Alice's message and can also verify that it truly came from her and no one else. You go about making this smaller message that represents the larger one with a *hash function*.

## Hash functions

Hash functions, also called *one-way* or *collision-resistant one-way functions*, are the fourth cryptographic primitive. A hash function takes a message of any size and computes a smaller, fixed-size message called a digest or hash (we will use digest to not confuse hash functions with what they produce). The computation required to compute a digest is very, very small. For example, remember that with AES in a CBC chain 69,893 1024-bit messages could be encrypted in 3 seconds. In that same 3 seconds, SHA-1, the standard for hashing, can hash 224,800 1024-bit messages. SHA-1 can compute digests 3.2 times faster than AES can encrypt those messages. Simply reading a file off of the hard disk requires approximately as much time as computing the hash while doing it. The way in which these hash functions compute a digest from an arbitrarily large message is beyond the scope of this book; however, there are three properties of all hash functions that make them very valuable.

- It is computationally infeasible to find two messages that can hash to the same digest.
- Given a digest, it is computationally infeasible to find a second message that will create the same digest.
- Given a digest, it is computationally infeasible to find the original message that created this digest.

These properties not only make hash functions very useful in the application of digital signatures, but also in storing passwords. Because the original message cannot be discovered from a digest, when storing a password only, the digest needs to be stored. This way, anyone can read the file containing the passwords, but no one can use this information to figure out someone's passwords.

While this is a very valuable cryptographic tool to have, there are some caveats to using hash functions, especially for password storage. First, a message always hashes to the same digest no matter how many times you compute it. The only way to change what digest is created is to change the message. This property allows the proof of message integrity. If Mallory changes a message while it's in transit, the message's digest will be changed as well. To protect message integrity, Alice must only compute her message's digest, and send that encrypted with Bob's public key to Bob along with the message. When Bob receives the message, he can compute the digest the same way Alice did, and verify that the message has not been altered in any way.

Let's return to password storage with a hash function. Users do not like passwords and have trouble remembering good ones, such as xSok32$lK329@)O. So instead, they create passwords such as *fluffy*, their cat's name. Mallory, who is looking to attack this type of password scheme, can compute the digest of all the words in a dictionary and compare those digests to the one stored in the password file. If one of the digests from the dictionary matches one in the password file, Mallory has discovered the password. However, one simple way of preventing this is to randomly *salt* the password before it is hashed. Salting is the addition of random data to a message before it is hashed so that the aforementioned dictionary attack cannot be carried out. The random data that is added is not too random, however, or no one would be able to verify the password. Instead the random data is chosen from one of only a few thousand possibilities. This randomly selected piece of data is concatenated to the password and then hashed. To verify the user's password, all combinations of the password and the random piece of data must be computed. If one of them matches, you can verify the password is correct. If none of them match, this password is not correct. This might seem like a lot of work, but because hashing algorithms is a fast computation, computing a few extra thousand digests for a single password is not a big deal. However, computing a few extra thousand digests for all the words in the dictionary quickly becomes infeasible. As computers grow faster, the number of different saltings used increases.

Bringing the discussion of cryptographic primitives full circle, hashing algorithms can be a great source of pseudorandom data. A method for creating pseudorandom data is outlined here:

1. Seed a hash function with a short random message. The resulting digest will be pseudorandom and the first number generated.
2. Using this number and a combination of the original seed, create a new message. (The original seed and the digest must be used together because the digest alone is too small to compute a digest from. Remember the message is larger than the digest.)
3. This new digest is another pseudorandom number. This process is continued for as long as needed.

Like any pseudorandom function, the hashing algorithm will eventually cycle. However, the number of hashes needed to cause the algorithm to cycle is considered computationally infeasible. This same basic method can be used to create a stream cipher. Simply use the key as your seed message. Then use the output of the hash function XORed with the plain text to create the cipher text. This is exactly like a one-time pad, but using a hash function as the random number generator.

### Keyed hash functions

While most hash functions do not require any sort of key to create their digest, there are hash functions designed to require a key. The idea behind these functions is that they hold all of the same principles as that of a regular hash function except they also have the additional property that the digest cannot be created without the proper key. Creating a message key combination that hashes to the same digest should be computationally equivalent to enumerating through all the keys. Any regular hash function can be turned into a keyed hash function and vice versa, so the distinction for our purposes is negligent. However, it is important to know that such functions exist.

# Putting These Primitives Together to Achieve CIA

Through the use of these four primitives, confidentiality, integrity, and authentication can be achieved. Consider the four scenarios where Alice is sending a message to Bob. She requires confidentiality in the first scenario, message integrity in the second, message authentication in the third, and all three in the fourth. For all four scenarios, assume that Alice and Bob have traded public keys and that they trust these public keys. This is a fair assumption to make because this is feasible through a web of trust or a certificate authority. It is important to note that while these scenarios demonstrate the ability to ensure these properties, they are not the only way to ensure them.

- **Confidentiality**—Alice wants to send a message to Bob without anyone else being able to read it.Alice creates a symmetric key and encrypts it using Bob's public key.Alice sends the encrypted symmetric key to Bob.Alice encrypts her message using the symmetric key and a symmetric key algorithm, and sends the message to Bob.Bob, and only Bob, is able to read the message because he has the symmetric key that was sent encrypted with his public key. Confidentiality is ensured.
- **Integrity**—Alice wants to send a message to Bob and ensure the message was not changed during transmission.Alice hashes her message and encrypts the resulting digest with Bob's public key.Alice sends the message and the encrypted digest to Bob.Bob is able to verify that the message has not been altered because he, too, can compute the message's digest and verify it with the one sent with the message.Mallory cannot change the message because the computed digest would not match the sent one. Mallory cannot change the sent digest because it is encrypted with Bob's public key. Integrity is ensured.
- **Authentication**—Alice wants to send a message to Bob and prove to Bob that she was the sender.Alice hashes her message and digitally signs the digest using her private key.She sends the message and the signed digest to Bob.Bob can verify the signature because he has Alice's public key. He can also verify that the digest belongs to that message because he can compute the digest.The only person that could create such a signed digest is Alice because only Alice has her private key. Authentication is ensured.
- **CIA**—Alice wants to send a message to Bob and in the process make sure that no one else can read the message, the message does not change, and prove to Bob that she was the sender of this message.Alice creates a symmetric key and encrypts the key with Bob's public key.Alice sends the encrypted symmetric key to Bob.Alice computes a digest of the message and digitally signs it.Alice encrypts her message and the message's signed digest using the symmetric key and sends the entire thing to Bob.Bob is able to receive the symmetric key from Alice because only he has the private key to decrypt the encryption.Bob, and only Bob, can decrypt the symmetrically encrypted message and signed digest because he has the symmetric key (confidentiality).He is able to verify that the message has not been altered because he can compute the digest (integrity).Bob is also able to prove to himself that Alice was the sender because only she can sign the digest so that it is verified with her public key (authentication).

While the last protocol seems a bit extreme, it ensures confidentiality, integrity, and authentication. This is part of the reason why speed is so important in cryptography. Sometimes, even to send the shortest message, multiple encryptions, hashing, signing, verifying, and decryption must be performed. For this reason, the fastest algorithm should be used when appropriate. Multiple protocols will ensure any combination of the three CIA properties. Each protocol has its advantages and disadvantages. The protocol used to complete a task is sometimes more important than the primitive used. Always make sure standards are followed when implementing any primitive or protocol.

# The Difference Between Algorithm and Implementation

Most of the time, when you hear about a cryptography system being broken, it is an implementation of the system rather than the actual algorithm itself. The distinction between an algorithm and an implementation of that algorithm is an important one. For example, there is a Windows SSH client that had a vulnerability with one of the functions that was used in the RSA encryption. No check was made to ensure the base of the exponentiation was not as large as the modulus used. What that means exactly is not important. However, you should note that it was a particular implementation of the RSA algorithm that had a problem. This does not mean that RSA itself is in any way flawed. An algorithm can be 100 percent provably secure, like a one-time pad, for example. The algorithm used to generate the random numbers could be 100 percent secure, as well. However, if the implementation of that random number generator happens to publish the initial seed used, the entire system can be easily attacked. Again, this does not mean that the algorithm is flawed, but it does mean that this particular implementation of the algorithm is not secure.

How does an implementation of an algorithm become insecure? The answer usually rests with the person or persons who implemented the algorithm not understanding what it really does. For example, if you were charged with creating an RSA implementation, would you know what numbers must be kept secret and which ones can be published? Also would you know enough about the operating system you are implementing the RSA algorithm for to know that if numbers are stored in certain parts of memory they can be read by other processes running on the same computer? When it comes to implementing an algorithm, it really requires someone with extensive knowledge of the operating system on which the algorithm is being implemented. It also requires an in-depth knowledge of the algorithm being implemented. Another good RSA example is a theorem called the *Chinese Remainder Theorem* that can be used to speed up the exponentiation required for each encryption and decryption. However, this theorem requires that you keep the *p* and *q* in the RSA algorithm. Do these values need to be kept secure, or can they just be stored in raw form in a file? This is the kind of knowledge required to properly implement an algorithm. If you do not have this level of knowledge about cryptography, using someone else's already tested implementation is usually the best idea.

A perfect example of a poor implementation of an algorithm is an FTP server that was recently published with an embarrassing vulnerability. This FTP server and client worked together to provide a secure means for transferring files to and from the server. This product was billed as a secure and seamless method for transferring files. To ensure that no one could capture the files and read them while being transferred from computer to computer, the traffic was encrypted. The encryption algorithm they used was DES, the standard for encryption at the time. Using DES, a published standard, instead of trying to invent an encryption algorithm was a sound idea. The implementation of the algorithm was perfect, as well; they just followed the standard. However, they ran into the same chicken-and-egg problem discussed with symmetric encryption; how do you distribute the keys? They knew that just using the same key was a bad idea, so they had the client create a new key for each session; but they still did not have a way to let the server know what the key was. So, instead of using asymmetric encryption methods, the key was simply sent as the first 56 bits of the data from the client to the server. After those 56 bits, all of the data sent from server to client or vice-versa was encrypted using DES. With a quick look at the DES standard, and some analysis of the bits sent across the network, a savvy hacker would quickly realize that DES uses a 56-bit key for encryption. From there, defeating the encryption was easy; anyone who was looking at the traffic already had the key. I'm willing to bet the software designers, however, thought that no one would be able to figure out the first 56 bits of data sent was the key used for the encryption. This leads right into the next subject, the use of open source algorithms and implementations versus proprietary ones. While this FTP server/client encryption mistake might seem like the exception, the use of proprietary algorithms and implementations with errors occurs more than most people think.

## Difference between cryptographic primitives and protocols

The line between primitives and protocols is often blurred in cryptography. In fact, an example of this has already been demonstrated in the discussion of asymmetric encryption. The use of an asymmetric encryption algorithm to share a symmetric key is not a cryptographic primitive, but rather a protocol that uses both asymmetric and symmetric encryption to complete the task. Why is the distinction between these two important when discussing cryptography? The reason is that when discussing protocols assumptions are usually made about the underlying primitives. Sometimes these assumptions are strong, like assuming that the asymmetric algorithm used in the above protocol is secure. However, sometimes more complex protocols assume properties about primitives that are not true. One example of this error is using a symmetric algorithm to encrypt a message twice and still assuming the message is secure. Often this is a fair assumption, but in many situations it is not. So a complete understanding of the underlying primitives is essential before using them in a protocol. More often than not, it is an unclear understanding of underlying primitive properties that leads to a flaw in a protocol.

Protocols are often flawed for reasons not relating to the underlying primitives, such as in the classic man-in-the-middle attack used to circumvent the Diffie-Hellman key exchange protocol. This attack works by having someone intercept the communication between the two parties attempting to establish a secret key for communication. Because the protocol does not use any of the underlying primitives discussed, it is a flaw that is a direct result of the protocol.

The attack works by having someone in the middle, Mallory, pretend to be the other side of the communication for each side. So when Alice sends the first part of the protocol to the person she thinks is Bob, it is really Mallory who intercepts the message. Mallory then continues with the protocol as if she is Bob communicating with Alice. Mallory also initiates the protocol with Bob as if she (Mallory) is Alice. Both Alice and Bob believe they are talking to each other; however, they are really communicating with Mallory. This allows Mallory to obtain all the important information and break the protocol. Mallory then uses the key she has established with Alice to communicate with Alice, and the key she has established with Bob to communicate with Bob. Mallory simply forwards all messages from Alice to Bob by first decrypting the message with Alice's key and then encrypting it with Bob's key, and neither is the wiser. This is one of the classic methods used to circumvent protocols.

This type of an attack can usually be secured by authenticating each of the parties. If Alice can authenticate her identity when sending a message to Bob, then Bob will not be tricked when Mallory attempts to change this authentication. While the proposed solution seems very easy and obvious on the surface, authentication can sometimes become quite complex. It can also lead to a chicken-and-egg type of a problem. Authentication usually requires the establishment of an asymmetric encryption scheme already in place. However, if this scheme is already in place, and secure, it would be used instead of the Diffie-Hellman key exchange protocol to actually exchange the symmetric key.

In working with cryptography you often find new and/or more secure protocols for completing a task. The cryptographic primitives discussed in the preceding paragraph have been well studied and are well understood. This is not true for protocols. After all, protocols need well-established primitives before they can be used or tested. Most of the work done in cryptography today is in the development of cryptographic protocols that are secure. The work of advancing primitives is usually very small and theoretical. Attacks on algorithms such as DES and SHA-1 are usually either theoretical attacks or simply advances in computing hardware to allow for a brute force search of a key space. With that said, some of the most interesting attacks on primitives have been in the area of hash functions, the least understood of the four primitives.

# Proprietary Versus Open Source Algorithms

For most cryptography algorithms it is impossible to prove that they are secure. Some algorithms are founded in mathematics, such as the number of theoretical ones shown earlier, and these foundations can help to ensure a level of security. However, even hard problems in mathematics are broken every once in a while. The only true test of an algorithm is time. The best algorithms are those that have been published for the entire world to see and have stood the test of time. If an algorithm has been published for a while, such as DES, AES, RSA, SHA-1, and so on, and still no one has been able to break the algorithm in any practical manner, the algorithm is assumed secure.

That said, there are still too many instances of companies creating proprietary encryption algorithms for use in their software. Most companies take the view that these algorithms are like any other type of intellectual property; keeping it secret is the only way to do business. This attitude is completely wrong. Keeping an encryption algorithm secret can only do harm to the business if someday down the road someone is able to break the algorithm. Whereas, if the algorithm is published and allowed to be analyzed for a few years, that algorithm gains a reputation as being secure and becomes accepted in the community.

DVDs provide a perfect example of the problems in implementing proprietary encryption. At the time when DVDs were created, they were to be the next generation in delivering movies to home theaters. DVDs have better quality sound and picture. However, Hollywood also wanted to be able to protect its movies from people copying them, just as it did with VHS tapes. To aid in protecting them filmakers enlisted the help of a company to create an encryption algorithm for encrypting DVDs. The idea was simple; the company would encrypt the movies on the DVD and then have the players simply decrypt the movies as they were being played. The key used to encrypt the movie is stored in an encrypted form on the DVD. The player would simply use its key to decrypt the movie's key, and then start decrypting the DVD.

The problem with this whole scheme was that the algorithm used to encrypt the movie was flawed. The algorithm was created privately and was never published. Only the people who worked on the algorithm were able to test it. After DVDs had been out for a short time, people started looking at the method of encryption and trying to break it — a task soon accomplished. This cost Hollywood and the DVD player manufacturers millions of dollars. What was to be a secure system to prevent people from copying movies was completely broken. DVDs could be played on open source computers without keys, and the movies could be copied. The entire system was rendered useless because the planners thought creating a new encryption algorithm was the best approach to security. This is never the case. In cryptography, maybe more so than in other areas of security, security through obscurity does not work.

# Attacks on Hash Functions

Cryptographic hash functions are an integral part of many of the protocols used in cryptography. Simply put, a hash function creates a representative of a piece of data without revealing what that data is. However, unlike an encryption algorithm, a hash function is one-way in nature. Given a digest it is computationally infeasible to recover the original message. Most of the protocols rely on this fact, and on the fact that it is computationally infeasible to create a second message that will produce the same digest. One must question what happens if these properties are not kept intact. If the hash function is flawed and two different messages can be created that result in the same digest, does this destroy the protocol? In most cases, the answer is "yes." So the next logical step is to determine how one goes about creating a collision using the most popular hash functions available. Much work has been done in this area because of the fame and notoriety that is gained by "breaking" a hash function or finding two different messages that hash to the same digest.

The two most popular families of hash functions to attack are the MD family, which stands for Message Digest, and the SHA family, which stands for Secure Hash Algorithm. The MD family of algorithms was created by Ronald Rivest, and consists of MD4 and MD5. (There is also an MD2 function but it was never used much, and was released under RFC 1319–The MD2 Message-Digest Algorithm by Kaliski in 1992.) The MD family of algorithms was the first in widespread use on the Internet for cryptographic protocols and authentication. These algorithms were also the first to be seriously attacked because of their widespread use, and they were determined not to be secure. However, MD5 is still used in some applications today where legacy compliance is needed, and where security can be compromised for legacy compliance.

The SHA family of algorithms, which include SHA-0, SHA-1, SHA-256, SHA-384, and SHA-512, are modified versions of MD4 created by the National Institute of Technology and Standards with the help of the National Security Agency. These algorithms were designed as a replacement for MD4 and MD5 for use in secure protocols. They are the standard for cryptographic hashing in the United States. Attacks have been identified for SHA-0 and it is now considered broken. Recent attacks on SHA-1 also leave its level of security in question.

These attacks have provided valuable insight into how to create a cryptographically secure hash function. While the presence of collisions in a function usually marks the end of the function's use in the cryptographic community, it does not mean that the algorithm is 100 percent broken. For example, one collision, as of the writing of this chapter, has been found for SHA-1. This certainly does not make it an insecure function to use. However, the discovery of this collision indicates that a more systematic method for producing collisions in a timely fashion will be developed. The next few sections explain how these attacks work on MD4, MD5, and SHA-0, and give some details of the recent attack on SHA-1.

## Attacks on MD4

The MD4 algorithm is a three-round iterative hash function. It contains three different Boolean functions used for each of the three rounds. Each round is 16 steps long, one step for each piece of the input words. The resulting hash is a 4-word bit string. The algorithm for computing an MD4 digest is shown here. There is also padding that is done to ensure each message is a multiple of 16 words. The padding method is also provided.

Input: 16 message words, each word 32 bits long.

Output: 4 words, of 32 bits per word, which forms the resulting digest.

Algorithm:

Let *X*1 ... *n* = the words of the message, *H*1 = *A* = 0x67452301, *H*2 = *B* = 0xEFCDAB89, *H*3 = *C* = 0x98BADCFE, *H*4 = *D* = 0x10325476.

First Round: Let *M* = [0, 1, 2, ... 15], and *S* = [3, 7, 11, 19, 3, 7, 11, 19, 3, 7, 11, 19, 3, 7, 11, 19]

For i = 0 ... 15, Let F(X,Y,Z) = (*X* ^ *Y*) ∨ (¬*X* ^ *Z*)

*TEMP* = (*A* + *F*(*B,C,D*) + *X*Mi) ⋘ *X*Si

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *TEMP*

Second Round: Let *M* = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15] and *S* = [3, 5, 9, 13, 3, 5, 9, 13, 3, 5, 9, 13, 3, 5, 9, 13]

For *i* = *0 ... 15*, Let *G*(*X,Y,Z*) = (*X* ^ *Y*) ∨ (*X* ^ *Z*) ∨ (*Y* ^ *Z*)

*TEMP* = (*A* + *G*(*B,C,D*) + *X*Mi + 0x5A827999) ⋘ *X*Si

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *TEMP*

Third Round: Let *M* = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] and *S* = [3, 9, 11, 15, 3, 9, 11, 15, 3, 9, 11, 15, 3, 9, 11, 15]

For *i* = *0 ... 15*, Let H(X, Y, Z) = *XxorYxorZ*

*TEMP* = (*A* + *H*(*B,C,D*) + *X*Mi + 0x6ED9EBA1) ⋘ *X*Si

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *TEMP*

Update chaining variables:

- *H*1 = *H*1 + A
- *H*2 = *H*2 + B
- *H*3 = *H*3 + C
- *H*4 = *H*4 + D

Continue from the previous method. until all words of the message have been used to compute the digest.

Resulting Hash: *H*1 || *H*2 || *H*3 || *H*4

Padding:

Append a single bit to the end of the message, and then append 0 bits to the end until the message length is 64 bits less than a multiple of 512 bits. Finally, append the 64-bit length of the message with the least significant word first.

This algorithm is probably the most important of all of the algorithms described in this chapter. The MD4 function laid the foundation for all of the hash functions that came after it. The idea of having a single compression function that changes with only the Boolean function used, and using a block of the message in each step of a round, is a trend that is found in MD5, and the SHA family of functions.

Attacks on all hash functions, including MD4, usually come in steps. Most commonly, the community will attack a single round of the algorithm to show that it is not collision resistant. Next, multiple rounds are shown to have collisions, sometimes with small modifications to the algorithm such as changing the initial values. Finally, someone is able to show that the entire algorithm, without modification, has collisions.

Following this trend of attacking hash functions in pieces, attacks on the last two rounds of MD4 were shown in 1992 by den Boer and Bosselaers. The attack used the observation "that the 8 message words X[1], X[5], X[9], X[13], X[2], X[6], X[10], and X[14] used in the elementary operations 5 till 12 are the same as those used in the elementary operations 21 till 28." The idea is that if the registers used in the algorithm (A,B,C,D) are the same after 12 operations, then they will also be the same after 20 operations for two messages. Also, if after 28 operations, the value of the registers are the same, then the resulting digest will also be the same resulting in two messages that are different, but hash to the same digest. If these statements hold true, then the message blocks only differ in the 8 words mentioned previously. To quote from the original paper: "Two alternatives for these message words (X[1], X[5], X[9], X[13], X[2], X[6], X[10], and X[14]) are precisely chosen in such a way that the 4-word buffer (A,B,C,D) has two alternatives after 8 and 24 elementary operations (this is halfway between the second and third round), but the same value for both messages after 12 and 28 elementary operations."

Another important attack on MD4 was launched by Hans Dobbertin in 1997. The attack came in the form of two papers, one titled "The First Two Rounds of MD4 Are Not One-Way" in which he found pre-images given a hash, and the other, "Cryptanalysis of MD4" in which he showed how to find collisions to a given message. These two papers sealed the fate of MD4 as a no-longer-secure hash function.

In the first paper, a pre-image for a digest consisting of all zeros was constructed. This attack was only on the first two rounds of the algorithm, however, and served as only a theoretical result, although an impressive one at the time. Although the technical details of how this feat was accomplished were not published in this paper, they were revealed in the second paper. The basic idea behind the attack is that a message *X* is systematically chosen so that *X*′ = {*X*′ = *X*i for i ≠ 12 and *X*′12 = *X*12 + 1} and *X* collide after being hashed using MD4. The attack is broken down into three parts: Inner Almost-Collisions (Steps 12–19), Differential Attack Modulo 232 (Steps 20–35), and Right Initial Value (Steps 0–11). The attack is a bit long and complex, and the reader is directed to the original paper for more information.

The result of these attacks on MD4 was, in part, the reason for the creation of MD5. While the actual MD4 function is not secure, it paved the way for new algorithms and design techniques that are still used today. To quote Dobbertin, "There is no other way than to start with concrete proposals, thereby pushing on an evolutionary process leading to better and better solutions. Therefore the introduction of MD4 by Rivest in 1990 was a significant contribution."

## Attacks on MD5

The MD5 algorithm was based closely on that of MD4 with the addition of another round, and more constants. These changes improved the security of MD5 by making it harder to track and fix changes to the registers (A,B,C,D) because they changed throughout the algorithm. These changes in turn created new attacks to compensate for the increased complexity of the resulting algorithm. The definition of the algorithm follows:

Input: 16 message words, each word 32 bits long.

Output: 4 words, of 32 bits per word, which forms the resulting digest.

Algorithm:

Let *X*1 ... *n* = the words of the message, *H*1 = *A* = 0x67452301, *H*2 = *B* = 0xEFCDAB89, *H*3 = *C* = 0x98BADCFE, *H*4 = *D* = 0x10325476. Let *K**j* = abs(sin(*j* + 1)), 0 ≤ *j* ≤ 63 where *j* is in radians.

First Round: Let *M* = [0, 1, 2, ... 15], and *S* = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22]

For *i* = *0 ... 15*, let *F*(*X, Y, Z*) = (*X* ^ *Y*) ∨ (¬*X* ^ *Z*)

*TEMP* = (*A* + *F*(*B,C,D*) + *X*Mi + *Ki*) ⋘ *X**S*i

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *B* + *TEMP*

Second Round: Let *M* = [1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12] and *S* = [5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20]

For *i* = *0 ... 15*, let *G*(*X,Y,Z*) = (*X* ^ *Z*) ∨ (*Y* ^ ¬*Z*)

*TEMP* = (*A* + *G*(*B,C,D*) + *X*Mi + *K*i+16) ⋘ *X**S*i

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *B* + *TEMP*

Third Round: Let *M* = [5, 8, 11, 14, 1, 4, 710, 13, 0, 3, 6, 9, 12, 15, 2] and *S* = [4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23]

For *i* = *0 ... 15*, Let H(X, Y, Z) = *XxorYxorZ*

*TEMP* = (*A* + *H*(*B,C,D*) + *X*Mi + *K*i+32) ⋘ *X**S*i

*A* = *D*

*D* = *C*

*C* = *B*

*B* = *B* + *TEMP*

Fourth Round: Let *M* = [0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9] and *S* = [6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

For *i* = *0 ... 15*, let I(X,Y,Z) = Xxor(X∨¬Z)

*TEMP* = (*A* + *I*(*B,C,D*) + *X*Mi + *K*i+48) ⋘ *X**S*i

*A* = *D*

*D* = *C*

*C* = *B*

*B = B + TEMP*

Update chaining variables:

- *H*1 = *H*1 + A
- *H*2 = *H*2 + B
- *H*3 = *H*3 + C
- *H*4 = *H*4 + D

Continue from previous algorithm until all words of the message have been used to compute the digest.

Resulting Hash: *H*1 || *H*2 || *H*3 || *H*4

Padding:

Same as the padding for MD4.

Like the attacks on MD4, the attacks on MD5 came in stages. The first attacks came on the compression function of MD5. This trend of attacking the compression function is one that is applied to all hash functions. If the compression function in an algorithm cannot withstand cryptanalysis, then the entire function will not be able to either. This lesson was learned by cryptanalysis of block encryption functions that employed the use of compression functions.

One of the first and most successful attacks on the compression function used in MD5 was done by den Boer and Bosselaer (it is no coincidence that the same people who worked on attacking MD4 also worked on attacking MD5). Their paper creates a collision search algorithm for the compression function of MD5. The authors note that "the idea of the collision search algorithm is to produce an input to the compression function such that complementing the MSB [most significant bit] of each of the 4 words of the buffer (A,B,C,D) has no influence on the output of the compression function." The paper then goes on to define three propositions that are needed for the attack to be successful, and then proves that they are correct. The paper also goes so far as to give a precise algorithm for launching an attack against the compression function of MD5. The algorithm is as follows:

Set i = 12

If i = 1, a solution has been found as there are no constraints on the value of A at the beginning of the first round.

Do Step *i* backwards. The value at the beginning of Step *i* of the buffer word that is updated in this step is calculated using the known value at the end of the step and the value of *X*[*i* − 1] from the forward walk.

If the MSB of the new value is 1, decrement i and goto 2.

Set *j* = *fw*[*i*], *k* = *i* (*k* keeps track of the highest first round step using a message word that has been adapted during the forward walk). Adapt the *s*2[*j*] MSBs of *X*[*i* − 1] to let the value of the buffer word at the beginning of first round step *i* approximate the magic value *N*.

If *j* = 32, set *i* = *k* and goto 2, as there are no constraints on the value of B at the end of the second round.

Do Step *j* forwards.

If the MSB of the updated buffer word is 1, increment *j* and goto 6.

If *bw*[*j*] < *i*, compute *X*[*bw*[*j*] − 1] (i.e., if the message word used in this step has not been used yet in the backward walk, then use all the bits of this message word to make the updated value of the buffer word equal to *N*). Increment *j* and goto 6.

Adapt the 32 − *s*2[*j*] LSBs of *X*[*bw*[*j*] − 1] to let the updated value of the buffer word in Step *j* approximate the magic value *N* (i.e., in case the message word used in this step has already been used in the backward walk).

If *bw*[*j*] > *k*, set *k* = *bw*[*j*] (the highest first round step so far using a message word that has been changed during this forward walk, and hence the place to start a new backward walk).

Increment *j* and goto 6.

Along with this paper, another seminal paper was published by Hans Dobbertin titled "Cryptanalysis of MD5 Compress." This paper provided very little technical information on how the collision was created, but instead simply reported the collision (the entire paper is only two pages long with most of it being the collision and references). However, the final nail in the coffin for MD5 was a paper written by four Chinese scientists titled, "Collisions for Hash Functions MD4, MD5, HAVAL-128 and RIPEMD." This paper, like Dobbertin's, is very brief in details but outlines collisions for all of the above mentioned hash functions. Following this, two of the four published a paper titled "How to Break MD5 and Other Hash Functions," which put to rest any questions as to the security of MD5.

## Attacks on SHA-0

With successful attacks on MD4 and MD5, NIST set out to develop a secure hash function that could be used as the standard for hashing in the United States. With help from the National Security Agency, NIST developed SHA-0. The algorithm for SHA-0 follows.

Input: 16 message words, each word 32 bits long.

Output: 5 words, of 32 bits per word, which form the resulting digest.

Algorithm**:**

Let *X*1 ... 16 = the words of the message, *H*1 = *A* = 0x67452301, *H*2 = *B* = 0xEFCDAB89, *H*3 = *C* = 0x98BADCFE, *H*4 = *D* = 0x10325476 and *H*5 = E = 0xC3D2E1F0. Let *K*1 = 0x5A827999, *K*2 = 0x6ED9EBA1, *K*3 = 0x8F1BBCDC, *K*4 = 0xCA62C1D6.

Expansion Round: For i = 16 ... 79 (expand 16 words to 80 words).

*X*i = *X*i − 3*xorX*i − 8*xorX*i − 14*xorX*i − 16

First Round: For *i* = *0 ... 19*, let *F*(*X, Y, Z*) = (*X* ^ *Y*) ∨ (¬*X* ^ *Z*)

*TEMP* = *A* ⋘ 5 + *F*(*B, C, D*) + *X*i + *K*1

*E* = *D*

*D* = *C*

*C* = *B* ⋘ 30

*B* = *A*

*A* = *TEMP*

Second Round: For *i* = *20 ... 39*, let *G*(*X*, *Y*, *Z*) = *XxorYxorZ*

*TEMP* = *A* ⋘ 5 + *G*(*B, C, D*) + *X*i + *K*2

*E* = *D*

*D* = *C*

*C* = *B* ⋘ 30

*B* = *A*

*A* = *TEMP*

Third Round: For *i* = *40 ... 59*, let H(X, Y, Z) = (*X* ^ *Y*) ∨ (*X* ^ *Z*) ∨ (*Y* ^ *Z*)

*TEMP* = *A* ⋘ 5 + *H*(*B,C,D*) + *X*i + *K*3

*E* = *D*

*D* = *C*

*C* = *B* ⋘ 30

*B* = *A*

*A* = *TEMP*

Fourth Round: For *i* = *60 ... 79*, let *I*(*X, Y, Z*) = *XxorYxorZ*

*TEMP* = *A* ⋘ 5 + *I*(*B,C,D*) + *X*i + *K*3

*E* = *D*

*D* = *C*

*C* = *B* ⋘ 30

*B* = *A*

*A* = *TEMP*

Update chaining variables:

- *H*1 = *H*1 + A
- *H*2 = *H*2 + B
- *H*3 = *H*3 + C
- *H*4 = *H*4 + D

Continue from Step 2 until all words of the message have been used to compute the digest.

Resulting Hash: *H*1 || *H*2 || *H*3 || *H*4

Padding:

Same as the padding for MD4.

Attacks on SHA-0 have not been immediately as successful as those launched on MD4 and MD5. One of the major reasons for this was the inclusion of the expansion round in SHA-0 over MD4 or MD5. This expansion round makes it harder to correct bit flips because each bit has an impact in multiple places in the algorithm. However, successful attacks on SHA-0 were launched. The most seminal paper in the attacks on the SHA family was a paper written by Florent Chabaud and Antoine Joux titled, "Differential Collisions in SHA-0." This paper (sometimes referred to as the "cats and dogs" paper because of a name used in the paper for a modified version of the algorithm) provided the framework for a new type of attack on hash functions. This type of attack uses perturbation patterns and differential masks to find two messages that hash to the same digest.

This method of perturbation patterns and differential masks was then later extended by many other researchers to launch more successful and complete attacks to SHA-0, and eventually SHA-1. A paper by Eli Biham and Rafi Chen described an attack on SHA-0 that found near collisions where 142 of the 160 bits were the same. This paper was a bit overshadowed by the unofficial presentation at the CRYPTO 2004 Rump Session of a collision for the full 80 rounds of SHA-0. However, the method used to find the collision in the full 80 rounds was a modified version of Bihma and Chen.

Attacks to SHA-0 were not as surprising as those to come for SHA-1. The reason is that NSA commented on the fact that SHA-1 was created because of "a technical flaw" in SHA-0. Although nothing more was stated about this flaw, many have speculated as to what it is, and most feel confident that the flaw is understood. One presentation of an explanation of the change of the algorithm is presented in a paper by Chabaud and Joux titled, "Differential Collisions: an Explanation for SHA-1." The reason for the change is that "In the SHA-1 case, the bits are interleaved and therefore it is no more possible to split the Expansion."

## Attacks on SHA-1

Only two years after NIST published FIPS PUB 180, the agency revised it with a small change to the algorithm. As stated, the change in the algorithm was to fix a technical flaw. Neither NIST nor the NSA released specific details on what the flaw with SHA-0 was. The updated algorithm, SHA-1, is exactly the same as SHA-0 except for a single bit rotation in the expansion round. The change is outlined in the following text.

For i = 16 ... 79 (expand 16 words to 80 words)

*X*i = (*X*i−3*xorX*i−8*xorX*i−14*xorX*i−16) ⋘ 1

This change is quite small; however, it does a good job of interleaving the bits of the input message into the expanded message. In the design of SHA-0, the 64 newly formed words can be reduced to be simple combinations of the 16 original message words using the exclusive OR operation. However, with the introduction of the single bit rotation, no reduction can be made, and the entire calculation is needed to determine one of the new 64 words.

There have not been many noteworthy attacks on SHA-1. The biggest one was presented by researchers in China. The researchers, Xiaoyun Wang, Yiqun Lisa Yin, and Hongbo Yu, showed how to create two messages that result in the same SHA-1 digest using 269 operations instead of the 280 needed to launch a brute-force attack. The details of the attack have not been released, but messages have surfaced proving the attack is successful, and SHA-1 is not collision free.

## The future of hash functions

Cryptographic hash functions are extremely important to cryptographic protocols. They are the cornerstone of digital signatures and many other protocols. While the attacks on SHA-1 are not enough to immediately discontinue the use of the function, it is a strong indication that the SHA-2 family (SHA-256, SHA-384, and SHA-512) should be used in the place of SHA-1. The world of cryptography moves very slowly; however, the level of paranoia ensures the rapidity of accusations about the security of algorithms and protocols. There is no question that more research will need to be conducted in the area of hash functions. Hash functions are also one area of cryptography that doesn't look as though it can be addressed by newer technology such as quantum computing, or implementations such as secure tokens or biometrics. There is simply no replacement for a fast and secure hash function. NIST is already discussing holding a contest, like the one that led to the development of AES, to develop a new hash function standard for the United States.

# Quantum Cryptography

The advance in science that shows the most promise for sweeping change in the field of cryptography is in applications of quantum computing to cryptography. Quantum computing is a very complex and rigorous science that is still being discovered and explored today, both in the theoretical and practical sense. Most cryptographers only deal with quantum computing in the theoretical sense, in that they do not worry about how to implement algorithms or protocols using quantum computers. Rather, they need only an understanding of the properties and abilities of a quantum computer in order to construct algorithms and protocols.

This section will not go into how one goes about implementing a quantum computer, or creating quantum bits. This is too far beyond the scope of this chapter, and does not provide any insight into what can and cannot be done with a quantum computer and quantum bits. Instead, the properties and some of the physics behind quantum computation will be discussed to give further insight into how this new technology can be used to enrich and advance the field of cryptography.

## Quantum bits and quantum computation

Quantum bits, or qbits, are at the heart of quantum computation as one might imagine. Before I dive into a complex explanation of what a qbit is using bras and kets, a quick look a regular or classical bit is in order. In Dirac notation, a vector a is written inside a "ket," which is represented by |a>. The dual vector is written inside a "bra," which is written as <b| for some vector b. The inner product of two vectors is written as "bra-ket" and is denoted as <c||d> or as <c|d>.

A bit is simply a symbolic representation for that state of something. Usually a 0 and 1 are used to denote the state of, say, a group of particles on a magnetic strip. However, these 0s and 1s can just as easily be used to represent the state of an LED, on or off. When these symbols are manipulated, say by addition of logical AND, the underlying representation or implementation of the bit is irrelevant. It does not matter if the symbol represents a group of particles on a magnetic strip, or a set of LEDs. When the operation is complete, the symbols denote the final state of the system. This same sort of approach will be taken with qbits; however, the disconnect is not as easy to establish because the power of qbits comes from quantum mechanics. Without some understanding of quantum mechanics, an understanding of qbits is not possible. However, one need not be as smart as Einstein to understand qbits (in fact, when it comes to certain areas of quantum mechanics, such as the local variable theory, he was even wrong).

A quantum bit is simply the symbolic representation of the state of something, just like a classical bit. However, in the case of quantum bits, the "something" is usually not a simple group of particles on a magnetic strip or the illumination of an LED. Instead, a qbit represents the state of something like the polarization of a photon, or the spin of the nucleus of an atom. However, here is where things quickly begin to diverge. The state of a classical bit is known *a priori*, whereas the state of a qbit is not known until it is measured or observed. This is quite counterintuitive and confusing at first glance. For example, the length of a pencil may be four inches even if it hasn't been measured. That length is determined by what has happened to the pencil up to that point, but so long as no one or no thing alters its length, it is four inches — even if no one in the world measures the length. The same is not true on the quantum level. The direction of the spin of an atom's nucleus, for example, is not known until it is measured. The spin might be to the right, or it might be to the left, but it is not known until it is observed or measured. In fact the spin has a 50 percent chance of being to the right, and a 50 percent chance of being to the left. However, once the spin has been observed or measured it will remain that way until an outside force acts to change it, just like the length of the pencil. Once this idea that the state of something is not predetermined, but rather probabilistic, is comprehended, qbits and quantum computation are not that difficult to understand.

Let's return to our symbolic representation of qbits — a qbit is a vector in two-dimensional complex vector space. This vector space needs a basis for measurement. Because the state of something at the quantum level is not predetermined, the basis for measurement becomes very important. Consider the pencil example — if a pencil is 4 inches or 10.16 centimeters, the length is still the same. With qbits, the basis for measurement is important, as will be shown in the secure communication section, because it is the only way to gain information about a qbit. For qbits, the basic states of |0> and |1> are used to represent the same states as classical bits 0 and 1. For a more visual description of qbits and the need for a basis of measurement, imagine a single vector pointing from the center of the earth to any point on the earth. Now imagine the basis for measurement to be the north and south poles. It is clear that no matter where the vector points to on the earth it is either in the northern hemisphere or the southern hemisphere (assuming the equator is infinitely thin). Now if the basis for measurement changes to be either the eastern or western hemisphere, the meaning of the vector completely changes.

Because a qbit is simply a vector that has only a defined state when measured, then before being measured the qbit is in what is called an entangled state. This entangled state is a superposition of |0> and |1>. This superposition can be represented as *a*|0> + *b*|1> where *a* and *b* are complex numbers, normalized such that |a|2 + |b|2 = 1. The probability of a measured value for the qbit being a |0> is |a|2 and the probability of the measured qbit being a |1> is |b|2. It is the ability of a qbit to be in this superposition state that is so powerful compared to classical bits. However, it should not be misunderstood that a qbit in an entangled state is representative of both |0> and |1> simultaneously — it is not.

The bit is simply in a state that has not yet been observed, so it is not determined *a priori*. Again, this seems a bit counterintuitive and almost contradictory, but it is not. To illustrate this point, it is important to mention that a qbit does not yield any more information than a single classical bit. This is because information about a qbit can only be obtained by measuring the bit and this measurement changes the state of the bit to one of the two basic states. No matter how tricky someone is with measurement, only a single classical bit's worth of information can be obtained.

With that stated, let's step away from theoretical quantum mechanics because you understand the properties of qbits. The questions become what you can do with these quantum bits and why this provides such a useful behavior. The answer is closely tied to the basis of all computation, Turing machines. There are two types of Turing machines, deterministic and nondeterministic. A nondeterministic machine can compute all possible outcomes simultaneously and check the result for its correctness. The same is true with a quantum bit. A quantum bit can be set into an entangled state, and then computations can be performed on that bit. The bit can have only one of two final states when eventually measured, |0> or |1>, but while the computations are being performed it is as if both states are being computed simultaneously. With a single bit this is not very interesting; however, when using multiple bits it becomes quite interesting.

Just as a single qbit can be in an entangled state, two qbits can be entangled with each other. Each of the bits depends upon the other for its measurement. This can be seen with two qbits and the state |00> + |11>. This state cannot be represented by its component states, or qbits, separately. Stated differently, it is impossible to find *x*1,*x*2,*y*1,*y*2 such that (*x*1|0> +*y*1|1>)Â(*x*2|0> +*y*2|1>) = |00>+|11>. Now with *n* qbits, all 2*n* possible values can be represented at the same time during a computation. This ability to have all possible states represented simultaneously while doing calculations is what gives quantum computation its advantage over classical bits. This is much the same as the advantage you get by using a nondeterministic Turing machine over a deterministic Turing machine.

As with the discussion of a single entangled qbit, the discussion of multiple entangled qbits leads one to believe that these bits can be used to communicate, because their dependence upon each other exists no matter how far apart you pull the two qbits. If you consider two entangled bits, when one is measured the probability of the measurement of the other immediately changes. On the surface it appears that this can be used to transmit information or communicate faster than the speed of light. However, this is not so. Einstein, Podolsky, and Rosen proposed that each particle, represented by a qbit, has an internal state called a *local hidden variable*. This theory would explain the ability of one observation to change the other because nothing is really being changed—no communication is occurring. In essence, what they proposed was that this internal variable is already predetermined; it is just impossible to know which state it is in, |0> or |1>. However, this theory cannot explain measurements of entangled bits from different bases.

### Secure communication channel

Although it is not possible to communicate faster than the speed of light using quantum mechanics, it is possible to communicate securely. Using the properties of qbits and the observation that measuring a qbit in different bases can result in different interpretations of the same qbit leads to the ability to communicate securely. Let's look back at the example of the earth and a vector pointing from the center of the earth to some point in space; if one person was measuring this vector using the northern and southern hemispheres and someone else was using the eastern and western hemisphere as their basis, then one of them might decode the same vector as a |0> and the other might decode it as a |1>. It would also be possible for two people using two different bases to measure the particle and for both to observe a |0>. Using these principles, a secure line of communication can be established.

The communication works by establishing a key between two people, Alice and Bob, and then the key is used with classic block or stream ciphers to securely communicate. However, the ability to establish a key over the open channel is what quantum mechanics provides. The communication works by having two channels, one quantum and the other a regular channel. In this scheme, Alice picks a series of bits, more than needed for the key, and encodes them in qbits. The encoding of the qbits is in one of two bases for measurement, randomly chosen for each bit. Bob, upon receiving the qbits, measures each one with a randomly chosen basis as well. The two then exchange information about which basis they used to encode and measure, respectively, on the open channel. There is a 50 percent chance that they will have encoded and measured with the same basis. These bits where the basis is the same are used in making the key.

Suppose there is an eavesdropper, Eve, who is able to "listen" to both communication channels and also capture and retransmit bits. If Eve attempts to "listen" in on the quantum channel, the other action she can take would be to measure or observe the qbits. When she does so, however, she has a 50 percent chance of passing it along to Bob correctly because she picked the same basis as that of Alice. Now Bob will have a 25 percent chance of measuring the wrong value even when he chooses the correct basis. This reduction in correctly transmitted bits will result in Bob and Alice knowing something has gone wrong. This increased error rate is detected by the introduction of a sufficiently large number of parity bits for the key communicated via the normal open channel. In the end Eve's key has only a 25 percent chance of being correct, and Alice and Bob will know that someone is listening in on the channel.

While this method does not prevent someone from listening in, it does provide a method for indicating when this is happening. Using this method, the two parties can know when they have securely established a key, and then begin to use it with a more classic encryption algorithm. There are also a few other methods of securely establishing a key over a quantum channel that exploit the properties of qbits. This method, in a more complex and rigorous protocol, is used today between banks for securely establishing keys before transmitting data. This method, and others like it, proves to be nice replacements for current classic key exchange protocols, and/or the use of public key infrastructures for establishing keys.

### Fast factoring of large composites

With the ability to do multiple computations simultaneously, researchers directed their work towards solving problems that are known to be difficult on a classic computer. One such problem is that of factoring large composites. This problem has huge implications because it is the foundation of the security behind the RSA public key encryption system. If a method is discovered to factor large composites into their constitute prime factors, breaking RSA encrypted messages would become trivial. An algorithm that does exactly this was developed by Peter Shor in 1994, and is appropriately called Shor's Algorithm. Since then, Shor's algorithm has been realized on a quantum computer to factor the number 15. Not an amazing feat considering that a classic computer, or high school student, could easily factor the same number, but it showed that the theoretical algorithm actually works in the practical world.

The algorithm is not extremely complex from a number theory standpoint, but does involve some complex computation on a quantum machine, namely computing a quantum Fourier Transform, which is outside the scope of this chapter. However, even without the exact details of how one computes a quantum Fourier Transform, the intuition behind the algorithm is not lost.

The basic idea behind the algorithm is to implement a method for finding the period of the function *a**r*mod*n*. Once this period is discovered, it is only a matter of taking the greatest common divisor, and the two, hopefully nontrivial, factors are discovered. Three main ideas from number theory are required before one can understand how Shor's algorithm works.

It is assumed that the composite trying to be factored is of the form *pq* = *n* where both *p* and *q* are large unique prime numbers. If an *x* and *y* can be found such that *xy* = *kn* where *k* is an integer and neither *x* or *y* equal 1, then the factors of n are gcd(*x*, *n*) and gcd(*y*, *n*).

A number of the form *a*2*s* − 1 can be factored into (a5+1)(a*s*−1). If that number equals *kn*, *a*2*s* − 1 = *kn*, then the following is also valid: a2*s*−1 ≡ 0(modn).

If *a* and *n* are co-prime, meaning the gcd(*a*, *n*) = 1, then the function a*r* (modn) will always have a period: a0 (modn) ≡ 1, a*r* (modn) ≡ 1, a2*r* (modn) ≡ 1,...

With these ideas firmly grasped, understanding Shor's algorithm is straightforward. The hardest step in Shor's algorithm is the use of the quantum computer to compute the period of the function. This is done using a quantum Fourier Transform. The important thing to note about the transform is not how it is done, but that it takes polynomial time to produce the input. Current algorithms for computing the factors of large composites require exponential time in the size of the input. Shor's algorithm is outlined here:

Input: The number, *n*, to be factored that is of the form *n* = *pq*.

Output: The factors of *n*, *p*, and *q*.

Algorithm:

Randomly pick a value for *a*. Check to make sure *a* < *n* and that gcd(*a*, *n*) = 1, otherwise *a* is a factor of *n*: return *a* and *n*/*a*.

Using the quantum Fourier Transform, compute the period *r* of the function ar(modn).

If *r* is odd or if a*r*/2 ≡ −1 (modn) go back to previous algorithm.

If a*r*/2 ± 1 = ± 1 then only trivial factors found, go back to previous algorithm.

Compute the p = gcd(a*r*/2 + 1, n) and q = gcd(a*r*/2 − 1, n).

Return *p* and *q* as the nontrivial factors of n.

With this algorithm, a simple example can show more precisely how this algorithm works. In the following example, the number 35 will be factored into its two prime factors. The step in which the period is computed would normally be done on a quantum machine. The machine would simultaneously compute all equations of the following a*r* ≡ 1 (mod35) letting *r* be a variable constructed of qbits in an entangled state. This is the essence of computing the quantum Fourier Transform, and finding the period of the function.

**Example of Shor's Algorithm:**

Randomly pick *a* = 3.3 < 35 and gcd(3, 35) = 1 and continue.

Using the quantum computer, the period of 3r (mod35) is calculated to be *r* = 12.

Because *r* is even and 36≡−6 (mod35) you should continue.

36 + 1 = 730 and 36 − 1 = 728 so only nontrivial factors will be computed, as shown below:

gcd(730, 35) = 5 and gcd(728, 35) = 7

A quick check reveals that 5 * 7 = 35, so the factors of 35 were correctly computed.

The implications of Shor's algorithm and quantum computation on the field of cryptography have not yet been fully felt. As of this writing, hardware is the biggest obstacle to overcome in building a quantum computer that has registers with enough qbits in them to store numbers large enough to have an impact on cryptography today. So for now, RSA is safe because classical computers are not fast enough to factor the large numbers that are being used for RSA, and quantum computers do not have registers large enough to factor numbers of the size being used with RSA. However, quantum computers are making advancements, and new things are being experimented with for use as a qbit every day. However, some argue that quantum computers of any practical use will never be fully realized because of the tremendous power required for the qbit registers, and other obstacles dictated by the laws of physics. There is no question, however, that if quantum computers of any substantial size can be realized, it will be the single biggest change so far to the field of cryptography.

## Passwords are obsolete

Cryptography and the creation of encryption and decryption algorithms are usually performed by researchers in academic or corporate research settings. The average person does not sit at home and develop encryption algorithms. The theory, mathematics, and concepts that go into crafting an encryption algorithm are much too complex for most people to apply in a safe manner to create an encryption algorithm. In fact, most researchers in the field agree that encryption algorithms should be published openly to the world for review. The old saying of, "Obscurity is not a replacement for security" applies heavily to encryption algorithms. The algorithm should be strong enough so that it does not require keeping how the algorithm works a secret. If relying on the fact that the algorithm is secret is part of the security of the algorithm, then the algorithm is not secure. There will always be someone who can break the code open and figure out how the algorithm works.

So while the development of encryption algorithms should be left to the experts, and reviewed by the masses, the use of cryptography is done by everyday people. So how can someone who does not know how the algorithms work, or why they are secure, reliably use cryptography? The answer is that the implementations of the algorithms are created in a very, very user-friendly manner. While a certain encryption algorithm might require the use of a 1,024-bit key, a user of that algorithm certainly does not need to remember 1,024 bits of information. So the question then becomes how does it all work, and the answer is a password.

A password is an easy-to-remember piece of information for someone. This piece of information allows a human to use an encryption algorithm without needing to remember 1,024 bits of information for one algorithm, and then 512 bits for another. Instead, only a small easy-to-remember password is used for, in some cases, both algorithms. However, this immediately presents a problem. The algorithm requires 1,024 bits of information, but a password of "fluffy" (your cat's name) has been used instead. Assuming 8 bits of information per character, "fluffy" is only 48 bits worth of information, far from the 1,024 needed. Independent of the implementation, these 48 bits of information somehow need to be stretched into 1,024 bits of information. This is a clear flaw in the security of the system. The algorithm's creators have specifically required the use of 1,024 bits of information as the key to the algorithm. However, through an implementation this has been reduced to only the 48 bits of information needed.

## Pass phrases

Cryptography is only as good as the key that you use to protect the information. If that key is published to the world, assuming a symmetric key system, then while the algorithm can be flawless, the implementation is certainly flawed, leaving the information poorly protected and exposed to the world. Now most people do not publish their passwords to the world; however, leaving your passwords on a note attached to a computer monitor is virtually the same thing.

The reason people do such egregious things is simply because passwords are hard to remember. While it is very easy to remember "fluffy," your cat's name, it is much, much harder to remember a good password such as X93lIj. It is the same number of characters; however, it is meaningless to most people. So the problem of a good password being hard to remember has unavoidably presented itself. Counterintuitively, one of the solutions is to lengthen the size of a password required.

Instead of using a really small, hard-to-remember password such as X93lIj or, worse yet, a small and easy-to-remember-and-guess password such as "fluffy," one solution is to use a really long and easy-to-remember phrase. Passphrases have the best of both worlds. They are long, so they are hard to brute-force by simply trying all possible combinations, and yet they can be made to be easily remembered but still hard to guess. For example, instead of using the simple, easy-to-guess password of "fluffy," someone could easily come up with the passphrase, "Fluffy is my WHITE cat." Notice the use of capital letters in the phrase, making it harder to guess even if someone knew that your cat was white. While this passphrase is 3.8 times longer than the original password of "fluffy," it is just as easy to remember.

While passphrases are a great solution to an age-old problem, there are some drawbacks. The first complaint that people have with passphrases is simply the amount of time required to type them in. If you are a system administrator who types a password many times a day, it can become quite tedious to have to type this phrase or sentence each time you want to log into a computer. Learning to touch type can help, but if you are having to log into a machine on the order of 100 times a day, passphrases might not be a good solution for your password problem.

The second complaint with passphrases is that the implementation either does not provide enough space for the phrase, or requires too many characters. How long is a long-enough passphrase? Should you enforce that all passphrases be at least 14 characters long? What about the upper bound on a passphrase? Should passphrases be allowed to be 200 characters long? The general thinking is that implementations should require passphrases to be at least 10 characters long, and as long as the user likes, within reason. Putting an upper limit on a passphrase of 1,024 characters is certainly acceptable because not many people will want to type in a passphrase of that length even on a once-a-day basis.

The last complaint about passphrases is that there's an increased chance for error, simply because more characters have to be typed and the characters don't show up on the screen. It is easy to make a mistake, especially if the person entering the phrase is not a skilled typist. This problem is usually just cured by practice with the phrase. Most people are capable of remembering the phrase without needing to repeat it in their heads while typing, but instead can just type the phrase in.

### Secure tokens

Passphrases are a much better solution to authentication than passwords. However, they still have problems in that they need to be changed every so often just like a password, to increase security. For systems that need a higher level of security, such as systems dealing with money and personal information, secure tokens can often be used. In these systems it is less what someone remembers and more what a person has that enables them to authenticate at a terminal. This idea is akin to putting a lock on the door of a house. Without physically having the proper key to open the lock, access to the house is not allowed. Secure tokens work off this same principle. In some cases, however, it is not merely a smart card or some other physical thing that is read by the terminal, but rather a token that displays a password. These passwords, however, are constantly changing and are only valid for about 30 seconds to a minute.

These types of secure tokens are starting to become widely accepted and used. They have the advantage that someone using one of them does not need to remember a password, and yet the password they use to access the system is constantly changing. They work by having both the secure token and the server that processes the authentication running a pseudorandom number generator synchronously. This way, when someone enters the number on the secure token, it either matches the number on the server, or time has expired for that number and it does not match. This type of system also prevents what is called a *replay attack* where someone obtains the password or packets sent to the server containing the password, and replays those packets at a later time and successfully authenticates with the server.

The random number generator used is called a cryptographically secure random number generator. The strongest property of such a generator is that, if given one number, it is impossible to discover the next number. This is not true for a lot of the statistically random number generators. The most common cryptographically secure random number generator is the Blum-Blum-Shlumb random number generator. The algorithm works much like RSA under the assumption that integer factoring is a hard or intractable problem. The algorithm for the generator is given in the material that follows:

Generate two large unique primes, *p* and *q*, that are both congruent to 3 modulo 4. Multiply these primes together to get *n* = *pq*.

Select a random integer *s* (the seed) in the interval [1, *n* − 1] such that gcd(*s*, *n*) = 1.

Compute *x*0 = *s*2mod*n*

For i from 1 to *l*, where *l* is the length of the bit sequence needed

*x*i = *x*i−12mod*n*

*z*i = the least significant bit of *x*i

Output the sequence *z*1, *z*2, *z*3, ..., *z*l

The bit sequence that is outputted is then concatenated into a single integer and used as the randomly generated number on the secure token. The same algorithm using the same key and prime numbers is also run on the server. A new number is generated every 30 seconds to a minute on both the token and the server. The user need only read the number off the token and enter it at the prompt at the terminal.

This type of a replacement for passwords is very secure. The password might be small, but the fact that it changes every 30 seconds to a minute is what provides the security of the system. The biggest complaint about the system by users is needing to remember to always carry the token around with them. While the tokens are usually quite small, they can be a bit much to attach to a key chain. Also some of the more cheaply made secure tokens do not show when the number is about to change. A user can begin typing the password and then have it change before they've finished.

Overall, secure tokens are a new approach to an age-old problem of authentication. Instead of someone needing to remember something, someone now needs to have something. This is usually a lot easier to enforce and keep secure. Simply attaching a secure token to one's key chain is usually a good solution and prevents the token from being stolen. Also, like a credit card or physical key, if the token is ever stolen, access by using it can be immediately disabled, rendering it useless.

### Biometrics

The last new approach to authentication is that of some sort of biometric identification. Instead of someone having to remember a password or passphrase, or having to carry a secure token or smart card, biometrics uses the authentication method that someone must be something. This prevents the problems discussed with passphrases and secure tokens. Nothing needs to be remembered, and nothing can be lost. However, the downside to this type of a system is cost. Most biometric authentication methods are very expensive. Some work by scanning one's fingerprints or by scanning the retina of the eye. These methods usually work very well; however, fingerprints have been known to change over time from exposure to acid or something as common as playing the guitar. The same is true for anything physical; it can change over time, so a recalibration is often needed once a year.

However, the price and size of the equipment usually make this method prohibitive in most situations except those that need the most absolute level of security. It would simply be prohibitive to have a retina scanning box at each workstation in a 10,000-employee office building. However, fingerprint scanning devices are becoming smaller and cheaper each day. It will not be too long before passphrases are obsolete as well, giving way to either a secure token or fingerprint scanning mechanism to authenticate even the home user when making purchases over the Internet.

## Malicious uses of encryption

While cryptography and encryption can be very powerful and useful tools in everyday life, malicious uses are beginning to pop up. There has always been a debate surrounding cryptography and encryption because they empower the average Joe to keep secret from the government any piece of information. The algorithms and implementations found on the Internet today are as strong as those used by the military to protect national secrets. This has fueled the debate about whether citizens should be allowed to have encryption strong enough so that even law enforcement, under authority of a court, is unable to read the information. For a long time, cryptographic implementations could not be exported from this country. Things have changed; the debate is over. However, new uses of cryptography have begun to reopen this debate. This time it is not a question of whether cryptography can be prevented from being used, but rather of how to deal with it when it is used in a malicious manner.

### Blackmail (encrypting a hard disk, then paying for it to be decrypted)

One of the most obvious malicious uses for cryptography is in aiding with blackmail. Traditionally, blackmail works by threatening a person or organization with the release of damaging information unless money is paid. Cryptography can aid blackmail by publishing the information in an encrypted format on the Web before a demand is made. The information is published in a way that shows the targeted person or organization that the blackmailer is serious. It also provides more leverage because all that needs to be done is to distribute the key — the information itself has already been distributed. The use of encryption to aid in this type of blackmail is very powerful. It sends a strong message to whoever is being blackmailed that everything should be treated seriously. The key can even be sent with the demand, so that the target knows the damaging information is actually out there on the Web. And if a proper algorithm is used, with a large enough key, the information will remain safe virtually forever if the demands are met.

Another form of blackmail, often aided by cryptography, is to prevent the target from accessing essential information. This can, at times, be as dangerous and effective as releasing a secret. For example, if a corporation is developing a new piece of software, and the code for this software is kept on a central server, then if that server becomes encrypted, the software production will come to a halt. This type of setup is usually harder to perform, because it requires all backup copies of the code to be encrypted as well. A single complete or even partial backup of the information can render the entire blackmail attempt worthless. However, in this scenario it's not as easy to prove that the one making the demands actually has the key. The only option is to encrypt part of the code with one key and the other part with another key.

While these types of blackmail do not happen very often, they are becoming more common. They are usually not reported because the company being blackmailed doesn't want the reputation of having an insecure computer system that can be attacked in this manner. However, in most of these situations the blackmail is performed by someone who used to work for the company.

### Encryption in worms

Another malicious use of cryptography does not relate to blackmail as much to providing stealth for a piece of code. Encryption's main goal is to remove patterns from plain text and yet have the process be reversible. However, to perform such an action it's also important that a piece of plain text look completely different when using one key than when it is encrypted using a different key. This is how encryption can provide stealth to a piece of code. This technique can also be used by viruses to avoid detection by automated scanning utilities.

A virus can use encryption to become polymorphic, or change what it looks like with each infection. This is done by having the majority of the payload of the virus be encrypted using standard algorithms. Then with each file or computer that becomes infected, a new randomly chosen key is used to encrypt the virus. This changes the signature of the virus so that automated scanning utilities are unable to identify the virus simply by scanning for a signature.

The virus clearly needs to be decrypted at some point so that the machine can execute the code. This is done by having a small bootstrapping payload that runs first over the virus to decrypt it and then loads the virus into memory and runs it. There is also the question of where the key is stored. In most classic applications of encryption, the key is never to be stored with the encrypted data. However, in this case, the security of the actual code is not important, just the fact that it changes with each new key that is used. This ability of the virus to change its signature with each infection makes it polymorphic and very, very hard to detect.

Combining the goals of using encryption for stealth and to blackmail, a recent virus has made its rounds on the Internet to perform both activities. The virus uses encryption to become polymorphic so that scanners are not able to detect it as easily. The virus, once on your computer, begins to encrypt the hard disk. Then a message is displayed that asks for money to be sent to an e-mail address. Once the money has been transferred, the key is provided to unlock the hard disk. This type of a setup is quite gutsy because the writer of the virus takes steps to identify himself/herself by providing an e-mail address to send money to. However, these are the new threats on the Internet, and the use of cryptography unfortunately just aids in these techniques.

# Summary

Cryptography is a very slow moving field 99 percent of the time. However, in the remaining 1 percent of the time, discoveries can change the field of cryptography forever and swiftly. For example, small attacks on modified versions of algorithms make news in the cryptographic community, but do not really change how that particular algorithm is used all that much. However, if someone were to find a polynomial method for factoring large numbers, the field of cryptography would be changed permanently.

These changes are few and far between, and usually very unpredictable. Modifications to algorithms, the invention of new algorithms, and attacks on older algorithms happen every day. These additions to the field do not monumentally change the field, however, and they occur usually without notice beyond the main researchers in the field. Also, widespread acceptance of any new algorithm or modification takes a long time, and only after use by many people. The reason is security. It is important that an algorithm be reviewed and critiqued before it is used generally. All errors and possible attacks on an algorithm must be discovered before widespread use of an algorithm takes place.

Because cryptography moves slowly most of the time, it's hard to predict what the next big thing will be. Some of the areas mentioned in this chapter are among areas to keep an eye on. There is no question that quantum cryptography could potentially and radically change the field of cryptography forever. However, implementation and other issues mentioned do not make it look enormously promising — at the moment. But with hardware and technology changing every day, it might not be long before quantum key exchange boxes are hooked to computers to establish keys for use on the Internet. However, before that, the use of secure tokens, biometrics, and other methods for authentication will be more easily deployed. The new methods for authenticating with a computer are usually much more secure and just as easy, if not easier, than the old method of remembering and entering a password. The adoption of these new methods has been slow, but should soon prevail.

Cryptography is an important and potentially dangerous tool. The field is always changing and evolving. What tomorrow will bring with respect to cryptography is unclear. But peer review and strong implementations remain the cornerstone of this discipline.

While this chapter covered quite a bit of information, you should take note of a few important points.

- There are four main cryptographic primitives that are used to create all the cryptographic protocols used today. Each primitive has a specific use and, when combined, they can be very powerful.
- Using a key more than once on the same piece of plain text is very dangerous. No matter what the encryption algorithm, reusing a key can severely weaken the strength of the algorithm.
- Implementations and algorithms are two different things. While an algorithm can be completely secure, an implementation can be flawed for reasons that have nothing to do with security.
- Open source and standardized algorithms are always better than proprietary algorithms. Always stick to the standards and try, whenever possible, to use already tested implantations of the published algorithms.
