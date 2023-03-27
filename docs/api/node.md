## Node

### Read Node

This endpoint queries the status of a client node.

https://developer.hashicorp.com/nomad/api-docs/nodes#read-node

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

node = my_nomad.node.get_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```

### List node allocations

This endpoint lists all of the allocations for the given node. This can be used to determine what allocations have been scheduled on the node, their current status, and the values of dynamically assigned resources, like ports.

https://developer.hashicorp.com/nomad/api-docs/nodes#list-node-allocations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

allocations = my_nomad.node.get_allocations('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')

for allocation in allocations:
  print (allocation)
```


### Create node evaluation

This endpoint creates a new evaluation for the given node. This can be used to force a run of the scheduling logic.

https://developer.hashicorp.com/nomad/api-docs/nodes#create-node-evaluation

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.node.evaluate_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```

### Drain node

This endpoint toggles the drain mode of the node. When draining is enabled, no further allocations will be assigned to this node, and existing allocations will be migrated to new nodes.

https://developer.hashicorp.com/nomad/api-docs/nodes#drain-node

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

#enable drain mode
my_nomad.node.drain_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', enable=True)

#disable drain mode
my_nomad.node.drain_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', enable=False)
```

### Drain node with DrainSpec

This endpoint toggles the drain mode of the node. When draining is enabled, no further allocations will be assigned to this node, and existing allocations will be migrated to new nodes.

https://developer.hashicorp.com/nomad/api-docs/nodes#drain-node

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

#enable drain mode
my_nomad.node.drain_node_with_spec('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', drain_spec={"Duration": "100000000"})

#enable drain mode but leave system jobs on the specificed node
my_nomad.node.drain_node_with_spec('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', drain_spec={"Duration": "100000000", "IgnoreSystemJobs": True})

#disable drain but leave node in an ineligible state
my_nomad.node.drain_node_with_spec('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', drain_spec={})

#disable drain and put node in an eligible state
my_nomad.node.drain_node_with_spec('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', drain_spec={}, mark_eligible=True)
```

### Eligible Node

This endpoint toggles the eligibility of the node. When a node's "SchedulingEligibility" is ineligible  the scheduler will not consider it for new placements.

https://developer.hashicorp.com/nomad/api-docs/nodes#toggle-node-eligibility

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

# sets node to ineligible state
my_nomad.node.eligible_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', ineligible=True)

# sets node to eligible state
my_nomad.node.eligible_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98', eligible=True)
```

### Purge Node

This endpoint purges a node from the system. Nodes can still join the cluster if they are alive.

https://developer.hashicorp.com/nomad/api-docs/nodes#purge-node

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.node.purge_node('ed1bbae7-c38a-df2d-1de7-50dbc753fc98')
```
