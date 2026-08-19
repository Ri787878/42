import sys


def print_to_stderr(*a):
    """Print a message to stderr"""
    print(*a, file=sys.stderr)
