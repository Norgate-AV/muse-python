from typing import Any, Callable, List, Protocol


class TimelineEvent(Protocol):
    arguments: dict[str, Any]


class TimelineExpired(Protocol):
    def listen(self, callback: Callable[[TimelineEvent], None]) -> None: ...


class Timeline(Protocol):
    expired: TimelineExpired

    def start(self, intervals: List[int], relative: bool, repeat: int) -> None: ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def restart(self) -> None: ...
