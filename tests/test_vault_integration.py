import pytest
import nomad
import json
import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from nomad.api import exceptions

def requests_retry_session(retries=3, backoff_factor=0.3,
                status_forcelist=(500, 502, 504), session=None,):
        session = session or requests.Session()
        retry = Retry(total=retries,
                      read=retries,
                      connect=retries,
                      backoff_factor=backoff_factor,
                      status_forcelist=status_forcelist,
                      )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

# # integration tests requires nomad Vagrant VM or Binary running
# Specific token for this policy
# Register Job
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-1)
def test_register_vault_job_valid(nomad_setup_vault_valid_token):
    with open("vault.json") as fh:
        job = json.loads(fh.read())
        nomad_setup_vault_valid_token.job.register_job("vault", job)
        assert "vault" in nomad_setup_vault_valid_token.job


# Specific token for this policy
# Get Job
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-2)
def test_get_vault_job_valid(nomad_setup_vault_valid_token):
    assert isinstance(nomad_setup_vault_valid_token.job.get_job("vault"), dict) == True


# Specific token for this policy
# Validate Job
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-3)
def test_get_vault_job_valid(nomad_setup_vault_valid_token):
    assert isinstance(nomad_setup_vault_valid_token.job.get_job("vault"), dict) == True

# Specific token for this policy
# Validate secret from vault
# deploy a container that run and http server
# and shows the secret stored at vault
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-4)
def test_get_secret_from_vault_job_valid():
    url="http://localhost:8080"
    response = requests_retry_session(retries=20).get(url,timeout=60)
    assert "python_nomad" in response.text


@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-5)
def test_delete_vault_job(nomad_setup_vault_valid_token):
    assert "EvalID" in nomad_setup_vault_valid_token.job.deregister_job("vault")
    test_register_vault_job_valid(nomad_setup_vault_valid_token)

# Specific BAD token for this policy
# test non valid token for deploy
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or os.environ.get("VAULT_TEST") != "true",
    reason="Not supported in version. At version 0.8.5 see regresion of 8.5.6 at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md, or you have configured a false VAULT_TEST")
@pytest.mark.run(order=-6)
def test_register_vault_job_invalid(nomad_setup_vault_invalid_token):
    with open("vault.json") as fh:
        job = json.loads(fh.read())
        with pytest.raises(nomad.api.exceptions.BaseNomadException):
            nomad_setup_vault_invalid_token.job.register_job("vault", job)
