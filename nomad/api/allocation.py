"""Nomad allocation: https://developer.hashicorp.com/nomad/api-docs/allocations"""
import nomad.api.exceptions

from nomad.api.base import Requester


class Allocation(Requester):
    """
    The allocation endpoint is used to query the a specific allocation.
    By default, the agent's local region is used; another region can be
    specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/alloc.html
    """

    ENDPOINT = "allocation"

    def __init__(self, **kwargs):
        super(Allocation, self).__init__(**kwargs)

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __getattr__(self, item):
        raise AttributeError

    def __contains__(self, item):
        try:
            response = self.get_allocation(item)

            if response["ID"] == item:
                return True
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __getitem__(self, item):
        try:
            response = self.get_allocation(item)

            if response["ID"] == item:
                return response
        except nomad.api.exceptions.URLNotFoundNomadException as exc:
            raise KeyError from exc

    def get_allocation(self, _id):
        """ Query a specific allocation.

           https://www.nomadproject.io/docs/http/alloc.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(_id, method="get").json()

    def stop_allocation(self, _id):
        """ Stop a specific allocation.

           https://www.nomadproject.io/api-docs/allocations/#stop-allocation

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(_id, "stop", method="post").json()
