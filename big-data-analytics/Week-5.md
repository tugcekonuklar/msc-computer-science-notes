#### Main Topics

After completing this week you should be able to:

* Describe the relational database mode
* Explain the problems caused by data that is too large for RAM
* Explain how Big Data causes problems for analytics

After completing this week, you will have made significant steps towards achieving the following module learning
outcomes:

* MO2 — Manipulate a data set to extract statistics and features

#### Sub titles:

* [Why databases?](#why-databases)

# Why databases?

* Answer is :  the term ‘database’ can be used in both an informal way (perhaps suggesting a collection of data on which
  we might base a decision) and more formally to mean a specific approach and software structure for storing and
  manipulating data.

## Intro

* Database can store traditional , numeric and alphanumeric values and also multimedia data such as picture, video or
  audio, biometric data such as finger prints, retins scans, geographic info such as coordinates etc.

* A database can derived as a collection of related data items with a special business process or problem setting.
* A Database Management System (DBMS) is the software package used to define create, use and maintain a database.
    * Populars , Oracle, Microsoft, IBM ,My-SQL( well known open source DBMS)
* A combination of database with DBMS called database system.
* Before databases, data was stored in files and this has the danger of data duplication, redundancy and inconsistency
  as different applications kept records in different files.
    * The other option is all the applications accessing the same file store and retrieve data but then this has the
      problem of concurrency management which isn't easy either.
* Then, with databases, DBMS is in charge of delivering the data and managing the data access. DBMS also manage the
  metadata related to the stored data.
* DBM is also provides database languages that both data query and access. Well known language SQL
* The file base approach results in a strong application data dependence, where as tha database approach allows for
  applications to be independence from the data and data definitions.

* DBMS also help to achieve a looser application-data coupling as opposed to the stronger coupling with the file-based
  approach.

### Elements of Database System

* Database Model and shema provodes the definition of the database data at different levels .
* The database state, the current set of instances, represents the data in the database at a particular moment.
* Data model provides a clear and unambigous description of the data items , its relation and variour data concerns .
    * Conceptional data model is high level description of data items. should be implementation independent,
      user-friendly, and close to how the business user perceives the data. It will usually represented with Enhanced
      Entity Relationsgip (EER) model.
    * Logical data model is translation or mapping of the conceptual data modal towards special implementation
      environment. Like OOP, This describes which data stores where.
    * External data models contains various subset data items in logical model, also called views. A view describes the
      part of the database that a particular application or user group is interested in, hiding the rest of database.
* Three-layer architecture is essential for
    * In external layer has the external model , which includes views.
    * In internal layer includes internal data model, which specifies how the data stores or organised pysicaly.
* Idealy changes in one layer should have no to minimal impact on the others.
  <img src="./img/5/1.png" alt="alt text" width="500" height="300"></br>

* Catalog is the hard of the DBMS, contains data definition or metadata of the application.
    * it stores definition of views, logical and internal data models, and syncronises these 3 models to ensure
      consistency.

### Database User

* Information architect, design conceptional data by working closely with business.
* Database designer, converts conceptional data to logical and internal data model.
* Database administrator (DBA), reposnsile implementation and monitoring tha db.

### Database language

* The Database Definition Language (DDL) is used by DBA to express the DB external, logical, internal data models.
* Data Manipulation Language (DML) is used to retrieve , insert, update delete and modify data.
* SQL offers bith DDL and DML for relational DBs.

## Advantage of Database System and Database Management

* Database offers some addvantages such as,
    * data independence; managing structured, semi-structured and unstructured data;
    * database modeling;
    * managing data radundancy;
    * specifiying integrity rules;
    * conqurrency control
    * backup and recovery facilities
    * data security and performance utilities.

### Data independence

* Means that changing data definition has minimal to no impact on the applications using the data.
* Physical data independence implies that neither the applications, views, or logical data model must be changed when
  changes are made to the data storage specifications in the internal data model.
* Logical data independence implies that software applications are minimally affected by changes in the conceptual or
  logical data model. Consider the example of adding new data items, characteristics, or relationships.

### Database Modeling

* A data model is an explicit representation of the data items together with their characteristics and relationships.
  Also include integrity rules and functions.
* Popular examples of data models are the hierarchical model, the CODASYL model, the (E)ER model, the relational model,
  and the object-oriented model.

### Managing Structured, Semi-Structured, and Unstructured Data

* It is important to note that not all kinds of data but only structured data can be described according to a formal
  logical data model.
* With structured data, individual characteristics of data items can be identified and formally specified, such as the
  number, name, address, and email of a student, or the number and name of a course.
    * The advantage is the ability to express integrity rules and in this way enforce the correctness of the data
* With unstructured data, ie text documents, there are no finer-grain components in a file or series of characters that
  can be interpreted in a meaningful way by a DBMS or application.
* The data that isn't completely structured or unstructured is called semi-structured. XML and NoSQL databases deal with
  semi-structured data.
    * The semi-structured data still has a certain structure, but the structure may be very irregular or highly
      volatile.

### Managing Data Redundancy

* The DBMS is responsible for the management of redundancy by providing synchronization facilities to safeguard data
  consistency.
    * DBMS might deliberately create data redundancy for faster retrieval where the data is distributed across different
      locations.

### Specifying Integrity Rules

* These rules can be used to enforce the correctness of the data.
    * Syntactical rules specify how the data should be represented and stored. Examples are:
      customerID should be represented as an integer
* Semantic rules focus on the semantic correctness or meaning of the data. Examples are:
  customerID should be unique; account balance should be bigger than 0;
* n. In the database approach, they are specified as part of the conceptual/logical data model and are stored centrally
  in the catalog.
    * This substantially improves the efficiency and maintainability of the applications since the integrity rules are
      now directly enforced by the DBMS whenever anything is updated

### Concurrency Control (ACID)

* A DBMS has built-in facilities to support concurrent or parallel execution of database programs, which allows for good
  performance.
* A key concept is a database transaction that is a sequence of read/write operations, considered to be an atomic unit
  in the sense that either all operations are executed or none at all.
* Typically, these read/write operations can be executed at the same time by the DBMS.
* DBMS must support the **ACID** (Atomicity, Consistency, Isolation, Durability) properties.
    * **Atomicity**, or the all-or-nothing property, requires that a transaction should either be executed in its
      entirety or not at all.
    * **Consistency** assures that a transaction brings the database from one consistent state to another.
    * **Isolation** ensures that the effect of concurrent transactions should be the same as if they had been executed
      in isolation.
    * **Durability** ensures that the database changes made by a transaction declared successful can be made permanent
      under all circumstances.

### Backup and Recovery Facilities

* A key advantage of using databases is the availability of backup and recovery facilities.
    * These facilities can be used to deal with the effect of loss of data due to hardware or network errors, or bugs in
      system or application software

### Data Security

* Depending on the business application considered, some users have read access, while others have write access to the
  data (role-based functionality)
    * This can also be further refined to certain parts of the data

### Performance Utilities

* Three key performance indicators (KPIs) of a DBMS are: response time; throughput rate; and space utilization
    * The response time denotes the time elapsed between issuing a database request (e.g., a query or update
      instruction) and the successful termination thereof
    * The throughput rate represents the transactions a DBMS can process per unit of time.
    * Space utilization refers to the space utilized by the DBMS to store both the raw data and the metadata. A
      high-performing DBMS is characterized by quick response times, high throughput rates, and low space utilization

# Data and quality management

## Data Management

* Data management entails the proper management of data and the corresponding data definitions or metadata
* Just as with raw data, metadata are also data that need to be properly modeled, stored, and managed.
    * Hence, the concepts of data modeling should also be applied to metadata in a transparent way
* In a DBMS approach, metadata are stored in a catalog, sometimes also called a data dictionary or data repository,
  which constitutes the heart of the database system
    * This facilitates the efficient answering of questions such as which data are stored where in the database? Who is
      the owner of the data? Who has access to the data? How are the data defined and structured? Which transactions
      work with which data? Are the data replicated and how can consistency be guaranteed? Which integrity rules are
      defined? How frequently are backups made?

* The catalog provides an important source of information for end-users, application developers, and the DBMS itself.
    * the data definitions are generated by the DDL compiler. The DML compiler and query processor use the metadata to
      solve queries and determine the optimal access path

* The catalog should provide support for various functionalities
    * It should implement an extensible metamodel for the description of the metadata.
    * It should have facilities to import and export the data definitions and provide support for maintenance and re-use
      of metadata.
* The integrity rules stored should be continuously monitored and enforced whenever the raw data are updated. By doing
  so, the catalog guarantees that the database is always in a consistent and correct state

* A metamodel determines the type of metadata that can be stored. Just as with raw data, a database design process can
  be used to design a database storing metadata

## Data Quality

* Data quality determines the intrinsic value of the data to the business. Information technology only serves as a
  magnifier for this intrinsic value.
    * Hence, high-quality data combined with effective technology comprises a great asset, but poor-quality data
      combined with effective technology is an equally great liability.
    * This is sometimes also called the GIGO — Garbage In, Garbage Out — principle, stating that bad data result in bad
      decisions, even with the best technology available.

* Poor DQ impacts organizations in many ways.
    * At the operational level, it affects customer satisfaction, increases operational expenses, and will lead to lower
      employee job satisfaction.
    * At the strategic level, it affects the quality of the decision-making process.

* A DQ framework categorizes the different dimensions of data quality
* The intrinsic category represents the extent to which data values conform to the actual or true values.
* The contextual category measures the extent to which data are appropriate to the task of the data consumer. Obviously,
  this can vary in time and across data consumers.
* The representation category indicates the extent to which data are presented in a consistent and interpretable way.
  Hence, it relates to the format and meaning of data.
* The access category represents the extent to which data are available and obtainable in a secure manner

  <img src="./img/5/2.png" alt="alt text" width="500" height="300"></br>

* Data Quality Problems:
    * Multiple data sources: multiple sources with the same data may produce duplicates — a problem of consistency.
    * Subjective judgment in data production: data production using human judgment (e.g., opinions)
      can cause the production of biased information — a problem of objectivity.
    * Limited computing resources: lack of sufficient computing resources and/or digitalization may limit the
      accessibility of relevant data — a problem of accessibility.
    * Volume of data: large volumes of stored data make it difficult to access needed information in a reasonable time —
      a problem of accessibility.
    * Changing data needs: data requirements change on an ongoing basis due to new company strategies or the
      introduction of new technologies — a problem of relevance.
    * Different processes using and updating the same data — a problem of consistency

# Data Governance

* To manage and safeguard DQ, a data governance culture should be put in place assigning clear roles and
  responsibilities.
* The aim of data governance is to set-up a company-wide controlled and supported approach toward DQ accompanied by DQ
  management processes.
* The core idea is to manage data as an asset rather than a liability, and adopt a proactive attitude toward data
  quality
* A TDQM cycle consists of four steps — define, measure, analyze, and improve — which are performed iteratively.

  <img src="./img/5/3.png" alt="alt text" width="500" height="300"></br>

# Roles in Data Management

* The **information architect** (also called information analyst) designs the conceptual data model, preferably in
  dialogue with the business users.
    * He/she bridges the gap between the business processes and the IT environment and closely collaborates with the
      database designer, who may assist in choosing the type of conceptual data model (e.g., EER or UML) and the
      database modeling tool.

* The **database designer** translates the conceptual data model into a logical and internal data model.
    * He/she also assists the application developers in defining the views of the external data model. To facilitate
      future maintenance of the database applications, the database designer should define company-wide uniform naming
      conventions when creating the various data models.

* **Data owner**, who has the authority to ultimately decide on the access to, and usage of, the data.
    * The data owner could be the original producer of the data, one of its consumers, or a third party.

* **Data stewards** are the DQ experts in charge of ensuring the quality of both the actual business data and the
  corresponding metadata.
    * They assess DQ by performing extensive and regular data quality checks.
        * A first type of action to be taken is the application of corrective measures.
            * However, data stewards are not in charge of correcting data themselves, as this is typically the
              responsibility of the data owner.
        * The second type of action to be taken upon the results of the DQ assessment involves a deeper investigation
          into the root causes of the DQ issues detected.
* The **database administrator (DBA)** is responsible for the implementation and monitoring of the database.
    * Example activities include: installing and upgrading the DBMS software; backup and recovery management;
      performance tuning and monitoring; memory management; replication management; security and authorization.
    * Closely collaborates with network and system managers

* **Data scientist** is a relatively new job profile within the context of data management.
    * He/she analyzes data using state-of-the-art analytical techniques to provide new insights into, for example,
      customer behavior.
    * A data scientist has a multidisciplinary profile combining ICT skills (e.g., programming) with quantitative
      modeling (e.g., statistics), business understanding, communication, and creativity
