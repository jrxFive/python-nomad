import os

# use vagrant IP if env variable is not specified, generally for local testing
URI = os.environ.get("NOMAD_URL", "http://192.168.33.10")

# internal ip of docker
IP = os.environ.get("NOMAD_IP", "192.168.33.10")

# Security token
NOMAD_VERSION = os.environ.get("NOMAD_VERSION", "0.7.1")

# use vagrant PORT if env variable is not specified, generally for local
# testing
NOMAD_PORT = os.environ.get("NOMAD_PORT", 4646)

# Security token
NOMAD_TOKEN = os.environ.get("NOMAD_TOKEN", "")
