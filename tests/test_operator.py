import pytest
import os
from nomad.api import exceptions


# integration tests requires nomad Vagrant VM or Binary running
@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 5), reason="Not supported in version"
)
def test_get_configuration_default(nomad_setup):
    assert isinstance(nomad_setup.operator.get_configuration(), dict)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 5), reason="Not supported in version"
)
def test_get_configuration_stale(nomad_setup):
    assert isinstance(nomad_setup.operator.get_configuration(stale=True), dict)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 5, 5), reason="Not supported in version"
)
def test_delete_peer(nomad_setup):
    with pytest.raises(exceptions.BaseNomadException):
        nomad_setup.operator.delete_peer("192.168.33.10:4646")


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.operator), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.operator), str)


def test_dunder_getattr(nomad_setup):
    with pytest.raises(AttributeError):
        d = nomad_setup.operator.does_not_exist
