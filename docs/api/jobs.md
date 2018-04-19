## Jobs

### List jobs

This endpoint lists all known jobs in the system registered with Nomad.

https://www.nomadproject.io/api/jobs.html#list-jobs

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

response = my_nomad.jobs.register_job(job)
```