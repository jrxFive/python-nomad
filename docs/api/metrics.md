## Metrics

### Get node metrics

https://developer.hashicorp.com/nomad/api-docs/metrics.html

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

metrics = my_nomad.metrics.get_metrics()
```
