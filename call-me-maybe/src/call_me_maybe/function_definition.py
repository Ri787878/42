from pydantic import BaseModel, Field


class Function_definition(BaseModel):
    name: str = Field()
    description: str = Field()
    parameters: list[tuple[str, str]] = Field()
    returns: str = Field()
