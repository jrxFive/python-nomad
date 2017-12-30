import nomad.api.exceptions


class Status(object):

    """
    By default, the agent's local region is used

    https://www.nomadproject.io/docs/http/status.html
    """
    ENDPOINT = "status"

    def __init__(self, requester):
        self._requester = requester
        self.leader = Leader(requester)
        self.peers = Peers(requester)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Status.ENDPOINT, *args)
            nodes = self._requester.get(url)

            return nodes.json()
        except:
            raise


class Leader(Status):

    ENDPOINT = "leader"

    def __init__(self, requester):
        self._requester = requester

    def __contains__(self, item):
        try:
            leader = self._get(Leader.ENDPOINT)

            if leader == item:
                return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        leader = self._get(Leader.ENDPOINT)
        return len(leader)

    def get_leader(self):
        """ Returns the address of the current leader in the region.

            https://www.nomadproject.io/docs/http/status.html

            returns: string
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(Leader.ENDPOINT)


class Peers(Status):

    ENDPOINT = "peers"

    def __init__(self, requester):
        self._requester = requester

    def __contains__(self, item):
        try:
            peers = self._get(Peers.ENDPOINT)

            for p in peers:
                if p == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        peers = self._get(Peers.ENDPOINT)
        return len(peers)

    def __getitem__(self, item):
        try:
            peers = self._get(Peers.ENDPOINT)

            for p in peers:
                if p == item:
                    return p
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        peers = self._get(Peers.ENDPOINT)
        return iter(peers)

    def get_peers(self):
        """ Returns the set of raft peers in the region.

            https://www.nomadproject.io/docs/http/status.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(Peers.ENDPOINT)
