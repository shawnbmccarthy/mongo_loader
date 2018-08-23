import pymongo
from datetime import datetime as dt
from bson import Decimal128

MONGO_URI = 'mongodb://localhost:27017/demo'  # change this as needed
TO_INSERT = 100000  # 100k inserts at a time

if __name__ == '__main__':
    client = pymongo.MongoClient(MONGO_URI)
    db = client.get_database()
    coll = db['idxExample']
    coll.drop()

    to_insert = []
    # for(var i = 1, i <= TO_INSERT; i++) equivalent to
    for i in range(0, 8):
        for j in range(1, TO_INSERT + 1):
            to_insert.append(
                {
                    'userID': ''.join(('user_', str(j))),
                    'regRepNumber': ''.join(('rrn_', str(j))),
                    'customerBirthdate': dt.now(),
                    'acctTypeCode': ''.join(('atc_', str(j))),
                    'accountBalance': Decimal128(str(j * 1.00)),
                    'otherField': j + 1,
                    'anotherField': j * 2
                }
            )
        # silly code (could do better but oh well)
        if i == 2 or i == 3:
            for d in to_insert:
                del d['customerBirthdate']
        elif i == 4 or i == 5:
            for d in to_insert:
                del d['acctTypeCode']
        elif i == 6 or i == 7:
            for d in to_insert:
                del d['customerBirthdate']
                del d['acctTypeCode']

        # no error checking!!
        result = coll.insert_many(to_insert)
        to_insert.clear()
        print('inserted 100k docs')

    coll.create_index([
        ('userID', pymongo.ASCENDING),
        ('regRepNumber', pymongo.ASCENDING),
        ('customerBirthdate', pymongo.ASCENDING),
        ('acctTypeCode', pymongo.ASCENDING),
        ('accountBalance', pymongo.ASCENDING)
    ])
    print('created compound index (5-fields)')

    project = {
        '_id': 0,
        'userID': 1,
        'regRepNumber': 1,
        'customerBirthdate': 1,
        'acctTypeCode': 1,
        'accountBalance': 1
    }

    print('\nquery1')
    d = coll.find({'userID': 'user_1'}, project).explain()
    print('nReturned: {}'.format(d['executionStats']['nReturned']))
    print('executionTimeMillis {}'.format(d['executionStats']['executionTimeMillis']))
    print('totalKeysExamined {}'.format(d['executionStats']['totalKeysExamined']))
    print('totalDocsExamined {}'.format(d['executionStats']['totalDocsExamined']))

    print('\nquery2')
    d = coll.find(
        {'userID': 'user_1', 'regRepNumber': 'rrn_1', 'customerBirthdate': {'$ne': ''}, 'acctTypeCode': {'$ne': ''}},
        project).explain()
    print('nReturned: {}'.format(d['executionStats']['nReturned']))
    print('executionTimeMillis {}'.format(d['executionStats']['executionTimeMillis']))
    print('totalKeysExamined {}'.format(d['executionStats']['totalKeysExamined']))
    print('totalDocsExamined {}'.format(d['executionStats']['totalDocsExamined']))

    # can even use covered query here!
    print('\nquery3')
    d = coll.find(
        {'userID': 'user_1', 'regRepNumber': 'rrn_1', 'customerBirthdate': {'$ne': ''}, 'acctTypeCode': 'atc_1'},
        project).explain()
    print('nReturned: {}'.format(d['executionStats']['nReturned']))
    print('executionTimeMillis {}'.format(d['executionStats']['executionTimeMillis']))
    print('totalKeysExamined {}'.format(d['executionStats']['totalKeysExamined']))
    print('totalDocsExamined {}'.format(d['executionStats']['totalDocsExamined']))
