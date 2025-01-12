from pydantic import BaseModel
from typing import Optional, List, Dict, Union


class GetAuthorData(BaseModel):
    id: int
    name: str
    photo: str 
    bio: str


class GetAuthorDataAndThemFairyTails(BaseModel):
    id: int
    name: str
    photo: str 
    bio: str 
    fairy_tails: Optional[List[Dict[str, Union[str, int]]]] 





