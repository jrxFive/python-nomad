import nomad.api.exceptions

from nomad.api.base import Requester


class Acl(Requester):
    """
    The endpoint manage security ACL and tokens

    https://www.nomadproject.io/api/acl-tokens.html
    """

    ENDPOINT = "acl"

    def __init__(self, **kwargs):
        super(Acl, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def generate_bootstrap(self):
        """ Activate bootstrap token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("bootstrap", method="post").json()

    def get_tokens(self):
        """ Get a list of tokens.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """

        return self.request("tokens", method="get").json()

    def get_token(self, id):
        """ Retrieve specific token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("token", id, method="get").json()

    def get_self_token(self):
        """ Retrieve self token used for auth.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("token", "self", method="get").json()

    def create_token(self, token):
        """ Create token.

            https://www.nomadproject.io/api/acl-tokens.html

            arguments:
                token
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("token", json=token, method="post").json()

    def delete_token(self, id):
        """ Delete specific token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: Boolean

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("token", id, method="delete").ok

    def update_token(self, id, token):
        """ Update token.

            https://www.nomadproject.io/api/acl-tokens.html

            arguments:
                - AccdesorID
                - token
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("token", id, json=token, method="post").json()

    def get_policies(self):
        """ Get a list of policies.

            https://www.nomadproject.io/api/acl-policies.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policies", method="get").json()

    def create_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - policy
            returns: request.Response

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, json=policy, method="post")

    def get_policy(self, id):
        """ Get a spacific.

            https://www.nomadproject.io/api/acl-policies.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, method="get").json()

    def update_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - name
                - policy
            returns: request.Response

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, json=policy, method="post")

    def delete_policy(self, id):
        """ Delete specific policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - id
            returns: Boolean

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy", id, method="delete").ok
