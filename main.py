from fastapi import FastAPI, HTTPException
from typing import List
from models import Major, Speciality, User , Role ,Gender , UserUpdate , UserCreate
from uuid import UUID, uuid4

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
    ),
    User(
        first_name="Sara",
        last_name="Ali",
        Bac_matrucule=2345678901,
        major=Major.IT,
        speciality=Speciality.DS,
        year_of_study=2,
        section=1,
        group_number=3,
        middle_name="M.",
        gender=Gender.FEMALE,
        roles=[Role.USER]
    )
]

@app.get("/")
async def read_root():
    return {"Hello": "Amin Khan"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: UserCreate):
    new_user = User(**user.model_dump())
    db.append(new_user)
    return new_user
    

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, updated_user: UserUpdate):
    for user in db :
        if user.id == user_id:
            if updated_user.first_name is not None:
                user.first_name = updated_user.first_name
            if updated_user.last_name is not None:
                user.last_name = updated_user.last_name
            if updated_user.Bac_matrucule is not None:
                user.Bac_matrucule = updated_user.Bac_matrucule
            if updated_user.major is not None:
                user.major = updated_user.major
            if updated_user.speciality is not None:
                user.speciality = updated_user.speciality
            if updated_user.year_of_study is not None:
                user.year_of_study = updated_user.year_of_study
            if updated_user.section is not None:
                user.section = updated_user.section
            if updated_user.group_number is not None:
                user.group_number = updated_user.group_number
            if updated_user.middle_name is not None:
                user.middle_name = updated_user.middle_name
            if updated_user.gender is not None:
                user.gender = updated_user.gender
            if updated_user.roles is not None:  
                user.roles = updated_user.roles
            return "updated successfully"
    raise HTTPException(status_code=404, detail="User not found")
            