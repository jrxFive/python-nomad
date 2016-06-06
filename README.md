#python-nomad


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

n = nomad.Nomad("172.16.100.10",timeout=5)

"example" in n.jobs

j = n.jobs["example"]["ID"]

example_allocation = n.allocation.get_allocations(j)

n.job.deregister_job(j)
```

## Development
* create virtualenv and activate
* install requirements-dev.txt
* can either use the Vagrantfile for local integration testing or create environment variables `NOMAD_IP` and `NOMAD_PORT` that are assigned to a nomad binary that is running

## TODO
* examples
* functional tests
* Inherit Base class, remove duplication and override parent dunders
* readthedocs
