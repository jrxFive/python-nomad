import os
import subprocess

# internal ip of docker
IP = os.environ.get("NOMAD_IP", "192.168.33.10")

# use vagrant PORT if env variable is not specified, generally for local
# testing
NOMAD_PORT = os.environ.get("NOMAD_PORT", 4646)

# Security token
NOMAD_TOKEN = os.environ.get("NOMAD_TOKEN", None)

# Security token
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root")
VAULT_ADDR = os.environ.get("VAULT_ADDR", "http://" + IP + ":8200")

vaultEnvironment = {"VAULT_TOKEN":"root","VAULT_ADDR":VAULT_ADDR}
p = subprocess.Popen("/tmp/vault token-create -field=token -policy=policy-demo", stdout=subprocess.PIPE, shell=True, env=vaultEnvironment)
(vaulttoken, err) = p.communicate()
p_status = p.wait()
print("\n SecurityVaultAcl: {}\n".format(vaulttoken.decode('utf-8')))

VAULT_POLICY_TOKEN=vaulttoken.decode('utf-8')
VAULT_POLICY_INVALID_TOKEN = '1a77d23a-01f9-d848-8457-08bcec267c65'
