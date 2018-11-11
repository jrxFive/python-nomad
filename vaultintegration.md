# Nomad & Vault

## Vault

Vault is a system to store secrets. This system could be integrated as a backend
of secrets of your Nomad cluster.

## Documentation
https://www.hashicorp.com/products/vault/

## Nomad Stanza Job with Vault
https://www.nomadproject.io/docs/job-specification/vault.html

## Security recomendaion using Vault backend
**You should enable** at nomad vault integration [`allow_unantenticated = false`](https://www.nomadproject.io/docs/configuration/vault.html#allow_unauthenticated)

## Nomad Stanza with Vault API v1
https://www.nomadproject.io/docs/job-specification/template.html#vault-kv-api-v1

- **Simple secrets backend**

Ex:
```
template {
  data = <<EOF
    AWS_ACCESS_KEY_ID = "{{with secret "secret/data/aws/s3"}}{{.Data.data.aws_access_key_id}}{{end}}"
  EOF
}
```

## Nomad Stanza with Vault API v2
https://www.nomadproject.io/docs/job-specification/template.html#vault-kv-api-v2

- **Versioned secrets backed.**

Ex:
```
template {
  data = <<EOF
    AWS_ACCESS_KEY_ID = "{{with secret "secret/data/aws/s3"}}{{.Data.data.aws_access_key_id}}{{end}}"
  EOF
}
```
