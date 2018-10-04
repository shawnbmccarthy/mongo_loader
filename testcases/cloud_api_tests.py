"""

TODO: VERY IMPORTANT!!!
TODO: - for org tests be aware that employee accounts have access to everything!!
TODO: - SA accounts have read access!!
TODO: - use an outside email which will have limited access!!

"""
import unittest
import configparser

from cloud_api.atlas import AtlasApi


class AtlasTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('../dev.conf')
        self.atlas_api = AtlasApi(api_usr=config['API']['cloud_user'], api_token=config['API']['cloud_token'])

    def test_root(self):
        root_json = self.atlas_api.get_api_info().json()
        self.assertEqual(root_json['appName'], 'MongoDB Atlas')


def run_tests():
    unittest.main()


if __name__ == '__main__':
    unittest.main()
