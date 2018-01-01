## System

### Force GC

This endpoint initializes a garbage collection of jobs, evaluations, allocations, and nodes. This is an asynchronous operation.

https://www.nomadproject.io/api/system.html#force-gc

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

my_nomad.system.initiate_garbage_collection()
```

### Reconcilie summaries

This endpoint reconciles the summaries of all registered jobs.

https://www.nomadproject.io/api/system.html#reconcile-summaries

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

my_nomad.system.reconcile_summaries()
```
