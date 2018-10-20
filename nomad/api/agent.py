import nomad.api.exceptions

from nomad.api.base import Requester


class Agent(Requester):

    """The self endpoint is used to query the state of the target agent."""
    ENDPOINT = "agent"

    def __init__(self, **kwargs):
        super(Agent, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def get_agent(self):
        """ Query the state of the target agent.

            https://www.nomadproject.io/docs/http/agent-self.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("self", method="get").json()

    def get_members(self):
        """Lists the known members of the gossip pool.

           https://www.nomadproject.io/docs/http/agent-members.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("members", method="get").json()

    def get_servers(self):
        """ Lists the known members of the gossip pool.

            https://www.nomadproject.io/docs/http/agent-servers.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("servers", method="get").json()

    def join_agent(self, addresses):
        """Initiate a join between the agent and target peers.

           https://www.nomadproject.io/docs/http/agent-join.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"address": addresses}
        return self.request("join", params=params, method="post").json()

    def update_servers(self, addresses):
        """Updates the list of known servers to the provided list.
           Replaces all previous server addresses with the new list.

           https://www.nomadproject.io/docs/http/agent-servers.html

            returns: 200 status code
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"address": addresses}
        return self.request("servers", params=params, method="post").status_code

    def force_leave(self, node):
        """Force a failed gossip member into the left state.

            https://www.nomadproject.io/docs/http/agent-force-leave.html

            returns: 200 status code
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"node": node}
        return self.request("force-leave", params=params, method="post").status_code
