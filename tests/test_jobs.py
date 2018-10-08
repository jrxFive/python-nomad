import os
import pytest
import json


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.jobs.register_job(job)
        assert "example" in nomad_setup.jobs


def test_get_jobs(nomad_setup):
    assert isinstance(nomad_setup.jobs.get_jobs(), list) == True


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 3), reason="Not supported in version")
def test_parse_job(nomad_setup):
    with open("example.nomad") as fh:
        hcl = fh.read()
        json_dict = nomad_setup.jobs.parse(hcl)
        assert json_dict["Name"] == "example"
        assert json_dict["Type"] == "service"


def test_dunder_getitem_exist(nomad_setup):
    j = nomad_setup.jobs["example"]
    assert isinstance(j, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.jobs["redis"]


def test_dunder_contain_exists(nomad_setup):
    assert "example" in nomad_setup.jobs


def test_dunder_contain_not_exist(nomad_setup):
    assert "redis" not in nomad_setup.jobs


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.jobs), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.jobs), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.jobs.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.jobs, '__iter__')
    for j in nomad_setup.jobs:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.jobs) >= 0
