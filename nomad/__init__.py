
import api

class Nomad(object):

    def __init__(self,host='127.0.0.1',port=4646,timeout=5,region=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        self.requester = api.Requester(host,port,timeout)

        self._jobs = api.Jobs(self.requester)
        self._nodes = api.Nodes(self.requester)
        self._allocations = api.Allocations()
        self._evaluations = api.Evaluations()
        self._agent = api.Agent()
        self._client = api.Client()
        self._regions = api.Regions()
        self._status = api.Status()
        self._system = api.System()


    @property
    def jobs(self):
        return self._jobs

    @property
    def nodes(self):
        return self._nodes

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

