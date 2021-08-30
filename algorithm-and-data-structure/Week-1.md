#### Main Topics

* Introduce pseudocode conventions
* Asymptotic notations such as big-oh (O), big theta (Ө), big-omega (Ω).
* Linear data structures such as Stacks, Queues and Linked List and their featured operations.

#### Sub titles:

* [Pseudo Code](#pseudo-code)

---

# Pseudo Code

* What separates pseudocode from “real” code is that in pseudocode, we employ whatever expressive method is most clear
  and concise to specify a given algorithm.

* Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input
  and produces some value, or set of values, as output. An algorithm is thus a sequence of computational steps that
  transform the input into the output.

## Algorithm Analysis

* To see which algorithm runs faster, there are 2 approaches.
* **experimental approach**, you need to:
    * write a program implementing the algorithm
    * run the program with inputs of varying size and composition
    * use a method like System.currentTimeMillis() to get an accurate measure of the actual running time
    * plot the results such as in diagram
* limitations for the experimental approach:
    * it is necessary to implement the algorithm, which may be difficult and expensive.
    * It may not be feasible waiting for hours to get a single experimental data.
    * Results may not be indicative of the running time on other inputs not included in the experiment.
    * In order to compare two algorithms, the same hardware and software environments must be used.

* **theoretical analysis approach**:
    * It uses a mathematical description of the algorithm instead of an implementation, which is cheap.
    * It characterises running time as a function of the input size, n.
    * It takes into account all possible inputs.
    * It allows us to evaluate the speed of an algorithm independent of the hardware/software environment.