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
        try:
            url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)
            agent = self._requester.get(url)

            return agent.json()
        except:
            raise

    def get_agent(self):
        return self._get("self")

    def get_members(self):
        return self._get("members")

    def get_servers(self):
        return self._get("servers")

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Agent.ENDPOINT, *args)

            response = self._requester.post(url, params=kwargs["params"])

            return response.json()
        except ValueError:
            return response.status_code

    def join_agent(self, addresses):
        params = "address=" + "&address=".join(addresses)
        return self._post("join", params=params)

    def update_servers(self, addresses):
        params = "address=" + "&address=".join(addresses)
        return self._post("servers", params=params)

    def force_leave(self, node):
        params = "node={node}".format(node=node)
        return self._post("force-leave", params=params)
