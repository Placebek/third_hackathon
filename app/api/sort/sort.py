from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.user.commands.user_crud import update_user_data, delete_favorite_story, get_all_favorite_story, all_fairy_tails, post_fovorite_create, get_user_data
from app.api.user.schemas.response import StatusResponse, FairyTailsResponse, GetUserData
from app.api.user.schemas.create import FavoriteCreate, UserData, FavoriteDelete
from context.context import get_access_token
from database.db import get_db


router = APIRouter()


@router.post(
    '/filter',
    summary="",
    response_model=StatusResponse
)
async def favorite(request: FavoriteCreate, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await post_fovorite_create(request=request, access_token=access_token, db=db)


