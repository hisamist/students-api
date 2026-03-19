from fastapi import FastAPI
from app.data import students_db, reset_db

app = FastAPI(title="Students API")

@app.get("/students")
async def get_all_students():
    return students_db

@app.post("/reset")
async def perform_reset():
    reset_db()
    return {"message": "Données réinitialisées avec succès"}