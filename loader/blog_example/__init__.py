import logging
import pymongo
import random
import time
from loader import data
from loader.utils import RepeatedTimer
from datetime import datetime as dt
from pymongo.errors import BulkWriteError

#
# 3.5 and earlier does not have secrets
#
try:
    import secrets as s
except ImportError:
    import loader.secrets as s

#
# 3.5 and earlier the random object does not have choices method
# we created a function in utils as the choices() method is an
# instance method
#
try:
    from random import choices
except ImportError:
    from loader.utils import choices

logger = logging.getLogger(__name__)

BLOG_TAGS = [
    'Admin',      'Advertising',  'Advice',         'Android',     'Anime',         'Apple',       'Architecture',
    'Art',        'Baking',       'Beauty',         'Blog',        'Blogging',      'Books',       'Business',
    'cars',       'Cartoons',     'Cats',           'Celebrities', 'Comedy',        'Comics',      'Cooking',
    'Cosmetics',  'Crafts',       'Cuisine',        'Culinary',    'Culture',       'Design',      'DIY',
    'Dogs',       'Drawing',      'Economy',        'Education',   'Entertainment', 'Environment', 'Events',
    'Exercise',   'Fantasy',      'Fashion',        'Fiction',     'Film',          'Fitness',     'Folk',
    'Food',       'Football',     'Fun',            'Funny',       'Gadgets',       'Games',       'Geek',
    'Google',     'Gossip',       'Graphic Design', 'Green',       'Health',        'History',     'Home',
    'Humor',      'Illustration', 'Indie',          'Inspiration', 'Internet',      'Landscape',   'Law',
    'Leadership', 'Lifestyle',    'Literature',     'Management',  'Marketing',     'Media',       'Mobile',
    'Money',      'Movies',       'Music',          'Nature',      'News',          'Painting',    'Pets',
    'Philosophy', 'Photography',  'Poetry',         'Politics',    'Recipes',       'Reviews',     'Sales',
    'Science',    'SEO',          'Shopping',       'Soccer',      'Software',      'Sports',      'Technology',
    'Television', 'Travel',       'Tutorials',      'Vacation',    'Videos',        'Web',         'Wildlife',
    'Wordpress',  'Work',         'Workouts',       'Workshops',   'Workstations',  'Writing',     'Zombies'
]
"""Set of top tags found on the web to be used"""

BLOG_CATEGORIES = [
    'Beauty',    'Business',     'Car',           'Career',     'Cat',         'Design',      'DIY',     'Dog',
    'Economics', 'Education',    'Entertainment', 'Fashion',    'Finance',     'Fitness',     'Food',    'Gaming',
    'Green',     'Health',       'History',       'Law',        'Lifestyle',   'Marketing',   'Medical', 'Money',
    'Movie',     'Music',        'Nature',        'Pet',        'Photography', 'Real Estate', 'Science', 'SEO',
    'Shopping',  'Social Media', 'Sports',        'Technology', 'Travel',      'University',  'Wedding', 'Wine'
]
"""Set of top categories found on the web to be used"""

GENERATE_BLOG_SECONDS = 2
"""Generate a new blog every 2 seconds"""

GENERATE_COMMENT_SECONDS = 2
"""Generate a new comment on a blog every 2 seconds"""

UPDATE_BLOG_SECONDS = 5
"""Update an existing blog every 5 seconds"""

UPDATE_USER_SECONDS = 2
"""Update a user profile every 2 seconds"""

TAG_ANALYTICS_SECONDS = 5
"""Execute tag analytics every 5 seconds"""

CLEANUP_BLOG_COMMENTS_SECONDS = 10
"""Cleanup blog comments every 10 seconds"""

CLEANUP_COMMENTS_SECONDS = 10
"""Remove older comments every 10 seconds"""

FIND_LATEST_BLOG_SECONDS = 2
"""Find the latest blog every 2 seconds"""

FIND_BLOGS_BY_AUTHOR_SECONDS = 2
"""Find all blogs by a give author every 2 seconds"""

FIND_BLOG_BY_TAGS_SECONDS = 2
"""Find blogs by tags every 2 seconds"""

FACET_SEARCH_SECONDS = 2
"""Run a faceted search every 2 seconds"""


