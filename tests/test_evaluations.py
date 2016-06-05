import pytest
import tests.common as common
import nomad

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP,port=common.NOMAD_PORT)
    return n


#integration tests requires nomad Vagrant VM or Binary running
def test_get_evaluations(nomad_setup):
    assert isinstance(nomad_setup.evaluations.get_evaluations(),list) == True

def test_dunder_getitem_exist(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    e = nomad_setup.evaluations[evalID]
    assert isinstance(e,dict)

def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):
        j = nomad_setup.evaluations["nope"]

def test_dunder_contain_exists(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    assert evalID in nomad_setup.evaluations

def test_dunder_contain_not_exist(nomad_setup):
    assert "nope"  not in nomad_setup.evaluations

def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.evaluations),str)

def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.evaluations),str)

def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.evaluations.does_not_exist

def test_dunder_iter(nomad_setup):
    assert hasattr(nomad_setup.evaluations, '__iter__')
    for j in nomad_setup.evaluations:
        pass

def test_dunder_len(nomad_setup):
    assert len(nomad_setup.evaluations) >= 0
