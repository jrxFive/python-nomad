## Search

### Regular search

https://developer.hashicorp.com/nomad/api-docs/search

Search in context (can be: jobs, evals, allocs, nodes, deployment, plugins, volumes or all) with prefix

`all` context means every context will be searched.

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

metrics = my_nomad.search("test", "jobs")
```

### Fuzzy search

https://developer.hashicorp.com/nomad/api-docs/search#fuzzy-searching

Search any text in context (can be: jobs, allocs, nodes, plugins, or all)

`all` context means every context will be searched.

Example:

```
import nomad

my_nomad = nomad.Nomad(host='192.168.33.10')

metrics = my_nomad.search.fuzzy("test", "jobs")
```