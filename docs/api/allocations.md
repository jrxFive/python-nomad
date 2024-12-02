## Allocations

### List allocations

This endpoint lists all allocations.

https://developer.hashicorp.com/nomad/api-docs/allocations#list-allocations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocations = my_nomad.allocations.get_allocations()

for allocation in allocations:
  print (allocation)
```

### Signal allocation

This endpoint sends a signal to an allocation or task.

https://developer.hashicorp.com/nomad/api-docs/allocations#signal-allocation

Example:

```
import signal
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

alloc_id = nomad_setup.allocations.get_allocations()[0]["ID"]

# Send signal to an allocation
my_nomad.client.allocation.signal_allocation(alloc_id, signal.SIGUSR1.name)

# Send signal to a task in allocation
my_nomad.client.allocation.signal_allocation(alloc_id, signal.SIGUSR1.name, task="my_task")
```
