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

* Types of devices to facilitate home access to the internet
    * **DSL** - Digital Subscriber Line – allows fast data transmission over copper telephone lines that are analogue or
      use
    * **ADSL** - Asymmetric Digital Subscriber Line - downstream is faster than upstream
    * **MODEM** - Modulator-Demodulator, uses a telephone line to create an analogue connection to a remote server.
* Types of media to transmit information between network devices
    * **TWISTED-PAIR** - insulated pairs of wires, can be shielded (STP) or unshielded (UTP), Cat5e, Cat6, Cat7.
      Traditionally used in telephone systems, where one wire carried the signal and the other grounded and absorbed
      signal interference. Network cables have four sets of wires which are paired by coloured sleeves; wires 2 and 6
      are used to send and receive data. The wires are twisted because when electromagnetic signals are conducted on
      copper wires in close proximity it causes crosstalk. Twisting the wires minimises the interference.
    * **FIBRE OPTICS** - single mode fibre (SMF) or multi-mode fibre (MMF). MMF used for shorter distances. Consists of
      thin strands of glass or plastic bound together in a sheath which transmits signals with light beams. Used for
      voice, data, or video. Expensive, great bandwidth, less susceptible to interference, thinner and lighter than
      other wires, transmits digital data. Difficult to install, expensive and harder to troubleshoot. Does not suffer
      from electrical interference.
    * **SATELLITE** - relay stations that receive signals from one earth station and rebroadcast them to another. Two
      types
        - geostationary and low earth orbiting.
    * **WIRELESS** - IEEE 802.11 WLAN standard, use access control devices such as router, devices can roam using
      signal, WiFi = Wireless Fidelity. Supports lower data rates than wired networks and can be susceptible to
      interference, e.g. weather, aircraft, microwave ovens.

* Type of devices for a core network infrastructure manage network traffic
    * **ROUTER** - Directs and forwards traffic between parts of a network. Maintains a routing table to efficiently
      direct packets from one node to another.
    * **SWITCH** - Interconnection device, reads data messages and sends to the correct port that the address is on, can
      reduce traffic on a network, has port intelligence and bandwidth allocation. Can be considered a multiport bridge.
    * **BRIDGE** - Used to connect two networks or segments together into a single aggregate network. Uses MAC
      addresses, can connect to different technologies, e.g. coaxial to Ethernet.
    * **GATEWAY** - Used to connect different, discrete, networks.
    * **HUB** - A dumb device that re-boosts signal and broadcasts from all ports. No intelligence, can amplify signals
      but shares bandwidth between all ports. Can be considered a multiport repeater.

## The Network Edge

* the computers and other devices connected to the Internet are often referred to as end systems.
    * End systems are also referred to as hosts because they host (that is, run) application programs such as a Web
      browser program
* **Hosts** are sometimes further divided into two categories: **clients** and **servers**.

### Access Networks

#### Home Access:

* Today, the two most prevalent types of broadband residential access are digital subscriber line (DSL) and cable.
* A residence typically obtains **DSL Internet access** from the same local telephone company (telco) that provides its
  wired local phone access.
    * when DSL is used, a customer’s telco is also its ISP (Internet Service Provider)
    * DSL modem uses the existing telephone line (twisted-pair copper wire)  to exchange data with a digital subscriber
      line access multiplexer (DSLAM) located in the telco’s local central office (CO).
    * The home’s DSL modem takes digital data and translates it to high- frequency tones for transmission over telephone
      wires to the CO; the analog signals from many such houses are translated back into digital format at the DSLAM.
    * On the customer side, a splitter separates the data and telephone signals arriving to the home and forwards the
      data signal to the DSL modem. On the telco side, in the CO, the DSLAM separates the data and phone signals and
      sends the data into the Internet. Hundreds or even thousands of households connect to a single DSLAM
    * The maximum rate is also limited by the distance between the home and the CO, the gauge of the twisted-pair line
      and the degree of electrical interference.
      </br><img src="./img/1/7.png" alt="alt text" width="500" height="300">

