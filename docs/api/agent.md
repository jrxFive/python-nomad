## Agent

### List members

This endpoint queries the agent for the known peers in the gossip pool. This endpoint is only applicable to servers. Due to the nature of gossip, this is eventually consistent.

https://www.nomadproject.io/api/agent.html#list-members

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

members = my_nomad.agent.get_members()

for member in members["Members"]:
  print (member["Name"])
```

### List all Servers

This endpoint lists the known server nodes. The servers endpoint is used to query an agent in client mode for its list of known servers. Client nodes register themselves with these server addresses so that they may dequeue work. The servers endpoint can be used to keep this configuration up to date if there are changes in the cluster

https://www.nomadproject.io/api/agent.html#list-servers

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

servers = my_nomad.agent.get_servers()

for server in servers:
  print (server)
```

### Query Self

This endpoint queries the state of the target agent (self).

https://www.nomadproject.io/api/agent.html#query-self

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

agent = my_nomad.agent.get_agent()

print (agent)
```

### Update Servers

This endpoint updates the list of known servers to the provided list. This replaces all previous server addresses with the new list.

https://www.nomadproject.io/api/agent.html#update-servers

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

r = my_nomad.agent.update_servers(['192.168.33.11', '10.1.10.200:4829'])
```

### Join agent

This endpoint introduces a new member to the gossip pool. This endpoint is only eligible for servers.

https://www.nomadproject.io/api/agent.html#join-agent

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

r = my_nomad.agent.join_agent("server02")
```

### Force leave

This endpoint forces a member of the gossip pool from the "failed" state to the "left" state. This allows the consensus protocol to remove the peer and stop attempting replication. This is only applicable for servers.

https://www.nomadproject.io/api/agent.html#force-leave-agent

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

r = my_nomad.agent.force_leave("server02")
```

### Health

This endpoint returns whether or not the agent is healthy. When using Consul it is the endpoint Nomad will register for its own health checks.

When the agent is unhealthy 500 will be returned along with JSON response containing an error message.

https://www.nomadproject.io/api/agent.html#health

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

r = my_nomad.agent.get_health()

```
