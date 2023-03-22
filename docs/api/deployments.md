## Deployments

The deployment endpoints are used to query for and interact with deployments.

### List deployments

This endpoint lists all deployments.

https://developer.hashicorp.com/nomad/api-docs/deployments#list-deployments

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

deployments = my_nomad.deployments.get_deployments()

for deployment in deployments:
  print (deployment)
```
