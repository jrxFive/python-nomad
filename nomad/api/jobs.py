import nomad.api.exceptions

from nomad.api.base import Requester


class Jobs(Requester):

    """
    The jobs endpoint is used to query the status of existing
    jobs in Nomad and to register new jobs.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/jobs.html
    """
    ENDPOINT = "jobs"

    def __init__(self, **kwargs):
        super(Jobs, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return True
                if j["Name"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        jobs = self.get_jobs()
        return len(jobs)

    def __getitem__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return j
                if j["Name"] == item:
                    return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        jobs = self.get_jobs()
        return iter(jobs)

    def get_jobs(self):
        """ Lists all the jobs registered with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()

    def register_job(self, job):
        """ Register a job with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(json=job, method="post").json()

    def parse(self, hcl, canonicalize=False):
        """ Parse a HCL Job file. Returns a dict with the JSON formatted job.
            This API endpoint is only supported from Nomad version 0.8.3.

            https://www.nomadproject.io/api/jobs.html#parse-job

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("parse", json={"JobHCL": hcl, "Canonicalize": canonicalize}, method="post", allow_redirects=True).json()
