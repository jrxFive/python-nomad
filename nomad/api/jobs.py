

class Jobs(object):

    def __init__(self,requester):
        self.requester = requester

    def __str__(self):
        pass

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

