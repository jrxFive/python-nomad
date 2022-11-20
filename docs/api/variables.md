## Variables

### List jobs

This endpoint lists all known variables in the system registered with Nomad.

https://developer.hashicorp.com/nomad/api-docs/variables

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

variables = my_nomad.variables.get_variables()

for var in variables:
  print(var)
```
