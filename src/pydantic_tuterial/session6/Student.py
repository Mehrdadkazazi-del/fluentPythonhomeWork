from pydantic import BaseModel, Field, ConfigDict


def to_lower_camel(string: str) -> str:
    first_word, *rest = string.split("_")
    capitalized_rest = "".join(word.capitalize() for word in rest if word)
    lower_camel  =f"{first_word}_{capitalized_rest}"
    return lower_camel

# alias generator
class Student(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore", alias_generator=to_lower_camel)
    first_name: str
    last_name: str
    student_number: int

json_student_data = {
    "firstName": "John",
    "lastName": "Doe",
    "studentNumber": 254456,
    "gpa": 19.80
}


student_object = Student.model_validate(json_student_data)
print(student_object.model_dump())

print(student_object.first_name)
print(student_object.last_name)
print(student_object.student_number)
