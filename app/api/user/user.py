from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.user.commands.user_crud import update_user_data, delete_favorite_story, get_all_favorite_story, all_fairy_tails, post_favorite_create, get_user_data, one_fairy_tail
from app.api.user.schemas.response import StatusResponse, FairyTailsResponse, GetUserData, FairyTailsForReads
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


@router.get(
    "/stories", 
    summary="",
    response_model=List[FairyTailsResponse]
)
async def fairy_tails(
    db: AsyncSession = Depends(get_db),
    skip: int = 0, 
    limit: int = 100, 
):
    return await all_fairy_tails(db=db, limit=limit, skip=skip)

@router.get(
    "/stories/{id}", 
    summary="Айди бойынша ертегені алу",
    response_model=FairyTailsResponse
)
async def fairy_tails_by_id(
    id: int,  
    db: AsyncSession = Depends(get_db)  
):
    return await one_fairy_tail(db=db, fairy_tail_id=id) 


@router.get(
    "/stories/{id}/read", 
    summary="Ертегі оқу",
    response_model=FairyTailsForReads
)
async def fairy_tails_for_read(
    
    id: int,  
    db: AsyncSession = Depends(get_db)  
):
    return await one_fairy_tail(db=db, fairy_tail_id=id) 
