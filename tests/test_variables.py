def test_get_variables(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables())


def test_get_variables_with_prefix(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables("example"))


def test_get_variables_with_prefix_no_exist(nomad_setup):
    assert 0 == len(nomad_setup.variables.get_variables("no_exist_var"))


def test_get_variables_from_namespace(nomad_setup):
    assert 1 == len(nomad_setup.variables.get_variables(namespace="default"))