import nomad.api.exceptions

from nomad.api.base import Requester


class Evaluation(Requester):

    """
    The evaluation endpoint is used to query a specific evaluations.
    By default, the agent's local region is used; another region can
    be specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/eval.html
    """
    ENDPOINT = "evaluation"

    def __init__(self, **kwargs):
        super(Evaluation, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):

        try:
            e = self.get_evaluation(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            e = self.get_evaluation(item)

            if e["ID"] == item:
                return e
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def get_evaluation(self, id, index=None):
        """ Query a specific evaluation.

           https://www.nomadproject.io/docs/http/eval.html

            arguments:
              - id
              - index  :(dict) optional, provides a dictionary for keeping track of x-nomad-index
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(id, method="get").json()

    def get_allocations(self, id, index=None):
        """ Query the allocations created or modified by an evaluation.

           https://www.nomadproject.io/docs/http/eval.html

            arguments:
              - id
              - index  :(dict) optional, provides a dictionary for keeping track of x-nomad-index
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(id, "allocations", method="get", index=index).json()
