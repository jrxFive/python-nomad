__author__ = 'jxfive'


import requests

class Requester(object):

    def __init__(self,uri='127.0.0.1',port=4646,timeout=5):
        self.uri = uri
        self.port = port
        self.timeout = timeout
        self.session = requests.Session()

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass




