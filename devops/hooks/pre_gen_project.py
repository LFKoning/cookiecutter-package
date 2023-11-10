"""Module with pre-generation cookiecutter hooks."""
import re
import sys


user_input = {
    "project": {
        "value": "{{ cookiecutter.project }}",
        "pattern": r"^[a-zA-Z][a-zA-Z0-9\-_\s]+$",
    },
    "package_name": {
        "value": "{{ cookiecutter.package_name }}",
        "pattern": r"^[a-z][a-z0-9\-]+$",
    },
    "azure_user": {
        "value": "{{ cookiecutter.azure_user }}",
        "pattern": r"^[a-zA-Z\-_]+$",
    },
    "azure_repo": {
        "value": "{{ cookiecutter.azure_repo }}",
        "pattern": r"^[a-zA-Z][a-zA-Z0-9\-_]+$",
    },
    "azure_project": {
        "value": "{{ cookiecutter.azure_project }}",
        "pattern": r"^[^_.][^:/\\~&%;@'\"?<>|#$*}{,+=[\]]+[^.]$",
    },
    "azure_url": {
        "value": "{{ cookiecutter.azure_url }}",
        "pattern": r"^https://[a-zA-Z\-_]+@dev.azure.com/[a-zA-Z\-_]+/[a-zA-Z][a-zA-Z0-9\-_]+/_git/[a-zA-Z][a-zA-Z0-9\-_]+$",
    },
}

# Check sanity of the inputs
for field, check in user_input.items():
    if not re.match(check["pattern"], check["value"]):
        print(f"ERROR: Input {field!r} contains invalid characters: {check['value']!r}!")
        sys.exit(1)
