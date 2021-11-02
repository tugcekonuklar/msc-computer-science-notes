#### Main Topics

* Lesson 1, basics of network security requirements :
    * Cryptography
    * Data encryption
    * IoT
    * Symmetric -v- asymmetric cryptography
    * Certificates and Keys
    * Ethics and legal issues
* lesson 2 security.:
    * SSL
    * VPN’s
* lesson 3 :
    * IPSEC

#### Sub titles:

# Network Security requirements

Cryptographic algorithms such as encryption and hash functions play a role both in computer security threats and
computer security techniques and we will be examining these in this module.

The main security requirements of a secure system are:

Confidentiality - information is not made available to unauthorised entities, This is the most common use of
cryptographic algorithms: encrypting sensitive information for transmission over an insecure channel, such as the
Internet. In packet-based transmission, confidentiality is achieved by encrypting the information (plaintext) before
transmission and decrypting the ciphertext at the receiving end using the same (= symmetric) key.

Integrity - information has not been altered during transmission in an unauthorised manner. Some cryptographic
algorithms can be used to create digital signatures that ensure that unauthorized changes have not been made to
transmitted information.

Accountability – users must authenticate themselves before being able to access the system

Availability – in first hand this means prevention of Denial of Service (DoS) attacks.

Integrity Ensuring that information is not modified in an unauthorized fashion.

Authentication - providing the ability to confirm the claimed identity of an individual or system. Public key
cryptography can be used to create digital certificates that provide authentication capabilities.

Non-repudiation - allowing the recipient of a message to undeniably prove to a third party that the message came from
the purported sender. Digital signatures provide nonrepudiation and, when they are used, prevent the sender of a message
from later denying that he or she originated the message.

# BYOD (Bring Your Own Devices)
* Bring Your Own Devices (BYOD) is a relatively new phenomenon and is now common.  Start by reading these articles looking at different aspects of BYOD for and organisation and then consider the questions that follow.

Question 1

Does BYOD save money?

Always
Never
Sometimes
Answer:
3. Sometimes

BYOD can save money in some ways, but cost money in others. For example, allowing users to purchase their own devices and bring them to work might save a company money on device purchasing, but it costs money to put management systems in place and train helpdesk staff.

Question 1

Does BYOD save money?

Always
Never
Sometimes
Answer:
3. Sometimes

BYOD can save money in some ways, but cost money in others. For example, allowing users to purchase their own devices and bring them to work might save a company money on device purchasing, but it costs money to put management systems in place and train helpdesk staff.



Question 2

True or false: Businesses should be concerned about the legal ramifications that exist for allowing BYOD.

True
False
Answer:
True

There are a couple of reasons that companies have to be concerned about legal issues when it comes to BYOD. Businesses have to worry about users' privacy: If the system that the IT department uses to manage devices or track users' activity exposes that an employee is engaging in illegal activities, the company may be obligated to report that information. An additional BYOD challenge is that many companies are subject to information security regulations, such as in health care or government. If employees have patient or confidential data on their personal devices, the company can face serious legal trouble



Question 3

How can businesses reduce the risks associated with corporate data security in BYOD environments?

Write policies that state which actions are acceptable for users to perform on their devices.
Encrypt data and devices and use two-factor authentication.
Both of the above.
Answer:
3. Both of the above.



Question 4

Which of the following is not an advantage of BYOD?

It can reduce capital spending on devices.
It improves employee productivity.
It lightens the help desk staff's workload.
It helps IT embrace the cloud.
Answer:
2. It improves employee productivity.

Though advantages of BYOD include reducing spending on devices, improving productivity and helping IT embrace the mobile- and cloud-centric way employees work today, one of the biggest BYOD challenges is that it puts more pressure on help desk staff. Not only do staff members have to undergo training in how to deal with consumer devices and how to use mobile management systems, but employees will also expect IT to help them with issues that may arise with their personal devices.



Question 5

Which of the following is a BYOD challenge?

Bandwidth strain
International roaming charges
Security flaws within devices
All of the above
Answer:
4. All of the above

