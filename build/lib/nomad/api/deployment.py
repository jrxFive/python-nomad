import nomad.api.exceptions


class Deployment(object):

    """
    The /deployment endpoints are used to query for and interact with deployments.

    https://www.nomadproject.io/docs/http/deployments.html
    """
    ENDPOINT = "deployment"

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
            d = self._get(item)
            return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):

        try:
            d = self._get(item)

            if d["ID"] == item:
                return d
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def _get(self, *args):
        try:
            url = self._requester._endpointBuilder(Deployment.ENDPOINT, *args)
            response = self._requester.get(url)

            return response.json()

        except:
            raise

    def get_deployment(self, id):
        """ This endpoint reads information about a specific deployment by ID.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get(id)

    def get_deployment_allocations(self, id):
        """ This endpoint lists the allocations created or modified for the given deployment.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
            returns: list of dicts
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get("allocations", id)

    def _post(self, *args, **kwargs):
        try:
            url = self._requester._endpointBuilder(Deployment.ENDPOINT, *args)
            response = self._requester.post(url, json=kwargs.get("json_dict", None))

            return response.json()

        except:
            raise

    def fail_deployment(self, id):
        """ This endpoint is used to mark a deployment as failed. This should be done to force the scheduler to stop
            creating allocations as part of the deployment or to cause a rollback to a previous job version.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        fail_json = {"DeploymentID": id}
        return self._post("fail", id, json_dict=fail_json)

    def pause_deployment(self, id, pause):
        """ This endpoint is used to pause or unpause a deployment.
            This is done to pause a rolling upgrade or resume it.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
              - pause, Specifies whether to pause or resume the deployment.
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        pause_json = {"Pause": pause,
                      "DeploymentID": id}
        return self._post("pause", id, json_dict=pause_json)

    def promote_deployment_all(self, id, all=True):
        """ This endpoint is used to promote task groups that have canaries for a deployment. This should be done when
            the placed canaries are healthy and the rolling upgrade of the remaining allocations should begin.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
              - all, Specifies whether all task groups should be promoted.
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        promote_all_json = {"All": all,
                            "DeploymentID": id}
        return self._post("promote", id, json_dict=promote_all_json)

    def promote_deployment_groups(self, id, groups=list()):
        """ This endpoint is used to promote task groups that have canaries for a deployment. This should be done when
            the placed canaries are healthy and the rolling upgrade of the remaining allocations should begin.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
              - all, Specifies whether all task groups should be promoted.
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        promote_groups_json = {"Groups": groups,
                               "DeploymentID": id}
        return self._post("promote", id, json_dict=promote_groups_json)

    def deployment_allocation_health(self, id, healthy_allocations=list(), unhealthy_allocations=list()):
        """ This endpoint is used to set the health of an allocation that is in the deployment manually. In some use
            cases, automatic detection of allocation health may not be desired. As such those task groups can be marked
            with an upgrade policy that uses health_check = "manual". Those allocations must have their health marked
            manually using this endpoint. Marking an allocation as healthy will allow the rolling upgrade to proceed.
            Marking it as failed will cause the deployment to fail.

           https://www.nomadproject.io/docs/http/deployments.html

            arguments:
              - id
              - healthy_allocations, Specifies the set of allocation that should be marked as healthy.
              - unhealthy_allocations,  Specifies the set of allocation that should be marked as unhealthy.
            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        allocations = {"HealthyAllocationIDs": healthy_allocations,
                       "UnHealthyAllocationIDs": unhealthy_allocations,
                       "DeploymentID": id}
        return self._post("allocation-health", id, json_dict=allocations)
