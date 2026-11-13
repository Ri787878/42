from pydantic import BaseModel, Field, model_validator
from typing import Any


class Function_definition(BaseModel):
    name: str = Field()
    description: str = Field()
    parameters: list[tuple[str, str]] = Field()
    returns: str = Field()
    json_schema: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def schema_creator(self) -> "Function_definition":
        self.json_schema = self.model_json_schema()
        return self
