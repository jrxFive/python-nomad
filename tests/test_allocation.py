import pytest
import json
import uuid
import responses
import tests.common as common
import os


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


def test_get_allocation(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert isinstance(nomad_setup.allocation.get_allocation(id), dict) == True


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 9, 2),
    reason="Nomad alloc stop not supported",
)
def test_stop_allocation(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert isinstance(nomad_setup.allocation.stop_allocation(id), dict) == True


def test_dunder_getitem_exist(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    a = nomad_setup.allocation[id]
    assert isinstance(a, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):  # restucture try/except/raises
        j = nomad_setup.allocation[str(uuid.uuid4())]


def test_dunder_contain_exists(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert id in nomad_setup.allocation


def test_dunder_contain_not_exist(nomad_setup):

    assert str(uuid.uuid4()) not in nomad_setup.allocation


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocation), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocation), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocation.does_not_exist


@responses.activate
#
# fix No data when you are using namespaces #82
#
def test_get_allocation_with_namespace(nomad_setup_with_namespace):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/allocation/a8198d79-cfdb-6593-a999-1e9adabcba2e?namespace={namespace}".format(
            ip=common.IP, port=common.NOMAD_PORT, namespace=common.NOMAD_NAMESPACE
        ),
        status=200,
        json={
            "ID": "a8198d79-cfdb-6593-a999-1e9adabcba2e",
            "EvalID": "5456bd7a-9fc0-c0dd-6131-cbee77f57577",
            "Namespace": common.NOMAD_NAMESPACE,
            "Name": "example.cache[0]",
            "NodeID": "fb2170a8-257d-3c64-b14d-bc06cc94e34c",
            "PreviousAllocation": "516d2753-0513-cfc7-57ac-2d6fac18b9dc",
            "NextAllocation": "cd13d9b9-4f97-7184-c88b-7b451981616b",
        },
    )
    assert (
        common.NOMAD_NAMESPACE
        in nomad_setup_with_namespace.allocation.get_allocation("a8198d79-cfdb-6593-a999-1e9adabcba2e")["Namespace"]
    )
