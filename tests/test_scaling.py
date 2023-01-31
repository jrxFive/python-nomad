import pytest

from nomad.api import exceptions


def test_scaling_list(nomad_setup):
    result = nomad_setup.scaling.get_scaling_policies()
    assert not result


def test_scaling_policy_not_exist(nomad_setup):
    with pytest.raises(exceptions.URLNotFoundNomadException):
        nomad_setup.scaling.get_scaling_policy("example")
