class Agent(object):

    """The self endpoint is used to query the state of the target agent."""
    ENDPOINT = "agent"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)
            agent = self._requester.get(url)

            return agent.json()
        except:
            raise

    def get_agent(self):
        """ Query the state of the target agent.

            https://www.nomadproject.io/docs/http/agent-self.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("self")

    def get_members(self):
        """Lists the known members of the gossip pool.

           https://www.nomadproject.io/docs/http/agent-members.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("members")

    def get_servers(self):
        """ Lists the known members of the gossip pool.

            https://www.nomadproject.io/docs/http/agent-servers.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("servers")

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)

            response = self._requester.post(url, params=kwargs["params"])

            return response.json()
        except ValueError:
            return response.status_code

    def join_agent(self, addresses):
        """Initiate a join between the agent and target peers.

           https://www.nomadproject.io/docs/http/agent-join.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = "address=" + "&address=".join(addresses)
        return self._post("join", params=params)

    def update_servers(self, addresses):
        """Updates the list of known servers to the provided list.
           Replaces all previous server addresses with the new list.

           https://www.nomadproject.io/docs/http/agent-servers.html

            returns: 200 status code
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = "address=" + "&address=".join(addresses)
        return self._post("servers", params=params)

    def force_leave(self, node):
        """Force a failed gossip member into the left state.

            https://www.nomadproject.io/docs/http/agent-force-leave.html

            returns: 200 status code
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = "node={node}".format(node=node)
        return self._post("force-leave", params=params)
