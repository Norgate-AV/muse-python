from timeline import Timeline
from typing import Any, Literal, overload, Protocol

class Services(Protocol):
    @overload
    def get(self, service: Literal["timeline"]) -> Timeline: ...
    @overload
    def get(self, service: str) -> Any: ...