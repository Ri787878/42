from llm_sdk import Small_LLM_Model
from call_me_maybe import Parcer, Command, Values
from pydantic import ValidationError
from utils import write_error
import sys
import time


def main() -> None:
    cmd = None

    try:
        project_values = Values()
        parcer = Parcer()
        start = time.perf_counter()
        llm_model = Small_LLM_Model()
        print(f"Model loading took {time.perf_counter() - start:.2f}s")

        arguments: list[str] = parcer.get_arguments(sys.argv)

        cmd = Command(
            arguments=arguments,
            llm_model=llm_model,
            project_values=project_values
        )

        cmd.run()

    except ValidationError as exc:
        output_filepath = (
            cmd.output_filepath
            if cmd is not None
            else "function_calling_results.json"
        )
        write_error(output_filepath, exc)
        sys.exit(1)

    except (ValueError, StopIteration) as exc:
        output_filepath = (
            cmd.output_filepath
            if cmd is not None
            else "function_calling_results.json"
        )
        write_error(output_filepath, exc)
        sys.exit(1)
