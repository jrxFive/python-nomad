import nomad.api.exceptions


class Sentinel(object):

    """
    The endpoint manage sentinel policies (Enterprise Only)

    https://www.nomadproject.io/api/sentinel-policies.html
    """

    ENDPOINT = "sentinel"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Sentinel.ENDPOINT, *args)
        response = self._requester.get(url,
                                       params=kwargs.get("params", None))

        return response.json()

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Sentinel.ENDPOINT, *args)

        if kwargs:
            response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
        else:
            response = self._requester.post(url)

        return response.json()

    def _post_no_json(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Sentinel.ENDPOINT, *args)
            
        if kwargs:
            response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
        else:
            response = self._requester.post(url)

        return response

    def get_policies(self):
        """ Get a list of policies.

            https://www.nomadproject.io/api/sentinel-policies.html

            returns: list

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("policies")

    def create_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            arguments:
                - policy
            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post_no_json("policy", id, json_dict=policy)


    def get_policy(self, id):
        """ Get a spacific policy.

            https://www.nomadproject.io/api/sentinel-policies.html

            returns: dict

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("policy", id)

    def update_policy(self, id, policy):
        """ Create policy.

            https://www.nomadproject.io/api/sentinel-policies.html

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

            https://www.nomadproject.io/api/sentinel-policies.html

            arguments:
                - id

            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete("policy", id)

    def _delete(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Sentinel.ENDPOINT, *args)
        response = self._requester.delete(url,
                                          params=kwargs.get("params", None))

        return response.ok
