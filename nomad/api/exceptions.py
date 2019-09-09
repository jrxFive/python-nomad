class BaseNomadException(Exception):
    """General Error occurred when interacting with nomad API"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp

    def __str__(self):
        return 'The {0} was raised with following response: {1}.'.format(self.__class__.__name__, self.nomad_resp.text)


class URLNotFoundNomadException(BaseNomadException):
    """The requeted URL given does not exist"""
    pass


class URLNotAuthorizedNomadException(BaseNomadException):
    """The requested URL is not authorized. ACL"""
    pass


class BadRequestNomadException(BaseNomadException):
    """Validation failure and if a parameter is modified in the request, it could potentially succeed."""
    pass


class InvalidParameters(Exception):
    """Invalid parameters given"""
