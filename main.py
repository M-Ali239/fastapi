'use client'


from fastapi import FastAPI, HTTPException, Body
from typing import List
from models import Student, Gender

app = FastAPI()

students = [
    Student(id=1, name="Naeem", age=57, gender=Gender.male),
    Student(id=2, name="Malika", age=21, gender=Gender.female),
    Student(id=3, name="Goraya", age=58, gender=Gender.male),
    Student(id=4, name="Shahzadi", age=23, gender=Gender.female),
    Student(id=5, name="Naeem Goraya", age=59, gender=Gender.male),
]

@app.get("/")
async def Home():
    return {"Name" : "Naeem Goraya"}




@app.get("/students")
async def get_students():
    return students

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
async def create_student(student: Student = Body(...)):
    students.append(student)
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student = Body(...)):
    for student_to_update in students:
        if student_to_update.id == student_id:
            student_to_update.name = student.name
            student_to_update.age = student.age
            student_to_update.gender = student.gender
            return student_to_update
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for student_to_delete in students:
        if student_to_delete.id == student_id:
            students.remove(student_to_delete)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")