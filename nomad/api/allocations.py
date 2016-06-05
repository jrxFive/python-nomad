
class Allocations(object):

    ENDPOINT="allocations"

    def __init__(self,requester):
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

    def _get(self,*args):
        try:
            url = self._requester._endpointBuilder(Allocations.ENDPOINT,*args)
            response = self._requester.get(url)

            return response.json()
        except:
            raise

    def get_allocations(self):
        return self._get()





