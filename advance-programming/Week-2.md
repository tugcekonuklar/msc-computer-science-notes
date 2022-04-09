#### Main Topics

#### Sub titles:

# Data encoding

## Binary

* All computers communicate using binary (base 2) at the lowest level.
* However, as this is very difficult for humans to understand when it is in long strings, it is represented in blocks of
  bits called bytes: 01100001 is a single byte. Even with spaces between each byte, it can still be challenging to read
  as well as taking up a lot of physical space.
* Therefore, binary values are more frequently written in Octal (base 8)
  or Hexadecimal (base 16).

## Encoding vs Format

* Encoding is the way in which each symbol is represented by the computer
* The data’s format is the way strings of symbols are arranged within a file and whether or not there is any extra
  information or structure to them (metadata)
* For example: A string containing “a,m,x” has both encoding and format.
    * **Encoding**: Each symbol could be represented as an 8-bit binary code. So a = 01100001, m = 01101101, x =
      01111000 and the comma = 101100. Notice these are all lower case characters; the upper case equivalents would have
      a different code.
    * **Format**: Each of the letters "a", "m", "x" are separated by a comma which is acting as a separator (
      delimitator) between each character, and is adding structure to the string.
        * This type of formatting is used to separate words, sentences and values in whole documents and is referred to
          as Comma Separated Values or CSV for short.
        * Files with a .CSV extension are in this format and can be read by spreadsheet applications such as Microsoft
          Excel.

* These terms “encoding” and “format” can often be used to mean either low-level symbol representation or high-level
  structure of data, and in some cases both.

## ASCII

* One of the most common encoding standards is ASCII (American Standard Code for Information Interchange), which was
  first released in 1963.
* ASCII uses a 7-bit binary sequence, giving a maximum of 128 code points which are used to encode alphanumeric
  characters, punctuation and codes for non-printable control charters such as a cage return (‘\n’).
* This is a very small set of encoded symbols, and it was realised fairly early on that a more extensive and flexible
  system was needed
  <img src="./img/2/1.png" alt="alt text" width="500" height="300">

* ASCII is the default encoding in HTML 4.01, which is still used in about 5% of web pages. Python 2.X’s default
  encoding is ASCII

## Unicode

* The Unicode standard provides both a structuring system and an encoding system, unlike ASCII, that enables consistency
  and extensibility.
* Unicode logically groups symbols into character sets; for example, the capital letter A is part of Basic Latin. Each
  character set is allocated a range of values, with Basic Latin occupying the range 0000–007F (Hexadecimal)
* Unicode code points all have the prefix U+ and are represented as a hexadecimal value. For example, the upper case
  Basic Latin symbol A is represented by U+0041

### Universal Coded Character Set (UCS)

* Like Unicode, UCS provides an organised structure for mapping symbols to code points and is defined by the
  International Standard ISO/IEC 10646 (Links to an external site.). The code points for each symbol in this standard
  are identical to those defined in Unicode, and the two organisations ensure this compatibility.

* As with Unicode, UCS is only concerned with the mapping of symbols, and unlike Unicode, provides no additional
  attributes for symbols. The encoding is left to other formats, some of which are defined within the UCS standard.
  These include UCS-2, UTC-16 and UCS4. However, UTF-8 is more frequently used for encoding UCS.

## UTF-8

* One of the reasons for its popularity is its compatibility with ASCII, as it preserves the ASCII code values, making
  translation fairly straightforward.
* UTF-8 is a variable length encoding system which uses a minimum of one byte when encoding low code points, with up to
  four bytes are available for symbols with higher code point values. Unicode restricts the number of bits used for
  encoding to twenty-one, which leaves a number of “padding bits” in each byte used.
  </br><img src="./img/2/2.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/3.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/4.png" alt="alt text" width="500" height="300"></br>

## UTF-16 and UTF-32

