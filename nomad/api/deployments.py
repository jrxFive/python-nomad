import nomad.api.exceptions

from nomad.api.base import Requester


class Deployments(Requester):

    """
    The /deployment endpoints are used to query for and interact with deployments.

    https://www.nomadproject.io/docs/http/deployments.html
    """
    ENDPOINT = "deployments"

    def __init__(self, **kwargs):
        super(Deployments, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __len__(self):
        response = self.get_deployments()
        return len(response)

    def __iter__(self):
        response = self.get_deployments()
        return iter(response)

    def __contains__(self, item):
        try:
            deployments = self.get_deployments()

            for d in deployments:
                if d["ID"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):
        try:
            deployments = self.get_deployments()

            for d in deployments:
                if d["ID"] == item:
                    return d
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def get_deployments(self, prefix=""):
        """ This endpoint lists all deployments.

           https://www.nomadproject.io/docs/http/deployments.html

            optional_arguments:
              - prefix, (default "") Specifies a string to filter deployments on based on an index prefix.
                        This is specified as a querystring parameter.

            returns: list of dicts
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        return self.request(params=params, method="get").json()
