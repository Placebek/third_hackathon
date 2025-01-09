from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel



class CategoryStoryInfo(BaseModel):
    id: int
    name_category: str
    
    class Config:
        from_attributes = True
        

class FairyTailsResponse(BaseModel):
    id: int
    title: str
    subtitle: str
    initial_picture: str
    story_reads: str
    text: str
    category: List[CategoryStoryInfo]
    age_category: str
    author_name: str

    class Config:
        from_attributes=True


class StatusResponse(BaseModel):
    roles: str
    status_code: int
    status_msg: str


class GetUserData(BaseModel):
    id: int
    user_name: int
    email: str 
    age: str 





