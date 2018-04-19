class BaseNomadException(Exception):
    """General Error occurred when interacting with nomad API"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp


class URLNotFoundNomadException(Exception):
    """The requeted URL given does not exist"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp
        

class URLNotAuthorizedNomadException(Exception):
    """The requested URL is not authorized. ACL"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp


class InvalidParameters(Exception):
    """Invalid parameters given"""
