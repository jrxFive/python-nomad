
class Client(object):

    ENDPOINT = "client"

    def __init__(self, requester):
        self._requester = requester
        self.ls = ls(requester)
        self.cat = cat(requester)
        self.stat = stat(requester)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(
                Client.ENDPOINT, "fs", *args)

            response = self._requester.get(url, params=kwargs)

            return response.json()
        except ValueError:
            return response.text
        except:
            raise


class ls(Client):

    ENDPOINT = "ls"

    def __init__(self, requester):
        self._requester = requester

    def list_files(self, id, path="/"):
        return self._get(ls.ENDPOINT, id, path=path)


class cat(Client):

    ENDPOINT = "cat"

    def __init__(self, requester):
        self._requester = requester

    def read_file(self, id, path="/"):
        return self._get(cat.ENDPOINT, id, path=path)


class stat(Client):

    ENDPOINT = "stat"

    def __init__(self, requester):
        self._requester = requester

    def stat_file(self, id, path="/"):
        return self._get(stat.ENDPOINT, id, path=path)
