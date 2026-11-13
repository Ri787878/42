from pydantic import BaseModel
from typing import Any


class Generator(BaseModel):

    @staticmethod
    def convert_to_token_list(command: Any) -> list[int]:
        from .command import Command

        if type(command) is not Command:
            return []

        encoded_prompt_tensor = command.llm_model.encode(
            command.prompts_list[0].prompt)

        encoded_prompt: list[int] = [
            int(x) for x in encoded_prompt_tensor.flatten().tolist()]
        context_ids: list[int] = list(encoded_prompt)

        return context_ids
