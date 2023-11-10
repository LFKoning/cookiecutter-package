"""Module with pre-generation cookiecutter hooks."""
import os
import shutil


print("\n\n")
print("Post-processing cookiecutter template.")

# Remove unnecessary CLI example files.
{%- if not cookiecutter.includes_cli -%}
print("Cleaning up CLI example files.")
os.remove("src/{{ cookiecutter.__package_path }}/cli.py")
{% endif %}

# Remove unnecessary data example files.
{%- if not cookiecutter.includes_data -%}
print("Cleaning up package data example files.")
os.remove("MANIFEST.in")
os.remove("src/{{ cookiecutter.__package_path }}/read_data.py")
shutil.rmtree("src/{{ cookiecutter.__package_path }}/package_data")
{% endif %}

# Create new git repo.
{%- if cookiecutter.create_git -%}
print("Setting up the git repository.")
os.system("git init -b main")

print("Adding remote: {{ cookiecutter.azure_url }}.")
os.system("git remote add origin {{ cookiecutter.azure_url }}")
{% endif %}

# Create Anaconda environment.
{%- if cookiecutter.create_conda -%}
print("Creating Anaconda environment: {{ cookiecutter.package_name }}.")
os.system(
    "conda create --yes --quiet --name {{ cookiecutter.package_name }} "
    + "python={{ cookiecutter.python_version }}"
)

print("Installing package with development dependencies.")
os.system(
    "conda activate {{ cookiecutter.package_name }} "
    + "& python -m pip install -e .[dev]"
)

# Pre-commit setup.
{%- if cookiecutter.precommit -%}

# Install pre-commit hooks.
# Note: Requires a git repository to be initialized!
{%- if cookiecutter.create_git %}
print("Installing pre-commit hooks.")
os.system("conda activate {{ cookiecutter.package_name }} & pre-commit install")
{%- else -%}
print("Cannot install pre-commit hooks; no git repository!")
print("Type `pre-commit install` in the package folder to install manually.")
{% endif %}

{%- else %}
# Remove pre-commmit config.
os.remove(".pre-commit-config.yaml")
{% endif %}

{% endif %}

print("All done!")
