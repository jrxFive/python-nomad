import pytest
import os
import nomad
import json


# integration tests requires nomad Vagrant VM or Binary running
@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_validate_job(nomad_setup):
    with open("example.json") as job:
        nomad_setup.validate.validate_job(json.loads(job.read()))


# integration tests requires nomad Vagrant VM or Binary running
@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 0), reason="Not supported in version"
)
def test_invalid_job(nomad_setup):
    with pytest.raises(nomad.api.exceptions.BadRequestNomadException):
        nomad_setup.validate.validate_job({})


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.validate), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.validate), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.validate.does_not_exist
