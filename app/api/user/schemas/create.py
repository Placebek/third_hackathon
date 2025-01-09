from pydantic import BaseModel

class FavoriteCreate(BaseModel):
    user_id: int
    story_berries_id: int

class UserData(BaseModel):
    email: str | None
    age: str | None


class FavoriteDelete(BaseModel):
    id: int

