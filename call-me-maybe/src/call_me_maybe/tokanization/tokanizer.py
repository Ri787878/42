from pydantic import BaseModel, Field
# , model_validator


class Tokanizer(BaseModel):
    stuff: str = Field()
