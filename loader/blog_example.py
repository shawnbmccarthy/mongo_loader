import logging
import pymongo
import random
import time
from loader import data
from loader.utils import RepeatedTimer
from datetime import datetime as dt
from pymongo.errors import BulkWriteError

# 3.5 and earlier does not have secrets
try:
    import secrets as s
except:
    import loader.secrets as s

# 3.5 and earlier the random object does not have choices method
# we created a function in utils as the choices() method is an
# instance method
try:
    from random import choices
except:
    from loader.utils import choices

logger = logging.getLogger(__name__)

#
# simple loader which will demo a simple blog with the following collections:
# users
# blogs
# comments
# tags
#
# How it runs:
#

# timeings for thread runs
GENERATE_BLOG_SECONDS=5
GENERATE_COMMENT_SECONDS=2
UPDATE_BLOG_SECONDS=10
UPDATE_AUTHOR=5
TAG_ANALYTICS_SECONDS=10
CLEANUP_BLOG_COMMENTS_SECONDS=20
CLEANUP_COMMENTS_SECONDS=20
FIND_LATEST_BLOG_SECONDS=5
FIND_BLOGS_BY_AUTHOR_SECONDS=5
FIND_BLOG_BY_TAGS_SECONDS=5
FACET_SEARCH_SECONDS=5

def _generate_user():
    user = {}

    user['fname'] = random.choice(data.CAST_OF_CHARACTERS)[0]
    user['lname'] = random.choice(data.CAST_OF_CHARACTERS)[1]
    user['_id'] = user['fname'] + '.' + user['lname']
    user['email'] = user['fname'] + '.' + user['lname'] + '@' + random.choice(data.INTERNET_DOMAINS)
    user['created_at'] = dt.now()
    user['pw'] = s.token_hex(30)
    user['is_locked'] = False
    user['interests'] = choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 15))
    return user

#
# TODO: Error checking
#
def _bulk_insert(coll, array, gte=1):
    if len(array) >= gte:
        logger.debug('attempting insert of %d documents' % len(array))
        try:
            res = coll.insert_many(array)
            logger.info('inserted %d documents using bulkd insert' % len(res.inserted_ids))
        except BulkWriteError as ex:
            logger.critical('exception(%d): %s, msg: %s' % (ex.code, str(ex), ex.details))
        return True
    return False


#
# generate initial set of users
# highly inefficient doing one at a time with a bunch of reads & writes (but it is a start)
#
# TODO: error checking & bulk inserts
#
def generate_user(db, no_of_authors, no_of_users):
    logger.info('attempting to generate %d authors and %d users' % (no_of_authors, no_of_users))
    for i in range(no_of_authors):
        user = _generate_user()
        while db['users'].count({'_id': user['_id']}) > 0:
            logger.debug('found duplicate user: %s, attempting new user' % user['_id'])
            user = _generate_user()
        user['is_author'] = True
        res = db['users'].insert_one(user)

    for i in range(no_of_users):
        user = _generate_user()
        while db['users'].count({'_id': user['_id']}) > 0:
            logger.debug('found duplicate user: %s, attempting new user' % user['_id'])
            user = _generate_user()
        user['is_author'] = False
        res = db['users'].insert_one(user)
    logger.info('finished generating users, total users: %d' % db['users'].count())
#
# generate a set of tags which will be used in the blogs (100 tags)
#
def generate_tags(db):
    logger.info('attepting to generate tags from lorem ipsum')
    cache = []
    for i in data.LOREM_IPSUM_TAGS:
        cache.append({'_id': i, 'total_blogs': 0})
        if _bulk_insert(db['tags'], cache, 1000):
            cache.clear()
    _bulk_insert(db['tags'], cache, 1)
    logger.info('successfully inserted %d tags for analysis' % db['tags'].count())

#
# generate blogs with a random number of paragraphs (5 - 30)
#
def generate_blog(db):
    logger.info('generating a blog')
    no_of_authors = db['users'].count({'is_author': True})
    author_cursor = db['users'].find({'is_author': True}, {'_id': 1}).skip(random.randint(0, (no_of_authors-1))).limit(1)
    blog = {}
    blog['title'] = ' '.join(choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 5)))
    blog['tags'] = choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 12))
    blog['created_on'] = dt.now()
    blog['author'] = author_cursor.next()['_id']
    blog['content'] = '\n'.join([data.LOREM_IPSUM[k] for k in choices(list(data.LOREM_IPSUM.keys()), k=random.randint(1,40))])
    blog['is_locked'] = False

    author_cursor.close()
    res = db['blogs'].insert_one(blog)
    logger.info('successfully created new blog')

