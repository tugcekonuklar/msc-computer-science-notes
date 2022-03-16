#### Main Topics

#### Sub titles:

# Variables

* There are no primitive types as there are in Java. The closest Python gets to this is a set of single value types
  referred to as 'Scalar types'.
* Unlike in Java, Python does not let you declare variables without assigning a value to them. So variables in Python
  are only declared at the point they are needed and assigned an initial value.
  <img src="./img/1/1.png" alt="alt text" width="500" height="300">

```py
  In [5]: num1 = 6
  In [6]: num2 = 105
  In [7]: sum = num1 + num2
  In [8]: product = num1 * num2
  In [9]: quotient = num2 / num1
  In [10]: difference = num1 - num2
  In [11]: print(f"Sum: {sum}, product: {product}")
  Sum: 111, product: 630

  In [12]: print(f"Quotient: {quotient}, difference: {difference}")
  Quotient: 17.5, different: -99
  ```

* The result of integer division (105 / 6) will produce a floating point value as a result. So the variable quotient
  will hold the value 17.5, not 17 as you would get in Java. To get the quotient as a whole number and the remainder
  separately you need to use the following operators:

```
In [13]: wholeNum = 105//6
In [14]: remainder = 105 % 6
In [15]: print(f"Whole number: {wholeNum}, Remainder: {remainder}")
Whole number: 17, Remainder: 3
```

  <img src="./img/1/2.png" alt="alt text" width="500" height="300">

# Decision / Conditions

* Python are if, elif and else
* Python is that it uses spaces “ ” (indentation) to define code structures, or 'blocks', whereas Java uses curly braces
  { } for this job.

```
In [1]: num1 = 56                                                     
In [2]: num2 = 37                                                     
In [3]: if num1 > num2:
     ...:     print(f"{num1} is larger than {num2}")
     ...: elif num1 < num2:
     ...:     print(f"{num1} is smaller than {num2}")
     ...: else:
     ...:     print("Both numbers are the same.")
56 is larger than 37

```

## Single line conditions

* do_something_if_TRUE if condition else otherwise do_something_else

## Condition statements

<img src="./img/1/3.png" alt="alt text" width="500" height="300">

# Loops

* Python has two structures for iteration: a for style loop and a while loop.

*** for loop :**

* renge() : The method range() is used to generate a list of valid values (steps) for each iteration. In Python 3.x the
  range() method returns an immutable sequence of type range, whereas in Python 2.x it returns a List. A common
  misconception is that range() still produces a List type, which is incorrect as range is a type in itself.
    * `range(start, end, steps)`
    * ins sample 3 (inclusive) and ends at 5, making the 6 exclusive.

``` 
  In [1]: for i in range(3,6):                                           
    ...:     print(i)
    ...:     
    3
    4
    5
  ```

* **while loop:**
* The while loop requires a counter defined outside the loop and an increment (or decrement) defined inside the loop

```
In [2]: count = 0
In [3]: while count <= 4:
   ...:     print(count)
   ...:     count += 1
   ...:     
0
1
2
3
4

```

* have an else clause attached at their end

```
 In [4]: while count < 6:
   ...:     print(count)
   ...:     count +=2
   ...: else:
   ...:     print("Finished!")
   ...:      
0
2
4
Finished!
```

* Loop controls
  <img src="./img/1/4.png" alt="alt text" width="500" height="300">

# Best Practice

* **Naming conventions:**
    * Variable names should be lower case.
    * Function names should be lower case.
    * Classes and Module names should be in Title Case.
    * Constants should be UPPER CASE with an underscore (_) used for spaces.

* Short variable names such as x, y, i, j are only used in enclosed structures such as a loop.
* All other variable names should clearly define what the variable holds in the context of the program, or function,
  they are defined within.
    * Function names should focus on what the function does and not on how it is implemented.
