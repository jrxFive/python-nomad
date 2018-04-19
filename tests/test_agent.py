import pytest
import tests.common as common
import nomad
import os
from nomad.api import exceptions as nomad_exceptions
import json


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

# integration tests requires nomad Vagrant VM or Binary running


def test_get_agent(nomad_setup):
    assert isinstance(nomad_setup.agent.get_agent(), dict) == True


def test_get_members(nomad_setup):
    m = nomad_setup.agent.get_members()

    if isinstance(m, list):
        assert True
    elif isinstance(m, dict):
        assert True
    else:
        assert False


def test_get_servers(nomad_setup):
    s = nomad_setup.agent.get_servers()
    assert isinstance(s, list) == True


def test_join_agent(nomad_setup):
    r = nomad_setup.agent.join_agent("nope")
    assert r["num_joined"] == 0


def test_update_servers(nomad_setup):
    known_servers = nomad_setup.agent.get_servers()
    r = nomad_setup.agent.update_servers(known_servers)
    assert r == 200
    assert known_servers[0] in nomad_setup.agent.get_servers()

    # 0.8 enforces list of known servers to the provided list releases below do allow this functionality
    try:
        nomad_setup.agent.update_servers(known_servers + ["10.1.10.200:4829"])
        assert "10.1.10.200:4829" in nomad_setup.agent.get_servers()
    except nomad_exceptions.BaseNomadException:
        pass


def test_force_leave(nomad_setup):
    r = nomad_setup.agent.force_leave("nope")
    assert r == 200


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.agent), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.agent), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.agent.does_not_exist
