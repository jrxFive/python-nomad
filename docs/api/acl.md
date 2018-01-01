## ACL & tokens

Valid for nomad version **>= 0.7.0**

Nomad must be running with ACL mode enabled.

### Bootstrap token

This endpoint is used to bootstrap the ACL system and provide the initial management token. This request is always forwarded to the authoritative region. It can only be invoked once until a bootstrap reset is performed.

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

This endpoint lists all ACL tokens. This lists the local tokens and the global tokens which have been replicated to the region, and may lag behind the authoritative region.

https://www.nomadproject.io/api/acl-tokens.html#list-tokens

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

tokens = my_nomad.acl.get_tokens()

for token in tokens:
  print (token['Name'])

```

### Create token

This endpoint creates an ACL Token. If the token is a global token, the request is forwarded to the authoritative region.

https://www.nomadproject.io/api/acl-tokens.html#create-token

Exmample:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

new_token = {
              "Name": "Readonly token",
              "Type": "client",
              "Policies": ["readonly"],
              "Global": False
            }

created_token = my_nomad.acl.create_token(new_token)
```

### Update token

This endpoint updates an existing ACL Token. If the token is a global token, the request is forwarded to the authoritative region. Note that a token cannot be switched from global to local or vice versa.

https://www.nomadproject.io/api/acl-tokens.html#update-token

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

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

This endpoint reads an ACL token with the given accessor. If the token is a global token which has been replicated to the region it may lag behind the authoritative region.

https://www.nomadproject.io/api/acl-tokens.html#read-token

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

token = my_nomad.acl.get_token("377ba749-8b0e-c7fd-c0c0-9da5bb943088")
```

### Read Self token

This endpoint reads the ACL token given by the passed SecretID. If the token is a global token which has been replicated to the region it may lag behind the authoritative region.

https://www.nomadproject.io/api/acl-tokens.html#read-self-token

Exmaple:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

self_token = my_nomad.acl.get_selftoken()
```

### Delete token

This endpoint deletes the ACL token by accessor. This request is forwarded to the authoritative region for global tokens.

https://www.nomadproject.io/api/acl-tokens.html#delete-token

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

my_nomad.acl.delete_token("377ba749-8b0e-c7fd-c0c0-9da5bb943088")
```


## Policies

Manage acl Policies

https://www.nomadproject.io/api/acl-policies.html

### List policies

This endpoint lists all ACL policies. This lists the policies that have been replicated to the region, and may lag behind the authoritative region.

https://www.nomadproject.io/api/acl-policies.html#list-policies

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

policies = my_nomad.acl.get_policies()
```

### Create policy

This endpoint creates an ACL Policy. This request is always forwarded to the authoritative region.

https://www.nomadproject.io/api/acl-policies.html#create-or-update-policy

Example:
```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

policy =  {
            "Name": "my-policy",
            "Description": "This is a great policy",
            "Rules": ""
          }

my_nomad.acl.create_policy("my-policy", policy)
```

### Update policy

This endpoint update an ACL Policy. This request is always forwarded to the authoritative region.

https://www.nomadproject.io/api/acl-policies.html#create-or-update-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

policy =  {
            "Name": "my-policy",
            "Description": "Update my policy",
            "Rules": ""
          }

my_nomad.acl.update_policy("my-policy", policy)
```

### Read policy

This endpoint reads an ACL policy with the given name. This queries the policy that have been replicated to the region, and may lag behind the authoritative region.

https://www.nomadproject.io/api/acl-policies.html#read-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

policy = my_nomad.acl.get_policy("my-policy")
```

### Delete policy

This endpoint deletes the named ACL policy. This request is always forwarded to the authoritative region.

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b')

my_nomad.acl.delete_policy("my-policy")
```
