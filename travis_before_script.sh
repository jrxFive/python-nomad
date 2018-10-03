#!/bin/bash

echo "Download Nomad Version ${NOMAD_VERSION}"
curl -L -o /tmp/nomad_${NOMAD_VERSION}_linux_amd64.zip https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip

echo "Download Vault Version ${VAULT_VERSION}"
curl -L -o /tmp/vault_${VAULT_VERSION}_linux_amd64.zip https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip

echo "Unzip nomad file"
unzip -d /tmp /tmp/nomad_${NOMAD_VERSION}_linux_amd64.zip

echo "Unzip Vault file"
unzip -d /tmp /tmp/vault_${VAULT_VERSION}_linux_amd64.zip

echo "Copy binary"
if [ ! -f /usr/bin/nomad ]
then
    cp /tmp/nomad /usr/bin/.
fi

if [ ! -f /usr/bin/vault ]
then
    cp /tmp/vault /usr/bin/.
fi

echo "Nomad: Create test job samples"
/usr/bin/nomad init
/usr/bin/nomad run -output example.nomad > example.json
cp example.nomad vault.hcl
sed -i s/"# vault {"/"vault { policies = [\"policy-demo\"]}"/g vault.hcl
sed -i s/"job \"example\" {"/"job \"vault\" {"/g vault.hcl
/usr/bin/nomad run -output vault.hcl > vault.json

echo "Nomad: Create config folder"
mkdir -p /etc/nomad.d

MAJOR_VERSION=`echo ${NOMAD_VERSION} | cut -d "." -f 2`
if [[ ${MAJOR_VERSION} -gt 6 ]]; then
  "Nomad version $NOMAD_VERSION supports acls"
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
  echo "Nomad version $NOMAD_VERSION"
fi

if [[ ${MAJOR_VERSION} -gt 7 ]]; then
  echo "Vault: Create policy test file"
cat << EOF > /tmp/policy-demo.hcl
path "secret/demo" {
    capabilities = ["read"]
  }
EOF
  echo "Nomad: Config Vault"
cat << EOF > /etc/nomad.d/vault.hcl
vault
{
  enabled     = true
  address     = "${VAULT_ADDR}"
  token = "root"
  allow_unauthenticated = false
}
EOF
  echo "Vault: Start Daemon"
  /tmp/vault server -dev -dev-listen-address=0.0.0.0:8200 -dev-root-token-id="root" > /dev/null 2>&1 &
  sleep 5

  echo "Vault: Write Vault Policies"
  VAULT_TOKEN=root vault policy-write -address=http://127.0.0.1:8200 policy-demo /tmp/policy-demo.hcl
  echo "Vault: Write Vault Secret"
  VAULT_TOKEN=root vault write -address=http://127.0.0.1:8200 secret/demo data=python_nomad

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
  http = "${NOMAD_PORT}"
}
addresses
{
  http = "${NOMAD_IP}"
  rpc = "${NOMAD_IP}"
}
advertise
{
  http = "${NOMAD_IP}"
  rpc = "${NOMAD_IP}"
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


nohup nomad agent -server -dev -config=/etc/nomad.d > /dev/null 2>&1 &

sleep 30
