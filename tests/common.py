import os
import requests

# internal ip of docker
IP = os.environ.get("NOMAD_IP", "192.168.33.10")

# use vagrant PORT if env variable is not specified, generally for local
# testing
NOMAD_PORT = os.environ.get("NOMAD_PORT", 4646)

# Security token
NOMAD_TOKEN = os.environ.get("NOMAD_TOKEN", None)

# Test namespace
NOMAD_NAMESPACE = "admin"

# Security token
VAULT_POLICY_INVALID_TOKEN = '1a77d23a-01f9-d848-8457-08bcec267c65'
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root")
VAULT_ADDR  = os.environ.get("VAULT_ADDR", "http://" + IP + ":8200")
VAULT_TEST = os.environ.get("VAULT_TEST", "true")
VAULT_VERSION = os.environ.get("VAULT_VERSION", "0.6.0")

if VAULT_TEST != "false":
    if tuple(int(i) for i in os.environ.get("VAULT_VERSION").split(".")) >= (0, 6, 2):
        print ("\n Vault integration")
    # create token based on policy "policy-demo"
        headers = {'X-Vault-Token': 'root'}
        payload = '{"policies": ["policy-demo"],"ttl": "3h","renewable": true}'
        r = requests.post(VAULT_ADDR + "/v1" + "/auth/token/create", headers=headers, data=payload)
        VAULT_POLICY_TOKEN=r.json()["auth"]["client_token"]
        print("\n SecurityVaultAclForPolicy: {}\n".format(VAULT_POLICY_TOKEN))
        print("\n SecurityVaultRootToken: root")