* Python coders typically use either snake_case or camelCase to differentiate words used in their variable names.
* the keywords (commands) cannot be used as variable names. like below:
  <img src="./img/1/5.png" alt="alt text" width="500" height="300">

* **White space:**
    * An expected standard is to use 2 or 4 spaces for indentation. Tabs should generally be avoided as their size
      varies in different IDEs and can be identified as an error by the Python interpreter.
    * Lines of code should not exceed 79 characters.

```
i = x + 1             # clear
i=x+1                 # not so clear

# grouping to make related operators and operands clearer
a = (b+4) * (c-7)           # clear
a = ( b + 4 ) * ( c - 7 )   # not so clear 
```

* Comments:

```
# a single line comment or

# a block comment both use 
# the hash symbol

area = pi * radius**2  #comment after a line of code 
```

# Strings and I/O

* [Python API](https://docs.python.org/3/library/string.html)
* They can be defined using either 'single quotes' or using "double quotes".
* Strings are an index from position 0 and each individual character can be accessed and manipulated using this index.
  The string “blue bird.” is 10 characters long and is an index from 0 to 9.
* Using this index, individual characters can be accessed easily using the square bracket notation [ ]
* Just like Java strings, Python strings are **immutable**; they cannot be changed once created. Even if a method looks
  as if it is adapting an existing string, it is not. It is creating a new one and discarding (in some cases) the old
  one

``` 
In [1]: myString = "Blue Birds."
In [2]: myString[5]
Out[2]: 'B'
```

* This index and the square brackets [] can be used to create a slice (substring) of a string.

``` 
In [3]: endOfString = myString[3:]
In [4]: endOfString
Out[4]: 'e Bird.'
In [5]: middleOfString = myString[3:6]
In [6]: middleOfString
Out[6]: 'e B'
```

* built-in functions:
    * [build in functions](https://docs.python.org/3/library/functions.html)
    * some built-in functions for string
      <img src="./img/1/6.png" alt="alt text" width="500" height="300">

## Formatting Strings

* One of the most useful methods that the string object provides is the format() metho
    * 2 ways to use

* .format()

```
In [7]: firstName = "Frank"
In [8]: age = 34
In [9]: "My name is {} and I am {} years old.".format(firstName, age)
Out[9]: 'My name is Frank and I am 34 years old.' 
```

* f placed before the string and the variables are embedded in the {}

```  
In [10]: f"My name is {firstName} and I am {age} years old."
Out[10]: 'My name is Frank and I am 34 years old.'
```

* for numbers

``` 
In [11]: pi = 3.14159
In [12]: rad = 6
In [13]: cir = 2 * pi * rad
In [14]: f"A radius of {rad:.2f}cm gives a circumference of {cir:.2f}cm"
Out[14]: 'A radius of 6.00cm gives a circumference of 37.70cm'

# 42. Formatting numbers, first a float to 2dp, second an integer to 4dp float
print(f"42. I am {myHeight:.2f}m tall and weigh {myWeight:.4f}kg")
```

## Console Output

* print() command

```
In [15]: print("A string:", myString, "A number:", 1567)
A string: Blue Birds. A number: 1567
```

* four keyword arguments that can be placed at the end of the argument list as required. These are sep, end, file and
  flush.
    * For formatting purposes, sep adds a separator between previous arguments (the default is a space), and end changes
      how the output should be terminated (the default is a new line

``` 
In [16]: print(56,78,"pink", sep="*",end="!")
56*78*pink!
```

## Console Input

* The input() method captures and returns anything entered in the console.
* The returned content is always a string, so if integers or floating point values are required by the program, then the
  string will need to be cast to the appropriate type
    * Simply wrap the input() method in either int() or float()

``` 
In [17]: name = input("Name: ")
Name: Frank
In [18]: num1 = int(input(f"{name} please enter a number: "))
Frank please enter a number: 45
In [19]: num2 = int(input("and a second number: "))
and a second number: 67
In [20]: sum = num1 + num2
In [21]: f"{name} the sum of {num1} and {num2} is {sum}."
Out[21]:'Frank the sum of 45 and 67 is 112.'

```

* user try catch

``` 
    try:
        myAge = int(input("Enter your age: "))
    except:
        print("Something has gone wrong")
```

# Lab

* Exercise one
* Write a program that outputs a times table from a given (user entered) integer value. It should start at 2 and output
  only the EVEN multiples. If the user entered the value 13, the even times table would be outputted in the following
  format:

* The even timetable for 13 is:
* 2 times 13 is 26 4 times 13 is 52 6 times 13 is 78 This program should continue until the user chooses to exit. You
  should format this so that the text “times” and “is” is always in the same column. The program should output up to and
  including 20 times the user value.

```
def lab1():
    try:
        inputNumber = int(input("Enter Number: "))
        for i in range(2, 21, 2):
            result = i * inputNumber;
            print(f'{i} times {inputNumber:.2f} is  {result:.2f} ')
    except:
        print("there is a problem")

```

* Exercise two
* In the sample code given for 'Iteration' in 1.1, there is a program for printing out a left-sided triangle of stars.
* Adapt the code to create a right-sided triangle. Adapt the code to output a diamond. Write a menu system so the user
  can choose the left or right-sided triangle, or diamond. Enable the program to take user input for the symbol used to
  generate the pattern and dictate the size of the pattern. The output from the program should look like this:

                                                *
      *                      *                 ***
      **                    **                *****
      ***                  ***                 ***
      ****                ****                  *

Left-sided Right-sided Diamond

``` 
def lab2():
    try:
        selected = int(input("Pres number of types that you want to select :  "
                             "\n 1-Left-sided "
                             "\n 2-Right-sided "
                             "\n 3-Diamond "))
        if selected == 1:
            print("*\n**\n***\n****")
        elif selected == 2:
            print("     *\n    **\n   ***\n  ****")
        else:
            print("    *   \n   **   \n   ***  \n  **** ")
    except:
        print("there is a problem")

```

* Exercise three
* Write a program that outputs a calendar, given two values inputted by the user. If the user inputs the values of 30
  and 7, the following structure will be produced, where 30 generates the number of days in the month and 7 (
  Sunday) indicates which day of the week the calendar starts on. The user should only be able to input a valid range of
  numbers, and regardless of the values entered the calendar should always output 7 lines (even if some of them are
  blank)
  .

``` 
# ugly solution without using data structures
def lab3():
    try:
        days = int(input("Count of days in a month : "))
        startWeekDay = int(input("Start week day : "))
        print("Calender")
        print("M   T   W  Th   F   S  Su")
        start = 0
        index = 1
        calender = ""
        while start <= 7 and index <= days + 6:
            if startWeekDay == start and index <= days:
                day = days - (days - index)
                calender += str(day)
                calender += "   "
                startWeekDay = (start + 1) % 7
                index += 1
            else:
                calender += "    "
            start = (start + 1) % 7
            if start == 0:
                print(calender)
                calender = ""
            if start == 0 and index >= days:
                break
    except:
        print("there is a problem")
```

# Data Structure

* Python provides a number of built-in data structures.
* Sequence types include range, lists and tuples and more complex types are dictionaries and sets.

# TODO:

* McKinney W. (2017) Python for Data Analysis. 2nd Ed. O'Reilly Media - Chapter 2
* Lee K. D. (2014) Python Programming Fundamentals. 2ndEd. Undergraduate Topics in Computer Science. Springer, Cham. pp
  39-61
* Lee K. D. (2014)Python Programming Fundamentals. 2nd Ed. Undergraduate Topics in Computer Science. Springer, Cham, pp
  63-89.
* [Pep8 guide](https://peps.python.org/pep-0008/)
* Padmanabhan T. R. (2016) Programming with Python. Undergraduate Topics in Computer Science. Springer, Cham. pp 137-174