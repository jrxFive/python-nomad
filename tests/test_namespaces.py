import pytest
import tests.common as common
import nomad
import json
import requests
from unittest.mock import patch
from unittest.mock import ANY
from unittest.mock import MagicMock


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n


# integration tests requires nomad Vagrant VM or Binary running

@patch('nomad.api.namespaces.Namespaces._get')
def test_get_namespaces(mock_get, nomad_setup):
    mock_get.return_value = [
                                {
                                    "CreateIndex": 31,
                                    "Description": "Production API Servers",
                                    "ModifyIndex": 31,
                                    "Name": "api-prod"
                                },
                                {
                                    "CreateIndex": 5,
                                    "Description": "Default shared namespace",
                                    "ModifyIndex": 5,
                                    "Name": "default"
                                }
                            ]
    assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True
