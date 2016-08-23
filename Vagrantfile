# -*- mode: ruby -*-
# vi: set ft=ruby :

IP = "192.168.33.10"
NOMAD_VERSION = "0.4.1"
NOMAD_PORT_GUEST = 4646
NOMAD_PORT_HOST = 4646

Vagrant.configure(2) do |config|

config.vm.box = "centos/7"

config.vm.network "forwarded_port", guest: NOMAD_PORT_GUEST, host: NOMAD_PORT_HOST

config.vm.network "private_network", ip: "#{IP}"

config.vm.provider "virtualbox" do |vb|
vb.name = "python-nomad"
vb.gui = false
vb.memory = "1024"
end

config.vm.provision "shell", inline: <<-SHELL

if [ ! -e /etc/yum.repos.d/docker.repo ]
  then
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

wget -q -P /tmp/ https://releases.hashicorp.com/nomad/#{NOMAD_VERSION}/nomad_#{NOMAD_VERSION}_linux_amd64.zip
yes | unzip -d /tmp /tmp/nomad_#{NOMAD_VERSION}_linux_amd64.zip

if [ ! -f /usr/bin/nomad ]
  then
    cp /tmp/nomad /usr/bin/.
fi

if [ $(pgrep nomad) ]
  then
    echo "Nomad running"
  else
    echo "Starting Nomad"
    nohup nomad agent -dev -bind #{IP} -node pynomad1 > /dev/null 2>&1 &
    sleep 30
fi

SHELL

end
