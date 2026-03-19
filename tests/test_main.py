from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

# --- GET TESTS (5) ---

def test_get_all_students_type():
    """Test 1: GET /students returns 200 and a list."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_students_contains_initial_data():
    """Test 2: GET /students must return all initial students(5 total) """
    response = client.get("/students")
    data = response.json()
    # Based on our INITIAL_STUDENTS in data.py
    assert len(data) == 5

def test_get_student_by_id_valid():
    """Test 3: GET /students/:id (valid) must return the corresponding student"""
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["firstName"] == "Alice"

def test_get_student_by_id_not_found():
    """Test 4: GET /students/:id (non-existent) must return 404. """
    response = client.get("/students/9999")
    assert response.status_code == 404

def test_get_student_by_id_invalide():
    """Test 5: GET /students/:id (invalid 'abc') must return 400. """
    response = client.get("/students/ab")
    # Our custom exception handler converts the 422(default for FastAPI) to 400
    assert response.status_code == 400