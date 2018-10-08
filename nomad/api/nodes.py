import nomad.api.exceptions

from nomad.api.base import Requester


class Nodes(Requester):

    """
    The nodes endpoint is used to query the status of client nodes.
    By default, the agent's local region is used

    https://www.nomadproject.io/docs/http/nodes.html
    """
    ENDPOINT = "nodes"

    def __init__(self, **kwargs):
        super(Nodes, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            nodes = self.get_nodes()

            for n in nodes:
                if n["ID"] == item:
                    return True
                if n["Name"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        nodes = self.get_nodes()
        return len(nodes)

    def __getitem__(self, item):
        try:
            nodes = self.get_nodes()

            for n in nodes:
                if n["ID"] == item:
                    return n
                if n["Name"] == item:
                    return n
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        nodes = self.get_nodes()
        return iter(nodes)

    def get_nodes(self):
        """ Lists all the client nodes registered with Nomad.

           https://www.nomadproject.io/docs/http/nodes.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
