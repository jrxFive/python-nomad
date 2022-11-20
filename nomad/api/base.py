import requests
import nomad.api.exceptions

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Requester(object):

    ENDPOINT = ""

    def __init__(self, address=None, uri='http://127.0.0.1', port=4646, namespace=None, token=None, timeout=5, version='v1', verify=False, cert=(), region=None, session=None, **kwargs):
        self.uri = uri
        self.port = port
        self.namespace = namespace
        self.token = token
        self.timeout = timeout
        self.version = version
        self.verify = verify
        self.cert = cert
        self.address = address
        self.session = session or requests.Session()
        self.region = region

    def _endpoint_builder(self, *args):
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
                                "acl",
                                "client",
                                "node"
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

    def _url_builder(self, endpoint):
        url = self.address

        if self.address is None:
            url = "{uri}:{port}".format(uri=self.uri, port=self.port)

        url = "{url}/{endpoint}".format(url=url, endpoint=endpoint)

        return url

    def _query_string_builder(self, endpoint, params=None):
        qs = {}

        if not isinstance(params, dict):
            params = {}

        if ("namespace" not in params) and (self.namespace and self._required_namespace(endpoint)):
            qs["namespace"] = self.namespace

        if "region" not in params and self.region:
            qs["region"] = self.region

        return qs

    def request(self, *args, **kwargs):
        endpoint = self._endpoint_builder(self.ENDPOINT, *args)
        response = self._request(
            endpoint=endpoint,
            method=kwargs.get("method"),
            params=kwargs.get("params", None),
            data=kwargs.get("data", None),
            json=kwargs.get("json", None),
            headers=kwargs.get("headers", None),
            allow_redirects=kwargs.get("allow_redirects", False),
            timeout=kwargs.get("timeout", self.timeout),
            stream=kwargs.get("stream", False)
        )

        return response

    def _request(self, method, endpoint, params=None, data=None, json=None, headers=None, allow_redirects=None, timeout=None, stream=False):
        url = self._url_builder(endpoint)
        qs = self._query_string_builder(endpoint=endpoint, params=params)

        if params:
            params.update(qs)
        else:
            params = qs

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
                    allow_redirects=allow_redirects,
                    cert=self.cert,
                    headers=headers,
                    params=params,
                    stream=stream,
                    timeout=timeout,
                    url=url,
                    verify=self.verify,
                )

            elif method == "post":
                response = self.session.post(
                    allow_redirects=allow_redirects,
                    cert=self.cert,
                    data=data,
                    headers=headers,
                    json=json,
                    params=params,
                    timeout=timeout,
                    url=url,
                    verify=self.verify,
                )
            elif method == "put":
                response = self.session.put(
                    cert=self.cert,
                    data=data,
                    headers=headers,
                    json=json,
                    params=params,
                    timeout=timeout,
                    url=url,
                    verify=self.verify,
                )
            elif method == "delete":
                response = self.session.delete(
                    cert=self.cert,
                    headers=headers,
                    params=params,
                    timeout=timeout,
                    url=url,
                    verify=self.verify,
                )

            if response.ok:
                return response
            elif response.status_code == 400:
                raise nomad.api.exceptions.BadRequestNomadException(response)
            elif response.status_code == 403:
                raise nomad.api.exceptions.URLNotAuthorizedNomadException(response)
            elif response.status_code == 404:
                raise nomad.api.exceptions.URLNotFoundNomadException(response)
            elif response.status_code == 409:
                raise nomad.api.exceptions.VariableConflict(response)
            else:
                raise nomad.api.exceptions.BaseNomadException(response)

        except requests.exceptions.ConnectionError as error:
            if all([stream, timeout]):
                raise nomad.api.exceptions.TimeoutNomadException(error)

            raise nomad.api.exceptions.BaseNomadException(error)

        except requests.RequestException as error:
            raise nomad.api.exceptions.BaseNomadException(error)
