## Jobs

### List jobs

This endpoint lists all known jobs in the system registered with Nomad.

https://developer.hashicorp.com/nomad/api-docs/jobs#list-jobs

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

jobs = my_nomad.jobs.get_jobs()

for job in jobs:
  print (job)
```

### Create new job

This endpoint creates (aka "registers") a new job in the system.

https://developer.hashicorp.com/nomad/api-docs/jobs#create-job

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

response = my_nomad.jobs.register_job(job)
```


### Parse Job
To convert to python dict and verify for correctness a hcl/nomad file. The example will use "example.nomad" when running
`nomad job init` and it will assume this file is in the current working directory. In practice this file should already
be read and used as the parameter hcl.

https://developer.hashicorp.com/nomad/api-docs/jobs#parse-job

```python

import nomad

nomad_client = nomad.Nomad()

with open("example.nomad", "r") as fh:
    try:
        job_raw_nomad = fh.read()
        job_dict = nomad_client.jobs.parse(job_raw_nomad)
    except nomad.api.exceptions.BadRequestNomadException as err:
        print(err.nomad_resp.reason)
        print(err.nomad_resp.text)
```

On success of example.nomad being successfully parsed job_dict will have:

```python
{'AllAtOnce': None,
 'Constraints': None,
 'CreateIndex': None,
 'Datacenters': ['dc1'],
 'Dispatched': False,
 'ID': 'example',
 'JobModifyIndex': None,
 'Meta': None,
 'Migrate': {'HealthCheck': 'checks',
             'HealthyDeadline': 300000000000,
             'MaxParallel': 1,
             'MinHealthyTime': 10000000000},
 'ModifyIndex': None,
 'Name': 'example',
 'Namespace': None,
 'ParameterizedJob': None,
 'ParentID': None,
 'Payload': None,
 'Periodic': None,
 'Priority': None,
 'Region': None,
 'Reschedule': None,
 'Stable': None,
 'Status': None,
 'StatusDescription': None,
 'Stop': None,
 'SubmitTime': None,
 'TaskGroups': [{'Constraints': None,
                 'Count': 1,
                 'EphemeralDisk': {'Migrate': None,
                                   'SizeMB': 300,
                                   'Sticky': None},
                 'Meta': None,
                 'Migrate': None,
                 'Name': 'cache',
                 'ReschedulePolicy': None,
                 'RestartPolicy': {'Attempts': 2,
                                   'Delay': 15000000000,
                                   'Interval': 1800000000000,
                                   'Mode': 'fail'},
                 'Tasks': [{'Artifacts': None,
                            'Config': {'image': 'redis:3.2',
                                       'port_map': [{'db': 6379}]},
                            'Constraints': None,
                            'DispatchPayload': None,
                            'Driver': 'docker',
                            'Env': None,
                            'KillSignal': '',
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
                                                        'DynamicPorts': [{'Label': 'db',
                                                                          'Value': 0}],
                                                        'IP': '',
                                                        'MBits': 10,
                                                        'ReservedPorts': None}]},
                            'Services': [{'AddressMode': '',
                                          'CanaryTags': None,
                                          'CheckRestart': None,
                                          'Checks': [{'AddressMode': '',
                                                      'Args': None,
                                                      'CheckRestart': None,
                                                      'Command': '',
                                                      'GRPCService': '',
                                                      'GRPCUseTLS': False,
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
                                          'Name': 'redis-cache',
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
            'ProgressDeadline': None,
            'Stagger': None},
 'VaultToken': None,
 'Version': None}
```

On failure it will raise `BadRequestNomadException` we can inspect the requests response:
```
>>> err.nomad_resp.reason
'Bad Request'

err.nomad_resp.text
"error parsing 'job': 1 error(s) occurred:\n\n* job: invalid key: datacenter"

```