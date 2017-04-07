import requests
import nomad.api.exceptions


class Job(object):

    """
    The job endpoint is used for CRUD on a single job.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/job.html
    """
    ENDPOINT = "job"

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
            j = self._get(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            j = self._get(item)

            if j["ID"] == item:
                return j
            if j["Name"] == item:
                return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Job.ENDPOINT, *args)
            job = self._requester.get(url)

            return job.json()
        except:
            raise

    def get_job(self, id):
        """ Query a single job for its specification and status.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)

    def get_allocations(self, id):
        """ Query the allocations belonging to a single job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id, "allocations")

    def get_evaluations(self, id):
        """ Query the evaluations belonging to a single job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id, "evaluations")

    def get_summary(self, id):
        """ Query the summary of a job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id, "summary")

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Job.ENDPOINT, *args)

            if kwargs:
                response = self._requester.post(url, json=kwargs["json_dict"], params=kwargs.get("params", None))
            else:
                response = self._requester.post(url)

            return response.json()
        except:
            raise

    def register_job(self, id, job):
        """ Registers a new job or updates an existing job

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, json_dict=job)

    def evaluate_job(self, id):
        """ Creates a new evaluation for the given job.
            This can be used to force run the scheduling logic if necessary.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, "evaluate")

    def plan_job(self, id, job, diff=False):
        """ Invoke a dry-run of the scheduler for the job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
              - job, dict
              - diff, optional boolean
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, "plan", json_dict=job, params={"diff": diff})

    def periodic_job(self, id):
        """ Forces a new instance of the periodic job. A new instance will be
            created even if it violates the job's prohibit_overlap settings.
            As such, this should be only used to immediately
            run a periodic job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._post(id, "periodic", "force")
    
    def dispatch_job(self, id, payload=None, meta=None):
        """ Dispatches a new instance of a parameterized job.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
              - payload
              - meta
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        dispatch_json = {"Meta": meta, "Payload": payload}
        return self._post(id, "dispatch", json_dict=dispatch_json)

    def _delete(self, *args):
        try:
            url = self._requester._endpointBuilder(Job.ENDPOINT, *args)
            job = self._requester.delete(url)

            return job.json()
        except:
            raise

    def deregister_job(self, id):
        """ Deregisters a job, and stops all allocations part of it.

           https://www.nomadproject.io/docs/http/job.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._delete(id)
