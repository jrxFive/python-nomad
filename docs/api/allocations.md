## Allocations

### List allocations

This endpoint lists all allocations.

https://www.nomadproject.io/api/allocations.html#list-allocations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocations = my_nomad.allocations.get_allocations()

for allocation in allocations:
  print (allocation)
```
