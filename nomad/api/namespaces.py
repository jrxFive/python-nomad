import nomad.api.exceptions


class Namespaces(object):

    """
    The namespaces from enterprise solution

    https://www.nomadproject.io/docs/enterprise/namespaces/index.html
    """
    ENDPOINT = "namespaces"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            namespaces = self._get()

            for j in namespaces:
                if j["Name"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        namespaces = self._get()
        return len(namespaces)

    def __getitem__(self, item):
        try:
            namespaces = self._get()

            for j in namespaces:
                if j["Name"] == item:
                    return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        namespaces = self._get()
        return iter(namespaces)

    def _get(self, *args):
        url = self._requester._endpointBuilder(Namespaces.ENDPOINT, *args)
        namespaces = self._requester.get(url)

        return namespaces.json()

    def get_namespaces(self):
        """ Lists all the namespaces registered with Nomad.

           https://www.nomadproject.io/docs/enterprise/namespaces/index.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get()
