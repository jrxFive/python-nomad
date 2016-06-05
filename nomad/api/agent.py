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
        url = self._requester._endpointBuilder(Agent.ENDPOINT, 'self', *args)
        agent = self._requester.get(url)

        return agent.json()

    def get_agent(self):
        return self._get()

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Agent.ENDPOINT, 'join', *args)
        params = "address={address}".format(address=kwargs["address"])

        response = self._requester.post(url, params=params)

        return response.json()

    def join_agent(self, address):
        return self._post(address=address)
