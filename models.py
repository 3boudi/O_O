from pydantic import Field
from typing import Optional , List
from uuid import uuid4, UUID
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    
class Major(str, Enum):
    CS = "Computer engineering"
    IT = "Information Technology"
    EE = "Electrical Engineering"

class Speciality(str, Enum):
    AI = "Artificial Intelligence"
    DS = "Data Science"
    SE = "Software Engineering"
    
class User(BaseModel):
    #id: UUID = uuid4()
    id: UUID = Field(default_factory=uuid4)# for auto generation
    first_name: str
    last_name: str
    Bac_matrucule: int
    major: Major
    speciality: Speciality
    year_of_study: int
    section: int
    group_number: int
    middle_name: Optional[str]= None
    gender: Gender
    roles: List[Role]

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    Bac_matrucule: Optional[int] = None
    major: Optional[Major] = None
    speciality: Optional[Speciality] = None
    year_of_study: Optional[int] = None
    section: Optional[int] = None
    group_number: Optional[int] = None
    middle_name: Optional[str] = None
    gender: Optional[Gender] = None
    roles: Optional[List[Role]] = None

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    Bac_matrucule: int
    major: Major
    speciality: Speciality
    year_of_study: int
    section: int
    group_number: int
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]
