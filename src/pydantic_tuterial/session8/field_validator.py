from pydantic import BaseModel, constr, field_validator, root_validator


class Person(BaseModel):
    first_name: constr(min_length=2, strip_whitespace=True, strict=True)
    last_name: constr(min_length=2, strip_whitespace=True, strict=True)

    @field_validator("first_name", "last_name")
    @classmethod
    def to_title(cls, value):
        if value.isnumeric():
            raise ValueError(f"{value} is not a valid number")
        return value.title()

    @root_validator(pre=True)
    def validate_lengths(cls, values):
        max_lengths = {
            "first_name": 10,
            "last_name": 50,
            "symbol": 50,
        }
        for field, max_length in max_lengths.items():
            if field in values and len(values[field]) > max_length:
                raise ValueError(f"{field} exceeds the maximum length of {max_length} characters")

        return values

# we get error because we write numeric for first_name
person = Person(first_name="123", last_name="Smith")
print(person.model_dump())
# person2 = Person(first_name="John", last_name="Smith")
# print(person2)
