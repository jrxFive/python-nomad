import nomad.api.exceptions

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
        variables = self.get_variables()

        for var in variables:
            if var["Path"] == item:
                return True
        else:
            return False

    def __getitem__(self, item):
        variables = self.get_variables()

        for var in variables:
            if var["Path"] == item:
                return var
        else:
            raise KeyError

    def get_variables(self, prefix="", namespace=None):
        """ 
        This endpoint lists variables.
        https://developer.hashicorp.com/nomad/api-docs/variables

        optional_arguments:
            - prefix, (default "") Specifies a string to filter variables on based on an index prefix.
                This is specified as a query string parameter.
            - namespace :(str) optional, Specifies the target namespace.
                Specifying * will return all variables across all the authorized namespaces.
        returns: list of dicts
        raises:
            - nomad.api.exceptions.BaseNomadException
            - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        if namespace:
            params["namespace"] = namespace

        return self.request(params=params, method="get").json()


