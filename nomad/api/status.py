import nomad.api.exceptions

from nomad.api.base import Requester


class Status(object):

    """
    By default, the agent's local region is used

    https://www.nomadproject.io/docs/http/status.html
    """

    def __init__(self, **kwargs):
        self.leader = Leader(**kwargs)
        self.peers = Peers(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError


class Leader(Requester):

    ENDPOINT = "status/leader"

    def __contains__(self, item):
        try:
            leader = self.get_leader()

            if leader == item:
                return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        leader = self.get_leader()
        return len(leader)

    def get_leader(self):
        """ Returns the address of the current leader in the region.

            https://www.nomadproject.io/docs/http/status.html

            returns: string
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()


class Peers(Requester):

    ENDPOINT = "status/peers"

    def __contains__(self, item):
        try:
            peers = self.get_peers()

            for p in peers:
                if p == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        peers = self.get_peers()
        return len(peers)

    def __getitem__(self, item):
        try:
            peers = self.get_peers()

            for p in peers:
                if p == item:
                    return p
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        peers = self.get_peers()
        return iter(peers)

    def get_peers(self):
        """ Returns the set of raft peers in the region.

            https://www.nomadproject.io/docs/http/status.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
