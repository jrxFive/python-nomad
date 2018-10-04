#!/bin/bash

echo "Get Binary Files"
wget -q -P /tmp/ https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/nomad_${NOMAD_VERSION}_linux_amd64.zip

wget -q -P /tmp/ https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/vault_${VAULT_VERSION}_linux_amd64.zip

echo "Copy binary"
if [ ! -f /usr/bin/nomad ]
then
    cp /tmp/nomad /usr/bin/.
fi

if [ ! -f /usr/bin/vault ]
then
    cp /tmp/vault /usr/bin/.
fi

MAJOR_VERSION=`echo ${NOMAD_VERSION} | cut -d "." -f 2`

echo "Vault: Create policy file"
cat << EOF > /tmp/policy-demo.hcl
path "secret/demo" {
    capabilities = ["read"]
}
EOF

echo "Vault: Start Daemon"
/usr/bin/vault server -dev -dev-listen-address=0.0.0.0:8200 -dev-root-token-id="root" > /var/log/vault.log 2>&1 &
sleep 5

echo "Vault: Write Vault Policies"
VAULT_TOKEN=root vault policy-write -address=http://127.0.0.1:8200 policy-demo /tmp/policy-demo.hcl

echo "Vault: Write Vault Secret"
VAULT_TOKEN=root vault write -address=http://127.0.0.1:8200 secret/demo data=python_nomad

echo "Nomad: Create config folder"
mkdir -p /etc/nomad.d

if [[ ${MAJOR_VERSION} -gt 7 ]]; then
echo "Nomad: Enable Config Vault"
cat << EOF > /etc/nomad.d/vault.hcl
vault
{
  enabled     = true
  address     = "${VAULT_ADDR}"
  token = "root"
  allow_unauthenticated = false
}
EOF
fi

echo "Nomad: Config base"
cat << EOF > /etc/nomad.d/base_config.hcl
datacenter = "dc1"
name = "pynomad1"
bind_addr = "${NOMAD_IP}"
client
{
    enabled = true
    node_class = "default"
}
ports
{
  http = ${NOMAD_PORT}
  rpc  = 4647
}
addresses
{
  http = "${NOMAD_IP}"
  rpc = "${NOMAD_IP}"
}
advertise
{
  http = "${NOMAD_IP}:${NOMAD_PORT}"
  rpc = "${NOMAD_IP}:4647"
}
log_level = "INFO"
enable_debug = false
EOF

echo "Nomad: Config Server"
cat << EOF > /etc/nomad.d/server.hcl
server
{
  enabled = true
  bootstrap_expect = 1
}
EOF

if [[ ${MAJOR_VERSION} -gt 6 ]]; then
echo "Nomad version $NOMAD_VERSION supports acls"
echo "Nomad: Config ACL"
cat << EOF > /etc/nomad.d/acl.hcl
acl
{
  enabled = true
  token_ttl = "30s"
  policy_ttl = "60s"
}
EOF
else
  echo "Nomad: version $NOMAD_VERSION"
fi

echo "Nomad: Create test job samples"
/usr/bin/nomad init
/usr/bin/nomad run -output example.nomad > example.json
if [[ ${MAJOR_VERSION} -gt 7 ]]; then
  cp example.nomad vault.hcl
  sed -i s/"# vault {"/"vault { policies = [\"policy-demo\"]}"/g vault.hcl
  sed -i s/"job \"example\" {"/"job \"vault\" {"/g vault.hcl
  /usr/bin/nomad run -output vault.hcl > vault.json
fi


echo "Starting Nomad"
nohup nomad agent -server -dev -config=/etc/nomad.d > /dev/null 2>&1 &
sleep 30

echo "You can execute your test! ENJOY!"
