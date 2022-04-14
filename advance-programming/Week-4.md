#### Main Topics

* understanding the NumPy and pandas' APIs for data analysis
* introducing the concept of data cleaning.

#### Sub titles:

# Mathematics refresher

## Descriptive statistics

* Read the following chapters which cover the measures of central tendency and measures of spread:
    * [Chapter 2 in Hinton, P, R. (2014) Statistics explained. London: Routledge](https://ebookcentral.proquest.com/lib/york-ebooks/reader.action?docID=1656789&ppg=24)
    * [Chapter 4 & 5 in Diamond, Ian., and Jefferies, J. (2001) Beginning Statistics: An Introduction for Social Scientists. Routledge](https://methods-sagepub-com.libproxy.york.ac.uk/book/beginning-statistics/n5.xml)

* mean
* mode
* median
* variance
* standard deviation
* quartile
* percentile
* normal distribution
* positive skew
* negative skew

## Set Theory

* Read the following chapter which covers set theory to some depth, not all are required:
    * [Chapter 2 (pp. 23-41) in O’Regan G. (2013) Mathematics in Computing London: Springer-Verlag](https://link-springer-com.libproxy.york.ac.uk/content/pdf/10.1007/978-1-4471-4534-9.pdf)

* set
* subset
* universal set
* union
* intersection
* algebra of sets

## Matrix mathematics

* Read the following pages which cover set theory to some depth, not all are required:
    * Pages 149-184 in Vince J. (2015) Matrices. In: Foundation Mathematics for Computer Science. Springer, Cham
    * Chapter 13, (pp 223-233) in O’Regan G. (2013) Mathematics in Computing London Springer-Verlag

* addition and multiplication
* matrix decompositions

## Regression and correlation

* Read the following chapter which covers regression and correlation techniques:
    * Chapter 20 in Hinton, P, R. (2014) Statistics explained. London: Routledge

* regression
* correlation

## Probability

* Read the following pages and pay close attention to the following terms and how they are used: independent and
  dependent probability.
    * Chapter 12, Section 12.4 in O’Regan G. (2013) Mathematics in Computing London: Springer-VerlagLinks to an external
      site.

* independent probability
* dependent probability.

### Further reading

* [Cramer, D., and Howitt, D.(Editors) (2004) The SAGE Dictionary of Statistics](https://eu.alma.exlibrisgroup.com/leganto/readinglist/citation/37246671830001381?institute=44YORK_INST&auth=SAML)

# NumPy

* NumPy is an API APIs in Python that support the cleaning and analysis of very large data sets with more efficiency
  than standard Python structures
* NumPy contains a highly effective way of managing data in single and multi-dimensional arrays.
* Resiurces:
    * [NumPy Documentation](https://numpy.org/)
    * [Anaconda installing packages guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)

* NumPy is a well developed and large library containing a wide range of functionality including:
    * A high-performance multidimensional array the ndarray
    * Functions for generating random values for testing and dummy data
    * New data types to express numbers more effectively with scalar and dtype
    * A plethora of mathematical functions (ufunc) that can be applied to all the values in the array
* Many more specialised mathematical techniques, and packages for connecting to other systems, languages and data
  sources.

* Python for Data Analysis, 2nd Edition, chapter 4 has so many examples for NumPy

# Pandas

* Panda is API that supports the analysis of large data sets.
* Like NumPy it provides specialist data structures, two this time the Series and DataFrame, and a range of functions
  that make it easier to manipulate, update and perform calculations with that data.
* Resources:
    * [Pandas](https://pandas.pydata.org/)
* pandas is a well-developed library with a large supporting open source community. It is being continually developed as
  new requirements for data scientists come to light.
    * two specialised data sets, Series for handling single labelled (key:value) data in a single row, and DataFrame for
      handling tabulated data, with column and row headers
    * integration with NumPy so that many of the functions there can be used with pandas objects
    * an extended set of statistical functions, including correlation and covariance, as well as being able to generate
      all common statistics from one function
    * set functions for determining membership and describing data in terms of counts and unique values.

* Python for Data Analysis, 2nd Edition, chapter 5 has so many examples for Pandas

# Preparing for data analysis

* make data analysis easier and consistent, data needs to be cleaned and anomalies handled effectively.

## Data reading and writing

* data needs to be read into programs and stored externally from the program. This requires reading and writing files,
  sometimes in very specific formats such as .CSV and .JSON. pandas provides a range of built-in functions for reading
  and writing data from various file types into a DataFrame. There are a number of optional parameters that can be set
  to tailor the transfer of data to specific requirements, such as managing missing data, skipping or retrieving headers
  for rows/columns, and combining data prior to entry into the DataFrame.

* Python for Data Analysis, 2nd Edition, chapter 6.1 of Python for Data Analysis that discusses and demonstrates the
  functionality provided by pandas for reading and writing from files into DataFrames. Much of the theory here in
  relation to data encoding and file formats have already been covered.

## Serialization

* Serialization is the process of storing and retrieving program objects, to and from a binary representation. Python
  provides an API called pickle (pickling an object is to serialize it) for this purpose, and pandas objects can access
  this through the to_pickle() method.
* Python for Data Analysis, 2nd Edition, Investigate the pickle() method (section 6.2Links to an external site. of
  Python for Data Analysis is a good place to start) and find examples of different objects that can be/have been
  pickled. Practice pickling and unpickling different objects in Python.

## Cleaning data

* When facing a new data analysis task, the first thing to do is get familiar with the data set that will be used. The
  next thing is to consider what parts of the data set are required to satisfy an information need. This may be as
  simple as portioning the data, it also may include cleaning and reshuffling the date. First, consider how data may
  need to be cleaned.
    * Removing missing data
    * Removing duplicate data
    * Replacing values
    * Renaming axis
    * Discretization and Binning
    * Removing outliers
* Python for Data Analysis, 2nd Edition, 7.1 and 7.2 to find out more about data cleaning and transformation.

# Note:

* Cleaning data:  Week 4 Codes in [here](./codes/4/Wk4_Activity_Example_Solutions/week4_act3_ex1.ipynb)

# Production

## Design:

* Consider the steps required for cleaning and shaping and any of the calculations (functions) you want to develop.
  Write pseudocode to sketch these out before you write code. Mentally or on paper walk the data through your pseudocode
  steps to test how effective your solution is.

## Implementation:

* The first stage is to clean the data and make sure it is fit for purpose. Examine the data careful to identify
  anomalies and then consider how your program can identify these and correct/delete or change. You will need to
  consider how you are going to handle erroneous or missing values. You should output a sample of the data that
  demonstrates how cleaning has changed the data.

* The next stage is to reshape the data as per any requirements of the brief. Is all the data needed to provide the
  required results? Is any of it duplicated? Is there data across different sources that needs to be brought together?
  Again, output a sample to the console to demonstrate how this has changed the structure of the data.

* Finally develop and test a set of functions (or objects and methods) that applies the statistical analysis to the data
  set, outputting the results to the console.

* Capture the results of your data cleaning, shaping and functions with screenshots of the consol. There is no
  requirement at this stage for anything to be functioning in through the GUI. Make sure it is clear what your output is
  testing/demonstrating (output simple informative statements).

## Reflection on design decisions:

* Write a 200-word reflection that states why you have selected specific tools from NumPy or pandas. This may be the
  data structure you have used, the functions you have applied to clean and shape the data. Clearly identify which
  specific aspects of the requirements or data’s structure informed the decisions. You should consider what literature
  supports your reasoning/decisions.