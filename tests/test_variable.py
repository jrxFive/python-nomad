import pytest
import os

# Nomad doesn't have any variables by default
from nomad.api import exceptions


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_create_variable(nomad_setup):
    payload = {
        "Items": {"user": "test", "password": "test123"},
    }
    nomad_setup.variable.create_variable("example/first", payload)
    assert "example/first" in nomad_setup.variables


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_create_variable_in_namespace(nomad_setup):
    payload = {
        "Items": {"user": "test2", "password": "321tset"},
    }
    nomad_setup.variable.create_variable("example/second", payload, namespace="default")
    assert "example/second" in nomad_setup.variables


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_create_variable_with_cas(nomad_setup):
    payload = {
        "Items": {"user": "test3", "password": "321tset123"},
    }
    nomad_setup.variable.create_variable("example/third", payload, cas=0)
    assert "example/third" in nomad_setup.variables


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variable_and_check_value(nomad_setup):
    var = nomad_setup.variable.get_variable("example/first")
    assert var["Items"]["user"] == "test"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_variable_in_namespace(nomad_setup):
    var = nomad_setup.variable.get_variable("example/first", namespace="default")
    assert var["Items"]["user"] == "test"


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_get_no_exist_variable(nomad_setup):
    with pytest.raises(KeyError):
        assert nomad_setup.variable["no_exist"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_getitem_exist(nomad_setup):
    var = nomad_setup.variable["example/first"]
    assert isinstance(var, dict)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_str(nomad_setup):
    assert isinstance(str(nomad_setup.variable), str)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.variable), str)


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_getattr(nomad_setup):
    with pytest.raises(AttributeError):
        nomad_setup.variable.does_not_exist


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_exist(nomad_setup):
    assert "example/second" in nomad_setup.variable


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_no_exist(nomad_setup):
    assert "no_exist" not in nomad_setup.variable


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_variable_getitem_not_exist(nomad_setup):
    with pytest.raises(KeyError):
        nomad_setup.variable["no_exists"]


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_delete_variable(nomad_setup):
    assert 3 == len(nomad_setup.variables.get_variables())
    nomad_setup.variable.delete_variable("example/third")
    assert "example/third" not in nomad_setup.variables
    assert 2 == len(nomad_setup.variables.get_variables())


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_delete_variable_in_namespace(nomad_setup):
    assert 2 == len(nomad_setup.variables.get_variables())
    nomad_setup.variable.delete_variable("example/second", namespace="default")
    assert "example/third" not in nomad_setup.variables
    assert 1 == len(nomad_setup.variables.get_variables())


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 4, 0), reason="Not supported in version"
)
def test_delete_variable_with_cas(nomad_setup):
    variable_path = "variable_with_cas"
    payload = {
        "Items": {"user": "test4", "password": "test123567"},
    }
    var = nomad_setup.variable.create_variable(variable_path, payload)
    assert variable_path in nomad_setup.variables
    with pytest.raises(exceptions.VariableConflict):
        nomad_setup.variable.delete_variable(variable_path, cas=var["ModifyIndex"] + 1)
        assert variable_path in nomad_setup.variables
    nomad_setup.variable.delete_variable(variable_path, cas=var["ModifyIndex"])
    assert variable_path not in nomad_setup.variables
