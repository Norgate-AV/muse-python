from typing import Any, Protocol

class Devices(Protocol):
    def get(self, device: str) -> Any: ...
    def has(self, device: str) -> bool: ...
    def ids(self) -> list[str]: ...