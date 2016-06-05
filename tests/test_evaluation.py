import pytest
import tests.common as common
import nomad

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP,port=common.NOMAD_PORT)
    return n

#integration tests requires nomad Vagrant VM or Binary running
def test_get_evaluation(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    assert isinstance(nomad_setup.evaluation.get_evaluation(evalID),dict) == True

def test_get_allocations(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    e = nomad_setup.evaluation[evalID]
    a = nomad_setup.evaluation.get_allocations(evalID)
    assert len(a) >= 0

def test_dunder_getitem_exist(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    e = nomad_setup.evaluation[evalID]
    assert isinstance(e,dict)

def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError): #restucture try/except/raises
        _ = nomad_setup.evaluation["nope"]

def test_dunder_contain_exists(nomad_setup):
    evalID = nomad_setup.job.get_allocations("example")[0]["EvalID"]
    assert evalID in nomad_setup.evaluation

def test_dunder_contain_not_exist(nomad_setup):
    assert "nope" not in nomad_setup.evaluation

def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.evaluation),str)

def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.evaluation),str)

def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        _ = nomad_setup.evaluation.does_not_exist