#
# generate comments on existing blogs
#
def generate_comment(db):
    logger.debug('generate comments')
    no_of_users = db['users'].count({'is_author': False})
    user_cursor = db['users'].find({'is_author': False}, {'_id': 1}).skip(random.randint(0, (no_of_users-1))).limit(1)
    no_of_blogs = db['blogs'].count()

    if no_of_blogs == 0:
        logger.info('no blogs to comment on')
        user_cursor.close()
        return False

    blog_cursor = db['blogs'].find().skip(random.randint(0, (no_of_blogs-1))).limit(1)
    blog_doc = blog_cursor.next()

    comment = {}
    comment['date'] = dt.now()
    comment['cmmt'] = data.LOREM_IPSUM_COMMENTS[random.randint(1, len(data.LOREM_IPSUM_COMMENTS))]
    comment['user'] = user_cursor.next()['_id']

    doc = db['blogs'].find_one_and_update({'_id': blog_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    while doc == None:
        time.sleep(1)
        doc = db['blogs'].find_one_and_update({'_id': blog_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    doc = db['blogs'].find_one_and_update({'_id': blog_doc['_id'], 'is_locked': True}, {'$push': {'comments': comment}, '$set': {'is_locked': False}})

    if doc == None:
        logger.warning('adding comment failed')
    else:
        logger.info('successfully create comment for blog')

    user_cursor.close()
    blog_cursor.close()

#
# longer running analytics to update tag data (number of blogs with tags etc.)
#
def generate_tag_analytics(db):
    logger.debug('generate_tag_analytics')
    for doc in db['blogs'].aggregate([{'$project': {'_id': 0, 'tags': 1}}, {'$unwind': '$tags'}, {'$group': {'_id': '$tags', 'count': {'$sum': 1}}}]):
        db['tags'].update_one({'_id': doc['_id']}, {'$set': {'total_blogs': doc['count']}})
    logger.info('finished generating tag analytics')

#
# move older comments to comments collection
#
def cleanup_blog_comments(db):
    logger.debug('cleanup_blog_comments')

    counter = 0
    for doc in db['blogs'].find({'comments.21': {'$exists': True}}):
        to_update = db['blogs'].find_one_and_update({'_id': doc['_id'], 'is_locked': False},{'$set': {'is_locked': True}})
        while to_update == None:
            time.sleep(1)
            to_update = db['blogs'].find_one_and_update({'_id': doc['_id'], 'is_locked': False},{'$set': {'is_locked': True}})
        to_insert = to_update['comments'][20:]
        for i in to_insert:
            i['blog_id'] = to_update['_id']
        db['comments'].insert_many(to_insert)
        db['blogs'].find_one_and_update({'_id': doc['_id'], 'is_locked': True}, {'$set': {'is_locked': False, 'comments': to_update['comments'][:20]}})
        counter = counter + 1

    logger.info('cleaned up %d documents' % counter)
#
# find the latest blogs
#
def find_latest_blogs(db):
    logger.debug('find_latest_blogs')
    counter = 0
    for doc in db['blogs'].find().sort([('created_on', pymongo.DESCENDING)]).limit(10):
        counter = counter + 1
    logger.info('found the latest %d blogs' % counter)

#
# find blog by tags
#
def find_blog_by_tags(db):
    logger.debug('find_blog_by_tags')
    tags = choices(data.LOREM_IPSUM_TAGS, k=random.randint(1, 10))
    counter = 0
    for doc in db['blogs'].find({'tags': {'$in': tags}}):
        counter = counter + 1
    logger.info('found %d documents based off tags' % counter)

#
# find blogs by author (sorted by date)
#
def find_blogs_by_author(db):
    logger.debug('find_blog_by_author')
    a_count = db['users'].count({'is_author': True})
    a_cursor = db['users'].find({'is_author': True}, {'_id': 1}).skip(random.randint(0, (a_count-1))).limit(1)
    counter = 0
    for doc in db['blogs'].find({'author': a_cursor.next()['_id']}):
        counter = counter + 1
    logger.info('found %d blogs by author' % counter)

#
# create a facet where left hand:
# authors, tags, and latest docs
#
def blog_facet_search(db):
    logger.debug('blog_facet_search')
    counter = 0
    for doc in db['blogs'].aggregate([{
        '$facet': {
            'byTags': [{'$unwind': '$tags'}, {'$sortByCount': '$tags'}],
            'byAuthor': [{'$sortByCount': '$author'}],
            'last10': [{'$sort': {'created_on': -1}}, {'$limit': 10}]
        }
    }]):
        counter = counter + 1
    logger.info('ran facet on blogs returned %d docs' % counter)

def cleanup_comments(db):
    logger.debug('cleanup_comments')
    c_count = db['comments'].count()
    counter = 0
    if c_count < 100000:
        logger.info('too few comments, not going to run cleanup')
        return

    for doc in db['comments'].find().sort({'date': -1}).skip(100000):
        db['comments'].delete_one({'_id': doc['_id']})
        counter = counter + 1

    logger.info('removed %d comments' % counter)

def update_blog(db):
    logger.debug('update a single blog - changing contents')
    b_count = db['blogs'].count()
    b_cursor = db['blogs'].find().skip(random.randint(0, (b_count-1))).limit(1)
    b_doc = b_cursor.next()

    doc = db['blogs'].find_one_and_update({'_id': b_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    while doc == None:
        doc = db['blogs'].find_one_and_update({'_id': b_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    update = db['blogs'].find_one_and_update(
        {'_id': doc['_id'], 'is_locked': True},
        {'$set': {
            'is_locked': False,
            'content': '\n'.join([data.LOREM_IPSUM[k] for k in choices(list(data.LOREM_IPSUM.keys()), k=random.randint(1,40))]),
            'updated_on': dt.now()
        }}
    )

    if update == None:
        logger.warning('update did not work for %s, must validate lock' % doc['_id'])
    else:
        logger.info('successfully updated document')
    b_cursor.close()

#
# start run, will drop existing database, create users, then the tags, then the blogs
# will provide comments and updates to the blog for some amount of time (could be forever)
#
def start_blog_run(db, no_of_blogs=10000, no_of_authors=100, no_of_users=900):
    logger.info('attempting to start blog demo application (no_of_blogs: %d, no_of_authors: %d, no_of_users: %d)' % (no_of_blogs, no_of_authors, no_of_users))

    generate_user(db, no_of_authors, no_of_users)
    generate_tags(db)

    blog_create_runner = RepeatedTimer(GENERATE_BLOG_SECONDS, no_of_blogs, generate_blog, db)
    blog_comment_runner = RepeatedTimer(GENERATE_COMMENT_SECONDS, -1, generate_comment, db)
    blog_comment_cleaner_runner = RepeatedTimer(CLEANUP_BLOG_COMMENTS_SECONDS, -1, cleanup_blog_comments, db)
    latest_blogs_runner = RepeatedTimer(FIND_LATEST_BLOG_SECONDS, -1, find_latest_blogs, db)
    blogs_by_tags_runner = RepeatedTimer(FIND_BLOG_BY_TAGS_SECONDS, -1, find_blog_by_tags, db)
    blogs_by_author_runner = RepeatedTimer(FIND_BLOGS_BY_AUTHOR_SECONDS, -1, find_blogs_by_author, db)
    facet_runner = RepeatedTimer(FACET_SEARCH_SECONDS, -1, blog_facet_search, db)
    comment_cleanup_runner = RepeatedTimer(CLEANUP_COMMENTS_SECONDS, -1, cleanup_comments, db)
    update_blog_runner = RepeatedTimer(UPDATE_BLOG_SECONDS, -1, update_blog, db)

    blog_create_runner.start()
    blog_comment_runner.start()
    latest_blogs_runner.start()
    blogs_by_tags_runner.start()
    blogs_by_author_runner.start()
    blog_comment_cleaner_runner.start()
    facet_runner.start()
    comment_cleanup_runner.start()
    update_blog_runner.start()

    while blog_create_runner.counter <= blog_create_runner.iterations:
        logger.info('still running: %d <= %d' % (blog_create_runner.counter, blog_create_runner.iterations))
        time.sleep(10)

    logger.info('created all blogs, now just running updates and good stuff')
    blog_create_runner.stop()