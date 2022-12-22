## Steps for Contributing:

### Adding a new endpoint

#### nomad/__init__.py
```python 
# Instantiate a new object and make it an attribute

    self._jobs = api.Jobs(**self.requester_settings)
    self._job = api.Job(**self.requester_settings)
    self._nodes = api.Nodes(**self.requester_settings)
    self._node = api.Node(**self.requester_settings)
    self._allocations = api.Allocations(**self.requester_settings)
    self._allocation = api.Allocation(**self.requester_settings)
    self._evaluations = api.Evaluations(**self.requester_settings)
    self._evaluation = api.Evaluation(**self.requester_settings)
    self._agent = api.Agent(**self.requester_settings)
    self._client = api.Client(**self.requester_settings)
    self._deployments = api.Deployments(**self.requester_settings)
    self._deployment = api.Deployment(**self.requester_settings)
    self._regions = api.Regions(**self.requester_settings)
    self._status = api.Status(**self.requester_settings)
    self._system = api.System(**self.requester_settings)
    self._operator = api.Operator(**self.requester_settings)
    self._validate = api.Validate(**self.requester_settings)
    self._namespaces = api.Namespaces(**self.requester_settings)
    self._namespace = api.Namespace(**self.requester_settings)
    self._acl = api.Acl(**self.requester_settings)
    self._sentinel = api.Sentinel(**self.requester_settings)
    self._metrics = api.Metrics(**self.requester_settings)
    self._<endpoint> = api.<Endpoint>(**self.requester_settings)
```

#### nomad/__init__.py
```python
# Add a new property to the class

    @property
    def jobs(self):
        return self._jobs
    
    @property
    def job(self):
        return self._job
    
    @property
    def nodes(self):
        return self._nodes
    
    @property
    def node(self):
        return self._node
    
    @property
    def allocations(self):
        return self._allocations
    
    @property
    def allocation(self):
        return self._allocation
    
    @property
    def evaluations(self):
        return self._evaluations
    
    @property
    def evaluation(self):
        return self._evaluation
    
    @property
    def agent(self):
        return self._agent
    
    @property
    def client(self):
        return self._client
    
    @property
    def deployments(self):
        return self._deployments
    
    @property
    def deployment(self):
        return self._deployment
    
    @property
    def regions(self):
        return self._regions
    
    @property
    def status(self):
        return self._status
    
    @property
    def system(self):
        return self._system
    
    @property
    def operator(self):
        return self._operator
    
    @property
    def validate(self):
        return self._validate
    
    @property
    def namespaces(self):
        return self._namespaces
    
    @property
    def namespace(self):
        return self._namespace
    
    @property
    def acl(self):
        return self._acl
    
    @property
    def sentinel(self):
        return self._sentinel
    
    @property
    def metrics(self):
        return self._metrics
        
    @property
    def <endpoint>(self):
        return self._<endpoint>
```

#### nomad/api/__init__.py
```python
# Add import of new endpoint

import nomad.api.exceptions
from nomad.api.base import Requester
from nomad.api.jobs import Jobs
from nomad.api.job import Job
from nomad.api.nodes import Nodes
from nomad.api.node import Node
from nomad.api.agent import Agent
from nomad.api.allocations import Allocations
from nomad.api.allocation import Allocation
from nomad.api.evaluations import Evaluations
from nomad.api.evaluation import Evaluation
from nomad.api.client import Client
from nomad.api.regions import Regions
from nomad.api.status import Status
from nomad.api.system import System
from nomad.api.operator import Operator
from nomad.api.validate import Validate
from nomad.api.deployments import Deployments
from nomad.api.deployment import Deployment
from nomad.api.namespaces import Namespaces
from nomad.api.namespace import Namespace
from nomad.api.acl import Acl
from nomad.api.sentinel import Sentinel
from nomad.api.metrics import Metrics
from nomad.api.<endpoint> import <Endpoint>
```

#### nomad/api/endpoint.py

##### Class

The Endpoint class inherits from Requester. To specify how the requests are constructed each Endpoint must have a class
variable `ENDPOINT` declared, when creating a request to an entity this class variable will be use in the construction
of the route.


```python
from nomad.api.base import Requester


class <Endpoint>(Requester):

    """
    https://www.nomadproject.io/docs/http/<endpoint>.html
    """
    ENDPOINT = "<endpoint>" 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
```

##### Entity

Adding an Entity will call the request method that is inherited from the Requester class. Arguments passed are added
as part of the route:

```python
self.request("something","further")
>>> ENDPOINT/something/further
```

Querystring parameters are passed as an dictionary the `params` keyword argument
Payloads are passed as an dictionary the `json` keyword argument
The HTTP method (get, post, put, delete) is specified as the `method` keyword argument

All requests will return a `requests.Response` object unless the request failed an can potentially raise
- BaseNomadException (status code 500)
- URLNotFoundNomadException (status code 404)
- URLNotAuthorizedNomadException (status code 403)
- BadRequestNomadException (status code 400)

Depending on the Nomad HTTP API documentation, either return the `.json()` or `text` of the `requests.Response` object.

```python
    def get_jobs(self):
        """ Lists all the jobs registered with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
```

```python
    def parse(self, hcl, canonicalize=False):
        """ Parse a HCL Job file. Returns a dict with the JSON formatted job.
            This API endpoint is only supported from Nomad version 0.8.3.

            https://www.nomadproject.io/api/jobs.html#parse-job

            returns: dict
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request("parse", json={"JobHCL": hcl, "Canonicalize": canonicalize}, method="post", allow_redirects=True).json()
```