def _generate_user():
    """
    generate a basic user profile for the blog application, the _id key will be used to get a free index.

    TODO: Build more advanced profile features
    :return:
    """
    logger.debug('attempting to generate a simple user')
    user = {
        'fname': random.choice(data.CAST_OF_CHARACTERS)[0],
        'lname': random.choice(data.CAST_OF_CHARACTERS)[1],
        'created_at': dt.now(),
        'pw': s.token_hex(30),
        'is_locked': False,
        'interests': choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 15)),
        'stats': {
            'likes': 0,
            'shares': 0,
            'read': 0
        }
    }

    # need to create these keys from existing user keys
    user['_id'] = user['fname'] + '.' + user['lname']
    user['email'] = user['fname'] + '.' + user['lname'] + '@' + random.choice(data.INTERNET_DOMAINS)
    return user


def _bulk_insert(coll, array, gte=1):
    """
    Attempt to insert an array of documents into the given collection, gte (great then or equal) is used to define a
    default length to check for the array, if no gte is provided any array of documents with size greater than or
    equal to one will be inserted.

    TODO: Error checking code

    :param coll:
    :param array:
    :param gte:
    :return:
    """
    if len(array) >= gte:
        logger.debug('attempting insert of %d documents' % len(array))
        try:
            res = coll.insert_many(array)
            logger.info('inserted %d documents using bulkd insert' % len(res.inserted_ids))
        except BulkWriteError as ex:
            logger.critical('exception(%d): %s, msg: %s' % (ex.code, str(ex), ex.details))
        return True
    return False


def generate_user(db, no_of_authors, no_of_users):
    """
    Generate initial set of users, inefficient as it is done one at a time causing lots of reads & writes

    TODO: make this more efficient & add proper error handling (validate res response for insert_one())

    :param db:
    :param no_of_authors:
    :param no_of_users:
    :return:
    """
    logger.info('attempting to generate %d authors and %d users' % (no_of_authors, no_of_users))
    for i in range(no_of_authors):
        user = _generate_user()
        while db['users'].count({'_id': user['_id']}) > 0:
            logger.debug('found duplicate user: %s, attempting new user' % user['_id'])
            user = _generate_user()
        user['is_author'] = True
        res = db['users'].insert_one(user)
        logger.debug('response: inserted %s' % res.acknowledged)

    for i in range(no_of_users):
        user = _generate_user()
        while db['users'].count({'_id': user['_id']}) > 0:
            logger.debug('found duplicate user: %s, attempting new user' % user['_id'])
            user = _generate_user()
        user['is_author'] = False
        res = db['users'].insert_one(user)
        logger.debug('response: inserted %s' % res.acknowledged)
    logger.info('finished generating users, total users: %d' % db['users'].count())


def generate_tags(db):
    """
    Generate a set of tags which will be used in the blogs

    :param db:
    :return:
    """
    logger.info('attepting to generate tags from BLOG_TAGS array')
    cache = []
    for i in BLOG_TAGS:
        cache.append({'_id': i, 'total_blogs': 0})
        if _bulk_insert(db['tags'], cache, 1000):
            cache.clear()
    _bulk_insert(db['tags'], cache, 1)
    logger.info('successfully inserted %d tags for analysis' % db['tags'].count())


def generate_blog(db):
    """
    Generate a lorem ipsum blog from 5 - 30 paragraphs which contains various tags & categories

    * changed limit(1) to limit(-1) for author search to close cursor after receiving initial batch as
      getmore() will not be called.
    * removed explicit call to create blog dictionary

    TODO: Error Checking for insert (validate res response for insert_one())
    TODO: Change Stream?

    :param db:
    :return:
    """
    logger.info('generating a blog')
    no_of_authors = db['users'].count({'is_author': True})
    author_cursor = db['users'].find({'is_author': True}, {'_id': 1})\
        .skip(random.randint(0, (no_of_authors-1))).limit(-1)
    res = db['blogs'].insert_one({
        'title': ' '.join(choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 5))),
        'tags': choices(BLOG_TAGS, k=random.randint(2, 12)),
        'categories': choices(BLOG_CATEGORIES, k=random.randint(2, 5)),
        'created_on': dt.now(),
        'author': author_cursor.next()['_id'],
        'content': '\n'.join(
            [data.LOREM_IPSUM[k] for k in choices(list(data.LOREM_IPSUM.keys()), k=random.randint(1, 40))]
        ),
        'is_locked': False
    })
    logger.info('successfully created new blog(%s)' % res.acknowledged)


