from nomad.api.base import Requester


class Client(object):

    def __init__(self, **kwargs):
        self.ls = ls(**kwargs)
        self.cat = cat(**kwargs)
        self.stat = stat(**kwargs)
        self.stats = stats(**kwargs)
        self.allocation = allocation(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError


class ls(Requester):

    """
    The /fs/ls endpoint is used to list files in an allocation directory.
    This API endpoint is hosted by the Nomad client and requests have to be
    made to the Nomad client where the particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-ls.html
    """

    ENDPOINT = "client/fs/ls"

    def __init__(self, **kwargs):
        super(ls, self).__init__(**kwargs)

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
        return self.request(ls.ENDPOINT, id, params=path, method="get").json()


class cat(Requester):

    """
    The /fs/cat endpoint is used to read the contents of a file in an
    allocation directory. This API endpoint is hosted by the Nomad
    client and requests have to be made to the Nomad client where the
    particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-cat.html
    """

    ENDPOINT = "client/fs/cat"

    def __init__(self, **kwargs):
        super(cat, self).__init__(**kwargs)

    def read_file(self, id, path="/"):
        """ Read contents of a file in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-cat.html

            arguments:
              - id
              - path
            returns: (str) text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(cat.ENDPOINT, id, params=path, method="get").text


class stat(Requester):

    """
    The /fs/stat endpoint is used to show stat information 
    This API endpoint is hosted by the Nomad client and requests have to be
    made to the Nomad client where the particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-stat.html
    """

    ENDPOINT = "client/fs/stat"

    def __init__(self, **kwargs):
        super(stat, self).__init__(**kwargs)

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
        return self.request(stat.ENDPOINT, id, params=path, method="get").json()


class stats(Requester):

    """
    The /stats endpoint queries the actual resources consumed on a node.
    The API endpoint is hosted by the Nomad client and requests have to
    be made to the nomad client whose resource usage metrics are of interest.

    https://www.nomadproject.io/api/client.html#read-stats
    """

    ENDPOINT = "client/stats"

    def __init__(self, **kwargs):
        super(stats, self).__init__(**kwargs)

    def read_stats(self):
        """ Query the actual resources consumed on a node.

            https://www.nomadproject.io/api/client.html#read-stats

            arguments:
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(stats.ENDPOINT, method="get").json()


class allocation(Requester):

    """
    The allocation/:alloc_id/stats endpoint is used to query the actual
    resources consumed by an allocation. The API endpoint is hosted by the 
    Nomad client and requests have to be made to the nomad client whose 
    resource usage metrics are of interest.

    https://www.nomadproject.io/api/client.html#read-allocation
    """

    ENDPOINT = "client/allocation"

    def __init__(self, **kwargs):
        super(allocation, self).__init__(**kwargs)

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
        return self.request(allocation.ENDPOINT, id, "stats", method="get").json()
