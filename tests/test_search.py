import os
import pytest

from nomad.api import exceptions


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search(nomad_setup):
    result = nomad_setup.search.search("example", "jobs")
    assert "example" in result["Matches"]["jobs"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search_incorrect_context(nomad_setup):
    # job context doesn't exist
    with pytest.raises(exceptions.InvalidParameters):
        nomad_setup.search.search("example", "job")


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search_fuzzy(nomad_setup):
    result = nomad_setup.search.fuzzy_search("example", "jobs")
    assert any(r["ID"] == "example" for r in result["Matches"]["jobs"])


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search_fuzzy_incorrect_context(nomad_setup):
    # job context doesn't exist
    with pytest.raises(exceptions.InvalidParameters):
        nomad_setup.search.fuzzy_search("example", "job")


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search_str(nomad_setup):
    assert isinstance(str(nomad_setup.search), str)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 1, 0), reason="Not supported in version"
)
def test_search_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.search), str)
