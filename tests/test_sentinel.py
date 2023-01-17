import tests.common as common

import json
import responses


# integration tests was mocked.
@responses.activate
def test_list_policies(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/sentinel/policies".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json=[
            {
                "Name": "foo",
                "Description": "test policy",
                "Scope": "submit-job",
                "EnforcementLevel": "advisory",
                "Hash": "CIs8aNX5OfFvo4D7ihWcQSexEJpHp+Za+dHSncVx5+8=",
                "CreateIndex": 8,
                "ModifyIndex": 8,
            }
        ],
    )

    policies = nomad_setup.sentinel.get_policies()
    assert isinstance(policies, list)
    assert "foo" in nomad_setup.sentinel.get_policies()[0]["Name"]


@responses.activate
def test_create_policy(nomad_setup):

    responses.add(
        responses.POST,
        "http://{ip}:{port}/v1/sentinel/policy/my-policy".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
    )

    policy_example = '{"Name": "my-policy", "Description": "This is a great policy", "Scope": "submit-job", "EnforcementLevel": "advisory", "Policy": "main = rule { true }"}'
    json_policy = json.loads(policy_example)
    nomad_setup.sentinel.create_policy(id_="my-policy", policy=json_policy)


@responses.activate
def test_update_policy(nomad_setup):

    responses.add(responses.POST, f"http://{common.IP}:{common.NOMAD_PORT}/v1/sentinel/policy/my-policy", status=200)

    policy_example = '{"Name": "my-policy", "Description": "Update", "Scope": "submit-job", "EnforcementLevel": "advisory", "Policy": "main = rule { true }"}'
    json_policy = json.loads(policy_example)
    nomad_setup.sentinel.update_policy(id_="my-policy", policy=json_policy)


@responses.activate
def test_get_policy(nomad_setup):
    responses.add(
        responses.GET,
        "http://{ip}:{port}/v1/sentinel/policy/foo".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json={
            "Name": "foo",
            "Description": "test policy",
            "Scope": "submit-job",
            "EnforcementLevel": "advisory",
            "Policy": "main = rule { true }\n",
            "Hash": "CIs8aNX5OfFvo4D7ihWcQSexEJpHp+Za+dHSncVx5+8=",
            "CreateIndex": 8,
            "ModifyIndex": 8,
        },
    )

    policy = nomad_setup.sentinel.get_policy("foo")
    assert "advisory" in policy["EnforcementLevel"]


@responses.activate
def test_delete_policy(nomad_setup):
    responses.add(
        responses.DELETE,
        "http://{ip}:{port}/v1/sentinel/policy/my-policy".format(ip=common.IP, port=common.NOMAD_PORT),
        status=200,
        json={
            "Name": "foo",
            "Description": "test policy",
            "Scope": "submit-job",
            "EnforcementLevel": "advisory",
            "Policy": "main = rule { true }\n",
            "Hash": "CIs8aNX5OfFvo4D7ihWcQSexEJpHp+Za+dHSncVx5+8=",
            "CreateIndex": 8,
            "ModifyIndex": 8,
        },
    )

    nomad_setup.sentinel.delete_policy(id_="my-policy")
