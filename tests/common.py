import os
import requests

# internal ip of docker
IP = os.environ.get("NOMAD_IP", "192.168.33.10")

# use vagrant PORT if env variable is not specified, generally for local
# testing
NOMAD_PORT = os.environ.get("NOMAD_PORT", 4646)

# Security token
NOMAD_TOKEN = os.environ.get("NOMAD_TOKEN", None)

# Security token
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root")
VAULT_ADDR  = os.environ.get("VAULT_ADDR", "http://" + IP + ":8200")
NOMAD_INTEGRATION_VAULT = os.environ.get("NOMAD_INTEGRATION_VAULT", "0.6.2")
VAULT_TEST = os.environ.get("VAULT_TEST", "false")
VAULT_POLICY_INVALID_TOKEN = '1a77d23a-01f9-d848-8457-08bcec267c65'
NOMAD_VERSION = os.environ.get("NOMAD_VERSION", "3.2.0")


NOMAD_INTEGRATION_VAULT_NUMBER = int(NOMAD_INTEGRATION_VAULT.replace(".",""))
NOMAD_VERSION_NUMBER = int(NOMAD_VERSION.replace(".",""))

if VAULT_TEST == "true":
    if NOMAD_VERSION_NUMBER >= NOMAD_INTEGRATION_VAULT_NUMBER:
    # create token based on policy "policy-demo"
    headers = {'X-Vault-Token': 'root'}
    payload = '{"policies": ["policy-demo"],"ttl": "3h","renewable": true}'
    r = requests.post(VAULT_ADDR + "/v1" + "/auth/token/create", headers=headers, data=payload)
    VAULT_POLICY_TOKEN=r.json()["auth"]["client_token"]
    print("\n SecurityVaultAcl: {}\n".format(VAULT_POLICY_TOKEN))
