from pydantic import BaseModel

class StatusResponse(BaseModel):
    roles: str
    status_code: int
    status_msg: str


class GetUserData(BaseModel):
    id: int
    username: str
    email: str 
    age: int 





