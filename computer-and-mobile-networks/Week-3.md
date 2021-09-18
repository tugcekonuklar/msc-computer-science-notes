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
    



    