```python
class cat(Requester):

    """
    The /fs/cat endpoint is used to read the contents of a file in an
    allocation directory. This API endpoint is hosted by the Nomad
    client and requests have to be made to the Nomad client where the
    particular allocation was placed.

    https://www.nomadproject.io/docs/http/client-fs-cat.html
    """

    ENDPOINT = "client/fs/cat"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def read_file(self, id=None, path="/"):
        """ Read contents of a file in an allocation directory.

           https://www.nomadproject.io/docs/http/client-fs-cat.html

            arguments:
              - id
              - path
            returns: (str) text
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        if id:
            return self.request(id, params={"path": path}, method="get").text
        else:
            return self.request(params={"path": path}, method="get").text
```

##### Contains

Contains should check if the key exists, if so return True otherwise False. The library will also raise `URLNotFoundNomadException`
if the said endpoint could not be found, this should also return False.

```python
"something" in n.endpoint
```

```python
    def __contains__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return True
                if j["Name"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False
```

##### Length

Length returns the len of the entity iterable

```python
len(n.endpoint)
```

```python
    def __len__(self):
        jobs = self.get_jobs()
        return len(jobs)
```

##### Get

Get will obtain the specified entity/item. If it is found return the item otherwise raise `KeyError`. The library will also raise
`URLNotFoundNomadException` if the said endpoint could not be found, this should also raise `KeyError`.

```python
n.endpoint["something"]
```

```python
    def __getitem__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return j
                if j["Name"] == item:
                    return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError
```

##### Iterate

Iterate will allow obtained items to be used as an iterable.

```python
for i in n.endpoint:
    # do something
```

```python
    def __iter__(self):
        jobs = self.get_jobs()
        return iter(jobs)
```

##### Delete

Delete should perform a DELETE operation to the Nomad API. Generally plurals (jobs, allocations...) will not have this functionality.
The request could fail and should properly pass whichever exception was raised.

```python
del n.endpoint["something"]
```

```python
def __delitem__(self, item):
    self.deregister_job(item)
```


#### Full Example

```python
from nomad.api.base import Requester


class <Endpoint>(Requester):

    """
    The jobs endpoint is used to query the status of existing
    jobs in Nomad and to register new jobs.
    By default, the agent's local region is used.

    https://www.nomadproject.io/docs/http/jobs.html
    """
    ENDPOINT = "<endpoint>" 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        msg = "{0} does not exist".format(item)
        raise AttributeError(msg)

    def __contains__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return True
                if j["Name"] == item:
                    return True
            else:
                return False
        except nomad.api.exceptions.URLNotFoundNomadException:
            return False

    def __len__(self):
        jobs = self.get_jobs()
        return len(jobs)

    def __getitem__(self, item):
        try:
            jobs = self.get_jobs()

            for j in jobs:
                if j["ID"] == item:
                    return j
                if j["Name"] == item:
                    return j
            else:
                raise KeyError
        except nomad.api.exceptions.URLNotFoundNomadException:
            raise KeyError

    def __iter__(self):
        jobs = self.get_jobs()
        return iter(jobs)

    def get_jobs(self):
        """ Lists all the jobs registered with Nomad.

           https://www.nomadproject.io/docs/http/jobs.html

            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        return self.request(method="get").json()
```

### Adding tests for a new endpoint

Create a new python file in `tests/test_endpoint.py`. If the tests expect to interact require a job, allocation, evaluation
add the test_register_job at the beginning of the file.

A nomad client library instance is available by add `nomad_setup` as a parameter to the test function (`tests/conftest.py`).

```python
import pytest
import json
import uuid


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job
```

Tests should be written for all endpoints, and test various success and failure modes if possible.

```python
def test_get_allocation(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert isinstance(nomad_setup.allocation.get_allocation(id), dict) == True


def test_dunder_getitem_exist(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    a = nomad_setup.allocation[id]
    assert isinstance(a, dict)


def test_dunder_getitem_not_exist(nomad_setup):

    with pytest.raises(KeyError):  # restucture try/except/raises
        j = nomad_setup.allocation[str(uuid.uuid4())]


def test_dunder_contain_exists(nomad_setup):
    id = nomad_setup.job.get_allocations("example")[0]["ID"]
    assert id in nomad_setup.allocation


def test_dunder_contain_not_exist(nomad_setup):

    assert str(uuid.uuid4()) not in nomad_setup.allocation


def test_dunder_str(nomad_setup):
    assert isinstance(str(nomad_setup.allocation), str)


def test_dunder_repr(nomad_setup):
    assert isinstance(repr(nomad_setup.allocation), str)


def test_dunder_getattr(nomad_setup):

    with pytest.raises(AttributeError):
        d = nomad_setup.allocation.does_not_exist
```


Enterprise endpoints (namespace, namespaces, sentinel...) can be mock the expected responses

```python
import tests.common as common

import pytest
import responses


# integration tests was mocked. If you have an enterprise nomad please uncomenet ##### ENTERPRISE TEST #####
@responses.activate
def test_get_namespaces(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespaces".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
                {
                    "CreateIndex": 31,
                    "Description": "Production API Servers",
                    "ModifyIndex": 31,
                    "Name": "api-prod"
                },
                {
                    "CreateIndex": 5,
                    "Description": "Default shared namespace",
                    "ModifyIndex": 5,
                    "Name": "default"
                }
            ]
    )

    assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True
```