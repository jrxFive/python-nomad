## Job

### Create new job

This endpoint creates (aka "registers") a new job in the system.

https://www.nomadproject.io/api/jobs.html#create-job

Example:

```
import nomad

job = {'Job': {'AllAtOnce': None,
  'Constraints': None,
  'CreateIndex': None,
  'Datacenters': ['dc1'],
  'ID': 'example',
  'JobModifyIndex': None,
  'Meta': None,
  'ModifyIndex': None,
  'Name': 'example',
  'Namespace': None,
  'ParameterizedJob': None,
  'ParentID': None,
  'Payload': None,
  'Periodic': None,
  'Priority': None,
  'Region': None,
  'Stable': None,
  'Status': None,
  'StatusDescription': None,
  'Stop': None,
  'SubmitTime': None,
  'TaskGroups': [{'Constraints': None,
    'Count': 1,
    'EphemeralDisk': {'Migrate': None, 'SizeMB': 300, 'Sticky': None},
    'Meta': None,
    'Name': 'cache',
    'RestartPolicy': {'Attempts': 10,
     'Delay': 25000000000,
     'Interval': 300000000000,
     'Mode': 'delay'},
    'Tasks': [{'Artifacts': None,
      'Config': {'image': 'redis:3.2', 'port_map': [{'db': 6379}]},
      'Constraints': None,
      'DispatchPayload': None,
      'Driver': 'docker',
      'Env': None,
      'KillTimeout': None,
      'Leader': False,
      'LogConfig': None,
      'Meta': None,
      'Name': 'redis',
      'Resources': {'CPU': 500,
       'DiskMB': None,
       'IOPS': None,
       'MemoryMB': 256,
       'Networks': [{'CIDR': '',
         'Device': '',
         'DynamicPorts': [{'Label': 'db', 'Value': 0}],
         'IP': '',
         'MBits': 10,
         'ReservedPorts': None}]},
      'Services': [{'AddressMode': '',
        'CheckRestart': None,
        'Checks': [{'Args': None,
          'CheckRestart': None,
          'Command': '',
          'Header': None,
          'Id': '',
          'InitialStatus': '',
          'Interval': 10000000000,
          'Method': '',
          'Name': 'alive',
          'Path': '',
          'PortLabel': '',
          'Protocol': '',
          'TLSSkipVerify': False,
          'Timeout': 2000000000,
          'Type': 'tcp'}],
        'Id': '',
        'Name': 'global-redis-check',
        'PortLabel': 'db',
        'Tags': ['global', 'cache']}],
      'ShutdownDelay': 0,
      'Templates': None,
      'User': '',
      'Vault': None}],
    'Update': None}],
  'Type': 'service',
  'Update': {'AutoRevert': False,
   'Canary': 0,
   'HealthCheck': None,
   'HealthyDeadline': 180000000000,
   'MaxParallel': 1,
   'MinHealthyTime': 10000000000,
   'Stagger': None},
  'VaultToken': None,
  'Version': None}}

my_nomad = nomad.Nomad(host='192.168.33.10')

response = my_nomad.job.register_job("example", job)
```


### Read job

This endpoint reads information about a single job for its specification and status.

https://www.nomadproject.io/api/jobs.html#read-job


Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

job = my_nomad.job.get_job("example")
```

### Job versions

This endpoint reads information about all versions of a job.

https://www.nomadproject.io/api/jobs.html#list-job-versions

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

versions = my_nomad.job.get_versions("example")

for version in versions["Versions"]:
  print (version)
```

### List job allocations

This endpoint reads information about a single job's allocations.

https://www.nomadproject.io/api/jobs.html#list-job-allocations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocations = my_nomad.job.get_allocations("example")

for allocation in allocations:
  print (allocation)
```

### List job evaluations

This endpoint reads information about a single job's evaluations

https://www.nomadproject.io/api/jobs.html#list-job-evaluations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

evaluations = my_nomad.job.get_evaluations("example")

for evaluation in evaluations:
  print (evaluation)
```


### List job deploymetns

This endpoint lists a single job's deployments

https://www.nomadproject.io/api/jobs.html#list-job-deployments

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

deployments = my_nomad.job.get_deployments("example")

for deployment in deployments:
  print (deployment)
```


### Read job's most recent deployment

This endpoint returns a single job's most recent deployment.

https://www.nomadproject.io/api/jobs.html#read-job-39-s-most-recent-deployment

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

deployment = my_nomad.job.get_deployment("example")

```

### Job summary

This endpoint reads summary information about a job.

https://www.nomadproject.io/api/jobs.html#read-job-summary

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

