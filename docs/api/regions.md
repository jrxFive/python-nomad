## Regions

### List regions

https://www.nomadproject.io/api/regions.html#list-regions

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

regions = my_nomad.regions.get_regions()

for region in regions:
  print (region)
```
