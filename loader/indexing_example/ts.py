#
# Example of holding time series data for a stock ticker for a given day
# one document = 1 day
#
import pymongo
import random
from datetime import datetime as dt

MONGO_URI = 'mongodb://localhost:27017/ts_demo'


def max_subdoc(db):
    """
    max for sub documment (or map of maps)
    pros:
    - clean look
    - the key has meaning
    - easy to read
    - no loss of information
    cons:
    - the key has meaning (not for computer) hard to manipulate the field - need to name each field
    - harder to process
    - big aggregations (can we do better with these)
    :param db:
    :return:
    """
    m_sub = {'$match': {'s': 'AAPL', 't': 'sub'}}
    p_sub_ota = {
        '$project': {
            's': 1, 't': 1, 'd': 1,
            'p.1': {'$objectToArray': '$p.1'},
            'p.2': {'$objectToArray': '$p.2'},
            'p.3': {'$objectToArray': '$p.3'},
            'p.4': {'$objectToArray': '$p.4'},
            'p.5': {'$objectToArray': '$p.5'},
            'p.6': {'$objectToArray': '$p.6'},
            'p.7': {'$objectToArray': '$p.7'},
            'p.8': {'$objectToArray': '$p.8'},
            'p.9': {'$objectToArray': '$p.9'},
            'p.10': {'$objectToArray': '$p.10'},
            'p.11': {'$objectToArray': '$p.11'},
            'p.12': {'$objectToArray': '$p.12'},
            'p.13': {'$objectToArray': '$p.13'},
            'p.14': {'$objectToArray': '$p.14'},
            'p.15': {'$objectToArray': '$p.15'},
            'p.16': {'$objectToArray': '$p.16'},
            'p.17': {'$objectToArray': '$p.17'},
            'p.18': {'$objectToArray': '$p.18'},
            'p.19': {'$objectToArray': '$p.19'},
            'p.20': {'$objectToArray': '$p.20'},
            'p.21': {'$objectToArray': '$p.21'},
            'p.22': {'$objectToArray': '$p.22'},
            'p.23': {'$objectToArray': '$p.23'},
            'p.24': {'$objectToArray': '$p.24'}
        }
    }
    p_sub_max = {
        '$project': {
            's': 1, 't': 1, 'd': 1,
            'max_p.1': {'$max': '$p.1.v'},
            'max_p.2': {'$max': '$p.2.v'},
            'max_p.3': {'$max': '$p.3.v'},
            'max_p.4': {'$max': '$p.4.v'},
            'max_p.5': {'$max': '$p.5.v'},
            'max_p.6': {'$max': '$p.6.v'},
            'max_p.7': {'$max': '$p.7.v'},
            'max_p.8': {'$max': '$p.8.v'},
            'max_p.9': {'$max': '$p.9.v'},
            'max_p.10': {'$max': '$p.10.v'},
            'max_p.11': {'$max': '$p.11.v'},
            'max_p.12': {'$max': '$p.12.v'},
            'max_p.13': {'$max': '$p.13.v'},
            'max_p.14': {'$max': '$p.14.v'},
            'max_p.15': {'$max': '$p.15.v'},
            'max_p.16': {'$max': '$p.16.v'},
            'max_p.17': {'$max': '$p.17.v'},
            'max_p.18': {'$max': '$p.18.v'},
            'max_p.19': {'$max': '$p.19.v'},
            'max_p.20': {'$max': '$p.20.v'},
            'max_p.21': {'$max': '$p.21.v'},
            'max_p.22': {'$max': '$p.22.v'},
            'max_p.23': {'$max': '$p.23.v'},
            'max_p.24': {'$max': '$p.24.v'}
        }
    }
    p_sub_max_ota = {
        '$project': {
            's': 1, 't': 1, 'd': 1, 'hour_high': {'$objectToArray': '$max_p'}
        }
    }
    p_sub_max_day = {
        '$project': {
            's': 1, 't': 1, 'd': 1, 'day_high': {'$max': '$hour_high.v'}
        }
    }

    # max for each hour
    print('max for each hour')
    for d in db['ts'].aggregate([m_sub, p_sub_ota, p_sub_max]):
        print(d)

    print('max for the day')
    for d in db['ts'].aggregate([m_sub, p_sub_ota, p_sub_max, p_sub_max_ota, p_sub_max_day]):
        print(d)


