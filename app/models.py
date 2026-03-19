from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class Student(BaseModel):
    id: int  
    firstName: str = Field(..., min_length=2)
    lastName: str = Field(..., min_length=2)
    email: EmailStr
    grade: float = Field(..., ge=0, le=20)
    field: Literal["informatique", "mathématiques", "physique", "chimie"]