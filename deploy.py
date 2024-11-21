#!/usr/bin/env python

import os
import json
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    username: str = os.environ.get("USERNAME", "")
    host: str = os.environ.get("HOST", "")

    if not username or not host:
        print("Please provide a username and host in the .env file.")
        exit(1)

    try:
        with open("program.json") as f:
            program: dict = json.load(f)
            name: str = program["name"]
            f.close()
    except FileNotFoundError:
        print("Please provide a program.json file.")
        exit(1)

    os.system(f"scp -r ./src {username}@{host}:/mojo/program/{name}/")
    os.system(f"scp program.json {username}@{host}:/mojo/program/{name}/")

    os.system(f"uv pip freeze > requirements.txt")
    os.system(f"scp requirements.txt {username}@{host}:/mojo/program/{name}/")

    # Restart the program
    # os.system(
    # f'ssh {username}@{host} "program:restart {program}"'
    # )  # This kills all current ssh sessions. Need to find a better way to restart the program.


if __name__ == "__main__":
    main()
