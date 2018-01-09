import requests
import nomad.api.exceptions

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Requester(object):

    def __init__(self, uri='http://127.0.0.1', port=4646, namespace=None, token=None, timeout=5, version='v1', verify=False, cert=()):
        self.uri = uri
        self.port = port
        self.namespace = namespace
        self.token = token
        self.timeout = timeout
        self.version = version
        self.verify = verify
        self.cert = cert
        self.session = requests.Session()

    def _endpointBuilder(self, *args):
        if args:
            u = "/".join(args)
            return "{v}/".format(v=self.version) + u

    def _required_namespace(self, endpoint):
        required_namespace = [
                                "job",
                                "jobs",
                                "allocation",
                                "allocations",
                                "deployment",
                                "deployments",
                                "acl"
                             ]
        # split 0 -> Api Version
        # split 1 -> Working Endpoint
        ENDPOINT_NAME = 1
        endpoint_split = endpoint.split("/")
        try:
            required = endpoint_split[ENDPOINT_NAME] in required_namespace
        except:
            required = False
        return required

    def _urlBuilder(self, endpoint):
        url = "{uri}:{port}/{endpoint}".format(uri=self.uri,
                                               port=self.port,
                                               endpoint=endpoint)
        if self.namespace:
            if self._required_namespace(endpoint):
                url = "{url}?namespace={namespace}".format(
                           url=url,
                           namespace=self.namespace)
        return url


    def get(self, endpoint, params=None, headers=None):
        url = self._urlBuilder(endpoint)
        if self.token:
            try:
                headers["X-Nomad-Token"] = self.token
            except TypeError:
                headers = { "X-Nomad-Token": self.token }
        response = None

        try:
            response = self.session.get(url,
                                        headers=headers,
                                        params=params,
                                        verify=self.verify,
                                        cert=self.cert,
                                        timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)
            if response.status_code == 403:
                raise nomad.api.exceptions.URLNotAuthorizedNomadException(response)

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException(response)

    def post(self, endpoint, params=None, data=None, json=None, headers=None):
        url = self._urlBuilder(endpoint)
        if self.token:
            try:
                headers["X-Nomad-Token"] = self.token
            except TypeError:
                headers = { "X-Nomad-Token": self.token }
        response = None

        try:
            response = self.session.post(url,
                                         params=params,
                                         json=json,
                                         headers=headers,
                                         data=data,
                                         verify=self.verify,
                                         cert=self.cert,
                                         timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException(response)

    def put(self, endpoint, params=None, data=None, headers=None):
        url = self._urlBuilder(endpoint)
        if self.token:
            try:
                headers["X-Nomad-Token"] = self.token
            except TypeError:
                headers = { "X-Nomad-Token": self.token }
        response = None

        try:
            response = self.session.put(url,
                                        params=params,
                                        headers=headers,
                                        data=data,
                                        verify=self.verify,
                                        cert=self.cert,
                                        timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException(response)

    def delete(self, endpoint, params=None, headers=None):
        url = self._urlBuilder(endpoint)
        if self.token:
            try:
                headers["X-Nomad-Token"] = self.token
            except TypeError:
                headers = { "X-Nomad-Token": self.token }
        response = None

        try:
            response = self.session.delete(url,
                                           params=params,
                                           headers=headers,
                                           verify=self.verify,
                                           cert=self.cert,
                                           timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException(response)
