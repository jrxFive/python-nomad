# Evaluations

### List evaluations

This endpoint lists all evaluations.

https://developer.hashicorp.com/nomad/api-docs/evaluations#list-evaluations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

evaluations = my_nomad.evaluations.get_evaluations()

for evaluation in evaluations:
  print (evaluation)
```
