from nomad.api.base import Requester


class Variable(Requester):

    """
    The /var endpoints are used to read or create variables.
    https://developer.hashicorp.com/nomad/api-docs/variables
    """

    ENDPOINT = "var"

    def __init__(self, **kwargs):
        super(Variable, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError


    def create_variable(self):