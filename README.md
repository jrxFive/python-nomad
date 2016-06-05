#python-nomad


Branch | Status | Coverage |
---| ---| --- 
master | [![Build Status](https://travis-ci.org/jrxFive/python-nomad.svg?branch=master)](https://travis-ci.org/jrxFive/python-nomad) | [![codecov](https://codecov.io/gh/jrxFive/python-nomad/branch/master/graph/badge.svg)](https://codecov.io/gh/jrxFive/python-nomad)


## Installation
```
pip install python-nomad
```

## Examples
```python

n = nomad.Nomad("172.16.100.10",timeout=5)

"example" in n.jobs

j = n.jobs["example"]["ID"]

example_allocation = n.allocation.get_allocations(j)

n.job.deregister_job(j)
```

## TODO
* functional tests
* Inherit Base class, remove duplication and override parent dunders
* readthedocs
