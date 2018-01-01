import pytest
import tests.common as common
import nomad
import json
from nomad.api import exceptions
from mock import patch, MagicMock
import requests



@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

# integration tests was mocked.

@patch('nomad.api.sentinel.Sentinel._get')
def test_list_policies(mock_get, nomad_setup):
    mock_get.return_value = [
                              {
                                "Name": "foo",
                                "Description": "test policy",
                                "Scope": "submit-job",
                                "EnforcementLevel": "advisory",
                                "Hash": "CIs8aNX5OfFvo4D7ihWcQSexEJpHp+Za+dHSncVx5+8=",
                                "CreateIndex": 8,
                                "ModifyIndex": 8
                              }
                            ]
    policies = nomad_setup.sentinel.get_policies()
    assert isinstance(policies, list)
    assert "foo" in nomad_setup.sentinel.get_policies()[0]["Name"]

@patch('nomad.api.sentinel.Sentinel._post_no_json')
def test_create_policy(mock_post_no_json, nomad_setup):
    mock_post_no_json.return_value = requests.codes.ok
    policy_example = '{"Name": "my-policy", "Description": "This is a great policy", "Scope": "submit-job", "EnforcementLevel": "advisory", "Policy": "main = rule { true }"}'
    json_policy = json.loads(policy_example)
    assert 200 == nomad_setup.sentinel.create_policy(id="my-policy", policy=json_policy)

@patch('nomad.api.sentinel.Sentinel._post_no_json')
def test_update_policy(mock_post_no_json, nomad_setup):
    mock_post_no_json.return_value = requests.codes.ok
    policy_example = '{"Name": "my-policy", "Description": "Update", "Scope": "submit-job", "EnforcementLevel": "advisory", "Policy": "main = rule { true }"}'
    json_policy = json.loads(policy_example)
    assert 200 == nomad_setup.sentinel.update_policy(id="my-policy", policy=json_policy)

@patch('nomad.api.sentinel.Sentinel._get')
def test_get_policy(mock_get, nomad_setup):
    mock_get.return_value = {
                              "Name": "foo",
                              "Description": "test policy",
                              "Scope": "submit-job",
                              "EnforcementLevel": "advisory",
                              "Policy": "main = rule { true }\n",
                              "Hash": "CIs8aNX5OfFvo4D7ihWcQSexEJpHp+Za+dHSncVx5+8=",
                              "CreateIndex": 8,
                              "ModifyIndex": 8
                            }
    policy = nomad_setup.sentinel.get_policy("foo")
    assert "advisory" in policy["EnforcementLevel"]

@patch('nomad.api.sentinel.Sentinel._delete')
def test_delete_policy(mock_delete, nomad_setup):
    mock_delete.return_value = requests.codes.ok
    nomad_setup.sentinel.delete_policy(id="my-policy")
    assert 200 == nomad_setup.sentinel.delete_policy(id="my-policy")
