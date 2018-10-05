import unittest
from cloud_api.atlas import AtlasApi

from testcases.atlas_api import test_cfg


class RootTests(unittest.TestCase):
    def setUp(self):
        self.a_api = AtlasApi(api_usr=test_cfg['API']['cloud_user'], api_token=test_cfg['API']['cloud_token'])

    def test_atlas_root(self):
        api_info = self.a_api.get_api_info()
        self.assertIn('appName', api_info, 'response does not contain appName')

    def test_atlas_root_envelope(self):
        api_info = self.a_api.get_api_info(envelope=True)
        self.assertIn('content', api_info, 'envelope response does not contain content')


if __name__ == '__main__':
    unittest.main()
