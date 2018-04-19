## Metrics

### Get node metrics

https://www.nomadproject.io/api/metrics.html

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

metrics = my_nomad.metrics.get_metrics()
```
