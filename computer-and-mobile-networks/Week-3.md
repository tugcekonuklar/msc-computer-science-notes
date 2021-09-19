#### Main Topics

* Basics of the Transport Layer and examine:
    * Layers;
    * Fibre.

* Types of connections. Particular topics include:
    * UDP;
    * Connectionless and connection orientated.
* TCP at the Transport Layer. We touch upon the following:
    * Multiplexing and demultiplexing;
    * TCP features and structure;
    * Transport primitives;
    * TCP sockets; Go-Back-N.

#### Sub titles:

* [What is the transport layer?](#what-is-the-transport-layer)

# What is the transport layer?

* In a protocol architecture, the transport protocol sits above the network layer and just below the application layer.
* The purpose of the transport layer is to provide the logical communication link between two endpoints
* There is no consideration here as to how that happens, what devices the data passes through, or how far apart the end
  points are.
* The abstract view from the applications’ perspective is that they are communicating directly with each other
* Transport layer protocols are typically the responsibility of the end devices.
* The transport layer:
    * Takes the user data from the application layer,
    * Wrapped with its relevant application layer protocol
    * Breaks down large chunks of data into packets of data referred to as ‘segments’.
    * Adds transport layer headers to each of these segments.
    * Passes these segments to the network layer.

* Each transport layer offering different implementation of
    * reliable data transfer;
    * throughput guarantees;
    * timing guarantees;
    * security.

* Focus on Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)
    * Both of them run IP layer
      </br><img src="./img/3/1.png" alt="alt text" width="500" height="300">

### Data transfer between layers

* Application layer uses socket to pass data to network layer and receive data from network layer
    * Socket acts as a doorway to the application
    * Transport layer responsibility is to direct the data to correct socket and vice versa, when data received to the
      network layer.
* Data from network comes to the transport layer, The headers are read and removed to determine the socket the data is
  to be passed to. This process is referred to as ‘**demultiplexing**’
    * that is, removing the headers and passing the data to the socket of the correct application.

* The opposide, an application packs up its data in the appropriate application protocol and passes it to the transport
  layer through its socket interface,
    * The transport layer adds headers determined by the type of service selected (TCP or UDP), and this process is
      referred to as ‘**multiplexing**’.
* Whereas the physical network transports data from host to host (endpoints), the transport layer is abstractly
  delivering data process-to-process, from the socket of one application to the socket of another.
* Each socket on a host machine has a unique identifier, and the headers in the transport level protocol, wrapped around
  the segment, enable the identification of that socket.

## Transport layer

* a programmer has little control of the transport layer. However, they are able to select between available transport
  layer protocols, which can offer different levels of service.
* Reliable Data Transfer:
    * networks suffer from packet loss, so if a protocol provides Reliable Data Transfer then it guarantees that all
      packets will arrive at the destination.
    * If a programmer selects a protocol that provides this then they simply pass their user data into the socket
      without any further concerns.
    * The socket manages the rest according to the selected protocol.
    * Some applications, such as streaming video, are more tolerant to packet loss than others, such as Word documents,
      and so can select protocols that may not provide Reliable Data Transfer.

* Throughput guarantees:
    * The volume of network traffic fluctuates, which may have an adverse effect on some types of application, such as
      live video streaming.
    * Therefore, protocols that can offer a guaranteed consistent throughput may be an advantage here.
    * These types of applications are said to be bandwidth-sensitive.
    * Other applications, such as email, can simply make use of the bandwidth that is available and are referred to as
      having an elastic requirement in terms of bandwidth.

* Timing guarantees:
    * Some applications have time-sensitive communications like the online gaming server described previously.
    * Being able to define the maximum amount of time within which a communication is sent would be useful here to
      ensure the ‘real timeliness’ of the game's interactions between users.

* Security:
    * Transport layer protocols can provide various types of protection services to the application layer, which are
      selected when designing a program that sends data over the Internet.
    * Encryption, authentication and data integrity services are examples of the types of security that can be offered
      here.

# Types of connection - UDP (connectionless)

* Process-to-process connections come in two types: **connection-orientated** and **connectionless**.
    * These terms refer to whether or not a persistent connection between the two end processes is preserved until a
      conversation is finished.

* **A connectionless protocol** does not require or enable any acknowledgments from the recipient.
  *The sender simply attaches the receiver's address and sends the data. As there is no acknowledgment, the sender has
  no guarantee it has arrived.  (UDP)

* **A connection-orientated protocol** does guarantee that the data has arrived at the receiver.
    * A connection-oriented protocol initiates the conversation via handshaking which creates a conceptual channel
      between sender and receiver.
    * The data is checked for integrity and sequence (when multiple segments are sent), and its safe arrival is
      acknowledged.  (TCP)

## UDP (connectionless)

* **User Datagram Protocol (UDP)** is a connectionless protocol that provides the bare minimum to enable sending data
  between processes.
    * The headers of a UDP segment contain
        * the source port
        * the data, as defined by the application sending
        * the destination port of the application receiving the data
    * Length and checksum are also included.
* The port numbers are what make UDP a protocol, and with these an application can connect to an individual server
  process, rather than to a host.

* The actual destination host machine address (IP address) is added at the network layer below. Given this, UDP is an
  unreliable protocol.

* 2 things are considering to select UDP
    * Is the timely arrival is important than guarantee of data arrival
    * Is the process tolerant to lost data?

