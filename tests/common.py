import os

# use vagrant IP if env variable is not specified, generally for local testing
IP = os.environ.get("NOMAD_IP","192.168.33.10")

# use vagrant PORT if env variable is not specified, generally for local testing
NOMAD_PORT = os.environ.get("NOMAD_PORT",4646)