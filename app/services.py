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

    @staticmethod
    def create_student(student_data: Student) -> Student:
        # 1. Check for email uniqueness -> 409 Conflict
        for s in students_db:
            if s.email == student_data.email:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email already registered"
                )

        # 2. Auto-generate ID (max ID + 1)
        new_id = max([s.id for s in students_db], default=0) + 1
        student_data.id = new_id

        # 3. Save and Return
        students_db.append(student_data)
        return student_data