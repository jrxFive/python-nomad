
import nomad.api as api

class Nomad(object):

    def __init__(self,host='127.0.0.1',port=4646,timeout=5,region=None,version='v1'):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.version = version

        self.requester = api.Requester(host,port,timeout,version)

        self._jobs = api.Jobs(self.requester)
        self._job = api.Job(self.requester)
        self._nodes = api.Nodes(self.requester)
        self._node = api.Node(self.requester)
        self._allocations = api.Allocations()
        self._evaluations = api.Evaluations(self.requester)
        self._agent = api.Agent()
        self._client = api.Client()
        self._regions = api.Regions(self.requester)
        self._status = api.Status(self.requester)
        self._system = api.System(self.requester)


    @property
    def jobs(self):
        return self._jobs

    @property
    def job(self):
        return self._job

    @property
    def nodes(self):
        return self._nodes

    @property
    def node(self):
        return self._node

    @property
    def allocations(self):
        return self._allocations

    @property
    def evaluations(self):
        return self._evaluations

    @property
    def agent(self):
        return self._agent

    @property
    def client(self):
        return self._client

    @property
    def regions(self):
        return self._regions

    @property
    def status(self):
        return self._status

    @property
    def system(self):
        return self._system

