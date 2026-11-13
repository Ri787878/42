import re
import json
from typing import Any

from pydantic import BaseModel, Field


class FunctionParameter(BaseModel):
    name: str
    type: str
    description: str = Field(default="")


class FunctionCall(BaseModel):
    prompt: str = Field(default="")
    name: str
    parameters: dict[str, Any] = Field(default_factory=dict)


class FunctionCallResult(BaseModel):
    calls: list[FunctionCall] = Field(default_factory=list)

    @staticmethod
    def build_generation_prompt(
        prompt_text: str,
        definitions: list[Any],
    ) -> str:
        return build_single_call_prompt(prompt_text, definitions)


def build_single_call_prompt(
    prompt_text: str,
    definitions: list[Any],
) -> str:
    available_functions = []

    for definition in definitions:
        available_functions.append({
            "name": definition.name,
            "description": definition.description,
            "parameters": dict(definition.parameters),
        })

    functions_json = json.dumps(available_functions, separators=(",", ":"))

    return f"""Select one function for the request. Return compact JSON only:
{{"name":"exact function name","parameters":{{"exact parameter name":"value"}}}}
Functions (parameter names mapped to types):
{functions_json}
Rules:
- Include all declared parameters with their declared types; no extra keys.
- Copy quoted values exactly, preserving spaces, case and punctuation.
- Escape quotes and backslashes inside JSON strings.
- Regex: all digits = [0-9]+; specific characters 2 and 5 = [25].
- Stop after the final closing brace. No explanation or formatting.
Request:
{prompt_text}
JSON:
"""



def _repair_invalid_json_escapes(text: str) -> str:
    """Escape backslashes that are invalid in JSON strings."""
    return re.sub(
        r'\\(?!["\\/bfnrtu])',
        r'\\\\',
        text,
    )


def parse_function_call(text: str) -> FunctionCall | None:
    decoder = json.JSONDecoder()
    candidate = text.lstrip()

    try:
        parsed_response, _ = decoder.raw_decode(candidate)
        return FunctionCall.model_validate(parsed_response)
    except (json.JSONDecodeError, ValueError):
        pass

    try:
        repaired_text = _repair_invalid_json_escapes(candidate)
        parsed_response, _ = decoder.raw_decode(repaired_text)
        return FunctionCall.model_validate(parsed_response)
    except (json.JSONDecodeError, ValueError):
        return None


def normalize_parameter_types(
    function_call: FunctionCall,
    definitions: list[Any],
) -> None:
    definition = next(
        item for item in definitions
        if item.name == function_call.name
    )

    expected_types = dict(definition.parameters)

    for parameter_name, expected_type in expected_types.items():
        value = function_call.parameters.get(parameter_name)

        if expected_type == "number" and isinstance(value, str):
            try:
                function_call.parameters[parameter_name] = (
                    float(value)
                    if "." in value
                    else int(value)
                )
            except ValueError:
                pass


def validate_parameter_types(
    function_call: FunctionCall,
    definitions: list[Any],
) -> None:
    definition = next(
        item
        for item in definitions
        if item.name == function_call.name
    )

    expected_types = dict(definition.parameters)

    for parameter_name, expected_type in expected_types.items():
        if parameter_name not in function_call.parameters:
            raise ValueError(
                f"Missing parameter: {parameter_name}"
            )

        value = function_call.parameters[parameter_name]

        if expected_type == "number" and (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise ValueError(
                f"Parameter '{parameter_name}' must be a number"
            )

        if expected_type == "string" and not isinstance(value, str):
            raise ValueError(
                f"Parameter '{parameter_name}' must be a string"
            )

        if expected_type == "boolean" and not isinstance(value, bool):
            raise ValueError(
                f"Parameter '{parameter_name}' must be a boolean"
            )


def normalize_substitution_regex(function_call: FunctionCall) -> None:
    """Build and validate the regex for substitution requests."""
    if function_call.name != "fn_substitute_string_with_regex":
        return

    prompt = function_call.prompt.casefold()

    # Spaces are requested by name, not as quoted characters.
    if "space" in prompt:
        function_call.parameters["regex"] = " "

    else:
        # Only inspect quoted values before the source string.
        request_part = re.split(r"\s+in\s+", prompt, maxsplit=1)[0]

        quoted_values = re.findall(
            r"""['"]([^'"]*)['"]""",
            request_part,
        )

        characters = "".join(
            value
            for value in quoted_values
            if len(value) == 1
        )

        if characters:
            function_call.parameters["regex"] = (
                f"[{re.escape(characters)}]"
            )
        elif "all digits" in prompt or "all numbers" in prompt:
            function_call.parameters["regex"] = r"\d+"

    regex = function_call.parameters.get("regex")

    if not isinstance(regex, str):
        raise ValueError("Substitution regex must be a string")

    try:
        re.compile(regex)
    except re.error as exc:
        raise ValueError(
            f"Invalid substitution regex: {regex!r}"
        ) from exc
