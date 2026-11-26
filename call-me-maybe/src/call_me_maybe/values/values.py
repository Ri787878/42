from pydantic import BaseModel, Field


class Values(BaseModel):
    """Class containg project wide set variables."""
    max_tries: int = Field(default=3)
    max_tokens: int = Field(default=50)
