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

<img src="./img/3/3.png" alt="alt text" width="500" height="300"><br>
<img src="./img/3/4.png" alt="alt text" width="500" height="300">

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

<img src="./img/3/4.png" alt="alt text" width="500" height="300">

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
    * Not everyone spots the data anomalies. Decision-makers may make costly mistakes on information based on incorrect
      data from applications that fail to correct for the faulty data.
    * If errors are not corrected early on in the process, the cleansing will have to be done for every project that
      uses that data.
    * Data errors may point to a business process that isn’t working as designed. we discovered clients who abused the
      couponing system and earned money while purchasing groceries.
    * Data errors may point to defective equipment, such as broken transmission lines and defective sensors.
    * Data errors can point to bugs in software or in the integration of software that may be critical to the company.

<img src="./img/3/6.png" alt="alt text" width="500" height="300"></br>
<img src="./img/3/7.png" alt="alt text" width="500" height="300"></br>
<img src="./img/3/8.png" alt="alt text" width="500" height="300"></br>

## Improving Decision Tree

* Decision trees induced from training data can often be simplified, without loss of accuracy, by discarding
  misclassified instances from the training set, relearning, and then repeating until there are no misclassified
  instances.
    * Experiments show that this hardly affects the classification accuracy but significantly simplifies the DT.
    * This method also helps to verify the subtree pruning and also gives a chance to review the misclassified records
      as they might erroneous in the first place anyway.

* Tackling the noise
    * If there is attribute noise present in the training data, instead of trying to remove it, a similar noise should
      be added to the training data as well. So, training on noisy data but testing on noise-free should be avoided.
      This is more realistic as real-life attributes are likely to contain noise too.
    * If there is class noise, however, then this should either be removed or data with noise-free classes should be
      collected. But with class noise (rather than attribute noise), it is best to train on noise free instances if
      possible.

## Robust regression

* The problems caused by noisy data have been known in linear regression for years. Statisticians often check data for
  outliers and remove them manually.
    * Outliers dramatically affect the usual least-squares regression because the squared distance measure accentuates
      the influence of points far away from the regression line.

* Statistical methods that address the problem of outliers are called robust.
    * One way of making regression more robust is to use an absolute-value distance measure instead of the usual squared
      one.
        * This weakens the effect of outliers.
    * Another possibility is to try to identify outliers automatically and remove them from consideration.
        * For example, one could form a regression line and then remove from consideration those 10% of points that lie
          furthest from the line
    * A third possibility is to minimize the median (rather than the mean) of the squares of the divergences from the
      regression line.
        * It turns out that this estimator is very robust and actually copes with outliers in the X-direction as well as
          outliers in the Y-direction—which is the normal direction one thinks of outliers.

* Here the anomalous group is because they store calls total number of minutes not counts.
  <img src="./img/3/8.png" alt="alt text" width="500" height="300"></br>

* The least median of squares line lies at the exact center of this band. Note that this notion is often easier to
  explain and visualize than the normal least-squares definition of regression.
    * Unfortunately, there is a serious disadvantage to median-based regression techniques: they incur high
      computational cost, which often makes them infeasible for practical problems.

## Detecting Anomalies

* Auto-detection of outliers/anomalies is prone to errors, especially if a human expert isn't consulted
    * In statistical regression, visualizations help.
    * most classification problems cannot be so easily visualized: the notion of “model type” is more subtle than a
      regression line.
    * One solution that has been tried is to use several different learning schemes— such as a decision tree, and a
      nearest-neighbor learner, and a linear discriminant function—to filter the data.
    * Training all three schemes on the filtered data and letting them vote can yield even better results.
        * However, there is a danger to voting techniques: some learning algorithms are better suited to certain types
          of data than others, and the most appropriate scheme may simply get out-voted!

    * Method of combining the output from different classifiers, called stacking in Ensemble learning.

* One possible danger with filtering approaches is that they might conceivably just be sacrificing instances of a
  particular class (or group of classes) to improve accuracy on the remaining classes
