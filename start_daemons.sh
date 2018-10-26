echo "Start daemons to test"

if [ -z "${NOMAD_VERSION}" ]; then
  echo "you should export NOMAD_VERSION"
  exit 1
fi

if [ -z "${NOMAD_PORT_GUEST}" ]; then
  NOMAD_PORT_GUEST="4646"
fi

if [ -z "${NOMAD_IP}" ]; then
  NOMAD_IP=127.0.0.1
fi

if [ -z "${VAULT_VERSION}" ]; then
  VAULT_VERSION="0.6.2"
fi

VAULT_ADDR="http://localhost:8200"

MAJOR_VERSION=`echo ${NOMAD_VERSION} | cut -d "." -f 2`
MAJOR_VERSION_VAULT_INTEGRATION=`echo ${NOMAD_VERSION} | tr -d "."|sed "s/^0*//"`
NOMAD_REQUIRED_TO_INEGRATE_WITH_VAULT=`echo ${NOMAD_INTEGRATION_VAULT}|tr -d "."|sed "s/^0*//"`

echo "Nomad: Create config folder"
rm -rf /tmp/nomad.d
mkdir -p /tmp/nomad.d

if [ "${VAULT_TEST}" = "true" ]; then
if [ ${MAJOR_VERSION_VAULT_INTEGRATION} -gt ${NOMAD_REQUIRED_TO_INEGRATE_WITH_VAULT} ]; then
  echo "Vault: Create policy file"
cat << EOF > /tmp/policy-demo.hcl
path "secret/demo" {
  capabilities = ["read"]
}
EOF

  echo "Vault: Start Daemon Version: ${VAULT_VERSION}"
  /tmp/vault server -dev -dev-listen-address=0.0.0.0:8200 -dev-root-token-id="root" > /dev/null 2>&1 &
  sleep 5

  echo "Vault: Write Vault Policies with API"
  curl -s --data '{"rules":"path \"secret/demo\" {capabilities = [\"read\",\"list\"]}"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/sys/policy/policy-demo

  echo "Vault: Write Vault Secret"
  curl -s --data '{"value":"python_nomad"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/secret/demo

  echo "Nomad: Enable Config Vault"
cat << EOF > /tmp/nomad.d/vault.hcl
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
cat << EOF > /tmp/nomad.d/base_config.hcl
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
cat << EOF > /tmp/nomad.d/server.hcl
server
{
  enabled = true
  bootstrap_expect = 1
}
EOF

if [ ${MAJOR_VERSION} -gt 6 ]; then
echo "Nomad: Version $NOMAD_VERSION supports acls"
echo "Nomad: Config ACL"
cat << EOF > /tmp/nomad.d/acl.hcl
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
/tmp/nomad init
/tmp/nomad run -output example.nomad > example.json
chmod 777 example*

echo "Nomad: Starting Nomad"
nohup /tmp/nomad agent -server -dev -config=/tmp/nomad.d > /dev/null 2>&1 &


PID=`ps -eaf | grep "vault server -dev" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "VAULT: service is RUNNING"
else
  echo "VAULT: service is STOPED (could be not necessary)"
fi

PID=`ps -eaf | grep "nomad agent -server" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "NOMAD: service is RUNNING"
else
  echo "NOMAD: service is STOPED"
fi
sleep 30
