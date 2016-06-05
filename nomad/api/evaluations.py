import nomad.api.exceptions

class Evaluations(object):

    ENDPOINT="evaluations"

    def __init__(self,requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            evaluations = self._get()

            for e in evaluations:
                if e["ID"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        evaluations = self._get()
        return len(evaluations)

    def __getitem__(self, item):
        try:
            evaluations = self._get()

            for e in evaluations:
                if e["ID"] == item:
                    return e
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        evaluations = self._get()
        return iter(evaluations)

    def _get(self,*args):
        try:
            url = self._requester._endpointBuilder(Evaluations.ENDPOINT,*args)
            evaluations = self._requester.get(url)

            return evaluations.json()
        except:
            raise

    def get_evaluations(self):
        return self._get()
