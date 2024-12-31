from pydantic import BaseModel, Field, ConfigDict


# use new version for support alias in pydantic
class Student(BaseModel):
    # model_config = ConfigDict(populate_by_name=True, extra="forbid")
    model_config = ConfigDict(populate_by_name=True, extra="ignore")
    # model_config = ConfigDict(populate_by_name=True, extra="allow")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    student_number: int = Field(alias="studentNumber")

    #@Deprecated
    # class Config:
    #     populate_by_name = True

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

student_data_with_snake_case_support = {
    "first_name": "John",
    "last_name": "Doe",
    "student_number": 254123,
    "gpa": 19.80
}

student_object = Student.model_validate(student_data_with_snake_case_support)
print(student_object.model_dump())
