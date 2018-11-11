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

# VAULT INTEGRATION
# Specific token for this policy
# Register Job
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_register_vault_job_valid(nomad_setup_vault_valid_token):
    if tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 9, 0):
        vault_job = "vault.json"
    else:
        vault_job = "vault_kv.json"
    with open(vault_job) as fh:
        job = json.loads(fh.read())
        nomad_setup_vault_valid_token.job.register_job("vault", job)
        assert "vault" in nomad_setup_vault_valid_token.job


# VAULT INTEGRATION
# Specific token for this policy
# Get Job
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_get_vault_job_valid(nomad_setup_vault_valid_token):
    assert isinstance(nomad_setup_vault_valid_token.job.get_job("vault"), dict) == True


# VAULT INTEGRATION
# Specific token for this policy
# Validate Job
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_get_vault_job_valid(nomad_setup_vault_valid_token):
    assert isinstance(nomad_setup_vault_valid_token.job.get_job("vault"), dict) == True

# VAULT INTEGRATION
# Specific token for this policy
# Validate secret from vault
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_get_secret_from_vault_job_valid():
    url="http://localhost:8080"
    response = requests_retry_session(retries=20).get(url,timeout=60)
    assert "python_nomad" in response.text


# VAULT INTEGRATION
# Specific token for this policy
# De-Register Job
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_delete_vault_job(nomad_setup_vault_valid_token):
    assert "EvalID" in nomad_setup_vault_valid_token.job.deregister_job("vault")
    test_register_vault_job_valid(nomad_setup_vault_valid_token)

# VAULT INTEGRATION
# Specific token for this policy
# Register Job with Bad Vault Token. It will report not authorized
# Depens on version uses versioned secrets
#
# NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
# NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
@pytest.mark.skipif(tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 6, 2)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,8,5)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) <= (0,5,0)
    or tuple(int(i) for i in os.environ.get("NOMAD_VERSION").split(".")) == (0,5,6)
    or os.environ.get("VAULT_TEST") == "false",
    reason="0.8.5 vault: Fix [GH-4698]. 0.5.6 server/vault: [GH-2648]. Review at https://github.com/hashicorp/nomad/blob/master/CHANGELOG.md")
def test_register_vault_job_invalid(nomad_setup_vault_invalid_token):
    if tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) < (0, 9, 0):
        vault_job = "vault.json"
    else:
        vault_job = "vault_kv.json"
    with open(vault_job) as fh:
        job = json.loads(fh.read())
        with pytest.raises(nomad.api.exceptions.BaseNomadException):
            nomad_setup_vault_invalid_token.job.register_job("vault", job)
