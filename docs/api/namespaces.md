# python-nomad

## Namespaces

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### List namespaces

List all namespaces

https://www.nomadproject.io/api/namespaces.html#list-namespaces

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

namespaces = my_nomad.namespaces.get_namespaces()

for namespace in namespaces:
  print (token['Name'])

```
