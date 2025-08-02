from pydantic import BaseModel


class DiceModel(BaseModel):
    number: int