def max_array_of_subdoc(db):
    """
    max for array of subdocs
    pros:
    - easier agg framework
    - smaller code set
    cons:
    - potential loss of hourly information ($addToSet does not guarantee order, but not sure about $push)
    :param db:
    :return:
    """
    m_aos = {'$match': {'s': 'AAPL', 't': 'aos'}}
    u_aos = {'$unwind': '$p'}
    p_aos = {
        '$project': {
            's': 1, 't': 1, 'd': 1, 'p': {'$objectToArray': '$p'}
        }
    }
    g_aos = {
        '$group': {
            '_id': '$_id',
            's': {'$first': '$s'},
            't': {'$first': '$t'},
            'd': {'$first': '$d'},
            'hour_high': {'$push': {'$max': '$p.v'}}
        }
    }
    p_aos_day = {
        '$project': {
            's': 1, 't': 1, 'd': 1, 'day_high': {'$max': '$hour_high'}
        }
    }

    print('max for each hour')
    for d in db['ts'].aggregate([m_aos, u_aos, p_aos, g_aos]):
        print(d)

    print('max for the day')
    for d in db['ts'].aggregate([m_aos, u_aos, p_aos, g_aos, p_aos_day]):
        print(d)


def max_array_of_array(db):
    """
    max for array of arrays
    pros:
    - even easier aggregation
    cons:
    - potential loss of hourly information ($addToSet does not guarantee order, but not sure about $push)
    :param db:
    :return:
    """
    m_aoa = {'$match': {'s': 'AAPL', 't': 'aoa'}}
    u_aoa = {'$unwind': '$p'}
    g_aoa = {
        '$group': {
            '_id': '$_id',
            's': {'$first': '$s'},
            't': {'$first': '$t'},
            'd': {'$first': '$d'},
            'hour_high': {'$push': {'$max': '$p'}}
        }
    }
    p_aoa_day = {
        '$project': {
            's': 1, 't': 1, 'd': 1, 'day_high': {'$max': '$hour_high'}
        }
    }
    db['ts'].aggregate([m_aoa])

    print('max for each hour')
    for d in db['ts'].aggregate([m_aoa, u_aoa, g_aoa]):
        print(d)

    print('max for the day')
    for d in db['ts'].aggregate([m_aoa, u_aoa, g_aoa, p_aoa_day]):
        print(d)


if __name__ == '__main__':
    c = pymongo.MongoClient(MONGO_URI)
    db = c.get_database()
    db['ts'].drop()
    d = dt.now()

    # subdocument
    # p: {1: {0: p1, ... 59: p59}, ... 24: {0: p1, ... 59: p59}}
    aapl_sub = {
        's': 'AAPL',
        't': 'sub',
        'd': dt(year=d.year, month=d.month, day=d.day),
        'p': {}
    }

    # array of subdocuments
    # array of 24 elements [{m0: p0, ... m59: p59}, {m0: p0, .... m59: p59}]
    aapl_aos = {
        's': 'AAPL',
        't': 'aos',
        'd': dt(year=d.year, month=d.month, day=d.day),
        'p': []
    }

    # array of array
    # 24 arrays of 60 arrays:
    # [[p1_0, ..., p1_59], ..., [p24_0, ..., p24_59]]
    aapl_aoa = {
        's': 'AAPL',
        't': 'aoa',
        'd': dt(year=d.year, month=d.month, day=d.day),
        'p': []
    }

    for i in range(1, 25):
        m_aoa_arr = []
        m_aos_dict = {}
        if i not in aapl_sub['p']:
            aapl_sub['p'][str(i)] = {}
        for j in range(0, 60):
            # create sub elements
            m_price = round(random.uniform(100, 200), 2)
            m_aoa_arr.append(m_price)
            m_aos_dict[str(j)] = m_price
            aapl_sub['p'][str(i)][str(j)] = m_price
        aapl_aoa['p'].append(m_aoa_arr)
        aapl_aos['p'].append(m_aos_dict)

    db['ts'].insert_many([aapl_sub, aapl_aoa, aapl_aos])

    print('\n---------------------------------------------------------------------------------------------------')
    max_subdoc(db)
    print('---------------------------------------------------------------------------------------------------\n')
    print('\n---------------------------------------------------------------------------------------------------')
    max_array_of_subdoc(db)
    print('---------------------------------------------------------------------------------------------------\n')
    print('\n---------------------------------------------------------------------------------------------------')
    max_array_of_array(db)
    print('---------------------------------------------------------------------------------------------------\n')
