#### Main Topics

* Explain and demonstrate the fundamental concepts and components used to describe networks.
* Compare the theoretical ISO/OSI network stack with the TCP/IP implementation.
* Discuss the benefits and limitations of packet switching over circuit switching.

#### Sub titles:

* [Network Components](#network-components)

# Network components

* This will be about protocols that allows to communication across various medium.
* **Open System Interchange model (OSI Model)**, which is a reference (theoritical model) for all rules that apply for
  every device and every piece of software has in place to communicate.
* We have 7 layers
    * At the top layer 7, is very much nearer to the human being
    * Layer 1 is showing electricity across cables or wireless devices.

* **MAC address** - that's Media Access Control.
    * MAC address is something that's hardwired into your device by the manufacture
    * Can not be cloned and it is unique.
        * The only time you can sort of clone them is when you do a virtual network and you have to spoof MAC addresses

* **Bridge** used to be a quite clunky hardware device that allowed two sections of a sub-network to talk to each other.
  And we don't really use them anymore because they've been replaced by switches.

* **Routers**: router sits quite high up in the stack and it's got lots of intelligence, it’s got lots of tasks
    * Uses IP Addresses
    * Broadcast the LAN segment only
    * Decides which routers to send data
    * Other roles: DHCP, DNS, Firewall, IP Leasing,
    * Can use MAC addresses
    * Can repeat the signal - backward capability

<img src="./img/1/2.png" alt="alt text" width="500" height="300">

* Layer 1 is the physical layer, so it's just about some copper inside some cable, shoving electrical pulses down.
    * there's no intelligence, it just repeats and re-amplifies, or doesn't send the signal on as it goes,
    * the higher up the stack you go, the nearer to the human you go.

* OSI vs TCP Model:

<img src="./img/1/3.png" alt="alt text" width="500" height="300">

* Diagram of two computers, one labelled “Source” and the other “Destination”, with a Link-layer switch and router in
  the middle

<img src="./img/1/4.png" alt="alt text" width="500" height="300">

## Network Design

* At the basic level network consist 2 design
    * Physical
    * Logical

* The **Physical design** consist of all the physical devices and technology that communicate and can include:
    * The layout of devices and connections called Topology
        * Most commons: star, peer-to-peer, extended star, bus and mesh
    * End devices form the interface between the human and the network
        * these can include clients (nodes, PC’s etc) servers, file stores, printers etc
    * Intermediary devices that provide connectivity
        * switch, hub, router etc
    * Network media - the channel over which a message or data travels
        * ethernet, wireless, fibre etc

<img src="./img/1/5.png" alt="alt text" width="500" height="300">

* Cisco icons are widely used and recognised in documentation

<img src="./img/1/6.png" alt="alt text" width="500" height="300">

* The **logical design** is the configuration of the devices, the IP addressing scheme, the bandwidth and the protocols
* The logical design is not technology dependent and can include:
    * Protocols – set of rules to guide a communication
    * TCP and OSI models – layer models
    * IP addressing
    * Network addressing
    * Routing

## The Network Edge

* the computers and other devices connected to the Internet are often referred to as end systems.
    * End systems are also referred to as hosts because they host (that is, run) appli- cation programs such as a Web
      browser program
* **Hosts** are sometimes further divided into two categories: **clients** and **servers**.
* 

  