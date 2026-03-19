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

    @staticmethod
    def update_student(student_id: int, updated_data: Student) -> Student:
        # 1. Find the student (404 if not found)
        target_student = StudentService.get_student_by_id(student_id)

        # 2. Unique Email Check (409 Conflict)
        for s in students_db:
            if s.email == updated_data.email and s.id != student_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Cet email est déjà utilisé par un autre étudiant."
                )

        # 3. Update the fields
        target_student.firstName = updated_data.firstName
        target_student.lastName = updated_data.lastName
        target_student.email = updated_data.email
        target_student.grade = updated_data.grade
        target_student.field = updated_data.field

        return target_student

    @staticmethod
    def delete_student(student_id: int) -> dict:
        """
        Delete a student by ID.
        - Raises 404 if not found.
        - Returns a confirmation message if successful.
        """
        # 1. Find the student (reuse GET logic for 404 check)
        target_student = StudentService.get_student_by_id(student_id)

        # 2. Remove from the list
        students_db.remove(target_student)

        # 3. Return a confirmation message
        return {"message": f"Student with ID {student_id} has been deleted successfully."}

    @staticmethod
    def get_stats() -> dict:
        """
        Calculate statistics for all students.
        Returns: total, average, count by field, and best grade.
        """
        if not students_db:
            return {
                "totalStudents": 0,
                "averageGrade": 0,
                "studentsByField": {},
                "bestStudent": 0
            }

        total_students = len(students_db)
        
        # 1. Average Grade (rounded to 2 decimals)
        all_grades = [s.grade for s in students_db]
        average_grade = round(sum(all_grades) / total_students, 2)
        
        # 2. Best Grade
        best_student = max(all_grades)
        
        # 3. Students by Field
        students_by_field = {}
        for s in students_db:
            field = s.field
            students_by_field[field] = students_by_field.get(field, 0) + 1

        return {
            "totalStudents": total_students,
            "averageGrade": average_grade,
            "studentsByField": students_by_field,
            "bestStudent": best_student
        }