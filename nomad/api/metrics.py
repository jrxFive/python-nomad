import nomad.api.exceptions


class Metrics(object):

    """
    The /metrics endpoint returns metrics for the current Nomad process.

    https://www.nomadproject.io/api/metrics.html

    Key metrics delivered via the endpoint could be found in Telemetry section:

    https://www.nomadproject.io/docs/agent/telemetry.html
    """
    ENDPOINT = "metrics"

    def __init__(self, requester):
        self._requester = requester

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def _get(self, *args):
        url = self._requester._endpointBuilder(Metrics.ENDPOINT, *args)
        metrics = self._requester.get(url)

        return metrics.json()

    def get_metrics(self):
        """ Get the metrics

           https://www.nomadproject.io/api/metrics.html

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self._get()
