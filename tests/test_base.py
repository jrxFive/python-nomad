import os

import mock
import pytest
import requests
import responses

import nomad
import tests.common as common


def test_base_region_qs():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN, region="random")
    qs = n.jobs._query_string_builder("v1/jobs")

    assert "region" in qs
    assert qs["region"] == "random"


def test_base_region_and_namespace_qs():
    n = nomad.Nomad(
        host=common.IP,
        port=common.NOMAD_PORT,
        verify=False,
        token=common.NOMAD_TOKEN,
        region="random",
        namespace="test",
    )
    qs = n.jobs._query_string_builder("v1/jobs")

    assert "region" in qs
    assert qs["region"] == "random"

    assert "namespace" in qs
    assert qs["namespace"] == "test"


def test_base_region_and_namespace_qs_namespace_override():
    n = nomad.Nomad(
        host=common.IP,
        port=common.NOMAD_PORT,
        verify=False,
        token=common.NOMAD_TOKEN,
        region="random",
        namespace="test",
    )
    qs = n.jobs._query_string_builder("v1/jobs", {"namespace": "new-namespace"})

    assert "namespace" not in qs
    assert "region" in qs
    assert qs["region"] == "random"


def test_base_region_and_namespace_qs_region_override():
    n = nomad.Nomad(
        host=common.IP,
        port=common.NOMAD_PORT,
        verify=False,
        token=common.NOMAD_TOKEN,
        region="random",
        namespace="test",
    )
    qs = n.jobs._query_string_builder("v1/jobs", {"region": "new-region"})

    assert "region" not in qs
    assert "namespace" in qs
    assert qs["namespace"] == "test"


def test_base_region_and_namespace_qs_overrides_via_params():
    n = nomad.Nomad(
        host=common.IP,
        port=common.NOMAD_PORT,
        verify=False,
        token=common.NOMAD_TOKEN,
        region="random",
        namespace="test",
    )
    qs = n.jobs._query_string_builder("v1/jobs", {"namespace": "new-namespace", "region": "new-region"})

    assert qs == {}


# integration tests requires nomad Vagrant VM or Binary running
def test_base_get_connection_error():
    n = nomad.Nomad(host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.evaluations["nope"]


def test_base_put_connection_error():
    n = nomad.Nomad(host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.system.initiate_garbage_collection()


def test_base_delete_connection_error():
    n = nomad.Nomad(host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.job.deregister_job("example")


@mock.patch("nomad.api.base.requests.Session")
def test_base_raise_exception_not_requests_response_object(mock_requests):
    mock_requests().delete.side_effect = [requests.RequestException()]

    with pytest.raises(nomad.api.exceptions.BaseNomadException) as excinfo:
        n = nomad.Nomad(host="162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)

        _ = n.job.deregister_job("example")

    # excinfo is a ExceptionInfo instance, which is a wrapper around the actual exception raised.
    # The main attributes of interest are .type, .value and .traceback.
    # https://docs.pytest.org/en/3.0.1/assert.html#assertions-about-expected-exceptions
    assert hasattr(excinfo.value.nomad_resp, "text") is False
    assert isinstance(excinfo.value.nomad_resp, requests.RequestException)
    assert "raised due" in str(excinfo.value)


def test_base_raise_exception_is_requests_response_object(nomad_setup):
    with pytest.raises(nomad.api.exceptions.BaseNomadException) as excinfo:
        _ = nomad_setup.job.get_job("examplezz")

    # excinfo is a ExceptionInfo instance, which is a wrapper around the actual exception raised.
    # The main attributes of interest are .type, .value and .traceback.
    # https://docs.pytest.org/en/3.0.1/assert.html#assertions-about-expected-exceptions
    assert hasattr(excinfo.value.nomad_resp, "text") is True
    assert isinstance(excinfo.value.nomad_resp, requests.Response)
    assert "raised with" in str(excinfo.value)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 7, 0), reason="Nomad dispatch not supported"
)
def test_base_get_connnection_not_authorized():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, token="aed2fc63-c155-40d5-b58a-18deed4b73e5", verify=False)
    with pytest.raises(nomad.api.exceptions.URLNotAuthorizedNomadException):
        j = n.job.get_job("example")


@responses.activate
def test_base_use_address_instead_on_host_port():
    responses.add(responses.GET, "https://nomad.service.consul:4646/v1/jobs", status=200, json=[])

    nomad_address = "https://nomad.service.consul:4646"
    n = nomad.Nomad(
        address=nomad_address, host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN
    )
    n.jobs.get_jobs()

@responses.activate
def test_use_custom_user_agent():
    custom_agent_name = "custom_agent"
    responses.add(responses.GET, "https://nomad.service.consul:4646/v1/jobs", status=200, json=[])

    nomad_address = "https://nomad.service.consul:4646"
    n = nomad.Nomad(
        address=nomad_address, host=common.IP, port=common.NOMAD_PORT, verify=False,
        token=common.NOMAD_TOKEN, user_agent=custom_agent_name
    )
    n.jobs.get_jobs()

    assert responses.calls[0].request.headers["User-Agent"] == custom_agent_name

def test_env_variables():
    # This ensures that the env variables are only read upon initialization of Nomad() instance,
    # and not before.
    with mock.patch.dict(os.environ, {"NOMAD_ADDR": "https://foo"}):
        n = nomad.Nomad()
        assert n.address == os.environ["NOMAD_ADDR"]
