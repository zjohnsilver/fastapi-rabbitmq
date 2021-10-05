# Pub/Sub RabbitMQ using FastAPI as publisher

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Application to try out FastAPI and RabbitMQ

## Before Running

- Create and start a virtual environment

```sh
poetry shell
```

- Install requirements

```sh
poetry install
```

- Download and install RabbitMQ in <https://www.rabbitmq.com/download.html>

## Running

- Run the consumer using

```sh
python consumer/main.py
```

- Run the publisher using

```sh
uvicorn publisher.main:app --reload
```

## Settings

- Settings to use in VS Code:

```json
  {
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--ignore=E24,W504,W503,E203",
        "--select=C,E,F,W,B,B9",
        "--exclude=.git,__pycache__,__init__.py,.mypy_cache,.pytest_cache",
        "--indent-size=4",
        "--max-doc-length=79",
        "--max-line-length=79",
        "--verbose"
      ],
    "files.trimFinalNewlines": true,
    "files.trimTrailingWhitespace": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "79"
    ],
    "[python]": {
      "editor.rulers": [79, 79],
      "editor.formatOnSave": true,
      "editor.formatOnPaste": false,
      "editor.formatOnSaveMode": "file"
    }
  }

```