* Automatic filtering is a poor substitute for getting the data right in the first place. And if this is too
  time-consuming and expensive to be practical, human inspection could be limited to those instances that are identified
  by the filter as suspect.

## One Class Learning

* If during training, there is only one class is available but prediction data presents records for unknown classes,
  then the one-class learner groups them as target/known and unknown classes.

## Outlier Detection

* One-class classification is often called outlier (or novelty) detection because the learning algorithm is being used
  to differentiate between data that appears normal and abnormal with respect to the distribution of the training data.
* A generic statistical approach to one-class classification is to identify outliers as instances that lie beyond a
  distance d from a given percentage p of the training data.
    * Alternatively, a probability density can be estimated for the target class by fitting a statistical distribution,
      such as a Gaussian, to the training data; any test instances with a low probability value can be marked as
      outliers.
    * If an appropriate distribution for the data at hand cannot be identified, one can adopt a non-parametric approach
      such as kernel density estimation.
        * An advantage of the density estimation approach is that the threshold can be adjusted at prediction time to
          obtain a suitable rate of outliers.
* Multi-class classifiers can be tailored to the one-class situation by fitting a boundary around the target data. * If
  the boundary is chosen too conservatively, data in the target class will erroneously be rejected. If it is chosen too
  liberally, the model will over-fit and reject too much legitimate data.

## Generating Arificial Data

* The most straightforward approach is to generate uniformly distributed data and learn a classifier that can
  discriminate this from the target.
    * However, different decision boundaries will be obtained for different amounts of artificial data.
    * To overcome this, rather than classifiers, class probability estimators such as bagged decision trees can be used.
      Then, the threshold level of the probability estimator can be adjusted as needed.
* There is one significant problem. As the number of attributes increases, it quickly becomes infeasible to generate
  enough artificial data to obtain adequate coverage of the instance space, and the probability that a particular
  artificial instance occurs inside or close to the target class diminishes to a point that makes any kind of
  discrimination impossible.
    * The solution is to generate artificial data that is as close as possible to the target class. In this case,
      because it is no longer uniformly distributed, the distribution of this artificial data—call this the “reference”
      distribution—must be taken into account when computing the membership scores for the resulting one-class model.
        * In other words, the class probability estimates of the two-class classifier must be combined with the
          reference distribution to obtain membership scores for the target class.

# Attribute Selection

* Experiments with a decision tree learner (C4.5) have shown that adding to standard datasets a random binary attribute
  generated by tossing an unbiased coin impacts classification performance, causing it to deteriorate (typically by 5 or
  10% in the situations tested)

* As you proceed further down the tree, less and less data is available to help make the selection decision. At some
  point, with little data, the random attribute will look good just by chance. Because the number of nodes at each level
  increases exponentially with depth, the chance of the rogue attribute looking good somewhere along the frontier
  multiplies up as the tree deepens.
    * The real problem is that you inevitably reach depths at which only a small amount of data is available for
      attribute selection. This is known as the fragmentation problem. If the dataset were bigger it wouldn’t
      necessarily help—you’d probably just go deeper.

* The fact that irrelevant distracters degrade the performance of decision tree and rule learners is, at first,
  surprising. Even more surprising is that relevant attributes can also be harmful.
    * The problem is that the new attribute is (naturally) chosen for splitting high up in the tree. This has the effect
      of fragmenting the set of instances available at the nodes below so that other choices are based on sparser data.
* Because of the negative effect of irrelevant attributes on most machine learning schemes, it is common to precede
  learning with an attribute selection stage that strives to eliminate all but the most relevant attributes.
    * The best way to select relevant attributes is manually, based on a deep understanding of the learning problem and
      what the attributes actually mean.

* More importantly, dimensionality reduction yields a more compact, more easily interpretable representation of the
  target concept, focusing the user’s attention on the most relevant variables.

## Scheme Independent Selection

