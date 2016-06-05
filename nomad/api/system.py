
class System(object):

    """
    The system endpoint is used to for system maintenance
    and should not be necessary for most users.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/system.html
    """

    ENDPOINT = "system"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _put(self, *args):
        try:
            url = self._requester._endpointBuilder(System.ENDPOINT, *args)
            response = self._requester.put(url)

            return response.ok
        except:
            raise

    def initiate_garbage_collection(self):
        """ Initiate garbage collection of jobs, evals, allocations and nodes.

            https://www.nomadproject.io/docs/http/system.html

            returns: None
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._put("gc")
