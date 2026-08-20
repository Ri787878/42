from pydantic import BaseModel, Field, model_validator
# from llm_sdk.llm_sdk import Small_LLM_Model
from call_me_maybe import Prompt, Function_definition
from utils import print_to_stderr
from parcer.parcer import Parcer
from pathlib import Path
import json


class Command(BaseModel):
    arguments: list[str] = Field()
    prompts_list: list[Prompt] = Field(default=[])
    func_definition_list: list[Function_definition] = Field(default=[])
    function_definition_filepath: str = Field(
        default="data/input/functions_definition.json")
    input_filepath: str = Field(
        default="data/input/function_calling_tests.json")
    output_filepath: str = Field(
        default="data/output/function_calling_results.json")

    @model_validator(mode="after")
    def validate_files(self) -> "Command":
        # Change files to the Custom ones
        self.change_default_filepaths()

        if not self.do_files_exist():
            exit()

        self.create_output_file()

        self.ingest_prompts()

        self.ingest_function_definitions()

        return self

    def do_files_exist(self) -> bool:
        """Validate if files exist"""
        flag1: bool = False
        flag2: bool = False
        if not Path(self.function_definition_filepath).exists():
            flag1 = True
            print_to_stderr(
                f"[ERROR] File '{self.function_definition_filepath}' "
                f"does not exist.")

        if not Path(self.input_filepath).exists():
            flag2 = True
            print_to_stderr(
                f"[ERROR] File '{self.input_filepath}' "
                f"does not exist.")
        if flag1 and flag2:
            print_to_stderr(
                "[SYSTEM] Missing Function_Defenitions and Input Files.")
            return False
        elif flag1:
            print_to_stderr("[SYSTEM] Missing Function_Defenitions File.")
            return False
        elif flag1 and flag2:
            print_to_stderr("[SYSTEM] Missing Input File.")
            return False
        else:
            print(
                "[SYSTEM] Function_Definitions File Exist.\n"
                "[SYSTEM] Input File Exist.\n")
        return True

    def create_output_file(self) -> None:
        """Create the Output Folder(s) and File"""
        folders_to_create: list[str] = []

        _, reversed_directory_path = self.output_filepath[::-1].split("/", 1)

        while reversed_directory_path.find("/") > 0:
            folder_name, reversed_directory_path = (
                reversed_directory_path.split("/", 1))

            folders_to_create.append(folder_name[::-1])

        folders_to_create.append(reversed_directory_path[::-1])

        current_path: str = ""
        for folder in reversed(folders_to_create):
            current_path += folder + "/"
            try:
                Path(current_path).mkdir()
                print(
                    f"[SYSTEM] Directory '{current_path}' "
                    f"created successfully.")
            except FileExistsError:
                print_to_stderr(
                    f"[WARNING] Directory '{current_path}' already exists.")
            except PermissionError:
                print_to_stderr(
                    f"[ERROR] Permission denied: "
                    f"Unable to create '{current_path}'.")
            except Exception as e:
                print_to_stderr(
                    f"[ERROR] An error occurred: {e}")

        with open(self.output_filepath, "a") as f:
            f.truncate()
            print("[SYSTEM] Output File Created.")

    def change_default_filepaths(self):
        """Change the default filepath to custum ones."""
        for arg in self.arguments:
            _, filepath = arg.split()
            if arg.startswith("--functions_definition"):
                self.function_definition_filepath = filepath
            elif arg.startswith("--input"):
                self.input_filepath = filepath
            elif arg.startswith("--output"):
                self.output_filepath = filepath
        else:
            pass

    def ingest_prompts(self) -> None:
        with open(self.input_filepath, "r") as file:
            data = json.load(file)
            i: int = 0
            while i < len(data):
                prompt = Prompt(prompt=data[i]['prompt'])
                self.prompts_list.append(prompt)
                i += 1

    def ingest_function_definitions(self) -> None:
        with open(self.function_definition_filepath, "r") as file:
            data = json.load(file)

            for func_def in data:
                parameters_list: list[tuple[str, str]] = []
                parameters_list = Parcer.get_parameters_list(func_def)

                func_def = Function_definition(
                    name=func_def['name'],
                    description=func_def['description'],
                    parameters=parameters_list,
                    returns=func_def['returns']['type'])

                self.func_definition_list.append(func_def)

    def run(self):
        """print(
            f"\nfuncitons_definition filepath = "
            f"{self.function_definition_filepath}"
            f"\ninput filepath = {self.input_filepath}"
            f"\noutput filepath = {self.output_filepath}")"""
        print(f"\nfunc_definition_list = {self.func_definition_list}")
        print(f"\nprompts_list = {self.prompts_list}")
        # llm = Small_LLM_Model()
        pass