These are just a few challenges that companies forget to consider when they're thinking about allowing BYOD. When businesses planned their networks, they did so with a one-device-per-user ratio in mind. But if users bring two or three devices to work with them, that's going to adversely affect bandwidth. And companies whose workers travel internationally have to deal with the roaming overages that their users are going to incur. Also remember that people find ways around lock screens and other features that are meant to keep a device secure.

 

# Ethics and Legal considerations
Ethics has a very broad definition in computing use and this can include challenging the principles of societal behaviour.

Points to consider may include:

The government's decisions on what should be regulated and what should not
In philosophy, the notion of intelligence and AI
In society – new apps which represent freedom or control
Ethical points to consider:

Charges for financial transactions – who decides what is fair? We are in an environment of electronic payments as opposed to cash, but who decides on the charges?
Interactive apps / TV – collecting data from children? Who is policing this?
Decisions made now – how might they affect future generations?
Education – the levels of abstraction. Increasingly we're moving from long division to abstraction, thus removing the need for the underlying skill – word processing and spell check is another example.
Libraries and access for all – does the technological equivalent provide these rights?
Automation of information and apps – how much does the government collect about an individual? Do you know what information is being collected and held about you? Where does it come from and who does it go to?
Society's dependence on technology – what would be the consequences if technology was removed?
GPS – tracking a person's movements – how far will this go?
Legal consideration may include:

Security concerns / BYOD / wifi hopping
Software ownership and liability / intellectual ownership copyright
Social impacts of distributed databases
Consequences of AI
Different laws in different countries
Just because something is illegal it does not mean it is not possible!

Some of the main legislative acts which cover legal use of computing include:

Computer Fraud and Abuse Act 1984 – USA
Right of Privacy Act
Anticybersquatting Act 1999
Policy standards and Acts cover the legislation that needs to be adhered to. These include the following:

Data Protection and GDPR 2018, and then updated 2021
Computer Misuse ActCryptography 1990
Communications Act 2003
Investigatory Powers Act 2016
The Investigatory Powers (Interception by Business etc. For Monitoring and Record-Keeping Purposes) Regulations 2018
Privacy and Electronic Communications (EC Directive) Regulations 2003, amended with Privacy and Electronic Communications (EC Directive) (Amendment) Regulations 2019

# Cryptography
Cryptography is the science of transmitting information securely. Information security professionals rely upon cryptographic algorithms, or ciphers, to add security to communications that would otherwise be susceptible to eavesdropping and other attacks. Crypto- graphic algorithms work to fulfil the four goals of confidentiality, integrity, authentication and nonrepudiation.

Cryptography, the practice of using encryption and decryption algorithms to obscure information in a reversible manner, is one of the main tools used to support two of these goals: confidentiality and integrity. In addition to supporting those major goals, some cryptographic algorithms can also be used to provide authentication and nonrepudiation functions.

Symmetric vs. asymmetric cryptography
Cryptographic algorithms can be assigned to one of two categories based upon the keys used by the sender and recipient. In symmetric cryptography, both the sender and the recipient use the same key to encrypt and decrypt the message. This key, known as a shared secret key, must be securely exchanged in advance of the communication. Alice can encrypt a message by using the encryption algorithm with the shared secret key to transform it into the ciphertext. When Bob receives the message, he uses the decryption algorithm, along with the same shared secret key used by Alice, to decrypt the message.

In asymmetric cryptography, on the other hand, the sender and receiver use different, but mathematically related, keys to encrypt and decrypt the message. Each participant in an

Key asymmetric cryptosystem has a pair of mathematically related keys: a public key and a private key. The private key is preserved as a secret known only to the individual who owns the keypair. The public key is freely distributed to anyone the individual wants to communicate with. The public and private keys are related in such a fashion that anything encrypted with one key from a pair can be decrypted with the corresponding key from the same pair.

For example, if Alice wanted to use asymmetric cryptography to send a message to Bob, she encrypts the message with Bob’s public key. Due to the nature of asymmetric cryptography, this message can then only be decrypted with the other key from that same keypair—Bob’s private key. Bob is the only person with access to that key, so the message can only be decrypted by Bob. In fact, Alice, who encrypted the message, does not have the ability to decrypt it herself because she does not have access to Bob’s private key.

