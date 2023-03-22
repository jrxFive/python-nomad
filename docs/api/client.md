## Client

### Read stats

This endpoint queries the actual resources consumed on a node. The API endpoint is hosted by the Nomad client and requests have to be made to the nomad client whose resource usage metrics are of interest.

https://developer.hashicorp.com/nomad/api-docs/client#read-stats

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')


```
