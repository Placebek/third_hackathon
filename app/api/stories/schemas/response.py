from typing import Optional, List, Dict, Union
from pydantic import BaseModel

      

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
    title_kz: str
    subtitle: str
    subtitle_kz: str
    text: str
    text_kz: str
    prologue_kz: str
    story_reads: str
    age_category: str   

    class Config:
        from_attributes=True



