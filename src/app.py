from mojo import context # type: ignore

def main():
    context.log.info("Hello from muse-python!")

if __name__ == "__main__":
    main()

context.run(globals())