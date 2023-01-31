import pytest
import tests.common as common
import sys


# integration tests requires nomad Vagrant VM or Binary running
def test_get_leader(nomad_setup):
    if int(sys.version[0]) == 3:
        assert isinstance(nomad_setup.status.leader.get_leader(), str) == True
    else:
        assert isinstance(nomad_setup.status.leader.get_leader(), unicode) == True


def test_get_peers(nomad_setup):
    assert isinstance(nomad_setup.status.peers.get_peers(), list) == True


def test_peers_dunder_getitem_exist(nomad_setup):
    n = nomad_setup.status.peers["{IP}:4647".format(IP=common.IP)]
    if int(sys.version[0]) == 3:
        assert isinstance(n, str)
    else:
        assert isinstance(n, unicode)


def test_peers_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        p = nomad_setup.status.peers["{IP}:4647".format(IP="172.16.10.100")]


def test_peers_dunder_contain_exists(nomad_setup):
    assert "{IP}:4647".format(IP=common.IP) in nomad_setup.status.peers


def test_peers_dunder_contain_not_exist(nomad_setup):
    assert "{IP}:4647".format(IP="172.16.10.100") not in nomad_setup.status.peers


def test_leader_dunder_contain_exists(nomad_setup):
    assert "{IP}:4647".format(IP=common.IP) in nomad_setup.status.leader


def test_leader_dunder_contain_not_exist(nomad_setup):
    assert "{IP}:4647".format(IP="172.16.10.100") not in nomad_setup.status.leader


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.status), str)
    assert isinstance(str(nomad_setup.status.leader), str)
    assert isinstance(str(nomad_setup.status.peers), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.status), str)
    assert isinstance(repr(nomad_setup.status.leader), str)
    assert isinstance(repr(nomad_setup.status.peers), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.status.does_not_exist


def test_peers_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.status.peers, "__iter__")
    for p in nomad_setup.status.peers:
        pass


def test_dunder_len(nomad_setup):
    assert len(nomad_setup.status.leader) >= 0
    assert len(nomad_setup.status.peers) >= 0
