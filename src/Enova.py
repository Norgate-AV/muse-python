from mojo import context  # type: ignore
from typing import List

MAX_OUTPUTS = 16
MAX_LEVELS = 3

LEVELS = ["VIDEO", "AUDIO", "ALL"]


class Enova:
    __timeline = context.services.get("timeline")

    __pending: List[List[bool]] = [
        [False for _ in range(MAX_OUTPUTS)] for _ in range(MAX_LEVELS)
    ]

    __output: List[List[int]] = [
        [0 for _ in range(MAX_OUTPUTS)] for _ in range(MAX_LEVELS)
    ]

    __busy: bool = False

    def __init__(self):
        self.__init()

    def __init(self) -> None:
        self.__timeline.expired.listen(self.__tick)
        self.__timeline.start([100], False, -1)

    def __tick(self, _) -> None:
        for i in range(MAX_OUTPUTS):
            for j in range(MAX_LEVELS):
                if not self.__pending[j][i] or self.__busy:
                    continue

                self.__busy = True
                self.__pending[j][i] = False
                self.__send(self.__get_command(self.__output[j][i], i, j))

    def __send(self, payload: str) -> None:
        context.log.info(f"Sending command: {payload}")
        self.__busy = False

    def __get_command(self, output: int, input: int, level: int) -> str:
        return f"CL{LEVELS[level]}I{input}O{output}"

    def switch(self, input: int, output: int, level: int) -> None:
        self.__output[level][input] = output
        self.__pending[level][input] = True
