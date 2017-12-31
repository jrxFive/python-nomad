# python-nomad

## Sentinel

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### List policies

Get all policies

https://www.nomadproject.io/api/sentinel-policies.html#list-policies

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policies = my_nomad.sentinel.get_policies()
```

## Create policy

Create a policy

https://www.nomadproject.io/api/sentinel-policies.html#create-or-update-policy

Example:
```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy =  {
            "Name": "my-policy",
            "Description": "This is a great policy",
            "Scope": "submit-job",
            "EnforcementLevel": "advisory",
            "Policy": "main = rule { true }",
          }

my_nomad.sentinel.create_policy("my-policy", policy)
```

## Update policy

Update specific policy

https://www.nomadproject.io/api/sentinel-policies.html#create-or-update-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy =  {
            "Name": "my-policy",
            "Description": "Updated policy",
            "Scope": "submit-job",
            "EnforcementLevel": "advisory",
            "Policy": "main = rule { true }",
          }

my_nomad.sentinel.update_policy("my-policy", policy)
```

## Read policy

Get specific policy

https://www.nomadproject.io/api/sentinel-policies.html#read-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy = my_nomad.sentinel.get_policy("my-policy")
```

## Delete policy

Delete specific policy

https://www.nomadproject.io/api/sentinel-policies.html#delete-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(uri='http://192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

my_nomad.sentinel.delete_policy("my-policy")
```
