"""The main module for the write-right application."""

import argparse
import os.path


def _main():
    arguments = _parse_command_line()
    content = _read_file(arguments.file)
    print(content)


def _parse_command_line() -> argparse.Namespace:
    """
    Parse the command line arguments.

    :return: The parsed command line arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Analyze a document for common writing mistakes such as passive voice, violations of Strunk & White, etc.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "file", help="The path to the root file to read.",
    )
    arguments = parser.parse_args()
    arguments.file = os.path.expanduser(arguments.file)
    return arguments


def _read_file(file_path: str):
    """
    Read a file into an array of lines.

    :param str file_path: The path to the file to open.
    :return: The contents of the file as a list of strings. Each line is one entry in the list.
    :rtype: list of str
    """
    with open(file_path, "r") as file_stream:
        content = file_stream.readlines()
    return content


if __name__ == "__main__":
    _main()
