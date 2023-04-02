## System

### Force GC

This endpoint initializes a garbage collection of jobs, evaluations, allocations, and nodes. This is an asynchronous operation.

https://developer.hashicorp.com/nomad/api-docs/system#force-gc

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.system.initiate_garbage_collection()
```

### Reconcilie summaries

This endpoint reconciles the summaries of all registered jobs.

https://developer.hashicorp.com/nomad/api-docs/system#reconcile-summaries

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.system.reconcile_summaries()
```
