import pytest
import json
import time
import os

import nomad

from flaky import flaky


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job

    time.sleep(20)


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version")
def test_ls_list_files(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.ls.list_files(a)


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version")
def test_stat_stat_file(nomad_setup):
    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.stat.stat_file(a)


@flaky(max_runs=5, min_passes=1)
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version")
def test_cat_read_file(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.cat.read_file(a, "/redis/executor.out")


@flaky(max_runs=5, min_passes=1)
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 7, 1), reason="Not supported in version")
def test_read_file_offset(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    _ = nomad_setup.client.read_at.read_file_offset(a, 1, 10, "/redis/executor.out")


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version")
def test_streamfile_fail(nomad_setup):

    with pytest.raises(nomad.api.exceptions.BadRequestNomadException):
        a = nomad_setup.allocations.get_allocations()[0]["ID"]
        _ = nomad_setup.client.stream_file.stream(a, 1, "start", "/redis/executor")  #invalid file name


@flaky(max_runs=5, min_passes=1)
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version")
def test_streamlogs(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    _ = nomad_setup.client.stream_logs.stream(a, "redis", "stderr", False)


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version")
def test_read_stats(nomad_setup):

    f = nomad_setup.client.stats.read_stats()


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 6), reason="Not supported in version")
def test_read_allocation_stats(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    f = nomad_setup.client.allocation.read_allocation_stats(a)


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version")
def test_gc_allocation_fail(nomad_setup):

    a = nomad_setup.allocations.get_allocations()[0]["ID"]
    with pytest.raises(nomad.api.exceptions.URLNotFoundNomadException):
        f = nomad_setup.client.gc_allocation.garbage_collect(a)  # attempt on non-stopped allocation


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
