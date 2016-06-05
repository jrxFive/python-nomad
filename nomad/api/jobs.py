import nomad.api.exceptions


class Jobs(object):

    """
    The jobs endpoint is used to query the status of existing
    jobs in Nomad and to register new jobs.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/jobs.html
    """
    ENDPOINT = "jobs"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            jobs = self._get()

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
        jobs = self._get()
        return len(jobs)

    def __getitem__(self, item):
        try:
            jobs = self._get()

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
        jobs = self._get()
        return iter(jobs)

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Jobs.ENDPOINT, *args)
            jobs = self._requester.get(url)

            return jobs.json()
        except:
            raise

    def get_jobs(self):
        """ Lists all the jobs registered with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get()

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Jobs.ENDPOINT, *args)

            if kwargs:
                response = self._requester.post(url, json=kwargs["job"])
            else:
                response = self._requester.post(url)

            return response.json()
        except:
            raise

    def register_job(self, job):
        """ Lists all the jobs registered with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(job=job)
