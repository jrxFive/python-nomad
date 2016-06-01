import requests

class Requester(object):
    def __init__(self, uri='127.0.0.1', port=4646, timeout=5, version='v1'):
        self.uri = uri
        self.port = port
        self.timeout = timeout
        self.version = version


    def _urlBuilder(self, endpoint):
        return "http://{uri}:{port}/{endpoint}".format(uri=self.uri,
                                                       port=self.port,
                                                       endpoint=endpoint)

    def get(self, endpoint, params=None):
        url = self._urlBuilder(endpoint)

        try:
            response = requests.get(url,
                                    params=params,
                                    timeout=self.timeout)

            if response.ok:
                return response
            else:
                raise requests.RequestException
        except requests.RequestException:
            raise


    def post(self, endpoint, data=None, json=None, headers=None):
        url = self._urlBuilder(endpoint)

        print url

        try:
            # r = requests.post("http://192.168.33.10:4646/v1/jobs",json=job,params=None,data=None,headers=None)
            response = requests.post(url,json=json,headers=headers,data=data)

            if response.ok:
                return response
            else:
                raise requests.RequestException
        except requests.RequestException:
            raise


    def delete(self):
        raise NotImplementedError




