
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
        try:
            url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
            response = self._requester.get(url,
                                           params=kwargs.get("params",None))

            return response.json()
        except:
            raise

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
            print (url)
            if kwargs:
                response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
            else:
                response = self._requester.post(url)

            return response.json()
        except:
            raise

    def _delete(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Acl.ENDPOINT, *args)
            response = self._requester.delete(url,
                                              params=kwargs.get("params", None))

            return response.ok
        except:
            raise

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

    def get_self(self):
        """ Retrieve self token used for auth.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("token","self")

    def delete_token(self, id):
        """ Delete specific token.

            https://www.nomadproject.io/api/acl-tokens.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete("token", id)

    def create_token(self, token):
        """ Create token.

            https://www.nomadproject.io/api/acl-tokens.html

            arguments:
                token: dict
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post("token", json_dict=token)

    def update_token(self, id, token):
        """ Update token.

            https://www.nomadproject.io/api/acl-tokens.html

            arguments:
                - AccdesorID
                - token: dict
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post("token", id, json_dict=token)
