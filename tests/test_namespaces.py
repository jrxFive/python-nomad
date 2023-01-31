import tests.common as common

import pytest
import responses


# integration tests was mocked. If you have an enterprise nomad please uncomenet ##### ENTERPRISE TEST #####
@responses.activate
def test_get_namespaces(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespaces".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
            {"CreateIndex": 31, "Description": "Production API Servers", "ModifyIndex": 31, "Name": "api-prod"},
            {"CreateIndex": 5, "Description": "Default shared namespace", "ModifyIndex": 5, "Name": "default"},
        ],
    )

    assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True


@responses.activate
def test_get_namespaces_prefix(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespaces?prefix=api-".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
            {"CreateIndex": 31, "Description": "Production API Servers", "ModifyIndex": 31, "Name": "api-prod"},
        ],
    )

    assert isinstance(nomad_setup.namespaces.get_namespaces(prefix="api-"), list) == True


@responses.activate
def test_namespaces_iter(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespaces".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
            {"CreateIndex": 31, "Description": "Production API Servers", "ModifyIndex": 31, "Name": "api-prod"},
            {"CreateIndex": 5, "Description": "Default shared namespace", "ModifyIndex": 5, "Name": "default"},
        ],
    )

    assert "api-prod" in nomad_setup.namespaces


@responses.activate
def test_namespaces_len(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/namespaces".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
            {"CreateIndex": 31, "Description": "Production API Servers", "ModifyIndex": 31, "Name": "api-prod"},
            {"CreateIndex": 5, "Description": "Default shared namespace", "ModifyIndex": 5, "Name": "default"},
        ],
    )

    assert 2 == len(nomad_setup.namespaces)


###### ENTERPRISE TEST ###########

# def test_get_namespaces(nomad_setup):
#     assert isinstance(nomad_setup.namespaces.get_namespaces(), list) == True
