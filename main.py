import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Привіт. Тут можна отимати дані студентів з Moodle. "}


@app.get("/get_student/{id}")
async def get_student(id: str):
    with open('students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    student = data[f'{id}']

    return student
