from mojo import context  # type: ignore
import cowsay  # type: ignore


def main() -> None:
    context.log.info("Hello from muse-python!")
    context.log.info("This is a simple example of a muse-python app.")

    message: str = "Hello from muse-python!"
    say: str = cowsay.get_output_string("cow", message)

    context.log.info(f"\n{say}\n")


if __name__ == "__main__":
    main()

context.run(globals())
