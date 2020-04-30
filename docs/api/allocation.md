## Allocation

### Get allocation

This endpoint reads information about a specific allocation.

https://www.nomadproject.io/api/allocations.html#read-allocation

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocation = my_nomad.allocation.get_allocation('32c54571-fb79-97d2-ee38-16673bab692c')

print (allocation)
```

### Stop an allocation

This endpoint stops and reschedules a specific allocation.

https://www.nomadproject.io/api-docs/allocations/#stop-allocation

Example of stopping an allocation

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.allocation.stop_allocation('32c54571-fb79-97d2-ee38-16673bab692c')
```
