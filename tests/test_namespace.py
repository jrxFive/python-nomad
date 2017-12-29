import pytest
import tests.common as common
import nomad
import json
import os
from nomad.api import exceptions
from unittest.mock import patch
from unittest.mock import ANY
from unittest.mock import MagicMock
import requests



@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

# integration tests requires nomad Vagrant VM or Binary running


@patch('nomad.api.namespace.Namespace._post')
def test_apply_namespace(mock_post, nomad_setup):
    mock_post.return_value = requests.codes.ok
    namespace_api='{"Name":"api","Description":"api server namespace"}'
    namespace = json.loads(namespace_api)
    assert 200 == nomad_setup.namespace.apply_namespace("api", namespace)

@patch('nomad.api.namespace.Namespace._get')
def test_get_namespace(mock_get, nomad_setup):
    mock_get.return_value = {"Name":"api","Description":"api server namespace"}
    assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]

@patch('nomad.api.namespace.Namespace._delete')
def test_delete_namespace(mock_delete, nomad_setup):
    mock_delete.return_value = {"Name":"api","Description":"api server namespace"}
    nomad_setup.namespace.delete_namespace("api")
    assert "api" == nomad_setup.namespace.delete_namespace("api")["Name"]
