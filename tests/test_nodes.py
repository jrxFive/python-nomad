import pytest
import os


# integration tests requires nomad Vagrant VM or Binary running
def test_get_nodes(nomad_setup):
    assert isinstance(nomad_setup.nodes.get_nodes(), list) == True

def test_get_node(nomad_setup):
    node = nomad_setup.nodes.get_nodes()[0]
    print(node)
    assert node["ID"] in nomad_setup.nodes
def test_get_nodes_prefix(nomad_setup):
    nodes = nomad_setup.nodes.get_nodes()
    prefix = nodes[0]["ID"][:4]
    nomad_setup.nodes.get_nodes(prefix=prefix)
def test_get_nodes_resouces(nomad_setup):
    nodes = nomad_setup.nodes.get_nodes(resources=True)
    print(nodes)
    assert "NodeResources" in nodes[0]

@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (1, 3, 0), reason="Not supported in version"
)
def test_get_nodes_os(nomad_setup):
    nodes = nomad_setup.nodes.get_nodes(os=True)
    assert "os.name" in nodes[0]["Attributes"]

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
    assert hasattr(nomad_setup.nodes, "__iter__")
    for j in nomad_setup.nodes:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.nodes) >= 0
