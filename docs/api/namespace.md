## Namespaces

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### Create namespace

Create new namespace

https://developer.hashicorp.com/nomad/api-docs/namespaces#create-or-update-namespace

Exmample:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

namespace = {
              "Name": "api-prod",
              "Description": "Production API Servers"
            }
my_nomad.namespace.create_namespace(namespace)
```

### Set working workspace for the session.

This endpoint manage the namespace used for the session.

Exmample:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

namespace = {
              "Name": "api-prod",
              "Description": "Production API Servers"
            }
my_nomad.namespace.create_namespace(namespace)

# Activate workspace on requests
my_nomad.set_namespace("api-prod")

# Show current workspace for the session
print (my_nomad.get_namespace())
```

### Read Namespace

This endpoint reads information about a specific namespace.

https://developer.hashicorp.com/nomad/api-docs/namespaces#read-namespace

Exmample:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

namespace = my_nomad.namespace.get_namespace("api-prod")
```


### Update namespace

Update existing namespace

https://developer.hashicorp.com/nomad/api-docs/namespaces#create-or-update-namespace

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

namespace = {
              "Name": "api-prod",
              "Description": "Production API Servers"
            }
my_nomad.namespace.create_namespace("api-prod", namespace)
```

### Delete namespace

Delete namespace

https://developer.hashicorp.com/nomad/api-docs/namespaces#create-or-update-namespace

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.namespace.delete_namespace("api-prod")
```
