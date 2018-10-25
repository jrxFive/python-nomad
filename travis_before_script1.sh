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
MAJOR_VERSION_VAULT_INTEGRATION=`echo ${NOMAD_VERSION} | tr -d "."|sed "s/^0*//"`
NOMAD_REQUIRED_TO_INEGRATE_WITH_VAULT=`echo ${NOMAD_INTEGRATION_VAULT}|tr -d "."|sed "s/^0*//"`

echo "Nomad: Create config folder"
mkdir -p /etc/nomad.d

if [[ "${VAULT_TEST}" == "true" ]]; then
if [[ ${MAJOR_VERSION_VAULT_INTEGRATION} -gt ${NOMAD_REQUIRED_TO_INEGRATE_WITH_VAULT} ]]; then
  echo "Vault: Create policy file"
cat << EOF > /tmp/policy-demo.hcl
path "secret/demo" {
  capabilities = ["read"]
}
EOF

  echo "Vault: Start Daemon"
  /usr/bin/vault server -dev -dev-listen-address=0.0.0.0:8200 -dev-root-token-id="root" > /var/log/vault.log 2>&1 &
  sleep 5

  echo "Vault: Write Vault Policies with API"
  if [[ ${MAJOR_VERSION_VAULT_INTEGRATION} -gt 8 ]]; then
    curl -s --data '{"policy":"path \"secret\/demo\" {capabilities = [\"read\"]}"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/sys/policy/policy-demo
  else
    curl -s --data '{"rules":"path \"secret\/demo\" {capabilities = [\"read\"]}"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/sys/policy/policy-demo
  fi

  echo "Vault: Write Vault Secret"
  curl -s --data '{"value":"python_nomad"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/secret/demo

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
  http = ${NOMAD_PORT_GUEST}
  rpc  = 4647
}
addresses
{
  http = "${NOMAD_IP}"
  rpc = "${NOMAD_IP}"
}
advertise
{
  http = "${NOMAD_IP}:${NOMAD_PORT_GUEST}"
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
echo "Nomad: Version $NOMAD_VERSION supports acls"
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
if [[ ${MAJOR_VERSION} -ge 8 ]]; then
  cp example.nomad vault.hcl
  sed -i s/"# vault {"/"vault { policies = [\"policy-demo\"]}"/g vault.hcl
  sed -i s/"job \"example\" {"/"job \"vault\" {"/g vault.hcl
  /usr/bin/nomad run -output vault.hcl > vault.json
fi
chmod 777 example* vault.*

echo "Starting Nomad"
nohup /usr/bin/nomad agent -server -dev -config=/etc/nomad.d > /dev/null 2>&1 &
sleep 30

echo "You can execute your test! ENJOY!"
