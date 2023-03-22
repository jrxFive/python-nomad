## Namespaces

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### List namespaces

This endpoint lists all namespaces.

https://developer.hashicorp.com/nomad/api-docs/namespaces#list-namespaces

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

namespaces = my_nomad.namespaces.get_namespaces()

for namespace in namespaces:
  print (token['Name'])

```
