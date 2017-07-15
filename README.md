# python-nomad


Branch | Status | Coverage |
---| ---| ---
develop | [![Build Status](https://travis-ci.org/jrxFive/python-nomad.svg?branch=develop)](https://travis-ci.org/jrxFive/python-nomad) | [![codecov](https://codecov.io/gh/jrxFive/python-nomad/branch/develop/graph/badge.svg)](https://codecov.io/gh/jrxFive/python-nomad)


## Installation
```
pip install python-nomad
```

## Examples
```python

import nomad

# For HTTP Nomad instances
n = nomad.Nomad("172.16.100.10",timeout=5)

# For HTTPS Nomad instances with non-self-signed SSL certificates
n = nomad.Nomad("172.16.100.10",timeout=5,verify=True)

# For HTTPS Nomad instances with self-signed SSL certificates
n = nomad.Nomad("172.16.100.10",timeout=5,verify="/path/to/certfile") # See http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

"example" in n.jobs

j = n.jobs["example"]["ID"]

example_allocation = n.job.get_allocations(j)

n.job.deregister_job(j)
```

## Class Dunders
| Class | contains | len | getitem | iter |
|---|---|---|---|---|
agent| N|N|N|N
allocation|Y|N|Y|N
allocations|N|Y|N|Y
client|N|N|N|N
evaluation|Y|N|Y|N
evaluations|Y|Y|Y|Y
job|Y|N|Y|N
jobs|Y|Y|Y|Y
node|Y|N|Y|N
nodes|Y|Y|Y|Y
regions|Y|Y|Y|Y
status.leader|Y|Y|N|N
status.peers|Y|Y|Y|Y
system|N|N|N|N

## Development
* create virtualenv and activate
* install requirements-dev.txt
* can either use the Vagrantfile for local integration testing or create environment variables `NOMAD_IP` and `NOMAD_PORT` that are assigned to a nomad binary that is running

```
virutalenv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

## Testing with vagrant and virtualbox
```
vagrant up --provider virtualbox
py.test --cov=nomad --cov-report=term-missing --runxfail tests/
```



## TODO
- [ ] examples
- [ ] functional tests
- [ ] Inherit Base class, remove duplication and override parent dunders
- [ ] readthedocs
