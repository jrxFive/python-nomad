import pytest
import sys


# integration tests requires nomad Vagrant VM or Binary running
def test_get_regions(nomad_setup):
    assert isinstance(nomad_setup.regions.get_regions(), list) == True


def test_dunder_getitem_exist(nomad_setup):
    n = nomad_setup.regions["global"]
    if int(sys.version[0]) == 3:
        assert isinstance(n, str)
    else:
        assert isinstance(n, unicode)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.regions["us-east-1"]


def test_dunder_contain_exists(nomad_setup):
    assert "global" in nomad_setup.regions


def test_dunder_contain_not_exist(nomad_setup):
    assert "us-east-1" not in nomad_setup.regions


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.regions), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.regions), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.regions.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.regions, "__iter__")
    for j in nomad_setup.regions:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.regions) >= 0
