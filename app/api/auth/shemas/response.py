from datetime import datetime
from pydantic import BaseModel

    
class TokenResponse(BaseModel):
    access_token: str
    access_token_expire_time: datetime
    access_token_type: str = 'Bearer'

class TokenResponseLogin(BaseModel):
    access_token: str
    access_token_expire_time: datetime
    access_token_type: str = 'Bearer'