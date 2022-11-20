TEST_VARIABLE_PATH = "example/first"


def test_create_variable(nomad_setup):
    payload = {
        "Items": {"user": "test", "password": "test123"},
    }
    nomad_setup.variable.create_variable(TEST_VARIABLE_PATH, payload)
    assert "example/first" in nomad_setup.variables


def test_get_variable_and_check_value(nomad_setup):
    var = nomad_setup.variable.get_variable(TEST_VARIABLE_PATH)

    assert var["Items"]["user"] == "test"
