import nomad.api.exceptions

from nomad.api.base import Requester


class Namespace(Requester):

    """
    The job endpoint is used for CRUD on a single namespace.
    By default, the agent's local region is used.

    https://www.nomadproject.io/api/namespaces.html
    """
    ENDPOINT = "namespace"

    def __init__(self, **kwargs):
        super(Namespace, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):

        try:
            j = self.get_namespace(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            j = self.get_namespace(item)

            if j["ID"] == item:
                return j
            if j["Name"] == item:
                return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

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
        return self.request(id, method="get").json()

    def create_namespace(self, namespace):
        """ create namespace

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
              - namespace (dict)
            returns: requests.Response
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(json=namespace, method="post")

    def update_namespace(self, id, namespace):
        """ Update namespace

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
              - namespace (dict)
            returns: requests.Response
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(id, json=namespace, method="post")

    def delete_namespace(self, id):
        """ delete namespace.

           https://www.nomadproject.io/api/namespaces.html

            arguments:
              - id
            returns: requests.Response
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(id, method="delete")
