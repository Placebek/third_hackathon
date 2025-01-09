from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    age: int

class UserBase(BaseModel):
    email_or_username: str
    password: str
