from fastapi import FastAPI, HTTPException
from app.data import students_db, reset_db  
from app.models import Student
from app.services import StudentService

app = FastAPI(title="Students API")

@app.get("/students", response_model=list[Student])
async def get_students():
    """
    Endpoint to get the list of all students.
    """
    try:
        return StudentService.get_all_students()
    except Exception:
        raise HTTPException(
            status_code=500, 
            detail="An error occurred while fetching students"
        )

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int): 
    try:
        return StudentService.get_student_by_id(student_id)
    except HTTPException as http_exc:
        raise http_exc
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/reset")
async def perform_reset():
    """
    Resets the database to initial values.
    """
    reset_db()
    return {"message": "Data successfully reset"}