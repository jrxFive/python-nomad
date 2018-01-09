### Nomad client

Examples:

```python


import nomad
# For HTTP Nomad instances
n = nomad.Nomad(host="172.16.100.10", timeout=5)

# For HTTPS Nomad instances with non-self-signed SSL certificates
n = nomad.Nomad(host="172.16.100.10", secure=True, timeout=5, verify=True)

# For HTTPS Nomad instances with self-signed SSL certificates and no validate the cert
n = nomad.Nomad(host="172.16.100.10", secure=True, timeout=5, verify=False)

# For HTTPS Nomad instances with self-signed SSL certificates that mus validate with cert
n = nomad.Nomad(host="172.16.100.10", secure=True, timeout=5, verify=True, cert="/path/to/certfile") # See http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

# For HTTPS Nomad instances with cert file and key
n = nomad.Nomad(host="https://172.16.100.10", secure=True, timeout=5, verify=True, cert=("/path/to/certfile", "/path/to/key") # See http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

# For HTTPS Nomad instances with namespace and acl token
n = nomad.Nomad(host="172.16.100.10", secure=True timeout=5, verify=False, namespace='Namespace-example',token='3f4a0fcd-7c42-773c-25db-2d31ba0c05fe')

"example" in n.jobs

j = n.jobs["example"]["ID"]

example_allocation = n.job.get_allocations(j)

n.job.deregister_job(j)
```
