import pytest
import os


# integration tests requires nomad Vagrant VM or Binary running
@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 7, 1), reason="Not supported in version"
)
def test_metrics(nomad_setup):
    nomad_setup.metrics.get_metrics()


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.metrics), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.metrics), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.metrics.does_not_exist
