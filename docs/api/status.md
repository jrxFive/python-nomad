## Status

### Read leader

This endpoint returns the address of the current leader in the region.

https://developer.hashicorp.com/nomad/api-docs/status#read-leader

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

leader = my_nomad.status.leader.get_leader()
```

### List peers

This endpoint returns the set of raft peers in the region.

https://developer.hashicorp.com/nomad/api-docs/status#list-peers

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

peers = my_nomad.status.peers.get_peers()

for peer in peers:
  print (peer)
```
