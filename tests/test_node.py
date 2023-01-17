import os
import pytest
import uuid

from nomad.api import exceptions as nomad_exceptions


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


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) > (1, 1, 0), reason="Not supported in version"
)
def test_drain_node(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert "EvalIDs" in nomad_setup.node.drain_node(nodeID)
    assert "EvalIDs" in nomad_setup.node.drain_node(nodeID, True)
    assert nomad_setup.node[nodeID]["Drain"] is True
    nomad_setup.node.drain_node(nodeID)
    assert nomad_setup.node[nodeID]["Drain"] is False


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version"
)
def test_drain_node_with_spec(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert "EvalIDs" in nomad_setup.node.drain_node_with_spec(nodeID, drain_spec={"Duration": "-100000000"})
    assert nomad_setup.node[nodeID]["Drain"] is True
    assert "EvalIDs" in nomad_setup.node.drain_node_with_spec(nodeID, drain_spec={}, mark_eligible=True)
    assert nomad_setup.node[nodeID]["Drain"] is False


@pytest.mark.skipif(
    tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 1), reason="Not supported in version"
)
def test_eligible_node(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]

    nomad_setup.node.eligible_node(nodeID, ineligible=True)
    assert nomad_setup.node[nodeID]["SchedulingEligibility"] == "ineligible"

    nomad_setup.node.eligible_node(nodeID, eligible=True)
    assert nomad_setup.node[nodeID]["SchedulingEligibility"] == "eligible"

    with pytest.raises(nomad_exceptions.InvalidParameters):
        assert nomad_setup.node.eligible_node(nodeID, eligible=True, ineligible=True)

    with pytest.raises(nomad_exceptions.InvalidParameters):
        assert nomad_setup.node.eligible_node(nodeID)


def test_dunder_getitem_exist(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    n = nomad_setup.node[nodeID]
    assert isinstance(n, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        _ = nomad_setup.node[str(uuid.uuid4())]


def test_dunder_contain_exists(nomad_setup):
    nodeID = nomad_setup.nodes["pynomad1"]["ID"]
    assert nodeID in nomad_setup.node


def test_dunder_contain_not_exist(nomad_setup):
    assert str(uuid.uuid4()) not in nomad_setup.node


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.node), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.node), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.node.does_not_exist
