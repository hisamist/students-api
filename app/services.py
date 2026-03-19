from app.models import Student
from app.data import students_db
from fastapi import HTTPException, status
class StudentService:
    @staticmethod
    def get_all_students() -> list[Student]:
        """
        Retrieve all students from the database.
        """
        return students_db

    @staticmethod
    def get_student_by_id(student_id: int) -> Student:
        """
        Search for a student by ID.
        Raises 404 if not found.
        """
        for student in students_db:
            if student.id == student_id:
                return student
        
        # If no student matches the ID, raise a clean 404 error
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Student with ID {student_id} not found"
            )