def generate_comment(db):
    """
    generate a comment from a given user and add this to the blog

    * changed limit(1) to limit(-1) for user and blog to automatically call the cursor

    TODO: Add Sessions

    :param db:
    :return:
    """
    logger.debug('generate comments')
    no_of_users = db['users'].count({'is_author': False})
    user_cursor = db['users'].find({'is_author': False}, {'_id': 1}).skip(random.randint(0, (no_of_users-1))).limit(-1)
    no_of_blogs = db['blogs'].count()

    if no_of_blogs == 0:
        logger.info('no blogs to comment on')
        user_cursor.close()
        return False

    blog_cursor = db['blogs'].find().skip(random.randint(0, (no_of_blogs-1))).limit(-1)
    blog_doc = blog_cursor.next()

    comment = {
        'date': dt.now(),
        'cmmt': data.LOREM_IPSUM_COMMENTS[random.randint(1, len(data.LOREM_IPSUM_COMMENTS))],
        'user': user_cursor.next()['_id']
    }

    doc = db['blogs'].find_one_and_update({'_id': blog_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    while doc is None:
        time.sleep(1)
        doc = db['blogs'].find_one_and_update(
            {'_id': blog_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}}
        )

    doc = db['blogs'].find_one_and_update(
        {'_id': blog_doc['_id'], 'is_locked': True}, {'$push': {'comments': comment}, '$set': {'is_locked': False}}
    )

    if doc is None:
        logger.warning('adding comment failed')
    else:
        logger.info('successfully create comment for blog')


def generate_tag_analytics(db):
    """
    Generate some tag analytics

    TODO: Describe the analytics here, maybe something more interesting?
    TODO: Error handling for aggregate?

    :param db:
    :return:
    """
    logger.debug('generate_tag_analytics')
    for doc in db['blogs'].aggregate([
        {'$project': {'_id': 0, 'tags': 1}},
        {'$unwind': '$tags'},
        {'$group': {'_id': '$tags', 'count': {'$sum': 1}}}]
    ):
        db['tags'].update_one({'_id': doc['_id']}, {'$set': {'total_blogs': doc['count']}})
    logger.info('finished generating tag analytics')


def cleanup_blog_comments(db):
    """
    Remove older comments from the blog (storing only the newest 20 comments embedded)

    TODO: Transactions?
    TODO: make use of _bulk_insert() line 321
    TODO: confirm unlock? line 322

    :param db:
    :return:
    """
    logger.debug('cleanup_blog_comments')

    counter = 0
    for doc in db['blogs'].find({'comments.21': {'$exists': True}}):
        to_update = db['blogs'].find_one_and_update(
            {'_id': doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}}
        )

        while to_update is None:
            time.sleep(1)
            logger.debug('was not able to get a lock, trying again...')
            to_update = db['blogs'].find_one_and_update(
                {'_id': doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}}
            )

        to_insert = to_update['comments'][20:]
        for i in to_insert:
            i['blog_id'] = to_update['_id']
        db['comments'].insert_many(to_insert)
        db['blogs'].find_one_and_update(
            {'_id': doc['_id'], 'is_locked': True},
            {'$set': {'is_locked': False, 'comments': to_update['comments'][:20]}}
        )
        counter = counter + 1

    logger.info('cleaned up %d documents' % counter)


def find_latest_blogs(db):
    """
    find the latest 10 blogs

    TODO: make this more interesting, what about updated_on, by tags, categories, etc.

    :param db:
    :return:
    """
    logger.debug('find_latest_blogs')
    counter = 0
    for doc in db['blogs'].find().sort([('created_on', pymongo.DESCENDING)]).limit(10):
        logger.debug('found doc: %s' % doc['_id'])
        counter = counter + 1
    logger.info('found the latest %d blogs' % counter)


def find_blog_by_tags(db):
    """
    find blog by tags

    TODO: Again a bit boring, can we make this more interesting

    :param db:
    :return:
    """
    logger.debug('find_blog_by_tags')
    tags = choices(data.LOREM_IPSUM_TAGS, k=random.randint(1, 10))
    counter = 0
    for doc in db['blogs'].find({'tags': {'$in': tags}}):
        logger.debug('found doc: %s' % doc['_id'])
        counter = counter + 1
    logger.info('found %d documents based off tags' % counter)


def find_blogs_by_author(db):
    """
    find blogs by author, sorted by date

    TODO: can we make this something more interesting

    :param db:
    :return:
    """
    logger.debug('find_blog_by_author')
    a_count = db['users'].count({'is_author': True})
    a_cursor = db['users'].find({'is_author': True}, {'_id': 1}).skip(random.randint(0, (a_count-1))).limit(1)
    counter = 0
    for doc in db['blogs'].find({'author': a_cursor.next()['_id']}):
        logger.debug('found doc: %s' % doc['_id'])
        counter = counter + 1
    logger.info('found %d blogs by author' % counter)


