import nomad.api.exceptions

from nomad.api.base import Requester


class Namespaces(Requester):

    """
    The namespaces from enterprise solution

    https://www.nomadproject.io/docs/enterprise/namespaces/index.html
    """
    ENDPOINT = "namespaces"

    def __init__(self, **kwargs):
        super(Namespaces, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            namespaces = self.get_namespaces()

            for n in namespaces:
                if n["Name"] == item:
                    return True
            
            return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        namespaces = self.get_namespaces()
        return len(namespaces)

    def __getitem__(self, item):
        try:
            namespaces = self.get_namespaces()

            for n in namespaces:
                if n["Name"] == item:
                    return n
            
            raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        namespaces = self.get_namespaces()
        return iter(namespaces)

    def get_namespaces(self, prefix=None):
        """ Lists all the namespaces registered with Nomad.

           https://www.nomadproject.io/docs/enterprise/namespaces/index.html
            arguments:
              - prefix :(str) optional, specifies a string to filter namespaces on based on an prefix.
                        This is specified as a querystring parameter.
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        return self.request(method="get", params=params).json()
