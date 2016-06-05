import requests

class Evaluation(object):
    ENDPOINT = "evaluation"

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
            e = self._get(item)
            return True
        except requests.RequestException:
            return False

    def __getitem__(self, item):

        try:
            e = self._get(item)

            if e["ID"] == item:
                return e
            else:
                raise KeyError
        except requests.RequestException:
            raise KeyError


    def _get(self,*args):
        url = self._requester._endpointBuilder(Evaluation.ENDPOINT,*args)
        evaluation = self._requester.get(url)

        return evaluation.json()

    def get_evaluation(self,id):
        return self._get(id)

    def get_allocations(self,id):
        return self._get(id,"allocations")
