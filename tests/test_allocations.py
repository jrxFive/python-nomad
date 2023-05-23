import json
import pytest
import responses
import tests.common as common


def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


# integration tests requires nomad Vagrant VM or Binary running
def test_get_allocations(nomad_setup):
    assert isinstance(nomad_setup.allocations.get_allocations(), list) == True


def test_get_allocations_prefix(nomad_setup):
    allocations = nomad_setup.allocations.get_allocations()
    prefix = allocations[0]["ID"][:4]
    nomad_setup.allocations.get_allocations(prefix=prefix)

def test_get_allocations_resouces(nomad_setup):
    allocations = nomad_setup.allocations.get_allocations(resources=True)
    assert "AllocatedResources" in allocations[0]

def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocations), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocations), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocations.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.allocations, "__iter__")
    for j in nomad_setup.allocations:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.allocations) >= 0


@responses.activate
#
# fix No data when you are using namespaces #82
#
def test_get_allocations_with_namespace(nomad_setup_with_namespace):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/allocations?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json=[
            {
                "ID": "a8198d79-cfdb-6593-a999-1e9adabcba2e",
                "EvalID": "5456bd7a-9fc0-c0dd-6131-cbee77f57577",
                "Namespace": common.NOMAD_NAMESPACE,
                "Name": "example.cache[0]",
                "NodeID": "fb2170a8-257d-3c64-b14d-bc06cc94e34c",
                "PreviousAllocation": "516d2753-0513-cfc7-57ac-2d6fac18b9dc",
                "NextAllocation": "cd13d9b9-4f97-7184-c88b-7b451981616b",
            }
        ],
    )
    assert common.NOMAD_NAMESPACE in nomad_setup_with_namespace.allocations.get_allocations()[0]["Namespace"]


@responses.activate
def test_get_allocations_with_namespace_override_namespace_declared_on_create(nomad_setup_with_namespace):
    override_namespace_name = "namespace=override-namespace"
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/allocations?prefix=a8198d79-cfdb-6593-a999-1e9adabcba2e&namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=override_namespace_name
        ),
        status=200,
        json=[
            {
                "ID": "a8198d79-cfdb-6593-a999-1e9adabcba2e",
                "EvalID": "5456bd7a-9fc0-c0dd-6131-cbee77f57577",
                "Namespace": override_namespace_name,
                "Name": "example.cache[0]",
                "NodeID": "fb2170a8-257d-3c64-b14d-bc06cc94e34c",
                "PreviousAllocation": "516d2753-0513-cfc7-57ac-2d6fac18b9dc",
                "NextAllocation": "cd13d9b9-4f97-7184-c88b-7b451981616b",
            }
        ],
    )

    nomad_setup_with_namespace.allocations.get_allocations(
        "a8198d79-cfdb-6593-a999-1e9adabcba2e", namespace=override_namespace_name
    )
