
import nomad.api as api
import os

class Nomad(object):

    def __init__(self, 
        host='127.0.0.1', 
        secure=False, 
        port=4646,
        address=os.getenv('NOMAD_ADDR', None),
        namespace=os.getenv('NOMAD_NAMESPACE', None),
        token=os.getenv('NOMAD_TOKEN', None), 
        timeout=5, 
        region=os.getenv('NOMAD_REGION', None), 
        version='v1', 
        verify=False, 
        cert=()):
        """ Nomad api client

          https://github.com/jrxFive/python-nomad/

           optional arguments:
            - host (defaults 127.0.0.1), string ip or name of the nomad api server/agent that will be used.
            - port (defaults 4646), integer port that will be used to connect.
            - secure (defaults False), define if the protocol is secured or not (https or http)
            - version (defaults v1), vesion of the api of nomad.
            - verify (defaults False), verify the certificate when tls/ssl is enabled
                                at nomad.
            - cert (defaults empty), cert, or key and cert file to validate the certificate
                                configured at nomad.
            - region (defaults None), version of the region to use. It will be used then
                                regions of the current agent of the connection.
            - namespace (defaults to None), Specifies the enterpise namespace that will
                                be use to deploy or to ask info to nomad.
            - token (defaults to None), Specifies to append ACL token to the headers to
                                make authentication on secured based nomad environemnts.
           returns: Nomad api client object

           raises:
             - nomad.api.exceptions.BaseNomadException
             - nomad.api.exceptions.URLNotFoundNomadException
             - nomad.api.exceptions.URLNotAuthorizedNomadException
        """
        self.host = host
        self.secure = secure
        self.port = port
        self.address = address
        self.region = region
        self.timeout = timeout
        self.version = version
        self.token = token
        self.verify = verify
        self.cert = cert
        self.__namespace = namespace

        self.requester_settings = {
            "address": self.address,
            "uri": self.get_uri(),
            "port": self.port,
            "namespace": self.__namespace,
            "token": self.token,
            "timeout": self.timeout,
            "version": self.version,
            "verify": self.verify,
            "cert": self.cert,
            "region": self.region
        }

        self._jobs = api.Jobs(**self.requester_settings)
        self._job = api.Job(**self.requester_settings)
        self._nodes = api.Nodes(**self.requester_settings)
        self._node = api.Node(**self.requester_settings)
        self._allocations = api.Allocations(**self.requester_settings)
        self._allocation = api.Allocation(**self.requester_settings)
        self._evaluations = api.Evaluations(**self.requester_settings)
        self._evaluation = api.Evaluation(**self.requester_settings)
        self._agent = api.Agent(**self.requester_settings)
        self._client = api.Client(**self.requester_settings)
        self._deployments = api.Deployments(**self.requester_settings)
        self._deployment = api.Deployment(**self.requester_settings)
        self._regions = api.Regions(**self.requester_settings)
        self._status = api.Status(**self.requester_settings)
        self._system = api.System(**self.requester_settings)
        self._operator = api.Operator(**self.requester_settings)
        self._validate = api.Validate(**self.requester_settings)
        self._namespaces = api.Namespaces(**self.requester_settings)
        self._namespace = api.Namespace(**self.requester_settings)
        self._acl = api.Acl(**self.requester_settings)
        self._sentinel = api.Sentinel(**self.requester_settings)
        self._metrics = api.Metrics(**self.requester_settings)

    def get_uri(self):
        if self.secure:
            protocol = "https"
        else:
            protocol = "http"
        return "{protocol}://{host}".format(protocol=protocol, host=self.host)

    def get_namespace(self):
        return self.__namespace

    def get_token(self):
        return self.token

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
    def allocation(self):
        return self._allocation

    @property
    def evaluations(self):
        return self._evaluations

    @property
    def evaluation(self):
        return self._evaluation

    @property
    def agent(self):
        return self._agent

    @property
    def client(self):
        return self._client

    @property
    def deployments(self):
        return self._deployments

    @property
    def deployment(self):
        return self._deployment

    @property
    def regions(self):
        return self._regions

    @property
    def status(self):
        return self._status

    @property
    def system(self):
        return self._system

    @property
    def operator(self):
        return self._operator

    @property
    def validate(self):
        return self._validate

    @property
    def namespaces(self):
        return self._namespaces

    @property
    def namespace(self):
        return self._namespace

    @property
    def acl(self):
        return self._acl

    @property
    def sentinel(self):
        return self._sentinel

    @property
    def metrics(self):
        return self._metrics
