from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class student(BaseModel):
    name: str ='Krishna Jatav' # default_value
    age: Optional[int] = None # optional field
    email: EmailStr # required field with email validation
    cgpa: float=Field(gt=0.0, lt=10.0, default=5.0, description="Cumulative Grade Point Average") # required field with validation for cgpa between 0 and 10
new_student = { "age": 24, "email": "krishna@example.com", "cgpa": 8.5 }
student=student(**new_student)

student_dic=dict(student)
print(student_dic)

student_json=student.model_dump_json()
print(student_json)