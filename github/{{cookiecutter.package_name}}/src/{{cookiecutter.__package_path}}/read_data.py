"""Module containing an example for reading package data."""
# Note: requires Python >= 3.7
from importlib import resources

# Import package_data as module
from {{ cookiecutter.__package_path }} import package_data


def main():
    """Main routine that reads a file from the package"""

    # Use resources read_text / read_binary to get file contents.
    # Note: Use open_text / open_binary if you need a file handle instead.
    file_content = resources.read_text(package_data, "sample.txt")
    print(file_content)


if __name__ == "__main__":
    main()
