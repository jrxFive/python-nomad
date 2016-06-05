import pytest
import tests.common as common
import nomad
import json

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP,port=common.NOMAD_PORT)
    return n

#integration tests requires nomad Vagrant VM or Binary running
def test_get_agent(nomad_setup):
    assert isinstance(nomad_setup.agent.get_agent(),dict) == True

def test_get_members(nomad_setup):
    m = nomad_setup.agent.get_members()
    assert isinstance(m, list) == True

def test_get_servers(nomad_setup):
    s = nomad_setup.agent.get_servers()
    assert isinstance(s, list) == True

def test_join_agent(nomad_setup):
    r = nomad_setup.agent.join_agent("nope")
    assert r["num_joined"] == 0

def test_update_servers(nomad_setup):
    r = nomad_setup.agent.update_servers(['one', 'two:4829'])
    assert r == 200
    assert "one:4647" in nomad_setup.agent.get_servers()
    assert "two:4829" in nomad_setup.agent.get_servers()

def test_force_leave(nomad_setup):
    r = nomad_setup.agent.force_leave("nope")
    assert r == 200

def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.agent),str)

def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.agent),str)

def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.agent.does_not_exist




