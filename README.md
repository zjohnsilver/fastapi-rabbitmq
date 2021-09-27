# Pub/Sub RabbitMQ using FastAPI as publisher

Application to try out FastAPI and RabbitMQ

## Before Running

- Create and start a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

- Install requirements

```sh
pip install -r requirements
```

- Download and install RabbitMQ in <https://www.rabbitmq.com/download.html>

## Running

- Run the consumer using

```sh
python consumer/main.py
```

- Run the publisher using

```sh
python publisher/main.py
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
        "--max-doc-length=85",
        "--max-line-length=85",
        "--verbose"
      ],
    "files.trimFinalNewlines": true,
    "files.trimTrailingWhitespace": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "85"
    ],
    "[python]": {
      "editor.rulers": [85, 85],
      "editor.formatOnSave": true,
      "editor.formatOnPaste": false,
      "editor.formatOnSaveMode": "file"
    }
  }

```
