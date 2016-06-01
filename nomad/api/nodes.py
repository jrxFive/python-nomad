
class Nodes(object):

    def __init__(self,requester):
        self.requester = requester

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        self.get()

        for n in self.nodes:
            if n["ID"] == item:
                return True
            if n["Name"] == item:
                return True
        else:
            return False

    def __len__(self):
        self.get()
        return len(self.nodes)

    def __getitem__(self, item):
        self.get()

        for n in self.nodes:
            if n["ID"] == item:
                return n
            if n["Name"] == item:
                return n
        else:
            raise KeyError

    def __iter__(self):
        self.get()
        return iter(self.nodes)

    def get(self):
        self.nodes = self.requester.get("/v1/nodes")
        return self.nodes



