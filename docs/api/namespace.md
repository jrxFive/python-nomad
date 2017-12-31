## Namespaces

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### Create namespace

Create new namespace

https://www.nomadproject.io/api/namespaces.html#create-or-update-namespace

Exmample:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

namespace = {
              "Namespace": "api-prod",
              "Description": "Production API Servers"
            }
my_nomad.namespace.create_namespace(namespace)
```

### Read Namespace

This endpoint reads information about a specific namespace.

https://www.nomadproject.io/api/namespaces.html#read-namespace

Exmample:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

namespace = my_nomad.namespace.get_namespace("api-prod")
```


### Update namespace

Update existing namespace

https://www.nomadproject.io/api/namespaces.html#create-or-update-namespace

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

namespace = {
              "Namespace": "api-prod",
              "Description": "Production API Servers"
            }
my_nomad.namespace.create_namespace("api-prod", namespace)
```

### Delete namespace

Delete namespace

https://www.nomadproject.io/api/namespaces.html#create-or-update-namespace

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10')

my_nomad.namespace.delete_namespace("api-prod")
```
