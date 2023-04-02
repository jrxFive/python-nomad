## Nodes

### List nodes

This endpoint lists all nodes registered with Nomad.

https://developer.hashicorp.com/nomad/api-docs/nodes#list-nodes

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

nodes = my_nomad.nodes.get_nodes()

for node in nodes:
  print (node)
```
