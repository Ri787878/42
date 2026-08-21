from pydantic import BaseModel, Field


class Prompt(BaseModel):
    prompt: str = Field()
