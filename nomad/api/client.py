from nomad.api.base import Requester


class Client(object):

    def __init__(self, **kwargs):
        self.ls = ls(**kwargs)
        self.cat = cat(**kwargs)
        self.stat = stat(**kwargs)
        self.stats = stats(**kwargs)
        self.allocation = allocation(**kwargs)
        self.read_at = read_at(**kwargs)
        self.stream_file = stream_file(**kwargs)
        self.stream_logs = stream_logs(**kwargs)
        self.gc_allocation = gc_allocation(**kwargs)
        self.gc_all_allocations = gc_all_allocations(**kwargs)

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

    def list_files(self, id=None, path="/"):
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
        if id:
            return self.request(id, params={"path": path}, method="get").json()
        else:
            return self.request(params={"path": path}, method="get").json()


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

    def read_file(self, id=None, path="/"):
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
        if id:
            return self.request(id, params={"path": path}, method="get").text
        else:
            return self.request(params={"path": path}, method="get").text


class read_at(Requester):

    """
    This endpoint reads the contents of a file in an allocation directory at a particular offset and limit.

    https://www.nomadproject.io/api/client.html#read-file-at-offset
    """

    ENDPOINT = "client/fs/readat"

    def __init__(self, **kwargs):
        super(read_at, self).__init__(**kwargs)

    def read_file_offset(self, id, offset, limit, path="/"):
        """ Read contents of a file in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-cat.html

            arguments:
              - id: (str) allocation_id required
              - offset: (int) required
              - limit: (int) required
              - path: (str) optional
            returns: (str) text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.BadRequestNomadException
        """
        params = {
            "path": path,
            "offset": offset,
            "limit": limit
        }
        return self.request(id, params=params, method="get").text


class stream_file(Requester):

    """
    This endpoint streams the contents of a file in an allocation directory.

    https://www.nomadproject.io/api/client.html#stream-file
    """

    ENDPOINT = "client/fs/stream"

    def __init__(self, **kwargs):
        super(stream_file, self).__init__(**kwargs)

    def stream(self, id, offset, origin, path="/"):
        """ This endpoint streams the contents of a file in an allocation directory.

            https://www.nomadproject.io/api/client.html#stream-file

            arguments:
              - id: (str) allocation_id required
              - offset: (int) required
              - origin: (str) either start|end
              - path: (str) optional
            returns: (str) text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.BadRequestNomadException
        """
        params = {
            "path": path,
            "offset": offset,
            "origin": origin
        }
        return self.request(id, params=params, method="get").text


class stream_logs(Requester):

    """
    This endpoint streams a task's stderr/stdout logs.

    https://www.nomadproject.io/api/client.html#stream-logs
    """

    ENDPOINT = "client/fs/logs"

    def __init__(self, **kwargs):
        super(stream_logs, self).__init__(**kwargs)

    def stream(self, id, task, type, follow=False, offset=0, origin="start", plain=False):
        """ This endpoint streams a task's stderr/stdout logs.

            https://www.nomadproject.io/api/client.html#stream-logs

            arguments:
              - id: (str) allocation_id required
              - task: (str) name of the task inside the allocation to stream logs from
              - type: (str) Specifies the stream to stream. Either "stderr|stdout"
              - follow: (bool) default false
              - offset: (int) default 0
              - origin: (str) either start|end, default "start"
              - plain: (bool) Return just the plain text without framing. default False
            returns: (str) text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.BadRequestNomadException
        """
        params = {
            "task": task,
            "type": type,
            "follow": follow,
            "offset": offset,
            "origin": origin,
            "plain": plain
        }
        return self.request(id, params=params, method="get").text


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

    def stat_file(self, id=None, path="/"):
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
        if id:
            return self.request(id, params={"path": path}, method="get").json()
        else:
            return self.request(params={"path": path}, method="get").json()


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

    def read_stats(self, node_id=None):
        """ Query the actual resources consumed on a node.

            https://www.nomadproject.io/api/client.html#read-stats

            arguments:
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(params={"node_id": node_id}, method="get").json()


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
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(id, "stats", method="get").json()


class gc_allocation(Requester):

    """
    This endpoint forces a garbage collection of a particular, stopped allocation on a node.

    https://www.nomadproject.io/api/client.html#gc-allocation
    """

    ENDPOINT = "client/allocation"

    def __init__(self, **kwargs):
        super(gc_allocation, self).__init__(**kwargs)

    def garbage_collect(self, id):
        """ This endpoint forces a garbage collection of a particular, stopped allocation on a node.

            https://www.nomadproject.io/api/client.html#gc-allocation

            arguments:
              - id: (str) full allocation_id
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        self.request(id, "gc", method="get")


class gc_all_allocations(Requester):

    """
    This endpoint forces a garbage collection of all stopped allocations on a node.

    https://www.nomadproject.io/api/client.html#gc-all-allocation
    """

    ENDPOINT = "client/gc"

    def __init__(self, **kwargs):
        super(gc_all_allocations, self).__init__(**kwargs)

    def garbage_collect(self, node_id=None):
        """ This endpoint forces a garbage collection of all stopped allocations on a node.

            https://www.nomadproject.io/api/client.html#gc-all-allocation

            arguments:
              - node_id: (str) full allocation_id
            raises:
              - nomad.api.exceptions.BaseNomadException
        """
        self.request(params={"node_id": node_id}, method="get")
