from llm_sdk import Small_LLM_Model
from call_me_maybe import Parcer, Command
from pydantic import ValidationError
from utils import print_to_stderr
import sys


def main() -> None:
    try:
        parcer = Parcer()
        llm_model = Small_LLM_Model()

        arguments: list[str] = parcer.get_arguments(sys.argv)

        cmd = Command(arguments=arguments)

        cmd.run(llm_model)

    except ValidationError as exc:
        print_to_stderr(exc)
