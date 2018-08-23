# Time Based Demos
The code in this directory will demonstrate common temporal data sets.

## Temporal Demo

## Bi-Temporal Demo

This demonstration will show how take a known set of predicates to be a fact
for some set of time.  With bi-temporal data sets we will use two sets of
time ranges, **valid time** and **transaction time**.

For these types of use cases, inserts will essentially create new facts, while
updates will invalidate older facts, and queries will be able to be used to
show how facts have changed over time.

So what is this fact we are talking about?  It really can be anything we need.
A person and their addresses, financial instruments, etc.  Anything where the
validity of that fact can change over time and we need to understand how this
fact has changed.

How is this different from other data in a database?  For example a user
profile typically is not considered temporal data.  We don't necessarily
care how a users profile changes over time, we only care about what it
currently states, where as we might care about what a users financial holdings
are over time for tax purposes.

## Definition of Time
We will not actually attempt to define what time is, does it have a beginning,
an end, etc., this is left to folks much smarter than I am.  But rather
when does a fact change in our database, and for this demo we will define
time for all ranges the following way:
- Time will be represented as a *day*, facts **will only** change daily
- The lower bound (or *start*) will be **closed**
- The upper bound (or *end*) will be **opened**

For example, we create fact one on `January 2, 2018`, for a fact that became valid
on `January 1, 2018` we will have:

| entry | valid st     | valid et | transaction st | transaction et | fact        |
| ----- | ------------ | -------- | -------------- | -------------- | ----------- |
| 1     | Jan. 1, 2018 | MAX_TIME | Jan. 2 2018    | MAX_TIME       | some_fact_1 |

Now a new fact comes in which supercedes our original fact, update of address, positions,
what ever this fact might be, And this fact comes in on `February 2, 2018`, but became
valid on `February 1, 2018`, we now have the following entries:

| entry | valid st     | valid et     | transaction st | transaction et | fact        |
| ----- | ------------ | ------------ | -------------- | -------------- | ----------- |
| 1     | Jan. 1, 2018 | Feb. 1, 2018 | Jan. 2 2018    | Feb. 2, 2018   | some_fact_1 |
| 2     | Feb. 1, 2018 | MAX_TIME     | Feb. 2 2018    | MAX_TIME       | some_fact_2 |

So we can know confidently state the following:
- *some_fact_1* was valid from `January 1, 2018` to `January 31, 2018`
- *some_fact_2* is not a valid fact and has been so since `February 1, 2018`

**NOTE**: though this looks relational, the fact can actually be a rich document, which
can contain many facts and comments about which of the facts has changed since the
last fact superseded the previous.


## valid time
Valid time is the time for which a fact is true in the real world.  A valid
time may be in the past, span current time, or occur in the future.

In MongoDB we will use `start_vt` and `end_vt` as the fields to specify
when the given fact is true in the real world.  The interval will be **closed**
on the lower bound and **opened** on the upper bound.

Though this data could be inserted at any time (see **transaction time** below)

**NOTE**: if a facts `end_vt` is **not** known at transaction time, `end_vt` will not
be entered, this will mean that the fact is still **true**.  *This statement
is subject to change a we learn more about **bitemporal modeling***.

## transaction time
Transaction time records the time period during which a database entry is accepted
as correct.  This enables queries that show the state of the database at a given
time.  *Transaction time periods can only occur in the past or up to the current time*.

In a transaction time table, *records are never deleted*.  Only new rows are **inserted**,
and existing ones **updated** by setting their transaction end time to show that
they are no longer current.

In MongoDB we will use `start_tt` and `end_tt` as the fields to specify when the
fact was enterd and when the fact was superceded by a new fact.  The interval
is **closed** on the lower bound and **opened** on the upper bound.

## Modeling Approaches
There are various modeling approaches we can take, first we will look a few
of the standard methods and see if we can create something a bit more custom
for MongoDB.

### [Slowly Changing Dimension](https://en.wikipedia.org/wiki/Slowly_changing_dimension)


## Sources
Without the below sources I would not be able to actually build this demo, a big
thanks to the smart folks that have shared their knowledge with the world!

1. **[Temporal Database](https://en.wikipedia.org/wiki/Temporal_database)**:
2. **[SDC](https://en.wikipedia.org/wiki/Slowly_changing_dimension)**:
3. **[Valid Time](https://en.wikipedia.org/wiki/Valid_time)**:
4. **[Transaction Time](https://en.wikipedia.org/wiki/Transaction_time)**:
5. **[An Introduction to Database Systems](https://www.amazon.com/Introduction-Database-Systems-8th/dp/0321197844)**: 8th edition, C.J. Date, Addison Wesley, Chapter 23
6. **[Artificial Intelligence](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-2nd/dp/0137903952)**: Second Edition, Stuart Russell & Peter Norvig, Prentice Hall (*this is an older edition*)

## Change Log
| Date       | Change                                   |
| ---------- | ---------------------------------------- |
| 06-07-2018 | Initial Description of the system        |
|            | Initial code base                        |
