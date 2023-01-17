import pytest
import os


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variables(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables())


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variables_with_prefix(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables("example/first"))


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variables_with_prefix_no_exist(nomad_setup):
    assert 0 == len(nomad_setup.variables.get_variables("no_exist_var"))


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variables_from_namespace(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables(namespace="default"))


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_iter_variables(nomad_setup):
    assert hasattr(nomad_setup.variables, "__iter__")
    for _ in nomad_setup.variables:
        pass


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_str(nomad_setup):
    assert isinstance(str(nomad_setup.variables), str)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.variables), str)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_not_exist(nomad_setup):
    assert "no_exist" not in nomad_setup.variables


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_exist(nomad_setup):
    assert "example/first" in nomad_setup.variables


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_getitem_exist(nomad_setup):
    var = nomad_setup.variables["example/first"]
    assert isinstance(var, dict)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_getitem_not_exist(nomad_setup):
    with pytest.raises(KeyError):
        nomad_setup.variables["no_exists"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variables_getattr(nomad_setup):
    with pytest.raises(AttributeError):
        nomad_setup.variables.does_not_exist
