import pytest
import nomad
import json
import os
from nomad.api import exceptions


# # integration tests requires nomad Vagrant VM or Binary running
# Specific token for this policy
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 0), reason="Not supported in version")
@pytest.mark.run(order=-1)
def test_register_job_valid(nomad_setup_vault_valid_token):
    with open("vault.json") as fh:
        job = json.loads(fh.read())
        nomad_setup_vault_valid_token.job.register_job("vault", job)
        assert "vault" in nomad_setup_vault_valid_token.job


# Specific token for this policy
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 0), reason="Not supported in version")
@pytest.mark.run(order=-2)
def test_get_job_valid(nomad_setup_vault_valid_token):
    assert isinstance(nomad_setup_vault_valid_token.job.get_job("vault"), dict) == True


# Specific token for this policy
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 0), reason="Not supported in version")
@pytest.mark.run(order=-3)
def test_delete_job_valid(nomad_setup):
    assert "EvalID" in nomad_setup.job.deregister_job("vault")


# Specific BAD token for this policy
# test non valid token for deploy
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 8, 0), reason="Not supported in version")
@pytest.mark.run(order=-4)
def test_register_job_invalid(nomad_setup_vault_invalid_token):
    with open("vault.json") as fh:
        job = json.loads(fh.read())

        with pytest.raises(nomad.api.exceptions.URLNotFoundNomadException):
            nomad_setup_vault_invalid_token.job.register_job("vault", job)
