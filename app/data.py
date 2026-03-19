from app.models import Student

# Initial Data
INITIAL_STUDENTS = [
    Student(
        id=1,
        firstName="Alice",
        lastName="Lovelace",
        email="alice@edu.com",
        grade=18.5,
        field="informatique",
    ),
    Student(
        id=2,
        firstName="Bob",
        lastName="Py",
        email="bob@edu.com",
        grade=12.0,
        field="mathématiques",
    ),
    Student(
        id=3,
        firstName="Charlie",
        lastName="Curie",
        email="charlie@edu.com",
        grade=15.0,
        field="physique",
    ),
    Student(
        id=4,
        firstName="David",
        lastName="Darwin",
        email="david@edu.com",
        grade=9.5,
        field="chimie",
    ),
    Student(
        id=5,
        firstName="Eve",
        lastName="Esprit",
        email="eve@edu.com",
        grade=17.0,
        field="informatique",
    ),
]

# Runtime in-memory database
students_db: list[Student] = []


def reset_db():
    """initialise data"""
    global students_db
    # model_copy(): copy as new object
    students_db.clear()
    students_db.extend([s.model_copy() for s in INITIAL_STUDENTS])


# Initialize the data on module load
reset_db()
