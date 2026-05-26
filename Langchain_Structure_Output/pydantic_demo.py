from pydantic import BaseModel
from typing import Optional

class student(BaseModel):
    name: str ='Krishna' # default_value
    age: Optional[int] = None # optional field
new_student = { "age": 25 }
student=student(**new_student)
print(student)