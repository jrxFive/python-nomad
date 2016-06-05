import requests
import nomad.api.exceptions


class Evaluation(object):

    """
    The evaluation endpoint is used to query a specific evaluations.
    By default, the agent's local region is used; another region can
    be specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/eval.html
    """
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
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            e = self._get(item)

            if e["ID"] == item:
                return e
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Evaluation.ENDPOINT, *args)
            evaluation = self._requester.get(url)

            return evaluation.json()

        except:
            raise

    def get_evaluation(self, id):
        """ Query a specific evaluation.

           https://www.nomadproject.io/docs/http/eval.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)

    def get_allocations(self, id):
        """ Query the allocations created or modified by an evaluation.

           https://www.nomadproject.io/docs/http/eval.html

            arguments:
              - id
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id, "allocations")
