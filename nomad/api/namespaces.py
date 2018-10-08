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
            else:
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
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        namespaces = self.get_namespaces()
        return iter(namespaces)

    def get_namespaces(self):
        """ Lists all the namespaces registered with Nomad.

           https://www.nomadproject.io/docs/enterprise/namespaces/index.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
