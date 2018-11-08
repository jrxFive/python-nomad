import nomad
import pytest
import tests.common as common

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

@pytest.fixture
def nomad_setup_with_namespace():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN, namespace=common.NOMAD_NAMESPACE)
    return n
