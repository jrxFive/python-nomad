from nomad.api.base import Requester


class Sentinel(Requester):

    """
    The endpoint manage sentinel policies (Enterprise Only)

    https://www.nomadproject.io/api/sentinel-policies.html
    """

    ENDPOINT = "sentinel"

    def __init__(self, **kwargs):
        super(Sentinel, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def get_policies(self):
        """ Get a list of policies.

            https://www.nomadproject.io/api/sentinel-policies.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policies", method="get").json()

    def create_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            arguments:
                - policy
            returns: requests.Response

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, json=policy, method="post")

    def get_policy(self, id):
        """ Get a spacific policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, method="get").json()

    def update_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            arguments:
                - name
                - policy
            returns: requests.Response

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, json=policy, method="post")

    def delete_policy(self, id):
        """ Delete specific policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            arguments:
                - id
            returns: Boolean

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, method="delete").ok
