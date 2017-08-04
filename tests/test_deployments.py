import pytest
import tests.common as common
import os
import nomad


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT)
    return n

# integration tests requires nomad Vagrant VM or Binary running

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_get_evaluation(nomad_setup):
    assert "example" == nomad_setup.deployments.get_deployments()[0]["JobID"]

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_getitem_exist(nomad_setup):
    jobID = nomad_setup.deployments.get_deployments()[0]["ID"]
    d = nomad_setup.deployment[jobID]
    assert isinstance(d, dict)

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_getitem_not_exist(nomad_setup):
    with pytest.raises(KeyError):
        _ = nomad_setup.deployments["nope"]

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_contain_exists(nomad_setup):
    jobID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert jobID in nomad_setup.deployments

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_contain_not_exist(nomad_setup):
    assert "nope" not in nomad_setup.deployments

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_len(nomad_setup):
    assert len(nomad_setup.deployments) == 1

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_dunder_iter(nomad_setup):
    for d in nomad_setup.deployments:
        pass


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.deployments), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.deployments), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.deployments.does_not_exist
