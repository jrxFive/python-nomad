## Deployment

The deployment endpoints are used to query for and interact with deployments.

### Read deployment

This endpoint reads information about a specific deployment by ID.

https://www.nomadproject.io/api/deployments.html#read-deployment

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

deployment = my_nomad.deployment.get_deployment('a8061a1c-d4c9-2a7d-a4b2-932c8f83e587')

print (deployment)
```


### List Allocations for Deployment

This endpoint lists the allocations created or modified for the given deployment.

https://www.nomadproject.io/api/deployments.html#list-allocations-for-deployment

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocations = my_nomad.deployment.get_deployment_allocations('a8061a1c-d4c9-2a7d-a4b2-932c8f83e587')

for allocation in allocations:
  print (allocation)
```

### Fail Deployment

This endpoint is used to mark a deployment as failed. This should be done to force the scheduler to stop creating allocations as part of the deployment or to cause a rollback to a previous job version. This endpoint only triggers a rollback if the most recent stable version of the job has a different specification than the job being reverted.

https://www.nomadproject.io/api/deployments.html#fail-deployment

example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

fail_deployment = my_nomad.deployment.fail_deployment('a8061a1c-d4c9-2a7d-a4b2-932c8f83e587')

# sample output (fail_deployment)
# {'DeploymentModifyIndex': 52,
# 'EvalCreateIndex': 52,
# 'EvalID': '47fd9a98-fc77-92ea-1547-881dccbd8fa1',
# 'Index': 52,
# 'RevertedJobVersion': 0}
#
```


### Pause deployments

This endpoint is used to pause or unpause a deployment. This is done to pause a rolling upgrade or resume it.

https://www.nomadproject.io/api/deployments.html#pause-deployment

example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

pause = my_nomad.deployment.pause_deployment("52c47d49-eefa-540f-f0f1-d25ba298c87f",True)

# sample output (pause)
# {'DeploymentModifyIndex': 75,
# 'EvalCreateIndex': 0,
# 'EvalID': '',
# 'Index': 75,
# 'RevertedJobVersion': None}
#

pause = my_nomad.deployment.pause_deployment("52c47d49-eefa-540f-f0f1-d25ba298c87f",False)

# sample output (pause)
#{'DeploymentModifyIndex': 76,
# 'EvalCreateIndex': 76,
# 'EvalID': '5e9b85fa-ad96-0692-98e9-85a7d957e984',
# 'Index': 76,
# 'RevertedJobVersion': None}
```


### Promote Deployment

This endpoint is used to promote task groups that have canaries for a deployment. This should be done when the placed canaries are healthy and the rolling upgrade of the remaining allocations should begin.

https://www.nomadproject.io/api/deployments.html#promote-deployment

#### Promote All

  - Specifies whether all task groups should be promoted.

example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

promote = my_nomad.deployment.promote_deployment_all("52c47d49-eefa-540f-f0f1-d25ba298c87f",True)
```

#### Promote Groups

  - Specifies a particular set of task groups that should be promoted

example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

promote = my_nomad.deployment.promote_deployment_groups("52c47d49-eefa-540f-f0f1-d25ba298c87f",groups=['task1','task2'])
```


### Set allocation health in deployment

This endpoint is used to set the health of an allocation that is in the deployment manually. In some use cases, automatic detection of allocation health may not be desired. As such those task groups can be marked with an upgrade policy that uses health_check = "manual". Those allocations must have their health marked manually using this endpoint. Marking an allocation as healthy will allow the rolling upgrade to proceed. Marking it as failed will cause the deployment to fail. This endpoint only triggers a rollback if the most recent stable version of the job has a different specification than the job being reverted.

https://www.nomadproject.io/api/deployments.html#set-allocation-health-in-deployment

example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

output = my_nomad.deployment.deployment_allocation_health("5456bd7a-9fc0-c0dd-6131-cbee77f57577", healthy_allocations=["eb13bc8a-7300-56f3-14c0-d4ad115ec3f5",    "6584dad8-7ae3-360f-3069-0b4309711cc1"
], unhealthy_allocations=[])

# output
#{
#  "EvalID": "0d834913-58a0-81ac-6e33-e452d83a0c66",
#  "EvalCreateIndex": 20,
#  "DeploymentModifyIndex": 20,
#  "RevertedJobVersion": 1,
#  "Index": 20
#}

```
