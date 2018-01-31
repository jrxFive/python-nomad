import nomad.api.exceptions


class Namespace(object):

    """
    The job endpoint is used for CRUD on a single namespace.
    By default, the agent's local region is used.

    https://www.nomadproject.io/api/namespaces.html
    """
    ENDPOINT = "namespace"

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
            j = self._get(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            j = self._get(item)

            if j["ID"] == item:
                return j
            if j["Name"] == item:
                return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        url = self._requester._endpointBuilder(Namespace.ENDPOINT, *args)
        namespace = self._requester.get(url)

        return namespace.json()

    def _post(self, *args, **kwargs):
        url = self._requester._endpointBuilder(Namespace.ENDPOINT, *args)
        if kwargs:
            response = self._requester.post(url, json=kwargs.get("json_dict", None), params=kwargs.get("params", None))
        else:
            response = self._requester.post(url)

        return response

    def _delete(self, *args):
        url = self._requester._endpointBuilder(Namespace.ENDPOINT, *args)
        namespace = self._requester.delete(url)

        return namespace

    def get_namespace(self, id):
        """ Query a single namespace.

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)


    def create_namespace(self, namespace):
        """ create namespace

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
              - namespace (dict)
            returns: None
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(json_dict=namespace)

    def update_namespace(self, id, namespace):
        """ Update namespace

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
              - namespace (dict)
            returns: None
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, json_dict=namespace)

    def delete_namespace(self, id):
        """ delete namespace.

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete(id)