Symmetrical encryption (for confidentiality)
Public key cryptography algorithms are far too slow to be used for encrypting the actual traffic to be carried over the communication link directly. For this purpose, symmetrical encryption (= encryption and decryption are performed with the same key) must be used.

Some widely used symmetrical encryption algorithms are Advanced Encryption Standard (AES) and 3-fold Data Encryption Standard (3DES) for encrypting blocks of information, and Rivest Cipher 4 (RC4) for encrypting streams of information.

#  Public key cryptography
## Diffie-Hellman vs. RSA
Public key cryptography is generally used in two ways:

by generating a shared secret at both ends of the communications link (key agreement)
by sending a secret to the other end of the communications link (key transport)
Known as the Diffie-Hellman key agreement scheme.

Or

by sending a secret to the other end of the communications link (key transport)
The RSA (Rivest, Shamir, Aldeman) scheme.

Question 1

In what way does a hash provide a between message integrity check than a checksum (such as the Internet checksum)

Answer:
One requirement of a message digest is that given a message M, it is very difficult to find another message M’ that has the same message digest and, as a corollary, that given a message digest value it is difficult to find a message M’’ that has that given message digest value. We have “message integrity” in the sense that we have reasonable confidence that given a message M and its signed message digest that the message was not altered since the message digest was computed and signed. This is not true of the Internet checksum, where it easy to find two messages with the same Internet checksum..



Question 2

Can you 'Decrypt' a hash of a message to get the original message? Explain your answer.

Answer:
No. This is because a hash function is a one-way function. That is, given any hash value, the original message cannot be recovered (given h such that h=H(m), one cannot recover m from h).



Question 3

What does it mean for a signed document to be verifiable and non-forgetable?

Answer:
Suppose Bob sends an encrypted document to Alice. To be verifiable, Alice must be able to convince herself that Bob sent the encrypted document. To be non-forgeable, Alice must be able to convince herself that only Bob could have sent the encrypted document (e.g.,, no one else could have guessed a key and encrypted/sent the document) To be non-reputable, Alice must be able to convince someone else that only Bob could have sent the document. To illustrate the latter distinction, suppose Bob and Alice share a secret key, and they are the only ones in the world who know the key. If Alice receives a document that was encrypted with the key, and knows that she did not encrypt the document herself, then the document is known to be verifiable and non-forgeable (assuming a suitably strong encryption system was used). However, Alice cannot convince someone else that Bob must have sent the document, since in fact Alice knew the key herself and could have encrypted/sent the document.



Question 4

Name two popular secure networking protocols in which public key certification is used.

Answer:
This is false. To create the certificate, certifier.com would include a digital signature, which is a hash of foo.com’s information (including its public key), and signed with certifier.com’s private key.



Question 5

In the link-state routing algorithm, we would somehow need to distribute the secret authentication key to each of the routers in the autonomous system. How do we ditribute the shared authentication key to the communicating entities?

Answer:
A public-key signed message digest is “better” in that one need only encrypt (using the private key) a short message digest, rather than the entire message. Since public key encryption with a technique like RSA is expensive, it’s desirable to have to sign (encrypt) a smaller amount of data than a larger amount of data.

# Pretty Good Privacy (PGP)
The Pretty Good Privacy (PGP) algorithm combines the use of symmetric and asymmetric cryptography. The process used to encrypt a message by using PGP uses the following steps:

The sender of the message chooses a randomly generated symmetric encryption key.
The sender encrypts the message by using the symmetric encryption key and a symmetric algorithm of the sender’s choice.
The sender encrypts the randomly generated symmetric encryption key with the recipient’s public key, using an asymmetric algorithm of the sender’s choice.
The sender transmits the encrypted message from step 2 and the encrypted key from step 3 to the recipient.
When the recipient receives the message, he or she follows the process to decrypt the message. The recipient decrypts the encrypted key by using the recipient’s private key. The recipient now has the randomly generated symmetric encryption key chosen by the sender. The recipient decrypts the message by using the symmetric key.