* UTF-16 is a 16-bit variable length encoding form, which uses a minimum of two bytes.
* Whereas UTF-8 can encode the first 128 symbols in one byte, UTF-16 will use two.
* So the capital letter A is represented as 01000001 in UTF-8, and it will be represented by 00000000 01000001 in UTF16
* This is not as widely used as UTF-8, but provides the encoding for larger systems such as operating systems like
  Microsoft Windows, and high-level languages like Java. Very few documents or web-pages use this encoding system.

* UTF-32 is even less popular, and uptake of this standard is generally regarded as being very poor. It is a fixed
  length encoding form and uses 4 bytes (32bits) to encode the 21 maximum bit representation of each Unicode symbol.

# File formats

* Files are used or generated by programs for three main reasons:
    * Data back-up: the program simply needs a way to store data/settings when it is closed so it can resume with that
      data.
    * Data input: the quantity of data that needs to be inputted into a program is too vast to be undertaken by hand via
      a user interface.
    * Data consumption: the results the program produces need to be made available for human consumption or transferred
      to other applications for further processing.

## Structured vs unstructured data

* **Unstructured data**, there is generally more flexibility in what it can contain, but there is little organisation of
  the data and no semantic information (metadata). Plain text .txt and .CSV files are examples of this.
* **Structured data** contains embed semantics about what the data is and how it is related to other bits of data.
  Relational databases such as MySQL or Oracle provide a sophisticated level of structure, organisation and
  relationships.
* **Semi-structured data** can be achieved in files using various mark-languages such as XML (eXtensible Mark-up
  Language) and OWL (Web Ontology Language). These provide a degree of semantics and/or metadata. HTML (Hypertext
  Mark-up Language) is perhaps the most prolific file format in use today, which provides the browser with structural
  information about the data, with CSS (Cascading Style Sheets) providing layout instructions for that structure.

## MetaData

* One of the key advantages of using structured or semi-structured data is that it provides information about that data.
* The term metadata means “data about data” and is used to refer to this sort of information.
    * For example, the string “79 North Goldfield Avenue.” is just a collection of characters to a computer. However, if
      we provided some metadata around the string such as <address>“79 North Goldfield Avenue.”</address> some meaning (
      in a rudimentary way) can be inferred by the computer, or more specifically, by the program being run on the
      computer.
* This type of metadata is referred to as 'mark-up'. Other forms of metadata exist such as the creation and last edited
  date stamps generated by Microsoft word documents.

## Plain txt

* Plain text files are exactly that - no formatting, no styling, just a string of symbols.

## docX

* Document files like those produced by word processors (MS Word, Pages and OpenOffice) contain extra information to
  give the contents structure and style. They also have metadata attached about the creation and editing of the file.
  Previous versions of this file type .doc use a proprietary format from Microsoft which requires a specific parser to
  handle. The current version .docX is based on XML, making it much easier to access and manipulate in non-Microsoft
  applications.

# Comma Separated Values .CSV

* This is a common file structure used for large data sets requiring little or no semantic information or metadata
  </br><img src="./img/2/5.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/6.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/7.png" alt="alt text" width="500" height="300"></br>

# eXtensible Mark-up Language .XML

* XML was developed in the 1970's and is a language that is able to describe data in many ways, providing strong
  semantic information, and other metadata.
* However, it is often perceived as difficult to handle and overly complex. Many common formats such as HTML and .docX
  have been derived from XML’s approach to structuring documents.
* XML validation:
* The first, a DTD, known as a Document Type Definition is a simple set of syntax for describing the relationship
  between parent and child elements, and which attributes belong to which tags. The second method for validation is to
  use an XML Schema. This is a validation document that is itself written in XML. This enables it to be highly
  extensible and take advantage of the XML structure. It is much easier to maintain than a DTD. Both these documents, a
  DTD and XML Schema serve the purpose of being used by a program to validate the correctness of an XML document  
  </br><img src="./img/2/8.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/9.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/10.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/11.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/12.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/13.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/14.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/15.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/16.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/17.png" alt="alt text" width="500" height="300"></br>

## JavaScript Object Notation .JSON

* JSON was developed in response to the growing need for a lightweight data transfer structure in asynchronous internet
  communications.