summary = my_nomad.job.get_summary("example")
```


### Update existing job

This endpoint registers a new job or updates an existing job.

https://www.nomadproject.io/api/jobs.html#update-existing-job

Example:

See create new job


### Dispatch job

This endpoint dispatches a new instance of a parameterized job.

https://www.nomadproject.io/api/jobs.html#dispatch-job

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

parametrize_job = {
    "Job": {
        "Region": "example-region",
        "ID": "example-batch",
        "ParentID": "",
        "Name": "example-batch",
        "Type": "batch",
        "Priority": 100,
        "AllAtOnce": False,
        "Datacenters": [
            "dc1"],
        "Constraints": [],
        "ParameterizedJob": {
            "Payload": "optional",
            "MetaRequired": [
                "time"
            ],
            "MetaOptional": []
        },
        "TaskGroups": [
            {
                "Name": "example-task-group",
                "Count": 0,
                "Constraints": None,
                "Tasks": [
                    {
                        "Name": "example-task",
                        "Driver": "docker",
                        "Config": {
                            "args": ["${NOMAD_META_TIME"],
                            "command": "sleep",
                            "image": "scratch",
                            "logging": [],
                            "port_map": []
                        },
                        "Constraints": None,
                        "Env": {},
                        "Services": [],
                        "Resources": {
                            "CPU": 100,
                            "MemoryMB": 200,
                            "IOPS": 0,
                            "Networks": []
                        },
                        "Meta": None,
                        "KillTimeout": 5000000000,
                        "LogConfig": {
                            "MaxFiles": 10,
                            "MaxFileSizeMB": 10
                        },
                        "Artifacts": None,
                        "Vault": None,
                        "Templates": [],
                        "DispatchPayload": None
                    }
                ],
                "RestartPolicy": {
                    "Interval": 600000000000,
                    "Attempts": 10,
                    "Delay": 30000000000,
                    "Mode": "delay"
                }
            }
        ],
        "Update": {
            "Stagger": 0,
            "MaxParallel": 0
        }
    }
}

my_nomad = nomad.Nomad(host='192.168.33.10')

response = my_nomad.job.register_job("example-batch", parametrize_job)

my_nomad.job.dispatch_job("example-batch", meta={"time": "500"})
```

### Revert to older job version

This endpoint reverts the job to an older version.

https://www.nomadproject.io/api/jobs.html#revert-to-older-job-version

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

prior_job_version = my_nomad.job.job.get_deployment("example")["JobVersion"]

prior_job_version = current_job_version - 1

my_nomad.job.revert_job("example", prior_job_version, current_job_version)
```


### Set job stability

This endpoint sets the job's stability.

https://www.nomadproject.io/api/jobs.html#set-job-stability

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

current_job_version = my_nomad.job.get_deployment("example")["JobVersion"]

my_nomad.job.stable_job("example", current_job_version, True)
```


### Create job evaluation

This endpoint creates a new evaluation for the given job. This can be used to force run the scheduling logic if necessary.

https://www.nomadproject.io/api/jobs.html#create-job-evaluation

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.job.evaluate_job("example")
```

### Create job plan

This endpoint invokes a dry-run of the scheduler for the job.

https://www.nomadproject.io/api/jobs.html#create-job-plan

Example:

```
import nomad

job = {'Job': {'AllAtOnce': None,
  'Constraints': None,
  'CreateIndex': None,
  'Datacenters': ['dc1'],
  'ID': 'example',
  'JobModifyIndex': None,
  'Meta': None,
  'ModifyIndex': None,
  'Name': 'example',
  'Namespace': None,
  'ParameterizedJob': None,
  'ParentID': None,
  'Payload': None,
  'Periodic': None,
  'Priority': None,
  'Region': None,
  'Stable': None,
  'Status': None,
  'StatusDescription': None,
  'Stop': None,
  'SubmitTime': None,
  'TaskGroups': [{'Constraints': None,
    'Count': 1,
    'EphemeralDisk': {'Migrate': None, 'SizeMB': 300, 'Sticky': None},
    'Meta': None,
    'Name': 'cache',
    'RestartPolicy': {'Attempts': 10,
     'Delay': 25000000000,
     'Interval': 300000000000,
     'Mode': 'delay'},
    'Tasks': [{'Artifacts': None,
      'Config': {'image': 'redis:3.2', 'port_map': [{'db': 6379}]},
      'Constraints': None,
      'DispatchPayload': None,
      'Driver': 'docker',
      'Env': None,
      'KillTimeout': None,
      'Leader': False,
      'LogConfig': None,
      'Meta': None,
      'Name': 'redis',
      'Resources': {'CPU': 500,
       'DiskMB': None,
       'IOPS': None,
       'MemoryMB': 256,
       'Networks': [{'CIDR': '',
         'Device': '',
         'DynamicPorts': [{'Label': 'db', 'Value': 0}],
         'IP': '',
         'MBits': 10,
         'ReservedPorts': None}]},
      'Services': [{'AddressMode': '',
        'CheckRestart': None,
        'Checks': [{'Args': None,
          'CheckRestart': None,
          'Command': '',
          'Header': None,
          'Id': '',
          'InitialStatus': '',
          'Interval': 10000000000,
          'Method': '',
          'Name': 'alive',
          'Path': '',
          'PortLabel': '',
          'Protocol': '',
          'TLSSkipVerify': False,
          'Timeout': 2000000000,
          'Type': 'tcp'}],
        'Id': '',
        'Name': 'global-redis-check',
        'PortLabel': 'db',
        'Tags': ['global', 'cache']}],
      'ShutdownDelay': 0,
      'Templates': None,
      'User': '',
      'Vault': None}],
    'Update': None}],
  'Type': 'service',
  'Update': {'AutoRevert': False,
   'Canary': 0,
   'HealthCheck': None,
   'HealthyDeadline': 180000000000,
   'MaxParallel': 1,
   'MinHealthyTime': 10000000000,
   'Stagger': None},
  'VaultToken': None,
  'Version': None}}

my_nomad = nomad.Nomad(host='192.168.33.10')

plan = my_nomad.job.plan_job("example", job)
```

### Stop a job

This endpoint deregisters a job, and stops all allocations part of it.

https://www.nomadproject.io/api/jobs.html#stop-a-job

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.job.deregister_job("example")
```
