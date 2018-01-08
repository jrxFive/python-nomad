import pytest
import tests.common as common
import nomad
from nomad.api import exceptions
import os


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n


# integration tests requires nomad Vagrant VM or Binary running
def test_base_get_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.evaluations["nope"]


def test_base_put_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.system.initiate_garbage_collection()


def test_base_delete_connection_error():
    n = nomad.Nomad(
        host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.job.deregister_job("example")


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 7, 0), reason="Nomad dispatch not supported")
def test_base_get_connnection_not_authorized():
    n = nomad.Nomad(
        host=common.IP, port=common.NOMAD_PORT, token='aed2fc63-c155-40d5-b58a-18deed4b73e5', verify=False)
    with pytest.raises(nomad.api.exceptions.URLNotAuthorizedNomadException):
        j = n.job.get_job("example")
