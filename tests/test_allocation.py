import pytest
import tests.common as common
import nomad
import json
import requests


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT)
    return n

# integration tests requires nomad Vagrant VM or Binary running


def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


def test_get_allocation(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert isinstance(nomad_setup.allocation.get_allocation(id), dict) == True


def test_dunder_getitem_exist(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    a = nomad_setup.allocation[id]
    assert isinstance(a, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):  # restucture try/except/raises
        j = nomad_setup.allocation["redis"]


def test_dunder_contain_exists(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert id in nomad_setup.allocation


def test_dunder_contain_not_exist(nomad_setup):

    assert "redis" not in nomad_setup.allocation


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocation), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocation), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocation.does_not_exist
