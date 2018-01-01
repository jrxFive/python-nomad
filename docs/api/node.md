## Node

### Read Node

This endpoint queries the status of a client node.

https://www.nomadproject.io/api/nodes.html#read-node

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

node = my_nomad.node.get_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```

### List node allocations

This endpoint lists all of the allocations for the given node. This can be used to determine what allocations have been scheduled on the node, their current status, and the values of dynamically assigned resources, like ports.

https://www.nomadproject.io/api/nodes.html#list-node-allocations

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

allocations = my_nomad.node.get_allocations('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')

for allocation in allocations:
  print (allocation)
```


### Create node evaluation

This endpoint creates a new evaluation for the given node. This can be used to force a run of the scheduling logic.

https://www.nomadproject.io/api/nodes.html#create-node-evaluation

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

my_nomad.node.evaluate_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```

### Drain node

This endpoint toggles the drain mode of the node. When draining is enabled, no further allocations will be assigned to this node, and existing allocations will be migrated to new nodes.

https://www.nomadproject.io/api/nodes.html#drain-node

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

my_nomad.node.drain_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```