RSA vs. DSA
As with any asymmetric algorithm, the complexity of RSA lies in finding an appropriate method to generate mathematically related, but secure, public and private keypairs. RSA does this by relying upon the difficulty of factoring the products of large prime numbers. The algorithm itself is still considered secure today.

In addition to secure key transport, the public key encryption method RSA also offers authentication using a digital signature. Another algorithm that can be used for this purpose is Digital Signature Algorithm (DSA).

RSA:  Key management + authentication
DSA:  Only authentication, no key management
Diffie-Hellman:  Only key management, no authentication.  

# Data Encryption Standard

One of the most well-known symmetric encryption algorithms, the Data Encryption Standard (DES) was selected by the US Government in 1976 as the standard encryption algorithm for government applications. DES is a symmetric block cipher that uses 56-bit encryption keys to operate on 64-bit blocks of data. Though it was widely used for decades in both the public and private sectors, the cryptographic community now considers DES insecure, due to the possibility of modern computers successfully conducting a brute-force attack against the short encryption keys used by DES. The algorithm is no longer approved for use by the US government, and private-sector cryptographers should consider using a different symmetric cipher. DES transforms plaintext into ciphertext by performing a variety of cryptographic operations on 64-bit blocks of data. The core building block of DES is the Feistel function which operates on half-blocks of data that are 32 bits long. 

## Triple DES (3DES) 
When cryptographers began to realize that DES was becoming cryptographically insecure, they were left in a quandary. Organisations in both government and the private sector had invested millions of dollars in hardware and software designed to work specifically with DES, and that investment was now facing obsolescence. Fortunately, cryptographers discovered that they could continue to use existing DES implementations in a secure manner by sim ply running data through the algorithm three times with different keys. This process became known as Triple DES (3DES). Because 3DES simply uses DES multiple times, it remains a 64-bit symmetric block cipher.

Users of 3DES choose three 56-bit encryption keys, called K1, K2, and K3. They then perform three steps:

Encrypt the plaintext by using DES with K1.
Decrypt the result of step 1 by using DES with K2.
Encrypt the result of step 2 by using DES with K3.
The output of step 3 is the ciphertext output of the 3DES algorithm.

When the recipient of a 3DES-encrypted message wants to transform the ciphertext back into plaintext, the following process is used:

Decrypt the plaintext by using DES with K3.
Encrypt the result of step 1 by using DES with K2.
Decrypt the result of step 2 by using DES with K1.
The user of 3DES can select the keys by using one of three approaches, each of which  provides a different effective key length:

In the most common approach, the keys are independent. K1, K2, and K3 are unrelated, randomly generated 56-bit keys. This is the strongest approach, providing a key length of 168 bits (three keys of 56 bits each) that is actually reduced to an effective key strength of 112 bits due to the existence of attacks on this approach.
In the second option, K1 and K2 are independent, but K1 = K3. This approach provides a key length of 112 bits (two keys of 56 bits each) that is reduced to an effective key strength of 80 bits due to existing attacks.
In the final option, all three keys are the same: K1=K2=K3. 3DES.
The use of 3DES is still considered secure today, this is functionally equivalent to DES and provides the same (insecure) key length of 56 bits. It is preserved to provide backward compatibility with systems that are not able to perform National Institute of Standards and Technology (NIST), and it remains certified for US federal government use.

Question 1

The encryption technique is know - published, standardised and available to everyone, even a potential intruder. Then where does the security of an encryption technique come from?

Answer:
1. Confidentiality is the property that the original plaintext message can not be determined by an attacker who intercepts the ciphertext-encryption of the original plaintext message. Message integrity is the property that the receiver can detect whether the message sent (whether encrypted or not) was altered in transit. The two are thus different concepts, and one can have one without the other. An encrypted message that is altered in transmit may still be confidential (the attacker can not determine the original plaintext) but will not have message integrity if the error is undetected. Similarly, a message that is altered in transit (and detected) could have been sent in plaintext and thus would not be confidential.



Question 2

What is the difference between known plaintext attack and chosen plaintext attack?

Answer:
4. In this case, a known plaintext attack is performed. If, somehow, the message encrypted by the sender was chosen by the attacker, then this would be a chosen-plaintext attack.



