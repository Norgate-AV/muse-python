import os
import json
from dotenv import load_dotenv


def main():
    load_dotenv()

    username = os.environ.get("USERNAME")
    host = os.environ.get("HOST")

    with open("program.json") as f:
        program = json.load(f)
        name = program["name"]
        f.close()

    os.system(f"scp -r ./src {username}@{host}:/mojo/program/{name}/")
    os.system(f"scp program.json {username}@{host}:/mojo/program/{name}/")

    os.system(f"uv pip freeze > requirements.txt")
    os.system(f"scp requirements.txt {username}@{host}:/mojo/program/{name}/")


if __name__ == "__main__":
    main()
