import pytest
import tests.common as common
import nomad
import json
import requests


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n


# integration tests requires nomad Vagrant VM or Binary running
def test_get_namespaces(nomad_setup):
    assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True
