import json
import sys


def print_to_stderr(*a: object) -> None:
    """Print a message to stderr"""
    print(*a, file=sys.stderr)


def write_error(output_filepath: str, exc: Exception) -> None:
    """Writes an error in the terminal and in a given file."""
    error_message = str(exc) or exc.__class__.__name__

    with open(output_filepath, "w", encoding="utf-8") as output_file:
        json.dump(
            {"error": error_message},
            output_file,
            indent=2,
        )
        output_file.write("\n")
