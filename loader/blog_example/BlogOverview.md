# Loader: Blog Demonstration

The `loader.blog_example`  will execute various blog operations including:
- **blog creation, & commenting**: various blog activity
- **blog analytics**: common analytics, top blog, newest blog, etc.
- **comment cleanup**: moving older comments to another collection
- **profile updating**: changing profile features

## Demo Overview
This simple program will generate queries similar to what you might find
in a simple blog application program.

## TODO: New Features to implement
1. **login**: feature needs to be defined and added
2. **logout**: feature needs to defined and added
3. **blog share stats**: feature needs to be defined and added
4. **blog comments on comments**: feature needs to be defined and added
5. **registration**: feature needs to be defined and added
6. **deactivation**: feature needs to be defined and added
7. **MongoDB 4.0 Features**: integrate 3.6 & 4.0 features including change
streams, retry writes, transactions, causal consistency, etc.
8. **change streams**: introduce change streams and a notification collection

### Extended Goals
Implement a document model which allows for a more advanced content management
use cases, some of the things we are thinking about:
1. **content workflows**: moving content through stages as it is developed
2. **advertising option**: adding add content
3. **advanced analytics**: how long someone stays on a page
4. **various counts**: show things like sort of counts (round about - might miss some)
5. **workload isolation**: possibility to implement isolation for analytics


## Change Log

| Date       | Change                                   |
| ---------- | ---------------------------------------- |
| 03-07-2018 | Moved to `loader.blog_example` package   |
|            | Properly commented `loader.blog_example` |
|            | Added `BlogOverview.md`                  |
|            | Added `stats` to user profile            |
|            | Cleaned up `generate_blog` functions     |


