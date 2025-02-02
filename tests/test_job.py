import json
import os
import uuid

import pytest
import responses

import nomad
import tests.common as common

from flaky import flaky

from nomad.api import exceptions


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


def test_get_job(nomad_setup):
    assert isinstance(nomad_setup.job.get_job("example"), dict) == True


@responses.activate
def test_get_jobs_with_namespace_override_no_namespace_declared_on_create_incorrect_declared_namespace(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/job/18a0f501-41d5-ae43-ff61-1d8ec3ec8314?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json=[
            {
                "Region": "global",
                "ID": "my-job",
                "ParentID": "",
                "Name": "my-job",
                "Namespace": common.NOMAD_NAMESPACE,
                "Type": "batch",
                "Priority": 50,
            }
        ],
    )

    with pytest.raises(exceptions.BaseNomadException):
        nomad_setup.job.get_job(id_=str(uuid.uuid4()))


@responses.activate
def test_get_jobs_with_namespace_override_no_namespace_declared_on_create(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/job/18a0f501-41d5-ae43-ff61-1d8ec3ec8314?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json=[
            {
                "Region": "global",
                "ID": "my-job",
                "ParentID": "",
                "Name": "my-job",
                "Namespace": common.NOMAD_NAMESPACE,
                "Type": "batch",
                "Priority": 50,
            }
        ],
    )

    nomad_setup.job.get_job(id_="18a0f501-41d5-ae43-ff61-1d8ec3ec8314", namespace=common.NOMAD_NAMESPACE)


@responses.activate
def test_get_jobs_with_namespace_override_namespace_declared_on_create(nomad_setup_with_namespace):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/job/18a0f501-41d5-ae43-ff61-1d8ec3ec8314?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace="override-namespace"
        ),
        status=200,
        json=[
            {
                "Region": "global",
                "ID": "my-job",
                "ParentID": "",
                "Name": "my-job",
                "Namespace": common.NOMAD_NAMESPACE,
                "Type": "batch",
                "Priority": 50,
            }
        ],
    )

    nomad_setup_with_namespace.job.get_job(id_="18a0f501-41d5-ae43-ff61-1d8ec3ec8314", namespace="override-namespace")


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
    test_register_job(nomad_setup)


@flaky(max_runs=5, min_passes=1)
def test_dispatch_job(nomad_setup):
    with open("example_batch_parameterized.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example-batch", job)
    try:
        nomad_setup.job.dispatch_job("example-batch", meta={"time": "500"}, id_prefix_template="run1")
    except (exceptions.URLNotFoundNomadException, exceptions.BaseNomadException) as e:
        print(e.nomad_resp.text)
        raise e
    assert "example-batch" in nomad_setup.job


@flaky(max_runs=5, min_passes=1)
def test_dispatch_job_idempotency(nomad_setup):
    with open("example_batch_parameterized.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example-batch-idempotent", job)

    # First dispatch should succeed
    try:
        nomad_setup.job.dispatch_job("example-batch-idempotent", meta={"time": "500"}, id_prefix_template="run1", idempotency_token="737ae8cd-f237-43a5-8fad-0e6a3f94ad55")
    except (exceptions.URLNotFoundNomadException, exceptions.BaseNomadException) as e:
        print(e.nomad_resp.text)
        raise e
    assert "example-batch-idempotent" in nomad_setup.job

    # Second dispatch with the same idempotency token should fail
    with pytest.raises(exceptions.BaseNomadException):
        nomad_setup.job.dispatch_job("example-batch-idempotent", meta={"time": "500"}, id_prefix_template="run2", idempotency_token="737ae8cd-f237-43a5-8fad-0e6a3f94ad55")


def test_summary_job(nomad_setup):
    j = nomad_setup.job["example"]
    assert "JobID" in nomad_setup.job.get_summary(j["ID"])


def test_plan_job(nomad_setup):
    with open("example.json") as fh:
        job = json.loads(fh.read())
        assert "Index" in nomad_setup.job.plan_job(nomad_setup.job["example"]["ID"], job)


def test_versions_job(nomad_setup):
    assert "Versions" in nomad_setup.job.get_versions("example")


def test_versions_job_missing(nomad_setup):
    with pytest.raises(nomad.api.exceptions.URLNotFoundNomadException):
        assert "Versions" in nomad_setup.job.get_versions("example1")


def test_get_job_deployments(nomad_setup):
    assert "JobID" in nomad_setup.job.get_deployments("example")[0]
    assert isinstance(nomad_setup.job.get_deployments("example"), list)
    assert isinstance(nomad_setup.job.get_deployments("example")[0], dict)
    assert "example" == nomad_setup.job.get_deployments("example")[0]["JobID"]


def test_get_job_deployment(nomad_setup):
    assert "JobID" in nomad_setup.job.get_deployment("example")
    assert isinstance(nomad_setup.job.get_deployment("example"), dict)
    assert "example" == nomad_setup.job.get_deployment("example")["JobID"]


def test_get_summary(nomad_setup):
    assert "JobID" in nomad_setup.job.get_summary("example")
    assert isinstance(nomad_setup.job.get_summary("example"), dict)
    assert "example" == nomad_setup.job.get_summary("example")["JobID"]


def test_revert_job(nomad_setup):
    current_job_version = nomad_setup.job.get_deployment("example")["JobVersion"]
    prior_job_version = current_job_version - 1
    nomad_setup.job.revert_job("example", prior_job_version, current_job_version)


def test_stable_job(nomad_setup):
    current_job_version = nomad_setup.job.get_deployment("example")["JobVersion"]
    nomad_setup.job.stable_job("example", current_job_version, True)


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


def test_delete_job_with_invalid_purge_param_raises(nomad_setup):
    with pytest.raises(exceptions.InvalidParameters):
        nomad_setup.job.deregister_job("example", purge="True")


def test_delete_job_with_purge(nomad_setup):
    # Run this last since it will purge the job completely, resetting things like
    # job version
    assert "EvalID" in nomad_setup.job.deregister_job("example", purge=True)

    # Job should not be available after a purge.
    with pytest.raises(exceptions.URLNotFoundNomadException):
        nomad_setup.job.get_job("example")

    # Reregister job
    test_register_job(nomad_setup)