* When selecting a good attribute subset, there are two fundamentally different approaches.
    * One is to make an independent assessment based on general characteristics of the data;
        * This is called the filter method, because the attribute set is filtered to produce the most promising subset
          before learning commences.
    * the other is to evaluate the subset using the machine learning algorithm that will ultimately be employed for
      learning
        * This is the wrapper method, because the learning algorithm is wrapped into the selection procedure.

* One simple scheme-independent method of attribute selection is to use just enough attributes to divide up the instance
  space in a way that separates all the training instances.

* Machine learning algorithms can be used for attribute selection. For instance, you might first apply a decision tree
  algorithm to the full dataset, and then select only those attributes that are actually used in the tree. While this
  selection would have no effect at all if the second stage merely built another tree, it will have an effect on a
  different learning algorithm.
    * Often the decision tree performs just as well when only the two or three top attributes are used for its construc-
      tion—and it is much easier to understand.

* Another possibility is to use an algorithm that builds a linear model—e.g., a linear support vector machine—and ranks
  the attributes based on the size of the coefficients. A more sophisticated variant applies the learning algorithm
  repeatedly. It builds a model, ranks the attributes based on the coefficients, removes the lowest-ranked one, and
  repeats the process until all attributes have been removed.
    * This method of recursive feature elimination has been found to yield better results on certain datasets (e.g.,
      when identifying important genes for cancer classification) than simply ranking attributes based on a single
      model.

* Attributes can be selected using instance-based learning methods too. You could sample instances randomly from the
  training set and check neighboring records of the same and different classes—“near hits” and “near misses.” If a near
  hit has a different value for a certain attribute, that attribute appears to be irrelevant and its weight should be
  decreased. On the other hand, if a near miss has a different value, the attribute appears to be relevant and its
  weight should be increased.

* Another way of eliminating redundant attributes as well as irrelevant ones is to select a subset of attributes that
  individually correlate well with the class but have little intercorrelation.

## Searching Attributes in space

* Most methods for attribute selection involve searching the space of attributes for the subset that is most likely to
  predict the class best. Fig. 8.1 illustrates the attribute space for the—by now all-too-familiar—weather dataset. The
  number of possible attribute subsets increases exponentially with the number of attributes, making exhaustive search
  impractical on all but the simplest problems.

* The downward direction, where you start with no attributes and add them one at a time, is called **forward selection**
  . The upward one, where you start with the full set and delete attributes one at a time, is **backward elimination**.

* In forward selection, each attribute that is not already in the current subset is tentatively added to it, and the
  resulting set of attributes is evaluated—using, e.g., cross-validation as described in the following section. This
  evaluation produces a numeric measure of the expected performance of the subset. The effect of adding each attribute
  in turn is quantified by this measure, the best one is chosen, and the procedure continues. However, if no attribute
  produces an improvement when added to the current subset, the search ends.

* Forward selection and backward elimination can be combined into a bidirectional search; again one can either begin
  with all the attributes or with none of them.

## Scheme Spesific Selection

* The performance of an attribute subset with scheme-specific selection is measured in terms of the learning scheme’s
  classification performance using just those attributes.

* The entire attribute selection process is rather computation intensive. If each evaluation involves a 10-fold
  cross-validation, the learning procedure must be executed 10 times.

* One way to accelerate the search process is to stop evaluating a subset of attributes as soon as it becomes apparent
  that it is unlikely to lead to higher accuracy than another candidate subset. This is a job for a paired statistical
  significance test, performed between the classifier based on this subset and all the other candidate classifiers based
  on other subsets. The performance difference between two classifiers on a particular test instance can be taken to be
  21, 0, or 1 depending on whether the first classifier is worse, the same as, or better than the second on that
  instance. A paired t-test can be applied to these figures over the entire test set, effectively treating the results
  for each instance as an independent estimate of the difference in performance.

* A simple method for accelerating scheme-specific search is to preselect a given number of attributes by ranking them
  first using a criterion like the information gain and discarding the rest before applying scheme-specific selection.

