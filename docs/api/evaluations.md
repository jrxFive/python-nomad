# Evaluations

### List evaluations

This endpoint lists all evaluations.

https://www.nomadproject.io/api/evaluations.html#list-evaluations

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

evaluations = my_nomad.evaluations.get_evaluations()

for evaluation in evaluations:
  print (evaluation)
```
