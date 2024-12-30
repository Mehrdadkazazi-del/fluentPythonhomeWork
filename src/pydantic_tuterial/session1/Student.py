from pydantic import BaseModel, ValidationError
from typing import List
class Student(BaseModel):
    student_number: int
    courses: List[str]

student = Student(
    student_number=2541,
    courses=['Python', 'Java', 'C++']
)

print(student)
print(student.model_dump())

data = {
    'student_number': 2542,
    'courses': ['Python', 'Java', 'C++']
}

student2 = Student(**data)
print(student2.model_dump())

wrong_data = {
    'student_number': "2543 is not an integer",
    'courses': ['Python', 'Java', 'C++']
}

try:
    student3 = Student(**wrong_data)
    print(student3.model_dump())
except ValidationError as e:
    print(e.errors())