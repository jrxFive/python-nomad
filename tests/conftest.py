import nomad
import pytest
import tests.common as common

@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n

@pytest.fixture
def nomad_setup_vault_valid_token():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN, vaulttoken=common.VAULT_POLICY_TOKEN)
    return n

@pytest.fixture
def nomad_setup_vault_invalid_token():
    n = nomad.Nomad(host=common.IP, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN, vaulttoken=common.VAULT_POLICY_INVALID_TOKEN)
    return n
