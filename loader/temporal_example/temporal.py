import pymongo
import random

from datetime import datetime as dt, timedelta as td

S_PARTS = [
    'filter',    'screen',     'motherboard', 'glass',     'crystal', 'cpu',    'chip',  'controller', 'processor',
    'simm',      'dimm',       'memory'       'marker',    'paper',   'card',   'cloth', 'hinge',      'metal',
    'board',     'whiteboard', 'plastic',     'protector', 'pen',     'pencil', 'cup',   'bag',        'usb',
    'notebook',  'stand',      'box',         'keyboard',  'light',   'bulb',   'wire',  'charger',    'chair',
    'powercord', 'strap',      'diode',       'magnet',    'bottle',  'fan',    'bowl',  'towel',      'tub'
]
"""possible parts used in our demo"""

# possible supplier termination reasons
ACTIVE = {'code': 'A', 'cmmnt': 'started new contract'}
SUSPENDED = {'code': 'S', 'cmmnt': 'contract suspended for some reason'}
TERMINATED = {'code': 'T', 'cmmnt': 'contract terminated'}
REPLACED = {'code': 'R', 'cmmnt': 'contract replaced'}
REINSTATED = {'code': 'I', 'cmmnt': 'supension lifted'}

# possible parts termination reasons
EOL = {'code': 'E', 'cmmnt': 'part has hit end of life'}
DISCONTINUED = {'code': 'D', 'cmmnt': 'part has been discontinued'}
REPLACED = {'code': 'R', 'cmmnt': 'part has been replaced'}


def _calculate_date(years=10):
    """
    calculate a random time from x number of years ago with a bit of randomness in the possible day as well

    :return:
    """
    d = dt.now() - td(days=random.randint(1,years)*random.randint(265,365))
    return dt(d.year, d.month, d.day)


def create_supplier(db):
    """
    create a supplier
    {
      _id: ObjectId,
      name: String:supplier_N,
      addr: { line1: String, line2: String, city: String, state: String, zip: String },
      phones: [ {main_office: String, support: String },
      since: ISODate,
      d_pct: Integer
    }

    find the newest supplier, add 1 to it and create a new one with a random date
    :return:
    """
    supplier_num = 1
    # TODO: test this out - to make sure we are getting the latest supplier
    for doc in db['supplier'].find({}).sort({'name': -1}).limit(1):
        supplier_num = int(doc['name'].split('_')[1]) + 1

    supplier_doc = {
        'name': ''.join(('supplier_', str(supplier_num))),
        'addr': {'line1': '123 main st.', 'line2': 'floor 1024', 'city': 'somewhere', 'state': 'ny', 'zip': '1234'},
        'phone': [{'main_office': '123-123-1234'}, {'support': '123-123-1234'}],
        'since': _calculate_date(),
        'status': ACTIVE,
        'cmmt': 'new contract',
        'd_pct': random.randint(0, 25)
    }

    ret = db['supplier'].insert_one(supplier_doc)
    # analyze return


def create_new_part_for_supplier(db):
    """
    create a part for a supplier:
    - find a random supplier, choose a random part, build the part set since (make sure
      it is newer than supplier since)

    TODO: error handling
    :return:
    """
    part_name = random.choice(S_PARTS)
    n = random.randint(1, db['supplier'].count_documents({'status': ACTIVE})) - 1  # 0 based index for skip
    part_no = 1
    for doc in db['inventory'].find({}).sort({'part_no': -1}).limit(-1):
        part_no = int(doc['part_no'].split('_')[1]) + 1

    s_doc = db['supplier'].find({'status': ACTIVE}).skip(n).limit(1).next()
    db['supplier'].insertOne({
        'name': part_name,
        'supplier': s_doc['name'],
        'since': _calculate_date(random.randint(1, s_doc['since'].year)),
        'inventory': random.randint(0, 400),
        'part_no': ''.join(('part_'), str(part_no))
    })


def find_current_parts_offering(db):
    """
    search for all current parts offered, group by supplier and parts with an inventory count

    :param db:
    :return:
    """
    match = {
        '$match': {
            'since': {'$lt': dt.now()},
            'to': {'$exists': False}
        }
    }

    group = {
        '$group': {
            '_id': {'supplier': '$supplier', 'name': '$name'},
            'total_inventory': {'$sum': '$inventory'}
        }
    }

    for doc in db['inventory'].aggregate(match, group):
        print(doc)


def group_current_parts_by_supplier(db):
    """

    :param db:
    :return:
    """
    pass


def find_current_suppliers(db):
    """

    :param db:
    :return:
    """
    pass


def find_past_suppliers(db):
    """

    :param db:
    :return:
    """
    pass


def find_past_parts(db):
    """

    :param db:
    :return:
    """
    pass


def find_past_parts_by_current_suppliers(db):
    """

    :param db:
    :return:
    """
    pass


def find_past_parts_by_suppliers(db):
    """

    :param db:
    :return:
    """
    pass


def end_contract_with_supplier(db):
    """
    this will be a transaction to end contract, and eol supplies from that contractor

    :param db:
    :return:
    """
    pass


def end_of_life_part_for_active_suppliers(db):
    """

    :param db:
    :return:
    """
    pass
