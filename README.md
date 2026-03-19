# Students API

[![CI](https://github.com/hisamist/students-api/actions/workflows/ci.yml/badge.svg)](https://github.com/hisamist/students-api/actions/workflows/ci.yml)

A RESTful API for managing student records, built with **FastAPI** and **Python**.

## Features

- Full CRUD for student records
- Pagination and sorting on the student list
- Search by name
- Global statistics endpoint
- Input validation with Pydantic (email, grade range 0–20, allowed fields)
- CI pipeline with linting (Ruff) and tests (Pytest) on Python 3.10 & 3.11

## Project Structure

```
students-api/
├── app/
│   ├── main.py       # FastAPI routes
│   ├── models.py     # Pydantic models
│   ├── services.py   # Business logic
│   └── data.py       # In-memory data store
├── tests/
│   └── test_main.py  # Pytest test suite
├── .github/
│   └── workflows/
│       └── ci.yml    # GitHub Actions CI
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd students-api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive docs: `http://127.0.0.1:8000/docs`

## API Endpoints

### `GET /students`

Returns a paginated and sorted list of students.

| Parameter | Default | Description                          |
|-----------|---------|--------------------------------------|
| `page`    | `1`     | Page number (min: 1)                 |
| `limit`   | `10`    | Results per page (1–100)             |
| `sort`    | `grade` | Field to sort by (`grade` or `name`) |
| `order`   | `desc`  | Sort direction (`asc` or `desc`)     |

| Status | Meaning                        |
|--------|--------------------------------|
| `200`  | List of students               |
| `400`  | Invalid query parameter        |

---

### `GET /students/{id}`

Returns a single student by ID.

| Status | Meaning                        |
|--------|--------------------------------|
| `200`  | Student found                  |
| `400`  | ID is not a valid integer      |
| `404`  | Student not found              |

---

### `POST /students`

Creates a new student.

**Request body:**

```json
{
  "firstName": "Alice",
  "lastName": "Lovelace",
  "email": "alice@edu.com",
  "grade": 18.5,
  "field": "informatique"
}
```

| Status | Meaning                              |
|--------|--------------------------------------|
| `201`  | Student created                      |
| `400`  | Validation error (missing/invalid field) |
| `409`  | Email already exists                 |

---

### `PUT /students/{id}`

Updates an existing student (full replacement).

| Status | Meaning                              |
|--------|--------------------------------------|
| `200`  | Student updated                      |
| `400`  | Validation error                     |
| `404`  | Student not found                    |
| `409`  | Email already used by another student|

---

### `DELETE /students/{id}`

Deletes a student by ID.

| Status | Meaning           |
|--------|-------------------|
| `200`  | Student deleted   |
| `404`  | Student not found |

---

### `GET /students/stats`

Returns global statistics.

**Response:**

```json
{
  "totalStudents": 5,
  "averageGrade": 14.2,
  "bestStudent": { "firstName": "Alice", ... },
  "studentsByField": {
    "informatique": 2,
    "mathématiques": 1
  }
}
```

| Status | Meaning |
|--------|---------|
| `200`  | Stats   |

---

### `GET /students/search?q=`

Searches students by first name or last name.

| Status | Meaning                     |
|--------|-----------------------------|
| `200`  | List of matching students   |
| `400`  | Missing or empty `q` param  |

---

### `POST /reset`

Resets all data to the initial state.

| Status | Meaning        |
|--------|----------------|
| `200`  | Data reset     |

---

### Student Schema

| Field       | Type    | Constraints                                              |
|-------------|---------|----------------------------------------------------------|
| `id`        | integer | Auto-assigned, optional on creation                     |
| `firstName` | string  | Min 2 characters                                        |
| `lastName`  | string  | Min 2 characters                                        |
| `email`     | string  | Valid email format, unique                              |
| `grade`     | float   | Between `0` and `20`                                    |
| `field`     | string  | `informatique`, `mathématiques`, `physique`, `chimie`   |

## Running Tests

```bash
python -m pytest
```

## Code Coverage

Run tests with coverage report:

```bash
# Terminal report
python -m pytest --cov=app --cov-report=term-missing

# HTML report (opens in browser)
python -m pytest --cov=app --cov-report=html
open htmlcov/index.html
```

Example output:

```
----------- coverage: app -----------
Name                Stmts   Miss  Cover
---------------------------------------
app/main.py            52      3    94%
app/services.py        38      2    95%
app/models.py           6      0   100%
app/data.py             8      0   100%
---------------------------------------
TOTAL                 104      5    95%
```

## Linting

```bash
python -m ruff check .
```

## CI/CD

GitHub Actions runs on every push and pull request to `main`, testing against Python 3.10 and 3.11:

1. Install dependencies
2. Lint with Ruff
3. Run tests with Pytest