* **Cable Internet access** makes use of the cable television company’s existing cable television infrastructure.
    * A residence obtains cable Internet access from the same company that provides its cable television
    * Fiber optics connect the cable head end to neighborhood-level junctions, from which traditional coaxial cable is
      then used to reach individual houses and apartments
    * Because both fiber and coaxial cable are employed in this system, it is often referred to as hybrid fiber coax (
      HFC).
    * Cable Internet access requires special modems, called cable modems. As with a DSL modem, the cable modem is
      typically an external device and connects to the home PC through an Ethernet port
    * At the cable head end, the cable modem termination system (CMTS) serves a similar function as the DSL network’s
      DSLAM —turning the analog signal sent from the cable modems in many downstream homes back into digital format.
    * One important characteristic of cable Internet access is that it is a shared broadcast medium. In particular,
      every packet sent by the head end travels downstream on every link to every home and every packet sent by a home
      travels on the upstream channel to the head end.
        * For this reason, if several users are simultaneously downloading a video file on the downstream channel, the
          actual rate at which each user receives its video file will be significantly lower than the aggregate cable
          down- stream rate
          </br><img src="./img/1/8.png" alt="alt text" width="500" height="300">

* **Fiber to the home (FTTH)** provides much higher speed
    * As the name suggests, the FTTH concept is simple—provide an optical fiber path from the CO directly to the home.
    * The simplest optical distribution network is called direct fiber, with one fiber leaving the CO for each home.
    * More commonly, each fiber leaving the central office is actually shared by many homes; it is not until the fiber
      gets relatively close to the homes that it is split into individual customer-specific fibers.
    * There are two competing optical-distribution network architectures that perform this split- ting: active optical
      networks (AONs) and passive optical networks (PONs).
        * AON is essentially switched Ethernet,

    * PON distribution architecture. Each home has an optical network terminator (ONT), which is connected by dedicated
      optical fiber to a neighborhood splitter
        * The splitter combines a number of homes onto a single, shared optical fiber, which connects to an optical line
          terminator (OLT) in the telco’s CO.
        * The OLT, providing conversion between optical and electrical signals, connects to the Internet via a telco
          router.
        * In the home, users connect a home router (typically a wireless router) to the ONT and access the Internet via
          this home router.
        * In the PON architecture, all packets sent from OLT to the splitter are replicated at the splitter (similar to
          a cable head end).  
          </br><img src="./img/1/9.png" alt="alt text" width="500" height="300">

* **A satellite link** can be used to connect a residence to the Internet.
    * StarBand and HughesNet are two such satellite access providers

#### Ethernet and WIFI

* On corporate and university campuses, and increasingly in home settings, a local area network (LAN) is used to connect
  an end system to the edge router.
* Although there are many types of LAN technologies, Ethernet is by far the most prevalent access technology in
  corporate, university, and home networks.
* Ethernet users use twisted-pair copper wire to connect to an Ethernet switch,
* The Ethernet switch, or a network of such interconnected switches, is then in turn connected into the larger Internet.
  </br><img src="./img/1/10.png" alt="alt text" width="500" height="300">

* In a wireless LAN setting, wireless users transmit/receive packets to/from an access point that is connected into the
  enterprise’s network (most likely using wired Ethernet), which in turn is connected to the wired Internet.
* A wireless LAN user must typically be within a few tens of meters of the access point.
* Wireless LAN access based on IEEE 802.11 technology, more colloquially known as WiFi
* a cable modem, providing broadband access to the Internet; and a router, which interconnects the base station and the
  stationary PC with the cable modem.   
  </br><img src="./img/1/11.png" alt="alt text" width="500" height="300">

#### 3G and LTE

* Telecommunications companies have made enormous investments in so-called third-generation (3G) wireless, which
  provides packet-switched wide-area wire- less Internet access at speeds in excess of 1 Mbps.
    * But even higher-speed wide-area access technologies—a fourth-generation (4G) of wide-area wireless networks—are
      already being deployed.
    * LTE (for “Long-Term Evolution”) has its roots in 3G technology, and can achieve rates in excess of 10 Mbps.

### Physical Media

* when traveling from source to destination, passes through a series of transmitter-receiver pairs.
    * For each transmitter- receiver pair, the bit is sent by propagating electromagnetic waves or optical pulses across
      a **physical medium**.
        * Examples of physical media include twisted-pair copper wire, coaxial cable, multi mode fiber-optic cable,
          terrestrial radio spectrum, and satellite radio spectrum.
    * Physical media fall into two categories: guided media and unguided media.
        * Guided media, the waves are guided along a solid medium, such as a fiber-optic cable, a twisted-pair cop- per
          wire, or a coaxial cable.
        * Unguided media, the waves propagate in the atmosphere and in outer space, such as in a wireless LAN or a
          digital satellite channel.

