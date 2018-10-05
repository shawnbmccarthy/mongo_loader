from cloud_api import CoreApi

# TODO: implement ops manager apis
# TODO: should support most of the same from cloud manager
class OpsManager(CoreApi):
    """
    """
    def __init__(
            self,
            api_url,
            api_usr,
            api_token
    ):
        """
        :param api_url:
        :param api_usr:
        :param api_token:
        """
        super(CloudManager, self).__init__(api_url, api_usr, api_token)
        self.logger.debug('use the atlas api structure')