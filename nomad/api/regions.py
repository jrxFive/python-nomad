
class Regions(object):

    ENDPOINT="regions"

    def __init__(self,requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        regions = self._get()

        for r in regions:
            if r == item:
                return True
        else:
            return False

    def __len__(self):
        regions = self._get()
        return len(regions)

    def __getitem__(self, item):
        regions = self._get()

        for r in regions:
            if r == item:
                return r
        else:
            raise KeyError

    def __iter__(self):
        regions = self._get()
        return iter(regions)

    def _get(self,*args):
        url = self._requester._endpointBuilder(Regions.ENDPOINT,*args)
        nodes = self._requester.get(url)

        return nodes.json()

    def get_regions(self):
        return self._get()