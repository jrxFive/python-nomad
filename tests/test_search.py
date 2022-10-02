import pytest

from nomad.api import exceptions


def test_search(nomad_setup):
    result = nomad_setup.search.search("example", "jobs")
    assert "example" in result["Matches"]["jobs"]


def test_search_incorrect_context(nomad_setup):
    # job context doesn't exist
    with pytest.raises(exceptions.InvalidParameters):
        nomad_setup.search.search("example", "job")


def test_search_fuzzy(nomad_setup):
    result = nomad_setup.search.fuzzy_search("example", "jobs")
    assert any(r['ID'] == 'example' for r in result["Matches"]["jobs"])

def test_search_fuzzy_incorrect_context(nomad_setup):
    # job context doesn't exist
    with pytest.raises(exceptions.InvalidParameters):
        nomad_setup.search.fuzzy_search("example", "job")


def test_search_str(nomad_setup):
    assert isinstance(str(nomad_setup.search), str)


def test_search_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.search), str)