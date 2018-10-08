import json
import pytest


def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


# integration tests requires nomad Vagrant VM or Binary running
def test_get_allocations(nomad_setup):
    assert isinstance(nomad_setup.allocations.get_allocations(), list) == True


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocations), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocations), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocations.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.allocations, '__iter__')
    for j in nomad_setup.allocations:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.allocations) >= 0
