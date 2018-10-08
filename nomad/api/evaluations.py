import nomad.api.exceptions

from nomad.api.base import Requester

class Evaluations(Requester):

    """
    The evaluations endpoint is used to query the status of evaluations.
    By default, the agent's local region is used; another region can
    be specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/evals.html
    """
    ENDPOINT = "evaluations"

    def __init__(self, **kwargs):
        super(Evaluations, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            evaluations = self.get_evaluations()

            for e in evaluations:
                if e["ID"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        evaluations = self.get_evaluations()
        return len(evaluations)

    def __getitem__(self, item):
        try:
            evaluations = self.get_evaluations()

            for e in evaluations:
                if e["ID"] == item:
                    return e
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        evaluations = self.get_evaluations()
        return iter(evaluations)

    def get_evaluations(self):
        """ Lists all the evaluations.

           https://www.nomadproject.io/docs/http/evals.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
