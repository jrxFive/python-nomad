## 2.0.0
### BREAKING CHANGES
* Drop Python 2 and Python 3.6 support
* Rename `id` arguments to `id_` across of code base
* Rename `type` arguments to `type_` across of code base
### Other changes
* Add more missing parameters to allocations.get_allocations()
* Up `requests` lib version to 2.28.1
* Add missing parameters to allocations.get_allocations and jobs.get_jobs (#144). Thanks @Kamilcuk
* Add option for custom user agent (#150)
* Add missing parameters to nodes.get_nodes (#152).
## 1.5.0
* Add `namespace` argument support for `get_allocations` and `get_deployments` endpoints (#133)
* Add Python 3.10 support (#133)
* Add support for pre-populated Sessions (#132)
* Add scaling policy endpoint (#136)
* Drop Python 3.5 support
* Up `requests` lib version 
* Add support for /var and /vars endpoints ()
* Add support for /search endpoint (#134)
