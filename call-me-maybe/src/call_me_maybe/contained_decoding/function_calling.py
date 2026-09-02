import json
from typing import Any

from pydantic import BaseModel, Field


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
                }
                for parameter_name, parameter_type in definition.parameters
            ],
            "returns": definition.returns,
        })

    functions_json = json.dumps(available_functions, indent=2)

    return f"""You select a function for a user request.

Available functions:
{functions_json}

User request:
{prompt_text}

Return exactly one JSON object.
Start your response with {{ and end it with }}.
Do not write explanations, markdown, or repeated instructions.

Use this structure:
- prompt: the original user request
- name: one available function name
- parameters: an object containing the required argument values

Begin the JSON response now:
"""
