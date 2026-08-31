from llm_sdk import Small_LLM_Model
from call_me_maybe import Parcer, Command, Values
from pydantic import ValidationError
from utils import print_to_stderr
import sys


def main() -> None:
    try:
        project_values = Values()
        parcer = Parcer()
        llm_model = Small_LLM_Model()

        arguments: list[str] = parcer.get_arguments(sys.argv)

        cmd = Command(
            arguments=arguments,
            llm_model=llm_model,
            project_values=project_values
        )

        cmd.run()

        # llm_model.

    except ValidationError as exc:
        print_to_stderr(exc)
