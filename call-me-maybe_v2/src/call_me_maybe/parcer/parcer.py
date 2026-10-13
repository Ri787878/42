from pydantic import BaseModel, Field
from utils import print_to_stderr
from typing import Any
import json
from pathlib import Path
import sys


class Parcer(BaseModel):
    function_definition_filepath: str = Field(default="")
    input_filepath: str = Field(default="")
    output_filepath: str = Field(default="function_calling_results.json")

    def is_valid_input(self) -> bool:
        run_command: str = " ".join(i for i in sys.argv[1:])

        if "--functions_definition" in run_command:
            self.function_definition_filepath = ""
        if "--input" in run_command:
            pass
        if "--output" in run_command:
            pass

        output_filepath = "data/output/" + sys.argv[6]
        open(output_filepath, "w")

        files: list = [
            sys.argv[2],
            sys.argv[4]]

        # Check if files exist
        file_exist_error_list: list = []
        for file in files:
            if not self.does_file_exist(file):
                file_exist_error_list.append(
                    f"[ERROR] File \"{file}\" doesn't exist.")
        if file_exist_error_list:
            for file_name in file_exist_error_list:
                print_to_stderr(file_name)
            return False

        # Check if formatted correctly
        file_formatting_error_list: list = []
        for file in files:
            if not self.is_valid_json(file):
                file_formatting_error_list.append(
                    f"[ERROR] Invalid Json formatting "
                    f"in provided file \"{file}\".")
        if file_formatting_error_list:
            for file_name in file_formatting_error_list:
                print_to_stderr(file_name)
            return False
        self.function_definition_filepath = files[0]
        self.input_filepath = files[1]
        self.output_filepath = "/data/output/function_calls.json"
        return True

    def does_file_exist(self, file: str) -> bool:
        try:
            with open(file) as f:
                _ = json.load(f)
            return True
        except FileNotFoundError:
            return False

    def is_valid_json(self, file: str) -> bool:
        try:
            with open(file) as f:
                _ = json.load(f)
            return True
        except ValueError:
            return False

    def get_arguments(self, command: list[str]) -> list[str]:
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
        parameters_list: list[tuple[str, str]] = []

        for param_name, param_def in data["parameters"].items():
            param_type: str = param_def["type"]
            parameters_list.append((param_name, param_type))
        return parameters_list

    @staticmethod
    def load_json_safely(path: str, default):
        p = Path(path)
        raw = p.read_text(encoding="utf-8").strip()
        if raw == "":
            return default
        try:
            return json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"[ERROR] Invalid JSON in {path}: {e}") from e
