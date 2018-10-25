# -*- mode: ruby -*-
# vi: set ft=ruby :

NOMAD_IP="192.168.33.10"
NOMAD_VERSION="0.8.6"
NOMAD_PORT_GUEST=4646
NOMAD_PORT_HOST=4646
VAULT_VERSION="0.9.0"
VAULT_PORT_GUEST=8200
VAULT_PORT_HOST=8200
VAULT_ADDR="http://127.0.0.1:8200"
VAULT_TEST="true"
NOMAD_INTEGRATION_VAULT="0.6.2"


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

echo "pip for test inside the vagrant"
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install -r /vagrant/requirements-dev.txt

cat << EOF > /tmp/environment.vars.sh
export NOMAD_IP="#{NOMAD_IP}"
export NOMAD_VERSION="#{NOMAD_VERSION}"
export NOMAD_PORT_GUEST="#{NOMAD_PORT_GUEST}"
export NOMAD_PORT_HOST="#{NOMAD_PORT_HOST}"
export VAULT_VERSION="#{VAULT_VERSION}"
export VAULT_ADDR="#{VAULT_ADDR}"
export VAULT_TEST="#{VAULT_TEST}"
export NOMAD_INTEGRATION_VAULT="#{NOMAD_INTEGRATION_VAULT}"
EOF
chmod +x /tmp/environment.vars.sh
source /tmp/environment.vars.sh
cd /vagrant
./travis_before_script.sh

SHELL

end
