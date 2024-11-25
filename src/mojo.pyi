# mojo.pyi

from typing import Any, Callable, List, Literal, overload, Protocol

class Devices(Protocol):
    def get(self, device: str) -> Any: ...
    def has(self, device: str) -> bool: ...
    def ids(self) -> list[str]: ...

class Log(Protocol):
    def debug(self, *args: str) -> None: ...
    def info(self, *args: str) -> None: ...
    def warning(self, *args: str) -> None: ...
    def error(self, *args: str) -> None: ...

class Timeline(Protocol):
    expired: TimelineExpired

    def start(self, intervals: List[int], relative: bool, repeat: int) -> None: ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def restart(self) -> None: ...

class TimelineExpired(Protocol):
    def listen(self, callback: Callable) -> None: ...

class Services(Protocol):
    @overload
    def get(self, service: Literal["timeline"]) -> Timeline: ...
    @overload
    def get(self, service: str) -> Any: ...

class context:
    """Type hints for the mojo.context"""

    devices: Devices
    log: Log
    services: Services

    @staticmethod
    def run(globals: dict[str, Any]) -> None: ...

__all__ = ["context"]
