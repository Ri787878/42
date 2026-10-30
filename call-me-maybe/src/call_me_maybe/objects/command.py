from utils import (
    print_to_stderr,
    softmax,
    decoding_strategy,
    extract_last_position_if_needed
)
from pydantic import BaseModel, Field, model_validator, ConfigDict
from .prompts import Prompt
from ..parcer import Parcer
from ..contained_decoding.function_calling import (
        FunctionCallResult,
        parse_function_call,
        validate_parameter_types,
        normalize_parameter_types,
        normalize_substitution_regex
    )
from ..contained_decoding.json_validator import (
        BasicJsonFSM,
        apply_json_mask,
        load_vocab_from_model,
)
# from .generator import Generator
from ..values import Values
# from ..contained_decoding import BasicJsonFSM, load_vocab_from_model
from .function_definition import Function_definition
from llm_sdk import Small_LLM_Model
from pathlib import Path
import numpy as np
import json
import time


class Command(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    vocab: dict[str, int] = Field(default_factory=dict)
    arguments: list[str] = Field(default_factory=list)
    llm_model: Small_LLM_Model = Field()
    project_values: Values = Field()
    response: str = Field(default="")
    prompts_list: list[Prompt] = Field(default_factory=list)
    func_definition_list: list[Function_definition] = Field(
        default_factory=list)
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

    def _generate_function_call(
        self,
        prompt: str,
        feedback: str = "",
        max_tokens: int = 80,
    ):
        start = time.perf_counter()
        generation_prompt = FunctionCallResult.build_generation_prompt(
            prompt,
            self.func_definition_list,
        )

        if feedback:
            generation_prompt += (
                "\nThe previous response was invalid.\n"
                f"Validation error: {feedback}\n"
                "Generate a corrected JSON object now:\n"
            )

        input_ids_tensor = self.llm_model.encode(generation_prompt)
        input_ids = [
            int(token_id)
            for token_id in input_ids_tensor.flatten().tolist()
        ]

        json_fsm = BasicJsonFSM(self.vocab)

        generated_token_ids: list[int] = []

        for _ in range(max_tokens):
            logits = self.llm_model.get_logits_from_input_ids(input_ids)
            logits = np.asarray(logits, dtype=float)

            masked_logits = apply_json_mask(logits, json_fsm)

            if not np.isfinite(masked_logits).any():
                raise ValueError(
                    "The model produced no valid token for the JSON response."
                )

            next_token_id = int(np.argmax(masked_logits))

            json_fsm.update_state(next_token_id)

            input_ids.append(next_token_id)
            generated_token_ids.append(next_token_id)

            if json_fsm.is_done():
                break

        if not json_fsm.is_done():
            raise ValueError(
                "The model did not generate a complete JSON function call."
            )

        generated_text = self.llm_model.decode(generated_token_ids)
        function_call = parse_function_call(generated_text)

        if function_call is None:
            raise ValueError(
                f"Could not parse generated function call: {generated_text!r}"
            )

        # The model output does not contain the original prompt, but the
        # normalization logic needs it to infer the substitution regex.
        function_call.prompt = prompt

        normalize_parameter_types(
            function_call,
            self.func_definition_list,
        )

        validate_parameter_types(
            function_call,
            self.func_definition_list,
        )

        normalize_substitution_regex(function_call)

        # Validate the complete result through Pydantic.
        result = FunctionCallResult.model_validate({
            "calls": [function_call],
        })
        print(
            f"Function generation took "
            f"{time.perf_counter() - start:.2f}s"
        )
        # REMOVE LATER
        print(f"Generated {len(generated_token_ids)} tokens")

        return result.calls[0]

    def run(self) -> None:
        """Generate and validate one function call per user prompt."""

        max_attempts = 5
        generated_calls: list[dict] = []
        self.vocab = load_vocab_from_model(self.llm_model)

        for prompt_data in self.prompts_list:
            prompt = prompt_data.prompt
            feedback = ""
            function_call = None

            for attempt in range(max_attempts):
                try:
                    function_call = self._generate_function_call(
                        prompt=prompt,
                        feedback=feedback,
                    )
                    break

                except (ValueError, TypeError) as exc:
                    feedback = str(exc)

                    if attempt == max_attempts - 1:
                        error = (
                            f"Could not generate a valid function call for "
                            f"prompt after {max_attempts} attempts: {prompt}"
                        )
                        raise ValueError(error) from exc
            print(self.llm_model._device)

            if function_call is None:
                raise ValueError(
                    f"No function call generated for prompt: {prompt}"
                )

            generated_calls.append({
                "prompt": prompt,
                "name": function_call.name,
                "parameters": function_call.parameters,
            })

        self.response = json.dumps(
            generated_calls,
            indent=2,
        )

        with open(self.output_filepath, "w", encoding="utf-8") as output_file:
            output_file.write(self.response)
            output_file.write("\n")
