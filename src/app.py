from mojo import context  # type: ignore
import cowsay  # type: ignore
from Timer import Timer
from utils import get_ip


def main() -> None:
    context.log.info("Hello from muse-python!")

    message: str = f"Your IP address is: {get_ip()}"
    say: str = cowsay.get_output_string("cow", message)

    context.log.info(f"\n{say}\n")

    timer = Timer()
    timer.start(on_tick)


def on_tick(event) -> None:
    context.log.info(f'Timeline Sequence: {event.arguments["sequence"]}')
    context.log.info(f'Timeline Time: {event.arguments["time"]}')
    context.log.info(f'Timeline Repetition: {event.arguments["repetition"]}')


if __name__ == "__main__":
    main()

context.run(globals())
