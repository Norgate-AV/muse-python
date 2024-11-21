from mojo import context  # type: ignore
from typing import Callable


class Timer:
    def __init__(self, interval: int = 1000):
        self.timeline = context.services.get("timeline")
        self.interval = interval

    def start(self, callback: Callable[[dict], None]) -> None:
        self.timeline.expired.listen(callback)
        self.timeline.start([self.interval], False, -1)

    def end(self) -> None:
        self.timeline.stop()
