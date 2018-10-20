import nomad.api.exceptions

from nomad.api.base import Requester


class Regions(Requester):

    """
    https://www.nomadproject.io/docs/http/regions.html
    """
    ENDPOINT = "regions"

    def __init__(self, **kwargs):
        super(Regions, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            regions = self.get_regions()

            for r in regions:
                if r == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        regions = self.get_regions()
        return len(regions)

    def __getitem__(self, item):
        try:
            regions = self.get_regions()

            for r in regions:
                if r == item:
                    return r
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        regions = self.get_regions()
        return iter(regions)

    def get_regions(self):
        """ Returns the known region names.

            https://www.nomadproject.io/docs/http/regions.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
