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

NOMAD_MAJOR_VERSION=`echo ${NOMAD_VERSION} | tr -d "."|sed "s/^0*//"`
VAULT_MAJOR_VERSION=`echo ${VAULT_VERSION} | tr -d "."|sed "s/^0*//"`

if [ ${VAULT_MAJOR_VERSION} -lt 62 ]; then
  echo "ATTENTION: Nomad Vault integration require Vault version >= 0.6.2. See https://www.nomadproject.io/guides/operations/vault-integration/index.html"
fi

if [ ! -f /tmp/nomad ]; then
  rm -rf /tmp/nomad
fi
echo "Nomad: Get Binary Files"
wget -q -P /tmp/ https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
yes | unzip -o -d /tmp /tmp/nomad_${NOMAD_VERSION}_linux_amd64.zip


if [ ! -f /tmp/vault ]; then
  rm -rf /tmp/vault
fi
echo "Vault: Get Binary Files"
wget -q -P /tmp/ https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
yes | unzip -o -d /tmp /tmp/vault_${VAULT_VERSION}_linux_amd64.zip


VAULT_ADDR="http://localhost:8200"


echo "Nomad: Create config folder"
rm -rf /tmp/nomad.d
mkdir -p /tmp/nomad.d


if [ ${VAULT_MAJOR_VERSION} -lt 62  ]; then
  echo "Vault: this version is not supported"
else
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
    #
    # For version > 0.9.0 deprecated use of policies. Rules vs Policy
    #
    if [ ${VAULT_MAJOR_VERSION} -lt 90 ]; then
      curl -s --data '{"rules":"path \"secret/demo\" {capabilities = [\"read\",\"list\"]}"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/sys/policy/policy-demo
    else
        curl -s --data '{"policy":"path \"secret/data/demo\" {capabilities = [\"read\",\"list\"]}"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/sys/policy/policy-demo
    fi

    echo "Vault: Write Vault Secret"
    #
    # Vault version >= 0.9.0 require versioned secrets
    #
    if [ ${VAULT_MAJOR_VERSION} -lt 90 ]; then
      curl -s --data '{"value":"python_nomad"}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/secret/demo
    else
      curl -s --data '{"options": {"cas": 0},"data": {"value": "python_nomad"}}' --request PUT --header "X-Vault-Token: root" ${VAULT_ADDR}/v1/secret/data/demo
    fi


fi




if [ ${NOMAD_MAJOR_VERSION} -ge 50  ]; then
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

if [ ${NOMAD_MAJOR_VERSION} -gt 60 ]; then
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
rm -rf example.nomad
rm -rf example.json
/tmp/nomad init
/tmp/nomad run -output example.nomad > example.json
chmod 777 example*

echo "Nomad: Starting Nomad"
nohup /tmp/nomad agent -server -dev -config=/tmp/nomad.d > /dev/null 2>&1 &


PID=`ps -eaf | grep "vault server -dev" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "Vault: service is Running"
else
  echo "Vault: service is Stoped (could be not necessary)"
fi

PID=`ps -eaf | grep "nomad agent -server" | grep -v grep | awk '{print $2}'`
if [ "" !=  "$PID" ]; then
  echo "Nomad: service is Running"
else
  echo "Nomad: service is Stoped. This make problems to make test!"
fi
sleep 10

echo "You can execute your test! ENJOY!"
