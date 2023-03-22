## Sentinel

Valid for nomad version **>= 0.7.0**

You must have nomad **ENTERPRISE Edition**

### List policies

Get all policies

https://developer.hashicorp.com/nomad/api-docs/sentinel-policies#list-policies

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policies = my_nomad.sentinel.get_policies()
```

## Create policy

Create a policy

https://developer.hashicorp.com/nomad/api-docs/sentinel-policies#create-or-update-policy

Example:
```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

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

https://developer.hashicorp.com/nomad/api-docs/sentinel-policies#create-or-update-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

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

https://developer.hashicorp.com/nomad/api-docs/sentinel-policies#read-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

policy = my_nomad.sentinel.get_policy("my-policy")
```

## Delete policy

Delete specific policy

https://developer.hashicorp.com/nomad/api-docs/sentinel-policies#delete-policy

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10', token='10f0cf19-2c8c-cb4b-721a-fda2a388740b', verify=False)

my_nomad.sentinel.delete_policy("my-policy")
```
