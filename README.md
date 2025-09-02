# service-library-sample

A tiny example Python package scaffolded for Poetry.

Quick commands:

Install dependencies and create venv (requires Poetry):

```bash
poetry install
poetry shell
```

Run tests (using pytest if installed, otherwise unittest):

```bash
poetry run pytest
# or
python -m unittest
```

Usage example:

```python
from service_library import greet

print(greet("World"))
```
