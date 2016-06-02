import pytest
import common
import nomad
import json

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP,port=common.NOMAD_PORT)
    return n

#integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example",job)
        assert "example" in nomad_setup.job

def test_get_job(nomad_setup):
    assert isinstance(nomad_setup.job.get_job("example"),dict) == True

def test_dunder_getitem_exist(nomad_setup):
    j = nomad_setup.job["example"]
    assert isinstance(j,dict)

def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.job["redis"]

def test_dunder_contain_exists(nomad_setup):
    assert "example" in nomad_setup.job

def test_dunder_contain_not_exist(nomad_setup):
    assert "redis" not in nomad_setup.job

def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.job),str)

def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.job),str)

def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.job.does_not_exist




