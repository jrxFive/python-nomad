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
