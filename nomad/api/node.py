import requests
import json

class Node(object):
    ENDPOINT = "node"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)


    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):

        try:
            n = self._get(item)
            return True
        except requests.RequestException:
            return False
        except BaseException:
            return False

    def __getitem__(self, item):

        try:
            n = self._get(item)

            if n["ID"] == item:
                return n
            if n["Name"] == item:
                return n
            else:
                raise KeyError
        except requests.RequestException:
            raise KeyError
        except BaseException:
            return KeyError


    def _get(self,*args):
        url = self._requester._endpointBuilder(Node.ENDPOINT,*args)
        node = self._requester.get(url)

        return node.json()

    def get_node(self,id):
        return self._get(id)

    def get_allocations(self,id):
        return self._get(id,"allocations")

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Node.ENDPOINT,*args)

        if kwargs:
            response = self._requester.post(url,params=kwargs["enable"])
        else:
            response = self._requester.post(url)

        return response.json()

    def evaluate_node(self,id):
        return self._post(id,"evaluate")

    def drain_node(self,id,enable=False):
        return self._post(id,"drain",enable={"enable":enable})


















