class ApiError(Exception):
    """
    Root error
    """
    def __init__(self, msg='', code=0):
        super(ApiError, self).__init__(msg)