Question 3

Consider a 16 block cipher. How many possible input blocks does this cipher have? How many possible mappings are there? If we view each mapping as a key, then how many possible keys does this cipher have?

Answer:
3. 5. An 8-block cipher has 28 possible input blocks. Each mapping is a permutation of the 28 input blocks; so there are 28! possible mappings; so there are 28! possible keys.



Question 4

Suppose N people want to communicate with each of N - 1 other people using symmetric key encryption. All communication between any two people, i and j, is visible to all other people in the group of N, and no other person in this group should be able to decode their communication. How many keys are required in the system as a whole? Now suppose that public key encryption is used. How many keys are required in this case?

Answer:
If each user wants to communicate with N other users, then each pair of users must have a shared symmetric key. There are N*(N-1)/2 such pairs and thus there are N*(N-1)/2 keys. With a public key system, each user has a public key which is known to all, and a private key (which is secret and only known by the user). There are thus 2N keys in the public key system.



Question 5

Supposing you want to encrypt the message 10010111 by encrypting the decimal number that corresponds to the message. what is the decimal number?

Answer:
175

# Message digests, certificates and key length

## Message digests (for integrity protection)
In packet-based transmission, integrity protection is ensured by using a message digest or hash algorithm to produce a Message Authentication Code (MAC) field that is appended to the data (usually before the encryption).

If an attacker changes the content of the message during transmission, the calculated MAC and transmitted MAC at the receiving end will nor match.

Two widely used message digest or hash algorithms are Message Digest 5 (MD5) and Secure Hash Algorithm 1 (SHA-1).

## Certificates
Key agreement (e.g. Diffie-Hellman) or key transport (e.g. RSA) schemes are vulnerable to man-in-the-middle attacks. A solution to this problem is to send the public key over the communication link using a signed certificate.

A certificate is a document that contains, along with the public key of the sender, the name of the certificate holder as well as the digital signature of an independent and trusted third party, called certification authority, to ensure the validity of the transmitted information. The certificate format is usually based on ITU-T recommendation X.509.

## Key length
In the same way as long passwords make password guessing impractical, long keys make exhaustive searches impractical.

Every additional bit in the key doubles search time (and doubles the number of possible keys), so adding even a few bits to a key’s length greatly increases the time needed to perform an exhaustive search. In addition to using long keys, it is important to change keys frequently.

There are complete security solutions that incorporate the various security mechanisms presented on the previous slides, that is key management schemes (Diffie-Hellman, RSA), authentication methods (RSA, DSA), encryption methods (AES, 3DES, RC4), integrity protection methods (MD5, SHA-1), additional security measures (e.g. anti-replay protection) and certificate management.

Important security solutions are SSL (TLS), SSH and IPSec. For wireless networks, there is Wired Equivalent Privacy (WEP) and Wi-Fi Protected Access (WPA).

# Digital signature

Digital signatures depend upon one of the properties of asymmetric algorithms—that anything encrypted with one key from a keypair can be decrypted with the other key from that pair.

As an alternative way of using private and public keys, if Alice encrypts a message with her private key, anybody can decrypt the message using Alice’s public key. No one else can encrypt the message in such a way that decrypting the message with Alice’s public key will give a valid result. In other words, Alice has authenticated herself by providing a digital signature.

The use of asymmetric cryptography for confidentiality, the sender of the message used the recipient’s public key to encrypt the message so that it required the recipient’s private key (known only to the recipient) to decrypt. With digital signatures, there is a different objective—you want to create something that only you could create and that anybody can verify. This requires using the sender’s private key to create the digital signature, which anybody can then verify with the sender’s public key.

Here’s the process for creating a digital signature:

