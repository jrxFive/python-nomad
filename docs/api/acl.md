## ACL & tokens

Valid for nomad version **>= 0.7.0**

Nomad must be running with ACL mode enabled.

### Bootstrap token

Activate bootstrap token

https://www.nomadproject.io/api/acl-tokens.html#bootstrap-token

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10',verify=False)

bootstrap = my_nomad.acl.generate_bootstrap()

print (bootstrap["SecretID"])
10f0cf19-2c8c-cb4b-721a-fda2a388740b
```

### List tokens

List all tokens

https://www.nomadproject.io/api/acl-tokens.html#list-tokens

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

tokens = my_nomad.acl.get_tokens()

for token in tokens:
  print (token['Name'])

```

### Create token

Create new token

https://www.nomadproject.io/api/acl-tokens.html#create-token

Exmample:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

new_token = {
              "Name": "Readonly token",
              "Type": "client",
              "Policies": ["readonly"],
              "Global": False
            }

created_token = my_nomad.acl.create_token(new_token)
```

### Update token

Update existing token

https://www.nomadproject.io/api/acl-tokens.html#update-token

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

update_token =  {
                  "AccessorID":'377ba749-8b0e-c7fd-c0c0-9da5bb943088',
                  "Name": "Update token",
                  "Type": "client",
                  "Policies": ["readonly"],
                  "Global": False
                }

updated_token = my_nomad.acl.update_token('377ba749-8b0e-c7fd-c0c0-9da5bb943088', update_token)
```

### Read token

Get specific token

https://www.nomadproject.io/api/acl-tokens.html#read-token

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

token = my_nomad.acl.get_token("377ba749-8b0e-c7fd-c0c0-9da5bb943088")
```

### Read Self token

Read token used in current session

https://www.nomadproject.io/api/acl-tokens.html#read-self-token

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

self_token = my_nomad.acl.get_selftoken()
```

### Delete token

Delete specific token

https://www.nomadproject.io/api/acl-tokens.html#delete-token

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

my_nomad.acl.delete_token("377ba749-8b0e-c7fd-c0c0-9da5bb943088")
```


# Policies

Manage acl Policies

https://www.nomadproject.io/api/acl-policies.html

### List policies

Get all policies

https://www.nomadproject.io/api/acl-policies.html#list-policies

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policies = my_nomad.acl.get_policies()
```

## Create policy

Create a policy

https://www.nomadproject.io/api/acl-policies.html#create-or-update-policy

Example:
```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy =  {
            "Name": "my-policy",
            "Description": "This is a great policy",
            "Rules": ""
          }

my_nomad.acl.create_policy("my-policy", policy)
```

## Update policy

Update specific policy

https://www.nomadproject.io/api/acl-policies.html#create-or-update-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy =  {
            "Name": "my-policy",
            "Description": "Update my policy",
            "Rules": ""
          }

my_nomad.acl.update_policy("my-policy", policy)
```

## Read policy

Get specific policy

https://www.nomadproject.io/api/acl-policies.html#read-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy = my_nomad.acl.get_policy("my-policy")
```

## Delete policy

Delete specific policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

my_nomad.acl.delete_policy("my-policy")
```
