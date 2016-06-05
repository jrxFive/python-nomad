import requests
import nomad.api.exceptions


class Allocation(object):

    """
    The allocation endpoint is used to query the a specific allocation.
    By default, the agent's local region is used; another region can be
    specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/alloc.html
    """

    ENDPOINT = "allocation"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            response = self._get(item)

            if response["ID"] == item:
                return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):
        try:
            response = self._get(item)

            if response["ID"] == item:
                return response
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Allocation.ENDPOINT, *args)
            response = self._requester.get(url)

            return response.json()
        except:
            raise

    def get_allocation(self, id):
        """ Query a specific allocation.

           https://www.nomadproject.io/docs/http/alloc.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)
