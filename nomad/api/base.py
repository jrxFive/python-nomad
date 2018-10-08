import requests
import nomad.api.exceptions

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Requester(object):

    ENDPOINT = ""

    def __init__(self, address=None, uri='http://127.0.0.1', port=4646, namespace=None, token=None, timeout=5, version='v1', verify=False, cert=(), region=None, **kwargs):
        self.uri = uri
        self.port = port
        self.namespace = namespace
        self.token = token
        self.timeout = timeout
        self.version = version
        self.verify = verify
        self.cert = cert
        self.address = address
        self.session = requests.Session()
        self.region = region

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
        url = self.address

        if self.address is None:
           url = "{uri}:{port}".format(uri=self.uri,
                                        port=self.port)
        url = "{url}/{endpoint}".format(url=url,
                                        endpoint=endpoint)
        if self.namespace:
            if self._required_namespace(endpoint):
                url = "{url}?namespace={namespace}".format(
                           url=url,
                           namespace=self.namespace)

        if self.region is not None:
            if self.namespace:
                delimiter = '&'
            else:
                delimiter = '?'
            url = "{url}{delimiter}region={region}".format(
                url=url, delimiter=delimiter,
                region=self.region)
        return url

    def request(self, *args, **kwargs):
        endpoint = self._endpointBuilder(self.ENDPOINT, *args)
        response = self._request(
            endpoint=endpoint,
            method=kwargs.get("method"),
            params=kwargs.get("params", None),
            data=kwargs.get("data", None),
            json=kwargs.get("json", None),
            headers=kwargs.get("headers", None),
            allow_redirects=kwargs.get("allow_redirects", False)
        )

        return response

    def _request(self, method, endpoint, params=None, data=None, json=None, headers=None, allow_redirects=None):
        url = self._urlBuilder(endpoint)

        if self.token:
            try:
                headers["X-Nomad-Token"] = self.token
            except TypeError:
                headers = {"X-Nomad-Token": self.token}

        response = None

        try:
            method = method.lower()
            if method == "get":
                response = self.session.get(
                    url=url,
                    params=params,
                    headers=headers,
                    timeout=self.timeout,
                    verify=self.verify,
                    cert=self.cert,
                    allow_redirects=allow_redirects
                )

            elif method == "post":
                response = self.session.post(
                    url=url,
                    params=params,
                    json=json,
                    headers=headers,
                    data=data,
                    timeout=self.timeout,
                    verify=self.verify,
                    cert=self.cert,
                    allow_redirects=allow_redirects
                )
            elif method == "put":
                response = self.session.put(
                    url=url,
                    params=params,
                    json=json,
                    headers=headers,
                    data=data,
                    verify=self.verify,
                    cert=self.cert,
                    timeout=self.timeout
                )
            elif method == "delete":
                response = self.session.delete(
                    url=url,
                    params=params,
                    headers=headers,
                    verify=self.verify,
                    cert=self.cert,
                    timeout=self.timeout
                )

            if response.ok:
                return response
            elif response.status_code == 400:
                raise nomad.api.exceptions.BadRequestNomadException(response)
            elif response.status_code == 403:
                raise nomad.api.exceptions.URLNotAuthorizedNomadException(response)
            elif response.status_code == 404:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)
            else:
                raise nomad.api.exceptions.BaseNomadException(response)

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException(response)
