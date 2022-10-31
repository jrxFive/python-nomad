from nomad.api.base import Requester


class Variables(Requester):

    """
    The /vars endpoints are used to query for and interact with variables.
    https://developer.hashicorp.com/nomad/api-docs/variables
    """

    ENDPOINT = "vars"

    def __init__(self, **kwargs):
        super(Variables, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            variables = self.get_variables()

            for var in variables:
                if var["ID"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):
        try:
            deployments = self.get_deployments()

            for d in deployments:
                if d["ID"] == item:
                    return d
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError