from datetime import datetime
from typing import Optional, List, Dict, Union
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
    category: Optional[List[Dict[str, Union[str, int]]]] 
    age_category: str   
    author_name: str

    class Config:
        from_attributes=True


class FairyTailsForReads(BaseModel):
    id: int
    title: str
    subtitle: str
    text: str
    story_reads: str
    category: Optional[List[Dict[str, Union[str, int]]]] 
    age_category: str   

    class Config:
        from_attributes=True




class StatusResponse(BaseModel):
    roles: str
    status_code: int
    status_msg: str


class GetUserData(BaseModel):
    id: int
    username: str
    email: str 
    age: int 





