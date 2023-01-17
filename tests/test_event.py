import json

from flaky import flaky


# integration tests requires nomad Vagrant VM or Binary running
def test_register_job(nomad_setup):

    with open("example.json") as fh:
        job = json.loads(fh.read())
        nomad_setup.job.register_job("example", job)
        assert "example" in nomad_setup.job


@flaky(max_runs=5, min_passes=1)
def test_get_event_stream_default(nomad_setup):

    stream, stream_exit, events = nomad_setup.event.stream.get_stream()
    stream.daemon = True
    stream.start()

    test_register_job(nomad_setup)
    event = events.get(timeout=5)
    assert event
    assert "Index" in event

    stream_exit.set()


@flaky(max_runs=5, min_passes=1)
def test_get_event_stream_with_customized_topic(nomad_setup):
    stream, stream_exit, events = nomad_setup.event.stream.get_stream(topic={"Node": "*"})
    stream.daemon = True
    stream.start()

    node_id = nomad_setup.nodes.get_nodes()[0]["ID"]
    nomad_setup.node.drain_node_with_spec(node_id, None)

    event = events.get(timeout=5)
    assert event
    assert "Index" in event
    assert event["Events"][0]["Type"] in (
        "NodeRegistration",
        "NodeDeregistration",
        "NodeEligibility",
        "NodeDrain",
        "NodeEvent",
    )

    stream_exit.set()
