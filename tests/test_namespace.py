import pytest
import tests.common as common
import nomad
import json
import os
from nomad.api import exceptions


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

# integration tests requires nomad Vagrant VM or Binary running


def test_apply_namespace(nomad_setup):
    namespace_api='{"Name":"api","Description":"api server namespace"}'
    namespace = json.loads(namespace_api)
    nomad_setup.namespace.apply_namespace("api", namespace)
    assert "api" in nomad_setup.namespace

def test_get_namespace(nomad_setup):
    assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]

def test_delete_namespace(nomad_setup):
    nomad_setup.namespace.delete_namespace("api")
    try:
        assert "api" != nomad_setup.namespace.get_namespace("api")["Name"]
    except nomad.api.exceptions.URLNotFoundNomadException:
        pass
