import os

# internal ip of docker
IP = os.environ.get("NOMAD_IP", "192.168.33.10")

# use vagrant PORT if env variable is not specified, generally for local
# testing
NOMAD_PORT = os.environ.get("NOMAD_PORT", 4646)

# Security token
NOMAD_TOKEN = os.environ.get("NOMAD_TOKEN", None)

# Test namespace
NOMAD_NAMESPACE = "admin"
