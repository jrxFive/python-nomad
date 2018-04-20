import pytest


# integration tests requires nomad Vagrant VM or Binary running
def test_initiate_garbage_collection(nomad_setup):
    nomad_setup.system.initiate_garbage_collection()


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.system), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.system), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.system.does_not_exist
