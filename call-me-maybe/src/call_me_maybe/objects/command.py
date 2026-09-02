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
    FunctionCall
)
# from .generator import Generator
from ..values import Values
# from ..contained_decoding import BasicJsonFSM, load_vocab_from_model
from .function_definition import Function_definition
from llm_sdk import Small_LLM_Model
from pathlib import Path
import numpy as np


class Command(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

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

    def run(self) -> None:
        """Generate and validate one function call per user prompt."""
        import json

        all_calls = []

        for prompt_item in self.prompts_list:
            generation_prompt = FunctionCallResult.build_generation_prompt(
                prompt_text=prompt_item.prompt,
                definitions=self.func_definition_list,
            )

            # print(f"\n{generation_prompt}\n")

            encoded_prompt_tensor = self.llm_model.encode(
                generation_prompt
            )

            context_ids: list[int] = [
                int(token_id)
                for token_id in encoded_prompt_tensor.flatten().tolist()
            ]

            generated_ids: list[int] = []
            decoded_text = ""
            function_call = None

            for _ in range(self.project_values.max_tries):
                logits = self.llm_model.get_logits_from_input_ids(
                    context_ids
                )

                next_token_logits = extract_last_position_if_needed(
                    logits
                ).copy()

                banned_token_ids = getattr(
                    self.project_values,
                    "banned_token_ids",
                    [],
                )

                if banned_token_ids:
                    next_token_logits[banned_token_ids] = -np.inf

                temperature = max(
                    float(
                        getattr(
                            self.project_values,
                            "temperature",
                            1.0,
                        )
                    ),
                    1e-6,
                )

                probabilities = softmax(
                    next_token_logits,
                    temperature=temperature,
                )

                if (
                    probabilities is None
                    or not np.isfinite(probabilities).all()
                    or probabilities.sum() <= 0
                ):
                    raise ValueError(
                        "The model returned an invalid "
                        "probability distribution."
                    )

                next_token_id = int(
                    decoding_strategy(probabilities)
                )

                context_ids.append(next_token_id)
                generated_ids.append(next_token_id)

                decoded_text = self.llm_model.decode(
                    generated_ids
                ).strip()

                try:
                    parsed_response = json.loads(decoded_text)

                    function_call = FunctionCall.model_validate(
                        parsed_response
                    )

                    break

                except (json.JSONDecodeError, ValueError):
                    continue

            if function_call is None:
                print(f"RAW RESPONSE: {decoded_text!r}")
                print(
                    f"GENERATED TOKEN COUNT: {len(generated_ids)}"
                )
                print(
                    f"MAX TRIES: {self.project_values.max_tries}"
                )

                raise ValueError(
                    "Could not generate a complete JSON function call "
                    f"for prompt: {prompt_item.prompt}"
                )

            function_call.prompt = prompt_item.prompt

            valid_function_names = {
                definition.name
                for definition in self.func_definition_list
            }

            if function_call.name not in valid_function_names:
                raise ValueError(
                    f"Unknown function '{function_call.name}' returned "
                    f"for prompt '{prompt_item.prompt}'."
                )

            all_calls.append(function_call.model_dump())

        self.response = json.dumps(
            all_calls,
            indent=2,
        )

        print(
            f"generated_function_call_count = {len(all_calls)}"
        )
        print(f"response: {self.response}")

        with open(self.output_filepath, "w") as output_file:
            output_file.write(self.response)


"""
def run(self, llm_model: Small_LLM_Model) -> None:
        print("\n\n")

        encoded_prompt_tensor = llm_model.encode(self.prompts_list[0].prompt)
        encoded_prompt: list[int] = [
            int(x) for x in encoded_prompt_tensor.flatten().tolist()]
        context_ids: list[int] = list(encoded_prompt)

        max_new_tokens = 30
        stop_strings = ["\nUser:", "\n\nUser:", "<|endoftext|>", "</s>"]

        # Configure banned tokens
        words_to_ban = ["<|endoftext|>"]
        processor = SimpleBanningProcessor(
            token_to_id=get_token_id(llm_model),
            words_to_ban=words_to_ban,
            unknown_token_policy="ignore",
        )

        generated_ids: list[int] = []
        probabilities: np.ndarray | None = None

        for _ in range(max_new_tokens):
            logits = llm_model.get_logits_from_input_ids(context_ids)
            next_token_logits = extract_last_position_if_needed(logits)

            # Apply banning processor (expects [batch=1][vocab])
            score_rows = [next_token_logits.tolist()]
            score_rows = processor(input_ids=[context_ids], scores=score_rows)
            next_token_logits = np.asarray(score_rows[0], dtype=float)

            # JSON filtering
            allowed_ids: list[Any] = []

            if not allowed_ids:
                print_to_stderr("[ERROR] No valid JSON continuation.")
                break

            # Mask everything not allowed
            next_token_logits = mask_all_except(
                next_token_logits,
                allowed_ids,
                value=-float("-inf")
            )

            # Optional safety: if everything got masked, stop
            if np.all(np.isneginf(next_token_logits)):
                print_to_stderr("[ERROR] All logits masked; stopping.")
                break

            # Softmax
            probabilities = softmax(next_token_logits)
            next_id = int(decoding_strategy(probabilities))

            context_ids.append(next_id)
            generated_ids.append(next_id)

            # Secondary stop rule via decoded text
            current_text = llm_model.decode(generated_ids)
            if any(s in current_text for s in stop_strings):
                break

            # Optional anti-loop guard
            if len(generated_ids) >= 8 and len(set(generated_ids[-8:])) == 1:
                break

        self.response = llm_model.decode(generated_ids)

        print(f"encoded_prompt = {encoded_prompt}\n")
        print(f"generated_token_count = {len(generated_ids)}")
        print(
            f"last_step_vocab_size = "
            f"{len(probabilities) if probabilities is not None else 0}")
        print(f"response: {self.response}")

        with open(self.output_filepath, "w") as f:
            f.write(
                str(probabilities.tolist() if (
                    probabilities is not None) else [])
            )







        print("\n\n")

        context_ids: list[int] = Generator.convert_to_token_list(self)

        generated_ids: list[int] = []
        probabilities: np.ndarray | None = None

        # Expects dict[str, int]
        tokenizer_vocab = load_vocab_from_model(self.llm_model)
        fsm = BasicJsonFSM(tokenizer_vocab)
        banned_token_ids: list[int] = getattr(
            self.project_values,
            "banned_token_ids", []
        )

        for _ in range(self.project_values.max_tries):
            logits = self.llm_model.get_logits_from_input_ids(context_ids)
            next_token_logits = extract_last_position_if_needed(logits).copy()

            # 1) Ban tokens first
            if banned_token_ids:
                next_token_logits[banned_token_ids] = -np.inf

            # 2) FSM-allowed tokens
            allowed_token_ids = fsm.get_allowed_token_ids()

            # remove banned from allowed set too (safety)
            if banned_token_ids:
                banned_set = set(banned_token_ids)
                allowed_token_ids = [
                    tid for tid in allowed_token_ids if tid not in banned_set]

            # if nothing allowed, stop safely
            if not allowed_token_ids:
                break

            # 3) Apply JSON mask
            json_mask = np.full_like(next_token_logits, fill_value=-np.inf)
            json_mask[allowed_token_ids] = next_token_logits[allowed_token_ids]
            next_token_logits = json_mask

            # if all tokens masked out, stop
            if not np.isfinite(next_token_logits).any():
                break

            # 4) Softmax with safe temperature
            temperature = max(
                float(getattr(self.project_values, "temperature", 1.0)), 1e-6)
            probabilities = softmax(next_token_logits, temperature=temperature)

            # guard against NaN/invalid distribution
            if (
                probabilities is None
                or not np.isfinite(probabilities).all()
                or probabilities.sum() <= 0.0
            ):
                break

            # 5) Sample
            next_id = int(decoding_strategy(probabilities))

            # hard safety check
            allowed_set = set(allowed_token_ids)
            if next_id not in allowed_set:
                break

            # 6) Advance FSM + append token
            fsm.update_state(next_id)
            context_ids.append(next_id)
            generated_ids.append(next_id)

            if fsm.current_state == fsm.STATE_DONE:
                break

        self.response = self.llm_model.decode(generated_ids)

        import json

        self.response = self.llm_model.decode(generated_ids).strip()

        try:
            json.loads(self.response)
        except Exception:
            # deterministic fallback that is always valid JSON
            prompt_text = (
                self.prompts_list[0].prompt if self.prompts_list else "")
            safe_prompt = (
                prompt_text.replace("\\", "\\\\")
                .replace('"', '\\"')
                .replace("\n", "\\n")
            )
            self.response = (
                f'{{"question":"{safe_prompt}",'
                f'"answer":"unknown"}}')

        print(f"generated_token_count = {len(generated_ids)}")
        print(
            f"last_step_vocab_size = "
            f"{len(probabilities) if probabilities is not None else 0}")
        print(f"prompt tested: {self.prompts_list[0].prompt}")
        print(f"response: {self.response}")

        with open(self.output_filepath, "w") as f:
            f.write(str(self.response))
"""
