from fastapi import FastAPI, HTTPException,Query
from app.data import students_db, reset_db  
from app.models import Student
from app.services import StudentService

app = FastAPI(title="Students API")

@app.get("/students/stats")
async def get_student_stats():
    """
    Get global statistics about students.
    """
    try:
        return StudentService.get_stats()
    except Exception as e:
        print(f"STATS error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/students/search", response_model=list[Student])
async def search_students(q: str = Query(None)):
    """
    Search students by name or first name.
    - 400: If 'q' is missing or empty.
    """
    if not q or q.strip() == "":
        raise HTTPException(
            status_code=400, 
            detail="The search parameter 'q' is required and cannot be empty."
        )
    
    try:
        return StudentService.search_students(q)
    except Exception as e:
        print(f"SEARCH error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

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
    """
    Retrieve a student by their ID.
    - 200: Success
    - 404: Not Found (via raise HTTPException)
    - 400: Validation Error (handled automatically by FastAPI for types)
    """
    try:
        return StudentService.get_student_by_id(student_id)
    except HTTPException as http_exc:
        raise http_exc
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/students", response_model=Student, status_code=201)
async def create_student(student: Student):
    """
    Create a new student with full validation.
    """
    try:
        return StudentService.create_student(student)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"POST Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student_data: Student):
    """
    Update an existing student.
    Validates data (400), checks existence (404), and email uniqueness (409).
    """
    try:
        return StudentService.update_student(student_id, student_data)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"PUT Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Deletes a student record.
    - 200: Success message
    - 404: Not Found
    """
    try:
        return StudentService.delete_student(student_id)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"DELETE error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/reset")
async def perform_reset():
    """
    Resets the database to initial values.
    """
    reset_db()
    return {"message": "Data successfully reset"}