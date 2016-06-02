
class Nodes(object):

    ENDPOINT="nodes"

    def __init__(self,requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        nodes = self._get()

        for n in nodes:
            if n["ID"] == item:
                return True
            if n["Name"] == item:
                return True
        else:
            return False

    def __len__(self):
        nodes = self._get()
        return len(nodes)

    def __getitem__(self, item):
        nodes = self._get()

        for n in nodes:
            if n["ID"] == item:
                return n
            if n["Name"] == item:
                return n
        else:
            raise KeyError

    def __iter__(self):
        nodes = self._get()
        return iter(nodes)

    def _get(self,*args):
        url = self._requester._endpointBuilder(Nodes.ENDPOINT,*args)
        nodes = self._requester.get(url)

        return nodes.json()

    def get_nodes(self):
        return self._get()





