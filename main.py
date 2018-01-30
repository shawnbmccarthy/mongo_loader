import argparse
import logging.config
import pymongo
import sys
from loader import blog_example, log_example

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

loader_demos = {
    'blog': blog_example.start_blog_run
}

def setup_parser():
    logger.debug('setting up parser')
    parser = argparse.ArgumentParser(description='loader program')
    parser.add_argument('--url', type=str, action='store', help='mongodb url', required=False,
                        default='mongodb://localhost:27017/test')
    parser.add_argument('--drop', action='store_true', required=False, default=False)

    loader_parser = parser.add_subparsers(help='help for loader types')

    blog_parser = loader_parser.add_parser('blog', help='blog loader help')
    blog_parser.set_defaults(loader='blog')
    blog_parser.add_argument('--users', type=int, action='store', help='number of users', default=900)
    blog_parser.add_argument('--authors', type=int, action='store', help='number of authors', default=100)
    blog_parser.add_argument('--blogs', type=int, action='store', help='number of blogs to create', default=10000)

    #
    # TODO: log line use case
    #
    # log_parser = loader_parser.add_parser('log', help='log line loader help')
    # log_parser.set_defaults(which='log')
    return parser

#
if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    parser = setup_parser()
    args = parser.parse_args()

    clnt = pymongo.MongoClient(args.url)

    print(args)

    try:
        db = clnt.get_database()
        if args.drop:
            logger.info('dropping database %s before we begin' % db.name)
            clnt.drop_database(db.name)
    except:
        logger.error('database not set in mongodb url, cannot continue')
        logger.error('use standard mongo url with a valid database name')
        sys.exit(1)

    if 'loader' not in args:
        logger.info('setting blog demo to be the default loader')
        args.loader = 'blog'

    if args.loader == 'blog':
        blog_example.start_blog_run(db, no_of_authors=args.authors, no_of_users=args.users)
    else:
        logger.error('invalid loader: %s, cannot continue' % args.loader)