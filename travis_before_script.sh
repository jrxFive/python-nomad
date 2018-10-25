
BASEDIR=$(dirname "$0")

if [ -z "${NOMAD_VERSION}" ]; then
  echo "you should export NOMAD_VERSION"
  exit 1
fi

if [ -z "${NOMAD_IP}" ]; then
  NOMAD_IP=127.0.0.1
fi

if [ -z "${VAULT_VERSION}" ]; then
  VAULT_VERSION="0.6.2"
fi

echo "NOMAD: Get Binary Files"
wget -q -P /tmp/ https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/nomad_${NOMAD_VERSION}_linux_amd64.zip

echo "VAULT: Get Binary Files"
wget -q -P /tmp/ https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/vault_${VAULT_VERSION}_linux_amd64.zip


$BASEDIR/start_daemons.sh

echo "You can execute your test! ENJOY!"
