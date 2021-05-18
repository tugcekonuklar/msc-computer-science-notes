#### Main Topics

* Regression and prediction — the two forms of prediction
* Using linear regression to predict numerical values
* Using decision trees to predict classifications
* Evaluating predictions

#### Sub titles:

* [Key concepts in machine learning](#key-concepts-in-machine-learning)

# Key concepts in machine learning

* What is a concise definition of “machine learning”?
* What is the difference between “machine learning” and “data mining”?
* Why is it valuable to think about machine learning as part of a wider process?
* Should we make a clear distinction between “machine learning” and “statistics”?

* In data mining, the data is stored electronically and the search is automated—or at least augmented—by computer.
* As the world grows in complexity, overwhelming us with the data it generates, data mining becomes our only hope for
  elucidating hidden patterns. Intelligently analyzed data is a valuable resource. It can lead to new insights, better
  decision making, and, in commercial settings, competitive advantages.
* Data mining is about solving problems by analyzing data already present in databases.
* In today’s highly competitive, customer-centered, service-oriented economy, data is the raw material that fuels
  business growth.
* Data mining is defined as the process of discovering patterns in data. The process must be automatic or (more usually)
  semiautomatic. The patterns discovered must be meaningful in that they lead to some advantage—e.g., an economic
  advantage. The data is invariably present in substantial quantities.
* Useful patterns allow us to make nontrivial predictions on new data. There are two extremes for the expression of a
  pattern: as a black box whose innards are effectively incomprehensible and as a transparent box whose construction
  reveals the structure of the pattern.
    * The difference is whether or not the patterns that are mined are represented in terms of a structure that can be
      examined, reasoned about, and used to inform future decisions. Such patterns we call structural because they
      capture the decision structure in an explicit way. In other words, they help to explain something about the data.
    * Most of this book is about techniques for finding and describing structural patterns in data, but there are
      applications where black-box methods are more appropriate because they yield greater predictive accuracy, and we
      also cover those.
* STRUCTURAL PATTERNS
    * Part of a structural description of this information might be as follows:
      If tear production rate 5 reduced then recommendation 5 none Otherwise, if age 5 young and astigmatic 5 no then
      recommendation 5 soft
    * Structural descriptions need not necessarily be couched as rules such as these. Decision trees, which specify the
      sequences of decisions that need to be made along with the resulting recommendation, are another popular means of
      expression.
    * The rules do not really generalize from the data; they merely summarize it. In most learning situations, the set
      of examples given as input is far from complete, and part of the job is to generalize to other, new examples.
    * The preceding rules classify the examples correctly, whereas often, because of errors or noise in the data,
      misclassifications occur even on the data that is used to create the classifier.
* MACHINE LEARNING
    * Our dictionary defines “to learn” as
        * to get knowledge of by study, experience, or being taught; to become aware by information or from observation;
        * to commit to memory;
        * to be informed of, ascertain;
        * to receive instruction.
    * First 2 is hard for computers but the last 3 computers can do easly
    * Learning implies thinking. Learning implies purpose. Something that learns has to do so intentionally. That is why
      we wouldn’t say that a vine has learned to grow round a trellis in a vineyard—we’d say it has been trained.
      Learning without purpose is merely training
    * Thus on closer examination the second definition of learning, in operational, performance-oriented terms, has its
      own problems when it comes to talking about computers. To decide whether something has actually learned, you need
      to see whether it intended to, whether there was any purpose involved
    * Philosophical discussions of what is really meant by “learning,” like discussions of what is really meant by
      “intention” or “purpose,” are fraught with difficulty.

* DATA MINING
    * Data mining is a practical topic and involves learning in a practical, not a theoretical, sense. We are
      interested in techniques for finding patterns in data, patterns that provide insight or enable fast and accurate
      decision making.
    * Many learning techniques look for structural descriptions of what is learned, descriptions that can become fairly
      complex and are typically expressed as sets of rules such as the ones described previously or the decision trees
    * Experience shows that in many applications of machine learning to data mining, the explicit knowledge structures
      that are acquired, the structural descriptions, are at least as important as the ability to perform well on new
      examples.
        * People frequently use data mining to gain knowledge, not just predictions.

* Weather problem:
    * In general, examples in a dataset are characterized by the values of features, or attributes, that measure
      different aspects of the example
    * A set of rules that are intended to be interpreted in sequence is called a decision list. Interpreted as a
      decision list, the rules correctly classify all of the examples in the table, whereas taken individually,
    * n the slightly more complex form shown in Table 1.3, two of the attributes—temperature and humidity—have numeric
      values. This means that any learning scheme must create inequalities involving these attributes, rather than
      simple equality tests as in the former case. This is called a numeric-attribute problem—in this case, a
      mixed-attribute problem because not all attributes are numeric.
    * The rules we have seen so far are classification rules: they predict the classification of the example in terms of
      whether to play or not. It is equally possible to disregard the classification and just look for any rules that
      strongly associate different attribute values. These are called association rules.

* Contact lences: an idealized problem
    * People frequently use machine learning techniques to gain insight into the structure of their data rather than to
      make predictions for new cases. In fact, a prominent and successful line of research in machine learning began as
      an attempt to compress a huge database of possible chess endgames and their outcomes into a data structure of
      reasonable size.
    * The data structure chosen for this enterprise was not a set of rules but a decision tree.
    * a structural description for the contact lens data in the form of a decision tree, which for many purposes is a
      more concise and perspicuous representation of the rules and has the advantage that it can be visualized more
      easily.

* Ireses: Classic numeric data set
    * These rules are very cumbersome, and we will see in Chapter 3, Output: knowledge representation, how more compact
      rules can be expressed that convey the same information.

* CPU performance: Introducing Numeric prediction
    * The classic way of dealing with continuous prediction is to write the outcome as a linear sum of the attribute
      values with appropriate weights, e.g.,

    * This is called a linear regression equation, and the process of determining the weights is called linear
      regression, a well-known procedure in statistics
    * The basic regression method is incapable of discovering nonlinear relationships, but variants exist

* Labor negotiations: More realistic example
    * In fact, Fig. 1.3B is a more accurate representation of the training dataset than Fig. 1.3A. But it is not
      necessarily a more accurate representation of the underlying concept of good versus bad contracts. Although it is
      more accurate on the data that was used to train the classifier, it may perform less well on an independent set of
      test data. It may be “overfitted” to the training data—following it too slavishly.

* soybean classification:
    * An often quoted early success story in the application of machine learning to practical problems is the
      identification of rules for diagnosing soybean diseases. The data is taken from questionnaires describing plant
      diseases.
    * These rules nicely illustrate the potential role of prior knowledge—often called domain knowledge—in machine
      learning, for in fact the only difference between the two descriptions is leaf condition is normal versus leaf
      malformation is absent. Now, in this domain, if the leaf condition is normal then leaf malformation is
      necessarily absent, so one of these conditions happens to be a special case of the other

## FIELDED APPLICATIONS

* Being fielded applications, the illustrations that follow tend to stress the use of learning in performance
  situations, in which the emphasis is on the ability to perform well on new examples.
    * WEB MINING
        * Search engine companies examine the hyperlinks in web pages to come up with a measure of “prestige” for each
          web page and website. Dictionaries define prestige as “high standing achieved through success or influence.”
        * A metric called PageRank, introduced by the founders of Google and used in various guises by other search
          engine developers too, attempts to measure the standing of a web page. The more pages that link to your
          website, the higher its prestige.
        * Another way in which search engines tackle the problem of how to rank web pages is to use machine learning
          based on a training set of example
        * queries—documents that contain the terms in the query and human judgments about how relevant the documents are
          to that query. Then a learning algorithm analyzes this training data and comes up with a way to predict the
          relevance judgment for any document and query.
        * Search engines mine the content of the Web. They also mine the content of your queries—the terms you search
          for—to select advertisements that you might be interested in
        * And then there are social networks and other personal data. We live in the age of selfrevelation: people share
          their innermost thoughts in blogs and tweets, their photographs, their music and movie tastes, their opinions
          of books, software, gadgets, and hotels, their social life. They may believe they are doing this anonymously,
          or pseudonymously, but often they are incorrect
    * DECISIONS INVOLVING JUDGMENT
    * When you apply for a loan, you have to fill out a questionnaire asking for relevant financial and personal
      information.
        * made in two stages: first, statistical methods are used to determine clear “accept” and “reject” cases. The
          remaining borderline cases are more difficult and call for human judgment.
    * A machine learning procedure was used to produce a small set of classification rules that made correct predictions
      on two-thirds of the borderline cases in an independently chosen test set.
        * Not only did these rules improve the success rate of the loan decisions, but the company also found them
          attractive because they could be used to explain to applicants the reasons behind the decision.
        * Although the project was an exploratory one that took only a small development effort, the loan company was
          apparently so pleased with the result that the rules were put into use immediately.
    * SCREENING IMAGES
    * Radar satellites provide an opportunity for monitoring coastal waters day and night, regardless of weather
      conditions.
    * A hazard detection system has been developed to screen images for subsequent manual processing.
    * Machine learning allows the system to be trained on examples of spills and nonspills supplied by the user and lets
      the user control the tradeoff between undetected spills and false alarms.
    * DIAGNOSIS
    * Diagnosis is one of the principal application areas of expert systems. Although the hand-crafted rules used in
      expert systems often perform well, machine learning can be useful in situations in which producing rules manually
      is too labor intensive.
    * The goal was not to determine whether or not a fault existed, but to diagnose the kind of fault, given that one
      was there.
        * Thus there was no need to include fault-free cases in the training set. The measured attributes were rather
          low level and had to be augmented by intermediate concepts,
        * i.e., functions of basic attributes, which were defined in consultation with the expert and embodied some
          causal domain knowledge
        * It is interesting to note, however, that the system was put into use not because of its good performance but
          because the domain expert approved of the rules that had been learned
    * MARKETING AND SALES
    * Market basket analysis is the use of association techniques to find groups of items that tend to occur together in
      transactions, e.g., supermarket checkout data.
    * For many retailers this is the only source of sales information that is available for data mining.
        * or example, automated analysis of checkout data may uncover the fact that customers who buy beer also buy
          chips, a discovery that could be significant from the supermarket operator’s point of view (although rather an
          obvious one that probably does not need a data mining exercise to discover)

## MACHINE LEARNING AND STATISTICS

* In truth, you should not look for a dividing line between machine learning and statistics because there is a
  continuum—and a multidimensional one at that—of data analysis techniques.

* If forced to point to a single difference of emphasis, it might be that statistics has been more concerned with
  testing hypotheses, whereas machine learning has been more concerned with formulating the process of generalization as
  a search through possible hypotheses. But this is a gross oversimplification: statistics is far more than just
  hypothesis-testing, and many machine learning techniques do not involve any searching at all.
* In the past, very similar schemes have developed in parallel in machine learning and statistics
    * Decision tree induction:  Four statisticians at Californian universities published a book on Classification and
      regression trees in the mid-1980s, and throughout the 1970s and early 1980s a prominent Australian machine
      learning researcher, J. Ross Quinlan, was developing a system for inferring classification trees from examples.
    * similar methods have arisen involves the use of nearest-neighbor methods for classification. These are standard
      statistical techniques that have been extensively adapted by machine learning researchers, both to improve
      classification performance and to make the procedure more efficient computationally.
* Right from the beginning, when constructing and refining the initial example set, standard statistical methods apply:
  visualization of data, selection of attributes, discarding outliers, and so on.
* Many learning algorithms use statistical tests when constructing rules or trees and for correcting models that are
  “overfitted” in that they depend too strongly on the details of the particular examples used to produce them
* Statistical tests are used to validate machine learning models and to evaluate machine learning algorithms.

# Machine Learning 101

* Machine learning is the field of study that develops the algorithms that the computers follow in order to identify and
  extract patterns from data.
* ML algorithms and techniques are applied primarily during the modeling stage of CRISP-DM. ML involves a two-step
  process.
    * First, an ML algorithm is applied to a data set to identify useful patterns in the data. These patterns can be
      represented in a number of different ways.
        * Simply put, ML algorithms create models from data, and each algorithm is designed to create models using a
          particular representation (neural network or decision tree or other).
    * Second, once a model has been created, it is used for analysis.
        * In some cases, the structure of the model is what is important.
        * A model structure can reveal what the important attributes are in a domain.

## Supervised versus Unsupervised Learning

* The goal of supervised learning is to learn a function that maps from the values of the attributes describing an
  instance to the value of another attribute, known as the target attribute, of that instance.
    * For example, when supervised learning is used to train a spam filter, the algorithm attempts to learn a function
      that maps from the attributes describing an email to a value (spam/not spam) for the target attribute; the
      function the algorithm learns is the spam-filter model returned by the algorithm.
* Supervised learning works by searching through lots of different functions to find the function that best maps between
  the inputs and output.
    * However depends on the complexity, there are so many combinations of inputs and possible mappings to outputs that
      an algorithm cannot try all possible functions.
    * As a consequence, each ML algorithm is designed to look at or prefer certain types of functions during its search.
      These preferences are known as the algorithm’s **learning bias**.
* **The real challenge in using ML** is to find the algorithm **whose learning bias is the best match for a**
  **particular data set.**
    * this task involves experiments with a number of different algorithms to find out which one works best on that data
      set.
* Supervised learning is “supervised” because each of the instances in the data set lists both the input values and the
  output (target) value for each instance.
    * So the learning algorithm can guide its search for the best function by checking how each function it tries
      matches with the data set, and at the same time the data set acts as a supervisor for the learning process by
      providing feedback
* for supervised learning to take place, each instance in the data set must be labeled with the value of the target
  attribute.
* In unsupervised learning, there is no target attribute.
    * As a consequence, unsupervised-learning algorithms can be used without investing the time and effort in labeling
      the instances of the data set with a target attribute.

* The most common type of unsupervised learning is cluster analysis, where the algorithm looks for clusters of instances
  that are more similar to each other than they are to other instances in the data.
    * These clustering algorithms often begin by guessing a set of clusters and then iteratively updating the clusters

* A challenge for clustering is figuring out how to measure similarity.
    * If all the attributes in a data set are numeric and have similar ranges, then it probably makes sense just to
      calculate the Euclidean distance (better known as the straight-line distance) between the instances (or rows).
    * In some data sets, different numeric attributes have different ranges, with the result that a variation in row
      values in one attribute may not be as significant as a variation of a similar magnitude in another attribute.
        * In these cases, the attributes should be normalized so that they all have the same range
    * Another complicating factor in calculating similarity is that things can be deemed similar in many different ways.
        * Some attributes are sometimes more important than other attributes, so it might make sense to weight some
          attributes in the distance calculations, or it may be that the data set includes nonnumeric data.
* The choice of which attributes to include and exclude from a data set is a key task in data science, but for the
  purposes of this discussion we will work with the data set as is.
* In unsupervised clustering algorithm will look for groups of rows that are more similar to each other than they are to
  the other rows in the data
    * Each of these groups of similar rows defines a cluster of similar instances.
* The simple idea of looking for clusters of similar rows is very powerful and has applications across many areas of
  life. Another application of clustering rows is making product recommendations to customers.