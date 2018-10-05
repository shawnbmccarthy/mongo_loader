import pprint
import unittest
from cloud_api.atlas import AtlasApi

from testcases.atlas_api import test_cfg


class OrgTests(unittest.TestCase):
    def setUp(self):
        self.a_api = AtlasApi(api_usr=test_cfg['API']['cloud_user'], api_token=test_cfg['API']['cloud_token'])

    def test_read_all_orgs(self):
        orgs = self.a_api.get_orgs()
        self.assertIn('results', orgs, 'orgs object does not contain array of results')
        self.assertIn('totalCount', orgs, 'orgs object does not contain a count of results')

    def test_page_queries(self):
        orgs = self.a_api.get_orgs(pageNum=1, itemsPerPage=1)
        self.assertIn('results', orgs, 'orgs object does not contain array of results')
        orgs = self.a_api.get_orgs(pageNum=2)
        self.assertIn('results', orgs, 'orgs object does not contain array of results')

    def test_crud(self):
        org = self.a_api.create_org(org={'name': 'mdb_api_unittest_org'})
        self.assertIn('id', org, 'return org object does not contain an id')
        oid = org['id']
        org = self.a_api.get_org(oid=oid)
        self.assertIn('name', org, 'did not read object successfully')
        org = self.a_api.rename_org(oid=oid, org={'name': 'mdb_api_unittest_org_2'})
        self.assertIn('name', org, 'did not update object successfully')
        org = self.a_api.delete_org(oid=oid)
        self.assertEqual(org, {}, 'did not delete object successfully')


if __name__ == '__main__':
    unittest.main()
