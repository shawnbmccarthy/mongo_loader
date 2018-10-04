import requests
import logging
from requests.auth import HTTPDigestAuth


class BaseApi:
    """

    """
    def __init__(self, api_url, api_usr, api_token):
        """

        :param api_url:
        :param api_usr:
        :param api_token:
        """
        self.logger = logging.getLogger(__name__)
        self.api_url = api_url
        self.api_usr = api_usr
        self.api_token = api_token

    def _get(self, resource):
        """
        TODO: handle query params

        :param resource:
        :return:
        """
        response = requests.get(
            str('{}{}'.format(self.api_url, resource)),
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )

        if response.status_code != 200:
            # TODO: process error handing here
            print('error!')
            print(response.status_code)
            print(response.content)
        return response

    def _patch(self, resource, data):
        pass

    def _post(self, resource, data):
        pass

    def _put(self, resource, data):
        pass

    def _delete(self, resource):
        pass


class CoreApi(BaseApi):
    """
    """
    def __init__(self, api_url, api_usr, api_token):
        super(BaseApi, self).__init__(api_url, api_usr, api_token)

    def get_api_info(self, pretty=False, envelope=False):
        """
        https://docs.atlas.mongodb.com/reference/api/root/

        :return:
        """
        return self._get('/')

    def get_from_link(self, link):
        """
        TODO: can we reduce this code to the _get! or vice versa _get builds a link!
        :param link:
        :return:
        """
        response = requests.get(
            link['href'],
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        if response.status_code != 200:
            # TODO: process error
            print('error!')
            print(response.status_code)
            print(response.content)
        return response
