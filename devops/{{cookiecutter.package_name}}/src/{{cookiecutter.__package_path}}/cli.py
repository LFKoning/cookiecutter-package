"""Module containing a very basic CLI example."""
import argparse


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser("CLI example")
    parser.add_argument(
        "-n", "--name", default="John Doe", type=str, help="Please enter your name"
    )
    return parser.parse_args()


def main():
    """Command line routine"""
    args = parse_arguments()
    print(f"Hello, {args.name} and welcome to this CLI example!")


if __name__ == "__main__":
    main()