def blog_facet_search(db):
    """
    create a facet which would represent something  like a home page

    TODO: maybe introduce some fun analytics here

    :param db:
    :return:
    """
    logger.debug('blog_facet_search')
    counter = 0
    for doc in db['blogs'].aggregate([{
        '$facet': {
            'byTags': [{'$unwind': '$tags'}, {'$sortByCount': '$tags'}],
            'byAuthor': [{'$sortByCount': '$author'}],
            'last10': [{'$sort': {'created_on': -1}}, {'$limit': 10}]
        }
    }]):
        logger.debug('found doc: %s' % doc)
        counter = counter + 1
    logger.info('ran facet on blogs returned %d docs' % counter)


def cleanup_comments(db):
    """
    Simple function used to remove older comments (currently we only hold 100k comments)

    TODO: change this (possibly get rid of this) and drop comments when we drop a blog?

    :param db:
    :return:
    """
    logger.debug('cleanup_comments')
    c_count = db['comments'].count()
    counter = 0
    if c_count < 1000000:
        logger.info('too few comments, not going to run cleanup')
        return

    for doc in db['comments'].find().sort({'date': -1}).skip(100000):
        db['comments'].delete_one({'_id': doc['_id']})
        counter = counter + 1

    logger.info('removed %d comments' % counter)


def update_blog(db):
    """
    Update the blog, simply change the content right now

    TODO: change streams here?
    TODO: what about versioning?

    :param db:
    :return:
    """
    logger.debug('update a single blog - changing contents')
    b_count = db['blogs'].count()
    b_cursor = db['blogs'].find().skip(random.randint(0, (b_count-1))).limit(-1)
    b_doc = b_cursor.next()

    doc = db['blogs'].find_one_and_update({'_id': b_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    while doc is None:
        doc = db['blogs'].find_one_and_update({'_id': b_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    update = db['blogs'].find_one_and_update(
        {'_id': doc['_id'], 'is_locked': True},
        {'$set': {
            'is_locked': False,
            'content': '\n'.join(
                [data.LOREM_IPSUM[k] for k in choices(list(data.LOREM_IPSUM.keys()), k=random.randint(1, 40))]
            ),
            'updated_on': dt.now()
        }}
    )

    if update is None:
        logger.warning('update did not work for %s, must validate lock' % doc['_id'])
    else:
        logger.info('successfully updated document')


def update_user(db):
    """
    Update user information, simply changing interests

    TODO: calculate stats

    :param db:
    :return:
    """
    logger.debug('update a single user - changing tags')
    u_count = db['users'].count()
    u_cursor = db['users'].find().skip(random.randint(0, (u_count-1))).limit(-1)
    u_doc = u_cursor.next()

    doc = db['users'].find_one_and_update({'_id': u_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    while doc is None:
        doc = db['blogs'].find_one_and_update({'_id': u_doc['_id'], 'is_locked': False}, {'$set': {'is_locked': True}})

    update = db['users'].find_one_and_update(
        {'_id': doc['_id'], 'is_locked': True},
        {'$set': {
            'is_locked': False,
            'interests': choices(data.LOREM_IPSUM_TAGS, k=random.randint(2, 15)),
            'updated_on': dt.now()
        }}
    )

    if update is None:
        logger.warning('update did not work for %s, must validate lock' % doc['_id'])
    else:
        logger.info('successfully updated user document')


def start_blog_run(db, no_of_blogs=10000, no_of_authors=100, no_of_users=900):
    """
    start the blog run, using the RepeatedTimer class, threads are generated and run every X seconds

    :param db:
    :param no_of_blogs:
    :param no_of_authors:
    :param no_of_users:
    :return:
    """
    logger.info(
        'attempting to start blog demo application (no_of_blogs: %d, no_of_authors: %d, no_of_users: %d)'
        % (no_of_blogs, no_of_authors, no_of_users)
    )

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
    tag_analytics_runner = RepeatedTimer(TAG_ANALYTICS_SECONDS, -1, generate_tag_analytics, db)
    update_user_runer = RepeatedTimer(UPDATE_USER_SECONDS, -1, update_user, db)

    blog_create_runner.start()
    blog_comment_runner.start()
    latest_blogs_runner.start()
    blogs_by_tags_runner.start()
    blogs_by_author_runner.start()
    blog_comment_cleaner_runner.start()
    facet_runner.start()
    comment_cleanup_runner.start()
    update_blog_runner.start()
    tag_analytics_runner.start()
    update_user_runer.start()

    while blog_create_runner.counter <= blog_create_runner.iterations:
        logger.info('still running: %d <= %d' % (blog_create_runner.counter, blog_create_runner.iterations))
        time.sleep(10)

    logger.info('created all blogs, now just running updates and good stuff')
    blog_create_runner.stop()
