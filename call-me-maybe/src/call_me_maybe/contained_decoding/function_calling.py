import re
import json
from typing import Any

from pydantic import BaseModel, Field


class FunctionParameter(BaseModel):
    name: str
    type: str
    description: str = Field(default="")


class FunctionCall(BaseModel):
    prompt: str
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
            "parameters": [
                {
                    "name": parameter_name,
                    "type": parameter_type,
                    "required": True,
                }
                for parameter_name, parameter_type in definition.parameters
            ],
            "returns": definition.returns,
        })

    functions_json = json.dumps(available_functions, indent=2)

    return f"""You select the best available function for the user request.

Available functions:
{functions_json}

User request:
{prompt_text}

Return exactly one JSON object with this structure:
{{
  "prompt": "exact original request",
  "name": "function name",
  "parameters": {{
    "parameter_name": "value with the declared type"
  }}
}}

Rules:
- Select one available function.
- Use the exact parameter names.
- Copy quoted values exactly, including spaces and capitalization.
- Infer regexes from the requested character type or operation, not from sample values.
- Return one short, complete JSON object only. Do not output explanations or Markdown.
- A regex must match only the target characters, not the entire source string.
- Output each argument using its declared JSON type.
- Numbers must be JSON numbers, not quoted strings.
- Strings must be quoted JSON strings.
- Booleans must be JSON true or false.

Begin the JSON response now:
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