* Twisted-Pair Copper Wire
    * The least expensive and most commonly used guided transmission medium is twisted- pair copper wire.
    * Twisted pair consists of two insulated copper wires, each about 1 mm thick, arranged in a regular spiral pattern
    * The wires are twisted together to reduce the electrical inter- ference from similar pairs close by
    * Typically, a number of pairs are bundled together in a cable by wrapping the pairs in a protective shield
    * Unshielded twisted pair (UTP) is commonly used for computer networks within a building, that is, for LANs.

* Coaxial Cable
    * Like twisted pair, coaxial cable consists of two copper conductors, but the two conductors are concentric rather
      than parallel
    * With this construction and special insulation and shielding, coaxial cable can achieve high data transmission
      rates.
    * Coaxial cable is quite common in cable television systems.
    * Coaxial cable can be used as a guided shared medium

* Fiber Optics
    * An optical fiber is a thin, flexible medium that conducts pulses of light, with each pulse representing a bit.
    * A single optical fiber can support tremendous bit rates, up to tens or even hundreds of gigabits per second.
    * They are immune to electromagnetic interference, have very low signal attenuation up to 100 kilometers, and are
      very hard to tap.
    * These characteristics have made fiber optics the preferred long-haul guided transmission media, particularly for
      overseas links

* Terrestrial Radio Channels
    * Radio channels carry signals in the electromagnetic spectrum.
    * They are an attractive medium because they require no physical wire to be installed, can penetrate walls, provide
      connectivity to a mobile user, and can potentially carry a signal for long distances
    * Terrestrial radio channels can be broadly classified into three groups:
        * operate over very short distance (e.g., with one or two meters);
        * operate in local areas, typically spanning from ten to a few hundred meters;
        * operate in the wide area, spanning tens of kilometers.

* Satellite Radio Channels
    * A communication satellite links two or more Earth-based microwave transmitter/ receivers, known as ground
      stations.
    * Two types of satellites are used in communications: geostationary satellites and low-earth orbiting (LEO)
      satellites
        * Geostationary satellites permanently remain above the same spot on Earth. This stationary presence is achieved
          by placing the satellite in orbit at 36,000 kilometers above Earth’s surface.
        * LEO satellites are placed much closer to Earth and do not remain permanently above one spot on Earth. They
          rotate around Earth (just as the Moon does) and may communicate with each other, as well as with ground
          stations.

# Protocol

* Communication between devices on a network is organised and made consistent by protocols. A protocol is an agreed set
  of actions in response to given situations.
* In computing, protocols are there to ensure that data transfer can happen regardless of the transmission media or the
  connected devices.
    * It can be thought of as ensuring that all networked devices (at the core or on the edge) speak the same language
      and consistent responses are given to specific requests.
* Protocols the rules that govern a communication between devices and rules can vary depending on protocol.
    * They’re necessary, because if you didn't have protocols in place, different equipment would try and transmit
      different types of data, different shapes of data.
    * So something needs to coexist so that everything can communicate in the same format.

* A group of protocols together is a **“protocol suite”** and they vary at the different layers of the OSI and the
  TCP/IP model,
* Communications are governed by protocols.
* Message Encoding
    * Encoding is the process of converting information into another acceptable form for transmission.
    * Decoding reverses this process to interpret the information
    * A piece of data goes to be transmitted across the network and it gets changed for a human format into the
      electrical signals.
      </br><img src="./img/1/12.png" alt="alt text" width="500" height="300">

* The Rules:
    * Message encoding
    * Messaging format and encapsulation
    * Message size
    * Message Timing
    * Message Delivery Options

* Message Delivery Options:
    * Unicast - one to one
    * Multicast - one to multi
    * Broadcast - one to all

</br><img src="./img/1/13.png" alt="alt text" width="500" height="300">

* The Internet protocol (IP) suite, which is used for transmitting data over the Internet, contains dozens of protocols.
    * Link layer - PPP, DSL, Wi-Fi;
        * Link layer protocols establish communication between devices at a hardware level. In order to transmit data
          from one device to another, each device's hardware must support the same link layer protocol
    * Internet layer - IPv4, IPv6;
        * Internet layer protocols are used to initiate data transfers and route them over the Internet
    * Transport layer - TCP, UDP;
        * Transport layer protocols define how packets are sent, received, and confirmed.
    * Application layer - HTTP, IMAP, FTP.
        * Application layer protocols contain commands for specific applications.
    </br><img src="./img/1/15.png" alt="alt text" width="500" height="300">

# Network models

* Open Systems Interconnection model (OSI model) was published as a conceptual model for network protocols and
  communications by ISO (International Standards Organisation).

* TCP/IP conceptial layers
  </br><img src="./img/1/14.png" alt="alt text" width="500" height="300">
