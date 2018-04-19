import pytest


# integration tests requires nomad Vagrant VM or Binary running
def test_get_nodes(nomad_setup):
    assert isinstance(nomad_setup.nodes.get_nodes(), list) == True


def test_dunder_getitem_exist(nomad_setup):
    n = nomad_setup.nodes["pynomad1"]
    assert isinstance(n, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.nodes["pynomad2"]


def test_dunder_contain_exists(nomad_setup):
    assert "pynomad1" in nomad_setup.nodes


def test_dunder_contain_not_exist(nomad_setup):
    assert "real.localdomain" not in nomad_setup.nodes


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.nodes), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.nodes), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.nodes.does_not_exist


def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.nodes, '__iter__')
    for j in nomad_setup.nodes:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.nodes) >= 0
