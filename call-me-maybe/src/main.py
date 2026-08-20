from src.parcer import Parcer, Command
from pydantic import ValidationError
from utils import print_to_stderr
import sys


def main() -> None:
    try:
        parcer = Parcer()

        arguments: list[str] = parcer.get_arguments(sys.argv)

        cmd = Command(arguments=arguments)

        cmd.run()

    except ValidationError as exc:
        print_to_stderr(exc)