* Originally designed to work with JavaScript it now has a growing following, and support for it has been developed in
  many other languages, including Python.

## .yaml

* YAML Ain't Markup Language (Links to an external site.) (a recursive acronym) is similar in many ways to JSON in being
  lightweight and breaking away from the complexity of languages like XML.
* It extends the functionality of JSON by providing structures like Maps. Like Python, indentation is used to provide
  structure and meaning within the syntax, making this a human-readable format
  </br><img src="./img/2/18.png" alt="alt text" width="500" height="300"></br>
  </br><img src="./img/2/19.png" alt="alt text" width="500" height="300"></br>

## HDF5 format

* This file format is specifically designed for storing large quantities of scientific data, within groups and
  subgroups. While not in general use compared to some of the above file formats it is used with specialist areas of
  science. HDF stands for hierarchical data format. This format provides the facility for metadata and is designed to
  support data compression.

# File input and output

## Relative and Absolute Paths

* There are two ways to define a path to a file or folder.
    * Absolute path: the whole folder structure is given, starting at the root/drive element.
        * “C:Work\Uni\Code\File.txt”
    * Relative path: a path is defined from the perspective of the current position in the path.
        * “File.txt”
        * To get to it from a relative perspective the program has to go up one level to Code and then back down into
          data to get to the file. To do this the relative path starts with ../ to indicate the jump up the structure.
        * “..\Data\File.txt”

</br><img src="./img/2/20.png" alt="alt text" width="500" height="300"></br>

## Hidden characters

* The lesson on encoding demonstrated that key strokes such as tabs and line feeds (LF) are all present as symbols
  within the text. These characters are invisible when a text file is viewed in a standard text editor. They are often
  referred to as non-printing characters. However, they are an important part of the structure of the document and a
  symbol that can be identified within a text file by a program, given its encoding.

## Reading from a file

* To read from a file the open() command is used, which returns a file object.

```
open(file, mode, buffering, encoding, errors, newline, closefd, opener) 
```

* The first parameter is the path of the file and is always required.
* The default value for mode is ‘r’, which is used when no explicit flag is given.
* The third parameter is an integer value that indicates whether or not a buffer will be used.
* Text files default to 1, line buffering. Other possible values are given BELOW

``` 
In [1]: file = open("Pop_Goes_The_Weasel.txt")
In [2]: file.readline()
Out[2]: 'Half a pound of tuppenny rice,\n'

In [3]: file.readline()
Out[3]: 'Half a pound of treacle.\n
```

* The whole file can be read at once by using the read() function as demonstrated here:

``` 
In [4]: file = open("Pop_Goes_The_Weasel.txt")
In [5]: file.read()
Out[5]: 'Half a pound of tuppenny rice,\nHalf a pound of treacle.\nThat’s the way the money goes,\nPop! goes the weasel.\n'
```

* The method read() can take an integer parameter that indicates how many characters to read in at a time:

``` 
In [8]: file = open("Pop_Goes_The_Weasel.txt")
In [9]: print(file.read(10))
Half a pou
```

* The file object can also be passed to a 'for loop' to iterate over each line at a time (perform multiple reads) and
  stop when it reaches the end of the file:

``` 
In [10]: file = open("Pop_Goes_The_Weasel.txt")
In [11]: for line in file:
    ...:     temp = line.rstrip('\n')
    ...:     print(f"** {temp:32}  **")
    ...:
** Half a pound of tuppenny rice,    **
** Half a pound of treacle.          **
** That’s the way the money goes,    **
** Pop! goes the weasel.             **
```

## Writing to a file

* To write to a file the same function is called, open(), but this time a mode must be indicated.
* When writing to a file there are four possible actions that may need to be performed:
    * Start writing at the beginning of a file, with all existing content being overwritten.
    * Start writing at the beginning of a new (empty) file.
    * Start writing at the end of an existing file
    * Start writing at a specific point within a file, so some existing content is kept, and some is overwritten.

* The returned value 28 indicates how many characters were written to the file.
* The code below completes as the file “Humpty_Dumpty.txt” does not exist, so a new one is created and then written too.

