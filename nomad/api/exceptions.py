class BaseNomadException(Exception):
    """General Error occurred when interacting with nomad API"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp


class URLNotFoundNomadException(Exception):
    """The requeted URL given does not exist"""
    def __init__(self, nomad_resp):
        self.nomad_resp = nomad_resp
