from typing import Protocol

class Log(Protocol):
    def debug(self, *args: str) -> None: ...
    def info(self, *args: str) -> None: ...
    def warning(self, *args: str) -> None: ...
    def error(self, *args: str) -> None: ...
