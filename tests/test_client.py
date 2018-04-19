import pytest
import json

# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


def test_ls_list_files(nomad_setup):
    """Use Functioncal Test Instead"""
    # test_register_job(nomad_setup)
    #
    # a = nomad_setup.allocations.get_allocations()[0]["ID"]
    # f = nomad_setup.client.ls.list_files(a)


def test_stat_stat_file(nomad_setup):
    """Use Functioncal Test Instead"""
    # test_register_job(nomad_setup)
    #
    # a = nomad_setup.allocations.get_allocations()[0]["ID"]
    # f = nomad_setup.client.stat.stat_file(a)


def test_cat_read_file(nomad_setup):
    """Use Functioncal Test Instead"""
    # test_register_job(nomad_setup)
    #
    # a = nomad_setup.allocations.get_allocations()[0]["ID"]
    # f = nomad_setup.client.cat.read_file(a,"/redis/redis-executor.out")


def test_read_stats(nomad_setup):
    """Use Functioncal Test Instead"""
    # test_register_job(nomad_setup)
    #
    # f = nomad_setup.client.stats.read_stats()


def test_read_allocation_stats(nomad_setup):
    """Use Functioncal Test Instead"""
    # test_register_job(nomad_setup)
    #
    # a = nomad_setup.allocations.get_allocations()[0]["ID"]
    # f = nomad_setup.client.allocation.read_allocation(a)


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
