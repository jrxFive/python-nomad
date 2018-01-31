import nomad.api.exceptions


class Acl(object):
    """
    The endpoint manage security ACL and tokens

    https://www.nomadproject.io/api/acl-tokens.html
    """

    ENDPOINT = "acl"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
        response = self._requester.get(url,
                                       params=kwargs.get("params", None))

        return response.json()

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
        if kwargs:
            response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
        else:
            response = self._requester.post(url)

        return response.json()

    def _post_no_json(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
        if kwargs:
            response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
        else:
            response = self._requester.post(url)

        return response

    def _delete(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
        response = self._requester.delete(url,
                                          params=kwargs.get("params", None))

        return response.ok

    def generate_bootstrap(self):
        """ Activate bootstrap token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """

        return self._post("bootstrap")

    def get_tokens(self):
        """ Get a list of tokens.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("tokens")

    def get_token(self, id):
        """ Retrieve specific token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("token", id)

    def get_self_token(self):
        """ Retrieve self token used for auth.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("token", "self")

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
        return self._post("token", json_dict=token)

    def delete_token(self, id):
        """ Delete specific token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete("token", id)

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
        return self._post("token", id, json_dict=token)

    def get_policies(self):
        """ Get a list of policies.

            https://www.nomadproject.io/api/acl-policies.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("policies")

    def create_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - policy
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post_no_json("policy", id, json_dict=policy)

    def get_policy(self, id):
        """ Get a spacific.

            https://www.nomadproject.io/api/acl-policies.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("policy", id)

    def update_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - name
                - policy
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post_no_json("policy", id, json_dict=policy)

    def delete_policy(self, id):
        """ Delete specific policy.

            https://www.nomadproject.io/api/acl-policies.html

            arguments:
                - id

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete("policy", id)