* UDP is most frequently used for real time applications, where the programmer can have more control over how to respond
  to incoming/outgoing communications and manually manage lost data.
    * It enables much more flexibility but does require the programmer to consider much more carefully how an
      application needs to respond to specific situations.
    * Reliability can be programmed into the application by design.
    * In effect, UDP is really leaving the specific protocol design, the communication process between two hosts, up to
      the programmer to define.

* UDP is lightweight in terms of overhead and segment size and does not maintain any state information regarding the
  communication.
    * In this way, an application at the server end can potentially hold communications with many more clients than if
      it was using TCP.

* UDP takes messages from the application process, attaches source and destination port number fields for the multi-
  plexing/demultiplexing service, adds two other small fields, and passes the resulting segment to the network layer.
    * The network layer encapsulates the transport-layer segment into an IP datagram and then makes a best-effort
      attempt to deliver the segment to the receiving host.
    * If the segment arrives at the receiving host, UDP uses the destination port number to deliver the segment’s data
      to the correct application process.

### UDP Segment structure

* UDP packet and its data.
  </br><img src="./img/3/2.png" alt="alt text" width="500" height="300">
* One of the actions performed by the transport layer is to divide the application layer data into chunks so there is a
  fixed size to the amount of data in each UDP segment.
* UDP packets use a 16-bit internet checksum on the data but it’s rarely used and often disabled.
* UDP headers are:
    * Source port - the port number of the application that generates the data
    * Destination port - the port number of the receiving application (process-to-process protocol)
    * Length - the length of the UDP header and the UDP data, in bytes.
    * Checksum - this field is used for error checking. It is optional in IPv4 and mandatory in IPv6.

## Checksum

* [Binary numbering system documentation](./doc/BINARY%20NUMBERS%202021.docx)
* [P-Checksum](./doc/P-Checksum.pdf)
* [How to Calculate IP Header Checksum (With an Example)](https://www.thegeekstuff.com/2012/05/ip-header-checksum/)

* A check sum is basically a value that is computed from data packet to check its integrity.
* Through integrity, we mean a check on whether the data received is error free or not.
* This is because while traveling on network a data packet can become corrupt and there has to be a way at the receiving
  end to know that data is corrupted or not. This is the reason the checksum field is added to the header.
* At the source side, the checksum is calculated and set in header as a field.
    * At the destination side, the checksum is again calculated and crosschecked with the existing checksum value in
      header to see if the data packet is OK or not.
* [IP Protocol Header](https://www.thegeekstuff.com/2012/03/ip-protocol-header/)
  </br><img src="./img/3/3.png" alt="alt text" width="500" height="300">

* So, as far as the algorithm goes, IP header checksum is : **16 bit one’s complement of the one’s complement sum of all
  16 bit words in the header**
    * This means that if we divide the IP header is 16 bit words and sum each of them up and then finally do a one’s
      compliment of the sum then the value generated out of this operation would be the checksum.

### Question

* An IPv4 datagram has arrived with the following information in the header (in hexadecimal notation)
  `0x45 00 00 54 00 03 58 50 20 06 00 00 7C 4E 03 02 B4 0E 0F 02`
    * Is the packet corrupted?
    * Are there any options?
    * Is the packet fragmented?
    * What is the size of the data?
    * How many more routers can the packet travel to?
    * What is the identification number of the packet?
    * What is the type of service?

* Answer
    * VER = 0x4 = 4
    * HLEN =0x5 = 5 -> 5 * 4 = 20 bytes
    * Service =0x00 = 0 (Normal/routine)
    * Total Length = 0x0054 = 84 bytes
    * Identification = 0x0003 = 3
    * Flags and Fragmentation = 0x5850 -> D = 1, M= 0, offset = 6224
    * Time to live = 0x20 = 32
    * Protocol = 0x06 = 6
    * Checksum = 0x0000??
    * Source Address: 0x7C4E0302 = 124.78.3.2
    * Destination Address: 0xB40E0F02 = 180.14.15.2

* If we see the checksum, we get 0x0000. The packet is likely to be corrupted.
* Since the length of the header is 20 bytes, there are no options.
* Since D = 1 and M = 0 and offset = 6224, the packet is not permitted to be fragmented.
* The total length is 84. Data size is 64 bytes (84-20 = 64 bytes).
* Since the value of time to live = 32, the packet may visit up to 32 more routers.
* The identification number of the packet is 3.
* The type of service is normal.

# Encapsulation

* When a host transmits data across a network to another device, the data goes through a process called “encapsulation”
  in which it is wrapped with protocol information at each layer of the OSI model.
    * Each layer communicates only with its peer layer on the receiving device.

* To communicate and exchange information, each layer uses **Protocol Data Units (PDUs)**.
    * These hold the control information attached to the data at each layer of the model.
    * They’re usually attached to the header in front of the data field, but can also be in the trailer, or end, of it.

* At a transmitting device, the data-encapsulation method works like this:
    1. User information is converted to data for transmission on the network.
    2. Data is converted to segments, and a reliable connection is set up between the transmitting and receiving hosts.
    3. Segments are converted to packets or datagrams, and a logical address is placed in the header so each packet can
       be routed through an internet work.
    4. Packets or datagrams are converted to frames for transmission on the local network.
    5. Hardware (Ethernet) addresses are used to uniquely identify hosts on a local network segment. Frames are
       converted to bits, and a digital encoding and clocking scheme is used.

# TCP (connection)

# TODO:

* [UDP in Java](https://www.baeldung.com/udp-in-java)
* [A Simple Java UDP Server and UDP Client](https://systembash.com/a-simple-java-udp-server-and-udp-client/)
* Spend some time researching concepts such as PPP, de-encapsulation and tunnelling with regard to encapsulation
