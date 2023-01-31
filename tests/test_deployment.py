import json
import pytest
import os
import nomad
import uuid
import responses
import tests.common as common


def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


# integration tests requires nomad Vagrant VM or Binary running
@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_get_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert isinstance(nomad_setup.deployment.get_deployment(deploymentID), dict)
    assert deploymentID == nomad_setup.deployment.get_deployment(deploymentID)["ID"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_get_deployment_allocations(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert isinstance(nomad_setup.deployment.get_deployment_allocations(deploymentID), list)
    assert isinstance(nomad_setup.deployment.get_deployment_allocations(deploymentID)[0], dict)
    assert "example" == nomad_setup.deployment.get_deployment_allocations(deploymentID)[0]["JobID"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_fail_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.fail_deployment(deploymentID)
    except nomad.api.exceptions.URLNotFoundNomadException as err:
        assert err.nomad_resp.text == "can't fail terminal deployment"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_pause_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.pause_deployment(deploymentID, False)
    except nomad.api.exceptions.BaseNomadException as err:
        assert err.nomad_resp.text == "can't resume terminal deployment"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_promote_all_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.promote_deployment_all(deploymentID)
    except nomad.api.exceptions.BaseNomadException as err:
        assert err.nomad_resp.text == "can't promote terminal deployment"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_promote_all_deployment(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    try:
        nomad_setup.deployment.promote_deployment_groups(deploymentID)
    except nomad.api.exceptions.BaseNomadException as err:
        assert err.nomad_resp.text == "can't promote terminal deployment"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_deployment_allocation_health(nomad_setup):
    deploymentID = nomad_setup.deployments.get_deployments()[0]["ID"]
    allocationID = nomad_setup.deployment.get_deployment(deploymentID)["ID"]
    try:
        nomad_setup.deployment.deployment_allocation_health(deploymentID, unhealthy_allocations=[allocationID])
    except nomad.api.exceptions.BaseNomadException as err:
        assert err.nomad_resp.text == "can't set health of allocations for a terminal deployment"


def test_dunder_getitem_exist(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    e = nomad_setup.evaluation[evalID]
    assert isinstance(e, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        _ = nomad_setup.deployment[str(uuid.uuid4())]


def test_dunder_contain_exists(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    assert evalID in nomad_setup.evaluation


def test_dunder_contain_not_exist(nomad_setup):
    assert str(uuid.uuid4()) not in nomad_setup.deployment


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.deployment), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.deployment), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.deployment.does_not_exist


@responses.activate
#
# fix No data when you are using namespaces #82
#
def test_get_deployment_with_namespace(nomad_setup_with_namespace):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/deployment/a8198d79-cfdb-6593-a999-1e9adabcba2e?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json={
            "ID": "70638f62-5c19-193e-30d6-f9d6e689ab8e",
            "JobID": "example",
            "JobVersion": 1,
            "JobModifyIndex": 17,
            "JobSpecModifyIndex": 17,
            "JobCreateIndex": 7,
            "Namespace": common.NOMAD_NAMESPACE,
            "Name": "example.cache[0]",
        },
    )
    assert (
        common.NOMAD_NAMESPACE
        in nomad_setup_with_namespace.deployment.get_deployment("a8198d79-cfdb-6593-a999-1e9adabcba2e")["Namespace"]
    )


@responses.activate
def test_get_deployments_with_namespace_override_namespace_declared_on_create(nomad_setup_with_namespace):
    override_namespace_name = "override-namespace"
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/deployments?prefix=a8198d79-cfdb-6593-a999-1e9adabcba2e&namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=override_namespace_name
        ),
        status=200,
        json={
            "ID": "70638f62-5c19-193e-30d6-f9d6e689ab8e",
            "JobID": "example",
            "JobVersion": 1,
            "JobModifyIndex": 17,
            "JobSpecModifyIndex": 17,
            "JobCreateIndex": 7,
            "Namespace": override_namespace_name,
            "Name": "example.cache[0]",
        },
    )

    nomad_setup_with_namespace.deployments.get_deployments(
        "a8198d79-cfdb-6593-a999-1e9adabcba2e", namespace=override_namespace_name
    )
