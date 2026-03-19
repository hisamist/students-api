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

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/students`           | List all students (paginated, sorted)|
| GET    | `/students/{id}`      | Get a student by ID                  |
| POST   | `/students`           | Create a new student                 |
| PUT    | `/students/{id}`      | Update an existing student           |
| DELETE | `/students/{id}`      | Delete a student                     |
| GET    | `/students/stats`     | Get statistics (total, avg grade...) |
| GET    | `/students/search?q=` | Search students by name              |
| POST   | `/reset`              | Reset data to initial state          |

### Query Parameters for `GET /students`

| Parameter | Default | Description                          |
|-----------|---------|--------------------------------------|
| `page`    | `1`     | Page number (min: 1)                 |
| `limit`   | `10`    | Results per page (1–100)             |
| `sort`    | `grade` | Field to sort by (`grade` or `name`) |
| `order`   | `desc`  | Sort direction (`asc` or `desc`)     |

### Student Schema

```json
{
  "firstName": "Alice",
  "lastName": "Lovelace",
  "email": "alice@edu.com",
  "grade": 18.5,
  "field": "informatique"
}
```

**Allowed fields:** `informatique`, `mathématiques`, `physique`, `chimie`
**Grade:** float between `0` and `20`

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
