"""Nomad allocation: https://developer.hashicorp.com/nomad/api-docs/allocations"""
from nomad.api.base import Requester


class Allocations(Requester):
    """
    The allocations endpoint is used to query the status of allocations.
    By default, the agent's local region is used; another region can be
    specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/allocs.html
    """
    ENDPOINT = "allocations"

    def __init__(self, **kwargs):
        super(Allocations, self).__init__(**kwargs)

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __getattr__(self, item):
        raise AttributeError

    def __len__(self):
        response = self.get_allocations()
        return len(response)

    def __iter__(self):
        response = self.get_allocations()
        return iter(response)

    def get_allocations(self, prefix=None, namespace=None):
        """ Lists all the allocations.

           https://www.nomadproject.io/docs/http/allocs.html
            arguments:
              - prefix :(str) optional, specifies a string to filter allocations on based on an prefix.
                        This is specified as a querystring parameter.
              - namespace :(str) optional, specifies the target namespace. Specifying * would return all jobs.
                        This is specified as a querystring parameter.
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        if namespace:
            params["namespace"] = namespace

        return self.request(method="get", params=params).json()
