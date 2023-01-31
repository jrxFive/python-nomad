import json
import pytest
import os
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
def test_get_evaluation(nomad_setup):
    assert "example" == nomad_setup.deployments.get_deployments()[0]["JobID"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_get_deployments_prefix(nomad_setup):
    deployments = nomad_setup.deployments.get_deployments()
    prefix = deployments[0]["ID"][:4]
    nomad_setup.deployments.get_deployments(prefix=prefix)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_dunder_getitem_exist(nomad_setup):
    jobID = nomad_setup.deployments.get_deployments()[0]["ID"]
    d = nomad_setup.deployment[jobID]
    assert isinstance(d, dict)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_dunder_getitem_not_exist(nomad_setup):
    with pytest.raises(KeyError):
        _ = nomad_setup.deployments["nope"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_dunder_contain_exists(nomad_setup):
    jobID = nomad_setup.deployments.get_deployments()[0]["ID"]
    assert jobID in nomad_setup.deployments


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_dunder_contain_not_exist(nomad_setup):
    assert "nope" not in nomad_setup.deployments


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_dunder_len(nomad_setup):
    assert len(nomad_setup.deployments) == 1


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
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


@responses.activate
#
# fix No data when you are using namespaces #82
#
def test_get_deployments_with_namespace(nomad_setup_with_namespace):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/deployments?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json=[
            {
                "ID": "70638f62-5c19-193e-30d6-f9d6e689ab8e",
                "JobID": "example",
                "JobVersion": 1,
                "JobModifyIndex": 17,
                "JobSpecModifyIndex": 17,
                "JobCreateIndex": 7,
                "Namespace": common.NOMAD_NAMESPACE,
                "Name": "example.cache[0]",
            }
        ],
    )
    assert common.NOMAD_NAMESPACE in nomad_setup_with_namespace.deployments.get_deployments()[0]["Namespace"]
