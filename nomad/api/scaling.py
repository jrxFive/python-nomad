import nomad.api.exceptions

from nomad.api.base import Requester


class Scaling(Requester):
    """
    Endpoints are used to list and view scaling policies.

    https://developer.hashicorp.com/nomad/api-docs/scaling-policies
    """
    ENDPOINT = "scaling"

    def __init__(self, **kwargs):
        super(Scaling, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def get_scaling_policies(self, job="", type=""):
        """
        This endpoint returns the scaling policies from all jobs.

        https://developer.hashicorp.com/nomad/api-docs/scaling-policies#list-scaling-policies

        arguments:
            - job
            - type
        returns: list of dicts
        raises:
            - nomad.api.exceptions.BaseNomadException
            - nomad.api.exceptions.URLNotFoundNomadException
        """
        type_of_scaling_policies = [
            "horizontal",
            "vertical_mem",
            "vertical_cpu",
            "",
        ] # we have only horizontal in OSS

        if type not in type_of_scaling_policies:
            raise nomad.api.exceptions.InvalidParameters("type is invalid "
                "(expected values are {} but got {})".format(type_of_scaling_policies, type))

        params = {"job": job, "type": type}

        return self.request("policies", method="get", params=params).json()

    def get_scaling_policy(self, id):
        """
        This endpoint reads a specific scaling policy.

        https://developer.hashicorp.com/nomad/api-docs/scaling-policies#read-scaling-policy

        arguments:
            - id
        returns: list of dicts
        raises:
            - nomad.api.exceptions.BaseNomadException
            - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("policy/{}".format(id), method="get").json()
