import pytest
import tests.common as common
import nomad
import json


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT)
    return n

# integration tests requires nomad Vagrant VM or Binary running


def test_get_node(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert isinstance(nomad_setup.node.get_node(nodeID), dict) == True


def test_get_allocations(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    n = nomad_setup.node[nodeID]
    a = nomad_setup.node.get_allocations(nodeID)
    assert len(a) >= 0


def test_evaluate_node(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert "EvalIDs" in nomad_setup.node.evaluate_node(nodeID)


def test_drain_node(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert "EvalIDs" in nomad_setup.node.drain_node(nodeID)
    assert "EvalIDs" in nomad_setup.node.drain_node(nodeID, True)
    assert nomad_setup.node[nodeID]["Drain"] == True
    nomad_setup.node.drain_node(nodeID)
    assert nomad_setup.node[nodeID]["Drain"] == False


def test_dunder_getitem_exist(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    n = nomad_setup.node[nodeID]
    assert isinstance(n, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        _ = nomad_setup.node["pynomad2"]


def test_dunder_contain_exists(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert nodeID in nomad_setup.node


def test_dunder_contain_not_exist(nomad_setup):
    assert "pynomad2" not in nomad_setup.node


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.node), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.node), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.node.does_not_exist
