from fastapi import FastAPI
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

@app.post("/reset")
async def perform_reset():
    reset_db()
    return {"message": "Données réinitialisées avec succès"}