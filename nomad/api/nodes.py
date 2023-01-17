"""Nomad Node: https://developer.hashicorp.com/nomad/api-docs/nodes"""
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
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __getattr__(self, item):
        msg = f"{item} does not exist"
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            nodes = self.get_nodes()

            for node in nodes:
                if node["ID"] == item:
                    return True
                if node["Name"] == item:
                    return True
            return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        nodes = self.get_nodes()
        return len(nodes)

    def __getitem__(self, item):
        try:
            nodes = self.get_nodes()

            for node in nodes:
                if node["ID"] == item:
                    return node
                if node["Name"] == item:
                    return node
            raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException as exc:
            raise KeyError from exc

    def __iter__(self):
        nodes = self.get_nodes()
        return iter(nodes)

    def get_nodes(self, prefix=None):
        """Lists all the client nodes registered with Nomad.

        https://www.nomadproject.io/docs/http/nodes.html
        arguments:
          - prefix :(str) optional, specifies a string to filter nodes on based on an prefix.
                    This is specified as a querystring parameter.
        returns: list
        raises:
          - nomad.api.exceptions.BaseNomadException
          - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        return self.request(method="get", params=params).json()
