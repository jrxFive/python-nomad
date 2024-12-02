import pytest
import json
import signal
import time
import os

import nomad

from flaky import flaky


def get_running_allocation(nomad_setup):
    max_iterations = 6
    for _ in range(max_iterations):
        try:
            return next(
                alloc
                for alloc in nomad_setup.allocations.get_allocations()
                if alloc["ClientStatus"] == "running"
            )
        except StopIteration:
            # No alloc running
            time.sleep(5)
    raise ValueError("No allocations running")


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job

        max_iterations = 6
        while nomad_setup.job["example"]["Status"] != "running":
            time.sleep(5)
            if max_iterations == 0:
                raise Exception("register_job, job 'example' did not start")

            max_iterations -= 1


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version"
)
def test_ls_list_files(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.ls.list_files(a)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version"
)
def test_stat_stat_file(nomad_setup):
    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.stat.stat_file(a)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version"
)
def test_streamfile_fail(nomad_setup):

    with pytest.raises(nomad.api.exceptions.BadRequestNomadException):
        a = nomad_setup.allocations.get_allocations()[0]["ID"]
        _ = nomad_setup.client.stream_file.stream(a, 1, "start", "/redis/executor")  # invalid file name


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version"
)
def test_read_stats(nomad_setup):

    f = nomad_setup.client.stats.read_stats()


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version"
)
def test_read_allocation_stats(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.allocation.read_allocation_stats(a)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 9, 1), reason="Not supported in version"
)
def test_signal_allocation(nomad_setup):
    alloc_id = get_running_allocation(nomad_setup)["ID"]
    nomad_setup.client.allocation.signal_allocation(alloc_id, signal.SIGUSR1.name)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 9, 1), reason="Not supported in version"
)
def test_signal_allocation_task(nomad_setup):
    allocation = get_running_allocation(nomad_setup)
    alloc_id = allocation["ID"]
    task = list(allocation["TaskStates"].keys())[0]
    nomad_setup.client.allocation.signal_allocation(alloc_id, signal.SIGUSR1.name, task)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 9, 1), reason="Not supported in version"
)
def test_signal_allocation_invalid_signal(nomad_setup):
    alloc_id = get_running_allocation(nomad_setup)["ID"]
    with pytest.raises(nomad.api.exceptions.BaseNomadException, match="invalid signal"):
        nomad_setup.client.allocation.signal_allocation(alloc_id, "INVALID-SIGNAL")


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version"
)
def test_gc_all_allocations(nomad_setup):
    node_id = nomad_setup.nodes.get_nodes()[0]["ID"]
    nomad_setup.client.gc_all_allocations.garbage_collect(node_id)
    nomad_setup.client.gc_all_allocations.garbage_collect()


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.client), str)
    assert isinstance(str(nomad_setup.client.ls), str)
    assert isinstance(str(nomad_setup.client.cat), str)
    assert isinstance(str(nomad_setup.client.stat), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.client), str)
    assert isinstance(repr(nomad_setup.client.ls), str)
    assert isinstance(repr(nomad_setup.client.cat), str)
    assert isinstance(repr(nomad_setup.client.stat), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.client.does_not_exist

    with pytest.raises(AttributeError):
        d = nomad_setup.client.ls.does_not_exist

    with pytest.raises(AttributeError):
        d = nomad_setup.client.cat.does_not_exist

    with pytest.raises(AttributeError):
        d = nomad_setup.client.stat.does_not_exist
