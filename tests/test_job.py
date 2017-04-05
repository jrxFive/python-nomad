import pytest
import tests.common as common
import nomad
import json
import os
from nomad.api import exceptions


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


def test_get_job(nomad_setup):
    assert isinstance(nomad_setup.job.get_job("example"), dict) == True


def test_get_allocations(nomad_setup):
    j = nomad_setup.job["example"]
    a = nomad_setup.job.get_allocations("example")
    assert j["ID"] == a[0]["JobID"]


def test_get_evaluations(nomad_setup):
    j = nomad_setup.job["example"]
    e = nomad_setup.job.get_evaluations("example")
    assert j["ID"] == e[0]["JobID"]


def test_evaluate_job(nomad_setup):
    assert "EvalID" in nomad_setup.job.evaluate_job("example")

# def test_periodic_job(nomad_setup):
#     assert "EvalID" in nomad_setup.job.periodic_job("example")


def test_delete_job(nomad_setup):
    assert "EvalID" in nomad_setup.job.deregister_job("example")
    assert "example" not in nomad_setup.job
    test_register_job(nomad_setup)


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get(
    "NOMAD_VERSION").split(".")) > (0, 5, 2),
                    reason="Nomad dispatch not supported")
def test_dispatch_job(nomad_setup):
    with open("example_batch_parameterized.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example-batch", job)
    try:
        nomad_setup.job.dispatch_job("example-batch", meta={"time": "500"})
    except (exceptions.URLNotFoundNomadException,
            exceptions.BaseNomadException) as e:
        print(e.nomad_resp.text)
        raise e
    assert "example-batch" in nomad_setup.job


def test_dunder_getitem_exist(nomad_setup):
    j = nomad_setup.job["example"]
    assert isinstance(j, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.job["redis"]


def test_dunder_contain_exists(nomad_setup):
    assert "example" in nomad_setup.job


def test_dunder_contain_not_exist(nomad_setup):
    assert "redis" not in nomad_setup.job


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.job), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.job), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.job.does_not_exist
