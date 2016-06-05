

class BaseNomadException(Exception):

    """General Error occurred when interacting with nomad API"""


class URLNotFoundNomadException(Exception):

    """The requeted URL given does not exist"""
