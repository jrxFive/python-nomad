import pytest
import tests.common as common
import nomad
import json
import os
from nomad.api import exceptions



@pytest.fixture
def nomad_setup(token=None):
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT,token=common.NOMAD_TOKEN, verify=False)
    return n

# integration tests requires nomad Vagrant VM or Binary running
# IMPORTANT: without token activated

@pytest.mark.run(order=0)
def test_create_bootstrap(nomad_setup):
    bootstrap = nomad_setup.acl.generate_bootstrap()
    assert "SecretID" in bootstrap
    common.NOMAD_TOKEN = bootstrap["SecretID"]
    print (common.NOMAD_TOKEN)

@pytest.mark.run(order=1)
def test_list_tokens(nomad_setup):
    assert "Bootstrap Token" in nomad_setup.acl.get_tokens()[0]["Name"]

@pytest.mark.run(order=2)
def test_create_token(nomad_setup):
    token_example='{"Name": "Readonly token","Type": "client","Policies": ["readonly"],"Global": false}'
    json_token = json.loads(token_example)
    created_token = nomad_setup.acl.create_token(json_token)
    assert "Readonly token" in created_token["Name"]

@pytest.mark.run(order=3)
def test_list_all_tokens(nomad_setup):
    tokens = nomad_setup.acl.get_tokens()
    assert isinstance(tokens, list)

@pytest.mark.run(order=4)
def test_update_token(nomad_setup):
    token_example='{"Name": "CreatedForUpdate","Type": "client","Policies": ["readonly"],"Global": false}'
    json_token = json.loads(token_example)
    created_token = nomad_setup.acl.create_token(json_token)

    token_update ='{"AccessorID":"' + created_token["AccessorID"] + '","Name": "Updated" ,"Type": "client","Policies": ["readonly"]}'
    json_token_update = json.loads(token_update)
    update_token = nomad_setup.acl.update_token(id=created_token["AccessorID"],token=json_token_update)

    assert "Updated" in update_token["Name"]

@pytest.mark.run(order=5)
def test_get_token(nomad_setup):
    token_example='{"Name": "GetToken","Type": "client","Policies": ["readonly"],"Global": false}'
    json_token = json.loads(token_example)
    created_token = nomad_setup.acl.create_token(json_token)
    get_token = nomad_setup.acl.get_token(created_token["AccessorID"])
    assert "GetToken" in created_token["Name"]

@pytest.mark.run(order=6)
def test_get_token(nomad_setup):
    token_example='{"Name": "DeleteToken","Type": "client","Policies": ["readonly"],"Global": false}'
    json_token = json.loads(token_example)
    created_token = nomad_setup.acl.create_token(json_token)
    assert "DeleteToken" in created_token["Name"]
    nomad_setup.acl.delete_token(created_token["AccessorID"])
    assert False == any("DeleteToken" in x for x in nomad_setup.acl.get_tokens())

def test_get_self(nomad_setup):
    get_token = nomad_setup.acl.get_self()
    assert nomad_setup.token in get_token["SecretID"]
