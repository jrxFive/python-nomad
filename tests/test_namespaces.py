import pytest
import tests.common as common
import nomad
import json
from nomad.api import exceptions
from mock import patch, MagicMock



@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n


# integration tests was mocked. If you have an enterprise nomad please uncomenet ##### ENTERPRISE TEST #####

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

@patch('nomad.api.namespaces.Namespaces._get')
def test_namespaces_iter_(mock_get, nomad_setup):
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
    assert "api-prod" in nomad_setup.namespaces

@patch('nomad.api.namespaces.Namespaces._get')
def test_namespaces_len_(mock_get, nomad_setup):
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
    assert 2 == nomad_setup.namespaces.__len__()




###### ENTERPRISE TEST ###########

# def test_get_namespaces(nomad_setup):
#     assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True
