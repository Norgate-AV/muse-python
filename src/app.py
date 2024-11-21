from mojo import context  # type: ignore
import cowsay  # type: ignore
from Timer import Timer


def main() -> None:
    context.log.info("Hello from muse-python!")
    context.log.info("This is a simple example of a muse-python app.")

    message: str = "Hello from muse-python!"
    say: str = cowsay.get_output_string("cow", message)

    context.log.info(f"\n{say}\n")

    timer = Timer()
    timer.start(on_tick)


def on_tick(event) -> None:
    context.log.info("Tick!")
    context.log.info(f'Timeline Sequence: {event.arguments["sequence"]}')
    context.log.info(f'Timeline Time: {event.arguments["time"]}')
    context.log.info(f'Timeline Repetition: {event.arguments["repetition"]}')


if __name__ == "__main__":
    main()

context.run(globals())
