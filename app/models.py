from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional

class Student(BaseModel):
    id: Optional[int] = None
    firstName: str = Field(..., min_length=2)
    lastName: str = Field(..., min_length=2)
    email: EmailStr
    grade: float = Field(..., ge=0, le=20)
    field: Literal["informatique", "mathématiques", "physique", "chimie"]