The sender and receiver agree upon a hash function that they will use to create a message digest.
The sender of the message uses the agreed-upon hash function to create a message digest of the message.
The sender of the message encrypts the message digest with the sender’s private key to create a digital signature.
The sender attaches the digital signature to the message and sends it to the recipient.
When the recipient of the message (or anyone else) wants to verify the digital signature, the recipient follows this process:
Using the same hash function selected by the sender, the recipient creates a message digest from the plaintext message.
The recipient decrypts the digital signature by using the sender’s public key to obtain the message digest computed by the sender.
The recipient compares the message digests generated by steps 1 and 2. If they match, the message is authentic.
It is very important to note that the only real conclusion you can draw from the digital signature process is that a message is authentic if the two digests match. If the digests do not match, you don’t know what has gone wrong. The digital signature might be forged, the message might have been intentionally tampered with, or the message might have been inadvertently altered in transit. You also can’t tell how “close” the message is to the authentic message because of the properties of hash functions.


# SSL
Secure Socket Layer (SSL) is a transport layer protocol (running on top of TCP) that offers security features for applications running on top of SSL, for example, HTTP over SSL (HTTPS), Simple Mail Transfer Protocol (SMTP) over SSL, or Lightweight Directory Access Protocol (LDAP) over SSL (LDAPS). These are client-server types of applications.

SSL was originally designed to provide security for web traffic. Early versions of SSL had several flaws that led to the creation of SSL 3.0, and then to the creation of Transport Layer Security (TLS) 1.0, which is broadly used today. TLS is an encryption protocol used to provide secure communication over networks to protect web traffic, email, VoIP, and other protocols. Today, SSL and TLS are often used as interchangeable terms, although TLS is most often the correct term. Many services are provided with both a TLS-protected version and a non-TLS version of the service, such as secure web traffic on port 443 as HTTPS, and unencrypted web traffic on port 80 for normal HTTP. TLS has a broad range of uses, from protecting services to providing the underlying security layer in SSL virtual private networks.

Before data transport can take place over a secure SSL connection, the connection must first be established using a handshake procedure. During the SSL handshake, the client and server need to agree on the algorithms that will be used to protect the data (first phase). Then, the server sends its public key in a signed certificate to the client, so that the client can authenticate the server (second phase) using the RSA or DSA authentication method.

The client generates a so-called pre-master secret and sends this secret in encrypted form (using the server’s public key for encryption) to the server (third phase). Both the server and client side use the pre-master secret for generating the actual keys for symmetrical encryption as well as the message authentication code (MAC). Finally, the client and server both calculate the MAC of the complete handshake information up to this point and send this information to the other side (fourth phase). Now the data communication can start.

Basic SSL handshake operation

Question 1

What is the defacto e-mail encryption scheme? What does it use for authentication?

Answer:
Alice provides a digital signature, from which Bob can verify that message came from Alice. PGP uses digital signatures, not MACs, for message integrity.



Question 2

In the SSL record, there is a field for SSL sequence numbers. True or False?

Answer:
False. SSL uses implicit sequence numbers.



Question 3

What is the purpose of the random nonces in the SSL handshake?

Answer:
The purpose of the random nonces in the handshake is to defend against the connection replay attack.



Question 4

Is there a fixed encryption algorithm in SSL?

Answer:
alse. An IKE SA is used to establish one or more IPsec SAs..

# Tunnelling

When tunnelling is used as a transition mechanism to IPv6, it involves encapsulating one type of protocol in another type of protocol for the purpose of transmitting it across a network that supports the packet type or protocol. At the tunnel endpoint, the packet is de-encapsulated and the contents are then processed in its native form.

Overlay tunnelling encapsulates IPv6 packets in IPv4 packets for delivery across an IPv4 network. Overlay tunnels can be configured between border routers or between a border router and a host capable of supporting both IPv6 and IPv4.

## GRE Tunnels
Although not used as an IPv6 transition mechanism, Generic Routing Encapsulation (GRE) tunnels are worth discussing while talking about tunneling. GRE is a general-purpose encap- sulation that allows for transporting packets from one network through another network through a VPN. One of its benefits is its ability to use a routing protocol. It also can carry non-IP traffic, and when implemented as a GRE over IPsec tunnel, it supports encryption. When this type of tunnel is built, the GRE encapsulation will occur before the IPSec encryp- tion process. One key thing to keep in mind is that the tunnel interfaces on either end must be in the same subnet.

