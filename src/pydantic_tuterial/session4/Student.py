from pydantic import BaseModel, Field


class Student(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    student_number: int = Field(alias="studentNumber")

    class Config:
        populate_by_name = True

json_student_data = {
    "firstName": "John",
    "lastName": "Doe",
    "studentNumber": 1234
}

student_object = Student.model_validate(json_student_data)
print(student_object.model_dump())

print(student_object.first_name)
print(student_object.last_name)
print(student_object.student_number)

student_data_with_snake_case_support = {
    "first_name": "John",
    "last_name": "Doe",
    "student_number": 1234
}

student_object = Student.model_validate(student_data_with_snake_case_support)
print(student_object.model_dump())
