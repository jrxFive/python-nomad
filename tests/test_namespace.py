import tests.common as common

import json

import responses


@responses.activate
def test_create_namespace(nomad_setup):

    responses.add(
        responses.POST, "http://{ip}:{port}/v1/namespace".format(ip=common.IP, port=common.NOMAD_PORT), status=200
    )

    namespace_api = '{"Name":"api","Description":"api server namespace"}'
    namespace = json.loads(namespace_api)
    nomad_setup.namespace.create_namespace(namespace)


@responses.activate
def test_update_namespace(nomad_setup):

    responses.add(
        responses.POST, "http://{ip}:{port}/v1/namespace/api".format(ip=common.IP, port=common.NOMAD_PORT), status=200
    )

    namespace_api = '{"Name":"api","Description":"updated namespace"}'
    namespace = json.loads(namespace_api)
    nomad_setup.namespace.update_namespace("api", namespace)


@responses.activate
def test_get_namespace(nomad_setup):

    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespace/api".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json={"Name": "api", "Description": "api server namespace"},
    )

    assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]


@responses.activate
def test_delete_namespace(nomad_setup):
    responses.add(
        responses.DELETE,
        "http://{ip}:{port}/v1/namespace/api".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
    )

    nomad_setup.namespace.delete_namespace("api")


######### ENTERPRISE TEST ###########
# def test_apply_namespace(nomad_setup):
#     namespace_api='{"Name":"api","Description":"api server namespace"}'
#     namespace = json.loads(namespace_api)
#     nomad_setup.namespace.apply_namespace("api", namespace)
#     assert "api" in nomad_setup.namespace
#
# def test_get_namespace(nomad_setup):
#     assert "api" in nomad_setup.namespace.get_namespace("api")["Name"]
#
# def test_delete_namespace(nomad_setup):
#     nomad_setup.namespace.delete_namespace("api")
#     try:
#         assert "api" != nomad_setup.namespace.get_namespace("api")["Name"]
#     except nomad.api.exceptions.URLNotFoundNomadException:
#         pass
