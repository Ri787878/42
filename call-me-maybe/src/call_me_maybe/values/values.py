from pydantic import BaseModel, Field


class Values(BaseModel):
    max_tries: int = Field(default=128)
