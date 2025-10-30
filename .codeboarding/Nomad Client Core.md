```mermaid
graph LR
    Nomad_Client_Core["Nomad Client Core"]
    Nomad_API_Endpoints["Nomad API Endpoints"]
    Nomad_Client_Core -- "initializes and provides access to" --> Nomad_API_Endpoints
```
[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Component Details

This graph illustrates the core components of the python-nomad library, focusing on the central `Nomad Client Core` which serves as the entry point for interacting with the Nomad cluster. It details how the client initializes connections and provides access to various `Nomad API Endpoints`, each responsible for managing specific Nomad resources. The primary flow involves the client initializing and then utilizing these API endpoint modules to perform operations on the Nomad cluster.

### Nomad Client Core
The primary entry point for the python-nomad library, responsible for initializing the connection to the Nomad cluster and providing access to all other API-specific client modules. It acts as the central interface for users to interact with the Nomad cluster.


**Related Classes/Methods**:

- `nomad.Nomad` (full file reference)
- `nomad.Nomad:__init__` (30:60)
- `nomad.Nomad.get_uri` (62:65)


### Nomad API Endpoints
This component encompasses a collection of modules, each dedicated to managing a specific resource or functionality within the Nomad API, such as ACLs, agents, allocations, jobs, and nodes. These modules are instantiated by the Nomad Client to facilitate interactions with the respective Nomad services, often inheriting from a common `Requester` base class for API communication.


**Related Classes/Methods**:

- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/acl.py#L6-L194" target="_blank" rel="noopener noreferrer">`nomad.api.acl.Acl` (6:194)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/agent.py#L6-L98" target="_blank" rel="noopener noreferrer">`nomad.api.agent.Agent` (6:98)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/allocation.py#L8-L73" target="_blank" rel="noopener noreferrer">`nomad.api.allocation.Allocation` (8:73)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/allocations.py#L8-L83" target="_blank" rel="noopener noreferrer">`nomad.api.allocations.Allocations` (8:83)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/client.py#L7-L32" target="_blank" rel="noopener noreferrer">`nomad.api.client.Client` (7:32)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/deployment.py#L8-L172" target="_blank" rel="noopener noreferrer">`nomad.api.deployment.Deployment` (8:172)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/deployments.py#L8-L78" target="_blank" rel="noopener noreferrer">`nomad.api.deployments.Deployments` (8:78)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/evaluation.py#L8-L74" target="_blank" rel="noopener noreferrer">`nomad.api.evaluation.Evaluation` (8:74)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/evaluations.py#L8-L75" target="_blank" rel="noopener noreferrer">`nomad.api.evaluations.Evaluations` (8:75)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/event.py#L12-L27" target="_blank" rel="noopener noreferrer">`nomad.api.event.Event` (12:27)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/job.py#L9-L363" target="_blank" rel="noopener noreferrer">`nomad.api.job.Job` (9:363)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/jobs.py#L9-L127" target="_blank" rel="noopener noreferrer">`nomad.api.jobs.Jobs` (9:127)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/metrics.py#L6-L42" target="_blank" rel="noopener noreferrer">`nomad.api.metrics.Metrics` (6:42)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/namespace.py#L8-L107" target="_blank" rel="noopener noreferrer">`nomad.api.namespace.Namespace` (8:107)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/namespaces.py#L8-L75" target="_blank" rel="noopener noreferrer">`nomad.api.namespaces.Namespaces` (8:75)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/node.py#L9-L193" target="_blank" rel="noopener noreferrer">`nomad.api.node.Node` (9:193)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/nodes.py#L10-L95" target="_blank" rel="noopener noreferrer">`nomad.api.nodes.Nodes` (10:95)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/operator.py#L6-L64" target="_blank" rel="noopener noreferrer">`nomad.api.operator.Operator` (6:64)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/regions.py#L8-L68" target="_blank" rel="noopener noreferrer">`nomad.api.regions.Regions` (8:68)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/scaling.py#L8-L74" target="_blank" rel="noopener noreferrer">`nomad.api.scaling.Scaling` (8:74)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/search.py#L8-L98" target="_blank" rel="noopener noreferrer">`nomad.api.search.Search` (8:98)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/sentinel.py#L6-L98" target="_blank" rel="noopener noreferrer">`nomad.api.sentinel.Sentinel` (6:98)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/status.py#L8-L27" target="_blank" rel="noopener noreferrer">`nomad.api.status.Status` (8:27)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/system.py#L6-L52" target="_blank" rel="noopener noreferrer">`nomad.api.system.System` (6:52)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/validate.py#L6-L44" target="_blank" rel="noopener noreferrer">`nomad.api.validate.Validate` (6:44)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/variable.py#L8-L111" target="_blank" rel="noopener noreferrer">`nomad.api.variable.Variable` (8:111)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/variables.py#L6-L66" target="_blank" rel="noopener noreferrer">`nomad.api.variables.Variables` (6:66)</a>
- <a href="https://github.com/jrxFive/python-nomad/blob/master/nomad/api/base.py#L10-L220" target="_blank" rel="noopener noreferrer">`nomad.api.base.Requester` (10:220)</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)