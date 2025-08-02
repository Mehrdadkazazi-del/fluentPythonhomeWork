from __future__ import annotations
from pydantic import BaseModel, constr, model_validator

class User(BaseModel):
    user_name: constr(min_length=3, max_length=30, strict=True)
    password1: constr(min_length=5, max_length=30, strict=True)
    password2: constr(min_length=5, max_length=30, strict=True)

    @model_validator(mode="after")
    def check_password(self) -> User:
        if self.password1 != self.password2:
            raise ValueError("passwords don't match")
        return self

u1 = User(user_name="user1", password1="asdfg1", password2="asdfg")
print(u1)