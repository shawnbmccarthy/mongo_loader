# Mongo Loader

A python loader for different use cases, the runner will also survive replica set failures and is built to be
sharded based off the _id.  This will allow the performance advisor as well as the profiler to show useful
index recommendations based off the various use cases

## Usage

```commandline
$ python3 ./main.py --help
usage: main.py [-h] [--url URL] {blog} ...

loader program

positional arguments:
  {blog}      help for loader types
    blog      blog loader help

optional arguments:
  -h, --help  show this help message and exit
  --url URL   mongodb url
  --drop
```

Please note that the mongo url should be a valid url with a given database for the loader being run against.
If the `--drop` flag is used the database will first be dropped before inserting more data

**future** The loader will support more use cases later 

## Logging

A logging.conf file is used to control how the data is logged, by default all data is logged to standard out with a 
level of info, this can be changed by modifying the logging.conf file

## Blog Loader

The blog demo will execute common queries that would be common to a blog, there will be 4 main collections, described 
below.

To execute the blog demo execute the following commands:

```commandline
$ python3 ./main.py --url mongodb://localhost:27017/test --drop blog --users 10000 --authors 1000 --blogs 100000
```

The above command will create an execution where it will first create `10000` users and `1000` authors then it will
begin to create and manage `100000` blogs.  How they are managed is described below.

If we call it with defaults:
```commandline
$ python3 ./main.py --url mongodb://localhost:27017/blogs --drop blog
```

The demo will run with `900` users, `100` authors, and manage `10000` blogs by default.

### Collections
#### users collection
chosen for `CAST_OF_CHARACTERS` found in `loader.data` which has 320 2-element arrays allowing for 10s of thousands of 
user creations.

Tests roughly 30k users took about 1 minute to create with duplication testing and debug (will work on better user creation later), 
and takes about 30 seconds without debug.

This will create a document in the following format:
```json
{
	"_id" : "Derek.Johnson",
	"fname" : "Derek",
	"lname" : "Johnson",
	"email" : "Derek.Johnson@postmark.com",
	"created_at" : ISODate("2018-01-29T21:40:11.349Z"),
	"pw" : "3cd10a132df5d2567561cb9496265eaefa7c33bd47559b865cd416ffa039",
	"is_locked" : false,
	"interests" : [
		"suspendisse",
		"varius",
		"suspendisse",
		"cursus"
	],
	"is_author" : true
}
```

The loader code will generate a user based of the `CAST_OF_CHARACTERS` array found in the `loaders.data` which has roughly
320 2-elemen arrays in the form `[FIRST_NAME, LAST_NAME]`, the code will pick 2 different arrays and chose a first and last 
name from the array and generate a unique `_id`, during the run it will test to ensure that the `_id` does not exist 
before attempting the insert.  

The `interests` array is chosen from a LOREM IPSUM array of words and the is_author is set to `true` or `false` depending
on what mode we are running in.

Tests roughly 30k users took about 1 minute to create with duplication testing and debug (will work on better user creation later), 
and takes about 30 seconds without debug.

Users are created once, before all other queries are run.

**TODO** change algorithm to use batch loading, as we get into the larger values 40000 and above it takes some time to do
the individual inserts

#### tags collection

100 tags are created in the following format:
```json
{ "_id" : "accumsan", "total_blogs" : 0 }
```

The `_id` represents the tag name, while the `total_blogs` is initially set to 0, later a background process will run
which will update the number of blogs that have the associated tag, this is silly but something that will allow more
queries to be run on the system.

Tags are created once, before all other queries start running.

#### blogs collection

once the `users` and `tags` are created, the blogs will begin to be created once every `5` seconds until the total number
of blogs are created, which can be specified on the command line.

The format of the blog document is: 
```json
{
	"_id" : ObjectId("5a6fdb10779666410bd1109f"),
	"title" : "urna blandit quam euismod",
	"tags" : [
		"eget",
		"lacinia",
		"cras",
		"placerat",
		"nulla",
		"sagittis",
		"sagittis",
		"luctus",
		"arcu",
		"vehicula",
		"lacinia"
	],
	"created_on" : ISODate("2018-01-29T21:40:16.499Z"),
	"author" : "Derek.Johnson",
	"content" : "Praesent eu feugiat eros. Morbi viverra tortor placerat eros gravida, ...",
	"is_locked" : false,
	"comments" : [
		{
			"date" : ISODate("2018-01-29T21:40:17.507Z"),
			"cmmt" : "Donec sem turpis, accumsan sed turpis eget, volutpat interdum augue. Nullam eget dolor tellus. Curabitur metus",
			"user" : "Jeff.Sandrov"
		}
	],
	"updated_on" : ISODate("2018-01-29T21:46:51.621Z")
}
```

For each blog, a random author is selected from the `users` collection and a set of random tags as well as random number
of LOREM IPSUM paragraphs.

The intial document will have 0 comments and no `updated_on` field.  During the run, `find_and_modify` commands will be
run to add comments as well as update the document contents.


#### comments collection
As comments are added to the document, a background process will run every 20 seconds to find all documents where the `21` index exists 
on comments, if the size of the array is above `20` the process will move all the comments with index greater than `20` 
to a comments collection.

The comments collection can only grow to 100000 comments, a background process will run every 20 seconds to delete any 
files greater than the limit.

### Operations on collections
Below describes all the operations on the collections

#### create users
This will be run once when the program starts it will create `users` and `authors` based of the arguments passed or the defaults
this can be found in `loader.blog_example.generate_user` function, currently this runs in `insert_one` to ensure we are not
creating duplicate `_id` as the demo wants unique user names.

**TODO** provide an update function for users where the user interest array is updated

#### create and update tags
This will be run once when the program starts, it will create 100 tags, these tags will be used in the `blogs` collection
the `_id` is the name of the tag so data is duplicated, this document will hold some analytics, the number of blogs associated
with this tag. 

The analytical update will happen once every 10 seconds

#### create & update blogs
One blog will be created every 5 seconds until the limit specified by the command line (or default) is hit.  Comments are 
then added to a random blog every 2 seconds.

Every 10 seconds a random blogs content and updated_at fields will be updated.

Every 20 seconds all blogs with more than 20 comments will be cleaned up.

These updates make use of the `find_and_modify` to ensure we are only updating documents which have been locked, ensuring
we don't lose data.

#### create & delete on comments
Once a blog has more than 20 comments the older comments are then moved to a comments collection.  This happens as the 
blog itself is updated.  

Once every 20 seconds all old comments that exceed the 100000 document threshold are removed one at a time.

**TODO** possibly introduce code to ensure writes happen successfully 

# Contributors
shawn McCarthy
Mike Lynn