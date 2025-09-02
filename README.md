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

## Snyk scans — before and after

Before (original PyPI dependency graph):

```
Testing /home/shakti/Projects/snyk_issues/service-library...

Tested 25 dependencies for known issues, found 5 issues, 49 vulnerable paths.

Issues to fix by upgrading dependencies:

	✗ Arbitrary Code Execution [Critical] in jsonpickle@1.4.2
		introduced by service-library-sample@0.1.0 > botbuilder-azure@4.16.2 > jsonpickle@1.4.2
		(fix: jsonpickle@3.3.0)

...other findings omitted for brevity...
```

After (using forked `botbuilder-azure` from https://github.com/srinadha-reddy/botbuilder-python):

```
Testing /home/shakti/Projects/snyk_issues/service-library...

Tested 25 dependencies for known issues, found 4 issues, 48 vulnerable paths.

Issues to fix by upgrading dependencies:

	✗ Information Exposure [Medium] in azure-storage-blob@12.7.0
		introduced by botbuilder-azure@4.17.0 > azure-storage-blob@12.7.0

	✗ Missing Report of Error Condition [Medium] in cryptography@43.0.3
		introduced by botbuilder-azure@4.17.0 > azure-storage-blob@12.7.0 > cryptography@43.0.3

	✗ Open Redirect [Medium] in urllib3@2.2.3
		introduced by botbuilder-azure@4.17.0 > botbuilder-schema@4.17.0 > urllib3@2.2.3

Note: the jsonpickle arbitrary-code-execution finding (SNYK-PYTHON-JSONPICKLE-8136229) is no longer reported after using the forked package which includes the updated dependency set.
```