## 6to4 Tunneling
6to4 tunneling is super useful for carrying IPv6 data over a network that is still IPv4. In some cases, you will have IPv6 subnets or portions of your network that are all IPv6, and those networks will have to communicate with each other. This could happen over a WAN or some other network that you do not control. So how do we fix this problem? By creating a tunnel that will carry the IPv6 traffic for you across the IPv4 network. Now having a tun- nel is not that hard, and it isn’t difficult to understand. It is really taking the IPv6 packet that would normally be traveling across the network, grabbing it up, and placing an IPv4 header on the front of it that specifies an IPv4 protocol type of 41.

When you’re configuring either a manual or automatic tunnel (covered in the next two sections), three key pieces must be configured:

The tunnel mode
The IPv4 tunnel source
A 6to4 IPv6 address that lies within 2002 ::/16
 
# Virtual Private Network (VPN)

A virtual private network (VPN) can be used within a public telecommunication infrastructure, such as the Internet, to provide remote offices or individual users with secure access to their organisation's network.

Screenshot 2021-09-01 at 10.44.51.png

A typical WAN connects two or more remote LANs together using someone else’s network this could be your Internet service provider  (ISP)—and a router. Your local host and router see these networks as remote networks and not as local networks or local resources. This would be a WAN in its most general definition. A VPN actually makes your local host part of the remote network by using the WAN link that connects you to the remote LAN. The VPN will make your host appear as though it’s actually local on the remote network, resulting in having access to the remote LAN’s resources and that access is very secure.

A VPN allows you to connect to these resources by locally attaching to the VLAN through a VPN across the WAN. The other option is to open up a network and servers to everyone on the Internet or another WAN service, in which case the security is compromised.

Types of VPNs are named based on the kind of role they play in a real-world business situation. There are three different categories of VPNs:

Client-to-Site (Remote-Access) VPNs Remote-access VPNs allow remote users like telecommuters to securely access the corporate network wherever and whenever they need to. It is typical that users can connect to the Internet but not to the office via their VPN client because they don’t have the correct VPN address and password.

Host-to-Host VPN A host-to-host VPN is somewhat like a site-to-site in concept except that the endpoints of the tunnel are two individual hosts. In this case all traffic is protected from the time it leaves the NIC on one host until it reaches the NIC of the other host.

Site-to-Site VPNs Site-to-site VPNs, or intranet VPNs, allow a company to connect its remote sites to the corporate backbone securely over a public medium like the Internet instead of requiring more expensive wide area network (WAN) connections like Frame Relay. This is probably the best solution for connecting a remote office to a main company office.

Extranet VPNs Extranet VPNs allow an organization’s suppliers, partners, and customers to be connected to the corporate network in a limited way for business-to-business (B2B) communications.

VPN concentrators
Secure remote access to networks is typically handled by virtual private network (VPN) concentrators. VPN concentrators allow remote users to securely connect to them and then provide secure encrypted communications between the remote machine and the organisation’s network by building a secure tunnel across the Internet or other network. In addition to providing remote access for individuals, VPN concentrators are often used to build secure networks between organizational networks across public Internet connections.

Current VPN concentrators typically use one of two major technologies for their VPN sessions: IPSec or SSL. Both have advantages and disadvantages:

IPSec VPNs have been the traditional answer to VPN needs. For IPSec VPNs to work, the client needs to have an IPSec VPN client installed and configured to work with the VPN concentrator, which can be expensive in time and effort if you have a large number of VPN users. IPSec VPNs operate at the network layer of the OSI (Open Systems Interconnection) model, meaning that the workstation that connects appears to be a part of the network where the VPN concentrator resides—in essence, the remote machine looks like it is on the local enterprise network. This is a benefit when applications depend on being on the local network, but it also means that remote systems can appear inside your protected network!

SSL VPNs use the client’s web browser to connect, meaning that there’s no additional overhead for installation and maintenance of a client. This means that they’re usually easier to support and deploy and that web-based applications are easily used via the VPN. The disadvantage to this is that only web-based applications will work via an SSL VPN, meaning that client-based applications won’t work out of the box without additional work to make them pass through the SSL VPN. If your organization is reliant on client-based thick client applications, printing, or storage, SSL VPN might not be the right solution.