``` 
In [12]: file = open("Pop_Goes_The_Weasel.txt", 'w')
In [13]: file.write("Humpty Dumpty sat on a wall.")
Out[13]: 28


In [17]: file = open("Humpty_Dumpty.txt", 'w')
In [18]: file.write("Humpty Dumpty sat on a wall.")
Out[18]: 28

In [19]: file.write("Humpty Dumpty had a great fall.")
Out[19]: 31

In [20]: file.write("All the king's horses and all the king's men")
Out[20]: 44

In [21]: file.write("Couldn't put Humpty together again.")
Out[21]: 35

In [22]: file.close()

```

* The second action is slightly more complicated as there is a need to check if the file exists so that data is not
  accidentally erased. Fortunately, Python has been designed to accommodate this and comes with an exclusive flag ‘x’
  that fails to write if the file exists:
    * In the example above, the code throws an exception, FileExistsError, as the file exists.

```
In [16]: file = open("Pop_Goes_The_Weasel.txt", 'x')
-------------------------------------------------------------------------

FileExistsError                           Traceback (most recent call last)
<ipython-input-45-f7523625772f> in <module>()
----> 1 file = open("Pop_Goes_The_Weasel.txt", 'x')

FileExistsError: [Errno 17] File exists: 'Pop_Goes_The_Weasel.txt
```

* The third action, **appending (retain the existing file content and add more to it) to the end of an existing file**, uses
  the character flag ‘a’.
    * However, here the file has to exist and if it does not a FileNotFoundError exception will be generated.

``` 
In [23]: file = open("Humpty_Dumpty.txt", 'a')
In [24]: file.write("Half a pound of tuppenny rice,\n")
Out[24]: 31

In [25]: file.write("Half a pound of treacle.\n")
Out[25]: 25

In [26]: file.close()
In [27]: file = open("Humpty_Dumpty.txt")
In [28]: for line in file:
    ...:     print(line)
    ...:     
Humpty Dumpty sat on a wall.
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.
Half a pound of tuppenny rice,
Half a pound of treacle.
```
* Depending on what the program requires, there may be a need to temporarily store parts of the file, or use regular expressions (see lesson 5) to find, change or extract parts of the file.
* Here is an example that keeps the first two lines of the new nursery rhyme and adds two (overwriting the existing content) from the previous nursery rhyme.
```
In [29]: file = open("Pop_Goes_The_Weasel.txt", 'r+')
In [30]: print("File pointer: ", file.tell())
File pointer:  0

In [31]: for line in file:
   ...:     print(line)
   ...:     
Half a pound of tuppenny rice,
Half a pound of treacle.
That's the way the money goes,
Pop! goes the weasel.

In [32]: print("File pointer: ", file.tell())
File pointer:  109

In [33]: file.seek(56,0)
Out[33]: 56

In [34]: file.write("All the king's horses and all the king's men\n")
Out[34]: 45

In [35]: print("File pointer: ", file.tell())
File pointer:  101

In [36]: file.write("Couldn't put Humpty together again.\n") 
Out[36]: 36

In [37]: print("File pointer: ", file.tell())
File pointer:  137

In [38]: file.seek(0,0)
Out[38]: 0

In [39]: for line in file:
    ...:     print(line)
    ...:    
Half a pound of tuppenny rice,
Half a pound of treacle.
All the king's horses and all the king's men
Couldn't put Humpty together again.
```


# TODO

* Padmanabhan T. R. (2016) Programming with Python. Undergraduate Topics in Computer Science. Springer, Cham Sections:
  7.1-7.2
* Beazley. D., Jones B. K.  (2013) Python Cookbook. 3rd Ed. O'Reilly Media, Sections: 6.9-6.10
* McKinney W. (2017) Python for Data Analysis. 2nd Ed. O'Reilly Media. Section 6.2
* Beazley. D., Jones B. K.  (2013) Python Cookbook. 3rd Ed. O'Reilly Media: 6.1-6.7 (Links to an external site.)

 