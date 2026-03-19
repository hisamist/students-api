from app.models import Student
from app.data import students_db

class StudentService:
    @staticmethod
    def get_all_students() -> list[Student]:
        """
        Retrieve all students from the database.
        """
        return students_db