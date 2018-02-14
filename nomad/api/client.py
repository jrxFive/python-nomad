
class Client(object):

    ENDPOINT = "client"

    def __init__(self, requester):
        self._requester = requester
        self.ls = ls(requester)
        self.cat = cat(requester)
        self.stat = stat(requester)
        self.stats = stats(requester)
        self.allocation = allocation(requester)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(
                Client.ENDPOINT, *args)

            response = self._requester.get(url, params=kwargs)

            return response.json()
        except ValueError:
            return response.text
        except:
            raise


class ls(Client):

    """
    The /fs/ls endpoint is used to list files in an allocation directory.
    This API endpoint is hosted by the Nomad client and requests have to be
    made to the Nomad client where the particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-ls.html
    """

    ENDPOINT = "fs/ls"

    def __init__(self, requester):
        self._requester = requester

    def list_files(self, id, path="/"):
        """ List files in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-ls.html

            arguments:
              - id
              - path          
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(ls.ENDPOINT, id, path=path)


class cat(Client):

    """
    The /fs/cat endpoint is used to read the contents of a file in an
    allocation directory. This API endpoint is hosted by the Nomad
    client and requests have to be made to the Nomad client where the
    particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-cat.html
    """

    ENDPOINT = "fs/cat"

    def __init__(self, requester):
        self._requester = requester

    def read_file(self, id, path="/"):
        """ Read contents of a file in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-cat.html

            arguments:
              - id
              - path
            returns: text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(cat.ENDPOINT, id, path=path)


class stat(Client):

    """
    The /fs/stat endpoint is used to show stat information 
    This API endpoint is hosted by the Nomad client and requests have to be
    made to the Nomad client where the particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-stat.html
    """

    ENDPOINT = "fs/stat"

    def __init__(self, requester):
        self._requester = requester

    def stat_file(self, id, path="/"):
        """ Stat a file in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-stat.html

            arguments:
              - id
              - path
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(stat.ENDPOINT, id, path=path)


class stats(Client):

    """
    The /stats endpoint queries the actual resources consumed on a node.
    The API endpoint is hosted by the Nomad client and requests have to
    be made to the nomad client whose resource usage metrics are of interest.

    https://www.nomadproject.io/api/client.html#read-stats
    """

    ENDPOINT = "stats"

    def __init__(self, requester):
        self._requester = requester

    def read_stats(self):
        """ Query the actual resources consumed on a node.

            https://www.nomadproject.io/api/client.html#read-stats

            arguments:
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(stats.ENDPOINT)


class allocation(Client):

    """
    The allocation/:alloc_id/stats endpoint is used to query the actual
    resources consumed by an allocation. The API endpoint is hosted by the 
    Nomad client and requests have to be made to the nomad client whose 
    resource usage metrics are of interest.

    https://www.nomadproject.io/api/client.html#read-allocation
    """

    ENDPOINT = "allocation"

    def __init__(self, requester):
        self._requester = requester

    def read_allocation_stats(self, id):
        """ Query the actual resources consumed by an allocation.

            https://www.nomadproject.io/api/client.html#read-allocation

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(allocation.ENDPOINT, id, "stats")
