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
def test_get_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert isinstance(nomad_setup.deployment.get_deployment(deploymentID), dict)
    assert deploymentID == nomad_setup.deployment.get_deployment(deploymentID)["ID"]

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_get_deployment_allocations(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert isinstance(nomad_setup.deployment.get_deployment_allocations(deploymentID), list)
    assert isinstance(nomad_setup.deployment.get_deployment_allocations(deploymentID)[0], dict)
    assert "example" == nomad_setup.deployment.get_deployment_allocations(deploymentID)[0]["JobID"]

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_fail_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.fail_deployment(deploymentID)
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't fail terminal deployment"

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_pause_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.pause_deployment(deploymentID, False)
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't resume terminal deployment"

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_promote_all_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.promote_deployment_all(deploymentID)
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't promote terminal deployment"

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_promote_all_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.promote_deployment_groups(deploymentID)
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't promote terminal deployment"

@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version")
def test_deployment_allocation_health(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    allocationID = nomad_setup.deployment.get_deployment(deploymentID)["ID"]
    try:
        nomad_setup.deployment.deployment_allocation_health(deploymentID, unhealthy_allocations=[allocationID])
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't set health of allocations for a terminal deployment"



def test_dunder_getitem_exist(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    e = nomad_setup.evaluation[evalID]
    assert isinstance(e, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        _ = nomad_setup.deployment["nope"]


def test_dunder_contain_exists(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    assert evalID in nomad_setup.evaluation


def test_dunder_contain_not_exist(nomad_setup):
    assert "nope" not in nomad_setup.deployment


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.deployment), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.deployment), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.deployment.does_not_exist
