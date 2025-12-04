from fastapi import FastAPI
from typing import List
from models import Major, Speciality, User , Role ,Gender
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        first_name="Amin",
        last_name="Khan",
        Bac_matrucule=2345673232,
        major=Major.CS,
        speciality=Speciality.AI,
        year_of_study=3,
        section=2,
        group_number=1,
        middle_name=None, 
        gender=Gender.MALE,
        roles=[Role.ADMIN]
    )
]

@app.get("/")
async def read_root():
    return {"Hello": "Amin Khan"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return user