"""
 pov: proof of value
 - some simple mongo code to build confidence in the mongodb database
 - why python? because ...
"""

_VERSION_MAJOR = 0
_VERSION_MINOR = 1
_VERSION_RELEASE = 'ALPHA'


def get_version():
    """
    Build simple version string for POV module
    :return:
    """
    return str(_VERSION_MAJOR + '.' + _VERSION_MINOR + '_' + _VERSION_RELEASE)


def capture_client_configuration():
    """
    capture core client configurations (cpu, memory, disk, etc.)

    :return:
    """
    return 'hardware'


def capture_mongo_configuration():
    """
    capture core mongodb configurations
    - assuming atlas right now

    :return:
    """
    return 'hardware'
