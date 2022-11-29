## Variable

### Read variable

This endpoint reads a specific variable by path. This API returns the decrypted variable body.

https://developer.hashicorp.com/nomad/api-docs/variables

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

variable = my_nomad.variable.get_variable("path_to_variable")
```

### Create variable

This endpoint creates or updates a variable.

https://developer.hashicorp.com/nomad/api-docs/variables

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

job = my_nomad.variable.create_variable("path_to_variable")

payload = {
    "Items": {"user": "test", "password": "test123"},
}
my_nomad.variable.create_variable("variable_path", payload)
```

### Delete variable

This endpoint deletes a specific variable by path.

https://developer.hashicorp.com/nomad/api-docs/variables

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

my_nomad.variable.delete_variable("path_to_variable")
```