SSL and SSL VPN
Secure Sockets Layer (SSL) security protocol was developed by Netscape to work with its browser. It’s based on Rivest, Shamir, and Adleman (RSA) public-key encryption and used to enable secure Session layer connections over the Internet between a web browser and a web server. SSL is service independent, meaning a lot of different network applications can be secured with it—a familiar one being the ubiquitous HTTP Secure (HTTPS) protocol. Later, SSL was merged with other Transport layer security protocols to form a new protocol called Transport Layer Security (TLS). The latest version of Transport Layer Security (TLS 2.0) provides a number of enhancements over earlier versions. The following are the most noteworthy:

Several improvements in the operation of a central component, the MD5/SHA-1 hash- ing function. Hashing functions are used to ensure that the data is not changed or altered (also known as maintaining data integrity).
More flexibility in the choice of hashing and encryption algorithms on the part of the client and the server.
Enhanced support for the Advanced Encryption Standard (AES).
SSL VPN is really the process of using SSL to create a virtual private network (VPN).


A VPN is a secured connection between two systems that would otherwise have to connect to each other through a non-secured network.

VPNs are essential for data that’s being sent within a private network that you wouldn’t want everyone on that network to be able to see. If you need a few specific computers on the intranet to be able to communicate with each other securely—for instance PC’s used in finance. you wouldn’t necessarily want that data sent off in a non secure or visible format.? No way. So, the finance machines can go on a VPN emulating them on their own private, secure subnetwork.

DTLS
Datagram Transport Layer Security (DTLS) provides security for datagram-based applications by allowing them to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery. It is based on the stream-oriented Transport Layer Security (TLS) protocol and is intended to provide similar security guarantees.

L2TP
The Layer 2 Tunneling Protocol (L2TP), which was created by the Internet Engineering Task Force (IETF). Is used for supporting non-TCP/IP protocols in VPNs over the Internet. L2TP is actually a combination of Microsoft’s Point-to-Point Tunneling Protocol (PPTP) and Cisco’s Layer 2 Forwarding (L2F) technologies. A sound L2TP feature is that, because it works at the Data Link layer (Layer 2) of the OSI model, it can support many protocols beyond just TCP/IP—a couple being Internetwork Packet Exchange (IPX) and AppleTalk. It’s a good tool to implement if you happen to have two non-TCP/IP networks that need to be connected via the Internet.

PPTP
PPTP acts by combining an unsecured Point-to-Point Protocol (PPP) session with a secured session using the Generic Routing Encapsulation (GRE) protocol. Because PPTP uses two different protocols, it opens up two different network sessions: so be aware, PPTP can cause problems when passing through a router. This is a largely why it is not used much  nowadays. It originally gained popularity because it was the first VPN protocol to be supported by Microsoft’s dial-up networking services, but few depend on dial-up to get to the Internet anymore. PPTP’s is also not overly secure.

GRE
Generic Routing Encapsulation (GRE) is a tunnelling protocol that can encapsulate many protocols inside IP tunnels. Some examples would be routing protocols such as EIGRP and OSPF and the routed protocol IPv6.

Generic Routing Encapsulation (GRE) encapsulating protocols between two IP VPN sites through an IP tunnel.

A GRE tunnel interface supports a header for each of the following:
A passenger protocol or encapsulated protocols like IP or IPv6, which is the protocol being encapsulated by GRE
GRE protocol
A Transport delivery protocol, typically IP GRE tunnels have the following characteristics:
GRE uses a protocol-type field in the GRE header so any Layer 3 protocol can be used through the tunnel.
GRE is stateless and has no flow control.
GRE offers no security.
GRE creates additional overhead for tunnelled packets—at least 24 bytes.
Source : Lammle, T (2016).CCNA Routing and Switching Complete Review Guide. Sybex.New York.

Implementing VPN using IPSec
Secure VPN connections can be implemented using the IPSec protocol. There exist many security solutions at higher protocol layers (e.g. SSL, SSH). However, IPSec is the only widely available and standardised protocol (rather: set of protocols) that operates (operate) at the network (or IP) layer. IPSec is specified by the IETF in RFC 2401.

