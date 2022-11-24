## MSC Algorithm and Data Structure Lesson Notes

This module is for MSC Algorithm and Data Structure lesson notes.

TBC

## Overview

* [Week 1](#week-1): hardware fundamentals which is a complete model of computer architecture in terms of hardware and
  operating system.
* [Week 2](#week-2): Computer memory with focusing types of memories, capabilities and performance
* [Week 3](#week-3): Component of systems and how they work together to make up a complete system - Building the system
    - busses and components
* [Week 4](#week-4) and [Week 5](#week-1): Exploring the nature of computer systems with the investigation of the
  operating systems, how they manage workload and maximise efficiency and their role on memory and storage management.
* [Week 6](#week-5): Basic principle of computer network from hardware and operating system perspective
* [Week 7](#week-6): Review of security and resilience issues of computer systems.

# WEEK 1

* [Fundamentals](#fundamentals)
    * [John von Neumann Model](#john-von-neumann-model)
        * [John von Neumann Model Bottleneck](#john-von-neumann-model-bottleneck)
    * [Clock signals](#clock-signals)
    * [Software view point](#software-view-point)
    * [Electronics](#electronics)
        * [Speed versus complexity](#speed-versus-complexity)
* [Processors: the heart of the machine.](#processors-the-heart-of-the-machine)
    * [Heat and power constraints](#heat-and-power-constraints)
    * [CPU architecture](#cpu-architecture)
    * [Beating the performance barrier](#beating-the-performance-barrier)
    * [Processor frequency](#processor-frequency)
        * [Scalar execution model](#scalar-execution-model)
        * [Pipelining](#pipelining)
        * [Superscalar execution model](#superscalar-execution-model)
        * [Data flow analysis](#data-flow-analysis)
        * [Branch Prediction](#branch-prediction)
        * [Speculative execution](#speculative-execution)
    * [Performance Balance](#performance-balance)
    * [Instruction micro-sequencing](#instruction-micro-sequencing)
    * [Introduction to Pipelining](#introduction-to-pipelining)
* [Terminology of Instructions](#terminology-of-instructions)
* [Computers Everywhere](#computers-everywhere)
    * [General purpose computers](#general-purpose-computers)
    * [Embedded Systems](#embedded-systems)
    * [Mainframes and supercomputers](#mainframes-and-supercomputers)
    * [Ambdal's Law](#ambdals-law)

# Fundamentals

* **Power**: Electrical power consumed by computer component or system often measured in Watt(W), milliWat(mW)(1x10^-3),
  microWat(
  uW)(1x10^-6) and nanoWat(nW)(1x10^-9)
* **Frequency**: how often given activities happen in any one second.
    * In computer system it refers to a basic operating cycle called a clock cycle.
    * The basic measure of frequency is Hertz(Hz).
    * Most computer works in high frequencies thats why MegaHertz(MHz) or Gigahertz(GHz) are using as normal units of
      measurement for computer.
* **Clock** : is a repetitive signal which alternates between binary zero and one, and provides a synchronising
  capability
  for system components.
* **Clock Cycle**: The frequency of activities is typically regulated by a **clock signal** and this repeative pulse
  dictates each event cycle and operates of frequency of event.
* **Data Capacity**: The number of data items a device or system can manage or store.
    * Data capacity is large multiples of bytes and bits that's why binary measurement units are using.
* **Data Rate**: The quantity of data can be transfer one point to another in a given amount of time mostly one second.
    * For example 100 milion bytes per second = 95.3 binary Megabytes/sec
* A bit is single binary value
    * 1 byte = 8 bit
    * 1 kilobyte(KB) = 1024 byte
    * 1 megabyte(MB) = 1024 KB
    * 1 gigabyte(GB) = 1024 MB
    * 1 terrabyte(TB) = 1024 GB
* MB to denote megabytes, and Mb to denote megabits.
* since the standard scientific units of kilo, mega, giga, etc are more generally based upon decimal powers 10^3, 10^6,
  10^9, etc. However, the binary version of these units correspond to 2^10, 2^20, 2^30 giving slightly different values.
    * A binary megabyte for example is 1,048,576 bytes, and a million bytes is 95.3 binary Megabytes^!.

* General purpose Computers: They are design to perform adequately across a wide range of uses, but they are rarely
  optimal in any of those cases.
* Application Specific Computers: They are designed to be highly efficient on a defined task to be achieve a high
  performance on the task. This computers are the cost effective versions of the general computers.
* A very simple computer system, as a first-order model, might be presented 2.3 Block diagram

## John von Neumann Model

* This is a key concept of the computer architecture proposed by John von Neumann 1945
* Most frequently used model for computer systems ever since.
* CPU, Memory andIO devices, those are the three essential components in Neumann architecture.
* A **bus** is a collection of wires that provide data and control signals and possibly addresses.
  Multiple devices are connected to a bus and can communicate with other devices via this connection.
    * Busses allow many devices to share one communication route for Information. However, it is important to note
      that only one device can control the bus at atime (the bus master).
* A **CPU** - Central Processing Unit is a digital electronic circuit built from many transistors. It can hold a small
  amount of temporary data and perform mathematical operations upon them. A CPU can also sequence operations according
  to a program it reads from memory, step by step.
    * it means :  a CPU performs a sequence of (often mathematical) operations upon temporary data it holds, and this
      sequence is dictated by a program found in memory.
    * this component better as the Processor,this is the component that does most of the hard work – the computations,
      the data translations and executes the program code in your computer when its running programs.
    * In the simplest computer system, all devices connect to a system bus, the CPU is always the bus master, and all
      devices appear as if they are part of the visible memory of the computer system. This allows for very
      straightforward programming models to access devices and modules within the system, though not necessarily
      the most optimal performance.
    * Extended definition of CPU:
        * A CPU is a digital electronic circuit, manufactured from a silicon technology defined as being at one
          particular technology node, consuming a certain amount of power, and generating a certain amount of heat
          during its operation
        * A CPU fetches program instructions from memory using a concept known as the **fetch-execute cycle**,
          and as each instruction is fetched, it is executed, performing one of a number of possible operations upon
          data held within the CPU registers.
        * These operations include mathematical and logical operations, and operations that change the flow of the
          program to execute parts chosen by the result of testing conditions encountered
          during a program sequence.
* Memory System and this is where data items can be stored as numerical values and this is where instruction code from
  the processor can be stored, also as numerical values.
* IO ( Input, Output ) interface is essentially mechanisms that allow devices to plug into the computer.
    * for example, a keyboard is an input device, and a video screen is an output device

</br><img src="./img/1.png" alt="alt text" width="500" height="300">

### John von Neumann Model Bottleneck

* Having a single bus creates the problem that's known as the von Neumann/Princeton bottleneck that limits the number of
  devices that can use the bus at a given time to 2. Other devices have to wait and this leads to running the jobs in
  serial and costs time.
* If a CPU wishes to fetch data from memory, it cannot also fetch an instruction from memory at the same time.
* Likewise, if an IO device was capable of accessing memory directly then it would similarly be prevented from doing so
  whenever the CPU was already accessing memory. This constraint, due to many devices wanting to use one shared bus, is
  known as the von Neumann bottleneck.
* There are some alternatives to prevent this problem:
    * Harvard Architecture addresses this by utilising 2 different busses, one for the program memory and one for the
      data memory & IO. So, fetch and decode/execute can happen in parallel, ie pipelined. This permits instructions and
      data to be accessed simultaneously, permitting a speed gain.
    * Another potential solution is using an on-chip cache which reduces the CPU's access to code and data memory and
      frees up the bus for other peripherals.

## Clock signals

* In computer systems binary signals have two states, these are usually represented
  by voltages so something near to zero volts would be a zero in binary and a signal which has a higher value,
  typically 1.8 volts or 3.3 volts, would represent a logic “1” so a clock signal is actually just a
  signal whose voltage turns on and off repeatedly over a period of time.
* Over a period of time that a number of clock signals can be fitted into a period, so we’d
  expect that a clock signal turns on, turns off again and that will repeat and that will repeat
  , and that would repeat again and this repetitive behaviour is what a **clock signal**
  essentially does.
  </br><img src="./img/2.png" alt="alt text" width="500" height="300">
* Clock cycle is showing with blue line.
* That is the basic definition of a **clock** – a rising edge (zero to one) and a falling edge (one to zero) – and these
  edges are what we
  use to synchronise events in the clock signal regime in a computer system.
* It turns out that one of those on-off transitions is what we refer to as one clock cycle,
* so when we talk about a clock cycle we’re talking about a complete process of going from zero to one and then back to
  zero again before it repeats.
  </br><img src="./img/3.png" alt="alt text" width="500" height="300">
* we can also define that clock cycle in terms of a clock period, so this takes a certain amount of time, so there’s an
  amount of time “t”, typically in milliseconds or microseconds or nanoseconds in a clock system, and that value t
  represents a period of time - the clock period.
* If t was 0.01 seconds, which is 10 milliseconds, then f, by virtue of the formula we have just discussed, would be 1
  divided by 0.01, which equals 100 Hertz.
    * be referred to as “cycles per second”

## Software view point

* software is a series of instructions relating to a complex set of actions to be performed by a digital circuit (the
  CPU) and rather than manipulating threads of cotton, we manipulate data values.
* we can divide software into **source code**, which is in some way intelligible to a human, and **machine code**, which
  is
  nothing more than a series of binary numbers, and rarely understood by visual inspection by a programmer.
* In modern computing, there are 2 **high-level languages, HLL**
    * **Compiled** where the source code is compiled by a compiler that automatically converts high-level statements
      into low-level machine code.
    * **Interpreted** approach, translates source code written a high-level language interactively and executes a
      pre-defined piece of low-level code for each statement.
    * Writing the code directly in the **assembly** language, is the 3rd option, where the textual representation of
      each instruction is used.

## Electronics

* **Transistors**: Invented in the late 1950's, a transistor is a kind of switch,at least as far as digital electronics
  is
  concerned ,and when properly used they can operate in a binary signalling regime
  (on and off, one and zero).
* **Transistor Operation**: A simplified description of transistor behaviour in switching mode might be as follows:
  Atypical transistor uses a control signal (the Gate) to control the flow of a signal from the input (the Source) to
  the output (the
  Drain). However, multiple transistors can be combined to create logical switching functions.
* **Logical Operation**: Imagine that our Gate control signal can switch from zero to one, and by combining two
  transistors
  in the right way, we can create a switching arrangement that produces corresponding outputs one and zero. That is to
  say, the
  output is the opposite of the input. This is known as an inverter, or a logical NOT operation: the simplest logic
  gate.
  The output is NOT the input, if you wish to think of it in those terms.
* **AND and OR**: We can also combine transistors in such away that they create gates with two inputs. Then the circuit
  can
  be arranged such that a signal output can only be binary one when both inputs are one (the AND gate function, where
  input-a AND input-b must both be one at the same time to generate an output of one)
  .Likewise,as lightly different arrangement causes the circuit to generate a one If either input is one (generates one
  if input-a OR input-b are one), creating an OR gate.

* The behaviour of three very simple logic functions with the definitions of **AND, OR,** and **NOT**.
* These circuits are referred to as **logic gates**. So we typically talk about the **AND gate, the OR gate, and the NOT
  gate** (or Just an inverter). A further gate, the **XOR gate** performs an exclusive or function, where an output is
  one only when anyone (but not both) inputs are one.
* truth tables:
  </br><img src="./img/4.png" alt="alt text" width="500" height="300">
* Mixtures of these eight logic (AND, OR, NOT, XOP, NAND, NOR, NEXOR(XNOR), buffer) gates can also be combined into more
  complex circuits, including circuits that add binary bits together (arithmetic), or perform other mathematical
  operations such as multiplying, comparing, and so on. These circuits are called **combinational circuits**.

### Speed versus complexity

* All of these logic gates and logic circuits **consume power** and **generate heat**
* Making the clock signal faster, makes the system operate faster. However, as the circuit gets more complex, each layer
  introduces an additional delay and the clock cannot go faster than the circuit can handle. This is known as the
  **speed vs complexity** dilemma.
* To overcome this, multicore CPUs came to life. Instead of trying to push the CPU to get faster and faster, multiple
  CPU are arranged in parallel. This way, complexity still increases but the operations are allowed to happen in
  parallel.
  </br><img src="./img/5.png" alt="alt text" width="500" height="300">
* Circuit (b) is more complex, and slower, than circuit (a). Intuitively you might also expect circuit (c) to have
  increased delay compared to (b). After all, circuit (c) is certainly more complex than circuit (b). Whilst it
  is true that increased complexity often, even typically, causes increased delay, it is sometimes possible to have more
  gates but not slow down the circuitry. Indeed, in circuit (c) what we have done is use parallelism, because there are
  actually two separate circuits operating side by side. This is a key principle underlying the idea of multicore
  processor
* The industry transition from the Complex Instruction Set Computers (CISC) to the Reduced Instruction Set Computers (
  RISC), reduced ISC, mentality. This helps because CISC had a lot of instructions that were rarely and ineffectively
  used. However, CISC processors still find applications in areas where specialised instructions are required to carry
  out hardware-accelerated jobs, ie image processing.

# Processors: the heart of the machine.

* Since the mid 1970's, the vast majority of computer systems have been built around a key component: the single-chip
  microprocessor.
* Prior to this time, computer systems were almost always built from a large number of discrete components.
* These were often individual transistors in small metal canisters, or very simple digital logic components implemented
  individually as very simple logic chips also known **integrated circuits.**
* But even further back, computer circuits were built from radio valves filling hundreds of racks, and a multitude of
  cabinets.

## Heat and power constraints

* Every time a transistor switches on or off, it consumes some power, known as **dynamic power**.
* The faster the on-off transitions occur, the more power is consumed.
* And what happens to all of this power? when a circuit consumes
  energy,one of the unwanted by-products is **heat**.
* Incidentally, silicon chips also consume power when the transistors are idle, like a car motor ticking over whilst
  waiting at a road junction. This is known as **static power**.
* As Moore's Lawl has predicted successfully for many decades, the number of transistors on a given chip area doubles
  every two years.
* In 20 years, the size required to fit a transistor dropped from 1um to 10nm.
    * This dimension is known as the feature size.
    * Each incremental advance in silicon technology is called the technology node.
* Although transistors get smaller and smaller, designers want to use more and more transistors per chip, and those
  transistors operate faster too. The complexity of processors is thus an ever-increasing feature of computing.
* Where we have smaller circuits consuming more power and thus generating more heat we can say that **power density**
  and then **thermal density** increases. This is recognised as a serious problem. This is why a modern processor system
  is
  often cooled by a large heat¬sink. a module designed to draw heat away from the processor so that it does not
  overheat.

## CPU architecture

* **instructions** are different computational operations performing by CPU
* Some characteristics of instructions
    * Data Is held in temporary storage components within the CPU, called **registers**. Instructions operate upon these
      register contents.
    * Many operations are directly mathematical: add, subtract, multiply, divide, and so on.
    * Some of these instructions operate only on integers (whole numbers) whilst other operations may be able to act
      upon floating
      point or fixed point numbers. Not all processors support both kinds of computation.
    * Some instructions are logical operations. These perform boolean **logic operations** on data.
    * Some instructions transfer data to and from memory. These are known as **Load/Store operations**.
    * Some instructions test conditions and choose which part of the program to execute next.
* Execution means: A program consists of a number of instructions, and a CPU executes (performs) each instruction in
  turn.
* In order to execute an instruction, the CPU must first **fetch** it from memory, where our program is usually stored.
    * Fetching an instruction, and then executing it, is known as the **fetch-execute cycle**.
* **linear program sequence**: execution of CPU one instruction after another in a continuous list,
* **Program-flow instructions**: Some Instructions test conditions and choose what part of the program to execute next'.
    * The flow of a fetch-execute cycle sequence, as it moves through memory, is generally **non-linear** (more
      accurately it is linear for short sequences), interspersed with a number of Jumps to other parts of the memory
      where the next short linear sequence is located.
    * Program-flow instructions are therefore frequently encountered.
*

## Beating the performance barrier

* Performance is the achievement of certain goals whilst consuming certain resources.
    * Another way to express this is cost versus benefit or cost-benefit.
    * We sometimes refer to this as a performance metric.
* **mips** is simply millions of instructions per second,a simplistic measure of the computational throughput a
  processor Is capable of.
* **peak mips**, which measures the maximum possible mips a processor can achieve under the best possible conditions
* Example for cost measurements:
    * A given CPU can execute one million instructions per second(**mips**) (meaning it has a throughput of one mips)
    * The CPU may well require 1 milliwatt of power to do this.
    * Assume that one watt of electricity costs 1/lOth cent,
    * Assume the CPU costs $100, and is used for 1yr continuously.
    * The CPU dimensions are 20x20x5mm
* Answer:
  _* Cost efficiency for power is calculated by figuring out the mips/W
    * to calculate the cost of running the CPU for a given duration
    * Find the duration in seconds
    * Multiply the duration with the power consumption in 1 second
    * Then multiply by the unit cost of electricity and convert the units to W, Dollars etc.
    * Finally, add the cost of owning the CPU._
        * This CPU performs 1 mips per milliwatt (because we use 1mw of power and get 1mips in return), or 1000 mips per
          watt, if you prefer.
        * One year equates to **365x24x60x60 =31,536,000** seconds,
        * and each second we consume 1 milliwatt at 1mips, requiring **31,536 watts (31 Kw)**.
        * At 0.1 cent per watt, this electricity will cost **31.54** dollars.
        * And 100 dolar CPU price plus makes this CPU for one year is **131.54 dollars**.

* This calculation is important to predict **cost-effectiveness** of a CPU
* Another Example :
    * </br><img src="./img/6.png" alt="alt text" width="500" height="300">
    * Which CPU can do the most processing in one hour?
        * highest mips per second is also makes highest per an hour. CPU-D 8 mips/1 mW = 8000 mips per watt.
    * Which CPU is most cost-efficient for power consumed?
        * _Performance per Dollar: Purchase price / mips_
        * CPU-C the best dollar for mips => $80/5= $16
    * Which CPU gives the most performance per dollar?
        * CPU-C 105$ per year
    * Which CPU is cheapest to buy and run for one year at 1mips? ▶Which CPU has the worst (highest) power density
        * _Power density is calculated as Power/Volume, ie W/mm3, bigger the worse._
        * CPU-A 6uW/mm^3
* To compare CPUs there are some test programs to run same workload for each CPU in run called **benchmarks**

## Processor frequency

* **clock frequency** is measurement how fast a processor can perform a key internal circut operation
    * We measure clock per second or Hertz
* The same identical operation on another processor mig require more or less or same number of clock cycles thats why
  clock frequency isnot guarantee highed mips or benchmark score by itself.
* For this we use **clock per instruction (CPI)**
* </br><img src="./img/6.png" alt="alt text" width="500" height="300">
* in this example better Z>X>Y

### Scalar execution model

* When a CPU can execute one instruction at a time
* Execution of instructions is serial. Instruction needs to finish before the next begin.

### Pipelining

* The execution of an instruction involves multiple stages of operation, including fetching the instruction, decoding
  the opcode, fetching operands, performing a calculation, and so on.
* Pipelining enables a processor to work simultaneously on multiple instructions by performing a different phase for
  each of the multiple instructions at the
  same time.
* The processor overlaps operations by moving data or instructions into a conceptual pipe with all stages
  of the pipe processing simultaneously.
* For example, while one instruction is being executed, the computer is decoding the next instruction. This is the same
  principle as seen in an assembly line.
* Instructions do not always need complicated before the next one begin, we called this concept as **overlapped
  instruction execution**
* Pipelining allows to run more instruction in fewer clock cycle, meaning inherent CPI decreases, brings better
  performance
* This kind of operations is only possible where the 2 instructions do not depend upon one on each other
* The next instruction clearly can not use the result of the previous unless its waits for the preceding instruction to
  finish.
* This potential dependency known **pipeline hazard** or **data hazard**
* With care and using concept known **data-flow analysis**, code can be written avoid many of this problems.

### Superscalar execution model

* Multiple instructions can start at the same time this called multiple issue,
    * This is the ability to issue more than one instruction in every processor clock cycle.
* This is the base of the super scalar execution model
* In effect, multiple parallel pipelines are used.

### Data flow analysis

* The processor analyzes which instructions are dependent on each other’s results, or data, to create an optimized
  schedule of instructions.
* In fact, instructions are scheduled to be executed when ready, independent of the original program order. This
  prevents unnecessary delay.

### Branch Prediction

* The processor looks ahead in the instruction code fetched from memory and predicts which branches, or groups of
  instructions, are likely to be processed next.
* If the processor guesses right most of the time, it can prefetch the correct instructions and buffer them so that the
  processor is kept busy.
* The more sophisticated examples of this strategy predict not just the next branch but multiple branches ahead.
* Thus, branch prediction potentially increases the amount of work available for the processor to execute.
* Branch means also jump in computer architecture
* Static branch prediction
    * In static prediction, all decisions are made at compile-time.
    * Some static predictors always assume that the jump won't happen and some others assume that the backward jump will
      occur, which optimizes the loop operations.
    * Branch delay slots are used to run independent instructions. So, if the branch is taken, the execute cycle is used
      to execute these independent operations.
* Dynamic branch prediction
    * This basically is an educated guess based on the branch history kept by the CPU.
    * When the dynamic branch predictor hasn't got enough data to use, it can fall back to the static prediction.
* Hit Rate:
    * </br><img src="./img/8.png" alt="alt text" width="500" height="300">

### Speculative execution

* Using branch prediction and data flow analysis, some processors speculatively execute instructions ahead of their
  actual appearance in the program execution, holding the results in temporary locations.
* This enables the processor to keep its execution engines as busy as possible by executing instructions that are likely
  to be needed.

## Performance Balance

* performance balance: an adjustment/tuning of the organization and architecture to compensate for the mismatch among
  the capabilities of the various components.
    * Designers constantly strive to balance the throughput and processing demands of the processor components, main
      memory, I/O devices, and the interconnection structures.
* The problem created by such mismatches is particularly critical at the inter- face between processor and main memory.
  While processor speed has grown rapidly, the speed with which data can be transferred between main memory and the
  processor has lagged badly.
* The interface between processor and main memory is the most crucial pathway in the entire
  computer because it is responsible for carrying a constant flow of program instructions and data between memory
  chips and the processor.
* The interface between the processor and main memory is the most crucial pathway in the entire computer because it is
  responsible for carrying a constant flow of program instructions and data between the memory and the processor.
* To improve performance
    * Increase the memory bus width
    * Incorporate cache on the dynamic random-access memory (DRAM)
    * Use close-to-the-processor caches
    * Increase the memory bus frequency and use a hierarchy of busses and caches
* Another bottleneck is the increasing I/O demands.
    * Strategies here include caching and buffering schemes plus the use of higher-speed interconnection buses and more
      elaborate structures of buses.

## Instruction micro-sequencing

* The internal organisation of the CPU is called the microarchitecture.
    * **Registers** hold numbers of certain size, ie 8, 16, 32 etc bits.
    * **Program Counter**, PC, keeps track of the next instruction in the memory so it can be fetched.
    * The **arithmetic Logic unit (ALU)** does arithmetic or logical operations on data held in registers
* When one instruction is executed at a time, this is known as the scalar execution and it's broken into
  micro-instructions such as Fetch, Decode, Read, Execute, Write.
    * When an instruction is going through different stages of its lifecycle, it's referred to as the instruction being
      in flight.
* Micro-sequencing is what happens inside a microprocessor when it is executing an instruction
* So an instruction does not execute in a single clock cycle as an atomic operation,
  a single indivisible operation, its actually executed internally as a number of steps in a micro
  sequence.
* </br><img src="./img/9.png" alt="alt text" width="500" height="300">
* Memory read operation resulting from memory a data-fetch (reads data value) or instruction-fetch (reads instructions)
* </br><img src="./img/10.png" alt="alt text" width="500" height="300">

## Introduction to Pipelining

* With pipelining, a processor can simultaneously work on multiple instructions. In other words, the execution of
  multiple instructions are overlapped.
* The 1st optimisation is, back to back register read/writes can be combined into a single clock cycle.
    * Making 2 parallel reads requires 2 read ports for the Register File and as read and write ports are different,
      register R/W can happen in parallel anyway. Such a register file would have 2+1=3 ports.
    * See how RegisterRead 2 and 3 are combined into a single cycle in the image below.
* Then, as soon as the 1st instruction is fetched, the memory/address bus is available, so, the 2nd instruction can be
  fetched
* As one instruction is completing per clock cycle, marked by the RW operations, the CPI is 1.
    * Although different from pipelining, superscalar architectures allow starting more than 1 instruction on the same
      core, multiple issue.
    * While there is not a universal agreement on the definition, superscalar design techniques typically include
      parallel instruction decoding, parallel register renaming, speculative execution, and out-of-order execution.
    * These techniques are typically employed along with complementing design techniques such as pipelining, caching,
      branch prediction, and multi-core in modern microprocessor designs.
* There is an issue called 'register hazard'. For example when we have ADD R2,R3,R6 and SUB R6,5,R6 and if they are
  pipelined SUB reads an earlier value of R6 before ADD completes and updates R6.
    * More generically, when two instructions depend on each other, this leads to pipeline or data hazard.
    * </br><img src="./img/11.png" alt="alt text" width="500" height="300">
* There are 2 ways to solve:
* inserting delay slots automatically when the hazard is detected by the CPU
    * we are introducing delays and you will notice that now the number of
      instruction completions is now taking fewer instruction completions over more cycles, so the
      CPI is dropping here. So this is not the most efficient solution.
    * </br><img src="./img/12.png" alt="alt text" width="500" height="300">
* Another and more efficient option is Static Instruction Scheduling, where the compiler re-orders the instructions and
  moves the instructions that aren't dependent on the target register in between.
    * </br><img src="./img/13.png" alt="alt text" width="500" height="300">

## Terminology of Instructions

</br><img src="./img/14.png" alt="alt text" width="500" height="300">
</br><img src="./img/15.png" alt="alt text" width="500" height="300">

* </br><img src="./img/18.png" alt="alt text" width="500" height="300">
    * </br><img src="./img/19.png" alt="alt text" width="500" height="300">

* </br><img src="./img/16.png" alt="alt text" width="500" height="300">
    * </br><img src="./img/17.png" alt="alt text" width="500" height="300">

* </br><img src="./img/20.png" alt="alt text" width="500" height="300">
    * </br><img src="./img/21.png" alt="alt text" width="500" height="300">

* Write a program to compute the following: 9 x (9+3)

``` 
LDI R1,9
LDI R2,3
ADD R1,R2,R3
MUL R1,R3,R1
HALT
```

* Write a program to compute the following:(3x5) - (6 x 4)

```
LDI R1,3
LDI R2,5
MUL R1,R2,R3
LDI R1,6
LDI R2,4
MUL R1,R2,R4
SUB R4,R3, R1
HALT
```

# Computers Everywhere

* At the simplest level of abstraction, computer systems can therefore be divided loosely into two groups. The
  **general-purpose machines** and those **application-specific**.

## General purpose computers

* As computers became more sophisticated and powerful, their uses expanded to many more tasks.
* At this point, many computers began to be designed with the general market in mind: one machine that can do many
  things for many customers was more cost-effective to mass-produce and sell.
* But, at the same time, these general-purpose computer systems became less efficient at very specific tasks. There is a
  saying 'Jack of all trades, and master of none.
* it is not just desktops and laptops that are general purpose computers. In recent years,smartphones and tablet
  computers have become widely popular and powerful enough to be used in similar ways; these are also general purpose
  computers.
* Application-specific systems that are engineered to the last detail to be highly efficient at the one, or few,
  tasks they are designed for.
* Features of General Purpose Computers
    * A large amount of memory (large in terms of the everyday u that allows a wide range of tasks to be performed.
    * A large amount of local disk storage (again, large in everyday terms),
    * Built from readily available, off-the-shelf, mass-market components,
    * Can run a variety of operating systems,
    * Can run a wide variety of software,
    * Has lots of different kinds of connections for peripheral devices.
    * Is relatively inexpensive.

## Embedded Systems

* The term embedded system refers to the use of electronics and software within a product, as opposed to a
  general-purpose computer.
* A combination of computer hardware and software, and perhaps additional mechanical or other parts, designed to perform
  a dedicated function. In many cases, embedded systems are part of a larger system or product, as in the case of an
  anti lock braking system in a car.
* Embedded systems may or may not be accessible from outside and their user interaction can be limited.
* </br><img src="./img/25.png" alt="alt text" width="500" height="300">
* there are a number of elements that differ from the typical desktop or laptop computer:
    * There may be a variety of interfaces that enable the system to measure, manip- ulate, and otherwise interact with
      the external environment. Embedded sys- tems often interact (sense, manipulate, and communicate) with external
      world through sensors and actuators and hence are typically reactive systems; a reactive system is in continual
      interaction with the environment and executes at a pace determined by that environment.
    * The human interface may be as simple as a flashing light or as complicated as real-time robotic vision. In many
      cases, there is no human interface.
    * The diagnostic port may be used for diagnosing the system that is being controlled—not just for diagnosing the
      computer.
    * Special-purpose field programmable (FPGA), application-specific (ASIC), or even non digital hardware may be used
      to
      increase performance or reliability.
    * Software often has a fixed function and is specific to the application.
    * Efficiency is of paramount importance for embedded systems. They are optimized for energy, code size, execution
      time, weight and dimensions, and cost.
* There are several noteworthy areas of similarity to general-purpose computer systems as well:
    * Even with nominally fixed function software, the ability to field upgrade to fix bugs, to improve security, and to
      add functionality, has become very important for embedded systems, and not just in consumer devices.
    * One comparatively recent development has been of embedded system platforms that support a wide variety of apps.
      Good examples of this are smart- phones and audio/visual devices, such as smart TVs.

## Mainframes and supercomputers

* Connecting one main computer via dumb terminals (hey were simply remote interfaces to the 'real' computer system. This
  was also an early form of networked computing infrastructure.) and allow users to use hos computers are called main
  frames
    * Any user could run their application and perform a task right at their desk. In order to give the impression that
      everyone had equal access, the concept of time-slicing was utilised.
* Going in the opposite direction,there were some computing domains
  where sharing out small slices of compute time to lots of general purpose users was not the primary goal. Instead, the
  demand was to run hugely complex computational tasks,with massive amounts of data,and to do so as fast as possible. A
  system designed to fulfil that kind of function is known as a **super computer**.

## Ambdal's Law

* Ambdal's Law deals with the potential speedup of a program using multiple processors compared to a single processor.
* Amdahl’s Law predicts the maximum speedup possible in a system and where some proportion of its activity P is
  optimised
* Amdahl's Law states that if a P percentage of a system is optimised, the maximum possible speedup is 1/(1-P). If P=0,
  this gives 1, which means no change in speed. P=0.5 gives 2, so, in the best case, if the improved half diminishes to
  0, this gives us 2 times the initial speed but can't exceed it.
    * the speedup using a parallel processor with N processors that fully exploits the parallel portion of the program
      is as follows
    * **True Speedup**: This formula gives infinity for P=1 as it isn't very realistic. To fix this, the formula is
      updated as 1/((1-P)+(
      P/N)) where N is the speedup factor for the optimization (N represents number of processor dividing the workload).
    * Example, if 80% can be optimised and we have 2 cores, this gives us 1/(0.2 + (0.8/2))=1.7. So, that 20% that can't
      be parallelised avoids the x2 speed and by incorporating N, we know how much we are going to improve rather than
      assuming the idealistic case of assigning '0' time.
    * Also note that when the CPU count approaches infinity, the formula gets closer to the original for of 1/(1-P).
* </br><img src="./img/22.png" alt="alt text" width="500" height="300">
* </br><img src="./img/23.png" alt="alt text" width="500" height="300">
* </br><img src="./img/24.png" alt="alt text" width="500" height="300">
* we’re assuming it’s a thousand in this case: remember, in reality, when we look at the case where
  there’s a thousand processors, we are dividing that 80% that we know can be optimised by
  execution in parallel, we’re dividing that amongst a thousand processors, but we’re not
  diminishing the remaining 20% at all.
* And you can see that, no matter how many processors you have, the 0.2
  portion of the equation will always be there, and that means we can never achieve a better
  speedup than 5, in the best-case possible scenario. And that’s what Amdahl’s original
  expression for Amdahl’s Law tells you - maximum speedup is 5, and here we’re approaching
  very closely the maximum and adding more processors at this point will have very little
  benefit.

## TODO Week 1 :

* 1.6 Activity did not finalise

# WEEK 2

* [Making Memory](#making-memory)

# Making Memory

* learn about :
    * Concepts of memory storage and terminology
    * Volatile and non-volatile memories
    * Static and dynamic memory technologies
* A computer memory retains information (data) for a period of time.
* A computer memory, on the other hand, is typically a permanent part of the computer system, and can be either volatile
  or non-volatile.
* However, storage devices are secondary data storage mediums, often capable of being removed from the computer
  system, and are typically non-volatile.

## Volatile and Non-Volatile Memory

* Volatile memory: DRAM and SRAM
    * Static Randomly Access Memory (SRAM) and the Dynamic Random Access Memory (DRAM).
* Static Randomly Access Memory (SRAM)
    * Uses 6T bit cell
    * Operates using purely digital circuitry, and the 6T bit-cell will remain in a zero or one state for as long as
      power is provided.
    * Even a short glitch leads to information loss or data corruption.
    * Is very fast
    * Has lower storage density and occupies more space than DRAM
    * Is more expensive than DRAM per bit
    * SRAM is roughly 3 times slower than the CPU's clock.
* DRAM
    * Uses capacitors (A capacitor is almost like a mini-battery, but it loses its charge quickly.) which take less
      space than 6T bit cell.
    * is relatively slow compared to SRAM
    * Has certain additional circuit operating requirements, known as a refresh cycle
    * Comes in SIMM and DIMM modules
    * DRAM access time (the time taken to read a data value) is 5-20 times slower than CPU speed.
    * This potential slow relative speed of memory means that a CPU could spend a lot of time simply waiting for DRAM to
      respond to a request for data instead of working on it.
      can be one to three times slower.
    * DRAM’s come in a number of formats, the most popular of which are small circuit boards known as **SIMM** and **
      DIMM** modules. These can be slotted into a socket on a motherboard of a computer system, and just as easily
      removed, making the system easily configurable and upgradeable.

### Non-volatile memories

* Non-Programmable (Read-Only) Memory:
    * Permanently manufactured with aparticular data content.
    * Manufactured as an Integrated circuit (1C) with fixed content.
    * Expensive to design, and to update (needs redesign).
    * Cheap when mass produced.
    * Sometimes referred to as Read-Only Memory (ROM).
    * Data content is never lost.

* One-Time Programmable Memory
    * Manufactured with an array preset to ablank state.
    * Can then be programmed to aparticular data content.
    * Once data is programmed it can never be erased.
    * Cheaper to manufacture.
    * Changes to content just require changes to the data being ’burned’ into the memory.
    * Data content is never lost.
    * Often known as PROM (Programmable Read Only Memory).

* Once programmed ROM and PROM can never be altered
* PROM comes un-programmed from the factory and customer programs them once.
* A true ROM (i.e. one that is manufactured as an 1C with a fixed content) is used where a permanent data content is
  required, and this is to be mass produced in very large numbers. ROM is used where content must never be altered.
    * For example, a program in an implanted medical device is safety critical and must never be able to be corrupted or
      deliberately hacked. ROM is a safe solution here.
    * However, it is very expensive to manufacture aROM from start to finish. The chips may only cost $5 but the design
      cost could be $250,000. To avoid such large up-front costs, we often use PROM instead.

* Programmable Non-Volatile Memory :
    * Can be erased and reprogrammed many times.
    * Data is retained even when no power is present.
    * Erasure and reprogramming can be done in several ways:
    * Non-volatile memory : EPROM and PROM
        * EPROM: Erasable Programmable ROM, is erased by UV light, and programmed by electrical signals.
        * EEROM: Electrically Erasable ROM, erased by an electrical signal, programmed by an electrical signal.
        * EAROM: Electrically Alterable ROM, is reprogrammable by electrical signals.
        * Flash Memory: A variation of EEROM, has large capacity, cheap, relatively fast to read and write data.
            * it is removable, non-volatile

### Questions:

* Which Memory protocol allows consecutive locations to be accessed in quick succession?
    * Burst Mode
* Fast Page Mode memory is fast because:
    * It allows multiple columns to be addressed in turn
* Describe what Cycle time means.
    * Cycle time is the time taken for a memory device to complete a whole memory access and be ready to start again
      with the next memory transaction.
* Which of these memories are non-volatile:
    * EPROM
    * PROM
* Which of these memories can never be altered once configured for their use:
    * ROM
    * PROM

# DRAM (Dynamic Random Access Memory)

## Memory Timing Concept:

* DRAM (Dynamic Random Access Memory) requires information to be provided in a form of an address, which tels the DRAM
  where in the memory chip it should access the data.
    * Because there are many millions of locations and we then generate a “data write” or a “data read”.
* There’s a protocol that is a set of procedures that allows a DRAM to perform a read operation.
* First CPU supplies a ROW (1 Clock cycle), which is half of the address
* The next we get a column (COL), which is the other half of the address. ROW and COL gives us the whole address
* The next we WAIT, because DRAM requires some time for internal circuitry to perform the read operation
* after wait, the DRAM is able to locate the particular item in the memory within the ROW and COL grid of
  its storage array that we want to access and it can output that piece of information called Data on the bus, we class
  that as READ
* </br><img src="./img/26.png" alt="alt text" width="500" height="300">
* Access time: the time after DRAM compates the address (after COL) and until the end of the READ (which the CPU can
  then access the data from.)
* </br><img src="./img/27.png" alt="alt text" width="500" height="300">
* READ latency: It is beginning from the ROW until the end of READ.
    * This helps us to understand how fast can read data from memory
* Recovery cycle: one DRAM finish READD data, depending on initial architecture of DRAM, does not do anything, we caled
  recovery cycle.
* </br><img src="./img/28.png" alt="alt text" width="500" height="300">
* Cycle Time: From beginning to the end of the after READ waiting we called Cycle time. It is probably the most
  important timing quantity for a memory because it dictates how quickly we can complete an entire READ cycle and then
  be ready to start the next READ cycle.
* Performance calculationL
* Finding the number of reading per second:
    * So the read rate of the memory is different to the clock rate so don’t get those two things confused. 1333
      Megahertz is not the same as the amount of read transactions that the memory can perform.
* </br><img src="./img/29.png" alt="alt text" width="500" height="300">
* If each read is 32 bits, which is four bytes, then we end up with a memory bandwidth of 266 million (which we’ve
  already worked out is the reads per second) multiplied by 4 (the number of bytes read per operation)  and that equates
  to 1064 million bytes per second.
* </br><img src="./img/30.png" alt="alt text" width="500" height="300">
* </br><img src="./img/31.png" alt="alt text" width="500" height="300">

## Boosting Memory Performance

* There are some technics to boost the memory performance
* Standard Read operation:
* </br><img src="./img/32.png" alt="alt text" width="500" height="300">
* </br><img src="./img/33.png" alt="alt text" width="500" height="300">
    * after getting ROW and COL addresses of data, we started to read.
    * we found in the previous video that the standard access time for a single READ is 5 clock cycle
    * And this is very inefficient because if we’re only reading one item and
      transferring one data item on the data BUS in every 5 clock cycles, then the efficiency of that
      system is no better than 20%.
* There are 2 technics to Improve:
    * Burst Mode Access
    * Fast Page Mode Access

### Burst Mode Access

* Normally after READ, DRAM causes a delay and finally after that delay we get to read the item of interest so we’ve
  read the first location here and now instead of finishing the operation at this point Burst Mode continues to look at
  the next location and the next location and the next location in a consecutive manner.
* </br><img src="./img/34.png" alt="alt text" width="500" height="300">
* So it's now going to continue to read and there are no delays now because we’ve already accessed the row of interest
  and we just simply need to select the item within the column that we’re interested in and this will continue **until
  we come to a point where, when we’ve completed the read burst,**
* we’ve actually read four items in a row and in this case the **Burst length** is four.
* 4 reads, taking a total of 8 clock cycles, so the average is 2 clock cycles per read better than 5 clock cyles read.

#### Mixed burst mode

* Example: In a system with 1333MHz clock rate, normal mode requires 7 clocks per block and the burst mode requires 2.5
  clocks per block and can only be used for 40% of the time on average. What will be the average data rate for a 32 bits
  system?
* 2.5*0.4 + 7*0.6 = 5.2 clocks/block
* 1333x10^6 / 5.2 = 256.35e6 blocks/s = 256.35e6 * 4B = 1025.4 MB/s = 978 MiB/s

## Fast Page Mode Access

* In Page Mode, after we READ we continue to provide Random COL and READ another value.
* The length of a Page Mode access sequence can be quite long if we want it to be - in this case
  we’ve made it 4 reads long - and that means 4 reads.
* </br><img src="./img/35.png" alt="alt text" width="500" height="300">
* 4 read, requires 11 clock cycle, makes 2,75 clock cycle per READ
* When we compare and convert 5 clock cyles into a number of gigabytes per second for different cases here
* On this basis we are assuming a frequency of 1333MHz which is a fairly common standard for memory bus timing, and a
  32-bit read, which again is a fairly common standard, that means 4 bytes per read.
* </br><img src="./img/36.png" alt="alt text" width="500" height="300">
* approximately 1GB per second in standard mode
* Burst mode, with the reduction in average cycle time, we end up with about 2.5GB per second.
* Page mode, for a short sequence of access, is equivalent to that of burst mode, has a lower performance - 1.8GB per
  second
    * but as page mode is used for longer and longer sequences, it tends towards an ultimate top range value of
      approximately 2.5GB per second as well.
    * page mode sequences have the flexibility of not having to be in a continuous incrementing sequence.

## Storage Technology Trends

* Since 1985
    * SRAM access times and cost per megabyte have decreased by a factor of about 100
    * DRAM cost per megabyte has decreased by a factor of 44,000 but access times have decreased by only a factor of 10
    * Disk storage costs per megabyte have dropped by a factor of 3,000,000 and access times have improved much more
      slowly, by only a factor of 25
    * CPU cycle times improved 500 times within the same period. So, DRAM and Disk performances are lagging behind the
      CPU.
    * While the SRAM keeps up, the gap between DRAM, disk performance and CPU performance is widening.
    * Modern computers make heavy use of SRAM based caches to try to bridge the processor-memory gap.
        * This approach works because of a fundamental property of application programs known as locality,
* </br><img src="./img/37.png" alt="alt text" width="500" height="300">
* </br><img src="./img/38.png" alt="alt text" width="500" height="300">

## Locality

* Programmers should understand the principle of locality because, in general, programs with good locality run faster
  than programs with the poor locality.
* All levels of computer systems, from the hardware to the operating system, to application programs, are designed to
  exploit locality.
* The hardware uses cache memories that hold blocks of the most recently referenced instructions and data items.
* At the OS level, the principle of locality allows the system to use the main memory as a cache of the most recently
  referenced chunks of the virtual address space.
* Temporal locality: If at one point a particular memory location is referenced, then it is likely that the same
  location will be referenced again in the near future.
    * In this case it is common to make efforts to store a copy of the referenced data in faster memory storage, to
      reduce the latency of subsequent references.
* Spatial locality: If a particular storage location is referenced at a particular time, then it is likely that nearby
  memory locations will be referenced in the near future.
    * In this case it is common to attempt to guess the size and shape of the area around the current reference for
      which it is worthwhile to prepare faster access for subsequent reference.
* </br><img src="./img/41.png" alt="alt text" width="500" height="300">
    * sumvec function enjoys good locality.
    * The elements of vector v are read sequentially, one after the other, in the order they are stored in memory
    * Thus, with respect to variable v, the function has good spatial locality but poor temporal locality since each
      vector element is accessed exactly once.
    * Since the function has either good spatial or temporal locality with respect to each variable in the loop body
    * A function such as sumvec that visits each element of a vector sequentially is said to have a stride-1 (sequential
      pattern) reference pattern
    * Visiting every kth element of a contiguous vector is called a stride-k reference pattern. Stride-1 reference
      patterns are a common and important source of spatial locality in programs.
    * In general, as the stride increases, the spatial locality decreases.
* </br><img src="./img/42.png" alt="alt text" width="500" height="300">
    * The result is a nice stride-1 reference pattern with excellent spatial locality.
    * The doubly nested loop reads the elements of the array in row-major order. That is, the inner loop reads the
      elements
      of the first row, then the second row, and so on.
    * The sumarrayrows function enjoys good spatial locality because it references the array in the same row-major order
      that the array is stored
* </br><img src="./img/43.png" alt="alt text" width="500" height="300">
    * poor spatial locality
    * because it scans the array column-wise instead of row-wise.
    * Since C arrays are laid out in memory row-wise, the result is a stride-N reference pattern,

* Since program instructions are stored in memory and must be fetched by the CPU, we can also evaluate the locality of a
  program with respect to its instruction fetches
    * Having a sequentially ordered set of instructions in the loop body and repeating the loop multiple times also
      gives good temporal locality as the instruction pipelining gets a high hit ratio.

* Summary:
    * Programs that repeatedly reference the same variables enjoy good temporal locality.
        * For programs with stride-k: reference patterns, the smaller the stride, the
          better the spatial locality.
    * Programs with stride-1 reference patterns have good spatial locality.
        * Programs that hop around memory with large strides have poor spatial locality.
    * Loops have good temporal and spatial locality with respect to instruction fetches.
        * The smaller the loop body and the greater the number of loop iterations, the better the locality.

* **Question:**
* </br><img src="./img/39.png" alt="alt text" width="500" height="300">

* **Answer:**
    * To create a stride-1 reference pattern, the loops must be permuted so that the rightmost indices change most
      rapidly.
  ```
  int productarray3d(int a[N][N][N]) 2{
    for (j = N-1; j >= 0; j--) {
       for (k = N-1; k >= 0; k--) {
         for (i = N-1; i >= 0; i--) {
            product *= a[j][k][i];
         }
       }
    }
      return product;
   }
  ```
  This is an important idea. Make sure you understand why this particular loop permutation results in a stride-1 access
  pattern.

* **Question:**
* </br><img src="./img/40.png" alt="alt text" width="500" height="300">

* **Answer**
    * The key to solving this problem is to visualize how the array is laid out in memory and then analyze the reference
      patterns.
    * Function clear1 accesses the array using a stride-1 reference pattern and thus clearly has the best
      spatial locality.
    * Function clear2 scans each of the N structs in order, which is good, but within each struct it hops around in a
      non-stride-1 pattern at the following offsets from the beginning of the struct: 0, 12, 4, 16, 8, 20 .
    * So clear2 has worse spatial locality than clear1. Function clear3 not only hops around within each struct,
      but also hops from struct to struct. So clear3 exhibits worse spatial locality than clear2 and clear1.

* [RAM Benchmarks](https://ram.userbenchmark.com/)

# The Performance Challenge

* We improve the speed of the memory architecture by using some additional architectural structures , known as Cache,
  and cache is just a fast memory device
* Main memory (DRAM) is large, slow and cheap. Cache is quick, small and quite expensive.
* As we noted earlier, SRAM is smaller, more expensive, but much faster than DRAM.
    * The concept of cache Is to provide a small amount of fast SRAM a long side a large amount of slow DRAM.
* So far, we have assumed that caches hold only program data. But, in fact, caches can hold instructions as well as data

## Cache for Speedup

* let's say all of the memory accesses require five clock cycles
* let's assume CPU read s from cache with 2 clock cycle.
* </br><img src="./img/44.png" alt="alt text" width="500" height="300">
* why would we read data from cache instead of from memory?
    * cache keeps copies of memory contents that are used frequently.
    * So, given that if you were to analyse a program, perhaps 10% of the data in the code will be accessed very
      frequently and the other 90% of the data in the code might be accessed very infrequently.
    * We could keep copies of the frequently accessed 10% in the cache memory, thereby the CPU would be able to go the
      cache memory and get a result very quickly instead of going to the slow memory and getting the result, taking a
      long time.
* a mixture of CPU and memory and CPU and cache,
* </br><img src="./img/45.png" alt="alt text" width="500" height="300">
* To calculate average clock cycles we need to include hit rates
* If CPU can find data in Cache we called **hit**, if can not and go to memory we called **missed**
* </br><img src="./img/46.png" alt="alt text" width="500" height="300">

## Multi-level Cache

* Modern processors tend to have on chip cache (on-chip cache) integrated into the silicon chip design, because there
  are so many
  transistors available in modern CPUs.
    * It is not difficult to integrate a section of the CPU circuitry to contain an additional cache.
* Lets assume build in cache has 1 cycle
* CPU cache hit rate is 90% and chip cache hit rates %80
* </br><img src="./img/47.png" alt="alt text" width="500" height="300">
* 1.5 – that’s the average memory speed of the system using on chip cache, that would give us quite a significant
  increase in memory bandwidth
* When this example processor is used in asystem where the external memory already has a cache, it would be referred to
  as a **two-level** cache hierarchy, where the on-chip cache represents level one and the external cache represents
  level two.
* benefits of using on-chip cache:
    * The on-chip cache can be optimised to work with the CPU circuitry to hide the address setup clock cycles, using
      overlapping activities (pipelining) to make these appear to take zero time. This means that the on-chip cache can
      deliver anew data item for every clock cycle.
    * The width of the on-chip cache can be fairly arbitrary, matched to the internals of the CPU rather than external
      memory, and potentially organised in ways that maximise cache performance for that specific processor under
      specific conditions.
    * The instruction cache and data cache can be accessed simultaneously, and it is rare that both caches have amiss
      at the same time, meaning that even if one cache misses, it can use the external memory bus whilst the other
      cache continues as if nothing has happened.
    * The split cache gives the impression that the memory bus no longer has the von Neumann bottleneck. On-chip at
      least, it is much closer to a Harvard architecture.
* </br><img src="./img/50.png" alt="alt text" width="500" height="300">
* multiple levels of cache allows other activities to continue in parallel with the CPU
* So while the CPU is doing its accessing of data in the cache, you can have something else happening an IO device could
  access memory
* we have a situation where the cache may want to fill up some of its content in order to make sure it contains the
  correct information so that later on when the CPU comes along and wants to use that cache it will get more hits, that
  is one way that the cache can improve its performance
* whereby two IO devices want to talk to each other and they also need to use the bus, because the CPU is busy
  internally accessing its cache, the external bus is available for any combination of these devices to be able to
  transfer data to each other.
* That concurrency, that parallelism is another way that on chip cache can boost performance
* Operating in parallel. So now, with the ability to operate the CPU such that it can access both instruction and data
  cache simultaneously, we could reasonably argue that average access time is actually half this amount, or 0.68 clock
  cycles .
    * This is evident, because if we can read two values at atime with an average access time of 1.35 clocks, then the
      average per single value is 1.35 divided by 2, giving 0.68 clocks per access.
* If we were again to assume the processor/system clock frequency is 1000 MHz, then we can also say that instruction
  bandwidth for the multilevel system with split cache is 1000/0.68 =1470 Million reads/sec, and the same for data
  bandwidth.

### Anatomy of a Real Cache Hierarchy

* And furthermore than on-chip cache, this cache may be split into two parts (a dual cache), these being instruction
  cache and data cache.
* A cache that holds instructions only is called an i-cache.
* A cache that holds program data only is called a d-cache.
* A cache that holds both instructions and data is known as a unified cache.
* With two separate caches, the processor can read an instruction word and a data word at the same time
* I-caches are typically read-only, and thus simpler
* The two caches are often optimized to different access patterns and can have different block sizes, associativities,
  and capacities.
* Also, having separate caches ensures that data accesses do not create conflict misses with instruction accesses, and
  vice versa, at the cost of a potential increase in capacity misses.

#### Performance Impact of Cache Parameters

</br><img src="./img/51.png" alt="alt text" width="500" height="300">

* Cache performance is evaluated with a number of metrics:
    * **Miss rate**. The fraction of memory references during the execution of a program, or a part of a program, that
      miss. It is computed as # misses/ # references.
    * **Hit rate**. The fraction of memory references that hit. It is computed as 1 − miss rate.
    * **Hit time.** The time to deliver a word in the cache to the CPU, including the time for set selection, line
      identification, and word selection. Hit time is on the order of several clock cycles for L1 caches.
    * **Miss penalty**. Any additional time required because of a miss. The penalty for L1 misses served from L2 is on
      the order of 10 cycles; from L3, 50 cycles; and from main memory, 200 cycles.
* Impact of Cache Size:
    * A larger cache will tend to increase the hit rate. On the other hand, it is always harder to make large memories
      run faster.
    * As a result, larger caches tend to increase the hit time. This explains why an L1 cache is smaller
      than an L2 cache, and an L2 cache is smaller than an L3 cache.
* Impact of Block Size:
    * for a given cache size, larger blocks imply a smaller number of cache lines, which can hurt the hit rate in
      programs with more temporal locality than spatial locality.
    * Larger blocks also have a negative impact on the miss penalty, since larger blocks cause larger transfer times.
* Impact of Associativity:
    * The issue here is the impact of the choice of the parameter E, the number of cache lines per set.
    * The advantage of higher associativity (i.e., larger values of E) is that it decreases the vulnerability of the
      cache to thrashing due to conflict misses
    * Higher associativity can increase hit time, because of the increased complexity, and it can also increase the miss
      penalty because of the increased complexity of choosing a victim line.
* Impact of Write Strategy:
    * Write-through caches are simpler to implement and can use a write buffer that works independently of the cache to
      update memory.
    * Furthermore, read misses are less expensive because they do not trigger a memory write
    * In general, caches further down the hierarchy are more likely to use write-back than write-through.

#### Memory Mountain

* The rate that a program reads data from the memory system is called the **read throughpu**t, or sometimes the read
  bandwidth.
* If a program reads n bytes over a period of s seconds, then the read throughput over that period is n/s,
  typically expressed in units of megabytes per second (MB/s).
* If we were to write a program that issued a sequence of read requests from a tight program loop, then the measured
  read throughput would give us some insight into the performance of the memory system for that particular sequence of
  reads.
* The size and stride arguments to the run function allow us to control the degree of temporal and spatial locality in
  the resulting read sequence.
    * Smaller values of size result in a smaller working set size, and thus better temporal locality.
    * Smaller values of stride result in better spatial locality.
    * If we call the run function repeatedly with different values of size and stride, then we can recover a fascinating
      two-dimensional function of read throughput versus temporal and spatial locality. This function is called a
      **memory mountain** .
* the performance of the memory system is not characterized by a single number.
    * Instead, it is a mountain of temporal
      and spatial locality whose elevations can vary by over an order of magnitude.
    * Wise programmers try to structure their programs so that they run in the peaks instead of the valleys.
    * The aim is to exploit temporal locality so that heavily used words are fetched from the L1 cache, and to exploit
      spatial locality so that as many words as possible are
      accessed from a single L1 cache line.

## QUIZ - WEEK 2

* **Question 1:** Calculate the number of addressable locations for a memory device with the following total number of
  address lines
  a. 16
  b. 24
  c. 9
* Answer:
  a. 2 16 = 65,536
  b. 2 24 = 16,777,216
  c. 2 9 = 512

* **Question 2:** A memory device has 16 address lines and 64 data lines. Calculate the storage capacity of the memory
  in
  bytes and kilobytes.
* Answer:
    * From question 1 we know that 16 addresses gives us 65536 locations. If each location has 64 data lines (64 bits)
      then this is 8 bytes (8*8=64). So we have:-
    * 8 x 65536 = 524,288 bytes
    * Divide by 1024 to get 512 Kilobytes

* **Question 3:** A memory has the following timing characteristics:-
    * Access time 3 clock cycles.
    * Zero Recovery cycles needed.
    * RAS(ROW Access) and CAS(COL Access) are 1 cycle each.
      Calculate the average memory read time.
* Answer:
    * Calculate the average memory read time.
    * If we Add ROW, COL, and 3 access time cycles we get 5 cycles.
    * So the average read time is 5 cycles.

* **Question 4:** For the memory speed calculated in (3), determine the data rate if the memory is 16bits wide and has a
  clock rate of 1GHz.
* Answer:
    * At 1GHz we get 1000/5 = 200 Million reads per second.
    * Each read is 2 bytes (16 bits), so we get 2x200 Million = 400 Million bytes per second
    * 400,000,000 / (1024*1024) = 381.467 MBps
* **Question 5:** A system has a main memory has a read time of 6 clock cycles, a cache with a read time of 1 clock
  cycle,
  and a hit rate of 75%.
  a. Calculate the average memory read time
  b. Calculate the worst case read time.
* Answer:
    * Average read time:
        * HIT 75% , requires 1 clock cycle, 1 x 75% = 0.75
        * MISS 25%, requires 1+6 = 7 cycles, 7 x 25% = 1.75
        * TOTAL = 0.75 +1.75 = 2.5 cycles. (average read time)
    * The worst case is when a cache miss occurs, resulting in a cache read (1) and a memory read (6) so worst case = 7
      cycles.

# Quick calculations :

* n address lines can address 2^n locations.
* n address lines where each memory block is K bits gives 2^n * K / 8 Bytes of memory.
* If a system's memory is 16 bits wide, has a clock rate of 1GHz and requires 5 clock cycles to access the memory, then
  the data rate is 10^9 * (16/8) / 5 = 400 MB/s = 381.47 MiB/s = 3.2Gbps

# WEEK 3

# WEEK 4

# WEEK 5

# WEEK 6

# WEEK 7