import requests

class Requester(object):
    def __init__(self, uri='127.0.0.1', port=4646, timeout=5, version='v1'):
        self.uri = uri
        self.port = port
        self.timeout = timeout
        self.version = version
        self.session = requests.Session()


    def _endpointBuilder(self,*args):
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
            else:
                raise requests.RequestException
        except requests.RequestException:
            raise


    def post(self, endpoint, params=None, data=None, json=None, headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.post(url,params=params,json=json,headers=headers,data=data)

            if response.ok:
                return response

        except requests.RequestException:
            raise


    def put(self, endpoint, params=None, data=None, headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.put(url,params=params,headers=headers,data=data)

            if response.ok:
                return response

        except requests.RequestException:
            raise


    def delete(self,endpoint,headers=None):
        url = self._urlBuilder(endpoint)

        try:
            response = self.session.delete(url,headers=headers)

            if response.ok:
                return response

        except requests.RequestException:
            raise




