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

## Non working versions

- NOMAD v 0.5.6 --> server/vault: Fix Vault Client panic when given nonexistent role [GH-2648]
- NOMAD v 0.8.5 --> vault: Fix a regression in which Nomad was only compatible with Vault versions greater than 0.10.0 [GH-4698]
- NOMAD (all version) vs Vault 0.11.0 --> Make crash nomad agent. 