* Whatever way you do it, scheme-specific attribute selection by no means yields a uniform improvement in performance.
  Because of the complexity of the process, which is greatly increased by the feedback effect of including a target
  machine learning algorithm in the attribution selection loop, it is quite hard to predict the conditions under which
  it will turn out to be worthwhile. As in many machine learning situations, trial and error using your own particular
  source of data is the final arbiter.

# Data Preparation and integration

* Data integration involves taking the data from different data sources and merging them to give a unified view of the
  data from across the organization.
    * For example patient information can store differant hospital seperately, the important part of it to integrate
      correctly those data of one patient.

* The first three CRISP-DM stages take up to 70 to 80 percent of the total data science project time, with the majority
  of this time being allocated to data integration.

* Integrating data from multiple data sources is difficult even when the data are structured.
    * However, when some of the newer big-data sources are involved, where semi- or unstructured data are the norm, then
      the cost of integrating the data and managing the architecture can become significant

* The typical data-integration process will involve a number of different stages, consisting of extracting, cleaning,
  standardizing, transforming, and finally integrating to create a single unified version of the data.
    * Extracting data from multiple data sources can be challenging because many data sources can be accessed only by
      using an interface particular to that data source. As a consequence, data scientists need to have a broad skill
      set to be able to interact with each of the data sources in order to obtain the data
    * Once data have been extracted from a data source, the quality of the data needs to be checked. Data cleaning is a
      process that detects, cleans, or **removes corrupt or inaccurate data from the extracted data**.
        * For example, customer address information may have to be cleaned in order to convert it into a standardized
          format. In addition, there may be duplicate data in the data sources, in which case it is necessary to
          identify the correct customer record that should be used and to remove all the other records from the data
          sets.
    * It is important to ensure that the values used in a data set are consistent.
        * For example, one source application might use numeric values to represent a customer credit rating, but
          another might have a mixture of numeric and character values.

    * The other representations should be mapped into the standardized representation.
        * For example, imagine one of the attributes in the data set is a customer’s shoe size. Customers can buy shoes
          from various regions around the world, but the numbering system used for shoe sizes in Europe, the United
          States, the United Kingdom, and other countries are slightly different
        * Prior to doing data analysis and modeling, these data values need to be standardized.

* A wide variety of techniques can be used during this step and include data **smoothing**, **binning**, and **
  normalization** as well as writing custom code to perform a particular transformation.
    * A customer’s age is often transformed from a raw age into a general age range. This process of converting ages
      into age ranges is an example of a data- transformation technique called **binning**.
        * Although binning is relatively straightforward from a technical perspective, the challenge here is to identify
          the most appropriate range thresholds to apply during binning. Applying the wrong thresholds may obscure
          important distinctions in the data. Finding appropriate thresholds, however, may require domain specific
          knowledge or a process of trial-and-error experimentation.

# Creating Analytics Base Table (ABT)

* The final step in data integration involves creating the data that are used as input to the ML algorithms. This data
  is known as the **analytics base table**.

* The most important step in creating the analytics base table is the selection of the attributes that will be included
  in the analysis.
    * The selection is based on domain knowledge and on an analysis of the relationships between attributes.

* Attributes that are found to have a high correlation with other attributes are likely to be redundant, and so one of
  the correlated attributes should be excluded.
    * Removing redundant features can result in simpler models which are easier to understand, and also reduces the
      likelihood of an ML algorithm returning a model that is fitted to spurious patterns in the data.

* The set of attributes selected for inclusion define what is known as the analytics record.
    * An analytics record typically includes both raw and derived attributes

* After the analytics record has been designed, a set of records needs to extracted and aggregated to create a data set
  for analysis. When these records have been created and stored—for example, in a database—this data set is commonly
  referred to as the analytics base table. The analytics base table is the data set that is used as input to the ML
  algorithms.

* selection of attributes that will be included in the analysis - based on domain knowledge
* removing redundant features --> simple models, easy to understand
* design analytics records - set of records to be extracted and aggregated to create a dataset
* ABT is used as input to the ml algorithm