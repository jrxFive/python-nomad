import json


class Jobs(object):
    ENDPOINT = "jobs"

    def __init__(self, requester):
        self.requester = requester


    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)


    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        self.get()

        for j in self.jobs:
            if j["ID"] == item:
                return True
            if j["Name"] == item:
                return True
        else:
            return False

    def __len__(self):
        self.get()
        return len(self.jobs)

    def __getitem__(self, item):
        self.get()

        for j in self.jobs:
            if j["ID"] == item:
                return j
            if j["Name"] == item:
                return j
        else:
            raise KeyError

    def __iter__(self):
        self.get()
        return iter(self.jobs)


    def get(self):
        jobs = self.requester.get("/{v}/{endpoint}".format(v=self.requester.version,
                                                                endpoint=Jobs.ENDPOINT))
        self.jobs = jobs.json()

        return self.jobs


    def register_job(self, job):
        url = "{v}/{endpoint}".format(v=self.requester.version, endpoint=Jobs.ENDPOINT)

        response = self.requester.post(url,json=job)

        return response.json()








