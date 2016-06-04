
class System(object):

    ENDPOINT="system"

    def __init__(self,requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _put(self,*args):
        url = self._requester._endpointBuilder(System.ENDPOINT,*args)
        response = self._requester.put(url)

        return response.ok

    def initiate_garbage_collection(self):
        return self._put("gc")