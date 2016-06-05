import requests
import json
import nomad.api.exceptions


class Node(object):

    """
    The node endpoint is used to query the a specific client node.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/node.html
    """
    ENDPOINT = "node"

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
            n = self._get(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            n = self._get(item)

            if n["ID"] == item:
                return n
            if n["Name"] == item:
                return n
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Node.ENDPOINT, *args)
            node = self._requester.get(url)

            return node.json()
        except:
            raise

    def get_node(self, id):
        """ Query the status of a client node registered with Nomad.

           https://www.nomadproject.io/docs/http/node.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)

    def get_allocations(self, id):
        """ Query the allocations belonging to a single node.

           https://www.nomadproject.io/docs/http/node.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id, "allocations")

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Node.ENDPOINT, *args)

            if kwargs:
                response = self._requester.post(url, params=kwargs["enable"])
            else:
                response = self._requester.post(url)

            return response.json()
        except:
            raise

    def evaluate_node(self, id):
        """ Creates a new evaluation for the given node.
            This can be used to force run the 
            scheduling logic if necessary.

           https://www.nomadproject.io/docs/http/node.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, "evaluate")

    def drain_node(self, id, enable=False):
        """ Toggle the drain mode of the node.
            When enabled, no further allocations will be
            assigned and existing allocations will be migrated.

           https://www.nomadproject.io/docs/http/node.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, "drain", enable={"enable": enable})
