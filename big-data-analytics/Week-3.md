#### Main Topics

After completing this week you should be able to:

* Evaluate the suitability of given data for use in analysis
* Transform and clean simple tabular data using several common techniques
* Extract and create features from simple tabular data
* Integrate data from diverse sources (including multiple tables)

* After completing this week, you will have made significant steps towards achieving the following module learning
  outcomes:
    * MO2 — Manipulate a data set to extract statistics and features

#### Sub titles:

* [Evaluating the suitability of given data for use in analysis](#evaluating-the-suitability-of-given-data-for-use-in-analysis)
* [ARFF files](#arff-format-attribute-relation-file-format)

# Evaluating the suitability of given data for use in analysis

* Week 1 [What are data and what is a data set ?] title.

# ARFF Format (attribute-relation file format)

<img src="./img/3/1.png" alt="alt text" width="500" height="300">

* Lines beginning with a % sign are comments.
* @relation tels the name of the data (weather)
* @attributes defines attributes (outlook, temperature, humidity, windy, play?).
    * Nominal attributes are followed by the set of values they can take on, enclosed in curly braces.
    * Values can include spaces; if so, they must be placed within quotation marks.
    * Numeric values are followed by the keyword numeric.
    * the class attribute is not distinguished in any way in the data file.
* @data line that signals the start of the instances in the dataset.
    * Instances are written one per line, with values for each attribute in turn, separated by commas.
    * If a value is missing it is represented by a single question mark (there are no missing values in this dataset).
* ARFF has 5 different attribute types:
    * numeric
    * nominal
    * string attributes
        * String attributes have values that are textual.
        * String attributes can have values that are very long—even a whole document.
    * date attributes
        * Weka uses the ISO-8601 combined date and time format yyyy-MM-dd’T’HH:mm:ss
    * relation-valued attributes
        * they allow multi-instance problems to be represented in ARFF format

```
@attribute bag relational
    @attribute outlook {sunny, overcast, rainy} @attribute temperature numeric
    @attribute humidity numeric
    @attribute windy {true, false}
@end bag
```

* Note, however, that in multi-instance learning the order in which the instances is given is generally considered
  unimportant. An algorithm might learn that cricket can be played if none of the days is rainy and at least one is
  sunny, but not that it can only be played in a certain sequence of weather events.

<img src="./img/3/2.png" alt="alt text" width="500" height="300">

## Sparce Data

* Sometimes most attributes have a value of 0 for most of the instances, ie market basket data showing the purchased
  items will have a lot 0 for all the other items in the stock.
    * Another example is text mining where attributes are the words that occur in the documents.
* Sparse data files have the same @relation and @attribute tags, followed by an @data line, but the data section is
  different and contains specifications in braces such as those shown previously.
    * Instead of '0, X, 0, 0, 0, 0, Y, 0, 0, 0, “class A”', '{1 X, 6 Y, 10 “class A”}' saves space.
* Note that the omitted values have a value of 0—they are not “missing” values! If a value is unknown, it must be
  explicitly represented with a question mark.

## Attribute Types

* How an attribute is processed during cleanup also depends on how the model is going to treat that value. For example,
  if a numerical value is going to be used as numerical or ordinal.
* If a learning scheme treats numeric attributes as though they are measured on ratio scales, the question of
  normalization arises.
    * Attributes are often normalized to lie in a fixed range—usually from zero to one—by dividing all values by the
      maximum value encountered or
    * By subtracting the minimum value and dividing by the range, max-min.
    * Another normalization technique is to subtract the mean from each value and divide the result by the standard
      deviation.
        * This process is called standardizing a statistical variable and results in a set of values whose mean is zero
          and the standard deviation is one.
* For distance-based algorithms, nominal attributes can be converted to synthetic binary attributes, ie for
  sunny/cloudy/rainy, we use one binary attribute for each.
* Sometimes there is a genuine mapping between nominal attributes and numeric scales, ie the Zipcode or the leading
  digits of phone number and the geolocation.

## Missing Values

* [Understand Missing data and 5 ways to handle!](https://www.youtube.com/watch?v=sUAMiAIUhcI)
* Missing values are usually indicated with a number that normally cannot appear for that attribute, ie -1 or 0.
    * Different missing values can be distinguished by different values, ie -1: non-recorded, -2: irrelevant etc.
    * For nominal attributes, missing values may be indicated by blanks or dashes. Sometimes different kinds of missing
      values are distinguished (e.g., unknown vs unrecorded vs irrelevant values) and perhaps represented by different
      negative integers (21, 22, etc.).
* When a value is missing, the question that should be asked is, is it missing just as a random event or a decision was
  taken not to carry out a particular measurement as a result of a problem with the specimen.

* Imputation is t put most reasonable value in missing data, for example salary info 5000 euro for missing value.

<img src="./img/3/3.png" alt="alt text"><br>
<img src="./img/3/4.png" alt="alt text">

## Inaccurate values

* It is important to check data mining files carefully for rogue attributes and attribute values. The data may not have
  been explicitly collected for that purpose.
* Typographic errors, ie spelling variations of a nominal attribute, extra spaces, upper/lower cases mismatches etc
  would lead to possible extra values.
    * To spot such issues, frequency tables as below and histograms can be useful.
* Typographical or measurement errors in numeric values generally cause outliers that can be detected by graphing one
  variable at a time.
    * Some incorrect values can be easy to spot due to huge variations from the rest but other times, this might require
      good domain knowledge.
* Duplicate data is another potential source of the problem, ie duplication of records leads to most ML algos giving
  them more weight.

<img src="./img/3/4.png" alt="alt text">

## Unbalance Data

* In practical applications of classification schemes, it is very often the case that one class is far more prevalent
  than the others. For example, when predicting the weather in Ireland, it is pretty safe to predict that tomorrow will
  be rainy rather than sunny. Given a dataset in which these two values form the class attribute, with information
  relevant to the forecast in the other attributes, excellent accuracy is obtained by predicting rainy regardless of the
  values of the attributes.

* Always predicting the majority outcome rarely says anything interesting about the data. The problem is that raw
  accuracy, measured by the proportion of correct predictions, is not necessarily the best criterion of success. In
  practice, different costs may be associated with the two types of error.

## Getting to know your data

* Simple tools that show histograms of the distribution of values of nominal attributes, and graphs of the values of
  numeric attributes (perhaps sorted or simply graphed against instance number), are very helpful.
    * These graphical visualizations of the data make it easy to identify outliers, which may well represent errors in
      the data file—or arcane conventions for coding unusual situations, such as a missing year as 9999 or a missing
      weight as 21 kg, that no one has thought to tell you about
* Domain experts need to be consulted to explain anomalies, missing values, the significance of integers that represent
  categories rather than numeric quantities, and so on. Pairwise plots of one attribute against another, or each
  attribute against the class value, can be extremely revealing.
* In a large database, you should sample a few instances and examine them carefully.

# Cleaning Data

* 5 Principles
    * You can't fix problems until you can see them
        * Some within range values can still be problematic if they are repeated erroneously or put in by someone to
          fix 'missing' value, ie using the mean or median for this purpose.
        * So, looking for suspicious repeating values, especially with decimal places.
    * Don't' fix problems by making things worse
        * Refrain from making 'fixes' that might distort the statistics.
    * Justify your fixes
    * Sometimes you shouldn't fix
        * Even if they won't like to hear it, be honest to the audience and don't attempt to fix things that you
          actually can't.
    * Acknowledge residual uncertainty
* Data should be cleansed when acquired for many reasons:
    * Not everyone spots the data anomalies. Decision-makers may make costly mis- takes on information based on
      incorrect data from applications that fail to cor- rect for the faulty data.
    * If errors are not corrected early on in the process, the cleansing will have to be done for every project that
      uses that data.
    * Data errors may point to a business process that isn’t working as designed. we discovered clients who abused the
      couponing system and earned money while purchasing groceries.
    * Data errors may point to defective equipment, such as broken transmission lines and defective sensors.
    * Data errors can point to bugs in software or in the integration of software that may be critical to the company.

<img src="./img/3/6.png" alt="alt text"></br>
<img src="./img/3/7.png" alt="alt text"></br>
<img src="./img/3/8.png" alt="alt text"></br>

