## Event

## Event Stream

This will setup an event stream. To avoid blocking and having more control to the user it will return a
tuple of (threading.Thread, threading.Event and queue.Queue). You can use your own `queue.Queue` if you want
to use LIFO or SimpleQueue or simply extend upon that.

### Default
Will listen to all topics

```
import nomad
n = nomad.Nomad()

stream, stream_exit_event, events = n.event.stream.get_stream()
stream.start()

while True:
    event = events.get()
    print(event)
    events.task_done()
```

### Set Index, Namespace and Topic(s) of Interest

```
import nomad
n = nomad.Nomad("0.0.0.0")

stream, stream_exit_event, events = n.event.stream.get_stream(index=0, topic={"Node": "*"}, namespace="not-default")
stream.start()

while True:
    event = events.get()
    print(event)
    events.task_done()
```

### Cancel thread/Optimistically exit
We will use the `stream_exit_event` to get the thread to return/exit gracefully. This isn't immediate
as we have to wait for an event or set an arbitrary timeout value to close/open the connection again.

In this example we will set `stream_exit_event` right before the timeout, knowing that it needs to re-establish
the connection to the stream. Using a try/except with queue.Queue.get(timeout=<VALUE>) we will check if the thread
is still alive; if it isn't we break the loop.

```
import nomad
import threading
import time
import queue


def stop_stream(exit_event, timeout):
    print("start sleep")
    time.sleep(timeout)
    print("set exit event")
    exit_event.set()


n = nomad.Nomad("0.0.0.0")

stream, stream_exit_event, events = n.event.stream.get_stream(index=0, topic={"Node": "*"}, timeout=3.2)
stream.start()

stop = threading.Thread(target=stop_stream, args=(stream_exit_event, 3.0))
stop.start()

while True:
    if not stream.is_alive():
        print("not alive")
        break

    try:
        event = events.get(timeout=1.0)
        print(event)
        events.task_done()
    except queue.Empty:
        continue
```