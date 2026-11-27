from pydantic import BaseModel, Field
from utils import print_to_stderr
from typing import Any
import json
from pathlib import Path


class Parcer(BaseModel):
    """Class that holds all the parcer logic of the program."""
    function_definition_filepath: str = Field(default="")
    input_filepath: str = Field(default="")
    output_filepath: str = Field(default="function_calling_results.json")

    def get_arguments(self, command: list[str]) -> list[str]:
        """
        Function extract all the parameters passed when running the program.
        """
        arguments: list[str] = []
        for i in range(len(command)):
            if (command[i].startswith("--") and i + 1 >= len(command)):
                print_to_stderr(
                    f"[ERROR] Flag \"{command[i]}\" has no argument.")
                return arguments
            elif (
                 command[i].startswith("--")
                 and command[i + 1].startswith("--")):
                print_to_stderr(
                    f"[ERROR] Flag \"{command[i]}\" has no argument.")
                continue
            elif command[i].startswith("--"):
                arguments.append(command[i] + " " + command[i + 1])
                i += 1
            i += 1

        return arguments

    @staticmethod
    def get_parameters_list(data: Any) -> list[tuple[str, str]]:
        """
        Function creates and returns a list of all the parameters.
        """
        parameters_list: list[tuple[str, str]] = []

        for param_name, param_def in data["parameters"].items():
            param_type: str = param_def["type"]
            parameters_list.append((param_name, param_type))
        return parameters_list

    @staticmethod
    def load_json_safely(path: str, default: Any) -> Any:
        """Function loads a json safely catching errors if needed."""
        p = Path(path)
        raw = p.read_text(encoding="utf-8").strip()
        if raw == "":
            return default
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"[ERROR] Invalid JSON in {path}: {e}") from e
