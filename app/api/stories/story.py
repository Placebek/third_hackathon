from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.stories.commands.story_crud import all_fairy_tails, one_fairy_tail, one_fairy_tail_for_read
from app.api.stories.schemas.response import FairyTailsResponse, FairyTailsForReads
from app.database.db import get_db


router = APIRouter()

@router.get(
    "/all", 
    summary="Бүкіл ертегілер",
    response_model=List[FairyTailsResponse]
)
async def fairy_tails(
    db: AsyncSession = Depends(get_db),
    skip: int = 0, 
    limit: int = 100
):
    return await all_fairy_tails(db=db, limit=limit, skip=skip)

@router.get(
    "/{id}", 
    summary="Айди бойынша ертегені алу",
    response_model=FairyTailsResponse
)
async def fairy_tails_by_id(
    id: int,  
    db: AsyncSession = Depends(get_db)  
):
    return await one_fairy_tail(db=db, fairy_tail_id=id) 


@router.get(
    "/{id}/read", 
    summary="Ертегі оқу",
    response_model=FairyTailsForReads
)
async def fairy_tails_for_read(
    id: int,  
    db: AsyncSession = Depends(get_db)  
):
    return await one_fairy_tail_for_read(db=db, fairy_tail_id=id) 
