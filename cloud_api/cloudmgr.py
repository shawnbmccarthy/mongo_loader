from cloud_api import CoreApi


class CloudManager(CoreApi):
    """
    """
    def __init__(
            self,
            api_url='https://cloud.mongodb.com/api/public/v1.0',
            api_usr='',
            api_token=''
    ):
        """
        :param api_url:
        :param api_usr:
        :param api_token:
        """
        super(CoreApi, self).__init__(api_url, api_usr, api_token)
        self.logger.debug('use the atlas api structure')