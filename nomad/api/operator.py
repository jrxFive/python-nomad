
class Operator(object):

    """
    The Operator endpoint provides cluster-level tools for
    Nomad operators, such as interacting with the Raft subsystem.

    https://www.nomadproject.io/docs/http/operator.html
    """

    ENDPOINT = "operator"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Operator.ENDPOINT, *args)
            response = self._requester.get(url,
                                           params=kwargs.get("params",None))

            return response.json()
        except:
            raise

    def _delete(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Operator.ENDPOINT, *args)
            response = self._requester.delete(url,
                                              params=kwargs.get("params", None))

            return response.ok
        except:
            raise

    def get_configuration(self, stale=False):
        """ Query the status of a client node registered with Nomad.

            https://www.nomadproject.io/docs/http/operator.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """

        params = {"stale": stale}
        return self._get("raft", "configuration", params=params)

    def delete_peer(self, peer_address):
        """ Remove the Nomad server with given address from the Raft configuration.
            The return code signifies success or failure.

            https://www.nomadproject.io/docs/http/operator.html

            arguments:
              - peer_address, The address specifies the server to remove and is given as an IP:port
            returns: Ok status
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """

        params = {"address": peer_address}
        return self._delete("raft", "peer", params=params)
