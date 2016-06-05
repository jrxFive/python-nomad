class Agent(object):
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
        url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)
        agent = self._requester.get(url)

        return agent.json()

    def get_agent(self):
        return self._get("self")

    def get_members(self):
        return self._get("members")

    def get_servers(self):
        return self._get("servers")

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)

        if kwargs:
            response = self._requester.post(url, params=kwargs["params"])
        else:
            response = self._requester.post(url)

        try:
            return response.json()
        except ValueError:
            return response.status_code

    def join_agent(self, address):
        params = "address={address}".format(address=address)
        return self._post("join", params=params)

    def force_leave_agent(self, node):
        params = "node={node}".format(node=node)
        return self._post("force-leave", params=params)
