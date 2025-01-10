from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    age: int

class UserBase(BaseModel):
    email_or_username: str
    password: str
