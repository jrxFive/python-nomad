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
        url = self._requester._endpointBuilder(Node.ENDPOINT, *args)
        node = self._requester.get(url)

        return node.json()

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
        url = self._requester._endpointBuilder(Node.ENDPOINT, *args)

        if kwargs:
            response = self._requester.post(url, params=kwargs.get("enable", None), json=kwargs.get("payload", {}))
        else:
            response = self._requester.post(url)

        return response.json()

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

            arguments:
              - id (str uuid): node id
              - enable (bool): enable node drain or not to enable node drain
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """

        return self._post(id, "drain", enable={"enable": enable})

    def drain_node_with_spec(self, id, drain_spec, mark_eligible=None):
        """ This endpoint toggles the drain mode of the node. When draining is enabled,
            no further allocations will be assigned to this node, and existing allocations
            will be migrated to new nodes.

            If an empty dictionary is given as drain_spec this will disable/toggle the drain.

            https://www.nomadproject.io/docs/http/node.html

            arguments:
              - id (str uuid): node id
              - drain_spec (dict): https://www.nomadproject.io/api/nodes.html#drainspec
              - mark_eligible (bool): https://www.nomadproject.io/api/nodes.html#markeligible
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        payload = {}

        if drain_spec and mark_eligible is not None:
            payload = {
                "NodeID": id,
                "DrainSpec": drain_spec,
                "MarkEligible": mark_eligible
            }
        elif drain_spec and mark_eligible is None:
            payload = {
                "NodeID": id,
                "DrainSpec": drain_spec
            }
        elif not drain_spec and mark_eligible is not None:
            payload = {
                "NodeID": id,
                "DrainSpec": None,
                "MarkEligible": mark_eligible
            }
        elif not drain_spec and mark_eligible is None:
            payload = {
                "NodeID": id,
                "DrainSpec": None,
            }

        return self._post(id, "drain", payload=payload)

    def eligible_node(self, id, eligible=None, ineligible=None):
        """ Toggle the eligibility of the node.

           https://www.nomadproject.io/docs/http/node.html

            arguments:
              - id (str uuid): node id
              - eligible (bool): Set to True to mark node eligible
              - ineligible (bool): Set to True to mark node ineligible
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        payload = {}

        if eligible is not None and ineligible is not None:
            raise nomad.api.exceptions.InvalidParameters
        if eligible is None and ineligible is None:
            raise nomad.api.exceptions.InvalidParameters

        if eligible is not None and eligible:
            payload = {"Eligibility": "eligible", "NodeID": id}
        elif eligible is not None and not eligible:
            payload = {"Eligibility": "ineligible", "NodeID": id}
        elif ineligible is not None:
            payload = {"Eligibility": "ineligible", "NodeID": id}
        elif ineligible is not None and not ineligible:
            payload = {"Eligibility": "eligible", "NodeID": id}

        return self._post(id, "eligibility", payload=payload)

    def purge_node(self, id):
        """ This endpoint purges a node from the system. Nodes can still join the cluster if they are alive.
        arguments:
          - id (str uuid): node id
        returns: dict
        raises:
          - nomad.api.exceptions.BaseNomadException
          - nomad.api.exceptions.URLNotFoundNomadException
        """

        return self._post(id, "purge")

