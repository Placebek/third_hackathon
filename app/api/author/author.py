from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.author.commands.author_crud import get_all_authors, get_author_data, get_author_data_and_them_fairy_tails
from app.api.author.schemas.response import GetAuthorData, GetAuthorDataAndThemFairyTails
from app.database.db import get_db


router = APIRouter()

@router.get(
    '/all',
    summary="Бүкіл ертегі жазушылар",
    response_model=List[GetAuthorData]
)
async def all_authors(db: AsyncSession = Depends(get_db)):
    return await get_all_authors(db=db)

@router.get(
    '/{id}/profile',
    summary="",
    response_model=GetAuthorDataAndThemFairyTails
)
async def profile_author(id: int, db: AsyncSession = Depends(get_db)):
    return await get_author_data_and_them_fairy_tails( author_id=id,db=db )


@router.get(
    '/{id}',
    summary="Ертегі жазушы туралы ақпарат",
    response_model=GetAuthorData
)
async def one_author_data(id: int ,db: AsyncSession = Depends(get_db)):
    return await get_author_data(id=id, db=db)



