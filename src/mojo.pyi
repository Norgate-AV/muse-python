from types.devices import Devices
from types.log import Log
from types.services import Services
from typing import Any

class context:
    devices: Devices
    log: Log
    services: Services

    @staticmethod
    def run(globals: dict[str, Any]) -> None: ...

__all__ = ["context"]
