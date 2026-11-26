from pydantic import BaseModel, Field


class Prompt(BaseModel):
    """Class holds a whole prompt."""
    prompt: str = Field()
