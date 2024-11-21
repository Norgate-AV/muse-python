# muse-python

This is a test project to test the integration of Muse with Python.

## Installation

The project uses [uv](https://docs.astral.sh/uv/) to manage the development environment. You can install it with `brew install uv`.

```bash
uv sync
```

This will create a virtual environment and install the dependencies.

## Environment Setup

You need to create a `.env` file in the root of the project with the following content:

```bash
USERNAME=your-username
HOST=your-host
```

This will be used to deploy the changes to the Muse processor.

## Deploy

```bash
./deploy.py
```

## LICENSE

[MIT](./LICENSE)
