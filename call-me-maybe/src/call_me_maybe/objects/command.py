from llm_sdk import Small_LLM_Model
from pydantic import BaseModel, Field, model_validator
from .function_definition import Function_definition
from .prompts import Prompt
from ..parcer import Parcer
from utils import print_to_stderr
from pathlib import Path


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
        flag1 = not Path(self.function_definition_filepath).exists()
        flag2 = not Path(self.input_filepath).exists()

        if flag1:
            print_to_stderr(
                f"[ERROR] File '{self.function_definition_filepath}' "
                f"does not exist.")

        if flag2:
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
        elif flag2:
            print_to_stderr("[SYSTEM] Missing Input File.")
            return False

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
        if (
            self.function_definition_filepath == self.input_filepath
            or self.function_definition_filepath == self.output_filepath
            or self.input_filepath == self.output_filepath
        ):
            print_to_stderr(
                "[ERROR] Same file location used for multiple inputted files.")
            exit()

    def ingest_prompts(self) -> None:
        data = Parcer.load_json_safely(self.input_filepath, default=[])
        if not isinstance(data, list):
            raise ValueError(
                f"[ERROR] Expected JSON array in {self.input_filepath}")

        for item in data:
            self.prompts_list.append(Prompt(prompt=item["prompt"]))

    def ingest_function_definitions(self) -> None:
        data = Parcer.load_json_safely(
            self.function_definition_filepath,
            default=[])

        if not isinstance(data, list):
            raise ValueError(
                f"[ERROR] Expected JSON array in "
                f"{self.function_definition_filepath}")

        for func_def in data:
            parameters_list: list[tuple[str, str]] = []
            parameters_list = Parcer.get_parameters_list(func_def)
            func_def = Function_definition(
                name=func_def['name'],
                description=func_def['description'],
                parameters=parameters_list,
                returns=func_def['returns']['type'])

            self.func_definition_list.append(func_def)

    def run(self, llm_model: Small_LLM_Model) -> None:
        """Runs the project itself based on provided arguments."""
        # print(f"\nfunc_definition_list = {self.func_definition_list}")
        # print(f"\nprompts_list = {self.prompts_list}")
        print("\n\n")

        encoded_prompt_tensor = llm_model.encode(self.prompts_list[0].prompt)
        # encoded_prompt: list[int] = [
        #     int(x) for x in encoded_prompt_tensor.flatten().tolist()]

        # logits_produced = llm_model.get_logits_from_input_ids(encoded_prompt)

        # print(f"encoded_prompt = {encoded_prompt}\n")
        # print(f"logits_produced = {logits_produced}")

        input_ids: list[int] = [
            int(x) for x in encoded_prompt_tensor.flatten().tolist()]
        max_new_tokens = 50
        eos_token_id = getattr(llm_model, "eos_token_id", None)

        for _ in range(max_new_tokens):
            # logits for current context
            logits = llm_model.get_logits_from_input_ids(input_ids)

            # if logits is [vocab], use directly; if [seq, vocab],
            # take last row
            if isinstance(logits[0], list):
                next_token_logits = logits[-1]
            else:
                next_token_logits = logits

            next_token_id = max(
                range(
                    len(next_token_logits)),
                key=lambda i: next_token_logits[i]
                )  # argmax
            input_ids.append(next_token_id)

            if eos_token_id is not None and next_token_id == eos_token_id:
                break

        # decode full sequence (or only newly generated tail)
        generated_text = llm_model.decode(input_ids)
        with open(self.output_filepath, "w") as f:
            f.write(generated_text)
        print(generated_text)

