## Evaluation

### Read evaluation

This endpoint reads information about a specific evaluation by ID.

https://www.nomadproject.io/api/evaluations.html#read-evaluation

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

evaluation = my_nomad.evaluation.get_evaluation('5456bd7a-9fc0-c0dd-6131-cbee77f57577')

print (evaluation)
```

### List allocations for evaluation

This endpoint lists the allocations created or modified for the given evaluation.

https://www.nomadproject.io/api/evaluations.html#list-allocations-for-evaluation

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

allocation = my_nomad.evaluation.get_allocations('5456bd7a-9fc0-c0dd-6131-cbee77f57577')

for allocation in allocations:
  print (allocation)
```
