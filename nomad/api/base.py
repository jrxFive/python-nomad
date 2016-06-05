import requests
import nomad.api.exceptions


class Requester(object):

    def __init__(self, uri='127.0.0.1', port=4646, timeout=5, version='v1'):
        self.uri = uri
        self.port = port
        self.timeout = timeout
        self.version = version
        self.session = requests.Session()

    def _endpointBuilder(self, *args):
        if args:
            u = "/".join(args)
            return "{v}/".format(v=self.version) + u

    def _urlBuilder(self, endpoint):
        return "http://{uri}:{port}/{endpoint}".format(uri=self.uri,
                                                       port=self.port,
                                                       endpoint=endpoint)

    def get(self, endpoint, params=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.get(url,
                                        params=params,
                                        timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException

    def post(self, endpoint, params=None, data=None, json=None, headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.post(
                url, params=params, json=json, headers=headers, data=data, timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException

    def put(self, endpoint, params=None, data=None, headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.put(
                url, params=params, headers=headers, data=data, timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException

    def delete(self, endpoint, headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.delete(
                url, headers=headers, timeout=self.timeout)

            if response.ok:
                return response
            if response.status_code == 400 or response.status_code == 404 or response.status_code == 500:
                raise nomad.api.exceptions.URLNotFoundNomadException

        except requests.RequestException:
            raise nomad.api.exceptions.BaseNomadException
