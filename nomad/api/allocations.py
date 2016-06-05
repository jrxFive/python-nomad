
class Allocations(object):

    """
    The allocations endpoint is used to query the status of allocations.
    By default, the agent's local region is used; another region can be
    specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/allocs.html
    """
    ENDPOINT = "allocations"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __len__(self):
        response = self._get()
        return len(response)

    def __iter__(self):
        response = self._get()
        return iter(response)

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Allocations.ENDPOINT, *args)
            response = self._requester.get(url)

            return response.json()
        except:
            raise

    def get_allocations(self):
        """ Lists all the allocations.

           https://www.nomadproject.io/docs/http/allocs.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get()
