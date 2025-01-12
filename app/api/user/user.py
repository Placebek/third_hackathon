from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.user.commands.user_crud import update_user_data, delete_favorite_story, post_favorite_create, get_user_data
from app.api.user.schemas.response import StatusResponse, GetUserData
from app.api.user.schemas.create import FavoriteCreate, UserData, FavoriteDelete
from app.context.context import get_access_token
from app.database.db import get_db


router = APIRouter()

@router.post(
    '/favorite',
    summary="",
    response_model=StatusResponse
)
async def favorite(request: FavoriteCreate, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await post_favorite_create(request=request, access_token=access_token, db=db)

@router.delete(
    '/favorite',
    summary="",
    response_model=StatusResponse
)
async def favorite(request: FavoriteDelete, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await delete_favorite_story(favorite_id=request, access_token=access_token, db=db)


@router.get(
    '/profile',
    summary="",
    response_model=GetUserData
)
async def user(access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await get_user_data(db=db, access_token=access_token)


@router.patch(
    '/profile/update',
    summary="",
    response_model=StatusResponse
)
async def user(user_data: UserData, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await update_user_data(user_data=user_data, db=db, access_token=access_token)
