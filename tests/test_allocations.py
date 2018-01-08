import pytest
import tests.common as common
import nomad


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

# integration tests requires nomad Vagrant VM or Binary running


def test_get_allocations(nomad_setup):
    assert isinstance(nomad_setup.allocations.get_allocations(), list) == True


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocations), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocations), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocations.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.allocations, '__iter__')
    for j in nomad_setup.allocations:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.allocations) >= 0
