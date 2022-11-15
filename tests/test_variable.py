

def test_create_variable(nomad_setup):
    payload = {
        "Items": {
            "user": "test",
            "password": "test123"
        },
    }
    nomad_setup.variable.create_variable("example/first", payload)
    assert "example/first" in nomad_setup.variables.get_variables()[0]["Path"]