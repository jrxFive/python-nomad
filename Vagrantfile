# -*- mode: ruby -*-
# vi: set ft=ruby :

NOMAD_IP="192.168.33.10"
NOMAD_VERSION="0.3.2"
NOMAD_PORT_GUEST=4646
NOMAD_PORT_HOST=4646
VAULT_VERSION="0.9.0"
VAULT_PORT_GUEST=8200
VAULT_PORT_HOST=8200
VAULT_ADDR="http://127.0.0.1:8200"


Vagrant.configure(2) do |config|

config.vm.box = "centos/7"

config.vm.network "forwarded_port", guest: NOMAD_PORT_GUEST, host: NOMAD_PORT_HOST
config.vm.network "forwarded_port", guest: VAULT_PORT_GUEST, host: VAULT_PORT_HOST

config.vm.network "private_network", ip: "#{NOMAD_IP}"

config.vm.provider "virtualbox" do |vb|
vb.name = "python-nomad"
vb.gui = false
vb.memory = "1024"
end

config.vm.provision "shell", inline: <<-SHELL

if [ ! -e /etc/yum.repos.d/docker.repo ]; then
tee /etc/yum.repos.d/docker.repo <<-EOF
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF
fi

yum -y install docker-engine unzip wget net-tools
usermod -aG docker vagrant
systemctl enable docker; systemctl start docker

echo "Download binary files"
wget -q -P /tmp/ https://releases.hashicorp.com/nomad/#{NOMAD_VERSION}/nomad_#{NOMAD_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/nomad_#{NOMAD_VERSION}_linux_amd64.zip

wget -q -P /tmp/ https://releases.hashicorp.com/vault/#{VAULT_VERSION}/vault_#{VAULT_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/vault_#{VAULT_VERSION}_linux_amd64.zip

echo "Copy binary"
if [ ! -f /usr/bin/nomad ]
then
    cp /tmp/nomad /usr/bin/.
fi

if [ ! -f /usr/bin/vault ]
then
    cp /tmp/vault /usr/bin/.
fi

MAJOR_VERSION=`echo #{NOMAD_VERSION} | cut -d "." -f 2`

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
  address     = "#{VAULT_ADDR}"
  token = "root"
  allow_unauthenticated = false
}
EOF
fi

echo "Nomad: Config base"
cat << EOF > /etc/nomad.d/base_config.hcl
datacenter = "dc1"
name = "pynomad1"
bind_addr = "#{NOMAD_IP}"
client
{
    enabled = true
    node_class = "default"
}
ports
{
  http = #{NOMAD_PORT_GUEST}
  rpc  = 4647
}
addresses
{
  http = "#{NOMAD_IP}"
  rpc = "#{NOMAD_IP}"
}
advertise
{
  http = "#{NOMAD_IP}:#{NOMAD_PORT_GUEST}"
  rpc = "#{NOMAD_IP}:4647"
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
  "Nomad: version #{NOMAD_VERSION} supports acls"
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
  echo "Nomad: version #{NOMAD_VERSION}"
fi

echo "Starting Nomad"
nohup nomad agent -server -dev -config=/etc/nomad.d > /dev/null 2>&1 &
sleep 30


echo "You can execute your test!"

SHELL

end
