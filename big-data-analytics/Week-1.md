#### Main Topics

After completing this Week you should be able to:

* Reasons might want to ask questions of data
* Explaining the way data is structured in analytics
* Describing a reasonable data science process, and explaining why each step is important
* Applying some basic descriptive statistics
* Explaining why validity and privacy are important concerns in big data analytics

#### Sub titles:

- [Reasons to ask question of data](#reasons-to-ask-question-of-data)
    - [Research Questions](#research-questions)
    - [Data Science](#data-science)

# Reasons to ask question of data

## Research Questions

* A research question is a question, and it describes something about the world that you don’t know, and that you intend
  to find out.
    * For example, what is the population of York?
* Criterion for research questions:
    * Criterion 1: It needs to be in the form of a question.
    * Criterion 2: It needs to be a complete question
        * For example : are videos a better way to learn? -> Are videos a better way to learn than text? => That’s
          better, it’s a bit more specific
    * Criterion 3: t needs to be narrow enough to answer using data we can collect, and the tools we have available.
        * For example : “are beans healthy?” -> "s there a correlation - statistical term - between average bean
          consumption - a particular measure which will need some operationalising, but it’s a measure you could take -
          and self-reported sick days?"
            * Likewise, it’s not trivial to measure, although the fact that it’s self-report makes it a bit easier; it
              also makes it less reliable but that’s by the by here. But you see you’ve got something you can really
              start to think about measurement and statistical analysis.

* Finding RQ’s is a craft skill:
    * What questions matter to you?
    * What data do you have? or extension, “what data can you easily get?”
    * Write down the questions that come up in your head.
* Always iterate

## Data Science

### What is data science?

* Data science encompasses a set of principles, problem definitions, algorithms, and processes for extracting non-
  obvious and useful patterns from large data sets.
    * Machine learning (ML) focuses on the design and evaluation of algorithms for extracting patterns from data.
        * “Machine learning” tends to be used when talking about specific algorithms used
            * The field of ML is at the core of modern data science because it provides algorithms that are able to
              automatically analyze large data sets to extract potentially interesting and useful patterns.
            * ML can be seen as automated techniques for finding patterns in data
            * Machine learning involves using a variety of advanced statistical and computing techniques to process data
              to find patterns.
            * GPUs have been adapted and optimized for ML use, which has contributed to large speedups in data
              processing and model training.
            * Data mining generally deals with the analysis of structured data and often implies an emphasis on
              commercial applications.
    * “Data science” is an umbrella term — it includes both of the others
* They can be used interchangeably in many practical contexts

* Data science can extract different type of patterns. Some examples below:
    * Identify groups of customers exhibiting similar behavior and tastes. In business jargon, this task is known as
      **customer segmentation**, and in data science terminology it is called **clustering**
    * Identifies products that are frequently bought together, a process called **association rule mining**.
    * Identify strange or abnormal events, such as fraudulent insurance claims, a process known as **anomaly** or
      **outlier detection**.
    * Identify classification rules as known **prediction**.
        * **Prediction** means deriving unknown properties of an entity from its known properties
        * So it is best to think of prediction patterns as predicting the missing value of an attribute rather than as
          predicting the future.
* Data science becomes useful when we have a large number of data examples and when the patterns are too complex for
  humans to discover and extract manually
* Features or variables means attributes of the data.
* The phrase **actionable insight** is sometimes used in this context to describe what we want the extracted patterns to
  give us.
    * **insight** highlights that the pattern should give us relevant information about the problem that isn’t obvious.
    * **actionable** highlights that the insight we get should also be something that we have the capacity to use in
      some way

### Data Gathering

* Transactional or operational data : Transactional data include event information such as the sale of an item, the
  issuing of an invoice, the delivery of goods, credit card payment, insurance claims, and so on.
* Non-transactional data: Such as demographic data, also have a long history.
* in 1970 Edgar F. Codd published a paper about **relational data** and relational database came up.
* Relational data model: the relational data model, which was revolutionary in terms of setting out how data were (at
  the time) stored, indexed, and retrieved from databases. The relational data model enabled users to extract data from
  a database using simple queries that defined what data the user wanted without requiring the user to worry about the
  underlying structure of the data or where they were physically stored.
    * Relational databases store data in tables with a structure of one row per instance and one column per attribute.
      This structure is ideal for storing data because it can be decomposed into natural attributes.
    * The development of structured query language (SQL) is using.
* Data warehouses: Data warehouses has the technology that was able to bring the data together and reconcile the data
  from disparate databases and that facilitated more complex analytical data operations. This business challenge led to
  the development of data warehouses.
* Meta data: Describe the structure and properties of the raw data.
* NoSQL databases :
    * A NoSQL database stores data as objects with attributes, using an object notation language such as the JavaScript
      Object Notation (JSON).
    * The advantage of using an object representation of data (in contrast to a relational table-based model) is that
      the set of attributes for each object is encapsulated within the object, which results in a flexible
      representation.

* **MapReduce** is a framework on Hadoop. In the MapReduce framework, the data and queries are mapped onto (or
  distributed across) multiple servers, and the partial results calculated on each server are then reduced (merged)
  together.

* Big Data is often defined in terms of the three Vs:
    * Three Vs:
        * Volume:  the extreme volume of data
        * Variety: the variety of the data types,
        * Velocity: and the velocity at which the data must be processed.

### History of Data analysis

* The simplest form of statistical analysis of data is the summarization of a data set in terms of summary (descriptive)
  statistics (including mea- sures of a central tendency, such as the arithmetic mean, or measures of variation, such as
  the range).
    * New developments in mathematics enabled statisticians to move beyond descriptive statistics and to start doing
      statistical learning.

* An engineer named William Playfair was inventing statistical graphics and laying the foundations for modern data
  visualization and exploratory data analysis.
    * He invented line, bar charts
* The advantage of visualizing quantitative data is that it allows us to 12 Chapter 1 use our powerful visual abilities
  to summarize, compare, and interpret data.
* t-distributed stochastic neighbor embedding (t-SNE) algorithm is a useful technique for reducing high-dimensional data
  down to two or three dimensions.
* Maximum likelihood estimate ia a method to draw conclusions based on the relative probability of events
* After the 1940s things started to move faster from the discovery of pattern recognition, neural networks, first steps
  of Machine Learning and then moved onto deep-learning neural networks and ensemble models in our times. Deep-Learning
  refers to a family of Neural Nets with multiple layers.
* The Knowledge Discovery in Databases (KDD), explains the required multidisciplinary approach to analyse large
  databases.
* The terms knowledge discovery in databases and data mining describe the same concept, the distinction being that data
  mining is more prevalent in the business communities and KDD more prevalent in academic communities.
* Breiman’s distinction between a statistical focus on models that explain the data versus an algorithmic focus on
  models that can accurately predict the data highlights a core difference between statisticians and ML researchers
* Today most data science projects are more aligned with the ML approach of build- ing accurate prediction models and
  less concerned with the statistical focus on explaining the data.

* **Skill set for a data scientist**.
    * Data scientists should have some domain expertise
    * Desirable skills: Machine learning, Communication ,Computer science ,Expertise in the application domain of the
      project , Working within the applicable ethical and legal codes
* Data Scientist needs to use HPC technologies.
    * High-performance computing (HPC) involves aggregating computing power to deliver higher performance than one can
      get from a standalone computer.
* computer science skills are also required to be able to understand and develop the ML models and integrate them into
  the production or analytic or back-end applications in an organization.

<img src="./img/1/1.png" alt="alt text" width="500" height="300">

* When are rigorous processes likely to be useful?
    * When we have a large volume of data examples
    * When we have are trying to find patterns over many attributes of entities

* What are the most important reasons computer science skills are valuable for a data scientist?
    * Understanding and developing machine learning algorithms
    * Using high-performance computing techniques for data processing

* Why have increases in networked app use stimulated
    * The volume of amount and variety of available data has increased

### Where Is Data Science Used?

* Data science drives decision making in nearly all parts of modern societies.
* Cases to show impact of ata science:
    * consumer companies using data science for sales and marketing;
        * The equivalent of up-selling and cross-selling in the online world is the “recommender system.”
    * governments using data science to improve health, criminal justice, and urban planning;
    * professional sporting franchises using data science in player recruitment.

#### Sales and marketing

* By tracking the past customers activities, behavior, analyzing social media trends, analyzing credit card activity
  they are using to recommend some product to customers.
* The equivalent of up-selling and cross-selling in the online world is the “recommender system.”
* Chris Anderson’s book The Long Tail (2008) argues that as pro- duction and distribution get less expensive, markets
  shift from selling large amounts of a small number of hit items to selling smaller amounts of a larger number of niche
  items.

#### Governments using data science

* Governments have recognized the advantages of adopting data science and uses it in different areas from
  health/targetted drop development to track, analyze & control environmental, energy, and transport systems and to
  inform long-term urban planning.
* Data science is also being used to predict crime hot spots and recidivism.

#### Data science in professional sports

* The MoneyBall movie tells the true story of how the Oakland A’s baseball team used data science to improve its player
  recruitment.
* The Moneyball story is a very clear example of how data science can give an organization an advantage in a competitive
  market space. However, from a pure data science perspective perhaps the most important aspect of the moneyball story
  is that it highlights that sometimes the primary value of data science is the **identification of informative
  attributes**.

### Myths about Data Science

* One of the big- gest myths is the belief that data science is an autonomous process that we can let loose on our data
  to find the answers to our problems.
    * In reality, data science requires skilled human oversight throughout the different stages of the process. Humans
      analysts are needed to frame the problem, to design and prepare the data, to select which ML algorithms are most
      appropriate, to critically interpret the results of the analysis, and to plan the appropriate action to take based
      on the insight(s) the analysis has revealed.
* The second big myth of data science is that every data science project needs big data and needs to use deep learning.
    * In general, having more data helps, but having the right data is the more important requirement.
* A third data science myth is that modern data science software is easy to use, and so data science is easy to do.
    * The danger with data science is that people can be intimidated by the technology and believe whatever results the
      soft- ware presents to them. They may, however, have unwittingly framed the problem in the wrong way, entered the
      wrong data, or used analysis techniques with inappropriate assumptions.
    * Data science properly requires both appropriate domain knowledge and the expertise regarding the properties of the
      data and the assumptions underpin- ning the different ML algorithms.
* The last myth about data science we want to mention here is the belief that data science pays for itself quickly.
    * Depends on the context of the organization.
    * data science will not give positive results on every project. Sometimes there is no hidden gem of insight in the
      data,and sometimes the organization is not in a position to act on the insight the analysis has revealed.

# Possible uses of data science

## Five projects that are harnessing big data for good

* [Five projects that are harnessing big data for good](https://theconversation.com/five-projects-that-are-harnessing-big-data-for-good-104844)
* The data science boom shouldn’t be limited to business insights and profit margins. When used ethically, big data can
  help solve some of society’s most difficult social and environmental problems.

### 1. Finding humanitarian hot spots

* This project was made with Australian Red Cross to figure out where the humanitarian hot spots are in Victoria.
* They use social media data to map everyday humanitarian activity to specific locations and found that the hot spots of
  volunteering and charity activity are located in and around Melbourne CBD and the eastern suburbs
* These kinds of insights can help local aid organisations channel volunteering activity in times of acute need.

### 2. Improving fire safety in homes

* In the United States, Enigma Labs built open data tools to model and map risk at the level of individual
  neighbourhoods.
* Their model combines national census data with a geocoder tool (TIGER), as well as analytics based on local fire
  incident data, to provide a risk score.

### 3. Mapping police violence in the US

* The Mapping Police Violence project in the US monitors, make sense of, and visualises police violence.
* It draws on three crowdsourced databases, but also fills in the gaps using a mix of social media, obituaries, criminal
  records databases, police reports and other sources of information

### 4. Optimising waste management

* These smart bins have solar-powered trash compactors that regularly compress the garbage inside throughout the day.
* This eliminates waste overflow and reduces unnecessary carbon emissions, with an 80% reduction in waste collection.

### 5. Identifying hotbeds of street harassment

* A group of four women – and many volunteer supporters – in Egypt developed HarassMap to engage with, and inform, the
  community in an effort to reduce sexual harassment.
* The platform they built uses anonymised, crowdsourced data to map harassment incidents that occur in the street in
  order to alert its users of potentially unsafe areas.

## Data science can help us fight human trafficking

* [Data science can help us fight human trafficking](https://theconversation.com/data-science-can-help-us-fight-human-trafficking-81647)
* Millions individuals worldwide are trapped in some form of modern-day slavery.
* Human trafficking occurs in every country in the world, because it’s one of the largest sources of profit for global
  organized crime, second only to illicit drugs.
* They have some problems:
    * Finding people at risk: They collect some data from goverment or organizations to understand the people who is at
      risk
    * Victim identification and location: Trafficking networks are dynamic. Traffickers are likely to frequently change
      distribution and transportation routes to avoid detection, leaving law enforcement and analysts with incomplete
      information as they attempt to identify and dismantle trafficking networks.
    * Network disruption: Interrupting the flow of people, money and other components of trafficking is critical to
      identifying trafficking networks, disrupting their infrastructure at the source and eliminating them.
* In operations research, scientists apply mathematical methods to answer complex questions about patterns in data and
  predict future trends or behaviors.

## Big data’s arrival in sport is changing the rules of the game

* [Big data’s arrival in sport is changing the rules of the game](https://theconversation.com/big-datas-arrival-in-sport-is-changing-the-rules-of-the-game-33519)
* Using data analysis in sport is complex – not just because of the sheer volume of it, but in finding ways to structure
  and relay many highly dynamic pieces of information to a coach, manager or athlete in order to make quick strategic
  decisions.
* Wearable clothes can collect health data and can use to increase performance of the athletes.
* Not only athletes ,data can use for fans too.
    * By understanding how fans engage with the sport or a team’s brand, decisions can be made about tailored sports
      advertising or broadcast content

## Explainer: what is big data?

* [Explainer: what is big data?](https://theconversation.com/explainer-what-is-big-data-13780)
* Big Data, as the name implies, relates to very large sets of data collected through free or commercial services on the
  internet.
* It is impossible to remove/withdraw information from big data - information once added will persist indefinitely in
  the cloud
* virtually any information that is stored electronically, including information within personal devices, offline data
  storage, even information thought to be deleted, has the potential to be included in big data.
* Data mining is the process of analysing inter-data relationships – connecting the dots and finding hidden meanings and
  relationships that can provide startling new insights.
* It may be argued that the capability to fully analyse internet-scale data will be key to nations in maintaining their
  prosperity and perhaps even security. The future may indeed rest with those with the best big data technologies.

## Big data: The next frontier for innovation, competition, and productivity

* [Big data: The next frontier for innovation, competition, and productivity](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/big-data-the-next-frontier-for-innovation)
* The amount of data in our world has been exploding, and analyzing large data sets—so-called big data—will become a key
  basis of competition, underpinning new waves of productivity growth, innovation, and consumer surplus.
* MGI studied big data in five domains—healthcare in the United States, the public sector in Europe, retail in the
  United States, and manufacturing and personal-location data globally.

* There are 5 ways for big data can create a value:
    * Big data can unlock significant value by making information transparent and usable at much higher frequency.
    * As organizations create and store more transactional data in digital form, they can collect more accurate and
      detailed performance information on everything from product inventories to sick days, and therefore expose
      variability and boost performance.
    * Big data allows ever-narrower segmentation of customers and therefore much more precisely tailored products and
      services.
    * Sophisticated analytics can improve decision making.
    * Bid data can used to improve the development of the next generation products and services.

* The use of big data will become a key basis of competition growth for individual firms.
* The use of big data will underpin new waves of productivity growth and consumer surplus.
* Some sectors are set for greater gains.
* There will be a shortage of talent necessary for organizations to take advantage of big data
* Several issues will have to be addressed to capture the full potential of big data. Policies related to privacy,
  security, intellectual property, and even liability will need to be addressed in a big data world.

# Describing a reasonable data science process

## The CRISP-DM Process

* Cross Industry Standard Process for Data Mining (CRISP- DM)
* Most of companies are using this pyramid to follow.
*

<img src="./img/1/2.png" alt="alt text" width="500" height="300">  

* The primary advantage of CRISP-DM, the main reason why it is so widely used, is that it is designed to be independent
  of any software, vendor, or data-analysis technique.

=============

# Group Lesson

* Standard attribute types:
    * **Numeric** : Numeric attributes describe measurable quantities that are repre- sented using integer or real
      values. Numeric attributes can be measured on either an interval scale or a ratio scale.

    * **Nominal**: Nominal (also known as categorical) attributes take values from a finite set. These values are
      names (
      hence “nominal”) for categories, classes, or states of things. Ex- amples of nominal attributes include marital
      status (sin- gle, married, divorced) and beer type (ale, pale ale, pils, porter, stout, etc.). A binary attribute
      is a special case of a nominal attribute where the set of possible values is re- stricted to just two values
    * **Ordinal** : Ordinal attributes are similar to nominal attributes, with the difference that it is possible to
      apply a rank order over the categories of ordinal attributes. For example, an at- tribute describing the response
      to a survey question might take values from the domain “strongly dislike, dislike, neu- tral, like, and strongly
      like.” There is a natural ordering over these values from “strongly dislike” to “strongly like” (or vice versa
      depending on the convention being used). How- ever, an important feature of ordinal data is that there is no
      notion of equal distance between these values. For ex- ample, the cognitive distance between “dislike” and “neu-
      tral” may be different from the distance between “like” and “strongly like.” As a result, it is not appropriate to
      apply arithmetic operations (such as averaging) on ordinal at- tributes. I
* **Structured data** : Structured data are data that can be stored in a table, and every instance in the table has the
  same structure (i.e., set of attributes). As an example, consider the demographic data for a population, where each
  row in the table describes one person and consists of the same set of demographic attributes (name, age, date of
  birth, address, gender, education level, job status, etc.). Structured data can be easily stored, organized, searched,
  reordered, and merged with other structured data. It is relatively easy to apply data science to structured data be-
  cause, by definition, it is already in a format that is suit- able for integration into an analytics record.
* **Unstructured data** : Unstructured data are data where each instance in the data set may have its own internal
  structure, and this structure is not necessarily the same in every instance. For example, imagine a data set of
  webpages, with each webpage having a struc- ture but this structure differing from one webpage to an- other.
  Unstructured data are much more common than structured data. For example, collections of human text (emails, tweets,
  text messages, posts, novels, etc.) can be considered unstructured data, as can collections of sound, image, music,
  video, and multimedia files. The variation in the structure between the different elements means that it is difficult
  to analyze unstructured data in its raw form. We can often extract structured data from unstructured data using
  techniques from artificial intelligence (such as natural-language processing and ML), digital signal pro- cessing, and
  computer vision. However, implementing and testing these data-transformation processes is expen- sive and
  time-consuming and can add significant financial overhead and time delays to a data science project.
* There are generally two terms for gathered raw data: captured data and exhaust data (Kitchin 2014a)
    * Captured data : Captured data are collected through a direct measurement or obser- vation that is designed to
      gather the data. For example, the primary purpose of surveys and experiments is to gather specific data on a
      particular topic of interest.

    * Exhaust data : Exhaust data are a by-product of a process whose primary purpose is something other than data
      capture. For example, the primary purpose of many social media technologies is to enable users to connect with
      other peo- ple. However, for every image shared, blog posted, tweet retweeted, or post liked, a range of exhaust
      data is gener- ated: who shared, who viewed, what device was used, what time of day, which device was used, how
      many people viewed/liked/retweeted, and so on. Similarly, the primary purpose of the Amazon website is to enable
      users to make purchases from the site. However, each purchase gener- ates volumes of exhaust data: what items the
      user put into her basket, how long she stayed on the site, what other items she viewed, and so on.
* Metadata : One of the most common types of exhaust data is metadata—that is, data that describe other data.


* Input
    * Concept
    * Concept description
    * Instance
    * Attribute

* classification learning - supervised
* association learning
* numeric prediction

## Questioning Data

## Structure of Data

## Data Science

## Using Statistics

## Data Validity and Privacy

