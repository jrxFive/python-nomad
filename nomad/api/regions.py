import nomad.api.exceptions


class Regions(object):

    """
    https://www.nomadproject.io/docs/http/regions.html
    """
    ENDPOINT = "regions"

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
            regions = self._get()

            for r in regions:
                if r == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        regions = self._get()
        return len(regions)

    def __getitem__(self, item):
        try:
            regions = self._get()

            for r in regions:
                if r == item:
                    return r
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        regions = self._get()
        return iter(regions)

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Regions.ENDPOINT, *args)
            nodes = self._requester.get(url)

            return nodes.json()
        except:
            raise

    def get_regions(self):
        """ Returns the known region names.

            https://www.nomadproject.io/docs/http/regions.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get()
