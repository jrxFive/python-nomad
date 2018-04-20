import json
from mock import patch, MagicMock
import requests



# integration tests was mocked. If you have an enterprise nomad please uncomenet ##### ENTERPRISE TEST #####
@patch('nomad.api.namespace.Namespace._post')
def test_create_namespace(mock_post, nomad_setup):
    mock_post.return_value = requests.codes.ok
    namespace_api='{"Name":"api","Description":"api server namespace"}'
    namespace = json.loads(namespace_api)
    assert 200 == nomad_setup.namespace.create_namespace(namespace)

@patch('nomad.api.namespace.Namespace._post')
def test_update_namespace(mock_post, nomad_setup):
    mock_post.return_value = requests.codes.ok
    namespace_api='{"Name":"api","Description":"updated namespace"}'
    namespace = json.loads(namespace_api)
    assert 200 == nomad_setup.namespace.update_namespace("api", namespace)


@patch('nomad.api.namespace.Namespace._get')
def test_get_namespace(mock_get, nomad_setup):
    mock_get.return_value = {"Name":"api","Description":"api server namespace"}
    assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]

@patch('nomad.api.namespace.Namespace._delete')
def test_delete_namespace(mock_delete, nomad_setup):
    mock_delete.return_value = {"Name":"api","Description":"api server namespace"}
    nomad_setup.namespace.delete_namespace("api")
    assert "api" == nomad_setup.namespace.delete_namespace("api")["Name"]


######### ENTERPRISE TEST ###########
# def test_apply_namespace(nomad_setup):
#     namespace_api='{"Name":"api","Description":"api server namespace"}'
#     namespace = json.loads(namespace_api)
#     nomad_setup.namespace.apply_namespace("api", namespace)
#     assert "api" in nomad_setup.namespace
#
# def test_get_namespace(nomad_setup):
#     assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]
#
# def test_delete_namespace(nomad_setup):
#     nomad_setup.namespace.delete_namespace("api")
#     try:
#         assert "api" != nomad_setup.namespace.get_namespace("api")["Name"]
#     except nomad.api.exceptions.URLNotFoundNomadException:
#         pass
