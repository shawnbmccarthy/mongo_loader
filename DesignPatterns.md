# Design Pattern Notes

This is intended to give an overview of various design patterns and options
which are available to the you (the developer) when working with MongoDB.

Various techniques will be covered, while the loader package will contain
different use-cases which will demonstrate the various techniques.

Each will be documented in detail in their respective python module
directories.

## Reference Material
The notes here come from experience as well as various sources, without
these sources, this project would not exist.  A big thank you for the work
the below references as they were invaluable:
- "[MongoDB Applied Design Patterns](https://www.amazon.com/MongoDB-Applied-Design-Patterns-Practical/dp/1449340040/)", O'Reilly, Rick Copeland
- "[The Littel Mongo DB Schema Design Book](https://www.amazon.com/Little-Mongo-Schema-Design-Book/dp/1517394023)", Learnpub, Christian Kvalheim
- "[MongoDB In Action](https://www.amazon.com/MongoDB-Action-Kyle-Banker/dp/1935182870)", Manning, Kyle Banker
- "[Scaling MongoDB](https://www.amazon.com/Scaling-MongoDB-Sharding-Cluster-Administration/dp/1449303218)", O'Reilly, Kristina Chodorow
- "[50 Tips and Tricks for MongoDB Developers: Get the Most Out of Your Database](https://www.amazon.com/50-Tips-Tricks-MongoDB-Developers-ebook/dp/B005011IIM)", O'Reilly, Kristina Chodorow
- "[Data Modeling Introduction](https://docs.mongodb.com/manual/core/data-modeling-introduction/)", MongoDB Documentation

## As compared to relational modeling
With relational modeling, we typically build data as a series of related
tables, each of which consist of some number of rows and columns.  This
collection of tables make up our database schema.

Relational databases use standard [modeling](https://en.wikipedia.org/wiki/Relational_model) techniques, to
store the data in [normal form](https://en.wikipedia.org/wiki/Database_normalization).
Typically we start with [1NF](https://en.wikipedia.org/wiki/First_normal_form) and grow
the model to a higher normal form such as [3NF](https://en.wikipedia.org/wiki/Third_normal_form) and others.

Each normal form has specific rules around reducing duplication, ensuring each
cell in the table contains exactly one value, etc.  Typically in relational
modeling one of the main goals is to reduce redundancy to allow for easy
updating of data.

We face problems when accessing the data as [joins](https://en.wikipedia.org/wiki/Join_(SQL)) can
be expensive, and scaling to multiple servers would introduce join across
distributed systems which is a complex and generally slow operation.

## Document Structure: Denormalized Structures
MongoDB stores data in a JSON like structure known as [BSON](https://docs.mongodb.com/manual/core/data-modeling-introduction/), which
is a binary representation of the structure.  This structure not only supports
key/value pairs (similar to relational), but also richer structures like arrays
as well as arrays of structures.  This allows us to develop or data structures
similar to the way we design our applications.  For example:

```
{
   _id: "joe",
   name: "Joe Bookreader",
   addresses: [
                {
                  street: "123 Fake Street",
                  city: "Faketon",
                  state: "MA",
                  zip: "12345"
                },
                {
                  street: "1 Some Other Street",
                  city: "Boston",
                  state: "MA",
                  zip: "12345"
                }
              ]
 }
```

Her we can easily embed multiple addresses into a single document allowing the
database to easily access on the data using a single `find()` operation without
the need to execute SQL join like operations.

### Document Atomicity
Documents are atomic structures in the MongoDB storage engine.  This is an all
or nothing operation which is isolated ensuring other readers will never see
an incomplete operation.

Using MongoDB 4.0, transactions have been introduced for edge use cases where
multiple documents need to updated in an atomic fashion.  There are also various
read concerns to ensure our applications can read our own writes using causal
consistency as well as sessions.

## Embedding and Referencing
Embedding will typically give the best performance, but there will be times
when a more normalized model can work better.

### Embedding

### Referencing

## Notes on the Demos
As each demo is developed notes on the demos as well as changelogs will be
stored in each demo as well as some of the core features it will be demonstrating

## Design Patterns

## TODO
1. finish this document
2. implement logging example
3. implement ecomm example

