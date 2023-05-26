# Backend for FreshAir processes

## How to run:

- Install dependencies: `poetry install`.
- Run server: `uvicorn app.main:app --reload`.

## Info

- Interactive API docs: http://127.0.0.1:8000/docs

## Useful Poetry commands:

- Install all dependencies: `poetry install`.
- Add new package at the latest version: `poetry add <package>`, e.g. `poetry add numpy`.
- Add package only for development: `poetry add <package> --group dev`, e.g. `poetry add black --group dev`.
- Regenerate `poetry.lock` file: `poetry lock --no-update`.
- Remove package: `poetry remove <package>`, e.g. `poetry remove numpy`.

## Lint autoformat

- `poetry run black --config black.py.toml .`

## Lint check

- `poetry run black --config black.py.toml . --check`
