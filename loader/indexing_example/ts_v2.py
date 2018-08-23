#
# another timeseries demo
# pros:
# - easy to read
# - easy to aggregate
# - abstract enough to keep aggregations command simple
# - easily shape to output data to a graphing tool as needed
# cons:
# - many documents, each ticker has 24 documents per day
# - might need to look at preagging to roll up older data (i.e. weekly, monthly, etc.)
#
import pymongo
import random
from datetime import datetime as dt

MONGO_URI = 'mongodb://localhost:27017/ts_demo'


if __name__ == '__main__':
    c = pymongo.MongoClient(MONGO_URI)
    db = c.get_database()
    db['ts_v2'].drop()

    today = dt.now()

    aapl = {
        's': 'AAPL',
        'd': dt(year=today.year, month=today.month, day=today.day),
        'p': []
    }

    # create 24 documents - 1 for each hour
    for hour in range(0, 24):
        if '_id' in aapl:
            del aapl['_id']
        aapl['h'] = hour
        aapl['p'].clear()
        for minute in range(0,60):
            aapl['p'].append({'k': minute, 'v': round(random.uniform(100,200),2)})
        db['ts_v2'].insert_one(aapl)

    # find max for each hour and create one document
    for doc in db['ts_v2'].aggregate([
        {'$match': {'s': 'AAPL', 'd': dt(year=today.year, month=today.month, day=today.day)}},
        {'$project': {'s': 1, 'd': 1, 'h': 1, 'hourly_high': {'$max': '$p.v'}}},
        {'$group': {'_id': '$s', 'd': {'$first': '$d'}, 'hourly_highs': {'$push': {'h': '$h', 'v': '$hourly_high'}}}}
    ]):
        print(doc)

    # find max for the day
    for doc in db['ts_v2'].aggregate([
        {'$match': {'s': 'AAPL', 'd': dt(year=today.year, month=today.month, day=today.day)}},
        {'$project': {'s': 1, 'd': 1, 'h': 1, 'hourly_high': {'$max': '$p.v'}}},
        {'$group': {'_id': '$s', 'd': {'$first': '$d'}, 'hourly_highs': {'$push': {'h': '$h', 'v': '$hourly_high'}}}},
        {'$project': {'s': '$_id', 'd': 1, 'daily_high': {'$max': '$hourly_highs.v'}}}
    ]):
        print(doc)