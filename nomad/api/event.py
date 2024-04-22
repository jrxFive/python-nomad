"""Nomad Events: https://developer.hashicorp.com/nomad/api-docs/events"""

import json
import threading
import queue

import requests

from nomad.api.base import Requester


class Event:
    """
    Nomad Event
    """

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return f"{self.__dict__}"

    def __getattr__(self, item):
        raise AttributeError

    def __init__(self, **kwargs):
        self.stream = stream(**kwargs)


# backward compatibility
class stream(Requester):  # pylint: disable=invalid-name
    """
    The /event/stream endpoint is used to stream events generated by Nomad.

    https://www.nomadproject.io/api-docs/events
    """

    ENDPOINT = "event/stream"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_stream(
        self, method, params, timeout, event_queue, exit_event
    ):  # pylint: disable=too-many-arguments
        """
        Used as threading target, to obtain json() value
        Args:
            method:
            params:
            timeout:
            event_queue:
            exit_event:
        """

        while exit_event.is_set() is False:
            try:
                with self.request(
                    method=method, params=params, timeout=timeout, stream=True
                ) as resp:
                    for raw_msg in resp.iter_lines():
                        msg = json.loads(raw_msg)

                        # don't send heartbeats
                        if msg:
                            event_queue.put(msg)

                        if exit_event.is_set():
                            return

            except requests.exceptions.ConnectionError:
                continue

    def get_stream(
        self, index=0, topic=None, namespace=None, event_queue=None, timeout=None
    ):  # pylint: disable=too-many-arguments
        """
        Usage:
            stream, stream_exit_event, events = n.event.stream.get_stream()
            stream.start()

            while True:
                event = events.get()
                print(event)
                events.task_done()

        Args:
            index: (int),  Specifies the index to start streaming events from. If the requested index is no longer
                in the buffer the stream will start at the next available index.

            topic: (None or dict), Specifies a topic to subscribe to and filter on.
                The default is to subscribe to all topics.
                Multiple topics may be specified by passing multiple topic parameters.
                A valid topic parameter includes a topic type and an optional filter_key separated by a colon :.
                As an example ?topic=Deployment:redis would subscribe to all Deployment events for a job redis.
                an additional topic &topic=Deployment:web would include deployment events for redis and web.
                To only subscribe to Node events a topic parameter of ?topic=Node without a separator value
                would be used. ?topic=Node:* is also valid.

            namespace: (str) Specifies the target namespace to filter on. Specifying * includes all namespaces
                for event types that support namespaces.

            event_queue: (None or queue.Queue) for thread listener to push events onto.

            timeout: (None or int), override timeout (seconds) so connection is not closed.
                Defaults to timeout in constructor if not given.

        Returns: (threading.Thread), (threading.Event) (queue.Queue)
        """

        params = {
            "index": index,
        }

        if namespace:
            params["namespace"] = namespace

        if topic:
            params["topic"] = topic

        if event_queue is None:
            event_queue = queue.Queue()

        stream_exit_event = threading.Event()
        _stream = threading.Thread(
            name="python-nomad-event-stream",
            target=self._get_stream,
            kwargs={
                "method": "get",
                "params": params,
                "timeout": timeout,
                "event_queue": event_queue,
                "exit_event": stream_exit_event,
            },
        )

        return _stream, stream_exit_event, event_queue
