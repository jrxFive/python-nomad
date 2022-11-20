import requests


class BaseNomadException(Exception):
    """General Error occurred when interacting with nomad API"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp

    def __str__(self):
        if isinstance(self.nomad_resp, requests.Response) and hasattr(self.nomad_resp, "text"):
            return 'The {0} was raised with following response: {1}.'.format(self.__class__.__name__, self.nomad_resp.text)
        else:
            return 'The {0} was raised due to the following error: {1}'.format(self.__class__.__name__,  str(self.nomad_resp))


class URLNotFoundNomadException(BaseNomadException):
    """The requeted URL given does not exist"""


class URLNotAuthorizedNomadException(BaseNomadException):
    """The requested URL is not authorized. ACL"""


class BadRequestNomadException(BaseNomadException):
    """Validation failure and if a parameter is modified in the request, it could potentially succeed."""


class VariableConflict(BaseNomadException):
    """In the case of a compare-and-set variable conflict"""


class InvalidParameters(Exception):
    """Invalid parameters given"""


class TimeoutNomadException(requests.exceptions.RequestException):
    """Timeout on request, if using a stream and timeout in conjunction"""
