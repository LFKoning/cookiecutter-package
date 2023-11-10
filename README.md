# Cookiecutter Templates for Python Packages

## Goal

The goal of this project is to provide an easy way to create a Python package. The
package template includes the following features:

- Creates package folder and file structure.
- Creates a `pyproject.toml` installation file.
- Documentation templates for `mkdocs`.
- Pre-commit hooks for code quality checks.
- Azure or GitHub CI pipelines for code quality checks.
- Optional: Examples for a Command Line Interface and package data.
- Optional: Creates a new git repository.
- Optional: Creates a new Anaconda virtual environment.

The templates are create using the `cookiecutter` package, so you need to have that
installed to be able to use these templates.

## Installation

To use these templates, you must have the `cookiecutter` package available on your
system. To install `cookiecutter` into your current Python environment, type:

```shell
python -m pip install cookiecutter
```

Or if you prefer Anaconda:

```shell
conda install cookiecutter
```

After installing `cookiecutter`, you can use these templates to kickstart your projects!

## Usage

Once you have `cookiecutter` installed, you can use the template to create a new project.
Go to the folder on your local drive where you want to create the new project and type:

```shell
cookiecutter https://github.com/LFKoning/cookiecutter-package
```

This will start `cookiecutter` and ask you for to choose from these templates:

1. Azure DevOps
2. GitHub

Select the remote git service you want to use to continue. After that `cookiecutter` will
ask you to provide additional information about your package.

If a default value is available, `cookiecutter` will display the default between square
brackets (`[..]`). Simply press `Enter` to accept the default value and continue.

*Tip: If you make an error filling in the values, you can either stop the process using
`CTRL + C` of continue and correct the mistake later on.*

### Azure DevOps

Selecting Azure DevOps creates a package tailored for this service. This will impact
the remote repository URL and CI pipeline for the package. You will be asked to provide
the following information:

|Input|Description|Example|
|---|---|---|
|`author_name`|Your first and last name.|`John Doe`|
|`author_email`|Your e-mail address.|`john.doe@gmail.com`|
|`project`|Title for your project.|`Test Project`|
|`package_name`|Name of your package.|`test-project`|
|`package_description`|Short description for your package.|`Test cookiecutter template`|
|`package_keywords`|Keywords for your package.|`cookiecutter, template, testing`|
|`azure_user`|Your username in Azure DevOps.|`john_doe`|
|`azure_project`|Project name in Azure DevOps.|`TEST`|
|`azure_repo`|Name of the project's repository.|`test-project`|
|`azure_url`|URL to the project's repository|`https://john_doe@dev.azure.com/john_Doe/TEST/_git/test_project`|
|`python_version`|The Python version you are using.|`3.9`|
|`includes_cli`|Does your project need a Command Line Interface? (y/n).|`n`|
|`includes_data`|Does your project include data files? (y/n).|`n`|
|`create_git`|Create a new git repository? (y/n).|`y`|
|`create_conda`|Create a new Anaconda environment? (y/n)|`y`|
|`precommit`|Install pre-commit hooks? (y/n).|`y`|

### GitHub

Selecting Azure DevOps creates a package tailored for this service. This will impact
the remote repository URL and CI pipeline for the package. You will be asked to provide
the following information:

|Input|Description|Example|
|---|---|---|
|`author_name`|Your first and last name.|`John Doe`|
|`author_email`|Your e-mail address.|`john.doe@gmail.com`|
|`project`|Title for your project.|`Test Project`|
|`package_name`|Name of your package.|`test-project`|
|`package_description`|Short description for your package.|`Test cookiecutter template`|
|`package_keywords`|Keywords for your package.|`cookiecutter, template, testing`|
|`github_user`|Your username on GitHub.|`JohnDoe`|
|`github_repo`|Name of the GitHub repository.|`test-project`|
|`github_url`|URL to the GitHub repository|`https://github.com/JohnDoe/test-project`|
|`python_version`|The Python version you are using.|`3.10`|
|`includes_cli`|Does your project need a Command Line Interface? (y/n).|`n`|
|`includes_data`|Does your project include data files? (y/n).|`n`|
|`create_git`|Create a new git repository? (y/n).|`y`|
|`create_conda`|Create a new Anaconda environment? (y/n)|`y`|
|`precommit`|Install pre-commit hooks? (y/n).|`y`|

## Package creation

After filling in the information, you should see a new folder with your package's
name in your working directory. This folder contains the folder structure and files for
your newly created package.

Depending on the choices you made, `cookiecutter` will have also:

1. Initialized a new git repository with the remote set to Azure DevOps or GitHub.
2. Created a new Anaconda environment with the same name as your package.
3. Installed your package including development dependencies (editable).
4. Installed the pre-commit hooks for isort, black, pylint, et cetera.

So you should be all good to go; good luck!

## Manually setting up

If you chose to skip setting up git or an Anaconda environmant, you should perform
these steps manually:

1. Initialize a new git repository: `git init -b main`
2. Set git remote: `git remote add origin <repository URL>`
3. Create Anaconda environment: `conda create -n <package name> python=<python version>`
4. Install your package: `python -m pip install -e . [dev, docs]`
5. Install pre-commit hooks: `pre-commit install`

## Contributing

If you want to contribute to this project, feel free to clone the code, make
improvements and open a pull request!

If you have suggestions or remarks not directly related to the project's code or
documentation, feel free to e-mail the authors.

## Maintainers

This project is maintained by:

1. Lukas Koning (lfkoning@gmail.com)
