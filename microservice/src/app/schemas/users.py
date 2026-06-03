from pydantic import BaseModel,EmailStr,Field,ConfigDict
from typing import Optional

class UserBase(BaseModel):
    is_active: bool = True
    is_superuser:bool = False
    full_name: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr
    password: str = Field(min_length=5,max_length=72)

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserUpdate(UserCreate):
    pass
